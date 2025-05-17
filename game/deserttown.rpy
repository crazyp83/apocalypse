label DesertTownFar:
scene deserttown with dissolve
$ knowdeserttown = True
if townseen == False:
    mc "Ah, there's that town in the middle of the desert..."
    if withbe:
        be "Finally, we found some civilization... Maybe."
    if withpe:
        pe "Ah yes, I remember that town now. It's a Road Warriors town."
        mc "And you say that NOW???"
        pe "Well, I didn't remember where it was. Now I know."
mc "Let's move, it's already getting late."

label DesertTown:
$ townseen = True
scene townentrance with dissolve
mc "This place is pretty bustling. With random blacked female Genesis 8 figures."
label DesertTown02:
scene townentrance
call screen town01
screen town01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/back.png"
        hover "Icons/back.png"
        action Jump ("DesertTownLeave")
    imagebutton:
        focus_mask True
        idle "Icons/goleft.png"
        hover "Icons/goleft.png"
        action Jump ("GoLeft")
    imagebutton:
        focus_mask True
        idle "Icons/goright.png"
        hover "Icons/goright.png"
        action Jump ("GoRight")
        
label DesertTownLeave:
scene deserttown with dissolve
if alone and withnone:
    mc "I think I should head back now."
    jump BackHex25

if alone == False or withnone == False:
    mc "I think we should head back now."
if withbe:
    be "Alright, your call."
if withpe:
    pe "Alright, your call."
jump BackHex25
    
label GoLeft:
scene desertstreetleft
call screen townleft
screen townleft:
    modal True
    imagebutton:
        focus_mask True
        idle "deserttown/tattooistidle.png"
        hover "deserttown/tattooisthover.png"
        action Jump ("Tattoo")
    if scoutinbath == False:
        imagebutton:
            focus_mask True
            idle "deserttown/hammamidle.png"
            hover "deserttown/hammamhover.png"
            action Jump ("Hammam01")
    imagebutton:
        focus_mask True
        idle "Icons/back.png"
        hover "Icons/back.png"
        action Jump ("DesertTown02")

label GoRight:
stop music
scene desertstreetright
call screen townright
screen townright:
    modal True
    imagebutton:
        focus_mask True
        idle "deserttown/bounceridle.png"
        hover "deserttown/bouncerhover.png"
        action Jump ("StripClub")
    imagebutton:
        focus_mask True
        idle "deserttown/marketidle.png"
        hover "deserttown/markethover.png"
        action Jump ("Market01")
    imagebutton:
        focus_mask True
        idle "Icons/back.png"
        hover "Icons/back.png"
        action Jump ("DesertTown02")

label Hammam01:
$ scoutinbath = True
if missionhg and donemissionhg:
    if withbe:
        mc "Wait for me outside Bella, I need to speak in private to that girl."
        be "That sounds fishy, but since the pool is empty, I don't mind."
    if withpe:
        mc "Wait for me outside Bella, I need to speak in private to that girl."
        pe "That sounds fishy, but since the pool is empty, I don't mind."
    if alone and withnone == False:
        call AloneStance
    if alone and withnone:
        mc "I'm alone, free and unencumbered by pesky sidekicks, so I can enter the hammam without justifying myself to anyone..."
    scene hammam01 with dissolve
    mc "Ah , the pool is back to full capacity, it worked!"
    show hammamgirl01 with moveinright
    hg "Hello [name], I can't thank you enough for restoring our pool water!"
    mc "It was tough, I had to defeat a very evil man with three eyes."
    hide hammamgirl01
    show hammamgirl02    
    with fastdissolve
    hg "Oh, wow, you're such a hero. I'd say you're DA MAN, but that's already taken."
    mc "So what's my reward?"
    hg "Well, for starters, the pool is FREE FOR LIFE for you obviously..."
    hg "Also, I have something you might find useful. A militiaman forgot his uniform on his last visit... I'm giving it to you as a sign of gratitude."
    window hide
    show militiauni at posmission
    pause
    hide militiauni
    $ militiauniform = True
    hg "And finally..."
    hide hammamgirl02
    show hammamgirl03    
    with fastdissolve
    hg "Come and FUCK ME!"
    mc "Alright!"
    scene hammam04 with dissolve
    mc "So, we've got this corner of the pool to ourselves again..."
    hg "Of course, all the better for me to give you a nice LONG sensuous handjob!"
    $ fuckedhammam03 = True
    jump HammamHandJobSlow
    
if missionhg and donemissionhg == False:
    if persistent.tipson:
        show hammamtip at tips with dissolve
        pause
        hide hammamtip            
    scene hammam01b with dissolve
    mc "Ah yes, the pool is still empty... I remember now."
    show hammamgirl01 with fastdissolve
    hg "Hello [name], did you manage to find out where our water has gone?"
    mc "Err... Not yet. But I'm working on it."
    hide hammamgirl01
    show hammamgirl04    
    hg "Well, that was a complete waste of time coming here then, hey?"
    mc "Yep. My bad."
    if withbe:
        be "Well, we'd better head back home, it's getting late."
    if withpe:
        pe "Well, we'd better head back home, it's getting late."
    if alone and withnone:
        mc "Well, I'd better head back home, it's getting late."
    hide hammamgirl04 with dissolve
    jump BackHex25    

if fuckedhammam == False:
    if alone and withnone == False:
        call AloneStance
    scene hammam01 with dissolve
    mc "This place sure looks nice...."
    show hammamgirl01 with fastdissolve
    hg "Welcome to Sulfurous Hammam!"
    mc "That name doesn't sound very enticing..."
    hide hammamgirl01
    show hammamgirl02
    hg "On the contrary, sulfur helps in the regeneration of radioactivity-ladden skin. It's only 5 dollars, well worth a try. I'll be taking a dip myself in a moment."
    if withbe:
        be "Cleanliness is next to Godliness and I can't miss out on this opportunity to cleanse my skin of sin and radioactivity, I'm in!"
    if withpe:
        pe "That sounds interesting... I was having some unusual rashes lately, and I can just about afford it, so I'll give it a try!"
    menu:
        "Join them (-5$)" if money >= 5 and alone == False:
            $ money -= 5
            jump Hammam02
        "Don't join them" if money >= 5 and alone == False:
            $ scoutinbath = False
            if withbe:
                mc "Not for me, thanks... We'll see each other later Bella."
            if withpe:
                mc "Not for me, thanks... We'll see each other later Penny."
            jump GoLeft
        "Join her (-5$)" if money >= 5 and alone:
            $ money -= 5
            jump Hammam02alone
        "Don't join her" if money >= 5 and alone:
            $ scoutinbath = False
        "I don't have enough money..." if money <= 4:
            hg "Well that's too bad, boy..."
            $ scoutinbath = False
            if withbe:
                mc "We'll see each other later Bella."
            if withpe:
                mc "We'll see each other later Penny."
            jump GoLeft

if fuckedhammam02 and missionhg == False:
    scene hammam01b with dissolve
    mc "Oh damn, the pool is empty for some reason..."
    show hammamgirl02 with fastdissolve
    hg "Hello [name], as you can see, the hammam has suffered a terrible tragedy."
    mc "What happened?"
    hide hammamgirl02
    show hammamgirl04 with fastdissolve
    hg "I suspect someone has been diverting the natural source of our water for his own profit! As if our planet didn't suffer enough already!"
    hg "I wondered if... you could help me."
    mc "Sure thing, I have a quest and mission interface just for dealing with stuff like that."
    hide hammamgirl04
    show hammamgirl02 with fastdissolve
    hg "Right, right. Then, find out what happened please, and get our precious water back where it belongs!"
    window hide
    show missionhg at posmission
    pause
    hide missionhg
    $ missionhg = True
    mc "I'll get right on it. Whoever stole that water will pay for it!"
    if persistent.tipson:
        show hammamtip at tips with dissolve
        pause
        hide hammamtip            
    if withbe:
        be "Well, we'd better head back home, it's getting late."
    if withpe:
        pe "Well, we'd better head back home, it's getting late."
    if alone:
        mc "Well, I'd better head back home, it's getting late."
    jump BackHex25

if fuckedhammam and missionhg == False:
    scene hammam01 with dissolve
    mc "I hope that hot black chick is there again..."
    show hammamgirl01 with fastdissolve
    mc "Ah, there she is, fast-dissolving into the screen, just like I like it."
    hg "Hello [name]! You're back again for some MORE? *wink*"
    if withbe:
        be "What does she mean?"
        mc "Err... Nothing."
    if withpe:
        pe "What does she mean?"
        mc "Err... Nothing."
    hide hammamgirl01
    show hammamgirl02 with fastdissolve
    hg "A special deal for you today: a FREE hammam session in the sulfuric baths!"
    if withbe:
        be "Oh, wow, thanks, I'll go right in then!"
        mc "I'll follow you two."
        jump Hammam02
    if withpe:
        pe "Oh, wow, thanks, I'll go right in then!"
        mc "I'll follow you two."
        jump Hammam02
    if alone:
        mc "Alright, I'm in then! I'll follow you."
        jump Hammam02alone

label Hammam02alone:
hide hammamgirl02
show hammamgirl03
hg "Great, take your clothes off, it's the best way to enjoy the sulfur on EVERY part of your skin..."
scene hammam02c with dissolve
hg "Are you ready yet?"
mc "Hell YEAH! Almost there, I'm getting my clothes off as fast as I can!"
scene hammam04 with dissolve
if fuckedhammam == False:
    mc "Time to make a move on that hot chick..."
if fuckedhammam:
    mc "I'm on my own with that hot chick again..."
jump HammamPrefuck

label Hammam02:
hide hammamgirl02
show hammamgirl03
hg "Great, take your clothes off, it's the best way to enjoy the sulfur on EVERY part of your skin..."
if withbe:
    scene hammam02a with fade
if withpe:
    scene hammam02b with fade
hg "Are you ready yet?"
mc "Hell YEAH! Almost there, I'm getting my clothes off as fast as I can!"
if withbe:
    be "I'm going ahead, I want to cleanse my sins as fast as possible!"
    play sound "Sounds/dive.mp3"
    scene hammam03a with dissolve
    be "Oh Phallus Lord, protect me from sin and... blablabla..."
    if fuckedhammam == False:
        mc "Right, Bella is praying the Mighty Phallus Lord, so I have time to show MY mighty phallus to that hot chick then..."
    if fuckedhammam:
        mc "I'm on my own with that hot chick..."        
