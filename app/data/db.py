import sqlite3
import os
import sys

def _get_db_path():
    if getattr(sys, 'frozen', False):  # Es EXE de PyInstaller
        # PyInstaller extrae archivos a _MEIPASS
        base_dir = sys._MEIPASS
    else:
        # Desarrollo: directorio del proyecto (padre del actual)
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    return os.path.join(base_dir, "universidad.db")

def get_connection():
    db_path = _get_db_path()
    print("Usando BD:", db_path)
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"BD no encontrada: {db_path}")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row 
    return conn
