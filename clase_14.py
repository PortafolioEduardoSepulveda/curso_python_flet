import flet as ft



def main(page: ft.Page):
    def increment_counter(e):
        nonlocal counter_value
        counter_value += 1
        counter.value = f"Counter: {counter_value}"
        page.update()

    def decrement_counter(e):
        nonlocal counter_value
        counter_value -= 1
        counter.value = f"Counter: {counter_value}"
        page.update()

    def on_navigation_change(e):
        selected_index = e.control.selected_index
        if selected_index == 0:
            show_home()
        elif selected_index == 1:
            show_search()
        elif selected_index == 2:
            show_setting()    
        page.update()    

    def show_home():
        page.controls.clear()
        counter.value = f"Counter: {counter_value}"
        page.add(navigation_bar,counter,btn_increment,btn_decrement)
        

    def show_search():
        print("entro 2")
        page.controls.clear()
        search_input.value = ""
        search_output.value = ""
        page.add(navigation_bar,search_input,search_output,btn_search)
        

    def search_text(e):
        search_output.value = f"search result: {search_input.value}"
        search_input.value = ""
        page.update()

    def show_setting():
        print("entro 3")
        page.controls.clear()
        page.add(navigation_bar,brightness_slider,btn_reset_brightness)

    def reset_brightness(e):
        brightness_slider.value = 50
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
    counter  = ft.Text("Counter : 0", weight=ft.FontWeight.BOLD ,size=30)
    btn_increment = ft.ElevatedButton("Increment",on_click=increment_counter)
    btn_decrement = ft.ElevatedButton("Decrement",on_click=decrement_counter)
    search_input = ft.TextField(label="Enter text to search")
    search_output = ft.Text("",size=20,color=ft.Colors.WHITE)
    btn_search = ft.ElevatedButton("Search",on_click=search_text)
    brightness_slider = ft.Slider(min=0,max=100,value=50,label="Brightness")
    btn_reset_brightness = ft.ElevatedButton("Reset",on_click=reset_brightness)
    counter_value = 0
    navigation_bar = ft.NavigationBar(
        selected_index=0,
        on_change=on_navigation_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME,label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.SEARCH,label="Search"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS,label="Settings"),
        ],
        bgcolor=ft.Colors.BLUE_GREY_900,
        indicator_color=ft.Colors.AMBER
    )
    show_search()
    
   
    

ft.app(target=main)