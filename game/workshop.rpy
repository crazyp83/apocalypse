label Workshop:
show screen mcstats
show screen calendar
$ loc = "workshop"
$ seenworkshop = True

if period == 3:
    if mcbike:
        scene workshopevening01
        show workshopevening01bike
        with dissolve
    if mcbike == False:
        scene workshopevening01 with dissolve
    call screen workshopevening

if period == 1 or period == 2:
    scene workshop01 with dissolve
    call screen workshop
screen workshop:
    modal True    
    imagebutton:
        focus_mask True
        idle "Icons/exitidle.png"
        hover "Icons/exithover.png"
        action Jump ("LeaveWorkshop")
    if period == 2 and not (day == 6 or day == 7):
        imagebutton:
            focus_mask True
            idle "Workshop/workshopamyidle.png"
            hover "Workshop/workshopamyhover.png"
            action Jump ("WorkshopAmy")    
    if period == 1 and (day == 6 or day == 7):
        imagebutton:
            focus_mask True
            idle "Workshop/workshopamyidle.png"
            hover "Workshop/workshopamyhover.png"
            action Jump ("WorkshopAmy")    
    imagebutton:
        focus_mask True
        idle "Workshop/workshoprubyidle.png"
        hover "Workshop/workshoprubyhover.png"
        action Jump ("WorkshopRuby")
    imagebutton:
        focus_mask True
        idle "Workshop/rigidle.png"
        hover "Workshop/righover.png"
        action Jump ("WorkshopRig")
  
screen workshopevening:
    modal True    
    imagebutton:
        focus_mask True
        idle "Icons/exitidle.png"
        hover "Icons/exithover.png"
        action Jump ("LeaveWorkshop")
    imagebutton:
        focus_mask True
        idle "Workshop/workshopeveningrubyidle.png"
        hover "Workshop/workshopeveningrubyhover.png"
        action Jump ("WorkshopRuby")
    if mcbike:
        imagebutton:
            focus_mask True
            idle "Workshop/mcbikeidle.png"
            hover "Workshop/mcbikehover.png"
            action Jump ("WorkshopBike")  
  
label WorkshopBike:
$ spokeruby = True
scene workshopevening01
show workshopevening01bike
with dissolve
show ruby07 with moveinright
ru "What do you think you're doing? Leave the maintenance of your bike to PROFESSIONALS."
mc "I want to take it for a ride actually. I mean, it is MY bike, right?"
hide ruby07
show ruby06
with fastdissolve        
ru "Chief Lena doesn't want scouts to leave in the evening, it's too dangerous."
if mcwarrior == 5:
    mc "Oh come on, we're both Road Warriors, we don't care about no stinking danger!"
    hide ruby06
    show ruby08
    with fastdissolve
    ru "I guess you're right. What was I thinking... Go and PILLAGE and LOOT some encampments and come back with the skulls of your dead enemies, [name]!"
    mc "Well, OK, calm down, I didn't plan on slaughtering anyone specifically, but I'll see what I can do..."
    hide ruby08
    show ruby07
    with fastdissolve    
    ru "Be a ROAD WARRIOR and don't be a SISSY!"
    mc "Ok, ok... Gee. Can I go now?"
    hide ruby07
    show ruby01
    with fastdissolve        
    ru "Yeah, don't come back too late though, Chief Lena sometimes does the rounds before the night..."    
    jump HippyEvening
if haremru:
    mc "Well, just don't tell her then."
    hide ruby06
    show ruby07
    with fastdissolve
    ru "And why would I do that?"
    mc "Cos you're in my harem and I regularly give you some GOOD HUGE DICK that you love, that's why."
    if weekfuckedruby == False:
        ru "Well, you didn't THIS week yet. And I won't let you leave with your bike until you DO!"
        mc "Alright, alright. Gee, these harem girls just want to fuck all the time. Bunch of nymphos."
        jump LeaveWorkshop
    if weekfuckedruby:
        hide ruby07
        show ruby04
        with fastdissolve    
        ru "I gues you DID give me some GOOD DICK this week. Alright, I'll look the other way for you, STUD!"
    jump HippyEvening
