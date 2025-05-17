label HaremInterface:
hide screen calendar
hide screen mcstats
scene bedroom01 with dissolve
if mcbike == False:
    jump HaremNext
if mcbike:
    call screen bikeinterface
    screen bikeinterface:
        add "Explore02/mcbikeupkeep.png" at posupkeep
        modal True
        imagebutton:
            focus_mask True
            idle "Explore02/noupkeep.png"
            hover "Explore02/noupkeep.png"
            action [SetVariable('bikepaid', False), Jump ("HaremNext")] 
        imagebutton:
            focus_mask True
            idle "Explore02/upkeep.png"
            hover "Explore02/upkeep.png"
            action [SetVariable('bikepaid', True), Jump ("HaremNextPre")]

label HaremNextPre:
$ money -= 5
label HaremNext:
show screen calendar
show screen mcstats
if pregza:
    $ maintenanceza = True
    if money >= 5:
        $ money -= 5
    "Zara is maintained in your harem at a cost of $5 if you have them."
if pregan:
    $ maintenancean = True
    if money >= 5:
        $ money -= 5
    "Angie is maintained in your harem at a cost of $5 if you have them."
if pregmo:
    $ maintenancemo = True
    if money >= 5:
        $ money -= 5
    "Nancy is maintained in your harem at a cost of $5 if you have them."
if pregmi:
    $ maintenancemi = True
    if money >= 5:
        $ money -= 5
    "Michiko is maintained in your harem at a cost of $5 if you have them."
if pregam:
    $ maintenanceam = True
    if money >= 5:
        $ money -= 5
    "Amy is maintained in your harem at a cost of $5 if you have them."
if preggw:
    $ maintenancegw = True
    if money >= 5:
        $ money -= 5
    "Gwen is maintained in your harem at a cost of $5 if you have them."
if pregay:
    $ maintenanceay = True
    if money >= 5:
        $ money -= 5
    "Ayla is maintained in your harem at a cost of $5 if you have them."
if pregla:
    $ maintenancela = True
    if money >= 5:
        $ money -= 5
    "Laurie is maintained in your harem at a cost of $5 if you have them."
if pregba:
    $ maintenanceba = True
    if money >= 5:
        $ money -= 5
    "Barbara is maintained in your harem at a cost of $5 if you have them."
if pregza:
    $ pregzastart += 1
if pregan:
    $ preganstart += 1
if pregmi:
    $ pregmistart += 1
if pregmo:
    $ pregmostart += 1
if pregam:
    $ pregamstart += 1
if preggw:
    $ preggwstart += 1
if pregay:
    $ pregaystart += 1
if pregla:
    $ preglastart += 1
if pregba:
    $ pregbastart += 1
window hide
if pregzastart == 8:
    show zarapregnant04 with moveinleft
    za "I will become a MOTHER any minute now. And you, a FATHER!"
    if mcchildren >= 1:
        mc "Been there, done that."
        za "Well, not ME! So take me to the medbay please, I.... QUICK!"
        mc "Sure, I already know the way to the maternity ward actually...."
        jump ZaraBirth
    mc "What? You mean, it's... happening?"
    hide zarapregnant04 
    show zarapregnant04b
    with fastdissolve
    za "YES! So take me to the medbay please, I.... QUICK!"
    mc "Alright, alright, err... Do you know the way to the maternity ward?"
    za "It's just the same as the medbay!"
    label ZaraBirth:
    scene zarapreggo05 with fade
    play music "Sounds/beep.mp3"
    play sound "Sounds/debrasex.mp3"
    ta "Push, Zara, PUSH!"
    scene zarapreggo05b with dissolve
    play sound "Sounds/womanscream.ogg"
    ta "Go on, I can see its head!"
    play sound "Sounds/Plop.mp3"
    ra "There you go, well done Zara!"
    call LustPlusZara
    mc "Is it a boy or a girl?"
    stop music
    scene birthbackground
    show tarazarababy 
    with dissolve
    play sound "v06/babycrying.mp3"
    ta "It's a girl!"
    za "I will call her Aisha."
    $ babyzara = True
    call MCbabies
    $ pregza = False
    $ sawbirth = True
    mc "That birth was exhausting... I should go back to my bedroom and leave my child here, like a good harem master would do."
    scene bedroom01 with dissolve
    $ pregzastart = 0
    jump HaremNextAngie
if pregzastart == 6:
    show zarapregnant03 with moveinleft
    za "I NEED to feed our baby, find me some... camel burgers! LOTS of them!"
    mc "You know, it has been proven that a pregnant woman isn't actually eating for tw..."
    hide zarapregnant03
    show zarapregnant03b 
    with fastdissolve
    za "SHUT UP and get me some BURGERS!"
    mc "Sure, sure, I'll go to the kitchen and get you some. But please go back to your bedroom and have a rest... *Gee, good thing this pregnancy is moving really FAST...*"
    hide zarapregnant03b with fastdissolve 
    jump HaremNextAngie
if pregzastart == 4:
    show zarapregnant02 with moveinleft
    za "Praise be to Allah! The baby is growing HEALTHILY inside me!"
    if mcchurch == 5:
        mc "My child will not grow into HERESY! Praise be to the Phallus Lord!"
        hide zarapregnant02
        show zarapregnant02b
        with fastdissolve
        za "Do not trigger the Prophet's wrath! He'll accept our child as he or she will be."
        mc "Well, not the Phallus Lord. He's not the same kind of tolerant prophet, so there!"
        call LustMinusZara
        za "I will pray to Allah for His forgiveness...."
        mc "Yeah, you do that. Whatever."
    if mcchurch <= 4:
        mc "Yeah, thanks to be my SUPERIOR American seed."
        hide zarapregnant02
        show zarapregnant02b
        with fastdissolve
        za "Which my FERTILE womb happily received."
        mc "Ah yeah, I see your point now. It takes two to tango."
        za "And to make a baby..."
    hide zarapregnant02b with fastdissolve
    jump HaremNextAngie
if pregzastart == 2:
    show zarapregnant01 with moveinleft
    za "[name], I'm pregnant, look!"
    mc "You're sure you're not just getting fat from all those camel burgers?"
    hide zarapregnant01
    show zarapregnant01b
    with fastdissolve
    za "Yes, I am SURE. Women KNOW when they are PREGNANT."
    mc "Ah, then... err... Congratulations on doing your bit to re-populate the world!"
    hide zarapregnant01b with fastdissolve
    jump HaremNextAngie
label HaremNextAngie:
window hide
if preganstart == 8:
    show angiepregnant04a with moveinleft
    an "[name], something's happening inside of me, I'm scared!"
    mc "Don't worry about it, it's just the baby growing, perfectly normal, it's call gestation."
    hide angiepregnant04a 
    show angiepregnant04b
    with fastdissolve
    an "But I mean... Something DIFFERENT! It's trying to GET OUT!"
    mc "Damn fetuses tend to do that. Normally after 9 months, but only 8 weeks nowadays, what with my superior sperm. I'll take you to the medbay then."
    hide angiepregnant04b 
    show angiepregnant04a
    with fastdissolve
    an "The... the medbay? I'm scared. Please tell me everything will be fine!"
    mc "With the amount of female juices you can squirt, I'm sure it'll pop out easily. So let's go."
    scene angiepregnant05a with fade
    play music "Sounds/beep.mp3"
    play sound "Sounds/debrasex.mp3"
    ta "Push, Angie, PUSH!"
    scene angiepregnant05b with dissolve
    play sound "Sounds/womanscream.ogg"
    ta "Go on, I can see its head!"
    play sound "Sounds/Plop.mp3"
    ra "There you go, well done Angie! That one sure came out easy in just a single pop."
    call LustPlusAngie
    mc "Told you so... Is it a boy or a girl?"
    stop music
    scene birthbackground
    show taraangiebaby 
    with dissolve
    play sound "v06/babycrying.mp3"
    ta "It's a girl!"
    an "I will call her Dolly."
    ra "You think she'll have HUGE tits like me then?"
    an "No! It's because she's my doll..."
    $ babyangie = True
    call MCbabies
    $ pregan = False
    $ sawbirth = True
    mc "That birth was exhausting... I should go back to my bedroom and leave my child here, like a good harem master would do."
    scene bedroom01 with dissolve
    $ preganstart = 0
    jump HaremNextNancy
if preganstart == 6:
    show angiepregnant03a with moveinleft
    an "I'm starting to regret getting a doll with you. This baby is going to be HUGE! Even bigger than me at this rate..."
    mc "I think it's almost ready to come out, don't worry."
    hide angiepregnant03a
    show angiepregnant03b 
    with fastdissolve
    an "And how is it going to come out of me??? My pussyhole is so tiny..."
    mc "Well, it took my monstercock without any problem, and that's almost as big as a baby's head."
    hide angiepregnant03b with fastdissolve 
    jump HaremNextNancy
if preganstart == 4:
    show angiepregnant02a with moveinleft
    an "Look [name], the baby is growing! When I find my mom and dad, I'll tell them they're gonna have a baby granddoll!"
    mc "Sure, sure, they'll be thrilled."
    hide angiepregnant02a
    show angiepregnant02b
    with fastdissolve
    an "Just like you, right? I mean, as thrilled as you are, you're SUPER-thrilled, aren't you?"
    mc "Oh yeah, big-time thrilled. Like totally into getting a nursery of expensive babies to maintain. Right on."
    an "YIPPEE, I'm so glad to hear that!"
    hide angiepregnant02b with fastdissolve
    jump HaremNextNancy
if preganstart == 2:
    show angiepregnant01a with moveinleft
    an "I think you did put a doll in me, look!"
    mc "Ah yes, I see now. It's subtle, but it's only been two weeks."
    hide angiepregnant01a
    show angiepregnant01b
    with fastdissolve
    an "What if I push my belly out like that? Can you see it better now?"
    mc "Err...Yeah, I can. Thank you. Just what I wanted to see when I woke up this morning."
    an "You're such an ACE future dad, [name]. Bye!"
    hide angiepregnant01b with fastdissolve
    jump HaremNextNancy
label HaremNextNancy:
window hide
if pregmostart == 8:
    show nancypregnant04 with moveinleft
    mo "Oh, sweetie pie... I'm absolutely BURSTING! I think... I need to go to the medbay NOW!"
    mc "What? You mean, it's... happening?"
    mo "YES, It's fucking happening! Now take me to the medbay you lousy father!"
    mc "Alright, alright, gee, pregnant women are just so... angry."
    scene nancypreggo05 with fade
    play music "Sounds/beep.mp3"
    play sound "Sounds/debrasex.mp3"
    ta "Push, Nancy, PUSH!"
    scene nancypreggo05b with dissolve
    play sound "Sounds/womanscream.ogg"
    ta "Go on, I can see its head!"
    play sound "Sounds/Plop.mp3"
    ra "There you go, well done Nancy!"
    call LustPlusNancy
    mc "Is it a boy or a girl?"
    stop music
    scene birthbackground
    show taranancybaby 
    with dissolve
    play sound "v06/babycrying.mp3"
    ta "It's a girl!"
    mo "I will call her Heather."
    $ babynancy = True
    call MCbabies
    $ sawbirth = True
    $ pregmo = False
    mc "That birth was exhausting... I should go back to my bedroom and leave my child here, like a good harem master would do."
    scene bedroom01 with dissolve
    $ pregmostart = 0
    jump HaremNextAmy
if pregmostart == 6:
    show nancypregnant03 with moveinleft
    mo "Your landlady is really getting BIG. Even my fat tits are getting bigger! This baby is going to be very-well FED!"
    mc "Well, I wouldn't mind having a..."
    hide nancypregnant03
    show nancypregnant03b
    with fastdissolve
    mo "It's for the BABY! ONLY FOR HIM! Now get me some strawberries. I WANT some strawberries! With whipped cream."
    mc "Sure, sure, I'll go to the kitchen and get you some. But please go back to your bedroom and have a rest... *Gee, good thing this pregnancy is moving really FAST...*"
    hide nancypregnant03b with dissolve
    jump HaremNextAmy
if pregmostart == 4:
    show nancypregnant02 with moveinleft
    mo "Look sweetie pie! My belly is really starting to GROW! I can already feel the baby kicking his tiny feet inside me!"
    mo "I sure HOPE it's a BOY! A BIG boy!..."
    mc "You mean big as in healthy and all that obviously. Nothing else."
    hide nancypregnant02
    show nancypregnant02b
    with fastdissolve
    mo "Well, of course, what kind of filthy depraved future mother do you think I am?"
    hide nancypregnant02b with dissolve
    jump HaremNextAmy
if pregmostart == 2:
    show nancypregnant01 with moveinleft
    mo "Look, honey! I'm starting to get pregnant. With YOUR baby!"
    mc "What? But, it's only been two weeks!"
    hide nancypregnant01
    show nancypregnant01b
    with fastdissolve
    mo "That means your alpha-radiated super-virile sperm is really working WONDERS."
    mo "I'll be giving birth to a healthy young baby in no time!"
    hide nancypregnant01b with dissolve
    jump HaremNextAmy
label HaremNextAmy:
window hide
if pregamstart == 8:
    show amypreggo04 with moveinleft
    am "Please [name], I'm SCARED! Hold me in your strong arms and tell me everything will be alright..."
    mc "Of course Amy."
    hide amypreggo04
    show amypreggo04b
    with fastdissolve
    mc "There, there, everything will be fi..."
    play sound "Sounds/splooge02.mp3"
    am "My waters broke, Quick, take me to the medbay, I'm about to give birth!"
    scene amypreggo05 with fade
    play music "Sounds/beep.mp3"
    play sound "Sounds/debrasex.mp3"
    ta "Push, Amy, PUSH!"
    scene amypreggo05b with dissolve
    play sound "Sounds/womanscream.ogg"
    ta "Go on, I can see its head!"
    play sound "Sounds/Plop.mp3"
    ra "There you go, well done Amy!"
    call LustPlusAmy
    mc "Is it a boy or a girl?"
    stop music
    scene birthbackground
    show taraamybaby 
    with dissolve
    play sound "v06/babycrying.mp3"
    ta "It's a boy!"
    am "I will call him Zander."
    $ babyamy = True
    call MCbabies
    $ pregam = False
    $ sawbirth = True
    mc "That birth was exhausting... I should go back to my bedroom and leave my child here, like a good harem master would do."
    scene bedroom01 with dissolve
    $ pregamstart = 0
    jump HaremNextMichiko
if pregamstart == 6:
    show amypreggo03 with moveinleft
    mc "Yours abs are gone. Pity, they were hot."
    am "Of course they're gone you idiot, I'm fucking PREGNANT!"
    mc "Well, good things guys can't get pregnant then cos I need to be STRONG."
    am "Well, I need to be strong too to carry this MASSIVE baby that's growing at five times the normal speed. You could try and be strong WITH me."
    mc "Sorry. Hang tight, you only have, like two weeks to go, Amy!"
    am "Two weeks that will feel like an ETERNITY!"
    hide amypreggo03 with fastdissolve
    jump HaremNextMichiko
if pregamstart == 4:
    show amypreggo02 with moveinleft
    am "Look [name]! The baby is GROWING. He's going to bring joy to the world!"
    mc "As well as outlandish maintenance fees I bet."
    hide amypreggo02
    show amypreggo02b
    with fastdissolve
    am "God, you just have to ruin EVERYTHING, don't you?"
    hide amypreggo02b with dissolve
    jump HaremNextMichiko
if pregamstart == 2:
    show amypreggo01 with moveinleft
    am "I don't know how to put it but... I'm PREGNANT!"
    am "Mother Nature is giving US a wonderful gift!"
    mc "Ah, err... Great, thanks Mother Nature! Maybe you could throw in some dollars in your gift cos raising a baby costs a fortune."
    hide amypreggo01
    show amypreggo01b
    with fastdissolve
    am "Why do you always have to spoil everything?"
    hide amypreggo01b with fastdissolve
    jump HaremNextMichiko
label HaremNextMichiko:
window hide
if pregmistart == 8:
    show michikopreggo04 with moveinleft
    mi "The Miracle of Life is about to happen, [name]!"
    mc "What? You mean, it's... happening?"
    play sound "Sounds/splooge01.mp3"
    mi "I am... That's it, my waters broke, take me to the medbay, quick!"
    mc "Alright, keep calm and... carry the baby."
    scene michikopreggo05 with fade
    play music "Sounds/beep.mp3"
    play sound "Sounds/debrasex.mp3"
    ta "Push, Michiko, PUSH!"
    scene michikopreggo05b with dissolve
    play sound "Sounds/womanscream.ogg"
    ta "Go on, I can see its head!"
    play sound "Sounds/Plop.mp3"
    ra "There you go, well done Michiko!"
    call LustPlusMichiko
    mc "Is it a boy or a girl?"
    stop music
    scene birthbackground
    show taramichikobaby 
    with dissolve
    play sound "v06/babycrying.mp3"
    ta "It's a boy!"
    mi "I will call him Haruto."
    $ babymichiko = True
    call MCbabies
    $ pregmi = False
    $ sawbirth = True
    mc "That birth was exhausting... I should go back to my bedroom and leave my child here, like a good harem master would do."
    scene bedroom01 with dissolve
    $ pregmistart = 0
    jump HaremNextGwen
