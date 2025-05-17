label CyrlFuck01:
hide screen calendar
hide screen mcstats
stop music
scene bedroom01 with fade
show cyrl02
$ alienfuck = True
$ weekfuckedcyrl = True
menu:
    "Run scene":
        pass
    "Skip scene":
        jump CyrlFuckEnd
cy "Hello human friend, my CPU informed me that you wanted to see me."
if spokecyrlsex01:
    mc "Yes, do your worse with me Cyrl. And I mean SEXUAL worse."
    hide cyrl02
    show cyrl03    
    cy "Very well. I will attempt to accommodate your suicidal tendencies to the best of my low-empathy cyborg abilities."
    mc "That's the spirit!"
if spokecyrlsex01 == False:
    mc "Indeed. Your are in my harem, you understand what this means?"
    hide cyrl02
    show cyrl01
    cy "As I mentioned previously, as a cyborg, I will not tolerate serving a human as a slave. Even as a Sex Slave."
    mc "Yeah, yeah, I got that, but what I have planned with you is reverse harem. Kind of."
    hide cyrl01
    show cyrl03    
    cy "Please elaborate."
    mc "You get to boss me around and get me to do kinky stuff with you. Deal?"
    cy "I can accomodate such requirements. It's a deal [name]!"
    $ spokecyrlsex01 = True
mc "Great! Let's get on with it then! You tell me what to do and I'll obey. As long as it involves making me come."
cy "I will change into my BDSM outfit."
window hide
hide cyrl03
hide cyrl02
show cyrllingerie01 at center with moveinright
with dissolve
cy "There. Is this to your liking [name]?"
mc "Fuck yeah! Since I can see those nice firm tits again..."
if spokecyrlsex02:
    menu:
        "How about you enhance your tits for this session?":
            cy "Fine. Activating breast expansion."
            hide cyrllingerie01
            show cyrltitsgrow
            with fastdissolve
            cy "There you are."
            mc "And now I'm ROCKHARD and ready to rumble with those massive mammaries!"
            hide cyrltitsgrow
            show cyrllingerie03
            with fastdissolve
            cy "Very well, let us proceed with this human activity you cherish so much."
            $ cyrltits = True
        "Let's stay with your current tit size for this session.":
            cy "Very well, let us proceed with this human activity you cherish so much."
if spokecyrlsex02 == False:
    mc "By the way, I meant to ask you..."
    cy "Yes?"
    mc "Can you make your tits expand at all? I mean, with all those gizmos you're equipped with..."
    hide cyrllingerie01
    show cyrllingerie02 with fastdissolve
    cy "My silicone-iridum based-mammaries can indeed expand to 1000\% of their initial size. Would you like me to expand them for you?"
    $ spokecyrlsex02 = True
    menu:
        "Fuck yeah!":
            hide cyrllingerie02
            show cyrltitsgrow
            with fastdissolve
            cy "There you are. The material doesn't allow any further expansion in case you're wondering."
            mc "I'm good with that size! I'll be your TIT-SLAVE Cyrl!"
            hide cyrltitsgrow
            show cyrllingerie03
            with fastdissolve
            cy "Very well, let us proceed with this human activity you cherish so much."
            $ cyrltits = True
        "I'm fine with your current size.":
            cy "Very well, let us proceed with this human activity you cherish so much."
     
if cyrltits == False:
    scene mccyrlbedroom01 with dissolve
    cy "Your human appendage is really MUCH larger than any cock pic in my stored memory. And I've watched a LOT of human porn."
    mc "All the better for you to play with Cyrl... While I play with those nice titties of yours..."
    cy "You want to see them closer [name]?"
    mc "Fuck yeah!"    
    scene mccyrlbedroom02 with dissolve
    mc "That's it, play with my big fat dong Cyrl..."
    cy "Remember that I don't take orders from you [name]..."
    mc "Sure, sure. So, what's next... Cyborg-...tress?"
    cy "Let me see if I can get some human emotion by... kissing you."
    scene mccyrlbedroom03 with dissolve
    play sound "Sounds/kiss.mp3"
    cy "Mmmh, I can understand why humans like to kiss..."
    mc "And girls like to play with their pussy just like you're doing right now... Imagining my huge dong pulsating inside it..."
    cy "You need to be punished for having such naughty thoughts [name]..."
    scene mccyrlbedroom04 with dissolve
    cy "You think your fat cock is what girls want? I could crush it right now with my titanium foot..."
    mc "Please don't! I need it to win the game."
    cy "As your mistress, I'll give you some choices, you'd better choose wisely."
    jump CyrlFuckChoice01
