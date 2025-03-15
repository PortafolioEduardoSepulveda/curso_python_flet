import flet as ft
import random


def main(page: ft.Page):
    def cambiar_tema(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.bgcolor = ft.Colors.BLUE_GREY_100
            tema_btn.text = "Modo Oscuro"
        else:
            page.theme_mode = ft.ThemeMode.DARK
            page.bgcolor = ft.Colors.BLUE_GREY_800
            tema_btn.text = "Modo Claro"
        page.update()    

    def reiniciar_juego(e):
        nonlocal numero_secreto,intentos 
        numero_secreto = random.randint(1,10)
        intentos = 0
        resultado.value = "Adivina el numero entre 1 y 10"
        resultado.color = ft.Colors.WHITE
        verificar_btn.disabled = False
        input_numero.value = ""
        page.update()
    def verificar_intento(e):
        nonlocal intentos
        intento = int(input_numero.value)
        intentos +=1
        if intento == numero_secreto:
            resultado.value = f"¡Correcto Numero Secreto es {numero_secreto}! Lo adivinaste en  {intento} intentos."
            resultado.color = ft.Colors.GREEN
            verificar_btn.disabled = True
        elif intento < numero_secreto:
            resultado.value = "Demasiado bajo. Intenta de Nuevo."
            resultado.color = ft.Colors.ORANGE
        else:
            resultado.value = "Demasiado Alto. Intenta de Nuevo."    
            input_numero.value = ""
            resultado.color = ft.Colors.ORANGE
        input_numero.value = ""
        intentos_text.value = f"Intentos :{intentos}"        
        page.update()
        
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.window.width = 800  # Ancho inicial
    page.window.height = 600  # Alto inicial
   
    page.window.resizable = False  # Permitir que el usuario redimensione la ventana
    page.padding= 10
    page.title = "Juego de Adivinanzas"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    texto  = ft.Text("Cards, Divider y VerticalDivider en Flet", weight=ft.FontWeight.BOLD ,size=30)
    
    numero_secreto = random.randint(1,10)
    intentos = 0
    
    divider_simple = ft.Divider(height=1,color=ft.Colors.BLUE_200)
    divider_vertical = ft.VerticalDivider(width=1,color=ft.Colors.BLUE)
    titulo_juego  = ft.Text("Juego de Adivinanzas", weight=ft.FontWeight.BOLD ,size=20)
    input_numero = ft.TextField(label="Tu intento",width=150)
    verificar_btn = ft.ElevatedButton("Verificar",on_click=verificar_intento)
    resultado = ft.Text("Adivina el numero entre 1 y 10")
    intentos_text = ft.Text("Intentos:0")
    reiniciar_btn = ft.ElevatedButton("Reiniciar juego",on_click=reiniciar_juego)
    tema_btn = ft.ElevatedButton("Modo Claro",on_click=cambiar_tema)
    card_simple1 = ft.Card(
        content=ft.Container(content=ft.Column([titulo_juego,input_numero,verificar_btn,resultado,intentos_text,reiniciar_btn],alignment=ft.MainAxisAlignment.CENTER,spacing=20),
                             padding=10,

                             ),
        width=300,
        height=400                     
    )
    card_simple2 = ft.Card(
        content=ft.Container(content=tema_btn,
                             padding=10,

                             ),
        width=150,
        height=100                     
    )
    layout = ft.Row([card_simple1,divider_vertical,card_simple2],alignment=ft.MainAxisAlignment.CENTER)
 
    page.add(texto,divider_simple,layout)


ft.app(target=main)