if pregmistart == 6:
    show michikopreggo03 with moveinleft
    mi "I can't even fit in my clothes anymore! I'm constantly LEAKING milk for my HUGE mammaries!"
    mc "Good, so I won't have to pay some maintenance fee for his feeding then."
    hide michikopreggo03
    show michikopreggo03b
    with fastdissolve
    mi "Is money all you think about when you're about to become a FATHER?"
    mc "Err... I mean, I'm thinking about our kid's FUTURE. Right?"
    mi "Yeah. RIGHT."
    hide michikopreggo03b with fastdissolve
    jump HaremNextGwen
if pregmistart == 4:
    show michikopreggo02 with moveinleft
    mi "OUR healthy future BIRACIAL baby is really growing inside me."
    mi "He weighs a TON. I won't be able to teach you close combat anymore."
    mc "This pregnancy is starting to become such a burden."
    mi "Says the man who doesn't have to carry a fetus in his womb for nine months!"
    mc "Eight weeks. Eight weeks it is with my super-virile sperm."
    hide michikopreggo02 with fastdissolve
    jump HaremNextGwen
if pregmistart == 2:
    show michikopreggo01 with moveinleft
    mi "I have some AMAZING news, [name]. Your virile sperm BRUTALLY pierced through my ova. I'm pregnant."
    mc "Oh? Is the baby going to be... you know, white or foreign-looking you reckon?"
    hide michikopreggo01
    show michikopreggo01b
    with fastdissolve
    mi "What is that supposed to mean? He'll be a healthy BIRACIAL baby. You got a problem with that?"
    if mctrumpster == 5:
        mc "Well, yeah, kind of. I'm worried he might be an illegal voter for the DemocRats in the future."
        mi "I have no time for this. You're too BRUTAL a future father!"
        call LustMinusMichiko
    if mctrumpster <= 4:
        mc "No, of course not. Hurray for diversity. Right?"
        mi "Yes. RIGHT."
    hide michikopreggo01b with fastdissolve
    jump HaremNextGwen
label HaremNextGwen:
window hide
if preggwstart == 8:
    show gwenpregnant04 with moveinleft
    gw "I don't know if I can carry this MASSIVE baby any longer [name]!"
    mc "Well, as a Trumpster, surely, you can't be thinking of aborting, right?"
    hide gwenpregnant04
    show gwenpregnant04b
    with fastdissolve    
    play sound "Sounds/splooge01.mp3"
    gw "No, I'm thinking of giving birth you idiot! Like RIGHT NOW!"
    mc "Alright, keep calm and... let's go to the medbay."
    scene gwenpregnant05 with fade
    play music "Sounds/beep.mp3"
    play sound "Sounds/debrasex.mp3"
    ta "Push, Gwen, PUSH!"
    scene gwenpregnant05b with dissolve
    play sound "Sounds/womanscream.ogg"
    ta "Go on, I can see its head!"
    play sound "Sounds/Plop.mp3"
    ra "There you go, well done Gwen!"
    call LustPlusGwen
    mc "Is it a boy or a girl?"
    stop music
    scene birthbackground
    show taragwenbaby 
    with dissolve
    play sound "v06/babycrying.mp3"
    ta "It's a boy!"
    gw "I will call him Eric."
    $ babygwen = True
    call MCbabies
    $ preggw = False
    $ sawbirth = True
    mc "That birth was exhausting... I should go back to my bedroom and leave my child here, like a good harem master would do."
    scene bedroom01 with dissolve
    $ preggwstart = 0
    jump HaremNextAyla
if preggwstart == 6:
    show gwenpregnant03 with moveinleft
    mc "Hey, why are you smoking? It's not good for our baby, don't you realize it?"
    gw "FUCK OFF, I do what I WANT! Freedom baby, FREE-DUM!!"
    hide gwenpregnant03
    show gwenpregnant03b
    with fastdissolve
    gw "What you're gonna do, uh? NOTHING, that's right. SNOWFLAKE!"
    mc "I see you are not in the best of moods, I shall therefore leave you to be. A pregnant smoking lady."
    gw "Damn right. FREE-DUM!"
    hide gwenpregnant03b with fastdissolve
    jump HaremNextAyla
if preggwstart == 4:
    show gwenpregnant02 with moveinleft
    gw "MY baby is doing very well, thanks to ME taking good care of him."
    mc "I'm taking good care of him too. By not pummeling your womb anymore."
    hide gwenpregnant02
    show gwenpregnant02b
    with fastdissolve
    gw "But I'm not doing so well. I get headaches and..."
    gw "It'll pass. In about 6 weeks."
    hide gwenpregnant02b with fastdissolve
    jump HaremNextAyla
if preggwstart == 2:
    show gwenpregnant01 with moveinleft
    gw "The baby is really growing FAST. Against all scientific preconceptions about human gestation."
    mc "I would contend that this is due to my superior ALPHA-SPUNK."
    hide gwenpregnant01
    show gwenpregnant01b
    with fastdissolve
    gw "Of course you'd try and take the credit for it!"
    mc "Well, it's scientifically proven that I am SUPER-VIRILE, so there."
    gw "Umpf..."
    hide gwenpregnant01b with fastdissolve
    jump HaremNextAyla
label HaremNextAyla:
window hide
if pregaystart == 8:
    show aylapregnant04a with moveinleft
    ay "I can't even walk anymore! And the pain is getting really BORING! Make it go away please [name]!"
    mc "I have the best idea to make the pain go away. WIth even more pain from childbirth. Follow me to the medbay Ayla."
    hide aylapregnant04a
    show aylapregnant04b
    with fastdissolve    
    ay "I told you I COULDN'T walk! So carry me instead of standing there like a moron!"
    hide aylapregnant04b
    show aylapregnant04c
    with fastdissolve        
    mc "Alright, just breathe deeply and I'll carry you there in my muscular arms."
    scene aylapregnant05 with fade
    play music "Sounds/beep.mp3"
    play sound "Sounds/debrasex.mp3"
    ta "Push, Ayla, PUSH!"
    scene aylapregnant05b with dissolve
    play sound "Sounds/womanscream.ogg"
    ta "Go on, I can see its head!"
    play sound "Sounds/Plop.mp3"
    ra "There you go, well done Ayla!"
    call LustPlusAyla
    mc "Is it a boy or a girl?"
    stop music
    scene birthbackground
    show taraaylababy 
    with dissolve
    play sound "v06/babycrying.mp3"
    ta "It's a girl!"
    ay "That's just boring. I'll call her South East then. At least that's original."
    $ babyayla = True
    call MCbabies
    $ pregay = False
    $ sawbirth = True
    mc "That birth was exhausting... I should go back to my bedroom and leave my child here, like a good harem master would do."
    scene bedroom01 with dissolve
    $ pregaystart = 0
    jump HaremNextLaurie
if pregaystart == 6:
    show aylapregnant03a with moveinleft
    mc "So, how is the baby going Ayla? Is it kicking yet and doing exciting stuff inside your uterus?"
    ay "My uterus is not a fucking playground! But the baby thinks it is..."
    ay "I must admit, it IS less boring than I thought. Put your head and listen in, sometimes it sings!"
    hide aylapregnant03a
    show aylapregnant03b
    with fastdissolve
    mc "A future musician, hey? See, I told you our baby would be exciting news!"
    ay "I hope you're right. Cos I ain't raising a BORING baby."
    hide aylapregnant03b with fastdissolve
    jump HaremNextLaurie
if pregaystart == 4:
    show aylapregnant02a with moveinleft
    ay "You were right, it grew  A LOT. And now I can't even have sex anymore. This is even MORE BORING."
    mc "Once you give birth, I'll fuck you into the wall, how's that for a deal?"
    hide aylapregnant02a
    show aylapregnant02b
    with fastdissolve
    ay "Mmmh, I'll consider your offer. But only because I'm just so BORED right now."
    mc "Think about the joy this bundle of tissues will bring to the world!"
    hide aylapregnant02b
    show aylapregnant02c
    with fastdissolve
    ay "Don't talk about MY baby like that, you FREAK!"
    hide aylapregnant02c with fastdissolve
    jump HaremNextLaurie
if pregaystart == 2:
    show aylapregnant01a with moveinleft
    ay "You got me pregnant! I wasn't expecting it to be ssooo boring. It's like, still tiny and not doing ANYTHING. This crap is gonna last 9 months???"
    mc "Not with my superior radiated seed. Wait a couple of weeks and you'll start feeling something, don't worry..."
    hide aylapregnant01a
    show aylapregnant01b
    with fastdissolve
    ay "I'll give you the benefit of the doubt. But if nothing happens by then, I'm DUMPING this BORING baby, I'm warning you!"
    mc "I am confident in my sperm's virility and therefore the fetus' chances of survival."
    ay "Whatever..."
    hide aylapregnant01b with fastdissolve
    jump HaremNextLaurie
label HaremNextLaurie:
window hide
if preglastart == 8:
    show lauriepregnant04a with moveinleft
    la "[name], help me, my waters broke and I'm LEAKING milk everywhere!"
    mc "You want me to lick it off you? I can do that."
    hide lauriepregnant04a
    show lauriepregnant04b
    with fastdissolve    
    la "No, I mean take me to the medbay, I'm about to GIVE BIRTH!"
    mc "Ah right, sorry, I got confused by... all that yummy breastmilk that could have been... *sigh*"
    scene lauriepregnant05a with fade
    play music "Sounds/beep.mp3"
    play sound "Sounds/debrasex.mp3"
    ta "Push, Laurie, PUSH!"
    scene lauriepregnant05b with dissolve
    play sound "Sounds/womanscream.ogg"
    ta "Go on, I can see its head!"
    play sound "Sounds/Plop.mp3"
    ra "There you go, well done Laurie!"
    call LustPlusLaurie
    mc "Is it a boy or a girl?"
    stop music
    scene birthbackground
    show taraamybaby 
    with dissolve
    play sound "v06/babycrying.mp3"
    ta "It's a boy!"
    mc "I told you so."
    la "I'll call him River. Like the river of milk that's pouring from my nipples right now."
    $ babylaurie = True
    call MCbabies
    $ pregla = False
    $ sawbirth = True
    mc "That birth was exhausting... I should go back to my bedroom and leave my child here, like a good harem master would do."
    scene bedroom01 with dissolve
    $ preglastart = 0
    jump HaremNextBarbara
if preglastart == 6:
    show lauriepregnant03a with moveinleft
    la "I think I much prefer the reproductive cycle of my salads than that of HUMANS! This HUGE baby HURTS!"
    mc "Ah, but do plants leak milk like you're doing right now? That's gotta be a positive for the human race!"
    hide lauriepregnant03a
    show lauriepregnant03b
    with fastdissolve
    la "Actually, the BostiBoobicus Gigantus DOES leak milk."
    mc "I did not know that. It was mentioned in some ancient porn game, but I thought it was all made up by the dev."
    hide lauriepregnant03b with fastdissolve
    jump HaremNextBarbara
if preglastart == 4:
    show lauriepregnant02a with moveinleft
    la "Oh dear, the baby is growing and so are my breasts!"
    mc "That's a good sign, it means you're getting ready to feed it. And it's probably a boy."
    hide lauriepregnant02a
    show lauriepregnant02b
    with fastdissolve
    la "Why do you say that? You don't know!"
    mc "A boy will require a LOT of feeding to..err..grow, if you know what I mean. Wink wink, nudge nudge."
    hide lauriepregnant02b
    show lauriepregnant02c
    with fastdissolve
    la "Really, I think you don't understand science at all."
    mc "You wanna bet it's a boy?"
    la "No! I'm not BETTING on my baby's future gender! Now leave me alone with him."
    mc "AH! You said \"him\", see? You KNOW it's going to be a boy, that's why you won't bet with me!"
    hide lauriepregnant02c with fastdissolve
    jump HaremNextBarbara
if preglastart == 2:
    show lauriepregnant01a with moveinleft
    la "You seeded me!"
    mc "I sure did, lots of virile seed if I remember correctly actually."
    if sierranickname:
        hide lauriepregnant01a
        show lauriepregnant01b
        with fastdissolve
        la "I guess they don't call you \"[name] the Seeder\" for nothing..."
        mc "That's right, baby, that's right..."
        la "You certainly made good use of it. Bye [name]!"        
    if sierranickname == False and mcsierra >= 4:
        hide lauriepregnant01a
        show lauriepregnant01b
        with fastdissolve
        la "That's right. And you certainly deserve the title of \"[name] the Seeder\"!"
        mc "Yooo-hoo! A new nickname!"
        window hide
        show mcsierranickname at posmission
        play sound "Sounds/skill.mp3"
        $ renpy.pause(2.0, hard=True)
        hide mcsierranickname
        $ sierranickname = True
        la "Now make good use of it. Bye [name]!"
    if sierranickname == False and mcsierra <= 3:
        hide lauriepregnant01a
        show lauriepregnant01b
        with fastdissolve
        la "If you had a higher standing in the Sierra Club, you might have even gained a nickname at this stage..."
        mc "What? You mean I missed an opportunity for a new nickname?"
        la "That's right.. Too bad, it won't come back again since you can't seed me more that once in this game... Bye [name]!"
    hide lauriepregnant01b with fastdissolve
    jump HaremNextBarbara
label HaremNextBarbara:
window hide
if pregbastart == 8:
    show barbarapregnant04a with moveinleft
    ba "[name], your genetically-superior sperm has turned into a GIANT baby who demands to get OUT right NOW!"
    mc "It sounds like YOU want him out, which ain't very nice of you if you ask m..."
    hide barbarapregnant04a
    show barbarapregnant04b
    with fastdissolve    
    ba "SHUT THE FUCK UP AND TAKE ME TO THE MEDBAY!"
    mc "Gee, teach, take it easy! I'll take you there, don't worry."
    scene barbarapregnant05a with fade
    play music "Sounds/beep.mp3"
    play sound "Sounds/debrasex.mp3"
    ta "Push, Barbara, PUSH!"
    scene barbarapregnant05b with dissolve
    play sound "Sounds/womanscream.ogg"
    ta "Go on, I can see its head!"
    play sound "Sounds/Plop.mp3"
    ra "There you go, well done Barbara!"
    call LustPlusBarbara
    mc "Is it a boy or a girl?"
    stop music
    scene birthbackground
    show taraamybaby 
    with dissolve
    play sound "v06/babycrying.mp3"
    ta "It's a boy!"
    ba "I'll call him... Junior. And he will grow up to be a valiant soldier for our glorious leader, I will make sure of that!"
    $ babybarbara = True
    call MCbabies
    $ pregba = False
    $ sawbirth = True
    mc "That birth was exhausting... I should go back to my bedroom and leave my child here, like a good harem master would do."
    scene bedroom01 with dissolve
    $ pregbastart = 0
    jump HaremNextPre02
if pregbastart == 6:
    show barbarapregnant03a with moveinleft
    ba "This baby is really genetically SUPERIOR. Like IMMENSELY superior."
    mc "Of course he is, my best sperm created it and my sperms are like, super-strong like me."
    hide barbarapregnant03a
    show barbarapregnant03b
    with fastdissolve
    ba "I do believe you! I can already feel him hitting me from the inside with his monstercock! There, just now!"
    mc "Err, are you even allowed to say such a thing???"
    hide barbarapregnant03b
    show barbarapregnant03c
    with fastdissolve
    ba "I saw a rendering of that in an ancient game that no longer exists on Patreon, but they allowed it at the time."
    mc "Ah, all's well then. If Patreon allows it, who are we to discuss their omnipotent decision, hey?"
    hide barbarapregnant03c with fastdissolve
    jump HaremNextPre02
if pregbastart == 4:
    show barbarapregnant02a with moveinleft
    ba "[name], I have great news, our baby is growing and so is the future of New America!"
    mc "And all that thanks to me."
    hide barbarapregnant02a
    show barbarapregnant02b
    with fastdissolve
    ba "No! If it weren't for President-for-Life Trumpf's policy of \"White American Babies First\", I would never have allowed you to impregnate me."
    hide barbarapregnant02b
    show barbarapregnant02a
    with fastdissolve
    ba "So it's really ALL THANKS TO HIM."
    mc "Not even me a bit?"
    ba "No, not one bit."
    hide barbarapregnant02a with fastdissolve
    jump HaremNextPre02
