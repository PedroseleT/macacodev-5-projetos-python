"""ViaCEP oficial, sem chave; formatos são validados antes e depois do HTTP."""

import json
import re
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


class CepNaoEncontrado(ValueError):
    """CEP tem oito dígitos, mas não foi encontrado pelo serviço."""


def normalizar_cep(cep):
    if not isinstance(cep, str) or not re.fullmatch(r"[0-9]{5}-?[0-9]{3}", cep.strip()):
        raise ValueError("CEP deve ter oito dígitos, com ou sem hífen: 01001-000.")
    return cep.strip().replace("-", "")


def interpretar_resposta(dados):
    if not isinstance(dados, dict):
        raise ValueError("O serviço não retornou um objeto JSON.")
    if dados.get("erro") in (True, "true"):
        raise CepNaoEncontrado("CEP não encontrado.")
    campos = ("cep", "logradouro", "bairro", "localidade", "uf")
    if any(not isinstance(dados.get(campo), str) for campo in campos):
        raise ValueError("Resposta incompleta ou com tipos inesperados.")
    resultado = {campo: dados[campo].strip() for campo in campos}
    normalizar_cep(resultado["cep"])
    if not resultado["localidade"] or not re.fullmatch(r"[A-Z]{2}", resultado["uf"]):
        raise ValueError("Cidade ou estado inválido na resposta.")
    return resultado


def consultar(cep, abrir=None):
    """abrir é substituível por um simulador nos testes; o padrão usa urllib."""
    normalizado = normalizar_cep(cep)
    url = f"https://viacep.com.br/ws/{normalizado}/json/"
    try:
        with (abrir or urlopen)(url, timeout=10) as resposta:
            if resposta.status != 200:
                raise ValueError("Serviço retornou um status HTTP inesperado.")
            conteudo = resposta.read(1_000_001)
        if len(conteudo) > 1_000_000:
            raise ValueError("Resposta maior que o limite de segurança.")
        dados = json.loads(conteudo.decode("utf-8"))
    except HTTPError as erro:
        raise ValueError(
            f"Serviço indisponível: HTTP {erro.code}. Tente depois."
        ) from erro
    except (URLError, TimeoutError) as erro:
        raise ValueError(
            "Falha de conexão ou tempo esgotado. Tente novamente."
        ) from erro
    except (json.JSONDecodeError, UnicodeError) as erro:
        raise ValueError("Serviço retornou JSON inválido.") from erro
    endereco = interpretar_resposta(dados)
    if normalizar_cep(endereco["cep"]) != normalizado:
        raise ValueError("Resposta não corresponde ao CEP consultado.")
    return endereco
