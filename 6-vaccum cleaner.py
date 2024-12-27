def vacuum_cleaner():
    # Get user inputs
    current_location = input("Enter the starting location of the vacuum (A or B): ").strip().upper()
    room_A_status = input("Enter the status of Room A (Clean or Dirty): ").strip().lower()
    room_B_status = input("Enter the status of Room B (Clean or Dirty): ").strip().lower()

    # Validate input
    if current_location not in ['A', 'B']:
        print("Invalid starting location. Please enter A or B.")
        return
    if room_A_status not in ['clean', 'dirty'] or room_B_status not in ['clean', 'dirty']:
        print("Invalid room status. Please enter Clean or Dirty.")
        return

    # Display initial state
    print("\nInitial State:")
    print(f"Room A: {room_A_status.capitalize()}, Room B: {room_B_status.capitalize()}")
    print(f"Vacuum starts at: Room {current_location}\n")

    actions = []
    
    # Cleaning process
    if current_location == 'A':
        if room_A_status == 'dirty':
            actions.append("Clean Room A")
            room_A_status = 'clean'
        actions.append("Move to Room B")
        if room_B_status == 'dirty':
            actions.append("Clean Room B")
            room_B_status = 'clean'
    elif current_location == 'B':
        if room_B_status == 'dirty':
            actions.append("Clean Room B")
            room_B_status = 'clean'
        actions.append("Move to Room A")
        if room_A_status == 'dirty':
            actions.append("Clean Room A")
            room_A_status = 'clean'

    # Display actions
    print("Actions taken:")
    for action in actions:
        print(f"- {action}")

    # Display final state
    print("\nFinal State:")
    print(f"Room A: {room_A_status.capitalize()}, Room B: {room_B_status.capitalize()}")

# Run the vacuum cleaner program
vacuum_cleaner()