if pregbastart == 2:
    show barbarapregnant01a with moveinleft
    ba "The impregnation was successful [name]! As successful as our President-for-Life's last re-election-for-Life campaign!"
    mc "I don't remember it, I was buried under a pile of rubble at the time."
    ba "Well, I can assure you that he easily won with over 99\% of the votes! He would have beaten George Washington easily with such a score!"
    mc "Did he cheat by any chance?"
    hide barbarapregnant01a
    show barbarapregnant01b
    with fastdissolve
    ba "Of course not! The Radical Far-Left are the ones who cheated, how would they have obtained almost 1\% of the votes otherwise?"
    mc "I see..."
    hide barbarapregnant01b with fastdissolve
    jump HaremNextPre02
label HaremNextPre02:
if replaceamy:
    $ replaceamy = False
    scene bedroom01
    show amy01 at centerleft with moveinleft
    mc "I'm replacing you with Bella."
    hide amy01
    show amy05 at centerleft
    with fastdissolve
    am "What? How can you do that to me?"
    mc "She won't join until you leave, sorry. Maybe sort out your differences one day. Outside of my harem!"
    hide amy05
    window hide
    call LustMinusAmy
    hide amy05 with moveoutleft
    $ haremam = False
    $ girlsinharem -= 1
    $ amydismissed = True
    $ pregamready = 0
    call HaremPreBella
if replaceangie:
    $ replaceangie = False
    scene bedroom01
    show anigeasking at centerleft with moveinleft
    mc "I'm replacing you with Bella."
    hide angieasking
    show angiesad at centerleft
    with fastdissolve
    an "What? What have I done?"
    mc "Nothing, it's just that she won't join until you leave, sorry. Maybe sort out your differences one day. Outside of my harem!"
    window hide
    call LustMinusAngie
    hide angiesad with moveoutleft
    $ hareman = False
    $ girlsinharem -= 1
    $ angiedismissed = True
    $ preganready = 0
    call HaremPreBella
if replaceayla:
    $ replaceayla = False
    scene bedroom01
    show ayla01 at centerleft with moveinleft
    mc "I'm replacing you with Bella. She hates you by the way."
    hide ayla01
    show ayla05 at centerleft
    with fastdissolve
    ay "What? I'm gonna headbutt that bitch!"
    mc "Get a ladder for that. And maybe sort out your differences one day. Outside of my harem!"
    window hide
    call LustMinusAyla
    hide ayla05 with moveoutleft
    $ haremay = False
    $ girlsinharem -= 1
    $ ayladismissed = True
    $ pregayready = 0
    call HaremPreBella
if replacebarbara:
    $ replacebarbara = False
    scene bedroom01
    show barbara08 at centerleft with moveinleft
    mc "I'm replacing you with Bella."
    hide barbara08
    show barbara07 at centerleft
    with fastdissolve
    ba "What? How can you do that to me?"
    mc "She won't join until you leave, sorry. Maybe sort out your differences one day. Outside of my harem!"
    window hide
    call LustMinusBarbara
    hide barbara07 with moveoutleft
    $ haremba = False
    $ girlsinharem -= 1
    $ barbaradismissed = True
    $ pregbaready = 0
    call HaremPreBella
if replacecyrl:
    $ replacecyrl = False
    scene bedroom01
    show cyrl02 at centerleft with moveinleft
    mc "I'm replacing you with Bella."
    hide cyrl02
    show cyrl04 at centerleft
    with fastdissolve
    cy "What is the Boolean logic behind this move?"
    mc "She won't join until you leave. Maybe sort out your differences one day. Outside of my harem!"
    window hide
    call LustMinusCyrl
    hide cyrl04 with moveoutleft
    $ haremcy = False
    $ girlsinharem -= 1
    $ cyrldismissed = True
    call HaremPreBella
if replacedebra:
    $ replacedebra = False
    scene bedroom01
    show debratalking01 at centerleft with moveinleft
    mc "I'm replacing you with Bella."
    hide debratalking01
    show debraoffended at centerleft
    with fastdissolve
    de "What? How can you do that to me?"
    mc "She won't join until you leave, sorry. Maybe sort out your differences one day. Outside of my harem!"
    window hide
    call LustMinusDebra
    hide debraoffended with moveoutleft
    $ haremde = False
    $ girlsinharem -= 1
    $ debradismissed = True
    call HaremPreBella
if replacegwen:
    $ replacegwen = False
    scene bedroom01
    show gwen03 at centerleft with moveinleft
    mc "I'm replacing you with Bella."
    hide gwen03
    show gwen05 at centerleft
    with fastdissolve
    gw "What? How can you do that to me?"
    mc "She won't join until you leave, sorry. Maybe sort out your differences one day. Outside of my harem!"
    window hide
    call LustMinusGwen
    hide gwen05 with moveoutleft
    $ haremgw = False
    $ girlsinharem -= 1
    $ gwendismissed = True
    $ preggwready = 0
    call HaremPreBella
if replacemarnie:
    $ replacemarnie = False
    scene bedroom01
    show marnie02 at centerleft with moveinleft
    mc "I'm replacing you with Bella."
    hide marnie02
    show marnie06 at centerleft
    with fastdissolve
    ma "What? How can you do that to me?"
    mc "She won't join until you leave, sorry. Maybe sort out your differences one day. Outside of my harem!"
    window hide
    call LustMinusMarnie
    hide marnie06 with moveoutleft
    $ haremma = False
    $ girlsinharem -= 1
    $ marniedismissed = True
    call HaremPreBella
if replacelaurie:
    $ replacelaurie = False
    scene bedroom01
    show laurie03 at centerleft with moveinleft
    mc "I'm replacing you with Bella."
    hide laurie03
    show laurie04 at centerleft
    with fastdissolve
    la "What? How can you do that to me?"
    mc "She won't join until you leave, sorry. Maybe sort out your differences one day. Outside of my harem!"
    window hide
    call LustMinusLaurie
    hide laurie04 with moveoutleft
    $ haremla = False
    $ girlsinharem -= 1
    $ lauriedismissed = True
    $ preglaready = 0
    call HaremPreBella
if replacelena:
    $ replacelena = False
    scene bedroom01
    show lena01 at centerleft with moveinleft
    mc "I'm replacing you with Bella."
    hide lena01
    show lena03 at centerleft
    with fastdissolve
    le "What? Why are you doing this to me?"
    mc "She won't join until you leave, sorry. Maybe sort out your differences one day. Outside of my harem!"
    window hide
    call LustMinusLena
    hide lena03 with moveoutleft
    $ haremle = False
    $ girlsinharem -= 1
    $ lenadismissed = True
    call HaremPreBella
if replaceclara:
    $ replaceclara = False
    scene bedroom01
    show clara03 at centerleft with moveinleft
    mc "I'm replacing you with Bella."
    hide clara03
    show clara04 at centerleft
    with fastdissolve
    cl "What? How can you do that to me?"
    mc "She won't join until you leave, sorry. Maybe sort out your differences one day. Outside of my harem!"
    window hide
    call LustMinusClara
    hide clara04 with moveoutleft
    $ haremcl = False
    $ girlsinharem -= 1
    $ claradismissed = True
    call HaremPreBella
if replacenancy:
    $ replacenancy = False
    scene bedroom01
    show nancybedroom02 at centerleft with moveinleft
    mc "I'm replacing you with Bella."
    hide nancybedroom02
    show nancybedroom01 at centerleft
    with fastdissolve
    mo "What? How can you do this to me, sweetie?"
    mc "She won't join until you leave, sorry. Maybe sort out your differences one day. Outside of my harem!"
    window hide
    call LustMinusNancy
    hide nancybedroom01 with moveoutleft
    $ haremmo = False
    $ girlsinharem -= 1
    $ momdismissed = True
    $ pregmoready = 0
    call HaremPreBella
if replacemichiko:
    $ replacemichiko = False
    scene bedroom01
    show michiko01 at centerleft with moveinleft
    mc "I'm replacing you with Bella."
    hide michiko01
    show michiko03 at centerleft
    with fastdissolve
    mi "What? How can you do that to me?"
    mc "She won't join until you leave, sorry. Maybe sort out your differences one day. Outside of my harem!"
    window hide
    call LustMinusMichiko
    hide michiko03 with moveoutleft
    $ haremmi = False
    $ girlsinharem -= 1
    $ michikodismissed = True
    $ pregmiready = 0
    call HaremPreBella
if replacepenny:
    $ replacepenny = False
    scene bedroom01
    show penny03 at centerleft with moveinleft
    mc "I'm replacing you with Bella."
    hide penny03
    show pennyserious at centerleft
    with fastdissolve
    pe "What? How can you do that to me?"
    mc "She won't join until you leave, sorry. Maybe sort out your differences one day. Outside of my harem!"
    window hide
    call LustMinusPenny
    hide pennyserious with moveoutleft
    $ harempe = False
    $ girlsinharem -= 1
    $ pennyodismissed = True
    call HaremPreBella
if replaceruby:
    $ replaceruby = False
    scene bedroom01
    show ruby06 at centerleft with moveinleft
    mc "I'm replacing you with Bella."
    hide ruby06
    show ruby07 at centerleft
    with fastdissolve
    ru "What? How can you do that to me?"
    mc "She won't join until you leave, sorry. Maybe sort out your differences one day. Outside of my harem!"
    window hide
    call LustMinusRuby
    hide ruby07 with moveoutleft
    $ haremru = False
    $ girlsinharem -= 1
    $ rubydismissed = True
    call HaremPreBella
if replacesuki:
    $ replacesuki = False
    scene bedroom01
    show suki02 at centerleft with moveinleft
    mc "I'm replacing you with Bella."
    hide suki02
    show suki03 at centerleft
    with fastdissolve
    su "What? How can you do that to me?"
    mc "She won't join until you leave, sorry. Maybe sort out your differences one day. Outside of my harem!"
    window hide
    call LustMinusSuki
    hide suki03 with moveoutleft
    $ haremsu = False
    $ girlsinharem -= 1
    $ sukidismissed = True
    call HaremPreBella
if replacezara:
    $ replacezara = False
    scene bedroom01
    show zara01 at centerleft with moveinleft
    mc "I'm replacing you with Bella."
    za "What? How can you do that to me?"
    mc "She won't join until you leave, sorry. Maybe sort out your differences one day. Outside of my harem!"
    window hide
    call LustMinusZara
    hide zara01 with moveoutleft
    $ haremza = False
    $ girlsinharem -= 1
    $ zaradismissed = True
    $ pregzaready = 0
    call HaremPreBella
    
if pregmo:
    jump HaremNextPreAngie
if haremmo and lustmo <= 3:
    show nancycountry01 at centerleft with moveinleft
    mo "Sweetie pie, You did something bad this week and my lust for you isn't high enough anymore."
    mc "What did I do exactly?"
    mo "I can't recall, but the lust stats don't lie. I'm sorry my sweet landboy, but this is over. Until you get my lust back up a bit..."
    window hide
    hide nancycountry01 with dissolve
    $ haremmo = False
    $ girlsinharem -= 1
    $ pregmoready = 0
    jump HaremNextPreAngie
if weekfuckedmom == False and haremmo and lustmo <= 4:
    show nancycountry01 at centerleft with moveinleft
    mo "Sweetie pie, my pussy was hungry and you... didn't take care of it. I don't think this harem thing is working for me. I'm leaving."
    mc "What? But I was like...err... just busy saving the world and all that."
    mo "Well call me back when you have TIME for ME and MY PUSSY then. Bye bye sweetie pie!"
    call LustMinusNancy
    window hide
    hide nancycountry01 with dissolve
    $ haremmo = False
    $ pregmoready = 0
    $ girlsinharem -= 1
if weekfuckedmom == False and haremmo and lustmo == 5:
    show nancycountry01 at centerleft with moveinleft
    mo "Sweetie pie, my pussy was hungry and you... didn't take care of it. My lust for you has decreased, but I'll remain in your harem for now..."
    mc "Ah. So lust of 4 now, right at the edge then..."
    call LustMinusNancy
    hide nancycountry01 with dissolve

label HaremNextPreAngie:
if pregan:
    jump HaremNextPreMichiko
if hareman and lustan <= 3:
    show angiesad at centerleft with moveinleft
    an "I don't feel loved by you anymore. And I don't feel enough LUST for you either. You didn't treat me well."
    mc "That's life, lust goes up, lust goes down."
    hide angiesad 
    show angiehesitant at centerleft
    with fastdissolve
    an "Maybe, but it always happens to ME. I want to leave your harem. And be alone."
    window hide
    hide angiehesitant with dissolve
    $ hareman = False
    $ preganready = 0
    $ girlsinharem -= 1
    jump HaremNextPreMichiko
if weekfuckedangie == False and hareman and lustan <= 4:
    show angiesad at centerleft with moveinleft
    an "I felt protected this week but... I didn't feel... loved. You never called me at nights! What have I done?"
    mc "Ah, I must have forgotten. My bad."
    hide angiesad 
    show angiehesitant at centerleft
    with fastdissolve
    an "Nobody ever notices me. I want to leave your harem. And be alone."
    call LustMinusAngie
    window hide
    $ preganready = 0
    hide angiehesitant with dissolve
    $ hareman = False
    $ girlsinharem -= 1
if weekfuckedangie == False and hareman and lustan == 5:
    show angiesad at centerleft with moveinleft
    an "I felt protected this week but... I didn't feel... loved. My lust for you has decreased, but I'll remain in your harem for now..."
    mc "Ah. So lust of 4 now, right at the edge then..."
    call LustMinusAngie
    hide angiesad with dissolve

label HaremNextPreMichiko:
if pregmi:
    jump HaremNextPreCyrl
if haremmi and lustmi <= 3:
    show michiko05 at centerleft with moveinleft
    mi "You were TOO brutal to me this week and my lust for you has taken a BRUTAL dive."
    mi "I'm leaving your harem until there is a BRUTAL uptick in my lust points. Which clearly won't be for a while."
    window hide
    hide michiko05 with dissolve
    mc "Damn, that was BRUTAL."
    $ haremmi = False
    $ girlsinharem -= 1
    $ pregmiready = 0
    jump HaremNextPreCyrl
if weekfuckedmichiko == False and haremmi and lustmi <= 4:
    show michiko05 at centerleft with moveinleft
    mi "I was expecting some BRUTAL FUCKING from you, and all I got was a dry pussy."
    mi "I'm leaving your harem until you can provide me with what I NEED."
    call LustMinusMichiko
    window hide
    hide michiko05 with dissolve
    mc "Damn, that was BRUTAL."
    $ haremmi = False
    $ pregmiready = 0
    $ girlsinharem -= 1
    jump HaremNextPreCyrl
if weekfuckedmichiko == False and haremmi and lustmi== 5:
    show michiko05 at centerleft with moveinleft
    mi "I was expecting some BRUTAL FUCKING from you, and all I got was a dry pussy. My lust for you has decreased, but I'll remain in your harem for now..."
    mc "Ah. So lust of 4 now, right at the edge then..."
    call LustMinusMichiko
    hide michiko05 with dissolve

label HaremNextPreCyrl:
if haremcy and lustcy <= 3:
    show cyrl05 at centerleft with moveinleft
    cy "My motherboard informs me that my lust for you has fallen below critical level."
    mc "Meaning?"
    cy "Meaning I shall no longer be a member of your harem. Goodbye human friend."
    window hide
    hide cyrl05 with dissolve
    $ haremcy = False
    $ girlsinharem -= 1
    jump HaremNextPreRuby
if weekfuckedcyrl == False and haremcy and lustcy <= 4:
    show cyrl05 at centerleft with moveinleft
    cy "My motherboard informs me that you failed to provide any lubricant to my internal sexual organs this week."
    mc "Meaning?"
    cy "Meaning I shall no longer be a member of your harem. Goodbye human friend."
    call LustMinusCyrl
    window hide
    hide cyrl05 with dissolve
    $ haremcy = False
    $ girlsinharem -= 1
if weekfuckedcyrl == False and haremcy and lustcy == 5:
    show cyrl05 at centerleft with moveinleft
    cy "My motherboard informs me that you failed to provide any lubricant to my internal sexual organs this week."
    cy "Also that my lust for you has decreased to the critical level of 4. Which is just about sufficient for me to remain in your harem..."
    call LustMinusCyrl
    hide cyrl05 with dissolve

label HaremNextPreRuby:
if haremru and lustru <= 3:
    show ruby07 at centerleft with moveinleft
    ru "How dare you treat me like some sissy Sierra Club member. I am a ROAD WARRIOR."
    mc "Err... What?"
    ru "Road Warriors don't belong to harems when their lust has fallen below 4. These are the RULES. I'm out of here!"
    window hide
    hide ruby07 with dissolve
    $ haremru = False
    $ girlsinharem -= 1
    jump HaremNextPreAmy
