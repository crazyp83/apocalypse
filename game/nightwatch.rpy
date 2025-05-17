label NightWatch:
hide screen mcstats
hide screen calendar
scene nightwatch01 with fade
play music "Sounds/desertwind01.mp3"
$ d4rollnightwatch=renpy.random.randint(1,4)

if d4rollnightwatch == 1:
    jump LenaNightWatch
if d4rollnightwatch == 2:
    jump RubyNightWatch
if d4rollnightwatch == 3:
    jump BellaNightWatch
if d4rollnightwatch == 4:
    jump PennyNightWatch
 
label LenaNightWatch:
scene nightwatch01 with fade
show lenawatch01 with moveinright
if seenlenawatch:
    mc "Ah, we have a nightwatch duty together it appears, Chief."
    le "I've got to make sure at least ONE watchman is doing his job properly..."
    mc "It sounded like a subtle jab, but I'm not sure..."
if seenlenawatch == False:
    mc "Chief Lena???"
    le "Yes, why are you acting so surprised? I do my duty like everyone else."
    $ seenlenawatch = True
$ d2lenawatch=renpy.random.randint(1,2)
if d2lenawatch == 1:
    hide lenawatch01
    show lenawatch02
    with dissolve
    le "I'll be handling the rifle tonight. And you the binoculars."
    jump LenaRifle
if d2lenawatch == 2:
    hide lenawatch01
    show lenawatch03
    with dissolve
    le "You'll be handling the rifle tonight."
    mc "Roger that, Chief."
    window hide
    hide lenawatch03
    show mcwatch02 at farleft03
    show lenawatch05 at farright
    with dissolve
    pause 2.0
    call Coyote
    jump LenaWatchEnd

label LenaRifle:
hide lenawatch02
show mcwatch04 at farleft02
show lenawatch07 at right
with fade
window hide
show coyote01 with dissolve
pause 1.0
hide coyote01
show coyote02
with fastdissolve
play sound "v061/coyote.mp3"
mc "Coyote at 12, Chief."
hide lenawatch07
show lenawatch08 at farright
with fastdissolve
le "I see it."
window hide
play sound "Sounds/gun.mp3"
$ renpy.pause(1.0, hard=True)
stop sound
hide coyote02
show coyote04
with dissolve
stop sound
$ renpy.pause(1.0, hard=True)
hide lenawatch08
show lenawatch07 at right
le "And now it's dead. That's how you do it."
hide mcwatch04
show mcwatch05 at farleft02
with fastdissolve
mc "Wow, nice shot Chief."

label LenaWatchEnd:
scene nightwatch02
show lenawatch04 at right
show mcwatch03 at left
with fade
le "It's dawn. Time to go back to the compound. And for you to go back to work. Or school. One or the other."
if nightwatchlenatold == False:
    mc "Is that all that ever happens during nightwatch?"
    le "Yes, and it's a good thing. Imagine if it had been some Trumpf militia mob storming our compound instead of a lone coyote?"
    mc "That would be terrible indeed. Trying to overthrow a democratically-elected leader such as yourself... Impeachable even I'd say."
    $ nightwatchlenatold = True
    jump NightwatchEnd
mc "Oh God, I'm just so tired..."
jump NightwatchEnd

label RubyNightWatch:
show rubywatch01 with moveinright
ru "Ah, I'm paired with you tonight..."
mc "Yep, isn't that great?"
ru "Let's get organized here, what will it be for you, binoculars or rifle?"
menu:
    "Binoculars, thanks.":
        if rubytoldpoof == False:
            hide rubywatch01
            show rubywatch02
            with fastdissolve
            ru "What are you, a poof or something?"
            mc "Err..."
            $ rubytoldpoof = True
        hide rubywatch01
        hide rubywatch02
        show rubywatch03
        with fastdissolve
        ru "Fine by me, I'll handle the rifle. Like a MAN."
        hide rubywatch03
        window hide
        jump RubyBinoculars
    "The rifle, thanks.":
        ru "Trying to be a REAL man, hey?"
        if haremru:
            mc "I remind you that you are in MY harem. Which definitely makes me a real MAN."
            hide rubywatch01
            show rubywatch03
            with fastdissolve        
            ru "Ooh, touchy. Yeah, I know you're a MAN in the sack [name]. Now prove you can be a MAN on the outside too. Shoot anything that moves."
            hide rubywatch03
            window hide
            jump RubyRifle
        mc "I AM a real man!"
        hide rubywatch01
        show rubywatch03
        with fastdissolve        
        ru "Then prove it. Shoot anything that moves."
        hide rubywatch03
        window hide
        jump RubyRifle

label RubyRifle:
hide rubywatch03
show mcwatch02 at farleft03
show rubywatch07 at farright
with dissolve
pause 2.0
call Coyote
jump RubyWatchEnd

