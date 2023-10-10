import requests
import json
from requests import request


#NOTE - Credenciais
app_key = "api key"
app_secret = "api secret"
endpoint_incluir_produtos = "https://app.omie.com.br/api/v1/geral/produtos/"
endpoint_listar_familias = "https://app.omie.com.br/api/v1/geral/familias/"


class Teste():
    def incluir_produto(self,dic_produtos):
        """
        Função responsável pelo cadastro de produtos no sistema Omie.
        Parâmetros:
            - Dicionário contendo dados dos produtos.
        Returns:
            - response.json()
        """
        payload = json.dumps({
        'call': 'IncluirProduto',
        'app_key': app_key,
        'app_secret': app_secret,
        'param': [
            {   
                "codigo": dic_produtos["codigo_produto"],
                "descricao": dic_produtos["nome_produto"],
                "ncm": dic_produtos["ncp"],
                "valor_unitario": dic_produtos["valor_produto"],
                "unidade": "UND",
                "codigo_produto_integracao": dic_produtos["codigo_integracao"],
           
            }
        ]
        })
        headers = {
            'Content-Type': 'application/json'
        }


        response = request(method='POST', url=endpoint_incluir_produtos, headers=headers, data=payload)
        print(response.json())
        if response.status_code == 200:
         
            return 'Produto cadastrado com sucesso'
        else:
            return'Não Foi possivel cadastrar produto'
        
