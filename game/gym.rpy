label Gym:
$ loc = "gym"
$ d6rollgym=renpy.random.randint(1,6)
stop music
if d6rollgym == 1:
    $ lenagym = True
if d6rollgym == 2:
    $ aylagym = True
if d6rollgym == 3 and preglastart >= 3:
    jump Gym
if d6rollgym == 3:
    $ lauriegym = True
if d6rollgym == 4:
    $ rubygym = True
if d6rollgym == 5 and (period == 3 and (day == 5 or day == 6)):
    jump Gym
if d6rollgym == 5:
    $ marniegym = True
if d6rollgym == 6 and (momcompound == False or pregmostart >= 3):
    jump Gym
if d6rollgym == 6 and momcompound:
    $ momgym = True

label Gym01b:
scene gym01 with fade
label GymMenu01:
call screen gym01
screen gym01:
    modal True    
    if lauriegym:
        imagebutton:
            focus_mask True
            idle "Gym/lauriegymidle.png"
            hover "Gym/lauriegymhover.png"
            action Jump ("LaurieGym")    
    imagebutton:
        focus_mask True
        idle "Icons/exitleftidle.png"
        hover "Icons/exitlefthover.png"
        action Jump ("GymOut")
    imagebutton:
        focus_mask True
        idle "Gym/gymmachine01idle.png"
        hover "Gym/gymmachine01hover.png"
        action Jump ("GymWorkout01")
    if lenagym:
        imagebutton:
            focus_mask True
            idle "Gym/lenagymidle.png"
            hover "Gym/lenagymhover.png"
            action Jump ("LenaGym")    
    if aylagym == True and aylagymout == False:
        imagebutton:
            focus_mask True
            idle "Gym/gymaylaidle.png"
            hover "Gym/gymaylahover.png"
            action Jump ("AylaGym")    
    if rubygym:
        imagebutton:
            focus_mask True
            idle "Gym/gymrubyidle.png"
            hover "Gym/gymrubyhover.png"
            action Jump ("RubyGym")
    if momgym:
        imagebutton:
            focus_mask True
            idle "Gym/gymnancyidle.png"
            hover "Gym/gymnancyhover.png"
            action Jump ("NancyGym")
    if marniegym:
        imagebutton:
            focus_mask True
            idle "Gym/gymmarnieidle.png"
            hover "Gym/gymmarniehover.png"
            action Jump ("MarnieGym")

label GymWorkout01:
show screen mcstats
$ seengym = True
scene machine01 with dissolve
mc "Let's pump iron! I want my guns to get even bigger and stronger!"
window hide
if lauriegym and seenlauriegym == False:    
    if mcstrength <= 9 or posingpouch == False:
        show lauriegym01 with dissolve
        la "Can I watch you [name]? I'm done with my yoga exercise..."
        mc "Of course Laurie. I'm gonna power-lift the heaviest set of weights you've ever seen in your life!"
        la "Wow... I can't wait to see that! (wink)"
        hide lauriegym01 with dissolve
    if mcstrength >= 10 and posingpouch:
        show lauriegym13 with dissolve
        la "I was about to leave but... May I stay and watch you lift [name]?"
        mc "Of course Laurie. I'm lifting even more than usual today. I feel so STRONG!!"
        la "Mmh, I can't wait to see THAT. And for your muscles to be all PUMPED-UP!"
        hide lauriegym13 with dissolve
    jump GymWorkout01b
if lenagym and seenlenagym == False:    
    show lenagym02 with dissolve
    le "Here again [name]? That's good, we need you to become the STRONGEST and BUFFEST MAN on the planet!"
    mc "I already am but I'll get even MORE MASSIVE for you Chief Lena!"
    le "Now that's what I like to hear..."
    hide lenagym02 with dissolve
    jump GymWorkout01b
if rubygym and seenrubygym == False:
    show rubygym01 with dissolve
    ru "Here again [name]? Trying to buff up? Let's see what you've got..."
    mc "I'm sure you'll be impressed Ruby!"
    ru "I'll be the judge of that..."
    hide rubygym01 with dissolve
    jump GymWorkout01b
if marniegym and seenmarniegym == False:
    show marniegym02 with dissolve
    ma "Oh, you're going to train [name]? I might watch you for a while, I want to see what your technique is."
    mc "My technique is PURE RAW POWER."
    ma "Well, let's see how POWERFUL you are then!"
    hide marniegym02 with dissolve
    jump GymWorkout01b
if aylagym and seenaylagym == False and lustay >=2:
    show aylagym02 with dissolve
    ay "Oh, hi [name]... I might stay around for a little while. Only cos I'm so BORED and watching you lifting heavy weights is slighty better than watching paint dry."
    mc "Sure Ayla, you watch and you'll get AMAZED by my SUPER-STRENGTH!"
    ay "I very much doubt it but we'll see..."
    hide aylagym02 with dissolve
    jump GymWorkout01b
if momgym and seenmomgym == False and lustmo >=2:
    show nancygym02 with dissolve
    mo "Oh, hello [name]... I might stay around for a little while. I want to see my SUPER-STRONG man show off how powerful he is."
    mc "You'll see Nancy, I'm taking the heaviest set around just for you!"
    mo "Ooh, I can't wait to see that..."
    hide nancygym02 with dissolve
    jump GymWorkout01b

label GymWorkout01b:
if mcstrength >= 10 and posingpouch:
    mc "(And since I'm getting SUPER-STRONG, time to kick it up a notch and train in my sexy posing pouch to impress the girls...)"
    $ workoutmax = True
    play music "Sounds/mcworkout.mp3"
    show mcgym01b
    call screen mcgymb
    screen mcgymb:
        modal True
        button:
            imagebutton:
                focus_mask True
                idle "Icons/nextidle.png"
                hover "Icons/nexthover.png"
                action Jump ("GymWorkoutEnd01b")        

play music "Sounds/mcworkout.mp3"
show mcgym01
call screen mcgym
screen mcgym:
    modal True
    button:
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("GymWorkoutEnd01")    

label GymWorkoutEnd01:
stop music
scene machine01 with dissolve
mc "Damn, that was a good workout! I need to POSE and FLEX those muscles!"
$ d3rollgymworkout = renpy.random.randint(1, 3)
if d3rollgymworkout == 1:
    scene gymposing01 with dissolve
    mc "Check those ripped muscles! I'm da man, I'm DA MAN!"
if d3rollgymworkout == 2:
    scene gymposing02 with dissolve
    mc "Fuck yeah! Monster teen muscle stud right here!"
if d3rollgymworkout == 3:
    scene gymposing03 with dissolve
    mc "Damn, my muscles are definitely getting BIGGER and STRONGER!"
$ mcstrengthlevel += 1
if mcstrengthlevel == 1:
    mc "A couple more workouts like this one and I'll get STRONGER for sure!"   
if mcstrengthlevel == 2:
    mc "I need another workout like this one and I'll get STRONGER for sure!"   
if mcstrengthlevel == 3:
    mc "Damn, my muscles are definitely getting BIGGER and STRONGER!"
    call PlusStrength
    $ mcstrengthlevel = 0
if marniegym and gymma == 0:
    $ gymma += 1
    scene gym03
    show marniegym02
    ma "Your eight-packs were indeed RIPPLING during that routine."
    mc "I hope you appreciated their awesome POWER..."
    ma "I did [name], I did..."
    if marnieplusgym == False:
        call LustPlusMarnie
        $ marnieplusgym = True
    mc "So, what are doing next Marnie?" 
    hide marniegym02
    show marniegym01
    with fastdissolve
    ma "I need to go back and man the bar. There are people drinking at all times of the day..."
    mc "I'll probably see you there later myself, I'm thirsty... for YOU!"
    ma "Well, what a charmer... See you later [name]!"
    hide marniegym01 with dissolve
    $ renpy.pause(.2, hard=True)
    jump GymOut
if marniegym and gymma >= 1:
    $ gymma += 1
    scene gym03
    show marniegym01
    ma "I didn't notice any difference with last time."
    mc "I'm getting stronger every week!"
    hide marniegym01
    show marniegym02
    with fastdissolve
    ma "Well, good for you. But neither your muscles nor your cock are noticeably growing... I'm going back to the bar now [name]..."
    hide marniegym02 with dissolve
    $ renpy.pause(.2, hard=True)
    jump GymOut
if momgym and gymmo == 0:
    $ gymmo += 1
    scene gym03
    show nancygym03
    mo "I'm so proud of you [name]! You must be the STRONGEST man on the planet!"
    mc "Damn right Nancy! And I'll protect you from anyone who tries to kidnap you and sell you as a sex slave, I swear!"
    hide nancygym03
    show nancygym02
    with fastdissolve
    mo "I feel so SAFE with you around, you really have become the MAN of the house!"
    if momplusgym == False:
        call LustPlusNancy
        $ momplusgym = True
    mo "I'm off to take a shower now. And recover from all these EMOTIONS..."
    menu:
        "Go and take a shower":
            mc "Yeah, now that I'm all pumped up, I'll go and take a PUMPED-UP shower too!"
            mo "Well that's great to hear sweetie..."
            hide nancygym02 with dissolve
            jump GymOut            
        "Ask her to join your harem" if lustmo >= 4 and haremmo == False and momharem == False and girlsinharem <= 5:
            mc "Hang on a minute Nancy... I think it's time that you... joined my harem."
            hide nancygym02
            show nancygym01
            with dissolve
            mo "Really? You want your old landlady in your HAREM?"
            mc "Well, yeah, I mean, you're still young and... err... fertile, so you can join my harem, no problem."
            hide nancygym01
            show nancygym03
            with fastdissolve
            mo "We probably shouldn't be telling anyone about it, but I'll gladly be your... harem girl, my sweet young man!"
            $ haremmo = True
            $ momharem = True
            $ girlsinharem += 1
            window hide
            show haremnancy at plus
            $ renpy.pause(2.0, hard=True)
            hide haremnancy
            mc "Then I'll see you... discreetly later on Nancy!"
            mo "Of course [name]! I can't wait to meet you \"in private\"."
            hide nancygym03 with dissolve
            mc "And I'll go and take a shower to get squeaky-clean for our future roomies romp!"
            jump GymShower            
        "Hypnotize her (+1 lust)" if pendulum and showedpendulum == False:
            call UsePendulum
            hide nancygym02
            show nancygym01
            with dissolve
            mo "Ooh, I don't know what's happening to me but I feel so... nice inside."
            call LustPlusNancy
            hide nancygym01
            show nancygym03
            with fastdissolve
            mo "I'll go and take a shower now sweetie, bye!"
            $ showedpendulum = True
            hide nancygym03 with dissolve
            mc "I might as well do the same..." 
            jump GymShower    
    hide nancygym02 with dissolve
    mc "I'll do the same. Can't wait for that landlady dream sequence that's bound to take place."
    jump GymShower
if momgym and gymmo >= 1:
    $ gymmo += 1
    scene gym03
    show nancygym03
    mo "Every time I see you training in the gym, you seem to be getting STRONGER [name]! I'm ssooo proud of you!"
    mc "Don't you think I deserve a reward for that Nancy?"
    hide nancygym03
    show nancygym02
    with fastdissolve
    mo "Oh, you want a kiss from your old landlady? Come here my sweet man."
    mc "(Actually, I wanted something else, but okay, I'll take it. I mean, a bit of landlady-tenant romanticism never killed a porn game, right?)"
    hide nancygym02
    show nancygym04
    with fastdissolve
    play sound "Sounds/kiss.mp3"
    mo "*kiss* See you later sweetie!"
    menu:
        "Go and take a shower":
            mc "Yeah, now that I'm all pumped up, I'll go and take a PUMPED-UP shower!"
            mo "Well that's great to hear sweetie... I'll go and take a shower myself. In the girls' shower room of course."
            hide nancygym02 with dissolve
            jump GymShower            
        "Ask her to join your harem" if lustmo >= 4 and haremmo == False and momharem == False and girlsinharem <= 5:
            mc "Hang on a minute Nancy... I think it's time that you... joined my harem."
            hide nancygym04
            show nancygym01
            with dissolve
            mo "Really? You want your old landlady in your HAREM?"
            mc "Well, yeah, I mean, you're still young and... err... fertile, so you can join my harem, no problem."
            hide nancygym01
            show nancygym03
            with fastdissolve
            mo "We probably shouldn't be telling anyone about it, but I'll gladly be your... harem girl, my sweet young man!"
            $ haremmo = True
            $ momharem = True
            $ girlsinharem += 1
            window hide
            show haremnancy at plus
            $ renpy.pause(2.0, hard=True)
            hide haremnancy
            mc "Then I'll see you... discreetly later on Nancy!"
            mo "Of course [name]! I can't wait to meet you \"in private\"."
            hide nancygym03 with dissolve
            mc "And I'll go and take a shower to get squeaky-clean for our future roomies romp!"
            jump GymShower            
        "Hypnotize her (+1 lust)" if pendulum and showedpendulum == False:
            call UsePendulum
            hide nancygym04
            show nancygym01
            with dissolve
            mo "Ooh, I don't know what's happening to me but I feel so... nice inside."
            call LustPlusNancy
            hide nancygym01
            show nancygym03
            with fastdissolve
            mo "I'll go and take a shower now sweetie, bye!"
            $ showedpendulum = True
            hide nancygym03 with dissolve
            mc "I might as well do the same..." 
            jump GymShower
    hide nancygym04 with dissolve
    mc "I'll go and take a shower now. Can't wait for that landlady dream sequence that's bound to take place."
    jump GymShower