label RubyBinoculars:
hide rubywatch03
hide rubywatch02
show rubywatch05 at right
show mcwatch04 at farleft02
with fade
window hide
show coyote01 with dissolve
pause 1.0
hide coyote01
show coyote02
with fastdissolve
play sound "v061/coyote.mp3"
mc "I see a coyote. And I hear it too."
hide rubywatch05
show rubywatch06 at right
with fastdissolve
ru "So do I..."
window hide
play sound "Sounds/gun.mp3"
$ renpy.pause(1.0, hard=True)
stop sound
hide coyote02
show coyote04
with dissolve
stop sound
$ renpy.pause(1.0, hard=True)
hide mcwatch04
show mcwatch05 at farleft02
with fastdissolve
mc "Wow, that was quick."
ru "I don't mess around."

label RubyWatchEnd:
scene nightwatch02
show rubywatch09 at right
show mcwatch03 at left
with fade
ru "It's dawn. Time to go back to the compound. And the fumes of the workshop."
if nightwatchrubytold == False:
    mc "Is that all that ever happens during nightwatch?"
    ru "As of v0.7, yes. If you've got any better ideas, tell the dev and stop moaning."
    mc "Maybe I will. Maybe I will."
    $ nightwatchrubytold = True
jump NightwatchEnd

label BellaNightWatch:
show bellawatch01 with moveinright
if seenbellawatch:
    mc "Bella, how nice it is to see you tonight as my watchman partner...."
    be "Don't flatter me, we have a JOB to do. We must protect the compound. And its Church."
if seenbellawatch == False:
    mc "Are we supposed to watch together?"
    be "Yes, always in pairs. In case someone falls asleep."
    $ seenbellawatch = True
be "I would appreciate it if you let me do the shooting. I am the most EXPERIENCED scout here."
menu:
    "No way! I love shooting stuff and Chief Lena put me in charge tonight!":
        hide bellawatch01
        show bellawatch02
        with fastdissolve
        be "Umpf... Fine..."
        $ nightwatchbellaupset -= 1
        if nightwatchbellaupset <= 3:
            call LustMinusBella
            $ nightwatchbellaupset = 0
        hide bellawatch02
        show bellawatch03 at farright
        show mcwatch02 at farleft03
        call Coyote
        jump BellaWatchEnd
    "Ok, ladies first...":
        be "Thank you [name]..."
        $ nightwatchbellaupset += 1
        if nightwatchbellaupset >= 3:
            call LustPlusBella
            $ nightwatchbellaupset = 0
        jump BellaCoyote
 
label BellaCoyote:
hide bellawatch01
show bellawatch05 at right
show mcwatch04 at farleft03
with dissolve
pause 2.0
show coyote01 with dissolve
pause 1.0
hide coyote01
show coyote02
with fastdissolve
play sound "v061/coyote.mp3"
mc "I see a coyote over there. Shoot it, Bella!"
be "I won't. If it's not meant to be eaten, it's not meant to be killed. So sayeth the Holy Spurt."
hide mcwatch04
show mcwatch05 at farleft02
with fastdissolve
mc "I didn't know he could talk."
hide coyote02
show coyote03
with dissolve
pause 1.0
hide coyote03 with fastdissolve
mc "Oh well, there he goes. You missed your chance."
hide bellawatch05
show bellawatch06 at right
with fastdissolve
be "I am fine with it. He was no threat to us."
mc "He could maybe have made a tasty coyote burger though..."

label BellaWatchEnd:
scene nightwatch02
show bellawatch07 at right
show mcwatch03 at left
with fade
be "It's dawn. Time to go back to the compound. In time for lauds."
if nightwatchbellatold == False:
    mc "Is that all that ever happens during nightwatch?"
    be "No, sometimes some young naked muscle hero with a huge hanging soft cock appears out of nowhere."
    mc "I see what you did there."
    $ nightwatchbellatold = True
jump NightwatchEnd

label PennyNightWatch:
show pennywatch01 with moveinright
if seenpennywatch == False:
    mc "Penny, fancy seeing you here."
    pe "And fancy seeing YOU here *wink*."
    $ seenpennyawatch = True
if seenpennywatch == False:
    mc "Ah, together again. All night long..."
    pe "Try and focus tonight, you naughty boy..."
if spliff and spliffused == False:
    menu:
        "What for, it's usually boring, why don't we smoke a joint?" if spliff and spliffused == False:
            $ spliff = False
            $ spliffused = True
            pe "I guess you're right. And we're FREE here to do whatever we want. In the great Road Wilderness."
            show pennywatch06
            pe "Oh yeah... This stuff is good. Where do you get it?"
            mc "I've got my secret suppliers..."
            call LustPlusPenny   
            pe "They're good.... Whoever they are..."
            jump PennyWatchEnd
        "Alright, give me the rifle and I'll shoot that damn coyote that keeps spawning.":
            jump NightwatchPenny02

