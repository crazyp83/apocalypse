label ExploreHex17:
stop sound
$ explored = True
scene desertstorm01 with fade
if exploredhex17:
    mc "It's very dusty and windy here...AGAIN."    
if exploredhex17 == False:
    mc "It's very dusty and windy here..."
if withbe:
    be  "A sandstorm must be brewing..."
    if exploredhex17:
        be "AGAIN."
    mc "I'll go investigate."
    be "Don't go too far, if the sandstorm strikes, we'll lose contact!"
if withpe:
    pe  "A sandstorm must be brewing..."
    if exploredhex17:
        pe "AGAIN."
    mc "I'll go investigate."
    pe "Don't go too far, if the sandstorm strikes, we'll lose contact!"
       
play music "Sounds/desertwind02.mp3"
$ exploredhex17 = True
show sandstorm02
mc "Ah, the sandstorm that was brewing just brewed..."
show sandstorm01
if scarlettjoined and withmo and missionwi01 and donemissionwi01 == False:
    mc "Nancy, stay with me."
    mo "Of course sweetie, this storm is scaring me... What shall we do?"
    mc "I hope Scarlett Joh..., I mean the Black Widow will come and rescue us..."
    hide sandstorm02
    show widowdesert03
    show sandstorm02
    mc "Ah, there she is! Hi Black Widow!"
    hide widowdesert03
    hide sandstorm02
    show widowdesert01
    show sandstorm02
    wi "Hello STUD! As a true AVENGER, you are drawn to our lair I see!"
    mc "Yep, and this time I brought a new recruit to our cause!"
    wi "Very good, let's move inside quickly, this storm is really strong."
    mo "Where is she taking us [name]? I'm not sure we can trust her..."
    mc "Don't worry Nancy, I've been here...err... plenty of times."
    jump DesertStormAgain
if scarlettjoined and withmo and donemissionwi01:
    mo "Oh, I see, we're going to visit the Black Widow. AGAIN."
    mc "She gathers essential information for me Nancy. And you do form a great couple..."
    hide sandstorm02
    show widowdesert03
    show sandstorm02
    mc "Ah, there she is! Hi Black Widow!"
    hide widowdesert03
    hide sandstorm02
    show widowdesert01
    show sandstorm02
    wi "Hello STUD! As a true AVENGER, you are drawn to our lair I see!"
    mc "Yep, and so is Captain Marvel!"
    wi "Ooh, I'm so happy she could join us again... *wink* Follow me to the Avengers' lair!"
    jump DesertStormAgain

if scarlettjoined:
    mc "I hope Scarlett Joh..., I mean the Black Widow will come and rescue me again..."
    hide sandstorm02
    show widowdesert03
    show sandstorm02
    mc "Ah, there she is! Hi Black Widow!"
    hide widowdesert03
    hide sandstorm02
    show widowdesert01
    show sandstorm02
    wi "Hello STUD! As a true AVENGER, you are drawn to our lair I see!"
    mc "Yep, also to your amazing body."
    wi "How flattering... Follow me, I'll show you the way."
    jump DesertStormAgain
mc  "Shit, now I can't see a damn thing..."
if withpe:
    mc "I don't even know where Penny is, I hope she's alright."
if withbe:
    mc "I don't even know where Bella is, I hope she's alright."
hide sandstorm02
show widowdesert03
show sandstorm02
if scarlettleft:
    mc "I see someone's shape over there, it's that mysterious woman again..."    
if withpe:
    mc  "I see someone's shape over there, I hope that's Penny. She found me."
    jump DesertStorm02
if withbe:
    mc  "I see someone's shape over there, I hope that's Bella. She found me."
    jump DesertStorm02

label DesertStorm02:
hide widowdesert03
hide sandstorm02
show widowdesert01
show sandstorm02
if scarlettleft:
    wi01 "THIS time, you'd better follow me for good stranger, or YOU WILL DIE!"
    mc "Right, okay."
    wi01 "Stay close to me!"
    jump DesertStorm03
mc "Hang on, it doesn't look like her at all..."
wi01 "If you want to live stranger, follow me."
menu:
    "Follow her":
        wi01 "Stay close to me!"
        jump DesertStorm03
    "Tell her to mind her own business":
        $ scarlettleft = True
        wi01 "You're crazy, you'll never survive this sandstorm, trust me!"
        mc "I'm pretty sure *cough*.. that I told you *cough* to fuck off!"
        wi01 "Fine, don't come crying to me when the sand starts choking you to death."
        hide widowdesert01 with dissolve
        if gasmask:
            mc "I'd better put my gas mask on *cough*. This sandstorm is getting worse."
            hide sandstorm01
            mc "Ah, it's  clearing up a bit...."
            jump DesertStormEnd
        mc "*cough*...*cough*."
        window hide
        show mcinjured at injured
        $ renpy.pause(2.0, hard=True)
        hide mcinjured
        $ mcinjured = True
        $ mcinjuredsand = True        
        hide sandstorm01
        mc "Ah, it's clearing up a bit, thanks God...*cough*"
        scene banknote01
        mc "Oh, and lucky me, the wind blew a ten New Dollar banknote right under my feet! That mysterious woman must have dropped it..."
        $ money += 10
        jump DesertStormEnd

label DesertStormEnd:
stop music
scene desertstorm01 with dissolve
if withbe:
    show bellaout03
    be "Where the hell were you? I've been searching for you for ages!"
    mc "I was stuck in the sandstorm, I looked for you too you know..."
    be "Well not very well clearly! Let's go back to the compound before another storm hits us..."
    mc "Roger that."
if withpe:
    show pennyout03
    pe "Where the hell were you? I've been searching for you for ages!"
    mc "I was stuck in the sandstorm, I looked for you too you know..."
    pe "Well not very well clearly! Let's go back to the compound before another storm hits us..."
    mc "Roger that."
scene command01 with fade
$ period += 1
show lena01
le "So, what do you have to report about area B7, scouts?"
if withbe:
    be "We were caught in a sandstorm. But once it cleared up, we didn't see anything. Just empty desert."
    if mcinjuredsand:
        be "Oh, and [name] ate some sand."
        mc "*hiss* Just... *breath*...a bit. *hiss*."
