from pydantic import BaseModel

class ParticipantBase(BaseModel):

    champion_id: int
    champion_name: str
    riot_id_game_name: str
    riot_id_tagline: str
    team_id: int
    team_position: str

class ParticipantCreate(ParticipantBase):
    pass


class Participant(ParticipantBase):
    id: int
    match_id: int

    model_config = {
        "from_attributes": True
    }