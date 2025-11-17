import time
import threading
import os
import sys

try:
    import pygame
    pygame.init()
    pygame.mixer.init()
    HAS_PYGAME = True
except:
    HAS_PYGAME = False


#     SIGNBOARD QUIZ


from Music_Lyrics import playlist

def feature_quiz():
    quiz_data = [
    ("🚫 NO ENTRY", ["No Entry", "Go Ahead", "Stop", "Parking"], "No Entry"),
    ("⚠️ SLIPPERY ROAD", ["Turn Left", "Slippery Road", "Pedestrian", "Stop"], "Slippery Road"),
    ("🅿️ PARKING", ["Hospital", "No Parking", "Parking", "Gas Station"], "Parking"),
    ("🚦 TRAFFIC LIGHT AHEAD", ["Traffic Light Ahead", "Stop", "One Way", "Speed Limit"], "Traffic Light Ahead"),
    ("🛑 STOP", ["Stop", "Yield", "No Entry", "Parking"], "Stop"),
    ("↪️ ONE WAY", ["No Entry", "One Way", "Slippery Road", "Stop"], "One Way"),
    ("⚡ ELECTRIC VEHICLE CHARGING", ["Gas Station", "Electric Vehicle Charging", "Parking", "Hospital"], "Electric Vehicle Charging"),
    ("👷 CONSTRUCTION AREA", ["Construction Area", "School Zone", "Parking", "Stop"], "Construction Area"),
    ("🚸 SCHOOL ZONE", ["School Zone", "Pedestrian Crossing", "Slippery Road", "Stop"], "School Zone"),
    ("↩️ U-TURN", ["No U-Turn", "U-Turn Allowed", "Parking", "Stop"], "U-Turn Allowed"),
    ("🛣️ HIGHWAY", ["Highway", "Slippery Road", "Parking", "No Entry"], "Highway"),
    ("🚧 ROAD CLOSED", ["Road Closed", "One Way", "Stop", "Parking"], "Road Closed"),
    ("⛔ NO PARKING", ["No Parking", "Parking", "Slippery Road", "Stop"], "No Parking"),
    ("🚶 PEDESTRIAN CROSSING", ["Pedestrian Crossing", "Stop", "One Way", "Parking"], "Pedestrian Crossing"),
]


    print("\n=== SIGNBOARD QUIZ ===\n")
    score = 0

    for idx, (sign, options, answer) in enumerate(quiz_data, 1):
        print(f"Question {idx}: Signboard: {sign}")
        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")

        while True:
            choice = input("\nChoose answer (1-4) or 'Q' to quit: ").lower()
            if choice == 'q':
                print("\nYou quit the quiz.\n")
                print(f"Your score: {score}/{len(quiz_data)}\n")
                return
            elif choice.isdigit() and int(choice) in range(1, 5):
                selected = options[int(choice)-1]
                if selected == answer:
                    print("✅ Correct!\n")
                    score += 1
                else:
                    print(f"❌ Wrong! The correct answer was: {answer}\n")
                break
            else:
                print("Invalid input. Enter 1-4 or 'q' to quit.")

        time.sleep(1)

    print(f"🎉 Quiz completed! Your final score: {score}/{len(quiz_data)}\n")








stop_lyrics_flag = False


def type_lyrics(lyrics):
    global stop_lyrics_flag
    last_time = 0

    for t, line in lyrics:
        if stop_lyrics_flag:
            return
        time.sleep(max(0, t - last_time))
        last_time = t

       
        for c in line:
            if stop_lyrics_flag:
                return
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.05)  
        print("\n")  

def feature_music():
    global stop_lyrics_flag

    print("\n=== MUSIC PLAYER ===\n")

    print("Available tracks:")
    for i, song in enumerate(playlist.keys(), 1):
        print(f"{i}. {song}")

    choice = input("\nSelect song number: ")
    if not choice.isdigit() or int(choice) not in range(1, len(playlist) + 1):
        print("Invalid choice.")
        return

    song_name = list(playlist.keys())[int(choice) - 1]
    song = playlist[song_name]

    print(f"\n▶ Now Playing: {song_name}\n")

    stop_lyrics_flag = False  


    if HAS_PYGAME:
        try:
            pygame.mixer.music.load(song["file"])
            pygame.mixer.music.play()
        except:
            print("⚠ Cannot play audio file.")


    lyrics_thread = threading.Thread(target=type_lyrics, args=(song["lyrics"],), daemon=True)
    lyrics_thread.start()


    input("\nPress ENTER to stop the music...\n")
    stop_lyrics_flag = True
    if HAS_PYGAME:
        pygame.mixer.music.stop()

    print("⏹ Music stopped.\n")




#      DASHBOARD

speed = 0
fuel = 100
engine_temp = 70
running_dashboard = False
lock = threading.Lock()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_dashboard():
    global speed, fuel, engine_temp, running_dashboard
    while running_dashboard:
        clear_console()
        print("=== PIXEL CAR DASHBOARD ===\n")
        print(f"""
    ┌───────────────────────────────────────────────┐
    │                🚗 PIXEL DASHBOARD              │
    ├───────────────────────────────────────────────┤
    │ Speed: {speed:3} km/h                             │
    │ Fuel: [{'█'*int(fuel/10)}{'░'*(10-int(fuel/10))}] {fuel}%                         │
    │ Engine Temp: {engine_temp}°C                        │
    ├───────────────────────────────────────────────┤
    │  [░░░░░] [░░░░░] [░░░░░] [░░░░░] [░░░░░]       │
    └───────────────────────────────────────────────┘
        """)
        print("\nControls: [a] Accelerate | [b] Brake | [r] Refuel | [q] Quit")
        time.sleep(0.5)

def fuel_consumption():
    global speed, fuel, running_dashboard, engine_temp
    while running_dashboard:
        if speed > 0:
            with lock:
                fuel -= speed * 0.05
                engine_temp += 0.05 * speed  # 
                if fuel < 0:
                    fuel = 0
                    speed = 0
                    engine_temp = 70
        time.sleep(1)

def user_input_dashboard():
    global speed, fuel, running_dashboard
    while running_dashboard:
        cmd = input("Enter command: ").lower()
        with lock:
            if cmd == 'a':
                if fuel > 0:
                    speed += 10
                    if speed > 200:
                        speed = 200
                else:
                    print("⚠ No fuel! Refuel first.")
            elif cmd == 'b':
                speed -= 10
                if speed < 0:
                    speed = 0
            elif cmd == 'r':
                fuel += 20
                if fuel > 100:
                    fuel = 100
            elif cmd == 'q':
                running_dashboard = False
            else:
                print("Invalid command!")

def feature_dashboard():
    global running_dashboard
    running_dashboard = True
    threading.Thread(target=draw_dashboard, daemon=True).start()
    threading.Thread(target=fuel_consumption, daemon=True).start()
    user_input_dashboard()
    print("\nExiting dashboard...\n")



#           MAIN MENU

def main_menu():
    while True:
        print("\n==============================")
        print("     🚗 EchoDrive Terminal")
        print("==============================\n")
        print("1. Signboard Quiz")
        print("2. Music + Lyrics")
        print("3. Pixel Dashboard")
        print("4. Exit")

        choice = input("\nChoose a feature (1-4): ")

        if choice == '1':
            feature_quiz()
        elif choice == '2':
            feature_music()
        elif choice == '3':
            feature_dashboard()
        elif choice == '4':
            print("\nGoodbye!\n")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main_menu()
