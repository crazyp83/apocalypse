label Intro:
stop music
show screen injury

scene apocalypse01 with dissolve
call screen intro01
screen intro01:
    add "intro01.png"
    modal True
    button:
        xpos .385
        ypos .30
        xysize(380, 80)        
        action Jump ("Intro01")
    button:
        xpos .385
        ypos .385
        xysize(380, 80)        
        action Jump ("Intro02")

label Intro01:
scene emergency01 with dissolve
play sound "Sounds/emergency.mp3"
pause 1.0
scene emergency02
pause 0.2
scene emergency01
pause 0.3
scene emergency02
pause 0.5
scene emergency01
pause 0.2
stop sound
scene whitehouse
show seal:
    xpos .3
    ypos .2
play sound "Sounds/whitehouse.mp3"
$ renpy.pause(4.5, hard='True')
stop sound
scene trump01 with dissolve
tr "Do I really have to say that?"
"Mister President, we are live to the nation in 3...2...1..."
scene trump02 with dissolve
tr "Listen folks. I wanted to order a Coke but I pressed the wrong button."
tr "It's not my fault, it's all crooked Hillary's fault, she put the button at the wrong place. \nLOCK HER UP!"
tr "Right now, we are under nuclear attack. But don't worry, we'll make Totally Ruined New America great again, believe me!"
tr "So hide in your basements, I have a big basement, the best basement in the world, so I'll be safe." 
scene trump03 with dissolve
tr "And don't watch CNN, they'll tell you you're dead but it will be FAKE NEWS! \n Don't believe your dead eyes, it's a WITCH HUNT!"
tr "Watch Fox News for the latest update on us beating the bad guys who attacked us because Obama put the nuclear button next to the Coke button."
"Sir, we must evacuate. Your bunker is ready."
scene trump04 with dissolve
tr "I'm not leaving until I get my Coke. And two scoops of ice cream."
scene intro01 with dissolve
"Meanwhile, in Springfield, a boy plays in the park while his mother looks on."
scene intro02 with dissolve
play sound "Sounds/explosion.mp3"
"Suddenly, the sky lights up in a fiery orange blaze..."
window hide
pause 5
stop sound
scene black with fade
"The apocalypse had begun..."
play music "Sounds/intromusic.mp3"
scene intromc01 with fade:
    xpos 0.0
    linear 5.0 xpos -0.5
"After months of radioactive hibernation, a young hero rose from the ashes of Totally Ruined New America. YOU are that hero!"
play sound "Sounds/thunder.mp3"
show intromc02
"Intent on exacting his vengeance upon those responsible for the death of his family and billions of others, the hero felt the power of wrath flow through his veins."
show intromc02
play sound "Sounds/thunder.mp3"
"His massive muscles glistened in the shine of the scorched earth."
play sound "Sounds/thunder.mp3"
hide intromc02
scene intromc02a:
    ypos 0.0
    linear 4.0 ypos -1.0
pause 5.0
play sound "Sounds/thunder.mp3"
scene intromc02f
show intromc02g
play sound "Sounds/thunder.mp3"
"Also, he had a HUGE penis."
stop sound
scene intromc03 with dissolve
"Weakened by his ordeal, he walked and walked amongst the ruins of a once great nation, meeting only silence and destruction."
scene intro07
"As death knocked on the door, he saw a large building in the middle of the desert. Was it real or a trick of his numbed mind?"
scene intro08
"In his state of semi-consciousness, he saw a female form rush towards him."
scene intro09
"Finally, he heard a familiar sound. One he had not heard in years. A human voice. Salvation had arrived."
be "Call the medical team, I found a survivor. And he's a male!"

