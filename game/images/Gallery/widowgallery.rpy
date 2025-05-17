label WidowGallery:
call screen gallerywidow
screen gallerywidow:
    add "Gallery/widowgallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("gallerywidow"), Jump ("MainGallery")]

    if renpy.seen_image("widowlairoutside"):
        imagebutton:
            focus_mask True
            idle "Gallery/widowgallery01.png" xpos 621 ypos 100
            hover "Gallery/widowgallery01.png"
            action Jump ("WidowGallery01")

    if renpy.seen_image("widowlairoutside") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("WidowGallery")

    if renpy.seen_image("scarlettblowbackground"):
        imagebutton:
            focus_mask True
            idle "Gallery/widowgallery02.png" xpos 1050 ypos 100
            hover "Gallery/widowgallery02.png"
            action Jump ("WidowGallery02")

    if renpy.seen_image("scarlettblowbackground") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("WidowGallery")

    if renpy.seen_image("scarlettnancy01"):
        imagebutton:
            focus_mask True
            idle "Gallery/widowgallery03.png" xpos 1478 ypos 100
            hover "Gallery/widowgallery03.png"
            action Jump ("WidowGallery03")

    if renpy.seen_image("scarlettnancy01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("WidowGallery")


    add "Gallery/galleryfuture.png" xpos 621 ypos 400

    add "Gallery/galleryfuture.png" xpos 1050 ypos 400

    add "Gallery/galleryfuture.png" xpos 1478 ypos 400

    add "Gallery/galleryfuture.png" xpos 621 ypos 700

    add "Gallery/galleryfuture.png" xpos 1050 ypos 700

    add "Gallery/galleryfuture.png" xpos 1478 ypos 700

    add "Gallery/gallerygrid02.png"
    add "Gallery/textwidow.png"
        
label WidowGallery01:
scene widowlairoutside
show widowdesert02
show sandstorm02
wi01 "This way, hurry up! We're almost there..."
scene widowlair01 with fade
show widow01
wi "We can breathe here, this place is well insulated from the elements."
mc "Who are you? You look familiar."
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
show widownude at midright with moveinright
wi "Oh my God! That thing is fucking HUGE! Let me worship it like it deserves Captain America..."
scene widowlair03 blurred
show widowsex01
wi "*gulp* How... How big is this gigantic thing?"
mc "17 inches long according to \"Measure Metrics\" on Daz Studio. So over 20 porn inches."
wi "Fuck my mouth with it Captain America, I've been a naughty girl..."
scene widowlair04 blurred
show widowsex02
mc "There you go, nice and slow at first..."
scene widowlair05 with dissolve
play music "Sounds/hardsucking.mp3"
label WidowBJslowerx:
hide widowbjfast
show widowbjslow
call screen widowbjslowx
screen widowbjslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WidowBJEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WidowBJfasterx") 

label WidowBJfasterx:
hide widowbjslow
show widowbjfast
call screen widowbjfastx
screen widowbjfastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WidowBJEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WidowBJslowerx") 

label WidowBJEndx:
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
label WidowFuckSlowx:
play music "Sounds/massive.mp3"
hide widowfuckfast
show widowfuckslow
call screen widowfuckslowx
screen widowfuckslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WidowFuckEndx")    
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WidowFuckFastx") 

label WidowFuckFastx:
hide widowfuckslow
show widowfuckfast
call screen widowfuckfastx
screen widowfuckfastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WidowFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WidowFuckSlowx") 
            
label WidowFuckEndx:
wi "Cum for me Captain America!"
stop music
scene widowlair05
play sound "Sounds/mccum.mp3"
show widowfuckcum
mc "FUCK! Sssooo fucking GOOOOD!"
wi "I can feel your warm ball-batter all over my back! I LOVE IT!"
mc "I've got more shots for you Black Widow!"
wi "Damn man, you really are a cum machine!"
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
jump WidowGallery

label WidowGallery02:
stop music
scene widowlair01
show widow03
wi "I like it when you come and visit me Captain America. I feel so alone in this place."
hide widow03
show widow02
with fastdissolve
wi "It makes me feel naughty to be with you. Are you feeling naughty too?"
mc "Of course! VERY naughty..."
wi "Then follow me to my SEX lair!"
scene widowroom01 with dissolve
wi "Get fully undressed this time, no need to play games anymore... [name]. \nI'll get into a skimpy outfit for you..."
show scarlett01 with dissolve
wi "So, do you like?"
mc "Fuck YEAH!"
hide scarlett01
show scarlett02
with fastdissolve
wi "Is that all you have to say?"
mc "Err... You're so sexy Scarlett!"
hide scarlett02
show scarlett03
with fastdissolve
wi "Is that cock getting HUGE and HARD for me yet?"
mc "Yes, ROCK-HARD for you Scarlett! And for that amazing ass of yours!"
scene widowroom02 blurred
show scarlett03b
with fastdissolve
wi "Are you going to POUND IT nice and HARD then?..."
mc "For sure, YES, YES!!!"
scene widowroom02
show scarlett04
with fastdissolve
wi "I can't wait... Thinking about that horsecock of yours is making me all WET down there... I just HAVE to take my panties off..."
hide scarlett04
show scarlett05
with fastdissolve
wi "I'm just imagining it sliding in and out of my TIGHT pussy... stretching me sssooo GOOOD... mmmh..."
scene widowroom03 blurred with fastdissolve
show scarlett06
wi "I think I'm ready now... My pussy hole is gaping and all slippery..."
mc "I can see that..."
$ scarlettfuckx = False
$ scarlettblowx = False
label ScarlettFuckChoicex:
wi "So, what's next, STUD?"
menu:
    "Let me prep your pussy. With my tongue!":
        wi "That's a great idea!"
        jump ScarlettLickx
    "Get on the edge of the bed, and open up that fuckhole for me!":
        wi "You're gonna POUND me into the bed [name]? I can't wait..."
        jump ScarlettPoundx
    "Give me a blowjob...":
        wi "What a NAUGHTY boy!"
        jump ScarlettBlowjobx
    "Get on all fours...":
        jump ScarlettFuckx
    "I'd say we're done for the day..." if scarlettfuckx or scarlettblowx:
        jump ScarlettEndx
        
label ScarlettLickx:
scene widowroom07
show widowlick01
with dissolve
wi "Isn't my pussy just ssooo tasty [name]?!"
mc "Sure is. *lick* Scarlett. *lick*"
hide widowlick01
show widowlick02
with fastdissolve
wi "I can tell you're enjoying it, your tongue is slurping up all my juices. You are such a NAUGHTY boy!!"
mc "I'm getting a meal anf a half there. * slurp* Your pussy is so wet... *slurp*"
scene widowroom03 blurred
show widowlick03
wi "And ready for what's coming NEXT!"
jump ScarlettFuckChoicex

label ScarlettPoundx:
scene widowroom09 with dissolve
show scarlettprepound01
wi "I can feel that GIANT piece of manmeat teasing my clit. Please, fuck me [name], I can't stand it!"
mc "Alright, open up, I'm gonna pummel you with my monster shaft!"
scene widowroom08 blurred
show scarlettprepound02
wi "Oh shit, just your massive cockhead is STRETCHING me so much. But I can take it don't worry, so just FUCK ME HARD, STUD!"
label ScarlettPoundSlowx:
scene widowroom09
play music "Sounds/scarlettpound.mp3"
hide widowpoundfast
show widowpoundslow
call screen scarlettpoundslowx
screen scarlettpoundslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ScarlettPoundEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ScarlettPoundFastx") 

label ScarlettPoundFastx:
hide widowpoundslow
show widowpoundfast
call screen scarlettpoundfastx
screen scarlettpoundfastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ScarlettPoundEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ScarlettPoundSlowx") 

label ScarlettPoundEndx:
stop music
$ scarlettpoundx = True
scene widowroom08 blurred
show widowpoundcum01
play sound "Sounds/mccum.mp3"
wi "YES, fill me up like a cumdump [name]! I just LOVE cum and YOU cum ssooo much!!"
mc "Fuck, it's spilling out all over the place!"
wi "Pull out and cover my body with the rest of your MEGA-LOAD!!"
hide widowpoundcum01
show widowpoundcum02
play sound "Sounds/mccum.mp3"
mc "Sure, I've got plenty more! RHAAA!"
wi "Damn it man, how do you manage to always deliver such GIANT loads? I'm CAKED in your rich creamy ball-batter!"
mc "You bring the best out of me I guess... Now, where did we leave off?"
jump ScarlettFuckChoicex

label ScarlettFuckx:
scene widowroom06 with dissolve
show scarlettprefuck
wi "Are you going to pile-drive that titanic rod in me?"
mc "Yep..."
wi "FUCK ME HARD! GIVE ME YOUR MONSTER MANMEAT YOU MUSCLE STUD!"
mc "Full steam ahead Scarlett!"
scene widowroom05 with dissolve
label ScarlettFuckSlowx:
play music "Sounds/scarlettpound.mp3"
hide scarlettfuckfast
show scarlettfuckslow
call screen scarlettfuckslowx
screen scarlettfuckslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ScarlettFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ScarlettFuckFastx") 

label ScarlettFuckFastx:
hide scarlettfuckslow
show scarlettfuckfast
call screen scarlettfuckfastx
screen scarlettfuckfastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ScarlettFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ScarlettFuckSlowx") 

label ScarlettFuckEndx:
stop music
$ scarlettfuckx = True
hide scarlettfuckslow
hide scarlettfuckfast
show scarlettfuck00b
show scarlettfuckcum01
play sound "Sounds/mccum.mp3"
wi "Oh my God, your cumshots are SSOO POWERFUL! I can feel every single one of them!"
mc "And your pussy is already full to the brim!"
wi "Come all over my back now, there is no cum inflation tag in this game. YET."
hide scarlettfuckcum01
hide scarlettfuck00b
show scarlettfuckcum02
play sound "Sounds/mccum.mp3"
mc "Sure, I've got plenty more! RHAAA!"
jump ScarlettFuckChoicex

label ScarlettBlowjobx:
if scarlettfuckx:
    wi "Let me take care of that cock of yours to KEEP IT ROCK-HARD for ANOTHER round!"
if scarlettfuckx == False:
    wi "Let me take care of that cock of yours..."

scene widowroom04
show scarlett07 with fastdissolve
if scarlettfuckx :
    mc "You want some more monster dick Scarlett?"
    wi "Yes I do... I want more... of that GIANT MANMEAT of yours! It's so fucking heavy and MASSIVE..."
if scarlettfuckx == False:
    wi "It's bigger than my head... So fucking heavy and MASSIVE..."

hide scarlett07
show scarlett08 with fastdissolve
wi "Let me worship it... Lick it ALL OVER... slowly and sensuously..."
mc "Fuck! You're making me so hard!"
wi "And then..."
label ScarlettBlowSlowx:
scene scarlettblowbackground with dissolve
hide scarlettblowfast
show scarlettblowslow
call screen scarlettblowslowx
screen scarlettblowslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ScarlettBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("ScarlettBlowFastx") 

label ScarlettBlowFastx:
hide scarlettblowslow
show scarlettblowfast
call screen scarlettblowfastx
screen scarlettblowfastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("ScarlettBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("ScarlettBlowSlowx") 

label ScarlettBlowEndx:
$ scarlettblowx = True
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
jump ScarlettFuckChoicex

label ScarlettEndx:
scene widowroom01 with dissolve
show scarlett09
wi "I sure enjoyed this little Avengers get-to-know-each-other-better session Captain America!"
mc "Yeah, it was great getting to know you in... more depth, Black Widow!"
$ scarlettfuckx = False
$ scarlettblowx = False
jump WidowGallery

label WidowGallery03:
scene widowlair01
show widow02 at right with move
hide widow02
show widow07 at right
show nancymarvel08 at left with moveinleft
wi "Oh wow, your mother looks AMAZING in that outfit! We definitely have a new Captain Marvel fighting alongside the AVENGERS!"
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
mc "It's part of the team bonding procedure that the Black Widow put in place mom. Just go with the flow."
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
mo "And what do you plan to achieve with that GIANT erect cock, son? This is no time for hanky-panky sweetie! I need HELP!"
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
label WidownancyHJSlowx:
hide widownancyhjfast
show widownancyhjslow
call screen widownancyhjslow01x
screen widownancyhjslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WidownancyHJEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WidownancyHJFastx") 

label WidownancyHJFastx:
hide widownancyhjslow
show widownancyhjfast
mc "Yes, FASTER!"
call screen widownancyhjfast01x
screen widownancyhjfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WidownancyHJEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WidownancyHJSlowx") 

label WidownancyHJEndx:
mc "Yes, you're making me cum! Get ready mom!"
mo "Please do try and aim your pint-sized shots at my costume sweetie pie..."
hide widownancyhjslow
hide widownancyhjfast
show widownancyhjcum01
stop music
play sound "Sounds/cumming.mp3"
wi "It's flying EVERYWHERE! You'll definitely get some on your costume Captain Marvel!"
mo "I hope it's a LOT if this ever has a chance to work..."
scene widowlair05 blurred with fastdissolve
show widownancyhjcum02
play sound "Sounds/mccum.mp3"
wi "That's it, blast that young virile goo all over her, Captain America!"
mc "Keep still mom, I've got more ropes of cum to deliver flying right at you! AAAH!"
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
wi "Oh my God [name]! Your mother... She's twirling her tongue on my pussy... Ooooh!"
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
mc "I think I'm gonna start with you Captain Mom. Err, I mean Captain Marvel."
mo "Ooh, YES please Captain America!"
scene widownancyprefuck02 with dissolve
mc "There, the head is almost in, just open really WIDE..."
mo "I'm trying... Just shove it in sweetie pie!"
mc "Alright, here we go!"
scene widowroom13 blurred with dissolve
label WidownancyFuckaSlowx:
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
call screen widownancyfuckaslow01x
screen widownancyfuckaslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckaEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WidownancyFuckaFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckbSlowx") 

label WidownancyFuckaFastx:
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
call screen widownancyfuckafast01x
screen widownancyfuckafast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckaEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WidownancyFuckaSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckbSlowx") 


label WidownancyFuckcSlowx:
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
call screen widownancyfuckcslow01x
screen widownancyfuckcslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckcEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WidownancyFuckcFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckdSlowx") 

label WidownancyFuckcFastx:
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
call screen widownancyfuckcfast01x
screen widownancyfuckcfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckcEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WidownancyFuckcSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckdFastx") 

    
label WidownancyFuckbSlowx:
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
call screen widownancyfuckbslow01x
screen widownancyfuckbslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckbEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WidownancyFuckbFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckaSlowx") 

label WidownancyFuckbFastx:
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
call screen widownancyfuckbfast01x
screen widownancyfuckbfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckbEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WidownancyFuckbSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckaFastx") 

label WidownancyFuckdSlowx:
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
call screen widownancyfuckdslow01x
screen widownancyfuckdslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckdEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WidownancyFuckdFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckcSlowx") 

label WidownancyFuckdFastx:
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
call screen widownancyfuckdfast01x
screen widownancyfuckdfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckdEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WidownancyFuckdSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckcFastx") 


label WidownancyFuckaEndx:
mo "You're pounding me so good sweetie pie, it's time for you to COME INSIDE ME!"
stop music
hide widownancyfuckaslow
hide widownancyfuckafast
show widownancyacum01
stop music
play sound "Sounds/cumming.mp3"
mc "I'm filling you up mom, AAAH!"
mo "AAAH, I can feel it PULSING inside me, I'm cumming with you!!!"
hide widownancyacum01
show widownancyacum02
mc "Take some more shots on your back, RHAAAA!"
mo "Oh my God sweetie pie, your loads... They are so BIG for me!"
mc "Phew... I'm still hard so I'm going to fuck you some more!"
mo "What? You're such a SUPER-STUD for mommy [name]. Fuck her again HARD!"
hide widownancyacum02
$ momcum += 1
jump WidownancyFuckcSlowx

label WidownancyFuckcEndx:
mo "You're pounding me so good sweetie pie, it's time for you to COME INSIDE ME!"
stop music
hide widownancyfuckcslow
hide widownancyfuckcfast
show widownancyccum01
stop music
play sound "Sounds/cumming.mp3"
mc "I'm filling you up Nancy, AAAH!"
mo "AAAH, I can feel it [name], I'm cumming with you!!!"
hide widownancyccum01
show widownancyccum02
mc "I'm filling you up mom, AAAH!"
mo "AAAH, I can feel it son, I'm cumming with you!!!"
$ momcum += 1
if momcum >= 2 and widowcum >= 2:
    jump WidownancyFuckAllEndx
mc "Phew... I'm still hard so I'm going to fuck you some more mom! Get ready for the pounding of your life!"
mo "Oh, I AM ready. Ready to take on my son's MONSTERCOCK once more!"
hide widownancyccum02
jump WidownancyFuckcSlowx

label WidownancyFuckbEndx:
if widowcum == 0:
    wi "Let it loose, Captain America! My hungry pussy WANTS a MEGA-LOAD of cream!"
if widowcum >= 1:
    wi "Let it loose, Captain America! My hungry pussy wants ANOTHER MEGA-LOAD of cream!"
stop music
hide widownancyfuckbslow
hide widownancyfuckbfast
show widownancywidowcumb01
stop music
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
    jump WidownancyFuckAllEndx
mc "Phew... I'm still hard so I'm going to fuck you some more Black Widow! Get ready to receive Captain's America's SUPERHERO cock!"
hide widownancywidowcumb03
if momcum == 1:
    jump WidownancyFuckdSlowx
if momcum == 0:
    jump WidownancyFuckbSlowx

label WidownancyFuckdEndx:
if widowcum == 0:
    wi "Let it loose, Captain America! My hungry pussy WANTS a MEGA-LOAD of cream!"
if widowcum >= 1:
    wi "Let it loose, Captain America! My hungry pussy wants ANOTHER MEGA-LOAD of cream!"
stop music
hide widownancyfuckdslow
hide widownancyfuckdfast
show widownancywidowcumd01
stop music
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
    jump WidownancyFuckAllEndx
mc "Phew... I'm still hard so I'm going to fuck you some more Black Widow! Captain America's superhero BULLBALLS are not done with you!"
wi "Oh my God, with such stamina, you could FUCK our enemies to DEATH Captain America!"
hide widownancywidowcumd03
if momcum == 1:
    jump WidownancyFuckdSlowx
if momcum == 0:
    jump WidownancyFuckbSlowx

label WidownancyFuckAllEndx:
mc "Phew, you drained so many loads from my balls..."
mo "I'm sssoo proud of you son. You just came and came and came again, I thought you just wouldn't STOP!"
wi "And you just showed us why you DESERVE to be Captain America... Captain America."
scene widowroom01 with dissolve
show scarlett11 at midright with moveinright
show nancypurple01 at midleft with moveinleft
$ momcum = 0
$ widowcum = 0
mo "I think it's time we got cleaned up..."
mc "I guess you're right. Let's go."
wi "Don't forget about me. Come back to visit me often BOTH of you! *wink*"
jump WidowGallery
