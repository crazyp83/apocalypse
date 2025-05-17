label ExploreHex23:
stop sound
$ explored = True
if knowforwardops or successprisoner:
    jump ForwardOps01
scene desert02 with dissolve
mc "There's nothing here apparently..."
if alone:
    mc "Let's go back to the compound and report to Chief Lena then..."
if withbe:
    be "But I have an inkling that something interesting might be hidden in those hills..."
    mc "Same here. We'll have to find out what it is. One day."
if withpe:
    pe "But I have an inkling that something interesting might be hidden in those hills..."
    mc "Same here. We'll have to find out what it is. One day."
$ period += 1
scene command01 with fade
show lena01
if alone:
    le "So, what do you have to report about area C3, [name]?"
if alone == False:
    le "So, what do you have to report about area C3 scouts?"
mc "Nothing yet, Chief. The area is full of hills and hidden crags. We couldn't explore everything on our first run."
hide lena01
show lena03
with fastdissolve
le "I see... We have to make sure there is absolutely nothing there or find out what IS there."
hide lena03
show lena10
with fastdissolve
le "Scouts DISMISSED!"
hide lena10
jump LeaveCommand

label ForwardOps01:
$ exploredhex23 = True
if foundbase == False:
    if alone:
        scene forward01
        show militiaguard01
        with fade
        mc "I think I finally found that forward ops base... I should try and infiltrate it."
        $ foundbase = True
        jump ForwardGuardChoice
    if withbe:
        scene forward01
        show militiaguard01
        show forwardbella
        with fade
        be "I think we finally found that forward ops base."
        mc "Are we supposed to just report back that we found it?"
        be "Chief Lena clearly said that we... I mean, YOU, needed to infiltrate it."
        mc "What? That sounds dangerous, there's a guard armed to the teeth over there!"
        be "May the Mighty Phallus Lord give you courage [name]. Se-men."
        $ foundbase = True
        jump ForwardGuardChoice
    if withpe:
        scene forward01
        show militiaguard01
        show forwardpenny
        with fade
        pe "I think we finally found that damn forward ops base."
        mc "Are we supposed to just report back that we found it?"
        pe "Chief Lena clearly said that we... I mean, YOU, needed to infiltrate it."
        mc "What? That sounds dangerous, there's a guard armed to the teeth over there!"
        pe "Road Warriors aren't scared. You shouldn't be."
        mc "Except I'm the one going, not YOU!"
        $ foundbase = True
        jump ForwardGuardChoice
if foundbase:
    if withbe:
        scene forward01
        show militiaguard01
        show forwardbella
        with fade
        be "So, you have a plan to infiltrate the base this time?"
        mc "I'm working on it."
    if withpe:
        scene forward01
        show militiaguard01
        show forwardpenny
        with fade
        pe "So, you have a plan to infiltrate the base this time?"
        mc "I'm working on it."
    if alone:
        scene forward01
        show militiaguard01
        with fade
        mc "Let's think of a way of getting in again..."

label ForwardGuardChoice:
if persistent.tipson:
    show hexforwardtip at tips with dissolve
    pause
    hide hexforwardtip
menu:
    "Shoot the guard (use sniper rifle)" if sniper:
        jump ForwardGuardShoot
    "Shoot the guard (use rifle)" if rifle and sniper == False:
        mc "She's quite far away. It would be better if I had a sniper rifle."
        jump ForwardGuardShoot
    "Approach the guard nonchalantly":
        jump ForwardGuardApproach
    "Approach the guard wearing a Trumpf Militia uniform" if militiauniform:
        jump ForwardGuarduniform
    "Screw you guys, I'm going home":
        $ infiltratefail = True
        jump ForwardOut

label ForwardGuardShoot:
if sniper:
    show mcsniper with dissolve
if sniper == False:
    show mcrifle with dissolve
    
if withbe:
    be "Take your time... She ain't going nowhere..."
if withpe:
    pe "Take your time... She ain't going nowhere..."
if shotmilitia:
    hide militiaguard01
    if sniper:
        hide mcsniper
    if sniper == False:
        hide mcrifle
    show militiaguard02
    if sniper:
        show mcsniper
    if sniper == False:
        show mcrifle
    with fastdissolve    
    fg "ALERT! Deep state rebels!"                 
    window hide
    play sound "Sounds/gun.mp3"
    $ renpy.pause(1.0, hard=True)
    mc "Shit, she already spotted us! Looks like I can't shoot her with a rifle more than once. Let's get the hell out of here!"
    $ infiltratefail = True
    stop sound
    jump BackHex23
    
call DiceRoll
if sniper:
    $ dshootroll=mcfirearms+diceroll
if sniper == False:
    $ dshootroll=mcfirearms+diceroll-3
if (dshootroll >= 7 and not diceroll == 1) or diceroll == 6:
    window hide
    play sound "Sounds/gun.mp3"
    $ renpy.pause(1.0, hard=True)
    hide militiaguard01
    if sniper:
        hide mcsniper
    if sniper == False:
        hide mcrifle
    show militiaguard03
    if sniper:
        show mcsniper
    if sniper == False:
        show mcrifle
    with fastdissolve
    stop sound
    fg "Oh no, I've been shot! I need to leave my post and go to the medbay where nurse Rachel Twin will get me back to full health in one night."             
    hide militiaguard03 with dissolve
    mc "I got her, she's leaving! And she's not even dead. We're like the A-Team, no one ever dies in this game."
    $ shotmilitia = True
    if withbe:
        be "Stop talking and get inside!"
    if withpe:
        pe "Stop talking and get inside!"
    mc "Roger that!"
    jump ForwardIn
