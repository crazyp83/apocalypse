label LaurieFuck01:
hide screen calendar
hide screen mcstats
if pregla and preglastart >= 3:
    scene bedroom01
    show lauriepregnant03a
    with fade
    la "Oh [name], I really don't think this is a good idea..."
    mc "HO-HO-HOT SEX is NEVER a bad idea!"
    hide lauriepregnant03a
    show lauriepregnant03b
    with fastdissolve
    la "It is when the woman is PREGNANT and the man has a 20-inch MONSTERCOCK!"
    mc "But... I didn't do my haremal duty with you this week..."
    hide lauriepregnant03a
    show lauriepregnant03b
    with fastdissolve
    la "Consider it done if you just leave me alone with the baby without HURTING it."
    mc "Sure, sure. Have a good night then, Laurie....and, whatever your name is."
    la "Bye [name]."
    hide lauriepregnant03b with dissolve
    $ weekfuckedlaurie = True    
    jump Bedroom
$ alienfuck = True
$ weekfuckedlaurie = True
scene bedroom01
show laurie02
with fade
menu:
    "Run scene":
        pass
    "Skip scene":
        la "That was quick. I didn't even feel a thing."
        jump LaurieEndB
la "You're calling me VERY LATE. I have to work EARLY in the morning you know."
mc "Well, tomorrow morning is your day off cos tonight is SEXY TIME with ME! And that takes a while so you won't sleep very much... *wink*"
hide laurie02
show laurie01
with fastdissolve
la "I guess I should have known... You're an insatiable BEAST."
if persistent.tipson and mushroomoffered == False:
    show laurietip at tips with dissolve
    pause
    hide laurietip
menu:
    "That's right, and you're my harem girl so put on some sexy lingerie and come back for some HO-HO-HOT loving!":
        hide laurie01
        show laurie03
        with fastdissolve        
        la "I'll see what I have in my wardrobe for you then [name]."
        hide laurie03 with moveoutright
        jump LaurieLingerie
    "That's right, insatiable for your HO-HO-HOT BOD, Laurie!" if mushroomoffered:
        hide laurie01
        show laurie03
        with fastdissolve 
        la "Well, I created a new line of healthy food I'd like you to try to go with your insatiable appetite then."
        mc "What's that?"
        hide laurie03
        show laurie02
        with fastdissolve 
        la "A new genetically-engineered mushnip!"
        if triedmushnip == False:
            mc "What's a mushnip?"
            la "You remember those mushrooms you found? I inject their DNA into a turnip and I made a mushnip!"        
            mc "Oh, yippee. My favorite fungus vegetable. *snickers* Can't we just go for the main dish instead, your HO-HO..."
            la "Not until you try my delicious mushnip. Then, you can do whatever you want to me..."
            mc "Anything? Even anal?"
            hide laurie02
            show laurie03
            with fastdissolve 
            la "Well, I suppose, yes."
            mc "Then bring on the mushnip!"
            la "I'll bring it in a sexy outfit just for you!"
            hide laurie03 with moveoutright
            jump LaurieLingerie02
        if triedmushnip:
            mc "Same as last time?"
            la "I think I managed to improve the taste."        
            mc "Then bring on the mushnip!"
            la "I'll bring it in a sexy outfit just for you!"
            hide laurie02 with moveoutright
            jump LaurieLingerie02

