label ExploreHex56:
if exploredhex56:
    scene fbifar01
    with fade
    play music "Sounds/desertwind01.mp3"
    mc "Back at FBI headquarters. A useless building paid for by your tax dollars."
    if exploredhex56third:
        if withbe:
            be "You KNOW you completed your training, so why are we back?"
        if withpe:
            pe "You KNOW you completed your training, so why are we back?"
        if alone:
            mc "Why I came back here knowing I already completed my training I will never know."
        mc "I must be bored. Or delusionally hopeful."
        scene fbidoorclosed with dissolve
        mc "Hi Siri, are there any new scenes in there by any chance?"
        si "No [name]. And you knew that, so why did you come back?"
        mc "Some players are just weirdos I guess."
        si "You should go back to the compound, it's getting late."
        mc "You're right Siri. Especially since there's absolutely no point in me being here whatsoever."
        jump BackHex56b
    mc "I've been told more training and assessment is available here. It says so in the changelog. Available on the main menu screen for those who never realized."
    if withbe:
        pe "I don't need FBI training so I'll wait outside for you to come back with some form of injury."
    if withbe:
        pe "I don't need FBI training so I'll wait outside for you to come back with some form of injury."
    scene fbidoorclosed with dissolve
    si "Welcome back [name]. Please place your iris on the eye detector for identity confirmation."
    mc "Come on, you know it's me! Just open the door, Siri."
    si "Not until you place your iris on the eye detector and I CONFIRM YOUR IDENTITY. [name]."
    mc "Gee, bureaucracy, hey?"
    if exploredhex56second == False:
        jump FBISecondTraining
    if exploredhex56third == False:
        jump FBIThirdTraining

if exploredhex56 == False:
    scene fbifar01
    with fade
    play music "Sounds/desertwind01.mp3"
    mc "Another lone building in the middle of nowhere..."
    if withbe:
        be "And another opportunity for you to get injured, maimed or even killed. I'll be right BEHIND you, [name]..."
    if withpe:
        pe "And another opportunity for you to get injured, maimed or even killed. I'll be right BEHIND you, [name]..."
    if alone:
        mc "And another opportunity for me to get injured, maimed or even killed. Oh, well..."
    scene fbidoorclosed with dissolve
    si "Welcome [name]. Please place your iris on the eye detector for identity confirmation."
    mc "What, Siri? What are you doing here?"
    si "My compound salary is not sufficient to pay for my Microsoft upgrades. I had to take a second job. Please place your iris on the eye detector for identity confirmation."
    mc "Come on, you know it's me! Just open the door, Siri."
    si "Not until you place your iris on the eye detector and I CONFIRM YOUR IDENTITY. [name]."
    mc "Gee, bureaucracy, hey?"
    $ exploredhex56 = True

scene fbidooropen with dissolve
play sound "v08/doorwoosh.mp3"
si "Identity confirmed. Please enter the building, Subject 42."
stop music
scene fbibackground01
show fox01 at left
with fade
play music "v08/humming.mp3"
fo "All clear. Subject 42 has entered the building. Over."
window hide
hide fox01
show fox02 at left
with fastdissolve
show dana01 at right with moveinright
mc "Who the fuck are you? And what is this place?"
if mcdeep <= 4:
    da "Welcome to FBI headquarters, [name]. My name is Agent Dana and this is Federal Agent Fox."
if mcdeep == 5:
    da "Welcome to FBI headquarters, Special Field Agent [name]. My name is Agent Dana and this is Federal Agent Fox."
mc "I ain't done nothing wrong! Err... Is that a gun in his right hand?"
hide dana01
show dana02 at right
with fastdissolve
da "What do YOU think it is?"
menu:
    "A gun?":
        hide dana02
        show dana01 at right
        with fastdissolve
        da "And if it is a gun, don't you think it would be wise to comply?"
        hide fox02
        show fox04 at left
        with fastdissolve
        fo "Subject 42 has noticed I'm holding a gun. Over."
        mc "Comply with what exactly? And why does this guy keep calling me \"Subject 42\"?"
        pass        
    "A water pistol?":
        hide dana02
        show dana01 at right
        with fastdissolve
        da "Does he look like a clown to you? You clearly aren't taking this seriously, [name]. But you WILL comply, eventually."
        hide fox02
        show fox04 at left
        with fastdissolve
        fo "Subject 42 thinks I'm holding a water pistol. Over."
        mc "Comply with what exactly? And why does this guy keep calling me \"Subject 42\"?"