if weekfuckedruby == False and haremru and lustru <= 4:
    show ruby07 at centerleft with moveinleft
    ru "What's wrong with you, wimp?"
    mc "What? I'm NOT A WIMP!"
    ru "You didn't even bother SMASHING my pussy this week. So yeah, you're a fucking wimp and I'm out of your stinkin' harem!"
    call LustMinusRuby
    window hide
    hide ruby07 with dissolve
    $ haremru = False
    $ girlsinharem -= 1
if weekfuckedruby == False and haremru and lustru == 5:
    show ruby07 at centerleft with moveinleft
    ru "You didn't even bother SMASHING my pussy this week. My lust for you has decreased, but I'll remain in your harem for now..."
    mc "Ah. So lust of 4 now, right at the edge then..."
    call LustMinusRuby
    hide ruby07 with dissolve

label HaremNextPreAmy:
if pregam:
    jump HaremNextPreAyla
if haremam and lustam <= 3:
    show amy06 at centerleft with moveinleft
    am "Sorry, but I don't want to have anything to do with a harem Master who can't keep my lust up for him."
    mc "It's the balance of Nature, not me, I swear!"
    hide amy06
    show amy04 at centerleft
    with fastdissolve
    am "Well, Nature's balance tells me not to bother belonging to your harem anymore."
    window hide
    hide amy04 with dissolve
    $ haremam = False
    $ girlsinharem -= 1
    $ pregamready = 0
    jump HaremNextPreAyla        
if weekfuckedamy == False and haremam and lustam <= 4:
    show amy06 at centerleft with moveinleft
    am "Sorry, but I don't want to have anything to do with a harem Master who CAN'T GET IT UP!"
    mc "Hey! I CAN get it UP. UP 18 inches as a matter of fact."
    hide amy06
    show amy04 at centerleft
    with fastdissolve
    am "Well I didn't see any of those inches this week, so I'm leaving you for greener pastures."
    call LustMinusAmy
    window hide
    hide amy04 with dissolve
    $ haremam = False
    $ pregamready = 0
    $ girlsinharem -= 1
if weekfuckedamy == False and haremam and lustam == 5:
    show amy06 at centerleft with moveinleft
    am "A plant needs constant caring, so do I, but you FAILED to water me this week. My lust for you has decreased, but I'll remain in your harem for now..."
    mc "Ah. So lust of 4 now, right at the edge then..."
    call LustMinusAmy
    hide amy06 with dissolve

label HaremNextPreAyla:
if pregay:
    jump HaremNextPreSuki
if haremay and lustay <= 3:
    show ayla04 at centerleft with moveinleft
    ay "You were sssooo BORING this week, my lust was you is now boringly below 4."
    mc "Well, that's exciting, isn't it?"
    hide ayla04
    show ayla05 at centerleft
    with fastdissolve
    ay "God you're ssooo BORING. I'm leaving this BORING harem."
    window hide
    hide ayla05 with dissolve
    $ haremay = False
    $ girlsinharem -= 1
    $ pregamready = 0
    jump HaremNextPreSuki        
if weekfuckedayla == False and haremay and lustay <= 4:
    show ayla04 at centerleft with moveinleft
    ay "You're a LOUSY harem Master. You didn't even fuck me this week. Sssooo BORING!"
    mc "I was busy saving the world and your soul, Ayla!"
    hide ayla04
    show ayla05 at centerleft
    with fastdissolve
    ay "Leave my soul alone, FREAK! I'm leaving your BORING harem!"
    call LustMinusAyla
    window hide
    hide ayla05 with dissolve
    $ haremay = False
    $ pregamready = 0
    $ girlsinharem -= 1
if weekfuckedayla == False and haremay and lustay == 5:
    show ayla04 at centerleft with moveinleft
    ay "You didn't even fuck me this week. Sssooo BORING! My lust for you has decreased, but I'll remain in your harem for now cos I'm just so BORED..."
    mc "Ah. So lust of 4 now, right at the edge then..."
    call LustMinusAyla
    hide ayla04 with dissolve
if mcchurch <= 3 and haremay:
    show ayla04 at centerleft with moveinleft
    ay "You've dropped out of favor with the Church..."
    mc "Yeah, so?"
    hide ayla04
    show ayla05 at centerleft
    with fastdissolve
    ay "And therefore you've dropped out of favor with ME! See you in HELL, [name]!"
    call LustMinusAyla
    hide ayla05 with dissolve
    $ haremay = False
    $ pregamready = 0
    $ girlsinharem -= 1
    mc "Well, my soul took a beating there."

label HaremNextPreSuki:
if weekfuckedsuki == False and haremsu and lustsu <= 4:
    show suki01 at centerleft with moveinleft
    su "You did something terrible to me this week. SO bad my lust fell."
    mc "Oh? What could it be?"
    hide suki01
    show suki03 at centerleft
    with fastdissolve
    su "It's irrelevant! Numbers don't LIE. I can't stay in your harem at this stage."
    window hide
    hide suki03 with dissolve
    $ haremsu = False
    $ girlsinharem -= 1
    jump HaremNextPreGwen        
if weekfuckedsuki == False and haremsu and lustsu <= 4:
    show suki01 at centerleft with moveinleft
    su "Maybe I was too busy hacking all week, but I seem to remember NOT having any sexual intercourse with you."
    mc "No, no, it happened I swear, you just... err... Don't remember!"
    hide suki01
    show suki03 at centerleft
    with fastdissolve
    su "Don't lie to me! That's it, I'm leaving your harem. It's virtual anyway since nothing ever happens in it!"
    call LustMinusSuki
    window hide
    hide suki03 with dissolve
    $ haremsu = False
    $ girlsinharem -= 1
if weekfuckedsuki == False and haremsu and lustsu == 5:
    show suki01 at centerleft with moveinleft
    su "I don't seem to remember having any sexual intercourse with you this week. Actually, I'm pretty sure NOTHING happened. My lust for you has therefore mathematically decreased by one point."
    mc "Ah. So lust of 4 now, right at the edge then..."
    call LustMinusSuki
    hide suki01 with dissolve

label HaremNextPreGwen:
if preggw:
    jump HaremNextPrePenny
if haremgw and lustgw <= 3:
    show gwen06 at centerleft with moveinleft
    gw "You finally had me lured into your harem and you somehow managed to SCREW THINGS UP this week."
    mc "Not as bad as the way you screw up Debra's experiments I hope?"
    hide gwen06
    show gwen05 at centerleft
    with fastdissolve
    gw "What??? I'm leaving your harem! I'd rather suffer at the hands of Debra than YOU!"
    window hide
    hide gwen05 with dissolve
    $ haremgw = False
    $ girlsinharem -= 1
    jump HaremNextPrePenny
if weekfuckedgwen == False and haremgw and lustgw <= 4:
    show gwen06 at centerleft with moveinleft
    gw "So, apparently, RAPING me is something you don't have any problems with, but making SWEET LOVE to me is beyond your capabilities..."
    mc "Err... Maybe I can rape you right now to make it up for it?"
    hide gwen06
    show gwen05 at centerleft
    with fastdissolve
    gw "What??? I'm leaving your harem! I'd rather suffer at the hands of Debra than YOU!"
    call LustMinusGwen
    window hide
    hide gwen05 with dissolve
    $ haremgw = False
    $ girlsinharem -= 1
if weekfuckedgwen == False and haremgw and lustgw == 5:
    show gwen06 at centerleft with moveinleft
    gw "The only sexual thing between us I remember is the time you RAPED me a while back. I have no recollection of any sweet love this week AT ALL. So my lust for you has decreased."
    call LustMinusGwen
    mc "Ah. So lust of 4 now, right at the edge then..."
    hide gwen06 with dissolve
    
label HaremNextPrePenny:
if harempe and lustpe <= 3:
    show pennypensive at centerleft with moveinleft
    pe "I don't know how you managed the extraordinary feat of pissing off a Road Warrior, but here we are."
    mc "Here we are where?"
    hide pennypensive
    show pennyserious at centerleft
    with fastdissolve
    pe "At the point where I tell you my lust for you isn't high enough! Goodbye, [name]! I'm back on the Road as a free woman!"
    window hide
    hide pennyserious with dissolve
    $ harempe = False
    $ girlsinharem -= 1
    jump HaremNextPreMarnie
if weekfuckedpenny == False and harempe and lustpe <= 4:
    show penny03 at centerleft with moveinleft
    pe "A Road Warrior needs to be LOVED. And FUCKED REGULARLY. Which you are apparently incapable of providing."
    mc "Are you accusing me of failing in my harem master duties?"
    hide penny03
    show pennyserious at centerleft
    with fastdissolve
    pe "YES I AM. Goodbye, [name]! I'm back on the Road as a free woman!"
    call LustMinusPenny
    window hide
    hide pennyserious with dissolve
    $ harempe = False
    $ girlsinharem -= 1
if weekfuckedpenny == False and harempe and lustpe == 5:
    show penny03 at centerleft with moveinleft
    pe "Road Warriors are known for their good memories. Like remembering the Road less travelled. And right now, my pussy is the Road less travelled. By your COCK. My lust for you has therefore decreased."
    call LustMinusPenny
    mc "Ah. So lust of 4 now, right at the edge then..."
    hide penny03 with dissolve
        
label HaremNextPreMarnie:
if haremma and lustma <= 3:
    show marnie05 at centerleft with moveinleft
    ma "Crossing a Road Warrior was a terrible mistake you made."
    mc "I did what?"
    ma "You did BAD. And I'm leaving your stinking BAD harem as a result!"
    window hide
    hide marnie05 with dissolve
    $ haremma = False
    $ girlsinharem -= 1
    jump HaremNextPreClara
if weekfuckedmarnie == False and haremma and lustma <= 4:
    show marnie05 at centerleft with moveinleft
    ma "I don't ask for much. Some kinky femdom or some ruthless maledom once a week. And you weren't sissy or man enough to provide EITHER!"
    mc "I'm a moderate, that's why! And you're an extremist!"
    hide marnie05
    show marnie06 at centerleft
    with fastdissolve
    ma "As a Road Warrior, I am taking your accusation EXTREMELY badly. And leaving you stinking harem as a result."
    call LustMinusMarnie
    window hide
    hide marnie06 with dissolve
    $ haremma = False
    $ girlsinharem -= 1
if weekfuckedmarnie == False and haremma and lustma == 5:
    show marnie06 at centerleft with moveinleft
    ma "I don't ask for much. Some kinky femdom or some ruthless maledom once a week. And you weren't sissy or man enough to provide EITHER!"
    hide marnie06
    show marnie04 at centerleft
    with fastdissolve
    ma "Which means..."
    call LustMinusMarnie
    ma "THIS!"
    mc "Ah. So lust of 4 now, right at the edge then..."
    hide marnie04 with dissolve

label HaremNextPreClara:
if haremcl and lustcl <= 3:
    show stripclara02 at centerleft with moveinleft
    cl "I prayed and prayed that I would not lose my Faith in you, but to no avail..."
    mc "Meaning in layperson's terms?"
    hide stripclara02
    show clara06 at centerleft
    with fastdissolve
    cl "That I have no choice but to leave your harem! Do not disturb me while I am on a spiritual retreat form the sexual ecstasy I endured all this time..."
    window hide
    hide clara06 with dissolve
    $ haremcl = False
    $ girlsinharem -= 1
    jump HaremNextPreLaurie
if weekfuckedclara == False and haremcl and lustcl <= 4:
    show stripclara02 at centerleft with moveinleft
    cl "I prayed and prayed that I would not lose my Faith in you, but to no avail..."
    mc "Meaning in layperson's terms?"
    hide stripclara02
    show clara06 at centerleft
    with fastdissolve
    cl "I know I am a sinner, but I still need some LOVING HOT SEX. You have forsaken me and I will leave on a spiritual journey of redemption."
    call LustMinusClara
    window hide
    hide clara06 with dissolve
    $ haremcl = False
    $ girlsinharem -= 1
if weekfuckedclara == False and haremcl and lustcl == 5:
    show stripclara01 at centerleft with moveinleft
    cl "I know I am a sinner, but I still need some LOVING HOT SEX. You have forsaken me this week."
    mc "Ah, yes, I should have provided with some Holy Spurts, my bad, too busy saving the world and all that. We're still good?"
    hide stripclara01
    show stripclara02 at centerleft
    with fastdissolve
    cl "Barely..."
    call LustMinusClara
    mc "Ah. So lust of 4 now, right at the edge then..."
    hide stripclara02 with dissolve

label HaremNextPreLaurie:
if haremla and lustla <= 3:
    show laurie03 at centerleft with moveinleft
    la "You've proven to me that this harem thing was nothing but a PLOY from day one."
    mc "I don't understand what you mean."
    hide laurie03
    show laurie04 at centerleft
    with fastdissolve
    la "You've been such a HORRIBLE person to me that I am longer in lust with you. I'm leaving your harem, [name]."
    mc "Ah. Well, that's clearer at least."
    window hide
    hide laurie04 with dissolve
    $ haremla = False
    $ girlsinharem -= 1
    jump HaremNextPreLena
if weekfuckedlaurie == False and haremla and lustla <= 4:
    show laurie03 at centerleft with moveinleft
    la "I know you're busy. And I'm busy too, feeding this compound. But why didn't you FUCK me this week?"
    mc "What? I didn't fuck you? MY bad, I have so many chicks in my har..."
    hide laurie03
    show laurie04 at centerleft
    with fastdissolve
    la "I don't want to be just ANOTHER ONE of your girls. This harem is NOT for me! I'm leaving."
    call LustMinusLaurie
    window hide
    hide laurie04 with dissolve
    $ haremla = False
    $ girlsinharem -= 1
if weekfuckedlaurie == False and haremla and lustla == 5:
    show laurie03 at centerleft with moveinleft
    la "I know you're busy. And I'm busy too, feeding this compound. But why didn't you FUCK me this week?"
    mc "What? I didn't fuck you? MY bad, I have so many chicks in my har..."
    hide laurie03
    show laurie04 at centerleft
    with fastdissolve
    la "I don't want to be just ANOTHER ONE of your girls. So you'd better take care of my needs next week or I'm LEAVING!"
    call LustMinusLaurie
    mc "Ah. So lust of 4 now, right at the edge then..."
    hide laurie04 with dissolve
    
label HaremNextPreLena:
if haremle and lustle <= 3:
    show lena06 at centerleft with moveinleft
    le "I knew I couldn't trust you! You blew it, like you always do."
    mc "I'll have you know that I have completed several quests and missions so far and my...."
    hide lena06
    show lena10 at centerleft
    with fastdissolve
    le "Enough! I'm leaving your harem and from now on, you shall call me CHIEF again, understood?"
    mc "Roger that. Chief."
    window hide
    hide lena10 with dissolve
    $ haremle = False
    $ girlsinharem -= 1
    jump HaremNextPreBarbara
if weekfuckedlena == False and haremle and lustle <= 4:
    show lena03 at centerleft with moveinleft
    le "You're even worse that Jake! He's got a small tiny dicklet, but at least he FUCKS ME!"
    mc "I was too busy doing quests and shit, you know stuff you GAVE me to do and..."
    hide lena03
    show lena10 at centerleft
    with fastdissolve
    le "Enough! I'm leaving your harem and from now on, you shall call me CHIEF again, understood?"
    mc "Roger that. Chief."
    call LustMinusLena
    window hide
    hide lena10 with dissolve
    $ haremle = False
    $ girlsinharem -= 1
if weekfuckedlena == False and haremle and lustle == 5:
    show lena03 at centerleft with moveinleft
    le "You're even worse that Jake! He's got a small tiny dicklet, but at least he FUCKS ME!"
    mc "I was too busy doing quests and shit, you know stuff you GAVE me to do and..."
    hide lena03
    show lena06 at centerleft
    with fastdissolve
    le "Excuses, always excuses! I grow tired of them and that makes my lust go down."
    call LustMinusLena
    mc "Ah. So lust of 4 now, right at the edge then..."
    hide lena06 with dissolve
    
label HaremNextPreBarbara:
if haremba and lustba <= 3:
    show barbara07 at centerleft with moveinleft
    ba "I thought you would be a GREAT harem Master but it turns out you are a do-nothing lousy one!"
    mc "I should give becoming a politician a shot then."
    hide barbara07
    show barbara03 at centerleft
    with fastdissolve
    ba "NOT as a Trumpster! Not until you show your devotion and loyalty to the Greatness of New America by being a decent harem Master."
    mc "Oh well."
    window hide
    hide barbara03 with dissolve
    $ haremba = False
    $ girlsinharem -= 1
    jump HaremNextPreBella
