label School:
$ loc = "school"
if angiereunited == False:
    scene class01 with dissolve
if angiereunited:
    scene class01
    show classnoangie
    with dissolve
play music "Sounds/classroom.mp3"
if weekschool == 1:
    mc "I arrived just before the start of the class. Maybe I can chat up a girl before the teacher arrives..."
if weekschool >= 2:
    mc "I 'm just on time, I won't have time to chat up with anyone before Barbara arrives..."
    jump StartSchool

label School01:
if angiereunited == False:
    call screen class01
    screen class01:
        modal True    
        imagebutton:
            focus_mask True
            idle "School/schoolviewidle.png"
            hover "School/schoolviewhover.png"
            action Jump ("ViewClass")
        if schoolmust == False:
            imagebutton:
                focus_mask True
                idle "Icons/exitidle.png"
                hover "Icons/exithover.png"
                action Jump ("Main01")
        imagebutton:
            focus_mask True
            idle "School/classaylaidle.png"
            hover "School/classaylahover.png"
            action Jump ("AylaClass")    
        imagebutton:
            focus_mask True
            idle "School/classamyidle.png"
            hover "School/classamyhover.png"
            action Jump ("AmyClass")    
        imagebutton:
            focus_mask True
            idle "School/classangieidle.png"
            hover "School/classangiehover.png"
            action Jump ("AngieClass")    
        imagebutton:
            focus_mask True
            idle "School/classsukiidle.png"
            hover "School/classsukihover.png"
            action Jump ("SukiClass")    

if angiereunited:
    call screen class01b
    screen class01b:
        modal True    
        if schoolmust == False:
            imagebutton:
                focus_mask True
                idle "Icons/exitidle.png"
                hover "Icons/exithover.png"
                action Jump ("Main01")
        imagebutton:
            focus_mask True
            idle "School/classaylaidle.png"
            hover "School/classaylahover.png"
            action Jump ("AylaClass")    
        imagebutton:
            focus_mask True
            idle "School/classamyidle.png"
            hover "School/classamyhover.png"
            action Jump ("AmyClass")    
        imagebutton:
            focus_mask True
            idle "School/classsukiidle.png"
            hover "School/classsukihover.png"
            action Jump ("SukiClass")    

label ViewClass:
show classaylaidle
show classamyidle
show classangieidle
show classsukiidle
mc "A nice view of the outside world. Badlands everywhere."
jump School01

label AylaClass:
scene class03 with dissolve
call AylaDialogue01
jump StartSchool  
    
label AmyClass:    
scene class03 with dissolve
call AmyDialogue01
jump StartSchool

label SukiClass:
scene class03 with dissolve
call SukiDialogue01
jump StartSchool
    
label AngieClass:
if pregan and preganstart >= 3:
    scene class03
    show angiepregnant02a
    with dissolve
    an "Hi [name], I'm so glad you came to school today, now my baby won't be all alone with me, YIPPEE!"
    mc "If I could, I would help you carry it of course, but you know, biological differences and so on..."
    hide angiepregnant02a
    show angiepregnant02b
    with dissolve
    an "The teacher is arriving, let's learn something so the baby becomes smart like you!"
    mc "Err, yeah, sure..."
    jump StartSchool
scene class03 with dissolve
call AngieDialogue01
jump StartSchool  

label StartSchool:
$ seenschool = True
$ weekschool += 1
$ school += 1
if angiereunited and barbaralustangie == False:
    stop music
    scene class02
    show barbara01
    with dissolve    
    ba "Before we start, I have an announcement to make!"
    hide barbara01
    show barbara08
    with fastdissolve 
    ba "Angie will not be joining us anymore because thanks to our President-for-Life Trumpf, WHO KEEPS HIS PROMISES, she has been re-united with her family!"
    mc "Err... I might have had some role to play in that teach..."
    hide barbara08
    show barbara03
    with fastdissolve 
    ba "You're right, I did hear you were patriotic enough to do President Trumpf bidding in order for this ALL-AMERICAN outcome to occur. Let's give YOU a round of applause, [name]..."
    call LustPlusBarbara
    ba "And to celebrate this... You all have the day off!"
    play sound "Sounds/applause.mp3"
    $ renpy.pause(0.5, hard='True')
    hide barbara03
    show barbara02
    with fastdissolve     
    ba "What was that?"
    mc "People applauding I guess... See you, teach!"
    hide barbara02 with dissolve
    $ period += 1
    $ barbaralustangie = True
    jump Main01
    
if school == 1:
    jump Class01
if school == 2:
    jump Class02
if school == 3:
    jump Class03
if school == 4:
    jump Class04
if school == 5:
    jump Class05
if school == 6:
    jump Class06
if school == 7:
    jump Class07
if school == 8:
    jump Class08
if school == 9:
    jump Class09
if school == 10:
    jump Class10
if school >= 11:
    jump Class11

label Class01:
scene class02 with dissolve
play music "Sounds/classroom.mp3"
mc "(I wonder what class is going to be taught today?)"
stop music
show barbara01 with dissolve
stop music
ba "Welcome everyone, I see that [name] joined us today, so make him feel welcome since he's not attending our classes regularly. Which is a SHAME. Another inept decision by Chief Lena!"
hide barbara01
show barbara02
ba "According to my manual, today's class will be sex ed for the New Great America."
ba "As you may be aware, men are a rarity these days. Well, for example, [name] is the only boy in this class..."
hide barbara02
show barbara03
ba "Therefore, it is important that you understand how our glorious President-for-Life Trumpf has decided to repopulate our great new nation."
ba "First, abortions are evil and no longer allowed in our great new nation. All women must be obedient and make as many white babies as they can to re-populate the New United States of America!"
su "Oh, that's just perfect, I'm saved from this Republican medieval outlook then! For once, your racism serves me well!"
hide barbara03
show barbara07
ba "This is not racist. This is patriotic. You Deep State foreign-looking troublemakers can't fathom the subtle difference."
su "Pff!"
ba "Who's the teacher here? Now please use your desk screens to follow the instructional videos for this course. That will give me a break from rebellious students..."
mc "(That should be interesting...)"
scene classbarbara01 with dissolve
mc "(Actually, it's all pretty boring... Even Barbara looks bored... Well, at least, I did my duty and went to school.)"
play sound "Sounds/schoolbell.mp3"
scene class02 with dissolve
show barbara01
ba "Ok, class dismissed! Have a wonderful day in New Great America kids!"
hide barbara01
$ period += 1
jump Main01

