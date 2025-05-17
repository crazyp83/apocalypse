label FoodUnit:
hide screen mcstats
hide screen calendar
$ loc = "food"
if stonepiece02 == False and missionge:
    scene foodunit01
    show stone02idle
    with dissolve
else:
    scene foodunit01 with dissolve
if persistent.tipson and missionge and stonepiece02 == False:
    show hexfoodtip at tips with dissolve
    pause
    hide hexfoodtip
call screen food01
screen food01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/exitidle.png"
        hover "Icons/exithover.png"
        action Jump ("FoodOut")
    if preglastart <= 3:
        imagebutton:
            focus_mask True
            idle "Science/foodlaurieidle.png"
            hover "Science/foodlauriehover.png"
            action Jump ("FoodLaurie")
    if preglastart >= 4:
        imagebutton:
            focus_mask True
            idle "v072/foodlaurieidle02.png"
            hover "v072/foodlauriehover02.png"
            action Jump ("FoodLaurie")
    if not (period == 1 or angiereunited):
        imagebutton:
            focus_mask True
            idle "Science/foodangieidle.png"
            hover "Science/foodangiehover.png"
            action Jump ("FoodAngie")
    imagebutton:
        focus_mask True
        idle "Science/foodcabinetidle.png"
        hover "Science/foodcabinethover.png"
        action Jump ("FoodCabinet")
    if stonepiece02 == False and missionge:
        imagebutton:
            focus_mask True
            idle "Icons/stone02idle.png"
            hover "Icons/stone02hover.png"
            action Jump ("StonePiece02")

label StonePiece02:
scene foodunit01
if not (period == 1 or angiereunited):
    show foodangieidle
if preglastart <= 3:
    show foodlaurieidle
if preglastart >= 4:
    show foodlaurieidle02
"You found one of the missing pieces of the Stone Artefact."
$ stonepieces -= 1
window hide
show achievementgenie at posmission
$ renpy.pause(0.5, hard=True)
show text "{font=Gui/Boogaloo-Regular.ttf}{color=#ff0000}{size=30}[stonepieces]{/font}" at StonePosition
$ renpy.pause(2.0, hard=True)
hide achievementgenie
$ stonepiece02 = True
jump FoodUnit
        
label FoodCabinet:
if not (period == 1 or angiereunited):
    show foodangieidle
if preglastart <= 3:
    show foodlaurieidle
if preglastart >= 4:
    show foodlaurieidle02
if stonepiece02 == False and missionge:
    show stone02idle
mc "It looks like a locked cabinet filled with weird plants. I wonder what they are..."
jump FoodUnit

label FoodAngie:
$ seenfood = True
scene foodunit02 with dissolve
call AngieDialogue01
if period == 2 and angiecosplayafternoon:
    jump AngieCosplay
if period == 3 and angiecosplayevening:
    jump AngieCosplay
jump FoodUnit

label FoodLaurie:
$ seenfood = True
if not (period == 1 or angiereunited):
    show foodangieidle
if preglastart <= 3:
    show laurie01
if preglastart >= 4:
    show laurie01preg
if stonepiece02 == False and missionge:
    show stone02idle
with fastdissolve
$ spokela += 1
if spokela == 1:
    jump LaurieDialogue01
if spokela >= 2:
    jump LaurieDialogue02

