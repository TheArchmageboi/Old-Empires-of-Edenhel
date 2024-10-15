import os
import time
import random

# Global settings
settings = {
    "text_speed": 0.05,  # Default text speed
    "difficulty": "Normal"
}

# Global player stats and character data
player = {
    "name": "",
    "gender": "",
    "race": "",
    "class": "",
    "attributes": {"Strength": 0, "Agility": 0, "Intelligence": 0, "Vitality": 0},
    "HP": 0,
    "Grain": 0,
    "Stamina": 0,
    "background": "",
    "skills": [],
    "magic_skills": {"Fire Magic": 0, "Water Magic": 0, "Earth Magic": 0, "Air Magic": 0},
    "non_magic_skills": {}
}

# Name pools for random names
male_names = ["Eldric", "Cynric", "Godwin", "Leofric", "Beorn", "Aldhelm"]
female_names = ["Edith", "Elfrida", "Wulfstan", "Hereward", "Gwen", "Anya"]

# Classes and initial stats based on user input
classes = {
    "Magic-User": {"HP": 10, "Grain": 50, "Stamina": 20},
    "Fighter": {"HP": 30, "Grain": 10, "Stamina": 40},
    "Priest": {"HP": 15, "Grain": 40, "Stamina": 25},
    "Thief": {"HP": 20, "Grain": 20, "Stamina": 35}
}

# Races with their skill bonuses and unique attributes
races = {
    "Edish (Human)": {
        "HP Bonus": 0,
        "Grain Bonus": 0,
        "Stamina Bonus": 0,
        "Skills": ["All skills +15%"],
        "Extra Skills": 5,
        "Base Attributes": {"Strength": 5, "Agility": 5, "Intelligence": 5, "Vitality": 5}
    },
    "Elf": {
        "HP Bonus": -5,
        "Grain Bonus": 20,
        "Stamina Bonus": 0,
        "Skills": ["Archery +15%", "Light Magic +10%", "Nature Lore +10%"],
        "Extra Skills": 3,
        "Base Attributes": {"Strength": 3, "Agility": 7, "Intelligence": 7, "Vitality": 3}
    },
    "Dwarf": {
        "HP Bonus": 10,
        "Grain Bonus": -10,
        "Stamina Bonus": 10,
        "Skills": ["Smithing +15%", "Mining +15%", "Axes +10%"],
        "Extra Skills": 2,
        "Base Attributes": {"Strength": 7, "Agility": 3, "Intelligence": 4, "Vitality": 8}
    },
    "Orc": {
        "HP Bonus": 20,
        "Grain Bonus": -10,
        "Stamina Bonus": 5,
        "Skills": ["Berserking +15%", "Maces +10%", "Intimidation +10%"],
        "Extra Skills": 2,
        "Base Attributes": {"Strength": 8, "Agility": 5, "Intelligence": 2, "Vitality": 8}
    },
    "Lizardfolk": {
        "HP Bonus": 0,
        "Grain Bonus": 5,
        "Stamina Bonus": 10,
        "Skills": ["Swimming +20%", "Survival +10%", "Dark Magic +5%"],
        "Extra Skills": 3,
        "Base Attributes": {"Strength": 6, "Agility": 6, "Intelligence": 4, "Vitality": 6}
    },
    "Yaphelem (Catfolk)": {
        "HP Bonus": -5,
        "Grain Bonus": 0,
        "Stamina Bonus": 15,
        "Skills": ["Stealth +20%", "Climbing +10%", "Hunting +10%"],
        "Extra Skills": 3,
        "Base Attributes": {"Strength": 4, "Agility": 8, "Intelligence": 6, "Vitality": 4}
    },
    "Ratfolk": {
        "HP Bonus": 0,
        "Grain Bonus": 0,
        "Stamina Bonus": 5,
        "Skills": ["Thievery +20%", "Alchemy +10%", "Dark Magic +5%"],
        "Extra Skills": 2,
        "Base Attributes": {"Strength": 4, "Agility": 6, "Intelligence": 6, "Vitality": 5}
    },
    "Mousefolk": {
        "HP Bonus": -5,
        "Grain Bonus": 10,
        "Stamina Bonus": 0,
        "Skills": ["History +20%", "Light Magic +10%", "Swordsmanship +5%"],
        "Extra Skills": 3,
        "Base Attributes": {"Strength": 3, "Agility": 7, "Intelligence": 8, "Vitality": 3}
    },
    "Stone Born": {
        "HP Bonus": 15,
        "Grain Bonus": -10,
        "Stamina Bonus": 10,
        "Skills": ["Stone Lore +15%", "Defense +10%", "Smithing +10%"],
        "Extra Skills": 2,
        "Base Attributes": {"Strength": 9, "Agility": 2, "Intelligence": 3, "Vitality": 9}
    },
    "Random": {}
}