label Class02:
stop music
scene class02 with dissolve
show barbara01
mc "(I wonder what class is going to be taught today?)"
ba "Settle down now... Today, we'll continue following the online course provided by our Department of New Education on... sexual education."
ba "Last time, we learnt why women must make as many babies as possible. Today, we'll learn HOW to achieve this patriotic goal."
hide barbara01
show barbara02
ba "Turn on your desk screen and watch... It might get quite graphic but you are all mature enough to deal with such videos."
su "This is disgusting, but at least a welcome change from internet videos of Trumpf tweeting on the bog!"
an "Ms Lebigue-Coq! My screen doesn't seem to work..."
am "Neither does mine. I think there's a bug..."
ay "God I'm so BORED!"
hide barbara02
show barbara05
ba "Calm down, our REAL government has a solution to every issue. I will consult my teacher's manual and we'll know what to do..."
hide barbara05
show barbara04
ba "Oh no! My DeVos manual says that in the event of a technical failure of the online course SE02, the teacher shall demonstrate the course live with the most sexually mature male student in the class..."
mc "That would be me-ee!"
hide barbara04
show barbara05 at left
show suki05 at right
ba "Suki, you're an Asian nerd, I mean... a gifted Asian-American student. Surely, you could fix this for us in no time?"
su "Well, I don't know Ms Lebigue-Coq... It could take a while..."
menu:
    "You're a genius Suki, I'm sure you can do it! (+1 lust Suki)":
        hide suki05
        show suki02 at right
        su "You think so [name]? That makes me so proud that you appreciate my brains rather than my... hideously-changed body..."
        mc "Well, I wouldn't go that far as to call you hideous..."
        call LustPlusSuki
        hide barbara05
        show barbara08 at left
        hide suki02
        show suki06 at right
        su "OK... I'll do it...."
        scene class02 with dissolve
        show barbara08 at left
        show suki05 at right
        su "Done Ms Lebigue-Coq. The screens should work now."
        ba "Thank you so much Suki, you saved me from a... sticky situation."
        mc "With my cum-cannon, it certainly would have been a VERY sticky situation!"
        hide suki05
        hide barbara08
        show barbara07 at left
        ba "Don't try and be funny [name]...."
        play sound "Sounds/schoolbell.mp3"
        hide barbara07
        show barbara01 at left        
        ba "Ok, class dimissed! Have a wonderful day in New Great America kids!"
        $ period +=1
        hide barbara01
        jump Main01        
    "Let's not waste time, I need to LEARN stuff here, that's what Chief Lena said! (+1 Deep State or Trumpsters)":
        hide barbara05
        show barbara07 at left
        hide suki05
        show suki07 at right
        ba "Hang on a minute, I should have my say in this!"
        mc "No you don't, your precious manual is very clear. You've got to demonstrate the course live with ME!"
        hide barbara07
        show barbara05 at left        
        ba "(sigh) You're right, I have no choice. I'm starting to regret downloading the DeVos method of New Teaching."
        if mctrumpster <=2:
            mc "You should regret having voted for Trumpf in the first place! Too late now!"
            window hide
            show plusdeep at posmission
            $ renpy.pause(2.0, hard=True)
            hide plusdeep
            $ mcdeep += 1
            hide suki07
            show suki04 at right            
            su "Ha, Ha, I have to agree with [name] there! We told you so!"
            hide barbara05
            show barbara07 at left                    
            ba "I see. Another Deep State conspiracy. Fine, I'll show you traitors how this doesn't phase a true patriot like me! Come forward [name], I'll do what my De Vos manual says!"
            mc "Right-ee-o Ms Lebigue-Coq!"
            jump School02b
        if mctrumpster >=3:
            mc "We must do as our President-for-Life intended in his infinite wisdom."
            call PlusTrumpster
            hide suki07
            show suki03 at right
            su "Pff! You guys are pathetic! I won't fix this wonky Republican software, it's probably imported from Russia anyway!"
            hide barbara05
            show barbara06 at left                    
            ba "Ah, the Deep State sees conspiracies everywhere! Fine, I'll show you Suki how true patriots deal with unforeseen hiccups! Come forward [name], I'll do what my De Vos manual says!"
            mc "Right-ee-o Ms Lebigue-Coq!"
            jump School02b
        
        
label School02b:
scene class02 with dissolve
show barbara09 at centerright
ba "Are you ready [name]?"
mc "Hell, I AM ready Barbara!"
hide barbara09
show barbara10 at centerright
ba "Take your pants off and come forward. I'll take my bra off and let you admire my backside to get you excited..."
scene class04 with dissolve
show barbarapre01
ba "And now, take my panties off."
mc "Let me do that my own way. With my COCK!"
hide barbarapre01
show barbarapre02
mc "Can you feel how strong my fucking cock is teach?"
ba "Oh my God! You are hung like a true American Boy from the Supreme Race!"
su "Spare us your racist bullshit and get on with it!"
play sound "Sounds/ripping.mp3"
ba "You TORE my panties off naughty boy!"
hide barbarapre02
show barbarapre03
ba "Now bring that mighty stallion-sized whopper over and get me horny. A boy has to get his woman hot and ready first..."
call LustPlusBarbara
scene barbara16
mc "My pleasure teach... First, I'm gonna coat that pussy of yours with pre-cum to make the penetration easier."
scene barbara17
ba "That's a great idea. I can feel it nudged between my asscheeks... It's so hard and HUGE! Put it in me [name]!"
scene barbara18
ba "Oh God, give me some time to adjust... (puff)"
mc "Sure teach..."
ba "Now, I'm ready to demonstrate how a woman gets fertilized... by a boy's monstercock."
ba "With a cock that size, you'll have no problem reaching all the way to my ovaries [name]!"
ay "Finally, something that's not as BORING as usual!"
play music "Sounds/barbarasex.mp3"
scene barbarasexbackground
show nextidle
call screen barbarasex
screen barbarasex:
    add barbarasex at center
    modal True
    button:
        xpos .91
        ypos .44
        xysize(140, 80)        
        action Jump ("BarbaraSexEnd")    


