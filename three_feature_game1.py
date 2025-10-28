import tkinter as tk
from tkinter import messagebox, filedialog
import time
import threading

try:
    import pygame
    pygame.init()
    pygame.mixer.init()
    HAS_PYGAME = True
except ImportError:
    HAS_PYGAME = False


class ThreeFeatureApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EchoDrive: 3-Feature Game")
        self.geometry("900x600")
        self.config(bg="#0e0e0e")
        self.main_menu()

    # --- MAIN MENU ---
    def main_menu(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(
            self,
            text="🚗 EchoDrive",
            font=("Consolas", 40, "bold"),
            fg="#00ff99",
            bg="#0e0e0e",
        ).pack(pady=60)

        tk.Label(
            self, text="Select a feature:", font=("Consolas", 18), fg="white", bg="#0e0e0e"
        ).pack(pady=20)

        tk.Button(self, text="1. Signboard Quiz", command=self.feature_quiz,
                  font=("Consolas", 16), bg="#1e1e1e", fg="#00ff99",
                  width=25, height=2).pack(pady=10)

        tk.Button(self, text="2. Music + Lyrics", command=self.feature_music,
                  font=("Consolas", 16), bg="#1e1e1e", fg="#00ff99",
                  width=25, height=2).pack(pady=10)

        tk.Button(self, text="3. Pixel Car Dashboard", command=self.feature_dashboard,
                  font=("Consolas", 16), bg="#1e1e1e", fg="#00ff99",
                  width=25, height=2).pack(pady=10)

        tk.Button(self, text="Exit", command=self.destroy,
                  font=("Consolas", 14), bg="#330000", fg="#ff5555",
                  width=20, height=1).pack(pady=40)

    # --- FEATURE 1: SIGNBOARD QUIZ ---
    def feature_quiz(self):
        for widget in self.winfo_children():
            widget.destroy()

        quiz_data = [
            ("🚫 NO ENTRY", ["No Entry", "Go Ahead", "Stop", "Parking"], "No Entry"),
            ("⚠️ SLIPPERY ROAD", ["Turn Left", "Slippery Road", "Pedestrian", "Stop"], "Slippery Road"),
            ("🅿️ PARKING", ["Hospital", "No Parking", "Parking", "Gas Station"], "Parking"),
        ]

        self.quiz_index = 0

        def ask_question():
            for widget in self.winfo_children():
                widget.destroy()

            if self.quiz_index >= len(quiz_data):
                tk.Label(self, text="🎉 You passed all signboards!",
                         font=("Consolas", 24), fg="#00ff99", bg="#0e0e0e").pack(pady=40)
                tk.Button(self, text="Back to Menu", command=self.main_menu,
                          font=("Consolas", 14), bg="#1e1e1e", fg="#00ff99").pack(pady=20)
                return

            q, options, ans = quiz_data[self.quiz_index]

            tk.Label(self, text=f"Identify this signboard:",
                     font=("Consolas", 22), fg="white", bg="#0e0e0e").pack(pady=30)
            tk.Label(self, text=q, font=("Consolas", 50), fg="#00ff99", bg="#0e0e0e").pack(pady=20)

            def check_answer(choice):
                if choice == ans:
                    self.quiz_index += 1
                    ask_question()
                else:
                    messagebox.showerror("Game Over", "❌ Wrong answer! You cannot proceed.")
                    self.main_menu()

            for opt in options:
                tk.Button(self, text=opt, command=lambda o=opt: check_answer(o),
                          font=("Consolas", 16), bg="#1e1e1e", fg="#00ff99",
                          width=20, height=1).pack(pady=8)

        ask_question()

    # --- FEATURE 2: MUSIC PLAYER ---
    def feature_music(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Title
        tk.Label(
            self,
            text="🎵 Music & Lyrics",
            font=("Consolas", 30, "bold"),
            fg="#00ff99",
            bg="#0e0e0e"
        ).pack(pady=30)

        # Music playlist data
        playlist = {
               "Multo": {
            "file": "multo.mp3",
            "lyrics": [
                (0,  "Humingang malalim, pumikit na muna"),
                (6,  "At baka-sakaling namamalikmata lang"),
                (12, "Ba't nababahala? 'Di ba't ako'y mag-isa?"),
                (18, "'Kala ko'y payapa, boses mo'y tumatawag pa"),
                (24, "Binaon naman na ang lahat"),
                (30, "Tinakpan naman na 'king sugat"),
                (36, "Ngunit ba't ba andito pa rin?"),
                (42, "Hirap na 'kong intindihin"),
                (48, "Tanging panalangin, lubayan na sana"),
                (54, "Dahil sa bawat tingin, mukha mo'y nakikita"),
                (60, "Kahit sa’n man mapunta ay anino mo'y kumakapit sa 'king kamay"),
                (66, "Ako ay dahan-dahang nililibing nang buhay pa"),
                (72, "Hindi na makalaya"),
                (78, "Dinadalaw mo 'ko bawat gabi"),
                (84, "Wala mang nakikita"),
                (90, "Haplos mo'y ramdam pa rin sa dilim"),
                (96, "Hindi na nananaginip"),
                (102,"Hindi na ma-makagising"),
                (108,"Pasindi na ng ilaw"),
                (114,"Minumulto na 'ko ng damdamin ko"),
                (120,"Ng damdamin ko"),
                (126,"Hindi mo ba ako lilisanin?"),
                (132,"Hindi pa ba sapat pagpapahirap sa 'kin?"),
                (138,"Hindi na ba ma-mamamayapa?"),
                (144,"Hindi na ba ma-mamamayapa?"),
                (150,"Hindi na makalaya"),
                (156,"Dinadalaw mo 'ko bawat gabi"),
                (162,"Wala mang nakikita"),
                (168,"Haplos mo'y ramdam pa rin sa dilim"),
                (174,"Hindi na nananaginip"),
                (180,"Hindi na ma-makagising"),
                (186,"Pasindi na ng ilaw"),
                (192,"Minumulto na 'ko ng damdamin ko"),
                (198,"Ng damdamin ko"),
                (204,"Hindi mo ba ako lilisanin?"),
                (210,"Hindi pa ba sapat pagpapahirap sa 'kin?"),
                (216,"Hindi na ba ma-mamamayapa?"),
                (222,"Hindi na ba ma-mamamayapa?"),
            ],
        },
           "Blue by Kai": {
    "file": "blue_by_kai.mp3",
    "lyrics": [
        (7,  "Your morning eyes.... I could stare like watching stars.."),
        (6,  "I could walk you by, and I'll tell without a thought"),
        (12, "You'd be mine, would you mind if I took your hand tonight?"),
        (18, "Know you're all that I want this life"),
        (24, "I'll imagine we fell in love"),
        (30, "I'll nap under moonlight skies with you"),
        (36, "I think I'll picture us, you with the waves"),
        (42, "The ocean's colors on your face"),
        (48, "I'll leave my heart with your air"),
        (54, "So let me fly with you"),
        (60, "Will you be forever with me?"),
        (66, "My love will always stay by you"),
        (72, "I'll keep it safe, so don't you worry a thing"),
        (78, "I'll tell you I love you more"),
        (84, "It's stuck with you forever, so promise you won't let it go"),
        (90, "I'll trust the universe will always bring me to you"),
        (96, "I'll imagine we fell in love"),
        (102,"I'll nap under moonlight skies with you"),
        (108,"I think I'll picture us, you with the waves"),
        (114,"The ocean's colors on your face"),
        (120,"I'll leave my heart with your air"),
        (126,"So let me fly with you"),
        (132,"Will you be forever with me?"),
    ],
},

        }

def load_music_file(self):
    """Let user select and play a custom MP3 file."""
    from tkinter import filedialog, messagebox
    import os, pygame, threading, time

    # Ask the user to pick an MP3 file
    filepath = filedialog.askopenfilename(
        title="Select an audio file",
        filetypes=[("MP3 files", "*.mp3"), ("All files", "*.*")]
    )

    if not filepath:
        return  # User canceled

    try:
        if pygame.mixer.get_init() is None:
            pygame.mixer.init()
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()
        messagebox.showinfo("Now Playing", f"Playing: {os.path.basename(filepath)}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not play file:\n{e}")

        

        song_var = tk.StringVar(value="Multo")

        # --- Custom dropdown frame ---
        dropdown_frame = tk.Frame(self, bg="#1e1e1e", highlightbackground="#00ff99", highlightthickness=2)
        dropdown_frame.pack(pady=15, ipady=5, ipadx=5)

        tk.Label(
            dropdown_frame,
            text="🎧 Select your track:",
            font=("Consolas", 16),
            fg="#00ff99",
            bg="#1e1e1e"
        ).pack(side="left", padx=10)

        dropdown = tk.OptionMenu(dropdown_frame, song_var, *playlist.keys())
        dropdown.config(
            font=("Consolas", 16),
            bg="#0e0e0e",
            fg="#00ff99",
            activebackground="#00ff99",
            activeforeground="#000000",
            width=20,
            relief="flat",
            highlightthickness=0,
        )
        dropdown.pack(side="left", padx=10)

        # Lyrics text box
        lyric_text = tk.Label(
            self, text="", font=("Consolas", 18),
            fg="white", bg="#0e0e0e", wraplength=700, justify="center"
        )
        lyric_text.pack(pady=40)

        # Update lyrics dynamically
        def update_lyrics(lyrics):
         for t, line in lyrics:
             lyric_text.config(text="")  # clear before typing
             for char in line:
                 current = lyric_text.cget("text")
                 lyric_text.config(text=current + char)
                 lyric_text.update()
                 time.sleep(0.05)  # typing speed (lower = faster)
             time.sleep(2)  # pause between lines
         lyric_text.config(text="(End of song)")


        # Play song logic
        def play_song():
            song = song_var.get()
            data = playlist[song]
            if HAS_PYGAME:
                try:
                    pygame.mixer.music.load(data["file"])
                    pygame.mixer.music.play()
                except Exception:
                    messagebox.showwarning("Missing File", f"Audio file not found: {data['file']}")
            threading.Thread(target=update_lyrics, args=(data["lyrics"],), daemon=True).start()

        # Buttons
        button_style = {"font": ("Consolas", 14), "bg": "#1e1e1e", "fg": "#00ff99", "width": 12, "height": 1}

        tk.Button(self, text="▶ Play", command=play_song, **button_style).pack(pady=10)
        tk.Button(self, text="📂 Load Audio", command=self.load_music_file, **button_style).pack(pady=5)

        tk.Button(
        self,
        text="🔙 Back to Menu",
        command=self.main_menu,
        font=("Consolas", 12),
        bg="#330000",
        fg="#ff5555",
        width=18,
        height=1
        ).pack(pady=40)

    # --- FEATURE 3: PIXEL CAR DASHBOARD ---
    def feature_dashboard(self):
        for widget in self.winfo_children():
            widget.destroy()

        canvas = tk.Canvas(self, width=900, height=600, bg="#0a0a0a", highlightthickness=0)
        canvas.pack()

        def draw_dashboard():
            canvas.create_text(450, 60, text="🚗 PIXEL DASHBOARD", font=("Consolas", 26, "bold"),
                               fill="#00ff99")
            canvas.create_rectangle(150, 150, 750, 500, fill="#111111", outline="#00ff99", width=3)
            canvas.create_text(450, 180, text="Speed: 80 km/h", font=("Consolas", 20), fill="white")
            canvas.create_text(450, 220, text="Fuel: ███████░░ 70%", font=("Consolas", 20), fill="#00ff99")
            canvas.create_text(450, 260, text="Engine Temp: 73°C", font=("Consolas", 20), fill="orange")
            canvas.create_text(450, 300, text="Music: Blue by Kai", font=("Consolas", 18), fill="cyan")

            for i in range(5):
                canvas.create_rectangle(300 + i * 60, 400, 330 + i * 60, 430, fill="#00ff99", outline="#0f0")

        draw_dashboard()
        tk.Button(self, text="Back to Menu", command=self.main_menu,
                  font=("Consolas", 12), bg="#1e1e1e", fg="#00ff99").pack(pady=20)


if __name__ == '__main__':
    app = ThreeFeatureApp()
    app.mainloop()