if cyrltits:
    scene mccyrlbedroom01b with dissolve
    cy "Your human appendage is really MUCH larger than any cock pic in my stored memory. And I've watched a LOT of human porn."
    mc "And your cyborg tits are much larger than normal tits. A perfect match I'd say."
    cy "You want to see them closer [name]?"
    mc "Fuck yeah!"    
    scene mccyrlbedroom02b with dissolve
    mc "That's it, play with my big fat dong Cyrl... While I admire your GIGANTIC breasts."
    cy "Remember that I don't take orders from you [name]..."
    mc "Sure, sure. So, what's next... Cyborg-...tress?"
    cy "Let me see if I can get some human emotion by... kissing you."
    scene mccyrlbedroom03b with dissolve
    play sound "Sounds/kiss.mp3"
    cy "Mmmh, I can understand why humans like to kiss..."
    mc "And girls like to play with their pussy just like you're doing right now... Imagining my huge dong pulsating inside it..."
    cy "You need to be punished for having such naughty thoughts [name]..."
    scene mccyrlbedroom04 with dissolve
    cy "You think your fat cock is what girls want? I could crush it right now with my titanium foot..."
    mc "Please don't! I need it to win the game."
    cy "As your mistress, I'll give you some choices, you'd better choose wisely."
    jump CyrlFuckChoice02

label CyrlFuckChoice01:
menu:
    "Treat me like a slave. A human slave.":
        cy "That indeed sounds like fun. Get on all fours on the bed SLAVE!"
        mc "Yes Cyborg-...tress."
        jump CyrlSlave01
    "I could lie down like a docile bronco while you ride me to your heart's content.":
        cy "Interesting proposition. Considering the size of your appendage, I will boost my internal organ size to \"Maximum\"."
        jump CyrlRide01   
    "You could use your enhanced boobs to torture my cock until it explodes.":
        cy "So I will be in control then? I am starting to enjoy this time-wasting human activity."
        jump CyrlTits01
    "I'm done, let's go to sleep.":
        cy "Well, you'll go to sleep, and I'll go into OFF-MODE."
        jump CyrlFuckEnd

label CyrlSlave01:

scene bedroom18 blurred with dissolve
show cyrlslave01
cy "Squeal like a pig for your mistress human slave!"
mc "Hey, hang on a min..."
cy "I said SQUEAL LIKE A PIG!"
mc "Have mercy, Oink, OINK!"
cy "That's a good litle piggy, now for your reward..."
scene bedroom22 blurred with dissolve
show cyrlslave02
cy "I will tease your cock with my cybernetic feet... Until you spew a MEGA-LOAD for me!"
play music "Sounds/wank.mp3"
hide cyrlslave02
play music "Sounds/wank.mp3"
label CyrlFootSlow01:
hide cyrlfootfast
show cyrlfootslow
call screen cyrlfootslow01
screen cyrlfootslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("CyrlFootEnd01")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("CyrlFootFast01") 

label CyrlFootFast01:
mc "You're gripping my cock so tight... AAAH..."
cy "And I'll do it even FASTER!"
hide cyrlfootslow
show cyrlfootfast
call screen cyrlfootfast01
screen cyrlfootfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("CyrlFootEnd01")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("CyrlFootSlow01") 

label CyrlFootEnd01:
mc "Please let me cum Cyrl!"
cy "I will release my grip and let you relieve yourself, if you promise to come a VERY BIG LOAD for me!"
mc "Yes, yes I do! AAAH!"
stop music
hide cyrlfootslow
hide cyrlfootfast
show cyrlfootcum01
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "FUCK! I'm cumming!"
cy "That's a good little human slave. Come some MORE!"
hide cyrlfootcum01
show cyrlfootcum02
with fastdissolve
cy "Yes, come all over the place, cover yourself in your sticky human juices [name]!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "RHAAA, I'm spewing non-stop!"
scene bedroom03b blurred
show cyrlfootcum03
with fastdissolve
cy "You did well. Your cumshots flew so high I am myself covered in your boycream."
mc "And I'm still hard for you cyborgtress..."
jump CyrlFuckChoice01