# Skills
skills = [
    "Fire Magic", "Water Magic", "Light Magic", "Dark Magic", "Swordsmanship",
    "Archery", "Axes", "Maces", "Stealth", "Smithing", "Alchemy", "Swimming",
    "Mining", "Survival", "Nature Lore", "History", "Intimidation", "Hunting",
    "Climbing", "Thievery", "Berserking", "Defense", "Cooking"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def title_screen():
    clear_screen()
    print("=======================================")
    print("       The Old Empires of Edenhel      ")
    print("=======================================")
    print("               1. Start New Game       ")
    print("               2. Load Game            ")
    print("               3. Settings             ")
    print("               4. Exit                 ")
    print("=======================================")
    print("Choose an option:")

def main_menu():
    while True:
        title_screen()
        choice = input("> ")
        if choice == '1':
            start_new_game()
        elif choice == '2':
            load_game()
        elif choice == '3':
            settings_menu()
        elif choice == '4':
            exit_game()
        else:
            print("Invalid choice, please select again.")
            time.sleep(1)

def start_new_game():
    clear_screen()
    print("Starting a new game...")
    character_creation()  # Start character creation
    display_character()    # Show the created character
    time.sleep(2)

def load_game():
    clear_screen()
    print("Loading game...")
    # Add load game logic here
    time.sleep(2)

def settings_menu():
    while True:
        clear_screen()
        print("============= Settings ==============")
        print(f"1. Text Speed (Current: {settings['text_speed']})")
        print(f"2. Difficulty (Current: {settings['difficulty']})")
        print("3. Return to Main Menu")
        print("=====================================")
        print("Select an option:")

        choice = input("> ")
        if choice == '1':
            adjust_text_speed()
        elif choice == '2':
            adjust_difficulty()
        elif choice == '3':
            break
        else:
            print("Invalid choice, please select again.")
            time.sleep(1)

def adjust_text_speed():
    clear_screen()
    print("Adjust Text Speed (1 = Slow, 2 = Normal, 3 = Fast):")
    choice = input("> ")
    if choice == '1':
        settings['text_speed'] = 0.1
    elif choice == '2':
        settings['text_speed'] = 0.05
    elif choice == '3':
        settings['text_speed'] = 0.01
    else:
        print("Invalid choice, returning to settings menu.")
        time.sleep(1)

def adjust_difficulty():
    clear_screen()
    print("Adjust Difficulty (1 = Easy, 2 = Normal, 3 = Hard):")
    choice = input("> ")
    if choice == '1':
        settings['difficulty'] = "Easy"
    elif choice == '2':
        settings['difficulty'] = "Normal"
    elif choice == '3':
        settings['difficulty'] = "Hard"
    else:
        print("Invalid choice, returning to settings menu.")
        time.sleep(1)

def exit_game():
    clear_screen()
    print("Exiting the game. Goodbye!")
    time.sleep(2)
    exit()

def character_creation():
    clear_screen()
    print("Character Creation")
    
    # Name selection
    print("Select a name:")
    name_choice = input("Type 'random' for a random name or enter a name: ")
    if name_choice.lower() == "random":
        gender = input("Select gender (M/F): ").upper()
        if gender == "M":
            player["name"] = random.choice(male_names)
        elif gender == "F":
            player["name"] = random.choice(female_names)
        else:
            print("Invalid gender selected. Setting default name.")
            player["name"] = "Hero"
    else:
        player["name"] = name_choice

    # Gender selection
    player["gender"] = input("Select gender (M/F): ").upper()

    # Race selection
    print("Choose your race:")
    for race in races.keys():
        print(f"- {race}")
    player["race"] = input("> ")

    # Class selection
    print("Choose your class:")
    for cls in classes.keys():
        print(f"- {cls}")
    player["class"] = input("> ")

    # Assign stats based on class and race
    player["HP"] = classes[player["class"]]["HP"] + races[player["race"]]["HP Bonus"]
    player["Grain"] = classes[player["class"]]["Grain"] + races[player["race"]]["Grain Bonus"]
    player["Stamina"] = classes[player["class"]]["Stamina"] + races[player["race"]]["Stamina Bonus"]

    # Initialize attributes
    for attribute in player["attributes"]:
        player["attributes"][attribute] = races[player["race"]]["Base Attributes"][attribute]

    # Initialize skills
    player["skills"] = random.sample(skills, races[player["race"]]["Extra Skills"])

def display_character():
    clear_screen()
    print("Character Overview")
    print(f"Name: {player['name']}")
    print(f"Gender: {player['gender']}")
    print(f"Race: {player['race']}")
    print(f"Class: {player['class']}")
    print(f"HP: {player['HP']}")
    print(f"Grain: {player['Grain']}")
    print(f"Stamina: {player['Stamina']}")
    print(f"Attributes: {player['attributes']}")
    print(f"Skills: {', '.join(player['skills'])}")
    print("=======================================")

if __name__ == "__main__":
    main_menu()
