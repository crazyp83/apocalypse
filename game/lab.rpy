label Lab:
show screen mcstats
show screen calendar
$ loc = "lab"
$ debraout = False

label Lab01:
scene lab01 with dissolve
label Lab01b:
scene lab01
call screen lab01
screen lab01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/exitidle.png"
        hover "Icons/exithover.png"
        action Jump ("Main01")
    imagebutton:
        focus_mask True
        idle "Science/labcabinetidle.png"
        hover "Science/labcabinethover.png"
        action Jump ("LabIncubator")
    if debraout == False:
        imagebutton:
            focus_mask True
            idle "Science/labdebraidle.png"
            hover "Science/labdebrahover.png"
            action Jump ("LabDebra")
    imagebutton:
        focus_mask True
        idle "Science/labgwenidle.png"
        hover "Science/labgwenhover.png"
        action Jump ("LabGwen")
    imagebutton:
        focus_mask True
        idle "Science/radioactiveidle.png"
        hover "Science/radioactivehover.png"
        action Jump ("LabNuclear")

label LabIncubator:
hide labcabinetidle
hide labgwenidle
if debraout == False:
    show labdebraidle
show radioactiveidle
show labcabinetidle
show labgwenidle
mc "Looks like some fancy incubator for growing genetically-modified plants. This lab must be sponsored by Monsanto."
jump Lab01b

label LabNuclear:
if debraout == False:
    show labdebraidle
show radioactiveidle
show labcabinetidle
show labgwenidle
mc "These must be some kind of radioactive containers. Like we don't have enough radioactivity in the air already."
jump Lab01b

label LabGwen:
if preggwstart >=4:
    scene lab03
    show debratalking01
    with dissolve
    de "I wouldn't bother her if I were you, she's in a foul mood. Because YOU got her pregnant and ruined her non-existent scientific career!"
    hide debratalking01
    show debratalking02
    with dissolve
    de "But you can still work as a lab assistant, as long as I command it. She'll have no choice but to accept."
    menu:
        "Ok, I need some dough. Let's do some work and earn some hard cash!":
            hide debratalking02
            show debrahappy01
            with dissolve
            de "Good, did you hear that Gwen? [name] is going to work in tandem with you."
            gw "I don't need any help!"
            hide debrahappy01
            show debratalkingright01
            with fastdissolve
            de "Yes you do! You're too SLOW. Now off you go in the kiddies corner [name]."
            hide debratalkingright01
            jump LabWork00
        "Na, I'm fine, I'm loaded anyway and this job stinks.":
            hide debratalking02
            show debraoffended
            with dissolve
            de "You'll never be anything but a deplorable oaf all your life!"
            mc "Some day, I'll be president, mark my words!"
            de "Pff! Be gone, you're wasting my time!"
            hide debraoffended with dissolve
            $ seenlab = True
            jump Main01

scene lab02 with dissolve
if gwensciencefucked == True and gwenapologized == False:
    jump GwenDialogueRape
else:
    jump GwenDialogueLab

label GwenDialogueLab:
scene lab02 with dissolve
show gwen04
if missiongw01 and successmissiongw01 == False:
    gw "I'm still recovering from being raped by you..."
    jump GwenLabDialogueChoice
if toldsuccessmissiongw01 == False and successmissiongw01:
    gw "Now we're even. You raped me and I raped Debra."
    show missionsuccessgw01 at posmission
    mc "Sounds totally even to me indeed. Especially since I didn't get raped."
    hide missionsuccessgw01
    $ toldsuccessmissiongw01 = True
    jump GwenLabDialogueChoice
if successmissiongw02:
    gw "I'm working as you can see. So please be quick with whatever you have to say, Debra is watching us!"
    jump GwenLabDialogueChoice
gw "I'm working as you can see. I don't want to be disturbed, I really need to finish my PhD!"
label GwenLabDialogueChoice:
menu:
    "But I would like to offer you this necklace I found on my adventures!" if necklace:
        hide gwen04
        show gwen03        
        if gwensciencefucked:
            gw "For me? Of all the girls, you chose me? Or is it to apologize for raping me? In any case, I'll gladly accept your gift [name]!"
        if gwensciencefucked == False:
            gw "For me? Of all the girls, you chose me? Wow, I feel so special now. Let me see it [name]!"
        scene lab02 blurred with dissolve
        show gwennecklace
        $ necklace = False
        gw "Thanks, I really like it! I'll take it back to my room tonight. But now I have to go back to work."
        call LustPlusGwen
        mc "Sure, I'll leave you to it then."
        scene lab01 with dissolve
        show debraoffended
        de "Stop disturbing my lab assistant [name]. I'm PAYING her to work. Now get out of my lab."
        hide debraoffended
        $ seenlab = True
        jump Main01
    "I'd like to show you something (hypnotize her, +1 lust)" if pendulum and showedpendulum == False:
        call UsePendulum
        hide gwen04
        show gwen05
        with fastdissolve
        gw "Wh...what happened... Oh, hi [name], you look... smart today..."
        call LustPlusGwen
        gw "Err... I don't know why I said that, I mean, you don't even have a PhD. I have to go back to work now."
        $ showedpendulum = True
        scene lab01 with dissolve
        show debraoffended
        de "Stop disturbing my lab assistant [name]. I'm PAYING her to work. Now get out of my lab."
        hide debraoffended
        $ seenlab = True
        jump Main01
    "Would you like to escape this dangerous lab and go on a date with me? (date with Gwen tomorrow morning)" if lustgw >= 2 and gwendatedone == False and knowredcanyon:
        hide gwen04
        show gwen03
        with fastdissolve
        gw "A date? I haven't been on one since... A long time. Because of this damn PhD that takes forever."
        mc "Also cos they aren't many men around."
        hide gwen03
        show gwen02
        with fastdissolve
        gw "That's true too. Agreed then! Now let me get back to work so I can get ahead and have time to waste on a date with you tomorrow morning."
        hide gwen02 with dissolve
        $ gwendateon = True        
        $ seenlab = True
        jump Main01
    "Maybe I can help you finish it faster?" if missiongw02 and successmissiongw02 == False:
        if helpedgwenthesis == 0:
            hide gwen04
            show gwen03
            with fastdissolve
            gw "Mmmh, why not. You won't get paid anything, I'm warning you."
            mc "I do it because I want to... help you."
            hide gwen03
            show gwen02
            with fastdissolve
            gw "How kind of you. Although I strongly suspect you expect an extra lust point from me at the end of this mission..."
            mc "Pfff. far be it from me to have such petty concerns!"
            hide gwen02
            show gwen04
            with fastdissolve
        gw "Sure... Well, get to work then. I'll tell you what to do and you just follow my orders, alright?"
        mc "No problemo! I'm used to obeying orders by now!"
        $ helpedgwenthesis += 1
        scene lab02 with fade
        $ period += 1
        hide gwen04
        show gwen01
        with fastdissolve
        if helpedgwenthesis == 1:
            gw "Well, thanks, that was sure helpful. I managed to finish the 3rd chapter of my thesis today!"
            mc "That's great. And... err... How many chapters are they supposed to be exactly?"
            gw "Five."
        if helpedgwenthesis == 2:
            gw "Well, thanks, that was sure helpful. I managed to finish the 4th chapter of my thesis today!"
            mc "That's great. And... err... How many chapters are they supposed to be exactly?"
            gw "Five."
        if helpedgwenthesis >= 3:
            gw "Well, thanks, that was sure helpful, I can finally submit my thesis!"
            window hide
            show missionsuccessgwen02 at posmission
            $ renpy.pause(2.0, hard=True)
            pause
            hide missionsuccessgwen02
            $ successmissiongw02 = True            
            call LustPlusGwen
            mc "Ah, finally, that extra lust point!"
            gw "Now I have to print it send it to Trumpf University. See you later [name]!"
            hide gwen01 with dissolve
            jump Main01
        mc "Well, I'll leave you to it then, I have to go."
        scene lab01 with dissolve
        jump Main01
    "I think the time is ripe for you to join my harem." if lustgw >= 4 and haremgw == False and gwenharem == False and girlsinharem <= 5 and gwendatedone:
        hide gwen04
        show gwen02
        with fastdissolve
        gw "I don't know... I mean, I AM attracted by the offer, but I don't want you to RAPE me again."
        mc "If you're in my harem, it won't be rape by definition. So everything's fine and dandy."
        $ haremgw = True
        hide gwen02
        show gwen03
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
        gw "Then, I should prepare myself for that. Emotionally I mean. See you, [name]!"
        hide gwen03 with fastdissolve 
        mc "And I guess I'll leave too and get my mind off her hot bod..."
        $ seenlab = True
        jump Main01
    "I think it's time for you to re-join my harem Gwen..." if lustgw >= 4 and haremgw == False and gwenharem  and gwendismissed == False  and girlsinharem <= 5:
        hide gwen04
        show gwen02
        with fastdissolve
        gw "Perhaps I can give you a second chance..."
        mc "Not just perhaps. You will. You know you can't live with my HUGE COCK, right?"
        hide gwen02
        show gwen03
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
        hide gwen03
        show gwen04
        with fastdissolve
        gw "Alright! I'm so excited, I have to... go back to work and get my mind off IT!" 
        hide gwen04 with fastdissolve 
        mc "And I guess I'll leave too and get my mind off her hot bod..."
        $ seenlab = True
        jump Main01
    "Sure, I'll leave you to it then.":
        hide gwen04
        jump Lab01

