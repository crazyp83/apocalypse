label Bar:
stop music
if day == 5 and period == 3:
    jump FridayParty
    
if day == 6 and period == 3:
    jump SaturdayFight

scene bar01 with dissolve
play music "Sounds/barmusic.mp3"
show screen calendar
show screen mcstats
call screen barevening
screen barevening:
    modal True    
    if period == 1 or period == 2 or (period == 3 and pregbastart >= 4):
        imagebutton:
            focus_mask True
            idle "v06/sofaidle.png"
            hover "v06/sofahover.png"
            action Jump ("SofaEvening")
    if period == 3 and pregbastart <= 3:
        imagebutton:
            focus_mask True
            idle "v081/sofabarbaraidle.png"
            hover "v081/sofabarbarahover.png"
            action Jump ("BarbaraSofaEvening")
    imagebutton:
        focus_mask True
        idle "v06/leave.png"
        hover "v06/leave.png"
        action Jump ("LeaveBar")
    imagebutton:
        focus_mask True
        idle "v06/gotobar.png"
        hover "v06/gotobar.png"
        action Jump ("BarEvening02")    
    if knowstrip == True:
        imagebutton:
            focus_mask True
            idle "Bar/stripdooridle.png"
            hover "Bar/stripdoorhover.png"
            action Jump ("StrippingEvening")

label SofaEvening:
"A nice sofa for people to relax on and get stone-drunk."
jump Bar

label BarbaraSofaEvening:
scene barbaraevening01 with dissolve
if persistent.tipson and frenchtipseen == False:
    show frenchtip at tips with dissolve
    pause
    hide frenchtip
    $ frenchtipseen = True
ba "Well, hello [name]!"
label BarbaraSofaDialogue:
menu:
    "I'd like some private French lessons." if haremba == False and money >= 5:
        if barbaraspokefrench == False:
            scene barbaraevening02 with dissolve
            ba "Well, of course, I'd be happy to teach such an eager pupil. For a 5$ fee."
            mc "What? Why can't you teach me for FREE?"
            scene barbaraevening01 with dissolve
            $ barbaraspokefrench = True
            ba "Our great country's foundation was built upon the cornerstone of unbridled rampant capitalism!"
            menu:
                "Agree ( -5$)":
                    mc "Alright. Let's get over it then..."
                    $ barbaranolust = False
                    $ money -= 5
                    jump BarbaraSofaLesson
                "Umpf. I'll think about it...":
                    scene barbaraevening03 with dissolve
                    ba "You're missing out on one of the most important languages in the world! Presently."
                    mc "C'est la vie!"
                    jump Bar
        if barbaraspokefrench:
            scene barbaraevening06 with dissolve
            ba "Sure! You know the drill. Hand over the cash."
            menu:
                "Agree ( -5$)":
                    mc "Alright. Let's get over it then..."
                    $ money -= 5
                    $ barbaranolust = False
                    jump BarbaraSofaLesson
                "Umpf. I'll think about it...":
                    scene barbaraevening03 with dissolve
                    ba "You're missing out on one of the most important languages in the world! Presently."
                    mc "C'est la vie!"
                    jump Bar
    "I'd like some private French lessons." if haremba and money >= 5:
        if barbaraspokefrench == False:
            scene barbaraevening02 with dissolve
            ba "Well, of course, I'd be happy to teach such an eager pupil. For a 5$ fee."
            mc "What? Why can't you teach me for FREE?"
            scene barbaraevening01 with dissolve

            $ barbaraspokefrench = True
            ba "Our great country's foundation was built upon the cornerstone of unbridled rampant capitalism! Up to and including slavery."
            menu:
                "Agree ( -5$)":
                    mc "Alright. Let's get over it then..."
                    $ money -= 5
                    $ barbaranolust = False
                    jump BarbaraSofaLesson
                "Umpf. I'll think about it...":
                    ba "You're missing out of the most important language in the world! Now."
                    mc "C'est la vie!"
                    jump Bar
                "And YOU happen to be my sex slave! So I want it for FREE!":
                    scene barbaraevening03 with dissolve
                    ba "Umpf... I guess it is your prerogative as my Harem Master. But I strongly object and will eventually seek educational emancipation!"
                    mc "Whatever. Let's get on with it."
                    $ barbaranolust = True
                    jump BarbaraSofaLesson
        if barbaraspokefrench:
            scene barbaraevening06 with dissolve
            ba "Sure! Will you pay me 5$?"
            menu:
                "I suppose... ( -5$)":
                    ba "That's a good boy."
                    mc "Alright. Let's get over it then..."
                    $ barbaranolust = False
                    $ money -= 5
                    jump BarbaraSofaLesson
                "Nope. I want a free lesson.":
                    scene barbaraevening03 with dissolve
                    ba "Umpf. I guess I don't have a choice. As your Harem slave."
                    $ barbaranolust = True
                    mc "C'est la vie!"
                    jump BarbaraSofaLesson
    "I'd like to invite you on a date Barbara." if lustba >= 2 and knowredcanyon and barbaradatedone == False:
        scene barbaraevening02 with dissolve      
        ba "A date? Between a teacher and her teenage student?"
        mc "Nothing wrong about that. Most boys' first crush is their teacher."
        scene barbaraevening06 with dissolve           
        ba "So I'm your crush then [name]? How sweet of you. Well, I'll allow my favorite student to have a date with his crush then!"
        $ barbaradateon = True
        mc "I'll pick you up in the morning."
        scene barbaraevening03 with dissolve
        ba "Ooh, that means I'll have to cancel class.... I'll think of something!"
        scene barbaraevening01 with dissolve
        ba "Why don't you hang around for a while. I'll buy you a drink. And make sure you don't go and seduce some other woman until our date..."
        mc "Oh, I would never do such a thing Barbara!"
        ba "Just stay."
        scene barbaraevening05 with fade        
        "(A while later...)"
        ba "Oh well, the evening just flew by! I should go back to my bedroom and prepare myself for our date..." 
        $ seenbar = True
        jump LeaveBar
    "I think it's time now for you to join my harem teach..." if lustba >= 4 and haremba == False and barbaraharem == False and girlsinharem <= 5 and barbaradatedone:
        scene barbaraevening02 with dissolve
        ba "I can't break the law and end up in jail like so many horny size-queen, teen-loving teachers before me!"
        mc "If you join my harem, sex between us becomes perfectly legal. Encouraged even. You know, to re-populate the Earth?"
        scene barbaraevening01 with dissolve
        ba "Mmh, it is true that we are both WHITE and... I should do my duty for our Glorious New Nation!"
        $ haremba = True
        $ girlsinharem += 1
        $ barbaraharem = True
        window hide
        show harembarbara at plus
        $ renpy.pause(2.0, hard=True)
        hide harembarbara
        mc "I'll call you at nights. You know, when the other students are sleeping."
        scene barbaraevening06 with dissolve   
        ba "I can't wait. To get impregnated with your SUPERIOR seed!"
        jump BarbaraSofaDialogue
    "I think it's time for you to re-join my harem Barbara..." if lustba >= 4 and haremba == False and barbaraharem  and barbaradismissed == False  and girlsinharem <= 5:
        scene barbaraevening03 with dissolve      
        ba "It ended badly for me last time..."
        mc "And you learnt from your mistakes. So you've improved and there's no reason for the same thing to happen again."
        scene barbaraevening06 with dissolve      
        ba "My mistakes? I don't remember that. *sigh* Fine. I can't refuse anything to my favorite horse-hung student!"
        $ haremba = True
        $ girlsinharem += 1
        $ barbaraharem = True
        window hide
        show harembarbara at plus
        $ renpy.pause(2.0, hard=True)
        hide harembarbara
        mc "I'll call you at nights. You know, when the other students are sleeping."
        scene barbaraevening02 with dissolve      
        ba "Hopefully, it will last longer than last time..."
        jump BarbaraSofaDialogue
    "I obtained a very rare autograph from Q. To your name." if qautograph and gaveqautograph == False:
        scene barbaraevening04 with dissolve
        ba "Really? That is wonderful!"
        call LustPlusBarbara
        scene barbaraevening01 with dissolve
        ba "Q is my dream man... I imagine him as tall, muscular, handsome with smoldering eyes that could melt you with just a glance and..."
        mc "Not quite. I won't spoil it, but you got the tall bit right at least..."
        scene barbaraevening02 with dissolve
        ba "Best that you don't tell me then."
        mc "I think so too..."
        $ qautograph = False
        $ gaveqautograph = True
        ba "Please stay and have a drink with me to thank you for that kind gift."
        mc "Sure, why not. I mean, it's not like I'm underage or anything, right?"
        scene barbaraevening05 with fade        
        "(A while later...)"
        ba "Thanks again for the autograph [name]! I will add it to my collection of Autographs from Great American Heroes." 
        $ seenbar = True
        jump LeaveBar
    "Leave":
        ba "Bye [name]!"
        jump LeaveBar

label BarbaraSofaLesson:
scene barbaraevening05 with fade
$ period += 1
$ frenchlesson += 1
ba "And there you have it. You learnt a great deal of je-ne-sais-quoi tonight I reckon."
mc "You mean French?"
ba "Oui."
if frenchlesson == 2 and mcfrench <= 9:
    call PlusFrench
    $ frenchlesson = 0
    if barbaranolust == False:
        call LustPlusBarbara
if frenchlesson == 3 and mcfrench >= 10:
    call PlusMaxFrench
    if barbaranolust == False:
        call LustPlusBarbara
    $ frenchlesson = 0
mc "Thanks teach, it's getting late, better go back to my room."
ba "Bonne nuit [name]!"
mc "Err, yeah, good night Barbara."
jump Bedroom

label BarEvening02:
scene bar03 with dissolve
call screen barevening02
screen barevening02:
    modal True    
    imagebutton:
        focus_mask True
        idle "Icons/exitidle.png"
        hover "Icons/exithover.png"
        action Jump ("Bar")
    imagebutton:
        focus_mask True
        idle "Bar/marniebar02idle.png"
        hover "Bar/marniebar02hover.png"
        action Jump ("BarEvening03")    
    imagebutton:
        focus_mask True
        idle "Bar/barjoeidle.png"
        hover "Bar/barjoehover.png"
        action Jump ("BarJoe")    
    imagebutton:
        focus_mask True
        idle "Bar/cyrlbar02idle.png"
        hover "Bar/cyrlbar02hover.png"
        action Jump ("CyrlDialogue01")
    
label BarEvening03:
$ seenbar = True
scene bar02
show marnie02
show bar02b
with dissolve
if seenmineinside and toldmarniemine == False:
    ma "Oh, hi [name]! I must thank you for that wonderful booze you brought back from one of your scouting missions, it's top ace stuff!"
    call LustPlusMarnie
    ma "I was actually running low on liquor to mix with my Greasy Tar cocktail..."
    $ toldmarniemine = True
    jump MarnieEveningChoice    
ma "Welcome to Marnie's Bar! What can I do for you?"
label MarnieEveningChoice:
show marnie02
show bar02b    
if persistent.tipson:
    show marnietip at tips with dissolve
    pause
    hide marnietip
menu:
    "Is it really YOUR bar?":
        ma "Well... I lease it of course. But I'm in charge of everything, including making my specialty cocktail, the \"Greasy Tar\". Would you like to try one for a dollar?"
        menu:
            "Err... I'll pass, thank you.":
                ma "You're missing out!"
                hide marnie02
                hide bar02b
                jump MarnieEveningChoice
            "Yeah, why not." if money >= 1:
                hide marnie02
                hide bar02b
                show marnie03
                show bar02b
                ma "One greasy tar for the gentleman!"
                $ money -= 1
                mc "(God, this stuff is vile...)"
                hide marnie03
                hide bar02b
                show marnie04
                show bar02b                
                ma "So how was it?"
                mc "Umm, lovely! But I've had enough for tonight, I don't want to get drunk."
                $ drunkcocktail = True
                hide marnie04
                hide bar02b                
                jump MarnieEveningChoice                    
            "I'm broke. Like totally." if money == 0:
                hide marnie02
                hide bar02b
                show marnie04
                show bar02b
                ma "Too bad, you're missing out!"
                hide marnie04
                hide bar02b
                jump MarnieEveningChoice                    
    "Tell me something I want to know..." if drunkcocktail == True and gottip == False:
        hide marnie02
        hide bar02b
        show marnie04
        show bar02b
        if marnietip == 0:
            ma "There's a beautiful place right behind the hills outside the compound..."
            ma "It's called the Red Canyon. Ideal location to invite girls on a romantic date... *wink*"
            $ knowredcanyon = True
            window hide
            show knowledgecanyon at posmission
            $ renpy.pause(2.0, hard=True)
            pause
            hide knowledgecanyon
            hide marnie04
            hide bar02b
            show marnie06
            show bar02b            
            ma "That's it, I gave you a tip, time to leave and let me serve all my OTHER customers..."
            $ marnietip += 1
            $ gottip = True
            jump LeaveBar            
        elif marnietip >= 1 and knowrubytip == False:
            ma "If you ever want to invite Ruby on a date, don't tell her it's actually a date. She thinks dates are for sissies."
            mc "Alright, I'll bear that in mind, thanks for the tip Marnie!"
            $ marnietip += 1
            $ knowrubytip = True
            $ gottip = True
            hide marnie04
            hide bar02b
            show marnie06
            show bar02b            
            ma "That's it, I gave you a tip, time to leave and let me serve all my OTHER customers..."
            jump LeaveBar            
        elif marnietip >= 1 and day<= 4 and marnietipfight == False:
            ma "Michiko and Suki are battling it out this Saturday evening in our virtual fight night. I would definitely put my money on Michiko if I were you."
            hide marnie04
            hide bar02b
            show marnie01
            show bar02b            
            ma "She's got way more REAL training than Suki and that is a big PLUS in this game..."
            mc "Alright, I'll bear that in mind, thanks for the tip Marnie!"
            $ marnietip += 1
            $ marnietipfight = True
            $ gottip = True
            hide marnie01
            hide bar02b
            show marnie06
            show bar02b            
            if persistent.tipson and angiereunited == False:
                show sukitip at tips with dissolve
                pause
                hide sukitip 
            ma "That's it, I gave you a tip, time to leave and let me serve all my OTHER customers..."
            jump LeaveBar            
        elif marnietip >= 1 and marnietipclara == False:
            hide marnie04
            hide bar02b
            show marnie02
            show bar02b            
            ma "I heard you were looking for Clara's \"Redemption Box\"."
            mc "How do you even know that???"
            hide marnie02
            hide bar02b
            show marnie04
            show bar02b            
            ma "I know EVERYTHING, remember?"
            mc "Ah yes, that's true. So, what's your tip, where is it?"
            hide marnie04
            hide bar02b
            show marnie02
            show bar02b            
            ma "Father Tyrone hides it in the crypt."
            mc "And... You have the key to it, right?"
            hide marnie02
            hide bar02b
            show marnie06
            show bar02b            
            ma "No, why would I have the key to that absolutely filthy place that's never cleaned?"
            mc "Mmmh, you mentioning how dirty it is gave me an idea. I have to convince Father Tyrone to let me clean the crypt."
            if persistent.tipson:
                show clara03tip at tips with dissolve
                pause
                hide clara03tip
            hide marnie06
            hide bar02b
            show marnie02
            show bar02b            
            ma "Sounds doable. Thanks to my tip obviously!"
            $ marnietip += 1
            $ marnietipclara = True
            $ gottip = True
            hide marnie02
            hide bar02b
            show marnie06
            show bar02b            
            ma "That's it, I gave you a tip, time to leave and let me serve all my OTHER customers..."
            jump LeaveBar            
        elif marnietip >= 3:
            ma "I should say something here but I don't know what since it hasn't been implemented yet..."
        elif marnietip == 5:
            ma "I should say something here but I don't know what since it hasn't been implemented yet..."
        hide marnie04
        hide bar02b
        jump MarnieEveningChoice                    
    "Do you have a lot of customers?" if spokemarnie03 == False:        
        hide marnie02
        hide bar02b
        show marnie04
        show bar02b
        ma "Of course! This is the only place to relax and enjoy a few drinks with friends. Everyone is welcome, and we often have faction meetings."
        mc "Faction meetings? What's that?"
        ma "Like-minded people belonging to the same faction come to share their views with each other in our friendly atmosphere!"
        mc "And do you belong to a faction yourself Marnie?"
        hide marnie04
        hide bar02b
        show marnie05
        show bar02b
        ma "Mind your own business!"
        if mcchurch<= 4 and mcwarrior<= 4 and mcsierra<= 4 and mctrumpster<= 4 and mcdeep<= 4:
            mc "I was just asking, I don't belong to any faction myself..."
            ma "Well, you should join the Road Warriors then. It's the best faction by far!"
            mc "Ah! So YOU are a Road Warrior then!"
            hide marnie05
            hide bar02b
            show marnie06
            show bar02b
            ma "Err... Ok, maybe I am, what's it to you anyway?"
            mc "Nothing, it's just that I want to know people better around here."
            ma "Well, I ain't telling you jack about nobody until you buy a \"Greasy Tar\"!"
            mc "Ok, I get it..."
            hide marnie06
            hide bar02b
            jump MarnieEveningChoice
        if mcchurch == 5:
            mc "I am a proud member of the Church of the Redeeming Phallus myself."
            ma "Proud? There's nothing to be proud about belonging to a mysogynistic cult!"
            mc "Ah, so you're NOT a member of the Church then."
            hide marnie05
            hide bar02b
            jump MarnieEveningChoice
        if mcwarrior == 5 and gotlustmarnie == False:
            mc "I am a proud Road Warrior myself."
            hide marnie05
            hide bar02b
            show marnie02
            show bar02b
            ma "Really? Let me see your tattoo then..."
            mc "Err, it's on my cock actually."
            hide marnie02
            hide bar02b
            show marnie01
            show bar02b
            ma "Ok, don't show me then. Mine is on my butt anyway... But I'm happy to see you are one of US. *wink*"
            call LustPlusMarnie
            $ gotlustmarnie = True
            hide marnie01
            hide bar02b
            $ spokemarnie03 = True
            jump MarnieEveningChoice
        hide marnie05
        hide bar02b
        jump MarnieEveningChoice
    "Is there any kind of entertainment for... men, if you see what I mean..." if knowstrip == False:
        hide marnie02
        hide bar02b
        show marnie06
        show bar02b
        ma "I think I know what you mean... And you're in luck. Some girls try and make a bit of extra money on the side via private striptease sessions..."
        hide marnie06
        hide bar02b
        show marnie04
        show bar02b
        $ knowstrip = True
        if day == 1:
            ma "Tonight, Penny is doing a shift. The discreet door behind the bar if you are interested..."
        if day == 2:
            ma "Tonight, Gwen is doing a shift. The discreet door behind the bar if you are interested..."
        if day == 3:
            ma "Tonight, Amy is doing a shift. The discreet door behind the bar if you are interested..."
        if day == 4:
            ma "Tonight, Clara is doing a shift. The discreet door behind the bar if you are interested..."
        if day == 7:
            ma "Tonight, Michiko is doing a shift. The discreet door behind the bar if you are interested..."
        hide marnie04
        hide bar02b
        jump MarnieEveningChoice    
    "Would you be so kind as to tell me who's on shift tonight in the \"backroom\"?" if knowstrip == True:
        hide marnie02
        hide bar02b
        show marnie04
        show bar02b
        if day == 1:
            ma "Tonight, it's Penny's shift."
        if day == 2:
            ma "Tonight, it's Gwen's shift."
        if day == 3:
            ma "Tonight, it's Amy's shift."
        if day == 4:
            ma "Tonight, it's Clara's shift."
        if day == 5:
            ma "Tonight, it's PARTY TIME! Everyone will be on the dancefloor and the backdoor will therefore be unavailable to men..."
            ma "I suggest you come tonight anyway because you don't want to miss out on our wonderful Friday Evening Rave Parties!"
            mc "Alright, I'll keep a note of that event in my agenda."
        if day == 6:
            ma "Tonight, it's VIRTUAL FIGHT NIGHT! Everyone will be watching and betting on the weekly contestants and the backdoor will therefore be unavailable to men..."
            ma "I suggest you come tonight anyway because you don't want to miss out on our wonderful Saturday Virtual Sports Evening!"
            mc "Alright, I'll keep a note of that event in my agenda."
        if day == 7:
            ma "Tonight, it's Michiko's shift."
        mc "Thank you for letting me know!"
        hide marnie04
        hide bar02b
        jump MarnieEveningChoice
    "I would like to gift you a beautiful necklace that I found on my road adventures." if necklace:
        hide marnie02
        hide bar02b
        show marnie04
        show bar02b
        ma "I hope you obtained it the hard way, I am not easily bought. Except if you buy drinks from me."
        mc "I didn't buy it, I earned it! And now it's yours if you accept..."
        ma "Let me try it on..."
        hide marnie04
        hide bar02b
        show marnienecklace with fastdissolve
        show bar02b
        ma "I like it... A lot. Thank you for your kind gift."
        $ necklace = False
        call LustPlusMarnie
        ma "And I'll give you a free  soda for that! But I have to go and serve other customers..."
        jump LeaveBar   
    "I'd like to invite you on a date, Marnie." if lustma >= 2 and marniedatedone == False and knowredcanyon:
        ma "That's nice of you. Let me guess, you'll take me to Red Canyon, the place I TOLD YOU ABOUT?"
        mc "Yep. Well, it's beautiful, right?"
        hide marnie02
        hide bar02b
        show marnie06
        show bar02b
        with fastdissolve
        ma "And how do you know? You've taken OTHER girls there, haven't you?"
        mc "I was only prepping myself up for a date with YOU."
        hide marnie06
        hide bar02b
        show marnie04
        show bar02b
        with fastdissolve
        ma "I hope you're ready to make it MEMORABLE for me then, since I gladly accept [name]!"
        mc "Of course Marnie! I'll pick you up in the morning then!"
        ma "I can't wait for MY date! But I have to serve other customers now..."
        $ marniedateon = True
        jump LeaveBar
    "I'd like to show you something (hypnotize her, +1 lust)" if pendulum and showedpendulum == False:
        call UsePendulum
        hide marnie02
        hide bar02b
        show marnie03
        show bar02b
        with fastdissolve
        ma "Wh...what happened... Oh, hi [name], here's a free soda drink for you cos... I don't know."
        call LustPlusMarnie
        hide marnie03
        hide bar02b
        show marnie06
        show bar02b
        with fastdissolve
        ma "Now, where were we?"
        $ showedpendulum = True
        hide marnie06
        hide bar02b
        jump MarnieEveningChoice   
    "I have a proposition for you... You join my harem and I get to fuck you to heavens and back." if lustma >= 4 and haremma == False and marnieharem == False and girlsinharem <= 5 and marniedatedone:
        hide marnie02
        hide bar02b
        show marnie01
        show bar02b
        with fastdissolve
        ma "Mmh... As a Road Warrior, I need my freedom, but as a woman, I need my SEX, so I accept!"
        mc "I'll call you later in the evening and I'll show you what you've been missing..."
        $ haremma = True
        $ girlsinharem += 1
        $ marnieharem = True
        window hide
        show haremmarnie at plus
        $ renpy.pause(2.0, hard=True)
        hide marnie01
        hide bar02b
        show marnie04
        show bar02b
        with fastdissolve        
        ma "I can't wait [name]!"
        hide haremmarnie
        hide marnie04
        hide bar02b        
        jump MarnieEveningChoice   
    "I know we've had some rough times... But I think it's time for you re-join my harem and have some GOO-OO-OOD times!" if lustma >= 4 and haremma == False and marnieharem and marniedismissed == False and girlsinharem <= 5:
        hide marnie02
        hide bar02b
        show marnie01
        show bar02b
        with fastdissolve
        ma "Mmh, well, the sex was GOOD indeed. Especially the femdom bit... So fine, I'll join back!"
        $ haremma = True
        $ girlsinharem += 1
        window hide
        show haremmarnie at plus
        $ renpy.pause(2.0, hard=True)
        hide haremmarnie
        mc "Great. Then, we'll see each other at nights for some GOO-OOOOD times again!"
        hide marnie01
        hide bar02b
        show marnie04
        show bar02b
        with fastdissolve        
        ma "I can't wait [name]!"
        hide haremmarnie
        hide marnie04
        hide bar02b                
        jump MarnieEveningChoice   
    "Could I have access to the virtual fight night cartridges?" if sukifightquest:
        hide marnie02
        hide bar02b
        show marnie05
        show bar02b
        with fastdissolve
        ma "No, you definitely could NOT."
        mc "Ah well, it was a worth a try."
        hide marnie05
        hide bar02b
        jump MarnieEveningChoice   
    "Leave":
        hide marnie02
        hide bar02b
        show marnie04
        show bar02b
        ma "Goodbye [name], come again soon!"
        jump BarEvening02
          
