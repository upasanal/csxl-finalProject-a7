from pydantic import BaseModel


class CircleTable(BaseModel):
    id: int
    cx: str
    cy: str
    radius: str
    fill: str | None
