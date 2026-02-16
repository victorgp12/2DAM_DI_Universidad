from PySide6.QtWidgets import QWidget, QMessageBox
from app.view.ProyectoPage_ui import Ui_Proyecto_page
from app.repository.proyecto_repo import ProyectoRepository
from app.service.proyecto_service import ProyectoService

class ProyectoPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Proyecto_page()
        self.ui.setupUi(self)
        
        # Inicialización de clases
        self.proyecto_repo = ProyectoRepository()
        self.proyecto_service = ProyectoService(self.proyecto_repo)
        
        # Inicializando métodos
        #self.cargar_datos()
        
        
        
    def cargar_datos(self):
        # MODIFICAR poner SERVICE Y CARGAR en tabla
        datos = self.proyecto_repo.obtener_todos()
        print(f"Datos {datos}")