label ZaraBedroom:
hide screen calendar
hide screen mcstats
if pregza and pregzastart >= 3:
    scene bedroom01
    show zarapregnant02
    with fade
    za "Hi [name]! You wanted to see me?"
    mc "Yep. It's SEX time."
    hide zarapregnant02
    show zarapregnant02b
    with fastdissolve
    za "I know you're my harem master, but I'm too far into my pregnancy. My womb is off-limits until I give birth!"
    mc "But... You're still satisfied, right?"
    hide zarapregnant02b
    show zarapregnant02
    with fastdissolve
    za "Of course [name]! I'm the only harem girl who is ALWAYS satisfied anyway, remember?"
    mc "Ah yeah, I remember now."
    za "Bye [name]!"
    hide zarapregnant02 with dissolve
    $ weekfuckedzara = True    
    jump Bedroom    
$ alienfuck = True
$ zaraharem = True
scene bedroom02 with dissolve
show zarabedroom01
za "Yes Master?"
if zaradancedone:
    mc "Ah, there you are. I'm ready for a HOT night of sweet LOVE and PASSION!"
    hide zarabedroom01
    show zarabedroom02
    za "Oh well, that's great to hear..."
    mc "So let's get straigth to business shall we?"
    label HaremZaraChoice:
    menu:
        "Belly-dance for me again...":
            jump HaremZaraDance
        "Come with me on the bed...":
            jump HaremZaraFuck
        "Skip scene":
            jump ZaraFuckEnd
            
label ZaraDialogueMenu01:
menu:
    "How do you find the compound?":
        za "I have been a nomad all my life. It's hard adapting to life here. I don't know many people..."
        mc "You'll get used to it and you'll love it I'm sure. And you know me. I saved you from that shitty nomadic life, remember?"
        za "Yes... Thank you Master."
        mc "And don't call me that. You're a free woman. You just happen to be a sex slave in my harem, that's all."
        jump ZaraDialogueMenu01
    "So, Zara, you seem reluctant to have sex with me. That's no good.":
        za "I'm sorry Master. I am... not used to this."
        mc "All you have to do is lie down on my bed and open up your legs from time to time. How hard can that be?"
        za "Yes Master. I will do my best to please you. I can belly-dance for you maybe?"
        mc "That sounds nice. And stop calling me Master. You're a free woman. You just happen to be a sex slave in my harem, that's all."
        jump ZaraDance
    "What skills do you have?":
        hide zarabedroom01
        show zarabedroom02
        za "I can dance... for men... Belly-dance."
        mc "Nice... How about you dance for me then?"
        hide zarabedroom02
        show zarabedroom01
        za "Yes... Master."
        mc "And don't call me that. You're a free woman. You just happen to be a sex slave in my harem, that's all."
        jump ZaraDance

label ZaraDance:
play music "Sounds/bellydance.mp3"
scene bedroom02 blurred
show zaradance01
call screen zaradance01
screen zaradance01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ZaraDance02")

label ZaraDance02:
if zaradancedone:
    mc "OK, now for the nude belly-dancing at which you excel..."
    za "Of course [name]!"
if zaradancedone == False:
    mc "That's real nice but... How about you get naked and continue this dance for me...?"
    za "I've never done nude belly-dancing... But I'll try."
hide zaradance01
show zaradance02
call screen zaradance02
screen zaradance02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ZaraDanceEnd")

label ZaraDanceEnd:
mc "You're a natural at it Zara! WOW!"
za "Would you like me to turn around?"
mc "Oh YEAH!"

hide zaradance02
show zarabutt
call screen zarabutt01
screen zarabutt01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ZaraButtEnd")

label ZaraButtEnd:
stop music
hide zarabutt
$ zaradancedone = True
show zarabedroom03
mc "That was... mesmerizing. Your amazing seductions skills could prove very useful on certain missions."
call LustPlusZara
mc "Now you got me hard and we've got to do something about that erection, right?"
za "Of course [name]. What would you like me to do to please you?"
mc "Why don't you come closer to me and rub that ass over my rod?"
scene mczarabedroom02 with dissolve
za "It's ssoo BIG! I've never seen such a beautiful specimen. Even on camels."
scene mczarabedroom01 with fastdissolve
mc "Yeah! You're getting me HARD AS A ROCK!"
scene mczarabedroom03 with fastdissolve
mc "I can't wait any longer, I'm gonna make sweet LOVE to you Zara!"
za "Oooh, [name], you're so strong! Take me to your bed and let's have some REAL fun!"
scene bedroom03 with dissolve
show zarabed01
mc "You look so cute... and so naughty at the same time!"
hide zarabed01
show zarabed02
mc "Yeah, play with those big titties... God, you're making me so HARD!"
hide zarabed02
show zarabed03
za "So, what would you like to do?"