if withpe:
    pe "We were caught in a sandstorm. But once it cleared up, we didn't see anything. Just empty desert."
    if mcinjuredsand:
        pe "Oh, and [name] ate some sand."
        mc "*hiss* Just... *breath*...a bit. *hiss*."
hide lena01
show lenapensive
le "I'm sure the Trumpf militia must be somewhere around that area... We'll look further tomorrow. Dismissed, scouts!"
if mcinjuredsand:
    hide lenapensive
    show lena03
    with fastdissolve
    le "And you, go and have this breathing problem checked at the medical bay. We need you in top condition."
    jump Medbay
hide lenapensive
jump LeaveCommand


label DesertStorm03:
$ scarlettjoined = True
scene widowlairoutside
show widowdesert02
show sandstorm02
wi01 "This way, hurry up! We're almost there..."

stop music
scene widowlair01 with fade
$ metwi = True
show widow01
wi "We can breathe here, this place is well insulated from the elements."
menu:
    "Who are you? You look familiar." if mctrumpster <= 2:
        hide widow01
        show widow02
        with fastdissolve
        wi "I am the Black Widow. Don't you recognize me?"
        mc "I recognize Scarlett Johansson, that's who I recognize. This is the REAL world, not Hollywood fantasy la-la land."
        hide widow02
        show widow04
        with fastdissolve
        wi "Well OK, I AM Scarlett Johansson. Are you happy now?"
        mc "Not really. It opens even more questions than it answers..."
        hide widow04
        show widow05
        with fastdissolve
        wi "And first of all, who the fuck are YOU, Mr-who's-just-been-saved-by-Scarlett-Johannson?"
        mc "My name is [name] and I am the HERO, that's who I am!"
        wi "The HERO? The hero of WHAT exactly Mr-smart-ass?"
        mc "The hero who is going to save the world by ousting President-for-Life Trumpf from power!"
        hide widow05
        show widow03
        with fastdissolve
        wi "Ah, so we have the same objective then. You could be my sidekick, I need one, Captain America is dead. Don't you agree?"
        mc "When you say Captain America, you actually mean the actor Chris Evans, right?"
        hide widow03
        show widow01
        with fastdissolve
        wi "Yeah, OK, I meant him. You didn't answer my question..."
        mc "I don't know yet, I need to think about it. Would I become Captain America then, I'm confused?"
        hide widow01
        show widow03
        with fastdissolve
        wi "Maybe I could help you think clearer Mr... \"Captain America\"..."
        jump DesertStorm04
    "What is this place?":
        hide widow01
        show widow03
        with fastdissolve
        wi "This is the secret lair of the Black Widow. From here, the Avengers plan their next move in their fight for FREEDOM and JUSTICE!"
        mc "Face it Scarlett, you're getting crazy. I recognize you. You're not the ACTUAL Black Widow, you're an ACTRESS who plays the Black Widow."
        mc "It's NOT the same thing my dear... The Black Widow is a FICTIONAL character. This is the REAL world, not Hollywood fantasy la-la land."
        hide widow03
        show widow04
        with fastdissolve
        wi "Well OK, I AM Scarlett Johansson. Are you happy now? Spoiling all the fun, you MUST be a Trumpster..."
        if mctrumpster == 5:
            mc "Yeah, and what if I am, Hollywood libtard?"
            hide widow04
            show widow05
            with fastdissolve
            wi "In that case, get the fuck out of my lair!"
            menu:
                "Reconsider my allegiances (-1 Trumspters)":
                    mc "I was only kidding, of course I'm not a bloody MAGAt. We can be friends."
                    hide widow05
                    show widow02
                    with fastdissolve
                    wi " Ah, that's better..."
                    window hide
                    show minustrumpster at posmission
                    $ renpy.pause(2.0, hard=True)
                    hide minustrumpster                                        
                    $ mctrumpster -= 1
                    wi "Now that you are on the morally-superior Hollywoood side, we NEED to unite our forces! Come on, you know it makes perfect sense! Pretty please..."
                    mc "I don't know yet, I need to think about it. Would I become Captain America then, I'm confused?"
                    hide widow02
                    show widow03
                    with fastdissolve
                    wi "Maybe I could help you think clearer Mr... \"Captain America\"..."
                    jump DesertStorm04
                "Do not budge from your current faction":
                    mc "Snowflake. Sssoo easily vexed."
                    wi "How dare you! Get the fuck out of my lair, deplorable!"
                    jump DesertStormEnd                    
        if mctrumpster <= 4:
            mc "No I'm NOT! I'm trying to find Trumpf City to oust him from power for what he's done to my family actually!"
            hide widow04
            show widow01
            with fastdissolve
            wi "Ah, so we have the same objective then. You could be my sidekick, I need one, Captain America is dead. Don't you agree?"
            mc "When you say Captain America, you actually mean the actor Chris Evans, right?"
            hide widow01
            show widow02
            with fastdissolve
            wi "Yeah, OK, I meant him. You didn't answer my question..."
            mc "I don't know yet, I need to think about it. Would I become Captain America then, I'm confused?"
            hide widow02
            show widow03
            with fastdissolve
            wi "Maybe I could help you think clearer Mr... \"Captain America\"..."
            jump DesertStorm04
                
    "Why did you decide to save me?":
        hide widow01
        show widow02
        wi "I'm looking for a sidekick. You seem strong. Like Captain America. I am the BLACK WIDOW for your information."
        mc "No you're not. You're clearly Scarlett Johansson, the ACTRESS who plays the Black Widow. Not the same thing..."
        if mctrumpster == 5:
            hide widow02
            show widow04
            with fastdissolve
            wi "Well OK, I AM Scarlett Johansson. Are you happy now? Spoiling all the fun, you MUST be a Trumpster..."
            mc "Yeah, and what if I am, Hollywood libtard?"
            hide widow04
            show widow05
            with fastdissolve
            wi "In that case, get the fuck out of my lair!"
            menu:
                "Reconsider my allegiances (-1 Trumspters)":
                    mc "I was only kidding, of course I'm not a bloody MAGAt. We can be friends."
                    hide widow05
                    show widow02
                    with fastdissolve
                    wi " Ah, that's better..."                    
                    window hide
                    call MinusTrumpster
                    wi "Now that you are on the morally-superior Hollywoood side, we NEED to unite our forces! Come on, you know it makes perfect sense! Pretty please..."
                    mc "I don't know yet, I need to think about it. Would I become Captain America then, I'm confused?"
                    hide widow02
                    show widow03
                    with fastdissolve
                    wi "Maybe I could help you think clearer Mr... \"Captain America\"..."                    
                    jump DesertStorm04
                "Do not budge from your current faction":
                    mc "Snowflake. Sssoo easily vexed."                    
                    wi "How dare you! Get the fuck out of my lair, deplorable!"
                    jump DesertStormEnd
        hide widow02
        show widow06
        with fastdissolve
        wi"Oh, why does everyone I meet have to spoil the fun? Please become my Captain America, I beg you!"
        mc "Why would I do that? I'm not playing here lady, I'm in the REAL fight of finding President-for-Life Trumpf and ousting him from power!"
        hide widow06
        show widow03
        with fastdissolve
        wi "Well so am I! So we NEED to unite our forces! Come on, you know it makes perfect sense! Pretty please..."
        mc "I don't know yet, I need to think about it. Would I become Captain America then, I'm confused?"
        wi "Maybe I could help you think clearer Mr... \"Captain America\"..."
        jump DesertStorm04
        
