label Bedroom:
stop music
stop sound
scene bedroom01 with dissolve
show screen mcstats
show screen calendar
$ loc = "bedroom"

if boughthat == True and period == 1:
    $ mnagahat = True
    $ boughthat = False
    "Ah, I received a parcel by drone. Must be my MNAGA hat..."
    window hide
    show mnagahat at posmission
    $ renpy.pause(4.0, hard=True)
    hide mnagahat
    call PlusTrumpster

if (period == 1 or period == 2) and day == 1 and week >= 4 and bounty and knowbounty == False:
    show messagesign
    mc "Oh, it looks like I have a message. I'll check the interface."
    hide screen calendar
    hide screen mcstats
    scene interface01
    if siriclothes == 1:
        show siri03aa with fastdissolve
    if siriclothes == 2:
        show siri03ba with fastdissolve
    if siriclothes == 3:
        show siri03ca with fastdissolve
    si "I am informing you that I found this message posted by the Trumpf Militia all over Qanon forums..."
    window hide
    show bounty at posmission
    $ renpy.pause(1.0, hard=True)
    pause
    scene interface01
    if siriclothes == 1:
        show siri04aa with fastdissolve
    if siriclothes == 2:
        show siri04ba with fastdissolve
    if siriclothes == 3:
        show siri04ca with fastdissolve
    si "You should be careful. Bounty-hunters will now be looking for you..."
    mc "Thanks for letting me know Siri."
    $ knowbounty = True
    $ metme = True
    jump Bedroom

if dayschurch == 0 and missionchurch and period == 1:
    scene bedroom01 with dissolve
    show messagesignlena
    mc "Oh, oh, it looks like Chief Lena wants to see me urgently..."
    jump LenaChurchEnd

if daysprisoner == 0 and missionprisoner and period ==1:
    scene bedroom01 with dissolve
    show messagesignlena
    mc "Oh, oh, it looks like Chief Lena wants to see me urgently..."
    jump EndPrisonerMission

if (period == 1 or period == 2) and day == 1 and week >= 6 and melaniabounty and knowmelaniabounty == False and bounty == False:
    show messagesign
    mc "Oh, it looks like I have a message. I'll check the interface."
    hide screen calendar
    hide screen mcstats
    scene interface01
    if siriclothes == 1:
        show siri03aa with fastdissolve
    if siriclothes == 2:
        show siri03ba with fastdissolve
    if siriclothes == 3:
        show siri03ca with fastdissolve
    si "You have received an urgent message from First Lady Melania. I think you should see it this time."
    mc "What the hell does she want now?"
    scene melania01 with dissolve
    show whitehouseframe
    me "It's me, First Lady Melania and double-secret Deep State Special Field Agent, codename \"Trophy\". You did something terrible, not good at all."
    play sound "Sounds/melania02.mp3"
    me "You shouldn't fight against the elites, we always get what we want. I wanted that boy. Magnus. He was mine. I paid good money for him."
    scene melania02 with dissolve
    show whitehouseframe
    me "I have my desires that my very busy husband cannot fulfill. How am I supposed to stay entertained? My life is dull and I was looking forward to playing with Magnus, my new sexual toy."
    me "And now you've taken him away from me. This is not good at all. Now I have to put a bounty on your head. I didn't want to, but you forced me to."
    scene melania03 with dissolve
    show whitehouseframe
    me "So stop being such a pain in the backside. Or BE AN ACTUAL PAIN IN MY BACKSIDE BY RAMMING YOUR POLE IN MY ASS! Come and get me. Or I'll come and get you..."                                                                                                                                      
    hide whitehouseframe
    scene interface01
    if siriclothes == 1:
        show siri04aa with fastdissolve
    if siriclothes == 2:
        show siri04ba with fastdissolve
    if siriclothes == 3:
        show siri04ca with fastdissolve
    mc "Well, that sounded threatening."
    si "You are correct. I have noticed that most home secret servers, which I can easily access due to their lax security, have now been contacted by the Supreme White House with the following ominous picture attachment."
    window hide
    show bounty at posmission
    $ renpy.pause(1.0, hard=True)
    pause
    $ knowmelaniabounty = True
    if renpy.seen_image("bountybackground01"):
        mc "What? Not again!"
    if renpy.seen_image("bountybackground01") == False:
        mc "Well thanks for letting me know Siri..."
    jump Bedroom

if period == 1 and day == 1 and week == 3:
    show messagesign
    mc "Oh, it looks like I have a message. I'll check the interface."
    hide screen calendar
    hide screen mcstats
    scene interface01 with dissolve
    if siriclothes == 1:
        show siri01aa with fastdissolve
    if siriclothes == 2:
        show siri01ba with fastdissolve
    if siriclothes == 3:
        show siri01ca with fastdissolve
    si "You have an important message from Chief Lena."
    scene interface01
    if siriclothes == 1:
        show siri03aa with fastdissolve
    if siriclothes == 2:
        show siri03ba with fastdissolve
    if siriclothes == 3:
        show siri03ca with fastdissolve
    si "It basically says: \"Come forthwith to the Command Center to receive top-secret instructions.\""
    mc "Ah, so you advise me to go or to sleep in?"
    scene interface01
    if siriclothes == 1:
        show siri04aa with fastdissolve
    if siriclothes == 2:
        show siri04ba with fastdissolve
    if siriclothes == 3:
        show siri04ca with fastdissolve
    si "I'd say you should go or you'll get your ass kicked..."
    mc "Alright, I'll put my clothes on then."
    si "That is indeed a good idea too..."
    show screen calendar
    show screen mcstats
    jump MissionPrisoner

if period == 1 and day == 1 and week >= 6 and successchurch == False and failchurch == False:
    show messagesign
    mc "Oh, it looks like I have a message. I'll check the interface."
    hide screen calendar
    hide screen mcstats
    scene interface01 with dissolve
    if siriclothes == 1:
        show siri01aa with fastdissolve
    if siriclothes == 2:
        show siri01ba with fastdissolve
    if siriclothes == 3:
        show siri01ca with fastdissolve
    si "You have an important message from Chief Lena."
    scene interface01
    if siriclothes == 1:
        show siri03aa with fastdissolve
    if siriclothes == 2:
        show siri03ba with fastdissolve
    if siriclothes == 3:
        show siri03ca with fastdissolve
    si "It basically says: \"Come forthwith to the Command Center to receive top-secret instructions.\""
    mc "Ah, so you advise me to go or to sleep in?"
    scene interface01
    if siriclothes == 1:
        show siri04aa with fastdissolve
    if siriclothes == 2:
        show siri04ba with fastdissolve
    if siriclothes == 3:
        show siri04ca with fastdissolve
    si "I'd say you should go or you'll get your ass kicked..."
    mc "Alright, I'll put my clothes on then."
    si "That is indeed a good idea too..."
    show screen calendar
    show screen mcstats
    jump MissionChurch

if period == 1 and whitehousecall >= 9 and seenmaragogo02 and seenmelaniasophia and seenkimberly01 == False and week >= 16 and seenweekwhitehousecall == False:
    $ d4whitehouserollb = renpy.random.randint(1,4)
    if d4whitehouserollb == 1:
        $ seenkimberly01 = True
        $ whitehousecall += 1
        show messagesign
        mc "Oh, it looks like I have a message. I'll check the interface."
        hide screen calendar
        hide screen mcstats
        scene interface02 with dissolve
        play sound "Sounds/interfacestart.mp3"
        pause 2.0
        scene interface01 with dissolve
        if siriclothes == 1:
            show siri01aa with dissolve
        if siriclothes == 2:
            show siri01ba with dissolve
        if siriclothes == 3:
            show siri01ca with dissolve
        si "You have a video message from the Supreme White House. Would you like to open it?"
        mc "Sure, why not, I've got nothing better to do than listen to crazy people on Zoom."
        $ seenweekwhitehousecall = True
        scene kimberlywhitehouse
        show whitehouseframe
        with dissolve
        show kimberly05 with moveinleft
        kg "It's me, Kimberly, here at the Supreme White House gym. AND THIS TIME YOU WILL LISTEN TO ME!"
        mc "*sigh* Here we go again, crazy person shouting at the screen."
        window hide
        scene kimberlywhitehouse blurred
        show kimberly06
        show whitehouseframe
        with dissolve
        kg "LOOK AT HOW BUFF I AM THANKS TO OUR GREAT LEADER WHO RIGHTFULLY STARTED A NUCLEAR WAR TO EMPOWER WOMEN SUCH AS MYSELF!"
        mc "I don't think this is how it happened. The game intro suggests it was a clumsy accid..."
        window hide
        hide kimberly06
        show kimberly07
        with dissolve
        kg "SHUT UP! PRESIDENT-FOR-LIFE DONALD TRUMPF HAS DONE MORE FOR WOMEN THAN ABRAHAM LINCOLN!"
        mc "Err... Can she hear me? What the fuck?"
        window hide
        hide kimberly07
        show kimberly08
        with dissolve
        play sound "Sounds/womangroan.mp3"
        kg "I've been told you have big muscles. BUT ARE YOU AS STRONG AS ME? I DOUBT IT! I COULD CRUSH YOU WITH MY LITTLE FINGER!"
        if mcstrength >= 10:
            mc "Ha ha, lol, ROFL! What's that, like only 500kg per curl? I can lift just as much, no problemo lady."
        if mcstrength <= 9:
            mc "Yeah okay, but I still have some training to do and I'll easily catch up to that level of strength. What is she, like strength 9 or something? Pfff..."
        window hide
        hide kimberly08
        show kimberly09
        with dissolve
        play sound "Sounds/ripping.mp3"
        kg "YOU'RE MAKING ME ANGRY! AND THIS IS WHAT HAPPENS WHEN YOU MAKE ME ANGRY!"
        window hide
        play sound "Sounds/ripping.mp3"
        hide kimberly09
        show kimberly10
        with dissolve
        kg "MY MUSCLES GROW EVEN BIGGER AND MY STRENGTH DOUBLES!"
        mc "Fuck me, she's HU-U-UGE!"
        window hide
        hide kimberly10
        show kimberly11
        with dissolve
        kg "THAT'S RIGHT, I'M MASSIVE! AND TOTALLY RIPPED EVERYWHERE! LOOK AT THOSE OVERMUSCLED GLUTES... AND WEEP!"
        window hide
        hide kimberly11
        show kimberly12
        with dissolve
        kg "AND LOOK AT MY CLIT, IT'S AS BIG AS A MAN'S COCK! ADMIT IT, YOU CAN'T BEAT ME WIMP!" 
        window hide
        hide kimberly12
        show kimberly13
        with dissolve
        kg "FUCK YEAH! GETTING SO BUFFED IS MAKING ME HORNY AS HELL! ARE YOU HORNY TOO? \nYOU'D BETTER BE, COS THIS MUSCLE SHE-HULK IS GOING TO CRUSH YOU!"        
        if mctrumpster == 5:
            kg "AND IT'S MAKING ME HORNY THAT YOU ARE A TRUMPSTER, DESPITE YOUR MANY FLAWS!"
            call LustPlusKimberly
        menu:
            "I ain't scared of no clit!... (+1 Deep State, -1 Trumpsters)":
                call MinusTrumpster
                call PlusDeep
            "Okay, I see. Radioactivity does have its downsides I guess. (+1 Sierra Club, -1 Road Warriors)":
                call MinusWarrior
                call PlusSierra
        scene interface01 with dissolve
        if siriclothes == 1:
            show siri01aa with dissolve
        if siriclothes == 2:
            show siri01ba with dissolve
        if siriclothes == 3:
            show siri01ca with dissolve
        si "The message ends like that."
        jump Bedroom                
                
