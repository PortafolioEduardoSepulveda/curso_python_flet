import flet as ft
import time


def main(page: ft.Page):
    def simular_descarga(e):
        archivos_seleccionados = [checkbox for checkbox in file_list.controls if checkbox.value]
        if not archivos_seleccionados:
            status_text.value = "Por favor, seleccione al menos un archivo."
            page.update()
            return
        progress_bar.value = 0
        progress_ring.value = 0
        page.update()

        total_size= sum([float(archivo.label.split("(")[1].split(" MB")[0]) for archivo in archivos_seleccionados ])
        downloaded = 0

        for archivo in archivos_seleccionados:
            file_size = float(archivo.label.split("(")[1].split(" MB")[0])
            status_text.value = f"Descargando {archivo.label}..."

            for _ in range(10):
                time.sleep(0.3)
                downloaded += file_size/10
                progress = min(downloaded/total_size,1)
                progress_bar.value = progress
                progress_ring.value = progress
                page.update()
        progress_bar.value = 1
        progress_ring.value = 1
        status_text.value = "!Descarga Completada¡"
        page.update()
        time.sleep(1)
        progress_bar.value = 0
        progress_ring.value = 0
        status_text.value = ""
        for checkbox in file_list.controls:
            checkbox.value = False     
        page.update()       
        
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.window.width = 800  # Ancho inicial
    page.window.height = 600  # Alto inicial
    page.window.resizable = False  # Permitir que el usuario redimensione la ventana
    page.padding= 10
    page.title = "Simulador de Descarga"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    texto  = ft.Text("Simulador de Descarga de Archivos", weight=ft.FontWeight.BOLD ,size=30)
    archivos = ft.Text("Selecciona archivos para descargar",size=16,color=ft.Colors.WHITE70)
    file_list = ft.Column([
        ft.Checkbox(label="documento.pdf (2.5 MB)",value=False),
        ft.Checkbox(label="imagen.jpg (5 MB)",value=False),
        ft.Checkbox(label="video.mp4 (50 MB)",value=False),
        ft.Checkbox(label="archivo.zip (100 MB)",value=False),
    ])
    contenedor_archivos = ft.Container(
        content=file_list,
        padding=10
    )
    progress_bar = ft.ProgressBar(width=400,color="amber",bgcolor="#263238",value=0)
    progress_ring = ft.ProgressRing(stroke_width=5,color="amber",value=0)
    fila = ft.Row(controls=[progress_bar,progress_ring],alignment=ft.MainAxisAlignment.CENTER)
    status_text = ft.Text("",color=ft.Colors.WHITE)
    boton_descarga = ft.ElevatedButton("Iniciar Descarga",on_click=simular_descarga,bgcolor=ft.Colors.AMBER,color=ft.Colors.BLACK)
    page.add(texto,archivos,contenedor_archivos,fila,status_text,boton_descarga)


ft.app(target=main)