if withpe:
    pe "I'm jumping in right now in that pool, cos I am a Road Warrior and we don't wait around for no one!"
    play sound "Sounds/dive.mp3"
    scene hammam03b with dissolve
    pe "Err, where are you guys? Damn, I can't see a thing in that fog... Oh, screw it, I don't need them to enjoy that sulfuric acid on my skin!"
    if fuckedhammam == False:
        mc "Now that Penny is lost in the sulfuric mist of that pool, time to make a move on that hot chick..."
    if fuckedhammam:
        mc "I'm on my own with that hot chick..."

scene hammam04 with dissolve
label HammamPrefuck:
if fuckedhammam == False:
    mc "So, what's a nice girl like you doing in a sulfurous place like this?"
    if withbe or withpe:
        hg "What a charmer..., And a naughty one at that, you're sporting a MASSIVE hardon! What if your friend sees us?"
        mc "I'd say she's lost in the fog and we have enough time to get better acquainted..."
    if alone:
        hg "What a charmer..., And a naughty one at that, you're sporting a MASSIVE hardon! What if someone were to see us?"
        mc "I'd say the sulfurous fog will keep them at bay and we have enough time to get better acquainted..."
    scene hammam05 with dissolve
    hg "You mean better acquainted like that? With my tiny hand wrapped around your monster pole?"
    mc "AAAH, yeah, just like that..."
if fuckedhammam:
    mc "So, we've got this corner of the pool to ourselves again..."
    hg "You did it on purpose didn't you, NAUGHTY BOY!"
    scene hammam05 with dissolve
    hg "But I don't mind, if I gave you a free session, it was to be alone with THAT delicious log!"
    mc "AAAH, yeah, just like that..."
    $ fuckedhammam02 = True

label HammamHandJobSlow:
hide screen mcstats
hide screen calendar
play music "Sounds/wank.mp3"
hide hammamhandjobfast
show hammamhandjobslow
call screen hammamhandjobslow
screen hammamhandjobslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HammamHandJobEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("HammamHandJobFast") 

label HammamHandJobFast:
hide hammamhandjobslow
show hammamhandjobfast
mc "Yes, faster! AAAHH!"
call screen hammamhandjobfast
screen hammamhandjobfast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HammamHandJobEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("HammamHandJobSlow") 

label HammamHandJobEnd:
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
scene hammamhandjob07
show hacum01
$ renpy.pause(0.06, hard=True)
scene hammamhandjob06
show hacum02
$ renpy.pause(0.06, hard=True)
scene hammamhandjob05
show hacum03
$ renpy.pause(0.06, hard=True)
scene hammamhandjob04
show hacum04
$ renpy.pause(0.06, hard=True)
scene hammamhandjob03
show hacum05
$ renpy.pause(0.06, hard=True)
scene hammamhandjob02
show hacum06
$ renpy.pause(0.06, hard=True)
scene hammamhandjob01
show hacum07
$ renpy.pause(0.06, hard=True)
scene hammamhandjob02
show hacum08
$ renpy.pause(0.06, hard=True)
scene hammamhandjob03
show hacum09
$ renpy.pause(0.06, hard=True)
scene hammamhandjob04
show hacum10
$ renpy.pause(0.06, hard=True)
scene hammamhandjob05
show hacum11
$ renpy.pause(0.12, hard=True)
scene hammamhandjob07
show hacum12
$ renpy.pause(0.06, hard=True)
scene hammamhandjob06
show hacum13
$ renpy.pause(0.06, hard=True)
scene hammamhandjob05
show hacum14
$ renpy.pause(0.06, hard=True)
scene hammamhandjob04
show hacum15
$ renpy.pause(0.06, hard=True)
scene hammamhandjob03
show hacum16
$ renpy.pause(0.06, hard=True)
scene hammamhandjob02
show hacum17
$ renpy.pause(0.06, hard=True)
scene hammamhandjob01
show hamcum01
$ renpy.pause(0.06, hard=True)
scene hammamhandjob02
show hamcum02
$ renpy.pause(0.06, hard=True)
scene hammamhandjob03
show hamcum03
$ renpy.pause(0.06, hard=True)
scene hammamhandjob04
show hamcum04
$ renpy.pause(0.06, hard=True)
scene hammamhandjob05
show hamcum05
$ renpy.pause(0.06, hard=True)
scene hammamhandjob06
show hamcum06
$ renpy.pause(0.06, hard=True)
scene hammamhandjob07
show hamcum07
$ renpy.pause(0.06, hard=True)
scene hammamhandjob06
show hamcum08
$ renpy.pause(0.06, hard=True)
scene hammamhandjob05
show hamcum09
$ renpy.pause(0.06, hard=True)
scene hammamhandjob04
show hamcum10
$ renpy.pause(0.06, hard=True)
scene hammamhandjob03
show hamcum11
$ renpy.pause(0.06, hard=True)
scene hammamhandjob02
show hamcum12
$ renpy.pause(0.06, hard=True)
show hamcum13
$ renpy.pause(0.06, hard=True)
stop music
scene hammamcumend01
hg "Oh my God, you cum like a STALLION!"
scene hammamcumend02
if fuckedhammam == False:
    hg "But So soon?"
    mc "Yeah, we don't have much time, and I want to FUCK YOU. Now my shaft is nice and slick, it will plough through your hole like BUTTER!"
    hg "Oh, wow, you can just stay hard like that???"
    mc "That's right, I'm the HERO of this game and I have UNLIMITED cum supplies in my balls!"
    mc "Not like that wimp in Battle of the Bulges who can only nut like 5 times a day."
    hg "O-kay. No idea what you're talking about, but please let me do the riding, I don't want you to destroy my poor pussy by being too rough."
    mc "No worries, you go for a ride girl!"
if fuckedhammam:
    hg "Just like last time, a mighty load to prep your monster dong for my FUCKHOLE!"
    mc "That's right, now you can jump aboard the mighty \"Titanic Rod\" and sink your pussy on it!"
    
scene hammamfuck with dissolve
label HammamFuckSlow:
play music "Sounds/fucksound.mp3"
hide hammamfuckfast
show hammamfuckslow
call screen hammamfuckslow
screen hammamfuckslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HammamFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("HammamFuckFast") 

label HammamFuckFast:
hide hammamfuckslow
show hammamfuckfast
call screen hammamfuckfast
screen hammamfuckfast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HammamFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("HammamFuckSlow") 

label HammamFuckEnd:
$ fuckedhammam = True
stop music
scene hammamfuckcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Damn, you're making me cum AGAIN! RHAAA!"
hg "What, it's OVERFLOWING my pussy, you had THAT MUCH left in you???"
show screen mcstats
show screen calendar
if fuckedhammam03:
    mc "Yep, I have unlimited supplies in my alpha-radiated nuts!"
    mc "But I'd better get back to my compound, it's getting late. We'll meet again hopefully, hammam girl!"
    hg "I sure hope so, [name] the hero!"
    if withpe:
        scene desertstreetleft 
        show pennyout02
        with dissolve
        pe "Ah, there you are, finally! No, don't tell me what you did in there, I don't want to know! let's just go back to the compound."
        jump BackHex25
    if withbe:
        scene desertstreetleft 
        show bellaout05
        with dissolve
        be "Ah, there you are, finally! It's getting LATE! We need to go back to the compound. And we've achieved NOTHING on this scouting mission."
        mc "Speak for yourself..."
        jump BackHex25
    jump BackHex25
    
mc "I could fuck you some more, but I think we don't have enough time..."
if alone:
    mc "It's getting late, I'd better head back to the compound."
    jump BackHex25
hg "You're right, we'd better get cleaned up before your friend returns..."
if withbe:
    scene hammam06a with dissolve
    be "So, did you cleanse your skin? I feel like a sin-free VIRGIN now!"
    mc "Yeah, we were waiting for you Bella, I think it's time to go..."
    be "You're right, let's dry ourselves up and go back to the compound."
    hg "It was a PLEASURE having you around, I hope you both come back soon!"
if withpe:
    scene hammam06a with dissolve
    pe "So, did you go in and enjoy the baths [name]? I couldn't find you two in the dense sulfuric mist..."
    mc "Yeah, we did, we were waiting for you Penny, I think it's time to go..."
    pe "You're right, let's dry ourselves up and go back to the compound."
    hg "It was a PLEASURE having you around, I hope you both come back soon!"
jump BackHex25

label Tattoo:
scene tattoo01 with dissolve
if mcwarrior <= 3:
    show tattooist02
    tt "Hello, I'm afraid I only make tattoos for Road Warriors. And you're nowhere near to being one!"
    mc "What a bummer, I really wanted one..."
    jump GoLeft
show tattooist01
if fuckedtattoo:
    tt "Oh, hi [name], nice to see you here again. I'll give a SPECIAL discount this time... A tattoo free of charge!"
    tt "But not free of DISCHARGE from that cum-cannon of yours! What do you say?"
    menu:
        "I say bring it on!":
            jump Tattoo02
        "I'd love too but I'm too busy... Another time.":
            hide tattooist01
            show tattooist02
            tt "Very disappointing. What's the point of carrying that log between your legs if you don't use it?"
            mc "Err... Yeah good point. But I'm not the player, he's the one who took this ill-advised decision."
            jump GoLeft
if fuckedtattoo == False:
    tt "Hello, you want a Road Warrior tattoo? Just 10$ and I'll make one of your choice... WHEREVER you want. And if you are already a Road Warrior, you get a discount."
menu:
    "Yes, I'm interested in getting one indeed... (-10$, +1 Road Warriors, faction change)" if mcwarrior == 4 and money >= 10:
        hide tattooist01
        show tattooist03
        tt "Step right in!"
        $ money -= 10
        jump Tattoo02
    "Yes, since I am a Road Warrior, I should really get one... (-5$)" if mcwarrior == 5 and money >= 5:
        hide tattooist01
        show tattooist03
        tt "Ah, in that case, it's only five dollars for you, step right in!"
        $ money -= 5
        jump Tattoo02
    "No thanks.":
        hide tattooist01
        show tattooist02
        tt "That's all I do in this shop... Goodbye."         
        jump GoLeft

label Tattoo02:
scene tattooparlor02 with dissolve
tt "Now, where would you like your tattoo?"
mc "On my cock. It seems appropriate since it has a HUGE skin surface area to work on."
show tattooparlor02b
tt "Err, okay, that's a rather unusual request... But I'll do it, I'm curious..."
hide tattooparlor02b
tt "So get undressed then. And get hard cos I need to do it on distended skin! *wink*"
mc "Sure thing!"

