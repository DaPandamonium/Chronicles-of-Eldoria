print('''



                                                                              
                                                                              
                                 ____                                         
                              .-"    `-.      ,                               
                            .'          '.   /j\                              
                           /              \,/:/#\                /\           
                          ;              ,//' '/#\              //#\          
                          |             /' :   '/#\            /  /#\         
                          :         ,  /' /'    '/#\__..--""""/    /#\__      
                           \       /'\'-._:__    '/#\        ;      /#, """---
                            `-.   / ;#\']" ; """--./#J       ':____...!       
                               `-/   /#\  J  [;[;[;Y]         |      ;        
""""""---....             __.--"/    '/#\ ;   " "  |     !    |   #! |        
             ""--.. _.--""     /      ,/#\'-..____.;_,   |    |   '  |        
                   "-.        :_....___,/#} "####" | '_.-",   | #['  |        
                      '-._      |[;[;[;[;|         |.;'  /;\  |      |        
                      ,   `-.   |        :     _   .;'    /;\ |   #" |        
                      !      `._:      _  ;   ##' .;'      /;\|  _,  |        
                     .#\"""---..._    ';, |      .;{___     /;\  ]#' |__....--
          .--.      ;'/#\         \    ]! |       "| , """--./_J    /         
         /  '%;    /  '/#\         \   !' :        |!# #! #! #|    :`.__      
        i__..'%] _:_   ;##J         \      :"#...._!   '  "  "|__  |    `--.._
         | .--""" !|""""  |"""----...J     | '##"" `-._       |  """---.._    
     ____: |      #|      |         #|     |          "]      ;   ___...-"T,  
    /   :  :      !|      |   _______!_    |           |__..--;"""     ,;MM;  
   :____| :    .-.#|      |  /\      /#\   |          /'               ''MM;  
    |""": |   /   \|   .----+  ;      /#\  :___..--"";                  ,'MM; 
   _Y--:  |  ;     ;.-'      ;  \______/#: /         ;                  ''MM; 
  /    |  | ;_______;     ____!  |"##"""MM!         ;                    ,'MM;
 !_____|  |  |"#"#"|____.'""##"  |       :         ;                     ''MM  
  | """"--!._|     |##""         !       !         :____.....-------"""""" |'
  |          :     |______                        ___!_ "#""#""#"""#"""#"""|  
__|          ;     |MM"MM"""""---..._______...--""MM"MM]                   |   
  "\-.      :      |#                                  :                   |  
    /#'.    |      /##,                                !                   |  
   .',/'\   |       #:#,                                ;       .==.       |  
  /"\'#"\',.|       ##;#,                               !     ,'||||',     |  
        /;/`:       ######,          ____             _ :     M||||||M     |  
       ###          /;"\.__"-._   """                   |===..M!!!!!!M_____|  
                           `--..`--.._____             _!_                    
                                          `--...____,="_.'`-.____        fsc



''')


# The story - Welcome Message
print("Chronicles of Eldoria: Shadows and Secrets | The Shadowy Figure")
print("The player's ultimate goal is to uncover the Lost Relic of Eldoria, a legendary artifact said to grant immense power and wisdom.\nIt's hidden somewhere within the castle, and the player must solve its mysteries to find it.\n")

#Explain the mission and the game
print("Unveil the secrets of Eldoria Castle and find the Lost Relic to uncover its power.")
print("Navigate the castle, make critical decisions, solve puzzles, and find the Lost Relic!\n")

#The player's name
player_name = input("Brave adventurer, what is your name: ")
print("Good luck, " + player_name + "let the adventure begin!\n")

#Story of the game and the player's choices
print("As a young adventurer, you must navigate through the castle, encountering various scenarios where they must choose their actions wisely.\n")
print(f"Welcome, {player_name}! Your mission is to uncover the Lost Relic hidden within Eldoria Castle.")
  
def start_adventure():
    choice1 = input("You enter the grand main hall. Do you go to the 'left' to the Ancient Library or 'right' to the Shadowy Dungeons? ").lower()
    
    if choice1 == "left":
        ancient_library()
    elif choice1 == "right":
        shadowy_dungeons()
    else:
        print("That's not a valid direction in the castle. Let's try again.")
        start_adventure()

