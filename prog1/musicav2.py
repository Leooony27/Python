import pygame
import os
import tkinter as tk
from tkinter import messagebox, filedialog
from mutagen.mp3 import MP3  
pygame.mixer.init()

class Player:
    def __init__(self, master):
        self.master = master
        master.title("MP3 Player")
        master.geometry("400x450") 
        master.config(bg="#808080")

        self.canvas = tk.Canvas(master, bg="#808080", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.create_rounded_rectangle(0, 0, 400, 450, 20, "#808080")

        self.is_playing = False
        self.is_paused = False
        self.current_position = 0
        self.total_length = 0
        
        self.song_label = tk.Label(master, text="Nome da Música", bg="#808080", font=("Arial", 14), fg="white")
        self.song_label.place(x=20, y=20)

        self.time_label = tk.Label(master, text="00:00 / 00:00", bg="#808080", font=("Arial", 16), fg="white")
        self.time_label.place(x=20, y=60)

        self.select_button = tk.Button(master, text="Escolher Arquivo MP3", command=self.select_file, width=20, bg="white", fg="black")
        self.select_button.place(x=40, y=100)

        button_frame = tk.Frame(master, bg="#808080")
        button_frame.place(x=40, y=140)

        self.play_button = tk.Button(button_frame, text="Play", command=self.play, width=10, bg="#4CAF50", fg="white")  # Verde
        self.play_button.pack(side=tk.LEFT, padx=5)

        self.pause_button = tk.Button(button_frame, text="Pause", command=self.pause, width=10, bg="white", fg="black")
        self.pause_button.pack(side=tk.LEFT, padx=5)

        self.resume_button = tk.Button(button_frame, text="Resume", command=self.resume, width=10, bg="white", fg="black")
        self.resume_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop, width=10, bg="white", fg="black")
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.rewind_button = tk.Button(button_frame, text="Rewind 10s", command=self.rewind, width=10, bg="white", fg="black")
        self.rewind_button.pack(side=tk.LEFT, padx=5)

        self.forward_button = tk.Button(button_frame, text="Forward 10s", command=self.forward, width=10, bg="white", fg="black")
        self.forward_button.pack(side=tk.LEFT, padx=5)

        self.volume_label = tk.Label(master, text="Volume", bg="#808080", fg="white")
        self.volume_label.place(x=40, y=380)

        self.volume_scale = tk.Scale(master, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, command=self.set_volume, bg="#808080", fg="white", sliderrelief="flat")
        self.volume_scale.set(0.5)
        self.volume_scale.place(x=100, y=375)

        self.caminho_do_mp3 = ""

    def create_rounded_rectangle(self, x1, y1, x2, y2, r, color):
        self.canvas.create_arc(x1, y1, x1 + r*2, y1 + r*2, start=90, extent=90, fill=color, outline=color)
        self.canvas.create_arc(x2 - r*2, y1, x2, y1 + r*2, start=0, extent=90, fill=color, outline=color)
        self.canvas.create_arc(x1, y2 - r*2, x1 + r*2, y2, start=180, extent=90, fill=color, outline=color)
        self.canvas.create_arc(x2 - r*2, y2 - r*2, x2, y2, start=270, extent=90, fill=color, outline=color)
        self.canvas.create_rectangle(x1 + r, y1, x2 - r, y2, fill=color, outline=color)
        self.canvas.create_rectangle(x1, y1 + r, x1 + r, y2 - r, fill=color, outline=color)
        self.canvas.create_rectangle(x2 - r, y1 + r, x2, y2 - r, fill=color, outline=color)

    def select_file(self):
        self.caminho_do_mp3 = filedialog.askopenfilename(title="Escolher Arquivo MP3", filetypes=[("MP3 Files", "*.mp3")])
        if self.caminho_do_mp3:
            audio = MP3(self.caminho_do_mp3)
            self.total_length = audio.info.length 
            self.update_time_label()  
            self.update_song_label()  

    def update_song_label(self):
        song_name = os.path.basename(self.caminho_do_mp3).replace('.mp3', '') 
        self.song_label.config(text=song_name)

    def update_time_label(self):
        total_time_str = self.format_time(self.total_length)
        self.time_label.config(text=f"00:00 / {total_time_str}")

    def play(self):
        if not self.is_playing and self.caminho_do_mp3:
            pygame.mixer.music.load(self.caminho_do_mp3)
            pygame.mixer.music.play(start=self.current_position)
            self.is_playing = True
            self.is_paused = False
            self.update_time()

    def update_time(self):
        if self.is_playing:
            current_time = pygame.mixer.music.get_pos() / 1000 
            self.time_label.config(text=f"{self.format_time(current_time)} / {self.format_time(self.total_length)}")
            self.master.after(1000, self.update_time)  

    def format_time(self, seconds):
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        return f"{minutes:02}:{seconds:02}"

    def pause(self):
        if self.is_playing and not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True
            self.current_position = pygame.mixer.music.get_pos() / 1000.0  

    def resume(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            self.update_time()  

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False
        self.current_position = 0
        self.time_label.config(text="00:00 / 00:00")  
        self.song_label.config(text="Nome da Música")  

    def forward(self):
        if self.is_playing:
            self.current_position += 10
            pygame.mixer.music.play(start=self.current_position)
            self.update_time() 

    def rewind(self):
        if self.is_playing:
            self.current_position -= 10
            if self.current_position < 0:
                self.current_position = 0
            pygame.mixer.music.play(start=self.current_position)
            self.update_time()  

    def set_volume(self, value):
        volume = float(value) 
        pygame.mixer.music.set_volume(volume)  

if __name__ == "__main__":
    try:
        root = tk.Tk()
        player = Player(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Erro", str(e))