label TattooCock:
scene tattoocock01 with dissolve
tt "Wow, that's a HUGE Road Warrior dong you have there!"
tt "I didn't know they could come THAT big! I never worked on such a MASSIVE fuckstick before..."
mc "Well go ahead, it's all yours."
scene tattoocock02 with dissolve
play music "Sounds/tattoodrill.mp3"
tt "Does it hurt?"
mc "Not a bit..."
scene tattoocock03 with fastdissolve
tt "It would be good if you stopped pumping all that pre-cum that's dripping down your shaft..."
mc "Oops, sorry, it has a mind of its own..."
tt "You can unload it AFTERWARDS."
scene tattoocock02 with fastdissolve
$ renpy.pause(2.0, hard=True)
stop music
tt "There, done!"
if mcwarrior <= 4:
    call PlusWarriorReal
tt "And now..."
scene tattoocock04 with dissolve
tt "Pump your seed, give me as much as you can muster STUD!"
hide screen mcstats
hide screen calendar
label TattooHandJobSlow:
hide tattoohandjobfast
show tattoohandjobslow
call screen tattoohandjobslow
screen tattoohandjobslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TattooHandJobEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TattooHandJobFast") 

label TattooHandJobFast:
hide tattoohandjobslow
show tattoohandjobfast
call screen tattoohandjobfast
screen tattoohandjobfast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TattooHandJobEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("TattooHandJobSlow") 

label TattooHandJobEnd:
scene tattoohandjob01
show tattoocum01
mc "RHAAAA!"
tt "Yes, gimme, gimme, cover my apron in your thick load!"
scene tattoohandjob04 with fastdissolve
show tattoocum02
tt "Keep going! But ON my apron, not my FACE!"
mc "I AM! It's sssoo goood!"
scene tattoocum03 with fastdissolve
tt "That's better, I can lick it  up later that way...."
show tattoocum04
tt "Thanks for all that delicious cream Mr ROAD WARRIOR. Come back anytime, some Road Warriors have more than one tattoo!"
$ mctattoo = True
show screen mcstats
show screen calendar

scene desertstreetleft with fade
if alone:
    mc "I'd better head back to the compound, it's getting late."
    jump BackHex25
if withbe:
    show bellaout03
    be "It's getting late and you've wasted your time getting a stupid tattoo... Let's go back to the compound."
    if scoutinbath:
        mc "Hey, you pampered yourself in sulfur while I was getting that tattoo! And it shows too, phew, what a smell..."
        hide bellaout03
        show bellaout04
        be "You don't like how I smell? Too bad for you, you're stuck with me all the way back to the compound!"
if withpe:
    show pennyout03
    pe "You'll have to show me that Road Warrior tattoo some time... But for now, let's go back to the compound, it's getting late."
    if scoutinbath:
        mc "Hey, you pampered yourself in sulfur while I was getting that tattoo! And it shows too, phew, what a smell..."
        hide pennyout03
        show pennyout02
        pe "You don't like how I smell? Too bad for you, you're stuck with me all the way back to the compound!"
jump BackHex25

label Market01:
if withbe:
    be "I'll stay back while you go...shopping."
if withpe:
    pe "I'll stay back while you go...shopping."
if alone and withru:
    ru "I'll stay back while you go...shopping. Which is for sissies."
if alone and withan:
    an "There are too many people on the market square, I'm scared. I think I'll wait for you here in the corner, where no one will notice me..."
if alone and withmo:
    mo "Why are you taking us back to this dreadful place? I can't stand it there, I just won't go there! PLEASE TAKE ME BACK [name]!"
    mc "Okay, okay, sorry, let's leave then."
    jump LeaveMarket
if alone and witham:
    am "I don't like that camel girl over there, camels are meant to live free in the wild! So I'll stay back."
if alone and withmi:
    mi "There are too many people on the market square, we might get lost. I think I'll wait for you here at the exit..."
if alone and withcy:
    cy "I fear my presence in this place might attract unwanted attention. I shall wait for you here at the exit."
if alone and withay:
    ay "A busy market? BORING. I'll stay back here instead and have fun by myself."
if alone and withza:
    za "Sorry [name], but I don't want to risk becoming a slavegirl to this man over there. I think I'll wait for you here at the exit..."
if alone and withsu:
    su "I think I'll leave you it, I spotted a ethernet hub hidden behind that tree, and I need to connect to my secret server."
if alone and withgw:
    gw "I don't like this place. It looks like it's full of sexual predators. It reminds of the lab when YOU'RE IN IT. SO I'll leave you to it..."
if alone and withma:
    ma "Well, I'll be in the stripclub chatting with some old friends while you do whatever it is you do here."
if alone and withcl:
    cl "I'll go and check if they sell any religious artefact. I think I saw a nice wooden Phallus over there."
if alone and withla:
    la "I'll go and check if they sell any interesting plants. They look like barbarians, but maybe some of them are nice people."
    mc "Be careful Laurie, cos they're NOT nice people."

if stonepiece08 == False and missionge == True and boughtmom:
    scene market01
    show cageempty
    show stone08idle
    with dissolve
if stonepiece08 == False and missionge == True and boughtmom == False:
    scene market01
    show stone08idle
    with dissolve
stop sound
stop music
play music "Sounds/market.mp3"
label Market01b:
if stonepiece08 == False and missionge == False and boughtmom == False:
    scene market01
if stonepiece08 == False and missionge == False and boughtmom:
    scene market01
    show cageempty
if stonepiece08 == False and missionge and boughtmom:
    scene market01
    show cageempty
    show stone08idle
if stonepiece08 == False and missionge and boughtmom == False:
    scene market01
    show stone08idle
if stonepiece08 and missionge and boughtmom == False:
    scene market01
if stonepiece08 and missionge and boughtmom:
    scene market01
    show cageempty
    
call screen market01a
screen market01a:
    modal True
    if boughtmom == False:
        imagebutton:
            focus_mask True
            idle "deserttown/cageidle.png"
            hover "deserttown/cagehover.png"
            action Jump ("MarketCage")
    imagebutton:
        focus_mask True
        idle "deserttown/slaveridle.png"
        hover "deserttown/slaverhover.png"
        action Jump ("MarketSlaver")
    imagebutton:
        focus_mask True
        idle "deserttown/spicegirlidle.png"
        hover "deserttown/spicegirlhover.png"
        action Jump ("MarketSpice")
    imagebutton:
        focus_mask True
        idle "deserttown/camel02idle.png"
        hover "deserttown/camel02hover.png"
        action Jump ("MarketCamel")
    imagebutton:
        focus_mask True
        idle "deserttown/camelgirlidle.png"
        hover "deserttown/camelgirlhover.png"
        action Jump ("CamelSeller")
    imagebutton:
        focus_mask True
        idle "Icons/leave.png"
        hover "Icons/leave.png"
        action Jump ("LeaveMarket")
    if stonepiece08 == False and missionge == True:
        imagebutton:
            focus_mask True
            idle "Icons/stone08idle.png"
            hover "Icons/stone08hover.png"
            action Jump ("StonePiece08")

label LeaveMarket:
if marketseen:
    if withbe:
        be "Are you done with your shopping?"
        mc "Yes, and we should head back, it's getting late..."
    if withpe:
        pe "Are you done with your shopping?"
        mc "Yes, and we should head back, it's getting late..."
    if alone:    
        mc "I should head back to the compound, it's getting late..."
    jump BackHex25
jump GoRight

label MarketCamel:
mc "Hey, kitty, kitty, kitty..."
mc "No answer. How rude."
jump Market01b

label StonePiece08:
scene market01
if boughtmom:
    show cageempty
"You found one of the missing pieces of the Stone Artefact."
$ stonepieces -= 1
window hide
show achievementgenie at posmission
$ renpy.pause(0.5, hard=True)
show text "{font=Gui/Boogaloo-Regular.ttf}{color=#ff0000}{size=30}[stonepieces]{/font}" at StonePosition
$ renpy.pause(2.0, hard=True)
hide achievementgenie
hide text
$ stonepiece08 = True
jump Market01b

label MarketCage:
if sawmom:
    scene nancycage02 with dissolve
    mo "[name], please get me out of this horrible cage, I beg you!"
    mc "Yeah, yeah, I'm working on it, show some patience."
    mo "Easy for YOU to say!"
    jump Market01b   
scene nancycage01 with dissolve
mc "Damn, these people put women in cages, they really are barbarians. Or maybe just Republicans."
mc "Hang on a minute, I... recognize her... It's NANCY!"
scene nancycage02 with dissolve
mo "[name]! Is that you? Oh my God, I thought you were dead! My sweet, sweet tenant!"
mc "Nancy! I thought you were dead too! What happened to you?"
mo "I... ended up here, I was kidnapped by a gang of horrible people who sold me as a slave! Please get me out of here, I beg you!"
mc "Of course Nancy, you can count on me!"
if sawmom == False:
    call LustPlusNancy
$ sawmom = True
$ metmo = True
$ marketseen = True

label MarketSlaver:
$ marketseen = True
scene market02 with dissolve
label SlaverChoice:
show slaver01b
if boughtmom:
    sl "Well, hello sir, how do you find your recent purchase? Are you a 100\% satisfied customer?"
    mc "Err... Yes, I guess I am."
    sl "Well, that's great to hear. I don't have any more slaves today to show you I'm afraid, they were taken out for a walk. Come back another time."
    mc "Right, I'll do that."
    jump Market01b
