import flet as ft
import random


def main(page: ft.Page):
    def create_example(title,description,content):
        return ft.Container(
            content=ft.Column([
                ft.Text(title,size=24,weight=ft.FontWeight.BOLD,color=ft.Colors.BLUE_200),
                ft.Text(description,color=ft.Colors.GREY_300),
                ft.Container(content=content,padding=10,border=ft.border.all(1,ft.Colors.BLUE_GREY_400))
            ]),
            margin=ft.margin.only(bottom=20)
        )
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.window.width = 800  # Ancho inicial
    page.window.height = 600  # Alto inicial
   
    page.window.resizable = False  # Permitir que el usuario redimensione la ventana
    page.padding= 10
    page.title = "Stack,Image y CircleAvatar en Flet"
    page.theme_mode = ft.ThemeMode.DARK
    #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    texto  = ft.Text("Demostracion de Stack,Image y CircleAvatar en Flet", weight=ft.FontWeight.BOLD ,size=30)
    page.scroll = "always"

    stack_ejemplo = ft.Stack([
        ft.Container(width=200,height=200,bgcolor=ft.Colors.BLUE_900),
        ft.Container(width=150,height=150,bgcolor=ft.Colors.BLUE_700,left=25,top=25),
        ft.Container(width=100,height=100,bgcolor=ft.Colors.BLUE_500,left=50,top=50),
        ft.Text("Stack Demo",color=ft.Colors.WHITE,size=12,left=70,top=90)
    ],width=200,height=200)
    
    stack_example = create_example("Stack","Stack nos permite superponer widgets uno encima de otro",stack_ejemplo)
    imagen_internet = ft.Image(src="https://assets.nintendo.com/image/upload/f_auto/q_auto/dpr_1.5/ncom/en_US/games/switch/n/new-super-mario-bros-u-deluxe-switch/description-image",width=200)
    imagen_local = ft.Image(src="images/montana.png",width=200)
    columna_imagen= ft.Column([
        imagen_internet,
        ft.Text("Imagen desde Url",size=14,color=ft.Colors.GREEN_300),
        imagen_local,
        ft.Text("Imagen local (si esta disponible)",size=14,color=ft.Colors.GREY_300)
    ])
    imagen_example = create_example("Image","Image Permite mostrar Imagenes desde varias fuentes",columna_imagen)
    
    a1 = ft.CircleAvatar(
        foreground_image_src="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
        content=ft.Text("FF"),
    )
    circulo_texto = ft.CircleAvatar(
        content=ft.Text("AA",color=ft.Colors.BLUE_700),
        radius=50,
        bgcolor= ft.Colors.BLUE_200
    )
    
    fila = ft.Row([a1,circulo_texto])
    imagen_avatar = create_example("Avatar","Permite motrar icono avatar",fila)
    
    page.add(texto,stack_example,imagen_example,imagen_avatar)


ft.app(target=main)