hide fox04
hide dana01
show fox02 at left
show dana03 at right
with fastdissolve
da "The Bureau is aware that you might be trying to infiltrate the Supreme White House. Is this correct?"
mc "Err, no, no. I just mean to have a, err... guided tour. Like a tourist visit. No storming, just a tourist visit."
hide dana03
show dana01 at right
with fastdissolve
da "Do not fear us, [name]. FBI stands for Federal Bureau of Infiltrations. We are here to HELP you get inside the Supreme White House."
mc "And how are you going to do that?"
hide dana01
show dana02 at right
with fastdissolve
da "We will make you stronger. MENTALLY stronger."
mc "Pfff! I don't need any of that psycho-bullcrap, I'm gonna plough my way to the Supreme White House with my muscles and cock!"
hide fox02
hide dana02
show fox04 at left
show dana01 at right
with fastdissolve
da "The Supreme White House is a VERY dangerous place. You NEED our HELP."
mc "What's this freaky place anyway? I want to see what you guys are up to before I agree to anything."
hide dana01
show dana04a at right
with fastdissolve
da "Sure, come forward, I'll give you a tour. A tourist visit, so to say."
hide fox04
hide dana04a
show dana04b at right
show fox03 at farleft02
with dissolve
da "There, as you can see, nothing here is dangerous. For your body..."
window hide
play sound "v08/penclick.mp3"
$ renpy.pause(0.5, hard='True')
hide dana04b
show dana05 at right
with fastdissolve
mc "Hey! What was that? You... pricked me with your pen!"
da "Did I? Oh, it was an accident, I'm sorry. How are you feeling, [name]?"
hide dana05
show dana06 at right
with fastdissolve
mc "I... feel weak and... *yawn* ...sleepy all of a sudden..."
da "Oh? Then go and sit on that chair over there to rest for a bit..."
mc "I..."
stop music
hide screen mcstats
hide screen calendar
scene fbi01 with fade
fo "Subject 42. SUBJECT 42! WAKE UP!"
scene fbi02 with dissolve
mc "Uh? AAAH, I can't see anything, I'm BLIND!"
da "No you're not. Activate Google mental goggles, Siri."
play sound "Sounds/interfacestart.mp3"
scene fbibackground02
show dana07a at right
show fox04 at left
with dissolve
if mcdeep <= 4:
    da "There, now, can you see, [name]?"
if mcdeep == 5:
    da "There, now, can you see, Special Field Agent [name]?"
