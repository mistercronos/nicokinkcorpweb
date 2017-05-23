import time
import random

print("Dragon Survivor by Nicolas Kress")
print("Special Thanks to:")
print("Nicolas Thollot")
print("Thibault Eid")
print("Clyde Sheridan")
print("Liam Christie")
time.sleep(5)
print("")
print("")
print("")
print("")
print("LOADING...")
print("")
print("")
print("")
print("")
time.sleep(2)

helpr = 1

class bcolors:
    Red = "\033[91m"
    Green = "\033[92m"
    Blank = "\033[0m"
if helpr == 1:
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    e = 'e'
        
    A = a
    B = b
    C = c
    D = d
    E = e
    
    yes = 'yes'
    YES = yes
    Yes = yes 
    yEs = yes
    yeS = yes
    yES = yes
    
    no = 'no'
    No = no
    NO = no
    nO = no
    
    helpr0 = 1
    if helpr0 == 1:
        
        keynum = 0
        carhaskey = False
        
        swordnum = 0
        swordlvl = 0
        carhassword = False
        
        shovelnum = 0
        shovellvl = 0
        carhasshovel = False
        
        birdfreernum = 0
        carhasbirdfreer = False
        
        tchest = 0
        carhastchest = False
        
        carhascode = False
        code = 38427
        
        carhasdragonmask = False
        dragonmasknum = 0
        
        carhasmagiclantern = False
        mlnum = 0
        
        exp = 10
        gold = 10
        capturedKinkies = 100
        freedKinkies = 0
        
        x = random.randint(0 , 5)
        x1 = random.randint(1 , 2)
        
        death = False
        gamerunning = True