mc "Sure, I'll leave you to it then."
hide gwen04
jump Lab01

label LabDebra:
scene lab03 with dissolve
show debratalking01

if worklab == 0 and workedlab == False:
    de "Hello [name]. Are you here to apply for a position in my lab?"
    jump DebraDialogueMenu01    
if worklab == 0 and workedlab:
    de "Ah, the young and inquiring mind who needs money is back!"
    jump DebraDialogueMenu01    
if worklab == 1 and gwensciencefucked == False and preggwstart <= 3:
    de "Ah, I'm glad you came, I just needed an extra assistant for an experiment..."
    jump DebraDialogueMenu01    
if worklab == 1 and week >= 3 and debraexperiment == False and gwensciencefucked and preggwstart <= 3:
    de "Ah, I'm glad you came, I just needed an extra assistant for an experiment..."
    jump DebraDialogueMenu01
if worklab == 1 and week >= 6 and debraexperiment and gwensciencefucked and debraspermcaught == False and debraspermlost == False  and preggwstart <= 3:
    de "Ah, I'm glad you came, you will assist me and make sure everything goes right this time."
    mc "Hey! I didn't volunteer for anything yet!"
    hide debratalking01
    show debrapointing
    with fastdissolve
    de "Irrelevant, I volunteered you and that's all that matters. Gwen, hop along too, you might prove yourself useful for once!"
    window hide
    show debrapointing at midright with move
    show gwen03 at midleft 
    with fastdissolve
    de "Now listen up, minions. Since I can't trust you NOT to turn into some degenerate monster inside the alpha-radiation machine, I will be the subject of my own experiment."
    hide gwen03
    show gwen02 at midleft
    with fastdissolve
    gw "Finally, some good news! So what do you need us for?"
    hide debrapointing
    show debratalkingright01 at midright
    with fastdissolve
    de "Just...in case. [name] will have the antidote at the ready while you will follow my instructions to power up the device."
    mc "Where should I inject you with the antidote Professor? The butt or the boobs?"
    hide debratalkingright01
    show debratalking01 at midright
    with fastdissolve
    de "Shut up! I will not turn into a brainless zombie since my intellect is far superior to yours. Therefore, I shall be able to orally formulate my orders if need be."
    mc "Alright, your call..."
    de "Now follow me to the alpha-chamber."
    jump DebraExperiment02
if worklab == 1 and week >= 6 and debraexperiment and gwensciencefucked and debraspermcaught == False and debraspermlost and preggwstart <= 3:
    $ debraexperiment02 = True
    de "Ah, I'm glad you came, we shall repeat the last experiment and this time, YOU'D BETTER CATCH MY FUTA SPERM!"
    mc "What? So I can take a beating once again! No thank you!"
    hide debratalking01
    show debrapointing
    with fastdissolve
    de "You didn't quite catch the part where I said that YOU DON'T HAVE A CHOICE IN THE MATTER. Gwen, you are also compelled to assist, come over here!"
    window hide
    show debrapointing at midright with move
    show gwen03 at midleft 
    with fastdissolve
    de "Now don't screw it up this time, get the bucket ready, I need the FULL DOSE for my analysis!"
    hide gwen05
    show gwen06 at midleft
    with fastdissolve
    gw "[name], I am holding YOU responsible this time if I end up in the medbay again..."
    hide debrapointing
    show debratalkingright01 at midright
    with fastdissolve
    de "I like your attitude Gwen, it is always best to blame the underlings in all situations, I see you are fast learning from ME!"
    mc "Hey! Where's MY underling that I can blame then?"
    hide debratalkingright01
    show debrapointing at midright
    with fastdissolve
    de "You don't have any since you are at the BOTTOM of the ladder. Now shut up and let's move to the alpha-chamber."
    jump DebraExperiment02b
