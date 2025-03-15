import flet as ft


def main(page: ft.Page):
    def delete_note(note):
        grid.controls.remove(note)
        page.update()
    def add_note(e):
        new_nota = create_note("Nueva Nota")
        grid.controls.append(new_nota)
        page.update()

    def create_note(text):
        note_content = ft.TextField(value=text,multiline=True,bgcolor= ft.Colors.BLUE_50)
        note = ft.Container(
            content= ft.Column([note_content,ft.IconButton(icon=ft.Icons.DELETE,
                                                           on_click=lambda _: delete_note(note))]),
            width=200,
            height=200,
            bgcolor=ft.Colors.BLUE_GREY_100,
            border_radius=10,
            padding=10                                               
                                                           
        )
        return note
    page.bgcolor = ft.Colors.BLUE_GREY_800
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # Cambiar el tamaño de la ventana al iniciar
    page.window.width = 800  # Ancho inicial
    page.window.height = 600  # Alto inicial
   
    page.window.resizable = False  # Permitir que el usuario redimensione la ventana
    page.update()
    page.padding= 20
    page.theme_mode = "light"
    page.title = "mi app"
    grid = ft.GridView(
        expand=True,
        max_extent=200,
        child_aspect_ratio=1,
        spacing=10,
        run_spacing=10)
    notes = [
        "comprar leche",
        "llamar al medico",
        "reunion a las 3 pm"
    ]
     
    for note in notes:
        grid.controls.append(create_note(note))
    
    page.add(ft.Row([
        ft.Text("Mis Notas Adhesivas",size=24,weight="bold",color=ft.Colors.WHITE),
        ft.IconButton(icon=ft.icons.ADD,on_click=add_note,icon_color=ft.Colors.WHITE)

    ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN)) 
    page.add(grid)




ft.app(target=main)
