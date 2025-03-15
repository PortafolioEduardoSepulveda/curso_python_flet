import flet as ft
import random


def main(page: ft.Page):
    def actualizar_tareas():
        lista_tareas.controls.clear()
        for tarea in generar_tareas():
            lista_tareas.controls.append(ft.Text(tarea,color=ft.Colors.WHITE))
        page.update()    
    def generar_tareas():
        tareas = ["hacer la compra","llamar al medico", "estudiar para el examen", "hacer ejercicio","leer un libro","preparar la cena"]
        return [random.choice(tareas) for _ in range(5)]
    
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 800  # Ancho inicial
    page.window.height = 600  # Alto inicial
   
    page.window.resizable = False  # Permitir que el usuario redimensione la ventana
    page.padding= 10
    page.update()
    page.title = "Tabs en Flet"
    texto  = ft.Text("Ejemplos de Tab en Flet", weight=ft.FontWeight.BOLD ,size=30,color=ft.Colors.WHITE)
    
    lista_tareas = ft.ListView(spacing=10,padding=20)
    actualizar_tareas()
    boton_actualizar = ft.ElevatedButton("Actualizar Tareas",on_click=lambda _: actualizar_tareas())
    contenido_tareas = ft.Column([lista_tareas,boton_actualizar])
    
    # contenido para Pestaña perfil
    campo_nombre = ft.TextField(label="Nombre",bgcolor=ft.Colors.BLUE_GREY_700)
    campo_email = ft.TextField(label="Email",bgcolor=ft.Colors.BLUE_GREY_700)
    boton_guardar = ft.ElevatedButton("Guardar Perfil")
    contenido_perfil = ft.Column([campo_nombre,campo_email,boton_guardar])
    # fin contenido perfil

    #contenido para pestaña configuracion
    switch_notificaciones = ft.Switch(label="Notificaciones",value=True)
    slider_volumen = ft.Slider(min=0,max=100,divisions=10,label="Volumen")
    contenido_config = ft.Column([switch_notificaciones,slider_volumen])
    #fin contenido pestaña configuracion
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Tareas",icon=ft.Icons.LIST_ALT,content=contenido_tareas),
            ft.Tab(text="Perfil",icon=ft.Icons.PERSON,content=contenido_perfil),
            ft.Tab(text="Tareas",icon=ft.Icons.SETTINGS,content=contenido_config),
        ]
    )
    page.add(texto,tabs)


ft.app(target=main)