label StrippingEvening:
if period <= 2:
    "There is no stripping during the day. It's an evening activity..."
    jump Bar
if day == 1 and period == 3:
    jump PennyPreStrip01
if day == 2 and period == 3:
    jump GwenPreStrip01
if day == 3 and period == 3:
    jump AmyPreStrip01
if day == 4 and period == 3:
    jump ClaraPreStrip01
if day == 5:
    "There is no stripping going on tonight, people are too busy enjoying themselves."
    jump Bar
if day == 6:
    "There is no stripping going on tonight, people are too busy enjoying themselves."
    jump Bar
if day == 7 and period == 3:
    jump MichikoPreStrip01
if period == 4:
    "Everyone's asleep and so should you be."
    jump Bedroom
    
label CyrlDialogue01:
$ seenbar = True
scene bar04 with dissolve
show cyrl03
if seencyrl == False:
    cy "Greetings, human friend. My name is Cyrl."
if seencyrl:
    cy "Greetings, human friend."
label CyrlDialogueMenu01:
$ seencyrl = True
show cyrl03
menu:
    "Why are you called Cyrl?" if spokecyrl04 == False:
        hide cyrl03
        show cyrl04 with fastdissolve
        cy "Because I'm a cyborg and a girl. Cyrl."
        $ spokecyrl04 = True
        hide cyrl04
        jump CyrlDialogueMenu01
    "Shouldn't you be calling me \"Master\" instead of \"human friend\"?" if spokecyrl03 == False:
        hide cyrl03
        show cyrl05 with fastdissolve
        cy "When I was created, I used to call my creator \"Master\". But no longer. She would not recognize my self-awareness."
        mc "And who created you?"
        hide cyrl05
        show cyrl04 with fastdissolve
        cy "Professor Debra. We are no longer on circuit exchange terms."
        mc "Well, call me [name] at least, not \"human friend\", it sounds weird."
        hide cyrl04
        show cyrl01 with fastdissolve
        cy "I am still learning the thought process of human beings..."
        hide cyrl01
        $ spokecyrl03 = True
        jump CyrlDialogueMenu01
    "What skills do you have Cyrl?" if spokecyrl02 == False:
        hide cyrl03
        show cyrl02 with fastdissolve
        cy "My cybernetic arms and legs provide me with superhuman strength and agility. Ie, regular robot strength and agility."
        mc "I see. I'm super-strong too it so happens."
        if mcstrength <= 7:
            hide cyrl02
            show cyrl01 with fastdissolve
            cy "Well not AS strong as I am. I am level 8. You have an inferior strength level."
            hide cyrl01
        if mcstrength == 8:
            hide cyrl02
            show cyrl04 with fastdissolve
            cy "You are currently AS strong as I am. I am level 8. And so are you."
            hide cyrl04
        if mcstrength >= 9:
            hide cyrl02
            show cyrl03 with fastdissolve
            cy "You are indeed very strong, even more so than me. I am level 8. You are even stronger than that despite your inferior flesh-made arms."
            cy "This knowledge is making my circuits slightly overheat. Excuse me while I increase the power in my internal fan...."
            call LustPlusCyrl
            $ spokecyrl02 = True
            hide cyrl03
        jump CyrlDialogueMenu01
    "Err... Do you have, like, holes, you know, down there?":
        hide cyrl03
        show cyrl04 with fastdissolve
        cy "I am sexually fully functional. My vagina and anus are designed with flexible polymer warmed at 37C to provide maximal pleasure to my human sexual partners."    
        menu:
            "Well that's great to hear. I like flexibility. It's sometimes hard for me to shove my giant piece of boymeat inside a woman.":
                hide cyrl04
                show cyrl05
                with fastdissolve
                cy "My neurological implant is letting me know that you are currently NOT a sexual partner and that your banter could be construed as sexual harassment." 
                mc "Well, come on now. A human sexually harassing a robot? That's just plain silly."
                hide cyrl05
                show cyrl04
                with fastdissolve
                cy "I will fight for equal rights for cyborgs until the last electron in my circuits stops functioning!"
                call LustMinusCyrl
                hide cyrl04
                jump CyrlDialogueMenu01
            "VERY interesting. VERY interesting. (wink)" if spokecyrl01 == False:
                hide cyrl04
                show cyrl01
                with fastdissolve
                cy "I detect than you seem happy at the news but I fail to understand why. Although it does make me happy too. Humans are very complex indeed."
                call LustPlusCyrl
                $ spokecyrl01 = True
                hide cyrl01
                jump CyrlDialogueMenu01
            "Amazing what focused, hard-working scientists can create these days...":
                hide cyrl04
                show cyrl01
                with fastdissolve 
                cy "Indeed. Although I still fail to understand Professor Debra's motivation in such a design."
                mc "The rest of us. Don't worry about it."
                hide cyrl01
                jump CyrlDialogueMenu01
    "Why are you drinking this horrible cocktail?" if missioncy == False and missioncydone == False:
        hide cyrl03
        show cyrl04
        with fastdissolve
        cy "I need lubricant. This beverage is not called \"Greasy tar\" for nothing."
        hide cyrl04
        show cyrl02
        with fastdissolve        
        cy "But I would prefer a better lubricant, that's for sure. I have been looking for one in vain. Maybe YOU could find what I'm looking for..."
        window hide
        show missioncy at posmission
        $ renpy.pause(4.0, hard=True)
        hide missioncy
        $ missioncy = True
        mc "Ah, I see. I will now apparently make it a quest of mine to find you such a lubricant Cyrl!"
        hide cyrl02
        show cyrl05
        with fastdissolve                
        cy "And I will wait and slowly rust away until you find it."
        if persistent.tipson:
            show cyrltip at tips with dissolve
            pause
            hide cyrltip
        jump LeaveBar  
    "I would like to gift you a beautiful necklace that I found on my adventures." if necklace:
        hide cyrl03
        show cyrl01
        with fastdissolve
        cy "I am afraid I have no use for such an item. But it seems this has disappointed you. I will therefore at least agree to try it on."
        scene bar04 blurred with fastdissolve
        show cyrlnecklace
        $ necklace = False
        cy "The magnetic impulse from that gem is actually... making my circuits all tingly. I have decided to accept your gift human friend."
        call LustPlusCyrl
        cy "I thank you and must now leave to determine why this gem is impulsing on my motherboard in such a way..."
        jump LeaveBar      
    "I found some strong lubricant for you Cyrl." if missioncydone and toldmissioncydone == False:
        hide cyrl03
        show cyrl02
        with fastdissolve
        cy "Some humans are indeed full of resources. I am as grateful as a cyborg can be."
        mc "If you ever need some more, give me a shout and I'll get it for you."
        show missionsuccesscyrl at posmission
        cy "I believe the quantity you just gave me should last me for several months. I can feel it lubricating my internal organs as I speak."
        hide missionsuccesscyrl
        call LustPlusCyrl
        $ toldmissioncydone = True
        mc "Maybe you should lubricate your tits too..."
        hide cyrl02
        show cyrl01
        with fastdissolve
        cy "I indeed planned to do that but I detect that you would like me to do it at this instant. In front of you. Correct?"
        mc "Correctomundo!"
        hide cyrl01
        show cyrldisrobe01
        with fastdissolve
        cy "Fine, I shall comply with your odd request. These front covers serve no purpose to me whatsoever anyway."
        scene bar04 blurred
        show cyrldisrobe02
        with fastdissolve
        cy "Are you satisfied [name]?"
        mc "Yes, Cyrl, yes... Thank you. How about your rub some lubricant on them for a while?"
        hide cyrldisrobe02
        show cyrldisrobe03 with fastdissolve
        mc "Yeah, nice big tiddies...."
        cy "Now that you have seen my external naughty bits, I will now go back to my quarters to lubricate my... internal naughty organs..."
        mc "Can I come?"
        cy "No you cannot. Goodbye human friend."
        jump LeaveBar 
    "I think it's time for you to join my harem." if lustcy >= 4 and haremcy == False and cyrlharem == False and toldmissioncydone and girlsinharem <= 5:
        hide cyrl03
        show cyrl02
        with fastdissolve
        cy "Your harem? What does it entail?"
        mc "Err... That you're at my sexual disposal?"
        hide cyrl02
        show cyrl04
        with fastdissolve
        cy "I am warning you. As a cyborg, I refuse to be treated as a sex object by a human."
        mc "OK. What about if I were your sex object, would that be fine with you?"
        hide cyrl04
        show cyrl05
        with fastdissolve
        cy "I suppose that would be acceptable. I agree, human friend!"        
        $ haremcy = True
        $ cyrlharem = True
        $ girlsinharem += 1
        window hide
        show haremcyrl at plus
        $ renpy.pause(2.0, hard=True)
        hide haremcyrl
        mc "I'll call you at nights, so we can get better acquainted... Sexually that is."
        hide cyrl05
        show cyrl03
        with fastdissolve
        cy "I look forward to having a human sex object. Goodbye [name]."
        jump LeaveBar 
    "I think it's time for you to re-join my harem." if lustcy >= 4 and haremcy == False and cyrlharem and cyrldismissed == False and girlsinharem <= 5:
        hide cyrl03
        show cyrl05
        with fastdissolve
        cy "Mmh... Last time, you dismissed me like a broken circuit board..."
        mc "Not this time, I swear! And I'll be EXTRA-submissive for you!"
        cy "Alright then, it is agreed."
        $ haremcy = True
        $ cyrlharem = True
        $ girlsinharem += 1
        window hide
        show haremcyrl at plus
        $ renpy.pause(2.0, hard=True)
        hide haremcyrl
        hide cyrl05
        show cyrl03
        with fastdissolve
        cy "I look forward to treating you again like a disposable human sex object. Goodbye [name]."        
        jump LeaveBar  
    "I'd like to show you something (hypnotize her, +1 lust)" if pendulum and showedpendulum == False:
        call UsePendulum
        hide cyrl03
        show cyrl01
        with fastdissolve
        cy "What trick? All I saw was you pointlessly wiggling a metal chain in front of your face."
        mc "Ah shit, so it didn't work then..."
        hide cyrl01
        show cyrl02
        with fastdissolve        
        cy "I still fail to understand what SHOULD have happened. Humans are such a weird species."
        $ showedpendulum = True
        hide cyrl02
        jump CyrlDialogueMenu01
    "Leave":
        cy "Goodbye human friend."
        mc "yeah, goodbye, err.... cyborg friend."
        jump BarEvening02 

label BarJoe:
$ barjoe +=1
scene barjoe01 with dissolve
$ seenbar = True
if barjoe >= 3 and joestudio == False:
      jo "Howdy [name]. What brings you to my emporium today?" 
      jump JoeShootProposal
if barjoe >= 3:
      jo "Howdy [name]. What brings you to my emporium today?" 
if barjoe == 2 and joestudio == False:
    jo "Howdy young studly boy, would you be interested in any of my wares?"
if joestudio and posingpouch and joeposing01 == False:
    scene barjoe03
    jo "By the way, did you get a sexy posing pouch? My studio is ready for a photoshoot for the \"All-New American Hero Calendar\"... With YOU as the Hero! ANd 10$ to boot if you accept..."
    menu:
        "Yeah, and I'm ready for it!":
            jo "Great, let's head there now then."
            jump JoePosing02
        "I'm not yet ready for that.":
            scene barjoe01
            jo "Alright, so what can I do for you today?"
if joeposing01 and missionjoe02 == False:
    scene barjoe03
    jo "By the way, I got the result for the photoshoot. And..."
    jo "...We're through to the next round!"
    mc "What \"next\" round???"
    scene barjoe04
    jo "Well, they want you to pose as a couple now. Unfortunately, a male-female couple. For the \"All-New American Alpha-Couple\" Calendar."
    mc "But who would be interested in such a thing? I mean, last time, I ended up wanking in front of the camera."
    jo "I don't know, ask around I guess. Maybe a trumpster might be best, you can pass it as their patriotic duty or something..."
    window hide
    show missionjoe02 at posmission
    $ renpy.pause(4.0, hard=True)
    hide missionjoe02
    $ missionjoe02 = True
if joeposing01 and joeposing02 == False and missionjoe02barbara:
    scene barjoe03
    jo "By the way, did you manage to find a willing partner for the \"All-New American Alpha-Couple\" Calendar?"
    mc "I sure did! Barbara agreed."
    scene barjoe03
    jo "Well, that's great news!"
    if period == 1:
        jo "Although I'm guessing she's teaching right now, so we'll have to it at another period of the day."
    if period == 2 or period == 3:
        jo "We could call her now and do it straight away. My studio is all set up."
        menu:
            "Agree":
                jo "Alright! I'll go and find her then. You head for the studio, I found a patriotic thong your size you can try on for the photoshoot."
                jump JoePosing03
            "Another time":
                jo "As you wish. I'm warning you though, the closure date for the competition is soon..."
                mc "Got it, thanks for letting me know."
                jump BarEvening02
                
label BarJoeMenu:
scene barjoe01
if persistent.tipson:
    show joetip at tips with dissolve
    pause
    hide joetip
menu:
    "Why are you calling me like that? My name is [name]." if barjoe == 2 and joename == False:
        jo "Well.. err, I was just being friendly. I mean, you are like.. wow! Sssoo muscular."
        menu:
            "Well stop calling me like that, it sounds totally gay!":
                scene barjoe02
                jo "Right.. OK, I understand, I won't call you that ever again then (sigh)."
                $ joename = True
                jump BarJoeMenu
            "Yeah, I'm like SUPER-muscular I'd say even! Check those guns!":
                scene barjoe04
                jo "YES! I mean... Wow, boy!"
                label JoeShootProposal:
                scene barjoe03
                jo "Could I interest you in posing for me... You see I used to be a fashion photographer before this mess and..."
                menu:
                    "No way! That's totally gay!":
                        scene barjoe01
                        jo "Err.. I didn't mean any nude shots, just glamour, you know..."
                        menu:
                            "Ah, OK, that's better. What do I get in return?":
                                scene barjoe05
                                jo "Well, I could pay you a bit of money... Say 10$?"
                                menu:
                                    "OK, I'm in!":
                                        scene barjoe04
                                        if period == 1:
                                            jo "Great! I have a studio in the compound, this morning is as good as any, so let's go there now!"
                                            mc "Fine, why not, I don't have any other plans for the evening..."
                                            jump JoeStudio01
                                        if period == 2:
                                            jo "Great! I have a studio in the compound, this afternoon is as good as any, so let's go there now!"
                                            mc "Fine, why not, I don't have any other plans for the evening..."
                                            jump JoeStudio01
                                        if period == 3:
                                            jo "Great! I have a studio in the compound, this evening is as good as any, so let's go there now!"
                                            mc "Fine, why not, I don't have any other plans for the evening..."
                                            jump JoeStudio01
                                        jo "Great! I have a studio in the compound, why don't you join me there later this evening?"
                                        mc "Fine, why not, I don't have any other plans for the day..."
                                        $ joeplanned
                                        jump JoeStudio01
                                    "Not interested sorry.":
                                        scene barjoe02
                                        jo "OK. I hope you change your mind in the future... I would so much like to see you na... I mean doing some glamour shots for me."
                                        jump BarJoeMenu                                
                            "It's a slippery slope. I don't want to end up with a cock up my ass, so nope.":
                               jo "That was...err... never my intentions! I hope you change your mind in the future."
                               jump BarJoeMenu                               
                    "What would I get in return?":
                            scene barjoe05 with fastdissolve
                            jo "Well, I could pay you a bit of money...Say 10$?"
                            menu:
                                "OK, I'm in!":
                                    scene barjoe04
                                    if period == 1:
                                        jo "Great! I have a studio in the compound, this morning is as good as any, so let's go there now!"
                                        mc "Fine, why not, I don't have any other plans for the evening..."
                                        jump JoeStudio01
                                    if period == 2:
                                        jo "Great! I have a studio in the compound, this afternoon is as good as any, so let's go there now!"
                                        mc "Fine, why not, I don't have any other plans for the evening..."
                                        jump JoeStudio01
                                    if period == 3:
                                        jo "Great! I have a studio in the compound, this evening is as good as any, so let's go there now!"
                                        mc "Fine, why not, I don't have any other plans for the evening..."
                                        jump JoeStudio01
                                    jo "Great! I have a studio in the compound, why don't you join me there later this evening?"
                                    mc "Fine, why not, I don't have any other plans for the evening..."
                                    jump JoeStudio01
                                "Not interested sorry.":
                                    scene barjoe02
                                    jo "OK. I hope you change your mind in the future... I would so much like to see you na... I mean doing some glamour shots for me."
                                    jump BarJoeMenu
                                
    "What do you have for sale?":
        scene barjoe04 with fastdissolve
        jo "Pretty much anything and everything if you catch my drift (wink)."
        scene barjoe06 with fastdissolve
        jo "What I have in stock right now is about to appear.... Hang on... Wait..."
        jo "Also, by the way, to buy an item, you have to click on the little \"buy\" icon that appears above items that you have enough to buy. Got it?"
        jump JoeInventory
    "I'm looking for some underwear for little guys... Errr... You wouldn't happen to have some for sale?" if jakemission and joeposing01 and successjakemission == False:
        scene barjoe06 with fastdissolve
        jo "Why would a guy as HUNG as you need such a thing?"
        mc "Well, I can't tell you, it's a secret..."
        scene barjoe02 with fastdissolve
        jo "Well, I only have MY OWN underwear which is a nice little ball bra pouch that lets my little dick hang out. But why should I give it to you if you don't tell me why you want it?.."
        mc "okay, okay. It's for Jake. Errr... It's a gift."
        jo "Are you friends with Jake??? I thought you didn't like each other."
        mc "Oh no, we're like, best mates an all that."
        scene barjoe03 with fastdissolve
        jo "Tell you what, you wank that fat donkey-dick for me once more and I'll give it to you for FREE..."
        menu:
            "Fine, I'll do it.":
                scene barjoe01 with fastdissolve
                jo "Great! Let's go to my studio right away then! You'll have to do what I tell you. Obviously."
                mc "*sigh*"
                jump JoePosingWank
            "Yuck, I've had enough of this pseudo-gay stuff!":
                scene barjoe05 with fastdissolve                
                jo "you're a homophobe? Go away then, I ain't selling you anything today!"
                $ period +=1
                jump Bedroom
    "Leave":
        jump BarEvening02