mc "What does she know? She never leaves the compound..."
hide ruby06
show ruby07
with fastdissolve
ru "Maybe, but she's our CHIEF! So go back to your room, cos there's no chance you're leaving with that bike tonight!"
mc "(Damn it!). Alright, alright..."
if persistent.tipson:
    show hippytip at tips with dissolve
    pause
    hide hippytip
jump LeaveWorkshop

label WorkshopRig:
show workshoprubyidle
if not period == 1:
    show workshopamyidle
mc "Some big rigs. Worthy of monster truck jams."
jump Workshop

label WorkshopAmy:
scene workshop02 with dissolve
show amy01
am "Hi there [name]! What can I do for you? Or better, what can YOU do for the planet? (wink)"
label WorkshopAmyMenu01:
show amy01
menu:
    "I would like to train in mechanics. I've been told you're the best at that.":
        hide amy01
        show amy02
        with fastdissolve
        am "And you were told right! I am indeed extremely proficient at handling big tools."
        label WorkshopAmyMenu02:
        show amy02
        menu:
            "Good. Cos I've got a big tool that needs polishing right now.":
                hide amy02
                show amy05
                with fastdissolve
                am "Ha, ha, funny boy. Or NOT FUNNY AT ALL PERVERT BOY. Try again."
                hide amy05
                jump WorkshopAmyMenu02
            "Alright, can you teach me a bit, like, right now?":
                am "Sure, I was just about to refit the exhaust pipe on this rig. Watch me and learn."
                hide amy02
                jump MechanicsTraining
            "Cool to know. I'll make sure to come and see you when I have time to train and gain this valuable skill.":
                am "Fine. Do come back later then."
                hide amy02
                jump WorkshopAmyMenu01
    "Would you like to go on an outdoors date with me? (date with Amy tomorrow morning)" if lustam >= 2 and amydatedone == False and knowredcanyon:
        hide amy01
        show amy04
        with fastdissolve
        am "Outdoors? And where do you have in mind?"
        mc "A beautiful place called the Red Canyon. We can go tomorrow morning if you're not too busy."
        am "Oh, I've heard of it... It's supposed to be beautiful. Agreed then!"
        hide amy04
        show amy02 
        with fastdissolve
        $ amydateon = True        
        hide amy02
        jump WorkshopAmyMenu01
    "I'm rather interested in learning more about the Club Sierra. Saving the trees and the bees seems like such a worthy endeavor in those troubled times.":
        hide amy01
        show amy02
        with fastdissolve
        am "I am  glad to hear you say that! It is indeed! To become a devoted servant of Mother Nature."
        am "We have a meeting tonight in the swimming pool area. You are welcome to join us."
        am "Except this scene has not been rendered yet, so actually, no, you're not welcome to join..."
        mc "What a bummer..."
        hide amy02        
        jump WorkshopAmyMenu01
    "I think it's time now for you to join my harem Amy..." if lustam >= 4 and haremam == False and amyharem == False and girlsinharem <= 5 and amydatedone:
        hide amy01
        show amy03
        with fastdissolve
        am "I was wondering when you were going to ask me that... My pussy has been tingling ever since my lust for you reached level 4."
        $ haremam = True
        $ girlsinharem += 1
        $ amyharem = True
        window hide
        show haremamy at plus
        $ renpy.pause(2.0, hard=True)
        hide haremamy
        mc "I'll call you at nights, so we can be together as ONE in unity with Mother Nature and linked by our bodily fluids. Or something like that."
        hide amy02
        show amy05
        with fastdissolve        
        am "That sounds real romantic... *snickers*"
        hide amy05
        jump WorkshopAmyMenu01
    "I think it's time for you to re-join my harem Amy..." if lustam >= 4 and haremam == False and amyharem  and amydismissed == False  and girlsinharem <= 5:
        hide amy01
        show amy03
        with fastdissolve
        am "Alright, but on one condition..."
        hide amy03
        show amy02
        with fastdissolve        
        am "That you don't discard me again like a non-recyclable item!"
        mc "I was just recycling harem girls is all... Being a good manager of limited resources."
        $ haremam = True
        $ girlsinharem += 1
        $ amyharem = True
        window hide
        show haremamy at plus
        $ renpy.pause(2.0, hard=True)
        hide haremamy
        mc "I'll call you at nights, so we can be together as ONE in unity with Mother Nature and linked by our bodily fluids. Or something like that."
        hide amy02
        show amy05
        with fastdissolve        
        am "That sounds real romantic... *snickers*"
        hide amy05
        jump WorkshopAmyMenu01
    "I'd like to show you something (hypnotize her, +1 lust)" if pendulum and showedpendulum == False:
        call UsePendulum
        am "Wh...what happened... Oh, hi [name], you look... hot today..."
        call LustPlusAmy
        hide amy01
        show amy05
        with fastdissolve
        am "Err... I don't know why I said that, it's probably the heat in the workshop that's getting to my head..."
        $ showedpendulum = True
        hide amy05
        jump WorkshopAmyMenu01
    "How about we relax with one of Mother Nature most precious gifts. Marijuana." if spliff and spliffused == False:
        hide amy01
        show amy02
        with fastdissolve
        if period == 1:
            am "Well, I'm tempted but it's a bit early in the day... I have work to do on those rigs and need to be able to concentrate."
            mc "Ah. Ok, I'll come back for that another time then..."
            hide amy02
            jump WorkshopAmyMenu01
        am "Why not. I did most of the work I was supposed to do. Let's just move to some more quiet area of the workshop though, I don't want Ruby to see us..."
        scene workshop04
        show amy04
        with dissolve
        $ spliff = False
        $ spliffused = True
        am "There, it's better. Now pull it out and roll it, I can't wait!"
        hide amy04
        show amy08
        with dissolve
        am "Mmmh, that's some good stuff [name]... Thanks for sharing, just like Mother Nature intended..."
        call LustPlusAmy
        $ period += 1
        hide amy08
        show amy05
        with dissolve
        mc "Oh man, I'm stoned out of my mind. I'd better get back to my bedroom for just a bit..."
        am "Yeah, I'll do the same, I don't think I'm going to be very productive right now..."
        jump Bedroom
    "I should leave now, I'm a very busy man, busy saving the world and all that.":
        hide amy01
        show amy02
        with fastdissolve
        am "Sure. Go save the world with your big biceps [name], I'm sure the dying trees needed just that..."
        $ period += 1
        jump Workshop
        