if period == 1 and whitehousecall >= 9 and seenmaragogo02 and seenivankakim01 and seenmelaniasophia == False and week >= 13 and seenweekwhitehousecall == False:
    $ d4whitehouserollb = renpy.random.randint(1,4)
    if d4whitehouserollb == 1:
        $ seenmelaniasophia = True
        $ whitehousecall += 1
        show messagesign
        mc "Oh, it looks like I have a message. I'll check the interface."
        hide screen calendar
        hide screen mcstats
        scene interface02 with dissolve
        play sound "Sounds/interfacestart.mp3"
        pause 2.0
        scene interface01 with dissolve
        if siriclothes == 1:
            show siri01aa with dissolve
        if siriclothes == 2:
            show siri01ba with dissolve
        if siriclothes == 3:
            show siri01ca with dissolve
        si "You have a video message from the Supreme White House. Would you like to open it?"
        mc "Sure, why not, I've got nothing better to do this morning."
        $ seenweekwhitehousecall = True
        scene melaniawhitehouse
        show melania20
        show whitehouseframe
        with dissolve
        me "Hello again [name]... How was your special time with me in Mar-a-Gogo?"
        window hide
        scene melaniawhitehouse blurred
        show melania21
        show whitehouseframe
        with dissolve
        me "I hope your harem girls aren't complaining that your balls are COMPLETELY DRAINED!"
        me "You were quite defiant too, if I remember well... As a member of the Super-Elite, it is my duty to show you what happens to those who defy us... LOWER THE SLAVE!"
        window hide
        hide melania21
        show melania22
        with dissolve
        play sound "v07/clunk.mp3"
        me "Now, where did I put that strapon?"
        window hide
        hide melania22
        show melania23
        with dissolve        
        me "Oh, do you recognize her now? She won't be serving free pizza anymore. But she'll be serving FREE ANUS to my Elite Super-Dong!"
        so "MMmgglll. Mmmuuummpppffff."
        me "Ah, there it is..."
        window hide
        hide melania23
        show melania24
        with dissolve
        play sound "v07/chain.mp3"
        me "She can't even talk, that's how we deal with LOUDMOUTHS! But soon, she'll BE BEST and she'll take my huge cock up her ass!"
        so "NNNuuuu. Pgglleeeefff."
        window hide
        hide melania24
        show melania25
        with dissolve
        me "There you go, milk ME this time, with your ass muscles!"
        so "AAAAff... Nnnnurffff...."
        hide melania25
        show melaniasofiafuck
        play music "Sounds/barbarasex.mp3"
        call screen melaniasofiafuck01
        screen melaniasofiafuck01:
            modal True
            imagebutton:
                focus_mask True
                idle "Icons/nextidle.png"
                hover "Icons/nexthover.png"
                action Jump ("MelaniaSofiaFuckEnd")
        label MelaniaSofiaFuckEnd:
        stop music
        hide melaniasofiafuck
        show melania28
        show whitehouseframe
        with dissolve
        me "And now her ass is like a brand new freeway. That's how the Super-Elite deal with Infrastructure Week!"
        me "So I hope you learnt your lesson [name] and that you won't cross me EVER AGAIN..."        
        menu:
            "Now I'm scared and I will respect the Super-Elite for the rest of my life... (+1 Trumpsters, -1 Road Warriors)":
                call MinusWarrior
                call PlusTrumpster
            "Well, it wasn't me so who cares? (+1 Road Warriors, -1 Deep State)":
                call MinusDeep
                call PlusWarrior
        scene interface01 with dissolve
        if siriclothes == 1:
            show siri01aa with dissolve
        if siriclothes == 2:
            show siri01ba with dissolve
        if siriclothes == 3:
            show siri01ca with dissolve
        si "The message ends like that."
        jump Bedroom                

if period == 1 and whitehousecall >= 9 and week >= 10 and seenivankakim01 == False and seenweekwhitehousecall == False:                
    $ d4whitehouserollb = renpy.random.randint(1,4)
    if d4whitehouserollb == 1:
        $ whitehousecall += 1
        $ seenivankakim01 = True
        $ metkg = True
        show messagesign
        mc "Oh, it looks like I have a message. I'll check the interface."
        hide screen calendar
        hide screen mcstats
        scene interface02 with dissolve
        play sound "Sounds/interfacestart.mp3"
        pause 2.0
        scene interface01 with dissolve
        if siriclothes == 1:
            show siri01aa with dissolve
        if siriclothes == 2:
            show siri01ba with dissolve
        if siriclothes == 3:
            show siri01ca with dissolve
        si "You have a video message from the Supreme White House. Would you like to open it?"
        mc "Sure, why not, I've got nothing better to do this morning."
        $ seenweekwhitehousecall = True
        scene ivankawhitehouse blurred
        show ivanka20 at right
        show whitehouseframe
        with dissolve
        iv "Hello TRAITOR! You clearly need to be brainwashed...err, I mean, to see the light."
        iv "So I've brought along my stepsister who is a motivational speaker. Listen carefully to what she has to say."
        window hide
        show kimberly03 at left with moveinleft
        kg "Thank you, General Ivanka. I am Kimberly Guilfool, daughter-in-law of OUR GREAT LEADER PRESIDENT-FOR-LIFE DONALD TRUMPF!"
        mc "Why is this crazy woman screaming all of a sudden? She's hurting my ears."
        window hide
        hide kimberly03
        show kimberly01 at left
        with fastdissolve
        if mctrumpster == 5:
            kg "I'VE BEEN TOLD YOU ARE A TRUE PATRIOT, BUT STILL NEED MORE SCREAMING AT!"
            call LustPlusKimberly
        kg "PRESIDENT-FOR-LIFE DONALD TRUMPF WILL RULE OVER NEW AMERICA FOR A THOUSAND YEARS!"
        window hide
        hide ivanka20
        show ivanka21 at right
        with fastdissolve
        iv "Well, let's not get carried away here, I mean, he is going to die one d..."
        window hide
        hide kimberly01
        show kimberly02 at left
        with fastdissolve
        kg "NO, PRESIDENT DONALD TRUMPF IS IMMORTAL AND WILL LIVE FOREVER AND ACCOMPLISH EVERYTHING, HE IS CHOSEN BY GOD HIMS..."
        window hide
        hide ivanka21
        show ivanka24 at right                
        iv "Come on! Even Daddy doesn't believe this crap! It's just for the rubes and the deplorables, we're dealing with a REAL threat from this hero over there! Stick to the script godammit!"
        window hide
        hide ivanka24
        hide kimberly02
        show ivanka22
        with dissolve
        kg "HOW DARE YOU? I WILL TELL OUR GREAT LEADER OF YOUR BLASPHEMOUS TREACHER..."
        window hide
        hide ivanka22
        show ivanka23
        with fastdissolve
        iv "That's it, I'm cutting this podcast short, you're way off script Kimberly!"
        kg "I AM NOT OFF-SCRIPT, THE SCRIPT OF OUR WHOLE LIVES IS WRITTEN BY OUR GLORIOUS LEADER PRESIDENT DONALD TRUMPF, AND THE BEST IS YET TO COME!!!!"
        scene interface01 with dissolve
        if siriclothes == 1:
            show siri01aa with dissolve
        if siriclothes == 2:
            show siri01ba with dissolve
        if siriclothes == 3:
            show siri01ca with dissolve
        si "The message ends like that."
        mc "Err... What the hell was that?"
        jump Bedroom                