label LaurieDialogue01:
show screen mcstats
show screen calendar
la "Hi, I'm so glad you're back! It means you show a keen interest in our future. Would you like to taste my latest mutated carrots?"
label LaurieDialogueMenu01:
show laurie01
menu:
    "I'd rather not. I'm against GMOs.":
        hide laurie01
        show laurie03
        with fastdissolve
        la "I understand your concern but we need to increase our production since more and more people keep joining the compound..."
        hide laurie03
        show laurie05
        with fastdissolve
        la "...Which is great of course, we need to find as many survivors as possible!"
        hide laurie05
        jump LaurieDialogueMenu01
    "Sure. I'll try it.":
        hide laurie01
        show laurie02
        with fastdissolve
        la "That's so great! I'm sure you'll love it!"
        window hide
        play sound "Sounds/crunch.mp3"
        pause 2
        play sound "Sounds/pain.mp3"
        pause 2
        la "So, how was it? I hope it wasn't too bitter?"
        mc "Just a bit too bitter..."
        hide laurie02
        show laurie03
        with fastdissolve
        la "I'm so sad you didn't like it. I failed. I have to improve my cross-breeding."
        la "Perhaps you'd like to try another one?"
        menu:
            "Ok, I'll try...":
                la "Oh wow, you're so keen! I never had anyone accept to go that far!"
                call LustPlusLaurie
                window hide
                play sound "Sounds/crunch.mp3"
                pause 2
                play sound "Sounds/pain.mp3"
                pause 2
                mc "My stomach, it hurts so much, I think I'm gonna die..."
                show mcinjured at injured
                pause 1
                $ mcinjured = True
                hide laurie03
                show laurie06
                with fastdissolve
                la "I'm so sorry [name]. Oh my God, what have I done? Let me take you to the medical bay...."
                $ mcinjuredsalad = True
                jump Medbay               
            "No thanks, I had enough vegetables for the day...":
                hide laurie03
                show laurie01
                with fastdissolve
                la "Vegetables are good for you. You should try it some day *snark*..."
                la "Now if you'll excuse me, I have much work to do."
                hide laurie01
                jump FoodOut       
        jump LaurieDialogueMenu01
    "Do you have any ketchup to go with that?":
        hide laurie01
        show laurie04
        with fastdissolve
        la "Ketchup? No, I don't have any. Ketchup is disgusting, it's full of chemicals and tons of sugar, which is really bad for you!"
        hide laurie04
        jump LaurieDialogueMenu01
    "Leave":
        la "Hope to see you again soon [name]!"
        hide laurie01
        jump FoodOut

label LaurieDialogue02:
la "Hi [name]! Welcome back to the amazing world of... mutated salads. We need all hands on deck to collect this lush offering from Mother Nature!"
la "Are you willing to do YOUR part?"
label LaurieDialogueChoice02:
if preglastart <= 3:
    show laurie01 with fastdissolve
if preglastart >= 4:
    show laurie01preg with fastdissolve