label ZaraFuckChoice:
stop music
menu:
    "Let's dilate that pussy of yours with some fisting action!":
        jump ZaraFisting
    "Give me a nice, slow handjob...":
        jump ZaraHandjob    
    "Get on top of me and ride me like a... err... camel.":
        jump ZaraBounce
    "Impale yourself on my love saber!":
        jump ZaraTop
    "It is time for me to affirm my breeding rights." if pregzaready >= 3 and impregnatedsomeone == False and babyzara == False:
        $ impregnatedsomeone = True
        za "You... want to breed me? And put a baby in my belly?"
        mc "Yep. So get ready Zara, I'm gonna need to cum a LOT!"
        jump ZaraImpregnation
    "I'm done, let's go to sleep.":
        jump ZaraFuckEnd
 
label ZaraFisting:
scene bedroom05 with dissolve
show prezarafist
mc "First a little lick to get your juices going...."
mc "And then..."
scene bedroom07 with dissolve
play music "Sounds/fucksound.mp3"
label ZaraFistingSlow:
hide zarafistfast
show zarafistslow
call screen zarafistingslow
screen zarafistingslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ZaraFistingEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ZaraFistingFast") 

label ZaraFistingFast:
hide zarafistslow
show zarafistfast
za "Yes, you're stretching me so wide with your fist!"
call screen zarafistingfast
screen zarafistingfast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ZaraFistingEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ZaraFistingSlow") 

label ZaraFistingEnd:
if missionge and stonepiece04 == False:
    mc "That's strange... I feel something hard at the back of your womb..."
    scene bedroom07 blurred with fastdissolve
    stop music
    show zarafiststone
    mc "What the hell is that???"
    za "I... don't know... The desert is very rocky and windy... I must have..."
    mc "Hang on a minute, it's a piece of the Stone Artefact!"
    $ stonepieces -= 1
    window hide
    show achievementgenie at posmission
    $ renpy.pause(0.5, hard=True)
    show text "{font=Gui/Boogaloo-Regular.ttf}{color=#ff0000}{size=30}[stonepieces]{/font}" at StonePosition
    $ renpy.pause(2.0, hard=True)
    hide achievementgenie
    hide text
    $ stonepiece04 = True    
    za "Oh well, I'm so happy for you... Please don't tell anyone where you found it [name]..."
    mc "Right. Let's move on..."
    jump ZaraFuckChoice
scene bedroom03b blurred
stop music
show zarafistend
za "You've totally stretched my hole... I can take anything in there now..."
mc "Let's test this theory..."
jump ZaraFuckChoice

label ZaraHandjob:
scene bedroom04 with dissolve
show zarabed04
mc "Get on your knees while you jack my crank..."
za "Of course Mast... I mean [name]."
scene bedroom06 blurred with dissolve
play music "Sounds/zarahandjob.mp3"
call screen zarahandjob01
screen zarahandjob01:
    modal True
    add zarahandjob
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ZaraHandjobCum")
        
label ZaraHandjobCum:
stop music
hide zarahandjob
show zarahandjobcum01
mc "Damn, you're making me CUUUMMM!"
hide zarahandjobcum01
show zarahandjobcum02
za "Ooh, [name], that is such a HUGE amount for your little sex slave! *wink*"
mc "You bring the best out of me, and the CUM out of my CUMHOLE! RHAAAA!"
hide zarahandjobcum02
show zarahandjobcum03
za "Look at my covered face, I'm going to need to slurp up ALL that sweet cream for the....NEXT part."
mc "Damn right, I'm still hard and ready!"
jump ZaraFuckChoice