label NightwatchPenny02:
pe "And not MISS hopefully."
window hide
hide pennywatch01
show mcwatch02 at farleft03
show pennywatch03 at farright
with dissolve
pause 2.0
call Coyote
jump PennyWatchEnd

label PennyWatchEnd:
scene nightwatch02
show pennywatch05 at right
show mcwatch03 at left
with fade
pe "It's dawn. And now our watch has ended."
if nightwatchpennytold == False:
    mc "Is that all that ever happens during nightwatch?"
    pe "Yes, but it's a extra way of earning money and vermin shot points to raise your Road Warrior standing."
    mc "Ah, so it counts like a shot camel then? Good to know..."
    $ nightwatchpennytold = True
jump NightwatchEnd

label Coyote:
window hide
show coyote01 with dissolve
pause 1.0
hide coyote01
show coyote02
with fastdissolve
play sound "v061/coyote.mp3"
if d4rollnightwatch == 1:
    le "I see a coyote over there. Are you ready to shoot it?"
if d4rollnightwatch == 2:
    ru "I spotted a coyote. Shoot the damn vermin!"
if d4rollnightwatch == 3:
    be "Did you hear that. It's a coyote. Get ready to scare him off."
    mc "Shooting it should do the trick."
if d4rollnightwatch == 4:
    pe "There's a coyote on that hill. You think you can shoot it from where you're standing?"
    mc "Only one way to find out..."

hide mcwatch02
show mcwatch01 at farleft
with fastdissolve
call DiceRoll
$ dshootroll=mcfirearms+diceroll
if (dshootroll >= 6 and not diceroll == 1) or diceroll == 6:
    window hide
    play sound "Sounds/gun.mp3"
    $ renpy.pause(1.0, hard=True)
    hide coyote02
    show coyote04
    with dissolve
    stop sound
    $ renpy.pause(1.0, hard=True)
    jump CoyoteWin
if (dshootroll <= 5 and not diceroll == 6) or diceroll == 1:
    window hide
    play sound "Sounds/gun.mp3"
    $ renpy.pause(1.0, hard=True)
    hide coyote02
    show coyote03
    with dissolve
    stop sound
    pause 1.0
    hide coyote03 with fastdissolve
    jump CoyoteLose
    
label CoyoteWin:
mc "Yeah, I got him! And I made even more noise by shooting it than he did."
$ camelsshot += 1
if camelsshot >= 10:
    mc "*I think I'm getting really good at shooting things in the wild...*"
    call PlusWarrior
    call MinusSierra
    $ camelsshot = 0        
if d4rollnightwatch == 1:
    hide lenawatch05
    show lenawatch06 at farright
    with fastdissolve
    le "Well done [name]. I didn't realize you were so good at handling guns... I like men who can handle guns. I've only ever had dates at a shooting range when I was young..."
    call LenaDateConvince
    if lenaconvincedate >= 3:
        "You can now invite Lena on a date. Talk to her in the command center."        
    mc "Well, maybe one day I'll take you to a DIFFERENT place. On a date."
    le "Oh, you! *blush*"
    return
if d4rollnightwatch == 2:
    hide rubywatch07
    show rubywatch08 at farright
    with fastdissolve
    ru "Nice shooting [name]. I'm impressed."
    $ nightwatchshoot += 1
    if nightwatchshoot >= 3:
        call LustPlusRuby
        $ nightwatchshoot = 0
    return
if d4rollnightwatch == 3:
    hide bellawatch03
    show bellawatch04 at right
    with fastdissolve
    be "You got him. The Phallus must have wanted this coyote dead."
    mc "My rifle wanted him dead."
    return
if d4rollnightwatch == 4:
    pe "I think it's dead. You're on your way to becoming a better Road Warrior [name]."
    return

label CoyoteLose:
mc "Damn it, he escaped. He was just too quick, like Wile E. Coyote in a racecar."
if d4rollnightwatch == 1:
    hide lenawatch05
    show lenawatch06 at farright
    with fastdissolve
    le "That's not good. He'll be howling all night and disturbing everyone's sleep."
    return
if d4rollnightwatch == 2:
    hide rubywatch07
    show rubywatch08 at farright
    with fastdissolve
    ru "You suck at this. Big time."
    $ nightwatchshoot -= 1
    if nightwatchshoot <= 3:
        call LustMinusRuby
        $ nightwatchshoot = 0
    return
if d4rollnightwatch == 3:
    hide bellawatch03
    show bellawatch04 at right
    with fastdissolve
    be "The Phallus Lord is protecting this coyote. There must be a purpose."
    mc "To stop me from becoming a Road Warrior apparently..."
    return
if d4rollnightwatch == 4:
    pe "You missed. You need to train some more [name], you're a lousy marksman."
    return

label NightwatchEnd:
$ money += 5
stop music
scene bedroom01 with fade
call NewDay
jump Bedroom