play music "Sounds/beep.mp3"
scene medbay02 blurred with fade
show tara02 at midright
show rachel01 at midleft
show medbay02b
mc "Where am I?... and... What happened to me?"
ta "You are in Compound Eden. I'm Doctor Tara and this is nurse Rachel."
ta "One of our scouts found you and brought you back here. The world we live in has changed dramatically after the Great Nuclear Fuckup War."
hide tara02
hide medbay02b
show tara03 at midright
show medbay02b
ta "But you survived somehow, you must have been caught in an alpha-radiation pocket. Instead of being exposed to beta-radiations like most people."
mc "Radiations? My body... It seems to have changed..."
hide tara03
hide medbay02b
show tara01 at midright
show medbay02b
ta "Alpha-radiations turned men into alpha-studs and beta-radiations turned them into beta-weaklings and, in most cases, killed them."
ta "It's pretty basic science really..."
ta "Women are immune to beta-radiations. Depending on how much alpha-radiations they received, their sexual organs might have enlarged too."
hide rachel01
hide medbay02b
show rachel03 at midleft
show medbay02b
ra "I think I got a whole LOT of alpha-radiations doc. My tits, they're HUGE now, look at them!"
hide tara01
hide medbay02b
show tara02 at midright
show medbay02b
ta "Yes, thank you for your demonstration Rachel, I'm not sure our young patient was supposed to see your nipples..."
mc "I didn't mind."
ta "I can see that. You obviously were exposed to a lot of alpha-radiations too..."
hide rachel03
hide medbay02b
show rachel05 at midleft
show medbay02b
ra "Wow, it almost makes me want to suck on it."
hide tara02
hide medbay02b
show tara04 at midright
show medbay02b
ta "And you will not do such a vile thing. I remind you that you belong to MY harem, girl!"
ta "Anyway, our patient clearly needs some rest. Give him a shot of ketamine so he can go to sleep." 
mc "Ketamine? Are you out of your fucking m..."
stop music
pause 1

label Intro02:
scene apocalypse02 with dissolve
call screen intro02
screen intro02:
    add "intro02.png"
    modal True
    button:
        xpos .385
        ypos .30
        xysize(380, 80)        
        action Jump ("Intro02a")

    button:
        xpos .385
        ypos .385
        xysize(380, 80)        
        action Jump ("Intro03a")

label Intro02a:
scene medbay02 blurred with fade 
show screen calendar
show jake01b at centerleft
show rachel02b at farleft
show tara01b at farright
show lena01 at centerright
show medbay02b
le "So, is this the new survivor?"
ja "He looks weak."
hide lena01
hide medbay02b
show lena02 at centerright
show medbay02b
le "What are you babbling about? He's got huge muscles everywhere! He clearly was exposed to alpha-radiations, so he could be very handy to us."
hide jake01b
hide medbay02b
hide rachel02b
show jake03b at centerleft
show rachel05b at farleft
show tara01b at farright
show lena02 at centerright
show medbay02b
ja "Hummpf..."
hide lena02
hide medbay02b
show lena06 at centerright
show medbay02b
le "What is your name boy?"
$ name = renpy.input("My name is...")
$ name = name.strip()
mc "I want to see my mum..."
le "Sorry to break it to you [name], but she's most likely dead, like millions of others who died for nothing because of President-for-Life Trumpf's stupidity. We are your family now."
mc "W...What? And who are you?"
le "My name is Lena, I'm in charge of this place, \"Compound Eden\". Come, I'll show you around and introduce you to the other people who live here."
stop music

scene lab01 with fade
show lena01
le "We are self-sufficient in food and clean water, thanks to the technological advances made by our research team."
show debratalking01 at right with moveinright
le "And here is the head of our research facility, Professor Debra Bangor."
de "Is this the new survivor? Nice to meet you. My assistant Gwen and I are working on new technologies to help humanity survive the harsh environment of the post-apocalyptic world."
hide debratalking01
show debratalkingright01 at right
with fastdissolve
de "Here she is, fresh from finishing helping me test some novel explosives."
show gwen07 at left with moveinleft
hide lena01
show lena02
gw "FUCK! It blew up in my face. AGAIN."
de "Stop complaining. The explosive clearly works which means the experiment was a total success."
gw "Why did I accept this fucking job?"
hide debratalkingright01
show debratalking02 at right
with fastdissolve
de "Never mind my assistant, she's always moaning. I need more assistants by the way, if you ever feel like working in the best research facility in the country."
gw "Best? You've got to be shitting me!"
hide lena02
show lena06
with fastdissolve
le "Ok, thanks Debra, we should be moving."

