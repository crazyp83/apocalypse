label AngieCosplay:
hide screen calendar
hide screen mcstats
$ alienfuck = True
scene bedroom01 with dissolve
mc "Angie should be arriving any minute now, with her Star Angel costume... I should get into character and wear my Captain America outfit..."
scene bedroom02 with fade
show angiecosplay01
an "I'm STAR ANGEL! I fight the bad guys with my magic wand wherever they are in the WHOLE GALAXY!"
mc "I have a magic wand too..."
an "Do you? Then, we can fight TOGETHER and become RULERS of the GALAXY!"
hide angiecosplay01
scene bedroom02 blurred with dissolve
show angiecosplay02
mc "Yes, CAPTAIN AMERICA is always on the side of the good guys!"
an "He's my FAVORITE super-hero!"
hide angiecosplay02
show angiecosplay03 with fastdissolve
an "I hope Captain America likes my little butt!"
mc "He sure does Star Angel... His wand is getting bigger."
hide angiecosplay03
show angiecosplay04 with fastdissolve
an "Wow, I hope it's a really BIG wand so you can do a lot of DAMAGE with it!"
mc "It's a pussy destroyer alright."
if angiecosplayed:
    an "Yeah, it actually destroyed MY pussy! But tonight you have to use it to destroy our ENEMIES' pussies!"
    mc "Well, you're making it hard right now so it will be a piece of cake! Let's fight them with my rock-hard magic wand!"
if angiecosplayed == False:
    an "What? Why would you want to hurt nice little kittens?"
    mc "Never mind what I said Star Angel, stand next to me and let's FIGHT together!"
scene mcangel01 with dissolve
mc "Thanks to your courage and my HUGE wand, we have VANQUISHED our foes. Let's savor our victory now, what do you say Star Angel?"
an "Oh yes! Let's celebrate! I want to thank your wand for saving the GALAXY!"
scene mcangel02 with fastdissolve
if angiecosplayed:
    mc "There, put your hand on it and feel it get even BIGGER from relishing in its numerous victories!"
    an "Mmmh, it sure is getting REALLY big Captain America! You must have the LARGEST wand in the whole galaxy!"
    an "But you're being VERY naughty Captain America... Star Angel is feeling..."
if angiecosplayed == False:
    mc "There it is, you can thank it by playing with it..."
    an "Is it?... Your COCK is your wand???"
    mc "Well, yeah, I mean, what the hell did you think I was talking about Star Angel?"
    an "Err... You're being VERY naughty Captain America... Star Angel is feeling..."
scene mcangel03 with fastdissolve
mc "...naughty too?"
if angiecosplayed:
    an "Yes! Star Angel is a very very naughty girl for looking at Captain America's GIANT rod like that!"
    mc "Well Star Angel fought valiantly, so she deserves a reward for her courage."
    an "Really? Wow, That's super-ACE! What reward will she get?"
    mc "Hold my rod of power and show it your appreciation for saving the world Star Angel and you'll get your reward!"
if angiecosplayed == False:
    an "Oh my God, what are you doing [name]? I... didn't expect that..."
    mc "I like to continue my cosplay games with some SEXY games, are you up for playing with me or not?"
    an "Well...err... Ok, if this is how you play... I'll play along!"
    mc "Then hold my rod of power and show it your appreciation for saving the world Star Angel!"
scene mcangel04 with fastdissolve
an "This my Ahegao face while holding your ROD OF POWER!"
mc "Silly but cute."
scene mcangel05 with fastdissolve
an "Your rod is become all slick with some nasty baby-juice. You're really NAUGHTY [name]!"
mc "And super-horny too. The faster you make me cum, the sooner you'll get your reward Star Angel..."
an "Are my cute breasts making you horny?"
mc "Yes, yes they are... AAAH, keep playing with my rod... AAAHH"
scene mcangel06 with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
an "Yes, give me a BIG reward for helping defeat our enemies Captain America!"
scene mcangel07 with fastdissolve
mc "Damn, you made me cum so fast! RHAAA!"
an "Star Angel has the fastest hands in the WHOLE GALAXY!"
scene mcangel08 with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "FUCK! I spewed all over the place in no time Star Angel!"
an "And you gave me a HUGE nasty reward Captain America!"
$ angiecosplayed = True
mc "How about we continue our sexy games then? My rod is still READY FOR MORE ACTION!"
if hareman:
    an "Yes, let's play some more!"
    jump AngiePreSexChoice    
