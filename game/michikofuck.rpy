label MichikoFuck01:
hide screen calendar
hide screen mcstats
if pregmi and pregmistart >= 3:
    scene bedroom01
    show michikopreggo02
    with fade
    mi "If you were thinking of having sex with me tonight, I'm sorry to say that you can't..."
    mc "What? Why not?"
    mi "As much as I enjoy your BRUTAL fucking, I must think of our baby. Such a poor inoccent little thing. He can't get hurt by your monstercock and that's FINAL!"
    mc "That was a brutal way of saying no..."
    hide michikopreggo02 with dissolve
    $ weekfuckedmichiko = True    
    jump Bedroom    
$ alienfuck = True
scene bedroom01 with fade
show michiko01
menu:
    "Run scene":
        pass
    "Skip scene":
        $ weekfuckedmichiko = True        
        jump MichikoFuckEnd
mi "Hi [name]? You called for me? For some SEXY time?"
mc "That's right Michiko! Tonight is HOT SEXY TIME together!"
hide michiko01
show michiko02
mi "And what do you have planned for our HOT SEXY TIME?"
if lingerie02:
    mc "I have a new lingerie set for you to try on Michiko!"
    hide michiko02
    show michiko04
    mi "I hope it fits my HUGE boobs..."
    mc "It should, it has an XXXL sized bra cup."
    mi "Great! I'll try it on straight away then [name]."
    jump MichikoLingerie
if lingerie02 == False:
    mc "Many, MANY things..."
    hide michiko02
    show michiko04    
    mi "You do know I love it ROUGH don't you?"
    mc "Then it will be HARD and ROUGH!"
    mi "Great! Let's get on with it then! I'll get undressed and you get ROCKHARD, deal?"
    mc "Deal!"
    jump MichikoNoLingerie    

label MichikoLingerie:
play music "v07/datemusic.mp3"
scene bedroom01 with fade
show michikolingerie01 at center with moveinright
mi "So, does it hug my curves well enough [name]?"
mc "It sure does Michiko!"
hide michikolingerie01
show michikolingerie02 with fastdissolve
mi "You haven't seen the back yet... You need to see how well it hugs my ass cheeks."
hide michikolingerie02
show michikolingerie03 with fastdissolve
mc "It hugs it very nicely... VERY nicely."
scene bedroom01 blurred with fastdissolve
show michikolingerie04
mi "Then I hope you'll fuck me roughly. VERY ROUGHLY."
mc "Anything you desire Michiko! My cock is hard and ready to service you every which way!"
scene bedroom01 with fastdissolve
show michikolingerie05
mi "Then take it out and let me see it [name]..."
scene mcmichiko01 with fastdissolve
mc "MMmh, you're already all wet down there Michiko..."
mi "I'm wet for that HUGE weapon of yours... Show it to me please [name]!"
scene mcmichiko02 with fastdissolve
mi "Oh FUCK! It's just... the BIGGEST cock I've ever seen in my life! And I never tire of seeing it AGAIN."
mc "It's all yours for the night Michiko..."
scene mcmichiko03 with fastdissolve
mi "I wish you would fuck me EVERY night with it [name]. But a STUD like you needs a harem to satisfy your insatiable SEXUAL appetite..."
mc "You can try and convince me to call you as often as possible..."
mi "Feel up my breast then and see what's in store for YOU!"
scene mcmichiko04 with fastdissolve
mi "How do they feel [name]? Big enough to FUCK with your giant boycock?"
mc "Of course Michiko, so nice and firm, perfect for some serious titfucking."
mi "Then let's get on with with it, I'm just too horny to wait any longer!"
mc "Sure, let's move to my bed."
stop music
jump MichikoFuckChoice

label MichikoNoLingerie:
scene bedroom01 with fade
show michikonaked at center with moveinright
mi "I'm ready to service you [name]. And get pounded as BRUTALLY as I deserve."

label MichikoFuckChoice:
$ weekfuckedmichiko = True
stop music
menu:
    "Get on your kness and worship my enormous fuckstick Michiko!":
        mi "Yes Master, your giant boymeat is ssooo addictive..."
        jump MichikoPraise
    "Get on all fours, I'm gonna pound your pussy into oblivion!":
        mi "Oh, FUCK!"
        jump MichikoPound    
    "I'm gonna pummel through your cleavage with my giant teenage meat!":
        mi "And cover them with an ENORMOUS load of boycream I hope!"
        jump MichikoTits
    "Give me a footjob and make me explode Michiko.":
        mi "My feet are so flexible you'll come in no time [name]..."
        jump MichikoFeet
    "You're ready to be impregnated. And I'm ready to impregnate you." if pregmiready >= 3 and impregnatedsomeone == False and babymichiko == False:
        $ impregnatedsomeone = True
        mi "I bet that's going to be a BRUTAL breeding. How will you proceed?"
        mc "Breeding by IMPALEMENT!"
        jump MichikoImpregnation
    "I'm done, let's go to sleep.":
        mi "Thanks for giving me the brutal fucking I deserved [name]..."
        jump MichikoFuckEnd

