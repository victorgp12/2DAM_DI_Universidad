from app.data.db import get_connection
from app.models.grupoInv import GrupoInvestigacion

class GrupoInvRepository:
    
    def cargar_lista_gruposInv(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT g.id_grupo, g.nombre FROM grupo_investigacion g")
        datos = cursor.fetchall()
        cursor.close()
        return datos
    
    def get_all_grupos_investigacion(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM grupo_investigacion")
        rows = cursor.fetchall()
        conn.close()
        return [GrupoInvestigacion(id=row[0], id_grupoInv=row[1], nombre=row[2], descripcion=row[3], fecha_creacion=row[4]) for row in rows]
    
    def delete_grupoInv(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM grupo_investigacion WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def update_facultad(self, grupo_inv):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE grupo_investigacion
            SET id_grupoInv = ?, nombre = ?, descripcion = ?, fecha_creacion = ?
            WHERE id = ?
        """, (grupo_inv.id_universidad, grupo_inv.id_grupoInv, grupo_inv.nombre, grupo_inv.descripcion, grupo_inv.fecha_creacion, grupo_inv.id))
        conn.commit()
        conn.close()

    def get_grupoInv_by_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM grupo_investigacion WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return GrupoInvestigacion(id=row[0], id_grupoInv=row[1], nombre=row[2], descripcion=row[3], fecha_creacion=row[4])
        return None