label BarbaraSexEnd:
stop music
scene barbarasexend01
ba "Are you watching girls? He's filling me up with ounces of boycream. That's how you get pregnant."
ay "A lot of it seems to be shooting OUT of your poontang... What a waste...."
mc "That's only because my shots are so powerful and her pussy is so tight."
ba "Stop bragging and when you're done dumping that massive load inside me, get off me so I can demonstrate the next step."
mc "Sure, I have another few shots left teach though... AAHH!"
scene barbarasexend02 with dissolve
mc "There you go..."
scene barbarasexend03 with dissolve
ba "Now gather round girls, this is the position you should adopt to maximize your chances of getting pregnant."
ay "How is that helping?"
ba "The cum will flow directly to my ovaries."
an "Aren't you scared of getting pregnant Ms Lebigue-Coq?"
ba "Err... I should be fine Angie, don't worry."
play sound "Sounds/schoolbell.mp3"
ba "Ok, class dimissed! Have a wonderful day in New Great America kids!"
scene class02
$ period += 1
jump Main01

    
label Class03:
stop music
scene class02 with dissolve
show barbara01
mc "(I wonder what class is going to be taught today?)"
ba "I have been made aware that a new online course is to be dispensed to all young American schoolchildren as soon as possible."
mc "(I hope it involves some kind of sexual activities like the last course...)"
hide barbara01
show barbara02 with fastdissolve
ba "You are all to learn... French. Intensively."
su "Why is that so? Chinese is the most widely spoken language in the world, we should learn that!"
hide barbara02
show barbara03 with fastdissolve
ba "Actually, China has been completely wiped off the face of the Earth. Nobody speaks that weirdo foreign language anymore."
ba "Since France was miraculously spared by the nuclear fallout, French is now the most widely spoken language in the world. So French it is."
an "Isn't your name French actually Ms Lebigue-Coq?"
hide barbara03
show barbara08 with fastdissolve
ba "Exactly Angie. My proud slave-owning ancestors came from France to build up this great nation through cotton plantations in Louisiana. So I can speak French and I will teach you."
hide barbara08
show barbara01 with fastdissolve
ba "The DeVos Foundation has also provided an online course for you to follow. For the girls, François will be your online guide. For you [name], it will be Francine."
mc "(That sounds totally boring...)"
hide barbara01
show barbara02 with fastdissolve
ba "So log onto your online desk screens and follow the first introductory course."
label Francine01:
hide screen calendar
hide screen mcstats
scene interface02 with dissolve
play sound "Sounds/interfacestart.mp3"
pause 1.0
scene interface01 with dissolve
show francine01
fr "Bonjour! Je m'appelle Francine!"
fr "Comment t'appelles-tu?"
menu: 
    "[name]":
        fr "Bonjour [name]!"
        hide francine01
    "What's it to you froggy?":
        hide francine01
        show francine03 with fastdissolve
        fr "Ooh la la! Tu es un naughty garçon!"
        hide francine03
show francine04 with fastdissolve
fr "Voulez-vous admirer mes big melons?"
menu:
    "Oui!":
        hide francine04
        show francine03 with fastdissolve        
        fr "Ooh la la! Tu es un très naughty garçon!"
        mc "Yep, that's me!"
    "Non!":
        hide francine04
        show francine02 with fastdissolve
        fr "Ooh la la! Mais tu es gai?"
        mc "Err... non."
hide francine02
hide francine03
show francine01 with fastdissolve
fr "Et maintenant..."
hide francine01
show francinelingerie01 with fastdissolve
fr "La lingerie. Ooh la la!"
mc "What the fuck is this online course?"
hide francinelingerie01
show francinelingerie02 with fastdissolve
fr "Et maintenant..."
hide francinelingerie02
show francinecorset01 with fastdissolve
fr "Le corset. Très sexy, n'est-ce pas?"
hide francinecorset01
show francinecorset02 with fastdissolve
fr "Et maintenant..."
hide francinecorset02
show francinestring01 with fastdissolve
fr "Où est le string?"
hide francinestring01
show francinestring02 with fastdissolve
fr "Le string est sur ma pussy chatte. Ooh la la!"
mc "I wonder what the hell the girls are seeing in their online course..."
hide francinestring02
show francinestring03 with fastdissolve
fr "Voulez-vous un bébé?"
fr "Moi, je veux un bébé..."
hide francinestring03
show francineend01 with fastdissolve
fr "Look! J'ai un bébé maintenant! Bravo [name]!"
mc "I think it's meant to encourage me to fuck girls and make babies but I'm not sure..."
hide francineend01
show francineend02 with fastdissolve
fr "Au revoir [name]. A bientôt!"
mc "Err... yeah, bye Francine..."
show screen calendar
show screen mcstats
scene class02 with dissolve
play sound "Sounds/schoolbell.mp3"
show barbara01
ba "Ok, class dismissed! Have a wonderful day in New Great America kids!"
hide barbara01
$ period += 1
jump Main01