if (dshootroll <= 6 and not diceroll == 6) or diceroll == 1:
    window hide
    play sound "Sounds/gun.mp3"
    $ renpy.pause(1.0, hard=True)
    hide militiaguard01
    if sniper:
        hide mcsniper
    if sniper == False:
        hide mcrifle
    show militiaguard02
    if sniper:
        show mcsniper
    if sniper == False:
        show mcrifle
    with fastdissolve    
    fg "ALERT! Deep state rebels!"
    window hide
    play sound "Sounds/gun.mp3"
    $ renpy.pause(1.0, hard=True)
    mc "Shit, I missed and now she's shooting back at us. Let's get the hell out of here!"
    $ infiltratefail = True
    stop sound
    jump BackHex23

label ForwardGuardApproach:
play sound "Sounds/whistling.mp3"
scene forward02
show militia01
with dissolve
fg "Hey you, stop right there or I'll shoot you!"
if mctrumpster == 5 and trumpsternickname and guardmission == False:
    hide militia01
    show militia03
    with fastdissolve
    fg "Oh sorry \"[name] the Grabber\", I didn't recognize you. At first. The boss is waiting for you, the Alpha barrack on your left."
    fg "But first... Could I... ask you for an autograph, it's such a honor to meet you!"
    mc "Sure,, let me sign your top..."
    hide militia03    
    show militia04
    with dissolve
    fg "My girlfriends are going to be sssooo jealous when I tell them..."
    hide militia04    
    show militia05
    with dissolve    
    mc "Yeah? Well, you can add that to what you tell them."
    fg "*blush* Oooh, [name], that is so grabby of you! But you're a celebrity, so it's alright."
    $ guardmission = True
    jump ForwardLeft
if mctrumpster == 5 and trumpsternickname and guardmission:
    hide militia01
    show militia03
    with fastdissolve
    fg "Oh sorry \"[name] the Grabber\", I didn't recognize you. Again. But you're not expected today. Why are you here?"    
    mc "Err..."
    menu:
        "Use Ruby" if withru and usednranra == False:
            ru "I'm from the NRANRA. Coming for the armory inspection. Here's my card."
            fg "Everything seems to be in order. You may enter. The armory is on the right."
            hide militia03 with dissolve
            $ usednranra = True
            ru "This won't work again, I'm warning you. It's too dangerous. But I liked doing it, it gave me an adrenaline kick..."
            call LustPlusRuby
            jump ForwardRight
        "I'm here for the inspection. NRANRA inspection. Here's my card." if nranramember and usednranra == False:
            fg "And where's your weapon?"
            if rifle == False and sniper == False:
                mc "My weapon? err... I left it at home."
                fg "AN NRANRA member never leaves without his weapon. You're a LIAR!"
                window hide
                show guardshoot
                play sound "Sounds/gun.mp3"
                pause 0.5
                hide guardshoot
                $ mcinjuredgun = True         
                mc "Hey, stop shooting, it fucking hurts!"
                call MCInjury
                fg "I didn't KILL YOU because you're a Trumpster but this base is OFF-LIMITS to civilians, so LEAVE NOW!"
                mc "Ah right, that's why there was a sign saying \"Military Personnel only\". I get it now. After I got shot by my own faction."
                $ infiltratefail = True
                jump ForwardOut                    
            mc "Here it is. A bad motherfucker as you can see."
            fg "Everything seems to be in order. The armory is on the right. Good inspection, \"[name] the Grabber\"."
            $ usednranra = True
            jump ForwardRight
        "She needs to see me again. Top secret stuff.":
            fg "I don't think so, I know every top secret stuff... You're an INFILTRATOR!"
            window hide
            show guardshoot
            play sound "Sounds/gun.mp3"
            pause 0.5
            hide guardshoot
            $ mcinjuredgun = True         
            mc "Hey, stop shooting, it fucking hurts!"
            call MCInjury
            fg "I didn't KILL YOU because you're a Trumpster but this base is OFF-LIMITS to civilians, so LEAVE NOW!"
            mc "Ah right, that's why there was a sign saying \"Military Personnel only\". I get it now. After I got shot by my own faction."
            jump ForwardOut            
    jump ForwardOut

if mctrumpster == 5:
    mc "I'm a Trumpster. Can't you tell?"
    hide militia01
    show militia03
    with fastdissolve
    fg "Ah yes, sorry sir, I hadn't noticed. At first. Still, what's your business here?"
    menu:
        "Use Ruby" if withru and usednranra == False:
            ru "I'm from the NRANRA. Coming for the armory inspection. Here's my card."
            fg "Everything seems to be in order. You may enter. The armory is on the right."
            hide militia03 with dissolve
            $ usednranra = True
            ru "This won't work again, I'm warning you. It's too dangerous. But I liked doing it, it gave me an adrenaline kick..."
            call LustPlusRuby
            jump ForwardRight
        "Just checking if the perimeter is secure enough.":
            hide militia03
            show militia01
            with fastdissolve
            fg "Only senior officers or NRANRA members do that. And you're not even military. I smell a rat, you're a liar!"
            if nranramember and usednranra == False:
                mc "Hey, I'm from the NRANRA, we never lie! Her's my card as PROOF."
                hide militia01
                show militia03
                with fastdissolve
                fg "Ah, sorry, I didn't know. You should present your card straight away next time."
                mc "My bad, so can I go through for my inspection tour then?"
                hide militia03
                show militia01
                with fastdissolve
                fg "Hang on a minute, where's your weapon?"
                if rifle == False and sniper == False:
                    mc "My weapon? err... I left it at home."
                    hide militia01
                    show militia02
                    with fastdissolve
                    fg "AN NRANRA member never leaves without his weapon. You're a LIAR!"
                    window hide
                    show guardshoot
                    play sound "Sounds/gun.mp3"
                    pause 0.5
                    hide guardshoot
                    $ mcinjuredgun = True         
                    mc "Hey, stop shooting, it fucking hurts!"
                    call MCInjury
                    fg "I didn't KILL YOU because you're a Trumpster but this base is OFF-LIMITS to civilians, so LEAVE NOW!"
                    mc "Ah right, that's why there was a sign saying \"Military Personnel only\". I get it now. After I got shot by my own faction."
                    $ infiltratefail = True
                    jump ForwardOut                    
                if rifle or sniper:
                    mc "Here it is. A bad motherfucker as you can see."
                    hide militia01
                    show militia03
                    with fastdissolve
                    fg "Yes indeed. Go ahead, the armory is on the right. So go there. On the RIGHT."                
                    jump ForwardRight               
            mc "Oh come on, so is our President-for-Life, so what's the big dea..."
            hide militia01
            show militia02
            fg "How dare you insult our Dear Leader!"
            window hide
            show guardshoot
            play sound "Sounds/gun.mp3"
            pause 0.5
            hide guardshoot
            $ mcinjuredgun = True         
            mc "Hey, stop shooting, it fucking hurts!"
            call MCInjury
            fg "I didn't KILL YOU because you're a Trumpster but this base is OFF-LIMITS to civilians, so LEAVE NOW!"
            mc "Ah right, that's why there was a sign saying \"Military Personnel only\". I get it now. After I got shot by my own faction."
            jump ForwardOut
        "I'm here for the \"mission\". Know wadda mean?" if guardmission == False:
            fg "Ah, yes, the boss is waiting for you. Alpha barrack on your left."
            mc "(That was easier than I thought...)"
            $ guardmission = True
            jump ForwardIn
        