label DesertStorm04:
hide screen mcstats
hide screen calendar
scene widowlair02 with dissolve
show widowundress01
wi "I already had big breasts before, but look at them NOW! So soft and HUGE... They could be yours if you agreed to join the Avengers..."
mc "Alright, if I must..."
hide widowundress01
show widowundress02
with fastdissolve
wi "Big enough for you big boy?"
mc "Fuck yeah! Perfect size for my massive cum-cannon..."
scene widowlair02 blurred
show widowtits01
wi "Mmh, I can't wait to get them covered in hot Captain America spunk!"
mc "I'll be happy to oblige!"
wi "What about my ass? My AVENGER ass? Do you want to see it?"
mc "Of course!"
scene widowstrip with dissolve:
        ypos -3.0
        linear 10.0 ypos 0.0
$ renpy.pause(10.0, hard=True)
wi "Please wear this Captain America outfit that's over there. It should fit you, it's the extra-muscular version in case we found someone bigger than Chris Evans to play the role..."
wi "And pretend I'm the Black Widow when you fuck me... Captain America..."
mc "Sure Scarl... I mean Black Widow."

scene widowlair01
show mcwidow01 at midleft with moveinleft
mc "I'm HARD and READY Black Widow! Prepare to feel the power of Captain America's love sword!"
window hide
$ americacostume = True
show americacostume at posmission
$ renpy.pause(4.0, hard=True)
hide americacostume
show widownude at midright with moveinright
wi "Oh my God! That thing is fucking HUGE! Let me worship it like it deserves Captain America..."
call LustPlusWidow
scene widowlair03 blurred
show widowsex01
wi "*gulp* How... How big is this gigantic thing?"
mc "17 inches long according to \"Measure Metrics\" on Daz Studio. So over 20 porn inches."
wi "Fuck my mouth with it Captain America, I've been a naughty girl..."
scene widowlair04 blurred
show widowsex02
mc "There you go, nice and slow at first..."

label DesertStorm05:
scene widowlair05 with dissolve
play music "Sounds/hardsucking.mp3"
label WidowBJslower:
hide widowbjfast
show widowbjslow
call screen widowbjslow
screen widowbjslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WidowBJEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WidowBJfaster") 

label WidowBJfaster:
hide widowbjslow
show widowbjfast
call screen widowbjfast
screen widowbjfast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WidowBJEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WidowBJslower") 

label WidowBJEnd:
stop music
scene widowlair05
show widowbjcum01
mc "Fuck, I'm coming down your throat! AAAH!"
scene widowlair05
show widowbjcum02
mc "There's more where that came from! RHAAA!"
wi "YES! Plaster me in your HOT Captain America spunk!"
scene widowlair06
show widowbjcum03
mc "There you go Scarl... I meant Black Widow!"
wi "Damn! That's a LOT of creamy sperm!"
scene widowlair06
show widowbjcum04
wi "Mmmh, it's so tasty! And as thick as porridge!"
wi "Let me clean myself up... By stuffing all that lovely Captain America spunk down my throat!"
mc "Hurry up, Captain America isn't done with you yet!"
wi "Really? That HUGE dong of yours is still hard? Then I'll have to take care of it..."
scene widowlair07 blurred
show widowprefuck01
wi "That's it, play with my big boobies while I take care of that... MONSTER COCK!"
scene widowlair07 blurred
show widowprefuck02
wi "Mmh, so tasty, I can still smell the salty scent of your previous MEGA-LOAD on the tip!"
scene widowlair07 blurred
show widowprefuck03
wi "*slurp* *slurp* Yummy!"
mc "Fuck, that's so good Black Widow!"
scene widowlair07 blurred
show widowprefuck04
wi "Gee, I wonder where I could stick this MASSIVE fuckstick?"

scene widowlair05 blurred with dissolve
label WidowFuckSlow:
play music "Sounds/massive.mp3"
hide widowfuckfast
show widowfuckslow
call screen widowfuckslow
screen widowfuckslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WidowFuckEnd")    
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WidowFuckFast") 

label WidowFuckFast:
hide widowfuckslow
show widowfuckfast
call screen widowfuckfast
screen widowfuckfast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WidowFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WidowFuckSlow") 
            
label WidowFuckEnd:
wi "Cum for me Captain America!"
stop music
scene widowlair05
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
show widowfuckcum
mc "FUCK! Sssooo fucking GOOOOD!"
wi "I can feel your warm ball-batter all over my back! I LOVE IT!"
mc "I've got more shots for you Black Widow!"
wi "Damn man, you really are a cum machine!"