label Class04:
stop music
scene class02 with dissolve
show barbara02
ba "Today we will continue where we left off. This online course has some...err... additional material for you."
hide barbara02
show barbara01 with fastdissolve
ba "So please log onto your online desk screens and follow the course."
label Francine02:
hide screen calendar
hide screen mcstats
scene interface02 with dissolve
play sound "Sounds/interfacestart.mp3"
pause 1.0
scene interface01 with dissolve
show francine01
fr "Bonjour [name]!"
mc "Yeah, hi Francine."
fr "Et maintenant..."
show francine01 at midright with move
show francois01b at midleft with moveinleft
hide francine01
show francine05 at midright with fastdissolve
fr "...mon ami François!"
mc "Nooooo, not THAT boy from Battle of the Bulges again! This is cross-game NTRing, I protest, there is no tag for that!"
hide francine05
show francine01 at midright with fastdissolve
fr "Et maintenant..."
hide francois01b
show francois02b at midleft with fastdissolve
hide francine01
show francine06 at midright with fastdissolve
fr "Le grand cock! ooh la la!"
mc "Yeah, yeah, we know he has a big whopper, get on with it..."
hide francois02b
hide francine06
show francine07 with fastdissolve
fr "Où est le grand cock?"
mc "Oh, let me guess. In your fucking pussy chatte?"
hide francine07
show francine08 with fastdissolve
fr "Bravo [name]. Oui, le grand cock est dans ma pussy chatte!"
hide francine08
show francine101
fr "Oooh, François! C'est si bon!"
hide francine101
show francinesex01
jump FrancineSex01
label FrancineSex01pre:
fr "Moins vite!"
label FrancineSex01:
hide francinesex02
show francinesex01
call screen francinesex01
screen francinesex01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("FrancineSexEnd")    
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("FrancineSex02")    

label FrancineSex02:
fr "Plus vite!"
hide francinesex01
show francinesex02
call screen francinesex02
screen francinesex02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("FrancineSexEnd")    
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("FrancineSex01pre")    

label FrancineSexEnd:
mc "Well, at least I've learnt a few French words I guess..."
fr "Et maintenant...."
hide francinesex01
hide francinesex02
show francine12 with fastdissolve
fr "La fontaine de sperme dans ma pussy chatte. Ooh la la!"
fr "Et maintenant..."
hide francine12
show francineend01 with fastdissolve
fr "J'ai un bébé! Merci François!"
mc "I should have guessed she would get virtually pregnant again..."
hide francineend01
show francineend02 with fastdissolve
fr "Au revoir [name]. A bientôt!"
hide francineend02
mc "I would really like to have a word with Betsy DeVos about her academic credentials..."
show screen calendar
show screen mcstats
scene class02 with dissolve
play sound "Sounds/schoolbell.mp3"
show barbara01
ba "Ok, class dismissed! Have a wonderful day in New Great America kids!"
hide barbara01
$ period += 1
jump Main01

label Class05:
scene class02 with dissolve
play music "Sounds/classroom.mp3"
mc "(I wonder what class is going to be taught today?)"
scene class02 with dissolve
show barbara01
stop music
ba "Welcome everyone. I have some excting news for you! You will learn how to create an online avatar of yourselves so you can interact with your online French tutor!"
am "What, you mean François, the horse-hu... I mean, the French kid?"
hide barbara01
show barbara08 with fastdissolve
ba "That's right, I'm sure you girls are all very eager to meet him in the \"virtual flesh\"."
mc "(And I get to meet Francine I assume...)"
ba "So get to work, the online course will guide you..."
hide screen calendar
hide screen mcstats
scene interface02 with dissolve
play sound "Sounds/interfacestart.mp3"
pause 1.0
scene interface01 with dissolve
"Please place your face in front of the camera."
play sound "Sounds/flash.mp3"
"How muscular are you?"
mc "VERY muscular, the STRONGEST boy on the planet as a matter of fact!"
"Very good, New America needs fertile young males."
show mchard00
"Here is your avatar. We have reconstructed the size of your genitalia in accordance with your musculature."
mc "(Well, that's a pretty damn close resemblance I must admit...)"
"Please confirm that it is the actual size of your penis."
mc "(Maybe I can lie here, I mean it's just virtual fun, right?)"
mc "Nope, I am much bigger than that!"
"Sorry, we did not mean to offend you Mr SUPERSTUD."
window hide
hide mchard00
show mcharder
$ renpy.pause(1.0, hard=True)
"Here is an updated version of your online avatar. Are you satisfied?"
mc "Yep, that's more like it. (Now Francine is going to be mighty impressed when she sees it, it's even bigger than that French douchebag.)"
show screen calendar
show screen mcstats
scene class02 with dissolve
play sound "Sounds/schoolbell.mp3"
show barbara01
ba "OK, class dismissed! Have a wonderful day in New Great America kids!"
hide barbara01
$ period += 1
jump Main01

label Class06:
scene class02 with dissolve
play music "Sounds/classroom.mp3"
mc "(I wonder what class is going to be taught today?)"
scene class02 with dissolve
show barbara01
stop music
ba "Since you all managed to create your avatar last time, today, you can finally get to meet your virtual tutor...err... virtually."
hide barbara01
show barbara03 with fastdissolve
ba "So go online, and try and learn some French that will be useful in your future careers as \"Mothers for New America\"..."
ba "Or in YOUR case [name], \"Studs for New America\"."
su "I refuse to be a walking womb, even for that good-looking virtual kid!"
hide barbara03
show barbara07 with fastdissolve
ba "You're starting to make me think you are nothing but a commie lefty troublemaker Suki! Shut up and follow the course or I'll have you reported to the Department of Re-Education!"
ba "And I can assure you you don't want THAT! Eric Trumpf is in charge of that department..."
su "Umpf..."
hide screen calendar
hide screen mcstats
scene interface02 with dissolve
play sound "Sounds/interfacestart.mp3"
pause 1.0
show francineblue01 at midright with dissolve
fr "Bonjour [name]! Joins-moi dans la réalité virtuelle!"
show mcbigger01 at midleft with moveinleft
mc "Ah, there I am, all in glorious high-resolution pixels. With a MASSIVE cock."
hide francineblue01
show francineblue02 at midright
fr "Ton cock est super-grand! Ooh la la!"
mc "Better to fuck you with it."
hide francineblue02
show francineblue03 at midright
fr "Veux-tu un bébé avec moi [name]?"
mc "Oui!"
fr "Ooh la la!"
hide francineblue03
show francineblue04 at midright
fr "Je veux ton super-grand cock dans mon bosom!"
label MCFrancine01:
hide mcbigger01
hide francineblue04
show mcfrancinesex01
call screen mcfrancinesex01
screen mcfrancinesex01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("McFrancine01End")

