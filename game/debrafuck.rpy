label DebraFuck01:
hide screen calendar
hide screen mcstats
$ alienfuck = True
$ weekfuckeddebra = True
scene bedroom01
show debrahappy02
with fade
menu:
    "Run scene":
        pass
    "Skip scene":
        jump DebraEnd
de "Ah, I'm glad you called, I have many SEX EXPERIMENTS in mind!"
mc "Err... OK. How about you get me in the mood Debra?"
hide debrahappy02
show debratalking01
with fastdissolve
de "Aren't you already in the mood by the mere mention of SEX mixed with SCIENCE?"
mc "Sure, I mean. Whatever. Just get into some sexy lingerie will you? There's always a scene like that with most harem girls."
hide debratalking01
show debrapensive
with fastdissolve
de "In my infinite generosity, I will give you a choice. Described in the next menu screen..."
menu:
    "Choose the vibration control outfit":
        $ chosedebravibration = True
        hide debrapensive
        show debratalking02
        with fastdissolve
        de "For once, YOU will be in control of MY PLEASURE..."
        jump DebraLingerie01
    "Choose the experimental succubus outfit":
        hide debrapensive
        show debrahappy01
        with fastdissolve
        de "A bold move... Curiosity got the better of you!"
        jump DebraLingerie02
        
label DebraLingerie01:
play music "v07/datemusic.mp3"
scene bedroom02 with fade
show debravibro01 at center with moveinright
de "Evrything is in place, as you can see..."
mc "Damn. Doesn't that hurt?"
hide debravibro01
show debravibro02
with fastdissolve
de "A little bit, it's GOOD pain. So take a GOOD look."
mc "Ooh yeah, I will.."
scene bedroom02 blurred
show debravibro03
with dissolve
mc "I will. So how does it work?"
hide debravibro03
show debravibro04
with fastdissolve
de "Here is the controller. You can activate each clamp by number. Number 1 for left nipple, number two for right nipple and number three for clit. You think you can remember?"
mc "Sure prof!"
scene debravibrosofa01 with dissolve
de "I'm ready for pleasurable electrical torture... Activate button 2 [name]!"
scene debravibrosofa02 with dissolve
play sound "Sounds/taser.mp3"
scene debravibrosofa02 with hpunch
de "Ooooh.. That's nice... And now the other nipple please..."
scene debravibrosofa03 with dissolve
play sound "Sounds/taser.mp3"
scene debravibrosofa03 with hpunch
de "AAAH! MORE, KEEP GOING!"
play sound "Sounds/taser.mp3"
scene debravibrosofa03 with hpunch
mc "More?"
de "Puff.. The clit NOW..."
scene debravibrosofa04 with dissolve
play sound "Sounds/taser.mp3"
scene debravibrosofa04 with hpunch
de "Gggg..."
mc "I'll take that as a sign I should keep going... I think I'll press ALL the buttons at once actually..."
scene debravibrosofa05 with dissolve
play sound "Sounds/taser.mp3"
scene debravibrosofa05 with hpunch
de "Oooohhh ---- my ---- GODDDD!"
scene debravibrosofa04 with dissolve
play sound "Sounds/taser.mp3"
scene debravibrosofa04 with hpunch
play sound "Sounds/moaning03.ogg"
de "My clit, it's vibbrrr-ATING!"
scene debravibrosofa06 with dissolve
play sound "Sounds/womanscream.ogg"
de "I'm CU-UUU-MMING!"
mc "Damn, that's a squirting WATERFALL!"
scene debravibrosofa07 with dissolve
mc "Let me help you in cleaning this up..."
de "Mmmh, that's a good boy..."
play sound "Sounds/slurp.mp3"
scene debravibrosofa08 with dissolve
play sound "Sounds/moaning02.mp3"
if debralustvibro == False:
    call LustPlusDebra
    $ debralustvibro = True
mc "And now, it's time for the REAL fun to begin. Get those things off and hop on the bed, Debra!"
stop sound
scene debrabed01 with dissolve
de "Like this? So I am at your mercy and you can decide whatever you want to do with me?"
mc "That's right..."
jump DebraFuckChoice

