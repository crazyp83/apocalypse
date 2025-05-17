label PennyGallery:
call screen gallerypenny
screen gallerypenny:
    add "Gallery/pennygallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("gallerypenny"), Jump ("MainGallery")]

    imagebutton:
        focus_mask True
        idle "Gallery/gallerynextpage.png"
        hover "Gallery/gallerynextpage.png"
        action [Hide ("gallerypenny"), Jump ("PennyGalleryb")]

    if renpy.seen_image("pennypool01"):
        imagebutton:
            focus_mask True
            idle "Gallery/pennygallery01.png" xpos 621 ypos 100
            hover "Gallery/pennygallery01.png"
            action Jump ("PennyGallery01")

    if renpy.seen_image("pennypool01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("PennyGallery")

    if renpy.seen_image("pennydate01"):
        imagebutton:
            focus_mask True
            idle "Gallery/pennygallery02.png" xpos 1050 ypos 100
            hover "Gallery/pennygallery02.png"
            action Jump ("PennyGallery02")

    if renpy.seen_image("pennydate01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("PennyGallery")

    if renpy.seen_image("pennystrip01"):
        imagebutton:
            focus_mask True
            idle "Gallery/pennygallery03.png" xpos 1478 ypos 100
            hover "Gallery/pennygallery03.png"
            action Jump ("PennyGallery03")

    if renpy.seen_image("pennystrip01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("PennyGallery")

    if renpy.seen_image("pennytitjobbackground"):
        imagebutton:
            focus_mask True
            idle "Gallery/pennygallery04.png" xpos 621 ypos 400
            hover "Gallery/pennygallery04.png"
            action Jump ("PennyGallery04")

    if renpy.seen_image("pennytitjobbackground") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("PennyGallery")

    if renpy.seen_image("pennyjenna01"):
        imagebutton:
            focus_mask True
            idle "Gallery/pennygallery05.png" xpos 1050 ypos 400
            hover "Gallery/pennygallery05.png"
            action Jump ("PennyGallery05")

    if renpy.seen_image("pennyjenna01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("PennyGallery")

    if renpy.seen_image("pennyjenna06"):
        imagebutton:
            focus_mask True
            idle "Gallery/pennygallery06.png" xpos 1478 ypos 400
            hover "Gallery/pennygallery06.png"
            action Jump ("PennyGallery06")

    if renpy.seen_image("pennyjenna06") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("PennyGallery")

    if renpy.seen_image("pennybedroom02"):
        imagebutton:
            focus_mask True
            idle "Gallery/pennygallery07.png" xpos 621 ypos 700
            hover "Gallery/pennygallery07.png"
            action Jump ("PennyGallery07")

    if renpy.seen_image("pennybedroom02") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("PennyGallery")

    if renpy.seen_image("pennycosplay01"):
        imagebutton:
            focus_mask True
            idle "Gallery/pennygallery08.png" xpos 1050 ypos 700
            hover "Gallery/pennygallery08.png"
            action Jump ("PennyGallery08")

    if renpy.seen_image("pennycosplay01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("PennyGallery")

    if renpy.seen_image("pennybed01"):
        imagebutton:
            focus_mask True
            idle "Gallery/pennygallery09.png" xpos 1478 ypos 700
            hover "Gallery/pennygallery09.png"
            action Jump ("PennyGallery09")

    if renpy.seen_image("pennybed01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("PennyGallery")

    add "Gallery/gallerygrid02.png"
    add "Gallery/textpenny.png"

label PennyGalleryb:
call screen gallerypennyb
screen gallerypennyb:
    add "Gallery/pennygallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("gallerypennyb"), Jump ("MainGallery")]

    imagebutton:
        focus_mask True
        idle "Gallery/gallerynextpage.png"
        hover "Gallery/gallerynextpage.png"
        action [Hide ("gallerypennyb"), Jump ("PennyGallery")]

    if renpy.seen_image("pennyjenna13"):
        imagebutton:
            focus_mask True
            idle "Gallery/pennygallery10.png" xpos 621 ypos 100
            hover "Gallery/pennygallery10.png"
            action Jump ("PennyGallery10")

    if renpy.seen_image("pennyjenna13") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGalleryb")

    if renpy.seen_image("pennyjenna17"):
        imagebutton:
            focus_mask True
            idle "Gallery/pennygallery11.png" xpos 1050 ypos 100
            hover "Gallery/pennygallery11.png"
            action Jump ("PennyGallery11")

    if renpy.seen_image("pennyjenna17") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGalleryb")

    add "Gallery/galleryfuture.png" xpos 1478 ypos 100

    add "Gallery/galleryfuture.png" xpos 620 ypos 400

    add "Gallery/galleryfuture.png" xpos 1048 ypos 400

    add "Gallery/galleryfuture.png" xpos 1478 ypos 400

    add "Gallery/galleryfuture.png" xpos 620 ypos 700

    add "Gallery/galleryfuture.png" xpos 1048 ypos 700

    add "Gallery/galleryfuture.png" xpos 1478 ypos 700

    add "Gallery/gallerygrid02.png"
    add "Gallery/textpenny02.png"
label PennyGallery01:
scene pool03
show pennypool01
pe "Yes?"
mc "That's a pretty revealing outfit you're wearing Penny..."
hide pennypool01
show pennypool02
pe "And so? The less clothes I wear, the better I feel..."
mc "Well, in that case, why don't you..."
hide pennypool02
show pennypool01
pe "I can't be naked in the pool area unfortunately, it's against the rules...."
mc "Rules? Road Warriors don't obey rules! (+1 Road Warriors)"
hide pennypool01
show pennypool03
with fastdissolve
pe "You're right! Damn it, I'm going to strut my stuff and to hell with anyone that tells me I can't!"
mc "That's the spirit! Of the ROAD WARRIORS!"
hide pennypool03
show pennypool05
with fastdissolve
pe "Now I feel liberated!"
mc "My cock is also trying to liberate itself..."
pe "It will have to wait another time, my lust for you is simply not high enough..."
mc "Damn it! I guess I'll go for a swim instead then..."
jump PennyGallery

label PennyGallery02:
play music "v07/datemusic.mp3"
scene canyon01
show pennydate01
pe "How come I'm a scout and I don't even know about this place???"
mc "Beats me, it's right next to the compound."
hide pennydate01
show pennydate02
with fastdissolve
pe "How many people know about this? And will someone else turn up while we're on our date?"
mc "Just a few and don't worry, no one will disturb us. We have the the place to ourselves for the whole morning..."
hide pennydate02
show pennydate04
with fastdissolve
pe "Good, now let's get in the water and start this date shall we?"
scene canyon02
show pennydate03
with fastdissolve
pe "The water is nice... But I feel like ALL of my skin is not enjoying it."
mc "What do you mean?"
pe "Modern society's moral constraints are not for ME. I'm a ROAD WARRIOR at heart! So I want to be free and... NAKED!"
mc "I'll all for the old values of old society, Penny!"
scene canyon01 blurred
show pennydate05
pe "That's... not really what I meant. THIS is what I meant."
mc "Yeah, that's what I meant too!"
pe "In that case, you should ALSO get naked, right!"
mc "Err... Right, right."
scene pennydate06
with dissolve
pe "Ah, that's MUCH better."
scene pennydate07
with dissolve
pe "And how are YOU doing, [name]? Enjoying the water on your FULL body?"
scene pennydate08
with dissolve
mc "Err, Yeah sure. I'm just... chilling, you know."
scene pennydate09
with dissolve
pe "With a great big HARDON! That's what you do on all your dates, you dirty boy?"
mc "Err..."
scene pennydate10
with dissolve
pe "Don't answer and let my LIPS do all the talking..."
mc "O..Okay."
pe "Now of course, this is our first date, so you won't get much from me. I'm not such an easy girl..."
scene pennydate11
with dissolve
pe "But a little kiss and a little taste of your abundant pre-cum can't hurt that much, right?"
play sound "Sounds/kiss.mp3"
pe "There, that's it."
mc "That's it? But... My hardon, it hurts!" 
pe "That'll teach you for rudely displaying your genitals on a first date... But thanks for the date anyway [name], I... enjoyed it."
stop music
jump PennyGallery

label PennyGallery03:
stop music
scene strip01
show strippenny01
pe "Oh... Well, now you know... Yes, I'm a part-time stripper. I just like the gig..."
mc "I like your gig too... So, what services do you offer?"
hide strippenny01
show strippenny02
with fastdissolve
pe "Several services, ranging from the naughty to the... very naughty!"
mc "I'll take a striptease session please."
hide strippenny02
show strippenny04
with fastdissolve
pe "Relax in the comfy chair and watch me... slowly taking off my lingerie for you."
play music "Sounds/stripmusic.mp3"
scene pennystriplarge with dissolve:
    ypos -3.0
    linear 10.0 ypos 0.0
$ renpy.pause(10.0, hard=True)
pe "Ready?"
mc "Full steam ahead!"
scene pennystrip01 with dissolve
pause
scene pennystrip02 with dissolve
pause
scene pennystrip03 with dissolve
pe "Mmh, should I take off my bra? I think I should..."
pause
scene pennystrip04 with dissolve
pause
scene pennystrip05 with dissolve
pause
scene pennystrip06 with dissolve
pause
scene pennystrip07 with dissolve
pause
scene pennystrip08 with dissolve
pause
scene pennystrip09 with dissolve
pause
scene pennystrip10 with dissolve
pause
scene strip01
show strippenny05 with fastdissolve
pe "I feel great! This is so liberating. But it's over for you [name]..."
mc "Let me liberate you some more."
pe "No. I have to work tomorrow. Have sweet dreams!"
jump PennyGallery

label PennyGallery04:
scene strip02 blurred
show strippenny05
pe "I feel great! This is so liberating. Now it's time for me to LIBERATE that dong of yours from the tight confines of your pants!"
scene pennypretitjob01 with dissolve
pe "And then, make it CAPTIVE between my big breasts..."
mc "Let me feel them first for a while please."
scene pennypretitjob02 with dissolve
pe "Yeah, maul them and soften them up for that massive CUM-CANNON of yours!"
mc "Will do!"
pe "I think you're ready. I am. So lean back and... ENJOY!"
play music "Sounds/wank.mp3"
scene pennytitjobbackground
label PennyTitjobSlowx:
show pennytitjobslow
hide pennytitjobfast
call screen pennytitjobslow01x
screen pennytitjobslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyTitjobEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PennyTitjobFastx") 

label PennyTitjobFastx:
pe "Time to speed it up and get you to release yourself all over my tits and face!"
window hide
hide pennytitjobslow
show pennytitjobfast
call screen pennytitjobfast01x
screen pennytitjobfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyTitjobEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PennyTitjobSlowx") 

label PennyTitjobEndx:
stop music
scene pennytitjobcum01
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
pe "Yes, LIBERATE your cum from the tight confines of your balls!"
scene pennytitjobbackground blurred
show pennytitjobcum02
pe "Blast it EVRYWHERE! On my tits, on my FACE!"
mc "FU-UUUCK! AAAH"
scene pennytitjobcum03
pe "Well, look at the mess you did, naughty boy!"
mc "Phew... Sorry, my shots are so POWERFUL, it's hard to aim."
pe "I saw that. You almost reached the ceiling..."
scene strip01 with dissolve
show strippenny05
pe "I hope you enjoyed the show [name]... and the titjob."
mc "I feel liberated. And tired. I'm going to go and stay captive in my bed for the night."
hide strippenny05
jump PennyGallery

label PennyGallery05:
scene pennyjenna01
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
jump PennyGallery

label PennyGallery06:
scene pennyjenna06
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
jump PennyGallery

label PennyGallery07:
scene bedroom01
show pennynight01
pe "Well, I was just about to go to bed and jill myself to sleep."
mc "And now you don't need to anymore, you've got the REAL stuff to play with!"
pe "Lucky me... And how shall the evening proceed?"
mc "I like that teddy of yours, keep it on and let's get moving."
hide pennynight01
show pennynight02
with fastdissolve
play music "v07/datemusic.mp3"
pe "So eager! Well, I'm eager too so I'll show you what I was about to do in my bed... Follow me to the sofa."
scene pennybedroom01 with dissolve
pe "Oh wow, I see you're already starting to undress... That cock of yours must be getting hard pretty FAST then!"
mc "You have no idea, it's about to tear a hole through my pants!"
scene pennybedroom02 with dissolve
pe "Let me help you... By making it get hard even FASTER!"
mc "Oh God, I... Quick, I need to..."
scene pennybedroom03 with dissolve
pe "There, much better. Free at last. Just like that hardening fucktool of yours."
mc "Phew, in the nick of time!"
scene pennybedroom04 with dissolve
pe "I feel so liberated... The only thing left to take off are my tiny panties..."
mc "Yes, yes, take them off! Or I'm going to explode all over the sofa!"
scene pennybedroom05 with dissolve
play sound "Sounds/moaning02.mp3"
pe "Now we wouldn't that, would we? Let me get my pussy nice and wet for your giant young boycock, [name]..."
mc "I just need to stick my fuckpole inside it. Like NOW!"
scene pennybedroom06 with dissolve
play sound "Sounds/boymoan.mp3"
pe "Wow, so EAGER! Go on, pump away inside of me, STUD!"
stop music
play music "Sounds/scarlettpound.mp3"
label PennyBedroomSlowx:
hide pennybedroomfast
show pennybedroomslow
call screen pennybedroomfuckslow01x
screen pennybedroomfuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyBedroomEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PennyBedroomFastx") 

label PennyBedroomFastx:
mc "I'm just so horny, I'm gonna need to fuck you faster!"
hide pennybedroomslow
show pennybedroomfast
call screen pennybedroomfuckfast01x
screen pennybedroomfuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyBedroomEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PennyBedroomSlowx") 

label PennyBedroomEndx:
play sound "Sounds/moaning03.ogg"
pe "You're making me come so much on your MONSTER fucktool! AAAH!"
stop music
scene pennybedroomfuckcum01 with dissolve
mc "Same here, your pussy is making me COME!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
pe "Go on, keep blasting that seed inside me, make me COME AGAIN! AAAH!"
scene pennybedroomfuckcum01 with fastflash
mc "I need to pull out, your pussy is DRAINING ME!"
scene pennybedroomfuckcum02 with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH!"
pe "What are you doing, I'm getting CAKED in your red-hot spunk!"
scene pennybedroomfuckcum03 with fastdissolve
mc "Oops, sorry, will try to aim better next time..."
pe "It's alright, I was just surprised, but I actually LOVED getting hosed down by your cum-cannon..."
mc "Good, cos I've got plenty more loads in store for you!"
pe "Really? Wow, what a STALLION you are, [name]! Let me get cleaned up and I'll join you on the bed for MORE THEN!"
jump PennyGallery

label PennyGallery08:
scene bedroom01
show pennycosplay01 with moveinright
pe "There I am! Ready to FUCK LIKE A HORNY BUNNY!"
mc "Well, that makes two of us!"
hide pennycosplay01
show pennycosplay02
with fastdissolve
pe "Is that so? As the female bunny, I should first entice you to fuck me, shouldn't I?"
mc "That is indeed your duty as I fight off other beta-males by repeatedly knocking them unconscious with my hard dong!"
pe "Then come closer to the den..."
play music "Sounds/stripmusic.mp3"
scene bedroom03 blurred
show pennywiggle
call screen pennywigglex
screen pennywigglex:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyWiggleEndx")
 
label PennyWiggleEndx:
pe "Are you done beating your rivals?"
mc "Of course!"
stop music
scene bedroom13 blurred
show pennycosplay03
with fastdissolve
pe "They didn't stand a chance against you and your superior ALPHA-COCK!"
scene bedroom50 blurred
show pennycosplay03b
with fastdissolve
mc "Damn right!"
scene bedroom13 blurred
show pennycosplay04
with fastdissolve
pe "Now that you've beaten them all up, time for me to prepare myself for copulation...."
mc "That's one scientific way to put it."
hide pennycosplay04
show pennycosplay05
with fastdissolve
pe "I am ready to be serviced by your harem master cock, [name]!"
mc "That's good bunny. Let me check the readiness of your bunny pussy..."
scene bedroom46
show pennymccosplay01
with fastdissolve
pe "Does it look ready?"
scene bedroom50 blurred
show pennymccosplay04
with fastdissolve
mc "It sure does, nice and wet and leaking pussy juices..."
scene bedroom13 blurred
show pennymccosplay02
with fastdissolve
play sound "Sounds/moaning.mp3"
pe "Fuck, your balls are so ENORMOUS [name]!"
mc "All the better to fill you up with lots of alpha-semen!"
hide pennymccosplay02
show pennymccosplay03
with fastdissolve
pe "Show me!"
mc "Alright, let's proceed on the bed where it's more comfortable..."
pe "And I'll take my mask off cos I want to see EVERYTHING!"
jump PennyGallery

label PennyGallery09:
scene bedroom03b
show pennybed01
pe "Alright, so what do you have planned for us to continue our all-night fuck session then?"
label PennyFuckChoicex:
menu:
    "I have a bestiality fetish. Let's go doggy!":
        pe "Woof, woof!"
        jump PennyDoggyx
    "I want to be rough on your pussy...":
        pe "As rough as a Road Warrior can be?"
        mc "You'll see..."
        jump PennyLiftx 
    "There's an unexplored hole of yours that needs to be cleared.":
        pe "Go ahead scout, explore away!"
        jump PennyAnalx
    "You look like a pretty flexible woman.":
        pe "Oooh, you're in for ACROBATIC sex then, huh?"
        mc "Err, yeah, that's right."
        pe "Then let me show you how acrobatic I can be!"
        jump PennyAcrobaticx
    "I'm done with this gallery.":
        jump PennyGallery

label PennyDoggyx:
scene bedroom18
show pennypredoggy01
with dissolve
mc "That's right, offer me your sweet behind... I'll sniff it first, like a good dog would do..."
scene bedroom48
show pennypredoggy02
with dissolve
pe "Is it to your liking? Why don't you give it a good lick? Like a dog would..."
mc "Mmh, yeah, it does look tasty."
scene bedroom34 blurred
show pennypredoggy03
with dissolve
play music "Sounds/moaning03.ogg"
play sound "Sounds/lick.mp3"
pe "Oooh, that's nice... You're getting my pussy all wet and READY FOR YOUR HUGE DONG!"
stop music
play music "Sounds/barbarasex.mp3"
label PennyDoggySlowx:
hide pennydoggypovslow
hide pennydoggypovfast
hide pennydoggyfast
scene bedroom30
show pennydoggyslow
call screen pennydoggyslow01x
screen pennydoggyslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyDoggyEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PennyDoggyFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/POVview.png"
        hover "Icons/POVview.png"
        action Jump ("PennyDoggyPOVSlowx") 

label PennyDoggyFastx:
mc "God, this pussy is so amazing, I'm going to need to FUCK IT FASTER!"
hide pennydoggypovslow
hide pennydoggypovfast
hide pennydoggyslow
scene bedroom30
show pennydoggyfast
call screen pennydoggyfast01x
screen pennydoggyfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyDoggyEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PennyDoggySlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/POVview.png"
        hover "Icons/POVview.png"
        action Jump ("PennyDoggyPOVFastx") 

label PennyDoggyPOVSlowx:
hide pennydoggyfast
hide pennydoggyslow
hide pennydoggyfast
scene bedroom14
show pennydoggypovslow
call screen pennydoggypovslow01x
screen pennydoggypovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyDoggyEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PennyDoggyPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("PennyDoggySlowx") 

label PennyDoggyPOVFastx:
mc "God, this pussy is so amazing, I'm going to need to FUCK IT FASTER!"
hide pennydoggyslow
hide pennydoggyslow
hide pennydoggyfast
scene bedroom14
show pennydoggypovfast
call screen pennydoggypovfast01x
screen pennydoggypovfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyDoggyEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PennyDoggyPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("PennyDoggyFastx") 
        
label PennyDoggyEndx:
pe "You need to mark your territory by CUMMING ALL OVER YOUR BITCH IN HEAT!"
mc "ALright, I was indeed just about to..."
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
hide pennydoggyslow
hide pennydoggyfast
hide pennydoggypovslow
hide pennydoggypovfast
scene bedroom14
show pennydoggycum01
with fastdissolve
mc "...CUM! RHAAA!"
show pennydoggycum01 with fastflash
pe "YES, keep going [name], plaster me in your young spunk! AAAH!"
scene bedroom30 blurred
show pennydoggycum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Bend over, I'm gonna cover your back with my unending streams of boygoo! AAH!"
stop sound
scene bedroom14
show pennydoggycum03
with fastdissolve
pe "Your sperm is so THICK and HEAVY on my back!"
mc "I have some pretty heavy balls, that's why."
pe "Now I hope you can get ROCK-HARD AGAIN, cos I want you to fuck me some more!"
mc "No worries, get cleaned up and I'll be with you in no time with a raging hardon."
scene bedroom03b
show pennybed01
with dissolve
pe "All cleaned up. Waiting for some more HOT FUN."
jump PennyFuckChoicex
    
label PennyLiftx:
scene bedroom13
show pennyprestand01
with dissolve
mc "So... You want it rough, hey?"
pe "Y...Yes. Please fuck the SHIT OUT OF ME!"
mc "You asked for it..."
scene bedroom13 blurred
play music "Sounds/barbarasex.mp3"
label PennyLiftSlowx:
hide pennystandfast
show pennystandslow
call screen pennystandslow01x
screen pennystandslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyLiftEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PennyLiftFastx") 

label PennyLiftFastx:
mc "Prepare to have my fat cock shoved up your quivering pussy even FASTER!"
hide pennystandslow
show pennystandfast
call screen pennystandfast01x
screen pennystandfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyLiftEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PennyLiftSlowx") 

label PennyLiftEndx:
pe "You're POUNDING me so hard! Cum inside me, FLOOD MY WOMB!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
hide pennystandslow
hide pennystandfast
show pennystandcum01
with fastdissolve
mc "Ask and you shall receive! BIG TIME, RHAAA!"
show pennystandcum01 with fastflash
pe "Sssooo much cum! Gimme MORE!"
hide pennystandcum01
show pennystandcum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Bend over, I'm gonna cover your back with my unending streams of boygoo! AAH!"
stop sound
hide pennystandcum02
show pennystandcum03
with fastdissolve
pe "You fucked me so well, now kiss me!"
play sound "Sounds/kiss.mp3"
mc "Who knew harem sex could be so romantic?"
pe "Shut up, silly boy. And since your cock is still ROCK-HARD, fuck me some more!"
mc "Damn right I'm still rock-hard and I'll give you more!"
hide pennystandcum03
show pennyprestandb01
with fastdissolve
mc "First, I'll lift you up arm in my muscular arms..."
pe "Ooh, you're so godamn STRONG!"
hide pennyprestandb01
show pennystandb00
with fastdissolve
mc "And then I'll IMPALE you on my mighty shaft!"
hide pennystandb00
play music "Sounds/barbarasex.mp3"
label PennyStandSlowx:
hide pennystandbfast
show pennystandbslow
call screen pennystandbslow01x
screen pennystandbslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyStandEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PennyStandFastx") 

label PennyStandFastx:
pe "Fuck me even faster with your cum-covered DONKEY-DICK, please!"
hide pennystandbslow
show pennystandbfast
call screen pennystandbfast01x
screen pennystandbfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyStandEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PennyStandSlowx") 

label PennyStandEndx:
pe "I want ANOTHER dose of plentiful boyspunk! Can you give it to me [name]?"
mc "You bet I can! Here it comes..."
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
hide pennystandbslow
hide pennystandbfast
show pennystandbcum01
with fastdissolve
mc "RIGHT NOW, RHAAA!"
scene bedroom41 blurred
show pennystandbcum02
with dissolve
pe "Oh fuck, you're pummelling my womb with your pellets of cum!"
show pennystandbcum02 with fastflash
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "That's right, and I've got more for you Penny!"
stop sound
scene bedroom13 blurred
show pennystandbcum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
pe "Damn boy, you truly are a CUM MACHINE!"
mc "Cos your body is so cum-inducing! AAAH!"
pe "You're going to PLASTER your bedroom with your spunk!"
hide pennystandbcum03
show pennystandbcum04
with fastdissolve
stop sound
mc "It's fine, the cleaning lady we never see will come round after our fuck session, don't worry..."
pe "That's nice to know... Are you still HARD for more?"
mc "Yep! Get on the bed and wait for my instructions..."
scene bedroom03b
show pennybed01
with dissolve
pe "So, what do you have in store for us, big boy?"
jump PennyFuckChoicex
    
label PennyAnalx:
scene bedroom20
show pennypreanal01
with dissolve
pe "Let me prep my rosebud for your MASSIVE TOOL..."
mc "Yeah, you do that Penny, while I jack off and get ROCK-HARD watching you."
scene bedroom17
show pennypreanal02
with dissolve
pe "Just a second, let me stick my finger and get some slime in there..."
mc "Hurry up please, I'm raring to go!"
pe "Ok. There, I'm ready. ANAL-IZE ME NOW!"
scene bedroom12 blurred with dissolve
play music "Sounds/fucksound.mp3"
label PennyAnalSlowx:
hide pennyanalfast
hide pennyanalpovfast
hide pennyanalpovslow
scene bedroom18
show pennyanalslow
call screen pennyanalslow01x
screen pennyanalslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PennyAnalFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("PennyAnalPOVSlowx")

label PennyAnalFastx:
hide pennyanalslow
hide pennyanalpovfast
hide pennyanalpovslow
scene bedroom18
show pennyanalfast
call screen pennyanalfast01x
screen pennyanalfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PennyAnalSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("PennyAnalPOVFastx") 

label PennyAnalPOVSlowx:
hide pennyanalslow
hide pennyanalfast
hide pennyanalpovfast
scene bedroom14 blurred
show pennyanalpovslow
call screen pennyanalpovslow01x
screen pennyanalpovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PennyAnalPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("PennyAnalSlowx") 

label PennyAnalPOVFastx:
hide pennyanalslow
hide pennyanalfast
hide pennyanalpovslow
scene bedroom14 blurred
show pennyanalpovfast
call screen pennyanalpovfast01x
screen pennyanalpovfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("PennyAnalPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("PennyAnalFastx") 

label PennyAnalEndx:
pe "Don't hold it in, just BLAST YOUR SPERM IN MY BACKSIDE!"
mc "If you ask so eargerly, then yes, I'll do it..."
scene bedroom49 blurred
show pennyanalcum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...NOW! RHAAAA!"
pe "AAAH, I'm CUMMING TOO! Feeling those red-hot pellets of young spunk EXPLODING inside me is just so incredible!!!"
show pennyanalcum01 with fastflash
mc "Oh God, I'm  cumming SSOOO MUCH, it's backing up! Need... To... PULL OUT!"
scene bedroom26 blurred
show pennyanalcum02
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Now I can let it fly, RHAAA!"
show pennyanalcum02 with fastflash
pe "You're drenching your coversheets with your own filthy sperm, this is so hot!"
scene bedroom52
show pennyanalcum03
with dissolve
stop sound
pe "Damn, my bowels are filled to the brim with your cream. I'm farting spunk."
mc "Eeew, too much information, TMI! Get cleaned up and stop farting. We have more positions to explore."
scene bedroom03b
show pennybed01
with dissolve
pe "Done! So which position shall we explore together this time?"
jump PennyFuckChoicex

label PennyAcrobaticx:
scene bedroom41 blurred
show pennypreacrob01
with dissolve
pe "Let's see... A huge hard pole sticking straight up in the air..."
mc "What are you going to do about it Penny?"
pe "Move your knees up a bit, I'll show you..."
scene bedroom18
show pennypreacrob02
with dissolve
pe "There, that's a good position."
mc "For what?"
pe "For THIS."
scene bedroom18 blurred
label PennyAcrobaticSlowx:
hide pennyacrobaticfast
hide pennyacrobaticpovslow
hide pennyacrobaticpovfast
scene bedroom18 blurred
show pennyacrobaticslow
call screen pennyacrobaticslow01x
screen pennyacrobaticslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyAcrobaticEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PennyAcrobaticFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/POVview.png"
        hover "Icons/POVview.png"
        action Jump ("PennyAcrobaticPOVSlowx") 

label PennyAcrobaticPOVSlowx:
hide pennyacrobaticslow
hide pennyacrobaticfast
hide pennyacrobaticpovfast
scene bedroom08 blurred
show pennyacrobaticpovslow
call screen pennyacrobaticpovslow01x
screen pennyacrobaticpovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyAcrobaticEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PennyAcrobaticPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("PennyAcrobaticSlowx") 

label PennyAcrobaticFastx:
hide pennyacrobaticslow
hide pennyacrobaticpovslow
hide pennyacrobaticpovfast
scene bedroom18 blurred
show pennyacrobaticfast
call screen pennyacrobaticfast01x
screen pennyacrobaticfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyAcrobaticEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PennyAcrobaticSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/POVview.png"
        hover "Icons/POVview.png"
        action Jump ("PennyAcrobaticPOVFastx") 

label PennyAcrobaticPOVFastx:
hide pennyacrobaticslow
hide pennyacrobaticfast
hide pennyacrobaticpovslow
scene bedroom08 blurred
show pennyacrobaticpovfast
call screen pennyacrobaticpovfast01x
screen pennyacrobaticpovfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PennyAcrobaticEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("PennyAcrobaticPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("PennyAcrobaticFastx") 
            
label PennyAcrobaticEndx:
mc "Penny, I'm warning you, I'm about to BLOW BIG TIME!"
pe "DO IT, EMPTY YOUR GIANT SEEDMAKERS!"
scene bedroom08 blurred
show pennyacrocum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
pe "YES!!!! Cum in me, give me your sweet young SEED! AAAH!"
play music "Sounds/splooge01.mp3"
show pennyacrocum01 with fastflash
mc "I can't stop... AAAH, I can't..."
hide pennyacrocum01
show pennyacrocum02
with fastdissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...STOP! RHAAA!"
pe "Oh my God, your blasts are so POWERFUL, I'm being thrown up in the air like a ragdoll!"
scene bedroom18
show pennyacrocum03
mc "There's more for you Penny, AAAH, take ALL my cum!"
pe "I will gladly! KEEP GOING, COVER ME IN YOUR THICK SCUM!"
show pennyacrocum03 with fastflash
pe "Sssoo, ssoo MUCH OF IT! I love it!"
scene bedroom03b blurred
show pennyacrocum04
stop sound
pe "Look at the CRAZY mess you made [name]! It's not normal than a boy can cum THAT MUCH, you know?"
mc "Well, I've got big balls, that's why. Speaking of which, they're not empty yet."
pe "No way! You want more?"
mc "Yep."
jump PennyFuckChoicex

label PennyGallery10:
stop music
scene pennyjenna06
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
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
pe "ALL OF IT, I need you FOCUSED for our scouting mission..."
scene pennyjenna15 with dissolve
stop sound
play sound "Sounds/lick.mp3"
je "Hum,, the next best thing after pussy juice and there's a LOT of it!"
scene pennyjenna16 with dissolve
play sound "Sounds/lick.mp3"
pe "I'll help you... *slurp* But we have to leave soon, [name] made us late already."
je "Don't worry about the mess Penny, I'll clean *slurp* ...it up. Go on your mission."
jump PennyGalleryb

label PennyGallery11:
stop music
$ jennafucktoldx = False
scene pennyjenna06
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
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Of fuck, I'm cumming...  A bit. Some pre-cum mixed with spunk... AAAH!"
scene pennyjenna20 with dissolve
je "Mmh, I made you cum prematurely my liege?"
mc "Y..Yeah. But I'm still HARD. I need to cum PROPERLY this time!"
scene pennyjennaprefuck01 with dissolve
je "Alright, your dick was so tasty that I agree for it to taste my PUSSY! SO come anf fuck me NOW!"
pe "Oooh! And I'll frig myself while watching you two go at it!"
play music "Sounds/womansex02.mp3"
label JennaSlowx:
hide jennafast
hide jennapovslow
hide jennapovfast
show jennaslow
call screen jennaslow01x
screen jennaslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("JennaEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("JennaFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("JennaPOVSlowx") 

label JennaPOVSlowx:
hide jennaslow
hide jennafast
hide jennapovfast
show jennapovslow
call screen jennapovslow01x
screen jennapovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("JennaEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("JennaPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("JennaSlowx") 

label JennaFastx:
if jennafucktoldx == False:
    pe "Go on [name], pump your monster shaft inside her even FASTER!"
    $ jennafucktoldx = True
hide jennaslow
hide jennapovslow
hide jennapovfast
show jennafast
call screen jennafast01x
screen jennafast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("JennaEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("JennaSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("JennaPOVFastx") 

label JennaPOVFastx:
hide jennaslow
hide jennafast
hide jennapovslow
show jennapovfast
call screen jennapovfast01x
screen jennapovfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("JennaEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("JennaPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("JennaFastx") 
            
label JennaEndx:
je "Please deliver your NUTJUICE, my liege!"
mc "Anytime... Soon.... Any..."
scene pennyjennacum01 with dissolve
if persistent.cumsoundon:
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
jump PennyGalleryb
    