an "I... I don't think so [name]. I don't want to play anymore, I need to get rid of all that sticky cream you dumped all over me..."
mc "OK, another time then maybe Angie?"
an "Sure, I had GREAT FUN playing with you [name]!"
call LustPlusAngie
$ period += 1
$ missionandone = True
show screen calendar
show screen mcstats
jump Bedroom

label AngieBedroom:
hide screen calendar
hide screen mcstats
if pregan and preganstart >= 3:
    scene bedroom01
    show angiepregnant02a
    with fade
    an "You wanted to play with my growing doll? I don't think I can show it to you yet..."
    mc "No, I was more like thinking of playing with my cock and your pussy again. Just like we agreed when you joined my harem."
    hide angiepregnant02a
    show angiepregnant02b
    with fastdissolve
    an "But... That would DESTROY my doll! I don't want that to happen!"
    mc "Come on, it's just a baby, I mean doll."
    hide angiepregnant02b
    show angiepregnant02a
    with fastdissolve
    an "When the bad guys attacked us, I lost my Barbie doll, and when I found it in the rubbles, it didn't have a HEAD ANYMORE!"
    mc "Ok, ok, calm down, we won't be doing the thing tonight then... To protect the doll. *sigh*"
    hide angiepregnant02b
    show angiepregnant02a
    with fastdissolve
    an "Yippee, you're ACE! Bye [name]!"
    hide angiepregnant02a with dissolve
    $ weekfuckedangie = True    
    jump Bedroom    
$ alienfuck = True
$ weekfuckedangie = True
scene bedroom02 with dissolve
show angiehesitant
menu:
    "Run scene":
        pass
    "Skip scene":
        jump AngieEnd
an "I'm not sure I should be here..."
mc "Of course you should. You're in my harem remember? I'm taking care of you and you take care of me..."
hide angiehesitant
show angieasking
an "What do you want me to do to take care of you? I want to play and wear a costume please!"
if maidcostume:
    mc "I have the perfect costume for you. A sexy French maid one. You pretend you're my maid and you've just finished cleaning up but you've been naughty and you didn't do a good job."
    hide angieasking
    show angiehappy01
    an "Oh, that sounds like FUN! I'll go and put it on then!"
    play music "v07/datemusic.mp3"
    scene bedroom02 blurred with fade
    show angiemaid01 with moveinright
    an "I have just finished cleaning up for you sir."
    mc "You missed some spots."
    hide angiemaid01
    show angiemaid02 with fastdissolve
    an "Oh? What did I miss sir?"
    mc "You forgot to polish the knob."
    scene bedroom02 blurred with fastdissolve
    show angiemaid03 with fastdissolve
    an "I'm so sorry sir! I can do it now for you if you want?"
    mc "Yeah, but you still deserve a punishment. For being so naughty."
    scene bedroom02 blurred with fastdissolve
    show angiemaid04
    an "You're right, I deserve it sir. Spank me for being such a naughty maid!"
    mc "That's exactly what I had in mind."
    scene mcangiemaid01 with fastdissolve
    an "Oh my God, what is that sir? Its' so BIG!"
    mc "That's the knob you forgot to polish naughty maid! Come over here and bend over my knees..."
    scene mcangiemaid02a with fastdissolve
    mc "Now. Prepare to receive your punishment so that you don't forget to polish my knob next time..."
    scene mcangiemaid02b with fastdissolve
    play sound "Sounds/slap.mp3"
    an "Ouch! It hurts, but it's my fault for not doing my job properly!"
    mc "So will you be a good maid in the future Angie?"
    scene mcangiemaid02a with fastdissolve
    an "Yes sir, I promise!"
    scene mcangiemaid02b with fastdissolve
    play sound "Sounds/slap.mp3"
    mc "There's a good girl... You deserve a reward now..."
    scene mcangiemaid03 with fastdissolve
    mc "You're all wet down there... You're getting excited again naughty maid?"
    play sound "Sounds/moaning.mp3"
    an "Oooh... Uuuh. Yes sir, it's not my fault, your cock is... ssooo BIG! I want it!"
    scene mcangiemaid04 with fastdissolve
    mc "Then let's move on to the serious stuff. On my bed."
    stop music