print("Hello! Welcome to Dragon Survivor! My name is Kinkily but you can call me Kink. Please, help me and free the other kinkies from the Dragons!")
while gamerunning == True:
    print("What would you like to do?")
    print("A: Start Game")
    print("B: Instructions")
    print("C: Shop")
    print("D: Open Treasure Chests")
    print("E: Quit")
    menustart = input("Enter corresponding letter of choice ")
    death = False
    if menustart == e:
        print("Goodbye! Thanks for playing!")
        gamerunning = False
    elif menustart == b:
        print("Hello. Are you having trouble playing? Well I'll explain the instructions")
        print ("The goal of this game is to find the treasure hidden somewhere in each level")
        print ("Every completed level will give you rewards. It can be coins and experience etc...")
        time.sleep(7)
        print ("You start with 10 gold and 10 experience")
        print ("To find the treasure, you will need to press the letter of your choice to either dig underground, climb a tree, etc...")
        print ("I hope you understand now the concept of this game!")
    elif menustart == c:
        print("What would you like to do?")
        print("A: Buy")
        print("B: Upgrade")
        xy = input("Enter corresponding letter of choice ")
        if xy == a: 
            print("What would you like to buy?")
            print("A: Shovel (5 gold) (Level 1)")
            print("B: Sword (5 gold) (Level 1)")
            print("C: Treasure Chest (3 gold)")
            wtb = input("Enter corresponding letter of choice ")
            if wtb == a:
                if carhasshovel == True:
                    print("You already own this item")
                elif carhasshovel == False:
                    print("Shovel Unlocked")
                    shovelnum = shovelnum + 1
                    carhasshovel = True
                    shovellvl = shovellvl + 1
                    gold = gold - 5
            elif wtb == b:
                if carhassword == True:
                    print("You already own this item")
                elif carhassword == False:
                    print("Sword Unlocked!")
                    swordnum = swordnum + 1
                    carhassword = True
                    swordlvl = 1
                    gold = gold - 5
            elif wtb == c:
                gold = gold - 3
                print("You recieved a tresure chest!")
                tchest = tchest + 1
    elif menustart == a:
        while death == False:
            print("What would you like to do?")
            print("A: Go to the parc ALONE " + bcolors.Red + "(DO NOT DO AT HOME)" + bcolors.Blank)
            print("B: Dig a hole")
            print("C: Climb a tree")
            print("D: Go inside")
            startchoice = input("Enter corresponding letter of choice ")
            if startchoice == a:
                print("You go to the parc. You see an evil dragon attacking the civilians!")
                choice = input("Will you help the civilians? Yes or No ")
                if choice == yes:
                    print("The dragon blows a fire circle around you.")
                    print("You are trapped forever...")
                    death = True
                elif choice == no:
                    print("You run away. 5 Kinkies have been captured!")
                    capuredKinkies = capturedKinkies + 5
            elif startchoice == b:
                print("You dig a hole deep by one foot")
                if carhasshovel == True:
                    if shovellvl == 1:
                        time.sleep(2)
                        print("2 feet")
                        time.sleep(2)
                        print("3 feet")
                        time.sleep(2)
                        print("4 feet")
                        time.sleep(1)
                    elif shovellvl == 2:
                        time.sleep(1.5)
                        print("2 feet")
                        time.sleep(1.5)
                        print("3 feet")
                        time.sleep(1.5)
                        print("4 feet")
                        time.sleep(0.75)
                elif carhasshovel == False:
                        time.sleep(4)
                        print("2 feet")
                        time.sleep(4)
                        print("3 feet")
                        time.sleep(4)
                        print("4 feet")
                        time.sleep(2)
                print("You found a treasure chest!")
                carhastchest = True
                tchest = tchest + 1
                if carhaskey == False:
                    print("You don't have a key to open it. Your chest is now in your inventory.")
                elif carhaskey == True:
                    openchest = input("Open? Yes or No?")
                    if openchest == yes:
                        tchest = tchest - 1
                        keynum = keynum - 1
                        if tchest == 0:
                            carhastchest = False
                        if x == 1:
                            if carhasshovel == False:
                                carhasshovel = True
                                shovelnum = shovelnum + 1
                                shovellvl = 1
                                print("Shovel unlocked!")
                            elif carhasshovel == True:
                                shovelnum = shovelnum + 1
                                shovelvl = shovellvl + 1
                                print("Shovel level improved!")
                        elif x == 3:
                            if carhassword == False:
                                carhassword = True 
                                swordnum = swordnum + 1
                                swordlvl = swordlvl + 1
                                print("Sword Unlocked")
                            elif carhassword == True:
                                swordnum = swordnum + 1
                                swordlvl = swordlvl + 1
                                print("Shovel level upgraded ")
                        else:
                            gold = gold + 5
                            exp = exp + 10
                            print("You recieved 5 gold and 10 experience")
                    else:
                        print("You keep the chest.")
                keepdig = input("Keep digging? Yes or No? ")
                if keepdig == yes:
                    if carhasshovel == True:
                        if shovellvl >= 5:
                            time.sleep(0.5)
                            print("5 feet")
                            time.sleep(1)
                            print("6 feet")
                            time.sleep(1)
                            print("7 feet")
                            time.sleep(1)
                            print("You find a big metal wall in the ground. On it is a keyboard.")
                            if carhascode == True:
                                ask = input("Do you think the code you saw on the paper earlier is the password? Yes or No? ")
                                if ask == yes:
                                    print("You have entered the code. You hear mechanical buzzing...")
                                    time.sleep(2)
                                    print("The wall opens into...")
                                    time.sleep(1)
                                    print("The Dragon Lair!")
                                    if carhasdragonmask == True:
                                        dragonmask = input("Use dragon mask? Yes or No? ")
                                        if dragonmask == yes:
                                            print("The dragons see you. They do  not think you are an intruder. You seen a red button on the other side of the room.")
                                            print("The button says 'ABORT INVASION AND FREE KINKIES'")
                                            pressandend = input("Will you press it? Yes or No? ")
                                            if pressandend == yes:
                                                if capturedKinkies == 100: 
                                                    print("You press it. The dragons are now on your side. The Kinkies are free.")
                                                    print(bcolors.Green + "YOU HAVE WON THE GAME")
                                                    print("Congratulations!" + bcolors.Blank)
                                                    gamerunning = False
                                                    death = True
                                                elif capturedKinkies > 100:
                                                    print("You press it. The dragons are now on your side. The Kinkies are free.")
                                                    time.sleep(3.5)
                                                    print("An Alarm sounds...")
                                                    print("Dragons! They came in the mechanical door you left open!")
                                                    print("These dragons aren't on your side. One of them attacked the civilians at the park!")
                                                    if carhassword == True:
                                                        if swordlvl > 1:
                                                            print("Your sword is strong enough to summon 2 Mages!")
                                                            usetm = input("Use? Yes or No? ")
                                                    elif carhassword == False:
                                                        time.sleep(3.5)
                                                        print("The dragons lock you up.")
                                                        print("You will be sent to a different lair. You will need a key to get out!")
                                                        print("You have not yet lost!")
                                                        time.sleep(5)
                                                        print("WELCOME TO:")
                                                        print("Dragon Survivor 2: THE ESCAPE")
                                                        
                                            elif pressandend == no:
                                                print("Your mask falls off. The dragons see you and lock you up for all eternity with the Kinkies.")
                                                print("You have lost...")
                                                death = True
                                        elif dragonmask == no:
                                            print("Too bad... ")
                                    elif carhasdragonmask == False:
                                        print("The dragons see you. They lock you up for all eternity with the Kinkies...")
                                        print("You have lost")
                                        death = True
                                elif ask == no:
                                    print("Then you must return to the beginning.")
                elif keepdig == no:
                    print("You return to the surface.")
                                
            elif startchoice == c:
                print("You start climbing a tree.")
                time.sleep(3)           
                print("You are at the top. You see a...")
                print("A flying squierrel with a key attached to his foot!")
                if carhassword == True:
                    usesword = input("Use sword? Yes or No? ")
                    if usesword == yes:
                        print("You use your sword. It summons the mage Magisto! He imprisons the squierrel in a big bubble.")
                        print("The bubble turns him into a nice flying squierrel!")
                        print("The flying squierrel gives you the key and 10 exp.")
                        exp = exp + 10
                        carhaskey = True
                        keynum = keynum + 1
                        time.sleep(5)
                elif carhassword == False:
                    print("You need a sword to continue...")
                    buy1 = input("Buy for 5 gold? Yes or No? ")
                    if buy1 == yes:
                        if gold < 5:
                            print("Not enough gold...")
                        elif gold > 5:
                            gold = gold - 5
                            carhassword = True
                            swordnum = swordnum + 1
                            swordlvl = 1
                            print("Sword Unlocked!")
                    if carhassword == True:
                        usesword = input("Use sword? Yes or No? ")
                        if usesword == yes:
                            print("You use your sword. It summons the mage Magisto! He imprisons the squierrel in a big bubble.")
                            print("The bubble turns him into a nice flying squierrel!")
                            print("The flying squierrel gives you the key and 10 exp.")
                            exp = exp + 10
                            carhaskey = True
                            keynum = keynum + 1
                            time.sleep(3.5)

            elif startchoice == d:
                print("You go inside.")
                print("Mother is cooking and Father is in his office.")
                gooutside = input("It starts raining outside. Would you like to go there? Yes or No? ")
                if gooutside == yes:
                    print("You go outside.")
                    time.sleep(1)
                    print("It's cold. You use a tree branch to draw in the mud.")
                    print("What will you draw?")
                    print("A: A Treasure Chest")
                    print("B: A Dragon Mask")
                    print("C: A Sword Level 6")
                    print("D: A Shovel Level 6")
                    print("E: A Magic Lantern")
                    drawing = input("Enter corresponding letter of choice ")
                    print("The Mage Wiseo was passing by.")
                    print("He decides to bring your drawing to life.")
                    time.sleep(3)
                    print("He asks you to hold a piece of paper while he brings your drawing to life. The paper says: 38427")
                    carhascode = True
                    print("You take it.")
                    if drawing == a:
                        print("You recieved a Tresure Chest!")
                        carhastchest = True
                        tchest = tchest + 1
                    elif drawing == b:
                        print("You recieved a Dragon Mask!")
                        carhasdragonmask = True
                        dragonmasknum = dragonmasknum + 1
                    elif drawing == c:
                        print("You recieved a Sword Level 6!")
                        carhassword = True
                        swordnum = swordnum + 1
                        swordlvl = 6
                    elif drawing == d:
                        print("You recieved a Shovel Level 6!")
                        carhasshovel = True
                        shovelnum = shovelnum + 1
                        shovellvl = 6
                    elif drawing == e:
                        print("You recieved a Magic Lantern!")
                        useml = input("Use? Yes or No? ")
                        if useml == yes:
                            print("You use the magic lantern. A geenie appears!")
                            print("The mage Wiseo got scared and ran away leaving the paper in your hands.")
                            print("The Geenie says he will bring to life 2 other drawings you do.")
                            time.sleep(2.5)
                            print("What will you draw?")
                            print("A: A Treasure Chest")
                            print("B: A Dragon Mask")
                            print("C: A Sword Level 6")
                            print("D: A Shovel Level 6")
                            wwd = input("Enter ONE corresponding letter of choice ")
                            if wwd == a:
                                print("You got a Treasure Chest!")
                                tchest = tchest + 1
                                carhastchest = True
                            elif wwd == b:
                                print("You recieved a Dragon Mask!")
                                carhasdragonmask = True
                                dragonmasknum = dragonmasknum + 1
                            elif wwd == c:
                                print("You recieved a Sword Level 6!")
                                carhassword = True
                                swordnum = swordnum + 1
                                swordlvl = 6
                            elif wwd == d:
                                print("You recieved a Shovel Level 6!")
                                carhasshovel = True
                                shovelnum = shovelnum + 1
                                shovellvl = 6
                            print("What will you draw?")
                            print("A: A Treasure Chest")
                            print("B: A Dragon Mask")
                            print("C: A Sword Level 6")
                            print("D: A Shovel Level 6")
                            wwd = input("Enter ONE corresponding letter of choice ")
                            if wwd == a:
                                print("You got a Treasure Chest!")
                                tchest = tchest + 1
                                carhastchest = True
                            elif wwd == b:
                                print("You recieved a Dragon Mask!")
                                carhasdragonmask = True
                                dragonmasknum = dragonmasknum + 1
                            elif wwd == c:
                                print("You recieved a Sword Level 6!")
                                carhassword = True
                                swordnum = swordnum + 1
                                swordlvl = 6
                            elif wwd == d:
                                print("You recieved a Shovel Level 6!")
                                carhasshovel = True
                                shovelnum = shovelnum + 1
                                shovellvl = 6
                            print("You go back inside. It stops raining. You go to your room.")
                print("You wait in your room. You don't do anything.")
                print("You hear Dragons.")
                time.sleep(3)
                print("They imprison you forever with all the other Kinkies...")
                print("You have lost...")
                death = True
    elif menustart == d:
        print("You have:")
        print(tchest)
        if tchest > 1:
            print("Treasure Chests")
        else:
            print("Treasure Chest")
        opentchest = input("Open? Yes or No? ")
        if carhastchest == True:
            while opentchest == yes:
                if opentchest == yes:
                    if x == 1:
                        if carhasshovel == False:
                            carhasshovel = True
                            shovelnum = shovelnum + 1
                            shovellvl = 1
                            print("Shovel unlocked!")
                        elif carhasshovel == True:
                            shovelnum = shovelnum + 1
                            shovelvl = shovellvl + 1
                            print("Shovel level improved!")
                    elif x == 3:
                        if carhassword == False:
                            carhassword = True 
                            swordnum = swordnum + 1
                            swordlvl = swordlvl + 1
                            print("Sword Unlocked")
                        elif carhassword == True:
                            swordnum = swordnum + 1
                            swordlvl = swordlvl + 1
                            print("Shovel level upgraded ")
                    else:
                        gold = gold + 5
                        exp = exp + 10
                        print("You recieved 5 gold and 10 experience")
                    tchest = tchest - 1
                    opentchest2 = input("Keep going? Yes or No? ")               
                    if carhastchest == False:
                        print("Out of chests!")
                        opentchest = no
        elif carhastchest == False:
            print("You have no chests")