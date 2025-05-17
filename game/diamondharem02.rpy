label FuckSukYuPaid:
hide screen mcstats
hide screen calendar
play music "v07/datemusic.mp3"
scene sukyupreharem01 with fade
sy "Hello [name], you can't get enough of my big tits, can you?"
mc "I certainly can't. Best tits in the land, Suk-Yu!"
sy "Then let me show them better to you..."
scene sukyupreharem02 with dissolve
play sound "Sounds/moaning.mp3"
sy "Ooh, I can feel something getting really BIG between my legs..."
mc "That would be my cock. Hard for YOU!"
sy "Let me suck it for you [name]. I want to hold it in my hands and feel it down my throat."
scene sukyupreblow01 with dissolve
sy "You really have the BIGGEST fuckstick in the land. Anf those balls... I just have to play with them, they are so MASSIVE.."
mc "Please Suk-Yu, just blow me, I can't stand it!"
sy "Alright big boy... I'll play with your balls and your asshole to enhance your pleasure while I give you the best blowjob of your life!"

stop music
play music "Sounds/hardsucking.mp3"
label SukyuBlowSlow:
hide sukyublowfast
show sukyublowslow
call screen sukyublowhugeslow01
screen sukyublowhugeslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukyuBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("SukyuBlowFast") 

label SukyuBlowFast:
mc "Your lips are so warm... And that finger in my ass, you're a real PRO, OOOH!"
hide sukyublowslow
show sukyublowfast
call screen sukyublowhugefast01
screen sukyublowhugefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukyuBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("SukyuBlowSlow") 

label SukyuBlowEnd:
mc "I... I think I'm about to blow my load Suk-Yu!"
stop music
scene sukyublowcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Damn it, oh my GOoooooOOOODDDD!"
with fastflash
scene sukyublowcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
sy "Yeah, keep BLASTING that white boy cream all over my Asian MILF boobs [name]!"
with fastflash
mc "I can't STOP, AAAH!"
scene sukyublowcum03 with dissolve
sy "You've COVERED me in your nasty spunk.. *slurp*"
mc "Now it's my turn to return the favor Suk-Yu. I wanna taste that sweet pussy of yours... And prep it for by rod."
scene sukyupostblow01 with dissolve
play music "Sounds/lick.mp3"
sy "OOOh, you're such a naughty boy... Licking my Asian MILF pussy like that..."
scene sukyupostblow02 with dissolve
play sound "Sounds/moaning03.ogg"
mc "Ah yes, I recognize the cliched and stereotypical ahegao face made by Asian women during sex the world over."
stop music
scene sukyupostblow03 with dissolve
mc "I think you're nice and slippery down there and therefore... READY to take on my teenage monsterdong!"
scene sukyuprestand01 with dissolve
sy "Oh I AM READY, believe it! Please FUCK ME SENSELESS!"
mc "You asked for it..."
hide sukyuprestand01
play music "Sounds/womansex02.mp3"
label SukStandSlow:
hide sukstandfast
show sukstandslow
call screen sukstandhugeslow01
screen sukstandhugeslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukStandEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("SukStandFast") 

label SukStandFast:
sy "Pound me HARDER and FASTER, I know you can do it, just pound the shit out of me!!"
hide sukstandslow
show sukstandfast
call screen sukstandhugefast01
screen sukstandhugefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukStandEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("SukStandSlow") 

label SukStandEnd:
sy "Come on, STUD! Pump a STALLION dose of cum inside me!"
stop music
scene sukstandcum01 with dissolve
play music "v07/creampie.mp3"
mc "Ohhhh, Here it comes!"
window hide
with fastflash
sy "You're delivering so much sweet young cream inside me, even after having cum so much earlier!"
scene sukstandcum02 with dissolve
mc "That's cos your hot bod is making me so HORNY, RHAAA!"
window hide
with fastflash
sy "Please, pull out and shower me with your hot spunk!"
stop music
scene sukstandcum03 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
sy "Look at the SIZE of these cumshots!"
with fastflash
mc "HUGE cumshots for a huge-titted babe, Suk-Yu, AAAH!"
with fastflash
sy "Oh fuck, this is so good! And you're such a FILTHY boy to be licking YOUR cum off my Asian MILF tits like that!"
if fuckwithdiamond == False:
    scene sukstandcumend with dissolve
    sy "That was an amazing POWERFUCK, [name]! Thanks for coming by. *wink*"
    call LustPlusSukYu
    jump EndDiamondRefuck
