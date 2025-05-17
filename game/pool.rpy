label Pool:
show screen mcstats
show screen calendar
scene pool01 with dissolve
play music "Sounds/pool.mp3"
$ loc = "pool"
$ seenpool = True
label Pool01:    
call screen pool01
screen pool01:
    modal True    
    imagebutton:
        focus_mask True
        idle "Icons/exitidle.png"
        hover "Icons/exithover.png"
        action Jump ("LeavePool")
    if zaraharem:
        imagebutton:
            focus_mask True
            idle "Pool/poolzaraidle.png"
            hover "Pool/poolzarahover.png"
            action Jump ("ZaraPool")
    if momcompound and pregmostart <= 3:
        if d2rollnancypool == 1 and missionnancybikinidone == False:
            imagebutton:
                focus_mask True
                idle "Pool/poolnancyidle.png"
                hover "Pool/poolnancyhover.png"
                action Jump ("NancyPool")
        if d2rollnancypool == 1 and missionnancybikinidone:
            imagebutton:
                focus_mask True
                idle "Pool/poolnancy02idle.png"
                hover "Pool/poolnancy02hover.png"
                action Jump ("NancyPool")
    if d6rollpool == 1:
        imagebutton:
            focus_mask True
            idle "Pool/poolbellaidle.png"
            hover "Pool/poolbellahover.png"
            action Jump ("BellaPool")    
    if d6rollpool == 2 and preggwstart <= 3:
        imagebutton:
            focus_mask True
            idle "Pool/poolgwenidle.png"
            hover "Pool/poolgwenhover.png"
            action Jump ("GwenPool")    
    if d6rollpool == 2 and preggw and preggwstart >= 4:
        imagebutton:
            focus_mask True
            idle "v07/poolgwen02idle.png"
            hover "v07/poolgwen02hover.png"
            action Jump ("GwenPool04")    
    if d6rollpool == 3 and pregamstart <= 3:
        imagebutton:
            focus_mask True
            idle "Pool/poolamyidle.png"
            hover "Pool/poolamyhover.png"
            action Jump ("AmyPool")    
    if d6rollpool == 4:
        imagebutton:
            focus_mask True
            idle "Pool/poolbarbaraidle.png"
            hover "Pool/poolbarbarahover.png"
            action Jump ("BarbaraPool")    
    if d6rollpool == 5:
        imagebutton:
            focus_mask True
            idle "Pool/poolpennyidle.png"
            hover "Pool/poolpennyhover.png"
            action Jump ("PennyPool")    
    if d6rollpool == 6:
        imagebutton:
            focus_mask True
            idle "Pool/pooldebraidle.png"
            hover "Pool/pooldebrahover.png"
            action Jump ("DebraPool")

label NancyPool:
$ poolmo += 1
if poolmo == 1:
    scene pool03
    show mompool01
    with dissolve
    mo "Hi sweetie!"
    mc "Hi Nancy! What are you doing here, aren't you supposed to be working for the compound."
    mo "Well, I'm allowed some time off from time to time. And since.... I still have this awful bikini from my time as a slave, I sometimes come here."
    hide mompool01
    show mompool01a
    with fastdissolve
    mo "But I prefer it when I'm alone, I'm so ashamed to be wearing this in front of others, especially you, my sweet tenant..."
    mc "Maybe I could find you a better bikini then Nancy."
    mo "Oh, that would be wonderful [name]!"
    window hide
    show missionbikini at posmission
    $ renpy.pause(4.0, hard=True)
    hide missionbikini
    $ missionnancybikini = True
    mc "Alright, I'll get right on it. I'll go for a swim now."
    jump PoolOut
if poolmo >= 2 and missionnancybikinidone == False:
    scene pool03
    show mompool01
    with dissolve
    mo "Hi sweetie!"
    mc "Hi Nancy! Nice to see you here again... In that hot bikini."
    hide mompool01
    show mompool01a
    with fastdissolve
    mo "Oh, don't say that sweetie, you know I don't like it... It reminds me of my time as a slave."
    if bikini01:
        mc "Well, guess what? I found you a new bikini Nancy!"
        hide mompool01a
        show mompool02
        with fastdissolve
        mo "Really? Oh, you are such a sweet ex-tenant of mine!"
        mc "Here it is, try it on, I'm sure you'll like it."
        hide mompool02
        show mompool03
        with fastdissolve
        mo "Alright, I'll turn around while I do it, out of modesty... Don't watch, sweetie!"
        hide mompool03
        show mompool04
        with fastdissolve
        mc "Sure, that never crossed my mind..."
        scene pool03 blurred
        show mompool05
        with fastdissolve
        mc "(Never ever... Fuck me, what an ass...)"
        scene pool03
        show mompool06
        with dissolve
        mo "There, how do I look, does it fit your old landlady well?"
        mc "Let me have a closer look..."
        scene pool03 blurred
        show mompool07
        with fastdissolve
        mc "Yes, the upper line is perfectly fitting your...err... huge knockers... Let's see the back shall we?"
        hide mompool07
        show mompool08
        with dissolve
        mc "And the bottom fits snugly between that sumptuous ass of yours... I'd say it's a perfect fit Nancy!"
        scene pool03
        show mompool06
        with dissolve
        mo "Thank you so much [name] for that.... And your supportive feedback... I'll go back to my room to have a look myself in the mirror."
        call LustPlusNancy
        $ missionnancybikinidone = True
        mc "I'll go for a swim then, see you another time Nancy!"
        jump PoolOut        
    if bikini01 == False:
        mc "I haven't found anything for you yet, but I'm working on it, I promise!"
        mo "Please hurry up, wearing this bikini is really starting to get to me... *sniff*"
        mo "And leave me alone, I... don't want my ex-tenant to see me like this...;"
        mc "Alright, I'll go for a swim and think of a way of getting you a brand new HOT bikini Nancy!"
        jump PoolOut