if rubygym and gymru == 0:
    $ gymru += 1
    scene gym03
    show rubygym01
    ru "Wow, you really ARE strong [name]... I'm sorry I doubted you... Mmmh, that young muscled body of yours..."
    if rubyplusgym == False:
        call LustPlusRuby
        $ rubyplusgym = True
    ru "If I wasn't so butch, I'd almost jump your bone right here, right now..."
    mc "You can jump it anyways, I don't care!"
    hide rubygym01
    show rubygym03
    with fastdissolve
    ru "Not now, I have to go back to the workshop to finish some manly stuff."
    hide rubygym03 with dissolve
    mc "Damn it!"
    jump GymOut
if rubygym and gymru >= 1:
    $ gymru += 1
    scene gym03
    show rubygym01
    ru "I see, I have to train EVEN MORE to become as strong as you... And then STRONGER so I'll beat you!"
    mc "Keep dreaming!"
    hide rubygym01
    show rubygym03
    with fastdissolve
    ru "We'll see... In the meantime you stay standing there in your stupid underpants while I go back to the workshop to finish some manly stuff!"
    hide rubygym03 with dissolve
    $ renpy.pause(.2, hard=True)
    jump GymOut
if lauriegym and gymla == 0:
    $ gymla += 1
    scene gym04 with dissolve
    show lauriegym02
    la "I... can't believe what I just saw. You did it with such ease! Sssoo strong..."
    if laurieplusgym == False:
        call LustPlusLaurie
        $ laurieplusgym = True
    mc "Err. Is it me or your tits grew? And your nipples... They're HUGE now!"
    hide lauriegym02
    show lauriegym03
    with fastdissolve
    la "Oh my God, this is so embarrassing... The... mutated salads... make my tits grow bigger when I'm horny. Oh no, I just said it!"
    hide lauriegym03
    show lauriegym04
    with fastdissolve
    la "I'm so ashamed... Please don't tell anyone... I... I need to go now [name]..."
    hide lauriegym04 with dissolve
    $ renpy.pause(.2, hard=True)
    jump GymOut
if lauriegym and gymla >= 1:
    $ gymla += 1
    scene gym04 with dissolve
    show lauriegym02
    la "Wow, you sure are getting BIGGER every time I see you..."
    mc "Your nipples are too..."
    hide lauriegym02
    show lauriegym03
    with fastdissolve
    la "Oh no, not again... I... just can't help it...."
    mc "Don't worry about it, I don't mind..."
    hide lauriegym03
    show lauriegym04
    with fastdissolve
    la "You're so nice to take it like that but I am REALLY ashamed... I... I need to go now [name]..."
    hide lauriegym04 with dissolve
    $ renpy.pause(.2, hard=True)
    jump GymOut
if lenagym and gymle == 0:
    $ gymle += 1
    scene gym02 with dissolve
    show lenagym02
    le "Mmh, you sure are strong [name]. But not strong enough. Train some more... As much as possible."
    hide lenagym02
    show lenagym03
    with fastdissolve
    le "Here, I'm offering you a new pair of posing pouches to make it \"easier\" for you to pump iron..."
    window hide
    show sexypouch at posmission
    $ renpy.pause(2.0, hard=True)
    pause
    hide sexypouch
    $ posingpouch = True
    le "Now if you'll excuse me, duty calls."
    hide lenagym03 with dissolve
    $ renpy.pause(.2, hard=True)
    jump GymOut
if lenagym and gymle == 1:
    $ gymle += 1
    scene gym02 with dissolve
    show lenagym02
    le "I sure wish Jake was built like you are."
    mc "Which means... built like... what?..."
    hide lenagym02
    show lenagym03
    with fastdissolve
    le "You want me to say it? Alright. BUILT LIKE A MUSCLE STUD."
    if lenaplusgym == False:
        call LustPlusLena
        $ lenaplusgym = True
    mc "That's right, and I'll get even bigger for you Chief Lena!"
    le "I don't doubt it, but I have to go back to the command center now..."
    hide lenagym03 with dissolve
    $ renpy.pause(.2, hard=True)
    jump GymOut
if lenagym and gymle >= 2:
    $ gymle += 1
    scene gym02 with dissolve
    show lenagym02
    le "I can see that you are getting even MORE muscular every week. That is excellent news, we need you as strong and built as possible to defeat Trumpf and his minions..."
    mc "I'll break them apart with my little finger Chief Lena!"
    hide lenagym02
    show lenagym01
    with fastdissolve
    le "Well, for that you also have to train at close combat I remind you..."
    mc "I'm doing that... Every now and then..."
    le "I have to go back to the command center now, duty calls..."
    hide lenagym03 with dissolve
    $ renpy.pause(.2, hard=True)
    jump GymOut
if aylagym == True and aylagymout == False and lustay <= 2:
    $ gymay += 1
    scene gym05 with dissolve
    show gymayla01
    ay "My boyfriend wans't a stupid bodybuilder on steroids, so watching you didn't bring back any fond memories whatsoever. It was BORING."
    mc "But... My HUGE muscles..."
    hide gymayla01
    show gymayla02
    with fastdissolve
    ay "Whatever. BORING."
    hide gymayla02 with dissolve
    $ renpy.pause(.2, hard=True)
    jump GymOut
if aylagym == True and aylagymout == False and lustay >= 3:
    $ gymay += 1
    scene gym05 with dissolve
    show gymayla03
    ay "It was... interesting... Maybe my boyfriend should get into this when I find him again..."
    if aylaplusgym == False:
        call LustPlusAyla
        $ aylaplusgym = True
    ay "I'll... think about it some more tonight in my bed..."
    hide gymayla03 with dissolve
    mc "Hey, don't go yet! We have so much in...err... common!"
    jump GymOut
jump GymOut

label GymWorkoutEnd01b:
stop music
scene mcliftend01 with dissolve
mc "That was an INTENSE workout and I feel so fucking STRONG and BUFF! I need to flex those muscles NOW!"
scene mcliftend02
show mcflexmax at centerright
with dissolve
$ mcstrengthlevel += 1
if mcstrengthlevel == 1:
    mc "A couple more workouts like this one and I'll get STRONGER for sure!"   
if mcstrengthlevel == 2:
    mc "I need another workout like this one and I'll get STRONGER for sure!"   
if mcstrengthlevel == 3:
    mc "Damn, my muscles are definitely getting BIGGER and STRONGER!"
    call PlusStrength
    $ mcstrengthlevel = 0
if marniegym and marniemax and gymma >= 5:
    $ gymma += 1
    window hide
    show marniegym04 at left with moveinleft
    ma "Still as IMPRESSIVE as ever [name]!"
    mc "For sure Marnie, getting STRONGER and BIGGER all the time!"
    ma "Sure but... what about that OTHER muscle of yours? Is it getting STRONGER and BIGGER?"
    mc "Check it out yourself Marnie, you know you want to..."
    hide marniegym04
    hide mcflexmax
    show mcflexmaxmarnie03
    with dissolve
    play sound "Sounds/gasp.mp3"
    ma "Oh, it sures feels like it's getting BIGGER... But how much STRONGER I wonder?"
    mc "STRONG enough to CARRY YOU on it I reckon!"
    ma "Let's test this theory of yours then... Pull it out and show me!"
    hide mcflexmaxmarnie03
    show mcflexmaxmarnie04
    with dissolve
    ma "It's sticking out between my thighs like a battering ram. Now TRY and lift me with it..."
    mc "Sure, turn round, I want to see your face when I do..."
    hide mcflexmaxmarnie04
    show mcflexmaxmarnie05
    with dissolve
    ma "Mmmh, it looks like you might have been right... Can you flex it so I can make sure it's not a trick?"
    mc "Sure. Here you go."
    hide mcflexmaxmarnie05
    show mcflexmaxmarnie06
    with dissolve
    ma "Oh wow, you DID IT! Lifting me clear off the ground by the sheer POWER of your MONSTERCOCK!"
    if marniemax02 == False:
        call LustPlusMarnie
        $ marniemax02 = True
    mc "Now watch this training exercise..."
    hide mcflexmaxmarnie06
    call screen marnieflex
    screen marnieflex:
        add flexmarnie at center
        modal True
        button:
            imagebutton:
                focus_mask True
                idle "Icons/nextidle.png"
                hover "Icons/nexthover.png"
                action Jump ("FlexMarnieGymEnd")    
    label FlexMarnieGymEnd:
    show mcflexmaxmarnie06
    menu:
        "While your wet pussy is sitting on my hard rod, I have a proposition for you... You join my harem and I get to fuck you to heavens and back." if lustma >= 4 and haremma == False and marnieharem == False and girlsinharem <= 5 and marniedatedone:
            ma "Mmh... As a Road Warrior, I need my freedom, but as a woman, I need my SEX, and you're so PUMPED-UP and HUNG that I accept!"
            mc "I'll call you later in the evening and I'll show you what this cock can TRULY do..."
            $ haremma = True
            $ girlsinharem += 1
            $ marnieharem = True
            window hide
            show haremmarnie at plus
            $ renpy.pause(2.0, hard=True)
            ma "I can't wait [name]! But please put me down now, I need to take a shower..."
            mc "Sure thing, Marnie, I also need to take a shower after this intense IRON-PUMPING and COCK-FLEXING session!"
            jump GymShower  
        "While your wet pussy is sitting on my hard rod, I meant to ask you re-join my harem and enjoy my monstercock in the flesh!" if lustma >= 4 and haremma == False and marnieharem and marniedismissed == False and girlsinharem <= 5:
            ma "Such a romantic setting to ask that of me... Still, I can't say no to this MONSTERDONG!"
            $ haremma = True
            $ girlsinharem += 1
            window hide
            show haremmarnie at plus
            $ renpy.pause(2.0, hard=True)
            hide haremmarnie
            ma "But please put me down now, I need to take a shower..."
            mc "Sure thing, Marnie, I also need to take a shower after this intense IRON-PUMPING and COCK-FLEXING session!"
            jump GymShower  
        "How are you enjoying feeling the POWER of my cock Marnie?":
            ma "It's amazing but.. you can... put me down now [name], this is getting embarrassing. Me sitting on your HUMONGOUS cock.... I need to take a shower." 
            mc "Sure thing, Marnie, I also need to take a shower after this intense IRON-PUMPING and COCK-FLEXING session!"
            jump GymShower
if marniegym:
    $ gymma += 1
    window hide
    show marniegym04 at left with moveinleft
    ma "Oh WOW! That was IMPRESSIVE [name]! Can I feel your guns?"
    mc "For sure Marnie, check out how HARD and MASSIVE they are!"
    hide marniegym04
    hide mcflexmax
    show mcflexmaxmarnie
    with dissolve
    play sound "Sounds/gasp.mp3"
    ma "Oh my GOD! My hands can't even get around them, they are so HUGE!"
    if marniemax == False:
        call LustPlusMarnie
        $ marniemax = True
    mc "FUCK YEAH!"
    scene mcliftend02 blurred
    show mcflexmaxmarnie02
    ma "I'm so... I need to take a shower."
    mc "So do I after this MASSIVE IRON-PUMPING SESSION!"
    jump GymShower
