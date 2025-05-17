label Dojo:
$ seendojo = True
$ loc = "dojo"
if pregmi and pregmistart >= 4:
    scene dojo01 with dissolve
    mc "Oh, it appears Michiko is not here today. Must be because I knocked her up real good. She must be resting."
    jump Main01
scene dojo01
show michiko01
with dissolve
if michikodatecancelled:
    mi "I'm so sad you couldn't come last night... I hope you can come this time?"
    if day == 4 or day == 5:
        mc "Except it's the weekend coming up, how about Sunday evening rather?"
        su "Alright, Sunday evening it is then!"
        $ michikodatesunday = True
        $ spokemichiko = True
        mi "So, apart from that are you here to train how to use every part of your body as a lethal weapon [name]?"
        jump MichikoDialogueMenu01    
    mc "Sure, I should be able to make it this time. If I don't get injured again in some horrible way..."
    $ michikodateon = True    
    mi "So, apart from that are you here to train how to use every part of your body as a lethal weapon [name]?"
    $ spokemichiko = True
    jump MichikoDialogueMenu01
if not (day == 5 or day == 6) and lustmi >= 2 and michikodatedone == False and not period == 3:
    mi "Oh, hi [name]. I'm glad you came to visit me... *wink*"
    mi "I'd like to know you a bit better... Why don't you come to my place tonight?"
    menu:
        "Sure Michiko, thanks for inviting me!":            
            $ michikodateon = True
            mi "You're welcome! I can't wait for you to come over! *wink*"
            mc "(Cool, I have a date with Michiko!)"
            mi "So, apart from that are you here to train how to use every part of your body as a lethal weapon [name]?"
            $ spokemichiko = True
            jump MichikoDialogueMenu01
        "I'm afraid I'm too busy tonight. Another day perhaps.":            
            mi "I understand, you're a HERO, right? I'll ask you out another day then..."
            mi "So, apart from that are you here to train how to use every part of your body as a lethal weapon [name]?"
            jump MichikoDialogueMenu01
if not (day == 4 or day == 5) and lustmi >= 2 and michikodatedone == False and period == 3:
    mi "Oh, hi [name]. I'm glad you came to visit me... *wink*"
    mi "I'd like to know you a bit better... Why don't you come to my place tomorrow evening?"
    menu:
        "Sure Michiko, thanks for inviting me!":            
            $ michikodateontomorrow = True
            mi "You're welcome! I can't wait for you to come over! *wink*"
            mc "(Cool, I have a date with Michiko!)"
            mi "So, apart from that are you here to train how to use every part of your body as a lethal weapon [name]?"
            $ spokemichiko = True
            jump MichikoDialogueMenu01
        "I'm afraid I'm too busy tonight. Another day perhaps.":            
            mi "I understand, you're a HERO, right? I'll ask you out another day then..."
            mi "So, apart from that are you here to train how to use every part of your body as a lethal weapon [name]?"
            jump MichikoDialogueMenu01
            
