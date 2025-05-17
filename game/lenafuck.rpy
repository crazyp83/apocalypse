label LenaFuck01:
hide screen calendar
hide screen mcstats
scene bedroom01
show lena01
with fade
$ d2lenaharem=renpy.random.randint(1,2)
if d2lenaharem == 1:
    $ alienfuck = True
    $ weekfuckedlena = True
    le "I'm still your Chief even if I am your harem girl now. Remember that."
    mc "I will, Chief. As long as I can be your daddy tonight! So come on, who's your daddy?"
    hide lena01
    show lena05
    with fastdissolve
    le "*sigh* You are. You're my daddy."
    mc "Woof, woof!"
    menu:
        "Run scene":
            pass
        "Skip scene":
            le "The story of my sex life. Gone in an instant."
            jump LenaEndB
if d2lenaharem == 2:
    le "I'm guessing you called me to fulfill your duty as harem master?"
    if jakecuck == False:
        mc "That's right! Get undressed and..."
        hide lena01
        show lena03
        with fastdissolve
        le "...Not tonight. I am still married to Jake and err... tonight, I'll be spending the night with him, I promised him. And I did make marital vows. At one stage."
        mc "Ah, shoo. I was already sporting a massive hardon in anticipation, what a let down."
        hide lena03
        show lena06
        with fastdissolve
        le "Notwithstanding the fact that it's probably too late for you to call another girl. You'll sleep alone tonight I'm afraid [name]. Good night."
        hide lena06 with dissolve
        if persistent.tipson:
            show jaketip at tips with dissolve
            pause
            hide jaketip
        jump MCsleep
    if jakecuck:
        $ alienfuck = True
        $ weekfuckedlena = True
        mc "That's correct!"
        hide lena01
        show lena03
        with fastdissolve
        le "Tonight, I'm supposed to be with Jake though..."
        menu:
            "Well, call the cuckboy then! (Humiliation scene for Jake, -1 Friendship Jake)":
                hide lena03
                show lena06
                with fastdissolve
                le "I see. You want to humiliate my darling husband by fucking me in front of him?"
                mc "You said it, baby!"
                hide lena06
                show lena07
                with fastdissolve
                le "Well, he IS a cuckboy and he DOES deserve what's coming to him. Let me go and fetch him for you..."
                hide lena07 with dissolve
                jump LenaCuck
            "I wouldn't want to ruin his marital sex life... (+1 Friendship Jake)":
                hide lena03
                show lena06
                with fastdissolve
                le "Well, that's thoughtful of you... I guess I'll be gone then. To have sex with my small-dicked husband. *sigh*."
                mc "Don't forget to tell him I ALLOWED him to have sex with you tonight."
                call FriendPlusJake
                hide lena06 with dissolve
                mc "Unfortunately, it's now too late for me to call another girl. I guess I'll be sleeping alone tonight then..."
                jump MCsleep

label LenaLingerie:
play channel1 "v07/datemusic.mp3"
scene bedroom02 with fade
show lenalingerie01 at center with moveinright
le "So, it's just the two of us tonight. That's why I'm wearing this especially seductive lingerie set. For you."
mc "It is my honor as...err... your harem master, to be...err..."
hide lenalingerie01
show lenalingerie02
with fastdissolve
le "...Just shut up and enjoy the show, [name]."
mc "Roger that, Chief!"
hide lenalingerie02
show lenalingerie03
with fastdissolve
le "I suppose you want to see the back too?"
hide lenalingerie03
show lenalingerie04
with fastdissolve
mc "Yeah... I always zoom in on the back for some reason..."
scene bedroom02 blurred
show lenalingerie05
with fastdissolve
le "That's enough. For now. I want to see YOU strip for me now... In that posing pouch I gave you."
scene bedroom02
show lenamclingerie01
with dissolve
mc "Here I am!"
le "Ooh, you're so... MANLY! Flex those biceps for me, Daddy..."
hide lenamclingerie01
show lenamclingerie02
with dissolve
mc "Anything for my muscle-loving harem girls!"
le "You're making me so horny, let me feel those boulders..."
scene bedroom13 blurred
show lenamclingerie03
with dissolve
le "Wow, you're getting ssooo HUGE! They must be over 25 inches around at LEAST!"
mc "Yeah, 26 inches last time I checked, Lena!"
play sound "Sounds/moaning.mp3"
hide lenamclingerie03
show lenamclingerie04
with dissolve
le "And those abs... I can't wait to feel their awesome STRENGTH when you POWERFUCK me!"
mc "Oh, I'll POWERFUCK alright, Lena! I'll pound you into the bed!"
hide lenamclingerie04
show lenamclingerie05
with dissolve
le "Please get out of your jock and show me your prodigious teenage fuckmeat, [name]!"
mc "Good timing, I was getting hard. And my jock can't contain my dong when it's FULLY ENGORGED!"
hide lenamclingerie05
show lenamclingerie06
with dissolve
play sound "Sounds/lick.mp3"
le "Let me worship it first, Daddy... It's so virile, it deserves to be worshipped, even by married women such as myself!"
mc "I guess Jake can't compete with me down there, hey?"
le "No, he's tiny. As in WAY TOO SMALL FOR ME!"
if jakemission == False:
    mc "Well, maybe we should find a way of getting him to participate, get my drift?"
    le "You want to let him know he's being cucked?"
    mc "That's right. He deserves to know HIS PLACE, don't you think?"
    le "I guess so. Daddy. He should know you're my Daddy, and not him anymore! But we need to dress him up for the occasion... Try and find some huliating garment for him to wear."
    window hide
    show missionjake at posmission
    $ renpy.pause(4.0, hard=True)
    hide missionjake
    $ jakemission = True
    le "And now that your new quest has started, let me get back to worshipping that MEGADONG of yours!"