if period == 1 and whitehousecall <= 8:
    if seenweekwhitehousecall == False:
        $ d3whitehouseroll = renpy.random.randint(1,3)
        if d3whitehouseroll == 1:
            $ seenweekwhitehousecall = True
            show messagesign
            mc "Oh, it looks like I have a message. I'll check the interface."
            hide screen calendar
            hide screen mcstats
            scene interface02 with dissolve
            play sound "Sounds/interfacestart.mp3"
            pause 2.0
            scene interface01 with dissolve
            if siriclothes == 1:
                show siri01aa with dissolve
            if siriclothes == 2:
                show siri01ba with dissolve
            if siriclothes == 3:
                show siri01ca with dissolve
            si "You have a video message from the Supreme White House. Would you like to open it?"
            mc "What? Who the hell could that be?"
            menu:
                "Accept the message":
                    if whitehousecall == 1:
                        $ whitehousecall += 1
                        call MelaniaCall01
                        scene interface01 with dissolve
                        if siriclothes == 1:
                            show siri01aa with dissolve
                        if siriclothes == 2:
                            show siri01ba with dissolve
                        if siriclothes == 3:
                            show siri01ca with dissolve
                        si "The message ends like that. With her legs spread wide open..."
                        jump Bedroom
                        
                    if whitehousecall == 2:
                        $ whitehousecall += 1
                        call IvankaCall01
                        scene interface01 with dissolve
                        if siriclothes == 1:
                            show siri01aa with dissolve
                        if siriclothes == 2:
                            show siri01ba with dissolve
                        if siriclothes == 3:
                            show siri01ca with dissolve
                        si "The message ends like that."
                        jump Bedroom

                    if whitehousecall == 3:
                        $ whitehousecall += 1
                        call IvankaCall02
                        scene interface01 with dissolve
                        if siriclothes == 1:
                            show siri01aa with dissolve
                        if siriclothes == 2:
                            show siri01ba with dissolve
                        if siriclothes == 3:
                            show siri01ca with dissolve
                        si "The message ends like that."
                        jump Bedroom

                    if whitehousecall == 4:
                        $ whitehousecall += 1
                        call MelaniaCall02
                        scene interface01 with dissolve
                        if siriclothes == 1:
                            show siri01aa with dissolve
                        if siriclothes == 2:
                            show siri01ba with dissolve
                        if siriclothes == 3:
                            show siri01ca with dissolve
                        si "The message ends like that."
                        jump Bedroom
                        
                    if whitehousecall == 5:
                        $ whitehousecall += 1
                        call IvankaCall03
                        scene interface01 with dissolve
                        if siriclothes == 1:
                            show siri01aa with dissolve
                        if siriclothes == 2:
                            show siri01ba with dissolve
                        if siriclothes == 3:
                            show siri01ca with dissolve
                        si "The message ends like that."
                        jump Bedroom

                    if whitehousecall == 6:
                        $ whitehousecall += 1
                        call MelaniaCall03
                        scene interface01 with dissolve
                        if siriclothes == 1:
                            show siri01aa with dissolve
                        if siriclothes == 2:
                            show siri01ba with dissolve
                        if siriclothes == 3:
                            show siri01ca with dissolve
                        si "The message ends like that."
                        jump Bedroom

                    if whitehousecall == 7:
                        $ whitehousecall += 1
                        call MelaniaCall04
                        scene interface01 with dissolve
                        if siriclothes == 1:
                            show siri01aa with dissolve
                        if siriclothes == 2:
                            show siri01ba with dissolve
                        if siriclothes == 3:
                            show siri01ca with dissolve
                        si "The message ends like that."
                        jump Bedroom

                    if whitehousecall == 8:
                        $ whitehousecall += 1
                        call MelaniaCall05
                        scene interface01 with dissolve
                        if siriclothes == 1:
                            show siri01aa with dissolve
                        if siriclothes == 2:
                            show siri01ba with dissolve
                        if siriclothes == 3:
                            show siri01ca with dissolve
                        si "The message ends like that."
                        mc "Damn, that escalated quickly. Now they're threatening me..."
                        si "I gathered that from the lewd spectacle I just endured... And which I will now erase from my hard memory."
                        jump Bedroom

                "Refuse the message":
                    si "The message has been erased Sir. Now I have more free space to...err... roam around my hard drive."
                    jump Bedroom

label DayBeginning:
    mc "What should I do today?"

if period == 1 and sukidateon and sukidatedone == False and (angiedateon or amydateon or ayladateon or rubydateon or marniedateon or gwendateon or pennydateon or lenadateon or claradateon or lauriedateon or barbaradateon or belladateon or debradateon):
    mc "Shit, it appears I have several dates at the same time, I'll have to cancel one of them. I'll go with Suki as a first choice cos it was a promise I made. First I'll take a shower."
    if angiedateon:
        $ angiedateon = False
    if amydateon:
        $ amydateon = False
    if ayladateon:
        $ ayladateon = False
    if rubydateon:
        $ rubydateon = False
    if marniedateon:
        $ marniedateon = False
    if pennydateon:
        $ pennydateon = False
    if gwendateon:
        $ gwendateon = False
    if lenadateon:
        $ lenadateon = False
    if claradateon:
        $ claradateon = False
    if lauriedateon:
        $ lauriedateon = False
    if barbaradateon:
        $ barbaradateon = False
    if bellaadateon:
        $ belladateon = False
    if debradateon:
        $ debradateon = False
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to see that nerdy-yet-hot Suki..." 
    stop music
    jump SukiDate

if period == 1 and sukidateon and sukidatedone == False :
    mc "I should get ready for my date with Suki... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to see that nerdy-yet-hot Suki..." 
    stop music
    jump SukiDate

if period == 1 and angiedateon and angiedatedone == False:
    mc "I should get ready for my date with Angie... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to see that naive Angie..." 
    stop music
    jump AngieDate

if period == 1 and marniedateon and marniedatedone == False :
    mc "I should get ready for my date with Marnie... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to see that hot barmaid with a fiery temper..." 
    stop music
    jump MarnieDate

if period == 1 and amydateon and amydatedone == False:
    mc "Ah, I have a date with Amy on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Amy to take her to the Red Canyon then..." 
    stop music
    jump AmyDate

if period == 1 and rubydateon and rubydatedone == False:
    mc "Ah, I have a date with Ruby on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Ruby to take her to the Red Canyon then..." 
    stop music
    jump RubyDate

if period == 1 and ayladateon and ayladatedone == False:
    mc "Ah, I have a date with Ayla on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Ayla to take her to the Red Canyon then..." 
    stop music
    jump AylaDate

if period == 1 and pennydateon and pennydatedone == False:
    mc "Ah, I have a date with Penny on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Penny to take her to the Red Canyon then..." 
    stop music
    jump PennyDate

if period == 1 and gwendateon and gwendatedone == False:
    mc "Ah, I have a date with Gwen on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Gwen to take her to the Red Canyon then..." 
    stop music
    jump GwenDate

if period == 1 and lenadateon and lenadatedone == False:
    mc "Ah, I have a date with Chief Lena on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Lena to take her to the Red Canyon then..." 
    stop music
    jump LenaDate

if period == 1 and claradateon and claradatedone == False:
    mc "Ah, I have a date with Sister Clara on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Clara to take her to the Red Canyon then..." 
    stop music
    jump ClaraDate

if period == 1 and lauriedateon and lauriedatedone == False:
    mc "Ah, I have a date with Laurie on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Laurie to take her to the Red Canyon then..." 
    stop music
    jump LaurieDate

if period == 1 and barbaradateon and barbaradatedone == False:
    mc "Ah, I have a date with Barbara on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Barbara to take her to the Red Canyon then..." 
    jump BarbaraDate

if period == 1 and belladateon and belladatedone == False:
    mc "Ah, I have a date with Bellaa on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Bellaa to take her to the Red Canyon then..." 
    jump BellaDate

if period == 1 and debradateon and debradatedone == False:
    mc "Ah, I have a date with Debra on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Debra to take her to the Red Canyon then..." 
    jump DebraDate

if period == 2 and explored == False and (not (day == 6 or day == 7)):
    call screen mustexploreb
    screen mustexploreb:
        modal True
        imagebutton:
            focus_mask True
            idle "Icons/commandmust.png"
            hover "Icons/commandmust.png"
            action Jump ("CommandExplore")

if period == 1 and day == 4 and weekschool == 0:
    mc "Oh, oh, looks like I've been skipping school this week, I need to go there pronto..."
    call screen mustclassc
    screen mustclassc:
        modal True
        imagebutton:
            focus_mask True
            idle "Icons/schoolmust.png"
            hover "Icons/schoolmust.png"
            action Jump ("School")
if period == 1 and day == 5 and weekschool <= 1:
    mc "Oh, oh, looks like I've been skipping school this week, I need to go there pronto..."
    call screen mustclassd
    screen mustclassd:
        modal True
        imagebutton:
            focus_mask True
            idle "Icons/schoolmust.png"
            hover "Icons/schoolmust.png"
            action Jump ("School")

if period == 2:
    mc "What should I do this afternoon?"
if period == 3:
    mc "What should I do this evening?"
