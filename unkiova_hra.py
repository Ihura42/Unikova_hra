import time
import random
import sys

inventory = ["sword"]

def game_end():
    print("The end of the game")
    sys.exit()

def end_game():
    print("You win. You made it to the end")
    game_end()

def dragon_fight():
    player_health = 100
    dragon_health = 400
    player_add = 0
    show_inventory()
    if "sword" in inventory:
        player_add += 10
        print(f"You have a sword, so your damage is up by 10. Now your additional damage is {player_add}")
        time.sleep(1)
    if "blade" in inventory:
        player_add += 20
        print(f"You have a blade, so your damage is up by 20. Now your additional damage is {player_add}")
        time.sleep(1)
    if "bow" in inventory:
        player_add += 15
        print(f"You have a bow, so your damage is up by 15. Now your additional damage is {player_add}")
        time.sleep(1)
    if "greataxe" in inventory:
        player_add += 25
        print(f"You have a greataxe, so your damage is up by 25. Now your additional damage is {player_add}")
        time.sleep(1)
    if "book" in inventory:
        player_add += 50
        print(f"You have a book, so your damage is up by 50. Now your additional damage is {player_add}")
        time.sleep(1)
    if "strength_potion" in inventory:
        player_add += 20
    if "health_potion" in inventory:
        player_health += 30      
    while player_health > 0 and dragon_health > 0:  
        player_damage = random.randint(10,20) + player_add
        dragon_health -= player_damage
        if dragon_health < 0:
            dragon_health = 0
        print(f"You attack the dragon for {player_damage} damage. Dragon's health: {dragon_health}")
        time.sleep(2)
        if dragon_health <= 0:
            print("You defeated the dragon!")
            time.sleep(2)
            end_game()
        dragon_damage = random.randint(5, 15)
        player_health -= dragon_damage
        print(f"The dragon attacks you for {dragon_damage} damage. Your health: {player_health}")
        time.sleep(2)
        if player_health <= 0:
            print("You were defeated by the dragon. Game Over.")
            time.sleep(2)
            game_end()    

def fog():
    print("You're clearing a path to the castle. You're almost to the castle and a dragon appears. Prepare for the final battle")
    time.sleep(2)
    dragon_fight() 
               
def easy_way():
    print("You're walking down a very dark tunnel.")
    time.sleep(2)
    print("It is very narrow and you can't see anything in front of you.")
    time.sleep(2)
    print("Then you see the light in front of you.")
    time.sleep(2)
    print("You walk over. It looks like a castle.")
    time.sleep(2)
    print("Congratulations, you've made it through the easy way.")
    time.sleep(2)
    end_game()

def show_inventory():
    print("Your inventory:")
    time.sleep(1)
    for i in inventory:
        time.sleep(0.5)
        print(i)

def market():
    print("You see a shop and a salesman.")
    time.sleep(2)
    print("Saleman: - Do you want to buy something from me?")
    choice = input("y/n")
    
    if choice == "y":
        if "blade" in inventory or "greataxe" in inventory or "bow" in inventory:
            print("Saleman: - Sorry. You already chose your weapon")
            time.sleep(2)
        else:
            print("Saleman: - You can choose ONLY ONE thing")
            time.sleep(2)
            print("Saleman: - YOU can get from me:")
            print("1.Blade")
            print("2.Greataxe")
            print("3.Bow")
            shop_choice = input("Choose one(1/2/3)")
            if shop_choice == "1":
                inventory.append("blade")
                time.sleep(2)
            elif shop_choice == "2":  
                inventory.append("greataxe")
                time.sleep(2)
            elif shop_choice == "3":  
                inventory.append("bow")
                time.sleep(2)
            else:
                print("You made a mistake")
                time.sleep(2)
    print("You have a choice.")
    time.sleep(2)
    print("Continue on to the castle(1) or go back?(2)")
    time.sleep(1)
    way_choice = input("Write 1 or 2")
    if way_choice == "1":
        print("You walk along and more and more fog appears.")
        time.sleep(2)
        print("You can't see anything in front of you and you walk deeper and deeper into the swamps.")
        if "torch" in inventory:
            print("You walk through the fog, because you have a torch.")
            time.sleep(2)
            fog()
        else:
            print("I can not continue. I need a torch")
            time.sleep(2)
            market()    
    elif way_choice == "2":
        river()                
  
