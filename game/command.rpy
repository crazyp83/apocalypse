label Command:
stop music
show screen mcstats
show screen calendar
$ loc = "command"
call screen command
screen command:
    add "Command/command01.jpg"
    modal True    
    imagebutton:
        focus_mask True
        idle "Icons/exitleftidle.png"
        hover "Icons/exitlefthover.png"
        action Jump ("LeaveCommand")
    if not period == 4: 
        imagebutton:
            focus_mask True
            idle "Command/commandlenaidle.png"
            hover "Command/commandlenahover.png"
            action Jump ("CommandLena")
    if not period == 1:
        imagebutton:
            focus_mask True
            idle "Command/commandsukiidle.png"
            hover "Command/commandsukihover.png"
            action Jump ("CommandSuki")
    if knowboiler:
        imagebutton:
            focus_mask True
            idle "Command/gateidle.png"
            hover "Command/gatehover.png"
            action Jump ("BoilerRoom")
    imagebutton:
        focus_mask True
        idle "Command/commandtableidle.png"
        hover "Command/commandtablehover.png"
        action Jump ("CommandTable")
    if stonepiece03 == False and missionge:
        imagebutton:
            focus_mask True
            idle "Icons/stone03idle.png"
            hover "Icons/stone03hover.png"
            action Jump ("StonePiece03")

label StonePiece03:
scene command01
if not period == 4:
    show commandlenaidle
if not period == 1:
    show commandsukiidle
show exitleftidle
"You found one of the missing pieces of the Stone Artefact."
$ stonepieces -= 1
window hide
show achievementgenie at posmission
$ renpy.pause(0.5, hard=True)
show text "{font=Gui/Boogaloo-Regular.ttf}{color=#ff0000}{size=30}[stonepieces]{/font}" at StonePosition
$ renpy.pause(2.0, hard=True)
hide achievementgenie
$ stonepiece03 = True
jump Command

label CommandTable:
scene command01
if not period == 4:
    show commandlenaidle
if not period == 1:
    show commandsukiidle
mc sidemc "This where the map of the known New America is located, all in glorious hexagonal technicolor."
if (period == 3 or period == 4):
    mc "But it's too late to go on a scouting mission today..."
    jump Command
if ((period == 1 or period ==2) and explored == True):
    mc "But I already went on a scouting mission this morning..."
    jump Command
if ((period == 1 or period ==2) and explored == False):
    menu:
        "Go on a scouting mission":
            jump ExploreMap
        "Not now.":
            jump Command
label ExploreMap:
scene mapgeneral
show hexA0idle
show hexA1idle
show hexA2idle
show hexA3idle
if wave01explored:
    show hexB1idle
    show hexB2idle
    show hexB3idle
    show hexB4idle
    show hexB5idle
    show hexB6idle
    show hexB7idle
if wave02explored and week >= 4:
    show hexC1idle
    show hexC2idle
    show hexC3idle
    show hexC4idle
    show hexC5idle
    show hexC6idle
    show hexC7idle
if knowdeserttown and wave01explored:
    if wave02explored:
        hide hexc5idle
    show hexC5bidle
if (knowforwardops and wave02explored) or (successprisoner and wave01explored):   
    if wave02explored:
        hide hexc3idle
    show hexC3bidle
if wave03explored and week >= 6:
    show hexD1idle
    show hexD2idle
    show hexD3idle
    show hexD5idle
    show hexD4idle
    show hexD6idle
if wave04explored and week >= 8:
    show hexE1idle
    show hexE2idle
    show hexE3idle
    show hexE4idle
    show hexE5idle
    show hexE6idle
if wave05explored and week >= 11:
    show hexF1idle
    show hexF2idle
    show hexF3idle
    show hexF4idle
    show hexF5idle
    show hexF6idle
if wave06explored and week >= 15:
    show hexG1idle
    show hexG2idle
    show hexG4idle
    show hexG5idle

if knowcity:
    show hexG3idle

le "Ready to go and explore the world [name]? Choose your hex wisely..."
jump ExploringMap

label CommandSuki:
scene sukicommand01 with dissolve
if clearedhex32 and talkedsukihulkquest == False and haremsu:
    $ talkedsukihulkquest = True
    jump CommandSukiChoice
if clearedhex32 and talkedsukihulkquest == False and haremsu == False:
    su "I heard about what you did with that boy. Disobeying Deep State instructions and bringing him back to his mother..."
    mc "Yeah, well, err..."
    scene sukicommand03 with fastdissolve
    su "I was going to say that I actually LIKED what you did... It takes courage to do the RIGHT thing even if the powers that be tell you to do otherwise..."
    mc "Oh. Right, right. That's me, always doing the right thing. Saving children and err... fragile women all over the land."
    scene sukicommand01 with fastdissolve
    su "And taking them into sexual slavery in your harem?"
    mc "No, no, VOLUNTARY sexual slavery! It's not the same thing."
    su "You're a doofus but you're kind of funny. And cute..."
    call LustPlusSuki
    su "So, what did you want to talk about?"
    $ talkedsukihulkquest = True
    jump CommandSukiChoice