scene bar03 with fade
show barjoeidle
show marniebar02idle
show lena08
le "Here is the common area where people gather after a hard day's work for entertainment and social interactions."
hide lena08
show lena01
with fastdissolve
le "You can also always count on seeing our trader Old Joe, who miraculously survived a massive dose of beta-radiations. Hi Joe!"
scene barjoe04
jo "Good morning to you chief. Who's the newbie?"
le "His name is [name]. One of the few remaining male survivors, just like you."
scene barjoe01
jo "That's great! Hi [name], care to check my junk?"
mc "Your what???"
le "He means the stuff that he sells. Which is indeed all junk. You can buy pretty much anything you want from Old Joe, that is, if you have the money for it."
le "Let's go and meet Marnie at the bar and take a refreshment."
scene bar02 with dissolve
show marnie02
show bar02b
ma "What's up chief? The usual?"
le "Two please. I'm sure [name] will love your \"Greasy Tar Cocktail\"."
hide marnie02
hide bar02b
show marnie03
show bar02b
mc "Err, I'm fine thanks."
le "Marnie is also a fountain of knowledge. She knows everything about everyone."
hide marnie03
hide bar02b
show marnie04
show bar02b
ma "Yep, that's me. People talk too much."
mc "Are there any, like, teens like me that survived?"
le "Oh, yes, we have some. They are probably at school right now but we can go there and introduce you. Come with me."

label Intro01d:
scene class01
show barbara01 at midleft
with dissolve
ba "Oh, Chief Lena, what brings you here today? We weren't expecting such an honor... Please stand up for our chief students."
le "No, no you can sit down everyone. I'm just here to introduce you to [name]. He's about your age. We found him a few days ago."
scene class02
show barbara02 at midleft
show lena07 at midright
with fastdissolve
ba "Will he be joining our class full-time?"
hide lena07
show lena02 at midright
with fastdissolve
le "No, we need him since he's... err... like really strong. He'll be a fighter."
mc "What? But I don't know how to fight!"
le "You'll learn. We have excellent training facilities. I'll take you there. Goodbye class, study hard so you don't end up as dumb as President-for-Life Trumpf."
hide barbara02
show barbara06 at midleft
with fastdissolve
ba "Don't politicize my classroom Chief Lena! I'm sick and tired of you misrepresenting our president. He needs time to make New America great again."
hide lena02
show lena04 at midright
with fastdissolve
le "Yeah? Well maybe he shouldn't have fucked up the old America in the first place! Remember, HE's responsible for the nuclear holocaust!"
hide barbara06
show barbara05 at midleft
with fastdissolve
ba "No he is NOT! It's the others who attacked us! The Mexican rapists and... err... all those shithole countries!"
hide lena04
show lena02 at midright
with fastdissolve
le "Sometimes I wonder why we even allow trumpsters in the compound! Come with me [name], I've had enough of listening to her!"

scene foodunit01
show laurie01 at midright
show lena01 at midleft
with fade
le "Here is our greenhouse where we grow our own food. The desert where we live is particularly arid so we rely on Laurie's salads to keep us fed. Every.fucking.day."
la "You'll grow to love my salads Chief! I take great care in ensuring they have all the right minerals for a healthy diet!"
mc "Ew, I'm sorry, but there's... a funny smell in here.... It's disgusting!"
hide laurie01 at midright
show laurie03 at midright
with fastdissolve
la "Well, I collect rare plants. You're probably smelling the delicate scent of a \"Bostiboobicus Gigantus\", which I took out to water. But I'll put it back in its closet shortly."
le "It is very stinky indeed. Let's leave, I'll show you your private quarters. Which Laurie designed since she is also in charge of improving the compound."

