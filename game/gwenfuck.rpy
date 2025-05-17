label GwenFuck01:
hide screen calendar
hide screen mcstats
if preggw and preggwstart >= 3:
    scene bedroom01
    show gwenpregnant02b
    with fade
    gw "Why did you call me? Can't you see I need some rest? For the baby..."
    mc "Well, time to wake him up. With my COCK!"
    hide gwenpregnant02b
    show gwenpregnant02
    with fastdissolve
    gw "Are you out of your fucking mind? You're pro-abortion, is that it?"
    mc "Err... No, I mean, I'm pro-sex, that's all."
    hide gwenpregnant02
    show gwenpregnant02b
    with fastdissolve
    gw "Well, I'm ANTI-SEX while I'm pregnant! So get lost, CHILD MURDERER!"
    mc "Gee, calm down. Ok, I'll give you a leave of absence until you give birth..."
    hide gwenpregnant02b with dissolve
    $ weekfuckedgwen = True    
    jump Bedroom    
scene bedroom01 with fade
show gwenlingerie01 with moveinright
$ alienfuck = True
$ weekfuckedgwen = True        
menu:
    "Run scene":
        pass
    "Skip scene":
        jump GwenEnd

gw "I'm guessing you called me late at night to satisfy my sexual needs. So I came in lingerie."
mc "You walked through the corridors half-naked to get here?"
hide gwenlingerie01
show gwenlingerie02
with fastdissolve
gw "I was ALREADY half-naked because Debra tried to KILL me once again with one of her crazy experiments."
hide gwenlingerie02
show gwenlingerie03
with fastdissolve
gw "But that dastardly experience is over now, so we can move on to something much more PLEASURABLE..."
menu:
    "Dance for me Gwen, I want to see those big tits wiggle and jiggle in that hot lingerie!":
        jump GwenLingerie01
    "Alright! Let's not waste time then, and let's move to the bed.":
        gw "Oh, so you don't want to see me slowly peel off my lingerie?"
        mc "Nope. Let's go straight to sex. Get naked and hop on the bed."
        jump GwenFuckChoicea
        
label GwenLingerie01:
play music "v07/datemusic.mp3"
hide gwenlingerie03
show gwenlingerie04
with fastdissolve
gw "I'll show why I'm the best stripper in the compound! Go and sit in the sofa and WATCH."
scene bedroom02 blurred
show gwenwiggle
with dissolve
call screen gwenwig
screen gwenwig:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenWiggleEnd")

label GwenWiggleEnd:
hide gwenwiggle
show gwenlingerie02
with dissolve
mc "I think you don't need a hypnosis pendulum to lure guys into your lair!"
gw "What are you babbling about?"
mc "Err... Nothing. Why don't you take ALL your clothes off for me, pretty please?"
hide gwenlingerie02
show gwenlingerie03
with fastdissolve
gw "But YOU need to take yours off too! *wink*"
hide gwenlingerie03
show gwenlingerie04
with fastdissolve
gw "I'll turn round first..."
scene bedroom02 blurred
show gwenlingerie05
mc "Oh yeah! Now peel your top off and turn back round..."
hide gwenlingerie05
show gwenlingerie06
with fastdissolve
mc "Such a nice pair of titties... Could you... Peel your panties off for me now? Slowly and sensuously..."
hide gwenlingerie06
show gwenlingerie07
with fastdissolve
gw "Alright, since you ask so nicely..."
hide gwenlingerie07
show gwenlingerie08
with fastdissolve
gw "Tada! All naked and ready for that young MONSTER SCHLONG!"
mc "And I'm ready too! Come over to the sofa, it's more comfortable...."
stop music
scene gwensofa01 with dissolve
mc "Now let's see what we're working on... Yeah, fucking nice tits..."
gw "What about my pussy?"
scene gwensofa02 with dissolve
mc "Yeah, I approve, nice and tender..."
play sound "Sounds/womanmoan.mp3"
gw "Oooh..."
scene gwensofa03 with dissolve
play sound "Sounds/kiss.mp3"
gw "*kiss* Thank you for taking care of me like that..."
mc "Now it's your turn... *kiss* ...to return the favor..."
gw "Oh yeah? How? *kiss*"
scene gwensofa04 with dissolve
mc "By sucking on my throbbing manhood!"
gw "I see... It sure looks yummy..."
play music "Sounds/hardsucking.mp3"
scene gwensofa06 with fastdissolve
pause 0.2
scene gwensofa05 with fastdissolve
pause 0.2
scene gwensofa06 with fastdissolve
pause 0.2
scene gwensofa05 with fastdissolve
pause 0.2
scene gwensofa06 with fastdissolve
pause 0.2
scene gwensofa05 with fastdissolve
pause 0.2
scene gwensofa06 with fastdissolve
pause 0.2
scene gwensofa05 with fastdissolve
pause 0.2
scene gwensofa06 with fastdissolve
pause 0.2
scene gwensofa05 with fastdissolve
pause 0.2
scene gwensofa06 with fastdissolve
pause 0.2
scene gwensofa05 with fastdissolve
pause 0.2
scene gwensofa06 with fastdissolve
pause 0.2
scene gwensofa05 with fastdissolve
pause 0.2
stop music
scene gwensofa07 with dissolve
gw "*pufff* Mmh, that was a good mouth exercise. Oooh, looks like you're right on the edge already! You're drooling more spunk than a month's worth of supply from a normal man..."
mc "Oh fuck, you blew me so good... I..."
show gwensofa07b with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
gw "GO ON, CUM! Yes, that's it, empty your nuts!"
mc "AAAH!"
gw "Look at how HUGE that cumshot is, I really made you BLAST your load BIG TIME, didn't I?"
show gwensofa07b  with flash
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Oh God, Gwen... RHAAA! There's more!"
gw "Keep delivering that sweet boygoo, [name]!"
scene gwensofa08 with dissolve
stop sound
play sound "Sounds/lick.mp3"
gw "*slurp* Ssso much CUM, you must be totally empty by now..."
scene gwensofa09 with dissolve
mc "No I'm not! I'm still raring to go! Just like a 74yo on dexamethasone! I'll show you what I'm capable of!"
gw "THROW me on the bed, [name]!"