if maidcostume == False and americacostume == True:
    mc "Why don't you get into your Star Angel costume then? I'll get my Captain America outfit and we can play sexy games together."
    hide angieasking
    show angiehappy01
    an "Alright! That sounds like great fun! I'll go and get dressed then."
    jump AngieCosplay
if maidcostume == False and americacostume == False: 
    mc "Well, I don't have any costume for us to play with right now, let's just go straight to my bed and fuck like rabbits."
    an "Where the game in that?"
    mc "Err... It's called \"Down the Rabbit-hole\". You're the hole, I'm the rabbit."
    an "That's a strange game but I'll play since you're protecting me from the bad people..."
    mc "That's the spirit."

label AngiePreSexChoice:
scene bedroom03 blurred with dissolve
show mcangiekiss01
mc "First, let's kiss and seal the deal..."
an "God, you're so STRONG! You're carrying my body on your horsedick!"
mc "That's right, and it will protect you from the bad people cos it's so powerful!"
scene bedroom09 blurred with dissolve
show mcangiekiss02
an "Show me how POWERFUL it is then please [name]!"

label AngieFuckChoice:
stop music
menu:
    "Why don't you play with your pussy, make it nice and wet for me..." if angieplayed == False:
        an "Wh...What? But..."
        mc "Come on, I'm sure you've played with yourself before and you've ENJOYED it a lot. Show me how you do it."
        an "OK... But there's a LOT of juice that will flow out, I'm warning you!"
        mc "Then I can play \"catch the juice\"."
        an "Alright, you try and catch MY juice, it will be FUN!"
        jump AngieSpread
    "Play a game of tug on my cock...":
        an "And what do I get if I win?"
        mc "A CREAMY reward!"
        an "Yippee!"
        jump AngieHandjob    
    "Time to get some backdoor action...":
        an "What? But... We can't make babies that way!"
        mc "Storks use the backdoor to deliver babies. Since they're all dead, someone's got to fill their shoes..."
        jump AngieAnal
    "Ride me like a donkey!":
        an "A donkey? More like a HORSE in your case! I LOVE horse-riding, I used to have a poney before..."
        jump AngieFuck
    "You want a little doll to play with? (Impregnate Angie)" if preganready >= 3 and impregnatedsomeone == False and babyangie == False:
        an "Oooh, yes please!"
        mc "Then get ready to get impregnated! In eight weeks, you'll be ready to pop that doll."
        an "Oh, really? That sounds weird, I thought dolls came from cabbage patches. You're sure I can have one that way?"
        mc "If you can bleed, you can breed. So let's get moving."
        an "Yippee!"
        $ impregnatedsomeone = True
        jump AngieImpregnation
    "I'm done, let's go to sleep.":
        jump AngieEnd
 

label AngieSpread:
$ angieplayed = True
scene bedroom03b with dissolve
show angieprespread01
mc "I'm ready to catch your juices in my glass when they squirt out Angie!"
if persistent.tipson:
    show minigametip at tips with dissolve
    pause
    hide minigametip