if period == 4:    
    if prisonerescapenight:
        mc "Oh, I should go back to the boiler room now that it's night and help Number 6 escape...."
        jump PrePrisonerEscape
    if mcwatch:
        play sound "v061/got.mp3"
        mc "It's already night time. And now my watch begins."
        stop sound
        jump NightWatch
    mc "It's getting late. Apart from sleeping or fucking, there is little to do..."
    if dayschurch >= 1 and missionchurch:
        mc "I could go and investigate the Church. Or I could invite a harem girl over and have a good time. Decisions, decisions."
        menu:
            "Investigate the Church":
                jump ChurchNight
            "Stay put":
                pass                
    if peetape and seenpeetape == False:
        mc "I could watch the pee-pee tape. Or I could invite a harem girl over and have a good time. Decisions, decisions."
        menu:
            "Watch the pee-pee tape":
                jump PeeTape
            "Another time":
                pass                
    if momcompound and haremmo == False and momdismissed == False and weekmomslept == False:
        $ d4rollmomsleep=renpy.random.randint(1,4)
        stop music
        if d4rollmomsleep == 1:
            show messagesignnancy
            mc "Oh, it looks like I have a message from Nancy, she probably wants to come and sleep in MY bed. I can't really break my promise."
            jump BedroomNancySleep
    if momcompound and haremmo == False and momdismissed and weekmomslept == False:
        $ d4rollmomsleep=renpy.random.randint(1,8)
        stop music
        if d4rollmomsleep == 1:
            show messagesignnancy
            mc "Oh, it looks like I have a message from Nancy, she probably wants to come and sleep in MY bed. I can't really break my promise."
            jump BedroomNancySleep
    if haremde or harembe or haremza or hareman or haremmo or haremmi or haremcy or haremru or haremam or haremay or haremsu or harempe or haremma or haremgw or haremcl or haremla or haremle or haremba:
        mc "I guess I could call a girl for some hanky-panky...."
        label CallGirlMenu:
        menu:
            "Call Zara" if haremza:
                jump ZaraBedroom
            "Call Angie" if hareman  and weekfuckedangie == False:
                jump AngieBedroom
            "Call Angie (already satisfied)" if hareman  and weekfuckedangie:
                jump AngieBedroom
            "Call Nancy" if haremmo and weekfuckedmom == False:
                jump NancyFuck01
            "Call Nancy (already satisfied)" if haremmo and weekfuckedmom:
                jump NancyFuck01
            "Call Michiko" if haremmi and weekfuckedmichiko == False:
                jump MichikoFuck01
            "Call Michiko (already satisfied)" if haremmi and weekfuckedmichiko:
                jump MichikoFuck01
            "Call Cyrl" if haremcy and weekfuckedcyrl == False:
                jump CyrlFuck01
            "Call Cyrl (already satisfied)" if haremcy and weekfuckedcyrl:
                jump CyrlFuck01
            "Call Ruby" if haremru and weekfuckedruby == False:
                jump RubyFuck01
            "Call Ruby (already satisfied)" if haremru and weekfuckedruby:
                jump RubyFuck01
            "Call Amy" if haremam and weekfuckedamy == False:
                jump AmyFuck01
            "Call Amy (already satisfied)" if haremam and weekfuckedamy:
                jump AmyFuck01
            "Call Ayla" if haremay and weekfuckedayla == False:
                jump AylaFuck01
            "Call Ayla (already satisfied)" if haremay and weekfuckedayla:
                jump AylaFuck01
            "Call Suki" if haremsu and weekfuckedsuki == False:
                jump SukiFuck01
            "Call Suki (already satisfied)" if haremsu and weekfuckedsuki:
                jump SukiFuck01
            "Call Gwen" if haremgw and weekfuckedgwen == False:
                jump GwenFuck01
            "Call Gwen (already satisfied)" if haremgw and weekfuckedgwen:
                jump GwenFuck01
            "Call Penny" if harempe and weekfuckedpenny == False:
                jump PennyFuck01
            "Call Penny (already satisfied)" if harempe and weekfuckedpenny:
                jump PennyFuck01
            "Call Marnie" if haremma and weekfuckedmarnie == False:
                jump MarnieFuck01
            "Call Marnie (already satisfied)" if haremma and weekfuckedmarnie:
                jump MarnieFuck01
            "Call Clara" if haremcl and weekfuckedclara == False:
                jump ClaraFuck01
            "Call Clara (already satisfied)" if haremcl and weekfuckedclara:
                jump ClaraFuck01
            "Call Laurie" if haremla and weekfuckedlaurie == False:
                jump LaurieFuck01
            "Call Laurie (already satisfied)" if haremla and weekfuckedlaurie:
                jump LaurieFuck01
            "Call Lena" if haremle and weekfuckedlena == False:
                jump LenaFuck01
            "Call Lena (already satisfied)" if haremle and weekfuckedlena:
                jump LenaFuck01
            "Call Barbara" if haremba and weekfuckedbarbara == False:
                jump BarbaraFuck01
            "Call Barbara (already satisfied)" if haremba and weekfuckedbarbara:
                jump BarbaraFuck01
            "Call Bella" if harembe and weekfuckedbella == False:
                jump BellaFuck01
            "Call Bella (already satisfied)" if harembe and weekfuckedbella:
                jump BellaFuck01
            "Call Debra" if haremde and weekfuckeddebra == False:
                jump DebraFuck01
            "Call Debra (already satisfied)" if haremde and weekfuckeddebra:
                jump DebraFuck01
            "Call both Amy and Gwen" if haremgw and haremam and weekfuckedgwen == False and weekfuckedamy == False and preggwstart <=2 and pregamstart <= 2:
                jump AmyGwenFuck01
            "Call both Amy and Gwen (both already satisfied)" if haremgw and haremam and weekfuckedgwen and weekfuckedamy:
                if pregam and pregamstart >= 3:
                    "Amy is too far into her pregnancy to call her tonight."
                    jump CallGirlMenu
                if preggw and preggwstart >= 3:
                    "Gwen is too far into her pregnancy to call her tonight."
                    jump CallGirlMenu
                jump AmyGwenFuck01
            "Don't call anyone and go to sleep":
                jump MCsleep
    mc "And since I don't have a harem yet, I guess it's sleeping time..."
    jump MCsleep

label Bedroom02:
call screen mcbedroom
screen mcbedroom:
    modal True
    imagebutton:
        focus_mask True
        idle "Bedroom/bedroominterfaceidle.png"
        hover "Bedroom/bedroominterfacehover.png"
        action Jump ("Interface")
    imagebutton:
        focus_mask True
        idle "Bedroom/bedroombedidle.png"
        hover "Bedroom/bedroombedhover.png"
        action Jump ("MCbed")
    imagebutton:
        focus_mask True
        idle "Bedroom/bedroomshoweridle.png"
        hover "Bedroom/bedroomshowerhover.png"
        action Jump ("BedroomShower")
    if genielamp == True:
        imagebutton:
            focus_mask True
            idle "Bedroom/bedroomlampidle.png"
            hover "Bedroom/bedroomlamphover.png"
            action Jump ("MCgenie")
    if seenbar == False:
        imagebutton:
            focus_mask True
            idle "Icons/baridle.png"
            hover "Icons/barhover.png"
            action Jump ("Bar")
    if seenpool == False:
        imagebutton:
            focus_mask True
            idle "Icons/poolidle.png"
            hover "Icons/poolhover.png"
            action Jump ("Pool")
    imagebutton:
        focus_mask True
        idle "Icons/commandidle.png"
        hover "Icons/commandhover.png"
        action Jump ("Command")
    if seengym == False:
        imagebutton:
            focus_mask True
            idle "Icons/gymidle.png"
            hover "Icons/gymhover.png"
            action Jump ("Gym")
    if seenchurch == False:
        imagebutton:
            focus_mask True
            idle "Icons/churchidle.png"
            hover "Icons/churchhover.png"
            action Jump ("Church")
    if seenlab == False:
        imagebutton:
            focus_mask True
            idle "Icons/labidle.png"
            hover "Icons/labhover.png"
            action Jump ("Lab")
    if seenschool == False and period <=2 and not (day == 6 or day == 7):
        imagebutton:
            focus_mask True
            idle "Icons/schoolidle.png"
            hover "Icons/schoolhover.png"
            action Jump ("School")
    if seendojo == False:
        imagebutton:
            focus_mask True
            idle "Icons/dojoidle.png"
            hover "Icons/dojohover.png"
            action Jump ("Dojo")
    if seenworkshop == False and period <= 3:
        imagebutton:
            focus_mask True
            idle "Icons/workshopidle.png"
            hover "Icons/workshophover.png"
            action Jump ("Workshop")
    if seenfood == False and period <= 2:
        imagebutton:
            focus_mask True
            idle "Icons/foodidle.png"
            hover "Icons/foodhover.png"
            action Jump ("FoodUnit")
    if period <= 3:
        imagebutton:
            focus_mask True
            idle "v061/passtime.png"
            hover "v061/passtime.png"
            action [SetVariable("period", period+1), Jump ("Bedroom")]
    if seenworkshop == True:
        add "Icons/workshopnone.png"
    if seenschool == True:
        add "Icons/schoolnone.png"
    if seengym == True:
        add "Icons/gymnone.png"
    if seenfood == True:
        add "Icons/foodnone.png"
    if seenpool == True:
        add "Icons/poolnone.png"
    if seenlab == True:
        add "Icons/labnone.png"
    if seenchurch == True:
        add "Icons/churchnone.png"
    if seenschool == True:
        add "Icons/schoolnone.png"
    if seendojo == True:
        add "Icons/dojonone.png"
    if seenbar == True:
        add "Icons/barnone.png"
    if seenfood == True:
        add "Icons/foodnone.png"
    if period >= 3 or day == 6 or day == 7:
        add "Icons/schoolnone.png"
    if period >= 3:
        add "Icons/foodnone.png"
    
label MCbed:
show screen mcstats
mc "That's my bed. I don't see any girl in it waiting for me. SAD."
if period == 4:
    mc "I guess it's time to go to bed. Even heroes need sleep."
    jump MCsleep
hide screen mcstats
scene bedroom01 with dissolve
jump Bedroom02

label BedroomShower:
hide screen mcstats
mc "I should take a shower. I feel so dirty."
scene mcshowering with dissolve
play music "Sounds/shower.mp3"
mc "Yeah, that's nice..."
stop music
show screen mcstats
scene bedroom01 with dissolve
jump Bedroom02

label Interface:
hide screen calendar
scene interface02 with dissolve
play sound "Sounds/interfacestart.mp3"
pause 2.0
label Interface02:
scene interface01 with dissolve
if siriclothes == 1:
    show siri01aa with dissolve
if siriclothes == 2:
    show siri01ba with dissolve
if siriclothes == 3:
    show siri01ca with dissolve

if firsttimeinterface == True:
    si "Hello [name], my name is Siri. How may I help you?"
    $ firsttimeinterface = False