label ZaraBounce:
scene bedroom09 with dissolve
show zarabed07
za "I can feel that powerful log between my asscheeks...."
mc "You're going to need to lift yourself up so I can bury it deep inside you while you ride me Zara!"
scene bedroom03 blurred
show zarabed05
za "It's so thick, it's stretching me wide open!"
mc "Let's stretch it some more then, bounce up and down on it Zara!"
scene bedroom08 blurred with dissolve

label ZaraBounceSlow:
play music "Sounds/zarabounce.mp3"
hide zarabouncefast
show zarabounceslow
call screen zarabounceslow
screen zarabounceslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ZaraBounceEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ZaraBounceFast") 

label ZaraBounceFast:
hide zarabounceslow
show zarabouncefast
za "My tits are bouncing all over the place, this is sssooo good!"
call screen zarabouncefast
screen zarabouncefast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ZaraBounceEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ZaraBounceSlow") 

label ZaraBounceEnd:
mc "Fuck, your hot pussy is making me CUUUMMMM!"
za "Cum inside of me, I want to feel every spurt swelling my womb!"
stop music
scene bedroom08 blurred
show zaraswell01
mc "Damn it, your pussy muscles are milking meeeee!"
za "Make my belly grow with your MASSIVE THICK LOAD!"
hide zaraswell01
show zaraswell02 with fastdissolve
za "It's pumping NON-STOP inside of me!"
mc "Damn right it is! I'm cumming like a STALLION IN HEAT!"
hide zaraswell02
show zaraswell03 with fastdissolve
za "I can feel my stomach BULGING with your cum! AAAHH!"
mc "I'm not done, I'm gonna PUMP THAT PUSSY FULL!"
hide zaraswell03
show zaraswell04 with fastdissolve
za "I can't take any more cum, I'm SWELLING like I'm pregnant!"
mc "Almost done... RHAAA!"
hide zaraswell04
show zaraswell05 with fastdissolve
za "Oh [name], I can't believe how MUCH you came! Your balls must be working OVERTIME to produce that much sweet virile seed."
mc "Yep, and I've got plenty more thick ball-batter stored in them for you!"
hide zaraswell05
show zaraswell06 with fastdissolve
za "And it's so tasty too! I can't wait to clean this cock..."
mc "Take your time, and don't forget to slurp up all that cum leaking out out your bloated pussy..."
jump ZaraFuckChoice
   
label ZaraTop:
scene bedroom03
show prezararide
za "Ooh, it looks sssoo BIG against my tiny body. The cocktip goes all the way to my chest!"
mc "And yet, it will somehow fit..."
label ZaraTopSlow:
scene bedroom03 blurred
play music "Sounds/fucksound.mp3"
show zararideslow
call screen zaratopslow
screen zaratopslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ZaraTopEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ZaraTopFast") 

label ZaraTopFast:
scene bedroom03 blurred
show zararidefast
za "Oh God, you're pounding me so HARD [name]!"
call screen zaratopfast
screen zaratopfast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ZaraTopEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ZaraTopSlow")

label ZaraTopEnd:
za "Cover my chest in your virile seed!"
stop music
scene bedroom03
show zararidecum01
mc "Yeah, take that ball-batter Zara!"
za "I LOVE IT! I can feel it dripping all over my tits!"
scene bedroom03b blurred
show zararidecum02
za "Dear Prophet! My face is dripping with warm spunk... I can barely see a thing..."
mc "Well, you'd better get cleaned up then so we can move on..."
jump ZaraFuckChoice

label HaremZaraDance:
play music "Sounds/bellydance.mp3"
scene bedroom02 blurred
show zaradance01
call screen zaradance03
screen zaradance03:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HaremZaraDance02")

label HaremZaraDance02:
mc "OK, now for the nude belly-dancing at which you excel..."
za "Of course [name]!"
hide zaradance01
show zaradance02
call screen zaradance04
screen zaradance04:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HaremZaraDanceEnd")

label HaremZaraDanceEnd:
scene bedroom02 with dissolve
show zarabedroom03
jump HaremZaraChoice

