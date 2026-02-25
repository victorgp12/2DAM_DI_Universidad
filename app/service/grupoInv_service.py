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
    
    def eliminar_grupo_inv(self, id_grupo_inv):
        grupo_inv_existente = self.grupo_inv_repo.get_grupo_inv_by_id(id_grupo_inv)
        if not grupo_inv_existente:
            raise ValueError("Grupo de investigación no encontrado")
        return self.grupo_inv_repo.delete_grupo_inv(id_grupo_inv)
    
    def actualizar_grupo_inv(self, id_grupo_inv, grupo_inv: GrupoInvestigacion):
        grupo_inv_existente = self.grupo_inv_repo.get_grupo_inv_by_id(id_grupo_inv)
        if not grupo_inv_existente:
            raise ValueError("Grupo de investigación no encontrado")
        if not grupo_inv.nombre or grupo_inv.nombre.strip() == "":
            raise ValueError("El nombre del grupo de investigación es obligatorio")
        return self.grupo_inv_repo.update_grupo_inv(grupo_inv)
    
    def obtener_grupo_inv_por_id(self, id_grupo_inv):
        grupo_inv = self.grupo_inv_repo.get_grupo_inv_by_id(id_grupo_inv)
        if not grupo_inv:
            raise ValueError("Grupo de investigación no encontrado")
        return grupo_inv