if momgym and mommax and gymmo >= 5:
    $ gymmo += 1
    window hide
    show nancygym05 at left with moveinleft
    mo "My sweet landboy is getting so BIG! I'm such a proud landlady..."
    mc "Yep, getting BIGGER and STRONGER every day, Nancy!"
    mo "I can see that, sweetie. ANd I can also see... Your bulge GROWING!"                                                                                              
    mc "After such an intense workout, ALL my muscles get BIGGER and HARDER!"
    hide nancygym05
    hide mcflexmax
    show mcflexmaxnancy03
    with dissolve
    play sound "Sounds/gasp.mp3"
    mo "Not quite totally HARD and HUGE yet though..."
    mc "When it's ROCKHARD, it's so BIG and POWERFUL, it could carry your whole bodyweight on it I'm pretty sure."
    mo "Oooh, is that so? Then show your landlady, she's dying to see how strong THAT muscle truly is!"
    hide mcflexmaxnancy03
    show mcflexmaxnancy04
    with dissolve
    mo "It sure feels POWERFUL, sticking between my legs, drooling lots of precum..."
    mc "Now turn around and I'll prove to you it's powerful enough to LIFT you!"
    hide mcflexmaxnancy04
    show mcflexmaxnancy05
    with dissolve
    mo "Oh my sweet Lord! I'm just sitting on your SLAB of beef! What an amazing LOVE MUSCLE you have my sweet tenant!"
    mc "Wait, it'll get even more amazing when I..."
    play sound "Sounds/mcworkout.mp3"
    hide mcflexmaxnancy05
    show mcflexmaxnancy06
    with dissolve
    mc "....FLEX IT MIGHTILY for you Nancy!"
    mo "SUPER-AMAZING! Such a strong, HORSE-HUNG tenant that I have!"
    if mommax02 == False:
        call LustPlusNancy
        $ mommax02 = True
    mc "And I can train it to get even STRONGER. Like that..."
    hide mcflexmaxnancy06
    call screen nancyflex
    screen nancyflex:
        add flexnancy at center
        modal True
        button:
            imagebutton:
                focus_mask True
                idle "Icons/nextidle.png"
                hover "Icons/nexthover.png"
                action Jump ("FlexNancyGymEnd")    
    label FlexNancyGymEnd:
    show mcflexmaxnancy06
    mo "Oooh, you are sssooo HUNG and STRONG [name]!"
    menu:
        "Hang on a minute Nancy... I think it's time that you... joined my harem." if momharem == False and lustmo >= 4 and haremmo == False and girlsinharem <= 5:
            mo "Really? You want your old landlady in your HAREM? And you're asking me while I'm sitting on your giant rockhard cock?"
            mc "Well, yeah, I mean, it's as good an opportunity as any. I guess."
            mo "We probably shouldn't be telling anyone about it, but I'll gladly be your... harem girl, my sweet young man!"
            $ haremmo = True
            $ momharem = True
            $ girlsinharem += 1
            window hide
            show haremnancy at plus
            $ renpy.pause(2.0, hard=True)
            hide haremnancy
            mc "Then I'll see you... discreetly later on Nancy!"
            mo "Of course [name]! I can't wait to meet you \"in private\"."
            mc "And I'll go and take a shower to get squeaky-clean for our future roomies romp!"
            jump GymShower            
        "Hang on a minute Nancy... I think it's time that you... re-joined my harem." if momharem and momdismissed == False and lustmo >= 4 and haremmo == False and girlsinharem <= 5:
            mo "Really? You want your old landlady back in your HAREM? And you're asking me while I'm sitting on your giant rockhard cock?"
            mc "Well, yeah, I mean, it's as good an opportunity as any. I guess."
            mo "We probably shouldn't be telling anyone about it, but I'll gladly be your... harem girl, my sweet young man!"
            $ haremmo = True
            $ momharem = True
            $ girlsinharem += 1
            window hide
            show haremnancy at plus
            $ renpy.pause(2.0, hard=True)
            hide haremnancy
            mc "Then I'll see you... discreetly later on Nancy!"
            mo "Of course [name]! I can't wait to meet you \"in private\"."
            mc "And I'll go and take a shower to get squeaky-clean for our future roomies romp!"
            jump GymShower     
        "That's cos I have the hottest landlady ever sitting on my cock!":
            mo "Oooh, you're gonna make me blush [name]. I think... We should stop here, someone might come in..."
            mo "Go and take a shower my sweet tenant, you've earned it!"
            mc "Damn right, Gottta make that muscle go down some way or another... And I know just how to do it..."
            mo "Ooh, you're such a NAUGHTY tenant!"
            jump GymShower     
    mo "Mmh, I could sit on your giant boycock for hours, but this workout is making your landlady all dizzy... I need to go and take a shower my sweet tenant! *wink*"
    mc "I do too, Nancy! Gottta make that muscle go down some way or another... And I know just how to do it..."
    mo "Ooh, you're such a NAUGHTY tenant!"
    jump GymShower
if momgym:
    $ gymmo += 1
    window hide
    show nancygym05 at left with moveinleft
    mo "Oh sweetie, you are getting absolutely MASSIVE! Your landlady just NEEDS to FEEL those guns!"
    mc "For sure Nancy, go ahead and check out how HARD and GIGANTIC they are!"
    hide nancygym05
    hide mcflexmax
    show mcflexmaxnancy
    with dissolve
    play sound "Sounds/gasp.mp3"
    mo "Look my sweet young landboy, I can't even get my hands around them!"
    if mommax == False:
        call LustPlusNancy
        $ mommax = True
    mc "FUCK YEAH!"
    scene mcliftend02 blurred
    show mcflexmaxnancy02
    mo "Mmh, I'm going to have some SWEET dreams tonight... *wink*"
    menu:
        "Hang on a minute Nancy... I think it's time that you... joined my harem." if momharem == False and lustmo >= 4 and haremmo == False and girlsinharem <= 5:
            mo "Really? You want your old landlady in your HAREM?"
            mc "Well, yeah, I mean, you're still young and... err... fertile, so you can join my harem, no problem."
            mo "We probably shouldn't be telling anyone about it, but I'll gladly be your... harem girl, my sweet young man!"
            $ haremmo = True
            $ momharem = True
            $ girlsinharem += 1
            window hide
            show haremnancy at plus
            $ renpy.pause(2.0, hard=True)
            hide haremnancy
            mc "Then I'll see you... discreetly later on Nancy!"
            scene mcliftend02
            show mcflexmaxnancy03
            with dissolve
            mo "Of course [name]! I can't wait to meet you \"in private\"."
            mc "And I'll go and take a shower to get squeaky-clean for our future roomies romp!"
            jump GymShower            
        "Hang on a minute Nancy... I think it's time that you... re-joined my harem." if momharem and momdismissed == False and lustmo >= 4 and haremmo == False and girlsinharem <= 5:
            mo "Really? You want your old landlady in your HAREM?"
            mc "Well, yeah, I mean, you're still young and... err... fertile, so you can join my harem, no problem."
            mo "We probably shouldn't be telling anyone about it, but I'll gladly be your... harem girl, my sweet young man!"
            $ haremmo = True
            $ momharem = True
            $ girlsinharem += 1
            window hide
            show haremnancy at plus
            $ renpy.pause(2.0, hard=True)
            hide haremnancy
            mc "Then I'll see you... discreetly later on Nancy!"
            scene mcliftend02
            show mcflexmaxnancy03
            with dissolve
            mo "Of course [name]! I can't wait to meet you \"in private\"."
            mc "And I'll go and take a shower to get squeaky-clean for our future roomies romp!"
            jump GymShower 
        "Same here, dreaming about my hot landlady feeling up with HUGE muscles!":
            scene mcliftend02
            show mcflexmaxnancy03
            with dissolve
            mo "Oooh, you're gonna make me blush [name]. I think... We should stop here, someone might come in..."
            mo "Go and take a shower my sweet tenant, you've earned it!"
            mc "Damn right, Gottta make THAT muscle go down some way or another... And I know just how to do it..."
            mo "Ooh, you're such a NAUGHTY tenant!"
            jump GymShower         
    mc "So will I when I get to the shower room!"
    jump GymShower

if lenagym and lenamax and gymle >= 5:
    $ gymle += 1
    window hide
    show lenagym04 at left with moveinleft
    le "I could swear you're getting BIGGER. ALL OVER."
    mc "Yeah, I'm totally PUMPED-UP, Chief Lena!"
    le "Totally? You mean including that... MAN-MUSCLE down there?"
    mc "Of course, especially with you around, Chief..."
    hide lenagym04
    hide mcflexmax
    show mcflexmaxlena03
    with dissolve
    play sound "Sounds/gasp.mp3"
    le "So I'm responsible for this great big FAT thing getting bigger? How much bigger can it get [name]? and how much STRONGER?"
    mc "STRONG enough to LIFT YOU CLEAR off the ground, Chief!"
    le "As Compound Chief, I demand to see THAT!"
    hide mcflexmaxlena03
    show mcflexmaxlena04
    with dissolve
    le "It's sticking so far out between my thighs... And rubbing against my... aching pussy!"
    mc "Face me when I flex it for you, Lena!"
    hide mcflexmaxlena04
    show mcflexmaxlena05
    with dissolve
    le "Oh, damn [name]!... I really don't regret accepting you into the compound now!"
    mc "Just watch this, Chief..."
    play sound "Sounds/mcworkout.mp3"
    hide mcflexmaxlena05
    show mcflexmaxlena06
    with dissolve
    le "Oh wow, your cock is so much more powerful than Jake's! Err... I probably shouldn't have said that..."
    mc "Don't worry Lena, I know, I saw his tiny pindick in the shower... I bet he can't do that either. Watch."
    hide mcflexmaxlena06
    call screen lenaflex
    screen lenaflex:
        add flexlena at center
        modal True
        button:
            imagebutton:
                focus_mask True
                idle "Icons/nextidle.png"
                hover "Icons/nexthover.png"
                action Jump ("FlexLenaGymEnd")    
    label FlexLenaGymEnd:
    show mcflexmaxlena06
    if lenamax02 == False:
        call LustPlusLena
        $ lenamax02 = True
    le "I'm... ashamed to admit, this made me quite horny... I should go and take a shower, we can't go any further than that [name]..."
    mc "So do I after this MASSIVE IRON-PUMPING and COCK FLEXING session!"
    jump GymShower
if lenagym:
    $ gymle += 1
    window hide
    show lenagym04 at left with moveinleft
    le "You sure are getting exactly where I wanted you to be. An absolute BEAST of a muscleboy! Let me check those guns to make sure I'm not dreaming..."
    mc "Go ahead Chief, they are ALL YOURS!"
    hide lenagym04
    hide mcflexmax
    show mcflexmaxlena
    with dissolve
    play sound "Sounds/gasp.mp3"
    le "Mmmh, [name], you could beat any enemy with such POWERFUL biceps!"
    if lenamax == False:
        call LustPlusLena
        $ lenamax = True
    mc "FUCK YEAH!"
    scene mcliftend02 blurred
    show mcflexmaxlena02
    le "I'm so... I need to take a shower."
    mc "So do I after this MASSIVE PUMPING SESSION!"
    jump GymShower

if rubygym and rubymax and gymru >= 5:
    $ gymru += 1
    window hide
    show rubygym06 at left with moveinleft
    ru "Still as IMPRESSIVE as ever [name]!"
    mc "For sure Marnie, getting STRONGER and BIGGER all the time!"
    ru "Sure but... what about that OTHER muscle of yours? Is it getting STRONGER and BIGGER?"
    mc "Check it out yourself Ruby, you know you want to..."
    hide rubygym06
    hide mcflexmax
    show mcflexmaxruby03
    with dissolve
    play sound "Sounds/gasp.mp3"
    ru "Oh, it sures feels like it's getting BIGGER... But how much STRONGER I wonder?"
    mc "STRONG enough to CARRY YOU on it I reckon!"
    ru "Let's test this theory of yours then... Pull it out and show me!"
    hide mcflexmaxruby03
    show mcflexmaxruby04
    with dissolve
    ru "It's sticking out between my thighs like a battering ram. Now TRY and lift me with it..."
    mc "Sure, turn round, I want to see your face when I do..."
    hide mcflexmaxruby04
    show mcflexmaxruby05
    with dissolve
    ru "Mmmh, it looks like you might have been right... Can you flex it so I can make sure it's not a trick?"
    mc "Sure. Here you go."
    play sound "Sounds/mcworkout.mp3"
    hide mcflexmaxruby05
    show mcflexmaxruby06
    with dissolve
    ru "Oh wow, you DID IT! Lifting me clear off the ground by the sheer POWER of your MONSTERCOCK!"
    if rubymax02 == False:
        call LustPlusRuby
        $ rubymax02 = True
    mc "Now watch this training exercise..."
    hide mcflexmaxruby06
    call screen rubyflex
    screen rubyflex:
        add flexruby at center
        modal True
        button:
            imagebutton:
                focus_mask True
                idle "Icons/nextidle.png"
                hover "Icons/nexthover.png"
                action Jump ("FlexRubyGymEnd")    
    label FlexRubyGymEnd:
    show mcflexmaxruby06
    ru "I'm so... I need to take a shower to COOL OFF."
    menu:
        "Wouldn't you say I'm now STRONG ENOUGH for you to join my harem?" if rubyharem == False and lustru >= 4 and haremru == False and girlsinharem <= 5 and rubydatedone:
            ru "I definitely would... My pussy is ready to take your HUGE COCK home, cowboy!"
            $ haremru = True
            $ girlsinharem += 1
            $ rubyharem = True
            window hide
            show haremruby at plus
            $ renpy.pause(2.0, hard=True)
            hide haremruby
            mc "Then it's a deal! I'll call at night to show you my most SPECTACULAR muscle, Ruby... *wink*"
            ru "And I'll show you how my pussy muscles handle your beast!"
            mc "Damn, I'm gonna have a HOT shower now!"
            ru "Enjoy it, STUD!"
            jump GymShower
        "I think it's time for you to re-join my harem Ruby..." if rubyharem and rubydismissed == False and lustru >= 4 and haremru == False and girlsinharem <= 5:
            ru "I don't even remember why I left it... Your body... is just OOZING sex! I need that monstercock again so I say YES!"
            $ haremru = True
            $ girlsinharem += 1
            window hide
            show haremruby at plus
            $ renpy.pause(2.0, hard=True)
            hide haremruby
            mc "I'll call you at nights, so we can have some more fun with my MOST spectacular muscle!"
            ru "And I'll show you how my pussy muscles handle your beast!"
            mc "Damn, I'm gonna have a HOT shower now!"
            ru "Enjoy it, STUD!"
            jump GymShower
        "So do I after this MASSIVE IRON-PUMPING and COCK FLEXING session!":
            ru "I confess that I underestimated you... You truly are a MUSCLE STALLION..."
            ru "Keep getting BIGGER and I'll keep being in AWE of your GIANT MUSCLES! And also that huge PUSSY-WRECKING MUSCLE!"
            jump GymShower
        "My cock is so hard right now, I could tear a hole through the wall!" if haremru:
            ru "Easy tiger! Keep some strength for ME to be able PLOUGH that fat truncheon in my ASS!"
            mc "Oh fuck, you're making me so horny..."
            ru "Not here, tiger, someone could come in... Go and take  shower."
            jump GymShower
    mc "So do I after this MASSIVE IRON-PUMPING and COCK FLEXING session!"
    jump GymShower