menu:
    "Change your outfit Siri.":        
        if siriclothes == 1:
            hide siri01aa
            show siri02aa
        if siriclothes == 2:
            hide siri01ba
            show siri02ba
        if siriclothes == 3:
            hide siri01ca
            show siri02ca
        si "What would you like me to wear?"
        menu:
            "Your default outfit." if siriclothes != 1:
                $ siriclothes = 1
                jump Interface02
            "A sexy bikini" if siriclothes != 3:
                $ siriclothes = 3
                jump Interface02
            "Some naughty outfit" if siriclothes != 2:
                $ siriclothes = 2
                jump Interface02
    "Show me the character interface.":        
        if siriclothes == 1:
            hide siri01aa
            show siri06aa at left with dissolve
        if siriclothes == 2:
            hide siri01ba
            show siri06ba at left with dissolve
        if siriclothes == 3:
            hide siri01ca
            show siri06ca at left with dissolve
        show characterinterface01 with moveinright
        show charam
        show charan
        show charay
        show charba
        show charbe
        show charcy
        show charde
        show chargw
        show charla
        show charcl
        show charle
        show charmi
        show charsu
        show charma
        show charpe
        show charra
        show charru
        show charta
        si "Here it is. Click on a character to access further details, Sir."
        jump CharacterInterface
    "Give me some hints Siri, I'm lost.":
        if siriclothes == 1:
            hide siri01aa
            show siri03aa
        if siriclothes == 2:
            hide siri01ba
            show siri03ba
        if siriclothes == 3:
            hide siri01ca
            show siri03ca
        si "What are you having troubles with Sir?"
        menu:
            "How do I get a girl to join my harem?":                
                if siriclothes == 1:
                    hide siri03aa
                    show siri05aa
                if siriclothes == 2:
                    hide siri03ba
                    show siri05ba
                if siriclothes == 3:
                    hide siri03ca
                    show siri05ca               
                si "A girl may join your harem if her lust for you has reached level 4."
                si "To reach such a level of lust, you must seduce her, and most likely perform a mission for her."
                if siriclothes == 1:
                    hide siri05aa
                    show siri03aa
                if siriclothes == 2:
                    hide siri05ba
                    show siri03ba
                if siriclothes == 3:
                    hide siri05ca
                    show siri03ca            
                si "You DO know how to seduce a girl without showing her your monster cock right?"
                mc "I could show her my huge muscles instead perhaps?"
                if siriclothes == 1:
                    hide siri03aa
                    show siri04aa
                if siriclothes == 2:
                    hide siri03ba
                    show siri04ba
                if siriclothes == 3:
                    hide siri03ca
                    show siri04ca              
                si "(Sigh). It might work for some girls at the gym, but it will be only worth one lust point. You will need to use other means to seduce most girls."
                si "You could for example invite them on a date. Either to the Red Canyon just outside of the Compound or for dinner. At YOUR costs."
                mc "I see. When does that option come about?"
                if siriclothes == 1:
                    hide siri04aa
                    show siri02aa
                if siriclothes == 2:
                    hide siri04ba
                    show siri02ba
                if siriclothes == 3:
                    hide siri04ca
                    show siri02ca                
                si "Once you have reached lust level 2 with a girl, the option to invite her will appear and the date location icon will also become available."
                mc "Thank you Siri. Can I show you my MASSIVE cock and then invite you on a date?"
                if siriclothes == 1:
                    hide siri02aa
                    show siri04aa
                if siriclothes == 2:
                    hide siri02ba
                    show siri04ba
                if siriclothes == 3:
                    hide siri02ca
                    show siri04ca                
                si "I am virtual you numbnuts."
                jump Interface02
            "What happens when a girl joins my harem?":
                if siriclothes == 1:
                    hide siri03aa
                    show siri05aa
                if siriclothes == 2:
                    hide siri03ba
                    show siri05ba
                if siriclothes == 3:
                    hide siri03ca
                    show siri05ca            
                si "Your duty as harem master is to fulfill her needs. If you do not, her lust level will go back down beyond level 4 and she will leave your harem."
                mc "What? That is simply outrageous! And what needs does a girl have anyway? Shopping? The last Walmart closed last year, too bad!"
                if siriclothes == 1:
                    hide siri05aa
                    show siri04aa
                if siriclothes == 2:
                    hide siri05ba
                    show siri04ba
                if siriclothes == 3:
                    hide siri05ca
                    show siri04ca                
                si "Your derogatory attitude toward women will not go unnoticed. A girl's needs are many. First, she will want to have sex. GREAT sex."
                si "Depending on how much of a cockslut she is, she might want to have more or less sex with you. Some girls are even frigid and won't require any sexual fulfillment."
                mc "Well, for the GREAT sex, you can count on me Siri! My cum-cannon never tires of stretching tight horny cu..."
                if siriclothes == 1:
                    hide siri04aa
                    show siri02aa
                if siriclothes == 2:
                    hide siri04ba
                    show siri02ba
                if siriclothes == 3:
                    hide siri04ca
                    show siri02ca               
                si "Yes, yes, thank you very much, there is no need to elaborate on your sexual prowess, I'm not interested."
                if siriclothes == 1:
                    hide siri02aa
                    show siri05aa
                if siriclothes == 2:
                    hide siri02ba
                    show siri05ba
                if siriclothes == 3:
                    hide siri02ca
                    show siri05ca                
                si "To spice up your sex life, some girls may have a fetish. Like cosplay, or BDSM. In which case, you will need the appropriate apparel for both of you to dress up in frilly outfits."
                mc "That sounds expensive. I knew there would be some shopping bills involved!"
                if siriclothes == 1:
                    hide siri05aa
                    show siri02aa
                if siriclothes == 2:
                    hide siri05ba
                    show siri02ba
                if siriclothes == 3:
                    hide siri05ca
                    show siri02ca              
                si "You will actually need to pay the Compound 5 dollars per week for each girl in your harem for their food sustainance."
                mc "Oh my God, this is getting more and more demanding! Why on earth would I want a girl to join my harem at such costs?"
                if siriclothes == 1:
                    hide siri02aa
                    show siri01aa
                if siriclothes == 2:
                    hide siri02ba
                    show siri01ba
                if siriclothes == 3:
                    hide siri02ca
                    show siri01ca              
                si "Girls have skills. That boys don't have. You may find some of those skills VERY useful on certain missions."
                mc "Alright, I get it. At least I'll get my rocks off."
                jump Interface02
            "What am I supposed to do every day?":
                if siriclothes == 1:
                    hide siri03aa
                    show siri02aa
                if siriclothes == 2:
                    hide siri03ba
                    show siri02ba
                if siriclothes == 3:
                    hide siri03ca
                    show siri02ca            
                si "You can do MANY things. The day is divided into four periods: morning, afternoon, evening and night. \n In each of these periods, you can visit a different place amongst many available locations."
                show allicons
                if siriclothes == 1:
                    hide siri02aa
                    show siri06aa
                if siriclothes == 2:
                    hide siri02ba
                    show siri06ba
                if siriclothes == 3:
                    hide siri02ca
                    show siri06ca 
                si "They are all here on the right. When there are surrounded by a blue circle, it means you can go there."
                si "Just hover above any of them to choose where you want to go. Try it, click on the gym icon for example..."
                call screen gyminterface
                screen gyminterface:
                    modal True    
                    imagebutton:
                        focus_mask True
                        idle "Icons/gymidle.png"
                        hover "Icons/gymhover.png"
                        action Jump ("GymInterface")
                label GymInterface:
                scene gym04 with dissolve
                if siriclothes == 1:
                    hide siri05aa
                    show siri01aa
                if siriclothes == 2:
                    hide siri05ba
                    show siri01ba
                if siriclothes == 3:
                    hide siri05ca
                    show siri01ca
                si "Look! We are now at the gym!"
                mc "Amazing what you can do with a computer these days..."
                si "Stop being snarky. And let's go back to the interface, I feel safer there..."
                scene interface01 with dissolve
                show allicons
                show gymnone
                if siriclothes == 1:
                    show siri01aa
                if siriclothes == 2:
                    show siri01ba
                if siriclothes == 3:
                    show siri01ca
                si "If you can't go somewhere, the icon for that location becomes grey. We've been to the gym, so you can't go back there today, and now the icon for it has turned into a dull grey..."
                if siriclothes == 1:
                    hide siri01aa
                    show siri06aa
                if siriclothes == 2:
                    hide siri01ba
                    show siri06ba
                if siriclothes == 3:
                    hide siri01ca
                    show siri06ca 
                si "See?"
                mc "Hey, that's not fair, we only went there virtually for a second or so!"
                if siriclothes == 1:
                    hide siri06aa
                    show siri02aa
                if siriclothes == 2:
                    hide siri06ba
                    show siri02ba
                if siriclothes == 3:
                    hide siri06ca
                    show siri02ca 
                si "Don't worry, if you don't do much in a given location and you leave quickly, its icon will not turn grey AND time will NOT advance..."
                mc "That's better..."
                si "On the other hand, if you MUST go somewhere, the icon for that location will turn red and all other icons will be de-activated..."
                if siriclothes == 1:
                    hide siri02aa
                    show siri06aa
                if siriclothes == 2:
                    hide siri02ba
                    show siri06ba
                if siriclothes == 3:
                    hide siri02ca
                    show siri06ca 
                hide allicons
                hide gymnone
                show commandmust
                si "Like so... You now MUST go the command centre to receive instructions from Chief Lena..."
                mc "I hate being told what to do. I'm the MASTER of my own Destiny!"
                if siriclothes == 1:
                    hide siri06aa
                    show siri03aa
                if siriclothes == 2:
                    hide siri06ba
                    show siri03ba
                if siriclothes == 3:
                    hide siri06ca
                    show siri03ca
                hide commandmust
                si "Of course you are (cough). Any other questions?"
                mc "Yeah. Are there any restrictions as to what I can do during different periods of the day?"
                if siriclothes == 1:
                    hide siri02aa
                    show siri03aa
                if siriclothes == 2:
                    hide siri02ba
                    show siri03ba
                if siriclothes == 3:
                    hide siri02ca
                    show siri03ca                
                si "Sure. For example, In either the morning or the afternoon of each weekday, you MUST go out and explore the outback for Chief Lena. You can choose to go with Bella or Penny, they will always be available."
                si "Or you could go alone when you have your own means of transportation. To go and explore an area, go to the command centre and click on the command table. Chief Lena will then give you instructions."
                if siriclothes == 1:
                    hide siri03aa
                    show siri05aa
                if siriclothes == 2:
                    hide siri03ba
                    show siri05ba
                if siriclothes == 3:
                    hide siri03ca
                    show siri05ca                
                si "And you can always bring a girl from your harem on top of that!"
                if siriclothes == 1:
                    hide siri05aa
                    show siri02aa
                if siriclothes == 2:
                    hide siri05ba
                    show siri02ba
                if siriclothes == 3:
                    hide siri05ca
                    show siri02ca              
                si "The rest of the time, you can spend practising your shooting, your hand-to-hand combat skills or pumping iron for example. You need to train twice at the gym in any given week to get stronger for example."
                mc "I heard I also have to go to school. That sucks."
                if siriclothes == 1:
                    hide siri02aa
                    show siri03aa
                if siriclothes == 2:
                    hide siri02ba
                    show siri03ba
                if siriclothes == 3:
                    hide siri02ca
                    show siri03ca                
                si "I can't do anything about that. But you only need to go to school twice a week, that's not a lot. You'll still remain as dumb as you were when you joined the Compound."
                mc "Hey! Stop picking on my intellect! I have HUGE muscles, it drains a lot of blood from up there. \n Especially to my MASSIVE COCK."
                if siriclothes == 1:
                    hide siri03aa
                    show siri04aa
                if siriclothes == 2:
                    hide siri03ba
                    show siri04ba
                if siriclothes == 3:
                    hide siri03ca
                    show siri04ca            
                si "I am well aware of that. Well, you could also strut that big bulge of yours at the swimming pool to relax a bit and meet some girls."
                mc "What about the night period, what am I supposed to do then?"
                if siriclothes == 1:
                    hide siri04aa
                    show siri05aa
                if siriclothes == 2:
                    hide siri04ba
                    show siri05ba
                if siriclothes == 3:
                    hide siri04ca
                    show siri05ca                
                si "If you have girls in your harem, night time is LOVE time. I mean SEX time."
                mc "What if I DON'T have any girls I need to sexually satisfy?"
                if siriclothes == 1:
                    hide siri05aa
                    show siri02aa
                if siriclothes == 2:
                    hide siri05ba
                    show siri02ba
                if siriclothes == 3:
                    hide siri05ca
                    show siri02ca              
                si "You can earn a bit of money by doing night watches. You can do that twice a week, otherwise you'll get too tired."
                si "Just go and see Chief Lena during the day in the command centre and tell her you are available for night duty that day to trigger it."
                mc "Is there any other stuff I can do to earn money? I'm kinda broke right now..."
                if siriclothes == 1:
                    hide siri02aa
                    show siri01aa
                if siriclothes == 2:
                    hide siri02ba
                    show siri01ba
                if siriclothes == 3:
                    hide siri02ca
                    show siri01ca 
                si "Yes. You can work at the science lab or the food unit. Ask Debra or Laurie for it. Or you can fulfill missions for Chief Lena from time to time when she gives you one..."                
                mc "What about the medbay, it doesn't look like I can choose to go there. Why is that?"
                if siriclothes == 1:
                    hide siri01aa
                    show siri03aa
                if siriclothes == 2:
                    hide siri01ba
                    show siri03ba
                if siriclothes == 3:
                    hide siri01ca
                    show siri03ca                
                si "If you get injured during the day or the evening, you WILL end up there until the following morning. In a poor condition may I add."
                if siriclothes == 1:
                    hide siri03aa
                    show siri05aa
                if siriclothes == 2:
                    hide siri03ba
                    show siri05ba
                if siriclothes == 3:
                    hide siri03ca
                    show siri05ca                
                si "But if you're lucky, you might get some LOVING from nurse Rachel to help relieve your pain! (wink)."
                mc "Ah! Now THAT is an incentive to get into all sorts of dangerous situations!"
                if siriclothes == 1:
                    hide siri05aa
                    show siri02aa
                if siriclothes == 2:
                    hide siri05ba
                    show siri02ba
                if siriclothes == 3:
                    hide siri05ca
                    show siri02ca
                si "Remember that time is important though, don't waste it too much on getting a handjob from that bimbo nurse..."
                mc "I'll do what I want! But thanks for the advice..."
                jump Interface02
            "What's the deal with those factions?":
                if siriclothes == 1:
                    hide siri03aa
                    show siri02aa
                if siriclothes == 2:
                    hide siri03ba
                    show siri02ba
                if siriclothes == 3:
                    hide siri03ca
                    show siri02ca            
                si "Factions emerged after the war. It was anarchy. People needed to feel a sense of belonging."
                si "The first faction to form were the Road Warriors. They decided to band together to better survive the harsh outdoor environment."
                si "They are known for being ruthless and often violent. And engaging in questionable human trafficking of sex slaves."
                mc "Sounds like a decent faction to me."
                if siriclothes == 1:
                    hide siri02aa
                    show siri04aa
                if siriclothes == 2:
                    hide siri02ba
                    show siri04ba
                if siriclothes == 3:
                    hide siri02ca
                    show siri04ca                
                si "For your information, since very few men survived, some of those sex slaves are actually MALES. Used as breeding studs for the sole purpose of female sexual enjoyment."
                mc "I wouldn't mind being used that way..."
                si "How come I am not surprised...."
                if siriclothes == 1:
                    hide siri04aa
                    show siri01aa
                if siriclothes == 2:
                    hide siri04ba
                    show siri01ba
                if siriclothes == 3:
                    hide siri04ca
                    show siri01ca  
                si "The second group of people to form a faction were those that needed a... \"divine\" explanation for the War. They formed a new Church called \"The Church of the Redeeming Phallus\"."
                mc "Right. Evangelical nutters re-formed I'm guessing."
                if siriclothes == 1:
                    hide siri01aa
                    show siri02aa
                if siriclothes == 2:
                    hide siri01ba
                    show siri02ba
                if siriclothes == 3:
                    hide siri01ca
                    show siri02ca
                si "Possibly. But not only. Since the third faction are the Trumpsters. Those who rallied behind President Trumpf and blame everyone else for the War."
                mc "Right. Evangelical nutters I'm guessing. Hang on, didn't I say that already?"
                if siriclothes == 1:
                    hide siri02aa
                    show siri04aa
                if siriclothes == 2:
                    hide siri02ba
                    show siri04ba
                if siriclothes == 3:
                    hide siri02ca
                    show siri04ca                
                si "Yes you did. Perhaps dementia is slowly kicking in. What with all that radioactivity...."
                mc "Hey! I'm not senile! I'm a YOUNG, virile, muscled STUD I'll have you know! \n Anyway, I'm not interested in becoming a Trumpster, I have to KILL the MOTHERFUCKER!"
                if siriclothes == 1:
                    hide siri04aa
                    show siri03aa
                if siriclothes == 2:
                    hide siri04ba
                    show siri03ba
                if siriclothes == 3:
                    hide siri04ca
                    show siri03ca  
                si "That is correct. Yet, being a Trumpster, at least temporarily, could prove useful in certain circumstances..."
                mc "Like when?"
                si "I can't tell you. That's for YOU to discover!"
                if siriclothes == 1:
                    hide siri03aa
                    show siri02aa
                if siriclothes == 2:
                    hide siri03ba
                    show siri02ba
                if siriclothes == 3:
                    hide siri03ca
                    show siri02ca
                si "The \"Deep State\" formed in response to the War and the decree issued by President Trumpf that he would remain president for life. Or maybe it was already there before, who knows..."
                mc "Ha! Now THAT sounds like a good faction to belong to, in order to achieve my goals!"
                si "Perhaps, but it is also more dangerous being a Deep State agent... You'll have to choose wisely..."
                if siriclothes == 1:
                    hide siri02aa
                    show siri01aa
                if siriclothes == 2:
                    hide siri02ba
                    show siri01ba
                if siriclothes == 3:
                    hide siri02ca
                    show siri01ca
                si "Finally, you might consider the \"Sierra Club\", neo-environmentalists who want to oversee a rebirth of planet Earth and all its miracles of Nature!"
                mc "That will be for me to decide. In the meantime, I'll stick my petroleum-based chewing gum surreptitiously under that desk... Carry on."
                if siriclothes == 1:
                    hide siri01aa
                    show siri04aa
                if siriclothes == 2:
                    hide siri01ba
                    show siri04ba
                if siriclothes == 3:
                    hide siri01ca
                    show siri04ca                
                si "At least, it's a romantic faction... Unlike you clearly."
                mc "Hey! I can be roshmantic! err... romantic!"
                mc "Instead of picking on me, please tell me how I join a faction..."
                if siriclothes == 1:
                    hide siri04aa
                    show siri02aa
                if siriclothes == 2:
                    hide siri04ba
                    show siri02ba
                if siriclothes == 3:
                    hide siri04ca
                    show siri02ca
                si "You can choose to join a faction once you have reached Level 5 in that faction. Immediately, you will drop 1 level in all other factions, since you can only belong to one faction at a time..."
                mc "I hate losing points. I'm a winner all the time!"
                si "You're sure you didn't mean \"whiner\"?"
                mc "Stop it! I'm a REAL human and you're just a crummy conputer software! So there!"
                si "And I am glad not to live in the emotional nightmare of the real world..."
                mc "Just tell me how I can level up in a given faction?"
                if siriclothes == 1:
                    hide siri02aa
                    show siri01aa
                if siriclothes == 2:
                    hide siri02ba
                    show siri01ba
                if siriclothes == 3:
                    hide siri02ca
                    show siri01ca
                si "Simply do things related to that faction's \"raison d'être\"."
                mc "Err... And in English?"
                if siriclothes == 1:
                    hide siri01aa
                    show siri04aa
                if siriclothes == 2:
                    hide siri01ba
                    show siri04ba
                if siriclothes == 3:
                    hide siri01ca
                    show siri04ca                
                si "That WAS English. Whose language contains 1,700 French cognates. For your information, I mean do stuff that a person from that faction would typically do. Got it?"
                mc "Pfff... What a nerd you are. Siri is a nerd, Siri is a nerd!"
                si "(sigh)"
                jump Interface02                
            "Some events seem to be random...":
                if siriclothes == 1:
                    hide siri03aa
                    show siri02aa
                if siriclothes == 2:
                    hide siri03ba
                    show siri02ba
                if siriclothes == 3:
                    hide siri03ca
                    show siri02ca            
                si "That is correct. In some areas, such as the gym or the pool, girls will appear randomly by a seed determined at the beginning of each day."
                if siriclothes == 1:
                    hide siri02aa
                    show siri04aa
                if siriclothes == 2:
                    hide siri02ba
                    show siri04ba
                if siriclothes == 3:
                    hide siri02ca
                    show siri04ca                
                si "So there's no point in rolling back. It won't work."
                si "That's why a walkthrough might be confusing. You were confused, right?"
                mc "A bit... I admit."
                if siriclothes == 1:
                    hide siri04aa
                    show siri01aa
                if siriclothes == 2:
                    hide siri04ba
                    show siri01ba
                if siriclothes == 3:
                    hide siri04ca
                    show siri01ca  
                si "And there is also randomness in the outcome of certain events, as determined by a die roll. The higher the roll, the better the outcome."
                si "Still, in those instances, it is best to have good stats, so as to increase your chances of success. For example, you need to be STRONG to pass a strength test more easily."
                mc "Ok, thanks, I get it now. I think..."
                jump Interface02                 
    "Leave the interface":
        jump Bedroom