label MechanicsTraining:
scene workshopamy01 with dissolve
am "So... I need a wrench. Something SOLID."
scene workshopamy02 with dissolve
mc "(Yeah, I've got something SOLID growing down my pants right now...)"
scene workshop02 with dissolve
show amy07
am "Would you mind concentrating on the job?"
mc "I am, I am. So, you've got a wrench. Now what?"
am "You get under the truck and have a fumble around."
am "If you don't wear overalls, you'll get dirty though and I don't have any your size."
mc "Alright. I'll take my clothes off then. It'll be more comfortable anyways."
mc "Unfortunately, this scene has not been implemented yet. What do we do?"
am "Well, we'll just pretend you learnt something."
#scene mechanics01 with dissolve
#am "How are you doing down there? Do you need any help at all [name]?"
#menu:
#    "No, I'm fine thanks. It's all starting to fall into place, I feel like I'm learning a lot right now.":
#        am "Alright..."
#        $ mcmechanics += 1
#        jump MechanicsTrainingEnd
#    "Well, you could help... I'm feeling a cramp down my legs...":
#        am "Yes, I see that... I'll make you feel better..."

$ mcmechanicslevel += 1
if mcmechanicslevel == 1:
#    call Levelup01
    mc "A couple more sessions handling big tools and I should get better at this!"   
if mcmechanicslevel == 2:
#    call Levelup02
    mc "Another session handling big tools and I should get better at this!"   
if mcmechanicslevel == 3:
#    call Levelup03
    mc "I feel like I know a lot about... big tools suddenly."
    call PlusMechanics
    $ mcmechanicslevel = 0