if fuckwithdiamond:
    scene sukstandcum04 with dissolve
    di "That was a HOT display... And watching you two got me HARD and HORNY!"
    mc "Ho-Ho... I think she means to DP you, Suk-Yu."
    sy "What, both of your big cocks at once in my poor holes?"
    di "I've got a better idea, both of our cocks at once in ONE hole. Your tight pussy!"
    menu:
        "FUCK YEAH!":            
            jump SukYuDP
        "OK, but my innocent futaphobic eyes cannot take in such a lewd display so let's skip to the end.":
            sy "Luckily, I didn't mind and you get a lust point for that scene."
            call LustPlusSukYu
            jump EndDiamondRefuck

label SukYuDP:
scene diamondheatherbackground01
show sukyupredp 
with dissolve
sy "Oh my God, how will your BIG cocks ever fit? They will STRETCH me out ssoo much!"
mc "Just give it a try. It will prep you for money-making gangbangs I reckon..."
scene diamondheatherbackground01 blurred
play music "Sounds/scarlettpound.mp3"
label SukyuDPSlow:
hide sukyudpfast
show sukyudpslow
call screen sukyudphugeslow01
screen sukyudphugeslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukyuDPEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("SukyuDPFast") 

label SukyuDPFast:
mc "Let's kick it up a notch, shall we?"
hide sukyudpslow
show sukyudpfast
call screen sukyudphugefast01
screen sukyudphugefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukyuDPEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("SukyuDPSlow") 

label SukyuDPEnd:
play sound "Sounds/moaning.mp3"    
sy "I've never been stretched so much before in my life! AAAH, I'm cumming!"
mc "I'm close..."
di "Same here, anytime..."
scene diamondheatherbackground01 blurred
show sukyudpcum01
with dissolve
play music "Sounds/splooge02.mp3"
play sound "Sounds/bothcum.mp3"
mc "...NOW, RHAAA!"
with fastflash
di "My futa cock is unloading too, OOOOH!"
with fastflash
sy "I can feel both of your cocks blasting inside me, AAAHH!"
hide sukyudpcum01
show sukyudpcum02
with dissolve
sy "You're BOTH still going so STRONG, this is the BEST FUCK EVER!"
with fastflash
sy "But I need to see those BIG cocks erupting one last time..."
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
hide sukyudpcum02
show sukyudpcum03
with dissolve
sy "Look at those thick plumes of viscous cream! Mmmh, my tits are getting covered!"
scene heathercumbackground02
show sukyudpcum04
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
sy "You're still going [name]? You're a TRUE STALLION!"
with fastflash
mc "FUCK, YEAH, AH, FUCK!!!!!"
with fastflash
mc "That's the last of it, I'm gonna faint!"
sy "Don't faint just yet. Wait for your lust point..."
call LustPlusSukYu

jump EndDiamondRefuck

label FuckHeatherPaid:
hide screen mcstats
hide screen calendar
play music "v07/datemusic.mp3"
scene heatherpreharem01 with fade
he "Hello [name], you can't get enough of my big tits, can you?"
mc "I certainly can't. Best tits in the land, Heather!"
he "Then come and fondle them..."
scene heatherpreharem02 with dissolve
play sound "Sounds/moaning.mp3"
he "Mmmh, your strong hands on my breasts feel real nice... And I can feel something getting really BIG between my legs..."
mc "That would be my cock. Hard for YOU!"
he "Let me suck it for you [name]. I want to hold it in my hands and feel it down my throat."
scene heatherpreblow01 with dissolve
he "You really have the BIGGEST fuckstick in the land. It looks so TASTY too."
mc "Please Heather, just blow me, I can't stand it!"
he "Alright big boy... I'll play with your balls and your asshole to enhance your pleasure while I give you the best blowjob of your life!"
stop music
play music "Sounds/hardsucking.mp3"
label HeatherBlowSlow:
hide heatherblowfast
show heatherblowslow
call screen heatherblowhugeslow01
screen heatherblowhugeslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HeatherBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("HeatherBlowFast") 