hide angieprespread01
show angiespread
window hide
show angiecatch
pause
$ d3rollsquirt=renpy.random.randint(1,3)
if d3rollsquirt == 1:
    call screen angiecatch01
    screen angiecatch01:
        modal True
        default time_left = 0.6

        add "Angie/angiesquirtleft01c.png"
        if time_left <= 0.5:
            add "Angie/angiesquirtleft01b.png"
        if time_left <= 0.4:
            add "Angie/angiesquirtleft01a.png"
        if time_left <= 0.3:
            add "Angie/angiesquirtleft02c.png"
        if time_left <= 0.2:
            add "Angie/angiesquirtleft02b.png"
        if time_left <= 0.1:
            add "Angie/angiesquirtleft02a.png"

        if time_left <= 0:
            timer .01 action Return
        else:
            timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)

        imagebutton:
            focus_mask True
            idle "Angie/catchleft.png"
            hover "Angie/catchleft.png"
            action Jump ("Catch")
        
        bar value StaticValue(time_left, 0.5):
            xalign 0.1 yalign 0.02
            xmaximum 200 
            ymaximum 10

if d3rollsquirt == 2:
    call screen angiecatch02
    screen angiecatch02:
        modal True
        default time_left = 0.6
        
        add "Angie/angiesquirtcenter01c.png"
        if time_left <= 0.5:
            add "Angie/angiesquirtcenter01b.png"
        if time_left <= 0.4:
            add "Angie/angiesquirtcenter01a.png"
        if time_left <= 0.3:
            add "Angie/angiesquirtcenter02c.png"
        if time_left <= 0.2:
            add "Angie/angiesquirtcenter02b.png"
        if time_left <= 0.1:
            add "Angie/angiesquirtcenter02a.png"

        if time_left <= 0:
            timer .01 action Return
        else:
            timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)

        imagebutton:
            focus_mask True
            idle "Angie/catchcenter.png"
            hover "Angie/catchcenter.png"
            action Jump ("Catch")
        
        bar value StaticValue(time_left, 0.5):
            xalign 0.1 yalign 0.02
            xmaximum 200 
            ymaximum 10

if d3rollsquirt == 3:
    call screen angiecatch03
    screen angiecatch03:
        modal True
        default time_left = 0.6

        add "Angie/angiesquirtright01c.png"
        if time_left <= 0.5:
            add "Angie/angiesquirtright01b.png"
        if time_left <= 0.4:
            add "Angie/angiesquirtright01a.png"
        if time_left <= 0.3:
            add "Angie/angiesquirtright02c.png"
        if time_left <= 0.2:
            add "Angie/angiesquirtright02b.png"
        if time_left <= 0.1:
            add "Angie/angiesquirtright02a.png"

        if time_left <= 0:
            timer .01 action Return
        else:
            timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)

        imagebutton:
            focus_mask True
            idle "Angie/catchright.png"
            hover "Angie/catchright.png"
            action Jump ("Catch")
        
        bar value StaticValue(time_left, 0.5):
            xalign 0.1 yalign 0.02
            xmaximum 200 
            ymaximum 10

label CatchFail:
scene bedroom03b blurred
show angiesquirtend
$ renpy.pause(1.0, hard=True)
mc "Shit, I was too slow..."
$ angiejuicelost = True
jump AngieSpreadEnd

label Catch:
scene bedroom03b blurred
show angiesquirtend
$ renpy.pause(1.0, hard=True)
mc "Yeah, I caught most of your squirting juices inside my glass! I win!"
if missioncy and missioncydone == False and knowpussyjuice:
    mc "And I've got some lubricant for Cyrl! PLENTY of it..."
    window hide
    show missioncydone01 at posmission
    $ renpy.pause(2.0, hard=True)
    pause
    hide missioncydone01
    $ missioncydone = True

label AngieSpreadEnd:
an "I think I made a big mess on your sheets..."
if angiejuicelost:
    an "But I won and you lost this FUN game!"
mc "Don't worry about it, I'll get them cleaned."
if angiejuicelost:
    an "I won and you lost this FUN game! Let's play another game..."
    jump AngieFuckChoice