menu:
    "OK, I'm ready to buy that slave!" if spokeslaver and money >= 200:
        scene market02 with dissolve
        show nancy01 at midleft
        show slaver03b at midright
        show nancy01 at midleft
        sl "Excellent purchase my friend! I'll wrap her up for you. Is it a present?"
        $ money -= 200
        mc "Err... No, it's to go."
        if sawmom == False:
            mc "Hang on, I recognize that woman... It's NANCY!"
        hide slaver03b
        show slaver02b at midright
        sl "Fine sir, then she's all yours, here are the keys. To the collar."
        $ boughtmom = True
        jump BoughtNancy
    "So what do you sell?" if spokeslaver02 == False:
        $ spokeslaver02 = True
        sl "The best whores in town! At reasonable prices may I add... Right now, we hold an '87 MILF model waiting to please a refined customer!"
        hide slaver01b
        show slaver03b
        sl "Something tells me YOU are a VERY refined customer. Am I right or am I right, sir?"
        mc "Err... I guess you're right."
        hide slaver03b
        jump SlaverChoice
    "Hey you, let her out or I'll fucking kill you!" if sawmom:
        hide slaver01b
        show slaver04b
        sl "Loser without a taser says what?"
        mc "What?... Oh shit."
        hide slaver04b
        show slavershootb
        sl "LOSER!"
        show slavertasershot
        play sound "Sounds/taser.mp3"
        scene market02b with hpunch
        $ renpy.pause(2.0, hard=True)
        scene market02
        show slavershootb
        hide slavertasershot
        mc "Hey, stop it, it fucking hurts!"
        call MCInjury   
        $ mcinjuredtaser = True
        scene market02 with fade
        show slaver01b        
        sl "So, you are going to be more cooperative from now on sir?"
        mc "Yes... yes, I will. Sir."
        jump SlaverChoice        
    "How much for that whore in the cage?":
        $ spokeslaver = True
        hide slaver01b
        show slaver03b
        sl "For you my friend, 200 new Dollars. Top quality product, 100\% customer satisfaction guaranteed!"
        mc "What? That is WAY too expensive!"
        hide slaver03b
        show slaver01b
        sl "I suggest you inspect the merchandise sir, you will find the price is a bargain for such a top-of-the-range model..."
        mc "Alright, let me have a closer look then."
        sl "Sure, I'll get her out of her cage."
        hide slaver01b
        show nancy01 at midleft with dissolve
        show slaver02b at midright with dissolve
        sl "See? She is in perfect condition... 32DDD-24-36. A bit of mileage of course, she's an '87 MILF model. \nBut ain't she a beauty, sir?"
        if sawmom == False:
            mc "(Hang on a minute, I... recognize her, it's Nancy!!!)"
        mc "Ahem... Sure, sure... What about the back?"
        sl "Oh, you won't be disappointed my friend, she's got one fine booty. Turn around slave!"
        hide nancy01
        show nancy02 at midleft with dissolve
        hide slaver02b
        show slaver01b at midright
        sl "Not a scratch, nothing. And only 200 new Dollars for this top notch quality product. What do you say, sir?"
        menu:
            "Not bad, but I'd like to check out the nipples. I'm a nipple man you see...":
                sl "Whatever rocks your boat sir. Get your top off for the nice customer slave!"
                hide nancy02
                show nancy03 at midleft
                call LustMinusNancy            
                sl "Don't hesitate to step closer sir, so you can better inpect those funbags... Best in town, 100\% customer satisfaction guaranteed!"
                hide slaver01b
                hide nancy03
                scene market02 blurred
                show nancy04 with fastdissolve
                mc "Yes, yes, I see better the quality of the product now..."
                hide nancy04
                show nancy05 with dissolve
                if sawmom:
                    mo "Why did you ask to see my tits? That is so embarrassing!" 
                    mc "I'm just doing that so he thinks I'm a genuine customer Nancy."
                    mo "Just get me out of here, please!"
                if sawmom == False:
                    mc "\*whispering\* Nancy, it's ME! I'll get you out of here, I promise!"
                    mo "Oh my God! I thought you were dead!"
                    call LustPlusNancy
                    mc "Don't speak too loud and pretend we don't know each other, I've got a plan..."
                    mo "Please, I beg you, get me out of this horrible place!"
                    $ sawmom = True
                    $ metmo = True
                scene market02
                show slaver01b at midright
                show nancy03 at midleft                                
                menu:
                    "Okay, you convinced me, I'll buy her!" if money >= 200:
                        $ money -= 200
                        hide slaver01b
                        show slaver03b at midright
                        sl "Excellent purchase my friend! I'll wrap her up for you. Is it a present?"
                        mc "Err... No, it's to go."
                        sl "Fine sir, then she's all yours, here are the keys. To the collar."
                        call PlusWarrior
                        $ boughtmom = True
                        jump BoughtNancy
                    "I'll have to think about it, I'll come back another time...":
                        $ sawmom = True
                        $ metmo = True
                        sl "Don't take too long to think it over sir, such quality alpha-radiated slaves usually go in no time!" 
                        jump Market01b                    
            "Okay, you convinced me, I'll buy her!" if money >= 200:
                scene market02 with dissolve
                show slaver03b at midright
                show nancy01 at midleft
                sl "Excellent purchase my friend! I'll wrap her up for you. Is it a present?"
                $ money -= 200
                mc "Err... No, it's to go."
                sl "Fine sir, then she's all yours, here are the keys. To the collar."
                call PlusWarrior
                $ boughtmom = True
                $ sawmom = True
                $ metmo = True
                jump BoughtNancy
            "I'll have to think about it, I'll come back another time...":
                $ sawmom = True
                $ metmo = True
                sl "Don't take too long to think it over sir, such quality alpha-radiated slaves usually go in no time!" 
                jump Market01b
        
    "I'd like to inspect the merchandise please.":
        $ spokeslaver = True
        sl "Of course. I'll get her out of her cage so you can inspect her better."
        hide slaver01b
        show nancy01 at midleft with dissolve
        show slaver02b at midright with dissolve
        sl "See? She is in perfect condition... 32DDD-24-36. A bit of mileage of course, she's an '87 MILF model. But ain't she a beauty, sir?"
        if sawmom == False:
            mc "(Hang on a minute, I... recognize her, it's Nancy!!!)"
        mc "Ahem... Sure, sure... What about the back?"
        sl "Oh, you won't be disappointed my friend, she's got one fine booty. Turn around slave!"
        hide nancy01
        show nancy02 at midleft
        hide slaver02b
        show slaver01b at midright
        sl "Not a scratch, nothing. And only 200 new Dollars for this top notch quality product. What do you say, sir?"
        menu:
            "Not bad, but I'd like to check out the nipples. I'm a nipple man you see...":
                sl "Whatever rocks your boat Sir. Get your top off for the nice customer slave!"
                hide nancy02
                show nancy03 at midleft
                call LustMinusNancy            
                sl "Don't hesitate to step closer Sir, so you can better inpect those funbags... Best in town, 100\% customer satisfaction guaranteed!"
                hide slaver01b
                scene market02 blurred
                hide nancy03
                show nancy04 with fastdissolve 
                mc "Yes, yes, I see better the quality of the product now..."                
                hide nancy04
                show nancy05 with dissolve
                if sawmom:
                    mo "Why did you ask to see my tits? That is so embarrassing!" 
                    mc "I'm just doing that so he thinks I'm a genuine customer Nancy."
                    mo "Just get me out of here, please!"
                if sawmom == False:
                    mc "\*whispering\* Nancy, it's ME! I'll get you out of here, I promise!"
                    mo "Oh my God! I thought you were dead!"
                    call LustPlusNancy 
                    mc "Don't speak too loud and pretend we don't know each other, I've got a plan..."
                    mo "Please, I beg you, get me out of this horrible place!"
                    $ sawmom = True
                    $ metmo = True
                scene market02
                show slaver01b at midright
                show nancy03 at midleft                                
                menu:
                    "Okay, you convinced me, I'll buy her!" if money >= 200:
                        hide slaver01b
                        show slaver03b at midright
                        sl "Excellent purchase my friend! I'll wrap her up for you. Is it a present?"
                        $ money -= 200
                        mc "Err... No, it's to go."
                        hide slaver03b
                        show slaver02b at midright
                        sl "Fine sir, then she's all yours, here are the keys. To the collar."
                        call PlusWarrior                       
                        $ boughtmom = True
                        jump BoughtNancy
                    "I'll have to think about it, I'll come back another time...":
                        sl "Don't take too long to think it over sir, such quality alpha-radiated slaves usually go in no time!" 
                        jump Market01b
            "Okay, you convinced me, I'll buy her!" if money >= 200:
                scene market02 with dissolve
                show nancy01 at midleft
                show slaver03b at midright
                show nancy01 at midleft
                sl "Excellent purchase my friend! I'll wrap her up for you. Is it a present?"
                $ money -= 200
                mc "Err... No, it's to go."
                hide slaver03b
                show slaver02b at midright
                sl "Fine sir, then she's all yours, here are the keys. To the collar."
                call PlusWarrior
                $ boughtmom = True
                jump BoughtNancy
            "I'll have to think about it, I'll come back another time...":
                $ sawmom = True
                $ metmo = True
                sl "Don't take too long to think it over sir, such quality alpha-radiated slaves usually go in no time!"
                jump Market01b
    "Leave":
        jump Market01b
                
label BoughtNancy:
scene market01
show cageempty
show nancy06 with dissolve
mo "[name], thank you SSOO much for saving me from this horrible place!"
hide nancy06
show nancy07 with fastdissolve
mo "My, you have grown so... MANLY..."
mc "Err, yeah, I received a ton of alpha-radiations, I'm a total alpha-STUD now!"
mo "Mmh, your landlady is VERY proud of you..."
call LustPlusNancy
mc "Well, you're super-BUFF too Nancy! Wow!"
hide nancy07
show nancy08 with fastdissolve
mo "Yes, I was caught in the same alpha-radiation pocket as you I think. Oh honey, I looked for you for days, I left you for dead, I'm so sorry!"
mc "It's okay Nancy, I survived as you can see."
mc "What about your husband? Did you find him?"
hide nancy08
show nancy09 with fastdissolve
mo "Oh, he was downtown when the nuke fell on Springfield, there's no way he could have survived..."
mo "You're the MAN of the house now [name]..."
hide nancy09
show nancy10 with fastdissolve
mo "Now please [name], take this collar off me, I feel so cheap wearing it!"
mc "Sure Nancy, I've got the keys since I...err... own you."
mo "Don't talk like that please [name]..."
hide nancy10
show nancy11 with fastdissolve
mo "Oh, I feel so much lighter! Now let's leave this God-forsaken place!"
mc "Sure Nancy, I'll take you back to the compound where I live straight away!"
stop music
if alone:
    mc "Sure Nancy, I'll take you back to the compound where I live straight away! With my OWN RIG, cos I'm such a hero I actually own my own motorbike."
    mo "Oh, WOW!!!"
    jump BackHex25    
mc "Sure Nancy, I'll take you back to the compound where I live straight away!"
scene deserttown with fade
if withbe:
    show bellaout01
    be "Who is she?"
    mc "She's my landlady, that's who she is, so show some RESPECT Bella!"
    mo "Nice to meet you Bella, excuse [name], his hormones are... you know. My name is Nancy."
    hide bellaout01
    show bellaout03
    be "Don't worry about it Nancy , I'm used to IT by now. Come with us, you can sit in the spare seat at the back, we'll head back to the compound."
if withpe:
    show pennyout01
    pe "Who is that woman with you?"
    mc "She's my landlady, I rescued her, she was being held captive as a slave."
    mo "Nice to meet you Penny, my name is Nancy."
    pe "There's not much space on my motorbike, but we'll fit you somehow Nancy, hop on! We're headed back for the compound."
jump BackHex25