mi "Are you here to train how to use every part of your body as a lethal weapon [name]?"
label MichikoDialogueMenu01:
show michiko01
menu:
    "Yes.":
        mi "Then put on your kimono and join me on the tatami..."
        if toldtatami == True:
            mc "Rightee-o."            
        if toldtatami == False:
            $ toldtatami = True
            mc "The what?"
            hide michiko01
            show michiko05
            with fastdissolve
            mi "(sigh). The mat."
        jump Dojo02
    "No, I just want to talk to you.":
        hide michiko01
        show michiko02 with fastdissolve
        mi "Oh? What can I do for you?"
        label MichikoDialogueMenu02:
        show michiko02
        menu:
            "I like your outfit, it really hugs your curves well.":
                hide michiko02
                show michiko09
                with fastdissolve
                mi "You think so? I inherited it from my later father's shop. He sold all sorts of traditional outfits. This is one that survived..."
                mc "Lucky for us! And lucky that it's like... err... big enough up top for you!"
                hide michiko09
                show michiko08
                with fastdissolve
                mi "Yes, they've grown quite big haven't they? But they don't stop me from being VERY flexible and combat-ready let me assure you!"
                hide michiko08
                $ spokemichiko = True
                jump MichikoDialogueMenu01 
            "How did you end up here?" if spokemichiko01 == False:
                hide michiko02
                show michiko06
                with fastdissolve
                mi "I was buried under the rubbles of a temple. But I FOUGHT my way out. through the ash and the radioactivity."
                mc "So did I. I was buried. And then I managed to dig my way out."
                hide michiko06
                show michiko04
                with fastdissolve
                mi "I heard you hibernated for YEARS. I got out quickly thanks God. But we do have something in common..."
                call LustPlusMichiko
                hide michiko04
                $ spokemichiko = True
                $ spokemichiko01 = True
                jump MichikoDialogueMenu01
            "I would like to gift you a beautiful necklace made of rare gems." if necklace:
                hide michiko02
                show michiko08 with fastdissolve
                mi "Really? That is such a kind gift, you truly are in tune with your inner Spirits."
                scene dojo01 blurred
                show michikonecklace
                with dissolve
                $ necklace = False
                mi "It's beautiful... and it's blue... You did it on purpose didn't you? Thank you so much, I will treasure it."
                call LustPlusMichiko
                mi "I will go back to my quarters to polish the gem with Japanese lacquer."
                $ period += 1
                scene dojo01 with dissolve
                jump Main01            
    "I can already use one part of my body as a lethal weapon. My COCK.":
        if lustmi>=2:
            hide michiko01
            show michiko02
            with fastdissolve
            mi "Yes, I... can see that. Seeing how hugely HUNG you are! *wink*"
            hide michiko02
            $ spokemichiko = True
            jump MichikoDialogueMenu01            
        if lustmi<=1:
            hide michiko01
            show michiko05
            with fastdissolve
            mi "Bragging is for losers. Or total narcissistic sociopaths. You must CONCENTRATE if you ever want to learn how to fight properly [name]!"
            mc "Ah, right. Thanks for the tip, I'll bear that in mind..."
            hide michiko05
            $ spokemichiko = True
            jump MichikoDialogueMenu01
    "I would like to offer you a beautiful gem necklace." if necklace:
        scene dojo01 blurred
        show michikonecklace
        mi "It's...stunning. I feel empowered by nature's bounty!"
        $ necklace = False
        mc "And it's blue too. That's why I thought of you immediately when I found it..."   
        call LustPlusMichiko
        scene dojo01 with dissolve
        $ spokemichiko = True
        jump MichikoDialogueMenu01
    "I'd like to offer you a bouquet of wild flowers I collected." if bouquet >= 1:
        hide michiko01
        show michiko06
        with fastdissolve
        mi "For me? Wow, it's beautiful and I really needed some for my private quarters, thanks a lot [name]!"
        call LustPlusMichiko
        hide michiko06
        $ spokemichiko = True
        $ bouquet -= 1
        jump MichikoDialogueMenu01
    "I think it's time for you to join my harem Michiko, don't you think?" if lustmi >= 4 and haremmi == False and michikoharem == False and girlsinharem <= 5 and michikodatedone:
        mi "I thought you would never ask! Yes I do think!"
        $ haremmi = True
        $ girlsinharem += 1
        $ michikoharem = True
        window hide
        show haremmichiko at plus
        $ renpy.pause(2.0, hard=True)
        hide haremmichiko
        mc "I'll call you at nights, so we can get better acquainted... Sexually that is."
        mi "I can't wait to see what you have in store for me [name]. *wink*."
        $ spokemichiko = True
        jump MichikoDialogueMenu01
    "I think it's time for you to re-join my harem Michiko. For some BRUTAL fucking." if lustmi >= 4 and haremmi == False and michikoharem == True and michikodismissed == False and girlsinharem <= 5:
        mi "Eventhough you BRUTALLY dismissed me last time, I will gladly re-join your harem. My pussy has its needs that only YOUR MONSTERCOCK can fulfill..."
        $ haremmi = True
        $ girlsinharem += 1
        window hide
        show haremmichiko at plus
        $ renpy.pause(2.0, hard=True)
        hide haremmichiko
        mc "I'll call you when it's time for you to receive some BRUTAL pounding from it then..."
        mi "I can't wait to see what you have in store for me [name]. *wink*."
        $ spokemichiko = True
        jump MichikoDialogueMenu01                
    "Leave":
        mc "I need to go."
        hide michiko01
        show michiko03
        with fastdissolve
        mi "Well go then. And leave me all alone... *sigh*"
        hide michiko03
        if spokemichiko:
            $ period += 1
        jump Main01

label Dojo02:
if mccombat == 0 and fightmi == 0:
    jump DojoFirstTraining
if mccombat == 0 and fightmi >= 1:
    jump DojoSecondTraining