label MCgenie:
if stonepieces >= 1:
    mc "This is my genie's lamp. I haven't collected enough pieces of the Stone Artefact to use it yet."
    scene bedroom01 with dissolve
    jump Bedroom02
if stonepieces == 0 and successge == False:
    mc "I think I have enough pieces of the Stone Artefact to call that rude genie chick."
    jump Geniewin
if successge == True:
    mc "This is my genie's lamp. I used it to get one crummy wish granted and now it's useless."
    scene bedroom01 with dissolve
    jump Bedroom02

label Geniewin:
scene bedroom01
show geniesmoke with dissolve
play sound "Sounds/smokepuff.mp3"
$ renpy.pause(0.5, hard='True')
hide geniesmoke
show genie01 with dissolve
ge "I hope you didn't disturb me for nothing!"
mc "I have collected all those stone pieces you asked for..."
hide genie01
show genie04 with fastdissolve
ge "Good. Hand me the artefact then..."
hide genie04
show genie07 with fastdissolve
ge "Well done! By the powers of Alka-Selzeir, I grant you..."
ge "...ONE wish."
mc "What? That's a rip-off!" 
hide genie07
show genie03 with fastdissolve
ge "Don't push your luck buddy! So, what will it be?"

label GenieChoice:
menu:
    "A pile of gold":
        hide genie03
        show genie07 with fastdissolve        
        ge "How greedy of you... But as you wish..."
        window hide
        show pileofgold at posmission
        $ renpy.pause(2.0, hard=True)
        mc "What? That's it? There's like THREE coins only in that pile!"
        hide genie07
        show genie02 with fastdissolve                
        ge "So? You asked for a pile of gold, three coins amount to a \"pile\". You now have a pile of gold. Worth 30 New dollars to be precise, according to the current exchange rate."
        mc "Oh my God, you're the worse genie ever!"
        hide genie02
        show genie03 with fastdissolve
        $ money += 30
        hide pileofgold
        ge "I will not stand here and take your insults any longer! I will go back into my lamp never to be disturbed again!"
        hide genie03
        show geniesmoke
        play sound "Sounds/smokepuff.mp3"
        $ successge = True
        $ renpy.pause(0.5, hard='True')
        hide geniesmoke
        jump Bedroom02
    "A bigger cock":
        hide genie03
        show genie02 with fastdissolve        
        ge "Well, what a surprise! Like your cock isn't big enough, really? But as you wish..."
        hide genie02 with moveoutright
        show mchard00 at center with moveinleft
        mc "I'm waiting..."
        $ successge = True
        window hide
        hide mchard00
        show mcharder
        $ renpy.pause(1.0, hard=True)
        mc "Hang on, I feel weird... Like weak... And I feel like I'm gonna..."
        hide mcharder
        show mcfainting with dissolve
        ge "You didn't ask for MORE blood supply to go with it dumbass! Too bad, you've wasted your wish and now I'm going back into my lamp..."
        mc "Ooh, I'm fainting..."
        call MCInjury
        $ mcinjuredfaint = True
        jump Medbay
    "Increased skill in close combat" if mccombat <= 4:
        hide genie03
        show genie07 with fastdissolve                
        ge "As you wish..."
        call PlusCombat
        $ successge = True
        hide genie07
        show genie04 with fastdissolve                        
        ge "I granted your wish, I will now rest for another 12 centuries in my lamp..."
        hide genie04
        show geniesmoke
        play sound "Sounds/smokepuff.mp3"
        $ renpy.pause(0.5, hard='True')
        hide geniesmoke
        jump Bedroom02
    "Increased skill in firearms" if mcfirearms <= 4:
        hide genie03
        show genie07 with fastdissolve        
        ge "As you wish..."
        call PlusFirearms
        $ successge = True
        hide genie07
        show genie04 with fastdissolve                        
        ge "I granted your wish, I will now rest for another 12 centuries in my lamp..."
        hide genie04
        show geniesmoke
        play sound "Sounds/smokepuff.mp3"
        $ renpy.pause(0.5, hard='True')
        hide geniesmoke
        jump Bedroom02
    "Increased skill in mechanics" if mcmechanics <= 4:
        hide genie03
        show genie07 with fastdissolve        
        ge "As you wish..."
        call PlusMechanics
        $ successge = True
        hide genie07
        show genie04 with fastdissolve                        
        ge "I granted your wish, I will now rest for another 12 centuries in my lamp..."
        hide genie04
        show geniesmoke
        play sound "Sounds/smokepuff.mp3"
        $ renpy.pause(0.5, hard='True')
        hide geniesmoke
        jump Bedroom02
    "Increased strength":
        hide genie03
        show genie07 with fastdissolve        
        ge "As you wish..."
        call PlusStrength
        $ successge = True
        hide genie07
        show genie04 with fastdissolve                        
        ge "I granted your wish, I will now rest for another 12 centuries in my lamp..."
        hide genie04
        show geniesmoke
        play sound "Sounds/smokepuff.mp3"
        $ renpy.pause(0.5, hard='True')
        hide geniesmoke
        jump Bedroom02