if worklab >= 1 and debraspermcaught:
    de "Ah, the young and inquiring mind who needs money is back! Unfortunately, I don't need you for anything today."
    if donemissionwi01 and week >= 8 and debranancyagree == False:
        mc "Ah, but this time, I'm the one who needs YOU. And your machine."
        hide debratalking01
        show debrapointing
        with fastdissolve
        de "And why the hell would I agree to work for YOU, silly apprentice?"
        mc "Well, this is your opportunity to show the world that your invention actually works for something. I have an idea for an experiment that CANNOT FAIL."
        hide debrapointing
        show debrabored
        with fastdissolve
        de "Keep going, so I can have a good laugh at the end..."
        mc "Err.. I suppose your machine has a reverse polarity button?"
        hide debrabored
        show debraoffended
        with fastdissolve
        de "Of course it has! What kind of world-class scientific equipment would it be WITHOUT a reverse polarity button?"
        mc "My mo... I mean landlady, gets the same kind of unbearable pain your machine inflicts on the unfortunate souls who enter it and..."
        hide debraoffended
        show debratalking01
        with fastdissolve
        de "What pain? I felt GREAT when I was in there!"
        mc "And I reckon that using reverse polarity might allow her to wear her Captain Marvel costume painlessly. It's covered in alpha-rays."
        hide debratalking01
        show debrapensive
        with fastdissolve
        de "Mmh, interesting. Reversing the polarity of the alpha-radiations might turn them into anti-quark alpha-protons. Yes, it might just work. Isn't science fun?"
        mc "Err, yeah, it's a real riot."
        hide debrapensive
        show debrapointing
        with fastdissolve
        de "Well, what are you waiting for, get Nancy back here and we'll test your silly theory! Of course, if something goes wrong, you'll be ENTIRELY RESPONSIBLE!"
        $ debranancyagree = True
        jump Lab
    menu:
        "What a shame... I so much wanted to be a guinea pig for you.":
            $ debraout = True
            jump Lab
        "How about you get some sun and go on a date with me? (date with Debra in the morning)" if lustde  >= 2 and debradatedone == False:
            hide debratalking01
            show debrapensive
            with fastdissolve
            de "Leaving the lab? With Gwen in charge?"
            $ debradateon = True
            mc "Just give her some menial task so she doesn't blow it up. You NEED to get out. For your own mental health."
            hide debrapensive
            show debrapointing
            with fastdissolve        
            de "Fine, but I hold YOU responsible if anything happens in my absence in this lab!"
            mc "Alright! I'll pick you up in the morning then."
            $ seenlab = True
            jump Main01
        "I think it's time now for you to join my harem Debra. And try out some experimental SEX with me!" if lustde >= 4 and haremde == False and debraharem == False and girlsinharem <= 5:
            hide debratalking01
            show debratalking02
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
            hide debratalking01
            show debraoffended
            with fastdissolve
            de "You dared to throw me out! Me, being thrown out of the harem of an underling!"
            mc "I was just testing. Like, experimenting if you wish. But now I know the limits of my experimental procedure."
            hide debraoffended
            show debrapointing
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

label DebraDialogueMenu01:
show debratalking01
menu:
    "What experiment? I'm all ears..." if worklab == 1 and week >= 3 and debraexperiment == False and gwensciencefucked:
        hide debratalking01
        show debrahappy01
        de "I like your enthusiasm. I'll take that as a yes and we shall therefore proceed with it today."
        gw "Nice one [name]... Now we're stuck with doing some crazy shit that might kill us!"
        jump ScienceTwo        
    "I would really like to help you in your research. For money.":
        hide debratalking01
        show debrahappy01
        if workedlab == False:
            de "Good. Cos I need a new lab rat, I mean lab assistant. Gwen is too weak."
            gw "I'm only weak because you keep firing shit at me!"
            hide debrahappy01
            show debratalkingright01
            with fastdissolve
            de "Stop complaining, this is a well-paid job that many girls here would fight for."
            hide debratalkingright01
            show debratalking01
            with fastdissolve
        if workedlab:
            de "That's great. And I'm ready to give you menial tasks befitting your lower intellect. You will work in tandem with Gwen...."
            gw "I don't need any help!"
            hide debrahappy01
            show debratalkingright01
            with fastdissolve
            de "Yes you do! You're too SLOW. Now off you go in the kiddies corner [name]."
            hide debratalkingright01
            jump LabWork00
        de "I'm putting the final details on a future experiment I plan that will change the course of history! I count on your full and voluntary forced participation in it when it's ready."
        de "But for now, I have much work to finish. You will therefore help Gwen over there. Doing some kiddie science stuff."
        gw "Hey! I'm doing a PhD THESIS here!"
        hide debratalking01
        show debratalkingright01        
        de "Sure, sure. Let me know when it's finished! (snickers)"
        jump LabWork00
    "I'm ready to give my body for science!" if worklab == 1 and gwensciencefucked == False:
        if worklab == 1:
            hide debratalking01
            show debrahappy02
            with fastdissolve
            de "Excellent! I so happen to have finished setting my new device and I need a healthy young subject."
            hide debrahappy02
            show debrapointing
            with fastdissolve
            de "Since Gwen is too weak, that subject will be YOU!"
            hide debrapointing
            show debratalkingright01
            with fastdissolve
            de "Come over here Gwen, you will also assist me in this new and exciting endeavor! While you come over, I will magically slide towards my left."
            window hide
            show debratalkingright01 at midright with move
            show gwen03 at midleft
            mc "I'm having second thoughts... What are you going to do to me exactly? Fire nasty stuff at me?"
            hide debratalkingright01
            show debratalking02 at midright
            de "Ah, an inquisitive mind! I like it. But next time, do shut up, you only need to listen and obey."
            gw "Welcome to my world [name]..." 
            hide debratalking02
            jump Science01
    "I meant to ask you about that cyborg girl you created..." if askeddebracyrl == False:
        hide debratalking01
        show debrapensive
        de "Cyrl? My biggest mistake. As soon as she reached self-awareness, she became a nightmare."
        hide debrapensive
        show debraoffended
        with fastdissolve
        de "She stopped obeying my orders and started thinking she had equal rights to humans. Pff!"
        de "I don't want to see her again. And if she ever needs her mushy brains repaired, she can go and get stuffed!"
        mc "Wow, that's harsh. She seems like a nice girl. I mean robot. Or whatever."
        hide debraoffended
        show debrabored
        de "Don't trust her. I bet she wants to overthrow the human race. That's why I will NEVER make another intelligent cyborg again."
        de "I have enough subversion to deal with with that dolt Gwen."
        hide debrabored
        $ askeddebracyrl = True
        jump DebraDialogueMenu01
    "I meant to ask you about Gwen." if worklab == 0:
        de "My lab assistant? She was in the middle of her PhD, filing a complaint for sexual harassment againt her supervisor, when the nuclear war started."
        hide debratalking01
        show debratalking02
        with fastdissolve
        de "I worked in the same university and since she survived the apocalypse, I recruited her in my lab."
        de "Eventually, we had to move out of the city and found this compound where I can continue my research to make the world a better place."
        hide debratalking02
        show debrabored
        with fastdissolve
        de "She keeps complaining but deep down, she knows she's working for a good cause."
        hide debrabored
        jump DebraDialogueMenu01
    "Would you happen to have some strong lubricant in your lab?" if missioncy and knowpussyjuice == False:
        hide debratalking01
        show debrapensive       
        de "Lubricant... No, I'm afraid not. Anyway, the best lubricant in the world is natural. It's pussy juice."
        mc "Pussy juice?"
        hide debrapensive
        show debratalking02               
        de "Yes, as in a horny woman's squirting pussy juice. And I'm not horny right now, so don't even ask." 
        hide debratalking02
        $ knowpussyjuice = True
        jump DebraDialogueMenu01
    "Cyrl needs some heavy lubricant. I thought you might have some." if missioncy:
        hide debratalking01
        show debraoffended
        with fastdissolve
        de "Even if I had some, I would not provide this revolting creature with any of it! May her motherboard rust in hell!"        
        hide debraoffended
        jump DebraDialogueMenu01
    "I'm too busy fighting the mighty oppressors of our land. I need to go.":
        hide debratalking01
        show debrabored
        with fastdissolve
        de "That's too bad. Muscles are no match for technology."
        hide debrabored
        show debraback01
        with fastdissolve
        de "I have wasted enough time talking to you, I have much work to finish." 
        $ debraout = True
        jump Lab01