$ seenworkshop = True
$ period += 1
hide amy07
jump Main01
        
label WorkshopRuby:
scene workshop03
show ruby01
with dissolve
ru "Hey there big boy. What's up?"
label WorkshopRubyMenu01:
scene workshop03
show ruby01
menu:
    "How did you become so muscular and err...well, huge?":
        hide ruby01
        show rubyflex
        ru "You mean these guns?"
        hide rubyflex
        show ruby04
        with fastdissolve
        ru "And those funbags?"
        mc "Yeah, that's basically what I meant."
        ru "Same way you did buddy. Alpha-radiations. Gotta lov' em."  
        hide ruby04
        jump WorkshopRubyMenu01
    "You said you were a Road Warrior. But I can't see any tattoo on you." if spokeruby01 == False:
        hide ruby01
        show rubyflex
        with fastdissolve
        ru "Oh, you wanna see my tattoo, hey? You're wondering where it is aren't you? Have a guess."
        mc "On your huge clitoris?"
        hide rubyflex
        show ruby07
        with fastdissolve
        ru "What the fuck? No, you moron!"
        hide ruby07
        scene workshop03 blurred
        show rubytits01
        with fastdissolve
        ru "It's on my right breast...Just below my nipple stud... You wanna suck on it big boy?"
        menu:
            "What? Err... No thanks.":
                hide rubytits01
                scene workshop03
                show ruby08
                with fastdissolve
                ru "Ah, ah, you're too old to suck on a woman's milkbags, hey? I get it, you want to pass off as a REAL man."        
                hide ruby08
                jump WorkshopRubyMenu01
            "Of course! And fondle those massive tits too!":
                ru "You can't, no touching, just your tongue on my nipple..."
                hide rubytits01
                show rubytits02
                with fastdissolve
                ru "There you go, just suck on it, play with your tongue..."
                hide rubytits02
                show rubytits03
                with fastdissolve
                ru "Oooh, I feel... so turned on..."
                hide rubytits03
                show rubytits04
                with fastdissolve
                ru "Enough now... You got my nipples all hard... Naughty boy..."
                call LustPlusRuby
                $ spokeruby01 = True
                ru "I'd better get my top back on before someone sees us..."
                hide rubytits04 with dissolve
                jump WorkshopRubyMenu01
    "Road Warriors are bad asses. How do I become one?" if spokeruby01 and spokeruby03 == False and mcwarrior <= 4:
        $ spokeruby03 = True
        hide ruby01
        show rubyflex
        with fastdissolve
        ru "You've got be a badass like us. Shooting camels is badass. I hate those godamn animals."
        mc "How many would do?"
        hide rubyflex
        show ruby04
        with fastdissolve
        ru "I don't know but A LOT. Like maybe one extra Road Warrior point for every ten camels shot."
        mc "Thanks for the info."
        hide ruby04
        jump WorkshopRubyMenu01
    "I'd like to become better at handling firearms.":
        if period == 3:
            hide ruby01
            show ruby07
            with fastdissolve
            ru "Sorry, can't shoot in the evenings. It's too dark..."
            hide ruby07
            jump WorkshopRubyMenu01            
        hide ruby01
        show ruby05
        with fastdissolve
        ru "No problemo! Let's head to the shooting range."
        jump ShootingRange
    "I would like to gift you a beautiful necklace that I found on my adventures." if necklace:
        hide ruby01
        show rubyflex
        ru "A necklace? That's... for girls."
        mc "Well, you are a girl."
        ru "But I'm a TOUGH girl! A ROAD WARRIOR!"
        mc "Well road warriors need ornaments too, this one is from the jungle, I had to beat up someone to get it, the Road Warrior way if you like..."
        hide rubyflex
        show ruby06 
        with fastdissolve
        ru "Interesting... Let's see your pussy-boy necklace then, I'll TRY it on just to see..."
        hide ruby06
        show rubynecklace
        with fastdissolve
        ru "It's okay I guess, kind of a nice change from my army tag... But I'll wear it only... in private."
        $ necklace = False
        call LustPlusRuby
        ru "OK, now I have to go and see what I can do with this necklace to make it... less feminine."
        mc "Sure. You do that, tough girl."
        scene workshop01 with dissolve
        $ spokeruby01 = True
        $ period += 1
        jump Main01
    "I would like to invite you on a date with me." if lustru >= 2 and rubydatedone == False and knowredcanyon and spokeruby02 == False:
        if knowrubytip:
            hide ruby01
            show ruby06
            with fastdissolve
            ru "That sounds... girly."
            mc "Not with me around. It will be MANLY."
            hide ruby06
            show rubyflex
            with fastdissolve
            ru "A manly date? Alright, I'm in! You'd better not disappoint me, big boy."
            $ rubydateon = True 
            $ spokeruby02 = True
            hide rubyflex
            jump WorkshopRubyMenu01        
        if knowrubytip == False:
            hide ruby01
            show ruby06
            with fastdissolve
            ru "That sounds... girly, mate."
            mc "Yeah, but I'll show you some MAN-love."
            hide ruby06
            show ruby07
            with fastdissolve
            ru "Man-love? Do I look like a poof to you?"
            mc "Err..no. What's a poof?"
            ru "Get out of here, poofter!"
            hide ruby07 with dissolve
            mc "Well, that didn't go well. I wonder what I did wrong? Normally, her lust is high enough and I know about the Red Canyon..."
            mc "Perhaps I should ask Marnie... She always has good tips."
            $ period += 1
            mc "And I just wasted one full period thinking aloud in the workshop. Damn it."            
            jump Main01            
    "I think I'm strong enough now for you to join my harem Ruby..." if lustru >= 4 and haremru == False and rubyharem == False and mcstrength >= 9 and girlsinharem <= 5 and rubydatedone:
        ru "I'll be the judge of that... Lift me up in one arm and prove it to me..."
        scene workshop03 blurred
        show rubylift01
        with dissolve
        ru "You DEFINITELY ARE [name]!"
        $ haremru = True
        $ girlsinharem += 1
        $ rubyharem = True
        window hide
        show haremruby at plus
        $ renpy.pause(2.0, hard=True)
        hide haremruby
        mc "I'll call you at nights, so I can show you one of my most spectacular muscles... *wink*"
        ru "And I'll show you how my pussy muscles handle your beast!"
        hide rubylift01 with dissolve
        jump WorkshopRubyMenu01
    "I think it's time for you to re-join my harem Ruby..." if lustru >= 4 and haremru == False and rubyharem and mcstrength >= 9 and rubydismissed == False and girlsinharem <= 5:
        ru "I'll be the judge of that... Show me that you're STILL strong enough to lift me up in one arm..."
        scene workshop03 blurred
        show rubylift01
        with dissolve
        ru "Alright, I agree then, [name]!"
        $ haremru = True
        $ girlsinharem += 1
        window hide
        show haremruby at plus
        $ renpy.pause(2.0, hard=True)
        hide haremruby
        mc "I'll call you at nights, so we can have some more fun with my MOST spectacular muscle!"
        ru "And I'll show you how my pussy muscles handle your beast!"
        hide rubylift01 with dissolve
        jump WorkshopRubyMenu01
    "I'd like to show you something (hypnotize her, +1 lust)" if pendulum and showedpendulum == False:
        scene workshop03 blurred
        show ruby01 
        with dissolve
        call UsePendulum
        ru "Wh...what happened... Oh, hi [name], you look... buff today..."
        call LustPlusRuby
        hide ruby01
        show ruby06 
        with fastdissolve
        $ showedpendulum = True
        ru "Err... I don't know why I said that, your muscles are nothing to brag about compared to mine ACTUALLY."
        scene workshop01 with dissolve
        $ spokeruby01 = True
        $ period += 1
        jump Main01
    "Leave":
        ru "You're scared, admit it, you're scared."
        hide ruby01 with dissolve
        jump Workshop

    