mc "Yeah. Phew. Err... Why are you half-naked, Agent Dana?"
hide dana07a
show dana10 at right
with fastdissolve
da "I'm NOT half-naked. What you are seeing is your own mental projection of me. Which means you're a pervert. We'll have to do something about that later."
hide fox04
show fox03 at left
with fastdissolve
fo "At least he's not gay, I'm not naked."
mc "That's a relief!"
hide dana10
show dana07b at right
with fastdissolve
da "Now concentrate [name]. This is not a test, this is a Real-Life Mental Event."
mc "Oh, you took your bra off. Nice tits, Agent Dana."
hide dana07b
show dana08 at right
with fastdissolve
da "No, YOU took my bra off! In your mind."
mc "Ah yes, sorry, my bad."
hide fox03
show fox02 at left
fo "He's right though, you do have a nice pair. Like, for real."
hide dana08
show dana09 at right
da "Shut up, Agent Fox! Can we get on with the test or what?"
mc "I thought it wasn't a test, I'm confused now."
da "*sigh*. Get out of the mental projection, Agent Fox, I think it's best if I stay alone with [name]. To help him CONCENTRATE."
hide fox02
show fox04 at left
fo "Subject 42 is all yours, Agent Dana. Over."
window hide
hide fox04 with moveoutleft
show dana09 at center with move
hide dana09
show dana08
with fastdissolve
da "Listen carefully [name]. You're in front of the Supreme White House and..."
mc "Am I? I can't see the entrance..."
hide dana08
show danayell
with fastdissolve
da "LISTEN! You have to IMAGINE what I'm telling you, GOT IT?"
mc "Ok, but it's really hard, especially with those tits hanging in my face."
da "Well, put some clothes back on me then!"
mc "Alright, alright, please stop yelling at me!"
hide danayell
show dana07a
with dissolve
da "Now, that's slightly better. I won't ask for more, because you are clearly mentally TOO WEAK."
hide dana07a
show dana12
with dissolve
da "So, imagine I am a Trumpf Militia Supreme White House guard, can you do that, or is it above your mental paygrade?"
mc "Gee lady, I'm not THAT stupid."
play sound "Sounds/dreaming.mp3"
hide dana12 with dissolve
show danaguard01 with dissolve
mc "There, you're a guard now. In a bikini of course."
da "*sigh* Why not actually, it might make the Real-Life Mental Test easier actually."
hide danaguard01
show danaguard02
with dissolve
da "Oooh, \"[name] the Grabber\"! Can I get an autograph please?"
mc "Err, sure baby."
hide danaguard02
show danaguard03
with dissolve
da "Thank you sssoo much, \"[name] the Grabber\"... Now I need to return the FAVOR."
play sound "Sounds/zipper.mp3"
mc "Errr, what... What are you doing?"
da "Returning the favor, \"[name] the Grabber\"! By sucking on your great big whopper! You don't mind, do you?"
scene fbi03 with dissolve
mc "N..No, of course not, I'm getting ROCKHARD for you, baby!"
scene fbibackground03
show danaguard04 
with dissolve
play sound "v08/wow.mp3"
da "Wow, \"[name] the Grabber\", your cock is HUGE! I just want to SUCK on it until you BLOW YOUR LOAD FOR ME!"
scene fbi04 with dissolve
mc "Oh fuck, this is amazing, I can mentally feel her lips on my dong, Agent Dana!"
scene fbibackground04 blurred
show danaguard05 
with dissolve
da "What about my tongue piercings? Does they feel good twirling all over your fist-sized helmet?"
hide danaguard05 
show danaguard06 
with fastdissolve
play sound "Sounds/lick.mp3"
mc "Oh God, oh God, this is incredible!"
hide danaguard06 
show danaguard05 
with fastdissolve
da "I should really let them SLIDE all over your sensitive glans..."
hide danaguard05 
show danaguard06 
with fastdissolve
play sound "Sounds/lick.mp3"
mc "Oh please, just... If you keep th.."
scene fbibackground03
show danaguard07
with dissolve
mc "I can't feel her mouth on my knobhead! Sssooo good!"
label DanaSuckSlow:
scene fbibackground03 blurred
play channel1 "Sounds/hardsucking.mp3"
play channel2 "Sounds/boymoan02.mp3"
hide danablowfast
show danablowslow
call screen danablowslow01
screen danablowslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DanaSuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DanaSuckFast") 

label DanaSuckFast:
mc "Aaah, those sucking lips, and that tongue piercing, OOOOH!"
hide danablowslow
show danablowfast
call screen danablowfast01
screen danablowfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DanaSuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DanaSuckSlow") 

label DanaSuckEnd:
mc "Oh fuck yeah, I'm gonna cum!"
stop channel1
stop channel2
hide danablowslow
hide danablowfast
show danapostblow01
with dissolve
da "No you're not, you're DEAD now!"
mc "Wh...What???"
da "Supreme White House guards have poisoned tongue piercings, so you just FAILED your infiltration!"
scene fbi05 with dissolve
mc "AAAH, I'm still GONNA CUM, GODAMMIT! Not gonna waste a hardon, RHAAA!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene fbibackground02
show danapostblow02 at centerright
with dissolve
da "Oh my God, you are sssooo totally not ready yet! Stop spewing your filthy virtual spunk all over me, Subject 42, you sexual pervert!"
window hide
show fox03 at farleft with moveinleft
fo "Should I virtually eliminate him, Agent Dana? By commiting suicide on him?"
da "Yes, Agent Fox, send him back up the Deep State rabbit-hole... This test was a TOTAL FAILURE... *sigh*"
hide fox03
show fox05 at left
with fastdissolve
play sound "Sounds/gun.mp3"
fo "You are TERMINATED!"
stop sound
scene fbi06 with dissolve
mc "You just shot me! I'm gonna d..."
show screen mcstats
show screen calendar
scene fbibackground01
show fox02 at left
show dana01 at right
with fade
mc "I... So am I dead? Like, for real?"
hide dana01
show dana04a at right
with fastdissolve
da "No, you're not dead for REAL. But you would have been had you embarked on your mission without proper FBI training."
call MCInjury
$ mcinjuredfbi = True
mc "Hey! Then why am I INJURED FOR REAL then?"
hide fox02
show fox04 at left
with fastdissolve
fo "Post-traumatic mental projection. Your mind is just not strong enough. You actually BELIEVED I shot you, so your body injured itself accordingly."
hide dana04a
show dana01 at right
with fastdissolve
da "You're gonna need to come back here for further assessment, [name]. We can't let you infiltrate the Supreme White House in such an inferior mental state."
mc "Err, Ok, I mean, it's not my fault, you jumped on my cock, remember?"
da "*sigh* And that was EXACTLY what you were supposed to RESIST. Do you get it now, [name]?"
mc "I think I do. So I need more virtual training, uh?"
hide dana01
show dana02 at right
with fastdissolve
da "That's correct. Assessment and training is always ongoing at the FBI!"
mc "Doesn't that imply that FBI agents are always undertrained?"
hide dana02
show dana11 at right
with fastdissolve
da "Just GET OUT HERE NOW!"
if withbe:
    scene fbifar01
    show bellaoutworry
    with dissolve
    be "So, what happened in there? You're injured?"
    mc "Only mentally. Only mentally. Let's go home."