if mcdeep == 5:
    mc "Calm down lady, I..."
    hide militia01
    show militia02
    with fastdissolve
    fg "DEEP STATE INFILTRATOR! OPEN FIRE!"
    window hide
    show guardshoot
    play sound "Sounds/gun.mp3"
    pause 0.5
    hide guardshoot
    $ mcinjuredgun = True         
    mc "Hey, stop shooting, it fucking hurts!"
    call MCInjury
    fg "I'll keep shooting until I have no more ammo, YEEE-HAAW!"
    mc "(I'd better get the FUCK OUT OF HERE!)"
    jump ForwardOut
if mcwarrior == 5:
    mc "Calm down lady, I..."
    hide militia01
    show militia02
    with fastdissolve
    fg "ROAD WARRIOR! OPEN FIRE!"
    if nranramember and usednranra == False:
        mc "Don't shoot, I'm from the NRANRA, you can't shoot me!"
        fg "Ah, sorry, I didn't know. You should present your card straight away next time."
        mc "My bad, so can I get through then?"
        fg "I see. That makes sense. I guess. You can go through then, the armory is on the right. Report back to me after your inspection tour. I'll come and check on you too."
        $ usednranra = True
        jump ForwardRight                    
    window hide
    show guardshoot
    play sound "Sounds/gun.mp3"
    pause 0.5
    hide guardshoot
    $ mcinjuredgun = True         
    mc "Hey, stop shooting, it fucking hurts!"
    call MCInjury
    fg "I'll keep shooting until I have no more ammo, YEEE-HAAW!"
    mc "(I'd better get the FUCK OUT OF HERE!)"
    jump ForwardOut
if mcchurch == 5:
    mc "Calm down lady, I..."
    hide militia01
    show militia02
    with fastdissolve
    fg "We don't welcome Church missionaries here, move on buddy, or I'll have no other option but to send you back to your Phallus God as a stiff."
    mc "Those who oppose the Church shall not redeem their sou..."
    fg "GET LOST I SAID!"
    mc "Alright, gee, what a bad attitude."
    $ infiltratefail = True
    jump ForwardOut
if mcsierra == 5:
    mc "Calm down lady, I..."
    fg "What are you looking for?"
    mc "This building desecrates this sacred ground and Mother Nature will not toler..."
    hide militia01
    show militia02
    with fastdissolve
    fg "GET LOST HIPPIE!"
    if spliff and usedspliff == False:
        mc "I think you need something to relax, girl, you're too angry. I've got just the thing..."
        hide militia02   
        show militia06
        with fastdissolve
        fg "A joint? But... I can't... It's not allowed. Even though it's tempting..."
        mc "Oh come on, what's a little spliff gonna do? You see someone around here? We're in the middle of the desert..."
        fg "Alright, just a few puffs then, I've got a while until the next guard shift. But don't you dare tell anyone."
        hide militia06   
        show militia07
        with fastdissolve
        fg "oh man, this is so good... This is good.... Who are you again?"
        mc "I'm Vice-General...err... Ponce."
        fg "oh, right, right... Get in Vice-General, the General is expecting you..."
        mc "Of course he is. I mean she is. I'm Vice-General Ponce."
        $ usedspliff = True
        jump ForwardIn
    if spliff == False:
        mc "Alright, gee, what a bad attitude."
        $ infiltratefail = True
        jump ForwardOut
    mc "Alright, gee, what a bad attitude."
    $ infiltratefail = True
    jump ForwardOut

if nranramember and usednranra == False:
    mc "Don't shoot, I'm from the NRANRA, you can't shoot me!"
    fg "I didn't receive any notification of an NRANRA inspection, that sounds fishy... You might be a Deep State infiltrator."
    mc "We changed our SOP. To confuse the Deep State. Now we don't call ahead."    
    fg "And where's your weapon?"
    if rifle == False and sniper == False and withru:
        ru "Here is MY weapon. Modified AK-47 with laser-guided visor. A new model custom-made for elite NRANRA members."
        hide militia01
        show militia03
        with fastdissolve
        fg "Damn, that thing is pretty cool. WIsh I had one... Everything seems to be in order. You may enter. The armory is on the right."
        hide militia03 with dissolve
        $ usednranra = True
        ru "Good thing I came along, but this won't work again, I'm warning you. It's too dangerous. But I liked doing it, it gave me an adrenaline kick..."
        call LustPlusRuby
        jump ForwardRight
    if rifle == False and sniper == False:
        mc "My weapon? err... I left it at home."
        hide militia01
        show militia02
        with fastdissolve
        fg "AN NRANRA member never leaves without his weapon. You're a LIAR!"
        window hide
        show guardshoot
        play sound "Sounds/gun.mp3"
        pause 0.5
        hide guardshoot
        $ mcinjuredgun = True         
        mc "Hey, stop shooting, it fucking hurts!"
        call MCInjury
        $ infiltratefail = True
        mc "Flee, flee, run for your life!"
        jump ForwardOut                    
    if rifle or sniper:
        mc "Here it is. A bad motherfucker as you can see."
        hide militia01
        show militia03
        with fastdissolve
        fg "Yes indeed. Go ahead, the armory is on the right. So go there. On the RIGHT."                
        $ usednranra = True
        jump ForwardRight               
    hide militia01
    show militia06
    with fastdissolve
    fg "I see. That makes sense. I guess. You can go through then, the armory is on the right. Report back to me after your inspection tour. I'll come and check on you too."
    $ usednranra = True
    jump ForwardRight                    