if poolmo >= 2 and missionnancybikinidone:
    scene pool03
    show mompool06
    with dissolve
    mo "Hi sweetie!"
    mc "Hi Nancy! Nice to see you here again... In that hot NEW bikini."
    hide mompool06
    show mompool09
    with fastdissolve
    mo "I REALLY like it a LOT. It feels so comfortable and SEXY at the same time."
    mc "SEXY is definitely the word I would use to describe it. ON YOU."
    if haremmo:
        mo "And I like feeling SEXY for my harem Master! *wink*"
        mc "Damn right! Turn round and show me that ass again, I'm getting a HARDON just looking at you..."
        hide mompool09
        show mompool08
        with fastdissolve
        mo "Like that my sweet tenant?"
        mc "Fuck yeah! I'm going to bang that ass later this week like it's never been banged! Phew, I need to go for a swim to cool off now..."
        mo "Don't cool off TOO much! *wink*"
        menu:
            "You know what? I 'm so fucking horny I'm gonna bang you right NOW!" if nancypoolbanged == False:
                jump NancyPoolBang
            "I've got an idea to make your Marvel costume painless to wear." if debranancyagree and debranancylab == False:
                hide mompool08 
                show mompool06
                with fastdissolve
                mo "But... Why would I need to wear this cosplay costume anyway, sweetie pie?"
                mc "Well, you never know. The Avengers must be ready at all times!"
                hide mompool06 
                show mompool09
                with fastdissolve
                mo "Well... I suppose, if it's REALLY necessary..."
                mc "I got a deal with Debra to try her alpha-ray machine on you in reverse polarity."
                hide mompool09 
                show mompool06
                with fastdissolve
                mo "Reverse polarity? What does that mean?"
                mc "Something to do with quarks and bosons and shit. Sciency stuff. You wouldn't understand, but it WILL WORK, I promise! Let's go!"
                mo "Su...Sure sweetie pie. Let me get my costume and I'll meet you there."
                jump DebraNancyScience
            "I need you to become Captain Marvel for a day. The New Avengers must defeat Sean Insannity!" if period == 1 and debranancylab and missionhannity and missionhannitydone == False:
                hide mompool08 
                show mompool06
                with fastdissolve
                mo "But.. I'm not REALLY a superhero, sweetie pie."
                mc "It's all in your mind Nancy. Once you wear the costume, you will BECOME Captain Marvel!"
                hide mompool06 
                show mompool09
                with fastdissolve
                mo "Well... I suppose, if you think so..."
                mc "I'm sure of it! Let's go and meet the Black Widow!"
                mo "Su...Sure sweetie pie. Let me get my costume first, I wouldn't want to meet her in a bikini."
                mc "And I'll get mine!"
                label NewAvengersPremission:
                scene command02
                show lena01
                show commandtable
                with fade
                le "Yes? Why are you wearing a silly Captain America costume?"
                mc "I'm ready, with the New Avengers to go and kick Sean Insannity's ass and get inside Trumpf City, Chief!"
                hide lena01
                show lena07
                with fastdissolve
                le "Ah, finally! Although I question your silly strategy, I will give you the benefit of the doubt."
                hide lena07
                show lena06
                with fastdissolve
                $ d2rollwith = renpy.random.randint(1, 2)
                if d2rollwith == 1:
                    le "And Bella will go with you to make sure you don't screw up this time."
                    $ withbe = True
                if d2rollwith == 2:
                    le "And Penny will go with you to make sure you don't screw up this time."
                    $ withpe = True                
                $ withmarvel = True
                jump Explore
            "Oh, I'll be ready for later this week, don't worry!":
                jump PoolOut
    if haremmo == False and lustmo <= 3:
        hide mompool09
        show mompool06
        with fastdissolve
        mo "You shouldn't be so BOLD, [name]. People might overhear you... Go back into the pool and cool off, you seem a bit... too excited today."
        mc "(Damn, I blew it. Her lust is just not high enough it seems.)"
        if pendulum and showedpendulum == False:
            mc "(But maybe I could hypnotize her with my pendulum and change that...)"        
            menu:
                "I'd like to show you something first (hypnotize her, +1 lust)" if pendulum and showedpendulum == False:
                    mo "What is it?"
                    call UsePendulum
                    hide mompool06
                    show mompool09
                    with fastdissolve
                    mo "Ooh, I feel... so SEXY. For YOU."
                    call LustPlusNancy
                    $ showedpendulum = True
                    mc "You definitely are, you definitely are. I'm off to go for a swim now, enjoy the rest of your day Nancy!"
                    mo "Bye sweetie!"
                    jump PoolOut
                "I've got an idea to make your Marvel costume painless to wear." if debranancyagree and debranancylab == False:
                    mo "But... Why would I need to wear this cosplay costume anyway, sweetie pie?"
                    mc "Well, you never know. The Avengers must be ready at all times!"
                    hide mompool06 
                    show mompool09
                    with fastdissolve
                    mo "Well... I suppose, if it's REALLY necessary..."
                    mc "I got a deal with Debra to try her alpha-ray machine on you in reverse polarity."
                    hide mompool09 
                    show mompool06
                    with fastdissolve
                    mo "Reverse polarity? What does that mean?"
                    mc "Something to do with quarks and bosons and shit. Sciency stuff. You wouldn't understand, but it WILL WORK, I promise! Let's go!"
                    mo "Su...Sure sweetie pie. Let me get my costume and I'll meet you there."
                    jump DebraNancyScience
                "Don't bother just now and go for a swim":
                        jump PoolOut
        jump PoolOut
    if haremmo == False and lustmo >= 4:
        mo "That's very BOLD of you, [name]. Just because I'm wearing a bikini that barely covers my HUGE tits... *wink*"
        menu:
            "I've got an idea to make your Marvel costume painless to wear." if debranancyagree and debranancylab == False:
                hide mompool09
                show mompool06
                with fastdissolve
                mo "But... Why would I need to wear this cosplay costume anyway, sweetie pie?"
                mc "Well, you never know. The Avengers must be ready at all times!"
                hide mompool06 
                show mompool09
                with fastdissolve
                mo "Well... I suppose, if it's REALLY necessary..."
                mc "I got a deal with Debra to try her alpha-ray machine on you in reverse polarity."
                hide mompool09 
                show mompool06
                with fastdissolve
                mo "Reverse polarity? What does that mean?"
                mc "Something to do with quarks and bosons and shit. Sciency stuff. You wouldn't understand, but it WILL WORK, I promise! Let's go!"
                mo "Su...Sure sweetie pie. Let me get my costume and I'll meet you there."
                jump DebraNancyScience
            "I think it's time that you... joined my harem, Nancy." if momharem == False and girlsinharem <= 5:
                hide mompool09
                show mompool06
                with fastdissolve
                mo "Really? You want your old landlady in your HAREM?"
                mc "Sure, I mean, you're still young and...err... fertile."
                mo "We probably shouldn't be telling anyone about it, but I'll gladly be your... harem girl, my sweet young man!"
                $ haremmo = True
                $ momharem = True
                $ girlsinharem += 1
                window hide
                show haremnancy at plus
                $ renpy.pause(2.0, hard=True)
                hide haremnancy
                mc "Then I'll see you... discreetly later on Nancy!"
                hide mompool06
                show mompool08
                with fastdissolve
                mo "Of course [name]! I can't wait to meet you \"in private\"."
                mc "And I'll go and take a swim to get squeaky-clean for our future roomies romp!"
                jump PoolOut            
            "I think it's time that you... re-joined my harem, Nancy." if momharem and girlsinharem <= 5 and momdismissed == False:
                hide mompool09
                show mompool06
                with fastdissolve
                mo "Really? You want your old landlady back in your HAREM?"
                mc "Sure, I already regret having let you go once, I won't make that same mistake again!"
                mo "Mmh, so this new bikini really did the trick then, hey, my sweet ex-tenant? I'll gladly accept, but let's not tell anyone please."
                $ haremmo = True
                $ momharem = True
                $ girlsinharem += 1
                window hide
                show haremnancy at plus
                $ renpy.pause(2.0, hard=True)
                hide haremnancy
                mc "Then I'll see you... discreetly later on Nancy!"
                hide mompool06
                show mompool08
                with fastdissolve
                mo "Of course [name]! I can't wait to meet you \"in private\"."
                mc "And I'll go and take a swim to get squeaky-clean for our future roomies romp!"
                jump PoolOut            
            "I'm glad you like it as much as I do...":
                mo "I do... But it's mine now, so no touching, naughty boy!"
                mc "You're a tease, Nancy. I'll tease you by going for a swim in my tight spandex..."
                mo "Ooh, you're such a NAUGHTY tenant!"
                jump PoolOut  