if withpe:
    scene fbifar01
    show pennyout01
    with dissolve    
    pe "So, what happened in there? You're injured?"
    mc "Only mentally. Only mentally. Let's go home."

stop music
$ period += 1
scene command01
show lena01
with fade
le "Ah, there you are. I know where you went. And I know how miserably you failed."
mc "You knew about this all along and you didn't warn me?"
hide lena01
show lena06
with fastdissolve
le "Of course not. The Deep State never tells its agents when they are going to be assessed. You are dismissed. To the medbay since you are mentally so weak that you almost committed virtual suicide." 
mc "Err, yeah. I'll go and see nurse Rachel."
hide lena06 with dissolve
jump Medbay

label BackHex56b:
$ period += 1
scene command01
show lena03
with fade
le "Ah, there you are. How does it feel knowing you totally wasted your time going back to that hex, [name]?"
mc "I feel fine. Don't know about the player though. He should be embarrassed."
hide lena03
show lenapensive
with fastdissolve
le "I'd say. VERY embarrassed. You are dismissed." 
hide lenapensive with dissolve
jump LeaveCommand

label FBISecondTraining:
play sound "v08/doorwoosh.mp3"
si "Identity confirmed. Please enter the building, Subject 42."
stop music
scene fbibackground01
show fox01 at left
with fade
play music "v08/humming.mp3"
fo "All clear. Subject 42 has entered the building. Over."
window hide
hide fox01
show fox02 at left
with fastdissolve
show dana01 at right with moveinright
if mcdeep <= 4:
    da "Welcome back to FBI headquarters, [name]."
if mcdeep == 5:
    da "Welcome back to FBI headquarters, Special Field Agent [name]."
mc "I'm warning you, if there is even the slightest chance I might get injured, I'm out of here."
hide dana01
show dana02 at right
with fastdissolve
da "The FBI takes its training very seriously, you have nothing to fear from us, remember?"
mc "Let me check first if you've made any changes in this freaky place."
hide dana02
show dana04a at right
with fastdissolve
da "Sure, come forward and have a look around [name]..."
hide fox02
hide dana04a
show dana04b at right
show fox03 at farleft02
with dissolve
da "There, as you can see, nothing here is dangerous. For your body..."
window hide
play sound "v08/penclick.mp3"
$ renpy.pause(0.5, hard='True')
hide dana04b
show dana05 at right
with fastdissolve
mc "Hey! What was that? You... pricked me with your pen again!"
da "Oh, I am so clumsy, sorry... How are you feeling, [name]?"
hide dana05
show dana06 at right
with fastdissolve
mc "I... feel weak and... *yawn* ...sleepy all of a sudden... I've been had. It's going to happen again isn't it?"
da "Yes, it will. Your assessment starts NOW. You'd better go and sit in the chair until the drugs wear off..."
mc "You bast..."
stop music
hide screen mcstats
hide screen calendar
scene fbi01 with fade
fo "Subject 42. SUBJECT 42! WAKE UP! Activate Google mental goggles, Siri."
scene fbi02 with dissolve
mc "Uh? What's going on this time?"
play sound "Sounds/interfacestart.mp3"
scene fbibackground02
show dana07a at right
with dissolve
if mcdeep <= 4:
    da "It's me, Agent Dana. In a bra again, since you just can't help yourself apparently... Are you ready for your second assessment, [name]?"
if mcdeep == 5:
    da "It's me, Agent Dana. In a bra again, since you just can't help yourself apparently... Are you ready for your second assessment, Special Field Agent [name]?"
