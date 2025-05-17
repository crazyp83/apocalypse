label PennyStation:
pe "I need to get some gasoline for my motorbike. And the workshop."
if pennygasexplained == False:
    pe "So we'll do a detour to visit a friend of mine. She owns the very last gas station in the desert..."
    $ pennygasexplained = True

stop sound
stop music
scene station01 with dissolve
show jenna01
je "Hi Penny! Fill 'er up as usual? And a couple of jerrycans?"
pe "Sure Jenna. [name] can do this, let's get inside, I'd like to...err... check out your supplies."
hide jenna01
show jenna02
je "Of course. *wink*"
scene station02
show jenna03 at left
show pennyout03 at right
with dissolve
je "Let's move inside..."
pe "Sure. [name], you wait here, I might be a little while..."
hide jenna03
hide pennyout03
with dissolve
mc "I see, and I get to stand here in the scorching sun. I thougt I was the HERO. Pfff!"
if withnone:
    scene mctankfill with dissolve
    if girlsinharem == 0:
        mc "This game is boring. Who wants to see a guy filling up a gas tank? I should have taken a harem girl with me. If only I had one."
    if girlsinharem >= 1:
        mc "This game is boring. Who wants to see a guy filling up a gas tank? I should have taken a harem girl with me. One who would fill up the gas tank for me."
    jump StationEnd

if withan:
    mc "Hey, Angie! Why don't you make yourself useful and fill up the tank for me. I need to go and check on Penny and Jenna..."
    an "Ooh, really? You trust ME? YIPPPEE!"
    jump GasStore
if withcy:
    mc "Cyrl, why don't you make yourself useful and fill up the tank for me. I need to go and check on Penny and Jenna..."
    cy "I see... More human-cyborg exploitation. You do realize that the scorching sun might also affect MY electronic circuit boards?"
    mc "No, I didn't know that. And I don't care. Just do as you're told."
    cy "Humpf..."
    jump GasStore
if withmo:
    mc "Nancy, could you fill up the gas tank please? I need to go and check on Penny and Jenna..."
    mo "Oh, alright sweetie pie!"
    jump GasStore
if withru:
    mc "Ruby, I need to go and check on Penny and Jenna... Why don't you fill up the tank for us? That's a manly thing to do."
    ru "Which is why you don't want to do it? Fine, I'll do it, sissy boy."
    jump GasStore
if withmi:
    mc "Michiko, why don't fill up the gas tank for me? I need to go and check on Penny and Jenna..."
    mi "I don't think so! Oil destroyed the planet and I refuse to be held accountable for my past behavior by filling up tanks! You can do it yourself."
    scene mctankfill with dissolve
    mc "Alright, alright. Gee, these tree-huggers, sometimes, I swear..."
    mi "I heard what you just said!"
    jump StationEnd
if witham:
    mc "Amy, why don't fill up the gas tank for me? I need to go and check on Penny and Jenna..."
    am "You KNOW I'm a member of the Sierra Club facton and you ask me to do that? I'm your harem girl, but not a prostitute for big oil companies!"
    scene mctankfill with dissolve
    mc "Alright, alright. Gee, these tree-huggers, sometimes, I swear..."
    am "I heard what you just said!"
    jump StationEnd
if withza:
    mc "Zara, you're middle-eastern, so you know all about petrol, right?"
    za "What the hell is that supposed to mean?"
    mc "That you're going to fill up the tank for me while I go and check on Penny..."
    jump GasStore
if withay:
    mc "Ayla, why don't fill up the gas tank for me? I need to go and check on Penny and Jenna..."
    ay "Do I look like I want to do such a BORING thing? Do it yourself!"
    mc "Alright, alright. Gee, what attitude."
    jump StationEnd
if withsu:
    mc "Suki, why don't fill up the gas tank for me? I need to go and check on Penny and Jenna..."
    su "Fine, but I'm not using the compound's credit card, I'm warning you!"
    mc "Don't worry, gas is free here apparently..."
    jump GasStore
if withgw:
    mc "Gwen, why don't fill up the gas tank for me? I need to go and check on Penny and Jenna..."
    gw "Don't come moaning if the whole thing explodes on me and we all end up at the medbay."
    mc "I can cope with that."
    jump GasStore
if withma:
    mc "Marnie, why don't fill up the gas tank for me? I need to go and check on Penny and Jenna..."
    ma "Sure, and I'll syphon a quart for my personal bar use too in exchange then."
    mc "I can cope with that. Not my gas anyway."
    jump GasStore