label LaurieLingerie:
play music "v07/datemusic.mp3"
scene bedroom02 blurred with fade
show laurielingerie01 at center with moveinright
la "This is a bit embarrassing. I know I'm your harem girl but still, why do I have to be almost naked in front of you like that? Can't we do this in the dark?"
mc "Why hide such a hot body Laurie? In such hot lingerie..."
hide laurielingerie01
show laurielingerie02
with fastdissolve
la "I just fear I'll grow bigger suddenly and... tear my bra apart."
mc "I'll try not to excite you too much. Right now, I'm fully dressed and totally not sexy, right?"
hide laurielingerie02
show laurielingerie03
with fastdissolve
la "I guess so. I don't feel anything at the moment."
mc "Good, so you can show me more of your sexy outfit and stop trying to cover it with your hands."
hide laurielingerie03
show laurielingerie04
with fastdissolve
la "Fine, I'll turn round and show you more, at least that way I won't have to face you... And your huge muscles."
mc "What did you say? You like my big muscles, hey?"
hide laurielingerie04
show laurielingerie05
with fastdissolve
la "You KNOW I do, stop teasing me..."
mc "I've been training a lot in the gym lately and I've become super-strong. I can feel my muscles really getting BIG lately..."
window hide
show laurielingerie05 at right with move
la "Please stop... You're making me... horny... Thanks God you're not totally pumped up at the moment."
window hide
show mclaurielingerie01 at left with moveinleft
mc "Tada! I always keep some super-heavy weights around to do a little bit of exercise in my room. And get TOTALLY PUMPED UP!"
hide laurielingerie05
show laurielingerie06 at right
with fastdissolve
la "What? Please... You know what will happen if..."
hide mclaurielingerie01
show mclaurielingerie02 at left
with fastdissolve
play sound "Sounds/mcworkout.mp3"
mc "...I do that?"
hide laurielingerie06
show laurielingerie07 at right
with fastdissolve
la "Oooh... You're sssoo strong!"
hide mclaurielingerie02
show mclaurielingerie01 at left
with fastdissolve
$ renpy.pause(0.4, hard='True')    
hide mclaurielingerie01
show mclaurielingerie02 at left
with fastdissolve
$ renpy.pause(0.4, hard='True')
play sound "Sounds/mcworkout.mp3"
hide mclaurielingerie02
show mclaurielingerie01 at left
with fastdissolve
$ renpy.pause(0.4, hard='True')    
hide mclaurielingerie01
show mclaurielingerie02 at left
with fastdissolve
play sound "Sounds/mcworkout.mp3"
$ renpy.pause(0.4, hard='True')
hide mclaurielingerie02
show mclaurielingerie01 at left
with fastdissolve
$ renpy.pause(0.4, hard='True')    
hide mclaurielingerie01
show mclaurielingerie02 at left
with fastdissolve
play sound "Sounds/mcworkout.mp3"
$ renpy.pause(0.4, hard='True')
mc "This is a good workout. I love to display my strength and muscles half-naked in front of some busty babe..."
hide laurielingerie07
show laurielingerie08 at right
with fastdissolve
play sound "Sounds/womanmoan.mp3"
la "Stop it, please... You're doing it on purpose... My bra... It's expanding!"
hide mclaurielingerie02
show mclaurielingerie03 at left
with fastdissolve
mc "Stop what? Doing that?"
hide laurielingerie08
show laurielingerie09 at right
with fastdissolve
la "AAAH, NOOOOO!"
hide laurielingerie09
show laurielingerie10 at right
with fastdissolve
la "Look at what you've done to me!"
hide mclaurielingerie03
show mclaurielingerie04 at left
with fastdissolve
mc "Oh, I'm looking, I'm looking... Now look at THIS!"
hide mclaurielingerie04
show mclaurielingerie05 at left
with fastdissolve
la "Ooh, it's ssoo big... And ERECT! Is it hard for me [name]?"
mc "Of course Laurie, and it wants to feel those great big knockers of yours... While I kiss you..."
scene bedroom49 blurred
show laurielingerie11
with fastdissolve
play sound "Sounds/kiss.mp3"
la "Mmmh, this is getting less embarrassing that I thought.. Thank you for making me feel better about myself [name]."
mc "You're welcome, now hop on the bed and let's get going with some SE-AAY-AAY-XY TIME!"
stop music
jump LaurieFuckChoiceA

label LaurieLingerie02:
play music "v07/datemusic.mp3"
scene bedroom02 blurred
show lauriemcprehuge01 at left
with fade
show laurielingerie13 at right with moveinright
la "Try this [name]!"
if triedmushnip == False:
    $ triedmushnip = True
    mc "Looks... appetizing."
    hide lauriemcprehuge01
    hide laurielingerie13
    show lauriemcprehuge02 at left
    show laurielingerie14 at right
    with fastdissolve
    play sound "Sounds/eating.mp3"
    la "So? Do you like it?"
    hide lauriemcprehuge02
    show lauriemcprehuge03 at left
    with fastdissolve
    mc "It tastes like... chicken. But at least I don't feel sick from it... It has no effect whatsoe..."
    hide lauriemcprehuge03
    show lauriemcprehuge04 at left
    with fastdissolve
    mc "...What's happening?"
    hide laurielingerie14
    show laurielingerie07 at right
    with fastdissolve
    jump EndLaurieLingerie02
