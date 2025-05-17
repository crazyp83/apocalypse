label AylaDialogue01:
stop music
show ayla04
ay "What do you want? You'd better not be BORING..."
label AylaDialogueMenu01:
show ayla04
menu:
    "Do you know who I am?":
        hide ayla04
        show ayla03
        with fastdissolve
        ay "Some random boy who thinks he's a big shot, that's who you are!"
        mc "No, I AM a big shot. A VERY BIG SHOT!"
        ay "Whaaat-ay-ver. Talk to the hand sister."
        hide ayla03
        jump AylaDialogueMenu01
    "Tell me about yourself." if spokeayla01 == False:
        hide ayla04
        show ayla01
        with fastdissolve
        ay "And why would I want to do that?"
        menu:
            "Because you have a deep urge to open your heart to me.":
                hide ayla01
                show ayla03
                with fastdissolve
                ay "Hu-hu... Nope."
                ay "You'd better leave... We're gonna have a lesson and be BORED TO DEATH soon."
                return
            "Because we could learn from each other and grow stronger.":
                hide ayla01
                show ayla02
                with fastdissolve
                ay "Mmh... Then YOU start."
                mc "I was born in a loving family and I lost everything. You see me now as a new man starting a new life."
                ay "Go on..."
                call LustPlusAyla           
                mc "Err... By a fortunate turn of event, I ended up here, with my body exhuming raw pow...."
                hide ayla02
                show ayla06
                with fastdissolve
                ay "Yeah, yeah, ok, I get the picture."
                mc "So will you tell me about yourself?"
                hide ayla06
                show ayla01
                with fastdissolve
                ay "Alright. Unlike you, I couldn't care less about the family I lost. They were all horrible people and I HATE THEM."
                mc "Gee, you have issues girl."
                hide ayla01
                show ayla05
                with fastdissolve
                ay "And I'm working on them. I know I am a SINNER. Don't put me down arsehole!"
                mc "OK, OK. (so she's a member of the Church of the Redeeming Phallus then. At least I learnt that.)"
                hide ayla05
                $ spokeayla01 = True
                return
    "How did a girl as tiny as you survive the nuclear holocaust?":
        hide ayla04
        show ayla05
        with fastdissolve
        ay "I might be tiny, but I can headbutt your groin and it will HURT!"
        mc "Gee, calm down girlfriend."
        ay "I am NOT your girlfriend! I had a boyfriend for your information. And I plan on marrying him one day and have lots of babies!"
        mc "Oh yeah, and where is he?"
        hide ayla05
        show ayla02
        with fastdissolve
        ay "Well, err... I lost him during the war. But I'll find him."
        mc "Good luck with that. (yawn)"
        hide ayla02
        show ayla05 
        with fastdissolve
        ay "Fuck you ARSEHOLE!"
        ay "You'd better leave... We're gonna have a lesson and be BORED TO DEATH soon."
        return
    "Are you alone or do you have family with you?":
        hide ayla04
        show ayla01
        with fastdissolve
        ay "I have family... And you're not a part of it, since you're not a member of the Church."
        mc "Ah, THAT kind of family..."
        ay "You'd better leave... We're gonna have a lesson and be BORED TO DEATH soon."
        return
    "I would like to gift you a beautiful necklace that I found on my adventures." if necklace:
        ay "A necklace? The necklace I'm wearing was a gift from my boyfriend... But it's kind of lousy. Let's see it then."
        hide ayla04
        show aylanecklace
        with fastdissolve
        ay "It fits my goth look quite well actually... Better than my previous necklace. You're full of surprises [name]..."
        $ necklace = False
        call LustPlusAyla
        ay "Thank you for that gift. But you'd better leave... We're gonna have a lesson and be BORED TO DEATH soon."
        return         
    "I have a gift for you. A valuable religious relic." if pubichair >= 1:
        hide ayla04
        show ayla06
        with fastdissolve
        ay "What is it?"
        mc "Err... A Holy Pubic Hair."
        hide ayla06
        show ayla02
        with fastdissolve
        ay "It's one of your own pubic hairs, isn't it, you PERVERT?"
        mc "No, no! I have a certificate of authenticity signed by High Priestess Pythia that goes with it, I swear it's not one of mine! Although mine are pretty holy too..."
        hide ayla02
        show ayla01
        with fastdissolve
        ay "Then I accept your gift. I'll... frame it and put it above my bunk bed. Thank you [name]..."
        call LustPlusAyla
        $ pubichair -= 1
        ay "But you'd better leave now... We're gonna have a lesson and be BORED TO DEATH soon."
        return
    "I propose to UNBORE you with a hot date with me outdoors (date with Ayla tomorrow morning)" if lustay >= 2 and ayladatedone == False and knowredcanyon:
        hide ayla04
        show ayla06
        with fastdissolve
        ay "What's the point of going outdoors? It's just scorching hot out there."
        mc "The place I'm thinking of is fresh and tolerable. Trust me."
        ay "Alright, only cos I'm just sssooo BORED."
        hide ayla06
        show ayla02  
        with fastdissolve
        $ ayladateon = True  
        ay "But you'd better leave now... We're gonna have a lesson and be BORED TO DEATH soon."
        return
    "I'd like to show you something (hypnotize her, +1 lust)" if pendulum and showedpendulum == False:
        call UsePendulum
        hide ayla04
        show ayla06
        with fastdissolve
        ay "Wh...what happened... Oh, hi [name], you look... hot today..."
        call LustPlusAyla
        ay "Err... I don't know why I said that, I should go, the teacher is arriving."
        $ showedpendulum = True
        return
    "You should join my harem... It's an exciting step up in your boring life." if lustay >= 4 and haremay == False and aylaharem == False and girlsinharem <= 5 and ayladatedone:
        if mcchurch <= 4:
            hide ayla04
            show ayla05
            with fastdissolve            
            ay "No way! Your standing in the Church is not high enough and I ain't servicing a novice!"
            ay "Now leave me alone, HERETIC, the teacher is arriving."
            return
        hide ayla04
        show ayla02
        with fastdissolve                    
        ay "Mmmh, let me think. OK, I'm just THAT bored that I'll accept."
        mc "I'll call you later in the evening and I'll show you some GOO-OO-OOD times..."
        $ haremay = True
        $ girlsinharem += 1
        $ aylaharem = True
        window hide
        show haremayla at plus
        $ renpy.pause(2.0, hard=True)
        hide haremayla
        ay "You'd better, cos I'm already BORED being in your harem. And now the teacher is arriving. How boring can this day get?"
        return         
    "Maybe it's time for you to re-join my harem... What do you say?" if lustay >= 4 and haremay == False and aylaharem and ayladismissed == False and girlsinharem <= 5:
        if mcchurch <= 3:
            hide ayla04
            show ayla05
            with fastdissolve            
            ay "No way! Your standing in the Church is not high enough and I ain't servicing a novice!"
            ay "Now leave me alone, HERETIC, the teacher is arriving."
            return
        hide ayla04
        show ayla02
        with fastdissolve                    
        ay "Alright. Only cos I know it CAN be NOT BORING. Sometimes."
        $ haremay = True
        $ girlsinharem += 1
        window hide
        show haremayla at plus
        $ renpy.pause(2.0, hard=True)
        hide haremayla
        mc "That's the spirit! Oh, the teacher is arriving. See you in the evenings, Ayla."
        return         
    "My cock has reached Saint-Manhood Ayla!" if canonized and toldaylacanonized == False:
        $ toldaylacanonized = True
        hide ayla04
        show ayla02
        with fastdissolve                    
        ay "And I should care because?..."
        mc "It's the highest standing in the church for a guy! Plus, it was HUGE when I got canonized, you should have seen it."
        hide ayla02
        show ayla03
        with fastdissolve
        ay "Yeah, but I didn't, I wasn't there, was I? So, whatever..."
        mc "But... You're supposed... to..."
        ay "You're BORING me. And now the teacher is arriving. How boring can this day get?"
        return         
    "Leave her.":
        hide ayla04
        show ayla01
        with fastdissolve
        ay "Yeah, you'd better leave... We're gonna have a lesson and be BORED TO DEATH soon."
        return