if withcl:
    mc "Clara, why don't fill up the gas tank for me? I need to go and check on Penny and Jenna..."
    cl "Uh... Alright. I hope I don't spill any. The Phallus Lord would get quite irrate."
    mc "That's right. Every drop of gas is sacred. Every drop of gas is good."
    jump GasStore
if withla:
    mc "Laurie, why don't fill up the gas tank for me? I need to go and check on Penny and Jenna..."
    la "Sorry, but I can't touch this filthy thing. It might contaminate my salads and everyone in the compound would get sick!"
    mc "Alright, I'll do it myself then... And contaminate the compound's camel burgers."
    jump StationEnd
if withba:
    mc "Barbara, why don't fill up the gas tank for me? I need to go and check on Penny and Jenna..."
    ba "I'm a teacher, not a gas pump attendant!"
    mc "And I'm taking you out on some exciting adventures..."
    ba "Alright then, I suppose..."
    jump GasStore
if withde:
    mc "Debra, why don't fill up the gas tank for me? I need to go and check on Penny and Jenna..."
    de "I never DO menial tasks. I have underlings for THAT!"
    mc "* sigh *, I'll do it myself then..."
    de "And I'll just WATCH YOU DO IT."
    jump StationEnd

label GasStore:
$ pennystation += 1
if pennystation == 1:
    jump GasStore01
if pennystation >= 4 and harempe and gaspennylust:
    jump GasStore04
if pennystation >= 3 and lustpe >= 3 and gaspennylust == False:
    jump GasStore03
if pennystation >= 2:
    jump GasStore02

label GasStore01:
scene pennyjenna01 with dissolve
play sound "Sounds/kiss.mp3"
mc "Ooh, I see Penny has a lesbian friend here... Let's continue watching while hiding behind the door frame, this might get interesting..."
scene pennyjenna02 with dissolve
play sound "Sounds/womanmoan.mp3"
mc "Now they're really going at each other... I hope it becomes SEXUAL fast..."
scene pennyjenna03 with dissolve
play sound "Sounds/kiss.mp3"
mc "More kissing... Come on, come on..."
scene pennyjenna04 with dissolve
play sound "Sounds/lick.mp3"
mc "And bingo... Now Jenna is licking Penny's pussy while rubbing her clit through her panties. Nice."
scene pennyjenna05 with dissolve
mc "And some more pussy-licking action. Though I don't have the best viewing spot for it and I'd better leave now and not let them see me spying on them..."
jump StationEnd

label GasStore02:
scene pennyjenna06 with dissolve
mc "Here we go again... I hope it's going to be just as steamy as last time..."
scene pennyjenna07 with dissolve
play sound "Sounds/womanmoan.mp3"
mc "This time, Penny is on her knees licking Jenna's juicy pussy..."
scene pennyjenna08 with dissolve
play sound "Sounds/lick.mp3"
mc "Oh, how innovative. And rather acrobatic."
scene pennyjenna09 with dissolve
play sound "Sounds/lick.mp3"
mc "I see this gas station also stores \"bedroom items\" by the looks of it."
scene pennyjenna10 with dissolve
mc "She's really pushing that 10-inch dildo up her friend's twat with ease. But I'd better leave now and not let them see me spying on them..."
jump StationEnd

label GasStore03:
scene pennyjenna06 with dissolve
mc "Here we go again... I hope it's going to be just as steamy as last time..."
scene pennyjenna07 with dissolve
play sound "Sounds/womanmoan.mp3"
mc "This time, Penny is on her knees licking Jenna's juicy pussy..."
scene pennyjenna11 with dissolve
mc "Uh oh, I think they spotted me..."
je "Penny, I think your friend is watching us..."
scene pennyjenna11b with dissolve
pe "Well, would you see that, a peeping Tom..."
mc "I can explain! I was just...err... looking for... err..."
je "...Our pussies?"
scene pennyjenna11c with fastdissolve
pe "Yep, I think that's what he was REALLY looking for."
je "Then he needs to be punished... Get your cock out boy, we'll make you forego your obsession..."
scene pennyjenna12 with dissolve
play sound "Sounds/lick.mp3"
mc "Oh God... I didn't expect that!"
je "Now get that cock HARD!"
scene pennyjenna13 with dissolve
play sound "Sounds/lick.mp3"
mc "Dear Lord, she's gobbling my nuts!"
pe "We're gonna make you come in NO TIME!"
scene pennyjenna14 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
je "There you go! Empty yourself, boy!"
scene pennyjenna14b with fastflash
play sound "Sounds/mccum.mp3"
pe "ALL OF IT, I need you FOCUSED for our scouting mission..."
if gaspennylust == False:
    call LustPlusPenny
    $ gaspennylust = True
