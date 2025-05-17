label IvankaGallery:
call screen galleryivanka
screen galleryivanka:
    add "Gallery/ivankagallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("galleryivanka"), Jump ("MainGallery")]

    imagebutton:
        focus_mask True
        idle "Gallery/gallerynextpage.png"
        hover "Gallery/gallerynextpage.png"
        action [Hide ("galleryivanka"), Jump ("IvankaGalleryb")]

    if renpy.seen_image("ivanka01"):
        imagebutton:
            focus_mask True
            idle "Gallery/ivankagallery01.png" xpos 621 ypos 100
            hover "Gallery/ivankagallery01.png"
            action Jump ("IvankaGallery01")

    if renpy.seen_image("ivanka01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action None

    if renpy.seen_image("ivanka04"):
        imagebutton:
            focus_mask True
            idle "Gallery/ivankagallery02.png" xpos 1050 ypos 100
            hover "Gallery/ivankagallery02.png"
            action Jump ("IvankaGallery02")

    if renpy.seen_image("ivanka04") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action None

    if renpy.seen_image("ivanka08"):
        imagebutton:
            focus_mask True
            idle "Gallery/ivankagallery03.png" xpos 1478 ypos 100
            hover "Gallery/ivankagallery03.png"
            action Jump ("IvankaGallery03")

    if renpy.seen_image("ivanka08") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action None

    if renpy.seen_image("ivankamelania01"):
        imagebutton:
            focus_mask True
            idle "Gallery/ivankagallery04.png" xpos 621 ypos 400
            hover "Gallery/ivankagallery04.png"
            action Jump ("IvankaGallery04")

    if renpy.seen_image("ivankamelania01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action None

    if renpy.seen_image("melaniaivanka01"):
        imagebutton:
            focus_mask True
            idle "Gallery/melaniagallery04.png" xpos 1050 ypos 400
            hover "Gallery/melaniagallery04.png"
            action Jump ("IvankaGallery05")

    if renpy.seen_image("melaniaivanka01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 400
            hover "Gallery/gallerylocked.png"
            action None

    if renpy.seen_image("ivankabj01"):
        imagebutton:
            focus_mask True
            idle "Gallery/ivankagallery06.png" xpos 1478 ypos 400
            hover "Gallery/ivankagallery06.png"
            action Jump ("IvankaGallery06")

    if renpy.seen_image("ivankabj01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 400
            hover "Gallery/gallerylocked.png"
            action None

    if renpy.seen_image("ivankaanalcum01"):
        imagebutton:
            focus_mask True
            idle "Gallery/ivankagallery07.png" xpos 621 ypos 700
            hover "Gallery/ivankagallery07.png"
            action Jump ("IvankaGallery07")

    if renpy.seen_image("ivankaanalcum01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 700
            hover "Gallery/gallerylocked.png"
            action None

    if renpy.seen_image("idesk04"):
        imagebutton:
            focus_mask True
            idle "Gallery/ivankagallery08.png" xpos 1050 ypos 700
            hover "Gallery/ivankagallery08.png"
            action Jump ("IvankaGallery08")

    if renpy.seen_image("idesk04") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 700
            hover "Gallery/gallerylocked.png"
            action None
            
    if renpy.seen_image("ivankabdsm01"):
        imagebutton:
            focus_mask True
            idle "Gallery/ivankagallery09.png" xpos 1478 ypos 700
            hover "Gallery/ivankagallery09.png"
            action Jump ("IvankaGallery09")

    if renpy.seen_image("ivankabdsm01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 700
            hover "Gallery/gallerylocked.png"
            action None

    add "Gallery/gallerygrid02.png"
    add "Gallery/textivanka.png"

label IvankaGalleryb:
call screen galleryivankab
screen galleryivankab:
    add "Gallery/ivankagallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("galleryivankab"), Jump ("MainGallery")]

    imagebutton:
        focus_mask True
        idle "Gallery/gallerynextpage.png"
        hover "Gallery/gallerynextpage.png"
        action [Hide ("galleryivankab"), Jump ("IvankaGallery")]

    if renpy.seen_image("ivankawhitehouse blurred"):
        imagebutton:
            focus_mask True
            idle "Gallery/ivankagallery10.png" xpos 621 ypos 100
            hover "Gallery/ivankagallery10.png"
            action Jump ("IvankaGallery10")

    if renpy.seen_image("ivankawhitehouse blurred") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("IvankaGalleryb")

    if renpy.seen_image("whbothend01"):
        imagebutton:
            focus_mask True
            idle "Gallery/whitehousegallery02.png" xpos 1050 ypos 100
            hover "Gallery/whitehousegallery02.png"
            action Jump ("IvankaGallery11")

    if renpy.seen_image("whbothend01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("IvankaGalleryb")
    if renpy.seen_image("newovaloffice01"):
        imagebutton:
            focus_mask True
            idle "Gallery/whitehousegallery03.png" xpos 1478 ypos 100
            hover "Gallery/whitehousegallery03.png"
            action Jump ("IvankaGallery12")

    if renpy.seen_image("newovaloffice01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("IvankaGalleryb")

    add "Gallery/galleryfuture.png" xpos 621 ypos 400

    add "Gallery/galleryfuture.png" xpos 1050 ypos 400

    add "Gallery/galleryfuture.png" xpos 1478 ypos 400

    add "Gallery/galleryfuture.png" xpos 620 ypos 700

    add "Gallery/galleryfuture.png" xpos 1048 ypos 700

    add "Gallery/galleryfuture.png" xpos 1478 ypos 700

    add "Gallery/gallerygrid02.png"
    add "Gallery/textivanka02.png"

label IvankaGallery01:
scene ivanka01
show whitehouseframe
iv "Well, hello there [name]. This is Ivanka, the First Daughter and the most successful self-made woman in the land."
iv "I heard you had a grudge against my daddy. I'm here to warn you. I will defend my family and as you can see..."
scene ivanka02 with dissolve
show whitehouseframe
iv "I have the muscles and the feminine beauty to do so..."
iv "Jared is, shall I say, a beta-weakling. Not because of any beta radiations, he's just always been one really."
iv "And I am an ALPHA-FEMALE! So what do you say we pair up so I can finally become President Ivanka Trumpf and you can be my Vice-President?"
scene ivanka03 with dissolve
show whitehouseframe
iv "You would have access to this hot muscled body... In the Oval Office under my desk."
iv "Think about it. A business opportunity such as this one doesn't come often..."
jump IvankaGallery

label IvankaGallery02:
scene ivanka04
show whitehouseframe
iv "So, apparently, you didn't quite get the message. How hard is it to understand you cannot fight the Trumpf syndica... I mean family?"
iv "Now watch carefully. What you are up against..."
scene ivanka05 with dissolve
show whitehouseframe
iv "See? I can power-lift even more than that, this is a piece of cake for me. I am the MOST POWERFUL WOMAN in the World!" 
iv "That's why I'm always invited to meet all the other powerful people in the world by Daddy."
iv "So don't fight him, or you'll be up against ME, the essence of feminine beauty and strength..."
scene ivanka06 with dissolve 
show whitehouseframe
iv "The best in this day and age is to be COMPLICIT. Just like I am. And to make tons of money out of the situation."
iv "I could promote your products via Twatter and you would promote mine via Fuckbook. Like my new flagrance \"In-Peach-Mint\". So come and join the Trumpf syndica... I meant family!"
iv "DO IT NOW. Before this special offer terminates. After that, I'll have no other choice but to TERMINATE YOU!"    
jump IvankaGallery

label IvankaGallery03:
scene ivanka08
show whitehouseframe
iv "Hello again [name]... As you can see, I am ready to go one step further with YOU!"
iv "I'm not wearing a bra, because I have nothing to hide. Just like my daddy, who has the most transparent administration in history!"
scene ivanka09 with dissolve
show whitehouseframe
iv "Oh, and look here, what do I have? A BIG THICK WHITE dildo... Not as HUGE as your cock from what I've heard..."
iv "But it will serve its purpose, I will use it to demonstrate the POWER of my alpha-female tits!"
scene ivanka10 with dissolve
show whitehouseframe
iv "See how it fits perfectly between my MASSIVE firm knockers?"
iv "My muscular breasts can squeeze it so hard, it might even BREAK!"
scene ivanka11 with dissolve
show whitehouseframe
iv "But don't worry, I won't DESTROY your cock with my superior breasts..."
iv "... If you're a good boy and you stop your phony WITCH-HUNT against my daddy!"
iv "Then, I'll lick it all over and make it EXPLODE its thick creamy boy-juice all over my First Daughter face!"
jump IvankaGallery

label IvankaGallery04:
scene melaniaivanka01
show whitehouseframe
me "Mmh, I'm feeling so HORNY today... But our President-for-Life is too busy making New America GREAT AGAIN."
me "Fortunately, his daughter isn't so busy, since she's just a senior adviser with no clear duties... Maybe I should call her, what do you think [name]?"
scene melaniaivanka02 with dissolve
show whitehouseframe
iv "Here I am! Ready for some SPECIAL FAMILY TIME!"
me "I bet you already have your HUGE cock out and ready to fap [name], right? My pussy is sssoo wet too..."
iv "We're not letting you into our private sex life for no reason [name]..."
me "We need you to PROMISE us that you'll be a good boy and abandon your vendetta against my hubby."
iv "And we'll show you what you can get in return..."
scene melaniaivanka03 with dissolve
show whitehouseframe
play sound "Sounds/kiss.mp3"
iv "I LOVE your tongue on mine Melania... Mmmmh..."
me "My daughter-in-law is such a NAUGHTY girl! For YOU!"
scene melaniaivanka04 with dissolve
show whitehouseframe
iv "And I love even more GRINDING my pussy against yours!"
me "Ooh, I'm sure [name] LOVES watching us being BEST!"
iv "I want you to PUMP MY PUSSY UP! It needs to be GIGANTIC to fit his ENORMOUS BOYCOCK!"
me "Ooh, that's a good idea Ivanka! And I have just the tool for that..."
scene melaniaivanka05 with dissolve
show whitehouseframe
play sound "Sounds/moaning.mp3"
me "See that [name]? Her pussy is SWELLING UP, ready to take on your GIANT PUSSY-PLEASER!"
iv "Oh yes, my clit is so fucking HUGE now, keep PUMPING IT Melania!"    
scene melaniaivanka06 with dissolve
show whitehouseframe
me "I just have to taste this MEGA-PUSSY now..."
iv "Yeah, rub your tongue all over my swollen pussy lips... And slurp up all my copious sex juices, God, I'm just so fucking HORNY!"
me "*lick* Mmmh, sssooo tasty, I wish you were here to savour my daughter-in-law's DELICIOUS cunt with me [name]!"
iv "Now it's my turn to return the favor Melania..."
scene melaniaivanka07 with dissolve
show whitehouseframe
me "Oh my God, I'm squirting, your tongue is so good Ivanka!"
iv "I hope you're CUMMING a MONSTERLOAD too, [name]!"
me "I imagine that his BEAST must be EXPLODING!"
scene melaniaivanka08 with dissolve
show whitehouseframe
me "I hope you enjoyed our little display of family bonding..."
if mctrumpster <= 4:
    iv "You could be part of it too, you know that, right? All you have to do is join the Trumpf syndic... I meant FAMILY!"
if mctrumpster == 5 and bounty == False:
    iv "And since you're already a Trumpster, we'll make sure to treat you like FAMILY when you come and bang us with your SUPERIOR FUCKSTICK!"
    me "We'll be waiting... Our pussies all swollen and READY to take you on, STUD!"
hide whitehouseframe
jump IvankaGallery

label IvankaGallery05:
scene ivankamelania01
show whitehouseframe
iv "Oh, hello [name]. You've caught us in an intimate position. My SLAVE is busy licking my pussy."
scene ivankamelania02 with dissolve
show whitehouseframe
iv "That's right, I can DOMINATE any woman I want, even the First Lady, and make them worship my SUPERIOR body!"
me "Yes, Ivanka, you are ssoo POWERFUL! So much more powerful than [name]..."
iv "What do you have to say about that? Melania seems to think you're nothing but a WIMP after all! Cos you STILL haven't FUCKED HER!"
scene ivankamelania03 with dissolve
show whitehouseframe
iv "And now it's time to give my mother-in-law what she's craving for. A BIG THICK DILDO!"
me "Ooh, Ivanka, give me what [name] REFUSES to give me! I want it DEEP in my creamy FIRST CUNT!"
scene ivankamelania04 with dissolve
show whitehouseframe
iv "There you go Melania, take it hard! See how I'm pounding her into oblivion [name]! Would you like to be in MY PLACE?"
play sound "Sounds/moaning.mp3"
me "I'm sure he would, but he still hasn't UNDERSTOOD what it means to be a part of the FAMILY... AAAh, I'm cumming AGAIN!"
scene ivankamelania05 with dissolve
show whitehouseframe
iv "So be reasonable and stop being DEPLORABLE! Or you might end up on the WRONG end of THIS stick!"
if bounty:
    iv "And maybe when a bounty hunter brings you back to me, I will treat you the same way. So be warned!"    
hide whitehouseframe
jump IvankaGallery

label IvankaGallery06:
scene bossroom02 blurred
show ivankabj01
iv "Damn, seeing is believing, I was told you were HUNG, but you are indeed A HORSE-HUNG HERO!"
mc "Yep, that's me!"
iv "That thing.... Still soft and already sssooo big. Like AT LEAST three times the length and width of Jared's pindick. YUM!"
mc "Well, get me hard and it'll become FIVE TIMES his size!"
iv "I can't wait to see this monster in all its ROCK-HARD GLORY. Please take it out and show me [name]!"
scene bossroom03 blurred
show ivankabj02
with dissolve
play music "Sounds/kiss.mp3"
iv "*kisses* What a GLORIOUS, TRUE AMERICAN FUCKPOLE!"
stop music
mc "Enough kissing and talking, open your mouth for my great big throat-gagging boymeat, General Ivanka!"
hide ivankabj02
show ivankabj03
with dissolve
mc "That's it... Now relax your throat muscles, and try and take a few more inches into your hungry size-queen mouth!"
hide ivankabj03
show ivankabj04
with dissolve
play music "Sounds/hardsucking.mp3"
mc "Oooh, your mouth is so good!"
hide ivankabj04
show ivankabj03
with fastdissolve
pause 0.2
hide ivankabj03
show ivankabj04
with fastdissolve
pause 0.2
hide ivankabj04
show ivankabj03
with fastdissolve
pause 0.2
hide ivankabj03
show ivankabj04
with fastdissolve
pause 0.2
hide ivankabj04
show ivankabj03
with fastdissolve
pause 0.2
hide ivankabj03
show ivankabj04
with fastdissolve
pause 0.2
hide ivankabj04
show ivankabj03
with fastdissolve
pause 0.2
hide ivankabj03
show ivankabj04
with fastdissolve
pause 0.2
hide ivankabj04
show ivankabj03
with fastdissolve
pause 0.2
hide ivankabj03
show ivankabj04
with fastdissolve
pause 0.2
hide ivankabj04
show ivankabj03
with fastdissolve
pause 0.2
hide ivankabj03
show ivankabj04
with fastdissolve
pause 0.2
stop music
mc "I love your sucking skills, but let's get to the REAL fun! Why don't you show me that alpha-radiated hot bod of yours Ivanka?"
hide ivankabj04
show ivankabj02
with fastdissolve
play sound "Sounds/kiss.mp3"
iv "*kisses* Of course, but just let me kiss that magnificent fuckpole one last time before I get undressed for YOU."
scene bossroom01 blurred
show ivankapose01
with dissolve
iv "That's what you wanted to see in the flesh [name]? My MUSCLED ALPHA-FEMALE BODY?"
mc "Ooh yeah!"
hide ivankapose01
show ivankapose02
with fastdissolve
iv "I am the most POWERFUL woman in the world! My biceps are made of PURE STEEL!"
mc "Alpha-radiation is the bomb! Literally."
hide ivankapose02
show ivankapose03
with fastdissolve
iv "Watch me flex my mighty biceps... See how they BALLOON with ABSOLUTE POWER?"
mc "I see, I see... And I can't wait to FEEL them too!"
hide ivankapose03
show ivankapose04
with fastdissolve
iv "And my bumcheeks are so CHORDED that they could CRUSH A HUMAN SKULL!"
mc "Thanks for the tip, I'll make sure not to get my face anywhere near it."
iv "Now come and WORSHIP me \"[name] the Grabber\"!"
hide ivankapose04
show ivankamc01
with dissolve
window hide
play sound "Sounds/womanmoan.mp3"
$ renpy.pause(1.0, hard=True)
iv "Ooh, I LOVE how you play with my big breasts!"
mc "I'm good at grabbing stuff, that's why they call me \"[name] the Grabber\"!"
iv "My family has always been good at grabbing stuff too."
hide ivankamc01
show ivankamc02
with fastdissolve
iv "Now kiss my POWERFUL biceps!"
play sound "Sounds/kiss.mp3"
iv "You like that, don't you? You like my HUGE muscles!"
mc "Mmh, yes, I love'em Ivanka... But it's time for YOU to WORSHIP MY BODY!"
iv "Of course, [name], it is worthy of MUSCLE WORSHIPPING!"
hide ivankamc02
show ivankamc03
with dissolve
iv "Those hard SLABS of pec muscles... are making me ssoo horny..."
hide ivankamc03
show ivankamc04
with fastdissolve
iv "...And that... COCK! So fucking MASSIVE! Mmh!"
window hide
play sound "Sounds/womanmoan.mp3"
$ renpy.pause(1.0, hard=True)
iv "Now come and OWN my ass, the hole that Jared never found!"
jump IvankaGallery

label IvankaGallery07:
scene ivankanalscene
show ivankapreanal01
iv "I want it DEEP inside my ass, you hear me, \"[name] the Grabber\"?"
mc "Of course, my general. Sir, YES SIR!"
play music "Sounds/fucksound.mp3"
hide ivankapreanal01
label IvankaAnalSlowx:
hide ivankaanalfast
show ivankaanalslow
with fastdissolve
call screen ivankaanalslow01x
screen ivankaanalslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("IvankaAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("IvankaAnalFastx") 

label IvankaAnalFastx:
iv "I'm going to IMPALE myself on your GIANT shaft even FASTER!"
hide ivankaanalslow
show ivankaanalfast
call screen ivankaanalfast01x
screen ivankaanalfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("IvankaAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("IvankaAnalSlowx") 

label IvankaAnalEndx:
iv "Oh God, I'm cumming! From a GIANT BOYCOCK IN MY ARSE!"
mc "And I'm about to come too!"
hide ivankaanalslow
hide ivankaanalfast
show ivankaanalcum01
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "AAAH! Hosing your back side at FULL BLAST!"
stop music
iv "YES! FLOOD it with your seed, \"[name] the Grabber\"! And then douse my body in your hot sauce!" 
scene ivankanalscene blurred
show ivankaanalcum02
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "RHAAA! There you go, general Ivanka!"
iv "Sssoo much young virile seed! You're all they said you were and MORE, [name]!"
scene ivankanalscene
show ivankaanalcum03
with dissolve
mc "That's it, I've emptied my nuts IN and ON you Ivanka!"
iv "Mmh, and it was wonderful, STUD!"
iv "But I have a lot of work to do. We're planning an attack on that rebellious compound of unpatriotic deep state never-trumpfers."
mc "Ah, I see... (I should report this back to Chief Lena.) Right, I'll be on my way then, general."
iv "Do come back and see me anytime! *wink*"
jump IvankaGallery

label IvankaGallery08:
scene ivankadeskscene blurred
show ivankapredesk01
iv "I still can't get over how BIG your cock is [name]... So veiny and menacing..."
mc "Look at my beast closely, Ivanka. It's about to fuck you fast and ROUGH!"
iv "Just like I like it! Fuck me as HARD as you want!"
play music "Sounds/fucksound.mp3"
scene ivankadeskscene
label IvankaDeskSlowx:
hide ivankadeskfast
show ivankadeskslow
with fastdissolve
call screen ivankadeskslow01x
screen ivankadeskslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("IvankaDeskEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("IvankaDeskFastx") 

label IvankaDeskFastx:
iv "Oh, God, you're fucking me so good, my tits are bouncing all over the place! Fuck me even HARDER please!"
hide ivankadeskslow
show ivankadeskfast
call screen ivankadeskfast01x
screen ivankadeskfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("IvankaDeskEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("IvankaDeskSlowx") 

label IvankaDeskEndx:
mc "I'm gonna flood your pussy anytime now, General Ivanka!"
iv "Yes, DROWN my fertile ovaries in your virile sperm, they belong to YOU now!"
hide ivankadeskslow
hide ivankadeskfast
show idesk04
show ivankadeskcum01
with fastdissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "FUCK YEAH, Cumming! RHAAA!"
iv "YES! Do your PATRIOTIC duty and IMPREGNATE ME! AAAH!" 
hide idesk04
hide ivankadeskcum01
show ivankadeskcum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "All the way up your womb! AAAH!"
iv "You're so ROUGH! Ah, it's hitting the back of my womb! I think I'm gonna faint! OOOH!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
hide ivankadeskcum02
show ivankadeskcum03
with fastdissolve
mc "Still cumming all over you! RHAA!"
mc "Oh, it looks like she really DID faint. My plan of fucking her HARD and ROUGH worked, now is the time to steal the attack plans and bring them back to the compound."
stop sound
jump IvankaGallery

label IvankaGallery09:
scene bossroom01 blurred
show ivankabdsm01
iv "Look who's waking up? The TRAITOR who foiled my attack plans!"
mc "Hey, untie me, Ivanka!"
iv "I don't think so. I think you need a good WHIPPING!"
hide ivankabdsm01
show ivankabdsm02
with fastdissolve
iv "With my trusted braided whip!"
play sound "Sounds/whip.wav"
hide ivankabdsm02
show ivankabdsm03
with fastdissolve
mc "Stop it please, it hurts!"
iv "Mmh, it seems useless, because you're already injured and I can't KILL you like I'd love to, since the dev is a SNOWFLAKE!"
hide ivankabdsm03
show ivankabdsm04
with fastdissolve
iv "But maybe this dog leash will change your TRAITOROUS mindset. I borrowed it from the Supreme White House... Now put on the dog collar that daddy makes Mike Ponce wear around the Oval Office!"
scene bossroom02
show ivankabdsm05
with fastdissolve
mc "A BAD doggy. GRRRLLL!"
iv "I KNEW you were a BAD DOGGY! Pull your jockstrap down and bend over that chair with your fat balls hanging between your legs..."
scene bossroom04 blurred
show ivankabdsm06
with fastdissolve
iv "Now prepare to be FLOGGED until you get RED BALLS, bad doggy!"
scene bossroom05
show ivankabdsm07a
with fastdissolve
iv "I'm going to enjoy doing THIS!"
hide ivankabdsm07a
show ivankabdsm07b
with fastdissolve
play sound "Sounds/slap.mp3"
mc "AAAH! My balls!"
hide ivankabdsm07b
show ivankabdsm07a
with fastdissolve
iv "They'll be USELESS once I'm done with them!"
hide ivankabdsm07a
show ivankabdsm07b
with fastdissolve
play sound "Sounds/slap.mp3"
mc "Stop it, I beg you!"
hide ivankabdsm07b
show ivankabdsm07a
with fastdissolve
iv "A bad doggy needs a SEVERE punishment!"
hide ivankabdsm07a
show ivankabdsm07b
with fastdissolve
play sound "Sounds/slap.mp3"
iv "Mmh, now they're all BLOATED and ready for MILKING TIME!"
mc "Wh...what?"
scene bossroom06 blurred
show ivankabdsm08
with dissolve
iv "Just let yourself go, you're nothing but my MILK SLAVE now! Don't resist!"
mc "Oooh, my balls ache so much, I need to empty them!"
iv "That's exactly right! They are sssooo MASSIVE. I'm gonna pump a REALLY HUGE load out of them!"
hide ivankabdsm08
show ivankabdsm09
with dissolve
play sound "Sounds/lick.mp3"
iv "Mmh, I love the musky scent of FAT BALLS ready to UNLOAD!"
scene bossroom04
show ivankabdsm10
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
iv "Let it all go, I want you to FILL UP that jar, you hear me?"
mc "Oh my God, I'm being milked like a cow!"
scene bossroom04 blurred:
    zoom 1.5
    xalign .5 yalign .5
show ivankabdsm11 at centerright
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
iv "Good boy, you've filled it up and you're STILL spewing some more thick shots of young virile semen."
mc "I can't.... Keep going... Empty..."
scene bossroom07 blurred:
    zoom 2.0
    xalign .5 yalign .8
show ivankabdsm12
with dissolve
play sound "Sounds/sucking.mp3"
iv "I'll suck the afterdregs out of your cumslit.... *suck*"
iv "So, will you now be a good doggy?"
mc "Yes! Warf, warf!"
iv "That's good. But you need to PROVE it to me. So get on your back and lap at my butthole like a GOOD DOGGY then!"
scene bossroom02 blurred
show ivankabdsm20
with fastdissolve
iv "Yeah, stick your tongue right up there, I want it SQUEAKY CLEAN, you hear me?"
play sound "Sounds/sucking.mp3"
iv "Good doggy, you're a natural. I'll allow you to pull your hard monster out and WANK IT FOR ME now..."
hide ivankabdsm20
show ivankabdsm21
with fastdissolve
iv "...While you lick the other side. Mmmh, my little anus is all tingly now... And wet from your saliva."
scene bossroom07
show ivankabdsm22
with dissolve
iv "Oh yeah, you're a nasty little doggy aren't you? Sniffing and slurping up my ass juices... Filthy, FILTHY DOGGY! You deserve a reward.... My FRONT PRIZE."
scene bossroom07
show ivankabdsm23
with dissolve
iv "Let me give you access to my juicy cunt..."
scene bossroom08 blurred
show ivankabdsm24
with dissolve
iv "There you go, twirl that dirty doggy tongue around my engorged pussylips. And wank that cock for me. But NO CUMMING, you hear me doggy?"
mc "But I want to cum so bad, Ivanka!"
iv "Don't call me that! I'm your MISTRESS and you're my LAPDOG, got it?"
mc "But..."
scene bossroom07 blurred
show ivankabdsm25
with dissolve
iv "It seems you don't quite understand what it means to be a REALLY GOOD DOGGY. I'll teach you a new trick then. See that rock-hard MONSTER COCK that's dripping filthy pre-cum?"
hide ivankabdsm25
show ivankabdsm26
with fastdissolve
play sound "Sounds/slap.mp3"
iv "Bad, BAD COCK! No cumming for you, BAD DOGGY!"
mc "Hey, I said I was a \"good doggy\"!"
hide ivankabdsm26
show ivankabdsm27
with fastdissolve
iv "YOU don't get to decide, I GET TO DECIDE, I'm your MISTRESS, remember?"
iv "And I've decided that you are a..."
hide ivankabdsm27
show ivankabdsm28
with fastdissolve
play sound "Sounds/slap.mp3"
iv "...BAD DOGGY!"
mc "Please tell me what can I do to be treated like a good doggy MISTRESS! I'll do anything to be allowed to cum!"
hide ivankabdsm28
show ivankabdsm27
with fastdissolve
iv "Well, for starters, you should embrace the dar... I mean the Trumpf side!"
mc "But I'm already a Trumpster, Ivanka!!!"
iv "Are you? Oh, I didn't realize. Then, you can come, GOOD DOGGY!"
hide ivankabdsm27
show ivankabdsm29
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
iv "Empty your cum-laden balls, doggy boy!"
mc "AAAH!"
hide ivankabdsm29
show ivankabdsm30
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
iv "Yeah, shoot some MORE! Your mistress DEMANDS a MASSIVE LOAD OF CUM!"
mc "AAAH!"
scene bossroom04:
    zoom 1.5
    xalign 1.0 yalign 1.0
show ivankabdsm31
with fastdissolve
iv "Mmmh, you did well, you ARE a good doggy after all... And you gave me all that sweet cum... Just for your mistress... Yummy!"
jump IvankaGallery

label IvankaGallery10:
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
jump IvankaGalleryb

label IvankaGallery11:
$ ivankaloadx = False
$ melaniadeepx = False
$ ivankadeepx = False
$  melanialoadx = False

scene ovaloffice02
show mcprewhfuck01
mc "See this? That's a schlong worthy of a REAL President!"
play sound "v08/wow.mp3"
me "Indeed... But how much Special Pizza Sauce can it deliver?"
iv "And how DEEP can it get into our pussies?"
hide mcprewhfuck01
show mcprewhfuck02
with dissolve
play sound "Sounds/lick.mp3"
mc "I'll show you soon enough. But first, I want a taste of those succulent nipples..."
scene ovaloffice02zoom blurred
show mcprewhfuck03
with dissolve
play sound "Sounds/slurp.mp3"
mc "Let me get a taste of your mommy-milk..."
iv "Oooh, but... That's normally reserved for my children..."
mc "Not anymore... I take what's MINE!"
iv "You're so forceful and... MANLY. Kiss me please..."
hide mcprewhfuck03
show mcprewhfuck04
with dissolve
play sound "Sounds/kiss.mp3"
me "Now that you're here, UNINVITED, with your massive cock all ROCKHARD and READY, why don't you show us some good times, [name]?"
mc "Of course First Lady... Get on all fours on the Oval Office carpet and I'll show you some GREAT times!"
scene whpredoggybackground
show whpredoggyanimslow
with dissolve
play music "Sounds/moaning02.mp3"
mc "Now that's better ladies. So, who will go first I wonder?"
menu:
    "Melania":
        mc "First Lady first..."
        jump MelaniaHouseFuckxc
    "Ivanka":
        mc "Muscles galore for my BIG MUSCLE first!"
        jump IvankaHouseFuckxc

label MelaniaHouseFuckxc:
stop music
scene whivankacumbackgroundzoom
show whmelaniaprefuck
with dissolve
mc "Ready First Lady?"
play sound "Sounds/moaning.mp3"
me "Mmmh, YES I AM!"
label MelaniaHouseFuckbxc:
stop music
play music "Sounds/womansex01.mp3"
scene whdoggymelaniabackground blurred
label MelaniaHouseSlowxc:
hide melaniawhdoggyfast
show melaniawhdoggyslow
call screen melaniawhfuckslow01xc
screen melaniawhfuckslow01xc:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("MelaniaHouseEndxc")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MelaniaHouseFastxc") 
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("IvankaHouseSwitchxc") 

label MelaniaHouseFastxc:
if melaniadeepx:
    mc "I'm the FIRST man that DEEP inside the First Lady! Fuck Yeah!"
if melaniadeepx == False:
    mc "You love that cock, don't you Melania?"
    me "YES, I LOVE IT, I admit it, just shut up and FUCK MY DIRTY HOLE HARDER!"
    $ melaniadeepx = True
hide melaniawhdoggyslow
show melaniawhdoggyfast
call screen melaniawhfuckfast01xc
screen melaniawhfuckfast01xc:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("MelaniaHouseEndxc")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MelaniaHouseSlowxc")
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("IvankaHouseSwitchxc") 
        
label MelaniaHouseEndxc:
me "DUMP your load inside my First Lady pussy [name]!"
stop music
play music "Sounds/splooge02.mp3"
scene whdoggymelaniabackground blurred
show whmelaniacum01
with dissolve
mc "You don't need to ask me twice, AAAAH"
window hide
with fastflash
me "Oh God, he's really FIRING his shots up my super-elite fuckhole!"
hide whmelaniacum01
show whmelaniacum02
with dissolve
play sound "Sounds/womanscream.ogg"
me "AAAH, sssoo sssoo DEEP, directly into my womb!"
window hide
with fastflash
mc "Damn right, RHAAAA!"
window hide
with fastflash
me "Pull out and DOUSE my back with your warm spunk!"
stop music
scene whmelaniacumbackground
show whmelaniacum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "There you go, massive ball-busting nutload coming your way, RHAAA!"
$ melanialoadx = True
window hide
with fastflash
iv "Oh fuck, I want some of that too... It looks so yummy..."
hide whmelaniacum03
show whmelaniacum04
with dissolve
play sound "Sounds/panting.mp3"
if ivankaloadx:
    mc "Then come and slurp it up Ivanka..."
    jump WhbothfuckEndxc
if ivankaloadx == False:
    mc "Don't you worry, I've got enough cum left for YOUR PUSSY!"
    iv "Please, fuck me, I'm dying to feel that GIANT shaft STRETCHING my hole..."
    jump IvankaHouseFuckxc

label IvankaHouseSwitchxc:
mc "Gonna switch before I cum inside that tight hole, aaah... Get ready Ivanka!"
jump IvankaHouseFuckbxc

label IvankaHouseFuckxc:
stop music
scene whivankacumbackgroundzoom
show whivankaprefuck
with dissolve
mc "Ready Ivanka?"
play sound "Sounds/moaning.mp3"
iv "Always ready for a big fat teenage MONSTERCOCK!"
label IvankaHouseFuckbxc:
stop music
play music "Sounds/womansex02.mp3"
label IvankaHouseSlowxc:
scene whdoggyivankabackground blurred
show ivankawhfuckslow
call screen ivankawhfuckslow01xc
screen ivankawhfuckslow01xc:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("IvankaHouseEndxc")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("IvankaHouseFastxc") 
    imagebutton:
        focus_mask True
        idle "v071/topview.png"
        hover "v071/topview.png"
        action Jump ("IvankaHouseTopSlowxc") 
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("MelaniaHouseSwitchxc") 
 
label IvankaHouseFastxc:
if ivankadeepx:
    mc "Gonna POUND that presidential-family fuckhole HARDER and FASTER!"
if ivankadeepx == False:
    mc "Am I DEEP enough inside your pussy Ivanka?"
    iv "Oooh, YES! But go faster please, fuck me HARD, make me CUM!"
    $ ivankadeepx = True
scene whdoggyivankabackground
show ivankawhfuckfast
call screen ivankawhfuckfast01xc
screen ivankawhfuckfast01xc:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("IvankaHouseEndxc")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("IvankaHouseSlowxc")
    imagebutton:
        focus_mask True
        idle "v071/topview.png"
        hover "v071/topview.png"
        action Jump ("IvankaHouseTopFastxc") 
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("MelaniaHouseSwitchxc") 

label IvankaHouseTopSlowxc:
scene whdoggyivankatopbackground
show ivankatopwhfuckslow
call screen ivankawhfucktopslow01xc
screen ivankawhfucktopslow01xc:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("IvankaHouseEndxc")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("IvankaHouseTopFastxc") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("IvankaHouseSlowxc") 
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("MelaniaHouseSwitchxc") 

label IvankaHouseTopFastxc:
if ivankadeepx:
    mc "Gonna POUND that presidential-family fuckhole HARDER and FASTER!"
if ivankadeepx == False:
    mc "Am I DEEP enough inside your pussy Ivanka?"
    iv "Oooh, YES! But go faster please, fuck me HARD, make me CUM!"
    $ ivankadeepx = True
scene whdoggyivankatopbackground
show ivankatopwhfuckfast
call screen ivankawhfucktopfast01xc
screen ivankawhfucktopfast01xc:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("IvankaHouseEndxc")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("IvankaHouseTopSlowxc")
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("IvankaHouseFastxc") 
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("MelaniaHouseSwitchxc") 

label IvankaHouseEndxc:
iv "Are you going to give me your fat load [name]?"
mc "* puff *  You want it? BEG FOR IT!"
iv "Ooohh, please, PLEASE, FLOOD MY FILTHY HOLE, IT'S YOURS!"
stop music
play music "Sounds/splooge02.mp3"
scene whdoggyivankabackground
show whivankacum01
with dissolve
mc "NUTTING INSIDE IVANKA TRUMPF, RHAAAA!"
window hide
with fastflash
iv "Uuuh, AAAAH, I'm coming too!"
stop music
scene whdoggyivankatopbackground
show whivankacum02
mc "There's MORE for you Ivanka, AAAAH!"
window hide
with fastflash
iv "Give it ALL to me, STALLION!"
stop music
scene whivankacumbackground blurred
show whivankacum03
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Take those shots on your amazon body, AAAH"
window hide
with fastflash
iv "CLAIM ME WITH YOUR SPERM, LIKE A TRUE ALPHA-MALE!"
play sound "Sounds/panting.mp3"
me "What about me? I'm the FIRST LADY and I should get priority for your SPECIAL PIZZA SAUCE!"
$ ivankaloadx = True
if melanialoadx:
    mc "Then come and have a taste yourself Melania..."
    iv "And I'll lick the cream off YOUR body too!"
    jump WhbothfuckEndxc
if melanialoadx == False:
    mc "Don't you worry, I've got enough cum left for YOUR PUSSY!"
    iv "Please, fuck me, I'm dying to feel that GIANT shaft STRETCHING my hole..."
    jump IvankaHouseFuckxc

label MelaniaHouseSwitchxc:
mc "Time to switch girls, this cock needs more than one pussy to make it come. Spread your legs wide open Melania!"
jump MelaniaHouseFuckbxc

label WhbothfuckEndxc:
scene whbothbackground blurred
show whbothend01
with dissolve
play sound "Sounds/lick.mp3"
mc "Oh fuck, watching you ladies going at each other is getting me HARD AGAIN!"
scene whbothbackgroundzoom
show whbothend02
with dissolve
play music "Sounds/footsteps.mp3"
me "Oh shit, I hear Donnie's footsteps. Quick, let's get dressed!"
stop music
jump IvankaGalleryb

label IvankaGallery12:
play channel1 "v10/ohyeah.mp3"
scene newovaloffice01
show mcwin01
mc "Fuck yeah!"
scene newovaloffice02
show mcwin02
with dissolve
mc "Before the FUCKING begins, my dev has instructed me to direct you to his Patreon page."
mc "If you're not yet a patron but enjoyed this now COMPLETED game, now is the time to join and leave a tip to show your appreciation."
hide mcwin02
show mcwin03
with fastdissolve
mc "So just click right THERE!..."
call screen endcredits
screen endcredits:
    modal True
    imagebutton idle "v10/epiclustpatreon.png" hover "v10/epiclustpatreon.png" xpos 1500 ypos 300 focus_mask True action OpenURL("https://www.patreon.com/epiclust")
    imagebutton idle "v10/epiclustpatreonnext.png" hover "v10/epiclustpatreonnext.png" xpos 1500 ypos 900 focus_mask True action Return
    
hide mcwin03
show mcwin04
with fastdissolve
mc "Now ladies, you're my Special SEX Advisors, so it's time to make the prez CUM!"
hide mcwin04
show mcwin05
with fastdissolve
play sound "Sounds/lick.mp3"
iv "Of course President [name]!"
me "We will make you cum as often as you like EVERY DAY from now on!"
stop music
play channel2 "Sounds/sucking.mp3"
scene melaniaivankablowbackground blurred
label MelaniaIvankaBlowSlowxc:
hide melaniaivankablowfast
show melaniaivankablowslow
call screen melaniaivankablowslow01xc
screen melaniaivankablowslow01xc:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MelaniaIvankaBlowEndxc")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MelaniaIvankaBlowFastxc") 

label MelaniaIvankaBlowFastxc:
hide melaniaivankablowslow
show melaniaivankablowfast
mc "You're getting my juices going, girls..."
me "We'll make them go FASTER then!"
call screen melaniaivankablowfast01xc
screen melaniaivankablowfast01xc:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MelaniaIvankaBlowEndxc")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MelaniaIvankaBlowSlowxc")

label MelaniaIvankaBlowEndxc:
iv "He's tensing up! The Prez is about to BLOW!"
mc "He sure is..."
hide melaniaivankablowslow
hide melaniaivankablowfast
show melaniaivankablowcum01
with dissolve
me "It's bubbling at the tip..."
window hide
with fastflash
mc "AAAH! I'm about to blow a big..."
stop channel2
hide melaniaivankablowcum01
show melaniaivankablowcum02
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "...ONE! RHAAA!"
window hide
with fastflash
mc "Fuck yeah, blowing my nut in the Oval Office!!!!"
play sound "Sounds/moaning02.mp3"
hide melaniaivankablowcum02
show melaniaivankablowcum03
with dissolve
me "Look at him DOUSE us with his warm teenage spunk!"
window hide
with fastflash
iv "I've never seen such THICK, CREAMY cumshots EVER! We're getting CAKED in it!"
window hide
with fastflash
mc "There's plenty more where that came from, ladies! But I need some reserves for the next scene..."
scene newovaloffice01
show melaniaivankablowcum04
with dissolve
play sound "Sounds/kiss.mp3"
mc "And now, BRING ON THE GIRLS FOR THE FINAL ORGY!"
stop channel1
jump IvankaGalleryb