label ShootingRange:
scene shooting01 with dissolve
show ruby05
ru "Here's a rifle. Handle it with care and choose wisely who you shoot, this training might influence your faction points..."
if persistent.tipson and mushroomoffered == False:
    show shoottip at tips with dissolve
    pause
    hide shoottip
hide ruby05
with dissolve
scene shooting02 with dissolve
if (shottrumpf - shotclinton) == 0:
    pass
if (shottrumpf - shotclinton) == 1:
    show trumpf01
if (shottrumpf - shotclinton) == 2:
    show trumpf02
if (shotclinton - shottrumpf) == 1:
    show clinton01
if (shotclinton - shottrumpf) == 2:
    show clinton02

menu:
    "Shoot Trumpf":
        play sound "Sounds/gun.mp3"
        $ renpy.pause(0.5, hard=True)
        show bullettrump01 with dissolve
        ru "Yeah, right between the eyes, shoot him some MORE. Yee-HAW!"
        hide bullettrump01
        show bullettrump
        $ shottrumpf += 1
        if (shottrumpf - shotclinton) == -1:
            hide clinton02
            show clinton01
        if (shottrumpf - shotclinton) == 0:
            hide clinton01
        if (shottrumpf - shotclinton) == 1:
            show trumpf01
        if (shottrumpf - shotclinton) == 2:
            hide trumpf01
            show trumpf02
        if (shottrumpf - shotclinton) == 3:
            hide trumpf02
            show trumpf03
            call MinusTrumpster
            call PlusDeep
            $ shottrumpf = 0
            $ shotclinton = 0
            hide trumpf03
    "Shoot Clit-On":
        play sound "Sounds/gun.mp3"
        $ renpy.pause(0.5, hard=True)
        show bulletclinton01 with dissolve
        ru "Yeah, right between the eyes, shoot her some MORE. Yee-HAW!"
        hide bulletclinton01
        show bulletclinton
        $ shotclinton += 1
        if (shotclinton - shottrumpf) == -1:
            hide trumpf02
            show trumpf01
        if (shotclinton - shottrumpf) == 0:
            hide trumpf01
        if (shotclinton - shottrumpf) == 1:
            show clinton01
        if (shotclinton - shottrumpf) == 2:
            hide clinton01
            show clinton02
        if (shotclinton - shottrumpf) == 3:
            hide clinton02
            show clinton03
            call MinusDeep
            call PlusTrumpster
            $ shotclinton = 0
            $ shottrumpf = 0
            hide clinton03