mc "Calm down lady, I..."
fg "What are you looking for?"
mc "Err... I'm dying to go for a pee?"
hide militia01
show militia02
with fastdissolve
fg "Go PISS SOMEWHERE ELSE!"
mc "Alright, gee, what a bad attitude."
$ infiltratefail = True
jump ForwardOut

label ForwardGuarduniform:
play sound "Sounds/whistling.mp3"
scene forward02
show militia01
with dissolve
fg "Hey you, stop right there or I'll shoot you!"
if militiauniform and usedmilitiauniform == False:
    mc "I'm from the militia, can't you tell?"
    hide militia01
    show militia03
    with fastdissolve
    fg "Ah yes, sorry sir, you can never be careful enough with those Deep State infiltrators loose in the country."
    mc "Right, right...."
    $ usedmilitiauniform = True
    jump ForwardIn
if militiauniform and usedmilitiauniform:
    mc "I'm from the militia, can't you tell?"
    hide militia01
    show militia02
    with fastdissolve
    fg "You're wearing a STOLEN uniform! You're a DEEP STATE INFILTRATOR!"
    window hide
    show guardshoot
    play sound "Sounds/gun.mp3"
    pause 0.5
    hide guardshoot
    $ mcinjuredgun = True         
    mc "Hey, stop shooting, it fucking hurts!"
    call MCInjury
    fg "I'll keep shooting until I have no more ammo, YEEE-HAAW!"
    mc "(I'd better get the FUCK OUT OF HERE!)"
    jump ForwardOut

label ForwardIn:
$ infiltratewin = True
scene forward03 with dissolve
mc "Mmmmh. Where should I go?"
call screen basechoice
screen basechoice:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/back.png"
        hover "Icons/back.png"
        action Jump ("ForwardOut")
    imagebutton:
        focus_mask True
        idle "Icons/goleft.png"
        hover "Icons/goleft.png"
        action Jump ("ForwardLeft")
    imagebutton:
        focus_mask True
        idle "Icons/goright.png"
        hover "Icons/goright.png"
        action Jump ("ForwardRight")

label ForwardLeft:
scene forward04 with dissolve
if knowalpha:
    mc "Ah, there's the Alpha-barrack..."
if knowalpha == False:
    mc "There's a barrack with an entrance..."
menu:
    "Barge in with guns blazing" if rifle or sniper or dagger:
        jump AlphaFight
    "Knock and enter":
        jump AlphaEnter
    "Leave":
        jump ForwardIn

label AlphaFight:
$ metiv = True
scene bossroom01
show ivankaops03
with dissolve
mc "YEE-HAW!"
iv "Yee-Haw indeed, but your visit is no surprise to ME, general Ivanka!"
play sound "Sounds/punch.mp3"
scene bossroom01 blurred
show ivankaops09
with flash
mc "Fuck, this HURTS! Stop it, please!"
call MCInjury
$ mcinjuredfight = True 
scene bossroom01
show ivankaops01
with dissolve
iv "I'll spare your useless life! This time... Now get out of MY base!"
$ ivankafail = True
jump ForwardOut

label AlphaEnter:
$ metiv = True
if trumpsternickname and mctrumpster >=4:
    scene bossroom01
    show ivankaops02
    with fade
    iv "Oh, there you are, \"[name] the Grabber\". It's a pleasure meeting you AT LAST."
    if medalcomplicity and medalawarded == False:
        iv "You're in luck, I just received a shipment of medals from my factory in Jina. Now is the time to officially award you the coveted \"Medal of Complicity\"."
        hide ivankaops02
        show ivankaops06
        with fastdissolve
        iv "Let me go and get one... Where did I put them... Ah, yes, there."
        hide ivankaops06
        show ivankaops04
        with fastdissolve
        iv "At attention soldier!"
        mc "Yes SIR! Err... I mean, MAM!"
        play sound "Sounds/whitehouse.mp3"
        iv "For services rendered to our Great New Nation, I, General Ivanka of the Trumpf Militia, award you, \n\"[name] the Grabber\", the Medal of Complicity."
        iv "Hmmm, there doesn't seem to be anywhere to pin it on your chest... But I see there is PLENTY of space on your MASSIVE BULGE!"
        scene bossroom02 blurred
        show ivankaops05
        with fastdissolve
        iv "I think it will fit just fine RIGHT THERE, don't you think, BIG BOY?"        
        window hide
        show medal at posmission
        $ renpy.pause(0.5, hard=True)
        pause
        hide medal
        iv "And of course, you also get a hefty reward of $20 New Dollars. God Bless New America!"
        $ medalawarded = True        
        $ money += 20
        if mctrumpster == 5:
            iv "And since you have joined our faction, you deserve ANOTHER reward... Get out of those tight pants and show me your GIANT BOYMEAT!"           
            jump IvankaBlow
            
    if medalcomplicity == False:
        hide ivankaops02
        show ivankaops08
        with fastdissolve
        iv "It's a shame you did not manage to exfiltrate our spy from the compound though... It's not too late to do it, she's still there."
        iv "So this is the MISSION I'm giving you, [name]. Do you accept?"
        menu:
            "Accept":
                mc "Of course, General Ivanka!"
                hide ivankaops08
                show ivankaops02
                with fastdissolve
                iv "That's a good boy... A good boy who deserves a REWARD! Get out of those tight pants and show me your GIANT BOYMEAT!"
                jump IvankaBlow
            "Refuse":
                mc "Na, she's good being a prisoner, she was useless anyway."
                hide ivankaops08
                show ivankaops03
                with fastdissolve                
                iv "That is not for YOU to decide! You're a TRAITOR!"
                play sound "Sounds/punch.mp3"
                scene bossroom01 blurred
                show ivankaops09
                with flash
                mc "Fuck, this HURTS! Stop it, please!"
                call MCInjury
                $ mcinjuredfight = True 
                scene bossroom01
                show ivankaops01
                with dissolve
                iv "I'll spare your useless life! This time... Now get out of MY base!"
                $ ivankafail = True
                jump ForwardOut
        