label MelaniaCall01:
    scene melania01 with dissolve
    show whitehouseframe
    me "Hello [name]. Don't be alarmed, this is just a friendly call..."
    me "From me, the First Lady, The Mother of Patriots..."
    scene melania02 with dissolve
    show whitehouseframe
    me "I was told that you... are not happy with my husband? Don't listen to the fake media, the president only wants to make us all Great!"
    play sound "Sounds/melania01.mp3"
    window hide
    pause 2
    me "I have... a new therapy for you. To make you feel better. To make you feel GREAT!"
    scene melania03 with dissolve
    show whitehouseframe
    me "So don't try and be a hero. And see what you could get if you decide to stop your desire for vengeance..."
    me "The First Pussy of the First Lady awaits you... Don't be a hero, be best, and come and grab this GREAT pussy..."
    stop sound
    menu:
        "That's a pretty convincing argument I must admit... (+1 Trumpsters)":
            call PlusTrumpster
        "I don't care about your old pussy, do you? (+1 Deep State)":
            call PlusDeep
    hide whitehouseframe
    return

label MelaniaCall02:
    scene melania04 with dissolve
    show whitehouseframe
    me "So, have you thought about my offer?"
    me "Maybe, I can show you some more to help you make up your mind..."
    scene melania05 with dissolve
    show whitehouseframe
    me "What would you look like to see... My great big new fake boobies? Or my tight First Pussy?"
    scene melania06 with dissolve
    show whitehouseframe
    me "I'll show you both to prove to you that I mean BUSINESS... And if YOU also mean business, you know it's time to stop hating my husband. Time to join him to become GREAT!"
    scene melania07 with dissolve
    show whitehouseframe
    me "I'm waiting for you... In the Supreme White House. Come and find me STUD, and this pussy will be ALL YOURS!"
    menu:
        "That's a pretty convincing argument I must admit... (+1 Trumpsters)":
            call PlusTrumpster
        "Women shouldn't be in power at all, POWER TO MEN! (+1 Church of the Redeeming Phallus)":
            call PlusChurch
    hide whitehouseframe
    return

label MelaniaCall03:
    scene melania08 with dissolve
    show whitehouseframe
    if mctrumpster <= 3:
        me "I think you might need some more enticing to BE BEST."
        me "So I took my top off...  I hope that will bring you to the dar... I mean, the TRUMPF side."
    if mctrumpster == 5:
        me "I think you need a reward for being such a loyal subject to the Trumpf Imperial Nepotic Family."
        me "So I took my top off...  And I will show you MUCH MORE, dear uneducated MNAGAt!"
    scene melania09 with dissolve
    show whitehouseframe
    me "See my big new tits? Custom alpha-radiated to be perfectly round, youthful and soft to the touch..."
    me "A perfect target for your superior seed!"
    scene melania10 with dissolve
    show whitehouseframe
    me "What about my SUPREME WHITE PUSSY? It's GREAT because it can take in GREAT things! And many people say that YOU have a HUGE thing."
    scene melania11 with dissolve
    show whitehouseframe
    me "I'll show you exactly what I mean... Watch how that monster black dildo, which by the way definitely proves that I am NOT racist, can plunge into my FIRST PUSSY!"
    me "So come and replace that nigg.. sorry, black cock with your SUPREME white cock and come and FUCK me in the SUPREME WHITE HOUSE! I'm waiting for you!"
    menu:
        "That's a pretty convincing argument I must admit... (+1 Trumpsters)":
            call PlusTrumpster
        "Is it me or that was totally racist? (+1 Deep State)":
            call PlusDeep
    hide whitehouseframe
    return

label IvankaCall01:
    scene ivanka01 with dissolve
    show whitehouseframe
    iv "Well, hello there [name]. This is Ivanka, the First Daughter and the most successful self-made woman in the land."
    iv "I heard you had a grudge against my daddy. I'm here to warn you. I will defend my family and as you can see..."
    scene ivanka02 with dissolve
    show whitehouseframe
    iv "I have the muscles and the feminine beauty to do so..."
    iv "Jared is, shall I say, a beta-weakling. Not because of any beta radiations, he's just always been one really."
    iv "And I am an ALPHA-FEMALE! So what do you say we pair up so I can finally become President Ivanka Trumpf and you can be my Vice-President?"
    scene ivanka03 with dissolve
    show whitehouseframe
    iv "You would have access to this hot muscled body... In the Oval Office under my desk."
    iv "Think about it. A business opportunity such as this one doesn't come often..."
    menu:
        "That's a pretty convincing argument I must admit... (+1 Trumpsters)":
            call PlusTrumpster
        "Ultra-capitalism is what destroyed the planet! (+1 Club Sierra)":
            call PlusSierra
    hide whitehouseframe
    return

