# Trabalho 01 - Tic Tac Toe com ML

## Integrantes

### Professora

- Silvia Moraes

### Alunos

- Augusto Baldino
- Felipe Freitas
- Isabela Kuser
- Luiza Heller
- Maria Eduarda Maia
- Paola Lopes

## Relatório

O relatório do projeto está disponível em [Relatório.pdf](Relatório.pdf). Recomenda-se a leitura do relatório para entender o processo de desenvolvimento do projeto e escolhas feitas, além de resultados obtidos.

## Como utilizar o projeto

### Front-End

O projeto conta com uma interface web simples para permitir a interação com o modelo de Machine Learning por meio de um tabuleiro de jogo da velha interativo. Conforme explicado no relatório, o front-end utilizado já havia sido desenvolvido previamente e está disponível em https://tictactowpwaangular01.web.app/.

**Observação:** O Front-End espera que o Back-End esteja rodando localmente na porta `8080`.

Alternativamente, se por qualquer motivo o front-end não estiver disponível, é possível baixar e executar o projeto localmente seguindo as instruções abaixo.

Clone o repositório do front-end com o comando abaixo:

```bash
git clone https://github.com/felipefreitassilvalearning/TicTacToePWA.git
```

Acesse a pasta do projeto com o comando abaixo:

```bash
cd TicTacToePWA
```

Instale as dependências do projeto com o comando abaixo:

```bash
npm install
```

Execute o projeto com o comando abaixo:

```bash
npm run start
```

Acesse o projeto em http://localhost:4200/.

### Back-End | Pré-requisitos

O projeto foi testado com Python 3.10.14 em ambientes Windows utilizando o [MiniConda](https://docs.conda.io/en/latest/miniconda.html). Outras versões do Python, sistemas operacionais e gerenciadores de pacotes podem não funcionar corretamente.

### Back-End | Instalação dos Requisitos

Após instalado o MiniConda, crie um ambiente virtual com o comando abaixo:

```bash
conda create -n ia-trabalho01 python=3.10.14
```

Ative o ambiente virtual com o comando abaixo:

```bash
conda activate ia-trabalho01
```

#### Alternativa - Sem (Mini)Conda

```sh
python -m venv ia-trabalho01
```

Windows
```sh
ia-trabalho01\Scripts\activate
```

Para instalar os requisitos do projeto, execute o comando abaixo:

```bash
pip install -r requirements.txt
```

### Back-End | Execução do Projeto

Para executar o projeto, execute o comando abaixo:

É importante que o ambiente virtual esteja ativado e que a porta `8080` esteja disponível.

```bash
python main.py
```

Acesse o projeto em http://localhost:8080/.

### Back-End | CLI

Se por qualquer motivo o front-end não estiver disponível, ou se desejar testar o back-end sem o front-end, é possível realizar requisições diretamente pelo terminal ou mesmo por algum navegador ou ferramenta de requisições HTTP (Postman, Insomnia, etc).

A API possui um único endpoint `/{board}` que recebe um tabuleiro de jogo da velha separado por vírgulas. O tabuleiro deve conter 9 posições, sendo `x` ou `1` para o jogador 1, `o` ou `-1` para o jogador 2 e `b` ou `0` para posições vazias.

Exemplo de requisição válida para `O Venceu` (parametros `estranhos` para testar entradas da API):

```bash
curl http://localhost:8080/X,b,O,x,1,o,-1,X,O
```

Em um último cenário, pode-se abrir o arquivo `trabalho01.py` e executar o código diretamente no terminal, alterando o "`game_state`" de teste da linha 377, por meio do comando `python trabalho01.py`.

## Como testar

Para testar o projeto, execute o comando abaixo:
Observação: O projeto deve estar rodando localmente na porta `8080`.

```bash
python test_integration.py
```

## Arquivos do Projeto

### data Folder

- `data/`: Contém os arquivos de dados utilizados no projeto.
- `data/Index`, `data/tic-tac-toe.data`, `data/tic-tac-toe.names`: Arquivos de dados do jogo da velha baixados diretamente do [repositório da UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/101/tic+tac+toe+endgame).
- `data/tic-tac-toe-minimum.data`: Arquivo de dados do jogo da velha com apenas 16 instâncias de cada classe.
- `data/tic-tac-toe-full.data`: Arquivo de dados do jogo da velha com todos os dados utilizados.

### requirements.txt

Arquivo contendo as dependências do projeto.

### main.py

Script principal do projeto. Contém uma API simples utilizando [FastAPI](https://fastapi.tiangolo.com/) que permite a integrar o modelo de Machine Learning com uma interface web.

### trabalho01.py

Script que contém as funções utilizadas para treinar o modelo de Machine Learning e realizar as predições. Foi gerado a partir do notebook `Trabalho01.ipynb`.

### Trabalho01.ipynb

Notebook utilizado para desenvolver o modelo de Machine Learning por meio da plataforma [Google Colab](https://colab.research.google.com/).

### test_integration.py

Script de testes de integração que verifica se a API está funcionando corretamente.