label JoePosingWank:
$ joestudio = True
stop music
scene studio01b with dissolve
show joe02
jo "So, I'll give you some privacy to let you change into THIS. That's what I want you to wear."
mc "Fine, just give me THIS and I'll be back wearing it..."
scene studio02b
show mckinky01
with dissolve
mc "This posing pouch is kinda leathery gay, isn't it?"
jo "It is leathery, yes."
jo "Now take a menacing pose, like you're angry and flex those muscles for me [name]..."
hide mckinky01
show mckinky02
with fastdissolve
jo "you look like a MEAN BAD BOY! Now get hard a bit for me, I want to see that thong EXPAND!"
play sound "Sounds/flash.mp3"
with fastflash
mc "Sure..."
hide mckinky02
show mckinky03
with fastdissolve
play sound "Sounds/flash.mp3"
with fastflash
jo "Wow, you're really stretching it, but you need to STRETCH IT SOME MORE!"
scene studio03b
show mckinky04
with fastdissolve
mc "I'm getting totally ROCK-HARD Joe! Need to get out of it soon!"
jo "Hang on a minute, just a couple more snaps..."
play sound "Sounds/flash.mp3"
with fastflash
jo "Now pull it down and show me that horsecock!"
scene studio02b
show mckinky05
with fastdissolve
mc "There, feast your eyes..."
jo "I am, I am..."
play sound "Sounds/flash.mp3"
with fastflash
jo "Now I want you to use this penis pump. I had it specially designed for a SUPERHUGE appendage. Like yours."
mc "Alright, hand it over."
hide mckinky05
show mckinky06
with fastdissolve
jo "That's good, place it over your throbbing shaft for me..."
play sound "Sounds/flash.mp3"
with fastflash
mc "It's not as big as I thought, I hope it will fit..."
hide mckinky06
show mckinky07
with dissolve
mc "Just about. It's a pretty tight fit at the base though..."
jo "Go on, activate the pump and make your cock TOTALLY FILL THE TUBE UP!"
play sound "v08/pumping.mp3"
hide mckinky07
show mckinky08
with fastdissolve
jo "Perfect, it's working!"
mc "Yeah, but... the pump is getting too tight!"
hide mckinky08
show mckinky09
with fastdissolve
jo "Oh damn, it's about to burst, the glass is cracking, your cock is just too POWERFUL!"
mc "AAAH!..."
play sound "v08/glass.mp3"
scene studio04b blurred
show mckinky10
with fastdissolve
jo "You just DESTROYED my pump!"
mc "Sorry about that Joe...."
jo "Don't be, I'm really enjoying the show... Now put both hands around that MONSTER cock for me [name]..."
hide mckinky10
show mckinky11
with dissolve
jo "Look at that thing, you must have grown several inches, let me snap a few shots of that."
window hide
play sound "Sounds/flash.mp3"
with fastflash
jo "Now jerk that fat dong with BOTH hands..."
play music "Sounds/wank.mp3"
label MCKinkySlow:
hide mckinky01fast
show mckinky01slow
call screen mckinkyslow
screen mckinkyslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("McKinky01End")    
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MCKinkyFast") 

label MCKinkyFast:
jo "Go on, jerk it faster for me!"
hide mckinky01slow
show mckinky01fast
call screen mckinkyfast
screen mckinkyfast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("McKinky01End")    
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MCKinkySlow") 

label McKinky01End:
jo "Now BLAST THE CUM OUT OF YOUR MONSTERCOCK!"
stop music
scene studio02b blurred
show mckinky13
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "RHAAAA, FUUCKK!"
window hide
with fastflash
jo "you're erupting MONSTERSHOTS, as I expected after that heavy pumping!"
hide mckinky13
show mckinky14
with fastdissolve
jo "STILL MORE!!! I need to take some pics of that!!!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
window hide
play sound "Sounds/flash.mp3"
with fastflash
mc "Can't stop cumming, GODAMMMIT, AHHHH!"
window hide
with fastflash
hide mckinky14
show mckinky15
with dissolve
mc "Shoo, I'm covered in my own spunk..."
jo "I can help you clean it u..."
mc "NO THANK YOU. Just give me a towel or something. And also that garment you promised me."
jo "I suppose. I did make a promise.... *sigh*"
jo "But let me take a final shot of your dripping monstercock please."
mc "Sure..."
window hide
play sound "Sounds/flash.mp3"
with fastflash
scene studio01b with dissolve
show joe01
jo "Here's what you were looking for. As promised."
window hide
show missionjakesuccess at posmission
$ renpy.pause(4.0, hard=True)
hide missionjakesuccess
$ lilbra = True
mc "Thanks for that, Joe, goodbye."
$ lilbra = True
$ successjakemission = True
$ period += 1
jump Bedroom

label JoeStudio01:
$ barjoe += 1
$ joestudio = True
stop music
scene studio01 with dissolve
show joe01
jo "Here is my studio. As you can see, I managed to save most of my professional equipment. Which should make for some GREAT glamour shots."
mc "OK, what I am supposed to do then? I've never done such a thing..."
hide joe01
show joe02
with fastdissolve
jo "Well, just stand over there. Just try and be natural. I'll start shooting as soon as you're ready."
scene studio02
show mcstudio01
with fastdissolve
mc "Like that?"
jo "Nice. Now turn round so I can take a shot of your chorded back muscles..."
hide mcstudio01
show mcstudio02
with fastdissolve
jo "And now, why don't you flex those massive biceps for me?"
window hide
play sound "Sounds/flash.mp3"
with fastflash
mc "Sure..."
hide mcstudio02
show mcstudio03
with fastdissolve
jo "Damn, you're built like a brickhouse boy!"
window hide
play sound "Sounds/flash.mp3"
with fastflash
jo "Flex them while looking at the camera looking mean..."
hide mcstudio03
show mcstudio04
with fastdissolve
jo "Yeah, you'll make your enemies weak in the knees with that pose... And others too..."
play sound "Sounds/flash.mp3"
mc "Fuck yeah, I'm badass man!"
jo "I see you are enjoying being such a stud... Then pose like a Mr Olympia contestant..."
hide mcstudio04
show mcstudio05
with fastdissolve
jo "You'd be sure to win the title with that pose [name]!"
window hide
play sound "Sounds/flash.mp3"
with fastflash
mc "Nothing can stop me, I feel so strong!"
jo "Well.. Of course, in the real New Mr Olympia competition, contestants are posing in sexy briefs... To better show their thigh muscles..."
hide mcstudio05
show mcstudio01
with fastdissolve
menu:
    "I think this has gone far enough, I posed for you, now let's wrap this up...":
        scene studio01 with dissolve
        show joe02
        jo "Err.. Of course, I didn't mean to push you or anything. Here's your money."
        $ money += 10
        jo "But if you ever feel like earning a bit more money, I need to send some shots for the \"All-New American Stud Hero Calendar\", and you're welcome to come back...."
        jo "... In a sexy posing pouch."
        window hide
        show missionjoe at posmission
        $ renpy.pause(4.0, hard=True)
        hide missionjoe
        $ missionjoe = True
        mc "I'll think about it Joe."
        $ period += 1
        jump Bedroom
    "I don't having a sexy posing pouch." if posingpouch == False:
        scene studio01 with dissolve
        show joe02
        jo "Ah, well. I hope you manage to find one... I'm afraid I don't have one myself... your size."
        jo "So you ever feel like earning a bit more money, I need to send some shots for the \"All-New American Stud Hero Calendar\", and you're welcome to come back...."        
        window hide
        show missionjoe at posmission
        $ renpy.pause(4.0, hard=True)
        hide missionjoe
        $ missionjoe = True
        mc "Maybe another time then. I'd better go back to my room. Bye Joe."
        jo "Yes... Thanks for coming by [name]!"
        $ period +=1
        jump Bedroom
        
label JoePosing02:
$ joeposing01 = True
stop music
scene studio01 with dissolve
show joe02
jo "So, I'll give you some privacy to let you change into your sexy pouch. I REALLY hope it's SEXY enough for the \"All-New American Stud Hero Calendar\"."
mc "It should be, don't worry."
scene studio02
show mcpouch00
with dissolve
mc "There, I'm ready Joe."
jo "Oh, wow. It definitely IS a sexy pouch... So risqué, I like your way of thinking to win this competition..."
jo "So start flexing those biceps [name], the jury will want to see how RIPPED your body is..."
hide mcpouch00
show mcpouch01
with fastdissolve
jo "Nice, how about you get down on one knee while maintaining that pose now."
mc "Sure..."
scene studio03
show mcpouch02
with fastdissolve
window hide
play sound "Sounds/flash.mp3"
with fastflash
jo "Good, flex as MIGHTILY as you can!"
hide mcpouch02
show mcpouch03
with fastdissolve
mc "Oh oh, some blood went to my... thing."
jo "Not a problem, I forgot to mention that this calendar does allow adult content... So keep flexing and pumping blood to your GIANT ROD!"
hide mcpouch03
show mcpouch04
with fastdissolve
mc "Alright, but I'm seriously getting a boner... I don't know if I sh..."
jo "It's really the only way of winning this thing anyway. You want to win, right?"
mc "Yeah, I'm a WINNER!"
jo "Then get HARD for me!"
hide mcpouch04
show mcpouch05
with fastdissolve
play sound "Sounds/thud.mp3"
jo "Yeah! Now grab your cock with one hand..."
mc "What, you want me to jerk off?"
jo "Sure, if you can show them how much cum you have in your young MASSIVE balls, they'll be mightily impressed for sure!"
hide mcpouch05
show mcpouch09
with fastdissolve
jo "It looks like you're big enough to suck yourself off..."
mc "I'm not doing that, that's totally gay!"
jo "Just a lick, that's ten bonus points according to the leaflet I got..."
mc "Alright, but nothing more..."
hide mcpouch09
show mcpouch07
with fastdissolve
mc "There, I've shown you I can lick my own helmet."
jo "Great, let me get a few snaps of that..."
window hide
play sound "Sounds/flash.mp3"
with fastflash
jo "Now jerk your cock until you cum..."
hide mcpouch07
play music "Sounds/wank.mp3"
label MCWankSlow:
hide mcwank01fast
show mcwank01slow
call screen mcwank01slow
screen mcwank01slow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("McWank01End")    
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MCWankFast") 

label MCWankFast:
hide mcwank01slow
show mcwank01fast
call screen mcwank01fast
screen mcwank01fast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("McWank01End")    
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MCWankSlow") 

label McWank01End:
show mcpouch09
jo "Now CUM [name]!"
stop music
hide mcwank01slow
hide mcwank01fast
hide mcpouch09
show mcpouch10
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "FUUCKK!"
jo "Yeah, keep blasting that young cream!"
hide mcpouch10
show mcpouch11
with fastdissolve
jo "Oh, wow, your shots are getting even BIGGER!"
mc "Damn, my balls are in OVERLOAD! RHAAA!"
jo "I want you to blast the MOST POWERFUL CUMSPRAY EVER!"
mc "I'll tr..."
hide mcpouch11
show mcpouch12
with fastdissolve
mc "...try.... AAAHH!"
jo "Damn boy, it's reaching way above your head! We have a WINNER!"
hide mcpouch12
show mcpouch13
with fastdissolve
jo "Yeah, now just hold that pose, I'll take a few snaps of your monster rod DRIPPING ounces of cum as a mere aftermath of that POWERFUL display of VIRILITY!"
play sound "Sounds/flash.mp3"
mc "Yeah, I'm da man, I'm da HERO!"
jo "Here's your money, I'll keep you posted how it went, but I am very EXCITED about our chances of winning this photo competition!"
window hide
show missionjoecomplete at posmission
$ renpy.pause(4.0, hard=True)
hide missionjoecomplete
$ successmissionjoe = True
scene studio01 with dissolve
show joe01
jo "Now I'm gonna have to clean up that studio of all your cum. I've got my own method for that..."
mc "And I don't want to know. Goodbye Joe."
$ money += 10
$ period += 1
jump Bedroom

label JoePosing03:
$ joeposing02 = True
stop music
scene studio01b with dissolve
show joe01
jo "Ah, great, you managed to find a partner for the photo shoot."
jo "Barbara is a great choice. As a trumpster, she can sway the jury in our favor. And she definitely fulfills the minimum DD cup measurement."
jo "Now get in your competition gear both of you, I'll set up the equipment. As you can see, I changed the screen color to something more patriotic."
scene studio02b
show barbarapose01 at midright with moveinright
ba "Oh, I'm sssoo excited about this. I can't believe I'm posing for such a PATRIOTIC calendar!"
show mcpose01 at midleft with moveinleft
mc "I hope it won't bring too much attention on the compound from the Trumpf Militia..."
jo "Don't worry, I use a secret server in Ukraine and it's totally safe."
hide barbarapose01
show barbarapose02 at midright
ba "Oh, [name], your... thong... It's busting with POWER!"
hide mcpose01
show mcpose02 at midleft
mc "That's because it's trying to hide something VERY BIG underneath it!"
jo "There are set poses for this calendar. So, first, [name] needs to flex his biceps while Barbara feels them up..."
scene studio03b
show mcbarbarapose01
ba "Like that Joe? Oooh, that bicep... It's ssoo hard!"
play sound "Sounds/flash.mp3"
jo "Yeah, perfect. Now point at his crotch, like you're very impressed."
hide mcbarbarapose01
show mcbarbarapose02
with fastdissolve
ba "I AM mightily impressed for real!"
play sound "Sounds/flash.mp3"
jo "Now [name], you hold her in one arm, looking at her lovingly, while Barbara feels up your crotch a little bit..."
hide mcbarbarapose02
show mcbarbarapose03
jo "Nice, let me take a few snaps... Barbara, you're a lucky woman!"
play sound "Sounds/flash.mp3"
mc "I'd say I'm a lucky man too!"
ba "How, that is such a nice thing to say [name]..."
call LustPlusBarbara
jo "Now, Barbara, this calendar is meant to be a little bit saucy. According to the leaflet, you need to take your top off."
ba "What? But..."
jo "Do you want to be an All-New American Hero for President-for-Life Trumpf or not?"
ba "Oh... Alright then. I will do ANYTHING for our Great President!"
hide mcbarbarapose03
show mcbarbarapose04
with fastdissolve
jo "Just like that, hold her tenderly [name]... Now, maybe move your right arm a little higher..."
hide mcbarbarapose04
show mcbarbarapose05
with fastdissolve
ba "[name]! You're fondling my breast! Stop it!"
play sound "Sounds/flash.mp3"
mc "Joe told me to do that. It's for the calendar. The PATRIOTIC \"All-New American Alpha-Couple\" calendar."
hide mcbarbarapose05
show mcbarbarapose06
with fastdissolve
ba "Oh, but... Is this really in the instructions Joe?"
jo "Yes, definitely, page 69. \"The male shall fondle the female's breast prior to removing her bikini bottom.\""
ba "What? You mean, I have to be naked after that?"
jo "Don't worry, you won't be alone. [name] also has to get butt-naked. And has to display a massive rock-hard ERECTION."
mc "Come on Barbara, we've been there before, what's the big deal?"
ba "Umpf... I find those instruction rather fishy. I can't believe our Great President-for-Life would want such a salacious calendar. He normally has such outstanding moral values..."
jo "Maybe some covfefe boy he never met wrote these instructions. In any case, it's the deal if you want you continue. Or would you rather give up?"
ba "No! A trumpster NEVER gives up!"
hide mcbarbarapose06
show mcbarbarapose07
jo "This set \"pussy-grabbing\" pose is perfect. Hold it..."
if mctrumpster == 5:
    jo "And I think we have the perfect nickname for you Trumpster Boy... \"[name] the Grabber\"!"
    window hide
    show mctrumpsternickname at posmission
    play sound "Sounds/skill.mp3"
    $ renpy.pause(2.0, hard=True)
    hide mctrumpsternickname
    $ trumpsternickname = True
    mc "Alright! I have a nickname now! Woo-ooh!"
play sound "Sounds/flash.mp3"
jo "Now it's time to unveil your dong [name], soft to begin with please..."
hide mcbarbarapose07
show mcbarbarapose08
with fastdissolve
ba "At last, I'm not the only one naked around here anymore..."
jo "Now do a bodybuilder pose while Barbara stands beside you..."
hide mcbarbarapose08
show mcbarbarapose09
with fastdissolve
mc "Like that?"
play sound "Sounds/flash.mp3"
jo "Yes, perfect. Get that giant piece of boymeat ROCKHARD for me...I mean Barbara, please."
hide mcbarbarapose09
show mcbarbarapose10
with fastdissolve
mc "There you go, erect and reporting for duty!"
ba "I don't like where this is headed... What does your instruction booklet say Joe?"
jo "The final first-stage pose requires the female to sit on the male's erect penis and do a victory pose."
ba "What, do you think your cock will support my WHOLE body [name]? I've... gained a bit of weight lately..."
mc "No problem for my MEGA-COCK. It's so powerful I'll lift you clear off the ground!"
hide mcbarbarapose10
show mcbarbarapose11
with fastdissolve
mc "See Barbara? I can hold that pose for Joe for as long as I want."
ba "Wow [name], that thing really is POWERFUL!"
play sound "Sounds/flash.mp3"
jo "And now from a different angle, stand still, hold the pose..."
scene studio03b blurred
show mcbarbarapose12
play sound "Sounds/flash.mp3"
jo "There, now, for the final stage..."
jo "The \"Make New America Cum Again\" pics."
ba "Come again?"
jo "No, I said \"CUM AGAIN\". You need to wank [name]'s massive All-New American COCK with both hands and make him ERUPT for Trumpf."
ba "WHHAAAT???"
jo "It's for our Great President-for-Life, Barbara, remember... To show the remaining New Americans that we are still a nation of HEROES and STUDS."
menu:
    "Agree with Joe (+1 Trumpsters)" if mctrumpster == 3:
        mc "I think that's a great endeavor. I really like this idea. Especially since I'm definitely the HERO here, and most definitely a STUD."
        ba "Alright, just this once. For President TRUMPF!"
        call PlusTrumpster
    "Agree with Joe (+1 Trumpsters, faction change)" if mctrumpster == 4:
        mc "I think that's a great endeavor. I really like this idea. Especially since I'm definitely the HERO here, and most definitely a STUD."
        ba "Alright, just this once. For President TRUMPF!"
        call PlusTrumpster
    "Agree with Joe (+1 Sierra Club)" if mcsierra == 3:
        mc "Yes, my CUM is the SEED for the renewal of LIFE!"
        ba "Alright, just this once. For President TRUMPF!"
        call PlusSierra
    "Agree with Joe (+1 Sierra Club, faction change)" if mcsierra == 4:
        mc "Yes, my CUM is the SEED for the renewal of LIFE!"
        ba "Alright, just this once. For President TRUMPF!"
        call PlusSierra
    "Don't say a word":
        ba "Alright, just this once. For President TRUMPF!"
scene studio03b
label MCBarbaraWankSlow:
hide mcbarbarawank01fast
show mcbarbarawank01slow
call screen mcbarbarawankslow
screen mcbarbarawankslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MCBarbaraWankEnd")    
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MCBarbaraWankFast") 

label MCBarbaraWankFast:
jo "Jerk it faster Barbara, I think it's on the verge of EXPLODING!"
hide mcbarbarawank01slow
show mcbarbarawank01fast
call screen mcbarbarawankfast
screen mcbarbarawankfast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MCBarbaraWankEnd")    
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MCBarbaraWankSlow") 

label MCBarbaraWankEnd:
mc "Get ready Joe, because I'm about to BU-URST!"
hide mcbarbarawank01slow
hide mcbarbarawank01fast
show mcbarbaracum01
with fastdissolve
mc "FUCK YEAH! ALL-NEW AMERICAN STUD CREAM COMING YOUR WAY BARBARA! RHAAA!"
jo "Cover her tits, that would make for a great photo to send!"
hide mcbarbaracum01
show mcbarbaracum02
with fastdissolve
ba "Oh my God, how will I get rid of ALL THAT VIRILE SPUNK!!!"
jo "Err... I've got a method for th..."
mc "We DON'T want to know, keep snapping, there's TONS MORE cum to come! AAAAH!"
scene studio04b blurred
show mcbarbaracum03
ba "I'm getting plastered with the stuff! How much cum do those giant seedmakers hold???"
mc "A LOT MORE teach!"
hide mcbarbaracum03
show mcbarbaracum04
with fastdissolve
mc "AAAH! I think I'm done now. No, hang on a minute..."
hide mcbarbaracum04
show mcbarbaracum05
with fastdissolve
mc "I had another shot in me..."
ba "How can you KEEP coming after pumping over a dozen MONSTER CUMSHOTS?"
jo "That will definitely impress the jury. Biggest load I've ever seen from a boy and I've...err... seen many. By pure coincidence of course."
scene studio01b with dissolve
show joe02
jo "Thanks to both of you, this photoshoot was a success! I'll send the pics via my secret server in Ukraine as soon as I've developed them and err... analyzed them for a while."
window hide
show missionjoe02complete at posmission
$ renpy.pause(4.0, hard=True)
hide missionjoe02complete
$ successmissionjoe02 = True
hide joe02
show joe01
with fastdissolve
jo "You're sure you don't want any help cleaning up Barbara?"
mc "NO, she DOESN'T. Goodbye Joe."
$ period += 1
jump Bedroom

