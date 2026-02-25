from app.models.grupoInv import GrupoInvestigacion
from app.repository.grupoInv_repo import GrupoInvRepository

class GrupoInvService:
    
    def __init__(self, grupo_inv_repo):
        self.grupo_inv_repo = grupo_inv_repo
    
    def cargar_lista_grupos_inv(self):
        return self.grupo_inv_repo.cargar_lista_gruposInv()