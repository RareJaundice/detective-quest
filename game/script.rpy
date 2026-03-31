# The script of the game goes in this file.

define gui.name_text_outlines = [(3, "#000000", 2, 2)]
define guy = Character("You", outlines = [(3, "#000000", 2, 2)])
define dame = Character("Widow", color = '#eb0000', outlines = [(3, "#000000", 2, 2)])
define bart = Character("Bart Enderson", color = '#00e200', outlines = [(3, "#000000", 2, 2)])

default stat_burl  = 8
default stat_wits  = 8
default stat_charm = 8
default stat_dex   = 8
default roll = 0

init python:
    def d20roll(mod):
        roll = renpy.random.randint(1, 20) + mod
        return roll

# The game starts here.

label start:
    
    play music "Hard-Boiled.mp3" fadein 3.0

    scene bg black

    pause

    "Eyelids stitched closed were the best at keeping the darkness out..."
    "But a man cannot hide from his own shadow forever."

    scene bg bar with Dissolve(1)

    "There I was. Drowning the day away."
    "I'd woken up at first light this morning, antsy at putting the case behind me. 
        I'd been laboring over the details in my head even as I slept."
    "Having put the pieces together around noon (the poor lad had been hanged in a practical joke 
        gone wrong), the evidence was in the constabulary's hands by three o'clock."
    "Didn't matter whose hands it was in..."

    scene bg crimescene with Dissolve(1)

    "Per usual, it would take a considerable washing to get it out from between the wrinkles of my mind."
    "And, just as it is with paint and primer; alcohol was the best solution..."
    "... One last bit of elbow grease."

    scene bg bar with Dissolve(1)
    show bar zorder 1:
        ypos 1

    guy "One last round, then I gotta pack it up for the night."
    guy "{i}Hey, Bart!{w} Over here!{/i}"

    show bart zorder 0:
        xpos 0.20 yalign 2
        linear 0.6 yalign 1

    "Bartender" "Alright alright, I hear ya!"
    "Bartender" "{i}What's your poison this time, Dick?{/i}"

    menu:
        
        "Whiskey (+ BURLINESS)":

            "Bartender" "Coming right up."

            show whiskey zorder 2:
                xpos -0.5
                linear 0.9 xpos 0.5

            "Bartender" "Orcish Fieldsman, 1255."
            "Bartender" "If you didn't have hair on your chest by now, a shot of this will do it."

            hide whiskey with Dissolve(1)

            $ stat_burl += 1

            guy "Braxis' beard! That's the real deal, ain't it."

            "Bartender" "Told you."
            "Bartender" "You could've asked for a chaser, you know.{w} Or a sapsparilla half 'n half..."
            "Bartender" "But you hard-boiled types always order it straight, and it really puzzles me."
            
        "Beer (+ RESOLVE)":

            "Bartender" "On it, boss."

            show beer zorder 2:
                xpos -0.5
                linear 0.9 xpos 0.5

            "Bartender" "Authentic Dwarven Drakenslager, fresh off the tap."

            guy "Wasting the good stuff on me, Bart? I'm flattered."

            hide beer with Dissolve(1)

            $ stat_dex += 1

            "Bartender" "Don't mention it."
            "Bartender" "Seriously.{w} Do you know how hard this is to get,
                the way trade relations are these days?"
            "Bartender" "Do not.{w} Mention this."

        "Pina Colada (+ APPEAL)":

            "Bartender" "Gettin' fruity with it, eh?"

            show pinacolada zorder 2:
                xpos -0.5
                linear 0.9 xpos 0.5

            guy "Where's my tiny umbrella?"

            "Bartender" "We're out of the umbrellas."

            guy "Can I at least get a toothpick sword?"

            "Bartender" "Sure, boss."

            show pinacolada sword

            guy "Now I can enjoy this beverage as Abraxas intended."

            hide pinacolada with Dissolve(1)

            $ stat_charm += 1

            "Bartender" "Not gonna lie. That looked delicious. And I envy you."
            "Bartender" "Just don't forget about your tab, alright."

    guy "Anybody ever told you ya look like Arnold Arkengthanz?"
    guy "I think it's the jawline, Bart."

    "Bartender" "Only celebrity I look like is Bartholemew B. Enderson, chum."
    bart "Because that's my name."
    bart "And don't you forget it."
    
    show bart:
        linear 1.0 xpos -0.5

    "(bridge prose)"

    "Excuse me."
    "Sir, could I speak to you a moment?"
    "I was so blasted, I figured I'd started hearing voices again."
    "Then she stepped into frame."

    show widow zorder 3:
        xalign 1.5
        linear 0.6 xalign 0.9

    dame "I'm looking for a detective. Are you him?"
    
    guy "Yep I detect stuff for a living what's it to ya?"

    dame "I need you to look into something for me."

    "She spoke as if I were already hired...{p} 
        As if I were a secretary pushing pencils and paperclips for a living."

    dame "As you might already know, my husband recently passed..."


label statchallenge_test:

    "Alright where was I..."
    "OH MY GOODNESS A STAT CHALLENGE!!!"

    $ roll = d20roll(stat_dex)

    "{i}You rolled [roll]!{/i}"

    if roll > 20 :
        pass
    else:
        jump challenge_fail

    "Oh thank goodness. I succeeded."
    "Now the game can continue."

    return

label challenge_fail:

    "YOU FUCKING FAILED AND SO YOU DIE AND SUCK HAHA"

    $ roll = d20roll(stat_dex)
    "{i}You rolled [roll]!{/i}"
    return


label finale:



    # This ends the game.
    return