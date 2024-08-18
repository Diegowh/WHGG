from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database.database import get_db
from backend.core.data_manager import DataManager
from backend.api.v1.schemas import ResponseDto, Request, RiotIdDto, RiotServerDto

router = APIRouter()

@router.get("/lol/profile/{server}/{game_name}-{tag_line}/", response_model=ResponseDto)
def get_account(
    server: str, 
    game_name: str, 
    tag_line: str, 
    db: Session = Depends(get_db),
    data_manager: DataManager = Depends(DataManager)
):
    return data_manager.get(
        db=db,
        request=Request(
            riot_id=RiotIdDto(
                game_name=game_name,
                tag_line=tag_line
            ),
            server=RiotServerDto(
                name=server
            )
        )
    )