if triedmushnip:
    mc "I sure will, I want to grow HUGE for you!"
    hide lauriemcprehuge01
    hide laurielingerie13
    show lauriemcprehuge02 at left
    show laurielingerie14 at right
    with fastdissolve
    play sound "Sounds/eating.mp3"
    la "Wait a bit, it should take effect in about..."
    hide lauriemcprehuge02
    show lauriemcprehuge03 at left
    with fastdissolve
    mc "...Right now!"
    hide laurielingerie14
    show laurielingerie07 at right
    with fastdissolve

label EndLaurieLingerie02:
la "Oh my God, look at you... You are an absolute MUSCLE BEAST!"
hide lauriemcprehuge03
hide laurielingerie07
show lauriemcprehuge04 at left
show laurielingerie12 at right
with fastdissolve
mc "AAH, I'm growing even MORE!"
la "And your cock, it's also getting BIGGER and HARDER!"
hide lauriemcprehuge04
show mclaurielingeriehuge01 at left
with fastdissolve
la "I... I can't believe how MASSIVE you've become!"
mc "Yeah? Pretty neat, hey? Why don't you come over and I'll show my newfound POWER!"
hide mclaurielingeriehuge01
hide laurielingerie12
show mclaurielingeriehuge02
with dissolve
play sound "Sounds/kiss.mp3"
mc "And now, get undressed and wait for me on the bed..."
stop music
jump LaurieFuckChoiceB

label LaurieFuckChoiceA:
scene bedroom03b blurred
show lauriebed02
la "What are we going to do to make my huge breasts go DOWN?"
stop music
menu:
    "A serious tit-rubbing with my cock might do the trick...":
        la "Then let's rub them very VIGOROUSLY against your shaft!"
        jump LaurieTitjob
    "If I really POUND your pussy with my huge cock, it might make you less horny.":
        la "Alright, that is a scientifically sound argument. Let's do it!"
        mc "So lay on your back and let me do the fucking..."
        jump LaurieFuck
    "Get on my cock and ride me really hard.":
        la "How is that going to help my tits go down in size?"
        mc "They'll be bouncing up and down all over the place, so it definitely SHOULD help. Anyway, don't argue, let's do it, you have nothing to lose!"
        jump LaurieRide
    "I'm done. And you'll get back to normal while we sleep. I assume.":
        la "I certainly hope so, I can't go to work with such huge knockers hindering me!"        
        jump LaurieEndA

label LaurieTitjob:
scene lauriepretitfuck01 with dissolve
mc "First, let me dive my head in those soft melons..."
play sound "Sounds/moaning02.mp3"
la "Mmmh, I'm not sure this is going to make me LESS horny [name]..."
scene lauriepretitfuck02 with dissolve
mc "You're horny are you, Laurie? Horny for my alpha-bullcock and huge muscles?"
la "Don't... Don't say that, you know I am!"
scene lauriepretitfuck03 with dissolve
mc "Then if you are, it's time for me to slide it between those huge breasts."
la "I'll push my hands against them to make it nice and tight for you..."
stop sound
play channel1 "Sounds/wank.mp3"
play channel2 "Sounds/moaning03.ogg"
label LaurieTitFuckSlow:
hide laurietitfuckfast
show laurietitfuckslow
call screen laurietitfuckslow01
screen laurietitfuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieTitFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LaurieTitFuckFast") 

label LaurieTitFuckFast:
la "Do my MASSIVE boobs feel nice, tightly wrapped around your pummeling monster pole, [name]?"
mc "Oh God, of course they do, they're the BEST!"
hide laurietitfuckslow
show laurietitfuckfast
call screen laurietitfuckfast01
screen laurietitfuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieTitFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LaurieTitFuckSlow") 

label LaurieTitFuckEnd:
mc "It's so good, I think I'm about to..."
stop channel1
stop channel2
scene laurietitfuckcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "....blow my load! AAAH!"
with fastflash
la "[name]! Your cumshots are going so FAR!"
scene laurietitfuckcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "That's cos my balls are so POWERFUL! RHAAA!"
with fastflash
la "MORE for me? I'm getting caked in your scalding cum!"
with fastflash
mc "The mast few shots for you Laurie, OOOOHH GODDAM!"
stop sound
scene laurietitfuckcum03 with dissolve
play sound "Sounds/lick.mp3"
la "Mmmh, it's so tasty... I hope slurping it eat up will help me get back to normal..."
mc "Didn't we already try that once and it didn't work? Plus, my cock is going to get hard again in no time so let's move on..."
jump LaurieFuckChoiceA