label HaremZaraFuck:
scene mczarabedroom02 with dissolve
za "I never tire of seeing this MONSTERCOCK up close and personal!"
scene mczarabedroom01 with fastdissolve
mc "ANd I never tire of you rubbing your sumptuous ass all over my shaft!"
scene mczarabedroom03 with fastdissolve
mc "I can't wait any longer, I'm gonna make sweet LOVE to you Zara!"
za "Oooh, [name], you're so strong! Take me to your bed and let's have some REAL fun!"
scene bedroom03 with dissolve
show zarabed01
za "I'm ready for you... Are you ready for me?"
hide zarabed01
show zarabed02
mc "Yeah, play with those big titties... God, you're making me so HARD!"
hide zarabed02
show zarabed03
za "So... I'm here, all wet and awaiting... that MASSIVE WEAPON of yours!"
jump ZaraFuckChoice

label ZaraImpregnation:
za "Could you at least try and be romantic for a change, I'd like my baby to be conceived in LOVE."
scene bedroom17
show zaraprepreg01
with dissolve
mc "ALright, let me kiss you then..."
play sound "Sounds/kiss.mp3"
mc "Do you want a boy or a girl?"
scene bedroom14 blurred
show zaraprepreg02
with dissolve
za "I want a girl. So she can grow up and become a sex slave in your harem, just like me!"
mc "Interesting thought... Won't happen in this game obviously, the timeframe is not long enough."
za "But we can still imagine it... A mother-daughter threesome with you..."
mc "That's making me horny, I need to fuck those big tits of yours!"

scene bedroom34 blurred
play channel1 "Sounds/wank.mp3"
play channel2 "Sounds/boymoan02.mp3"
label ZaraPrePregSlow:
hide zaratitsfast
show zaratitsslow
call screen zaratitsslow01
screen zaratitsslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nextidle.png"
        action Jump ("ZaraPrePregEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ZaraPrePregFast") 

label ZaraPrePregFast:
za "Your cock is REALLY rock-hard! Keep fucking my breasts faster, please [name]!"
hide zaratitsslow
show zaratitsfast
call screen zaratitsfast01
screen zaratitsfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nextidle.png"
        action Jump ("ZaraPrePregEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ZaraPrePregSlow") 
        
label ZaraPrePregEnd:
scene bedroom34 blurred
show zaraprepreg03
with dissolve
stop channel1
stop channel2
play sound "Sounds/boymoan.mp3"
za "Mmmh, I think it's as STIFF as it will get! This titfuck really made you HORNY, didn't it?"
mc "Damn well it did! And now I'm ready to BREED you, my sexy harem girl!"

scene bedroom09
show zarapreg00
with dissolve
mc "Are you ready Zara?"
za "I am, oh yes I am, BREED ME Master!"
play music "Sounds/womansex01.mp3"
hide zarapreg00
label ZaraPregSlow:
hide zarapregfast
show zarapregslow
call screen zarapregslow01
screen zarapregslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("ZaraPregEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ZaraPregFast") 

label ZaraPregFast:
za "That's it, keep going, FASTER MASTER!"
hide zarapregslow
show zarapregfast
call screen zarapregfast01
screen zarapregfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("ZaraPregEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ZaraPregSlow") 

label ZaraPregEnd:
mc "I'm going to fill up your womb with my seed, Zara!"
za "YES, GIVE ME A BABY!"
stop music
scene bedroom09 blurred
show zaraimpregnatecum01
with fastdissolve
play music "Sounds/splooge02.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAAH! That's it, the baby-batter is coming!"
show zaraimpregnatecum01 with flash
za "YES, give me all your cum [name], I want a baby, I NEED a baby from you!"
$ pregza = True
stop music
scene bedroom36 blurred
show zaraimpregnatecum02
with dissolve
play sound "Sounds/splooge01.mp3"
za "I am so happy for us and our future baby!"
mc "Err, I'm so happy for YOU for taking care of it in about eight weeks!"
scene bedroom10 blurred
show zaraimpregnatecum03
with dissolve
stop sound
za "I really hope it worked... It would be such a disappointment having to do that again."
mc "I think it did. I'm pretty sure it did. You're leaking great big globs of my spunk all over the place."
stop music
za "Then let's go to sleep and find out..."   

label ZaraFuckEnd:
show screen calendar
show screen mcstats
scene zaramcsleep
$ loc = "bedroom"
play sound "Sounds/snoring.mp3"
pause 3
call NewDay
jump Bedroom
