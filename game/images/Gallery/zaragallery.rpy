label ZaraGallery:
call screen galleryzara
screen galleryzara:
    add "Gallery/zaragallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("galleryzara"), Jump ("MainGallery")]

    if renpy.seen_image("poolzara01"):
        imagebutton:
            focus_mask True
            idle "Gallery/zaragallery01.png" xpos 621 ypos 100
            hover "Gallery/zaragallery01.png"
            action Jump ("ZaraGallery01")

    if renpy.seen_image("poolzara01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("ZaraGallery")

    if renpy.seen_image("zaradance01"):
        imagebutton:
            focus_mask True
            idle "Gallery/zaragallery02.png" xpos 1050 ypos 100
            hover "Gallery/zaragallery02.png"
            action Jump ("ZaraGallery02")

    if renpy.seen_image("zaradance01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("ZaraGallery")

    if renpy.seen_image("mczarabedroom02"):
        imagebutton:
            focus_mask True
            idle "Gallery/zaragallery03.png" xpos 1478 ypos 100
            hover "Gallery/zaragallery03.png"
            action Jump ("ZaraGallery03")

    if renpy.seen_image("mczarabedroom02") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("ZaraGallery")

    add "Gallery/galleryfuture.png" xpos 621 ypos 400

    add "Gallery/galleryfuture.png" xpos 1050 ypos 400

    add "Gallery/galleryfuture.png" xpos 1478 ypos 400

    add "Gallery/galleryfuture.png" xpos 620 ypos 700

    add "Gallery/galleryfuture.png" xpos 1048 ypos 700

    add "Gallery/galleryfuture.png" xpos 1478 ypos 700

    add "Gallery/gallerygrid02.png"
    add "Gallery/textzara.png"

label ZaraGallery01:
scene poolzara01
za "Oh, hello [name]! You found my secret hiding place..."
za "This is where I hang out in my free time..."   
za "...When I'm not busy pampering myself to be your sex slave for the evening..."
mc "Well, being a harem girl a full-time job. At least in MY harem."
scene poolzara02 with dissolve
za "I know, I have to do at least two hours of kegels in the morning to re-arrange my pussy after you've fisted and pounded me..."
mc "NICE."
za "Actually, I should go now, I need to insert insanely large objects into my pussy to get it into shape for... later this week."
scene poolzara03 with dissolve
za "Bye [name]!"
mc "Bye Zara. (What a fine ass...)"
mc "Oh well, I might as well go for a swim since she's leaving."
jump ZaraGallery

label ZaraGallery02:
scene bedroom02
show zarabedroom01
mc "Ah, there you are. I'm ready for a HOT night of sweet LOVE and PASSION!"
hide zarabedroom01
show zarabedroom02
with fastdissolve
za "Oh well, that's great to hear..."
mc "So let's get straigth to business shall we?"
mc "Belly-dance for me again..."
play music "Sounds/bellydance.mp3"
scene bedroom02 blurred
show zaradance01
call screen zaradance01x
screen zaradance01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ZaraDance02x")

label ZaraDance02x:
mc "OK, now for the nude belly-dancing at which you excel..."
za "Of course [name]!"
hide zaradance01
show zaradance02
call screen zaradance02x
screen zaradance02x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ZaraDanceEndx")


label ZaraDanceEndx:
mc "You're a natural at it Zara! WOW!"
za "Would you like me to turn around?"
mc "Oh YEAH!"
hide zaradance02
show zarabutt
call screen zarabutt01x
screen zarabutt01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ZaraButtEndx")

label ZaraButtEndx:
stop music
hide zarabutt
$ zaradancedone = True
show zarabedroom03
mc "That was... mesmerizing. Your amazing seductions skills could prove very useful on certain missions."
jump ZaraGallery

label ZaraGallery03:
scene bedroom02 blurred
show zarabedroom03
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

label ZaraFuckChoicex:
stop music
menu:
    "Let's dilate that pussy of yours with some fisting action!":
        jump ZaraFistingx
    "Give me a nice, slow handjob...":
        jump ZaraHandjobx   
    "Get on top of me and ride me like a... err... camel.":
        jump ZaraBouncex
    "Impale yourself on my love saber!":
        jump ZaraTopx
    "It is time for me to affirm my breeding rights." if renpy.seen_image("zaraprepreg01"):
        za "You... want to breed me? And put a baby in my belly?"
        mc "Yep. So get ready Zara, I'm gonna need to cum a LOT!"
        jump ZaraImpregnationx
    "I'm done with this gallery":
        jump ZaraGallery
 
label ZaraFistingx:
scene bedroom05 with dissolve
show prezarafist
mc "First a little lick to get your juices going...."
mc "And then..."
scene bedroom07 with dissolve
play music "Sounds/fucksound.mp3"
label ZaraFistingSlowx:
hide zarafistfast
show zarafistslow
call screen zarafistingslowx
screen zarafistingslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ZaraFistingEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ZaraFistingFastx") 

label ZaraFistingFastx:
hide zarafistslow
show zarafistfast
za "Yes, you're stretching me so wide with your fist!"
call screen zarafistingfastx
screen zarafistingfastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ZaraFistingEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ZaraFistingSlowx") 

label ZaraFistingEndx:
scene bedroom03b blurred
stop music
show zarafistend
za "You've totally stretched my hole... I can take anything in there now..."
mc "Let's test this theory..."
jump ZaraFuckChoicex

label ZaraHandjobx:
scene bedroom04 with dissolve
show zarabed04
mc "Get on your knees while you jack my crank..."
za "Of course Mast... I mean [name]."
scene bedroom06 blurred with dissolve
play music "Sounds/zarahandjob.mp3"
call screen zarahandjob01x
screen zarahandjob01x:
    modal True
    add zarahandjob
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ZaraHandjobCumx")
        
label ZaraHandjobCumx:
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
jump ZaraFuckChoicex

label ZaraBouncex:
scene bedroom09 with dissolve
show zarabed07
za "I can feel that powerful log between my asscheeks...."
mc "You're going to need to lift yourself up so I can bury it deep inside you while you ride me Zara!"
scene bedroom03 blurred
show zarabed05
za "It's so thick, it's stretching me wide open!"
mc "Let's stretch it some more then, bounce up and down on it Zara!"
scene bedroom08 blurred with dissolve
label ZaraBounceSlowx:
play music "Sounds/zarabounce.mp3"
hide zarabouncefast
show zarabounceslow
call screen zarabounceslowx
screen zarabounceslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ZaraBounceEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ZaraBounceFastx") 

label ZaraBounceFastx:
hide zarabounceslow
show zarabouncefast
za "My tits are bouncing all over the place, this is sssooo good!"
call screen zarabouncefastx
screen zarabouncefastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ZaraBounceEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ZaraBounceSlowx") 

label ZaraBounceEndx:
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
jump ZaraFuckChoicex
   
label ZaraTopx:
scene bedroom03
show prezararide
za "Ooh, it looks sssoo BIG against my tiny body. The cocktip goes all the way to my chest!"
mc "And yet, it will somehow fit..."
label ZaraTopSlowx:
scene bedroom03 blurred
play music "Sounds/fucksound.mp3"
show zararideslow
call screen zaratopslowx
screen zaratopslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ZaraTopEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ZaraTopFastx") 

label ZaraTopFastx:
scene bedroom03 blurred
show zararidefast
za "Oh God, you're pounding me so HARD [name]!"
call screen zaratopfastx
screen zaratopfastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ZaraTopEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ZaraTopSlowx")

label ZaraTopEndx:
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
jump ZaraFuckChoicex

label ZaraImpregnationx:
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
label ZaraPrePregSlowx:
hide zaratitsfast
show zaratitsslow
call screen zaratitsslow01x
screen zaratitsslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nextidle.png"
        action Jump ("ZaraPrePregEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ZaraPrePregFastx") 

label ZaraPrePregFastx:
za "Your cock is REALLY rock-hard! Keep fucking my breasts faster, please [name]!"
hide zaratitsslow
show zaratitsfast
call screen zaratitsfast01x
screen zaratitsfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nextidle.png"
        action Jump ("ZaraPrePregEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ZaraPrePregSlowx") 
        
label ZaraPrePregEndx:
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
label ZaraPregSlowx:
hide zarapregfast
show zarapregslow
call screen zarapregslow01x
screen zarapregslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("ZaraPregEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ZaraPregFastx") 

label ZaraPregFastx:
za "That's it, keep going, FASTER MASTER!"
hide zarapregslow
show zarapregfast
call screen zarapregfast01x
screen zarapregfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("ZaraPregEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ZaraPregSlowx") 

label ZaraPregEndx:
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
jump ZaraGallery