if trumpsternickname == False:
    scene bossroom01
    show ivankaops01
    with fade
    iv "[name]... We meet at last."
    menu:
        "What are you guys up to?":
            if mctrumpster == 5:
                iv "We're trying to get rid of the Deep State, that's what we're doing!"
                mc "Oh right, yeah, those pesky Deep State people... Pfff! I'm a total trumpster now, like level 5 or something."
                hide ivankaops01
                show ivankaops08
                with fastdissolve
                iv "Is that so? Therefore, you're in WITH us, I can count on you?"
                mc "Of course, General Ivanka!"
                iv "Then let me check that you're up to the task.... Get UNDRESSED NOW and show me your GIANT BOYMEAT!"
                jump IvankaBlow
            if mctrumpster <= 4:
                hide ivankaops01
                show ivankaops07
                with fastdissolve
                iv "That's none of your business! Just like you have NO BUSINESS being HERE!"
                mc "Oh, oh..."
                hide ivankaops07
                show ivankaops03
                with fastdissolve
                iv "Oh oh indeed, cos you can't beat ME at close combat! I'm TOO STRONG FOR YOU!"
                play sound "Sounds/punch.mp3"
                scene bossroom01 blurred
                show ivankaops09
                with flash
                mc "Fuck, this HURTS! Stop it, please!"
                call MCInjury
                $ mcinjuredfight = True 
                scene bossroom01
                show ivankaops01
                with dissolve
                iv "I'll spare your useless life! This time... Now get out of MY base!"
                $ ivankafail = True
                jump ForwardOut
        "I answered the call of your messages... (+1 Trumpsters)":
            hide ivankaops01
            show ivankaops08
            with fastdissolve
            iv "You mean... The one where I invited you over to SUCK ON YOUR GIANT BOYMEAT?"
            mc "Yep. That one."
            hide ivankaops08
            show ivankaops02
            with fastdissolve            
            iv "I knew you would finally join the dark... I mean, the Trumpf side! Alright. Get UNDRESSED THEN!"
            call PlusTrumpster
            jump IvankaBlow

label IvankaBlow:
scene bossroom02 blurred
show ivankabj01
with dissolve
iv "Damn, seeing is believing, I was told you were HUNG, but you are indeed A HORSE-HUNG HERO!"
mc "Yep, that's me!"
iv "That thing.... Still soft and already sssooo big. Like AT LEAST three times the length and width of Jared's pindick. YUM!"
mc "Well, get me hard and it'll become FIVE TIMES his size!"
iv "I can't wait to see this monster in all its ROCK-HARD GLORY. Please take it out and show me [name]!"
scene bossroom03 blurred
show ivankabj02
with dissolve
play music "Sounds/kiss.mp3"
iv "*kisses* What a GLORIOUS, TRUE AMERICAN FUCKPOLE!"
stop music
mc "Enough kissing and talking, open your mouth for my great big throat-gagging boymeat, General Ivanka!"
hide ivankabj02
show ivankabj03
with dissolve
mc "That's it... Now relax your throat muscles, and try and take a few more inches into your hungry size-queen mouth!"
hide ivankabj03
show ivankabj04
with dissolve
play music "Sounds/hardsucking.mp3"
mc "Oooh, your mouth is so good!"
hide ivankabj04
show ivankabj03
with fastdissolve
pause 0.2
hide ivankabj03
show ivankabj04
with fastdissolve
pause 0.2
hide ivankabj04
show ivankabj03
with fastdissolve
pause 0.2
hide ivankabj03
show ivankabj04
with fastdissolve
pause 0.2
hide ivankabj04
show ivankabj03
with fastdissolve
pause 0.2
hide ivankabj03
show ivankabj04
with fastdissolve
pause 0.2
hide ivankabj04
show ivankabj03
with fastdissolve
pause 0.2
hide ivankabj03
show ivankabj04
with fastdissolve
pause 0.2
hide ivankabj04
show ivankabj03
with fastdissolve
pause 0.2
hide ivankabj03
show ivankabj04
with fastdissolve
pause 0.2
hide ivankabj04
show ivankabj03
with fastdissolve
pause 0.2
hide ivankabj03
show ivankabj04
with fastdissolve
pause 0.2
stop music
mc "I love your sucking skills, but let's get to the REAL fun! Why don't you show me that alpha-radiated hot bod of yours Ivanka?"
hide ivankabj04
show ivankabj02
with fastdissolve
play sound "Sounds/kiss.mp3"
iv "*kisses* Of course, but just let me kiss that magnificent fuckpole one last time before I get undressed for YOU."