label LaurieFuck:
scene lauriehugeprefuck01 with dissolve
play sound "Sounds/moaning02.mp3"
la "What... What are you doing? Oooh, your fingers rubbing on my clit..."
mc "Just making sure you're nice and slippery for my huge shaft..."
scene lauriehugeprefuck02 with dissolve
la "[name]! You're supposed to make me LESS horny! This... is making me ssoo WET!"
play sound "Sounds/moaning.mp3"
mc "Oh well, too bad. Your tits will remain MASSIVE when I fuck you then."
scene lauriehugefuck00 with dissolve
mc "Which is NOW!"
play music "Sounds/womansex02.mp3"
label LaurieFuckSlow:
hide lauriefuckfast
show lauriefuckslow
call screen lauriefuckslow01
screen lauriefuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LaurieFuckFast") 

label LaurieFuckFast:
mc "Those MONSTER tits of yours... Just make me want to pound that tight warm pussy even FASTER!"
hide lauriefuckslow
show lauriefuckfast
call screen lauriefuckfast01
screen lauriefuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LaurieFuckSlow") 

label LaurieFuckEnd:
la "AAAH.. *puff* My tits aren't going *puff* down [name], OOOOH!"
mc "Yeah, but you're enjoying yourself, aren't you? And I'm about to hit MY climax soon too after this HEAVY PUSSY-POUNDING!"
stop music
play music "Sounds/splooge02.mp3"
scene lauriehugefuckcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Like RIGHT NOW! AAAH!"
with fastflash
la "You're PUMPING me full of virile seed, ready to fertilize the world! AAAH!"
scene lauriehugefuckcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "MORE, I NEED TO UNLOAD MOOORRRE!"
with fastflash
la "Your sweet ball-batter is so hot, it's making sssooo HORNY!"
scene lauriehugefuckcum03 with dissolve
mc "Fuck me, your tits, they're growing while I'm FLOODING your tight pussy!"
with fastflash
la "Nooo! I'm too horny, it won't stop!"
stop music
scene lauriehugefuckcum04 with dissolve
mc "Phew, I'm done spewing, and yours tits are done growing. And now they are like two ENORMOUS MILK-BALLOONS!"
la "This is so embarrassing! This fucking was supposed to make them go down, do something please [name]!"
scene lauriemega00 with dissolve
mc "Seeing your ginormous titties like that makes me think of only one thing. FUCKING YOU SOME MORE!"
play music "Sounds/womansex01.mp3"
label LaurieMegaSlow:
hide lauriemegafast
show lauriemegaslow
call screen lauriemegaslow01
screen lauriemegaslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieMegaEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LaurieMegaFast") 

label LaurieMegaFast:
mc "I just can't stop PUMMELLING that warm pussy!"
la "Your cock is just so big, my enhanced breast are jiggling everywhere!"
hide lauriemegaslow
show lauriemegafast
call screen lauriemegafast01
screen lauriemegafast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieMegaEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LaurieMegaSlow") 

label LaurieMegaEnd:
mc "I'm about to blow my load again, Laurie, get ready for another REFILL!"
la "I don't know if my battered womb can hold anymore of your spunk but I'll be glad to be showevered with another dose of your young cum!"
stop music
scene lauriemegacum01 with dissolve
play music "Sounds/splooge02.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "That's it, HERE IT COMES!"
with fastflash
la "You're coming so much AGAIN! Plaster my huge tits with it, please [name]!"
stop music
scene lauriemegacum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "There you go, another few OUNCES for you Laurie!"
with fastflash
la "Your boulders are just a cum factory, aren't they? It's SPLASHING everywhere!"
scene lauriemegacum03 with dissolve
play sound "Sounds/moaning.mp3"
la "And now I'm just COVERED in the stuff... AGAIN!"
mc "Yeah, you are quite messy indeed. I suggest you clean yourself up and wait on the bed for the next round of SEXY FUN!"
la "You can still go? Ooooh... Hopefully, this time, my tits will shrink back to normal. I can feel them going down a bit, thanks to your abundant offering."
mc "Yeah, sure, let's hope for the...err... best."
jump LaurieFuckChoiceA