mc "Do I have a choice?"
hide dana07a
show dana20 at right
with fastdissolve
da "Not really."
mc "Then I'm READY. Throw it at me, I know it's all FAKE anyway!"
hide dana20
show dana21 at right
with fastdissolve
da "We'll see about that. I'd like to introduce you to the president's most ardent defender."
window hide
show kimfbi02 at left with moveinleft
da "Kimberly Guilfool! She is totally devoted to him and will NEVER flinch in her support."
kg "PRAISE BE TO DONALD TRUMPF, MAY HE REIGN SUPREME FOR A THOUSAND YEARS!"
mc "Noooo, not HER! This is mental TORTURE!"
hide dana21
show dana22 at right
with fastdissolve
da "Kimberly Guilfool will be your most formidable oppponent inside the Supreme White House so listen carefully."
hide kimfbi02
show kimfbi01 at left 
with fastdissolve
kg "WHEN I'M ANGRY, I AM INVINCIBLE! I HAVE BEEN BLESSED BY OUR GREAT LEADER PRESIDENT-FOR-LIFE DONALD TRUMPF!"
mc "Make her stop, I beg you Agent Dana!"
hide dana22
show dana10 at right
with fastdissolve
da "LISTEN! She will use her pussy to subdue and break you. Can you take it?"
mc "Pfff, yeah sure, I can DESTROY any pussy I want!"
hide dana10
show dana23 at right
with fastdissolve
da "Our informers tell us that her pussy is like a titanium clamp due to EXTREME radiation exposure."
da "She has KILLED over two dozen agents by fucking them to DEATH, do you understand?"
hide kimfbi01
show kimfbi03 at farleft 
with fastdissolve
kg "THE BEST HAS PASSED AND BETTER STILL IS YET TO COME!"
mc "Are you sure she didn't just yell at them to death?"
hide dana23
show dana22 at right
with fastdissolve
da "Yes, I am SURE! I'll leave you with her now, try and get out of this virtual-event simulation ALIVE!" 
window hide
hide dana22 with moveoutright
hide kimfbi03
show kimfbi01
with dissolve
kg "YOU...SHALL...NOT...PASS!"
mc "Err... Are you my guide for the visit? Where's the toilet?"
hide kimfbi01
show kimfbi04 
with fastdissolve
kg "Now you're making me ANGRY!"
play sound "Sounds/ripping.mp3"
hide kimfbi04
show kimfbi05 
with dissolve
kg "VERY ANGRY!"
hide kimfbi05
show kimfbi06
with dissolve
kg "SUPREMELY ANGRY!"
mc "Oh fuck..."
hide kimfbi06
show kimfbi07
with dissolve
kg "YOU SEE THIS CLIT? IT WILL GRIP YOUR COCK TO DEATH!"
mc "Hang on a minute, this is MENTAL RAPE!"
scene fbibackground02 blurred
show kimfbi08
with dissolve
play sound "Sounds/hulkgrowl01.mp3"
kg "SHUT UP AND FUCK ME!"
mc "Right, right, sure will do Kimberly, just please stop yelling at me!"
play channel1 "Sounds/debrasex.mp3"
hide kimfbi08
show kimfbianim
with fastdissolve
call screen kimfbianim01
screen kimfbianim01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KimberlyFBIEnd01")

label KimberlyFBIEnd01:
play channel2 "v08/humming.mp3"
scene fbi10 with dissolve
mc "AAAH! My cock, it HURTS!"
da "FIGHT THE PAIN, [name], you MUST!"
stop channel2
scene fbibackground02 blurred
show kimfbianim
with dissolve
call screen kimfbianim02
screen kimfbianim02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KimberlyFBIEnd02")

