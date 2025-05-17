label FinalStart:
scene trumpfwall05 with dissolve
mc "Now, all I need to do is find the Supreme White House in this big city."
if withbe == False and withpe == False and withwi == False and withkr == False:
    mc "I suppose I could ask someone. Excuse, young totally black lady, where is the Supreme White House please?"
    "Behind that wall over there."
    mc "Well, this was surprisingly easy. Let's go."
    jump WhiteHouse
if withbe == False and withpe == False and withwi == False and withkr:
    $ kristaentered = True
    window hide
    show derek01 at right
    show krista01 at left
    with dissolve
    dr "I know where it is. It's just behind that wall over there."
    mc "Oh, cheers Derek."
    hide derek01
    show derek03 at right
    with fastdissolve
    play sound "v08/gulp.mp3"    
    kr "I don't think President Trumpf wants to see you hun."
    mc "I don't need no invitation."
    hide derek03
    show derek04 at right
    with fastdissolve
    dr "Are you going there for a tourist visit?"
    mc "Err, yeah, that's right. Nothing seditious or anything."
    hide krista01
    show krista02 at left
    with fastdissolve
    kr "Well, we gotta go hun, we need to find ourselves a new container for the kids."
    hide derek04
    show derek01 at right
    with fastdissolve
    mc "Okay, good luck with your future... pregnancies. I' better hurry, the weather seems to be turning."
    $ withkr = False
    jump WhiteHouse
if withkr:
    $ kristaentered = True
    window hide
    show derek01 at right
    show krista01 at left
    with dissolve
    dr "I know where it is. It's just behind that wall over there."
    mc "Oh, cheers Derek."
    hide derek01
    show derek03 at right
    with fastdissolve
    play sound "v08/gulp.mp3"    
    kr "I don't think President Trumpf wants to see you hun."
    mc "I don't need no invitation."
    hide derek03
    show derek04 at right
    with fastdissolve
    dr "Are you going there for a tourist visit?"
    mc "Err, yeah, that's right. Nothing seditious or anything."
    hide krista01
    show krista02 at left
    with fastdissolve
    kr "Well, we gotta go hun, we need to find ourselves a new container for the kids."
    hide derek04
    show derek01 at right
    with fastdissolve
    mc "Okay, good luck with your future... pregnancies. I' better hurry, the weather seems to be turning."
    $ withkr = False
    jump WhiteHouse
if withpe:
    pe "Why don't you just ask someone?"
if withbe:
    be "Why don't you just ask someone?"
if withwi:
    wi "Why don't you just ask someone?"
if withpe or withbe or withwi:
    mc "I suppose so... Excuse me, young totally black lady, where is the Supreme White House please?"
    "Behind that wall over there."
    mc "Well, this was surprisingly easy. Let's go."
    jump WhiteHouse

label WhiteHouse:
play sound "v10/rain.mp3"
scene whitehouse01 with fade
mc "Ah finally, it's the Supreme White House! Looks similar to the previously-destroyed White House but more \"supreme\"."
if withbe:
    be "It's heavily guarded. How are we, I mean YOU, going to get inside?"
if withpe:
    pe "It's heavily guarded. How are we, I mean YOU, going to get inside?"
if withwi:
    wi "It's heavily guarded. How are we, I mean YOU, going to get inside?"
if withkr and withmo:
    mo "It's heavily guarded sweetie pie. How are you going to get inside? Mommy needs to go back to the compound and start the oven."
if withkr and withla:
    la "It's heavily guarded. How are we, I mean YOU, going to get inside? My plants NEED me and I'm heading back now that you've reached your final destination..."
if withpe or withbe or withwi:
    mc "I guess we'll have to SHOOT OUR WAY into the White House! Let's hide behind this police car wreck."    
else:
    mc "I guess I'll have to SHOOT MY WAY into the White House then! Let's hide behind this police car wreck."    
play sound "v10/gunfire.mp3"
if not (withbe or withpe or withwi):
    $ laststanding = True
if laststanding:
    scene whitehouse02
    with dissolve
    mc "They saw me! And now they're SHOOTING AT ME!"
if withbe:
    scene whitehouse02
    show whitehouse02bella01
    with dissolve
    be "They saw us! And now they're SHOOTING AT US!"
if withpe:
    scene whitehouse02
    show whitehouse02penny01
    with dissolve
    pe "They saw us! And now they're SHOOTING AT US!"
if withwi:
    scene whitehouse02
    show whitehouse02widow01
    with dissolve
    wi "They saw us! And now they're SHOOTING AT US!"
mc "Well, let's shoot back then, it's the only way! Injuring them so they have to retire to their medbay. On 3...2...1..."
$ whpenny_health = 2.0
$ whbella_health = 2.0
$ whwidow_health = 2.0
$ whmc_health = 2.0
$ whguard01_health = 2.0
$ whguard02_health = 2.0
show screen screenfightwhbase
if withbe:
    show screen screenfightwhbella
if withpe:
    show screen screenfightwhpenny
if withwi:
    show screen screenfightwhwidow

label WhiteHouseRound:
scene whitehouse02
if whguard01_health <= 0.09:
    show whguard01down
if whguard02_health <= 0.09:
    show whguard02down
if withbe and whbella_health >= 0.1:
    show whitehouse02bella01
if withpe and whpenny_health >= 0.1:
    show whitehouse02penny01
if withwi and whwidow_health >= 0.1:
    show whitehouse02widow01
if laststanding:
    pass
with dissolve

mc "...SHOOT!"
if withbe and whbella_health >= 0.1:
    show whitehouse02mcshoot
    show whitehouse02bellashoot
if withpe and whpenny_health >= 0.1:
    show whitehouse02mcshoot
    show whitehouse02pennyshoot
if withwi and whwidow_health >= 0.1:
    show whitehouse02mcshoot
    show whitehouse02widowshoot
if laststanding:
    show whitehouse02mcshoot
play sound "Sounds/gun.mp3"
window hide
$ renpy.pause(0.5, hard='True')
call DiceRoll
if sniper:
    $ dshootwhroll=mcfirearms+diceroll+1
if sniper == False:
    $ dshootwhroll=mcfirearms+diceroll
if (dshootwhroll >= 14 and not diceroll == 1) or diceroll == 6:
    if whguard02_health <= 0.09:
        $ whguard01out = True
        $ counting = 0        
        while counting < 20:
            $ whguard01_health -= 0.05
            $ counting += 1
            pause 0.01
        if whguard01_health >= 0.1:
            show whguard01injured
            mc "Got her! She's out for this round too! Let's take cover and reload."
            jump WhiteHouseRound
        if whguard01_health <= 0.09:
            show whguard01down
            mc "I got her! She's out for good!"
            if laststanding:
                mc "Now is the time to make a run for it!"
            if withbe and whbella_health >= 0.1:
                be "Then you're good to go! Run inside, while I keep any other guard that might come at bay!"
            if withpe and whpenny_health >= 0.1:
                pe "Then you're good to go! Run inside, while I keep any other guard that might come at bay!"
            if withwi and whwidow_health >= 0.1:
                wi "Then you're good to go! Run inside, while the Black Widow keeps any other guard that might come at bay!"
            play sound "Sounds/gun.mp3"
            hide whitehousemcshoot
            show whitehousemcrun
            with dissolve
            mc "YEE-HAW!"
            jump WhiteHouseDoor

    if whguard02_health >= 0.1:
        $ whguard02out = True
        $ counting = 0
        while counting < 20:
            $ whguard02_health -= 0.05
            $ counting += 1
            pause 0.01
        if whguard02_health >= 0.1:
            show whguard02injured
            with dissolve
            mc "Got her! She's out for this round too!"
        if whguard02_health <= 0.09:
            show whguard02down
            with dissolve
            mc "I got mine! She's out for good!"
            if whguard01_health <= 0.09:
                if withbe and whbella_health >= 0.1:
                    be "Then you're good to go! Run inside, while I keep any other guard that might come at bay!"
                if withpe and whpenny_health >= 0.1:
                    pe "Then you're good to go! Run inside, while I keep any other guard that might come at bay!"
                if withwi and whwidow_health >= 0.1:
                    wi "Then you're good to go! Run inside, while the Black Widow keeps any other guard that might come at bay!"
                if laststanding:
                    mc "Now is the time to make a run for it!"
                play sound "Sounds/gun.mp3"
                hide whitehousemcshoot
                show whitehousemcrun
                with dissolve
                mc "YEE-HAW!"
                jump WhiteHouseDoor
if (dshootwhroll <= 13 and not diceroll == 6) or diceroll == 1:
    if whguard02_health <= 0.09:
        mc "Shit, I missed..."
    if whguard02_health >= 0.1:
        mc "Shit, I missed... And now she's going to shoot back at me I'm guessing..."

if withpe and whpenny_health <= 0.09:
    jump ShootBack
if withpe and whguard01_health <= 0.09 and whpenny_health >= 0.1:
    play sound "Sounds/gun.mp3"
    pe "My turn to shoot at her!"
    call DiceRoll
    if diceroll >= 3:
        $ whguard02out = True
        $ counting = 0
        while counting < 20:
            $ whguard02_health -= 0.05
            $ counting += 1
            pause 0.01
        if whguard02_health >= 0.1:
            show whguard02injured
            with dissolve
            pe "Got her! She's out for this round too so she won't shoot back at you!"
        if whguard02_health <= 0.09:
            show whguard02down
            with dissolve
            pe "Road Warriors are the best shooters, and now she's out for GOOD!"
            pe "So you're good to go! Run inside, while I keep any other guard that might come at bay!"
            play sound "Sounds/gun.mp3"
            hide whitehousemcshoot
            show whitehousemcrun
            with dissolve
            mc "YEE-HAW!"
            jump WhiteHouseDoor
    else:
        pe "I missed... Rain is the enemy of the Road Warrior..."
if withpe and whguard01_health >= 0.1 and whpenny_health >= 0.1:
    play sound "Sounds/gun.mp3"
    pe "My turn to shoot at MY assigned GUARD on the balcony!"
    call DiceRoll
    if diceroll >= 3:
        $ whguard01out = True
        $ counting = 0
        while counting < 20:
            $ whguard01_health -= 0.05
            $ counting += 1
            pause 0.01
        if whguard01_health >= 0.1:
            show whguard01injured
            with dissolve
            pe "Got her! She's out for this round too!"
        if whguard01_health <= 0.09:
            show whguard01down
            with dissolve
            pe "Road Warriors are the best shooters, and now she's out for GOOD!"
            if whguard02_health <= 0.09:
                pe "So you're good to go! Run inside, while I keep any other guard that might come at bay!"
                play sound "Sounds/gun.mp3"
                hide whitehousemcshoot
                show whitehousemcrun
                with dissolve
                mc "YEE-HAW!"
                jump WhiteHouseDoor
    else:
        pe "I missed... Rain is the enemy of the Road Warrior..."

if withbe and whbella_health <= 0.09:
    jump ShootBack
if withbe and whguard01_health <= 0.09 and whbella_health >= 0.1:
    play sound "Sounds/gun.mp3"
    be "My turn to shoot at her!"
    call DiceRoll
    if diceroll >= 4:
        $ whguard02out = True
        $ counting = 0
        while counting < 20:
            $ whguard02_health -= 0.05
            $ counting += 1
            pause 0.01
        if whguard02_health >= 0.1:
            show whguard02injured
            with dissolve
            be "Got her! She's out for this round too so she won't shoot back at you!"
        if whguard02_health <= 0.09:
            show whguard02down
            with dissolve
            be "The Phallus Lord guided my bullet and now she's out for GOOD!"
            be "So you're good to go! Run inside, while I keep any other guard that might come at bay!"
            play sound "Sounds/gun.mp3"
            hide whitehousemcshoot
            show whitehousemcrun
            with dissolve
            mc "YEE-HAW!"
            jump WhiteHouseDoor
    else:
        be "I missed... Why did you abandon me, O Phallus Lord?"
if withbe and whguard01_health >= 0.1  and whbella_health >= 0.1:
    play sound "Sounds/gun.mp3"
    be "My turn to shoot at MY assigned GUARD on the balcony!"
    call DiceRoll
    if diceroll >= 4:
        $ whguard01out = True
        $ counting = 0
        while counting < 20:
            $ whguard01_health -= 0.05
            $ counting += 1
            pause 0.01
        if whguard01_health >= 0.1:
            show whguard01injured
            with dissolve
            be "Got her! She's out for this round too!"
        if whguard01_health <= 0.09:
            show whguard01down
            with dissolve
            be "The Phallus Lord guided my bullet and now she's out for GOOD!"
            if whguard02_health <= 0.09:
                be "So you're good to go! Run inside, while I keep any other guard that might come at bay!"
                play sound "Sounds/gun.mp3"
                hide whitehousemcshoot
                show whitehousemcrun
                with dissolve
                mc "YEE-HAW!"
                jump WhiteHouseDoor
    else:
        be "I missed... Why did you abandon me, O Phallus Lord?"
        
if withwi and whwidow_health <= 0.09:
    jump ShootBack
if withwi and whguard01_health <= 0.09 and whwidow_health >= 0.1 and whguard02_health >= 0.1:
    play sound "Sounds/gun.mp3"
    wi "My turn to shoot at her!"
    call DiceRoll
    if diceroll >= 5:
        $ whguard02out = True
        $ counting = 0
        while counting < 20:
            $ whguard02_health -= 0.05
            $ counting += 1
            pause 0.01
        if whguard02_health >= 0.1:
            show whguard02injured
            with dissolve
            if widowjoke01:
                wi "Got her! She's out for this round too so she won't shoot back at you!"
            if widowjoke01 == False:
                $ widowjoke01 = True
                wi "Got her! This shootout turns out to be safer than a shooting with Alec Baldwin. She's out for this round too so she won't shoot back at you!"
        if whguard02_health <= 0.09:
            show whguard02down
            with dissolve
            wi "Once again, the Black Widow to the rescue! You're good to go! Run inside, while I keep any other guard that might come at bay!"
            play sound "Sounds/gun.mp3"
            hide whitehousemcshoot
            show whitehousemcrun
            with dissolve
            mc "YEE-HAW!"
            jump WhiteHouseDoor
    else:
        wi "I missed... At least I didn't shoot some passing assistant director by mistake."
