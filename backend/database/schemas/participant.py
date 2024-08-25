'''
Este módulo contiene varias DTOs que extienden de `pydantic.BaseModel`, responsables de
manejar los datos relacionados con `models.Participant`.
'''
from pydantic import BaseModel


class ParticipantBase(BaseModel):
    """Clase base para representar la información de un participante en una partida."""

    champion_id: int
    champion_name: str
    riot_id_game_name: str
    riot_id_tagline: str
    team_id: int
    team_position: str

class ParticipantCreate(ParticipantBase):
    """DTO para representar los datos necesarios para crear una nueva instancia de
    `models.Participant`
    """


class Participant(ParticipantBase):
    """DTO para representar un participante en un partido
    
    Se utiliza para transportar los datos obtenidos de una instancia de `models.Participant`
    """
    id: int
    match_id: int

    model_config = {
        "from_attributes": True
    }