scene bedroom01
show lena08
with fade
le "Here are your private quarters. Since you're a male, we want to pamper you. Most people sleep in bunks here. So count yourself lucky."
hide lena08
show lena06
with fastdissolve
le "I'm also giving you 10 New Dollars as a gift. But you'll have to earn money from now on."
$ money += 10
le "You also have access to our intranet on this computer. And once you start having a harem, you can call girls through the computer interface."
mc  "A harem?"
hide lena06
show lena07
with fastdissolve
le "Well, sure! I mean, a boy like you, in his sexual prime, and especially with a... ahem... thing as big as yours, will inevitably end up leading a harem."
le "There are so many girls and not enough men on this planet right now. We need to repopulate the Earth if humanity is to survive."
hide lena07
show lena06
with fastdissolve
le "Just don't procreate with trumpsters though, we have enough of these deplorables around as it is!"
label LenaIntroChoice:
show lena06
menu:
    "What about you? Are you in a harem?":
        hide lena06
        show lena11
        with fastdissolve
        le "Well... Yes... I mean, no.... Jake and I... We're married. But... The radiations... Well, it's complicated."
        hide lena11
        jump LenaIntroChoice
    "How do I build a harem?":
        hide lena06
        show lena05
        with fastdissolve
        le "Well, you need to convince girls to join it. And then, you need to keep them by providing them with what they need. Both sexual and other needs."
        hide lena05
        jump LenaIntroChoice
    "What's the point of building a harem?":
        hide lena06
        show lena07 
        with fastdissolve
        le "The girls in your harem are at your sexual disposal for starters. But more importantly, they will accompany you and provide valuable expertise that you might need for the successful completions of your missions."
        le "Your harem shouldn't be too big though, or you won't be able to satisfy your girls and they will leave you and look for another harem to join."
        le "However, you can also dismiss a girl from your harem at any time. So you can have different girls at different times depending on your mission needs."
        hide lena07
        jump LenaIntroChoice
    "You seem to dislike Trumpf a lot.":
        hide lena06
        show lena10
        with fastdissolve
        le "Of course, he's a fucking moron! I'm a member of the Deep State. Our group of freedom fighters are trying to overthrow him."
        hide lena10
        jump LenaIntroChoice
    "Can I join the Deep State?":
        hide lena06
        show lena05
        with fastdissolve
        le "Maybe, but we don't accept just any newcomers like that. It's the same with the other tight-knit groups."
        mc  "What other groups are there?"
        hide lena05
        show lena01
        with fastdissolve
        le "Let's see... The Sierra Club, who devote their lives to the protection of the environment, or at least what's left of it."  
        le "There's the Trumpsters of course, who continue to support the president because they are so fucking dumb. You met one already, Barbara the school teacher."
        le "Then there's the Church of the Redeeming Phallus, a new religion that is growing fast and getting bigger and bigger every day with all the new blood pouring in."
        le "And finally the Road Warriors, many of whom live freely in the wild but we also have a few here, like Penny. They recognize each other with their tattoos."
        hide lena01
        jump LenaIntroChoice
    "Who is responsible for the death of my family?":
        hide lena06
        show lena10
        with fastdissolve
        le "President Trumpf! He launched a nuclear attack on South Korea thinking he was bombing North Korea, and then North Korea nuked Russia by mistake, and then all hell broke loose. All his fault."
        hide lena10
        jump LenaIntroChoice
    "Let's start this harem thing. Get undressed, I'm horny.":
        hide lena06
        show lena10 
        with fastdissolve
        le "Who the fuck do you think I am? A cheap whore?"
        call LustMinusLena
        mc  "Well...err.. I was just trying out my luck, sorry if I offended you."
        hide lena10
        jump LenaIntroChoice        
    "Thanks, I have no more questions.":
        le "Then let's go to the workshop now to meet Amy and Ruby."
        jump WorkshopIntro