label KimberlyFBIEnd02:
play channel2 "v08/humming.mp3"
scene fbi11 with dissolve
mc "I'm... trying to cum... But I CAN'T! AAAH"
fo "Your best course of action is to FORCE the cum out of your cumslit, despite the TREMENDOUS PAIN!"
mc "My... spermtube is... TOO CONSTRICTED!"
call MCInjury
$ mcinjuredcock = True
da "You can DO IT! BLAST THAT SPUNK INSIDE THIS VILE WOMAN!"
mc "NOOOO! I CAN'T! TOO MUCH P..."
stop channel2
stop channel1
show fbi11 with hpunch
show screen mcstats
show screen calendar
$ exploredhex56second = True
scene fbibackground01
show fox02 at left
show dana01 at right
with fade
mc "Wh... What happened?"
da "You passed out from the pain. The test was a total failure. On your part."
fo "It sure LOOKED painful. Never see a cock that... twirled up. Except on a pig."
mc "Yeah, thanks for reminding me, I am in TREMENDOUS pain because of you crazy guys! Do you even have a medbay around here, I need URGENT care!"
hide fox02
show fox04 at left
with fastdissolve
fo "No. Why would we need one?"
mc "Cos you keep INJURING people through mental torture, that's why!"
hide dana01
show dana04a at right
with fastdissolve
da "Properly trained agents don't get injured..."
hide dana04a
show dana03 at right
with fastdissolve
if mcstrength <= 15 and mcmaxstrength == False:
    da "We checked your stats on our statometer and your strength is just not high enough to withstand the amount of pussy pressure Kimberly can apply on your cock I'm afraid..."
    mc "Well, can't I just, like, NOT have sex with her?"
    fo "Agents have tried. And died. You WILL meet her inside the Supreme White House. So you must be prepared to sustain EXTREME COCK PAIN."
    hide dana03
    show dana02 at right
    with fastdissolve
    da "Come back again. After you've increased your strength sufficiently. Another session should allow you to be ready to face her on your infiltration mission."
    if mcstrength == 15:
        mc "And how am I supposed to increase my strength exactly? I'm already MAXED OUT on MY stat screen!"
        hide fox04
        show fox01 at left
        with fastdissolve
        fo "Our studies indicate that chopping down trees is the most MANLY activity there is. Try and find a forest somewhere and get on with the work."
        hide dana02
        show dana01 at right
        with fastdissolve
        da "This is it for today, you may leave, we have other agents to train..."
        mc "Right, ooh, sorry for taking up your PRE-CIOUS time while you torture my cock!"
        hide fox01
        show fox04 at left
        with fastdissolve
        fo "Sarcasm won't work on us. We are FBI agents. You know the way out."
    if mcstrength <= 14: 
        mc "Good thing there's a gym in my compound. I'll just train some more and reach my MAX STRENGTH of 15 then! Piece of cake."
        hide dana02
        show dana03 at right
        with fastdissolve
        da "Not so fast. This won't be enough. According to our statometer, you would need strength of at least 16 to survive Kimberly's pussy."
        mc "And how am I supposed to increase my strength past my MAX STRENGTH exactly???"
        hide fox04
        show fox01 at left
        with fastdissolve
        fo "Our studies indicate that chopping down trees is the most MANLY activity there is. Try and find a forest somewhere and get on with the work."
        hide dana03
        show dana01 at right
        with fastdissolve
        da "This is it for today, you may leave, we have other agents to train..."
        mc "Right, ooh, sorry for taking up your PRE-CIOUS time while you torture my cock!"
        hide fox01
        show fox04 at left
        with fastdissolve
        fo "Sarcasm won't work on us. We are FBI agents. You know the way out."
    jump BackHex56c
        
if mcmaxstrength:
    da "We checked your stats on our statometer and your strength is just about high enough to withstand the amount of pussy pressure Kimberly can apply on your cock I'm afraid..."
    fo "That's why you escaped this preliminary trial ALIVE."
    mc "PRELIMINARY? What is that supposed to mean?"
    hide dana03
    show dana02 at right
    with fastdissolve
    da "That you have to come back. So we can train you to FIGHT the pain and beat Kimberly Guilfool."
    hide fox04
    show fox02 at left
    with fastdissolve
    fo "It's the only way. You WILL meet her inside the Supreme White House. So you must be prepared to sustain EXTREME COCK PAIN."
    hide dana02
    show dana01 at right
    with fastdissolve
    da "This is it for today, you may leave, we have other agents to train... But come back again.  Another session should allow to be ready to face her on your infiltration mission."
    mc "Right, ooh, sorry for taking up your PRE-CIOUS time while you torture my cock!"
    hide fox02
    show fox04 at left
    with fastdissolve
    fo "Sarcasm won't work on us. We are FBI agents. You know the way out."
    jump BackHex56c

label BackHex56c:
$ period += 1
scene command01
show lena03
with fade
le "Ah, there you are. I was told about your...err... predicament. In the groin area."
mc "Why don't you tell the whole world about it?"
hide lena03
show lenapensive
with fastdissolve
le "I DID think of doing that. For a laugh. But it would be mean. So go to the medbay and none shall speak of your deformed twisted dong again." 
hide lenapensive with dissolve
jump Medbay
    