label MarketSpice:
$ marketseen = True
scene spicestall with dissolve
show spicegirl01
show stall
sg "Spices, spices! Food rations for the hungry with money!"
label SpiceGirlChoice:
show spicegirl01
show stall
menu:
    "What do you sell exactly?":
        sg "What it says on the menus. Some saffron and some food rations..."
        jump SpiceGirlChoice
    "I'll buy some alpha-radiated saffron. (-20 dollars)" if money >= 20:
        hide spicegirl01
        hide stall
        show spicegirl02
        show stall
        sg "There your are, 1 gram of saffron."
        $ money -= 20
        $ saffron += 1
        hide stall
        hide spicegirl02
        jump SpiceGirlChoice
    "I'll buy a NASA food ration. (-10 dollars)" if money >= 10:
        hide spicegirl01
        hide stall
        show spicegirl02
        show stall
        sg "They last forever... Or at least the half-life of the cesium that's in them..."
        $ nasafood += 1
        $ money -= 10
        hide stall
        hide spicegirl02
        jump SpiceGirlChoice
    "Leave":
        jump Market01b

label CamelSeller:
$ marketseen = True
scene market03 with dissolve
show camelgirl01
cs "You want some fine camels? Best desert camels from the far reaches of...err... the desert!"
label CamelVendorChoice:
show camelgirl01
menu:
    "I'll buy one camel please. (-20 dollars)" if money >= 20:
        hide camelgirl01
        show camelgirl02 with fastdissolve
        cs "One camel for the gentleman!"
        $ camels += 1
        $ money -= 20        
        hide camelgirl02
        jump CamelVendorChoice
    "DO you BUY camels? Cos I've got some." if camels>= 1:
        cs "Yes, for ten dollars."
        menu:
            "Sell her one camel":
                hide camelgirl01
                show camelgirl02 with fastdissolve                
                cs "That's a nice camel you HAD there. Now it's MINE!"
                $ money += 10
                $ camels -= 1
                "You now have [camels] camels."
                hide camelgirl02
                jump CamelVendorChoice
            "Sell her all your camels ([camels] camels)" if camels >= 2:
                hide camelgirl01
                show camelgirl02 with fastdissolve                
                cs "These are nice camels you HAD there. Now they're MINE!"
                $ money += (camels * 10)
                $ camels = 0
                hide camelgirl02
                jump CamelVendorChoice                
            "That's a rip-off, I'll keep my camels then.":
                cs "Whatever..."
                jump CamelVendorChoice
    "Leave":
        jump Market01b

label StripClub:
scene stripclubentrance01
show bouncer01
with dissolve
bo "Where do you think you're going, boy?"
if persistent.tipson:
    show bouncertip at tips with dissolve
    pause
    hide bouncertip            
label BouncerChoice:
menu:
    "What is this place?":
        hide bouncer01
        show bouncer04
        with fastdissolve
        if mcwarrior <= 4:            
            bo "It's a stripclub reserved for Road Warriors. So it's not for you, boy."
        if mcwarrior == 5:            
            bo "It's a stripclub. Five dollar entrance fee for Road Warriors, plus you need to have at least five more dollars on you. No loiterers allowed."
        hide bouncer04
        show bouncer01
        with fastdissolve
        jump BouncerChoice
    "I'm a Road Warriors and I've got a free entry pass. Let me in." if mcwarrior == 5 and stripfreeentry and money >= 5:
        hide bouncer01
        show bouncer02
        with fastdissolve
        bo "A refined guest of our boss, I see. Please enter."
        jump StripClub01
    "I'm a Road Warriors and I've got enough money. Let me in." if mcwarrior == 5 and money >= 5 and warriornickname:
        hide bouncer01
        show bouncer04
        with fastdissolve
        bo "What is the password?"
        if jakepassword:
            mc "\"Gazoonka.\""            
            hide bouncer04
            show bouncer02
            with fastdissolve
            bo "Please enter, \"[name] the Impaler\". It's free for a celebrity such as yourself..."
            mc "I should bloody think so!"
            jump StripClub01
        if jakepassword == False:
            mc "Err... Sesame?"
            hide bouncer04
            show bouncer03
            with fastdissolve            
            bo "WRONG answer \"[name] the Impaler\"! How did you become such a celebrity withouth knowing the Road Warriors password? Get out here!"
            jump GoRight    
    "I'm a Road Warriors and I've got enough money. Let me in." if mcwarrior == 5 and money >= 10 and warriornickname == False:
        hide bouncer01
        show bouncer04
        with fastdissolve
        bo "What is the password?"
        if jakepassword:
            mc "\"Gazoonka.\""            
            hide bouncer04
            show bouncer02
            with fastdissolve
            bo "Of course, please enter."
            $ money -= 5
            jump StripClub01
        if jakepassword == False:
            mc "Err... Sesame?"
            hide bouncer04
            show bouncer03
            with fastdissolve            
            bo "WRONG answer! You're not a True Road Warrior then! Get out here!"
            jump GoRight                                      
    "Let me through you oaf, or I'll trample you!":
        hide bouncer01
        show bouncer03
        with fastdissolve
        bo "How are you going to do that when you're knocked unconscious by my mighty fist?"
        play sound "Sounds/punch.mp3"
        scene stripclubentrance01
        show bouncer03
        with flash
        call MCInjury
        $ mcinjuredfight = True
        hide bouncer03
        show bouncer01
        with fastdissolve
        bo "I think you learnt your lesson..."
        mc "I should have guessed trying to fight an 8ft tall bouncer wasn't a good idea..."
        jump BouncerChoice       
    "Use Zara" if withza and money >= 5:
        mc "Zara, why don't you mesmerize that oaf with a belly-dance?"
        if usedzarabouncer:
            za "I already did that once, now he knows what we're up to, it's too dangerous..."
            mc "Ah, shit. Back to square one then."
            jump BouncerChoice
        za "I can try. I hope this works."        
        play music "Sounds/bellydance.mp3"
        scene stripclubentrance02
        show zaradance01
        call screen zaradancebouncer
        screen zaradancebouncer:
            modal True
            imagebutton:
                focus_mask True
                idle "Icons/nextidle.png"
                hover "Icons/nexthover.png"
                action Jump ("BouncerZaraDanceEnd")
        label BouncerZaraDanceEnd:
        scene stripclubentrance01
        show bouncer04b
        with dissolve
        bo "Ggg..."
        mc "We would like to get in..."
        hide bouncer04b
        show bouncer02
        with fastdissolve
        stop music
        bo "You... may get in... With the lovely lady..."
        mc "Oh wow, it worked, well done Zara! I'm not surprised though, you're smoking hot."
        call LustPlusZara
        za "I'm... happy I could help you [name].... *blush*"        
        $ usedzarabouncer = True
        jump StripClub01
    "Use Marnie" if withma and money >= 5:
        mc "Marnie, any chance you could use your Road Warriors credentials on that oaf?"
        if usedmarniebouncer:
            ma "After what you did last time we went inside, there's no way I'm putting my reputation on the line again for you!"
            mc "Ah, shit. Back to square one then."
            jump BouncerChoice
        ma "Actually, I used to work here. Let me do all the talking..."        
        scene stripclubentrance02
        show marnie04 
        with dissolve
        ma "Hey, Big Bob, don't you recognize me, it's Marnie!"
        scene stripclubentrance01
        show bouncer04b
        with fastdissolve
        bo "Marnie? You're back? Big Bob very happy!"
        ma "That's right, I'll catch you later, but I need to talk to Diamond, so let us in please."
        hide bouncer04b
        show bouncer02
        with fastdissolve
        stop music
        bo "Sure... Get inside... Boss will be happy to see you again!"
        mc "Oh wow, it worked, well done Marnie!"
        call LustPlusMarnie
        ma "I'm... glad I could help you [name].... *blush*"        
        $ usedmarniebouncer = True
        jump StripClub01
    "Leave" if money >=5:
        mc "I see I am not welcome here. Therefore, I shall leave!"
        hide bouncer01
        show bouncer04
        with fastdissolve        
        bo "Good riddance."
        jump GoRight
    "Leave, I don't have enough money to get into this place anyway." if money <= 4:
        mc "I see I am not welcome here. Therefore, I shall leave!"
        hide bouncer01
        show bouncer04
        with fastdissolve        
        bo "Good riddance."
        jump GoRight
        
label StripClub01:
stop music
play music "Sounds/stripclub.mp3"
if seendiamond:
    if heatherquestdone or sukyuquestdone:
        $ d2stripperchoice=renpy.random.randint(1,2)
        if d2stripperchoice == 1:
            scene stripclub01 with dissolve 
        if d2stripperchoice == 2:
            scene stripclub01h with dissolve 
        jump StripClub01b        
    if choseheather == False and heatherquestdone == False:
        scene stripclub01 with dissolve    
    else:
        scene stripclub01h with dissolve    
    jump StripClub01b
if seendiamond == False:
    if choseheather == False and heatherquestdone == False:
        scene stripclub01 with dissolve    
    else:
        scene stripclub01h with dissolve    
show warriorchief03
with dissolve
if warriornickname:
    di "Well, well, well, if it's not \"[name] the Impaler\" paying us a visit. He looks less fierce than I thought..."
    mc "Whatever lady, I'm the IMPALER! And who are you anyway?"
    hide warriorchief03
    show warriorchief01
    with fastdissolve
    di "My name is Diamond. And I'm the BOSS here. I'm ALLOWING you to stay, got it? And I've got my eyes on you, [name]..."    
    hide warriorchief01
    with dissolve
if warriornickname == False:
    di "Well, well, well, a newbie. Looks like a wannabe Road Warriors more than a REAL one to me..."
    mc "Whatever lady, I'm a TRUE warrior! And who are you anyway?"
    hide warriorchief03
    show warriorchief01
    with fastdissolve
    di "My name is Diamond. And I'm the BOSS here. I'm ALLOWING you to stay, got it? And I've got my eyes on you, [name]..."    
    hide warriorchief01
    with dissolve
$ seendiamond = True
label StripClub01b:
hide screen mcstats
hide screen calendar
call screen stripclub
screen stripclub:
    if (choseheather == False and heatherquestdone == False) or d2stripperchoice == 1:
        add "deserttown/stripclub01.jpg"
    if choseheather or d2stripperchoice == 2:
        add "v071/stripclub01h.jpg"
    modal True    
    imagebutton:
        focus_mask True
        idle "deserttown/leaveclub.png"
        hover "deserttown/leaveclub.png"
        action Jump ("LeaveStripClub")
    imagebutton:
        focus_mask True
        idle "deserttown/stripslaveridle.png"
        hover "deserttown/stripslaverhover.png"
        action Jump ("StripSlaver")
    if (choseheather == False and heatherquestdone == False) or d2stripperchoice == 1:
        imagebutton:
            focus_mask True
            idle "deserttown/stripperidle.png"
            hover "deserttown/stripperhover.png"
            action Jump ("StripShow")
    if (choseheather and sukyuquestdone == False) or d2stripperchoice == 2:
        imagebutton:
            focus_mask True
            idle "v071/stripperbidle.png"
            hover "v071/stripperbhover.png"
            action Jump ("StripShowHeather")
    imagebutton:
        focus_mask True
        idle "deserttown/gotobar.png"
        hover "deserttown/gotobar.png"
        action Jump ("StripBar")
    if stonepiece09 == False and missionge and (zaralost or (stonepiece07 == False and clearedhex16)):
        imagebutton:
            focus_mask True
            idle "Icons/stone09idle.png"
            hover "Icons/stone09hover.png"
            action Jump ("StonePiece09")

