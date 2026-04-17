# The script of the game goes in this file.

define gui.name_text_outlines = [(3, "#000000", 2, 2)]
define guy = Character("Gnash", outlines = [(3, "#000000", 2, 2)])
define dame = Character("Widow", color = '#eb0000', outlines = [(3, "#000000", 2, 2)])
define bart = Character("Bart Enderson", color = '#00e200', outlines = [(3, "#000000", 2, 2)])

default stat_burl  = 8
default stat_wits  = 8
default stat_charm = 8
default stat_dex   = 8
default stat_alc   = 5
default roll = 0

init python:
    def d20roll(mod):
        roll = renpy.random.randint(1, 20) + mod
        return roll

# The game starts here.

label start:
    
    menu:
        "Scene Select"

        "Apartment Start":
            jump apartment_start

        "Bar Start":
            jump bar_start

label apartment_start:

    play music "Hard-Boiled.mp3" fadein 2.0

    "???" "This city really is settin' voyage up to Hell, ain't it?"
    "???" "Cess pit. All the drink in the world can't hold it down."
    "???" "You either chuck up the filth and hang out to dry or set sail right down the tubes."
    "???" "Right down the fucking tubes."
    "???" "Fools out there dancin' away, kicking up cobble and muck..."
    "???" "Main Street looks more like a dugout trench these days than anything else."
    "???" "One'a these days, just you watch."
    "???" "The Big Guy himself is gonna come back. And pull the plug on the whole thing."
    "???" "I mean, have you seen the Flooded Quarter?"
    "???" "Sank another half-fathom. {i}Overnight{/i}."
    "???" "You hear about that? Of course."
    "???" "You only leave this room when you get the itch to knock your own head off with goblin shine and reatach it firmly up your own ass."
    "???" "Are you hearing anything I'm saying, {i}Gnash{/i}?"
    "???" "You better find your head, or by Abraxas I'm gonna find it for you."

    "..."

    "Your eyes blink open slowly and you see the shape of a rodentian man, illuminated by candlelight in the dim studio apartment."
    "You recognize the figure to be Provolone Gardetto, host and owner of the Waning Sun Pub."
    
    "Provolone" "Drunken. {w}Fuckin. {w}Oaf."

    "He seems upset. And more importantly, at you. But you haven't the slightest clue what you did."
    "You and Prove go way back. Too far back for comfort really."
    "Best just to ride this one out, and not get too testy with him."

    "Provolone" "Look, I got paying customers to keep up with, and second-breakfast don't cook itself."
    "Provolone" "There's a lady waiting for you out front, so get your marbles rolling, alright."
    "Provolone" "You look like shit. And you smell even worse."
    "Provolone" "I do mean a {i}proper{/i} lady this time. Kept calling me your 'vittler'."
    "Provolone" "Imagine that! Me, operating a 3-bit hostel with some actual class."
    "Provolone" "Hah! When my tenants actually pay their dues, maybe."

    "You remember now. You haven't paid rent in at least three sets."
    "You suppose that just riding this one out may no longer be in the cards."
    "You're not just riding a wave of utter humiliation, either. You're... scared?"
    "The hangover has created a disconnect between the emotion and the cause. But... Prove?"
    "Couldn't be him. That judgemental stare is the only weapon he's ever brandished."
    "You attempt to sit up in your bed, blinking away the haze like a stoned toad."

    guy "Argh!"

    "Stinging, writhing pain." 
    "You're used to this brand. The lower back, kidneys. The abdomen, the liver."
    "But it's never been so... comprehensive."
    "This pain is not your friend, here to inform you that you have indeed been poisoning yourself."
    "This pain is sinister."
    "You begin to crumple."

    "Provolone" "Hey, woah!"
    
    "As your body jolts, and your hand instinctively applies pressure to the bandage along your torso, Provolone closes the distance between you."
    "He grabs your shoulder with one hand, and lays the other flat between your shoulder blades to stabilize you."
    "No hesitation. It is a practiced reflex."

    "Provolone" "Shit... I guess I lost myself for a minute."
    "Provolone" "You owe me more than just rent, Gnash."
    "Provolone" "The story is that you took a blade to the guts last night."
    "Provolone" "Some drunk challenged you to a brawl on account of you being a dirt-eating cut-purse."
    "Provolone" "You were out drinking in the Dead Leas. Serious fellas that way."
    "Provolone" "Roquefort found you beat half-blue, buried under a Prester and a Lay-Knight."
    "Provolone" "Luck ain't a thing you've ever been known for but this... is a record low."
    
    "Hand planted firmly over the wound, you find just enough resolve to remain upright, and swing your legs out of bed."
    "Provolone adopts his rare but ever-dangerous thinking look. You're intimate with this look and its repercussions."
    "He is about to have either the best idea he has ever had, or realize that he has left the oven on overnight."

    "Provolone" "Hey... Roque and I didn't bother checking your pockets when we got you back here."
    "Provolone" "So, if you did happen to have in your possession a ring of significant value that surely won't be missed by its rightful owner..."
    "Provolone" "You could maybe take it over to Haggle's for appraisal."
    "Provolone" "And maybe pawn it off for enough coin to maybe pay me that rent you owe."
    "Provolone" "The rent that I am so graciously not charging you late fees or interest on."
    "Provolone" "I mean, seriously. If my old man were still alive and kicking..."
    "Provolone" "He'd have my ass on a platter for letting you stay one second overdue."
    "Provolone" "..."
    "Provolone" "Hello? Come on man, say somethin."
    
    menu:

        "I take a knife to the guts and you couldn't spare some sherry and biscuits? (+ BOLDNESS, + ALCOHOLISM)":
            "Provolone" "Funny guy, huh? I left you a ration on the bar by the sink."
            "Provolone" "You want to be funny with me, I'll let Roque know to finish the job next time he finds you half bled-out."
            "Provolone" "See how the sherry sits in your stomach when you've been run all the way through, huh?"