label McFrancine01End:
fr "Oui, c'est bon! Ooh la la! J'aime ton super-grand cock [name]!"
fr "Je veux ton ENORME cock dans ma pussy chatte!"
hide mcfrancinesex01
show mcfrancinesex02
call screen mcfrancinesex02
screen mcfrancinesex02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("McFrancine02End")
label McFrancine02End:        
fr "Ton cock est TRES TRES GRAND! Ooh la la!"
fr "Je veux que tu éjacules dans ma pussy chatte!"
mc "I can ejaculate, oui!"
hide mcfrancinesex02
show mcfrancinesexcum01
mc "FUCK! AAAH! I'm filling you up like a Renault truck!"
fr "OUI! Ejacule BEAUCOUP de hot sperme!"
hide mcfrancinesexcum01
show mcfrancinesexcum02 with fastdissolve
mc "Fuck, I'm virtually cumming a LOT!"
fr "Ooh la la, beaucoup de sperme dans ma pussy chatte ET sur moi! Merci [name]!"
play sound "Sounds/schoolbell.mp3"
scene class02 with dissolve
show barbara01
ba "Ok, class dismissed! Have a wonderful day in New Great America kids!"
hide barbara01
$ period += 1
jump Main01

label Class07:
scene class02 with dissolve
play music "Sounds/classroom.mp3"
mc "(I wonder what class is going to be taught today?)"
scene class02 with dissolve
show barbara01
stop music
ba "Today we will continue where we left off. You still have so much to learn from your avatar encounter from last time..."
hide barbara01
show barbara03 with fastdissolve
ba "So go online, and try and learn some French that will be useful in your future careers as \"Mothers for New America\"..."
an "Ms Lebigue-Coq, I didn't learn any French last time. This François kid did... err... I don't know how to say it...."
su "He virtually RAPED you, admit it Angie! This course is DISGUSTING, and so typical of the DeVos Department of \"Education\"!"
hide barbara03
show barbara02 with fastdissolve
ba "Well, err... I'm sure you must have said something wrong to him Angie. Just don't make him angry and you'll be fine, alright?"
an "I'll try Ms Lebigue-Coq..."
hide screen calendar
hide screen mcstats
scene interface02 with dissolve
play sound "Sounds/interfacestart.mp3"
pause 1.0
show francineblue01 at midright with dissolve
fr "Bonjour [name]! Joins-moi dans la réalité virtuelle!"
show mcbigger01 at midleft with moveinleft
mc "Ah, there I am again, all in glorious high-resolution pixels. With a MASSIVE cock. More sexy French fun for me today!"
scene class02 with fade
mc "What happened?"


show suki04 at midright
su "That's right, I hacked into the server and SABOTAGED this VILE course before we all got raped once again by DeVos' weirdo pedo-fantasy!"
show barbara07 at midleft
ba "This is OUTRAGEOUS! You are depriving your classmates of a valuable education opportunity!"
hide suki04
show suki03 at midright
su "You have no choice now but to teach us French the NORMAL way! Long live the Deep State!"
hide barbara07
show barbara05 at midleft
ba "I KNEW IT! This is all an underhanded attempt by our enemies to undermine our glorious President-for-Life's authority!"
menu:
    "Side with Barbara (+1 Trumpsters, - 1 lust Suki)":
        mc "Our Department of Education knows what's best for us and you just ruined everything Suki!"
        call PlusTrumpster
        hide suki03
        show suki01 at midright
        su "What? How can you say that? I thought you were on OUR side..."
        call LustMinusSuki
        jump Class07Next
    "Side with Suki (+1 Deep State, -1 lust Barbara)":
        mc "I have always questioned the DeVos method. It doesn't fit with the teachers union's demands."
        hide suki03
        show suki02 at midright
        call PlusDeep
        hide barbara05
        show barbara02 at midleft        
        ba "What? How can you say that? I see... You are on the commie unionized lefties side!"        
        call LustMinusBarbara
        
        jump Class07Next        
    "Don't take sides (no change)":
        jump Class07Next
label Class07Next:
hide barbara05
hide barbara02
hide suki02
hide suki01
show barbara07 at midleft
ba "So, thanks to Suki, it will be French CONJUGATION for everyone today!"
scene classbarbara01 with fade
ba "Je suis. Tu es. Il-elle est. Nous..."
play sound "Sounds/schoolbell.mp3"
scene class02 with dissolve
show barbara01
ba "Ok, class dismissed! Have a wonderful day in New Great America kids! Except you Suki."
su "Pfff..."
hide barbara01
$ period += 1
jump Main01


label Class08:
scene class02 with dissolve
play music "Sounds/classroom.mp3"
mc "(I wonder what class is going to be taught today?)"
scene class02 with dissolve
show barbara07
stop music
ba "Welcome everyone. Since Suki SABOTAGED your online course, I have to resort to more drastic measures to get you to understand what Betsy DeVos wants from you!"
hide barbara07
show barbara03 with fastdissolve
ba "So you will each come forward and practice your French on [name], who will serve as a stud surrogate you have to seduce. I have brought some lingerie for you. First up, Angie!"
an "What? But... Ms Lebigue-Coq!"
su "We are being treated as second-class citizens!"
hide barbara03
show barbara07 with fastdissolve
ba "Absolutely NOT! Your are first-class citizens in New America! The males are the ones that are second-class citizens, only here to impregnate women, and I don't here [name] complaining!"
mc "That's right. I'm not complaining. I don't mind being a second-class citizen Ms Lebigue-Coq!"
hide barbara07
show barbara02 with fastdissolve
ba "See? Now come forward Angie and put on this small-size ensemble I brought for you."
hide barbara02 with fade
show angieschool01b at midright with moveinright
an "Like that Ms Lebigue-Coq?"
ba "Yes, wonderful Angie. Now, [name] will come wearing something sexy too for you."
hide angieschool01b
show angieschool02b at midright
an "Re... Really?"
if posingpouch:
    show mcpouch00 at midleft with moveinleft
    ba "I'd say so, he's wearing a sexy pouch."
