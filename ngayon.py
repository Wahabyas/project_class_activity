# car_game_simulation.py
import time
import random
from colorama import Fore, Style, init

init(autoreset=True)

def title_screen():
    print(Fore.CYAN + Style.BRIGHT + "\n🚗 WELCOME TO THE ULTIMATE CAR SIMULATION! 🚗")
    print(Fore.YELLOW + "=" * 60)
    print(Fore.GREEN + "Choose your challenge:")
    print(Fore.MAGENTA + "1. Speed Challenge")
    print(Fore.CYAN + "2. Fuel Management")
    print(Fore.BLUE + "3. Car Race Simulation")
    print(Fore.RED + "4. Exit")
    print(Fore.YELLOW + "=" * 60)


# ---------------------- GAME 1 ----------------------
def speed_challenge():
    print(Fore.GREEN + "\n🏁 SPEED CHALLENGE 🏁")
    print(Fore.YELLOW + "Instructions: When you see 'GO!', press ENTER as fast as you can!")
    time.sleep(random.uniform(2, 4))
    print(Fore.RED + "\nREADY...")
    time.sleep(1)
    print(Fore.YELLOW + "SET...")
    time.sleep(random.uniform(1, 2))
    print(Fore.GREEN + Style.BRIGHT + "\nGO!!!")

    start = time.time()
    input(Fore.CYAN + ">> Press ENTER now! << ")
    reaction = time.time() - start

    if reaction < 0.25:
        print(Fore.MAGENTA + f"🚀 Amazing reflexes! ({reaction:.2f} seconds)")
    elif reaction < 0.5:
        print(Fore.GREEN + f"Great job! ({reaction:.2f} seconds)")
    else:
        print(Fore.RED + f"Too slow! ({reaction:.2f} seconds)")


# ---------------------- GAME 2 ----------------------
def fuel_management():
    print(Fore.CYAN + "\n⛽ FUEL MANAGEMENT SIMULATOR ⛽")
    fuel = 50
    distance = 0
    goal = 100

    while fuel > 0 and distance < goal:
        print(Fore.YELLOW + f"\nFuel: {fuel}L | Distance: {distance}/{goal} km")
        print(Fore.GREEN + "Choose an action:")
        print("1. Drive fast (-10 fuel, +20 km)")
        print("2. Drive slow (-5 fuel, +10 km)")
        print("3. Refuel (+15 fuel, +0 km)")
        choice = input(Fore.CYAN + "Enter choice (1-3): ")

        if choice == "1":
            fuel -= 10
            distance += 20
            print(Fore.MAGENTA + "💨 You sped through the highway!")
        elif choice == "2":
            fuel -= 5
            distance += 10
            print(Fore.GREEN + "🚗 Cruising steadily...")
        elif choice == "3":
            fuel += 15
            print(Fore.BLUE + "⛽ You refueled at a gas station.")
        else:
            print(Fore.RED + "Invalid choice!")
        
        time.sleep(1)

    if distance >= goal:
        print(Fore.GREEN + Style.BRIGHT + "\n🎉 You reached your destination! Great driving!")
    else:
        print(Fore.RED + Style.BRIGHT + "\n💥 You ran out of fuel! Game over!")


# ---------------------- GAME 3 ----------------------
def car_race():
    print(Fore.YELLOW + "\n🏎️ CAR RACE SIMULATION 🏎️")
    cars = ["Red Falcon", "Blue Storm", "Green Arrow"]
    positions = [0, 0, 0]
    finish_line = 50

    print(Fore.CYAN + "The race begins in 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print(Fore.GREEN + Style.BRIGHT + "GO!!!")

    while max(positions) < finish_line:
        for i in range(len(cars)):
            move = random.randint(1, 6)
            positions[i] += move
            bar = "🏁" * (positions[i] // 2)
            print(f"{Fore.MAGENTA}{cars[i]}: {bar}")
        print(Fore.YELLOW + "-" * 60)
        time.sleep(0.5)

    winner = cars[positions.index(max(positions))]
    print(Fore.GREEN + Style.BRIGHT + f"\n🏆 The winner is {winner}! 🏆")


# ---------------------- MAIN MENU ----------------------
def main():
    while True:
        title_screen()
        choice = input(Fore.CYAN + "\nEnter your choice (1-4): ")

        if choice == "1":
            speed_challenge()
        elif choice == "2":
            fuel_management()
        elif choice == "3":
            car_race()
        elif choice == "4":
            print(Fore.MAGENTA + "Goodbye! Thanks for playing! 🚗💨")
            break
        else:
            print(Fore.RED + "Invalid choice! Please select 1-4.")

        input(Fore.YELLOW + "\nPress ENTER to return to main menu...")
        print("\n" * 3)

if __name__ == "__main__":
    main()