label DebraLingerie02:
play music "v07/datemusic.mp3"
scene bedroom02 with fade
show debrasuccubus01 at center with moveinright
de "I made it myself! I call it the Sucubbus Outfit."
mc "It's... different."
hide debrasuccubus01
show debrasuccubus02
with fastdissolve
de "Oh, it IS different. Scientifically proven to induce a rush of dopamine in horny tenage boys..."
mc "I see... I can feel that dopamine right NOW..."
hide debrasuccubus02
show debrasuccubus03
with fastdissolve
de "It's almost MESMERIZING, don't you think?"
mc "Yes... Let me a have a closer mesmerized look..."
scene bedroom02 blurred
show debrasuccubus04
with dissolve
mc "Yeah, now I'm totally mesmerized... Fuck yeah..."
scene bedroom02
show debrasuccubus05
with dissolve
de "But look. It comes with a special equipment... *wink*"
mc "What's that?"
de "Let me demonstrate... On your HARD cock!"
scene debramcsofa01 with dissolve
de "See? I place it over your apple-sized helmet... Like so..."
mc "Is is going to hurt?"
de " A little bit... Where's the fun if it doesn't?"
mc "But..."
stop music
play channel1 "Sounds/wank.mp3"
play channel2 "Sounds/boymoan02.mp3"
label DebraHandSlow:
hide debrahandfast
show debrahandslow
call screen debrahandslow01
screen debrahandslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraHandEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DebraHandFast") 

label DebraHandFast:
de "Your cock seems to like that. A LOT. So let's do it FASTER!"
hide debrahandslow
show debrahandfast
call screen debrahandfast01
screen debrahandfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraHandEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DebraHandSlow") 

label DebraHandEnd:
mc "Deb...Debra, I'm gonna cum!"
de "That was the whole point of this experiment, so go ahead [name]!"
stop channel1
stop channel2
scene debramcsofawankcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
de "That's it, AAAAH!"
window hide
with fastflash
de "Oooh, the succubus sucked your mojo right out of your cumslit!"
scene debramcsofawankcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
de "Still more splooge for me and my cock-jerker?"
window hide
with fastflash
mc "Gggg! RHAAAA!"
de "YEAH, let it SHOOT OUT!"
scene debramcsofawankcum03 with dissolve
play sound "Sounds/lick.mp3"
mc "Oh GOD! This thing... Just too much."
de "Nonsense. You cock is still sufficiently hard to indulge in more experimental sex. On the bed."
play sound "Sounds/lick.mp3"
de "Let me... *slurp*  lick that yummy cream first, then I'll get naked and wait for you over there. You'd better not make me wait, STUD!"
if debralustsuccubus == False:
    call LustPlusDebra
    $ debralustsuccubus = True
scene debrabed01 with dissolve
de "Ah, I see you completely recovered and your balls seems to be as full as ever. Good. What shall we do to empty them properly then?"

label DebraFuckChoice:
stop music
menu:
    "I'll give you control this time. Ride me cowgirl style!" if chosedebravibration:
        de "I'm going to enjoy this as much as YOU will, cowboy!"
        jump DebraRide
    "Since you're a Succubus, ride me to Valhalla!" if chosedebravibration == False:
        de "I think you got your mythology mixed up but I'm game!"
        jump DebraRide
    "Let's do something more traditional. Me fucking you senseless doggy.":
        de "I suppose we could try that. For a change of pace."
        jump DebraSex 
    "Treat me like a slave. A lab assistant basically.":
        de "Lab assistants have to clean up the mess after an experiment. So get on your knees and get cleaning!"
        jump DebraSlave
    "Some players are heavily into FMG. But we're far away from the alpha-X-ray machine, so I guess they're screwed." if debramuscles == False:
        scene debraprehuge01 with dissolve
        $ debramuscles = True
        de "Far from it! I have designed a miniature version of my successful machine..."
        mc "That tiny dildo thing? How is that even scientifically plausible?"
        de "Don't ask questions and just go with the flow [name]..."
        jump DebraHuge
    "Why don't you use that female muscle growth dildo or whatever it is?" if debramuscles:
        scene debraprehuge01 with dissolve
        de "You want some MUSCLE SEX, hey? I'll give you MUSCLE SEX then!"
        jump DebraHuge
    "I'm done, let's go to sleep.":
        jump DebraEnd