if weekfuckedbarbara == False and haremba and lustba <= 4:
    show barbara07 at centerleft with moveinleft
    ba "I thought you would be a GREAT harem Master but it turns out you are a do-nothing lousy one!"
    mc "What didn't I do nothing about?"
    hide barbara07
    show barbara03 at centerleft
    with fastdissolve
    ba "You did not SATISFY my sexual needs, that's what! So I'm leaving your harem."
    mc "Oh well."
    call LustMinusBarbara
    window hide
    hide barbara03 with dissolve
    $ haremba = False
    $ girlsinharem -= 1
if weekfuckedbarbara == False and haremba and lustba == 5:
    show barbara07 at centerleft with moveinleft
    ba "I thought you would be a GREAT harem Master but it turns out you are a do-nothing lousy one!"
    mc "What didn't I do nothing about?"
    hide barbara07
    show barbara03 at centerleft
    with fastdissolve
    ba "You did not SATISFY my sexual needs, that's what! You'd better up your game because I won't stay in your harem that much longer if you can't FUCK me properly."
    call LustMinusBarbara
    mc "Ah. So lust of 4 now, right at the edge then..."
    hide barbara03 with dissolve

label HaremNextPreBella:
if bellajustjoined:
    jump HaremNextPreInterface
if harembe and lustbe <= 3:
    show bella07 at centerleft with moveinleft
    be "You were supposed to make sure I stay in your harem and you somehow managed to anger the Phallus Lord!"
    mc "Him again? Always pestering me..."
    hide bella07
    show bean at centerleft
    with fastdissolve
    be "Yeah, well he made my lust for you fall dramatically. Below the minimum required level to stay in your sinful harem. So adios!"
    mc "Oh well."
    window hide
    hide bean with dissolve
    $ harembe = False
    $ girlsinharem -= 1
    jump HaremNextPreInterface
if weekfuckedbella == False and harembe and lustbe <= 4:
    show bella07 at centerleft with moveinleft
    be "You were supposed to make sure I stay in your harem and you somehow managed to anger the Phallus Lord!"
    mc "Him again? Always pestering me..."
    hide bella07
    show bean at centerleft
    with fastdissolve
    be "Yeah, well you should have use your PHALLUS this week on me and you didn't! So Adios!"
    mc "Oh well."
    call LustMinusBella
    window hide
    hide bella03 with dissolve
    $ harembe = False
    $ girlsinharem -= 1
if weekfuckedbella == False and harembe and lustbe == 5:
    show bean at centerleft with moveinleft
    be "What is wrong with you? The Phallus Lord protects you and your phallus and you can't even be bothered USING IT!"
    mc "I forgot to fuck you this week, is that it?"
    hide bean
    show bella07 at centerleft
    with fastdissolve
    be "NOW you remember. You're lucky I'm not leaving your sinful harem. Just yet."
    call LustMinusBella
    mc "Ah. So lust of 4 now, right at the edge then..."
    hide barbara03 with dissolve
        
if haremza == False and haremde == False and haremle == False and haremba == False and haremla == False and haremcl == False and hareman == False and haremma == False and haremmo == False and haremmi == False and haremcy == False and haremru == False and haremam == False and harempe == False and haremay == False and haremsu == False and haremgw == False:
    return

label HaremNextPreInterface:
$ bellajustjoined = False
show hareminterface at poshareminterface
$ renpy.pause(0.5, hard=True)   
label HaremMaintenance:
if (haremza and maintenanceza == False) or (haremde and maintenancede == False) or (haremba and maintenanceba == False) or (harembe and maintenancebe == False) or (haremle and maintenancele == False) or (haremla and maintenancela == False) or (haremcl and maintenancecl == False) or (haremma and maintenancema == False) or (hareman and maintenancean == False) or (haremmo and maintenancemo == False) or (haremam and maintenanceam == False) or (harempe and maintenancepe == False) or (haremay and maintenanceay == False) or (haremsu and maintenancesu == False) or (haremgw and maintenancegw == False) or (haremmi and maintenancemi == False) or (haremcy and maintenancecy == False) or (haremru and maintenanceru == False):
    call screen hareminterface01
hide hareminterface
show screen mcstats
show screen calendar
return