scene pennyjenna15 with dissolve
stop sound
play sound "Sounds/lick.mp3"
je "Hum,, the next best thing after pussy juice and there's a LOT of it!"
scene pennyjenna16 with dissolve
play sound "Sounds/lick.mp3"
pe "I'll help you... *slurp* But we have to leave soon, [name] made us late already."
je "Don't worry about the mess Penny, I'll clean *slurp* ...it up. Go on your mission."
jump StationEnd02

label GasStore04:
scene pennyjenna06 with dissolve
mc "Those raving lesbians are at it again..."
scene pennyjenna07 with dissolve
play sound "Sounds/womanmoan.mp3"
mc "I might as well make myself noticed since they are ignoring me."
scene pennyjenna11 with dissolve
je "Peeping [name] is watching us again..."
mc "I am Penny's harem Master for your information, so I'm entitled to know what she is up to behind my back!"
scene pennyjenna11c with dissolve
pe "You know very well I am bisexual. And I can indulge in pussy-grazing as much as I like, even if I'm in your harem."
mc "As your harem overlord, I invoke my \"jus pussis primae\"! That means I get to fuck Jenna in front of you."
scene pennyjenna11b with fastdissolve
je "Well, let's see if I agree with that. Bring your fat donkey-cock over here, my wannabe liege!"
scene pennyjenna17 with dissolve
play sound "Sounds/lick.mp3"
je "Mmmmh, I just love this dick. Almost makes me forget I like pussy even more."
mc "Why don't you get it down your throat for a better taste then?"
scene pennyjenna18 with dissolve
play sound "Sounds/sucking.mp3"
je "*puff* GLlluuurr..."
stop sound
play sound "Sounds/hardsucking.mp3"
scene pennyjenna19 with fastdissolve
pause 0.3
scene pennyjenna18 with fastdissolve
pause 0.2
scene pennyjenna19 with fastdissolve
pause 0.3
scene pennyjenna18 with fastdissolve
pause 0.2
scene pennyjenna19 with fastdissolve
pause 0.3
scene pennyjenna18 with fastdissolve
pause 0.2
scene pennyjenna19 with fastdissolve
pause 0.3
scene pennyjenna18 with fastdissolve
pause 0.2
scene pennyjenna19 with fastdissolve
pause 0.3
scene pennyjenna18 with fastdissolve
pause 0.2
scene pennyjenna19 with fastdissolve
pause 0.3
scene pennyjenna18 with fastdissolve
pause 0.2
pe "Yeah, you go girl. Even if I don't know how you fit this thing in your tiny mouth."
scene pennyjenna19 with fastdissolve
pause 0.3
scene pennyjenna18 with fastdissolve
pause 0.2
scene pennyjenna19 with fastdissolve
pause 0.3
scene pennyjenna18 with fastdissolve
pause 0.2
scene pennyjenna19 with fastdissolve
pause 0.3
scene pennyjenna18 with fastdissolve
pause 0.2
scene pennyjenna19 with fastdissolve
pause 0.3
scene pennyjenna18 with fastdissolve
pause 0.2
scene pennyjenna19 with fastdissolve
pause 0.3
scene pennyjenna18 with fastdissolve
pause 0.2
scene pennyjenna19 with fastdissolve
pause 0.3
scene pennyjenna18 with fastdissolve
pause 0.2
scene pennyjenna19 with fastdissolve
play sound "Sounds/mccum.mp3"
mc "Of fuck, I'm cumming...  A bit. Some pre-cum mixed with spunk... AAAH!"
scene pennyjenna20 with dissolve
je "Mmh, I made you cum prematurely my liege?"
mc "Y..Yeah. But I'm still HARD. I need to cum PROPERLY this time!"
scene pennyjennaprefuck01 with dissolve
je "Alright, your dick was so tasty that I agree for it to taste my PUSSY! SO come anf fuck me NOW!"
pe "Oooh! And I'll frig myself while watching you two go at it!"
play music "Sounds/womansex02.mp3"
label JennaSlow:
hide jennafast
hide jennapovslow
hide jennapovfast
show jennaslow
call screen jennaslow01
screen jennaslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("JennaEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("JennaFast") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("JennaPOVSlow") 

label JennaPOVSlow:
hide jennaslow
hide jennafast
hide jennapovfast
show jennapovslow
call screen jennapovslow01
screen jennapovslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("JennaEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("JennaPOVFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("JennaSlow") 

label JennaFast:
if jennafucktold == False:
    pe "Go on [name], pump your monster shaft inside her even FASTER!"
    $ jennafucktold = True
hide jennaslow
hide jennapovslow
hide jennapovfast
show jennafast
call screen jennafast01
screen jennafast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("JennaEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("JennaSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("JennaPOVFast") 

label JennaPOVFast:
hide jennaslow
hide jennafast
hide jennapovslow
show jennapovfast
call screen jennapovfast01
screen jennapovfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("JennaEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("JennaPOVSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("JennaFast") 
            
label JennaEnd:
je "Please deliver your NUTJUICE, my liege!"
mc "Anytime... Soon.... Any..."
scene pennyjennacum01 with dissolve
play sound "Sounds/mccum.mp3"
mc "...NOW! RHAAAA!"
scene pennyjennacum02 with dissolve
pe "Good, FILL HER UP! Like a gas tank. Literally."
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
scene pennyjennacum02 with fastflash
je "AAAH, he's totally whitewashing my insides with his young cream!"
scene pennyjennacum03 with dissolve
mc "And now I'm whitewashing your outsides! RHAAA!"
scene pennyjennacum03 with fastflash
pe "Look at those MONSTER plumes of spunk! You really neede to EMPTY yourself, didn't you [name]?"
scene pennyjennacum04 with dissolve
stop sound
play sound "Sounds/boymoan.mp3"
mc "Oh God, that was so GOOD..."
pe "We need to go. So tuck that monster schlong back into your trousers and let's go to whatever hex we were supposed to go to. WHile I help Jenna clean up your spunky mess."
scene pennyjenna15 with dissolve
stop sound
play sound "Sounds/lick.mp3"
je "Mmmh, Even MORE yummy boyspunk! *slurp* Don't wait around, I can cope, you can go on your... *slurp* ...mission."
mc "Alright Jenna, thanks for the gas and the... sexy fun."
jump StationEnd02
    
label StationEnd:
scene station02 with fade
play sound "Sounds/whistling.mp3"
$ renpy.pause(1, hard=True)
show pennyout03 with dissolve
mc "Ah, there you are. Found anything interesting?"
hide pennyout03
show pennyout01
with fastdissolve
pe "Err. Yes, I did. And you, did you fill up the tank and the jerrycans?"
mc "I sure did, I sure did... Let's get moving to our destination then, it's getting late."
label StationEndb:
if period == 1 and withnone:
    scene explorepenny02a
    with fade
if period == 2 and withnone:
    scene explorepenny02b
    with fade
if withmo:
    scene explorepenny02b
    show nancypennybike02
    with fade
if withmi:
    scene explorepenny02b
    show michikopennybike02
    with fade
if withan:
    scene explorepenny02b
    show angiepennybike02
    with fade
if withru:
    scene explorepenny02b
    show rubypennybike02
    with fade
if withcy:
    scene explorepenny02b
    show cyrlpennybike02
    with fade
if withza:
    scene explorepenny02b
    show zarapennybike02
    with dissolve
if witham:
    scene explorepenny02b
    show amypennybike02
    with fade
if withsu:
    scene explorepenny02b
    show sukipennybike02
    with fade
if withgw:
    scene explorepenny02b
    show gwenpennybike02
    with fade
if withma:
    scene explorepenny02b
    show marniepennybike02
    with fade
if withcl:
    scene explorepenny02b
    show clarapennybike02
    with fade
if withla:
    scene explorepenny02b
    show lauriepennybike02
    with fade
play sound "Sounds/explorepenny02.mp3"
pause 3
pe "Yee-ha!"
scene explorepenny03 with dissolve
stop sound
mc "Are we there yet?"
pe "Of course, I can ride this beast way above the non-existing speed limits."    
jump ExploreHex

label StationEnd02:
scene station02 with fade
play sound "Sounds/whistling.mp3"
$ renpy.pause(1, hard=True)
show pennyout03 with dissolve
mc "So, are we ready to go, Penny?"
hide pennyout03
show pennyout01
with fastdissolve    
pe "Yes, and you KNOW we're late, so let's hurry up, naughty boy."
jump StationEndb