if withwi and whguard01_health >= 0.1 and whwidow_health >= 0.1:
    play sound "Sounds/gun.mp3"
    wi "My turn to shoot at MY assigned GUARD on the balcony!"
    call DiceRoll
    if diceroll >= 5:
        $ whguard01out = True
        $ counting = 0
        while counting < 20:
            $ whguard01_health -= 0.05
            $ counting += 1
            pause 0.01
        if whguard01_health >= 0.1:
            show whguard01injured
            with dissolve
            if widowjoke01:
                wi "Got her! She's out for this round too!"
            if widowjoke01 == False:
                $ widowjoke01 = True
                wi "Got her! This shootout turns out to be safer than a shooting with Alec Baldwin.... She's out for this round too!"
        if whguard01_health <= 0.09:
            show whguard01down
            with dissolve
            wi "Once again, the Black Widow to the rescue! Mine is now OUT FOR GOOD!"
            if whguard02_health <= 0.09:
                wi "So you're good to go! Run inside, while I keep any other guard that might come at bay!"
                play sound "Sounds/gun.mp3"
                hide whitehousemcshoot
                show whitehousemcrun
                with dissolve
                mc "YEE-HAW!"
                jump WhiteHouseDoor
    else:
        if widowjoke02:
            wi "Damn, I missed..."
        if widowjoke02 == False:
            $ widowjoke02 = True
            wi "I missed... At least I didn't shoot some passing assistant director by mistake."

label ShootBack:
if (whguard02out == False and whguard02_health >= 0.1) or (laststanding and whguard01out == False and whguard01_health >= 0.1):
    play sound "v10/gunfire.mp3"
    mc "I'm being shot at!"
    call DiceRoll
    if diceroll >= 4:
        $ counting = 0
        while counting < 20:
            $ whmc_health -= 0.05
            $ counting += 1
            pause 0.01
        if whmc_health >= 0.1:
            mc "Damn, I was hit! Just a scrap though, I will soldier on..."
            scene whitehouse02
            if laststanding:
                jump WhiteHouseRound        
            if withbe and whbella_health >= 0.1:
                scene whitehouse02
                show whitehouse02bellashoot
                if whguard01_health <= 0.09:
                    show whguard01down
                with dissolve
            if withpe and whbella_health >= 0.1:
                scene whitehouse02
                show whitehouse02pennyshoot
                if whguard01_health <= 0.09:
                    show whguard01down
                with dissolve
            if withwi and whbella_health >= 0.1:
                scene whitehouse02
                show whitehouse02widowshoot
                if whguard01_health <= 0.09:
                    show whguard01down
                with dissolve            
                    
        if whmc_health <= 0.09:
            scene whitehousemcinjured01 with dissolve
            mc "I've been shot real bad... I don't think I can continue..."
            if repairkit:
                $ repairkit = False
                if laststanding:
                    mc "Unless..."
                    scene whitehousemcinjured03 with fastdissolve
                    mc "I use this repair kit which doubles as a first aid kit! I KNEW this thing would come in handy one day..."
                    $ counting = 0
                    while counting < 20:
                        $ whmc_health += 0.1
                        $ counting += 1
                        pause 0.01
                    mc "Yeah, back on my feet in no time!"
                    jump WhiteHouseRound
                if withpe and whpenny_health >= 0.1:
                    pe "Don't you have a repair kit?"
                    scene whitehousemcinjured02 with fastdissolve
                    mc "Yeah, why? Was good is that?"
                    pe "It's also a health kit. Use it and get back on your feet, I ain't fighting alone!"
                if withbe and whbella_health >= 0.1:
                    be "Don't you have a repair kit?"
                    scene whitehousemcinjured02 with fastdissolve
                    mc "Yeah, why? Was good is that?"
                    be "It's also a health kit. Use it and get back on your feet, I ain't fighting alone!"
                if withwi and and whwidow_health >= 0.1:
                    wi "Don't you have a repair kit?"
                    scene whitehousemcinjured02 with fastdissolve
                    mc "Yeah, why? Was good is that?"
                    wi "It's also a health kit. Use it and get back on your feet, I ain't fighting alone!"
                scene whitehousemcinjured03 with fastdissolve
                mc "Ooh, really? I KNEW this thing would come in handy one day..."
                $ counting = 0
                while counting < 20:
                    $ whmc_health += 0.1
                    $ counting += 1
                    pause 0.01
                mc "Yeah, back on my feet in no time!"
                jump WhiteHouseRound
            if repairkit == False:
                mc "I guess I have no choice but to go back to the compound... What a waste."
                call MCInjury
                $ mcinjuredgun = True
                jump BackCompoundWhiteHouse
    else:
        mc "HA, she missed! Let's take cover behind the car before she shoots again..."
        if whguard01out or whguard01_health <= 0.09:
            jump WhiteHouseRound
        scene whitehouse02
        if laststanding:
            jump WhiteHouseRound        
        if withbe and whbella_health >= 0.1:
            scene whitehouse02
            show whitehouse02bellashoot
            if whguard01_health <= 0.09:
                show whguard01down
            with dissolve
        if withpe and whbella_health >= 0.1:
            scene whitehouse02
            show whitehouse02pennyshoot
            if whguard01_health <= 0.09:
                show whguard01down
            with dissolve
        if withwi and whbella_health >= 0.1:
            scene whitehouse02
            show whitehouse02widowshoot
            if whguard01_health <= 0.09:
                show whguard01down
            with dissolve            

else:
    mc "I'll take cover and reload my rifle then."
    if laststanding:
        jump WhiteHouseRound        
    if withbe and whbella_health >= 0.1:
        scene whitehouse02
        show whitehouse02bellashoot
        if whguard01_health <= 0.09:
            show whguard01down
        with dissolve
    if withpe and whbella_health >= 0.1:
        scene whitehouse02
        show whitehouse02pennyshoot
        if whguard01_health <= 0.09:
            show whguard01down
        with dissolve
    if withwi and whbella_health >= 0.1:
        scene whitehouse02
        show whitehouse02widowshoot
        if whguard01_health <= 0.09:
            show whguard01down
        with dissolve            
$ whguard02out = False

if whguard01out == False and whguard01_health >= 0.1:
    play sound "v10/gunfire.mp3"
    call DiceRoll
    if diceroll >= 4 and withbe and whbella_health >= 0.1:
        $ counting = 0
        while counting < 20:
            $ whbella_health -= 0.05
            $ counting += 1
            pause 0.01
        if whbella_health >= 0.1:
            be "I'm hit! But I will pray the pain away."
            hide whitehouse02bellashoot
            show whitehouse02bella01
            if whguard02_health <= 0.09:
                show whguard02down
            with dissolve
            be "I'm reloaded and ready to shoot again. Give the signal."
            jump WhiteHouseRound           
        if whbella_health <= 0.09:
            scene whitehousebellainjured with dissolve
            be "I'm out [name]! I've been shot too badly..."
            menu:
                "Continue fighting alone":
                    mc "Ok Bella, get out of here, I'll take it from there, after all, I'm the HERO!"
                    $ laststanding = True
                    jump WhiteHouseRound
                "Retreat and go back to the compound":
                    jump BackCompoundWhiteHouse

    if diceroll <= 3 and withbe and whbella_health >= 0.1:
        be "She missed! The Phallus Lord is protecting me."
        hide whitehouse02bellashoot
        show whitehouse02bella01
        if whguard02_health <= 0.09:
            show whguard02down
        with dissolve
        be "I'm reloaded and ready to shoot again. Give the signal."
        jump WhiteHouseRound           

    if diceroll >= 4 and withpe and whpenny_health >= 0.1:
        $ counting = 0
        while counting < 20:
            $ whpenny_health -= 0.05
            $ counting += 1
            pause 0.01
        if whpenny_health >= 0.1:
            pe "I'm hit! Damn you, rain!"
            hide whitehouse02pennyshoot
            show whitehouse02penny01
            if whguard02_health <= 0.09:
                show whguard02down
            with dissolve
            pe "I'm reloaded and ready to shoot again. Give the signal."
            jump WhiteHouseRound   
        if whpenny_health <= 0.09:
            scene whitehousepennyinjured with dissolve
            pe "I'm out [name]! I've been shot too badly..."
            menu:
                "Continue fighting alone":
                    mc "Ok Penny, get out of here, I'll take it from there, after all, I'm the HERO!"
                    $ laststanding = True
                    jump WhiteHouseRound
                "Retreat and go back to the compound":
                    jump BackCompoundWhiteHouse
    
    if diceroll <= 3 and withpe and whbella_health <= 0.09:
        pe "She missed! She ain't no Road Warrior!"
        hide whitehouse02pennyshoot
        show whitehouse02penny01
        if whguard02_health <= 0.09:
            show whguard02down
        with dissolve
        pe "I'm reloaded and ready to shoot again. Give the signal."
        jump WhiteHouseRound           

    if diceroll >= 4 and withwi:
        $ drollbulletwidow=renpy.random.randint(1,2)
        if drollbulletwidow == 1:
            $ counting = 0
            while counting < 20:
                $ whwidow_health -= 0.05
                $ counting += 1
                pause 0.01
            if whwidow_health >= 0.1:
                wi "I'm hit! I can't believe they would shoot a Hollywood actress! I mean, The BLACK WIDOW!"                    
                hide whitehouse02widowshoot
                show whitehouse02widow01
                if whguard02_health <= 0.09:
                    show whguard02down
                with dissolve
                wi "I'm reloaded and ready to shoot again. Give the signal."
                jump WhiteHouseRound   
            if whwidow_health <= 0.09:
                scene whitehousewidowinjured with dissolve
                wi "I'm out [name]! I've been shot too badly..."
                menu:
                    "Continue fighting alone":
                        mc "Ok Black Widow, get out of here, I'll take it from there, after all, I'm the HERO!"
                        $ laststanding = True
                        jump WhiteHouseRound
                    "Retreat and go back to the compound":
                        jump BackCompoundWhiteHouse
        if drollbulletwidow == 2:
            wi "She got me but my bullet-proof vest took the brunt of it. The Black Widow PREVAILS once again!"
            hide whitehouse02widowshoot
            show whitehouse02widow01
            if whguard02_health <= 0.09:
                show whguard02down
            with dissolve
            wi "I'm reloaded and ready to shoot again. Give the signal."
            jump WhiteHouseRound   
    
    if diceroll <= 3 and withwi:
        wi "She missed! The Black Widow survives ONCE AGAIN!"
        hide whitehouse02widowshoot
        show whitehouse02widow01
        if whguard02_health <= 0.09:
            show whguard02down
        with dissolve
        wi "I'm reloaded and ready to shoot again. Give the signal."
        jump WhiteHouseRound           

    if diceroll >= 4 and laststanding:
        $ counting = 0
        while counting < 20:
            $ whmc_health -= 0.05
            $ counting += 1
            pause 0.01
        if whmc_health >= 0.1:
            mc "Shit, I'm hit!"
            hide whitehouse02mcshoot
            show whitehouse02
            if whguard02_health <= 0.09:
                show whguard02down
            with dissolve
            mc "Let's take cover and reload..."
            jump WhiteHouseRound           
        if whmc_health <= 0.09:
            scene whitehousemcinjured with dissolve
            be "I'm out [name]! I've been shot too badly..."
            menu:
                "Continue fighting alone":
                    mc "Ok Bella, get out of here, I'll take it from there, after all, I'm the HERO!"
                    scene whitehouse02 with dissolve
                    jump WhiteHouseRound
                "Retreat and go back to the compound":
                    scene whitehouse01 with dissolve

if whguard01out or whguard01_health <= 0.09:
    if withbe and whbella_health >= 0.1:
        hide whitehouse02bellashoot
        show whitehouse02bella01
        with dissolve
        be "I'm reloaded and ready to shoot again. Give the signal."
    if withpe and whpenny_health >= 0.1:
        hide whitehouse02pennyshoot
        show whitehouse02penny01
        with dissolve
        pe "I'm reloaded and ready to shoot again. Give the signal."
    if withwi and whwidow_health >= 0.1:
        hide whitehouse02widowshoot
        show whitehouse02widow01
        with dissolve
        wi "I'm reloaded and ready to shoot again. Give the signal."
    
$ whguard01out = False
$ whguard02out = False
jump WhiteHouseRound   

label BackCompoundWhiteHouse:
$ period = 4
hide screen screenfightwhbase
if withbe:
    hide screen screenfightwhbella
if withpe:
    hide screen screenfightwhpenny
if withwi:
    hide screen screenfightwhwidow
show screen mcstats
show screen calendar
scene command01
show lena06
with fade
le "So, what happened? Did you kick Trumpf out of the White House?"
if mcinjured:
    mc "Err... Not yet. There was intense gunfight there and I was badly shot..."
if mcinjured == False:
    mc "Err... Not yet. There was intense gunfight and I couldn't fight those damn cloned militia guards off on my own..."
hide lena06
show lena03
with dissolve
le "You're getting close. And yet you are still so far... Go to the medbay and try AGAIN."
jump Medbay

label WhiteHouseDoor:
stop music
stop sound
hide screen screenfightwhbase
if withbe:
    hide screen screenfightwhbella
if withpe:
    hide screen screenfightwhpenny
if withwi:
    hide screen screenfightwhwidow

scene whitehouseentrance with fade
mc "Finally, I'm inside the Supreme White House!"
window hide
show kimwh01 with moveinright
kg "And where do you think YOU'RE going?"
mc "Stand aside crazy woman, you are no match for..."
hide kimwh01
show kimwh02
with dissolve
kg "AAARGH, AN INTRUDER, THAT MAKES ME MAD AND ANGRY!"
mc "Err..."
hide kimwh02
show kimwh03
with dissolve
play sound "Sounds/ripping.mp3"
$ renpy.pause(0.5, hard='True')
kg "YOU'VE MADE ME EXTREMELY ANGRY!"
mc "Well, let's just calm down for a seco..."
hide kimwh03
show kimwh04
with dissolve
play sound "Sounds/hulkgrowl01.mp3"
kg "AND WHEN I GET ANGRY, MY MUSCLES GET REALLY MAD!"
mc "Uuh-oh..."
kg "NOW GET YOUR COCK OUT, I'M GOING TO FUCK YOU TO... DEATH!"
mc "Alright, alright, gee, can't even walk into the White House without getting sexually assaulted these days."
scene whitehouseentrance blurred
show kimwh05
with dissolve
kg "First, I'll make you spew your MOJO so you'll be an easier... PREY!"
mc "Oh, behave!"
stop music
play channel1 "Sounds/wank.mp3"
play channel2 "Sounds/boymoan.mp3"
scene whitehouseentrance blurred
show kimwankslow
call screen kimhandjobslow
screen kimhandjobslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("KimHandjobFast") 

label KimHandjobFast:
kg "And now, I'll go even FASTER, for the KILL!"
mc "I can take it, I'm a trained... wanker! Just like your boss."
kg "DO NOT MOCK OUR BELOVED CULT LEADER!"
hide kimwankslow
show kimwankfast
call screen kimhandjobfast
screen kimhandjobfast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KimHandjobEnd")

