from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from trabalho01 import (
    CELL_B, CELL_O, CELL_X,
    O_GANHOU, TEM_JOGO, VELHA, X_GANHOU,
    get_game_state, has_won, to_cell,
)


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/{board}")
def main(board: str):
    board = board.split(",")
    if len(board) != 9:
        raise HTTPException(status_code=400, detail="Invalid board size")
    for i in range(9):
        if board[i] in ["-1", "0", "1"]:
            board[i] = int(board[i])
        else:
            board[i] = board[i].lower()

    board_cells = [to_cell(cell) for cell in board]
    if has_won(CELL_X, board_cells):
        correct_output = X_GANHOU
    elif has_won(CELL_O, board_cells):
        correct_output = O_GANHOU
    elif CELL_B in board_cells:
        correct_output = TEM_JOGO
    else:
        correct_output = VELHA

    try:
        return {
            "correctOutput": correct_output,
            "kNN": get_game_state(board, "kNN"),
            "MLP": get_game_state(board, "MLP"),
            "DTree": get_game_state(board, "DTree"),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8080)