ba "So now say something in French to him Angie."
hide angieschool02b
show angieschool03b at midright
an "Err... Bonjour [name]! Comment vas-tu?"
mc "Err... Bonjour Angie. Good, thanks."
ba "Now come on [name], that was NOT French!"
mc "Yes it was, I said \"Bonjour\"!"
ba "I don't think we'll get anywhere today with these two dolts. Go back to your seats, we will learn French conjugation, that'll teach you all!"
hide angieschool03b
show angieschool01b at midright
an "It wasn't my fault Ms Lebigue-Coq! I tried my best..."
ba "Yes I know Angie, it's [name] who clearly learnt NOTHING from his avatar encounter."
mc "Oh, I learnt a LOT. I assure you."
ba "Umpf, I don't even want to know what this means."
scene classbarbara01 with dissolve
ba "Je suis. Tu es. Il-elle est. Nous..."
play sound "Sounds/schoolbell.mp3"
scene class02 with dissolve
show barbara01
ba "Ok, class dismissed! Have a wonderful day in New Great America kids!"
hide barbara01
$ period += 1
jump Main01


label Class09:
scene class02 with dissolve
play music "Sounds/classroom.mp3"
scene class02 with dissolve
show barbara01
stop music
ba "Next up today for our French conversational class is Amy!"
am "It better not be made from synthetic material that is destroying the planet!"
hide barbara01
show barbara02 with fastdissolve
ba "Well, for your information, I brought over a wool lingerie set for you. See, I can take care of my students' needs like a good, qualified, DeVos-approved schoolteacher."
hide barbara02
show barbara03 with fastdissolve
ba "So come over Amy and put it on for [name]. Remember, you have to SEDUCE him. In French."
su "But why? It doesn't even make any sense since [name] sucks at French!"
mc "Excusez-moi? Ooh la la! Non non non!"
su "As I said..."
hide barbara03
show barbara07 with fastdissolve
ba "There is a very simple reason Suki. You are likely to encounter French boys who outnumber all other males in the world at the moment."
ba "You will have to seduce them and make them NEW AMERICANS for the glory of our Nation!"
su "Well, I've never met one! Except that François dude. Virtually."
ba "Enough of your rebellious attitude. It's in the educational program, therefore it's what you need. Are you done Amy?"
window hide
hide barbara07 with fade
show amyschool01b at midright with moveinright
am "Yes, I am ready. I must admit I don't mind wearing this, it's quite cosy."
ba "And how do you say cosy in French?"
am "Not a clue."
show mcpouch00 at danceleft with moveinleft
mc "Here I am! Ready to get seduced! And I HAVE brushed up my French this time."
ba "Good. So we can hope you won't make a complete fool of yourself like last time. You start the conversation Amy."
hide amyschool01b
show amyschool03b at midright with fastdissolve
am "Bonjour [name]. Est-ce-que tu aimes my set de lingerie?"
hide amyschool03b
show amyschool02b at midright with fastdissolve
am "Et mon bottom musculaire?"
mc "Err... Pussy chatte? Oooh la la!"
ba "What the hell is that supposed to mean [name]?"
mc "That I'm ready to impregnate her and make Franco-New American babies?"
ba "This is complete nonsense!"
su "Yeah, this whole course is a load of nonsense!"
ba "Shut up Suki! And now go back to your seats, this part of the course is definitely OVER!"
hide amyschool02b
show amyschool01b at midright with fastdissolve
am "I had nothing to do with this disaster... Can I keep the wool sweater by any chance?"
ba "NO! Give it back to me and go and sit down and shut up. All of you, SHUT UP!"
mc "(Damn, she's losing it, we must have really pissed her off...)"
scene classbarbara01 with fade
ba "Je suis. Tu es. Il-elle est. Nous..."
play sound "Sounds/schoolbell.mp3"
scene class02 with dissolve
show barbara02
ba "Ok, class dismissed! I can finally take a break from you lot!"
hide barbara01
$ period += 1
jump Main01

label Class10:
scene class02 with dissolve
play music "Sounds/classroom.mp3"
scene class02 with dissolve
show barbara01
stop music
ba "I am going to give ONE more shot to seduction conversational French today. So you'd better not screw things up this time [name]!"
hide barbara01
show barbara02 with fastdissolve
ba "Ayla, it's your turn."
ay "I don't care about French, it's BORING!"
hide barbara02
show barbara08 with fastdissolve
ba "I see. Well, I'm giving up. French CONJUGATION for the rest of the month for all of you!"
scene classbarbara01 with fade
ba "Je suis. Tu es. Il-elle est. Nous..."
play sound "Sounds/schoolbell.mp3"
scene class02 with dissolve
show barbara01
ba "Ok, class dismissed! Have a wonderful day in New Great America kids!"
hide barbara01
$ period += 1
jump Main01

label Class11:
scene class02 with dissolve
play music "Sounds/classroom.mp3"
scene class02 with dissolve
show barbara07
stop music
ba "French conjugation for everyone again today! And pay attention this time."
scene classbarbara01 with dissolve
ba "J'ai. Tu as. Il-elle a. Nous..."
mc "God, that's boring. I'm going to day-dream of hot girls instead..."
label SchoolDreamMenu:
menu:
    "Daydream of Barbara":
        jump DreamBarbara
    "Daydream of Amy":
        jump DreamAmy
    "Daydream of Ayla":
        jump DreamAyla
    "Daydream of Angie":
        jump DreamAngie
    "Daydream of Suki":
        jump DreamSuki
    "Na, I'd rather conjugate French verbs.":
        $ mcfrenchlevel += 1
        if mcfrenchlevel == 3:
            call PlusFrench
            $ mcfrenchlevel = 0        
        jump Class11End
        