su "Yes?"
label CommandSukiChoice:
scene sukicommand01
menu:
    "What is your job here exactly Suki?":
        su "I run the entire intranet structure of the compound. Security cameras, alert system, New Google Maps update."
        scene sukicommand03 with fastdissolve
        su "Your intranet access too. I'm the one who designed Siri..."
        if missionba:
            mc "Mmh, would you happen to have access to the actual internet?"
            scene sukicommand05 with fastdissolve
            su "I have indeed privileged access to the Dark Web. And only me."
            $ knowsukiweb = True        
        mc "I see... Well congrats on Siri, she's smoking hot."
        jump CommandSukiChoice
    "I need to access the Dark Web for an urgent purchase... Could you help me? (BUY MNAGA HAT, +1 Trumpsters when delivered)" if missionba and knowsukiweb and lustsu >= 2 and mnagahat == False:
        scene sukicommand05 with fastdissolve  
        su "I don't know, this is against procedures..." 
        menu:
            "What if I invited you on a date?" if sukidateon == False:
                scene sukicommand03 with fastdissolve
                su "Really? Then I'll let you into the darker corners of the Web for sure!"
                $ sukidateon = True
                mc "It's on! How about tomorrow morning?"
                su "Of course! Let's do that purchase quickly then... What are you trying to buy exactly?"
                mc "Err... A MNAGAt Hat..."
                scene sukicommand02 with fastdissolve
                su "What? Are you kidding me?"
                mc "It's purely for... err... research purposes. Come on, this is a free country, I buy what I want!"
                scene sukicommand05 with fastdissolve
                su "Alright. Just NEVER wear it in my presence."
                scene sukicommand04 with fastdissolve  
                su "You need to give me 5 bucks. That's how much this crappy hat costs and I'm using the only workable credit card of the compound."
                menu:
                    "Pay her (-5 dollars)" if money >=5:
                        $ money -= 5
                        mc "Here you are, you can order it now. How will it be delivered actually?"
                        su "By New Amazon drone I believe. You'll get it first thing in the morning."
                        $ boughthat = True
                        scene sukicommand01 with fastdissolve 
                        su "I really look forward to our date but you must go now, I was about to hack some government server and I can't be disturbed." 
                        $ period += 1
                        scene command01 with fade
                        jump Main01
                    "Don't pay her":
                        mc "Actually, I changed my mind."
                        scene sukicommand03 with fastdissolve
                        su "Your call. But it's too late for the date, it's still ON!"
                        $ period += 1
                        scene command01 with fade
                        jump Main01
            "What if I paid you five bucks?" if money >= 10:
                scene sukicommand05 with fastdissolve  
                su "Mmmh, I certainly could use the money... Alright, let's do this quid pro quo then. What is it for?"
                $ money -= 5
                mc "Here are your five bucks for starters. And it's...err... for the purchase of A MNAGAt Hat..."
                scene sukicommand02 with fastdissolve
                su "What? Are you kidding me?"
                mc "It's purely for... err... research purposes. Come on, this is a free country, I buy what I want!"
                scene sukicommand05 with fastdissolve
                su "Alright. Just NEVER wear it in my presence."
                scene sukicommand04 with fastdissolve  
                su "You need to give me another 5 bucks. That's how much this crappy hat costs and I'm using the only workable credit card of the compound."
                mc "Gee, this is getting expensive. Here you are, you can order it now. How will it be delivered actually?"
                $ money -= 5
                su "By New Amazon drone I believe. You'll get it first thing in the morning."
                $ boughthat = True
                scene sukicommand01 with fastdissolve 
                su "Right, I did the \"favor you asked of me though\" and now you must go now, I was about to hack some government server and I can't be disturbed."                         
                $ period += 1
                scene command01 with fade
                jump Main01
    "What happened to you after the Apocalypse?" if spokesuki02 == False:
        $ spokesuki02 = True
        scene sukicommand05 with fastdissolve   
        su "I searched for my family. My seven brothers and sisters, my parents, my four grandparents..."
        menu:
            "That's a lot of ILLEGALS right there. (+1 Trumpsters)":
                call PlusTrumpster
                scene sukicommand02 with fastdissolve                   
                su "What the hell is wrong with you? No empathy whatsoever, just like your CULT LEADER! Now get out of here and stop pestering me!"
                $ period += 1
                scene command01 with fade
                jump Main01
            "And? What happened to them? (+1 Deep State)":
                scene sukicommand06 with fastdissolve                              
                su "They were ALL dead! *sob* I cried for such a long time..."
                mc "Wow, that is tough, losing your entire extended family like that. I feel for you..."
                scene sukicommand01 with fastdissolve                               
                su "*sob*.. And then, I had an awakening. I was going to use my skills to get back at those who did that to my family."
                mc "Amazing, just like me. We have so much in common."
                call PlusDeep
                scene sukicommand03 with fastdissolve                                
                su "And we complement each other too, since you have the muscles and... I have the brains."
                mc "Hey, I have a brain too!"
                su "Sure [name]. Just not as developed as other people... You must go now, I was about to hack some government server and I can't be disturbed."
                $ period += 1
                scene command01 with fade
                jump Main01
    "Aren't you tired of being stuck in this basement all day long Suki?" if spokesuki04 == False:
        $ spokesuki04 = True
        scene sukicommand05 with fastdissolve  
        su "My job is super-important for your information. And I am prepared for this small sacrifice to help our cause!"
        mc "Ah yes, the \"Cause\", I almost forgot. What is it again?"
        scene sukicommand02 with fastdissolve  
        su "Removing President-For-Life Trumpf from power! Don't you ever read game synopses?"
        mc "Roger that. But this game is still not political at all, right?"
        scene sukicommand01 with fastdissolve  
        su "Of course not, it's a PORN game. And people who think otherwise are just SNOWFLAKES."
        su "It was nice talking to you but I'm afraid you must go now, I was about to hack some government server and I can't be disturbed."
        mc "Sure thing Suki. For the \"Cause\"."
        scene command01 with fade
        jump Main01
    "I'd like to show you something (hypnotize her, +1 lust)" if pendulum and showedpendulum == False:
        scene sukicommand07
        with dissolve
        call UsePendulum
        su "Wh...why are so close to my face? My, I didn't realize you were... that handsome..."
        call LustPlusSuki
        mc "I wanted to see how cute you looked up close."        
        scene sukicommand03
        with dissolve
        su "I hope you weren't... disappointed."
        mc "I definitely wasn't, Suki..."
        scene sukicommand01
        with dissolve
        su "Thanks... *blush*"
        $ showedpendulum = True
        $ period += 1
        scene command01 with fade
        jump Main01
    "I heard you were going to fight Michiko in Saturday's virtual fight night." if marnietipfight and sukifightquest == False and sukifightquestdone == False:
        su "Yes, I was actually training to get better at that stupid game."
        scene sukicommand02 with fastdissolve
        su "But it's not fair! She's already a trained professional in REAL life, so she knows all the moves and she'll humiliate me for sure..."
        mc "Maybe I could help you win this fight?"
        scene sukicommand03 with fastdissolve
        su "You would do that for me?"
        mc "Of course! I think you DESERVE to win."
        su "Then I need you to retrieve Michiko's fight card from the game drive."
        mc "Alright. How do I do that?"
        scene sukicommand05 with fastdissolve
        su "Unfortunately, Marnie keeps it but she'll never give it to you..."
        scene sukicommand01 with fastdissolve
        su "Your only chance would be on Friday evening when she locks it up in the strip lounge because she doesn't man the bar."
        mc "I see. This quest is going to be tough, but I accept the challenge!"
        window hide
        show sukiquest at posmission
        $ renpy.pause(1.0, hard=True)
        pause
        hide sukiquest
        $ sukifightquest = True
        scene sukicommand03 with fastdissolve
        su "Well, good luck to you, [name]. You'll get a reward of course if you succeed..."
        mc "(I'm guessing an extra lust point since she's the new harem girl in this month's update...)"
        $ period += 1
        scene command01 with fade
        jump Main01
    "You seem stressed. I have the right stuff to help you relax." if spliff and spliffused == False:
        su "And what's that?"
        mc "A big fat joint. Top quality stuff, I already tried it."
        if period == 1 or period == 2:
            scene sukicommand05 with dissolve
            su "In broad daylight and in front of Chief Lena, are you crazy? I can't do that."
            mc "Ah, okay, it was a suggestion, maybe in the evening then?"
            scene sukicommand02 with dissolve
            su "It was a DUMB suggestion. Now leave me to do some actual WORK, I was about to hack some government server..."
            scene command01 with fade
            jump Main01            
        if period == 3 and lustsu >= 3:
            $ spliff = False
            $ spliffused = True
            scene sukicommand04 
            show sukiblankscreen
            with dissolve
            su "Why not, I'm kind of bored tonight... But we have to make sure Lena is gone. I'll pretend I'm working and you just have a quick look."
            scene sukicommand08 with dissolve
            su "So, is she still there?"
            mc "Nope, she left. We're alone."
            scene sukicommand03 with dissolve
            su "Alright then, let's try this. As a member of the Deep State, I need to know about all this illegal stuff. For resarch purposes that is."
            mc "You'll see, you'll be so mellow, you'll forget why you smoked it in the first place..."
            scene sukispliff01 with dissolve
            su "Ah yes... I feel... relaxed."
            mc "Same here, I could just like... fly over the country to Trumpf City or something..."
            su "Like a super-hero?"
            mc "Yeah... like... Superboy! Oh man, I'm already flying."
            su "You sure have even bigger muscles than superm..."
            scene sukispliff02 with dissolve
            su "Shit, Chief Lena is back. How do we get rid of this thing."
            mc "Err... I'll eat it. Give it to me."
            scene sukicommand03 with dissolve
            mc "You really... actually... ate the joint. And saved us. Thanks [name], but it's best if you leave now."
            call LustPlusSuki
            $ period += 1
            mc "Ah yeah, it's getting late anyway. I've been flying for too long..."
            jump Bedroom
        if period == 3 and lustsu <= 2:
            scene sukicommand05 with dissolve
            su "No, this is against regulations. And I have a lot of work to do. Don't ask me that again until I'm more... enclined with YOU."
            mc "Got it. Gotta raise that lust so we can have some goo-oo-ood times."
            scene command01 with fade
            jump Main01
    "I think it's time now for you to join my harem Suki..." if lustsu  >= 4 and haremsu == False and sukiharem == False and girlsinharem <= 5 and sukidatedone:
        scene sukicommand03 with fastdissolve
        su "A harem? Well... I've never been in one. But... I'll try!"
        $ haremsu = True
        $ girlsinharem += 1
        $ sukiharem = True
        window hide
        show haremsuki at plus
        $ renpy.pause(2.0, hard=True)
        hide haremsuki
        mc "I'll call you at nights, so we can be together as ONE in unity with Mother Nature and linked by our bodily fluids. Or something like that."
        scene sukicommand05 with fastdissolve
        su "At nights? But... normally... I'm sleeping. But... Right, I'll come and we'll... do stuff together."
        jump CommandSukiChoice
    "How about we go on a date together so you can get out of this stinking basement? (date with Suki in the morning)" if lustsu  >= 3 and sukidatedone == False:
        scene sukicommand03 with fastdissolve
        su "A date? With me? I'm in!"
        $ sukidateon = True
        mc "We can go in the morning then."
        su "Promise?"
        mc "Of course, I'm a man of my word."
        jump CommandSukiChoice
    "I think it's time for you to re-join my harem Suki..." if lustsu >= 4 and haremsu == False and sukiharem  and sukidismissed == False  and girlsinharem <= 5:
        scene sukicommand05 with fastdissolve
        su "I don't know, you kind of treated me like dirt last time..."
        mc "But that was a long time ago. All is forgotten."
        scene sukicommand03 with fastdissolve
        su "I think the expression is \"all is forgiven\"... But you're right, I forgive you and I accept, hoping this time you won't be such a terrible human being."
        mc "I could make promises but then I might have to break them. So let's just wish for the best."
        $ haremsu = True
        $ girlsinharem += 1
        $ sukiharem = True
        window hide
        show haremsuki at plus
        $ renpy.pause(2.0, hard=True)
        hide haremsuki
        mc "I'll call you at nights, so we can rekindle our flame and our passion for each other as a harem master and harem slave."
        scene sukicommand01 with fastdissolve
        su "As usual, I get called and I have to come."
        mc "I'm the harem master, so it's only fair."
        jump CommandSukiChoice    
    "Leave her.":
        mc "I'd better go. Gotta save the world and all that."
        su "Sure, you do that while I actually achieve something by hacking some government server."
        scene command01 with fade
        jump Main01
                
