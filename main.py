import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "mi app"
    texto  = ft.Text("Mi primera app con Felt")
    texto2 = ft.Text("Este es un ejemplo para mi para mostrar otro texto")

    
    def cambiar_texto(e):
        texto2.value = "Modificacion de Texto"
        page.update()
    
    boton = ft.FilledButton(text="Cambiar Texto",on_click=cambiar_texto)
    page.add(texto)
    page.add(texto2)
    page.add(boton)




ft.app(target=main)