label KimHandjobEnd:
kg "I can feel you getting there... LET YOUR MOJO SPILL OUT!"
stop channel1
stop channel2
hide kimwankfast
show kimwankcum01
with dissolve
play music "Sounds/moaning03.ogg"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "AAAH! I can't hold BA-AAA-CK!"
window hide
with fastflash
kg "That's it, MORE OF IT!"
hide kimwankcum01
show kimwankcum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "GODAAAMMMMMIIIT! RHAAAA!"
window hide
with fastflash
kg "YOU ARE DEFEATED, SUBMIT TO MY SUPERIOR HAND MUSCLES!"
stop music
play sound "Sounds/boymoan02.mp3"
hide kimwankcum02
show kimwankcum03
with fastdissolve
mc "NOT YET, AAAHH!"
window hide
with fastflash
kg "YOU MIGHT COME LIKE A CUM FOUNTAIN, BUT YOUR MOJO IS SLOWLY DRAINING OUT OF YOU!"
window hide
with fastflash
mc "My Mojo is UNLIMITED, RHAAA!"
stop music
play sound "Sounds/panting.mp3"
hide kimwankcum03
show kimwankcum04
with dissolve
kg "In that case, I have no choice but to SQUEEZE IT OUT WITH MY PUSSY MUSCLES!"
mc "Damn it woman, let me breathe for a min..."
kg "NO, SIT ON THE STAIRS AND PREPARE TO GET YOUR COCK SQUISHED TO OBLIVION!"
scene kimwhprefuck00 with dissolve
kg "You're still hard... BUT YOU WON'T BE FOR LONG!"
scene kimwhprefuck01 with dissolve
kg "ALL THAT FILTHY SPUNK DRIPPING DOWN YOUR SCHLONG... I'LL MAKE BETTER USE OF IT!"
scene kimwhprefuck02 with dissolve
kg "Right there, between my asscheeks. SQUEEZING YOUR SHAFT!"
mc "AAAH, your glutes are like STEEL!"
kg "THAT'S RIGHT, AND MY PUSSY IS LIKE TITANIUM!"
stop music
play channel1 "Sounds/debrasex.mp3"
play channel2 "Sounds/panting.mp3"
scene whitehouseentrance blurred
show kimfuckslow
call screen kimfuckslow
screen kimfuckslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("KimFuckFast") 

label KimFuckFast:
kg "I'VE BEEN TOO KIND SO FAR, NOW YOU WILL FEEL MY PUSSY MUSCLES CLAMPING DOWN... HARD!!!!"
mc "Do... your... worst... I can take it... AAAH."
kg "WE'LL SEE ABOUT THAT!"
hide kimfuckslow
show kimfuckfast
call screen kimfuckfast
screen kimfuckfast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KimFuckEnd")

label KimFuckEnd:
scene kimwhfuckcum01 with dissolve
kg "Can you feel your cock being slowly SQUEEZED like a VICE?"
scene kimwhfuckcum02 with dissolve
mc "AAAH, it hurts but I can take it!"
scene kimwhfuckcum03 with dissolve
kg "Can you now, Are you SURE?"
if exploredhex56third == False:
    stop channel2
    play sound "Sounds/crunch.mp3"
    scene kimwhfuckcum06a with dissolve
    $ renpy.pause(2.0, hard='True')    
    play sound "Sounds/pain.mp3"
    mc "AAAAH, I'm trying to cum but you're squeezing me TOO TIGHT!"
    window hide
    with fastflash
    scene kimwhfuckcum06b with dissolve
    play sound "Sounds/crunch.mp3"    
    kg "YOUR SPUNK WLL BE FORCED BACK INTO YOUR BLADDER UNTIL YOU PASS OUT!"
    window hide
    with fastflash
    play sound "Sounds/pain.mp3"
    mc "NOOOO, AAAAH!"
    $ renpy.pause(2.0, hard='True')      
    stop channel1
    stop music
    stop sound
    scene kimwhlose with fade
    kg "NO COCK CAN WITHSTAND THE POWER OF MY PUSSY!"
    call MCInjury
    $ mcinjuredcock = True
    kg "NOW BEGONE, OUT OF THE MNAGAT PEOPLE'S HOUSE!"
    if persistent.tipson:
        show hexwh01tip at tips with dissolve
        pause
        hide hexwh01tip
    $ period = 4
    scene command01
    show lena03
    with fade
    le "You're back? I'm going to venture that you failed miserably."
    mc "Miserable is the word. For my bladder and twisted cock..."
    hide lena03
    show lenapensive
    with fastdissolve
    le "Do I want to see that injury? No, I think not. Off you go to the medbay, see if nurse Rachel can do anything about this miserable dick of yours." 
    hide lenapensive with dissolve
    jump Medbay    
    
if exploredhex56third:
    scene kimwhfuckcum04 with dissolve
    mc "Yes, I AM SURE! And I'll PROVE IT TO YOU RIGHT NOW BY CUMMING UNTIL YOUR PUSSY IS OVERFILLED WITH MY SUPERIOR SPUNK!"
    stop channel1
    stop channel2
    play channel2 "Sounds/splooge02.mp3"
    play channel1 "Sounds/boycum.mp3"
    scene kimwhfuckcum05 with dissolve
    mc "There you go, RHAAA!"
    window hide
    with fastflash
    kg "MY PUSSY WILL SWALLOW YOUR MEAGER OFFERING!!!"
    window hide
    with fastflash
    scene kimwhfuckcumpreggo:
        ypos -1.0
        linear 4.0 ypos -0.0
    pause 5.0
    kg "WHAT??? MY BELLY IS... EXPLODING... YOU'RE CUMMING TOO MUCH, I CAN't HOLD ONTO YOUR DISGORGING SHAFT, AAAH!"
    stop channel2
    stop channel1
    play music "Sounds/cumming.mp3"
    scene kimwhmegacum01 with dissolve
    mc "RHAAAA! MEGACUM!!!!"
    play sound "Sounds/waterspray.mp3"
    window hide
    with fastflash
    kg "AAAH, WHAT IS HAPPENING???"
    window hide
    with fastflash
    mc "I AM THE ULTIMATE PUSSY-WRECKER!!!"
    stop music
    scene kimwhmegacum02 with fade
    mc "The stairs look a bit too slippery. If you'll excuse me, I think I'll take the lift..."
    kg "Gggg... Aaaaah..."
    jump PreVPOffice

label PreVPOffice:
stop sound
stop music
show whitehousecorridor02 with dissolve
mc "Mmmh... A corridor with two doors. One on the left and one on the right..."
mc "I'm leaning right on that one. Like Virginia lately."

label VPOffice:
scene pence01 with dissolve
mp "Please come in and sit down [name], I was expecting you."
mc "Err... I'm just looking for the Oval Office actu..."
mp "We MUST talk. About your FUTURE."
scene pence02a with dissolve
mc "Fine, I guess... Who the fuck are you anyway?"
play music "v10/buzzpence.mp3"
scene pence02b with fastdissolve
mp "I am Mike Ponce, head of the Phallus Force."
stop music
scene pence02a with fastdissolve
mc "The what? Why are your eyes and mou..."
play music "v10/buzzpence.mp3"
scene pence02b with fastdissolve
play music "v10/buzzpence.mp3"
if mcchurch == 5:
    mp "I am detecting that you are a member of the Church."
    stop music
    scene pence02a with fastdissolve    
    mc "Correct, but I am here to..."
    play music "v10/buzzpence.mp3"
    scene pence02b with fastdissolve
    mp "Then JOIN US. Join the Phallus Force. Devote your ENTIRE LIFE to the Church."
    mc "He's... hypnotizing me. He's a hypno-robot! I..."
    show churchtotal
    stop music
    scene pence02a with fastdissolve    
    mc "Yes, Yes, I see the LIGHT. The red light from your eyes to be precise. I WILL DEVOTE MY ENTIRE LIFE TO THE CHURCH!"
    play music "v10/buzzpence.mp3"
    scene pence02b with fastdissolve    
    mp "Good. Then it's game over for you."
    mc "Err, what the f..."
    return

if mcchurch <= 4:
    mp "I am detecting that you are not a member of the Church."
    stop music
    scene pence02a with fastdissolve    
    mc "Yeah, so?"
    play music "v10/buzzpence.mp3"
    scene pence02b with fastdissolve    
    mp "The Phallus Force is here to protect New America from Alien Heretical Invaders, it is the most IMPORTANT branch of the military."
    mp "You MUST join us. Join the Phallus Force! NOW!"
    call PlusChurchReal
    stop music
    scene pence02a with fastdissolve    
    mc "Damn, he's... hypnotizing me, he's a hypno-robot! I... must... fight it!"
    play music "v10/buzzpence.mp3"
    scene pence02b with fastdissolve    
    mp "Stay. Let's talk some more about the PHALLUS FORCE."
    stop music
    scene pence02a with fastdissolve
    play sound "Sounds/panting.mp3"
    mc "No! Let's... get out of here... before he... enlists me!"
    jump PreOvalOffice

label PreOvalOffice:
stop sound
stop music
show whitehousecorridor02 with dissolve
mc "Phew! That was close. I guess I'll take the left door this time..."
    
label OvalOffice:
if seenovaloffice == True:
    scene ovaloffice01
    show melaniaoval01 at left
    show ivankaoval02 at right
    with dissolve
    me "You AGAIN!"
    iv "Prepare to FIGHT!"
    mc "What, no negociating this time, nothing?"
    iv "NO! FIGHT ME YOU SNOWFLAKE! AFTER I GET INTO MY FIGHTING GEAR!"
    window hide
    hide ivankaoval02 with moveoutright
    me "I'll leave him to you Ivanka..."
    window hide
    hide melaniaoval01 with moveoutleft
    mc "Err... So, are we fighting or not?"
    window hide
    show ivankaprefight01 with moveinright
    iv "Yes we ARE!"
    jump IvankaFight
scene ovaloffice01
show melaniaoval00 at left
show ivankaoval00 at right
with dissolve
me "So, Ivanka, what did you buy Donald for his birthday party?"
iv "I have a framed photoshopped picture of his re-inauguration with millions of people on it."
$ seenovaloffice = True
hide melaniaoval00
hide ivankaoval00
show melaniaoval01 at left
show ivankaoval01 at right
with fastdissolve
me "What are YOU doing here? Can't I have some peace from you once in a while?"
mc "I'm here to kick Trumpf out of this office!"
hide ivankaoval01
show ivankaoval02 at right
with fastdissolve
iv "I will protect Daddy! I am next in line, and won't be if YOU take his place!"
if clearedhex65:
    mc "Are you aware that your mother-in-law is in fact a treasonous SPY who works for Vladimir Pewtin?"
    hide ivankaoval02
    show ivankaoval02b at right
    with fastdissolve
    iv "Yeah, so? We knew that all along, we let her do it since the Russians work for Daddy during election time!"
    hide melaniaoval01
    show melaniaoval02b at left
    with fastdissolve    
    me "Oh? I didn't realize that. I thought I was being clever."
    hide melaniaoval02b
    show melaniaoval01 at left
    with fastdissolve
    
mc "Let me through ladies, this is between HIM and ME!"
hide ivankaoval02b
show ivankaoval02 at right
with fastdissolve
iv "My stake is too high. What do you offer in return for such a favor?"
hide melaniaoval01
show melaniaoval02 at left
with fastdissolve    
me "Why are you doing this Ivanka? I thought you loved your daddy!"
menu:
    "I offer you all my money and a nice cushy job as my Special Adviser.":
        hide ivankaoval02
        hide melaniaoval02
        show melaniaoval01 at left
        show ivankaoval02b at right
        with fastdissolve
        iv "And how much money do you have exactly?"
        mc "[money] dollars."
        if money <= 99:
            hide ivankaoval02b
            show ivankaoval02 at right
            with fastdissolve
            iv "That little? This is insulting! Prepare to FIGHT! Let me get into my FIGHTING GEAR!"
            window hide
            hide ivankaoval02 with moveoutright
            me "I'm out of this..."
            window hide
            hide melaniaoval01 with moveoutleft
            mc "Err... So, are we fighting or not?"
            window hide
            show ivankaprefight01 with moveinright
            iv "Yes we ARE!"
            $ ivankafirst = True
            jump IvankaFight
        if money >= 100:
            hide ivankaoval02b
            show ivankaoval04 at right
            with fastdissolve
            iv "Not bad, I could buy myself a condo in Flori-duh with that much money."
            mc "Really? Man, real estate really took a beating afer that war then..."
            hide ivankaoval04
            show ivankaoval01 at right
            with fastdissolve
            iv "Still, about the adviser job... Advising you on what exactly?"
            mc "Anything you want. You'd be leading really basically since I have zero qualification for the job, just like your father."
            hide ivankaoval01
            show ivankaoval04 at right
            with fastdissolve
            iv "And I'd still be in charge of the Militia?"
            mc "The [name] Militia, yes."
            iv "Maybe then... It doesn't sound like such a bad deal. And you have a much bigger cock than Daddy."
            hide melaniaoval01
            show melaniaoval02b at left
            with fastdissolve
            me "What? How would YOU know that? He swore he would be faithful to me!"
            hide ivankaoval04
            show ivankaoval06 at right
            with fastdissolve            
            iv "Well, err... He's my Daddy! How could I refuse?"
            hide melaniaoval02b
            show melaniaoval04 at left
            with fastdissolve
            me "I'll deal with YOU and HIM later, right now, I have a little surprise for [name]..."
            hide ivankaoval06
            show ivankaoval01 at right
            with fastdissolve            
            mc "A surprise? Oh, I LOVE surp..."
            window hide
            play sound "Sounds/taser.mp3"
            scene ovalofficetased with hpunch
            $ renpy.pause(2.0, hard=True)
            me "Surprise!"
            mc "Hey, how did you do that? I thought that damn implant had been removed! Now here's MY surprise, prepare to FIGHT! And I'll go first cos I said it first!"
            scene ovaloffice01
            show melaniaoval09 at left
            show ivankaoval01 at right            
            me "Well, that's gonna be easy...."
            iv "I'm... out of your way for that nasty fight scene..."
            hide ivankaoval01 with moveoutright
            jump MelaniaFight    
    "I offer you my fist in your face! (FIGHT - Close Combat)":
            iv "Fine, let's FIGHT! Let me get into my FIGHTING GEAR!"
            window hide
            hide ivankaoval02 with moveoutright
            me "I'm out of this..."
            window hide
            hide melaniaoval02 with moveoutleft
            mc "Err... So, are we fighting or not?"
            window hide
            show ivankaprefight01 with moveinright
            iv "Yes we ARE!"
            jump IvankaFight
            
label IvankaFight:
hide screen mcstats
hide screen calendar
scene ovalofficefight
show mcovalfight01 at farleft
show ivankafight01 at farright
with dissolve
with dissolve
$ mc_health = 2.0
$ ivanka_health = 2.0
show screen screenfightmcivanka

label IvankaRound:
if ivankafirst:
    jump RoundIvankaFight
if ivankafirst == False:
    jump RoundMCIvankaFight

