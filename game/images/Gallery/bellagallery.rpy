label BellaGallery:
call screen gallerybella
screen gallerybella:
    add "Gallery/bellagallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("gallerybella"), Jump ("MainGallery")]

    if renpy.seen_image("poolbella01"):
        imagebutton:
            focus_mask True
            idle "Gallery/bellagallery01.png" xpos 621 ypos 100
            hover "Gallery/bellagallery01.png"
            action Jump ("BellaGallery01")

    if renpy.seen_image("poolbella01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("BellaGallery")

    if renpy.seen_image("belladate01"):
        imagebutton:
            focus_mask True
            idle "Gallery/bellagallery02.png" xpos 1050 ypos 100
            hover "Gallery/bellagallery02.png"
            action Jump ("BellaGallery02")

    if renpy.seen_image("belladate01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("BellaGallery")

    if renpy.seen_image("bellalingerie01"):
        imagebutton:
            focus_mask True
            idle "Gallery/bellagallery03.png" xpos 1478 ypos 100
            hover "Gallery/bellagallery03.png"
            action Jump ("BellaGallery03")

    if renpy.seen_image("bellalingerie01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("BellaGallery")

    if renpy.seen_image("bellaset01"):
        imagebutton:
            focus_mask True
            idle "Gallery/bellagallery04.png" xpos 621 ypos 400
            hover "Gallery/bellagallery04.png"
            action Jump ("BellaGallery04")

    if renpy.seen_image("bellaset01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("BellaGallery")

    if renpy.seen_image("bellabed"):
        imagebutton:
            focus_mask True
            idle "Gallery/bellagallery05.png" xpos 1050 ypos 400
            hover "Gallery/bellagallery05.png"
            action Jump ("BellaGallery05")

    if renpy.seen_image("bellabed") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("BellaGallery")

    add "Gallery/galleryfuture.png" xpos 1478 ypos 400

    add "Gallery/galleryfuture.png" xpos 620 ypos 700

    add "Gallery/galleryfuture.png" xpos 1048 ypos 700

    add "Gallery/galleryfuture.png" xpos 1478 ypos 700

    add "Gallery/gallerygrid02.png"
    add "Gallery/textbella.png"

label BellaGallery01:
scene poolbella01
be "Oh, hello [name]. Do you like our indoor swimming pool? It's great isn't it? The water is so warm..."
scene poolbella02 with dissolve
mc "Such a fine ass..."
be "You were saying?"
scene poolbella03 with dissolve
mc "Err... nothing."
be "I'm gonna need to dry off. I hope to go on an adventure with you soon [name]!"
mc "Well, since I'm in the pool, I might as well go for a swim..."
jump BellaGallery

label BellaGallery02:
play channel1 "v07/datemusic.mp3"
scene canyon01
show belladate01
be "I'm glad we can finally be ALONE. I'm getting tired that you always bring a harem girl with you on my rig."
mc "It's for the good of the missions. Otherwise, I would definitely rather be ALONE with you, Bella..." 
hide belladate01
show belladate02
with fastdissolve
be "I'm flattered. Like, really. But you need MORE to get into MY panties..."
mc "Errr, that's why I took you to this beautiful place befitting a... err, beautiful lady such as yourself."
hide belladate02
show belladate03
with fastdissolve
be "Nice try [name]... Is the water here also befitting me?"
mc "Oh, yes! It's crystal clear, pure, refreshing and...err..."
be "So hopefully better than in the compound's underground pool? Let's go for a swim then!"
scene belladate04 with dissolve
be "Mmmh, you were right, the water really IS refreshing here..."
scene belladate05 with dissolve
be "Since I want a nice even tan, I'll remove my top, I expect that you don't mind, do you?"
mc "Of course not, be my guest! I also want an even tan so..."
scene belladate06 with dissolve
mc "* Fuck Yeah... Time to make a move. With my COCK! *"
scene belladate07 with dissolve
be "The water isn't refreshing enough for that cock of yours apparently. Maybe it's time for me to check what a Saint-Manhood looks like... UP CLOSE!"
scene belladate10 with fastdissolve
be "This cock sure is worthy of a Saint-Manhood..."
mc "And you hot bod sure is worthy of handling it!"
scene belladate11 with fastdissolve
be "But can this cock handle THIS?..."
play channel2 "Sounds/wank.mp3"
scene belladate11 with fastdissolve
pause 0.2
scene belladate12 with fastdissolve
pause 0.2
scene belladate11 with fastdissolve
pause 0.2
scene belladate12 with fastdissolve
pause 0.2
scene belladate11 with fastdissolve
pause 0.2
scene belladate12 with fastdissolve
pause 0.2
scene belladate11 with fastdissolve
pause 0.2
scene belladate12 with fastdissolve
pause 0.2
scene belladate11 with fastdissolve
pause 0.2
scene belladate12 with fastdissolve
pause 0.2
scene belladate11 with fastdissolve
pause 0.2
scene belladate12 with fastdissolve
pause 0.2
scene belladate11 with fastdissolve
pause 0.2
scene belladate12 with fastdissolve
pause 0.2
scene belladate11 with fastdissolve
pause 0.2
scene belladate12 with fastdissolve
pause 0.2
scene belladate11 with fastdissolve
pause 0.2
scene belladate12 with fastdissolve
pause 0.2
scene belladate11 with fastdissolve
pause 0.2
scene belladate12 with fastdissolve
pause 0.2
mc "Ah, fuck, you're gonna make me..."
stop channel2
scene belladate13 with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...CU-UUU-UUUM! AAAH!"
window hide
with fastflash
be "Yeah, BLAST that young cream for me!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
window hide
with fastflash
mc "God, still MORE! RHAAA!"
window hide
with fastflash
be "Damn, you keep PUMPING those hot shots everywhere!"
play sound "Sounds/panting.mp3"
scene belladate14 with fastdissolve    
be "That must have been REAL good for you.... You came sssoo much. Very impressive Saint-Manhood!"
mc "Oooh... The period just advanced, I didn't realize I came for THAT LONG. Maybe we should head back to the compound Bella..."
be "No respite for HARD working scouts like us!"
stop channel1
jump Bedroom

label BellaGallery03:
play music "v07/datemusic.mp3"
scene bedroom02
show bellalingerie01 at center with moveinright
be "Here I am! In a SEXY TOPLESS leotard."
mc "Wow. Just wow."
hide bellalingerie01
show bellalingerie02
with fastdissolve
be "I feel naughty and yet closer to the Phallus Lord when I wear it."
mc "My cock is getting closer to him too as we speak."
hide bellalingerie02
show bellalingerie03
with fastdissolve
be "Did you notice the conveniently placed holes in this leotard I'm wearing [name]?"
mc "I sure did. I'm gonna zoom in on them now if you don't mind..."
scene bedroom02 blurred
show bellalingerie03zoom
with fastdissolve
be "You must be squinting your eyes, right? I do that as a scout when I don't have my binoculars."
mc "Yeah, that's how it's done."
scene bedroom02
show bellalingerie04
with dissolve
be "It also happens to expose my buttcheeks in the most shockingly sinful way when I turn round."
mc "Let me check closer for that shock effect."
scene bedroom02 blurred
show bellalingerie04zoom
with fastdissolve
be "Is it shocking then?"
mc "Shockingly cock-hardening..."
scene bedroom02
show bellalingerie02 at farright
with dissolve
be "I think you need to come and show me your shockingly MASSIVE cock now. Let's see what the Phallus Lord has blessed you with."
window hide
show mcbellalingerie01 at left with moveinleft
mc "Seventeen God-given inches of it!"
hide bellalingerie02
show bellalingerie05 at farright
with fastdissolve
if canonized:
    mc "And a Saint-Manhood to boot!"
    be "I will sing its praises at the next Church service!"
if canonized == False:
    be "What a mighty Phallus it is!"
be "I need to kiss you under the One-Eye of the Phallus Lord for him to bless our forecoming carnal union!"
hide bellalingerie05
hide mcbellalingerie01
show mcbellalingerie02
with dissolve
play sound "Sounds/kiss.mp3"
be "And now let me feel the vigor and power of your giant teenage fuckpole... Stick it between my legs!"
mc "Alright, sounds good to me. Something new too."   
hide mcbellalingerie02
show bellaleg00 
with dissolve
be "Now let my thighs take you to the Heavenly Gates of Eternal Pleasure!"
stop music
scene bedroom02 blurred
play channel1 "Sounds/wank.mp3"
label BellaLegSlowx:
hide bellalegfast
show bellalegslow
call screen bellalegslow01x
screen bellalegslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BellaLegEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BellaLegFastx") 

label BellaLegFastx:
be "It feels like a mall ride... On your HORSECOCK instead of a poney!"
hide bellalegslow
show bellalegfast
call screen bellalegfast01x
screen bellalegfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BellaLegEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BellaLegSlowx") 

label BellaLegEndx:
be "I want you to spurt for me. Small spurts, NON-STOP, you hear me?"
hide bellalegslow
hide bellalegfast
show bellalegcum
window hide
play channel2 "Sounds/boymoan.mp3"
pause
be "That's it, just like that... And now cum for REAL!"
hide bellalegcum
show bellalegbigcum01
with fastdissolve
stop channel1
stop channel2
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
pause
mc "AAAH!"
window hide
with fastflash
be "YEAH, let it SHOOT OUT!"
hide bellalegbigcum01
show bellalegbigcum02
with fastdissolve
mc "Oh GOD!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
window hide
with fastflash
be "Praise be to the Phallus Lord, Defender of the Spunk!"
hide bellalegbigcum02
show bellalegbigcum03
with fastdissolve
be "How are you feeling now that you are relieve of your SINFUL SPUNK?"
mc "Aaaah... Sssooo much better..."
be "Good, then it is time for you to FUCK ME SENSELESS in front of the Phallus Lord! I'll hop on the bed and wait for you..."
stop music
jump BellaGallery


label BellaGallery04:
play music "v07/datemusic.mp3"
scene bedroom01 blurred with fade
show bellaset01 at center with moveinright
be "THIS is my lace lingerie outfit."
mc "I wonder where you got it from in this post-apocalyptic world?"
hide bellaset01
show bellaset02
with fastdissolve
be "I managed to save some personal stuff after the War... I wasn't always as pious as I am now..."
mc "I see. You're a wild girl deep down."
hide bellaset02
show bellaset03
with fastdissolve
be "Depends on the man. If HE's wild, I CAN be wild. Are you wild [name]?"
scene bedroom01 blurred
show bellaset03zoom
mc "What, uh? You were saying?"
be "You seem to like my tits a LOT. You're not even LISTENING anymore."
mc "Err..."
scene bedroom01
show bellaset04
with fastdissolve
be "Maybe I should turn round so you can clear your mind..."
mc "Oh..."
scene bedroom01 blurred
show bellaset04zoom
with fastdissolve
be "Can you see things more clearly now?"
mc "The background is blurry but I am totally focused now."
scene bedroom01 blurred
show bellaset05
with fastdissolve
be "That's good. So, will you be a WILD man for me?"
mc "As wild as the wildest beast in the wildest jungle!"
be "Then sit on the sofa and let me strip for you while you get that cock of yours nice and HARD for me..."
scene bedroom02 blurred
show bellaset06
with dissolve
be "Is your cock filling up with blood yet [name]?"
mc "Fuck yeah! Getting HARDER and BIGGER by the second Bella!"
hide bellaset06
show bellaset07
with fastdissolve
be "I hope THIS will hasten your tool's hardening..."
mc "Oh, it will, it will!"
hide bellaset07
show bellaset08
with fastdissolve
be "Only the bottom left to remove for you..."
hide bellaset08
show bellaset09
with fastdissolve
be "I can see this did the trick. You are FULLY HARD."
mc "And leaking precum all over the place..."
be "Then I guess I'll just have to clean your shaft and balls from that slimy mess you've made..."
mc "Let's start with my balls, they demand a warm tongue to help them churn up a BIG load."
stop music
play music "Sounds/lick.mp3"
scene mcbellasofa01 with dissolve
be "Like that? My tongue twsting and curling all over your fat bull-balls?"
mc "Yeah, just like that... Keep going..."
scene mcbellasofa02 with fastdissolve
$ renpy.pause(.3, hard=True)
scene mcbellasofa03 with fastdissolve
$ renpy.pause(.3, hard=True)
scene mcbellasofa02 with fastdissolve
$ renpy.pause(.3, hard=True)
scene mcbellasofa03 with fastdissolve
$ renpy.pause(.3, hard=True)
scene mcbellasofa02 with fastdissolve
$ renpy.pause(.3, hard=True)
scene mcbellasofa03 with fastdissolve
$ renpy.pause(.3, hard=True)
scene mcbellasofa02 with fastdissolve
$ renpy.pause(.3, hard=True)
scene mcbellasofa03 with fastdissolve
$ renpy.pause(.3, hard=True)
mc "Oh Fuck, that's good Bella! Lavish them with your spit!"
scene mcbellasofa02 with fastdissolve
$ renpy.pause(.3, hard=True)
scene mcbellasofa03 with fastdissolve
$ renpy.pause(.3, hard=True)
scene mcbellasofa02 with fastdissolve
$ renpy.pause(.3, hard=True)
scene mcbellasofa03 with fastdissolve
$ renpy.pause(.3, hard=True)
scene mcbellasofa02 with fastdissolve
$ renpy.pause(.3, hard=True)
scene mcbellasofa03 with fastdissolve
$ renpy.pause(.3, hard=True)
scene mcbellasofa02 with fastdissolve
$ renpy.pause(.3, hard=True)
scene mcbellasofa03 with fastdissolve
$ renpy.pause(.3, hard=True)
stop music
mc "And now, the shaft... It needs a DEEP cleanse. Your throat should do the trick."
play channel1 "Sounds/hardsucking.mp3"
play channel2 "Sounds/wank.mp3"
label BellaBlowSlowx:
scene bellablowslow
call screen bellablowslow01x
screen bellablowslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BellaBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BellaBlowFastx") 

label BellaBlowFastx:
mc "That throat is just sssoo DEEP and WARM! Need to pummel it FASTER!"
scene bellablowfast
call screen bellablowfast01x
screen bellablowfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BellaBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BellaBlowSlowx") 

label BellaBlowEndx:
mc "You're going to PUMP the semen out of me!"
stop channel2
stop channel1
scene bellablowcum01 with dissolve
play channel1 "v07/creampie.mp3"
play channel2 "Sounds/splooge02.mp3"
mc "Fuck YEAH!"
window hide
with fastflash
mc "Blowing NON-STOP, AAAH!"
scene bellablowcum02 with dissolve
stop channel2
stop channel1
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "The rest for you HOT BOD, RHAAA!"
window hide
with fastflash
be "Look at those plumes of boyspunk, they're so MASSIVE, I'm gonna cum too! AAAH!"
scene bellablowcum03 with dissolve
be "Watching you pump so much cum is just too much, I LOVE IT!"
window hide
with fastflash
mc "Take those last half-dozen shots, FUCK OOOOHHHH!"
scene bellablowcum04 with dissolve
play sound "Sounds/lick.mp3"
be "Mmmh, it's delicious... I hope you have some MORE for me [name]!"
mc "Don't worry Bella, I've got plenty more cum in store for you. Let's move to the bed and I'll show you..."
stop sound
stop music
scene bedroom03b
show bellabed
with dissolve
be "I'll all cleaned-up and as sinless as a newborn. So fill me up with SIN and SEMEN so I can repent!"
jump BellaGallery

label BellaGallery05:
scene bedroom03b
show bellabed
label BellaFuckChoicex:
stop music
menu:
    "I'm hungry for your bod. I want to spoon you.":
        be "Are you a cannibal or something?"
        mc "A SEX cannibal!"
        be "Well come and show me, BEAST!"
        jump BellaSpoonx
    "Ride me to Heavens and back, Bella!":
        be "I'll get closer to the Phallus Lord that way, I'm in!"
        jump BellaRidex 
    "After my outdoor adventures, I need a good rub and scrub. On my COCK!":
        be "I have an idea of what to do... Lie on your back and let me do the rubbing and scrubbing."
        jump BellaRubx
    "What's the Church's position on anal sex?":
        be "Me on my stomach while you ram your giant dong in my rosebud!"
        mc "Now I can certainly get behind that teaching... Behind, get it?"
        be "Stop making silly puns and SODOMIZE ME!"
        jump BellaAnalx
    "I'm donewith this gallery.":
        jump BellaGallery

label BellaSpoonx:
scene bellapresex01 with dissolve
mc "Let me feel you up while you frig yourself..."
play sound "Sounds/moaning.mp3"
be "Please kiss me... Before you POUND ME..."
scene bellapresex02 with dissolve
play sound "Sounds/kiss.mp3"
$ renpy.pause(1.0, hard=True)
scene bellapresex03 with dissolve
mc "So are you ready for my dong now, Bella?"
be "Yes, I'm ready to take on your MONSTERCOCK!"
play music "Sounds/womansex02.mp3"
label BellaSexSlowx:
hide bellasexfast
show bellasexslow
call screen bellasexslow01x
screen bellasexslow0x1:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BellaSexEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BellaSexFastx") 

label BellaSexFastx:
mc "Your pussy feels ssooo TIGHT around my shaft!"
be "Then pound it FASTER, that should ease its GRIP!"
hide bellasexslow
show bellasexfast
call screen bellasexfast01x
screen bellasexfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BellaSexEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BellaSexSlowx") 

label BellaSexEndx:
mc "The friction is just... TOO MUCH!"
stop music
scene bellasexcum01 with dissolve
play music "v07/creampie.mp3"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "... AND IS MAKING ME COME! AAAAH!"
window hide
with fastflash
be "Sweet Phallus Lord, I can feel your MASSIVE jets spewing inside me!"
scene bellasexcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
be "FUCK, you're FILLING ME UP!"
window hide
with fastflash
mc "RRHHHHAAAAH!"
window hide
with fastflash
be "MORE? I'm BURSTING, please PULL OUT, AAAH!"
scene bellasexcum03 with dissolve
stop sound
stop music
mc "Damn, that was pretty wild, wasn't it Bella?"
play sound "Sounds/womanmoan.mp3"
be "I'm LEAKING your warm boycum... I'm going to need to confess to Father Tyrone."
mc "Confess what?"
be "That I can't get enough of your MONSTERCOCK!"
mc "Well, I'm raring to go AGAIN anytime you are, Bella!"
scene bellabed with dissolve
be "I AM ready now, so please, GIVE ME MORE OF IT!"
jump BellaFuckChoicex
    
label BellaRidex:
scene bedroom37
show bellapreride01
with dissolve
be "Jus stand still and let me do the impaling."
mc "Fine by me Bella."
hide bellapreride01
show bellapreride02
with fastdissolve
be "Phallus Lord have mercy! I can barely get the fist-sized helmet of this pussy-destroyer inside my tender snatch..."
mc "Use my precum, there's quite a lot of it and it will lubricate my shaft."
be "Thanks for the tip [name]. I think I got it now and..."
be "LET'S GO!"
scene bedroom37 blurred
play music "Sounds/fucksound.mp3"
label BellaRideSlowx:
scene bedroom37 blurred
show bellarideslow
with fastdissolve
call screen bellarideslow01x
screen bellarideslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BellaRideEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BellaRideFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("BellaRidePOVSlowx") 

label BellaRideFastx:
scene bedroom37 blurred
show bellaridefast
with fastdissolve
call screen bellaridefast01x
screen bellaridefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BellaRideEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BellaRideSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("BellaRidePOVFastx") 

label BellaRidePOVSlowx:
scene bedroom08 blurred
show bellaridepovslow
with fastdissolve
call screen bellaridepovslow01x
screen bellaridepovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BellaRideEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BellaRidePOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("BellaRideSlowx") 

label BellaRidePOVFastx:
scene bedroom08 blurred
show bellaridepovfast
with fastdissolve
call screen bellaridepovfast01x
screen bellaridepovfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BellaRideEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BellaRidePOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("BellaRideFastx") 
        
label BellaRideEndx:
mc "You're driving me over the edge, Bella!"
be "Then go ahead and DUMP YOUR LOAD INSIDE ME!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene bedroom37 blurred
show bellaridecum01
with dissolve
be "That feels sssoo GOOD, you're PUMPING me full of your scalding seed!"
window hide
with fastflash
mc "Here are some more shots for you Bella, RHAAA!"
be "Let me pull this CUM-CANNON out of my filed-up pussy and see how much scum you have left to BLOW!"
hide bellaridecum01
show bellaridecum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
be "As expected, you're still SHOOTING MONSTER CUMSHOTS!"
window hide
with fastflash
mc "OOOOH, AAAH!"
hide bellaridecum02
show bellaridecum03
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
be "They're even growing BIGGER! Where do you store THAT MUCH SPUNK?"
window hide
with fastflash
mc "DAMN, AAAH, I... OOOOH!"
window hide
with fastflash
be "You're covering me in warm boycum you BEAST! And yourself too by the looks of it..."
scene bellaridecum04 with dissolve
play sound "Sounds/panting.mp3"
be "Finally, it stopped. After at least TWO DOZENS MEGA-SHOTS... Wow, now that was a MESSY spunk explosion..."
mc "Aaahhh...."
be "Come on, I want some MORE SEX. Show me that you can get it up again, STUD!"
mc "S...Sure... Just give me a few seconds to recover."
be "I'll be waiting on the bed then..."
scene bellabed with dissolve
be "Like so..."
jump BellaFuckChoicex
    
label BellaRubx:
scene bellaprerub01 with dissolve
be "Let's just place that teenage monstercock right here... Next to my wet pussy!"
mc "Oh God, what... What are you going to do?..."
be "THIS!"
play music "Sounds/wank.mp3"
label BellaRubSlowx:
scene bellarubslow with fastdissolve
call screen bellarubslow01x
screen bellarubslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BellaRubEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BellaRubFastx") 

label BellaRubFastx:
be "You like it when I rub my pussy on your fuckstick like that, don't you [name]?"
mc "Y... yeah, please do it FASTER now!"
scene bellarubfast with fastdissolve
call screen bellarubfast01x
screen bellarubfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BellaRubEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BellaRubSlowx") 

label BellaRubEndx:
be "Oooh, I can feel you getting ready for a mighty EXPLOSION of young cum!"
scene bellarubcum01 with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "... Can't hold it, AAAH!"
window hide 
with fastflash
be "Keep blowing that nut, I need a LOT of lotion if you want a CLEAN cock!"
scene bellarubcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "There, for you Bella, RHAAA!"
window hide 
with fastflash
be "Now we're talking, MASSIVE jets of boyspunk everywhere!"
scene bellarubcum03 with dissolve
play sound "Sounds/lick.mp3"
be "Sssoo tasty... But your cock is not CLEAN enough. Your balls need to empty their DIRTY load once MORE!"
mc "Wh... Hang on, I just came and..."
stop sound
scene bellafoot00 with dissolve
be "Shush... Look at you, you're still ROCKHARD! You know you need to RELIEVE yourself AGAIN!"
label BellaFootSlowx:
play music "Sounds/wank.mp3"
show bellafootslow with fastdissolve
call screen bellafootslow01x
screen bellafootslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BellaFootEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BellaFootFastx") 

label BellaFootFastx:
be "Look at all that filthy prespunk dribbling from your cumhole... It makes your cock all wet and slippery. Perfect for a good clean rub!"
mc "AAAH, your feet are so good on my shaft...."
show bellafootfast with fastdissolve
call screen bellafootfast01x
screen bellafootfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BellaFootEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BellaFootSlowx") 

label BellaFootEndx:
mc "You're gonna make me... CUM AGAIN!"
stop music
scene bellafootcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH, that's it, NEED TO BLOW ONCE MORE!"
window hide 
with fastflash
be "YES, you need to EMPTY your balls this time, RELEASE EVERYTHING!"
scene bellafootcum02 with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
be "Look at you cumming like a STALLION... AGAIN!"
window hide 
with fastflash
mc "Can't stop blowing, your feet are sssooo good, RHAAA!"
scene bellafootcum03 with fastdissolve
play sound "SOunds/panting.mp3"
be "Mmmh, your sperm is just... DIVINE..."
mc "Slurp it all up, I've got some MORE in store for you!"
scene bellabed with dissolve
be "And what would that be exactly?"
jump BellaFuckChoicex
    
label BellaAnalx:
scene bedroom20
show bellapreanal01
with dissolve
be "I'm assuming the position of the submissive and repentful woman who is prepared to wash away the sins of the w...."
hide bellapreanal01
show bellapreanal02
with fastdissolve
play sound "Sounds/womanscream.ogg"
be "...OUCH!"
mc "Enough talking, let's do some anal-fucking!"
be "Yes, go ahead and don't be gentle, I deserve it, I'm a sinful wom..."
hide bellapreanal02
show bellapreanal03
with fastdissolve
play sound "Sounds/womanscream.ogg"
mc "There, that should shut you up Bella!"
be "UUUR... It hurts but I deserve it..."
play music "Sounds/fucksound.mp3"
label BellaAnalSlowx:
scene bellaanalslow
call screen bellaanalslow01x
screen bellaanalslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BellaAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BellaAnalFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("BellaAnalSideSlowx") 

label BellaAnalFastx:
be "Pound me HARDER and FASTER, plough the sin out of my ass!"
scene bellaanalfast
call screen bellaanalfast01x
screen bellaanalfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BellaAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BellaAnalSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("BellaAnalSideFastx") 

label BellaAnalSideSlowx:
scene bellaanalsideslow
call screen bellaanalsideslow01x
screen bellaanalsideslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BellaAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BellaAnalSideFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("BellaAnalSlowx") 

label BellaAnalSideFastx:
be "Pound me HARDER and FASTER, plough the sin out of my ass!"
scene bellaanalsidefast
call screen bellaanalsidefast01x
screen bellaanalsidefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BellaAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BellaAnalSideSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("BellaAnalFastx") 
        
label BellaAnalEndx:
be "Fulfill the Phallus Lord's 69th commandment and CUM INSIDE MY BACKDOOR!"
scene bedroom14 blurred
show bellaanalcum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "I AM NOW! RHAAAA!"
window hide
with fastflash
be "I can feel it, I can feel my sins being washed away in a TIDE OF YOUNG CUM! AAAH!"
hide bellaanalcum01
show bellaanalcum02
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "The tide is retreating, OUT OF YOUR ASSHOLE!"
window hide
with fastflash
be "...In great waves of white spunk, OOOOH! There's so much of it!"
scene bedroom32 blurred
show bellaanalcum03
play sound "Sounds/moaning.mp3"
be "My poor ass... You destroyed it... I won't be able to sit straight for a week."
mc "Then you'll kneel instead next time you pray, it's win-win situation really."
be "Oooh..."
scene bellabed with dissolve
be "I've recovered. Barely. And I'm ready for you, STUD!"
jump BellaFuckChoicex
jump BellaGallery