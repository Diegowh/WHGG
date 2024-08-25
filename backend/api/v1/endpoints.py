'''
Módulo que define un router de FastAPI para gestionar las solicitudes HTTP GET 
relacionadas con las solicitudes de perfil de usuario de League of Legends
'''

from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from backend.database import schemas
from backend.core.data_manager import DataManager
from backend.database.database import get_db

router = APIRouter()

@router.get("/lol/profile/{server}/{game_name}-{tag_line}/", response_model=schemas.Response | schemas.ResponseError)
def get_account(
    server: str,
    game_name: str,
    tag_line: str,
    db: Session = Depends(get_db),
    data_manager: DataManager = Depends(DataManager)
):
    """Obtiene el perfil de un usuario de League of Legends mediante el Riot ID y el servidor.

    Args:
        server (str): Nombre del servidor de League of Legends. Ej: EUW, NA, KR, etc.
        game_name (str): Nombre de invocador del usuario (Parte previa al # del Riot ID)
        tag_line (str): Etiqueta del usuario (Parte posterior al # del Riot ID)
        db (Session, optional): Sesión de base de datos.
        data_manager (DataManager, optional): Instancia de DataManager.

    Returns:
        schemas.Response: Objeto que contiene la información solicitada del perfil de usuario.
    """
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


FAVICON_PATH = 'favicon.ico'
@router.get('/favicon.ico', include_in_schema=False)
async def favicon():
    """API favicon"""
    return FileResponse(FAVICON_PATH)