show ruby08 with dissolve
stop sound
ru "OK, that's the end of your training."
$ mcfirearmslevel += 1
if mcfirearmslevel == 1:
#    call Levelup01
    mc "A couple more sessions shooting at our political leaders and I should get better at this!"   
if mcfirearmslevel == 2:
#    call Levelup02
    mc "Another session shooting at our political leaders and I should get better at this!"   
if mcfirearmslevel == 3:
#    call Levelup03
    mc "Damn, I feel closer to... Robert de Niro in Taxi Driver suddenly."
    call PlusFirearms
    $ mcfirearmslevel = 0
$ seenworkshop = True
if mcfirearms >= 3 and nranramember == False:
    ru "You're getting good at this [name]... You might want to consider joining the NRANRA..."
    menu:
        "Join the NRANRA ($20 membership fee, +1 Ruby lust)" if money >= 20:
            $ money -= 20
            window hide
            show nranramember at posmission
            $ renpy.pause(0.5, hard=True)
            pause
            hide nranramember
            hide ruby08
            show ruby05
            with fastdissolve
            ru "I'm proud of you. Now you can shoot anything or anyone and get completely exonerated."
            $ nranramember = True
            call LustPlusRuby
        "No way!":
            hide ruby08
            show ruby07
            with fastdissolve
            ru "Grumpf... SNOWFLAKE!"      
$ period += 1
jump Main01

label LeaveWorkshop:
if spokeamy or spokeruby:
    $ period +=1
    $ seenworkshop = True
jump Main01

label HippyEvening:
scene mcbikeevening with fade
if seenhippiesevening == False:
    mc "Off to see those hippie chicks at last!"
if seenhippiesevening:
    mc "Off to see those hippie chicks again!"
window hide
play sound "Sounds/explorepenny02.mp3"
pause 2