label LaurieRide:
scene lauriepreride01 with dissolve
la "You want me to ride this GIANT menacing rod?"
mc "Yes I do. It's the only way to make your tits go down, remember?"
scene lauriepreride02 with dissolve
la "And you're very excited about it aren't you? Your dong is drooling massive amounts of pre-cum already..."
mc "That's why there's no time to waste Laurie!"
la "Alright, I'll ride your beast... Till you EXPLODE!"
play music "Sounds/barbarasex.mp3"
label LaurieRideSlow:
hide laurieridefast
show laurierideslow
call screen laurierideslow01
screen laurierideslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieRideEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LaurieRideFast") 

label LaurieRideFast:
la "Your cock goes so far up my tender pussy!"
mc "That's a good sign, it means you can take all 18 inches!"
hide laurierideslow
show laurieridefast
call screen laurieridefast01
screen laurieridefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieRideEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LaurieRideSlow") 

label LaurieRideEnd:
la "I don't think I...can take much more of this brutal pussy-wrecker [name]!"
mc "Then I guess it's time for me to..."
stop music
scene laurieridecum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "...UNLOAD! THERE I GO, AAAH!"
with fastflash
la "Thank you for being really considerate and dumping your mega-load inside me when I ask you to [name]!"
scene laurieridecum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "How about some outside too? RHAAA!"
with fastflash
la "Ah, uh, well, if you don't mind messy sheets, I guess..."
with fastflash
stop sound
scene laurieridecum03 with dissolve
play sound "Sounds/panting.mp3"
mc "Ahh, that was so good. So, did your tits go down in size?"
la "No! But now they're covered in your sticky spunk."
mc "Ah, that's too bad. I guess you should get cleaned up and I'll think of something else to help you..."
jump LaurieFuckChoiceA
    
label LaurieFuckChoiceB:
$ laurieanaltold = False
scene bedroom03b blurred
show lauriebed01
la "What are we going to do to make your GIANT MUSCLES and MASSIVE COCK go back to normal?"
stop music
menu:
    "Let's check how STRONG my new enhanced body is!":
        la "What do you have in mind?"
        mc "I'm gonna lift you up with my MASSIVE love muscle and IMPALE you on it!"
        la "Oooh, you're going to fuck me like a ragdoll?"
        mc "Yep. Come over here and FEEL MY POWER!"
        jump LaurieLift
    "Maybe a tight fit in your backdoor will force my cock down a few notches.":
        la "Or it will force my ass UP a few notches...."
        mc "Possibly. One can never tell until one tries."
        jump LaurieAnal
    "I want to see how FAR up your pussy my enhanced cock will go.":
        la "My pussy is only 10 inches deep..."
        mc "Then let's make it stretch up to 20 inches deep!"
        jump LaurieHugeSex
    "While I'm still MASSIVE and SUPER-VIRILE, let's make a baby." if preglaready >= 3 and impregnatedsomeone == False and babylaurie == False:
        $ impregnatedsomeone = True
        la "I hope it won't grow as HUGE as you inside me!"
        mc "It'll grow fast but you should be okay."
        jump LaurieImpregnation
    "I... feel like I'm going back to normal. Still hung like a mule of course, but with less energy after all this MONSTER FUCKING. So let's go to sleep...":
        jump LaurieEndB

label LaurieLift:
scene bedroom13 blurred
show lauriehugepreup01
with dissolve
la "Oh my God, look at your cock... It's way bigger than my arm!"
mc "Then imagine how good it will be fitting snugly in your tight pussy."
la "Mmmh, lift me up with it so I can imagine that better..."
hide lauriehugepreup01
show laurieup01
with dissolve
mc "I did it with ease. Just as I expected."
scene bedroom41 blurred
show laurieup02
with dissolve
la "Your lust pillar is just ssoo POWERFUL!"
mc "Then get ready for a POWERFUL fuck!"
scene bedroom33 blurred    
play music "Sounds/womansex02.mp3"
label LaurieUpSlow:
hide lauriehugeupfast
show lauriehugeupslow
call screen laurieupslow01
screen laurieupslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieUpEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LaurieUpFast") 

