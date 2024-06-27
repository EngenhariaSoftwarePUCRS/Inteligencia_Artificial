import requests
import unittest

from trabalho01 import TEM_JOGO, VELHA, X_GANHOU


API_URL = "http://localhost:8080"


class TestTicTacToaAPI(unittest.TestCase):
    
    def setUp(self):
        # Configuração inicial de cada teste
        self.base_url = API_URL


    def _test_board_successful(self,
                                board: str,
                                expected_output: dict[str, str],
                                expected_status_code: int = 200):
        response = requests.get(f"{self.base_url}/{board}")
        self.assertEqual(response.status_code, expected_status_code)
        response_data = dict(response.json())
        expected_key = list(expected_output.keys())[0]
        self.assertIn(expected_key, response_data.keys(), "Output key not found in response")
        self.assertEqual(
            response_data.get(expected_key),
            expected_output.get(expected_key),
            "Output value does not match expected value",
        )


    def test_game_state_endpoint_for_X_victory(self):
        # Caso de teste para verificar endpoint/{board}
        # Teste com um tabuleiro que resulta em X_GANHOU
        board = "O,O,X,O,X,O,X,O,X"
        expected_output = { "correctOutput" : X_GANHOU }
        return self._test_board_successful(board, expected_output)


    def test_game_state_endpoint_for_has_game(self):
        # Teste com um tabuleiro com result TEM_JOGO
        board = "X,b,b,b,X,b,O,b,O"
        expected_output = { "correctOutput": TEM_JOGO }
        return self._test_board_successful(board, expected_output)


    def test_game_state_endpoint_for_tie(self):
        # Teste com um tabuleiro com result VELHA
        board = "X,O,X,O,X,O,O,X,O"
        expected_output = { "correctOutput": VELHA }
        return self._test_board_successful(board, expected_output)


    def test_game_state_endpoint_for_invalid_board(self):
        # Teste com um tabuleiro inválido (não possui 9 células)
        board = "O,O,X,O,X,O,X,O"
        expected_output = {"detail": "Invalid board size"}
        response = requests.get(f"{self.base_url}/{board}")
        self.assertEqual(response.status_code, 400)
        response_data = dict(response.json())
        self.assertEqual(response_data, expected_output)


if __name__ == "__main__":
    try:
        requests.options(API_URL)
        unittest.main()
    except requests.exceptions.ConnectionError:
        # Italics and bold red
        print("\033[3m", "\033[1;31m")
        print("API is not running.")
        # Yellow
        print("\033[33m", end="")
        print("Please start the API before running the tests.")
        print("To start the API, run 'python main.py' in the terminal.")
        print("\033[0m")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
