from pydantic import BaseModel
from typing import List, Optional


class Game(BaseModel):
    game_name: str
    evaluation: str
    