label DebraRide:
scene debrapreride01 with dissolve
de "I'm going to take control of that cock now. Are you ready [name]?"
mc "Sure, you go right ahead..."
scene debrapreride02 with dissolve
de "Let me first engulf that monster cockhead of yours... Do NOT move!"
mc "I am as still as a male sex doll. The one with the giant cock."
scene debraride00 with dissolve
play sound "Sounds/womanscream.ogg"
de "* Puff...* Nice and snug inside me and now..."
play music "Sounds/fucksound.mp3"
label DebraRideSlow:
scene debrarideslow
with fastdissolve
call screen debrarideslow01
screen debrarideslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraRideEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DebraRideFast") 

label DebraRideFast:
scene debraridefast
with fastdissolve
call screen debraridefast01
screen debraridefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraRideEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DebraRideSlow") 

label DebraRideEnd:
mc "I don't think I can hold much longer Debra... Where... Where do you want me to cum?"
de "CUM INSIDE MY SNATCH!"
stop music
scene debraridecum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
de "Oh yeah, I will to estimate the volume of cum you can ejaculate with the cum sensors I have placed at strategic points inside my poontang and uterus..."
window hide
with fastflash
mc "Wh.. What? Oh God, AAAH!"
scene debraridecum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
de "That's it, keep blowing, you're up to 500ml of spunk, I want MORE!"
window hide
with fastflash
mc "OOOOH, AAAH!"
scene bedroom41 blurred
show debraridecum03
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
de "You know how much young virile seed you have ejaculated so far [name]?"
window hide
with fastflash
mc "N...no... AAAH! How much?"
window hide
with fastflash
de "A whopping 800ml!"
scene debraridecum04 with dissolve
play sound "Sounds/panting.mp3"
mc "Phew... Is that good?"
de "It is adequate I would say. But NOT SUFFICIENT!"
scene debraridecum05 with dissolve
mc "Hang on, wh.. what are you doing???"
de "I also have sensors in my ASS! So let's try the other hole, shall we?"
scene debrarideass00 with dissolve
play sound "Sounds/womanscream.ogg"
de "UUURH! It's so BIG! But your cock is already nicely lubricated with your copious juices so I can do it!"
play music "Sounds/debrasex.mp3"
label DebraRideAssSlow:
scene debrarideassslow
with fastdissolve
call screen debrarideassslow01
screen debrarideassslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraRideAssEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DebraRideAssFast") 

label DebraRideAssFast:
scene debrarideassfast
with fastdissolve
call screen debrarideassfast01
screen debrarideassfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraRideAssEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DebraRideAssSlow") 

label DebraRideAssEnd:
de "I can feel your monster rumbling... You must be close to delivering your SECOND MONSTERLOAD then!"
mc "I... AAAH!"
stop music
scene debrarideasscum01 with dissolve
play music "Sounds/splooge01.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "... CUMMING NOW! RHAAA!"
window hide
with fastflash
de "Ooh, it's well on its way to being a BIG ONE AGAIN!"
scene debrarideasscum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "FUCK, YOUR TIGHT ASS IS MILKING ME!"
window hide
with fastflash
de "And your giant cock is STRETCHING ME!"
stop music
scene debrarideasscum03 with dissolve
play sound "Sounds/panting.mp3"
de "Seems like you're out. For now."
mc "How much did I come this time?"
scene bedroom41 blurred
show debraridecum03
with dissolve
de "My sensors indicate a whopping 500ml of warm spunk sloshing in my colon... Are you ready for MORE? Cos I am!"
mc "Sure... Just give me a minute or so to recover..."
stop sound
scene debrabed01 with dissolve
de "A minute has passed. And I'm horny."
jump DebraFuckChoice
    