def ancient_library():
    print("You're in the Ancient Library, surrounded by relics of knowledge and forgotten lore.")
    choice = input("Do you 'search' the ancient texts, try to 'solve' the mural puzzle, or 'examine' the celestial scroll? ").lower()

    if choice == "search":
        print("Rummaging through the shelves, you discover a hidden piece of a map, tucked away in a forgotten tome.")
        return ancient_library()  
    elif choice == "solve":
        print("Focused on the mural, you decipher its secrets and unearth a mysterious key, buried beneath the surface.")
        return ancient_library()  
    elif choice == "examine":
        print("You unfurl a dusty scroll titled 'Celestial Guides of the Ancients.' It speaks of several stars significant to the ancient civilization. Vega is highlighted as 'the beacon in the night, guiding the path to wisdom.' This star's importance is underscored, suggesting its key role not just in the night sky but perhaps in unlocking secrets within the tower.")
        
        return ancient_library()
    else:
        print("Unsure of what to do next, you decide to head back to the main hall, the heart of your adventure.")
        start_adventure()

def shadowy_dungeons():
    print("You're in the Shadowy Dungeons.")
    choice = input("Do you 'navigate' the traps or attempt to 'disarm' them? ").lower()

    if choice == "navigate":
        print("You find a passage leading to a secret room.")
        tower_observatory()
    elif choice == "disarm":
        print("You acquire valuable ancient artifacts.")
        underground_vault()
    else:
        print("Feeling overwhelmed, you return to the main hall for a different path.")
        start_adventure()

def enchanted_gardens():
    print("You enter the Enchanted Gardens, a place of surreal beauty and mystery.")
    choice = input("You see two paths: one leads to a singing tree, the other to a talking fountain. Do you go to the 'tree' or the 'fountain'? ").lower()

    if choice == "tree":
        solve_singing_tree_puzzle()
    elif choice == "fountain":
        solve_talking_fountain_puzzle()
    else:
        print("Confused by the enchanting sights and sounds, you decide to return to the main hall.")
        start_adventure()

def solve_singing_tree_puzzle():
    print("The tree sings a melody with a riddle embedded in its lyrics.")
    riddle_answer = input("What runs, but never walks; has a bed, but never sleeps; has a mouth, but never eats? ")
    if riddle_answer.lower() == "river":
        print("The tree reveals a hidden key in its trunk. You take the key.")
        royal_chambers()
    else:
        print("The tree stops singing, and you feel like you missed something important.")
        enchanted_gardens()

def solve_talking_fountain_puzzle():
    print("The fountain asks you to balance the water flow by adjusting several valves.")
    # Implement a puzzle where the player has to enter the correct sequence
    valve_sequence = input("Enter the sequence to balance the flow - four valves total (e.g., '5895'): ")
    if valve_sequence == "1234":  
        print("The water clears, revealing a shimmering gem at the bottom of the fountain.")
        ancient_library()
    else:
        print("The fountain's waters become murky, and you realize you've made a mistake.")
        enchanted_gardens()


def continue_story_after_riddle_solved():
    print("As you take the key from the tree, a secret passage opens behind you.")
    print("You follow the passage and find yourself in a hidden chamber.")
    ancient_library()
    
    
    
def royal_chambers():
    print("You find yourself in the Royal Chambers, filled with opulence and whispers of the past.")
    choice = input("Two items catch your eye: an ancient book and a mysterious painting. Do you examine the 'book' or the 'painting'? ").lower()

    if choice == "book":
        solve_ancient_book_puzzle()
    elif choice == "painting":
        solve_mysterious_painting_puzzle()
    else:
        print("Overwhelmed by the chamber's grandeur, you decide to leave.")
        start_adventure()