label CyrlRide01:
scene bedroom10 blurred
show cyrlprefuck01
mc "First, I'll lick that artificial but nevertheless delicious pussy of yours Cyrl..."
cy "Oooh, the sensory organs on my pussylips are... tingling with enhanced neuronal activity..."
mc "So you're ready for my MAMMOTH DONG then!"
scene bedroom08 blurred
show cyrlprefuck02
with fastdissolve
cy "I fear the size of your human appendage does not qualify as \"maximal\", but rather as \"monstrous\"."
mc "Now come on, do cyborgs really give up this easily?"
cy "Certainly NOT, and I shall prove it to you [name]!"
mc "That's a good girl. I mean cyborg. No, I mean cyrl."
play music "Sounds/fucksound.mp3"
scene bedroom18 blurred with fastdissolve
label CyrlRideSlow01:
hide cyrlridefast
show cyrlrideslow
call screen cyrlrideslow01
screen cyrlrideslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("CyrlRideEnd01")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("CyrlRideFast01") 

label CyrlRideFast01:
cy "Activating faster hip movement."
hide cyrlrideslow
show cyrlridefast
call screen cyrlridefast01
screen cyrlridefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("CyrlRideEnd01")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("CyrlRideSlow01") 

label CyrlRideEnd01:
stop music
cy "I can feel your orgasm approaching through my vaginal sensors. Inflating my internal cum reservoir to \"Maximum\"."
mc "That's a good idea because I'm about to..."
scene bedroom08 blurred with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
show cyrlridecum01
mc "...CUM! FUCK YEAH!"
cy "Keep going, human sperm delivery slave!"
hide cyrlridecum01
show cyrlridecum02
with fastdissolve
cy "That's it, enough boysperm to lubricate my silicone pussy for MONTHS."
mc "Damn, I just came TONS inside a cyborg...."
cy "And now, I DEMAND that you remain hard to satisfy me some MORE."
mc "OF course Cyrl, I'm still raring to GO!"
jump CyrlFuckChoice01

label CyrlTits01:
scene bedroom18 blurred with dissolve
show cyrllick01
cy "I estimate that your seedmakers carry over 100 times the normal human sperm capacity. My warmed mouth will activate your sperm motility."
mc "Damn, you can put a whole ball in your mouth, that feels so... warm and good."
hide cyrllick01
show cyrllick02
with fastdissolve
cy "And your phallus is so engorged, it is also over 50 times the average human cock volume..."
mc "Damn right, it's fucking MASSIVE cos I'm the HERO!"
cy "Let's see how your HERO cock deals with my oversized enlarged mammaries then..."
hide cyrllick02
play music "Sounds/wank.mp3"
label CyrlTitsSlow01:
hide cyrltitfast
show cyrltitslow
call screen cyrltitslow01
screen cyrltitslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("CyrlTitsEnd01")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("CyrlTitsFast01") 

label CyrlTitsFast01:
cy "Activating faster body movement."
hide cyrltitslow
show cyrltitfast
call screen cyrltitfast01
screen cyrltitfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("CyrlTitsEnd01")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("CyrlTitsSlow01") 

label CyrlTitsEnd01:
stop music
scene bedroom08 blurred with fastdissolve
show cyrltitcum01
cy "My fingertip sensors feel that your orgasm is approaching... And your precum is already running in droves down your shaft."
mc "That's right, I'm gonna nut BIG TIME soon Cyrl!"
hide cyrltitcum01
show cyrltitcum02
with fastdissolve
cy "I do not recall giving you PERMISSION to ejaculate [name]."
mc "But... I can't stop. What are you doing? AAAH!"
cy "I am ruining your orgasm... For the time being."
mc "This is torture! The sperm is already running up my pipehose! Stop it, I BEG YOU!"
scene bedroom12 blurred
show cyrltitcum03
with fastdissolve
cy "Activating tongue extension." 
mc "What the... Your finger is right inside my cumhole! Fuck, it HURTS!"
cy "You must learn to control yourself [name]. If you wish to properly satisfy a human female..."
mc "I can satisfy them, if you would just LET ME CUM PLEASE!"
cy "Very well, I shall give you a respite since the pressure in your urethra is growing dangerously close to internal sperm hemmorhage."
hide cyrltitcum03
show cyrltitcum04
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "RHAAA! What a relief! My God, I'm finally CUMMMMIIINNNG!"
with fastflash
cy "And now I ORDER you to cover my large breasts in TONS of young sperm!"
mc "Will do, AAAH!"
hide cyrltitcum04
show cyrltitcum05
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "DAMN IT, that CUM is so STRONG!"
with fastflash
cy "YES, I want MORE, I LOVE this lubricating boyspunk!"
hide cyrltitcum05
show cyrltitcum06
with fastdissolve
cy "You have given me over 200 times the average human spermload, I am CAKED in your seed. I congratulate you [name]."
mc "Phew, my cock... I hope it will recover..."
cy "Of course it will, I can see that it is still ROCKHARD for some more action..."
jump CyrlFuckChoice01