label DebraSex:
scene debrapresuck00 with dissolve
de "Before you stick your giant pud in my tight hole, I want to lick it..."
mc "Be my guest, Professor..."
scene debrapresuck01 with dissolve
play sound "Sounds/lick.mp3"
de "First those balls... * lick* That never fail to deliver HUGE amounts of sweet teenage spunk..."
mc "You're damn right!"
scene debrapresuck02 with dissolve
play sound "Sounds/lick.mp3"
de "...Then that veiny THICK shaft..."
mc "Oh yeah!"
play music "Sounds/lick.mp3"
scene debrapresuck03 with dissolve
de "All the way up its amazing length..."
play music "Sounds/slurp.mp3"
scene debrapresuck02 with dissolve
scene debrapresuck03 with dissolve
scene debrapresuck02 with dissolve
scene debrapresuck03 with dissolve
scene debrapresuck02 with dissolve
stop music
de "Ssooo tasty..."
scene debrapresuck04 with dissolve
play sound "Sounds/lick.mp3"
de "Let me suck on that tip. And..."
play channel1 "Sounds/hardsucking.mp3"
play channel2 "Sounds/boymoan02.mp3"
label DebraSuckSlow:
scene debrasuckslow
with fastdissolve
call screen debrasuckslow01
screen debrasuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraSuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DebraSuckFast") 

label DebraSuckFast:
scene debrasuckfast
with fastdissolve
call screen debrasuckfast01
screen debrasuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraSuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DebraSuckSlow") 

label DebraSuckEnd:
mc "Get down that shaft, swallow it deeper into your throat Debra!"
label DebraSuck02Slow:
scene debrasuck02slow
with fastdissolve
call screen debrasuck02slow01
screen debrasuck02slow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraSuck02End")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DebraSuck02Fast") 

label DebraSuck02Fast:
scene debrasuck02fast
with fastdissolve
call screen debrasuck02fast01
screen debrasuck02fast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraSuck02End")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DebraSuck02Slow") 

label DebraSuck02End:
stop channel1
stop channel2
mc "Oh fuck, that's it, I'm gonna..."
scene debrasuckcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...CUM! AAAH!"
with fastflash
mc "CUMMING DOWN YOUR GULLET, RHAAA!"
scene debrasuckcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
de "Gllurb!!!!"
with fastflash
mc "Yeah, swallow that load, Debra!"
scene debrasuckcum03 with dissolve
mc "Damn, that was a blowjob and a half. I don't even know where my cock went."
de "* slurp * Straight down my stomach, that's where."
scene debrasuckcum04 with dissolve
de "And now... * slurp *... It's going to go straight into my womb! I want YOU to fuck me DEEP and HARD!"
mc "Alright! That was the option I chose at the end of the day."
scene debrapredoggy01 with dissolve
de "Don't go easy on me, pound that pussy [name], show me what a STUD you are!"
play music "Sounds/womansex01.mp3"    
label DebraSexSlow:
scene debradoggyslow
with fastdissolve
call screen debradoggyslow01
screen debradoggyslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraSexEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DebraSexFast") 

label DebraSexFast:
scene debradoggyfast
with fastdissolve
call screen debradoggyfast01
screen debradoggyfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraSexEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DebraSexSlow") 

label DebraSexEnd:
de "You're gonna cum again [name]? I can feel your BEAST GROWING INSIDE ME!"
mc "That's right, I'm getting real close..."
scene debradoggycum01 with dissolve
play music "Sounds/splooge01.mp3"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Here it COMES!"
de "YES, fill my snatch with your ball-batter!"
scene debradoggycum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Still pumping, RHAAA!"
window hide
with fastflash
de "Oh, this is a DELUGE of cum!"
scene debradoggycum03 with dissolve
play sound "Sounds/womanscream.ogg"
mc "And now, take my load even DEEPER! OOOH!"
window hide
with fastflash
de "You're just using my uterus as a cum dump, AAAH!"
scene debradoggycum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Fuck yeah!"
window hide
with fastflash
scene debradoggycum03 with dissolve
play sound "Sounds/womanscream.ogg"
$ renpy.pause(.5, hard=True)
window hide
with fastflash
scene debradoggycum02 with dissolve
$ renpy.pause(.5, hard=True)
window hide
with fastflash
scene debradoggycum03 with dissolve
play sound "Sounds/womanscream.ogg"
$ renpy.pause(.5, hard=True)
window hide
with fastflash
stop music
mc "That's it, I think, I'm done RHAAA!"
scene debradoggycum04 with dissolve
play sound "Sounds/womanmoan.mp3"
de "My poor pussy just got an in-depth lesson in fluid dynamics... Oooh..."
mc "Those fluids are now leaking out from where I'm standing..."
de "I know... Let me... clear my gaping tunnel and recover a bit..."
mc "Hurry up Debra, I'm STILL HARD!"
scene debrabed01 with dissolve
de "So you are indeed... Which means?..."
jump DebraFuckChoice