label StonePiece09:
if (choseheather == False and heatherquestdone == False) or d2stripperchoice == 1:
    scene stripclub01
else:
    scene stripclub01h  
"You found one of the missing pieces of the Stone Artefact."
$ stonepieces -= 1
window hide
show achievementgenie at posmission
$ renpy.pause(0.5, hard=True)
show text "{font=Gui/Boogaloo-Regular.ttf}{color=#ff0000}{size=30}[stonepieces]{/font}" at StonePosition
$ renpy.pause(2.0, hard=True)
hide achievementgenie
$ stonepiece09 = True
jump StripClub01b

label StripSlaver:
if (choseheather == False and heatherquestdone == False) or d2stripperchoice == 1:
    scene stripclub01
if choseheather:
    scene stripclub01h
sl "Don't disturb me while I'm shopping!"
jump StripClub01b

label StripShow:
if withbe:
    be "Oh, I see. You want to see some perverted freakshow? Then I'll head for the bar. Alcohol is allowed... and encouraged in the Church."
if withpe:
    pe "I'll be scouting the area. And I'll be watching what this girl is made of too..."
stop music
scene stripclub01
play music "Sounds/strippermusic.mp3"
"And now, ladies and gentlemen, for your viewing pleasure, the \"Queen of the Blue Oyster\",\nthe \"Mother of Melons\", the distinguished... SUK-YU DONG!"
label Stripper01:
hide nextidle
scene strippershow01 with dissolve
pause
scene strippershow02 with dissolve
pause
scene strippershow03 with dissolve
pause
scene strippershow04 with dissolve
pause
scene strippershow05 with dissolve
pause
scene strippershow06 with dissolve
mc "I can't stop myself from giving her five bucks... Those tits in my face..."
sy "Ooh, a fan I see..."
mc "SHUT UP AND TAKE MY MONEY!"
$ money -= 5
scene strippershow07 with dissolve
pause
scene strippershow08 with dissolve
pause
if strippercatchwin == False:
    scene strippershow09 with dissolve
    "And now, ladies and gentlemen, the \"Suk-Yu Dong Ping-Pong Show!\""
    jump Stripper10
if strippercatchwin:
    jump StripperDildo01

label Stripper10:
scene strippershow10 with dissolve
play sound "Sounds/plop.mp3"
pause
scene strippershow09 with dissolve
sy "Who wants to play? Catch the ball with your mouth if you can!"
mc "Me, me, me!"
sy "Be ready to catch it then!"
window hide
show angiecatch
pause
$ d3rollsball=renpy.random.randint(1,3)
if d3rollsball == 1:
    play sound "Sounds/plop.mp3"
    call screen strippercatch01
    screen strippercatch01:
        modal True
        default time_left = 0.6

        add "deserttown/ballempty.png"
        if time_left <= 0.6:
            add "deserttown/ballleft01.png"
        if time_left <= 0.4:
            add "deserttown/strippershow09.jpg"
            add "deserttown/ballempty.png"
            add "deserttown/ballleft02.png"
        if time_left <= 0.2:
            add "deserttown/strippershow09.jpg"
            add "deserttown/ballempty.png"
            add "deserttown/ballleft03.png"

        if time_left <= 0:
            timer .01 action Return
        else:
            timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)

        imagebutton:
            focus_mask True
            idle "Angie/catchleft.png"
            hover "Angie/catchleft.png"
            action Jump ("StripperCatch")
        
        bar value StaticValue(time_left, 0.5):
            xalign 0.1 yalign 0.02
            xmaximum 200 
            ymaximum 10

if d3rollsball == 2:
    play sound "Sounds/plop.mp3"
    call screen strippercatch02
    screen strippercatch02:
        modal True
        default time_left = 0.6
        
        add "deserttown/ballempty.png"
        if time_left <= 0.6:
            add "deserttown/ballcenter01.png"
        if time_left <= 0.4:
            add "deserttown/strippershow09.jpg"
            add "deserttown/ballempty.png"
            add "deserttown/ballcenter02.png"
        if time_left <= 0.2:
            add "deserttown/strippershow09.jpg"
            add "deserttown/ballempty.png"
            add "deserttown/ballcenter03.png"

        if time_left <= 0:
            timer .01 action Return
        else:
            timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)
        
        imagebutton:
            focus_mask True
            idle "Angie/catchcenter.png"
            hover "Angie/catchcenter.png"
            action Jump ("StripperCatch")

        bar value StaticValue(time_left, 0.5):
            xalign 0.1 yalign 0.02
            xmaximum 200 
            ymaximum 10

if d3rollsball == 3:
    play sound "Sounds/plop.mp3"
    call screen strippercatch03
    screen strippercatch03:
        modal True
        default time_left = 0.6

        add "deserttown/ballempty.png"
        if time_left <= 0.6:
            add "deserttown/ballright01.png"
        if time_left <= 0.4:
            add "deserttown/strippershow09.jpg"
            add "deserttown/ballempty.png"
            add "deserttown/ballright02.png"
        if time_left <= 0.2:
            add "deserttown/strippershow09.jpg"
            add "deserttown/ballempty.png"
            add "deserttown/ballright03.png"

        if time_left <= 0:
            timer .01 action Return
        else:
            timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)

        imagebutton:
            focus_mask True
            idle "Angie/catchright.png"
            hover "Angie/catchright.png"
            action Jump ("StripperCatch")
        
        bar value StaticValue(time_left, 0.5):
            xalign 0.1 yalign 0.02
            xmaximum 200 
            ymaximum 10

label StripperCatchFail:
scene strippershow09
mc "Shit, I was too slow..."
sy "Too bad, better luck next time!"
mc "Damn it. I think I need to catch this ball somehow... I'll have to come back."
jump LeaveStripClubShowEnd

label StripperCatch:
$ strippercatchwin = True
scene strippercatchball with dissolve
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)
mc "Yeah, I caught it! I win!"
sy "Congratulations. But please give me my ping pong ball back. You can stick it back inside my pussy if you want... *wink*"
scene stripperballend with dissolve
sy "Ooh, yeah, put it back DEEP inside me. AAAH!"
mc "Damn, you're deep."
scene stripperkiss with dissolve
sy "For the winner... a kiss. If you tell me your name."
call LustPlusSukYu
if warriornickname:
    mc "[name]... the IMPALER."
    sy "Oooh! I'd love to see you IMPALE ME... some day..."
    play sound "Sounds/kiss.mp3"
    sy "So come back and see me again [name] the Impaler... I have even NAUGHTIER games in store for you. *wink*"
if warriornickname == False:
    mc "[name]..."
    play sound "Sounds/kiss.mp3"
    sy "Come back and see me again [name]... I have even NAUGHTIER games in store for you. *wink*"
mc "Alright! I will."
if successprisoner == False:    
    sy "Before you go... I've got some info you might be interested in."
    mc "I'm all ears."
    sy "Trumpf Militia guards sometimes come here for... their enjoyment. I know their Forwards Ops base is at area C3."
    window hide
    show knowledgeforwardops at posmission
    $ renpy.pause(4.0, hard=True)
    hide knowledgeforwardops    
    $ knowforwardops = True
    mc "Thanks for the tip, Ms...errr.... Dong."
    sy "It's Suk-Yu. For you."    
jump LeaveStripClubShowEnd

label StripperDildo01:
scene strippershow15 with dissolve
"And now, ladies and gentlemen, the \"Suk-Yu Dong King-Kong Dong Show!\""
scene strippershow16 with dissolve
pause
scene strippershow17 with dissolve
pause
scene strippershow18 with dissolve
sy "Is there anyone in the assistance who thinks he's big enough to replace this King-sized dildo?"
mc "Me, me, me!"
sy "Oooh, you again [name]. Alright, let's see what you have... Hop onto the stage."
window hide
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)
scene stripperprefuck01 with dissolve
sy "Your young manhood certainly looks like it could be as BIG as my King-Kong dildo..."
mc "And it can get yet HARDER and BIGGER."
sy "Then GET hard so I can compare the two and see if you can replace it..."
scene stripperprefuck02 with dissolve
sy "Wow, look at that MASSIVE fuckstick. Even LARGER than my 16-inch MONSTER pussy-plugger!"
mc "Yep, that's me."
sy "Lie down on your back and I'll IMPALE MYSELF on your GIANT lovesword!"
if warriornickname:
    mc "That's why they call me \"[name] the Impaler\"..."