label bar_start:

    play music "Hard-Boiled.mp3" fadein 2.0

    scene bg black

    pause 0.5

    "Eyelids stitched closed were the best at keeping the darkness out..."
    "But a man cannot hide from his own shadow forever."

    scene bg bar with Dissolve(1)
    show bar foreground zorder 1 with Dissolve(1)

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
    show bar foreground zorder 1

    guy "One last round, then I gotta pack it up for the night."
    guy "{i}Hey, Bart!{w} Over here!{/i}"

    show bart zorder 0:
        xysize(500, 880) xpos -0.5
        easein 0.5 xpos 0.20 ypos 0.12

    "Bartender" "Alright alright, I hear ya!"
    "Bartender" "{i}What's your poison this time, Dick?{/i}"

    menu:
        
        "Whiskey (+ BURLINESS)":

            "Bartender" "Coming right up."

            show whiskey zorder 2:
                xpos -0.5 ypos 1.0
                easein 0.8 xpos 0.4 ypos 0.61

            "Bartender" "Orcish Fieldsman, 1255."
            "Bartender" "If you didn't have hair on your chest by now...{p}a shot of this will do it."

            hide whiskey with Dissolve(1)

            $ stat_burl += 1

            guy "Braxis' beard! That's the real deal, ain't it."

            "Bartender" "Told you."
            "Bartender" "You could've asked for a chaser, you know.{p}Or a sasparilla half 'n half..."
            "Bartender" "But you hard-boiled types always order it straight, and it really puzzles me."
            
        "Beer (+ RESOLVE)":

            "Bartender" "On it, boss."

            show beer zorder 2:
                xpos -0.6 ypos 1.0
                easein 0.9 xpos 0.4 ypos 0.56

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
                xpos -0.5 ypos 1.0
                easein 0.8 xpos 0.4 ypos 0.53

            guy "Where's my tiny umbrella?"

            "Bartender" "We're out of the umbrellas."

            guy "Can I at least get a toothpick sword?"

            "Bartender" "Sure, boss."

            show pinacolada sword with Dissolve(0.5)

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
        easeout 1 xpos -0.5 ypos 0.2

    "(bridge prose)"

##   "Excuse me."
##   "Sir, could I speak to you a moment?"
##   "I was so blasted, I figured I'd started hearing voices again."
##   "Then she stepped into frame." 

    guy "Alright... {w}That's enough medicine for tonight."
    guy "Bed time."

    # barstool sound effect here

    "My legs wobbled as I got up. One drink too many."

    # bg bar entrance

    "I stumbled through the mass of San Marais' finer specimens."
    "The salloon doors screamed on their brass hinges as I fell through them."

    # bg black
    # splat sound effect

    "Found myself face down in the mud..."
    "My luck, I was rinsed enough to mistake it for my bed."
    "And I had the craziest dream..."

    # bg apartment

    "I was back at my office, well, my apartment flat. {p}Nothing seemed out of the ordinary."

    # show door open

    "Then, drifting through my door, which was always locked, came the most astonishing thing."

    # show door mist

    "Some kind of mist. A ghost... or maybe something more primal... more..."

    # show angel

    "Primordial. {w}That's the word."

    fa "Sir?"
    fa "Excuse me..."
    fa "Mister, you need to get up."

    "My head dislodged from the mud like a joint popping loose."
    "Then she came into frame."

    show widow zorder 3:
        xpos 1.3 ypos 0.12
        easein 1.2 xpos 0.48

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