from teste import Teste
import unittest


class Uni(unittest.TestCase):
    """
    Teste unitário do cadastro de produtos no sistema Omie.
    """
 
    def test_cadastro_suesso(self):
        """
        Testa o cadastro bem-sucedido de um produto.

        O teste envia os dados de um produto válido para o método de cadastro
        e verifica se o resultado é uma mensagem de sucesso.
        """        
        dicionario = {
            "codigo_produto": 2827787449,
            "nome_produto": "teste unitario",
            "ncp": "1905.90.90",
            "valor_produto": 152,
            "unidade": "UND",
            "codigo_integracao": "p697087",
            
    }
        
        dados = Teste()
        valor = dados.incluir_produto(dicionario)        
        self.assertEqual(valor, 'Produto cadastrado com sucesso')

    
    def test_cadastro_falho(self):
        """"
        Testa o cadastro mal-sucedido de um produto.

        O teste envia os dados de um produto inválido (mesmos dados do teste de sucesso)
        para o método de cadastro e verifica se o resultado é uma mensagem de falha.
        """       

        dicionario = {
            "codigo_produto": 2827787449,
            "nome_produto": "teste unitario",
            "ncp": "1905.90.92",
            "valor_produto": 152,
            "unidade": "UND",
            "codigo_integracao": "p697087",          
    }
        
        dados = Teste()
        valor = dados.incluir_produto(dicionario)        
        self.assertEqual(valor, 'Não Foi possivel cadastrar produto')