label DreamBarbara:
play sound "Sounds/dream.mp3"
scene classdream with fade
show dreambarbara01
play music "Sounds/showerstrip.mp3"
ba "The fourth of July is approaching. Are you also looking forward to this PATRIOTIC day [name]?"
mc "I didn't even know we were in summer..."
hide dreambarbara01
show dreambarbara02
with fastdissolve
ba "Oh look, some beautiful fireworks in the glorious sky of New America!"
mc "I'm watching. Maybe not high up enough, but I'm looking..."
hide dreambarbara02
show dreambarbara03
with fastdissolve
ba "I must admit, thinking about our GREAT nation is making me horny..."
mc "I'm a patriot too! I'm horny too!"
ba "The only thing that's missing is a MILITARY PARADE of our fierce tanks..."
mc "I can arrange that..."
hide dreambarbara03
show dreambarbara04
with fastdissolve
mc "I'm equipped for the occasion. Here's the cannon of a Sherman Tank. Fully loaded."
ba "Oh my! That looks like AT LEAST a 16-inch gauge cannon, am I right?"   
mc "You're not far off. You know your military stuff teach."
hide dreambarbara04
show dreambarbara05
with fastdissolve
ba "Now I'm gonna have to check for myself what kind of ammo this cannon fires..."   
mc "Be my guest. But be warned it's a multi-shots cannon."
scene classdream02
show dreambarbara06 
with dissolve
ba "I'll try and muffle those salvoes then. With my ARSE. Shoot it in there, soldier!"
scene classdream02 blurred
show dreambarbara07
with fastdissolve
ba "Let me spread my ass cheeks... This cannon is so BIG, I know it's going to do a LOT of DAMAGE!"
mc "Here it comes, Barbara!"
hide dreambarbara07
show dreambarbara08
with fastdissolve
ba "Oh, dear lord, no wonder our military is the GREATEST in the world!"
mc "Push back on it, I'm charging the cannon..."
window hide
hide dreambarbara08
show dreambarbara09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreambarbara09
show dreambarbara08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreambarbara08
show dreambarbara09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreambarbara09
show dreambarbara08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreambarbara08
show dreambarbara09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreambarbara09
show dreambarbara08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreambarbara08
show dreambarbara09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreambarbara09
show dreambarbara08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreambarbara08
show dreambarbara09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreambarbara09
show dreambarbara08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreambarbara08
show dreambarbara09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreambarbara09
show dreambarbara08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreambarbara08
show dreambarbara09
with fastdissolve
$ renpy.pause(0.2, hard=True)
ba "FIRE, soldier, NOW!"
hide dreambarbara09
show dreambarbara10
with fastdissolve
mc "I'm shooting! RHAAA!"
ba "I can feel your shots, fire away soldier! And don't forget to douse the enemy's backline! I'm cumming too, AAAHHH!"
hide dreambarbara10
show dreambarbara11
with fastdissolve
mc "There you go, I'm drowning the backline in my creamy salvoes, FUCK YEAH!"
ba "Oooh, yes!"
hide dreambarbara11
show dreambarbara12
with fastdissolve
ba "You did well [name], you sure could join the tank division of our Glorious Leader's Army!"
mc "Yeah, I'll think about it... But right now.... PHEW!"
jump Class11End

label DreamAmy:
play sound "Sounds/dream.mp3"
scene classdream with fade
show dreamamy01
play music "Sounds/showerstrip.mp3"
am "Do you like what I'm wearing [name]?"
hide dreamamy01
show dreamamy02
with fastdissolve
am "It's so comfortable. I LOVE natural cotton and how it hugs my ass curves, right?"
mc "Oooh yeah!"
hide dreamamy02
show dreamamy03
with fastdissolve
am "Of course, it's even better when I'm half naked... Letting the warm breeze flow over my hardening nipples..."
mc "The breeze is good. The breeze is good."
hide dreamamy03
show dreamamy04
with fastdissolve
am "And when it flows between my thighs and tickles my clit... I get so HORNY!"
mc "Praise the Breeze!"
hide dreamamy04
show dreamamy05
with fastdissolve
am "And I bet you're horny and hard already, right? I've got just the thing to make you even harder and BIGGER!"
am "So pull those pants down and show me your fuckpole, I'm going to PUMP IT UP!"
mc "Praise the Pump!"
hide dreamamy05
show dreamamy06
with fastdissolve
am "There, I think it fits perfectly over your megadong. It's the XXXXL version of course..."
am "Now let's PUMP!"
hide dreamamy06
show dreamamy07
with fastdissolve
am "Look at it! It's already getting FATTER! I'm going to pump it until you FILL IT UP!"
hide dreamamy07
show dreamamy08
with fastdissolve
am "Almost there... It's becoming monstrously HUGE! I want your fat shaft to reach the TIP!"
mc "Damn, it feels GOOOOOD!"
hide dreamamy08
show dreamamy09
with fastdissolve
am "I think you're ALL PUMPED UP now! Look at that BEHEMOTH of a cock! It makes my mouth salivate."
mc "Maybe it's time to pull the pump off Amy? Cos I feel like I'm about to cum..."
am "You're right, let's see that DONKEY-DICK up close so it can unload a MONSTER LOAD all over me!"
hide dreamamy09
show dreamamy10
with fastdissolve
am "My God, it's sooo HUGE!... And leaking TONS of precum! Come for me [name], let it all OUT!"
mc "Yes, Amy, I'm about to..."
hide dreamamy10
show dreamamy11
with fastdissolve
mc "...UNLEASH! RHAAA!"
am "YES! BLAST THAT VIRILE CREAM! COVER ME FROM HEAD TO TOE IN YOUR WARM SPUNK!"
hide dreamamy11
show dreamamy12
with fastdissolve
mc "Phew... I'm done. Plastering your body."
am "And plaster it you did! I cannot thank you enough for providing me with this vital natural energy, [name]!"
mc "You're welcome."
jump Class11End
    