jump Command

label LeaveCommand:
scene command01
if not period == 4: 
    show commandlenaidle
if not period == 1: 
    show commandsukiidle
if stonepiece03 == False and missionge:
    show stone03idle
jump Main01

label BoilerRoom:
if seenprisoner:
    "You've already visited Number 6 today. Wait until tomorrow for another interrogation session."
    jump Command
if seenprisoner == False:
    jump Prisoner01

label CommandLena:
scene command02
show lena01
show commandtable
le "Yes?"
menu:
    "Tell me again about those factions...":
        hide commandtable
        hide lena01
        show lena05
        show commandtable
        le "There are five factions... Although some people may not belong to any of them or even to another one that is beyond your concern, like Cyrl, most people are affiliated to one of the five factions."  
        le "For example, I belong to the Deep State. Our endgoal is the removal of President Trumpf from power. This clearly overlaps with YOUR aim if I'm not mistaken..."
        le "The second faction is The Sierra Club, whose members devote their lives to the protection of the environment, or at least what's left of it."
        hide commandtable
        hide lena05
        show lena06
        show commandtable
        le "There's the Trumpsters of course, who continue to support the president because they are so fucking dumb. I tolerate them in the Compound because they have useful skills to us."
        le "Then there's the Church of the Redeeming Phallus, a new religion that is growing fast and getting bigger and bigger every day with all the new blood pouring in."
        hide commandtable
        hide lena06
        show lena07
        show commandtable        
        le "And finally the Road Warriors, many of whom live freely in the wild but we also have a few here, like Penny. They recognize each other with their tattoos."
        jump CommandLena
    "I'd like to volunteer for night watch duty Chief!" if not mcwatch:
        if mcfirearms <= 3 or mccombat <= 2:            
            hide commandtable
            hide lena01
            show lena06
            show commandtable
            le "You're not ready yet, [name]. You need to improve your firearms and combat skills first. Only the BEST can join the Nightwatch. We don't want no riff-raff."
            hide commandtable
            hide lena06
            show lena01
            show commandtable
            le "Now if you'll excuse me, I'm busy."
            jump Command
        $ nightwatchduty += 1
        if nightwatchduty <= 2:
            hide commandtable
            hide lena01
            show lena07
            show commandtable 
            le "Good. I was looking for an extra pair of hands for tonight actually. Be on the watchtower at midnight then."
            if askedlenawatch == False:
                mc "Before I commit, how much does it pay?"
                le "5 dollars per watch."
                mc "Alright. I'll do it then."
                $ askedlenawatch = True
            hide commandtable
            hide lena07
            show lena01
            show commandtable 
            $ mcwatch = True
            jump CommandLena
        if nightwatchduty >= 3:
            hide lena01
            show lena03
            show commandtable 
            le "You've already done two nightwatch duties this week. Any more, and you'll fall asleep at the wheel. So no."
            mc "Ah, that explains why I've been drinking ten cups of coffee a day recently."
            hide lena03
            show lena01
            show commandtable            
            jump CommandLena        
    "I'm ready to go and explore the world and find Trumpf City!" if ((period == 1 or period ==2) and explored == False):
        hide commandtable
        hide lena01
        show lena07
        show commandtable        
        le "Good. Choose your hex wisely."
        jump ExploringMap
    "It might sound weird but I would like to invite you on a date, Chief!" if lustle >= 2 and lenadatedone == False and lenaconvincedate >= 3 and knowredcanyon:
        hide commandtable
        hide lena01
        show lena11
        show commandtable        
        le "Well... Uh, I'm married... And... It's too dangerous, he might see us. The compound isn't that big."
        mc "I'll take you outdoors, not far away, to the Red Canyon, he won't be able to follow us..."
        hide commandtable
        hide lena11
        show lena06
        show commandtable        
        le "The Red Canyon? I never heard of that place."
        mc "Oh, it's beautiful, I promise. You'll love it. There's clear water and even trees."
        hide commandtable
        hide lena06
        show lenapensive  
        show commandtable
        $ lenadateon = True  
        le "Well, alright, that sounds quite nice indeed... But don't tell anyone, this is between you and me."
        mc "No worries, Chief. I'll pick you up in the morning. Bring your bikini!"
        jump Command
    "I think it's time for you to join my harem, Lena. And start getting fucked by a PROPER MAN." if lustle >= 4 and haremle == False and lenaharem == False and girlsinharem <= 5 and lenadatedone:
        hide commandtable
        hide lena01
        show lena11
        show commandtable 
        le "Well, that would be awkward, I'm... married, remember?"
        mc "Jake doesn't need to know. Just lie and tell him you have night duty. The nights I call you to satisfy your deepest sexual desires..."
        hide commandtable
        hide lena11
        show lenapensive
        show commandtable 
        le "You sure have a seductive way of convincing women to become your sexual slaves. I agree then!"
        $ haremle = True
        $ girlsinharem += 1
        $ lenaharem = True
        window hide
        show haremlena at plus
        $ renpy.pause(2.0, hard=True)
        hide haremlena
        mc "I'll call you at nights and show you how a REAL MAN fucks..."
        le "I... am looking forward to it. Just don't tell anyone. Yet."            
        jump CommandLena
    "Maybe it's time for you to re-join my harem... And for me to be your Daddy again." if lustle >= 4 and haremle == False and lenaharem and lenadismissed == False and girlsinharem <= 5 and alreadylenaharem == False:
        hide commandtable
        hide lena01
        show lena05
        show commandtable 
        le "I don't know. You didn't treat me like a normal Daddy should treat his girl last time, why would it be different THIS TIME?"
        mc "You've got to forgive Daddy. My little girl...err.. I mean Chief Lena, err..."
        le "*sigh*"
        hide commandtable
        hide lena05
        show lena03
        show commandtable            
        le "I'll give you one LAST CHANCE. You'd better not screw it up this time. Daddy."
        $ haremle = True
        $ girlsinharem += 1
        window hide
        show haremlena at plus
        $ renpy.pause(2.0, hard=True)
        hide haremlena
        $ alreadylenaharem = True        
        mc "Will do, I swear, Chief!"
        jump CommandLena
    "I found something for Jake to wear." if lilbra and successjakemission and jakecuck == False and haremle:
        hide commandtable
        hide lena01
        show lena06
        show commandtable 
        le "What is it?"
        mc "It's called a ball-bra. Lets his little cock hand out free while his marbles are held snugly inside a little pouch."
        hide commandtable
        hide lena06
        show lena07
        show commandtable 
        le "That should do the trick. give it to me and I'll talk to him. And convince him to be a good little cuckold for me!"
        mc "And then we can have some FU-UUU-UN times all three of us! Well, all two of us plus him getting humiliated obviously."
        hide commandtable
        hide lena07
        show lena03
        show commandtable 
        le "That's right... It will be the icing on the cake, so to speak...."
        $ lilbra = False
        $ jakecuck = True
        jump CommandLena
    "Err... nothing.":
        le "Well, that was fascinating."
        jump Command
        
