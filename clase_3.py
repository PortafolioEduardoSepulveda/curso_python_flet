import flet as ft


def main(page: ft.Page):
    def seleccionar_tarea(e):
        seleccionadas = [t.title.value for t in tareas if t.leading.value]
        tareas_seleccionadas.value = "Tarea seleccionada: "+", ".join(seleccionadas)
        page.update()
    def actualizar_lista():
        lista_tareas.controls.clear()
        lista_tareas.controls.extend(tareas)
        page.update()
    def agregar_tarea(e):
        if campo_tarea.value:
            tarea = ft.ListTile(title=ft.Text(campo_tarea.value,color=ft.colors.WHITE),leading=ft.Checkbox(check_color=ft.colors.WHITE,on_change=seleccionar_tarea))
            tareas.append(tarea)
            campo_tarea.value = ""
            actualizar_lista()
    
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = "light"
    page.title = "Lista de Tareas"
    texto  = ft.Text("Lista de Tareas", weight=ft.FontWeight.BOLD ,size=30,color=ft.colors.WHITE)
    campo_tarea = ft.TextField(hint_text="Escribe una Nueva Tarea",color=ft.colors.WHITE,border_color=ft.colors.WHITE)
    boton_agregar = ft.FilledButton(text="Agregar Tarea", on_click=agregar_tarea)
    lista_tareas = ft.ListView(expand=1,spacing=3)
    tareas = []
    tareas_seleccionadas = ft.Text("",size=20,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)
    page.add(texto,campo_tarea,boton_agregar,lista_tareas,tareas_seleccionadas)





ft.app(target=main)