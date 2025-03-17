import flet as ft
import time


def main(page: ft.Page):
    def show_stats(e):
        total_items = len(shopping_list.controls)
        checked_items = sum(1 for item in shopping_list.controls if item.leading.value)
        category_counts = {}
        for item in shopping_list.controls:
            category = item.subtitle.controls[1].value
            category_counts[category] = category_counts.get(category,0)+1
            stats_text = f"Total: {total_items}, Comprados: {checked_items}, Pendientes: {total_items-checked_items}"
            stats_text += "\nCategorias:\n"+ "\n".join([f"{cat}: {count}" for cat,count in category_counts.items()])

            snack = ft.SnackBar(content=ft.Text(stats_text,color=ft.Colors.BLACK),bgcolor=ft.Colors.AMBER)
            page.overlay.append(snack)
            snack.open = True
            page.update()
    
    
    def clear_list(e):
        shopping_list.controls.clear()
        page.update()

    def add_item(e):
        if item_input.value:
            quantity = quantity_input.value if quantity_input.value else "1"
            def update_category(e):
                category_text.value = f"Categoria : {e.control.value}"
                page.update()


            category_dropdown = ft.Dropdown(
                options=[ft.dropdown.Option(category) for category in categorias],
                value=categorias[0],
                on_change=update_category,
                color=ft.Colors.AMBER,
                width=150
            )
            category_text = ft.Text(f"Categoria : {categorias[0]}",color=ft.Colors.AMBER_200)
            new_item = ft.ListTile(
                leading=ft.Checkbox(value=False,fill_color=ft.Colors.AMBER),
                title=ft.Text(f"{item_input.value} (x{quantity})", color=ft.Colors.AMBER),
                subtitle=ft.Row(controls=[category_text,category_dropdown],alignment=ft.MainAxisAlignment.START,spacing=10),
                trailing=ft.IconButton(icon=ft.Icons.DELETE,icon_color=ft.Colors.RED_400,on_click= lambda _: shopping_list.controls.remove(new_item) or page.update())
            )
            
            shopping_list.controls.append(new_item)
            item_input.value = ""
            quantity_input.value = ""
            page.update()
        
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.window.width = 800  # Ancho inicial
    page.window.height = 600  # Alto inicial
    page.window.resizable = False  # Permitir que el usuario redimensione la ventana
    page.padding= 20
    page.title = "Lista de Compras"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    texto  = ft.Text("Lista de Compras con flet", weight=ft.FontWeight.BOLD ,size=30)
    categorias = ["Sin Categoria","Alimentos","Limpieza","Electronica","Ropa"]
    shopping_list = ft.Column(scroll=ft.ScrollMode.AUTO)     
    item_input = ft.TextField(hint_text="Añadir Articulo",border_color=ft.Colors.AMBER,color=ft.Colors.WHITE,width=300,text_align=ft.TextAlign.CENTER)
    quantity_input = ft.TextField(hint_text="Cantidad",border_color=ft.Colors.AMBER,color=ft.Colors.WHITE,width=100,text_align=ft.TextAlign.CENTER)
    
    add_button = ft.OutlinedButton(
        text="Añadir a la lista",
        on_click=add_item,
        style=ft.ButtonStyle(color=ft.Colors.AMBER,side=ft.BorderSide(2,ft.Colors.AMBER))
    )
    clear_button = ft.IconButton(
        icon=ft.Icons.CLEANING_SERVICES,
        tooltip="Limpiar Lista",
        on_click=clear_list,
        icon_color=ft.Colors.AMBER
    )
    button_show_stats = ft.TextButton(
        text="Estadisticas",
        on_click=show_stats,
        style=ft.ButtonStyle(color=ft.Colors.AMBER)
    )
    fila_input = ft.Row(controls=[item_input,quantity_input,add_button],alignment=ft.MainAxisAlignment.CENTER,spacing=10)
    fila_botones = ft.Row(controls=[clear_button,button_show_stats],alignment=ft.MainAxisAlignment.CENTER,spacing=10)
     
    
    page.add(texto,fila_input,fila_botones,
             ft.Divider(height=20,thickness=2,color=ft.Colors.AMBER),
             shopping_list)
    

ft.app(target=main)