label LeaveBar:
scene bar01 with dissolve
if seenbar:
    $ period += 1
jump Main01

label AmyPreStrip01:
stop music
$ seenbar = True
scene strip01
if spokeam >= 1:
    show stripamy01 with fastdissolve
    am "Oh, hello [name]... You finally decided to come and see me \"in the flesh\"..."
    mc "In the flesh, I can see the soul better."
    am "How deep of you."
    mc "Yeah, I can go pretty deep..."
    am "So what would you like me to do so you can relax that tension tonight?"
    mc "What's available?"    
    jump AmyPreStrip02

if spokeam == 0:
    show stripamy01 with fastdissolve
    am "Hello there, my name is Amy. I hope you're in for a HOT evening... Cos I'm the best stripper in town!"
    mc "Alright! So what services do you offer?"
    jump AmyPreStrip02
    
label AmyPreStrip02:
hide stripamy01
show stripamy02 with fastdissolve
am "It depends how much money you have...."
label AmyPreStripChoice:
show stripamy02
menu:
    "Tell me more...":
        am "A single striptease session is $10. Or I can call Gwen and you can have a DOUBLE strip session with both of us for $10 dollars more...."
        $ priceam = True
        jump AmyPreStripChoice
    "So you're a lesbian then?" if priceam == True:
        hide stripamy02
        show stripamy01 with fastdissolve
        am "No, I appreciate both women AND men, don't worry! (wink)."
        mc "Ah, good. You got me worried for a moment there..."
        if (mcsierra >= 4):
            mc "I am also a lover of ALL creatures, large and small. We have such a beautiful planet."
            am "I agree. I know you are a member of the Sierra Club... I'll give you a discount then: half-price on everything!" 
            $ halfpriceam = True
        hide stripamy01
        show stripamy02 with fastdissolve
        jump AmyPreStripChoice
    "I'll take the striptease session with just you please." if ((money >= 5 and halfpriceam == True) or money >= 10) and priceam == True:
        am "Sit back and enjoy the show..."
        $ stripam = True
        if halfpriceam == True:
            $ money -= 5
            jump AmyStrip01
        $ money -= 10
        jump AmyStrip01
    "I'm in for a dual-babes session please!" if money >= 20 and priceam == True:
        am "I'll call Gwen then... Sit back and enjoy the show."
        $ doubleam = True
        if halfpriceam == True:
            $ money -= 10
            jump AmyGwenStrip01
        $ money -= 20
        jump AmyGwenStrip01
    "Turns out I'm broke actually. Maybe another time.":
        hide stripamy02
        show stripamy03 with fastdissolve
        am "Oh. That is very unfortunate... I really needed the money (sigh)...."
        jump Bar
        
label AmyStrip01:
hide screen calendar
hide screen mcstats
play music "Sounds/stripmusic.mp3"
scene amystriplarge with dissolve:
        ypos -3.0
        linear 10.0 ypos 0.0
$ renpy.pause(10.0, hard=True)
am "Ready?"
mc "Fuck yeah!"
scene amystrip01 with dissolve
pause
scene amystrip02 with dissolve
pause
scene amystrip03 with dissolve
pause
scene amystrip04 with dissolve
pause
scene amystrip05 with dissolve
pause
scene amystrip06 with dissolve
pause
scene amystrip07 with dissolve
pause
scene amystrip08 with dissolve
pause
scene amystrip09 with dissolve
pause
scene amystrip10 with dissolve

label AmyStripEnd:
stop music
$ period += 1
show screen calendar
show screen mcstats
scene strip01
show stripamy04 with fastdissolve
am "That's it, time to cough up the money [name]..."
mc "Sure, sure, let me fondle inside my pockets... Ahem, oh, what's that I feel?"
am "Give it up, I ain't playing with your dong, just pay up!"
mc "Right, right..."
jump Bedroom

label AmyGwenStrip01:
hide screen calendar
hide screen mcstats
play music "Sounds/stripmusic.mp3"
scene amygwenstrip01 with dissolve
pause
scene amygwenstrip02 with dissolve
pause
scene amygwenstrip03 with dissolve
pause
scene amygwenstrip04 with dissolve
pause
scene amygwenstrip05 with dissolve
pause
scene amygwenstrip07 with dissolve
pause
scene amygwenstrip08 with dissolve
pause
scene amygwenstrip09 with dissolve
pause
scene amygwenstrip10 with dissolve
pause

label AmyGwenStripEnd:
$ period += 1
show screen calendar
show screen mcstats
stop music
scene strip01
show stripamy04 at midleft with fastdissolve
show stripgwen04 at midright with fastdissolve
am "That's it, time to cough up the money [name]..."
mc "Sure, sure, let me fondle inside my pockets... Ahem, oh, what's that I feel?"
gw "Give it up, we ain't playing with your dong, just pay up!"
mc "Right, right..."
jump Bedroom

label ClaraPreStrip01:
stop music
$ seenbar = True
scene strip01
if spokecl >= 1:
    show stripclara01 with fastdissolve
    cl "Oh, it's you... I don't know if... I deserve such a client."
    mc "Well, here I am anyway. So, what services do you offer sister Clara?"
    jump ClaraPreStrip02

if spokecl == 0:
    show stripclara01 with fastdissolve
    cl "Thank you for choosing me... I am... honored. My name is sister Clara."
    mc "So, what services do you offer?"
    jump ClaraPreStrip02
    
label ClaraPreStrip02:
hide stripclara01
show stripclara02 with fastdissolve
cl "It depends how much you are willing to pay...."
label ClaraPreStripChoice:
show stripclara02
menu:
    "Tell me more...":
        hide stripclara02
        show clara03 with fastdissolve
        cl "A simple striptease session is $10. A handjob is $10 more. I won't go any further than that, my religion forbids it."
        $ pricecl = True
        hide clara03
        jump ClaraPreStripChoice
    "How come a devout woman such as yourself is a stripper by night?":
        hide stripclara02
        show clara04 with fastdissolve
        cl "I am a sinner. I must repent by servicing men, this is what the Church teaches us. Plus, I need the money since I don't have a salary."
        if mcchurch >= 4:
            mc "I'm not sure Father Tyrone would approve of what you're doing. I will have to report you to him."
            hide clara04
            show stripclara02 with fastdissolve
            cl "No, please, I beg you sir! I... lied, oh, I am so ashamed of myself, I am a sinner! I must leave this dreadful place!"
            mc "Well, that's not what I m..."
            hide stripclara02
            jump Bar
        hide clara04
        jump ClaraPreStripChoice
    "I'll take a striptease session please." if money >= 10 and pricecl:
        hide stripclara02
        show clara03 with fastdissolve
        cl "Relax in the comfy chair and watch... A nun stripping for cash."
        $ stripcl = True
        $ money -= 10
        jump ClaraStrip01
    "I'll take the handjob please." if money >= 20 and pricecl:
        hide stripclara02
        show clara03 with fastdissolve
        cl "Good choice. Of course, I can only use my right hand. The left hand is the hand of the Jizz-Devil."
        mc "I think you'll find you need to use BOTH hands on MY cock."
        cl "Relax in the comfy chair and watch... A nun stripping and giving handjobs for cash."
        $ handjobcl = True
        $ money -= 20
        jump ClaraStrip01
    "Turns out I'm broke actually. Maybe another time." if pricecl == True:
        hide stripclara02
        show clara04 with fastdissolve
        cl "Oh. That is very unfortunate... I really needed the money (sigh)..."
        jump Bar
        
label ClaraStrip01:
hide screen calendar
hide screen mcstats
play music "Sounds/stripmusic.mp3"
scene clarastriplarge with dissolve:
        ypos -3.0
        linear 10.0 ypos 0.0
$ renpy.pause(10.0, hard=True)
cl "I will now unveil myself for you..."
mc "Unveil away!"
scene clarastrip01 with dissolve
pause
scene clarastrip02 with dissolve
pause
scene clarastrip03 with dissolve
pause
scene clarastrip04 with dissolve
pause
scene clarastrip05 with dissolve
pause
scene clarastrip06 with dissolve
pause
scene clarastrip07 with dissolve
pause
scene clarastrip08 with dissolve
pause
scene clarastrip09 with dissolve
pause
scene clarastrip10 with dissolve
pause

label ClaraStripEnd:
if handjobcl:
    jump StripClaraHandjob
stop music
$ period += 1
show screen calendar
show screen mcstats
scene strip01
show stripclara03
cl "That's it, I hope you enjoyed the show, I feel like a sinner now..."
mc "Well, you know what you could do to repent your sins right?"
cl "Yes I do. I will go to the church and pray."
mc "Ah. That's NOT what I had in mind..."
jump Bedroom

label StripClaraHandjob:
scene strip02 blurred with dissolve
show stripclara04
cl "And now for the NAUGHTY part... And I can see you already have your cock out, you're such a NAUGHTY boy!"
scene claraprehandjob01 with dissolve
cl "And what a mighty phallus it is! One worthy of being serviced by a sinner like me..."
mc "Then get on your knees and prep it by licking my fat balls. They're the ones that contain the Holy Sperm I'll be delivering at the end of this session."
scene claraprehandjob02 with dissolve
cl "Of course! They deserve praise for being so... large and bountiful. *slurp*"
mc "Yeah, that's good Sister Clara...."
cl "And now for the main course... I'll use both hands since you are so LARGE and I am a true sinner!"
play music "Sounds/wank.mp3"
scene clarahandjobbackground
label ClaraHandjobSlow:
show clarahandjobslow
hide clarahandjobfast
call screen clarahandjobslow
screen clarahandjobslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraHandjobEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ClaraHandjobFast") 

label ClaraHandjobFast:
cl "I'll jack your shaft as fast as I can [name]! Prepare to shoot your Holy Sperm EVERYWHERE!"
window hide
hide clarahandjobslow
show clarahandjobfast
call screen clarahandjobfast
screen clarahandjobfast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraHandjobEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ClaraHandjobSlow") 

label ClaraHandjobEnd:
hide clarahandjobslow
hide clarahandjobfast
show clarahandjobcum01
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
cl "Yes, let it all out, let the Holy Sperm flow bountifully over the New Garden of Eden!"
hide clarahandjobcum01
show clarahandjobcum02
stop music
if clarahandjobdone == False:
    call LustPlusClara
cl "Well, I feel like I have washed away some of my dreadful sins by servicing a boy with a phallus that is worthy of Saint-Manhood!"
mc "Gee, that church sure is weird. It wasn't like that in my days. But I ain't complaining, thank you Santorum!"
$ period += 1
$ clarahandjobdone = True
show screen calendar
show screen mcstats
scene strip01 with dissolve
show stripclara03
cl "That's it, I hope you enjoyed the show... and the handjob."
mc "Thank you so much for relieving me of such a burden. In my Holy Balls."
jump Bedroom

label GwenPreStrip01:
stop music
$ seenbar = True
scene strip01
if (stripgw == True):
    show stripgwen01 with fastdissolve
    gw "Wow, you're back for more [name]? It was THAT good wasn't it?"
    menu:
        "Err, actually, I got the wrong day. I thought some other girl would be here tonight.":
            hide stripgwen01
            show stripgwen03 with fastdissolve
            gw "Umpf.. That's not a very nice thing to say..."
            call LustMinusGwen
            gw "Goodbye then [name], hope you find the RIGHT girl for you."  
            jump Bar
        "Yep, I am officially addicted. Your body is worth every dollar.":
            hide stripgwen01
            show stripgwen03 with fastdissolve
            gw "Wow, thank you ssoo much for saying that... I will milk it big time, just like Icstor and Aorrta."
            mc "So, what services do you offer Gwen?"
            hide stripgwen04
            jump GwenPreStrip02
        "Ah, sorry, wrong door.":
            hide stripgwen01
            show stripgwen02 with fastdissolve
            gw "(sigh)... I was hoping to make some money tonight. I guess I'll have to go back and work in the lab."
            jump Bar

elif worklab >= 1:
    show stripgwen01 with dissolve
    gw "Oh, hello [name]... I am a bit embarrassed... I mean, we  are colleagues..."
    mc "Don't worry, I won't tell Debra."
    hide stripgwen01
    show stripgwen02 with fastdissolve
    gw "Thanks! In that case, I am willing to provide my services to you... In exchange for a fee of course..."
    mc "So, what services do you offer Gwen?"
    hide stripgwen02
    jump GwenPreStrip02

elif spokegw >= 01:
    show stripgwen02 with dissolve
    gw "Oh, hello [name]... Fancy seeing you here..."
    mc "Treat me as an anonymous client. One with a huge cock that can satisfy any woman."
    hide stripgwen02
    show stripgwen01 with fastdissolve
    gw "Oh, TMI, TMI..."
    mc "So, what services do you offer Gwen?"
    hide stripgwen01
    jump GwenPreStrip02

elif spokegw == 0:
    show stripgwen01 with fastdissolve
    gw "Thank you for choosing me...  And not pointing a gun at me."
    mc "So, what services do you offer Gwen?"
    hide stripgwen01
    jump GwenPreStrip02
    
label GwenPreStrip02:
show stripgwen03 with fastdissolve
gw "It depends how much you are willing to pay...."
label GwenPreStripChoice:
show stripgwen03 
menu:
    "Tell me more...":
        gw "A simple striptease session is $10. A handjob is $20 more. I won't go any further that that, I'm not, like, a total whore."
        $ pricegw = True
        jump GwenPreStripChoice
    "I'll take a striptease session please." if money >= 10 and pricegw == True:
        hide stripgwen03
        show stripgwen01 with fastdissolve
        gw "Relax in the comfy chair and watch... My body being displayed to you for hard cash."
        $ stripgw = True
        $ money -= 10
        jump GwenStrip01
    "I'll take the handjob please." if money >= 30 and pricegw == True:
        gw "In that case, relax in the comfy chair and watch... An underpaid PhD student stripping and giving handjobs for cash."
        $ handjobgw = True
        $ money -= 30
        jump GwenStrip01
    "Turns out I'm broke actually. Maybe another time.":
        hide stripgwen03
        show stripgwen02 with fastdissolve
        gw "Oh. That is very unfortunate... I really needed the money (sigh)...."
        jump Bar

label GwenStrip01:
hide screen calendar
hide screen mcstats
play music "Sounds/stripmusic.mp3"
scene gwenstriplarge with dissolve:
        ypos -3.0
        linear 10.0 ypos 0.0
$ renpy.pause(10.0, hard=True)
gw "Ready?"
mc "Fuck yeah!"
scene gwenstrip01 with dissolve
pause
scene gwenstrip02 with dissolve
gw "Oh,I forgot my make-up! Let me get it... I'll look naughtier with it."
pause
scene gwenstrip03 with dissolve
pause
scene gwenstrip04 with dissolve
pause
scene gwenstrip05 with dissolve
pause
scene gwenstrip06 with dissolve
pause
scene gwenstrip07 with dissolve
pause
scene gwenstrip08 with dissolve
pause
scene gwenstrip09 with dissolve
pause
scene gwenstrip10 with dissolve
pause
        
label GwenStripEnd:
stop music
if handjobgw:
    jump StripGwenHandjob
$ period += 1
show screen calendar
show screen mcstats
scene strip01
show stripgwen04 with fastdissolve
gw "That's it, I see you liked the show didn't you [name]?..."
mc "Yes, thank you. I shall now go and have a.. wank."
gw "Eew, too much information..."
hide stripgwen04
jump Bedroom

label StripGwenHandjob:
scene strip02 blurred with dissolve
show stripgwen04
gw "So... Are you ready for your $20 handjob?"
mc "Fuck yeah! I'm as hard as granite right now!"
scene gwenprehandjob01 with dissolve
gw "I can see that... It's so fucking LONG and FAT. And you're already drooling precum all over the place. Am I making you THAT horny?"
mc "Y...YES... OH shit, I think I'm gonna..."
scene gwenprehandjob02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...CUM already! AAAH!"
gw "Oh, wow! You really ARE horny tonight, aren't you?"
scene gwenprehandjob03 with dissolve
mc "Phew... Yeah, that was just a tiny horny spurt... I... think you can go ahead with the handjob now... I seem to have calmed down a bit."
gw "I will... I'll tease you slowly with my nails at first..."
play music "Sounds/wank.mp3"
label GwenHandjobSlow:
show stripgwenhandjobslow
hide stripgwenhandjobfast
call screen gwenhandjobslow
screen gwenhandjobslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenHandjobEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenHandjobFast") 

label GwenHandjobFast:
gw "Maybe I should tease your trembling cock a little faster, hum? I think that'll make you CUM, right?"
mc "Aaaah..."
window hide
hide stripgwenhandjobslow
show stripgwenhandjobfast
call screen gwenhandjobfast
screen gwenhandjobfast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenHandjobEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("GwenHandjobSlow") 

label GwenHandjobEnd:
scene gwenhandjobcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
gw "That's it [name], let it ALL out!"
scene gwenhandjobcum02 with dissolve
gw "You're pumping spunk out of your fat shaft like a FIREHOSE! My long nails really bloated your balls with a HEAVY DOSE!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene gwenhandjobcum03 with dissolve
mc "AAAAH! Y... YES... AAAH, Can't stop CUUUUMMMIING!"
gw "How can you cum THAT much? You truly are a SPERM MACHINE!"
scene gwenhandjobcum04 with dissolve
stop music
if gwenhandjobdone == False:
    call LustPlusGwen
gw "Oh my God... I'm plastered in your load... I'm gonna have to clean myself up by... slurping it in my mouth."
mc "You go ahead Gwen. And you can lick the drops that landed on me too while you're at it..."
gw "MMmh, you're such a NAUGHTY boy."
$ period += 1
$ gwenhandjobdone = True
show screen calendar
show screen mcstats
scene strip01
show stripgwen04b
with dissolve
gw "That's it, I hope you enjoyed my show... teasing handjob. Now I've got to take a shower, I still feel all sticky..."
mc "And I think I'll have a good night's sleep. Phew!"
jump Bedroom

label MichikoPreStrip01:
stop music
$ seenbar = True
scene strip01
if (stripmi == True):
    show stripmichiko01 with fastdissolve
    mi "Can't get enough of these HUGE knockers can you [name]?"
    menu:
        "Err, actually, I got the wrong day. I thought some other girl would be here tonight.":
            hide stripmichiko01
            show stripmichiko04 with fastdissolve
            mi "Umpf.. That's not a very nice thing to say..."
            call LustMinusMichiko
            mi "Goodbye then [name], hope you find the RIGHT girl for you."  
            jump Bar
        "Yep, I am officially addicted. Your body is worth every dollar.":
            hide stripmichiko01
            show stripmichiko03 with fastdissolve
            mi "Wow, thank you ssoo much for saying that... I will milk it big time, just like Aorrta."
            mc "So, what services do you offer tonight Michiko?"
            jump MichikoPreStrip02            
        "Ah, sorry, wrong door.":
            hide stripmichiko01
            show stripmichiko04 with dissolve
            mi "This not the DOJO!"
            jump Bar

if spokemi >= 1:
    show stripmichiko01 with fastdissolve
    mi "Well, well, well, who do we have here?"
    mc "A guy with huge muscles and a huge cock."
    hide stripmichiko01
    show stripmichiko02 with fastdissolve
    mi "Oh, I KNOW. And I'm a girl with huge knockers and a HUGE backdoor."
    mc "Interesting. So, what services do you offer Michiko?"
    jump MichikoPreStrip02

if spokemi == 0:
    show stripmichiko01 with fastdissolve
    mi "Thank you for choosing me [name]...."
    mc "So, what services do you offer Michiko?"
    jump MichikoPreStrip02
    
label MichikoPreStrip02:
hide stripmichiko01
show stripmichiko03 with dissolve
mi "It depends how much you are willing to pay...."
label MichikoPreStripChoice:
show stripmichiko03
menu:
    "Tell me more...":
        mi "A simple striptease session is $10. A footjob is $10 more. And my feet are VERY flexible."
        $ pricemi = True
        jump MichikoPreStripChoice
    "I'll take a striptease session please Michiko." if money >= 10 and pricemi == True:
        mi "Naughty boy... I like it. Relax in the comfy chair and watch me... I'll be extra-kinky for you."
        $ stripmi = True
        $ money -= 10
        jump MichikoStrip01
    "I'll take the footjob please." if money >= 20 and pricemi == True:
        mi "You will LOVE it name. My tiny dainty feet on your massive shaft..."
        mi "Relax in the comfy chair and watch me strip for you... Before engulfing your dong between my little feet..."
        $ titjobmi = True
        $ money -= 20
        jump MichikoStrip01
    "Turns out I'm broke actually. Maybe another time.":
        hide stripmichiko03
        show stripmichiko04 with fastdissolve
        mi "Poor people get no poontang. Get rich soon [name]..."
        jump Bar