if rubygym:
    $ gymru += 1
    window hide
    show rubygym06 at left with moveinleft
    ru "I must confess... Your arms are absolutely BEASTLY. I just want to feel their RAW POWER with my hands!"
    mc "Put them around my guns and you will Ruby!"
    hide rubygym06
    hide mcflexmax
    show mcflexmaxruby
    with dissolve
    play sound "Sounds/gasp.mp3"
    ru "They must be well over 25 inches around [name]! Ssssoo MASSIVE!"
    if rubymax == False:
        call LustPlusRuby
        $ rubymax = True
    mc "FUCK YEAH!"
    scene mcliftend02 blurred
    show mcflexmaxruby02
    ru "I'm so... I need to take a shower to COOL OFF."
    menu:
        "Wouldn't you say I'm now STRONG ENOUGH for you to join my harem?" if rubyharem == False and lustru >= 4 and haremru == False and girlsinharem <= 5 and rubydatedone:
            hide mcflexmaxruby02
            show mcflexmaxruby03
            with dissolve
            ru "I definitely would... My pussy is ready to take your HUGE COCK home, cowboy!"
            $ haremru = True
            $ girlsinharem += 1
            $ rubyharem = True
            window hide
            show haremruby at plus
            $ renpy.pause(2.0, hard=True)
            hide haremruby
            mc "Then it's a deal! I'll call at night to show you my most SPECTACULAR muscle, Ruby... *wink*"
            ru "And I'll show you how my pussy muscles handle your beast!"
            mc "Damn, I'm gonna have a HOT shower now!"
            ru "Enjoy it, STUD!"
            jump GymShower
        "I think it's time for you to re-join my harem Ruby..." if rubyharem and rubydismissed == False and lustru >= 4 and haremru == False and girlsinharem <= 5:
            hide mcflexmaxruby02
            show mcflexmaxruby03
            with dissolve
            ru "I don't even remember why I left it... Your body... is just OOZING sex! I need that monstercock again so I say YES!"
            $ haremru = True
            $ girlsinharem += 1
            window hide
            show haremruby at plus
            $ renpy.pause(2.0, hard=True)
            hide haremruby
            mc "I'll call you at nights, so we can have some more fun with my MOST spectacular muscle!"
            ru "And I'll show you how my pussy muscles handle your beast!"
            mc "Damn, I'm gonna have a HOT shower now!"
            ru "Enjoy it, STUD!"
            jump GymShower
        "So do I after this MASSIVE IRON-PUMPING SESSION!":
            hide mcflexmaxruby02
            show mcflexmaxruby03
            with dissolve
            ru "I confess that I underestimated you... You truly are a MUSCLE STALLION..."
            ru "Keep getting BIGGER and I'll keep being in AWE of your GIANT MUSCLES!"
            jump GymShower
        "I'm so BUFFED UP right now, I could fuck a whole harem under the shower!" if haremru:
            hide mcflexmaxruby02
            show mcflexmaxruby03
            with dissolve
            ru "Easy tiger! Keep some strength for ME to be able PLOUGH that fat truncheon in my ASS!"
            mc "Oh fuck, you're making me so horny..."
            ru "Not here, tiger, someone could come in... Go and take  shower."
            jump GymShower
    mc "So do I after this MASSIVE IRON-PUMPING SESSION!"
    jump GymShower

if lauriegym:
    $ gymla += 1
    window hide
    show lauriegym05 at left with moveinleft
    la "How can anyone grow so BIG! Can I feel your biceps pretty please [name]?"
    mc "Of course Laurie, but don't get TOO excited when you do! *wink*"
    hide lauriegym05
    hide mcflexmax
    show mcflexmaxlaurie
    with dissolve
    play sound "Sounds/gasp.mp3"
    la "Astounding! My palms can't even begin to contain those BOULDERS!"
    if lauriemax == False:
        call LustPlusLaurie
        $ lauriemax = True
    mc "FUCK YEAH!"
    scene mcliftend02 blurred
    show mcflexmaxlaurie02
    la "Mmmh, I really enjoy rubbing my hands all over those chorded GUNS! It's really... exciting!"
    mc "Oh, oh..."
    hide mcflexmaxlaurie02
    show mcflexmaxlaurie03
    with dissolve    
    la "Oh no! I'm... growing again!"
    mc "I warned you you would when you felt the awesome POWER of my MONSTERGUNS!"
    hide mcflexmaxlaurie03
    show mcflexmaxlaurie04
    with dissolve
    la "I'm so ashamed... I'm getting horny just feeling you up..."
    mc "Nothing to be ashamed of. I'm getting a hardon just feeling all PUMPED-UP!"
    hide mcflexmaxlaurie04
    show mcflexmaxlaurie05
    with dissolve
    mc "And also feeling up those massive titties of yours..."
    la "Oh, [name]! We... can't do that in the gym, I need to go and take a COLD shower to get back to normal."
    mc "I'll go and take a HOT shower then and dream of... nevermind."   
    jump GymShower

if aylagym and aylamax and gymay >= 5:
    $ gymay += 1
    window hide
    show gymayla04 at left with moveinleft
    ay "OK, that's wasn't boring after all... You seem to be getting BIGGER actually. I liked it."
    mc "I told you you would be impressed by how CHORDED I am after such an intense workout!"
    ay "Now you got me curious... About that other HUGE muscle of yours. Is it also getting STRONGER?"
    mc "For sure Ayla, and it's also getting BIGGER right now... Come here and I'll let you feel it."
    hide gymayla04
    hide mcflexmax
    show mcflexmaxayla03
    with dissolve
    play sound "Sounds/gasp.mp3"
    ay "I can feel your MONSTER with my leg... It's almost as THICK as one of them!... But can it lift me up clear off the floor?"
    mc "Your tiny body would be no match for his awesome POWER!"
    ay "Let's see if that's true then... Pull it out and show me how powerful it REALLY is!"
    hide mcflexmaxayla03
    show mcflexmaxayla04
    with dissolve
    ay "My feet are already not touching the ground anymore! And you haven't even flexed it yet..."
    mc "Turn round and I'll FLEX it for you Ayla!"
    hide mcflexmaxayla04
    show mcflexmaxayla05
    with dissolve
    ay "I'm suspended in mid-air on your GIANT BOYMEAT! Flex it for me now [name], flex it MIGHTILY!"
    mc "Sure. Watch this."
    play sound "Sounds/mcworkout.mp3"
    hide mcflexmaxayla05
    show mcflexmaxayla06
    with dissolve
    ay "Your cock should be canonized [name], it could be used as a WEAPON by the Church!"
    if aylamax02 == False:
        call LustPlusAyla
        $ aylamax02 = True
    ay "More, MORE! Just flex it like I'm a ragdoll!"
    hide mcflexmaxayla06
    call screen aylaflex
    screen aylaflex:
        add flexayla at center
        modal True
        button:
            imagebutton:
                focus_mask True
                idle "Icons/nextidle.png"
                hover "Icons/nexthover.png"
                action Jump ("FlexAylaGymEnd")    
    label FlexAylaGymEnd:
    show mcflexmaxayla06
    ay "Mmmh, well, that wasn't as BORING as I thought it would be. Actually, I liked it. A LOT."
    menu:    
        "You should join my harem... It would be non-boring just like this is." if aylaharem == False and lustay >= 4 and haremay == False and girlsinharem <= 5 and ayladatedone:
            if mcchurch <= 4:
                ay "No way! Your standing in the Church is not high enough and I ain't servicing a novice!"
                ay "Now let me get down. I need to take a shower. ALONE with the Phallus Lord."
                mc "Fine, but you'll regret it, the Phallus Lord is clearly on MY side seeing how HUGE I am down there!"
                jump GymShower
            ay "If you promise to make it as not-so-boring as this... Then I accept!"
            mc "I'll call you later in the evenings and I'll show you some GOO-OO-OOD times..."
            $ haremay = True
            $ girlsinharem += 1
            $ aylaharem = True
            window hide
            show haremayla at plus
            $ renpy.pause(2.0, hard=True)
            hide haremayla
            ay "You'd better, cos I'm already BORED being in your harem. I'm going to take a shower cos I'm already BORED."
            mc "I will too and I will let my imagination make it NOT BORING. You should do the same..."
            jump GymShower           
        "Maybe it's time for you to re-join my harem... What do you say?" if aylaharem and ayladismissed == False and lustay >= 4 and haremay == False and girlsinharem <= 5:
            if mcchurch <= 3:
                ay "No way! Your standing in the Church is not high enough and I ain't servicing a novice!"
                ay "Now let me get down. I need to take a shower. ALONE with the Phallus Lord."
                mc "Fine, but you'll regret it, the Phallus Lord is clearly on MY side seeing how HUGE I am down there!"
                jump GymShower
            ay "Alright. Only cos I know it CAN be NOT BORING. Sometimes."
            $ haremay = True
            $ girlsinharem += 1
            window hide
            show haremayla at plus
            $ renpy.pause(2.0, hard=True)
            hide haremayla
            mc "That's the spirit! I'll call you later in the evenings and I'll show you some GOO-OO-OOD times..."
            ay "You'd better, cos I'm already BORED being in your harem. I'm going to take a shower cos I'm already BORED."
            mc "I will too and I will let my imagination make it NOT BORING. You should do the same..."
            jump GymShower           
        "Yep, flexing my cock while a girl sits on it is pretty exciting for me too...":
            ay "I think you're starting to become very NAUGHTY. I'm not that kind of girl, so I'll go and take a shower now..."
            mc "I need to take one too, I'm sweating form this intense IRON-PUMPING and COCK-FLEXING session!"
            jump GymShower           
        "Flexing my cock while a girl sits on it is pretty exciting for me too... I'm fucking ROCKHARD for you Ayla!" if haremay:
            ay "I think you're starting to become very NAUGHTY. We can't do that here, find some holy baby oil and I'll show you what I can do with IT..."
            ay "Until then, put me down and go and take a shower to get this great big meatpole down to a decent state..."
            mc "Alright, but it will take a while after this intense IRON-PUMPING and COCK-FLEXING session!"
            jump GymShower           
    ay "But this is starting to become very NAUGHTY. I'm not that kind of girl, so I'll go and take a shower now..."    
    mc "I need to take one too, I'm sweating form this intense IRON-PUMPING and COCK-FLEXING session!"
    jump GymShower           
