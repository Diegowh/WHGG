'''
Este módulo contiene varias DTOs que extienden de `pydantic.BaseModel`, responsables de
manejar los datos relacionados con la solicitud entrante de la API Gateway.
'''

from typing import Optional

from pydantic import BaseModel, field_validator, model_validator



server_mappings: dict[str, tuple[str, str]] = {
    "NA": ("americas", "na1"),
    "EUW": ("europe", "euw1"),
    "EUNE": ("europe", "eun1"),
    "OCE": ("sea", "oc1"),
    "KR": ("asia", "kr1"),
    "JP": ("asia", "jp1"),
    "BR": ("americas", "br1"),
    "LAN": ("americas", "la1"),
    "LAS": ("americas", "la2"),
    "RU": ("europe", "ru"),
    "TR": ("europe", "tr1"),
    "SG": ("sea", "sg2"),
    "PH": ("sea", "ph2"),
    "TW": ("sea", "tw2"),
    "VN": ("sea", "vn2"),
    "TH": ("sea", "th2"),
}

class RiotServer(BaseModel):
    """Esta clase es un DTO que valida los datos de un servidor de Riot Games
    """
    name: str
    platform: Optional[str] = None
    region: Optional[str] = None


    @field_validator('name')
    @classmethod
    def validate_name(cls, v: str) -> str:
        """Valida que el name del `RiotServer` esté dentro de los servidores válidos
        y lo convierte a mayúsculas."""
        v = v.upper()
        if v not in server_mappings:
            raise ValueError(f"'{v}' is not a valid server name.")
        return v

    @model_validator(mode='after')
    def set_platform_and_region(self):
        """
        Asigna los valores de `platform` y `region` basados en el `name` del servidor.
        
        Este método se llama automáticamente después de la validación del campo ´name´,
        para configurar los atributos `platform` y `region`en función del nombre del 
        servidor proporcionado.
        Utiliza el diccionario `server_mappings` para mapear el nombre
        del servidor a su plataforma y región correspondientes.
        
        Ejemplo:
            Si `name` es 'EUW', `platform` se establece en 'europe' y `region` en 'euw1'.
            
        Returns:
            RiotServer: La instancia de `RiotServer` con los atributos 
            `platform` y `region` actualizados.
        """
        server_name = self.name
        if server_name:
            region, platform = server_mappings[server_name]
            self.region = region
            self.platform = platform
        return self


class RiotId(BaseModel):
    """Esta clase es un DTO que valida los datos de un Riot ID"""
    game_name: str
    tag_line: str


    @field_validator('game_name')
    @classmethod
    def validate_game_name(cls, v: str) -> str:
        """Valida que el `game_name` del Riot ID cumpla con los requerimientos
        de longitud y tipo de caracteres establecido por Riot Games.
        """
        if not 3 <= len(v) <= 16:
            raise ValueError("game_name must be between 3 and 16 characters long.")
        if not v.isalnum():
            raise ValueError("game_name must contain only alphanumeric characters.")
        return v


    @field_validator('tag_line')
    @classmethod
    def validate_tag_line(cls, v: str) -> str:
        """Valida que el `tag_line` del Riot ID cumpla con los requerimientos
        de longitud y tipo de caracteres establecido por Riot Games.
        """
        if not 3 <= len(v) <= 5:
            raise ValueError('tag_line must be between 3 and 5 characters long.')
        if not v.isalnum():
            raise ValueError('tag_line must contain only alphanumeric characters.')
        return v


class Request(BaseModel):
    """Esta clase es un DTO que valida una peticion entrante de la API Gateway

    Attrs:
        riot_id (RiotId): DTO que representa un Riot ID.
        server (RiotServer): DTO que contiene los datos de un servidor de League of Legends
    """
    riot_id: RiotId
    server: RiotServer