label WorkshopIntro:
scene workshop01 with fade
show ruby01 at midright
show amy01b at midleft
le "Here is our mechanics workshop. Amy on the left is also in your class but she works part-time here under the supervision of Ruby. They keep our rigs up and running everyday."
ru "G'day. A New recruit, hey? You look pretty tough, you could be a Road Warrior."
hide amy01b
show amy02b at midleft
with fastdissolve
am "...Or a Sierra Club member."
hide ruby01
show ruby03 at midright
with fastdissolve
ru "Yeah, or a sissy boy who loves trees that don't even exist anymore. Your choice."
hide amy02b
show amy03b at midleft
with fastdissolve
am "Despite what Ruby said, the Sierra Club is actually composed of tough, hard-working people who are trying to make the world a BETTER PLACE instead of POLLUTING IT EVEN MORE."
hide ruby03
show ruby03 at midright
with fastdissolve
ru "Oh sorry baby, did I hurt your tree-hugging feelings? Who cares about pollution, the world is totally fucked up anyway."
hide amy03b
show amy04b at midleft
with fastdissolve
le "Keep your squabbles down, what kind of example are you setting for our new scout?"
hide ruby03
hide amy04b
show amy05b at midleft
show ruby06 at midright
with fastdissolve
am "Sorry Chief Lena..."
le "Amy might not look like it but she's very keen on protecting the environment. She's a member of Club Sierra."
hide amy05b
show amy01b at midleft
hide ruby06
show ruby08 at midright
with fastdissolve
le "Ruby is also an expert in firearms. And a member of the NRANRA, the National Rifle Association of New Rebuilt America. She can teach you how to shoot, which would be useful in your future missions."
hide ruby08
show rubyflex at midright
with fastdissolve
ru "Hope you like your guns big and heavy boy, cos Ruby's got what you're looking for!"
mc "Yes, I can see that, thank you."
le "Let's move on to our sports facility. Which I hope you will use a LOT."
scene gym01
show lena01 at midright
with fade
le "Here is our gym. Quite a few people come here to use it but you should be able to find some equipment available at any time to build up your body even more."
show michiko01b at midleft with moveinleft
le "Oh, here comes Michiko. She is an expert in close combat. She can cut 100 sushi rolls in 20 seconds with her little finger."
hide michiko01b
show michiko02b at midleft
with fastdissolve
mi "Konnichiwa! I will teach you how to use every part of your body as a lethal weapon."
hide lena01
show lena06 at midright
with fastdissolve
le "Come here regularly to train so you can become more useful to us."
mi "And don't forget to visit me in the dojo to learn close combat techniques..."
mc "Sorry, but what exactly are you expecting from me?"
le "It's time for you to meet our combat team. Then, I can explain everything to you."

label Intro03:
show screen mcstats
$ period += 1
scene command01
show commandsukiidle
show jake01b at center
show pennyfriendly01 at midright
show beneb at left
with fade
le "Everyone's here, the scout teams haven't left yet. Suki is working as our network and communications expert. She's at the back over there and also a student your age."
le "But first, meet Bella, she's the one who found you a few days..."
hide beneb
show bella01b at left
with fastdissolve
be "Totally naked. You were totally naked. Cock hanging out to the knees and all that."
le "Yes, thank you for your valuable input on the subject matter Bella."
mc "And thank you for saving me."
be "You're welcome stud (wink)."
call LustPlusBella
hide bella01b
show beneb at left
with fastdissolve
le "Jake is the co-founder of our colony. He built the compound with me and we share so much..."
le "So he's in charge of the combat team's strategy with me, eventhough he doesn't actually engage in any actual fighting."
ja "You'd better learn your place here quickly boy!"
le "Stop being so jealous Jake! Get over the fact that [name] didn't receive any beta-radiations in the crotch area like you did!"
hide jake01b
hide pennyfriendly01
hide beneb
show jake02b at center
show pennyfriendly01 at midright
show beneb at left
with fastdissolve
ja "Humpf..."
le "Finally, we have a second scout on our team, Penny."
hide pennyfriendly01
show pennyfriendly02 at midright
with fastdissolve
pe "Welcome aboard [name]! I'm Penny, I'm a Road Warrior but I joined the compound as a scout a few months ago. Hopefully, we'll work together one day."
mc "A Road Warrior? What's that?"
hide pennyfriendly02
show pennyfriendly01 at midright
with fastdissolve
le "After the apocalypse, many people were left to fend for themselves. The Road Warriors allowed them to belong to something again."
le "Most Road Warriors are outside, in the wilderness. You'll probably meet some on your missions."
mc "What missions?"
le "We didn't rescue you for you to be a drag on our resources. You'll have to accomplish the missions I will give you if you want to be allowed to stay here."
le "Most missions will require that you leave the compound and explore the wilderness in the hope of finding Trumpf City."
le "Our scouts are all going out on reconnaissance today. It might be a good idea to join one of them to see for yourself."
label ScoutChoice01:
menu:
    "No thank you, I'm good staying here.":
        le "I don't think you quite understood. I wasn't asking. I was ordering you."
        jump ScoutChoice01
    "Go with Bella":
        hide beneb
        show bella01b at left
        with fastdissolve
        be "No worries, I have plenty of space in my truck!"
        $ withbe = True
        jump IntroMission01
    "Go with Penny":
        hide pennyfriendly01
        show pennyhappy01 at midright
        with fastdissolve
        pe "You're in for a ride with me boy! I have the meanest, badest motherfucking motorbike in the area!"
        $ withpe = True
        jump IntroMission01