if aylagym:
    $ gymay += 1
    window hide
    show gymayla04 at left with moveinleft
    ay "I used to watch bodybuilding contests with my boyfriend on TV... I never saw anyone lift THAT MUCH [name]! How do you do it?"
    mc "Lots of TRAINING and alpha-radiated MONSTER MUSCLES!"
    ay "Can I feel your HUGE BICEPS with my tiny hands?!"
    hide gymayla04
    hide mcflexmax
    show mcflexmaxayla
    with dissolve
    play sound "Sounds/gasp.mp3"
    ay "I think your arms are even BIGGER than my head [name]!"
    if aylamax == False:
        call LustPlusAyla
        $ aylamax = True
    mc "FUCK YEAH!"
    scene mcliftend02 blurred
    show mcflexmaxayla02
    ay "This wasn't boring at all after all... I like feeling up those MUSCLE BOULDERS... But I should take a shower now, I'm getting... Can't say it."
    menu:    
        "You should join my harem... It would be non-boring just like this is." if aylaharem == False and lustay >= 4 and haremay == False and girlsinharem <= 5 and ayladatedone:
            if mcchurch <= 4:
                ay "No way! Your standing in the Church is not high enough and I ain't servicing a novice!"
                ay "Now let me get down. I need to take a shower. ALONE with the Phallus Lord."
                mc "Fine, but you'll regret it, the Phallus Lord is clearly on MY side seeing how HUGE I am down there!"
                jump GymShower
            scene mcliftend02
            show mcflexmaxayla03
            with dissolve
            ay "If you promise to make it as not-so-boring as this... Then I accept!"
            mc "I'll call you later in the evenings and I'll show you some GOO-OO-OOD times..."
            $ haremay = True
            $ girlsinharem += 1
            $ aylaharem = True
            window hide
            show haremayla at plus
            $ renpy.pause(2.0, hard=True)
            hide haremayla
            ay "You'd better, cos I'm already BORED being in your harem. I'm going to take a shower cos I'm sssooo BORED."
            mc "I will too and I will let my imagination make it NOT BORING. You should do the same..."
            jump GymShower           
        "Maybe it's time for you to re-join my harem... What do you say?" if aylaharem and ayladismissed == False and lustay >= 4 and haremay == False and girlsinharem <= 5:
            if mcchurch <= 3:
                ay "No way! Your standing in the Church is not high enough and I ain't servicing a novice!"
                ay "Now let me get down. I need to take a shower. ALONE with the Phallus Lord."
                mc "Fine, but you'll regret it, the Phallus Lord is clearly on MY side seeing how HUGE I am down there!"
                jump GymShower
            scene mcliftend02
            show mcflexmaxayla03
            with dissolve
            ay "Alright. Only cos I know it CAN be NOT BORING. Sometimes. Because of this HORSEDICK of yours."
            $ haremay = True
            $ girlsinharem += 1
            window hide
            show haremayla at plus
            $ renpy.pause(2.0, hard=True)
            hide haremayla
            mc "That's the spirit! I'll call you later in the evenings and I'll show you some GOO-OO-OOD times... Again."
            ay "You'd better, cos I'm going to take a shower cos I'm already BORED being in your harem again."
            mc "I will too and I will let my imagination make it NOT BORING. You should do the same..."
            jump GymShower           
        "Yep, flexing my huge muscles for a busty chick while wearing a sexy posing pouch is pretty exciting for me too...":
            scene mcliftend02
            show mcflexmaxayla03
            with dissolve
            ay "I think you're starting to become very NAUGHTY. I'm not that kind of girl, so I'll go and take a shower now..."
            mc "I need to take one too, I'm sweating form this intense IRON-PUMPING session!"
            jump GymShower           
        "Flexing my guns for you is pretty exciting for me too... I'm fucking ROCKHARD for you Ayla!" if haremay:
            scene mcliftend02
            show mcflexmaxayla03
            with dissolve
            ay "I think you're starting to become very NAUGHTY. We can't do that here, find some holy baby oil and I'll show you what I can do with IT..."
            ay "Until then, put me down and go and take a shower to get this great big meatpole down to a decent state..."
            mc "Alright, I'm hitting the shower stall for some NON-BORING shower scene!"
            jump GymShower           
    mc "Same here, I'm hitting the shower stall for some NON-BORING shower scene!"
    jump GymShower

label MarnieGym:
show screen mcstats
$ seengym = True
$ seenmarniegym = True
label GymMarnie01:
scene gym05 with dissolve
show marniegymbells01
ma "Oh, hi [name]! I hope you don't need those dumbbells because I'm about to use them..."
mc "I'm fine, they are too light for me anyway, you go ahead with your training..."
ma "And you'll watch I have no doubt..."
scene gym06
show marnietrain01
mc "(You bet I will...)"
hide marnietrain01
show marniegym
call screen marniegym
screen marniegym:
    add "Icons/nextidle.png"
    modal True
    button:
        xpos .91
        ypos .44
        xysize(140, 80)        
        action Jump ("MarnieGymWorkoutEnd")

label MarnieGymWorkoutEnd:
scene gym02 with dissolve
show marniegym02
ma "I LOVE using the gym... It makes me feel so ALIVE to be FIT!"
mc "I agree, and the BIGGER the muscles, the BETTER!"
hide marniegym02
show marniegym03
ma "Yeah? Well, check those abs [name]!"
mc "Nice Marnie, they're getting really developed. Not as much as mine of course..."
hide marniegym03
show marniegym01
ma "Stop bragging. And show me then."
mc "Well watch my EIGHT-pack while I pump iron!"
ma "Alright. Go ahead."
jump GymWorkout01

label NancyGym:
show screen mcstats
$ seengym = True
$ seenmomgym = True

label GymNancy01:
scene gym06 with dissolve
show nancytrain01
mc "There's Nancy doing some crunches..."
hide nancytrain01
show nancygym
call screen nancygym
screen nancygym:
    add "Icons/nextidle.png"
    modal True
    button:
        xpos .91
        ypos .44
        xysize(140, 80)        
        action Jump ("NancyGymWorkoutEnd")

label NancyGymWorkoutEnd:
scene gym02 with dissolve
show nancygym01
mo "Oh, hi [name]! I wasn't expecting you here."
menu:
    "I come here often to train Nancy, I need to get EVEN STRONGER!":
        mo "And how are you going to do that?"
        mc "By PUMPING over 2000lbs of iron!"
        hide nancygym01
        show nancygym02
        mo "What? THAT MUCH? I want to see that..."
        jump GymWorkout01
    "I've got an idea to make your Marvel costume painless to wear." if debranancyagree and debranancylab == False:
        hide nancygym04
        show nancygym01
        with fastdissolve
        mo "But... Why would I need to wear this cosplay costume anyway, sweetie pie?"
        mc "Well, you never know. The Avengers must be ready at all times!"
        hide nancygym01 
        show nancygym02
        with fastdissolve
        mo "Well... I suppose, if it's REALLY necessary..."
        mc "I got a deal with Debra to try her alpha-ray machine on you in reverse polarity."
        hide nancygym02 
        show nancygym01
        with fastdissolve
        mo "Reverse polarity? What does that mean?"
        mc "Something to do with quarks and bosons and shit. Sciency stuff. You wouldn't understand, but it WILL WORK, I promise! Let's go!"
        mo "Su...Sure sweetie pie. Let me get my costume and I'll meet you there."
        $ debranancyagree = True
        jump DebraNancyScience
    "I need you to become Captain Marvel for a day. The New Avengers must defeat Sean Insannity!" if period == 1 and debranancylab and missionhannity and missionhannitydone == False and haremmo:
        hide nancygym04 
        show nancygym01
        with fastdissolve
        mo "But.. I'm not REALLY a superhero, sweetie pie."
        mc "It's all in your mind Nancy. Once you wear the costume, you will BECOME Captain Marvel!"
        hide nancygym01 
        show nancygym03
        with fastdissolve
        mo "Well... I suppose, if you think so..."
        mc "I'm sure of it! Let's go and meet the Black Widow!"
        mo "Su...Sure sweetie pie. Let me get my costume first, I wouldn't want to meet her in a bikini."
        mc "And I'll get mine!"
        jump NewAvengersPremission

label LenaGym:
show screen mcstats
$ seengym = True
$ seenlenagym = True

label GymLena01:
scene gym02 with dissolve
show lenagym01
le "Hi [name], I was about to do some pull-ups... Wanna watch?"
mc "Sure chief..."
scene gym02
call screen lenagym
screen lenagym:
    add "lenagym"
    add "Icons/nextidle.png"
    modal True
    button:
        xpos .91
        ypos .44
        xysize(140, 80)        
        action Jump ("LenaGymWorkoutEnd")

label LenaGymWorkoutEnd:
scene gym02 with dissolve
show lenagym02
le "I'm glad to see that you use our gym. We want you to become as strong as possible to defeat our enemies!"
menu:
    "I was just passing by really, like visiting to see what's on offer.":
        hide lenagym02
        show lenagym03
        le "Oh. Well, as you can see, there is some very good equipment for a man like you to pump iron."
        le "Notably, a titanium-barbell that can support over 2000lbs of steel plates. You should train with these... You look like you could be capable of lifting such heavy weights..."
        mc "Sure, I'll try one day. But right now, I have others things to do."
        hide lenagym03
        show lenagym01
        le "Fine. But don't forget to train HARD before you PLAY hard! (wink)"
        hide lenagym01
        jump GymOut
    "Sure, I was just about to use the iron pumping station.":
        hide lenagym02
        show lenagym03
        le "Nice, I'd like to see that. You lifting the biggest set of weights we have. Over 2000lbs..."
        mc "Piece of cake for me, my body is so strong, I'll show you!"
        hide lenagym03
        jump GymWorkout01
#    "Sure, I was just about to do some curls. Lots of them to get bigger guns!":
#        le "Nice, I'd like to see that. You curling the biggest set of dumbbells we have. Over 500lbs each...."
#        mc "Piece of cake for me, my biceps are so powerful, I'll show you!"
#        jump GymWorkout02b


label AylaGym:
show screen mcstats
$ seengym = True
$ seenaylagym = True
if gymay == 0:
        jump GymAyla01
if gymay >= 1:
        jump GymAyla02
    
label GymAyla01:
scene aylagymstart with dissolve
mc sidemc "Ayla is using the treadmill."
scene aylagymbackground
call screen aylagymjog01
screen aylagymjog01:
    add aylagymjog01
    add "Icons/nextidle.png"
    modal True
    button:
        xpos .91
        ypos .44
        xysize(140, 80)        
        action Jump ("AylaGymWorkoutEnd")

label AylaGymWorkoutEnd:
scene aylagymstart with dissolve
show aylagymend
ay "I saw you ogling my big tits while I was on the treadmill. That's disgusting!"
mc "What? What have I done?"
$ aylagymout = True
ay "Just get out of my face FREAK."
mc "You sound like some chick from that other game... What's her name... Maddy."
call LustMinusAyla
$ gymay += 1
jump Gym01b

label GymAyla02:
scene aylagymstart with dissolve
mc sidemc "Ayla is using the treadmill. I'd better not ogle her big tits this time..."
scene aylagymbackground
call screen aylagymjog02
screen aylagymjog02:
    add aylagymjog01
    add "Icons/nextidle.png"
    modal True
    button:
        xpos .91
        ypos .44
        xysize(140, 80)        
        action Jump ("AylaGymWorkoutEnd02")
label AylaGymWorkoutEnd02:
scene aylagymstart with dissolve
show aylagymend
ay "What do you want?"
mc "Nothing. I was just waiting for you to finish to start my reps..."
ay "Well, I'm done here. So get on with your stupid reps then."
mc "Rightee-ooo."
jump GymWorkout01
    
label LaurieGym:
show screen mcstats
$ seengym = True
$ seenlauriegym = True
if gymla == 0:
        jump GymLaurie01
if gymla == 1:
        jump GymLaurie02
if gymla >= 2:
        jump GymLaurie03

label GymLaurie01:
play music "Sounds/laurieworkout.mp3"
scene laurieyoga01 with dissolve
mc "There's Laurie doing some yoga in a tight spandex suit..."
scene laurieyoga02 with dissolve
mc "Wow, she's really flexible..."
scene laurieyoga03 with dissolve
mc "I can think of many wild uses for that flexibility in bed..."
scene laurieyoga04 with dissolve
mc "Looks like she's almost finished..."
show laurieyoga04b
la "Oh, hi [name]! Let me finish my last exercise and I'll be with you..."

label LaurieGymEnd:
stop music
scene gym04 with dissolve
show lauriegym01 with dissolve
la "Are you going to pump iron? Can I watch you? I'm done with my yoga for the day..."
mc "Of course Laurie. I'm gonna power-lift the heaviest set of weights you've ever seen in your life!"
la "Wow... I can't wait to see that! (wink)"
jump GymWorkout01