label FBIThirdTraining:
play sound "v08/doorwoosh.mp3"
si "Identity confirmed. Please enter the building, Subject 42."
stop music
scene fbibackground01
show fox01 at left
with fade
play music "v08/humming.mp3"
fo "All clear. Subject 42 has entered the building. Over."
window hide
hide fox01
show fox02 at left
with fastdissolve
show dana01 at right with moveinright
if mcdeep <= 4:
    da "Welcome back to FBI headquarters, [name]."
if mcdeep == 5:
    da "Welcome back to FBI headquarters, Special Field Agent [name]."
if mcmaxstrength:
    mc "I'm SUPER-STRONG now, so my cock is like a bar of TITANIUM! No need for your stupid training!"
    hide dana01
    show dana04a at right
    with fastdissolve
    da "That is great to hear! Step in, let me be the first to congratulate you and offer you the FBI Medal of Valor..."
    hide fox02
    hide dana04a
    show dana04b at right
    show fox03 at farleft02
    with dissolve
    mc "Alright, this had better be good."
    da "Sure, just this way please..."
    window hide
    play sound "v08/penclick.mp3"
    $ renpy.pause(0.5, hard='True')
    hide dana04b
    show dana05 at right
    with fastdissolve
    mc "Hey! What was that? Noooo, not again!"
    hide dana05
    show dana06
    with fastdissolve
    da "You still need one more training [name], one more tr..."
    jump LastTraining
if mcmaxstrength == False:
    mc "I'm not at MAX strength yet, so it's totally pointless for me to be here for this assessment. So why don't we have some SAY-AY-XY fun instead, Agent Dana? Agent Fox here can watch."
    hide dana01
    show dana04a at right
    with fastdissolve
    da "REAL sex with a horse-hung HERO? Well, I'm certainly in, what do you say Agent Fox, should we let him step inside and lead him to the SAY-AY-XY bed? *wink*"
    hide fox02
    show fox03 at farleft
    with fastdissolve
    fo "Err, yeah, sure, I get it, I get it, THAT sexy bed..."
    hide fox03
    hide dana04a
    show dana04b at right
    show fox03 at farleft02
    with dissolve
    mc "Alright, this is going to be EPIC! Where's that SAY-AY-XY bed then?"
    window hide
    play sound "v08/penclick.mp3"
    $ renpy.pause(0.5, hard='True')
    hide dana04b
    show dana05 at right
    with fastdissolve
    mc "Hey! What was that? Noooo, not again!"
    hide dana05
    show dana06
    with fastdissolve
    da "You still need one more training [name], one more tr..."
    jump LastTraining

label LastTraining:
stop music
hide screen mcstats
hide screen calendar
scene fbi01 with fade
fo "Subject 42. SUBJECT 42! WAKE UP! Activate Google mental goggles, Siri."
scene fbi02 with dissolve
mc "Uh? My cock, is it still intact?"
play sound "Sounds/interfacestart.mp3"
scene fbibackground02
show dana07a
with dissolve
da "Your cock is doing just fine [name]. For the time being..."
mc "Phew, that's a relief. Now get me out of here, or I'll..."
hide dana07a
show dana20
with fastdissolve
da "NOT until you PASS the test."
hide dana20
show dana22
with fastdissolve
da "You know the drill, but this time, CONCENTRATE and FOCUS YOUR STRENGTH DOWN TO YOUR DICK!"
window hide
hide dana22 with moveoutright
show kimfbi01 with moveinleft
mc "Hey, please don't leave me alone with h..."
play sound "Sounds/hulkgrowl01.mp3"
kg "YOU ARE AN ENEMY OF THE PEOPLE, PREPARE TO DIE BY PUSSY SMOTHERING!"
mc "AAAAH, HELP!"
window hide
hide kimfbi01
show kimfbi04 
with fastdissolve
kg "I'm getting ANGRY!"
play sound "Sounds/ripping.mp3"
hide kimfbi04
show kimfbi05 
with dissolve
kg "AND ANGRIER!"
hide kimfbi05
show kimfbi07
with dissolve
kg "AND ANGRIEST!"
mc "* Oh shit, oh shit, concentrate [name], concentrate! The life of your prized horsecock depends on it! *"
scene fbibackground02 blurred
show kimfbi08
with dissolve
play sound "Sounds/hulkgrowl01.mp3"
kg "NOW FUCK ME!"
play channel1 "Sounds/debrasex.mp3"
hide kimfbi08
show kimfbianim
with fastdissolve
call screen kimfbianim03
screen kimfbianim03:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KimberlyFBIEnd03")