label MissionPrisoner:
show screen calendar
show screen mcstats
$ loc = "command"
scene command01
if stonepiece01 == False and missionge:
    show stone03idle
show lena01
with dissolve
le "Ah, there you are. I have a mission of the utmost importance for you [name]!"
mc "I'm all ears."
hide lena01
show lena03
with fastdissolve
le "Recently, we have YET AGAIN apprehended a Trumpster agent in our midst. It's the sixth time this happened and it better be the last!"
mc "Wow, I didn't realize we were THAT infiltrated."
le "The prisoner won't talk. Jake tried everything but failed miserably!"
hide lena03
show lena01
with fastdissolve
le "You are our last chance to make her spill the beans. I want to know if there are more spies in the compound AND I want to know where the government's forward base is located, understood?"
$ missionprisoner = True
$ daysprisoner = 3
window hide
show missionprisoner at posmission
show text "{font=Gui/Boogaloo-Regular.ttf}{color=#ff0000}{size=35}[daysprisoner]{/font}" at PrisonerPosition
pause
hide text
hide missionprisoner
mc "Roger that, Chief Lena."
hide lena01
show lena07
with fastdissolve
le "Use all means necessary. You have three days. After that, I will have no choice but to make her..."
le "... \"commit suicide\" like the other five before her."
mc "That's kind of brutal."
hide lena07
show lena06
with fastdissolve
le "This is the way of the Deep State to get rid of troublemakers! If you ever want to join us, you'd better get with the motion!"
le "And eventually help us run one of our numerous 3PGs around the country..."
mc "What's a \"3PG\"???"
hide lena06
show lena03
with fastdissolve
le "A Pizza Parlour Pedophile Gang. What, you never heard of them?"
mc "I thought that was fake news."
le "Ah! I see our allies in the lame stream media successfully managed to PASS IT for fake news then."
hide lena03
show lena01
with fastdissolve
le "Now go and interrogate Number 6, it's through this gate behind me. And report back to me in three days. Dismissed!"
$ knowboiler = True
jump Prisoner01

label Prisoner01:
$ loc = "prison"
if prisonerescaped:
    scene prison01b
if prisonerescaped == False:
    scene prison01
stop music
play music "Sounds/waterdrip.mp3"
call screen steam01
screen steam01:
    modal True
    if prisonerescaped == False:
        imagebutton:
            focus_mask True
            idle "Command/prisoneridle.png"
            hover "Command/prisonerhover.png"
            action Jump ("Prisoner02")
    if stonepiece01 == False and missionge:
        imagebutton:
            focus_mask True
            idle "Icons/stone01idle.png"
            hover "Icons/stone01hover.png"
            action Jump ("StonePiece01")
    if prisonerescaped:
        imagebutton:
            focus_mask True
            idle "Icons/exitleftidle.png"
            hover "Icons/exitlefthover.png"
            action Jump ("LeavePrison")

label StonePiece01:
scene prison01
"You found one of the missing pieces of the Stone Artefact."
$ stonepieces -= 1
window hide
show achievementgenie at posmission
$ renpy.pause(0.5, hard=True)
show text "{font=Gui/Boogaloo-Regular.ttf}{color=#ff0000}{size=30}[stonepieces]{/font}" at StonePosition
$ renpy.pause(2.0, hard=True)
hide achievementgenie
$ stonepiece01 = True
jump Prisoner01

label Prisoner02:
scene prison02 with dissolve
show prisoner01
if successprisoner or failprisoner:
    jump PrisonerFuck04
if prisonerday01  and prisonerday02 == False:
    jump PrisonerSecondDay
if prisonerday02:
    jump PrisonerThirdDay

mc "So, I hear you won't talk, Number 6? I'll make you talk."
hide prisoner01
show prisoner02
with fastdissolve
pr "PLEA-EASE. You're just a little boy with abnormally large muscles, you don't scare me."
hide prisoner02
label PrisonerChoice:
show prisoner01
menu:
    "Watch what you're saying, I'll beat you to a pulp lady! I swear!":
        hide prisoner01
        show prisoner04
        with fastdissolve
        pr "God, you're pathetic at this. You've never done it before, have you?"
        mc "Err... Yeah, for sure! Plenty of times. Now TALK.. err... BITCH!"
        hide prisoner04
        show prisoner02
        with fastdissolve
        pr "Oh, insults, hey? That will really get me to spill the beans. Pfff! *eyeroll*"
        mc "(Looks like I won't get anywhere with this lame method...)"
        $ prisonertalk = True
        hide prisoner02
        jump PrisonerChoice
    "Perhaps my BIG FAT truncheon will change your mind about that!":
        hide prisoner01
        show prisoner02
        with fastdissolve
        pr "Oh, I get it, you have a big dildo attached to your groin. Ooh, I'm sssoo scared!"
        mc "No, it's my REAL abnormally large PUSSY WRECKER lady! You're gonna feel its wrath!"
        hide prisoner02
        show prisoner04
        with fastdissolve
        pr "Go on, rape me with your dildo, you fucking pervert. Shall I take off my panties for you and give you instructions?"
        mc "Err... No, that won't be necessary, I know what I'm doing. But yeah, take your panties off, BITCH!"
        hide prisoner04
        show prisoner03
        with fastdissolve
        pr "Oooh, I'm ssoo scared, the little boy is going to rape me with his pee-pee! Help! *snickers*"
        stop music
        jump PrisonerFuck01
    "I'm a Trumpster myself, I'll help you escape Number 6. (TRICK HER)":
        hide prisoner01
        show prisoner04
        with fastdissolve
        pr "Is that a trick? I ain't falling for it."
        mc "No, I SWEAR. On my mother's grave and all that."
        hide prisoner04
        show prisoner02
        with fastdissolve
        pr "How are you going to get me out then?"
        mc "Err... I've got a plan. But I need to know where the forward base is so I can get you there safely."
        hide prisoner02
        show prisoner04
        with fastdissolve
        pr "Oh, so it WAS a trick. How dumb do you think I am. Like, really..."
        mc "Err.... A lot? I mean, you do support Trumpf after all."
        hide prisoner04
        show prisoner02
        with fastdissolve
        pr "Oh, insults, hey? That will really get me to spill the beans. Pfff! *eyeroll*"
        mc "(Looks like I won't get anywhere with this lame method...)"
        $ prisonertalk = True
        hide prisoner02
        jump PrisonerChoice
    "I'm a Trumpster myself, I'll help you escape Number 6. (LET HER ESCAPE)" if mctrumpster == 5:
        hide prisoner01
        show prisoner04
        with fastdissolve
        pr "Is that a trick? I ain't falling for it."
        mc "No, I SWEAR. On my mother's grave and all that."
        hide prisoner04
        show prisoner02
        with fastdissolve
        pr "How are you going to get me out then?"
        if period == 4:
            mc "I've got the keys. We can literally just walk out of here, there are no guards."
            pr "Let's do it then!"
            jump PrisonerEscape
        mc "Ah yes, I should have planned this better I guess. I'll come back at night, since it's the only time we can escape without Chief Lena seeing us."
        $ prisonerescapenight = True
        jump Main01        
    "I'm almost a Trumpster myself, I'll help you escape Number 6. (LET HER ESCAPE, +1 Trumpsters, faction change)" if mctrumpster == 4:
        pr "Is that a trick? I ain't falling for it."
        mc "No, I SWEAR. On my mother's grave and all that."
        pr "How are you going to get me out then?"
        if period == 4:
            mc "I've got the keys. We can literally just walk out of here, there are no guards."
            pr "Let's do it then!"
            jump PrisonerEscape
        mc "Ah yes, I should have planned this better I guess. I'll come back at night, since it's the only time we can escape without Chief Lena seeing us."
        $ prisonerescapenight = True
        jump Main01
    "I clearly won't make you talk unless I rape you and I refuse to do so. (LEAVE)" if prisonertalk:
        hide prisoner01
        show prisoner04
        with fastdissolve
        pr "Snowflake! I knew it! You have a tiny cock, just like Jake who couldn't even put it in!"
        menu:
            "What? I'll prove you wrong by RAPING YOU AFTER ALL!":
                hide prisoner04
                show prisoner03
                with fastdissolve
                pr "Oooh, I'm ssoo scared, the little boy is going to rape me with his pee-pee! Help! *snickers*"
                jump PrisonerFuck01
            "You can insult me all you like, I ain't touching you.":
                hide prisoner04
                show prisoner02
                with fastdissolve
                pr "Then I WIN! So much winning! Bye LOSER!"
                jump LeavePrison
        