scene hippyevening01 with fade
stop sound
mc "There they are. Still haven't got a clue I guess."
scene hippyevening02
show stellaevening01b at left
show livieevening01 at right
with dissolve
if seenhippiesevening == False:
    st "Oh, hi there! We haven't seen you in such a LONG time!"
    li "And you didn't bring that fascist girl with you this time, so you can join us for our pre-Burning Man own mini-festival!"
if seenhippiesevening:
    st "Oh, hi [name]! We haven't seen you in such a LONG time!"
    li "Yeah, it feels like AGES since you last came to visit."
    mc "It wasn't THAT long ago really..."
    li "Stella, get the ganja out, I feel like I need some more to stay in my eternal trip..."
hide stellaevening01b
show stellaevening02b
with fastdissolve
st "Oh yeah, I forgot about that! Let me get the ganja stock out of the trunk!"
hide stellaevening02b with moveoutleft
li "Cool dude."
if seenhippiesevening == False:
    mc "I'm [name] by the way."
if seenhippiesevening:
    mc "You're gonna play th eguitar again?"
hide livieevening01
show livieevening02 at right
with dissolve
if seenhippiesevening == False:
    li "And I'm Livie. Let's go and sit around the campfire.... [name]."
if seenhippiesevening:
    li "Yeah, I'll go and get it, sit down and get ready for another SEXY evening..."
hide screen calendar
hide screen mcstats
scene hippyfire01 with dissolve
li "So... Tell us all about your adventures while Stella rolls a big fat joint and I'll go and grab my guitar..."
mc "Well, you know, I'm the HERO here, so I saved many people and I could bang on and on for..."
scene hippyfire02 with dissolve
mc "...hours about all my exploits and all the weirdos I met along the..."
st "Oh, shut up! Play something Livie. Something relaxing."
play music "Sounds/hippies.mp3"
st "I LOVE that song... I'm gonna get ssooo stoned on it."
scene hippyfire03 with dissolve
$ renpy.pause(2.0, hard=True)
scene hippyfire02 with dissolve
$ renpy.pause(1.0, hard=True)
mc "I'll have some too please..."
mc "Oh man, I'm tripping now..."
window hide
scene hippyfire03 with psych01
$ renpy.pause(1.0, hard=True)
scene hippyfire02 with psych02
$ renpy.pause(1.0, hard=True)
scene hippyfire03 with psych01
$ renpy.pause(1.0, hard=True)
scene hippyfire02 with circleirisout
$ renpy.pause(1.0, hard=True)
mc "Psychedelic dude, I'm seeing things.... That ganja is strong."
call PlusSierra
stop music
scene hippykiss01 with psych01
$ renpy.pause(1.0, hard=True)
mc "Oh wow, when did that just happen?"
play sound "Sounds/kiss.mp3"
st "Mmmh..."
play sound "Sounds/womanmoan.mp3"
li "Are you out of your trip, [name]? Why don't you come and join us..."
mc "Oh yeah. What, I'm already naked too? Cool, dude, I don't have to take my clothes off then."
scene hippykiss02 with dissolve
play sound "Sounds/kiss.mp3"
st "Your cock is sssooo BIG! I want it..."
mc "Then come and get it..."
scene hippykiss03 with dissolve
play sound "Sounds/lick.mp3"
st "Like that?"
li "Oooh, I can sense you TREMBLING with anticipation, [name]..."
st "I want to FUCK! Sex is way better when you're totally stoned..."
mc "AAAh, yeah, sure... I'll fuck you... Where am I?"
scene hippiefuckbackground03
show hippyprefuck01
with dissolve
mc "Are you ready girl?"
st "Oh, you aren't in yet? I thought you were. Man, I'm so stoned..."
scene hippiefuckbackground01
show hippiesex00
with fastdissolve
play sound "Sounds/moaning.mp3"
st "AAAH! Now I'm really SURE you're in!"
hide hippiesex00
play music "Sounds/womansex01.mp3"
label HippyFuckaSlow:
show hippyfuck01slow
hide hippyfuck01fast
call screen hippyfuckaslow
screen hippyfuckaslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HippyFuckaEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("HippyFuckaFast")     