label GwenFuckChoicea:
scene bedroom03b
show gwenbed01
with dissolve
gw "And now bring that GIANT piece of boymeat over here..."

label GwenFuckChoice:
stop music
menu:
    "Let's party like it's nineteen-69!":
        gw "This party will BLOW your mind..."
        jump GwenBlowjob
    "I've got a PhD too. A Pretty huge Dick!":
        gw "Your puns are pathetic, but I'm willing to allow you to defend that so-called thesis of yours by FUCKING ME HARD!"
        jump GwenUp
    "Stand up, I'll fuck your holes into the wall!":
        gw "BOTH holes? Pound them NICE and HARD, [name]!"
        jump GwenWall
    "Well, fuck me sideways. No, I meant fuck YOU sideways!":
        gw "*sigh* Stop messing around and make good use of that HUGE WEAPON of yours!"
        jump GwenSide
    "It is my duty to repopulate the Earth. And yours to get pregnant over and over again." if preggwready >= 3 and impregnatedsomeone == False and babygwen == False:
        $ impregnatedsomeone = True
        if successmissiongw02:
            gw "Well, I finally submitted my thesis, so I can abandon all my career aspirations and become a conservative woman cum receptacle I guess."
            jump GwenImpregnation
        if successmissiongw02 == False:
            gw "I'm not done with my thesis! So no way, I still have career aspirations beyond becoming your cum receptacle!"
            mc "Ah. Shit. I guess I'll have to help you finish that damn thesis faster then to access this scene."
            gw "You're starting to understand how things work around here. \"Mission not accomplished\" yet in this case."
            jump GwenFuckChoice
    "I'm done, let's go to sleep.":
        jump GwenEnd

label GwenBlowjob:
scene bedroom48
show gwenprefuck02
with dissolve
gw "That MONSTERDONG looks so... tasty and enticing... And ready to BURST already, precum is leaking down your shaft..."
mc "Go for it, I can take your HOT mouth."
scene bedroom18
show gwenprefuck03
with dissolve
mc "...While I lick your HOT pussy."
play sound "Sounds/moaning.mp3"
gw "Ooh, just like that, yes, mmmh! Shit, I NEED to SUCK on that cock so BAD!"
scene bedroom48 blurred with dissolve
play music "Sounds/hardsucking.mp3"
label GwenBlowSlow:
hide gwenblowfast
show gwenblowslow
call screen gwenblowslow01
screen gwenblowslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenBlowFast") 

label GwenBlowFast:
mc "Oh God, take me right to the edge now, Gwen!"
hide gwenblowslow
show gwenblowfast
call screen gwenblowfast01
screen gwenblowfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("GwenBlowSlow") 