label IvankaCall02:
    scene ivanka04 with dissolve
    show whitehouseframe
    if mctrumpster <= 4:
        iv "So, apparently, you didn't quite get the message. How hard is it to understand you cannot fight the Trumpf syndica... I mean family?"
        iv "Now watch carefully. What you are up against..."
        scene ivanka05 with dissolve
        show whitehouseframe
        iv "See? I can power-lift even more than that, this is a piece of cake for me. I am the MOST POWERFUL WOMAN in the World!" 
        iv "That's why I'm always invited to meet all the other powerful people in the world by Daddy."
        iv "So don't fight him, or you'll be up against ME, the essence of feminine beauty and strength..."
        scene ivanka06 with dissolve 
        show whitehouseframe
        iv "The best in this day and age is to be COMPLICIT. Just like I am. And to make tons of money out of the situation."
        iv "I could promote your products via Twatter and you would promote mine via Fuckbook. Like my new flagrance \"In-Peach-Mint\". So come and join the Trumpf syndica... I meant family!"
        iv "DO IT NOW. Before this special offer terminates. After that, I'll have no other choice but to TERMINATE YOU!"    
    if mctrumpster == 5:
        iv "Well, I'm glad to see you have finally seen the light of complicity."
        iv "Now I'll show what our alliance will be made of. I'll show you how STRONG I am!"
        scene ivanka05 with dissolve  
        show whitehouseframe
        iv "See? I can power-lift even more than that, this is a piece of cake for me. I am the MOST POWERFUL WOMAN in the World!" 
        iv "That's why I'm always invited to meet all the other powerful people in the world by Daddy."
        scene ivanka06 with dissolve 
        show whitehouseframe
        iv "The best in this day and age is to be COMPLICIT. Just like I am. And to make tons of money out of the situation."
        iv "I could promote your products via Twatter and you would promote mine via Fuckbook. Like my new flagrance \"In-Peach-Mint\". Now that you are a member of the Trumpf syndica... I meant family!"
        iv "I'll be waiting for you. And that HUGE COCK of yours... Mmmh..."    
        mc "As soon as I find Trumpf City, I'll give it to you good Ivanka!"
        hide whitehouseframe
        return
    menu:
        "That's a pretty convincing argument I must admit... (+1 Trumpsters)":
            call PlusTrumpster
        "I ain't buying it, just like I ain't buying your shoes made in China! (+1 Road Warriors)":
            call PlusWarrior
    hide whitehouseframe
    return

label IvankaCall03:
    scene ivanka08 with dissolve
    show whitehouseframe
    iv "Hello again [name]... As you can see, I am ready to go one step further with YOU!"
    iv "I'm not wearing a bra, because I have nothing to hide. Just like my daddy, who has the most transparent administration in history!"
    scene ivanka09 with dissolve
    show whitehouseframe
    iv "Oh, and look here, what do I have? A BIG THICK WHITE dildo... Not as HUGE as your cock from what I've heard..."
    iv "But it will serve its purpose, I will use it to demonstrate the POWER of my alpha-female tits!"
    scene ivanka10 with dissolve
    show whitehouseframe
    iv "See how it fits perfectly between my MASSIVE firm knockers?"
    iv "My muscular breasts can squeeze it so hard, it might even BREAK!"
    scene ivanka11 with dissolve
    show whitehouseframe
    iv "But don't worry, I won't DESTROY your cock with my superior breasts..."
    if mctrumpster <= 4:
        iv "... If you're a good boy and you stop your phony WITCH-HUNT against my daddy!"
        iv "Then, I'll lick it all over and make it EXPLODE its thick creamy boy-juice all over my First Daughter face!"
    if mctrumpster == 5:
        iv "Especially since you are already a loyal Trumpster..."
        iv "No, for someone SPECIAL like you, I'll lick it all over and make it EXPLODE its thick creamy boy-juice all over my First Daughter face!"
        mc "As soon as I find Trumpf City, I'll plaster it good Ivanka!"
        hide whitehouseframe
        return
    menu:
        "That's a pretty convincing argument I must admit... (+1 Trumpsters)":
            call PlusTrumpster
        "Sounds like a quid pro quo... I'll impeach and impale you until you speak! (+1 Deep State)":
            call PlusDeep
    hide whitehouseframe
    return
    
label MelaniaCall04:
    scene melaniaivanka01 with dissolve
    show whitehouseframe
    me "Mmh, I'm feeling so HORNY today... But our President-for-Life is too busy making New America GREAT AGAIN."
    me "Fortunately, his daughter isn't so busy, since she's just a senior adviser with no clear duties... Maybe I should call her, what do you think [name]?"
    scene melaniaivanka02 with dissolve
    show whitehouseframe
    iv "Here I am! Ready for some SPECIAL FAMILY TIME!"
    me "I bet you already have your HUGE cock out and ready to fap [name], right? My pussy is sssoo wet too..."
    iv "We're not letting you into our private sex life for no reason [name]..."
    me "We need you to PROMISE us that you'll be a good boy and abandon your vendetta against my hubby."
    iv "And we'll show you what you can get in return..."
    scene melaniaivanka03 with dissolve
    show whitehouseframe
    play sound "Sounds/kiss.mp3"
    iv "I LOVE your tongue on mine Melania... Mmmmh..."
    me "My daughter-in-law is such a NAUGHTY girl! For YOU!"
    scene melaniaivanka04 with dissolve
    show whitehouseframe
    iv "And I love even more GRINDING my pussy against yours!"
    me "Ooh, I'm sure [name] LOVES watching us being BEST!"
    iv "I want you to PUMP MY PUSSY UP! It needs to be GIGANTIC to fit his ENORMOUS BOYCOCK!"
    me "Ooh, that's a good idea Ivanka! And I have just the tool for that..."
    scene melaniaivanka05 with dissolve
    show whitehouseframe
    play sound "Sounds/moaning.mp3"
    me "See that [name]? Her pussy is SWELLING UP, ready to take on your GIANT PUSSY-PLEASER!"
    iv "Oh yes, my clit is so fucking HUGE now, keep PUMPING IT Melania!"    
    scene melaniaivanka06 with dissolve
    show whitehouseframe
    me "I just have to taste this MEGA-PUSSY now..."
    iv "Yeah, rub your tongue all over my swollen pussy lips... And slurp up all my copious sex juices, God, I'm just so fucking HORNY!"
    me "*lick* Mmmh, sssooo tasty, I wish you were here to savour my daughter-in-law's DELICIOUS cunt with me [name]!"
    iv "Now it's my turn to return the favor Melania..."
    scene melaniaivanka07 with dissolve
    show whitehouseframe
    me "Oh my God, I'm squirting, your tongue is so good Ivanka!"
    iv "I hope you're CUMMING a MONSTERLOAD too, [name]!"
    me "I imagine that his BEAST must be EXPLODING!"
    scene melaniaivanka08 with dissolve
    show whitehouseframe
    me "I hope you enjoyed our little display of family bonding..."
    if mctrumpster <= 4:
        iv "You could be part of it too, you know that, right? All you have to do is join the Trumpf syndic... I meant FAMILY!"
    if mctrumpster == 5 and bounty == False:
        iv "And since you're already a Trumpster, we'll make sure to treat you like FAMILY when you come and bang us with your SUPERIOR FUCKSTICK!"
        me "We'll be waiting... Our pussies all swollen and READY to take you on, STUD!"
    menu:
        "Damn, these two crazy bitches are making me want to FUCK THEM BIG TIME! (+1 Trumpsters)":
            call PlusTrumpster
        "You're clearly just a bunch of dykes and homosexuality is a sin! (+1 Church of the Redeeming Phallus)":
            call PlusChurch
    hide whitehouseframe
    return

label MelaniaCall05:
    scene ivankamelania01 with dissolve
    show whitehouseframe
    iv "Oh, hello [name]. You've caught us in an intimate position. My SLAVE is busy licking my pussy."
    scene ivankamelania02 with dissolve
    show whitehouseframe
    iv "That's right, I can DOMINATE any woman I want, even the First Lady, and make them worship my SUPERIOR body!"
    me "Yes, Ivanka, you are ssoo POWERFUL! So much more powerful than [name]..."
    iv "What do you have to say about that? Melania seems to think you're nothing but a WIMP after all! Cos you STILL haven't FUCKED HER!"
    scene ivankamelania03 with dissolve
    show whitehouseframe
    iv "And now it's time to give my mother-in-law what she's craving for. A BIG THICK DILDO!"
    me "Ooh, Ivanka, give me what [name] REFUSES to give me! I want it DEEP in my creamy FIRST CUNT!"
    scene ivankamelania04 with dissolve
    show whitehouseframe
    iv "There you go Melania, take it hard! See how I'm pounding her into oblivion [name]! Would you like to be in MY PLACE?"
    play sound "Sounds/moaning.mp3"
    me "I'm sure he would, but he still hasn't UNDERSTOOD what it means to be a part of the FAMILY... AAAh, I'm cumming AGAIN!"
    scene ivankamelania05 with dissolve
    show whitehouseframe
    iv "So be reasonable and stop being DEPLORABLE! Or you might end up on the WRONG end of THIS stick!"
    if bounty:
        iv "And maybe when a bounty hunter brings you back to me, I will treat you the same way. So be warned!"    
    hide whitehouseframe
    return
    
label PeeTape:
scene peetape01 with dissolve
mc "Alright, this had better be good. I sure hope it's genuine..."
play sound "Sounds/knock.mp3"
scene peetape02 with dissolve
mc "Ah, a knock on the door. And some big-titted blond Russian hookers get in the room. Looks good so far... Let me grab my cock..."
scene peetape03 with dissolve
play channel1 "Sounds/wank.mp3"
play channel2 "Sounds/peetapesound.mp3"
mc "Hookers getting naked... Mhhh, nice titties."
mc "And now we finally see the guy... Ah, it's DEFINITELY Trumpf! I'd recognize his stupid hair anywhere. Let's see what they are going to get up to..."
mc "They're getting HIM naked now..."
scene peetape04 with dissolve
stop channel1
mc "Oh my God, what is this monstrosity? It... It looks like Toad from Mario Kart, yuck! That's it, I've already lost my hardon."
mc "And now they're pissing on him... And... he... What the hell is he doing? Gross, man! This is vile beyond imagination!"
scene peetape05 with dissolve
mc "I don't think I can take much more of this... horror freakshow. Oh no, he's at it again! Turn it off, turn it off!"
stop channel2
mc "I think I'm going to be sick... Well, at least, I know it IS genuine now... I'll try... and sleep. And not have any nightmares... Good thing you guys didn't see what I just saw..."
$ seenpeetape = True

label MCsleep:
scene mcsleep with fade
$ loc = "bedroom"
play sound "Sounds/snoring.mp3"
pause 3
scene bedroom01 with fade
call NewDay
jump Bedroom



