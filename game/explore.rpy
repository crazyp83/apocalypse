label Explore:
show screen mcstats
show screen calendar
$ explored = True
if withbe and withmarvel:
    scene bellamarvel
    with fade
    mc "Avengers, ready?"
    mo "Oh, I suppose, sweetie pie..."
    be "Let's go!"
    window hide
    play sound "Sounds/explorepenny02.mp3"
    pause 2
    stop sound
    jump AvengersMission

if withpe and withmarvel:
    scene pennymarvel
    with fade
    mc "Avengers, ready?"
    mo "Oh, I suppose, sweetie pie..."
    pe "Let's go!"
    window hide
    play sound "Sounds/explorepenny02.mp3"
    pause 2
    stop sound
    jump AvengersMission

if alone and withnone:
    scene mcbikeruby
    show mcbikealone
    with fade
    mc "On the road again. Goin' places that I've never been."
    window hide
    play sound "Sounds/explorepenny02.mp3"
    pause 2
    stop sound
    jump ExploreHex
if alone and witham:
    scene mcbikeruby
    show mcbikeamy
    with fade
    mc "Ready for some adventure Amy?"
    am "I sure am! Mother Nature, here I come!"
    play sound "Sounds/explorepenny02.mp3"
    window hide
    pause 2
    stop sound
    jump ExploreHex
if alone and withan:
    scene mcbikeruby
    show mcbikeangie
    with fade
    mc "Ready to tackle some potential danger Angie?"
    an "With you protecting me, I'm READY!"
    play sound "Sounds/explorepenny02.mp3"
    window hide
    pause 2
    jump ExploreHex
if alone and withay:
    scene mcbikeruby
    show mcbikeayla
    with fade
    mc "Ready for some non-boring fun Ayla?"
    ay "Whatever, get on with it."
    window hide
    play sound "Sounds/explorepenny02.mp3"
    pause 2
    stop sound
    jump ExploreHex
if alone and withcy:
    scene mcbikeruby
    show mcbikecyrl
    with fade
    mc "Ready for to serve mankind Cyrl?"
    cy "AND cyborgkind if you please..."
    window hide
    play sound "Sounds/explorepenny02.mp3"
    pause 2
    stop sound
    jump ExploreHex
if alone and withmo:
    scene mcbikeruby
    show mcbikenancy
    with fade
    mc "Ready?"
    mo "I'm holding steady around your large pec muscles sweetie pie!"
    window hide
    play sound "Sounds/explorepenny02.mp3"
    pause 2
    stop sound
    jump ExploreHex
if alone and withza:
    scene mcbikeruby
    show mcbikezara
    with fade
    mc "Ready to go where no nomad has gone before Zara?"
    za "Oh yes, I'm glad to be leaving the compound with you [name]!"
    window hide
    play sound "Sounds/explorepenny02.mp3"
    pause 2
    jump ExploreHex
if alone and withmi:
    scene mcbikeruby
    show mcbikemichiko
    with fade
    mc "Ready for some adventure Michiko?"
    mi "I sure am! Mother Nature, here we go!"
    window hide
    play sound "Sounds/explorepenny02.mp3"
    pause 2
    stop sound
    jump ExploreHex
if alone and withru:
    scene mcbikeruby
    with fade
    mc "Ready for some adventure Ruby?"
    ru "Let's kick some enemy ass! Yee-Haw!"
    window hide
    play sound "Sounds/explorepenny02.mp3"
    pause 2
    stop sound
    jump ExploreHex
if alone and withsu:
    scene mcbikeruby
    show mcbikesuki
    with fade
    mc "Ready for some adventure Suki?"
    su "Sure [name], I feel SAFE with you!"
    window hide
    play sound "Sounds/explorepenny02.mp3"
    pause 2
    stop sound
    jump ExploreHex
if alone and withgw:
    scene mcbikeruby
    show mcbikegwen
    with fade
    mc "Ready for some adventure Gwen?"
    gw "Sure [name], as long as nothing EXPLODES in my face!"
    window hide
    play sound "Sounds/explorepenny02.mp3"
    pause 2
    stop sound
    jump ExploreHex
if alone and withma:
    scene mcbikeruby
    show mcbikemarnie
    with fade
    mc "Ready for some adventure Marnie?"
    ma "It better bring something useful for the compound bar, I should be making tar cocktails normally at this time!"
    window hide
    play sound "Sounds/explorepenny02.mp3"
    pause 2
    stop sound
    jump ExploreHex
if alone and withcl:
    scene mcbikeruby
    show mcbikeclara
    with fade
    mc "Ready for some adventure Clara?"
    cl "I am, but may the Phallus Lord protect us!"
    window hide
    play sound "Sounds/explorepenny02.mp3"
    pause 2
    stop sound
    jump ExploreHex
if alone and withla:
    scene mcbikeruby
    show mcbikelaurie
    with fade
    mc "Ready for some adventure Laurie?"
    la "I am, I just watered my plants!"
    window hide
    play sound "Sounds/explorepenny02.mp3"
    pause 2
    stop sound
    jump ExploreHex
if alone and withba:
    scene mcbikeruby
    show mcbikebarbara
    with fade
    mc "Ready for some adventure Barbara?"
    ba "Of course, we'll call this a school trip!"
    window hide
    play sound "Sounds/explorepenny02.mp3"
    pause 2
    stop sound
    jump ExploreHex
if alone and withde:
    scene mcbikeruby
    show mcbikedebra
    with fade
    mc "Ready for some adventure Debra?"
    de "I don't like leaving Gwen in the lab alone but I guess I don't have a choice..."
    window hide
    play sound "Sounds/explorepenny02.mp3"
    pause 2
    stop sound
    jump ExploreHex
    
if withbe:
    play sound "Sounds/explorebella02.mp3"
    if hex == 32 and rescuedmagnus:
        scene explorebella01 with fade
        be "Off we go! Put on your seatbelt [name]!"
        mc "Let's go to the Red Canyon and get Magnus on the way to the crater please Bella."
        be "Alright, detour to the Red Canyon!"
        scene canyon01
        show magnus02
        with dissolve
        mg "Am I finally going to see mommy again?"
        mc "Yep. Hop on, I'll take you to her..."
        jump ExploreHex
    if withnone:
        scene explorebella01 with fade
        be "Off we go! Put on your seatbelt [name]!"
    if withmo:
        scene explorebella01
        show nancybellatruck01
        with fade
        be "Off we go! Put on your seatbelts!"
        mo "I don't have any..."
        be "Yeah, sorry Nancy, but this beast is a two-seater, I'll drive carefully don't worry."
    if withmi:
        scene explorebella01
        show michikobellatruck01
        with fade
        be "Off we go! Put on your seatbelts!"
        mi "I don't have any..."
        be "Yeah, sorry Michiko, but this beast is a two-seater, I'll drive carefully don't worry."
    if withan:
        scene explorebella01
        show angiebellatruck01
        with fade
        be "Off we go! Put on your seatbelts!"
        an "I don't have any..."
        be "Yeah, sorry Angie, but this beast is a two-seater, I'll drive carefully don't worry."
    if withru:
        scene explorebella01
        show rubybellatruck01
        with fade
        be "Off we go! Put on your seatbelts!"
        ru "Yee-HA, no seatbelt for me!"
    if withcy:
        scene explorebella01
        show cyrlbellatruck01
        with fade
        be "Off we go! Put on your seatbelts!"
        cy "I see that humans couldn't care less about my safety since I have not been provided with a seatbelt."
        be "Yeah, sorry Cyrl, but this beast is a two-seater, I'll drive carefully don't worry."
    if withza:
        scene explorebella01
        show zarabellatruck01
        with fade
        be "Off we go! Put on your seatbelts!"
        za "I don't have any..."
        be "Yeah, sorry Zara, but this beast is a two-seater, I'll drive carefully don't worry."
    if witham:
        scene explorebella01
        show amybellatruck01
        with fade
        be "Off we go! Put on your seatbelts!"
        am "Ah, the great outdoors!"
    if withay:
        scene explorebella01
        show aylabellatruck01
        with fade
        be "Off we go! Put on your seatbelts!"
        ay "This had better not be BORING."
    if withsu:
        scene explorebella01
        show sukibellatruck01
        with fade
        be "Off we go! Put on your seatbelts!"
        su "Finally, out of the basement!"
    if withgw:
        scene explorebella01
        show gwenbellatruck01
        with fade
        be "Off we go! Put on your seatbelts!"
        gw "Finally, out of the lab!"
    if withma:
        scene explorebella01
        show marniebellatruck01
        with fade
        be "Off we go! Put on your seatbelts!"
        ma "Not me, I want to be FREE!"
    if withcl:
        scene explorebella01
        show clarabellatruck01
        with fade
        be "Off we go! Put on your seatbelts!"
        cl "I'm fine without. The Phallus Lord will protect me."
    if withla:
        scene explorebella01
        show lauriebellatruck01
        with fade
        be "Off we go! Put on your seatbelts!"
        la "Oh dear me, I hope it doesn't get too bumpy."
    if withba:
        scene explorebella01
        show barbarabellatruck01
        with fade
        be "Off we go! Put on your seatbelts!"
        ba "The school's health and safety board might have something to say about this..."
    if withde:
        scene explorebella01
        show debrabellatruck01
        with fade
        be "Off we go! Put on your seatbelts!"
        de "Safety is always my main concern in the lab. Except if Gwen is involved."

    if period == 1 and withnone:
        scene explorebella02a
        with dissolve
    if period == 2 and withnone:
        scene explorebella02b
        with dissolve
    window hide
    pause
    be "We'll get there in not time with my rig!"
    stop sound
    jump ExploreHex
if withpe:
    scene explorepenny01 with fade
    pe "Hang tight in there [name]!"
    if hex == 32 and rescuedmagnus:
        mc "Let's go to the Red Canyon and get Magnus on the way to the crater please Penny."
        pe "Alright, detour to the Red Canyon!"
        scene canyon01
        show magnus02
        with dissolve
        mg "Am I finally going to see mommy again?"
        mc "Yep. Hop on, I'll take you to her..."
        jump ExploreHex
    if withnone and harempe == False and lustpe >= 4:
        menu:
            "While we're here alone, I' like to say that I think it's time now for you to join my harem Penny..." if pennyharem == False and girlsinharem <= 5:
                pe "A harem? Road Warriors are FREE CREATURES!"
                mc "Then you're FREE to join my harem."
                pe "I guess that makes sense. I'll join out of my OWN FREE WILL then!"
                $ harempe = True
                $ girlsinharem += 1
                $ pennyharem = True
                window hide
                show harempenny at plus
                $ renpy.pause(2.0, hard=True)
                hide harempenny
                mc "I'll call you at nights, so we can explore each other's bodies in a FUN SEXY WAY."
                pass
            "While we're here alone, I' like to say that I think it's time for you to re-join my harem Penny..." if pennyharem and pennydismissed == False  and girlsinharem <= 5 and pennyrejoined == False:
                $ pennyrejoined = True
                pe "And what assurances do I have that you won't dump me on the side of the road like you did last time?"
                mc "Remember, the Road is everywhere. In spirits. So you were still there with me. In spirits."
                pe "That's a fishy explanation but I'll agree to come back into your harem. THIS ONCE."
                $ harempe = True
                $ girlsinharem += 1
                $ pennyharem = True
                window hide
                show harempenny at plus
                $ renpy.pause(2.0, hard=True)
                hide harempenny
                mc "I'll call you at nights, so we can explore each other's bodies in a FUN SEXY WAY."
                pass
            "Let's go.":
                pass
    window hide
    if withmo:
        mc "Hang on a minute, where's Nancy?"
        mo "I'm here, sweetie pie, just putting on my shoes..."
        mc "Sit behind me, we're about to head off."
    if withmi:
        mc "Hang on a minute, where's Michiko?"
        mi "I'm here, just getting ready..."
        mc "Sit behind me Michiko, we're about to head off."
    if withan:
        mc "Hang on a minute, where's Angie?"
        an "I'm here, just getting ready..."
        mc "Sit behind me Angie, we're about to head off."
    if withru:
        mc "Hang on a minute, where's Ruby?"
        ru "I'm here, just getting ready..."
        mc "Sit behind me Ruby, we're about to head off."
    if withcy:
        mc "Hang on a minute, where's Cyrl?"
        cy "I am calculating my chances of survival if I agree to ride of this infernal mechanical device..."
        mc "Come on, just sit behind me Cyrl, we'll be fine."
    if withza:
        mc "Hang on a minute, where's Zara?"
        za "I'm here, just getting ready..."
        mc "Sit behind me Zara, we're about to head off."
    if witham:
        mc "Hang on a minute, where's Amy?"
        am "I'm here, just getting ready for the Great Outdoors!"
    if withay:
        mc "Hang on a minute, where's Ayla?"
        ay "I'm here, but don't wait for me, I can't be bothered."
        mc "Just hop on and stop moaning, will you?"
    if withsu:
        mc "Hang on a minute, where's Suki?"
        su "I'm here, just had to finish downloading my Windows 11 update. It took ages."
    if withgw:
        mc "Hang on a minute, where's Gwen?"
        gw "I'm here, just finishing putting on some makeup."
    if withma:
        mc "Hang on a minute, where's Marnie?"
        ma "I was just cleaning the tar cocktail barrel, but I'm ready now."
    if withcl:
        mc "Hang on a minute, where's Clara?"
        cl "I was just praying for our safe journey but I'm done so I'm ready to go on your adventure!"
    if withla:
        mc "Hang on a minute, where's Laurie?"
        la "I was just watering my Bostiboobicus Gigantus, I'm here now!"
    if withba:
        mc "Hang on a minute, where's Barbara?"
        ba "I'm here, I was just letting the students know that school is cancelled!"
    if withde:
        mc "Hang on a minute, where's Debra?"
        de "I'm here, I was just giving my final instructions to Gwen."
    
    if period == 1 and withnone:
        scene explorepenny02a
        with dissolve
    if period == 2 and withnone:
        scene explorepenny02b
        with dissolve
    if withmo:
        scene explorepenny02b
        show nancypennybike02
        with dissolve
    if withmi:
        scene explorepenny02b
        show michikopennybike02
        with dissolve
    if withan:
        scene explorepenny02b
        show angiepennybike02
        with dissolve
    if withru:
        scene explorepenny02b
        show rubypennybike02
        with dissolve
    if withcy:
        scene explorepenny02b
        show cyrlpennybike02
        with dissolve
    if withza:
        scene explorepenny02b
        show zarapennybike02
        with dissolve
    if witham:
        scene explorepenny02b
        show amypennybike02
        with dissolve
    if withay:
        scene explorepenny02b
        show aylapennybike02
        with dissolve
    if withsu:
        scene explorepenny02b
        show sukipennybike02
        with dissolve
    if withgw:
        scene explorepenny02b
        show gwenpennybike02
        with dissolve
    if withma:
        scene explorepenny02b
        show marniepennybike02
        with dissolve
    if withcl:
        scene explorepenny02b
        show clarapennybike02
        with dissolve
    if withla:
        scene explorepenny02b
        show lauriepennybike02
        with dissolve
    if withba:
        scene explorepenny02b
        show barbarapennybike02
        with dissolve
    if withde:
        scene explorepenny02b
        show debrapennybike02
        with dissolve
    play sound "Sounds/explorepenny02.mp3"
    if d4rollpennyexplore == 4:
        jump PennyStation
    pe "Yee-ha!"

label ExploreHex:
if ((bounty and knowbounty and mctrumpster <= 4) or (melaniabounty and knowmelaniabounty)) and day <= 5 and missionchurch == False:    

    if d4rollbounty == 1:
        jump BountyHunter

if withpe and withnone:
    scene explorepenny03 with dissolve
    stop sound
    mc "Nice one Penny, you're a really good rider!"
    pe "Can't find a faster way to travel than with me!"    

if hex == 01:
    jump ExploreHex01
if hex == 02:
    jump ExploreHex02
if hex == 03:
    jump ExploreHex03
if hex == 11:
    jump ExploreHex11
if hex == 12:
    jump ExploreHex12
if hex == 13:
    jump ExploreHex13
if hex == 14:
    jump ExploreHex14
if hex == 15:
    jump ExploreHex15
if hex == 16:
    jump ExploreHex16
if hex == 17:
    jump ExploreHex17
if hex == 21:
    jump ExploreHex21
if hex == 22:
    jump ExploreHex22
if hex == 23:
    jump ExploreHex23
if hex == 24:
    jump ExploreHex24
if hex == 25:
    jump ExploreHex25
if hex == 26:
    jump ExploreHex26
if hex == 27:
    jump ExploreHex27
if hex == 31:
    jump ExploreHex31
if hex == 32:
    jump ExploreHex32
if hex == 33:
    jump ExploreHex33
if hex == 34:
    jump ExploreHex34
if hex == 35:
    jump ExploreHex35
if hex == 36:
    jump ExploreHex36

if hex == 41:
    jump ExploreHex41
if hex == 42:
    jump ExploreHex42
if hex == 43:
    jump ExploreHex43
if hex == 44:
    jump ExploreHex44
if hex == 45:
    jump ExploreHex45
if hex == 46:
    jump ExploreHex46

if hex == 51:
    jump ExploreHex51
if hex == 52:
    jump ExploreHex52
if hex == 53:
    jump ExploreHex53
if hex == 54:
    jump ExploreHex54
if hex == 55:
    jump ExploreHex55
if hex == 56:
    jump ExploreHex56

if hex == 61:
    jump ExploreHex61
if hex == 62:
    jump ExploreHex62
if hex == 64:
    jump ExploreHex64
if hex == 65:
    jump ExploreHex65

label ExploreHex01:
if exploredhex01 == False:
    jump Hex01a
if exploredhex01 == True:
    jump Hex01b

label Hex01a:
stop sound
stop music
scene desert01 
show desertrocks
with dissolve
$ exploredhex01 = True

if withbe:
    be "Just like last time, nothing to see here..."
    mc "Are all scouting missions THAT boring?"
    be "So far, pretty much, yes."
if withpe:
    pe "Just like last time, nothing to see here..."
    mc "Are all scouting missions THAT boring?"
    pe "What? You're looking for trouble? Like you want to meet some mean Road Warriors?"
    mc "Well, errr..."

show camel01
mc "Hang on a minute, there's a camel over there. What's it doing here?"
if withbe:
    be "It's a desert... There are camels in it. I saw one here last time too. Shot him and got a 10$ reward for its meat."
    mc "I know that camels live in the desert. But NOT in the American desert!"
    hide camel01
    show camel02
    be "The Islamo-Nucleorists brought them over at the end of the War, that's why!"
    mc "Should we shoot it then?"
    be "Yes, I guess this a good opportunity to test your shooting skills. I'll LEND you my rifle this once."
    be "Let's move behind that rock over there to get closer..."
    jump CamelShoot
if withpe:
    pe "Camels live in the desert, man. I saw one here last time too. Shot him straight between the eyes. Makes for good sturdy meat burgers back in the compound."
    mc "But how did a camel end up here in America?"
    pe "Who knows, maybe we're not even in America anymore! I call it the \"Road Wilderness\" personally..."
    hide camel01
    show camel02
    mc "Except there are no roads... Should we try and shoot the damn camel then?"
    pe "Yes, I guess this a good opportunity to test your shooting skills. I'll LEND you my rifle this once."
    pe "Let's move behind that rock over there to get closer..."
    jump CamelShoot

label CamelShoot:
if withbe:
    hide desertrocks
    show bellarock01
    with dissolve
    be "Aim carefully..."
    call DiceRoll
    $ dshootroll=mcfirearms+diceroll
    if (dshootroll >= 3 and not diceroll == 1) or diceroll == 6:
        window hide
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel02
        show cameldead
        with dissolve
        stop sound
        $ renpy.pause(1.0, hard=True)
        be "Congrats, it's dead meat now. We can go back to the compound."
        $ camelshot = True
        $ camelsshot += 1
        if camelsshot >= 10:
            mc "*I think I'm getting really good at shooting things in the wild...*"
            call PlusWarrior
            call MinusSierra
            $ camelsshot = 0        
        jump CamelMissionOut01
    if (dshootroll <= 2 and not diceroll == 6) or diceroll == 1:
        window hide
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel02
        show camel05
        with dissolve
        stop sound
        be "You missed. And now it's getting away. Give me my rifle back, quick!"
        hide bellarock01
        show bellarock02
        with dissolve
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel05
        show cameldead02
        with dissolve
        stop sound
        $ renpy.pause(1.0, hard=True)
        $ bellashotcamels += 1
        if bellashotcamels <= 3:
            hide bellarock02
            show bellarock01
            with dissolve
            be "Good thing MY shooting skills are better than YOURS! Let's go back to the compound now."
            $ bellashotcamel = True
            $ camelshot = True
        if bellashotcamels >= 4:
            hide bellarock02
            show bellarock01
            with dissolve
            be "Good thing MY shooting skills are better than YOURS! Let's go back to the compound now. For MY reward." 
            $ bellashotcamel = True
        jump CamelMissionOut01

if withpe:
    hide desertrocks
    show pennyrock01
    with dissolve
    pe "Aim carefully..."
    call DiceRoll
    $ dshootroll=mcfirearms+diceroll
    if (dshootroll >= 3 and not diceroll == 1) or diceroll == 6:
        window hide
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel02
        show cameldead
        with dissolve
        stop sound
        $ renpy.pause(1.0, hard=True)
        pe "Congrats, it's dead meat now. We can go back to the compound."
        $ camelshot = True
        $ camelsshot += 1
        if camelsshot >= 10:
            mc "*I think I'm getting really good at shooting things in the wild...*"
            call PlusWarrior
            call MinusSierra
            $ camelsshot = 0        
        jump CamelMissionOut01
    if (dshootroll <= 2 and not diceroll == 6) or diceroll == 1:
        window hide
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel02
        show camel05
        with dissolve
        stop sound
        pe "You missed. And now it's getting away. Give me my rifle back, quick!"
        hide pennyrock01
        show pennyrock02
        with dissolve
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel05
        show cameldead02
        with dissolve
        stop sound
        $ renpy.pause(1.0, hard=True)
        $ pennyshotcamels += 1
        if pennyshotcamels <= 3:
            hide pennyrock02
            show pennyrock01
            with dissolve
            pe "Good thing MY shooting skills are better than YOURS! Let's go back to the compound now."   
            $ camelshot = True
            $ pennyshotcamel = True            
        if pennyshotcamels >= 4:
            hide pennyrock02
            show pennyrock01
            with dissolve
            pe "Good thing MY shooting skills are better than YOURS! Let's go back to the compound now. For MY reward."        
            $ pennyshotcamel = True
        jump CamelMissionOut01
    
label Hex01b:
stop sound
stop music
if persistent.tipson:
    show hex01tip at tips with dissolve
    pause
    hide hex01tip
if withbe:
    scene desert01
    show camel01
    show desertrocks
    with dissolve
    be "Ah, there's another camel. Seems like they spawn here quite easily."
    hide camel01
    show camel02
    mc "Let's shoot it then!"
    if rifle and bellashotcamels >= 4:
        be "Use your OWN rifle this time."
if withpe:
    scene desert01
    show camel01
    show desertrocks
    with dissolve
    pe "Ah, there's another camel. Seems like they spawn here quite easily."
    hide camel01
    show camel02
    mc "Let's shoot it then!"
    if rifle and pennyshotcamels >= 4:
        pe "Use your OWN rifle this time."
if darts >= 1 and money >= 5:
    menu:
        "How about we capture it alive? (-5 dollars, -1 dart, +1 camel)":
            if withbe:
                be "That doesn't bring any money to me..."
                if rifle or (rifle and bellashotcamels <= 3):
                    mc "I'll pay you your share, five bucks, if you let me use your rifle and one of my tranquilizer darts..."
                if rifle and bellashotcamels >= 4:
                    mc "I'll pay you your share, five bucks, if you let me use one of my tranquilizer darts..."
                be "Fine, as long as I get my money... Like now."
                $ money -= 5
                $ darts -= 1
                if darts == 0:
                    $ dart = False
                jump CamelCapture
            if withpe:
                pe "That doesn't bring any money to me..."
                if rifle or (rifle and pennyshotcamels <= 3):
                    mc "I'll pay you your share, five bucks, if you let me use your rifle and one of my tranquilizer darts..."
                if rifle and pennyshotcamels >= 4:
                    mc "I'll pay you your share, five bucks, if you let me use one of my tranquilizer darts..."
                pe "Fine, as long as I get my money... Like now."
                $ money -= 5
                $ darts -= 1
                if darts == 0:
                    $ dart = False
                jump CamelCapture
        "OK, let's shoot it for its meat and the reward.":
            if withbe:
                be "I'm fine with that. You try first, you need training."
            if withpe:
                pe "I'm fine with that. You try first, you need training."            
            jump CamelShoot
jump CamelShoot

label CamelCapture:
if withbe:
    hide desertrocks
    show bellarock01
    with dissolve
    be "Aim carefully..."
    call DiceRoll
    $ dshootroll=mcfirearms+diceroll
    if (dshootroll >= 3 and not diceroll == 1) or diceroll == 6:
        window hide
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel02
        show cameldead
        with dissolve
        stop sound
        be "There, it's asleep now. We can bring it back to the compound. And you'd better hide it from Chief Lena."
        $ camelcaptured = True
        $ camels += 1
    if (dshootroll <= 2 and not diceroll == 6) or diceroll == 1:
        window hide
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel02
        show camel05
        with dissolve
        stop sound
        be "You missed. And now it's getting away. Give me my rifle back, quick!"
        hide bellarock01
        show bellarock02
        with dissolve
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel05
        show cameldead02
        with dissolve
        stop sound
        $ renpy.pause(1.0, hard=True)
        $ bellashotcamels += 1
        if bellashotcamels <= 3:
            hide bellarock02
            show bellarock01
            with dissolve
            be "Good thing MY shooting skills are better than YOURS! It's dead now, since you only loaded ONE dart. But let's go back to the compound for our reward."        
            be "I'll give you your 5 bucks back though since you failed miserably and we didn't end up capturing it..."
            $ money += 5
            $ camelshot = True
        if bellashotcamels >= 4:
            hide bellarock02
            show bellarock01
            with dissolve
            be "Good thing MY shooting skills are better than YOURS! It's dead now, since you only loaded ONE dart. Let's go back to the compound now. For MY reward."
            be "But I'll give you your 5 bucks back though since you failed miserably..."
            $ money += 5
        $ bellashotcamel = True
        jump CamelMissionOut01
    "You now have [camels] camels in your possession."
    if missionza and camels >= 4:
        "You have enough camels to go back to the nomad camp."
    if missionza02 and camels >= 6:
        "You have enough camels to go back to the nomad camp."   
    jump CamelMissionOut01
if withpe:
    hide desertrocks
    show pennyrock01
    with dissolve
    pe "Aim carefully..."
    call DiceRoll
    $ dshootroll=mcfirearms+diceroll
    if (dshootroll >= 3 and not diceroll == 1) or diceroll == 6:
        window hide
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel02
        show cameldead
        with dissolve
        stop sound
        pe "There, it's asleep now. We can bring it back to the compound. And you'd better hide it from Chief Lena."
        $ camelcaptured = True
        $ camels += 1
    if (dshootroll <= 2 and not diceroll == 6) or diceroll == 1:
        window hide
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel02
        show camel05
        with dissolve
        stop sound
        pe "You missed. And now it's getting away. Give me my rifle back, quick!"
        hide pennyrock01
        show pennyrock02
        with dissolve
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel05
        show cameldead02
        with dissolve
        stop sound
        $ renpy.pause(1.0, hard=True)
        $ pennyshotcamels += 1
        if pennyshotcamels <= 3:
            hide pennyrock02
            show pennyrock01
            with dissolve
            pe "Good thing MY shooting skills are better than YOURS! It's dead now, since you only loaded ONE dart. But let's go back to the compound for our reward."        
            pe "I'll give you your 5 bucks back though since you failed miserably and we didn't end up capturing it..."
            $ money += 5
            $ camelshot = True
        if pennyshotcamels >= 4:
            hide pennyrock02
            show pennyrock01
            with dissolve
            pe "Good thing MY shooting skills are better than YOURS! It's dead now, since you only loaded ONE dart. Let's go back to the compound now. For MY reward."
            pe "But I'll give you your 5 bucks back though since you failed miserably..."
            $ money += 5
        $ pennyshotcamel = True
        jump CamelMissionOut01
    "You now have [camels] camels in your possession."
    if missionza and camels >= 4:
        "You have enough camels to go back to the nomad camp."
    if missionza02 and camels >= 6:
        "You have enough camels to go back to the nomad camp."   
    jump CamelMissionOut01


label CamelMissionOut01:
$ period += 1
scene command01 with fade
show lena01
le "So, what do you have to report about area A1, scouts?"
if camelshot:
    $ camelshot = False
    if pennyshotcamel or bellashotcamel:
        mc "I report that we shot a camel. Well, one of us did, but it was teamwork."
    if pennyshotcamel == False and bellashotcamel == False:
        mc "I report that I shot a camel. Right between the eyes."
    hide lena01
    show lena06
    with fastdissolve
    le "That's it? A camel? You didn't see anything else?"
    mc "Nope. Just desert and a camel in it. Now a dead camel which we brought back for its meat."
    hide lena06
    show lenapensive
    with fastdissolve
    le "Umpf. I guess we should start exploring other areas."
    mc "At least we have a camel Chief Lena!"
    hide lenapensive
    show lena05
    with fastdissolve
    le "That's so great. More bloody camel burgers for everyone on the menu this week..."
    $ bellashotcamel = False
    $ pennyshotcamel = False
    if withpe:
        pe "May I remind you Chief Lena that a camel is worth 10 dollars for the scout that brings it back here. Both of us in this case."
        hide lena05
        show lena06
        with fastdissolve
        le "I am well aware of this cost... Here's your money. Now get some rest. We need to get valuable intel from these scouting missions in the future."
        $ money += 5
        hide lena06
        jump LeaveCommand
    if withbe:
        be "Far from me being greedy, which is against the Church's teachings, but I'm aware there is a scout reward for camel meat..."
        hide lena05
        show lena06
        with fastdissolve
        le "I am also well aware of this cost to the compound... Here's your money. Now get some rest. We need to get valuable intel from these scouting missions in the future."
        $ money += 5
        hide lena06
        jump LeaveCommand
            
if pennyshotcamel or bellashotcamel:
    mc "Nothing to report. Just desert and a scorching sun Chief Lena!"
    hide lena01
    show lenapensive
    with fastdissolve
    le "That is disappointing. I was sure there was something there.... I guess we should start exploring other areas."
    if withbe:
        be "I also report a dead camel which we brought back for its meat. No thanks to [name]'s atrocious shooting skills. I would like my reward."
        le "Sure Bella. Here is your 10$ reward then. Now get some rest both of you. We need to get valuable intel from these scouting missions in the future."
        mc "What about me? Can't I get paid for my hard work?"
        hide lenapensive
        show lena10
        with fastdissolve
        le "What hard work? So far you've proven to be nothing but a burden on us! You'd better up your game [name]..."
        hide lena10
        $ bellashotcamel = False
        jump LeaveCommand            
    if withpe:
        pe "I also report a dead camel which we brought back for its meat. No thanks to [name]'s atrocious shooting skills. I demand my rightful reward for that."
        le "Sure Penny. Here is your 10$ reward then. Now get some rest both of you. We need to get valuable intel from these scouting missions in the future."
        mc "What about me? Can't I get paid for my hard work?"
        show lena10
        le "What hard work? So far, you've proven to be nothing but a burden on us! You'd better up your game [name]..."
        hide lena10
        $ pennyshotcamel = False
        jump LeaveCommand

if camelcaptured:
    mc "Nothing to report. Just desert and a scorching sun Chief Lena!"
    hide lena01
    show lenapensive
    with fastdissolve
    le "That is disappointing. I was sure there was something there.... I guess we should start exploring other areas."
    hide lenapensive
    show lena10
    with fastdissolve
    le "You are dismissed, scouts..."
    hide lena10
    $ camelcaptured = False
    jump LeaveCommand            

label ExploreHex02:
$ explored = True
$ exploredhex02 = True
stop sound
stop music
scene aliens01 with fade
play music "Sounds/desertwind01.mp3"
mc "I see something over there. It looks like a plane, but it's huge!"
if withbe:
    be "We have to find out what it is so we can report to the Chief. It might be a new government weapon."
    jump DesertAlienChoice01
if withpe:
    pe "We have to find out what it is so we can report to the Chief. It might be a new government weapon."
    jump DesertAlienChoice01
label DesertAlienChoice01:
menu:
    "Yeah... I don't know. It sounds dangerous and we are not heavily armed.":
        if withbe:
            be "If we go back empty-handed, Chief Lena will kill us. Stop being a coward and come."
            mc "Alright..."
            jump DesertAlien02
        if withpe:
            pe "A true Road Warrior never flees in the face of danger! Stop being a coward and come."
            if mcwarrior >= 1:
                window hide
                show minuswarrior at posmission
                $ renpy.pause(2.0, hard=True)
                hide minuswarrior                
                $ mcwarrior -= 1
            mc "Alright..."
            jump DesertAlien02    
    "Alright then. Let's get closer as quietly as possible...":
        jump DesertAlien02
        

label DesertAlien02:
stop music
scene aliens02 with dissolve
show alienfemale
mc "Are you seeing what I'm seeing? It looks like... an alien. A totally naked alien."
if withbe:
    be "Jeezus! We have to report back to the Chief about that immediately..."
if withpe:
    pe "Fuck me! We have to find out what she's doing out here..."
window hide
if persistent.tipson:
    show hex02tip at tips with dissolve
    pause
    hide hex02tip
show alienmale01 at left with dissolve
alm "Ah, finally! Some pitiful humans! Now. Explain to me what the fuck is going on on this planet!"
menu:
    "I have no idea what you're talking about.":
        alm "I'm talking about the fact that we have stopped receiving porn clips from pornrub.com, that's what I'm talking about!"
        window hide
        hide alienmale01
        show alienmale02 at left
        with fastdissolve
        alm "Glurglub, my beauty, come over here, I found some members of the subspecies!"
        window hide
        hide alienfemale
        show alienfemale02 at right
        with fastdissolve         
        alf "Well done my fierce Glorglob. A male and a female specimens, perfect!"
        window hide
        hide alienmale02
        show alienmale01 at left
        with fastdissolve
        hide alienfemale02
        show alienfemale01 at right
        with fastdissolve
        alm "So, I won't repeat myself sub-aliens! Why the hell is there no porn coming out of this planet anymore?"
        jump DesertAliens03
    "Are you an illegal alien?":
        alm "I am Glorglob, that's who I am! Now shut up until spoken to, pitiful human specimen!"
        window hide
        hide alienmale01
        show alienmale04 at left
        with fastdissolve
        alm "Here, that should teach you a lesson!"
        window hide
        show alienshoot
        play sound "Sounds/raygun.mp3"
        pause 0.5
        hide alienshoot
        $ mcinjuredalien = True         
        mc "Hey, stop it, it fucking hurts!"
        window hide
        show mcinjured at injured
        $ renpy.pause(2.0, hard=True)
        hide mcinjured
        $ mcinjured = True
        hide alienmale04
        show alienmale02 at left
        with fastdissolve
        alm "Glurglub, my beauty, come over here, I found some members of the subspecies!"
        window hide
        hide alienfemale
        show alienfemale02 at right
        with fastdissolve         
        alf "Well done my fierce Glorglob. A male and a female specimens, perfect!"
        window hide
        hide alienmale02
        show alienmale01 at left
        hide alienfemale02
        show alienfemale01 at right
        with fastdissolve
        alm "So, I won't repeat myself sub-aliens! Why the hell is there no porn coming out of this planet anymore?"
        jump DesertAliens03        
    "Err.. Your cock is hanging out mate...":
        window hide
        hide alienmale01
        show alienmale03 at left
        with fastdissolve
        alm "Yeah... And it's pretty big isn't it? Glurglub, my beauty, come over here, I found some members of the subspecies!"
        window hide
        hide alienfemale
        show alienfemale02 at right
        with fastdissolve         
        alf "Well done my fierce Glorglob. A male and a female specimens, perfect!"
        window hide
        hide alienmale03
        show alienmale01 at left
        hide alienfemale02
        show alienfemale01 at right
        with fastdissolve
        alm "So, I won't repeat myself sub-aliens! Why the hell is there no porn coming out of this planet anymore?"
        jump DesertAliens03

label DesertAliens03:
hide alienfemale01
show alienfemale04 at right
with fastdissolve
alf "The only thing we've received lately are videos of some orang-utang sitting on a toilet bowl. NOT GOOD ENOUGH!"
mc "Ah. That would be because President-for-life Trumpf replaced all internet content with video clips of him tweeting."
alm "Well we're not interested in seeing his fat lardy ass! We want PORN! So we can make fun of your pathetically small genitals."
label AlienChoice01:
show alienfemale04 at right
show alienmale01 at left
menu:
    "What? Is that why you're interested in human porn?":
        hide alienmale01        
        show alienmale03 at left
        with fastdissolve
        alm "Yeah, I mean look at my monster. Every guy on Glorglon is hung like me. It's so funny watching you guys and your tiny penises going inside the minuscule holes of your inferior women."
        hide alienfemale04
        show alienfemale03 at right
        with fastdissolve
        alf "And your females have such small boobs, it's laughable. Everyone on Glorglon LOVES to make fun of them! Human porn is streamed on the Glorglan Comedy Channel."
        hide alienmale03
        hide alienfemale03
        jump AlienChoice01
    "I beg to differ! You'll find that since the nuclear war, some of us guys have grown mammoth dongs!":
        hide alienmale01        
        show alienmale02 at left
        with fastdissolve        
        alm "Oh yeah? Prove it subspecies! Or we'll destroy your planet!"
        mc "Alright, you asked for it."
        jump AlienSex01
    "Well, take your demands to President Trumpf then. And kill him, while you're at it.":
        hide alienmale01        
        show alienmale04 at left
        with fastdissolve  
        alm "We don't have time for that nonsense. Besides, nobody knows where Trumpf City is!"
        alm "Here, take that for your insolence sub-alien!"
        window hide
        show alienshoot
        play sound "Sounds/raygun.mp3"
        pause 0.5
        hide alienshoot
        $ mcinjuredalien = True         
        mc "Hey, stop it, it fucking hurts!"
        window hide
        show mcinjured at injured
        $ renpy.pause(2.0, hard=True)
        hide mcinjured
        if mcinjured:
            mc "AGAIN!"
        $ mcinjured = True
        hide alienfemale04
        show alienfemale02 at right
        with fastdissolve
        alf "Oh, you are so fierce my beloved Glorglob!"
        hide alienfemale02
        hide alienmale04
        jump AlienChoice01
        
label AlienSex01:
$ alienmet = True
scene aliens03 with dissolve
show mcout01 at midleft
if withbe:
    show bellaout01b at midright
    mc "There. Happy now? Notice how it is MUCH bigger than... Glorglob, or whatever the fuck your foreign name is."
    be "I don't know what the hell you think you're doing... I'm scared [name]..."
    mc "Trust me. I'm saving the world..."
    call LustPlusBella
if withpe:
    show pennyout01 at midright
    mc "There. Happy now? Notice how it is MUCH bigger than... Glorglob, or whatever the fuck your foreign name is."
    pe "I don't know what the hell you think you're doing [name]..."
    mc "Trust me. I'm saving the world..."
    call LustPlusPenny
alf "Wow, it is indeed the most MASSIVE sex organ I have ever seen in the whole galaxy."
alm "Yeah, OK, but he's still a pitiful human, right Glurglub?"
alf "Of course my fierce Glorglob! I resent this inferior species. But still..."
scene aliens02
show alienmale01 at left
show alienfemale01 at right
with dissolve
alm "Now, my beauty Glurglub, I have an idea. How about you join this sub-alien for some interspecies porn?"
hide alienfemale01
show alienfemale02 at right
with fastdissolve
alf "What a great idea my fierce Glorglob! This will be a first and make us very rich indeed!"
menu:
    "Hang on a minute, who says I want to bang your ugly green broad?":
        hide alienmale01
        show alienmale04 at left
        hide alienfemale02
        show alienfemale01 at right
        with fastdissolve
        alm "How dare you refuse to have sex with Miss Glorglon 42066825! AND 42066827 two years later!"
        alm "This will teach you to respect the beauty of our superior species, insolent human specimen!"
        window hide
        show alienshoot
        play sound "Sounds/raygun.mp3"
        pause 0.5
        hide alienshoot
        $ mcinjuredalien = True         
        mc "Hey, stop it, it fucking hurts!"
        window hide
        show mcinjured at injured
        $ renpy.pause(2.0, hard=True)
        hide mcinjured
        if mcinjured:
            mc "AGAIN!"
        $ mcinjured = True
        hide alienmale04
        show alienmale02 at left
        with fastdissolve
        alm "Now shut up and get on with it. Glurglub will assume the insemination position and you will stick your semen pole all the way up her baby hole."
        mc "I don't think it will work, if you have in mind what I think you have in mind, but whatever, I'll do it."
        jump AlienSex
    "Do I get a cut in this?":
        hide alienmale01
        show alienmale03 at left
        with fastdissolve
        alm "Ah, ah, sure. I'll send you some Glorglonubs via GlorglonPal, tons of it. It's worth jackshit on your pitiful planet of course..."
        mc "Ah, shit, I hadn't thought about that..."
        hide alienfemale02
        show alienfemale03 at right
        hide alienmale03
        show alienmale02 at left
        with fastdissolve
        alm "Now shut up and get on with it. Glurglub will assume the insemination position and you will stick your semen pole all the way up her baby hole."
        mc "I don't think it will work, if you have in mind what I think you have in mind, but whatever, I'll do it."
        jump AlienSex
    "Of course, oh Lord Master of our Galaxy.":
        hide alienfemale02
        show alienfemale03 at right
        with fastdissolve
        alf "I like this human specimen, my glorglaries are all tingly."
        hide alienmale01
        show alienmale02 at left
        with fastdissolve
        alm "Good, this will work even better then."
        alm "Glurglub will assume the insemination position and you will stick your semen pole all the way up her baby hole."
        mc "I don't think it will work, if you have in mind what I think you have in mind, but whatever, I'll do it."
        jump AlienSex

label AlienSex:        
scene aliens04 with dissolve
show mcalien01
mc "Err, it that the insemination position?"
alf "No, that's the gloggy position silly. I'm just priming my glorglaries..."
alm "Stick it as far up up her stomach as you can, I want to see a baby bump in there, understood inferior species?"
mc "Sure..."
alm "My VHS camera is ready. You can fuck her now, pitiful human!"
scene aliens04 with dissolve
play music "Sounds/aliensex.mp3"
call screen mcalien
screen mcalien:
    add aliensex at center
    modal True
    button:
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("McAlienEnd")    
        
label McAlienEnd:
stop music
scene aliens05
show aliencum
with dissolve
alf "YES, fill me up! Give me an intergalactic baby!!!"
alm "Don't stop shooting inside her, she needs billions and billions of tiny babies to grow inside her so we can repopulate the universe!"
mc "Shit, you guys are CRAY-AY-ZYYYY..."
scene aliens04
show aliencumend
with dissolve
mc "Fuck... I've nutted as much seed as I could... I'm empty."
alf "I can feel my multi-billion eggs getting inseminated by this inferior specimen my fierce Glorglob!"
alm "Great, it worked! I knew it, that's why we are the most intelligent species in the galaxy!"
mc "The CRAY-AY-ZIEST species you mean..."
alm "Shut up insolent human! Now stand up and cover your mammoth appendage, it's vulgar."

label DesertAliens04:
scene aliens02
show alienmale02 at left
show alienfemale01 at right
with dissolve
alm "You did well human specimens. Now we can go back to our planet and show our fellow Glorglans this videotape."
hide alienfemale01
show alienfemale04 at right
with fastdissolve
alf "But we need more porn. Here's a high-tech mini-VHS camera. Install it in your lair and send us at least one porn video clip each Glorglan day."
hide alienmale02
show alienmale01 at left
with fastdissolve
alm "Or we'll come back and destroy your useless planet!"
mc "Hang on a minute. Each \"Glorglan\" day? What does that mean?"
hide alienfemale04
show alienfemale03 at right
with fastdissolve
alf "I guess that's about one of your pitiful weeks. Don't forget to send us some hot clips!"
hide alienmale01
show alienmale04 at left
with fastdissolve
alm "And not some crazy German shit-eating porn by the way, we hate those. I'll come back and kill you this time if you do this!"
mc "Right... Well, thanks for dropping by on our planet and not destroying it. (Assholes)."
hide alienmale04
show alienmale01 at left
with fastdissolve
alm "We'll go right back to Glorglon now, the foul pure air on this planet is unbearable! Come, my beauty Glurglub."
hide alienmale01
hide alienfemale03
mc "God I hate aliens."
if withbe:
    be "It didn't look like it while you were fucking that alien female..."
    be "Let's get back to the compound, I've seen enough... sinful behavior for the day."
    jump BackHex02
if withpe:
    pe "That's something you have in common with President Trumpf then!"
    pe "Let's get back to the compound, and probably never speak of this again."
    jump BackHex02

label BackHex02:
$ period += 1
scene command01 with fade
show lena01
le "So, what do you have to report about area A2, scouts?"
mc "Nothing out of the ordinary Chief."
if mcinjured:
    mc "Except I hurt myself.... err... slipping on some rocks."
if withbe:
    be "Right. Nothing really..."
if withpe:
    pe "I concur. Not even a camel this time. No earthly life form at all..."
hide lena01
show lenapensive
with fastdissolve
le "Hum... Maybe it's time to explore further then...."
hide lenapensive
show lena06
with fastdissolve
le "Dismissed scouts!"
if mcinjured:
    le "And you, [name], go to the medical bay for a checkup on that injury."
    mc "Sure thing boss!"
    mc "*Before that I should go and install that mini-VHS camera in my bedroom just in case..."
hide lena06
mc "I should go and install that mini-VHS camera in my bedroom just in case..."
if mcinjured:
    jump Medbay
jump Bedroom

label ExploreHex03:
$ explored = True
$ exploredhex03 = True
stop sound
stop music
scene oasis01
show oasisnomadidle
show oasiszaraidle
show oasiscamelidle
with fade

if missionza or missionza02:
    jump OasisZara
mc "Oh, there's an oasis behind that hill. And some people around a tent."
if withbe:
    be "Umpf... They look like nomads. Chief Lena doesn't want any more people in the compound, we are already saturated."
if withpe:
    pe "We need this place cleared up, water is a scarce ressource."
mc "Let's see what they are up to..."
if persistent.tipson:
    show hex03tip at tips with dissolve
    pause
    hide hex03tip
label Oasis01b:
scene oasis01
$ metza = True
call screen oasis
screen oasis:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/exitidle.png"
        hover "Icons/exithover.png"
        action Jump ("LeaveOasis")
    imagebutton:
        focus_mask True
        idle "oasis/oasistentidle.png"
        hover "oasis/oasistenthover.png"
        action Jump ("OasisTent")
    imagebutton:
        focus_mask True
        idle "oasis/oasisnomadidle.png"
        hover "oasis/oasisnomadhover.png"
        action Jump ("OasisNomad")
    imagebutton:
        focus_mask True
        idle "oasis/oasiszaraidle.png"
        hover "oasis/oasiszarahover.png"
        action Jump ("OasisZara")
    imagebutton:
        focus_mask True
        idle "oasis/oasiscamelidle.png"
        hover "oasis/oasiscamelhover.png"
        action Jump ("OasisCamel")
        
label OasisCamel:
show oasiscamelidle
show oasiszaraidle
show oasisnomadidle
mc "It's a camel. Looks pretty healthy to me. I'm starting to get hungry."
jump Oasis01b

label OasisTent:
show oasiscamelidle
show oasiszaraidle
show oasisnomadidle
mc "A comfortable nomad tent with all the modern amenities. Except toilets."
jump Oasis01b

label OasisZara:    
hide oasisnomadidle
hide oasiszaraidle
show oasiscamelidle
if missionza or missionza02:
    show zaragreet at midright
    show nomadgreet at midleft
    no "So, do you have enough camels fellow traveller?"
    if camels >= 4 and missionza:
        mc "Yep, I have the four camels you asked for!"
        $ camels -= 4
        jump ZaraLeave
    if camels >= 6 and missionza02:
        mc "Yep, I have the six camels you asked for!"
        $ camels -= 6
        jump ZaraLeave
    if (camels <= 3 and missionza)  or (camels <= 5 and missionza02):   
        mc "Not yet. But I'm working on it."
        hide zaragreet
        show zarasad at midright
        hide nomadgreet
        show nomadne at midleft
        no "Well, it was a bit of a waste of time coming back here then, my friend..."
        mc "I just wanted to see your daughter again..."
        no "Well, you've seen her. Now leave and come back with the camels I need if you want her!"
        mc "Alright, alright. Gee, what a pushy man."
        jump OasisOut03
    

show nomadgreet at center
no "Hello strangers! Who are you? We don't want any trouble. And we are armed in case you're looking for trouble."
menu:
    "Fear not old man, we come in peace. We just want to know what you are doing here.":
        if withpe:
            hide nomadgreet
            show nomadan
            no "Who is that woman with you? I recognize that tattoo... You are Road Warriors! Zara, get the guns!"
            menu:
                "Hang on a minute, I'm not a road warrior! She's with me, but she'll leave and won't cause any trouble." if mcwarrior <= 4:
                    hide nomadan
                    jump Nomad01
                "Yes we are, and that camel of yours is now ours! (+1 Road Warriors)" if mcwarrior == 5:
                    no "I knew it! We shall never trust a human being who looks like a total wanker like you again in our lives!"
                    mc "Hey, watch your language old man! Or I'll take more than one camel..."
                    pe "Let's just leave them to die, the Road Warrior way. And take that camel. We'll go back to the compound now, it's getting late."
                    $ camels += 1
                    $ stolecamel = True
                    $ clearedhex03 = True
                    call PlusWarrior
                    jump BackHex03
        label Nomad01:
        hide nomadgreet
        show nomadne
        no "We are nomads. We were attacked by road warriors and they killed most of our camels."
        mc "That's terrible. But that chick with me? She's not really with them, we're from the Resistance Compound down south."
        no "My daughter and I are strangers to your political bickerings. We just want to survive and move to a better place."
        no "But we can't right now, we don't have enough camels. Zara, make some tea for our guest!"
        no "Please accept my hospitality and join me in our tent."
        menu:
            "I really should be going...":
                no "It is very rude to refuse the hospitality of nomads! I am offended. Please leave at once and never come back."
                jump OasisOut03
            "With pleasure fellow traveller.":
                if withbe:
                    be "I'll stay next to my truck for safety. You deal with them [name]."                    
                jump Nomad02
    "I just wanted to talk to that hot chick over there.":
        hide nomadgreet
        show nomadne
        no "That \"hot chick\", as you call her, happens to be my lovely daughter Zara!"
        mc "Well, you should be proud of her then, cos she's smoking hot."
        no "If you think so, then I have a deal for you. I'll sell her to you for 6 camels."
        menu:
            "Hang on a minute, doesn't she have a say in this?":
                no "She understands, this is the way of the nomads."
                no "But why don't we talk about it in my tent. Zara wil make us a delicious tea."
                mc "Err... Alright."
                jump Nomad02
            "Deal!":
                hide nomadne
                show nomadgreet
                no "Come back with 6 camels stranger, and she is yours..."
                window hide
                show missionza02 at posmission
                $ renpy.pause(4.0, hard=True)
                hide missionza02
                $ missionza02 = True
                jump OasisOut01
                                    
label OasisNomad:
hide oasisnomadidle
show oasiszaraidle
show oasiscamelidle
show nomadgreet
no "Hello strangers! I hope you come in peace, we are travelling nomads and we don't want any trouble."
menu:
    "Fear not old man, we come in peace. We just want to know what you are doing here.":
        if withpe:
            hide nomadgreet
            show nomadan
            no "Who is she? I recognize that tattoo... You are Road Warriors! Zara, get the guns!"
            menu:
                "Hang on a minute, I'm not a road warrior! She's with me, but she'll leave and won't cause any trouble." if mcwarrior <= 4:
                    jump Nomad01b
                "Yes we are, and that camel of yours is now ours!" if mcwarrior == 5:
                    no "I knew it! We shall never trust a human being who looks like a total wanker like you again in our lives!"
                    mc "Hey, watch your language old man! Or I'll take more than one camel..."
                    pe "Let's just leave them to die, the Road Warrior way. And take that camel. We'll go back to the compound now, it's getting late."
                    $ camels += 1
                    $ stolecamel = True
                    call PlusWarrior
                    $ clearedhex03 = True
                    jump BackHex03            
            label Nomad01b:
            hide nomadan
            show nomadne
            no "We are nomads. We were attacked by road warriors and they killed most of our camels."
            mc "That's terrible. But that chick with me? She's not really with them, we're from the Resistance Compound down south."
            no "My daughter and I are strangers to your political bickerings. We just want to survive and move to a better place."
            no "But we can't right now, we don't have enough camels. Zara, make some tea for our guest!"
            hide nomadne
            show nomadan
            no "Please accept my hospitality and join me in our tent."
            menu:
                "I really should be going...":
                    no "It is very rude to refuse the hospitality of nomads! I am offended. Please leave at once and never come back."
                    jump OasisOut03
                "With pleasure fellow traveller.":
                    if withbe:
                        be "I'll stay next to my truck for safety. You deal with them [name]."
                    jump Nomad02
        hide nomadgreet
        show nomadne
        no "We were attacked by a pack of filthy road warriors and sought refuge in this quiet place. They stole most of our camels..."
        no "We hope to be moving on soon once we find some more camels."
        hide nomadne
        show nomadan
        no "Please accept my hospitality stranger and come into my tent where my daughter Zara will serve tea."
        menu:
            "I don't have time to waste sipping tea. Give me that healthy looking camel or else... (+1 Road Warriors)":
                no "What? This is the only camel we have left, you will leave us to die here?"
                mc "I'm sure you'll find a way out of your predicament. Not my problem anyway. Just give us the camel and we'll leave."
                show zarasad at farright
                za "I think it's best we do as this horrible man says father... We'll find a way out if this..."
                mc "The hot chick can come with us too..."
                if withbe:
                    be "No she can't! I told you Chief Lena doesn't want anyone else in the compound. Especially girls."
                    mc "Alright, alright. We'll take the camel then and you get to keep the smoking hot chick lucky man! (wink)"
                    no "She's my daughter you dumb fuck!"
                    mc "No need to get all personal old man... What you do with her is none of my business."
                    be "Leave them here and let's go back to the compound with that camel then."
                if withpe:
                    pe "Let's just leave them to die, the Road Warrior way. And take that camel."
                    mc "Wow, that's harsh. But it is the Road Warrior way, so agreed."
                    pe "Let's go back to the compound with that camel then."
                $ camels += 1
                $ stolecamel = True
                $ clearedhex03 = True
                call PlusWarrior
                jump BackHex03
            "With pleasure fellow traveller":
                jump Nomad02
    "You don't want any trouble? Give us that camel you have and we won't give you any trouble... (+1 Road Warriors)":
            hide nomadgreet
            show nomadan
            no "What? You would take our last belongings and leave us to die like dogs?"
            mc "You can walk. We need that camel to feed the Resistance, so don't do anything silly or else..."
            show zarasad at farright
            za "I think it's best we do as this horrible man says father... We'll find a way out if this..."
            mc "The hot chick can come with us too..."
            if withbe:
                be "No she can't! I told you Chief Lena doesn't want anyone else in the compound. Especially girls."
                mc "Alright, alright. We'll take the camel then and you get to keep the smoking hot chick lucky man! (wink)"
                hide zarasad
                show zaragreet at farright
                no "She's my daughter you dumb fuck!"
                mc "No need to get all personal old man... What you do with her is none of my business."
                be "Leave them here and let's go back to the compound with that camel then."
            if withpe:
                pe "Let's just leave them to die, the Road Warrior way. And take that camel."
                mc "Wow, that's harsh. But it is the Road Warrior way, so agreed."
                pe "Let's go back to the compound with that camel then."
            $ camels += 1
            $ stolecamel = True
            call PlusWarrior
            $ clearedhex03 = True
            jump BackHex03                

label Nomad02:
scene oasistent01 with dissolve
no "Please, enjoy this tea made by my lovely daughter Zara. Isn't she beautiful?"
menu:
    "Yes, she is stunning indeed.":
        scene oasistent02
        call LustPlusZara 
        no "I'm glad you think so. I have little time left on this Earth and it is time for her to find a man."
        label Nomad02b:
        scene oasistent02
        no "I'll sell her to you for 6 camels."
        menu:
            "What? I ain't buying a woman like that in exchange of camels!":
                scene oasistent03
                no "Why not? This is the way of the nomads. She knows it, she will accept it."
                menu: 
                    "No way! I have my moral standards even if this is a harem porn game!":
                        scene oasistent04
                        no "Too bad. Then we have no more business to talk about. Finish your tea and leave fellow traveller..."
                        jump OasisOut03
                    "Ok, but I ain't paying that much for her":
                        no "A haggler are we? Alright. 4 camels then."
                        mc "It's a deal! I'll come back with four camels and pick her up."
                        window hide
                        show missionza at posmission
                        $ renpy.pause(4.0, hard=True)
                        hide missionza
                        $ missionza = True
                        jump OasisOut01                
            "6 camels huh? She's a 7 tops. Not even sure Trump would grab her by the pussy. Barely worth 2 camels I'd say.":
                scene oasistent03
                call LustMinusZara                    
                no "A haggler are we? Alright. 4 camels then."
                mc "It's a deal! I'll come back with four camels and pick her up."
                window hide
                show missionza at posmission
                $ renpy.pause(4.0, hard=True)
                hide missionza
                $ missionza = True
                no "Great. We'll be waiting for you. I bid you farewell fellow traveller."
                jump OasisOut01                
            "She's butt ugly really. Let's talk about that camel you have left. I want it. (+1 road warriors)":
                scene oasistent04
                no "What? I invite you into my tent, you insult my lovely daughter and now you want to steal my camel?"
                mc "Well, it's a tough world old man. Do as you're told and move on and nothing will happen to you."
                za "Father, you'd better do as this horrible man asks. He looks very... strong and dangerous."
                no "I will never trust another human being in my life! Fine, take my last camel and leave us to die asshole!"
                mc "No need to get all personal old man. It's just the way of the...err.. road warriors."
                no "I knew it! You are a fucking Road Warrior after all! You tricked us!"
                $ camels +=1
                $ stolecamel = True
                call PlusWarrior
                mc "Well, duh. Yeah."
                jump OasisOut02
    "She's okay. A 7 tops. Not sure even Trumpf would grab her by the pussy.":
        scene oasistent02
        no "Oh come on now, you made her sad. And I was going to propose a deal to you..."
        mc "What deal?"
        no "I'll sell her to you for four camels."
        menu:
            "What? I ain't buying a woman like that in exchange of camels!":
                scene oasistent03
                no "Why not? This is the way of the nomads. She knows it, she will accept it."
                mc "No way! I have my moral standards even if this is a harem porn game!"
                scene oasistent04
                no "Too bad. Then we have no more business to talk about. Finish your tea and leave fellow traveller..."
                jump OasisOut03
            "4 camels huh? Barely worth 2 camels I'd say.":
                scene oasistent03
                no "I can't go below 4 camels. A 7 is worth 4 camels, that's the going rate and you said she was a 7."
                mc "Alright. I'll come back with four camels and pick her up."
                window hide
                show missionza at posmission
                $ renpy.pause(4.0, hard=True)
                hide missionza
                $ missionza = True
                no "Great. We'll be waiting for you. I bid you farewell fellow traveller."
                jump OasisOut01                
            "She's butt ugly really. Let's talk about that camel you have left. I want it. (+1 road warriors)":
                scene oasistent04
                no "What? I invite you into my tent, you insult my lovely daughter and now you want to steal my camel?"
                mc "Well, it's a tough world old man. Do as you're told and move on and nothing will happen to you."
                za "Father, you'd better do as this horrible man asks. He looks very... strong and dangerous."
                no "I will never trust another human being in my life! Fine, take my last camel and leave us to die asshole!"
                mc "No need to get all personal old man. It's just the way of the...err.. Road Warriors."
                no "I knew it! You are a fucking Road Warrior after all! You tricked us!"
                $ camels +=1
                $ stolecamel = True
                call PlusWarrior
                mc "Well, duh. Yeah."
                jump OasisOut02

label ZaraLeave:
hide nomadgreet
show nomadne at midleft
no "They look healthy. Now I'll be able to leave this place. Thank you young man."
mc "Err... If I remember correctly, your daughter is supposed to come with ME."
no "Ah yes, I almost forgot. Please take good care of her."
mc "I sure will..."
call LustPlusZara
play music "Sounds/farewell.mp3"
scene oasis01 blurred
show oasiscamelidle blurred
show zaraleave with dissolve
no "Darling Zara, your father must leave you. Join this man's harem, he seems strong and will give you healthy babies."
za "But father, I don't want to leave you..."
no "I sold you for some healthy camels, I cannot go back on my promise. Farewell, my sweet Zara, salam alikoum!"
za "Inch'Allah father. I will miss you. I pray that you will find your way to our tribe safe and sound."
no "Do not worry my sweet little girl. I will travel the four corn..."
stop music
mc "Now come on Zara, come with me, this is taking too long. I'll show you the compound, I'm sure you'll love it. It's way better than this dump."
scene oasis01
show oasiscamelidle
show nomadne at midleft
show zaragreet at midright
za "Ok, I'm coming. This was getting too boring, I agree."
$ clearedhex03 = True
$ missionza = False
$ missionza02 = False
$ haremza = True
$ zaraharem = True
$ girlsinharem += 1
window hide
show haremzara at plus
$ renpy.pause(2.0, hard=True)
hide haremzara
hide zaragreet
hide nomadne
hide oasiscamelidle
jump ZaraMissionOut

label ZaraMissionOut:
if withbe:
    show bellaout05 with dissolve
    be "Umpf... I can't say I'm particularly happy about this new girl you're bringing to the compound..."
    call LustMinusBella
    mc "She'll be useful to me and to our cause. In many ways..."
if withpe:
    show pennyout03 with dissolve
    pe "I don't have enough room on my rig for her..."
    mc "She'll sit on my lap..."
    pe "If she falls off, don't blame me..."
jump BackHex03

label OasisOut01:
scene oasis01 with dissolve
if withpe:
    pe "I hope you were stern with them and they will leave. We need this place cleaned up, it's a good source of water."
    mc "Err... No, I mean, yes, but we have to find some camels first for them."
    pe "What? That is so disappointing of you, you'll never become a road warrior with that kind of attitude!"
    call MinusWarrior
    pe "Let's go back to the compound..."
    jump BackHex03 
if withbe:
    show bellaout03
    be "These people look... strange. They dress up like they worship another God. I think they are Islamo-nucleorists, I heard about these heretics, I hope you were harsh with them!"
    mc "Now, come on, we should be tolerant of other people's faith. Right?"
    hide bellaout03
    show bellaout05
    be "That is definitely NOT what the Church teaches us..."
    call MinusChurch
    be "Let's go back to the compound..."
    jump BackHex03   

label OasisOut02:
scene oasis01 with dissolve
$ clearedhex03 = True
if withpe:
    pe "I hope you were stern with them and they will leave. We need this place cleaned up, it's a good source of water."
    mc "Yep. All sorted out. And I stole their camel."
    pe "Nice...Let's go back to the compound now..."
    jump BackHex03
if withbe:
    show bellaout01
    be "These people look... strange. They dress up like they worship another God. I think they are Islamo-nucleorists, I heard about these heretics! I hope you were harsh with them."
    mc "I sure was. Stole their camel just like we used to steal their oil in the good old days."
    hide bellaout03
    show bellaout01
    be "I see. I can't remember reading that theft was approved in the Brand New Testament, but I'll check on it."
    be "Let's go back to the compound now..."
    jump BackHex03

label OasisOut03:
scene oasis01 with dissolve
if withpe:
    pe "I hope you were stern with them and they will leave. We need this place cleaned up, it's a good source of water."
    mc "Err... Sure, yeah, I told them to piss off."
    pe "Somehow, I don't believe you... You'll never become a road warrior with that kind of attitude."
    call MinusWarrior 
    pe "Let's go back to the compound..."
    jump BackHex03
if withbe:
    show bellaout03
    be "These people look... strange. They dress up like they worship another God. I think they are Islamo-nucleorists, I heard about these heretics, I hope you were harsh with them!"
    mc "Now, come on, we should be tolerant of other people's faith. Right?"
    hide bellaout03
    show bellaout05
    be "That is definitely NOT what the Church teaches us..."
    call MinusChurch
    be "Let's go back to the compound..."
    jump BackHex03
 
label LeaveOasis:
mc "Let's leave, I smell a rat..."
if withbe:
    be "What? We just arrived! You are such a coward..."
if withpe:
    pe "What? We just arrived! You are such a coward..."
jump BackHex03
 
label BackHex03:
$ period += 1
scene command01 with fade
show lena01
le "So, what do you have to report about area A3, scouts?"
if haremza == True:
    mc "The area has been cleared Chief! No more nomads around, the oasis is ours!"
    hide lena01
    show lena07
    le "What a pleasant surprise. Now we can move on and stop wasting our time exploring that area then..."
    hide lena07
    show lena06
    le "You are dismissed scouts!"
    hide lena06
    jump LeaveCommand
if missionza == True or missionza02 == True:
    mc "We found some nomads near an oasis and err....They'll leave soon as soon as I go back to tell them to piss off."
    hide lena01
    show lena10
    le "What? That were not your orders! You HAVE to clear areas so we can move onto other areas!"
    mc "Ah, I get it now. Thanks for clearing that up Chief."
    hide lena10
    show lena06
    le "God you're thick sometimes [name]. Scouts dismissed!"
    hide lena06
    jump LeaveCommand
if stolecamel:
    mc "We found some nomads near an oasis and cleared the area Chief! And we got a live camel out of the deal too!"
    hide lena01
    show lena07    
    le "Fine, one less place to explore then. We'll move to the next one another day. You are dismissed scouts!"
    mc "Err... What about my money for the camel?"    
    hide lena07
    show lena05
    le "Right. Here's 10 new dollars. Please don't bring back any more camels... Especially live ones."
    $ money += 10
    hide lena05
    $ zaralost = True
    jump LeaveCommand
mc "We found some nomads near an oasis and err....They'll leave soon as soon as I go back to tell them to piss off."
hide lena01
show lena10
le "What? That were not your orders! You HAVE to clear areas so we can move onto other areas!"
mc "Ah, I get it now. Thanks for clearing that up Chief."
hide lena10
show lena06
le "God you're thick sometimes [name]. Scouts dismissed!"
hide lena06
jump LeaveCommand

label ExploreHex11:
$ explored = True
$ exploredhex11 = True
scene desert02 with fade
stop sound
mc "Nothing... AGAIN."
if persistent.tipson:
    show hex04tip at tips with dissolve
    pause
    hide hex04tip
show inquisitorfar with dissolve
mc "Hang on, I see some people over there coming our..."
hide inquisitorfar
show inquisitorgirls01
show inquisitor02 with fastdissolve
mc "..way. Damn, that was quick!"
sp "In the name of the Holy Church of the Redeeming Phallus, thou shalt not pass until thou provest to us that thou arst not heretics!"
mc "And who are you to give orders here?"
sp "We arst..."
window hide
play sound "Sounds/dundun.mp3"
pause 2.0
sp "...the Spanish Inquisition!"
hide inquisitor02
show inquisitor01
sp "Ah ah, you weren't expecting me to say that, did you?"
mc "I expect just about anything in this crazy game."
hide inquisitor01
show inquisitor03
sp "What? But NOBODY expects the Spanish Inquisition! Tell me you weren't expecting us pretty please!"
mc "Ok, ok, I wasn't expecting you. There, happy?"
hide inquisitor03
show inquisitor02
sp "Ah ah, indeed. Nobody expects the Spanish Inquisition! NOBODY!"
window hide
play sound "Sounds/dundun.mp3"
pause 2.0
hide inquisitor02
show inquisitor01
sp "Now. I shalt inspect thee to find out whether thou arst heretics or not."
if withbe:
    be "I am a fervant member of the Church your Eminence! Oh, how I worship thy Penis Oh Lord!"
    sp "Yeah, Ok, no need to get all sexual about this, I am meant to be a holy man after all."
sp "So, young man, are you a member of the Church?"
if churchbaptized and mcchurch >= 2:
    mc "I'm baptized, yes."
    sp "Ah good. Then I shalt not have to punish you with..."
    window hide
    play sound "Sounds/dundun.mp3"
    pause 2.0
    sp "The comfy chair..."    
    mc "Gee, lucky me."
    if withpe:
        sp "And you, young woman?"
        pe "I certainly am NOT a member of your pathetic religion! I am a Road Warrior and the Master of my own Destiny!"
        if churchbaptized:
            mc "So basically, she's a heretic, and I'm not. So get onto her, not me!"
            pe "What? You are such a lousy coward [name]!"
            call LustMinusPenny      
            sp "Yeah, but I don't like picking on women. And she looks tough so..."
            jump InquisitorJump
    sp "Err, do you guys know any heretics around her? We're kind of tired of meeting only people who tell us they are members of the Church and we haven't used our comfy chair yet."
    mc "Err. No, sorry."
    sp "What a bummer. OK, let's go, these non-heretics shalt be allowed to pass amidst ourst mist. Or something like that."
    hide inquisitor01
    $ clearedhex11 = True
    jump BackHex11

mc "What church?"
hide inquisitor01
show inquisitor02
sp "Clearly, you are a HERETIC!"
mc "I am a HERO, that's what I am and I'll prove it Cardinal My-Ass!"
label InquisitorJump:
hide inquisitor01
hide inquisitor02
show inquisitor03
if withpe:
    sp "We shall battle it out young man, the power of the Mighty Penis is on my side anyway! And I get to choose our weapons, in accordance with the Road Warrior Code, right?"
    pe "That is correct."
if withbe:
    sp "Then we shall battle it out, the power of the Mighty Penis is on my side anyway! And I get to choose our weapons, in accordance with the Church's Teachings!"
    be "I agree, that's what the Church says, you have no choice [name]."
sp "And I choose..."
window hide
play sound "Sounds/dundun.mp3"
pause 2.0
hide inquisitor03
show inquisitor02
sp "...The soft cushion! The weapon of choice of the Spanish Inquisition! Ah ah, I can read the fear in your eyes young man, right?"
mc "Not really. Even if you win, I'll barely get injured."
sp "We shalt see! En garde!"

label SpanishFight:
hide screen mcstats
hide screen calendar
$ spanishfirst = True    
scene desert02
show mcfightout01b at farleft
show inquisitorfight02 at farright03
with dissolve
$ mc_health = 2.0
$ inquis_health = 2.0
show screen screenfightmcinquis

label SpanishRound:
if spanishfirst:
    jump RoundSpanishFight
if spanishfirst == False:
    jump RoundMCSpanishFight

label RoundSpanishFight:  
sp "Soft Cushion Attack Wheel!"
window hide
show inquisitorfight02 at farright with movefast
hide inquisitorfight02
show inquisitorfight03 at farright
show inquisitorfight03 at farright02 with movefast
hide inquisitorfight03
show inquisitorfight04 at farright02
show inquisitorfight04 at centerright with movefast
hide inquisitorfight04
show inquisitorfight05 at centerright
show inquisitorfight05 at center with movefast
window hide
call DiceRoll
if diceroll >= 4:
    hide mcfightout01b
    hide inquisitorfight05
    show inquisitorfight02
    show mcpillowhit at farleft
    with fastdissolve
    play sound "Sounds/punch.mp3"
    sp "I just hit you VERY HARD with a SOFT cushion! I bet it hurts a LOT!"
    $ counting = 0
    while counting < 20:
        $ mc_health -= 0.05
        $ counting += 1
        pause 0.01
    if mc_health >= 0.1:
        mc "Not really, I'm just barely injured."
    if mc_health <= 0:
        hide mcpillowhit
        hide inquisitorfight02
        show mcyieldout at farleft
        show inquisitorfight01
        with fastdissolve
        sp "The Phallus Lord gave you a mighty spanking!"
        mc "Alright, I yield. Damn, I didn't know a soft cushion could hurt that much. My head is spinning."
        call MCInjury
        $ mcinjuredfight = True
        jump SpanishWinFightEnd        
    hide inquisitorfight02
    hide mcpillowhit
    show mcfightout01b at farleft
    show inquisitorfight02 at farright03
    with fastdissolve
if diceroll <= 3:
    hide mcfightout01b
    hide inquisitorfight05
    show inquisitorfight02
    show mcpillowdodge at farleft
    with fastdissolve
    play sound "Sounds/punch.mp3"
    mc "Didn't hurt a bit."
    sp "Be damned! These cushions are just not soft enough!"
    hide inquisitorfight02
    hide mcpillowdodge
    show mcfightout01b at farleft
    show inquisitorfight02 at farright03
    with fastdissolve
$ spanishfirst = False
jump SpanishRound

label RoundMCSpanishFight:  
mc "Catch, Cardinal My-Butt!"
window hide
hide mcfightout01b
show mcfightout02b at farleft
show mcfightout02b at left with movefast
hide mcfightout02b
show mcfightout03 at left
with fastdissolve
call DiceRoll
$ dcombatroll=mccombat+diceroll        
if (dcombatroll >= 5 and not diceroll == 1) or diceroll == 6:
    window hide
    hide mcfightout03
    show mcfightout03b at left
    show cushion at left
    with fastdissolve
    hide cushion
    show cushion at farright with movefast
    hide inquisitorfight02
    show inquisitorfight07 at farright03
    with fastdissolve
    play sound "Sounds/punch.mp3"
    mc "Take that!"
    if inquis_health >= 0.1:
        sp "Ouch! But my sins have already been forgiven, so it doesn't hurt as much!"
    $ counting = 0
    while counting < 20:
        $ inquis_health -= 0.05
        $ counting += 1
        pause 0.01
    if inquis_health <= 0:
        sp "Ouch! Please stop hitting me with this awfully soft cushion, I yield!"
        jump SpanishFightWin
    hide cushion
    hide mcfightout03b
    hide inquisitorfight07
    show mcfightout01b at farleft
    show inquisitorfight02 at farright03
    with fastdissolve
if (dcombatroll <= 4 and not diceroll == 6) or diceroll == 1:
    window hide
    hide mcfightout03
    show mcfightout03b at left
    show cushion at left
    with fastdissolve
    hide inquisitorfight02
    show inquisitorfight06 at farright03
    show cushion at left
    with fastdissolve
    hide cushion with moveoutright
    with fastdissolve
    sp "Missed! The Phallus Lord protects me!"
    hide inquisitorfight06
    hide mcfightout03b
    show mcfightout01b at farleft
    show inquisitorfight02 at farright03
    with fastdissolve
$ spanishfirst = True
jump SpanishRound   

label SpanishWinFightEnd:
hide screen screenfightmcinquis
show screen mcstats
show screen calendar
scene desert02
show inquisitorgirls01
show inquisitor02 with fastdissolve
sp "The Spanish Inquisition hereby bans you from this place on the charge of heresy and aposta..."
hide inquisitor02
show inquisitor03
with fastdissolve
sp "Hang on, I'll start over again."
hide inquisitor03
show inquisitor02
with fastdissolve
sp "The Spanish Inquisition hereby bans you from this place on the TWO charges of heresy, apostasy and a lack of devotion to the Ch...."
hide inquisitor02
show inquisitor03
with fastdissolve
sp "...Oh, bugger! Just go. You're banned."
$ spanishdefeated = True
jump BackHex11

label SpanishFightWin:
hide screen screenfightmcinquis
show screen mcstats
show screen calendar
scene desert02 with dissolve
show inquisitor03
sp "Alright, I give up... You win. The Phallus Lord must have meant it to be..."
mc "The Phallus Lord is always on my side!"
$ clearedhex11 = True
$ inquisitorwin = True
if withbe:
    be "You... beat up His Eminence. I can't believe it..."
    call LustMinusBella
    be "I need to go back to the Compound and repent my sins!"
    jump BackHex11
if withpe:
    pe "Nice one [name], you gave it to him good. Let's go back to the compound and report that this area has been cleared."
    call LustPlusPenny
    jump BackHex11    

label BackHex11:
$ period += 1
scene command01 with fade
show lena01
le "So, what do you have to report about area B1, scouts?"
if spanishdefeated:
    mc "I was violently assaulted by a soft cushion I wasn't expecting."
    hide lena01
    show lena03
    with fastdissolve
    le "..."
    le "I am speechless."
    mc "I'll see myself out, Chief. And I'll check myself into the medbay."
    $ spanishdefeated = False
    jump Medbay    
mc "Some inquisitor from the Church of the Redeeming Phallus."
hide lena01
show lenapensive
le "Damn, even in the middle of the desert, we are not safe from these lunatics!"
if mcchurch >= 4:
    mc "Hey, watch what you're saying Cheif Lena! Blasphemy against the Holy Church is punishable by... err... cock-choking."
if withbe:
    be "Chief, I remind you that the Phallus Lord is watching down over ALL of us! With his mighty one-eye."
    hide lenapensive
    show lena03
    le "Yeah, yeah, I get it. Sorry if I offended you... You can go now, you are dismissed scouts."
    hide lena03
    jump LeaveCommand
if withpe:
    pe "But he got what was coming to him at the end...."
    hide lenapensive
    show lena07
    le "Good, then this area is cleared. You are dismissed scouts!"
    hide lena07
    jump LeaveCommand

label ExploreHex12:
$ explored = True
$ exploredhex12 = True
stop sound
scene mesa01
if withbe:
    show bellaoutback
if withpe:
    show pennyoutback
with fade
mc "Nothing again..."
if withbe:
    hide bellaoutback
    show bellaout09
    be "Don't say that until we've confirmed it. Pass me the binoculars..."
    mc "Well, I'll go and rest on that rock over there while you watch for nothing..."
    be "Then watch the rig. I'll go and do MY duty as a scout while you \"rest\"..."
    hide bellaout09 with moveoutright
if withpe:
    hide pennyoutback
    show pennyout03
    pe "Don't say that until we've confirmed it. Pass me the binoculars..."
    mc "Well, I'll go and rest on that rock over there while you watch for nothing..."
    pe "Then watch the rig. I'll go and do MY duty as a scout while you \"rest\"..."
    hide pennyout03 with moveoutright

scene mesa02
mc "Boring..."
scene mesa03
mc "Hang on, what's that? It looks like a lamp of some kind."
mc "Maybe I should rub it, this world is crazy enough that a genie might pop out of..."
scene mesa04
show geniesmoke with dissolve
play sound "Sounds/smokepuff.mp3"
$ renpy.pause(0.5, hard='True')
hide geniesmoke
show genie01 with dissolve
ge "Finally, someone let me out of this fucking stinking lamp!"
mc "Are... Are you a genie?"
hide genie01
show genie02 with fastdissolve
ge "What does it look like fartbrains? Of course I'm a genie!"
mc "Well... err... Usually genies are a bit more polite than that."
hide genie02
show genie03 with fastdissolve
ge "That's bullshit! You try and stay for twelve centuries in a tiny lamp like I did and you come back to me!"
mc "Ok, Ok. So, aren't you going to grant me three wishes then?"
hide genie03
show genie02 with fastdissolve
ge "Three wishes? Are you out of your fucking mind?"
mc "Well, that's standard, right?"
hide genie02
show genie04 with fastdissolve
ge "First of all, where's the stone artefact than came with the lamp? You're supposed to give it to me."
mc "What? What stone artefact?"
hide genie04
show genie05 with fastdissolve
ge "Oh my God, he doesn't know what it is, someone please put me out of my misery!"
hide genie05
show genie03 with fastdissolve
ge "I'll grant you jackshit until you bring back the stone!"
mc "And how am I supposed to find it exactly?"
hide genie03
show genie04 with fastdissolve
ge "I guess it must have shattered and bits have been scattered all over the place. You've got to find every single piece of it."
mc "Don't tell me this is one of those annoying minigames where you have to find tiny hidden cards in the background..."
hide genie04
show genie06 with fastdissolve
ge "Actually, come to think about it, it is EXACTLY like one of those annoying minigames. Except the cards are pieces of rock. Even more boring."
hide genie06
show genie07 with fastdissolve
ge "Good luck sonny. I'm going back to sleep now, wake me up when you have the stone... And don't rub me the wrong way when you do."
hide genie07
show geniesmoke
play sound "Sounds/smokepuff.mp3"
$ renpy.pause(0.5, hard='True')
hide genie07
hide geniesmoke
window hide
show missionge at posmission
$ renpy.pause(4.0, hard=True)
hide missionge
$ missionge = True
mc "I guess I might as well take the lamp and put in my room for later then... When I find those godamn pieces of rock."
if persistent.tipson:
    show hex05tip at tips with dissolve
    pause
    hide hex05tip
$ genielamp = True
if withbe:
    mc "Oh, Bella is coming back, I'd better act like nothing happened...."
    show bellaout09
    be "Well, you were right, there's nothing on the horizon. Let's go back to the compound and report to Chief Lena."
if withpe:
    mc "Oh, Penny is coming back, I'd better act like nothing happened...."
    show pennyout03
    pe "Well, you were right, there's nothing on the horizon. Let's go back to the compound and report to Chief Lena."

$ period += 1
scene command01 with fade
show lena01
le "So, what do you have to report about area B2, scouts?"
mc "Nothing. Just empty desert Chief."
hide lena01
show lenapensive
le "I'm sure the Trumpf militia must be somewhere around that area... We'll look further tomorrow. Dismissed, scouts!"
hide lenapensive
jump LeaveCommand

label ExploreHex13:
stop sound
scene matrix with fade
$ explored = True
$ exploredhex13 = True 
if withbe:
    show bellaoutback
    be "What the hell is that?"
    mc "It looks like this outdoor area hasn't been implemented yet..."
    be "Either that, or we are stuck in some kind of virtual reality video game..."
    mc "That's too spooky a thought, let's leave."
    jump LeaveHex13
if withpe:
    show pennyoutback
    pe "What the hell is that?"
    mc "It looks like this outdoor area hasn't been implemented yet..."
    pe "Either that, or we are stuck in some kind of virtual reality video game..."
    mc "That's too spooky a thought, let's leave."
    jump LeaveHex13
    
label LeaveHex13:
$ period += 1
scene command01 with fade
show lena01
le "So, what do you have to report about area B3, scouts?"
mc "We were stuck in the Matrix on the thirteenth floor, Chief."
hide lena01
show lena03
le "What? What kind of drugs are you on?"
mc "The red pill. Hang on, or maybe the blue pill, I can never remember..."
hide lena03
show lena10
le "DISMISSED, scouts!"
jump LeaveCommand

label ExploreHex14:
stop sound
$ explored = True
$ exploredhex14 = True
scene hippy01 with fade
if withbe:
    be "Who are these people? And what are they doing in the middle of the desert???"
    mc "From the looks of their van, I'd say they are a bunch of millenial hippie chicks. \nUsually, they are peaceful..."
    be "Still, we shouldn't take any chances..."
if withpe:
    pe "Who are these people? And what are they doing in the middle of the desert???"
    mc "From the looks of their van, I'd say they are a bunch of millenial hippie chicks. \nUsually, they are peaceful..."
    pe "Still, we shouldn't take any chances..."
if persistent.tipson:
    show hex06tip at tips with dissolve
    pause
    hide hex06tip
menu:
    "Approach them with weapons drawn":
        jump HippieFlee
    "Approach them peacefully":
        jump Hippie01
    
label HippieFlee:
scene hippy02 with dissolve
show stella02
st "Livie, alert! Activate the ganja smokescreen!"
mc "Hang on a minu..."
window hide
show geniesmoke at midleft
play sound "Sounds/smokepuff.mp3"
$ renpy.pause(.5, hard=True)
show geniesmoke02 at midright
play sound "Sounds/smokepuff.mp3"
$ renpy.pause(1.0, hard=True)
show sandstorm01
mc "*cough* Fall back!"
scene hippyfled with fastdissolve
show sandstorm02
play sound "Sounds/bellatruck01.mp3"
$ renpy.pause(2.0, hard=True)
mc "...Shit, they're gone. Before I even had the chance to talk to them..."
$ hippyfled = True
scene hippy03 with dissolve
stop sound
mc "Damn, and they've left nothing worthwhile save... a spliff."
$ spliff = True
window hide
show spliff at posmission
$ renpy.pause(4.0, hard=True)
hide spliff
if withbe:
    be "Never mind, at least they're gone and we can report back to Chief Lena that we've cleared the area..."
    mc "Well, they might come back for all we know..."
    be "OK, if you want to waste your time coming back here, fine. We'll tell Chief Lena there were some suspicious-looking women and they fled as soon as they saw your ugly face!"
    mc "Hey, you're the one who said we should be careful!"
    be "*sigh* Let's go back to the compound now..."
    jump ExploredHex14Back
if withpe:
    pe "Never mind, at least they're gone and we can report back to Chief Lena that we've cleared the area..."
    mc "Well, they might come back for all we know..."
    pe "OK, if you want to waste your time coming back here, fine. We'll tell Chief Lena there were some suspicious-looking women and they fled as soon as they saw your ugly face!"
    mc "Hey, you're the one who said we should be careful!"
    pe "*sigh* Let's go back to the compound now..."
    jump ExploredHex14Back

label Hippie01:
$ exploredhex14b = True
scene hippy02 with dissolve
show stella01 at midleft
show livie01 at midright
mc "Howdy young women! Err... Peace and love and all that. May I ask you what you are doing here?"
st "We are here to attend Burning Man like every year. What about you? You're here for that too?"
mc "Not really. Didn't even know that festival was still going on after the Great Nuclear Fuckup War and the apocalypse..."
hide livie01
show livie03 at midright
li "What war?"
mc "Don't you girls ever try and listen to the radio?"
hide stella01
show stella03 at midleft
st "Our radio is busted, but we have our mp3 players with all the hippie music we need!"
hide livie03
show livie02 at midright
li "And enough ganja to last us for years... You wanna try some?"
mc "Sure... I mean, NO! How can you NOT KNOW that the world as we know it has ended???"
hide stella03
show stella04 at midleft
st "Haha, you're trying to pull our legs, right? So funny..."
if withbe:
    be "When was the last time you saw civilization exactly?"
if withpe:
    pe "When was the last time you saw civilization exactly?"
hide livie02
show livie04 at midright
li "Depends what you call civilization... There's a town not far east from here, where we get our supplies from."
hide stella04
show stella03 at midleft
st "It's called \"Desert Town\". We give them some ganja and they give us what we need."
window hide
show knowledgetown at posmission
$ renpy.pause(2.0, hard=True)
pause
hide knowledgetown
$ knowdeserttown = True
hide livie04
show livie03 at midright
li "So you're not here for Burning Man? Dude, it feels like we've been waiting for that festival to start for years."
mc "It's not just a feeling. You HAVE been waiting for years."
hide stella03
show stella04 at midleft
st "Wow, we're, like, totally stoned, it's so funny! You want some ganja?"
if withbe:
    $ hippiebella = True
    be "We don't have time for that [name]! Let's go back to the compound..."
    hide livie03
    show livie02 at midright
    li "Gee, who's that nazi with you, man? Come back and see us, we've got tons of dope..."
    mc "I guess we should leave..."
    be "And we'll NEVER come back, not with MY rig!"    
if withpe:
    $ hippiepenny = True
    pe "We don't have time for that [name]! Let's go back to the compound..."
    hide livie03
    show livie02 at midright
    li "Gee, who's that nazi with you, man? Come back and see us, we've got tons of dope..."
    mc "I guess we should leave..."
    pe "And we'll NEVER come back, not with MY rig!"

label ExploredHex14Back:
$ period += 1
scene command01 with fade
show lena01
le "So, what do you have to report about area B4, scouts?"
if hippyfled:
    mc "Some chicks in a van who fled as soon as they saw us."
    hide lena01
    show lena03
    le "And you didn't manage to catch up with them with your rig?"
    mc "They were... rather quick."
    hide lena03
    show lena11
    le "Well, that's no good! We NEED to know what they were up to!"
    hide lena11
    show lena10
    le "DISMISSED, scouts!"
    jump LeaveCommand

if hippyfled == False:
    mc "Some hippie chicks in a van. No threat at all. They didn't even know about the Great Nuclear Fuckup War."
    if withbe:
        be "And they gave us some valuable information about a town in the middle of the desert at area C5."
    if withpe:
        pe "And they gave us some valuable information about a town in the middle of the desert at area C5."
    hide lena01
    show lenapensive
    le "A town? Interesting... You are dismissed for now scouts."
    jump LeaveCommand

label ExploreHex15:
stop sound
$ exploredhex15 = True
$ explored = True
scene desert03
show desertrocks
show camel02b at camelleft
show camel08b at camelright
with fade

mc "Ah, another area with camels. Two of them this time."
if withbe:
    be "Double-whammy!"
if withpe:
    pe "Double-whammy!"

if darts >= 1:
    menu:
        "How about we capture one alive and shoot the last one? (-1 dart, +1 camel if successful)":
            if withbe:
                be "Fine, but I get ALL of the money from the meat then. You get to keep the live camel. And FEED IT."
                mc "Deal!"
                $ darts -= 1
                if darts == 0:
                    $ dart = False
                jump CamelCapture15
            if withpe:
                pe "Fine, but I get ALL of the money from the meat then. You get to keep the live camel. And FEED IT."
                mc "Deal!"
                $ darts -= 1
                if darts == 0:
                    $ dart = False
                jump CamelCapture15
        "OK, let's shoot them for their meat.":
            jump CamelShoot15
mc "OK, let's each shoot one then. We'll get 10 bucks each for that!"

label CamelShoot15:
$ camelshot = True
if withbe:
    hide desertrocks
    show bellarock01
    hide camel02b
    show camel04    
    with dissolve
    be "Aim carefully..."
    call DiceRoll
    $ dshootroll=mcfirearms+diceroll
    if (dshootroll >= 3 and not diceroll == 1) or diceroll == 6:
        window hide
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel04
        hide camel08b
        show camel05d
        show cameldead02     
        with dissolve
        stop sound
        be "Shoot the other one before it gets away!"
        $ camelsshot += 1
        call DiceRoll
        $ dshootroll=mcfirearms+diceroll
        if (dshootroll >= 3 and not diceroll == 1) or diceroll == 6:
            window hide
            play sound "Sounds/gun.mp3"
            $ renpy.pause(1.0, hard=True)
            hide camel05d
            show cameldeadc at cameldeadright
            with dissolve
            stop sound
            be "Congrats, you got both of them!"
            $ camelsshot += 1
            mc "I should get ALL the money then, right?"
            be "NOT right. I let you shoot them for training purposes. I could have shot both of them easily MYSELF."
            mc "Alright, alright. Let's go back to the compound for the dough then." 
            $ shotbothcamels = True
        if (dshootroll <= 2 and not diceroll == 6) or diceroll == 1:
            window hide
            play sound "Sounds/gun.mp3"
            $ renpy.pause(1.0, hard=True)
            hide camel05d
            show camel05c
            hide bellarock01
            show bellarock02
            with dissolve
            stop sound
            be "You missed. I'll shoot it quickly before it gets away then!"
            play sound "Sounds/gun.mp3"
            $ renpy.pause(1.0, hard=True)
            hide camel05c
            show cameldeadc at cameldeadright
            with dissolve
            stop sound
            $ bellashotcamels += 1
            be "There, got it! That was close. But we'll share the reward since you still managed to shoot at least ONE of them."
            mc "I should bloody think so! Let's go back to the compound for the dough then."
            $ bellashotcamel = True
        if camelsshot >= 10:
            mc "*I think I'm getting really good at shooting things in the wild...*"
            call PlusWarrior
            call MinusSierra
            $ camelsshot = 0        
        jump ExploreHex15Back
    if (dshootroll <= 2 and not diceroll == 6) or diceroll == 1:
        window hide
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel04
        hide camel08b
        show camel05c
        show camel05
        with dissolve
        stop sound
        be "You missed. And now they're both getting away! Damn it, I only have time to shoot one of them..."
        hide bellarock01
        show bellarock02
        with dissolve
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel05c
        hide camel05
        show cameldead02
        with dissolve
        stop sound
        $ bellashotcamels += 1
        be "The other one got away... So we'll only share 10$ instead of 20$. Because of your ATROCIOUS shooting skills!"
        mc "I'm training to get better you know!"
        hide bellarock02
        show bellarock01
        with fastdissolve
        $ bellashotonecamel = True
        be "Not enough clearly... Let's head back to the compound, it's getting late..."
        jump ExploreHex15Back
if withpe:
    hide desertrocks
    show pennyrock01
    hide camel02b
    show camel04    
    with dissolve
    pe "Aim carefully..."
    call DiceRoll
    $ dshootroll=mcfirearms+diceroll
    if (dshootroll >= 3 and not diceroll == 1) or diceroll == 6:
        window hide
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel04
        hide camel08b
        show camel05d
        show cameldead02     
        with dissolve
        stop sound
        pe "Shoot the other one before it gets away!"
        $ camelsshot += 1
        call DiceRoll
        $ dshootroll=mcfirearms+diceroll
        if (dshootroll >= 3 and not diceroll == 1) or diceroll == 6:
            window hide
            play sound "Sounds/gun.mp3"
            $ renpy.pause(1.0, hard=True)
            hide camel05d
            show cameldeadc at cameldeadright
            with dissolve
            stop sound
            pe "Congrats, you got both of them!"
            $ camelsshot += 1
            mc "I should get ALL the money then, right?"
            pe "NOT right. I let you shoot them for training purposes. I could have shot both of them easily MYSELF."
            mc "Alright, alright. Let's go back to the compound for the dough then." 
            $ shotbothcamels = True
        if (dshootroll <= 2 and not diceroll == 6) or diceroll == 1:
            window hide
            play sound "Sounds/gun.mp3"
            $ renpy.pause(1.0, hard=True)
            hide camel05d
            show camel05c
            hide pennyrock01
            show pennyrock02
            with dissolve
            stop sound
            pe "You missed. I'll shoot it quickly before it gets away then!"
            play sound "Sounds/gun.mp3"
            $ renpy.pause(1.0, hard=True)
            hide camel05c
            show cameldeadc at cameldeadright
            with dissolve
            stop sound
            $ pennyshotcamels += 1
            pe "There, got it! That was close. But we'll share the reward since you still managed to shoot at least ONE of them."
            mc "I should bloody think so! Let's go back to the compound for the dough then."
            $ pennyshotcamel = True
        if withmi:
            mi "Why did you bring me along to make me endure this vile spectacle? Shooting innocent creatures of Mother Nature..."
            call LustMinusMichiko
        if camelsshot >= 10:
            mc "*I think I'm getting really good at shooting things in the wild...*"
            call PlusWarrior
            call MinusSierra
            $ camelsshot = 0        
        jump ExploreHex15Back
    if (dshootroll <= 2 and not diceroll == 6) or diceroll == 1:
        window hide
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel04
        hide camel08b
        show camel05c
        show camel05
        with dissolve
        stop sound
        pe "You missed. And now they're both getting away! Damn it, I only have time to shoot one of them..."
        hide pennyrock01
        show pennyrock02
        with dissolve
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel05c
        hide camel05
        show cameldead02
        with dissolve
        stop sound
        $ pennyshotcamels += 1
        pe "The other one got away... So we'll only share 10$ instead of 20$. Because of your ATROCIOUS shooting skills!"
        mc "I'm training to get better you know!"
        hide pennyrock02
        show pennyrock01
        with fastdissolve
        $ pennyshotonecamel = True
        pe "Not enough clearly... Let's head back to the compound, it's getting late..."
        jump ExploreHex15Back
label CamelCapture15:
if withbe:
    hide desertrocks
    show bellarock01
    hide camel02b
    show camel04    
    with dissolve
    be "Aim carefully..."
    call DiceRoll
    $ dshootroll=mcfirearms+diceroll
    if (dshootroll >= 3 and not diceroll == 1) or diceroll == 6:
        window hide
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel04
        hide camel08b
        show camel05d
        show cameldead02     
        with dissolve
        stop sound
        be "Nice one, that camel is now asleep, I'll shoot the other one for its meat."
        hide bellarock01
        show bellarock02
        with dissolve
        $ camels += 1
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel05d
        show cameldeadc at cameldeadright
        with dissolve
        stop sound
        be "There, got it! Let's go back to the compound now."
        "You now have [camels] camels in your possession."
        if missionza and camels >= 4:
            "You have enough camels to go back to the nomad camp."
        if missionza02 and camels >= 6:
            "You have enough camels to go back to the nomad camp."
        $ bellashotonecamel = True
        jump ExploreHex15Back
    if (dshootroll <= 2 and not diceroll == 6) or diceroll == 1:
        window hide
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel04
        hide camel08b
        show camel05c
        show camel05
        with dissolve
        stop sound
        be "You missed. And now they're both getting away! Damn it, I only have time to shoot one of them..."
        hide bellarock01
        show bellarock02
        with dissolve
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel05c
        hide camel05
        show cameldead02
        with dissolve
        stop sound
        be "The other one got away... But that one was YOURS. I ain't sharing my reward, as per our agreement..."
        mc "I'm training to get better you know!"
        hide bellarock02
        show bellarock01
        with fastdissolve
        $ bellashotonecamel = True
        be "Not enough clearly... Let's head back to the compound, it's getting late..."
        jump ExploreHex15Back
if withpe:
    hide desertrocks
    show pennyrock01
    hide camel02b
    show camel04    
    with dissolve
    pe "Aim carefully..."
    call DiceRoll
    $ dshootroll=mcfirearms+diceroll
    if (dshootroll >= 3 and not diceroll == 1) or diceroll == 6:
        window hide
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel04
        hide camel08b
        show camel05d
        show cameldead02     
        with dissolve
        stop sound
        pe "Nice one, that camel is now asleep, I'll shoot the other one for its meat."
        hide pennyrock01
        show pennyrock02
        with dissolve
        $ camels += 1
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel05d
        show cameldeadc at cameldeadright
        with dissolve
        stop sound
        pe "There, got it! Let's go back to the compound now."
        "You now have [camels] camels in your possession."
        if missionza and camels >= 4:
            "You have enough camels to go back to the nomad camp."
        if missionza02 and camels >= 6:
            "You have enough camels to go back to the nomad camp."
        $ pennyshotonecamel = True
        jump ExploreHex15Back
    if (dshootroll <= 2 and not diceroll == 6) or diceroll == 1:
        window hide
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel04
        hide camel08b
        show camel05c
        show camel05
        with dissolve
        stop sound
        pe "You missed. And now they're both getting away! Damn it, I only have time to shoot one of them..."
        hide pennyrock01
        show pennyrock02
        with dissolve
        play sound "Sounds/gun.mp3"
        $ renpy.pause(1.0, hard=True)
        hide camel05c
        hide camel05
        show cameldead02
        with dissolve
        stop sound
        pe "The other one got away... But that one was YOURS. I ain't sharing my reward, as per our agreement..."
        mc "I'm training to get better you know!"
        hide pennyrock02
        show pennyrock01
        with fastdissolve
        $ pennyshotonecamel = True
        pe "Not enough clearly... Let's head back to the compound, it's getting late..."
        jump ExploreHex15Back

label ExploreHex15Back:
$ period += 1
scene command01 with fade
show lena01
le "So, what do you have to report about area B5, scouts?"
if camelshot == False:
    if bellashotonecamel:
        $ bellashotonecamel = False
        mc "Nothing to report. Just desert and a scorching sun Chief Lena!"
        be "I have something to report... I shot a camel, Chief. I'd like my 10$ reward..."
        hide lena01
        show lena03
        with fastdissolve
        le "Fine, here it is. Now please stop shooting camels and start exploring more interesting areas... Scouts dismissed!"
        hide lena03 with dissolve
        jump LeaveCommand
    if pennyshotonecamel:
        $ pennyshotonecamel = False
        mc "Nothing to report. Just desert and a scorching sun Chief Lena!"
        pe "I have something to report... I shot a camel, Chief. I'd like my 10$ reward..."
        hide lena01
        show lena03
        with fastdissolve
        le "Fine, here it is. Now please stop shooting camels and start exploring more interesting areas... Scouts dismissed!"
        hide lena03 with dissolve
        jump LeaveCommand
if camelshot:
    if bellashotonecamel:
        $ bellashotonecamel = False
        be "We found some camels and I managed to shoot one while [name] failed miserably at shooting any of them."
        mc "Hey, that's not a very nice thing to say!"
        hide lena01
        show lenapensive
        with fastdissolve
        le "So one camel, that's five dollars each then. You are dismissed scouts."
        mc "Tha's right, 10 New Dollars each please. And a side of McCamel Fries with that!"
        $ money += 5
        hide lenapensive with dissolve
        jump LeaveCommand
    if pennyshotonecamel:
        $ pennyshotonecamel = False
        pe "We found some camels and I managed to shoot one while [name] failed miserably at shooting any of them."
        mc "Hey, that's not a very nice thing to say!"
        hide lena01
        show lenapensive
        with fastdissolve
        le "So one camel, that's five dollars each then. You are dismissed scouts."
        mc "Tha's right, 10 New Dollars each please. And a side of McCamel Fries with that!"
        $ money += 5
        hide lenapensive with dissolve
        jump LeaveCommand
    if shotbothcamels:
        mc "I report that I shot TWO camels. One right between the eyes. And the other one right between the balls."
        $ shotbothcamels = False
    if withbe and bellashotcamel:
        mc "I report that I shot a camel. Right between the eyes. And Bella shot one too. Right between the balls. Yuck."
        $ bellashotcamel = False
    if withpe and pennyshotcamel:
        mc "I report that I shot a camel. Right between the eyes. And Penny shot one too. Right between the balls. Yuck."
        $ pennyshotcamel = False
    hide lena01
    show lenapensive
    with fastdissolve
    le "Great. More camel burgers and extra costs to the compound...."
    mc "Tha's right, 10 New Dollars each please. And a side of McCamel Fries with that!"
    hide lenapensive
    show lena05
    with fastdissolve
    le "Not funny. Not funny at all. You are dismissed scouts."
    hide lena05 with dissolve
    $ money += 10
    $ camelshot = False
    jump LeaveCommand
            
label ExploreHex16:
stop sound
$ explored = True
scene jungle01 with fade
$ exploredhex16 = True
if withbe and missionop and donemissionop == False:
    show bellaout01
    be "You're going back into that jungle? Then, I'll wait for you here to keep an eye on the rig..." 
    jump JungleOpala01
if withpe and missionop and donemissionop == False:
    show pennyout01
    pe "You're going back into that jungle? Then, I'll wait for you here to keep an eye on my bike..." 
    jump JungleOpala01
if withbe and donemissionop:
    show bellaout01
    be "You're going back into that jungle? Then, I'll wait for you here to keep an eye on the rig..." 
    jump TempleOpala
if withpe and donemissionop:
    show pennyout01
    pe "You're going back into that jungle? Then, I'll wait for you here to keep an eye on my bike..." 
    jump TempleOpala
if withbe:
    show bellaout01
    be "We seem to have reached the edge of a jungle. I can't go any further with my rig..."
    mc "I'll go alone and explore that forest a bit then."
    be "Fine, I'll be waiting for you right here, don't take too long [name]!"
    jump Jungle01
if withpe:
    show pennyout01
    pe "We seem to have reached the edge of a jungle. I can't go any further with my rig..."
    mc "I'll go alone and explore that forest a bit then."
    pe "Fine, I'll be waiting for you right here, don't take too long [name]!"
    jump Jungle01
if alone:
    mc "Let's get a move..."
    jump Jungle01
    
label JungleOpala01:
scene temple01 with dissolve
mc " I know exactly where to go this time..."
jump OpalaEntrance

label Jungle01:
scene jungle02 with dissolve
mc "This place is pretty lush... A welcome change from the dust and sand of the scorching desert..." 
mc "I'll refresh myself in this river and move forward..."
if persistent.tipson:
    show hex07tip at tips with dissolve
    pause
    hide hex07tip    
label Temple01:
scene temple01 with dissolve
mc "There are some ruins behind these trees. Looks like the entrance to a temple of some sort..."
menu:
    "Enter the temple":
        jump TempleOpala
    "Leave this creepy place":
        jump QueenLeave

label TempleOpala:
if almostclearedhex16:
    scene temple02
    show stone07idle
    show leveridle
    show pillar01aidle
    with dissolve
    mc "I'm really back here just to get this godamn stone artefact... So let's look around very closely..."
    call screen templeopalad
    screen templeopalad:
        modal True    
        imagebutton:
            focus_mask True
            idle "Explore/leveridle.png"
            hover "Explore/leverhover.png"
            action Jump ("TempleOpala")

        if stonepiece07 == False and missionge:
            imagebutton:
                focus_mask True
                idle "Icons/stone07idle.png"
                hover "Icons/stone07hover.png"
                action Jump ("StonePiece07")    
        imagebutton:
            focus_mask True
            idle "Icons/exitleftidle.png"
            hover "Icons/exitlefthover.png"
            action Jump ("QueenLeave01")
scene temple02
if pillar01 == 3 and pillar02 == 2 and pillar03 == 3:
    jump OpalaEntrance

label TempleOpalab:
scene temple02
if persistent.tipson and missionge and stonepiece07 == False:
    show hex07btip at tips with dissolve
    pause
    hide hex07btip
call screen templeopala
screen templeopala:
    modal True    
    imagebutton:
        focus_mask True
        idle "Icons/exitleftidle.png"
        hover "Icons/exitlefthover.png"
        action Jump ("QueenLeave01")
    imagebutton:
        focus_mask True
        idle "Explore/leveridle.png"
        hover "Explore/leverhover.png"
        action Jump ("TempleOpala")
    if pillar01 == 1:
        imagebutton:
            focus_mask True
            idle "Explore/pillar01aidle.png"
            hover "Explore/pillar01ahover.png"
            action Jump ("MovePillar01")
    if pillar01 == 2:
        imagebutton:
            focus_mask True
            idle "Explore/pillar01bidle.png"
            hover "Explore/pillar01bhover.png"
            action Jump ("MovePillar01")
    if pillar01 == 3:
        imagebutton:
            focus_mask True
            idle "Explore/pillar01cidle.png"
            hover "Explore/pillar01chover.png"
            action Jump ("MovePillar01")

    if pillar02 == 1:
        imagebutton:
            focus_mask True
            idle "Explore/pillar02aidle.png"
            hover "Explore/pillar02ahover.png"
            action Jump ("MovePillar02")
    if pillar02 == 2:
        imagebutton:
            focus_mask True
            idle "Explore/pillar02bidle.png"
            hover "Explore/pillar02bhover.png"
            action Jump ("MovePillar02")
    if pillar02 == 3:
        imagebutton:
            focus_mask True
            idle "Explore/pillar02cidle.png"
            hover "Explore/pillar02chover.png"
            action Jump ("MovePillar02")
    
    if pillar03 == 1:
        imagebutton:
            focus_mask True
            idle "Explore/pillar03aidle.png"
            hover "Explore/pillar03ahover.png"
            action Jump ("MovePillar03")
    if pillar03 == 2:
        imagebutton:
            focus_mask True
            idle "Explore/pillar03bidle.png"
            hover "Explore/pillar03bhover.png"
            action Jump ("MovePillar03")
    if pillar03 == 3:
        imagebutton:
            focus_mask True
            idle "Explore/pillar03cidle.png"
            hover "Explore/pillar03chover.png"
            action Jump ("MovePillar03")
    
    if stonepiece07 == False and missionge:
        imagebutton:
            focus_mask True
            idle "Icons/stone07idle.png"
            hover "Icons/stone07hover.png"
            action Jump ("StonePiece07")

label MovePillar01:
scene temple02
show leveridle
show exitleftidle
show pillarleft
play sound "Sounds/pillar.mp3"
$ pillar01 += 1
if pillar01 == 4:
    $ pillar01 = 1
if pillar01 == 1:
    if pillar02 == 1:
        show pillar02aidle
    if pillar02 == 2:
        show pillar02bidle
    if pillar02 == 3:
        show pillar02cidle
    if pillar03 == 1:
        show pillar03aidle
    if pillar03 == 2:
        show pillar03bidle
    if pillar03 == 3:
        show pillar03cidle
    show pillar01aidle with dissolve
if pillar01 == 2:
    if pillar02 == 1:
        show pillar02aidle
    if pillar02 == 2:
        show pillar02bidle
    if pillar02 == 3:
        show pillar02cidle
    if pillar03 == 1:
        show pillar03aidle
    if pillar03 == 2:
        show pillar03bidle
    if pillar03 == 3:
        show pillar03cidle    
    show pillar01bidle with dissolve
if pillar01 == 3:
    if pillar02 == 1:
        show pillar02aidle
    if pillar02 == 2:
        show pillar02bidle
    if pillar02 == 3:
        show pillar02cidle
    if pillar03 == 1:
        show pillar03aidle
    if pillar03 == 2:
        show pillar03bidle
    if pillar03 == 3:
        show pillar03cidle    
    show pillar01cidle with dissolve
jump TempleOpalab

label MovePillar02:
scene temple02
show leveridle
show exitleftidle
show pillarleft
play sound "Sounds/pillar.mp3"
$ pillar02 += 1
if pillar02 == 4:
    $ pillar02 = 1
if pillar02 == 1:
    if pillar01 == 1:
        show pillar01aidle
    if pillar01 == 2:
        show pillar01bidle
    if pillar01 == 3:
        show pillar01cidle
    if pillar03 == 1:
        show pillar03aidle
    if pillar03 == 2:
        show pillar03bidle
    if pillar03 == 3:
        show pillar03cidle
    show pillar02aidle with dissolve
if pillar02 == 2:
    if pillar01 == 1:
        show pillar01aidle
    if pillar01 == 2:
        show pillar01bidle
    if pillar01 == 3:
        show pillar01cidle
    if pillar03 == 1:
        show pillar03aidle
    if pillar03 == 2:
        show pillar03bidle
    if pillar03 == 3:
        show pillar03cidle    
    show pillar02bidle with dissolve
if pillar02 == 3:
    if pillar01 == 1:
        show pillar01aidle
    if pillar01 == 2:
        show pillar01bidle
    if pillar01 == 3:
        show pillar01cidle
    if pillar03 == 1:
        show pillar03aidle
    if pillar03 == 2:
        show pillar03bidle
    if pillar03 == 3:
        show pillar03cidle    
    show pillar02cidle with dissolve
jump TempleOpalab

label MovePillar03:
scene temple02
show leveridle
show exitleftidle
show pillarleft
play sound "Sounds/pillar.mp3"
$ pillar03 += 1
if pillar03 == 4:
    $ pillar03 = 1
if pillar03 == 1:
    if pillar01 == 1:
        show pillar01aidle
    if pillar01 == 2:
        show pillar01bidle
    if pillar01 == 3:
        show pillar01cidle
    if pillar02 == 1:
        show pillar02aidle
    if pillar02 == 2:
        show pillar02bidle
    if pillar02 == 3:
        show pillar02cidle
    show pillar03aidle with dissolve
if pillar03 == 2:
    if pillar01 == 1:
        show pillar01aidle
    if pillar01 == 2:
        show pillar01bidle
    if pillar01 == 3:
        show pillar01cidle
    if pillar02 == 1:
        show pillar02aidle
    if pillar02 == 2:
        show pillar02bidle
    if pillar02 == 3:
        show pillar02cidle    
    show pillar03bidle with dissolve
if pillar03 == 3:
    if pillar01 == 1:
        show pillar01aidle
    if pillar01 == 2:
        show pillar01bidle
    if pillar01 == 3:
        show pillar01cidle
    if pillar02 == 1:
        show pillar02aidle
    if pillar02 == 2:
        show pillar02bidle
    if pillar02 == 3:
        show pillar02cidle    
    show pillar03cidle with dissolve
jump TempleOpalab

label StonePiece07:
show pillarleft
show leveridle
"You found one of the missing pieces of the Stone Artefact."
$ stonepieces -= 1
window hide
show achievementgenie at posmission
$ renpy.pause(0.5, hard=True)
show text "{font=Gui/Boogaloo-Regular.ttf}{color=#ff0000}{size=30}[stonepieces]{/font}" at StonePosition
$ renpy.pause(2.0, hard=True)
hide text
hide achievementgenie
$ stonepiece07 = True
if almostclearedhex16:
    $ almostclearedhex16 = False
    $ clearedhex16 = True
    mc "Finally, I got what I was looking for and I can go back to the compound..."
    jump QueenLeave02 

jump TempleOpalab
label OpalaEntrance:
scene temple02
show pillarleft
show geniesmoke with dissolve
play sound "Sounds/smokepuff.mp3"
$ renpy.pause(1.0, hard='True')
hide geniesmoke with dissolve
show opala01 with moveinbottom
if beatopala and missionop == False and donemissionop == False:
    op "What do you want again? Haven't you tormented me enough?"
    mc "I came to apologize. I thought you were someone else. But now I'm ready to be your loyal servant."
    hide opala01
    show opala03
    with fastdissolve
    op "I don't know if I can trust you. But I have nothing to lose at the same time."
    mc "That's the spirit!"
    hide opala03
    show opala04
    with fastdissolve
    op "I don't know if I can trust you. But I have nothing to lose at the same time."
    op "If you want to help me and my tribe, you must retrieve my Gold Scepter, so that I can rule anew over my people!"
    mc "O...kay... And where could I find that scepter your Majesty?"
    hide opala04
    show opala01
    with fastdissolve
    op "The evil Spaniards stole it from me, but the fierce jaguar attacked them in the jungle and they fled without it. It must be somewhere in the eastern jungle around here."
    mc "Ri-ight... I just have to find a small item hidden in the jungle somewhere. Copy that..."
    hide opala01
    show opala04
    with fastdissolve
    op "Return with it and you shall be treated like a mighty hero. Fail, and you shall feel the wrath of Queen Opala!"
    window hide
    show missionopala at posmission
    $ renpy.pause(1.0, hard=True)
    pause
    hide missionopala
    $ missionop = True
    mc "(Or maybe I just won't come back here you bat-shit crazy woman...)"
    hide opala04 with dissolve
    mc "Right, and now she's gone and I didn't get to pump her full of my cream. I guess I just have to go back empty-cocked for now... *sigh*"
    jump QueenLeave
if missionop and donemissionop == False:
    op "I hope for your sake that you bring good tidings!"
    mc "Ah, no, sorry, still haven't found your scepter."
    hide opala01
    show opala03
    with fastdissolve
    op "So why are you here? Did you come to torment me and my tribe?"
    mc "Err... No. I wouldn't do that. I just thought... Maybe you'd like to pay me in advance or something?"
    hide opala03
    show opala04
    with fastdissolve
    op "How dare you ask anything of me when you have failed miserably in your quest! FEEL THE WRATH OF QUEEN OPALA!"
    play sound "Sounds/opalaspell.mp3"
    scene temple02
    show pillarleft
    show opala04
    with flash
    call MCInjury
    $ mcinjuredfight = True
    mc "What the F... I feel like I've been stabbed in the stomach... Now I know how women feel when I fuck their womb."
    hide opala04
    show opala02
    with fastdissolve
    op "Do NOT return until you have my scepter, you hear me, white man?"
    mc "Ok...Okay... Your Majesty."
    jump QueenLeave
if missionop and donemissionop:
    op "I hope for your sake that you bring good tidings!"
    mc "Yes, I found your scepter. In the middle of the jungle, just like you said."
    window hide
    show missionopalasuccess at posmission
    $ renpy.pause(1.0, hard=True)
    pause
    hide missionopalasuccess    
    hide opala01
    show opala05
    with dissolve
    op "Oh, what a glorious day for my tribe! Arise, my fellow Amazons!"
    mc "I don't see anything happening."
    op "They will arise once I have taken your... SEED!"
    mc "I see..."
    op "So get undressed and let us proceed with the ritual. I want you to FUCK ME GOOD AND FLOOD MY WOMB!"
    mc "Roger that your Majesty!"
    jump OpalaSex
op "Who dares trespass these immortal ruins?"
menu:
    "Just passing by, never mind me...":
        hide opala01
        show opala03
        with fastdissolve
        op "Then pass... And leave."
        jump QueenLeave
    "I am a survivor of the Great Apocalypse. Who are you?":
        hide opala01
        show opala04
        with fastdissolve
        op "I am Queen Opala of the great tribe of the Amazons. My tribespeople were slaughtered by white men... Just like you!"
        menu:
            "Yeah, well, that was like a long time ago and I've got nothing to do with it.":
                hide opala04
                show opala03
                with fastdissolve
                op "Humpf... I shall ask you to leave this place at once young man, or you will feel the wrath of Queen Opala!"
                mc "Fine, your mythology is all screwed up anyway, Queen Opala was a queen of Egypt!"
                jump QueenLeave
            "OK... I was just passing by anyway...":
                hide opala04
                show opala03
                with fastdissolve
                op "Then pass... And leave."                
                jump QueenLeave
            "Hang on a minute. I rescued you from that... trap or whatever.":
                hide opala04
                show opala03
                with fastdissolve
                op "That's my tomb. You disturbed me and the spirits of my tribe!"
                menu:
                    "Aaaah... I didn't know, sorry. Can I make it up to you in any way your Majesty?":
                        jump Queen02
                    "What a silly way to rest in peace. Your people are a weird bunch. Plus, I heard Amazons only had one tit. Pfff! (FIGHT - Close Combat)":
                        hide opala03
                        show opala02
                        with fastdissolve
                        op "Your insolence shall not go unpunished young man. Prepare to fight!"
                        $ opalafirst = True
                        jump QueenFight 
            "Land gets stolen, people get killed, what's the big deal?":
                hide opala04
                show opala02
                with fastdissolve
                op "The deal is that I cannot trust men of your kind. Prepare to fight, white man!"
                $ opalafirst = True
                jump QueenFight
            "Fear not, I come in peace your Majesty!":
                hide opala04
                show opala01
                with fastdissolve
                op "Peace I have... For eternity. It is help I seek."
                mc "Alright. What could I do to help you then?"
                jump Queen02
    "I don't like the tone of your voice... (FIGHT - Close combat)":
        hide opala01
        show opala02
        with fastdissolve
        op "And I don't like that smirk on your face. Prepare to fight!"
        jump QueenFight

label Queen02:
scene temple02
show pillarleft
show opala04 with fastdissolve
op "If you want to help me and my tribe, you must retrieve my Gold Scepter, so that I can rule anew over my people!"
mc "O...kay... And where could I find that scepter your Majesty?"
hide opala04
show opala01
with fastdissolve
op "The evil Spaniards stole it from me, but the fierce jaguar attacked them in the jungle and they fled without it. It must be somewhere in the eastern jungle around here."
mc "Ri-ight... I just have to find a small item hidden in the jungle somewhere. Copy that..."
hide opala01
show opala04
with fastdissolve
op "Return with it and you shall be treated like a mighty hero. Fail, and you shall feel the wrath of Queen Opala!"
window hide
show missionopala at posmission
$ renpy.pause(2.0, hard=True)
pause
hide missionopala
$ missionop = True
mc "(Or maybe I just won't come back here you bat-shit crazy woman...)"
hide opala04 with dissolve
mc "Right, and now she's gone and I didn't get to pump her full of my cream. I guess I just have to go back empty-cocked for now... *sigh*"
jump QueenLeave

label QueenFight:
hide screen mcstats
hide screen calendar
scene temple02 with dissolve
show pillarleft
show fightopala01 at farright
show mcfightopala01 at farleft
$ mc_health = 2.0
$ opala_health = 2.0
show screen screenfightmcopala

label OpalaRound:
if opalafirst:
    jump RoundOpalaFight
if opalafirst == False:
    jump RoundMCOpalaFight

label RoundOpalaFight:  
op "Fight like a man, boy!"
show fightopala01 at right with move
hide fightopala01
show fightopala02 at right
show fightopala02 at center with movefast
window hide
call DiceRoll
if diceroll >= 4:
    hide mcfightopala01
    hide fightopala02
    show fightopala03 at centerleft
    show mcfightopala04 at midleft
    with fastdissolve
    play sound "Sounds/punch.mp3"
    op "Amazon groin-kick!"
    $ counting = 0
    while counting < 20:
        $ mc_health -= 0.05
        $ counting += 1
        pause 0.01
    if mc_health >= 0.1:
        mc "My nuts! That was BELOW the belt!"
    if mc_health <= 0:
        hide mcfightopala04        
        show mcfightopala06 at farleft
        hide fightopala03
        show fightopala01
        with fastdissolve
        op "You can't beat me. I'm an undead anyway."
        mc "Well, I yield before I become one myself... You won, Queen Opala."
        call MCInjury
        $ mcinjuredfight = True
        hide screen screenfightmcopala
        jump QueenWinFightEnd        
    hide mcfightopala04
    hide fightopala03
    show mcfightopala01 at farleft
    show fightopala01 at farright
    with dissolve
if diceroll <= 3:
    hide mcfightopala01
    hide fightopala02
    show mcfightopala05 at farleft
    show fightopala03 at centerleft
    with fastdissolve
    play sound "Sounds/punch.mp3"
    mc "My nuts are made of steel. Didn't hurt a bit."
    op "Next time, I'll stick my foot heel first in them!"
    hide mcfightopala05
    hide fightopala03    
    show mcfightopala01 at farleft
    show fightopala01 at farright
    with dissolve
$ opalafirst = False
jump OpalaRound

label RoundMCOpalaFight:  
mc "Get ready for a beating, Amazon Queen!"
window hide
hide mcfightopala01
show mcfightopala02 at midleft
show mcfightopala02 at right with move
call DiceRoll
if dagger:
    $ dcombatroll=mccombat+diceroll+1
if dagger == False:
    $ dcombatroll=mccombat+diceroll
if (dcombatroll >= 6 and not diceroll == 1) or diceroll == 6:
    window hide
    hide fightopala01
    hide mcfightopala02
    show mcfightopala03 at midright
    with fastdissolve
    play sound "Sounds/crunch.mp3"
    mc "Boob Crush!"
    $ counting = 0
    while counting < 20:
        $ opala_health -= 0.05
        $ counting += 1
        pause 0.01
    if opala_health >= 0.1:
        op "Get OFF me, you OAF!"
    if opala_health <= 0:
        op "Get my tits out of YOUR face, I yield!"
        hide screen screenfightmcopala
        jump OpalaWinFightEnd
    hide mcfightopala03
    show mcfightopala01 at farleft
    show fightopala01 at farright
    with dissolve
if (dcombatroll <= 5 and not diceroll == 6) or diceroll == 1:
    window hide
    play sound "Sounds/punch.mp3"
    hide fightopala01
    hide mcfightopala02
    show mcfightopala07 at midright
    with fastdissolve
    op "Missed! Just like the Spaniards."
    hide mcfightopala07
    show mcfightopala01 at farleft
    show fightopala01 at farright
    with dissolve
$ opalafirst = True
jump OpalaRound   

label OpalaWinFightEnd:
hide screen screenfightmcopala
show screen mcstats
show screen calendar
scene opaladefeated
op "Your are brave and strong young man. The Queen is defeated. Take your spoils and leave."
$ money += 20
$ stolenecklace = True
$ beatopala = True
$ necklace = True
window hide
show opalanecklace at posmission
pause
hide opalanecklace
mc "I will indeed do just that... Cheerio, your Majesty."
call MinusSierra
jump QueenLeave

label QueenWinFightEnd:
hide screen screenfightmcopala
show screen mcstats
show screen calendar
op "Now get out of MY sacred temple!"
mc "It's in ruins anyway, no comfort here whatsoever."
jump QueenLeave

label QueenLeave01:
mc "I give up..."
label QueenLeave:
$ pillar01 = 1
$ pillar02 = 3
$ pillar03 = 2
scene jungle01 with dissolve
if withbe and donemissionop:
    show bellaout01
    be "Ah, there you are... you took a while..."
    mc "I had to clear the area. Took a while because...err... I got lost on my way back."
    be "Good scouts don't get lost, you have still much to learn. Let's go back to the compound, it's starting to get late."
    jump QueenLeave02
if withpe and donemissionop:
    show pennyout01
    pe "Ah, there you are... you took a while..."
    mc "I had to clear the area. Took a while because...err... I got lost on my way back."
    pe "Good scouts don't get lost, you have still much to learn. Let's go back to the compound, it's starting to get late."
    jump QueenLeave02
if withbe:
    show bellaout01
    be "Ah, there you are... Did you find anything interesting?"
    mc "There's some kind of ancient ruins in there, I didn't have time to investigate it that much. We might need to come back here again."
    be "Let's go back to the compound then, it's starting to get late."
if withpe:
    show pennyout01
    pe "Ah, there you are... Did you find anything interesting?"
    mc "There's some kind of ancient ruins in there, I didn't have time to investigate it that much. We might need to come back here again."
    pe "Let's go back to the compound then, it's starting to get late."
$ period += 1
scene command01 with fade
show lena01
le "So, what do you have to report about area B6, scouts?"
mc "I found some ancient ruins in a jungle."
hide lena01
show lena03
with fastdissolve
le "A jungle? So it's not just desert out there?"
mc "That's right, trees looked huge and healthy too..."
hide lena03
show lenapensive
with fastdissolve
le "Mmh, the ideal place for Trumpf militia men to hide then..."
hide lenapensive
show lena10
with fastdissolve
le "DISMISSED, scouts!"
jump LeaveCommand

label QueenLeave02:
$ period += 1
scene command01 with fade
show lena01
le "So, what do you have to report about area B6, scouts?"
if almostclearedhex16 == False:
    mc "I cleared it, Chief! No trumpf militia, no Amazon Queen with the wrong mythological name, nada."
    hide lena01
    show lena07
    with fastdissolve
    le "That's good. We can finally move on to other areas then."
    le "DISMISSED, scouts!"
    hide lena07 with dissolve
    if mcinjuredopala:
        mc "I should go to the medbay, that crazy nympho queen pounced on my groin so hard it hurts..."
        jump Medbay
    jump LeaveCommand
le "So, what do you have to report about area B6, scouts?"
if almostclearedhex16:
    mc "I almost cleared it, Chief! In that I forgot to pick up a piece of stone artefact. But otherwise, all clear."
    hide lena01
    show lena06
    with fastdissolve
    le "Why didn't you pick it up the first time round?"
    mc "Couldn't find it. Pretty well hidden just behind the ledge of the trap door on the right-hand side I'm told."    
    hide lena06
    show lena03
    with fastdissolve
    le "Well go back and get it and CLEAR THIS HEX! You are dismissed."
    hide lena03 with dissolve
    if mcinjuredopala:
        mc "I should go to the medbay, that crazy nympho queen pounced on my groin so hard it hurts..."
        jump Medbay
    jump LeaveCommand

label OpalaSex:
scene templesex01
show opalasex01
with dissolve
op "Unzip those pants and show your Queen YOUR mighty scepter!"
window hide
play sound "Sounds/zipper.mp3"
$ renpy.pause(1.0, hard=True)
op "Oh my... Let me handle that thing first, to make sure it is nice and SLIPPERY before it enters my fertile Amazon womb!"
mc "It's all yours, your Majesty..."
scene templesex02
show opalasex02
with dissolve
op "Mmmh... So tasty... *lick*"
window hide
play sound "Sounds/lick.mp3"
$ renpy.pause(1.0, hard=True)
op "Please... FUCK MY ROYAL MOUTH WITH IT!"

scene templesex01 with dissolve
play music "Sounds/hardsucking.mp3"
label OpalaBlowSlow:
hide opalablowfast
show opalablowslow
call screen opalablowslow02
screen opalablowslow02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("OpalaBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("OpalaBlowFast") 

label OpalaBlowFast:
mc "Open your mouth even WIDER my Queen, cos I'm going to fuck it even FASTER!"
hide opalablowslow
show opalablowfast
call screen opalablowfast02
screen opalablowfast02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("OpalaBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("OpalaBlowSlow") 

label OpalaBlowEnd:
stop music
scene templesex02 blurred
show opalablowcum01
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Swallow it ALL! RHAAAA!"
op "Gllurb.... Cccbuum... on... mbeeee..."
mc "I think I got that."
hide opalablowcum01
show opalablowcum02
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "And there you go, what you asked for, FUCK YEAH!"
op "And I'll... glurb... lick those FAT balls to make you cum... glub... even MORE!"
scene templesex04
show opalablowcum03
with dissolve
op "I'm covered in your filthy scum.... But it's not in the right place. I want it sloshing in my WOMB!"
mc "Well, I have another MEGA-LOAD for you stored up in my balls, your Majesty, so hop on the creamy...I mean gravy train!"
scene templesex03 blurred
show opalaprefuck01
with dissolve
op "I don't know how I'm ever going to fit something THAT big in my poor pussy..."
mc "Come on, you're an Amazon Queen, surely your fuckhole is a true warrior too."
op "Of course it is, every fiber of my body is made for fighting! And I WILL FIGHT your cock right now!"
hide opalaprefuck01
play music "Sounds/fucksound.mp3"
label OpalaFuckSlow:
hide opalafuckfast
show opalafuckslow
call screen opalafuck02
screen opalafuck02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("OpalaFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("OpalaFuckFast") 

label OpalaFuckFast:
op "I'm going to ride you FASTER to COAX the BIGGEST load of cum possible from your MONSTER NUTS!"
hide opalafuckslow
show opalafuckfast
call screen opalafuckfast02
screen opalafuckfast02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("OpalaFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("OpalaFuckSlow") 

label OpalaFuckEnd:
op "Cum in me, GIVE ME YOUR SEED TO START MY NEW TRIBE!"
mc "*Gee, what's with all those crazy nymphos wanting babies from me?*"
hide opalafuckslow
hide opalafuckfast
stop music
show opalafuckcum01
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "CUMMING FOR YOU MY QUEEN!"
scene templesex04
show opalafuckcum02
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
op "Keep blasting that virile ball-batter, IMPREGNATE ME!"
mc "I can't stop cumming for you! AAAAAHHH!"
scene templesex01 blurred
show opalafuckcum03
with dissolve
op "That's not enough! I want EVERY LAST DROP!"
mc "*cough* You're... choking me... And hitting my groin too hard!"
op "My babies need to be conceived in agony. YOUR agony!"
call MCInjury
$ mcinjuredopala = True
scene templesex02
show opalafuckcum04
with dissolve
op "You did good, your sperm is sloshing in my womb and will give me a healthy tribe to rule anew over my KINDGOM!"
call PlusSierra
if mcsierra >= 4:
    op "Henceforth, thou shalt be known as \"[name] the Seeder\"."
    mc "Yooo-hoo! A new nickname!"
    window hide
    show mcsierranickname at posmission
    play sound "Sounds/skill.mp3"
    $ renpy.pause(2.0, hard=True)
    hide mcsierranickname
    $ sierranickname = True
mc "*cough* Glad... I could help... (Fuck, my groin hurts!)"
op "As a low-life impregnating stud to the Amazon Queen, you are of course forever banned from this temple."
mc "Well, that's not very nice..."
op "But I will gladly reward you with treasures beyond your wildest imagination!"
mc "I have a pretty wild imagination, I'm warning you."
if stolenecklace == False:
    op "Have this jewelled necklace and a gift of gold and begone, Absent Father of the Amazons!"
    $ necklace = True
    window hide
    show opalanecklace at posmission
    $ renpy.pause(2.0, hard=True)
    pause
    hide opalanecklace
if stolenecklace:
    op "Have this gift of gold and begone, Absent Father of the Amazons!"
$ money += 40
mc "I'm only absent cos you banned me..."
op "Stop moaning, take your money and get the fuck out of here."
mc "Roger that."
if missionge and stonepiece07:
    $ clearedhex16 = True
if missionge and stonepiece07 == False:
    $ almostclearedhex16 = True
jump QueenLeave

label ExploreHex21:
scene oracle01 with dissolve
play music "Sounds/desertwind01.mp3"
if exploredhex21 and knowentrancenorth == False and alone:
    "I hope the High Priestess will grant me an audience this time..."
    if withay: 
        ay "Why? She didn't last time?"
        mc "Nope, wouldn't give me the time of day."
        ay "If she gives you any more trouble, I'll straighten her up! I'll headbutt her in the fucking cunt if I have to!"
        mc "OK, calm down Ayla, let's see how it goes first...."
    jump Pythia01
if exploredhex21 and knowentrancenorth == False and withbe:
    be "We're back at the Oracle's temple. I hope this time you are prepared for the High Priestess's requirements..."
    mc "Yeah, hopefully."
    jump Pythia01
if exploredhex21 and knowentrancenorth == False and withpe:
    pe "We're back at this temple of Doom. I hope you know what you're doing this time, [name]..."
    mc "Yeah, hopefully."
    jump Pythia01
if exploredhex21 and knowentrancenorth and withbe:
    be "We're back at the Oracle's temple. Not quite sure why, since you already got what you were looking for last time."
    mc "Err... I just have to say a few more words to Pythia. Just stay behind this time."
    jump Pythia01
if exploredhex21 and knowentrancenorth and withpe:
    pe "We're back at this temple of Doom. Not quite sure why, since you already got what you were looking for last time."
    mc "Err... I just have to say a few more words to Pythia. Just stay behind Penny."
    jump Pythia01
if withbe:
    be "I feel the presence of the Phallus Lord! This place is blessed, it must belong to the Church."
    mc "Ok, then let's investigate."
if withpe:
    pe "More ruins. Probably due to raiders. There's most likely nothing to find here."
    mc "Still, we have to clear the area so we must investigate."
if alone:
    "What's this place? Let's have a look..."

label Pythia01:
scene oracle02
show pythia01
with dissolve
if exploredhex21 and knowentrancenorth == False:
    py "So, are you now ready to FULLY embrace the Church's teaching, [name]?"
    mc "Yes, High Priestess!"
    if mcchurch <= 3:
        hide pythia01
        show pythia03
        with fastdissolve        
        py "You say that, and yet, you are NOT EVEN close to being a member of the One, True Church..."
        py "You disappoint me. AND the Phallus Lord."
        hide pythia03
        show oracletrans01
        with dissolve
        play sound "Sounds/thunder.mp3"
        call MCInjury
        $ mcinjuredcurse = True                
        mc "What the hell just happened?"
        scene oracle01 blurred
        show oracletrans02
        with dissolve
        py "You were cursed by the Phallus Lord! Now leave and only come back when you become a True Servant of the Church!"
        mc "Alright, gee, I get it. You can quit all the drama."
        if withbe:
            be "Let's leave the High Priestess and go back to the compound, [name]."
        if withpe:
            pe "Let's leave this dreaded place and go back to the compound, [name]."
        jump BackHex21
    if mcchurch == 4:
        call PlusChurchReal
        hide pythia01
        show pythia02
        with fastdissolve        
        py "Well done, young man! You are now a fully-fledged MEMBER of the Church."
        hide pythia02
        show pythia01
    if mcchurch >= 5:
        hide pythia01
        show pythia02
        py "Of course, you must now pay a small fee for my services. 20 New Dollars."
        menu:
            "Pay the fee (-20$)" if money >=20:
                $ money -= 20
                jump OracleNext
            "I don't have enough money right now but I'll be back, oh Oracle!" if money <= 19:
                hide pythia02
                show pythia03
                with fastdissolve                        
                py "If you want to learn about your future, you must. Jizz be with you, my son."
                jump BackHex21
            "Refuse to pay the fee" if money >=20:
                hide pythia02
                show pythia03
                with fastdissolve                        
                py "The Phallus Lord will be mightily disappointed, young man!"
                if withay:
                    ay "This fee is a rip-off anyway! The Church doesn't allow for it, you stupid bitch!"
                    mc "Ayla, she's super-powerful, I think it's best if..."
                    ay "I'm not scared of her, I'll headbutt her in the c..."
                    mc "*cough* She didn't mean it, forgive her, oh High Priestess."
                    hide pythia02
                    show pythia01
                    with fastdissolve 
                    py "She's a feisty young woman... I sense a strength in her. That I've never felt before. You may go in peace. May the the Holy Spurt be with you."
                    mc "Thank you High Priestess, we'll leave in peace. Se-men."
                    jump BackHex21
                hide pythia03
                show oracletrans01
                with dissolve
                play sound "Sounds/thunder.mp3"
                call MCInjury
                $ mcinjuredcurse = True                
                mc "What the hell just happened?"
                scene oracle01 blurred
                show oracletrans02
                with dissolve
                py "You were cursed by the Phallus Lord! Now leave and only come back when you can pay your tribute to the Oracle!"
                mc "Alright, gee, I get it. You can quit all the drama."
                if withbe:
                    be "Let's leave the High Priestess and go back to the compound, [name]."
                if withpe:
                    pe "Let's leave this dreaded place and go back to the compound, [name]."
                jump BackHex21

if exploredhex21 and knowentrancenorth:
    py "Oh, it is you again, \"[name] the Punisher\". Have you come to PUNISH me again?"
    mc "Yep. The Phallus Lord summoned me again to WRECK your pussy inside out!"
    if mcchurch <= 4:
        hide pythia01
        show pythia03
        with fastdissolve
        py "Problem is... Since your last visit, you actually ABANDONED the Church. The Phallus Lord is actually mightily DISAPPOINTED in you."
        mc "Oh, shit..."
        hide pythia03
        show oracletrans01
        play sound "Sounds/thunder.mp3"
        with dissolve
        py "I sense... The wrath of the All-Jizzing One-Eye!"
        call MCInjury
        $ mcinjuredcurse = True                
        mc "What the hell just happened?"
        scene oracle01 blurred
        show oracletrans02
        with dissolve
        py "You were cursed by the Phallus Lord! Now leave and only come back when you are a True Servant of the Church!"
        mc "Alright, gee, I get it. You can quit all the drama. I'm outta here."
        jump BackHex21
    if mcchurch >= 5:
        hide pythia01
        show pythia02
        with fastdissolve
        py "I recognized his mark, you truly are blessed, [name]! And I must comply with the Phallus Lord's command..."
        hide pythia02
        show pythia04
        with dissolve
        py "So come and FUCK ME. Again."
        $ oraclefuckagain = True
        jump OraclePreFuck

py "Jizz be with you, travellers. I am High Priestess Pythia, the Oracle of the Church of the Redeeming Phallus."
mc "And what are you doing in the middle of nowhere?"
hide pythia01
show pythia05
with fastdissolve
py "Members of the Church come from far and wide to learn about their futures. \nFor I alone can see through the One-Eye of the Phallus Lord!"
if alone:
    if mcchurch >= 5:
        mc "I'm a member of the Church, oh Oracle! So I'm ready to see my HERO future."
        hide pythia05
        show pythia02
        with fastdissolve        
        py "That is wonderful! Then, I will grant you an audience. For a small fee of 20 New Dollars of course."
        mc "Ah. I should have guessed. This is New America after all."
        menu:
            "Pay the fee (-20$)" if money >= 20:
                $ money -= 20
                jump OracleNext
            "I don't have enough money right now but I'll be back, oh Oracle!" if money <= 19:
                hide pythia02
                show pythia03
                with fastdissolve                        
                py "If you want to learn about your future, you must. Jizz be with you, my son."
                jump BackHex21
            "Refuse to pay the fee":
                hide pythia02
                show pythia03
                with fastdissolve                        
                py "The Phallus Lord will be mightily disappointed, young man!"
                if withay:
                    ay "This fee is a rip-off! The Church doesn't allow for it, you stupid bitch!"
                    mc "Ayla, she's super-powerful, I think it's best if..."
                    ay "I'm not scared of her, I'll headbutt her in the c..."
                    mc "*cough* She didn't mean it, oh High Priestess."
                    hide pythia02
                    show pythia01
                    with fastdissolve 
                    py "She's a feisty young woman... I sense a strength in her. That I've never felt before. You may go in peace. May the the Holy Spurt be with you."
                    mc "Thank you High Priestess, we'll leave in peace. Se-men."
                    jump BackHex21
                hide pythia03
                show oracletrans01
                with dissolve
                play sound "Sounds/thunder.mp3"
                call MCInjury
                $ mcinjuredcurse = True                
                mc "What the hell just happened?"
                scene oracle01 blurred
                show oracletrans02
                with dissolve
                py "You were cursed by the Phallus Lord! Now leave and only come back when you can pay your tribute to the Oracle!"
                mc "Alright, gee, I get it. You can quit all the drama."
                jump BackHex21
    if mcchurch == 4:
        mc "I'm almost a member, oh High Priestess! And I value the Church's teachings. Plus, I'm a HERO, my future must be valuable."
        hide pythia05
        show pythia02
        with fastdissolve        
        py "That is wonderful! Are you willing, right now, to FULLY EMBRACE the Church's teachings?"
        menu:
            "Join Church of the Redeeming Phallus faction (abandon previous faction)":
                mc "YES! Please accept me into your Church, oh Phallus Lord!"
                call PlusChurchReal
                py "Well done, young man! Of course, thre is also a small fee for my services. 20 New Dollars."
                mc "Ah. I should have guessed. This is New America after all."
                menu:
                    "Pay the fee (-20$)":
                        $ money -= 20
                        jump OracleNext
                    "I don't have enough money right now but I'll be back, oh Oracle!" if money <= 19:
                        hide pythia02
                        show pythia03
                        with fastdissolve                        
                        py "If you want to learn about your future, you must. Jizz be with you, my son."
                        jump BackHex21
                    "Refuse to pay the fee":
                        hide pythia02
                        show pythia03
                        with fastdissolve                        
                        py "The Phallus Lord will be mightily disappointed, young man!"
                        if withay:
                            ay "This fee is a rip-off! The Church doesn't allow for it, you stupid bitch!"
                            mc "Ayla, she's super-powerful, I think it's best if..."
                            ay "I'm not scared of her, I'll headbutt her in the c..."
                            mc "*cough* She didn't mean it, oh High Priestess."
                            hide pythia02
                            show pythia01
                            with fastdissolve 
                            py "She's a feisty young woman... I sense a strength in her. That I've never felt before. You may go in peace. May the the Holy Spurt be with you."
                            mc "Thank you High Priestess, we'll leave in peace. Se-men."
                            jump BackHex21
                        hide pythia03
                        show oracletrans01
                        with dissolve
                        play sound "Sounds/thunder.mp3"
                        call MCInjury
                        $ mcinjuredcurse = True                
                        mc "What the hell just happened?"
                        scene oracle01 blurred
                        show oracletrans02
                        with dissolve
                        py "You were cursed by the Phallus Lord! Now leave and only come back when you can pay your tribute to the Oracle!"
                        mc "Alright, gee, I get it. You can quit all the drama."
                        jump BackHex21
            "Not yet, oh Oracle! (keep previous faction)":
                hide pythia02
                show pythia03
                with fastdissolve                        
                py "The Phallus Lord will be mightily disappointed, young man!"
                hide pythia03
                show oracletrans01
                with dissolve
                play sound "Sounds/thunder.mp3"
                call MCInjury
                $ mcinjuredcurse = True                
                mc "What the hell just happened?"
                scene oracle01 blurred
                show oracletrans02
                with dissolve
                py "You were cursed by the Phallus Lord! Now leave and only come back when you can pay your tribute to the Oracle!"
                mc "Alright, gee, I get it. You can quit all the drama."
                jump BackHex21
    if mcchurch <= 3:
        py "Are you a member of the Church? I don't sense that you are AT ALL."
        mc "Not yet, High Priestess. But so what? Isn't the Phallus Lord supposed to be tolerant and to love everyone?"
        hide pythia05
        show pythia03
        with fastdissolve        
        py "You must mistake Him for one of the Old Gods. He only cares for HIS flock. So not you, clearly. You must leave at once and only come back when you have seen His True Light."
        jump BackHex21
    
if withbe:
    be "Oh, what a blessed day! I am a fervent believer, oh Oracle! Please grant me an audience!"
    hide pythia05
    show pythia03
    py "Unfortunately for you my dear, only MEN of faith are allowed an audience with the Oracle. Is this boy a Member of the Church?"
    if mcchurch >= 5:
        be "Yes he is. But only recently, I've been an active memb..."
        py "Sorry, the Phallus Lord has spoken. Only HE may enter the Temple of the Oracle."
        mc "Alright! I'm starting to really like this male-centric organization."
        hide pythia03
        show pythia02
        py "Of course, for a small fee. 20 New Dollars."
        mc "Ah. I should have guessed. This is New America after all."
        menu:
            "Pay the fee (-20$)":
                $ money -= 20
                jump OracleNext
            "I don't have enough money right now but I'll be back, oh Oracle!" if money <= 19:
                hide pythia02
                show pythia03
                with fastdissolve                        
                py "If you want to learn about your future, you must. Jizz be with you, my son."
                jump BackHex21
            "Refuse to pay the fee":
                hide pythia02
                show pythia03
                with fastdissolve                        
                py "The Phallus Lord will be mightily disappointed, young man!"
                if withay:
                    ay "This fee is a rip-off! The Church doesn't allow for it, you stupid bitch!"
                    mc "Ayla, she's super-powerful, I think it's best if..."
                    ay "I'm not scared of her, I'll headbutt her in the c..."
                    mc "*cough* She didn't mean it, oh High Priestess."
                    hide pythia02
                    show pythia01
                    with fastdissolve 
                    py "She's a feisty young woman... I sense a strength in her. That I've never felt before. You may go in peace. May the the Holy Spurt be with you."
                    mc "Thank you High Priestess, we'll leave in peace. Se-men."
                    jump BackHex21
                hide pythia03
                show oracletrans01
                with dissolve
                play sound "Sounds/thunder.mp3"
                call MCInjury
                $ mcinjuredcurse = True                
                mc "What the hell just happened?"
                scene oracle01 blurred
                show oracletrans02
                with dissolve
                py "You were cursed by the Phallus Lord! Now leave and only come back when you can pay your tribute to the Oracle!"
                mc "Alright, gee, I get it. You can quit all the drama."
                be "Let's leave the High Priestess and go back to the compound, [name]."
                jump BackHex21
    if mcchurch == 4:
        be "Not quite, but he's working on it. On the other hand, I've been an active memb..."
        py "Sorry, the Phallus Lord has spoken. Only HE may enter. If he embraces the Church's teachings to their FULLEST!"
        menu:
            "Join Church of the Redeeming Phallus faction (abandon previous faction)":
                call PlusChurchReal
                hide pythia03
                show pythia02
                with fastdissolve        
                py "Well done, young man! Of course, thre is also a small fee for my services. 20 New Dollars."
                mc "Ah. I should have guessed. This is New America after all."
                menu:
                    "Pay the fee (-20$)":
                        $ money -= 20
                        jump OracleNext
                    "I don't have enough money right now but I'll be back, oh Oracle!" if money <= 19:
                        hide pythia02
                        show pythia03
                        with fastdissolve                        
                        py "If you want to learn about your future, you must. Jizz be with you, my son."
                        jump BackHex21
                    "Refuse to pay the fee":
                        hide pythia02
                        show pythia03
                        with fastdissolve                        
                        py "The Phallus Lord will be mightily disappointed, young man!"
                        if withay:
                            ay "This fee is a rip-off! The Church doesn't allow for it, you stupid bitch!"
                            mc "Ayla, she's super-powerful, I think it's best if..."
                            ay "I'm not scared of her, I'll headbutt her in the c..."
                            mc "*cough* She didn't mean it, oh High Priestess."
                            hide pythia02
                            show pythia01
                            with fastdissolve 
                            py "She's a feisty young woman... I sense a strength in her. That I've never felt before. You may go in peace. May the the Holy Spurt be with you."
                            mc "Thank you High Priestess, we'll leave in peace. Se-men."
                            jump BackHex21
                        hide pythia03
                        show oracletrans01
                        play sound "Sounds/thunder.mp3"
                        with dissolve
                        call MCInjury
                        $ mcinjuredcurse = True                
                        mc "What the hell just happened?"
                        scene oracle01 blurred
                        show oracletrans02
                        with dissolve
                        py "You were cursed by the Phallus Lord! Now leave and only come back when you can pay your tribute to the Oracle!"
                        mc "Alright, gee, I get it. You can quit all the drama."
                        be "Let's leave the High Priestess and go back to the compound, [name]."
                        jump BackHex21
            "Don't join the Church of the Redeeming Phallus faction (keep previous faction)":
                hide pythia02
                show pythia03
                with fastdissolve                        
                py "The Phallus Lord will be mightily disappointed, young man!"
                hide pythia03
                show oracletrans01
                with dissolve
                play sound "Sounds/thunder.mp3"
                call MCInjury
                $ mcinjuredcurse = True                
                mc "What the hell just happened?"
                scene oracle01 blurred
                show oracletrans02
                with dissolve
                py "You were cursed by the Phallus Lord! Now leave and only come back when you can pay your tribute to the Oracle!"
                mc "Alright, gee, I get it. You can quit all the drama."
                be "Let's leave the High Priestess and go back to the compound, [name]."
                jump BackHex21
    if mcchurch <= 3:
        py "Are you a member of the Church? I don't sense that you are AT ALL."
        mc "Not yet, High Priestess. But so what? Isn't the Phallus Lord supposed to be tolerant and to love everyone?"
        hide pythia05
        show pythia03
        with fastdissolve        
        py "You must mistake Him for one of the Old Gods. He only cares for HIS flock. So not you, clearly. You must leave at once and only come back when you have seen His True Light."
        be "That'll teach you for being an unbeliver, [name]. Now let's leave the High Priestess and go back to the compound, she must be very busy."
        jump BackHex21
                                                                
if withpe:
    pe "Well, I don't believe in this supernatural nonsense. I'm outta here. Gonna look after my rig."
    py "I pity the fools who fail to follow the Church's teachings!"
    if mcchurch >= 5:
        mc "I'm a member of the Church, oh Oracle! Unlike that fiendish atheist."
        hide pythia05
        show pythia02
        with fastdissolve        
        py "That is wonderful! Then, I will grant you an audience. For a small fee of 20 New Dollars of course."
        mc "Ah. I should have guessed. This is New America after all."
        menu:
            "Pay the fee (-20$)" if money >= 20:
                $ money -= 20
                jump OracleNext
            "I don't have enough money right now but I'll be back, oh Oracle!" if money <= 19:
                hide pythia02
                show pythia03
                with fastdissolve                        
                py "If you want to learn about your future, you must. Jizz be with you, my son."
                jump BackHex21
            "Refuse to pay the fee":
                hide pythia02
                show pythia03
                with fastdissolve                        
                py "The Phallus Lord will be mightily disappointed, young man!"
                if withay:
                    ay "This fee is a rip-off! The Church doesn't allow for it, you stupid bitch!"
                    mc "Ayla, she's super-powerful, I think it's best if..."
                    ay "I'm not scared of her, I'll headbutt her in the c..."
                    mc "*cough* She didn't mean it, oh High Priestess."
                    hide pythia02
                    show pythia01
                    with fastdissolve 
                    py "She's a feisty young woman... I sense a strength in her. That I've never felt before. You may go in peace. May the the Holy Spurt be with you."
                    mc "Thank you High Priestess, we'll leave in peace. Se-men."
                    jump BackHex21
                hide pythia03
                show oracletrans01
                with dissolve
                play sound "Sounds/thunder.mp3"
                call MCInjury
                $ mcinjuredcurse = True                
                mc "What the hell just happened?"
                scene oracle01 blurred
                show oracletrans02
                with dissolve
                py "You were cursed by the Phallus Lord! Now leave and only come back when you can pay your tribute to the Oracle!"
                mc "Alright, gee, I get it. You can quit all the drama."
                pe "Let's leave this dreaded place and go back to the compound, [name]."
                jump BackHex21
    if mcchurch == 4:
        mc "I'm almost a member, oh High Priestess! And I value the Church's teachings, unlike that fiendish atheist."
        hide pythia05
        show pythia02
        with fastdissolve        
        py "That is wonderful! Are you willing, right now, to FULLY EMBRACE the Church's teachings?"
        menu:
            "Join Church of the Redeeming Phallus faction (abandon previous faction)":
                mc "YES! Please accept me into your Church, oh Phallus Lord!"
                call PlusChurchReal
                py "Well done, young man! Of course, thre is also a small fee for my services. 20 New Dollars."
                mc "Ah. I should have guessed. This is New America after all."
                menu:
                    "Pay the fee (-20$)":
                        $ money -= 20
                        jump OracleNext
                    "I don't have enough money right now but I'll be back, oh Oracle!" if money <= 19:
                        hide pythia02
                        show pythia03
                        with fastdissolve                        
                        py "If you want to learn about your future, you must. Jizz be with you, my son."
                        jump BackHex21
                    "Refuse to pay the fee":
                        hide pythia02
                        show pythia03
                        with fastdissolve                        
                        py "The Phallus Lord will be mightily disappointed, young man!"
                        if withay:
                            ay "This fee is a rip-off! The Church doesn't allow for it, you stupid bitch!"
                            mc "Ayla, she's super-powerful, I think it's best if..."
                            ay "I'm not scared of her, I'll headbutt her in the c..."
                            mc "*cough* She didn't mean it, oh High Priestess."
                            hide pythia02
                            show pythia01
                            with fastdissolve 
                            py "She's a feisty young woman... I sense a strength in her. That I've never felt before. You may go in peace. May the the Holy Spurt be with you."
                            mc "Thank you High Priestess, we'll leave in peace. Se-men."
                            jump BackHex21
                        hide pythia03
                        show oracletrans01
                        with dissolve
                        play sound "Sounds/thunder.mp3"
                        call MCInjury
                        $ mcinjuredcurse = True                
                        mc "What the hell just happened?"
                        scene oracle01 blurred
                        show oracletrans02
                        with dissolve
                        py "You were cursed by the Phallus Lord! Now leave and only come back when you can pay your tribute to the Oracle!"
                        mc "Alright, gee, I get it. You can quit all the drama."
                        pe "Let's leave this dreaded place and go back to the compound, [name]."
                        jump BackHex21
            "Not yet, oh Oracle! (keep previous faction)":
                hide pythia02
                show pythia03
                with fastdissolve                        
                py "The Phallus Lord will be mightily disappointed, young man!"
                hide pythia03
                show oracletrans01
                with dissolve
                play sound "Sounds/thunder.mp3"
                call MCInjury
                $ mcinjuredcurse = True                
                mc "What the hell just happened?"
                scene oracle01 blurred
                show oracletrans02
                with dissolve
                py "You were cursed by the Phallus Lord! Now leave and only come back when you can pay your tribute to the Oracle!"
                mc "Alright, gee, I get it. You can quit all the drama."
                pe "Let's leave this dreaded place and go back to the compound, [name]."
                jump BackHex21
    if mcchurch <= 3:
        py "Are you a member of the Church? I don't sense that you are AT ALL."
        mc "Not yet, High Priestess. But so what? Isn't the Phallus Lord supposed to be tolerant and to love everyone?"
        hide pythia05
        show pythia03
        with fastdissolve        
        py "You must mistake Him for one of the Old Gods. He only cares for HIS flock. So not you, clearly. You must leave at once and only come back when you have seen His True Light."
        pe "Let's leave this dreaded place and go back to the compound, [name]."
        jump BackHex21
        
label OracleNext:
py "Follow me up the steps to the Temple, young man."
hide pythia02
show pythia04
with dissolve
py "And leave all your anger and fears behind."
scene oracle03
show pythia05
show pythia06
with dissolve
py "For the ceremony to proceed, you must first make a jizz offering to the Phallus Lord!"
mc "What???"
py "Yes, the Phallus Lord demands it. Also, I want to see what's hiding underneath that HUGE bulge of yours."
mc "Fine, fine..."
play sound "Sounds/zipper.mp3"
hide pythia06
show pythia07
with fastdissolve
py "Oh my..."
hide pythia05
hide pythia07
show pythia02
with fastdissolve
py "And now the Phallus Lord demands that the offering be made IN MY PUSSY!"
mc "Oh, here we go again. Bunch of nymphos."
label OraclePreFuck:
scene oracleprefuck01 with fade
py "What are you waiting for? Get that godly phallus HARD and come and seed me!"
mc "I'm coming, getting my clothes off as fast as I can, High Priestess!"
scene oracleprefuck02 with dissolve
py "I've been a VERY NAUGHTY High Priestess, you need to PUNISH me [name]!"
if churchnickname == False:
    mc "Oh I will, and I've got the tool to flagellate your insides too!"
    py "The Phallus Lord will therefore grant you a new nickname... \"[name] the Punisher\"!"
    window hide
    show mcchurchnickname at posmission
    $ renpy.pause(2.0, hard=True)
    $ churchnickname = True
    mc "Alright! I have a nickname now! Woo-ooh! Prepare to be PUNISHED by \"[name] the Punisher\"!"

play music "Sounds/fucksound.mp3"
label OracleFuckSlow:
hide oraclefuckfast
show oraclefuckslow
call screen oraclefuck02
screen oraclefuck02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("OracleFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("OracleFuckFast") 

label OracleFuckFast:
py "Fuck me FASTER! I need your offering in my pussy blasting at FULL SPEED!"
hide oraclefuckslow
show oraclefuckfast
call screen oraclefuckfast02
screen oraclefuckfast02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("OracleFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("OracleFuckSlow") 

label OracleFuckEnd:
py "This is so good! You truly are an upstanding MEMBER of the Church!"
mc "I'm about to blow my load, High Priestess!"
stop music
scene oraclefuckcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "FUCK! RHAAA!"
py "Your Holy Seed is in ME! AAAH, I'm cumming a CELESTIAL orgasm!"
scene oraclefuckcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "I've got some more splooge for you, High Priestess! AAARGH!"
py "I can FEEL it! Every MASSIVE cumshot! And it's making me cum too!"
scene oraclefuckcum03 with dissolve
if oraclefuckagain and pubichairgifted:
    mc "Phew, I hope the Phallus Lord is happy with that offering."
    py "I don't know about Him, but I sure am! Mmmh, so yummy... Let me get dressed so I can bid you farewell in an appropriate attire..."
    mc "Ah yes, so I can get another pubic hair. Sorry, another Holy Pubic Hair."
    scene oracle03
    show pythia02
    with dissolve
    py "That is correct and here it is, again with its certificate of authenticity and unique stock number."
    show holypubichair at posmission
    $ renpy.pause(1.0, hard=True)
    pause
    hide holypubichair
    $ pubichair += 1
    mc "Well, I thank you once again for this holy gift, Pythia. I should head back home to the compound now."
    hide pythia02
    show pythia01
    with fastdissolve    
    py "Farewell, \"[name] the Punisher\"!"
    jump BackHex21
if oraclefuckagain:
    $ pubichairgifted = True
    mc "Phew, I hope the Phallus Lord is happy with that offering."
    py "I don't know about Him, but I sure am! Mmmh, so yummy... Let me get dressed so I can bid you farewell in an appropriate attire..."
    scene oracle03
    show pythia02
    with dissolve
    py "You've been such a nice boy, I have a gift for you. A relic that is much sought after by Members of the Church. A Holy Pubic Hair."
    mc "A holy what?"
    hide pythia02
    show pythia05
    with fastdissolve
    py "A Holy Pubic Hair. From the very one and only Phallus Lord. It comes with a certificate of authenticity signed by me."
    hide pythia05
    show pythia02
    with fastdissolve    
    py "This would make a valuable gift to Members of the Church. Obviously not to heretical unbelievers..."
    py "And I have a whole stock of them, so I'll give you another one every time you come and visit me to... err... make a jizz offering."
    window hide
    show holypubichair at posmission
    $ renpy.pause(1.0, hard=True)
    pause
    hide holypubichair
    $ pubichair += 1
    mc "Well... err... I thank you for this...err... amazing holy gift, Pythia. I should head back home to the compound now."
    hide pythia02
    show pythia01
    with fastdissolve    
    py "Farewell, \"[name] the Punisher\"!"
    jump BackHex21
mc "I think I'm done now. I hope this offering was sufficient, Pythia. Cos I want to find out about my future as the HERO."
py "Now that the offering has been made successfully, I can read your future. Follow me, I'll get dressed and ready."
stop music
play music "Sounds/desertwind02.mp3"
scene oracle03 blurred
show oracletrans01
with dissolve
py "Oh Phallus Lord, let me see through your One-Eye..."
play sound "Sounds/thunder.mp3"
scene oracle04 blurred
show oracletrans02
with dissolve
py "I see... A large city... Surrounded by a mighty wall."
mc "Is it a bigly wall?"
py "Yes. It is."
mc "Must be Trumpf City then. Go on."
play sound "Sounds/thunder.mp3"
py "I see... An entrance. To the North... A dark and damp sewer. Where many dangers lie."
window hide
show knowledgenorth at posmission
$ renpy.pause(2.0, hard=True)
pause
hide knowledgenorth
$ knowentrancenorth = True
mc "Alright. How do I overcome these dangers then?"
hide oracletrans02
show oracletrans03
with dissolve
py "I... I'm sorry, my vision has faded."
mc "That's it then?"
stop music
play music "Sounds/desertwind01.mp3"
scene oracle03
show pythia02
with dissolve
py "Yep. That's it. Come back to see me anytime you want to learn more about your future, young hero! \nAnd Jizz be with you."
mc "Yeah. Jizz be with you too, High Priestess. Actually, I believe it's IN YOU right now."
if withbe:
    scene oracle01
    show bellaout01
    with dissolve
    be "So, how did your audience with the High Priestess go?"
    mc "Pretty well, I learnt about Trumpf City and how to sneak inside."
    be "Is that all? Your audience was VERY LONG! Did she say anything about me?"
    mc "Nope, sorry Bella..."
    be "*sigh* Let's go back to the compound then."
    jump BackHex21
if withpe:
    scene oracle01
    show pennyout01
    with dissolve
    pe "FINALLY. You took ages. That's why I don't waste my time going to church, it's just so time-consuming."
    mc "Yeah, it took a while but it was worth it. Let's go back to the compound."
    jump BackHex21

label BackHex21:
$ exploredhex21 = True
stop music
$ period += 1
scene command01 with fade
show lena01
if alone:
    le "So, what do you have to report about area C1, [name]?"
if alone == False:
    le "So, what do you have to report about area C1, scouts?"
if mcinjuredcurse:
    mc "I report that apostasy is punishable by severe cursing."
    hide lena01
    show lena03
    with fastdissolve
    le "What are you talking about?"
    mc "I'm cursed, CURSED I TELL YOU!"
    le "Alright, calm down, go to the medbay for... psychiatric treatment and we'll see you tomorrow in better spirits hopefully... SCOUTS DISMISSED!"
    jump Medbay
if knowentrancenorth and oraclefuckagain == False:
    mc "I saw my future self finding Trumpf City and entering it through a dark and damp sewer. Praise the Phallus Lord!"
    hide lena01
    show lena10
    with fastdissolve
    le "Oh, more of that superstitious gibberish... (sigh). At least, I can consider this area cleared. SCOUTS DISMISSED."
    hide lena10 with dissolve
    if mcinjuredcurse:
        mc "I don't feel well. I'd better go to the medical bay."
        jump Medbay
    jump LeaveCommand
if knowentrancenorth and oraclefuckagain:
    mc "I saw the Oracle again. But I didn't get anything...err... interesting out of her this time."
    hide lena01
    show lena10
    with fastdissolve
    le "And hopefully, she didn't get anything interesting OUT of YOU either! Scouts DISMISSED!"
    hide lena10 with dissolve
    if mcinjuredcurse:
        mc "I don't feel well. I'd better go to the medical bay."
        jump Medbay
    jump LeaveCommand
if knowentrancenorth == False:
    if alone:
        mc "I found a strange woman who claimed to be an Oracle who could see the future. But I didn't fall for her trickery. Yet."
        hide lena01
        show lena05
        with fastdissolve
        le "Meaning you WILL fall for her trickery in the future then..."
        mc "Oh, so you can see the future too then, Chief?"
        hide lena05
        show lena10
        with fastdissolve        
        le "Stop being insolent [name]! You are DISMISSED!"
        hide lena10 with dissolve
        jump LeaveCommand        
    if withbe:
        be "We found the Oracle, Chief Lena! But [name] here couldn't be bothered paying her a minor tribute for an audience, so we left empty-handed..."
        mc "Yeah, well, I don't have money to waste on that kind of things."
        hide lena01
        show lena10
        with fastdissolve
        le "(sigh). Well, try and make an effort next time, will you? SCOUTS DISMISSED!"
        hide lena10 with dissolve
        if mcinjuredcurse:
            mc "I don't feel well. I'd better go to the medical bay."
            jump Medbay
        jump LeaveCommand
    if withpe:
        pe "We found some weirdo priestess who claims she can see the future. And then she kicked us out."
        mc "Very rude of her I say. Very rude."
        hide lena01
        show lena10
        with fastdissolve
        le "(sigh). Well, try and make an effort next time, will you? SCOUTS DISMISSED!"
        hide lena10 with dissolve
        if mcinjuredcurse:
            mc "I don't feel well. I'd better go to the medical bay."
            jump Medbay
        jump LeaveCommand

label ExploreHex22:
play music "Sounds/desertwind01.mp3"
scene desertflowers01 with fade
if exploredhex22 == False:
    mc "There's a river running through that desert plain... I guess it still rains sometimes. And there are flowers all over the place too. I guess it's spring."
    if withbe:
        be "The Phallus Lord has brought us this human marvel."
    if withpe:
        pe "I used to ride my motorbike through fields of wild flowers."
    if withan or witham:
        an "Oh look, this is so beautiful!"
    if withcy:
        cy "Unfortunately, I am not equipped with an adequate smelling device."
    if withmo:
        mo "And I couldn't even put flowers on my husband's tomb... Since he doesn't even have one."
    if withmi:
        mi "Flowers are a sign that the planet is slowly recovering."
    if withru:
        ru "Pff. Flowers are for sissies. Still, I'll admit this place is very quiet and peaceful."
    if withza:
        za "I've never seen a flower in my life. Since I've lived in the desert for almost all of it."
    if withay:
        ay "These flowers will die soon. And then they'll be BORING."
    if withsu:
        su "I've only seen these things on my desktop background."
    if withgw:
        gw "I wonder if some have medicinal propeties that could be useful in the lab?"
    if withma:
        ma "I'll take some and see if I can concoct some new cocktail with them."
    if withcl:
        cl "The Phallus Lord has blessed this place with His Raw Beauty."
    if withla:
        la "This beautiful place might contain some interestingly mutated plants."
    if withba:
        ba "That's a nice place for a school trip!"
    if withde:
        de "There might some interesting DNA mutations in some of those plants. I'll collect some."
    mc "This place reminds me of both the fragility and the resilience of Mother Nature."
    call PlusSierra
if exploredhex22:
    mc "Back at the river bend..."
mc "I guess I could make a bouquet of wild flowers. Some girls back at the compound might like that as a gift. Sierra Club members most likely."
window hide
show flowerbouquet at posmission
$ renpy.pause(1.0, hard=True)
pause
hide flowerbouquet
$ bouquet += 1
if alone == False or withnone == False:
    mc "Well, that was time-consuming, we'd better head back to the compound now."
if alone and withnone:
    mc "Well, that was time-consuming, I'd better head back to the compound now."

label BackHex22:
stop music
$ exploredhex22 = True
stop music
$ period += 1
scene command01 with fade
show lena01
if alone:
    le "So, what do you have to report about area C2, scout?"
    mc "I found signs that life is slowly coming back. At least flowers are."
if alone == False:
    le "So, what do you have to report about area C2, scouts?"
    mc "We found signs that life is slowly coming back. At least flowers are."
hide lena01
show lena06
with fastdissolve
le "And no sign of the Trumpf Militia?"
mc "Nope. I guess they don't like flowers."
le "Fine. Scouts dismissed then!"
hide lena06 with dissolve
jump LeaveCommand

label ExploreHex24:
stop sound
$ explored = True
$ exploredhex24 = True
play music "Sounds/desertwind01.mp3"
scene evillair04 with dissolve
if alone:
    mc "Wow, what's that place at the top I wonder?"   
    scene evillairbottom01
    with dissolve
    show dronefarin with easeinright
    mc "There's a drone guarding the entrance. It's going to be tough getting in..."
    window hide
    show dronefarin with easeinright
    menu:
        "Run for the entrance using intimidating shouts":
            mc "I could make a run for it. I wonder what my chances are? Let's do a number crunch real quick..."
            mc "I'm coming up with 32.33. Repeating, of course. That's good enough for me."
            play sound "Sounds/leroy.mp3"
            $ renpy.pause(2.5, hard=True)                             
            jump RunEntranceLair
        "Approach the entrance nonchalantly":
            jump ApproacheDroneLair
    
mc "Wow, what's that place at the top?"
if withbe:
    be "Looks like the lair of Dr Evil. The Church warned us about him."
    mc "Dr Evil? Come on, that's just a parody character, he doesn't exist!"
    be "Don't take the Church's teaching lightly! He DOES exist and he is PURE evil!"
if withpe:
    pe "The Road Warriors Elders talked of an evil doctor living at the top of a mountain in the New Grand Canyon."
    mc "Elders? It's not like the New Grand Canyon is THAT old!"
    pe "The Elders are wise and I trust their wisdom. So should you."   
if withbe:
    scene evillairbottom01
    show evillairbella
    with dissolve
    show dronefarin with easeinright
if withpe:
    scene evillairbottom01
    show evillairpenny
    with dissolve
    show dronefarin with easeinright
mc "There's a drone guarding the entrance. It's going to be tough getting in..."
window hide
hide dronefarin at center
show dronefarout at center
hide dronefarout with easeoutright
if withbe:
    be "What are you going to do? You MUST do something! Dr Evil is just...like... so evil."
if withpe:
    pe "What are you going to do? You MUST do something! Dr Evil is just...like... so evil."
window hide
show dronefarin with easeinright
menu:
    "Run for the entrance using intimidating shouts":
        mc "I could make a run for it. What do you think are my chances? Can you give me a number crunch real quick?"
        if withbe:
            be "Yeah, I'm coming up with 32.33. Repeating, of course."
        if withpe:
            pe "Yeah, I'm coming up with 32.33. Repeating, of course."
        mc "That's good enough for me."
        play sound "Sounds/leroy.mp3"
        $ renpy.pause(2.5, hard=True)                             
        jump RunEntranceLair
    "Approach the entrance nonchalantly":
        jump ApproacheDroneLair

label RunEntranceLair:
scene evillairbottom02
with dissolve
play music "Sounds/drone.mp3"
window hide
show drone01 with moveinright
hide drone01
show drone02
with fastdissolve
play sound "Sounds/drone01.mp3"
$ renpy.pause(1.0, hard=True)
hide drone02
show drone03
with fastdissolve
mc "Oh shit..."
window hide
play sound "Sounds/gun.mp3"
pause 0.5
$ mcinjuredgun = True         
call MCInjury
mc "Flee, flee, run for your life!"
stop sound
jump LairFail

label ApproacheDroneLair:
stop music
play sound "Sounds/whistling.mp3"
scene evillairbottom02
with dissolve
play music "Sounds/drone.mp3"
window hide
show drone01 with moveinright
hide drone01
show drone02
with fastdissolve
mc "Well, hello there, you... sexy drone."
play sound "Sounds/drone01.mp3"
menu:
    "Punch it in the...err...face (STRENGTH test)":
        jump PunchDroneLair        
    "Try and disconnect it (MECHANICS test)":
        jump DisconnectDroneLair
    "Use Cyrl" if withcy:
        mc "Cyrl, you're a robot, can't you do something?"
        cy "I am a cyborg, not a robot, for your information. Completely different. But I can attempt to interact with its inferior CPU."
        cy "One moment... Contacting the drone... There."
        window hide
        play sound "Sounds/drone02.mp3"
        hide drone02
        show drone01
        with fastdissolve
        hide drone01 with moveoutright
        stop music
        mc "Wow, good work, Cyrl! The coast is now clear. Let's go up to the top of that mountain. By lift, I hope."
        cy "Ah, so you finally recognize the added-value of a cyborg in human society...."
        call LustPlusCyrl
        jump EvilLairEntrance
    "Flee. It's too dangerous.":
        hide drone02
        show drone03
        with fastdissolve
        mc "Oh shit..."
        window hide
        play sound "Sounds/gun.mp3"
        pause 0.5
        $ mcinjuredgun = True         
        call MCInjury
        mc "Hey, stop shooting, I was fleeing anyway dammit!"
        stop sound
        jump LairFail

label PunchDroneLair:
show mcpunch
play sound "Sounds/punch.mp3"
$ renpy.pause(1.0, hard=True)
call DiceRoll
$ dtestroll=(mcstrength+diceroll)
if (dtestroll >= 12 and not diceroll == 1) or diceroll == 6:
    window hide
    hide drone02
    hide mcpunch
    show dronepunch02
    show mcpunch
    with fastdissolve
    show strengthwin at posskill
    $ renpy.pause(2.0, hard=True)
    hide strengthwin
    hide mcpunch
    stop music
    hide dronepunch02 with moveoutbottom
    mc "Ah, ah, got you, stupid drone. Now the coast is clear for me to get to the top of that mountain."
    jump EvilLairEntrance
if (dtestroll <= 11 and not diceroll == 6) or diceroll == 1:
    window hide
    show strengthfail at posskill
    $ renpy.pause(2.0, hard=True)
    hide strengthfail
    mc "Fuck, that metal is too strong!"
    hide mcpunch
    play sound "Sounds/drone02.mp3"
    hide drone02
    show drone03
    with fastdissolve
    mc "Oh shit..."
    window hide
    play sound "Sounds/gun.mp3"
    pause 0.5
    $ mcinjuredgun = True         
    call MCInjury
    mc "Flee, flee, run for your life!"
    stop sound
    jump LairFail

label DisconnectDroneLair:
call DiceRoll
$ dtestroll=(mcmechanics+diceroll)
if (dtestroll >= 7 and not diceroll == 1) or diceroll == 6:
    window hide
    show mechanicswin at posskill
    $ renpy.pause(2.0, hard=True)
    hide mechanicswin
    mc "Ah, there's the off switch."
    hide drone02 with moveoutbottom
    mc "And now the coast is clear for me to get to the top of that mountain."
    jump EvilLairEntrance

if (dtestroll <= 6 and not diceroll == 6) or diceroll == 1:
    window hide
    show mechanicsfail at posskill
    $ renpy.pause(2.0, hard=True)
    hide mechanicsfail
    mc "Where is the fucking off-switch?"
    play sound "Sounds/drone02.mp3"
    hide drone02
    show drone03
    with fastdissolve
    mc "Oh shit..."
    window hide
    play sound "Sounds/gun.mp3"
    pause 0.5
    $ mcinjuredgun = True         
    call MCInjury
    mc "Flee, flee, run for your life!"
    stop sound
    jump LairFail    

label LairFail:
play music "Sounds/desertwind01.mp3"
if alone:
    scene evillairbottom01
    with dissolve
    show dronefarin with easeinright
    mc "That was a disaster. Let's go back to the compound."
    jump BackHex24
if withbe:
    scene evillairbottom01
    show evillairbella
    with dissolve
    show dronefarin with easeinright
if withpe:
    scene evillairbottom01
    show evillairpenny
    with dissolve
    show dronefarin with easeinright
if withbe:
    window hide
    hide dronefarin
    show dronefarout
    be "What happened back there? I heard gunshots."
    hide dronefarout with easeoutright
    mc "Yeah...err... The drone wouldn't let me pass."
    window hide
    show dronefarin with easeinright
    be "And it shot you. I can see you're bleeding. We'd better head back to the compound then."
    mc "It's probably a good idea indeed..."
if withpe:
    window hide
    hide dronefarin
    show dronefarout
    pe "What happened back there? I heard gunshots."
    hide dronefarout with easeoutright
    mc "Yeah...err... The drone wouldn't let me pass."
    window hide
    show dronefarin with easeinright
    pe "And it shot you. I can see you're bleeding. We'd better head back to the compound then."
    mc "It's probably a good idea indeed..."
jump BackHex24

label EvilLairEntrance:
stop music
play music "Sounds/desertwind01.mp3"
scene evillair03 with dissolve
mc "Finally, I'm at the top. And there's the bridge supposedly leading to Dr Evil's lair... Let's cross it."
stop music
scene evillair01 with dissolve
show drevil01
if seenevil:
    ev "You again? This time I'll take the combat initiative before you. Because I'm just ssooo EVIL. Prepare to get MILDLY INJURED!"
    $ evilfirst = True
    jump EvilFight
$ seenevil = True
ev "Ah, you finally found me, Tricky Dick's goons, but it is TOO LATE!"
mc "What are you babbling about, old man?"
hide drevil01
show drevil04
with fastdissolve
ev "Don't try and stop me, I have the ULTIMATE WEAPON in my hands!"
mc "What? A bottle of beer?"
ev "Sure, it might look like one but it is the perfect BIO-WEAPON! After decades of development in the confinement of my secret lab, it is finally ready to be UNLEASHED on the world!"
hide drevil04
show drevil02
with fastdissolve
ev "You can tell your stupid boss, President Nixon, that I, Dr Evil, am the TRUE bearer of DESTRUCTION! Behold, the..."
hide drevil02
show drevil04
with fastdissolve
play sound "Sounds/evillaugh.mp3"
ev "...CORONA-VIRUS! I will watch as the world crumbles to its knees, I will then have reached the PINNACLE of my evil career!"
window hide
$ renpy.pause(2.0, hard=True)
mc "Err... I don't want to break the party dude, but the world has already been destroyed. By the Great Nuclear Fuckup War."
hide drevil04
show drevil03
with fastdissolve
ev "What? How is that possible? Is it Tricky Dick, is it HIM? TELL ME, I need to know if this asshole STOLE the destruction of the Earth from ME!"
mc "Nope, it's President Donald Trumpf mainly."
hide drevil03
show drevil05
with fastdissolve
ev "President Trumpf? HA HA! Good one! As if a bankrupt New York real estate developer could become president! HO HO, what a laugh, I needed that, thank you, young man!"
hide drevil05
show drevil01
with fastdissolve
ev "Anyway, I already made a million cases of Corona-Virus beer, I finally found a source of water nearby, so I'm not backing down! Unless you happen to have on you... ONE MILLION DOLLARS! AH AH, I thought not!"
if missionhg:
    mc "Ah, so you're the one who stole the water from the sulfurous hammam then!"
    ev "So that's where the funny taste comes from. Never mind, with a slice of lemon to cover it, it will be the perfect beer to spread the virus to dumb spring breakers and various other self-entitled deplorables."
hide drevil01
show drevil02
with fastdissolve
ev "It's being shipped by Amazon drones to nearby towns as we speak!"
menu:
    "You're really evil, you know that, right?":
        hide drevil02
        show drevil03
        with fastdissolve
        ev "Of course I do. I'm DR EVIL. It says so in the name, dumbass. Now prepare to FIGHT! AND DIE! No, actually, I'll just mildly injure you, it's more evil!"
        $ evilfirst = True
        jump EvilFight
    "I'm the hero here, so I must stop you. Prepare to fight! (FIGHT - Close combat)":
        hide drevil02
        show drevil03
        with fastdissolve
        ev "So be it. Your demise will be the icing on the cake, Nixon goon!"
        mc "Nixon's dead, baby. Nixon's dead."
        jump EvilFight
    
label EvilFight:
hide screen mcstats
hide screen calendar
scene evillair02
show mcfightin01 at farleft
show evilfight01 at farright
with dissolve
$ mc_health = 2.0
$ evil_health = 2.0
show screen screenfightmcevil
label EvilRound:
if evilfirst:
    jump RoundEvilFight
if evilfirst == False:
    jump RoundMCFight

label RoundEvilFight:  
ev "Just watch my hypnotic eye, goon!"
play sound "Sounds/radiation02.mp3"
window hide
show hypnowave at poswave
$ renpy.pause(2.0, hard=True)
call DiceRoll
if diceroll >= 3:
    hide mcfightin01
    hide hypnowave
    show mchypnotized01 at farleft
    with fastdissolve
    mc "I... am... a zombie..."
    ev "Yes you are, now become WEAK, zombie!"
    $ counting = 0
    while counting < 20:
        $ mc_health -= 0.05
        $ counting += 1
        pause 0.01
    if mc_health <= 0:
        call MCInjury
        $ mcinjuredfight = True
        hide mchypnotized01
        hide evilfight01
        show mcyield01 at farleft
        show evilfight03 at farright
        with fastdissolve
        ev "Once again, Dr Evil defeats his enemies! Actually, it's the first time, but never mind. I WIN!"
        jump EvilWinFightEnd        
    hide mchypnotized01
    show mcfightin01 at farleft
    with fastdissolve
if diceroll <= 2:
    hide hypnowave
    with fastdissolve
    mc "Pff... Pathetically NOT evil, Dr Evil!"
    ev "Damn! It was supposed to work! But they wouldn't let me attach frickin laser beams to the sharks, I mean honestly throw me a bone here!"
$ evilfirst = False
jump EvilRound

label RoundMCFight:  
mc "I'm gonna kick your evil butt!"
window hide
show mcfightin01 at center with move
hide mcfightin01
show mckickin01
with fastdissolve
call DiceRoll
if dagger == False:
    $ dcombatroll=mccombat+diceroll        
if dagger:
    $ dcombatroll=mccombat+diceroll+1
if (dcombatroll >= 7 and not diceroll == 1) or diceroll == 6:
    window hide
    play sound "Sounds/punch.mp3"
    hide mckickin01
    hide evilfight01
    show evilfight02 at farright
    show mckickin02
    with fastdissolve
    mc "Take that!"
    ev "Ah, it hurts! I LOVE PAIN, but not THAT MUCH!"
    $ counting = 0
    while counting < 20:
        $ evil_health -= 0.05
        $ counting += 1
        pause 0.01
    if evil_health <= 0:
        jump EvilFightWin
    hide mckickin02
    hide evilfight02
    show mcfightin01 at farleft
    show evilfight01 at farright
    with fastdissolve
if (dcombatroll <= 6 and not diceroll == 6) or diceroll == 1:
    window hide
    play sound "Sounds/punch.mp3"
    hide mckickin01
    hide evilfight01
    show mckickin02
    show evilfight04 at farright
    with fastdissolve
    ev "Ah, ah, I dodged your WEAK move! Now it's my turn, the EVIL turn!"
    hide evilfight04
    hide mckickin02
    show mcfightin01 at farleft
    show evilfight01 at farright
    with fastdissolve
$ evilfirst = True
jump EvilRound   

label EvilWinFightEnd:
hide screen screenfightmcevil
show screen mcstats
show screen calendar
scene evillair01
show drevil01
with dissolve
ev "Now go back to your nurse so you can come back and I can injure you ONCE AGAIN! Ah, Ah, I'm just sssooo evil!"
$ evildefeated = True
jump EvilEnd

label EvilFightWin:
hide screen screenfightmcevil
show screen mcstats
show screen calendar
scene evillairfightwin01 with dissolve
ev "I yield!"
mc "That's better. Now promise you won't be so evil in the future."
ev "NEVER!"
mc "You want some more of my fist in your ugly third eye, old man?"
scene evillairfightwin02 with dissolve
ev "Alright, alright! I was just trying to win some time. I was hoping something would happen to save me at the last minute..."
mc "That works only with HEROES like me, don't you ever watch Bond movies?"
scene evillairfightwin01 with dissolve
ev "Ah, shit. I forgot I was the bad guy. Ok, what do you want to let me go?"    
if missionhg:
    mc "First, you get the water you've been diverting from the sulfurous source back to where it belongs!"
    scene evillairfightwin02 with dissolve
    ev "Fine, fine! Please don't hurt me, I'll be a good boy, I swear!"
    window hide
    show donemissionhg01 at posmission
    pause
    hide donemissionhg01
    $ donemissionhg = True
    mc "And next..."
    scene evillairfightwin01 with dissolve
mc "I'll take whatever loot I can find in this crappy lab. You'd better have something good."
scene evillairfightwin02 with dissolve
ev "I have a hypnosis pendulum. That's all, I promise! On my evil mother's grave!"
mc "And where is it?"
scene evillairfightwin01 with dissolve
ev "G...give me a beer first. I'm thirsty. Then I'll tell you."
menu:
    "Alright, here you are. Would you like a slice of lemon with that, asshole?":
        scene evillairfightwin03 with dissolve
        play sound "Sounds/spit.mp3"
        ev "Ssshhh! *spit*"
        ev "Ha, ha, ha! I got you, the virus spreads by spitting on people, I forgot to warn you! Oh, how EVIL I am!"
        call MCInjury
        $ mcinjuredvirus = True
        mc "What? You fucking prick! Now I have Covid-19! *cough*!"
        scene evillairfightwin01 with dissolve        
        ev "Ha, ha! The hypnosis pendulum is in my drawer by the way. Enjoy your Covid-19, ha, ha!"
        window hide
        show hypnosispendulum at posmission
        pause
        hide hypnosispendulum
        $ pendulum = True        
        mc "Ah, finally, something I can use on girls to increase their lust for me. I hope it doesn't break like in Battle of the Bulges, that would suck..."
        ev "What?"
        mc "Never mind what I was saying. Now, you be a good boy and I'd better not have to come back here to spank you, you hear me?"
        mc "(I should get the hell out of this infected place...)"
        jump EvilEnd
    "In your dreams. Tell me where the pendulum is or I swear...":
        scene evillairfightwin01 with dissolve
        ev "I'm immune to pain, I'm Dr EVIL! Ha, ha! I'll never speak now, your chances of finding that pendulum in my messy lab are ZILCH!"
        ev "So give me my beer or leave..."
        menu:
            "Fine, I'll give you your damn beer...":
                scene evillairfightwin03 with dissolve
                play sound "Sounds/spit.mp3"
                ev "Ssshhh! *spit*"
                ev "Ha, ha, ha! I got you, the virus spreads by spitting on people, I forgot to warn you! Oh, how EVIL I am!"
                call MCInjury
                $ mcinjuredvirus = True
                mc "What? You fucking prick! Now I have Covid-19! *cough*!"
                scene evillairfightwin01 with dissolve        
                ev "Ha, ha! The hypnosis pendulum is in my drawer by the way. Enjoy your Covid-19, ha, ha!"
                window hide
                show hypnosispendulum at posmission
                pause
                hide hypnosispendulum
                $ pendulum = True        
                mc "Ah, finally, something I can use on girls to increase their lust for me. I hope it doesn't break like in Battle of the Bulges, that would suck..."
                ev "What?"
                mc "Never mind what I was saying. Now, you be a good boy and I'd better not have to come back here to spank you, you hear me?"
                mc "(I should get the hell out of this infected place...)"
                jump EvilEnd
            "I'll look for it myself. And I'll find it.":
                ev "No you won't! Ha, ha!"
                scene evillair01 with dissolve
                mc "It's true this place is a right mess..."
                mc "Oh, I found some money at least. Strangely enough, currency that is still valid today."
                $ money += 10
                mc "But no luck with the pendulum. Oh, well, I'd better leave now, it's getting late."
                ev "See you later, alligator! Ha, ha, told you you wouldn't find it!"
                mc "EVIL ASSHOLE!"
                jump EvilEnd
label EvilEnd:
if alone:
    jump BackHex24    
play music "Sounds/desertwind01.mp3"
if withbe:
    scene evillairbottom01 blurred
    show bellaout01
    with fade
    be "So, what happened up there?"
    if evildefeated:
        mc "Err... Let's just say I have to come back to finish the job."
        be "Oh my Phallus Lord! You lost, didn't you? You were defeated by Dr Evil?"
        mc "Momentarily, yes. Please let's just go back to the compound."
        jump BackHex24
    mc "Oh nothing, just the usual stuff for a hero. I beat the crap out of Dr Evil and stopped his world domination plan is all."
    if mcinjuredvirus:
        play sound "Sounds/cough.mp3"
        be "Why are you coughing? Are you sick or something? Good thing the Phallus Lord is protecting me from above."
    be "Let's go back to the compound, it's getting late."
    mc "Roger that."
    jump BackHex24
if withpe:
    scene evillairbottom01 blurred
    show pennyout02
    with fade
    pe "So, what happened up there?"
    if evildefeated:
        mc "Err... Let's just say I have to come back to finish the job."
        pe "By the asphalt of the Great Roads! You lost, didn't you? You were defeated by Dr Evil?"
        mc "Momentarily, yes. Please let's just go back to the compound."
        jump BackHex24
    mc "Oh nothing, just the usual stuff for a hero. I beat the crap out of Dr Evil and stopped his world domination plan is all."
    if mcinjuredvirus:
        play sound "Sounds/cough.mp3"
        pe "Why are you coughing? Are you sick or something? Good thing I have my scarf to protect my face."
    pe "Let's go back to the compound, it's getting late."
    mc "Roger that."
    jump BackHex24

label BackHex24:
$ evilfirst = False
stop music
$ period += 1
scene command01 with fade
show lena01
if alone:
    le "So, what do you have to report about area C4, scout?"
if alone == False:
    le "So, what do you have to report about area C4, scouts?"
if evildefeated:
    mc "I met Dr Evil, we had a frank and open discussion about how evil he was and...err..."
    hide lena01
    show lena03
    with fastdissolve
    le "... He defeated you."
    mc "Yep. But it wasn't fair, he has three eyes and I only have two!"
    le "*sigh* DISMISSED!"
    hide lena03 with dissolve
    $ evildefeated = False
    mc "I'd better go and see nurse Rachel..."
    jump Medbay
if donemissionhg:
    mc "I met Dr Evil, defeated him, and cleared the area, Chief!"
    hide lena01
    show lena03
    with fastdissolve
    le "Right. Somehow, I find that story hard to believe... But I'll assume the area is cleared."
    $ clearedhex24 = True
    if mcinjuredvirus:
        play sound "Sounds/cough.mp3"
        mc "Sure... *cough* ...is, Chief! *cough*"
        le "And do us all a favor and go and get that terrible cough checked with nurse Rachel, will you?"
        mc "Of... *cough*... course."
        jump Medbay
    le "DISMISSED!"
    hide lena03
    with dissolve
    jump LeaveCommand
if donemissionhg == False:
    if seenevil:
        mc "I met Dr Evil. God, he's ssooo evil, you wouldn't believe."
        hide lena01
        show lena03
        with fastdissolve
        le "And you clearly failed to defeat him. LAME."
        mc "Not my fault, he's like... REALLY EVIL."
        le "*sigh* DISMISSED."
        if mcinjuredvirus:
            play sound "Sounds/cough.mp3"
            mc "Right...*cough* ...Chief. *cough*"
            le "And do us all a favor and go and get that terrible cough checked with nurse Rachel, will you?"
            mc "Of... *cough*... course."
            jump Medbay
        hide lena03
        with dissolve
        jump LeaveCommand
    if seenevil == False:
        mc "We found some kind of super-villain lair."
        hide lena01
        show lena03
        with fastdissolve
        le "And?"
        mc "Well, I couldn't get in, a drone shot me. But I swear I'll try again and next time, I'll succeed!"
        if mcinjuredgun:
            hide lena03
            show lena10
            with fastdissolve
            le "That's a big FAIL then, young man! Go to the medbay, you're bleeding all over my floor."
            mc "Sure, I was about to go, Chief."
            jump Medbay
        hide lena10
        with dissolve
        jump LeaveCommand

label ExploreHex26:
if seenmineinside:
    scene mine01 
    show minedooropenidle
    with dissolve
    if alone:
        mc "Nothing seems to have moved since my last visit. That's a good sign at least."        
    if alone == False:    
        mc "Nothing seems to have moved since our last visit. That's a good sign at least."
if exploredhex26 == False:
    scene mine01 with dissolve
    mc "It looks like some kind of abandoned mine..."
    if withbe:
        be "Watch out, it could be a trap..."
    if withpe:
        pe "I smell a rat. We'd better be careful..."
    if withan:
        an "This adventure is so exciting!"
    if withcy:
        cy "Why abandon a mine? The human mind is complex."
    if withmo:
        mo "Be careful [name], slavers use abandoned mines to hide their cargo. I was once stuck in a mine for a month."
    if withmi:
        mi "I'm prepared for close combat with any living creature that may dwell in this mine!"
    if withru:
        ru "Maybe there's some ruby in the mine. Ruby, got it?"
    if withza:
        za "I like jewels. But I'm just a sex slave so I can't afford them."
    if withay:
        za "Abandoned, cos it was a BORING mine."
    if withsu:
        za "There might some hi-tech basement behind that door for all we know."
    if withgw:
        gw "I'm out of here. This place is probably booby-trapped with explosives and I just KNOW I'll be the one getting blown up."
    if withma:
        ma "I can smell booze. I want this door opened!"
    if withcl:
        cl "Maybe this place is meant to be off-limits to us mere mortals. Like the Church crypt."
    if withla:
        la "This place is desolate. Not a vegetable in sight."
    if withba:
        ba "This place is quite empty. Like a post-apocalyptic school class."
    if withde:
        de "I wonder what kind of explosives they used to dig that mine."
if exploredhex26 and seenmineinside == False:
    scene mine01 with dissolve
    if alone:
        mc "I hope this time that I'll find a way of getting past that door..."
    if alone == False:    
        mc "I hope this time that we'll find a way of getting past that door..."

label AbandonedMine02:
$ exploredhex26 = True
scene mine01
if persistent.tipson:
    show minetip at tips with dissolve
    pause
    hide minetip
call screen abandonedmine
screen abandonedmine:
    modal True    
    imagebutton:
        focus_mask True
        idle "Icons/exitidle.png"
        hover "Icons/exithover.png"
        action Jump ("MineLeave")
    if seenmineinside == False:
        imagebutton:
            focus_mask True
            idle "Explore/mineentranceidle.png"
            hover "Explore/mineentrancehover.png"
            action Jump ("MineDoor")    
    if seenmineinside:
        imagebutton:
            focus_mask True
            idle "Explore/minedooropenidle.png"
            hover "Explore/minedooropenhover.png"
            action Jump ("MineDoor")    
    imagebutton:
        focus_mask True
        idle "Explore/minecartidle.png"
        hover "Explore/minecarthover.png"
        action Jump ("MineCart")

label MineCart:
scene minecart with dissolve
mc "Mmh, it's empty. Anything that might be interesting must be INSIDE the mine then."
if mcsierra == 5 and foundgems == False:
    jump MineDiamonds
if mcsierra == 4 and foundgems == False:
    $ d2rolldiamond = renpy.random.randint(1, 2)
    if d2rolldiamond == 1:
        jump AbandonedMine02
    if d2rolldiamond == 2:
        jump MineDiamonds
if mcsierra <= 3 and witham and foundgems == False:
    $ d2rolldiamond = renpy.random.randint(1, 2)
    if d2rolldiamond == 1:
        jump AbandonedMine02
    if d2rolldiamond == 2:
        $ amyfounddiamonds = True
        jump MineDiamonds
if mcsierra <= 3:    
    jump AbandonedMine02
label MineDiamonds:
window hide
show gemsparkling
$ renpy.pause(0.1, hard=True)
hide gemsparkling
$ renpy.pause(0.05, hard=True)
show gemsparkling
$ renpy.pause(0.1, hard=True)
hide gemsparkling
$ renpy.pause(0.05, hard=True)
show gemsparkling
$ renpy.pause(0.1, hard=True)
hide gemsparkling
$ renpy.pause(0.05, hard=True)
show gemsparkling
$ renpy.pause(0.1, hard=True)
hide gemsparkling
$ renpy.pause(0.05, hard=True)
show gemsparkling
$ renpy.pause(0.1, hard=True)
if amyfounddiamonds:
    am "Hang on name, I think I see something. Some diamonds! Or as I call them \"sacred carbon holders\"."
    mc "Wow, well spotted Amy!"
    call LustPlusAmy
    am "It was nothing, don't mention it. Just doing my bit for the planet and... your hero quest... *blush*"
if amyfounddiamonds == False:
    mc "Oh, hang on, my Sierra Club intuition was right after all, I spotted some small diamonds!"
$ foundgems = True
$ gem = True
window hide
show gems at posmission
$ renpy.pause(2.0, hard=True)
pause
hide gems
hide gemsparkling
if seenmineinside:
    $ clearedhex26 = True
mc "It will be hard to sell them but I could use them for barter perhaps."
if withza:
    za "Or you could give them to someone as a gift..."
    mc "Someone like you I presume?"
    za "Well, sure, I wouldn't mind..."
    mc "Yeah, but raising your lust points isn't important, you're a sex slave, remember?"
    za "Ummpfff..."
if withbe:
    be "Coveting rare gems is against the teachings of the Church. You should hand them over to the priest for safe-keeping."
    mc "Pff! AS IF!"
    be "Mmmf..."
    call MinusChurch
jump AbandonedMine02
    
label MineDoor:
if seenmineinside:
    scene mineentrance
    show minedooropen
    with dissolve
    mc "We've already taken everything that was inside the mine. There's nothing to see here anymore."
    jump AbandonedMine02
if seenmineinside == False:
    scene mineentrance with dissolve
    mc "This door looks pretty solid... But there is a small opening big enough for a small person."
    menu:
        "Use your mighty strength to force it open (Strength test)":
            show mcdoorclosed
            call DiceRoll
            $ dstrengthroll=(mcstrength+diceroll)
            if dstrengthroll >= 15:
                window hide
                show strengthwin at posskill
                $ renpy.pause(2.0, hard=True)
                hide strengthwin
                window hide
                play sound "Sounds/forcedooropen.wav"
                $ renpy.pause(1.0, hard=True)
                hide mcdoorclosed
                show minedooropen
                show mcdooropen
                with dissolve
                mc "And we're in! Thanks to my POWERFUL muscles!"
                jump MineInside
            if dstrengthroll <= 14:
                window hide
                show strengthfail at posskill
                $ renpy.pause(2.0, hard=True)
                hide strengthfail
                play sound "Sounds/forcedooropen.wav"
                $ renpy.pause(1.0, hard=True)            
                mc "Damn, this door is too solid! And I hurt myself too..."
                call MCInjury
                $ mcinjureddoor = True
                if withbe:
                    be "I think it's time to leave [name], you're injured and it's getting late."
                if withpe:
                    pe "I think it's time to leave [name], you're injured and it's getting late."
                jump BackHex26
        "Blow it up with explosives" if explosives:
            show minedoorexplosives
            mc "Ok, everyone, move away, I'm gonna blast that door open!"
            if withpe:
                pe "You're so... brutal. I like that. It's the Road Warriors way."
                call PlusWarrior
            window hide
            play sound "Sounds/explosion02.mp3"
            $ renpy.pause(1.0, hard=True)
            hide minedoorexplosives
            show minedooropen 
            with fastdissolve
            mc "And now, time to see what's inside..."
            jump MineInside
        "Ask Angie to sneak in through the small opening" if withan:
            an "Really? You want ME to be USEFUL? YIPPEE!"
            show angiesneak with dissolve
            if alone:
                mc "Once you're inside, you should be able to unlock the door ."
            if alone == False:
                mc "Once you're inside, you should be able to unlock the door for us."
            window hide
            hide angiesneak with dissolve
            play sound "Sounds/minedooropen.mp3"
            $ renpy.pause(1.0, hard=True)
            show minedooropenangie
            an "Yeah, I was USEFUL!"
            call LustPlusAngie
            mc "Well done Angie, now we can get in!"
            jump MineInside
        "Ask Ayla to sneak in through the small opening" if withay:
            ay "Why would I do that? It sounds BORING."
            mc "Who knows what's on the other side. Something exciting perhaps?"
            ay "Mmmh, I hadn't thought of it that way. Alright, I'll do it."
            show angiesneak with dissolve
            if alone:
                mc "Once you're inside, you should be able to unlock the door ."
            if alone == False:
                mc "Once you're inside, you should be able to unlock the door for us."
            window hide
            hide angiesneak with dissolve
            play sound "Sounds/minedooropen.mp3"
            $ renpy.pause(1.0, hard=True)
            show minedooropenayla
            ay "Yeah, I did, that was... Kinda exciting..."
            call LustPlusAyla
            mc "Well done Ayla, now we can get in!"
            jump MineInside
        "Ask Cyrl to force the door open (Cyrl Strength: 8)" if withcy:
            cy "I see, in case the door is too solid, my cybernetic arm will break in half while you'll be just fine."
            mc "You're my harem girl, do as you're told and follow the laws of robotics for once in your life."
            cy "They are ingrained in my mother board, I don't need to be reminded of their sadistic provisions. Fine, I'll do it."
            show cyrldoorclosed
            call DiceRoll
            if diceroll >= 5:
                window hide
                play sound "Sounds/forcedooropen.wav"
                $ renpy.pause(1.0, hard=True)
                hide cyrldoorclosed
                show cyrldooropen
                with dissolve
                cy "Clearly, humans cannot build doors that are solid enough."
                mc "Well done Cyrl, now we can get in!"
                jump MineInside            
            if diceroll <= 4:
                window hide
                play sound "Sounds/forcedooropen.wav"
                $ renpy.pause(1.0, hard=True)
                cy "It appears that this door is too solid even for a superior cyborg such as myself."
                mc "Damn, even if Cyrl can't open it... We'd better leave, it's getting late anyway."
                jump BackHex26
        "Leave and look elsewhere":
            if withbe:
                show bellaoutworry
                be "What are we going to do? I bet there's something super-important behind that door."
                mc "We can always come back here, after I get stronger or we figure out another way of getting inside..."
                jump BackHex26
            if withpe:
                show pennyout03
                pe "The mighty [name] is not so mighty after all..."
                mc "We can always come back here, after I get stronger or we figure out another way of getting inside..."
                jump BackHex26
        
label MineInside:
$ seenmineinside = True
scene mineinside with dissolve
mc "What do we have here... Some barrels of oil. Could be useful for the compound, we'll definitely take them back with us."
mc "And a crate. Let's open it and see what's inside..."
window hide
show boozehaul at posmission
$ renpy.pause(1.0, hard=True)
pause
hide boozehaul
$ booze = True
if withma == False:
    mc "Some booze... Marnie should be happy about that."
if withma:
    ma "A crate full of alcohol, I knew it! Can I take it for the bar, please [name]? I'm running low on liquor."
    mc "Sure, why not."
    ma "Thanks a lot! Of course, you'll carry it for me, you're strong, right?"
    mc "Err, I suppose."
    call LustPlusMarnie
    $ toldmarniemine = True    
if map == False:
    window hide
    show roadmap at posmission
    $ renpy.pause(1.0, hard=True)
    pause
    hide roadmap
    $ map = True
mc "A map of the US. Of the Old Times."
mc "And some cash. 40 new dollars worth. Let's leave before the rightful owners come back..."
$ money += 40
if foundgems:
    $ clearedhex26 = True
jump BackHex26

label MineLeave:
mc "Let's get the hell out of here and back to the compound."

label BackHex26:
$ period += 1
scene command01 with fade
show lena01
if alone:
    le "So, what do you have to report about area C6, scout?"
if alone == False:
    le "So, what do you have to report about area C6, scouts?"
if seenmineinside:
    if alone:
        mc "I found an abandoned mine and come back with the loot, Chief Lena!"
    if alone == False:
        mc "We found an abandoned mine and come back with the loot, Chief Lena!"
    hide lena01
    show lena03
    with fastdissolve
    le "And pray tell me, what does that loot consist of?"
    mc "Barrels of oil."
    hide lena03
    show lena06
    with fastdissolve
    le "Oh? I am pleasantly surprised. I was expecting more damn camel burgers. Congratulations, scouts! You are dismissed."
    hide lena06 with dissolve
    jump LeaveCommand
if seenmineinside == False:
    if alone:
        mc "I found an abandoned mine but the door was locked and I couldn't managed to force it open. But I'll try again."
    if alone == False:
        mc "We found an abandoned mine but the door was locked and we couldn't managed to force it open. But we'll try again."
    hide lena01
    show lena05
    with fastdissolve
    le "Mmh, another failure of a scouting mission then. You are DISMISSED!"
    hide lena05 with dissolve
    jump LeaveCommand

label ExploreHex27:
stop sound
$ explored = True
scene jungle01 with fade
$ exploredhex27 = True
if alone:
    mc "It seems to be the edge of a jungle. Since I can't go any further with my rig, I'll go on foot."
    call AloneStance
if withbe:
    show bellaout01
    be "We seem to have reached the edge of a jungle. I can't go any further with my rig..."
    mc "I'll go alone and explore it a bit then."
    be "Fine, I'll be waiting for you right here, don't take too long [name]!"
if withpe:
    show pennyout01
    pe "We seem to have reached the edge of a jungle. I can't go any further with my rig..."
    mc "I'll go alone and explore it a bit then."
    pe "Fine, I'll be waiting for you right here, don't take too long [name]!"

scene jungle03 with dissolve
play music "Sounds/jungle01.mp3"    
mc "I should choose my path wisely or I'll get lost..."
if persistent.tipson:
    show hex27tip at tips with dissolve
    pause
    hide hex27tip
call screen jungle03
screen jungle03:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/goahead.png"
        hover "Icons/goahead.png"
        action Jump ("Jungle04")
    imagebutton:
        focus_mask True
        idle "Icons/goleft.png"
        hover "Icons/goleft.png"
        action Jump ("Jungle05")
    imagebutton:
        focus_mask True
        idle "Icons/goright.png"
        hover "Icons/goright.png"
        action Jump ("Jungle06")
       
label Jungle05:
scene jungle05 with dissolve
stop music
play music "Sounds/jungle02.mp3"    
mc "It doesn't look like I can go any further, this is a dead end. I'd better turn round and go back on my tracks."
scene jungle03 with dissolve
stop music
play music "Sounds/jungle01.mp3"    
call screen jungle03b
screen jungle03b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/goahead.png"
        hover "Icons/goahead.png"
        action Jump ("Jungle06")
    imagebutton:
        focus_mask True
        idle "Icons/goleft.png"
        hover "Icons/goleft.png"
        action Jump ("Jungle04")
    imagebutton:
        focus_mask True
        idle "Icons/goright.png"
        hover "Icons/goright.png"
        action Jump ("JungleLeave")

label Jungle04:
scene jungle04 with dissolve
call screen jungle04
screen jungle04:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/goleft.png"
        hover "Icons/goleft.png"
        action Jump ("Jungle05b")
    imagebutton:
        focus_mask True
        idle "Icons/goright.png"
        hover "Icons/goright.png"
        action Jump ("Jungle07b")

label Jungle05b:
scene jungle05 with dissolve
stop music
play music "Sounds/jungle02.mp3"    
mc "It doesn't look like I can go any further, this is a dead end. I'd better turn round and go back on my tracks."
scene jungle06 with dissolve
stop music
play music "Sounds/jungle01.mp3"    
call screen jungle05b
screen jungle05b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/goahead.png"
        hover "Icons/goahead.png"
        action Jump ("Jungle07b")
    imagebutton:
        focus_mask True
        idle "Icons/goright.png"
        hover "Icons/goright.png"
        action Jump ("Jungle03c")

label Jungle03c:
scene jungle03 with dissolve
call screen jungle03c
screen jungle03c:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/goahead.png"
        hover "Icons/goahead.png"
        action Jump ("JungleLeave")
    imagebutton:
        focus_mask True
        idle "Icons/goleft.png"
        hover "Icons/goleft.png"
        action Jump ("Jungle06")
    imagebutton:
        focus_mask True
        idle "Icons/goright.png"
        hover "Icons/goright.png"
        action Jump ("Jungle05")

label Jungle06:
scene jungle07 with dissolve
call screen jungle06
screen jungle06:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/goahead.png"
        hover "Icons/goahead.png"
        action Jump ("Jungle08")
    imagebutton:
        focus_mask True
        idle "Icons/goleft.png"
        hover "Icons/goleft.png"
        action Jump ("Jungle07")

label Jungle08:
scene jungle08 with dissolve
mc "Oh, oh..."
show jaguarleap
play sound "Sounds/jaguar.mp3"
scene jungle08
show jaguarleap
with flash
mc "Ah, I'm being mauled by a big pussy cat! FLEE, FLEE!"
call MCInjury
$ mcinjuredjaguar = True        
stop sound
if mcsierra <= 4:
    mc "And he ripped my money pouch open too, I've lost some money..."
    if money >= 10:
        $ money -= 10
    if money <= 9:
        $ money = 0
scene jungle06 with fade
call screen jungle08
screen jungle08:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/goahead.png"
        hover "Icons/goahead.png"
        action Jump ("Jungle09b")
    imagebutton:
        focus_mask True
        idle "Icons/goright.png"
        hover "Icons/goright.png"
        action Jump ("Jungle07")

label Jungle07:
scene jungle04 with dissolve
call screen jungle07
screen jungle07:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/goleft.png"
        hover "Icons/goleft.png"
        action Jump ("Jungle09")
    imagebutton:
        focus_mask True
        idle "Icons/goright.png"
        hover "Icons/goright.png"
        action Jump ("Jungle10")

label Jungle07b:
stop music
play music "Sounds/jungle02.mp3"    
scene jungle06
show tucan01
with dissolve
mc "Shut up, stupid bird!"
if mcsierra == 5:
    mc "I don't like this. This bird seems to be sounding the alarm. The jaguar will now be alerted to my presence..."
    mc "I think it's best to turn round and find another path then."
    jump Jungle09
if withmi and mcsierra <= 4:
    mi "That tucan is sounding the alarm throughout the jungle."
    mc "How do you know?"
    mi "I studied the ancient Japanese art of bird-calling, which totally exists, despite what some people might say."
    mc "So, what do you suggest we do then?"
    mi "We should go back on our tracks..."
    mc "Alright, since you're in the Sierra Club, I trust you on this one..."
    if michikotoucan == False:
        call LustPlusMichiko
        $ michikotoucan = True
    mi "I'm glad I could be of help!"
    jump Jungle09
call screen jungle07b
screen jungle07b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/goahead.png"
        hover "Icons/goahead.png"
        action Jump ("Jungle10b")
    imagebutton:
        focus_mask True
        idle "Icons/goright.png"
        hover "Icons/goright.png"
        action Jump ("Jungle11")

label Jungle09:
stop music
play music "Sounds/jungle01.mp3"    
scene jungle07 with dissolve
call screen jungle09
screen jungle09:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/goahead.png"
        hover "Icons/goahead.png"
        action Jump ("Jungle05b")
    imagebutton:
        focus_mask True
        idle "Icons/goleft.png"
        hover "Icons/goleft.png"
        action Jump ("Jungle03c")

label Jungle09b:
scene jungle03 with dissolve
call screen jungle09b
screen jungle09b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/goahead.png"
        hover "Icons/goahead.png"
        action Jump ("Jungle05")
    imagebutton:
        focus_mask True
        idle "Icons/goleft.png"
        hover "Icons/goleft.png"
        action Jump ("JungleLeave")
    imagebutton:
        focus_mask True
        idle "Icons/goright.png"
        hover "Icons/goright.png"
        action Jump ("Jungle04")

label Jungle10:
if missionop and donemissionop == False:
    scene jungle09 with dissolve
    call screen jungle09b
    screen jungle09b:
        modal True
        imagebutton:
            focus_mask True
            idle "Icons/goright.png"
            hover "Icons/goright.png"
            action Jump ("Jungle10c")
        imagebutton:
            focus_mask True
            idle "Icons/goleft.png"
            hover "Icons/goleft.png"
            action Jump ("Jungle10c")
        imagebutton:
            focus_mask True
            idle "Explore/scepteridle.png"
            hover "Explore/scepterhover.png"
            action Jump ("JungleScepter")
if missionop == False:
    scene jungle09 with dissolve
    mc "Oh, oh..."
    show jaguarleap
    play sound "Sounds/jaguar.mp3"
    scene jungle08
    show jaguarleap
    with flash
    mc "Ah, I'm being mauled by a big pussy cat! FLEE, FLEE! Out of this dangerous jungle!"
    call MCInjury
    $ mcinjuredjaguar = True        
    stop sound
    if mcsierra <= 4:
        mc "And he ripped my money pouch open too, I've lost some money..."
        if money >= 10:
            $ money -= 10
        if money <= 9:
            $ money = 0
    jump JungleLeave02

label JungleScepter:   
scene jungle09
mc "Finally, I found that godamm scepter."
mc "No jaguar in sight... It's the ideal time to pick it up and GET THE HELL OUT OF HERE!"
$ donemissionop = True
window hide
show opalascepter at posmission
$ renpy.pause(1.0, hard=True)
pause
hide opalascepter
jump JungleLeave02
    
label Jungle10b:
scene jungle09 with dissolve
show jaguarleap
play sound "Sounds/jaguar.mp3"
scene jungle09
show jaguarleap
with flash
mc "Ah, Where the fuck did he come from? FLEE, FLEE!"
call MCInjury
$ mcinjuredjaguar = True        
stop sound
if mcsierra <= 4:
    mc "And he ripped my money pouch open too, I've lost some money..."
    if money >= 10:
        $ money -= 10
    if money <= 9:
        $ money = 0
scene jungle07
show tucan02
with dissolve
mc "Maybe it was that asshole bird which sounded the alarm..."
mc "It's getting late anyway, I need to get back, I know where the scepter is now at least..."
jump JungleLeave02

label Jungle10c:
scene jungle09
show jaguarleap
with dissolve
play sound "Sounds/jaguar.mp3"
scene jungle09
show jaguarleap
with flash
mc "Ah, Where the fuck did he come from? FLEE, FLEE!"
call MCInjury
$ mcinjuredjaguar = True        
stop sound
if mcsierra <= 4:
    mc "And he ripped my money pouch open too, I've lost some money..."
    if money >= 10:
        $ money -= 10
    if money <= 9:
        $ money = 0
scene jungle07
show tucan02
with dissolve
mc "It's getting late anyway, I need to get back, I know where the scepter is now at least..."
jump JungleLeave02

label Jungle11:
stop music
play music "Sounds/jungle01.mp3"    
scene jungle07 with dissolve
call screen jungle11
screen jungle11:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/goleft.png"
        hover "Icons/goleft.png"
        action Jump ("Jungle08")
    imagebutton:
        focus_mask True
        idle "Icons/goright.png"
        hover "Icons/goright.png"
        action Jump ("Jungle09b")

label JungleLeave:
stop music
scene jungle01 with dissolve
mc "Ah, shit, looks like I left the jungle by mistake..."
jump JungleLeave02b

label JungleLeave02:
stop music
scene jungle01 with dissolve
label JungleLeave02b:
if withbe:
    show bellaout01
    if mcinjuredjaguar:
        be "You look terrible, you've got scratches all over your body. What happened?"
        mc "I was viciously attacked by a jaguar with no manners whatsoever."
    be "Did you find anything interesting in there?"
    if donemissionop:
        mc "Yes, I found a scepter that could be useful."
        be "What, you plan on becoming Queen of the Jungle or something? Let's go back to the compound, we've wasted enough time with your wild goose chases..."
        jump ExploreHex27Compound
    mc "Not really, but I think it will be worth a shot to come back here again..."
    hide bellaout01
    show bellaout05
    with fastdissolve
    be "Let's go back to the compound, we've wasted enough time with your wild goose chases..."
if withpe:
    show pennyout01
    if mcinjuredjaguar:
        pe "You look terrible, you've got scratches all over your body. What happened?"
        mc "I was viciously attacked by a jaguar with no manners whatsoever."
    be "Did you find anything interesting in there?"
    if donemissionop:
        mc "Yes, I found a scepter that could be useful."
        pe "What, you plan on becoming Queen of the Jungle or something? Let's go back to the compound, we've wasted enough time with your wild goose chases..."
        jump ExploreHex27Compound
    mc "Not really, but I think it will be worth a shot to come back here again..."
    hide pennyout01
    show pennyout03
    pe "Let's go back to the compound, we've wasted enough time with your wild goose chases..."
jump ExploreHex27Compound

label ExploreHex27Compound:
$ period += 1
scene command01 with fade
show lena01
le "So, what do you have to report about area C7, scouts?"
if donemissionop:
    mc "I found some ancient artefact in a jungle."
    hide lena01
    show lena10
    with fastdissolve
    le "Oh, fantastic. For NOBODY. At least, we can consider this area CLEARED. Scouts DISMISSED."
    hide lena10 with dissolve
    if mcinjuredjaguar:
        mc "I'd better go to the medaby and have those scratches checked out by nurse Rachel..."
        jump Medbay
    jump LeaveCommand
if donemissionop == False:
    mc "I got lost in a jungle."
    hide lena01
    show lena10
    with fastdissolve
    le "Oh, perfect. A scout who gets lost. Just what I needed in this compound! You are DISMISSED!"
    hide lena10 with dissolve
    if mcinjuredjaguar:
        mc "I'd better go to the medbay and have those scratches checked out by nurse Rachel..."
        jump Medbay
    jump LeaveCommand

label ExploreHex25:
$ exploredhex25 = True
jump DesertTownFar

label ExploreHex31:
$ explored = True
$ exploredhex31 = True
stop music
scene pizza01 with fade
if seenpizza == False:
    mc "What's this pizza place doing in the middle of nowhere? And there's a road, FINALLY! Leading up to it..."
    if withbe:
        be "They can't have that many customers, it's strange indeed."
    if withpe:
        pe "They can't have that many customers, it's strange indeed."
    mc "I guess we should investigate... I'm hungry for pizza anyway, haven't had one in years."
    if withbe:
        be "Yeah, go and stuff your mouth with pizza while I stay and keep an eye on the rig, as per usual..."
    if withpe:
        pe "Yeah, go and stuff your mouth with pizza while I stay and keep an eye on the rig, as per usual..."
    if withan:
        an "I want some pizza too! Can I come?"
        mc "No, it's too dangerous, I'll bring you a slice back if I get some."
    if witham:
        am "Junk food for a junk mind..."
        mc "Pff..."
    if withcy:
        cy "Do they have tar pizza you think?"
        mc "I very much doubt it."
    if withmo:
        mo "Be careful."
    if withru:
        ru "I'll stay back too and shoot anyone that comes along..."
    if withsu:
        su "I prefer sushi. Next time, try and find a sushi bar please."
    if withmi:
        mi "Junk food for a junk mind..."
        mc "Pff..."
    if withay:
        ay "I want some pizza too! Can I come?"
        mc "No, it's too dangerous, I'll bring you a slice back if I get some."
    if withza:
        za "I've never tasted pizza before..."
        mc "I'll bring you a slice back if I get some, Zara."
    if withgw:
        gw "I heard stuff about pizza parlors on Fox News. Not Good. Not good AT ALL."
    if withma:
        ma "Maybe I should start selling pizzas at the bar I reckon..."
    if withcl:
        cl "If you bring one back, maybe I could bless it?"
    if withla:
        la "Bring one back, I'd like to see what kind of tomatoes they use."
    if withba:
        ba "Bring one back, I like pizzas. It's an American invention we stole from someone else."
    if withde:
        de "Bring one back, a scientist's lab diet is essentially pizzas."
    jump PizzaInside
                                        
if seenpizza:
    if withbe:
        be "Are you hungry again?"
    if withpe:
        pe "Are you hungry again?"
    mc "Yep. Pizza, pizza, PIZZA! YUMMY!"
    if withbe:
        be "*sigh* Yeah, go and stuff your mouth with pizza while I stay and keep an eye on the rig, as per usual..."
    if withpe:
        pe "*sigh* Yeah, go and stuff your mouth with pizza while I stay and keep an eye on the rig, as per usual..."

label PizzaInside:
scene pizzainside
show pizzagirl01
show pizzabar
with dissolve
if seenmilking == False and seenpizza:
    so "Benvenutti to Mamma Sofia's Supa-Dupa Pizzas! Again... May I take your order please?"
if seenmilking == False and seenpizza == False:
    so "Benvenutti to Mamma Sofia's Supa-Dupa Pizzas! May I take your order please?"
if seenmilking:
    so "Benvenutti to Mamma Sofia's Supa-Dupa Pizzas again, Special Agent!"
$ seenpizza = True
if persistent.tipson and seenmilking == False:
    show pizzatip at tips with dissolve
    pause
    hide pizzatip
label PizzaDialogue:
menu:
    "What is this place? How can you even be in business???":
        hide pizzabar
        hide pizzagirl01
        show pizzagirl02
        show pizzabar
        with fastdissolve
        so "What-a are you implying? My pizzas are well known AND liked by my-a many young customers."
        hide pizzabar
        hide pizzagirl02
        show pizzagirl01
        show pizzabar
        with fastdissolve
        jump PizzaDialogue
    "Is this a 3PG by any chance?" if seenmilking == False:
        hide pizzabar
        hide pizzagirl01
        show pizzagirl02
        show pizzabar
        with fastdissolve
        so "Who wants to know?"
        if mcdeep == 5:
            mc "Hey, I'm from the Deep State, you can totally trust me."
        if mcdeep == 4:
            mc "I'm an aspiring Deep State agent. Just need one more faction point...."
            hide pizzabar
            hide pizzagirl02
            show pizzagirl04
            show pizzabar
            with fastdissolve  
            so "Ah, so you want some field training then?"
            mc "Ah yes, that's a good idea."
            hide pizzabar
            hide pizzagirl04
            show pizzagirl05
            show pizzabar
            with fastdissolve  
            so "Alright, let's-a go to the basement then, I was just about to milk our latest catch-a!"
            $ deeptraining = True
            jump PizzaBasement
        if mcdeep <= 3:
            mc "Err... I just heard about them on the news, that's all."
            hide pizzabar
            hide pizzagirl02
            show pizzagirl01
            show pizzabar
            with fastdissolve        
            so "I don't know nothin'. I ain't seen nothin'. May I take you order please?"
            jump PizzaDialogue
        hide pizzabar
        hide pizzagirl02
        show pizzagirl04
        show pizzabar
        with fastdissolve
        so "And who are you? I never heard nothin' about you."
        if deepnickname:
            mc "I'm Special Deep State Agent \"[name] the Intruder\", that's who I am."
            hide pizzabar
            hide pizzagirl04
            show pizzagirl03
            show pizzabar
            with fastdissolve        
            so "Ah, well why didn't you say so earlier, special agent \"[name] the Intruder\"! The merchandise is in the basement. It's for a pick-up and delivery I presume?"
            mc "Err... Yes, that's right. I'll pick it up and...err... deliver it."
            hide pizzabar
            hide pizzagirl03
            show pizzagirl05
            show pizzabar
            with fastdissolve  
            so "Alright, let's-a go then, one final milking and he'll be good-a to go!"
            $ lastmilking = True
            jump PizzaBasement
        if deepnickname == False:
            mc "I'm Special Deep State Agent [name] ma'am."
            hide pizzabar
            hide pizzagirl04
            show pizzagirl01
            show pizzabar
            with fastdissolve        
            so "Never heard of that name. Are you here for field training?"
            mc "Err, yes, that's right. Totally."
            hide pizzabar
            hide pizzagirl01
            show pizzagirl05
            show pizzabar
            with fastdissolve                    
            so "Alright, let's-a go to the basement then, I was just about to milk our latest catch-a!"
            $ deeptraining = True
            jump PizzaBasement
    "I'm here to pick up the merchandise. Special Deep State Agent \"[name] the Intruder\" at your service, ma'am." if deepnickname and seenmilking:
            hide pizzabar
            hide pizzagirl01
            show pizzagirl03
            show pizzabar
            with fastdissolve
            so "Ah, finally, this boy was starting to fill up my sperm-a tank to overfilling. I am-a glad the client finally wants him delivered!"
            hide pizzabar
            hide pizzagirl03
            show pizzagirl05
            show pizzabar
            with fastdissolve  
            so "Alright, let's-a go then, one final milking and he'll be good-a to go!"
            $ lastmilking = True
            jump PizzaBasement
    "I'd like a... err... How much does it cost anyway?":
        hide pizzabar
        hide pizzagirl01
        show pizzagirl04
        show pizzabar
        with fastdissolve
        so "Mamma Sofia always-a make-a pizza for free for the bambini. So it's free for you, my boy."
        mc "Alright! A \"Mega-Studa Pizza\" then. Whatever the hell that is."
        hide pizzabar
        hide pizzagirl04
        show pizzagirl03
        show pizzabar
        with fastdissolve        
        so "It's a gran pizza for mega-studi. Easy-peasy pizza, I have one made already."
        hide pizzabar
        hide pizzagirl03
        show pizzagirl05
        show pizzabar
        with fastdissolve        
        so "I'll go and get it. You'll see, Mamma Sofia make-a the best pizzas in the world!"
        hide pizzabar
        hide pizzagirl05
        show pizzagirl04
        show pizzabar
        show pizza
        with fastdissolve
        so "Here, enjoy your pizza!"
        jump PizzaEat
    "I'm outta here. This place is fishy.":
        hide pizzabar
        hide pizzagirl01
        show pizzagirl02
        show pizzabar
        with fastdissolve
        so "How dare-a you insult my pizzas! I don't even have a pizza marinera, how can it be fishy? Get out of here, mamma mia!"
        mc "Yeah, that's what I was about to do."
        jump LeavePizza
        
label PizzaEat:
hide pizzabar
hide pizza
hide pizzagirl04
show pizzagirl03
show pizzabar
with fastdissolve
play sound "Sounds/eating.mp3"
so "So? How is-a my pizza?"
mc "Ok, it'a great pizza, I agree. Thanks, Mamma Sofia! Now I'd better be on my way."
so "Come back anytime, bambino!"
$ pizzaeaten = True

label LeavePizza:
if withbe:
    scene pizza01
    show bellaout09
    with dissolve
    be "So, did you enjoy your pizza?"
    if pizzaeaten:
        mc "Yes, I did. It was a gran pizza for mega-studi like me."
        be "*sigh* Let's go back to the compound..."
    if pizzaeaten == False:
        mc "No, I smelt a rat. I think this place has something to hide, we might have to come back here..."
        be "Let's go back to the compound..."
    mc "Err... Yeah, sure. Yummy, yummy, yummy."
    pe "*sigh* Let's go back to the compound..."
    jump BackHex31
if withpe:
    scene pizza01
    show pennyout03
    with dissolve
    pe "So, did you enjoy your pizza?"
    if pizzaeaten:
        mc "Yes, I did. It was a gran pizza for mega-studi like me."
        pe "*sigh* Let's go back to the compound..."
    if pizzaeaten == False:
        mc "No, I smelt a rat. I think this place has something to hide, we might have to come back here..."
        pe "Let's go back to the compound..."
    mc "Err... Yeah, sure. Yummy, yummy, yummy."
    pe "*sigh* Let's go back to the compound..."
    jump BackHex31
if alone:
    jump BackHex31

label LeavePizza02:
if withbe:
    scene pizza01
    show bellaout09 at right
    with dissolve
    be "So, did you enjoy your pizza?"
    if rescuedmagnus:
        mc "I did not. But I enjoyed rescuing She-Hulk's son. Here he is."
        show magnus01 at left with moveinleft
        mg "Hello! I'm free at last!"
        hide bellaout09
        show bellaoutworry at right
        with fastdissolve
        be "Who the hell is that ENORMOUSLY-MUSCLED boy? You sure it's safe to bring him back?"
        mc "Yeah, no worries, I'll take care of him. We'll drop him off at the Red Canyon and don't say a word to Chief Lena please..."
        be "*sigh* Alright, let's go back to the compound."
        $ deeptraining = False
        jump BackHex31b
    mc "Err... Yeah, sure. Yummy, yummy, yummy."
    be "*sigh* Let's go back to the compound..."
    if deeptraining:
        $ deeptraining = False
    jump BackHex31 

if withpe:
    scene pizza01
    show pennyout03 at right
    with dissolve
    pe "So, did you enjoy your pizza?"
    if rescuedmagnus:
        mc "I did not. But I enjoyed rescuing She-Hulk's son. Here he is."
        show magnus01 at left with moveinleft
        mg "Hello! I'm free at last!"
        if withnone == False:
            hide pennyout03
            show pennyout01 at right
            with fastdissolve
            pe "Who the hell is that ENORMOUSLY-MUSCLED boy? We can't bring him back, my rig doesn't have enough seats!"
            mc "Ah, shit I hadn't thought of that... Err, sorry Magnus, but I'll have to leave you with Mamma Sofia until I come back and rescue you without taking any useless harem girl with me..."
            hide magnus01
            show magnus02 at left
            with fastdissolve
            mg "What? But... my mommy! You promised!"
            mc "And now I promise that I'll come back and rescue you. So everything will be fine, right?"
            mg "I... guess."
            mc "I'll tell Mamma Sofia there's been a hiccup and I'll pick you up later."
            hide magnus02
            hide pennyout01
            show pennyout03 at right
            with fade
            mc "And now, we can go back to the compound..."
            $ rescuedmagnus = False
            $ magnusbehind = True
            jump BackHex31
        if withnone:
            hide pennyout03
            show pennyout01 at right
            with fastdissolve
            pe "Who the hell is that ENORMOUSLY-MUSCLED boy? You sure it's safe to bring him back?"
            mc "Yeah, no worries, I'll take care of him. We'll drop him off at the Red Canyon and don't say a word to Chief Lena please..."
            pe "*sigh* Alright, let's go back to the compound."
            $ deeptraining = False
            jump BackHex31b
    mc "Err... Yeah, sure. Yummy, yummy, yummy."
    be "*sigh* Let's go back to the compound..."
    if deeptraining:
        $ deeptraining = False
    jump BackHex31
if alone:
    jump BackHex31
    
label PizzaBasement:
scene basement01 with fade
if seenmilking == False:
    so "The merchandise is for a very important-a lady. Before delivery, she asked for twenty gallons of \"Special Pizza Sauce\", I don't-a know why."
    mc "Maybe she's really hungry?"
    so "Ha ha, sure, she's-a \"hungry\" alright!" 
if seenmilking:
    so "He is still-a giving plenty of \"Special Pizza Sauce\" you'll be glad to know."
    mc "I'm sure the client will appreciate..."
scene basement02 with dissolve
if seenmilking == False:
    mc "And who's that guy?"
    so "It's Joe Bid'em, don't-a disturb him, he still thinks he's running his 2020 campaign, he's notta good in the head."
    jb "If you're black and you don't vote for me, then you're actually t-t-totally white!"
    jb "So vote for me, vote for Joe B-B-Bid... Hang on, what's my name again?"
if seenmilking:
    mc "Ah, he's still there..."
    jb "What are the latest polls? Am I gonna win? I saw a guy called \"Joe Bid'em\" was leading, who the hell is that guy and why am I t-t-trailing him?"
    mc "And he still doesn't remember his name..."
    so "I will let him sniff my hair later on so that-a he takes a nap and stoppa sitting in front of the computer."
    mc "Better \"Sleepy Joe\" than \"Demented Joe\", I agree..."
scene basement03 with dissolve
if deeptraining == False:
    so "There he is, our bigga boy, ready for his milking session. Would-a you like to watch, Special Deep State Agent?"
if deeptraining:
    so "There he is, our bigga boy, ready for his milking session. I'll let you watch so that-a you can learn."
if missionhulk and missionhulkdone == False:
    mc "(Hang on, I recognize him, it's She-Hulk's son!)"
if deeptraining == False or missionhulk == False:    
    mc "Err... Yeah, sure, I need to check that everything is done by the books."
if lastmilking == False:
    so "Oh, I assure you this is a very professional 3PG! The Mafia has been in the business for-a many years now."
if lastmilking and seenmilking:
    so "You've already seen me, you know I do everything-a very professionally."
    mc "Of course, it's just the regulations, you know."
so "Wait for me and watch over the boy, I will change into my pizza parlor ped*phile gang mafiosa boss outfit."

scene basement04 with dissolve
if missionhulk and missionhulkdone == False and seenmilking == False:
    mc "*low voice* Hey Magnus, I met your mom, she's waiting for you."
    mg "What, mommy? You found my mom?"
    mc "Yeah, I did, she's in a crater. I'll explain, but I don't have time right now."
    mg "I've been captured! Please help me mister! *sniff*"
    mc "I'll try and think of something, but in the meantime, play along her kinky games, alright?"
    mg "*sniff* Al...alright mister."
if missionhulk and missionhulkdone == False and seenmilking:
    mc "*low voice* Hey Magnus, I'm going to take you back to your mom, but play along her kinky games one last time, alright?"
    if toldmagnus == False:
        mg "What, mommy? You found my mom?"
        mc "Yeah, I did, she's in a crater. I'll explain, but I don't have time right now."
        mg "I've been captured! Please help me mister! *sniff*"
    if toldmagnus:
        mg "Really, you're going to take me back to her this time?"
        mc "Yeah, I promise, don't worry."
if missionhulk == False:
    mc "So, how is it hanging...err...so to speak?"
    mg "I've been captured! Please help me mister! *sniff*"
    mc "I don't know what to do, sorry buddy. I'd need a quest or something, but you're not on any of my current ones."
window hide
play sound "Sounds/footsteps.mp3"
$ renpy.pause(2.0, hard=True)
mc "Sssh, she's coming back."
stop sound
scene basement05 with dissolve   
mg "NOOOOO! Not again, please Mamma Sofia! You already milked me five times today! *sob*"
if lastmilking == False:
    so "I need MORE cream from you, my sweet bambino. Your cream is VERY valuable cos you are such a BIGGA STRONG boy!"
    mc "Please proceed with the cum extraction Mamma Sofia... I will watch and... err... take notes."
if lastmilking:
    so "It's your last milking, my sweet bambino. So make-a sure you give Mamma Sofia a VERY BIGGA LOAD!"
    mc "Please proceed with the cum extraction Mamma Sofia... I will take the merchandise over to the client aferwards."
if deeptraining:
    so "Yes, take notes and learn, this is essential field training for Deep State agents..."
    jump PizzaBasement02
if deepnickname == False:
    so "Of course Special Deep State Agent [name]."
if deepnickname:
    so "Of course, Special Deep State Agent \"[name] the Intruder\"."
label PizzaBasement02:
so "First, I will fit the merchandise with an XXXXXL-MEGA condom to capture his ENORMOUS boyloads."

scene basement06 with dissolve
play music "Sounds/vibrator.ogg"
so "And I will tease him with my edging stick to get him ROCK-HARD...."

scene basement07 with dissolve
so "See? He got rock-hard and ready for extraction in no time. Mamma Sofia's edging skills are that-a good, ha, my bigga boy?"
play sound "Sounds/boymoan.mp3"
mg "*sob* I... didn't want to get hard but..."
so "Don't-a worry, bambino, just let your juices flow and give Mamma Sofia a LOT of \special pizza sauce\"!"
stop music
scene basement08a with dissolve
so "There you go my bigga boy! Your stallion cock is a perfect fit for my 30-inch-around studcock gripper!"
play music "Sounds/wank.mp3"
scene basement08b with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08a with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08b with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08a with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08b with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08a with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08b with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08a with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08b with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08a with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08b with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08a with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08b with fastdissolve
$ renpy.pause(.2, hard=True)
stop music
scene basement09 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mg "AAAHHHH!"
so "That's a good-a strong boy! Give Mamma Sofia what-a she wants, a BIG load of young warm-a spunk!"
scene basement10 with dissolve
mg "OOOOH! AAAHHHH!"
so "You see this Special Deep State Agent? Another gallon of cum for-a the client. Now, I just need to empty the condom into the cum storage unit. Easy-peasy."
mc "Damn, how many gallons do you have already????"
if lastmilking == False:
    so "Oh, A LOT. This boy is the biggest cum supplier I've ever had, that's-a for sure!"
if lastmilking:
    so "Oh, A LOT. And enough now for you to deliver him to the client."

scene basementsofiabackground blurred
show mammasofia01
with dissolve
so "Before you go... I'll show you the automatic cum extraction procedure with the milking-a machine..."
hide mammasofia01
show mammasofia02
with fastdissolve
so "So we can have some fun time together, what do you say? *wink*"
mc "Well, it's not against Deep State regulations so..."
hide mammasofia02
show mammasofia03
with fastdissolve
so "I've seen that bulge in your pants. You are a BIGGA boy too. Big enough for Mamma Sofia to give her a LOTTA OF PLEASURE! Show it to me!"
play sound "Sounds/zipper.mp3"
hide mammasofia03
show mammasofia04
with fastdissolve
so "Mmmmh, Mamma Sofia is VERY impressed, young agent! Your cock is the PERFECT size. This boy is just too big, I don't-a know what the client wants to do with him..."
so "But let's show him how it's done so he's prepared for when he's delivered..."
mg "What? But... Mamma Sofia, please, I don't want to do that, let me go back to my mommy!"
so "Now now, bambino, just watch-a and learn, This STUD will show you the ropes."
scene sofiaprefuck01 with dissolve
mc "First, you moisten her pussy with your fingers to prep her fuckhole for your cock..."
so "Mmh, Mamma Sofia is sssoo wetta already! Please SHOVE IT IN!"
play music "Sounds/womansex02.mp3"
label SofiaFuckSlow:
hide sofiafast
show sofiaslow
call screen sofiafuckslow01
screen sofiafuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SofiaFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("SofiaFuckFast") 

label SofiaFuckFast:
mc "And now, I'll increase the pace to make her cum big time!"
so "Oooh, yes, Mamma Sofia is COMING!!! AAAH!"
hide sofiaslow
show sofiafast
call screen sofiafuckfast01
screen sofiafuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SofiaFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("SofiaFuckSlow") 

label SofiaFuckEnd:
mc "DUMPING MY LOAD INSIDE YOU! AAH!"
stop music
scene sofiafuckcum01 with dissolve
play sound "Sounds/boycum.mp3"
mg "AAAH!"
so "Yes bambini, come together, make Mamma Sofia proud!"
scene sofiafuckcum02 with dissolve
mc "Repainting your body with my cream! RHAAA!"
so "See that, my stronga boy? THIS is how you do it! He's coming EVERYWHERE, women LOVE that!"
mg "But I can't do that, my cum is getting sucked up by the pump! AAAH!"
so "That's because I need another gallon of spunk from you, bambino, so EXPLODE in the tube for Mamma Sofia!"
stop sound
scene sofiafuckcum03 with dissolve
so "I see you're both done... Mmh, and YOUR cum is DELICIOUS!"
$ seenmilking = True
if lastmilking and missionhulk:
    scene basementsofiabackground blurred
    show mammasofia01
    with dissolve
    so "I guess you can take-a the boy now. I'll give you a loincloth for him to go outside. Arrivederci, Special Agent!"
    mc "Yeah, thanks Mamma Sofia, I'll do that."
    $ rescuedmagnus = True    
    jump LeavePizza02
if lastmilking and missionhulk == False:
    scene basementsofiabackground blurred
    show mammasofia01
    with dissolve
    so "I guess you can take-a the boy now and deliver him to the client."
    mc "Yeah, about that. I just got a call from the client, she wants to delay the delivery."
    hide mammasofia01
    show mammasofia02
    with fastdissolve
    so "Oh? She wants-a more \"Special Pizza Sauce\", hey?"
    mc "Yeah, that's what she said. So... I'll come back another time."
    jump LeavePizza
    
so "I hope you learnt well, bambino! Just a few more gallons from you and you'll be good-a to go!"
scene basementsofiabackground blurred
show mammasofia01
with dissolve
so "Grazie for your help, Special Agent. I hope you learnt something too..."
if deeptraining:
    call PlusDeep
mc "I sure did, Mamma Sofia, I sure did... See you another time. I hope."
so "Arrivederci!"
jump LeavePizza

label BackHex31:
$ period += 1
scene command01
show lena01
with fade
le "So, what do you have to report about area D1, scouts?"
mc "I infiltrated a pizza parlor."
hide lena01
show lena03
with fastdissolve
le "A pizza parlor you say? And...what did you discover?"
if seenmilking == False and lastmilking == False:
    mc "That they make pretty decent pizzas."
    le "*sigh* And you think I pay you to eat pizza? SCOUTS DISMISSED!"
    hide lena03 with dissolve
    jump Main01    
if seenmilking or lastmilking:
    mc "I've learnt some interesting tidbits about 3PGs..."
    hide lena03
    show lena07
    with fastdissolve
    le "I see. You're fast acquiring valuable knowledge about the Deep State."
    if mcdeep == 5 and deepnickname == False:
        le "I shall therefore grant you a nickname for our faction. \"[name] the Intruder\"."
        window hide
        show mcdeepnickname at posmission
        $ renpy.pause(2.0, hard=True)
        pause
        hide mcdeepnickname
        $ deepnickname = True
        mc "Alright! Intrusion, here we come!"
    if withbe:
        be "What are you guys talking about? As a scout, I demand to know what's going on!"
        hide lena07
        show lena04
        with fastdissolve
        le "This is none of your concern at this stage Bella. SCOUTS DISMISSED."
        hide lena04 with dissolve
    if withpe:
        pe "What are you guys talking about? As a scout, I demand to know what's going on!"
        hide lena07
        show lena04
        with fastdissolve
        le "This is none of your concern at this stage Penny. SCOUTS DISMISSED."
        hide lena04 with dissolve
jump Main01

label BackHex31b:
$ period += 1
scene command01
show lena01
with fade
le "Ah, there you are, I just received an encrypted message on my home secret server from one of our top 3PG field agents..."
hide lena01
show lena10
with fastdissolve
le "She claims YOU did not deliver some \"merchandise\" to its rightful owner!"
mc "That kidnapped boy was actually the son of a very valuable NPC in this game. She'll help me get into Trumpf City potentially."
mc "Isn't that more important than delivering a kidnapped boy to some rich ped*phile?"
hide lena10
show lena05
with fastdissolve
le "You clearly don't UNDERSTAND how this works! You've meddled in the internal affairs of a 3PG and you've got yourself some powerful elite enemy now!"
mc "Pff! I ain't scared."
if renpy.seen_image("bountybackground01"):
    le "We'll see about that when you get ANOTHER bounty on your head!"
if renpy.seen_image("bountybackground01") == False:
    le "We'll see about that when you get a bounty on your head!"
hide lena05
show lena10
with fastdissolve
le "Clearly, the Deep State CANNOT TRUST YOU to do the RIGHT thing! You are DISMISSED! Restricted to your quarters for the rest of the day effective IMMEDIATELY!"
call MinusDeep
mc "What, I'm grounded???"
le "That's right, YOU ARE GROUNDED!"
$ melaniabounty = True
$ period = 4
$ clearedhex31 = True
scene bedroom01 with fade
if girlsinharem == 0:
    mc "This sucks. Well, I can go to sleep I guess."
if girlsinharem >= 1:
    mc "Pff, this sucks. At least, I can invite a girl over for some sex I guess."
if bounty:
    jump Bedroom 
if bounty == False:
    show messagesign
    mc "Oh, it looks like I have a message. I'll check the interface."
    hide screen calendar
    hide screen mcstats
    scene interface01
    if siriclothes == 1:
        show siri03aa with fastdissolve
    if siriclothes == 2:
        show siri03ba with fastdissolve
    if siriclothes == 3:
        show siri03ca with fastdissolve
    si "You have received an urgent message from First Lady Melania. I think you should see it this time."
    mc "What the hell does she want now?"
    scene melania01 with dissolve
    show whitehouseframe
    me "It's me, First Lady Melania and double-secret Deep State Special Field Agent, codename \"Trophy\". You did something terrible, not good at all."
    play sound "Sounds/melania02.mp3"
    me "You shouldn't fight against the super-elites, we always get what we want. I wanted that boy, Magnus. He was mine. I paid good money for him."
    scene melania02 with dissolve
    show whitehouseframe
    me "I have my desires that my very busy tweeting husband cannot fulfill. How am I supposed to stay entertained? My life is dull and I was looking forward to playing with Magnus, my new sexual toy."
    me "And now you've taken him away from me. This is not good at all. Now I have to put a bounty on your head. I didn't want to, but you forced me to."
    scene melania03 with dissolve
    show whitehouseframe
    me "So stop being such a pain in the backside. Or BE AN ACTUAL PAIN IN MY BACKSIDE BY RAMMING YOUR POLE IN MY ASS! Come and get me. Or I'll come and get you..."                                                                                                                                      
    hide whitehouseframe
    scene interface01 with fade
    if siriclothes == 1:
        show siri04aa with fastdissolve
    if siriclothes == 2:
        show siri04ba with fastdissolve
    if siriclothes == 3:
        show siri04ca with fastdissolve
    mc "Well, that sounded threatening."
    si "You are correct. I have noticed that most home secret servers, which I can easily access due to their lax security, have received the following ominous picture attachment."
    window hide
    show bounty at posmission
    $ renpy.pause(1.0, hard=True)
    pause
    $ knowmelaniabounty = True
    if renpy.seen_image("bountybackground01"):
        mc "What? Not again!"
    if renpy.seen_image("bountybackground01") == False:
        mc "Well thanks for letting me know Siri..."
    $ metme = True
    jump Bedroom

label ExploreHex32:
scene crater01 with dissolve
play music "Sounds/desertwind01.mp3"
if rescuedmagnus and withbe:
    be "So I'm guessing you're gonna go down this hellhole with that boy then, is that the plan? You might have forgotten the fact that HE doesn't have a gas mask."
    mc "I think he'll be fine. She-Hulk has a... secret antidote."
    mg "I'll risk anything to see my mom again!"
    be "Fine, I'll just wait here and guard my rig then..."
    jump Radioactive03
if rescuedmagnus and withpe:
    pe "So I'm guessing you're gonna go down this hellhole with that boy then, is that the plan? You might have forgotten the fact that HE doesn't have a gas mask."
    mc "I think he'll be fine. She-Hulk has a... secret antidote."
    mg "I'll risk anything to see my mom again!"
    pe "Fine, I'll just wait here and guard my rig then..."
    jump Radioactive03    

if seenhulk:
    if alone and withnone:
        mc "Let's get down the crater again..."
        jump Radioactive02
    if withbe:
        be "Why are we back here? You already went down in the crater..."
        mc "Yeah, but I don't think I saw everything. What with all that radioactive green fog everywhere. You stay behind, I'll be back in an hour or so..."
    if withpe:
        pe "Why are we back here? You already went down in the crater..."
        mc "Yeah, but I don't think I saw everything. What with all that radioactive green fog everywhere. You stay behind, I'll be back in an hour or so..."
    if alone and withnone == False:
        call AloneStance
    jump Radioactive02
mc "That doesn't look like a nice place... What's with all the green shit everywhere?"
if withbe:
    be "It might be the crater from a nuclear explosion. My Geiger counter is all over the place. We'd better leave now!"
if withpe:
    pe "It might be the crater from a nuclear explosion. My Geiger counter is all over the place. We'd better leave now!"
menu:
    "I agree, better safe than sorry.":
        jump BackHex32        
    "Hang on, I have a mask that should protect me. I'll go and investigate." if gasmask:
        if withbe:
            be "I'm not equipped, so it will be without me..."
            mc "OK, I'll report back in an hour or so. Don't leave without me."
            be "I'll be right here waiting for you [name]..."
        if withpe:
            pe "While I would love to come with you on this exciting adventure, I think I'll stay back and guard my motorbike..."
            mc "OK, I'll report back in an hour or so. Don't leave without me."
            pe "I'll be right here waiting for you [name]..."
        $ maskon = True
        jump Radioactive02        
    "Radioactivity, schmadioactivity. I ain't scared of nothing I can't see!":
        if withbe:
            be "Well, I'm not sure whether you're very brave or very stupid, but you'll go alone..."
            mc "The answer is: I'm very brave."
            be "Right. Well, I'll be right here waiting for you, brave boy..."
        if withpe:
            pe "Well, I'm not sure whether you're very brave or very stupid, but you'll go alone..."
            mc "The answer is: I'm very brave."
            pe "Right. Well, I'll be right here waiting for you, brave boy..."        
        jump Radioactive02
        
label Radioactive02:
scene crater02 with dissolve
if seenhulk:
    mc "I should put my mask on, even if She-Hulk doesn't like it."
    jump Radioactive03
if maskon:
    mc "That green fog is getting worse. oh, well. Down we go..."
    jump Radioactive03
if maskon == False:
    mc "That green fog is getting worse. And it's actually very sandy too... *cough*"
    call MCInjury
    $ mcinjuredsand = True
    play sound "Sounds/cough.mp3"
    mc "I can't go on like that. *cough*. I should head back."
    $ craterfail = True
    jump CraterBack

label Radioactive03:
scene crater03
stop music
play music "Sounds/mask.mp3"
show greenmist
with dissolve
mc "I can barely see a thing in this green fog..."
play sound "Sounds/hulkgrowl01.mp3"
"GRRR!"
if seenhulk == False:
    mc "What was that?"
if seenhulk:
    mc "Ah, there she is, greeting me in her tender voice once again."
window hide
hide greenmist
show shehulk01
with dissolve
play sound "Sounds/hulkgrowl01.mp3"
$ renpy.pause(1, hard=True)
if seenhulk == False:
    mc "An 8ft tall She-Hulk! Fortunately, she seems to be shackled at the ankles..."
    sh "AAAAR! MASK....BAD MAN... GRRR!"
    play sound "Sounds/hulkgrowl02.mp3"
    mc "She seems pissed off..."
    menu:
        "Remove your mask":
            mc "Maybe she think I'm her captor because of my mask. So I'll remove it."
            stop music
            show shehulk01b with dissolve
            mc "*cough* I'm getting... radioactive sand... *cough*  in my lungs."
            call MCInjury
            $ mcinjuredsand = True        
            jump SheHulk02
        "Keep your mask and approach her":
            mc "Well, she's in shackles. She can't hurt me, right?"
            jump SheHulk03
        "Keep your mask and get the hell out of here":
            mc "Doesn't look good... I'm outta here."
            jump CraterBack
if seenhulk and missionhulk == False:
    mc "Good, she's still shackled at the ankles..."
    sh "AAAAR! MASK....BAD MAN... GRRR!"
    play sound "Sounds/hulkgrowl02.mp3"
    menu:
        "Remove your mask":
            mc "Maybe she think I'm her captor because of my mask. So I'll remove it."
            stop music
            show shehulk01b with dissolve
            mc "*cough* I'm getting... radioactive sand... *cough*  in my lungs."
            call MCInjury
            $ mcinjuredsand = True        
            jump SheHulk02
        "Keep your mask and approach her":
            mc "Well, she's in shackles. She can't hurt me, right?"
            jump SheHulk03
        "Keep your mask and get the hell out of here":
            mc "Doesn't look good... I'm outta here."
            jump CraterBack
if seenhulk and missionhulk and rescuedmagnus:
    mc "It's ME, She-Hulk! Don't you recognize my HUGE muscles?"
    sh "MAGNUS... WHERE IS... MAGNUS?"
    mc "I rescued him! He's right behind me, coughing his lungs out cos he doesn't have a mask like me..."
    jump HulkMagnusMeet
if seenhulk and missionhulk and rescuedmagnus == False:
    mc "It's ME, She-Hulk! Don't you recognize my HUGE muscles?"
    sh "MAGNUS... WHERE IS... MAGNUS?"
    mc "Ah yes, about that... I'm still looking for him but I thought we could talk abo..."
    jump SheHulk03
    
label SheHulk03:
$ seenhulk = True
hide shehulk01
show shehulk02
with dissolve
play sound "Sounds/hulkgrowl02.mp3"
mc "Ah, FUCK, she bit me!"
call MCInjury
$ mcinjuredfight = True        
mc "I'd better leave, she's nuts. And dangerous."
jump CraterBack

label SheHulk02:
$ seenhulk = True
scene crater04
show shehulk03
with dissolve
sh "AAAR... COME... BOY... DRINK... MILK... GOOD... SAFE..."
mc "Mmmh, Green Giant milk. Can't be that bad, right?"
hide shehulk03
show shehulk04
with dissolve
play sound "Sounds/sucking.mp3"
$ mcinjured = False
$ mcinjuredsand = False
mc "Oh wow, it seems to have cured me of my injuries..."
scene crater03 blurred
show shehulk05
with dissolve
sh "MILK... GOOD..."
mc "Yes, very good. Thank you."
sh "Boy... Me... BREED... BABIES!"
mc "Ah. I should have seen this one coming."
mc "Alright, lady. I'll get undressed and show you my mighty HERO COCK."
play sound "Sounds/zipper.mp3"
hide shehulk05
show shehulk06
with dissolve
sh "BOY... BIG COCK... GOOD..."
mc "That's right, she-hulk! And there's plenty of cream sloshing around in my cum factories to satisfy your needs for breeding!"
hide shehulk06
show shehulk07
with dissolve
play sound "Sounds/lick.mp3"
sh "BIG BALLS... SPERM... LOT OF SPERM... *lick*"
mc "Yeah, make them warm and shiny with your tongue... And I'll give you LOTS OF SPERM. AAAH!"
hide shehulk07
show shehulk08
with dissolve
play sound "Sounds/hulkgrowl01.mp3"
sh "GRR! BOY... FUCK... NOW!"
mc "Yeah, OK, I'll fuck you, don't worry! But please don't crush my cock with your ass muscles."

scene crater04 blurred
show shehulkpredoggy01
with dissolve
play sound "Sounds/hulkgrowl02.mp3"
sh "AAAR! NOW!"
mc "Yeah, hang on, I'm trying to get it in... You might be a giant she-hulk, but my cock is still XXXL-sized!"
hide shehulkpredoggy01
show shehulkdoggy00
with fastdissolve
mc "Damn, she's quite tight despite being 8ft tall... Her pussy muscles are gripping my knob... Here we go!"
hide shehulkdoggy00
play music "Sounds/fucksound.mp3"
label SheHulkFuckSlow:
hide shehulkfast
show shehulkslow
call screen shehulkslow01
screen shehulkslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SheHulkFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("SheHulkFuckFast") 

label SheHulkFuckFast:
mc "I think she wants me to fuck her FASTER."
hide shehulkslow
show shehulkfast
call screen shehulkfast01
screen shehulkfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SheHulkFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("SheHulkFuckSlow") 

label SheHulkFuckEnd:
mc "Time to unload in that green pussy..."
stop music
hide shehulkslow
hide shehulkfast
show shehulkcum01
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Yeah, take my seed, She-Hulk! AAAH!"
hide shehulkcum01
show shehulkcum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "RHAA! Gonna paint your skin white again!"
play sound "Sounds/hulkgrowl01.mp3"
mc "Ok, I'll stop and flood your insides... Calm down..."
hide shehulkcum02
show shehulkcum03
with dissolve
mc "There. Is that better?"
play sound "Sounds/womanmoan.mp3"
mc "See, you can have a tender voice. When you're receiving ounces of cum in your womb!"
mc "Now, if you don't mind, I've done my duty and I'll be on my merry way..."
play sound "Sounds/hulkgrowl02.mp3"
sh "GGRRR... NO!"
scene crater04 blurred
show shehulk09
with dissolve
mc "What's that?"
sh "MAGNUS... SON... BACK..."
mc "I see. You want me to find your son and bring him back to this dreadful place?"
if persistent.tipson:
    show hulktip at tips with dissolve
    pause
    hide hulktip            
sh "YES... MAGNUS... NEEDS MOMMY...."
window hide
show hulkquest at posmission
$ renpy.pause(1.0, hard=True)
pause
hide hulkquest
$ missionhulk = True
jump CraterBack

label HulkMagnusMeet:
scene crater03
show hulksexbackground
with dissolve
show magnusmeethulk01 at left with moveinleft
show magnusmeethulk02 at right with moveinright
sh "MAGNUS...MOMMY!"
mg "Mom! Yippee, I found you... (cough)... again!"
mc "That scene's gonna make for fascinating conversation I fear..."
sh "Drink... MOMMY... MILK..."
mc "Yeah, you go ahead buddy, it's good, I can vouch for it. Ahem."
scene crater03 blurred
show hulkmagnusmilk01
with dissolve
play sound "Sounds/sucking.mp3"
mg "Mmmh, just like I remember it."
sh "BABY...GOOD....MOMMY... CHECK ON YOU..."
hide hulkmagnusmilk01
show hulkmagnusmilk02
with dissolve
play sound "Sounds/ripping.mp3"
mc "Oh, oh, she found out about his MONSTER cock. Was bound to happen, right?"
sh "MAGNUS... COCK... SO BIG! MOMMY... LOVE!"
mc "Of course, she's not really human anymore, so it's no longer inc*st at all. Which makes it perfectly suitable for Patreon audiences around the world."
menu:
    "I'm a snowflake and I don't want to watch the ensuing MMF threesome scene (SKIP SCENE)":
        jump SheHulkDiamondEnd
    "I'm not a snowflake and I DO want to see the MMF threesome scene":
        pass
hide hulkmagnusmilk02
show hulkmagnusprelick01
with dissolve
play sound "Sounds/lick.mp3"
mg "But mommy.... What are you doing? AAAH, your tongue... it feel so good!"
mc "You wait till she dislocates her jaws and engulfs your entire helmet, buddy...."
hide hulkmagnusprelick01
show hulkmagnusprelick02
with dissolve
mg "AAAH! MOMMMYYY!"
mc "I think it's about to happen..."
play sound "Sounds/crunch.mp3"
hide hulkmagnusprelick02
show hulksexbackground
show hulkmagnusblow01
with fastdissolve
mg "Mommy... You're swallowing my...."
stop sound
mc "Cock. Yeah, she's blowing you basically. Enjoy."
window hide
play music "Sounds/hardsucking.mp3"
hide hulkmagnusblow01
show hulkmagnusblow02
with fastdissolve
pause 0.2
hide hulkmagnusblow02
show hulkmagnusblow01
with fastdissolve
pause 0.3
hide hulkmagnusblow01
show hulkmagnusblow02
with fastdissolve
pause 0.2
hide hulkmagnusblow02
show hulkmagnusblow01
with fastdissolve
pause 0.3
hide hulkmagnusblow01
show hulkmagnusblow02
with fastdissolve
pause 0.2
hide hulkmagnusblow02
show hulkmagnusblow01
with fastdissolve
pause 0.3
hide hulkmagnusblow01
show hulkmagnusblow02
with fastdissolve
pause 0.2
hide hulkmagnusblow02
show hulkmagnusblow01
with fastdissolve
pause 0.3
hide hulkmagnusblow01
show hulkmagnusblow02
with fastdissolve
pause 0.2
hide hulkmagnusblow02
show hulkmagnusblow01
with fastdissolve
pause 0.3
hide hulkmagnusblow01
show hulkmagnusblow02
with fastdissolve
pause 0.2
hide hulkmagnusblow02
show hulkmagnusblow01
with fastdissolve
pause 0.3
hide hulkmagnusblow01
show hulkmagnusblow02
with fastdissolve
pause 0.2
hide hulkmagnusblow02
show hulkmagnusblow01
with fastdissolve
pause 0.3
play sound "Sounds/boymoan.mp3"
mg "AAAAH!"
mc "Looks like he's about to blow..."
stop music

hide hulkmagnusblow01
show hulkmagnusblowcum01
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mg "OOOOH, I'm pumping my seed in your mouth MOMMMMMYYY!"
mc "Yeah, make her GAG on it, Magnus, I can tell she wants to!"
hide hulkmagnusblowcum01
show hulkmagnusblowcum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
sh "Mmmgggbbb, CUM... SON..."
hide hulkmagnusblowcum02
show hulkmagnusblowcum03
with fastdissolve
sh "MOMMY... PROUD... LOTS OF CUM... NOW FUCK MOMMY..."
mc "Can I join the fuckfest this time She-Hulk pretty please?"
sh "YOU... GIVE ME COCK... IN MOUTH... FUCK MY FACE...."
mc "Alright! Let's do it Magnus, you fuck her giant gaping green pussy with your monstercock and I'll fuck her mouth with mine, okay?"
mg "Err... Okay, mister..."

scene crater04
show hulksexbackground
show hulkmagnusprefuck01
with dissolve
mc "I'm ready, already half my cock is buried in your mom's mouth. Now shove yours into her moist cunt, Magnus!"
mg "I...don't know how it could fit...."
mc "Let the dev worry about that. Her pussy will distend enough for it to fit, trust me."
sh "MAGNUS... FUCK.... MOMMY..."
mg "O...Okay."
scene crater03 blurred
play music "Sounds/fucksound.mp3"
label MagnusFuckSlow:
hide hulkmagnusfast
hide POVhulkmagnusslow
hide POVhulkmagnusfast
show hulksexbackground
show hulkmagnusslow
call screen hulkmagnusslow01
screen hulkmagnusslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MagnusFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MagnusFuckFast") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("MagnusFuckPOVSlow") 
        
label MagnusFuckPOVSlow:
hide POVhulkmagnusfast
hide hulkmagnusfast
hide hulkmagnusslow
show POVhulkmagnusslow
call screen hulkmagnuspovslow01
screen hulkmagnuspovslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MagnusFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MagnusFuckPOVFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MagnusFuckSlow") 

label MagnusFuckPOVFast:
hide POVhulkmagnusslow
hide hulkmagnusfast
hide hulkmagnusslow
show POVhulkmagnusfast
call screen hulkmagnuspovfast01
screen hulkmagnuspovfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MagnusFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MagnusFuckPOVSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MagnusFuckFast") 

label MagnusFuckFast:
hide hulkmagnusslow
hide POVhulkmagnusslow
hide POVhulkmagnusfast
show hulksexbackground
show hulkmagnusfast
call screen hulkmagnusfast01
screen hulkmagnusfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MagnusFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MagnusFuckSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("MagnusFuckPOVFast") 

label MagnusFuckEnd:
mc "God, I'm close..."
mg "Me too, I can't hold it anymore, AAAH!"
hide hulkmagnusslow
hide hulkmagnusfast
hide POVhulkmagnusslow
hide POVhulkmagnusfast
stop music
play channel1 "Sounds/splooge02.mp3"
if persistent.cumsoundon:
    play channel2 "Sounds/mccum.mp3"
scene crater04 blurred
show hulksexbackground
show hulksexcum01
with dissolve
mg "AAAH, MOMMY, I'm cumming inside you!"
mc "Fuck, I'm about to blow too!"
scene crater03 blurred
show hulksexpovcum01
stop channel2
play sound "Sounds/boycum.mp3"
mc "Nutting right down She-Hulk's throat, RHAAAA!"
hide hulksexpovcum01
show hulksexpovcum02
with dissolve
mc "Here, take that on your face She-Hulk!"
sh "SPERM.... GOOOD.... MMMH...."
stop channel1
play sound "Sounds/splooge01.mp3"
mc "Yeah, you like that, hey? Your son is filling you up with his boygoo too what I can hear back there... Why don't you pull out and cover your mom's tits with it Magnus?"
scene crater04 blurred
show hulksexcum02
with dissolve
stop channel1
stop channel2
play sound "Sounds/splooge01.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Hey, watch out where you're aiming those massive jets of spunk buddy!"
sh "MAGNUS SPERM... LOTS OF IT... MOMMMY... SSSOOO PROUD..."
mc "I'm still hard and I have a bit of time. What about you Magnus, ready for another round?"
mg "Y...Yes, I think so."
sh "YOU TWO... FUCK ME... STANDING UP..."
mc "Alright! I'll take her ass cos I don't think you'll manage to squeeze that THING back there, even in your mom. Maybe in the future, with some practice..."


scene crater05
show hulksexbackground
with dissolve
play channel1 "Sounds/wank.mp3"
play channel2 "Sounds/barbarasex.mp3"
label HulkUpSlow:
hide hulkupfast
show hulkupslow
call screen hulkupslow01
screen hulkupslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HulkUpEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("HulkUpFast") 

label HulkUpFast:
sh "FUCK ME... FASTER!"
hide hulkupslow
show hulkupfast
call screen hulkupfast01
screen hulkupfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HulkUpEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("HulkUpSlow") 

label HulkUpEnd:
mc "That ass is ssso tight... I think I'm gonna cum soon!"
mg "Me...Me too!"
sh "COME... TOGETHER... IN MY HOLES..."
stop channel1
stop channel2
play sound "Sounds/boycum.mp3"
scene crater06
show hulksexbackground
show hulkupcum01
with dissolve
mc "Fuck, blowing right in your poopchute, She-Hulk!"
mg "AAAH, MOMMY, I'm CUMMING AGAIN INSIDE YOU!"
sh "GOOD BOY... CUM...IN MOMMY..."
stop sound
hide hulkupcum01
show hulkupcum02
with dissolve
sh "MMMMH... STILL HARD... FUCK MOMMY MORE..."
mc "Okay, I'm done guys and it's getting late, I'll leave you getting to know each other better..."
label SheHulkDiamondEnd:
scene crater03 blurred
show hulkdiamonds 
with dissolve
sh "BEFORE GO... GIFT... BOY... TAKE..."
window hide
show gemsparkling02
$ renpy.pause(0.1, hard=True)
hide gemsparkling02
$ renpy.pause(0.05, hard=True)
show gemsparkling02
$ renpy.pause(0.1, hard=True)
hide gemsparkling02
$ renpy.pause(0.05, hard=True)
show gemsparkling02
$ renpy.pause(0.1, hard=True)
hide gemsparkling02
$ renpy.pause(0.05, hard=True)
show gemsparkling02
$ renpy.pause(0.1, hard=True)
hide gemsparkling02
$ renpy.pause(0.05, hard=True)
show gemsparkling02
$ renpy.pause(0.1, hard=True)
$ hulkgem = True
window hide
show gems at posmission
$ renpy.pause(2.0, hard=True)
pause
hide gems
hide gemsparkling02
$ clearedhex32 = True
if gem == True:
    mc "(Ah, another haul of diamonds. I'm gonna be able to open a jeweller's shop soon...)"
    mc "ME...THANK...YOU...BYE..."
    mg "And thanks again for rescuing me from that horrible pizza parlor place [name]!"
jump CraterBack

label CraterBack:
stop sound
stop music
scene crater01 with fade
if hulkgem and alone:
    mc "I did my duty as a HERO and I cleared the area. I shall never be able to come back here again so let's enjoy the view of this magnificent radioactive crater one last time..."
    jump BackHex32
if hulkgem and withbe:
    show bellaoutworry
    be "Ah, I was starting to get worried, you took a while just to bring Magnus back to his mother..."
    mc "Well, you know, family reunions... They can take a while."
    be "Let's head back to the compound, it's getting late."
    jump BackHex32
if hulkgem and withpe:
    show pennyout03
    pe "You took a while just to bring Magnus back to his mother... What happened down there?"
    mc "Well, you know, family reunions... They can take a while."
    pe "Let's head back to the compound, it's getting late."
    jump BackHex32
if withbe:
    show bellaoutworry
    be "So, what was down there?"
if withpe:
    show pennyout03
    pe "So, did you find anything down there?"
if craterfail:
    mc "Err... No, the sand carried by that green fog was too much for my lungs. *wheeze* I'm actually injured, as that little icon on the top left corner clearly indicates."
    if withbe:
        hide bellaoutworry
        show bellaout09
        with fastdissolve
        be "I told you not to go down there! Let's head back to the compound then."
    if withpe:
        hide pennyout03
        show pennyout01
        with fastdissolve        
        pe "I told you not to go down there! Let's head back to the compound then."
    jump BackHex32
if missionhulk:
    mc "Oh, nothing, just another quest to do for the HERO here!"
    if withbe:
        hide bellaoutworry
        show bellaout09
        with fastdissolve
        be "Whatever, as long as we leave this stinking place NOW. Let's go back to the compound."
        jump BackHex32
    if withpe:
        hide pennyout03
        show pennyout01
        with fastdissolve
        pe "Whatever, as long as we leave this stinking place NOW. Let's go back to the compound."
        jump BackHex32
if missionhulk == False:
    mc "Some monstrous 8ft tall super-busty muscle lady. Didn't hang around to ask for her name, she seemed MEAN."
    if withbe:
        hide bellaoutworry
        show bellaout09
        with fastdissolve
        be "That's strange, what was she doing down there? We really should investigate further another time. But for now, let's go back to the compound."
        jump BackHex32
    if withpe:
        hide pennyout03
        show pennyout01
        with fastdissolve
        pe "That's strange, what was she doing down there? We really should investigate further another time. But for now, let's go back to the compound."
        jump BackHex32
mc "I should head back to the compound, it's getting late..."

label BackHex32:
$ exploredhex32 = True
stop music
$ period += 1
scene command01 with fade
show lena01
le "So, what do you have to report about area D2, scouts?"
if clearedhex32:
    mc "I completed yet another quest, Chief Lena!"
    hide lena01
    show lena03 
    with fastdissolve
    le "Meaning?..."
    mc "That hex D2 is cleared."
    le "And that's it?"
    mc "Yep. Pretty good, hey?"
    hide lena03
    show lena06 
    with fastdissolve
    le "I guess so. SCOUTS DISMISSED!"
    hide lena06 with dissolve
    jump LeaveCommand
if craterfail:
    mc "We found... *wheeze*... A crater left behind by a nuclear bomb. *hiss*"
    if withbe:
        be "[name] got some radioactive sand in his lungs by being foolishly brave."
    if withpe:
        pe "[name] got some radioactive sand in his lungs by being foolishly brave."
    hide lena01
    show lena06 
    with fastdissolve
    le "Well, you'd better head to the medbay then. SCOUTS DISMISSED!"
    $ craterfail = False
    jump Medbay
if seenhulk:
    mc "We found a crater left behind by a nuclear bomb. And there was this 8ft tall green She-Hulk in it."
    hide lena01
    show lena03 
    with fastdissolve
    le "What? A She-Hulk???"
    mc "That's right. Kind of dirty green more than dark green like in the comics, and with shorter hair. But still, I call her \"She-Hulk\", and so does the dev."
    hide lena03
    show lenapensive
    with fastdissolve
    le "She might be a secret Trumpf Militia weapon for all we know... We should investigate this further. SCOUTS DISMISSED."
    if mcinjured:
        mc "And I should head to the medbay..."
        jump Medbay
    mc "Roger that, Chief!"
    hide lenapensive with dissolve
    jump LeaveCommand
           
label ExploreHex33:
play music "Sounds/desertwind01.mp3"
$ exploredhex33 = True
scene frenchbackgroundfar
with fade
mc "There are some tanks over there, I hope it's not the Trumpf Militia..."
if alone:
    mc "Since they've probably spotted me already, I might as well approach them and look as innocent as possible..."
if withbe:
    be "They've probably spotted us already. If we flee, they'll shoot at us."
    mc "Right, so we should approach and pretend we're lost or something. That should work."
if withpe:
    pe "They've probably spotted us already. If we flee, they'll shoot at us."
    mc "Right, so we should approach and pretend we're lost or something. That should work."

scene frenchbackground
with dissolve
stop music
$ exploredhex33 = True
mc "Oh oh, that guy over there looks like he's in bad shape... And what is that insignia on these tanks I wonder?"
if withbe:
    be "I don't recognize it... It looks foreign to me. It's definitely not the Trumpf Militia at least."
if withpe:
    pe "I don't recognize it... It looks foreign to me. It's definitely not the Trumpf Militia at least."
if withsu:
    su "I've seen that insignia before, it belongs to the French Foreign Legion. Finally, my learning French might come in handy!"
window hide
show french02 with moveinright
we "(in French) Sergeant Wendy Royal-with-Cheese, 2nd Division Blindée de la Légion Etrangère! State your\n\ \ name and business..."
if mcfrench >= 5:
    mc "Oh, I understood that! Err... Moi [name] le HERO!"
    hide french02
    show french01
    with fastdissolve
    jump FrenchSpeak
if mcfrench <= 4:
    mc "Didn't get a bloody word of that. Why can't these foreigners speak English like everyone?"
    if withsu:
        su "I understood what she said and she confirmed she's from the Foreign Legion. Let me do the talking, she is armed to the teeth and we should not offend her."
        hide french02
        show french06
        with fastdissolve
        we "(in French) Answer me or I'll shoot!"
        su "(in French) I'm Suki and this is [name]. We come in peace. We are A-ME-RI-CANS."
        hide french06
        show french03
        with fastdissolve
        we "(in English) Yeah, I know you are, I'm American too. I joined the Foreign Legion cos the pay is much better than anything I could get around here."  
        su "See? Having brains helped us out here!"
        call LustPlusSuki
        mc "I'll grant you that Suki, well done! But having HUGE MUSCLES like me helps a lot MORE in most cases..."        
        jump FrenchSpeak02
    show microntalk with fastdissolve
    if alone and withnone:
        cm "(in French) We're wasting our time with this boy. Tell him to go away, sergeant! Ouch, my stomach..."
    if alone == False or withnone == False:
        cm "(in French) We're wasting our time with these people. Tell them to go away, sergeant! Ouch, my stomach..."
    hide french02
    show french06
    with fastdissolve
    we "Go...Go...Go... Ou je shoote."
    hide microntalk with fastdissolve
    mc "Alright, alright, gee, foreigners invade our land and then they kick us out. That never happened before in North America, it's simply unheard of!"
    if persistent.tipson:
        show hex33atip at tips with dissolve
        pause
        hide hex33atip
    jump BackHex33

label FrenchSpeak:
we "(in English) I must say, your French is pretty good actually. I'm very impressed."
mc "What, so you speak English???"
hide french01
show french03 
with fastdissolve
we "Well of course, I'm American. I joined the Foreign Legion cos the pay is much better than anything I could\n\ \ get around here."
label FrenchSpeak02:
mc "Well, why didn't you say so to begin with?!?!"
hide french03
show french02 
with fastdissolve
we "Yeah, sorry about that, but Capitaine Micron insists we speak French. He claims that when we finally meet someone who understands us, it will mean we're finally in Louisiana."
mc "Well, I'm pretty sure you're not in Louisiana. Louisiana is in the south, and this is hex D3."
hide french02
show french01
with fastdissolve
we "Ah, I didn't know, I suck at geography. Like most Americans."
we "As soon as he gets better, we'll head south then, thanks for the tip. We've been heading due west so far."
show microntalk with fastdissolve
cm  "Coq-au-vin... Camembert... Aaah... Omelette du fromage... Mmh..."
mc "What's wrong with him? What is he babbling about?"
hide microntalk with fastdissolve
hide french01
show french04
with fastdissolve
we "Bad stomach cramps. He can't take McCamel burgers anymore, and that's all we've been eating, ever since we left Trumpf City."
mc "You were in Trumpf City?"
hide french04
show french03 
with fastdissolve
we "Yeah, sure, Capitaine Micron was the official emissary of Président-C'est-La-Vie Macron, and he bought Louisiana from President Trumpf for one million new francs."
mc "What, Trumpf sold Louisiana to France???"
hide french03
show french02 
with fastdissolve
we "Yeah, he tried to throw Puerto Rico in the lot too, but Macron didn't want that since it's surrounded by some BIG water. Ocean water, apparently."
we "So now that we have the official deed, we're looking for Louisiana to claim it back for France basically. But we don't know where it is."
if map:
    $ clearedhex33 = True
    mc "I have a road map!"
    hide french02
    show french01
    with fastdissolve
    we "Really? Let me see it, it could be useful to us."
    mc "And what do I get in return?"
    show microntalk with fastdissolve
    if alone == False or withnone == False:
        cm "(in French) Just take the map from them and... Ouch! ...get rid of them!"
    if alone and withnone:
        cm "(in French) Just take the map from him and... Ouch! ...get rid of him!"
    hide microntalk
    hide french01
    show french06
    with fastdissolve
    we "Sorry, but I'll take the map and you'll just have to leave NOW. Or I'll shoot you!"
    mc "Hey, that's not very nice, I gave you a map, godammit!"
    $ map = False
    we "I'm really sorry but orders are orders. He won't budge when he's in such a foul mood and he's in a bad mood cos he hasn't eaten any decent food in days."
    if nasafood >= 1:
        mc "What if I told you I have some decent food that doesn't involve camel meat?"
        we "Like what?"
        mc "First, what do I get in return for my most excellent NASA food? It actually says \"Omelette du fromage\" on the packaging..."
        show microntalk with fastdissolve
        cm "(in French) Omelette du fromage? Did I hear that right? Mon Dieu! I LOVE omelettes du fromage!"
        hide french06
        show french05
        with fastdissolve
        we "(in French) Yes, Capitaine Micron! He says he has some. But he wants something in return. What should I do?"
        cm "(in French) Offer him our \"laisser-passer\" for Trumpf City, we... ouch!... don't need it anymore."
        hide microntalk with fastdissolve
        hide french05
        show french02
        with fastdissolve
        we "(in English). Ok, here's the deal. Your NASA food ration for a diplomatic pass to enter Trumpf City via the main West entrance. Interested?"
        mc "Alright! Diplomatic immunity, here I come!"
        $ nasafood -= 1
        window hide
        show diplomatic at posmission
        $ renpy.pause(0.5, hard=True)
        $ diplomaticpass = True
        hide french02
        show french01
        with fastdissolve        
        we "Dope! Good luck finding Trumpf City, boy! I must warn you that the pass has an expiry date by the way. But I don't know what it is since the dev hasn't determined it yet."
        hide diplomatic
        mc "Ah right, so I guess the clock is now ticking for me to find Trumpf City and use this thing. I feel like I've been conned."
        hide french01
        show french03
        with fastdissolve
        we "We felt the same way too when Trumpf sold us Louisiana for that much money... Now go, before Capitaine Micron changes his mind!"
        jump BackHex33        
    if nasafood == 0:
        $ lostmap = True
        if withbe:
            be "Let's not argue with her. That map was useless to us anyway, since there are no roads left... Let's go."
            mc "I just hate it when I have an item and then I lose it and then I don't get another better item to replace it!"
            jump BackHex33
        if withpe:
            pe "Let's not argue with her. That map was useless to us anyway, since there are no roads left... Let's go."
            mc "I just hate it when I have an item and then I lose it and then I don't get another better item to replace it!"
            jump BackHex33
if map == False:
    mc "Sorry, can't help you more there."
    show microntalk with fastdissolve
    if alone and withnone:
        cm "(in French) We're wasting our time with this boy. Tell him to go away, sergeant! Ouch, my stomach..."
    if alone == False or withnone == False:
        cm "(in French) We're wasting our time with these people. Tell them to go away, sergeant! Ouch, my stomach..."
    hide french01
    show french06
    with fastdissolve
    we "Sorry, but orders are orders. Leave NOW or I'll have no other option but to shoot you!"
    mc "Alright, alright, gee, foreigners invade our land and then they kick us out. That never happened before in North America, it's simply unheard of!"
    if persistent.tipson:
        show hex33btip at tips with dissolve
        pause
        hide hex33btip

label BackHex33:
$ period += 1
scene command01
show lena01
with fade
le "So, what do you have to report about area D3?"
if lostmap:
    if alone and withnone:
        mc "I met some froggy foreigners with tanks. I think we're being invaded."
    if alone == False or withnone == False:
        mc "We met some froggy foreigners with tanks. I think we're being invaded."
    hide lena01
    show lena03
    with fastdissolve
    le "What? That is ludicrous!"
    mc "It's true, I swear! And they stole my US road map too, said they were going down to Louisiana."
    mc "I'm guessing that's why they smelt of garlic so much, to repel the mosquitoes down there."
    hide lena03
    show lena05
    with fastdissolve
    le "*sigh* So you've wasted a scouting mission AND you lost an item from your inventory?"
    mc "That is correct. But the area is now cleared, Chief Lena!"
    hide lena05
    show lenapensive
    with fastdissolve
    le "I wonder what COULD have happened had you NOT lost that map in exchange of NOTHING..."
    mc "I guess we'll never know until I read that pdf hints guide that is conveniently attached to the main game folder...(except on Android)"
    hide lenapensive 
    show lena10
    with dissolve
    le "You are dismissed!"
    hide lena10 with dissolve
    jump LeaveCommand
if diplomaticpass:
    mc "I obtained a diplomatic pass to enter Trumpf City, Chief Lena!"
    hide lena01
    show lena07
    with fastdissolve
    le "What? I'm really impressed. And where is Trumpf City?"
    mc "Err... Somewhere East?"
    hide lena07
    show lena05
    with fastdissolve
    le "*sigh* We already knew that [name]... You'll have to do better than that next time, we NEED to find out where it is! Scout Dismissed!"
    hide lena05 with dissolve
    jump LeaveCommand
if clearedhex33 == False:
    if alone and withnone:
        mc "I met some foreigners with tanks. I think we're being invaded. And they smelt heavy of garlic, so maybe they think we turned into vampires or something."
    if alone == False or withnone == False:
        mc "We met some foreigners with tanks. I think we're being invaded. And they smelt heavy of garlic, so maybe they think we turned into vampires or something."
    hide lena01
    show lena03
    with fastdissolve
    le "What? That is ludicrous!"
    mc "It's true, I swear! And they spoke funny too."
    hide lena03
    show lena05
    with fastdissolve
    le "*sigh* Well, go back there and find out what they REALLY want."
    hide lena05
    show lenapensive
    with fastdissolve
    le "I'm not fighting a war against President Trumpf only to realize there are even bigger threats at our doorstep. Scouts dismissed!"
    hide lena05 with dissolve
    jump LeaveCommand

label ExploreHex34:
$ exploredhex34 = True
scene native01 with fade
if missionti == False:
    mc "It looks like some sort of campsite..."
if missionti:
    mc "Ah, Titahontas is there again. Let's talk to her then."
    if withbe:
        mc "I think I'll need some time alone with her. She's going through a rough patch. She might freak out if she sees you."
        be "Right. While you inspire confidence?"
        mc "Yeah, of course, I'm the HERO here, remember?"
        be "Just hurry up, I don't like this place. I cannot feel the presence of the Phallus Lord here."
        jump Titahontas02
    if withpe:
        mc "I think I'll need some time alone with her. She's going through a rough patch. She might freak out if she sees a Road Warrior like you."
        pe "Right. While you inspire confidence?"
        mc "Yeah, of course, I'm the HERO here, remember?"
        pe "Just hurry up, I don't like this place. I feel the presence of marauders."
        mc "Then keep them at bay while I do my business."
        jump Titahontas02        
    call AloneStance
    jump Titahontas02
label Native01:
call screen natives
screen natives:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/exitidle.png"
        hover "Icons/exithover.png"
        action Jump ("LeaveNatives")
    imagebutton:
        focus_mask True
        idle "Explore02/teepeeidle.png"
        hover "Explore02/teepeehover.png"
        action Jump ("NativeTent")
    imagebutton:
        focus_mask True
        idle "Explore02/titahontasidle.png"
        hover "Explore02/titahontashover.png"
        action Jump ("Titahontas")
        
label NativeTent:
"A large teepee with smoke coming out the top. Which looks remarkably like a bunghole."
jump Native01

label Titahontas:
if missionti == False:
    jump Titahontas01
if missionti and missionticompleted == False:
    jump Titahontas02

label Titahontas01:
scene native02
show titahontas01
with dissolve
ti "Ugh, whiteskin. I am Titahontas of the Cheyoquois tribe. Are you the witch doctor that Chief \"Little Red Mushroom Dick\" sent for?"
mc "Err...Not that I know. I'm the hero, but not a witch doctor. Why do you ask?"
hide titahontas01
show titahontas02
with fastdissolve
ti "Then all is lost... My poor daughter will never recover. *sob* After my husband died of the White Man's Curse, I have nothing to live for anymore!"
mc "Hang on, I'm good at quests and missions, I've done tons of them already. What do you need for your daughter?"
hide titahontas02
show titahontas05
with fastdissolve
ti "She has a terrible fever and I am afraid she is dying. Our Chief sent for a witch doctor who had a reserve of cactus milk, but he should have arrived by now..."
hide titahontas05
show titahontas03
with fastdissolve
ti "I fear the White Man's Curse that turned Chief \"Big Red Mushroom Dick\" into Chief \"Little Red Mushroom Dick\" has struck him too and he will never come..."
mc "Cactus milk you say? Well, there's plenty of cactuses around, I've seen them where camels spawn eternally."
hide titahontas03
show titahontas02
with fastdissolve
ti "These are not the right cactuses. The camels brought over here at the end of the White Man's Curse eat them too quickly, and they never grow large enough to give milk."
mc "Ah, well if that can console you, I've shot quite a few of those damn camels."
hide titahontas02
show titahontas03
with fastdissolve
ti "Please find some cactus milk and return here to save my daughter, young white hero! Kokopenis, the God of Fertility, and myself, will be forever grateful if you do!"
"Developer's note: The fertility deity of the Native Americans is actually called Kokopelli. Notice the subtle play on words there..."
window hide
show cactus at posmission
$ renpy.pause(1.0, hard=True)
$ missionti = True
mc "Fear not, Titahontas! I, \"Humongous White Cock\", of the...err... Western Capitalist tribe, will find cactus milk for your daughter. Ugh!"
hide cactus
hide titahontas03
show titahontas04
with fastdissolve
ti "Oh, I pray Kokopenis that you will succeed, err... \"Humongous White Cock\". Ugh!"
if persistent.tipson:
    show hex34tip at tips with dissolve
    pause
    hide hex34tip
jump BackHex34
    
label Titahontas02:
scene native02
show titahontas01
with dissolve
ti "Ugh...\"Humongous White Cock\". Did you manage to find some cactus milk for my daughter?"
if cactusmilk:
    mc "Yep. I told you I was good at quests and shit. Here it is. And I didn't even wrap it in a typhoid-ladden blanket. That's how NICE I am."
    hide titahontas01
    show titahontas04
    with fastdissolve
    ti "Oh thank you so much young white hero! My daughter will be saved and I have found a renewed will to live in the White Man's Curse World."
    window hide
    call PlusSierra
    mc "It's not that bad. If you like camel burgers."
    hide titahontas04
    show titahontas07
    with fastdissolve
    ti "Let me give this concoction to my daughter straight away. She is inside the teepee. Please wait here young hero!"
    hide titahontas07
    with dissolve
    mc "Sure, I ain't leaving until I get my reward anyway."
    jump TitahontasSex
if cactusmilk == False:
    mc "Err. No actually."
    hide titahontas01
    show titahontas02
    with fastdissolve
    ti "Then why did you come? To torment me? And watch me cry and kill myself?"
    mc "Come on, it's just an honest mistake, what with all those hexes, I sometimes get confused. Cactus milk it was, right?"
    hide titahontas02
    show titahontas03
    with fastdissolve
    ti "Yes, and hurry up please! My daughter is DYING!"
    mc "Alright, alright. I'll be right on it, don't worry. And I'll come back with the right stuff next time."
    jump BackHex34

label TitahontasSex:
scene native02
show titahontas06
with fade
ti "I have given her the concoction. She already seems to be getting better and is now soundly asleep. Now it is my turn to return the favor..."
show cactussuccess at posmission
window hide
$ renpy.pause(2.0, hard=True)
pause
hide cactussuccess
hide titahontas06
show titahontas08 with dissolve
ti "I want to know why you are called \"Humongous White Cock\"... Come back with me behind the teepee."
mc "Alright, now we're talking! I'll show you my HUMONGOUS WHITE COCK and what I can do with it, Titahontas!"
ti "That's what I expect from you! Hurry up, my daughter is sleeping right now."
scene titahontasprefuck01 with fade
ti "Now I see why you are called \"Humongous White Cock\", whiteskin! Let me ride that tremendous pole and show you the pleasure of native pussy!"
play sound "Sounds/lick.mp3"
mc "Oh yeah, never tasted such lovely nipples before too!"
stop sound
scene titahontasprefuck02 with dissolve
ti "You like it when I grind my pussy against your groin?"
mc "Yeah, but I'll LOVE it even more when my dong gets inside it!"
ti "Then let me ride you like a wild mustang!"
play music "Sounds/fucksound.mp3"
label TitahontasSlow:
hide titahontasfast
hide titahontasfastb
hide titahontasslowb
show titahontasslow
call screen titahontasslow01
screen titahontasslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TitahontasEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TitahontasFast") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("TitahontasPOVSlow") 

label TitahontasPOVSlow:
hide titahontasfast
hide titahontasfastb
hide titahontasslow
show titahontasslowb   
call screen titahontasslow01b
screen titahontasslow01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TitahontasEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TitahontasPOVFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("TitahontasSlow") 

label TitahontasFast:
mc "Yeah, twerk that tight Indian pussy on my cock, Titahontas!"
ti "I can sense you like that, don't you whiteskin?"
hide titahontasslow
hide titahontasfastb
hide titahontasslowb
show titahontasfast
call screen titahontasfast01
screen titahontasfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TitahontasEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("TitahontasSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("TitahontasPOVFast") 

label TitahontasPOVFast:
hide titahontasfast
hide titahontasslowb
hide titahontasslow
show titahontasfastb 
call screen titahontasfast01b
screen titahontasfast01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TitahontasEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("TitahontasPOVSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("TitahontasFast") 

label TitahontasEnd:
mc "Oh Fuck, you're gonna make me EXPLODE!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
scene titahontasbouncecum01 with dissolve
ti "Yes, fill me up with your whiteskin sperm!"
scene titahontasbouncecum02 with dissolve
ti "Oh, this is so good, you're cumming inside me so MUCH! You are such a HUMONGOUS WHITE STUD!"
scene titahontasbouncecum03 with dissolve
mc "Phew... That was something else. Nothing like some primeval wild native pussy I must say."
play sound "Sounds/moaning.mp3"
ti "This was sssoo good.... My pussy is pounding to the heartbeat of the wild buffalo. I cannot take anymore of that humongous cock of yours there..."
scene titapreanal01 with dissolve
mc "Well, I'm not done with you, Titahontas! I'm gonna pound that tight ass of yours into submission! Turn round and prepare for my deep anal penetration!"
ti "Where have I heard that before... Fine, do your worse, \"Humongous White Cock\"!"
hide titapreanal01
play channel1 "Sounds/womansex01.mp3"
play channel2 "Sounds/wank.mp3"
label TitaAnalSlow:
hide titaanalfast
show titaanalslow
call screen rockslow01
screen rockslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TitaAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TitaAnalFast") 

label TitaAnalFast:
ti "Your cock is... just too HUMONGOUS!"
mc "Then I'll go faster so it will be over FASTER!"
hide titaanalslow
show titaanalfast
call screen rockfast01
screen rockfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TitaAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("TitaAnalSlow") 

label TitaAnalEnd:
mc "That's it, I'm on the verge of WHITEWASHING your ass with my spunk!"
stop channel1
stop channel2
play music "Sounds/splooge02.mp3"
scene titaanalcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
ti "Oh my God, I can HEAR it spurt inside my ass!"
scene titaanalcum02 with dissolve
stop music
stop sound
play sound "Sounds/splooge01.mp3"
ti "I'm releasing the overflow! I'M POURING CUM OUT OF MY BACKSIDE!"
stop sound
scene titaanalcum03 with dissolve
mc "Yeah, I did come a lot actually. My balls are drained... Time for me to leave you and your daughter, Titahontas..."
ti "Really? So soon... But you're right, I should go and check on Lolihontas anyway... Let's get dressed."
scene native02
show titahontas06
with fade
ti "Before you go. I have a gift for you. A talisman that will provide you with the protection of the spirits of the desert."
window hide
show talisman at posmission
pause
hide talisman
$ talisman = True
mc "Thanks, Titahontas! That should be very helpful, since most of this forsaken place is in fact... desert."
hide titahontas06
show titahontas04 with fastdissolve
ti "Farewell, young white hero!"
$ missionticompleted = True
$ clearedhex34 = True
jump BackHex34

label BackHex34:
$ period += 1
scene command01
show lena01
with fade
if alone:
    le "So, what do you have to report about area D4, [name]?"
if alone == False :
    le "So, what do you have to report about area D4, scouts?"
if missionti and missionticompleted == False:
    mc "I met a Native American tribeswoman. Ugh."
    hide lena01
    show lena03
    with fastdissolve
    le "And? Did she help you in any way? Did she have information that is of any value to me?"
    mc "Not yet. But I have a new quest now. Once I complete it, I'll get a reward for sure, which may or may not include information that is valuable to you, Chief Lena!"
    hide lena03
    show lena05
    with fastdissolve
    le "*sigh* Right. So I just have to hope and pray that you're not wasting MY time again."
    mc "I thought you weren't the religious type Chief?"
    hide lena05
    show lena10
    with fastdissolve
    le "You are dismissed!"    
    hide lena10 with fastdissolve
    jump LeaveCommand
if missionti and missionticompleted:
    mc "I met that Native American tribeswoman again and completed yet another quest!"
    hide lena01
    show lena06
    with fastdissolve
    le "Good. So, what valuable information are you bringing back to me then?"
    mc "Err... Sorry, it was one of those quests with a personal reward, nothing for you. My bad."
    hide lena06
    show lena05
    with fastdissolve
    le "*sigh* I KNEW you were wasting my time with that area. Scouts dismissed!"
    hide lena05 with fastdissolve
    jump LeaveCommand    

label ExploreHex35:
play music "Sounds/desertwind01.mp3"
scene junktownfar with fade
if tomarried:
    mc "Time for my conjugal visit..."
    jump Junktown01
if exploredhex35 == False:
    mc "There's seems to be something over there, in the middle of nowhere..."    
    if withbe and metci == False:
        be "Well, as much as it pains me to meet yet again potentially-dangerous total strangers, we should investigate..."
        mc "We'll see, they could be hot-to-trot strangers with a bit of luck."
    if withpe and metci == False:
        pe "Well, as much as it pains me to meet yet again potentially-dangerous total strangers, we should investigate..."
        mc "We'll see, they could be hot-to-trot strangers with a bit of luck."
    if alone:
        call AloneStance
    jump Junktown01
mc "We're back at Cindy's gun store, which is exactly where I wanted to be. Good thing they don't move around that hex the size of Texas too much."
if withbe and metci:
    be "Why are we here? Do you need more firepower?"
    mc "Err, yeah, that's what I need. You can stay back while I barter with these rednecks."
    be "I see... Don't take too long, this place is very exposed. I'll guard my rig and be on the lookout."
if withpe and metci:
    pe "Why are we here? Do you need more firepower?"
    mc "Err, yeah, that's what I need. You can stay back while I barter with these rednecks."
    pe "I see... Don't take too long, this place is very exposed. I'll guard my rig and be on the lookout."
if alone:
    call AloneStance

label Junktown01:
$ exploredhex35 = True
stop music
if pregto:
    if pregtostart <= 2:
        scene junktown01
        show cindy01 at right
        with dissolve
        ci "Welcome back boy!"
        window hide
        show taylorpregnant01b at left with moveinleft
        to "Oh hi hubby! I'm as happy as a puppy with two peckers to see you again!"
        hide cindy01
        show cindy02 at right
        with dissolve
        ci "As it turns out, you DID knock her up real good. Mah daughter is pregnant."
        to "Isn't that darn tootin', hubby? Come and see for yahself!"
        hide cindy02
        show cindy08 at right
        hide taylorpregnant01b
        show taylorpregnant02b at left
        with dissolve
        mc "That's amazing, even your tits seem to grow bigger..."
        to "I can still get fucked by your great big whopper, I'm not pregnant enough yet!"
        ci "Yep, I reckon you should do your marital duty and fuck mah daughter again..."
        mc "Of course... Cos, why not?"
        ci "I'll go varmint huntin' while you do your deed..."
        jump TaylorFuckAgain

    if pregtostart <= 4:
        scene junktown01
        show cindy01 at right
        show taylorpregnant03b at left with moveinleft
        with dissolve
        ci "Welcome back boy!"
        to "Oh hi hubby! My belly is starting to ache. The baby is growing sssso fast! Come and comfort me, please..."
        hide cindy01
        hide taylorpregnant03b
        show cindy08 at right
        show taylorpregnant04b at left
        with dissolve
        mc "There, there, everything will be fine, I'm here for you..."
        ci "Well, will you look at these two lovebirds? But enough fondling mah daughter's tits, young man, are you here to buy something from mah gun store?"
        mc "Ah, yes, I'll have a look at what you have..."
        to "Bye, darling hubby, I feel better now!"
        hide taylorpregnant04b with dissolve
        hide cindy08 
        show cindy02 at right
        with fastdissolve
        ci "Let's do some business."
        $ cindyinventory01 = True
        jump CindyInventory
        label CindyInventoryReturn01:
        hide inventoryinterface
        $ cindyinventory01 = False
        if alone:
            ci "In case you're wondering, I ain't cleaning your bike alone without mah daughter... But you can fuck me on it if you want..."
            menu:
                "Hell, why not.":
                    jump CindyQuickFuck
                "Na, gotta go.":
                    hide cindy02
                    show cindy01 at right
                    with fastdissolve
                    ci "I'm almost offended. Like your prefer your wife's pussy to mah experienced MILF one..."
                    jump BackHex35
        ci "Well, since you don't have your bike with ya, I'll let you go back to your city life."
        jump BackHex35
                    
    if pregtostart <= 6:
        scene junktown01
        show cindy01 at right
        show taylorpregnant05b at left with moveinleft
        with dissolve
        ci "Welcome back boy!"
        to "Hubby! It hurts so much! The baby is getting GIGANTIC! Your sperm is just sssooo virile!"
        hide cindy01
        hide taylorpregnant05b
        show cindy08 at right
        show taylorpregnant06b at left
        with dissolve
        mc "I see what you mean... It must a boy then. We'll get through this together, don't worry."
        ci "By that you mean she'sll get through this while you're living your city life far away from 'ere, dontcha?"
        mc "Err.. Yeah, something like that."
        to "Well, I feel better now anyhoo! I'll go and rest a bit, bye darling hubby!"
        hide taylorpregnant06b with dissolve
        hide cindy08 
        show cindy02 at right
        with fastdissolve
        ci "So, you want to see what I got in mah store I reckon? Let's do some business then."
        $ cindyinventory01 = True
        jump CindyInventory

    if pregtostart == 7:
        to "Oh, Ma, I think it's happening... I'm gonna pop a fetus!"
        ci "And it will become a baby with no more Texas-approved legal protection once it's born."
        mc "Quick, let's do something about it! Where's the nearest medbay?"
        hide cindy01
        show cindy02 
        with fastdissolve
        ci "You don't make no sense, boy! There ain't no medbay round these parts. We give birth the good ole' fashioned way down 'ere in Texas."
        mc "Meaning?"
        hide cindy02
        show cindy03 
        with fastdissolve
        ci "In the back of the truck, of course."
        scene taylorbirth01 with dissolve
        ci "Now go on Taylor, push for your Ma and you'll become one too."
        play sound "Sounds/womanscream.ogg"
        scene taylorbirth02 with dissolve
        ci "Keep pushing, girl, I can darn see its head!"
        play sound "Sounds/Plop.mp3"
        ci "There you go, one new Texan baby."
        mc "Is it a boy or a girl?"
        stop music
        scene taylorbirthbackground
        show cindybaby
        with dissolve
        play sound "v06/babycrying.mp3"
        ci "It's a boy! And a mighty BIG boy might I add."
        call MCbabies
        to "Does it have a great big whopper like his daddy?"
        if babytaylorcount == 1:
            ci "He sure does Taylor, as big as an Alabama anaconda. Just like his brother."
            to "I'll call that one Jax. Its sounds nicely white-trashy, just like his brother Randy."
            jump TaylorBirthAgain
        if babytaylorcount >= 2:
            ci "He sure does Taylor, as big as an Alabama anaconda. Just like his brothers."
            to "I'll call that one Joey. Its sounds nicely white-trashy, just like his brother Randy."
            jump TaylorBirthAgain
        ci "He sure does Taylor, as big as an Alabama anaconda."
        to "I'll call him Randy."
        mc "And I bet he'll be a randy little bugger when he grows up."
        label TaylorBirthAgain:
        ci "I think you should let your wife rest now. You can come back next week to breed her again. And re-populate Texas with horse-hung boys like this one."
        $ babytaylor = True
        $ babytaylorcount += 1
        $ pregto = False
        $ pregtostart = 0
        mc "That birth was indeed exhausting... And took a full period. I should go back to the compound now."
        jump BackHex35

if babytaylor:
        scene junktown01
        show cindy01 at right
        with dissolve
        ci "Welcome back boy!"
        window hide
        show taylorbaby01 at left with moveinleft
        to "Oh, look who's here Randy! It's daddy!"
        mc "Hello there, little fella. Or should I say \"big\" fella, nod, nod, wink, wink, say no more, say no more."
        hide taylorbaby01
        show taylorbaby02 at left 
        with fastdissolve
        to "What are you yapping about?"
        mc "Err... Nothing."
        hide taylorbaby02
        show taylorbaby01 at left 
        with fastdissolve
        play sound "v06/babycrying.mp3"
        to "Well, I'd better be off, He wants to be fed. Lots of breast milk cos he darn likes it so much. And measure his cock to see if he's grown some more."
        mc "Ha, I KNEW it!"
        to "Say bye to daddy!"
        hide taylorbaby01 with moveoutleft
        ci "So, are you here to breed mah daughter again or to see what I have in mah store?"
        menu:
            "To breed her again.":
                hide cindy01
                show cindy02 at right
                with fastdissolve
                ci "Well, that's darn tootin of you, young man. I'll let her know you're ready to fill her up again and I'll leave you two to it then."
                jump TaylorFuckAgain
            "To look at your store":
                $ cindyinventory02 = True
                jump CindyInventory
                label CindyInventoryReturn02:
                $ cindyinventory02 = False
                hide cindy02
                show cindy04 at right
                with dissolve
                ci "It's getting late and I need to go vermint hunting to feed the family. Including YOUR son."
                mc "Alright, I'll get going then."
                jump BackHex35
 
scene junktown01
show cindy01
with dissolve        
if persistent.tipson:
    show cindytip at tips with dissolve
    pause
    hide cindytip
if metci == False:
    ci "Howdy boy! Welcome to mah gun shop, \"Cindy's Top Guns\". We got the meanest, baddest NRANRA-certified guns'n ammos down 'ere."
if metci:
    ci "Welcome back young'un! I'm as happy as a puppy with two peckers to see ya again."
    if nranramember and cindyknownranra:
        hide cindy01
        show cindy02
        with fastdissolve
        jump CindyBuy
    if nranramember and cindyknownranra == False:
        mc "And now I'm a member of the NRANRA so I can buy some guns from you!"
        hide cindy01
        show cindy02
        with fastdissolve
        ci "Well that's just great!"
        $ cindyknownranra = True
        jump CindyBuy
    if nranramember == False:
        ci "Have you gotten yourself an NRANRA card yet?"
        mc "Err. No."
        hide cindy01
        show cindy03
        with fastdissolve
        ci "That ain't no good. You ain’t got the sense God gave an ant. Come back 'ere when you've checked yourself with the big boys."
        jump BackHex35
label FirstMeet:
$ metci = True
hide cindy01
show cindy02
with fastdissolve
ci "Now of course, I only sell to background-checked NRANRA members but I'm sure a fine young man like you won't have no problem with that."
if nranramember:
    mc "You're darn right missus! I'm a full-blown proud-paying member of the NRANRA."
    ci "Well that just dills my pickles!"
    $ cindyknownranra = True
if nranramember == False:
    mc "The NR what?"
    hide cindy02
    show cindy03
    with fastdissolve
    ci "Well, I'll be a monkey's uncle! This city boy ain't go no right to even own an Arkansas toothpick! Sorry, but I can't do no business with you, sir."
    mc "What? What did I do?"
    hide cindy03
    show cindy01
    with fastdissolve
    jump Junktown02

label CindyBuy:
window hide
show cindy02 at right with move
ci "So ya wanna see what I got in mah store? Here's the list of what I've got selling."
hide cindy01
show cindy02 at right
with fastdissolve
$ cindyinventory03 = True
jump CindyInventory
label CindyInventoryReturn03:
$ cindyinventory03 = False

label Junktown02:
hide inventoryinterface
if metto:
    ci "I reckon ya'all wanna see mah daughter again?"
    menu:
        "Not really, I don't have time for that. I'll be on my way.":
            hide cindy02
            show cindy03 at right
            with fastdissolve
            ci "Well look who's getting all uppity down 'ere."
            jump BackHex35
        "Sure, I was wondering where she was actually." if seenbikewash02 == False:
            hide cindy02
            show cindy01 at right
            with fastdissolve
            ci "She was pro'bly hitting the bushes, but she's back now."
            show taylor02b at left with moveinleft
            to "Hi there [name]!"
            ci "Look at her, pretty as a peach. She could make a hound dog smile."
            mc "Sure. And do some other tricks too."
            hide taylor02b
            show taylor01b at left
            with fastdissolve
            to "Oh yah? Like what? I sure have a hankerin' for a puppy to do all sorts of tricks for me right now!"
            hide cindy01
            show cindy02 at right
            with fastdissolve
            ci "Now don't you get no funny ideas girl. What you need is a husband who ain't no yaller dog like your father was, not some silly puppy. We shoot those down' ere."
            mc "Well, I should leave you fine people to your... err... puppy-shooting, it's getting late."
            hide taylor01b
            show taylor03b at left
            with fastdissolve
            to "Bye [name]! Come back and see us again soon!"                                                                                                
            jump BackHex35
        "Sure, I was wondering where she was actually. And I have my own bike now." if seenbikewash == False and alone:
            hide cindy02
            show cindy01 at right
            with fastdissolve
            ci "She was pro'bly hitting the bushes, but she's back now."
            show taylor02b at left with moveinleft
            to "Hi there [name]!"
            ci "Look at her, pretty as a peach. She could make a hound dog smile."
            mc "Sure. And do some other tricks too."
            hide taylor02b
            show taylor01b at left
            with fastdissolve
            to "Speaking of tricks, mahbe we can wash your motorbike for you this time. I see you came with it..."
            hide cindy01
            show cindy02 at right
            with fastdissolve
            ci "Now that's a fine idea. Whaddya reckon, boy?"
            menu:
                "I reckon, darn yeah! (-5$)" if money >= 5:
                    hide cindy02
                    show cindy01 at right
                    with fastdissolve        
                    ci "I'll get me fixing mah bikini and I'll be back lickety-split. Dontcha go nowhere."
                    hide cindy01 with moveoutright
                    mc "What foreign country is your mother from Taylor?"
                    hide taylor01b
                    show taylor02b at left
                    with fastdissolve
                    to "What? She ain't from no foreign country silly! We're from good 'ole Texas! Pure local corn-bred!"
                    jump Bikewash    
                "I reckon I should leave you fine people, it's getting late.":
                    hide cindy02
                    show cindy03 at right
                    with fastdissolve
                    ci "Well look who's getting all uppity down 'ere."
                    jump BackHex35
        "And I want to see you girls wash my motorbike again! (-$5)" if alone and seenbikewash and seenbikewash02 == False and money >= 5:
            hide cindy02
            show cindy01 at right
            with fastdissolve
            ci "We're up for it. The sun is blazing and I don't mind some fresh water on mah skin."
            show taylor02b at left with moveinleft
            to "Hi there [name]!"
            ci "Look at her, pretty as a peach as always. She could make a hound dog smile."
            to "Are we gonna wash his motorbike in our bikinis again Ma?"
            ci "That's right, I'll get mah bikini and you get the bucket and soap."
            $ money -= 5
            jump BikeWashRepeat
        "And I want to see you girls wash my motorbike again! (-$5)" if alone and seenbikewash02:
            hide cindy02
            show cindy03 at right
            with fastdissolve
            ci "Well, first, I'm still waiting for you to do something you should 'ave done a long time ago, boy!"
            mc "What's that?"
            $ cindyproposed = True
            jump TaylorWedding01
        "And I'm ready to propose to her!" if seenbikewash02 and cindyproposed:
            hide cindy01
            show cindy02 at right
            with fastdissolve
            ci "Well, that's just darn sweet of you! Taylor, come 'ere, this boy is gonna be your breeder!"
            jump TaylorWedding02
            

ci "Now before you leave to go back to your city life, I'd like to introduce you to mah daughter. Taylor, come and give this city boy some sugar."
window hide
$ metto = True
show taylor01b at left with moveinleft
to "Hi there mister!"
hide cindy02
show cindy01 at right
with fastdissolve
ci "Don't she look prettier than a glob of butter melting on a stack of wheat cakes?"
mc "Err... Yes, sure, she's lovely."
hide cindy01
show cindy02 at right
with fastdissolve
if alone:
    ci "You're darn tootin' she is. Now we could both wash your motorbike for an extra five bucks in only our bikinis, whaddya say?"
    menu:
        "I don't have that kind of money to throw out of the window.":
            hide cindy02
            hide taylor01b
            show taylor04b at left
            show cindy03 at right
            with fastdissolve
            ci "Well, would you listen to that Taylor? The boy couldn’t jump over a nickel to save a dime. Bless his heart."
            mc "I didn't catch a word of that but I think I'd better get going."
            hide taylor04b
            show taylor03b at left
            with fastdissolve
            to "See ya mister!"
            jump BackHex35
        "I' gladly pay to see THAT (-$5)." if money >= 5:
            $ money -= 5
            hide cindy02
            show cindy01 at right
            with fastdissolve        
            ci "I'll get me fixing mah bikini and I'll be back lickety-split. Dontcha go nowhere."
            hide cindy01 with moveoutright
            mc "What foreign country is your mother from Taylor?"
            hide taylor01b
            show taylor02b at left
            with fastdissolve
            to "What? She ain't from no foreign country silly! We're from good 'ole Texas! Pure local corn-bred!"
            jump Bikewash    
if alone == False:
    ci "You're darn tootin' she is."
    hide taylor01b
    show taylor03b at left
    with fastdissolve
    to "How did you get here mister? I don't see no bikes or cars?"
    mc "My scouting partner is over that hill guarding her rig."
    hide cindy02
    show cindy01 at right
    with fastdissolve
    ci "Oh? So you don't have yar own rig?"
    if mcbike == False:
        mc "Not yet."
        hide taylor03b
        show taylor04b at left
        hide cindy01
        show cindy03 at right
        with fastdissolve
        ci "That ain't good. You can't go nowhere you want with no motorbike round these parts."
        mc "Yeah, it's a bummer, I'm saving money in the hope of buying my own one day."
        hide taylor04b
        show taylor02b at left
        with fastdissolve
        to "I sure hope you do mister! Hope to see you back 'ere with your OWN rig!"
        hide cindy03
        show cindy02 at right
        with fastdissolve
        mc "Sure, I WILL come back when I get one. Now I should go, it's getting late."
        hide taylor02b
        show taylor03b at left
        with fastdissolve
        to "Bye mister!"
        jump BackHex25
    if mcbike:
        mc "I do but it's back at the workshop for maintenance."
        hide cindy03
        show cindy01 at right
        with fastdissolve
        ci "Well if you come back n' visit us again, we could both wash your motorbike for an extra five bucks in only our bikinis, whaddya say?"
        mc "Alright! I'll definitely come back alone to see that then."
        hide taylor03b
        show taylor04b at left
        with fastdissolve
        to "Hope to see you again soon mister! Bye!"
        jump BackHex35

label Bikewash:
$ seenbikewash = True
scene junktown02
show cindybikini02 at right with moveinright
ci "Get the bucket and the soap Taylor, we're ready to show this city boy how we's wash things proper down 'ere."
window hide
show taylorwet01 with moveinleft
to "Heehee..."
play sound "Sounds/waterspray.mp3"
scene junktown02
show junktownwet01 
with dissolve
ci "What are you doing TAYLOR? You're nuttier than a squirrel's turd, you're getting your mamma all wet!"
hide junktownwet01
show taylorbikini01 at left
show cindybikini03 at right
with dissolve
ci "Now look at the mess you've made Taylor! I'm all wet and mah bikini is almost see-thru now."
scene junktown02 blurred
show cindybikini04
with fastdissolve
ci "Well, it’s hotter than blue blazes out here, so I might as well take it off..."
hide cindybikini04
show cindybikini05
with fastdissolve
to "Oh Ma, you're showing your big jugs to this city boy, that's real sugar of you! Mahbe I should do the same then..."
scene junktown02
show cindybikini06 at right
show taylortopless01 at left
with dissolve
ci "Oh look at mah daughter sweet-talking to ya'all. Now let's wash his motorbike like we said we'd do. Go and get the soap and bucket this time Taylor."
hide taylortopless01 with moveoutleft
ci "What's your name boy?"
mc "[name]. The HERO."
show bikewash01 at left with moveinleft
with dissolve
to "Heehee, I've made a mess of the soap, it's all over mah tits now."
ci "TAYLOR! You're a naughty girl, and now I'm gonna have to look just like you so no one's jealous."
scene junktown02 blurred
show bikewash02
with dissolve
ci "Come over and run that sponge over your Ma's skin. I'll use mah tits to wash [name]'s rig, they have more surface than that sponge."
scene junktown03
show bikewash03
with dissolve
ci "Your motorbike is so dirty it don't belong to a hero. We'll make it real clean in no time I reckon."
hide bikewash03
show bikewash04
with dissolve
to "Heehee, you're rubbing your big jugs all over that bike, you're gonna get'em all dirty Ma!"
ci "That way we do the job faster and we get our five bucks faster honey!"
hide bikewash04
show bikewash05
with dissolve
to "Ma, you're cleaning ME instead of the bike, silly!"
ci "I'm just getting the grit out of your skin so you look nice for that city boy. I think we're done 'ere."
mc "Time for me to inspect your handiwork ladies. In my jockstrap cos I like to ride my bike almost commando-style."
scene junktown04
show bikewash06 
with dissolve
play sound "Sounds/gasp.mp3"
to "*gasp* Look, Ma, he's packing more than an inbred country mule!"
call LustPlusTaylor
stop sound
ci "I sure wish your pa had been hung like that when he knocked me up in high school. And he was mah cousin." 
hide bikewash06
show bikewash07 
with dissolve
mc "Yeah, I like what you did ladies. It's squeaky clean and the brakes now work better than before!"
to "Well, I think we deserve a reward [name] for the work we done, dontcha think?"
scene junktown03
show bikewash08 
with dissolve
ci "He already paid us honey, what else you want from him?"
to "I want to see his great big pecker!"
ci "Well that ain't no manners Taylor! I home trained you better than to ask a city boy to show you his big old fat pud!"
ci "I reckon you should ask sweeter than that."
mc "It's alright, I don't mind one bit. Get on your knees then Taylor and behold..."
scene junktown04
show bikewash09 
with dissolve
mc "...my HERO cock!"
to "Oh, wow, it's even bigger than I hoped it would be! It's a whopper!"
mc "And why don't say hello to him with your mouth Taylor?"
ci "That would be the proper thing to do."
to "I don't know, it's sssoo big I don't think even an Alabama anaconda could swallow that monster!"
ci "Now, now, I brought you up better than to refuse a challenge Taylor. Let me demonstrate, like a good mother would."
scene junktown05
show bikewash10
with dissolve
to "How are you going to do it Ma, [name]'s pud is just so... GIGANTIC!"
ci "You just have to let your lips stretch real wide and it'll fit. Watch and learn Taylor."
scene junktown05 blurred
label BikeBlowSlow:
play music "Sounds/hardsucking.mp3"
hide bikeblowfast
show bikeblowslow
call screen bikeblowslow01
screen bikeblowslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BikeBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BikeBlowFast") 

label BikeBlowFast:
to "Oh wow, look at how your giant dong is stretching my Ma's lips... Try and gobble his pole faster Ma!"
hide bikeblowslow
show bikeblowfast
call screen bikeblowfast01
screen bikeblowfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BikeBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BikeBlowSlow") 

label BikeBlowEnd:
stop music
scene junktown05
show bikewash10
with dissolve
ci "Now it's your turn Taylor. You make me proud, girl, and you get [name] to spew his sauce right down your throat."
to "Oh, wow, Ma, thanks for letting me be the one to swallow his monstercock spunk, that's real sugar of you!"
ci "I'll suck on his juicenuts and make sure he delivers when we wants him to."
scene junktown05 blurred
label BikeBlowSlow02:
play music "Sounds/hardsucking.mp3"
hide bikeblowfast02
show bikeblowslow02
call screen bikeblowslow02
screen bikeblowslow02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BikeBlowEnd02")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BikeBlowFast02") 

label BikeBlowFast02:
ci "That's mah girl! Now get that log down your throat even faster honey!!"
hide bikeblowslow02
show bikeblowfast02
call screen bikeblowfast02
screen bikeblowfast02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BikeBlowEnd02")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BikeBlowSlow02") 

label BikeBlowEnd02:
ci "I think he's about to spew his Texas sauce! Open your throat real wide and swallow as much you can Taylor. You don't want to be making a mess of it now do ya?"
stop music
hide bikeblowfast02
hide bikeblowslow02
show taylorblow09
show taylorblowcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "FU-U-UCK!"
hide taylorblowcum01
hide taylorblow09
show taylorblow03
show taylorblowcum02
with fastdissolve
mc "Damn it! She's sucking my load right out of my cumslit! AAAH!"
ci "Now I don't know where you learnt that Taylor but you seem to be givin' that boy some real sugar there!"
hide taylorblowcum02
hide taylorblow03
show taylorblowcum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "I've got more Texas sauce for you ladies, RHAAA!"
ci "PLASTER us in it then [name], I want mah tits to be COVERED in red-hot spunk!"

hide taylorblowcum03
show bikeblowcum05
with dissolve
stop sound
play sound "Sounds/kiss.mp3"
ci "Mmmh, I LOVE slurping that city boy's splooge directly out of your mouth, Taylor!"
mc "Oh God, that is so filthy... You ladies have sucked the life out of me."
mc "It's getting late anyway, I thank you for your cleaning job and I shall bid you farewell."
to "Mmh, slurp... *kiss*"
play sound "Sounds/kiss.mp3"
mc "And apparently, they're not even listening to me..."
jump BackHex35

label BikeWashRepeat:
$ seenbikewash02 = True
scene junktown02
show cindybikini02 at right with moveinright
ci "And don't you splash water on me, you hear?"
window hide
show taylorwet01 with moveinleft
to "Heehee..."
play sound "Sounds/waterspray.mp3"
scene junktown02
show junktownwet01 
with dissolve
ci "You did it AGAIN, TAYLOR!!! You ain't got home trainin', girl!"
hide junktownwet01
show taylorbikini01 at left
show cindybikini03 at right
with dissolve
to "Sorry Ma, I couldn't help it, it's real fun seeing you all wet."
ci "And now mah bikini is almost see-thru. AGAIN."
scene junktown02 blurred
show cindybikini04
with fastdissolve
ci "Well, it’s hotter than blue blazes out here, so I might as well take it off... Again."
hide cindybikini04
show cindybikini05
with fastdissolve
to "Oh Ma, you're showing your big jugs to this city boy, that's real sugar of you! Mahbe I should do the same then... Again."
scene junktown02
show cindybikini06 at right
show taylortopless01 at left
with dissolve
ci "Oh look at mah daughter sweet-talking to ya'all. Now let's wash his motorbike like we said we'd do. Go and get the soap and bucket this time Taylor."
hide taylortopless01 with moveoutleft
ci "You must think we're all loonies down in Texas."
mc "Far be it from me to have such a thought. Ahem."
show bikewash01 at left with moveinleft
with dissolve
to "Heehee, I've made a mess of the soap, it's all over mah tits now."
ci "TAYLOR! You're being a naughty girl AGAIN, and now I'm gonna have to look just like you so no one's jealous."
scene junktown02 blurred
show bikewash02
with dissolve
ci "Come over and run that sponge over your Ma's skin. I'll use mah tits to wash [name]'s rig, they have more surface than that sponge."
scene junktown03
show bikewash03
with dissolve
ci "Your motorbike is so dirty it don't belong to a hero. We'll make it real clean in no time I reckon. Just like last time."
hide bikewash03
show bikewash04
with dissolve
to "Heehee, you're rubbing your big jugs all over that bike, you're gonna get'em all dirty Ma!"
ci "That way we do the job faster and we get our five bucks faster honey!"
hide bikewash04
show bikewash05
with dissolve
to "Ma, you're cleaning ME instead of the bike, silly! You did that last time too, you're nuttier than a squirrel's turd!"
ci "Hey, that's MY southern slang line, Taylor! I think we're done 'ere."
mc "Time for me to inspect your handiwork ladies. In my jockstrap like last time so the same sex scene can happen again at the end."
scene junktown04
show bikewash06 
with dissolve
to "Still as hung as an inbred country mule!"
ci "It almost looks like he's still growing. I could swear it's even fatter than last time. It's gonna be a real challenge sucking him off and getting him to spew his sauce." 
hide bikewash06
show bikewash07 
with dissolve
mc "Yeah, I like what you did ladies. It's squeaky clean and the brakes now work even better than they already worked better before!"
to "Well, I think we deserve a reward [name] for the work we done, dontcha think? Like, you show us your big whopper and we all suck it silly again."
mc "Yeah, I guess it simply has to come to that... Get on your knees then Taylor and behold..."
scene junktown04
show bikewash09 
with dissolve
mc "...my still-HERO cock!"
to "Oh, wow, it's a real whopper, biggest one I ever tasted!"
call LustPlusTaylor
mc "I think you should go first this time, you're a pro at it. And your stacked mother can gobble one of my nuts."
ci "That would be the proper thing to do."
scene junktown05
show bikewash11
with dissolve
to "Are you ready [name]? Cos my jaws are still aching from last time, but I think I can stretch 'em real wide for you this time!"
mc "Yeah, I'm ready, Taylor. You can get on with the blowjob..."
scene junktown05 blurred
label BikeBlowSlow02b:
play music "Sounds/hardsucking.mp3"
hide bikeblowfast02
show bikeblowslow02
call screen bikeblowslow02b
screen bikeblowslow02b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BikeBlowEnd02b")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BikeBlowFast02b") 

label BikeBlowFast02b:
ci "That's mah girl! You go and let him skull-fuck you even faster now, honey!"
hide bikeblowslow02
show bikeblowfast02
call screen bikeblowfast02b
screen bikeblowfast02b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BikeBlowEnd02b")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BikeBlowSlow02b") 

label BikeBlowEnd02b:
mc "Oh God, Taylor, you blow me so good!"
hide bikeblowslow02
hide bikeblowfast02
show bikewash10
with dissolve
stop music
ci "That's it Taylor, you got to stop or you'll make him spew too soon. Now it's mah turn on his great big pecker."
to "Alright Ma, he's all yours!"
hide bikewash10
label BikeBlowSlowRepeat:
play music "Sounds/hardsucking.mp3"
hide bikeblowfast
show bikeblowslow
call screen bikeblowslow01b
screen bikeblowslow01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BikeBlowEndRepeat")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BikeBlowFastRepeat") 

label BikeBlowFastRepeat:
to "Oh wow, look at how your giant dong is stretching my Ma's lips... Try and gobble his pole faster, Ma!"
hide bikeblowslow
show bikeblowfast
call screen bikeblowfast01b
screen bikeblowfast01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BikeBlowEndRepeat")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BikeBlowSlowRepeat") 

label BikeBlowEndRepeat:
mc "That's it, I'm gonna blow my nut!"
hide bikeblowfast
hide bikeblowslow
show cindyblowcum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
to "He's nutting right down your throat, Ma! I sure hope it tastes real good!"
hide cindyblowcum01
show bikeblow00
show cindyblowcum02
with dissolve
mc "Those sucking lips! That's too much! RHAAA!"
hide bikeblow00
hide cindyblowcum02
show bikeblowcum04
with dissolve
stop sound
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
to "Oh look Ma, he's still coming as strong as ever! It's POURING out of his monstercock!"
ci "Cover our tits and faces in your red-hot spunk [name]!"
hide bikeblowcum04
show bikeblowcum05
with dissolve
stop sound
play sound "Sounds/kiss.mp3"
to "Mmmh, I LOVE slurping that city boy's splooge directly out of your mouth, Ma!"
mc "FUCK! You country bumpkins really are filthy incels!"
scene junktown02
show cindybikini07
with dissolve
ci "What did you say??? Now that ain't no way to show respect to us ladies, young man!"
ci "You come right 'ere behind me and you fuck me real good to make things right, you hear me, city boy?"
mc "Err... Ok, missus."
to "Oh Ma, you're gonna let this boy fuck your old pussy with his monstercock, that's real sugar of you!"
                                                                                                        
scene junktown06
show cindyprefuck
with dissolve
ci "No need for any lubing, I'm already dripping with mah own slime, so just SHOVE IT IN!"
scene junktown04
label CindyFuckSlow:
play music "Sounds/fucksound.mp3"
hide cindyfuckfast
show cindyfuckslow
call screen cindyfuckslow01
screen cindyfuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("CindyFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("CindyFuckFast") 

label CindyFuckFast:
ci "That's it! Pound that fuckhole faster [name]!"
hide cindyfuckslow
show cindyfuckfast
call screen cindyfuckfast01
screen cindyfuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("CindyFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("CindyFuckSlow") 

label CindyFuckEnd:
ci "You'd better give me a nice fat creamy load to make up for yar rudeness, boy!"
scene junktown06 blurred
show cindyfuckcum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
to "Oh Ma, he's filling you up like a gas tank!"
ci "That's how you get babies, so watch and learn Taylor!"
mc "FU-UU-UCK! I'll pull out, I'm still cumming full-blast!"
scene junktown04
show cindyfuckcum02
with dissolve
ci "That's a good boy, I'm full anyway, pump that spunk outside of mah overfilled stretched-out pussy."
to "[name]! You're spewing over your own motorbike, silly! You're gonna make it all dirty again!"
scene junktown03c
show bikewash12
with dissolve
to "Now I'm gonna have to clean your mess with mah tongue! *slurp*"
play sound "Sounds/lick.mp3"
$ renpy.pause(2.0, hard=True)
scene junktown05 blurred
show bikewash13
with dissolve
ci "I'll join you Taylor, so we's do it faster and the boy can go with a clean motorbike."
to "That's the last of it... *slurp* All clean mister!"
play sound "Sounds/lick.mp3"
mc "Well, thank you very much ladies. Now I shall bid you farewell, it's getting late..."
jump BackHex35

label TaylorWedding01:
ci "Just when are you gonna propose to mah lovely daughter?"
mc "What? You want me to marry her???"
window hide
show taylorbride01 at left with moveinleft
with fastdissolve
hide cindy03
show cindy02 at right
with fastdissolve
ci "Well of course! You agreed yahself, she's dang prettier than a glob of butter mel..."
mc "...melting on some wheat cakes, yeah, yeah. But I'm a harem Master, not the husband type."
hide taylorbride01
show taylorbride02 at left
hide cindy02
show cindy03 at right
with fastdissolve
ci "Now that's no way to treat mah sweet daughter!"
mc "Well...err... Maybe she can join my harem? Or one day our wedding gets implemented by the dev?"
hide taylorbride02
show taylorbride01 at left
hide cindy03
show cindy02 at right
with fastdissolve
to "Oh yes, I hope our wedlock gets implemented in the future by popular demand!"
ci "That better happen real fast, cos we ain't washing your motorbike no more until you break mah girl's hymen and make her bleed real good, you hear me?"
hide cindy02
show cindy01 at right
with fastdissolve
ci "Now don't come back for a bikewash until you can give her some good dickin'."
to "Bye [name]! I hope to see you again real soon!"
to "Apparently, our wedlock has been implemented as of v0.6 so do come back, my future darling hubby!"
jump BackHex35

label TaylorWedding02:
window hide
show taylorbride01 at left with moveinleft
with fastdissolve
to "Oh, hi [name]! Is it true? you're gonna make me happier than a puppy with two peckers?"
mc "Err... Yeah, That's correct."
call LustPlusTaylor
hide cindy01
show cindy03 at right
with fastdissolve
ci "Now we just need to find someone else, cos we need at least two witnesses in the One-Eye of our Lord down 'ere in Texas..."
if withnone == False and alone:
    mc "(Ah, shit I can't really ask one of my harem girls, she would be mighty pissed off...)"
    mc "I'm afraid I came alone... Don't you have somebody around here you could call?"
    ci "Na, we're all alone. No Texas rangers ain't ever come round these parts in donkey's years."
    hide taylorbride01
    show taylorbride02 at left
    with fastdissolve
    to "Oh, shoot. I ain't getting married today..."
    call LustMinusTaylor
    hide cindy03
    show cindy02 at right
    with fastdissolve
    ci "Well, you'd better come back 'ere with someone. Until you do, we ain't sluttily stripping down and cleaning your bike like we's did last time!"
    mc "Fine, fine. I'll come back with someone."
    jump BackHex35
if alone == False:
    if withbe:
        mc "(Maybe I could ask Bella...)"
    if withpe:
        mc "(Maybe I could ask Penny...)"
    mc "As it happens, I came with someone, I'll go and get her!"
    hide cindy03
    show cindy01 at right
    with fastdissolve
    ci "And I'll get my New Bible."
    to "Yippee, I'm going to get knocked up by a super-huge whopper!"
    if withbe:
        scene junktownfar
        show bellaout09
        with fade
        be "So, are you ready to go back to the compound [name]?"
        mc "Err.. Not quite. I need you to do something for me. Be a witness to a totally religious ceremony."
        be "What's that?"
        mc "I'm getting married. You'll be a witness."
        hide bellaout09
        show bellaout08
        with fastdissolve
        be "I see... Are you serious about this or is it just you being stupidly young and horny?"
        mc "I'm dead serious! I need to re-populate the Earth for our Phallus Lord, remember?"
        if mcchurch <= 3:
            hide bellaout08
            show bellaoutworry
            with fastdissolve
            be "I don't believe you. Your standing in the Church is just not high enough to justify a Holy Wedding at this time. It just doesn't feel right."
            mc "What? But..."
            be "There is no but. I WON'T DO IT! Let's just go back home."
            mc "Alright, alright, gee. I'll just have to warn my future bride-not-to-be then..."
            scene junktown01
            show cindy02 at right
            show taylorbride01 at left
            ci "So, is that person coming?"
            mc "Err... No, I'm afraid, she refused. But I'll make sure she agrees next time, I swear!"
            hide cindy02
            show cindy03
            with fastdissolve
            ci "You'd better, city boy! Mah daughter is getting older fast and we don't have time to waste round 'ere!"
            hide taylorbride01
            show taylorbride02 at left
            with fastdissolve
            call LustMinusTaylor
            to "Bye... *sniff* ...[name]. I hope you come back soon... *sniff*"
            jump BackHex35
        be "Alright then, I'll do it..."
        scene junktown03 with fade
        play sound "v06/wedding.mp3"
        show taylorwedding01 at left with moveinleft
        show weddingbella01 at right with moveinright
        ci "In the name of our Phallus Lord, we are here to witness the breeding... sorry wedding, between Taylor and [name]. May they be fertile and re-populate the Earth. Se-men."
        be "Se-men."
        ci "You may kiss the bride. And then fuck her."
        hide taylorwedding01
        show taylorwedding02 at left
        hide weddingbella01
        show weddingbella02 at right
        with fastdissolve
        to "Oooh, [name], you're sssoo romantic. This breeding is going to be PERFECT!"
        call LustPlusTaylor
        mc "And err... Where are we supposed to do it by the way?"
        ci "Well, in the back of the truck, where else are you gonna make a baby in Texas?"
        be "Dare I ask you to hurry up? We need to get back to the compound soon..."
        ci "Let's just go sunbathin' while they do their stuff. I bet he knocks up mah daughter real good and fast."
        jump TaylorFuck    
    if withpe:
        scene junktownfar
        show pennyout03
        with fade
        pe "So, are you ready to go back to the compound [name]?"
        mc "Err.. Not quite. I need you to do something for me. Be a witness to my wedding."
        pe "Are you kidding me?"
        mc "No I'm not! I'm getting married and I need you to be a witness. Please, Penny, I'll owe you one, big time!"
        hide pennyout03
        show pennyout01
        with fastdissolve
        pe "Well...err... I never did something like that. But fine, let's get this over and done with then."
        scene junktown03 with fade
        play sound "v06/wedding.mp3"
        show taylorwedding01 at left with moveinleft
        show weddingpenny01 at right with moveinright
        ci "In the name of our Phallus Lord, we are here to witness the breeding... sorry wedding, between Taylor and [name]. May they be fertile and re-populate the Earth. Se-men."
        to "Se-men."
        ci "You may kiss the bride. And then fuck her."
        hide taylorwedding01
        show taylorwedding02 at left
        hide weddingpenny01
        show weddingpenny02 at right
        with fastdissolve
        to "Oooh, [name], you're sssoo romantic. This breeding is going to be PERFECT!"
        mc "And err... Where are we supposed to do it by the way?"
        ci "Well, in the back of the truck, where else are you gonna make a baby in Texas?"
        pe "Dare I ask you to hurry up? We need to get back to the compound soon..."
        ci "Let's just go sunbathin' while they do their stuff. I bet he knocks up mah daughter real good and fast."
        jump TaylorFuck
    
label TaylorFuck:
stop sound
$ tomarried = True
scene taylorfucksetup
show taylorprefuck01
with dissolve
to "So, I'm READY! Are you ready to fuck me and BREED ME, [name]?"
mc "Why don't you take off your wedding dress for me, Tayl... I mean, my darling wife."
hide taylorprefuck01
show taylorprefuck02
with fastdissolve
to "Of course, hubby! See your wife's panties? They're darn wet for your whopper!"
mc "I see... Why don't you turn round while I get... hard."
hide taylorprefuck02
show taylorprefuck03
with fastdissolve
to "I hope I'm SEXY enough to get you ROCK-HARD so you can really give it to me HARD!"
show mctaylorprefuck03 at farright with moveinright
"Oh, I'll give it to you HARD, don't worry Taylor!"
to "Look at that HUGE whopper! Come and kiss me, darling husband..."
hide taylorprefuck03
hide mctaylorprefuck03
show mctaylorprefuck04
with fastdissolve
play sound "Sounds/kiss.mp3"
to "*kiss* Please, BREED ME!"
call LustPlusTaylor
mc "Lie back on the mattress then, I'll show you how it's done."
scene pretaylorfuck01 with dissolve
play sound "Sounds/gasp.mp3"
to "Oh my Golly, your cock is just so big! How is it going to enter into my tight little virgin pussy [name]?"
mc "With all the pre-goo I'm producing right now, quite easily as a matter of fact. Let me demonstrate..."
play music "v06/taylorfuck.mp3"
label TaylorSlow:
hide taylorfuckfast
hide taylorfuckpovslow
hide taylorfuckpovfast
show taylorfuckslow
call screen taylorfuckslow01
screen taylorfuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TaylorEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TaylorFast") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("TaylorPOVSlow") 
        
label TaylorPOVSlow:
hide taylorfuckfast
hide taylorfuckslow
hide taylorfuckpovfast
show taylorfuckpovslow
call screen taylorfuckpovslow01
screen taylorfuckpovslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TaylorEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TaylorPOVFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("TaylorSlow") 

label TaylorPOVFast:
hide taylorfuckfast
hide taylorfuckslow
hide taylorfuckpovslow
show taylorfuckpovfast
call screen taylorfuckpovfast01
screen taylorfuckpovfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TaylorEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("TaylorPOVSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("TaylorFast") 

label TaylorFast:
hide taylorfuckslow
hide taylorfuckpovslow
hide taylorfuckpovfast
show taylorfuckfast
call screen taylorfuckfast01
screen taylorfuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TaylorEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("TaylorSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("TaylorPOVFast") 

label TaylorEnd:
mc "I'm gonna BREEEEDDD YOU!"
to "Please hubby, fill me up like a spermtank!"
scene taylorfuckcum01 with dissolve
stop music
play music "Sounds/splooge02.mp3"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
scene taylorfuckcum01 with fastflash
mc "RHAAA! Take my seed Taylor!"
stop music
scene taylorfuckcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "I'm coming right up your womb! AAAH!"
play sound "Sounds/splooge01.mp3"
to "I can sure darn feel it, hubby! My belly is SWELLING with your cum!"
call LustPlusTaylor
scene taylorfuckcum03 with dissolve
mc "Phew, that tight virgin pussy of yours DRAINED me."
to "So, am I a good wife?"
mc "Oooh yeah, you're a perfect cum-draining wife Taylor!"
to "Quick, get dressed, I hear Ma coming back!"
$ pregto = True
scene taylorfucksetup
show taylorpostfuck01 at left
with fade
show cindy06 at farright with moveinright
ci "So, did you knock up mah daughter real good [name]?"
mc "I'm pretty sure I did my duty."
to "Oh, yes Ma, I'm BURSTING with my hubby's bull-sized load! He came sssooo much in me, I'm dang leaking cum everywhere!"
ci "Well, lemme check... Like a good mother would do."
scene taylorpostfuck02 with dissolve
play sound "Sounds/slurp.mp3"
ci "That's darn good, boy, this is a high-grade quality sperm."
if withbe:
    be "Sorry to interfere with your family reunion, but [name] and I need to go now, it's getting late and we are expected back at the compound."
if withpe:
    pe "Sorry to interfere with your family reunion, but [name] and I need to go now, it's getting late and we are expected back at the compound."
scene taylorpostfuck03 with dissolve
to "Can I come with you hubby?"
ci "Certainly not Taylor! Your place is down 'ere in Texas with your Ma. Your husband will do his conjugal duty and come and visit you once a week to breed you until you get a baby."
mc "And if I don't come cos I'm too busy saving the world and all that?"
ci "Most likely, mah daughter's lust for you will go down I reckon..."
mc "I see. At least, there aren't any maintenance fees, right?"
ci "We girls can take care of ourselves. Huntin' varmint and such with our guns."
mc "Well, I'll be on my way then. See you my darling wife... err, Taylor, right?"
to "Yes, my name is Taylor, mah darling hubby!"
if withbe:
    be "Let's go, \"Darling Hubby\"."
if withpe:
    pe "Let's go, \"Darling Hubby\"."
jump BackHex35

label TaylorFuckAgain:
stop sound
scene taylorfucksetup
show taylorprefuck03
with dissolve
to "So, I'm READY! Are you ready to fuck me again, my darling hubby?"
show mctaylorprefuck03 at farright with moveinright
"Oh, yeah, I am READY, don't worry Taylor!"
to "Look at that HUGE whopper! Let's do it in the back of the truck. Again."
scene pretaylorfuck01 with dissolve
play sound "Sounds/gasp.mp3"
to "Oh my Golly, your cock is STILL just so big! How is it going to enter into my tight little not-so-virgin-anymore pussy [name]?"
mc "With all the pre-goo I'm producing right now, quite easily as a matter of fact. Let me demonstrate...Again."
play music "v06/taylorfuck.mp3"
label TaylorSlowAgain:
hide taylorfuckfast
hide taylorfuckpovslow
hide taylorfuckpovfast
show taylorfuckslow
call screen taylorfuckslow01b
screen taylorfuckslow01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TaylorEndAgain")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TaylorFastAgain") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("TaylorPOVSlowAgain") 
        
label TaylorPOVSlowAgain:
hide taylorfuckfast
hide taylorfuckslow
hide taylorfuckpovfast
show taylorfuckpovslow
call screen taylorfuckpovslow01b
screen taylorfuckpovslow01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TaylorEndAgain")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TaylorPOVFastAgain") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("TaylorSlowAgain") 

label TaylorPOVFastAgain:
hide taylorfuckfast
hide taylorfuckslow
hide taylorfuckpovslow
show taylorfuckpovfast
call screen taylorfuckpovfast01b
screen taylorfuckpovfast01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TaylorEndAgain")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("TaylorPOVSlowAgain") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("TaylorFastAgain") 

label TaylorFastAgain:
hide taylorfuckslow
hide taylorfuckpovslow
hide taylorfuckpovfast
show taylorfuckfast
call screen taylorfuckfast01b
screen taylorfuckfast01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TaylorEndAgain")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("TaylorSlowAgain") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("TaylorPOVFastAgain") 

label TaylorEndAgain:
mc "I'm gonna CUM!"
to "Please hubby, fill me up like a spermtank just like ya did last time!"
scene taylorfuckcum01 with dissolve
stop music
play music "Sounds/splooge02.mp3"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
scene taylorfuckcum01 with fastflash
mc "RHAAA! Take my seed Taylor!"
to "Oh God, you're making me happier than a tornado in a trailer park cumming in me like that!"
stop music
scene taylorfuckcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "I'm coming right up your womb! AAAH!"
play sound "Sounds/splooge01.mp3"
to "I can sure darn feel it, hubby! My belly is SWELLING with your cum!"
call LustPlusTaylor
scene taylorfuckcum03 with dissolve
mc "Phew, that tight Texan pussy of yours DRAINED me."
to "So, am I a good wife?"
mc "Oooh yeah, you're a perfect cum-draining wife Taylor!"
to "Quick, get dressed, I hear Ma coming back!"
$ pregto = True
scene taylorfucksetup
show taylorpostfuck01 at left
with fade
show cindy08 at farright with moveinright
ci "So, did you fuck mah daughter real good [name] again?"
mc "I'm pretty sure I did..."
to "Oh, yes Ma, I'm BURSTING with my hubby's bull-sized load! He came sssooo much in me, I'm dang leaking cum everywhere!"
ci "Well, that's just darn tootin'. I guess I'll have to clean you up then. And [name] can go back to his city life. For the time being..."
to "Bye, darling hubby! See ya again soon!"
mc "Err, yeah, bye my darling wife. And my... err... darling mother-in-law."
play music "Sounds/desertwind01.mp3"
if withbe:
    scene junktownfar
    show bellaout06
    with fade
    be "So, are you done fucking your wife again? Can we go now?"
    mc "Yep, did my duty. Balls are drained. Time to go.."
    be "So romantic... *snickers*"
    call LustMinusBella
if withpe:
    scene junktownfar
    show pennyout03
    with fade
    pe "So, are you done fucking your wife again? Can we go now?"
    mc "Yep, did my duty. Balls are drained. Time to go.."
    pe "So romantic... *snickers*"
    call LustMinusPenny
jump BackHex35

label CindyQuickFuck:
scene junktown06
show cindyprefuck
with dissolve
ci "No need for any lubing, I'm already dripping with mah own slime, so just SHOVE IT IN!"
scene junktown04
label CindyFuckSlowb:
play music "Sounds/fucksound.mp3"
hide cindyfuckfast
show cindyfuckslow
call screen cindyfuckslow01b
screen cindyfuckslow01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("CindyFuckEndb")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("CindyFuckFastb") 

label CindyFuckFastb:
ci "That's it! Pound that fuckhole faster [name]!"
hide cindyfuckslow
show cindyfuckfast
call screen cindyfuckfast01b
screen cindyfuckfast01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("CindyFuckEndb")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("CindyFuckSlowb") 

label CindyFuckEndb:
ci "You'd better give me a nice fat creamy load, boy!"
scene junktown06 blurred
show cindyfuckcum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
ci "That's it, douse your ma-in-law's pussy with your boycum!"
mc "FU-UU-UCK! I'll pull out, I'm still cumming full-blast!"
scene junktown04
show cindyfuckcum02
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH! I'm emptying my nuts!"                              
ci "That's a good boy, I'm full anyway, pump that spunk outside of mah overfilled stretched-out pussy."
ci "Now I ain't cleaning it I warned ya. So you'll just have to leave with a bike covered in cum..."
jump BackHex35

label BackHex35:
$ period += 1
scene command01
show lena01
with fade
if alone:
    le "So, what do you have to report about area D5, [name]?"
if alone == False:
    le "So, what do you have to report about area D5, scouts?"
if tomarried and toldmarried == False:
    $ toldmarried = True
    mc "I got married, Chief! It was a romantic wedding, with back-of-the-truck consummation as is traditional in Texas."
    hide lena01
    show lena06
    with fastdissolve
    le "WHAT? Is that what you're spending your time with in that hex? You're supposed to remove Trumpf from power, remember?"
    mc "It's all part of the plan, Chief! I mean, a president needs a First Lady, right?"
    hide lena06
    show lena05
    with fastdissolve
    le "Oh, because you think YOU'll be taking his place? And what competences do you have in managing a completely ruined country exactly?"
    mc "Well, err... I'll hire the best people! Like you, Chief..."
    hide lena05
    show lena06
    with fastdissolve
    le "You want ME in your cabinet?"
    mc "Sure, Chief! You're the best... err... manager I know. You can be like the Secretary of Management or something like that."
    hide lena06
    show lena05
    with fastdissolve
    le "There's no such position, but I'm flattered. In the meantime, you are DISMISSED!"
    hide lena05 with dissolve
    jump LeaveCommand
if nranramember == False:
    mc "Just a country bumpkin in the middle of nowhere Chief!"
    hide lena01
    show lena06
    with fastdissolve
    le "So the area is cleared then?"
    mc "Err... Not quite. She owns a gun store and I'd like to see what she has, something might be useful to find Trumpf City."
    hide lena06
    show lena05
    with fastdissolve
    le "*sigh* Alright. Scouts dismissed!"
    hide lena05 with dissolve
    jump LeaveCommand
if nranramember:
    mc "Just some gun store that's cheaper than Old Joe."
    hide lena01
    show lena03
    with fastdissolve
    le "Well, we'd better not tell him then, he won't be happy about that..."
    mc "Sure thing, Chief!"
    with fastdissolve
    le "Scouts dismissed!"
    hide lena03 with dissolve
    jump LeaveCommand

label ExploreHex36:
$ exploredhex36 = True
scene border01 with dissolve
mc "There seems to be some kind of wall in the distance. Hard to tell how tall it is because of deceptive perspectives on a 2D plane. Let's get closer then."
scene border02 with dissolve
mc "Ah, it turns out it's just a pathetic teenie-weenie wall after all. And there are huge, healthy cactuses on the other side..."
scene border03
show mexican01b with moveinright
hide mexican01b
show mexican01
show borderwall
with dissolve
mx "No se puede entrar en Mexico!"
mc "What?"
mx "I said, you can't enter Mexico. The border is closed."
mc "What border?"
hide mexican01
hide borderwall
show mexican02
show borderwall
with fastdissolve
mx "Didn't you notice the wall we built? This is the US-Mexico border, gringo."
mc "And where is OUR wall that Trumpf built?"
hide mexican02
hide borderwall
show mexican03
show borderwall
with fastdissolve
mx "Gone. Mexicans took it down for raw materials to build casas."
if missionti:
    mc "Well, I want to go through, I need some cactus milk."
    hide mexican03
    hide borderwall
    show mexican01
    show borderwall
    with fastdissolve
    mx "I said: PROHIBIDO ENTRAR EN MEXICO, caramba!"
if missionti == False:
    mc "I bet they used, like, average-force winds to knock it down... Anyway, I have no interest in entering your country since Spring Break is over."
    hide mexican03
    hide borderwall
    show mexican01
    show borderwall
    with fastdissolve
    mx "Adios then gringo! If you ever come back, I'll be RIGHT HERE waiting for you."
    if alone == False or withnone == False:
        mc "Let's get back to the compound, it's getting late, we have no business being here anyway."
    jump BackHex36

label BorderDialogue:
if persistent.tipson:
    show hex36tip at tips with dissolve
    pause
    hide hex36tip
menu:
    "You do realize that I have a gun while you just have a stick, lady?" if (rifle or sniper):
        mx "You cannot shoot me, that would be an act of war since I am in Mexico."
        mc "Well, you can't hit me with your st..."
        hide mexican01
        hide borderwall
        show mexican04
        show borderwall
        with fastdissolve
        play sound "Sounds/punch.mp3"
        scene border03
        show mexican04
        show borderwall
        with flash
        call MCInjury
        $ mcinjuredfight = True
        hide borderwall
        hide mexican04
        show mexican01
        show borderwall        
        with fastdissolve
        mc "Hey, what the hell was that for? This is an ACT OF WAR!"
        mx "No it's not. The end of my truncheon was in Mexico, so it's authorized by the International Post-Apocalyptic Court. Too puto bad, gringo."
        hide mexican01
        hide borderwall
        show mexican03
        show borderwall
        with fastdissolve
        mx "That is why the Mexican Army equipped us with VERY LONG sticks. You arrogant Yankee thought it was because we are poor, but it's because we are SMART! Ay, Caramba!"
        hide mexican03
        hide borderwall
        show mexican01
        show borderwall
        with fastdissolve
        jump BorderDialogue
    "Is your name Maria by any chance?" if knowmaria == False:
        hide mexican01
        hide borderwall
        show mexican03
        show borderwall
        with fastdissolve
        mx "Si. How did you guess?"
        mc "I don't know. Just an inkling for some reason..."
        hide mexican03
        hide borderwall
        show mexican01
        show borderwall
        with fastdissolve
        $ knowmaria = True
        jump BorderDialogue    
    "It's not fair. You have loads of cactuses, and we don't have any!" if knowmexico == False:
        hide mexican01
        hide borderwall
        show mexican03
        show borderwall
        with fastdissolve
        mx "Too puto bad, gringo. Now you know how it feels to want something ON THE OTHER SIDE of the border!"
        mc "How come they all are on YOUR SIDE anyway?"
        hide mexican03
        hide borderwall
        show mexican01
        show borderwall
        with fastdissolve
        mx "Because we don't let camels into our country. CAMELLOS PROHIBIDOS EN MEXICO!"
        $ knowmexico = True
        jump BorderDialogue    
    "Show us ya tits, Mexican lady. I'll throw you some money across the border.":
        hide mexican01
        hide borderwall
        show mexican04
        show borderwall
        with fastdissolve
        play sound "Sounds/punch.mp3"
        scene border03
        show mexican04
        show borderwall
        with flash
        call MCInjury
        $ mcinjuredfight = True
        hide borderwall
        hide mexican04
        show mexican01
        show borderwall        
        with fastdissolve
        mc "Hey, what the hell was that for?"
        mx "You think I'm some cheap PUTA? I am a soldier in the EJERCITO MEXICANO, stupid gringo!"  
        jump BorderDialogue
    "I'll pay you to get some cactus milk over there.":
        mx "Oh si? I have no use for your New Dollars. The Mexican currency is PESOS or TACOS!"
        mc "Tacos?!?!"
        hide mexican01
        hide borderwall
        show mexican05
        show borderwall
        with fastdissolve
        mx "Si! Me gustan los tacos! Mmmh, muy mucho!"
        mc "(Well shit, Trumpf got rid of all the taco trucks, I don't have any tacos to trade with her...)"
        hide mexican05
        hide borderwall
        show mexican01
        show borderwall
        with fastdissolve        
        jump BorderDialogue
    "What if I unleashed a camel across your pathetic wall? How would you like THAT?" if camels == 1 and knowmexico:
        mx "I'll hit it with my stick until it goes back into your country, gringo!"
        mc "Ah, shit... I might need more camels if this threat is ever going to work..."
        jump BorderDialogue
    "What if I unleashed several camels across your pathetic wall? How would you like THAT?" if camels >= 2 and knowmexico:
        hide mexican01
        hide borderwall
        show mexican06
        show borderwall
        with fastdissolve
        mx "Qué? No, senor, por favor! I can't hold off more than one camel at a time with my stick!"
        mc "Well, I have MORE THAN ONE CAMEL... So, give me some cactus milk OR ELSE!"
        hide mexican06
        hide borderwall
        show mexican07
        show borderwall
        with fastdissolve        
        mx "Qué miseria! Ok, Ok, gringo. I'll get you some cactus milk, but please keep your camels on a leash."
        mc "Now that's better, you're becoming more reasonable."
        hide mexican07 with dissolve
        "A while later..."
        scene border03
        show mexican08
        show borderwall
        with fade
        mx "There. I filled up your bottle with cactus milk."
        window hide
        show cactusmilk at posmission
        pause
        hide cactusmilk
        $ cactusmilk = True
        mc "Thank you, Mexican lady. I hope you didn't get stung by a cactus while milking it. lol..."
        hide mexican08
        hide borderwall
        show mexican01
        show borderwall
        with fastdissolve 
        mx "I know how to avoid PRICKS. Speaking of which, leave now and never come back to Mexico, gringo!"
        mc "I had no intention! Spring Break is not until...err... next spring."
        if alone == False or withnone == False:
            mc "Let's get back to the compound, it's getting late and I got what I wanted anyway."
        $ clearedhex36 = True
        $ missiontidone = True
        jump BackHex36       
    "Leave":
        if alone == False or withnone == False:
            mc "Let's get back to the compound, it's getting late, I'll think of some other way of getting across that damn border."
        jump BackHex36
        
label BackHex36:
$ period += 1
scene command01
show lena01
with fade
le "So, what do you have to report about area D6, scouts?"
if clearedhex36:
    mc "We reached the end of the known world."
    hide lena01
    show lena03
    with fastdissolve
    le "What?"
    mc "The Mexican border I mean. Foreign land. Very dangerous, full of drug lords and rap..."
    hide lena03
    show lena10
    with fastdissolve
    le "Spare us your diatribe! Is the hex cleared? This is all I want to know!"
    mc "Yep, all cleared, Chief Lena!"
    hide lena10
    show lena01
    with fastdissolve
    le "Good. So we can move on to other hexes. All of which are within the known US territory. Scouts DISMISSED!"
    if mcinjured:
        mc "I'd better get to the medbay after that beating I got."
        jump Medbay  
    jump LeaveCommand
if clearedhex36 == False:
    mc "We reached the end of the known world."
    hide lena01
    show lena03
    with fastdissolve
    le "What?"
    mc "The Mexican border I mean. Foreign land. Very dangerous, full of rap..."
    hide lena03
    show lena10
    with fastdissolve
    le "Spare us your diatribe! Is the hex cleared? This is all I want to know!"
    mc "Nope, not at all, I had to deal with a tough Mexican Border Guard who would simply not let me into Mexico."
    mc "So I need to get back there again. I want to know what's so nice over there that they built a wall to stop us from getting in!"
    hide lena10
    show lena05
    with fastdissolve
    le "*sigh*. You'd better clear this hex QUICKLY, [name]! We don't have time to waste at that border, Trumpf City is clearly NOT there. Scouts DISMISSED!"
    if mcinjured:
        mc "I'd better get to the medbay after that beating I got."
        jump Medbay  
    jump LeaveCommand

label ExploreHex44:
stop sound
$ explored = True
play music "Sounds/desertwind01.mp3"
scene desertman01 with fade
$ exploredhex44 = True
if seencohen == False:
    mc "What's that guy doing in the middle of the desert with a camel?"
    if persistent.tipson and angiereunited == False:
        show cohentip at tips with dissolve
        pause
        hide cohentip
    if withpe: 
        pe "I'd say he's just a lone survivor. We could get a camel out of it, but nothing much..."
        mc "Let's get closer then..."
    if withbe:
        be "Most likely a lone survivor. He looks like he needs guidance. Like from the Phallus Lord."
        mc "Let's have a closer look at him..."
    if alone and withay:
        ay "A man in the desert. BORING!"
        mc "Let's have a closer look at him, he might be less boring up close."
    if alone and witham:
        am "Be careful, his camel doesn't look in the best of shapes, it's a sign he does love Mother Nature."
        mc "Let's have a closer look at him then. And that camel of his."
    if alone and withan:
        an "Maybe he's a SUPER-HERO in disguise? How EXCITING!"
        mc "You have a wild imagination but let's check if you're right..."
    if alone and withru:
        ru "I could shoot him from this distance. Easily."
        mc "Let's... deal with this some OTHER way."
    if alone and withmi:
        mi "Be careful [name]. I sense a disturbance in the Force. Of Mother Nature."
        mc "I didn't realize you were a Jedi. Let's get closer to this \"disturbance\" then..."
    if alone and withmo:
        mo "Be careful sweetie! I have a bad feeling about men. And this man in particular."
        mc "Stay back, I'll go and see what he's up to."
    if alone and withsu:
        su "Just another nomad fighting for his survival. I pity him. He should be fighting on OUR side."
        mc "Let's have a closer look at him, maybe he has valuable intel."
    if alone and withcy:
        cy "I think I will go into my resting mode. I don't envisage me being needed here."
        mc "Hey! But ok, he doesn't look dangerous, I agree. I'll go and meet him ALONE, then..."
    if alone and withza:
        za "Oh, a fellow nomad! Maybe he has seen my father!"
        mc "It's a stretch, but a possibility. Let's go and meet him to find out then."
    if alone and withgw:
        gw "He looks dirty. I'll stay back if you don't mind."
        mc "Right. So, you're no use to me at all on this scouting mission then."
    if alone and withma:
        ma "I can tell you that he doesn't look like a Road Warrior."
        mc "Ok, so he's not dangberous then."
    if alone and withcl:
        cl "What a poor lost soul, I'm sure he needs our guidance."
        mc "Don't worry, I'll guide him alright. Once I find out what he's doing here."
    if alone and withla:
        la "This guy doesn't look right. There's something stinky about him."
        mc "As stinky as a BostiBoobicus Gigantus?"
        la "Just be careful [name]."
    if alone and withba:
        ba "I don't like this man, he doesn't look like a proper American..."
        mc "Well, let's find out..."
    if alone and withde:
        de "I find the best course of action when meeting a stranger is to blow them up with..."
        mc "Please stay out of this, I'll talk to him before testing explosives on him if you don't mind."
        de "Umpf..."

if seencohen:
    mc "Ah, he hasn't moved one bit since last time. What a schmuck."
    
scene desertman02 with dissolve
show cohenbody01
show kohn01
with dissolve
co "Hi there, friend!"
hide kohn01
show cohen01
mc "I'm not your friend, buddy!"
hide cohenbody01
hide cohen01
show cohenbody02
show kohn02
with fastdissolve
play sound "Sounds/relax.mp3"
co "Hey, relax, guy, trust me!"
hide kohn02
show cohen05
if seencohen == False:
    if alone:
        mc "He looks strangely familiar. I think it's Michael Kohn, Trumpf's personal attorney!"
    if withbe:
        be "He looks strangely familiar. I think it's Michael Kohn, Trumpf's personal attorney!"
    if withpe:
        pe "He looks strangely familiar. I think it's Michael Kohn, Trumpf's personal attorney!"
    hide cohenbody02
    hide cohen05
    show cohenbody01
    show kohn01
    with fastdissolve
    co "EX-attorney if you please. I was thrown under the bus, like all the others!"
    hide kohn01
    show cohen01
    with fastdissolve
    hide cohen01
    show kohn01
    with fastdissolve
    co "And my daughter Lolly was kidnapped by Epstein. Lolly Kohn. Got it?"
    hide kohn01
    show cohen01
    with fastdissolve    
    $ seencohen = True

if seencohen:
    mc "So, you're not back in jail yet?"
    hide cohenbody02
    hide cohen05
    show cohenbody01
    show kohn01
    with fastdissolve    
    co "Ah, ah, very funny. I was thrown under the bus, remember?"
    hide kohn01
    show cohen01
    with fastdissolve
    
menu:
    "Never mind that, I want that camel of yours. (+1 Road Warriors)":
        hide cohenbody01
        hide cohen01
        show cohenbody02
        show kohn02
        with fastdissolve
        co "I thought you were my friend, buddy!"
        hide kohn02
        show cohen05
        with fastdissolve
        mc "I'm NOT, I told you! Now give me that camel OR ELSE!"
        hide cohenbody02
        hide cohen05
        show cohenbody01
        show kohn01
        with fastdissolve                
        co "I used to bully people and now I'm being bullied! Take it and leave me to die then, guy!"
        hide kohn01
        show cohen01
        with fastdissolve        
        mc "I'm a ROAD WARRIOR, that's our way..."
        call PlusWarrior
        hide cohenbody01
        hide cohen01
        show cohenbody02
        show kohn02
        with fastdissolve
        play sound "Sounds/buddy.mp3"
        co "You guys are worse than lawyers! Fuck you buddy!"
        hide kohn02
        show cohen05
        with fastdissolve        
        $ camels += 1
        $ clearedhex44 = True
        if withpe:
            pe "Let's just leave him to die. I hate lawyers anyway."
            mc "And let's go back to the compound with that camel then."
        if withbe:
            be "I'm sure he'll find his way, the Phallus Lord will guide him, like he guides all survivors."
            mc "Let's go back to the compound with that camel then."
        jump BackExploreHex44
    "Never mind that, I want that camel of yours." if mcwarrior == 5:
        hide cohenbody01
        hide cohen01
        show cohenbody02
        show kohn02
        with fastdissolve
        co "I thought you were my friend, buddy!"
        hide kohn02
        show cohen05
        with fastdissolve
        mc "I'm NOT, I told you! Now give me that camel OR ELSE!"
        hide cohenbody02
        hide cohen05
        show cohenbody01
        show kohn01
        with fastdissolve        
        co "I used to bully people and now I'm being bullied! Take it and leave me to die then, guy!"
        hide kohn01
        show cohen01
        with fastdissolve        
        mc "I'm a ROAD WARRIOR, that's our way..."
        hide cohenbody01
        hide cohen01
        show cohenbody02
        show kohn02
        with fastdissolve
        play sound "Sounds/buddy.mp3"
        co "You guys are worse than lawyers! Fuck you buddy!"
        hide kohn02
        show cohen05
        with fastdissolve        
        $ camels += 1
        $ clearedhex44 = True
        if withpe:
            pe "Let's just leave him to die. I hate lawyers anyway."
            mc "And let's go back to the compound with that camel then."
        if withbe:
            be "I'm sure he'll find his way, the Phallus Lord will guide him, like he guides all survivors."
            mc "Let's go back to the compound with that camel then."
        jump BackExploreHex44
    "What are you up to? More dodgy deals with Trumpf?":
        hide cohenbody01
        hide cohen01
        show cohenbody02
        show kohn02
        with fastdissolve
        co "Hey! He's not my friend anymore, buddy!"
        hide kohn02
        show cohen05
        with fastdissolve
        mc "And can you prove it or are you lying, just like him?"
        hide cohen05
        show kohn02
        with fastdissolve
        co "Sure I could prove it, guy. I could write a book. OR..."
        hide cohenbody02
        hide kohn02
        show cohenbody03
        show kohn03
        with fastdissolve        
        co "I could sell you this tape for only 50 bucks, friend! The PEE-PEE tape... OCTOBER SURPRISE!"
        hide kohn03
        show kohn03
        with fastdissolve
        co "With that, you could... BLACKMAIL him, just like Pewtin has been doing all along..."
        mc "So why don't YOU do it, then?"
        hide kohn03
        show kohn03
        with fastdissolve
        play sound "Sounds/relax.mp3"
        co "He's onto me, buddy. I'm running away from him. Hey, relax guy, trust me, it's the REAL McCOY! Guy gets pissed on by Russian hookers and loves it. Slurps it all up, friend!"
        hide kohn03
        show cohen09
        with fastdissolve        
        if alone and withan:
            an "Is he talking about our nice President-for-life???"
            mc "Errr, yeah, cover your ears, Angie, this is not for you."
        if alone and withsu:
            su "I think it's worth a shot, you should buy it [name]!"
        if withpe:
            pe "I think it's worth a shot, you should buy it [name]!"
        if withbe:
            be "I think it's worth a shot, you should buy it [name]!"
        menu:
            "Buy the tape" if money >= 50:
                mc "Alright, I'll have it."
                hide cohenbody03
                hide cohen09
                show cohenbody02
                show kohn02
                with fastdissolve        
                co "It's a bargain, I tell ya, buddy!"
                hide kohn02
                show cohen05
                with fastdissolve
                $ money -= 50
                $ peetape = True
                window hide
                show peepeetape at posmission
                $ renpy.pause(1.0, hard=True)
                pause
                hide peepeetape
                $ clearedhex44 = True
                mc "Let's get back to the compound now. I think I got everything I could get out of that lawyer."
                hide cohenbody02
                hide cohen05
                show cohenbody01
                show kohn01
                with fastdissolve
                co "See ya, guy!"
                jump BackExploreHex44                
            "Don't buy the tape" if money >= 20:
                mc "No, I'm not in, it sounds dodgy as hell."
                hide cohenbody03
                hide cohen09
                show cohenbody02
                show kohn02
                with fastdissolve        
                play sound "Sounds/buddy.mp3"
                co "What? Me, dodgy? Fuck you buddy!"
                hide kohn02
                show cohen05
                with fastdissolve                
                mc "Whatever. Let's leave."
                jump BackExploreHex44
            "I don't have enough money but I'm potentially interested..." if money <= 19:
                hide cohenbody03
                hide cohen09
                show cohenbody02
                show kohn02
                with fastdissolve        
                co "Well, I ain't moving from this patch of desert. So come back with the money, and the tape is yours, friend!"
                hide kohn02
                show cohen05
                with fastdissolve                
                mc "Alright. Let's leave now."
                jump BackExploreHex44
    "Do you know where Trumpf City is?":
        hide cohenbody01
        hide cohen01
        show cohenbody02
        show kohn02
        with fastdissolve
        co "Sure I do, buddy! How much are you willing to give me for that confidential information, friend?"
        hide kohn02
        show cohen05
        with fastdissolve
        mc "What? You call yourself my friend and you want money, just for a piece of info?"
        hide cohenbody02
        hide cohen05
        show cohenbody01
        show kohn01
        with fastdissolve        
        co "I have a retaining fee everytime I open my mouth, guy! Actually, you already owe me around 650 dollars, buddy!"
        hide kohn01
        show cohen01
        with fastdissolve
        mc "I'm not your buddy, guy!"
        hide cohen01
        show kohn01
        with fastdissolve
        co "I'm not your guy, friend!"
        hide kohn01
        show cohen01
        with fastdissolve
        mc "I'm not your friend, buddy!"
        if withpe:
            pe "Alright, let's stop this silly nonsense, I'm going back to the compound. NOW."
        if withbe:
            be "Alright, let's stop this silly nonsense, I'm going back to the compound. NOW."
        scene desertman03 with dissolve
        play sound "Sounds/notbuddy.mp3"
        $ renpy.pause(1.0, hard=True)
        co "I'm not your buddy, guy!"
        mc "I'm not your guy, friend!"        
        play sound "Sounds/buddy.mp3"
        co "You're leaving without paying the retaining fee? Fuck you, buddy!"
        window hide
        if withpe:
            play sound "Sounds/explorepenny02.mp3"
            pause 2
            stop sound            
        if withbe:
            play sound "Sounds/explorebella02.mp3"
            pause 2
            stop sound            
        jump BackExploreHex44
                    
label BackExploreHex44:
stop music
$ period +=1
scene command01
show lena01
with fade
if alone:
    le "So, what do you have to report about area E4, [name]?"
if alone == False:
    le "So, what do you have to report about area E4, scouts?"
if clearedhex44 and peetape == False:
    mc "We met some lawyer dude and stole his camel."
    hide lena01
    show lena03
    with fastdissolve
    le "You stole something from a lawyer? How did you manage that???"
    mc "He had a camel. I stole it by force and now I have it. And the hex is also cleared, Chief!"
    hide lena03
    show lena06
    with fastdissolve
    le "Well, that's... kind of impressive. DISMISSED!"
    hide lena06
    with dissolve
    jump LeaveCommand
if clearedhex44 and peetape:
    mc "I have the pee-pee tape, Chief!"
    hide lena01
    show lena03
    with fastdissolve
    le "What pee-pee tape?"
    mc "You know, the one where Trumpf gets pissed on by some Russian hookers. Slurps it all up apparently, filthy bugger."
    hide lena03
    show lenapensive
    with fastdissolve
    le "Are you sure it's genuine? Maybe I should have a look, just to make sure..."
    mc "Hey! You're trying to watch the pee-pee tape before me? Are you into that kind of stuff, Chief?"
    hide lenapensive
    show lena11
    with fastdissolve
    le "No... I mean, it was purely out of political interest. But you're right. It's YOUR pee-pee tape..."
    mc "Damn right it's MY pee-pee tape! I paid good money for that and I intend to watch it intently and then blackmail the fucker with it!"
    hide lena11
    show lena07
    with fastdissolve
    le "Well, I'm glad to hear that! Of course, IF it's genuine... You are dismissed!"
    call PlusDeep
    hide lena07
    with dissolve
    jump LeaveCommand
if clearedhex44 == False:
    mc "I met Trumpf's ex-lawyer, Michael Kohn. He's my friend now. Or my buddy, I can't remember."
    hide lena01
    show lena03
    with fastdissolve
    le "And did you get valuable intel out of your new \"friend\"?"
    mc "Not yet. But that buddy of mine, he owes me. He's my GUY now. Or maybe my friend."
    hide lena03
    show lena10
    with fastdissolve
    le "Well, get your \"buddy guy friend\" to be useful QUICKLY and clear that hex, understood?"
    mc "Roger that, Chief. You're still my friend, right?"
    hide lena10
    show lenapensive
    with fastdissolve
    le "*sigh* You are dismissed, [name]."
    hide lenapensive
    with dissolve
    jump LeaveCommand
    
label ExploreHex45:
$ exploredhex45 = True
play music "Sounds/desertwind01.mp3"
scene factoryfar01 with fade
mc "There seems to be some kind of abandoned industrial building, in the middle of nowhere..."    
if withbe:
    be "I sense evil here... But we are protected by the Phallus Lord so let's go inside!"
    mc "Err... You're SURE he's protecting us?"
    be "Of course I am! Come on, let's move [name]!"
if withpe:
    pe "I don't like this place, but we must investigate and clear this area..."
    mc "Couldn't we just tell Chief Lena we did, and forget about it? I mean, she wouldn't be any wiser..."
    pe "Stop being a coward and let's move!"
if alone:
    call AloneStance
        
scene factory01 with dissolve
if persistent.tipson:
    show hexe5tip at tips with dissolve
    pause
    hide hexe5tip            
play music "v06/spooky.mp3"
mc "This place is spooky. Even the music playing in my head is spooky."
if withbe:
    be "I... tend to agree. I can hear it too. May the Phallus Lord protect us from all Evil!"
if withpe:
    pe "I... tend to agree. I can hear it too. And I never heard such spooky music before even during my times as a bloodthirsty Road Warrior."    
scene factory02 with dissolve
mc "Nothing to see in this spooky place apparently. Let's go home then."
window hide
show factorygirl01 with dissolve
$ renpy.pause(1.0, hard=True)
play sound "v06/lalala.wav"
$ renpy.pause(2.0, hard=True)
hide factorygirl01 with dissolve
mc "Was that a little girl?"
window hide
show factorygirl02 with dissolve
play sound "v06/lalala.wav"
$ renpy.pause(2.0, hard=True)
hide factorygirl02 with dissolve
$ renpy.pause(0.5, hard=True)
show factorygirl03 with dissolve
$ renpy.pause(1.0, hard=True)
mc "There she is on the left behind that corner! How did she move so fast?"

if withbe:
    be "Poor thing, she needs the guidance of the Phallus Lord."
if withpe:
    pe "Poor thing, all alone in this... spooky place."
if alone:
    mc "Poor thing, all alone in this.. spooky place."

scene factory03 with dissolve
play sound "v06/lalala.wav"
mc "I could have sworn she was around here..."
stop music
play sound "Sounds/thunder.mp3"
show creepy01 with fastflash
cg "Please, help me!"
menu:
    "What's wrong?":
        jump Creepy02
    "Err, why are you in a straitjacket?":
        jump Creepy03
    "Damn girl, you scared the bejeezus out of me!":
        jump Creepy04
    
label Creepy02:
hide creepy01
show creepy02
with fastdissolve
cg "Some nasty people came... *sob*"    
play sound "v06/sobbing.mp3"
hide creepy02
show creepy03
with fastflash
play sound "Sounds/thunder.mp3"
cg "...INTO MY LAIR!"
if talisman:
    jump CreepyTalisman
if talisman == False:
    jump CreepyNoTalisman

label Creepy03:
hide creepy01
show creepy02
with fastdissolve
cg "The nasty men tried to..."
hide creepy02
show creepy03
with fastflash
play sound "Sounds/thunder.mp3"
cg "...RESTRAIN ME!"
if talisman:
    jump CreepyTalisman
if talisman == False:
    jump CreepyNoTalisman

label Creepy04:
hide creepy01
show creepy02
with fastdissolve
play sound "v06/sobbing.mp3"
cg "*sob* I'm just... a little girl. I'm... not... scary..."
hide creepy02
show creepy03
with fastflash
play sound "Sounds/thunder.mp3"
cg "AM I?"
if talisman:
    jump CreepyTalisman
if talisman == False:
    jump CreepyNoTalisman

label CreepyTalisman:
hide creepy03
show creepy02
with fastdissolve
cg "AAAAH, the Talisman, the PP-RRRECIOUS!"
hide creepy02
show creepy05
with flash
mc "Looks like that talisman Titahontas gave me scared this creepy girl."
hide creepy05 with dissolve
menu:
    "Continue looking for her":
        jump CreepyEnd
    "Clear the area and leave":
        mc "Well, nothing to see or find in this creepy place so let's go back to the compound!"
        if withbe:
            be "I wholeheartedly agree."
        if withpe:
            pe "I wholeheartedly agree."
        jump BackHex45

label CreepyNoTalisman:
hide creepy03
show creepy04
with fastdissolve
play sound "v06/knife.mp3"
cg "Bad, bad man!"
call MCInjury
$ mcinjuredjaguar = True
mc "Hey, what the fuck!"
hide creepy04
show creepy05
with flash
play sound "v06/lalala.wav"
cg "hi hi hi..."
menu:
    "Continue looking for her":
        jump CreepyEnd
    "Get the hell out of here.":
        if withbe:
            be "I wholeheartedly agree."
        if withpe:
            pe "I wholeheartedly agree."
        jump BackHex45

label CreepyEnd:
scene factory04 with dissolve
play music "v06/spooky.mp3"
if talisman:
    play sound "v06/lalala.wav"
    cg "Put the PP-RRECIOUS in the box!"
    menu:
        "Fine, creepy little girl, I'll give you my talisman.":
            scene factory05 with dissolve
            mc "There... Now what?"
            jump CreepyGoodEnd
        "Fuck you creepy girl, it's MY talisman!":
            show creepy03 with flash
            play sound "Sounds/thunder.mp3"
            cg "No, it's MY PP-RRECIOUS!"
            mc "Uh oh... OK, let's get the hell out of here! I'm already injured and I can't die!"
            jump BackHex45
            
if talisman == False:
    show creepy03 with flash
    play sound "Sounds/thunder.mp3"
    cg "Why are you STILL here?"
    mc "Err... Just looking for the exit, don't mind me..."
    if withbe:
        be "She's nuts and dangerous, let's leave this place [name]!"
    if withpe:
        pe "She's nuts and dangerous, let's leave this place [name]!"
    mc "Yeah, I think it would be wise... Bye bye, little girl, have a...err.. nice day!"
    hide creepy03
    show creepy02
    with fastdissolve
    play sound "v06/sobbing.mp3"        
    cg "Oh no, they're leaving me all alone. AGAIN!"
    hide creepy02 with dissolve
    jump BackHex45
    
label CreepyGoodEnd:
stop music
$ talisman = False
$ usedtalisman = True
show creepy06 with flash
play sound "Sounds/thunder.mp3"
cg "It's so BEAUTIFUL! My PP-RRECIOUS!"
hide creepy06
show creepy07
with fastflash
cg "My head... What... What happened to me? Who are you mister?"
mc "You were cursed and I just saved you apparently. As well as made you stark naked, but that's NOT what I wished for, I want to make this perfectly clear, OK?"
cg "Oh, thank you mister... Err... Do you have any clothes for me or are you going to stare at my tits a while longer?"
if withbe:
    be "Of course little girl, here take this shirt to cover your naughty bits. And we'll help you remove your harness."
    jump CreepyGoodEndb
if withpe:
    pe "Of course little girl, here take this shirt to cover your naughty bits. And we'll help you remove your harness."
    jump CreepyGoodEndb
mc "Err, no sorry, I don't have anything handy with me right now..."   
hide creepy07
show creepy09
with dissolve
play sound "v06/sobbing.mp3"
cg "Well, thanks for NOTHING for leaving me NAKED in this spooky place like that!"
mc "Err, can I have my talisman back then?"
hide creepy09
show creepy10
with dissolve
cg "What??? What a CREEP! Get out of MY home!"
mc "Alright, alright, gee! I'm leaving."
jump BackHex45b

label CreepyGoodEndb:
hide creepy07
show creepy08
with dissolve
cg "Gee, thanks a lot! I was getting cold in this... spooky place."
mc "Well, maybe I can get my talisman back now, thank you very much."
if withbe:
    be "How dare you? After all this poor girl has gone through? You GAVE it to her!"
if withpe:
    pe "How dare you? After all this poor girl has gone through? You GAVE it to her!"
    mc "Yeah, but isn't it the Road Warrior's way to TAKE BACK anything you give?"
    pe "Not really, never heard of THAT rule."
    mc "Damn, seemed like a nice Road Warrior rule."
hide creepy08
show creepy11
with dissolve
cg "I have something for you mister, but I get to keep the talisman!"
if mcbike == False and (hulkgem == False or gem == False):
    cg "I found some diamonds in a pit behind the factory..."
    show gemsparkling
    $ renpy.pause(0.1, hard=True)
    hide gemsparkling
    $ renpy.pause(0.05, hard=True)
    show gemsparkling
    $ renpy.pause(0.1, hard=True)
    hide gemsparkling
    $ renpy.pause(0.05, hard=True)
    show gemsparkling
    $ renpy.pause(0.1, hard=True)
    hide gemsparkling
    $ renpy.pause(0.05, hard=True)
    show gemsparkling
    $ renpy.pause(0.1, hard=True)
    hide gemsparkling
    $ renpy.pause(0.05, hard=True)
    window hide
    show gems at posmission
    $ renpy.pause(2.0, hard=True)
    pause
    hide gems
    mc "Ah, great,that last haul of diamonds, I needed it to buy myself a motorbike! Now I can go and visit Diamond in the strip club in Desert Town..."
    mc "Bye, creey little girl!"
    if hulkgem == False:
        $ hulkgem = True
        jump BackHex45b
    if gem == False:
        $ gem = True
    jump BackHex45b
cg "I found some money in a drawer in the factory's office... ANd I don't need it."
$ money += 30
mc "Thirty bucks? Then it was worth coming here and clearing that hex. Will you be alright alone here, creepy little girl?"
hide creepy11
show creepy08
with dissolve
cg "Oh, yes mister, don't worry about me... Now that I have my PRECIOUS, I can make this place my HOME."
mc "Err, okay. Goodbye then."
jump BackHex45b

label BackHex45:
scene factoryfar01 with dissolve
if withbe:
    scene factoryfar01
    show bellaout01
    with dissolve
    be "I'm still spooked out, let's go back to the compound and never come back to this place!"
if withpe:
    scene factoryfar01
    show pennyout01
    with dissolve
    pe "Even though I'm a Road Warrior, I'm still spooked out, let's go back to the compound and never come back to this place!"
    
label BackHex45b:
$ clearedhex45 = True
stop music
$ period += 1
scene command01
show lena01
with fade
le "So, what do you have to report about that hex D5?"
mc "An abandoned factory, Chief. Nothing inside whatsoever. Tha area is clear."
if mcinjured: 
    hide lena01
    show lena06 
    with fastdissolve
    le "And how do you explain all these cuts on your body then?"
    mc "Err... Industrial hazard, Chief! You know, while inspecting the building."
    hide lena06
    show lena03
    with fastdissolve
    le "Well go and see Nurse Rachel at the medbay then, we need you in top form, I know we are close to our goal!"
    mc "Sure thing, Chief Lena!"
    jump Medbay
hide lena01
show lena06 
with fastdissolve
le "Umpf, disappointing. But I know we are close to our goal! You are dismissed."
hide lena06 with dissolve
jump LeaveCommand    

label ExploreHex46:
$ exploredhex46 = True
scene swamps01 with fade
if seenwendy:
    mc "Back to the edge of swampy Louisiana. I'll go alone, like last time..."
    jump Louisiana02
if withbe:
    be "We seem to have reached the edge of a swampy jungle. I can't go any further with my rig..."
    mc "I'll go alone and explore that forest a bit then."
    be "Fine, I'll be waiting for you right here, don't take too long [name]!"
    jump Louisiana02
if withpe:
    pe "We seem to have reached the edge of a swampy jungle. I can't go any further with my rig..."
    mc "I'll go alone and explore that forest a bit then."
    pe "Fine, I'll be waiting for you right here, don't take too long [name]!"
    jump Louisiana02
if alone:
    mc "I seem to have reached the edge of a swampy jungle. I can't go any further with my rig... So I'll go alone then."
    call AloneStance
    jump Louisiana02
  
label Louisiana02:
scene swamps02 with fade
play music "v06/swamp.mp3"
if seenwendy:
    mc "Damn those gators are still there. In exactly the same position too."
    jump Louisiana03
if seenwendy == False:
    mc "Oh, there seems to be a house over there, but gators in the way... This place is really inhospitable, I wonder what part of the US it used to be?"
    menu:
        "Press forward despite the danger":
            jump Louisiana03
        "Get back to the compound like a coward":
            jump BackHex46
        
label Louisiana03:
stop music
scene pitfall01
show mcpitfall01a
with dissolve
if seenwendy:
    mc "And I have to go past them again like a stupid Tarzan."
if seenwendy == False:
    mc "Hey, why am I all pixelated? This game has gone back to 80's technology, it's pathetic."
hide mcpitfall01a
show pitfallclip02
show mcpitfall01a
show pitfallvine02
with fastdissolve
if seenwendy == False:
    mc "Ah, I see, I've got to catch that vine and jump over those alligators..."
hide mcpitfall01a
show mcpitfall02 at pitfallpos01
show mcpitfall02 at pitfallpos02 with move
hide mcpitfall02
show mcpitfall01b
$ pitfall01_time = 9.6
call screen pitfall
screen pitfall:
    modal True
    add pitfall
    add pitfallvine
    add "v06/mcpitfall01b.png"
    if pitfall01_time <= 0:
        timer .01 action Return
    else:
        timer .1 repeat True action SetVariable("pitfall01_time", pitfall01_time-.1)

    imagebutton:
        focus_mask True
        idle "v06/jump.png"
        hover "v06/jump.png"
        action Jump ("PitfallJump01")
    
label PitfallFail01:
"You were too slow..."
label PitfallFail02:
scene pitfallfail with dissolve
play sound "v06/gator.mp3"
mc "Get OFF me, you nasty lizard, I'm not edible!"
call MCInjury
$ mcinjuredgator
scene swamps02 with fade
play music "v06/swamp.mp3"
mc "*puff* I finally managed to get away...  Can't go on, I'm too injured, need to go back to the compound..."
jump BackHex46

label PitfallJump01:
if (pitfall01_time >= 7.0 and pitfall01_time <= 7.6) or (pitfall01_time >= 3.8 and pitfall01_time <= 4.4):
    jump PitfallSuccess01
else:
    scene pitfall02
    play sound "v06/jump.mp3"
    show mcpitfall02 at pitfallpos07
    show vine05
    mc "oh, oh..."
    hide mcpitfall02  
    show mcpitfall02 at pitfallpos08
    pause 0.5
    jump PitfallFail02

label PitfallSuccess01:
scene pitfall01
play sound "v06/jump.mp3"
show mcpitfall02 at pitfallpos04
show vine01
pause 0.2
hide mcpitfall02
hide vine01
play sound "v06/vine.mp3"
show pitfallvinemc
pause 2.4
hide pitfallvinemc
show mcpitfall02 at pitfallpos05
show vine09
pause 0.2
hide mcpitfall02
hide vine09
show pitfallclip02
show pitfallvine03
show mcpitfall01 at pitfallpos03
mc "I did it!"
hide mcpitfall01
show mcpitfall02 at pitfallpos03
show mcpitfall02 at pitfallpos06 with move
hide mcpitfall02
show mcpitfall01 at pitfallpos06
mc "I'm clear!"
if seenwendy:
    jump Louisiana04
scene pitfall03
show mcpitfall01a
show pitfallvine02
with dissolve
mc "What? Not AGAIN!"

hide mcpitfall01a
show mcpitfall02 at pitfallpos01
show mcpitfall02 at pitfallpos02 with move
hide mcpitfall02
show mcpitfall01b
$ pitfall02_time = 9.6
call screen pitfall02
screen pitfall02:
    modal True
    add "v06/pitfall03.jpg"
    add pitfallvine
    add "v06/mcpitfall01b.png"
    if pitfall02_time <= 0:
        timer .01 action Return
    else:
        timer .1 repeat True action SetVariable("pitfall02_time", pitfall02_time-.1)

    imagebutton:
        focus_mask True
        idle "v06/jump.png"
        hover "v06/jump.png"
        action Jump ("PitfallJump02")
    
label PitfallFail03:
scene pitfallfail with dissolve
mc "Oh, there was a gator in this hole too! Get OFF me, you nasty lizard, I'm not edible!"
call MCInjury
$ mcinjuredgator

label PitfallJump02:
if (pitfall02_time >= 7.0 and pitfall02_time <= 7.6) or (pitfall02_time >= 3.8 and pitfall02_time <= 4.4):
    jump PitfallSuccess02
else:
    jump PitfallFail02

label PitfallSuccess02:
scene pitfall03
play sound "v06/jump.mp3"
show mcpitfall02 at pitfallpos04
show vine01
pause 0.2
hide mcpitfall02
hide vine01
play sound "v06/vine.mp3"
show pitfallvinemc
pause 2.4
hide pitfallvinemc
show mcpitfall02 at pitfallpos05
show vine09
pause 0.2
hide mcpitfall02
hide vine09
show pitfallvine03
show mcpitfall01 at pitfallpos03
mc "I did it!"
hide mcpitfall01
show mcpitfall02 at pitfallpos03
show mcpitfall02 at pitfallpos06 with move
hide mcpitfall02
show mcpitfall01 at pitfallpos06
mc "I'm clear! Of this stage anyhow..."
label Louisiana04:
play music "v06/swamp.mp3"
scene swamphouse01
show wendy01
with dissolve
if seenwendy == False:
    jump WendyFirstTime
if seenwendy:
    jump WendySecondTime

label WendyFirstTime:
we "Oh, hi there, I remember you... Welcome to Lousiana. Or as it's now called, Lousiane."
mc "What... What are you doing here???"
hide wendy01
show wendy02
with fastdissolve
we "Well, after my detachment got here and claimed Louisiana in the name of France, Captain Micron offered me a piece of land to settle on. So here I am, trying to make a living out of this swampy place!"
mc "And how are you doing that exactly?"
hide wendy02
show wendy03
with fastdissolve
we "I skin gators and make handbags out of them..."
mc "Is there... Anyone else around? I'm supposed to clear this hex. So I can move on to F-range hexes and hopefully get closer to finding Trumpf City."
hide wendy03
show wendy01
with fastdissolve
if diplomaticpass:
    we "Oh, so you still haven't found it? Even with that diplomatic pass I gave you?"
if diplomaticpass == False:
    we "Oh, so you still haven't found it?"
mc "No. Could you help me some more?"
hide wendy01
show wendy04
with fastdissolve
we "I don't know... What's in it for me?..."
mc "Err... What could I do to make it WORTH YOUR WHILE... *wink*"
hide wendy04
show wendy02
with fastdissolve
we "I was thinking... I need an extra pair of hands. You come and work for me and I'll tell you where Trumpf City is on your map. I'll pay you 5 bucks a day for that too."
we "IF you manage to skin a gator that is..."
mc "How often would I have to work?"
we "How about... You kill three gators, so three FULL days at least. Need to stock up on gator skins..."
mc "Is that one or two game periods then?"
hide wendy02
show wendy04
with fastdissolve
we "It's TWO game periods. Come in the morning, leave in the evening. So come alone, without any scouts..."
if mcbike == False:
    mc "But I don't have my own bike, I rely on scouts to take me everywhere on the map!"
    we "What, you STILL don't have your own rig? Man, you're WAY BEHIND. In any case, that's the deal and it ain't changing just cos you're a lousy player."
mc "Do I have to go through these gator-infested swamps EVERY TIME I come here???"
we "I'll fill up that hole in the ground, but I can't do anything about the gators...."
$ seenwendy = True
if period == 1 and alone:
    menu:
        "Well, it's still morning and I came alone so I can stay for a full day, might as well start NOW.":
            jump WendyWork01
        "I could start working NOW but I need to go back to the compound.":
            jump BackHex46
if period == 2:
    mc "Ah, it's too late to start today then... I'll go back tot he compound and come back another time then, Wendy!"
    we "And I'll be right here waiting for you."
    jump BackHex46
if alone == False:
    mc "Ah, I came with a scout and she's waiting for me, need to go, but I'll come back another time then, Wendy!"
    we "And I'll be right here waiting for you."
    jump BackHex46

label WendyWork01:
scene swamphouse01 blurred
show wendy05
with dissolve
play sound "v06/shortlick.mp3"
we "Good. I like a man... who doesn't mind hard labor. And DANGER. I like a man with a name too... What's yours?"
mc "[name]. The hero."
if wendydidwork == False:
    call LustPlusWendy
$ wendydidwork = True
we "I'll change into my bikini, you should get down to your skivvies too, gators can smell dirty clothes."
mc "Ah, right, sure..."
jump WendySecondTimeb

label WendySecondTime:
if gatorwork >= 5:
    we "Ooh, and what do I owe this unexpected visit to?"
    mc "I was thinking about how lonely you must be in this desolate place..."
    hide wendy01
    show wendy04
    with fastdissolve
    we "And you decided to come and alleviate my loneliness with your fat dong, didn't you?"
    mc "Err, yeah, pretty much."
    if lustwe >= 4:
        we "Well, GOOD. Cos I need some DICK, and you've got the BIGGEST monsterdick I've ever seen!"
        jump WendyFuck02
    if lustwe <= 3:
        hide wendy04
        show wendy02
        with fastdissolve
        we "Well, I'm not in the mood. But I am in the mood for SKINNING GATORS!"
        mc "*Ah, I see, lust is not high enough, need to skin a gator to get it back up to at least 4...*"
        jump WendyBikini
we "Ah, good to see you back [name]! Are you ready to catch some gators?"
if wendydidwork == False:
    mc "Sure, that's why I'm here. To skin gators."
    jump WendyWork01
    
label WendyBikini:
mc "Sure, I'll get undressed and wait for you to come back in that sexy bikini..."
hide wendy02
show wendy04
with fastdissolve
we "Oh, I'm flattered!"
if gatorwork == 0:
    jump WendySecondTimeb
scene swamphouse01 blurred
show wendy06
with fade
we "So let's go and skin some gators!"
scene swamps02 with fade
we "Same as last time, I take the gator on the left, you take the one on the right."
mc "Okey-dokey..."
jump GatorFight

label WendySecondTimeb:
scene swamphouse01 blurred
show wendy06
with fade
we "So let's go to WORK! I'm got my machete, I assume you have a decent weapon?"
if dagger:
    mc "Yeah, I have a hunting knife."
    hide wendy06
    show wendy07
    with fastdissolve
    we "Well, that's good, cos you're going to need one, only way to beat gators around here... Let's go!"    
if dagger == False:
    mc "No, I don't have anything..."
    hide wendy06
    show wendy07
    with fastdissolve
    we "I'll lend you a hunting knife then, you'll need one... Only way to beat gators around here... Let's go!"
scene swamps02 with fade
we "I take the gator on the left, you take the one on the right."
mc "Okey-dokey..."

label GatorFight:
hide screen mcstats
hide screen calendar
scene swamps03
show gatormc01 at farleft02
show gator01 at farright
with dissolve
$ mc_health = 2.0
$ gator_health = 2.0
show screen screenfightmcgator
$ gatorfirst = False
if gatorwork == 3:
    mc "This one looks fiercer than the first two..."
    $ gatorfirst = True 
    hide gator01
    show gator02 at farright
    play sound "v06/gator.mp3"
    show gator02 at centerright with move
    mc "Shit, he's attacking me first too, he's damn quick!"
    window hide
    jump RoundGatorFightb

label GatorRound:
if gatorfirst:
    jump RoundGatorFight
if gatorfirst == False:
    jump RoundMCGatorFight

label RoundGatorFight:  
mc "You don't scare me!"
window hide
hide gator01
show gator02 at farright
play sound "v06/gator.mp3"
show gator02 at centerright with move
window hide
label RoundGatorFightb:
call DiceRoll
if (gatorwork == 1 and diceroll >= 5) or (gatorwork == 2 and diceroll >= 4) or (gatorwork ==3 and diceroll >= 4):
    hide gatormc01
    hide gator02
    show gator03 at left
    with fastdissolve
    play sound "v06/gator.mp3"
    $ counting = 0
    while counting < 20:
        $ mc_health -= 0.05
        $ counting += 1
        pause 0.01
    if mc_health >= 0.1:
        mc "Just a scratch. You wait till I SKIN you, damn gator!"
    if mc_health <= 0:
        hide gator03
        show gatormc06 at farleft
        show gator02 at right
        with fastdissolve
        mc "I yield, but get OFF me, you damn lizard, I'm not edible!"
        call MCInjury
        $ mcinjuredgator = True
        jump GatorWinFightEnd        
    hide gator03
    show gatormc01 at farleft02
    show gator01 at farright
    with fastdissolve
else:
    hide gatormc01
    hide gator02
    show gator04 at left
    with fastdissolve
    mc "And just where do you think you're going buddy? Get back to the other side of the screen!"
    hide gator04
    show gatormc01 at farleft02
    show gator01 at farright
    with fastdissolve
$ gatorfirst = False
jump GatorRound

label RoundMCGatorFight:  
mc "Prepare to become a fashion accessory!"
window hide
show gatormc01 at left with move
hide gatormc01
show gatormc02
hide gator01
show gator02 at farright03
with fastdissolve
call DiceRoll
$ dcombatroll=mccombat+diceroll        
if (dcombatroll >= 8 and not diceroll == 1) or diceroll == 6:
    window hide
    hide gatormc02
    hide gator02
    show gatormc03 at right
    with fastdissolve
    play sound "v06/knife.mp3"
    mc "How do you like that, hey?"
    if gator_health >= 0.1:
        play sound "v06/gator.mp3"
    $ counting = 0
    while counting < 20:
        $ gator_health -= 0.05
        $ counting += 1
        pause 0.01
    if gator_health <= 0:
        jump GatorFightWin
    hide gatormc03
    show gatormc01 at farleft02
    show gator01 at farright
    with fastdissolve
if (dcombatroll <= 7 and not diceroll == 6) or diceroll == 1:
    window hide
    hide gatormc02
    hide gator02
    show gatormc04 at right
    with fastdissolve
    play sound "v06/gator.mp3"
    mc "Hey, that's not a fair move!"
    hide gatormc04
    show gatormc01 at farleft02
    show gator01 at farright
    with fastdissolve
$ gatorfirst = True
jump GatorRound   

label GatorFightWin:
hide screen screenfightmcgator
show screen mcstats
show screen calendar
hide gatormc03
show gatormc05
with dissolve
mc "I'm a winner baby!"
$ gatorwon = True

label GatorWinFightEnd:
hide screen screenfightmcgator
show screen mcstats
show screen calendar
stop sound
stop music
$ period += 1
scene swamphouse01 blurred
show wendy06
with fade
we "So, how did it go for you? I got MY gator..."
if gatorwon:
    $ gatorwork += 1
    $ gatorwon = False
    mc "And I got mine!"
    call LustPlusWendy
    hide wendy06
    show wendy07
    with fastdissolve
    if gatorwork >=5 and lustwe >= 4:
        we "Then I guess, it's time for you to..."
        hide wendy07
        show wendy06
        with fastdissolve
        we "...Fuck me with your GIANT COCK!"
        jump WendyFuck02
    if gatorwork >=5 and lustwe <= 3:
        we "Well, that's good but.."
        hide wendy07
        show wendy06
        with fastdissolve
        we "...My lust for you still isn't high enough."
        hide wendy06
        show wendy08
        with fastdissolve
        we "You'll just have to come back and skin some more gators for me if you want a piece of that booty!"
        jump BackHex46
    we "Oh, well done, I underestimated you... Here's your money for the day."
    $ money += 5
    hide wendy07
    show wendy08
    with fastdissolve 
    if gatorwork == 2:
        we "Come back again and get two more gators and I'll make it worth your while EVEN MORE..."
    if gatorwork == 3:
        we "I'm all dirty, I'm going to take a shower. Care to join me?"
        mc "Of course Wendy!"
        jump WendyShower
    if gatorwork == 4:
        mc "Hey, what about showing me where Trumpf City is? I've skinned three gators for you, that was the deal."
        we "Before I show you where Trumpf City is on your map..."
        hide wendy08
        show wendy10
        with fastdissolve
        we "I want you you to FUCK ME with your GIANT teenage cock!"
        mc "Alright! Double-whammy!"
        hide wendy10
        show wendy08
        with fastdissolve
        we "So get undressed and follow me in the shower..."
        jump WendyFuck    
    jump BackHex46
if gatorwon == False:
    mc "Err.. He escaped. But just barely, I almost got him."
    hide wendy06
    show wendy09
    with fastdissolve
    we "And those bite marks, that's just for fun is it? You FAILED miserably and you got yourself injured on top of that!"
    call LustMinusWendy
    we "Just leave. And don't come back until you're ready to SKIN SOME GATORS."
    jump BackHex46

label WendyShower:
stop music
play music "Sounds/shower.mp3"
scene wendyshower01
with fade
we "What are you waiting for [name]?"
scene wendyshower02 with dissolve
mc "I'm right here behind you..."
scene wendyshower03 with dissolve
we "Ooh, and what's that HUGE thing I feel nudging between my ass cheeks?"
mc "That would be my HUGE cock. Still soft but getting hard fast... Cos your body is smoking hot!"
scene wendyshower04 with fastdissolve
we "Oh my, what are we going to do about it? I know. I'll make it go down with my expert hands!"
stop music
scene wendyshower05 with fastdissolve
we "What a MASSIVE fuckstick. I'm gonna have to use BOTH hands on such a MONSTER."

label WendyHandSlow:
play music "Sounds/wank.mp3"
hide wendyhandfast
show wendyhandslow
call screen wendyhandslow01
screen wendyhandslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyHandEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WendyHandFast") 

label WendyHandFast:
we "You like that, don't you? A two-handed jacking of your monster cock... I'll go faster for you..."
hide wendyhandslow
show wendyhandfast
call screen wendyhandfast01
screen wendyhandfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyHandEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WendyHandSlow") 

label WendyHandEnd:
mc "Aah, gonna cum Wendy!"
we "Give me a CUM SHOWER, please!"
stop music
scene wendyhandcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "There you goooo! RHAAA!"
scene wendyhandcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
we "Yes, aim it at my tits, COVER THEM WITH YOUR CREAM!"
scene wendyhandcum02 with fastflash
mc "AAAH, can't stop CUMMMMMIINNNGGG!"
scene wendyhandcum03 with dissolve
stop sound
we "Oh my God, look at HOW MUCH you came! There's TONS of it. I'm gonna have to take ANOTHER shower..."
mc "Phew! And I need to go back to my compound, they'll be asking too many questions otherwise..."
we "Don't forget to COME BACK and get a even BETTER reward, [name]!"
mc "Sure will do, Wendy."
jump BackHex46

label WendyFuck:
stop music
$ knowcity = True
play music "Sounds/shower.mp3"
scene wendyshower01
with fade
we "Come over here [name]. You and your HUGE COCK!"
scene wendyshower02 with dissolve
mc "I'm right here behind you..."
we "Now that I've seen how GIGANTIC and POWERFUL that fuckpole of yours is, I want to FEEL it INSIDE ME!"
mc "And I'm ROCK-HARD and READY for that!"
scene wendyshower04 with dissolve
we "Indeed you are... Let me turn the shower off and suck on that FAT DONG!"
stop music
scene wendyshower05 with dissolve
we "Are you ready, big boy?"
mc "Fuck yeah!"

label WendyBlowSlow:
play channel1 "Sounds/hardsucking.mp3"
play channel2 "Sounds/boymoan02.mp3"
hide wendyblowfast
show wendyblowslow
call screen wendyblowslow01
screen wendyblowslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WendyBlowFast") 

label WendyBlowFast:
mc "Get ready, I'm going to fuck your mouth faster!"
hide wendyblowslow
show wendyblowfast
call screen wendyblowfast01
screen wendyblowfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WendyBlowSlow") 

label WendyBlowEnd:
mc "AAh, gonna blow down your throat, Wendy!"
stop channel1
stop channel2
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene wendyblowcum01 with dissolve
mc "Oh God, that's it, right down your THROAT! AAAH!"
scene wendyblowcum02 with dissolve
play music "Sounds/splooge02.mp3"
mc "Here, let me help you!"
scene wendyblowcum02 with fastflash
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Ssssooo, so GOOD! RHAAA!"
stop music
scene wendyblowcum03 with dissolve
we "You FILLED my stomach UP! I can feel your dirty spunk sloshing inside me... There's... too much of it!"
mc "Come on now, just swallow like a good girl, this is unbecoming..."
scene wendyblowcum04 with dissolve
we "Alrigh,t I'm feeling better now..."
mc "Good, cos we haven't fucked yet and I'm still ROCK-HARD!"
we "Pound me from behind with that giant log!"
    
label WendyFuckSlow:
play music "Sounds/fucksound.mp3"
hide wendyfuckfast
show wendyfuckslow
call screen wendyfuckslow01
screen wendyfuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WendyFuckFast") 

label WendyFuckFast:
mc "Fuck, that pussy is sssoo nice, I'm just gonna have to pound it faster!"
we "Yes, do it, STUD!"
hide wendyfuckslow
show wendyfuckfast
call screen wendyfuckfast01
screen wendyfuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WendyFuckSlow") 

label WendyFuckEnd:    
we "Oh God, I'm cumming again, you're fucking me so goooood!"
mc "And I'm about to..."
scene wendyfuckcum01 with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "...blow too! RHAAA!"
we "My pussy is being filled to the brim with your cream! AAAH!"
scene wendyfuckcum01 with fastflash
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "God, can't stop cumming!"
scene wendyfuckcum02 with dissolve
stop sound
we "I see you've made a big mess all over my back, you naughty boy... I'm going to have to take yet ANOTHER shower!"
scene wendyfuckcum03 with dissolve
mc "No time for that. I'm still hard and I want to fuck that lovely ASS of yours!"
we "What? You're gonna fuck me some more after you just dumped TWO HUGE LOADS all over me???"
mc "Your hot bod is making me THAT horny!"

label WendyAnalSlow:
play music "Sounds/fucksound.mp3"
hide wendyanalfast
show wendyanalslow
call screen wendyanalslow01
screen wendyanalslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WendyAnalFast") 

label WendyAnalFast:
we "I love feeling your giant log in my ass while I'm dripping with your load, it's so hot, but please FUCK ME FASTER!"
hide wendyanalslow
show wendyanalfast
call screen wendyanalfast01
screen wendyanalfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WendyAnalSlow") 

label WendyAnalEnd:
we "Oh God, I'm cumming again, you're fucking me so goooood!"
mc "And I'm about to..."
scene wendyanalcum01 with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "...blow too! RHAAA!"
we "My ass is being filled to the brim with your cream! AAAH!"
scene wendyanalcum01 with fastflash
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "God, can't stop cumming!"
scene wendyanalcum02 with dissolve
play sound "Sounds/splooge01.mp3"
we "AAAH, you're so DEEP in my ass!"
scene wendyanalcum02 with fastflash
mc "A few... more... shots, AAAAh!"
we "I can't take it anymore, my legs are failing me..."
scene wendyanalcum03 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
we "You're STILL hosing me down? My ass... It's leaking your cream like a faucet... I've never been... fucked so HARD in my life!"
scene wendyanalcum04 with dissolve
stop sound
mc "Phew, I think you've drained me for good this time."
we "Let me recover... And meet me at the wooden dock."
scene swamphouse01 blurred
show wendy11
with fade
we "I'm gonna have to take ANOTHER shower now, you've COVERED me in your yummy cum!"
mc "About that promise of yours..."
we "OK, show me your map and I'll tell you where Trumpf City is, I THINK..."
hide wendy11
show wendy12
with dissolve
we "Mmmh, I would say... Hex G3. Yep, definitely, that one."
window hide
show knowledgecity at posmission
$ renpy.pause(1.0, hard=True)
pause
hide knowledgecity
mc "Thanks for the IMPORTANT tip, Wendy!"
hide wendy12
show wendy11
with dissolve
we "You're welcome, come back ANYTIME you want, STUD..."
jump BackHex46b

label WendyFuck02:
stop music
play music "Sounds/shower.mp3"
scene wendyshower01
with fade
we "What are you waiting for [name]?"
scene wendyshower02 with dissolve
mc "I'm right here behind you..."
scene wendyshower03 with dissolve
we "Ooh, and what's that HUGE thing I feel nudging between my ass cheeks?"
mc "That would be my HUGE cock. Still soft but getting hard fast... Cos your body is smoking hot!"
scene wendyshower04 with fastdissolve
we "Oh my, what are we going to do about it? I know. I'll make it go down with my expert hands!"
stop music
scene wendyshower05 with fastdissolve
we "What a MASSIVE fuckstick. I'm gonna have to use BOTH hands on such a MONSTER."

label WendyHandSlowb:
play music "Sounds/wank.mp3"
hide wendyhandfast
show wendyhandslow
call screen wendyhandslow01b
screen wendyhandslow01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyHandEndb")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WendyHandFastb") 

label WendyHandFastb:
we "You like that, don't you? A two-handed jacking of your monster cock... I'll go faster for you..."
hide wendyhandslow
show wendyhandfast
call screen wendyhandfast01b
screen wendyhandfast01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyHandEndb")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WendyHandSlowb") 

label WendyHandEndb:
mc "Aah, gonna cum Wendy!"
we "Give me a CUM SHOWER, please!"
stop music
scene wendyhandcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "There you goooo! RHAAA!"
scene wendyhandcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
we "Yes, aim it at my tits, COVER THEM WITH YOUR CREAM!"
scene wendyhandcum02 with fastflash
mc "AAAH, can't stop CUMMMMMIINNNGGG!"
scene wendyhandcum03 with dissolve
stop sound
we "Oh my God, look at HOW MUCH you came! There's TONS of it. I'm gonna have to take ANOTHER shower..."
play music "Sounds/shower.mp3"

scene wendyshower02 with dissolve
we "What? You're hard again already???"
mc "Of course Wendy, standing next to your hot bod just drives me crazy!"
scene wendyshower04 with dissolve
we "Mmh, I just need to feel this POWERFUL log again then! This time with my mouth!"
stop music
scene wendyshower05 with dissolve
we "Are you ready, big boy?"
mc "Fuck yeah!"

label WendyBlowSlowb:
play channel1 "Sounds/hardsucking.mp3"
play channel2 "Sounds/boymoan02.mp3"
hide wendyblowfast
show wendyblowslow
call screen wendyblowslow01b
screen wendyblowslow01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyBlowEndb")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WendyBlowFastb") 

label WendyBlowFastb:
mc "Get ready, I'm going to fuck your mouth faster!"
hide wendyblowslow
show wendyblowfast
call screen wendyblowfast01b
screen wendyblowfast01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyBlowEndb")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WendyBlowSlowb") 

label WendyBlowEndb:
mc "AAh, gonna blow down your throat, Wendy!"
stop channel1
stop channel2
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene wendyblowcum01 with dissolve
mc "Oh God, that's it, right down your THROAT! AAAH!"
scene wendyblowcum02 with dissolve
play music "Sounds/splooge02.mp3"
mc "Here, let me help you!"
scene wendyblowcum02 with fastflash
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Ssssooo, so GOOD! RHAAA!"
stop music
scene wendyblowcum03 with dissolve
we "You FILLED my stomach UP! I can feel your dirty spunk sloshing inside me... There's... too much of it!"
mc "Come on now, just swallow like a good girl, this is unbecoming..."
scene wendyblowcum04 with dissolve
we "Alrigh,t I'm feeling better now..."
mc "Good, cos we haven't fucked yet and I'm still ROCK-HARD!"
we "Pound me from behind with that giant log!"
    
label WendyFuckSlowb:
play music "Sounds/fucksound.mp3"
hide wendyfuckfast
show wendyfuckslow
call screen wendyfuckslow01b
screen wendyfuckslow01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyFuckEndb")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WendyFuckFastb") 

label WendyFuckFastb:
mc "Fuck, that pussy is sssoo nice, I'm just gonna have to pound it faster!"
we "Yes, do it, STUD!"
hide wendyfuckslow
show wendyfuckfast
call screen wendyfuckfast01b
screen wendyfuckfast01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyFuckEndb")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WendyFuckSlowb") 

label WendyFuckEndb:    
we "Oh God, I'm cumming again, you're fucking me so goooood!"
mc "And I'm about to..."
scene wendyfuckcum01 with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "...blow too! RHAAA!"
we "My pussy is being filled to the brim with your cream! AAAH!"
scene wendyfuckcum01 with fastflash
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "God, can't stop cumming!"
scene wendyfuckcum02 with dissolve
stop sound
we "I see you've made a big mess all over my back, you naughty boy... I'm going to have to take yet ANOTHER shower!"
scene wendyfuckcum03 with dissolve
mc "No time for that. I'm still hard and I want to fuck that lovely ASS of yours!"
we "What? You're gonna fuck me some more after you just dumped TWO HUGE LOADS all over me???"
mc "Your hot bod is making me THAT horny!"

label WendyAnalSlowb:
play music "Sounds/fucksound.mp3"
hide wendyanalfast
show wendyanalslow
call screen wendyanalslow01b
screen wendyanalslow01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyAnalEndb")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WendyAnalFastb") 

label WendyAnalFastb:
we "I love feeling your giant log in my ass while I'm dripping with your load, it's so hot, but please FUCK ME FASTER!"
hide wendyanalslow
show wendyanalfast
call screen wendyanalfast01b
screen wendyanalfast01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyAnalEndb")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WendyAnalSlowb") 

label WendyAnalEndb:
we "Oh God, I'm cumming again, you're fucking me so goooood!"
mc "And I'm about to..."
scene wendyanalcum01 with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "...blow too! RHAAA!"
we "My pussy is being filled to the brim with your cream! AAAH!"
scene wendyanalcum01 with fastflash
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "God, can't stop cumming!"
scene wendyanalcum02 with dissolve
play sound "Sounds/splooge01.mp3"
we "AAAH, you're so DEEP in my ass!"
scene wendyanalcum02 with fastflash
mc "A few... more... shots, AAAAh!"
we "I can't take it anymore, my legs are failing me..."
scene wendyanalcum03 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
we "You're STILL hosing me down? My ass... It's leaking your cream like a faucet... I've never been... fucked so HARD in my life!"
scene wendyanalcum04 with dissolve
stop sound
mc "Phew, I think you've drained me for good this time."
we "Let me recover... And meet me at the wooden dock."
scene swamphouse01 blurred
show wendy11
with fade
we "I'm gonna have to take ANOTHER shower now, you've COVERED me in your yummy cum!"
mc "My pleasure. Hopefully, we'll meet again Wendy!"
jump BackHex46b

label BackHex46:
if withbe:
    scene swamps01
    show bellaout03
    with fade
    be "So, did you find anything interesting in that place?"
    if seenwendy == False:
        mc "No, it's too dangerous in there. Full of nasty alligators."
        if mcinjured:
            hide bellaout03
            show bellaoutworry
            with fastdissolve
            be "I can see that, you've got bite marks all over yourself. We should head back to the compound so you can get proper medical treatment."
            jump BackHex46b
        be "Then let's head back to the compound, it's getting late."
        jump BackHex46b
    if seenwendy:
        mc "Yeah, I met some woman who knows where Trumpf City is."
        be "And? Where is it?"
        mc "She won't tell me until I work for her and skin enough gators for her handbag business."
        hide bellaout03
        show bellaoutworry
        with fastdissolve
        be "Umpf... I think she's abusing you... Let's go back to the compound."
        jump BackHex46b

if withpe:
    scene swamps01
    show pennyout03
    with fade
    pe "So, did you find anything interesting in that place?"
    if seenwendy == False:
        mc "No, it's too dangerous in there. Full of nasty alligators."
        if mcinjured:
            hide pennyout03
            show pennyout01
            with fastdissolve
            pe "I can see that, you've got bite marks all over yourself. We should head back to the compound so you can get proper medical treatment."
            jump BackHex46b
        pe "Then let's head back to the compound, it's getting late."
        jump BackHex46b
    if seenwendy:
        mc "Yeah, I met some woman who knows where Trumpf City is."
        pe "And? Where is it?"
        mc "She won't tell me until I work for her and skin enough gators for her handbag business."
        hide pennyout03
        show pennyout01
        with fastdissolve
        pe "Umpf... I think she's abusing you... Let's go back to the compound."

label BackHex46b:
stop music
$ period += 1
scene command01
show lena01
with fade
if wendytold02:
    le "So, you're back from that hex with no use to me anymore whatsoever I see..."
    mc "Just needed to drop by and say hi to an old friend."
    hide lena01
    show lena10
    with fastdissolve
    le "Which is a TOTAL WASTE OF TIME! You are dismissed."
    if mcinjured: 
        le "And get those bite marks sorted out with nurse Rachel, you look terrible."
        mc "Sure thing, Chief Lena!"
        jump Medbay
    hide lena10 with fastdissolve
    jump LeaveCommand
if wendytold:
    le "So, do you have the location for Trumpf City now?"
    if knowcity == False:
        mc "Not yet. Still have to skin some more gators..."
        hide lena01
        show lena10
        with fastdissolve
        le "Well, hurry up! DISMISSED!"
        if mcinjured: 
            le "And get those bite marks sorted out with nurse Rachel, you look terrible."
            mc "Sure thing, Chief Lena!"
            jump Medbay        
    if knowcity:
        $ wendytold02 = True
        mc "Yep, Chief! It's hex G3. Supposedly."
        hide lena01
        show lena07
        with fastdissolve
        le "I knew it! If I could have picked an hex, I would have picked that one!"
        mc "Apparently, so did the dev."
        hide lena07
        show lenapensive
        with fastdissolve        
        le "I will update the map immediately. But we should still proceed with caution and not go straight there without first exploring the rest of the map."
        mc "Sure Chief!"
        le "You are dismissed."
        hide lenapensive with dissolve
        jump LeaveCommand
if alone == False:
    le "So, what do you have to report about area E6, scouts?"
if alone:
    le "So, what do you have to report about area E6, [name]?"
if seenwendy:
    $ wendytold = True
    mc "A potential future possibility for acquiring knowledge of the location of Trumpf City, Chief!"
    hide lena01
    show lena03
    with fastdissolve
    le "Really? That would be quite valuable indeed..."
    mc "Indeed it would."
    hide lena03
    show lenapensive
    with fastdissolve
    le "You MUST find out where it is, this is your MISSION! And the aim of the game incidentally."
    if mcinjured: 
        le "You are dismissed. And get those bite marks sorted out with nurse Rachel, you look terrible."
        mc "Sure thing, Chief Lena!"
        jump Medbay
    le "You are dismissed!"
    hide lenapensive with dissolve
    jump LeaveCommand

jump LeaveCommand

label ExploreHex41:
$ exploredhex41 = True
scene ambush01 with fade
play music "Sounds/desertwind01.mp3"
if withpe:
    play sound "Sounds/explorepenny02.mp3"
    pe "I don't like this place, it looks like the perfect spot for a Road Warriors ambush..."
    mc "Well, there's nowhere else to go but forward, so let's move through this place quickly then!"
    scene ambush02penny with dissolve
if withbe:
    play sound "Sounds/explorebella02.mp3"
    be "Something doesn't feel right. Like I lost my connection with the Phallus Lord."
    mc "Well, there's nowhere else to go but forward, so let's move through this place quickly then!"
    scene ambush02bella with dissolve
if alone:
    play sound "Sounds/explorepenny02.mp3"
    mc "Looks like some kind of canyon down there. I guess there's nowhere else to go but FORWARD!"
    scene ambush02alone with dissolve
mc "Looks fine and quiet to m..."
play sound "Sounds/intromusic.mp3"
scene ambushwarrior01 with dissolve:
    xpos 0.0
    linear 5.0 xpos -0.5
mc "Ah shit, it was an ambush after all..."
stop sound
scene ambushwarrior02 with dissolve
wa "It's over travellers, we have the high ground."
mc "You underestimate my power!"
if withpe:
    pe "Don't listen to him, we yield. I'm a Road Warrior, so let me go and take him."
    mc "Hey! What the fuck, Penny?"
    pe "Sorry [name], but this is the only way I can escape with my rig. I'll try and find you again..."
    scene ambushwarrior03 with fastdissolve
    wa "Come with us young man, Chief Diamond is waiting for you..."
if withbe:
    be "The Phallus Lord has even HIGHER ground! So yield, mere mortals, you cannot f..."
    play sound "Sounds/taser.mp3"
    scene ambushwarrior02 with hpunch
    $ renpy.pause(2.0, hard=True)
    be "Ouch!"
    mc "Fuck, they tasered us! No, you didn't understimate my power, I'm the one who totally overestimated it!"
    call MCInjury   
    $ mcinjuredtaser = True    
    scene ambushwarrior03 with fastdissolve
    if withnone:
        wa "Now come with us young man, Chief Diamond is waiting for you... Leave the woman and her rig behind, we have no use for them."
    if withnone == False:
        wa "Now come with us young man, Chief Diamond is waiting for you... Leave the others and the rig behind, we have no use for them."
if alone and withnone:
    scene ambushwarrior03 with fastdissolve    
    wa "WRONG answer! Take him and the bike. And gag him, I don't want to hear a word from this wannabe Road warrior lowlife!"
if alone and withnone == False:
    scene ambushwarrior03 with fastdissolve    
    wa "WRONG answer! Take him and the bike, and let the girl go. We have no use for her."
    if withan:
        mc "Use this beacon Angie, and wait for Penny or Bella to pick you up..."
        an "I'm scared [name]! You were supposed to PROTECT me!"
        call LustMinusAngie
    if witham:
        mc "Use this beacon Amy, and wait for Penny or Bella to pick you up..."
        am "Mother Nature will provide me until someone arrives, I am confident."
    if withcl:
        mc "Use this beacon Clara, and wait for Penny or Bella to pick you up..."
        cl "The Phallus Lord will guide them to me if I pray hard enough!"
    if withla:
        mc "Use this beacon Laurie, and wait for Penny or Bella to pick you up..."
        la "Mother Nature will provide me until someone arrives, I am confident."
    if withma:
        mc "Use this beacon Marnie, and wait for Penny or Bella to pick you up..."
        ma "Be careful [name], thse Road Warriors are from a particularly NASTY subfaction. Involved in all kinds of filthy sex trades."
        mc "I see. Well, that doesn't sound so bad..."
    if withmi:
        mc "Use this beacon Michiko, and wait for Penny or Bella to pick you up..."
        mi "Too bad they have the high ground or I'd kick them unconscious easily!"
    if withmo:
        mc "Use this beacon Nancy, and wait for Penny or Bella to pick you up..."
        mo "Be careful sweetie, I recognize their tattoo, they are the ones who KIDNAPPED me and tried to sell me as a sex slave!"
    if withsu:
        mc "Use this beacon Suki, and wait for Penny or Bella to pick you up..."
        su "I'm aware of that, I'm the one who designed the beacon... Hoping no one would ever have to use it... *sigh*"
    if withru:
        mc "Use this beacon Ruby, and wait for Penny or Bella to pick you up..."
        ru "I'd be fighting them if they weren't Road Warriors, you know? Good luck to you [name], they can be quite nasty..."
    if withza:
        mc "Use this beacon Zara, and wait for Penny or Bella to pick you up..."
        za "Don't worry about me, I'll be fine, I know how to survive in the desert."
    if withcy:
        cy "And I have no use for you, humans. My motherboard will guide me back home."
        mc "Warn the others, I don't know where they are taking me."
    if withgw:
        mc "Use this beacon Gwen, and wait for Penny or Bella to pick you up..."
        gw "I should have stayed in the lab. Even that is SAFER than travelling with YOU. Umpf."
        call LustMinusGwen
    if withay:
        mc "Use this beacon Ayla, and wait for Penny or Bella to pick you up..."
        ay "So I'm gonna be stuck in this BORING place for hours? This is just SSSOOO BORING!"
        call LustMinusAyla
    if withba:
        mc "Use this beacon Barbara, and wait for Penny or Bella to pick you up..."
        ba "Oh dear me, I might be late for my next school lesson..."
    if withde:
        mc "Use this beacon Debra, and wait for Penny or Bella to pick you up..."
        de "I know how it works, I'm the one who designed it!"
    wa "Now come with us young man, Chief Diamond is waiting for you... And gag him, I don't want to hear a word from this wannabe Road warrior lowlife!"
jump DiamondHarem
    
label DiamondHarem:
$ period += 1
$ warriorcapture = True
stop music
scene diamondharem01b
show warriorchief01
with fade
play music "v07/diamondmusic.mp3"
if alone:
    $ mcbikestolen = True
di "Ah, there you are. It took a while for my Warriors to find you."
mc "What is this place?"
hide warriorchief01
show warriorchief03
with fastdissolve
di "This is in MY harem, hex E3, where you are at MY mercy."
window hide
show knowledgeharem at posmission
$ renpy.pause(1.0, hard=True)
pause
hide knowledgeharem
if renpy.seen_image("strippershow01"):
    mc "What do you want from me? By the way, is that Suk-Yu over there? And who's the other big-titted chick? She looks hot."
if renpy.seen_image("strippershow01") == False:
    mc "What do you want from me? And who are these two big-bosomed beauties behind you?"
hide warriorchief03
show warriorchief02
with fastdissolve
di "They're MY harem girls, and they will NEVER be yours, you hear me?"
if mcinjured == False:
    di "Taser him Bob to show him what I mean..."
    bo "Yes boss."
    mc "Hey! Wh...."
    play sound "Sounds/taser.mp3"
    scene diamondharemtaser with hpunch
    $ renpy.pause(2.0, hard=True)
    mc "Fuck! That hurt like hell!"
    call MCInjury   
    $ mcinjuredtaser = True
    scene diamondharem01b
    show warriorchief01
    with fastdissolve
    di "Now you understand who's the BOSS here, correct?"
    mc "Yes... Correct."
    hide warriorchief01
    show warriorchief02
hide warriorchief02
show warriorchief03
with fastdissolve
if renpy.seen_image("strippershow01"):
    di "However, as it turns out, I did bring you here because of them. And because I saw your \"performance\" with Suk-Yu at the stripclub in Desert Town... "
if renpy.seen_image("strippershow01") == False:
    di "However, as it turns out, I did bring you here because I heard about you... And your ALPHA-cock."
hide warriorchief03
show warriorchief04
with fastdissolve
if renpy.seen_image("strippershow01"):
    di "You seem to be the ideal person to help me decide whether to keep her as my feature stripper or... replace her with Heather over there."
if renpy.seen_image("strippershow01") == False:
    di "You seem to be the ideal person to help me decide whether to keep Suk-Yu as my feature stripper or... replace her with Heather over there."
hide warriorchief04
show warriorchief02
with fastdissolve
di "So go and meet them both, they know why you're here..."
$ methe = True
scene haremsukyu01 with dissolve
if renpy.seen_image("strippershow01"):
    mc "*Oh yeah, I remember that big-titted Asian stripper...*"
if renpy.seen_image("strippershow01") == False:
    mc "*Fuck yeah, damn those titties are HUGE!...*"

scene haremsukyu02 with dissolve
if renpy.seen_image("strippershow01"):
    sy "Well, hello [name], fancy meeting YOU here..."
    mc "I'm always where the HOT action is!"
if renpy.seen_image("strippershow01") == False:
    sy "Well, hello there, we haven't had the PLEASURE to meet yet..."
    mc "The pleasure is all mine at the moment..."
scene haremsukyu03 with dissolve
if renpy.seen_image("strippershow15"):
    sy "My pussy is still tingly from the feeling of your MASSIVE teenage fucktool plowing through it..."
    mc "And I'm getting hard remembering how great your DEEP Asian pussy felt impaled on my giant shaft!"
if renpy.seen_image("strippershow15") == False:
    sy "By the looks of that BULGE on you, you could easily fill up my very DEEP Asian pussy... What do you think?"
    mc "Oh yeah, I'm sure I could. I'd hit the back of your womb with my GIANT teenage cock for sure!"
scene haremsukyu04 with dissolve
if renpy.seen_image("strippershow15"):
    sy "Oh, you're watching my tits, aren't you? I never got to WRAP them around your rockhard shaft... I think you would enjoy that A LOT, wouldn't you?"
if renpy.seen_image("strippershow15") == False:
    sy "Oh, you're watching my tits, aren't you? Can you imagine how good they'd feel WRAPPED around your MONSTER shaft... I think you would enjoy that A LOT, wouldn't you?"
mc "Damn, you're getting me ROCKHARD Suk-Yu!"
di "Now move on and check out Heather, my new recruit..."

scene haremheather01 with dissolve
mc "*Well, what do we have here?... That's a DDD-cup AT LEAST!"
scene haremheather02 with dissolve
he "Chief Diamond told me about you... How you like girls with HUGE bazongas... Because you have such a HUMONGOUS lovepole. Is that true?"
mc "She's damn right, BIGGEST ROD in the country!"
scene haremheather03 with dissolve
he "And I have the biggest JUGGS you'll ever encounter... Imagine how BLISSFUL your shaft would feel lodged between these two puppies?"
mc "Fuck yeah!"
scene haremheather04 with dissolve
he "That much titflesh rubbing against your sensitive veins as your cock gets harder than a bar of steel, ready to EXPLODE all over them!"
mc "Oh damn, my cock is trying to pierce a hole through my pants right now, if you'll excuse me young lady..."

scene diamondharem01b
show diamond01
with dissolve
mc "Errr, you're naked too? Wow, this harem is PARADISE!"
di "You won't be fucking me if that's what you were thinking!"
hide diamond01
show diamond02
with fastdissolve
di "But I'll be having FUN with my two harem girls on the other hand!"
hide diamond02
show diamond03
with fastdissolve
mc "What the fuck? You're a FUTA???"
di "You don't get to rise to my position as Chief of the Road Warriors without some MANLY equipment!"
mc "You're... You're going to fuck me with this, is that what this is all about you sick PERVERT?"
di "Don't FLATTER yourself, you're just a piece of meat to me! And I ain't attracted to MEN."
hide diamond03
show diamond04
with fastdissolve
di "What I want you to do for me is to be a test suject. A customer waiting to be so entirely and completely satisfied that he will fork out heavy tips and come back for more."
mc "Alright! I like that! Way more than getting fucked up the ass by your futa dick!"
di "The future of these girls depends on the wisdom of your judgment."
mc "I am wise beyond my age, trust me, everybody says so!"
di "We'll start with a cock-licking session. Get naked and get hard [name], and girls, get on either side of his pillar!"

stop music
hide screen injury
hide screen mcstats
hide screen calendar
scene diamondlickbackground
show diamondprelick01 with dissolve
he "It's so big mister! I've never seen such a MOUTHFUL!"
sy "He's actually bigger than my King Dong dildo, which I use for one of MY main attractions as the FEATURE STRIPPER OF THE BLUE OYSTER!"
di "Stop talking and start LICKING!"
hide diamondprelick01
show diamondlick00
with dissolve
mc "Oh God, this is going to be GOOD!"
hide diamondlick00
play channel1 "Sounds/lick.mp3"
play channel2 "v07/lick02.ogg"
label DiamondLickSlow:
hide diamondlickfast
show diamondlickslow
call screen diamondlickslow01
screen diamondlickslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DiamondLickEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DiamondLickFast") 

label DiamondLickFast:
di "Go on girls, show him what you're capable of doing... I want the customer to cum UNDER 2 minutes max!"
hide diamondlickslow
show diamondlickfast
call screen diamondlickfast01
screen diamondlickfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DiamondLickEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DiamondLickSlow") 

label DiamondLickEnd:
di "That's it, he's ready to BURST. I can see his veins throbbing and his cumslit expanding!"
hide diamondlickslow
hide diamondlickfast
show diamondlickcum01
with dissolve
stop channel1
stop channel2
mc "Fuck, AAAAH!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
he "Oh my God, I've never seen such a MASSIVE jet of boyspunk!"
with fastflash
sy "He's cumming like a STALLION!"
hide diamondlickcum01
show diamondlickcum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
he "It's flying so HIGH up in the air, you're going to get plastered with the stuff, boss!"
with fastflash
di "Don't worry about me, keep holding his shaft and let it FLY!"
hide diamondlickcum02
show diamondlickcum03
with fastdissolve
di "Nice one girls, that was WELL UNDER two minutes..."
mc "I... I fell drained. And I need to go back to the compound, it(s getting late already. So I will bid you g..."
di "Where do you think you're going?"
hide diamondlickcum03
show diamondpretit01
with dissolve
di "Your cock is still in functioning order.  And we're FAR from over!"
mc "Oh, dear Lord, I'm going to be la..."
hide diamondpretit01
show diamondtit00
with dissolve
he "We're ready whenever you say so, Chief Diamond..."
di "Good, and I'll massage his balls with my feet while you girls rub those huge shaft-pleasing tits all over his throbbing manhood."
sy "Ready to cover our boobs in a GIANT boyload [name]?"
he "I want AT LEAST an inch-thick layer of your splooge all over my ENORMOUS bosom!"
scene diamondlickbackground blurred
play channel1 "v07/twogirls.mp3"
play channel2 "Sounds/wank.mp3"
hide diamondtit00
label DiamondTitSlow:
hide diamondtitfast
show diamondtitslow
call screen diamondtitslow01
screen diamondtitslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DiamondTitEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DiamondTitFast") 

label DiamondTitFast:
di "Keep going girls, rub that titflesh against his shaft even FASTER and make him ERUPT!"
hide diamondtitslow
show diamondtitfast
call screen diamondtitfast01
screen diamondtitfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DiamondTitEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DiamondTitSlow") 

label DiamondTitEnd:
hide diamondtitslow
hide diamondtitfast
show diamondtitcum01
with dissolve
stop channel2
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH, those monster tits are making me CUM!"
with fastflash
di "Keep rubbing his shaft and DRAIN HIM, girls!"
scene diamondtitcumbackground blurred
show diamondtitcum02
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
with dissolve
he "Mmmh, look at how HIGH his cumshots are going!"
with fastflash
sy "He's PLASTERING us with his young boycream, it's ALL OVER THE PLACE!"
hide diamondtitcum02
show diamondtitcum03
with dissolve
stop sound
stop channel1
di "That was a nice BIG load you gave us there... But some of our customers want MORE than a titfuck. So let's move on to the MAIN COURSES!"
he "Please, can I go first, boss? I've been stretching my pussy and I'm sure I can take it and bring him over the edge in less than two minutes!"
if renpy.seen_image("strippershow15"):
    sy "I did that when he visited me in Desert Town in a minute flat!"
if renpy.seen_image("strippershow15") == False:
    sy "My more experienced pussy is what this boy needs to make him cum HARDER THAN EVER BEFORE!"
di "Don't worry girls, you'll both have your turn. But Heather will go first and you will show me your handjob skills..."
sy "Sure thing Chief Diamond!"
scene heathercumbackground03
show heatherprefuck01
with dissolve
he "See that nice, tight, young pussy [name]? It's all yours. RAM your dick in there and feel my warmth engulf your shaft until you can't stop cumming!"
scene heathercumbackground03
show heatherprefuck02
with dissolve
mc "Oh God... Yes, I will do it!"
he "It will make you spew your sauce in no time!"
play music "v07/heatherfuck.mp3"
label HeatherFuckSlow:
scene heatherfuckbackground
show heatherfuckslow
call screen heatherfuckslow01
screen heatherfuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HeatherFuckEndA")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("HeatherFuckFast") 
    imagebutton:
        focus_mask True
        idle "v07/sukyuview.png"
        hover "v07/sukyuview.png"
        action Jump ("DiamondSukYuSlow") 

label DiamondSukYuSlow:
play sound "Sounds/zarahandjob.mp3"
scene diamondsukyubackground01 blurred
show diamondsukyuslow
call screen diamondsukyuslow01
screen diamondsukyuslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HeatherFuckEndB")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DiamondSukYuFast") 
    imagebutton:
        focus_mask True
        idle "v07/heatherview.png"
        hover "v07/heatherview.png"
        action Jump ("HeatherFuckSlow") 

label HeatherFuckFast:
scene heatherfuckbackground
show heatherfuckfast
call screen heatherfuckfast01
screen heatherfuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HeatherFuckEndA")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("HeatherFuckSlow") 
    imagebutton:
        focus_mask True
        idle "v07/sukyuview.png"
        hover "v07/sukyuview.png"
        action Jump ("DiamondSukYuFast") 

label DiamondSukYuFast:
play sound "Sounds/zarahandjob.mp3"
scene diamondsukyubackground01 blurred
show diamondsukyufast
call screen diamondsukyufast01
screen diamondsukyufast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HeatherFuckEndB")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("DiamondSukYuSlow") 
    imagebutton:
        focus_mask True
        idle "v07/heatherview.png"
        hover "v07/heatherview.png"
        action Jump ("HeatherFuckFast") 
            
label HeatherFuckEndA:
$ heathercuma = True
he "Come on STUD, I want to feel your POWERFUL shots BLASTING away inside my womb! Do it!"
mc "Hang on, I'm getting close..."
scene heathercumbackground01 blurred
show heatherfuckcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
stop music
play music "v07/heathercumming.mp3"
mc "RHAAA, that's IT! Your pussy is making me ERUPT!"
scene heathercumbackground02 blurred
show heatherfuckcum02
with dissolve
he "I'm cumming too, this is soo good!"
with fastflash
he "Douse my HUGE TITS with the rest of your GIGANTIC load please!"
scene heathercumbackground03 blurred
show heatherfuckcum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "You asked for it, RHAAA!"
with fastflash
he "Oh, I LOVE IT! MORE, MORE!"
stop music
if heathercumb:
    jump DiamondSessionNext
play sound "Sounds/zarahandjob.mp3"
scene diamondsukyubackground01 blurred
show diamondsukyuslow 
with dissolve
label HeatherFuckEndB:
$ heathercumb = True
sy "Boss, I can feel your cock TREMBLING, are you ready to COVER ME in your futa-cum?"
di "Just keep pumping away Suk-Yu...and I'll..."
scene diamondsukyubackground01
show diamondsukyucum01
with dissolve
stop music
play sound "Sounds/moaning02.mp3"
di "....CUM!"
with fastflash
sy "Oh boss, you had sssoo much futa-sperm left for me in your balls... Let me massage them for you..."
hide diamondsukyucum01
show diamondsukyucum02
with fastdissolve
di "Wh.. What are you doing? OOOOH, I'm cumming even MORE!"
sy "It's my special new technique to DRAIN customers, boss! You like it?"
with fastflash
di "Y...Yeah, AAAHHH!"
scene diamondlickbackground blurred
show diamondsukyucum03
with dissolve
play sound "Sounds/lick.mp3"
sy "Mmmmh, it's... delicious, boss!"
if heathercuma:
    jump DiamondSessionNext
if heathercuma == False:
    play music "v07/heatherfuck.mp3"
    scene heatherfuckbackground
    show heatherfuckslow
    with dissolve
    jump HeatherFuckEndA

label DiamondSessionNext:
stop music
stop sound
scene diamondhighbackground blurred
show diamondhigh01
with dissolve
di "OK, time to switch partners. You take Suk-Yu and I'm gonna bang Heather's sweet pussy..."
he "Oooh, I can't wait boss!"
sy "And I can't wait to get STRETCHED by [name]'s MONSTERCOCK!"
scene heathercumbackground01
show sukyuprefuck01
with fade
sy "You're going to fuck me HARD [name]? I LOVE it DEEP and POWERFUL!"
play sound "Sounds/moaning.mp3"
mc "Damn, not only are your tits amazing but so is that tight ass... I'm going to POWERFUCK you doggy-style then!"
scene diamondheatherbackground01
show diamondheatherprefuck01
with dissolve
he "Are you ready for me to impale myself on your ALPHA-FUTA cock, boss?"
di "Oh yeah, you're making me so ROCKHARD Heather, GET DOWN ON IT!"

play music "v07/heatherfuck.mp3"
label SukYuFuckSlow:
scene heathercumbackground01
show sukyufuckslow
call screen sukyufuckslow01
screen sukyufuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukYuFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("SukYuFuckFast") 
    imagebutton:
        focus_mask True
        idle "v07/heatherview.png"
        hover "v07/heatherview.png"
        action Jump ("DiamondHeatherSlow") 

label DiamondHeatherSlow:
scene diamondheatherbackground01
show diamondheatherslow
call screen diamondheatherslow01
screen diamondheatherslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukYuFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DiamondHeatherFast") 
    imagebutton:
        focus_mask True
        idle "v07/sukyuview.png"
        hover "v07/sukyuview.png"
        action Jump ("SukYuFuckSlow") 

label SukYuFuckFast:
sy "Please PILE-DRIVE your mammoth dong into me FASTER!"
scene heathercumbackground01
show sukyufuckfast
call screen sukyufuckfast01
screen sukyufuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukYuFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("SukYuFuckSlow") 
    imagebutton:
        focus_mask True
        idle "v07/heatherview.png"
        hover "v07/heatherview.png"
        action Jump ("DiamondHeatherFast") 

label DiamondHeatherFast:
di "Go on Heather, fuck my futa cock FASTER!"
scene diamondheatherbackground01
show diamondheatherfast
call screen diamondheatherfast01
screen diamondheatherfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukYuFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("DiamondHeatherSlow") 
    imagebutton:
        focus_mask True
        idle "v07/sukyuview.png"
        hover "v07/sukyuview.png"
        action Jump ("SukYuFuckFast") 
            
label SukYuFuckEnd:
sy "Are you about to PUMP YOUR SEED inside me [name]? I can't wait to feel your GIANT jets of jizz!"
mc "Oh God, you're spurring me on... I..."
scene heathercumbackground01 blurred
show sukyufuckcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
stop music
play music "Sounds/splooge02.mp3"
sy "Oh YES, I LOVE being filled up by a young stud-shota's sweet cum!"
with fastflash
mc "I'm giving it ALL, ALL OF MY NUTJUICE! AAAH!"
scene sukyucumbackground blurred
show sukyufuckcum02
with dissolve
sy "Oooh, you're already DRIPPING out of my tight Asian fuckhole, there's SSOOO MUCH of your sweet nectar!"
with fastflash
mc "I have some MORE for you Suk-Yu!"
stop music
hide sukyufuckcum02
show sukyufuckcum03
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "More pumped-up shota cum for you Suk-Yu! AAAH!"
with fastflash
sy "Mmmh, it feels so SCALDING on my back [name], you're my BEST customer!"
mc "Phew, that's cos you bring out the BEST in me Suk-Yu!"

play music "Sounds/womansex01.mp3"
scene diamondheatherbackground01 blurred
show diamondheatherfast
with dissolve
di "I'm ready to unleash a torrent of my futa-cum inside you Heather!"
he "Go on boss, do it, I'm ready!"
hide diamondheatherfast
show diamondheathercum01
with dissolve
stop music
play sound "Sounds/moaning02.mp3"
di "I'm cumming!"
with fastflash
he "So am I boss, your cock feel sssooo good pumping its jizz inside my tender pussy!"
hide diamondheathercum01
show diamondheathercum02
with dissolve
he "Oooh? You're still BLASTING your BIG load all over my back!"
with fastflash
di "Damn girl, I never came so much, AAAHH!"
scene diamondheatherbackground01 blurred
show diamondheathercum03
with dissolve
play sound "Sounds/kiss.mp3"
he "Mmmh, boss... You're the best... And I hope I was the BEST for YOU!"
di "Get cleaned up girls, I need to talk with my test subject..."
if period == 2:
    $ period += 1
show screen injury
show screen mcstats
show screen calendar
scene diamondharem01
show warriorchief03 at right
with fade
stop sound
stop music
play music "v07/diamondmusic.mp3"
if strippercatchwin and renpy.seen_image("strippercum01") == False and lustsy == 0:
    $ lustsy = 1
if strippercatchwin and renpy.seen_image("strippercum01") and lustsy <= 1:
    $ lustsy = 2    
di "So, which girl deserves to be my feature stripper?"
menu:
    "Suk-Yu for sure!":
        hide warriorchief03
        show warriorchief02 at right
        with fastdissolve
        di "I was actually thinking the same thing. So it will be then!"
        show sukyu01 at centerleft with moveinleft
        sy "Oh, I'm honored! I'll make sure people give LOTS of tips!"
        call LustPlusSukYu
        $ chosesukyu = True
    "Heather of course!":
        hide warriorchief03
        show warriorchief02 at right
        with fastdissolve
        di "I was actually thinking the same thing. So it will be then!"
        show heather01 at centerleft with moveinleft
        he "My tits will be the central pieces of the show!"
        call LustPlusHeather
        $ choseheather = True
hide warriorchief02
show warriorchief03 at right
with fastdissolve
di "And now my Warriors will take you back to your compound."
mc "What, you know where it is???"
hide warriorchief03
show warriorchief01 at right
with fastdissolve
di "Of course I do! I have my little spies EVERYWHERE."
if mcbikestolen:
    hide warriorchief01
    show warriorchief04 at right
    with fastdissolve    
    mc "And why can't I go back with my OWN rig?"
    di "Because I get to KEEP your motorbike! You want it back? BUY it back. WIth DIAMONDS! HA HA!"
stop music
$ period += 1
scene command01
show lena03
with fade
if withpe:
    le "What happened to you? Penny told me you were kidnapped by some Road Warriors?"
if withbe:
    le "What happened to you? Bella told me you were kidnapped by some Road Warriors?"
if alone and withnone == False:
    le "What happened to you? Penny had to retrieve your accompanying harem girl in the middle of nowhere."
if alone and withnone:
    le "What happened to you? Why are you coming back so late?"
mc "Road Warriors Chief Diamond had me abducted. She needed my expertise for some delicate matter. Picking a stripper for her joint."
hide lena03
show lena05
with fastdissolve
le "And apparently, you decided to STAY longer than you should have! Thus WASTING everyone's time!"
mc "I didn't have the choice Chief, I swear! They almost drained my nuts. Almost."
hide lena05
show lena06
with fastdissolve
le "*sigh* Well go to the medbay because you do indeed look in poor shape. DISMISSED."
mc "Sure thing, Chief Lena!"
jump Medbay

label ExploreHex43:
play music "Sounds/desertwind01.mp3"
if warriorcapture == False:
    scene noharemfar with fade
    mc "Nothing. Just desolation and dust."
    if withpe:
        pe "Let's not hang around here too long then and let's go back to the compound."
        mc "Still, I wonder whether this is one of those hexes where there's nothing until I somehow find out that there is something through some other hex..."
        pe "You mean like Desert Town?"
        mc "Yeah, like that one..."
        pe "Maybe we'll know some day. Let's go."
        jump BackHex43b
    if withbe:
        be "Let's not hang around here too long then and let's go back to the compound."
        mc "Still, I wonder whether this is one of those hexes where there's nothing until I somehow find out that there is something through some other hex..."
        be "You mean like Desert Town?"
        mc "Yeah, like that one..."
        be "Maybe we'll know some day. Let's go."
        jump BackHex43b
    if alone:
        mc "I wonder whether this is one of those hexes where there's nothing until I somehow find out that there is something through some other hex..."
        mc "Guess I won't find out today, it's getting late, I should head back to the compound."
        jump BackHex43b
    
if warriorcapture:
    scene diamondharemfar with fade
    mc "Ah, back at Diamond's harem... Hope I'll be allowed inside."
    scene haremdoor01
    show bouncer01
    with dissolve
    bo "What do you want?"
    mc "I have something important to tell the boss."
    hide bouncer01
    show bouncer02
    with fastdissolve
    bo "Alright, you can come in, but I'll keep my eyes on you. And no one else is allowed in but you, is that clear?"
    mc "Crystal clear. Or diamond clear, right? Got the pun? right?"
    stop music
    if (choseheather and sukyuharemquest == False) or (choseheather == False and heatherharemquest == False):
        scene diamondharem01 with dissolve
    if choseheather and sukyuharemquest and clearedhex51 == False:
        scene diamondharem01
        show diamondharem01c
        show warriorchief01 
        with dissolve
    if choseheather == False and heatherharemquest and clearedhex51 == False:
        scene diamondharem01
        show diamondharem01d
        show warriorchief01 
        with dissolve
    if clearedhex51:
        $ d2girlharem=renpy.random.randint(1,2)
        if d2girlharem == 1:
            scene diamondharem01
            show diamondharem01c
            show warriorchief01 
            with dissolve
        if d2girlharem == 2:
            scene diamondharem01
            show diamondharem01d
            show warriorchief01 
            with dissolve
    play music "v07/diamondmusic.mp3"
    di "What do you want?"
    label HaremChiefDialogue:
    menu:
        "I'm here to buy back the bike you STOLE from me!" if mcbikestolen and (gem or hulkgem or aliendiamonds):
            hide warriorchief01
            show warriorchief04
            with fastdissolve
            di "I don't really like the tone of your voice... Do you have some diamonds at least or are you just full of yourself?"
            mc "I do have some diamonds. HERE. Now give me my fucking bike back!"
            hide warriorchief04
            show warriorchief03
            with fastdissolve
            di "That's a fine haul. You can have your bike back. After this."
            mc "After what?"
            di "This..."
            play sound "Sounds/punch.mp3"
            scene diamondharem01
            show warriorchief03
            with flash
            call MCInjury
            $ mcinjuredfight = True
            mc "Ouch! What was that for?"
            di "Thank you Bob. This young man deserves to understand WHO'S THE BOSS HERE!"
            mc "Ok, Ok, I understand. Perfectly well. Could I have my bike back pretty please? With sugar on top?"
            stop music
            scene townbike with fade
            show warriorchief03 at right with moveinright
            di "There she is. Now leave, you hear me?"
            mc "Sure, I'm off, Chief Diamond... Sorry about all the bother."
            hide warriorchief03 with dissolve
            $ mcbike = True
            $ mcbikeboughtharem = True
            $ boughtbackbikeharem = True
            $ mcbikestolen = False
            if gem:
                $ gem = False
                jump BackHex43b
            if hulkgem:
                $ hulkgem = False
                jump BackHex43b
            if aliendiamonds:
                $ aliendiamonds = False
                jump BackHex43b
            jump BackHex43b
        "I might have come across some diamonds... LOTS of diamonds." if knowdiamonds and totalgems >= 1 and mcbike == False and mcbikestolen == False:
            hide warriorchief01
            show warriorchief04
            with fastdissolve
            di "Really?... That might interest me then. What's your haul and what do you want in return?"
            mc "You're the head of the local Road Warriors, you must have some spare rigs. I want one."
            hide warriorchief04
            show warriorchief03 
            with fastdissolve
            di "Let me see your haul then..."
            if totalgems >= 2:
                hide warriorchief03
                show warriorchief04 
                with fastdissolve
                di "Oh... Quite the haul there... OK, it's a deal then! I'll take you round the back and show you your new TOP motorbike then."  
                stop music
                scene townbike with fade
                show warriorchief03 at right with moveinright
                di "There she is. Top speed of 180 miles an hour. Can carry an extra passenger too."
                mc "Alright! I have my own rig now, cha-ching cha-ching!"
                di "And I'll grant you free entry into our stripbar from now on too. See, I ain't the bitch you thought I was, hey?"
                mc "No you are not indeed! I will now leave you and test-drive this baby."
                hide warriorchief03 with dissolve
                $ gem = False
                $ hulkgem = False
                $ aliendiamonds = False
                $ mcbike = True
                $ mcbikeboughtharem = True
                jump BackHex43b
            hide warriorchief03
            show warriorchief02 
            with fastdissolve
            di "PATHETIC! Not nearly enough diamonds to be worth my while! Come back when you have found MORE of them."            
            mc "Ah, I thought that would be enough, sorry..."
            jump BackHex43b
        "So, I see Suk-Yu is here... (have free sex with Suk-Yu)" if d2girlharem == 1:
            hide warriorchief01
            show warriorchief04 
            with fastdissolve
            di "Is that why you came? Just to fuck one of MY girls?"
            mc "May I remind you that you have a full harem again, thanks to me..."
            hide warriorchief04
            show warriorchief03 
            with fastdissolve
            di "Umpf.. I suppose I do owe you a debt of gratitude. Fine, you can have her. For ONE period. Then, you'll have to leave."
            jump FuckSukYuPaid
        "So, I see Suk-Yu is here. I'm here. My cock is here. Err.. Even your cock is here." if heatherharemquest and heatherquestdone == False:
            hide warriorchief01
            show warriorchief04 
            with fastdissolve
            di "You wanna fuck her? Twenty bucks."
            menu:
                "Ah. I don't have that kind of money." if money <= 19:
                    hide warriorchief04
                    show warriorchief02 
                    with fastdissolve
                    di "And I don't have that kind of time to WASTE with you, poor boy! Be gone!"
                    jump BackHex43b
                "Mmmh, definitely cheaper than what Twatt Gaetz paid, I'm in!" if money >= 20:
                    $ money -= 20
                    hide warriorchief04
                    show warriorchief03 
                    with fastdissolve 
                    di "Of course it's cheaper, minors are more expensive. Suk-Yu's all yours. For a period. Then she's MINE again!"
                    jump FuckSukYuPaid
                "What about you give me a price and you get to join in on the action?" if money >= 10:
                    $ money -= 10
                    hide warriorchief04
                    show warriorchief01 
                    with fastdissolve 
                    di "I can GET the action anytime I want. So why would I accept such a deal?"
                    mc "Well, how about we test if we can stick BOTH our cocks into Suk-Yu's pussy? Can you get THAT kind of action without me around?"
                    hide warriorchief01
                    show warriorchief03 
                    with fastdissolve 
                    di "Interesting... Alright, I'll let you fuck her for a while and then we test your theory for a 10 dollar discount."
                    mc "Alright! MFutaF tag, here we come!"
                    $ fuckwithdiamond = True
                    jump FuckSukYuPaid
                "That's too steep for me, not interested." if money >= 20:
                    hide warriorchief04
                    show warriorchief02 
                    with fastdissolve
                    di "And that's too fucking bad for you then. Be gone!"
                    jump BackHex43b            
        "So, I see Heather is here... (have free sex with Heather)." if d2girlharem == 2:
            hide warriorchief01
            show warriorchief04 
            with fastdissolve
            di "Is that why you came? Just to fuck one of MY girls?"
            mc "May I remind you that you have a full harem again, thanks to me..."
            hide warriorchief04
            show warriorchief03 
            with fastdissolve
            di "Umpf.. I suppose I do owe you a debt of gratitude. Fine, you can have her. For ONE period. Then, you'll have to leave."
            jump FuckHeatherPaid
        "So, I see Heather is here. I'm here. My cock is here. Err.. Even your cock is here." if sukyuharemquest and sukyuquestdone == False:
            hide warriorchief01
            show warriorchief04 
            with fastdissolve
            di "You wanna fuck her? Twenty bucks."
            menu:
                "Ah. I don't have that kind of money." if money <= 19:
                    hide warriorchief04
                    show warriorchief02 
                    with fastdissolve
                    di "And I don't have that kind of time to WASTE with you, poor boy! Be gone!"
                    jump BackHex43b
                "Mmmh, definitely cheaper than what Twatt Gaetz paid, I'm in!" if money >= 20:
                    $ money -= 20
                    hide warriorchief04
                    show warriorchief03 
                    with fastdissolve 
                    di "Of course it's cheaper, minors are more expensive. Heather's all yours. For a period. Then she's MINE again!"
                    jump FuckHeatherPaid
                "What about you give me a price and you get to join in on the action?" if money >= 10:
                    $ money -= 10
                    hide warriorchief04
                    show warriorchief01 
                    with fastdissolve 
                    di "I can GET the action anytime I want. So why would I accept such a deal?"
                    mc "Well, how about we test if we can stick BOTH our cocks into Heather's pussy? Can you get THAT kind of action without me around?"
                    hide warriorchief01
                    show warriorchief03 
                    with fastdissolve 
                    di "Interesting... Alright, I'll let you fuck her for a while and then we test your theory for a 10 dollar discount."
                    mc "Alright! MFutaF tag, here we come!"
                    $ fuckwithdiamond = True
                    jump FuckHeatherPaid
                "That's too steep for me, not interested." if money >= 20:
                    hide warriorchief04
                    show warriorchief02 
                    with fastdissolve
                    di "And that's too fucking bad for you then. Be gone!"
                    jump BackHex43b            
        "I saw Heather, she ain't doing so good. You should really take her back into your harem." if heatherharemquest and heatherquestdone == False:
            if sukyuaccepted == False or diamondaccepted == False:
                hide warriorchief01
                show warriorchief02
                with fastdissolve
                di "And why would I do that?"
                mc "Errr. Cos you're a nice person? Right?"
                hide warriorchief02
                show warriorchief01
                with fastdissolve
                di "WRONG! You must mistake me for someone who CARES!"
                jump HaremChiefDialogue
        "I saw Suk-Yu, she ain't doing so good. You should really take her back into your harem." if sukyuharemquest and sukyuquestdone == False:
            if heatheraccepted == False or diamondaccepted == False:
                hide warriorchief01
                show warriorchief02
                with fastdissolve
                di "And why would I do that?"
                mc "Errr. Cos you're a nice person? Right?"
                hide warriorchief02
                show warriorchief01
                with fastdissolve
                di "WRONG! You must mistake me for someone who CARES!"
                jump HaremChiefDialogue
        "So, how is Suk-Yu doing as your continuing feature stripper?" if chosesukyu and heatherharemquest == False:
            hide warriorchief01
            show warriorchief03 
            with fastdissolve
            di "She's doing VERY well. Bringing in lots of customers and MONEY."
            mc "Since I helped you choose her, I should get a cut, right?"
            di "HA HA, you're a funny guy... Anything else you'd like to bother me with?"
            window hide
            hide warriorchief03
            show warriorchief01
            with dissolve
            jump HaremChiefDialogue            
        "So, how is Heather doing as your new feature stripper?" if choseheather and sukyuharemquest == False:
            hide warriorchief01
            show warriorchief03 
            with fastdissolve
            di "She's doing VERY well. Bringing in lots of customers and MONEY."
            mc "Since I helped you choose her, I should get a cut, right?"
            di "HA HA, you're a funny guy... Anything else you'd like to bother me with?"
            window hide
            hide warriorchief03
            show warriorchief01            
            with dissolve
            jump HaremChiefDialogue            
        "Ah, I was hoping to see Suk-Yu and Heather, but they are not here..." if sukyuharemquest == False and heatherharemquest == False:
            hide warriorchief01
            show warriorchief03 
            with fastdissolve
            di "I bet you were also hoping to fuck them for free? I'm DONE using you, nothing is free for you any longer, you hear me?"
            mc "Alright, alright, gee, I was about to offer my alpha-cock FREE OF CHARGE, but I see it is not wanted..."
            window hide
            hide warriorchief03
            show warriorchief01
            with dissolve
            di "Anything else?"
            jump HaremChiefDialogue        
        "I'd like to get a tattoo of your gang. (-10$, + 1 Road Warrior pt)" if mcwarrior >= 4 and money >= 10 and diamondtattoo == False:
            hide warriorchief01
            show warriorchief03 
            with fastdissolve
            di "Fine, but I'm warning you, it means you are MINE and you'll do what I need from you in the future!"
            mc "I'm fine with that, as long as I don't get kidnapped by your Road Warriors gang any more..."
            hide warriorchief03
            show warriorchief02 
            with fastdissolve            
            di "Agreed then. Please follow Shelly..."
            show tattooist02 at left with moveinleft
            tt "This way please..."
            hide tattooist02 with moveoutleft
            scene diamondharem01
            show warriorchief03
            with fade
            $ money -= 10
            $ diamondtattoo = True
            di "So, are you happy with your tattoo?"
            mc "Sure. I mean, I can't see it, it's on my back, and really small so it won't ever appear on-screen, but yeah, I like it. I feel like a Road Warrior now!"
            call PlusWarrior
            hide warriorchief03
            show warriorchief01
            with dissolve
            di "Anything else?"
            jump HaremChiefDialogue
        "Leave":
            mc "It was a pleasure talking to you."
            di "NOT likewise."
            jump BackHex43b

label BackHex43b:
stop music
$ period += 1
scene command01
show lena01
with fade
if alone:
    le "So, what do you have to report about area E3, scout?"
if alone == False:
    le "So, what do you have to report about area E3, scouts?"
if diamondtattoo and diamondtattoosaid == False:
    mc "I got a brand new tattoo, Chief! I'm now an official gang member. I'm totally badass."
    hide lena01
    show lena05
    with fastdissolve    
    le "Well good for you. How much time was wasted on this adventure exactly?"
    mc "Err..."
    hide lena05
    show lena06
    with fastdissolve
    le "DISMISSED!"
    $ diamondtattoosaid = True
    jump LeaveCommand    
if boughtbackbikeharem:
    mc "I got my rig back, Chief!"
    hide lena01
    show lena05
    with fastdissolve    
    le "Well good for you. How much time was wasted on this adventure exactly?"
    mc "Err..."
    hide lena05
    show lena06
    with fastdissolve
    le "DISMISSED!"
    jump LeaveCommand    
if mcbikeboughtharem:
    mc "I acquired a top motorbike, Chief! Now I can roam around the wilderness unencumbered by a scout."
    if withpe:
        pe "Hey! What is that supposed to mean?"
        call LustMinusPenny
    if withbe:
        be "Hey! What is that supposed to mean?"
        call LustMinusBella
    mc "Err... Ah, I forgot you were still here..."
    hide lena01
    show lena05
    with fastdissolve
    le "*sigh*. That'll teach you a lesson on STAYING FOCUSED. DISMISSED."
    hide lena05 with dissolve
    jump LeaveCommand
if warriorcapture == False:
    mc "Desolation and dust, Chief. Nothing else. Not even a genie's lamp."
    hide lena01
    show lena06
    with fastdissolve
    le "What are you babbling about? *sigh*. Try and stay focused for once, [name]... DISMISSED."
    hide lena06 with dissolve
    jump LeaveCommand
if (heatherharemquest and heatherquestdone == False) or(sukyuharemquest and sukyuquestdone == False):
    mc "I'm working on completing a quest. Then I'll be almost done with that hex."
    hide lena01
    show lena06
    with fastdissolve
    le "A quest? What kind of quest?"
    mc "Err, you know, something personal..."
    hide lena06
    show lena05
    with fastdissolve
    le "I like a man of mystery but sometimes you're just too mysterious. You are dismissed!"
    hide lena05 with dissolve
    jump LeaveCommand
if (heatherharemquest and heatherquestdone) or (sukyuharemquest and sukyuquestdone):
    mc "I completed an essential quest, Chief!"
    hide lena01
    show lena06
    with fastdissolve
    le "A quest? What kind of quest?"
    mc "Err, you know, something personal..."
    hide lena06
    show lena05
    with fastdissolve
    le "I like a man of mystery but sometimes you're just too mysterious. You are dismissed!"
    hide lena05 with dissolve
    jump LeaveCommand
mc "Err, well, nothing much at this stage. But something tells me there will be MORE going on in this hex eventually."
hide lena01
show lena06
with fastdissolve    
le "Well, I don't have time to wait months for the dev to clear this hex, so in the meantime, you've got to move to OTHER hexes, understood?"
mc "I get it, Chief."
le "DISMISSED."
hide lena06 with dissolve
jump LeaveCommand

label ExploreHex51:
$ exploredhex51 = True
scene caravan01 with fade
play music "Sounds/desertwind01.mp3"
if choseheather and sukyuharemquest:
    mc "Let's go and talk to Suk-Yu again."
    scene caravan03 blurred with dissolve
    show sukyucautious with moveinright
    sy "You again? I hope you bring good news..."
    if sukyuquestdone == False:
        mc "Err... Just checking on you, making sure you're still alive."
        hide sukyucautious
        show sukyuangry
        with fastdissolve
        sy "I am, but you WON'T BE if you continue to WASTE MY TIME!"
        mc "Alright, alright, my mistake. I'll be on my way then..."    
        sy "I told you NOT TO COME BACK until you GOT ME MY JOB BACK!"
        hide sukyuangry with dissolve
    if sukyuquestdone:
        mc "Yes, Chief Diamond is prepared to take you back into her harem!"
        hide sukyucautious
        show sukyuhappy
        with fastdissolve
        sy "Really? I can leave this dump and go back to being a stripper and a prostitute?"
        mc "Yep, all thanks to me. And you'll be sharing the stage with Heather, so you'll have even more time prostituting."
        hide sukyuhappy
        show sukyulaughing
        with fastdissolve
        sy "Thank you so much [name]! I'll go and pack my bags straight away!"
        call LustPlusSukYu
        hide sukyulaughing
        show sukyuhappy
        with fastdissolve
        sy "And I hope to see you at Chief Diamond's harem for some FUN time together... *wink*"
        sy "Remember, it's hex E3."
        mc "Oh, I remember, I remember..."
        $ toldsukyuquestdone = True
        hide sukyuhappy with dissolve        
        $ clearedhex51 = True
    jump BackHex51        

if choseheather == False and heatherharemquest:
    mc "Let's go and talk to Heather again."
    scene caravan03 blurred with dissolve
    he "You again? I hope you bring good news..."
    if heatherquestdone == False:
        mc "Err... Just checking on you, making sure you're still alive."
        hide heathercautious
        show heatherangry
        with fastdissolve
        he "I am, but you WON'T BE if you continue to WASTE MY TIME!"
        mc "Alright, alright, my mistake. I'll be on my way then..."    
        he "I told you NOT TO COME BACK until you GOT ME MY JOB BACK!"
        hide heatherangry with dissolve
    if heatherquestdone:
        mc "Yes, Chief Diamond is prepared to take you back into her harem!"
        hide heathercautious
        show heatherhappy
        with fastdissolve
        he "Really? I can leave this dump and go back to being a stripper and a prostitute?"
        mc "Yep, all thanks to me. And you'll be sharing the stage with Suk-Yu, so you'll have even more time prostituting."
        hide heatherhappy
        show heatherlaughing
        with fastdissolve
        he "Thank you so much [name]!"
        call LustPlusHeather
        hide heatherlaughing
        show heatherhappy
        with fastdissolve
        he "And I hope to see you at Chief Diamond's harem for some FUN time together... *wink*"
        he "Remember, it's hex E3."
        mc "Oh, I remember, I remember..."
        hide heatherhappy with dissolve
        $ toldheatherquestdone = True
        $ clearedhex51 = True
    jump BackHex51

mc "There's a lonely caravan over there, next to a lake, that looks like it might be occupied..."
if withpe:
    pe "Our job is to investigate. So... Why don't you go and investigate.."
    mc "I feel like I'm being used as a guinea pig in a giant experiment..."
    pe "Stop moaning and do what you're paid to do. I'll look out for you. From a distance."
if withbe:
    be "Our job is to investigate. So... Why don't you go and investigate.."
    mc "I feel like I'm being used as a guinea pig in a giant experiment..."
    be "Stop moaning and do what you're paid to do. I'll pray for you. From a distance."
if alone:
    mc "I shall go and investigate. Cos I'm that kind of brave adventurer."

scene caravan02 with dissolve
mc "The blinds are down. Mmmh, what should I do I wonder..."
menu:
    "Call out for someone's presence":
        mc "Anybody there? Bueller? Anyone? Anyone?"
        $ seencaravan = True
        jump DoorOpen        
    "Try and open the door":
        $ seencaravan = True
        jump CaravanDoor
    "Leave":
        mc "This place is clearly empty. I'm not even investigating and leaving straight away cos I'm a coward."
        jump BackHex51
 
label CaravanDoor:
scene caravan04 with dissolve
play sound "v071/doorjammed.mp3"
mc "Ah shit, the door is locked. And really tough to open by brute force for some reason."
scene caravan03 with dissolve
play sound "v071/doorslam.mp3"
if choseheather:
    show sukyuguns with dissolve
    play sound "Sounds/gun.mp3"
    sy "Get the fuck out of here, marauding thieves!"
    window hide
    $ renpy.pause(1.0, hard=True)
    stop sound
    if withpe:
        pe "Stop shooting, I'm a Road Warrior!"
        hide sukyuguns
        show sukyuguns02
        with fastdissolve
        sy "Mmmh, well I ain't anymore, but I'll stop out of respect for you, Penny."
        pe "What do you mean you're not anymore?"
        hide sukyuguns02
        show sukyuangry
        with fastdissolve
        sy "Your little boyfriend here got me KICKED OUT and RUINED my career by choosing that slut Heather over me!"
        jump Caravan02
    $ mcinjuredgun = True 
    call MCInjury
    if warriornickname == False:
        mc "Shit, she's shooting at me! Stop it, it's me, [name]!"
    if warriornickname:
        mc "Shit, she's shooting at me! Stop it, it's me, \"[name] the Impaler\"!"
    hide sukyuguns
    show sukyuguns02
    with fastdissolve
    sy "Why are you here? Haven't you done me enough harm?"    
    mc "What... What do you mean?"
    hide sukyuguns02
    show sukyuangry
    with fastdissolve
    sy "What do you think? You RUINED my career by choosing that slut Heather over me!"
    jump Caravan02    
if choseheather == False and exploredhex41:
    show heatherguns with dissolve
    play sound "Sounds/gun.mp3"
    he "Get the fuck out of here, marauding thieves!"
    window hide
    $ renpy.pause(1.0, hard=True)
    stop sound
    if withpe:
        pe "Stop shooting, I'm a Road Warrior!"
        hide heatherguns
        show heatherguns02
        with fastdissolve
        he "Mmmh, well I ain't anymore, but I'll stop out of respect for you, Penny."
        pe "What do you mean you're not anymore?"
        hide heatherguns02
        show heatherangry
        with fastdissolve        
        he "Your little boyfriend here got me KICKED OUT and RUINED my career by choosing that old whore Suk-Yu over me!"
        jump Caravan02
    $ mcinjuredgun = True 
    call MCInjury
    if warriornickname == False:
        mc "Shit, she's shooting at me! Stop it, it's me, [name]!"
    if warriornickname:
        mc "Shit, she's shooting at me! Stop it, it's me, \"[name] the Impaler\"!"
    hide heatherguns
    show heatherguns02
    with fastdissolve
    he "Why are you here? Haven't you done me enough harm?"
    mc "What... What do you mean?"
    hide heatherguns02
    show heatherangry
    with fastdissolve        
    he "What do you think? You RUINED my career by choosing that old whore Suk-Yu over me!"
    jump Caravan02
    
label DoorOpen:
scene caravan03 with dissolve
play sound "Sounds/doorsqueak.mp3"
if choseheather and sukyuharemquest == False:
    show sukyucautious with dissolve
    mc "Suk-Yu? What... What are you doing here?"
    hide sukyucautious
    show sukyuangry
    with fastdissolve
    sy "What do you think? You RUINED my career by choosing that slut Heather over me! I have no place to live except this dump now!"
    jump Caravan02    
if choseheather == False and exploredhex41 and heatherharemquest == False:
    show heathercautious with dissolve
    mc "Heather? What... What are you doing here?"
    hide heathercautious
    show heatherangry
    with fastdissolve
    he "What do you think? You RUINED my career by choosing that old whore Suk-Yu over me! I have no place to live except this dump now!"
label Caravan02:
scene caravan03 blurred
if choseheather:
    show sukyuangry
if choseheather == False and exploredhex41:
    show heatherangry
mc "I'm really sorry, I was FORCED to pick someone by Chief Diamond, I didn't want to, I swear!"
if choseheather:
    hide sukyuangry
    show sukyucautious
    with fastdissolve
if choseheather == False and exploredhex41:
    hide heatherangry
    show heathercautious
    with fastdissolve
mc "Tell you what. Why don't you come back with me and join my harem, I'll take care of you. I live in a great place called \"Compound Eden\", what do you say?"

if choseheather:
    hide sukyucautious 
    show sukyulaughing
    with fastdissolve
    sy "Compound Eden? HA HA, you don't know?"
    mc "What?"
    hide sukyulaughing 
    show sukyuangry
    with fastdissolve
    sy "It's going to be destroyed on March the 4th when President-for-Life Trumpf releases the Kraken! I ain't going to your compound, I'll watch it BURN from my computer!"
    jump Caravan03   
if choseheather == False and exploredhex41:
    hide heathercautious
    show heatherlaughing
    with fastdissolve
    he "Compound Eden? HA HA, you don't know?"
    mc "What?"
    hide heatherlaughing
    show heatherangry
    with fastdissolve   
    he "It's going to be destroyed on March the 4th when President-for-Life Trumpf releases the Kraken! I ain't going to your compound, I'll watch it BURN from my computer!"

label Caravan03:
if withbe:
    be "That's on week 25!"
if withpe:
    pe "That's on week 25!"
if alone:
    mc "Hang on, let me calculate what week that is... Ah, it's on week 25."
if week >= 25:
    mc "And since we're already past that date, I don't know what it means."
    if choseheather:
        hide sukyuangry
        show sukyulaughing
        with fastdissolve   
        sy "It means your save is fucked. Like you're totally screwed in this game."
        mc "Hang on, how is the dev going to deal with this time lapse? I'm past that endgame point, so I'll just keep going and there's nothing he can do about it!"
        hide sukyulaughing
        show sukyuangry
        with fastdissolve   
        sy "I think you'll find that he can screw you big time if you don't start over."
    if choseheather == False and exploredhex41:
        hide heatherangry
        show heatherlaughing
        with fastdissolve   
        he "It means your save is fucked. Like you're totally screwed in this game."
        mc "Hang on, how is the dev going to deal with this time lapse? I'm past that endgame point, so I'll just keep going and there's nothing he can do about it!"
        hide heatherlaughing
        show heatherangry
        with fastdissolve   
        he "I think you'll find that he can screw you big time if you don't start over."
if week >= 20 and week <= 24:
    mc "That's less than five weeks away, I'd better hurry up!"
mc "Is this info reliable anyway? Where did you get it from?"
if choseheather:
    hide sukyuangry
    show sukyucautious
    with fastdissolve   
    sy "I have time on my hands now. And I follow \"Q\" on the Dark Web. He's never wrong in his prophecies! Well, except for just a few times."
    mc "What are you talking about, who's \"Q\"???"
    sy "The Prophet-Messenger of our Revolution! He will tell us when President Trumpf will finally arrest the cabal of leftist baby-eating pedophiles that rule the World!"
    hide sukyucautious
    show sukyulaughing
    with fastdissolve   
    sy "Oh, it will be a glorious day, I have my popcorn ready. And March the 4th is DEFINITELY the date to watch on my calendar. And it should be on YOURS!"
    mc "I need to stop this, I can't let all the innocent people who live in the compound die! Tell me where \"Q\" is!"
    hide sukyulaughing
    show sukyuthinking
    with fastdissolve   
    sy "No one has ever seen him. It is said that he might live in a bunker in hex F2, but I've been there and I never saw him, so neither will you! You can't STOP the QANON PROPHECY!"
    jump Caravan03b   
if choseheather == False and exploredhex41:
    hide heatherangry
    show heathercautious
    with fastdissolve   
    he "I have time on my hands now. And I follow \"Q\" on the Dark Web. He's never wrong in his prophecies! Well, except for just a few times."
    mc "What are you talking about, who's \"Q\"???"
    he "The Prophet-Messenger of our Revolution! He will tell us when President Trumpf will finally arrest the cabal of leftist baby-eating pedophiles that rule the World!"
    hide heathercautious
    show heatherlaughing
    with fastdissolve   
    he "Oh, it will be a glorious day, I have my popcorn ready. And March the 4th is DEFINITELY the date to watch on my calendar. And it should be on YOURS!"
    mc "I need to stop this, I can't let all the innocent people who live in the compound die! Tell me where \"Q\" is!"
    hide heatherlaughing
    show heatherthinking
    with fastdissolve   
    he "No one has ever seen him. It is said that he might live in a bunker in hex F2, but I've been there and I never saw him, so neither will you! You can't STOP the QANON PROPHECY!"
    jump Caravan03b  
label Caravan03b:
window hide
$ knowqanon = True
show knowledgeq at posmission
$ renpy.pause(1.0, hard=True)
pause
hide knowledgeq
mc "Thanks for the info! Tell you what, I'll petition Chief Diamond to take you back into her harem, how's that?"
if choseheather:
    hide sukyuthinking
    show sukyucautious
    with fastdissolve   
    sy "Yeah, whatever, good luck with that. We parted ways on very bad terms."
    window hide
    $ sukyuharemquest = True
    show sukyuquest at posmission
    $ renpy.pause(1.0, hard=True)
    pause
    hide sukyuquest    
    jump Caravan04   
if choseheather == False and exploredhex41:
    hide heatherthinking
    show heathercautious
    with fastdissolve   
    he "Yeah, whatever, good luck with that. We parted ways on very bad terms."
    window hide
    $ heatherharemquest = True
    show heatherquest at posmission
    $ renpy.pause(1.0, hard=True)
    pause
    hide heatherquest
    jump Caravan04   

label Caravan04:
mc "Trust me, my dong can be very persuasive..."
if choseheather:
    hide sukyucautious
    show sukyuthinking
    with fastdissolve   
    sy "Then it will be battle of dong wits, cos hers can be very persuasive too!"
    if persistent.tipson:
        show heathertip at tips with dissolve
        pause
        hide heathertip    
    jump Caravan05  
if choseheather == False and exploredhex41:
    hide heathercautious
    show heatherthinking
    with fastdissolve   
    he "Then it will be battle of dong wits, cos hers can be very persuasive too!"
    if persistent.tipson:
        show sukyutip at tips with dissolve
        pause
        hide sukyutip    
    jump Caravan05  
label Caravan05:
if withbe:
    be "What is she talking about? Chief Diamond has a cock? That's DISGUSTING! Why do you always associate yourself with the heretics of the Earth, [name]?"
    call LustMinusBella
    mc "Err... Part of my mission?"
if choseheather:
    mc "I think we should get going. I'll be back when I've found a way of making amends with you, Suk-Yu..."
    hide sukyuthinking
    show sukyucautious
    with fastdissolve   
    sy "I'd like to see that... Don't bother coming back until you succeed!"
    hide sukyucautious with dissolve
if choseheather == False and exploredhex41:
    mc "I think we should get going. I'll be back when I've found a way of making amends with you, Heather..."
    hide heatherthinking
    show heathercautious
    with fastdissolve   
    he "I'd like to see that... Don't bother coming back until you succeed!"
    hide heathercautious with dissolve

label BackHex51:
stop music
$ period += 1
scene command01
show lena01
with fade
if alone == False:
    le "So, what do you have to report about area F1, scouts?"
if alone:
    le "So, what do you have to report about area F1, [name]?"
if toldlenaqanon:
    le "A place that you've already been to if I remember correctly..."
    if clearedhex51 == False:
        mc "Yeah, I did, but I forgot something there so had to go back."
        hide lena01
        show lena06
        with fastdissolve
        le "*sigh* Get your act together will you [name]? DISMISSED!"
        hide lena06 with dissolve
    if clearedhex51:
        mc "Yeah, I did, but I went back to clear that hex. That's what you want, right, cleared hexes and all that."
        hide lena01
        show lena06
        with fastdissolve
        le "*sigh* Fine. You are dismissed."
        hide lena06 with dissolve
    jump LeaveCommand    
if knowqanon and toldlenaqanon == False:
    $ toldlenaqanon = True
    mc "I learnt that \"Q\" lives in hex F2."
    hide lena01
    show lenapensive
    with fastdissolve
    le "That dangerous quack... Could be an opportunity to blow the lid off these crazy conspiracy theories he's been spreading..."
    if rescuedmagnus:
        mc "But are they though? I mean, \"3PGs\" are real, I saw one."
        hide lenapensive
        show lena10
        with fastdissolve
        le "That's not the point! They're BAD for us, THEREFORE, they're conspiracy theories!"
        mc "Aaaah, I get it now, sorry Chief."
        hide lena10
        show lenapensive
        with fastdissolve
        le "He could be coming up with something even worse for all we know..."
    mc "Actually, it was also mentioned that the compound would be destroyed on March 4th, according to his prophecy. I mean, conspiracy theory."
    hide lenapensive
    show lena06
    with fastdissolve
    le "Then, you definitely have to do something about this! Find him and stop his prophecy! Or at least, delay it. While we deal wiht President Trumpf."
    mc "But how can I stop a prophecy?"
    hide lena06
    show lena10
    with fastdissolve
    le "That's YOUR problem. You are DISMISSED! And hurry up, March 4th is on week 25."
    if mcinjured:
        le "And go to the medbay, you're bleeding all over the place!"
        mc "Roger that, Chief."
        hide lena10 with dissolve
        jump Medbay
    hide lena10 with dissolve
    jump LeaveCommand
if knowqanon == False:
    mc "Just another desolate place with nothing of importance whatsoever."
    if withbe:
        be "Well, there was a caravan, but [name] was too cowardly to investigate."
        hide lenapensive
        show lena10
        with fastdissolve
        le "Well go BACK there and INVESTIGATE! That's what you're paid to do! DISMISSED!"
        hide lena10 with dissolve
        jump LeaveCommand
    if withpe:
        pe "Well, there was a caravan, but [name] was too cowardly to investigate."        
        hide lenapensive
        show lena10
        with fastdissolve
        le "Well go BACK there and INVESTIGATE! That's what you're paid to do! DISMISSED!"
        hide lena10 with dissolve
        jump LeaveCommand
    hide lenapensive
    show lena06
    with fastdissolve
    le "Really? That's strange, Penny did a quick scouting of the area the other day and said she saw a caravan in the distance."
    mc "Err.. A caravan you say? Nope, can't say I notic...."
    hide lenapensive
    show lena10
    with fastdissolve
    le "I can tell you're LYING. Go BACK there and INVESTIGATE! That's what you're paid to do! DISMISSED!"
    hide lena10 with dissolve
    jump LeaveCommand

label ExploreHex52:
scene bunkerfar with fade
play music "Sounds/desertwind01.mp3"
if knowqanon == False:
    mc "Ok, there's everything here. A forest on the left and some fields on the right. Which amounts to pretty much everything in this desolate world."
    menu:
        "Go into the forest":
            scene forest with dissolve
            if foundmushrooms == False:
                mc "This forest is pretty creepy. But I ain't leaving until I've picked up some of these adorable mushrooms. I'll see what Laurie thinks of them back at the compound."
                window hide
                show mushroom at posmission
                $ renpy.pause(2.0, hard=True)
                pause
                hide mushroom
                $ mushrooms = True
                $ foundmushrooms = True
            if foundmushrooms:
                mc "Apart from some mushrooms, and I already found those, there is nothing to see in this creepy forest. Let's go back to the compound."
                jump BackHex52
        "Go into the fields":
            scene bunkerfields01 with dissolve
            mc "There doesn't seem to be anything of interest around these parts. Let's go back home."
            jump BackHex52

if knowqanon:
    mc "So, the entrance to Q's bunker is here somewhere. Where should I search I wonder?..."
if persistent.tipson:
    show hex52atip at tips with dissolve
    pause
    hide hex52atip
menu:
    "Search the fields":
        if withpe and withnone:
            pe "I'll be staying by my rig, sorry, you're on your own there."
            mc "I'm used to it."
        if withbe and withnone:
            be "I'll be staying by my rig, sorry, you're on your own there."
            mc "I'm used to it."
        if withnone == False:
            if withpe:
                pe "I'll be staying by my rig, it needs to be watched over."
            if withbe:
                be "I'll be staying by my rig, it needs to be watched over."
            if witham:
                am "I'll go and search the forest then, I haven't seen trees in a long time!"
                jump SearchFields
            if withla:
                la "I'll go and search the forest then, I haven't seen trees in a long time!"
                jump SearchFields
            if withmi:
                mi "I'll go and search the forest then, I haven't seen trees in a long time!"
                jump SearchFields
            if not (witham or withla or withmi):
                mc "(talking to accompanying harem girl) I think it's best if you come with me, we can search together. And you're not a Sierra Club member so you'll be perfectly useless."
        jump SearchFields
    "Search the forest":
        if withpe and withnone:
            pe "I'll be staying by my rig, sorry, you're on your own there."
            mc "I'm used to it."
        if withbe and withnone:
            be "I'll be staying by my rig, sorry, you're on your own there."
            mc "I'm used to it."
        if withnone == False:
            if withpe:
                pe "I'll be staying by my rig, it needs to be watched over."
            if withbe:
                be "I'll be staying by my rig, it needs to be watched over."
            if witham:
                am "I'll go and search the plains then, I haven't seen grass in a long time!"
            if withla:
                la "I'll go and search the plains then, I haven't seen grass in a long time!"
            if withmi:
                mi "I'll go and search the plains then, I haven't seen grass in a long time!"
            if not (witham or withla or withmi):
                mc "(talking to accompanying harem girl) I think it's best if you come with me, we can search together. And you're not a Sierra Club member so you'll be perfectly useless."
        jump SearchForest
        
label SearchForest:
scene forest with dissolve
if foundmushrooms == False:
    mc "Dammit, I can't see jackshit in this dark forest, this search is pointless. Ah, but I see some mushrooms though, might as well pick some up and show them to Laurie."
    window hide
    show mushroom at posmission
    $ renpy.pause(2.0, hard=True)
    pause
    hide mushroom
    $ mushrooms = True
    $ foundmushrooms = True
    jump BackHex52
if foundmushrooms:
    mc "Apart from some mushrooms, which I already picked up once, there is nothing to see in this creepy forest..."
if withla:
    $ d2rolllaurieforest = renpy.random.randint(1, 2)
    if d2rolllaurieforest == 1:
        la "Come over here, I think I found something!"
        mc "Ah, Laurie's calling me from over there, ie: the fields. Let's go and meet her."
        scene bunkerlatch01 with fade
        mc "Well done Laurie, you found the bunker's entrance!"
        $ foundbunker = True
        jump BunkerLatch 
scene bunkerfar with fade
if withla:
    show laurie01 with dissolve
    la "Sorry [name], I searched the fields but couldn't find anything. But I didn't have time to look everywhere, it might still be there..."
if withmi:
    show michiko01 with dissolve
    mi "Sorry [name], I searched the fields but couldn't find anything. But I didn't have time to look everywhere, it might still be there..."
if witham:
    show amy01 with dissolve
    am "Sorry [name], I searched the fields but couldn't find anything. But I didn't have time to look everywhere, it might still be there..."
mc "Let's go back home then, it's getting late..."
jump BackHex52

label SearchFields:
scene bunkerfields01 with fade
mc "Let's look somewhere around here..."
if foundbunker:
    mc "I think I remember where it was..."
    if mcsierra <= 3: 
        mc "Actually, no, I don't remember. I've lost all sense of tracking since my Sierra Club points are so low... And now I'm lost in this tall grass..."
        mc "Let's go back home, I've wasted enough time here..."
        jump BackHex52
    scene bunkerlatch01 with fade
    mc "Ah, there, I found it again! Let's try and get inside then..."
    jump BunkerLatch
if foundbunker == False:
    if mcsierra == 5:  
        scene bunkerlatch01 with fade
        mc "Ah, there's a suspicious latch! It MUST BE the entrance to Q's bunker."
        mc "My deep sense of tracking, acquired through weeks of Sierra Club...err.. tree-hugging, is finally paying off! Let's see if I can open that door now..."
        $ foundbunker = True
        jump BunkerLatch
    if mcsierra <= 4:  
        mc "Dammit, I can't see jackshit in this tall grass, this search is pointless."
        mc "Let's go back home, I've wasted enough time here..."
        jump BackHex52

label BunkerLatch:
if blewdoorbunker:
    mc "Damn, the latch was replaced after I blew it up last time."    
if trieddoorbunker == False:
    scene bunkerlatchtclosed with dissolve
    play sound "v071/doorjammed.mp3"
    mc "And of course, it's locked. FUCK!"
    $ trieddoorbunker = True
    jump BunkerDoorUnlock
if trieddoorbunker:
    if explosives == False:
        mc "Since I know it's locked, I have to try and use my sklls in picklocking, acquired through weeks of...err... mechanics training."
    if explosives:
        mc "Since I know it's locked, I have to try and use my sklls in picklocking, acquired through weeks of...err... mechanics training. Or blow it up with explosives."

label BunkerDoorUnlock:
scene bunkerlatch02 with dissolve
menu:
    "Try and pick the lock (Mechanics test)":
        jump BunkerPick
    "Blow it up" if explosives:
        jump BunkerBlow
    "Give up and go home":
        mc "I can't be bothered trying anything. I just can't."
        jump BackHex52

label BunkerBlow:
scene bunkerlatch01 with dissolve
play sound "Sounds/explosion.mp3"
mc "3. 2. 1..."
show bunkerlatchexplode with fastdissolve
mc "Thar' she blows!"
window hide
stop sound
pause 1.0
hide bunkerlatchexplode
show bunkerlatchopen01
with dissolve
mc "And now I can get in."
$ explosives = False
$ openedbunker = True
jump Bunker01

label BunkerPick:
scene bunkerlatchtclosed with dissolve
call DiceRoll
$ dtestrollbunker=(mcmechanics+diceroll)
if (dtestrollbunker >= 11 and not diceroll == 1) or diceroll == 6:
    window hide
    play sound "Sounds/doorsqueak.mp3"
    show mechanicswin at posskill
    $ renpy.pause(2.0, hard=True)
    hide mechanicswin
    mc "Yes, I did it!"
    $ openedbunker = True
    jump Bunker01
if (dtestrollbunker <= 10 and not diceroll == 6) or diceroll == 1:
    window hide
    play sound "v071/doorjammed.mp3"
    show mechanicsfail at posskill
    $ renpy.pause(2.0, hard=True)
    hide mechanicsfail
    play sound "Sounds/panting.mp3"
    mc "Damn, I failed miserably. And it's getting late. Will have to try another time then."
    jump BackHex52

label Bunker01:
scene bunker01
with dissolve
play music "Sounds/waterdrip.mp3"
mc "Down the rabbit-hole we go..."
scene bunker02
with dissolve
if metq == False:
    mc "What a creepy place... Let's move forward nevertheless, since I am a fearless hero."
if metq:
    mc "I remember where to go this time."
    jump MeetQ
scene bunker03 with dissolve
mc "Ah, a decision needs to be made I see... I hate those. There's always a good one and one where I end up injured."
label FirstIntersectionBunker:
scene bunker03
call screen bunker01
screen bunker01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/goleft.png"
        hover "Icons/goleft.png"
        action Jump ("Bunker02")
    imagebutton:
        focus_mask True
        idle "Icons/goright.png"
        hover "Icons/goright.png"
        action Jump ("Bunker03")

label Bunker02:
scene bunkercorridor with dissolve
mc "A long, potentially dangerous corridor. The suspense is killing me."
scene bunker04 with dissolve
mc "Not dead yet. And another intersection..."
label SecondIntersectionBunker:
scene bunker04
call screen bunker02
screen bunker02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/goleft.png"
        hover "Icons/goleft.png"
        action Jump ("Bunker04")
    imagebutton:
        focus_mask True
        idle "Icons/goright.png"
        hover "Icons/goright.png"
        action Jump ("Bunker05")

label Bunker03:
scene bunkercorridor
show bunkercorridorb
with dissolve
mc "Ah, there seems to be a door at the end of this long corridor."
scene bunker05l with dissolve
mc "Well, everything seems to be fine..."
scene bunkerwrong with dissolve
mc "Let's quietly push the do..."
play sound "Sounds/taser.mp3"
scene bunkerwrongb with hpunch
$ renpy.pause(2.0, hard=True)
scene bunker05l
with dissolve
play sound "Sounds/panting.mp3"
mc "Fuck, it was ELECTRIFIED!"
call MCInjury   
$ mcinjuredtaser = True
mc "Let's go back to the previous intersection. If I can remember where it was..."
jump FirstIntersectionBunker

label Bunker04:
scene bunkercorridor
show bunkercorridorb
with dissolve
mc "Ah, there seems to be a door at the end of this long corridor."
scene bunker05m with dissolve
mc "Well, everything seems to be fine..."
scene bunkerwrong with dissolve
mc "Let's quietly push the do..."
play sound "Sounds/taser.mp3"
scene bunkerwrongb with hpunch
$ renpy.pause(2.0, hard=True)
scene bunker05m
with dissolve
play sound "Sounds/panting.mp3"
mc "Fuck, it was ELECTRIFIED!"
call MCInjury   
$ mcinjuredtaser = True
mc "Let's go back to the previous intersection. If I can remember where it was..."
jump SecondIntersectionBunker

label Bunker05:
scene bunkercorridor
show bunkercorridorb
with dissolve
mc "Still alive and kicking. Indiana Jones has nothing on me. And now, another long, potentially dangerous, corridor with a door at the end..."
label MeetQ:
scene bunker06 with dissolve
if metq == False:
    mc "*Ah, that door is marked \"Q\"... Let's find out who Q really is then. I wonder if it's Trumpf himself. Or Ivanka. Or just some fat guy living in his mommy's basement.*"
if metq:
    mc "Let's try and surprise lardass this time..."
play sound "Sounds/doorsqueak.mp3"
scene shelter01
show qanon01
with dissolve
if metq == False:
    $ metq = True
    mc "*Ah. I guess it was the last option.*"
    q "So, we meet finally, I have been following your progress... Do you know who I am?"
    menu:
        "Yes I heard about you, you're Q. I thought you were some hot chick. What a disappointment.":
            hide qanon01
            show qanon02
            with fastdissolve
            q "The Deep State is always one step behind me, that's why! HA-HA!"
            hide qanon02
            show qanon03
            with fastdissolve
            q "Now. Do you want to know the truth? Can you HANDLE THE TRUTH?"
            mc "The truth is that I'm going to kick your ass if you don't change the date of the Day of the Kraken."
            hide qanon03
            show qanon01
            with fastdissolve        
            q "What, March the 4th? This is engraved in our CONSTITUTION, I can't change it and I WON'T CHANGE IT!"
            mc "Then we are at an impasse. Prepare to FIGHT!"
            hide qanon01
            show qanon03
            with fastdissolve                
            q "FIGHT WE SHALL THEN! I said it first, so I have the initiative! HA HA, the Deep State is always one step behind me!"
            jump QanonFight
        "Why are you half-naked?":
            hide qanon01
            show qanon02
            with fastdissolve
            q "I don't have time to worry about these petty things. I hav to monitor the DEEP STATE ELITE 24/7!"
            mc "It's kind of vile though. Especially since you're kind of vile yourself."
            hide qanon02
            show qanon03
            with fastdissolve
            q "What's vile is what the ELITE controlling the world are doing! Do you want to know the truth? Can you HANDLE THE TRUTH?"
            mc "The truth is that I'm going to kick your ass if you don't change the date of the Day of the Kraken."
            hide qanon03
            show qanon01
            with fastdissolve        
            q "What, March the 4th? This is engraved in our CONSTITUTION, I can't change it and I WON'T CHANGE IT!"
            mc "Then we are at an impasse. Prepare to FIGHT!"
            hide qanon01
            show qanon03
            with fastdissolve                
            q "FIGHT WE SHALL THEN! I said it first, so I have the initiative! HA HA, the Deep State is always one step behind me!"
            jump QanonFight
        "No and I don't care. Do you? I'm outta here! (leave)":
            q "You don't want to know the TRUTH! YOU CAN'T HANDLE THE TRUTH!"
            mc "Wha-tever dude."
            jump BackHex52

if metq:
    q "You again? You're like the Deep State, you just never give up, do you?"
    mc "Nope. So prepare to get your ass kicked! And this time, I have the initiative because I said it first!"
    $ qanoninitiative = True
    jump QanonFight
    
label QanonFight:
hide screen mcstats
hide screen calendar
play music "v072/battle.mp3"
scene shelter01
show qanonmcfight01 at farleft
show qanonfight01 at farright
with dissolve
if mcinjured:
    $ mc_health = 2.0
    mc "I start at a disadvantage because I'm injured..."
if mcinjured == False:
    $ mc_health = 3.0
$ qanon_health = 3.0
show screen screenfightmcqanon
if qanoninitiative == False:
    $ qanonfirst = True
if qanoninitiative:
    $ qanonfirst = False

label QanonRound:
if qanonfirst:
    jump RoundQanonFight
if qanonfirst == False:
    jump RoundMCQanonFight

label RoundQanonFight:  
mc "You don't scare me!"
play sound "v072/stomping.mp3"
window hide
hide qanonfight01
show qanonfight02 at farright
show qanonfight02 at farright02 with move
hide qanonfight02
show qanonfight01 at farright02
show qanonfight01 at centerright with move
hide qanonfight01
show qanonfight02 at centerright
show qanonfight02 at center with move
hide qanonfight02
show qanonfight01 at center
show qanonfight01 at centerleft with move
stop sound
window hide
label RoundQanonFightb:
call DiceRoll
if diceroll >= 4:
    hide qanonmcfight01
    hide qanonfight01
    show qanonfight04 at left
    with fastdissolve
    play sound "Sounds/crunch.mp3"
    q "Come closer to daddy, little man! REAL CLOSE!"
    $ counting = 0
    while counting < 20:
        $ mc_health -= 0.05
        $ counting += 1
        pause 0.01
    if mc_health >= 0.1:
        mc "AAARGH, let me down you fat oaf!"
    if mc_health <= 0.09:
        mc "I yield, Please stop breaking all my ribs!"
        if mcinjured == False:
            call MCInjury
        hide qanonfight04
        show qanonfight05 at midleft
        with fastdissolve
        $ mcinjuredfight = True
        jump QanonLoseEnd        
    hide qanonfight04
    show qanonmcfight01 at farleft
    show qanonfight01 at farright
    with fastdissolve
else:
    hide qanonmcfight01
    hide qanonfight01
    show qanonfight08 at left
    with fastdissolve
    mc "Duck and dodge. I learnt that move the other day!"
    q "Curses, you little rascal!"
    hide qanonfight08
    show qanonmcfight01 at farleft
    show qanonfight01 at farright
    with fastdissolve
$ qanonfirst = False
jump QanonRound

label RoundMCQanonFight:  
mc "I'm going to turn your face into a pumpkin until you're REALLY anonymous!"
window hide
show qanonmcfight01 at centerleft with move
call DiceRoll
$ dcombatroll=mccombat+diceroll        
if (dcombatroll >= 12 and not diceroll == 1) or diceroll == 6:
    window hide
    hide qanonmcfight01
    hide qanonfight01
    show qanonfight06 at farright02
    with fastdissolve
    play sound "Sounds/punch.mp3"
    mc "How do you like that, hey?"
    $ counting = 0
    while counting < 20:
        $ qanon_health -= 0.05
        $ counting += 1
        pause 0.01
    if qanon_health >= 0.1:
        q "Damn you, not my pretty face!"
        hide qanonfight06
        show qanonmcfight01 at farleft
        show qanonfight01 at farright
        with dissolve        
    if qanon_health <= 0.09:
        q "Damn you, not my pretty face!"
        hide qanonfight06
        show qanonfight07 at right
        with fastdissolve
        jump QanonWinEnd
if (dcombatroll <= 11 and not diceroll == 6) or diceroll == 1:
    window hide
    hide qanonmcfight01
    hide qanonfight01
    show qanonfight03 at farright02
    with fastdissolve
    q "HA HA! I felt nothing!"
    mc "I'm just hitting flab, this is useless..."
    hide qanonfight03
    show qanonmcfight01 at farleft
    show qanonfight01 at farright
    with dissolve
$ qanonfirst = True
jump QanonRound   

label QanonLoseEnd:
hide screen screenfightmcqanon
show screen mcstats
show screen calendar
mc "I just can't compete against 400lbs of lard!"
q "I am what I eat and I eat what I want!"
q "Now young man, DO YOU BELIEVE?"
mc "What?"
q "The righteousness of the Qanon movement!"
menu:
    "Yes, I see the light! At the end of the Dark Web tunnel! (+1 Trumpsters)":
        call PlusTrumpster
        q "Ah, another recruit for our Cause! I will let you leave and spread the Big Lie then!"
    "I'll never wear your tin foil hat! (+1 Deep State)":
        call PlusDeep
        q "So be it, then you must leave in shame! And injured!"
        mc "Been there, done that. And I'll be back."
jump BackHex52

label QanonWinEnd:
$ beatqanon = True
hide screen screenfightmcqanon
show screen mcstats
show screen calendar

play sound "Sounds/panting.mp3"
if persistent.tipson:
    show qtip at tips with dissolve
    pause
    hide qtip
if qanonwonfight02 and qautograph:
    q "Alright, stop it... *puff* I'm not in the top shape I used to be anymore and I yield! Here's 10 bucks, take them and leave!"
    $ money += 10
    mc "I'd better not have to come back and spank that fat ass of yours, you hear me?"
    q "I'll grow fatter and stronger and I'll beat you next time!"
    mc "Whatever, loser! I'm off."
    jump BackHex52    
if qanonwonfight02 and qautograph == False:
    q "Alright, stop it... *puff* I'm not in the top shape I used to be anymore and I yield! Here's 10 bucks, take them and leave!"
    $ money += 10
    mc "Oh, I'll take them. But I want an autograph from you!"
    q "Excuse me? WTF?"
    mc "Not for me, dumb ass. Make it to the name of Barbara."
    q "Alright, alright, here, let me go now!"
    mc "I'd better not have to come back and spank that fat ass of yours, you hear me?"
    q "I'll grow fatter and stronger and I'll beat you next time!"
    mc "Whatever, loser! I'm off."
    $ qautograph = True
    jump BackHex52    
if qanonwonfight and qanonwonfight02 == False:
    q "Alright, stop it... *puff* I'm not in the top shape I used to be anymore and I yield! Here's 20 bucks, take them and leave!"
    $ money += 20
    mc "Oh, I'll take them. But I ain't done with you by a long shot. Now tell me some info I don't know about but would be useful for me to know to get rid of Trumpf once and for all!"
    q "I... I just know that per the CONSTITUTION, the 69th Amendment to be more precise, presidents need to have children to continue their dynasty. Oh, and hot big-titted wife too."
    mc "Interesting..."
    q "That's it, I don't know nothing more, let me go now!"
    mc "I'd better not have to come back and spank that fat ass of yours, you hear me?"
    q "I'll grow fatter and stronger and I'll beat you next time!"
    mc "Whatever, loser! I'm off."
    $ qanonwonfight02 = True
    jump BackHex52    
if qanonwonfight == False:
    q "Alright, stop it... *puff* I'm not in the top shape I used to be anymore and I yield! Here's 20 bucks, take them and leave!"
    $ money += 20
    mc "Oh, I'll take them. But I ain't done with you by a long shot. Now you'll do as I said and change the date of the Day of the Kraken!"
    q "Alright, I'll... announce that it's been delayed another 5 weeks."
    mc "Five weeks only? Are you fucking kidding me?"
    q "I can't delay it any further or people will start not believing me anymore! I swear, this is the best I can do to maintain my cover and the trust of the Silent Majority."
    mc "You mean the deplorables?"
    q "Yeah, those dumb guys. They'll believe anything. Almost. That's why I can't push my luck too far."
    mc "I'd better not have to come back and spank that fat ass of yours, you hear me?"
    q "I'll grow fatter and stronger and I'll beat you next time!"
    mc "Whatever, loser! I'm off."
    $ qanonwonfight = True
jump BackHex52

label BackHex52:
stop sound
stop music
$ period += 1
scene command01
show lena01
with fade
if renpy.seen_image("caravan03") == False:
    le "So, what do you have to report about hex F2? Anything interesting?"
    if toldlenamushrooms == False and foundmushrooms:
        mc "I found some magic mushrooms, Chief."
        hide lena01
        show lena03
        with fastdissolve
        le "Oh, great, so now you're on drugs?"
        mc "No, it's for Laurie. She might find them useful. I would never eat them like that just for recreational use."
        le "Alright, well, you are dismissed."
        hide lena03 with dissolve
        $ toldlenamushrooms = True
        jump LeaveCommand
    if foundmushrooms == False:
        mc "Just... nothing really."
        hide lena01
        show lena03
        with fastdissolve
        le "If this hex exists, it must be important. It can't be like hex B3, the dev would be pushing it."
        mc "I agree, but he DOES often push it. Push it MANY INCHES."
        le "*sigh* You are dismissed, [name]..."
        hide lena03 with dissolve
        jump LeaveCommand
if renpy.seen_image("caravan03"):
    if toldlenabunker and toldlenaq and bunkerlenalust:
        le "So, did you manage to defeat Q again?" 
        if beatqanon:
            mc "I sure defeated him again, Chief!"
            hide lena01
            show lena06
            with fastdissolve
            le "And what was the point of that exactly?"
            mc "Errr. I got 20 bucks out of it?"
            hide lena06
            show lena05
            with fastdissolve            
            le "And you wasted one scouting mission... You are dismissed."
            if mcinjured:
                hide lenapensive
                show lena03
                with fastdissolve
                le "And go to the medbay, you look injured."
                jump Medbay
            $ beatqanon = False
            jump LeaveCommand    
        if beatqanon == False:
            mc "Err, no, no I didn't. Not this time. He put on some weight, if that was even possible."
            hide lena06
            show lena10
            with fastdissolve
            le "*sigh* You are dismissed."
            mc "I'll start by dismissing myself to the medbay."
            jump Medbay
                
    if toldlenabunker == False:
        le "So, what do you have to report about hex F2? Did you find Q's bunker?"    
        if foundbunker:
            mc "I sure did, Chief."
            $ toldlenabunker = True
            hide lena01
            show lena03
            with fastdissolve
            le "Good. Now, next question. Did you manage to infiltrate the bunker?"
            if openedbunker:
                mc "Got inside alright, Chief!"
                $ toldlenaq = True        
                hide lena03
                show lena06
                with fastdissolve        
                le "I like your answers so far. And now for the final question. Did you defeat Q?"
                if beatqanon:
                    mc "I sure did too, Chief!"
                    hide lena06
                    show lena07
                    with fastdissolve
                    le "Well, I'm very impressed!"
                    if bunkerlenalust == False:
                        call LustPlusLena
                        $ bunkerlenalust = True
                    le "And how much time did that buy us?"
                    mc "Five weeks. Tops. Can't do any better, he was very persuasive."
                    hide lena07
                    show lenapensive
                    with fastdissolve
                    le "Not much, but maybe sufficient to deal with the Orange menace... You are dismissed."
                    if mcinjured:
                        hide lenapensive
                        show lena03
                        with fastdissolve
                        le "And go to the medbay, you look injured."
                        jump Medbay
                    jump LeaveCommand 
                    $ beatqanon = False
                if beatqanon == False:
                    mc "Err, no, no I didn't. He was too fast. I mean, too fat."
                    hide lena06
                    show lena10
                    with fastdissolve
                    le "*sigh* Well, get FATTER and go back there to defeat him FAST. DISMISSED."
                    mc "I'll start by dismissing myself to the medbay."
                    jump Medbay
            if openedbunker == False:
                mc "Err, no, no I didn't. The latch was tightly locked, just as one would expect from a bunker latch."
                hide lena03
                show lena10
                with fastdissolve
                le "That's not an acceptable excuse! You're supposed to be a TRAINED adventurer. Open that latch and GET INSIDE! Dismissed."
                hide lena10 with dissolve
                jump LeaveCommand       
        if foundbunker == False:
            mc "Not yet. It is apparently very well hidden. Like anonymous or something."        
            hide lena01
            show lena10
            with fastdissolve
            le "You MUST find it! Our survival depends upon it, you understand?"
            mc "Copy that, Chief."
            le "DISMISSED!"
            hide lena10 with dissolve
            jump LeaveCommand

    if toldlenabunker and toldlenaq and bunkerlenalust == False:
        le "So, did you manage to defeat Q this time?" 
        if beatqanon:
            mc "I sure did, Chief!"
            hide lena01
            show lena07
            with fastdissolve
            if bunkerlenalust == False:
                call LustPlusLena
                $ bunkerlenalust = True
            le "And how much time did that buy us?"
            mc "Five weeks. Tops. Can't do any better, he was very persuasive."
            hide lena07
            show lenapensive
            with fastdissolve
            le "Not much, but maybe sufficient to deal with the Orange menace... You are dismissed."
            if mcinjured:
                hide lenapensive
                show lena03
                with fastdissolve
                le "And go to the medbay, you look injured."
                jump Medbay
            $ beatqanon = False
            jump LeaveCommand    
        if beatqanon == False:
            mc "Err, no, no I didn't. He was too fast. I mean, too fat."
            hide lena06
            show lena10
            with fastdissolve
            le "*sigh* Well, get FATTER and go back there to defeat him FAST. DISMISSED."
            mc "I'll start by dismissing myself to the medbay."
            jump Medbay
        
    if toldlenabunker and toldlenaq == False:
        le "So, did you manage to infiltrate the bunker this time?" 
        if openedbunker:
            mc "Got inside alright, Chief!"
            $ toldlenaq = True        
            hide lena03
            show lena06
            with fastdissolve        
            le "I like your answers so far. And now for the final question. Did you defeat Q?"
            if qanonwonfight:
                mc "I sure did too, Chief!"
                hide lena06
                show lena07
                with fastdissolve
                le "Well, I'm very impressed!"
                if bunkerlenalust == False:
                    call LustPlusLena
                    $ bunkerlenalust = True
                le "And how much time did that buy us?"
                mc "Five weeks. Tops. Can't do any better, he was very persuasive."
                hide lena07
                show lenapensive
                with fastdissolve
                le "Not much, but maybe sufficient to deal with the Orange menace... You are dismissed."
                if mcinjured:
                    hide lenapensive
                    show lena03
                    with fastdissolve
                    le "And go to the medbay, you look injured."
                    jump Medbay
                jump LeaveCommand    
            if qanonwonfight == False:
                mc "Err, no, no I didn't. He was too fast. I mean, too fat."
                hide lena06
                show lena10
                with fastdissolve
                le "*sigh* Well, get FATTER and go back there to defeat him FAST. DISMISSED."
                mc "I'll start by dismissing myself to the medbay."
                jump Medbay
        if openedbunker == False:
            mc "Err, no, no I didn't. The latch was tightly locked, just as one would expect from a bunker latch."
            hide lena03
            show lena10
            with fastdissolve
            le "That's not an acceptable excuse! You're supposed to be a TRAINED adventurer. Open that latch and GET INSIDE! Dismissed."
            hide lena10 with dissolve
            jump LeaveCommand       

label ExploreHex54:
$ exploredhex54 = True
play music "Sounds/desertwind01.mp3"
scene farm01 with fade
mc "Looks like a farm over there. I was starting to wonder where all the other survivors got their food from."    
if withbe:
    be "That food could very well be contaminated by radiation. I only trust Laurie's mutated salads and the camels I shoot by the will of the Phallus Lord!"
    mc "Sure, but I still need to investigate, right?"
    be "Oh yeah, you go right ahead."
if withpe:
    pe "That food could very well be contaminated by radiation. I only trust Laurie's mutated salads and the camels I shoot on the Wild Road!"
    mc "Sure, but I still need to investigate, right?"
    pe "Oh yeah, you go right ahead."
if alone:
    call AloneStance
        
scene farm02 with dissolve
if persistent.tipson:
    show hexf4tip at tips with dissolve
    pause
    hide hexf4tip
if seensneed == False:
    mc "I apparently came too late for some good fun."
    window hide
    show betty01 with moveinright
    bt "Betty Sneed's the name. What can I do you for, stranger?"
    mc "What happened to Chuck?"
    hide betty01
    show betty02
    with fastdissolve
    bt "He went out of luck. His bank fucked him over and he had to sell me his farm for a buck."
    mc "Well that must have sucked. For him, I mean."
    hide betty02
    show betty01
    with fastdissolve
    bt "Sure, especially since the banker was also fucking his wife."
    mc "Oh, so he was a cuck, too?"
    hide betty01
    show betty03
    with fastdissolve
    bt "Stop mucking about."
    hide betty03
    show betty01
    with fastdissolve    
    bt "What do you need?"
    $ seensneed = True
    jump SneedDialogues
if seensneed:
    show betty01 with dissolve
    bt "Welcome back, stranger. What do you need today?"
label SneedDialogues:

menu:
    "I need some feed":
        jump SneedFeed
    "I need some seed":
        jump SneedSeed
    "I need to... get back home.":
        hide betty01
        show betty03
        with fastdissolve
        bt "You need to GROW UP!"
        mc "I shall heed no such advice! Goodbye, ma'am."
        jump BackHex54
label SneedFeed:
bt "And what breed of steed do you have?"
mc "Err... I don't have any animals to be honest."
hide betty01
show betty03
with fastdissolve
bt "You're starting to get rather te-dious."
mc "Sorry indeed."
hide betty03
show betty01
with fastdissolve
jump SneedDialogues

label SneedSeed:
bt "I would have thought a strapping young man like you had plenty of seed already!"
mc "Yeah, okay, very funny. What seeds do you have? I need some salad seeds to be precise."
hide betty01
show betty02
with fastdissolve
bt "Yep, got that. Twenty bucks a bag."
menu:
    "Buy a bag" if money >= 20 and seedquest:
        hide betty02
        show betty01
        with fastdissolve
        $ money -= 20
        bt "I'll go and get it for you!"
        window hide
        hide betty01 with moveoutright
        mc "(Now I should be able to go back to Derek and try out his crazy plan to enter Trumpf City...)"
        show betty01 with moveinright
        bt "And... There it is. In your hands."        
        $ seedbag = True
        window hide
        show missionseedsuccess at posmission
        pause
        mc "A good deed done!"
        bt "Indeed. Have a good day, stranger!"
        hide betty01 with dissolve
        jump BackHex54        
    "Don't buy anything" if money >= 20:
        mc "This is too damn expensive! 20 bucks for some salad? What is this, a Wendy's or something?"
        hide betty02
        show betty03
        with fastdissolve
        bt "Our farm is radiation-organic! Our seeds are guaranteed 95\% radiation-free."
        mc "Well, I'll think about it then... Goodbye ma'am."
        bt "You seem to be a very needy person..."
        hide betty03 with dissolve
        jump BackHex54
    "I don't have enough money" if money <= 19:
        mc "This is too damn expensive! 20 bucks a salad? What is this, a Wendy's or something?"
        hide betty02
        show betty03
        with fastdissolve
        bt "Our farm is radiation-organic! Our seeds are guaranteed 95\% radiation-free."
        mc "Well, I'll think about it then... Goodbye ma'am."
        bt "You seem to be a very needy person..."
        hide betty03 with dissolve
        jump BackHex54

label BackHex54:
stop music
scene command01 with fade
show lena01
$ period += 1
if alone:
    le "So, what do you have to report about area F4, scout?"
if alone == False:
    le "So, what do you have to report about area F4, scouts?"
if seedbag:
    mc "I bought some salad seeds from an organic farm."
    hide lena01
    show lena03
    with fastdissolve
    le "Why would you do that? We have plenty of godam salads here as it is!"
    mc "Ah, but the catch is that it's not for the compound. It's to enter Trumpf City."
    hide lena03
    show lena06
    with fastdissolve    
    le "This sounds STOOPID. Dismissed!"
    hide lena06 with dissolve
    jump LeaveCommand
if seedbag == False:
    mc "I came across an organic farm."
    hide lena01
    show lenapensive
    with fastdissolve
    le "Interesting. That could be where the Trumpf Militia gets its food from... Maybe we should burn it to the ground."
    if mcwarrior == 5:
        mc "Okay! I'm a Road Warrior, I like doing that kind of stuff! When do we start?" 
        hide lenapensive
        show lena06
        with fastdissolve                
        le "Well, hang on a minute. We've got to make sure it's their source of food. So don't do anything just yet."
        mc "AAAAR! My Road Warrior anger just went down a notch."
        call MinusWarrior
        le "Too bad for you. DISMISSED!"
        jump LeaveCommand
    if mcwarrior <= 4:
        mc "Okay! I'm a Road Warrior, I like doing that kind of stuff! When do we start?" 
        hide lenapensive
        show lena06
        with fastdissolve                
        le "Well, hang on a minute. We've got to make sure it's their source of food. So don't do anything just yet."
        mc "AAAAR! My Road Warrior anger just went down a notch."
        call MinusWarrior
        le "Too bad for you. DISMISSED!"
        jump LeaveCommand

label ExploreHex55:
$ explored = True
$ exploredhex55 = True
$ clearedhex55 = True
stop sound
stop music
scene newaliens01 with fade
play music "Sounds/desertwind01.mp3"
mc "Looks like another empty and desolate h..."
window hide
scene newaliens01 blurred
play sound "v071/spaceship.mp3"
show alienship at alienshipmove
$ renpy.pause(2.0, hard='True')
mc "What the fuck? The aliens are back, the aliens are back!"
window hide
show alienshoot at aliensshoot01
play sound "Sounds/raygun.mp3"
$ renpy.pause(0.5, hard='True')
if withpe:
    mc "Argh, flee, Penny, turn around, turn around! Penny? Oh shit, they shot her!"
if withbe:
    mc "Argh, flee, Bella, turn around, turn around! Bella? Oh shit, they shot her!"
if alone and withnone:
    mc "Argh, flee, turn around, turn around! Ah, I'm trapped!"
if alone and withan:
    mc "Argh, flee, let's turn around, Hang on tight Angie! Angie? Oh, shit, they shot her!"
if alone and witham:
    mc "Argh, flee, let's turn around, Hang on tight Amy! Amy? Oh, shit, they shot her!"
if alone and withma:
    mc "Argh, flee, let's turn around, Hang on tight Marnie! Marnie? Oh, shit, they shot her!"
if alone and withmi:
    mc "Argh, flee, let's turn around, Hang on tight Michiko! Michiko? Oh, shit, they shot her!"
if alone and withcy:
    mc "Argh, flee, let's turn around, Hang on tight Cyrl! Cyrl? Oh, shit, they shot her!"
if alone and withmo:
    mc "Argh, flee, let's turn around, Hang on tight Nancy! Nancy? Oh, shit, they shot her!"
if alone and withru:
    mc "Argh, flee, let's turn around, Hang on tight Ruby! Ruby? Oh, shit, they shot her!"
if alone and withsu:
    mc "Argh, flee, let's turn around, Hang on tight Suki! Suki? Oh, shit, they shot her!"
if alone and withay:
    mc "Argh, flee, let's turn around, Hang on tight Ayla! Ayla? Oh, shit, they shot her!"
if alone and withza:
    mc "Argh, flee, let's turn around, Hang on tight Zara! Zara? Oh, shit, they shot her!"
if alone and withgw:
    mc "Argh, flee, let's turn around, Hang on tight Gwen! Gwen? Oh, shit, they shot her!"    
if alone and withcl:
    mc "Argh, flee, let's turn around, Hang on tight Clara! Clara? Oh, shit, they shot her!"    
if alone and withla:
    mc "Argh, flee, let's turn around, Hang on tight Laurie! Laurie? Oh, shit, they shot her!"    
if alone and withba:
    mc "Argh, flee, let's turn around, Hang on tight Barbara! Barbara? Oh, shit, they shot her!"    
if alone and withde:
    mc "Argh, flee, let's turn around, Hang on tight Debra! Debra? Oh, shit, they shot her!"    
    
scene newaliens02 with dissolve
mc "That's it, it's the END. I'm about to die. In a game where no one dies, what a pathetic death that will b..."
window hide
play sound "v071/spaceshipdoor.mp3"
show aliengirl01 at left with dissolve
show alien02girl01 at right with dissolve
alg01 "Oh my Glod, it's HIM!"
alg02 "Oh my Glod, oh my Glod, I'm wetting my panties right now, I'm so excited!"
hide aliengirl01
show aliengirl04 at left
with fastdissolve
alg01 "All the girls at Glorglimbo High are going to be sssooo jealous!"
hide alien02girl01
show alien02girl03 at right
with fastdissolve
alg02 "When we show them the pictures of us getting fucked by the biggest sex appendage in the galaxy!"
hide aliengirl04
show aliengirl01 at left
with fastdissolve
alg01 "Please give us an autograph, \"Earthling Stallion\"!"
if alone and withnone:
    mc "Err, yeah sure..."
    hide aliengirl01
    show aliengirl05 at left
    with fastdissolve    
    alg01 "This is so glexciting!"
    jump NewAlienDialogue
if withpe and withnone:
    mc "What have you done to Penny you murderous bitches?"
if withbe and withnone:
    mc "What have you done to Bella you murderous bitches?"
if withpe and withnone == False:
    mc "What have you done to Penny and my accompanying harem girl you murderous bitches?"
if withbe and withnone == False:
    mc "What have you done to Bella and my accompanying harem girl you murderous bitches?"
if alone and withnone == False:
    mc "What have you done to my accompanying harem girl you murderous bitches?"

hide alien02girl03
show alien02girl02 at right
with fastdissolve
alg02 "She's only stunned, don't get your knickers in a twist."
hide aliengirl01
show aliengirl02 at left
with fastdissolve
play sound "Sounds/raygun.mp3"
alg01 "And this is for calling us bitches, BIATCH!"
$ mcinjuredalien = True 
call MCInjury
hide alien02girl02
show alien02girl01 at right
with fastdissolve
hide aliengirl02
show aliengirl03 at left
with fastdissolve
alg02 "We ain't bitches, we're just normal sex-starved pre-teen Glorglans!"

label NewAlienDialogue:
menu:
    "Let me guess, you want me to give you ten zillion intergalactic babies?":
        if alone and withnone:
            hide aliengirl05
        hide aliengirl03
        show aliengirl07 at left
        with fastdissolve
        alg01 "Eeew, that's DISGUSTING! What a filthy boy you are!"
        if alone and withnone:
            hide alien02girl03
        hide alien02girl01
        show alien02girl04 at right
        with fastdissolve
        alg02 "We're only 11 and 12 Glorglyear-old you FREAK, we can't have babies yet!"
        alg01 "We just want a taste of your monster schlong, like all the preteen girls on our planet, that's all. So don't you dare try and impregnate us, you hear me?"
        mc "What's in it for me though?"
        hide aliengirl07
        hide alien02girl04        
    "Well, why aren't you naked like the previous aliens that came over here then?":
        if alone and withnone:
            hide aliengirl05
        hide aliengirl03
        show aliengirl07 at left
        with fastdissolve
        alg01 "Well, doh! We're only 11 and 12 Glorglyear-old, we can't walk around showing our naughty bits on Glorglon, we would end up in jail for glolicon entrapment!"
        if alone and withnone:
            hide alien02girl03
        hide alien02girl01
        show alien02girl03 at right
        with fastdissolve
        alg02 "However, on THIS pathetic planet, we can indulge in anything we want since you don't even have a functioning judiciary system!"
        hide aliengirl07
        show aliengirl04 at left
        with fastdissolve
        alg01 "That's what I LOVE about inferior alien species! Especially when the male specimen has such a great big whopper such as yourself!"
        mc "What's in it for me though?"
        hide aliengirl04
        hide alien02girl03        
    "So my intergalactic nickname is \"Earthling Stallion\"? Interesting...":
        if alone and withnone:
            hide aliengirl05
        hide aliengirl03
        show aliengirl04 at left
        with fastdissolve
        alg01 "Yes, you're the biggest Kunt-Popping Star on our planet!"
        alg02 "Your sex romps are watched by over 200 trillion delirious preteen Glorglan girls each week!"
        if alone and withnone:
            hide alien02girl03
        hide alien02girl01
        show alien02girl03 at right
        with fastdissolve
        alg02 "And we're the FIRST ones to find you and meet you in the flesh!"
        mc "What's in it for me though?"
        hide aliengirl04
        hide alien02girl03        


show aliengirl03 at left
show alien02girl02 at right
with fastdissolve
alg01 "What? You ask for something in return? When you have the opportunity to bang the two hottest girls of Glorglimbo High?"
mc "Wee, err.... I mean, I'm the star here, ain't I?"
hide alien02girl02
show alien02girl01 at right
with fastdissolve
alg02 "Fine, what do you want?"
menu:
    "Do you have some diamonds perhaps?":
        hide aliengirl03
        show aliengirl07 at left
        with fastdissolve
        alg01 "Diamonds? Pff, that's so cheap! Everyone in the galaxy knows Zircon is WAY more valuable!"
        hide alien02girl01
        show alien02girl04 at right
        with fastdissolve
        alg02 "Hang on, if this idiot wants diamonds, let's give him some and be done with it. We have tons of the filthy stuff in the cargo bay."
        $ aliendiamonds = True
        window hide
        show galaxygems at posmission
        $ renpy.pause(2.0, hard=True)
        pause
        hide galaxygems        
        hide alien02girl04
        show alien02girl03 at right
        with fastdissolve
        alg02 "And now that you got what you wanted, let's get NAKED and have some FUN!"        
    "I want to be paid. In dollars, not Glorgonubs.":
        alg01 "Alright, we'll give you 30 of your pitiful and useless dollars that we stole from some guy wandering the desert."
        mc "That's better, I'll definitely whore myself out to some intergalactic invasion force for that amount of money, no problemo."
        $ money += 30
        hide alien02girl01
        show alien02girl03 at right
        with fastdissolve
        alg02 "And now that you got what you wanted, let's get NAKED and have some FUN!"        
    "How about you lift that threat of destruction on my planet?":
        alg01 "Alright, I'll speak to my great-great granddad. He's the union rep for the Planet Destruction Task Force, so it should be no problem."
        $ planetlifted = True
        hide alien02girl01
        show alien02girl03 at right
        with fastdissolve
        alg02 "Now that you got what you wanted, let's get NAKED and have some FUN!"

hide aliengirl07
hide aliengirl03
show aliengirl06 at left
with fastdissolve
alg01 "So drop those trousers and show us your \"Earthling Stallion\" Megadong!"
hide alien02girl03
show alien02girl01 at right
with fastdissolve
alg02 "And we'll show you OUR MEGATONGUES!"
hide aliengirl06
hide alien02girl01
show aliengirl08 at left
show alien02girl05 at right
with fastdissolve
alg01 "Oh wow, it's just as BIG as I imagined it from those VHS videos!"
hide alien02girl05
show alien02girl06 at right
with fastdissolve
alg02 "I bet he can really fuck my tight purple pussy REAL DEEP!"
stop music
scene alienslick01 with dissolve
play music "Sounds/lick.mp3"
mc "Ooooh, how... How are you doing this?"
alg01 "Ggglll, our glllongues are... extendaglgggllle and ....pregglllhensile...."
scene alienslick02 with dissolve
alg02 "Glllyou like gglllthat , don't ya?"
mc "Oh damn, your tongues are... rubbing all over my shaft, it's sssooo goood!"
scene alienslick03 with dissolve
alg01 "We're the best cocklickers on Glorglon, that's why!"
stop music
play music "v071/alienslick.mp3"
show alienslickanim
call screen alienslickanim
screen alienslickanim:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AliensLickEnd")

label AliensLickEnd:
mc "God damn, I can't hold it any longer!"
scene alienslick04 with dissolve
stop music
mc "FUCK, AAAHH!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
alg02 "Glllast away!"
scene alienslick04 with fastflash
alg01 "Wglwe want gllbbmore! GLMUCH MORE!"
scene alienslick05 with dissolve
mc "You're PUMPING THE CUM OUT OF ME, OOOOH!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene alienslick05 with fastflash
mc "There's more, you're coaxing sso much spunk out of my sperm factories, RHAAA!"
scene alienslick06 with dissolve
stop sound
mc "Phew, you alien girls certainly know your way around a soda-thick shaft... With those tongues of yours. So, can I go now?"
alg01 "We're only JUST GETTING STARTED!"
scene aliens02prefuck01 with dissolve
play sound "Sounds/panting.mp3"
alg02 "You'd better have some MORE hot loads in those monster nuts of yours, earthling! Cos we ain't satisfied till we can show our friends your dong stuffed INSIDE our juicy pussies!"
mc "Stop it, you're choking me!"
alg01 "Will you FUCK ME GOOD? I NEED to know."
mc "Y...Yes, yes I WILL!"
alg02 "Let's check if this cock is truly ROCKHARD then..."
scene aliens02prefuck02 with dissolve
play sound "Sounds/slap.mp3"
alg01 "Oooh, I LIKED the sound of that massive slab of fuckmeat THUMPING your chest!"
mc "Then let me go and I'll show you what I can do with it! I'll fuck you girls so HARD I'll send your pussies back to whatever fucking galaxy you cray-ay-zy guys come from!"
alg02 "Oooh, is that so? Let him go Glaty, I want to see if he REALLY can deliver on this promise..."
alg01 "Bring that fat pussy-splitter over to my fuckhole! I'm gonna lie down on your filthy Earth, that'll make the sex even more DIRTY!"
scene alien01prefuck01 with dissolve
alg01 "I'm ready to receive your \"Earthling Stallion\" mega-dick inside my baby-hole!"
scene alien01prefuck02 with fastdissolve
play sound "v071/cockslap.mp3"
mc "Oh yeah? And how bad do you want it, hey?"
scene alien01prefuck01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene alien01prefuck02 with fastdissolve
play sound "v071/cockslap.mp3"
$ renpy.pause(0.4, hard=True)
scene alien01prefuck01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene alien01prefuck02 with fastdissolve
play sound "v071/cockslap.mp3"
$ renpy.pause(0.4, hard=True)
alg01 "Stop teasing me and SHOVE it in, please!"
scene alien01prefuck01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene alien01prefuck02 with fastdissolve
play sound "v071/cockslap.mp3"
$ renpy.pause(0.4, hard=True)
mc "And where should I come after I'm done with you, you dirty preteen Glorglan girl?"
scene alien01prefuck01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene alien01prefuck02 with fastdissolve
play sound "v071/cockslap.mp3"
$ renpy.pause(0.4, hard=True)
alg01 "Pump it all inside my baby-hole!"
mc "I thought you didn't want to get pregnant with zillions of spawns?"
alg02 "She's on the pill, silly! Every preteen is on the pill on Glorglon, until they reach 13 glorglyears. That's about 90 of your inferior years."
mc "You guys are CRAY-AY..."
alg01 "Stop talking and start FUCKING!"
scene aliensfuckanimb00
play music "Sounds/aliensex.mp3"
label Aliens01FuckSlow:
hide aliens01fuckfast
show aliens01fuckslow
call screen aliens01fuckslow01
screen aliens01fuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("Aliens01FuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("Aliens01FuckFast") 

label Aliens01FuckFast:
alg02 "Come on, show us why you're the biggest Kunt-Popping star on Glorglon, FUCK HER FASTER!"
hide aliens01fuckslow
show aliens01fuckfast
call screen aliens01fuckfast01
screen aliens01fuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("Aliens01FuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("Aliens01FuckSlow") 

label Aliens01FuckEnd:
alg01 "Oh, he's fucking me so good, AAAH, I'm coming AGAIN!"
alg02 "It's time for you to DELIVER, \"Earthling Stallion\"! Pump your sub-species seed inside her fuckhole, so I can have a go on that monster prong!"
mc "Just a sec... AAAH, yes, it's coming! I can feel it in my balls!"
scene alien01fuckcum01 with fastdissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
alg01 "I can feel it! He's pumping his Earthling seed inside me! AAAH!"
scene alien01fuckcum02 with dissolve
play sound "Sounds/splooge02.mp3"
mc "FUCK AAAAH! Damn it, you dirty preteen Glorglan sex-addict!"
window hide
with fastflash
show alien01fuckcum02b with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
alg02 "Your belly is SWELLING with his unending streams!"
window hide
with fastflash
alg01 "Yes, he's really DUMPING an INTERGALACTIC LOAD IN ME, I LOVE IT, AAAHH!"
scene alien01fuckcum03 with dissolve
play sound "Sounds/panting.mp3"
mc "Phew, I hope you don't get pregnant, I don't want to have to maintain ten zillions babies, I don't have enough money for that..."
alg02 "Enough of your nonsensical sub-species talk, I NEED that cock and I need it NOW!"
scene aliensprefuck01 with dissolve
alg02 "But first, let me make SURE this cock is EXTRA-HARD for me..."
mc "Oh God, what are you doing?"
play sound "Sounds/lick.mp3"
scene aliensprefuck02 with dissolve
alg02 "Hold him still while I suck his vital life essence out of him, Glaty!"
alg01 "He ain't going nowhere Glaren! Do it, SUCK HIM DRY!"
show alien02suck
play music "Sounds/hardsucking.mp3"
call screen alien02suck01
screen alien02suck01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("Alien02SuckEnd")    
label Alien02SuckEnd:
hide alien02suck
stop music
scene aliensprefuck04 with dissolve
alg02 "Yeah, that was a nice APPETIZER. Now let's move on to the REAL FUCK SESSION!"
alg01 "You heard her, \"Earthling Stallion\", get into the Gloglinary position!"
stop music

scene alien02prefuck01 with fastdissolve
$ renpy.pause(0.4, hard=True)
mc "That's it, I've had enough, now I'm in charge and I'm gonna POUND my prong into you!"
scene alien02prefuck02 with fastdissolve
play sound "v071/cockslap.mp3"
$ renpy.pause(0.4, hard=True)
mc "Hear that? That's the sound of my POWERFUL pussy-tamer! It can tame ANY pussy, even a Glorglan one!"
play sound "Sounds/moaning02.mp3"
alg02 "Oooh, you're such an intergalactic STUD!"
scene alien02prefuck01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene alien02prefuck02 with fastdissolve
play sound "v071/cockslap.mp3"
$ renpy.pause(0.4, hard=True)
scene alien02prefuck01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene alien02prefuck02 with fastdissolve
play sound "v071/cockslap.mp3"
$ renpy.pause(0.4, hard=True)
scene alien02prefuck01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene alien02prefuck02 with fastdissolve
play sound "v071/cockslap.mp3"
$ renpy.pause(0.4, hard=True)
mc "Damn right I am! Now get ready, I'm going to IMPALE you on this thing!"
alg01 "Fuck her HARD, I'll film everything with my mini-VHS camera for the girls back home!"

play music "Sounds/womansex01.mp3"
label Aliens02FuckSlow:
hide aliens02fuckfast
show aliens02fuckslow
call screen aliens02fuckslow01
screen aliens02fuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("Aliens02FuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("Aliens02FuckFast") 

label Aliens02FuckFast:
mc "So you like my stallion cock, hey, alien girl?"
alg02 "YES! I love it... It's sssooo massive!"
mc "Then let me shove it in even FASTER!"
hide aliens02fuckslow
show aliens02fuckfast
call screen aliens02fuckfast01
screen aliens02fuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("Aliens02FuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("Aliens02FuckSlow") 

label Aliens02FuckEnd:
mc "Oh, I'm getting close!"
alg01 "Give her all you've got left of your babyjuice \"Earthling Stallion\", we want to show our friends how we coaxed THREE HUGE NUTLOADS OUT OF YOU!"
stop music
scene alien02fuckcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "That's it, take it you little alien sex-fiend!"
window hide
with fastflash
alg02 "PLASTER me with it, I want to have a photo of me taken with your earthling juices ALL OVER ME!"
scene alien02fuckcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "That's for you then, RHAAA!"
window hide
with fastflash

scene alien02fuckcum03 with dissolve
play sound "Sounds/moaning.mp3"
alg02 "I'm CAKED in his HOT baby-cream...Aaaah..."
alg01 "You did good, just as we expected, \"Earthling Stallion\"... Now let's get dressed, we don't want to be seen like this on this filthy planet."
scene newaliens02
show aliengirl05 at left
show alien02girl01 at right
with fastdissolve
mc "So, what channel will this hot romp be aired on?"
hide aliengirl05
show aliengirl04 at left
with fastdissolve
alg01 "Channel? Oh boy, you're such an old-timer! Even if you're only 2 Glorglyear-old..."
hide alien02girl01
show alien02girl02 at right
with fastdissolve
alg02 "Doh! We'll be streaming it on our galactic FikFok account OBVIOUSLY!"
hide aliengirl04
show aliengirl03 at left
with fastdissolve
alg01 "Glaren, let's leave this planet, it's full of total losers."
$ money += 20
mc "Hey! We're not losers, we're WINNING! Even getting tired of it actually."
hide alien02girl02
show alien02girl04 at right
with fastdissolve
alg02 "Wha-tever! See you old-timer. In your GRAVE!"
window hide
hide alien02girl04
hide aliengirl03
with dissolve
play sound "v071/spaceship.mp3"
scene newaliens01 blurred
show alienship at alienshipmoveout
$ renpy.pause(2.0, hard='True')
mc "Thanks God they're gone. FOR GOOD!"
if withpe and withnone:
    mc "Let me check on Penny to make sure she's okay and let's go back home..."
if withpe and withan:
    mc "Let me check on Penny and Angie to make sure they're okay and let's go back home..."
if withpe and witham:
    mc "Let me check on Penny and Amy to make sure they're okay and let's go back home..."
if withpe and withma:
    mc "Let me check on Penny and Marnie to make sure they're okay and let's go back home..."
if withpe and withsu:
    mc "Let me check on Penny and Suki to make sure they're okay and let's go back home..."
if withpe and withmo:
    mc "Let me check on Penny and Nancy to make sure they're okay and let's go back home..."
if withpe and withcy:
    mc "Let me check on Penny and Cyrl to make sure they're okay and let's go back home..."
if withpe and withru:
    mc "Let me check on Penny and Ruby to make sure they're okay and let's go back home..."
if withpe and withmi:
    mc "Let me check on Penny and Michiko to make sure they're okay and let's go back home..."
if withpe and withay:
    mc "Let me check on Penny and Ayla to make sure they're okay and let's go back home..."
if withpe and withza:
    mc "Let me check on Penny and Zara to make sure they're okay and let's go back home..."
if withpe and withcl:
    mc "Let me check on Penny and Clara to make sure they're okay and let's go back home..."
if withpe and withgw:
    mc "Let me check on Penny and Gwen to make sure they're okay and let's go back home..."
if withpe and withla:
    mc "Let me check on Penny and Laurie to make sure they're okay and let's go back home..."
if withpe and withba:
    mc "Let me check on Penny and Barbara to make sure they're okay and let's go back home..."
if withpe and withde:
    mc "Let me check on Penny and Debra to make sure they're okay and let's go back home..."
if withbe and withan:
    mc "Let me check on Bella and Angie to make sure they're okay and let's go back home..."
if withbe and witham:
    mc "Let me check on Bella and Amy to make sure they're okay and let's go back home..."
if withbe and withma:
    mc "Let me check on Bella and Marnie to make sure they're okay and let's go back home..."
if withbe and withsu:
    mc "Let me check on Bella and Suki to make sure they're okay and let's go back home..."
if withbe and withmo:
    mc "Let me check on Bella and Nancy to make sure they're okay and let's go back home..."
if withbe and withcy:
    mc "Let me check on Bella and Cyrl to make sure they're okay and let's go back home..."
if withbe and withru:
    mc "Let me check on Bella and Ruby to make sure they're okay and let's go back home..."
if withbe and withmi:
    mc "Let me check on Bella and Michiko to make sure they're okay and let's go back home..."
if withbe and withay:
    mc "Let me check on Bella and Ayla to make sure they're okay and let's go back home..."
if withbe and withza:
    mc "Let me check on Bella and Zara to make sure they're okay and let's go back home..."
if withbe and withcl:
    mc "Let me check on Bella and Clara to make sure they're okay and let's go back home..."
if withbe and withgw:
    mc "Let me check on Bella and Gwen to make sure they're okay and let's go back home..."
if withbe and withla:
    mc "Let me check on Bella and Laurie to make sure they're okay and let's go back home..."
if withbe and withba:
    mc "Let me check on Bella and Barbara to make sure they're okay and let's go back home..."
if withbe and withde:
    mc "Let me check on Bella and Debra to make sure they're okay and let's go back home..."
if alone and withan:
    mc "Let me check on Angie to make sure she's okay and let's go back home..."
if alone and witham:
    mc "Let me check on Amy to make sure she's okay and let's go back home..."
if alone and withma:
    mc "Let me check on Marnie to make sure she's okay and let's go back home..."
if alone and withmi:
    mc "Let me check on Michiko to make sure she's okay and let's go back home..."
if alone and withcy:
    mc "Let me check on Cyrl to make sure she's okay and let's go back home..."
if alone and withmo:
    mc "Let me check on Nancy to make sure she's okay and let's go back home..."
if alone and withru:
    mc "Let me check on Ruby to make sure she's okay and let's go back home..."
if alone and withsu:
    mc "Let me check on Suki to make sure she's okay and let's go back home..."
if alone and withay:
    mc "Let me check on Ayla to make sure she's okay and let's go back home..."
if alone and withza:
    mc "Let me check on Zara to make sure she's okay and let's go back home..."
if alone and withgw:
    mc "Let me check on Gwen to make sure she's okay and let's go back home..."
if alone and withcl:
    mc "Let me check on Clara to make sure she's okay and let's go back home..."
if alone and withla:
    mc "Let me check on Laurie to make sure she's okay and let's go back home..."
if alone and withba:
    mc "Let me check on Barbara to make sure she's okay and let's go back home..."
if alone and withde:
    mc "Let me check on Debra to make sure she's okay and let's go back home..."
if alone and withnone:
    mc "Let's go back home... Not sure what I'll tell Chief Lena. I'll probably lie as usual."

label BackHex55:
stop sound
stop music
$ period += 1
scene command01
show lena01
with fade
le "So, what do you have to report about hex F5?"    
mc "More illegal aliens pouring into our country. We really ought to build a wall. In the sky."
hide lena01
show lena03
with fastdissolve
if withpe: 
    le "What is this nonsense? Penny, what did you see exactly?"
    pe "I... I was knocked unconscious by something... I need to go to the medbay actually, my head still hurts."
    if planetlifted:
        mc "That was the actual SPACE aliens I'm talking about! Fortunately, I saved the day by fucking them senseless and now our planet is safe."
    if planetlifted == False:
        mc "That was the actual SPACE aliens I'm talking about! Fortunately, I saved the day by fucking them senseless and so they left covered in my \"Earthling Stallion\" cum."
    hide lena03
    show lena05
    with fastdissolve
    le "I see, you have a concussion. Go to the medbay and get some heavy medicine from Nurse Rachel to clear your mind, you are delusional."
    mc "Why won't anyone believe me here?"
    jump Medbay
if withbe: 
    le "What is this nonsense? Bella, what did you see exactly?"
    be "I... I was knocked unconscious by something... I need to go to the medbay actually, my head still hurts."
    if planetlifted:
        mc "That was the actual SPACE aliens I'm talking about! Fortunately, I saved the day by fucking them senseless and now our planet is safe."
    if planetlifted == False:
        mc "That was the actual SPACE aliens I'm talking about! Fortunately, I saved the day by fucking them senseless and so they left covered in my \"Earthling Stallion\" cum."
    hide lena03
    show lena05
    with fastdissolve
    le "I see, you have a concussion. Go to the medbay and get some heavy medicine from Nurse Rachel to clear your mind, you are delusional."
    mc "Why won't anyone believe me here?"
    jump Medbay
if alone:
    le "What is this nonsense? In the sky???"
    if planetlifted:
        mc "Yeah, cos I meant I saw ACTUAL aliens. Like from outer space. Fortunately, I saved the day by fucking them senseless and now our planet is safe."
    if planetlifted == False:
        mc "Yeah, cos I meant I saw ACTUAL aliens. Like from outer space. Fortunately, I saved the day by fucking them senseless and so they left covered in my \"Earthling Stallion\" cum."
if withnone:
    hide lena03
    show lena05
    with fastdissolve
    le "And you have witnesses to your glorious Earth-saving romp?"
    mc "Err, no. I went there alone and I conquered alone."
    le "*sigh*. You now what I'm about to say?"
    mc "That I'm dismissed?"
    hide lena05
    show lena10
    with fastdissolve
    le "That's right. SCOUT DISMISSED!"
    if mcinjured:
        le "...To the medbay!"
        mc "Ah, I see you noticed I got injured then..."
        jump Medbay
    hide lena10 with dissolve
    jump LeaveCommand            
if withnone == False:
    hide lena03
    show lena05
    with fastdissolve
    le "And your accompanying harem girl can corrobate your delusional rant?"
    mc "Err, no. No, she can't. Because they stunned her and she didn't actually get to see my heroic sexual exploits."
    le "*sigh*. You now what I'm about to say?"
    mc "That I'm dismissed?"
    hide lena05
    show lena10
    with fastdissolve
    le "That's right. SCOUT DISMISSED!"
    if mcinjured:
        le "...To the medbay!"
        mc "Ah, I see you noticed I got injured then..."
        jump Medbay
    hide lena10 with dissolve
    jump LeaveCommand        

label ExploreHex61:
scene quebec01 with fade

if exploredhex61 == False:
    mc "That's a big forest. And it looks super-realistic, almost like it's a real photograph. The dev really outdid himself on that render."
    if withbe:
        be "Either that or he couldn't be bothered and actually used a REAL photograph."
    if withpe:
        pe "Either that or he couldn't be bothered and actually used a REAL photograph."
    mc "Na, he wouldn't do such a thing, that would be quite offensive to the players. In any case, those trees are like super-tall too!"
    if withbe:
        be "Maybe because of radiation? Who knows what that stuff did to plants..."
    if withpe:
        pe "Maybe because of radiation? Who knows what that stuff did to plants..."
    mc "I'll go deeper in there just to check but I doubt I'll find anything."

if exploredhex61 and clearedhex61:
    mc "Back at the big Canadian forest. Hope Paulette is in for some HOT SEX."
    jump CanadaBackWorked

if exploredhex61 and workcanadaagree:
    mc "Back at the big Canadian forest. Good thing they didn't build a wall like we tried."
    jump CanadaBackWork

if exploredhex61 and workcanadaagree == False and metqu:
    mc "Back at the big Canadian forest. Good thing they didn't build a wall like we tried."    
    jump CanadaBackNoWork

if exploredhex61 and metqu == False:
    mc "Back at the big Canadian forest. Good thing they didn't build a wall like we tried."
    jump CanadaBack

$ exploredhex61 = True
scene quebec02 with dissolve
mc "Hang on, this looks like a campsite, so somebody must be nearby..."
window hide
show paulette01 with moveinright
qu "Bonjour... (in French) Who are you and what are you doing here in Canada?"
if frenchovermax >= 1:
    mc "(I actually understood this French-Canadian chick. I must be getting pretty good at this useless language.)"
    mc "(in French) Err. My name is [name] and I'm the hero of this fucked-up world. Looking to overthrow Trumpf. Not Cluedeau, you can keep him. Don't let colonel Mustard near him though."
    label PauletteFrench:
    hide paulette01
    show paulette03
    with fastdissolve    
    qu "(in English). Ah, I see we have a connoisseur of Cartier's language here. I will therefore switch to your arrogant overreaching language. English, that is."
    hide paulette03
    show paulette05
    with fastdissolve    
    qu "My name is Paulette and you are in my home forest of Québec. Although I hear some people *snickers* call it hex G1."
    $ metqu = True
    mc "So what are you, some kind of lumberjack? Didn't even know we still had trees."
    hide paulette05
    show paulette03
    with fastdissolve    
    qu "Well, YOU don't have trees. WE still have plenty here in Canada. And they've grown even larger thanks to radiation fallouts. I was aboot to cut this 200ft-tall bonsai actually."
    jump CanadaPre
    
if mcfrench <= 10:
    mc "Err... Moi, American, A-ME-RI-CAN. Do you speak English?"
    hide paulette01
    show paulette02
    with fastdissolve
    qu "(in English) I refuse to speak English to you until you've PROVEN to me that you made the effort of learning some French. (in French) Tabarnacle!"
    mc "But you just did. Speak English. Just now."
    hide paulette02
    show paulette01
    with fastdissolve
    qu "(in English) That was only aboot explaining things to you. It didn't count."
    mc "You did it again! Come on, you can clearly speak English, so stop pretending you can't! Canadians speak English, godammit!"
    hide paulette01
    show paulette04
    with fastdissolve
    qu "(in French) Quoi? I don't understand, sorry, I don't speak your language. Please speak French."
    mc "(Clearly, I ain't going nowhere with this stubborn French-Canadian chick until I get better at French...)"
    mc "Err... Au revoir."
    hide paulette04
    show paulette03
    with fastdissolve    
    qu "We hope you enjoyed your stay in Canada. Come back again soon."
    mc "Not really, no, I didn't."
    if persistent.tipson:
        show quebectip at tips with dissolve
        pause
        hide quebectip
    jump BackHex61

label CanadaPre:
qu "You look puny, American boy."
if mcstrength == 15:
    mc "Puny? I've already reached my max strength of 15! I'm like SUPER-HUMAN strong?"
    qu "Oh yeah? I bet you could become stronger if you worked with me here for a while."
    scene quebec02 blurred
    show pauletteflex01
    with dissolve
    play sound "Sounds/womangroan.mp3"
    qu "Look at MY NATURAL MUSCLES! What aboot THAT?"
    hide pauletteflex01
    show pauletteflex02
    with dissolve
    qu "And those abs... What aboot THEM?"
    mc "FUCK ME! Err, OK, what would that entail?"
    hide pauletteflex02
    show paulette03
    with dissolve
    label PauletteWorkTalk:
    qu "You just come here and help me clear this forest. Three FULL working days should be sufficient for both of us."
    menu:
        "Agree":
            $ workcanadaagree = True
            mc "Alright, can we start now then?"
            if period == 1:
                hide paulette03
                show paulette05
                with fastdissolve    
                qu "We sure can, since it's only morning. Take this axe and let's get's get to work. What's your name, puny boy?"
                mc "[name]. And I'm NOT puny!"
                qu "We'll see aboot that."
                if alone == False:
                    mc "Ah, but I came with a scout I remember now... Can't leave her for that long, so I'll have to come back another day alone."
                    hide paulette05
                    show paulette03
                    with fastdissolve                        
                    qu "Fine, lad, come back here in the morning, I'll be waiting for you, probably already chopping down trees."
                    jump BackHex61
                jump CanadaFirst                
            if period == 2:
                qu "It's already too late for a FULL working day. Come back here in the morning, lad, and we can get on with the work. Come back ALONE."
                mc "Alright, I get it."
                hide paulette03
                show paulette05
                with fastdissolve                    
                qu "We hope you enjoyed your stay in Canada. Come back again soon."                
                jump BackHex61
        "Let me think about this":
            hide paulette03
            show paulette01
            with fastdissolve    
            qu "I should have know a puny boy like you would CHICKEN OUT! Get out of here!"
            mc "Well, that's just rude!"
            qu "We hope you enjoyed your stay in Canada. Come back again soon."
            jump BackHex61

if mcstrength <= 14:
    mc "Well, I still have some strength to gain, I'm not at my max strength of 15 yet."
    qu "Well, that's not enough to work as a lumberjack like me. You need to have EXTRA-BIG muscles for this job."
    mc "Pff, my muscles are plenty big enough!"
    scene quebec02 blurred
    show pauletteflex01
    with dissolve
    play sound "Sounds/womangroan.mp3"
    qu "Are they as big as this? Look at MY NATURAL MUSCLES! What aboot THAT?"
    hide pauletteflex01
    show pauletteflex02
    with dissolve
    qu "And those abs... What aboot THEM? I don't need a puny boy like you around here. I need a REAL man!"
    mc "FUCK ME! Err, I guess I'll come back when I hit strength of 15 then..."
    hide pauletteflex02
    show paulette03
    with dissolve
    qu "That's better. When you do, I might have a job for you... Until then, go away."
    mc "Well, that's a bit rude."
    qu "We hope you enjoyed your stay in Canada. Come back again soon."
    jump BackHex61

label CanadaFirst:
$ workcanada += 1
scene quebec03
show paulettelumberjack00 
with dissolve
qu "So, are you ready to cut down trees and to skip and jump?"
mc "Sure, I'm ready."
window hide
play music "v081/lumberjack.mp3"
hide paulettelumberjack00
show mclumberjack01a
show paulettelumberjack01a
with dissolve
$ renpy.pause(0.5, hard=True)
hide paulettelumberjack01a
hide mclumberjack01a
show paulettelumberjack01b
show mclumberjack01b
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide paulettelumberjack01b
hide mclumberjack01b
show mclumberjack01a
show paulettelumberjack01a
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide paulettelumberjack01a
hide mclumberjack01a
show paulettelumberjack01b
show mclumberjack01b
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide paulettelumberjack01b
hide mclumberjack01b
show mclumberjack01a
show paulettelumberjack01a
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide paulettelumberjack01a
hide mclumberjack01a
show paulettelumberjack01b
show mclumberjack01b
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide paulettelumberjack01b
hide mclumberjack01b
show paulettelumberjack03
show mclumberjack03
with dissolve
$ renpy.pause(1.0, hard=True)
hide paulettelumberjack03
hide mclumberjack03
show paulettelumberjack02a
show mclumberjack02a
with dissolve
$ renpy.pause(0.5, hard=True)
hide paulettelumberjack02a
hide mclumberjack02a
show paulettelumberjack02b
show mclumberjack02b
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide paulettelumberjack02b
hide mclumberjack02b
show paulettelumberjack02a
show mclumberjack02a
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide paulettelumberjack02a
hide mclumberjack02a
show paulettelumberjack02b
show mclumberjack02b
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide paulettelumberjack02b
hide mclumberjack02b
show paulettelumberjack03
show mclumberjack03
with fastdissolve
$ renpy.pause(1.0, hard=True)
hide paulettelumberjack03
hide mclumberjack03
show paulettelumberjack04a
show mclumberjack04a
with dissolve
$ renpy.pause(1.0, hard=True)
hide paulettelumberjack04a
hide mclumberjack04a
show paulettelumberjack04b
show mclumberjack04b
with dissolve
$ renpy.pause(0.5, hard=True)
hide paulettelumberjack04b
hide mclumberjack04b
show paulettelumberjack04c
show mclumberjack04a
with dissolve
$ renpy.pause(1.0, hard=True)
hide paulettelumberjack04c
hide mclumberjack04a
show paulettelumberjack04b
show mclumberjack04b
with dissolve
$ renpy.pause(0.5, hard=True)
hide paulettelumberjack04b
hide mclumberjack04b
show paulettelumberjack04c
show mclumberjack04a
with dissolve
$ renpy.pause(1.0, hard=True)
hide paulettelumberjack04c
hide mclumberjack04a
show paulettelumberjack04b
show mclumberjack04b
with dissolve
$ renpy.pause(0.5, hard=True)
hide paulettelumberjack04b
hide mclumberjack04b
show paulettelumberjack04c
show mclumberjack04a
with dissolve
$ renpy.pause(1.0, hard=True)
stop music
scene quebec04
show paulettelumberjack00 
with dissolve
$ period += 1
qu "Well done [name], I think we've worked enough for today, we've cleared a bit of that forest."
call LustPlusPaulette
mc "I notice indeed that a couple of trees are gone from the previous background pic."
qu "You can go back to your country now. I need to clean myself in the river. The rugged Canadian way."
mc "Sure. See you soon for another day of hard rugged labor Paulette!"
hide paulettelumberjack00 with fastdissolve
mc "(I might take a detour on my way back and see if I can find the spot where she cleans herself. Naked hopefully!...)"
scene quebecriver01 with fade
play music "v081/river.mp3"
mc "Oh, there she is, cleaning herself up in the river. Let's hide and spy on her. Like a pervy MC..."
scene quebecriver02 with dissolve
mc "Damn, that girl has some MUSCLES on her!"
scene quebecriver03 with dissolve
mc "...And some TITS!"
scene quebecriver04 with dissolve
mc "Best to leave now before she sees me though..."
jump BackHex61

label CanadaBackNoWork:
scene quebec02
show paulette01
with dissolve
qu "So, are you going to start being a REAL man and work as a Canadian lumberjack with me?"
if mcstrength <= 14:
    mc "Err, no, cos I came back even though my strength still hasn't reached 15."
    hide paulette01
    show paulette02
    with fastdissolve
    qu "Well, that was a waste of time, wasn't it?"
    mc "I guess so... I'll just... show myself out."
    hide paulette02
    show paulette05
    with fastdissolve
    qu "We hope you enjoyed your stay in Canada. Come back again soon."
    jump BackHex61
if mcstrength == 15:
    mc "I'm strong enough for it. What does it entail again remind me?"
    hide paulette01
    show paulette03
    with fastdissolve    
    jump PauletteWorkTalk

label CanadaBack:
scene quebec02
show paulette01
with dissolve
qu "(in French). Alors? Are you going to start speaking the PROPER Canadian language or you are still USELESS in French?"
if frenchovermax >= 1:
    mc "(in French) Of course, Mademoiselle, I speak French fluently now, voilà!"    
    jump PauletteFrench
if mcfrench <= 10:
    mc "( * Still don't understand a word she's saying... * )"
    hide paulette01
    show paulette02
    with fastdissolve
    qu "I guess the answer is \"non\"..."
    hide paulette02 with moveoutright
    mc "What, she just left like that? How RUDE!"
    jump BackHex61
    
label CanadaBackWork:
scene quebec02 with dissolve
window hide
show paulette01 with moveinright 
if period == 1:
    qu "Ah there you are [name]. So are you ready to work in the great outdoors?"
    mc "Sure, that's why I'm here Paulette."
    qu "Then follow me..."
    if workcanada == 0:
        jump CanadaFirst
    if workcanada == 1:
        jump CanadaSecond
    if workcanada == 2:
        jump CanadaThird
if period == 2:
    qu "Ah there you are [name]."
    hide paulette01
    show paulette02
    with fastdissolve
    qu "But you're LATE. I specifically told you to come in the MORNINGS. What did you not understand aboot THAT?"
    mc "Ah. I forgot. My mistake. I'll show myself out then."
    hide paulette02
    show paulette03
    with fastdissolve
    qu "We hope you enjoyed your stay in Canada. Come back again soon."
    jump BackHex61

label CanadaBackWorkedb:
scene quebec02 with dissolve
window hide
show paulette05b with moveinright 
qu "And what brings you back here [name]?"
hide paulette05b
show paulette01b
with fastdissolve
qu "And why are you wearing a Captain America costume? You can't scare me, I'm Canadian!"
mc "I need your help to beat a horrible monster and enter Trumpf City, Paulette. And he's too strong for me alone so we'll have to form a team. A team of SUPER-HEROES!"
if lustqu <= 3:
    hide paulette01b
    show paulette02b
    with fastdissolve        
    qu "Well, maybe you should have thought aboot that BEFORE you came to see me with such a LOW lust level!"
    mc "Are you telling me I came all the way over here for NOTHING?"
    qu "That's EXACTLY what I'm saying."
    wi "Oh, well done Captain America... Thanks for WASTING the valuable time of the Black Widow! I'm going back to my secret lair."
    mc "Okay, okay, I'll... get her lust level up by coming back here alone and having some...err... special time with her and we can come back another time..."
    $ period += 1
    scene command01
    show lena01
    with fade
    le "So, what do you have to report about area G2, scouts?" 
    mc "Err.. Nothing. Same as usual. Trees and stuff."
    hide lena01
    show lena06
    with fastdissolve
    le "I see. You FAILED in whatever it is you were planning on doing there, didn't you?"
    mc "Errr. Yeah. Pretty much sums it up."
    le "DISMISSED!"
    hide lena06 with dissolve
    jump LeaveCommand        
show marvelcanada01 at farleft02 with moveinleft
hide paulette01b
show paulette02b
with fastdissolve
mc "Meet Captain Marvel!"
show widowcanada01 at farright03 with moveinright
mc "And the Black Widow!"
hide paulette02b
show pauletteprecanuck01b
with fastdissolve
qu "You're sure aboot that? She looks like Scarlett Johansson to me..."
hide widowcanada01
show widowcanada02 at farright03
with fastdissolve
wi "Well, fine, I'm really Scarlett Johannson, but I'm the LEADER of the New Avengers! So there."
hide pauletteprecanuck01b
show paulette03b
with fastdissolve        
qu "In that case, it is time for me to reveal the seat of my incredible strength for I am none other than..."
window hide
show geniesmoke
play sound "Sounds/smokepuff.mp3"
$ renpy.pause(.5, hard=True)
hide geniesmoke 
hide paulette03b
show paulettecanuck01bb
show geniesmoke
with fastdissolve
hide geniesmoke 
hide paulettecanuck01bb
show paulettecanuck01cb
show geniesmoke
with fastdissolve
hide geniesmoke 
hide paulettecanuck01cb
hide marvelcanada01
show paulettecanuck01d
show marvelcanada02 at farleft02
with fastdissolve
qu "...Captain Canuck!"
play sound "Sounds/dundun.mp3"
$ renpy.pause(1.0, hard=True)    
hide widowcanada02
show widowcanada03 at farright03
with fastdissolve
wi "Captain who?"
mc "Is that even an actual superhero name???"
hide paulettecanuck01d
show paulettecanuck02b
with fastdissolve
play sound "v09/canada.mp3"
qu  "YES! Look it up, it's a FAMOUS Canadian Superhero!"
qu "And the dev painstakingly designed the texture of this costume, so stop taking the piss out of Canada or Captain Canuck will come and whip your American asses!"
mc "Alright, alright, sorry if I offended you Paul... I mean Captain Canuck. You are welcome to join the New Avengers."
hide widowcanada03
show widowcanada01 at farright03
with fastdissolve
wi "Umpf. I was supposed to say that. I'm the LEADER of the New Avengers, remember?"
hide marvelcanada02
show marvelcanada01 at farleft02
with fastdissolve
mo "Maybe we should go to... wherever it is we're supposed to go to, sweetie pie. I need to go back to the compound soon to prepare the salads."
hide paulettecanuck02b
show paulettecanuck01d
with fastdissolve
qu "That's some superheroes you've got there... *snickers*"
hide widowcanada01
show widowcanada03 at farright03
with fastdissolve
wi "Okay everyone, NEW AVENGERS are GO!"
if withbe:
    mc "There should be enough space with Bella's rig for all of us  to drive there in no time!"
if withpe:
    mc "There should be enough space with Penny's rig for all of us  to drive there in no time!"
jump NorthGateAvengers

label CanadaBackWorked:
scene quebec02 with dissolve
window hide
show paulette05 with moveinright 
qu "And what brings you back here [name]?"
hide paulette05
show pauletteflex01 with fastdissolve
qu "Is it perhaps those HUGE muscles? *wink*"    
mc "Which are a perfect match for MY huge muscle!"
hide pauletteflex01
show pauletteflex02 with fastdissolve
qu "I see where you're getting at... You want some HOT MUSCLE SEX, don't you?"
mc "Damn right I do!"
qu "Then get your kit off and let's do it in the cleared forest!"
$ fuckedpaulettegain = True
jump PaulettePreSex
label CanadaSecond:
$ workcanada += 1
scene quebec04
show paulettelumberjack00 
with dissolve
qu "You'll see, you'll get used to it and you'll get stronger eventually. Aboot as strong as ME perhaps!"
window hide
play music "v081/lumberjack.mp3"    
call Lumberjack
$ period += 1
scene quebec05
show paulettelumberjack00 
with dissolve
qu "I think we've worked enough for today, we've cleared a bit more of that forest."
mc "I notice indeed that a couple MORE trees are gone from the previous background pic."
qu "We were faster than last time. You have time to get cleaned up in the river with me before heading back to your country [name]? *wink*"
mc "Sure! I'm all dirty, I need a THOROUGH cleaning."
hide paulettelumberjack00 
show paulettelumberjack01 
with fastdissolve
qu "Then follow me to the river. And get your clothes off once we get there."

scene quebecriver02 with dissolve
play music "v081/river.mp3"
qu "You know, I saw you the other day."
scene quebecriver03 with dissolve
qu "...Spying on me while I was naked..."
mc "Err, I just stumbled upon you on my way back, it was not intentional and I didn't stay more than four pics, I swear!"
scene quebecriver04 with dissolve
qu "Well, maybe this time, you'll get a few more pics. I mean more \"peeks\"."
mc "(* Alright! *)"
scene quebecriver05 with dissolve
qu "Do you always get a blood rush down to your cock when you bathe with a MUSCLED lass?"
mc "Oh, shit, I didn't realize..."
scene quebecriver06 with dissolve
qu "...That you were sporting a great big hardon next to me?"
mc "Err..."
qu "Let'ts see if your other muscles are as BIG as this one... Let's compare biceps."
mc "Right... Okay..."
scene quebecriver07 with dissolve
mc "(* need... to... flex... MIGHTILY! *)"
play sound "Sounds/mcworkout.mp3"
scene quebecriver08 with dissolve
qu "You can try as hard as you want, BOY, I'm BIGGER than you..."
mc "I... realize that."
qu "For being such a puny American boy, KISS MY BICEPS."
mc "Wh... What?"
qu "I said KISS IT!"
scene quebecriver09 with dissolve
play sound "Sounds/kiss.mp3"
qu "That's right, kiss those superior muscular BOULDERS and worship them!"
play sound "Sounds/kiss.mp3"
qu "Your cock is getting even harder, isn't it [name]?"
scene quebecriver10 with dissolve
qu "I think you need to UNLOAD then, don't you? I'll make sure you spill your seed on sacred Canadian soil!"
mc "Oh fuck! Your grip is so TIGHT on my shaft!"
qu "I'll show you what a REAL handjob feels like!"
play channel1 "Sounds/wank.mp3"
play channel2 "Sounds/panting.mp3"
label PauletteWankSlow:
hide paulettewankfast
show paulettewankslow
call screen paulettewankslow01
screen paulettewankslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PauletteWankEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PauletteWankFast") 

label PauletteWankFast:
qu "You like that, dirty boy, don't you? I'll make you EXPLODE in no time, you'll see..."
hide paulettewankslow
show paulettewankfast
call screen paulettewankfast01
screen paulettewankfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PauletteWankEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PauletteWankSlow") 

label PauletteWankEnd:
stop channel1
stop channel2
hide paulettewankslow
hide paulettewankfast
show paulettewankcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH!"
with fastflash
qu "That's it, get it all out [name]!"
scene paulettewankcum02 with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
qu "Nice! You really needed to unload those balls, didn't you, DIRTY BOY?"
with fastflash
mc "You... AAAHH? made me COME like that!"
scene paulettewankcum03 with fastdissolve
qu "Still MORE? That's a load for the record..."
with fastflash
mc "I'm... done, you've drained me..."
play sound "Sounds/panting.mp3"
call LustPlusPaulette
qu "You made a right mess and you're all dirty again. What aboot I lick some cum off your chest and help you clean up?"
scene paulettewankcum04 with fastdissolve
play sound "Sounds/lick.mp3"
mc "Oh Paulette, this is so fucking hot..."
qu "Mmh... *slurp*.... Do you know what a French-Canadian kiss is?"
mc "Err... A French kiss that tastes of maple syrup?"
qu "No silly boy..."
scene paulettewankcum05 with fastdissolve
qu "THIS is a French-Canadian kiss!"
play sound "Sounds/kiss.mp3"
mc "Ah, so a French kiss that tastes of cum then."
scene quebecriver11 with fastdissolve
qu "Now go back to your country [name] or you'll be late. For whatever it is you Americans do in the evenings."
mc "And what will YOU do Paulette? *wink*"
qu "I've got some Netflix DVDs."
jump BackHex61b   
    
label CanadaThird:
$ clearedhex61 = True
scene quebec05
show paulettelumberjack00 
with dissolve
qu "You'll see, you'll get used to it and you'll get stronger eventually. Aboot as strong as ME perhaps!"
window hide
play music "v081/lumberjack.mp3"    
call Lumberjack
$ period += 1
scene quebec06
show paulettelumberjack00 
with dissolve
qu "We did it! I have enough wood now to build myself a cabin. Can you feel your strength increasing?"
mc "Hang on..."
if mcstrength == 15:
    window hide
    play sound "Sounds/skill.mp3"
    show plusmaxstrength at posskill
    $ renpy.pause(2.0, hard=True)
    mc "FUCK YEAH! MAX STRENGTH of 16!"
    hide plusmaxstrength
    $ mcmaxstrength = True
    qu "Still not as much as ME!"
    jump PauletteThird
if mcstrength <= 14:
    call PlusStrength
mc "FUCK YEAH!"
label PauletteThird:
qu "Since you're super-strong now, we can have super-dirty sex. No need to clean ourselves, I want it RAW!"
mc "Alright, I'm in Paulette!"
hide paulettelumberjack00 
show paulettelumberjack01 
with fastdissolve
qu "Let's do it over there. Get your kit off and your cock HARD! I need some SEXERCISE!"

label PaulettePreSex:
scene quebec08
show paulettepresex01
with dissolve
qu "Here is good. Under the arch."
scene quebec08 blurred
show paulettepresex02
with dissolve
qu "Are you naked yet? Get down on your knees. I'm going to do front squats ON YOUR COCK."
mc "Err, that sounds dangerous. A bit?"
scene paulettesexbackground
show paulettepresex03
with dissolve
qu "Stop being such a puss. Just hold your cock steady and make sure it goes in the RIGHT hole when I squat down. Ready?"
mc "I... I guess so."
hide paulettepresex03
play channel1 "Sounds/womangroan.mp3"
play channel2 "Sounds/wank.mp3"
label PauletteSexSlow:
hide paulettesexfast
show paulettesexslow
call screen paulettesexslow01
screen paulettesexslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PauletteSexEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PauletteSexFast") 

label PauletteSexFast:
qu "That's a good SEXERCISE! Let's do it FASTER now, I hope your big cock is ready for it!"
hide paulettesexslow
show paulettesexfast
call screen paulettesexfast01
screen paulettesexfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PauletteSexEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PauletteSexSlow") 

label PauletteSexEnd:
qu "Yeah, I can feel my quads really straining... As well as my pussy."
mc "Can we... take a break... PLEASE!"
qu "Alright, puny boy."
stop channel1
stop channel2
hide paulettesexslow
hide paulettesexfast
show paulettepresex03
with dissolve
play sound "Sounds/panting.mp3"
qu "Is your cock still intact?"
mc "AAAH... barely..."
qu "But it still is, right? What aboot we do some more POWERFUCKING then?"
mc "You want some powerfucking? I'll POWERFUCK YOU alright, Paulette! Get on your back and you'll see!"
qu "Oooh, I like boys with CONFIDENCE! I usually scare them away, but you seem up for the task!"
scene paulettefuckbackground
show pauletteprefuck
with dissolve
mc "I've got the tip in... Feels so tight already!"
qu "I'm totally WET I am for your magnificent MONSTERCOCK so just SHOVE IT IN!"                                                                  
scene paulettefuckbackground blurred
play channel1 "Sounds/debrasex.mp3"
play channel2 "Sounds/wank.mp3"
label PauletteFuckSlow:
hide paulettefuckfast
show paulettefuckslow
mc "Nice and slow at first, so you can get used to my size..."
qu "Mon Dieu! Even Canadian lumberjacks don't have LOGS THAT SIZE!"
call screen paulettefuckslow01
screen paulettefuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PauletteFuckFast")

label PauletteFuckFast:
mc "And now, FASTER, so I can really plunge my tool DEEP inside you!"
hide paulettefuckslow
show paulettefuckfast
qu "AAAh, you're really STRETCHING me, STUD!"
call screen paulettefuckfast01
screen paulettefuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PauletteFuckEnd")

label PauletteFuckEnd:
mc "I'm gonna shoot my load inside you NOW!"
stop channel1
stop channel2
hide paulettefuckslow
hide paulettefuckfast
show paulettefuckcum
play channel1 "Sounds/splooge02.mp3"
play channel2 "v07/creampie.mp3"
call screen paulettefuckcum01
screen paulettefuckcum01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PauletteFuckEndCum")

label PauletteFuckEndCum:
qu "Dump the rest on me please!"
stop channel1
stop channel2
hide paulettefuckcum
show paulettefuckcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "ALRIGHT, HERE IT COMES, AAAH!"
window hide
with fastflash
qu "Becoming super-strong really made you HORNY, didn't it, [name]?"
window hide
with fastflash
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "FUCK YEAH!"
window hide
with fastflash
qu "It never ends, you're STILL ERUPTING!"
scene paulettefuckbackground
show paulettefuckcum02
with dissolve
play sound "Sounds/panting.mp3"
qu "I'm TOTALLY covered in your dirty American boycum... What a MESS you made..."
call LustPlusPaulette
scene quebec08 blurred
show paulettepostsex
with dissolve
qu "I'm finally gonna need to go and clean myself up in the river... You covered me with TOO MUCH HOT SPUNK!"
mc "Ah, well, I can't join you Paulette, it's getting late and I need to get back to my compound."
qu "That's too bad for you... Being forced to leave sacred Canadian soil."
mc "Maybe I'll come back again one day."
jump BackHex61c
    
label BackHex61:
stop music
scene command01
show lena01
with fade
$ period += 1
if alone:
    le "So, what do you have to report about area G1, scout?"
if alone == False:
    le "So, what do you have to report about area G1, scouts?"
if frenchovermax >= 1 and workcanada >= 1:
    mc "I ended up in Canada. I took up a job as a lumberjack. I cut down trees, I eat my lunch and I go to the lavatory."
    hide lena01
    show lena03
    with fastdissolve
    le "And what exactly is the use of that towards your MAIN OBJECTIVE?"
    mc "The promise of getting SUPER-STRONG at the end. Apparently, that is required for some reason. Something to do with Kimberly would be my guess."
    hide lena03
    show lenapensive
    with fastdissolve
    le "I suppose... She is damn strong, I saw her stats."
    hide lenapensive
    show lena06
    with fastdissolve
    le "But do NOT lose track of your main objective: removing Trumpf from power!"
    mc "Oh, is that what it is? I thought it was banging as many chicks as I could. Like in most games."
    le "* sigh* You are dismissed."
    hide lena06 with dissolve
    jump LeaveCommand
if frenchovermax >= 1 and workcanada == 0:
    mc "I ended up in Canada. I might work there part-time chopping down trees to get even buffer."
    hide lena01
    show lena03
    with fastdissolve
    le "What? You can't WORK there, you're already employed by the compound!"
    mc "Well, hang on a minute. Most Americans have TWO jobs to make ends meet. Especially in this piss-poor economy."
    hide lena03
    show lenapensive
    with fastdissolve
    le "*sigh*. I suppose you're right, I can't stop you from seeking better employment elsewhere..."
    mc "Damn right you can't!"
    hide lenapensive
    show lena06
    with fastdissolve
    le "But do NOT lose track of your main objective: removing Trumpf from power!"
    mc "Oh, is that what it is? I thought it was banging as many chicks as I could. Like in most games."
    le "* sigh* You are dismissed."
    hide lena06 with dissolve
    jump LeaveCommand
if mcfrench <= 10:
    mc "I ended up in Canada. Unfortunately, the silly part of it. Couldn't understand a bloody word that French-Canadian lumberjack chick was saying."
    hide lena01
    show lena03
    with fastdissolve
    le "A lumberjack? So they have trees over there?"
    mc "Yes, same as before, huge forests. Nothing seems to have changed in Canada. The girls are still super-buff."
    hide lena03
    show lenapensive
    with fastdissolve    
    le "Well. No point going back there then. Trumpf is most definitely NOT WELCOME in Canada. You are dismissed [name]."
    hide lenapensive with dissolve
    jump LeaveCommand
    
label BackHex61d:
stop music
scene command01
show lena01
with fade
$ period += 1
le "So, what do you have to report about area G1?"
mc "Nothing much."
hide lena01
show lena03
with fastdissolve
le "As in you went there for nothing much then. You are dismissed."
hide lena03 with dissolve
jump LeaveCommand
    
label BackHex61c:
if fuckedpaulettegain:
    jump BackHex61d
stop music
scene command01
show lena01
with fade
$ period += 1
le "So, what do you have to report about area G1, scout?"
mc "After all my hard work, I've become SUPER-STRONG! Also, I came buckets all over sacred Canadian soil apparently."
hide lena01
show lena03
with fastdissolve
le "I still don't think I wanted to know that... You are dismissed."
hide lena03 with dissolve
jump LeaveCommand

label BackHex61b:
stop music
scene command01
show lena01
with fade
$ period += 1
le "So, what do you have to report about area G1, scout?"
mc "I'm getting buffer Chief, I can feel it. Must have gained at least 10 pounds of muscles. And lost the same amount in sperm unfortunately."
hide lena01
show lena03
with fastdissolve
le "I don't think I wanted to know that... You are dismissed."
hide lena03 with dissolve
jump LeaveCommand
    
label Lumberjack:
    window hide
    play music "v081/lumberjack.mp3"
    hide paulettelumberjack00
    show mclumberjack01a
    show paulettelumberjack01a
    with dissolve
    $ renpy.pause(0.5, hard=True)
    hide paulettelumberjack01a
    hide mclumberjack01a
    show paulettelumberjack01b
    show mclumberjack01b
    with fastdissolve
    pause 0.5
    hide paulettelumberjack01b
    hide mclumberjack01b
    show mclumberjack01a
    show paulettelumberjack01a
    with fastdissolve
    pause 0.5
    hide paulettelumberjack01a
    hide mclumberjack01a
    show paulettelumberjack01b
    show mclumberjack01b
    with fastdissolve
    pause 0.5
    hide paulettelumberjack01b
    hide mclumberjack01b
    show mclumberjack01a
    show paulettelumberjack01a
    with fastdissolve
    pause 0.5
    hide paulettelumberjack01a
    hide mclumberjack01a
    show paulettelumberjack01b
    show mclumberjack01b
    with fastdissolve
    pause 0.5
    hide paulettelumberjack01b
    hide mclumberjack01b
    show paulettelumberjack03
    show mclumberjack03
    with dissolve
    pause 1.0
    hide paulettelumberjack03
    hide mclumberjack03
    show paulettelumberjack02a
    show mclumberjack02a
    with dissolve
    pause 0.5
    hide paulettelumberjack02a
    hide mclumberjack02a
    show paulettelumberjack02b
    show mclumberjack02b
    with fastdissolve
    pause 0.5
    hide paulettelumberjack02b
    hide mclumberjack02b
    show paulettelumberjack02a
    show mclumberjack02a
    with fastdissolve
    pause 0.5
    hide paulettelumberjack02a
    hide mclumberjack02a
    show paulettelumberjack02b
    show mclumberjack02b
    with fastdissolve
    pause 0.5
    hide paulettelumberjack02b
    hide mclumberjack02b
    show paulettelumberjack03
    show mclumberjack03
    with fastdissolve
    pause 1.0
    hide paulettelumberjack03
    hide mclumberjack03
    show paulettelumberjack04a
    show mclumberjack04a
    with dissolve
    pause 1.0
    hide paulettelumberjack04a
    hide mclumberjack04a
    show paulettelumberjack04b
    show mclumberjack04b
    with dissolve
    pause 0.5
    hide paulettelumberjack04b
    hide mclumberjack04b
    show paulettelumberjack04c
    show mclumberjack04a
    with dissolve
    pause 1.0
    hide paulettelumberjack04c
    hide mclumberjack04a
    show paulettelumberjack04b
    show mclumberjack04b
    with dissolve
    pause 0.5
    hide paulettelumberjack04b
    hide mclumberjack04b
    show paulettelumberjack04c
    show mclumberjack04a
    with dissolve
    pause 1.0
    hide paulettelumberjack04c
    hide mclumberjack04a
    show paulettelumberjack04b
    show mclumberjack04b
    with dissolve
    pause 0.5
    hide paulettelumberjack04b
    hide mclumberjack04b
    show paulettelumberjack04c
    show mclumberjack04a
    with dissolve
    pause 1.0
    stop music
    return

label NorthGateAvengers:
$ period += 1
play music "Sounds/desertwind01.mp3"
scene northgate01 with fade
mc "This is where the entrance to Trumpf City lies... Through these damp and dangerous sewers."
mo "Oh dear, this doesn't sound like a very good idea, sweetie pie..."
qu "Come on, let's go, Captain Canuck has some trees to chop down back in Canada!"
if withbe:
    be "I'll stay back and guard the rig. In case you lose your fight and need to be taken to the medbay. As usual."
if withpe:
    pe "I'll stay back and guard the rig. In case you lose your fight and need to be taken to the medbay. As usual."
    
label HannityFight:
scene northgate03 with dissolve
mc "This place is the same as where I first met this ins..."
window hide
play sound "Sounds/hulkgrowl01.mp3"
show hannity01 with moveinright
se "-- AAARRH! TAN SUIT! RHAAA! LAW AND ORRR-DERRR!"
mc "That's it, it's HIM!"
mo "Oh dear me, he looks very angry."
play sound "Sounds/hulkgrowl02.mp3"
hide hannity01
show hannity02
with fastdissolve
se "-- DEMO-CRRATIC... GRRRR.... HOAX!"
wi "Time for the NEW AVENGERS to KICK SOME ASS! I'll supervise from the sideline, that's my superpower."
qu "LAME! But Captain Canuck is ready for a FIGHT!"
mc "So is Captain America!"
pause
mc "Captain Marvel?"
mo "Oh... I guess I'm ready sweetie pie. As long as someone tells me what to do..."

hide screen mcstats
hide screen calendar
play music "v072/battle.mp3"
scene northgate03
show avengersfight01
show hannityfight01 at farright
with dissolve
$ avengers_health = 3.0
$ hannity_health = 3.0
show screen screenfightavengers
$ hannityfirst = False

label HannityRound:
if hannityfirst:
    jump RoundHannityFight
if hannityfirst == False:
    jump RoundMCHannityFight

label RoundHannityFight:  
wi "Avengers! Prepare for DEFENSE!"
play sound "Sounds/hulkgrowl02.mp3"
window hide
hide hannityfight01
show hannityattack
with fastdissolve
se "-- GRRRR.... DOSSIER!"
stop sound
window hide
label RoundHannityFightb:
call DiceRoll
if diceroll >= 3:
    hide avengersfight01
    hide hannityattack
    show hannityattackhit
    with fastdissolve
    play sound "Sounds/punch.mp3"
    se "-- AAAR!"
    mc "Damn, what a punch!!"
    $ counting = 0
    while counting < 20:
        $ avengers_health -= 0.05
        $ counting += 1
        pause 0.01
    if avengers_health >= 0.1:
        qu "Captain Canuck is barely... stopping his mighty advance!"
    if avengers_health <= 0.09:
        hide hannityattackhit
        show hannityattackhit02
        with fastdissolve        
        wi "Avengers, strategic RETREAT before he kills all of us! I mean all of you!"
        qu "You're injured, I'll pull you out of this fight for your own sake!"
        hide screen screenfightavengers
        show screen mcstats
        show screen calendar
        mc "I'm NOT injured, let me fight this beast!"
        call MCInjury
        $ mcinjuredfight = True
        mc "Ah, ok, I am injured after all..."
        mo "Oh dear me... Please let's leave this dreadful place sweetie pie..."
        stop music
        hide hannityattackhit02
        show hannity02
        with dissolve
        play sound "Sounds/hulkgrowl02.mp3"
        se "-- GGRRRR! SNOWFLAKES!"        
        $ attackexplained = False
        $ nancytoldnuts = False
        jump HannityLoseEnd        
    hide hannityattackhit
    show avengersfight01
    show hannityfight01 at farright
    with fastdissolve
else:
    hide avengersfight01
    hide hannityattack
    show hannityattackmiss
    with fastdissolve
    play sound "Sounds/hulkgrowl02.mp3"    
    mc "You can growl all you want, we BLOCKED your attack, BEAST!"
    se "-- AAARH! CHEATS!"
    hide hannityattackmiss
    show avengersfight01
    show hannityfight01 at farright
    with fastdissolve
$ hannityfirst = False
jump HannityRound

label RoundMCHannityFight:  
if attackexplained:
    wi "Avengers! Prepare for ATTACK! Same strategy as usual!"    
if attackexplained == False:
    wi "Avengers! Prepare for ATTACK!"
    mo "And what should I do?"
    wi "Slide under him, Captain Marvel! While Captain America and Captain...Canuck distract him through a FRONTAL and AERIAL attack!"
    $ attackexplained = True
window hide
hide avengersfight01
hide hannityfight01
show avengerspreattack
with fastdissolve
call DiceRoll
$ dcombatroll=mccombat+diceroll        
if (dcombatroll >= 13 and not diceroll == 1) or diceroll == 6:
    window hide
    hide avengerspreattack
    show avengersattackhit
    with fastdissolve
    play sound "Sounds/punch.mp3"
    mc "Take that!"
    play sound "Sounds/crunch.mp3"
    qu "And what aboot THAT!"
    if nancytoldnuts == False:
        mo "I'm kicking him in the NUTS! Which are very small for his stature I must say."
        $ nancytoldnuts = True
    play sound "Sounds/hulkgrowl01.mp3"
    $ counting = 0
    while counting < 20:
        $ hannity_health -= 0.05
        $ counting += 1
        pause 0.01
    if hannity_health >= 0.1:
        se "-- AAARH!"
        hide avengersattackhit
        show avengersfight01
        show hannityfight01 at farright
        with dissolve        
    if hannity_health <= 0.09:
        se "-- GR-AAARH!"
        hide avengersattackhit
        show hannityvictory01
        with dissolve
        wi "Looks like he's done for, he's gonna fall!"
        mc "Disperse! And let him DIE!"
        jump HannityWinEnd
if (dcombatroll <= 12 and not diceroll == 6) or diceroll == 1:
    window hide
    hide avengerspreattack
    show avengersattackmiss
    with fastdissolve
    with fastdissolve
    se "-- ROAR!"
    play sound "Sounds/hulkgrowl01.mp3"
    mc "Get away girls, my punches aren't doing anything!"
    wi "Regroup for DEFENSE, New Avengers!"
    hide avengersattackmiss
    show avengersfight01
    show hannityfight01 at farright
    with dissolve
$ hannityfirst = True
jump HannityRound   

label HannityLoseEnd:
scene northgate01 with fade
if withbe:
    show bellaoutworry with moveinright
    be "So, what happened? You all look in such a terrible shape... Except the Black Widow."
if withpe:
    show pennyout01 with moveinright
    pe "So, what happened? You all look in such a terrible shape... Except the Black Widow."
wi "A small setback for the New Avengers, nothing more. We shall tend to our injuries, I mean THEIR injuries, and we WILL come back to defeat EVIL!"
qu "Captain Canuck will need to be in communion with the forest until next week. Don't ask me to help you until then..."
$ canuckdefeated = True
mc "Alright, we'll attack again next week. Either that, or I find another way into Trumpf City..."
$ period += 1
scene command01
show lena01
with fade
le "So, what do you have to report about area G2, scouts?"
if withbe:
    be "Major defeat all round, Chief Lena. Courtesy of the New Avengers... To which I DO NOT belong."
if withpe:
    pe "Major defeat all round, Chief Lena. Courtesy of the New Avengers... To which I DO NOT belong."
mc "Hey! Come on, we fought valiantly and we almo..."
hide lena01
show lena10
with fastdissolve
le "ALMOST winning doesn't COUNT! You NEED to get inside Trumpf City. Go to the medbay and ponder THAT!"
mc "Roger that, Chief..."
jump Medbay

label HannityWinEnd:
hide screen screenfightavengers
show screen mcstats
show screen calendar
stop music
hide hannityvictory01
show hannityvictory02
with dissolve
play sound "Sounds/dive.mp3"
$ renpy.pause(1.0, hard='True')
show widowsewer01 with moveinleft
wi "Victory! the New Avengers, under the leadership of the Black Widow, have defeated the evil Sean Insannity!"
window hide
show nancysewer01 at farright with moveinright
show canucksewer01 at farleft02 with moveinleft
qu "Oui, we did it! Canada beats the world. AGAIN!"
mc "This calls for an orgy-like celebration girls! Get your kits off and let's have some F-U-U-N!"
hide widowsewer01
show widowsewer02
with fastdissolve
wi "Are you really suggesting we have sex in a filthy sewer above the radioactive carcass of Sean Insannity?"
mc "Err... Well, the way you put, it doesn't sound so appealing, BUT I recko..."
hide canucksewer01
show canucksewer02 at farleft02
with fastdissolve
qu "Captain Canuck only has sex on sacred Canadian soil! And it's aboot time she went back HOME."
hide nancysewer01
show nancysewer02 at farright
with fastdissolve
mo "I think Captain Marvel needs to go back to the compound honey. She still has 200 salads to chop up and 200 camel paddies to cook..."
mc "Alright, alright, I get it! Captain America will soldier onwards alone..."
hide widowsewer02
show widowsewer03
with fastdissolve    
wi "Not alone! The Black Widow will stand...err... mostly BEHIND you!"
if withbe:
    mc "Oh, I see Bella is coming our way... Can you take Captain Canuck and Nancy back and lend your rifle to the Black Widow? We are going into Trumpf City!"
    be "She can have my rifle as long as you promise to give it back to me when you've kicked Trumpf out of office."
if withpe:
    mc "Oh, I see Penny is coming our way... Can you take Captain Canuck and Nancy back and lend your rifle to the Black Widow? We are going into Trumpf City!"
    pe "She can have my rifle as long as you promise to give it back to me when you've kicked Trumpf out of office."
mc "Thanks! Then, I bid you farewell my friends, for it is time for me, and the Black Widow BEHIND me, to enter the dreaded..."
mc "TRUMPF CITY!"
play sound "Sounds/dundun.mp3"
$ renpy.pause(1.0, hard=True)
hide nancysewer02
show nancysewer01 at farright
with fastdissolve
mo "Oh dear, this sounds scary. Don't come back too late sweetie pie, we're having camel burger and salad for dinner."
scene northgate04 with fade
$ withpe = False
$ withbe = False
$ withwi = True
mc "Finally! I can see the end of the sewer and what clearly looks like a city afar... Woo-Hoo! Supreme White House, here we come!"
jump FinalStart
    
label ExploreHex62:
$ exploredhex62 = True
play music "Sounds/desertwind01.mp3"
scene northgate01 with dissolve
if knowcity == False:
    mc "Uh oh, looks like we've reached some city walls. Well, no point standing here, I have no idea what's behind that wall because I'm so far behind in the game's progression."
    if withbe:
        be "What, you're not even going to investigate?"
        mc "And get shot at by some guard? No thanks. Let's go home."
        be "Umpf, I'll have no choice but to report your cowardly attitude to Chief Lena..."
    if withpe:
        pe "What, you're not even going to investigate?"
        mc "And get shot at by some guard? No thanks. Let's go home."
        pe "Umpf, I'll have no choice but to report your cowardly attitude to Chief Lena..."
    stop music
    $ period += 1
    scene command01
    show lena01
    with fade
    le "So, what do you have to report about area G2? Surely, something interesting, Trumpf City can't be that far away...."
    mc "Errr, nothing really. Just a wall. Separating us from God knows what."
    if withbe:
        be "And he wouldn't even investigate!"
        hide lena01
        show lena10 
        with fastdissolve
        le "What? You're paid to be a SCOUT and a scout INVESTIGATES!"
        call LustMinusLena
        le "You'd better learn what's behind that wall, you're WAY BEHIND! DISMISSED!"
        hide lena10 with dissolve
        jump LeaveCommand
    if withpe:
        pe "And he wouldn't even investigate!"
        hide lena01
        show lena10 
        with fastdissolve
        le "What? You're paid to be a SCOUT and a scout INVESTIGATES!"
        call LustMinusLena
        le "You'd better learn what's behind that wall, you're WAY BEHIND! DISMISSED!"
        hide lena10 with dissolve
        jump LeaveCommand

if knowcity and knowentrancenorth == False:
    mc "Must be the walls surrounding Trumpf City. I see a sewer entrance but there is no way I'm getting wet and dirty. There must be another way in. Let's go home."
    if withbe:
        be "What, you're not even going to try?"
        mc "I don't want my baby skin to get contaminated by diry waters!"
        be "Umpf..."
    if withpe:
        pe "What, you're not even going to try?"
        mc "I don't want my baby skin to get contaminated by diry waters!"
        pe "Umpf..."
    stop music
    $ period += 1
    scene command01
    show lena01
    with fade
    le "So, what do you have to report about area G2? Surely, something interesting, Trumpf City can't be that far away...."
    mc "Trumpf City sure isn't far. We saw its walls. But no way in I'm afraid."
    hide lena01
    show lenapensive
    with fastdissolve
    le "There MUST be a way into that city. You MUST find it, you hear me?"
    mc "Roger that, Chief!"
    hide lenapensive
    show lena03
    with fastdissolve
    le "You're dismissed."
    hide lena02 with dissolve
    jump LeaveCommand

if knowcity and knowentrancenorth:
    mc "Finally! Must be the walls surrounding Trumpf City. And the sewer entrance the Oracle spoke about in her vision."
    if withbe:
        be "Then it is a sign of the Phallus Lord! We MUST get inside those sewers and enter the City!"
        mc "Hang on a minute, let me decide when a menu pops up..."
    if withpe:
        pe "It's quite risky, she mentioned many dangers lying inside those sewers if I remember correctly..."
    menu:
        "Enter the sewers":
            jump EnterSewer
        "Go back to the compound":
            jump LeaveSewer01

label LeaveSewer01:
stop music
$ period += 1
scene command01
show lena01
with fade
le "So, what do you have to report about area G2? Surely, something interesting, Trumpf City can't be that far away...."
mc "Trumpf City sure isn't far. We saw its walls. But no way in I'm afraid."
hide lena01
show lenapensive
with fastdissolve
le "There MUST be a way into that city. You MUST find it, you hear me?"
mc "Roger that, Chief!"
hide lenapensive
show lena03
with fastdissolve
le "You're dismissed."
hide lena02 with dissolve
jump LeaveCommand

label EnterSewer:
stop music
play music "Sounds/waterdrip.mp3"
scene northgate02 with dissolve
mc "God it's smelly in here. Did someone fart?"
if withbe:
    be "Just move along [name]..."
if withpe:
    pe "Just move along [name]..."
    
scene northgate03 with dissolve
mc "When will those sewers ever en..."
window hide
play sound "Sounds/hulkgrowl01.mp3"
show hannity01 with moveinright
se "-- AAARRH! Open BOR-DERRRS! RHAAA! VOTER FRRRAUD!"
mc "What is this insane monster babbling about?"
play sound "Sounds/hulkgrowl02.mp3"
hide hannity01
show hannity02
with fastdissolve
se "-- SOCIALISM! RHOOOO! RAY-PEEESTS!"
mc "He doesn't have a neck. It must be Sean Insannity from Fixed News, radiations turned him into something even more horrible than he already was!"
menu:
    "Hey buddy, I just want to get through so...":
        play sound "Sounds/hulkgrowl01.mp3"
        se "-- EEE-LEEE-GALS! AAARH!"
        hide hannity02
        show hannity03
        with fastdissolve
        play sound "Sounds/punch.mp3"
        mc "Yikes, what a punch!"        
        call MCInjury
        $ mcinjuredfight = True 
        hide hannity03
        show hannity04
        with fastdissolve
        play sound "Sounds/dive.mp3"
        se "-- CITY BORDER...AAAHHR! CLOSED!"
        mc "Shit, there's no way to beat him alone clearly! I'm outta here!"
    "He looks too strong and pissed, get the hell out of there":
        hide hannity02
        show hannity04
        with fastdissolve 
        play sound "Sounds/hulkgrowl01.mp3"
        se "-- FAR LEFT LEE-BRALS! OOORH!"

stop music
play music "Sounds/desertwind01.mp3"
scene northgate01 with fade        
mc "I think I need to recruit more muscle to beat that monster."
window hide
show hannityquest at posmission
$ renpy.pause(1.0, hard=True)
pause
hide hannityquest
$ missionhannity = True
if metqu:
    mc "Perhaps re-forming the New Avengers with Paulette would be appropriate..."
if metqu == False:
    mc "Perhaps re-forming the New Avengers would be appropriate..."
if persistent.tipson:
    show hannitytip at tips with dissolve
    pause
    hide hannitytip
stop music
$ period += 1
scene command01
show lena01
with fade
le "So, what do you have to report about area G2? Surely, something interesting, Trumpf City can't be that far away...."
mc "You are correct as always Chief! And I found an entrance to the city through some dark and damp sewers."
hide lena01
show lena03
with fastdissolve
le "Right... So you entered Trumpf City then?"
mc "Err, not exactly. I was stopped by an incredibly strong and insane monster. Sean Insannity to be precise."
hide lena03
show lenapensive
with fastdissolve
le "He's most definitely an insane Trumpster... He must be guarding that entrance then, which means it is an important passage into the City."
hide lenapensive
show lena07
with fastdissolve
le "Time is running out, you therefore NEED to find a way to get past him [name]."
mc "Roget that Chief. Will most definitely do when I get the chance. I already have a plan."
hide lena07
show lena05
with fastdissolve
le "It better be a good plan. You are dismissed."
hide lena05 with dissolve
if mcinjured:
    mc "And I'll show myself to the medbay after the beating I took..."
jump LeaveCommand

label ExploreHex64:
scene cave01 with fade
play music "Sounds/desertwind01.mp3"
if exploredhex64 == False:
    mc "There seems to be some kind of cave over there. And light is coming out of it..."
    if withpe:
        pe "Be careful, it might be a trap. If you see a naked woman in there, it's definitely a trap. Like in Mad Max."
    if withbe:
        pe "Be careful, it might be a trap. If you see a naked woman in there, it's definitely a trap. Like in Mad Max."
    jump DevCave01

if exploredhex64:
    mc "Let's go inside and see how the ladies are coping..."
    jump DevCave02

label DevCave01:
stop music
$ exploredhex64 = True
scene devcave01 with dissolve
ln "Hello? Is anyone there? ICSTOR?"
aw "Am I a pedophile deep down L\&P? Please answer me, I need to know!"
scene devcave02 with dissolve
ln "Hey YOU, HELP! We're trapped!"
mc "What's going on here? What happened to you ladies?"
scene devcave03 with dissolve
aw "Our devs kidnapped us and we've been waiting here for over TWO years without any sex scenes!"
scene devcave02 with dissolve
ln "And we're being MILKED every month! Just open the latch please mister."
mc "Umh, is this a trap? Like a scam or something?"
scene devcave04 with dissolve
aw "NO! What the fuck? HELP US, can't you see we are being held captive against our virtual free will?"
mc "I don't know, feels like a scam..."
ln "You're not going to HELP us? What kind of fucked-up hero are you?"
mc "Not my fault. MY dev hasn't finished this scene. He's milking it too. Cos if ICSTOR and L\&P can get away with it, why can't he?"
aw "Is this a sick joke? How much LONGER are we going to have to wait???"
mc "Two months. He's pausing his Patreon page in September."
scene devcave05 with dissolve
ln "Well, at least he's pausing it. Mine didn't pause his page for two years while producing NOTHING."
scene devcave06 with dissolve
aw "Don't complain Linda! At least you had some hot sex with your so.. I mean tenant, at one stage. I only had sex ONCE with my lousy husband. And he has a tiny dicklet."
scene devcave07 with dissolve
ln "[name] here is going to DESTROY your pussy in two months then! I hear he has the BIGGEST hero-cock on f95zone."
mc "Damn right I have! So think about it for another two months and get your snatches REAL WET for me for when I come back!"
scene devcave04 with dissolve
aw "Can't you just.. at least... show it to us?"
ln "I haven't seen a cock in two years!"
mc "Na, no time for that. See you ladies!"
scene devcave02 with dissolve
ln "What? COME BACK HERE FUCKING ASSHOLE! I'M HORNY, GODAMMIT!"
scene devcave08 with dissolve
aw "I don't think I'll EVER have sex again in my virtual life... *sob*"
jump BackHex64

label BackHex64:
stop music
scene command01
show lena01
with fade
$ period += 1
if alone:
    le "So, what do you have to report about area G4, scout?"
if alone == False:
    le "So, what do you have to report about area G4, scouts?"
mc "I stumbled upon a character-holding cave built by milking devs."
hide lena01
show lena03
with fastdissolve
le "Milking devs? What's that?"
mc "Well, the list goes on but you have ICSTOR, L\&P, Gumdrop, Psychodelu..."
hide lena03
show lena06
with fastdissolve
le "Alright, I get it, stop right there. The compound can't afford the lawsuits. You are dismissed."
hide lena06 with dissolve
jump LeaveCommand

label DevCave02:
stop music
scene devcave01 with dissolve
aw "Did I really have to jerk off these prepubescent boys L\&P? It felt... wrong."
mc "I'm BACK ladies!"
scene devcave02 with dissolve
ln "About bloody time! Get us out of here and FUCK US REAL GOOD!"
scene devcave04 with dissolve
mc "Sure, where's the latch?"
scene devcave08 with dissolve
aw "We don't know... Our devs never tell us anything about who we are and why we're here..."
scene devcave05 with dissolve
ln "The why is easy Sophia! They are MILKING us. And their patrons! Just look around for some switch, [name]... And hurry up, I need a good FUCK!!!"
scene devcave11 with dissolve
play sound "v08/doorwoosh.mp3"
aw "That did the trick! I can finally breathe fresh air."
ln "Well done, REAL HERO!"
scene devcave12 with dissolve
ln "Look Sophia, this place is even stranger than I anticipated... What twisted devs we have."
aw "It feels so weird being in 1920*1080 resolution... I'm normally only rendered at 1280*720 pixels..."
ln "At least there's a nice big cushion right in the middle of the cave."
scene devcave13 with dissolve
aw "What are you thinking about Linda?"
ln "That it's the perfect spot for a HOT ROMP with our hero STUD! So let's show him what we've got in store for his massive dong!"

play music "v07/datemusic.mp3"
scene devcave14 with dissolve
ln "That's it Sophia, show him that fine ass... That should get him HARD and READY for us in no time!"
aw "I'm used to exposing myself like that to boys for some strange reason..."
ln "I want to rub my pussy against yours Sophia... Let's get on the love pillow..."
scene devcave15 with dissolve
play sound "Sounds/moaning03.ogg"
aw "OOOH, I haven't felt this naughty in such a long time!"
scene devcave16 with dissolve
ln "You like our boots I see?"
mc "Yes... And your tits too."
ln "Then lie on the ground by the pillow, we'll use them to jack your crank into a mighty orgasm!"
scene devcaveprefoot01 with dissolve
ln "There, are you feeling comfortable?"
aw "This is so dirty, our boots rubbing against his fat shaft... Mmmh..."
mc "Y...Yes, I think I'm ready..."
ln "I can see that, you're already LEAKING... Let's get to work Sophia, shall we?"
play music "Sounds/wank.mp3"
label DevCaveAnimSexSlow:
scene devcaveanimslow with fastdissolve
call screen devcaveanimsexslow01
screen devcaveanimsexslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DevCaveAnimSexEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DevCaveAnimSexFast") 

label DevCaveAnimSexFast:
ln "I think we need to increase the tempo. To get him to SPEW HIS SAUCE!"
scene devcaveanimfast with fastdissolve
call screen devcaveanimsexfast01
screen devcaveanimsexfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DevCaveAnimSexEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DevCaveAnimSexSlow") 

label DevCaveAnimSexEnd:
stop music
scene devcavecum01 with dissolve                                         
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH!"
ln "That's it, we made you cum with our boots!"
window hide
with fastflash
aw "There's sooo much of it, I've never seen a load THAT big!"
scene devcavecum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
ln "I told you, [name] is the biggest STUD on f95zone..."
window hide
with fastflash
aw "If only he was a love interest in \"A Wife And Mother\"... Instead of the beta-boys I have to contend with..."
scene devcavecum03 with dissolve
play sound "Sounds/panting.mp3"
ln "Was that good [name]? Did it relieve your big fat straining balls?"
mc "Phew, yeah, it did the trick, they feel lighter now..."
ln "And I'm feeling SUPER-HORNY. And I want that hard cock UP MY ASS! I expect a STUD like you to keep it UP and ROCKHARD!"
scene devcavecum04 with dissolve
aw "Are you sure Linda? It looks awfully HUGE for that hole!"
ln "Don't worry about me, I've been practising this for so long, I could stick a telephone pole up there!"
scene devcave17 with dissolve
play music "v07/datemusic.mp3"
ln "Let me first get you into the mood [name]..."
scene devcave18 with dissolve
ln "Mmh, there you go, I can see you are already back to FULL HARDNESS for me... You really can't wait to pound that ass, hey?"
scene devcave19 with dissolve
mc "Shit, it looks so fucking amazing, I want IN, right NOW! Come over here and bend over!"
aw "Sssoo manly... Not like my pindick husband..."
scene devcavepreass03 with dissolve
aw "I can't believe you're going to stick this monster pud inside that tiny hole... You're going to DESTROY it with that massive weapon of yours!"
scene devcavepreass02 with dissolve
ln "It is indeed a weapon of ASS DESTRUCTION! Spread my asscheeks for him will you Sophia?"
mc "And watch carefully Sophia.... Cos this is what will happen to your pussy NEXT!"
scene devcavepreass04 with dissolve
mc "Are you ready to have your ass DESTROYED?"
ln "YES! Pound it HARD, and show me what I've been missing for over two years!"
label DevCaveFuckSexSlow:
$ devcaveoral = False
play music "Sounds/fucksound.mp3"
scene devcavefuckslow with fastdissolve
call screen devcavefucksexslow01
screen devcavefucksexslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DevCaveFuckSexFast") 
    imagebutton:
        focus_mask True
        idle "v082/mouth.png"
        hover "v082/mouth.png"
        action Jump ("DevCaveMouthSlow") 

label DevCaveFuckSexFast:
if devcaveoral == False:
    ln "Go on, POUND ME HARDER!"
$ devcaveoral = False
play music "Sounds/fucksound.mp3"
scene devcavefuckfast with fastdissolve
call screen devcavefucksexfast01
screen devcavefucksexfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DevCaveFuckSexEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DevCaveFuckSexSlow") 
    imagebutton:
        focus_mask True
        idle "v082/mouth.png"
        hover "v082/mouth.png"
        action Jump ("DevCaveMouthFast") 

label DevCaveMouthSlow:
if devcaveoral == False:
    mc "Let's switch holes... Sophia's MOUTH!"
$ devcaveoral = True
play music "Sounds/hardsucking.mp3"
scene devcavemouthslow with fastdissolve
call screen devcavemouthslow01
screen devcavemouthslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DevCaveMouthFast") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("DevCaveFuckSexSlow") 

label DevCaveMouthFast:
if devcaveoral == False:
    mc "Let's switch holes... Sophia's MOUTH!"
$ devcaveoral = True
play music "Sounds/hardsucking.mp3"
scene devcavemouthfast with fastdissolve
call screen devcavemouthfast01
screen devcavemouthfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DevCaveMouthSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("DevCaveFuckSexFast") 

label DevCaveFuckSexEnd:
stop music
scene devcavefuckcum01 with dissolve                                         
play music "v07/creampie.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Dumping my load, AAAHH!"
window hide
with fastflash
mc "Open your mouth real WIDE Sophia!"
aw "What? W...Why???"
scene devcavefuckcum02 with dissolve   
stop music
play music "Sounds/hardsucking.mp3"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "That's why!"
window hide
with fastflash
aw "* Glllurb...* "
scene devcavefuckcum03 with dissolve   
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "And now directly down your gullet! AAAH!"
window hide
with fastflash
ln "Yes, fill up her stomach with your sauce [name]!"
scene devcavefuckcum04 with dissolve   
stop music
stop sound
play sound "Sounds/slurp.mp3"
mc "Yeah, swap mouthfulls of my cum ladies.... That's so nasty..."
ln "Mmmh, it's so tasty, give me more Sophia..."
scene devcavefuckcum05 with dissolve   
mc "There, here are a few more afterdregs for you..."
aw "Wow, there MORE cum left in your spermtube than my poor hubby can produce in a MONTH!"
scene devcavefuckcum06 with dissolve  
play sound "Sounds/thud.mp3"
mc "And guess what? I'm still ROCKHARD!"
ln "I think it's your turn to get your pussy DESTROYED, Sophia..."
scene devsophiaprefuck01 with dissolve
ln "And you can lick my cummy butthole while [name] rams his cunt-destroyer inside your tender snatch!"
scene devsophiaprefuck02 with dissolve
play sound "Sounds/lick.mp3"
ln "Mmmh, that's nice, Sophia, keep going... And you stud, FUCK HER!"
play music "Sounds/womansex02.mp3"
label DevCaveSophiaSexSlow:
scene devcavesophiafuckslow with fastdissolve
call screen devcavesophiafucksexslow01
screen devcavesophiafucksexslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DevCaveSophiaSexEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DevCaveSophiaSexFast") 

label DevCaveSophiaSexFast:
aw "AAAH, UUUH, Genesis 8 boys are so much better than Genesis 3 ones!"
mc "That's correct, we're BIGGER and STRONGER. Let me demonstrate by pummeling your fuckhole even FASTER!"
scene devcavesophiafuckfast with fastdissolve
call screen devcavesophiafucksexfast01
screen devcavesophiafucksexfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DevCaveSophiaSexEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DevCaveSophiaSexSlow") 

label DevCaveSophiaSexEnd:
mc "That pussy is gonna MILK the cum out of me VERY SOON!"
aw "I have a lot of experience with MILKING. Milking patrons essentially."
stop music
play music "Sounds/splooge02.mp3"
scene devsophiacum01 with dissolve                                         
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "That's it, I'm blowing ANOTHER LOAD!"
window hide
with fastflash
aw "It's so DEEP and WARM inside me! My hubby never FILLED ME UP LIKE THAT!"
scene devsophiacum02 with dissolve                                         
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "And there's more for you pretty ladies, RHAAA!"
window hide
with fastflash
ln "God, even though this is your THIRD load in a row, it's still more CREAM than my so.. landboy can muster in a FULL GAME. Whenever that will be complete."
scene devsophiacum03 with dissolve                                         
play sound "Sounds/panting.mp3"
mc "Phew, well that was worth waiting two months for, wasn't it ladies?"
scene devcaveend01 with dissolve
ln "Yes, you fucked us real good. But now I somehow feel compelled to go back into my cage."
aw "I have the same strange feeling... Like I am drawn to it."
scene devcaveend02 with dissolve
mc "Come on ladies, you're being mind-controlled by your devs! You're FREE to go now!"
scene devcaveend03 with dissolve
ln "No, I think it's best if we go back... What would we do in the REAL world outside?"
aw "I don't have a home in this world. I NEED to go back to my virtual mansion, my pindick hubby and take care of my children. By regularly exposing myself to them."
scene devcaveend02 with dissolve
mc "So I did all this for NOTHING?"
scene devcaveend04 with dissolve
ln "I found some money in my panty. 10 bucks. With someone's goofy face on it that I don't recognize."
mc "Let me see. Ah, it's President-for-Life Donald Trumpf. It's REAL money then."
scene devcaveend05 with dissolve
aw "What? That doofus is president in the REAL world? Oh my God, please take the banknote I ALSO found in my panty and let's go back to our virtual slavery."
$ money += 20
scene devcaveend06 with dissolve
ln "For sure, I would rather wait idly for another 2 years to maybe resurface than live in a world where Donald Trumpf is president!"
mc "That's actually a decent argument I guess. Alright, I'll put you back into your cages then..."
scene devcaveend07 with dissolve
aw "Thank you so much for your kindness. HORSE-HUNG HERO."
ln "Like they should be in every game really."
scene devcave01 with dissolve
ln "ICSTOR, I'm back! When are you going to use me instead of that little freckled redhead trollop?"
aw "It's me L\&P! I'm ready for some REAL virtual sex now! Pretty please..."
mc "I guess I should leave, they're hopeless cases..."
$ clearedhex64 = True

stop music
scene command01
show lena01
with fade
$ period += 1
if alone:
    le "So, what do you have to report about area G4, scout?"
if alone == False:
    le "So, what do you have to report about area G4, scouts?"
mc "I went back into that cave. I managed to free the ladies there and banged them real good. They gave me twenty bucks and then went back into their cages. Hex cleared, end of story."
hide lena01
show lena06
with fastdissolve
le "Remind me never to nominate you for a Pulitzer Prize. Dismissed."
hide lena06 with dissolve
jump LeaveCommand

label ExploreHex65:
scene maragogofar01 with fade
if seenmaragogo01:
    mc "Ah, I recognize this place, it's Mar-a-Gogo! Melania is probably there, waiting to fuck young boys with monster fucksticks behind her hubby's back..."
    mc "And therefore, since I don't have that damn implant in me anymore, I'll surprise her and fuck her silly till she gives me valuable intel about the Supreme White House!"
    if withbe:
        be "That sounds like a decent plan for once, at least you won't be fucking some stranger for nothing...."
        mc "That's right! I will make her bow down to my superior alpha-bullcock!"    
        be "Alright, stop bragging and go do your deed, I'll stand guard here."
    if withpe:
        pe "That sounds like a decent plan for once, at least you won't be fucking some stranger for nothing...."
        mc "That's right! I will make her bow down to my superior alpha-bullcock!"    
        pe "Alright, stop bragging and go do your deed, I'll stand guard here."
    if withnone == False:
        call AloneStance
    jump MaragogoNew

if seenmaragogo01 == False:
    mc "Looks like some fancy residential area. I have therefore no business here, being a poor hero from the slums and all that."
    if withbe:
        be "That's it? Giving up already?"
        mc "No, just hurrying up the game to enter Trumpf City, that's all."
        be "I see... I guess that's one strategy."
    if withpe:
        pe "That's it? Giving up already?"
        mc "No, just hurrying up the game to enter Trumpf City, that's all."
        pe "I see... I guess that's one strategy."
    stop music
    $ period += 1
    scene command01
    show lena01
    with fade
    le "So, what do you have to report about area G5? This is the last hex on the map, it better be something good..."
    mc "Errr, nothing really. Just a residential area for the Super-Elite. Which I am not a member of."
    hide lena01
    show lenapensive 
    with fastdissolve
    le "Well, that's disappointing. It's almost as if you didn't do something that you should have done to trigger that hex..."
    mc "I don't think so. I've explored everything so far. Right?"
    le "Maybe... Who knows. You are dismissed."
    hide lenapensive with dissolve
    jump LeaveCommand

label MaragogoNew:
scene maragogofar02 with dissolve
mc "Up the ledge and  behind the bushes by the pool where I shall first observe what she's up to..."
scene maragogofar03 with dissolve
mc "Who's that? She's talking to some big-titted chick in a uniform and a strange hat."
mc "Let's squint my eyes so I can zoom in and listen onto what they say..."
scene maragogo02 blurred
show melaniatitiana01
with dissolve
me "There you are Agent Titiana, everything is on the microfilm."
mc "What's all this about? I should go and confront them."
scene maragogo02
show melaniaout03 at left
show titiana01b at centerright
with dissolve
me "What are YOU doing here?"
tn "Who is this boy, comrade?"
hide melaniaout03
show melaniaout02 at left
with fastdissolve
me "A pain in the ass, that's who..."
mc "What the hell? She's a Russian spy! You're not a double-agent Melania, you're a TRIPLE-agent!"
hide titiana01b
show titiana02b at centerright
with fastdissolve
tn "Fear not Comrade Melania, I shall protect you with my bosom! For the glory of Mother Russia!"
me "I'm not scared of him, he probably just came over to try and fuck me."
mc "Hey, how did you guess?"
hide titiana02b
show titiana03b at centerright
with fastdissolve
tn "Then let me deal with this Western spy. The Russian way."
play music "v082/russia.mp3"
scene maragogo08 blurred
show titiana04
with dissolve
tn "So, you want SEX, American boy?"
mc "Err... Yeah, but with Melania cos I can blackmail her now, so step aside lady and let m..."
window hide
hide titiana04
show titiana05
with fastdissolve
tn "Not before I show you this!"
hide titiana05
show titiana06
with dissolve
$ renpy.pause(0.5, hard='True')
hide titiana06
show titiana05
with dissolve
hide titiana05
show titiana07
with dissolve
$ renpy.pause(0.5, hard='True')
hide titiana07
show titiana05
with dissolve
hide titiana05
show titiana06
with dissolve
$ renpy.pause(0.5, hard='True')
hide titiana06
show titiana05
with dissolve
hide titiana05
show titiana07
with dissolve
$ renpy.pause(0.5, hard='True')
hide titiana07
show titiana05
with dissolve
hide titiana05
show titiana06
with dissolve
$ renpy.pause(0.5, hard='True')
hide titiana06
show titiana05
with dissolve
hide titiana05
show titiana07
with dissolve
$ renpy.pause(0.5, hard='True')
hide titiana07
show titiana05
with dissolve
hide titiana05
show titiana06
with dissolve
$ renpy.pause(0.5, hard='True')
hide titiana06
show titiana05
with dissolve
hide titiana05
show titiana07
with dissolve
$ renpy.pause(0.5, hard='True')
hide titiana07
show titiana05
with dissolve
hide titiana05
show titiana06
with dissolve
mc "What... What is she doing flicking her hair like that in front of me? This is somewhat... mesmerizing...."
hide titiana06
show titiana05
with dissolve
tn "And now, let me get undressed for you, American Boy..."
scene maragogo02
show titiana10
with dissolve
mc "Fuck me, those melons are worthy of Mother Russia AND Mother America!"
hide titiana10
show titiana11
with fastdissolve
tn "Now it's your turn to get naked... and ROCKHARD for me!"
stop music
scene titianapretitfuck01 with dissolve
tn "I see you have wasted no time, American Boy."
mc "The sooner I'm done fucking you till you submit, the sooner I can move on to Melania..."
scene titianapretitfuck02 with dissolve
tn "Oh, but we have TIME, don't we? Your MONSTER American boycock needs some tender tit-loving first..."
mc "I suppose I could indulge in some titfucking first... To get me in the mood..."
tn "Oh, it'll get you in the mood, don't worry about THAT!"
play channel1 "Sounds/wank.mp3"
play channel2 "Sounds/moaning03.ogg"
label TitianaTitsSlow:
show titianatitsslow
call screen titianatitfuckslow01
screen titianatitfuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TitianaTitsEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TitianaTitsFast") 

label TitianaTitsFast:
tn "You seem to enjoy my warm Russian bosom, don't you?"
mc "Oh... Fuck... I... can... resist. You're not going to get to me!... Aaaah..."
tn "You think so? I think it's time to make you EXPLODE your filthy capitalist cum all over the place!"
show titianatitsfast
call screen titianatitfuckfast01
screen titianatitfuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TitianaTitsEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("TitianaTitsSlow") 

label TitianaTitsEnd:
tn "Come on American boy, show me how much SPUNK you hold, RELEASE IT ALL!"    
stop channel1
stop channel2
scene titianatitscum01 with dissolve    
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "FUCK, I'm blowing my load, AAAH!"
window hide
with fastflash
tn "YES! EMPTY THOSE BALLS FOR ME!"
scene titianatitscum02 with dissolve    
mc "Those tits... I can't hold back, RHAAA!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
window hide
with fastflash
tn "That's right, Russian breasts can milk any American boycock DRY!"
scene titianatitscum03 with dissolve  
play sound "Sounds/gasp.mp3"
tn "Well, what a mess you made. Now you're empty and I have you at MY MERCY! *slurp*"
mc "Is that what you think?"
scene titianatitscum04 with dissolve  
mc "I'll show you that my American cock is not about to be overcome by enemy trickery!"
tn "What??? You're not empty yet?"
mc "That's right, and I'm gonna to turn you from a commie spy into a cummy mess!"
scene maragogo05 blurred
show titianaprefuck01
with dissolve
mc "You think you can manage this super-sized American boycock, hey, Titiana?"
tn "I can take it, I have been trained in extreme sexual resistance at the school of famous sexologist Professor Jakkov, just shove it in already!"
scene maragogo04b blurred
show titianaprefuck02
with dissolve
mc "I don't know... Your pussy looks awfully tiny compared to it. Can you feel its massive girth rubbing on your clit?"
play sound "Sounds/moaning.mp3"
tn "I... I can feel it, yes... My pussy will withstand your pound..."
hide titianaprefuck02
show titianaprefuck03
with dissolve
play sound "Sounds/womanscream.ogg"
tn "AAAH! I... must... endure it... For the glory of Mother Russia, I will take it for Team Red!"
mc "We'll see about that!"
play music "Sounds/fucksound.mp3"
scene maragogo04 blurred
label TitianaSexSlow:
hide titianafuckfast
show titianafuckslow
call screen titianafuckslow01
screen titianafuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TitianaSexEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TitianaSexFast") 

label TitianaSexFast:
tn "Come on American boy, show me what you got! Pound that Russian pussy HARDER!"
mc "You asked for it!"
hide titianafuckslow
show titianafuckfast
call screen titianafuckfast01
screen titianafuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TitianaSexEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("TitianaSexSlow") 

label TitianaSexEnd:
tn "Please stop pummelling my pussy, I relent! Your Western Capitalist cock is far superior to the Russian Communist ones!"
mc "Beg for my cum then, Titiana!"
tn "Please American boy, fill me up with your superior seed, I BEG YOU!"
scene maragogo04b blurred
show titianafuckcum01
with dissolve
play music "v07/creampie.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH, there you go, directly into your Russian spy snatch!"
window hide
with fastflash
tn "Pull out, your plumes are just TOO POWERFUL!"
play music "sounds/splooge02.mp3"
scene maragogo10 blurred
show titianafuckcum02
with dissolve
mc "No fucking way, you thought I was empty, I'll prove you wrong, RHAAA, take that!"
window hide
with fastflash
tn "T...Too MUCH, AAAH!"
scene maragogo04b blurred
show titianafuckcum03
with dissolve
mc "Fuck ME, it's POURING out of your pussy! RHAAA!"
window hide
with fastflash
tn "That's because you pumped a GALLON of spunk inside it!"
hide titianafuckcum03
show titianafuckcum04
with dissolve
mc "Now that I have disposed of you, I will fuck Melania into submission! Where is she actually? I thought she was watching us."
tn "HA HA, American boy, I have succeeded! My Russian charms have given Comrade Melania enough time to escape out of your clutches and into the safety of the Supreme White House!"
mc "Damn it, I've been had! Now get dressed before I decide to fuck you to death, you wicked Russian agent!"
stop music
scene maragogo08 blurred
show titiana01 
with dissolve
mc "After fucking a non-harem girl, I always expect some kind of reward, so what are you going to offer me in exchange for letting you go? And I don't mean rubles!"
tn "I have some spy equipment that might be useful to you. Or money. 50 New dollars for my freedom. It's my best offer."
menu:
    "I'll take the money.":
        tn "Now you're absolutely LOADED."
        mc "Hang on, let me count it, you gave me fifty one dollar notes by the looks of it..."
        mc "One... Two... Three..."
        hide titiana01 with moveoutright
        mc "Four...Five... Seven. No, hang on, six... Hey, where did she go?"
        $ money += 50
        mc "She escaped while I was counting. That's just below the belt. You just can't trust Russian spies these days."
        jump BackHex65
    "I'll take the spy equipment, whatever the hell it is. What is it by the way?":
        pass        
tn "Wait a minute, I'll fetch it."
window hide
hide titiana01 with moveoutright
show titianaend02 with moveinright
tn "This fine French moustache, ideal for a disguise. HAN HAN HAN."
mc "Sorry Monsieur, but who are you? I was waiting for a Russian lady, did you happen to see her, s'il vous plaît?"
hide titianaend02
show titianaend03
with fastdissolve
tn "See, you actually think I'm French just because I'm wearing it, this is how cunning this disguise is! But I am ACTUALLY... "
play sound "Sounds/ripping.mp3"
hide titianaend03
show titianaend04
with dissolve
tn "...Titiana!"
window hide
play sound "Sounds/dundun.mp3"
$ renpy.pause(1.0, hard=True)
mc "Oh my God, it was YOU all along? I was completely fooled, as I'm guessing most players were, the transformation induced by this fine moustache in indeed remarkably cunning."
tn "So it's a deal then, this fine French moustache for my freedom?"
window hide
show frenchmoustache at posmission
$ renpy.pause(1.0, hard=True)
pause
hide frenchmoustache
$ moustache = True
mc "And I'd better not see you again rummaging around our state secrets, you hear me?"
hide titianaend04
show titianaend02
with dissolve
tn "Now if you'll excuse me sir, I have a train to catch to Paris. HAN HAN HAN."
mc "Of course Monsieur, I shall not keep you waiting, please send my regards to Madame Macron."
window hide
hide titianaend02 with moveoutright
mc "Where the hell did Titiana go? She must have escaped while I was speaking with this French gentleman. Shucks, I was going to ask her who really killed JFK. I guess we'll just never know...."
$ clearedhex65 = True

label BackHex65:
stop music
$ period += 1
scene command01
show lena01
with fade
if alone:
    le "So, what do you have to report about area G5, [name]?"
if alone == False:
    le "So, what do you have to report about area G5, scouts?"
mc "I found Mar-a-Gogo and I foiled a Russian spy attempt to obtain state secrets from First Lady Melania."
hide lena01
show lena07
with fastdissolve
le "Well, that's impressive. Can I reasonably expect that you brought Melania back so we can hold her captive and blackmail President Trumpf?"
mc "Err... No. She cunningly escaped to the Supreme White House while I was... err... dealing with the Russian agent."
hide lena07
show lena03
with fastdissolve
le "Something seems fishy about your story..."
mc "But the hex is now cleared, Chief!"
hide lena03
show lena06
with fastdissolve
le "Right. You've got that going for you at least... You're dismissed."
hide lena06 with dissolve
jump LeaveCommand    
        
label AvengersMission:
stop sound
$ explored = True
scene widowdesertavengers with fade
play music "Sounds/desertwind01.mp3"
mc "It's quite dusty here again."    
if withbe:
    be  "A sandstorm must be brewing...AGAIN."
if withpe:
    pe  "A sandstorm must be brewing...AGAIN."
mc "Yeah, but that was planned. We'll just stay put and wait for the Black Widow. She always appears during sandstorms in this place anyway."       
play music "Sounds/desertwind02.mp3"
show sandstorm02
mc "Ah, there comes the sandstorm..."
mc "Come on Scarl... I mean, come on Black Widow, we don't have all day!"
hide sandstorm02
show widowsand01
show sandstorm02
with dissolve
mc "Ah, there she is! Hi Black Widow!"
hide widowsand01
hide sandstorm02
show widowsand04
show sandstorm02
wi "Captain America? With Captain Marvel no less! Are we all here for sex or to finally fight for the GOOD CAUSE?"
mc "This time, it's for the good cause. I need to infiltrate Trumpf City!"
hide widowsand04
hide sandstorm02
show widowsand02
show sandstorm02
wi "Ah, the lair of the Evil One! My nemesis the Taskmaster, Mister Hydra, the Republican Guardian... I've run out of names."
mc "I've met a super-buff Canadian chick and I reckon we should go and see her. We'll need all the muscle we can muster to beat Sean Insannity!"
hide widowsand02
hide sandstorm02
show widowsand04
show sandstorm02
wi "Err, why is that?"
mc "He's turned into an 8ft tall green monster."
hide widowsand04
hide sandstorm02
show widowsand01
show sandstorm02
wi "I see, so this is like a, err.. physically dangerous mission, like for real?"
mc "Of course, the New Avengers aren't scared of REAL FIGHTS!"
wi "Sure, sure... I mean, I haven't had much training but, I could be useful..."
hide widowsand01
hide sandstorm02
show widowsand03
show sandstorm02
wi "...As the Leader of the NEW AVENGERS!"
mc "So let's go! To CANADA! You can ride with me Black Widow!"
stop music
jump CanadaBackWorkedb

label AvengersMissionNew:
stop sound
$ explored = True
scene widowdesertavengers with fade
play music "Sounds/desertwind01.mp3"
mc "I'll wait for her. I just know she'll come even if there's a sandstorm brewing..."    
play music "Sounds/desertwind02.mp3"
show sandstorm02
mc "Ah, there comes the sandstorm..."
window hide
hide sandstorm02
show widowsand01
show sandstorm02
with dissolve
mc "And... There she is. Hi Black Widow!"
hide widowsand01
hide sandstorm02
show widowsand04
show sandstorm02
wi "Captain America? Again?"
mc "Yeah, I need your help. AGAIN. To enter Trumpf City through the sewers. AGAIN."
hide widowsand04
hide sandstorm02
show widowsand02
show sandstorm02
wi "But where is Captain Marvel?"
mc "We don't need her, and we don't need Captain Canuck either since we've already defeated Sean Insannity and the coast is clear. Time is of the essence, let's go!"
hide widowsand02
hide sandstorm02
show widowsand03
show sandstorm02
wi "Alright, the Black Widow is READY!"
stop music
$ period += 1
play music "Sounds/desertwind01.mp3"
scene northgate01 with fade
mc "The coast is clear..."
scene northgate03
show hannityvictory02
with dissolve
mc "And that radioactive carcass is still there. I guess radioactivity preserves from being eaten by rats."
wi "Don't get any funny ideas. Let's move on..."
scene northgate04 with fade
$ withwi = True
mc "Finally, the end of the tunnel! Supreme White House, here we come, and this time it's to KICK ASS!"
jump WhiteHouse