hide lenamclingerie06
show lenamclingerie07
with dissolve
play sound "Sounds/lick.mp3"
le "Mmmh, I could lick this tasty rod all night long!"
mc "But I have other plans for you, Lena, so stop licking and start gobbling!"
le "Of course Daddy!"
hide lenamclingerie07
show lenamclingerie08
with fastdissolve
play channel2 "Sounds/hardsucking.mp3"
mc "Yeah, that's good, try and get more inches into your warm mouth!"
hide lenamclingerie08
show lenamclingerie09
with fastdissolve
mc "Damn, Lena, you're a real pro at sucking BIG COCKS!"
hide lenamclingerie09
show lenamclingerie10
with fastdissolve
stop channel2
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "I'm cumming down your throat, AAAHH!"
window hide
with fastflash
le "Glub.... *swallow*"
scene bedroom50 blurred
show lenamclingerie11
with dissolve
play sound "Sounds/panting.mp3"
le "I want to coax MANY more loads out of your donkey-dick tonight.... Are you up for it, Daddy?"
mc "Of course, just hop on the bed and I'll join you with a massive hardon in no time!"
stop channel1
jump LenaFuckChoiceB

label LenaCuck:
play music "v07/datemusic.mp3"
scene bedroom02 with fade
show lenalingerie01 at right with moveinright
le "I'm back [name]! In sexy lingerie. For YOU."
window hide
show jakecuck01 at farleft with moveinleft
hide lenalingerie01
show lenajakelingerie01 at right
with fastdissolve
le "And look who I brought. My darling hubby!"
if jakeknowsharem:
    ja "Are you going to fuck him in front of me again?"
    le "That's right, and there's nothing you can do about it."
if jakeknowsharem == False:
    ja "Why are we here Lena? And why is this boy standing there in a see-thru jockstrap?!?!"
    le "That's [name], I'm in his harem now, and there's nothing you can do about it."
    $ jakeknowsharem == True

le "Come over here [name], and show Jake how to treat a woman... And make her lustful for a heavy session of PURE RAW SEX."
hide jakecuck01
hide lenajakelingerie01
show lenajakelingerie02 at right
show jakecuck02 at farleft
with dissolve
play sound "Sounds/moaning.mp3"
le "Mmmh, yes, slowly peel my bra off..."  
hide lenajakelingerie02
show lenajakelingerie03 at right
with dissolve  
play sound "Sounds/kiss.mp3"
le "Mmmh, your body is so manly... And what do I feel between my legs? Is that your GIANT hardening dong?"
ja "Please stop talking about his thing like that Lena..."
le "Well, I'm sorry hubby but it's simply COLOSSAL. Especially compared to your puny dick."
mc "Do you want to see it up close and personal Chief?"
le "Ooh, yes DADDY!"
ja "But... I'm supposed to be your daddy..."
scene bedroom03 blurred
show lenacuck02
with dissolve  
play sound "Sounds/kiss.mp3"
le "Look at that MONSTER, Jake!"
mc "Hey, little man, wy don't you get down on your knees and start licking Lena's asshole. You've got to make it nice and slick for me..."
ja "But..." 
le "Just OBEY the MASTER, Jake! Or you'll never get anywhere near me EVER AGAIN!"
scene bedroom02 blurred
show lenacuck01
with dissolve  
play sound "Sounds/lick.mp3"
mc "How's the view from there, Jake? Are you sticking your tongue deep enough in there?"
scene bedroom38 blurred
show lenacuck03
with dissolve
ja "I....hope I've done a good job for you Master..."
le "You were VERY good, hubby! I think you deserve a little reward. I'll get you off with my fingers. Come over here."

