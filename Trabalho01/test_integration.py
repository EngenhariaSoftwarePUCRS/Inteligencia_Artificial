import requests
import unittest

class TestTicTacToaAPI(unittest.TestCase):
    
    def setUp(self):
        # Configuração inicial de cada teste
        self.base_url = "http://localhost:4200"

    def test_game_state_endpoint(self):
        # Caso de teste para verificar endpoint/{board}
        # Teste com um tabuleiro que resulta em X_GANHOU
        board = "-1,-1,1,-1,1,-1,1,-1,1"
        expected_output = {
            "correctOutput" : "X_GANHOU",
            "kNN": "X_GANHOU",
            "MLP": "X_GANHOU",
            "DTree": "X_GANHOU",
        }

        response = requests.get(f"{self.base_url}/{board}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_output)

        # Teste com um tabuleiro com result TEM_JOGO
        board = "0,0,-1,1,-1,1,-1,1,-1"
        expected_output = {
            "correctOutput": "TEM_JOGO",
            "kNN": "TEM_JOGO",
            "MLP": "TEM_JOGO",
            "DTree": "TEM_JOGO"
        }

        response = requests.get(f"{self.base_url}/{board}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_output)

        # Teste com um tabuleiro com result VELHA
        board = "1,-1,1,-1,1,-1,-1,1,-1"
        expected_output = {
            "correctOutput": "VELHA",
            "kNN": "VELHA",
            "MLP": "VELHA",
            "DTree": "VELHA"
        }

        response = requests.get(f"{self.base_url}/{board}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_output)

        # Teste com um tabuleiro inválido (não possui 9 células)
        board = "-1,-1,1,-1,1,-1,1,-1"
        expected_output = {"error": "Invalid board size"}

        response = requests.get(f"{self.base_url}/{board}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), expected_output)


if __name__ == "__main__":
    unittest.main()
