label PennyFuck01:
hide screen calendar
hide screen mcstats
scene bedroom01
show pennynight01
with fade
menu:
    "Run scene":
        pass
    "Skip scene":
        $ alienfuck = True
        $ weekfuckedpenny = True
        jump PennyEnd
pe "Well, I was just about to go to bed and jill myself to sleep."
mc "And now you don't need to anymore, you've got the REAL stuff to play with!"
pe "Lucky me... And how shall the evening proceed?"
menu:
    "I like that teddy of yours, keep it on and let's get moving.":
        hide pennynight01
        show pennynight02
        with fastdissolve
        pe "So eager! Well, I'm eager too so I'll show you what I was about to do in my bed... Follow me to the sofa."
        jump PennyLingerie
    "Do you have some kind of kinky costume?" if pennycostumeasked == False:
        $ pennycostumeasked = True
        hide pennynight01
        show pennynight03
        with fastdissolve
        pe "Well yes, as a matter of fact... A HORNY BUNNY costume! I'll go and change into it. Don't move, and get HARD in the meantime."
        window hide
        hide pennynight03 with dissolve
        mc "*I am, I am, just imagining it...*"
        jump PennyCostume
    "Put on your bunny costume, I'm in the mood to FUCK LIKE RABBITS!" if pennycostumeasked:
        hide pennynight01
        show pennynight03
        with fastdissolve        
        pe "I see. Good thing I am too then! Don't move, I'll change into it. And get HARD in the meantime."
        window hide
        hide pennynight03 with dissolve
        mc "*I am, I am, just imagining it...*"
        jump PennyCostume

label PennyCostume:
show pennycosplay01 with moveinright
pe "There I am! Ready to FUCK LIKE A HORNY BUNNY!"
mc "Well, that makes two of us!"
hide pennycosplay01
show pennycosplay02
with fastdissolve
pe "Is that so? As the female bunny, I should first entice you to fuck me, shouldn't I?"
mc "That is indeed your duty as I fight off other beta-males by repeatedly knocking them unconscious with my hard dong!"
pe "Then come closer to the den..."
play music "Sounds/stripmusic.mp3"
scene bedroom03 blurred
show pennywiggle
call screen pennywiggle
screen pennywiggle:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyWiggleEnd")
 
label PennyWiggleEnd:
pe "Are you done beating your rivals?"
mc "Of course!"
stop music
scene bedroom13 blurred
show pennycosplay03
with fastdissolve
pe "They didn't stand a chance against you and your superior ALPHA-COCK!"
scene bedroom50 blurred
show pennycosplay03b
with fastdissolve
mc "Damn right!"
scene bedroom13 blurred
show pennycosplay04
with fastdissolve
pe "Now that you've beaten them all up, time for me to prepare myself for copulation...."
mc "That's one scientific way to put it."
hide pennycosplay04
show pennycosplay05
with fastdissolve
pe "I am ready to be serviced by your harem master cock, [name]!"
mc "That's good bunny. Let me check the readiness of your bunny pussy..."
scene bedroom46
show pennymccosplay01
with fastdissolve
pe "Does it look ready?"
scene bedroom50 blurred
show pennymccosplay04
with fastdissolve
mc "It sure does, nice and wet and leaking pussy juices..."
scene bedroom13 blurred
show pennymccosplay02
with fastdissolve
play sound "Sounds/moaning.mp3"
pe "Fuck, your balls are so ENORMOUS [name]!"
mc "All the better to fill you up with lots of alpha-semen!"
hide pennymccosplay02
show pennymccosplay03
with fastdissolve
pe "Show me!"
mc "Alright, let's proceed on the bed where it's more comfortable..."
pe "And I'll take my mask off cos I want to see EVERYTHING!"
scene bedroom03b
show pennybed01
with dissolve
pe "Now that's better. Let's fuck like rabbits then."
jump PennyFuckChoice