label LaurieUpFast:
mc "Fancy an even more POWERFUL ride?"
la "Yes, THRUST your horsecock FASTER, please [name]!"
hide lauriehugeupslow
show lauriehugeupfast
call screen laurieupfast01
screen laurieupfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieUpEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LaurieUpSlow") 

label LaurieUpEnd:
mc "That's a good exercise... But now I need to CUM!"
la "I can take care of that... *puff* Just... Put me down and I'll make sure you ejaculate a MASSIVE quantity of your seed!"
stop music
scene bedroom13 blurred
show lauriehugepreup01
with dissolve
mc "Interesting... What do you have in mind?"
la "I want to delicately massage your giant balls."
mc "Be my guest then!"
scene bedroom13 blurred
play music "Sounds/boymoan02.mp3"
label LauriBallsSlow:
hide laurieballsfast
show laurieballsslow
call screen laurieballsslow01
screen laurieballsslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LauriBallsEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LauriBallsFast") 

label LauriBallsFast:
la "Your balls are going to be churning so much cum for me..."
hide laurieballsslow
show laurieballsfast
call screen laurieballsfast01
screen laurieballsfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LauriBallsEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LauriBallsSlow") 

label LauriBallsEnd:
la "How does it feel? I can sense your balls RUMBLING..."
mc "It's... DIVINE.. I can't hold off...."
stop music
hide laurieballsslow
hide laurieballsfast
show laurieballscum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...ANY LONGER! AAAH!"
with fastflash
la "There you go, just blast away [name], EMPTY your huge cumsack!"
hide laurieballscum01
show laurieballscum02
with fastdissolve
la "Oh my God, your spurts are getting even BIGGER!"
with fastflash
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
la "Ssso much cream!"
scene bedroom35 blurred
show laurieballscum03
with fastdissolve
mc "AAAAH!"
with fastflash
la "Still going strong? Mmmh, I must have really boosted the spunk-producing capacity of your giant boulders then, hey?"
scene bedroom13 blurred
show lauriehugepreup01
with dissolve
la "So, how did it feel?"
mc "Fantastic. But my balls still aren't drained... So get back on the bed..."
jump LaurieFuckChoiceB

label LaurieAnal:
scene lauriepreanal01 with dissolve
la "Ooh, I can feel your heavy MONSTER against my asscheek... I don't know if it will ever fit."
mc "If it doesn't fit, we'll MAKE it fit."
scene lauriepreanal02 with dissolve
play sound "Sounds/moaning.mp3"
mc "Let's just try with the head in first... See, it fits."
mc "And now... The rest of it!"
play music "Sounds/barbarasex.mp3"
label LaurieAnalSlow:
hide laurieanalfast
scene bedroom17 blurred
show laurieanalslow
call screen laurieanalslow01
screen laurieanalslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LaurieAnalFast") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("LaurieAnalAssSlow") 

label LaurieAnalAssSlow:
show lauriehugeanalslow
call screen laurieanaltopslow01
screen laurieanaltopslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LaurieAnalAssFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("LaurieAnalSlow") 

label LaurieAnalFast:
if laurieanaltold == False:
    mc "Come on Laurie, I know you can ride that cock FASTER!"    
    la "AAh, uuuh, but, it's just so GIGANTIC!"
    mc "Just try. Up and down, up and down, but FASTER!"
    $ laurieanaltold = True
hide laurieanalslow
scene bedroom17 blurred
show laurieanalfast
call screen laurieanalfast01
screen laurieanalfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LaurieAnalSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("LaurieAnalAssFast") 

label LaurieAnalAssFast:
if laurieanaltold == False:
    mc "Come on Laurie, I know you can ride that cock FASTER!"    
    la "AAh, uuuh, but, it's just so GIGANTIC!"
    mc "Just try. Up and down, up and down, but FASTER!"
    $ laurieanaltold = True