label LabWork00:
$ workedlab = True
if preggwstart <= 3:
    scene lab02
    show gwen03
    with dissolve
if preggwstart >= 4:
    scene lab02
    show gwenlabpreggo01
    with dissolve
gw "OK, just do everything I tell you, and don't drop anything!"
mc "Sure Gwen. You can count on me!"
scene lab01 with fade
$ period += 1
show debratalking01
de "Right, you worked reasonably hard, so I will pay you reasonably badly. 5 dollars."
$ money += 5
$ worklab += 1
$ seenlab = True
mc "Sssooo generous... (snickers)"
hide debratalking01
show debraback01
de "Stop moaning. That will be the rate everytime you come and work here anyway."
hide debraback01
jump Main01

label DebraExperiment02:
$ worklab += 1
$ seenlab = True
scene debrascience01 with fade
de "Do you have the antidote [name]?"
mc "Yes Debra, I have it firmly in my hand!"
de "Good. Now, Gwen, power to level 1!"
gw "Alright, Professor."
scene debrascience02 with dissolve
play music "Sounds/radiation01.mp3"
de "I feel... Very little. My genetically-superior body probably requires a heavy dose. Power to Level 3, Gwen!"
gw "Err, we're skipping level 2 then?"
de "Obey my instructions and don't ask questions!"
scene debrascience03 with dissolve
stop music
play music "Sounds/radiation02.mp3"
de "AAAAH, my muscles are... contracting... This feels sssooo GOOD!"
mc "Is Debra a known masochist, Gwen?"
gw "I only know she's a SADIST."
de "SHUT...UP... LEVEL 4... NOW!"
scene debrascience04 with dissolve
stop music
play music "Sounds/radiation02.mp3"
de "RHHHOOOOAAARRRR!"
mc "Uh oh, she's growing huge and also growing a dick. Just like you did."
gw "Oh fuck, she's gonna RAPE me! Give her the antidote, [name]! I'm turning this machine off! How do I do that, Professor?"
scene debrascience05 with dissolve
de "NO! AAAAH! I LIKE... IT! UUUUH! BIG DICK!"
mc "Sorry Gwen, but she's the boss."
gw "She's barely comprehensible, can't you see she's turning into a degenerate monster like we did?"
mc "I resent that, I was NOT a degenerate monster. Apart from that raping urge, I was perfectly fine."
scene debrascience06 with dissolve
stop music
gw "Oh thanks God, the machine stopped by itself. Look at her, she's FREAKY MASSIVE! Give her the fucking antidote, [name]!"
play sound "Sounds/moaning.mp3"
de "DICK... RHHHAAA!"
mc "She's not doing anything bad, she's just touching herself. I can sympathize with that. I do that all the time."
de "AAAR...NEED...TO....CUM!"
mc "Good girl. Jack off that monster futa cock and cum."
gw "And please don't rape me!"
de "BOY... CATCH... MY SPERM... NEED... FOR... ANALYSIS! RHOOOOAR!"
gw "I'll get the bucket, make sure she doesn't cum just yet, keep her distracted!"
mc "What... How?"
scene debrascience07 with dissolve
play music "Sounds/wank.mp3"
mc "Err... There once was a shy little girl who turned into a massive muscled futa monster and she was...err... very nice to everyone around her and..."
de "BOY...SHUT...THE...FUCK...UP! RHOAAR! BRING BUCKET OR I KILL YOU!"
mc "Alright, gee, I was just telling a nice story. Gwen? Come quick, please!"
gw "I've got it, here you are, you take care of this nonsense now, it's YOUR responsibility."
scene debrascience08 with dissolve
mc "I'm ready to catch your spermblasts in the bucket, Professor!"
de "RRHOOOOAR! DON'T... FUCKING... MISS... AAAH!"
scene debrawankbackground
show debrawank
with dissolve
window hide
show angiecatch
pause
$ d3rollsperm=renpy.random.randint(1,3)
if d3rollsperm == 1:
    call screen debracatch01
    screen debracatch01:
        modal True
        default time_left = 0.6

        add "Science/debrawankbackground.jpg"
        add "Angie/angiecatch.png"
        add "Science/debrawank10.png"
        add "Science/debracumleft01.png"
        if time_left <= 0.4:
            add "Science/debracumleft02.png"
        if time_left <= 0.2:
            add "Science/debracumleft03.png"

        if time_left <= 0:
            timer .01 action Return
        else:
            timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)

        imagebutton:
            focus_mask True
            idle "Angie/catchleft.png"
            hover "Angie/catchleft.png"
            action Jump ("CatchSperm")
        
        bar value StaticValue(time_left, 0.5):
            xalign 0.1 yalign 0.02
            xmaximum 200 
            ymaximum 10

if d3rollsperm == 2:
    call screen debracatch02
    screen debracatch02:
        modal True
        default time_left = 0.6
        
        add "Science/debrawankbackground.jpg"
        add "Angie/angiecatch.png"
        add "Science/debrawank05.png"
        add "Science/debracumcenter01.png"
        if time_left <= 0.4:
            add "Science/debracumcenter02.png"
        if time_left <= 0.2:
            add "Science/debracumcenter03.png"

        if time_left <= 0:
            timer .01 action Return
        else:
            timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)

        imagebutton:
            focus_mask True
            idle "Angie/catchcenter.png"
            hover "Angie/catchcenter.png"
            action Jump ("CatchSperm")
        
        bar value StaticValue(time_left, 0.5):
            xalign 0.1 yalign 0.02
            xmaximum 200 
            ymaximum 10