label PrisonerFuck01:
hide screen mcstats
hide screen calendar
stop music
scene prisonfuck01 blurred with dissolve
show prisonerfuck01
pr "So, are you in yet? I can't feel a thing. It must be real SMALL, boy! Ho ho..."
hide prisonerfuck01
show prisonerfuck02
with fastdissolve
pr "....AAAAAAAH! What the fuck is that?"
mc "Sorry, you were saying?"
pr "Get that fucking thing out of me, I beg you!"
mc "Oh, am I hurting you? But my dong is only halway-..."
hide prisonerfuck02
show prisonerfuck03
with fastdissolve
mc "...in!"
play sound "Sounds/womanscream.ogg"
pr "AAAH, It's so fucking DEEP! Please, have MERCY!"
mc "No way, you deserve what you're getting! Until you talk!"
label Prison01Slower:
play music "Sounds/barbarasex.mp3"
show prisonfuckmovie01slow
call screen prison01slow
screen prison01slow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PrisonerFuck01End")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("Prison01Faster") 

label Prison01Faster:
hide prisonfuckmovie01slow
show prisonfuckmovie01fast
call screen prison01fast
screen prison01fast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PrisonerFuck01End")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("Prison01Slower") 

label PrisonerFuck01End:
pr "Come in me, I want your seed!"
mc "Will you talk if I give you my seed?"
pr "YES, I promise! Just come in ME, PLEASE!"
if persistent.tipson:
    show prisoner01tip at tips with dissolve
    pause
    hide prisoner01tip
menu:
    "Come inside her":
        mc "You'd better keep your promise and talk after that CUM WHORE!"
        jump PrisonFuckCumInside
    "Pull out and douse her back":
        mc "You don't deserve my seed!"
        jump PrisonFuckCumOutside
        
label PrisonFuckCumInside:
stop music
scene prisonfuck01 blurred
show prisonercum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Damn, ssoo good! That tight pussy is milking ounces of cream out of my cum factories!"
show prisonercum03 with fastflash
pr "YES, GIVE ME YOUR SEED, YES!!! I LOVE IT!"
mc "So, you're gonna talk now?"
stop sound
hide prisonercum03
show prisonerfuck01
show prisonercuminsidelayout
with fastdissolve
pr "Ha Ha, now I have your seed in me, just like I wanted, why should I talk? I owned you, LIBTARD!"
mc "What? You fucking lying BITCH!"
pr "And now..."
scene prisonfight01 with dissolve
pr "My FAVORITE leg scissoring move!"
mc "Ah, stop it, you're choking me!"
window hide
call MCInjury
$ mcinjuredprisoner = True
$ mcinjured = True
scene prisonfuck02 with dissolve
mc "That's it, I'm done joking around with you! Get ready for the ANAL POUNDING of your life!"
pr "What? Your dong is too big for that!"
mc "I'll be the judge of that..."
jump PrisonFuck02

label PrisonFuckCumOutside:
stop music
scene prisonercum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Fuck, I'm blowing my load! AAH!"
scene prisonercum01 with fastflash
pr "No, you're spilling it, please! What a waste!"
scene prisonercum02 with dissolve
mc "There you go, I've plastered your back with my cum. I OWE you now BITCH!"
pr "Why are so you so cruel to me? *sob*"
$ prisonerwillpower -= 1
window hide
show achievementprisoner at posmission
$ renpy.pause(1.0, hard=True)
pause
hide achievementprisoner
mc "I might be less cruel if you were to talk..."
pr "Too late, you've spilt your seed, you're no use to me now..."
mc "You think I'm done?"
scene prisonfuck02 with dissolve
show prisonfuck02cumlayout
mc "This time, I'll fuck you up THE ASS!"
pr "What? Your dong is too big for that!"
mc "I'll be the judge of that..."
jump PrisonFuck02

label PrisonFuck02:
$ prisonerday01 = True
scene prisonarse01 with dissolve
mc "It seems perfectly capable of fitting, what do you think?"
pr "Oh my God, oh my God, please, I beg you!"
scene prisonarse02 with dissolve
play sound "Sounds/womanscream.ogg"
mc "As I said, no problem sticking it all the way up your backdoor!"
pr "AAAH, take it out, it's impaling my guts!"
mc "I don't think so... I like it there."
scene prisonanalbackground with dissolve
label PrisonAnal01Slower:
play music "Sounds/womansex01.mp3"
hide prisonanalfast
show prisonanalslow
call screen prisonanal01slow
screen prisonanal01slow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("Prisoner02AnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PrisonAnal01Faster") 

label PrisonAnal01Faster:
hide prisonanalslow
show prisonanalfast
call screen prisonanal01fast
screen prisonanal01fast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("Prisoner02AnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PrisonAnal01Slower") 

label Prisoner02AnalEnd:
stop music
scene prisonanalcumbackground
show prisonanalcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Fuck Yeah! Cumming so much! Giving you a sperm edema!"
pr "This is so humiliating, you are so cruel!"
$ prisonerwillpower -= 1
window hide
show achievementprisoner at posmission
$ renpy.pause(1.0, hard=True)
pause
hide achievementprisoner
mc "See you again for more CRUELTY until you SPEAK number 6!"
$ period += 1
$ seenprisoner = True
show screen mcstats
show screen calendar
play music "Sounds/waterdrip.mp3"
scene prison01b with dissolve
show prisonerlying
if stonepiece01 == False and missionge:
    show stone01idle
if mcinjured:
    mc "I'd better go to the medical bay, my neck really hurts..."
    jump Medbay
jump Main01

label PrisonerSecondDay:
$ prisonerday02 = True
mc "Remind me Number 6, where we did we leave off the other day?"
hide prisoner01
show prisoner04
pr "Give it up, I WON'T TALK! You can rape me all you want, it won't change a thing!"
mc "We'll see about that. Get undressed, you know the drill..."
hide screen mcstats
hide screen calendar
stop music
scene prisonfuck01 blurred with dissolve
show prisonerfuck02
pr "You're too rough, you'll destroy my pussy!"
mc "That's the idea..."
hide screen mcstats
label Prison02Slower:
play music "Sounds/womansex01.mp3"
hide prisonfuckmovie01fast
show prisonfuckmovie01slow
call screen prison02slow
screen prison02slow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PrisonerFuck02End")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("Prison02Faster") 

label Prison02Faster:
hide prisonfuckmovie01slow
show prisonfuckmovie01fast
call screen prison02fast
screen prison02fast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PrisonerFuck02End")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("Prison02Slower") 

label PrisonerFuck02End:
pr "Come in me, I want your seed!"
mc "I don't know, why should I be nice to you?"
pr "I'll tell you ANYTHING you want! PLEASE GIVE ME YOUR SEED!"
if persistent.tipson:
    show prisoner02tip at tips with dissolve
    pause
    hide prisoner02tip
menu:
    "Come inside her":
        mc "You'd better keep your promise and talk after that CUM WHORE!"
        jump PrisonFuck02CumInside
    "Pull out and douse her back":
        mc "You don't deserve my seed!"
        jump PrisonFuck02CumOutside
        
label PrisonFuck02CumInside:
stop music
scene prisonfuck01 blurred
show prisonercum03
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Damn, ssoo good! That tight pussy is milking ounces of cream out of my cum factories!"
show prisonercum03 with fastflash
pr "YES, GIVE ME YOUR SEED, YES!!! I LOVE IT!"
mc "So, you're gonna talk now?"
hide prisonercum03
show prisonerfuck01
show prisonercuminsidelayout
with fastdissolve
$ prisonerwillpower -= 1
window hide
show achievementprisoner at posmission
$ renpy.pause(1.0, hard=True)
pause
hide achievementprisoner
pr "*puff* Let me enjoy that warm cum sloshing inside me first..."
mc "We don't have time for that, get ready to receive an ANAL POUNDING AGAIN!"
scene prisonfuck02 with dissolve
pr "What? Not again, I'm still in pain from the last time!"
mc "No pain, no game..."
jump PrisonFuck02b