def solve_ancient_book_puzzle():
    print("The ancient book before you whispers secrets of Eldoria's past, recounting pivotal moments and the legends of old.")
    print("To unlock the wisdom hidden within, you must chronologically arrange the events that shaped the kingdom:")
    
    events = [
        "🌟 The Founding of Eldoria by the legendary King Everon.",
        "👑 The Rise of the Ancient Rulers and the era of prosperity.",
        "⚔️ The Epic Battle against the shadow forces, marking the kingdom's darkest hour.",
        "🌌 The Rebirth of Eldoria, a new dawn under the stars."
    ]
    
    for event in events:
        print(event)
    
    correct_order = "1234"
    event_symbols = "🌟👑⚔️🌌"
    
    event_order = input("\nArrange the events in chronological order by entering their corresponding symbols (e.g., '🌟👑⚔️🌌'): ")
    
    num_correct_pages = sum([1 for i in range(len(event_order)) if event_order[i] == correct_order[i]])
    
    if num_correct_pages == 4:  # All events are in the correct order
        print("\nAs you rearrange the events in their true order, the air around you shifts, and the bookshelf beside you creaks open, revealing a secret scroll.")
        # Player acquires the scroll
    else:
        print(f"\nYou have {num_correct_pages} out of 4 events in the correct order. The tapestry of Eldoria's history is intricate and detailed. Reflect upon the legends and their legacy.")
        if '🌟' not in event_order[0]:
            print("Remember, the foundation of Eldoria is where the tale begins.")
        if '🌌' not in event_order[-1]:
            print("The rebirth signifies a new era, a culmination of the trials and triumphs that came before.")
        royal_chambers()



def solve_mysterious_painting_puzzle():
    print("The painting is an intricate portrait with several elements that can be moved.")
    painting_alignment = input("Align the painting's elements (e.g., 'moon-sun-star'): ")
    correct_alignment = "sun-moon-star"

    if painting_alignment == correct_alignment:
        print("As you align the elements in the painting following the sequence 'sun-moon-star', a faint resonance echoes through the chamber, and a soft glow envelops the painting. Legends speak of an ancient order where the sun, symbolizing light and wisdom, always leads the way, followed by the moon, keeper of secrets and mysteries, and finally the star, representing guidance and destiny.")
        print("With the painting now unlocked, it swings open, unveiling the hidden alcove that has remained dormant for centuries.")
        tower_observatory()
    else:
        print("You attempt to rearrange the elements in the painting, but the chamber remains silent. Perhaps the spirits of the past seek a different alignment, or there's a deeper connection waiting to be revealed.")
        royal_chambers()


def tower_observatory():
    print("As you ascend the ancient, spiraling staircase, a chill of anticipation sends shivers down your spine. You emerge into the Tower Observatory, a sanctum of knowledge where the heavens themselves unfold.")
    print("The walls are lined with shelves of dusty tomes and celestial instruments, each telling its own story of the cosmos. In the center of the room, a large, domed ceiling opens to the starry sky above, dominated by a vast star map and an ancient, ornate telescope.")
    
    # Offer a choice that feels impactful by providing context
    print("Your quest for the Lost Relic of Eldoria has led you here, where secrets of the universe whisper to those who listen. Will you decode the mysteries of the stars, or will you peer into the depths of space to find your destiny?")
    choice = input("Do you choose to study the 'map' to unlock the celestial patterns, or use the 'telescope' to gaze into the cosmos? (map/telescope): ").lower()

    if choice == "map":
        print("\nDrawn to the intricate constellations, you approach the star map. It's a living tapestry of light and shadow, where ancient secrets await.")
        solve_star_map_puzzle()
    elif choice == "telescope":
        print("\nYou approach the ancient telescope, its lens aimed at the heavens. Through its gaze, the mysteries of the universe beckon.")
        approach_telescope_puzzle()
    else:
        print("\nUncertain of where to focus your attention, you decide that perhaps the answers you seek lie not in the stars but in the heart of the castle itself.")
        start_adventure()

