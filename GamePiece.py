# Feel free to add pieces to your hearts content!
from enum import Enum, auto


class GamePiece(Enum):
    Floor = auto()
    Player = auto()
    Wall = auto()
    Box = auto()


piece_colors = {
    GamePiece.Floor: (255, 255, 255),
    GamePiece.Player: (120, 30, 20),
    GamePiece.Wall: (30, 10, 10),
    GamePiece.Box: (210, 170, 20)
}