label RoundIvankaFight:  
mc "Come and get some, I dare you Ivanka!"
window hide
show ivankafight01 at centerright with move
window hide
label RoundIvankaFightb:
call DiceRoll
if diceroll >= 3:
    hide mcovalfight01
    hide ivankafight01
    show ivankafight06 at left
    with fastdissolve
    play sound "Sounds/punch.mp3"
    iv "No groin can RESIST me!"
    $ counting = 0
    while counting < 20:
        $ mc_health -= 0.05
        $ counting += 1
        pause 0.01
    if mc_health >= 0.1:
        mc "I'm not out, unlike Jared after twenty seconds!"
    if mc_health <= 0:
        hide ivankafight06
        show mcovalfight05 at left
        with fastdissolve
        play sound "Sounds/pain.mp3"
        mc "I yield, you win, I'm just a snowflake..."
        call MCInjury
        $ mcinjuredfight = True
        jump IvankaWinFightEnd        
    hide ivankafight06
    show mcovalfight01 at farleft
    show ivankafight01 at farright
    with fastdissolve
else:
    hide mcovalfight01
    hide ivankafight01
    show ivankafight05 at left
    with fastdissolve
    mc "MY muscles are stronger than YOUR muscles!"
    hide ivankafight05
    show mcovalfight01 at farleft
    show ivankafight01 at farright
    with fastdissolve
$ ivankafirst = False
jump IvankaRound

label RoundMCIvankaFight:  
mc "I'll show you that I've trained a LOT since our last meeting!"
window hide
show mcovalfight01 at center with move
with fastdissolve
call DiceRoll
$ dcombatroll=mccombat+diceroll        
if (dcombatroll >= 13 and not diceroll == 1) or diceroll == 6:
    window hide
    hide mcovalfight01
    hide ivankafight01
    show mcivankafight02 at right
    with fastdissolve
    play sound "Sounds/punch.mp3"
    mc "White House INTERN-AL damage! Got it?"
    if ivanka_health >= 0.1:
        $ counting = 0
        while counting < 20:
            $ ivanka_health -= 0.05
            $ counting += 1
            pause 0.01
    if ivanka_health <= 0:
        hide mcivankafight02
        show mcivankafight03 at right
        with fastdissolve
        mc "I'm a winner baby! So why don't you fuck me. Get naked ladies and get ready for my Mighty Rod of Impalement!"
        jump IvankaFightWin
    hide mcivankafight02
    show mcovalfight01 at farleft
    show ivankafight01 at farright
    with fastdissolve
if (dcombatroll <= 12 and not diceroll == 6) or diceroll == 1:
    window hide
    hide mcovalfight01
    hide ivankafight01
    show ivankafight02 at right
    with fastdissolve
    mc "Damn, she's quick despite those large funbags!"
    hide ivankafight02
    show ivankafight03 at right
    with fastdissolve
    play sound "Sounds/thud.mp3"
    iv "Look at you, LOSER!"
    mc "I'll try again. And AGAIN!"
    hide ivankafight03
    show mcovalfight01 at farleft
    show ivankafight01 at farright
    with fastdissolve
    
$ ivankafirst = True
jump IvankaRound   

label IvankaFightWin:
hide screen screenfightmcivanka
show screen mcstats
show screen calendar
me "Alright, you win. THIS time. I need more Special Pizza Sauce anyway."
jump OvalOfficeSex

label IvankaWinFightEnd:
hide screen screenfightmcivanka
show screen mcstats
show screen calendar
iv "The Trumpf dynasty is safe now! Go back to your compound and don't you dare ever come back!"
mc "Y... Yes, thank you for your kindness, General Ivanka..."
stop music
$ period += 1
scene command01
show lena01
with fade
le "What happened in the Supreme White House? Did you kick Trumpf out yet?"
mc "Err... No, Ivanka kicked my butt..."
hide lena01
show lena06
with fastdissolve
le "Well, that must be embarrassing."
mc "Yes, it is...It surely is... Now if you'll excuse me, I'll show myself to the medbay..."
jump Medbay

label MelaniaFight:
hide screen mcstats
hide screen calendar
scene ovalofficefight
show mcovalfight01 at farleft
show melaniafight01 at farright
with dissolve
with dissolve
$ mc_health = 2.0
$ melania_health = 2.0
show screen screenfightmcmelania

label MelaniaRound:
if melaniafirst:
    jump RoundMelaniaFight
if melaniafirst == False:
    jump RoundMCMelaniaFight

label RoundMelaniaFight:  
me "Well, that's gonna be easy. All I have to do is press this button..."
mc "Uh Oh..."
window hide
hide melaniafight01
show melaniafight04a at farright
window hide
label RoundMelaniaFightb:
call DiceRoll
if diceroll >= 4:
    hide mcovalfight01
    show melaniafight05 at farleft
    with fastdissolve
    play sound "Sounds/taser.mp3"
    $ counting = 0
    while counting < 20:
        $ mc_health -= 0.05
        $ counting += 1
        pause 0.01
    if mc_health >= 0.1:
        mc "AAAH, fuck it hurts!"
    if mc_health <= 0:
        hide melaniafight05
        hide melaniafight04a
        show melaniafight07 at left        
        with fastdissolve
        play sound "Sounds/panting.mp3"
        mc "I yield, please stop pressing that button, I can't take it anymore."
        call MCInjury
        $ mcinjuredtaser = True
        jump MelaniaWinFightEnd        
    hide melaniafight05
    hide melaniafight04a
    show mcovalfight01 at farleft
    show melaniafight01 at farright
    with fastdissolve
else:
    hide melaniafight04a
    show melaniafight04b at farright
    window hide    
    me "What's happening, why won't that remote work?"
    hide mcovalfight01
    show melaniafight06 at farleft02    
    mc "HA! It's the Chinese 5G waves that are disrupting it! And now it's MY turn to ATTACK!"
    hide melaniafight06
    hide melaniafight04b
    show mcovalfight01 at farleft
    show melaniafight01 at farright
    with fastdissolve
$ melaniafirst = False
jump MelaniaRound

label RoundMCMelaniaFight:  
mc "I'm going to re-arrange that botox in your face, Melania!"
window hide
show mcovalfight01 at center with move
with fastdissolve
call DiceRoll
$ dcombatroll=mccombat+diceroll        
if (dcombatroll >= 11 and not diceroll == 1) or diceroll == 6:
    window hide
    hide melaniafight01
    hide mcovalfight01
    show melaniafight02 at right
    with fastdissolve
    play sound "Sounds/slap.mp3"
    me "How dare you slap the First Lady?"
    if melania_health >= 0.1:
        $ counting = 0
        while counting < 20:
            $ melania_health -= 0.05
            $ counting += 1
            pause 0.01
    if melania_health <= 0:        
        mc "I'm the First Man to beat the First Lady! And I won't be the last to FUCK her! So get naked ladies and get ready for my Mighty Rod of Impalement!"
        hide melaniafight02
        show melaniafight08
        with dissolve
        me "Let me down, you oaf!"
        jump MelaniaFightWin
    mc "You've got a very slappable face!"
    hide melaniafight02
    show mcovalfight01 at farleft
    show melaniafight01 at farright
    with fastdissolve
if (dcombatroll <= 10 and not diceroll == 6) or diceroll == 1:
    window hide
    hide melaniafight01
    hide mcovalfight01
    show melaniafight03 at right
    with fastdissolve
    with fastdissolve
    mc "Damn, she ducked before I could slap her!"
    me "I don't care, do u?"
    hide melaniafight03
    show mcovalfight01 at farleft
    show melaniafight01 at farright
    with fastdissolve
$ melaniafirst = True
jump MelaniaRound   

label MelaniaFightWin:
hide screen screenfightmcmelania
show screen mcstats
show screen calendar
iv "Alright, you win. THIS time. We have some time before Daddy arrives anyway..."
jump OvalOfficeSex

label MelaniaWinFightEnd:
hide screen screenfightmcmelania
show screen mcstats
show screen calendar
me "You will NOT make ONE MORE STEP in this Oval Office. Go back to your compound and never come back, [name]!"
mc "Y... Yes First Lady, I will obey..."
stop music
$ period += 1
scene command01
show lena01
with fade
le "What happened in the Supreme White House? Did you kick Trumpf out yet?"
mc "Err... No, I was kicked out. By Melania..."
hide lena01
show lena06
with fastdissolve
le "Well, that must be embarrassing."
mc "Yes, it is...It surely is... Now if you'll excuse me, I'll show myself to the medbay..."
jump Medbay

label OvalOfficeSex:
scene ovaloffice02
show mcprewhfuck01
with dissolve
mc "See this? That's a schlong worthy of a REAL President!"
play sound "v08/wow.mp3"
me "Indeed... But how much Special Pizza Sauce can it deliver?"
iv "And how DEEP can it get into our pussies?"
hide mcprewhfuck01
show mcprewhfuck02
with dissolve
play sound "Sounds/lick.mp3"
mc "I'll show you soon enough. But first, I want a taste of those succulent nipples..."
scene ovaloffice02zoom blurred
show mcprewhfuck03
with dissolve
play sound "Sounds/slurp.mp3"
mc "Let me get a taste of your mommy-milk..."
iv "Oooh, but... That's normally reserved for my children..."
mc "Not anymore... I take what's MINE!"
iv "You're so forceful and... MANLY. Kiss me please..."
hide mcprewhfuck03
show mcprewhfuck04
with dissolve
play sound "Sounds/kiss.mp3"
me "Now that you're here, UNINVITED, with your massive cock all ROCKHARD and READY, why don't you show us some good times, [name]?"
mc "Of course First Lady... Get on all fours on the Oval Office carpet and I'll show you some GREAT times!"

scene whpredoggybackground
show whpredoggyanimslow
with dissolve
play music "Sounds/moaning02.mp3"
mc "Now that's better ladies. So, who will go first I wonder?"
menu:
    "Melania":
        mc "First Lady first..."
        jump MelaniaHouseFuck
    "Ivanka":
        mc "Muscles galore for my BIG MUSCLE first!"
        jump IvankaHouseFuck

label MelaniaHouseFuck:
stop music
scene whivankacumbackgroundzoom
show whmelaniaprefuck
with dissolve
mc "Ready First Lady?"
play sound "Sounds/moaning.mp3"
me "Mmmh, YES I AM!"
label MelaniaHouseFuckb:
stop music
play music "Sounds/womansex01.mp3"
scene whdoggymelaniabackground blurred
label MelaniaHouseSlow:
hide melaniawhdoggyfast
show melaniawhdoggyslow
call screen melaniawhfuckslow01
screen melaniawhfuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("MelaniaHouseEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MelaniaHouseFast") 
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("IvankaHouseSwitch") 

label MelaniaHouseFast:
if melaniadeep:
    mc "I'm the FIRST man that DEEP inside the First Lady! Fuck Yeah!"
if melaniadeep == False:
    mc "You love that cock, don't you Melania?"
    me "YES, I LOVE IT, I admit it, just shut up and FUCK MY DIRTY HOLE HARDER!"
    $ melaniadeep = True
hide melaniawhdoggyslow
show melaniawhdoggyfast
call screen melaniawhfuckfast01
screen melaniawhfuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("MelaniaHouseEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MelaniaHouseSlow")
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("IvankaHouseSwitch") 
        
label MelaniaHouseEnd:
me "DUMP your load inside my First Lady pussy [name]!"
stop music
play music "Sounds/splooge02.mp3"
scene whdoggymelaniabackground blurred
show whmelaniacum01
with dissolve
mc "You don't need to ask me twice, AAAAH"
window hide
with fastflash
me "Oh God, he's really FIRING his shots up my super-elite fuckhole!"
hide whmelaniacum01
show whmelaniacum02
with dissolve
play sound "Sounds/womanscream.ogg"
me "AAAH, sssoo sssoo DEEP, directly into my womb!"
window hide
with fastflash
mc "Damn right, RHAAAA!"
window hide
with fastflash
me "Pull out and DOUSE my back with your warm spunk!"
stop music
scene whmelaniacumbackground
show whmelaniacum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "There you go, massive ball-busting nutload coming your way, RHAAA!"
$ melaniaload = True
window hide
with fastflash
iv "Oh fuck, I want some of that too... It looks so yummy..."
hide whmelaniacum03
show whmelaniacum04
with dissolve
play sound "Sounds/panting.mp3"
if ivankaload:
    mc "Then come and slurp it up Ivanka..."
    jump WhbothfuckEnd
if ivankaload == False:
    mc "Don't you worry, I've got enough cum left for YOUR PUSSY!"
    iv "Please, fuck me, I'm dying to feel that GIANT shaft STRETCHING my hole..."
    jump IvankaHouseFuck

label IvankaHouseSwitch:
mc "Gonna switch before I cum inside that tight hole, aaah... Get ready Ivanka!"
jump IvankaHouseFuckb

