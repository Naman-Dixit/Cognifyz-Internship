# Welcome Message
print("🏚️ Welcome to the Haunted Mansion!")
print("You are a distant family member who has inherited the mansion from your late uncle.")
print("As you explore the mansion, you discover that it is haunted by ghosts.")
print("The mansion is old, creepy, and full of secrets.")
print("You must solve puzzles and uncover mysteries to escape alive.\n")

# First Choice
choice = input("Do you want to enter the living room? (yes/no): ").lower()

if choice == "yes":
    print("\nYou enter the living room.")
    print("A ghostly figure appears!")
    print("'Welcome,' it whispers. 'To escape, you must explore three rooms.'")
    print("Rooms available: library, kitchen, basement\n")

    room_choice = input("Which room do you want to enter first? (library/kitchen/basement): ").lower()

    if room_choice == "library":
        print("\n📚 You enter the library.")
        print("You find an old diary with a hidden password inside.")
        print("The password opens the main gate. You escape safely!")
    
    elif room_choice == "kitchen":
        print("\n🍳 You enter the kitchen.")
        print("You find a strange recipe book with a hidden map.")
        print("The map leads you to a secret basement exit.")
        print("You escape the mansion!")
    
    elif room_choice == "basement":
        print("\n🕯️ You enter the dark basement.")
        print("A locked chest sits in the corner.")
        code = input("Enter a 3-digit code to open the chest: ")

        if code == "777":
            print("The chest opens! Inside is a key to the front gate.")
            print("You unlock the gate and escape!")
        else:
            print("Wrong code! The ghosts catch you...")
            print("💀 GAME OVER.")
    
    else:
        print("Invalid room choice. The ghost disappears. GAME OVER.")

elif choice == "no":
    print("\nYou decide to leave the mansion.")
    print("Maybe some mysteries are better left unsolved.")
    print("GAME OVER.")

else:
    print("Invalid input. Please restart the game.")
