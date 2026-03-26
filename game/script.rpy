# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define gui.name_text_outlines = [(3, "#000000", 2, 2)]
define guy = Character("Dr. Dick", outlines = [(3, "#000000", 2, 2)])
define yol = Character("Yolanda von Dhark", color = '#eb0000', outlines = [(3, "#000000", 2, 2)])
define a = Character("some other npc", color = '#00e200', outlines = [(3, "#000000", 2, 2)])

# The game starts here.

label start:

    scene bg office

    "I woke up to the sight of my ceiling."
    "A terrible hangover."
    "I could just barely make out the events of last night's drinking"
    "then, a flash of memory. an open case."
    "a well-dressed dame had come through the door of my office bawling her eyes out."
    "somehting about a dead husband, or the grave of the husband, or something."
    "grave robbers."
    "somebody had dug up the coffin, took the stiff, and a few other valuables that were supposed to be with him"
    "rotten stuff."
    "I looked at the clock. I was about to be late, so i got up, and put my pants on."

    scene bg town

    "the sun was about to set already." 
    "by the gods, how long had i been up drinking?"

    scene bg gravesite

    yol "took you long enough."

    show yolanda

    guy "i dont come out this way often."
    guy "i forget how tricky the roads get."

    yol "mhhmm...."

    menu:

        "say something stupid":
            "duhhhh duhhhhhdoyyyy"
            "uhhhhhhh fuuuuuu"

        "say something intelligent":
            "statistics show that most grave robbings are done by those who were closest to the corpse"
            "we should ask those weirdos standing nearby"

    yol "what a great idea."

    scene bg lineup

    "Suspect_1" "ahh crap I'm suspect 1"
    "Suspect_2" "ahhh fuc im suspect 2"
    "Suspect_3" "what the crap idk anything about this"

    menu:
        "which lead do you want to pursue?"

        "SUSPECT1":
            jump vamp_route

        "SUSPECT2":
            jump thief_route

        "SUSPECT3":
            jump necro_route

label vamp_route:
    "Lets go to the bar in town"

label thief_route:
    "lets run an errand for the moldy mike"

label necro_route:
    "lets help this crazy guy"


label finale:



    # This ends the game.
    return