label IvankaSex01:
scene bossroom01 blurred
show ivankapose01
with dissolve
iv "That's what you wanted to see in the flesh [name]? My MUSCLED ALPHA-FEMALE BODY?"
mc "Ooh yeah!"
hide ivankapose01
show ivankapose02
with fastdissolve
iv "I am the most POWERFUL woman in the world! My biceps are made of PURE STEEL!"
mc "Alpha-radiation is the bomb! Literally."
hide ivankapose02
show ivankapose03
with fastdissolve
iv "Watch me flex my mighty biceps... See how they BALLOON with ABSOLUTE POWER?"
mc "I see, I see... And I can't wait to FEEL them too!"
hide ivankapose03
show ivankapose04
with fastdissolve
iv "And my bumcheeks are so CHORDED that they could CRUSH A HUMAN SKULL!"
mc "Thanks for the tip, I'll make sure not to get my face anywhere near it."
if trumpsternickname:
    iv "Now come and WORSHIP me \"[name] the Grabber\"!"
if trumpsternickname == False:
    iv "Now come and WORSHIP me [name]!"
hide ivankapose04
show ivankamc01
with dissolve
window hide
play sound "Sounds/womanmoan.mp3"
$ renpy.pause(1.0, hard=True)
iv "Ooh, I LOVE how you play with my big breasts!"
if trumpsternickname:
    mc "I'm good at grabbing stuff, that's why they call me \"[name] the Grabber\"!"
    iv "My family has always been good at grabbing stuff too."
if trumpsternickname == False:
    iv "I think I found a new nickname for you... \"[name] the Grabber\"!"
    window hide
    show mctrumpsternickname at posmission
    play sound "Sounds/skill.mp3"
    $ renpy.pause(2.0, hard=True)
    $ trumpsternickname = True
    hide mctrumpsternickname
    mc "Alright! I have a nickname now! Woo-ooh!"
hide ivankamc01
show ivankamc02
with fastdissolve
iv "Now kiss my POWERFUL biceps!"
play sound "Sounds/kiss.mp3"
iv "You like that, don't you? You like my HUGE muscles!"
mc "Mmh, yes, I love'em Ivanka... But it's time for YOU to WORSHIP MY BODY!"
iv "Of course, [name], it is worthy of MUSCLE WORSHIPPING!"
hide ivankamc02
show ivankamc03
with dissolve
iv "Those hard SLABS of pec muscles... are making me ssoo horny..."
hide ivankamc03
show ivankamc04
with fastdissolve
iv "...And that... COCK! So fucking MASSIVE! Mmh!"
window hide
play sound "Sounds/womanmoan.mp3"
$ renpy.pause(1.0, hard=True)
if ivankasex == 0:
    iv "Now come and OWN my ass, the hole that Jared never found!"
    $ ivankasex += 1
    jump IvankaAnal
if ivankasex >= 1:
    iv "Now bend me over the desk and fuck me like a dirty, useless senior adviser!"
    jump IvankaDesk
    