label DreamAyla:
play sound "Sounds/dream.mp3"
scene classdream with fade
show dreamayla01
play music "Sounds/showerstrip.mp3"
ay "God I'm just so BORED."
mc "Maybe we could play a game to keep ourselves entertained?"
ay "What game?"
mc "Err... How about strip poker. But without cards. Goes quicker."
hide dreamayla01
show dreamayla02
with fastdissolve
ay "Alright, but only because I'm so BORED. So how do we play it?"
mc "First, you need to turn round..."
hide dreamayla02
show dreamayla03
with fastdissolve
ay "That doesn't sound like fun AT ALL. But I'll do it anyway. God, SSSOOO BORED!"
mc "It's fun for me at least... Now pull your top off and let your nipples say hi to me."
ay "Why? This game is so STUPID. But I guess I have nothing BETTER to do right now."
hide dreamayla03
show dreamayla04
with fastdissolve
ay "There. Are you happy you sick PERVERT?"
mc "Quite so, quite so."
ay "So, what next, FREAK?"
mc "Pull your panties down too."
hide dreamayla04
show dreamayla05
with fastdissolve
ay "This game had better become more interesting SOON. I'm already getting BORED!"
mc "It will, don't worry, it will."
hide dreamayla05
show dreamayla06
with fastdissolve
ay "I'm waiting... All naked and WAITING for this stupid game to get BETTER."
mc "Alright, let's kick it up a notch then."
hide dreamayla06
show dreamayla07
with fastdissolve
mc "There. Is the game getting more interesting now?"
ay "I guess so. This thing is WAY bigger than my boyfriend's for sure..."
mc "And it can deliver way more cream than him too!"
ay "I don't believe you. I need to check myself."
mc "Be my guest..."
hide dreamayla07
show dreamayla08
with fastdissolve
ay "Alright, let's see... How to make sure you're not lying..."
mc "Maybe tug it hard and fast?"
ay "Yes, I like that new game better than the old one..."
window hide
hide dreamayla08
show dreamayla09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla09
show dreamayla08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla08
show dreamayla09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla09
show dreamayla08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla08
show dreamayla09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla09
show dreamayla08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla08
show dreamayla09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla09
show dreamayla08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla08
show dreamayla09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla09
show dreamayla08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla08
show dreamayla09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla09
show dreamayla08
with fastdissolve
$ renpy.pause(0.2, hard=True)
mc "I'm about to blow my load Ayla!"
ay "Go ahead, I don't care if you get some on me. I bet it won't be too much trouble cleaning it anyway."
hide dreamayla08
show dreamayla10
with fastdissolve
ay "What the FUCK? You're BLASTING all the way up to the ceiling!?!?"
ay "That is definitely already WAY MORE than my boyfriend."
hide dreamayla10
show dreamayla11
with fastdissolve
ay "You ARSEHOLE! Look at what you've done! I'm covered in your filthy SEED!"
mc "You wanted to know if I came more than your boyfriend. Now you know."
hide dreamayla11
show dreamayla12
with fastdissolve
ay "Alright. I forgive you. THIS ONCE. But only because your cum is DELICIOUS."
mc "I was hoping you'd notice."
jump Class11End

label DreamAngie:
play sound "Sounds/dream.mp3"
scene classdream with fade
show dreamangie01
play music "Sounds/showerstrip.mp3"
an "Did someone call SUPERGIRL?"
mc "Yeah, I did. What are your superpowers exactly?"
hide dreamangie01
show dreamangie02
with fastdissolve
an "I can grow my tits and my pussy to fight off the LARGEST dangers that civilization is confronted with!"
mc "I see. Then let me put your superpowers to the test..."
hide dreamangie02
show dreamangie03
with fastdissolve
an "Really? Oh, I sure hope it's a BIG challenge!"
mc "Yep, it will be, it will be... You'd better start using your superpowers now actually."
hide dreamangie03
show dreamangie04
with fastdissolve
an "Alright, supergirl powers are GO!"
mc "Go, go, go! Fuck YEAH. You need to get even BIGGER Angie! The danger you will encounter is MASSIVE!"
hide dreamangie04
show dreamangie05
with fastdissolve
an "Supergirl is now READY to face off her mighty enemy!"
mc "Just look down, it's about to appear..."
hide dreamangie05
show dreamangie06
with fastdissolve
an "Oh my God, what is this fiendish foe?"
mc "It's the \"One-Eyed-Monster\". You need to tame it before it wreaks havoc on the world!"
an "But... How?"
mc "Maybe take your top off and try and smother it with your SUPERTITS."
an "Ooh, yes, that's a good idea!"
hide dreamangie06
show dreamangie07
with fastdissolve
an "The \"One-Eyed-Monster\" is now at the mercy of Supergirl's powerful bosom!"
mc "You need to make it spew its vital essence to vanquish it."
an "I WILL. This is my DUTY as a SUPERHERO!"
hide dreamangie07
show dreamangie08
with fastdissolve
an "Oh no, the Monster is getting HARDER and BIGGER!"
mc "Y... Yes... AAH!"
an "What should I do?"
mc "Just... Keep.... UUUHH... rubbing it!"
window hide
hide dreamangie08
show dreamangie07
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamangie07
show dreamangie08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamangie08
show dreamangie07
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamangie07
show dreamangie08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamangie08
show dreamangie07
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamangie07
show dreamangie08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamangie08
show dreamangie07
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamangie07
show dreamangie08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamangie08
show dreamangie07
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamangie07
show dreamangie08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamangie08
show dreamangie07
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamangie07
show dreamangie08
with fastdissolve
$ renpy.pause(0.2, hard=True)
an "I can feel it... Tremble with TERROR!"
mc "Sure... *puff* It's about to be defeated.... AAAHH!"
hide dreamangie08
show dreamangie09
with fastdissolve
an "I WIN! Yippee!"
mc "RHAAA! I concede! Err... I mean... The \"One-Eyed-Monster\" gives up! AAAH!"
hide dreamangie09
show dreamangie10
with fastdissolve
an "Look at all his vital essence blasting out! He will have NONE left!"
mc "FUCK, OOOH, AAAH! Yeah... AAAH! Well done Angie..."
hide dreamangie10
show dreamangie11
with fastdissolve
an "And now it's all floppy and useless. The world has once again been saved by SUPERGIRL!"
mc "Phew...He might come back... One day..."
jump Class11End

label DreamSuki:
play sound "Sounds/dream.mp3"
scene classdream with fade
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
jump Class11End

label Class11End:
stop music
play sound "Sounds/schoolbell.mp3"
scene class02 with dissolve
show barbara01
ba "Ok, class dismissed! Have a wonderful day in New Great America kids!"
hide barbara01
$ period += 1
jump Main01