def solve_star_map_puzzle():
    print("You step into the Tower Observatory, where ancient and enigmatic energies swirl amidst the echoes of time.")
    print("Before you, an ancient star map sprawls across the dome ceiling, each constellation shimmering with a light that seems to pulse with ancient wisdom.")
    print("Legend holds that an Astral Key, forged in the heart of a fallen star, was hidden by the ancients somewhere within this map, locked away until the stars align in perfect harmony.")

    # Introduce an element that suggests observation and interaction with the environment.
    print("A dusty tome on a nearby pedestal catches your eye. Its pages whisper tales of celestial architects who crafted the constellations to guard their most precious secrets.")
    print("The tome speaks of four constellations - Orion, the hunter; Draco, the dragon; Lyra, the lyre; and Cygnus, the swan - as the pillars of the celestial lock.")

    correct_alignment = "Orion-Draco-Lyra-Cygnus"
    
    print("To your right, a series of levers and dials beckon, seemingly connected to the star map above.")
    constellation_alignment = input("Align the constellations correctly (e.g., 'Orion-Draco-Lyra-Cygnus'): ")
    
    if constellation_alignment.lower() == correct_alignment.lower():
        print("As you adjust the final dial, the Observatory trembles. The constellations align, resonating with a harmonious frequency that bathes the room in a radiant light.")
        print("A hidden compartment in the wall slides open, revealing the Astral Key. It glows with a light that seems to contain the essence of the cosmos itself, vibrating with the power to unlock secrets long forgotten.")
        underground_vault()
    else:
        print("Despite your efforts, the constellations seem to resist alignment, as if mocking the limits of mortal understanding.")
        print("The tome's pages flutter as if caught in a sudden breeze, hinting at additional wisdom yet to be gleaned. Perhaps examining the constellations' lore more closely or seeking insights hidden in the Observatory will reveal the path to true alignment.")
        # Hint at the possibility of finding additional clues or lore within the game environment.
        tower_observatory()


def approach_telescope_puzzle():
    print("Recalling the scroll from the library and the murmured legends of the ancients, you realize the tower's secrets are aligned with the stars. The prominence of Vega in the lore you've uncovered cannot be a coincidence.")
    print("The ancient civilization revered Vega as a guide, a beacon illuminating the path to hidden knowledge. The murals, the diaries, and the celestial maps all point to one star as the key: Vega.")
    print("As you stand before the ancient telescope, the pieces of the puzzle begin to fall into place. Aligning the telescope with Vega seems not just a guess, but an informed decision, a culmination of all the clues you've gathered on your journey.")
    solve_telescope_puzzle()


def solve_telescope_puzzle():
    print("\nThe ancient telescope, crafted from an alloy unknown to modern science, stands before you, its lens glaringly misaligned under the starlit sky.")
    print("You recall the scroll from the library, the whispers of ancients, and the alignment of Vega in the night sky, as depicted in murals and celestial maps. It's clear; Vega is the key.")
    
    # Puzzle initiation
    telescope_alignment = input("Which celestial body will you align the telescope with? (e.g 'Polaris'): ").strip()
    
    # Correct alignment logic
    if telescope_alignment.lower() == "vega":
        print("\nAs you carefully adjust the ancient mechanism, the telescope aligns with Vega. A beam of starlight filters through the lens, focusing on the wall opposite to reveal a hidden message.")
        print("The message, written in the light of Vega itself, outlines the location of a lost temple, rumored to house the legendary Relic. Your path is clear, and your resolve stronger than ever.")
        underground_vault()
    else:
        print("The stars remain just distant lights. Perhaps a different alignment is needed.")
        tower_observatory()
        


def underground_vault():
    print("Descending into the dimly lit vault, you're greeted by the sight of gleaming treasures and shelves laden with ancient scrolls, their secrets untouched by time. The air is thick with dust and the weight of history.")
    choice = input("In the heart of the vault, upon a pedestal bathed in a lone shaft of light, rests the fabled Eldoria Scepter, said to wield untold power. Do you 'take' the scepter, drawn to its allure, or 'investigate' the scrolls, sensing the true treasure may lie within knowledge? ").lower()

    if choice == "take":
        print("The moment your fingers brush against the scepter, a deep rumble echoes through the chamber. The floor beneath you begins to shift, a clear sign of an ancient security measure triggered by your greed. You must act swiftly to avoid the unfolding trap and find a way out before you're sealed within forever.")
        escape_vault()
    elif choice == "investigate":
        print("Carefully unrolling the brittle scrolls, you discover they are not just any tomes but the chronicles of Eldoria, detailing the history and secrets of an ancient civilization. Among these texts, a revelation strikes you; the true power of Eldoria was never in its scepter but in the wisdom carried forward by its people. The scrolls hint at the Lost Relic being a mere symbol, with its real value lying in the knowledge it represents, leading you to the true location of this ancient wisdom.")
        final_showdown()
    else:
        print("Your hesitation costs you dearly. The faint echo of footsteps grows louder, a clear sign of the vault's guardians on their way. With precious little time, you need to decide quickly how to face the imminent threat of capture.")
        captured_by_guards()