label WidowEnd01:
show screen mcstats
show screen calendar
scene widowlair01 with fade
show widow01
wi "Well, it took me some time to get cleaned up from all the MASSIVE AMOUNT of cum you plastered my body with Captain America..."
wi "And I must say, I'm so glad that you are BACK with us, Captain America!"
mc "Who's \"us\" exactly?"
hide widow01
show widow03
wi "Well... err. The AVENGERS of course!"
mc "Ah yes, I almost forgot..."
mc "Do any of these dials and screens in this place actually work?"
hide widow03
show widow04
wi "No. It's a set. The set of the Avengers movie I was filming when the Great Nuclear Fuckup War happened."
hide widow04
show widow02
wi "I'm the only survivor because I was stuck in the lavatory with Chris Evans at the time."
mc "Oh, so he died because of beta-radiations then?"
hide widow02
show widow06
wi "No, for another reason. A heart attack while we were... err... trying to get out."
mc "I see..."
hide widow06
show widow03
wi "Don't forget, Captain America, come back anytime, so that together, we can fight for FREEDOM and JUSTICE!"
mc "Yee-hah! Bye Scarl... I mean Black Widow..."
jump DesertStormEnd

label DesertStormAgain:
stop music
scene widowlair01 with fade
show widow03
wi "I like it when you come and visit me Captain America. I feel so alone in this place."
if withmo and missionwi01 and donemissionwi01 == False:
    mc "And this time, I brought along Nancy, who is willing to become Captain Marvel for our cause!"
    mo "Well, hang on a minute sweetie..."
    mc "Come on Nancy, the costume suits you perfectly, you're blond, strong and super...err... developed, you're the perfect match!"
    hide widow03
    show widow02
    wi "I have to agree with [name], you do LOOK a lot like her. A BUSTY version of her anyway."
    mo "Well, thank you for all the compliments. I... Alright, I 'll put it on for you my sweet young man. But I hope I don't become BIGGER like last time."
    mc "No, that would terrible indeed..."
    jump WidowNancy01
if withmo and donemissionwi01:
    mc "You won't feel alone for long Black Widow, Captain Marvel is here to...err... make you feel less alone!"
    mo "Sweetie, I don't know if you should..."
    hide widow03
    show widow02
    wi "Didn't we have a GREAT time on your last visit Captain Marvel?"
    mo "Well... Yes, but..."
    wi "Let's move to my secret SEX lair to get more cozy shall we?"
    mc "Of course, we'll come along Scarlett!"
    jump WidowNancyAgain01
    
hide widow03
show widow02
wi "It makes me feel naughty to be with you. Are you feeling naughty too?"
mc "Of course! VERY naughty..."
wi "Then follow me to my SEX lair!"
hide screen mcstats
hide screen calendar
scene widowroom01 with dissolve
wi "Get fully undressed this time, no need to play games anymore... [name]. \nI'll get into a skimpy outfit for you..."
show scarlett01 with dissolve
wi "So, do you like?"
mc "Fuck YEAH!"
hide scarlett01
show scarlett02
wi "Is that all you have to say?"
mc "Err... You're so sexy Scarlett!"
hide scarlett02
show scarlett03
wi "Is that cock getting HUGE and HARD for me yet?"
mc "Yes, ROCK-HARD for you Scarlett! And for that amazing ass of yours!"
hide scarlett03
scene widowroom02 blurred with fastdissolve
show scarlett03b
wi "Are you going to POUND IT nice and HARD then?..."
mc "For sure, YES, YES!!!"
scene widowroom02 with fastdissolve
show scarlett04
wi "I can't wait... Thinking about that horsecock of yours is making me all WET down there... I just HAVE to take my panties off..."
hide scarlett04
show scarlett05
wi "I'm just imagining it sliding in and out of my TIGHT pussy... stretching me sssooo GOOOD... mmmh..."
scene widowroom03 blurred with fastdissolve
show scarlett06
wi "I think I'm ready now... My pussy hole is gaping and all slippery..."
mc "I can see that..."
label ScarlettFuckChoice:
wi "So, what's next, STUD?"
menu:
    "Let me prep your pussy. With my tongue!" if lustwi >= 3:
        wi "That's a great idea!"
        jump ScarlettLick
    "Get on the edge of the bed, and open up that fuckhole for me!" if lustwi >= 3:
        wi "You're gonna POUND me into the bed [name]? I can't wait..."
        jump ScarlettPound
    "Give me a blowjob...":
        wi "What a NAUGHTY boy!"
        jump ScarlettBlowjob
    "Get on all fours...":
        jump ScarlettFuck
    "I'd say we're done for the day..." if scarlettfuck or scarlettblow:
        jump ScarlettEnd
        
label ScarlettLick:
scene widowroom07 with dissolve
show widowlick01
wi "Isn't my pussy just ssooo tasty [name]?!"
mc "Sure is. *lick* Scarlett. *lick*"
hide widowlick01
show widowlick02 with fastdissolve
wi "I can tell you're enjoying it, your tongue is slurping up all my juices. You are such a NAUGHTY boy!!"
mc "I'm getting a meal anf a half there. * slurp* Your pussy is so wet... *slurp*"
scene widowroom03 blurred
show widowlick03
wi "And ready for what's coming NEXT!"
jump ScarlettFuckChoice

label ScarlettPound:
scene widowroom09 with dissolve
show scarlettprepound01
wi "I can feel that GIANT piece of manmeat teasing my clit. Please, fuck me [name], I can't stand it!"
mc "Alright, open up, I'm gonna pummel you with my monster shaft!"
scene widowroom08 blurred
show scarlettprepound02
wi "Oh shit, just your massive cockhead is STRETCHING me so much. But I can take it don't worry, so just FUCK ME HARD, STUD!"
label ScarlettPoundSlow:
scene widowroom09
play music "Sounds/scarlettpound.mp3"
hide widowpoundfast
show widowpoundslow
call screen scarlettpoundslow
screen scarlettpoundslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ScarlettPoundEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ScarlettPoundFast") 

