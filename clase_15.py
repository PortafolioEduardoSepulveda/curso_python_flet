import flet as ft
import random
import string


def main(page: ft.Page):
    def generate_password(length,use_uppercase,use_number,use_symbols):
        characters = string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_number:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation
        characters = characters.replace("'","")     
        characters = characters.replace("\"","")       
        return ''.join(random.choice(characters) for _ in range(length))
    
    def update_password(e):
        password_field.value = generate_password(
            int(length_slider.value),
            uppecase_switch.value,
            digits_switch.value,
            symbols_switch.value
        )
        page.update()

    def copy_to_clipboard(e):
        page.set_clipboard(password_field.value)
        snack_bar = ft.SnackBar(ft.Text("Contraseña copiada al portapapeles"))
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()

    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.padding= 20
    page.title = "NavigationBar Example"
    page.theme_mode = ft.ThemeMode.DARK
    #page.scroll = ft.ScrollMode.AUTO
    #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 600  # Ancho inicial
    page.window.height = 600  
    page.update()
    titulo  = ft.Text("Generador de Contraseñas", weight=ft.FontWeight.BOLD ,size=30)
    
    password_field = ft.TextField(
        read_only=True,
        width=400,
        text_align=ft.TextAlign.CENTER,
        text_style=ft.TextStyle(size=20,weight=ft.FontWeight.BOLD)
    )
    length_slider = ft.Slider(min=8,max=32,divisions=24,label="{value}",value = 12 ,on_change=update_password)
    generate_button = ft.ElevatedButton("Generar Contraseña",on_click=update_password)
    uppecase_switch = ft.Switch(label="Incluir Mayusculas",value=True ,on_change=update_password)
    digits_switch = ft.Switch(label="Incluir Numeros",value=True ,on_change=update_password)
    symbols_switch = ft.Switch(label="Incluir Simbolos",value=True ,on_change=update_password)
    copy_button = ft.ElevatedButton(
        "Copiar al Portapapeles",
        on_click=copy_to_clipboard,
        icon=ft.Icons.COPY
        )
    page.add(titulo,
             ft.Text("Longitud de la Contraseña"),
             length_slider,
             uppecase_switch,
             digits_switch,
             symbols_switch,
             password_field,
             ft.Row(controls=[generate_button,copy_button],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,spacing=10)
             )
    
   
    

ft.app(target=main)