def escape_vault():
    print("The walls close in, and ancient traps spring to life. Your only hope lies through a hidden passage.")
    decision = input("Do you 'search' for the passage or 'force' your way through the traps? ").lower()

    if decision == "search":
        print("Your keen eyes spot a lever disguised as a torch holder. Pulling it, a passage opens, and you escape just in time!")
        print("Breathing heavily, you find yourself in a mysterious chamber that might lead you to the Lost Relic.")
        mysterious_chamber()  
    elif decision == "force":
        print("Despite your bravery, the traps are too cunning. A dart dipped in ancient poison ends your journey.")
        print("As darkness claims you, you wonder what secrets the vault kept hidden.")
        play_again() 
    else:
        print("Indecision is as deadly as the traps. The walls close in, and your adventure ends here.")
        play_again()


def mysterious_chamber():
    print("You find yourself in a chamber untouched by time, its walls adorned with frescoes that tell the story of an ancient civilization.")
    print("In the center, a pedestal holds an orb that pulses with a soft light, illuminating two doors: one of gold, and one of stone.")
    
    choice = input("Do you approach the 'orb' to uncover its secrets, or choose a door: 'gold' or 'stone'? ").lower()

    if choice == "orb":
        print("As your hand touches the orb, visions of the past flood your mind. You see the Relic, powerful and coveted, hidden away in a place where earth meets sky.")
        print("The vision fades, and you now understand that the Relic is not within these walls, but further up, guarded by the elements.")
        ascend_to_peak() 
    elif choice == "gold":
        print("The golden door leads to a treasure trove, but the Relic is nowhere to be found. Though riches abound, you know your quest is not for gold.")
        print("A hidden passage in the treasure room offers a way onward, hinting that your journey is far from over.")
        secret_passage() 
    elif choice == "stone":
        print("The stone door opens to a library of ancient texts. Among them, a map that hints at the Relic's true location: a peak shrouded in clouds.")
        ascend_to_peak()  
    else:
        print("Hesitation grips you as the chamber begins to seal itself. You must choose quickly or be trapped forever.")
        mysterious_chamber()  # Allows the player another chance to make a decision

# Placeholder functions for narrative continuity
def ascend_to_peak():
    print("With the knowledge gained from the orb, you set out towards the towering peak that pierces the clouds above. The journey is treacherous, with paths winding through ancient forests and over crumbling bridges.")
    print("As you ascend, the air thins, and the environment becomes harsher, but ahead, silhouetted against the moonlight, is an ancient temple. It is said to be the final resting place of the Lost Relic.")
    print("The temple doors are open, as if inviting you in. Inside, the air is thick with history, and the shadows seem to whisper secrets of the past.")
    
    choice = input("Do you 'explore' the temple to find the Relic, or 'study' the temple's murals for clues about its location? ").lower()

    if choice == "explore":
        print("Your exploration leads you to the heart of the temple, where the Relic shines with an otherworldly light. It is more magnificent than you imagined, and its power is palpable.")
        celebrate_victory()  
    elif choice == "study":
        print("The murals tell the story of the Relic's creation and its significance. Armed with this knowledge, you uncover a hidden chamber where the Relic has been kept safe for millennia.")
        celebrate_victory()
    else:
        print("Lost in thought, you fail to notice the temple's traps awakening. The path to the Relic is perilous without clear intent.")
        captured_by_temple_traps()  