label NancyPoolBang:
$ nancypoolbanged = True
$ weekfuckedmom = True
play music "v07/datemusic.mp3"
hide mompool08
show mompool09
with fastdissolve
mo "Right here? With the risk of people walking in on us?"
window hide
show mompool09 at right with move
show mcmompool10 at farleft with moveinleft
mc "The girl who was here with us just left... We have time for a quickie."
hide mompool09
show mompool10 at right
with fastdissolve
mo "Oh, my sweet tenant, you're such a naughty boy!"
hide mompool10
hide mcmompool10
show mcmompool11 
with dissolve
mc "So what do you say?"
mo "I... I don't know... I am kind of horny too... seeing you like this!"
scene pool03 blurred
show mcmompool12 
with dissolve
mc "Then get out of that tight bikini bottom and I'll give you a good pounding right away!"
mo "Ooooh, you're... so MANLY! I just want to kiss my studly landboy first..."
play sound "Sounds/kiss.mp3"
hide mcmompool12
show mcmompool13 
with dissolve
mc "I can't wait any longer, I NEED to fuck that tight ass of yours, Nancy!"
mo "My ass? Oh God, this is so dirty, anyone could just walk in on us and see me with your giant teenage cock stretching my poor little ass..."
mc "I guess you'll just have to try and keep the moaning down..."
hide mcmompool13
show mcmompool14a 
with dissolve
mc "Can you feel my dong slapping against your thighs, Nancy?"
window hide
hide mcmompool14a
show mcmompool14b
with fastdissolve
play sound "Sounds/slap.mp3"
hide mcmompool14b
show mcmompool14a
with fastdissolve
mo "Oh, honey, it's so HEAVY and BRUTAL! You're going to HAMMER it into me, aren't you?"
window hide
hide mcmompool14a
show mcmompool14b
with fastdissolve
play sound "Sounds/slap.mp3"
mc "Fuck yeah, so let's do it standing up, I just can't wait any longer..."
hide mcmompool14b
play music "Sounds/womansex01.mp3"
label NancyPoolSlow:
hide nancypoolfast
show nancypoolslow
call screen nancypoolslow01
screen nancypoolslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("NancyPoolEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("NancyPoolFast") 

label NancyPoolFast:
mc "I'm gonna make you moan louder now... By POUNDING IT FASTER!"
mo "Oh, sweetie pie, someone might hear us if you do th..."
play music "Sounds/womansex02.mp3"
hide nancypoolslow
show nancypoolfast
call screen nancypoolfast01
screen nancypoolfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("NancyPoolEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("NancyPoolSlow") 

label NancyPoolEnd:
mc "That's it, I'm close, Nancy..."
mo "Come inside me [name], I want to feel your warm sperm ERUPTING in my little pussy!"
stop music
hide nancypoolfast
hide nancypoolslow
show mcmompoolfuckcum01
with dissolve
play music "Sounds/splooge02.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH, GODDAMIT? this is sssooo GOOOD!"
window hide
with fastflash
mc "My cock is EXPLODING, that pussy is just the BEST!"
scene pool05 blurred
show mcmompoolfuckcum02
with dissolve
mo "YES! Keep pumping that seed, sweetie pie!"
window hide
with fastflash
mc "I'm gonna FILL YOU UP, AAHHH!"
scene pool03 blurred
show mcmompoolfuckcum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mo "My belly... It's SWELLING with your MONSTERLOAD!"
window hide
with fastflash
mc "That's cos you're making me cum BIG TIME, RHAAA!"
stop music
scene pool06 blurred
show mcmompoolfuckcum04
with dissolve
play sound "Sounds/splooge01.mp3"
mo "You came ssooo MUCH, honey pot... I hope nobody walks in on us with your seed POURING out of my stretched ass like that..."
if nancylustpool == False:
    $ nancylustpool = True
    call LustPlusNancy
mc "It does look rather lewd I agree. I think I'd better go for a swim to exonerate myself."
mo "And I'll just... wait for it to stop pumping out and then clean up the mess..."
jump PoolOut

label ZaraPool:
$ poolza += 1    
label ZaraPool01:
scene poolzara01 with dissolve
if poolza == 1:
    za "Oh, hello [name]! You found my secret hiding place..."
if poolza >= 2:
    za "Oh, hello [name]! Are you here to relax or to try and get some lust points?"
    mc "Hopefully, both! Although I don't need to get YOUR lust points up cos I bought you for some camels."
    za "I am grateful to you for giving me a better life, [name]."
za "This is where I hang out in my free time..."   
if haremza and poolza == 1:
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
    jump PoolOut
if haremza == False and poolza == 1:
    za "...Since I haven't been brutally fisted in a while, I can enjoy the water jets on my back and relax a bit."
    menu:
        "About that. I think it's for you re-join my harem." if haremza == False and girlsinharem <= 5 and money >= 5 and zaradismissed == False:
            scene poolzara02 with dissolve
            za "Do you have money now? I have my needs..."
            mc "Yeah, I'm loaded, so I'll take good care of you."
            call LustPlusZara
            $ haremza = True
            $ zaraharem = True
            $ girlsinharem += 1
            window hide
            show haremzara at plus
            $ renpy.pause(2.0, hard=True)
            hide haremzara
            $ haremzararejoined = True
            mc "Now that's better, I wouldn't want to lose such a beautiful girl..."
            scene poolzara03 with dissolve
            za "I'll see you some evening this week I guess... I'd better go and do lots of kegels to prep my pussy then... Bye [name]!"
            mc "That would be advisable. I DO plan some brutal fisting indeed... (what a fine ass...)"
            mc "Oh well, I might as well go for a swim since she's leaving."
            jump PoolOut            
        "Enjoy it while it lasts then, Zara. You'll be begging me to get you back into my harem one day....":
            scene poolzara02 with dissolve
            za "As long as you have money to cover my needs, I'm willing, [name]...."
            mc "Ah, yes. Money. I need more of that. You girls are expensive."
            scene poolzara03 with dissolve
            za "I'll see you around [name]. And I'll enjoy my pussy being normal-sized while it lasts..."
            mc "Oh well, I might as well go for a swim since she's leaving."
            jump PoolOut            

if haremza and pregza >= 3:
    za "I can still swim a bit even though I'm pregnant... The baby seems to be enjoying it too."
    mc "That's good to know. I see I can't really tell if you're pregnant or not cos your belly is under the water."
    scene poolzara02 with dissolve
    za "It's on purpose so the dev doesn't have to do new renders of me being pregnant."
    mc "That sounds kind of LAZY."
    za "I should go now, don't want the chlorine to enter my womb and hurt the baby."
    scene poolzara03 with dissolve
    za "Bye [name]!"
    mc "Bye Zara. (What a fine ass...)"
    mc "Oh well, I might as well go for a swim since she's leaving."
    jump PoolOut    

if haremza and poolza >= 2:
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
    jump PoolOut
if haremza == False and poolza >= 2:
    za "...Since I haven't been brutally fisted in a while, I can enjoy the water jets on my back and relax a bit."
    menu:
        "About that. I think it's time for you re-join my harem." if haremza == False and girlsinharem <= 5 and money >= 5 and zaradismissed == False:
            scene poolzara02 with dissolve
            za "Do you have money now? I have my needs..."
            mc "Yeah, I'm loaded, so I'll take good care of you."
            call LustPlusZara
            $ haremza = True
            $ zaraharem = True
            $ girlsinharem += 1
            $ haremzararejoined = True
            window hide
            show haremzara at plus
            $ renpy.pause(2.0, hard=True)
            hide haremzara
            mc "Now that's better, I wouldn't want to lose such a beautiful girl..."
            scene poolzara03 with dissolve
            za "I'll see you some evening this week I guess... I'd better go and do lots of kegels to prep my pussy then... Bye [name]!"
            mc "That would be advisable. I DO plan some brutal fisting indeed... (what a fine ass...)"
            mc "Oh well, I might as well go for a swim since she's leaving."
            jump PoolOut            
        "Enjoy it while it lasts then, Zara. You'll be begging me to get you back into my harem one day....":
            scene poolzara02 with dissolve
            za "As long as you have money to cover my needs, I'm willing, [name]...."
            mc "Ah, yes. Money. I need more of that. You girls are expensive."
            scene poolzara03 with dissolve
            za "I'll see you around [name]. And I'll enjoy my pussy being normal-sized while it last..."
            mc "Oh well, I might as well go for a swim since she's leaving."
            jump PoolOut            

label AmyPool:
$ poolam += 1
if poolam >= 1:
    jump AmyPool01

label AmyPool01:
scene pool04 with dissolve
show amypool01
mc "Amy sure has a fine ass..."
menu:
    "Call her":
        hide amypool01
        show amypool03
        am "Yes?"
        jump AmyPoolDialogue
    "Leave":
        mc "I'll go for a swim while I'm here."
        jump PoolOut
    "Wolf-whistle":
        play sound "Sounds/wolfwhistle.mp3"
        hide amypool01
        show amypool02 with dissolve
        am "Is it for my ass or my muscles?"
        menu:
            "Your ass.":
                hide amypool02
                show amypool03
                am "Mmh... I don't even want to think about what goes through your head at this pool then..."
                mc "Nothing untoward, nothing untoward!"
                hide amypool03
                show amypool04                        
                am "This is very disappointing, I thought you were... different."   
                hide amypool04
                mc "Oops,I fucked up on that one. I'll go for a swim instead then."
                jump PoolOut
            "Your muscles.":
                am "I'm glad you're an admirer of female muscles, most guys are taken aback by them..."
                if poolamymusclelust == False:
                    $ poolamymusclelust = True
                    call LustPlusAmy
                am "Now watch this..."
                hide amypool02
                show amypool05
                am "Aaaar."
                mc "NICE."
                hide amypool05
                show amypool02
                am "That's enough for now [name], I need to get back to the workshop. See you later!"
                hide amypool02
                mc "Oh well, I might as well go for a swim then..."
                jump PoolOut            
        jump PoolOut

label AmyPoolDialogue:
menu:
    "Would you like to go on an outdoors date with me? (date with Amy tomorrow morning)" if lustam >= 2 and amydatedone == False and knowredcanyon:
        hide amypool03
        show amypool02
        with fastdissolve
        am "Outdoors? And where do you have in mind?"
        mc "A beautiful place called the Red Canyon. We can go tomorrow morning if you're not too busy."
        am "Oh, I've heard of it... It's supposed to be beautiful. Agreed then! I'll be going for a swim now to get into shape for it!"
        $ amydateon = True        
        hide amypool02
        jump PoolOut
    "I'd like to show you something (hypnotize her, +1 lust)" if pendulum and showedpendulum == False:
        call UsePendulum
        hide amypool03
        show amypool04
        with fastdissolve
        am "Wh...what happened... Oh, hi [name], you look... hot today..."
        call LustPlusAmy
        hide amypool04
        show amypool03
        with fastdissolve
        am "Err... I don't know why I said that, it's probably the heat of the pool that's getting to my head..."
        $ showedpendulum = True
        hide amypool03
        jump PoolOut
    "Let's compare muscles. Just for the heck of it." if lustam >= 3 and haremam == False:
        hide amypool03
        show amypool02
        with fastdissolve
        am "Alright! Let's see what you've got..."
        window hide
        show amypool02 at right with move
        show mcmompool10 at left with moveinleft
        mc "Fuck yeah, my muscles are all pumped up in anticipation..."
        hide mcmompool10
        hide amypool02
        show mcamypool01
        with dissolve
        am "I'll start..."
        play sound "Sounds/womangroan.mp3"
        mc "Nice biceps flexing there, Amy, I can really see the definition..."
        scene pool04 blurred
        show mcamypool02
        with dissolve
        mc "My turn..."
        play sound "Sounds/mcworkout.mp3"
        mc "What do you think of THOSE biceps?"
        am "Wow! They're so... fucking HUGE!"
        am "Now flex them with me with your hands above your head!"
        scene pool04
        show mcamypool03
        with dissolve
        play sound "Sounds/womangroan.mp3"
        mc "ALRIGHT!"
        am "We're like two muscle FREAKS! Well, especially YOU! Can I touch them?"
        mc "Of course, I'll flex my right bicep as BIG as possible for you Amy..."        
        hide mcamypool03
        show mcamypool04
        with dissolve
        mc "Like that..."
        play sound "Sounds/mcworkout.mp3"
        am "Damn [name]! Your bicep must be AT LEAST 25 inches around in that state!"
        mc "Even more Amy..."
        am "You're making me... all dizzy..."
        if amypoolust == False:
            $ amypoolust = True        
            call LustPlusAmy
        scene pool05 blurred
        show mcamypool05
        with dissolve
        mc "Then feel those triceps too!"
        am "Everything in you is like HARDENED STEEL!"
        mc "Yeah, pretty much. ROCKHARD STEEL you might even say!"
        scene pool04 blurred
        show mcamypool06
        with dissolve
        am "You're really a naughty boy... But a naughty MUSCLE STUD BOY, so you can get away with it..."
        am "And also, please take your hand off my tit, I need to go back to the workshop."
        mc "Ah.. Yeah, alright. I'll go for a swim then... See you around, Amy!"
        am "See you, ROCKHARD STUD!"
        jump PoolOut
    "Nothing really. I'm going for a swim." if haremam == False:
        am "Fascinating. I'm not. Enjoy your swim then."
        jump PoolOut
    "Nothing really. Just wanted to see that hot bod of yours again." if haremam:
        hide amypool03
        show amypool02
        with fastdissolve
        am "Well, you'll have PLENTY of time to see it better in your BED this week, remember? * wink *"
        mc "Fuck yeah! I won't forget to satisfy you, that's for sure!"
        jump PoolOut
     
label BellaPool:
scene poolbella01 with dissolve
be "Oh, hello [name]. Do you like our indoor swimming pool? It's great isn't it? The water is so warm..."
scene poolbella02 with dissolve
mc "Such a fine ass..."
scene poolbella03 with dissolve
be "You were saying?"
menu:
    "Offer her a Holy Pubic Hair" if pubichair >=1:
        mc "I have something for you. I'm sure you'll like it."
        be "Oh, thank you [name]! I was really hoping you'd offer me one of these, since Pythia never wants to grant ME an audience..."
        call LustPlusBella
        mc "It's a bit wet, but you can dry it off..."
        be "Speaking of which, I need to dry off myself. I hope to go on an outdoors adventure with you soon [name]!"
        $ pubichair -= 1
        jump PoolOut
    "You've got the perfect attire to go on a date with me..." if lustbe >= 2 and belladatedone == False and knowredcanyon:
        hide poolbella03
        show poolbella04
        with fastdissolve
        be "And why is that?"
        mc "Because I'll take to the Red Canyon where a teeny-weeny bikini is almost mandatory!"
        hide poolbella04
        show poolbella05
        with fastdissolve
        be "Oh, I see... I'll be there then. With a different but still teeny-weeny bikini..."
        $ belladateon = True  
        mc "I'll pick you up in the morning and take you to there then!"
    "It's time for you to join my harem... So sayeth the Phallus Lord." if lustbe >= 4 and harembe == False and askedbellajoin == False and bellaharem == False and belladatedone and mcchurch >= 4:
        $ bellapool = True
        be "Does he now? Did he also warn you about this..."
        call BellaHarem
    "It's time for you to re-join my harem... And be in communion with the wishes of the One-Eye." if lustbe >= 4 and harembe == False and askedbellajoin == False and bellaharem and belladismissed == False:
        $ bellapool = True
        be "You know what I'm about to say, right?"
        mc "Not really, a girl will need to be kicked out, but who? The suspense is killing me."
        call BellaHarem
    "Don't bother just yet.":
        pass
$ bellapool = False
be "I'm gonna need to dry off. I hope to go on an outdoors adventure with you soon [name]!"
mc "Well, since I'm in the pool, I might as well go for a swim..."
jump PoolOut

label DebraPool:
$ poolde += 1
if poolde >= 1:
    jump DebraPool01

label DebraPool01:
scene pool04 with dissolve
show debrapool03
mc "She's got her back turned to me... Enough time to ogle her ass before she turns round then..."
scene pool04 blurred with fastdissolve
show debrapoolarse
mc "Yeah, I'm almost getting a boner right here and there..."
scene pool04 with dissolve
show debrapool02
de "You think you can sneak on me like this? I heard you arriving... What do you want?"
menu:
    "That's a very futuristic swimsuit you have there Professor...":
        de "That's right, I designed it myself, using ultra-resistant kevlar, in case some pervert tried to get it off me. Even one as muscular as you."
        mc "I see. So I'll have to get it off you some other way then... *wink*"
        hide debrapool02
        show debrapool04
        with fastdissolve
        de "Until you mature enough to seduce a woman like me, you'll just have to spend your life wanking that giant cock of yours! See you in the lab WORKING [name]!"
        hide debrapool04
        mc "(Damn, she left. I might as well go for a swim then...)"
        jump PoolOut
    "Hey Professor, any new crazy experiment planned?" if gwensciencefucked:
        de "My experiments are NOT crazy! They are essential to the survival of the human race."
        de "Only those with a superior intellect can fathom the extent of their importance. Ie: NOT YOU!"
        hide debrapool02
        show debrapool01
        with fastdissolve
        de "But to answer your question, I DO have experiments planned and I expect your full voluntary cooperation when the time comes."
        mc "Sure thing boss, anything to help your \"superior intellect\". *snickers*"
        hide debrapool01
        show debrapool04        
        with fastdissolve
        de "Now if you'll excuse me, I have to go back to the lab and WORK, unlike some lazy people around here..."
        hide debrapool04
        mc "(Damn, she left. I might as well go for a swim then...)"
        jump PoolOut
    "I would like to offer this beautiful necklace I found on my adventures..." if necklace:
        hide debrapool02
        show debrapool04
        with fastdissolve
        de "For me? I am not used to people giving me gifts, as a scientist, I usually only accept grant money from Soros. But hand it over, I'll try it on."
        scene pool04 blurred with fastdissolve
        show debrapoolnecklace
        call LustPlusDebra
        $ necklace = False
        de "Thank you [name], it is indeed a very nice necklace... Now I will go back to the lab to study its mineral composition."
        hide debrapoolnecklace
        mc "And I'll go for a swim then."
        jump PoolOut
    "How about you get some sun and go on a date with me? (date with Debra in the morning)" if lustde >= 2 and debradatedone == False:
        hide debrapool02
        show debrapool04
        with fastdissolve
        de "Leaving the lab? With Gwen in charge?"
        $ debradateon = True
        mc "Just give her some menial task so she doesn't blow it up. You NEED to get out. For your own mental health."
        hide debrapool04
        show debrapool01
        with fastdissolve        
        de "Fine, but I hold YOU responsible if anything happens in my absence in this lab!"
        mc "Alright! I'll pick you up in the morning then."
        $ seenlab = True
        jump Main01
    "I think it's time now for you to join my harem Debra. And try out some experimental SEX with me!" if lustde >= 4 and haremde == False and debraharem == False and girlsinharem <= 5:
        hide debrapool02
        show debrapool01
        with fastdissolve
        de "Experimental sex you say? I have some inventions of mine that could indeed get handy..."
        $ haremde = True
        $ girlsinharem += 1
        $ debraharem = True
        window hide
        show haremdebra at plus
        $ renpy.pause(2.0, hard=True)
        hide haremdebra
        mc "I'll call you at nights. After Gwen is done cleaning up the mess in the lab..."
        $ seenlab = True
        jump Main01
    "I think it's time for you to re-join my harem Debra." if lustde >= 4 and haremde == False and debraharem and debradismissed == False  and girlsinharem <= 5:
        de "You dared to throw me out! Me, being thrown out of the harem of an underling!"
        mc "I was just testing. Like, experimenting if you wish. But now I know the limits of my experimental procedure."
        hide debrapool02
        show debrapool01
        with fastdissolve        
        de "I should bloody well hope so. An underling NEVER dismisses his superior. I trust you will not make the SAME experimental mistake again!"
        $ haremde = True
        $ girlsinharem += 1
        $ debraharem = True
        window hide
        show haremdebra at plus
        $ renpy.pause(2.0, hard=True)
        hide haremdebra
        mc "I sure won't, Professor, I sure won't..."
        $ seenlab = True
        jump Main01
    "Err... Nothing. I'll leave.":        
        de "Fascinating conversation..."
        jump PoolOut
   
label GwenPool:
$ poolgw += 1
if poolgw >= 1:
    jump GwenPool01
if poolgw  >= 2:
    jump GwenPool02
if poolgw  >= 3:
    jump GwenPool03
    
label GwenPool04:
scene gwenpoolpregnant01
with dissolve
mc "Hey Gwen, what are you doing here?"
scene gwenpoolpregnant02
with dissolve
gw "I'm trying to get some rest from carrying this MONSTER baby you put in my belly, that's what! Floating is the only way I get respite from the extra gravity pull..."
mc "I see. Well, I'll let you two float and I'll go swimming then."
gw "Yeah, rub it in that I can't even move my arms and legs properly... God I hate being pregnant!"
jump PoolOut

label GwenPool01:
scene pool05
show gwenpool01
with dissolve
if gwensciencefucked == True and gwenapologized == False:
    call GwenDialogueRape

gw "And what brings you here? You need to relax?"
mc "Yeah. What about you? Aren't you supposed to be working in the lab with Debra?"
gw "Not right now. Thanks God I'm allowed every now and then to escape the daily routine of getting fired at or burnt or maimed in the most excrutiating way Debra can find..."
label GwenPoolDialogueChoice:
menu:
    "Are you hurt right now? Maybe I can give you a back rub." if gwenrub == False:
        gw "Oh, wow, that would be wonderful! I've just been beaten with a stick by this lunatic who wanted to test its rigidity so I am all sore back there..."
        jump GwenPoolRub
    "I was wondering if you could get me some strong lubricant?" if missioncy and missioncydone == False:
        gw "Strong lubricant? Why do you need that?"
        if gwensciencefucked:
            gw "Are you planning on ramming that giant pole in my pussy again? No THANK YOU!"
        if gwensciencefucked == False:
            mc "Just some scientific experiment I'm conducting."
            gw "Well, pussy juice is a VERY strong lubricant. And Since I share a bunk with Angie, I can tell you the girl is PISSING the stuff when she's having erotic dream."
            mc "Interesting. Thanks for the tip..."
            jump GwenPoolDialogueChoice            
#    "Would you like to go on a date with me Gwen?" if lustgw >= 2 and dategwen == False:
#        jump GwenDialogueJoe
    "You look beautiful in that bikini Gwen." if missiongw02 == False:
        gw "Thanks [name]. That means... not a lot to me. For your information, the only thing I care about is finishing my PhD..."
        mc "Ah, right.. Anything I could do to help you with that?"
        gw "Well, except if you have the brains of Albert Einstein, which, no offense, you clearly DON'T, the only thing I could think of..."
        gw "...You could always help me in the lab. I work on the side on top of what Debra tells me to do to finish my PhD."
        hide gwenpool01
        show gwenpool04
        with fastdissolve
        gw "If you did the same, I could finish my experiments faster and finally write up my thesis!"
        mc "Alright, I'll think about it."
        $ missiongw02 = True
        window hide
        show missiongw02 at posmission
        $ renpy.pause(4.0, hard=True)
        hide missiongw02
        mc "I'll go for a swim now."
        jump PoolOut
    "I'd like to show you something (hypnotize her, +1 lust)" if pendulum and showedpendulum == False:
        call UsePendulum
        gw "Wh...what happened... Oh, hi [name], you look... smart today... And I'm wearing a bikini! *giggles*"
        call LustPlusGwen
        hide gwenpool01
        show gwenpool02
        with fastdissolve
        gw "Err... I don't know why I said that, I mean, you don't even have a PhD. I'll... leave you now..."
        $ showedpendulum = True
        hide gwenpool02 with dissolve
        mc "I might as well go for a swim then..."
        jump PoolOut
    "I would like to offer you this necklace I found on my adventures." if necklace:
        hide gwenpool01
        show gwenpool04 
        with fastdissolve
        if gwensciencefucked:
            gw "For me? Of all the girls, you chose me? Or is it to apologize for raping me? In any case, I'll gladly accept your gift [name]!"
        if gwensciencefucked == False:
            gw "For me? Of all the girls, you chose me? Wow, I feel so special now. Let me see it [name]!"
        scene pool05 blurred with dissolve
        show gwenpoolnecklace
        call LustPlusGwen
        $ necklace = False
        gw "Thanks, I really like it! I'll take it back to my room, I don't want to lose it here."
        hide gwenpoolnecklace
        mc "I'll go for a swim now."
        jump PoolOut
    "Would you like to escape your daily routine and go on a date with me? (date with Gwen tomorrow morning)" if lustgw >= 2 and gwendatedone == False and knowredcanyon:
        hide gwenpool01
        show gwenpool04 
        with fastdissolve
        gw "A date? I haven't been on one since... A long time. Because of this damn PhD that takes forever."
        mc "Also cos they aren't many men around."
        gw "That's true too. Agreed then!"
        $ gwendateon = True        
        hide gwenpool04
        mc "I'll go for a swim now."
        jump PoolOut
    "I think the time is ripe for you to join my harem." if lustgw >= 4 and haremgw == False and gwenharem == False and girlsinharem <= 5 and gwendatedone:
        hide gwenpool01
        show gwenpool02 
        with fastdissolve
        gw "I don't know... I mean, I AM attracted by the offer, but I don't want you to RAPE me again."
        mc "If you're in my harem, it won't be rape by definition. So everything's fine and dandy."
        $ haremgw = True
        hide gwenpool02
        show gwenpool04 
        with fastdissolve
        gw "Alright then, I'll join!"
        mc "Good girl."
        $ haremgw = True
        $ girlsinharem += 1
        $ gwenharem = True
        window hide
        show haremgwen at plus
        $ renpy.pause(2.0, hard=True)
        hide haremgwen
        mc "I'll call you at nights, and all you'll have to do is obey my every sexual order. Which is not rape at all."
        hide gwenpool04
        show gwenpool01 
        with fastdissolve
        gw "Then, I should prepare myself for that. Emotionally I mean. See you, [name]!"
        hide gwenpool01
        with fastdissolve 
        mc "And I guess I'll go for a swim while I'm here then."
        jump PoolOut
    "I think it's time for you to re-join my harem Gwen..." if lustgw >= 4 and haremgw == False and gwenharem  and gwendismissed == False  and girlsinharem <= 5:
        hide gwenpool01
        show gwenpool02 
        with fastdissolve
        gw "Perhaps I can give you a second chance..."
        mc "Not just perhaps. You will. You know you can't live with my HUGE COCK, right?"
        hide gwenpool02
        show gwenpool03 
        with fastdissolve
        gw "Oh, alright, I'll admit it. I want to be back so bad!"
        mc "Good girl."
        $ haremgw = True
        $ girlsinharem += 1
        $ gwenharem = True
        window hide
        show haremgwen at plus
        $ renpy.pause(2.0, hard=True)
        hide haremgwen
        mc "I'll call you at nights, and you'll be sexually fullfilled once again."
        hide gwenpool03
        show gwenpool04 
        with fastdissolve
        gw "Alright! I'm so excited, I have to... leave and get ready for it!" 
        hide gwenpool04
        with fastdissolve 
        mc "And I guess I'll go for a swim while I'm here then."
        jump PoolOut
    "Err... Nothing. I'll leave.":   
        hide gwenpool01
        show gwenpool03        
        with fastdissolve
        gw "Fascinating conversation..."
        jump PoolOut
        
label GwenPoolRub:
scene gwenrub01 with dissolve
mc "I'll start with a thigh rub."
gw "Fine by me, let's see how good you are with your hands, when you're not breaking stuff in the lab..."
scene gwenrub02 with dissolve
play sound "Sounds/womanmoan.mp3"
mc "(She's enjoying it...)"
scene gwenrub03 with dissolve
gw "That's a bit naughty of you to be rubbing my crotch like that [name]... But I liked your massage, I feel so much more relaxed..."
call LustPlusGwen
$ gwenrub = True
gw "I can go back to the lab now and work on my thesis, thanks to that relaxing \"massage\"."
mc "You're welcome!"
jump PoolOut

label BarbaraPool:
$ poolba += 1
if poolba == 1:
    jump BarbaraPool01
if poolba >= 2:
    jump BarbaraPool02
if poolba >= 3:
    jump BarbaraPool03

label GwenPool02:
"This scene has not been implement yet... Go for a swim instead."
jump PoolOut


label BarbaraPool01:
scene pool03 with dissolve
show barbarapool01
mc "Barbara sure has a fine ass..."
menu:
    "Call her":
        hide barbarapool01
        show barbarapool02
        ba "Yes?"
        jump BarbaraPoolDialogue
    "Leave":
        mc "I'll go for a swim while I'm here."
        jump PoolOut
    "Wolf-whistle":
        play sound "Sounds/wolfwhistle.mp3"
        hide barbarapool01
        show barbarapool04 with dissolve
        ba "That is highly inappropriate behavior young man! I'm your TEACHER!"
        if classfuck:
            mc "Well, I was just showing my appreciation for the hot body I banged the other day for educational purposes..."
            ba "Ah, err... Yes, let's just forget about that, shall we?"
            mc "I'll try but it will be HARD teach!"
            hide barbarapool04
            show barbarapool03
            ba "(sigh)... What do you want [name]?"
            jump BarbaraPoolDialogue
        call LustMinusBarbara
        ba "That's it, I'm going to dry off and leave this pool full of young PERVERTS! President Trumpf should lock you up in a concentration camp!"
        hide barbarapool04
        mc "Well, that's a bit far-fetched. Like there could be any concentration camps in this country, pfff..."
        jump PoolOut
        
label BarbaraPoolDialogue:
menu:
    "What are we going to learn next teach?":        
        ba "Since you only come VERY FEW times, I can't say what YOU will learn. Not much is my guess..."
        mc "Hey! You're the teacher, if I don't learn anything, it's YOUR fault!"
        hide barbarapool02
        show barbarapool03
        ba "No, it's Chief Lena's fault, I am willing to give you a proper PATRIOTIC education, but she prefers to waste your time on some pointless quest."
        mc "Right, well, I came here to relax, so that's what I'll do..."
        jump PoolOut        
    "What could I do to increase my grades?":
        hide barbarapool02
        show barbarapool03        
        with fastdissolve
        ba "Are you trying to bribe me?"
        mc "Err. No, I'm just offering some \"services\"."
        hide barbarapool03
        show barbarapool04        
        with fastdissolve
        ba "Well, I don't need your \"services\"! Now leave me alone."
        hide barbarapool04
        mc "That didn't go down well... I'll go for a swim then."
        jump PoolOut
    "How about we go for a swim together Barbara?":
        hide barbarapool02
        show barbarapool04
        with fastdissolve
        ba "Can't you see I just came OUT of the pool? I'm all wet and I'm wasting my time speaking to you when I should be drying off."
        ba "GOODBYE [name]!"
        hide barbarapool04
        mc "That didn't go down well... I'll go for a swim then."
        jump PoolOut
    "I'd like to show you something (hypnotize her, +1 lust)" if pendulum and showedpendulum == False:
        call UsePendulum
        hide barbarapool02
        show barbarapool04
        with fastdissolve        
        ba "Wh...what happened... Oh, hi [name], my FAVORITE student looks mighty SPUNKY in a speedo!"
        call LustPlusBarbara
        hide barbarapool04
        show barbarapool08
        with fastdissolve
        ba "Err... I don't know why I said that, this is so unbecoming of my usual professionalism... I'm sorry [name] but I should leave now and better sutdy the De Vos manual to become a better teacher."
        $ showedpendulum = True
        hide barbarapool08 with dissolve
        mc "I might as well go for a swim then..."
        jump PoolOut
    "I like your patriotic swimsuit.":
        ba "I'm glad you do, I bought it on www.trumpfmadeinjina.com."
        ba "They sell all sorts of patriotic ware there, you should buy something yourself and show your support for our country!"
        mc "Err.. Yeah, I'll think about it..."
        window hide
        show missionba at posmission
        $ renpy.pause(4.0, hard=True)
        hide missionba
        $ missionba = True
        if persistent.tipson:
            show barbaratip at tips with dissolve
            pause
            hide barbaratip
        jump PoolOut

label BarbaraPool02:
scene pool03 with dissolve
show barbarapool01
mc "Barbara sure has a fine ass..."
hide barbarapool01
show barbarapool02
label BarbaraPoolDialogue02:
menu:
    "How about we go for a swim together Barbara?":
        hide barbarapool02
        show barbarapool04
        ba "Can't you see I just came OUT of the pool? I'm all wet and I'm wasting my time speaking to you when I should be drying off."
        ba "GOODBYE [name]!"
        hide barbarapool04
        mc "That didn't go down well... I'll go for a swim then."
        jump PoolOut
    "I like your patriotic swimsuit." if missionba == False:
        ba "I'm glad you do, I bought it on www.trumpfmadeinjina.com."
        ba "They sell all sorts of patriotic ware there, you should buy something yourself and show your support for our country!"
        mc "Err.. Yeah, I'll think about it..."
        window hide
        show missionba at posmission
        $ renpy.pause(4.0, hard=True)
        hide missionba
        $ missionba = True
        jump PoolOut
    "I got myself a patriotic MNAGAt hat teach! (+1 Lust Barbara)" if missionba and mnagahat and successmissionba == False:
        hide barbarapool02
        show barbarapool05
        ba "Oh really, let's see it then!"
        show mcpoolhat01 at midleft with moveinleft
        show barbarapool05 at midright with move
        hide barbarapool05
        show barbarapool07  at midright       
        ba "Oh, you look so CLASSY in that baseball cap [name]! You could definitely join one of our Glorious Leader's great rallies with it."
        call LustPlusBarbara
        mc "Yeah, I can tell by my reflection in the pool. Totally not deplorable at all."
        ba "Don't jump in the pool with it though, I don't think it's very high quality material."
        mc "Sure teach!"
        ba "I'm going to dry off now..."
        scene pool06 with fastdissolve
        show barbarapool06
        mc "(Yep, nice ass fur sure...) I'd better leave and go for a swim or she'll see me ogling her though...)"
        $ successmissionba = True
        jump PoolOut
    "Would you like to pose for a PATRIOTIC calendar with me Barbara?" if missionjoe02 and missionjoe02barbara == False:
        hide barbarapool02
        show barbarapool03
        ba "What? I'm not sure, I've never done that before... Why would you need me for such a calendar?"
        mc "Well, you already have a patriotic swimming suit for starters... And you're smoking hot too."
        hide barbarapool03
        show barbarapool04
        ba "I'm not planning on posing in a swimsuit with you [name]! This would be highly inappropriate..."
        mc "The calendar competition was launched by President-for-life Trumpf himself teach! How could you refuse?"
        hide barbarapool04
        show barbarapool08
        ba "Err... Ok, if it is for the sake of our Great Nation, then I'll do it I guess..."
        window hide
        show missionjoebarbara at posmission
        $ missionjoe02barbara = True
        hide barbarapool08
        show barbarapool02        
        mc "I'll call you when Joe is ready for it then. Bye Barbara!"
        hide missionjoebarbara
        jump PoolOut
    "I'd like to show you something (hypnotize her, +1 lust)" if pendulum and showedpendulum == False:
        call UsePendulum
        hide barbarapool02
        show barbarapool04
        with fastdissolve        
        ba "Wh...what happened... Oh, hi [name], my FAVORITE student looks mighty SPUNKY in a speedo!"
        call LustPlusBarbara
        hide barbarapool04
        show barbarapool08
        with fastdissolve
        ba "Err... I don't know why I said that, this is so unbecoming of my usual professionalism... I'm sorry [name] but I should leave now and better sutdy the De Vos manual to become a better teacher."
        $ showedpendulum = True
        hide barbarapool08 with dissolve
        mc "I might as well go for a swim then..."
        jump PoolOut
    "I'd like to invite you on a date Barbara." if lustba >= 2 and knowredcanyon and barbaradatedone == False:
        hide barbarapool02
        show barbarapool08
        with fastdissolve        
        ba "A date? Between a teacher and her teenage student?"
        mc "Nothing wrong about that. Most boys' first crush is their teacher."
        hide barbarapool08
        show barbarapool04
        with fastdissolve                
        ba "So I'm your crush then [name]? How sweet of you. Well, I'll allow my favorite student to have a date with his crush then!"
        $ barbaradateon = True
        mc "I'll pick you up in the morning."
        ba "Ooh, that means I'll have to cancel class.... I'll think of something!"
        jump PoolOut
    "I think it's time now for you to join my harem teach..." if lustba >= 4 and haremba == False and barbaraharem == False and girlsinharem <= 5 and barbaradatedone:
        hide barbarapool02
        show barbarapool08
        with fastdissolve        
        ba "I can't break the law and end up in jail like so many horny size-queen, teen-loving teachers before me!"
        mc "If you join my harem, sex between us becomes perfectly legal. Encouraged even. You know, to re-populate the Earth?"
        hide barbarapool08
        show barbarapool04
        with fastdissolve                
        ba "Mmh, it is true that we are both WHITE and... I should do my duty for our Glorious New Nation!"
        $ haremba = True
        $ girlsinharem += 1
        $ barbaraharem = True
        window hide
        show harembarbara at plus
        $ renpy.pause(2.0, hard=True)
        hide harembarbara
        mc "I'll call you at nights. You know, when the other students are sleeping."
        hide barbarapool04
        show barbarapool05
        with fastdissolve        
        ba "I can't wait. To get impregnated with your SUPERIOR seed!"
        jump PoolOut
    "I think it's time for you to re-join my harem Barbara..." if lustba >= 4 and haremba == False and barbaraharem and barbaradismissed == False and girlsinharem <= 5:
        hide barbarapool02
        show barbarapool08
        with fastdissolve        
        ba "It ended badly for me last time..."
        mc "And you learnt from your mistakes. So you've improved and there's no reason for the same thing to happen again."
        ba "My mistakes? I don't remember that. *sigh* Fine. I can't refuse anything to my favorite horse-hung student!"
        $ haremba = True
        $ girlsinharem += 1
        window hide
        show harembarbara at plus
        $ renpy.pause(2.0, hard=True)
        hide harembarbara
        mc "I'll call you at nights. You know, when the other students are sleeping."
        hide barbarapool08
        show barbarapool05
        with fastdissolve        
        ba "Hopefully, it will last longer than last time..."
        jump PoolOut

jump PoolOut
        
label PennyPool:
$ poolpe += 1
if poolpe >= 1:
    jump PennyPool01

label PennyPool01:
scene pool03 with dissolve
show pennypool01
pe "Yes?"
menu:
    "That's a pretty revealing outfit you're wearing Penny..." if spokepoolpe01 == False:
        $ spokepoolpe01 = True
        hide pennypool01
        show pennypool02
        pe "And so? The less clothes I wear, the better I feel..."
        mc "Well, in that case, why don't you..."
        hide pennypool02
        show pennypool01
        pe "I can't be naked in the pool area unfortunately, it's against the rules...."
        menu:
            "Rules? Road Warriors don't obey rules! (+1 Road Warriors)" if mcwarrior >= 2:
                hide pennypool01
                show pennypool03
                with fastdissolve
                pe "You're right! Damn it, I'm going to strut my stuff and to hell with anyone that tells me I can't!"
                mc "That's the spirit! Of the ROAD WARRIORS!"
                call PlusWarrior
                hide pennypool03
                show pennypool05
                with fastdissolve
                pe "Now I feel liberated!"
                mc "My cock is also trying to liberate itself..."
                pe "It will have to wait another time, my lust for you is simply not high enough..."
                mc "Damn it! I guess I'll go for a swim instead then..."
                jump PoolOut
            "Ah yes, Rules must be obeyed at all times. So says our Commander-in-Chief! (+1 Trumpsters)" if mctrumpster >=2:
                call PlusTrumpster
                hide pennypool01
                show pennypool04
                with fastdissolve
                pe "You're starting to become rather pathetic [name]... I'm off, I'll leave you to your pool and your \"Rules\"..."
                hide pennypool04 with dissolve
                mc "Well, in that case, I shall go for a swim. As per the Rules that a swimming pool is to swim in."
                jump PoolOut
            "That's too bad...You have such a hot body... (+1 lust Penny)" :
                hide pennypool01
                show pennypool02
                with fastdissolve
                pe "Yes, it is indeed... But remember, you can visit me on Monday evenings if you want to see more \"skin\"... *wink*"
                call LustPlusPenny
                mc "Ah, good to know... Thanks Penny!"
                mc "(I'll go for a swim now to keep my cock down cos it's starting to get pretty damn BIG in my speedos...)"
                jump PoolOut
    "Your outfit is an invitation to sin... You beguiling Devil-Woman! (+1 Church of the Redeeming Phallus, -1 Road Warriors)" if mcchurch >= 2 and spokepoolpe02 == False:
        $ spokepoolpe02 = True
        call PlusChurch
        hide pennypool01
        show pennypool04
        with fastdissolve
        pe "You're starting to become rather pathetic [name]... I'm off, I'll leave you to your pool and your \"Church\"..."
        call MinusWarrior
        hide pennypool04 with dissolve
        mc "Well, in that case, I shall go for a swim. Away from the temptation of a... err.... super-hot woman."
        jump PoolOut
    "Would you like to go on a date with me Penny?" if lustpe >= 2 and lustpe <= 4 and knowredcanyon and pennydatedone == False:
        hide pennypool01
        show pennypool02
        with fastdissolve
        pe "Why not. Your lust is high enough enough, but not too high, so I don't risk much."
        mc "I like your positive attitude! I'll pick you up tomorrow morning then."
        pe "I so can't wait I'm going to dip in the pool to cool down my brain..."
        mc "Now, that sarcasm wasn't necessary. I'll go for a swim too then."
        $ pennydateon = True
        hide pennypool02 with dissolve
        jump PoolOut
    "I'd like to show you something (hypnotize her, +1 lust)" if pendulum and showedpendulum == False:
        call UsePendulum
        hide pennypool01
        show pennypool02
        with fastdissolve
        pe "Wh...what happened... Ooh, I feel so tingly between my legs! Must be the fabric rubbing against my clit..."
        call LustPlusPenny
        hide pennypool02
        show pennypool04
        with fastdissolve
        pe "Err... I don't know why I said that, I mean, I'd rather I wasn't wearing ANYTHING actually. I'll go back to my quarters where I can be as naked as a baby."
        $ showedpendulum = True
        hide pennypool04 with dissolve
        mc "I might as well go for a swim then..."
        jump PoolOut
    "I think it's time now for you to join my harem Penny..." if lustpe  >= 4 and harempe == False and pennyharem == False and girlsinharem <= 5:
        hide pennypool01
        show pennypool03
        with fastdissolve
        pe "A harem? Road Warriors are FREE CREATURES!"
        mc "Then you're FREE to join my harem."
        hide pennypool03
        show pennypool02
        with fastdissolve
        pe "I guess that makes sense. I'll join out of my OWN FREE WILL then!"
        $ harempe = True
        $ girlsinharem += 1
        $ pennyharem = True
        window hide
        show harempenny at plus
        $ renpy.pause(2.0, hard=True)
        hide harempenny
        mc "I'll call you at nights, so we can explore each other's bodies in a FUN SEXY WAY."
        hide pennypool02
        with fastdissolve
        jump PoolOut
    "I think it's time for you to re-join my harem Penny..." if lustpe >= 4 and harempe == False and pennyharem and pennydismissed == False  and girlsinharem <= 5 and pennyrejoined == False:
        $ pennyrejoined = True
        hide pennypool01
        show pennypool04
        with fastdissolve
        pe "And what assurances do I have that you won't dump me on the side of the road like you did last time?"
        mc "Remember, the Road is everywhere. In spirits. So you were still there with me. In spirits."
        hide pennypool04
        show pennypool02
        with fastdissolve
        pe "That's a fishy explanation but I'll agree to come back into your harem. THIS ONCE."
        $ harempe = True
        $ girlsinharem += 1
        $ pennyharem = True
        window hide
        show harempenny at plus
        $ renpy.pause(2.0, hard=True)
        hide harempenny
        mc "I'll call you at nights, so we can explore each other's bodies in a FUN SEXY WAY."
        hide pennypool02
        with fastdissolve
        jump PoolOut
    "Nothing.":
        hide pennypool01
        show pennypool02
        with fastdissolve
        pe "Nothing? Is that it???"
        mc "Yep, this was the only menu option available to me at this stage. Nothing. I need to get higher in certain factions to be able to say something else to you..."
        pe "Hopefully, we'll meet randomly again after that happened."
        hide pennypool02 with dissolve
        mc "(I guess I'll go for a swim then...)"
        jump PoolOut

label PoolOut:
scene mcpool with dissolve
mc "The water is nice and refreshing..."
$ period +=1 
if period == 4:
    mc "But it's getting late...."
    jump Bedroom
scene pool01 with fade
jump Main01

label LeavePool:
mc "Ok, the girl I'm interested in isn't there. So I'll leave without losing time like in the previous versions of the game when I forced to go swimming."
jump Main01