label PrisonFuck02CumOutside:
stop music
scene prisonercum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Fuck, I'm blowing my load! AAH!"
pr "What the fuck! I told you to come inside me asshole!"
scene prisonercum02 with dissolve
mc "Oops, I guess I forgot, what you're gonna do about it BITCH?"
pr "I'll tell you what I'll do..."
scene prisonfight01b with dissolve
pr "My FAVORITE leg scissoring move!"
mc "Ah, stop it, you're choking me!"
window hide
call MCInjury
$ mcinjuredprisoner = True
$ mcinjured = True
scene prisonfuck02 with dissolve
mc "That's it, I'm done joking around with you! Get ready for ANOTHER ANAL POUNDING!"
pr "What? Not again, I'm still in pain from last time!"
mc "No pain, no game..."
jump PrisonFuck02b

label PrisonFuck02b:
$ prisonerday01 = True
scene prisonarse01 with dissolve
mc "Ready to take my giant teenage fuckstick up your poopchute again number 6?"
pr "No, I'll never be ready for such a monstrous thing!"
scene prisonarse02 with dissolve
play sound "Sounds/womanscream.ogg"
mc "There you go, that's where Cheney should have looked for weapons of ass destruction!"
pr "You're going to KILL me with it if you pound me TOO HARD!"
mc "You took it like a pro last time, you can take it again!"
pr "NOOOOO!"
if persistent.tipson:
    show prisoner03tip at tips with dissolve
    pause
    hide prisoner03tip
scene prisonanalbackground with dissolve
label PrisonAnal02Slower:
play music "Sounds/womansex01.mp3"
hide prisonanalfast
show prisonanalslow
call screen prisonanal02slow
screen prisonanal02slow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PrisonerAnal02End")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PrisonAnal02Faster") 

label PrisonAnal02Faster:
hide prisonanalslow
show prisonanalfast
pr "No, it's too fast, I... I'm gonna faint..."
call screen prisonanal02fast
screen prisonanal02fast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PrisonerAnal02bEnd")

label PrisonerAnal02End:
stop music
scene prisonanalcumbackground
show prisonanalcum01
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Fuck Yeah! Another creamy ass-load coming your way number 6!"
show prisonanalcum01 with fastflash
pr "This is so humiliating! I feel like a cheap cumdump... *sob*"
stop sound
scene prisonerend01 with dissolve
play music "Sounds/waterdrip.mp3"
mc "So, you're gonna talk now?"
pr "No... *sob* I'm.... strong... I will always cover...for... *sob*.... our God-sent President-for-Life!"
mc "Really? Is it worth all that pain?"
pr "FUCK OFF and LET ME DIE!"
mc "Gee, lady, calm down. I'll see you tomorrow, when you've recovered. See, I can be a nice guy..."
$ prisonerwillpower -= 1
window hide
show achievementprisoner at posmission
$ renpy.pause(1.0, hard=True)
pause
hide achievementprisoner
$ period += 1
$ seenprisoner = True
scene prison01b with dissolve
show screen mcstats
show screen calendar
show prisonerlying
if stonepiece01 == False and missionge:
    show stone01idle
if mcinjured:
    mc "I'd better go to the medical bay, my neck really hurts..."
    jump Medbay
jump Main01

label PrisonerAnal02bEnd:
scene prisonerfaint with dissolve
mc "Shit, she really DID faint. I was too rough..."
mc "Oh well, I guess she'll recover by tomorrow... I'll just dump my load in her and get out of here..."
$ period += 1
scene prison01b with dissolve
play music "Sounds/waterdrip.mp3"
show screen mcstats
show screen calendar
show prisonerlying
if stonepiece01 == False and missionge:
    show stone01idle
$ seenprisoner = True
if mcinjured:
    mc "I'd better go to the medical bay, my neck really hurts..."
    jump Medbay
jump Main01

label PrisonerThirdDay:
mc "So, today is the day. Just pounding you to oblivion until you talk. Understood, number 6?"
hide prisoner01
show prisoner04
with fastdissolve
pr "Do your filthy deed, you fucking RAPIST! You'll get NOTHING out of me!"
mc "We'll see about that. Get undressed, you know the drill..."
hide screen mcstats
hide screen calendar
stop music
scene prisonfuck01 blurred with dissolve
show prisonerfuck02
pr "My poor pussy, it will never recover! But I must be STRONG! Give me all you can ASSHOLE!"
mc "Alright, you asked for it..."
hide screen mcstats
label Prison03Faster:
play music "Sounds/womansex01.mp3"
hide prisonerfuck02
hide prisonfuckmovie01slow
show prisonfuckmovie01fast
call screen prison03fast
screen prison03fast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PrisonerFuck03End")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("Prison03Slower") 

label Prison03Slower:
hide prisonfuckmovie01fast
show prisonfuckmovie01slow
pr "Finally, a respite from that fast and brutal pounding..."
pause 2.0
pr "But you should not have made such a mistake rookie..."
pr "Because..."
hide prisonfuckmovie01slow
scene prisonfight01 with dissolve
stop music
pr "Now I can use my FAVORITE leg scissoring move!"
mc "Ah, stop it, you're choking me!"
window hide
call MCInjury
$ mcinjuredprisoner = True
$ mcinjured = True
scene prisonfuck02 with dissolve
mc "That's it, I'm done joking around with you! Get ready for the ULTIMATE ANAL POUNDING!"
pr "The ultimate? Does this mean it's going to hurt A LOT?"
mc "CORRECTAMUNDO!"
jump PrisonFuck02c

label PrisonerFuck03End:
mc "I'll fucking blast my creamy load over you now, ready for a heavy dose of scalding spunk number 6?"
pr "NOOOO, please don't waste it!"
stop music
scene prisonercum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Too late! RHAAAA! Take that!"
scene prisonercum02 with dissolve
pr "Why are so you so cruel to me? *sob*"
stop sound
$ prisonerwillpower -= 1
window hide
show achievementprisoner at posmission
$ renpy.pause(1.0, hard=True)
pause
hide achievementprisoner
mc "I might be less cruel if you were to talk..."
pr "Too late, you've spilt your seed, you're no use to me now..."
mc "You think I'm done?"
scene prisonfuck02 with dissolve
show prisonfuck02cumlayout
mc "This time, you will receive the ULTIMATE ANAL POUNDING!"
pr "What? The ULTIMATE? Does this mean it's going to hurt A LOT?"
mc "CORRECTAMUNDO!"
jump PrisonFuck02c

label PrisonFuck02c:
$ prisonerday01 = True
scene prisonarse01 with dissolve
mc "Ready to take my giant teenage fuckstick up your poopchute again number 6?"
pr "No, I'll never be ready for such a monstrous thing!"
scene prisonarse02 with dissolve
play sound "Sounds/womanscream.ogg"
mc "There you go, a solid twelve inches inside your guts."
pr "You're going to KILL me with it if you pound me TOO HARD!"
mc "You took it like a pro last time, you can take it again!"
pr "NOOOOO!"
scene prisonanalbackground with dissolve
label PrisonAnal03Slower:
play music "Sounds/womansex01.mp3"
hide prisonanalfast
show prisonanalslow
call screen prisonanal03slow
screen prisonanal03slow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PrisonerAnal03End")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PrisonAnal03Faster") 

label PrisonAnal03Faster:
hide prisonanalslow
show prisonanalfast
pr "Too much, too much, I can't take it any more, I GIVE UP! Please STOP!"
call screen prisonanal03fast
screen prisonanal03fast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PrisonerAnal03End")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PrisonAnal03Slower") 

label PrisonerAnal03End:
stop music
scene prisonanalcumbackground
show prisonanalcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Fuck Yeah! Another creamy ass-load coming your way number 6!"
pr "This is so humiliating! I feel like a cheap cumdump... *sob*"
$ prisonerwillpower -= 1
window hide
show achievementprisoner at posmission
$ renpy.pause(1.0, hard=True)
pause
hide achievementprisoner
scene prisonerend01 with dissolve
play music "Sounds/waterdrip.mp3"
show screen mcstats
show screen calendar
mc "So, you're gonna talk now?"
if prisonerwillpower <= 0:
    pr "Yes... *sob*... You've broken me..."
    mc "Go on..."
    pr "I'm the LAST spy in the compound... *sob*... I was about to send its location to the forward base at area C3..."
    pr "*sob* That's it, you know everything now... *sob* Please let me go!"
    $ successprisoner = True
    window hide
    show prisonerwin at posmission
    $ renpy.pause(2.0, hard=True)  
    hide prisonerwin
    mc "You did good Number 6. Just the information I needed... I'll leave you to recover then."