def secret_passage():
    print("The secret passage winds deeper into the earth, leading you to an underground network of caves. The air is cool and damp, and the sound of distant water echoes through the tunnels.")
    print("After what feels like hours, you emerge into a vast cavern illuminated by crystals that glow with an ethereal light. At its center stands an ancient altar, upon which lies a dusty tome.")
    
    choice = input("Do you 'read' the tome for wisdom or 'search' the cavern for other exits? ").lower()

    if choice == "read":
        print("The tome reveals the true power of the Lost Relic and its location atop the ancient peak. With newfound determination, you set out to climb the mountain.")
        ascend_to_peak()
    elif choice == "search":
        print("Your search uncovers a hidden pathway that ascends steeply. It appears to lead directly to the peak where the Relic is rumored to be hidden.")
        ascend_directly()  
    else:
        print("Hesitation in the cavern leads to a collapse, blocking the way back. You must move forward or risk being lost in the darkness forever.")
        trapped_in_cavern()  

def captured_by_temple_traps():
    print("The temple, ancient and cunning, is alive with hidden dangers. As you navigate its corridors, traps spring from every shadow.")
    print("Your agility and wit are tested to their limits as you dodge pitfalls, sidestep snares, and leap over flames. With each close call, the path forward becomes clearer, teaching you the temple's rhythm.")
    print("Finally, with one last daring leap, you escape the temple's grasp, its traps now silent behind you. Ahead lies the inner sanctum, and with it, the Relic.")
    final_showdown()


def ascend_directly():
    print("Choosing the direct path, you face the mountain's wrath. The ascent is steep, the winds fierce, and the path fraught with peril.")
    print("But your resolve is stronger than stone. You climb, each step a testament to your determination. The peak draws closer, and with it, the promise of the Relic.")
    print("At the summit, the world stretches out below, a breathtaking panorama of what your journey has overcome. Here, among the clouds, you find the Relic, guarded not by traps or puzzles, but by the sheer will required to reach it.")
    final_showdown()


def trapped_in_cavern():
    print("The cavern is a labyrinth of echoes and shadows, where every step could be a misstep. Your light flickers, casting long shadows that seem to move.")
    print("But you are not deterred. You map the caverns in your mind, noting each twist and turn. Slowly, a pattern emerges, and with it, a way forward.")
    print("Emerging from the cavern's mouth, you are greeted by the light of dawn. The Relic is close now, its presence almost palpable.")
    final_showdown()




def final_showdown():
    print("Armed with the knowledge from the scrolls, you track the Lost Relic to its true hiding place.")
    print("Standing before you is the Guardian of the Relic, a creature of myth and shadow.")
    challenge = input("Do you 'confront' the guardian or 'outwit' it with a riddle? ").lower()

    if challenge == "confront":
        print("Steel clashes with shadow. Your courage shines bright, overwhelming the guardian.")
        print("Victorious, you claim the Lost Relic, a symbol of hope and power.")
        celebrate_victory()  # Assuming a function to celebrate or conclude the adventure
    elif challenge == "outwit":
        print("With wisdom, you pose a riddle that has puzzled many. The guardian, bound by ancient rules, yields passage.")
        print("The Lost Relic lies before you, its light a beacon in the gloom.")
        celebrate_victory()
    else:
        print("Hesitation allows the guardian to strike. You are overwhelmed, and the relic remains lost.")
        play_again()


def captured_by_guards():
    print("Surrounded by the king's elite guard, escape is impossible. You're taken to the dungeons.")
    play_again = input("Locked away, your adventure is halted prematurely. Would you like to try again? (yes/no) ").lower()

    if play_again == "yes":
        start_adventure()  # Assuming this resets or starts a new game
    else:
        print("Thank you for playing! Though this journey ends in chains, remember that every end is a new beginning.")


def celebrate_victory():
    print("As you hold the Lost Relic, its light pulsating with ancient power, you feel a sense of accomplishment wash over you.")
    print("Your journey has been long and fraught with danger, but in the end, you've emerged victorious.")
    print("The lands will sing of your deeds for generations, and the relic will protect the realm from darkness.")
    print("As you exit the chamber, you know that your name will be etched in the annals of history.")
    print("Congratulations, brave adventurer. You have completed your quest.")
    play_again()


def play_again():
    choice = input("Would you like to embark on another adventure? (yes/no) ").lower()

    if choice == "yes":
        print("Brave soul! Your thirst for adventure is unquenchable. Let us begin anew.")
        start_adventure()  
    else:
        print("Rest well, hero. When you're ready to wield sword and wit again, the realm will await your return.")
        print("Thank you for playing!")


start_adventure()
