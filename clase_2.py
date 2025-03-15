import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "Mi App mejorada con filas y columnas"

    texto1 = ft.Text("Texto 1", size=24, color=ft.colors.WHITE)
    texto2 = ft.Text("Texto 2", size=24, color=ft.colors.WHITE)
    texto3 = ft.Text("Texto 3", size=24, color=ft.colors.WHITE)

    fila_texto1 = ft.Row(
        controls=[texto1,texto2,texto3],
        alignment= ft.MainAxisAlignment.CENTER,
        spacing=50
    )
    page.add(fila_texto1)

    boton1 = ft.FilledButton(text="Boton 1")
    boton2 = ft.FilledButton(text="Boton 2")
    boton3 = ft.FilledButton(text="Boton 3")

    fila_texto2 = ft.Row(
        controls=[boton1,boton2,boton3],
        alignment= ft.MainAxisAlignment.CENTER,
        spacing=50
    )
    page.add(fila_texto2)
    
    textos_columnas1 = [
        ft.Text("Columna 1 -Fila 1", size=18, color= ft.colors.WHITE),
        ft.Text("Columna 1 -Fila 2", size=18, color= ft.colors.WHITE),
        ft.Text("Columna 1 -Fila 3", size=18, color= ft.colors.WHITE)
    ]

    columna_texto1 = ft.Column(
        controls=textos_columnas1,
        alignment= ft.MainAxisAlignment.CENTER,
    )

    textos_columnas2 = [
        ft.Text("Columna 2 -Fila 1", size=18, color= ft.colors.WHITE),
        ft.Text("Columna 2 -Fila 2", size=18, color= ft.colors.WHITE),
        ft.Text("Columna 2 -Fila 3", size=18, color= ft.colors.WHITE)
    ]

    columna_texto2 = ft.Column(
        controls=textos_columnas2,
        alignment= ft.MainAxisAlignment.CENTER,
     
    )
    fila_columnas = ft.Row(
        controls=[columna_texto1,columna_texto2],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )
    page.add(fila_columnas)


ft.app(target=main)