if d3rollsperm == 3:
    call screen debracatch03
    screen debracatch03:
        modal True
        default time_left = 0.6

        add "Science/debrawankbackground.jpg"
        add "Angie/angiecatch.png"
        add "Science/debrawank00.png"
        add "Science/debracumright01.png"
        if time_left <= 0.4:
            add "Science/debracumright02.png"
        if time_left <= 0.2:
            add "Science/debracumright03.png"

        if time_left <= 0:
            timer .01 action Return
        else:
            timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)

        imagebutton:
            focus_mask True
            idle "Angie/catchright.png"
            hover "Angie/catchright.png"
            action Jump ("CatchSperm")
        
        bar value StaticValue(time_left, 0.5):
            xalign 0.1 yalign 0.02
            xmaximum 200 
            ymaximum 10

label CatchSpermFail:
hide debrawank
stop music
scene debrawankendfail01 with dissolve
$ renpy.pause(1.0, hard=True)
mc "Shit, I was too slow... And she came all over me instead of inside the bucket."
$ debraspermlost = True
scene debrawankendfail02 with dissolve
de "RHOOOOAR! BAD... MINIONS!"
gw "Aaah, you're hurting... *cough*... ME!"
mc "What the...?"
scene black with fade
pause 1
$ loc = "medbay"
$ period = 3
scene medbay03 with fade
play music "Sounds/beep.mp3"
show rachel01 with dissolve
ra "Wakey wakey young man!"
mc "Wh... Where am I?"
hide rachel01
show rachel06
with fastdissolve
ra "You're in the medical bay silly boy. Don't you recognize me?"
mc "What happened? I can't remember anything."
hide rachel06
show rachel02
with fastdissolve
ra "You took a serious beating from Professor Giant-Futa-Dick Debra."
mc "What? How serious? How is my... penis?"
hide rachel02
show rachel01
with fastdissolve
ra "Your cock is fine, I checked it first thing you arrived here."
mc "What a relief! And... err.. Gwen is fine too?"
hide rachel01
show rachel04
with fastdissolve
ra "Well, that's nice of you to be inquiring about her health. She also took a beating, Doctor Tara is taking care of her."
hide rachel04
show rachel03
with fastdissolve
ra "Which means... She won't come to mess with us tonight!"
mc "I see. You want to bang an almost comatosed patient."
ra "But one with a functioning dick!"
hide rachel03
show rachel10
with fastdissolve
ra "So come on, horny boy, pull those sheets off and let me climb on that bed... And on your BIG HARD COCK!"
mc "Alright, if you must..."
jump MedbayNew

label CatchSperm:
hide debrawank
stop music
scene debrawankendgood01 with dissolve
$ debraspermcaught = True
$ renpy.pause(1.0, hard=True)
mc "Yeah, I caught most of that gallon of futa sperm!"
de "AAARRR... GOOD.. BOY..."
scene debrawankendgood02 with dissolve
gw "Looks like she's going back to normal after her giant cum release..."
scene debrawankendgood03 with dissolve
de "*Phew* That was... intense. Well done [name], you caught my genetically-superior female sperm. Give me the bucket, I'll do an analysis straight away."
call LustPlusDebra
gw "And what about our payment for carrying through with this crazy idea of yours?"
de "You shouldn't be asking for money when you just witnessed the most important scientific discovery this decade! Shame on you, Gwen..."
gw "Umpf... We got ripped off, once again."
mc "I got a lust point out of it so I'm happy."
de "Now get out of here, I need to get dressed!"
scene lab01 with fade
$ period += 1
jump Main01

label DebraExperiment02b:
$ worklab += 1
$ seenlab = True
scene debrascience01 with fade
de "Do you have the bucket [name]?"
mc "Yes Debra, I have it at the ready to catch your giant load of...err... futa cum."
de "Good. Now, Gwen, power to level 3!"
gw "What? What happened to levels 1 and 2???"
de "Nothing will happen to my body at such lame levels of radiations, so do as you're told!"
scene debrascience03 with dissolve
play music "Sounds/radiation02.mp3"
de "AAAAH, my muscles are... contracting... This feels sssooo GOOD! Just like last time."
mc "I hope this shit works."
de "SHUT...UP... LEVEL 4... NOW!"
scene debrascience04 with dissolve
stop music
play music "Sounds/radiation02.mp3"
de "RHHHOOOOAAARRRR!"
mc "Yep, seems to be working, the monster futa dick has already appeared."
scene debrascience07 with dissolve
stop music
gw "Oh thanks God, the machine stopped by itself. Say nice things to her and get her to start jacking off! I don't want to be raped."
de "DICK... RHHHAAA!"
mc "Yes, that's right, you have a dick, good girl. Now put your hands on it and rub it... It feels good doesn't it?"
de "AAAR...NEED...TO....CUM! CATCH...MY SPERM...YOU...MORON!"
scene debrascience08 with dissolve
mc "I'm ready to catch your spermblasts in the bucket, so blast away, Professor!"
de "RRHOOOOAR! DON'T... FUCKING... MISS... AAAH!"
scene debrawankbackground
show debrawank
with dissolve
play music "Sounds/wank.mp3"
window hide
show angiecatch
pause
$ d3rollspermb=renpy.random.randint(1,3)
if d3rollspermb == 1:
    call screen debracatch01b
    screen debracatch01b:
        modal True
        default time_left = 0.6

        add "Science/debrawankbackground.jpg"
        add "Angie/angiecatch.png"
        add "Science/debrawank10.png"
        add "Science/debracumleft01.png"
        if time_left <= 0.4:
            add "Science/debracumleft02.png"
        if time_left <= 0.2:
            add "Science/debracumleft03.png"

        if time_left <= 0:
            timer .01 action Return
        else:
            timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)

        imagebutton:
            focus_mask True
            idle "Angie/catchleft.png"
            hover "Angie/catchleft.png"
            action Jump ("CatchSpermb")
        
        bar value StaticValue(time_left, 0.5):
            xalign 0.1 yalign 0.02
            xmaximum 200 
            ymaximum 10

if d3rollspermb == 2:
    call screen debracatch02b
    screen debracatch02b:
        modal True
        default time_left = 0.6
        
        add "Science/debrawankbackground.jpg"
        add "Angie/angiecatch.png"
        add "Science/debrawank05.png"
        add "Science/debracumcenter01.png"
        if time_left <= 0.4:
            add "Science/debracumcenter02.png"
        if time_left <= 0.2:
            add "Science/debracumcenter03.png"

        if time_left <= 0:
            timer .01 action Return
        else:
            timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)

        imagebutton:
            focus_mask True
            idle "Angie/catchcenter.png"
            hover "Angie/catchcenter.png"
            action Jump ("CatchSpermb")
        
        bar value StaticValue(time_left, 0.5):
            xalign 0.1 yalign 0.02
            xmaximum 200 
            ymaximum 10