def monster_lair():
    print("Very dark and scary")
    time.sleep(1)
    print("Up ahead you see a big cave monster")
    time.sleep(1)
    print("The fight begins")
    time.sleep(2)
    show_inventory()
    time.sleep(1)
    player_health = 100
    monster_health = 150
    while player_health > 0 and monster_health > 0:  
        player_damage = random.randint(10,20)
        monster_health -= player_damage
        if monster_health < 0:
            monster_health = 0
        print(f"You attack the monster for {player_damage} damage. Monster's health: {monster_health}")
        time.sleep(2)
        if monster_health <= 0:
            print("You defeated the monster!")
            end_game()
        monster_damage = random.randint(5, 15)
        player_health -= monster_damage
        print(f"The monster attacks you for {monster_damage} damage. Your health: {player_health}")
        time.sleep(2)
        if player_health <= 0:
            print("You were defeated by the monster. Game Over.")
            game_end()

def alchemist():
    if "strength_potion" in inventory or "health_potion" in inventory:
        print("You can not take it twice. Go back!")
        church()
    else:    
        print("You went to the alchemist. He offered two potions.")
        time.sleep(1)
        print("Strength(1) or health(2).")
        time.sleep(2)
        choice = input("Which do you want?(1/2)")
        if choice == "1":
            print("You got strength potion.")
            inventory.append("strength_potion")
        elif choice == "2":
            print("You got heal potion.")
            inventory.append("heal_potion")
        else: 
            print("You make a mistake")    
        print("There's no other way. I have to go back") 
        time.sleep(2)
        church()            

def rocks():
    print("As you approach the rocks, you see a huge cave.")
    choice = input("Should I go in? y/n: ")
    if choice == "y":
        print("It's very dark.")
        time.sleep(1)
        print("Walking through the rocks, you see an elf.")
        time.sleep(1)
        print("There are also two more paths.")
        print("1. Talk to the elf")
        print("2. Go left")
        print("3. Go right")
        elf_choice = input("Choose one")
        if elf_choice == "1":
            if "jack_ask" in inventory:
                Jack_speech = input("Do you want to speak(1) or choose path?(2)? 1/2: ")
                if Jack_speech == "1":
                    print("I'm from Jack. You have to give him something.")
                    time.sleep(2)
                    print("-Yeah. Here you go.")
                    time.sleep(2)
                    inventory.append("Jack's_thing")
                    forest()
                elif Jack_speech == "2":
                    print("Then choose two paths. The left is short and the right is long.")
                    time.sleep(1)
                    path_choice = input("Choose short(1) or long(2) or go back(3): ")
                    if path_choice == "1":
                        monster_lair()
                    elif path_choice == "2":
                        easy_way()
                    elif path_choice == "3":
                        forest()
            else:
                print("You can't talk to the elf without 'jack_ask' in your inventory.")
                time.sleep(1)
                print("Then choose two paths. The left is short and the right is long.")
                path_choice = input("Choose short(1) or long(2) or go back(3): ")
                if path_choice == "1":
                    monster_lair()
                elif path_choice == "2":
                    easy_way()
                elif path_choice == "3":
                    forest()
        elif elf_choice == "2":
            monster_lair()
        elif elf_choice == "3":
            easy_way()    
                                


def bridge():
    print("You see the bridge. It's destroyed and without boards and nails you can't cross it.")
    time.sleep(2)
    if "boards and nails" in inventory:
        print("Now I can get to the castle. ")
        time.sleep(2)
        choice = input("Go to the castle(1) or go back(2)")
        if choice == "1":
            print("You crossed the bridge. You're getting closer to the castle. Suddenly a dragon appears.")
            time.sleep(3)
            dragon_fight()
        elif choice == "2":
            forest()    
    else:
        print("You may need an additional item or look for another way.") 
        time.sleep(2)
        forest()           