label ScarlettPoundFast:
hide widowpoundslow
show widowpoundfast
call screen scarlettpoundfast
screen scarlettpoundfast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ScarlettPoundEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ScarlettPoundSlow") 

label ScarlettPoundEnd:
stop music
$ scarlettpound = True
scene widowroom08 blurred
show widowpoundcum01
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
wi "YES, fill me up like a cumdump [name]! I just LOVE cum and YOU cum ssooo much!!"
mc "Fuck, it's spilling out all over the place!"
wi "Pull out and cover my body with the rest of your MEGA-LOAD!!"
hide widowpoundcum01
show widowpoundcum02
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Sure, I've got plenty more! RHAAA!"
wi "Damn it man, how do you manage to always deliver such GIANT loads? I'm CAKED in your rich creamy ball-batter!"
mc "You bring the best out of me I guess... Now, where did we leave off?"
jump ScarlettFuckChoice

label ScarlettFuck:
scene widowroom06 with dissolve
show scarlettprefuck
wi "Are you going to pile-drive that titanic rod in me?"
mc "Yep..."
wi "FUCK ME HARD! GIVE ME YOUR MONSTER MANMEAT YOU MUSCLE STUD!"
mc "Full steam ahead Scarlett!"
scene widowroom05 with dissolve
label ScarlettFuckSlow:
play music "Sounds/scarlettpound.mp3"
hide scarlettfuckfast
show scarlettfuckslow
call screen scarlettfuckslow
screen scarlettfuckslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ScarlettFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ScarlettFuckFast") 

label ScarlettFuckFast:
hide scarlettfuckslow
show scarlettfuckfast
call screen scarlettfuckfast
screen scarlettfuckfast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ScarlettFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ScarlettFuckSlow") 

label ScarlettFuckEnd:
stop music
$ scarlettfuck = True
hide scarlettfuckslow
hide scarlettfuckfast
show scarlettfuck00b
show scarlettfuckcum01
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
wi "Oh my God, your cumshots are SSOO POWERFUL! I can feel every single one of them!"
mc "And your pussy is already full to the brim!"
wi "Come all over my back now, there is no cum inflation tag in this game. YET."
hide scarlettfuckcum01
hide scarlettfuck00b
show scarlettfuckcum02
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Sure, I've got plenty more! RHAAA!"
jump ScarlettFuckChoice

label ScarlettBlowjob:
if scarlettfuck == True:
    wi "Let me take care of that cock of yours to KEEP IT ROCK-HARD for ANOTHER round!"
if scarlettfuck == False:
    wi "Let me take care of that cock of yours..."

scene widowroom04
show scarlett07 with fastdissolve
if scarlettfuck == True:
    mc "You want some more monster dick Scarlett?"
    wi "Yes I do... I want more... of that GIANT MANMEAT of yours! It's so fucking heavy and MASSIVE..."
if scarlettfuck == False:
    wi "It's bigger than my head... So fucking heavy and MASSIVE..."

hide scarlett07
show scarlett08 with fastdissolve
wi "Let me worship it... Lick it ALL OVER... slowly and sensuously..."
mc "Fuck! You're making me so hard!"
wi "And then..."
label ScarlettBlowSlow:
scene scarlettblowbackground with dissolve
hide scarlettblowfast
show scarlettblowslow
call screen scarlettblowslow
screen scarlettblowslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ScarlettBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ScarlettBlowFast") 

label ScarlettBlowFast:
hide scarlettblowslow
show scarlettblowfast
call screen scarlettblowfast
screen scarlettblowfast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ScarlettBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ScarlettBlowSlow") 

label ScarlettBlowEnd:
$ scarlettblow = True
wi "Fill up my throat!"
scene scarlettblowbackground
show scarlettblow07
show scarlettblowcum01
mc "AAAH!"
hide scarlettblow07
hide scarlettblowcum01
show scarlettblowcum02
wi "My God, you cum like a STALLION! My stomach is full and... THIS???"
mc "Alpha-radiated cum is always nourishing and plentiful!"
jump ScarlettFuckChoice

label ScarlettEnd:
scene widowroom01 with dissolve
show scarlett09
wi "I sure enjoyed this little Avengers get-to-know-each-other-better session Captain America!"
call LustPlusWidow
mc "Yeah, it was great getting to know you in... more depth, Black Widow!"
if lustwi == 4:
    wi "I think it is time for us to recruit more super-heroes to our cause. I found a Captain Marvel costume on the set..."
    mc "Oh, great, that's a female character, right?"
    hide scarlett09
    show scarlett10 with fastdissolve
    wi "Yes indeed. And the costume is for a SUPER-BUSTY woman. Not quite sure why they made it that way, they certainly didn't find the right actress for it..."
    wi "So YOUR task is to recruit a woman who would fit the bill. And bring her to the Avengers' lair so she can fight with us for FREEDOM and JUSTICE!"
    window hide
    show missionwi01 at posmission
    $ renpy.pause(4.0, hard=True)
    hide missionwi01
    $ missionwi01 = True
    $ marvelcostume = True
    mc "Yeah, FREEDOM and JUSTICE!"
    hide scarlett10
    show scarlett09 with fastdissolve
    wi "Oh, and by the way, the costume was exposed to alpha-radiations for a long time I'm warning you..."
if withbe:
    mc "I'd better get going now, Bella is probably looking for me..."
if withpe:
    mc "I'd better get going now, Penny is probably looking for me..."
$ scarlettfuck = False
$ scarlettblow = False
show screen mcstats
show screen calendar
jump DesertStormEnd