label HippyFuckaFast:
st "Oooh, fuck me faster, cos right now, everything feels ssooo slow..."
show hippyfuck01fast
hide hippyfuck01slow
call screen hippyfuckafast
screen hippyfuckafast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HippyFuckaEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("HippyFuckaSlow")     

label HippyFuckaEnd:
mc "Oh, I feel like... I'm going to..."
stop music
hide hippyfuck01fast
hide hippyfuck01slow
show hippiefuckcum01
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...CU-UM!!!! AAAH!"
st "AAAH, I'm cumming too with your horsecock lodged sssooo DEEP inside me!"
hide hippiefuckcum01
show hippiefuckcum02
with dissolve
mc "RHAAA! Let me plaster your back with my teenage scum! SSSOOO GOOOD!"
scene hippiefuckbackground02
show hippiefuckcum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
st "Please put it back inside me, I want the rest sloshing aroung in my WOMB!"
scene hippiefuckbackground03
show hippiefuckcum04
with dissolve
mc "Alright, here it comes, the last of my cum-salvoes! AAAH"
li "OOoh, I missed out on sssooo much cum..."
mc "Don't worry Livie, I'm still ROCK-HARD and RARING TO GO!"
scene hippiefuckbackground02
show hippyprefuck02
with dissolve
mc "Just let yourself slide down that shaft, Livie..."
st "Looks like there's a LOT of inches to slide down onto!"
li "I'm so stoned I actually think I can do it..."
mc "Time to PROVE IT!"
hide hippyprefuck02
play music "Sounds/womansex02.mp3"
label HippyFuckbSlow:
show hippyfuck02slow
hide hippyfuck02fast
call screen hippyfuckbslow
screen hippyfuckbslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HippyFuckbEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("HippyFuckbFast")     

label HippyFuckbFast:
li "I LOVE bouncing up and down your fat boymeat!"
show hippyfuck02fast
hide hippyfuck02slow
call screen hippyfuckbfast
screen hippyfuckbfast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HippyFuckbEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("HippyFuckbSlow")     

label HippyFuckbEnd:
li "Come inside me please! I want it, I want your LOAD!"
mc "AAAH, here it comes BLASTING, Livie!"
stop music
hide hippyfuck02slow
hide hippyfuck02fast
show hippiesex02cum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
li "Ooh, it's pumping inside my womb like a firehose! SSSOOO MUCH SWEET YOUNG CUM! MORE!"
show hippiesex02cum01 with fastflash
play music "Sounds/splooge02.mp3"
mc "There's more where that came from!"
li "Show me, GIVE ME MORE!"
hide hippiesex02cum01
show hippiesex02cum02
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "There, FUCKING CU-UU-MMING!"
st "Look at how POWERFUL he blasts his spunk all over your back! Just like he did with me... What a STALLION!"
li "I'm cumming too! AAAH! And cum is still pouring out of my overfilled snatch!"
scene hippiefuckbackground03
show hippiesex02cum03
with dissolve
mc "Phew! Ladies, I think I should go... I don't know how I'll ride back home cos I don't even know where is home but it ain't here and they'll be looking for me if I don't go back..."
st "What? To that place with the fascist girls? Why don't you stay with us..."
mc "Sorry, I'll come back, I  promise, but I need to go..."
li "Let's get dressed then, I'm getting tired anyway, smoked waaaayyy too much dope..."

$ seenhippiesevening = True
show screen calendar
show screen mcstats
scene hippyevening02
show stellaevening01b at left
show livieevening01 at right
with dissolve
st "Bye [name]!"
hide livieevening01
show livieevening02 at right
with fastdissolve
li "[name] who? Oh, that guy. Dude, I need some more ganja... Give him one for the road too."
$ spliff = True
window hide
show spliff at posmission
$ renpy.pause(4.0, hard=True)
hide spliff
mc "That could become handy one day... Thanks, I'm off now. But I'll be back..."
play sound "Sounds/explorepenny02.mp3"
pause 2
$ period +=1
jump Bedroom