if d3rollspermb == 3:
    call screen debracatch03b
    screen debracatch03b:
        modal True
        default time_left = 0.6

        add "Science/debrawankbackground.jpg"
        add "Angie/angiecatch.png"
        add "Science/debrawank00.png"
        add "Science/debracumright01.png"
        if time_left <= 0.4:
            add "Science/debracumright02.png"
        if time_left <= 0.2:
            add "Science/debracumright03.png"

        if time_left <= 0:
            timer .01 action Return
        else:
            timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)

        imagebutton:
            focus_mask True
            idle "Angie/catchright.png"
            hover "Angie/catchright.png"
            action Jump ("CatchSpermb")
        
        bar value StaticValue(time_left, 0.5):
            xalign 0.1 yalign 0.02
            xmaximum 200 
            ymaximum 10
            
label CatchSpermFailb:
hide debrawank
stop music
scene debrawankendfail01 with dissolve
mc "Shit, I was too slow... She's going to get angry again..."
$ debraspermlost = True
scene debrawankendfail02 with dissolve
de "RHOOOOAR! BAD... MINIONS!"
gw "Aaah, you're hurting... *cough*... ME!"
mc "What the...?"
scene black with fade
pause 1
$ loc = "medbay"
$ period = 3
scene medbay03 with fade
play music "Sounds/beep.mp3"
show rachel01 with dissolve
ra "Wakey wakey young man!"
mc "Wh... Where am I?"
hide rachel01
show rachel06
with fastdissolve
ra "You're in the medical bay silly boy. Don't you recognize me?"
mc "What happened? I can't remember anything."
hide rachel06
show rachel02
with fastdissolve
ra "You took a serious beating from Professor Giant-Futa-Dick Debra. Again."
mc "What? How serious? How is my... penis?"
hide rachel02
show rachel01
with fastdissolve
ra "Your cock is fine, I checked it first thing you arrived here. Like last time."
mc "What a relief! And... err.. Gwen is fine too?"
hide rachel01
show rachel04
with fastdissolve
ra "Well, that's nice of you to be inquiring about her health. She also took a beating, Doctor Tara is taking care of her."
hide rachel04
show rachel03
with fastdissolve
ra "Which means... She won't come to mess with us tonight! Again."
mc "Alright, here we go again."
ra "That's right, I'm a nympho and you know it!"
hide rachel03
show rachel10
with fastdissolve
ra "So come on, horny boy, pull those sheets off and let me climb on that bed... And on your BIG HARD COCK!"
jump MedbayNew

label CatchSpermb:
hide debrawank
stop music
scene debrawankendgood01 with dissolve
$ debraspermcaught = True
$ renpy.pause(1.0, hard=True)
mc "Yeah, I caught most of that gallon of futa sperm!"
de "AAARRR... GOOD.. BOY..."
scene debrawankendgood02 with dissolve
gw "Looks like she's going back to normal after her giant cum release..."
scene debrawankendgood03 with dissolve
de "*Phew* That was... intense. Well done [name], you caught my genetically-superior female sperm. Give me the bucket, I'll do an analysis straight away."
call LustPlusDebra
gw "And what about our payment for carrying through with this crazy idea of yours?"
de "You shouldn't be asking for money when you just witnessed the most important scientific discovery this decade! Shame on you, Gwen..."
gw "Umpf... We got ripped off, once again."
mc "I got a lust point out of it so I'm happy."
de "Now get out of here, I need to get dressed!"
scene lab01 with fade
$ period += 1
jump Main01

label Science01:
$ worklab += 1
$ seenlab = True
show debrapointing at midright
de "What I have in mind is a completely revolutionary experiment. No firing anything at you that could injure your body, quite the contrary."
hide gwen03
show gwen02 at midleft
gw "Oh, so HE gets to do the exciting stuff and I get to be fired at?"
hide debrapointing
show debratalkingright01 at midright
de "Wait for the rest Gwen. I need [name] to be completely NAKED."
hide gwen02
show gwen05b at midleft
mc "I don't NECESSARILY have a problem with that but I'd like to know more about that experiment of yours..."
hide debratalkingright01
show debratalking01 at midright
de "Do you want to become even MORE muscular? I have converted an X-ray machine into a powerful alpha-radiations dispenser. You will be my beta-tester. Or alpha-tester if you prefer."
de "If I succeed, I could build an army of invicible Amazon warriors ready to take over the world so I can ru... I mean, so WE can rebuild this great nation in peace."
hide gwen05b
show gwen06 at midleft
gw "Who says I want to take part in this treasonous endeavor?"
hide debratalking01
show debratalkingright01 at midright
de "You want to finish your PhD? Then do as you're told and stop moaning Gwen!"
hide gwen06
show gwen05b at midleft
mc "Well, I'm all in for my part!"
hide debratalkingright01
show debraback01 at midright
de "You didn't actually have a choice but never mind. Follow me to the radiation room."
scene science02 with dissolve
show debratalking02 at center
de "Now get those trousers off and stand inside the radiation tube. I will start the machine so it's ready as soon as you are."
scene science03
gw "Actually, I'm glad it was YOU that ended up all naked in there..."
de "Stop ogling his great big dangling manhood and step back Gwen, I don't want a radiation leak onto you."
de "Ready? Activation in 3...2...1...."
scene science04 with dissolve
play music "Sounds/radiation01.mp3"
mc "AAAH! What the fuck is happening? My body, it's... in so  much pain... Stop it please!"
de "Muscle contractions are all perfectly normal and expected, don't worry. I will up the dose now..."
scene science05 with dissolve
stop music
play music "Sounds/radiation02.mp3"
mc "AAARGH! GRRRR!"
gw "Is THAT normal professor?"
de "Hang on, let me try and fix this... Oops, I dialed in the wrong number. Oh well, at least it clearly works."
gw "He keeps growing and growing... And his cock too!"
scene science06 with dissolve
stop music
play sound "Sounds/hulkgrowl01.mp3"
mc "NEED... TO... FUCK..."
gw "You've turned him into a SEX MONSTER! Do something about it!"
de "Err... I've lost control, I think you'd better run for your life Gwen, he seems mighty horny right now and you're the nearest pussy to him!"
scene science07 with dissolve
gw "Hey, let me go you oaf!"
mc "SMELL... PUSSY... AAAARRR!"
de "Stop fighting him, you'll get him even madder, just bide your time while I prepare an antidote."
scene science08 with dissolve
gw "His monstrous hands are fondling my tits, this is so humiliating... Help me, I beg you Debra!"
de "Yes, yes, I'm going as fast as I can, just pretend you enjoy it!"
mc "BOOBIES... BIG BOOBIES...."
de "See? He seems to like your breasts. This will buy us some time."
mc "PUSSY... BIG PUSSY...."
de "Ah. That is definitely not good news for you my dear Gwen..."
gw "Is he going to rape me?"
scene science09 with dissolve
de "I'd say it looks increasingly likely."
gw "He's going to KILL me with that thing!"
de "It certainly is going to re-arrange your insides..."
mc "FUCK... PUSSY..."
label Science01b:
scene science10 with dissolve
call screen sciencefuck01
screen sciencefuck01:
    add sciencefuck01
    modal True
    button:
        xpos .91
        ypos .44
        xysize(140, 80)        
        action Jump ("ScienceFuck02")
        