if prisonerwillpower >= 1:
    pr "No... *sob* I'm.... strong... I will always cover...for... *sob*.... our God-sent President-for-Life!"
    mc "DAMN IT! TALK, NUMBER 6!"
    show prisonerend02 with fastdissolve
    pr "FUCK OFF and LET ME DIE!"
    mc "(I don't think I'll get anything out of her, I haven't broken her enough... Chief Lena will be disappointed.)"
    window hide
    show prisonerfail at posmission
    $ renpy.pause(2.0, hard=True)
    hide prisonerfail
    $ failprisoner = True
scene prison01b with dissolve
show prisonerlying
if stonepiece01 == False and missionge:
    show stone01idle
$ seenprisoner = True
$ period += 1
mc "Let's report back to Chief Lena then..."

label EndPrisonerMission:
stop music
scene command01 with fade
stop music
show lena01
le "So, what is your report concerning the incredibly important mission I assigned to you? Did the prisoner talk?"
if successprisoner == True:
    mc "Yep, I got her to spill the beans, I know everything Chief Lena!"
    hide lena01
    show lena07
    with fastdissolve
    le "Really? I underestimated you... So, tell me everything you know then..."
    mc "There are no more spies and the forward base is at Area C3, also known as area 51."
    le "Ah, Great to know. I'll update the map then. Congratulations [name], you've earnt yourself a whopping 20 New Dollars and a strong accolade from all of us at the Deep State."
    window hide
    show knowledgeforwardops at posmission
    $ renpy.pause(4.0, hard=True)
    hide knowledgeforwardops    
    $ money += 20
    if mcdeep <= 4:
        call PlusDeepReal
    $ daysprisoner = 999
    le "And... How did you get her to talk out of curiosity?"
    menu:
        "That's my personal secret recipe... (+1 Deep State)":
            hide lena07
            show lena03
            with fastdissolve
            le "I see... A man of secrets."
            call PlusDeep
            le "You can take a well-earned break now. Dismissed!"
            hide lena03 with dissolve
        "She couldn't resist my HUGE dong... (+1 Lust Lena)":
            hide lena07
            show lena11
            with fastdissolve
            le "I see... It must be a mighty impressive... weapon then..."
            call LustPlusLena
            hide lena11
            show lena03
            with fastdissolve
            le "You can take a well-earned break now. Dismissed!"
            hide lena03 with dissolve
if successprisoner == False and prisonerescaped == False:
    mc "Ah yeah, no, I failed. The bitch wouldn't talk I'm afraid."
    hide lena01
    show lena05
    with fastdissolve
    le "I see, you suck just as much as Jake at this. Next time, I'll ask a WOMAN to torture a Trumpster spy instead of a lousy man!"
    mc "Hey, don't insult men! We are still the BEST torturers and rapists on this planet, you can't take that away from us!"
    hide lena05
    show lena10
    with fastdissolve
    le "You are DISMISSED!"
    $ daysprisoner = 999
    hide lena10 with dissolve
if successprisoner == False and prisonerescaped:
    mc "Ah, yes, I remember now. She escaped."
    hide lena01
    show lena10
    with fastdissolve
    le "What??? How on earth could she escape?"
    mc "Well, the door was open and she l...."
    hide lena10
    show lena06
    with fastdissolve
    le "You are INCOMPETENT! She was YOUR responsibility! I'm beginning to suspect you might be a Trumpster SABOTEUR!"
    mc "What, me? Now, come on! It wasn't my fault, she was about to talk and then she just vanished into thin air."
    hide lena06
    show lena10
    with fastdissolve
    le "You FAILED. Nothing for you and no accolade from the Deep State!"
    if mcdeep >= 1 and mcdeep <= 4:
        window hide
        show minusdeep at posmission
        $ renpy.pause(2.0, hard=True)
        hide minusdeep
        $ mcdeep -= 1
    $ daysprisoner = 999
    hide lena10 with dissolve

if mcinjured:
    mc "I'd better go to the medical bay, my neck really hurts..."
    jump Medbay
jump Main01


label PrisonerFuck04:
mc "Ah, there you are, number 6..."
if successprisoner:
    hide prisoner01
    show prisoner04
    with fastdissolve
    pr "What, you again? But I've already spilt the beans! What do you want from me?"
if failprisoner:
    hide prisoner01
    show prisoner02
    with fastdissolve
    pr "What, you again? It's too late, I'll never talk, you should know that you FAILED by now, LOSER!"
menu:
    "This time, I'm here to help you escape Number 6. I'm almost a Trumpster now you see. (LET HER ESCAPE, +1 Trumpsters, faction change)" if mctrumpster == 4:
        pr "And how are you going to get me out exactly?"
        if period == 4:
            mc "I've got the keys. We can literally just walk out of here, there are no guards."
            pr "Let's do it then!"
            jump PrisonerEscape
        mc "Ah yes, I should have planned this better I guess. I'll come back at night, since it's the only time we can escape without Chief Lena seeing us."
        mc "Just stay put and wait for me."
        pr "Oh damn, I was planning on a night out, I guess I'll have to cancel.... (snickers)."
        $ prisonerescapenight = True
        jump LeavePrison
    "This time, I'm here to help you escape Number 6. I'm a Trumpster now you see. (LET HER ESCAPE)" if mctrumpster == 5:
        pr "And how are you going to get me out exactly?"
        if period == 4:
            mc "I've got the keys. We can literally just walk out of here, there are no guards."
            pr "Well that's easier than I thought. Those Deep State haters really don't know how to run a torture facility like we can, hey?"
            mc "Yeah. Bunch of LOSERS. Come!"            
            jump PrisonerEscape
        mc "Ah yes, I should have planned this better I guess. I'll come back at night, since it's the only time we can escape without Chief Lena seeing us."
        mc "Just stay put and wait for me."
        pr "Oh damn, I was planning on a night out, I guess I'll have to cancel.... *snickers*."
        $ prisonerescapenight = True
        jump LeavePrison
    "Err... I guess, free sex.":
        hide prisoner02
        hide prisoner04
        show prisoner03
        with fastdissolve
        pr "Oh, when will this nightmare ever end?"
        mc "Not for a while. This section of the ren'py code is on a perpetual loop until I become a Trumpster. Now get undressed, you know the drill..."
        jump PrisonerFuckall
    "Nothing, I was just passing by to say hi.":
        pr "Are you fucking kidding me? I've been kept prisoner here for so long, I can't even remember my name anymore!"
        mc "I believe it's \"Number 6\"."
        pr "I am NOT a NUMBER, I am a...err... chained woman!"
        mc "Yeah, whatever. Bye!"
        jump LeavePrison

label PrePrisonerEscape:
scene prison02
show prisoner02
with fade
mc "Here I am, Number 6!"
pr "Thanks God! I feel like I can trust you as much as I can trust the Senate to do absolutely nothing!"
mc "Right..."
$ prisonerescapenight = False

label PrisonerEscape:
scene prisonerescape with dissolve
$ prisonerescaped = True
mc "This way!"
pr "Well that's easier than I thought. Those Deep State haters really don't know how to run a torture facility like we can, hey?"
mc "Yeah. Bunch of LOSERS. Come!"
scene command01 with dissolve
stop music
mc "And now, that corridor over there, just walk out, no one will notice you, the night duty watch tower is on the opposite side of the compound..."
pr "Thanks a lot! I will definitely let our Glorious President-for-Life know about your patriotic deed!"
pr "You might even get the Medal of Complicity, the highest honor in our Land!"
$ medalcomplicity = True
call PlusTrumpster
pr "And also, here's all my money, I don't need it anymore. Ten bucks that I kept in my... err... personal space."
$ money += 10
jump Bedroom

label PrisonerFuckall:
$ seenprisoner = True
stop music
hide screen mcstats
hide screen calendar
scene prisonfuck01 blurred
show prisonerfuck02
with dissolve
pr "You're too rough, you'll destroy my pussy!"
mc "That's the idea..."
play music "Sounds/barbarasex.mp3"
label Prison05Slower:
hide prisonfuckmovie01fast
show prisonfuckmovie01slow
call screen prison05slow
screen prison05slow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PrisonerFuck05End")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("Prison05Faster") 