show lauriehugeanalfast
call screen laurieanaltopfast01
screen laurieanaltopfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("LaurieAnalAssSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("LaurieAnalFast") 
            
label LaurieAnalEnd:
$ laurieanaltold = False
la "Please cum, my ass is getting DESTROYED!"
mc "I'm close, I'm..."
stop music
scene lauriehugeanalcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "...CUMMING, AAAH!"
with fastflash
play music "Sounds/moaning03.ogg"
la "Oooh, it's BLASTING inside of my poor little ass! I'm cumming too, [name]!"
scene lauriehugeanalcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "There you go, Laurie, MORE for you, RHAAA!"
with fastflash
stop music
la "Please pull out, your BHEMOTH is giving me a cum enema, there's just too much cm, AAHH!"
scene lauriehugeanalcum03 with dissolve
play sound "Sounds/panting.mp3"
mc "Damn, your backdoor is just LEAKING my slime... It's so filthy. And yet it makes me horny at the same time."
la "So this means you're going to get HARD again and fuck me some MORE?"
mc "You've got that right, Laurie."
jump LaurieFuckChoiceB

label LaurieHugeSex:
scene lauriepreside01 with dissolve
mc "Damn, your pussy is so tiny and my cock is so big... It's going to be a tight fit but..."
scene lauriesexhuge00 with dissolve
play sound "Sounds/womanscream.ogg"
mc "...It will fit!"
play music "Sounds/womansex02.mp3"
label LaurieSexHugeSlow:
hide lauriesexhugefast
show lauriesexhugeslow
call screen lauriesexhugeslow01
screen lauriesexhugeslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieSexHugeEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LaurieSexHugeFast") 

label LaurieSexHugeFast:
mc "That pussy feels so damn good wrapped around my monster pole!"
la "Andd your monster pole feels so damn HUGE inside my poor little pussy!"
hide lauriesexhugeslow
show lauriesexhugefast
call screen lauriesexhugefast01
screen lauriesexhugefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieSexHugeEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LaurieSexHugeSlow") 

label LaurieSexHugeEnd:
la "Please dump your load [name], I don't know if I can take much more of this BRUTAL pounding!"    
scene lauriesidecum01 with dissolve
play music "Sounds/splooge02.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Alright, here goes, RHAAA!"
with fastflash
scene lauriesidecum02 with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
la "STILL spewing? What a STUD your are!"
with fastflash
mc "You know what? I need to fuck you some more RIGHT NOW!"
scene lauriemishuge00
la "What? But, you JUST CAME!!!"
play music "Sounds/womansex02.mp3"
label LaurieMisHugeSlow:
hide lauriemishugefast
show lauriemishugeslow
call screen lauriemishugeslow01
screen lauriemishugeslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieMisHugeEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LaurieMisHugeFast") 

label LaurieMisHugeFast:
mc "How are you enjoying my superior cock and body Laurie?"
la "It's... incredible.. *puff* and your cock is so fucking BIG! AAAH! FUCK ME LIKE A BEAST!"
hide lauriemishugeslow
show lauriemishugefast
call screen lauriemishugefast01
screen lauriemishugefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieMisHugeEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LaurieMisHugeSlow") 

label LaurieMisHugeEnd:
la "Please come again, I want to feel your warm spunk blasting inside my pussy and all over me, AGAIN!"  
play sound "v07/creampie.mp3"
hide lauriemishugeslow
hide lauriemishugefast 
scene lauriemissionarycum01
with dissolve
mc "AAAH, I'm cumming AGAIN!"
with fastflash
la "I can  FEEL IT!"
scene lauriemissionarycum02 with dissolve
mc "Gotta hold onto something while I BLAST AWAY, RHAAA!"
with fastflash
la "Your shots are so POWERFUL [name]!"
scene lauriemissionarycum03 with dissolve
mc "Still some MORE, cumming NON-STOP for you Laurie!"
with fastflash
la "If you have more, COVER ME WITH IT PLEASE!"
stop music
scene lauriemissionarycum04 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH! There you are, RHAA!"
with fastflash
la "Ssso, ssoo much YOUNG CUM!"
scene lauriemissionarycum05 with dissolve
stop sound
play sound "Sounds/panting.mp3"
la "It's so tasty too,.. *slurp* I'm going to lick it ALL!"
mc "Good idea, while I recover. Then we can move on to more sexy fun with my MONSTER BODY!"
jump LaurieFuckChoiceB

label LaurieImpregnation:
scene bedroom03
show lauriepreimpreg01
with dissolve
la "What's the best position for human insemination, do you know? I only know about plant breeding I'm afraid."
mc "Yes, I do know. The best position is my giant cock 20 inches up your pussy."
la "Wow. That is so romantic."
hide lauriepreimpreg01
show lauriepreimpreg02
with dissolve
play sound "Sounds/slap.mp3"
mc "What were you saying?"
hide lauriepreimpreg02
show lauriepreimpreg01
with fastdissolve
la "Oooh, [name], please stop teasing me..."
hide lauriepreimpreg01
show lauriepreimpreg02
with fastdissolve
play sound "Sounds/slap.mp3"
mc "Teasing you with what?"
hide lauriepreimpreg02
show lauriepreimpreg01
with fastdissolve
la "With you great big monstercock..."
hide lauriepreimpreg01
show lauriepreimpreg02
with fastdissolve
play sound "Sounds/slap.mp3"
mc "You mean this cock that's slapping your ass?"
hide lauriepreimpreg02
show lauriepreimpreg01
with fastdissolve
la "Yes, this huge meatpole...  You know it..."
hide lauriepreimpreg01
show lauriepreimpreg02
with fastdissolve
play sound "Sounds/slap.mp3"
mc "OK, just relax and let me do all the pounding..."
la "Al...alright."
play music "Sounds/barbarasex.mp3"
label LaurieImpregnateSlow:
hide lauriepregnantslow
hide lauriepregnantfast
hide lauriepregfast
scene bedroom03 blurred
show lauriepregslow
call screen lauriepregnantsceneslow01
screen lauriepregnantsceneslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LauriePregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LaurieImpregnateFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("LauriePregnantSlow") 
            
label LaurieImpregnateFast:
hide lauriepregnantslow
hide lauriepregnantfast
hide lauriepregslow
scene bedroom03 blurred
show lauriepregfast
call screen lauriepregnantscenefast01
screen lauriepregnantscenefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LauriePregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("LaurieImpregnateSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("LauriePregnantFast") 
                        
label LauriePregnantSlow:
hide lauriepregnantfast
hide lauriepregslow
hide lauriepregfast
scene bedroom48 blurred
show lauriepregnantslow
call screen lauriepregnantslow01
screen lauriepregnantslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LauriePregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LauriePregnantFast") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("LaurieImpregnateSlow") 

label LauriePregnantFast:
hide lauriepregnantslow
hide lauriepregslow
hide lauriepregfast
scene bedroom48 blurred
show lauriepregnantfast
call screen lauriepregnantfast01
screen lauriepregnantfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LauriePregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LauriePregnantSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("LaurieImpregnateFast") 

label LauriePregnantEnd:
la "Please, just dump your baby-batter, I can't take much more of this MONSTER POUNDING!"
mc "You're in luck, I can feel my balls rumbling and..."
scene bedroom20 blurred
show laurieimpregcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
play music "Sounds/splooge02.mp3"
mc "...ready to unleash! RHAAAH!"
with fastflash
la "I'm cumming too, the baby will be conceived in pure bliss, AAAH!"
with fastflash
$ pregla = True
hide laurieimpregcum01
show laurieimpregcum02
with dissolve
stop music
play music "Sounds/splooge01.mp3"
mc "And there's still MORE swimming sperms for your eggs! OOOOOH!"
with fastflash
la "You're cumming like a BEAST inside me [name], give me MOOOOORRE, AAAH!"
with fastflash
mc "What? Oh yeah, sorry, I'm cumming ssooo much!"
stop music
scene laurieimpregcum03 with dissolve
play sound "Sounds/gasp.mp3"
la "I am BLOATED with AT LEAST a gallon of your sweet young boycum!"
mc "Well, that was a fun way to safeguard the future of humanity, wasn't it?"
la "I really hope this works... I don't want to have to go through such a MONSTER POUNDING again."
mc "Ah. Well, I'm getting back to normal size, let's sleep on it."
jump LaurieEndB

label LaurieEndA:
show screen calendar
show screen mcstats
scene lauriesleep02 with fade
$ loc = "bedroom"
play sound "Sounds/snoring.mp3"
pause 3
scene lauriesleep01b with fade
play sound "v072/yawning.mp3"
la "Thanks God I'm back to normal... See you [name], I'm off to the food unit to harvest today's salads!"
call NewDay
jump Bedroom

label LaurieEndB:
show screen calendar
show screen mcstats
scene lauriesleep01 with fade
$ loc = "bedroom"
play sound "Sounds/snoring.mp3"
pause 3
call NewDay
jump Bedroom