scene stripperprefuck03 with dissolve
sy "Let me just spread my pussylips wider... And here we go!"
label StripperFuckSlow:
hide stripperfuckfast
show stripperfuckslow
call screen stripperfuckslow01
screen stripperfuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("StripperFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("StripperFuckFast") 

label StripperFuckFast:
mc "Oh god, impale yourself on my shaft even FASTER Suk-Yu!"
if warriornickname:
    sy "Ooh, YES! I can see where you got your nickname from!"
hide stripperfuckslow
show stripperfuckfast
call screen stripperfuckfast01
screen stripperfuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("StripperFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("StripperFuckSlow") 

label StripperFuckEnd:
sy "Fill me up with cum [name]!"
scene strippercum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
sy "Ooh, that's good, I've been missing that..."
play music "Sounds/splooge01.mp3"
scene strippercum01 with fastflash
mc "AAAH! My nuts are EXPLODING!"
scene strippercum02 with dissolve
sy "You're making such a MESS..."
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
scene strippercum02 with fastflash
mc "That's cos I can't stop CUMMING! RHAAA!"
stop music
stop sound
play sound "Sounds/panting.mp3"
scene strippercum03 with dissolve
sy "I'll just have to clean your cock now... Mmmh, your seed is DELICIOUS!"
if knowdiamonds == False:
    call LustPlusSukYu
mc "Alpha-radiated cum tastes like chicken, I've been told."
scene strippercum04 with dissolve
if knowdiamonds == False:
    sy "Now that we're abone, I'b got to tell you... *lick*"
    mc "Try and speak slowly Suk-Yu... You've got a mouth full of cum..."
    sy "Biamonb's weak point is... BIAMONBS."
    mc "You mean \"diamonds\"?"
    sy "Bes..."
    mc "Interesting... Thanks for the tip, Suk-Yu."
    sy "You're belcome."
    $ knowdiamonds = True
    jump LeaveStripClubShowEnd
if exploredhex41 and chosesukyulust == False:
    sy "I'b still haven't banked you for..."
    mc "Try and speak slowly Suk-Yu... You've got a mouth full of cum..."
    sy "...for choosing me instead of bat slut Heather..."
    call LustPlusSukYu
    mc "My pleasure Suk-Yu, my pleasure...."
    $ chosesukyulust = True
if heatherharemquest and sukyuaccepted == False:
    mc "Hang on a minute, I need to ask you a favor. Can you agree to put your dispute with Heather aside and let her re-join Chief Diamond's harem?"
    sy "Bwhat's in it for ME?"
    mc "Err... You'd have more free time to do like, stuff, since you would have to share the stage with her. Plus, I want that to happen, and I'm the hero here."
    if lustsy >= 4:
        sy "But I'd lose money!"
        mc "Not if you prostitute yourself in your free time. That's even MORE money."
        sy "Fine, I'b agree. But only because your cock is so GOOD."
        $ sukyuaccepted = True
        mc "Yep, that cock always gets what it wants."
        if diamondaccepted == False:
            mc "*Now I still need to convince Chief Diamond... Probably at her harem in hex E3.*"
        if diamondaccepted:
            window hide
            show heatherquestsuccess at posmission
            $ renpy.pause(1.0, hard=True)
            pause 
            hide heatherquestsuccess
            $ heatherquestdone = True
            mc "Ah, I should go and tell Heather the good news then!"
            sy "Goob idea, I bneed to get cleaned ub."
    if lustsy <= 3:
        sy "No bway, I don't care that you're the hero, my blust for you is just not bwigh enough!"
        mc "Oh well, it was worth a try. And now I know what I need to do to get you to accept next time I come. That's some kind of progress."
jump LeaveStripClubShowEnd

label StripShowHeather:
if withbe:
    be "Oh, I see. You want to see some perverted freakshow? Then I'll head for the bar. Alcohol is allowed... and encouraged in the Church."
if withpe:
    pe "I'll be scouting the area. And I'll be watching what this girl is made of too..."
stop music
scene stripclub01h
play music "Sounds/strippermusic.mp3"
"And now, ladies and gentlemen, for your viewing pleasure, the \"New Queen of the Blue Oyster\",\nthe \"Mother of Balloons\", the young kinky... HEATHER!"
scene heatherstrip01 with dissolve
pause
scene heatherstrip02 with dissolve
pause
scene heatherstrip03 with dissolve
pause
scene heatherstrip04 with dissolve
pause
scene heatherstrip05 with dissolve
pause
scene heatherstrip06 with dissolve
mc "I can't stop myself from giving her five bucks... Those tits in my face..."
he "Ooh, my BIGGEST fan here... *wink*"
mc "SHUT UP AND TAKE MY MONEY!"
$ money -= 5
if renpy.seen_image("heatherstrip07") == False:
    "And now, ladies and gentlemen, Heather will demonstrate her acrobatic skills. With a chair!"
    play sound "Sounds/applause.mp3"
    jump HeatherFirstShow
    
$ d2rollheathershow = renpy.random.randint(1, 2)
if d2rollheathershow == 1:
    "And now, ladies and gentlemen, Heather will demonstrate her acrobatic skills. WIth a chair!"
    play sound "Sounds/applause.mp3"
    jump HeatherFirstShow
if d2rollheathershow == 2:
    "And now, ladies and gentlemen, Heather will change into... \"Leather Heather\"!"
    play sound "Sounds/applause.mp3"
    jump HeatherSecondShow
    
label HeatherFirstShow:
scene heatherstrip07 with dissolve
pause
scene heatherstrip08 with dissolve
pause
scene heatherstrip09 with dissolve
pause
scene heatherstrip10 with dissolve
pause
scene heatherstrip11 with dissolve
pause
scene heatherstrip12 with dissolve
"Thank you for watching the show and a round of applause for our new sensation... HEATHER!"
window hide
play sound "Sounds/applause.mp3"
stop music
scene heatherstripkiss with dissolve
play sound "Sounds/kiss.mp3"
he "And a special thank you to YOU. *kiss*"
stop sound
if knowdiamonds == False:
    he "Now that we're alone, I've got to tell you... Diamond's weak point is... DIAMONDS."
    mc "Interesting... Thanks for the tip, Heather. Now I can finally buy a rig. Perhaps. At least to talk Chief Diamond at the bar about it."
    he "You're welcome."
    $ knowdiamonds = True
jump LeaveStripClubShowEnd

label HeatherSecondShow:
scene heatherleather01 with dissolve
pause
scene heatherleather02 with dissolve
pause
scene heatherleather03 with dissolve
pause
scene heatherleather03b with dissolve
he "You might be wondering why I've been wearing this crotchless leather outfit... Here's the reason!"
window hide
play sound "Sounds/applause.mp3"
$ renpy.pause(2.0, hard=True)
scene heatherleather05 with dissolve
play sound "Sounds/moaning02.mp3"
pause
scene heatherleather04 with dissolve
pause
scene heatherleather06 with dissolve
play sound "Sounds/moaning03.ogg"
he "It's nice... But not BIG enough..."
pause
stop sound
scene heatherleather07 with dissolve
he "Is there anyone in the audience with a BIG cock who's ready to come and FUCK this pussy real good in front of EVERYONE?"
scene heatherleather08 with dissolve
he "What about you [name]? I KNOW you have a really HUGE cock for me... *wink*"
menu:
    "Damn right and I'll show you what it can do to a tight pussy! (-1 Church Faction)":
        he "Then whip it out and come onto the stage!"
        window hide
        play sound "Sounds/applause.mp3"
        $ renpy.pause(2.0, hard=True)
        call MinusChurch
        mc "*My immorality is duly noted by the Phallus Lord apparently... But screw it, and let's screw Heather!*"
        jump LeatherPreFuck01
    "Not today Heather, I'm just enjoying watching the show...":
        he "That's disappointing... Without you, the show is OVER!"
        stop music
        jump LeaveStripClubShowEnd

label LeatherPreFuck01:
stop music
scene heatherleatherprefuck01 with dissolve
play sound "Sounds/audiencegasp.mp3"
he "Hear them gasp [name]? That's cos they are MIGHTY impressed by that hard horsecock of yours... Bring it over..."
scene heatherleatherprefuck02 with dissolve
play sound "Sounds/applause.mp3"
he "I'm going to have a LOT of fun coaxing a GIANT load out of those boulders... You have a lot of cum for me [name]?"
mc "Fuck yeah, plenty to satisfy you, Heather!"
he "Just imagine the people's faces in this room when they see your cum-missile unloading its mighty load all over poor little me..."
mc "You're... such a TEASE, Heather!"
scene heatherleatherprefuck03 with dissolve
he "You want me to stop teasing you? Then come and fuck this pussy real HARD, donkey-dicked boy!"

play music "Sounds/barbarasex.mp3"
label LeatherFuckSlow:
hide leatherfuckfast
show leatherfuckslow
call screen leatherfuckslow01
screen leatherfuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LeatherFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LeatherFuckFast") 

label LeatherFuckFast:
he "Aaah, this is so HOT, I LOVE getting fucked by a horse-hung guy in front of everyone like that!"
mc "You like that dick you dirty little stripper, hey?"
he "Ooh, yeah, it's so good DEEP in my pussy like that. Fuck me FASTER, show these people what you're made of, STUD!"
hide leatherfuckslow
show leatherfuckfast
call screen leatherfuckfast01
screen leatherfuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LeatherFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LeatherFuckSlow") 

label LeatherFuckEnd:
he "Are you going to blow your load [name]? I want you to pump it inside my pussy... To OVERFILLING!"
mc "Aah, jut a sec...."
stop music
scene heatherleathercum01 with dissolve
play music "Sounds/splooge02.mp3"
play sound "v07/creampie.mp3"
mc "Oh, FUCK!"
with fastflash
he "BLAST THAT NASTY TEENAGE SPUNK! AAAAH!"
scene heatherleathercum02 with dissolve
mc "RHAAA, CAN'T STOP CUMMING!"
with fastflash
he "I'm getting pumped full of cum in public, OOH-UUUHHH!"
stop music
stop sound
scene heatherleathercum03 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Let them see these cumshots too then, FU-UUU-CCCKKK!"
with fastflash
he "You're STILL spewing? This is so NASTY!"
scene heatherleathercum04 with dissolve
play sound "Sounds/applause.mp3"
he "Oooh, [name], you made such a nasty mess... In front of all these people watching us FUCK... It's sssoo kinky..."
mc "I had to show them what I'm made of, just like you said..."
he "You've proven to them than you are a true Road Warrior STALLION!"
call PlusWarrior
if warriornickname == False and mcwarrior == 5:
    he "And someone worthy of a WARRIOR nickname. How about \"[name] the Impaler!\"?"
    window hide
    show mcwarriornickname at posmission
    play sound "Sounds/skill.mp3"
    $ renpy.pause(2.0, hard=True)
    $ warriornickname = True
    mc "Sounds perfectly appropriate!"
    hide mcwarriornickname
scene heatherleathercum05 with dissolve
play sound "Sounds/sucking.mp3"
he "And you've reminded me  how TASTY your spunk is... *slurp*"
if heatherleatherlust == False:
    call LustPlusHeather
    $ heatherleatherlust = True
he "Now off you go, I have to get myself ready for my NEXT show! *wink*"
if sukyuharemquest and heatheraccepted == False:
    mc "Hang on a minute, I need to ask you a favor. Chief Diamond is ready to take Suk-Yu back into her harem, but she wants YOU to agree to it too."
    he "What's in it for ME?"
    mc "Err... You'd have more free time to do like, stuff, since you would have to share the stage with her. Plus, I want that to happen, and I'm the hero here."
    if lusthe >= 4:
        he "But I'd lose money!"
        mc "Not if you prostitute yourself in your free time. That's even MORE money."
        he "Fine, I'll agree. But only because your cock is so GOOD."
        mc "Yep, that cock always gets what it wants."
        $ heatheraccepted = True         
        if diamondaccepted == False:
            mc "*Now I still need to convince Chief Diamond... Probably at her harem in hex E3.*"
        if diamondaccepted:
            window hide
            show sukyuquestsuccess at posmission
            $ renpy.pause(1.0, hard=True)
            pause 
            hide sukyuquestsuccess
            $ sukyuquestdone = True
            mc "Ah, I should go and tell Suk-Yu the good news then!"
            he "Yeah, you do that [name]. WHile I get cleaned up for my next show..."
    if lusthe <= 3:
        he "No way, I don't care that you're the hero, my lust for you is just not high enough!"
        mc "Oh well, it was worth a try. And now I know what I need to do to get you to accept next time I come. That's some kind of progress."
jump LeaveStripClubShowEnd

label StripBar:
scene stripbar01
show warriorchief03
with dissolve
di "What are you doing here? If you come to the bar, you MUST consume. Have a 5 dollar cocktail or I'll have my girls cut your throat!"
mc "Alright, alright!"
$ money -= 5
hide warriorchief03
show warriorchief01
with fastdissolve

label DiamondDialogue01:
di "If you're thinking of ever becoming the boss here, think again! My authority is TOTAL."
if persistent.tipson:
    show diamondtip at tips with dissolve
    pause
    hide diamondtip            
label DiamondDialogue:
menu:
    "That was never my intentions." if spokediamond01 == False:
        hide warriorchief01
        show warriorchief04
        with fastdissolve
        di "It better not be. I'll kill you before you even get the chance of thinking about it..."
        hide warriorchief04
        show warriorchief01 
        with fastdissolve
        $ spokediamond01 = True
        jump DiamondDialogue
    "So I see you've replaced Suk-Yu with Heather. Wise choice. You listened to me." if choseheather and tolddiamondchoseheather == False:
        $ tolddiamondchoseheather = True
        hide warriorchief01
        show warriorchief04
        with fastdissolve
        di "You want a medal or something? Be glad I didn't ENSLAVE you as well!"
        hide warriorchief04
        show warriorchief01 
        with fastdissolve
        jump DiamondDialogue
    "So. Your name. Diamond. Is that because you like diamonds?":
        hide warriorchief01
        show warriorchief02
        with fastdissolve
        di "What's it to you, poor boy? I ain't telling you jack about me!"
        hide warriorchief02
        show warriorchief01 
        with fastdissolve
        jump DiamondDialogue
    "I might have come across some diamonds... LOTS of diamonds." if knowdiamonds and totalgems >= 1:
        hide warriorchief01
        show warriorchief04
        with fastdissolve
        di "Really?... That might interest me then. What's your haul and what do you want in return?"
        mc "You're the head of the local Road Warriors, you must have some spare rigs. I want one."
        if mcwarrior <= 4:            
            hide warriorchief04
            show warriorchief01 
            with fastdissolve
            di "You ain't no Road Warrior! I'm not selling a road bike to no weasel from another faction! Come back when you've joined the CORRECT faction."
            jump DiamondDialogue
        if mcwarrior == 5 and totalgems == 1:            
            hide warriorchief04
            show warriorchief03 
            with fastdissolve
            di "Let me see your haul then..."
            hide warriorchief03
            show warriorchief02 
            with fastdissolve
            di "PATHETIC! Not nearly enough diamonds to be worth my while! Come back when you have found MORE of them."            
            jump DiamondDialogue
        if mcwarrior == 5 and totalgems >= 2:            
            hide warriorchief04
            show warriorchief03 
            with fastdissolve
            di "Let me see your haul then..."
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
            if gem:
                $ gem = False
            if hulkgem:
                $ hulkgem = False
            if aliendiamonds:
                $ aliendiamonds = False
            $ stripfreeentry = True
            $ mcbike = True
            $ mcbikebought = True
            jump BackHex25
    "Leave":
        mc "It was a pleasure talking to you."
        di "NOT likewise."
        jump LeaveStripClubShowEnd

label LeaveStripClub:
mc "I'm done here, this place is too depraved..."
stop music
jump GoRight

label LeaveStripClubShowEnd:
show screen calendar
show screen mcstats
stop music
play music "Sounds/stripclub.mp3"
if withbe:
    if choseheather == False:
        scene stripclub01
        show bella01
        with fade
    if choseheather:
        scene stripclub01h
        show bella01
        with fade
    mc "It's getting late Bella, let's go back to the compound."
    be "Finally, you're done..."
if withpe:
    if choseheather == False:
        scene stripclub01
        show pennyfriendly01
        with fade
    if choseheather:
        scene stripclub01h
        show pennyfriendly01
        with fade
    mc "It's getting late Penny, let's go back to the compound."    
    pe "Alright, fun has to end sometimes..."
if alone:
     if choseheather == False:
        scene stripclub01
        with fade
     if choseheather:
        scene stripclub01h
        with fade
     mc "It's getting late, better get back to the compound."
stop music
jump BackHex25

label BackHex25:
$ period += 1
scene command01
show lena01
with fade
le "So, what do you have to report about area C5, scouts?"
if mcbikebought:
    mc "I bought my own rig! Now I can scout on my own like a TRUE Road Warrior!"
    hide lena01
    show lena05
    with fastdissolve
    le "I fail to see how that will help in your missions considering what a blabbering fool you are sometimes..."
    if withbe:
        be "I can vouch for that statement, Chief Lena!"
    if withpe:
        pe "I can vouch for that statement, Chief Lena!"
    mc "Bella and Penny can go scouting somewhere else while I explore the Great Wilderness in search of Trumpf City, Chief!"
    hide lena05
    show lena03
    with fastdissolve
    le "Alright, alright. But YOU pay for its maintenance in the workshop. that'll cost you 5$ a week or your rig will be immobilized."
    mc "I'll bear that in mind. Got find me some more MONEY then."
    le "Scouts dismissed!"
    hide lena03 with dissolve
    $ mcbikebought = False
    jump LeaveCommand
if boughtmom and momcompound == False:
    $ momcompound = True
    mc "I found my landlady, she survived!"
    hide lena01
    show lena03
    with fastdissolve
    le "What? So she wasn't killed by President-for-Life Trumpf then?"
    mc "Nope. And I brought her back here, cos she was a slave and she has nowhere to live."
    window hide
    show lena03 at midright with move
    show nancyinside01 at midleft with moveinleft
    hide lena03
    show lena02 at midright
    le "Ah. Err, that's fantastic! For YOU."
    mc "I'm sure you can find her a job so she can be useful to the compound. I know she's a great cook!"
    le "Sure... She can be a cook if you insist then. We should also find her some clothes... Cos she can't walk around the compound like that."
    hide nancyinside01
    show nancyinside02 at midleft
    mo "Oh thank you so much! I won't disappoint you I promise! [name] told me so many nice things about this place and...you!"
    hide lena02
    show lenapensive at midright
    le "Well, we do have some spare clothes lying around... Suki will show you."
    hide nancyinside02 with moveoutleft
    hide lenapensive
    show lena01 at midright
    le "She'll have to sleep in bunks though, we cannot spare a luxury room for a woman, even if she is your ex-landlady..."
    show nancycountry01 at midleft with moveinleft
    mc "These clothes look great on you Nancy!"
    le "Well, I'll let you show her around, I have to go back to WORK, managing a compound with yet ANOTHER person in it."
    mc "Come with me, I'll show you my room, it's top ace!"
    scene bedroom01 with fade
    show nancycountry02 with moveinright
    mo "Oh [name], I'm so proud of you, you're becoming a HERO in this compound to have such a BIG bedroom!"
    mc "Yeah, I AM the HERO actually Nancy!"
    scene bedroom03b
    show nancycountry03 with fastdissolve
    mo "I sure would LOVE to have such a comfy bed... Especially after having slept in a cage for MONTHS..."
    mc "Well, you're always welcome to come and sleep here Nancy, and I'll sleep... on the floor."
    mo "Oh, I recognize my SWEET SWEET man!"
    mc "Come, I'll show you the gym where I train to get even STRONGER!"
    mo "I can't wait!"
    scene machine01 with fade
    show nancycountry02 at midright with dissolve
    mc "I use these weights. They're over 2000lbs and I can do hundreds of reps with them."
    mo "Oh my God, you are sssooo STRONG!"
    mc "I wonder how much YOU can benchpress..."
    hide nancycountry02
    show nancycountry01 at midright with fastdissolve
    mo "I don't know either, I never had the CHANCE to try... Maybe I'll come and use this gym in my spare time!"
    mc "(Fuck yeah... So I can have a SEX dream sequence in the locker room with her...)"
    if mcinjuredtaser:
        mc "I think I need to go to the medbay to check on my injury, I'll let you discover your new job in the kitchen...yourself. Cos there's no useless eating sequences in this game."
        mo "Of course [name], I think I can handle myself. Thanks a bunch for being such a SWEET boy to your landlady! And recover from that nasty injury fast!"
        jump Medbay
    mc "I think I need to go back to the command center now, I'll let you discover your new job in the kitchen...yourself. Cos there's no useless eating sequences in this game."
    mo "Of course [name], I think I can handle myself. Thanks a bunch for being such a SWEET boy to your landlady!"
    jump LeaveCommand
if mctattoo:
    mc "I report that I got a tattoo. Pretty neat, hey?"
    $ mctattoo = False
    hide lena01
    show lena10
    with fastdissolve
    le "Oh neat, really? You're supposed to get VALUABLE INTEL from these scouting missions, not a frigging TATTOO!"
    mc "Well, it was part of my infiltration tactic. I learnt that...err... there are a lot of Road Warriors in that... Road Warrior town."
    hide lena10
    show lena03
    with fastdissolve
    le "Well, thank you Captain Obvious! DISMISSED!"
    hide lena03
    jump LeaveCommand
if scoutinbath:
    $ scoutinbath = False
    mc "We infiltrated a hammam."
    hide lena01
    show lena03
    with fastdissolve
    le "Yeah, AND?..."
    mc "It was... bigly wet. And sulfuric."
    hide lena03
    show lena10
    with fastdissolve
    le "Well, that is FASCINATING. Scouts DISMISSED!"
    hide lena10
    jump LeaveCommand
if marketseen:
    mc "I went to the market."
    hide lena01
    show lena10
    with fastdissolve
    le "And now you'll stay at home. Scouts DISMISSED!"
    hide lena10
    jump LeaveCommand
if knowforwardops and toldforwardops == False:
    mc "I learnt where the Trumpf Militia Forward Ops base is located, Chief! It's area C3."
    hide lena01
    show lena07
    with fastdissolve
    le "Finally, some good news! Well done, scouts. I'll think of a strategy to deal with this information..."
    le "Dismissed!"
    hide lena07
    $ toldforwardops = True
    jump LeaveCommand
mc "We went into Desert Town. It turns out it's being run by Road Warriors."
hide lena01
show lena03
with fastdissolve
le "So Road Warriors are becoming more and more sedentary... You'll have to be extra careful from now in that town, understood?"
mc "Roger that Chief!"
jump LeaveCommand
    
    
    