menu:
    "How much does it pay?" if lauriepayasked == False:
        if preglastart <= 3:
            hide laurie01
            show laurie03
            with fastdissolve
        if preglastart >= 4:
            hide laurie01preg
            show laurie03preg
            with fastdissolve
        la "Five new dollars per shift AND... a free salad."
        mc "Yippee."
        if preglastart <= 3:
            hide laurie03 with fastdissolve
        if preglastart >= 4:
            hide laurie03preg with fastdissolve
        $ lauriepayasked = True
        jump LaurieDialogueChoice02
    "Yep, I'm willing to pick up salads all day long for a meagre pay to do my part." if lauriepayasked:
        if preglastart <= 3:
            hide laurie01
            show laurie02
            with fastdissolve
        if preglastart >= 4:
            hide laurie01preg
            show laurie02preg
            with fastdissolve
        if period == 2 and angiereunited == False:
            la "Well, that's great to hear! I'll put you in a tandem with Angie, she'll show you the ropes."
            scene foodunit02
            show angiehappy02
            with dissolve
            an "Oh, you're gonna work with ME [name]? Yippee! You'll see, it's top ACE!"
            mc "Yeah, I'm sure packing salads is absolutely mind-boggingly exciting."
            hide angiehappy02
            show angiehappy01
            with fastdissolve
            an "Just follow me and do the same as I do and you'll have so much FUN!"
            scene foodunit01
            show laurie01
            with fade
            la "Thank you for doing your part in feeding the world [name]! Here are five dollars for your labor."
            $ money += 5
            $ workedfood += 1
            if workedfood == 3:
                la "Wow, and you've already worked so often here doing menial tasks, that you just went up one notch in the best faction on the planet!"
                $ workedfood = 0
                call PlusSierra
            hide laurie01 with dissolve
            jump FoodOut
        if period == 1 or angiereunited:
            la "Well, that's great to hear. You can go and store all the salads I pick in our cold room then."
            scene foodunit02 with dissolve
            if preglastart <= 3:
                hide laurie02
                show laurie05
                with fastdissolve
            if preglastart >= 4:
                hide laurie02preg
                show laurie05preg
                with fastdissolve
            la "Just follow my lead, everytime I fill up a basket of salads, you go and take them to the store room, okay?"
            mc "Roger that. Physical labor with no intellectual challenge, that's right up my alley."
            if preglastart <= 3:
                scene foodunit01
                show laurie01
                with fade
            if preglastart >= 4:
                scene foodunit01
                show laurie01preg
                with fade
            la "Thank you for doing your part in feeding the world [name]! Here are five dollars for your labor."
            mc "Ga...gaga... I'm cold."
            $ money += 5
            $ workedfood += 1
            if workedfood == 3:
                la "Wow, and you've already worked so often here doing menial tasks, that you just went up one notch in the best faction on the planet!"
                $ workedfood = 0
                call PlusSierra
            jump FoodOut            
    "Why don't you eat some mutated salads so we can see your tits grow huge again?" if gymla >= 2:
        hide laurie01
        show laurie04
        with fastdissolve
        la "What? I... How can you say such a thing? This is so embarrassing! Please leave now [name]."
        call LustMinusLaurie
        mc "Hey, I just think you have great tits. When they're HUGE."
        la "JUST. GO."
        jump FoodOut        
    "I would like to offer you a gem necklace Laurie. For being such a courageous girl and saving the world with your salads and all that." if necklace:
        scene foodunit01 blurred
        show laurienecklace
        with dissolve
        la "Oh my God, that is the first time anyone has ever acknowledged my contribution to the compound in such a ... sweet way. Thank you [name]!"
        $ necklace = False
        call LustPlusLaurie
        la "Maybe it might even help the salads grow by sending its energy to the plants? I'll go and investigate this exciting possibility right now! See you [name] and thanks again for that wonderful gift!"        
        jump FoodOut
    "I've collected a bouquet of wild flowers for you Laurie." if bouquet >= 1:
        if preglastart <= 3:
            hide laurie01
            show laurie02
            with fastdissolve
        if preglastart >= 4:
            hide laurie01preg
            show laurie02preg
            with fastdissolve
        la "It's beautiful, thanks a lot [name]! I can already spot a couple of rare plants in that bouquet. I'll make sure to crossbreed and create yet another NEW flower!"
        call LustPlusLaurie
        mc "You make science sound like so much fun."
        if preglastart <= 3:
            hide laurie02
            show laurie03
            with fastdissolve
        if preglastart >= 4:
            hide laurie02preg
            show laurie03preg
            with fastdissolve
        la "It is! Especially when you're growing salads to SAVE THE WORLD! And now maybe some flower-salad! I'll take care of these flowers right now. Thanks again for the kind gift."
        $ bouquet -= 1
        jump FoodOut
    "I found some wild mushrooms on of my missions. You can have them." if mushrooms and mushroomoffered == False:
        $ mushrooms = False
        if preglastart <= 3:
            hide laurie01
            show laurie02
            with fastdissolve
        if preglastart >= 4:
            hide laurie01preg
            show laurie02preg
            with fastdissolve
        la "Mushrooms? Interesting... Normally, they should be highly radioactive after the nuclear winter we had. And therefore, potentially excellent for genetic engineering!"
        call LustPlusLaurie
        mc "That's exactly what I thought. Err... How radioactive exactly? I did feel some burning sensation in my hands when I picked them up..."
        if preglastart <= 3:
            hide laurie02
            show laurie03
            with fastdissolve
        if preglastart >= 4:
            hide laurie02preg
            show laurie03preg
            with fastdissolve
        la "Don't worry about it too much. If you get sick from it, you'll die a very slow and painful death for sure, so what's to worry about?"
        mc "Err... yeah, right. Nothing at all."
        $ mushroomoffered = True
        hide laurie03
        jump LaurieDialogueChoice02
    "I know a place outside where water and life abound. I could take you there on a date..." if lustla >= 2 and lauriedatedone == False and knowredcanyon:
        if preglastart <= 3:
            hide laurie01
            show laurie02
            with fastdissolve
        if preglastart >= 4:
            hide laurie01preg
            show laurie02preg
            with fastdissolve
        la "You think I could find some interesting plants there?"
        mc "Sure. As long as you wear a bikini so you can explore the area more... freely."
        if preglastart <= 3:
            hide laurie02
            show laurie03
            with fastdissolve
        if preglastart >= 4:
            hide laurie02preg
            show laurie03preg
            with fastdissolve
        la "I see... You'll be on the prowl for me while I'll be on the prowl for plants. Let's see who wins at the end..."
        if preglastart <= 3:
            hide laurie03
            show laurie01
            with fastdissolve
        if preglastart >= 4:
            hide laurie03preg
            show laurie01preg
            with fastdissolve
        $ lauriedateon = True  
        mc "I'll pick you up in the morning then!"
        la "I can't wait..."
        hide laurie01 with dissolve
        jump Main01
    "It's time, Laurie. Join my harem and make the world a better place." if laurieharem == False and lustla >= 4 and haremla == False and girlsinharem <= 5 and lauriedatedone:
        hide laurie01
        show laurie05
        with fastdissolve
        la "Well, if it's time, it's time I guess..."
        mc "I'll call you later in the evenings and I'll show you some HO-HO-HOT times!"
        $ haremla = True
        $ girlsinharem += 1
        $ laurieharem = True
        window hide
        show haremlaurie at plus
        $ renpy.pause(2.0, hard=True)
        hide haremlaurie
        hide laurie05
        show laurie02
        with fastdissolve        
        la "I see... Hopefully, as steamy as my tropical greenhouse then... *wink*"
        hide laurie02
        jump LaurieDialogueChoice02           
    "I'm ready for you to re-join my harem... But are YOU ready?" if laurieharem and lauriedismissed == False and lustla >= 4 and haremla == False and girlsinharem <= 5:
        hide laurie01
        show laurie03
        with fastdissolve
        la "Well, it is customary to offer the future born-again harem slave a present..."
        menu:
            "Offer her a bouquet of wild flowers" if bouquet >= 1:
                mc "I was not aware of this post-apocalyptic custom, but as it turns out, I DO have a beautiful bouquet of wildflowers to offer you as a token of your submissiveness."
                hide laurie03
                show laurie02
                with fastdissolve
                la "That's better! Now I AM ready to re-join your harem."
                $ haremla = True
                $ girlsinharem += 1
                window hide
                show haremlaurie at plus
                $ renpy.pause(2.0, hard=True)
                hide haremlaurie
                mc "Great! So... I'll see you at nights then for some HO-HO-HOT times!"
                la "Bye [name]!"
                hide laurie02 with dissolve
                jump Main01
            "Don't offer her anything":
                if bouquet == 0:
                    mc "Yeah, the thing is, I didn't have time to pick up some flowers for you, because I'm a very busy man, trying to save the world and all that."
                    hide laurie03
                    show laurie04
                    with fastdissolve
                    la "And I'm a very busy girl FEEDING IT. So NO DEAL. Now let me WORK."
                    hide laurie04 with dissolve
                    jump Main01                    
    "Err. Nothing.":
        if preglastart <= 3:
            hide laurie01
            show laurie05
            with fastdissolve
        if preglastart >= 4:
            hide laurie01preg
            show laurie05preg
            with fastdissolve
        la "Nothing for me. Nothing for the planet. You are an empty vessel [name]."
        mc "Hey! I'm the HERO who's gonna save the planet, remember?"
        la "Sure, I'll be waiting. *snark*"
        scene foodunit01 with dissolve
        jump Main01

label FoodOut:
    $ period += 1
if stonepiece02 == False and missionge:
    scene foodunit01
    show stone02idle
    with dissolve
else:
    scene foodunit01 with dissolve
jump Main01