label MichikoPraise:
scene bedroom10 with dissolve
show michikoprepraise01
mi "Bring that MONSTER cock over here [name] so I can worship it like it deserves..."
mc "It's all yours Michiko..."
hide michikoprepraise01
show michikoprepraise02
mi "Such a MIGHTY organ deserves much praising..."
mc "It's a lethal weapon alright. Thanks to tons of alpha-radiations."
mi "Which turned you into an ALPHA-STUD."
mc "Lick it nice and slow Michiko..."
mi "Of course MASTER STUD. I'll do more than that, I'll gobble it down!"

scene bedroom03b blurred with dissolve
play music "Sounds/hardsucking.mp3"
label MichikoPraiseSlow:
hide michikopraisefast
show michikopraiseslow
call screen michikopraiseslow01
screen michikopraiseslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoPraiseEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MichikoPraiseFast") 

label MichikoPraiseFast:
mc "Go faster Michiko, shove my fat cock all the way down your throat!"
hide michikopraiseslow
show michikopraisefast
call screen michikopraisefast01
screen michikopraisefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoPraiseEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MichikoPraiseSlow") 

label MichikoPraiseEnd:
mc "That's it. I'm gonna BLAST my load inside your hungry mouth!"
hide michikopraiseslow
hide michikopraisefast
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
show michikopraise09
show michikopraisecum01
with fastdissolve
mc "Gobble it up, Deep-throat me until you choke while I dump my seed directly down your throat Michiko!"
mi "Gllrrbbb!"
hide michikopraise09
hide michikopraisecum01
show michikopraisecum02
with fastdissolve
mc "You're making a right mess of it Michiko.. Here, taste some more thick jets of my cum! RHAAA!"
hide michikopraisecum02
show michikopraisecum03
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Damn it, I think you've drained me. For now. You've got TONS of cum all over your face and my thick load is dripping down your huge tits..."
mi "I'm a total cumwhore mess but I LOVED IT [name]. Mmmh, let me slurp some more juice out your monster cock..."
mc "Get cleaned up and let's move on..."
jump MichikoFuckChoice
    
label MichikoPound:
scene bedroom14 blurred with dissolve
show michikoprefuck01
mi "Let me open up as wide as possible for your GIANT teenage fuckstick [name]."
mc "Yeah, while I lube it up with some precum..."
scene bedroom15 with fastdissolve
show michikoprefuck02
mc "And now, I'll slowly ease it in..."
mi "Oh FUCK, it's so BIG!"
mc "That's just the tip Michiko. Wait for the rest..."
scene bedroom09 blurred
play music "Sounds/fucksound.mp3"
label MichikoPoundSlow:
hide michikopoundfast
show michikopoundslow
call screen michikopoundslow01
screen michikopoundslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoPoundEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MichikoPoundFast") 

label MichikoPoundFast:
mi "I'm getting POUNDED by your MONSTER ROD! But I want it EVEN HARDER!"
hide michikopoundslow
show michikopoundfast
call screen michikopoundfast01
screen michikopoundfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoPoundEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MichikoPoundSlow") 

label MichikoPoundEnd:
mc "I'm about to blow Michiko! Gonna fill you up anytime now..."
mi "YES! treat me like your cum dump [name]!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene bedroom09
show michikofuckcum01 with fastdissolve
mc "Here it comes, FUUUUCKKK, RHAAAA!"
mi "Go on, fill me up like a gas guzzler with your hot load! AAAH, I'm cumming too!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
hide michikofuckcum01
show michikofuckcum02
mc "DAMN, I'm nutting NON-STTOOOPP! AAH!"
mi "I can feel it! Oh God, I'm cumming so hard too!"
hide michikofuckcum02
show michikofuckcum03
mc "And I'll claim you as my cum-whore by blasting your back now, FUCK YEAH!"
mi "Do it [name], I AM your cum-whore!"
hide michikofuckcum03
show michikofuckcum04
mi "Oh my God, I'm never been so BRUTALLY fucked... And covered in TONS of boyspunk too... That was sssoo good, thank you [name]."
mc "Who said I was done with you?"
mi "What, you're gonna fuck me some more after you just dumped a MONUMENTAL load all over me?"
scene bedroom17 with fastdissolve
show michikoreprefuck01
mc "You got that right! Get ready for some more BRUTAL pounding!"