scene bedroom02 blurred
show jakepreblow01
with dissolve
le "While I jerk cuckboy off, I'm definitely going to have to taste THIS appetizing cock!"
mc "Be my guest, Lena!"
scene bedroom03 blurred
play channel1 "Sounds/hardsucking.mp3"
play channel2 "Sounds/wank.mp3"
label JakeBlowSlow:
hide jakeblowfast
show jakeblowslow
call screen jakeblowslow01
screen jakeblowslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("JakeBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("JakeBlowFast") 

label JakeBlowFast:
mc "Damn that mouth was made to suck huge cocks. Just like in my dreams..."
hide jakeblowslow
show jakeblowfast
call screen jakeblowfast01
screen jakeblowfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("JakeBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("JakeBlowSlow") 

label JakeBlowEnd:    
ja "Lena, I don't think I can hold off much longer if you keep doing that..."
stop channel1
stop channel2
hide jakeblowslow
hide jakeblowfast
show jakecuckblowcum01
with dissolve
le "What about you [name], are you ready to pop too?"
mc "I... Almost there..."
hide jakecuckblowcum01
show jakecuckblowcum02
with fastdissolve
ja "AAAH, I'm CUMMMING!"
le "You call this pathetic drop \"cumming\"??? Show him how a TRUE STALLION comes [name]!"
hide jakecuckblowcum02
show jakecuckblowcum03
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Sure Chief, here comes the sauce, AAAAHHHH!"
window hide
with fastflash
le "See that hubby? that's what I'm talking about!"
hide jakecuckblowcum03
show jakecuckblowcum04
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
le "His shots are so LONG and MASSIVE!"
window hide
with fastflash
ja "He's dousing me, this is disgusting!"
window hide
with fastflash
mc "FUCK, YEAH? RHAAA!"
with fastflash
le "Take it like a beta-sub Jake, it's not his fault if his cumshots are so POWERFUL!"
hide jakecuckblowcum04
show jakecuckblowcum05
with fastdissolve
play sound "Sounds/lick.mp3"
le "Ssssooo tasty too, nothing like Jake's foul-smelling beta-cum..."
ja "I... I'm covered in his filthy spunk!"
play sound "Sounds/lick.mp3"
mc "Then get cleaned up cos I'm not done with your wife. By a LONG SHOT. Long shot, got it?"
if jakefriend <= 0:
    ja "I'll... get you for that [name]! Our friendship is OVER!"
if jakefriend >= 1:
    ja "How could you do this to me [name]? I thought we were friends!"
    call FriendMinusJake
le "Come on hubby, you wanted this, remember? Now get on the bed and start licking my pussy for the night's events."
jump LenaFuckChoiceA

label LenaFuckChoiceA:
scene bedroom03b blurred
show lenabed02
with fade
le "So, what do you have planned next for me and cuckboy down there?"
stop music
menu:
    "Let's show him what a REAL MAN'S COCK can do...":
        le "You're going to pound your MASSIVE pole into me, [name]?"
        mc "Damn right! And Jake will watch from the sideline."
        le " Don't worry hubby, I'll let you lick his creamy offering from my overstuffed pussy after he's done..."
        ja "But... I don't want to lick his cum, that's disgusting!"
        jump LenaFuck
    "I want to drill that tight ass of yours, Chief!":
        le "Did you hear that, hubby? I don't remember the last time I let you ass-fuck me..."
        ja "So why are you letting HIM do it then?"
        le "Because he's got a monstercock, that's why."        
        jump LenaAss
    "How about we DP you. Small-dick here obviously takes your ass.":
        le "That's very kinky. Too bad it won't be with TWO big cocks but yours is so big, it will be sufficient."
        ja "So... I get to fuck your ass, Lena?"
        le "As a reward for being a good cuckboy. Obviously, I won't feel a thing with [name]'s monstercock stuffed in my pussy."
        jump LenaDP
    "I'm done. But my bed is not big enough for the three of us...":
        le "I'm sorry Jake, but that means you'll have to sleep on the floor."  
        mc "Like a good little doggy."
        jump LenaEndA

label LenaFuck:
scene jakeprecuck01 with dissolve
mc "See that dong, Jake? That's why your wife is in my harem..."
ja "It's not fair, how can I compete with THAT thing?"
le "You simply can't, hubby. You'll just have to watch this stallion STRETCH my hole and pray I can even feel your puny dick afer such a massive pounding!"
scene jakeprecuck02 with dissolve
mc "Let's see if it fits first. It does. Your wife was made to take HUGE COCKS up there."
le "YES! Only YOUR cock, Harem Master! Now fuck me please, FUCK ME HARD IN FRONT OF MY CUCKOLD HUSBAND!"
play music "Sounds/womansex02.mp3"
label LenaJakeSlow:
hide jakecuckfast
hide jakecuckpovslow
hide jakecuckpovfast
show jakecuckslow
call screen jakecuckslow01
screen jakecuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaJakeEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaJakeFast") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("LenaJakePOVSlow") 

label LenaJakePOVSlow:
hide jakecuckslow
hide jakecuckfast
hide jakecuckpovfast
show jakecuckpovslow
call screen jakecuckpovslow01
screen jakecuckpovslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaJakeEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaJakePOVFast") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("LenaJakeSlow") 

label LenaJakeFast:
hide jakecuckslow
hide jakecuckpovslow
hide jakecuckpovfast
show jakecuckfast
call screen jakecuckfast01
screen jakecuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaJakeEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LenaJakeSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("LenaJakePOVFast") 

label LenaJakePOVFast:
hide jakecuckslow
hide jakecuckfast
hide jakecuckpovslow
show jakecuckpovfast
call screen jakecuckpovfast01
screen jakecuckpovfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaJakeEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("LenaJakePOVSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("LenaJakeFast") 
            
label LenaJakeEnd:
le "Are you going to cum for me, DAddy?"
ja "Please Lena, don't..."
stop music
scene jakecuckcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "AAAH, CUMMMING INSIDE YOUR PUSSY!"
window hide
with fastflash
mc "NOW IT BELONGS TO ME, RHAAA!"
scene jakecuckcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
le "Yes, it does! Look with how MUCH cum he's stuffing my fuckhole, hubby!"
window hide
with fastflash
le "You can't even come that much in A YEAR!"
scene jakecuckcum03 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Now I'm gonna cover you in my spunk and claim your body as MINE!"
window hide
with fastflash
le "Do it [name], BLAST that young virile seed all over me!"
ja "This is disgusting, how are we going to clean this up?"
window hide
with fastflash
mc "That's YOUR job, cuckhold! AAAH, here are some more shots for you to lick up!"
scene jakecuckcum04 with dissolve
play sound "Sounds/lick.mp3"
le "That's good hubby, lick my abs clean of this boy's nasty spunk... Oooh..."
mc "And don't forget her pussy once you're done up there."
le "Yes, it's really OVERFILLED. And LEAKING so much cum, you've got to make sure it's spotless for us, Jake!"
scene jakecuckcum05 with dissolve
play sound "Sounds/lick.mp3"
mc "There you go, you seem to be enjoying this after all, aren't you Jake?"
play sound "Sounds/lick.mp3"
ja "Y...Yes,, thank you Harem Master. For letting me slurp your sperm out of my wife's pussy..."
play sound "Sounds/lick.mp3"
le "I think I'm clean enough now for you to FUCK ME SOME MORE [name], what do you say?"
mc "My still-rockhard cock nods in approval, Lena!"
jump LenaFuckChoiceA

label LenaAss:
scene lenapreass01 with dissolve
mc "Are you ready to take my big cock up your ass, Chief?"
le "On second thoughts, it looks just sssooo HUGE..."
mc "Maybe we should ask Jake what he thinks..."
scene bedroom49 blurred
show lenapreass02
with dissolve
ja "This is nuts, it will never fit! You're going to DESTROY my wife!"
le "I don't care about YOUR opinion. That's it, I'm ready, FUCK THE SHIT OUT OF ME, [name]! Jake, guide my Harem Master's stud cock into my fuckhole!"
ja "What??? But..."
le "Do as you're told, CUCKBOY!"
scene lenapreass03 with dissolve
play sound "Sounds/moaning.mp3"
le "Ooh, yeah! His cock is so THICK! Can you feel it too, Jake?"
ja "Y... Yeah... My hand can't get around its girth..."
mc "That's it, stop touching my dong gayboy, and just watch from the sidelines as I pound your wife's tight backdoor!"
le "And I'll make sure he has a nice view!"
scene bedroom49 blurred
play music "Sounds/womansex02.mp3"
label LenaAssSlow:
hide lenaassfast
show lenaassslow
call screen lenaassslow01
screen lenaassslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaAssEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaAssFast") 

label LenaAssFast:
mc "Who's your ass-daddy, hey? Who's your ass-daddy?"
le "Oh God, you are, YOU ARE! Fuck me FASTER!"
hide lenaassslow
show lenaassfast
call screen lenaassfast01
screen lenaassfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaAssEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LenaAssSlow") 

label LenaAssEnd:
le "Are you seeing how his throbbing cock is pummelling my ass, Jake?"
ja "I... I don't want to watch but..."
mc "Cuckboy here has a hardon I bet..."
le "Yeah, a 3-inch dicklet hardon!"
ja "Please Lena, stop humiliating me like this in front of this boy!"
stop music
play music "Sounds/splooge02.mp3"
hide lenaassslow
hide lenaassfast
show lenaasscum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "How's that for TOTAL HUMILIATION JAKE? RHAAA! I'm dumping my load in your wife's backdoor!"
window hide
with fastflash
le "There's so much of his young spunk ERUPTING inside me hubby! At least a year's worth of supply from your little pindick!"
hide lenaasscum01
show lenaasscum02
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "And I'm not done yet, by a long shot! AAAH!"
window hide
with fastflash
le "Watch this boy's giant pole ravage your wife's rosebud! Watch and learn how it's done, Jake! Oooh, I'm cumming too!"
stop music
stop sound
hide lenaasscum02
show lenaasscum03
with dissolve
play sound "Sounds/panting.mp3"
ja "Please stop it Lena, I'll do anything for you if just stop th..."
le "Shushh honey, I don't want to hear another word fr..."
scene lenaassagain00 with dissolve
play sound "Sounds/gasp.mp3"
le "...Eeek! He just... plunged his tool into me sssooo DEEP!"
mc "I'm not done with you, Chief! More ass-drilling coming your way!"
play music "Sounds/womansex01.mp3"
label LenaAssAgainSlow:
show lenaassagainslow
call screen lenaassagainslow01
screen lenaassagainslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaAssAgainEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaAssAgainFast") 
    imagebutton:
        focus_mask True
        idle "v08/bottomview.png"
        hover "v08/bottomview.png"
        action Jump ("LenaAssBottomSlow") 

label LenaAssAgainFast:
if lenaasssaid == False:
    le "This is incredible! Getting ass-fucked by the biggest dick ever while my hubby watches us and wanks his tiny cock... PLEASE POUND THAT MONSTERCOCK INTO ME FASTER NOW!"
    $ lenaasssaid = True
show lenaassagainfast
call screen lenaassagainfast01
screen lenaassagainfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaAssAgainEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LenaAssAgainSlow") 
    imagebutton:
        focus_mask True
        idle "v08/bottomview.png"
        hover "v08/bottomview.png"
        action Jump ("LenaAssBottomFast") 

label LenaAssBottomSlow:
scene bedroom49 blurred
show lenaassbottomslow
call screen lenaassassslow01
screen lenaassassslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaAssAgainEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaAssBottomFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("LenaAssAgainSlow") 

label LenaAssBottomFast:
if lenaasssaid == False:
    le "This is incredible! Getting ass-fucked by the biggest dick ever while my hubby watches us and wanks his tiny cock... PLEASE POUND THAT MONSTERCOCK INTO ME FASTER NOW!"
    $ lenaasssaid = True
scene bedroom49 blurred
show lenaassbottomfast
call screen lenaassassfast01
screen lenaassassfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaAssAgainEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LenaAssBottomSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("LenaAssAgainFast") 
        
label LenaAssAgainEnd:
mc "I think I'm about to cum again Lena!"
le "Uh, AAAH, OOOH, this is ssooo GOOOD, I'm ALREADY cumming NON-STOP!"
stop music
scene bedroom48 blurred
show lenaassagaincum01
with dissolve
play music "Sounds/splooge01.mp3"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
ja "He's doing it! You're letting this boy pump your ass full again!"
window hide
with fastflash
le "Of course I am, it feels so godam GREAT, AAAH!"
scene lenaassagaincum02 with dissolve
play sound "Sounds/moaning03.ogg"
le "I'm going to squirt, AAAH!"
window hide
with fastflash
mc "Ooh, wow, did you know your wife was such a squirter, Jake?"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
ja "N...No..."
window hide
with fastflash
le "Only with a HUGE COCK PUMPING IN MY ASS!"
scene lenaassagaincum03 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
le "Dear Lord, you're STILL cumming! My body is shaking all over!"
window hide
with fastflash
mc "I think Jake's is cumming a small drop watching us..."
stop music
ja "*groan* UUUH!"
scene lenaassagaincum04 with dissolve
play sound "Sounds/gasp.mp3"
le "This was ssooo INTENSE. And you came TWO MONSTER loads inside my poor ass..."
mc "And guess what? I'm still hard for some MORE hot action!"
$ lenaasssaid = False
jump LenaFuckChoiceA

label LenaDP:
scene lenapredp01 with dissolve
play sound "Sounds/kiss.mp3"
le "So, are you ready for your reward, cuckboy?"
ja "Y...yes, thank you Lena."
mc "And Harem Master. Don't forget about me."
ja "Y...Yes, thank you Harem... Master..."
mc "Good, now let's swap, you've had enough fun with your wife, now it's my turn."
scene lenapredp02 with dissolve 
mc "Thos tittties belong to ME now, don't they Lena?"
le "Of course. Daddy."
scene lenapredp03 with dissolve
play sound "Sounds/kiss.mp3"
mc "Now let's get into position. I'll doggy you and cuckboy can stick all three of his puny inches in your backside."
scene lenadp00 with dissolve
play sound "Sounds/moaning03.ogg"
mc "I feel a little tingling on the top of my cock. Oh, that's Jake little stub."
ja "I...'m weirdly turned on by this humiliation..."
le "Enjoy the feeling while it lasts then hubby, and GET ON WITH THE FUCKING BOTH OF YOU!"
play music "Sounds/womansex02.mp3"
label LenaDPSlow:
hide lenadpfast
show lenadpslow
call screen lenaDPslow01
screen lenaDPslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaDPEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaDPFast") 

label LenaDPFast:
mc "This pussy is so good, cuckboy. But once I'm done with your wife, she won't be able to feel your pindick in there!"
le "I ain't letting him anywhere near my pussy anyway! Except to lick my Harem Master's cum out of it!"
mc "Let's move  faster now Jake, shall we?"
ja "O... Okay."
hide lenadpslow
show lenadpfast
call screen lenaDPfast01
screen lenaDPfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaDPEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LenaDPSlow") 

label LenaDPEnd:
le "It's time for you boys to fill BOTH my holes up with your cream!"
scene lenadpcum01 with dissolve
stop music
play music "Sounds/splooge02.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
window hide
mc "Fuck YEAH! CU-UUU-UUUMING!"
window hide
with fastflash
ja "Me too, aah!"
scene lenadpcum02 with dissolve
le "Keep going boys, fill up my holes with your splooge!"
window hide
with fastflash
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "GODDAMMIT, THIS PUSSY IS SO GOOD, RHAAA!"
scene lenadpcum03 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
le "Mmmh, [name] is still going STRONG, I can feel his MASSIVE cumshots splashing inside me! AAAH, I'm cumming AGAIN!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
window hide
with fastflash
mc "AAAH, still spewing my sauce for you, Lena!"
scene lenadpcum04 with dissolve
stop music
stop sound
play sound "Sounds/panting.mp3"
le "I have sssoo much young cum sloshing around inside my womb... Good thing I'm on birth control, hey hubby?"
mc "I'm not done. Give me a couple of minutes and I'll be ready to go again!"
ja "I... don't think I can get hard again..."
le "No surprise there, you've already outdone yourself tonight with two loads, that's your absolute best in one night, Jake..."
mc "I can go ALL NIGHT!"
le "Good, then let's get back into our starting positions then shall we, hubby?"
ja "I... guess so."
jump LenaFuckChoiceA

label LenaFuckChoiceB:
scene bedroom09 blurred
show lenabed01
with fade
le "What are you going to do to me, Daddy?"
stop music
menu:
    "I've just got to play with those sumptuous tits!":
        le "They're all yours to play with, Daddy!"
        jump LenaTits
    "Get ready for some serious pussy-pounding!":
        le "I can't wait for you to STRETCH my hole!"
        jump LenaSex
    "You've always wanted me to become stronger and stronger. I'll show you how strong I am now!":
        le "Ooh, yes please, let me worship your HUGE muscles, Daddy!"
        jump LenaUp
    "I'm done, let's go to sleep...":
        jump LenaEndB

label LenaTits:
scene lenaprefondle01 with dissolve
mc "Fuck yeah, I've always wanted to fondle those nice titties of yours..."
play music "Sounds/moaning02.mp3"
label LenaFondleSlow:
hide lenafondlefast
show lenafondleslow
call screen lenafondleslow01
screen lenafondleslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaFondleEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaFondleFast") 

label LenaFondleFast:
le "You know your stuff [name]... Your strong hands can be real delicate..."
mc "I always take good care of my girls' most precious assets..."
hide lenafondleslow
show lenafondlefast
call screen lenafondlefast01
screen lenafondlefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaFondleEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LenaFondleSlow") 

label LenaFondleEnd:
stop music
scene lenapostfondle01 with dissolve
le "Now it's my turn to return the favor. I'm gonna titfuck that mega-dong of yours till you EXPLODE young warm seed EVERYWHERE!"
scene lenapostfondle02 with dissolve
le "Your cock likes that... I can feel it hardening between my legs... God, look how FAR it extends in front of me!"
mc "I'm so horny and looking forward to that titfuck you promised me, Lena..."
le "I can see, you're postively LEAKING precum!"
le "Let me wrap my jugs around its tremendous girth then..."        
play channel1 "Sounds/moaning03.ogg"
play channel2 "Sounds/wank.mp3"
label LenaTitsSlow:
hide lenatitscloseslow
hide lenatitsfast
show lenatitsslow
call screen lenatitsslow01
screen lenatitsslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaTitsEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaTitsFast") 
    imagebutton:
        focus_mask True
        idle "v08/bottomview.png"
        hover "v08/bottomview.png"
        action Jump ("LenaTitsPOVSlow") 

label LenaTitsPOVSlow:
hide lenatitsslow
hide lenatitsclosefast
show lenatitscloseslow
call screen lenatitscloseslow01
screen lenatitscloseslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaTitsEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaTitsPOVFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("LenaTitsSlow") 

label LenaTitsFast:
hide lenatitsslow
hide lenatitsclosefast
show lenatitsfast
call screen lenatitsfast01
screen lenatitsfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaTitsEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LenaTitsSlow") 
    imagebutton:
        focus_mask True
        idle "v08/bottomview.png"
        hover "v08/bottomview.png"
        action Jump ("LenaTitsPOVFast") 

label LenaTitsPOVFast:
hide lenatitscloseslow
hide lenatitsfast
show lenatitsclosefast
call screen lenatitsclosefast01
screen lenatitsclosefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaTitsEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("LenaTitsPOVSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("LenaTitsFast") 
            
label LenaTitsEnd:
le "Are you going to release that pent-up semen for me, Daddy? I want an EXTRA-BIG LOAD!"
mc "Oh don't worry Lena, I'll give you..."
stop channel1
stop channel2
scene lenatitscum01a with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "...ONE...CUMMING, AAAH!"
with fastflash
le "Oooh, it's BLASTING so high up in the air, Daddy!"
scene lenatitscum01b with fastdissolve
mc "There you go, Lena, MORE for you, RHAAA!"
with fastflash
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene lenatitscum02 with dissolve
le "How can you CUM SO MUCH?"
with fastflash
le "STILL  MORE????"
scene lenatitscum03 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
le "This is incredible, you're pumping seed like a fire hydrant on full blast!"
with fastflash
mc "RHAAAA, SO FUCKING GOOOOD!"
stop sound
scene lenatitscum04 with dissolve
play sound "Sounds/panting.mp3"
le "Do you even have any cum left in your balls after dumping like, a GALLON of cum all over the place?"
mc "Yeah, don't worry, I replenish quickly. Let's move on to some more FUN!"
jump LenaFuckChoiceB

label LenaSex:
scene lenapresex01 with dissolve
mc "Ready for it, Chief?"
scene lenapresex02 with dissolve
le "Ready for what, Daddy? Your MONSTER COCK that's drooling pre-cum all over the place?"
mc "Yeah, that thing..."
scene lenapresex03 with dissolve
le "I'm ready... My pussy is all wet for you, Daddy!"
mc "Then it's time to stretch it!"
play music "Sounds/barbarasex.mp3"
label LenaSexSlow:
hide lenasexfast
hide lenasexpovslow
show lenasexslow
call screen lenasexslow01
screen lenasexslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaSexEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaSexFast") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("LenaSexPOVSlow") 

label LenaSexPOVSlow:
hide lenasexpovfast
hide lenasexslow
show lenasexpovslow
call screen lenasexcloseslow01
screen lenasexcloseslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaSexEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaSexPOVFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("LenaSexSlow") 

label LenaSexFast:
mc "Gonna pummel that tight pussy of yours even faster, Lena!!"
le "Yes, do that daddy! Drill my fuckhole as deep and fast as you please!"
hide lenasexslow
hide lenasexpovfast
show lenasexfast
call screen lenasexfast01
screen lenasexfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaSexEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LenaSexSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("LenaSexPOVFast") 

label LenaSexPOVFast:
mc "Gonna pummel that tight pussy of yours even faster, Lena!!"
le "Yes, do that daddy! Drill my fuckhole as deep and fast as you please!"
hide lenasexfast
hide lenasexpovslow
show lenasexpovfast
call screen lenasexclosefast01
screen lenasexclosefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaSexEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("LenaSexPOVSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("LenaSexFast") 
            
label LenaSexEnd:
mc "Oh God, the way your pussywalls just WRAP themselves around my shaft..."
le "It makes you want to cum, doesn't it, Daddy? Go on, UNLOAD INSIDE MY CUNTHOLE!"
stop music
scene lenasexcum01 with dissolve
play music "Sounds/moaning.mp3"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "AAAH, fucking nutting like CRAY-AAAYYY-ZYYY!"
window hide
with fastflash
le "You're filling me up with ssoo much cum, DADDY!"
scene lenasexcum02 with dissolve
mc "RHAAA!"
window hide
with fastflash
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Still got more for you! AAAH!"
scene lenasexcum03 with dissolve
stop music
mc "And take the rest of your face and tits, OOOOH!"
window hide
with fastflash
le "You're the BEST, daddy! Cumming so much for me! AAAH!"
scene lenasexcum04 with dissolve
play sound "Sounds/gasp.mp3"
le "Are you okay Daddy? I hope my sweet pussy didn't break your stride..."
mc "You want to fuck some more? I'll show you that I can still FUCK YOU SOME MORE!"
le "Ooh, YES DADDY!"
stop sound
jump LenaFuckChoiceB

label LenaUp:
scene bedroom41 blurred
show lenapreup01
with dissolve
le "Mmmh, what are you doing [name]? You're..."
hide lenapreup01
show lenapreup02
with fastdissolve
mc "Playing with that nice pussy of yours..."
play sound "Sounds/moaning.mp3"
le "Oooh, it's so good, you're going to make me cum already!"
mc "That's the idea. So you're nice and wet for my cock, Lena!"
scene bedroom35 blurred
show lenapreup03a
with fastdissolve
play sound "Sounds/moaning02.mp3"
le "AAAH, I'm gonna squirt Daddy!"
hide lenapreup03a
show lenapreup03b
with fastdissolve
play sound "Sounds/moaning03.ogg"
mc "There you go, let it all out, Lena..."
scene bedroom13 blurred
show lenapreup04
with fastdissolve
le "That was really good... *puff*"
hide lenapreup04
show lenapreup05
with fastdissolve
play sound "Sounds/kiss.mp3"
le "Mmmh, that tireless cock of yours... It's so hard and BIG!"
mc "How could it NOT BE hard in front of such a hot lady?"
hide lenapreup05
show lenapreup06
with fastdissolve
le "How big is it exactly? Tell me please, daddy!"
mc "Seventeen full inches of teenage fuckstick for you, Lena."
play sound "Sounds/moaning.mp3"
le "Lift me up on it, show me its POWER, DADDY!"
hide lenapreup06
show lenapreup07
with fastdissolve
le "Damn it boy, you're ridiculously HUNG! And ssoo muscular to boot... Stick that huge cock in me and FUCK ME!"
play music "Sounds/womansex01.mp3"
scene bedroom13 blurred
label LenaUpSlow:
hide lenaupfast
show lenaupslow
call screen lenaupslow01
screen lenaupslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaUpEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaUpFast") 

label LenaUpFast:
le "Your donkey-dick is splitting me in half, Daddy!"
mc "I'm going balls deep on each stroke, Lena!"
hide lenaupslow
show lenaupfast
call screen lenaupfast01
screen lenaupfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaUpEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LenaUpSlow") 

label LenaUpEnd:
play sound "Sounds/moaning03.ogg"
le "I'm like a ragdoll in your strong muscled arms! I'm gonna CU-UUUMM!"
mc "I'm about to burst a nut too!"
stop music
hide lenaupslow
hide lenaupfast
show lenaupcum01
with dissolve
stop music
play music "Sounds/splooge02.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
le "I can feel your pole shooting its nasty virile sperm inside me, AAAH!"
window hide
with fastflash
mc "Well, feel that shot now, RHAAA!"
scene bedroom41 blurred
show lenaupcum02
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Here comes more splooge for you Lena, RHAAA!"
window hide
with fastflash
le "You're FLOODING ME, I can't hold that much seed in my stretched hole!"
play sound "Sounds/moaning03.ogg"
window hide
with fastflash
scene bedroom49 blurred
show lenaupcum03
with dissolve
stop music
le "I can feel TONS of cum trickling down my legs... You came so much, Daddy!"
mc "You bring out the BEST in me, Chief!"
scene bedroom13 blurred
show lenaupcum04
with dissolve
le "Lie me down on the bed and let me recuperate. Until our next romp!"
jump LenaFuckChoiceB

label LenaEndA:
show screen calendar
show screen mcstats
scene lenasleep02 with fade
$ loc = "bedroom"
play sound "Sounds/snoring.mp3"
pause 3
call NewDay
jump Bedroom

label LenaEndB:
show screen calendar
show screen mcstats
scene lenasleep01 with fade
$ loc = "bedroom"
play sound "Sounds/snoring.mp3"
pause 3
call NewDay
jump Bedroom