label IvankaHouseFuck:
stop music
scene whivankacumbackgroundzoom
show whivankaprefuck
with dissolve
mc "Ready Ivanka?"
play sound "Sounds/moaning.mp3"
iv "Always ready for a big fat teenage MONSTERCOCK!"
label IvankaHouseFuckb:
stop music
play music "Sounds/womansex02.mp3"
label IvankaHouseSlow:
scene whdoggyivankabackground blurred
show ivankawhfuckslow
call screen ivankawhfuckslow01
screen ivankawhfuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("IvankaHouseEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("IvankaHouseFast") 
    imagebutton:
        focus_mask True
        idle "v071/topview.png"
        hover "v071/topview.png"
        action Jump ("IvankaHouseTopSlow") 
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("MelaniaHouseSwitch") 
 
label IvankaHouseFast:
if ivankadeep:
    mc "Gonna POUND that presidential-family fuckhole HARDER and FASTER!"
if ivankadeep == False:
    mc "Am I DEEP enough inside your pussy Ivanka?"
    iv "Oooh, YES! But go faster please, fuck me HARD, make me CUM!"
    $ ivankadeep = True
scene whdoggyivankabackground
show ivankawhfuckfast
call screen ivankawhfuckfast01
screen ivankawhfuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("IvankaHouseEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("IvankaHouseSlow")
    imagebutton:
        focus_mask True
        idle "v071/topview.png"
        hover "v071/topview.png"
        action Jump ("IvankaHouseTopFast") 
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("MelaniaHouseSwitch") 

label IvankaHouseTopSlow:
scene whdoggyivankatopbackground
show ivankatopwhfuckslow
call screen ivankawhfucktopslow01
screen ivankawhfucktopslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("IvankaHouseEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("IvankaHouseTopFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("IvankaHouseSlow") 
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("MelaniaHouseSwitch") 

label IvankaHouseTopFast:
if ivankadeep:
    mc "Gonna POUND that presidential-family fuckhole HARDER and FASTER!"
if ivankadeep == False:
    mc "Am I DEEP enough inside your pussy Ivanka?"
    iv "Oooh, YES! But go faster please, fuck me HARD, make me CUM!"
    $ ivankadeep = True
scene whdoggyivankatopbackground
show ivankatopwhfuckfast
call screen ivankawhfucktopfast01
screen ivankawhfucktopfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("IvankaHouseEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("IvankaHouseTopSlow")
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("IvankaHouseFast") 
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("MelaniaHouseSwitch") 

label IvankaHouseEnd:
iv "Are you going to give me your fat load [name]?"
mc "* puff *  You want it? BEG FOR IT!"
iv "Ooohh, please, PLEASE, FLOOD MY FILTHY HOLE, IT'S YOURS!"
stop music
play music "Sounds/splooge02.mp3"
scene whdoggyivankabackground
show whivankacum01
with dissolve
mc "NUTTING INSIDE IVANKA TRUMPF, RHAAAA!"
window hide
with fastflash
iv "Uuuh, AAAAH, I'm coming too!"
stop music
scene whdoggyivankatopbackground
show whivankacum02
mc "There's MORE for you Ivanka, AAAAH!"
window hide
with fastflash
iv "Give it ALL to me, STALLION!"
stop music
scene whivankacumbackground blurred
show whivankacum03
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Take those shots on your amazon body, AAAH"
window hide
with fastflash
iv "CLAIM ME WITH YOUR SPERM, LIKE A TRUE ALPHA-MALE!"
play sound "Sounds/panting.mp3"
me "What about me? I'm the FIRST LADY and I should get priority for your SPECIAL PIZZA SAUCE!"
$ ivankaload = True
if melaniaload:
    mc "Then come and have a taste yourself Melania..."
    iv "And I'll lick the cream off YOUR body too!"
    jump WhbothfuckEnd
if melaniaload == False:
    mc "Don't you worry, I've got enough cum left for YOUR PUSSY!"
    iv "Please, fuck me, I'm dying to feel that GIANT shaft STRETCHING my hole..."
    jump IvankaHouseFuck

label MelaniaHouseSwitch:
mc "Time to switch girls, this cock needs more than one pussy to make it come. Spread your legs wide open Melania!"
jump MelaniaHouseFuckb

label WhbothfuckEnd:
scene whbothbackground blurred
show whbothend01
with dissolve
play sound "Sounds/lick.mp3"
mc "Oh fuck, watching you ladies going at each other is getting me HARD AGAIN!"
scene whbothbackgroundzoom
show whbothend02
with dissolve
label FinalShowdown:
play music "Sounds/footsteps.mp3"
me "Oh shit, I hear Donnie's footsteps. Quick, let's get dressed!"
stop music
scene ovaloffice02
show trumpfoval01b with moveinright
play sound "v10/whatthehell.mp3"
tr "What the hell is going on here? This place smells... funny."
window hide
show melaniaoval05 at farleft with moveinleft
me "I can explain Donald..."
hide trumpfoval01b
show trumpfoval09b at centerleft
with fastdissolve
tr "What's this? Is it some new skin lotion? Let me taste it, it smells funny..."
hide trumpfoval09b
hide melaniaoval05
show melaniaoval07 at farleft
show trumpfoval09b at centerleft
with fastdissolve
me "Donald, it's not what you th..."
hide trumpfoval09b
show trumpfoval10b
with fastdissolve
play sound "Sounds/slurp.mp3"
tr "That's some good stuff, I want some more."
mc "Finally, we meet."
play sound "Sounds/dundun.mp3"
$ renpy.pause(1.0, hard=True)
hide trumpfoval10b
hide melaniaoval07
show melaniaoval08 at farleft
show trumpfoval04b
with dissolve
tr "What's this noise? And who the hell are you?"
mc "I'm the HERO who's going to kick you out of this White House and take your place, that's who!"
hide trumpfoval04b
show trumpfoval05b
with fastdissolve
tr "Pfff. What makes you think you I would let you do that?"
play sound "v10/ridiculous.mp3"
$ renpy.pause(1.0, hard=True)
mc "Because the patrons... I mean people, want ME, the HERO, to beat you!"
hide trumpfoval05b
show trumpfoval08b
with fastdissolve
tr "Nobody wants a loser in the White House. And everyone wants a big-titted hot First Lady. I have a beautiful wife, Melanie, she's not here right now, but she's got HUGE..."
hide melaniaoval08
show melaniaoval06 at farleft
with fastdissolve
me "I AM here! And my name is MELANIA! I so much want a divorce... Damn that prenup..."
window hide
hide melaniaoval06 with moveoutleft
tr "So that makes me bigly desirable as Prez..."
window hide
show totalendgame at postotal
show trumpfplus at postrumpf01 with fastdissolve
hide trumpfplus at postrumpf01 with fastdissolve
show trumpfplus at postrumpf01 with fastdissolve
hide trumpfplus at postrumpf01 with fastdissolve
play sound "Sounds/faction.mp3"
show trumpfplus at postrumpf01 with fastdissolve
$ trumpftotal += 1
if tomarried:
    mc "Well, I'm married too for your information. And yeah, she's got big tits. And a DEEP pussy."
    window hide
    show mcplus at posmc01 with fastdissolve
    hide mcplus at posmc01 with fastdissolve
    show mcplus at posmc01 with fastdissolve
    hide mcplus at posmc01 with fastdissolve
    play sound "Sounds/faction.mp3"
    show mcplus at posmc01 with fastdissolve
    $ mctotal += 1
    hide trumpfoval08b
    show trumpfoval05b
    with fastdissolve    
    tr "I'd like to meet her. And grab her by that deep pus...."
    mc "Don't even THINK about it, old man!"
    play sound "v10/sueher.mp3"
    $ renpy.pause(2.0, hard=True)    
if tomarried == False:
    mc "Err... Well, never mind that, it's not important."
    hide trumpfoval08b
    show trumpfoval05b
    with fastdissolve
    play sound "v10/lookatthisguy.mp3"
    tr "It's SUPER important. SO you get NULL POINT. LOSER!"

hide trumpfoval05b
show trumpfoval07b
with fastdissolve
tr "And children. Beautiful children. A president needs to have lots of children. To create a dynasty. Americans love that kind of stuff."
hide trumpfoval07b
show trumpfoval08b
with fastdissolve
tr "I have... Four. Ivanka, Junior, John Barron..."
me "Just Barron, you moron!"
hide trumpfoval08b
show trumpfoval07b
with fastdissolve
tr "And that other girl."
play sound "v10/shesaslob.mp3"
$ renpy.pause(2.0, hard=True)
iv "What about Eric, daddy?"
hide trumpfoval07b
show trumpfoval06b
with fastdissolve
tr "Who?"
iv "Eric. Your son. My brother. The one with the huge teeth."
hide trumpfoval06b
show trumpfoval04b
with fastdissolve
tr "I have a son called Eric? Who gave him such a stupid name?"
mc "Wow, you can't even remember how many children you have..."
hide trumpfoval04b
show trumpfoval08b
with fastdissolve
tr "So I have FIVE children then. Man, woman, camera, TV, Eric. See, I CAN remember. How many do you have?"
play sound "v10/reallysmart.mp3"
mc "I have [mcchildren]."
if mcchildren <= 4:
    hide trumpfoval08b
    show trumpfoval02b
    with fastdissolve    
    play sound "v10/lookatthisguy.mp3"
    tr "So less than me. LOSER!"
    if trumpftotal == 1:
        window hide
        show trumpfplus02 at postrumpf02 with fastdissolve
        hide trumpfplus02 at postrumpf02 with fastdissolve
        show trumpfplus02 at postrumpf02 with fastdissolve
        hide trumpfplus02 at postrumpf02 with fastdissolve
        play sound "Sounds/faction.mp3"
        show trumpfplus02 at postrumpf02 with fastdissolve
        $ trumpftotal += 1
    if trumpftotal == 0:
        window hide
        show trumpfplus at postrumpf01 with fastdissolve
        hide trumpfplus at postrumpf01 with fastdissolve
        show trumpfplus at postrumpf01 with fastdissolve
        hide trumpfplus at postrumpf01 with fastdissolve
        play sound "Sounds/faction.mp3"
        show trumpfplus at postrumpf01 with fastdissolve
        $ trumpftotal += 1
    hide trumpfoval02b
    show trumpfoval05b
    with fastdissolve    
    tr "Not to mention, you have no leverage on me."
if mcchildren == 5:
    hide trumpfoval08b
    show trumpfoval06b
    with fastdissolve    
    tr "Same as me. It's a tie then..."
    play sound "v10/dontlikethat.mp3"
    hide trumpfoval06b
    show trumpfoval05b
    with fastdissolve
    tr "Still, you have no leverage on me!"
if mcchildren >= 6:
    mc "SO MORE than you. I would therefore be MORE POPULAR than you as president."
    hide trumpfoval08b
    show trumpfoval01b
    with fastdissolve
    if mctotal == 1:
        window hide
        show mcplus02 at posmc02 with fastdissolve
        hide mcplus02 at posmc02 with fastdissolve
        show mcplus02 at posmc02 with fastdissolve
        hide mcplus02 at posmc02 with fastdissolve
        play sound "Sounds/faction.mp3"
        show mcplus02 at posmc02 with fastdissolve
        $ mctotal += 1
    if mctotal == 0:
        window hide
        show mcplus at posmc01 with fastdissolve
        hide mcplus at posmc01 with fastdissolve
        show mcplus at posmc01 with fastdissolve
        hide mcplus at posmc01 with fastdissolve
        play sound "Sounds/faction.mp3"
        show mcplus at posmc01 with fastdissolve
        $ mctotal += 1
    hide trumpfoval01b
    show trumpfoval05b
    with fastdissolve
    tr "Still, you have no leverage on me!"

if seenpeetape:
    mc "Oh I think I have... You see, I own the pee-pee tape."
    hide trumpfoval05b
    show trumpfoval01b
    with fastdissolve    
    tr "What pee-pee tape?"
    mc "The one where you're getting pissed on by some Russian hookers and then we can see you pulling out your..."
    play sound "v10/notaniceperson.mp3"
    hide trumpfoval01b
    show trumpfoval04b
    with fastdissolve
    tr "Alright, alright, no need to go into such nasty details. Good thing Melanie isn't here."
    me "I AM here! And my name is STILL Melani-A!"
    if mctotal == 2:
        window hide
        show mcplus03 at posmc03 with fastdissolve
        hide mcplus03 at posmc03 with fastdissolve
        show mcplus03 at posmc03 with fastdissolve
        hide mcplus03 at posmc03 with fastdissolve
        play sound "Sounds/faction.mp3"
        show mcplus03 at posmc03 with fastdissolve
        $ mctotal += 1
    if mctotal == 1:
        window hide
        show mcplus02 at posmc02 with fastdissolve
        hide mcplus02 at posmc02 with fastdissolve
        show mcplus02 at posmc02 with fastdissolve
        hide mcplus02 at posmc02 with fastdissolve
        play sound "Sounds/faction.mp3"
        show mcplus02 at posmc02 with fastdissolve
        $ mctotal += 1
    if mctotal == 0:
        window hide
        show mcplus at posmc01 with fastdissolve
        hide mcplus at posmc01 with fastdissolve
        show mcplus at posmc01 with fastdissolve
        hide mcplus at posmc01 with fastdissolve
        play sound "Sounds/faction.mp3"
        show mcplus at posmc01 with fastdissolve
        $ mctotal += 1
        
if seenpeetape == False:
    mc "Well... Maybe not, but who cares? I don't need no stinkin' leverage, I'm the HERO here!"
    hide trumpfoval05b
    show trumpfoval04b
    with fastdissolve    
    if trumpftotal == 2:
        window hide
        show trumpfplus03 at postrumpf03 with fastdissolve
        hide trumpfplus03 at postrumpf03 with fastdissolve
        show trumpfplus03 at postrumpf03 with fastdissolve
        hide trumpfplus03 at postrumpf03 with fastdissolve
        play sound "Sounds/faction.mp3"
        show trumpfplus03 at postrumpf03 with fastdissolve
        $ trumpftotal += 1
    if trumpftotal == 1:
        window hide
        show trumpfplus02 at postrumpf02 with fastdissolve
        hide trumpfplus02 at postrumpf02 with fastdissolve
        show trumpfplus02 at postrumpf02 with fastdissolve
        hide trumpfplus02 at postrumpf02 with fastdissolve
        play sound "Sounds/faction.mp3"
        show trumpfplus02 at postrumpf02 with fastdissolve
        $ trumpftotal += 1
    if trumpftotal == 0:
        window hide
        show trumpfplus at postrumpf01 with fastdissolve
        hide trumpfplus at postrumpf01 with fastdissolve
        show trumpfplus at postrumpf01 with fastdissolve
        hide trumpfplus at postrumpf01 with fastdissolve
        play sound "Sounds/faction.mp3"
        show trumpfplus at postrumpf01 with fastdissolve
        $ trumpftotal += 1
    play sound "v10/lookatthisguy.mp3"
    tr "Looks like you DO need leverage after all..."

hide trumpfoval04b
show trumpfoval07b
with fastdissolve
tr "How much taxes have you paid in your ENTIRE life? Only LOSERS pay taxes. Like the dev, who pays 20\% of his Patreon income to the taxman. And losers can't be president!"
mc "Well, zero dollar to be honest. I was a minor when you destroyed the world and I'm only 18 now. Allegedly."
hide trumpfoval07b
show trumpfoval06b
with fastdissolve
tr "Ah, so the same as me then. That's a tie. But how good are your ratings?"
hide trumpfoval06b
show trumpfoval08b
with fastdissolve
tr "A President needs great ratings, I have the BEST ratings, BILLIONS of people watch my YuckTube videos of me texting super-important stuff! You can't beat THAT!"
mc "YES I CAN! I have literally ZILLIONS of followers throughout the galaxy watching MY PORN VIDEOS. Of me fucking hot big-titted babes with my HUGE cock!"
hide trumpfoval08b
show trumpfoval01b
with fastdissolve
if mctotal == 3:
    window hide
    show mcplus04 at posmc04 with fastdissolve
    hide mcplus04 at posmc04 with fastdissolve
    show mcplus04 at posmc04 with fastdissolve
    hide mcplus04 at posmc04 with fastdissolve
    play sound "Sounds/faction.mp3"
    show mcplus04 at posmc04 with fastdissolve
    $ mctotal += 1
if mctotal == 2:
    window hide
    show mcplus03 at posmc03 with fastdissolve
    hide mcplus03 at posmc03 with fastdissolve
    show mcplus03 at posmc03 with fastdissolve
    hide mcplus03 at posmc03 with fastdissolve
    play sound "Sounds/faction.mp3"
    show mcplus03 at posmc03 with fastdissolve
    $ mctotal += 1
if mctotal == 1:
    window hide
    show mcplus02 at posmc02 with fastdissolve
    hide mcplus02 at posmc02 with fastdissolve
    show mcplus02 at posmc02 with fastdissolve
    hide mcplus02 at posmc02 with fastdissolve
    play sound "Sounds/faction.mp3"
    show mcplus02 at posmc02 with fastdissolve
    $ mctotal += 1
if mctotal == 0:
    window hide
    show mcplus at posmc01 with fastdissolve
    hide mcplus at posmc01 with fastdissolve
    show mcplus at posmc01 with fastdissolve
    hide mcplus at posmc01 with fastdissolve
    play sound "Sounds/faction.mp3"
    show mcplus at posmc01 with fastdissolve
    $ mctotal += 1
$ renpy.pause(2.0, hard=True)
label Test:
if mctotal >= (trumpftotal+1):
    scene ovaloffice02
    show trumpfoval01b
    with dissolve
    mc "And I heard YOU had a TINY one..."
    me "Oh, that's DEFINITELY true."
    hide trumpfoval01b
    show trumpfoval08b
    with fastdissolve
    play sound "v10/wrong.mp3"
    tr "What? WRONG, WRONG! Look at my hands, they're YUGE! Just like my thingie!"
    mc "You ain't fooling nobody anymore, old man. Time for you to get KICKED OUT OF THE SUPREME WHITE HOUSE!"
    play sound "v10/dontlikethat.mp3"
    hide trumpfoval08b
    show trumpfoval04b
    with fastdissolve
    tr "This game is RIGGED! I demand an audit by Cyber-Ninjas!"
    show ivankaoval06 at farright with moveinright
    iv "Sorry, daddy, but [name] here is just... the HERO president we need!"
    show melaniaoval09  at farleft with moveinleft
    me "And hopefully, he'll cancel my prenup by executive order!"
    play sound "v10/people.mp3"
    $ renpy.pause(2.0, hard=True)
    mc "Hold him still ladies..."
    hide trumpfoval04b
    hide melaniaoval09
    hide ivankaoval06
    show trumpfend01
    with dissolve
    mc "Kick the orange man-baby!"
    play sound "v10/babykick.mp3"
    $ renpy.pause(3.0, hard=True)    
    show trumpfendleg01 with fastdissolve
    play sound "Sounds/punch.mp3"
    hide trumpfend01
    hide trumpfendleg01
    show trumpfend02
    show trumpfendleg02
    with dissolve
    play sound "v10/glass.mp3"
    scene ovaloffice02b
    with dissolve
    show ovaloffice02c with dissolve
    mc "Now I'm the PREZ! So let's make some changes in decoration to this dusty Oval Office..."    
    jump GameWin
if mctotal <= trumpftotal:
    label EndLose:
    scene ovaloffice02
    show trumpfoval05b
    with dissolve
    tr "Well, I can grab any woman I want by the pussy. They just let me do it cos I'm sssooo popular."
    mc "And you pay them."
    hide trumpfoval05b
    show trumpfoval07b
    with fastdissolve
    tr "And I'll pay Ivanka and Melania to KICK YOU OUT RIGHT NOW!"
    mc "They won't do it, they know I'm the HER..."
    window hide
    show ivankaoval07 at farright03 with moveinright
    iv "Of course, Daddy! You're just the BEST President EVER!"
    show melaniaoval10  at farleft with moveinleft
    me "I suppose a pre-nup is a pre-nup. Goodbye forever, [name]."
    play sound "v10/lookatthisguy.mp3"
    hide trumpfoval07b
    show trumpfoval05b
    with fastdissolve
    mc "Hey, what's going on here? I was supposed to WIN this game!"
    hide trumpfoval05b
    show trumpfoval02b
    with fastdissolve
    tr "Loser, loser! I'm the Prez and you're just a LOSER!"
    play music "v10/loser.mp3"
    hide trumpfoval02b
    show trumpfoval03b
    with fastdissolve
    $ renpy.pause(.5, hard=True)
    hide trumpfoval03b
    show trumpfoval02b
    with fastdissolve
    $ renpy.pause(.5, hard=True)
    hide trumpfoval02b
    show trumpfoval03b
    with fastdissolve
    $ renpy.pause(.5, hard=True)
    hide trumpfoval03b
    show trumpfoval02b
    with fastdissolve
    $ renpy.pause(.5, hard=True)
    hide trumpfoval02b
    show trumpfoval03b
    with fastdissolve
    $ renpy.pause(.5, hard=True)
    hide trumpfoval03b
    show trumpfoval02b
    with fastdissolve
    $ renpy.pause(.5, hard=True)
    hide trumpfoval02b
    show trumpfoval03b
    with fastdissolve
    $ renpy.pause(.5, hard=True)
    hide trumpfoval03b
    show trumpfoval02b
    with fastdissolve
    $ renpy.pause(.5, hard=True)
    hide trumpfoval02b
    show trumpfoval03b
    with fastdissolve
    $ renpy.pause(.5, hard=True)
    hide trumpfoval03b
    show trumpfoval02b
    stop music
    tr "Hey LOSER! I bet you're into findom, aren't you? Then go check that page, totally legit website, and give ALL YOUR MONEY to that guy to help make NEW AMERICA GREAT AGAIN!"
    call screen endcredits03
    screen endcredits03:
        modal True
        imagebutton idle "v10/epiclustpatreon.png" hover "v10/epiclustpatreon.png" xpos 1600 ypos 50 focus_mask True action OpenURL("https://www.patreon.com/epiclust")
        imagebutton idle "v10/epiclustpatreonnext.png" hover "v10/epiclustpatreonnext.png" xpos 1600 ypos 800 focus_mask True action Return
    play music "v10/loser.mp3"
    hide trumpfoval02b
    show trumpfoval03b
    with fastdissolve
    $ renpy.pause(.5, hard=True)
    hide trumpfoval03b
    show trumpfoval02b
    with fastdissolve
    $ renpy.pause(.5, hard=True)
    hide trumpfoval02b
    show trumpfoval03b
    with fastdissolve
    $ renpy.pause(.5, hard=True)
    hide trumpfoval03b
    show trumpfoval02b
    with fastdissolve
    $ renpy.pause(.5, hard=True)
    hide trumpfoval02b
    show trumpfoval03b
    with fastdissolve
    $ renpy.pause(.5, hard=True)
    hide trumpfoval03b
    show trumpfoval02b
    with fastdissolve
    stop music
    hide melaniaoval10
    hide ivankaoval07
    window hide
    show trumpfoval02b at farleft with move
    tr "You wanna know what's the next game you're going to lose to, LOSER?"
    hide trumpfoval02b
    show trumpfoval08b at left
    with fastdissolve    
    tr "Then check this out, it's going to be BIG! It will have the BEST ratings EVER!"
    window hide
    show superboy01 at centerright with moveinright
    sc "That's right, I'm the next HERO in the dev's next game! A SUPERHERO actually!"
    hide trumpfoval08b
    show trumpfoval05b at left
    with fastdissolve    
    tr "A superhero? I'm chosen by God, so I'm like a SUPER-GOD-HERO!"
    hide superboy01
    show superboy02 at centerright
    with dissolve
    sc "But you don't have a donkey-dick like mine..."
    hide trumpfoval05b
    hide superboy02
    show trumpfoval04b at left
    show superboy03 at centerright
    with dissolve
    play sound "Sounds/thud.mp3"
    tr "It looks deformed. Like, where's the big spotty mushroom-looking tip?"
    sc "My dick is normal in appearance. YOURS is the deformed one, Toady-boy..."
    hide superboy03
    show superboy04 at centerright
    with dissolve
    sc "So EVERYONE should join the dev's Patreon page and support the development of \"COCKHAM\". A game where I will FIGHT organized SEX CRIME in Cockham City with other * SEXY * superheroes."
    hide trumpfoval04b
    show trumpfoval06b at left
    with fastdissolve 
    tr "Ah yeah? Like who for example?"
    show captainmilf at farright03 with moveinright
    hide superboy04
    show superboy03 at centerright
    with dissolve
    sc "Like this lady, Captain MILF. She's my mo... I mean landlady."
    hide trumpfoval06b
    show trumpfoval01b at left
    with fastdissolve 
    tr "Damn, she's got bigger tits than Melanie. And she looks crisper than us for some reason..."
    hide trumpfoval01b
    show trumpfoval07b at left
    with fastdissolve 
    tr "OK, I'm sold. I'm already super-excited about the game and I will advertise it on my twatter account. Which was NOT suspended since I'm Prez-for-Life."
    sc "Thanks Mister Dictat..., I mean, President-For-Life!"
    hide trumpfoval07b
    hide superboy03
    hide captainmilf
    show captainmilf at centerright
    with dissolve
    window hide
    play music "v10/thisistheend.mp3"
    show screen endcredit01
    screen endcredit01:
        imagebutton idle "v10/epiclustpatreon.png" hover "v10/epiclustpatreon.png" xpos 1600 ypos 50 focus_mask True action OpenURL("https://www.patreon.com/epiclust")
    show endcredits at left:
        yalign 1.0
        linear 5.0 yalign 0.1
    $ renpy.pause(43.0, hard=True)
    return
        
label GameWin:
play channel1 "v10/ohyeah.mp3"
scene newovaloffice01
show mcwin01
with fade
mc "Fuck yeah!"
scene newovaloffice02
show mcwin02
with dissolve
mc "Before the FUCKING begins, my dev has instructed me to direct you to his Patreon page."
mc "If you're not yet a patron but enjoyed this now COMPLETED game, now is the time to join and leave a tip to show your appreciation."
hide mcwin02
show mcwin03
with fastdissolve
mc "So just click right THERE!..."
call screen endcredits
screen endcredits:
    modal True
    imagebutton idle "v10/epiclustpatreon.png" hover "v10/epiclustpatreon.png" xpos 1500 ypos 300 focus_mask True action OpenURL("https://www.patreon.com/epiclust")
    imagebutton idle "v10/epiclustpatreonnext.png" hover "v10/epiclustpatreonnext.png" xpos 1500 ypos 900 focus_mask True action Return
    
hide mcwin03
show mcwin04
with fastdissolve
mc "Now ladies, you're my Special SEX Advisors, so it's time to make the prez CUM!"
hide mcwin04
show mcwin05
with fastdissolve
play sound "Sounds/lick.mp3"
iv "Of course President [name]!"
me "We will make you cum as often as you like EVERY DAY from now on!"
stop music
play channel2 "Sounds/sucking.mp3"
scene melaniaivankablowbackground blurred
label MelaniaIvankaBlowSlow:
hide melaniaivankablowfast
show melaniaivankablowslow
call screen melaniaivankablowslow01
screen melaniaivankablowslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MelaniaIvankaBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MelaniaIvankaBlowFast") 

label MelaniaIvankaBlowFast:
hide melaniaivankablowslow
show melaniaivankablowfast
mc "You're getting my juices going, girls..."
me "We'll make them go FASTER then!"
call screen melaniaivankablowfast01
screen melaniaivankablowfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MelaniaIvankaBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MelaniaIvankaBlowSlow")

label MelaniaIvankaBlowEnd:
iv "He's tensing up! The Prez is about to BLOW!"
mc "He sure is..."
hide melaniaivankablowslow
hide melaniaivankablowfast
show melaniaivankablowcum01
with dissolve
me "It's bubbling at the tip..."
window hide
with fastflash
mc "AAAH! I'm about to blow a big..."
stop channel2
hide melaniaivankablowcum01
show melaniaivankablowcum02
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "...ONE! RHAAA!"
window hide
with fastflash
mc "Fuck yeah, blowing my nut in the Oval Office!!!!"
play sound "Sounds/moaning02.mp3"
hide melaniaivankablowcum02
show melaniaivankablowcum03
with dissolve
me "Look at him DOUSE us with his warm teenage spunk!"
window hide
with fastflash
iv "I've never seen such THICK, CREAMY cumshots EVER! We're getting CAKED in it!"
window hide
with fastflash
mc "There's plenty more where that came from, ladies! But I need some reserves for the next scene..."
scene newovaloffice01
show melaniaivankablowcum04
with dissolve
play sound "Sounds/kiss.mp3"
mc "And now, BRING ON THE GIRLS FOR THE FINAL ORGY!"
mc "Oh, and by the way guys, you can use BOTH hands to jack off like I do... No need to press any key for the following sequence... Except if you want to end it."
hide melaniaivankablowcum04

label EndFuck01:
show screen endall
screen endall:
    imagebutton idle "v10/endall.png" hover "v10/endall.png" xpos 1800 ypos 20 focus_mask True action Jump ("FutureGameEnd") 
$ endstart = True

label EndFuck:
scene newovaloffice01
$ drollnextWin=renpy.random.randint(1,24)
$ drollmcsetup=renpy.random.randint(1,3)
$ drolltrumpfsetup=renpy.random.randint(1,3)
$ drolltrumpfsex=renpy.random.randint(1,3)
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
if drollmcsetup == 1:
    show mcsetup01a
if drollmcsetup == 2:
    show mcsetup03
if drollmcsetup == 3:
    show mcsetup04
if endstart:
    hide mcsetup04
    hide mcsetup03
    hide mcsetup01a
    show mcsetup01b
    $ endstart = False

if drollWin == drollnextWin:
    jump EndFuck
if drollnextWin == 1:
    $ drollWin = drollnextWin
    jump Winnancyfuck
if drollnextWin == 2:
    $ drollWin = drollnextWin
    jump Winlenafuck
if drollnextWin == 3:
    $ drollWin = drollnextWin
    jump Winamyfuck
if drollnextWin == 4:
    $ drollWin = drollnextWin
    jump Wincyrlfuck
if drollnextWin == 5:
    $ drollWin = drollnextWin
    jump Winsukifuck
if drollnextWin == 6:
    $ drollWin = drollnextWin
    jump Winmichikofuck
if drollnextWin == 7:
    $ drollWin = drollnextWin
    jump Winbarbarafuck
if drollnextWin == 8:
    $ drollWin = drollnextWin
    jump Winangiefuck
if drollnextWin == 9:
    $ drollWin = drollnextWin
    jump Winaylafuck
if drollnextWin == 10:
    $ drollWin = drollnextWin
    jump Winbellafuck
if drollnextWin == 11:
    $ drollWin = drollnextWin
    jump Winpennyfuck
if drollnextWin == 12:
    $ drollWin = drollnextWin
    jump Wintarafuck
if drollnextWin == 13:
    $ drollWin = drollnextWin
    jump Windebrafuck
if drollnextWin == 14:
    $ drollWin = drollnextWin
    jump Winrubyfuck
if drollnextWin == 15:
    $ drollWin = drollnextWin
    jump Winlauriefuck
if drollnextWin == 16:
    $ drollWin = drollnextWin
    jump Winmarniefuck
if drollnextWin == 17:
    $ drollWin = drollnextWin
    jump Winzarafuck
if drollnextWin == 18:
    $ drollWin = drollnextWin
    jump Winclarafuck
if drollnextWin == 19:
    $ drollWin = drollnextWin
    jump Wingwenfuck
if drollnextWin == 20:
    $ drollWin = drollnextWin
    jump Winrachelfuck
if drollnextWin == 21 and tomarried:
    $ drollWin = drollnextWin
    jump Wintaylorfuck
if drollnextWin == 21 and tomarried == False:
    jump EndFuck
if drollnextWin == 22 and metwi:
    jump Winwidowfuck
if drollnextWin == 22 and metwi == False:
    jump EndFuck
if drollnextWin == 23 and seenwendy:
    jump Winwendyfuck
if drollnextWin == 23 and seenwendy == False:
    jump EndFuck
if drollnextWin == 24 and metqu:
    jump Winpaulettefuck
if drollnextWin == 24 and metqu == False:
    jump EndFuck

label Winnancyfuck:
show orgynancysetup at farleft02
mc "FUCK YEAH, NANCY! {w=1.0}{nw}"
window hide
show orgynancysetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgynancysetup at left
with dissolve
mo "Only the BEST for that MONSTERCOCK, sweetie pie... {w=2.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex01.mp3"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-705
        show winnancyfuck
    if drolltrumpfsex == 2:
        show winnancyfuck
        show winmelaniaivanka02-705
    if drolltrumpfsex == 3:
        show winnancyfuck
        show winmelaniaivanka03-705
    $ renpy.pause(.705, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-705
    show orgynancycum
if drolltrumpfsex == 2:
    show orgynancycum
    show winmelaniaivanka02-705
if drolltrumpfsex == 3:
    show orgynancycum
    show winmelaniaivanka03-705
with dissolve
mc "CUMMING IN YOUR ASS, AAAH! {w=1.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
mo "Oh God, my dear boy, you're PUMPING ME FULL, AAAH! {w=2.0}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgynancyleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgynancyleave with moveoutright
jump EndFuck        

label Winlenafuck:
show orgylenasetup at farleft02
mc "Lena! I'm the BIG chief now, so come over here... {w=1.5}{nw}"
window hide
show orgylenasetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgylenasetup at left
with dissolve
le "This cock DESERVES to be worshipped... {w=1.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex01.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-79
        show winlenafuck
    if drolltrumpfsex == 2:
        show winlenafuck
        show winmelaniaivanka02-79
    if drolltrumpfsex == 3:
        show winlenafuck
        show winmelaniaivanka03-79
    $ renpy.pause(.79, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-79
    show orgylenacum
if drolltrumpfsex == 2:
    show orgylenacum
    show winmelaniaivanka02-79
if drolltrumpfsex == 3:
    show orgylenacum
    show winmelaniaivanka03-79
with dissolve
mc "And now worship THAT, my FAT LOAD in your pussy, AAAH! {w=2.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
le "Mmmmh, you came sssoo much, that was a PRESIDENTIAL LOAD [name]! {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgylenaleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgylenaleave with moveoutright
jump EndFuck        

label Winamyfuck:
show orgyamysetup at farleft02
mc "BOOYAH, It's muscle girl Amy! {w=1.5}{nw}"
window hide
show orgyamysetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgyamysetup at left
with dissolve
am "And my ass is going to deal with that HUGE MUSCLE of yours! {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex01.mp3"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-705
        show winamyfuck
    if drolltrumpfsex == 2:
        show winamyfuck
        show winmelaniaivanka02-705
    if drolltrumpfsex == 3:
        show winamyfuck
        show winmelaniaivanka03-705
    $ renpy.pause(.705, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-705
    show orgyamycum
if drolltrumpfsex == 2:
    show orgyamycum
    show winmelaniaivanka02-705
if drolltrumpfsex == 3:
    show orgyamycum
    show winmelaniaivanka03-705
with dissolve
mc "YOUR TIGHT ASS IS MAKING ME NU-UU-UUT! {w=1.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
am "FILL IT UP, I WANT ALL THAT CUM! {w=2.0}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgyamyleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgyamyleave with moveoutright
jump EndFuck        

label Wincyrlfuck:
show orgycyrlsetup at farleft02
mc "SEXY CYBORG CYRL! YEAH! {w=1.0}{nw}"
window hide
show orgycyrlsetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgycyrlsetup at left
with dissolve
cy "Activate mouth enlargement. MAXIMAL SIZE FOR THE PRESIDENTIAL DONKEY-DICK! {w=3.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/blowjob.ogg"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-705
        show wincyrlfuck
    if drolltrumpfsex == 2:
        show wincyrlfuck
        show winmelaniaivanka02-705
    if drolltrumpfsex == 3:
        show wincyrlfuck
        show winmelaniaivanka03-705
    $ renpy.pause(.705, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-705
    show orgycyrlcum
if drolltrumpfsex == 2:
    show orgycyrlcum
    show winmelaniaivanka02-705
if drolltrumpfsex == 3:
    show orgycyrlcum
    show winmelaniaivanka03-705
with dissolve
mc "BLOWING MY SEED INSIDE A ROBOT MOUTH, RHAAA! {w=2.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
cy "Fortunately, my stomach has a CUM CAPACITY of over a GALLON! {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgycyrlleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgycyrlleave with moveoutright
jump EndFuck   

label Winsukifuck:
show orgysukisetup at farleft02
mc "Suki! I'll show you I'm an inclusive prez... {w=1.5}{nw}"
window hide
show orgysukisetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgysukisetup at left
with dissolve
su "By inserting your GIANT TEENAGE COCK inside of me I presume? {w=2.5}{nw}"
mc "CORRECTOMUNDO! {w=1.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex01.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-79
        show winsukifuck
    if drolltrumpfsex == 2:
        show winsukifuck
        show winmelaniaivanka02-79
    if drolltrumpfsex == 3:
        show winsukifuck
        show winmelaniaivanka03-79
    $ renpy.pause(.79, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-79
    show orgysukicum
if drolltrumpfsex == 2:
    show orgysukicum
    show winmelaniaivanka02-79
if drolltrumpfsex == 3:
    show orgysukicum
    show winmelaniaivanka03-79
with dissolve
mc "I've got a BIG LOAD FOR YOU SUKI, AAAH! {w=2.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
su "It sure is HUGE, I can FEEL IT! {w=1.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgysukileave at centerright
with dissolve
mc "I NEED MORE SEX, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgysukileave with moveoutright
jump EndFuck        

label Winmichikofuck:
show orgymichikosetup at farleft02
mc "Big-Busted Asian babe Michiko! {w=1.5}{nw}"
window hide
show orgymichikosetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgymichikosetup at left
with dissolve
mi "And my Asian ASS demands some ANAL POUNDING! {w=2.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex01.mp3"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-705
        show winmichikofuck
    if drolltrumpfsex == 2:
        show winmichikofuck
        show winmelaniaivanka02-705
    if drolltrumpfsex == 3:
        show winmichikofuck
        show winmelaniaivanka03-705
    $ renpy.pause(.705, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-705
    show orgymichikocum
if drolltrumpfsex == 2:
    show orgymichikocum
    show winmelaniaivanka02-705
if drolltrumpfsex == 3:
    show orgymichikocum
    show winmelaniaivanka03-705
with dissolve
mc "ONE FAT LOAD OF TEENAGE CREAM COMING YOUR WAY, RHAAA! {w=2.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
mi "You're so BRUTAL when you UNLOAD YOUR SEED IN ME, AAAH! {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgymichikoleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgymichikoleave with moveoutright
jump EndFuck        

label Winbarbarafuck:
show orgybarbarasetup at farleft02
mc "Barbara! It's recess so come over here... {w=1.0}{nw}"
window hide
show orgybarbarasetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgybarbarasetup at left
with dissolve
ba "And recess is for PLAYING and FUN! {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex01.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-95
        show winbarbarafuck
    if drolltrumpfsex == 2:
        show winbarbarafuck
        show winmelaniaivanka02-95
    if drolltrumpfsex == 3:
        show winbarbarafuck
        show winmelaniaivanka03-95
    $ renpy.pause(.95, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-95
    show orgybarbaracum
if drolltrumpfsex == 2:
    show orgybarbaracum
    show winmelaniaivanka02-95
if drolltrumpfsex == 3:
    show orgybarbaracum
    show winmelaniaivanka03-95
with dissolve
mc "Here, take that and have fun with my MONSTERLOAD, RHAAA! {w=1.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
ba "I'll keep it to snack on later on, OOOH! {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgybarbaraleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgybarbaraleave with moveoutright
jump EndFuck        

label Winangiefuck:
show orgyangiesetup at farleft02
mc "ANGIE! come here sweetie... {w=1.0}{nw}"
window hide
show orgyangiesetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgyangiesetup at left
with dissolve
an "I've been waiting for a long time to FEEL that HUGE COCK again! {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex01.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-95
        show winangiefuck
    if drolltrumpfsex == 2:
        show winangiefuck
        show winmelaniaivanka02-95
    if drolltrumpfsex == 3:
        show winangiefuck
        show winmelaniaivanka03-95
    $ renpy.pause(.95, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-95
    show orgyangiecum
if drolltrumpfsex == 2:
    show orgyangiecum
    show winmelaniaivanka02-95
if drolltrumpfsex == 3:
    show orgyangiecum
    show winmelaniaivanka03-95
with dissolve
mc "I'm gonna DROWN your womb, RHAAA!{w=1.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
an "I can feel your giant JOYSTICK convulsing inside me, AAAH! {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgyangieleave at centerright
with dissolve
mc "I NEED MORE SEX, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgyangieleave with moveoutright
jump EndFuck        

label Winaylafuck:
show orgyaylasetup at farleft02
mc "Ayla! Little girl, deep pussy... {w=1.0}{nw}"
window hide
show orgyaylasetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgyaylasetup at left
with dissolve
ay "I'm gonna show you exactly how DEEP it is... {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex02.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-95
        show winaylafuck
    if drolltrumpfsex == 2:
        show winaylafuck
        show winmelaniaivanka02-95
    if drolltrumpfsex == 3:
        show winaylafuck
        show winmelaniaivanka03-95
    $ renpy.pause(.95, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-95
    show orgyaylacum
if drolltrumpfsex == 2:
    show orgyaylacum
    show winmelaniaivanka02-95
if drolltrumpfsex == 3:
    show orgyaylacum
    show winmelaniaivanka03-95
with dissolve
mc "I'm gonna FILL your tiny womb with my SPUNK, RHAAA!{w=2.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
ay "And my SUPER-DEEP pussy can TAKE IT, AAAH {w=2.0}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgyaylaleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgyaylaleave with moveoutright
jump EndFuck        

label Winbellafuck:
show orgybellasetup at farleft02
mc "Fuck yeah, Bella! {w=1.0}{nw}"
window hide
show orgybellasetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgybellasetup at left
with dissolve
be "May my pussy give much pleasure to that HOLY GIANT PRESIDENTIAL PHALLUS! {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex02.mp3"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-6
        show winbellafuck
    if drolltrumpfsex == 2:
        show winbellafuck
        show winmelaniaivanka02-6
    if drolltrumpfsex == 3:
        show winbellafuck
        show winmelaniaivanka03-6
    $ renpy.pause(.6, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-6
    show orgybellacum
if drolltrumpfsex == 2:
    show orgybellacum
    show winmelaniaivanka02-6
if drolltrumpfsex == 3:
    show orgybellacum
    show winmelaniaivanka03-6
with dissolve
mc "Take my MONSTER CUMSHOTS Bella, RHAAA!{w=1.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
be "PRAISE OUR CUM-LADEN PREZ! AAAAH!{w=1.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgybellaleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgybellaleave with moveoutright
jump EndFuck        

label Winpennyfuck:
show orgypennysetup at farleft02
mc "One of my FAVORITE scouts, PENNY! {w=1.5}{nw}"
window hide
show orgypennysetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgypennysetup at left
with dissolve
pe "And I'll show you how my TITS definitely ARE your FAVORITES! {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/wank.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-74
        show winpennyfuck
    if drolltrumpfsex == 2:
        show winpennyfuck
        show winmelaniaivanka02-74
    if drolltrumpfsex == 3:
        show winpennyfuck
        show winmelaniaivanka03-74
    $ renpy.pause(.74, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-74
    show orgypennycum
if drolltrumpfsex == 2:
    show orgypennycum
    show winmelaniaivanka02-74
if drolltrumpfsex == 3:
    show orgypennycum
    show winmelaniaivanka03-74
with dissolve
mc "Your funbags are making me BL-OOO-OOOW! AAH!{w=2.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
pe "Let it RAIN, President [name]! {w=1.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgypennyleave at centerright
mc "I NEED MORE SEX, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgypennyleave with moveoutright
jump EndFuck 

label Wintarafuck:
show orgytarasetup at farleft02
mc "Tara?! I thought you were a lesbian. {w=1.5}{nw}"
window hide
show orgytarasetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgytarasetup at left
with dissolve
ta "I'm a DEEP STATE lez and you're the DEEP STATE Prez! So probe my ass REAL DEEP! {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex02.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-74
        show wintarafuck
    if drolltrumpfsex == 2:
        show wintarafuck
        show winmelaniaivanka02-74
    if drolltrumpfsex == 3:
        show wintarafuck
        show winmelaniaivanka03-74
    $ renpy.pause(.74, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-74
    show orgytaracum
if drolltrumpfsex == 2:
    show orgytaracum
    show winmelaniaivanka02-74
if drolltrumpfsex == 3:
    show orgytaracum
    show winmelaniaivanka03-74
with dissolve
mc "Can a dildo do that, CUM MASSIVE ROPES OF SEMEN INSIDE YOU, RHAAA!{w=2.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
ta "I'm liking this, I might turn STRAIGHT, AAAHH!{w=2.0}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgytaraleave at centerright
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgytaraleave with moveoutright
jump EndFuck        

label Windebrafuck:
show orgydebrasetup at farleft02
mc "Ooh yeah, Debra! {w=1.0}{nw}"
window hide
show orgydebrasetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgydebrasetup at left
with dissolve
de "I can't wait to get fucked by your MONSTERCOCK!{w=2.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex02.mp3"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-6
        show windebrafuck
    if drolltrumpfsex == 2:
        show windebrafuck
        show winmelaniaivanka02-6
    if drolltrumpfsex == 3:
        show windebrafuck
        show winmelaniaivanka03-6
    $ renpy.pause(.705, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-6
    show orgydebracum
if drolltrumpfsex == 2:
    show orgydebracum
    show winmelaniaivanka02-6
if drolltrumpfsex == 3:
    show orgydebracum
    show winmelaniaivanka03-6
with dissolve
mc "Take my MONSTER CUMSHOTS Debra, RHAAA! {w=1.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
de "FUCK, you're FILLING ME UP WITH SO MUCH CUM!{w=2.0}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgydebraleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgydebraleave with moveoutright
jump EndFuck        

label Winrubyfuck:
show orgyrubysetup at farleft02
mc "PUMPED-UP MUSCLE BABE RUBY, YEE-HAW! {w=2.0}{nw}"
window hide
show orgyrubysetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgyrubysetup at left
with dissolve
ru "And my TIT MUSCLES are ESPECIALLY pumped up. TO PUMP YOUR POLE! {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/wank.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-74
        show winrubyfuck
    if drolltrumpfsex == 2:
        show winrubyfuck
        show winmelaniaivanka02-74
    if drolltrumpfsex == 3:
        show winrubyfuck
        show winmelaniaivanka03-74
    $ renpy.pause(.74, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-74
    show orgyrubycum
if drolltrumpfsex == 2:
    show orgyrubycum
    show winmelaniaivanka02-74
if drolltrumpfsex == 3:
    show orgyrubycum
    show winmelaniaivanka03-74
with dissolve
mc "GODAMMIT, I'm BLOWING A MONSTER LOAD, AAAH! {w=2.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
ru "My tits did the JOB. The TITJOB! {w=1.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgyrubyleave at centerright
with dissolve
mc "I NEED MORE SEX, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgyrubyleave with moveoutright
jump EndFuck        

label Winlauriefuck:
show orgylauriesetup at farleft02
mc "Hey, LAURIE's coming for a PRESIDENTIAL SEX VISIT! {w=2.0}{nw}"
window hide
show orgylauriesetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgylauriesetup at left
with dissolve
la "And my tits are ready to SERVICE your MEATY POLE, President! {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/wank.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-74
        show winlauriefuck
    if drolltrumpfsex == 2:
        show winlauriefuck
        show winmelaniaivanka02-74
    if drolltrumpfsex == 3:
        show winlauriefuck
        show winmelaniaivanka03-74
    $ renpy.pause(.74, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-74
    show orgylauriecum
if drolltrumpfsex == 2:
    show orgylauriecum
    show winmelaniaivanka02-74
if drolltrumpfsex == 3:
    show orgylauriecum
    show winmelaniaivanka03-74
with dissolve
mc "You're servicing me so WELL, I'm NU-UUU-TTING BIG TIME!!! {w=2.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
la "I'm glad I could be of service to your PRESIDENTIAL SCEPTER! {w=2.0}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgylaurieleave at centerright
with dissolve
mc "I NEED MORE SEX, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgylaurieleave with moveoutright
jump EndFuck        

label Winmarniefuck:
show orgymarniesetup at farleft02
mc "WOO-HOO, Marnie! {w=1.0}{nw}"
window hide
show orgymarniesetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgymarniesetup at left
with dissolve
ma "I want you to POUND my pussy real GOOD, President [name]! {w=2.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex02.mp3"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-6
        show winmarniefuck
    if drolltrumpfsex == 2:
        show winmarniefuck
        show winmelaniaivanka02-6
    if drolltrumpfsex == 3:
        show winmarniefuck
        show winmelaniaivanka03-6
    $ renpy.pause(.6, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-6
    show orgymarniecum
if drolltrumpfsex == 2:
    show orgymarniecum
    show winmelaniaivanka02-6
if drolltrumpfsex == 3:
    show orgymarniecum
    show winmelaniaivanka03-6
with dissolve
mc "Here's some MONSTER CUMSHOTS FOR YOU, RHAAA!{w=1.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
ma "AAAH! You're PUMPING sssoo MUCH SEED IN ME! {w=2.0}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgymarnieleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgymarnieleave with moveoutright
jump EndFuck        

label Winzarafuck:
show orgyzarasetup at farleft02
mc "Damn, it's none other than ZARA! {w=1.5}{nw}"
window hide
show orgyzarasetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgyzarasetup at left
with dissolve
za "Yes it's ME, Master President. Ready to report for ANAL SEX DUTY! {w=3.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/barbarasex.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-74
        show winzarafuck
    if drolltrumpfsex == 2:
        show winzarafuck
        show winmelaniaivanka02-74
    if drolltrumpfsex == 3:
        show winzarafuck
        show winmelaniaivanka03-74
    $ renpy.pause(.74, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-74
    show orgyzaracum
if drolltrumpfsex == 2:
    show orgyzaracum
    show winmelaniaivanka02-74
if drolltrumpfsex == 3:
    show orgyzaracum
    show winmelaniaivanka03-74
with dissolve
mc "And now your DUTY is to TAKE MY CUMLOAD, AAAH!!{w=2.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
za "AAAH! I will obey and let you dump your MONSTERLOAD inside me! {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgyzaraleave at centerright
with dissolve
mc "I NEED MORE SEX, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgyzaraleave with moveoutright
jump EndFuck        

label Winclarafuck:
show orgyclarasetup at farleft02
mc "OOH YEAH, CLARA! {w=1.0}{nw}"
window hide
show orgyclarasetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgyclarasetup at left
with dissolve
cl "Let us pray. That your GIANT TEENAGE COCK FITS INSIDE MY SINFUL MOUTHHOLE! {w=3.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/blowjob.ogg"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-705
        show winclarafuck
    if drolltrumpfsex == 2:
        show winclarafuck
        show winmelaniaivanka02-705
    if drolltrumpfsex == 3:
        show winclarafuck
        show winmelaniaivanka03-705
    $ renpy.pause(.705, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-705
    show orgyclaracum
if drolltrumpfsex == 2:
    show orgyclaracum
    show winmelaniaivanka02-705
if drolltrumpfsex == 3:
    show orgyclaracum
    show winmelaniaivanka03-705
with dissolve
mc "Ramming it in DEEP... AND CUMMING! {w=1.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
cl "YES! WASH AWAY MY SINS WITH YOUR MANLY SPUNK! {w=2.0}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgyclaraleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgyclaraleave with moveoutright
jump EndFuck        

label Wingwenfuck:
show orgygwensetup at farleft02
mc "Gwen! Naughty girl... {w=1.0}{nw}"
window hide
show orgygwensetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgygwensetup at left
with dissolve
gw "You want naughty? I'll show you NAUGHTY! {w=2.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/barbarasex.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-79
        show wingwenfuck
    if drolltrumpfsex == 2:
        show wingwenfuck
        show winmelaniaivanka02-79
    if drolltrumpfsex == 3:
        show wingwenfuck
        show winmelaniaivanka03-79
    $ renpy.pause(.79, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-79
    show orgygwencum
if drolltrumpfsex == 2:
    show orgygwencum
    show winmelaniaivanka02-79
if drolltrumpfsex == 3:
    show orgygwencum
    show winmelaniaivanka03-79
with dissolve
mc "Take my NAUGHTY CUM, RHAAA! {w=1.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
gw "Damn [name], your balls really were FULL, weren't they? {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgygwenleave at centerright
with dissolve
mc "I NEED MORE SEX, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgygwenleave with moveoutright
jump EndFuck        

label Winrachelfuck:
show orgyrachelsetup at farleft02
mc "ULTRA-BUSTY NURSE RACHEL! {w=1.0}{nw}"
window hide
show orgyrachelsetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgyrachelsetup at left
with dissolve
ra "I must make sure our President stays HEALTHY and ACTIVE. SO I'll ACTIVATE YOUR GIANT PHALLUS WITH MY PUSSY! {w=3.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/barbarasex.mp3"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-74
        show winrachelfuck
    if drolltrumpfsex == 2:
        show winrachelfuck
        show winmelaniaivanka02-74
    if drolltrumpfsex == 3:
        show winrachelfuck
        show winmelaniaivanka03-74
    $ renpy.pause(.74, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-74
    show orgyrachelcum
if drolltrumpfsex == 2:
    show orgyrachelcum
    show winmelaniaivanka02-74
if drolltrumpfsex == 3:
    show orgyrachelcum
    show winmelaniaivanka03-74
with dissolve
mc "Take that HEALTHY dose of teenage cum, AAAH! {w=1.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
ra "You can EMPTY yourself in my poontang ANYTIME you want, President [name]! {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgyrachelleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgyrachelleave with moveoutright
jump EndFuck        
    
label Wintaylorfuck:
show orgytaylorsetup at farleft02
mc "TAYLOR! Conjugal visit in the White House! {w=1.5}{nw}"
window hide
show orgytaylorsetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgytaylorsetup at left
with dissolve
to "I see you've been busy hubby, now is the time to make my ASS BUSY! {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/barbarasex.mp3"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-74
        show wintaylorfuck
    if drolltrumpfsex == 2:
        show wintaylorfuck
        show winmelaniaivanka02-74
    if drolltrumpfsex == 3:
        show wintaylorfuck
        show winmelaniaivanka03-74
    $ renpy.pause(.74, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-74
    show orgytaylorcum
if drolltrumpfsex == 2:
    show orgytaylorcum
    show winmelaniaivanka02-74
if drolltrumpfsex == 3:
    show orgytaylorcum
    show winmelaniaivanka03-74
with dissolve
mc "Take that WIFEY, RIGHT UP YOUR POOPCHUTE! {w=1.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
to "My darling hubby kept a REAL BIG LOAD for his wife, didn't he? {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgytaylorleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgytaylorleave with moveoutright
jump EndFuck        

label Winwidowfuck:
show orgywidowsetup at farleft02
mc "The BLACK WIDOW! Or Scarlett Johansson to be more precise. {w=2.0}{nw}"
window hide
show orgywidowsetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgywidowsetup at left
with dissolve
wi "After FIGHTING against EVIL, it's time for my PUSSY to FIGHT against your MONSTERCOCK! {w=3.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/barbarasex.mp3"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-74
        show winwidowfuck
    if drolltrumpfsex == 2:
        show winwidowfuck
        show winmelaniaivanka02-74
    if drolltrumpfsex == 3:
        show winwidowfuck
        show winmelaniaivanka03-74
    $ renpy.pause(.74, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-74
    show orgywidowcum
if drolltrumpfsex == 2:
    show orgywidowcum
    show winmelaniaivanka02-74
if drolltrumpfsex == 3:
    show orgywidowcum
    show winmelaniaivanka03-74
with dissolve
mc "BUSTING INSIDE A PSEUDO-SUPERHEROINE, AAAH! {w=2.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
wi "You're FLOODING my insides with your superhero cream, AAAH! {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgywidowleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgywidowleave with moveoutright
jump EndFuck        

label Winwendyfuck:
show orgywendysetup at farleft02
mc "Wendy from swampy Louisiana! HURRAH! {w=2.0}{nw}"
window hide
show orgywendysetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgywendysetup at left
with dissolve
we "I'm gonna DRAIN YOUR SWAMP, cowboy! {w=2.0}{nw}"
mc "Take a ride, YEE-HAW! {w=1.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/barbarasex.mp3"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-74
        show winwendyfuck
    if drolltrumpfsex == 2:
        show winwendyfuck
        show winmelaniaivanka02-74
    if drolltrumpfsex == 3:
        show winwendyfuck
        show winmelaniaivanka03-74
    $ renpy.pause(.74, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-74
    show orgywendycum
if drolltrumpfsex == 2:
    show orgywendycum
    show winmelaniaivanka02-74
if drolltrumpfsex == 3:
    show orgywendycum
    show winmelaniaivanka03-74
with dissolve
mc "TRY AND DRAIN THAT MONSTERLOAD, AAAH! {w=2.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
we "This FLOOD was worse than Katrina, but I LOVED IT! {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgywendyleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgywendyleave with moveoutright
jump EndFuck        

label Winpaulettefuck:
show orgypaulettesetup at farleft02
mc "Canadian super-envoy Paulette! Welcome to the US of SEX! {w=2.5}{nw}"
window hide
show orgypaulettesetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgypaulettesetup at left
with dissolve
qu "I must extend my country's friendship with yours. ORALLY, hey? {w=3.0}{nw}"
mc "HEY YEAH! {w=1.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/blowjob.ogg"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-74
        show winpaulettefuck
    if drolltrumpfsex == 2:
        show winpaulettefuck
        show winmelaniaivanka02-74
    if drolltrumpfsex == 3:
        show winpaulettefuck
        show winmelaniaivanka03-74
    $ renpy.pause(.74, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-74
    show orgypaulettecum
if drolltrumpfsex == 2:
    show orgypaulettecum
    show winmelaniaivanka02-74
if drolltrumpfsex == 3:
    show orgypaulettecum
    show winmelaniaivanka03-74
with dissolve
mc "TAKE THIS FAT LOAD BACK TO CANADA, RHAAA! {w=2.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
qu "I'm sure Trudeau will appreciate your cream pudding. {w=2.0}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgypauletteleave at centerright
with dissolve
mc "I NEED MORE SEX, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgypauletteleave with moveoutright
jump EndFuck        
    
label FutureGameEnd:
stop channel1
stop channel2
play music "Sounds/showerstrip.mp3"
hide screen endall
window hide
scene ovalofficeaftermath:
    xpos 0.0
    linear 4.0 xpos -0.1
$ renpy.pause(5.0, hard='True')
show mcend01b at left with moveinleft
mc "That's right people, I'm the ULTIMATE SEX PREZ NOW! NOBODY CAN BEAT ME IN THE SEX DEPARTMENT!"
window hide
show superboy01 at centerright with moveinright
sc "Oh yeah? Well I'm the next HERO in the dev's next game! A SUPERHERO actually!"
hide mcend01b
show mcend02b at left
with fastdissolve
mc "Pff, you? You're like a MIDGET next to ME!"
hide superboy01
show superboy02 at centerright
with dissolve
sc "I beg to differ. Check THIS donkey-dick out!"
hide mcend02b
hide superboy02
show mcend03b at left
show superboy03 at centerright
with dissolve
play sound "Sounds/thud.mp3"
mc "Doesn't look quite as big as me buddy... I'm still the KING here!"
sc "I'm just on level One of my body progression. I can grow even BIGGER! Imagine how ENORMOUS I'll be at level THREE!"
hide mcend03b
show mcend04b at left
with fastdissolve
mc "That must be a sight!"
hide superboy03
show superboy04 at centerright
with dissolve
sc "So EVERYONE should join the dev's Patreon page and support the development of \"COCKHAM\". A game where I will FIGHT organized SEX CRIME in Cockham City with other * SEXY * superheroes."
hide mcend03b
show mcend04b at left
with fastdissolve
mc "Ah yeah? Like who for example?"
show captainmilf at farright03 with moveinright
hide superboy04
show superboy03 at centerright
with dissolve
sc "Like this hot superheroine, Captain MILF. She's my mo... I mean landlady."
hide mcend04b
show mcend03b at left
with fastdissolve
mc "Mmmh, I think I've seen this face before... But the body is BIGGER and MORE MUSCULAR than what I remember... Also crisper for some reason..."
hide mcend03b
show mcend04b at left
with fastdissolve
mc "OK, I'm sold. I'm already super-excited about the game and I will advertise it on my presidential twatter account."
sc "I thought you had been banned for being a seditious traitor?"
hide mcend04b
show mcend02b at left
with fastdissolve
mc "Na, that was the former guy. I'm the NEW GUY. AND I WON THE GAME."
hide mcend02b
show mcend03b at left
with fastdissolve
mc "By the way... You've got nicer hair than me. Can I sniff them?"
play sound "v10/lookatthisguy.mp3"
$ renpy.pause(1.0, hard='True')
stop music
play music "v10/thisistheend.mp3"
scene ovalofficeaftermath blurred
show captainmilf at farright02
with dissolve
window hide
show screen endcredit02
screen endcredit02:
    imagebutton idle "v10/epiclustpatreon.png" hover "v10/epiclustpatreon.png" xpos 1550 ypos 50 focus_mask True action OpenURL("https://www.patreon.com/epiclust")
show endcredits at left:
    yalign 1.5
    linear 5.0 yalign 0.2
$ renpy.pause(39.8, hard=True)
return





