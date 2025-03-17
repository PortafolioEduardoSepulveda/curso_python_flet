import flet as ft
import pygame
import os
import asyncio
from mutagen.mp3 import MP3


class Song:
    def __init__(self,filename):
        self.filename = filename
        self.title = os.path.splitext(filename)[0]
        self.duration = self.get_duration()

    def get_duration(self):
        audio = MP3(os.path.join("canciones",self.filename))  
        return audio.info.length  

async def main(page: ft.Page):
    def load_song():
        pygame.mixer.music.load(os.path.join("canciones",play_list[current_song_index].filename))
    
    def play_pause(e):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            play_button.icon = ft.Icons.PLAY_ARROW
        else:
            if pygame.mixer.music.get_pos() == -1:
                load_song()
                pygame.mixer.music.play()
            else:
                pygame.mixer.music.unpause()
            play_button.icon = ft.icons.PAUSE
        page.update()        

    def change_song(delta):
        nonlocal current_song_index
        current_song_index = (current_song_index + delta) % len(play_list)
        load_song()
        pygame.mixer.music.play()
        update_song_info()
        play_button.icon = ft.Icons.PAUSE
        page.update()

    def update_song_info():
        song = play_list[current_song_index]
        song_info.value = f"{song.title}"
        duration.value = format_time(song.duration)
        progess_bar.value = 0.0
        current_time_text.value = "00:00"
        page.update()

    def format_time(seconds):
        minutes,seconds = divmod(int(seconds),60)
        return f"{minutes:02d}:{seconds:02d}"    
    
    
    async def update_progress():
        while True:
            if pygame.mixer.music.get_busy():
                current_time = pygame.mixer.music.get_pos() /1000
                progess_bar.value = current_time/play_list[current_song_index].duration
                current_time_text.value = format_time(current_time)
                page.update()
            await asyncio.sleep(1)    
                
    page.title = "Reproductor de Música"
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.padding = 20
    titulo = ft.Text("Reproductor de Musica",size=30,color=ft.Colors.WHITE)
    page.window.width = 450  # Ancho inicial
    page.window.height = 200  # Alto inicial
    page.theme_mode = ft.ThemeMode.DARK
    pygame.mixer.init()
    play_list = [Song(f) for f in os.listdir("canciones") if f.endswith(".mp3")]

    current_song_index = 0
    song_info = ft.Text(size=20,color=ft.Colors.WHITE)
    current_time_text = ft.Text("00:00",color=ft.Colors.WHITE60)
    duration = ft.Text("00:00",color=ft.Colors.WHITE60)
    progess_bar = ft.ProgressBar(value=0.0,width=300,color="white",bgcolor="red")
    play_button = ft.IconButton(icon=ft.Icons.PLAY_ARROW,on_click=play_pause,icon_color=ft.Colors.WHITE)
    prev_button = ft.IconButton(icon=ft.Icons.SKIP_PREVIOUS,on_click=lambda _: change_song(-1),icon_color=ft.Colors.WHITE)
    next_button = ft.IconButton(icon=ft.Icons.SKIP_NEXT,on_click=lambda _: change_song(+1),icon_color=ft.Colors.WHITE)
    
    controles = ft.Row(
        controls=[prev_button,play_button,next_button],
        alignment=ft.MainAxisAlignment.CENTER
    )
    fila_reproductor = ft.Row(
        controls=[current_time_text,progess_bar,duration],
        alignment=ft.MainAxisAlignment.CENTER
    )

    columna = ft.Column([song_info,fila_reproductor,controles],alignment=ft.MainAxisAlignment.CENTER,spacing=20)
    page.add(columna)

    if play_list:
        load_song()
        update_song_info()
        page.update()
        await update_progress()


ft.app(target=main)