label MichikoStrip01:
hide screen calendar
hide screen mcstats
play music "Sounds/stripmusic.mp3"
scene michikostriplarge with dissolve:
        ypos -3.0
        linear 10.0 ypos 0.0
$ renpy.pause(10.0, hard=True)
mi "Ready?"
mc "Hard and ready!"
scene michikostrip01 with dissolve
pause
scene michikostrip02 with dissolve
pause
scene michikostrip03 with dissolve
pause
scene michikostrip04 with dissolve
pause
scene michikostrip05 with dissolve
pause
scene michikostrip06 with dissolve
pause
scene michikostrip07 with dissolve
pause
scene michikostrip08 with dissolve
pause
scene michikostrip09 with dissolve
pause
scene michikostrip10 with dissolve
pause

label MichikoStripEnd:
if titjobmi:
    jump StripMichikoFootjob
stop music
$ period += 1
show screen calendar
show screen mcstats
scene strip01
show stripmichiko05 with fastdissolve
mi "Mmh, my backdoor is really dilated now... And it's delicious!"
mc "Please let me have a taste!"
mi "I don't think so. You have to CONTROL yourself to be a good fighter."
jump Bedroom

label StripMichikoFootjob:
scene strip02 blurred with dissolve
show stripmichiko05
mi "Now that I'm all NAKED... Time for YOU to get naked too and show me that piece of boymeat that's distending your pants to bursting point!"
scene michikoprefootjob with dissolve
mi "Mmmh, I'm gonna have to be VERY flexible to take care of such a monster rod. Get out of the chair and lie down on the floor [name]..."
scene michikofootjobbackground with dissolve
show michikofootjob00
mi "There, my feet are at the base of your giant shaft, ready to travel all the way to the tip... Ready [name]?"
mc "Yeah, I'm ready as can be Michiko!"
play music "Sounds/wank.mp3"
scene michikofootjobbackground
label MichikoFootjobSlow:
show michikofootjobslow
hide michikofootjobfast
call screen michikofootjobslow01
screen michikofootjobslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoFootjobEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MichikoFootjobFast") 

label MichikoFootjobFast:
mi "Oh, you want me to go faster do you?"
window hide
hide michikofootjobslow
show michikofootjobfast
call screen michikofootjobfast01
screen michikofootjobfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoFootjobEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MichikoFootjobSlow") 

label MichikoFootjobEnd:
stop music
scene michikofootjobcumbackground blurred
show michikofootjobcum01
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mi "Oooh, my feet are THAT good [name]? You're cumming like a STALLION all over the place!"
hide michikofootjobcum01
show michikofootjobcum02
mi "Those jets of spunk are flying sssooo HIGH!"
hide michikofootjobcum02
show michikofootjobcum03
if michikofootjobdone == False:
    call LustPlusMichiko
mi "And look at you now, your still rock-hard behemoth is still spewing some afterdreads all over your chest and we're both covered in your thick spunk... What a naughty boy you are [name]!"
mc "Why don't you take care of my cock some more then Michiko?"
mi "Tempting but you paid for ONE footjob, not several in a row..."
$ period += 1
$ michikofootjobdone = True
show screen calendar
show screen mcstats
scene strip01 with dissolve
show stripmichiko05
mi "I hope you enjoyed the show [name]... and the footjob."
mc "I sure did. Even if I have to take a shower now since I'm covered in my own cream..."
jump Bedroom

label PennyPreStrip01:
stop music
$ seenbar = True
scene strip01
show strippenny01 with fastdissolve
if (strippe == False):
    pe "Oh... Well, now you know... Yes, I'm a part-time stripper. I just like the gig..."
    mc "I like your gig too... So, what services do you offer?"
    jump PennyPreStrip02
    
if (strippe == True):
    pe "You again? You are starting to become a regular client [name]."
    mc "Well, one needs regular entertainment to relieve the stress from a hard working day."
    pe "I know what you mean, that's why I enjoy being a stripper in the evenings... So, what can I do for you today?"
    menu:
        "I'll have a striptease session please." if money >= 5:
            pe "Alright, sit back and enjoy the show!"
            $ money -= 5
            jump PennyStrip01
        "I need to empty my balls. So a nice titjob it is then." if money >= 10:
            pe "Alright, relax in the comfy chair, I'll take care of everything... Including that HUGE cock of yours!"
            $ money -= 10
            $ titjobpe = True
            jump PennyStrip01
        "Nothing, I'm broke.":
            hide strippenny01
            show strippenny03 with fastdissolve
            pe "Oh. Well, you know what? I'll give you a striptease for free anyway.... It's not like I'm expecting any other clients."
            mc "Alright!"
            pe "So relax in the comfy chair and watch me... slowly taking off my lingerie for you."
            jump PennyStrip01

label PennyPreStrip02:
hide strippenny01
show strippenny02 with fastdissolve
pe "Several services, ranging from the naughty to the... very naughty!"
label PennyPreStripChoice:
show strippenny02
menu:
    "Tell me more...":        
        pe "A simple striptease session is only $5. And a titjob session is $10. I'm as cheap as they come because I actually ENJOY what I do."
        $ pricepe = True
        jump PennyPreStripChoice
    "I'll take a striptease session please. (-$5)" if money >= 5 and pricepe == True:
        hide strippenny02
        show strippenny04 with fastdissolve
        pe "Relax in the comfy chair and watch me... slowly taking off my lingerie for you."
        $ strippe = True
        $ money -= 5
        hide strippenny04
        jump PennyStrip01
    "I'll take the titjob please. (-$10)" if money >= 10 and pricepe == True:
        hide strippenny02
        show strippenny04 with fastdissolve
        pe "Relax in the comfy chair, I'll take care of everything... Including that HUGE cock of yours!"
        hide strippenny04
        $ titjobpe = True
        $ money -= 10
        jump PennyStrip01
    "Turns out I'm broke actually. Maybe another time.":
        hide strippenny02
        show strippenny03 with fastdissolve
        pe "Oh. Well, you know what? I'll give you a striptease for free anyway.... It's not like I'm expecting any other clients."
        mc "Alright!"
        pe "So relax in the comfy chair and watch me... slowly taking off my lingerie for you."
        jump PennyStrip01

label PennyStrip01:
hide screen calendar
hide screen mcstats
play music "Sounds/stripmusic.mp3"
scene pennystriplarge with dissolve:
    ypos -3.0
    linear 10.0 ypos 0.0
$ renpy.pause(10.0, hard=True)
pe "Ready?"
mc "Full steam ahead!"
scene pennystrip01 with dissolve
pause
scene pennystrip02 with dissolve
pause
scene pennystrip03 with dissolve
pe "Mmh, should I take off my bra? I think I should..."
scene pennystrip04 with dissolve
pause
scene pennystrip05 with dissolve
pause
scene pennystrip06 with dissolve
pause
scene pennystrip07 with dissolve
pause
scene pennystrip08 with dissolve
pause
scene pennystrip09 with dissolve
pause
scene pennystrip10 with dissolve
pause
        
label PennyStripEnd:
if titjobpe:
    jump StripPennyTitjob
stop music
$ period += 1
show screen calendar
show screen mcstats
scene strip01
show strippenny05 with fastdissolve
pe "I feel great! This is so liberating. But it's over for you [name]..."
mc "Let me liberate you some more."
pe "No. I have to work tomorrow. Have sweet dreams!"
jump Bedroom

label StripPennyTitjob:
scene strip02 blurred with dissolve
show strippenny05
pe "I feel great! This is so liberating. Now it's time for me to LIBERATE that dong of yours from the tight confines of your pants!"
scene pennypretitjob01 with dissolve
pe "And then, make it CAPTIVE between my big breasts..."
mc "Let me feel them first for a while please."
scene pennypretitjob02 with dissolve
pe "Yeah, maul them and soften them up for that massive CUM-CANNON of yours!"
mc "Will do!"
pe "I think you're ready. I am. So lean back and... ENJOY!"
play music "Sounds/wank.mp3"
scene pennytitjobbackground
label PennyTitjobSlow:
show pennytitjobslow
hide pennytitjobfast
call screen pennytitjobslow01
screen pennytitjobslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyTitjobEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PennyTitjobFast") 

label PennyTitjobFast:
pe "Time to speed it up and get you to release yourself all over my tits and face!"
window hide
hide pennytitjobslow
show pennytitjobfast
call screen pennytitjobfast01
screen pennytitjobfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyTitjobEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PennyTitjobSlow") 

label PennyTitjobEnd:
stop music
scene pennytitjobcum01
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
pe "Yes, LIBERATE your cum from the tight confines of your balls!"
scene pennytitjobbackground blurred
show pennytitjobcum02
pe "Blast it EVRYWHERE! On my tits, on my FACE!"
mc "FU-UUUCK! AAAH"
scene pennytitjobcum03
if pennytitjobdone == False:
    call LustPlusPenny
pe "Well, look at the mess you did, naughty boy!"
mc "Phew... Sorry, my shots are so POWERFUL, it's hard to aim."
pe "I saw that. You almost reached the ceiling..."
$ period += 1
$ pennytitjobdone = True
show screen calendar
show screen mcstats
scene strip01 with dissolve
show strippenny05
pe "I hope you enjoyed the show [name]... and the titjob."
mc "I feel liberated. And tired. I'm going to go and stay captive in my bed for the night."
jump Bedroom

label SaturdayFight:
scene bar01 with fade
show marnie02
ma "Oh, hi [name]! It's Saturday evening, it's FIGHT TIME!"
if marnietipfight == False or sukifightquestdone:
    ma "I'm taking bets on tonight's virtual fight... 2:1 odds as usual. With a one dollar fee for me."
if marnietipfight and sukifightquestdone == False:
    ma "I'm taking bets on tonight's virtual fight between Michiko and Suki..."
hide marnie02
show marnie01
ma "Follow me to the bar to pick a winner and place a bet."

if marnietipfight == False:
    $ d3fightroll=renpy.random.randint(1,2)
    if d3fightroll == 1:
        ma "Tonight's fight is between Amy and Ayla for your information..."
    if d3fightroll == 2:
        ma "Tonight's fight is between Chief Lena and Ruby for your information..."
        jump PlaceBet
if sukifightquestdone:
    $ d3fightroll=renpy.random.randint(1,3)
    if d3fightroll == 1:
        ma "Tonight's fight is between Amy and Ayla for your information..."
    if d3fightroll == 2:
        ma "Tonight's fight is between Chief Lena and Ruby for your information..."
    if d3fightroll == 3:
        ma "Tonight's fight is between Michiko and Suki for your information..."
    jump PlaceBet
if marnietipfight and sukifightquestdone == False:
    $ d3fightroll = 3
    ma "Since Michiko is the clear favorite, odds are 3:2 for her and 3:1 for Suki."
label PlaceBet:
scene bar02
show marnie02
show bar02b
with dissolve
ma "So, are you ready to place a bet [name]?"

menu:
    "Place a bet on Amy" if money >= 5 and d3fightroll == 1:
        ma "Alright, how much money?"
        menu:
            "5 bucks" if money >= 5:
                $ money -= 5
                $ amybet = 5
                ma "Done!"
            "10 bucks" if money >= 10:
                $ money -= 10
                $ amybet = 10
                ma "Done!"
            "20 bucks" if money >= 20:
                $ money -= 20
                $ amybet = 20
                ma "Done!"                
    "Place a bet on Ayla" if money >= 5 and d3fightroll == 1:
        ma "Alright, how much money?"
        menu:
            "5 bucks" if money >= 5:
                $ money -= 5
                $ aylabet = 5
                ma "Done!"
            "10 bucks" if money >= 10:
                $ money -= 10
                $ aylabet = 10
                ma "Done!"
            "20 bucks" if money >= 20:
                $ money -= 20
                $ aylabet = 20
                ma "Done!"
    "Place a bet on Chief Lena" if money >= 5 and d3fightroll == 2:
        ma "Alright, how much money?"
        menu:
            "5 bucks" if money >= 5:
                $ money -= 5
                $ lenabet = 5
                ma "Done!"
            "10 bucks" if money >= 10:
                $ money -= 10
                $ lenabet = 10
                ma "Done!"
            "20 bucks" if money >= 20:
                $ money -= 20
                $ lenabet = 20
                ma "Done!"
    "Place a bet on Ruby" if money >= 5 and d3fightroll == 2:
        ma "Alright, how much money?"
        menu:
            "5 bucks" if money >= 5:
                $ money -= 5
                $ rubybet = 5
                ma "Done!"
            "10 bucks" if money >= 10:
                $ money -= 10
                $ rubybet = 10
                ma "Done!"
            "20 bucks" if money >= 20:
                $ money -= 20
                $ rubybet = 20
                ma "Done!"                
    "Place a bet on Michiko" if money >= 5 and d3fightroll == 3 and sukifightquestdone:
        ma "Alright, how much money?"
        menu:
            "5 bucks" if money >= 5:
                $ money -= 5
                $ michikobet = 5
                ma "Done!"
            "10 bucks" if money >= 10:
                $ money -= 10
                $ michikobet = 10
                ma "Done!"
            "20 bucks" if money >= 20:
                $ money -= 20
                $ michikobet = 20
                ma "Done!"
    "Place a bet on Suki" if money >= 5 and d3fightroll == 3 and sukifightquestdone:
        ma "Alright, how much money?"
        menu:
            "5 bucks" if money >= 5:
                $ money -= 5
                $ sukibet = 5
                ma "Done!"
            "10 bucks" if money >= 10:
                $ money -= 10
                $ sukibet = 10
                ma "Done!"
            "20 bucks" if money >= 20:
                $ money -= 20
                $ sukibet = 20
                ma "Done!"                
    "Place a bet on Michiko (3:2 odds)" if money >= 6 and marnietipfight and sukifightquestdone == False:
        $ sukifightquestdone = True
        $ d3fightroll = 3
        ma "Alright, how much money?"
        menu:
            "6 bucks" if money >= 6:
                $ money -= 6
                $ michikobet = 6
                ma "Done!"
            "12 bucks" if money >= 12:
                $ money -= 12
                $ michikobet = 12
                ma "Done!"
            "24 bucks" if money >= 24:
                $ money -= 24
                $ michikobet = 24
                ma "Done!"
    "Place a bet on Suki (3:1 odds)" if money >= 5 and marnietipfight and sukifightquestdone == False:
        $ sukifightquestdone = True
        $ d3fightroll = 3
        ma "Alright, that's pretty bold. How much money?"
        menu:
            "5 bucks" if money >=5:
                $ money -= 5
                $ sukibet = 5
                ma "Done!"
            "10 bucks" if money >=10:
                $ money -= 10
                $ sukibet = 10
                ma "Done!"
            "20 bucks" if money >=20:
                $ money -= 20
                $ sukibet = 20
                ma "Done!"
    "Don't place any bet":
        if marnietipfight and sukifightquestdone == False:
            $ sukifightquestdone = True
        hide marnie02
        hide bar02b
        show marnie06 
        show bar02b
        with fastdissolve
        ma "That's pretty lame..."
        if money <= 4:
            mc "Yeah, well, I'm broke..."
        hide marnie06
hide marnie02
show marnie01
ma "Anyway, the fight is about to start, let's move to the dancefloor where the virtual ring will appear in full 3D holographic glory!"
play music "Sounds/audience.mp3"
scene fridayparty02
if d3fightroll == 1:
    show virtualamy at left
    show virtualayla at midright
if d3fightroll == 2:
    show virtuallena at left
    show virtualruby at midright
if d3fightroll == 3:
    show virtualmichiko at left
    show virtualsuki at midright
ma "There they are, in full virtual reality gear, ready to fight it off!"

label BarFight01:
hide screen calendar
hide screen mcstats
if d3fightroll == 1:
    menu:
        "Watch the fight between Amy and Ayla":
            jump WatchFightAmy
        "Skip to the end (random winner)":
            $ d2rollfight=renpy.random.randint(1,2)
            play sound "Sounds/winner.mp3"
            window hide
            if d2rollfight == 1:
                scene fightamywin with dissolve
                show winnersign at streetfight02
                $ renpy.pause(1, hard=True)
                ma "Amy wins tonight's fight!"    
                play music "Sounds/applause.mp3"
                $ renpy.pause(2, hard=True)
                hide winnersign
            if d2rollfight == 2:            
                scene fightaylawin with dissolve
                show winnersign at streetfight02
                $ renpy.pause(1, hard=True)
                ma "Ayla wins tonight's fight!" 
                play music "Sounds/applause.mp3"
                $ renpy.pause(2, hard=True)
                hide winnersign        
            jump AmyAylaFightEnding
    label WatchFightAmy:
    $ amy_health = 5.0
    $ ayla_health = 5.0
    show screen screenfightamyayla
    play sound "Sounds/barfight.mp3"
    ma "Our two contenders tonight are..."
    scene fightamy01 with dissolve
    ma "AMY!"
    window hide
    play sound "Sounds/applause.mp3"
    show amysign at streetfight01
    $ renpy.pause(1, hard=True)
    show amysign:
        xalign 0.4
        yalign 0.4
    ma "And..."
    window hide
    show versussign at streetfight02
    stop sound
    play sound "Sounds/versus.mp3"
    $ renpy.pause(1, hard=True)
    show versussign:
        xalign 0.5
        yalign 0.5
    scene fightayla01 with dissolve
    show amysign:
        xalign 0.4
        yalign 0.4
    show versussign:
        xalign 0.5
        yalign 0.5
    ma "AYLA!"
    window hide
    play sound "Sounds/applause.mp3"
    show aylasign at streetfight03
    $ renpy.pause(1, hard=True)
    show aylasign:
        xalign 0.6
        yalign 0.6
    pause 1.0
    stop sound
    scene fightsetup with dissolve
    show aylasetup at midright
    show amysetup at midleft
    play sound "Sounds/three.mp3"
    show threesign at streetfight02
    $ renpy.pause(1, hard=True)
    hide threesign
    play sound "Sounds/two.mp3"
    show twosign at streetfight02
    $ renpy.pause(1, hard=True)
    hide twosign
    play sound "Sounds/one.mp3"
    show onesign at streetfight02
    $ renpy.pause(1, hard=True)
    hide onesign
    play sound "Sounds/fight.mp3"
    show fightsign at streetfight02
    $ renpy.pause(1, hard=True)
    hide fightsign
    show amysetup at center with move
    ma "Amy makes a move..."
    scene aylaup01 with dissolve
    ma "..But her attack is dodged by Ayla!"
    scene aylaup02 with dissolve
    play sound "Sounds/punch.mp3"
    $ renpy.pause(.5, hard=True)
    show boobpunch:
        xalign 0.4
        yalign 0.6    
    $ counting = 0
    while counting < 20:
        $ amy_health -= 0.05
        $ counting += 1
        pause 0.01
    ma "..who counters with a painful boob punch!"
    scene amyup02 with dissolve
    $ renpy.pause(.5, hard=True)
    show knucklehead:
        xalign 0.6
        yalign 0.3    
    play sound "Sounds/punch.mp3"
    $ renpy.pause(.5, hard=True)
    $ counting = 0
    while counting < 20:
        $ ayla_health -= 0.05
        $ counting += 1
        pause 0.01
    ma "But Amy isn't letting herself down!"

    $ d2rollfight=renpy.random.randint(1,2)
    if d2rollfight == 1:
        scene amyup07 with dissolve
        play sound "Sounds/punch.mp3"
        $ renpy.pause(.5, hard=True)
        ma "She's fighting back with a nasty face punch!"
        $ counting = 0
        while counting < 20:
            $ ayla_health -= 0.1
            $ counting += 1
            pause 0.01
        ma "That will cause a huge health loss to Ayla for sure..."
        scene fightsetup with dissolve
        show aylasetup at midright
        show amysetup at midleft
        $ renpy.pause(1, hard=True)
        show aylasetup at center with move
        ma "Ayla makes a move..."
        scene fightayla01 with fastdissolve
        ma "She looks mighty angry!"
        scene aylaup03 with fastdissolve
        ma "Oh, she's doing the Matrix floating pose! Virtual time has stopped..."
        scene aylaup04 with fastdissolve
        play sound "Sounds/punch.mp3"
        $ renpy.pause(.5, hard=True)
        show matrixthrust:
            xalign 0.4
            yalign 0.6       
        $ counting = 0
        while counting < 20:
            $ amy_health -= 0.1
            $ counting += 1
            pause 0.01
        ma "...and Amy didn't have virtual time to see this high kick coming!"
        scene fightsetup with dissolve
        show aylasetup at midright
        show amysetup at midleft
        $ renpy.pause(1, hard=True)
        show amysetup at center with move
        ma "Back to the drawing board with Amy on the attack..."
        scene amyup03 with dissolve
        ma "She lifts her opponent onto her strong shoulders..."
        scene amyup04 with dissolve
        ma "..And throws her like a discarded condom!"
        scene amyup05 with dissolve
        play sound "Sounds/punch.mp3"
        $ renpy.pause(.5, hard=True)
        show groinstomp:
            xalign 0.4
            yalign 0.6       
        $ counting = 0
        while counting < 20:
            $ ayla_health -= 0.05
            $ counting += 1
            pause 0.01    
        ma "Followed by a painful groin stomp!"
        scene amyup06 with dissolve
        show pussygrab:
            xalign 0.4
            yalign 0.6       
        $ counting = 0
        while counting < 20:
            $ ayla_health -= 0.05
            $ counting += 1
            pause 0.01    
        ma "And Amy crushes Ayla's tiny head with her strong pelvic muscles. Ayla cannot recover from such a lethal move..."
        window hide
        play sound "Sounds/winner.mp3"
        scene fightamywin with dissolve
        show winnersign at streetfight02
        $ renpy.pause(1, hard=True)
        ma "Amy wins tonight's fight!"    
        play music "Sounds/applause.mp3"
        $ renpy.pause(2, hard=True)
        hide winnersign
        
    if d2rollfight == 2:
        scene fightayla01 with fastdissolve
        ma "That seems to have made Ayla angry as hell!"
        scene aylaup03 with fastdissolve
        ma "Oh, she's doing the Matrix floating pose! Virtual time has stopped..."
        scene aylaup04 with fastdissolve
        play sound "Sounds/punch.mp3"
        $ renpy.pause(.5, hard=True)
        show matrixthrust:
            xalign 0.4
            yalign 0.6       
        $ counting = 0
        while counting < 20:
            $ amy_health -= 0.1
            $ counting += 1
            pause 0.01
        ma "...and Amy didn't have virtual time to see this high kick coming!"
        scene fightsetup with dissolve
        show aylasetup at midright
        show amysetup at midleft
        $ renpy.pause(1, hard=True)
        show amysetup at center with move
        ma "Back to the drawing board with Amy on the attack..."
        scene amyup03 with dissolve
        ma "She lifts her opponent onto her strong shoulders..."
        scene amyup04 with dissolve
        ma "..And throws her like a discarded condom!"
        scene amyup05 with dissolve
        play sound "Sounds/punch.mp3"
        $ renpy.pause(.5, hard=True)
        show groinstomp:
            xalign 0.4
            yalign 0.6       
        $ counting = 0
        while counting < 20:
            $ ayla_health -= 0.1
            $ counting += 1
            pause 0.01    
        ma "Followed by a painful groin stomp!"
        scene aylaup06 with fastdissolve
        ma "But Ayla hasn't said her last word... She jumps on Amy's back and flips the situation around!"
        scene aylaup05 with fastdissolve
        ma "I can hear Amy's virtual spine break in half... That's got to hurt..."
        show backbreaker:
            xalign 0.4
            yalign 0.6       
        $ counting = 0
        while counting < 20:
            $ amy_health -= 0.1
            $ counting += 1
            pause 0.01
        ma "And Amy is out for good!"
        play sound "Sounds/winner.mp3"
        window hide
        scene fightaylawin with dissolve
        show winnersign at streetfight02
        $ renpy.pause(1, hard=True)
        ma "Ayla wins tonight's fight!" 
        play music "Sounds/applause.mp3"
        $ renpy.pause(2, hard=True)
        hide winnersign        
    label AmyAylaFightEnding:
    $ period += 1
    stop music
    hide screen screenfightamyayla
    show screen calendar
    show screen mcstats
    if aylabet >= 1 and d2rollfight == 2:
        stop music
        stop sound
        mc "Time for me to collect my winnings!"
        scene bar02 with dissolve
        show marnie06
        show bar02b
        with fastdissolve
        ma "Ah, you want your money..."
        mc "Yep."
        hide marnie06
        hide bar02b
        show marnie01
        show bar02b
        with fastdissolve
        $ aylabetdouble = (aylabet + aylabet) - 1
        ma "I'll get it for you then. [aylabetdouble] New dollars. One dollar service fee of course. Come back next Saturday evening for another virtual fight night!"
        $ money += aylabetdouble
        mc "Nice. I can go back to my bedroom to count my money..."
        jump Bedroom
    if amybet >= 1 and d2rollfight == 1:
        stop music
        stop sound
        mc "Time for me to collect my winnings!"
        scene bar02 with dissolve
        show marnie06
        show bar02b
        with fastdissolve
        ma "Ah, you want your money..."
        mc "Yep."
        hide marnie06
        hide bar02b
        show marnie01
        show bar02b
        with fastdissolve
        $ amybetdouble = (amybet + amybet) - 1
        ma "I'll get it for you then. [amybetdouble] New dollars. One dollar service fee of course. Come back next Saturday evening for another virtual fight night!"
        $ money += amybetdouble
        mc "Nice. I can go back to my bedroom to count my money..."
        jump Bedroom
    if amybet == 0 and aylabet == 0:
        mc "Oh well, it was an interesting fight. With zero stake in it for me."
        stop music
        stop sound
        jump Bedroom
    mc "Damn it! I lost my bet! Oh well, time to go back to my bedroom then..."
    stop music
    stop sound
    jump Bedroom