label PennyLingerie:
play music "v07/datemusic.mp3"
scene pennybedroom01 with dissolve
pe "Oh wow, I see you're already starting to undress... That cock of yours must be getting hard pretty FAST then!"
mc "You have no idea, it's about to tear a hole through my pants!"
scene pennybedroom02 with dissolve
pe "Let me help you... By making it get hard even FASTER!"
mc "Oh God, I... Quick, I need to..."
scene pennybedroom03 with dissolve
pe "There, much better. Free at last. Just like that hardening fucktool of yours."
mc "Phew, in the nick of time!"
scene pennybedroom04 with dissolve
pe "I feel so liberated... The only thing left to take off are my tiny panties..."
mc "Yes, yes, take them off! Or I'm going to explode all over the sofa!"
scene pennybedroom05 with dissolve
play sound "Sounds/moaning02.mp3"
pe "Now we wouldn't that, would we? Let me get my pussy nice and wet for your giant young boycock, [name]..."
mc "I just need to stick my fuckpole inside it. Like NOW!"
scene pennybedroom06 with dissolve
play sound "Sounds/boymoan.mp3"
pe "Wow, so EAGER! Go on, pump away inside of me, STUD!"
stop music
play music "Sounds/scarlettpound.mp3"
label PennyBedroomSlow:
hide pennybedroomfast
show pennybedroomslow
call screen pennybedroomfuckslow01
screen pennybedroomfuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyBedroomEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PennyBedroomFast") 

label PennyBedroomFast:
mc "I'm just so horny, I'm gonna need to fuck you faster!"
hide pennybedroomslow
show pennybedroomfast
call screen pennybedroomfuckfast01
screen pennybedroomfuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyBedroomEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PennyBedroomSlow") 

label PennyBedroomEnd:
play sound "Sounds/moaning03.ogg"
pe "You're making me come so much on your MONSTER fucktool! AAAH!"
stop music
scene pennybedroomfuckcum01 with dissolve
mc "Same here, your pussy is making me COME!"
play sound "Sounds/cumming.mp3"
pe "Go on, keep blasting that seed inside me, make me COME AGAIN! AAAH!"
scene pennybedroomfuckcum01 with fastflash
mc "I need to pull out, your pussy is DRAINING ME!"
scene pennybedroomfuckcum02 with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH!"
pe "What are you doing, I'm getting CAKED in your red-hot spunk!"
scene pennybedroomfuckcum03 with fastdissolve
mc "Oops, sorry, will try to aim better next time..."
pe "It's alright, I was just surprised, but I actually LOVED getting hosed down by your cum-cannon..."
mc "Good, cos I've got plenty more loads in store for you!"
pe "Really? Wow, what a STALLION you are, [name]! Let me get cleaned up and I'll join you on the bed for MORE THEN!"
scene bedroom03b
show pennybed01
with dissolve
pe "Alright, so what do you have planned for us to continue our all-night fuck session then?"
jump PennyFuckChoice

label PennyFuckChoice:
$ alienfuck = True
$ weekfuckedpenny = True
stop music
menu:
    "I have a bestiality fetish. Let's go doggy!":
        pe "Woof, woof!"
        jump PennyDoggy
    "I want to be rough on your pussy...":
        pe "As rough as a Road Warrior can be?"
        mc "You'll see..."
        jump PennyLift 
    "There's an unexplored hole of yours that needs to be cleared.":
        pe "Go ahead scout, explore away!"
        jump PennyAnal
    "You look like a pretty flexible woman.":
        pe "Oooh, you're in for ACROBATIC sex then, huh?"
        mc "Err, yeah, that's right."
        pe "Then let me show you how acrobatic I can be!"
        jump PennyAcrobatic
    "I'm done, let's go to sleep.":
        jump PennyEnd

label PennyDoggy:
scene bedroom18
show pennypredoggy01
with dissolve
mc "That's right, offer me your sweet behind... I'll sniff it first, like a good dog would do..."
scene bedroom48
show pennypredoggy02
with dissolve
pe "Is it to your liking? Why don't you give it a good lick? Like a dog would..."
mc "Mmh, yeah, it does look tasty."
scene bedroom34 blurred
show pennypredoggy03
with dissolve
play music "Sounds/moaning03.ogg"
play sound "Sounds/lick.mp3"
pe "Oooh, that's nice... You're getting my pussy all wet and READY FOR YOUR HUGE DONG!"

stop music
play music "Sounds/barbarasex.mp3"
label PennyDoggySlow:
hide pennydoggypovslow
hide pennydoggypovfast
hide pennydoggyfast
scene bedroom30
show pennydoggyslow
call screen pennydoggyslow01
screen pennydoggyslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyDoggyEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PennyDoggyFast") 
    imagebutton:
        focus_mask True
        idle "Icons/POVview.png"
        hover "Icons/POVview.png"
        action Jump ("PennyDoggyPOVSlow") 

