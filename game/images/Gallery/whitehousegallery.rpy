label WhiteHouseGallery:
stop music
call screen gallerywhitehouse
screen gallerywhitehouse:
    add "v10/whitehousegallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("whitehousegallery"), Jump ("MainGallery")]

    if renpy.seen_image("kimwhmegacum01"):
        imagebutton:
            focus_mask True
            idle "Gallery/whitehousegallery01.png" xpos 621 ypos 100
            hover "Gallery/whitehousegallery01.png"
            action Jump ("WhitehouseGallery01")

    if renpy.seen_image("kimwhmegacum01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("WhitehouseGallery")

    if renpy.seen_image("whbothend01"):
        imagebutton:
            focus_mask True
            idle "Gallery/whitehousegallery02.png" xpos 1050 ypos 100
            hover "Gallery/whitehousegallery02.png"
            action Jump ("WhitehouseGallery02")

    if renpy.seen_image("whbothend01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("WhitehouseGallery")

    if renpy.seen_image("newovaloffice01"):
        imagebutton:
            focus_mask True
            idle "Gallery/whitehousegallery03.png" xpos 1478 ypos 100
            hover "Gallery/whitehousegallery03.png"
            action Jump ("WhitehouseGallery03")

    if renpy.seen_image("newovaloffice01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("WhiteHouseGallery")

    if renpy.seen_image("newovaloffice01"):
        imagebutton:
            focus_mask True
            idle "Gallery/whitehousegallery04.png" xpos 621 ypos 400
            hover "Gallery/whitehousegallery04.png"
            action Jump ("WhitehouseGallery04")

    if renpy.seen_image("newovaloffice01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("WhiteHouseGallery")

    add "Gallery/gallerygrid03.png"
    add "v10/textwhitehouse.png"

label WhitehouseGallery01:
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
call screen kimhandjobslowx
screen kimhandjobslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("KimHandjobFastx") 

label KimHandjobFastx:
kg "And now, I'll go even FASTER, for the KILL!"
mc "I can take it, I'm a trained... wanker! Just like your boss."
kg "DO NOT MOCK OUR BELOVED CULT LEADER!"
hide kimwankslow
show kimwankfast
call screen kimhandjobfastx
screen kimhandjobfastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KimHandjobEndx")

label KimHandjobEndx:
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
label KimFuckSlowx:
show kimfuckslow
call screen kimfuckslowx
screen kimfuckslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("KimFuckFastx") 

label KimFuckFastx:
kg "I'VE BEEN TOO KIND SO FAR, NOW YOU WILL FEEL MY PUSSY MUSCLES CLAMPING DOWN... HARD!!!!"
mc "Do... your... worst... I can take it... AAAH."
kg "WE'LL SEE ABOUT THAT!"
hide kimfuckslow
show kimfuckfast
call screen kimfuckfastx
screen kimfuckfastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KimFuckEndx")

label KimFuckEndx:
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
jump WhiteHouseGallery


label WhitehouseGallery02:
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
        jump MelaniaHouseFuckx
    "Ivanka":
        mc "Muscles galore for my BIG MUSCLE first!"
        jump IvankaHouseFuckx

label MelaniaHouseFuckx:
stop music
scene whivankacumbackgroundzoom
show whmelaniaprefuck
with dissolve
mc "Ready First Lady?"
play sound "Sounds/moaning.mp3"
me "Mmmh, YES I AM!"
label MelaniaHouseFuckbx:
stop music
play music "Sounds/womansex01.mp3"
scene whdoggymelaniabackground blurred
label MelaniaHouseSlowx:
hide melaniawhdoggyfast
show melaniawhdoggyslow
call screen melaniawhfuckslow01x
screen melaniawhfuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("MelaniaHouseEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MelaniaHouseFastx") 
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("IvankaHouseSwitchx") 

label MelaniaHouseFastx:
if melaniadeepx:
    mc "I'm the FIRST man that DEEP inside the First Lady! Fuck Yeah!"
if melaniadeepx == False:
    mc "You love that cock, don't you Melania?"
    me "YES, I LOVE IT, I admit it, just shut up and FUCK MY DIRTY HOLE HARDER!"
    $ melaniadeepx = True
hide melaniawhdoggyslow
show melaniawhdoggyfast
call screen melaniawhfuckfast01x
screen melaniawhfuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("MelaniaHouseEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MelaniaHouseSlowx")
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("IvankaHouseSwitchx") 
        
label MelaniaHouseEndx:
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
    jump WhbothfuckEndx
if ivankaloadx == False:
    mc "Don't you worry, I've got enough cum left for YOUR PUSSY!"
    iv "Please, fuck me, I'm dying to feel that GIANT shaft STRETCHING my hole..."
    jump IvankaHouseFuckx

label IvankaHouseSwitchx:
mc "Gonna switch before I cum inside that tight hole, aaah... Get ready Ivanka!"
jump IvankaHouseFuckbx

label IvankaHouseFuckx:
stop music
scene whivankacumbackgroundzoom
show whivankaprefuck
with dissolve
mc "Ready Ivanka?"
play sound "Sounds/moaning.mp3"
iv "Always ready for a big fat teenage MONSTERCOCK!"
label IvankaHouseFuckbx:
stop music
play music "Sounds/womansex02.mp3"
label IvankaHouseSlowx:
scene whdoggyivankabackground blurred
show ivankawhfuckslow
call screen ivankawhfuckslow01x
screen ivankawhfuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("IvankaHouseEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("IvankaHouseFastx") 
    imagebutton:
        focus_mask True
        idle "v071/topview.png"
        hover "v071/topview.png"
        action Jump ("IvankaHouseTopSlowx") 
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("MelaniaHouseSwitchx") 
 
label IvankaHouseFastx:
if ivankadeepx:
    mc "Gonna POUND that presidential-family fuckhole HARDER and FASTER!"
if ivankadeepx == False:
    mc "Am I DEEP enough inside your pussy Ivanka?"
    iv "Oooh, YES! But go faster please, fuck me HARD, make me CUM!"
    $ ivankadeepx = True
scene whdoggyivankabackground
show ivankawhfuckfast
call screen ivankawhfuckfast01x
screen ivankawhfuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("IvankaHouseEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("IvankaHouseSlowx")
    imagebutton:
        focus_mask True
        idle "v071/topview.png"
        hover "v071/topview.png"
        action Jump ("IvankaHouseTopFastx") 
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("MelaniaHouseSwitchx") 

label IvankaHouseTopSlowx:
scene whdoggyivankatopbackground
show ivankatopwhfuckslow
call screen ivankawhfucktopslow01x
screen ivankawhfucktopslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("IvankaHouseEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("IvankaHouseTopFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("IvankaHouseSlowx") 
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("MelaniaHouseSwitchx") 

label IvankaHouseTopFastx:
if ivankadeepx:
    mc "Gonna POUND that presidential-family fuckhole HARDER and FASTER!"
if ivankadeepx == False:
    mc "Am I DEEP enough inside your pussy Ivanka?"
    iv "Oooh, YES! But go faster please, fuck me HARD, make me CUM!"
    $ ivankadeepx = True
scene whdoggyivankatopbackground
show ivankatopwhfuckfast
call screen ivankawhfucktopfast01x
screen ivankawhfucktopfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("IvankaHouseEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("IvankaHouseTopSlowx")
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("IvankaHouseFastx") 
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("MelaniaHouseSwitchx") 

label IvankaHouseEndx:
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
    jump WhbothfuckEndx
if melanialoadx == False:
    mc "Don't you worry, I've got enough cum left for YOUR PUSSY!"
    iv "Please, fuck me, I'm dying to feel that GIANT shaft STRETCHING my hole..."
    jump IvankaHouseFuckx

label MelaniaHouseSwitchx:
mc "Time to switch girls, this cock needs more than one pussy to make it come. Spread your legs wide open Melania!"
jump MelaniaHouseFuckbx

label WhbothfuckEndx:
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
jump WhiteHouseGallery

label WhitehouseGallery03:
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
label MelaniaIvankaBlowSlowx:
hide melaniaivankablowfast
show melaniaivankablowslow
call screen melaniaivankablowslow01x
screen melaniaivankablowslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MelaniaIvankaBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MelaniaIvankaBlowFastx") 

label MelaniaIvankaBlowFastx:
hide melaniaivankablowslow
show melaniaivankablowfast
mc "You're getting my juices going, girls..."
me "We'll make them go FASTER then!"
call screen melaniaivankablowfast01x
screen melaniaivankablowfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MelaniaIvankaBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MelaniaIvankaBlowSlowx")

label MelaniaIvankaBlowEndx:
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
mc "And now, BRING ON THE GIRLS FOR THE FINAL ORGY! Each one in  turn, cos this is the Gallery Replay and I want to FUCK ALL OF THEM!"
stop channel1
jump WhiteHouseGallery

label WhitehouseGallery04:
stop music
play music "v10/ohyeah.mp3"
show screen endallx
screen endallx:
    imagebutton idle "v10/endall.png" hover "v10/endall.png" xpos 1800 ypos 20 focus_mask True action Jump ("WhiteHouseGallery") 
$ endstartx = True
label EndFuckx:
scene newovaloffice01
$ drollmcsetup=renpy.random.randint(1,3)
$ drolltrumpfsetup=renpy.random.randint(1,3)
$ drolltrumpfsex=renpy.random.randint(1,3)
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
if drollmcsetup == 1:
    show mcsetup01a
if drollmcsetup == 2:
    show mcsetup03
if drollmcsetup == 3:
    show mcsetup04
if endstartx:
    hide mcsetup04
    hide mcsetup03
    hide mcsetup01a
    show mcsetup01b
    $ endstartx = False

label Winnancyfuckx:
show orgynancysetup at farleft02
mc "FUCK YEAH, NANCY! {w=1.0}{nw}"
window hide
show orgynancysetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgynancysetup at left
with dissolve
mo "Only the BEST for that MONSTERCOCK, sweetie pie... {w=2.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex01.mp3"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-705
        show winnancyfuck
    if drolltrumpfsex == 2:
        show winnancyfuck
        show winmelaniaivanka02-705
    if drolltrumpfsex == 3:
        show winnancyfuck
        show winmelaniaivanka03-705
    $ renpy.pause(.705, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-705
    show orgynancycum
if drolltrumpfsex == 2:
    show orgynancycum
    show winmelaniaivanka02-705
if drolltrumpfsex == 3:
    show orgynancycum
    show winmelaniaivanka03-705
with dissolve
mc "CUMMING IN YOUR ASS, AAAH! {w=1.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
mo "Oh God, my dear boy, you're PUMPING ME FULL, AAAH! {w=2.0}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgynancyleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgynancyleave with moveoutright

label Winlenafuckx:
show orgylenasetup at farleft02
mc "Lena! I'm the BIG chief now, so come over here... {w=1.5}{nw}"
window hide
show orgylenasetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgylenasetup at left
with dissolve
le "This cock DESERVES to be worshipped... {w=1.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex01.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-79
        show winlenafuck
    if drolltrumpfsex == 2:
        show winlenafuck
        show winmelaniaivanka02-79
    if drolltrumpfsex == 3:
        show winlenafuck
        show winmelaniaivanka03-79
    $ renpy.pause(.79, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-79
    show orgylenacum
if drolltrumpfsex == 2:
    show orgylenacum
    show winmelaniaivanka02-79
if drolltrumpfsex == 3:
    show orgylenacum
    show winmelaniaivanka03-79
with dissolve
mc "And now worship THAT, my FAT LOAD in your pussy, AAAH! {w=2.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
le "Mmmmh, you came sssoo much, that was a PRESIDENTIAL LOAD [name]! {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgylenaleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgylenaleave with moveoutright       

label Winamyfuckx:
show orgyamysetup at farleft02
mc "BOOYAH, It's muscle girl Amy! {w=1.5}{nw}"
window hide
show orgyamysetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgyamysetup at left
with dissolve
am "And my ass is going to deal with that HUGE MUSCLE of yours! {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex01.mp3"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-705
        show winamyfuck
    if drolltrumpfsex == 2:
        show winamyfuck
        show winmelaniaivanka02-705
    if drolltrumpfsex == 3:
        show winamyfuck
        show winmelaniaivanka03-705
    $ renpy.pause(.705, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-705
    show orgyamycum
if drolltrumpfsex == 2:
    show orgyamycum
    show winmelaniaivanka02-705
if drolltrumpfsex == 3:
    show orgyamycum
    show winmelaniaivanka03-705
with dissolve
mc "YOUR TIGHT ASS IS MAKING ME NU-UU-UUT! {w=1.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
am "FILL IT UP, I WANT ALL THAT CUM! {w=2.0}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgyamyleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgyamyleave with moveoutright       

label Wincyrlfuckx:
show orgycyrlsetup at farleft02
mc "SEXY CYBORG CYRL! YEAH! {w=1.0}{nw}"
window hide
show orgycyrlsetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgycyrlsetup at left
with dissolve
cy "Activate mouth enlargement. MAXIMAL SIZE FOR THE PRESIDENTIAL DONKEY-DICK! {w=3.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/blowjob.ogg"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-705
        show wincyrlfuck
    if drolltrumpfsex == 2:
        show wincyrlfuck
        show winmelaniaivanka02-705
    if drolltrumpfsex == 3:
        show wincyrlfuck
        show winmelaniaivanka03-705
    $ renpy.pause(.705, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-705
    show orgycyrlcum
if drolltrumpfsex == 2:
    show orgycyrlcum
    show winmelaniaivanka02-705
if drolltrumpfsex == 3:
    show orgycyrlcum
    show winmelaniaivanka03-705
with dissolve
mc "BLOWING MY SEED INSIDE A ROBOT MOUTH, RHAAA! {w=2.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
cy "Fortunately, my stomach has a CUM CAPACITY of over a GALLON! {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgycyrlleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgycyrlleave with moveoutright  

label Winsukifuckx:
show orgysukisetup at farleft02
mc "Suki! I'll show you I'm an inclusive prez... {w=1.5}{nw}"
window hide
show orgysukisetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgysukisetup at left
with dissolve
su "By inserting your GIANT TEENAGE COCK inside of me I presume? {w=2.5}{nw}"
mc "CORRECTOMUNDO! {w=1.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex01.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-79
        show winsukifuck
    if drolltrumpfsex == 2:
        show winsukifuck
        show winmelaniaivanka02-79
    if drolltrumpfsex == 3:
        show winsukifuck
        show winmelaniaivanka03-79
    $ renpy.pause(.79, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-79
    show orgysukicum
if drolltrumpfsex == 2:
    show orgysukicum
    show winmelaniaivanka02-79
if drolltrumpfsex == 3:
    show orgysukicum
    show winmelaniaivanka03-79
with dissolve
mc "I've got a BIG LOAD FOR YOU SUKI, AAAH! {w=2.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
su "It sure is HUGE, I can FEEL IT! {w=1.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgysukileave at centerright
with dissolve
mc "I NEED MORE SEX, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgysukileave with moveoutright        

label Winmichikofuckx:
show orgymichikosetup at farleft02
mc "Big-Busted Asian babe Michiko! {w=1.5}{nw}"
window hide
show orgymichikosetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgymichikosetup at left
with dissolve
mi "And my Asian ASS demands some ANAL POUNDING! {w=2.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex01.mp3"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-705
        show winmichikofuck
    if drolltrumpfsex == 2:
        show winmichikofuck
        show winmelaniaivanka02-705
    if drolltrumpfsex == 3:
        show winmichikofuck
        show winmelaniaivanka03-705
    $ renpy.pause(.705, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-705
    show orgymichikocum
if drolltrumpfsex == 2:
    show orgymichikocum
    show winmelaniaivanka02-705
if drolltrumpfsex == 3:
    show orgymichikocum
    show winmelaniaivanka03-705
with dissolve
mc "ONE FAT LOAD OF TEENAGE CREAM COMING YOUR WAY, RHAAA! {w=2.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
mi "You're so BRUTAL when you UNLOAD YOUR SEED IN ME, AAAH! {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgymichikoleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgymichikoleave with moveoutright        

label Winbarbarafuckx:
show orgybarbarasetup at farleft02
mc "Barbara! It's recess so come over here... {w=1.0}{nw}"
window hide
show orgybarbarasetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgybarbarasetup at left
with dissolve
ba "And recess is for PLAYING and FUN! {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex01.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-95
        show winbarbarafuck
    if drolltrumpfsex == 2:
        show winbarbarafuck
        show winmelaniaivanka02-95
    if drolltrumpfsex == 3:
        show winbarbarafuck
        show winmelaniaivanka03-95
    $ renpy.pause(.95, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-95
    show orgybarbaracum
if drolltrumpfsex == 2:
    show orgybarbaracum
    show winmelaniaivanka02-95
if drolltrumpfsex == 3:
    show orgybarbaracum
    show winmelaniaivanka03-95
with dissolve
mc "Here, take that and have fun with my MONSTERLOAD, RHAAA! {w=1.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
ba "I'll keep it to snack on later on, OOOH! {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgybarbaraleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgybarbaraleave with moveoutright        

label Winangiefuckx:
show orgyangiesetup at farleft02
mc "ANGIE! come here sweetie... {w=1.0}{nw}"
window hide
show orgyangiesetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgyangiesetup at left
with dissolve
an "I've been waiting for a long time to FEEL that HUGE COCK again! {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex01.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-95
        show winangiefuck
    if drolltrumpfsex == 2:
        show winangiefuck
        show winmelaniaivanka02-95
    if drolltrumpfsex == 3:
        show winangiefuck
        show winmelaniaivanka03-95
    $ renpy.pause(.95, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-95
    show orgyangiecum
if drolltrumpfsex == 2:
    show orgyangiecum
    show winmelaniaivanka02-95
if drolltrumpfsex == 3:
    show orgyangiecum
    show winmelaniaivanka03-95
with dissolve
mc "I'm gonna DROWN your womb, RHAAA!{w=1.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
an "I can feel your giant JOYSTICK convulsing inside me, AAAH! {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgyangieleave at centerright
with dissolve
mc "I NEED MORE SEX, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgyangieleave with moveoutright       

label Winaylafuckx:
show orgyaylasetup at farleft02
mc "Ayla! Little girl, deep pussy... {w=1.0}{nw}"
window hide
show orgyaylasetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgyaylasetup at left
with dissolve
ay "I'm gonna show you exactly how DEEP it is... {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex02.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-95
        show winaylafuck
    if drolltrumpfsex == 2:
        show winaylafuck
        show winmelaniaivanka02-95
    if drolltrumpfsex == 3:
        show winaylafuck
        show winmelaniaivanka03-95
    $ renpy.pause(.95, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-95
    show orgyaylacum
if drolltrumpfsex == 2:
    show orgyaylacum
    show winmelaniaivanka02-95
if drolltrumpfsex == 3:
    show orgyaylacum
    show winmelaniaivanka03-95
with dissolve
mc "I'm gonna FILL your tiny womb with my SPUNK, RHAAA!{w=2.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
ay "And my SUPER-DEEP pussy can TAKE IT, AAAH {w=2.0}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgyaylaleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgyaylaleave with moveoutright        

label Winbellafuckx:
show orgybellasetup at farleft02
mc "Fuck yeah, Bella! {w=1.0}{nw}"
window hide
show orgybellasetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgybellasetup at left
with dissolve
be "May my pussy give much pleasure to that HOLY GIANT PRESIDENTIAL PHALLUS! {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex02.mp3"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-6
        show winbellafuck
    if drolltrumpfsex == 2:
        show winbellafuck
        show winmelaniaivanka02-6
    if drolltrumpfsex == 3:
        show winbellafuck
        show winmelaniaivanka03-6
    $ renpy.pause(.6, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-6
    show orgybellacum
if drolltrumpfsex == 2:
    show orgybellacum
    show winmelaniaivanka02-6
if drolltrumpfsex == 3:
    show orgybellacum
    show winmelaniaivanka03-6
with dissolve
mc "Take my MONSTER CUMSHOTS Bella, RHAAA!{w=1.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
be "PRAISE OUR CUM-LADEN PREZ! AAAAH!{w=1.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgybellaleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgybellaleave with moveoutright        

label Winpennyfuckx:
show orgypennysetup at farleft02
mc "One of my FAVORITE scouts, PENNY! {w=1.5}{nw}"
window hide
show orgypennysetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgypennysetup at left
with dissolve
pe "And I'll show you how my TITS definitely ARE your FAVORITES! {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/wank.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-74
        show winpennyfuck
    if drolltrumpfsex == 2:
        show winpennyfuck
        show winmelaniaivanka02-74
    if drolltrumpfsex == 3:
        show winpennyfuck
        show winmelaniaivanka03-74
    $ renpy.pause(.74, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-74
    show orgypennycum
if drolltrumpfsex == 2:
    show orgypennycum
    show winmelaniaivanka02-74
if drolltrumpfsex == 3:
    show orgypennycum
    show winmelaniaivanka03-74
with dissolve
mc "Your funbags are making me BL-OOO-OOOW! AAH!{w=2.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
pe "Let it RAIN, President [name]! {w=1.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgypennyleave at centerright
mc "I NEED MORE SEX, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgypennyleave with moveoutright

label Wintarafuckx:
show orgytarasetup at farleft02
mc "Tara?! I thought you were a lesbian. {w=1.5}{nw}"
window hide
show orgytarasetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgytarasetup at left
with dissolve
ta "I'm a DEEP STATE lez and you're the DEEP STATE Prez! So probe my ass REAL DEEP! {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex02.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-74
        show wintarafuck
    if drolltrumpfsex == 2:
        show wintarafuck
        show winmelaniaivanka02-74
    if drolltrumpfsex == 3:
        show wintarafuck
        show winmelaniaivanka03-74
    $ renpy.pause(.74, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-74
    show orgytaracum
if drolltrumpfsex == 2:
    show orgytaracum
    show winmelaniaivanka02-74
if drolltrumpfsex == 3:
    show orgytaracum
    show winmelaniaivanka03-74
with dissolve
mc "Can a dildo do that, CUM MASSIVE ROPES OF SEMEN INSIDE YOU, RHAAA!{w=2.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
ta "I'm liking this, I might turn STRAIGHT, AAAHH!{w=2.0}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgytaraleave at centerright
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgytaraleave with moveoutright      

label Windebrafuckx:
show orgydebrasetup at farleft02
mc "Ooh yeah, Debra! {w=1.0}{nw}"
window hide
show orgydebrasetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgydebrasetup at left
with dissolve
de "I can't wait to get fucked by your MONSTERCOCK!{w=2.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex02.mp3"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-6
        show windebrafuck
    if drolltrumpfsex == 2:
        show windebrafuck
        show winmelaniaivanka02-6
    if drolltrumpfsex == 3:
        show windebrafuck
        show winmelaniaivanka03-6
    $ renpy.pause(.705, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-6
    show orgydebracum
if drolltrumpfsex == 2:
    show orgydebracum
    show winmelaniaivanka02-6
if drolltrumpfsex == 3:
    show orgydebracum
    show winmelaniaivanka03-6
with dissolve
mc "Take my MONSTER CUMSHOTS Debra, RHAAA! {w=1.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
de "FUCK, you're FILLING ME UP WITH SO MUCH CUM!{w=2.0}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgydebraleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgydebraleave with moveoutright       

label Winrubyfuckx:
show orgyrubysetup at farleft02
mc "PUMPED-UP MUSCLE BABE RUBY, YEE-HAW! {w=2.0}{nw}"
window hide
show orgyrubysetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgyrubysetup at left
with dissolve
ru "And my TIT MUSCLES are ESPECIALLY pumped up. TO PUMP YOUR POLE! {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/wank.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-74
        show winrubyfuck
    if drolltrumpfsex == 2:
        show winrubyfuck
        show winmelaniaivanka02-74
    if drolltrumpfsex == 3:
        show winrubyfuck
        show winmelaniaivanka03-74
    $ renpy.pause(.74, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-74
    show orgyrubycum
if drolltrumpfsex == 2:
    show orgyrubycum
    show winmelaniaivanka02-74
if drolltrumpfsex == 3:
    show orgyrubycum
    show winmelaniaivanka03-74
with dissolve
mc "GODAMMIT, I'm BLOWING A MONSTER LOAD, AAAH! {w=2.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
ru "My tits did the JOB. The TITJOB! {w=1.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgyrubyleave at centerright
with dissolve
mc "I NEED MORE SEX, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgyrubyleave with moveoutright       

label Winlauriefuckx:
show orgylauriesetup at farleft02
mc "Hey, LAURIE's coming for a PRESIDENTIAL SEX VISIT! {w=2.0}{nw}"
window hide
show orgylauriesetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgylauriesetup at left
with dissolve
la "And my tits are ready to SERVICE your MEATY POLE, President! {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/wank.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-74
        show winlauriefuck
    if drolltrumpfsex == 2:
        show winlauriefuck
        show winmelaniaivanka02-74
    if drolltrumpfsex == 3:
        show winlauriefuck
        show winmelaniaivanka03-74
    $ renpy.pause(.74, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-74
    show orgylauriecum
if drolltrumpfsex == 2:
    show orgylauriecum
    show winmelaniaivanka02-74
if drolltrumpfsex == 3:
    show orgylauriecum
    show winmelaniaivanka03-74
with dissolve
mc "You're servicing me so WELL, I'm NU-UUU-TTING BIG TIME!!! {w=2.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
la "I'm glad I could be of service to your PRESIDENTIAL SCEPTER! {w=2.0}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgylaurieleave at centerright
with dissolve
mc "I NEED MORE SEX, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgylaurieleave with moveoutright       

label Winmarniefuckx:
show orgymarniesetup at farleft02
mc "WOO-HOO, Marnie! {w=1.0}{nw}"
window hide
show orgymarniesetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgymarniesetup at left
with dissolve
ma "I want you to POUND my pussy real GOOD, President [name]! {w=2.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/womansex02.mp3"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-6
        show winmarniefuck
    if drolltrumpfsex == 2:
        show winmarniefuck
        show winmelaniaivanka02-6
    if drolltrumpfsex == 3:
        show winmarniefuck
        show winmelaniaivanka03-6
    $ renpy.pause(.6, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-6
    show orgymarniecum
if drolltrumpfsex == 2:
    show orgymarniecum
    show winmelaniaivanka02-6
if drolltrumpfsex == 3:
    show orgymarniecum
    show winmelaniaivanka03-6
with dissolve
mc "Here's some MONSTER CUMSHOTS FOR YOU, RHAAA!{w=1.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
ma "AAAH! You're PUMPING sssoo MUCH SEED IN ME! {w=2.0}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgymarnieleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgymarnieleave with moveoutright       

label Winzarafuckx:
show orgyzarasetup at farleft02
mc "Damn, it's none other than ZARA! {w=1.5}{nw}"
window hide
show orgyzarasetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgyzarasetup at left
with dissolve
za "Yes it's ME, Master President. Ready to report for SEX DUTY! {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/barbarasex.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-74
        show winzarafuck
    if drolltrumpfsex == 2:
        show winzarafuck
        show winmelaniaivanka02-74
    if drolltrumpfsex == 3:
        show winzarafuck
        show winmelaniaivanka03-74
    $ renpy.pause(.74, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-74
    show orgyzaracum
if drolltrumpfsex == 2:
    show orgyzaracum
    show winmelaniaivanka02-74
if drolltrumpfsex == 3:
    show orgyzaracum
    show winmelaniaivanka03-74
with dissolve
mc "And now your DUTY is to TAKE MY CUMLOAD, AAAH!!{w=2.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
za "AAAH! I will obey and let you dump your MONSTERLOAD inside me! {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgyzaraleave at centerright
with dissolve
mc "I NEED MORE SEX, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgyzaraleave with moveoutright      

label Winclarafuckx:
show orgyclarasetup at farleft02
mc "OOH YEAH, CLARA! {w=1.0}{nw}"
window hide
show orgyclarasetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgyclarasetup at left
with dissolve
cl "Let us pray. That your GIANT TEENAGE COCK FITS INSIDE MY SINFUL MOUTHHOLE! {w=3.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/blowjob.ogg"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-705
        show winclarafuck
    if drolltrumpfsex == 2:
        show winclarafuck
        show winmelaniaivanka02-705
    if drolltrumpfsex == 3:
        show winclarafuck
        show winmelaniaivanka03-705
    $ renpy.pause(.705, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-705
    show orgyclaracum
if drolltrumpfsex == 2:
    show orgyclaracum
    show winmelaniaivanka02-705
if drolltrumpfsex == 3:
    show orgyclaracum
    show winmelaniaivanka03-705
with dissolve
mc "Ramming it in DEEP... AND CUMMING! {w=1.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
cl "YES! WASH AWAY MY SINS WITH YOUR MANLY SPUNK! {w=2.0}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgyclaraleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgyclaraleave with moveoutright       

label Wingwenfuckx:
show orgygwensetup at farleft02
mc "Gwen! Naughty girl... {w=1.0}{nw}"
window hide
show orgygwensetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgygwensetup at left
with dissolve
gw "You want naughty? I'll show you NAUGHTY! {w=2.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/barbarasex.mp3"
$ count = 10
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-79
        show wingwenfuck
    if drolltrumpfsex == 2:
        show wingwenfuck
        show winmelaniaivanka02-79
    if drolltrumpfsex == 3:
        show wingwenfuck
        show winmelaniaivanka03-79
    $ renpy.pause(.79, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-79
    show orgygwencum
if drolltrumpfsex == 2:
    show orgygwencum
    show winmelaniaivanka02-79
if drolltrumpfsex == 3:
    show orgygwencum
    show winmelaniaivanka03-79
with dissolve
mc "Take my NAUGHTY CUM, RHAAA! {w=1.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
gw "Damn [name], your balls really were FULL, weren't they? {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgygwenleave at centerright
with dissolve
mc "I NEED MORE SEX, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgygwenleave with moveoutright

label Winrachelfuckx:
show orgyrachelsetup at farleft02
mc "ULTRA-BUSTY NURSE RACHEL! {w=1.0}{nw}"
window hide
show orgyrachelsetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgyrachelsetup at left
with dissolve
ra "I must make sure our President stays HEALTHY and ACTIVE. SO I'll ACTIVATE YOUR GIANT PHALLUS WITH MY PUSSY! {w=3.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/barbarasex.mp3"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-74
        show winrachelfuck
    if drolltrumpfsex == 2:
        show winrachelfuck
        show winmelaniaivanka02-74
    if drolltrumpfsex == 3:
        show winrachelfuck
        show winmelaniaivanka03-74
    $ renpy.pause(.74, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-74
    show orgyrachelcum
if drolltrumpfsex == 2:
    show orgyrachelcum
    show winmelaniaivanka02-74
if drolltrumpfsex == 3:
    show orgyrachelcum
    show winmelaniaivanka03-74
with dissolve
mc "Take that HEALTHY dose of teenage cum, AAAH! {w=1.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
ra "You can EMPTY yourself in my poontang ANYTIME you want, President [name]! {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgyrachelleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgyrachelleave with moveoutright       
    
label Wintaylorfuckx:
show orgytaylorsetup at farleft02
mc "TAYLOR! Conjugal visit in the White House! {w=1.5}{nw}"
window hide
show orgytaylorsetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgytaylorsetup at left
with dissolve
to "I see you've been busy hubby, now is the time to make my ASS BUSY! {w=2.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/barbarasex.mp3"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-74
        show wintaylorfuck
    if drolltrumpfsex == 2:
        show wintaylorfuck
        show winmelaniaivanka02-74
    if drolltrumpfsex == 3:
        show wintaylorfuck
        show winmelaniaivanka03-74
    $ renpy.pause(.74, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-74
    show orgytaylorcum
if drolltrumpfsex == 2:
    show orgytaylorcum
    show winmelaniaivanka02-74
if drolltrumpfsex == 3:
    show orgytaylorcum
    show winmelaniaivanka03-74
with dissolve
mc "Take that WIFEY, RIGHT UP YOUR POOPCHUTE! {w=1.5}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
to "My darling hubby kept a REAL BIG LOAD for his wife, didn't he? {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgytaylorleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgytaylorleave with moveoutright      

label Winwidowfuckx:
show orgywidowsetup at farleft02
mc "The BLACK WIDOW! Or Scarlett Johansson to be more precise. {w=2.0}{nw}"
window hide
show orgywidowsetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgywidowsetup at left
with dissolve
wi "After FIGHTING against EVIL, it's time for my PUSSY to FIGHT against your MONSTERCOCK! {w=3.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/barbarasex.mp3"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-74
        show winwidowfuck
    if drolltrumpfsex == 2:
        show winwidowfuck
        show winmelaniaivanka02-74
    if drolltrumpfsex == 3:
        show winwidowfuck
        show winmelaniaivanka03-74
    $ renpy.pause(.74, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-74
    show orgywidowcum
if drolltrumpfsex == 2:
    show orgywidowcum
    show winmelaniaivanka02-74
if drolltrumpfsex == 3:
    show orgywidowcum
    show winmelaniaivanka03-74
with dissolve
mc "BUSTING INSIDE A PSEUDO-SUPERHEROINE, AAAH! {w=2.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
wi "You're FLOODING my insides with your superhero cream, AAAH! {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgywidowleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgywidowleave with moveoutright       

label Winwendyfuckx:
show orgywendysetup at farleft02
mc "Wendy from swampy Louisiana! HURRAH! {w=2.0}{nw}"
window hide
show orgywendysetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgywendysetup at left
with dissolve
we "I'm gonna DRAIN YOUR SWAMP, cowboy! {w=2.0}{nw}"
mc "Take a ride, YEE-HAW! {w=1.5}{nw}"
scene newovaloffice01
play channel2 "Sounds/barbarasex.mp3"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-74
        show winwendyfuck
    if drolltrumpfsex == 2:
        show winwendyfuck
        show winmelaniaivanka02-74
    if drolltrumpfsex == 3:
        show winwendyfuck
        show winmelaniaivanka03-74
    $ renpy.pause(.74, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-74
    show orgywendycum
if drolltrumpfsex == 2:
    show orgywendycum
    show winmelaniaivanka02-74
if drolltrumpfsex == 3:
    show orgywendycum
    show winmelaniaivanka03-74
with dissolve
mc "TRY AND DRAIN THAT MONSTERLOAD, AAAH! {w=2.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
we "This FLOOD was worse than Katrina, but I LOVED IT! {w=2.5}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgywendyleave at centerright
with dissolve
mc "I'm STILL HARD, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgywendyleave with moveoutright       

label Winpaulettefuckx:
show orgypaulettesetup at farleft02
mc "Canadian super-envoy Paulette! Welcome to the US of SEX! {w=2.5}{nw}"
window hide
show orgypaulettesetup at left with move
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02a
show orgypaulettesetup at left
with dissolve
qu "I must extend my country's friendship with yours. ORALLY, hey? {w=3.0}{nw}"
mc "HEY YEAH! {w=1.0}{nw}"
scene newovaloffice01
play channel2 "Sounds/blowjob.ogg"
$ count = 12
while count > 0:
    if drolltrumpfsex == 1:
        show winmelaniaivanka01-74
        show winpaulettefuck
    if drolltrumpfsex == 2:
        show winpaulettefuck
        show winmelaniaivanka02-74
    if drolltrumpfsex == 3:
        show winpaulettefuck
        show winmelaniaivanka03-74
    $ renpy.pause(.74, hard='True')
    $ count -= 1
scene newovaloffice01
if drolltrumpfsex == 1:
    show winmelaniaivanka01-74
    show orgypaulettecum
if drolltrumpfsex == 2:
    show orgypaulettecum
    show winmelaniaivanka02-74
if drolltrumpfsex == 3:
    show orgypaulettecum
    show winmelaniaivanka03-74
with dissolve
mc "TAKE THIS FAT LOAD BACK TO CANADA, RHAAA! {w=2.0}{nw}"
stop channel2
play sound "v10/ah.ogg"
window hide
with fastflash
qu "I'm sure Trudeau will appreciate your cream pudding. {w=2.0}{nw}"
scene newovaloffice01
if drolltrumpfsetup == 1:
    show trumpfsetup01
if drolltrumpfsetup == 2:
    show trumpfsetup02
if drolltrumpfsetup == 3:
    show trumpfsetup03
show mcsetup02b
show orgypauletteleave at centerright
with dissolve
mc "I NEED MORE SEX, NEXT GIRL!{w=1.0}{nw}"
window hide
hide orgypauletteleave with moveoutright
jump Winnancyfuckx        
