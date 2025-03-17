import flet as ft



def main(page: ft.Page):
    def update_preview(e):
        
        preview.value = f"""
        Nombre: {name_input.value}
        Edad:  {age_dropdown.value}
        Genero: {gender_radio.value}
        Intereses: {','.join([c.label for c in interests_checkbox.controls if c.value])}
        Modo Oscuro: {"Activado" if theme_switch.value else "Desactivado"}
        """
        page.update()

    def toggle_theme(e):
        if theme_switch.value:
            page.theme_mode = ft.ThemeMode.DARK
            page.bgcolor = ft.Colors.BLUE_GREY_800
            texto.color = ft.Colors.LIGHT_BLUE_200
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.bgcolor = ft.Colors.BLUE_GREY_100
            texto.color = ft.Colors.PINK_300
        page.update()        

    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.window.width = 800  # Ancho inicial
    page.window.height = 600  # Alto inicial
    page.window.resizable = False  # Permitir que el usuario redimensione la ventana
    page.padding= 20
    page.title = "Perfil de Usuario"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO
    #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    texto  = ft.Text("Perfil de Usuario con flet", weight=ft.FontWeight.BOLD ,size=30)
    name_input = ft.TextField(label="Nombre",border_radius=8,on_change=update_preview)
    age_dropdown = ft.Dropdown(
        label="Edad",
        options=[ft.dropdown.Option(str(age)) for age in range(18,101)],
        border_radius=8,
        on_change=update_preview
    )
    gender_radio = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Masculino",label="Masculino"),
            ft.Radio(value="Femenino",label="Femenino"),
            ft.Radio(value="Otro",label="Otro"),
        ]),on_change=update_preview
    )
    interests = ["Arte","Tecnologia","Musica","Deporte","Viajes"]
    interests_checkbox = ft.Column([
        ft.Checkbox(label=interest,on_change=update_preview) for interest in interests
    ])
    theme_switch = ft.Switch(label="Modo Oscuro",on_change=lambda e:[toggle_theme(e),update_preview(e)],value=True)
    preview = ft.Text("Completa el formulario para ver la Previsualizacion", size=14)
    page.add(texto,
             name_input,
             age_dropdown,
             ft.Text("Genero:",size=16,weight=ft.FontWeight.BOLD),
             gender_radio,
             ft.Text("Intereses:",size=16,weight=ft.FontWeight.BOLD),
             interests_checkbox,
             theme_switch,
             ft.Text("Previsualizacion del Perfil:",size=16,weight=ft.FontWeight.BOLD),
             preview 
             )
    

ft.app(target=main)