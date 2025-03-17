import flet as ft



def main(page: ft.Page):
    def add_book(e):
        title_field.error_text = ""
        author_field.error_text = ""
        page.update()
        if not title_field.value:
            title_field.error_text= "Por favor ingrese un titulo"
            page.update()
            return
        if not author_field.value:
            author_field.error_text = "Por favor ingrese un autor"
            page.update()
            return
        new_book = ft.ListTile(
            title=ft.Text(title_field.value),
            subtitle=ft.Text(author_field.value if author_field.value else "Desconocido"),
            trailing=ft.PopupMenuButton(
                icon=ft.Icons.MORE_VERT,
                items=[
                    ft.PopupMenuItem("Eliminar",on_click=lambda _: book_view.controls.remove(new_book) or page.update())
                    ])
        )
        book_view.controls.append(new_book)
        title_field.value = None
        author_field.value = ""
        page.update() 
    def destination_change(e):
        content.controls.clear()
        index = e.control.selected_index
        if index == 0:
            content.controls.append(book_view)
        elif index == 1:
            content.controls.append(add_book_view)
        elif index == 2:
            content.controls.append(wishlist_view)
        page.update()            


    def change_theme(e):
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        theme_icon_button.icon = ft.Icons.LIGHT_MODE if  theme_icon_button.icon == ft.Icons.DARK_MODE else ft.Icons.DARK_MODE
        #page.bgcolor = ft.Colors.BLUE_GREY_100 if page.bgcolor == ft.Colors.BLUE_GREY_800 else ft.Colors.BLUE_GREY_800
        page.update()

    #page.bgcolor = ft.Colors.BLUE_GREY_900
    page.padding= 20
    page.title = "Biblioteca Personal"
    page.theme_mode = ft.ThemeMode.DARK
    #page.scroll = ft.ScrollMode.AUTO
    #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    texto  = ft.Text("Biblioteca Personal con flet", weight=ft.FontWeight.BOLD ,size=30)
    theme_icon_button = ft.IconButton(
        icon=ft.Icons.DARK_MODE,
        tooltip="Cambiar Tema",
        on_click=change_theme
    )
    app_bar = ft.AppBar(
        title=texto,
        center_title=True,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[theme_icon_button]
    )
    book_view = ft.ListView(expand=1,spacing=10,padding=20)
    wishlist_view = ft.ListView(expand=1,spacing=10,padding=20)
    title_field  = ft.TextField(label="Titulo del libro",width=300)
    author_field = ft.TextField(label="Autor",width=300)
    add_button = ft.ElevatedButton("Añadir Libro",on_click=add_book)
    add_book_view = ft.Column(controls=[
        ft.Text("Añadir nuevo Libro",size=20,weight=ft.FontWeight.BOLD),
        title_field,
        author_field,
        add_button 

    ],spacing=20)

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.BOOK,label="Mis Libros"),
            ft.NavigationRailDestination(icon=ft.Icons.ADD,label="Añadir Libros"),
            ft.NavigationRailDestination(icon=ft.Icons.FAVORITE,label="Lista de Deseos"),
        ],
        on_change=destination_change
    )
    content = ft.Column(controls=[book_view],expand=True) 
    
    page.add(app_bar,ft.Row([
        rail,
        ft.VerticalDivider(width=1),
        content
        ],expand=True))
   
    

ft.app(target=main)