label ScienceFuck02:
scene science12 with dissolve
mc "CUM... INSIDE... PUSSY..."
play sound "Sounds/splooge02.mp3"
gw "AAAH, he's forcing his filthy load inside me!"
de "Almost done, filling up the syringe, just hang in there Gwen!"
scene science13 with dissolve
gw "I'm about to burst, ther's so much cum filling me up!"
mc "CUM... MORE... CUM..."
de "Keep him occupied, I'll inject the antidote in his buttcheek!"
scene science14 with dissolve
de "There, gotcha! How are you doing up there Gwen?"
gw "Gggg..."
stop sound
scene science15 with dissolve

de "Finally, he's out and he'll go back to normal soon. Which is a damn shame."
call LustPlusDebra
gw "Aahhh, I'm gonna faint..."
de "...And poor Gwen is going to take some time to recover from this ordeal."
de "I guess I'd better call the medical team to take over from here. And the cleaning ladies too."
$ gwensciencefucked = True
scene black with fade
pause 1

label MedbayScience:
$ loc = "medbay"
$ period = 3
scene medbay03 with fade
play music "Sounds/beep.mp3"
show rachel01 with dissolve
ra "Wakey wakey young man!"
mc "Wh... Where am I?"
hide rachel01
show rachel06
with fastdissolve
ra "You're in the medical bay silly boy. Don't you recognize me?"
mc "What happened? I can't remember anything."
hide rachel06
show rachel02
with fastdissolve
ra "Professor Debra says you turned into a sex monster after an experiment went wrong and she had to inject you with a horse-sized dose of ketamine to stop you from killing Gwen."
mc "Killing Gwen?"
hide rachel02
show rachel01
with fastdissolve
ra "Yes, you raped her silly with your giant monster cock and came buckets inside her."
mc "What? Is... Is she okay?"
hide rachel01
show rachel04
with fastdissolve
ra "Well, apart from the fact that Doctor Tara had to pump a gallon of spunk out of her belly and stick a full ice pack up her poonani to keep the swelling down, she's doing fine."
mc "Oh My God, that's terrible. I feel so bad for her."
ra "I'd say she's a lucky girl, she got to feel your monster three foot-long cock inside her..."
mc "Err... It looks like I'm restrained to the bed."
hide rachel04
show rachel01
with fastdissolve
ra "Yes, Professor Debra said it's for the best. While you have gone back to normal, she's worried you might have a relapse. I'm here to watch over you in case you do."
hide rachel01
show rachel05
with fastdissolve
ra "Imagine that, you'd have a three-foot long hard dong for me to play with! I hope you DO relapse (giggles)."
mc "This is not funny nurse. I almost killed Gwen."
hide rachel05
show rachel06
with fastdissolve
ra "Well, you can apologize to the poor girl once she's recovered, but in the meantime, YOU need to recover. So go back to sleep sweetie pie."
stop music
scene black with dissolve
pause 1
scene medbay02 with fade
hide screen calendar
"You wake up the next day feeling much better."
show rachel01
show medbay02b
ra "You slept like a LOG. And you were carrying one between your legs too!"
mc "My head... It's spinning..."
hide rachel01
hide medbay02b
show rachel05
show medbay02b
ra "You'll be fine. Dr Tara gave you the all-clear. Now off you go [name], I hope to see you again here SOON!"
hide rachel05
with dissolve
mc "I'd better get back to my bedroom and get some new clothes for the day..."
$ loc = "bedroom"
call NewDay
jump Bedroom

label ScienceTwo:
$ debraexperiment = True
$ seenlab = True
de "Stop moaning and come along. I will again MAGICALLY slide to the right for your sprite to appear in due course..."
show debrahappy01 at midright with move
show gwen06 at midleft with moveinleft
gw "Damn it..."
hide debrahappy01
show debrapointing at midright
de "Now listen up. The only reason the previous experiment failed is that Gwen distracted me at a crucial time point."
hide gwen06
show gwen02 at midleft
gw "Oh, I get it, it's all MY fault AGAIN, is it?"
hide debrapointing
show debratalkingright01 at midright
de "... And therefore, in order to avoid any hiccups this time, YOU will get in the machine."
hide gwen02
show gwen08b at midleft
gw "This is nuts! And I have to get naked too?"
de "We all know you're a stripper by night because you spend all the money I pay you as soon as you get your wasteful hands on it, so what's the big deal?"
mc "I sure as hell ain't going back into that radiation tube, I don't want to hurt anyone."
hide gwen08b
show gwen02 at midleft
gw "FINE! I'll go into your damn doomsday machine, and hopefully, I'll end up killing both of you!"
hide debratalkingright01
show debratalking01 at midright
de "Now, now, calm down Gwen, don't get your knickers in a twist. Actually, take them off, I need you totally naked. The machine doesn't accept any material other than human flesh."
scene science02 with dissolve
show debratalking02 at center
de "Just stand on the side and get ready to use your strength to restrain her if she goes berserk, alright [name]?"
mc "Ah, I see you actually have doubts about the success of this experiment after all..."
de "Certainly NOT! I'm just prepared this time, that's all. Now do as you're told and shut up!"
scene science21 with dissolve
de "So, are you ready to get buffed up Gwen?"
gw "I don't feel good about this..."
mc "I hope her tits will get bigger too professor."
gw "Shut up, pervert! And stop looking at me like you want to rape me. You already did that!"
mc "It wasn't my fault, I was somebody else, I would never hurt you Gwen!"
de "Stop arguing, I need to concentrate. Activating sequence."
de "3... 2... 1... Alpha-radiations level 1 activated."
scene science22 with dissolve
play music "Sounds/radiation01.mp3"
gw "It... hurts a bit..."
de "Everything fine on my side, wait for your muscles to contract and grow..."
scene science23 with dissolve
gw "I'm growing, I can feel it!"
mc "And we can see it..."
de "Activating Level 2..."
scene science24 with dissolve
stop music
play music "Sounds/radiation02.mp3"
gw "I'm... still growing...! But it hurts so much!"
de "The pain will subside, hold it!"
mc "Wow... her tits..."
scene science25 with dissolve
play sound "Sounds/hulkgrowl01.mp3"
gw "AAARGH! GRRRR!"
mc "Pretty much exactly what I said at this stage of the procedure..."
de "Stop distracting me [name]. Damn, why is it doing this again?"
stop music
scene science26 with dissolve
mc "I don't want to alarm you Professor, but she'a actually growing a COCK now. A BIG ONE might I add..."
gw "NEED... TO... FUCK..."
gw "...DEBRA!"
de "Restrain her [name], restrain her quickly!"
menu:
    "Try and restrain Gwen (+1 Lust Debra if successful - STRENGTH test)":
        jump GwenRestrain
    "Let her rape Debra (Get back at Debra/ +1 Lust Gwen)":
        call LustPlusGwen
        $ successmissiongw01 = True
        jump GwenDebraSex01