label WidowNancy01:
hide screen mcstats
hide screen calendar
show widow02 at right with move
hide widow02
show widow07 at right
show nancymarvel08 at left with moveinleft
wi "Oh wow, your landlady looks AMAZING in that outfit! We definitely have a new Captain Marvel fighting alongside the AVENGERS!"
mo "Well, I don't really know how to fight..."
hide nancymarvel08
hide widow07
show widownancy01
with fastdissolve
wi "Don't worry about it, the mere sight of a super-hero makes our enemies tremble with FEAR!"
mo "Well, I hope you are right Ms Black Widow..."
wi "Call me Scarlett... And your civilian name, Captain Marvel?"
mo "Nancy... Well, you certainly look a lot like the REAL Scarlett Johannson..."
wi "Maybe I am... *wink*"
hide widownancy01
show widownancy02
with fastdissolve
wi "So what do you think Captain America? Do we form a great team or what?"
mc "I say the BEST team of...err... busty super-heroes!"
wi "Speaking of which, Nancy has such a huge pair, I just need to check them out... They're even bigger than mine and I've never met someone with breasts larger than my 32GGG."
mo "Well...err... I don't know... I've never..."
mc "It's part of the team bonding procedure that the Black Widow put in place Nancy. Just go with the flow."
mo "Alright sweetie..."
scene widowlair02 blurred
show widownancy03
with fastdissolve
wi "Mmmmh, you could certainly SMOTHER TO DEATH your enemies between that deep cleavage..."
mo "Uhm, I don't... You think so Scarlett?"
wi "Of course Nancy... Let me check out more of that HOT BOD of yours..."
mo "Hang on, I feel... It's happening again [name]!"
hide widownancy03
show widownancy04
with fastdissolve
wi "Oh WOW! Nancy, your muscles... And your tits! They're getting even BIGGER!"
mo "Yes, it's those alpha-rays that are doing it! I want it to stop! Please help me Black Widow."
wi "I have no idea what to do quite frankly. But I'm mesmerized..."
window hide
show widownancy04 at right with move
show mcamerica01 at left with moveinleft
mc "Captain America to the rescue!"
hide widownancy04
show widownancy05 at right
with fastdissolve
mo "And what do you plan to achieve with that GIANT erect cock, [name]? This is no time for hanky-panky sweetie! I need HELP!"
hide mcamerica01
show mcamerica02 at left
with fastdissolve
mc "My alpha-radiated cum will negate the effects of those alpha-rays laced in your outfit. Trust me, it makes perfect sense."
mo "It doesn't make any sense at all but I am so desperate, I am willing to give it a try..."
wi "I can certainly help you now Captain Marvel. I'll take care of his massive bull-balls and you can take care of his cock."
scene widowlair03 blurred with dissolve
show widownancymc01
mc "Yes, prep my balls Black Widow, make sure they are churning TONS of alpha-radiated cum... Mmmh, that's good Captain Marvel, you tongue feels so good..."
mc "Now use both your hands. Both of you. That will make me come quickly so I can rescue Captain Marvel from this evil spell as fast as possible!"
scene widowlair02 blurred
play music "Sounds/wank.mp3"
label WidownancyHJSlow:
hide widownancyhjfast
show widownancyhjslow
call screen widownancyhjslow01
screen widownancyhjslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WidownancyHJEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WidownancyHJFast") 

label WidownancyHJFast:
hide widownancyhjslow
show widownancyhjfast
mc "Yes, FASTER!"
call screen widownancyhjfast01
screen widownancyhjfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WidownancyHJEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WidownancyHJSlow") 

label WidownancyHJEnd:
mc "Yes, you're making me cum! Get ready Nancy!"
mo "Please do try and aim your pint-sized shots at my costume sweetie pie..."
hide widownancyhjslow
hide widownancyhjfast
show widownancyhjcum01
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
wi "It's flying EVERYWHERE! You'll definitely get some on your costume Captain Marvel!"
mo "I hope it's a LOT if this ever has a chance to work..."
scene widowlair05 blurred with fastdissolve
show widownancyhjcum02
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
wi "That's it, blast that young virile goo all over her, Captain America!"
mc "Keep still Nancy, I've got more ropes of cum to deliver flying right at you! AAAH!"
scene widowlair05 blurred with fastdissolve
show widownancyhjcum03
mo "Oh, it doesn't seem to have done anything... I should have guessed, this was the dumbest idea ever!"
mc "I think it was worth a shot. A cumshot that is."
mo "I'll get out of this cursed costume, I know this will work at least..."
scene widowlair01 with fastdissolve
show widowmcnancy01 at left
show widonancyaftercumb at right with moveinright
mo "There, I feel much better now. And I'm all cleaned up too."
wi "But Captain America is still rock-hard and drooling tons of cum on MY costume now."
wi "I think we should move to my SEX lair to take care of his monstrous erection that never goes down."
jump WidowNancyRoom01