an "You won that game... I want my revenge, let's play another game!"
jump AngieFuckChoice

label AngieHandjob:
scene bedroom12 with dissolve
show angiepretug01
mc "Start tugging on it..."
an "Can I use both hands? I's a very BIG pole to tug on."
mc "Of course, the more hands the merrier."
scene bedroom12 blurred with dissolve
play music "Sounds/wank.mp3"
label AngieTugSlow:
hide angietugfast
show angietugslow
call screen angietugslow01
screen angietugslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AngieTugEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AngieTugFast") 

label AngieTugFast:
hide angietugslow
show angietugfast
mc "Oooh, your hands are so good on my shaft, I might give you your creamy reward real SOOON!"
call screen angietugfast01
screen angietugfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AngieTugEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AngieTugSlow") 

label AngieTugEnd:
stop music
scene bedroom11 blurred
show mcangiecum01
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Damn, you're making me CUUUMMM!"
scene bedroom12 blurred
hide mcangiecum01
show mcangiecum02
an "Does this mean I won the tug of war game?"
mc "Sure, and here's your reward for winning! RHAAAA!"
hide mcangiecum02
show mcangiecum03
an "Oh wow, I must have been a BIG winner to receive so MUCH rewarding cream! So much winning!"
mc "And I'm not tired of all this winning since I'm STILL HARD for more!"
jump AngieFuckChoice

label AngieAnal:
scene bedroom12 with dissolve
show angieanalprefuck01
an "Please be careful. I'm really tight back there and your cock... It's sssoo big!"
scene bedroom09 with dissolve
show angieanalprefuck02
an "Oh my God, you're stretching my ass wide open!"
mc "Just open up a bit wider... There you go."

scene bedroom10 blurred with dissolve
play music "Sounds/fucksound.mp3"
label AngieAnalSlow:
hide angieanalfast
show angieanalslow
call screen angieanalslow01
screen angieanalslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AngieAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AngieAnalFast") 

label AngieAnalFast:
hide angieanalslow
show angieanalfast
an "This is so good, you're fucking me so hard!!!"
call screen angieanalfast01
screen angieanalfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AngieAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AngieAnalSlow") 

label AngieAnalEnd:
mc "Fuck, your tight ass is making me CUUUMMMM!"
an "Yes, flood my backside like the storks do!"
stop music
scene bedroom03b blurred
show angieanalcum01
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Damn it, your ass muscles are milking meeeee!"
hide angieanalcum01
show angieanalcum02 with fastdissolve
an "Wow, you're such an ACE friend to be offering me that much baby-juice!"
mc "I have enough left to plaster your body too! RHAAA!"
hide angieanalcum02
scene bedroom12 with fastdissolve
show angieanalcum03
mc "Phew! This time I'm drained. But still hard for some MORE FUN."
jump AngieFuckChoice
   
label AngieFuck:
scene bedroom09
show mcangieprefuck01
an "Mmh, what do you want me to do with that rock-hard love pole [name]?!"
mc "Straddle me Angie, we'll play rodeo sex, you're the cowboy and I'm the bull..."
an "Yippee, that sounds like so much FUN!"
scene bedroom09 blurred
play music "Sounds/fucksound.mp3"
label AngieFuckSlow:
hide angiefuckfast
show angiefuckslow
call screen angiefuckslow01
screen angiefuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AngieFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AngieFuckFast") 

label AngieFuckFast:
hide angiefuckslow
show angiefuckfast
an "I'm still holding on, make the game harder [name]!"
mc "Sure, bounce on that saddle cock FASTER and I'll make it HARDER for you Angie!"
call screen angiefuckfast01
screen angiefuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AngieFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AngieFuckSlow")