label GymLaurie02:
$ gymla += 1
scene gym04 with dissolve
show lauriegym12
la "Aah, that was a good stretching routine..."
hide lauriegym12
show lauriegym11
la "Now I'm so tired..."
hide lauriegym11
show lauriegym10
la "Oh, it's you... And... you're wearing a... see-thru thong!"
mc "Yeah, it's a gift from Chief Lena, she says it will allow me to train better by not constraining blood flow throughout my body..."
hide lauriegym10
show lauriegym13
la "I... guess that makes sense... But it's so... lewd!"
mc "Well, there's nothing I can do about it, Chief's orders and all that."
show lauriegym13b
la "Don't worry, I... don't mind..."
mc "Err.. Your tits seem to be growing again. Are you getting horny?"
hide lauriegym13b
show lauriegym13c
la "What? Oh no!"
hide lauriegym13
hide lauriegym13c
show lauriegym14
mc "I hope you're wearing a stretchy top, cos you're really growing HUGE real fast Laurie!"
la "My God, what's happening to me? Please do something about it [name]!"
mc "I'm not sure what I could..."
play sound "Sounds/snap.mp3"
hide lauriegym14
hide lauriegym13
show lauriegym15
mc "... do."
la "My top has snapped, now my breasts are exposed, this is so embarassing!"
mc "Don't worry about it, I've seen plenty of breasts before. ALthoug not as MASSIVE as your funbags right now!"
hide lauriegym15
show lauriegym16
la "It's really PAINFUL! Please help me [name]"
menu:
    "Let me squirt some milk out of your tits to make them go back to normal":
        la "Please be gentle..."
        jump LaurieGymSquirt
    "Maybe my cum covering your tits will alleviate the pain...":
        la "This option has not been implemented yet. Choose the other one."
        mc "Right. I choose the other one then..."
        jump LaurieGymSquirt        
        la "What? That sounds dumb.. But I'm desperate so I'll agree..."
        mc "Trust me, I received a heavy dose of alpha-radiations, so my cum is special."
        jump LaurieGymCum

label LaurieGymSquirt:
scene gym04 with dissolve
show lauriegymsquirt01a
mc "I'll slowly push around your nipples..."

hide lauriegymsquirt01a
show lauriegymsquirt01b
mc "There you go..."
la "Aah, I'm squirting milk!"
hide lauriegymsquirt01b
show lauriegymsquirt01a
mc "And again..."
hide lauriegymsquirt01a
show lauriegymsquirt01b
la "Do you think this is working?"
hide lauriegymsquirt01b
show lauriegymsquirt02a
mc "I'd say so, your tit has shrunk, but there's still some milf left..."
hide lauriegymsquirt02a
show lauriegymsquirt02b
la "Ooh, this is starting to feel good... Oh no, why did I say that?"
hide lauriegymsquirt02b
show lauriegymsquirt02a
mc "I didn't hear a thing, I'm totally concentrated on my task..."
hide lauriegymsquirt02a
show lauriegymsquirt02b
mc"I think we're done with this breast, let's work on the other one..."
scene gym04squirt blurred
show lauriegymsquirt03a at left
la "This is... so embarrassing... A man breast-pumping me like that..."
mc "You asked for help, and here I am!"
hide lauriegymsquirt03a
show lauriegymsquirt03b at left
mc "Nice, some breastjuice is also squirting out of this one like crazy...."
hide lauriegymsquirt03b
show lauriegymsquirt03a at left
la "Do it again, I can feel I'm still... full.."
hide lauriegymsquirt03a
show lauriegymsquirt03b at left
mc "Rightee-ooo..."
hide lauriegymsquirt03b
show lauriegymsquirt03c at left
la "OOh, I feel much better now..."
mc "Hang, on, there's still a bit more milk I need to remove..."
hide lauriegymsquirt03c
show lauriegymsquirt03d at left
mc "I think we're done Laurie... Your tits are still huge, but it's their normal size more or less..."
scene gym04 with dissolve
show lauriegymsquirt04
la "Thank you so much [name]... Please... don't mention that to anyone.."
mc "Sure Laurie... Hang on, you shouldn't leave the gym with milk pouring out of your nipples like that, let me help you get rid of it..."
hide lauriegymsquirt04
show lauriegymsquirt05
la "What are you doing?"
mc "Just cleaning up... You're all done now..."
la "Thanks God for that, this was just sssooo embarassing... I'd better leave now [name]."
hide lauriegymsquirt05
mc "Damn, and I wasting too much time on de-milking her tits... I just have time for a quick shower... And a dreamy wank of course."
jump GymOut

label LaurieGymCum:
scene lauriegymcum with dissolve
show mclauriecum01
mc "OK, I'll jerk off while you hold your titties to receive my dose, the best way is for it to splash all over them and cover as much surface as possible.."
la "This had better work [name], because it's vile and disgusting!"
mc "What's vile about receiving my virile load? Get ready, I'm about to blow!"
hide mclauriecum01

show lauriegymcum01
la "I don't feel a thing..."
mc "Maybe you should eat some of it then, that might work..."
hide lauriegymcum01
show lauriegymcum02
la "It's delicious... Oh no, I didn't want to say that!"
mc "Well, you said it. Now eat up, there's enough for a full lunch."
hide lauriegymcum02
show lauriegymcum03
la "Nothing happened. My engorged tits are still hurting me..."
mc "Well, I'm sorry, I gave it a try, the best you can do is sleep on it, hopefully, they will have gone back to normal by tomorrow..."
la "You're right. But I have so much work to do... (sigh)."
$ seengym = True
jump GymOut

label GymLaurie03:
play music "Sounds/laurieworkout.mp3"
scene laurieyoga01 with dissolve
mc "There's Laurie doing some yoga in a tight spandex suit..."
scene laurieyoga02 with dissolve
mc "Wow, she's really flexible..."
scene laurieyoga03 with dissolve
mc "I can think of many wild uses for that flexibility in bed..."
scene laurieyoga04 with dissolve
mc "Looks like she's almost finished..."
show laurieyoga04b
la "Oh, hi [name]! I'm sorry, but I'm too busy to do a not-yet implemented scene..."
mc "I guess I'll pump iron on my own then..."
jump GymWorkout01

label RubyGym:
show screen mcstats
$ seengym = True
$ seenrubygym = True
if gymru >= 1:
        jump GymRuby01
if gymru == 2:
        jump GymRuby02
if gymru == 3:
        jump GymRuby03

label GymRuby01:
scene gym03
show rubygym01
ru "Hi there big man. Wanna see me lift this super-heavy barbell?"
mc "Fine. Go ahead."
hide rubygym01
scene gym03
show nextidle
play music "Sounds/womangroan.mp3"
call screen rubygymbell
screen rubygymbell:
    add rubygymbell at center
    modal True
    button:
        xpos .91
        ypos .44
        xysize(140, 80)        
        action Jump ("RubyGymWorkoutEnd")
        
label RubyGymWorkoutEnd:
stop music
scene gym03
show rubygym02
ru "Enjoyed watching the show big man? Do you think you can power-lift as much as me?"
mc "Of course, I'm more muscular and stronger than you!"
hide rubygym02
show rubygym03
ru "Oh yeah, you think so?"
hide rubygym03
show rubygym04
ru "You really think you can compare to this body?"
mc "Well, obviously, my tits are smaller..."
hide rubygym04
show rubygym05
ru "I'm talking about my chorded musculature...."
mc "Yeah I'm sure and I'll prove it! I'll pick the heaviest set of weights to show you what I'm made of..."
hide rubygym05
show rubygym01
ru "Let's see you in action then big man. See if you've got enough spunk in you to be a true Road Warrior."
hide rubygym01
jump GymWorkout01
        
label GymShower:
scene locker01 with fade
if week >= 2:
    $ d4rolllocker=renpy.random.randint(1,4)
    if d4rolllocker == 1:
        $ jakelocker = True
    if jakelocker:
        show lockerjakeidle
        mc "Ah, there's that douchebag Jake. Stark naked."
if jakelocker == False:
    mc "Great, there's no one around. Then again, there aren't many guys around in the compound. Or in the whole world."
call screen menchanging
screen menchanging:
    modal True    
    imagebutton:
        focus_mask True
        idle "Gym/showeridle.png"
        hover "Gym/showerhover.png"
        action Jump ("Shower")
#    imagebutton:
#        focus_mask True
#        idle "Gym/crackidle.png"
#        hover "Gym/crackhover.png"
#        action Jump ("MenCrack")
    imagebutton:
        focus_mask True
        idle "Gym/lockersidle.png"
        hover "Gym/lockershover.png"
        action Jump ("MenLocker")
    if jakelocker:
        imagebutton:
            focus_mask True
            idle "Gym/lockerjakeidle.png"
            hover "Gym/lockerjakehover.png"
            action Jump ("JakeLocker")

label JakeLocker:
scene locker03 with dissolve
if persistent.tipson and mushroomoffered == False:
    show friendtip at tips with dissolve
    pause
    hide friendtip
if jakefriend <= 1:
    show jakeshower01b
    ja "What do you want? I'm about to leave."
if jakefriend >= 2:
    show jakeshower03b    
    ja "What's up [name]?"
menu:
    "I couldn't help but notice how TINY your pee-pee was... (humiliate Jake)" if spokejakelocker == 1:
        scene locker03
        show jakeshower02b
        ja "Hey! Stop staring, you fucking FAGGOT!"
        mc "I wasn't staring, you were stark naked, and it was hard to see it, that's all..."
        mc "Mine, on the other hand, is clearly visible from MILES AWAY."
        ja "Yeah, so? You're just a young man, you'd better learn your place here quickly I'm warning you!"
        mc "Oh, I know my place here. At the top of the ALPHA-STUD LADDER! And Chief Lena knows it too..."
        hide jakeshower02b
        show jakeshower04b
        with fastdissolve
        ja "What are you implying?"
        mc "That you can't possibly satisfy her with that pindick of yours!"
        window hide
        show jakeshower04b at midright with move
        show mcnaked01 at midleft with moveinleft
        mc "Now THAT is a real man's cock! It's so big, it doesn't even fit on the screen."
        hide jakeshower04b
        show jakeshower05b at midright
        with fastdissolve
        ja "That thing is MONSTROUS! You would totally destroy Lena's pussy with it!"
        mc "And she would love it, dontcha think?"
        hide jakeshower05b
        show jakeshower06b at midright
        ja "Perhaps... I don't know, this is so humiliating!"
        hide mcnaked01
        show mcnaked02 at midleft
        with fastdissolve
        mc "Come on now, it's not your fault, you should just do what any good lousy husband does and become a cuck to an ALPHA-STUD!"
        ja "Wha... What do you mean?"
        mc "You've got to instill in her mind the idea of her getting fucked by my STALLION COCK, know whadda mean? It's for her own good."
        ja "O...Okay."
        call LustPlusLena
        mc "Now off you go Little Jake, I need to take a shower."
        ja "Yes... I'll go."
        hide jakeshower06b
        $ spokejakelocker += 1
        call FriendMinusJake
        $ jakelocker = False
        jump Shower       
    "Hi Jake, good to see a fellow man using the gym... (befriend Jake)" if jakefriend <= 1:
        scene locker03
        show jakeshower03b
        with fastdissolve
        ja "Yeah, I'm not letting women take over OUR gym man!"
        mc "I was thinking EXACTLY the same thing."
        ja "Well, I'm glad to see we're on the same page. See you later buddy!"
        mc "See you jake!"
        hide jakeshower03b
        mc "(I might have to work more on that friendship, there might be something to get out of it, right?)"
        call FriendPlusJake
        $ jakelocker = False
        jump Shower
    "Hi Jake, do you mind if I take a shower?... (befriend Jake)" if jakefriend >= 2:
        scene locker03
        show jakeshower01b
        with fastdissolve
        ja "Of course, you go right ahead buddy. I was about to leave anyway, it's all yours."
        mc "Thanks. Phew, no pain, no gain, right?"
        hide jakeshower01b
        show jakeshower03b
        with fastdissolve
        ja "Yeah, I've been pumping iron so much my muscles ache!"
        mc "I know what you mean, same here! (what a wimp, my muscles don't ache at all...)"
        call FriendPlusJake
        if jakefriend >= 4 and jakepassword == False:
            hide jakeshower03b
            show jakeshower05b
            with fastdissolve
            ja "Listen man, since you're working for us..."
            mc "Yes?"
            ja "I was a Road Warrior before... We have a secret password. I might as well tell you what it is."
            mc "Yes, it could prove useful on my important missions."
            hide jakeshower05b
            show jakeshower01b
            with fastdissolve
            ja "But don't EVER use it before you become an ACTUAL Road Warrior, understood?"
            mc "Sure, I'll use it only when I can. Wouldn't want to be found out and hung like a traitor."
            hide jakeshower01b
            show jakeshower03b
            with fastdissolve
            ja "It's... \"Gazoonka\"."
            mc "Copy that. Thanks Jake."
            ja "I'll go and get dressed now. See you later buddy!"
            hide jakeshower03b with dissolve
            call PlusWarrior
            mc "Gazoonka. Gazoonka. I'd better remember that word. Too bad I don't have a pen and a piece of paper to write it down."
            $ jakelocker = False
            $ jakepassword = True
            jump Shower
        ja "Enjoy your shower [name], see you later!"
        hide jakeshower03b
        mc "(I might have to work more on that friendship, there might be something to get out of it, right?)"
        $ jakelocker = False
        jump Shower
    "So, how did you enjoy your last cuckolding session?" if jakeknowsharem:
        scene locker03
        show jakeshower06b
        with fastdissolve
        ja "I... don't know what to think. On the one hand, Lena is finally sexually satisfied..."
        hide jakeshower06b
        show jakeshower05b
        with fastdissolve
        ja "...But now she doesn't look at me the same way..."        
        mc "That's what happens to girls after I've filled up their holes with my HUGE horsecock. Other men just don't compare anymore."
        hide jakeshower05b
        show jakeshower06b
        with fastdissolve
        ja "I feel so humiliated."
        mc "Don't be too hard on yourself. The same thing would have happened to any other man. As I said, after I've ploughed my MONSTERDICK into th..."
        hide jakeshower06b
        show jakeshower04b
        with fastdissolve
        ja "Yeah, ok, I GET IT! I'm leaving."
        mc "Temper, temper..."
        $ jakelocker = False
        jump Shower

