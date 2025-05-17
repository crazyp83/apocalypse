label ClaraFuck01:
hide screen calendar
hide screen mcstats
$ alienfuck = True
$ weekfuckedclara = True
scene bedroom01
show stripclara01b
with fade
menu:
    "Run scene":
        pass
    "Skip scene":
        jump ClaraEnd
cl "I was praying for my redemption... But I heard your call on the harem-intraphone."
mc "Yes, I was told you are in immortal danger because of your naughty sins, Sister. I am here to help in your redemption! Through SEX!"
hide stripclara01b
show stripclara02b
with fastdissolve
cl "The Church does indeed condone redemption through the sexual pleasuring of harem masters..."
menu:
    "So wear something more appropriate to indicate that you are a sinner in need of redemption, Clara." if churchnickname:
        hide stripclara02b
        show clara03
        with fastdissolve        
        cl "I see. You want me in my \"naughty sister\" outfit then?"
        mc "That's right! And I'll get in my...err... pervy harem master outfit. My jocks basically."
        cl "Will be right back [name]..."
        hide clara03 with moveoutright
        jump ClaraSpanking
    "Do you have some sexy lingerie to put us into the mood?":
        hide stripclara02b
        show clara03
        with fastdissolve 
        cl "Since you've managed to break into my \"Redemption Box\", I do. Let me go and see what I can find in there for you..."
        hide clara03 with moveoutright
        jump ClaraLingerie
    "Then let's move on to that bit straight away then!":
        hide stripclara02b
        show clara03
        with fastdissolve 
        cl "You are VERY eager [name]! I'll will disrobe my religious garments and lie on the bed for you then..."
        jump ClaraFuckChoice
            
label ClaraSpanking:
play music "v07/datemusic.mp3"
scene bedroom02 with fade
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
jump ClaraFuckChoice

label ClaraLingerie:
play music "v07/datemusic.mp3"
scene bedroom02 blurred with fade
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

label ClaraFuckChoice:
scene bedroom03b blurred
show clarabed
with dissolve
cl "What Holy Phallic activities should we engage in [name]?"
stop music
menu:
    "My Phallus demands a warm mouth. And warm tits.":
        cl "Then it shall first enjoy the warmth of my tits followed by the hotness of my mouth and throat!"
        jump ClaraBlowjob
    "Lay on your back Clara, I'm gonna pound your pussy to oblivion!":
        cl "Oblivion??? I don't know... Alright, I AM a SINFUL nun, DO IT!"
        jump ClaraLift 
    "Lather my Saint-Manhood with Holy Baby Oil and let's see if we can make it GROW!" if canonized and toldclaracanonized:
        cl "That would be the HOLIEST of sights indeed if it works! Oh, I so WISH it will work!"
        jump ClaraHugeCock
    "A sinful nun such as yourself needs a thorough backdoor scrubbing.":
        cl "You mean to stick your massive pole in my ASS?"
        mc "Yep."
        cl "Then do a proper rimjob on it to make it nice and slick for your ass-pounder!"
        mc "Alright, I'm in."
        jump ClaraAnal
    "I'm done, let's go to sleep.":
        jump ClaraEnd

label ClaraBlowjob:
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
label ClaraTitfuckSlow:
hide claratitfuckfast
hide claratitfuckpovslow
hide claratitfuckpovfast
show claratitfuckslow
call screen claratitfuckslow01
screen claratitfuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraTitfuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ClaraTitfuckFast") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("ClaraTitfuckPOVSlow") 

label ClaraTitfuckPOVSlow:
hide claratitfuckslow
hide claratitfuckfast
hide claratitfuckpovfast
show claratitfuckpovslow
call screen claratitfuckpovslow01
screen claratitfuckpovslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraTitfuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ClaraTitfuckPOVFast") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("ClaraTitfuckSlow") 

label ClaraTitfuckFast:
if claratitssaid == False:
    mc "Damn, those tits wrapped around my shaft... I'm going to pummel between them FASTER!"
    $ claratitssaid = True
hide claratitfuckslow
hide claratitfuckpovslow
hide claratitfuckpovfast
show claratitfuckfast
call screen claratitfuckfast01
screen claratitfuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraTitfuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ClaraTitfuckSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("ClaraTitfuckPOVFast") 

label ClaraTitfuckPOVFast:
if claratitssaid == False:
    mc "Damn, those tits wrapped around my shaft... I'm going to pummel between them FASTER!"
    $ claratitssaid = True
