from app.models.grupoInv import GrupoInvestigacion
from app.repository.grupoInv_repo import GrupoInvRepository

class GrupoInvService:
    
    def __init__(self, grupo_inv_repo):
        self.grupo_inv_repo = GrupoInvRepository()
    
    def cargar_lista_grupos_inv(self):
        return self.grupo_inv_repo.cargar_lista_grupos_inv()
    
    def obtener_grupos_inv_id(self):
        grupos_inv = self.grupo_inv_repo.get_grupo_inv_by_id()
        if not grupos_inv:
            raise ValueError("No se encontraron grupos de investigación")
        return grupos_inv
    
    def crear_grupo_inv(self, grupo_inv: GrupoInvestigacion):
        if not grupo_inv.nombre or grupo_inv.nombre.strip() == "":
            raise ValueError("El nombre del grupo de investigación es obligatorio")
        return self.grupo_inv_repo.create_grupo_inv(grupo_inv)