label DebraSlave:
scene debraslave01 with dissolve
de "That's it, I want you to lick my pussy and make it SHINY!"   
mc "Oh, I will, it looks so yummy."
play music "Sounds/lick.mp3"    
scene debraslave02 with dissolve
$ renpy.pause(0.4, hard='True')
scene debraslave03 with dissolve
de "I'll shake my booty while you twirl your tongue in there."
scene debraslave02 with dissolve
$ renpy.pause(0.4, hard='True')
scene debraslave03 with dissolve
$ renpy.pause(0.4, hard='True')
scene debraslave02 with dissolve
$ renpy.pause(0.4, hard='True')
scene debraslave03 with dissolve
$ renpy.pause(0.4, hard='True')
scene debraslave02 with dissolve
$ renpy.pause(0.3, hard='True')
scene debraslave03 with dissolve
$ renpy.pause(0.3, hard='True')
scene debraslave02 with dissolve
$ renpy.pause(0.3, hard='True')
scene debraslave03 with dissolve
$ renpy.pause(0.3, hard='True')
scene debraslave02 with dissolve
$ renpy.pause(0.3, hard='True')
scene debraslave03 with dissolve
$ renpy.pause(0.3, hard='True')
stop music
play sound "Sounds/womanmoan.mp3"
de "That's nice but... You need better access to my snatch. I really want to feel your tongue slide ALL OVER IT."
de "Now you stay on your knees like a good little underling and I'll lie on my back on the bed."
scene debraslave04 with dissolve
play sound "Sounds/slurp.mp3"
play music "Sounds/moaning.mp3"    
de "Mmh, yeah, that's even better..."
scene debraslave05 with dissolve
de "And now, keep licking while I hold your head in place with my strong thighs..."
play music "Sounds/moaning02.mp3"
play sound "Sounds/lick.mp3"
de "That's a good slave. Oooh..."
scene debraslave06 with dissolve
play music "Sounds/moaning03.ogg"
play sound "Sounds/lick.mp3"
de "Yes, YES! You're getting me there, slave, don't stop! AAAH!"
scene debraslave07 with dissolve
de "This was good... But I want to feel your tongue on my rosebud now. I want to SQUIRT all over your dirty boy's face!"
scene debraslave08 with dissolve
play sound "Sounds/slurp.mp3"
de "Yeah, lap it up, [name], ooh, this tickles, sssooo good!"
scene debraslave09 with dissolve
play music "Sounds/splooge01.mp3"
play sound "Sounds/womanscream.ogg"
de "AAAAH! I'm CUMMING!"
window hide
with fastflash
de "Sssooo much squirting, AAAH!"
scene debraslave10 with dissolve
stop music
play sound "Sounds/panting.mp3"
de "Well, look at you. It's YOUR turn to be covered in MY juices. You're a DIRTY BOY!"
mc "I'll...I'll clean up. Like a good underling."
de "And don't you dare go SOFT on me."
scene debrabed01 with dissolve
de "Now that you're nice and clean, I DEMAND some hot sex from your MASSIVELY-SWOLLEN DONKEY-DICK!"
jump DebraFuckChoice