label MenLocker:
scene menlocker01
mc "This locker is open. But empty. I smell a quest that wasn't implemented and never will be."
jump GymShower

label Shower:
mc "I'll take a well-deserved shower."
if jakelocker:
    ja "I was about to leave anyway, it's all yours..."
    mc "Godamn right, it's all mine. I've been PUMPING iron and I need to shower!"
scene lockermc01 with dissolve
play music "Sounds/shower.mp3"
mc "Aaah. That's nice and relaxing. So much so that I'm getting a massive boner..."
scene lockermc02 with dissolve
mc "If only there was a hot woman to bang next to me...."
hide screen calendar
hide screen mcstats

if marniegym:
    menu:
        "Like Marnie...":
            jump MarnieDream01
        "Skip":
            jump ShowerEnd
    label MarnieDream01:            
    play sound "Sounds/dream.mp3"
    scene locker03dream with dissolve
    show marnieshower01
    play music "Sounds/showerstrip.mp3"
    ma "Are you looking for a tip? I've got plenty of SEX TIPS for you."
    mc "Yeah? Like what?"
    hide marnieshower01    
    show marnieshower02
    ma "Well, I'll tell you only if you promise..."
    ma "...to FUCK me like a BEAST!"
    mc "I can make that promise, no worries!"
    hide marnieshower02    
    show marnieshower03                                            
    ma "I knew you would agree... Well, my first tip is that you need to have a HUGE ROCK-HARD COCK! So that it fits between my HUGE SOFT TITS!"
    mc "And I HAVE, what a coincidence!"
    hide marnieshower03
    scene locker03 blurred
    show marnieshower04
    ma "And my second tip is that..."
    ma "...You need to COVER them in an INCH-THICK layer of man-juice!"
    mc "I'll see what I can do... Let us proceed then."
    scene lockermarnietit01 with dissolve    
    ma "Mmh, you're ROCK-HARD and already DRIPPING with yummy pre-cum! I'l gonna have a lot of fun with that giant cock!"
    scene lockermarnietit02 with dissolve    
    ma "Let's see if that MONSTER ROD fits between my MASSIVE RACK shall we?"
    mc "I'm pretty sure it does, it's even sticking out..."
    scene lockermarnietit03 with fastdissolve    
    ma "Great, then I can suck on the tip, while you PUMMEL my breasts!"
    mc "I'll fuck them so hard and fast they will heat up like an iron bar in furnace!"
    call screen marniegymdream01
    screen marniegymdream01:
        add dreammarniegym01 at center
        modal True
        button:
            imagebutton:
                focus_mask True
                idle "Icons/nextidle.png"
                hover "Icons/nexthover.png"
                action Jump ("DreamMarnie01GymEnd")    
    label DreamMarnie01GymEnd:
    mc "Damn, I need to cool off or I'll blow my load right there!"
    ma "Then eat my pussy dirty boy!"
    scene lockermarnielick01 with dissolve
    ma "Yes, swirl your tongue, just like that..."
    scene lockermarnielick02 with dissolve
    ma "Oooh, you are a man of so many wonders..."
    mc "I'm the HERO, that's why it's assumed I am a Master Cocksman."
    ma "Then it's time to FUCK ME, Master Cocksman!"
    scene lockermarniefuck01 with dissolve
    ma "Be careful, I've never had anything THAT big in me before!" 
    mc "Just relax those pussy muscles and..."
    scene lockermarniefuck02 with dissolve 
    mc "...It will fit without any problem."
    call screen marniegymdream02
    screen marniegymdream02:
        add dreammarniegym02 at center
        modal True
        button:
            imagebutton:
                focus_mask True
                idle "Icons/nextidle.png"
                hover "Icons/nexthover.png"
                action Jump ("DreamMarnie02GymEnd")    
    label DreamMarnie02GymEnd:
    ma "Don't cum inside me, I want your cum ALL OVER my body!"
    scene lockermarniecum with dissolve
    mc "RHAAA!"
    ma "There you go! Remember, you need to cover my chest in an INCH-THICK layer of ball-batter!"
    mc "Fuck, I'm spewing non-stop!"
    stop music
    play music "Sounds/shower.mp3"
    scene lockermccum01 with dissolve
    mc "Yeah, take those jets Marnie! AAAH!"    
    jump ShowerEnd

if momgym:
    menu:
        "Like Nancy...":
            jump NancyDream01
        "Skip":
            jump ShowerEnd
    label NancyDream01:            
    play sound "Sounds/dream.mp3"
    scene locker03dream with dissolve
    show nancyshower01
    play music "Sounds/showerstrip.mp3"
    mo "Oh [name], please help me! Free me from these horrible chains... And Nancy will do ANYTHING for you. \nAnd I mean ANYTHING."
    mc "Of course Nancy, I'll break them apart with my SUPERMAN STRENGTH!"
    hide nancyshower01    
    show nancyshower02
    mo "Wow, you did it with such ease, you are ssooo STRONG my sweet young man..."
    mc "About that promise of yours..."
    mo "Of course [name], I haven't forgotten..."
    hide nancyshower02    
    show nancyshower03                                            
    mo "I bet your muscles are huge ALL OVER for your landlady?"
    mc "Damn right, I'm hard as a rock for your smoking hot bod Nancy!"
    hide nancyshower03
    scene locker03 blurred
    show nancyshower04
    mo "Maybe you'd like to suckle on my big tits for starters?"
    mc "Gimme, gimme your milk Nancy!"
    scene lockernancytit01 with dissolve    
    mo "I still have plenty of milk for my sweet man!"
    mc "*slurp* Mmh, it tastes so good..."
    scene lockernancytit02 with fastdissolve    
    mo "I'm so happy to be FEEDING you! Get as much of my milk as you can, it will make you stronger!"
    mc "Now it's time for ME to feed YOU! With some MEAT!"
    scene lockernancy01 with dissolve
    mo "I can barely fit the head in my mouth, you're so HUNG [name]!"
    mc "Just let it slip down your throat, I'm sure you can do it!"
    scene lockernancy02 with dissolve
    mc "Fuck Nancy, you're DEVOURING my cock almost to the balls!"
    mo "Glllurgg..."
    mc "God, I'm so hard I need to FUCK you NOW Nancy!"
    scene lockernancyfuck01 with dissolve
    mo "And I'm so HORNY I want to ride that sweet massive manmeat till it explodes inside of my womb!" 
    mc "Fuck, that's so dirty! And I'm a DIRTY BOY!"
    scene lockernancyfuck02 with dissolve 
    mo "Oh my God, your dick is like a tree trunk inside of my tender pussy! Fuck me HARD! FUCK YOUR LANDLADY!"
    call screen nancygymdream
    screen nancygymdream:
        add dreamnancygym at center
        modal True
        button:
            imagebutton:
                focus_mask True
                idle "Icons/nextidle.png"
                hover "Icons/nexthover.png"
                action Jump ("DreamNancyGymEnd")    
    label DreamNancyGymEnd:
    scene lockernancycum01 with dissolve
    mc "I'm EXPLODING inside you and dumping my load in your womb!"
    mo "I can feel it [name], you're FLOODING it with your sweet sweet CUM!"
    scene lockernancycum02 with dissolve
    mc "I can tell, it's dripping like crazy down my shaft and balls, you must be BLOATED with the stuff!"
    mo "I am [name] and it feels ssoo good! Keep pumping your seed inside of me please!"
    stop music
    play music "Sounds/shower.mp3"
    scene lockermccum01 with dissolve
    mc "Yeah, take that Nancy! AAAH!"    
    jump ShowerEnd

if lenagym:
    menu:
        "Like Chief Lena...":
            jump LenaDream01
        "Skip":
            jump ShowerEnd
    label LenaDream01:            
    play sound "Sounds/dream.mp3"
    scene locker03dream with dissolve
    show lenashower01
    play music "Sounds/showerstrip.mp3"
    le "Well, hello [name]. I was just about to take a shower myself..."
    mc "Then why don't you join me Chief Lena!"
    hide lenashower01    
    show lenashower02
    le "Of course I will, but first I have to get totally undressed..."
    mc "What a fine body you have Chief!"
    le "That's why I'm the Chief..."
    hide lenashower02    
    show lenashower03                                            
    le "Oh my, [name]. Your cock is sssooo much bigger than Jake's. He's a toddler next to you."
    mc "Fuck yeah, I'm da REAL man here!"
    hide lenashower03
    scene locker03 blurred
    show lenashower04
    le "Show me what you can do with your mighty love sword STUD!"
    mc "I'll impale you on it Chief! Then you'll feel the power of a REAL man, not a wimp like your pindick hubby!"
    le "Ooooh, you're ssoo manly! But first, I want to lick your shaft EVERYWHERE!" 
    scene lockerlena01    
    mc "There you go Chief, can you feel how hard I am for you?"
    le "You're so BIG! I've never been with a man as virile as you! I want to suck it NOW!"
    scene lockerlenasuck01 with dissolve
    mc "You're doing good Lena... But let me feed you a few more inches to see how GREAT a cocksucker you can be!"
    scene lockerlenasuck02 with dissolve
    mc "That's it, all the way down your throat!"
    le "Glllurgg..."
    scene lockerlena02 with dissolve
    mc "And now for the main course... Your tight pussy!"
    le "It's so thick [name]! You're such a MEGA-stud!"  
    scene lockerlena02a with dissolve 
    le "AAAH! Your giant love muscle is pulsating inside me and making me cum like crazy!"
    mc "Take it Chief Lena, take ALL of it! RHHAAA!"
    call screen lenagymdream
    screen lenagymdream:
        add dreamlenagym at center
        modal True
        button:
            imagebutton:
                focus_mask True
                idle "Icons/nextidle.png"
                hover "Icons/nexthover.png"
                action Jump ("DreamLenaGymEnd")    
    label DreamLenaGymEnd:
    le "I'm squirting! Oh my God, I never squirt with Jake! Your cock is ssooo good!"
    mc "I'm about to blow my load too Chief Lena, get ready for a mighty cum shower!"
    scene lockerlena03 with dissolve
    mc "RHAAA? I'm still cumming after filling you up!"
    le "YES, YES, keep pumping your sauce [name], I want to be covered in it!"
    scene lockerlena04 with dissolve
    mc "Ask and you shall receive! Here's more thick jets of spunk for you Chief Lena!"
    le "So good, and so warm, you're a real cum-machine [name], I can't believe how much cum you can spew, keep going I beg you!"
    stop music
    play music "Sounds/shower.mp3"
    scene lockermccum01 with dissolve
    mc "Yeah, take that Chief Lena! AAAH!"    
    jump ShowerEnd