scene bedroom16 blurred with dissolve
play music "Sounds/womansex01.mp3"
label MichikoPoundSlow02:
hide michikorefuckfast
show michikorefuckslow
call screen michikopoundslow02
screen michikopoundslow02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoPoundEnd02")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MichikoPoundFast02") 

label MichikoPoundFast02:
mi "FUCK! Your cock is so MASSIVE! Give it to me [name], really POUND IT!"
hide michikorefuckslow
show michikorefuckfast
call screen michikopoundfast02
screen michikopoundfast02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoPoundEnd02")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MichikoPoundSlow02") 

label MichikoPoundEnd02:
mc "I'm gonna cum again... NOW!"
hide michikorefuckslow
hide michikorefuckfast
show michikorefuckcum01 with fastdissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mi "Oh my God, another GIANT boyload for me! You're making me cum AGAIN!"
mc "Take that Michiko! Feel the POWER of my blasts inside your tight pussy!"
mi "You're such an ALPHA-STUD [name]! I can't believe you can unleash such a TORRENT of spunk after your previous MEGA-LOAD!"
hide michikorefuckcum01
show michikorefuckcum02
mc "You'd better believe it! RHAAA!"
mi "Getting CUM-OWNED by the biggest BULLCOCK around! CUMMING!"
scene bedroom18 blurred
show michikorefuckcum03
mc "There you go, a few more blasts and we can move on to something else."
mi "Like, more BRUTAL FUCKING?"
mc "Exactly..."
jump MichikoFuckChoice
    
label MichikoTits:
scene bedroom17 with dissolve
show michikopretit01
mi "Damn [name], that cock of yours is a LETHAL weapon... Fuck my tits without mercy with it!"
mc "Will do Michiko, will do..."
scene bedroom18 blurred with dissolve
play music "Sounds/fucksound.mp3"
label MichikoTitSlow:
hide michikotitfast
show michikotitslow
call screen michikotitslow01
screen michikotitslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoTitEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MichikoTitFast") 

label MichikoTitFast:
mi "Go on, slide it even FASTER between my firm mammaries!"
hide michikotitslow
show michikotitfast
call screen michikotitfast01
screen michikotitfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoTitEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MichikoTitSlow") 

label MichikoTitEnd:
mi "Now COVER me from head to toes in your red-hot spunk [name]!"
hide michikotitslow
hide michikotitfast
show michikotitcum01
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "There you go Michikooooo! AAAH!"
mi "Oh FUCK! There's more cum BLASTING out in a single shot than ten full orgasms from beta-males!"
mc "And I've got plenty more for you, open your mouth wide!"
hide michikotitcum01
show michikotitcum02
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "That's it, eat it all up Michiko! Fuck YEAH!!!"
mi "Glllr.... Mmmmm..."
scene bedroom20 blurred
show michikotitcum03
mi "I want my face to be covered like if I had been in bukkake gangbang!"
mc "You'll look like it I promise once I'm done spewing my sauce! RHAAA!"
mi "Yeah, over a dozen MONSTER SHOTS and still counting, keep PLASTERING my face with it [name]!"
hide michikotitcum03
show michikotitcum04
mc "That's it Michiko, you've drained me... But I gave you more cum than you would have received from over 100 men I'd say."
mi "More like 500 men combined I can tell you, WOW! And you're STILL HARD for more?"
mc "Of course Michiko! Let's move on to something EVEN MORE BRUTAL!"
jump MichikoFuckChoice

label MichikoFeet:
scene bedroom15 with dissolve
show michikoprefeet01
mc "First, I'll prep your toes by licking them..."
mi "Since you're into BRUTAL fucking, I'll be the one on my back and you'll be the one FUCKING my feet."
mc "Great, that way I can control the pace and everything."
scene bedroom19
show michikofeet01
mc "Ready Michiko? My dong is sure ready to FUCK YOUR FEET."
mi "Yes, do what you want with them and then COVER THEM in your thick sauce [name]!"
play music "Sounds/wank.mp3"
label MichikoFeetSlow:
hide michikofeetfast
hide michikofeetpovslow
hide michikofeetpovfast
scene bedroom19 blurred
show michikofeetslow
call screen michikofeetslow01
screen michikofeetslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoFeetEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MichikoFeetFast") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("MichikoFeetPOVSlow") 
        
label MichikoFeetPOVSlow:
hide michikofeetfast
hide michikofeetslow
hide michikofeetpovfast
scene bedroom14 blurred
show michikofeetpovslow
call screen michikofeetpovslow01
screen michikofeetpovslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoFeetEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MichikoFeetPOVFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MichikoFeetSlow") 

label MichikoFeetPOVFast:
hide michikofeetfast
hide michikofeetslow
hide michikofeetpovslow
scene bedroom14 blurred
show michikofeetpovfast
call screen michikofeetpovfast01
screen michikofeetpovfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoFeetEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MichikoFeetPOVSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MichikoFeetFast") 