label GwenRestrain:
scene science27b with dissolve
mc "I will use my MIGHTY STRENGTH to restrain her Professor!"
call DiceRoll
$ dtestroll=(mcstrength+diceroll)
if (dtestroll >= 9 and not diceroll == 1) or diceroll == 6:
    window hide
    show strengthwin at posskill
    $ renpy.pause(2.0, hard=True)
    hide strengthwin
    de "Well done [name]! Now I can inject her with the antidote!"
    scene science27d
    mc "Quick, I can't hold her like that forever, she's very strong!"
    de "I've got the syringe,I'm coming over now!"
    scene science32 with fade
    show debrahappy02 at centerleft
    de "Well, she's out. Thanks to your bravery and your... huge muscles."
    call LustPlusDebra
    de "I think you also deserved HER wage. So, ten dollars it is for you, eventhough this experiment didn't quite go the way I planned..."
    $ money += 10
    mc "Yeah, I think you should go easy on the dials Professor..."
    hide debrahappy02
    show debratalking02 at centerleft
    de "Don't tell me how to do MY job! You can go now... I'll take care of her..."
    scene lab01 with dissolve
    $ period += 1
    jump Main01
if (dtestroll <= 8 and not diceroll == 6) or diceroll == 1:
    window hide
    show strengthfail at posskill
    $ renpy.pause(2.0, hard=True)
    hide strengthfail
    mc "She's.. too strong for me!"
    scene science27c with dissolve
    play sound "Sounds/punch.mp3"
    gw "FUCK...YOU!"
    window hide
    call MCInjury
    $ mcinjuredgwen = True
    gw "WILL...RAPE... DEBRA!"
    de "Shit!..."
    jump GwenDebraSex01b

label GwenDebraSex01:
scene science27 with dissolve
play sound "Sounds/hulkgrowl02.mp3"
de "Let go of me Gwen! And DO SOMETHING [name] for God's sake!"
mc "Remind me where that antidote is again?"
gw "PUSSY...NEED...TO...FUCK...PUSSY...."
jump GwenDebraSexSlow

label GwenDebraSex01b:
scene science27 with dissolve
de "Let go of me Gwen!"
play sound "Sounds/hulkgrowl02.mp3"
gw "PUSSY...NEED...TO...FUCK...PUSSY...."
jump GwenDebraSexSlow

label GwenDebraSexSlow:
play music "Sounds/debrasex.mp3"
scene gwendebrabackground blurred
show gwendebrasexslow
call screen gwendebrasexslow
screen gwendebrasexslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenDebraSexEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenDebraSexFast") 

label GwenDebraSexFast:
scene gwendebrabackground
show gwendebrasexfast
de "Get the fucking antidote [name], I can't take much more of that pounding!"
mc "I'm looking for it Professor..."
call screen gwendebrasexfast
screen gwendebrasexfast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenDebraSexEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("GwenDebraSexSlow")

label GwenDebraSexEnd:
scene science29 with dissolve
de "She's pile-driving her mammoth futa-cock into me!"
mc "Ah, there, I found the antidote Professor!"
de "Inject it quickly, my pussy is turning into a mush!"
stop music
scene science30 with dissolve
play sound "Sounds/hulkgrowl01.mp3"
de "Oh my dear Lord, she's nutting her filthy mutated sperm inside my womb!"
scene science31 with dissolve
mc "Not sure how to do this, so I'll do it in her BUTT..."
de "Hurry!"
scene science32 with fade
show debranude01 at centerleft
de "Finally, she's out! What an ordeal... I'll make her pay for that."
hide debranude01
show debranude02 at centerleft
de "And you... You were rather slow... But I'll forgive you THIS TIME."
mc "You're welcome. Do you need help cleaning up that sperm that's still on you?"
de "NO. I DO NOT. Now get out of my lab, I'll take it from here! And no money for you!"
if mcinjuredgwen == True:
    de "And you'd better get to the medbay, your face looks like a giant potato."
    mc "Yeah, well, it still looks better than the inside of your pussy."
    hide debranude02
    show debranude01 at centerleft
    de "*sigh*..."
    jump Medbay
$ period += 1
scene lab01 with dissolve
jump Main01

label DebraNancyScience:
$ debranancylab = True
scene lab03 with fade
show debratalking01 with moveinright
de "Ah, there you are. With Nancy. I hope her genes are better than yours."
mo "What does she mean, sweetie pie?"
mc "Don't worry Nancy, it's just sciency stuff."
hide debratalking01
show debraback01
with fastdissolve        
de "Now if you'll follow me to the alpha-ray chamber..."
scene nancylab01 with dissolve
de "Just go inside that totally safe area over there..."
mo "Oh dear me, I'm starting to regret this. And my costume is already starting to HURT..."
mc "So let's be quick about it then!"
scene nancylab02 with dissolve
play music "Sounds/radiation02.mp3"
de "Indeed. I'm going straight to level 2 then!"
mo "Oh, I don't like that... My... muscles are contracting!"
scene nancylab03 with dissolve
play sound "Sounds/gasp.mp3"
mc "You meant level 2 in reverse polarity Professor, right?"
de "What? Oh yeah, I should have pressed THAT button beforehand."
scene nancylab05 with dissolve
mo "AAAAH!"
mc "That's not good, she's... growing a futa bulge now on top of everything else! Reverse the polarity or she'll rape us BOTH!"
scene nancylab04 with dissolve
de "Sure, sure, ah, there it is..."
play music "Sounds/radiation01.mp3"
scene nancylab06 with dissolve
mc "Ah, this looks better, she's... reversing back to normal. I hope."
mo "Gggg-gggg..."
de "Now I forgot to warn you reverse polarity should induce severe muscle spasm..."
scene nancylab07 with dissolve
play sound "Sounds/womanscream.ogg"
mo "AAAH!"
mc "Shit, I need to catch her before she falls!"
scene nancylab08 with dissolve
stop music
de "So, did it work?"
mc "It looks like it might have, her muscles are back to normal..."
de "Science WINS again! Take that, anti-quarkkers! Thank you for PROVING me right AGAIN!"
call LustPlusDebra
scene nancylab09 with dissolve
mc "She looks like she might be regaining consciousness too..."
mo "Uhh? Oh, sweetie pie, it's you..."
mc "Yes, how are you feeling, does it hurt?"
mo "No... Not anymore..."
scene nancylab10 with dissolve
play sound "Sounds/kiss.mp3"
call LustPlusNancy
mc " * Bingo! An extra lust point. *"
scene nancylab09 with dissolve
mo "Take me back to my bunk please, I'm... tired."
mc "Sure thing!"
scene nancylab11 with dissolve
mc "And once again, the HERO saves the day!"
de "I think you'll find that MY machine saved the day!"
$ period += 1
jump Bedroom