label PennyDoggyFast:
mc "God, this pussy is so amazing, I'm going to need to FUCK IT FASTER!"
hide pennydoggypovslow
hide pennydoggypovfast
hide pennydoggyslow
scene bedroom30
show pennydoggyfast
call screen pennydoggyfast01
screen pennydoggyfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyDoggyEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PennyDoggySlow") 
    imagebutton:
        focus_mask True
        idle "Icons/POVview.png"
        hover "Icons/POVview.png"
        action Jump ("PennyDoggyPOVFast") 

label PennyDoggyPOVSlow:
hide pennydoggyfast
hide pennydoggyslow
hide pennydoggyfast
scene bedroom14
show pennydoggypovslow
call screen pennydoggypovslow01
screen pennydoggypovslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyDoggyEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PennyDoggyPOVFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("PennyDoggySlow") 

label PennyDoggyPOVFast:
mc "God, this pussy is so amazing, I'm going to need to FUCK IT FASTER!"
hide pennydoggyslow
hide pennydoggyslow
hide pennydoggyfast
scene bedroom14
show pennydoggypovfast
call screen pennydoggypovfast01
screen pennydoggypovfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyDoggyEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PennyDoggyPOVSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("PennyDoggyFast") 
        
label PennyDoggyEnd:
pe "You need to mark your territory by CUMMING ALL OVER YOUR BITCH IN HEAT!"
mc "ALright, I was indeed just about to..."
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
hide pennydoggyslow
hide pennydoggyfast
hide pennydoggypovslow
hide pennydoggypovfast
scene bedroom14
show pennydoggycum01
with fastdissolve
mc "...CUM! RHAAA!"
show pennydoggycum01 with fastflash
pe "YES, keep going [name], plaster me in your young spunk! AAAH!"
scene bedroom30 blurred
show pennydoggycum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Bend over, I'm gonna cover your back with my unending streams of boygoo! AAH!"
stop sound
scene bedroom14
show pennydoggycum03
with fastdissolve
pe "Your sperm is so THICK and HEAVY on my back!"
mc "I have some pretty heavy balls, that's why."
pe "Now I hope you can get ROCK-HARD AGAIN, cos I want you to fuck me some more!"
mc "No worries, get cleaned up and I'll be with you in no time with a raging hardon."
scene bedroom03b
show pennybed01
with dissolve
pe "All cleaned up. Waiting for some more HOT FUN."
jump PennyFuckChoice
    
label PennyLift:
scene bedroom13
show pennyprestand01
with dissolve
mc "So... You want it rough, hey?"
pe "Y...Yes. Please fuck the SHIT OUT OF ME!"
mc "You asked for it..."
scene bedroom13 blurred
play music "Sounds/barbarasex.mp3"
label PennyLiftSlow:
hide pennystandfast
show pennystandslow
call screen pennystandslow01
screen pennystandslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyLiftEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PennyLiftFast") 

label PennyLiftFast:
mc "Prepare to have my fat cock shoved up your quivering pussy even FASTER!"
hide pennystandslow
show pennystandfast
call screen pennystandfast01
screen pennystandfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyLiftEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PennyLiftSlow") 

label PennyLiftEnd:
pe "You're POUNDING me so hard! Cum inside me, FLOOD MY WOMB!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
hide pennystandslow
hide pennystandfast
show pennystandcum01
with fastdissolve
mc "Ask and you shall receive! BIG TIME, RHAAA!"
show pennystandcum01 with fastflash
pe "Sssooo much cum! Gimme MORE!"
hide pennystandcum01
show pennystandcum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Bend over, I'm gonna cover your back with my unending streams of boygoo! AAH!"
stop sound
hide pennystandcum02
show pennystandcum03
with fastdissolve
pe "You fucked me so well, now kiss me!"
play sound "Sounds/kiss.mp3"
mc "Who knew harem sex could be so romantic?"
pe "Shut up, silly boy. And since your cock is still ROCK-HARD, fuck me some more!"
mc "Damn right I'm still rock-hard and I'll give you more!"
hide pennystandcum03
show pennyprestandb01
with fastdissolve
mc "First, I'll lift you up arm in my muscular arms..."
pe "Ooh, you're so godamn STRONG!"
hide pennyprestandb01
show pennystandb00
with fastdissolve
mc "And then I'll IMPALE you on my mighty shaft!"
if mcwarrior == 5 and warriornickname == False:
    pe "Then, you certainly deserve a nickname, a ROAD WARRIORS NICKNAME! \"[name] the Impaler\" sounds about right!"
    window hide
    show mcwarriornickname at posmission
    play sound "Sounds/skill.mp3"
    $ renpy.pause(2.0, hard=True)
    $ warriornickname = True
    mc "Alright! I have a nickname now! Woo-ooh!"
    hide mcwarriornickname

