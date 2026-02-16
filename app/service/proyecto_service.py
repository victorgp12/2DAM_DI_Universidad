from app.models.proyecto import Proyecto

class ProyectoService:
    
    def __init__(self, proyecto_repo):
        self.proyecto_repo = proyecto_repo