label IntroMission01:
$ hex = 01
scene command02
show lena06
show pennyfriendly01 at right
show bella01b at left
show commandtable
with dissolve
le "Right... Let's have a look at the map..."
scene mapgeneral
show hexA1idle
show hexA2idle
show hexA0idle
show hexA3idle
show lenaarm01
le "We are here. As you can see, we need to expand our knowledge of the surrounding lands."
hide lenaarm01
hide hexA1idle
show hexA1ahover
show lenaarm02
le "Area A1 seems like a good choice..."
mc "Ah. Apparently, we can only go East. Why is that?"
hide lenaarm02
le "The radioactivity levels in the Rockies are too high."
mc "But we are right next to them. What about the levels in the compound?"
le "They are totally acceptable. The reading on our Russian-made dosimeter indicates a level of 3.6 Roentgen."
le "Not great, not terrible."
scene command02 with dissolve
show lena06
show pennyfriendly01 at right
show bella01b at left
show commandtable
if withbe:
    le "Enough chitchat, today, you will go and explore area A1 with Bella."
    hide bella01b
    hide commandtable
    show bella02b at left
    show commandtable
    with fastdissolve
    be "We went there the other day, it's just desert Chief!"
    hide lena06
    hide commandtable
    show lena02
    show commandtable
    with fastdissolve
    le "The Trumpf Militia is closing in on us, we have to make sure they are still not there! Do not discuss my orders Bella!"
    be "Sorry Chief..."
    hide lena02
    hide commandtable
    show lena07
    show commandtable
    with fastdissolve
    le "Now off you go. And take [name] with you."
    $ withnone = True
    jump Explore
    
if withpe:
    le "Enough chitchat, today, you will go and explore area A1 with Penny."
    hide pennyfriendly01
    hide commandtable
    show pennypensive at right
    show commandtable
    with fastdissolve
    pe "I believe we went there the other day Chief..."
    hide lena06
    hide commandtable
    show lena05
    show commandtable
    with fastdissolve
    le "Yes I am well aware of that Penny. But the Trumpf Militia is closing in on us, we have to make sure they are still not there..."
    hide pennypensive
    hide commandtable
    show pennyfriendly01 at right
    show commandtable
    with fastdissolve
    pe "I see Chief..."
    hide lena05
    hide commandtable
    show lena06
    show commandtable
    with fastdissolve
    le "Now off you go. And take [name] with you."
    $ withnone = True
    jump Explore

label Intro03a:
"Please enter your name"
$ name = renpy.input("My name is...")
$ name = name.strip()
$ money = 10
show screen calendar
show screen mcstats
jump Intro03