label WidowNancyAgain01:
$ widowmomagain = True
hide screen mcstats
hide screen calendar
label WidowNancyRoom01:
scene widowroom01 with dissolve
show scarlett11 at midright with moveinright
show nancypurple01 at midleft with moveinleft
wi "Let's see what you have in store for us [name]..."
mc "You both look so hot, it's hard to decide. Maybe you can play with each other a bit while I make up my mind..."
mo "Alright sweetie, I'm getting so horny that I DO want to taste some super-hero pussy!"
scene widowroom01 blurred with fastdissolve
show scarlettnancy01
wi "And I want to taste those succulent lips. Kiss me Nancy..."
play sound "Sounds/kiss.mp3"
mc "*Damn, they're going full-lesbian on me...*"
hide scarlettnancy01
show scarlettnancy02
wi "And those MASSIVE nipples..."
mo "Mmh, yes... AAAH."
scene widowroom11 blurred with fastdissolve
show scarlettnancy03
wi "And finally, that tasty super-hero pussy..."
mo "Oh... Scarlett, I..."
wi "Let's move on to the bed Captain Marvel, shall we?"
mc "I'll sit in the armchair, don't mind me..."
scene widowroom05 with fastdissolve
show scarlettnancy04
play sound "Sounds/kiss.mp3"
mo "Aah, Scarlett, this is..."
hide scarlettnancy04
show scarlettnancy05
with fastdissolve
play sound "Sounds/kiss.mp3"
mo "You lick my pussy so well...Oooh!"
play sound "Sounds/kiss.mp3"
mo "Now it's my turn to return the favor..."
hide scarlettnancy05
show scarlettnancy06
with fastdissolve
wi "You're so kinky Nancy...Mmmh."
mo "You ain't seen nothing yet Scarlett."
scene widowroom03 blurred with fastdissolve
show scarlettnancy07
wi "Oh my God [name]! Your landlady... She's twirling her tongue on my pussy... Ooooh!"
mc "Maybe it's time I get it on with the action. Come over here my super-hero teammates and suck on my heroic love sword!"
scene widowroom04 blurred  with fastdissolve
show widownancysuck01
mc "Yes, that's it, lick the vast surface of my mammoth dong..."
window hide
play sound "Sounds/lick.mp3"
hide widownancysuck01
show widownancysuck02
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide widownancysuck02
show widownancysuck01
$ renpy.pause(0.2, hard=True)
hide widownancysuck01
show widownancysuck02
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide widownancysuck02
show widownancysuck01
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide widownancysuck01
show widownancysuck02
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide widownancysuck02
show widownancysuck01
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide widownancysuck01
show widownancysuck02
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide widownancysuck02
show widownancysuck01
with fastdissolve
$ renpy.pause(0.2, hard=True)
wi "It's ssoo BIG Captain America, I don't even know where to begin."
mc "Well, I know where to begin. Get on the bed both of you, I'll fuck you in turns and feel you up each with some warm spunk!"
mo "Mmh, you're such a STUD Captain America!"
$ momcum = 0
$ widowcum = 0
scene widownancyprefuck01 with dissolve
mc "I think I'm gonna start with you Captain Nancy. Err, I mean Captain Marvel."
mo "Ooh, YES please Captain America!"
scene widownancyprefuck02 with dissolve
mc "There, the head is almost in, just open really WIDE..."
mo "I'm trying... Just shove it in sweetie pie!"
mc "Alright, here we go!"
scene widowroom13 blurred with dissolve
label WidownancyFuckaSlow:
stop music
play music "Sounds/womansex02.mp3"
hide widownancyacum01
hide widownancyacum02
hide widownancyfuckafast
hide widownancyfuckbfast
hide widownancyfuckbslow
hide widownancyfuckcfast
hide widownancyfuckdfast
hide widownancyfuckcslow
hide widownancyfuckdslow
show widownancyfuckaslow
call screen widownancyfuckaslow01
screen widownancyfuckaslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckaEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WidownancyFuckaFast") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckbSlow") 

label WidownancyFuckaFast:
stop music
play music "Sounds/womansex02.mp3"
hide widownancyacum01
hide widownancyacum02
hide widownancyfuckaslow
hide widownancyfuckbfast
hide widownancyfuckbslow
hide widownancyfuckcfast
hide widownancyfuckdfast
hide widownancyfuckcslow
hide widownancyfuckdslow
show widownancyfuckafast
call screen widownancyfuckafast01
screen widownancyfuckafast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckaEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WidownancyFuckaSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckbSlow") 


label WidownancyFuckcSlow:
stop music
play music "Sounds/womansex02.mp3"
hide widownancyccum01
hide widownancyccum02
hide widownancyfuckaslow
hide widownancyfuckbfast
hide widownancyfuckbslow
hide widownancyfuckcfast
hide widownancyfuckdfast
show widownancyfuckcslow
hide widownancyfuckdslow
hide widownancyfuckafast
call screen widownancyfuckcslow01
screen widownancyfuckcslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckcEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WidownancyFuckcFast") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckdSlow") 

label WidownancyFuckcFast:
stop music
play music "Sounds/womansex02.mp3"
hide widownancyccum01
hide widownancyccum02
hide widownancyfuckaslow
hide widownancyfuckbfast
hide widownancyfuckbslow
show widownancyfuckcfast
hide widownancyfuckdfast
hide widownancyfuckcslow
hide widownancyfuckdslow
hide widownancyfuckafast
call screen widownancyfuckcfast01
screen widownancyfuckcfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckcEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WidownancyFuckcSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckdFast") 

    
label WidownancyFuckbSlow:
stop music
play music "Sounds/womansex01.mp3"
hide widownancywidowcumb03
hide widownancywidowcumd03
hide widownancyfuckaslow
hide widownancyfuckbfast
hide widownancyfuckcfast
hide widownancyfuckdfast
hide widownancyfuckcslow
hide widownancyfuckdslow
hide widownancyfuckafast
show widownancyfuckbslow
call screen widownancyfuckbslow01
screen widownancyfuckbslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckbEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WidownancyFuckbFast") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckaSlow") 

label WidownancyFuckbFast:
stop music
play music "Sounds/womansex01.mp3"
hide widownancywidowcumb03
hide widownancywidowcumd03
hide widownancyfuckaslow
hide widownancyfuckcfast
hide widownancyfuckdfast
hide widownancyfuckcslow
hide widownancyfuckdslow
hide widownancyfuckafast
hide widownancyfuckbslow
show widownancyfuckbfast
call screen widownancyfuckbfast01
screen widownancyfuckbfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckbEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WidownancyFuckbSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckaFast") 

label WidownancyFuckdSlow:
stop music
play music "Sounds/womansex01.mp3"
hide widownancywidowcumb03
hide widownancywidowcumd03
hide widownancyfuckaslow
hide widownancyfuckcfast
hide widownancyfuckdfast
hide widownancyfuckcslow
hide widownancyfuckbslow
hide widownancyfuckafast
hide widownancyfuckbfast
show widownancyfuckdslow
call screen widownancyfuckdslow01
screen widownancyfuckdslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckdEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WidownancyFuckdFast") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckcSlow") 

label WidownancyFuckdFast:
stop music
play music "Sounds/womansex01.mp3"
hide widownancywidowcumb03
hide widownancywidowcumd03
hide widownancyfuckaslow
hide widownancyfuckcfast
hide widownancyfuckbfast
hide widownancyfuckcslow
hide widownancyfuckdslow
hide widownancyfuckafast
hide widownancyfuckbslow
show widownancyfuckdfast
call screen widownancyfuckdfast01
screen widownancyfuckdfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckdEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WidownancyFuckdSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckcFast") 