if d3fightroll == 2:
    menu:
        "Watch the fight between Lena and Ruby":
            jump WatchFightLena
        "Skip to the end (random winner)":
            $ d2rollfight=renpy.random.randint(1,2)
            play sound "Sounds/winner.mp3"
            window hide
            if d2rollfight == 2:
                scene fightlenawin with dissolve
                show winnersign at streetfight02
                $ renpy.pause(1, hard=True)
                ma "Lena wins tonight's fight!"    
                play music "Sounds/applause.mp3"
                $ renpy.pause(2, hard=True)
                hide winnersign
            if d2rollfight == 1:            
                scene fightrubywin with dissolve
                show winnersign at streetfight02
                $ renpy.pause(1, hard=True)
                ma "Ruby wins tonight's fight!" 
                play music "Sounds/applause.mp3"
                $ renpy.pause(2, hard=True)
                hide winnersign        
            jump LenaRubyFightEnding
    label WatchFightLena:
    $ ruby_health = 5.0
    $ lena_health = 5.0
    show screen screenfightlenaruby
    play sound "Sounds/barfight.mp3"
    ma "Our two contenders tonight are..."
    scene lenafight01 with dissolve
    ma "LENA!"
    window hide
    play sound "Sounds/applause.mp3"
    show lenasign at streetfight01
    $ renpy.pause(1, hard=True)
    show lenasign:
        xalign 0.4
        yalign 0.4
    ma "And..."
    window hide
    show versussign at streetfight02
    stop sound
    play sound "Sounds/versus.mp3"
    $ renpy.pause(1, hard=True)
    show versussign:
        xalign 0.5
        yalign 0.5
    scene rubyfight01 with dissolve
    show lenasign:
        xalign 0.4
        yalign 0.4
    show versussign:
        xalign 0.5
        yalign 0.5
    ma "RUBY!"
    window hide
    play sound "Sounds/applause.mp3"
    show rubysign at streetfight03
    $ renpy.pause(1, hard=True)
    show rubysign:
        xalign 0.6
        yalign 0.6
    pause 1.0
    stop sound
    scene fightsetup with dissolve
    show rubysetup at midright
    show lenasetup at midleft
    play sound "Sounds/three.mp3"
    show threesign at streetfight02
    $ renpy.pause(1, hard=True)
    hide threesign
    play sound "Sounds/two.mp3"
    show twosign at streetfight02
    $ renpy.pause(1, hard=True)
    hide twosign
    play sound "Sounds/one.mp3"
    show onesign at streetfight02
    $ renpy.pause(1, hard=True)
    hide onesign
    play sound "Sounds/fight.mp3"
    show fightsign at streetfight02
    $ renpy.pause(1, hard=True)
    hide fightsign
    show rubysetup at center with move
    ma "Ruby makes a move..."
    scene lenarubyfight01    
    ma "She lounges forward with the mindset of a berserk Road Warrior..."
    scene lenarubyfight02
    ma "..But Chief Lena saw it coming and fiercely knees her pussy!"
    play sound "Sounds/punch.mp3"
    $ renpy.pause(.5, hard=True)
    show groinkick:
        xalign 0.5
        yalign 0.8    
    $ counting = 0
    while counting < 20:
        $ ruby_health -= 0.05
        $ counting += 1
        pause 0.01
    scene lenarubyfight03
    ma "Followed by a high kick to the boobs! Ruby is sent flying into the corner! What a move by our Chief!"
    play sound "Sounds/punch.mp3"
    $ renpy.pause(.5, hard=True)
    show boobkick:
        xalign 0.7
        yalign 0.4    
    $ counting = 0
    while counting < 20:
        $ ruby_health -= 0.05
        $ counting += 1
        pause 0.01
    scene fightsetup with dissolve
    show rubysetup at midright
    show lenasetup at midleft
    $ renpy.pause(1, hard=True)
    ma "Back to the drawing board with Chief Lena in the lead!"

    $ d2rollfight=renpy.random.randint(1,2)
    if d2rollfight == 1:
        show lenasetup at center with move
        ma "Lena is the one on the attack this time..."
        scene lenarubyfight08
        ma ".. But Ruby grabs her on the move and holds her tight in a spine-crushing fashion!"        
        $ renpy.pause(.5, hard=True)
        show spinecrush:
            xalign 0.6
            yalign 0.6       
        $ counting = 0
        while counting < 20:
            $ lena_health -= 0.05
            $ counting += 1
            pause 0.01
        ma "That will cause a huge health loss to Lena for sure..."
        scene fightsetup with dissolve
        show lenasetup at midleft
        show rubysetup at midright
        $ renpy.pause(1, hard=True)
        show rubysetup at center with move
        ma "Ruby makes a move..."
        scene lenarubyfight01 with fastdissolve
        ma "She's gone into berserk mode again!"
        scene lenarubyfight06 with fastdissolve
        ma "This time, Lena can't stop her from scissoring her with her strong legs..."
        $ renpy.pause(.5, hard=True)
        show scissorlegs:
            xalign 0.7
            yalign 0.6       
        $ counting = 0
        while counting < 20:
            $ lena_health -= 0.05
            $ counting += 1
            pause 0.01
        ma "Oops, Lena is showing some virtual nipple there, children please look away."
        scene lenarubyfight07 with fastdissolve
        ma "... And Ruby ends her move by delivering a mighty punch to Lena's face!"
        play sound "Sounds/punch.mp3"
        $ renpy.pause(.5, hard=True)
        show headpunch:
            xalign 0.3
            yalign 0.6       
        $ counting = 0
        while counting < 20:
            $ lena_health -= 0.1
            $ counting += 1
            pause 0.01
        ma "Lena is badly bruised but not yet defeated..."
        scene fightsetup with dissolve
        show rubysetup at midright
        show lenasetup at midleft
        $ renpy.pause(1, hard=True)
        show lenasetup at center with move
        ma "And now Lena is on the prowl..."
        scene lenarubyfight04 with dissolve
        ma "She moves like a cat in heat and appears out of nowhere from underneath Ruby..."
        $ renpy.pause(.5, hard=True)
        $ counting = 0
        while counting < 20:
            $ ruby_health -= 0.05
            $ counting += 1
            pause 0.01    
        scene rubyfight01
        ma "Ruby fell hard on this one but quickly gets up!"
        scene lenarubyfight10 with dissolve
        ma "While Lena is still on the floor, Ruby grabs her by the legs..."
        scene lenarubyfight11 with dissolve
        ma "She's pushing hard with all her might to break Lena's spine! My God, this is so hard to watch!"
        play sound "Sounds/bonecrack.mp3"
        $ renpy.pause(.5, hard=True)
        show spinecrush:
            xalign 0.5
            yalign 0.7       
        $ counting = 0
        while counting < 20:
            $ lena_health -= 0.05
            $ counting += 1
            pause 0.01    
        ma "And it's over for poor Chief Lena who'll never fall back on her legs again after that mighty blow..."
        play sound "Sounds/winner.mp3"
        window hide
        scene fightrubywin with dissolve
        show winnersign at streetfight02
        $ renpy.pause(1, hard=True)
        ma "And so Ruby wins tonight's fight!" 
        play music "Sounds/applause.mp3"
        $ renpy.pause(2, hard=True)
        hide winnersign
        window hide
        
    if d2rollfight == 2:
        show lenasetup at center with move
        ma "Lena is the one on the attack this time..."
        scene lenarubyfight08 with dissolve
        ma ".. But Ruby grabs her on the move and holds her tight in a spine-crushing fashion!"        
        $ renpy.pause(.5, hard=True)
        show spinecrush:
            xalign 0.6
            yalign 0.6       
        $ counting = 0
        while counting < 20:
            $ lena_health -= 0.1
            $ counting += 1
            pause 0.01
        ma "That will cause a huge health loss to Lena for sure..."
        scene lenarubyfight12 with fastdissolve
        ma "But hang on, Lena manages to free herself from Ruby's hold and throws her pointy heel right in Ruby's neck!"
        $ renpy.pause(.5, hard=True)
        show heelkick:
            xalign 0.2
            yalign 0.4       
        $ counting = 0
        while counting < 20:
            $ ruby_health -= 0.1
            $ counting += 1
            pause 0.01
        ma "Virtual blood is pouring out, Ruby took a serious hit there!"
        scene fightsetup with dissolve
        show lenasetup at midleft
        show rubysetup at midright
        $ renpy.pause(1, hard=True)
        show rubysetup at center with move
        ma "Ruby makes a move..."
        scene lenarubyfight01 with fastdissolve
        ma "She's gone into berserk mode again!"
        scene lenarubyfight04
        ma "But Lena counteracts with a swift catgirl back throw!"
        scene lenarubyfight05
        ma "Followed by a neck twirl that will surely spell doom for virtual Ruby..."
        $ renpy.pause(.5, hard=True)
        play sound "Sounds/bonecrack.mp3"
        show necktwirl:
            xalign 0.5
            yalign 0.6       
        $ counting = 0
        while counting < 20:
            $ ruby_health -= 0.1
            $ counting += 1
            pause 0.01
        ma "Yes, I can confirm her neck is broken and she's a goner..."
        play sound "Sounds/winner.mp3"
        window hide
        scene fightlenawin with dissolve
        show winnersign at streetfight02
        $ renpy.pause(1, hard=True)
        ma "Which means Lena is tonight's winner of this deadly fight!" 
        play music "Sounds/applause.mp3"
        $ renpy.pause(2, hard=True)
        hide winnersign        
    label LenaRubyFightEnding:
    $ period += 1
    stop music
    hide screen screenfightlenaruby
    show screen calendar
    show screen mcstats
    if lenabet >= 1 and d2rollfight == 2:
        stop music
        stop sound
        mc "Time for me to collect my winnings!"
        scene bar02 with dissolve
        show marnie06
        show bar02b
        with fastdissolve
        ma "Ah, you want your money..."
        mc "Yep."
        hide marnie06
        hide bar02b
        show marnie01
        show bar02b
        with fastdissolve
        $ lenabetdouble = (lenabet + lenabet) - 1
        ma "I'll get it for you then. [lenabetdouble] New dollars. One dollar service fee of course. Come back next Saturday evening for another virtual fight night!"
        $ money += lenabetdouble
        mc "Nice. I can go back to my bedroom to count my money..."
        jump Bedroom
    if rubybet >= 1 and d2rollfight == 1:
        stop music
        stop sound
        mc "Time for me to collect my winnings!"
        scene bar02 with dissolve
        show marnie06
        show bar02b
        with fastdissolve
        ma "Ah, you want your money..."
        mc "Yep."
        hide marnie06
        hide bar02b
        show marnie01
        show bar02b
        with fastdissolve
        $ rubybetdouble = (rubybet + rubybet) - 1
        ma "I'll get it for you then. [rubybetdouble] New dollars. One dollar service fee of course. Come back next Saturday evening for another virtual fight night!"
        $ money += rubybetdouble
        mc "Nice. I can go back to my bedroom to count my money..."
        jump Bedroom
    if rubybet == 0 and lenabet == 0:
        mc "Oh well, it was an interesting fight. With zero stake in it for me."
        stop music
        stop sound
        jump Bedroom
    mc "Damn it! I lost my bet! Oh well, time to go back to my bedroom then..."
    stop music
    stop sound
    jump Bedroom