label GwenBlowEnd:
stop music
hide gwenblowslow
hide gwenblowfast
show gwenblowcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "FUCK, AAAH!"
gw "*gobble*"
hide gwenblowcum01
show gwenblowcum02
with dissolve
gw "STILL spewing???"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Yeah, You made me so...AAAHHH... HORNY!"
scene bedroom49 blurred
show gwenblowcum03
with dissolve
stop sound
gw "I thought you'd never... *slurp* ... stop cumming. You gave me a... *lick* ... MASSIVE load!"
mc "Yeah, it was pretty big even by my standards. But enough chit-chat, I'm still HARD and I want MORE!"
play sound "Sounds/lick.mp3"
gw "Let me get... *slurp* ... myself cleaned up and I'll be with you in a sec."
scene bedroom03b
show gwenbed01
with dissolve
gw "There, now come and give me some MORE of that hot fuckstick..."
jump GwenFuckChoice

label GwenUp:
scene bedroom13
show gwenpreup01
with dissolve
mc "First, I'll show you what my Pretty huge Dick can do..."
gw "Wh... What do you have in mind?"
hide gwenpreup01
show gwenpreup02
with dissolve
mc "THIS!"
gw "Mmmmh, that's a POWERFUL opening statement, [name]!"
gw "Now dwell deeper into that theory of yours, inspect every nook and cranny with your \"PhD\"!"
play music "Sounds/womansex02.mp3"
label GwenLiftSlow:
scene bedroom46
hide gwenupfast
show gwenupslow
call screen gwenupslow01
screen gwenupslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenLiftEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenLiftFast") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("GwenLiftPOVSlow") 