label DebraHuge:
scene debraprehuge02 with dissolve
de "All I have to do is stick this device up my poontang. Like so."
scene debraprehuge03 with dissolve
play sound "Sounds/moaning.mp3"
de "As DEEP as it will go... Then press the... *puff*... level 4 button right here..."
play music "Sounds/radiation01.mp3"
mc "You're sure you don't want to go through levels 1 to 3 first?"
de "Who's the scientist here?"
scene debraprehuge04 with dissolve
play sound "Sounds/womanscream.ogg"
mc "I hope you don't grow a cock is all..."
scene debraprehuge04 with hpunch
de "Don't be silly now."
scene debraprehuge05 with dissolve
de "I can feel my... MUSCLES GROWING!"
scene debraprehuge05 with hpunch
mc "Shit, it's actually working. Cray-ay-zy."
scene debraprehuge06 with dissolve
play sound "Sounds/plop.mp3"
stop music
mc "Look at you, Professor Debra, you're MASSIVE!"
window hide
with fastflash
de "AAARGH!"
scene debraprehuge07 with dissolve
de "That's right, and my MASSIVE body demands a MASSIVE FUCK!"
de "You'd better be quick about it, the effects will wear off pretty soon..."
mc "Ok, fast fucking, here we go!"
play music "Sounds/fucksound.mp3"
label DebraHugeSlow:
scene debrahugeanimslow
call screen debrahugeslow01
screen debrahugeslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraHugeEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DebraHugeFast") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("POVDebraHugeSlow") 

label DebraHugeFast:
mc "You want it even faster, Debra?"
de "Yes, POUND ME HARDER TOO!"
scene debrahugeanimfast
call screen debrahugefast01
screen debrahugefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraHugeEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("DebraHugeSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("POVDebraHugeFast") 

label POVDebraHugeSlow:
scene debrahugepovanimslow
call screen povdebrahugeslow01
screen povdebrahugeslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraHugeEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasteridle.png"
        action Jump ("POVDebraHugeFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("DebraHugeSlow") 

label POVDebraHugeFast:
mc "And now, even FASTER FUCKING!"
scene debrahugepovanimfast
call screen povdebrahugefast01
screen povdebrahugefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraHugeEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("POVDebraHugeSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("DebraHugeFast") 

label DebraHugeEnd:
de "Cum before the effects wear off [name]!"
mc "Good thing I'm really close because the player pressed the NEXT button in time..."
stop music
scene debrahugecum01 with dissolve
play music "Sounds/splooge02.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Take that, you muscled huge-titted sizequeen! RHAAA!"
window hide
with fastflash
de "Pound that pussy with your young seed! Just fill it to the brim!"
scene debrahugecum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "That's it, I'm cumming non-stop inside you! AAAH!"
window hide
with fastflash
de "YES! FLOOD MY CUNT!"
scene debrahugecum01 with dissolve
de "MORE, MORE!"
scene debrahugecum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "UUUH, AAAH!"
window hide
with fastflash
de "You've got some more left? For my huge VEINY breasts?"
stop music
scene debrahugecum03 with dissolve
play music "Sounds/moaning02.mp3"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Of course, there you go!"
window hide
with fastflash
de "Damn, that's one HUGE CUMSHOT [name]!"
window hide
with fastflash
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "And another one!"
window hide
with fastflash
mc "And..."
stop music
scene debrahugecum04 with dissolve
mc "...I'm spent now. Not for long of course."
de "Obviously. An alpha-irradiated STALLION like you can keep it up for HOURS. It's basic science really."
scene debrahugecum05 with dissolve
play sound "Sounds/womanmoan.mp3"
mc "Uh oh, look like your monster muscles are shrinking, Debra..."
de "Yes, I can see that. As I predicted. I told you the effects are only temporary."
scene debrahugecum06 with dissolve
de "Let me taste that still warm spunk you've covered me with while my body adjusts back to its normal size..."
mc "Of course, be my guest. This protein shake is free of charge."
scene debrabed01 with dissolve
de "I'm back to normal and totally clean again. Therefore, I am ready for some MORE SEX."
jump DebraFuckChoice
    
label DebraEnd:
show screen calendar
show screen mcstats
scene debrasleep with fade
$ loc = "bedroom"
play sound "Sounds/snoring.mp3"
pause 3
call NewDay
jump Bedroom