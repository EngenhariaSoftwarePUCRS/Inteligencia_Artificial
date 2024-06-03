from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from trabalho01 import get_game_state


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
        return {"error": "Invalid board size"}
    for i in range(9):
        if board[i] in ["-1", "0", "1"]:
            board[i] = int(board[i])
        else:
            board[i] = board[i].lower()
    try:
        return {
            "kNN": get_game_state(board, "kNN"),
            "MLP": get_game_state(board, "MLP"),
            "DTree": get_game_state(board, "DTree"),
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8080)