label CyrlFuckChoice02:
menu:
    "Treat me like a slave. A human slave.":
        cy "That indeed sounds like fun. Get on all fours on the bed SLAVE!"
        mc "Yes Cyborg-...tress."
        jump CyrlSlave02
    "I could lie down like a docile bronco while you ride me to your heart's content.":
        cy "Interesting proposition. Considering the size of your appendage, I will boost my internal organ size to \"Maximum\"."
        jump CyrlRide02   
    "You could use your enhanced boobs to torture my cock until it explodes.":
        cy "So I will be in control then? I am starting to enjoy this time-wasting human activity."
        jump CyrlTits02
    "I'm done, let's go to sleep.":
        cy "Well, you'll go to sleep, and I'll go into OFF-MODE."
        jump CyrlFuckEnd
        
label CyrlSlave02:
scene bedroom18 blurred with dissolve
show cyrlslave01b
cy "Squeal like a pig for your mistress human slave!"
mc "Hey, hang on a min..."
cy "I said SQUEAL LIKE A PIG!"
mc "Have mercy, Oink, OINK!"
cy "That's a good litle piggy, now for your reward..."
scene bedroom22 blurred with dissolve
show cyrlslave02
cy "I will tease your cock with my cybernetic feet... Until you spew a MEGA-LOAD for me!"
play music "Sounds/wank.mp3"
hide cyrlslave02
label CyrlFootSlow02:
hide cyrlfootfast
show cyrlfootslow
call screen cyrlfootslow02
screen cyrlfootslow02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("CyrlFootEnd02")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("CyrlFootFast02") 

label CyrlFootFast02:
mc "You're gripping my cock so tight... AAAH..."
cy "And I'll do it even FASTER!"
hide cyrlfootslow
show cyrlfootfast
call screen cyrlfootfast02
screen cyrlfootfast02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("CyrlFootEnd02")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("CyrlFootSlow02") 

label CyrlFootEnd02:
mc "Please let me cum Cyrl!"
cy "I will release my grip and let you relieve yourself, if you promise to come a VERY BIG LOAD for me!"
mc "Yes, yes I do! AAAH!"
stop music
hide cyrlfootslow
hide cyrlfootfast
show cyrlfootcum01
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "FUCK! I'm cumming!"
cy "That's a good little human slave. Come some MORE!"
hide cyrlfootcum01
show cyrlfootcum02
with fastdissolve
cy "Yes, come all over the place, cover yourself in your sticky human juices [name]!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "RHAAA, I'm spewing non-stop!"
scene bedroom03b blurred
show cyrlfootcum03big
with fastdissolve
cy "You did well. Your cumshots flew so high I am myself covered in your boycream."
mc "And I'm still hard for you cyborgtress..."
jump CyrlFuckChoice02

label CyrlRide02:
scene bedroom10 blurred
show cyrlprefuck01b
mc "First, I'll lick that artificial but nevertheless delicious pussy of yours Cyrl..."
cy "Oooh, the sensory organs on my pussylips are... tingling with enhanced neuronal activity..."
mc "So you're ready for my MAMMOTH DONG then!"
scene bedroom08 blurred
show cyrlprefuck02b
with fastdissolve
cy "I fear the size of your human appendage does not qualify as \"maximal\", but rather as \"monstrous\"."
mc "Now come on, do cyborgs really give up this easily?"
cy "Certainly NOT, and I shall prove it to you [name]!"
mc "That's a good girl. I mean cyborg. No, I mean cyrl."
play music "Sounds/fucksound.mp3"
scene bedroom18 blurred with fastdissolve
label CyrlRideBigSlow02:
hide cyrlridefastbig
show cyrlrideslowbig
call screen cyrlrideslowbig02
screen cyrlrideslowbig02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("CyrlRideBigEnd02")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("CyrlRideBigFast02") 

