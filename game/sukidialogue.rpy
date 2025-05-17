label SukiDialogue01:
show suki02 with fastdissolve
su "Hi [name]!"
label SukiDialogueMenu01:
show suki02
menu:
    "I heard you were a good student.":
        hide suki02
        show suki01
        with fastdissolve
        su "I am. But I don't learn ANYTHING in this classroom. The courses are just... ridiculous."
        mc "What do you mean?"
        hide suki01
        show suki06
        with fastdissolve
        su "It's all about SEX all the time. Like we're just some piece of meat waiting to get impregnated. It's embarrassing."
        mc "Ah. THAT bit. Yeah, I see your point now."
        hide suki06
        show suki07
        with fastdissolve
        su "Shh. We've spoken enough and that dumb teacher is arriving. Let's go back to our seats."
        return
    "Tell me about yourself." if spokesuki01 == False:
        hide suki02
        show suki06
        with fastdissolve
        su "I'm not sure I trust you... Even if you seem like a nice boy."
        menu:
            "Why don't you trust me?" if mcdeep <= 3:
                hide suki06
                show suki05 
                with fastdissolve
                su "You're not from the Deep State. You might be a Trumspter spy for all I know..."
                menu:
                    "I'm NOT. I want to kill the motherfucker for what he did to my family as a matter of fact!" if sawmom == False and spokesuki01 == False:
                        hide suki05
                        show suki02
                        with fastdissolve
                        su "Oh really? That's great to hear. I'll definitely help you in THAT endeavor!"
                        call LustPlusSuki
                        $ spokesuki01 = True
                        su "The teacher is arriving, let's go back to out seats."
                        return
                    "Pff. What a ridiculous assumption. You're too paranoid.":
                        hide suki05
                        show suki01
                        with fastdissolve
                        su "I've already caught SEVERAL trumpster agents here. Chief Lena calls me the \"Trumpster Exterminator\" I'm warning you!"
                        su "Now go back to your seat before I OUT you for what you REALLY ARE!"
                        mc "Gee, calm down Suki, we're all on the same side here..."
                        su "I KNEW you would say that!"
                        return
                    "And if YOU were a Deep State double-agent, hey? How about THAT?":
                        su "What? I... NEVER... SHUT UP! How dare you!"
                        call LustMinusSuki
                        hide suki05
                        show suki06 
                        with fastdissolve
                        su "Now go back to your seat and stop pestering me! *sob*"
                        return
            "I understand. Deep State agents need to be careful, right?" if mcdeep >= 4 and spokesuki02 == False:
                hide suki06
                show suki02                
                su "Oh! I SEE. *wink* I'll tell you more about myself then!"
                mc "I'm all ears!"
                hide suki02
                show suki05 
                with fastdissolve
                su "You can find me in the command centre except on mornings... I monitor the whole compound via discreet cameras..."
                mc "Oh, so you know everything that goes on here then?"
                hide suki05
                show suki07 
                with fastdissolve
                su "Pretty much, yes... And I have access to the internet too. I hacked a governement satellite."
                mc "Wow, you're so smart Suki. I might come and see you if I ever need to access the Dark Web... err... for research purposes of course."
                hide suki07
                show suki06
                with fastdissolve
                su "I MIGHT let you in if you're nice to me [name]! *wink*"
                call LustPlusSuki
                su "Ssh. We've spoken enough and that dumb teacher is arriving. Let's go back to our seats before she hears us. Trumpsters should never know anything about the Deep State."
                $ spokesuki02 = True
                return
            "I understand. Deep State agents need to be careful, right?" if mcdeep >= 4 and spokesuki02:
                hide suki06
                show suki02
                with fastdissolve
                su "Yes, and we should be extra-careful with Barbara..."
                su "Actually, she's arriving. Let's go back to our seats and pretend nothing happened..."
                return 
    "What happened to you after the Apocalypse?" if spokesuki02 == False:
        $ spokesuki02 = True
        hide suki02
        show suki01
        su "I searched for my family. My seven brothers and sisters, my parents, my four grandparents..."
        menu:
            "That's a lot of ILLEGALS right there. (+1 Trumpsters)":
                call PlusTrumpster
                hide suki01
                show suki05 
                with fastdissolve
                su "What the hell is wrong with you? No empathy whatsoever, just like your CULT LEADER! Now go back to your seat and stop pestering me!"
                return
            "And? What happened to them? (+1 Deep State)":
                su "They were ALL dead! *sob* I cried for such a long time..."
                mc "Wow, that is tough, losing your entire extended family like that. I feel for you..."
                su "*sob*.. And then, I had an awakening. I was going to use my skills to get back at those who did that to my family."
                mc "Amazing, just like me. We have so much in common."
                call PlusDeep
                hide suki01
                show suki07 
                with fastdissolve
                su "And we complement each other too, since you have the muscles and... I have the brains."
                mc "Hey, I have a brain too!"
                su "Ssh. We've spoken enough and that dumb teacher is arriving. Let's go back to our seats."
                return 
    "You seem to dislike the teacher a lot.":
        hide suki02
        show suki05
        with fastdissolve
        su "Well yeah, I mean, she's a Trumpster and I'm... I've said enough."
        mc "Ah, I knew it! You're from the Deep State, right?"
        su "Maybe, what does it matter? Let's go back to our seats, Barbara is arriving and I don't want her to overhear THIS conversation..."
        return
    "I would like to gift you a beautiful necklace that I found on my adventures." if necklace:
        su "A necklace? I haven't worn one in years! That's such a nice gift, I'll try it on straight away!"
        hide suki02
        show sukinecklace with fastdissolve
        $ necklace = False
        call LustPlusSuki
        su "Thank you [name], I didn't realize you could be so romantic... And it's blue too, my favorite color..."
        su "But we've spoken enough and that dumb teacher is arriving. Let's go back to our seats."
        return         
    "I'd like to show you something (hypnotize her, +1 lust)" if pendulum and showedpendulum == False:
        hide suki02
        show suki06
        with fastdissolve
        su "Really? What is it?"
        call UsePendulum
        hide suki06
        show suki05
        with fastdissolve
        su "Wh...what happened... Oh, hi [name], you look... hot today..."
        call LustPlusSuki
        su "Err... I don't know why I said that, I should go, the teacher is arriving."
        $ showedpendulum = True
        return
    "I heard you were going to fight Michiko in Saturday's virtual fight night." if marnietipfight and sukifightquest == False and sukifightquestdone == False:
        hide suki02
        show suki01
        with fastdissolve
        su "Yeah, but it's not fair! She's already a trained professional in REAL life, so she knows all the moves and she'll humiliate me for sure..."
        mc "Maybe I could help you win this fight?"
        hide suki02
        show suki05
        with fastdissolve
        su "You would do that for me?"
        mc "Of course! I think you DESERVE to win."
        hide suki05
        show suki07
        with fastdissolve
        su "Then I need you to retrieve Michiko's fight card from the game drive."
        mc "Alright. How do I do that?"
        su "Unfortunately, Marnie keeps it but she'll never give it to you..."
        hide suki07
        show suki02
        with fastdissolve
        su "Your only chance would be on Friday evening when she locks it up in the strip lounge because she doesn't man the bar."
        mc "I see. This quest is going to be tough, but I accept the challenge!"
        window hide
        show sukiquest at posmission
        $ renpy.pause(1.0, hard=True)
        pause
        hide sukiquest
        $ sukifightquest = True
        su "Well, good luck to you, [name]. You'll get a reward of course if you succeed..."
        mc "(I'm guessing an extra lust point since she's the new harem girl in this month's update...)"
        hide suki02
        show suki06
        with fastdissolve
        su "The teacher is arriving, don't tell anyone about this... conversation."
        return
    "How about we go on a date together tomorrow morning? (date with Suki in the morning)" if lustsu  >= 3 and sukidatedone == False:
        hide suki02
        show suki07
        with fastdissolve
        su "A date? With me? I'm in!"
        $ sukidateon = True
        mc "I'll come and pick you up first thing in the morning then."
        hide suki07
        show suki06
        with fastdissolve        
        su "Promise?"
        mc "Of course, I'm a man of my word."
        su "You'd better be... Oh, the teacher is arriving.."
        return
    "I think it's time now for you to join my harem Suki..." if lustsu  >= 4 and haremsu == False and sukiharem == False and girlsinharem <= 5:
        hide suki02
        show suki07
        with fastdissolve
        su "A harem? Well... I've never been in one. But... I'll try!"
        $ haremsu = True
        $ girlsinharem += 1
        $ sukiharem = True
        window hide
        show haremsuki at plus
        $ renpy.pause(2.0, hard=True)
        hide haremsuki
        mc "I'll call you at nights. When you're done being a nerd on the computer."
        hide suki07
        show suki05
        with fastdissolve        
        su "At nights? But... normally... I'm sleeping. But... Right, I'll come and we'll... Oh, the teacher is arriving."
        return
    "I think it's time for you to re-join my harem Suki..." if lustsu >= 4 and haremsu == False and sukiharem and sukidismissed == False  and girlsinharem <= 5:
        hide suki02
        show suki05
        with fastdissolve
        su "I don't know, you kind of treated me like dirt last time..."
        mc "But that was a long time ago. All is forgotten."
        hide suki05
        show suki07
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
        mc "I'll call you at nights, so we can rekindle our flame and our passion for each other as a harem master and harem slave."
        hide suki07
        show suki01
        with fastdissolve        
        su "As usual, I get called and I have to come."
        mc "I'm the harem master, so it's only fair. Ah, the teacher is arriving..."
        return    
    "Leave her.":
        hide suki02
        show suki07
        with fastdissolve
        su "Oh, you don't want to talk to me anymore?"
        mc "Nope."
        return