label WidownancyFuckaEnd:
mo "You're pounding me so good sweetie pie, it's time for you to COME INSIDE ME!"
stop music
hide widownancyfuckaslow
hide widownancyfuckafast
show widownancyacum01
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "I'm filling you up Nancy, AAAH!"
mo "AAAH, I can feel it PULSING inside me, I'm cumming with you!!!"
hide widownancyacum01
show widownancyacum02
mc "Take some more shots on your back, RHAAAA!"
mo "Oh my God sweetie pie, your loads... They are so BIG for me!"
mc "Phew... I'm still hard so I'm going to fuck you some more!"
mo "What? You're such a SUPER-STUD for me [name]. Fuck me again HARD!"
hide widownancyacum02
$ momcum += 1
jump WidownancyFuckcSlow

label WidownancyFuckcEnd:
mo "You're pounding me so good sweetie pie, it's time for you to COME INSIDE ME!"
stop music
hide widownancyfuckcslow
hide widownancyfuckcfast
show widownancyccum01
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "I'm filling you up Nancy, AAAH!"
mo "AAAH, I can feel it [name], I'm cumming with you!!!"
hide widownancyccum01
show widownancyccum02
mc "Take some more shots on your back, RHAAAA!"
mo "Oh my God sweetie pie, AGAIN? You're just a CUM-MACHINE aren't you?"
$ momcum += 1
if momcum >= 2 and widowcum >= 2:
    jump WidownancyFuckAllEnd
mc "Phew... I'm still hard so I'm going to fuck you some more Nancy! Get ready for the pounding of your life!"
mo "Oh, I AM ready. Ready to take on my tenant's MONSTERCOCK once more!"
hide widownancyccum02
jump WidownancyFuckcSlow

label WidownancyFuckbEnd:
if widowcum == 0:
    wi "Let it loose, Captain America! My hungry pussy WANTS a MEGA-LOAD of cream!"
if widowcum >= 1:
    wi "Let it loose, Captain America! My hungry pussy wants ANOTHER MEGA-LOAD of cream!"
stop music
hide widownancyfuckbslow
hide widownancyfuckbfast
show widownancywidowcumb01
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
if widowcum == 0:
    wi "There you go Black Widow, one MEGA-LOAD coming your way! AAAH!"
if widowcum >= 1:
    mc "There you go Black Widow, another MEGA-LOAD coming your way! AAAH!"
wi "AAAH, I can feel it PULSING inside me, I'm cumming with you!!!"
hide widownancywidowcumb01
show widownancywidowcumb02
mc "Take some more shots till you're bloated with my seed, RHAAAA!"
hide widownancywidowcumb02
show widownancywidowcumb03
$ widowcum += 1
if momcum >= 2 and widowcum >= 2:
    jump WidownancyFuckAllEnd
mc "Phew... I'm still hard so I'm going to fuck you some more Black Widow! Get ready to receive Captain's America's SUPERHERO cock!"
hide widownancywidowcumb03
if momcum == 1:
    jump WidownancyFuckdSlow
if momcum == 0:
    jump WidownancyFuckbSlow

label WidownancyFuckdEnd:
if widowcum == 0:
    wi "Let it loose, Captain America! My hungry pussy WANTS a MEGA-LOAD of cream!"
if widowcum >= 1:
    wi "Let it loose, Captain America! My hungry pussy wants ANOTHER MEGA-LOAD of cream!"
stop music
hide widownancyfuckdslow
hide widownancyfuckdfast
show widownancywidowcumd01
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
if widowcum == 0:
    wi "There you go Black Widow, one MEGA-LOAD coming your way! AAAH!"
if widowcum >= 1:
    mc "There you go Black Widow, another MEGA-LOAD coming your way! AAAH!"
mc "There you go Black Widow, another MEGA-LOAD coming your way! AAAH!"
wi "AAAH, I can feel it PULSING inside me, I'm cumming with you!!!"
hide widownancywidowcumd01
show widownancywidowcumd02
mc "Take some more shots till you're bloated with my seed, RHAAAA!"
hide widownancywidowcumd02
show widownancywidowcumd03
$ widowcum += 1
if momcum >= 2 and widowcum >= 2:
    jump WidownancyFuckAllEnd
mc "Phew... I'm still hard so I'm going to fuck you some more Black Widow! Captain America's superhero BULLBALLS are not done with you!"
wi "Oh my God, with such stamina, you could FUCK our enemies to DEATH Captain America!"
hide widownancywidowcumd03
if momcum == 1:
    jump WidownancyFuckdSlow
if momcum == 0:
    jump WidownancyFuckbSlow

label WidownancyFuckAllEnd:
$ weekfuckedmom = True
mc "Phew, you drained so many loads from my balls..."
mo "I'm sssoo proud of you [name]. You just came and came and came again, I thought you just wouldn't STOP!"
if widowmomagain == False:
    call LustPlusNancy
wi "And you just showed us why you DESERVE to be Captain America... Captain America."
scene widowroom01 with dissolve
show scarlett11 at midright with moveinright
show nancypurple01 at midleft with moveinleft
$ momcum = 0
$ widowcum = 0
if withbe:
    mo "I think it's time we got cleaned up, Bella is probably worried sick by now..."
if withpe:
    mo "I think it's time we got cleaned up, Penny is probably worried sick by now..."
mc "I guess you're right. Let's go."
wi "Don't forget about me. Come back to visit me often BOTH of you! *wink*"
call LustPlusWidow
if lustwi >= 5 and jakepassword == False:
    hide scarlett11
    show scarlett09 at midright
    with fastdissolve
    wi "Oh, and by the way, you might be interested in the secret Road Warrior password which I overheard during one of my outings fighting for FREEDOM and JUSTICE."
    $ jakepassword = True
    mc "Yes, what is it?"
    wi "It's... \"Gazoonka\"."
    mc "Gazooka? That's it?"
    wi "Yes, that's it. But only use it if you ever become a Road Warrior. I tried to use it once, and I was found out, sicne I'm not a Road Warrior, I am an AVENGER!"
show screen mcstats
show screen calendar
$ donemissionwi01 = True
jump DesertStormEnd