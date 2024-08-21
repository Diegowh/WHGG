from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import backend.database.schemas as schemas
from backend.core.data_manager import DataManager
from backend.database.database import get_db

router = APIRouter()

@router.get("/lol/profile/{server}/{game_name}-{tag_line}/", response_model=schemas.Response)
def get_account(
    server: str, 
    game_name: str, 
    tag_line: str, 
    db: Session = Depends(get_db),
    data_manager: DataManager = Depends(DataManager)
):
    return data_manager.get(
        db=db,
        request=schemas.Request(
            riot_id=schemas.RiotId(
                game_name=game_name,
                tag_line=tag_line
            ),
            server=schemas.RiotServer(
                name=server
            )
        )
    )