hide pennystandb00
play music "Sounds/barbarasex.mp3"
label PennyStandSlow:
hide pennystandbfast
show pennystandbslow
call screen pennystandbslow01
screen pennystandbslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyStandEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PennyStandFast") 

label PennyStandFast:
pe "Fuck me even faster with your cum-covered DONKEY-DICK, please!"
hide pennystandbslow
show pennystandbfast
call screen pennystandbfast01
screen pennystandbfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyStandEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PennyStandSlow") 

label PennyStandEnd:
pe "I want ANOTHER dose of plentiful boyspunk! Can you give it to me [name]?"
mc "You bet I can! Here it comes..."
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
hide pennystandbslow
hide pennystandbfast
show pennystandbcum01
with fastdissolve
mc "RIGHT NOW, RHAAA!"
scene bedroom41 blurred
show pennystandbcum02
with dissolve
pe "Oh fuck, you're pummelling my womb with your pellets of cum!"
show pennystandbcum02 with fastflash
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "That's right, and I've got more for you Penny!"
stop sound
scene bedroom13 blurred
show pennystandbcum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
pe "Damn boy, you truly are a CUM MACHINE!"
mc "Cos your body is so cum-inducing! AAAH!"
pe "You're going to PLASTER your bedroom with your spunk!"
hide pennystandbcum03
show pennystandbcum04
with fastdissolve
stop sound
mc "It's fine, the cleaning lady we never see will come round after our fuck session, don't worry..."
pe "That's nice to know... Are you still HARD for more?"
mc "Yep! Get on the bed and wait for my instructions..."
scene bedroom03b
show pennybed01
with dissolve
pe "So, what do you have in store for us, big boy?"
jump PennyFuckChoice
    
label PennyAnal:
scene bedroom20
show pennypreanal01
with dissolve
pe "Let me prep my rosebud for your MASSIVE TOOL..."
mc "Yeah, you do that Penny, while I jack off and get ROCK-HARD watching you."
scene bedroom17
show pennypreanal02
with dissolve
pe "Just a second, let me stick my finger and get some slime in there..."
mc "Hurry up please, I'm raring to go!"
pe "Ok. There, I'm ready. ANAL-IZE ME NOW!"
scene bedroom12 blurred with dissolve
play music "Sounds/fucksound.mp3"
label PennyAnalSlow:
hide pennyanalfast
hide pennyanalpovfast
hide pennyanalpovslow
scene bedroom18
show pennyanalslow
call screen pennyanalslow01
screen pennyanalslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PennyAnalFast") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("PennyAnalPOVSlow")

label PennyAnalFast:
hide pennyanalslow
hide pennyanalpovfast
hide pennyanalpovslow
scene bedroom18
show pennyanalfast
call screen pennyanalfast01
screen pennyanalfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PennyAnalSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("PennyAnalPOVFast") 

label PennyAnalPOVSlow:
hide pennyanalslow
hide pennyanalfast
hide pennyanalpovfast
scene bedroom14 blurred
show pennyanalpovslow
call screen pennyanalpovslow01
screen pennyanalpovslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PennyAnalPOVFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("PennyAnalSlow") 

