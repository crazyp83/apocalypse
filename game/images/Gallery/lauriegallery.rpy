label LaurieGallery:
call screen gallerylaurie
screen gallerylaurie:
    add "Gallery/lauriegallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("gallerylaurie"), Jump ("MainGallery")]

    if renpy.seen_image("laurieyoga01"):
        imagebutton:
            focus_mask True
            idle "Gallery/lauriegallery01.png" xpos 621 ypos 100
            hover "Gallery/lauriegallery01.png"
            action Jump ("LaurieGallery01")

    if renpy.seen_image("laurieyoga01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("LaurieGallery")

    if renpy.seen_image("lauriegymsquirt04"):
        imagebutton:
            focus_mask True
            idle "Gallery/lauriegallery02.png" xpos 1050 ypos 100
            hover "Gallery/lauriegallery02.png"
            action Jump ("LaurieGallery02")

    if renpy.seen_image("lauriegymsquirt04") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("LaurieGallery")

    if renpy.seen_image("laurieshower01"):
        imagebutton:
            focus_mask True
            idle "Gallery/lauriegallery03.png" xpos 1478 ypos 100
            hover "Gallery/lauriegallery03.png"
            action Jump ("LaurieGallery03")

    if renpy.seen_image("laurieshower01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("LaurieGallery")

            
    if renpy.seen_image("lauriedate01"):
        imagebutton:
            focus_mask True
            idle "Gallery/lauriegallery04.png" xpos 621 ypos 400
            hover "Gallery/lauriegallery04.png"
            action Jump ("LaurieGallery04")

    if renpy.seen_image("lauriedate01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("LaurieGallery")

    if renpy.seen_image("lauriebed02"):
        imagebutton:
            focus_mask True
            idle "Gallery/lauriegallery05.png" xpos 1050 ypos 400
            hover "Gallery/lauriegallery05.png"
            action Jump ("LaurieGallery05")

    if renpy.seen_image("lauriebed02") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("LaurieGallery")

    if renpy.seen_image("lauriebed01"):
        imagebutton:
            focus_mask True
            idle "Gallery/lauriegallery06.png" xpos 1478 ypos 400
            hover "Gallery/lauriegallery06.png"
            action Jump ("LaurieGallery06")

    if renpy.seen_image("lauriebed01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("LaurieGallery")

    add "Gallery/galleryfuture.png" xpos 621 ypos 700

    add "Gallery/galleryfuture.png" xpos 1050 ypos 700

    add "Gallery/galleryfuture.png" xpos 1478 ypos 700

    add "Gallery/gallerygrid02.png"
    add "Gallery/textlaurie.png"

label LaurieGallery01:
play music "Sounds/laurieworkout.mp3"
scene laurieyoga01
mc "There's Laurie doing some yoga in a tight spandex suit..."
scene laurieyoga02 with dissolve
mc "Wow, she's really flexible..."
scene laurieyoga03 with dissolve
mc "I can think of many wild uses for that flexibility in bed..."
scene laurieyoga04 with dissolve
mc "Looks like she's almost finished..."
show laurieyoga04b
la "Oh, hi [name]! Let me finish my last exercise and I'll be with you..."
stop music
scene gym04 with dissolve
show lauriegym01 with dissolve
la "Are you going to pump iron? Can I watch you? I'm done with my yoga for the day..."
mc "Of course Laurie. I'm gonna power-lift the heaviest set of weights you've ever seen in your life!"
la "Wow... I can't wait to see that! (wink)"
hide lauriegym01
play music "Sounds/mcworkout.mp3"
call screen mcgym01z
screen mcgym01z:
    add mcgym01 at center
    modal True
    button:
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("GymWorkoutEnd01z")    

label GymWorkoutEnd01z:
stop music
scene machine01 with dissolve
mc "Damn, that was a good workout! I need to POSE and FLEX those muscles!"
scene gymposing03 with dissolve
mc "Damn, my muscles are definitely getting BIGGER and STRONGER!"
scene gym04 with dissolve
show lauriegym02
la "I... can't believe what I just saw. You did it with such ease! Sssoo strong..."
mc "Err. Is it me or your tits grew? And your nipples... They're HUGE now!"
hide lauriegym02
show lauriegym03
with fastdissolve
la "Oh my God, this is so embarrassing... The... mutated salads... make my tits grow bigger when I'm horny. Oh no, I just said it!"
hide lauriegym03
show lauriegym04
with fastdissolve
la "I'm so ashamed... Please don't tell anyone... I... I need to go now [name]..."
jump LaurieGallery

label LaurieGallery02:
scene gym04
show lauriegym12
la "Aah, that was a good stretching routine..."
hide lauriegym12
show lauriegym11
la "Now I'm so tired..."
hide lauriegym11
show lauriegym10
la "Oh, it's you... And... you're wearing a... see-thru thong!"
mc "Yeah, it's a gift from Chief Lena, she says it will allow me to train better by not constraining blood flow throughout my body..."
hide lauriegym10
show lauriegym13
la "I... guess that makes sense... But it's so... lewd!"
mc "Well, there's nothing I can do about it, Chief's orders and all that."
show lauriegym13b
la "Don't worry, I... don't mind..."
mc "Err.. Your tits seem to be growing again. Are you getting horny?"
hide lauriegym13b
show lauriegym13c
la "What? Oh no!"
hide lauriegym13
hide lauriegym13c
show lauriegym14
mc "I hope you're wearing a stretchy top, cos you're really growing HUGE real fast Laurie!"
la "My God, what's happening to me? Please do something about it [name]!"
mc "I'm not sure what I could..."
play sound "Sounds/snap.mp3"
hide lauriegym14
hide lauriegym13
show lauriegym15
mc "... do."
la "My top has snapped, now my breasts are exposed, this is so embarassing!"
mc "Don't worry about it, I've seen plenty of breasts before. ALthoug not as MASSIVE as your funbags right now!"
hide lauriegym15
show lauriegym16
la "It's really PAINFUL! Please help me [name]"
mc "Let me squirt some milk out of your tits to make them go back to normal."
la "Please be gentle..."
scene gym04 with dissolve
show lauriegymsquirt01a
mc "I'll slowly push around your nipples..."
hide lauriegymsquirt01a
show lauriegymsquirt01b
with fastdissolve
mc "There you go..."
la "Aah, I'm squirting milk!"
hide lauriegymsquirt01b
show lauriegymsquirt01a
with fastdissolve
mc "And again..."
hide lauriegymsquirt01a
show lauriegymsquirt01b
with fastdissolve
la "Do you think this is working?"
hide lauriegymsquirt01b
show lauriegymsquirt02a
with fastdissolve
mc "I'd say so, your tit has shrunk, but there's still some milf left..."
hide lauriegymsquirt02a
show lauriegymsquirt02b
with fastdissolve
la "Ooh, this is starting to feel good... Oh no, why did I say that?"
hide lauriegymsquirt02b
show lauriegymsquirt02a
mc "I didn't hear a thing, I'm totally concentrated on my task..."
hide lauriegymsquirt02a
show lauriegymsquirt02b
with fastdissolve
mc"I think we're done with this breast, let's work on the other one..."
scene gym04squirt blurred
show lauriegymsquirt03a at left
with fastdissolve
la "This is... so embarrassing... A man breast-pumping me like that..."
mc "You asked for help, and here I am!"
hide lauriegymsquirt03a
show lauriegymsquirt03b at left
mc "Nice, some breastjuice is also squirting out of this one like crazy...."
hide lauriegymsquirt03b
show lauriegymsquirt03a at left
with fastdissolve
la "Do it again, I can feel I'm still... full.."
hide lauriegymsquirt03a
show lauriegymsquirt03b at left
with fastdissolve
mc "Rightee-ooo..."
hide lauriegymsquirt03b
show lauriegymsquirt03c at left
with fastdissolve
la "OOh, I feel much better now..."
mc "Hang, on, there's still a bit more milk I need to remove..."
hide lauriegymsquirt03c
show lauriegymsquirt03d at left
with fastdissolve
mc "I think we're done Laurie... Your tits are still huge, but it's their normal size more or less..."
scene gym04 with dissolve
show lauriegymsquirt04
with fastdissolve
la "Thank you so much [name]... Please... don't mention that to anyone.."
mc "Sure Laurie... Hang on, you shouldn't leave the gym with milk pouring out of your nipples like that, let me help you get rid of it..."
hide lauriegymsquirt04
show lauriegymsquirt05
with fastdissolve
la "What are you doing?"
mc "Just cleaning up... You're all done now..."
la "Thanks God for that, this was just sssooo embarassing... I'd better leave now [name]."
jump LaurieGallery

label LaurieGallery03:
play sound "Sounds/dream.mp3"
scene locker03dream
show laurieshower01 at center
play music "Sounds/showerstrip.mp3"
la "Oh hi [name], are you taking a shower? Can I join you? I'm done with my yoga for the day...."
mc "For sure Laurie, I'll make room for you... and my cock!"
hide laurieshower01    
show laurieshower02
la "I've never seen a man with a godly body like yours. You're making me ssoo horny."
mc "I'm horny too. Perfect combination."
hide laurieshower02    
show laurieshower03
la "I'm sssoo hot for you [name], my tits have grown to a simply GIGANTIC size!"
mc "Fuck yeah! So has my huge shaft for you Laurie!"
hide laurieshower03        
scene locker03 blurred
show laurieshower04
la "I'm a vegetarian but I'll gladly eat YOUR meat."
mc "It's hot and ready for your hungry mouth, get to it!"
la "I'll do it \"Yoga style\"..." 
scene lockerlauriefuck01b with dissolve
mc "That's it, suck it hard Laurie, I want your spit all over my mighty shaft!"
scene lockerlauriefuck01c with dissolve
mc "Open wider,I'm gonna pound that filthy mouth of yours"
scene lockerlauriefuck01b with dissolve
pause 0.3
scene lockerlauriefuck01d with fastdissolve
mc "YES, ALL THE WAY down your throat! Damn it girl, you can swallow it all!"
scene lockerlauriefuck01a with dissolve
la "I'm feeling so dirty, with all your copious precum dripping down my chin..."
mc "Just you wait till I come for REAL..."
la "Well, why don't I help you coax that load... I'll show you what my flexible body can do to your donkey dick..."
scene lockerlauriefuck02a with dissolve
mc "Not bad, but you still have over ten inc..."
scene lockerlauriefuck02b with dissolve
mc "... to go! AAAH!"
la "You were saying?"
scene lockerlauriefuck02a with fastdissolve
pause 0.2
scene lockerlauriefuck02b with fastdissolve
pause 0.3
scene lockerlauriefuck02a with fastdissolve
pause 0.2
scene lockerlauriefuck02b with fastdissolve
pause 0.3
scene lockerlauriefuck02a with fastdissolve
pause 0.2
scene lockerlauriefuck02b with fastdissolve
pause 0.3
scene lockerlauriefuck02a with fastdissolve
pause 0.2
scene lockerlauriefuck02b with fastdissolve
pause 0.3
scene lockerlauriefuck02a with fastdissolve
pause 0.2
scene lockerlauriefuck02b with fastdissolve
pause 0.3
la "Are you getting there? I can feel your monster cock getting bigger and harder... (giggles)"
scene lockerlauriefuck02d with fastdissolve
mc "FUCK! I'm cumming a MONSTER LOAD DEEP INSIDE YOU LAURIE!"
scene lockerlauriefuck02c with dissolve
la "YES, keep pumping that shaft, cover me with your warm virile cream [name]!"
stop music
play music "Sounds/shower.mp3"
scene lockermccum01 with dissolve
mc "Yeah, take that Laurie, I'm gonna drown your giant tits in my cum!"
scene lockermccum02 with dissolve
mc "Damn, I made a right dreamy mess. I'd better clean all of it before I leave or people will think I'm a total pervert. Which I definitely AM NOT."
jump LaurieGallery

label LaurieGallery04:
play music "v07/datemusic.mp3"
scene canyon01
show lauriedate01
mc "This is it. The Red Canyon. Even has trees. Not edible though, I warn you."
hide lauriedate01
show lauriedate02
with fastdissolve
la "Ah yes, I remember this place when I visited it years ago to install a water pump for my salads..."
mc "But you haven't been here since, right?"
hide lauriedate02
show lauriedate03
with fastdissolve
la "No I haven't. I haven't been invited on a date actually. Come, let's go for a swim, I'm dying to get into the water!"
scene lauriedate04 with dissolve
la "The water is so nice. And pure. That's why my salads taste so great!"
mc "Don't go too far though, it can get pretty deep around here."
scene lauriedate05 with dissolve
la "Don't worry about me, I know how to swim, I want to cross onto the other side and see if I can find some interesting new plants."
mc "Okay, I'll swim along with you then, just to be on the safe side."
la "You wouldn't want to lose your date, now would you? *wink*"
scene lauriedate06 with dissolve
la "Oh, I think I found the entrance to a cave... Let's go inside, this is exciting!"
mc "Err... You're sure this is a good idea. I was thinking more of...like swimming and you admiring my muscles and then me kissing you. The sort of stuff that usually happens on my dates."
la "Yes, I AM sure. If you don't come with me, I'll go ALONE."
mc "Fine, I'll follow you then..."
stop music
play music "v072/cave.mp3"
scene lauriedate07 with dissolve
la "Wow, look at this cave, it's beautiful!"
mc "Remember that I invited you on this date. Without my input, we would never have stumbled upon this place..."
scene lauriedate08 with dissolve
la "And look, there are some mushrooms here too! Do you know that mushrooms are VERY nutritious?"
mc "And some of them are poisonous..."
scene cavebackground
show lauriedate09 at right
show lauriedate10 at left
with dissolve
la "These look alright to me. Why don't you try one? For me? Please."
menu:
    "Accept":
        jump MushroomAtex
    "Refuse":
        jump MushroomNotAtex

label MushroomAtex:
hide lauriedate09
hide lauriedate10
show lauriedate11 at right
show lauriedate11b at left
with fastdissolve
la "So? Did it taste good?"
mc "It's okay I guess..."
stop music
hide lauriedate11b
show lauriedate12b at left
with fastdissolve
mc "AAARGH, what's happening? It hurts all over!"
la "[name]! Your bulge.... It's getting BIGGER! You're gonna rip the fabr..."
play sound "Sounds/ripping.mp3"
hide lauriedate12b
hide lauriedate11
show lauriedate12 at right
show lauriedate13b at left
with fastdissolve
mc "This is too much! My cock! It can't stop GROWING!"
la "I can see that... It's getting bigger than a tree trunk!"
hide lauriedate13b
hide lauriedate12
show lauriedate13 at right
show lauriedate14b at left
with fastdissolve
mc "Help me please Laurie, I can't feel my heart pumping anymore, all the blood is in my rod, AAAAH!"
la "Okay, maybe... Try and EJACULATE! Your cock will go soft and smaller and you'll have enough blood flowing into the rest of your body that way!"
hide lauriedate14b
show lauriedate15b at left
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "AAAAAHHHHH!"
with fastflash
la "Oh my God, this is the biggest monster cumshot I've eveer seen in my life! And I owned a poney when I was a child!"
hide lauriedate15b
hide lauriedate13
show lauriedate17 at right
show lauriedate16b at left
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "GOD DAMN, THIS IS TOO MUCH, RHAAAA!"
with fastflash
la "Keep going [name], let it ALL OUT, it's the ONLY way!"
hide lauriedate16b
show lauriedate17b at left
with fastdissolve
mc "Oooh, finally, I'm done, I... can feel the blood coming back..."
hide lauriedate17
show lauriedate16 at centerright
mc "But I feel nauseous. I think those mushrooms were poisonous..."
la "I'm sorry I told you to eat that thing... But you were very brave for sacrificing your health for the future of humanity!"
mc "*Well at least I got a lust point out of this...*"
mc "I think I really need to get to the medbay, Laurie!"
la "Sure, I'll take you there, just hang in there and continue to be brave..."
jump LaurieGallery
label MushroomNotAtex:
hide lauriedate10
show lauriedate10b at left
with fastdissolve
mc "Not really, I don't feel good about this..."
play sound "Sounds/slap.mp3"
hide lauriedate10b
hide lauriedate09
show lauriedateno
with fastdissolve
la "How dare you refuse my on-date demand! This date is OVER. Let's go back to the compound, I have to take care of my salads."
mc "Wow, that escalated quickly."
jump LaurieGallery

label LaurieGallery05:
play music "v07/datemusic.mp3"
scene bedroom02 blurred
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
label LaurieFuckChoiceAx:
scene bedroom03b blurred
show lauriebed02
la "What are we going to do to make my huge breasts go DOWN?"
stop music
menu:
    "A serious tit-rubbing with my cock might do the trick...":
        la "Then let's rub them very VIGOROUSLY against your shaft!"
        jump LaurieTitjobx
    "If I really POUND your pussy with my huge cock, it might make you less horny.":
        la "Alright, that is a scientifically sound argument. Let's do it!"
        mc "So lay on your back and let me do the fucking..."
        jump LaurieFuckx
    "Get on my cock and ride me really hard.":
        la "How is that going to help my tits go down in size?"
        mc "They'll be bouncing up and down all over the place, so it definitely SHOULD help. Anyway, don't argue, let's do it, you have nothing to lose!"
        jump LaurieRidex
    "I'm done with this gallery":
        jump LaurieGallery

label LaurieTitjobx:
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
label LaurieTitFuckSlowx:
hide laurietitfuckfast
show laurietitfuckslow
call screen laurietitfuckslow01x
screen laurietitfuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieTitFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LaurieTitFuckFastx") 

label LaurieTitFuckFastx:
la "Do my MASSIVE boobs feel nice, tightly wrapped around your pummeling monster pole, [name]?"
mc "Oh God, of course they do, they're the BEST!"
hide laurietitfuckslow
show laurietitfuckfast
call screen laurietitfuckfast01x
screen laurietitfuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieTitFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LaurieTitFuckSlowx") 

label LaurieTitFuckEndx:
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
jump LaurieFuckChoiceAx

label LaurieFuckx:
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
label LaurieFuckSlowx:
hide lauriefuckfast
show lauriefuckslow
call screen lauriefuckslow01x
screen lauriefuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LaurieFuckFastx") 

label LaurieFuckFastx:
mc "Those MONSTER tits of yours... Just make me want to pound that tight warm pussy even FASTER!"
hide lauriefuckslow
show lauriefuckfast
call screen lauriefuckfast01x
screen lauriefuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LaurieFuckSlowx") 

label LaurieFuckEndx:
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
label LaurieMegaSlowx:
hide lauriemegafast
show lauriemegaslow
call screen lauriemegaslow01x
screen lauriemegaslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieMegaEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LaurieMegaFastx") 

label LaurieMegaFastx:
mc "I just can't stop PUMMELLING that warm pussy!"
la "Your cock is just so big, my enhanced breast are jiggling everywhere!"
hide lauriemegaslow
show lauriemegafast
call screen lauriemegafast01x
screen lauriemegafast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieMegaEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LaurieMegaSlowx") 

label LaurieMegaEndx:
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
jump LaurieFuckChoiceAx

label LaurieRidex:
scene lauriepreride01 with dissolve
la "You want me to ride this GIANT menacing rod?"
mc "Yes I do. It's the only way to make your tits go down, remember?"
scene lauriepreride02 with dissolve
la "And you're very excited about it aren't you? Your dong is drooling massive amounts of pre-cum already..."
mc "That's why there's no time to waste Laurie!"
la "Alright, I'll ride your beast... Till you EXPLODE!"
play music "Sounds/barbarasex.mp3"
label LaurieRideSlowx:
hide laurieridefast
show laurierideslow
call screen laurierideslow01x
screen laurierideslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieRideEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LaurieRideFastx") 

label LaurieRideFastx:
la "Your cock goes so far up my tender pussy!"
mc "That's a good sign, it means you can take all 18 inches!"
hide laurierideslow
show laurieridefast
call screen laurieridefast01x
screen laurieridefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieRideEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LaurieRideSlowx") 

label LaurieRideEndx:
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
jump LaurieFuckChoiceAx

label LaurieGallery06:
play music "v07/datemusic.mp3"
scene bedroom02 blurred
show lauriemcprehuge01 at left
show laurielingerie13 at right with moveinright
la "Try this [name]!"
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
label LaurieFuckChoiceBx:
$ laurieanaltoldx = False
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
        jump LaurieLiftx
    "Maybe a tight fit in your backdoor will force my cock down a few notches.":
        la "Or it will force my ass UP a few notches...."
        mc "Possibly. One can never tell until one tries."
        jump LaurieAnalx
    "I want to see how FAR up your pussy my enhanced cock will go.":
        la "My pussy is only 10 inches deep..."
        mc "Then let's make it stretch up to 20 inches deep!"
        jump LaurieHugeSex
    "While I'm still MASSIVE and SUPER-VIRILE, let's make a baby." if renpy.seen_image("lauriepreimpreg01"):
        la "I hope it won't grow as HUGE as you inside me!"
        mc "It'll grow fast but you should be okay."
        jump LaurieImpregnationx
    "I'm done with this gallery.":
        jump LaurieGallery

label LaurieLiftx:
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
label LaurieUpSlowx:
hide lauriehugeupfast
show lauriehugeupslow
call screen laurieupslow01x
screen laurieupslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieUpEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LaurieUpFastx") 

label LaurieUpFastx:
mc "Fancy an even more POWERFUL ride?"
la "Yes, THRUST your horsecock FASTER, please [name]!"
hide lauriehugeupslow
show lauriehugeupfast
call screen laurieupfast01x
screen laurieupfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieUpEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LaurieUpSlowx") 

label LaurieUpEndx:
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
label LauriBallsSlowx:
hide laurieballsfast
show laurieballsslow
call screen laurieballsslow01x
screen laurieballsslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LauriBallsEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LauriBallsFastx") 

label LauriBallsFastx:
la "Your balls are going to be churning so much cum for me..."
hide laurieballsslow
show laurieballsfast
call screen laurieballsfast01x
screen laurieballsfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LauriBallsEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LauriBallsSlowx") 

label LauriBallsEndx:
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
jump LaurieFuckChoiceBx

label LaurieAnalx:
scene lauriepreanal01 with dissolve
la "Ooh, I can feel your heavy MONSTER against my asscheek... I don't know if it will ever fit."
mc "If it doesn't fit, we'll MAKE it fit."
scene lauriepreanal02 with dissolve
play sound "Sounds/moaning.mp3"
mc "Let's just try with the head in first... See, it fits."
mc "And now... The rest of it!"
play music "Sounds/barbarasex.mp3"
label LaurieAnalSlowx:
hide laurieanalfast
scene bedroom17 blurred
show laurieanalslow
call screen laurieanalslow01x
screen laurieanalslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LaurieAnalFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("LaurieAnalAssSlowx") 

label LaurieAnalAssSlowx:
show lauriehugeanalslow
call screen laurieanaltopslow01x
screen laurieanaltopslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LaurieAnalAssFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("LaurieAnalSlowx") 

label LaurieAnalFastx:
if laurieanaltoldx == False:
    mc "Come on Laurie, I know you can ride that cock FASTER!"    
    la "AAh, uuuh, but, it's just so GIGANTIC!"
    mc "Just try. Up and down, up and down, but FASTER!"
    $ laurieanaltoldx = True
hide laurieanalslow
scene bedroom17 blurred
show laurieanalfast
call screen laurieanalfast01x
screen laurieanalfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LaurieAnalSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("LaurieAnalAssFastx") 

label LaurieAnalAssFastx:
if laurieanaltoldx == False:
    mc "Come on Laurie, I know you can ride that cock FASTER!"    
    la "AAh, uuuh, but, it's just so GIGANTIC!"
    mc "Just try. Up and down, up and down, but FASTER!"
    $ laurieanaltoldx = True
show lauriehugeanalfast
call screen laurieanaltopfast01x
screen laurieanaltopfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("LaurieAnalAssSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("LaurieAnalFastx") 
            
label LaurieAnalEndx:
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
jump LaurieFuckChoiceBx

label LaurieHugeSexx:
scene lauriepreside01 with dissolve
mc "Damn, your pussy is so tiny and my cock is so big... It's going to be a tight fit but..."
scene lauriesexhuge00 with dissolve
play sound "Sounds/womanscream.ogg"
mc "...It will fit!"
play music "Sounds/womansex02.mp3"
label LaurieSexHugeSlowx:
hide lauriesexhugefast
show lauriesexhugeslow
call screen lauriesexhugeslow01x
screen lauriesexhugeslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieSexHugeEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LaurieSexHugeFastx") 

label LaurieSexHugeFastx:
mc "That pussy feels so damn good wrapped around my monster pole!"
la "Andd your monster pole feels so damn HUGE inside my poor little pussy!"
hide lauriesexhugeslow
show lauriesexhugefast
call screen lauriesexhugefast01x
screen lauriesexhugefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieSexHugeEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LaurieSexHugeSlowx") 

label LaurieSexHugeEndx:
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
label LaurieMisHugeSlowx:
hide lauriemishugefast
show lauriemishugeslow
call screen lauriemishugeslow01x
screen lauriemishugeslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieMisHugeEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LaurieMisHugeFastx") 

label LaurieMisHugeFastx:
mc "How are you enjoying my superior cock and body Laurie?"
la "It's... incredible.. *puff* and your cock is so fucking BIG! AAAH! FUCK ME LIKE A BEAST!"
hide lauriemishugeslow
show lauriemishugefast
call screen lauriemishugefast01x
screen lauriemishugefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LaurieMisHugeEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LaurieMisHugeSlowx") 

label LaurieMisHugeEndx:
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
jump LaurieFuckChoiceBx

label LaurieImpregnationx:
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
label LaurieImpregnateSlowx:
hide lauriepregnantslow
hide lauriepregnantfast
hide lauriepregfast
scene bedroom03 blurred
show lauriepregslow
call screen lauriepregnantsceneslow01x
screen lauriepregnantsceneslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LauriePregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LaurieImpregnateFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("LauriePregnantSlowx") 
            
label LaurieImpregnateFastx:
hide lauriepregnantslow
hide lauriepregnantfast
hide lauriepregslow
scene bedroom03 blurred
show lauriepregfast
call screen lauriepregnantscenefast01x
screen lauriepregnantscenefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LauriePregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("LaurieImpregnateSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("LauriePregnantFastx") 
            
label LauriePregnantSlowx:
hide lauriepregnantfast
hide lauriepregslow
hide lauriepregfast
scene bedroom48 blurred
show lauriepregnantslow
call screen lauriepregnantslow01x
screen lauriepregnantslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LauriePregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LauriePregnantFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("LaurieImpregnateSlowx") 

label LauriePregnantFastx:
hide lauriepregnantslow
hide lauriepregslow
hide lauriepregfast
scene bedroom48 blurred
show lauriepregnantfast
call screen lauriepregnantfast01x
screen lauriepregnantfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LauriePregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LauriePregnantSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("LaurieImpregnateFastx") 

label LauriePregnantEndx:
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
jump LaurieGallery
