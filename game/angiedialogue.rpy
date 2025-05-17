label AngieDialogue01:
stop music

show angiehappy02
an "Hi, I'm Angie! You're [name], right? I heard a LOT about you..."
label AngieDialogueMenu01:
show angiehappy02
menu:
    "Really, what did you hear exactly?" if spokeangie01 == False:
        hide angiehappy02
        show angiehappy01
        with fastdissolve
        an "That you will protect us from the bad people because you're so strong!"
        $ spokeangie01 = True
        menu:
            "That's right, and I'll kill that motherfucker Trumpf, I promise you!":
                hide angiehappy01
                show angiestanding
                with fastdissolve
                an "What? Why do you want to do such a bad thing? Mister Trumpf is also protecting us from the bad people!"
                mc "Sorry, but who the fuck are the \"bad people\" exactly according to you?"
                hide angiestanding
                show angiesad
                with fastdissolve
                an "You shouldn't swear like that, it's not nice, I didn't say anything bad..."
                mc "Okay, sorry. But I still don't get it who you think are the bad people???"
                hide angiesad
                show angiehesitant
                with fastdissolve
                an "The... the nasty people on the roads who kill everyone."
                mc "You've met some Road Warriors?"
                an "No, I don't know what they look like but I know Mister Trumpf and the nice man in grey hair with him said they were the enemy of the people."
                hide angiehesitant
                show angiesad
                with fastdissolve
                an "Also, all the people who say bad things about Mister Trumpf, so you shouldn't say bad things about him, otherwise you're the enemy of the people too!"
                hide angiesad
                show angiestanding
                with fastdissolve
                an "You're not, right?"
                mc "No, of course not, I'm the GOOD guy, remember?"
                hide angiestanding
                show angiehappy02
                with fastdissolve
                an "Of yes, that's right, and you'll protect us from the bad people, yippee!"
                mc "(She seems to be a few apples short of a fruitcake, I'd better watch out what I say around her if I want her in my harem..)"
                show angiestanding
                if loc == "school":
                    an "I think the teacher is arriving..."
                if loc == "food":
                    an "I should go back to work now..."
                return             
            "Of course I will, and if you want EXTRA protection, well, you know, I've got a nice bedroom here...":
                hide angiehappy01
                show angiestanding
                with fastdissolve
                an "What do you mean? You'll give me EXTRA protection?"
                call LustPlusAngie
                mc "Sure. If you join my harem."
                hide angiestanding
                show angiehesitant
                with fastdissolve
                an "I... I don't know yet..."
                mc "Well think about it...."
                hide angiehesitant
                show angiestanding
                with fastdissolve
                if loc == "school":
                    an "I think the teacher is arriving..."
                if loc == "food":
                    an "I should go back to work now..."
                return             
    "I don't like people talking behind my back like that.":
        hide angiehappy02
        show angiesad
        with fastdissolve
        an "I know, I don't like it either, I'm sorry I bothered you..."
        mc "I forgive you."
        hide angiesad
        jump AngieDialogueMenu01
    "I didn't hear anything about you though.":
        hide angiehappy02
        show angiehesitant
        with fastdissolve
        an "That's because I like to keep to myself. I'm a bit shy..."
        hide angiehesitant
        jump AngieDialogueMenu01
    "Why are you wearing such... clothing?" if missionan == False:
        hide angiehappy02
        show angiestanding
        with fastdissolve
        an "I had nothing on but my precious Star Angel cosplay costume when they found me."
        hide angiestanding
        show angiesad
        with fastdissolve
        an "And they don't want me to wear it, so they gave me this instead. It's the only thing I have..."
        menu:
            "Star Angel costume? What's that?":
                hide angiesad
                show angiehappy02
                with fastdissolve
                an "She's my favorite anime hero! I wish I was brave and courageous like her..."
                mc "How about you show me that costume of yours?"
                hide angiehappy02
                show angieasking
                with fastdissolve
                an "Really? You want to play with me? I'm so happy! Do you have a costume yourself?"
                mc "Err. No."
                hide angieasking
                show angiestanding
                with fastdissolve
                an "You should really get one. I don't want to play with you if you don't have a costume too."
                $ missionan = True
                window hide
                show missionan at posmission
                $ renpy.pause(4.0, hard=True)
                hide missionan                
                hide angiestanding
                show angiestanding
                with fastdissolve
                if loc == "school":
                    an "I think the teacher is arriving..."
                if loc == "food":
                    an "I should go back to work now..."
                return             
            "I've got a costume. An elephant costume. Here are the two ears and...":
                hide angiesad
                show angieshy
                with fastdissolve
                an "Eeew. That's... so naughty. And disgusting."
                call LustMinusAngie
                hide angieshy
                show angiestanding
                with fastdissolve
                if loc == "school":
                    an "I think the teacher is arriving..."
                if loc == "food":
                    an "I should go back to work now..."
                return                             
    "Are you alone or do you have family with you?":
        hide angiehappy02
        show angiesad
        with fastdissolve
        an "I'm all alone. I got separated from my family. (sniff)"
        mc "Same here. I feel your pain. But we have to be strong and fight back against those who killed our families."
        hide angiesad
        show angieasking
        with fastdissolve
        an "Your family is dead? Are you sure? Mister Trumpf promised he would re-unite all children with their families, I'm hoping he'll find mine soon!"
        menu:
            "That would be lie number 46943.":
                hide angieasking
                show angiestanding
                with fastdissolve
                an "What do you mean?"
                mc "I mean Trumpf is a big fat liar. And you shouldn't trust a word he says."
                hide angiestanding
                show angieshy
                with fastdissolve
                an "That's not nice to say bad things about Mister Trumpf..."
                call LustMinusAngie
                hide angieshy
                show angiestanding
                with fastdissolve
                if loc == "school":
                    an "I think the teacher is arriving..."
                if loc == "food":
                    an "I should go back to work now..."
                return             
            "I don't want to quash your hopes, but they are probably dead...":
                hide angieasking
                show angiesad  
                with fastdissolve
                an "NO! I don't want them to be dead!"
                mc "It's best if you try and forget about them and start a new life. With us, your new family."
                hide angiesad
                show angiehesitant
                with fastdissolve
                an "(sniff) I'll try..."
                hide angiehesitant
                show angiestanding
                with fastdissolve
                if loc == "school":
                    an "I think the teacher is arriving..."
                if loc == "food":
                    an "I should go back to work now..."
                return             
            "Maybe he will. At least you have something to hang onto.":
                hide angieasking
                show angiehappy01 
                with fastdissolve
                an "Yes, I believe in Mister Trumpf, he's such a nice man, and also the man in the grey hair with him."
                mc "Yeah, whatever."
                hide angiehappy01
                show angiestanding
                with fastdissolve
                if loc == "school":
                    an "I think the teacher is arriving..."
                if loc == "food":
                    an "I should go back to work now..."
                return
    "How about we go on a date Angie? (date with Angie tomorrow morning)" if lustan >= 2 and angiedatedone == False and knowredcanyon:
        an "Really? You want to go on a date with ME?"
        mc "I'll take you to the Red Canyon, it's beautiful you'll see..."
        hide angiehappy02
        show angiestanding
        with fastdissolve
        an "I'm so excited! I never went on a date with any boy before!"
        $ angiedateon = True        
        if loc == "school":
            an "Ooh, ooh, I think the teacher is arriving..."
        if loc == "food":
            an "I should go back to work now..."        
        return
    "I have a cosplay costume to play with you Angie!" if missionan and missionandone == False and americacostume:
        an "Really? Wow, that's ACE! Let's play today, I really want to try on my Star Angel costume and play with YOU [name]!"
        if period == 1 and not (day == 6 or day == 7):
            mc "This evening then, I have to explore the world like a true SUPER-HERO this afternoon..."
            $ angiecosplayevening = True
            return
        if period == 1 and (day == 6 or day == 7):
            if loc == "school":
                mc "Sure, I'm free this afternoon, we can play then..."
            if loc == "food":
                mc "Sure, I'm free this afternoon, I'll be in my room waiting for you then..."
            $ angiecosplayafternoon = True
            return
        if period == 3 and loc == "food":
            an "I'm done working for the evening, so let's play NOW!"
            mc "Alright, I'll get into my SUPER-HERO costume and wait for you in my room then..."
            $ angiecosplayevening = True
            return
        if period == 2 and loc == "food":
            an "I'm done working for the afternoon, so let's play NOW!"
            $ angiecosplayafternoon = True
            return            
    "Maybe it's time for you to join my harem... I'll take care of you and you'll be safe that way." if lustan >= 4 and hareman == False and angieharem == False and girlsinharem <= 5 and angiedatedone:
        an "I accept! What do I need to do?"
        mc "I'll call you later in the evening and I'll show you what it means..."
        $ hareman = True
        $ girlsinharem += 1
        $ angieharem = True
        window hide
        show haremangie at plus
        $ renpy.pause(2.0, hard=True)
        hide haremangie
        return         
    "Maybe it's time for you to re-join my harem... I'll take care of you and you'll be safe that way." if lustan >= 4 and hareman == False and angieharem and angiedismissed == False and girlsinharem <= 5:
        an "I accept! I'm tired of being scared, I want to feel PROTECTED again!"
        $ hareman = True
        $ girlsinharem += 1
        window hide
        show haremangie at plus
        $ renpy.pause(2.0, hard=True)
        hide haremangie
        mc "Great. Then, I'll protect you and I'll show you some good SEXY time too!"
        return         
    "I would like to gift you a beautiful necklace that I found on my HEROE adventures." if necklace:
        an "Really? I don't know if I deserve it..."
        mc "Just try it on, I'm sure you'll love it."
        hide angiehappy02
        show angienecklace
        with fastdissolve
        $ necklace = False
        call LustPlusAngie
        an "Thank you so much [name], I love it! It's ssoo beautiful!"
        if loc == "school":
            an "Ooh, ooh, I think the teacher is arriving..."
            scene class02 with dissolve
        if loc == "food":
            an "I should go back to work now..."        
        return         
    "I'd like to show you something (hypnotize her, +1 lust)" if pendulum and showedpendulum == False:
        hide angiehappy02
        show angiestanding
        with fastdissolve
        an "Oh, what is it? I'm so excited!"
        call UsePendulum
        hide angiestanding
        show angiehappy01
        with fastdissolve
        an "Wow, I'm, like, REALLY excited now..."
        call LustPlusAngie
        hide angiehappy01
        show angiehesitant
        with fastdissolve 
        $ showedpendulum = True
        an "Err... I don't know why I said that, I should go, the teacher is arriving."
        return
    "Leave her.":
        hide angiehappy02
        show angiestanding
        with fastdissolve
        if loc == "school":
            an "I think the teacher is arriving..."
        if loc == "food":
            an "I should go back to work now..."
        return
            
            

