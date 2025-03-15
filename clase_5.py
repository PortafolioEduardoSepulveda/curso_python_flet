import flet as ft
import os
import base64


def main(page: ft.Page):
    def crear_producto(nombre,precio,color,imagen_nombre):
        image_path = os.path.join(os.path.dirname(__file__),"assets",imagen_nombre)
        try:
            with open(image_path,"rb") as image_file:
                image_bytes = base64.b64encode(image_file.read()).decode()
        except FileNotFoundError:
            print(f"Advertencia: la imagen {imagen_nombre} no existe en {image_path} ")
            image_bytes=None        
        return ft.Container(
            content = ft.Column([
                ft.Image(src_base64=image_bytes,width=150,height=150,fit=ft.ImageFit.CONTAIN,error_content=ft.Text("Imagen no Encontrada") if image_bytes else ft.Text("Imagen no Encontrada") ),
                ft.Text(nombre,size=16,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE),
                ft.Text(precio,size=14,color=ft.Colors.WHITE),
                ft.ElevatedButton("Agregar al carrito",bgcolor=ft.Colors.BLUE_GREY_300, color=ft.Colors.WHITE)
            ]),
            bgcolor=color,
            border_radius=10,
            padding=20,
            alignment=ft.alignment.center
    )
    page.bgcolor = ft.Colors.BLUE_GREY_900
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # Cambiar el tamaño de la ventana al iniciar
    page.window.width = 800  # Ancho inicial
    page.window.height = 600  # Alto inicial
   
    page.window.resizable = False  # Permitir que el usuario redimensione la ventana
    page.update()
    page.padding= 10
    page.theme_mode = "light"
    page.title = "Galeria de Productos Responsiva"
    texto  = ft.Text("Galeria de Productos", weight=ft.FontWeight.BOLD ,size=30,color=ft.Colors.WHITE)
    
    productos = [
        crear_producto("Producto 1", 19.9,ft.Colors.BLUE_500,"Producto1.png"),
        crear_producto("Producto 2", 29.9,ft.Colors.AMBER_500,"Producto2.png"),
        crear_producto("Producto 3", 39.9,ft.Colors.GREEN_500,"Producto3.png"),
        crear_producto("Producto 4", 49.9,ft.Colors.ORANGE_500,"Producto4.png"),
        crear_producto("Producto 5", 59.9,ft.Colors.PURPLE_500,"Producto5.png"),
    ]
    galeria = ft.ResponsiveRow(
        [ft.Container(producto,col={"sm":12,"md":6,"lg":3}) for producto in productos],
        run_spacing=20,
        spacing=20,
    )
    contenido = ft.Column([
        texto,
        ft.Divider(height=20,color=ft.Colors.WHITE),
        galeria
    ],scroll=ft.ScrollMode.AUTO,expand=True)
    page.add(contenido)


ft.app(target=main)