label PennyAnalPOVFast:
hide pennyanalslow
hide pennyanalfast
hide pennyanalpovslow
scene bedroom14 blurred
show pennyanalpovfast
call screen pennyanalpovfast01
screen pennyanalpovfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("PennyAnalPOVSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("PennyAnalFast") 

label PennyAnalEnd:
pe "Don't hold it in, just BLAST YOUR SPERM IN MY BACKSIDE!"
mc "If you ask so eargerly, then yes, I'll do it..."
scene bedroom49 blurred
show pennyanalcum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...NOW! RHAAAA!"
pe "AAAH, I'm CUMMING TOO! Feeling those red-hot pellets of young spunk EXPLODING inside me is just so incredible!!!"
show pennyanalcum01 with fastflash
mc "Oh God, I'm  cumming SSOOO MUCH, it's backing up! Need... To... PULL OUT!"
scene bedroom26 blurred
show pennyanalcum02
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Now I can let it fly, RHAAA!"
show pennyanalcum02 with fastflash
pe "You're drenching your coversheets with your own filthy sperm, this is so hot!"
scene bedroom52
show pennyanalcum03
with dissolve
stop sound
pe "Damn, my bowels are filled to the brim with your cream. I'm farting spunk."
mc "Eeew, too much information, TMI! Get cleaned up and stop farting. We have more positions to explore."
scene bedroom03b
show pennybed01
with dissolve
pe "Done! So which position shall we explore together this time?"
jump PennyFuckChoice

label PennyAcrobatic:
scene bedroom41 blurred
show pennypreacrob01
with dissolve
pe "Let's see... A huge hard pole sticking straight up in the air..."
mc "What are you going to do about it Penny?"
pe "Move your knees up a bit, I'll show you..."
scene bedroom18
show pennypreacrob02
with dissolve
pe "There, that's a good position."
mc "For what?"
pe "For THIS."
scene bedroom18 blurred
play music "Sounds/womansex02.mp3"
label PennyAcrobaticSlow:
hide pennyacrobaticfast
hide pennyacrobaticpovslow
hide pennyacrobaticpovfast
scene bedroom18 blurred
show pennyacrobaticslow
call screen pennyacrobaticslow01
screen pennyacrobaticslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyAcrobaticEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PennyAcrobaticFast") 
    imagebutton:
        focus_mask True
        idle "Icons/POVview.png"
        hover "Icons/POVview.png"
        action Jump ("PennyAcrobaticPOVSlow") 

label PennyAcrobaticPOVSlow:
hide pennyacrobaticslow
hide pennyacrobaticfast
hide pennyacrobaticpovfast
scene bedroom08 blurred
show pennyacrobaticpovslow
call screen pennyacrobaticpovslow01
screen pennyacrobaticpovslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyAcrobaticEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PennyAcrobaticPOVFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("PennyAcrobaticSlow") 

label PennyAcrobaticFast:
hide pennyacrobaticslow
hide pennyacrobaticpovslow
hide pennyacrobaticpovfast
scene bedroom18 blurred
show pennyacrobaticfast
call screen pennyacrobaticfast01
screen pennyacrobaticfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyAcrobaticEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PennyAcrobaticSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/POVview.png"
        hover "Icons/POVview.png"
        action Jump ("PennyAcrobaticPOVFast") 

label PennyAcrobaticPOVFast:
hide pennyacrobaticslow
hide pennyacrobaticfast
hide pennyacrobaticpovslow
scene bedroom08 blurred
show pennyacrobaticpovfast
call screen pennyacrobaticpovfast01
screen pennyacrobaticpovfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyAcrobaticEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("PennyAcrobaticPOVSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("PennyAcrobaticFast") 
            
label PennyAcrobaticEnd:
mc "Penny, I'm warning you, I'm about to BLOW BIG TIME!"
pe "DO IT, EMPTY YOUR GIANT SEEDMAKERS!"
stop music
scene bedroom08 blurred
show pennyacrocum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
pe "YES!!!! Cum in me, give me your sweet young SEED! AAAH!"
play music "Sounds/splooge01.mp3"
show pennyacrocum01 with fastflash
mc "I can't stop... AAAH, I can't..."
hide pennyacrocum01
show pennyacrocum02
with fastdissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...STOP! RHAAA!"
pe "Oh my God, your blasts are so POWERFUL, I'm being thrown up in the air like a ragdoll!"
scene bedroom18
show pennyacrocum03
mc "There's more for you Penny, AAAH, take ALL my cum!"
pe "I will gladly! KEEP GOING, COVER ME IN YOUR THICK SCUM!"
show pennyacrocum03 with fastflash
pe "Sssoo, ssoo MUCH OF IT! I love it!"
scene bedroom03b blurred
show pennyacrocum04
stop sound
pe "Look at the CRAZY mess you made [name]! It's not normal than a boy can cum THAT MUCH, you know?"
mc "Well, I've got big balls, that's why. Speaking of which, they're not empty yet."
pe "No way! You want more?"
mc "Yep."
jump PennyFuckChoice

label PennyEnd:
show screen calendar
show screen mcstats
scene pennymcsleep with fade
$ loc = "bedroom"
play sound "Sounds/snoring.mp3"
pause 3
call NewDay
jump Bedroom