label IvankaAnal:
scene ivankanalscene
show ivankapreanal01
with dissolve
iv "I want it DEEP inside my ass, you hear me, \"[name] the Grabber\"?"
mc "Of course, my general. Sir, YES SIR!"
play music "Sounds/fucksound.mp3"
hide ivankapreanal01
label IvankaAnalSlow:
hide ivankaanalfast
show ivankaanalslow
with fastdissolve
call screen ivankaanalslow01
screen ivankaanalslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("IvankaAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("IvankaAnalFast") 

label IvankaAnalFast:
iv "I'm going to IMPALE myself on your GIANT shaft even FASTER!"
hide ivankaanalslow
show ivankaanalfast
call screen ivankaanalfast01
screen ivankaanalfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("IvankaAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("IvankaAnalSlow") 

label IvankaAnalEnd:
iv "Oh God, I'm cumming! From a GIANT BOYCOCK IN MY ASS!"
mc "And I'm about to come too!"
hide ivankaanalslow
hide ivankaanalfast
show ivankaanalcum01
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "AAAH! Hosing your back side at FULL BLAST!"
stop music
iv "YES! FLOOD it with your seed, \"[name] the Grabber\"! And then douse my body in your hot sauce!" 
scene ivankanalscene blurred
show ivankaanalcum02
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "RHAAA! There you go, general Ivanka!"
iv "Sssoo much young virile seed! You're all they said you were and MORE, [name]!"
scene ivankanalscene
show ivankaanalcum03
with dissolve
mc "That's it, I've emptied my nuts IN and ON you Ivanka!"
iv "Mmh, and it was wonderful, STUD!"
call LustPlusIvanka
iv "But I have a lot of work to do. We're planning an attack on that rebellious compound of unpatriotic deep state never-trumpfers."
mc "Ah, I see... (I should report this back to Chief Lena.) Right, I'll be on my way then, general."
iv "Do come back and see me anytime! *wink*"
$ knowplans = True
jump ForwardOut

label IvankaDesk:
scene ivankadeskscene blurred
show ivankapredesk01
with dissolve
iv "I still can't get over how BIG your cock is [name]... So veiny and menacing..."
mc "Look at my beast closely, Ivanka. It's about to fuck you fast and ROUGH!"
iv "Just like I like it! Fuck me as HARD as you want!"
play music "Sounds/fucksound.mp3"
scene ivankadeskscene
label IvankaDeskSlow:
hide ivankadeskfast
show ivankadeskslow
with fastdissolve
call screen ivankadeskslow01
screen ivankadeskslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("IvankaDeskEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("IvankaDeskFast") 

label IvankaDeskFast:
iv "Oh, God, you're fucking me so good, my tits are bouncing all over the place! Fuck me even HARDER please!"
hide ivankadeskslow
show ivankadeskfast
call screen ivankadeskfast01
screen ivankadeskfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("IvankaDeskEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("IvankaDeskSlow") 

label IvankaDeskEnd:
mc "I'm gonna flood your pussy anytime now, General Ivanka!"
iv "Yes, DROWN my fertile ovaries in your virile sperm, they belong to YOU now!"
hide ivankadeskslow
hide ivankadeskfast
show idesk04
show ivankadeskcum01
with fastdissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "FUCK YEAH, Cumming! RHAAA!"
iv "YES! Do your PATRIOTIC duty and IMPREGNATE ME! AAAH!" 
hide idesk04
hide ivankadeskcum01
show ivankadeskcum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "All the way up your womb! AAAH!"
iv "You're so ROUGH! Ah, it's hitting the back of my womb! I think I'm gonna faint! OOOH!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
hide ivankadeskcum02
show ivankadeskcum03
with fastdissolve
mc "Still cumming all over you! RHAA!"
mc "Oh, it looks like she really DID faint. My plan of fucking her HARD and ROUGH worked, now is the time to steal the attack plans and bring them back to the compound."
menu:
    "Steal the plans":
        mc "I'll get a reward from Chief Lena for sure now!"
        show missionplanssuccess at posmission
        window hide
        $ renpy.pause(2.0, hard=True)
        pause
        hide missionplanssuccess        
        call MinusTrumpster
        mc "But not from Ivanka. I probably shouldn't come back here."
        call LustMinusIvanka
        $ clearedhex23 = True
        $ stoleplans = True
    "Leave them, theft is bad, m'kay.":
        mc "It would be unpatriotic of me to steal those plans belonging to the Trumpf Militia..."
        call MinusDeep
        mc "Then again... I might want to consider it in the future."
        $ infiltratewin = True
jump ForwardOut

label ForwardRight:
scene forward05 with dissolve
if knowarmory:
    mc "Ah, there's the armory. Let's get inside discreetly."
if knowarmory == False:
    mc "There's a barrack with an entrance... Let's see what's inside..."
$ seenarmory = True
scene armory01 with dissolve
mc "Nice! Plenty of weapons to grab, but I should be quick before a guard comes along, probably best to only steal one thing at a time..."
call screen armory
screen armory:
    modal True
    imagebutton:
        focus_mask True
        idle "Explore/armorysniperidle.png"
        hover "Explore/armorysniperhover.png"
        action Jump ("StealArmorySniper")
    imagebutton:
        focus_mask True
        idle "Explore/armorydaggeridle.png"
        hover "Explore/armorydaggerhover.png"
        action Jump ("StealArmoryDagger")
    imagebutton:
        focus_mask True
        idle "Explore/armoryrifleidle.png"
        hover "Explore/armoryriflehover.png"
        action Jump ("StealArmoryRifle")
    imagebutton:
        focus_mask True
        idle "Explore/armoryexplosivesidle.png"
        hover "Explore/armoryexplosiveshover.png"
        action Jump ("StealArmoryExplosives")
    imagebutton:
        focus_mask True
        idle "Explore/armorymaskidle.png"
        hover "Explore/armorymaskhover.png"
        action Jump ("StealArmoryMask")

label StealArmorySniper:
if sniper:
    "You already have a rifle. This one is no different. What a waste..."
    mc "Damn it! But I don't have time to pick something up, I've got to leave before that militia chick comes checking on me..."
    jump ForwardOut
if sniper == False:
    window hide
    show sniperrifle at posmission
    $ renpy.pause(1.0, hard=True)
    pause
    hide sniperrifle
    $ sniper = True
    mc "Let's get out of here, a guard might come barging in at any time..."
    jump ForwardOut

label StealArmoryRifle:
if rifle:
    "You already have a rifle. This one is no different. What a waste..."
    mc "Damn it! But I don't have time to pick something up, I've got to leave before that militia chick comes checking on me..."
    jump ForwardOut
if rifle == False:
    window hide
    show rifleinventory at posmission
    $ renpy.pause(1.0, hard=True)
    pause
    hide rifleinventory
    $ rifle = True
    mc "Let's get out of here, a guard might come barging in at any time..."
    jump ForwardOut

label StealArmoryExplosives:
if explosives:
    "You already have explosives. You planned on blowing up the planet or something?"
    mc "Damn it! But I don't have time to pick something up, I've got to leave before that militia chick comes checking on me..."
    jump ForwardOut
if explosives == False:
    window hide
    show explosive at posmission
    $ renpy.pause(1.0, hard=True)
    pause
    hide explosive
    $ explosives = True
    mc "Let's get out of here, a guard might come barging in at any time..."
    jump ForwardOut
    
label StealArmoryMask:
if gasmask:
    "You already have a gas mask. It is re-usable, unlike covid-19 cotton masks..."
    mc "Damn it! But I don't have time to pick something up, I've got to leave before that militia chick comes checking on me..."
    jump ForwardOut
if gasmask == False:
    window hide
    show gasmask at posmission
    $ renpy.pause(1.0, hard=True)
    pause
    hide gasmask
    $ gasmask = True
    mc "Let's get out of here, a guard might come barging in at any time..."
    jump ForwardOut

label StealArmoryDagger:    
if dagger:
    "You already have a dagger. You planned on going on a killing spree or something?"
    mc "Damn it! But I don't have time to pick something up, I've got to leave before that militia chick comes checking on me..."
    jump ForwardOut
if dagger == False:
    window hide
    show daggerinventory at posmission
    $ renpy.pause(1.0, hard=True)
    pause
    hide daggerinventory
    $ dagger = True
    mc "Let's get out of here, a guard might come barging in at any time..."
    jump ForwardOut

label ForwardOut:
scene forward01 with fade
if alone and ivankafail:
    mc "Now I'm, gonna have to go back to the compound and shamefully admit I was beaten up by a girl..."
    jump BackHex23
if alone and mcinjuredgun:
    mc "Now I'm, gonna have to go back to the compound and shamefully admit I was shot by a girl..."
    jump BackHex23
if alone and infiltratefail:
    mc "Now I'm, gonna have to go back to the compound and shamefully admit I failed to infiltrate it..."
    jump BackHex23
if withbe:
    show forwardbella
    be "So, how did it go?"
if withpe:
    show forwardpenny
    be "So, how did it go?"
if seenarmory:
    mc "I managed to get inside their armory. And steal something."
    if withbe:
        be "I hope it's something useful... Let's go back to the compound and report to Chief Lena."
        jump BackHex23
    if withpe:
        pe "I hope it's something useful... Let's go back to the compound and report to Chief Lena."
        jump BackHex23 
    mc "Time to head back to the compound undetected..."
    jump BackHex23        
if ivankafail:
    mc "Err... I saw General Ivanka. But she's a tough cookie. She beat the crap out of me."
    if withbe:
        be "That's kind of pathetic. Being beaten up by a girl. The Church teaches that men are supposed to be virile."
        mc "Yeah, well, you haven't seen her muscles. She's alpha-radiated to the max."
        be "Let's go back to the compound and report the bad news to Chief Lena."        
    if withpe:
        pe "That's kind of pathetic. Being beaten up by a girl. The Church teaches that men are supposed to be virile."
        mc "Yeah, well, you haven't seen her muscles. She's alpha-radiated to the max."
        pe "Let's go back to the compound and report the bad news to Chief Lena."    
    jump BackHex23    
if stoleplans:
    mc "I've got the attack plans!"
    if withbe:
        be "Congrats! Let's go back to the compound as fast as possible, time is of the essence."
        jump BackHex23
    if withpe:
        pe "Congrats! Let's go back to the compound as fast as possible, time is of the essence."
        jump BackHex23
    mc "Time to head back to the compound undetected..."
    jump BackHex23    
if mcinjuredgun:
    mc "Err... Not so good. I didn't manage to infiltrate the base. Yet."
    if withbe:
        be "And I see you got shot too, you're bleeding heavily. We'd better head back, you need medical attention."
        be "Chief Lena is going to be disappointed in you..."
    if withpe:
        pe "And I see you got shot too, you're bleeding heavily. We'd better head back, you need medical attention."
        pe "Chief Lena is going to be disappointed in you..."
if infiltratefail:
    mc "Err... Not so good. I didn't manage to infiltrate the base. Yet."
    if withbe:
        be "Chief Lena is going to be disappointed in you... Let's head back to the base."
    if withpe:
        pe "Chief Lena is going to be disappointed in you... Let's head back to the base."
if infiltratewin and stoleplans == False:
    mc "I got inside. And then I chickened out."
    if withbe:
        be "That's kind of pathetic. Chief Lena is going to be disappointed in you... Let's head back to the base."
    if withpe:
        pe "That's kind of pathetic. Chief Lena is going to be disappointed in you... Let's head back to the base."
jump BackHex23

label BackHex23:
$ period += 1
scene command01 with fade
show lena01
if alone:
    le "So, what do you have to report about area C3, [name]?"
if alone == False:
    le "So, what do you have to report about area C3, scouts?"
if seenarmory:
    mc "I infiltrated their armory. They have tons of weapons, Chief Lena!"
    hide lena01
    show lenapensive
    with fastdissolve
    le "Mmmh, if they are so heavily armed, it means they are preparing something... We need to find out what it is! SCOUTS DISMISSED!"
    hide lenapensive
    with dissolve
    $ seenarmory = False
    jump LeaveCommand   
if ivankafail:
    mc "I managed to infiltrate the base. I know of the presence of General Ivanka there, Chief Lena!"
    hide lena01
    show lenapensive
    with fastdissolve
    le "Mmmh, if she's there, there must be something IMPORTANT going on. We MUST find out what it is! SCOUTS DISMISSED!"
    hide lenapensive
    with dissolve
    $ ivankafail = False
    jump LeaveCommand
if stoleplans:
    mc "I successfully managed to exfiltrate the Trumpf Militia attack plans, Chief!"
    hide lena01
    show lena07
    with fastdissolve
    le "I am impressed! And I knew I could count on you, [name]. Now we can be ready to counteract their attack and ensure the survival of the compound!"
    call LustPlusLena
    call PlusDeep
    le "As a sign of the compound's gratitude, I am also rewarding you with 50 New Dollars in hard cash. Unmarked notes."
    $ money += 50
    $ bounty = True
    le "Scouts dismissed!"
    if day == 5 or day == 6:
        le "Enjoy an evening at the bar [name], you deserve to relax a bit."
    hide lena07 with dissolve
    jump LeaveCommand

if infiltratefail:
    mc "I found the forward ops militia base. But I didn't manage to get inside just yet..."
    hide lena01
    show lena06
    with fastdissolve
    le "Did you try at least?"
    mc "Yeah, sure I tried, but it's guarded by heavily armed... err... militia chicks. We'll go back and I'll found a way, I promise."
    le "You'd better up your game [name]. SCOUTS DISMISSED!"
    $ infiltratefail = False
    hide lena06 with dissolve
    jump LeaveCommand
    
if infiltratewin:
    $ infiltratewin = False
    mc "I managed to infiltrate the Forward Ops base. But I didn't find anything interesting so far."
    hide lena01
    show lena06
    with fastdissolve
    if missionplan == False:
        le "I've learnt that they are on the verge of launching an attack on the compound. We need to find out what their attack plans are!"
        show missionplans at posmission
        window hide
        $ renpy.pause(2.0, hard=True)
        pause
        hide missionplans    
        $ missionplan = True
        hide lena06
        show lena10
        with fastdissolve        
        le "This should be your MAIN concern from now on!"
        mc "Ok, Chief!"
        le "Scouts dismissed!"
        hide lena10
        if mcinjuredgun:
            mc "I should go to the med bay to take care of that gun wound."
            jump Medbay        
        jump LeaveCommand
        
    if missionplan:
        hide lena01
        show lena10
        with fastdissolve
        le "So, you still didn't get a hold of those attack plans then? I told you, this should be your MAIN concern!"
        if lostlustlenaplans == False:
            call LustMinusLena
        $ lostlustlenaplans = True    
        le "Scouts dismissed!"
        hide lena10
        if mcinjuredgun:
            mc "I should go to the med bay to take care of that gun wound."
            jump Medbay        
        jump LeaveCommand

if mcinjuredgun:
    mc "I should go to the med bay to take care of that gun wound."
    jump Medbay
jump LeaveCommand

    
    
        
    
