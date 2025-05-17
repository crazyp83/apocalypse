label KimberlyGallery:
call screen gallerykimberly
screen gallerykimberly:
    add "Gallery/kimberlygallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("gallerykimberly"), Jump ("MainGallery")]

    if renpy.seen_image("ivankawhitehouse blurred"):
        imagebutton:
            focus_mask True
            idle "Gallery/ivankagallery10.png" xpos 621 ypos 100
            hover "Gallery/ivankagallery10.png"
            action Jump ("KimberlyGallery01")

    if renpy.seen_image("ivankawhitehouse blurred") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("KimberlyGallery")

    if renpy.seen_image("kimberlywhitehouse"):
        imagebutton:
            focus_mask True
            idle "Gallery/kimberlygallery02.png" xpos 1050 ypos 100
            hover "Gallery/kimberlygallery02.png"
            action Jump ("KimberlyGallery02")

    if renpy.seen_image("kimberlywhitehouse") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("KimberlyGallery")

    if renpy.seen_image("kimfbi08"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery26.png" xpos 1478 ypos 100
            hover "Gallery/exploregallery26.png"
            action Jump ("kimberlygallery03")

    if renpy.seen_image("kimfbi08") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("KimberlyGallery")

    if renpy.seen_image("kimwhmegacum01"):
        imagebutton:
            focus_mask True
            idle "Gallery/whitehousegallery01.png" xpos 621 ypos 400
            hover "Gallery/whitehousegallery01.png"
            action Jump ("kimberlygallery04")

    if renpy.seen_image("kimwhmegacum01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("KimberlyGallery")

    add "Gallery/galleryfuture.png" xpos 1050 ypos 400

    add "Gallery/galleryfuture.png" xpos 1478 ypos 400

    add "Gallery/galleryfuture.png" xpos 620 ypos 700

    add "Gallery/galleryfuture.png" xpos 1048 ypos 700

    add "Gallery/galleryfuture.png" xpos 1478 ypos 700

    add "Gallery/gallerygrid02.png"
    add "Gallery/textkimberly.png"

label KimberlyGallery01:
scene ivankawhitehouse blurred
show ivanka20 at right
show whitehouseframe
iv "Hello TRAITOR! You clearly need to be brainwashed...err, I mean, to see the light."
iv "So I've brought along my stepsister who is a motivational speaker. Listen carefully to what she has to say."
window hide
show kimberly03 at left with moveinleft
kg "Thank you, General Ivanka. I am Kimberly Guilfool, daughter-in-law of OUR GREAT LEADER PRESIDENT-FOR-LIFE DONALD TRUMPF!"
mc "Why is this crazy woman screaming all of a sudden? She's hurting my ears."
window hide
hide kimberly03
show kimberly01 at left
with fastdissolve
kg "PRESIDENT-FOR-LIFE DONALD TRUMPF WILL RULE OVER NEW AMERICA FOR A THOUSAND YEARS!"
window hide
hide ivanka20
show ivanka21 at right
with fastdissolve
iv "Well, let's not get carried away here, I mean, he is going to die one d..."
window hide
hide kimberly01
show kimberly02 at left
with fastdissolve
kg "NO, PRESIDENT DONALD TRUMPF IS IMMORTAL AND WILL LIVE FOREVER AND ACCOMPLISH EVERYTHING, HE IS CHOSEN BY GOD HIMS..."
window hide
hide ivanka21
show ivanka24 at right                
iv "Come on! Even Daddy doesn't believe this crap! It's just for the rubes and the deplorables, we're dealing with a REAL threat from this hero over there! Stick to the script godammit!"
window hide
hide ivanka24
hide kimberly02
show ivanka22
with dissolve
kg "HOW DARE YOU? I WILL TELL OUR GREAT LEADER OF YOUR BLASPHEMOUS TREACHER..."
window hide
hide ivanka22
show ivanka23
with fastdissolve
iv "That's it, I'm cutting this podcast short, you're way off script Kimberly!"
kg "I AM NOT OFF-SCRIPT, THE SCRIPT OF OUR WHOLE LIVES IS WRITTEN BY OUR GLORIOUS LEADER PRESIDENT DONALD TRUMPF, AND THE BEST IS YET TO COME!!!!"
jump KimberlyGallery

label KimberlyGallery02:
scene kimberlywhitehouse
show whitehouseframe
show kimberly05 with moveinleft
kg "It's me, Kimberly, here at the Supreme White House gym. AND THIS TIME YOU WILL LISTEN TO ME!"
mc "*sigh* Here we go again, crazy person shouting at the screen."
window hide
scene kimberlywhitehouse blurred
show kimberly06
show whitehouseframe
with dissolve
kg "LOOK AT HOW BUFF I AM THANKS TO OUR GREAT LEADER WHO RIGHTFULLY STARTED A NUCLEAR WAR TO EMPOWER WOMEN SUCH AS MYSELF!"
mc "I don't think this is how it happened. The game intro suggests it was a clumsy accid..."
window hide
hide kimberly06
show kimberly07
with dissolve
kg "SHUT UP! PRESIDENT-FOR-LIFE DONALD TRUMPF HAS DONE MORE FOR WOMEN THAN ABRAHAM LINCOLN!"
mc "Err... Can she hear me? What the fuck?"
window hide
hide kimberly07
show kimberly08
with dissolve
play sound "Sounds/womangroan.mp3"
kg "I've been told you have big muscles. BUT ARE YOU AS STRONG AS ME? I DOUBT IT! I COULD CRUSH YOU WITH MY LITTLE FINGER!"
mc "Yeah okay, but I still have some training to do and I'll easily catch up to that level of strength. What is she, like strength 9 or something? Pfff..."
window hide
hide kimberly08
show kimberly09
with dissolve
play sound "Sounds/ripping.mp3"
kg "YOU'RE MAKING ME ANGRY! AND THIS IS WHAT HAPPENS WHEN YOU MAKE ME ANGRY!"
window hide
play sound "Sounds/ripping.mp3"
hide kimberly09
show kimberly10
with dissolve
kg "MY MUSCLES GROW EVEN BIGGER AND MY STRENGTH DOUBLES!"
mc "Fuck me, she's HU-U-UGE!"
window hide
hide kimberly10
show kimberly11
with dissolve
kg "THAT'S RIGHT, I'M MASSIVE! AND TOTALLY RIPPED EVERYWHERE! LOOK AT THOSE OVERMUSCLED GLUTES... AND WEEP!"
window hide
hide kimberly11
show kimberly12
with dissolve
kg "AND LOOK AT MY CLIT, IT'S AS BIG AS A MAN'S COCK! ADMIT IT, YOU CAN'T BEAT ME WIMP!" 
window hide
hide kimberly12
show kimberly13
with dissolve
kg "FUCK YEAH! GETTING SO BUFFED IS MAKING ME HORNY AS HELL! ARE YOU HORNY TOO? YOU'D BETTER ME, COS THIS MUSCLE SHE-HULK IS GOING TO CRUSH YOU!"        
jump KimberlyGallery

label kimberlygallery03:
stop music
scene fbi01
fo "Subject 42. SUBJECT 42! WAKE UP! Activate Google mental goggles, Siri."
scene fbi02 with dissolve
mc "Uh? My cock, is it still intact?"
play sound "Sounds/interfacestart.mp3"
scene fbibackground02
show dana07a
with dissolve
da "Your cock is doing just fine [name]. For the time being..."
mc "Phew, that's a relief. Now get me out of here, or I'll..."
hide dana07a
show dana20
with fastdissolve
da "NOT until you PASS the test."
hide dana20
show dana22
with fastdissolve
da "You know the drill, but this time, CONCENTRATE and FOCUS YOUR STRENGTH DOWN TO YOUR DICK!"
window hide
hide dana22 with moveoutright
show kimfbi01 with moveinleft
mc "Hey, please don't leave me alone with h..."
play sound "Sounds/hulkgrowl01.mp3"
kg "YOU ARE AN ENEMY OF THE PEOPLE, PREPARE TO DIE BY PUSSY SMOTHERING!"
mc "AAAAH, HELP!"
window hide
hide kimfbi01
show kimfbi04 
with fastdissolve
kg "I'm getting ANGRY!"
play sound "Sounds/ripping.mp3"
hide kimfbi04
show kimfbi05 
with dissolve
kg "AND ANGRIER!"
hide kimfbi05
show kimfbi07
with dissolve
kg "AND ANGRIEST!"
mc "* Oh shit, oh shit, concentrate [name], concentrate! The life of your prized horsecock depends on it! *"
scene fbibackground02 blurred
show kimfbi08
with dissolve
play sound "Sounds/hulkgrowl01.mp3"
kg "NOW FUCK ME!"
play channel1 "Sounds/debrasex.mp3"
hide kimfbi08
show kimfbianim
with fastdissolve
call screen kimfbianim03xx
screen kimfbianim03xx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KimberlyFBIEnd03xx")

label KimberlyFBIEnd03xx:
play channel2 "v08/humming.mp3"
scene fbi10 with dissolve
mc "AAAH! My cock! Must... FIGHT... the... PAIN!"
stop channel2
scene fbibackground02 blurred
show kimfbianim
with dissolve
call screen kimfbianim04xx
screen kimfbianim04xx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KimberlyFBIEnd04xx")

label KimberlyFBIEnd04xx:
play channel2 "v08/humming.mp3"
scene fbi11 with dissolve
mc "NEED... TO... CUM..."
da "FOCUS! BELIEVE your cock is STRONGER than her PUSSY!"
scene fbi12 with dissolve
mc "YES! AAAAH!"
window hide
with fastflash
da "Well done [name]! Keep going!"
scene fbi13 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "FUCK YEAH, MASSIVE CUMLOAD, RHAAA!"
scene fbibackground02 blurred
stop channel2
show kimfbi09
with dissolve
play channel2 "Sounds/splooge02.mp3"
kg "WHAT IS HAPPENING? MY PUSSY IS THE STRONGEST PUSSY IN THE WORLD!!!"
window hide
with fastflash
mc "My cock is STRONGER, RHAAA!"
stop channel2
stop channel1
play channel2 "v08/humming.mp3"
scene fbi14 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"    
mc "NOW I AM BECOME SEX, THE DESTROYER OF CUNTS!!!"
window hide
with fastflash
da "Amazing, you succeeded! Project Man-at-Twat accomplished!"
stop channel2
scene fbi15 with fade
play sound "Sounds/panting.mp3"
mc "Eeeh... Uuuuh..." 
da "Agent Fox, go and get the mop..."
jump KimberlyGallery

label kimberlygallery04:
stop music
stop sound
scene whitehouseentrance
mc "Finally, I'm inside the Supreme White House!"
window hide
show kimwh01 with moveinright
kg "And where do you think YOU'RE going?"
mc "Stand aside crazy woman, you are no match for..."
hide kimwh01
show kimwh02
with dissolve
kg "AAARGH, AN INTRUDER, THAT MAKES ME MAD AND ANGRY!"
mc "Err..."
hide kimwh02
show kimwh03
with dissolve
play sound "Sounds/ripping.mp3"
$ renpy.pause(0.5, hard='True')
kg "YOU'VE MADE ME EXTREMELY ANGRY!"
mc "Well, let's just calm down for a seco..."
hide kimwh03
show kimwh04
with dissolve
play sound "Sounds/hulkgrowl01.mp3"
kg "AND WHEN I GET ANGRY, MY MUSCLES GET REALLY MAD!"
mc "Uuh-oh..."
kg "NOW GET YOUR COCK OUT, I'M GOING TO FUCK YOU TO... DEATH!"
mc "Alright, alright, gee, can't even walked into the White House without getting sexually assaulted these days."
scene whitehouseentrance blurred
show kimwh05
with dissolve
kg "First, I'll make you spew your MOJO so you'll be an easier... PREY!"
mc "Oh, behave!"
stop music
play channel1 "Sounds/wank.mp3"
play channel2 "Sounds/boymoan.mp3"
scene whitehouseentrance blurred
show kimwankslow
call screen kimhandjobslowxb
screen kimhandjobslowxb:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("KimHandjobFastxb") 

label KimHandjobFastxb:
kg "And now, I'll go even FASTER, for the KILL!"
mc "I can take it, I'm a trained... wanker! Just like your boss."
kg "DO NOT MOCK OUR BELOVED CULT LEADER!"
hide kimwankslow
show kimwankfast
call screen kimhandjobfastxb
screen kimhandjobfastxb:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KimHandjobEndxb")

label KimHandjobEndxb:
kg "I can feel you getting there... LET YOUR MOJO SPILL OUT!"
stop channel1
stop channel2
hide kimwankfast
show kimwankcum01
with dissolve
play music "Sounds/moaning03.ogg"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "AAAH! I can't hold BA-AAA-CK!"
window hide
with fastflash
kg "That's it, MORE OF IT!"
hide kimwankcum01
show kimwankcum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "GODAAAMMMMMIIIT! RHAAAA!"
window hide
with fastflash
kg "YOU ARE DEFEATED, SUBMIT TO MY SUPERIOR HAND MUSCLES!"
stop music
play sound "Sounds/boymoan02.mp3"
hide kimwankcum02
show kimwankcum03
with fastdissolve
mc "NOT YET, AAAHH!"
window hide
with fastflash
kg "YOU MIGHT COME LIKE A CUM FOUNTAIN, BUT YOUR MOJO IS SLOWLY DRAINING OUT OF YOU!"
window hide
with fastflash
mc "My Mojo is UNLIMITED, RHAAA!"
stop music
play sound "Sounds/panting.mp3"
hide kimwankcum03
show kimwankcum04
with dissolve
kg "In that case, I have no choice but to SQUEEZE IT OUT WITH MY PUSSY MUSCLES!"
mc "Damn it woman, let me breathe for a min..."
kg "NO, SIT ON THE STAIRS AND PREPARE TO GET YOUR COCK SQUISHED TO OBLIVION!"
scene kimwhprefuck00 with dissolve
kg "You're still hard... BUT YOU WON'T BE FOR LONG!"
scene kimwhprefuck01 with dissolve
kg "ALL THAT FILTHY SPUNK DRIPPING DOWN YOUR SCHLONG... I'LL MAKE BETTER USE OF IT!"
scene kimwhprefuck02 with dissolve
kg "Right there, between my asscheeks. SQUEEZING YOUR SHAFT!"
mc "AAAH, your glutes are like STEEL!"
kg "THAT'S RIGHT, AND MY PUSSY IS LIKE TITANIUM!"
stop music
play channel1 "Sounds/debrasex.mp3"
play channel2 "Sounds/panting.mp3"
scene whitehouseentrance blurred
label KimFuckSlowxb:
show kimfuckslow
call screen kimfuckslowxb
screen kimfuckslowxb:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("KimFuckFastxb") 

label KimFuckFastxb:
kg "I'VE BEEN TOO KIND SO FAR, NOW YOU WILL FEEL MY PUSSY MUSCLES CLAMPING DOWN... HARD!!!!"
mc "Do... your... worst... I can take it... AAAH."
kg "WE'LL SEE ABOUT THAT!"
hide kimfuckslow
show kimfuckfast
call screen kimfuckfastxb
screen kimfuckfastxb:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KimFuckEndxb")

label KimFuckEndxb:
scene kimwhfuckcum01 with dissolve
kg "Can you feel your cock being slowly SQUEEZED like a VICE?"
scene kimwhfuckcum02 with dissolve
mc "AAAH, it hurts but I can take it!"
scene kimwhfuckcum03 with dissolve
kg "Can you now, Are you SURE?"
scene kimwhfuckcum04 with dissolve
mc "Yes, I AM SURE! And I'll PROVE IT TO YOU RIGHT NOW BY CUMMING UNTIL YOUR PUSSY IS OVERFILLED WITH MY SUPERIOR SPUNK!"
stop channel1
stop channel2
play channel2 "Sounds/splooge02.mp3"
play channel1 "Sounds/boycum.mp3"
scene kimwhfuckcum05 with dissolve
mc "There you go, RHAAA!"
window hide
with fastflash
kg "MY PUSSY WILL SWALLOW YOUR MEAGER OFFERING!!!"
window hide
with fastflash
scene kimwhfuckcumpreggo:
    ypos -1.0
    linear 4.0 ypos -0.0
pause 5.0
kg "WHAT??? MY BELLY IS... EXPLODING... YOU'RE CUMMING TOO MUCH, I CAN't HOLD ONTO YOUR DISGORGING SHAFT, AAAH!"
stop channel2
stop channel1
play music "Sounds/cumming.mp3"
scene kimwhmegacum01 with dissolve
mc "RHAAAA! MEGACUM!!!!"
play sound "Sounds/waterspray.mp3"
window hide
with fastflash
kg "AAAH, WHAT IS HAPPENING???"
window hide
with fastflash
mc "I AM THE ULTIMATE PUSSY-WRECKER!!!"
stop music
scene kimwhmegacum02 with fade
mc "The stairs look a bit too slippery. If you'll excuse me, I think I'll take the lift..."
kg "Gggg... Aaaaah..."
jump KimberlyGallery