if mccombat == 1 and fightmi >= 1:
    jump DojoThirdTraining
if mccombat >= 2:
    jump DojoTraining
    
label DojoFirstTraining:
scene dojo01 with fade
show michikodojo01
mi "So, are you feeling ready for your very first close combat training session [name]?"
mc "Yes I am. Muscles are rumbling, fists are flexing, get ready for the beating of your..."
hide michikodojo01
show michikodojo02
with fastdissolve
mi "Kurae!"
hide michikodojo02
show michikodojo03
with fastdissolve
window hide
play sound "Sounds/punch.mp3"
pause 1
hide michikodojo03
scene dojomichiko01 with dissolve
mi "You were saying?"
mc "Ggg... Ouch!"
$ mcinjuredmichiko = True
$ fightmi += 1
call MCInjury
scene dojomichiko02 with dissolve
mi "Oh, I think I hurt you. See? Despite your huge muscles, you were no match against a skilled fighter like me..."
mi "I'm sorry you had to learn the hard way... Does it hurt a lot? Where does it hurt?"
mc "Everywhere!"
scene dojomichiko03 with dissolve
mi "Even there? There does seem to be a great big lump right THERE..."
call LustPlusMichiko
mc "Yeah, you kicked me right in the nuts!"
mi "I'll take to you the medbay then if you are really hurt...."
mi "But it proves that you clearly need to train A LOT. If you follow three sessions, you will definitely improve under my expert guidance!"
$ mccombatlevel += 1
jump Medbay

label DojoSecondTraining:
scene dojo01
show michikodojo01
with fade
mi "Let me show you the basic moves you need to master for efficient close combat. First off, defensive moves."
window hide
hide michikodojo01
show michikodojotraining
pause 2.0
mi "Did you get it?"
mc "Err... it was going a bit fast but I got the jest of it."
hide michikodojotraining
show michikodojo01
with fastdissolve
mi "Then show me. I'll attack you and you defend."
mc "Please don't aim for my ba..."
hide michikodojo01
show michikodojo02
with fastdissolve
mi sidemi "Kurae!"
hide michikodojo02
show michikodojo03
with fastdissolve
window hide
play sound "Sounds/punch.mp3"
pause 1
hide michikodojo03
scene dojomichiko01 with dissolve
mi "Oh, sorry, did I hurt your BIG balls?"
mc "No I'm fine... Ouch."
mi "Let's do this again until you learn this move..."
$ period += 1
scene dojo01
show michiko01
with fade
mi "I think our training went well. You have improved. Somewhat."
$ mccombatlevel += 1
if mccombatlevel == 1:
    mc "A couple more training sessions like this one this week and I'll get better at close combat for sure!"   
if mccombatlevel == 2:
    mc "Another training session like this one this week and I'll get better at close combat for sure!"   
if mccombatlevel == 3:
    mc "I can feel.... closer to Bruce Lee suddenly."
    call PlusCombat
    $ mccombatlevel = 0
hide michiko01
show michiko06
with fastdissolve
mi "Come back again to train some more [name]!"
hide michiko06 with dissolve
jump Main01

label DojoThirdTraining:
scene dojo01
show michikoattack04
with fade
mi "The next lessons is about ATTACK. When fighting two opponents."
mc "I don't think this ever happens in this game."
mi "*sigh* Just watch and LEARN."
window hide
hide michikoattack04
show michikodojoattack
play sound "Sounds/womangroan.mp3"
pause 2.0
mi "Did you get it?"
mc "Err... it was going a bit fast but I got the jest of it."
hide michikodojoattack
show michikodojo01
with fastdissolve
mi "Then show me. Attack me."
mc "Alright, prepare to get your ass kicked Michiko!"
hide michikodojo01
show michikodojo02
with fastdissolve
mi sidemi "Kurae!"
hide michikodojo02
show michikodojo03
with fastdissolve
window hide
play sound "Sounds/punch.mp3"
pause 1
hide michikodojo03
scene dojomichiko01 with dissolve
mi "Oh, sorry, did I hurt your BIG balls?"
mc "No I'm fine... Ouch."
mi "Let's do this again until you learn this move..."
$ period += 1
scene dojo01
show michiko01
with fade
mi "I think our training went well. You have improved. Somewhat."
$ mccombatlevel += 1
if mccombatlevel == 1:
    mc "A couple more training sessions like this one this week and I'll get better at close combat for sure!"   
