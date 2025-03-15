import flet as ft
from openpyxl import Workbook
from datetime import datetime


def main(page: ft.Page):
    def guardar_excel(e):
        wb = Workbook()
        ws = wb.active
        ws.title = "Datos de la Tabla"
        ws.append(["ID","Nombre","Edad"])
        for row in data_table.rows:
            ws.append([cell.content.value for cell in row.cells])

            fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = f"datos_tabla_{fecha_hora}.xlsx"
            wb.save(nombre_archivo)
            snack_bar = ft.SnackBar(content=ft.Text(f"Datos guardados en {nombre_archivo}"))
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()




    def agregar_filas(e):
        print("entro Boton")
        nueva_fila = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(len(data_table.rows)+1),color=ft.Colors.WHITE)),
                ft.DataCell(ft.Text(nombre_input.value,color=ft.Colors.WHITE)),
                ft.DataCell(ft.Text(edad_input.value,color=ft.Colors.WHITE)),
            ]
        )
        data_table.rows.append(nueva_fila)
        nombre_input.value = ""
        edad_input.value = ""
        page.update()
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 1000  # Ancho inicial
    page.window.height = 600  # Alto inicial
   
    page.window.resizable = False  # Permitir que el usuario redimensione la ventana
    page.padding= 10
    page.theme_mode = "light"
    page.update()
    page.title = "DataTable en Flet con Excel"
    texto  = ft.Text("DataTable en Flet", weight=ft.FontWeight.BOLD ,size=30,color=ft.Colors.WHITE)
    
    data_table = ft.DataTable(
        bgcolor=ft.Colors.BLUE_GREY_700,
        border=ft.border.all(width=2,color=ft.Colors.BLUE_GREY_200),
        border_radius=10,
        vertical_lines=ft.BorderSide(1,ft.Colors.BLUE_200),
        horizontal_lines=ft.BorderSide(1,ft.Colors.BLUE_GREY_400),
        columns=[
            ft.DataColumn(ft.Text("ID",color=ft.Colors.BLUE_GREY_200)),
            ft.DataColumn(ft.Text("Nombre",color=ft.Colors.BLUE_GREY_200)),
            ft.DataColumn(ft.Text("Edad",color=ft.Colors.BLUE_GREY_200)),
        ],
        rows=[]
    )
    nombre_input = ft.TextField(label="Nombre",
                                bgcolor=ft.Colors.BLUE_GREY_700,color=ft.Colors.WHITE)
    edad_input = ft.TextField(label="Edad",
                                bgcolor=ft.Colors.BLUE_GREY_700,color=ft.Colors.WHITE)
    agregar_boton = ft.ElevatedButton("Agregar",on_click=agregar_filas,color=ft.Colors.WHITE,bgcolor=ft.Colors.BLUE) 
    guardar_excel_boton = ft.ElevatedButton("Guardar en Excel",on_click=guardar_excel,color=ft.Colors.WHITE,bgcolor=ft.Colors.GREEN) 
    input_container = ft.Row(
        controls=[nombre_input,edad_input,agregar_boton,guardar_excel_boton],
        alignment=ft.MainAxisAlignment.CENTER
    )
    page.add(texto,data_table,input_container,)


ft.app(target=main)