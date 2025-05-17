label MarnieGallery:
call screen gallerymarnie
screen gallerymarnie:
    add "Gallery/marniegallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("gallerymarnie"), Jump ("MainGallery")]

    if renpy.seen_image("marniegymbells01"):
        imagebutton:
            focus_mask True
            idle "Gallery/marniegallery01.png" xpos 620 ypos 100
            hover "Gallery/marniegallery01.png"
            action Jump ("MarnieGallery01")

    if renpy.seen_image("marniegymbells01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 620 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("MarnieGallery")

    if renpy.seen_image("marnieshower01"):
        imagebutton:
            focus_mask True
            idle "Gallery/marniegallery02.png" xpos 1048 ypos 100
            hover "Gallery/marniegallery02.png"
            action Jump ("MarnieGallery02")

    if renpy.seen_image("marnieshower01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1048 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("MarnieGallery")

    if renpy.seen_image("marniedate01"):
        imagebutton:
            focus_mask True
            idle "Gallery/marniegallery03.png" xpos 1478 ypos 100
            hover "Gallery/marniegallery03.png"
            action Jump ("MarnieGallery03")

    if renpy.seen_image("marniedate01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("MarnieGallery")

    if renpy.seen_image("marniefemdom05"):
        imagebutton:
            focus_mask True
            idle "Gallery/marniegallery04.png" xpos 620 ypos 400
            hover "Gallery/marniegallery04.png"
            action Jump ("MarnieGallery04")

    if renpy.seen_image("marniefemdom05") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 620 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("MarnieGallery")

    if renpy.seen_image("marniemaledom04"):
        imagebutton:
            focus_mask True
            idle "Gallery/marniegallery05.png" xpos 1048 ypos 400
            hover "Gallery/marniegallery05.png"
            action Jump ("MarnieGallery05")

    if renpy.seen_image("marniemaledom04") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1048 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("MarnieGallery")

    add "Gallery/galleryfuture.png" xpos 1478 ypos 400

    add "Gallery/galleryfuture.png" xpos 620 ypos 700

    add "Gallery/galleryfuture.png" xpos 1048 ypos 700

    add "Gallery/galleryfuture.png" xpos 1478 ypos 700

    add "Gallery/gallerygrid02.png"
    add "Gallery/textmarnie.png"
        
label MarnieGallery01:
scene gym05
show marniegymbells01
ma "Oh, hi [name]! I hope you don't need those dumbbells because I'm about to use them..."
mc "I'm fine, they are too light for me anyway, you go ahead with your training..."
ma "And you'll watch I have no doubt..."
scene gym06
show marnietrain01
mc "(You bet I will...)"
hide marnietrain01
show marniegym
call screen marniegymx
screen marniegymx:
    add "Icons/nextidle.png"
    modal True
    button:
        xpos .91
        ypos .44
        xysize(140, 80)        
        action Jump ("MarnieGymWorkoutEndx")

label MarnieGymWorkoutEndx:
scene gym02 with dissolve
show marniegym02
ma "I LOVE using the gym... It makes me feel so ALIVE to be FIT!"
mc "I agree, and the BIGGER the muscles, the BETTER!"
hide marniegym02
show marniegym03
ma "Yeah? Well, check those abs [name]!"
mc "Nice Marnie, they're getting really developed. Not as much as mine of course..."
hide marniegym03
show marniegym01
ma "Stop bragging. And show me then."
mc "Well watch my EIGHT-pack while I pump iron!"
ma "Alright. Go ahead." 
hide marniegym01
play music "Sounds/mcworkout.mp3"
call screen mcgym01n
screen mcgym01n:
    add mcgym01 at center
    modal True
    button:
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("GymWorkoutEnd01n")    

label GymWorkoutEnd01n:
stop music
scene machine01 with dissolve
mc "Damn, that was a good workout! I need to POSE and FLEX those muscles!"
scene gymposing02 with dissolve
mc "Fuck yeah! Monster teen muscle stud right here!"
scene gym03
show marniegym02
ma "Your eight-packs were indeed RIPPLING during that routine."
mc "I hope you appreciated their awesome POWER..."
ma "I did [name], I did..."
mc "So, what are doing next Marnie?" 
hide marniegym02
show marniegym01
with fastdissolve
ma "I need to go back and man the bar. There are people drinking at all times of the day..."
mc "I'll probably see you there later myself, I'm thirsty... for YOU!"
ma "Well, what a charmer... See you later [name]!"
jump MarnieGallery
    
label MarnieGallery02:
play sound "Sounds/dream.mp3"
scene locker03dream
show marnieshower01
play music "Sounds/showerstrip.mp3"
ma "Are you looking for a tip? I've got plenty of SEX TIPS for you."
mc "Yeah? Like what?"
hide marnieshower01    
show marnieshower02
ma "Well, I'll tell you only if you promise..."
ma "...to FUCK me like a BEAST!"
mc "I can make that promise, no worries!"
hide marnieshower02    
show marnieshower03                                            
ma "I knew you would agree... Well, my first tip is that you need to have a HUGE ROCK-HARD COCK! So that it fits between my HUGE SOFT TITS!"
mc "And I HAVE, what a coincidence!"
hide marnieshower03
scene locker03 blurred
show marnieshower04
ma "And my second tip is that..."
ma "...You need to COVER them in an INCH-THICK layer of man-juice!"
mc "I'll see what I can do... Let us proceed then."
scene lockermarnietit01 with dissolve    
ma "Mmh, you're ROCK-HARD and already DRIPPING with yummy pre-cum! I'l gonna have a lot of fun with that giant cock!"
scene lockermarnietit02 with dissolve    
ma "Let's see if that MONSTER ROD fits between my MASSIVE RACK shall we?"
mc "I'm pretty sure it does, it's even sticking out..."
scene lockermarnietit03 with fastdissolve    
ma "Great, then I can suck on the tip, while you PUMMEL my breasts!"
mc "I'll fuck them so hard and fast they will heat up like an iron bar in furnace!"
call screen marniegymdream01x
screen marniegymdream01x:
    add dreammarniegym01 at center
    modal True
    button:
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("DreamMarnie01GymEndx")    
label DreamMarnie01GymEndx:
mc "Damn, I need to cool off or I'll blow my load right there!"
ma "Then eat my pussy dirty boy!"
scene lockermarnielick01 with dissolve
ma "Yes, swirl your tongue, just like that..."
scene lockermarnielick02 with dissolve
ma "Oooh, you are a man of so many wonders..."
mc "I'm the HERO, that's why it's assumed I am a Master Cocksman."
ma "Then it's time to FUCK ME, Master Cocksman!"
scene lockermarniefuck01 with dissolve
ma "Be careful, I've never had anything THAT big in me before!" 
mc "Just relax those pussy muscles and..."
scene lockermarniefuck02 with dissolve 
mc "...It will fit without any problem."
call screen marniegymdream02x
screen marniegymdream02x:
    add dreammarniegym02 at center
    modal True
    button:
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("DreamMarnie02GymEndx")    
label DreamMarnie02GymEndx:
ma "Don't cum inside me, I want your cum ALL OVER my body!"
scene lockermarniecum with dissolve
mc "RHAAA!"
ma "There you go! Remember, you need to cover my chest in an INCH-THICK layer of ball-batter!"
mc "Fuck, I'm spewing non-stop!"
stop music
play music "Sounds/shower.mp3"
scene lockermccum01 with dissolve
mc "Yeah, take those jets Marnie! AAAH!"    
scene lockermccum02 with dissolve
mc "Damn, I made a right dreamy mess. I'd better clean all of it before I leave or people will think I'm a total pervert. Which I definitely AM NOT."
jump MarnieGallery

label MarnieGallery03:
play music "v07/datemusic.mp3"
scene canyon01
show marniedate02
ma "I know this place, but I haven't been here in a while... There are too many alcoholics in the compound and I have very little free time."
mc "Who's manning the bar this morning then?"
hide marniedate02
show marniedate01
with fastdissolve
ma "Cyrl is. But I'll make sure to count how many Tar Cocktails she drinks and CHARGE them to her account!"
mc "So, what shall we do?"
hide marniedate01
show marniedate04
with fastdissolve
ma "I know what you're thinking... You're wondering where my Road Warriors tattoo is, aren't you?"
mc "Purely out of professional interest. I need to better understand Road Warriors lore and customs for my missions."
hide marniedate04
show marniedate05
with fastdissolve
ma "Well, it's right there on my left ankle... Do you want to get a closer look since you're such a \"professional\"?"
scene canyon03 blurred
show marniedate06
mc "I see... A skull. Surrounded by roses."
ma "That's right, it represents the fight between love and death. Sometimes you have to sacrifice your loved ones to avoid death."
mc "(She's a troubled girl it seems...) Well, I'm also in a fight between love and death. The love for my dead family and the fact that I'm going to kill that motherfucker Trumpf!"
scene canyon02
show marniedate03
with fastdissolve
ma "That's good [name], you have RESOLVE. And you NEED that to survive in this merciless world."
hide marniedate03
show marniedate07
ma "Now let's swim, it's good for the muscles. And you NEED to get even BIGGER muscles."
scene marniecanyon01 with dissolve
play sound "Sounds/dive.mp3"
mc "Wow, she's pretty fit and a very good swimmer. I really have to strain myself to keep up with her."
$ period += 1
scene marniecanyon02 with fade
ma "Mmmh, isn't it a marvellous place? I wish I could be here all day... Did you have a good swim?"
mc "*Puff*... Yeah, I think... I can feel it in my muscles."
ma "I told you it was a good exercise. Now let's see how BIG they've become..."
scene marniecanyon03
ma "Mmmh, VERY nice... And VERY BIG..."
scene marniecanyon03 with dissolve
ma "I told you this was a very good exercise for your muscles [name]. That's how I get MY six-pack."
ma "But enough admiring our muscles, it's getting late and I have to get back to the bar. Hopefully, Cyrl won't be on the floor, totally tar-drunk, like last time."
scene canyon01 blurred
show marniedate01
with dissolve
ma "Thanks a lot for this wonderful date [name]!"    
stop music
jump MarnieGallery

label MarnieGallery04:
play music "v07/datemusic.mp3"
scene bedroom01
show marnie01
ma "Get ready for some serious SPANKING from the ULTIMATE Road Warrior Dominatrix!"
ma "Get into your undies and sit down, SLAVE. I'll be right back..."
hide marnie01 with dissolve
window hide
scene bedroom02 with dissolve
show marniefemdom01 with moveinright
ma "Bow down to your MISTRESS, [name]!"
mc "What if I refuse?"
hide marniefemdom01
show marniefemdom03
with fastdissolve
ma "Then this will happen!"
hide marniefemdom03
show marniefemdom04
with fastdissolve
play sound "Sounds/whip.wav"
mc "Ouch! Ok, Ok, I bow down to you, mistress..."
hide marniefemdom04
show marniefemdom03
with fastdissolve
ma "That's better. You'd better learn your place now, SLAVE! Just because you have the biggest FUCKTOOL I've ever seen in my life doesn't mean you're entitled to even dare speak to your MISTRESS, you hear me?"
mc "Err... Am I supposed to talk or not here, I'm confused?"
hide marniefemdom03
show marniefemdom04
with fastdissolve
play sound "Sounds/whip.wav"
ma "Speak when spoken to, SLAVE! And only then!"
mc "I get it mistress, I get it!"
hide marniefemdom04
show marniefemdom02
with fastdissolve
ma "Let's play a little game... That involves this edging stick and your HARD COCK!"
scene marniefemdom05 with dissolve
ma "Lie on your back, cock sticking rigidly up in the air..."
stop music
scene marniefemdom06a with dissolve
play music "Sounds/vibrator.ogg"
scene marniefemdom06b with fastdissolve
ma "There you go... Feel those vibrations running all along your giant trembling shaft?"
scene marniefemdom06c with fastdissolve
mc "Uh.. ggg..."
label MarnieFemdomStickx:
show marniefemdomstick
call screen marniefemdomstick01x
screen marniefemdomstick01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieFemdomStickEndx")

label MarnieFemdomStickEndx:
scene marniefemdom07 with dissolve
stop music
ma "I think that's enough for now... Wouldn't want you to come just yet, would we?"
play sound "Sounds/boymoan.mp3"
ma "Get up and stop moaning you wimpy slave!"
scene marniefemdom08 with dissolve
ma "And now come over here and stick your monster fuckstick between my thighs. I'm gonna leg-scissor it till you can't stop cumming all over the place!"
scene marniefemdom09a with dissolve
ma "There, nice and cosy between my muscular thighs, isn't it?"
mc "Y..yes, Mistress..."
ma "Fuck my thighs. Fuck 'em HARD!"
scene marniefemdom09b with fastdissolve
ma "Mmmh, you're drooling nasty pre-spunk already, naughty boy? Keep fucking!"
play music "Sounds/wank.mp3"
scene marniefemdom09a with fastdissolve
$ renpy.pause(.2, hard=True)
scene marniefemdom09b with fastdissolve
$ renpy.pause(.2, hard=True)
scene marniefemdom09a with fastdissolve
$ renpy.pause(.2, hard=True)
scene marniefemdom09b with fastdissolve
$ renpy.pause(.2, hard=True)
scene marniefemdom09a with fastdissolve
$ renpy.pause(.2, hard=True)
scene marniefemdom09b with fastdissolve
$ renpy.pause(.2, hard=True)
scene marniefemdom09a with fastdissolve
$ renpy.pause(.2, hard=True)
scene marniefemdom09b with fastdissolve
$ renpy.pause(.2, hard=True)
scene marniefemdom09a with fastdissolve
$ renpy.pause(.2, hard=True)
scene marniefemdom09b with fastdissolve
$ renpy.pause(.2, hard=True)
scene marniefemdom09a with fastdissolve
$ renpy.pause(.2, hard=True)
scene marniefemdom09b with fastdissolve
$ renpy.pause(.2, hard=True)
scene marniefemdom09a with fastdissolve
$ renpy.pause(.2, hard=True)
scene marniefemdom09b with fastdissolve
$ renpy.pause(.2, hard=True)
scene marniefemdom09a with fastdissolve
$ renpy.pause(.2, hard=True)
scene marniefemdom09b with fastdissolve
$ renpy.pause(.2, hard=True)
scene marniefemdom09a with fastdissolve
$ renpy.pause(.2, hard=True)
scene marniefemdom09b with fastdissolve
$ renpy.pause(.2, hard=True)
scene marniefemdom10 with dissolve
stop music
mc "Uh... AAaah..."
ma "And now, CUM! BLAST IT ALL OUT FOR YOUR MISTRESS!"
scene marniefemdom11 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
ma "That's it, I want a MONSTERLOAD, you hear me?"
scene marniefemdom11 with fastflash
mc "Y...Yes Mistress, I'm cumming as hard as I can for you!"
ma "It's not ENOUGH, I want MORE!"
scene marniefemdom12 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
ma "That's better, just let it all out, SLAVE! Empty your cum factories for your Dominatrix!"
scene marniefemdom12 with fastflash
mc "AAAH, I'm blowing non-stop for you!"
scene marniefemdom13 with dissolve
ma "Mmmh, that was a MIGHTY load, slave... I'm giving you 5 stars on UberStud. Now get hard again and crawl ove to the bed!"
mc "Y...Yes my Femdom Queen..."
label MarnieFuckChoiceAx:
scene bedroom03b
show marniebed01 
with dissolve
ma "Let's see... What will we do next..."
stop music
menu:
    "Please ride me like the submissive slave I am!":
        ma "That's a good idea. MY idea actually, you hear me?"
        mc "Of course Mistress..."
        jump MarnieRidex
    "My dong deserves to be tortured into submission, Mistress.":
        ma "And I have the perfect tool for that. My TITS!"
        jump MarnieTitfuckx
    "I... Can't keep up... Please Mistress, I need to sleep!":
        ma "I will grant you a respite. Because you've been a good slave. So let's go to sleep. And back to my gallery."
        jump MarnieGallery

label MarnieRidex:
default marnietoldfastx = False
scene bedroom49
show marniefemdomprefuck01
with dissolve
ma "Just make sure that slave fuckstick of yours is REALLY HARD for me, cos I'm gonna ride it HARD AND FAST!"
play music "Sounds/barbarasex.mp3"
label MarnieFemdomSlowx:
hide marniefemdompovslow
hide marniefemdompovfast
hide marniefemdomfast
scene bedroom17
show marniefemdomslow
call screen marniefemdomslow01x
screen marniefemdomslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieFemdomEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MarnieFemdomFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("MarnieFemdomPOVSlowx") 

label MarnieFemdomFastx:
hide marniefemdompovslow
hide marniefemdompovfast
hide marniefemdomslow
scene bedroom17
show marniefemdomfast
if marnietoldfastx == False:
    ma "That's a good slave cock you got there, I'm gonna need to ride it FASTER!"
    $ marnietoldfastx = True
call screen marniefemdomfast01x
screen marniefemdomfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieFemdomEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MarnieFemdomSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("MarnieFemdomPOVFastx") 

label MarnieFemdomPOVSlowx:
hide marniefemdomfast
hide marniefemdomslow
hide marniefemdomfast
scene bedroom18
show marniefemdompovslow
call screen marniefemdompovslow01x
screen marniefemdompovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieFemdomEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MarnieFemdomPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MarnieFemdomSlowx") 

label MarnieFemdomPOVFastx:
if marnietoldfastx == False:
    ma "That's a good slave cock you got there, I'm gonna need to ride it FASTER!"
    $ marnietoldfastx = True
hide marniefemdomslow
hide marniefemdomslow
hide marniefemdomfast
scene bedroom18
show marniefemdompovfast
call screen marniefemdompovfast01
screen marniefemdompovfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieFemdomEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MarnieFemdomPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MarnieFemdomFastx") 
        
label MarnieFemdomEndx:
$ marnietoldfastx = False
ma "You've had enough enjoyment and I came enough times. So now, GIVE ME YOUR SEED!"
mc "Sure..I..."
ma "It's an ORDER, useless slave, do it NOW!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene bedroom18
show marniefemdomcum01
with fastdissolve
mc "...CUM! RHAAA!"
show marniefemdomcum01 with fastflash
ma "Ooh, that's GOOD, slave, keep PUMPING that load!"
hide marniefemdomcum01
show marniefemdomcum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Bend over, I'm gonna cover your back with my unending streams of boygoo! AAH!"
stop sound
hide marniefemdomcum02
show marniefemdomcum03
with fastdissolve
ma "You filled me up pretty good slave. Now your cocks is filthy with cum and pussy slime."
mc "I'm just a dirty boy, I mean, dirty slave...."
scene bedroom49 blurred
show marniefemdomcum04
with dissolve
ma "Yes you are, a DIRTY FILTHY BOY! You're lucky you have a MONSTER TEENAGE COCK, or you'd be lower than garbage to me!"
mc "My dick is just a piece of meat to serve you, Mistress..."
scene bedroom12
show marniefemdomcum05
with dissolve
ma "That's right, and right now it's filthy. I guess I'll clean it up then so you can give me some more HOT DICKING!"
play sound "Sounds/lick.mp3"
mc "Oh God Mistress, that's it, I'm staying ROCK-HARD FOR YOU!"
scene bedroom03b
show marniebed01
with dissolve
ma "Good. Now come over here, I'm not done with you yet..."
jump MarnieFuckChoiceAx
    
label MarnieTitfuckx:
scene bedroom16
show marniepretitfuck01
with dissolve
ma "Slide you legs apart so I can get snug and comfy between them. And your monstercock can get snug and comfy between THESE!"
scene bedroom16
show marnietitfuck00
with dissolve
ma "I'm going to totally bring you over the edge SLAVE, just watch!"
mc "Oh, I'm watching, I'm watching Mist..."
scene bedroom16 blurred
play music "Sounds/wank.mp3"
label MarnieTitfuckSlowx:
hide marnietitfuckfast
show marnietitfuckslow
call screen marnietitfuckslow01x
screen marnietitfuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieTitfuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MarnieTitfuckFastx") 

label MarnieTitfuckFastx:
mc "Oh Mistress, this is soo good!"
ma "But you haven't cum yet, I need to go even FASTER then!"
hide marnietitfuckslow
show marnietitfuckfast
call screen marnietitfuckfast01x
screen marnietitfuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieTitfuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MarnieTitfuckSlowx") 

label MarnieTitfuckEndx:
mc "I can't hold off any longer!"
ma "That's because NOBODY can survive Marnie's titfucks!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
hide marnietitfuckslow
hide marnietitfuckfast
show marnietitfuckcum01
with fastdissolve
mc "That's it, all for you Mistress, RHAAA!"
show marnietitfuckcum01 with fastflash
ma "ANd there's a LOT of it, nice one, SLAVE!"
scene bedroom20 blurred
show marnietitfuckcum02
with fastdissolve
mc "Oh God, you're pumping ALL the cum out of me Mistress! AAHH!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
with fastflash
ma "Stop lying, I can feel you're nowhere near to being DRAINED! So KEEP GOING!"
scene bedroom26 blurred
show marnietitfuckcum03
with dissolve
ma "That's better, huge plumes of young virile spunk, just like I love'em!"
with fastflash
mc "Oh God, I came so much, my balls, they hurt, Mistress..."
scene bedroom10 blurred
show marnietitfuckcum04
with dissolve
stop sound
play sound "Sounds/panting.mp3"
ma "You think I'm done with you? No way, I DEMAND ANOTHER LOAD of cum!"
mc "But I'm..."
ma "...drained? That's what YOU think. But my expert hands will prove otherwise!"
scene bedroom34 blurred
label MarnieHandjobSlowx:
show marniehandjobslow
call screen marniehandjobslow01x
screen marniehandjobslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieHandjobEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MarnieHandjobFastx") 

label MarnieHandjobFastx:
mc "Aaah, I NEED to CUM!"
ma "Do you now? Mmmh, let me wank that fat shaft FASTER then!"
hide marniehandjobslow
show marniehandjobfast
call screen marniehandjobfast01x
screen marniehandjobfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieHandjobEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MarnieHandjobSlowx") 

label MarnieHandjobEndx:
mc "Please, LET ME CUM MISTRESS!"
ma "Not until I say so!"
mc "But I can't..."
stop music
scene bedroom14 blurred
show marniehandjobcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
ma "You DISOBEYED! SO I'll RUIN your orgasm!"
scene bedroom30 blurred
show marniehandjobcum02
with dissolve
mc "AAAH, this is TORTURE, Marnie! Please remove your hand from my cumslit!"
ma "I told you NOT to cum, you're a BAD slave! Nevertheless..."
scene bedroom14 blurred
show marniehandjobcum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
ma "I want to see how FAR your jizz can flyafter I RUINED your blissful orgasm!"
mc "RHAAAA!"
scene bedroom41 blurred
show marniehandjobcum04
with dissolve
play music "Sounds/splooge02.mp3"
ma "Look at THAT! It's almost hitting the CEILING!"
ma "And it's making such a DISGUSTING gushing sound!"
scene bedroom30 blurred
show marniehandjobcum05
with dissolve
stop music
mc "GGgg... I feel... weakened."
ma "You'd better regain your strength and vigor, SLAVE, cos I'm  ain't done with you! So clean yourself up, you're FILTHY."
jump MarnieFuckChoiceAx

label MarnieGallery05:
play music "v07/datemusic.mp3"
scene bedroom01
show marnie02
ma "Let's have a hot night of MALEDOM BDSM!"
mc "Alright!"
ma "That's right, I want you to DOMINATE ME. Any which way you want."
mc "Yee-ha!"
hide marnie02
show marnie01
with fastdissolve
ma "I brought some... things for you to prepare for the evening. Have a look at them while I change into my submissive slut outfit..."
hide marnie01 with dissolve
mc "And I'll go and sit in the sofa while I wait."
scene marniemaledom00 with dissolve
mc "So, what do we have here... Anal beads. Nice."
mc "And a gag for some master-slave bondage. Alright, we're in business!"
scene bedroom02
show marniemaledom03 with moveinright
ma "I'm a filthy slut Master, treat me like one."
mc "I see. You certainly dress like one."
hide marniemaledom03
show marniemaledom02
with fastdissolve
ma "Yes, I am so ashamed of myself for being such a whore. I deserve to be punished."
mc "Right, right, you sure do. Turn round."
hide marniemaledom02
show marniemaledom01
with fastdissolve
ma "I'm such a depraved slut, I got tattoos about it all over my body."
scene bedroom02 blurred
show marniemaledom01b
with fastdissolve
mc "Indeed. This one seems to imply you are a nothing more than a fuck toy."
ma "That's exactly what I am. YOUR fuck toy. To dispose of as you wish. Including with the help of those sex toys I gave you... *wink*"
hide marniemaledom01b
show marniemaledom03b
with dissolve
ma "And as you can see, this most embarrassing one clearly states that my pussy is free to be used as a cumdump."
mc "I'm getting rockhard just thinking about all the nasty stuff we're going to do together my little fuck toy."
scene bedroom02
show marniemaledom02
ma "Then let me take care of your giant teenage love muscle please Master!"
mc "Alright. Get on your knees and crawl towards me..."
scene marniemaledom04 with dissolve
ma "Oh, Master, your cock... It's so big and beautiful! Does a filthy whore like me really deserve to worship such a magnificent fuckpole?"
scene marniemaledom05 with dissolve
play sound "Sounds/lick.mp3"
mc "If you do a good job on it, you might..."
scene marniemaledom06 with dissolve
play sound "Sounds/boymoan.mp3"
mc "AAAH, your tongue... It's so warm..."
play sound "Sounds/lick.mp3"
scene marniemaledom06b with dissolve
ma "My mouth is even warmer... And your magnificent cock deserves to be warm..."
mc "Yeah, uh..."
stop music
play music "Sounds/hardsucking.mp3"
label MarnieMaledomSlowx:
hide marniemaledomblowfast
show marniemaledomblowslow
call screen marniemaledomblowslow01x
screen marniemaledomblowslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieMaledomEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MarnieMaledomFastx") 

label MarnieMaledomFastx:
mc "Do it faster, suck it DEEP!"
hide marniemaledomblowslow
show marniemaledomblowfast
call screen marniebedroomfuckfast01x
screen marniebedroomfuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieMaledomEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MarnieMaledomSlowx") 

label MarnieMaledomEndx:
stop music
scene marniemaledom07c with dissolve
play music "Sounds/splooge02.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Of fuck, that's it, I'm NUTTING DOWN YOUR THROAT!"
with fastflash
mc "Drink it all, SLAVE SLUT!"
scene marniemaledom08 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "God, sssooo goood, AAHHH!"
with fastflash
mc "That's it, open that throat WIDE! RHAAA!"
stop music
stop sound
scene marniemaledom08b with dissolve
mc "You did good my little cumbucket... But you didn't catch it all."
ma "I am sorry Master, I was so unworthy of your superior alpha-seed monsterload..."
mc "Then you need to be punished. Stick those anal beads where the sun don't shine."
scene marniemaledom09 with dissolve
ma "That's it Master, they are almost all in, I'll just leave a few beads out so you can play with them as you wish."
mc "That's good. Come over here now..."
scene marniemaledom10 with dissolve
mc "I'll pull them out slowly at first..."
scene marniemaledom11 with fastdissolve
mc "...And then, I'll rip them out!"
play sound "Sounds/moaning03.ogg"
ma "Ouch! My poor worthless rosebud..."
mc "You talk too much. Put on that mouthgag so I don't hear you interrupt me."
ma "Of course Master, I am so sorry that I..."
mc "SILENCE, slave!"
scene marniemaledom12 with dissolve
mc "That's better. I like you like that, just a mindless fuckdoll."
scene marniemaledom13 with dissolve
ma "Mmmm...Gbmmm!"
mc "Yeah, you were saying?"
mc "I guess I should ungag you, I like to hear my slave SCREAMING when I fuck them. And I'm hard again, so let's move to the bed!"

label MarnieFuckChoiceBx:
scene bedroom03b
show marniebed02 
with dissolve
ma "I am ready to be your slave-slut, [name]..."
mc "Let's see... What will we do next..."
stop music
menu:
    "A dirty slave likes you deserves a severe punishment. My cum missile in your ARSE!":
        ma "That will be tremendously painful Master, I'm not sure I even deserve such..."
        mc "Silence, SLUT! And get on your back, I'm going to smother your face with my fat nutsack for starters..."
        ma "Of course, Master... Oooh..."
        jump MarnieAnalx
    "I need to unload pronto. Twice at least. So spread your legs for my cum-missile!":
        ma "Of course, my hole is a free ride for you and your mega-dong!"
        jump MarnieMaledomFuckx
    "I'm done, let's go to sleep. And leave that cum on you as a mark of my ownership.":
        ma "Of course Master, I deserve nothing less than to sleep with your stinky scum covering me. And to go back to my gallery."
        jump MarnieGallery

label MarnieAnalx:
scene bedroom09
show marniepreanal01
with dissolve
mc "Let's see what we have here... I should prep that rosebud of yours because it's so tiny compared to my alpha-MASTERCOCK!"
scene bedroom34
show marniepreanal02
with dissolve
play sound "Sounds/lick.mp3"
mc "Yeah, that's it, lick those balls good and make them churn up a HUGE load for your backdoor!"
scene bedroom09 blurred
show marniepreanal03
with dissolve
play sound "Sounds/moaning.mp3"
mc "Yeah, I think you're ready down there... You're leaking filthy slime all over the place."
scene bedroom16
show marniepreanal04
with dissolve
mc "Therefore... You are READY to take on my MASSIVE pillar of lust!"
ma "Oh, I am, Sir, please fuck me BRUTALLY in the ass, like I deserve to!"
play music "Sounds/fucksound.mp3"
label MarnieAnalSlowx:
hide marnieanalfast
hide marnieanalpovfast
hide marnieanalpovslow
scene bedroom16 blurred
show marnieanalslow
call screen marnieanalslow01x
screen marnieanalslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MarnieAnalFastx") 
    imagebutton:
        focus_mask True
        idle "v07/frontidle.png"
        hover "v07/frontidle.png"
        action Jump ("MarnieAnalPOVSlowx")

label MarnieAnalFastx:
hide marnieanalslow
hide marnieanalpovfast
hide marnieanalpovslow
scene bedroom16 blurred
show marnieanalfast
call screen marnieanalfast01x
screen marnieanalfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MarnieAnalSlowx") 
    imagebutton:
        focus_mask True
        idle "v07/frontidle.png"
        hover "v07/frontidle.png"
        action Jump ("MarnieAnalPOVFastx") 

label MarnieAnalPOVSlowx:
hide marnieanalslow
hide marnieanalfast
hide marnieanalpovfast
scene bedroom18 blurred
show marnieanalpovslow
call screen marnieanalpovslow01x
screen marnieanalpovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MarnieAnalPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MarnieAnalSlowx") 

label MarnieAnalPOVFastx:
hide marnieanalslow
hide marnieanalfast
hide marnieanalpovslow
scene bedroom18 blurred
show marnieanalpovfast
call screen marnieanalpovfast01x
screen marnieanalpovfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("MarnieAnalPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MarnieAnalFastx") 

label MarnieAnalEndx:
mc "I'm getting close, my little anal-whore! Get ready for blast-off!"
scene bedroom16 blurred
show marnieanalcum01
with dissolve
stop music
play music "Sounds/splooge02.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...NOW! RHAAAA!"
with fastflash
ma "Yes Master, I can feel your MONSTER jets of boyspunk filling my filthy backhole!"
mc "I think you need to be branded with my scum!"
stop music
scene bedroom18 blurred
show marnieanalcum02
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
ma "Ooh, I've such a depraved cum-whore, gimme more Master, COVER me in your naughty teenage cream!"
with fastflash
mc "I will, I'm not done yet, by a LONG..."
scene bedroom30 blurred
show marnieanalcum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "...SHOT! RHAAA!"
with fastflash
ma "It's so HOT on my back and it's so THICK too!"
scene bedroom16 blurred
show marnieanalcum04
with dissolve
mc "Now I OWN YOU, you hear me?"
ma "Y...Yes, Master, I am your devoted cum slut for LIFE!"
mc "Good, now clean yourself up and let's see what else we can do..."
jump MarnieFuckChoiceBx
    
label MarnieMaledomFuckx:
scene maledomprefuck01 with dissolve
ma "You're ssooo BIG Master! Your cock si such an alpha-pussywrecker! I don't know if I deserve it..."
scene maledomprefuck02 with dissolve
mc "You don't really, but you're the only fuckhole around and I'm SUPER-HORNY!"
ma "Oooh, I'm such a depraved cockwhore, I'll just do anything for you, Master."
play music "Sounds/fucksound.mp3"
label MarnieMaledomFuckSlowx:
hide marniemaledomfast
hide marniemaledompovfast
hide marniemaledompovslow
scene bedroom18
show marniemaledomslow
call screen marniemaledomslow01x
screen marniemaledomslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieMaledomFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MarnieMaledomFuckFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("MarnieMaledomFuckPOVSlowx")

label MarnieMaledomFuckFastx:
hide marniemaledomslow
hide marniemaledompovfast
hide marniemaledompovslow
scene bedroom18
show marniemaledomfast
call screen marniemaledomfast01x
screen marniemaledomfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieMaledomFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MarnieMaledomFuckSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("MarnieMaledomFuckPOVFastx") 

label MarnieMaledomFuckPOVSlowx:
hide marniemaledomslow
hide marniemaledomfast
hide marniemaledompovfast
scene bedroom14 blurred
show marniemaledompovslow
call screen marniemaledompovslow01x
screen marniemaledompovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieMaledomFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MarnieMaledomFuckPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MarnieMaledomFuckSlowx") 

label MarnieMaledomFuckPOVFastx:
hide marniemaledomslow
hide marniemaledomfast
hide marniemaledompovslow
scene bedroom14 blurred
show marniemaledompovfast
call screen marniemaledompovfast01x
screen marniemaledompovfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieMaledomFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("MarnieMaledomFuckPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MarnieMaledomFuckFastx") 

label MarnieMaledomFuckEndx:
scene maledomcum01 with dissolve
play music "Sounds/splooge02.mp3"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Fuck yeah, blowing my load in my litttle cum dumpster slave! RHAAA!"
with fastflash
ma "You're giving me ssooo much of your sweet boycream!"
scene maledomcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "That's cos you're just a cum-dump for it, RHAAAA!"
with fastflash
ma "I am, just use me like a cheap cumwhore! AAAH, I'm squirting on your GIANT DONKEY-DICK!"
stop sound
stop music
scene maledomcum03 with dissolve
play sound "Sounds/panting.mp3"
mc "I'm not done yet. When you have a slave slut like you around, one needs to take advantage of it!"
ma "Oh my God Master, you're STILL HARD! You're gonna dump ANOTHER GIANT LOAD inside me? That'll be an extra two tattoo ticks on my slutty body!"
play music "Sounds/barbarasex.mp3"
label MarnieMaledomPostSlowx:
hide marniemaledompostfast
show marniemaledompostslow
call screen marniemaledompostslow01x
screen marniemaledompostslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieMaledomPostEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MarnieMaledomPostFastx") 

label MarnieMaledomPostFastx:
ma "Use my pussy as your cum-filled cock sleeve, pound it as fast as you wish!"
hide marniemaledompostslow
show marniemaledompostfast
call screen marniemaledompostfast01x
screen marniemaledompostfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MarnieMaledomPostEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MarnieMaledomPostSlowx") 

label MarnieMaledomPostEndx:
ma "I can feel your balls RUMBLE! Fill me up again please [name]!"
mc "Do you think you deserve it?"
ma "I don't of course, I'm just a filthy cum dump for you to deposit your dirty spunk whenever you need to empty your monster balls, Master!"
mc "Then I'll do just that..."
stop music
show maledompostcum01 with dissolve
play sound "v07/creampie.mp3"
mc "AAAH, I'm nutting again!"
with fastflash
ma "Ooh, it's SPLASHING everywhere, my pussy was already so FULL!"
scene maledompostcum02 with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Still more SPUNK spewing!"
with fastflash
ma "I feel so fulfilled... As the cheapest cumslave in the compound!"
scene bedroom18
show maledompostcum03
with dissolve
ma "Oh Master, you were so... masterful!"
mc "You liked it? You were not supposed to! You need more punishment!"
jump MarnieFuckChoiceBx