label HeatherBlowFast:
mc "Your lips are so warm... And that finger in my ass, you're a real PRO, OOOH!"
hide heatherblowslow
show heatherblowfast
call screen heatherblowhugefast01
screen heatherblowhugefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HeatherBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("HeatherBlowSlow") 

label HeatherBlowEnd:
mc "I... I think I'm about to blow my load Heather!"
stop music
scene heatherblowcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Damn it, oh my GOoooooOOOODDDD!"
with fastflash
scene heatherblowcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
he "Yeah, keep BLASTING that teenage boy cream all over my monster boobs [name]!"
with fastflash
mc "I can't STOP, AAAH!"
scene heatherblowcum03 with dissolve
he "You've COVERED me in your nasty spunk.. *slurp*"
mc "Now it's my turn to return the favor, Heather. I wanna taste that sweet pussy of yours... And prep it for by rod."
scene heatherpostblow01 with dissolve
play music "Sounds/lick.mp3"
he "OOOh, you're such a naughty boy... Licking my horny wet pussy like that..."
scene heatherpostblow02 with dissolve
play sound "Sounds/moaning03.ogg"
he "AAAAH! You're making me CCUUUUMMMM!"
stop music
scene heatherpostblow03 with dissolve
mc "I think you're nice and slippery now down there and therefore... READY to take on my teenage monsterdong!"
scene heatherprestand01 with dissolve
he "Oh I AM READY, believe it! Please FUCK ME SENSELESS!"
mc "You asked for it..."
hide heatherprestand01
play music "Sounds/womansex02.mp3"
label HeatherStandSlow:
hide heatherstandfast
show heatherstandslow
call screen heatherstandhugeslow01
screen heatherstandhugeslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HeatherStandEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("HeatherStandFast") 

label HeatherStandFast:
he "Pound me HARDER and FASTER, I know you can do it, just pound the shit out of me!"
hide heatherstandslow
show heatherstandfast
call screen heatherstandhugefast01
screen heatherstandhugefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HeatherStandEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("HeatherStandSlow") 

label HeatherStandEnd:
he "Come on, STUD! Pump a STALLION dose of cum inside me!"
stop music
scene heatherstandcum01 with dissolve
play music "v07/creampie.mp3"
mc "Ohhhh, Here it comes!"
window hide
with fastflash
he "You're delivering so much sweet young cream inside me, even after having cum so much earlier!"
scene heatherstandcum02 with dissolve
mc "That's cos your hot bod is making me so HORNY, RHAAA!"
window hide
with fastflash
he "Please, pull out and shower me with your hot spunk!"
stop music
scene heatherstandcum03 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
he "Look at the SIZE of these cumshots!"
with fastflash
mc "HUGE cumshots for a huge-titted babe, Heather, AAAH!"
with fastflash
he "Oh fuck, this is so good! And you're such a FILTHY boy to be licking YOUR cum off my tits like that!"
if fuckwithdiamond == False:
    scene heatherstandcumend with dissolve
    he "That was an amazing POWERFUCK, [name]! Thanks for coming by. *wink*"
    call LustPlusHeather
    jump EndDiamondRefuck

if fuckwithdiamond:
    scene heatherstandcum04 with dissolve
    di "That was a HOT display... And watching you two got me HARD and HORNY!"
    mc "Ho-Ho... I think she means to DP you, Suk-Yu."
    he "What, both of your big cocks at once in my poor holes?"
    di "I've got a better idea, both of our cocks at once in ONE hole. Your tight pussy!"
    menu:
        "FUCK YEAH!":            
            jump HeatherDP
        "OK, but my innocent futaphobic eyes cannot take in such a lewd display so let's skip to the end.":
            he "Luckily, I didn't mind and you get a lust point for that scene."
            call LustPlusHeather
            jump EndDiamondRefuck

label HeatherDP:
scene diamondheatherbackground01
show heatherpredp 
with dissolve
he "Oh my God, how will your BIG cocks ever fit? They will STRETCH me out ssoo much!"
mc "Just give it a try. It will prep you for motherhood I reckon..."
scene diamondheatherbackground01 blurred
play music "Sounds/scarlettpound.mp3"
label HeatherDPSlow:
hide heatherdpfast
show heatherdpslow
call screen heatherdphugeslow01
screen heatherdphugeslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HeatherDPEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("HeatherDPFast") 