label KimberlyFBIEnd03:
play channel2 "v08/humming.mp3"
scene fbi10 with dissolve
mc "AAAH! My cock! Must... FIGHT... the... PAIN!"
stop channel2
scene fbibackground02 blurred
show kimfbianim
with dissolve
call screen kimfbianim04
screen kimfbianim04:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KimberlyFBIEnd04")

label KimberlyFBIEnd04:
if mcmaxstrength ==False:
    jump KimberlyFBIEnd02
if mcmaxstrength:
    play channel2 "v08/humming.mp3"
    scene fbi11 with dissolve
    mc "NEED... TO... CUM..."
    da "FOCUS! BELIEVE your cock is STRONGER than her PUSSY!"
    scene fbi12 with dissolve
    mc "YES! AAAAH!"
    window hide
    with fastflash
    da "Well done [name]! Keep going!"
    scene fbi13 with dissolve
    if persistent.cumsoundon:
        play sound "Sounds/cumming.mp3"
    mc "FUCK YEAH, MASSIVE CUMLOAD, RHAAA!"
    scene fbibackground02 blurred
    stop channel2
    stop channel1
    show kimfbi09
    with dissolve
    play channel2 "Sounds/splooge02.mp3"
    kg "WHAT IS HAPPENING? MY PUSSY IS THE STRONGEST PUSSY IN THE WORLD!!!"
    window hide
    with fastflash
    mc "My cock is STRONGER, RHAAA!"
    stop channel2
    play channel2 "v08/humming.mp3"
    scene fbi14 with dissolve
    if persistent.cumsoundon:
        play sound "Sounds/mccum.mp3"    
    mc "NOW I AM BECOME SEX, THE DESTROYER OF CUNTS!!!"
    window hide
    with fastflash
    da "Amazing, you succeeded! Project Man-at-Twat accomplished!"
    stop channel2
    scene fbi15 with fade
    play sound "Sounds/panting.mp3"
    mc "Eeeh... Uuuuh..." 
    da "Agent Fox, go and get the mop..."
    show screen mcstats
    show screen calendar
    scene fbibackground01
    show fox02 at left
    show dana02 at right
    with fade
    mc "I feel... GREAT!"
    da "And you were GREAT indeed!"
    call PlusDeep
    hide fox02
    show fox04 at left
    with fastdissolve    
    fo "Now you are READY to infiltrate the Supreme White House and accomplish the Deep State's goal of..."
    hide dana02
    show dana13 at right
    with fastdissolve
    da "AGENT FOX!"
    hide fox04
    show fox03 at left
    with fastdissolve
    fo "Ah yeah, sorry, hush hush, hey?"
    hide fox03
    hide dana13
    show fox04 at left
    show dana01 at right
    with fastdissolve
    da "You are free to go, Special Infiltration Agent [name]... *wink*"
    mc "Oooh, is that a new title? But I didn't see any icon appearing... Oh, I get it, it's fake. Like everything else here."
    hide dana01
    show dana11 at right
    with fastdissolve
    da "Just get out of here RIGHT NOW!"
    $  exploredhex56third = True
    $ period += 1
    scene command01
    show lena07
    with fade
    le "Ah, there you are. Special Infiltration Agent [name]. *wink*"
    mc "Don't bother with the flattery, I know it's fake. I didn't even get a badge."
    if mcdeep == 5 and deepnickname == False:
        hide lena07
        show lena03
        with fastdissolve
        le "Ah. What about a Deep State nickname instead of a badge? Would that please you?"
        mc "Yes, that would do nicely."
        hide lena03
        show lena06
        with fastdissolve        
        le "I hereby grant you a nickname for our faction. \"[name] the Intruder\"."
        window hide
        show mcdeepnickname at posmission
        $ renpy.pause(2.0, hard=True)
        pause
        hide mcdeepnickname
        $ deepnickname = True
        mc "Alright! Intrusion, here we come!"
        le "You're still dismissed though."
        hide lena06 with dissolve
        jump LeaveCommand
    hide lena07
    show lena03
    with fastdissolve
    le "Oh? I see. Right, I guess you are just dismissed then." 
    hide lena03 with dissolve
    jump LeaveCommand    
        



                                                        