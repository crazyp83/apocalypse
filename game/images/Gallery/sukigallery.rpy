label SukiGallery:
stop music
call screen gallerysuki
screen gallerysuki:
    add "Gallery/sukigallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("gallerysuki"), Jump ("MainGallery")]

    if renpy.seen_image("sukicommand05"):
        imagebutton:
            focus_mask True
            idle "Gallery/sukigallery01.png" xpos 621 ypos 100
            hover "Gallery/sukigallery01.png"
            action Jump ("SukiGallery01")

    if renpy.seen_image("sukicommand05") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("SukiGallery")

    if renpy.seen_image("sukidate01"):
        imagebutton:
            focus_mask True
            idle "Gallery/sukigallery02.png" xpos 1050 ypos 100
            hover "Gallery/sukigallery02.png"
            action Jump ("SukiGallery02")

    if renpy.seen_image("sukidate01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("SukiGallery")

    if renpy.seen_image("dreamsuki01"):
        imagebutton:
            focus_mask True
            idle "Gallery/sukigallery03.png" xpos 1478 ypos 100
            hover "Gallery/sukigallery03.png"
            action Jump ("SukiGallery03")

    if renpy.seen_image("dreamsuki01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("SukiGallery")

    if renpy.seen_image("sukipyjama02"):
        imagebutton:
            focus_mask True
            idle "Gallery/sukigallery04.png" xpos 621 ypos 400
            hover "Gallery/sukigallery04.png"
            action Jump ("SukiGallery04")

    if renpy.seen_image("sukipyjama02") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("SukiGallery")

    if renpy.seen_image("sukiwiggle"):
        imagebutton:
            focus_mask True
            idle "Gallery/sukigallery05.png" xpos 1050 ypos 400
            hover "Gallery/sukigallery05.png"
            action Jump ("SukiGallery05")

    if renpy.seen_image("sukiwiggle") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("SukiGallery")

    add "Gallery/galleryfuture.png" xpos 1478 ypos 400

    add "Gallery/galleryfuture.png" xpos 621 ypos 700

    add "Gallery/galleryfuture.png" xpos 1050 ypos 700

    add "Gallery/galleryfuture.png" xpos 1478 ypos 700

    add "Gallery/gallerygrid02.png"
    add "Gallery/textsuki.png"

label SukiGallery01:
scene sukicommand01
su "Yes?"
scene sukicommand01
mc "What is your job here exactly Suki?"
su "I run the entire intranet structure of the compound. Security cameras, alert system, New Google Maps update."
scene sukicommand03 with fastdissolve
su "Your intranet access too. I'm the one who designed Siri..."
mc "Mmh, would you happen to have access to the actual internet?"
scene sukicommand05 with fastdissolve
su "I have indeed privileged access to the Dark Web. And only me."        
mc "I see... Well congrats on Siri, she's smoking hot."
mc "What happened to you after the Apocalypse?"
scene sukicommand05 with fastdissolve   
su "I searched for my family. My seven brothers and sisters, my parents, my four grandparents..."
mc "And? What happened to them?"
scene sukicommand06 with fastdissolve                              
su "They were ALL dead! *sob* I cried for such a long time..."
mc "Wow, that is tough, losing your entire extended family like that. I feel for you..."
scene sukicommand01 with fastdissolve                               
su "*sob*.. And then, I had an awakening. I was going to use my skills to get back at those who did that to my family."
mc "Amazing, just like me. We have so much in common."
scene sukicommand03 with fastdissolve                                
su "And we complement each other too, since you have the muscles and... I have the brains."
mc "Hey, I have a brain too!"
su "Sure [name]. Just not as developed as other people... You must go now, I was about to hack some government server and I can't be disturbed."
jump SukiGallery

label SukiGallery02:
play music "v07/datemusic.mp3"
scene canyon01
show sukidate01
su "Wow, this place is absolutely BEAUTIFUL! Thank you so much for taking me here [name]!"
mc "My pleasure, I knew you would like to get outdoors and...err... get in your bikini."
hide sukidate01
show sukidate02
with fastdissolve
su "I can finally stretch my legs a bit and enjoy the sunshine, instead of being stuck in the compound basement..."
mc "You're welcome to suntan, we have several hours ahead of us here..."
hide sukidate02
show sukidate03
with fastdissolve
su "Mmh, yes, I might just do that."
mc "Topless?"
su "Why, you want to ogle my big Asian breasts [name]?"
mc "It's just that tanlines might ruin your otherwise flawless complexion."
hide sukidate03
show sukidate01
su "Ah yeah, that's true. I hadn't thought about that, you seem to know a lot more than me about outdoors stuff."
mc "Sure, I'm an adventurer and a HERO, so I need to know about that kind of stuff."
su "Sure you are, sure you are... And hopefully a valuable asset for the Deep State... Let's go and lie down on that rock over there."
scene sukidatenaked01 with fade
mc "Cool, she even decided to go full naked..."
scene sukidatenaked02
su "Did you say something [name]?"
mc "Err..."
su "Why don't you join me on this rock, you need to catch some sun too. I read on the dark web that sun rays cleanse the skin of radioactivity..."
mc "Really? Then I'll definitely join you. COMMANDO-style!"
su "I thought so..."
scene sukidatenaked03
su "Especially since there is a LOT of skin that needs cleansing on that giant dong of yours... *wink*"
scene canyon01 with dissolve
show sukidate01
su "Well, thank you for this great date with me... I... should go now."
mc "A goodbye kiss perhaps?"
su "Of course, I thought you'd never ask!"
hide sukidate01
scene canyon01 blurred with fastdissolve
show sukidate04
window hide
play sound "Sounds/kiss.mp3"
$ renpy.pause(2.0, hard='True')
scene canyon01 with dissolve
show sukidate01
mc "See you around the compound Suki..."
su "Yes, I sure WILL..."
stop music
jump SukiGallery

label SukiGallery03:
play sound "Sounds/dream.mp3"
scene classdream
show dreamsuki01
play music "Sounds/showerstrip.mp3"
su "Beware, I'm a REAL Ninja Freedom Fighter!"
mc "Hey, I'm on your side! You can drop the blade, Suki."
hide dreamsuki01
show dreamsuki02
with fastdissolve
su "A Ninja NEVER lets his guard down... How can you prove to me you're not a Trumpster?"
mc "Hang on, let me check my stats screen... Ah, shit, I can't do that during a day-dreaming sequence."
hide dreamsuki02
show dreamsuki03
with fastdissolve
su "Are you ogling my tits? That would make you either a FAKE CONSERVATIVE PERVERT or a normal liberal."
mc "I was actually thinking... Doesn't it slow down your ninja moves, since it looks quite tight..."
su "And what are you suggesting to improve my agility?"
mc "Well, I'm suggesting you go naked, basically. Cos I'm a normal real liberal pervert or something like that."
su "I might try that, just this once. Since this is all your dream and it's not real."
hide dreamsuki03
show dreamsuki04
with fastdissolve
su "I must admit, I DO feel lighter and... more dexterous and adroit."
mc "I didn't catch a word of that but I totally agree."
hide dreamsuki04
show dreamsuki05
with fastdissolve
su "Ah, ah, it was a vocabulary test to see if yours was just as limited as President-for-life Trumpf's! You've given yourself in, trumpster!"
mc "Hang on a minute, if it's my dream, these were MY words. So MY extended liberal vocabulary."
hide dreamsuki05
show dreamsuki06
with fastdissolve
su "That is indeed impeccable Boolean logic. I apologize [name]. How can I make it up to you?"
mc "Have a guess..."
su "Liberal logic would predict that you're about to pull your pants down and require vigorous handling of your man-tool."
play sound "Sounds/zipper.mp3"
hide dreamsuki06
show dreamsuki07
with fastdissolve
mc "See, I'm a perfectly libero-logical person indeed. Just like you."
su "And your cock is VERY progressive. It's progressing right now... 18 inches, 19, 20 INCHES!"
hide dreamsuki07
show dreamsuki08
with fastdissolve
su "Do you like how I tenderly tease your giant glans while I cup your cum-laden balls?"
mc "I sure do, Suki, keep going!"
su "Maybe we should slowly progress to the next stage. You cumming LIBERALLY all over the place!"
mc "I'm in! I'm as progressive as it gets for that kind of stuff."
hide dreamsuki08
show dreamsuki09
with fastdissolve
su "Then let my expert ninja fingers do the work..."
window hide
hide dreamsuki09
show dreamsuki10
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamsuki10
show dreamsuki09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamsuki09
show dreamsuki10
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamsuki10
show dreamsuki09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamsuki09
show dreamsuki10
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamsuki10
show dreamsuki09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamsuki09
show dreamsuki10
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamsuki10
show dreamsuki09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamsuki09
show dreamsuki10
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamsuki10
show dreamsuki09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamsuki09
show dreamsuki10
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamsuki10
show dreamsuki09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamsuki09
show dreamsuki10
with fastdissolve
mc "Oh, fuck, you're such a tease, I'm gonna..."
hide dreamsuki10
show dreamsuki11
with fastdissolve
mc "...CUM! AAAH!"
su "Ooh, I was THAT good, hey? BLAST all that HOT SPUNK, [name]!"
hide dreamsuki11
show dreamsuki12
with fastdissolve
su "Yes, all that cum on my face is pure virtual BLISS!"
mc "FUCK, I'm dumping a MEGA-LOAD! RHAAA!"
hide dreamsuki12
show dreamsuki13
with fastdissolve
su "And it's sssooo tasty too! I could eat this ALL DAY."
mc "By the way, I meant to ask you. Did you clean your hands with hydroalcoholic gel before touching my cock?"
hide dreamsuki13
show dreamsuki14
with fastdissolve
su "And why do you ask?"
mc "Well, I mean, you're Asian, so I've got to be careful, what with all those Chinaviruses running around."
su "Umpf. I KNEW IT!"
stop music
jump SukiGallery

label SukiGallery04:
scene bedroom01
show sukipyjama01 with moveinright
with dissolve
su "You called me? I was about to go to bed."
mc "Yeah, you're in my harem, time to do your duty."
su "Errr... I'm not used to this. I..."
mc "Are you a virgin?"
su "Well... Yes."
mc "Don't worry, I'll talk you through this. Just take off your gown slowly for me..."
play music "v07/datemusic.mp3"
hide sukipyjama01
show sukipyjama02
with fastdissolve
su "Like that?"
mc "Yeah, just like that... Keep going..."
hide sukipyjama02
show sukipyjama03
with fastdissolve
su "How do I compare to the other girls? Am I to your liking [name]?"
mc "Damn right you are Suki, you're smoking hot!"
hide sukipyjama03
show sukipyjama04
with fastdissolve
su "I... put on some lingerie for you. I... don't know if I should show you..."
mc "Show me, show me, show me please!"
hide sukipyjama04
show sukipyjama05
with fastdissolve
su "I'm... a bit shy. In front of a boy looking at me like that."
mc "Then turn round so you won't see me looking..."
hide sukipyjama05
show sukipyjama06
with fastdissolve
su "Mmmh..."
scene bedroom01 blurred
show sukipyjama06b
with dissolve
su "What... What are you doing?"
mc "Just admiring the rear view..."
su "Come closer to me please, I want to feel... your body next to mine."
scene bedroom01
show sukipyjama07
with dissolve
su "I...took my top off for you. I know boys like breasts..."
mc "You're damn right we do!"
su "You can... come closer and touch them if you want."
hide sukipyjama07
show sukipyjama08
with dissolve
play sound "Sounds/womanmoan.mp3"
su "Oooh, a boy is... feeling  me up!"
mc "And you're grinding your ass on my cock, naughty girl. You want to see it?"
su "Y..Yes. Yes, I do, [name]!"
scene mcbedroomsuki00 with dissolve
su "So it's true! Other girls told me it was GIGANTIC and now I see why."
mc "Do you want to feel its POWER, Suki?"
su "Y...Yes."
scene mcbedroomsuki01 with dissolve
su "My hand can't even get around its GIANT girth! I... I don't know if it will fit."
mc "We'll make it fit, don't worry. Let me lick your pussy to get you going..."
su "O...Okay. But be gentle, please."
stop music
scene mcbedroomsuki02 with dissolve
play music "Sounds/lick.mp3"
su "Oooh! Your tongue... twirling on my sensitive pussy!"
mc "What a tasty snack...err.. I meant snatch. I think you're ready now."
stop music
scene mcbedroomsuki03 with dissolve
su "I don't know...  How can any pussy be ready for such an ENORMOUS piece of boymeat???"
mc "Just slowly slide down on it, Suki, you can do it!"
su "I'll... I'll try."

play music "Sounds/womansex01.mp3"
label MCSukiSlowx:
hide mcbedroomsukifast
show mcbedroomsukislow
call screen mcsukislow01x
screen mcsukislow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("MCSukiEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MCSukiFastx") 

label MCSukiFastx:
su "Your cock is just... SSOO BIG!"
mc "Do it faster, that way, it will over faster. It's a win-win situation."
hide mcbedroomsukislow
show mcbedroomsukifast
call screen mcsukifast01x
screen mcsukifast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("MCSukiEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MCSukiSlowx") 

label MCSukiEndx:
hide mcbedroomsukislow
hide mcbedroomsukifast
scene mcbedroomsukicum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Damn, I'm nutting already! You pussy is just TOO GOOD!"
su "Oooh, I'm so proud! You can keep pumping your seed inside me, go on, do it [name], FILL ME UP WITH YOUR BOYSEED!"
scene mcbedroomsukicum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Damn, you're becoming a real cumslut real fast, Suki! Here I go, MORE CUM FOR YOU! AAAAH!"
su "AAAH, I've never felt so FULL and FULLFILLED!"
scene mcbedroomsukicum03 with dissolve
su "You've BLOATED me with your cum [name]! I can't... even stand up anymore."
mc "Just pour it out by pressing on your belly."
scene mcbedroomsukicum03b with dissolve
play sound "Sounds/splooge01.mp3"
su "Like that?"
scene mcbedroomsukicum03 with dissolve
su "There's still a LOT left."
mc "Then do it again..."
scene mcbedroomsukicum03b with dissolve
play sound "Sounds/splooge01.mp3"
su "That's better... I think you came about a GALLON of cum inside me."
mc "That sounds about right. But I'm still HARD and READY for MORE, so hop on the bed, Suki!"
scene bedroom03b 
show sukibed01
with dissolve
su "I... think I'm ready to service you like a good harem girl now."
stop music
jump SukiGallery

label SukiGallery05:
mc "I see that, you're still in your bed gown."
su "But I have something sexy underneath..."
mc "And it's time for you to show it to me!"
hide sukipyjama01
show sukipyjama02
with dissolve
hide sukipyjama01
show sukipyjama02
with fastdissolve
su "Like that?"
mc "Yeah, just like that... Nice and slow...Keep going..."
hide sukipyjama02
show sukipyjama03
with fastdissolve
su "You like this lingerie don't you [name]?"
mc "Damn right I do, especially when worn by someone as smoking hot as you!"
hide sukipyjama03
show sukipyjama04
with fastdissolve
su "I'll drop the bed gown and..."
mc "Now we're talking!"
hide sukipyjama04
show sukipyjama05
with fastdissolve
su "I think I should tease you a bit, this is going too fast after all... I'm not that kind of girl."
mc "No, don't tease me please!"
hide sukipyjama05
show sukipyjama06
with fastdissolve
su "You're a naughty boy, I'll turn my back to you then..."
scene bedroom01 blurred
show sukipyjama06b
with dissolve
mc "The view is just as nice from this side..."
su "I just took my top off while you were ogling my ass and now I have a surprise for you..."
scene bedroom01
show sukiwiggle
with dissolve
play music "Sounds/stripmusic.mp3"
call screen sukiwigx
screen sukiwigx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukiWiggleEndx")

label SukiWiggleEndx:
su "Now your turn to bring that fat cock over here closer to me [name]. I want to see it again!"
stop music
hide sukiwiggle
show sukipyjama07
with dissolve
mc "Like what you see Suki?"
su "Y...yes. And you, do you like my breasts? They are not too small compared to some of the other girls?"
mc "Let me check..."
hide sukipyjama07
show sukipyjama08
with dissolve
play sound "Sounds/womanmoan.mp3"
mc "Nope, just the right size for a full breast-grabbing session..."
su "Oooh, I like it when you feel me up like that..."
mc "Let's move to the bed Suki, I'm like SUPER-HORNY right now!"
scene bedroom03b
show sukibed01
with dissolve
su "I'm not tired anymore. I'm READY."

label SukiFuckChoicex:
stop music
menu:
    "Let's take it nice and slow. Tender-loving missionary style.":
        su "Thank you for being such a considerate harem Master, [name]."
        mc "You're welcome Suki."
        jump SukiMissionaryx
    "I'll hop on the bed and you'll hop on my cock.":
        su "Sure, I can do that."
        mc "And take ALL of it?"
        su "Err... I'll try."
        jump SukiImpalex
    "How about you dislocate your jaw for me?":
        su "You mean you want a blowjob?"
        mc "You read my mind."
        jump SukiBlowjobx
    "It's time I show you the pleasures of TOTAL ANAL DESTRUCTION.":
        su "What? Are you... sure?"
        mc "Yep. I'm sure."
        jump SukiAnalx
    "Let's go to the sofa. And do some stuff there.":
        su "You want to stuff me on the sofa?"
        mc "Correctomundo."
        jump SukiSofaFuckxx
    "I'm done, let's go to sleep.":
        stop music
        jump SukiGallery
        
label SukiImpalex:
scene sukibedjprejump01 with dissolve
mc "Mmmh, yeah, just like that. You're such a tease."
su "You ain't seen nothing yet. I'll TEASE you to the BRINK!"

label SukiTeasex:
show sukiprejump00 with dissolve
su "By slowly going UP and DOWN that mighty shaft with my ass..."
play channel1 "Sounds/boymoan.mp3"
play channel2 "Sounds/wank.mp3"
show mcsukiprejump
call screen mcsukiprejump01x
screen mcsukiprejump01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukiTeaseEndx")

label SukiTeaseEndx:
hide mcsukiprejump
stop channel1
stop channel2
scene bedroom18 blurred
show sukibedprefuck01
mc "Oh God, oh God... I can take much more of this teasing. Please let me fuck your pussy!"
su "BEG for it, [name]."
mc "I'm begging you! AAAH!"

play music "Sounds/womansex02.mp3"
scene mcbedsukijump00
label SukiImpaleSlowx:
hide sukiimpalefast
show sukiimpaleslow
call screen sukiimpaleslow01x
screen sukiimpaleslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukiImpaleEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("SukiImpaleFastx") 

label SukiImpaleFastx:
mc "Please... Please do it FASTER, Suki!"
hide sukiimpaleslow
show sukiimpalefast
call screen sukiimpalefast01x
screen sukiimpalefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukiImpaleEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("SukiImpaleSlowx") 

label SukiImpaleEndx:
mc "Get ready for my load deep inside your womb, Suki!"
stop music
hide sukibedprefuck01
play sound "Sounds/splooge02.mp3"
hide sukiimpaleslow
hide sukiimpalefast
scene sukibedjumpcum01 with fastdissolve
su "You're PUMPING so MUCH cum inside me, I can hear it rumble!"
mc "AAAH! I'm not done yet!"
su "Then I'd better pull your DISGORGING cum-cannon out my overstuffed pussy!"
scene sukibedjumpcum02 with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
su "There, much better, come all MUCH as you like now [name]!"
mc "FUCK! RHAAA! I'm blasting NON-STOP, this is sssooo goood!"
scene sukibedjumpcum03 with fastdissolve
play sound "Sounds/kiss.mp3"
mc "You did a really good job, Suki, worthy of being in my top 6 harem girls."
su "Aren't you limited to 6 anyway?"
mc "Errr... Possibly, I can't remember. Let's move on, I want MORE of you!"
scene bedroom03b
show sukibed01
with dissolve
su "My holes are ready to service you. AGAIN."
jump SukiFuckChoicex
    
label SukiMissionaryx:
scene bedroom18
show sukibedprefuck02
with dissolve
su "So you're going to be gentle with me?"
mc "I'll try..."
su "I know it's not easy with a cock THIS size but try and spare a thought for my poor pussy..."
scene bedroom14
show sukibedprefuck03
with dissolve
mc "There. I'm tenderly pushing your moist pussylips apart with my apple-sized helmet..."
su "Oooh! *puff* Let me take a deep breath..."
su "...And now go ahead, POUND ME with it!"
scene bedroom12 blurred
play music "Sounds/fucksound.mp3"
label SukiMissionarySlowx:
hide mcsukifuckfast
show mcsukifuckslow
call screen sukifuckslow01x
screen sukifuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("SukiMissionaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("SukiMissionaryFastx") 

label SukiMissionaryFastx:
su "You can POWERFUCK ME FASTER if you want, [name]! DO IT!"
hide mcsukifuckslow
show mcsukifuckfast
call screen sukifuckfast01x
screen sukifuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("SukiMissionaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("SukiMissionarySlowx") 

label SukiMissionaryEndx:
mc "Can I tenderly BLAST MY SEMEN inside your pussy, Suki? Cos I'm real close..."
su "YES YOU CAN!"
stop music
hide mcsukifuckslow
hide mcsukifuckfast
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
show sukibedfuckcum01 with fastdissolve
mc "RHAAAA!"
su "PUMP your seed inside me, [name]! I LOVE how your MONSTERCOCK pulses and convulses on every MASSIVE JET OF BOYSPUNK!"
mc "Hang on Suki, I've got some more sperm reserves to cover your body! AAAH!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
hide sukibedfuckcum01
show sukibedfuckcum02
with dissolve
su "Mmmh, you're COVERING me in your HOT ball-batter!"
mc "That's right, cumming FULL STEAM AHEAD! AAAAHHH!"
scene bedroom14 blurred
show sukibedfuckcum03
with dissolve
mc "That's the last of it... PHEW!"
su "You covered me in TONS of cum... ANd it's as thick as porridge! I want some MORE of that stuff, [name]"
mc "Oh, you want MORE? Well, I've got MORE for you, Suki! Get cleaned up and get ready for MORE!"
scene bedroom03b 
show sukibed01
with dissolve
su "My body is ready to please you again, [name]!"
mc "Good girl."
jump SukiFuckChoicex

label SukiBlowjobx:
scene sukipresuck01 with dissolve
su "Your cock is really looking forward to this, isn't it? I can see fat rivulets of precum dripping down your spermhole...."
mc "Yeah... Please don't make me wait too long SUki! I'm desperate for your HOT MOUTH around my FAT SHAFT!"
su "Well, you ask so politely..."
play music "Sounds/hardsucking.mp3"
label SukiBlowSlowx:
hide sukiblowfast
show sukiblowslow
call screen sukiblowslow01x
screen sukiblowslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukiBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("SukiBlowFastx") 

label SukiBlowFastx:
mc "You're doing good, Suki. But you have to increase the tempo and get me to COME!"
hide sukiblowslow
show sukiblowfast
call screen sukiblowfast01x
screen sukiblowfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukiBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("SukiBlowSlowx") 

label SukiBlowEndx:
mc "You're gobbling my dong so well, you're going to make me CUM! Get ready, Suki!"
scene mcsukisuckcum01 with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "FUCK, Blowing my WA-AA-AAD!"
scene mcsukisuckcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
su "GLLRBBB! *puff* You're STILL coming like a fountain???"
scene mcsukisuckcum03 with dissolve
play sound "Sounds/lick.mp3"
su "Wow, you came SSSOO much. All over yourself too! Let me clean that up for you... *slurp*"
mc "Damn, I'm... almost exhausted from this crazy blowjob you gave me..."
su "* slurp* Which means you're NOT exhausted and we can keep going then?"
mc "Yeah, sure. I'm still ROCK-HARD for you, Suki!"
scene bedroom03b 
show sukibed01
with dissolve
su "And I'm all cleanep up and ready to service you. AGAIN."
mc "Good girl."
jump SukiFuckChoicex
    
label SukiAnalx:
scene bedroom18
show sukipreanal01
with dissolve
su "WH...What ar you doing, [name]?"
mc "I'm prepping your tender rosebud..."
su "Are you going ot give it to me ROUGH AND HARD?"
mc "Is that what you want Suki?"
su "YES!!!!"
mc "Alright, get on all fours, I'm gonna PUMMEL your ass!"
scene bedroom12 blurred with dissolve
play music "Sounds/fucksound.mp3"
label SukiAnalSlowx:
hide sukianalfast
hide povsukianalfast
hide povsukianalslow
scene bedroom18 blurred
show sukianalslow
call screen sukianalslow01x
screen sukianalslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukiAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("SukiAnalFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("POVSukiAnalSlowx") 

label SukiAnalFastx:
hide povsukianalslow
hide povsukianalfast
hide sukianalslow
scene bedroom18 blurred
show sukianalfast
call screen sukianalfast01x
screen sukianalfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukiAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("SukiAnalSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("POVSukiAnalFastx") 

label POVSukiAnalSlowx:
hide povsukianalfast
hide sukianalslow
hide sukianalfast
scene bedroom14
show povsukianalslow
call screen povsukianalslow01x
screen povsukianalslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukiAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasteridle.png"
        action Jump ("POVSukiAnalFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("SukiAnalSlowx") 

label POVSukiAnalFastx:
hide povsukianalslow
hide sukianalslow
hide sukianalfast
scene bedroom14
show povsukianalfast
call screen povsukianalfast01x
screen povsukianalfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukiAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("POVSukiAnalSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("SukiAnalFastx") 

label SukiAnalEndx:
su "Please cream in my ass, [name]! I came so many times already and I can't take anymore of your POUNDING!"
mc "You're in luck, I was just about...."
scene bedroom18 blurred
show sukianalcum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...to cum! RHAAAA!"
su "OOOh, my bowels are EXPLODING with cum! AAAH! Please pull out, I feel like I'm past breaking point [name]!!!"
scene bedroom12
show sukianalcum02
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Fuck, DUMPING my load ALL OVER your abck! AAAH!"
su "It's so thick and ther's so much of it! You're SHOWERING CUM all over me!"
scene bedroom14 blurred
show sukianalcum03
su "You're such a BEAST. ALways HARD and INSATIABLE for your harem girls."
mc "That's right! So get cleaned up and let's FUCK SOME MORE!"
scene bedroom03b 
show sukibed01
with dissolve
su "ALL CLEAN! And waiting for what you have in store for me..."
jump SukiFuckChoicex

label SukiSofaFuckxx:
scene mcbedroomsuki00 with dissolve
su "Are you ALWAYS rock-hard?"
mc "Pretty much, yeah. Especially with a HOT harem girl such as you."
su "I'm... flattered."
scene mcbedroomsuki01 with dissolve
su "I could... wank your giant shaft while you kiss my neck perhaps?"
mc "I'd rather taste that sweet pussy of yours, Suki."
su "That's... nice. A harem Master pleasing his harem girl."
scene mcbedroomsuki02 with dissolve
play music "Sounds/lick.mp3"
su "Oooh! Your tongue... twirling on my sensitive pussy! You do this so well, [name]!"
mc "Tons of pussy-licking experience does the trick. Now it's time for you to RIDE THE DONG!"
stop music
scene mcbedroomsuki03 with dissolve
su "Oh God, why did I let myself into this? It looks... too big for my tiny pussy!"
mc "Just slowly slide down on it, Suki, you can do it!"
su "I'll... I'll try."

play music "Sounds/womansex01.mp3"
label SukiSofaSlowxx:
hide mcbedroomsukifast
show mcbedroomsukislow
call screen mcsukislow02xx
screen mcsukislow02xx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("SukiSofaEndxx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("SukiSofaFastxx") 

label SukiSofaFastxx:
su "Your cock is just... SSOO BIG!"
mc "Do it faster, that way, it will over faster. It's a win-win situation."
hide mcbedroomsukislow
show mcbedroomsukifast
call screen mcsukifast02xx
screen mcsukifast02xx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("SukiSofaEndxx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("SukiSofaSlowxx") 

label SukiSofaEndxx:
hide mcbedroomsukislow
hide mcbedroomsukifast
scene mcbedroomsukicum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Damn, I'm nutting already! You pussy is just TOO DAMN GOOD!"
su "YES, I'm cumming too [name]!, FILL ME UP WITH YOUR BOYSEED!"
scene mcbedroomsukicum02 with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH, that's amazing, here I go, MORE CUM FOR YOU! AAAAH!"
su "AAAH, I've never felt so FULL and FULLFILLED!"
scene mcbedroomsukicum03 with dissolve
su "You've BLOATED me with your cum [name]! I can't... even stand up anymore."
mc "Just pour it out by pressing on your belly."
scene mcbedroomsukicum03b with dissolve
play sound "Sounds/splooge01.mp3"
su "Like that?"
scene mcbedroomsukicum03 with dissolve
su "There's still a LOT left."
mc "Then do it again..."
scene mcbedroomsukicum03b with dissolve
play sound "Sounds/splooge01.mp3"
su "That's better... I think you came about a GALLON of cum inside me."
mc "That sounds about right. But I'm still HARD and READY for MORE, so hop on the bed, Suki!"
scene bedroom03b 
show sukibed01
with dissolve
su "I... think I'm ready to service you like a good harem girl now."
jump SukiFuckChoicex
