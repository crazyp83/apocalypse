label AmyDialogue01:
stop music
if pregam and pregamstart >= 3:
    show amypreggo02
else:
    show amy01
am "Hello [name], I hope you're ready for another beautiful day on our planet!"
label AmyDialogueMenu01:
if pregam and pregamstart >= 3:
    show amypreggo02
else:
    show amy01
menu:
    "You mean another dusty and scorching day in the middle of the desert?":
        if pregamstart <=2:
            hide amy01
            show amy05
            with fastdissolve
        am "You shouldn't be so pessimistic! We can do much to improve the planet. If we try..."
        am "In the meantime, let's go back to our seats, today's class is about to start."
        if pregamstart <=2:
            hide amy05
        jump AmyDialogueMenu01
    "Tell me about yourself." if spokeamy01 == False:
        hide amy01
        show amy02
        with fastdissolve
        am "And what do you want to know?"
        menu:
            "Your measurements for starters.":
                hide amy02
                show amy03
                with fastdissolve
                am "You're such a pervert, really..."
                call LustMinusAmy
                am "I'm going back to my seat now, you'd better do the same, the lesson is about to start."
                return
            "How did you end up in the compound?" if spokeamy04 == False:
                hide amy02
                show amy01
                with fastdissolve
                am "I lived just nearby on a farm with my mom and dad. But they were out on the town selling our vegetables at the organic market when the bombs starting hitting us..."
                mc "We all have stories of pain and suffering. I was actually buried under a bomb. And my whole family died too."
                hide amy01
                show amy04
                with fastdissolve
                am "Wow, that's even worse than my story! You truly are a survivor then. Which means the planet CHOSE you to survive."
                call LustPlusAmy      
                mc "Yeah, that's why I'm the HERO here."
                hide amy04
                show amy02
                with fastdissolve
                am "Yeah, sure you are [name]. Now the hero is going to have to sit in class like the rest of us and listen to some boring shit, cos Barbara is arriving..."
                $ spokeamy04 = True
                return
            "How come you're so good at mechanics?":
                hide amy02
                show amy04
                with fastdissolve
                am "Well I grew up on a farm. With lots of tractors that kept falling apart. Since my parents were on the verge of bankruptcy, I learnt from my dad and helped as much as I could."
                mc "Sounds plausible, I'm sold. What did you guys grow on that farm?"
                hide amy04
                show amy05
                with fastdissolve
                am "Mainly soybean for the Chinese Market. And that trade war with China hit us hard."
                mc "You mean Jina? I'm pretty sure it's Jina, I kept hearing that on TV."
                hide amy05
                show amy02
                with fastdissolve
                am "Err. I'm pretty certain it's pronounced China. Jina isn't a country. And neither is Nambia."
                mc "Nambia, Narnia, what's the difference anyway? I like Jina best. Sounds like..."
                hide amy02
                show amy06
                with fastdissolve
                am "...I don't want to know. And anyway, the teacher is arriving, so let's go back to our seats."
                return                
    "Would you like to go on an outdoors date with me? (date with Amy tomorrow morning)" if lustam >= 2 and amydatedone == False and knowredcanyon:
        hide amy01
        show amy04
        with fastdissolve
        am "Outdoors? And where do you have in mind?"
        mc "A beautiful place called the Red Canyon. We can go tomorrow morning if you're not too busy."
        am "Oh, I've heard of it... It's supposed to be beautiful. Agreed then!"
        hide amy01
        show amy02  
        with fastdissolve
        $ amydateon = True        
        return                
    "Fancy smoking some dope with me one of these days? I've got a nice big fat spliff to share." if spliff and spliffused == False:
        if pregam and pregamstart >= 3:
            hide amypreggo02
            show amypreggo02b
            am "I'm pregnant, come on! You're trying to tempt me and hurt our baby?"
            mc "Err, no, of course not. I won't ask you again, I promise."
            am "You'd better not... And the teacher is arriving, so let's go back to our seats."
            return
        hide amy01
        show amy04
        with fastdissolve
        am "Really? Where... did you get it? Laurie refuses to grow any of that stuff in the compound under Chief Lena's orders."
        mc "On one of my numerous exciting adventures exploring the outside world."
        hide amy04
        show amy05
        with fastdissolve
        am "You're so lucky to be a scout... I so much wish I could be one and explore the natural wonders around us... *sigh*"
        if haremam == False:
            mc "Well, if you join my harem, I can take you with me everywhere I go."
            am "I know, but it's a tough price to pay... *sigh*"
            hide amy05
            show amy02
            with fastdissolve
            am "Maybe I should forget about it with a nice spliff then. Meet me in the worskhop and ask again, cos class is about to start..."
            return
        if haremam:
            mc "I'll try and take you on some of my missions more often."
            hide amy08
            show amy04
            with fastdissolve
            am "That's nice of you, [name]! I'd... like to share that spliff with you then. Meet me in the worskhop and ask again, cos class is about to start..."
            return
    "I'm rather interested in learning more about the Club Sierra. Saving the trees and the bees seems like such a worthy endeavor in those troubled times.":
        if pregamstart <= 2:
            hide amy01
            show amy02
            with fastdissolve
        am "I am  glad to hear you say that! It is indeed! To become a devoted servant of Mother Nature, one must embrace Her."
        mc "I could sure embrace the Sierra Club... members."
        am "Let's go back to our seats, today's class is about to start."
        return
    "I would like to gift you a beautiful necklace that I found on my adventures." if necklace:
        if pregamstart <=2:
            hide amy01
            show amy05
            with fastdissolve
        am "I hope it's not some synthetic material like zircon..."
        mc "Absolutely not. It's very old and made from real gems from the far reaches of the jungle."
        am "Oh wow!"
        if pregam and pregamstart >= 3:
            hide amypreggo02
            show amynecklace
            with fastdissolve
        else:
            hide amy05
            show amynecklace
            with fastdissolve
        am "Thank you [name], it's beautiful! *kisses*"
        $ necklace = False
        call LustPlusAmy
        am "But let's go back to our seats, today's class is about to start."
        hide amynecklace
        return   
    "I collected some wild flowers for you Amy." if bouquet >= 1:
        if pregamstart <=2:
            hide amy01
            show amy02
            with fastdissolve
        am "For me, really? That is such a sweet and sierraclubby thing to do!"
        call LustPlusAmy
        mc "I couldn't be scouting without thinking about you..."
        $ bouquet -= 1
        if pregamstart <=2:
            hide amy02
            show amy04
            with fastdissolve
        am "*blush* I wish I could go with you on all these wonderful adventures in the beautiful landscapes of New America!"
        mc "Actually, most of it is just desert to be honest."
        if pregam and pregamstart >= 3:
            hide amypreggo02
            show amypreggo02b
            with fastdissolve
        else:
            hide amy04
            show amy03
            with fastdissolve        
        am "Oh, the teacher is arriving, we'll have to continue this discussion another time..."
        return
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
        hide amy03
        show amy05
        with fastdissolve        
        am "That sounds real romantic... *snickers*. But let's go back to our seats, today's class is about to start."
        return
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
        am "That sounds real romantic... *snickers*. But let's go back to our seats, today's class is about to start."
        return
    "I'd like to show you something (hypnotize her, +1 lust)" if pendulum and showedpendulum == False:
        call UsePendulum
        am "Wh...what happened... Oh, hi [name], you look... hot today..."
        call LustPlusAmy
        if pregamstart <=2:
            hide amy01
            show amy05
            with fastdissolve
        am "Err... I don't know why I said that, I should go, the teacher is arriving."
        $ showedpendulum = True
        return
    "Leave her.":
        am "Yes, let's go back to our seats, today's class is about to start."
        return