def hut():
    print("You're walking through a dark forest. ")
    time.sleep(1)
    print("There is a hut up ahead and someone is clearly living in it.")
    time.sleep(1)
    print("There's a hermit.")
    time.sleep(1)

    print("Hermit: -My name is Jack.")
    time.sleep(1)
    print("Jack: -Do what I ask and then we'll talk.")
    time.sleep(1)
    print("Jack: -Get the thing from the elf. He will be in a cave")
    time.sleep(1)

    if "Jack's_thing" in inventory:
        print("Jack: - All right, thank you. What do you want in return?")
        time.sleep(1)
        jack_choice = input("Write what do you want. 1.Torch 2.Boards and nails")
        if jack_choice == "1":
            inventory.append("torch")
            print("You received a torch.")
            inventory.append("torch")
        elif jack_choice == "2":
            inventory.append("board and nails")
            print("You received boards and nails.")
            inventory.append("boards and nails")
        else:
            print("You have a problem")
    else:
       print("Jack: -Come back when you've completed the elf's quest.")

    time.sleep(1)
    print("There's nothing more for me to do here. I should go back.")
    inventory.append("jack_ask")
    time.sleep(3)
    forest()    

def forest():
    print("You walked through the dark forest.")
    time.sleep(2)
    if "wolf_tusk" not in inventory:
        print("Something rustled in the bushes")
        time.sleep(1)
        print("A wolf jumped out at you")
        time.sleep(1)
        print("The fight was started")
        time.sleep(1)
        player_health = 100
        wolf_health = 50
        while player_health > 0 and wolf_health > 0:
            player_damage = random.randint(10, 20)
            wolf_health -= player_damage
            print(f"You do {player_damage} damage. Wolf's health: {wolf_health}")
            time.sleep(1)
            if wolf_health <= 0:
                print("You won")
                inventory.append("wolf_tusk")
                break
            wolf_damage = random.randint(5, 15)
            player_health -= wolf_damage
            print(f"Wolf do {wolf_damage} damage. Your health: {player_health}")
            time.sleep(1)
            if player_health <= 0:
                game_end()
    print("You have 3 paths")
    print("1.Go to the hut")
    print("2.Go to the bridge")
    print("3.Go to the rocks")
    print("4.Go back")
    choice =  int(input("Choose one of pathes"))
    if choice == 1:
        print("You go to the hut")
        hut()
    elif choice == 2:
        print("You go to the bridge")
        bridge()
    elif choice == 3:
        print("You go to the rocks")
        rocks()
    elif choice == 4:
        print("return back")
        start()    
    else:
        print("You have a mistake")

def river():
    print("You walk for a long time and you see a river in front of you.")
    time.sleep(1)

    choice = input("Do you want to go straight(1) or go back to start(2)?")
    if choice == "1":
        market()
    elif choice == "2":
        start()    
        
    

def church():
    print("In front of you is a large, ancient church.")
    time.sleep(1)
    church_pray = input("Should i pray? y/n")
    if church_pray == "y":
        print("You walked into a church and saw a large number of books and decided to take a look.")
        time.sleep(2)
        print("There was a book about the dragon's weaknesses.")
        time.sleep(1)
        print("You recieved a book")
        inventory.append("book")
    print("There's a way to alchemist(1) or to the start(2)")
    time.sleep(1)
    choice = input("Go there(1) or go back(2)? 1/2")
    if choice == "1":
        alchemist()
    elif choice == "2":
        start()    
        

def start():
    print("You have 3 paths")
    print("1.Go to the forest")
    print("2.Go to the castle")
    print("3.Go to the church")
    choice =  int(input("Choose one of pathes"))
    if choice == 1:
        print("You go to the forest")
        forest()
    elif choice == 2:
        print("You go to the river")
        river()
    elif choice == 3:
        print("You go to the church")
        church()
    else:
        print("You have a mistake")   


while True:
    show_inventory()  
    start()
