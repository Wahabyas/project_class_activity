import random
import time


def calculate_fuel(distance, speed, style):
    """Estimate fuel consumption (L) based on speed and driving style"""
    base_efficiency = 15  # km per liter for ideal driving

    if style == "aggressive":
        base_efficiency -= 5
    elif style == "normal":
        base_efficiency -= 2
    elif style == "eco":
        base_efficiency -= 0

    # Speed effect
    if speed > 100:
        base_efficiency -= (speed - 100) / 10
    elif speed < 40:
        base_efficiency -= 1

    base_efficiency = max(5, base_efficiency)
    fuel_used = distance / base_efficiency
    return round(fuel_used, 2)

def calculate_emissions(fuel_used):
    CO2_per_liter = 2.31
    return round(fuel_used * CO2_per_liter, 2)

def give_advice(style, speed):
    """Return a string of eco-driving advice"""
    advice = []
    if style == "aggressive":
        advice.append("Avoid rapid acceleration and sudden braking.")
        advice.append("Try smoother driving to save fuel.")
    elif style == "normal":
        advice.append("Maintain steady speeds for better fuel economy.")
        advice.append("Consider switching to eco-driving habits!")
    else:
        advice.append("Excellent! Eco-driving reduces emissions and saves money.")

    if speed > 100:
        advice.append("Driving slower (below 100 km/h) improves fuel efficiency.")
    elif speed < 40:
        advice.append("Driving too slow can also waste fuel in lower gears.")
    
    return advice

def trip_round(destination, distance, score):
    print(f"\n📍 New Trip: {destination} ({distance} km)")
    print("Plan your driving wisely!")

    try:
        speed = float(input("Enter your average speed (km/h): "))
        style = str(input("Driving style (eco / normal / aggressive): ").strip().lower())

        fuel_used = calculate_fuel(distance, speed, style)
        emissions = calculate_emissions(fuel_used)

        print("\n--- Trip Report ---")
        print(f"Distance: {distance} km")
        print(f"Average Speed: {speed} km/h")
        print(f"Style: {style.capitalize()}")
        print(f"Fuel Used: {fuel_used} L")
        print(f"CO₂ Emitted: {emissions} kg")

        # Scoring logic
        if style == "eco" and speed <= 100:
            gain = 20
        elif style == "normal":
            gain = 10
        else:
            gain = 5
        
        if emissions > 25:
            gain -= 3

        score += max(gain, 0)

        # Advice
        advice = give_advice(style, speed)
        print("\n🚦 Driving Tips:")
        for line in advice:
            print("-", line)

        time.sleep(1)
        print(f"\n⭐ Trip Score: +{gain} points!")
        print(f"🏁 Total Score: {score}\n")
        time.sleep(1)

        return score

    except ValueError:
        print("❌ Invalid input! Skipping this trip...")
        return score

def main():
    print("=== 🚗 FUEL EFFICIENCY CHALLENGE ===")
    print("Test your driving habits and learn how to drive greener!\n")

    destinations = [
        ("Downtown City", 50),
        ("Mountain Pass", 80),
        ("Coastal Highway", 120),
        ("Countryside Route", 60),
        ("Industrial Zone", 100)
    ]

    random.shuffle(destinations)
    score = 0

    for i, (place, distance) in enumerate(destinations, start=1):
        print(f"\n==== Trip {i} of {len(destinations)} ====")
        score = trip_round(place, distance, score)

    print("\n=== 🏆 GAME OVER ===")
    print(f"Your Final Score: {score}")

    if score >= 80:
        rating = "🌿 Eco Master — you're a model driver!"
    elif score >= 50:
        rating = "🚘 Responsible Driver — great effort!"
    else:
        rating = "⚠️ Fuel Waster — try driving smoother next time."

    print(f"Rating: {rating}")
    print("\nThank you for promoting sustainable driving habits! 🌍")

if __name__ == "__main__":
    main()
