from pydantic import BaseModel


class RectangleTable(BaseModel):
    id: int
    x: str
    y: str
    width: str
    height: str
    fill: str | None