label MichikoFeetFast:
hide michikofeetslow
hide michikofeetpovslow
hide michikofeetpovfast
scene bedroom19 blurred
show michikofeetfast
call screen michikofeetfast01
screen michikofeetfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoFeetEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MichikoFeetSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("MichikoFeetPOVFast") 

label MichikoFeetEnd:
mc "Your feet are ssoo soft, I'm gonna CUM soon!"
hide michikofeetslow
hide michikofeetpovslow
hide michikofeetpovfast
hide michikofeetfast
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene bedroom19 blurred
show michikofeetcum01
mc "Damn, I'm nutting right now! FUCK YEAH!"
mi "Yeah, show me what you've got STUD! I bet you have an awful LOT, don't you?"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
scene bedroom20 blurred with dissolve
show michikofeetcum02
mc "You tell me Michiko! RHAAA!"
mi "What a CUM GEYSER! You really have bottomless balls don't you?"
mc "You're the one bringing the best out of me Michiko! AAH!"
scene bedroom14 blurred with dissolve
show michikofeetcum03
mi "Now I'm going to have to clean up all this cum, because I bet you're still hard for some more brutal loving aren't you?"
mc "You got that right Michiko. So get cleaned up and let's move on..."
jump MichikoFuckChoice
    
label MichikoImpregnation:
scene bedroom13
show michikoprepreg02 with dissolve
mi "Then show me how STRONG you are, my breeding STALLION!"
mc "I'll show, I'll LIFT YOU UP on my raging hardon!"
scene bedroom13 blurred
show michikoprepreg01 
with fastdissolve
play sound "Sounds/moaning02.mp3"
mi "You REALLY did, that's AMAZING!"
mc "Of course I did, and now my powerful bullcock is ready to IMPREGNATE you!"
window hide
hide michikoprepreg01
show michikoprepreg03 
with fastdissolve
mi "Fuck me HARD, please. AS HARD as you LIKE!"
mc "Will do..."
play music "Sounds/womansex02.mp3"
label MichikoPregnantSlow:
hide michikopregnantfast
hide michikopregnantsceneslow
hide michikopregnantscenefast
scene bedroom13 blurred
show michikopregnantslow
call screen michikopregnantslow01
screen michikopregnantslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoPregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MichikoPregnantFast") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("MichikoImpregnateSlow") 

label MichikoImpregnateSlow:
hide michikopregnantslow
hide michikopregnantfast
hide michikopregnantscenefast
scene bedroom41 blurred
show michikopregnantsceneslow
call screen michikopregnantsceneslow01
screen michikopregnantsceneslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoPregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MichikoImpregnateFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MichikoPregnantSlow") 

label MichikoPregnantFast:
hide michikopregnantslow
hide michikopregnantsceneslow
hide michikopregnantscenefast
scene bedroom13 blurred
show michikopregnantfast
call screen michikopregnantfast01
screen michikopregnantfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoPregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MichikoPregnantSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("MichikoImpregnateFast") 

label MichikoImpregnateFast:
hide michikopregnantslow
hide michikopregnantfast
hide michikopregnantsceneslow
scene bedroom41 blurred
show michikopregnantscenefast
call screen michikopregnantscenefast01
screen michikopregnantscenefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoPregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("MichikoImpregnateSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MichikoPregnantFast") 
            
label MichikoPregnantEnd:
mc "I'm on the edge, Michiko, I'm on the verge of..."
stop music
scene bedroom41 blurred
show michikopregcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "CUMMING! AAAH!"
mi "BRUTALLY FLOOD MY WOMB WITH YOUR FERTILE SEED!"
play music "Sounds/splooge02.mp3"
show michikopregcum01 with flash
mc "I AM, RHAAA!"
$ pregmi = True
hide michikopregcum01
show michikopregcum02
with fastdissolve
stop music
play sound "Sounds/splooge01.mp3"
mi "Keep pumping, I want a GALLON of your spunk in me to make sure I have a baby, AAAAH!"
show michikopregcum02 with fastflash
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "There you go, take that, nutting non-stop in that amazing pussy of yours!"
mi "I'm SURE to get pregnant with such a MASSIVE load swishing inside me... I'm exhausted."
scene bedroom13 blurred
show michikopregcumend
with dissolve
play sound "Sounds/gasp.mp3"
mc "Try and keep that sperm inside you and let's go to sleep then."
mi "Oh my God, how can you still have so much POWER in you after such a BRUTAL breeding?"
mc "I'm a STUD, that's why."

label MichikoFuckEnd:
show screen calendar
show screen mcstats
scene michikomcsleep with fade
$ loc = "bedroom"
play sound "Sounds/snoring.mp3"
pause 3
call NewDay
jump Bedroom