if lauriegym:
    menu:
        "Like Laurie...":
            jump LaurieDream01
        "Skip":
            jump ShowerEnd
    label LaurieDream01:            
    play sound "Sounds/dream.mp3"
    scene locker03dream with dissolve
    show laurieshower01 at center
    play music "Sounds/showerstrip.mp3"
    la "Oh hi [name], are you taking a shower? Can I join you? I'm done with my yoga for the day...."
    mc "For sure Laurie, I'll make room for you... and my cock!"
    hide laurieshower01    
    show laurieshower02
    la "I've never seen a man with a godly body like yours. You're making me ssoo horny."
    mc "I'm horny too. Perfect combination."
    hide laurieshower02    
    show laurieshower03
    la "I'm sssoo hot for you [name], my tits have grown to a simply GIGANTIC size!"
    mc "Fuck yeah! So has my huge shaft for you Laurie!"
    hide laurieshower03        
    scene locker03 blurred
    show laurieshower04
    la "I'm a vegetarian but I'll gladly eat YOUR meat."
    mc "It's hot and ready for your hungry mouth, get to it!"
    la "I'll do it \"Yoga style\"..." 
    scene lockerlauriefuck01b with dissolve
    mc "That's it, suck it hard Laurie, I want your spit all over my mighty shaft!"
    scene lockerlauriefuck01c with dissolve
    mc "Open wider,I'm gonna pound that filthy mouth of yours"
    scene lockerlauriefuck01b with dissolve
    pause 0.3
    scene lockerlauriefuck01d with fastdissolve
    mc "YES, ALL THE WAY down your throat! Damn it girl, you can swallow it all!"
    scene lockerlauriefuck01a with dissolve
    la "I'm feeling so dirty, with all your copious precum dripping down my chin..."
    mc "Just you wait till I come for REAL..."
    la "Well, why don't I help you coax that load... I'll show you what my flexible body can do to your donkey dick..."
    scene lockerlauriefuck02a with dissolve
    mc "Not bad, but you still have over ten inc..."
    scene lockerlauriefuck02b with dissolve
    mc "... to go! AAAH!"
    la "You were saying?"
    scene lockerlauriefuck02a with fastdissolve
    pause 0.2
    scene lockerlauriefuck02b with fastdissolve
    pause 0.3
    scene lockerlauriefuck02a with fastdissolve
    pause 0.2
    scene lockerlauriefuck02b with fastdissolve
    pause 0.3
    scene lockerlauriefuck02a with fastdissolve
    pause 0.2
    scene lockerlauriefuck02b with fastdissolve
    pause 0.3
    scene lockerlauriefuck02a with fastdissolve
    pause 0.2
    scene lockerlauriefuck02b with fastdissolve
    pause 0.3
    scene lockerlauriefuck02a with fastdissolve
    pause 0.2
    scene lockerlauriefuck02b with fastdissolve
    pause 0.3
    la "Are you getting there? I can feel your monster cock getting bigger and harder... (giggles)"
    scene lockerlauriefuck02d with fastdissolve
    mc "FUCK! I'm cumming a MONSTER LOAD DEEP INSIDE YOU LAURIE!"
    scene lockerlauriefuck02c with dissolve
    la "YES, keep pumping that shaft, cover me with your warm virile cream [name]!"
    stop music
    play music "Sounds/shower.mp3"
    scene lockermccum01 with dissolve
    mc "Yeah, take that Laurie, I'm gonna drown your giant tits in my cum!"    
    jump ShowerEnd

if rubygym:
    menu:
        "Like Ruby...":
            jump RubyDream01
        "Skip":
            jump ShowerEnd
    label RubyDream01:            
    play sound "Sounds/dream.mp3"
    scene locker03dream with dissolve
    show rubyshower01
    play music "Sounds/showerstrip.mp3"
    ru "Well, what do we have here? A teen muscle stud with a giant hard cock!"
    mc "That's right Ruby, ALL my muscles are HUGE and HARD!"
    hide rubyshower01    
    show rubyshower02
    ru "I can see that [name]. Never seen someone as buff as you. My pussy is all tingly."
    mc "Then we should remedy this tingling sensation and replace it with a HARD POUNDING one."
    hide rubyshower02    
    show rubyshower03                                            
    ru "I like your way of thinking. Fuck me HARD then, as HARD as you can! Just like it says right here on my butt..."
    mc "I don't need to be asked twice!"
    hide rubyshower03
    scene locker03 blurred
    show rubyshower04
    ru "I'm sure a young virile monstercock like yours can handle my fit muscled body and HUGE tits!"
    mc "Of course Ruby! I'll lift you up in my strong arms and impale you on my GIANT manmeat!"
    scene lockerrubyfuck00 with dissolve
    ru "Damn, this is the biggest and hardest fuckstick I've ever had the pleasure of handling..."
    mc "It's ROCK-HARD to better SMASH your pussy Ruby!"    
    ru "Show me how STRONG and POWERFUL you are [name]!"
    scene lockerrubyfuck01 with dissolve
    ru "Your monster cock is pounding the shit out of my poor pussy, I LOVE IT! Fuck me HARDER!"
    scene lockerrubyfuck01a with dissolve
    mc "I like women who can take it like you, I'll fucking DESTROY your pussy and make it mine forever!"
    call screen rubygymdream02
    screen rubygymdream02:
        add dreamrubygym02 at center
        modal True
        button:
            imagebutton:
                focus_mask True
                idle "Icons/nextidle.png"
                hover "Icons/nexthover.png"
                action Jump ("DreamRubyGymEnd02")    
    label DreamRubyGymEnd02:
    ru "AAAH, ooh! YES, YES! Give it to me [name], I want ALL of it!"
    mc "You want more huh? You want more of that monster teen cock hey?"
    ru "YES, SMASH my pussy! FASTER!"
    call screen rubygymdream
    screen rubygymdream:
        add dreamrubygym at center
        modal True
        button:
            imagebutton:
                focus_mask True
                idle "Icons/nextidle.png"
                hover "Icons/nexthover.png"
                action Jump ("DreamRubyGymEnd")    
    label DreamRubyGymEnd:
    mc "Let's switch position, lean against the shower wall..." 
    scene lockerrubyfuck02 with dissolve
    ru "That dick is just so good, ssooo fucking good. Kiss me while you take me [name]..."
    scene lockerrubyfuck03 with dissolve
    play sound "Sounds/kiss.mp3"
    ru "And you're a great kisser too. What a TOTAL STUD! Fuck me some more please! HARDER, make me COME!"
    scene lockerrubyfuck02 with dissolve    
    ru "I'm cumming, shit, I'm cumming so hard with your cock ssoo DEEP inside me, AAAAH!"
    mc "I'm gonna cum too! Your belly will swell with my mighty cumload! RHHHHAAAA!"
    scene lockerrubyfuck04 with dissolve
    ru "Fuck, you're filling me up like a spermtank with your MASSIVE loads!"
    mc "Fuck yeah! I've got tons more creamy sauce to feed your hungry hole Ruby!"
    ru "AAAH, what a TORRENT of young virile spunk!"
    stop music
    play music "Sounds/shower.mp3"
    scene lockermccum01 with dissolve
    mc "Yeah, feel my jets of spunk inside you Ruby! AAAH!"    
    jump ShowerEnd

if aylagym:
    menu:
        "Like Ayla...":
            jump AylaDream01
        "Skip":
            jump ShowerEnd
    label AylaDream01:            
    play sound "Sounds/dream.mp3"
    scene locker03dream with dissolve
    show aylashower01
    play music "Sounds/showerstrip.mp3"
    ay "Hello [name]... I feel like a demonic urge to jump that MASSIVE bone of yours, what d'ya say?"
    mc "I say it is wise to follow Satan's orders..."
    hide aylashower01    
    show aylashower02
    ay "My body will bring you to the DARK side of LUST and DEPRAVITY!"
    mc "I think I'm already almost there but a little help won't hurt..."
    hide aylashower02    
    show aylashower03                                            
    ay "Satan has turned me into a total sizequeen COCK-WHORE... And your MONSTER DONG is just what I NEED!"
    mc "Well, come and join me in the shower stall and I'll give you what you need! 18 thick inches of it!"
    hide aylashower03
    scene locker03 blurred
    show aylashower04
    ay "My pussy is already dripping wet! I want you to POUND the shit out of me, understood?"
    mc "Crystal clear!"
    scene lockeraylafuck01a with dissolve
    ay "Dear Belzebuth! Your cock is so big that I can suck it standing up... (kiss)"
    play sound "Sounds/kiss.mp3"
    mc "Well, you're quite tiny too... So tiny that I could easily lift you up on my rock-hard crank..."
    scene lockeraylafuck01c with dissolve    
    ay "OOOh, YES PLEASE! Show me how POWERFUL it is!"
    scene lockeraylalift01 with dissolve
    mc "Ready for lift-off?"
    ay "YES! Lift me up to the Lord of Jizz, I need to repent my sins!"
    scene lockeraylalift02 with dissolve
    ay "Fuck! You did that so easily! That love muscle is made of CONCRETE!"
    mc "And now, let me impale you on it Ayla!"
    scene lockeraylafuck02 with dissolve
    ay "Don't hold back! I might be small, but I can take your giant pussy-pleaser, all EIGHTEEN INCHES OF IT!"
    mc "You want all of my monster cock Ayla? I'll give it to you then!"
    call screen aylagymdream
    screen aylagymdream:
        add dreamaylagym at center
        modal True
        button:
            imagebutton:
                focus_mask True
                idle "Icons/nextidle.png"
                hover "Icons/nexthover.png"
                action Jump ("DreamAylaGymEnd")    
    label DreamAylaGymEnd:
    ay "That's it, claim that whore-hole, make it yours with your satanic seed!"
    mc "I'm gonna blow any time now, I'll give you a spunk enema Ayla!"
    show lockeraylafuck03 with dissolve        
    ay "YES? I can feel each and every one of your powerful wads, it's ssoo amazing! "
    mc "You want more? I'll give you MORE and take you to sex heaven Ruby!"
    stop music
    play music "Sounds/shower.mp3"
    scene lockermccum01 with dissolve
    mc "I've got some more cum showers for you Ayla, RHAAAA!"    
    jump ShowerEnd
mc "But there isn't one, I'll just wank myself silly anyway..."
scene lockermccum01 with dissolve
mc "Fuck, cumming non-stop, RHAAAA!"    
jump ShowerEnd

label ShowerEnd:
$ period += 1
show screen calendar
show screen mcstats
scene lockermccum02 with dissolve
mc "Damn, I made a right dreamy mess. I'd better clean all of it before I leave or people will think I'm a total pervert. Which I definitely AM NOT."
jump Main01

label GymOut:
if seengym:
    mc "I'd better take a shower after all this..."
    jump GymShower
jump Main01

#FOR WHEN MACHINE 02 IS IMPLEMENTED
label GymWorkout02:
$ seengym = True
scene machine02 with dissolve
mc "Let's pump iron! I want my guns to get even bigger and stronger!"

label GymWorkout02b:
play music "Sounds/mcworkout.mp3"
call screen mcgym02
screen mcgym02:
    add mcgym02 at center
    modal True
    button:
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("GymWorkoutEnd02")    

label GymWorkoutEnd02:
stop music
scene machine02 with dissolve
mc "Damn, that was a good workout! I need to POSE and FLEX those muscles!"
$ d3rollgymworkout = renpy.random.randint(1, 3)
if d3rollgymworkout == 1:
    scene gymposing01 with dissolve
    mc "Check those ripped muscles! I'm da man, I'm DA MAN!"
if d3rollgymworkout == 2:
    scene gymposing02 with dissolve
    mc "Fuck yeah! Monster teen muscle stud right here!"
if d3rollgymworkout == 3:
    scene gymposing03 with dissolve
    mc "Damn, my muscles are definitely getting BIGGER and STRONGER!"
$ mcstrengthlevel += 1
if mcstrengthlevel == 1:
    mc "A couple more workouts like this one and I'll get STRONGER for sure!"   
if mcstrengthlevel == 2:
    mc "I need another workout like this one and I'll get STRONGER for sure!"   
if mcstrengthlevel == 3:
    mc "Damn, my muscles are definitely getting BIGGER and STRONGER!"
    call PlusStrength
    $ mcstrengthlevel = 0

if rubygym:
    scene gym03
    show rubygym01
    ru "Wow, you really ARE strong [name]... I'm sorry I doubted you... Mmmh, that young muscled body of yours..."
    call LustPlusRuby
    ru "If I wasn't so butch, I'd almost jump your bone right here, right now..."
    mc "You can jump it anyways, I don't care!"
    hide rubygym01
    show rubygym03
    ru "Not now, I have to go back to the workshop to finish some manly stuff."
    hide rubygym03
    mc "Damn it!"
    jump GymOut
if lauriegym:
    scene gym04 with dissolve
    show lauriegym02
    la "I... can't believe what I just saw. You did it with such ease! Sssoo strong...."
    call LustPlusLaurie
    mc "Err. Is it me or your tits grew? And your nipples... They're HUGE now!"
    hide lauriegym02
    show lauriegym03
    la "Oh my God, this is so embarrassing... The... mutated salads... make my tits grow bigger when I'm horny. Oh no, I just said it!"
    hide lauriegym03
    show lauriegym04
    la "I'm so ashamed... Please don't tell anyone... I... I need to go now [name]..."
    hide lauriegym04
    jump GymOut
if lenagym:
    scene gym02 with dissolve
    show lenagym02
    le "Mmh, you sure are strong [name]. But not strong enough. Train some more... As much as possible."
    hide lenagym02
    show lenagym03
    le "Here, I'm offering you a new pair of posing pouches to make it \"easier\" for you to pump iron..."
    le "You can check for them in your inventory by preesing \"i\" in-game..."
    le "Now if you'll excuse me, duty calls."
    hide lenagym03
    jump GymOut
if aylagym == True and aylagymout == False:
    scene gym05 with dissolve
    show gymayla01
    ay "Possibly I should be impressed but this scene has not been implemented yet..."
    ay "So I'll just leave you like that without saying a word."
    mc "Hey, wait..."
    hide gymayla01
    jump GymOut
jump GymOut