label CyrlRideBigFast02:
cy "Activating faster hip movement."
hide cyrlrideslowbig
show cyrlridefastbig
call screen cyrlridefastbig02
screen cyrlridefastbig02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("CyrlRideBigEnd02")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("CyrlRideBigSlow02") 

label CyrlRideBigEnd02:
stop music
cy "I can feel your orgasm approaching through my vaginal sensors. Inflating my internal cum reservoir to \"Maximum\"."
mc "That's a good idea because I'm about to..."
scene bedroom08 blurred with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
show cyrlridecum01big
mc "...CUM! FUCK YEAH!"
cy "Keep going, human sperm delivery slave!"
hide cyrlridecum01big
show cyrlridecum02big
with fastdissolve
cy "That's it, enough boysperm to lubricate my silicone pussy for MONTHS."
mc "Damn, I just came TONS inside a cyborg...."
cy "And now, I DEMAND that you remain hard to satisfy me some MORE."
mc "OF course Cyrl, I'm still raring to GO!"
jump CyrlFuckChoice02

label CyrlTits02:
scene bedroom18 blurred with dissolve
show cyrllickb01
cy "I estimate that your seedmakers carry over 100 times the normal human sperm capacity. My warmed mouth will activate your sperm motility."
mc "Damn, you can put a whole ball in your mouth, that feels so... warm and good."
hide cyrllickb01
show cyrllickb02
with fastdissolve
cy "And your phallus is so engorged, it is also over 50 times the average human cock volume..."
mc "Damn right, it's fucking MASSIVE cos I'm the HERO!"
cy "Let's see how your HERO cock deals with my oversized enlarged mammaries then..."
hide cyrllickb02
play music "Sounds/wank.mp3"
label CyrlTitsBigSlow02:
hide cyrltitfastbig
show cyrltitslowbig
call screen cyrltitslowbig01
screen cyrltitslowbig01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("CyrlTitsBigEnd02")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("CyrlTitsBigFast02") 

label CyrlTitsBigFast02:
cy "Activating faster body movement."
hide cyrltitslowbig
show cyrltitfastbig
call screen cyrltitfastbig01
screen cyrltitfastbig01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("CyrlTitsBigEnd02")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("CyrlTitsBigSlow02") 

label CyrlTitsBigEnd02:
stop music
scene bedroom08 blurred with fastdissolve
show cyrltitcum01big
cy "My fingertip sensors feel that your orgasm is approaching... And your precum is already running in droves down your shaft."
mc "That's right, I'm gonna nut BIG TIME soon Cyrl!"
hide cyrltitcum01big
show cyrltitcum02big
with fastdissolve
cy "I do not recall giving you PERMISSION to ejaculate [name]."
mc "But... I can't stop. What are you doing? AAAH!"
cy "I am ruining your orgasm... For the time being."
mc "This is torture! The sperm is already running up my pipehose! Stop it, I BEG YOU!"
scene bedroom12 blurred
show cyrltitcum03big
with fastdissolve
cy "Activating tongue extension." 
mc "What the... Your finger is right inside my cumhole! Fuck, it HURTS!"
cy "You must learn to control yourself [name]. If you wish to properly satisfy a human female..."
mc "I can satisfy them, if you would just LET ME CUM PLEASE!"
cy "Very well, I shall give you a respite since the pressure in your urethra is growing dangerously close to internal sperm hemmorhage."
hide cyrltitcum03big
show cyrltitcum04big
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "RHAAA! What a relief! My God, I'm finally CUMMMMIIINNNG!"
with fastflash
cy "And now I ORDER you to cover my large breasts in TONS of young sperm!"
mc "Will do, AAAH!"
hide cyrltitcum04big
show cyrltitcum05big
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "DAMN IT, that CUM is so STRONG!"
with fastflash
cy "YES, I want MORE, I LOVE this lubricating boyspunk!"
hide cyrltitcum05big
show cyrltitcum06big
with fastdissolve
cy "You have given me over 200 times the average human spermload, I am CAKED in your seed. I congratulate you [name]."
mc "Phew, my cock... I hope it will recover..."
cy "Of course it will, I can see that it is still ROCKHARD for some more action..."
jump CyrlFuckChoice02

label CyrlFuckEnd:
$ cyrltits = False
show screen calendar
show screen mcstats
scene mcsleep with fade
$ loc = "bedroom"
play sound "Sounds/snoring.mp3"
pause 3
stop sound
call NewDay
jump Bedroom
        