label GwenLiftFast:
gw "You're pummeling me so HARD! But do it FASTER now!"
scene bedroom46
hide gwenupslow
show gwenupfast
call screen gwenupfast01
screen gwenupfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenLiftEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("GwenLiftSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("GwenLiftPOVFast") 

label GwenLiftPOVSlow:
scene bedroom47
hide gwenuppovfast
show gwenuppovslow
call screen gwenuppovslow01
screen gwenuppovslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenLiftEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenLiftPOVFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("GwenLiftSlow") 

label GwenLiftPOVFast:
gw "You're pummeling me so HARD! But do it FASTER now!"
scene bedroom47
hide gwenuppovslow
show gwenuppovfast
call screen gwenuppovfast01
screen gwenuppovfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenLiftEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("GwenLiftPOVSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("GwenLiftFast")
            
label GwenLiftEnd:
gw "Time for your closing argument [name]!"
mc "I'm about to deliver it. BIG TIME!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene bedroom47 with fastdissolve
show gwenupcum01
mc "Here's my final statement! RHAAAA!"
gw "Oh God, you're ejaculating sssooo much spunk into my womb, I award you a degree CUM LOADED!"
hide gwenupcum01
show gwenupcum02
with fastdissolve
stop sound
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "AAAH! I still need to spermmark my thesis, here you go!"
scene bedroom46
show gwenupcum03
with fastdissolve
gw "Damn [name], did you get your degree in Fuckology or what?"
mc "Phew, you brought out the best in me, it was team work."
scene bedroom03b
show gwenbed01
with dissolve
gw "Come on, let's discover something new and exciting together then!"
jump GwenFuckChoice
    
label GwenWall:
scene bedroom42 with dissolve
show gwenprewall01
mc "Mmh, which hole should I choose first I wonder?..."
gw "I don't care what you choose, just FUCK ME!"
mc "Alright, I'll go with..."
menu:
    "Your backdoor!":
        hide gwenprewall01
        jump GwenWallAnalSlow
    "Your front entrance!":
        hide gwenprewall01
        jump GwenWallPussySlow

label GwenWallPussySlow:
scene bedroom42
stop music
play music "Sounds/fucksound.mp3"
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
show gwenwallpussyslow
call screen gwenwallpussyslow01
screen gwenwallpussyslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("GwenWallPussyEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenWallPussyFast") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("GwenWallAnalSlow") 

label GwenWallAnalSlow:
scene bedroom42
stop music
play music "Sounds/womansex01.mp3"
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallpussyslow
show gwenwallanalslow
call screen gwenwallanalslow01
screen gwenwallanalslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("GwenWallAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenWallAnalFast") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("GwenWallPussySlow") 

label GwenWallPussyFast:
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
show gwenwallpussyfast
call screen gwenwallpussyfast01
screen gwenwallpussyfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("GwenWallPussyEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("GwenWallPussySlow") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("GwenWallAnalSlow") 

label GwenWallAnalFast:
hide gwenwallpussyfast
hide gwenwallanalslow
hide gwenwallpussyslow
show gwenwallanalfast
call screen gwenwallanalfast01
screen gwenwallanalfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("GwenWallAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("GwenWallAnalSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("GwenWallPussySlow") 
            
label GwenWallPussyCumSlow:
stop music
play music "Sounds/fucksound.mp3"
hide gwenwallpussycumfast
hide gwenwallanalcumfast
hide gwenwallanalcumslow
show gwenwallpussycumslow
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
call screen gwenwallpussycumslow01
screen gwenwallpussycumslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("GwenWallPussyEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenWallPussyCumFast") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("GwenWallAnalCumSlow") 

label GwenWallAnalCumSlow:
stop music
play music "Sounds/womansex01.mp3"
hide gwenwallpussycumfast
hide gwenwallanalcumfast
hide gwenwallpussycumslow
show gwenwallanalcumslow
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
call screen gwenwallanalcumslow01
screen gwenwallanalcumslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("GwenWallAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenWallAnalCumFast") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("GwenWallPussyCumSlow") 

label GwenWallPussyCumFast:
hide gwenwallanalcumfast
hide gwenwallanalcumslow
hide gwenwallpussycumslow
show gwenwallpussycumfast
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
call screen gwenwallpussycumfast01
screen gwenwallpussycumfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("GwenWallPussyEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("GwenWallPussyCumSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("GwenWallAnalCumSlow") 

label GwenWallAnalCumFast:
hide gwenwallpussycumfast
hide gwenwallanalcumslow
hide gwenwallpussycumslow
show gwenwallanalcumfast
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
call screen gwenwallanalcumfast01
screen gwenwallanalcumfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("GwenWallAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("GwenWallAnalCumSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("GwenWallPussyCumSlow") 
            
label GwenWallPussyEnd:
mc "I'm about to flood your pussy, Gwen!"
gw "Go on, dump your nut inside me and then PLASTER my back with the rest, I need some skin lotion!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
hide gwenwallpussycumfast
hide gwenwallanalcumslow
hide gwenwallpussycumslow
hide gwenwallanalcumfast
if gwenwallanalcum == False and gwenwallpussycum == False:
    show gwenwallpussy05
    show gwenwallcumpussy01nocum
    with fastdissolve
    mc "You asked for it! RHAAA!!!"
    gw "Oooh, your cock gets even MORE MASSIVE with every POWERFUL jet of boygoo!"
    mc "Hang on Gwen, I've got some more cum lotion for your skin!"
    if persistent.cumsoundon:
        play sound "Sounds/cumming.mp3"
    hide gwenwallcumpussy01nocum
    hide gwenwallpussy05
    show gwenwallcumpussy02
    with fastdissolve
if gwenwallanalcum or gwenwallpussycum:
    show gwenwallpussycum05
    show gwenwallcumpussy01
    with fastdissolve
    mc "You asked for it! RHAAA!!!"
    gw "Oooh, your cock gets even MORE MASSIVE with every POWERFUL jet of boygoo!"
    mc "Hang on Gwen, I've got some more cum lotion for your skin!"
    if persistent.cumsoundon:
        play sound "Sounds/cumming.mp3"
    hide gwenwallcumpussy01
    hide gwenwallpussycum05
    show gwenwallcumpussy02
    with fastdissolve
gw "Oh my God, you've totally COVERED my back in your never-ending pellets."
$ gwenwallpussycum = True
if gwenwallanalcum:
    hide gwenwallcumpussy02
    show gwenwallcumanal03
    with fastdissolve    
    mc "Your holes have actually DRAINED me. temporarily of course. Get cleaned up and hop on the bed!"
    stop sound
    scene bedroom03b blurred
    show gwenbed01
    with dissolve
    gw "I don't even how you can still be hard after this MARATHON romp, but I'll gladly continue servicing your SEX PILLAR!"
    $ gwenwallpussycum = False
    $ gwenwallanalcum = False
    jump GwenFuckChoice
if gwenwallanalcum == False:
    hide gwenwallcumpussy02
    show gwenwallcumanal03
    with fastdissolve    
    mc "I ain't done with you, still need to cum inside that enticing rosebud of yours..."
    hide gwenwallcumanal03
    play music "Sounds/womansex01.mp3"
    jump GwenWallAnalCumSlow

label GwenWallAnalEnd:
mc "I'm about to flood your backdoor, Gwen!"
gw "YES! Give me a cum enema and then PLASTER the rest of my back!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
hide gwenwallpussycumfast
hide gwenwallanalcumslow
hide gwenwallpussycumslow
hide gwenwallanalcumfast
if gwenwallpussycum == False and gwenwallanalcum == False:
    show gwenwallanal05
    show gwenwallcumanal01nocum
    with fastdissolve
    mc "You asked for it! RHAAA!!!"
    gw "Oooh, your cock get even MORE MASSIVE with every POWERFUL jet of boygoo!"
    mc "Hang on Gwen, I've got some more cum lotion for your skin!"
    if persistent.cumsoundon:
        play sound "Sounds/cumming.mp3"
    hide gwenwallcumanal01nocum
    hide gwenwallanal05
    show gwenwallcumanal02
    with fastdissolve
if gwenwallpussycum or gwenwallanalcum:
    show gwenwallanalcum05
    show gwenwallcumanal01
    with fastdissolve
    mc "You asked for it! RHAAA!!!"
    gw "Oooh, your cock get even MORE MASSIVE with every POWERFUL jet of boygoo!"
    mc "Hang on Gwen, I've got some more cum lotion for your skin!"
    if persistent.cumsoundon:
        play sound "Sounds/cumming.mp3"
    hide gwenwallcumanal01
    hide gwenwallanalcum05
    show gwenwallcumanal02
    with fastdissolve
gw "Oh my God, you've totally COVERED my back in your never-ending pellets."
$ gwenwallanalcum = True
if gwenwallpussycum:
    hide gwenwallcumanal02
    show gwenwallcumanal03
    with fastdissolve    
    mc "Your holes have actually DRAINED me. temporarily of course. Get cleaned up and hop on the bed!"
    stop sound
    scene bedroom03b blurred
    show gwenbed01
    with dissolve
    gw "I don't even how you can still be hard after this MARATHON romp, but I'll gladly continue servicing your SEX PILLAR!"
    $ gwenwallpussycum = False
    $ gwenwallanalcum = False
    jump GwenFuckChoice
if gwenwallpussycum == False:
    hide gwenwallcumanal02
    show gwenwallcumanal03
    with fastdissolve    
    mc "I ain't done with you, still need to cum inside that enticing fuckhole of yours..."
    hide gwenwallcumanal03
    play music "Sounds/fucksound.mp3"
    jump GwenWallPussyCumSlow
    
label GwenSide:
scene bedroom17
show gwenprefuck04
with dissolve
gw "Ooh, you're so grabby [name]!"
mc "That's cos they are so many good things to grab on YOU!"
if trumpsternickname == False:
    gw "Maybe I should award you a Trumpster faction nickname then... \"[name] the Grabber\"!"
    window hide
    show mctrumpsternickname at posmission
    play sound "Sounds/skill.mp3"
    $ renpy.pause(2.0, hard=True)
    $ trumpsternickname = True
    mc "Alright! I have a nickname now! Woo-ooh!"
    hide mctrumpsternickname
    gw "Now come and REALLY grab me. By the pussy with your monsterdong!"    
scene bedroom16 blurred
show gwenprefuck05
with dissolve
mc "Your pussylips are just so moist... You really want this, don't you?"
gw "Yes I DO! Please, just stick it inside me, I NEED IT!"
scene bedroom16 blurred with dissolve
play music "Sounds/wank.mp3"
label GwenSideSlow:
hide gwensidefast
show gwensideslow
call screen gwensideslow01
screen gwensideslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenSideEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenSideFast") 

label GwenSideFast:
gw "GRAB me FASTER! I want to be GRABBED so BAD!"
hide gwensideslow
show gwensidefast
call screen gwensidefast01
screen gwensidefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenSideEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("GwenSideSlow") 

label GwenSideEnd:
mc "That's it, your pussy muscles are grabbing onto my shaft so hard, they're pulling the cum right out of my nuts..."
hide gwensideslow
hide gwensidefast
show gwensidecum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...And I'm cumming!"
gw "Yes, let me GRAB as much CUM from you as I can! And then, GRAB your cock and spew your load EVERYWHERE!"
hide gwensidecum01
show gwensidecum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
gw "That's it, fire those salvoes of sweet boycum all over me! AAAHH, I LOVE IT!"
mc "RHAAA! Here it comes, Gwen!"
hide gwensidecum02
show gwensidecum03
with fastdissolve
stop sound
gw "Look at the filthy mess you've made [name]. You're such a naughty boy. Grabbing girls like that and cumming all over them..."
mc "Well, I'm a celebrity now, so I guess I'm allowed to do it, right?"
gw "You're DIRTIER than a DIRTY old man. Now FUCK ME SOME MORE!"
scene bedroom03b blurred
show gwenbed01
with dissolve
gw "So, what are you going to GRAB next?"
jump GwenFuckChoice

label GwenImpregnation:
scene bedroom17
show gwenpreimpregnate01 with dissolve
gw "How.. Are we going to proceed? I've never done this in order to get pregnant."
mc "Don't worry, just lie down and let my cum-missile do all the work. And let me churn up a MONSTER LOAD for you by some sexy pre-impregnation fun."
scene bedroom16
show gwenpreimpregnate02 
with fastdissolve
play sound "Sounds/moaning02.mp3"
mc "...Like playing with those big funbags."
play sound "Sounds/lick.mp3"
mc "... And licking those tasty nipples... Mmmh..."
play sound "Sounds/moaning.mp3"
gw "Oooh! I like what you're doing... My body, I'm getting all tingly... Come and kiss me."
scene bedroom17 blurred
show gwenpreimpregnate03 
with fastdissolve
play sound "Sounds/kiss.mp3"
gw "Please... [name]... I want a baby! I know this is my duty now, you've convinced me."
scene bedroom12
show gwenpreimpregnate04 
with fastdissolve
mc "And now let the sperm flow and the impregnation begin!"
play music "Sounds/womansex02.mp3"
label GwenPregnantSlow:
hide gwenimpregnatefast
hide gwenimpregnatepovslow
hide gwenimpregnatepovfast
scene bedroom12
show gwenimpregnateslow
call screen gwenimpregnateslow01
screen gwenimpregnateslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenPregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenPregnantFast") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("GwenImpregnateSlow") 

label GwenImpregnateSlow:
hide gwenimpregnateslow
hide gwenimpregnatefast
hide gwenimpregnatepovfast
scene bedroom14 blurred
show gwenimpregnatepovslow
call screen gwenimpregnatepovslow01
screen gwenimpregnatepovslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenPregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenImpregnateFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("GwenPregnantSlow") 

label GwenPregnantFast:
hide gwenimpregnateslow
hide gwenimpregnatepovslow
hide gwenimpregnatepovfast
scene bedroom12
show gwenimpregnatefast
call screen gwenimpregnatefast01
screen gwenimpregnatefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenPregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("GwenPregnantSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("GwenImpregnateFast") 

label GwenImpregnateFast:
hide gwenimpregnateslow
hide gwenimpregnatefast
hide gwenimpregnatepovslow
scene bedroom14 blurred
show gwenimpregnatepovfast
call screen gwenimpregnatepovfast01
screen gwenimpregnatepovfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenPregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("GwenImpregnateSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("GwenPregnantFast") 
            
label GwenPregnantEnd:
stop music
scene bedroom12
show gwenimpregnatecum01
with dissolve
play music "Sounds/splooge02.mp3"
gw "Yes, pump your virile cream inside my womb, AAAH!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
show gwenimpregnatecum01 with flash
mc "I AM, RHAAA!"
$ preggw = True
scene bedroom12 blurred
show gwenimpregnatecum02 with dissolve
stop music
play sound "Sounds/splooge01.mp3"
gw "You're coming ssoo much, it looks like I'm pregnant with your ball-batter!"
mc "You'll get pregnant for real soon enough! AAHH, STILL COMING!"
show gwenimpregnatecum02 with fastflash
gw "You're coming ssoo much, it looks like I'm pregnant with your ball-batter!"
mc "You'll get pregnant for real soon enough! AAHH, STILL COMING!"
stop music
scene bedroom14
show gwenimpregnatecum03
with fastdissolve
play sound "Sounds/gasp.mp3"
gw "Oh my God, I'm so bloated with your spunk that I'm leaking cum like a faucet..."
mc "When a cum receptacle is full, it's either that or a massive explosion. So count yourself lucky. And pregnant."
scene bedroom12 blurred
show gwenimpregnatecum04
with fastdissolve
gw "You're a great sperm provider, but a lousy future father I can already tell."
mc "I told you my job was to impregante you. And that is what I did. Let's go to sleep and think of your bright future ahead as a mother."

label GwenEnd:
show screen calendar
show screen mcstats
scene gwenmcsleep with fade
$ loc = "bedroom"
play sound "Sounds/snoring.mp3"
pause 3
call NewDay
jump Bedroom