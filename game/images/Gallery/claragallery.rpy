label ClaraGallery:
call screen galleryclara
screen galleryclara:
    add "Gallery/claragallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("galleryclara"), Jump ("MainGallery")]

    if renpy.seen_image("clarastrip01"):
        imagebutton:
            focus_mask True
            idle "Gallery/claragallery01.png" xpos 621 ypos 100
            hover "Gallery/claragallery01.png"
            action Jump ("ClaraGallery01")

    if renpy.seen_image("clarastrip01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("ClaraGallery")

    if renpy.seen_image("clarahandjobcum01"):
        imagebutton:
            focus_mask True
            idle "Gallery/claragallery02.png" xpos 1050 ypos 100
            hover "Gallery/claragallery02.png"
            action Jump ("ClaraGallery02")

    if renpy.seen_image("clarahandjobcum01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("ClaraGallery")

    if renpy.seen_image("clara11"):
        imagebutton:
            focus_mask True
            idle "Gallery/claragallery03.png" xpos 1478 ypos 100
            hover "Gallery/claragallery03.png"
            action Jump ("ClaraGallery03")

    if renpy.seen_image("clara11") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("ClaraGallery")

    if renpy.seen_image("claradate05"):
        imagebutton:
            focus_mask True
            idle "Gallery/claragallery04.png" xpos 620 ypos 400
            hover "Gallery/claragallery04.png"
            action Jump ("ClaraGallery04")

    if renpy.seen_image("claradate05") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 620 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("ClaraGallery")

    if renpy.seen_image("claralingerie01"):
        imagebutton:
            focus_mask True
            idle "Gallery/claragallery05.png" xpos 1050 ypos 400
            hover "Gallery/claragallery05.png"
            action Jump ("ClaraGallery05")

    if renpy.seen_image("claralingerie01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("ClaraGallery")

    if renpy.seen_image("clarabedroom01"):
        imagebutton:
            focus_mask True
            idle "Gallery/claragallery06.png" xpos 1478 ypos 400
            hover "Gallery/claragallery06.png"
            action Jump ("ClaraGallery06")

    if renpy.seen_image("clarabedroom01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("ClaraGallery")

    if renpy.seen_image("clarabed"):
        imagebutton:
            focus_mask True
            idle "Gallery/claragallery07.png" xpos 620 ypos 700
            hover "Gallery/claragallery07.png"
            action Jump ("ClaraGallery07")

    if renpy.seen_image("clarabed") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 620 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("ClaraGallery")

    add "Gallery/galleryfuture.png" xpos 1050 ypos 700

    add "Gallery/galleryfuture.png" xpos 1478 ypos 700

    add "Gallery/gallerygrid02.png"
    add "Gallery/textclara.png"

label ClaraGallery01:
scene strip01
show stripclara01
cl "Thank you for choosing me... I am... honored. My name is sister Clara."
mc "I'll take a striptease session please."
hide stripclara01
show clara03 with fastdissolve
cl "Relax in the comfy chair and watch... A nun stripping for cash."
play music "Sounds/stripmusic.mp3"
scene clarastriplarge with dissolve:
        ypos -3.0
        linear 10.0 ypos 0.0
$ renpy.pause(10.0, hard=True)
cl "I will now unveil myself for you..."
mc "Unveil away!"
scene clarastrip01 with dissolve
pause
scene clarastrip02 with dissolve
pause
scene clarastrip03 with dissolve
pause
scene clarastrip04 with dissolve
pause
scene clarastrip05 with dissolve
pause
scene clarastrip06 with dissolve
pause
scene clarastrip07 with dissolve
pause
scene clarastrip08 with dissolve
pause
scene clarastrip09 with dissolve
pause
scene clarastrip10 with dissolve
pause
stop music
scene strip01
show stripclara03
cl "That's it, I hope you enjoyed the show, I feel like a sinner now..."
mc "Well, you know what you could do to repent your sins right?"
cl "Yes I do. I will go to the church and pray."
mc "Ah. That's NOT what I had in mind..."
jump ClaraGallery

label ClaraGallery02:
scene strip02 blurred
show stripclara04
cl "And now for the NAUGHTY part... And I can see you already have your cock out, you're such a NAUGHTY boy!"
scene claraprehandjob01 with dissolve
cl "And what a mighty phallus it is! One worthy of being serviced by a sinner like me..."
mc "Then get on your knees and prep it by licking my fat balls. They're the ones that contain the Holy Sperm I'll be delivering at the end of this session."
scene claraprehandjob02 with dissolve
cl "Of course! They deserve praise for being so... large and bountiful. *slurp*"
mc "Yeah, that's good Sister Clara...."
cl "And now for the main course... I'll use both hands since you are so LARGE and I am a true sinner!"
play music "Sounds/wank.mp3"
scene clarahandjobbackground
label ClaraHandjobSlowx:
show clarahandjobslow
hide clarahandjobfast
call screen clarahandjobslowx
screen clarahandjobslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraHandjobEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ClaraHandjobFastx") 

label ClaraHandjobFastx:
cl "I'll jack your shaft as fast as I can [name]! Prepare to shoot your Holy Sperm EVERYWHERE!"
window hide
hide clarahandjobslow
show clarahandjobfast
call screen clarahandjobfastx
screen clarahandjobfastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraHandjobEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ClaraHandjobSlowx") 

label ClaraHandjobEndx:
hide clarahandjobslow
hide clarahandjobfast
show clarahandjobcum01
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
cl "Yes, let it all out, let the Holy Sperm flow bountifully over the New Garden of Eden!"
hide clarahandjobcum01
show clarahandjobcum02
stop music
cl "Well, I feel like I have washed away some of my dreadful sins by servicing a boy with a phallus that is worthy of Saint-Manhood!"
mc "Gee, that church sure is weird. It wasn't like that in my days. But I ain't complaining, thank you Santorum!"
jump ClaraGallery

label ClaraGallery03:
stop music
play sound "Sounds/footsteps.mp3"
scene cryptenter
mc "Oh, oh, Father Tyrone and Sister Clara are entering the Moist Crypt. Let's follow them and hide in the shadows."
stop sound
scene cryptdooropen with dissolve
play sound "Sounds/doorsqueak.mp3"
mc "This door's hinges clearly need some WD-69."
stop sound
scene crypt01 with fade
mc "I found a good hiding place with a clear view of the crypt. What a stroke of luck. Thank you dev."
window hide
show clara10 with moveinleft
mc "Oh, Oh, Clara is wearing some rather naughty nun outfit..."
ty "Sister Clara, do you confess to your utter depravity?"
cl "Y.. Yes, Father."
ty "And do you know what is the punishment for sinning whores like you?"
hide clara10
show clara10b
with fastdissolve
cl "Y..Yes Father. But, I..."
ty "Silence! May the Phallus Lord have mercy on you, cos I sure won't. Assume your position for your Holy Flogging."
scene crypt05
show clara11
with dissolve
ty "I will administer your flogging in my Punisher outfit. As per the rules."
cl "But the rules say th..."
ty "Silence! I KNOW the rules, don't try and teach them to me! Now lift that fine ass higher to the Phallus Lord..."
hide clara11
show clara12
with dissolve
ty "That's better... What a shame it is to flog such a nice piece of booty..."
cl "Wh...What are you saying Father?"
ty "Tell you what, I will commute your punishment to Holy Spanking."
cl "I... never heard of this, Fath..."
hide clara12
show clara13
with dissolve
ty "Silence! The rules are clear, it's not my fault if you are an ignorant slut!"
hide clara13
show clara14
with fastdissolve
play sound "Sounds/slap.mp3"
ty "Take that, you depraved hussy!"
hide clara14
show clara13
with fastdissolve
cl "AAAH, you're hurting me Father!"
hide clara13
show clara14
with fastdissolve
play sound "Sounds/slap.mp3"
ty "And some more, devilishly tempting creature!"
hide clara14
show clara13
with fastdissolve
cl "AAAH, I repent, please stop!"
ty "Not good enough, get on my knees for a REAL spanking."
hide clara13
show clara15
with fastdissolve
ty "Yeah, that's nice..."
cl "But Father, I can feel your... thingie rubbing ag..."
hide clara15
show clara16
with fastdissolve
play sound "Sounds/slap.mp3"
ty "Silence while I spank you!"
hide clara16
show clara15
with fastdissolve
mc "It feels wrong. And kinda right at the same time knowing that crazy Church. I don't know what to make of it..."
hide clara15
show clara16
with fastdissolve
play sound "Sounds/slap.mp3"
ty "And don't you dare complain to the Cardinal, you hear me, nasty bitch?"
mc "Oh, oh, he's hiding something..."
cl "AAAH! I... I promise, Father."
window hide
play sound "Sounds/drop.mp3"
$ renpy.pause(1.0, hard=True)
mc "Ah shit, I dropped a candelaber... Let's get the hell out of here quickly!"
stop sound
jump ClaraGallery

label ClaraGallery04:
play music "v07/datemusic.mp3"
scene canyon01
show claradate01
cl "I hope this bathing suit is to your liking, it is unfortunately the only one the Church will allow me to wear..."
mc "My imagination is seeing right through it, so don't worry."
cl "Oh... Well, I sure hope that you have a... nice imagination."
hide claradate01
show claradate02
with fastdissolve
cl "It is amazing how the sun shining from the Phallus Lord's One Eye turns this canyon into such a wonderful and peaceful place..."
cl "I really don't know how to thank you for showing me this place..."
mc "An extra lust point perhaps?"
hide claradate02
show claradate03
with fastdissolve
cl "That would be...too soon. This date hasn't even started properly yet."
cl "And I... I am embarrassed to admit... that I can't swim. I... never learnt."
hide claradate03
show claradate04
with fastdissolve
mc "Well don't worry, I'm a good swimmer and I'll teach you."
cl "Oh really? That is... so sweet of you... I actually brought along an inflatable banana float. Which is all I could find in the Church's inventory."
mc "That should do the trick to start with. I'll blow it up and you just get in the water where it's shallow."
scene claradate05 with fastdissolve
cl "I... I think I'm in too deep, I can't feel the bottom of the lake!" 
mc "Hang on, I'll come and help you Clara!" 
scene claradate06 with fastdissolve
mc "There, you have nothing to worry about anymore. Why don't you try without the float?"
cl "O...Okay, But you stay behind me to catch me if I start drowning, right?"
mc "Of course, I'll be right behind you."
scene claradate07 with dissolve
mc "See, it wasn't so hard. And I can easily catch you if you slip and carry you to safety."
cl "Thanks [name]. I feel... safer with you around... And I know you could easily lift me in your... muscular arms."
mc "You want me to show you?"
cl "Err, alright, but please hold me tight [name]!"
scene claradate08 with dissolve
mc "I don't need to hold you tight when I can just hold you with one arm up in the air!"
cl "Dear Phallus Lord! You are sso STRONG! But please let me down, I am scared of height on top of being scared of water!"
scene claradate09 with dissolve
cl "This date went... very well. I haven't felt that way since I... embraced the Phallus Lord and made my vows..."
mc "Why don't you embrace ME this time then?"
scene claradate10 with dissolve
play sound "Sounds/kiss.mp3"
cl "Mmmh...."
mc "*Bingo*"
scene claradate09 with dissolve
cl "Let's go back to the compound, it's getting late and I have Church duty."
mc "Of course Clara, I'll help you back onto the shore."
stop music
jump ClaraGallery


label ClaraGallery05:
play music "v07/datemusic.mp3"
scene bedroom02 blurred
show claralingerie01 at center with moveinright
cl "Here I am. Do you like it? The white symbolizes PURITY. Are you intentions PURE, [name]?"
mc "They are indeed. Purely sexual, that is."
hide claralingerie01
show claralingerie02
with fastdissolve
cl "I know I am in for a HOT night of PURE RAW UNADULTERED SEX with you!"
mc "You're certainly getting me in the mood for that..."
hide claralingerie02
show claralingerie03
with fastdissolve
mc "Yeah, most definitely...."
hide claralingerie03
show claralingerie04
with fastdissolve
cl "Should I remove it sensuously for you? Like I'm a naughty stripper?"
mc "Fuck yeah!"
hide claralingerie04
show claralingerie05
with fastdissolve
cl "And I won't make you pay this time. Since you are giving me such a generous maintenance allowance."
mc "Damn right I am!"
hide claralingerie05
show claralingerie06
with fastdissolve
cl "Now come and show me that phallus that deserves so much praise."
mc "I'm ROCKHARD for you Clara!"
hide claralingerie06
show claralingerie07
with fastdissolve
cl "Oh my Phallus Lord, that dick feels so HEAVY!"
mc "Ten pounds of pure raw meat for you!"
scene bedroom13 blurred
show claralingerie08
with fastdissolve
play sound "Sounds/kiss.mp3"
cl "I'm so horny... Sitting on your POWERFUL fucktool."
mc "Then hop on the bed and I'll be right with you..."
stop music
jump ClaraGallery

label ClaraGallery06:
play music "v07/datemusic.mp3"
scene bedroom02
show claraharem01 with moveinright
cl "Here I am, ready to be PUNISHED, Master!"
mc "Good. Now show me what I'll be working on... Turn around for starters..."
hide claraharem01
show claraharem04
with fastdissolve
cl "Like so? So you can admire my naughty ass cheeks?"
mc "Yeah, the ones I'm gonna be SPANKING!"
hide claraharem04
show claraharem07
with fastdissolve
cl "I hope you SPANK me good [name], because I have been a VERY NAUGHTY SISTER!"
scene bedroom02 blurred
show claraharem08
with fastdissolve
mc "Oh, I'm gonna spank it good... Cos you're being naughty right now!"
scene bedroom02
show claraharem02
with fastdissolve
cl "But I'm being naughty for YOU! So you can help me relieve me of my sins..."
mc "And it is my therefore my duty to PUNISH you and relive you of that sin!"
hide claraharem02
show claraharem03
with fastdissolve
cl "I can't thank you enough for being such a good sin-reliever... *kiss*"
mc "Of course, you need to undress completely if I am to administer a proper spanking..."
hide claraharem03
show claraharem05
with fastdissolve
cl "I am naked and ready, [name]..."
mc "You're a tease Clara! A NAUGHTY tease! Come and sit on my lap and get ready for your SPANKING!"
stop music
scene clarabedroom01 with dissolve
mc "Prepare to receive your PUNISHMENT!"
cl "Spank me, \"[name] the Punisher\", I deserve it and you're the man to deliver!"
scene clarabedroom02 with fastdissolve
play sound "Sounds/slap.mp3"
cl "...AAAH!"
scene clarabedroom01 with fastdissolve
mc "Not enough, you need to be spanked some more!"
cl "YES I DO! Do it HARDER this time!"
scene clarabedroom02 with fastdissolve
play sound "Sounds/slap.mp3"
$ renpy.pause(0.3, hard=True)
scene clarabedroom01 with fastdissolve
mc "I'll spank you till you're red in the butt!"
scene clarabedroom02 with fastdissolve
play sound "Sounds/slap.mp3"
$ renpy.pause(0.3, hard=True)
scene clarabedroom02b with dissolve
cl "You battered my poor sinful ass... But it feels good. Like I am relieved of a heavy weight."
mc "There is still some inner sin in you that needs to be removed..."
scene clarabedroom03 with dissolve
mc "Let me reach for it..."
cl "Oooh, what... What are you doing?"
scene clarabedroom04 with dissolve
mc "Just my duty as \"[name] the Punisher\"."
play sound "Sounds/womanmoan.mp3"
scene clarabedroom05 with dissolve
mc "Removing that sin that you're holding DEEP down inside you!"
cl "Th... Thank you, but.... AAAHH, I'm cumming!"
play music "Sounds/moaning03.ogg"
scene clarabedroom06 with dissolve
play sound "Sounds/splooge01.mp3"
mc "I think that's it, you released it... We can move on. Hop onto the bed and let's FUCK!"    
jump ClaraGallery

label ClaraGallery07:
$ claratitssaidx = False
label ClaraFuckChoicex:
scene bedroom03b blurred
show clarabed
cl "What Holy Phallic activities should we engage in [name]?"
stop music
menu:
    "My Phallus demands a warm mouth. And warm tits.":
        cl "Then it shall first enjoy the warmth of my tits followed by the hotness of my mouth and throat!"
        jump ClaraBlowjobx
    "Lay on your back Clara, I'm gonna pound your pussy to oblivion!":
        cl "Oblivion??? I don't know... Alright, I AM a SINFUL nun, DO IT!"
        jump ClaraLiftx 
    "Lather my Saint-Manhood with Holy Baby Oil and let's see if we can make it GROW!" if canonized and toldclaracanonized:
        cl "That would be the HOLIEST of sights indeed if it works! Oh, I so WISH it will work!"
        jump ClaraHugeCockx
    "A sinful nun such as yourself needs a thorough backdoor scrubbing.":
        cl "You mean to stick your massive pole in my ASS?"
        mc "Yep."
        cl "Then do a proper rimjob on it to make it nice and slick for your ass-pounder!"
        mc "Alright, I'm in."
        jump ClaraAnalx
    "I'm done with this gallery.":
        jump ClaraGallery

label ClaraBlowjobx:
scene clarapretits01 with dissolve
mc "You're excited by this aren't you? You're getting ME super-HARD too!"
cl "MMmh, yes, I feel like I'm ALIVE again. Bring that MONSTER ROD closer, [name]... Between my tits!"
scene clarapretits02 with dissolve
mc "Interesting. An upside down titfuck."
cl "That way I can lick your fat dangling balls on each upstroke..."
play sound "Sounds/lick.mp3"
mc "Oooh, don't start just yet, let me get into a tempo..."
play channel1 "Sounds/wank.mp3"
play channel2 "Sounds/moaning02.mp3"
label ClaraTitfuckSlowx:
hide claratitfuckfast
hide claratitfuckpovslow
hide claratitfuckpovfast
show claratitfuckslow
call screen claratitfuckslow01x
screen claratitfuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraTitfuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ClaraTitfuckFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("ClaraTitfuckPOVSlowx") 

label ClaraTitfuckPOVSlowx:
hide claratitfuckslow
hide claratitfuckfast
hide claratitfuckpovfast
show claratitfuckpovslow
call screen claratitfuckpovslow01x
screen claratitfuckpovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraTitfuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ClaraTitfuckPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("ClaraTitfuckSlowx") 

label ClaraTitfuckFastx:
if claratitssaidx == False:
    mc "Damn, those tits wrapped around my shaft... I'm going to pummel between them FASTER!"
    $ claratitssaidx = True
hide claratitfuckslow
hide claratitfuckpovslow
hide claratitfuckpovfast
show claratitfuckfast
call screen claratitfuckfast01x
screen claratitfuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraTitfuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ClaraTitfuckSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("ClaraTitfuckPOVFastx") 

label ClaraTitfuckPOVFastx:
if claratitssaidx == False:
    mc "Damn, those tits wrapped around my shaft... I'm going to pummel between them FASTER!"
    $ claratitssaidx = True
hide claratitfuckslow
hide claratitfuckfast
hide claratitfuckpovslow
show claratitfuckpovfast
call screen claratitfuckpovfast01x
screen claratitfuckpovfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraTitfuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("ClaraTitfuckPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("ClaraTitfuckFastx") 
            
label ClaraTitfuckEndx:
mc "We'd better stop or I'll blow my load before I have a chance to throat-fuck you..."
stop channel1
stop channel2
scene clarablowjobbackgroundzoom
show claraposttits01
with dissolve
cl "Yeah, let your warm pre-cum drip onto my sinful face..."
hide claraposttits01
show clarapreblow01
with dissolve
play sound "Sounds/kiss.mp3"
cl "Such a beautiful cock...Fuck my mouth [name], relieve me of my oral sins!"    
play music "Sounds/hardsucking.mp3"
scene clarablowjobbackground blurred
label ClaraBlowSlowx:
hide clarablowfast
show clarablowslow
call screen clarablowslow01x
screen clarablowslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ClaraBlowFastx") 

label ClaraBlowFastx:
mc "Oh God, that mouth! So fucking warm and your throat is so deep! Gotta throat-fuck you faster!!"
hide clarablowslow
show clarablowfast
call screen clarablowfast01x
screen clarablowfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ClaraBlowSlowx") 

label ClaraBlowEndx:
mc "Not gonna be able to hold off much longer Clara! Gonna spew my load directly down your throat!"
window hide
hide clarablowslow
hide clarablowfast
show clarablowcum01
with dissolve
play music "v07/creampie.mp3"
mc "NOW! AAAHH!"
with fastflash
mc "Swallow that ounce-big cumshot and I'll give you more of the same!"
window hide
scene clarablowjobbackgroundzoom
show clarablowcum02
with dissolve
mc "Oh Damn, you're sucking me DRY-AYE, SSSOOO GOO-OOD!"
with fastflash
mc "I'll just have to pull my dong and..."
window hide
scene clarablowcum03 with dissolve
mc "...BLOW THE REST ALL OVER YOUR TITS, RHAAA!"
with fastflash
cl "Oh my Phallus Lord, there is ssooo MUCH if it!"
window hide
stop music
scene clarablowcum04 with dissolve
play sound "Sounds/lick.mp3"
cl "Let me... *lick*... suck the last dregs out of your DIVINE appendage... *slurp*"
mc "Phew! That's a good girl. I mean sister. Hang on, we can't have incest here, I mean, nun."
cl "Should I get cleaned up so you can show me some more HOT action from your holy rod?"
mc "Yes... That would be a good idea, I've got MORE in store for you, Clara!"
jump ClaraFuckChoicex

label ClaraLiftx:
scene clarapremissionary01 with dissolve
cl "Mmmh, it's so big and already dripping lovely warm pre-cum..."
mc "Mmmh, are you ready for my mighty pillar of lust, Sister Clara?"
cl "If it can relieve me of my inner sins, then yes, I am rea..."
play sound "Sounds/womanscream.ogg"
scene claramissionary00 with dissolve
cl "...DY-AAAH! Your phallus is sssooo BIG! Be careful but... ALSO, FUCK ME HARD!"

play music "Sounds/womansex02.mp3"
label ClaraMissionarySlowx:
hide claramissionaryfast
show claramissionaryslow
call screen claramissionaryslow01x
screen claramissionaryslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraMissionaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ClaraMissionaryFastx") 

label ClaraMissionaryFastx:
mc "That pussy is just divine... THe way it grips so tight on my shaft..."
cl "Then POUND IT FASTER, it's all yours [name]!"
hide claramissionaryslow
show claramissionaryfast
call screen claramissionaryfast01x
screen claramissionaryfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraMissionaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ClaraMissionarySlowx") 

label ClaraMissionaryEndx:
mc "Oh, gotta have to... stop... Or I'll blow my load too soon."
cl "Don't take it out of my pussy please, it feels so good nudged in there..."
stop music
scene clarafuckbackground
show clarapremissionary02
with dissolve
play sound "Sounds/womanmoan.mp3"
mc "Don't worry, I'll just lift you up on it..."
hide clarapremissionary02
show clarafuck00
with dissolve
mc "...And continue fucking it!"
play music "Sounds/womansex01.mp3"
label ClarafuckSlowx:
hide clarafuckfast
scene clarafuckbackground
show clarafuckslow
call screen clarafuckslow01x
screen clarafuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClarafuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ClarafuckFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("ClarafuckTopSlowx") 

label ClarafuckTopSlowx:
show clarafucktopslow
call screen clarafucktopslow01x
screen clarafucktopslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClarafuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ClarafuckTopFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("ClarafuckSlowx") 

label ClarafuckFastx:
hide clarafuckslow
scene clarafuckbackground
show clarafuckfast
call screen clarafuckfast01x
screen clarafuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClarafuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ClarafuckSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("ClarafuckTopFastx") 

label ClarafuckTopFastx:
show clarafucktopfast
call screen clarafucktopfast01x
screen clarafucktopfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClarafuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("ClarafuckTopSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("ClarafuckFastx") 
            
label ClarafuckEndx:
mc "Now THIS time, I will BLOW MY LOAD!"
hide clarafucktopfast
hide clarafucktopslow
scene clarafuckcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
cl "I can feel it! It's SPLASHING inside my womb!"
with fastflash
mc "AAAH! I've got MORE for you! Need to pull out!"
scene clarafuckcum02 with dissolve
cl "Ooh, that feels much better, doesn't it [name]?"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "RHAAA!"
with fastflash
cl "Your CONVULSING cum-missile being able to liberally DOUSE my body with warm sperm! Aah, it's so RED-HOT!" 
scene clarafuckcum03 with dissolve
play sound "Sounds/panting.mp3"
mc "Damn it, you made me spew like CRAY-AY-ZY!"
cl "Well, I'm glad I could also help YOU relieve yourself of that sinful nutcream!"
mc "Not quite yet, I may have another load churning in there for you..."
jump ClaraFuckChoicex

label ClaraHugeCockx:
scene bedroom40 blurred
show claraprehuge00
with dissolve
cl "Let me cover my hands with my Holy Baby Oil... And then I'll give you a nice oily handjob..."
scene bedroom37
show claraprehuge01a
with dissolve
cl "Are you ready to GROW even BIGGER, big boy?"
mc "Oh, fuck, I am, I am! When I do, I'll pound you so HARD with it, Clara!"
cl "I would certainly like to FEEL that!"
play music "Sounds/wank.mp3"
scene bedroom37 blurred
show clarahugewank
call screen clarahugewank01x
screen clarahugewank01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraHugeWankEndx")
label ClaraHugeWankEndx:
cl "May this Holy Baby Oil bless this Saint-Manhood, Oh Lord Phallus, and grant [name] the gift of..."
play sound "Sounds/thunder.mp3"
mc "I think it's working! My cock, it's getting..."
window hide
stop music
hide clarahugewank
show claraprehuge02a
with dissolve
mc "...BIGGER! AAAH!"
cl "...May the Holy Spurt descend upon this tremendous fuckstick!"
window hide
play sound "Sounds/thunder.mp3"
hide claraprehuge02a
show claraprehuge02b
with dissolve
mc "And EVEN BIGGER STILL! You did it, Clara!"
cl "It is MASSIVE now! The BIGGEST and HOLIEST of phalluses!"
scene bedroom17 blurred
show claraprehuge03
with dissolve
cl "And it's already leaking precum like a FAUCET! Your balls, they feel so HEAVY!"
play sound "Sounds/boymoan02.mp3"
mc "Oh God, I feel totally PUMPED-UP FULL OF CUM FOR YOU!"
scene claraprehuge04 with dissolve
mc "I can't wait any longer Clara, I NEED to fuck you right here, right NOW!"
cl "Please be careful with that MONSTER when you do [name]..."
scene bedroom17
show claraprehuge05
with dissolve
cl "Oh my Phallus Lord, what did I let myself into?"
mc "THIS... will totally relieve you of your inner sins!"
cl "Alright then, do it, shove your throbbing behemoth in, and pound the sin out of me!"
scene bedroom17 blurred
play music "Sounds/barbarasex.mp3"
label ClaraHugeSlowx:
hide clarahugefast
show clarahugeslow
call screen clarahugeslow01x
screen clarahugeslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraHugeEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ClaraHugeFastx") 

label ClaraHugeFastx:
cl "It takes a while to make a BEAST like that cum, I'm going to have to increase the tempo to bring you over the EDGE!"
mc "AAAH, sssooo goood...."
hide clarahugeslow
show clarahugefast
call screen clarahugefast01x
screen clarahugefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraHugeEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ClaraHugeSlowx") 

label ClaraHugeEndx:
cl "That's it, I can feel your beast RUMBLE. The spermtube is expanding!"
scene bedroom17
show clarahugecum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...Thar she blows!"
cl "Damn it, you're such a tease! RHAAA!"
hide clarahugecum01
show clarahugecum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
cl "I think you deserve some sperm ON YOU! I'll aim your cum-cannon a little bit LOWER..."
scene bedroom14 blurred
show clarahugecum03
cl "That's it, you've COVERED your bedsheet and your muscled pecs with your warm cream.... Does it feel good [name]? I bet it does... I wanna taste it too, you know..."
hide clarahugecum03
show clarahugecum04
with fastdissolve
mc "Oh fuck, I'm spent... Hang on, NO, I can KEEP ON GOING ALL NIGHT LONG!"
hide clarahugecum04
show clarahugecum05
with fastdissolve
cl "Oh my, and how shall we continue making that BEAST explode over and over again?"
jump ClaraFuckChoicex
    
label ClaraAnalx:
scene clarapreanal00
with dissolve
cl "Don't hesitate to stick your tongue as FAR as it will go inside my butthole [name]... While I keep that monstercock of yours  ROCK-HARD for the main event!"
play music "Sounds/lick.mp3"
scene clarapreanal01a with fastdissolve
pause 0.4
scene clarapreanal01b with fastdissolve
pause 0.4
scene clarapreanal01a with fastdissolve
pause 0.4
scene clarapreanal01b with fastdissolve
pause 0.4
scene clarapreanal01a with fastdissolve
pause 0.4
scene clarapreanal01b with fastdissolve
pause 0.4
scene clarapreanal01a with fastdissolve
pause 0.4
scene clarapreanal01b with fastdissolve
pause 0.4
scene clarapreanal01a with fastdissolve
pause 0.4
scene clarapreanal01b with fastdissolve
pause 0.4
stop music
cl "Mmmh, that was good, I think I'm ready to take on..."
scene clarapreanal02
with dissolve
cl "*swallow* Glup... On second thoughts... Your dick... It's just COLOSSAL!"
mc "But it will fit, don't worry."
cl "Alright, if you say so... Put it in me and ass-fuck me slowly for starters..."
play music "Sounds/fucksound.mp3"
label ClaraAnalSlowx:
hide claraanalfast
show claraanalslow
call screen claraanalslow01x
screen claraanalslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ClaraAnalFastx") 

label ClaraAnalFastx:
cl "That's good, I'm getting used to the size... You can POUND ME FASTER NOW!"
hide claraanalslow
show claraanalfast
call screen claraanalfast01x
screen claraanalfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ClaraAnalSlowx") 

label ClaraAnalEndx:
cl "Are you going to cum [name]? I can feel your cock getting bigger..."
mc "Yes, I am, I..."
scene claraanalcum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...AM! RHAAAA!"
with fastflash
cl "Oh my, I've never been filled with so much cum in my ass in my life! There's so much of it!"
scene claraanalcum02
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Hang on, there's MORE!"
with fastflash
cl "How can you cum SO MUCH? You're a cum-pumping MACHINE!"
scene claraanalcum03 with dissolve
play sound "Sounds/panting.mp3"
cl "Ooh, you gave me a CUM enema..."
mc "The purity of my white cream will wash away your anal sins."
cl "Thanks then... I guess. I'll try and keep it in for as long as possible but it's dripping out already because you BLASTED so much spunk inside my hole..."
mc "Then we can quickly move on to the next stage of your sexual redemption. Hop on the bed."
jump ClaraFuckChoicex