hide claratitfuckslow
hide claratitfuckfast
hide claratitfuckpovslow
show claratitfuckpovfast
call screen claratitfuckpovfast01
screen claratitfuckpovfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraTitfuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("ClaraTitfuckPOVSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("ClaraTitfuckFast") 
            
label ClaraTitfuckEnd:
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
label ClaraBlowSlow:
hide clarablowfast
show clarablowslow
call screen clarablowslow01
screen clarablowslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ClaraBlowFast") 

label ClaraBlowFast:
mc "Oh God, that mouth! So fucking warm and your throat is so deep! Gotta throat-fuck you faster!!"
hide clarablowslow
show clarablowfast
call screen clarablowfast01
screen clarablowfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ClaraBlowSlow") 

label ClaraBlowEnd:
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
jump ClaraFuckChoice

label ClaraLift:
scene clarapremissionary01 with dissolve
cl "Mmmh, it's so big and already dripping lovely warm pre-cum..."
mc "Mmmh, are you ready for my mighty pillar of lust, Sister Clara?"
cl "If it can relieve me of my inner sins, then yes, I am rea..."
play sound "Sounds/womanscream.ogg"
scene claramissionary00 with dissolve
cl "...DY-AAAH! Your phallus is sssooo BIG! Be careful but... ALSO, FUCK ME HARD!"

play music "Sounds/womansex02.mp3"
label ClaraMissionarySlow:
hide claramissionaryfast
show claramissionaryslow
call screen claramissionaryslow01
screen claramissionaryslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraMissionaryEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ClaraMissionaryFast") 

label ClaraMissionaryFast:
mc "That pussy is just divine... THe way it grips so tight on my shaft..."
cl "Then POUND IT FASTER, it's all yours [name]!"
hide claramissionaryslow
show claramissionaryfast
call screen claramissionaryfast01
screen claramissionaryfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraMissionaryEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ClaraMissionarySlow") 

label ClaraMissionaryEnd:
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
label ClarafuckSlow:
hide clarafuckfast
scene clarafuckbackground
show clarafuckslow
call screen clarafuckslow01
screen clarafuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClarafuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ClarafuckFast") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("ClarafuckTopSlow") 

label ClarafuckTopSlow:
show clarafucktopslow
call screen clarafucktopslow01
screen clarafucktopslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClarafuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ClarafuckTopFast") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("ClarafuckSlow") 

label ClarafuckFast:
hide clarafuckslow
scene clarafuckbackground
show clarafuckfast
call screen clarafuckfast01
screen clarafuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClarafuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ClarafuckSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("ClarafuckTopFast") 

label ClarafuckTopFast:
show clarafucktopfast
call screen clarafucktopfast01
screen clarafucktopfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClarafuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("ClarafuckTopSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("ClarafuckFast") 
            
label ClarafuckEnd:
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
jump ClaraFuckChoice

label ClaraHugeCock:
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
call screen clarahugewank01
screen clarahugewank01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraHugeWankEnd")
label ClaraHugeWankEnd:
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
label ClaraHugeSlow:
hide clarahugefast
show clarahugeslow
call screen clarahugeslow01
screen clarahugeslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraHugeEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ClaraHugeFast") 

label ClaraHugeFast:
cl "It takes a while to make a BEAST like that cum, I'm going to have to increase the tempo to bring you over the EDGE!"
mc "AAAH, sssooo goood...."
hide clarahugeslow
show clarahugefast
call screen clarahugefast01
screen clarahugefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraHugeEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ClaraHugeSlow") 

label ClaraHugeEnd:
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
jump ClaraFuckChoice
    
label ClaraAnal:
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
label ClaraAnalSlow:
hide claraanalfast
show claraanalslow
call screen claraanalslow01
screen claraanalslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ClaraAnalFast") 

label ClaraAnalFast:
cl "That's good, I'm getting used to the size... You can POUND ME FASTER NOW!"
hide claraanalslow
show claraanalfast
call screen claraanalfast01
screen claraanalfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ClaraAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ClaraAnalSlow") 

label ClaraAnalEnd:
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
jump ClaraFuckChoice

label ClaraEnd:
show screen calendar
show screen mcstats
scene clarasleep with fade
$ loc = "bedroom"
play sound "Sounds/snoring.mp3"
pause 3
call NewDay
jump Bedroom