screen hareminterface01:
    add "Icons/hareminterface.png" at poshareminterface02
    modal True
    $ haremintpos = 0

    if haremza and maintenanceza:
        $ haremintpos += 1
        add "Icons/haremzara.png" at posharem01
    if haremza and maintenanceza == False:
        $ haremintpos += 1
        add "Icons/haremzara.png" at posharem01
        imagebutton:
            focus_mask True
            idle "Icons/dismiss01.png"
            hover "Icons/dismiss01.png"
            action Jump ("ZaraDismiss")    
        imagebutton:
            focus_mask True
            idle "Icons/maintenance01.png"
            hover "Icons/maintenance01.png"
            action Jump ("ZaraMaintain")

    if hareman and maintenancean:
        $ haremintpos += 1
        if haremintpos == 1:
            add "Icons/haremangie.png" at posharem01        
        if haremintpos == 2:
            add "Icons/haremangie.png" at posharem02
    if hareman and maintenancean == False:
        $ haremintpos += 1
        if haremintpos == 1:
            add "Icons/haremangie.png" at posharem01
            imagebutton:
                focus_mask True
                idle "Icons/dismiss01.png"
                hover "Icons/dismiss01.png"
                action Jump ("AngieDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance01.png"
                hover "Icons/maintenance01.png"
                action Jump ("AngieMaintain")    
        if haremintpos == 2:
            add "Icons/haremangie.png" at posharem02
            imagebutton:
                focus_mask True
                idle "Icons/dismiss02.png"
                hover "Icons/dismiss02.png"
                action Jump ("AngieDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance02.png"
                hover "Icons/maintenance02.png"
                action Jump ("AngieMaintain")

    if haremmo and maintenancemo:
        $ haremintpos += 1
        if haremintpos == 1:
            add "Icons/haremnancy.png" at posharem01        
        if haremintpos == 2:
            add "Icons/haremnancy.png" at posharem02        
        if haremintpos == 3:
            add "Icons/haremnancy.png" at posharem03        
    if haremmo and maintenancemo == False:
        $ haremintpos += 1
        if haremintpos == 1:
            add "Icons/haremnancy.png" at posharem01
            imagebutton:
                focus_mask True
                idle "Icons/dismiss01.png"
                hover "Icons/dismiss01.png"
                action Jump ("NancyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance01.png"
                hover "Icons/maintenance01.png"
                action Jump ("NancyMaintain")    
        if haremintpos == 2:
            add "Icons/haremnancy.png" at posharem02
            imagebutton:
                focus_mask True
                idle "Icons/dismiss02.png"
                hover "Icons/dismiss02.png"
                action Jump ("NancyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance02.png"
                hover "Icons/maintenance02.png"
                action Jump ("NancyMaintain")    
        if haremintpos == 3:
            add "Icons/haremnancy.png" at posharem03
            imagebutton:
                focus_mask True
                idle "Icons/dismiss03.png"
                hover "Icons/dismiss03.png"
                action Jump ("NancyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance03.png"
                hover "Icons/maintenance03.png"
                action Jump ("NancyMaintain")    

    if haremmi and maintenancemi:
        $ haremintpos += 1
        if haremintpos == 1:
            add "Icons/haremmichiko.png" at posharem01        
        if haremintpos == 2:
            add "Icons/haremmichiko.png" at posharem02        
        if haremintpos == 3:
            add "Icons/haremmichiko.png" at posharem03        
        if haremintpos == 4:
            add "Icons/haremmichiko.png" at posharem04        
    if haremmi and maintenancemi == False:
        $ haremintpos += 1
        if haremintpos == 1:
            add "Icons/haremmichiko.png" at posharem01
            imagebutton:
                focus_mask True
                idle "Icons/dismiss01.png"
                hover "Icons/dismiss01.png"
                action Jump ("MichikoDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance01.png"
                hover "Icons/maintenance01.png"
                action Jump ("MichikoMaintain")    
        if haremintpos == 2:
            add "Icons/haremmichiko.png" at posharem02
            imagebutton:
                focus_mask True
                idle "Icons/dismiss02.png"
                hover "Icons/dismiss02.png"
                action Jump ("MichikoDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance02.png"
                hover "Icons/maintenance02.png"
                action Jump ("MichikoMaintain")    
        if haremintpos == 3:
            add "Icons/haremmichiko.png" at posharem03
            imagebutton:
                focus_mask True
                idle "Icons/dismiss03.png"
                hover "Icons/dismiss03.png"
                action Jump ("MichikoDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance03.png"
                hover "Icons/maintenance03.png"
                action Jump ("MichikoMaintain")    
        if haremintpos == 4:
            add "Icons/haremmichiko.png" at posharem04
            imagebutton:
                focus_mask True
                idle "Icons/dismiss04.png"
                hover "Icons/dismiss04.png"
                action Jump ("MichikoDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance04.png"
                hover "Icons/maintenance04.png"
                action Jump ("MichikoMaintain")    

    if haremcy and maintenancecy:
        $ haremintpos += 1
        if haremintpos == 1:
            add "Icons/haremcyrl.png" at posharem01        
        if haremintpos == 2:
            add "Icons/haremcyrl.png" at posharem02        
        if haremintpos == 3:
            add "Icons/haremcyrl.png" at posharem03        
        if haremintpos == 4:
            add "Icons/haremcyrl.png" at posharem04        
        if haremintpos == 5:
            add "Icons/haremcyrl.png" at posharem05        
    if haremcy and maintenancecy == False:
        $ haremintpos += 1
        if haremintpos == 1:
            add "Icons/haremcyrl.png" at posharem01
            imagebutton:
                focus_mask True
                idle "Icons/dismiss01.png"
                hover "Icons/dismiss01.png"
                action Jump ("CyrlDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance01.png"
                hover "Icons/maintenance01.png"
                action Jump ("CyrlMaintain")    
        if haremintpos == 2:
            add "Icons/haremcyrl.png" at posharem02
            imagebutton:
                focus_mask True
                idle "Icons/dismiss02.png"
                hover "Icons/dismiss02.png"
                action Jump ("CyrlDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance02.png"
                hover "Icons/maintenance02.png"
                action Jump ("CyrlMaintain")    
        if haremintpos == 3:
            add "Icons/haremcyrl.png" at posharem03
            imagebutton:
                focus_mask True
                idle "Icons/dismiss03.png"
                hover "Icons/dismiss03.png"
                action Jump ("CyrlDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance03.png"
                hover "Icons/maintenance03.png"
                action Jump ("CyrlMaintain")    
        if haremintpos == 4:
            add "Icons/haremcyrl.png" at posharem04
            imagebutton:
                focus_mask True
                idle "Icons/dismiss04.png"
                hover "Icons/dismiss04.png"
                action Jump ("CyrlDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance04.png"
                hover "Icons/maintenance04.png"
                action Jump ("CyrlMaintain")    
        if haremintpos == 5:
            add "Icons/haremcyrl.png" at posharem05
            imagebutton:
                focus_mask True
                idle "Icons/dismiss05.png"
                hover "Icons/dismiss05.png"
                action Jump ("CyrlDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance05.png"
                hover "Icons/maintenance05.png"
                action Jump ("CyrlMaintain")    

    if haremru and maintenanceru:
        $ haremintpos += 1
        if haremintpos == 1:
            add "Icons/haremruby.png" at posharem01        
        if haremintpos == 2:
            add "Icons/haremruby.png" at posharem02        
        if haremintpos == 3:
            add "Icons/haremruby.png" at posharem03        
        if haremintpos == 4:
            add "Icons/haremruby.png" at posharem04        
        if haremintpos == 5:
            add "Icons/haremruby.png" at posharem05        
        if haremintpos == 6:
            add "Icons/haremruby.png" at posharem06        
    if haremru and maintenanceru == False:
        $ haremintpos += 1
        if haremintpos == 1:
            add "Icons/haremruby.png" at posharem01
            imagebutton:
                focus_mask True
                idle "Icons/dismiss01.png"
                hover "Icons/dismiss01.png"
                action Jump ("RubyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance01.png"
                hover "Icons/maintenance01.png"
                action Jump ("RubyMaintain")    
        if haremintpos == 2:
            add "Icons/haremruby.png" at posharem02
            imagebutton:
                focus_mask True
                idle "Icons/dismiss02.png"
                hover "Icons/dismiss02.png"
                action Jump ("RubyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance02.png"
                hover "Icons/maintenance02.png"
                action Jump ("RubyMaintain")    
        if haremintpos == 3:
            add "Icons/haremruby.png" at posharem03
            imagebutton:
                focus_mask True
                idle "Icons/dismiss03.png"
                hover "Icons/dismiss03.png"
                action Jump ("RubyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance03.png"
                hover "Icons/maintenance03.png"
                action Jump ("RubyMaintain")    
        if haremintpos == 4:
            add "Icons/haremruby.png" at posharem04
            imagebutton:
                focus_mask True
                idle "Icons/dismiss04.png"
                hover "Icons/dismiss04.png"
                action Jump ("RubyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance04.png"
                hover "Icons/maintenance04.png"
                action Jump ("RubyMaintain")    
        if haremintpos == 5:
            add "Icons/haremruby.png" at posharem05
            imagebutton:
                focus_mask True
                idle "Icons/dismiss05.png"
                hover "Icons/dismiss05.png"
                action Jump ("RubyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance05.png"
                hover "Icons/maintenance05.png"
                action Jump ("RubyMaintain")    
        if haremintpos == 6:
            add "Icons/haremruby.png" at posharem06
            imagebutton:
                focus_mask True
                idle "Icons/dismiss06.png"
                hover "Icons/dismiss06.png"
                action Jump ("RubyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance06.png"
                hover "Icons/maintenance06.png"
                action Jump ("RubyMaintain")    

    if haremam and maintenanceam:
        $ haremintpos += 1
        if haremintpos == 1:
            add "Icons/haremamy.png" at posharem01        
        if haremintpos == 2:
            add "Icons/haremamy.png" at posharem02        
        if haremintpos == 3:
            add "Icons/haremamy.png" at posharem03        
        if haremintpos == 4:
            add "Icons/haremamy.png" at posharem04        
        if haremintpos == 5:
            add "Icons/haremamy.png" at posharem05        
        if haremintpos == 6:
            add "Icons/haremamy.png" at posharem06        

    if haremam and maintenanceam == False:
        $ haremintpos += 1
        if haremintpos == 1:
            add "Icons/haremamy.png" at posharem01
            imagebutton:
                focus_mask True
                idle "Icons/dismiss01.png"
                hover "Icons/dismiss01.png"
                action Jump ("AmyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance01.png"
                hover "Icons/maintenance01.png"
                action Jump ("AmyMaintain")    
        if haremintpos == 2:
            add "Icons/haremamy.png" at posharem02
            imagebutton:
                focus_mask True
                idle "Icons/dismiss02.png"
                hover "Icons/dismiss02.png"
                action Jump ("AmyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance02.png"
                hover "Icons/maintenance02.png"
                action Jump ("AmyMaintain")    
        if haremintpos == 3:
            add "Icons/haremamy.png" at posharem03
            imagebutton:
                focus_mask True
                idle "Icons/dismiss03.png"
                hover "Icons/dismiss03.png"
                action Jump ("AmyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance03.png"
                hover "Icons/maintenance03.png"
                action Jump ("AmyMaintain")    
        if haremintpos == 4:
            add "Icons/haremamy.png" at posharem04
            imagebutton:
                focus_mask True
                idle "Icons/dismiss04.png"
                hover "Icons/dismiss04.png"
                action Jump ("AmyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance04.png"
                hover "Icons/maintenance04.png"
                action Jump ("AmyMaintain")    
        if haremintpos == 5:
            add "Icons/haremamy.png" at posharem05
            imagebutton:
                focus_mask True
                idle "Icons/dismiss05.png"
                hover "Icons/dismiss05.png"
                action Jump ("AmyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance05.png"
                hover "Icons/maintenance05.png"
                action Jump ("AmyMaintain")    
        if haremintpos == 6:
            add "Icons/haremamy.png" at posharem06
            imagebutton:
                focus_mask True
                idle "Icons/dismiss06.png"
                hover "Icons/dismiss06.png"
                action Jump ("AmyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance06.png"
                hover "Icons/maintenance06.png"
                action Jump ("AmyMaintain")    

    if haremay and maintenanceay:
        $ haremintpos += 1
        if haremintpos == 1:
            add "Icons/haremayla.png" at posharem01        
        if haremintpos == 2:
            add "Icons/haremayla.png" at posharem02        
        if haremintpos == 3:
            add "Icons/haremayla.png" at posharem03        
        if haremintpos == 4:
            add "Icons/haremayla.png" at posharem04        
        if haremintpos == 5:
            add "Icons/haremayla.png" at posharem05        
        if haremintpos == 6:
            add "Icons/haremayla.png" at posharem06        

    if haremay and maintenanceay == False:
        $ haremintpos += 1
        if haremintpos == 1:
            add "Icons/haremayla.png" at posharem01
            imagebutton:
                focus_mask True
                idle "Icons/dismiss01.png"
                hover "Icons/dismiss01.png"
                action Jump ("AylaDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance01.png"
                hover "Icons/maintenance01.png"
                action Jump ("AylaMaintain")    
        if haremintpos == 2:
            add "Icons/haremayla.png" at posharem02
            imagebutton:
                focus_mask True
                idle "Icons/dismiss02.png"
                hover "Icons/dismiss02.png"
                action Jump ("AylaDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance02.png"
                hover "Icons/maintenance02.png"
                action Jump ("AylaMaintain")    
        if haremintpos == 3:
            add "Icons/haremayla.png" at posharem03
            imagebutton:
                focus_mask True
                idle "Icons/dismiss03.png"
                hover "Icons/dismiss03.png"
                action Jump ("AylaDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance03.png"
                hover "Icons/maintenance03.png"
                action Jump ("AylaMaintain")    
        if haremintpos == 4:
            add "Icons/haremayla.png" at posharem04
            imagebutton:
                focus_mask True
                idle "Icons/dismiss04.png"
                hover "Icons/dismiss04.png"
                action Jump ("AylaDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance04.png"
                hover "Icons/maintenance04.png"
                action Jump ("AylaMaintain")    
        if haremintpos == 5:
            add "Icons/haremayla.png" at posharem05
            imagebutton:
                focus_mask True
                idle "Icons/dismiss05.png"
                hover "Icons/dismiss05.png"
                action Jump ("AylaDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance05.png"
                hover "Icons/maintenance05.png"
                action Jump ("AylaMaintain")    
        if haremintpos == 6:
            add "Icons/haremayla.png" at posharem06
            imagebutton:
                focus_mask True
                idle "Icons/dismiss06.png"
                hover "Icons/dismiss06.png"
                action Jump ("AylaDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance06.png"
                hover "Icons/maintenance06.png"
                action Jump ("AylaMaintain")    

    if haremsu and maintenancesu:
        $ haremintpos += 1
        if haremintpos == 1:
            add "Icons/haremsuki.png" at posharem01        
        if haremintpos == 2:
            add "Icons/haremsuki.png" at posharem02        
        if haremintpos == 3:
            add "Icons/haremsuki.png" at posharem03        
        if haremintpos == 4:
            add "Icons/haremsuki.png" at posharem04        
        if haremintpos == 5:
            add "Icons/haremsuki.png" at posharem05        
        if haremintpos == 6:
            add "Icons/haremsuki.png" at posharem06        

    if haremsu and maintenancesu == False:
        $ haremintpos += 1
        if haremintpos == 1:
            add "Icons/haremsuki.png" at posharem01
            imagebutton:
                focus_mask True
                idle "Icons/dismiss01.png"
                hover "Icons/dismiss01.png"
                action Jump ("SukiDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance01.png"
                hover "Icons/maintenance01.png"
                action Jump ("SukiMaintain")    
        if haremintpos == 2:
            add "Icons/haremsuki.png" at posharem02
            imagebutton:
                focus_mask True
                idle "Icons/dismiss02.png"
                hover "Icons/dismiss02.png"
                action Jump ("SukiDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance02.png"
                hover "Icons/maintenance02.png"
                action Jump ("SukiMaintain")    
        if haremintpos == 3:
            add "Icons/haremsuki.png" at posharem03
            imagebutton:
                focus_mask True
                idle "Icons/dismiss03.png"
                hover "Icons/dismiss03.png"
                action Jump ("SukiDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance03.png"
                hover "Icons/maintenance03.png"
                action Jump ("SukiMaintain")    
        if haremintpos == 4:
            add "Icons/haremsuki.png" at posharem04
            imagebutton:
                focus_mask True
                idle "Icons/dismiss04.png"
                hover "Icons/dismiss04.png"
                action Jump ("SukiDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance04.png"
                hover "Icons/maintenance04.png"
                action Jump ("SukiMaintain")    
        if haremintpos == 5:
            add "Icons/haremsuki.png" at posharem05
            imagebutton:
                focus_mask True
                idle "Icons/dismiss05.png"
                hover "Icons/dismiss05.png"
                action Jump ("SukiDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance05.png"
                hover "Icons/maintenance05.png"
                action Jump ("SukiMaintain")    
        if haremintpos == 6:
            add "Icons/haremsuki.png" at posharem06
            imagebutton:
                focus_mask True
                idle "Icons/dismiss06.png"
                hover "Icons/dismiss06.png"
                action Jump ("SukiDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance06.png"
                hover "Icons/maintenance06.png"
                action Jump ("SukiMaintain")    

    if haremgw and maintenancegw:
        $ haremintpos += 1
        if haremintpos == 1:
            add "Icons/haremgwen.png" at posharem01        
        if haremintpos == 2:
            add "Icons/haremgwen.png" at posharem02        
        if haremintpos == 3:
            add "Icons/haremgwen.png" at posharem03        
        if haremintpos == 4:
            add "Icons/haremgwen.png" at posharem04        
        if haremintpos == 5:
            add "Icons/haremgwen.png" at posharem05        
        if haremintpos == 6:
            add "Icons/haremgwen.png" at posharem06        

    if haremgw and maintenancegw == False:
        $ haremintpos += 1
        if haremintpos == 1:
            add "Icons/haremgwen.png" at posharem01
            imagebutton:
                focus_mask True
                idle "Icons/dismiss01.png"
                hover "Icons/dismiss01.png"
                action Jump ("GwenDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance01.png"
                hover "Icons/maintenance01.png"
                action Jump ("GwenMaintain")    
        if haremintpos == 2:
            add "Icons/haremgwen.png" at posharem02
            imagebutton:
                focus_mask True
                idle "Icons/dismiss02.png"
                hover "Icons/dismiss02.png"
                action Jump ("GwenDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance02.png"
                hover "Icons/maintenance02.png"
                action Jump ("GwenMaintain")    
        if haremintpos == 3:
            add "Icons/haremgwen.png" at posharem03
            imagebutton:
                focus_mask True
                idle "Icons/dismiss03.png"
                hover "Icons/dismiss03.png"
                action Jump ("GwenDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance03.png"
                hover "Icons/maintenance03.png"
                action Jump ("GwenMaintain")    
        if haremintpos == 4:
            add "Icons/haremgwen.png" at posharem04
            imagebutton:
                focus_mask True
                idle "Icons/dismiss04.png"
                hover "Icons/dismiss04.png"
                action Jump ("GwenDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance04.png"
                hover "Icons/maintenance04.png"
                action Jump ("GwenMaintain")    
        if haremintpos == 5:
            add "Icons/haremgwen.png" at posharem05
            imagebutton:
                focus_mask True
                idle "Icons/dismiss05.png"
                hover "Icons/dismiss05.png"
                action Jump ("GwenDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance05.png"
                hover "Icons/maintenance05.png"
                action Jump ("GwenMaintain")    
        if haremintpos == 6:
            add "Icons/haremgwen.png" at posharem06
            imagebutton:
                focus_mask True
                idle "Icons/dismiss06.png"
                hover "Icons/dismiss06.png"
                action Jump ("GwenDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance06.png"
                hover "Icons/maintenance06.png"
                action Jump ("GwenMaintain")

    if harempe and maintenancepe:
        $ haremintpos += 1
        if haremintpos == 1:
            add "v061/harempenny.png" at posharem01        
        if haremintpos == 2:
            add "v061/harempenny.png" at posharem02        
        if haremintpos == 3:
            add "v061/harempenny.png" at posharem03        
        if haremintpos == 4:
            add "v061/harempenny.png" at posharem04        
        if haremintpos == 5:
            add "v061/harempenny.png" at posharem05        
        if haremintpos == 6:
            add "v061/harempenny.png" at posharem06        

    if harempe and maintenancepe == False:
        $ haremintpos += 1
        if haremintpos == 1:
            add "v061/harempenny.png" at posharem01
            imagebutton:
                focus_mask True
                idle "Icons/dismiss01.png"
                hover "Icons/dismiss01.png"
                action Jump ("PennyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance01.png"
                hover "Icons/maintenance01.png"
                action Jump ("PennyMaintain")    
        if haremintpos == 2:
            add "v061/harempenny.png" at posharem02
            imagebutton:
                focus_mask True
                idle "Icons/dismiss02.png"
                hover "Icons/dismiss02.png"
                action Jump ("PennyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance02.png"
                hover "Icons/maintenance02.png"
                action Jump ("PennyMaintain")    
        if haremintpos == 3:
            add "v061/harempenny.png" at posharem03
            imagebutton:
                focus_mask True
                idle "Icons/dismiss03.png"
                hover "Icons/dismiss03.png"
                action Jump ("PennyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance03.png"
                hover "Icons/maintenance03.png"
                action Jump ("PennyMaintain")    
        if haremintpos == 4:
            add "v061/harempenny.png" at posharem04
            imagebutton:
                focus_mask True
                idle "Icons/dismiss04.png"
                hover "Icons/dismiss04.png"
                action Jump ("PennyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance04.png"
                hover "Icons/maintenance04.png"
                action Jump ("PennyMaintain")    
        if haremintpos == 5:
            add "v061/harempenny.png" at posharem05
            imagebutton:
                focus_mask True
                idle "Icons/dismiss05.png"
                hover "Icons/dismiss05.png"
                action Jump ("PennyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance05.png"
                hover "Icons/maintenance05.png"
                action Jump ("PennyMaintain")    
        if haremintpos == 6:
            add "v061/harempenny.png" at posharem06
            imagebutton:
                focus_mask True
                idle "Icons/dismiss06.png"
                hover "Icons/dismiss06.png"
                action Jump ("PennyDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance06.png"
                hover "Icons/maintenance06.png"
                action Jump ("PennyMaintain")

    if haremma and maintenancema:
        $ haremintpos += 1
        if haremintpos == 1:
            add "v07/haremmarnie.png" at posharem01        
        if haremintpos == 2:
            add "v07/haremmarnie.png" at posharem02        
        if haremintpos == 3:
            add "v07/haremmarnie.png" at posharem03        
        if haremintpos == 4:
            add "v07/haremmarnie.png" at posharem04        
        if haremintpos == 5:
            add "v07/haremmarnie.png" at posharem05        
        if haremintpos == 6:
            add "v07/haremmarnie.png" at posharem06        

    if haremma and maintenancema == False:
        $ haremintpos += 1
        if haremintpos == 1:
            add "v07/haremmarnie.png" at posharem01
            imagebutton:
                focus_mask True
                idle "Icons/dismiss01.png"
                hover "Icons/dismiss01.png"
                action Jump ("MarnieDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance01.png"
                hover "Icons/maintenance01.png"
                action Jump ("MarnieMaintain")    
        if haremintpos == 2:
            add "v07/haremmarnie.png" at posharem02
            imagebutton:
                focus_mask True
                idle "Icons/dismiss02.png"
                hover "Icons/dismiss02.png"
                action Jump ("MarnieDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance02.png"
                hover "Icons/maintenance02.png"
                action Jump ("MarnieMaintain")    
        if haremintpos == 3:
            add "v07/haremmarnie.png" at posharem03
            imagebutton:
                focus_mask True
                idle "Icons/dismiss03.png"
                hover "Icons/dismiss03.png"
                action Jump ("MarnieDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance03.png"
                hover "Icons/maintenance03.png"
                action Jump ("MarnieMaintain")    
        if haremintpos == 4:
            add "v07/haremmarnie.png" at posharem04
            imagebutton:
                focus_mask True
                idle "Icons/dismiss04.png"
                hover "Icons/dismiss04.png"
                action Jump ("MarnieDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance04.png"
                hover "Icons/maintenance04.png"
                action Jump ("MarnieMaintain")    
        if haremintpos == 5:
            add "v07/haremmarnie.png" at posharem05
            imagebutton:
                focus_mask True
                idle "Icons/dismiss05.png"
                hover "Icons/dismiss05.png"
                action Jump ("MarnieDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance05.png"
                hover "Icons/maintenance05.png"
                action Jump ("MarnieMaintain")    
        if haremintpos == 6:
            add "v07/haremmarnie.png" at posharem06
            imagebutton:
                focus_mask True
                idle "Icons/dismiss06.png"
                hover "Icons/dismiss06.png"
                action Jump ("MarnieDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance06.png"
                hover "Icons/maintenance06.png"
                action Jump ("MarnieMaintain")

    if haremcl and maintenancecl:
        $ haremintpos += 1
        if haremintpos == 1:
            add "v071/haremclara.png" at posharem01        
        if haremintpos == 2:
            add "v071/haremclara.png" at posharem02        
        if haremintpos == 3:
            add "v071/haremclara.png" at posharem03        
        if haremintpos == 4:
            add "v071/haremclara.png" at posharem04        
        if haremintpos == 5:
            add "v071/haremclara.png" at posharem05        
        if haremintpos == 6:
            add "v071/haremclara.png" at posharem06        

    if haremcl and maintenancecl == False:
        $ haremintpos += 1
        if haremintpos == 1:
            add "v071/haremclara.png" at posharem01
            imagebutton:
                focus_mask True
                idle "Icons/dismiss01.png"
                hover "Icons/dismiss01.png"
                action Jump ("ClaraDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance01.png"
                hover "Icons/maintenance01.png"
                action Jump ("ClaraMaintain")    
        if haremintpos == 2:
            add "v071/haremclara.png" at posharem02
            imagebutton:
                focus_mask True
                idle "Icons/dismiss02.png"
                hover "Icons/dismiss02.png"
                action Jump ("ClaraDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance02.png"
                hover "Icons/maintenance02.png"
                action Jump ("ClaraMaintain")    
        if haremintpos == 3:
            add "v071/haremclara.png" at posharem03
            imagebutton:
                focus_mask True
                idle "Icons/dismiss03.png"
                hover "Icons/dismiss03.png"
                action Jump ("ClaraDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance03.png"
                hover "Icons/maintenance03.png"
                action Jump ("ClaraMaintain")    
        if haremintpos == 4:
            add "v071/haremclara.png" at posharem04
            imagebutton:
                focus_mask True
                idle "Icons/dismiss04.png"
                hover "Icons/dismiss04.png"
                action Jump ("ClaraDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance04.png"
                hover "Icons/maintenance04.png"
                action Jump ("ClaraMaintain")    
        if haremintpos == 5:
            add "v071/haremclara.png" at posharem05
            imagebutton:
                focus_mask True
                idle "Icons/dismiss05.png"
                hover "Icons/dismiss05.png"
                action Jump ("ClaraDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance05.png"
                hover "Icons/maintenance05.png"
                action Jump ("ClaraMaintain")    
        if haremintpos == 6:
            add "v071/haremclara.png" at posharem06
            imagebutton:
                focus_mask True
                idle "Icons/dismiss06.png"
                hover "Icons/dismiss06.png"
                action Jump ("ClaraDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance06.png"
                hover "Icons/maintenance06.png"
                action Jump ("ClaraMaintain")

    if haremla and maintenancela:
        $ haremintpos += 1
        if haremintpos == 1:
            add "v072/haremlaurie.png" at posharem01        
        if haremintpos == 2:
            add "v072/haremlaurie.png" at posharem02        
        if haremintpos == 3:
            add "v072/haremlaurie.png" at posharem03        
        if haremintpos == 4:
            add "v072/haremlaurie.png" at posharem04        
        if haremintpos == 5:
            add "v072/haremlaurie.png" at posharem05        
        if haremintpos == 6:
            add "v072/haremlaurie.png" at posharem06        

    if haremla and maintenancela == False:
        $ haremintpos += 1
        if haremintpos == 1:
            add "v072/haremlaurie.png" at posharem01
            imagebutton:
                focus_mask True
                idle "Icons/dismiss01.png"
                hover "Icons/dismiss01.png"
                action Jump ("LaurieDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance01.png"
                hover "Icons/maintenance01.png"
                action Jump ("LaurieMaintain")    
        if haremintpos == 2:
            add "v072/haremlaurie.png" at posharem02
            imagebutton:
                focus_mask True
                idle "Icons/dismiss02.png"
                hover "Icons/dismiss02.png"
                action Jump ("LaurieDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance02.png"
                hover "Icons/maintenance02.png"
                action Jump ("LaurieMaintain")    
        if haremintpos == 3:
            add "v072/haremlaurie.png" at posharem03
            imagebutton:
                focus_mask True
                idle "Icons/dismiss03.png"
                hover "Icons/dismiss03.png"
                action Jump ("LaurieDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance03.png"
                hover "Icons/maintenance03.png"
                action Jump ("LaurieMaintain")    
        if haremintpos == 4:
            add "v072/haremlaurie.png" at posharem04
            imagebutton:
                focus_mask True
                idle "Icons/dismiss04.png"
                hover "Icons/dismiss04.png"
                action Jump ("LaurieDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance04.png"
                hover "Icons/maintenance04.png"
                action Jump ("LaurieMaintain")    
        if haremintpos == 5:
            add "v072/haremlaurie.png" at posharem05
            imagebutton:
                focus_mask True
                idle "Icons/dismiss05.png"
                hover "Icons/dismiss05.png"
                action Jump ("LaurieDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance05.png"
                hover "Icons/maintenance05.png"
                action Jump ("LaurieMaintain")    
        if haremintpos == 6:
            add "v072/haremlaurie.png" at posharem06
            imagebutton:
                focus_mask True
                idle "Icons/dismiss06.png"
                hover "Icons/dismiss06.png"
                action Jump ("LaurieDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance06.png"
                hover "Icons/maintenance06.png"
                action Jump ("LaurieMaintain")
                
    if haremle and maintenancele:
        $ haremintpos += 1
        if haremintpos == 1:
            add "v08/haremlena.png" at posharem01        
        if haremintpos == 2:
            add "v08/haremlena.png" at posharem02        
        if haremintpos == 3:
            add "v08/haremlena.png" at posharem03        
        if haremintpos == 4:
            add "v08/haremlena.png" at posharem04        
        if haremintpos == 5:
            add "v08/haremlena.png" at posharem05        
        if haremintpos == 6:
            add "v08/haremlena.png" at posharem06        

    if haremle and maintenancele == False:
        $ haremintpos += 1
        if haremintpos == 1:
            add "v08/haremlena.png" at posharem01
            imagebutton:
                focus_mask True
                idle "Icons/dismiss01.png"
                hover "Icons/dismiss01.png"
                action Jump ("LenaDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance01.png"
                hover "Icons/maintenance01.png"
                action Jump ("LenaMaintain")    
        if haremintpos == 2:
            add "v08/haremlena.png" at posharem02
            imagebutton:
                focus_mask True
                idle "Icons/dismiss02.png"
                hover "Icons/dismiss02.png"
                action Jump ("LenaDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance02.png"
                hover "Icons/maintenance02.png"
                action Jump ("LenaMaintain")    
        if haremintpos == 3:
            add "v08/haremlena.png" at posharem03
            imagebutton:
                focus_mask True
                idle "Icons/dismiss03.png"
                hover "Icons/dismiss03.png"
                action Jump ("LenaDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance03.png"
                hover "Icons/maintenance03.png"
                action Jump ("LenaMaintain")    
        if haremintpos == 4:
            add "v08/haremlena.png" at posharem04
            imagebutton:
                focus_mask True
                idle "Icons/dismiss04.png"
                hover "Icons/dismiss04.png"
                action Jump ("LenaDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance04.png"
                hover "Icons/maintenance04.png"
                action Jump ("LenaMaintain")    
        if haremintpos == 5:
            add "v08/haremlena.png" at posharem05
            imagebutton:
                focus_mask True
                idle "Icons/dismiss05.png"
                hover "Icons/dismiss05.png"
                action Jump ("LenaDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance05.png"
                hover "Icons/maintenance05.png"
                action Jump ("LenaMaintain")    
        if haremintpos == 6:
            add "v08/haremlena.png" at posharem06
            imagebutton:
                focus_mask True
                idle "Icons/dismiss06.png"
                hover "Icons/dismiss06.png"
                action Jump ("LenaDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance06.png"
                hover "Icons/maintenance06.png"
                action Jump ("LenaMaintain")

    if haremba and maintenanceba:
        $ haremintpos += 1
        if haremintpos == 1:
            add "v081/harembarbara.png" at posharem01        
        if haremintpos == 2:
            add "v081/harembarbara.png" at posharem02        
        if haremintpos == 3:
            add "v081/harembarbara.png" at posharem03        
        if haremintpos == 4:
            add "v081/harembarbara.png" at posharem04        
        if haremintpos == 5:
            add "v081/harembarbara.png" at posharem05        
        if haremintpos == 6:
            add "v081/harembarbara.png" at posharem06        

    if haremba and maintenanceba == False:
        $ haremintpos += 1
        if haremintpos == 1:
            add "v081/harembarbara.png" at posharem01
            imagebutton:
                focus_mask True
                idle "Icons/dismiss01.png"
                hover "Icons/dismiss01.png"
                action Jump ("BarbaraDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance01.png"
                hover "Icons/maintenance01.png"
                action Jump ("BarbaraMaintain")    
        if haremintpos == 2:
            add "v081/harembarbara.png" at posharem02
            imagebutton:
                focus_mask True
                idle "Icons/dismiss02.png"
                hover "Icons/dismiss02.png"
                action Jump ("BarbaraDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance02.png"
                hover "Icons/maintenance02.png"
                action Jump ("BarbaraMaintain")    
        if haremintpos == 3:
            add "v081/harembarbara.png" at posharem03
            imagebutton:
                focus_mask True
                idle "Icons/dismiss03.png"
                hover "Icons/dismiss03.png"
                action Jump ("BarbaraDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance03.png"
                hover "Icons/maintenance03.png"
                action Jump ("BarbaraMaintain")    
        if haremintpos == 4:
            add "v081/harembarbara.png" at posharem04
            imagebutton:
                focus_mask True
                idle "Icons/dismiss04.png"
                hover "Icons/dismiss04.png"
                action Jump ("BarbaraDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance04.png"
                hover "Icons/maintenance04.png"
                action Jump ("BarbaraMaintain")    
        if haremintpos == 5:
            add "v081/harembarbara.png" at posharem05
            imagebutton:
                focus_mask True
                idle "Icons/dismiss05.png"
                hover "Icons/dismiss05.png"
                action Jump ("BarbaraDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance05.png"
                hover "Icons/maintenance05.png"
                action Jump ("BarbaraMaintain")    
        if haremintpos == 6:
            add "v081/harembarbara.png" at posharem06
            imagebutton:
                focus_mask True
                idle "Icons/dismiss06.png"
                hover "Icons/dismiss06.png"
                action Jump ("BarbaraDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance06.png"
                hover "Icons/maintenance06.png"
                action Jump ("BarbaraMaintain")

    if harembe and maintenancebe:
        $ haremintpos += 1
        if haremintpos == 1:
            add "v082/harembella.png" at posharem01        
        if haremintpos == 2:
            add "v082/harembella.png" at posharem02        
        if haremintpos == 3:
            add "v082/harembella.png" at posharem03        
        if haremintpos == 4:
            add "v082/harembella.png" at posharem04        
        if haremintpos == 5:
            add "v082/harembella.png" at posharem05        
        if haremintpos == 6:
            add "v082/harembella.png" at posharem06        

    if harembe and maintenancebe == False:
        $ haremintpos += 1
        if haremintpos == 1:
            add "v082/harembella.png" at posharem01
            imagebutton:
                focus_mask True
                idle "Icons/dismiss01.png"
                hover "Icons/dismiss01.png"
                action Jump ("BellaDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance01.png"
                hover "Icons/maintenance01.png"
                action Jump ("BellaMaintain")    
        if haremintpos == 2:
            add "v082/harembella.png" at posharem02
            imagebutton:
                focus_mask True
                idle "Icons/dismiss02.png"
                hover "Icons/dismiss02.png"
                action Jump ("BellaDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance02.png"
                hover "Icons/maintenance02.png"
                action Jump ("BellaMaintain")    
        if haremintpos == 3:
            add "v082/harembella.png" at posharem03
            imagebutton:
                focus_mask True
                idle "Icons/dismiss03.png"
                hover "Icons/dismiss03.png"
                action Jump ("BellaDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance03.png"
                hover "Icons/maintenance03.png"
                action Jump ("BellaMaintain")    
        if haremintpos == 4:
            add "v082/harembella.png" at posharem04
            imagebutton:
                focus_mask True
                idle "Icons/dismiss04.png"
                hover "Icons/dismiss04.png"
                action Jump ("BellaDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance04.png"
                hover "Icons/maintenance04.png"
                action Jump ("BellaMaintain")    
        if haremintpos == 5:
            add "v082/harembella.png" at posharem05
            imagebutton:
                focus_mask True
                idle "Icons/dismiss05.png"
                hover "Icons/dismiss05.png"
                action Jump ("BellaDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance05.png"
                hover "Icons/maintenance05.png"
                action Jump ("BellaMaintain")    
        if haremintpos == 6:
            add "v082/harembella.png" at posharem06
            imagebutton:
                focus_mask True
                idle "Icons/dismiss06.png"
                hover "Icons/dismiss06.png"
                action Jump ("BellaDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance06.png"
                hover "Icons/maintenance06.png"
                action Jump ("BellaMaintain")

    if haremde and maintenancede:
        $ haremintpos += 1
        if haremintpos == 1:
            add "v09/haremdebra.png" at posharem01        
        if haremintpos == 2:
            add "v09/haremdebra.png" at posharem02        
        if haremintpos == 3:
            add "v09/haremdebra.png" at posharem03        
        if haremintpos == 4:
            add "v09/haremdebra.png" at posharem04        
        if haremintpos == 5:
            add "v09/haremdebra.png" at posharem05        
        if haremintpos == 6:
            add "v09/haremdebra.png" at posharem06        

    if haremde and maintenancede == False:
        $ haremintpos += 1
        if haremintpos == 1:
            add "v09/haremdebra.png" at posharem01
            imagebutton:
                focus_mask True
                idle "Icons/dismiss01.png"
                hover "Icons/dismiss01.png"
                action Jump ("DebraDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance01.png"
                hover "Icons/maintenance01.png"
                action Jump ("DebraMaintain")    
        if haremintpos == 2:
            add "v09/haremdebra.png" at posharem02
            imagebutton:
                focus_mask True
                idle "Icons/dismiss02.png"
                hover "Icons/dismiss02.png"
                action Jump ("DebraDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance02.png"
                hover "Icons/maintenance02.png"
                action Jump ("DebraMaintain")    
        if haremintpos == 3:
            add "v09/haremdebra.png" at posharem03
            imagebutton:
                focus_mask True
                idle "Icons/dismiss03.png"
                hover "Icons/dismiss03.png"
                action Jump ("DebraDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance03.png"
                hover "Icons/maintenance03.png"
                action Jump ("DebraMaintain")    
        if haremintpos == 4:
            add "v09/haremdebra.png" at posharem04
            imagebutton:
                focus_mask True
                idle "Icons/dismiss04.png"
                hover "Icons/dismiss04.png"
                action Jump ("DebraDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance04.png"
                hover "Icons/maintenance04.png"
                action Jump ("DebraMaintain")    
        if haremintpos == 5:
            add "v09/haremdebra.png" at posharem05
            imagebutton:
                focus_mask True
                idle "Icons/dismiss05.png"
                hover "Icons/dismiss05.png"
                action Jump ("DebraDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance05.png"
                hover "Icons/maintenance05.png"
                action Jump ("DebraMaintain")    
        if haremintpos == 6:
            add "v09/haremdebra.png" at posharem06
            imagebutton:
                focus_mask True
                idle "Icons/dismiss06.png"
                hover "Icons/dismiss06.png"
                action Jump ("DebraDismiss")    
            imagebutton:
                focus_mask True
                idle "Icons/maintenance06.png"
                hover "Icons/maintenance06.png"
                action Jump ("DebraMaintain")
return

label ZaraDismiss:
if haremza:
    scene bedroom01
    show zara01 at centerleft with moveinleft
    mc "I'm afraid I'm going to have to let you go Zara."
    za "Since you own me, I will be available to rejoin your harem at your discretion Master... After a one week delay."
    mc "Well that's good to know."
    hide zara01 with moveoutleft
$ haremza = False
$ zaradismissed = True
$ girlsinharem -= 1
$ pregzaready = 0
jump HaremMaintenance

label ZaraMaintain:
if money <= 0:
    "It appears you don't have enough money to maintain Zara. You need to dismiss her instead."
    jump ZaraDismiss
if money <= 4:
    $ money = 0
if money >= 5:
    $ money -= 5
$ maintenanceza = True
scene bedroom01
show zara02 at centerleft with moveinleft
if haremzararejoined == False:
    za "Thank you Master, I am honored to remain in your harem."
    $ pregzaready += 1
if haremzararejoined:
    za "Thank you Master for taking me back into your harem, I am honored."
    $ haremzararejoined = False
window hide
hide zara02  with dissolve
jump HaremMaintenance

label AngieDismiss:
scene bedroom01
show angieasking at center with moveinleft
mc "I'm afraid I'm going to have to let you go Angie."
hide angieasking
show angiesad at center
with fastdissolve
an "What have I done? I feel like I've been abandoned once again...."
mc "Life is tough. I'm sorry it had to be this way."
window hide
call LustMinusAngie
hide angiesad with moveoutleft
$ angiedismissed = True
$ girlsinharem -= 1
$ hareman = False
$ preganready = 0
jump HaremMaintenance
                            
label AngieMaintain:
if money <= 0:
    "It appears you don't have enough money to maintain Angie. You need to dismiss her instead."
    jump AngieDismiss
if money <= 4:
    $ money = 0
if money >= 5:
    $ money -= 5
$ maintenancean = True
$ preganready += 1
scene bedroom01
show angiehappy01 at centerleft with moveinleft
an "Yippee, I'll still be PROTECTED from the bad guys for another week!"
window hide
hide angiehappy01 with dissolve
jump HaremMaintenance

label NancyDismiss:
scene bedroom01
show nancybedroom02 at centerleft with moveinleft
mc "I'm afraid I can't keep you in my harem Nancy."
hide nancybedroom02
show nancybedroom01 at centerleft
with fastdissolve
mo "But why [name]? We were starting to be a real household again..."
mc "Yeah, but a filthy household. That's apparently frowned upon in this fucked-up new world. The good old times of landlady-tenant game relationships are gone, I'm sorry..."
window hide
call LustMinusNancy
hide nancybedroom01 with moveoutleft
$ momdismissed = True
$ girlsinharem -= 1
$ haremmo = False
$ pregmoready = 0
jump HaremMaintenance

label NancyMaintain:
if money <= 0:
    "It appears you don't have enough money to maintain Nancy. You need to dismiss her instead."
    jump NancyDismiss
scene bedroom01
if money <= 4:
    $ money = 0
if money >= 5:
    $ money -= 5
$ maintenancemo = True
show nancybedroom02 at centerleft with moveinleft
mo "I'm so happy you've decided to keep me in your harem."
mc "How could I do otherwise? I can't get enough of your hot bod!"
hide nancybedroom02
show nancybedroom03 at centerleft
mo "I hope I'll see you OFTEN this week at nights [name]... * wink*"
$ pregmoready += 1
window hide
hide nancybedroom03 with dissolve
jump HaremMaintenance

label MichikoDismiss:
scene bedroom01
show michiko01 at centerleft with moveinleft
mc "I'm afraid I'm going to have to let you go Michiko. The economy is tanking, times are tough, and so on."
hide michiko01
show michiko03 at centerleft
with fastdissolve
mi "Even when you're dismissing me, you're BRUTAL. But not sexually this time..."
window hide
call LustMinusMichiko
hide michiko03 with moveoutleft
$ girlsinharem -= 1
$ haremmi = False
$ michikodismissed = True
$ pregmiready = 0
jump HaremMaintenance

label MichikoMaintain:
if money <= 0:
    "It appears you don't have enough money to maintain Michiko. You need to dismiss her instead."
    jump MichikoDismiss
scene bedroom01
if money <= 4:
    $ money = 0
if money >= 5:
    $ money -= 5
$ maintenancemi = True
show michiko02 at centerleft with moveinleft
mi "I'm glad you're keeping me. So we can have more BRUTAL fuck sessions."
$ pregmiready += 1
window hide
hide michiko02 with dissolve
jump HaremMaintenance

label CyrlMaintain:
if money <= 0:
    "It appears you don't have enough money to maintain Cyrl. You need to dismiss her instead."
    jump CyrlDismiss
scene bedroom01
if money <= 4:
    $ money = 0
if money >= 5:
    $ money -= 5
$ maintenancecy = True
show cyrl03 at centerleft with moveinleft
cy "I'm glad you're keeping me human friend. I enjoy our little BDSM sessions together. As well as the free booze you provide me with."
window hide
hide cyrl03 with dissolve
jump HaremMaintenance

label CyrlDismiss:
scene bedroom01
show cyrl02 at centerleft with moveinleft
mc "I'm gonna have to let you go Cyrl. I don't even know why I have to pay a maintenance fee for you. I mean, you don't even eat."
hide cyrl02
show cyrl04 at centerleft
with fastdissolve
cy "Correct. But I drink. A lot. I'm a taraholic."
mc "Yeah, well, I ain't paying for your addiction anymore."
cy "Umpf. I should have known. You are untrustworthy. Like all humans."
window hide
call LustMinusCyrl
hide cyrl04 with moveoutleft
$ haremcy = False
$ girlsinharem -= 1
$ cyrldismissed = True
jump HaremMaintenance

label RubyMaintain:
if money <= 0:
    "It appears you don't have enough money to maintain Ruby. You need to dismiss her instead."
    jump RubyDismiss
scene bedroom01    
if money <= 4:
    $ money = 0
if money >= 5:
    $ money -= 5
$ maintenanceru = True
show ruby04 at centerleft with moveinleft
ru "Can't get enough of my big guns, hey? I'll gladly stay and show you how a REAL WOMAN fucks."
window hide
hide ruby04 with dissolve
jump HaremMaintenance

label RubyDismiss:
scene bedroom01
show ruby06 at centerleft with moveinleft
mc "Don't take it too badly but... I'm going to have to let you go Ruby."
hide ruby06
show ruby07 at centerleft
with fastdissolve
ru "You can't dismiss a ROAD WARRIOR! You'll PAY for that!"
mc "Actually, by dismissing you, I WON'T HAVE TO PAY your maintenance. That's the beauty of it."
ru "I see. You're just a cheapstake. Don't bother trying to get me back into your harem for a while."
window hide
call LustMinusRuby
hide ruby07 with moveoutleft
$ haremru = False
$ girlsinharem -= 1
$ rubydismissed = True
jump HaremMaintenance

label AmyMaintain:
if money <= 0:
    "It appears you don't have enough money to maintain Amy. You need to dismiss her instead."
    jump AmyDismiss
scene bedroom01    
if money <= 4:
    $ money = 0
if money >= 5:
    $ money -= 5
$ maintenanceam = True
show amy02 at centerleft with moveinleft
am "Thank you for keeping me as... err... a sextoy for your harem."
mc "You're welcome."
$ pregamready += 1
window hide
hide amy02 with dissolve
jump HaremMaintenance

label AmyDismiss:
scene bedroom01
show amy01 at centerleft with moveinleft
mc "I have to cull my harem down a bit. I'm afraid I'm going to have to let you go Amy."
hide amy01
show amy05 at centerleft
with fastdissolve
am "You are disturbing Nature's balance by dismissing me like that!"
mc "Or maybe I'm RESTORING her balance, who knows?"
hide amy05
show amy06 at centerleft
am "Humpf... That is so lame."
window hide
call LustMinusAmy
hide amy06 with moveoutleft
$ haremam = False
$ girlsinharem -= 1
$ amydismissed = True
$ pregamready = 0
jump HaremMaintenance

label AylaMaintain:
if money <= 0:
    "It appears you don't have enough money to maintain Ayla. You need to dismiss her instead."
    jump AylaDismiss
scene bedroom01    
if money <= 4:
    $ money = 0
if money >= 5:
    $ money -= 5
$ maintenanceay = True
$ pregayready += 1
show ayla02 at centerleft with moveinleft
ay "You're keeping me? I won't be BORED for another week, so thanks."
mc "You're welcome."
window hide
hide ayla02 with dissolve
jump HaremMaintenance

label AylaDismiss:
scene bedroom01
show ayla01 at centerleft with moveinleft
mc "My harem suffers from overcrowding. I blame the Church and not my abysmal management skills."
hide ayla01
show ayla05 at centerleft
with fastdissolve
ay "The Phallus Lord will punish you!"
mc "Bring him on. Until then, You are dismissed, Ayla."
hide ayla05
show ayla03 at centerleft
ay "Whatever... I was bored in your harem anyway."
window hide
call LustMinusAyla
hide ayla03 with moveoutleft
$ haremay = False
$ girlsinharem -= 1
$ ayladismissed = True
$ pregayready = 0
jump HaremMaintenance

label SukiMaintain:
if money <= 0:
    "It appears you don't have enough money to maintain Suki. You need to dismiss her instead."
    jump SukiDismiss
scene bedroom01    
if money <= 4:
    $ money = 0
if money >= 5:
    $ money -= 5
$ maintenancesu = True
show suki02 at centerleft with moveinleft
su "I managed to ace your harem test? I'm so happy!"
mc "You got an A+ actually. So you get on to the next round. Of HEAVY FUCKING."
window hide
hide suki02 with dissolve
jump HaremMaintenance

label SukiDismiss:
scene bedroom01
show suki02 at centerleft with moveinleft
mc "I suck at Microsoft Excel and a clerical error means you can no longer remain in my harem. Sorry, Suki."
hide suki02
show suki03 at centerleft
with fastdissolve
su "You're a noob at Excel AND you're a noob at HAREM MASTERING, clearly! You should take some online course."
mc "At least I didn't pay some guy to take my SATs for me like Trumpf."
window hide
call LustMinusSuki
hide suki03 with moveoutleft
$ haremsu = False
$ girlsinharem -= 1
$ sukidismissed = True
jump HaremMaintenance

label GwenMaintain:
if money <= 0:
    "It appears you don't have enough money to maintain Gwen. You need to dismiss her instead."
    jump GwenDismiss
scene bedroom01    
if money <= 4:
    $ money = 0
if money >= 5:
    $ money -= 5
$ maintenancegw = True
show gwen04 at centerleft with moveinleft
gw "Another week in your harem without being raped? I'm IN!"
mc "Obviously, as my harem slave, I can't legally rape you. It's necessarily consensual."
gw "Don't complicate things, [name]."
$ preggwready += 1
hide gwen04 with dissolve
jump HaremMaintenance

label GwenDismiss:
scene bedroom01
show gwen03 at centerleft with moveinleft
mc "I'd love to keep you but the money is tight."
hide gwen03
show gwen05 at centerleft
with fastdissolve
gw "The only tight thing here is YOU. President-for-Life Trumpf gave everyone a fat check the other day, that will be added to our abysmal national debt. Did you blow it all off already?"
mc "Well, I didn't get jack. He doesn't care about me obviously. So you must leave my harem."
window hide
call LustMinusGwen
hide gwen05 with moveoutleft
$ haremgw = False
$ girlsinharem -= 1
$ gwendismissed = True
$ preggwready = 0
jump HaremMaintenance

label PennyMaintain:
if money <= 0:
    "It appears you don't have enough money to maintain Penny. You need to dismiss her instead."
    jump PennyDismiss
scene bedroom01    
if money <= 4:
    $ money = 0
if money >= 5:
    $ money -= 5
$ maintenancepe = True
show pennyfriendly01 at centerleft with moveinleft
pe "Being your harem fuck partner on top of your scout partner for another week? I'm IN!"
mc "We'll be exploring the human body together. IN DEPTH."
hide pennyfriendly01
show pennyfriendly02 at centerleft
with fastdissolve
pe "I see what you did there. * Wink* "
window hide
hide pennyfriendly02 with dissolve
jump HaremMaintenance

label PennyDismiss:
scene bedroom01
show penny03 at centerleft with moveinleft
mc "I need to dismiss you. For lack of funds."
hide penny03
show pennyserious at centerleft
with fastdissolve
pe "A REAL road warrior can always fend for himself. Or herself in my case. I'm FREE AGAIN at last!"
mc "Well, until I find some more money and call your back here, that is..."
window hide
call LustMinusPenny
hide pennyserious with moveoutleft
$ harempe = False
$ girlsinharem -= 1
$ pennydismissed = True
jump HaremMaintenance

label MarnieMaintain:
if money <= 0:
    "It appears you don't have enough money to maintain Marnie. You need to dismiss her instead."
    jump MarnieDismiss
scene bedroom01    
if money <= 4:
    $ money = 0
if money >= 5:
    $ money -= 5
$ maintenancema = True
show marnie02 at centerleft with moveinleft
ma "I knew you just couldn't stay away from our hot steamy FEMDOM sessions! *wink*"
mc "Well, err... Please just don't tell the others. MISTRESS."
hide marnie02
show marnie04 at centerleft
with fastdissolve
ma "Your perversion is SAFE with me. Remember, I NEVER give out secrets."
window hide
hide marnie04 with dissolve
jump HaremMaintenance

label MarnieDismiss:
scene bedroom01
show marnie02 at centerleft with moveinleft
mc "I think you're more useful behind the bar than in my harem."
hide marnie02
show marnie06 at centerleft
with fastdissolve
ma "What is that supposed to mean?"
mc "That I am dismissing so you can go back behind the bar where you belong."
window hide
call LustMinusMarnie
hide marnie06 with moveoutleft
$ haremma = False
$ girlsinharem -= 1
$ marniedismissed = True
jump HaremMaintenance

label ClaraMaintain:
if money <= 0:
    "It appears you don't have enough money to maintain Clara. You need to dismiss her instead."
    jump ClaraDismiss
scene bedroom01    
if money <= 4:
    $ money = 0
if money >= 5:
    $ money -= 5
$ maintenancecl = True
show clara03 at centerleft with moveinleft
cl "The Phallus Lord has blessed me with another week of sexual slavery in your harem!"
mc "Yeah, isn't he a great guy or what?"
window hide
hide clara03
with fastdissolve
jump HaremMaintenance

label ClaraDismiss:
scene bedroom01
show clara03 at centerleft with moveinleft
mc "The Church has called you back. Temporarily of course, but you can't stay in my harem."
hide clara03
show clara04 at centerleft
with fastdissolve
cl "Oh... Well, I must serve the Church first and foremost so... I guess I'll leave."
mc "That's a good girl. Be ready to be CALLED BACK into my harem though."
window hide
call LustMinusClara
hide clara04 with moveoutleft
$ haremcl = False
$ girlsinharem -= 1
$ claradismissed = True
jump HaremMaintenance

label LaurieMaintain:
if money <= 0:
    "It appears you don't have enough money to maintain Laurie. You need to dismiss her instead."
    jump LaurieDismiss
scene bedroom01    
if money <= 4:
    $ money = 0
if money >= 5:
    $ money -= 5
$ maintenancela = True
$ preglaready += 1
show laurie02 at centerleft with moveinleft
la "I can stay? And you'll still eat your vegetables?"
mc "Your SPECIAL vegetables, yes."
window hide
hide laurie02
with fastdissolve
jump HaremMaintenance

label LaurieDismiss:
scene bedroom01
show laurie03 at centerleft with moveinleft
mc "I know you crave my meat but so do I. I mean, crave meat. So your vegetables don't cut it anymore, I'm gonna have to let you go."
hide laurie03
show laurie04 at centerleft
with fastdissolve
la "You'll come to regret this. Too much meat will affect blood flow. To your cock..."
mc "I'll worry about that when I'm like, 80 or something."
window hide
call LustMinusLaurie
hide laurie04 with moveoutleft
$ haremla = False
$ girlsinharem -= 1
$ preglaready = 0
$ lauriedismissed = True
jump HaremMaintenance

label LenaMaintain:
if money <= 0:
    "It appears you don't have enough money to maintain Lena. You need to dismiss her instead."
    jump LenaDismiss
scene bedroom01    
if money <= 4:
    $ money = 0
if money >= 5:
    $ money -= 5
$ maintenancele = True
show lena07 at centerleft with moveinleft
le "I had no doubt you would do the right thing and KEEP ME IN YOUR HAREM."
mc "I still don't get why I have to pay for that though. I mean, you're the Chief and you could just plunder the treasury for your own benefit."
le "I'm not Steve Mnuchin, that's why."
window hide
hide lena07
with fastdissolve
jump HaremMaintenance

label LenaDismiss:
scene bedroom01
show lena01 at centerleft with moveinleft
le "Did you want to tell me something?"
mc "Yeah, I did. YOU'RE DISMISSED!"
hide lena01
show lena03 at centerleft
with fastdissolve
le "Is that a joke?"
mc "No, but I do find it funny though. DISMISSED!"
window hide
call LustMinusLena
hide lena03 with moveoutleft
$ haremle = False
$ girlsinharem -= 1
$ lenadismissed = True
jump HaremMaintenance

label BarbaraMaintain:
if money <= 0:
    "It appears you don't have enough money to maintain Barbara. You need to dismiss her instead."
    jump BarbaraDismiss
scene bedroom01    
if money <= 4:
    $ money = 0
if money >= 5:
    $ money -= 5
$ maintenanceba = True
$ pregbaready += 1
show barbara08 at centerleft with moveinleft
ba "You did your PATRIOTIC duty and kept ME in your harem. Another great day in New Great America. See you in class [name]!"
window hide
hide barbara08
with fastdissolve
jump HaremMaintenance

label BarbaraDismiss:
scene bedroom01
show barbara08 at centerleft with moveinleft
ba "Are you ready for another glorious day in New Great America [name]?"
mc "Sure I am. I'll make it even greater by dismissing you from my harem and saving money. You know, for the good of the economy and the country."
hide barbara08
show barbara07 at centerleft
with fastdissolve
ba "I definitely need to start teaching some basic economics because you clearly do NOT understand anything about it!"
mc "I understand that I'm saving five bucks and that's good enough for me."
window hide
call LustMinusBarbara
hide barbara07 with moveoutleft
$ haremba = False
$ girlsinharem -= 1
$ barbaradismissed = True
$ pregbaready = 0
jump HaremMaintenance

label BellaMaintain:
if money <= 0:
    "It appears you don't have enough money to maintain Bella. You need to dismiss her instead."
    jump BellaDismiss
scene bedroom01    
if money <= 4:
    $ money = 0
if money >= 5:
    $ money -= 5
$ maintenancebe = True
show bella01 at centerleft with moveinleft
be "Fine, I'll stay in your harem as long as that filthy whore is out of it!"
mc "Who do you mean exactly?"
be "I think you know..."
window hide
hide bella01
with fastdissolve
jump HaremMaintenance

label BellaDismiss:
scene bedroom01
show bella08 at centerleft with moveinleft
mc "I've explored your body inside out. That area is now cleared so you have to leave my harem."
hide bella08
show bean at centerleft
with fastdissolve
be "How dare you! The Phallus Lord shall punish you for this!"
mc "I very much doubt s..."
window hide
call MinusChurch
hide bean
show bella06 at centerleft
with fastdissolve
be "There. I warned you."
window hide
call LustMinusBella
hide bella06 with moveoutleft
$ harembe = False
$ girlsinharem -= 1
$ belladismissed = True
jump HaremMaintenance

label DebraMaintain:
if money <= 0:
    "It appears you don't have enough money to maintain Debra. You need to dismiss her instead."
    jump DebraDismiss
scene bedroom01    
if money <= 4:
    $ money = 0
if money >= 5:
    $ money -= 5
$ maintenancede = True
show debrahappy01 at centerleft with moveinleft
de "I expected nothing less from my lab underling. You might even get promoted one day."
mc "You mean above Gwen?"
hide debrahappy01
show debratalking01
with fastdissolve
de "Let's not push it... Bye [name]!"
window hide
hide debratalking01
with fastdissolve
jump HaremMaintenance

label DebraDismiss:
scene bedroom01
show debrabored at centerleft with moveinleft
de "What do you want? I was BUSY working in my lab, you do realize that?"
mc "In that case I have great news for you. You'll be able to work there even MORE. I'm kicking you out of my harem."
hide debrabored
show debraoffended at centerleft
with fastdissolve
de "Fine! I don't need sex. I'm a SCIENTIST. I can... stick a state-of-the-art dildo up my twat."
call LustMinusDebra
mc "Sure, you do that Professor. In between experiments."
hide debraoffended with moveoutleft
$ haremde = False
$ girlsinharem -= 1
$ debradismissed = True
jump HaremMaintenance

label HaremPreBella:
scene bedroom01
show bella01 at centerleft with moveinleft
mc "I got rid of that, err.., sinful bitch. You can now join my harem Bella!"
be "Great! I'll show you some much BETTER times than she ever could, I promise!"
hide bella01 with moveoutleft
$ girlsinharem += 1
$ bellaharem = True
$ harembe = True
if money <= 4:
    $ money = 0
if money >= 5:
    $ money -= 5
$ maintenancebe = True
$ bellajustjoined = True
return