label AngieFuckEnd:
stop music
an "Come inside me please, I don't care if I get pregnant!"
scene bedroom03b blurred
show mcangiefuckcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "RHAAA! As you wish Angie!"
an "Oh wow, I can FEEL it inside me, there's so much of it and it feels so warm!"
hide mcangiefuckcum01
show mcangiefuckcum02
with fastdissolve
an "Uuh, what's that on my back, oh my God, you're STILL spewing your baby-cream???"
with flash
mc "Fuck yeah, you've got enough inside you to impregnate you ten times over so I'm giving you a nice back lotion sample!"
an "Thank you [name], you're such an ACE friend! I can't wait for what sex games you have planned next..."
jump AngieFuckChoice

label AngieImpregnation:
scene bedroom48
show angiepreimpregnate01 with dissolve
an "Are you playing with my tiddies? Are they big enough for you to get you excited?"
mc "Fuck yeah, they're perfect Angie..."
an "Yippee, I'm so happy! i'm going to get impregnated!"
hide angiepreimpregnate01
show angiepreimpregnate02
with fastdissolve
mc "See? My cock is getting REAL hard for you!"
an "Oh name, it's sssoo BIG! You're going to dump a really HUGE load inside me, aren't you?"
mc "That's right Angie, I'm going to fill you up to the BRIM! Get on all fours and get ready to receive my breeding cum-cannon!"

play music "Sounds/womansex01.mp3"
label AngiePregnantSlow:
hide angiepregnantfast
hide angiepregnantpussyslow
hide angiepregnantpussyfast
scene bedroom16
show angiepregnantslow
call screen angiepregnantslow01
screen angiepregnantslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AngiePregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AngiePregnantFast") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("AngieImpregnateSlow") 

label AngieImpregnateSlow:
hide angiepregnantslow
hide angiepregnantfast
hide angiepregnantpussyfast
scene bedroom37 blurred
show angiepregnantpussyslow
call screen angiepregnantpussyslow01
screen angiepregnantpussyslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AngiePregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AngieImpregnateFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AngiePregnantSlow") 

label AngiePregnantFast:
hide angiepregnantslow
hide angiepregnantpussyslow
hide angiepregnantpussyfast
scene bedroom16
show angiepregnantfast
call screen angiepregnantfast01
screen angiepregnantfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AngiePregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AngiePregnantSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("AngieImpregnateFast") 

label AngieImpregnateFast:
hide angiepregnantslow
hide angiepregnantfast
hide angiepregnantpussyslow
scene bedroom37 blurred
show angiepregnantpussyfast
call screen angiepregnantpussyfast01
screen angiepregnantpussyfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AngiePregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("AngieImpregnateSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AngiePregnantFast") 
            
label AngiePregnantEnd:
an "Are you about to pump me full of baby-seed?"
stop music
scene bedroom37 blurred
show angieimpregnatecum01
with dissolve
mc "YES I AM, RIGHT NOW, RHAAA!"
play music "Sounds/splooge02.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
with fastflash
an "I'm squirting! It means I'm SUPER-thrilled by it!"
$ pregan = True
scene bedroom16 blurred
show angieimpregnatecum02
with dissolve
stop music
play sound "Sounds/splooge01.mp3"
mc "STILL PUMPING, GODDAMIT, THIS PUSSY'S TIGHT, AAHHH!"
show angieimpregnatecum02 
with fastflash
an "Oh yippee, it means I'll hold your baby-batter even better!"
stop music
scene bedroom48 blurred
show angieimpregnatecum03
with dissolve
play sound "Sounds/gasp.mp3"
an "AAAH, my stomach... It's FULL OF YUMMY BABY SPUNK!!!"
play sound "Sounds/panting.mp3"
mc "I confirm, I can see it bulging. Phew, I think I'm done."
scene bedroom18 blurred
show angieimpregnatecum04
with dissolve
an "I'll do like teacher says and let it flow down inside."
mc "I think I filled you up so much, it's not really necessary Angie... Let's go to bed, I'm exhausted."

label AngieEnd:
show screen calendar
show screen mcstats
scene angiemcsleep with fade
$ loc = "bedroom"
play sound "Sounds/snoring.mp3"
pause 3
call NewDay
jump Bedroom