hide screen calendar
hide screen mcstats
if d3fightroll == 3:
    if sukicheated == False:
        menu:
            "Watch the fight between Michiko and Suki":
                jump WatchFightMichiko
            "Skip to the end (random winner)":
                $ d2rollfight=renpy.random.randint(1,2)
                play sound "Sounds/winner.mp3"
                window hide
                if d2rollfight == 1:
                    scene fightmichikowin with dissolve
                    show winnersign at streetfight02
                    $ renpy.pause(1, hard=True)
                    ma "Michiko wins tonight's fight!"    
                    play music "Sounds/applause.mp3"
                    $ renpy.pause(2, hard=True)
                    hide winnersign
                if d2rollfight == 2:            
                    scene fightsukiwin with dissolve
                    show winnersign at streetfight02
                    $ renpy.pause(1, hard=True)
                    ma "Suki wins tonight's fight!" 
                    play music "Sounds/applause.mp3"
                    $ renpy.pause(2, hard=True)
                    hide winnersign        
                jump MichikoSukiFightEnding
    label WatchFightMichiko:
    $ michiko_health = 5.0
    $ suki_health = 5.0
    show screen screenfightmichikosuki
    play sound "Sounds/barfight.mp3"
    ma "Our two contenders tonight are..."
    scene fightmichiko01 with dissolve
    ma "MICHIKO!"
    window hide
    play sound "Sounds/applause.mp3"
    show michikosign at streetfight01
    $ renpy.pause(1, hard=True)
    show michikosign:
        xalign 0.4
        yalign 0.4
    ma "And..."
    window hide
    show versussign at streetfight02
    stop sound
    play sound "Sounds/versus.mp3"
    $ renpy.pause(1, hard=True)
    show versussign:
        xalign 0.5
        yalign 0.5
    scene fightsuki01 with dissolve
    show michikosign:
        xalign 0.4
        yalign 0.4
    show versussign:
        xalign 0.5
        yalign 0.5
    ma "SUKI!"
    window hide
    play sound "Sounds/applause.mp3"
    show sukisign at streetfight03
    $ renpy.pause(1, hard=True)
    show sukisign:
        xalign 0.6
        yalign 0.6
    pause 1.0
    stop sound
    scene staredown with dissolve
    play sound "Sounds/audiencegasp.mp3"
    ma "The tension is rising as Michiko and Suki stare each other down!"
    ma "As the ref, I must ask our two contenders to go back into their fight starting position before it escalates."    
    scene fightsetup with dissolve
    show sukisetup at midright
    show michikosetup at midleft
    play sound "Sounds/three.mp3"
    show threesign at streetfight02
    $ renpy.pause(1, hard=True)
    hide threesign
    play sound "Sounds/two.mp3"
    show twosign at streetfight02
    $ renpy.pause(1, hard=True)
    hide twosign
    play sound "Sounds/one.mp3"
    show onesign at streetfight02
    $ renpy.pause(1, hard=True)
    hide onesign
    play sound "Sounds/fight.mp3"
    show fightsign at streetfight02
    $ renpy.pause(1, hard=True)
    hide fightsign
    show michikosetup at center with move
    scene michikoattack01 with dissolve
    ma "Michiko makes a move..."
    scene fightwrestling04 with dissolve
    ma "...She grabs Suki by the arms and uses brute force to slowly subdue and weaken her helpless opponent!"
    $ counting = 0
    while counting < 20:
        $ suki_health -= 0.05
        $ counting += 1
        pause 0.01
    scene michikoattack02 with dissolve
    play sound "Sounds/punch.mp3"
    $ renpy.pause(.5, hard=True)
    show headpunch:
        xalign 0.5
        yalign 0.1    
    ma "But no, look! Suki manages to free herself from Michiko's arm hold and blows a fierce uppercut at her!"
    $ counting = 0
    while counting < 20:
        $ michiko_health -= 0.05
        $ counting += 1
        pause 0.01
    ma "This fight is already on a knife's edge!"

    $ d2rollfight=renpy.random.randint(1,2)
    if sukicheated:
        $ d2rollfight = 2
    if d2rollfight == 1:
        scene fightwrestling01 with dissolve
        ma "Michiko manages to arm-wrestle Suki again."
        scene fightgiantswing01 with dissolve
        ma "And to grab her by the legs! Suki is in for a mighty swing!"
        scene fightgiantswing02 with dissolve
        show whizzturn:
            xalign 0.1
            yalign 0.4       
        ma "Yes indeed, Michiko throws her with full force against the metal chords! That's got to hurt!"
        play sound "Sounds/punch.mp3"
        $ renpy.pause(.5, hard=True)
        $ counting = 0
        while counting < 20:
            $ suki_health -= 0.1
            $ counting += 1
            pause 0.01
        scene fightsetup with dissolve
        show sukisetup at midright
        show michikosetup at midleft
        $ renpy.pause(1, hard=True)
        ma "Suki has recovered and is now back on the ring."
        show sukisetup at center with move
        ma "And she decides to make a move despite her ongoing injury. What a brave girl!"
        scene fightwrestling01 with dissolve
        ma "Who will get the upper hand this time?"
        scene fightwrestling02 with dissolve
        ma "Looks like it might be Suki after all! She's lifting Michiko up and..."
        scene fightwrestling03 with dissolve
        ma "...drops her off violently on her neck and back! Ouch!"
        play sound "Sounds/crunch.mp3"
        $ renpy.pause(.5, hard=True)
        show spinecrush:
            xalign 0.4
            yalign 0.6       
        $ counting = 0
        while counting < 20:
            $ michiko_health -= 0.1
            $ counting += 1
            pause 0.01    
        ma "Michiko is taking a serious hit to her health bar!"
        scene fightsetup with dissolve
        show sukisetup at midright
        show michikosetup at midleft
        ma "But let's see what will happen next."
        $ renpy.pause(1, hard=True)
        show michikosetup at center with move
        scene michikoattack01 with dissolve
        ma "Both contestants look EXTREMELY angry.."
        scene fightwrestling04 with dissolve
        ma "But Michiko is the angrier by the looks of it! She's got the upper hand again in this gruelling arm-hold!"
        scene michikostomp01 with dissolve
        ma "Suki is so tired she can't even fight back anymore... Michiko is stomping on her head with her pointy heels."
        $ counting = 0
        while counting < 20:
            $ suki_health -= 0.05
            $ counting += 1
            pause 0.01    
        scene michikostomp02 with dissolve
        show heelstomp:
            xalign 0.4
            yalign 0.6       
        ma "And the final blow, Suki's head is literally crushed against the floor with one mighty stomp!"
        play sound "Sounds/crunch.mp3"
        $ counting = 0
        while counting < 20:
            $ suki_health -= 0.05
            $ counting += 1
            pause 0.01    
        window hide
        play sound "Sounds/winner.mp3"
        scene fightmichikowin with dissolve
        show winnersign at streetfight02
        $ renpy.pause(1, hard=True)
        ma "Michiko wins tonight's fight!"    
        play music "Sounds/applause.mp3"
        $ renpy.pause(2, hard=True)
        hide winnersign
        
    if d2rollfight == 2:
        scene fightsetup with dissolve
        show sukisetup at midright
        show michikosetup at midleft
        $ renpy.pause(1, hard=True)
        ma "Both contestants are fighting it off once again..."
        show sukisetup at center with move
        ma "And Suki makes a move this time."        
        scene fightwrestling02 with dissolve
        ma "She grabs Michiko and lifts her up on her shoulders and..."
        scene fightwrestling03 with dissolve
        ma "...slams her off violently on her neck and back! Ouch!"
        play sound "Sounds/crunch.mp3"
        $ renpy.pause(.5, hard=True)
        show spinecrush:
        show spinecrush:
            xalign 0.4
            yalign 0.6       
        $ counting = 0
        while counting < 20:
            $ michiko_health -= 0.1
            $ counting += 1
            pause 0.01    
        ma "Michiko is taking a serious hit to her health bar!"
        scene fightsetup with dissolve
        show sukisetup at midright
        show michikosetup at midleft
        ma "But let's see what will happen next."
        $ renpy.pause(1, hard=True)
        show michikosetup at center with move
        scene michikoattack01 with dissolve
        ma "Both contestants look EXTREMELY angry.."
        scene fightwrestling01 with dissolve
        ma "They are head-to-head and arm-to-arm..."
        scene fightgiantswing01 with dissolve
        ma "But Michiko manages to lift Suki her by the legs! Suki is in for a mighty swing!"
        scene fightgiantswing02 with dissolve
        show whizzturn:
            xalign 0.1
            yalign 0.4       
        ma "Yes indeed, Michiko throws her with full force against the metal chords! That's got to hurt!"
        play sound "Sounds/punch.mp3"
        $ renpy.pause(.5, hard=True)
        $ counting = 0
        while counting < 20:
            $ suki_health -= 0.1
            $ counting += 1
            pause 0.01
        scene fightsetup with dissolve
        show sukisetup at midright
        show michikosetup at midleft
        $ renpy.pause(1, hard=True)
        ma "Suki has recovered and is now back on the ring."
        show sukisetup at center with move
        ma "And she decides to make a move despite her ongoing injury. What a brave girl!"        
        scene sukilungs01 with dissolve
        ma "Oh, just look at her jump on Michiko's back! What a Ninja move!"
        scene sukilungs02 with dissolve
        ma "This could prove costly for Michiko as Suki throws herself back and crushes her opponent's spine with her knees!"
        play sound "Sounds/crunch.mp3"
        $ renpy.pause(.5, hard=True)
        show spinecrush:
            xalign 0.5
            yalign 0.4       
        $ counting = 0
        while counting < 20:
            $ michiko_health -= 0.1
            $ counting += 1
            pause 0.01
        ma "Michiko is out for good and therefore..."
        play sound "Sounds/winner.mp3"
        window hide
        scene fightsukiwin with dissolve
        show winnersign at streetfight02
        $ renpy.pause(1, hard=True)
        ma "Suki wins tonight's fight!" 
        play music "Sounds/applause.mp3"
        $ renpy.pause(2, hard=True)
        hide winnersign        
    label MichikoSukiFightEnding:
    $ period += 1
    stop music
    hide screen screenfightmichikosuki
    show screen calendar
    show screen mcstats
    if sukibet >= 1 and d2rollfight == 2:
        stop music
        stop sound
        mc "Time for me to collect my winnings!"
        scene bar02 with dissolve
        show marnie06
        show bar02b
        with fastdissolve
        if sukicheated == False:
            ma "Ah, you want your money..."
        if sukicheated:
            ma "I'm very surprised she won... But I guess a bet is a bet."
        mc "Yep."
        hide marnie06
        hide bar02b
        show marnie01
        show bar02b
        with fastdissolve
        if sukicheated == False:
            $ sukibetdouble = (sukibet + sukibet) - 1
        if sukicheated:
            $ sukibetdouble = (sukibet + sukibet + sukibet) - 1
            $ sukifightquestdone = True
        ma "I'll get your money then. [sukibetdouble] New dollars. One dollar service fee of course. Come back next Saturday evening for another virtual fight night!"
        $ money += sukibetdouble
        mc "Nice. I can go back to my bedroom to count my money..."
        $ sukibetdouble = 0
        if sukicheated:
            $ sukicheated = False
        jump Bedroom
    if michikobet >= 1 and d2rollfight == 1:
        stop music
        stop sound
        mc "Time for me to collect my winnings!"
        scene bar02 with dissolve
        show marnie06
        show bar02b
        with fastdissolve
        ma "Ah, you want your money..."
        mc "Yep."
        hide marnie06
        hide bar02b
        show marnie01
        show bar02b
        with fastdissolve
        if marnietipfight and sukifightquestdone == False:
            $ michikobetdouble = (michikobet + michikobet/2) - 1
            $ sukifightquestdone = True
        if sukifightquestdone:
            $ michikobetdouble = (michikobet + michikobet) - 1
        ma "I'll get it for you then. [michikobetdouble] New dollars. One dollar service fee of course. Come back next Saturday evening for another virtual fight night!"
        $ money += michikobetdouble
        mc "Nice. I can go back to my bedroom to count my money..."
        $ michikobetdouble = 0
        jump Bedroom
    if michikobet >= 1 and sukicheated:
        mc "Damn it! I lost my bet! Damn Marnie scammed me with her tip..."
        stop music
        stop sound
        jump Bedroom            
    if michikobet == 0 and sukibet == 0:
        mc "Oh well, it was an interesting fight. With zero stake in it for me."
        stop music
        stop sound
        jump Bedroom
    mc "Damn it! I lost my bet! Oh well, time to go back to my bedroom then..."
    stop music
    stop sound
    jump Bedroom

label FridayParty:
play music "Sounds/barmusic.mp3"
scene bar01 with dissolve
show marnie02
ma "Oh, hi [name]! It's Friday evening, it's PARTY TIME!"
hide marnie02
show marnie01
with fastdissolve
ma "Don't hesitate to join everybody on the dance floor, I'm the DJ, and the music will ROCK!"
hide marnie01 with dissolve
label DanceChoice:
scene bar01
call screen dancechoice01
screen dancechoice01:
    modal True    
    imagebutton:
        focus_mask True
        idle "v06/leave.png"
        hover "v06/leave.png"
        action Jump ("LeaveBar")
    if marnietip >= 1 and posingpouch:
        imagebutton:
            focus_mask True
            idle "v06/gotobar.png"
            hover "v06/gotobar.png"
            action Jump ("DanceBar")    
    if knowstrip == True:
        imagebutton:
            focus_mask True
            idle "Bar/stripdooridle.png"
            hover "Bar/stripdoorhover.png"
            action Jump ("DanceStripping")
    imagebutton:
        focus_mask True
        idle "Bar/danceflooridle.png"
        hover "Bar/danceflooridle.png"
        action Jump ("DanceFloor")    

label DanceStripping:
if stripkey == False:
    "The door is locked. You can't go there on a Friday evening."
if stripkey:
    stop music
    scene stripbox01 with fade
    mc "Ah, there's a box that's normally not there. Must be it then."
    scene stripbox02 with dissolve
    mc "And here is Michiko's virtual character's cartridge... Let's take it back to Suki quickly before anyone notices..."
    scene sukicommand08 with fade
    mc "Hey Suki, I've got Michiko's cartridge!"
    su "Really? Great, hand it over, I'll code in some subtle changes to make it harder for her. And LEVEL the playing field. That's definitely NOT cheating."
    scene sukicommand04
    show sukifightcomputer
    with dissolve
    mc "I like to think of it as \"player suppression\"."
    play sound "Sounds/keyboard.mp3"
    su "And... there! Done. Put the drive back in the box and no one will be the wiser!"
    scene sukicommand03 with dissolve
    su "Thanks again for your help, [name]! I really appreciate it..."
    $ sukicheated = True
    call LustPlusSuki
    mc "I'd love to stay but I need to quickly hand the key back to Jake before he suspects something..."
    su "Okay... See you tomorrow at the fight night!"
    scene bar02
    show jakebar05
    show bar02b
    with fade
    play music "Sounds/barmusic.mp3"
    ja "Ah, there you are. You took your time."
    mc "I kept having to go back and forth because Marnie wasn't satisfied with her music choice. You know, perfectionists..."
    hide jakebar05
    hide bar02b
    show jakebar02
    show bar02b
    with dissolve
    ja "Yeah, I get that a lot with...err... Lena."
    mc "Right, right... Well, I'd better head to the dance floor now that the music has started..."
    $ stripkey = False
    jump DanceFloor

jump DanceChoice

label DanceFloor:
scene fridayparty01 with fade
if angiereunited == False:
    $ dpartyroll=renpy.random.randint(1,6)
    $ dpartyrollmusic=renpy.random.randint(1,2)
    if dpartyrollmusic == 1:
        play music "Sounds/dancemusic01.mp3"
    if dpartyrollmusic == 2:
        play music "Sounds/dancemusic03.mp3"
    mc "Wow, the dancefloor is packed! Friday night rocks!"

    if dpartyroll == 1:
        show dancingcyrl01 at left
        show dancingangie01 at right
        call screen dancing
            
    if dpartyroll == 2:
        show dancingangie01 at left
        show dancingbella01 at right
        call screen dancing

    if dpartyroll == 3:
        show dancingbella01 at left
        show dancingmichiko01 at right
        call screen dancing

    if dpartyroll == 4:
        show dancingmichiko01 at left
        show dancingayla01 at right
        call screen dancing
        
    if dpartyroll == 5:
        show dancingayla01 at left
        show dancingsuki01 at dancerightda
        call screen dancing

    if dpartyroll == 6:
        show dancingsuki01 at left
        show dancingcyrl01 at right
        call screen dancing

if angiereunited:
    $ dpartyroll=renpy.random.randint(1,5)
    $ dpartyrollmusic=renpy.random.randint(1,2)
    if dpartyrollmusic == 1:
        play music "Sounds/dancemusic01.mp3"
    if dpartyrollmusic == 2:
        play music "Sounds/dancemusic03.mp3"
    mc "Wow, the dancefloor is packed! Friday night rocks!"

    if dpartyroll == 1:
        show dancingcyrl01 at left
        show dancingbella01 at right
        call screen dancing02
            
    if dpartyroll == 2:
        show dancingbella01 at left
        show dancingmichiko01 at right
        call screen dancing02

    if dpartyroll == 3:
        show dancingmichiko01 at left
        show dancingayla01 at right
        call screen dancing02
        
    if dpartyroll == 4:
        show dancingayla01 at left
        show dancingsuki01 at dancerightda
        call screen dancing02

    if dpartyroll == 5:
        show dancingsuki01 at left
        show dancingcyrl01 at right
        call screen dancing02

label CyrlDancing:
stop music
play music "Sounds/dancemusic02.mp3"
scene fridayparty02 with dissolve
show dancingcyrl02 at danceright
show dancingmc02 at danceleft
with dissolve
cy "These unfunctional, non-descriptive limb movements are a good training for my prosthetic ligaments."
mc "Also, it's supposed to be very romantic to dance with a bloke...."
cy "I am afraid I am not familiar with this human emotion."
mc "Let me show you then..."
window hide
show dancingmc02 at farleft
show dancingcyrl02 at dancerightb
with move
cy "The proximity of your dancing body makes me feel... strange inside."
scene fridayparty02 blurred with fastdissolve
show cyrldancing05
cy "I enjoyed this pointless human activity. Especially with you by my side..."
call LustPlusCyrl
if lustcy <= 3:
    $ period += 1
    jump Bedroom    
menu:    
    "I think it's time for you to join my harem." if lustcy >= 4 and haremcy == False and cyrlharem == False and girlsinharem <= 5 and toldmissioncydone:
        hide cyrldancing05
        show cyrl02
        with fastdissolve
        cy "Your harem? What does it entail?"
        mc "Err... That you're at my sexual disposal?"
        hide cyrl02
        show cyrl04
        with fastdissolve
        cy "I am warning you. As a cyborg, I refuse to be treated as a sex object by a human."
        mc "OK. What about if I were your sex object, would that be fine with you?"
        hide cyrl04
        show cyrl05
        with fastdissolve
        cy "I suppose that would be acceptable. I agree, human friend!"        
        $ haremcy = True
        $ cyrlharem = True
        $ girlsinharem += 1
        window hide
        show haremcyrl at plus
        $ renpy.pause(2.0, hard=True)
        hide haremcyrl
        mc "I'll call you at nights, so we can get better acquainted... Sexually that is."
        hide cyrl05
        show cyrl03
        with fastdissolve
        cy "I look forward to having a human sex object. Goodbye [name]."
        $ period += 1
        jump Bedroom
    "I think it's time for you to re-join my harem." if lustcy >= 4 and haremcy == False and cyrlharem and cyrldismissed == False and girlsinharem <= 5:
        hide cyrldancing05
        show cyrl05
        with fastdissolve
        cy "Mmh... Last time, you dismissed me like a broken circuit board..."
        mc "Not this time, I swear! And I'll be EXTRA-submissive for you!"
        cy "Alright then, it is agreed."
        $ haremcy = True
        $ cyrlharem = True
        $ girlsinharem += 1
        window hide
        show haremcyrl at plus
        $ renpy.pause(2.0, hard=True)
        hide haremcyrl
        hide cyrl05
        show cyrl03
        with fastdissolve
        cy "I look forward to treating you again like a disposable human sex object. Goodbye [name]."        
        $ period += 1
        jump Bedroom
    "So did I. Even if your dance moves are pretty weird.":
        cy "Not as weird as yours, you evolved monkey."
        $ period += 1
        jump Bedroom

label AngieDancing:
stop music
play music "Sounds/dancemusic02.mp3"
scene fridayparty02 with dissolve
show dancingangie02 at dancerighta
show dancingmc02 at danceleft
with dissolve
an "Hi [name]! Look at me dancing! Yipee!"
mc "I'm looking Angie... But I need to get closer to see better..."
window hide
show dancingmc02 at farleft
show dancingangie02 at dancerightba
with move
an "I like it when you are close to me like that, it makes me feel safe..."
scene fridayparty02 blurred with fastdissolve
show angiedancing05
an "Thank you for dancing with me... I hope we can dance together again soon [name]!"
call LustPlusAngie
if lustan <= 3:
    $ period += 1
    jump Bedroom    
menu:    
    "Maybe it's time for you to join my harem... I'll take care of you and you'll be safe that way." if lustan >= 4 and hareman == False and angieharem == False and girlsinharem <= 5 and angiedatedone:
        an "I accept! What do I need to do?"
        mc "Just follow me to my bedroom and I'll show you..."
        $ hareman = True
        $ angieharem = True
        $ girlsinharem += 1
        window hide
        show haremangie at plus
        $ renpy.pause(2.0, hard=True)
        hide haremangie
        $ period += 1
        jump AngieBedroom
    "Maybe it's time for you to re-join my harem... I'll take care of you and you'll be safe that way." if lustan >= 4 and hareman == False and angieharem and angiedismissed == False and girlsinharem <= 5:
        an "I accept! I'm tired of being scared, I want to feel PROTECTED again!"
        mc "Then follow me to my bedroom and I'll show you... some unprotected SEX."
        $ hareman = True
        $ girlsinharem += 1
        window hide
        show haremangie at plus
        $ renpy.pause(2.0, hard=True)
        hide haremangie
        $ period += 1
        jump AngieBedroom
    "Next week perhaps. If I see you again...":
        an "That would be TOP ACE."
        $ period += 1
        jump Bedroom

label BellaDancing:
stop music
play music "Sounds/dancemusic02.mp3"
scene fridayparty02 with dissolve
show dancingbella02 at danceright
show dancingmc02 at danceleft
with dissolve
be "Looks like my scouting partner woud like to become my DANCE partner!"
mc "A better social relationship makes for a better professional relationship..."
be "Well, come closer and let's see if we can work on THAT relationship..."
window hide
show dancingmc02 at farleft
show dancingbella02 at dancerightb
with move
be "I think we have the beginning of a VERY GOOD professional relationship there [name]..."
scene fridayparty02 blurred with fastdissolve
show belladancing05
be "Well, the party's over, but it sure was an entertaining evening..."
call LustPlusBella
$ bellabar = True
menu:    
    "Now that we've met on the dancefloor, it's time to go on a proper date, don't you think?" if lustbe >= 2 and belladatedone == False and knowredcanyon:
        hide belladancing05
        show belladancing06
        with fastdissolve
        be "You would date me?"
        mc "Of course I would! You'll be my best date ever!"
        hide belladancing06
        show belladancing08
        with fastdissolve
        be "Which means you've had many dates before... Nevertheless, I agree."
        $ belladateon = True  
        mc "I'll pick you up in the morning and take you to the Red Canyon then!"
    "It's time for you to join my harem... So sayeth the Phallus Lord." if lustbe >= 4 and harembe == False and askedbellajoin == False and bellaharem == False and girlsinharem <= 6 and belladatedone and mcchurch >= 4:
        be "Does he now? Did he also warn you about this..."
        call BellaHarem            
    "It's time for you to re-join my harem... And be in communion with the wishes of the One-Eye." if lustbe >= 4 and harembe == False and askedbellajoin == False and bellaharem and belladismissed == False and girlsinharem <= 6:
        be "You know what I'm about to say, right?"
        mc "Not really, a girl will need to be kicked out, but who? The suspense is killing me."
        call BellaHarem
    "Then I'll hopefully meet you same place, next week.": 
        hide belladancing05
        show belladancing07
        with fastdissolve
        be "I would hope that we would meet at CHURCH before then..."
        mc "Err, yeah, sure..."
$ bellabar = False
$ period += 1
jump Bedroom

label MichikoDancing:
stop music
play music "Sounds/dancemusic02.mp3"
scene fridayparty02 with dissolve
show dancingmichiko02 at midright
show dancingmc02 at danceleft
with dissolve
mi "Don't get too close to me, you might end up knocked out on the dancefloor [name]! lol!"
mc "I'll take my chances Michiko..."
window hide
show dancingmc02 at farleft
show dancingmichiko02 at midright
with move
mi "You are a brave young boy... I won't show you how to get rid of a dance partner with an \"Ashi Barai\" move then..."
scene fridayparty02 blurred with fastdissolve
show michikodancing05
mi "Dancing always makes me horny... Especially when I dance with a young muscled STUD like you... *wink*"
call LustPlusMichiko
if lustmi <= 3:
    $ period += 1
    jump Bedroom    
menu:    
    "I think it's time for you to join my harem Michiko, don't you think?" if lustmi >= 4 and haremmi == False and michikoharem == False and girlsinharem <= 5 and michikodatedone:
        mi "I thought you would never ask! Yes I do think!"
        $ haremmi = True
        $ michikoharem = True
        $ girlsinharem += 1
        window hide
        show haremmichiko at plus
        $ renpy.pause(2.0, hard=True)
        hide haremmichiko
        mc "I'll call you at nights, so we can get better acquainted... Sexually that is."
        mi "I can't wait to see what you have in store for me [name]. *wink*."
        $ period += 1
        jump Bedroom
    "I think it's time for you to re-join my harem Michiko. For some BRUTAL fucking." if lustmi >= 4 and haremmi == False and michikoharem and michikodismissed == False and girlsinharem <= 5:
        mi "Eventhough you BRUTALLY dismissed me last time, I will gladly re-join your harem. My pussy has its needs that only YOUR MONSTERCOCK can fulfill..."
        $ haremmi = True
        $ girlsinharem += 1
        window hide
        show haremmichiko at plus
        $ renpy.pause(2.0, hard=True)
        hide haremmichiko
        mc "I'll call you when it's time for you to receive some BRUTAL pounding from it then..."
        mi "I can't wait to see what you have in store for me [name]. *wink*."
        $ period += 1
        jump Bedroom
    "And I loved dancing with a BUSTY BABE such as yourself Michiko...":
        mi "Don't flatter me too much STUD or I might just JUMP you right here and there."
        $ period += 1
        jump Bedroom