label HeatherDPFast:
mc "Let's kick it up a notch, shall we?"
hide heatherdpslow
show heatherdpfast
call screen heatherdphugefast01
screen heatherdphugefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HeatherDPEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("HeatherDPSlow") 

label HeatherDPEnd:
play sound "Sounds/moaning.mp3"    
he "I've never been stretched so much before in my life! AAAH, I'm cumming!"
mc "I'm close..."
di "Same here, anytime..."
scene diamondheatherbackground01 blurred
show heatherdpcum01
with dissolve
play music "Sounds/splooge02.mp3"
play sound "Sounds/bothcum.mp3"
mc "...NOW, RHAAA!"
with fastflash
di "My futa cock is unloading too, OOOOH!"
with fastflash
he "I can feel both of your cocks blasting inside me, AAAHH!"
hide heatherdpcum01
show heatherdpcum02
with dissolve
he "You're BOTH still going so STRONG, this is the BEST FUCK EVER!"
with fastflash
he "But I need to see those BIG cocks erupting one last time..."
stop music
hide heatherdpcum02
show heatherdpcum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
he "Look at those thick plumes of viscous cream! Mmmh, my tits are getting covered!"
scene heathercumbackground02
show heatherdpcum04
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
he "You're still going [name]? You're a TRUE STALLION!"
with fastflash
mc "FUCK, YEAH, AH, FUCK!!!!!"
with fastflash
mc "That's the last of it, I'm gonna faint!"
he "Don't faint just yet. Wait for your lust point..."
call LustPlusHeather

label EndDiamondRefuck:
show screen mcstats
show screen calendar
scene diamondharem01
show warriorchief03
with fade
stop sound
stop music
play music "v07/diamondmusic.mp3"
if strippercatchwin and renpy.seen_image("strippercum01") == False and lustsy == 0:
    $ lustsy = 1
if strippercatchwin and renpy.seen_image("strippercum01") and lustsy <= 1:
    $ lustsy = 2    
if fuckwithdiamond == False:
    di "So, did you enjoy my harem girl?"
    mc "I sure did! I might come back again actually..."
    hide warriorchief03
    show warriorchief02
    with fastdissolve
    di "As long as you have the money.... Now let me enjoy MY harem girl alone and be gone!"
    jump BackHex43b
if fuckwithdiamond:
    di "I must say, that WAS interesting. And kinky."
    if heatherharemquest and diamondaccepted == False:
        mc "So, will you finally accept to take Heather back into your harem?"
        hide warriorchief03
        show warriorchief04
        with fastdissolve
        $ diamondaccepted = True
        di "I suppose I could give my agreement at this stage..."
        if sukyuaccepted == False:
            mc "*Now I still need to convince Suk-Yu... Probably at the stripclub in Desert Town.*"
        if sukyuaccepted:
            window hide
            show heatherquestsuccess at posmission
            $ renpy.pause(1.0, hard=True)
            pause 
            hide heatherquestsuccess
            $ heatherquestdone = True
            mc "Ah, I should go and tell Heather the good news then!"
            di "Good idea, Now let me enjoy MY harem girl alone and be gone!"
    if sukyuharemquest and diamondaccepted == False:
        mc "So, will you finally accept to take Suk-Yu back into your harem?"
        hide warriorchief03
        show warriorchief04
        with fastdissolve
        di "I suppose I could give my agreement at this stage..."
        $ diamondaccepted = True
        if heatheraccepted == False:
            mc "*Now I still need to convince Heather... Probably at the stripclub in Desert Town.*"
            hide warriorchief04
            show warriorchief01
            with fastdissolve            
            di "Now let me enjoy MY harem girl alone and be gone!"
        if heatheraccepted:
            window hide
            show sukyuquestsuccess at posmission
            $ renpy.pause(1.0, hard=True)
            pause 
            hide sukyuquestsuccess
            $ sukyuquestdone = True
            mc "Ah, I should go and tell Suk-Yu the good news then!"
            di "Good idea, Now let me enjoy MY harem girl alone and be gone!"
    jump BackHex43b
        
        
    
