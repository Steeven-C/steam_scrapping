from pydantic import BaseModel
from typing import List, Optional


class Game(BaseModel):
    name: str
    evaluation: str
    