label Prison05Faster:
hide prisonfuckmovie01slow
show prisonfuckmovie01fast
call screen prison05fast
screen prison05fast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PrisonerFuck05End")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("Prison05Slower") 

label PrisonerFuck05End:
mc "Fuck, I'm about to BLOW!"
menu:
    "Come inside her":
        jump PrisonFuck05CumInside
    "Pull out and douse her back":
        jump PrisonFuck05CumOutside

label PrisonFuck05CumInside:
stop music
scene prisonfuck01 blurred
show prisonercum03
with dissolve
mc "Damn, ssoo good! That tight pussy is milking ounces of cream out of my cum factories!"
scene prisonfuck02 with dissolve
mc "That's it, I'm done joking around with you! Get ready for the ANAL POUNDING of your life!"
pr "How many times do I have to tell you that your dong is too big for that!"
mc "As often as I come around to visit..."
jump PrisonFuck02e

label PrisonFuck05CumOutside:
stop music
scene prisonercum01 with dissolve
mc "RHAAA!"
scene prisonercum02 with dissolve
mc "There you go, I've plastered your back with my cum. I OWE you now BITCH!"
pr "Why are so you so cruel to me? *sob*"
scene prisonfuck02
show prisonfuck02cumlayout
with dissolve
mc "You know how it goes, now I want to feel yout TIGHT ASS wrapped around my pole!"
pr "How many times do I have to tell you that your dong is too big for that!"
mc "As often as I come around to visit..."
jump PrisonFuck02e

label PrisonFuck02e:
scene prisonarse01 with dissolve
mc "Ready to take my giant teenage fuckstick up your poopchute again, number 6?"
pr "No, I'll never be ready for such a monstrous thing!"
scene prisonarse02 with dissolve
mc "You know you like it DEEP DOWN!"
pr "NOOOOO!"
play music "Sounds/womansex01.mp3"
scene prisonanalbackground with dissolve
label PrisonAnal05Slower:
hide prisonanalfast
show prisonanalslow
call screen prisonanal05slow
screen prisonanal05slow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PrisonerAnal05End")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PrisonAnal05Faster") 

label PrisonAnal05Faster:
hide prisonanalslow
show prisonanalfast
pr "Too much, too much, I can't take it any more! Please STOP!"
call screen prisonanal05fast
screen prisonanal05fast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PrisonerAnal05End")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PrisonAnal05Slower") 

label PrisonerAnal05End:
stop music
scene prisonanalcumbackground
show prisonanalcum01
with dissolve
mc "Fuck Yeah! Another creamy ass-load coming your way number 6!"
pr "This is so humiliating! I feel like a cheap cumdump... *sob*"
scene prisonerend01 with dissolve
mc "That's exactly what you are..."
pr "You fucking ASSHOLE!"
mc "Now, now, no need to be rude. See you another time, whenever I CHOOSE, Number 6!"
show screen mcstats
show screen calendar
scene prison01b with dissolve
show prisonerlying
if stonepiece01 == False and missionge:
    show stone01idle
$ period += 1
jump Main01

label LeavePrison:
if prisonerescaped:
    scene prison01b
if prisonerescaped == False:
    scene prison01
    show prisoneridle
if stonepiece01 == False and missionge:
    show stone01idle
jump Main01

label MissionChurch:
show screen calendar
show screen mcstats
$ loc = "command"
scene command01
show lena01
with dissolve
le "Ah, there you are. I have a mission of the utmost importance for you, [name]!"
mc "I'm all ears, Chief."
hide lena01
show lena06
with fastdissolve
le sidele "The influence of the Church of the Redeeming Phallus is getting out of hands. Too many of our girls are falling for this religious gobbledygook."
hide lena06
show lenapensive
with fastdissolve
le sidele "I also strongly suspect Priest Tyrone of being nothing but a sexual pervert intent on taking control of the Compound through the manipulation of the masses!"
hide lenapensive
show lena07
with fastdissolve
le sidele "Try and gather incriminating evidence involving Priest Tyrone and report to me in three days. And only me."
if persistent.tipson and angiereunited == False:
    show lenachurchtip at tips with dissolve
    pause
    hide lenachurchtip 
if mcchurch == 5:
    mc sidemc "I must object to this unholy mission! As an upstanding \"pillar\" of the Church, I refuse to investigate our priest! Get lost!"
    hide lena07
    show lena08
    with fastdissolve    
    le sidele "I'm not giving you a choice, gullible fool! So withdraw from this silly faction at once!"
    call MinusChurch
    le "As per usual with religion, I don't get a choice in the matter apparently... Fine, I'll do your unholy mission then."
    hide lena08
    show lena02
    with fastdissolve        
    $ missionchurch = True
    $ dayschurch = 3
    window hide
    show missionchurch at posmission
    $ renpy.pause(1.0, hard=True)
    show text "{font=Gui/Boogaloo-Regular.ttf}{color=#ff0000}{size=35}[dayschurch]{/font}" at ChurchPosition
    pause
    hide text
    hide missionchurch
    jump MissionChurch02
$ missionchurch = True
$ dayschurch = 3
window hide
show missionchurch at posmission
$ renpy.pause(1.0, hard=True)
show text "{font=Gui/Boogaloo-Regular.ttf}{color=#ff0000}{size=35}[dayschurch]{/font}" at ChurchPosition
pause
hide text
hide missionchurch
mc "Roger that, Chief Lena."
label MissionChurch02:
le "Now go, time is of the essence. After three days, he will have garnered too much support from the brainwashed masses. Infiltrate the church, at nights preferably, when all the perversion comes to light..."
jump Command

label LenaChurchEnd:
scene command01 with dissolve
show lena01
$ missionchurch = False
le "So, have you been able to gather evidence against Priest Tyrone? I want to counter his influence as soon as possible, before it's too late."
if mcchurch >= 5:
    mc "I investigated everything I could, interviewed plenty of potential witnesses, I explored all avenues..."
    mc "And I must conclude that Priest Tyrone is entirely innocent of any wrongdoing. This is my report, Chief Lena."
    hide lena01
    show lena03
    with fastdissolve
    le "What? I find that hard to believe... But I guess I must take your word for it. Consider this mission terminated. Dismissed."
    jump Main01
if churchevidence >= 3:
    mc "Oh yeah. That guy is as dodgy as it comes..."
    hide lena01
    show lena07
    with fastdissolve
    le "I knew it! Tell me everything you know..."
    mc "I have seen him abuse girls as young as... err... 18, yeah, definitely 18."
    if pencescroll:
        mc "And also, he doesn't follow the Church's official guidelines which I have recovered after much hard labor."
    hide lena07
    show lena06
    with fastdissolve    
    le "Well done for a successful mission! I knew I could count on you..."
    call LustPlusLena
    le "Thanks to you, Father Tyrone is done for! He won't be bothering me again and I'll keep the Church under a tight lid. You deserve a reward. $40 shiny dollars."
    $ successchurch = True
    $ dayschurch = 999
    $ money += 40
    jump Main01
if churchevidence <= 2:
    mc "I certainly accumulated some evidence, but maybe not quite enough."
    hide lena01
    show lena03
    with fastdissolve
    le "What do you mean?"
    mc "Well, you know, some things that MIGHT be construed as wrongdoings, but without any clear evidence."
    hide lena03
    show lena05
    with fastdissolve
    le "In other words, you failed miserably..."
    mc "Well, hang on, I mean, I worked my butt off on this mis..."
    hide lena05
    show lena10
    with fastdissolve    
    le "You're USELESS! Get out of my sight! You are DISMISSED!"    
    $ failchurch = True
    $ dayschurch = 999
    jump Main01
if churchevidence == 0:
    mc "Ah, yeah, THAT mission. Totally forgot about it to be honest."
    hide lena01
    show lena10
    with fastdissolve
    le "Are you fucking kidding me? I CANNOT TRUST you to do anything around here!"
    call LustMinusLena
    mc "Sorry, my bad."
    le "You're USELESS! Get out of my sight! You are DISMISSED!" 
    $ failchurch = True
    $ dayschurch = 999
    jump Main01
    