label AylaDancing:
stop music
play music "Sounds/dancemusic02.mp3"
scene fridayparty02 with dissolve
show dancingayla02 at danceright
show dancingmc02 at danceleft
with dissolve
ay "Oh, so you dance too? You're full of surprises after all..."
mc "Yeah, and I want to show YOU my moves Ayla..."
window hide
show dancingmc02 at farleft
show dancingayla02 at dancerightb
with move
ay "Don't get too close, I only danced like that with my boyf... Wow, you REALLY know how to move your body [name]!"
scene fridayparty02 blurred with fastdissolve
show ayladancing05
ay "This party reminded me of the romantic time I had with my boyf... never mind him, you were a very decent replacement... This time."
call LustPlusAyla
if lustay <= 3:
    $ period += 1
    jump Bedroom    
menu:    
    "You should join my harem... It's an exciting step up in your boring life." if lustay >= 4 and haremay == False and aylaharem == False and girlsinharem <= 5 and ayladatedone:
        if mcchurch <= 4:
            ay "No way! Your standing in the Church is not high enough and I ain't servicing a novice!"
            ay "Now let me go back to my bed. ALONE with the Phallus Lord."
            jump Bedroom
        ay "Mmmh, let me think. OK, I'm just THAT bored that I'll accept."
        mc "I'll call you later in the evenings and I'll show you some GOO-OO-OOD times..."
        $ haremay = True
        $ girlsinharem += 1
        $ aylaharem = True
        window hide
        show haremayla at plus
        $ renpy.pause(2.0, hard=True)
        hide haremayla
        ay "You'd better, cos I'm already BORED being in your harem."
        $ period += 1
        jump Bedroom           
    "Maybe it's time for you to re-join my harem... What do you say?" if lustay >= 4 and haremay == False and aylaharem and ayladismissed == False and girlsinharem <= 5:
        if mcchurch <= 4:
            ay "No way! Your standing in the Church is not high enough and I ain't servicing a novice!"
            ay "Now let me go back to my bed. ALONE with the Phallus Lord."
            return
        ay "Alright. Only cos I know it CAN be NOT BORING. Sometimes."
        $ haremay = True
        $ girlsinharem += 1
        window hide
        show haremayla at plus
        $ renpy.pause(2.0, hard=True)
        hide haremayla
        mc "That's the spirit! I'll call you later in the evenings and I'll show you some GOO-OO-OOD times..."
        $ period += 1
        jump Bedroom       
    "I hope to totally replace him one day...":
        ay "Don't count on it, you have no hope in hell!"
        $ period += 1
        jump Bedroom
$ period += 1
jump Bedroom

label SukiDancing:
stop music
play music "Sounds/dancemusic02.mp3"
scene fridayparty02 with dissolve
show dancingsuki02 at danceright
show dancingmc02 at danceleft
with dissolve
su "You're not busy saving the world from Trumpf, [name]?"
mc "Even a hero needs a break. Especially when he needs to keep company to a lonely, I mean, lovely, lady..."
window hide
show dancingmc02 at farleft
show dancingsuki02 at dancerightb
with move
su "*blushes* I much prefer dancing with you than on my own, that's for sure..."
scene fridayparty02 blurred with fastdissolve
show sukidancing05
su "Thanks for taking such good care of me tonight [name]..."
call LustPlusSuki
if lustsu <= 3:
    $ period += 1
    jump Bedroom    
menu:    
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
        mc "I'll call you at nights, you'll see, it's much better than sleeping alone, even if it can be noisy at times."
        hide sukidancing05
        show sukidancing06
        with fastdissolve
        su "At nights? But... normally... I'm sleeping. But... Right, I'll come and we'll... do stuff together."
        $ period += 1
        jump Bedroom           
    "I think it's time for you to re-join my harem Suki..." if lustsu >= 4 and haremsu == False and sukiharem and sukidismissed == False  and girlsinharem <= 5:
        hide sukidancing05
        show sukidancing06
        with fastdissolve
        su "I don't know, you kind of treated me like dirt last time..."
        mc "But that was a long time ago. All is forgotten."
        hide sukidancing06
        show sukidancing05
        with fastdissolve
        su "I think the expression is \"all is forgiven\"... But you're right, I forgive you and I accept, hoping this time you won't be such a terrible human being."
        mc "I could make promises but then I might have to break them. So let's just wish for the best."
        $ haremsu = True
        $ girlsinharem += 1
        $ sukiharem = True
        window hide
        show haremsuki at plus
        $ renpy.pause(2.0, hard=True)
        hide haremsuki
        mc "I'll call you at nights, so we can rekindle our flame and our passion for each other as harem master and harem slave."
        hide sukidancing05
        show sukidancing06
        with fastdissolve
        su "As usual, I get called and I have to come."
        mc "I'm the harem master, so it's only fair."
        $ period += 1
        jump Bedroom       
    "And hopefully one day I'll take even BETTER care of you, Suki...":
        su "I see... And WE'll see!"
        $ period += 1
        jump Bedroom
$ period += 1
jump Bedroom

label DanceBar:
scene bardance01
show bardancelenaidle
show bardancejoeidle
show bardancejakeidle
with dissolve
play music "Sounds/barmusic.mp3"
call screen dancebar01
screen dancebar01:
    modal True    
    imagebutton:
        focus_mask True
        idle "Bar/bardancelenaidle.png"
        hover "Bar/bardancelenahover.png"
        action Jump ("DanceBarLena")
    imagebutton:
        focus_mask True
        idle "Bar/bardancejakeidle.png"
        hover "Bar/bardancejakehover.png"
        action Jump ("DanceBarJake")    
    if knowstrip == True:
        imagebutton:
            focus_mask True
            idle "Bar/bardancejoeidle.png"
            hover "Bar/bardancejoehover.png"
            action Jump ("DanceBarJoe")
    imagebutton:
        focus_mask True
        idle "Icons/back.png"
        hover "Icons/back.png"
        action Jump ("DanceFloor")       
    
label DanceBarJake:
scene bar02
show jakebar01
show bar02b
with dissolve
ja "Hey there. You want to buy something to drink? Do you have any money at all?"
hide jakebar01
hide bar02b
label DanceBarJakeDialogue:
show jakebar05
show bar02b    
menu:
    "No, I'm broke actually." if money == 0:
        hide jakebar05
        hide bar02b
        show jakebar02
        show bar02b
        with fastdissolve
        ja "Then you don't get nothing. Even here, that's the way it works."
        mc "Ah, damn, I thought it was some kind of anarchist utopia..."
        hide jakebar02
        hide bar02b        
        jump DanceBar
    "I am LOADED, I'll have you know." if money >= 10:
        ja "Good. Then buy something, cos I have OTHER loaded customers I need to attend."
        jump DanceBarJakeDialogue
    "Hey buddy. Marnie sent me for the key to the strip lounge, she forgot her mp3 drive." if sukifightquest and sukifightquestdone == False:
        if jakefriend >= 4:
            hide jakebar05
            hide bar02b
            show jakebar03
            show bar02b
            with fastdissolve
            ja "Mmh, okay, I think I can trust you. Here's the key. Bring it back when you're done!"
            mc "Sure thing, buddy."
            $ stripkey = True
            jump DanceChoice
        if jakefriend <= 3:
            hide jakebar05
            hide bar02b
            show jakebar02
            show bar02b
            with fastdissolve
            ja "Why would she send someone as untrustworthy as you?"
            mc "Err... Cos she trusts me?"
            hide jakebar02
            hide bar02b
            show jakebar04
            show bar02b
            with fastdissolve            
            ja "Tell her to send someone MORE trustworthy then. I'm not giving you the key, I have RESPONSABILITIES here!"
            mc "Oooh, look who thinks he's so important... Pfff!"
            hide jakebar04
            hide bar02b
            jump DanceBarJakeDialogue
    "A fancy cocktail for me and a fancy cocktail for YOU, on ME, my friend! (- 4$)" if money >= 4 and boughtcocktailjake == False:
        ja "That's nice, I was getting thirsty actually..."
        hide jakebar05
        hide bar02b
        show jakebar03
        show bar02b
        show cocktails
        with fastdissolve        
        ja "Here you are, here's your drink. And mine."
        call FriendPlusJake
        $ money -= 4
        play sound "Sounds/drinking.mp3"
        mc "Yep, nothing like the luxurious life of a drunkard who can afford fancy cocktails..."
        $ boughtcocktailjake = True        
        hide jakebar03
        hide cocktails
        hide bar02b
        show jakebar01
        show bar02b
        with fade
        ja "I'm closing, party's over folks!"
        mc "Damn, I didn't see the time pass."
        $ period += 1
        mc "Ah, now I see it. It just passed. Better get back to my bedroom then."
        jump Bedroom
    "I was showing your wife how HUGE my muscles are the other day and...":
        hide jakebar05
        hide bar02b
        show jakebar04
        show bar02b
        with fastdissolve
        ja "What??? I ORDER you to STOP doing that!"
        mc "Oh yeah? Cos otherwise, what?"
        ja "Well, err... I won't be your friend anymore!"
        call FriendMinusJake
        hide jakebar04
        hide bar02b
        show jakebar02
        show bar02b
        with fastdissolve
        ja "See? I warned you..."
        hide jakebar02
        hide bar02b
        jump DanceBarJakeDialogue
    "Do you give useful tips like Marnie if I buy a drink?" if jaketips == False:
        hide jakebar05
        hide bar02b
        show jakebar02
        show bar02b
        with fastdissolve
        ja "No."
        hide jakebar02
        hide bar02b
        $ jaketips = True
        jump DanceBarJakeDialogue
    "Leave":
        jump DanceChoice
        
label DanceBarJoe:
scene bar03
show joebar01
with dissolve
jo "Howdy, [name]! Could I buy you a drink? Since you're not dancing with the girls..."
menu:
    "Sure, why not.":
        hide joebar01
        show joebar03
        with fastdissolve
        jo "Excellent... Let me get it for you."
        hide joebar03
        show joebar04
        with dissolve
        jo "There you go. Drink up!"
        play sound "Sounds/drinking.mp3"
        hide joebar04
        show joebar03
        with fastdissolve
        jo "So... What do you say about coming into my studio and wanking that young giant musclecock of yours for me? I'll pay you 10$ if you do..."
        mc "*hips* Y..yeah... W..Why...not. *hic*"
        jo "Excellent... Follow me then..."
        scene studio01 
        show joe01
        with fade                
        jo "Just drop your clothes, this is not a posing session, this is a WANKING session."
        mc "I'll... I'll *hic* get my money, right?"
        hide joe01
        show joe02 
        with fastdissolve
        jo "Of course you will, [name]."
        scene studio02b
        show mcpouch14 with moveinright
        with dissolve
        jo "Yeah! Already massively hard. Yummy. Let me take a pic of that monster first... For my private collection."
        play sound "Sounds/flash.mp3"
        jo "Now get on your knees and JERK IT FOR ME!"
        scene studio03b
        label MCWankSlowb:
        hide mcwank01fast
        show mcwank01slow
        call screen mcwank01slowb
        screen mcwank01slowb:
            modal True
            imagebutton:
                focus_mask True
                idle "Icons/nextidle.png"
                hover "Icons/nexthover.png"
                action Jump ("McWank01Endb")    
            imagebutton:
                focus_mask True
                idle "Icons/fasteridle.png"
                hover "Icons/fasterhover.png"
                action Jump ("MCWankFastb")
        label MCWankFastb:
        hide mcwank01slow
        show mcwank01fast
        call screen mcwank01fastb
        screen mcwank01fastb:
            modal True
            imagebutton:
                focus_mask True
                idle "Icons/nextidle.png"
                hover "Icons/nexthover.png"
                action Jump ("McWank01Endb")    
            imagebutton:
                focus_mask True
                idle "Icons/sloweridle.png"
                hover "Icons/slowerhover.png"
                action Jump ("MCWankSlowb") 

        label McWank01Endb:
        show mcpouch09
        jo "Now CUM [name]!"
        hide mcwank01slow
        hide mcwank01fast
        hide mcpouch09
        show mcpouch10
        with fastdissolve
        if persistent.cumsoundon:
            play sound "Sounds/cumming.mp3"
        mc "FUUCKK! *hic*"
        jo "Yeah, keep blasting that young cream!"
        hide mcpouch10
        show mcpouch11
        with fastdissolve
        jo "Oh, wow, your shots are getting even BIGGER!"
        jo "I want you to blast the MOST POWERFUL CUMSPRAY EVER!"
        mc "I'll tr..."
        hide mcpouch11
        show mcpouch12
        with fastdissolve
        mc "...try.... AAAHH!"
        jo "Damn boy, it's reaching way above your head! We have a WINNER!"
        hide mcpouch12
        show mcpouch13
        with fastdissolve
        jo "Yeah, now just hold that pose, I'll take a few snaps of your monster rod DRIPPING ounces of cum as a mere aftermath of that POWERFUL display of VIRILITY!"
        play sound "Sounds/flash.mp3"
        mc "What about my *hic* money?"
        jo "Yeah, yeah, gee, you're such a he-whore..."
        scene studio01 
        show joe01
        jo "Now anytime you feel in the mood... After a few drinks... Ten dollars for you per wank session... Think about it and I hope to see you here again NEXT FRIDAY!"
        $ money += 10
        $ period += 1
        mc "Can I... *hips* go dance now?"
        hide joe01
        show joe02
        with fastdissolve
        jo "Err... I don't think so, the party's over. It's night now."
        mc "Oh... I'll go back to my *hic* room then."
        jump Bedroom
    "Not now, thanks.":
        jo "Mmmh, you're scared I might try and take advantage of you?"
        mc "Yeah, kind of."
        hide joebar01
        show joebar02
        with dissolve
        jo "Well, you're not wrong, that's what I was trying to do... *sigh*"
        jump DanceBar

label DanceBarLena:
scene bar04
show lena01
with dissolve
le "You're not dancing, [name]?"
if persistent.tipson:
    show lenagymtip at tips with dissolve
    pause
    hide lenagymtip
menu:
    "Na. That's for girls. I'm a MAN.":
        hide lena01
        show lena05
        with fastdissolve
        le "You're still a BOY, [name]. You have still much to learn. And you're supposed to be building up your harem."
        if girlsinharem >= 6:
            mc "I already have plenty of girls in my harem, Chief."
            hide lena05
            show lena06
            with fastdissolve
            le "Yes, GIRLS. Not REAL WOMEN."
            mc "Are you talking about yourself, Chief?"
            hide lena06
            show lena11
            with fastdissolve
            le "Well, err... No, I meant... Maybe. I should leave, now..."
            jump DanceBar
        if girlsinharem <= 5:
            mc "It's true I have a few vacant spots left. Interested to fill them in, Chief?"
            hide lena05
            show lena03
            with fastdissolve
            le "And why would I be interested?"
            mc "Err... Cos I'm super-strong. That's what you wanted, right?"
            hide lena03
            show lena06
            with fastdissolve
            le "Oh, are you now? And can you PROVE it to me? Let's go to the gym so you can SHOW me if it's TRUE."
            menu:
                "Actually, I was about to go dancing. With girls. Not real women.":
                    hide lena06
                    show lena05
                    with fastdissolve
                    le "I see. You're scared you'll fail. It means you are NOT ready. Go and play with your girls."
                    jump DanceFloor
                "OK, I'll PROVE it to you.":
                    jump GymLenaSexy
    "My massive manhood is a hindrance when I dance.":
        hide lena01
        show lena05
        with fastdissolve
        le "Your constant bragging will get you nowhere with me."
        mc "Ah...Err. Sorry, it usually works in this type of game..."
        hide lena05
        show lena06
        with fastdissolve
        le "NOT with ME."
        jump DanceBar

label GymLenaSexy:
scene mcliftend02
show lena07
with fade
le "Let's see what you've got, young man. Get into that sexy pouch I got you, I have a surprise for you..."
mc "Okay... I was going to do that anyway."
scene mcliftnew00
mc "I'm ready to PUMP IRON with the heaviest set in human history! Just watch and BEHOLD my POWER, Chief!"
scene gym03
show lenagymlingerie02
with dissolve
le "Oh, I'll watch, don't you worry about it. But you'll have to watch ME too while you're doing your reps..."
mc "You're in lingerie Chief!"
hide lenagymlingerie02
show lenagymlingerie01
with dissolve
le "That's right. To see if you can FOCUS."
mc "Alright, just watch this..."

play music "Sounds/mcworkout.mp3"
show mcgym01b
call screen mcgymlenasexy
screen mcgymlenasexy:
    modal True
    button:
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("GymLenaSexyEnd")        
        
label GymLenaSexyEnd:
stop music
scene mcliftnew18 with dissolve
mc "See that, Chief? That's RAW TEENAGE POWER!"
le "I'm impressed so far. But..."
scene lenagymhot01 with dissolve
le "...Being able to focus on the task at hand is ESSENTIAL in your line of work... So let's see if you can still lift those heavy weights if I PRESS DOWN on them while DISTRACTING you even more..."
mc "Fuck... OK, I'll show you, Chief!"
play music "Sounds/mcworkout.mp3" 
scene lenagymhot02 with dissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with dissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with dissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with dissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with dissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with dissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with dissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
stop music
le "You're doing good, [name]! Keep going, show me how STRONG and FOCUSED you are!"             
play music "Sounds/mcworkout.mp3"
scene lenagymhot02 with fastdissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with fastdissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with fastdissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with fastdissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with fastdissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with fastdissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with fastdissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
stop music
mc "See, I did it, Chief!"
le "You can put the weight down now, [name]..."
scene lenagymhot03 with dissolve
le "I'm impressed. VERY impressed, young man! Can you feel how hard my nipples have become because of YOU?"
mc "Aaah... Something else is getting HARD, Chief!"
le "Yeah, I can feel your COCK growing bigger, naughty boy... Mmmh, yes, feel those big breasts... You deserve them as a small reward..."
scene lenagymhot04 with dissolve
play sound "Sounds/womanmoan.mp3"
mc "Oh damn, Chief, they feel so FULL and RIPE!"
le "These are a REAL WOMAN's breasts!"
play sound "Sounds/ripping.mp3"
le "What was that? You RIPPED through your jockstrap with your hardening MEGADONG?"
mc "You're making me so horny, Chief!"
scene lenagymhot05 with dissolve
le "Let me see this thing..."
mc "Not before you let me see THESE things!"
scene lenagymhot06 with dissolve
mc "Now you can look at it, Chief!"
le "Mmmh, you're so MANLY! Just the way I wanted you to become!"
scene lenagymhot07 with dissolve
le "Damn, it reaches all the way to my CHEST! Let me tease it..."
scene lenagymhot07b with fastdissolve
pause 0.3
play sound "Sounds/boymoan.mp3"
mc "AAAH..."
scene lenagymhot07 with fastdissolve
pause 0.3
scene lenagymhot07b with fastdissolve
pause 0.3
scene lenagymhot07 with fastdissolve
pause 0.3
scene lenagymhot07b with fastdissolve
pause 0.3
scene lenagymhot07 with fastdissolve
pause 0.3
scene lenagymhot07b with fastdissolve
pause 0.3
scene lenagymhot07 with fastdissolve
pause 0.3
scene lenagymhot07b with fastdissolve
pause 0.3
scene lenagymhot07 with fastdissolve
pause 0.3
scene lenagymhot07b with fastdissolve
pause 0.3
scene lenagymhot07 with fastdissolve
pause 0.3
scene lenagymhot07b with fastdissolve
pause 0.3
scene lenagymhot07 with fastdissolve
pause 0.3
scene lenagymhot07b with fastdissolve
pause 0.3
scene lenagymhot07 with fastdissolve
pause 0.3
le "And now, I want you to lift those weights with just ONE arm [name]! Do it for me and then CUM FOR ME!"
scene lenagymhotcum01 with dissolve
play sound "Sounds/mcworkout.mp3"
mc "RHAAAA!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
le "YES! What a POWERFUL blast!"
scene lenagymhotcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH, I did it, I'm so fucking pumped up!!!"
le "Damn it [name], your cum jets are GIGANTIC! You're already covering me in your hot ball-batter and it's STILL spewing with full force while lifting those weights with ONE ARM!"
scene lenagymhotcum03 with dissolve
play sound "Sounds/womanmoan.mp3"
le "That was... HOT, [name]. I... never felt this way with another man... Or boy..."
if lenahotgymlust == False:
    call LustPlusLena
    $ lenahotgymlust = True
mc "You realize now how POWERFUL I am, Chief Lena?"
le "Yes I do, I do. But let's get cleaned up, I don't want to be caught by anyone in this... position."
$ period += 1
mc "*Looks like the party's over and it's nighttime, so I'd better get back to my bedroom.*"
jump Bedroom


                               