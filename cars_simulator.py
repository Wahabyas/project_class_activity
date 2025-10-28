

engine_running = False  

while True:
    command = input("Enter command (start/stop/quit): ").lower()
    if command == "start":
        if engine_running:
            print("Engine is already running.")
        else:
            engine_running = True
            print("Engine started...")
    
    elif command == "stop":
        
        if not engine_running:
            print("Engine is already stopped.")
        else:
            engine_running = False
            print("Engine stopped.")
    
    elif command == "quit":
        print("Exiting program. Goodbye!")
        break
    
    else:
        print("I don't understand that.")