if mccombatlevel == 2:
    mc "Another training session like this one this week and I'll get better at close combat for sure!"   
if mccombatlevel == 3:
    mc "I can feel.... closer to Bruce Lee suddenly."
    call PlusCombat
    $ mccombatlevel = 0
hide michiko01
show michiko06
with fastdissolve
mi "Come back again to train some more [name]!"
hide michiko06 with dissolve
jump Main01

label DojoTraining:
scene dojo01
show michikodojo01
with fade
mi "What should we train for today? Attack or defence?"
menu:
    "Attack":
        jump DojoAttack
    "Defence":
        jump DojoDefence
    "Skip scene":
        mc "Let's pretend I did all that and I improved."
        $ period += 1
        $ mccombatlevel += 1
        if mccombatlevel == 1:
            mc "A couple more training sessions like this one this week and I'll get better at close combat for sure!"   
        if mccombatlevel == 2:
            mc "Another training session like this one this week and I'll get better at close combat for sure!"   
        if mccombatlevel == 3:
            mc "I can feel.... closer to Bruce Lee suddenly."
            call PlusCombat
            $ mccombatlevel = 0        
        hide michikodojo01
        show michiko06
        with dissolve
        mi "Come back again to train some more [name]!"
        hide michiko06 with dissolve
        jump Main01

label DojoAttack:
hide michikodojo01
show michikoattack04
with dissolve
mi "Ok, let me show you some offensive moves then."
window hide
hide michikoattack04
show michikodojoattack
play sound "Sounds/womangroan.mp3"
pause 2.0
mi "Did you get it?"
mc "Err... it was going a bit fast but I got the jest of it."
hide michikodojoattack
show michikodojo01
with fastdissolve
mi "Then show me. Attack me."
mc "Alright, prepare to get your ass kicked Michiko!"
hide michikodojo01
show michikodojo02
with fastdissolve
mi sidemi "Kurae!"
hide michikodojo02
show michikodojo03
with fastdissolve
window hide
play sound "Sounds/punch.mp3"
pause 1
hide michikodojo03
scene dojomichiko01 with dissolve
mi "Oh, sorry, did I hurt your BIG balls?"
mc "No I'm fine... Ouch."
mi "Let's do this again until you learn this move..."
$ period += 1
scene dojo01
show michiko01
with fade
mi "I think our training went well. You have improved. Somewhat."
$ mccombatlevel += 1
if mccombatlevel == 1:
    mc "A couple more training sessions like this one this week and I'll get better at close combat for sure!"   
if mccombatlevel == 2:
    mc "Another training session like this one this week and I'll get better at close combat for sure!"   
if mccombatlevel == 3:
    mc "I can feel.... closer to Bruce Lee suddenly."
    call PlusCombat
    $ mccombatlevel = 0
hide michiko01
show michiko06
with fastdissolve
mi "Come back again to train some more [name]!"
hide michiko06 with dissolve
jump Main01

label DojoDefence:
mi "Ok, let me show you some defensive moves then."
window hide
hide michikodojo01
show michikodojotraining
pause 2.0
mi "Did you get it?"
mc "Err... it was going a bit fast but I got the jest of it."
hide michikodojotraining
show michikodojo01
with fastdissolve
mi "Then show me. I'll attack you and you defend."
mc "Please don't aim for my ba..."
hide michikodojo01
show michikodojo02
with fastdissolve
mi sidemi "Kurae!"
hide michikodojo02
show michikodojo03
with fastdissolve
window hide
play sound "Sounds/punch.mp3"
pause 1
hide michikodojo03
scene dojomichiko01 with dissolve
mi "Oh, sorry, did I hurt your BIG balls?"
mc "No I'm fine... Ouch."
mi "Let's do this again until you learn this move..."
$ period += 1
scene dojo01
show michiko01
with fade
mi "I think our training went well. You have improved. Somewhat."
$ mccombatlevel += 1
if mccombatlevel == 1:
    mc "A couple more training sessions like this one this week and I'll get better at close combat for sure!"   
if mccombatlevel == 2:
    mc "Another training session like this one this week and I'll get better at close combat for sure!"   
if mccombatlevel == 3:
    mc "I can feel.... closer to Bruce Lee suddenly."
    call PlusCombat
    $ mccombatlevel = 0
hide michiko01
show michiko06
with fastdissolve
mi "Come back again to train some more [name]!"
hide michiko06 with dissolve
jump Main01