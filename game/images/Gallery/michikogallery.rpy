label MichikoGallery:
call screen gallerymichiko
screen gallerymichiko:
    add "Gallery/michikogallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("gallerymichiko"), Jump ("MainGallery")]

    if renpy.seen_image("michikodojo01"):
        imagebutton:
            focus_mask True
            idle "Gallery/michikogallery01.png" xpos 621 ypos 100
            hover "Gallery/michikogallery01.png"
            action Jump ("MichikoGallery01")

    if renpy.seen_image("michikodojo01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("MichikoGallery")

    if renpy.seen_image("michikoroombed"):
        imagebutton:
            focus_mask True
            idle "Gallery/michikogallery02.png" xpos 1050 ypos 100
            hover "Gallery/michikogallery02.png"
            action Jump ("MichikoGallery02")

    if renpy.seen_image("michikoroombed") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("MichikoGallery")

    if renpy.seen_image("michikostrip01"):
        imagebutton:
            focus_mask True
            idle "Gallery/michikogallery03.png" xpos 1478 ypos 100
            hover "Gallery/michikogallery03.png"
            action Jump ("MichikoGallery03")

    if renpy.seen_image("michikostrip01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("MichikoGallery")

    if renpy.seen_image("michikofootjobbackground"):
        imagebutton:
            focus_mask True
            idle "Gallery/michikogallery04.png" xpos 621 ypos 400
            hover "Gallery/michikogallery04.png"
            action Jump ("MichikoGallery04")

    if renpy.seen_image("michikofootjobbackground") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("MichikoGallery")

    if renpy.seen_image("michikolingerie01"):
        imagebutton:
            focus_mask True
            idle "Gallery/michikogallery05.png" xpos 1050 ypos 400
            hover "Gallery/michikogallery05.png"
            action Jump ("MichikoGallery05")

    if renpy.seen_image("michikolingerie01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("MichikoGallery")

    if renpy.seen_image("michikonaked"):
        imagebutton:
            focus_mask True
            idle "Gallery/michikogallery06.png" xpos 1478 ypos 400
            hover "Gallery/michikogallery06.png"
            action Jump ("MichikoGallery06")

    if renpy.seen_image("michikonaked") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("MichikoGallery")
            
    add "Gallery/galleryfuture.png" xpos 621 ypos 700

    add "Gallery/galleryfuture.png" xpos 1048 ypos 700

    add "Gallery/galleryfuture.png" xpos 1478 ypos 700

    add "Gallery/gallerygrid02.png"
    add "Gallery/textmichiko.png"
        

label MichikoGallery01:
scene dojo01
show michikodojo01
mi sidemi "So, are you feeling ready for your very first close combat training session [name]?"
mc sidemc "Yes I am. Muscles are rumbling, fists are flexing, get ready for the beating of your..."
hide michikodojo01
show michikodojo02
with fastdissolve
mi "Kurae!"
hide michikodojo02
show michikodojo03
with fastdissolve
window hide
play sound "Sounds/punch.mp3"
pause 1
hide michikodojo03
scene dojomichiko01 with dissolve
mi sidemi "You were saying?"
mc sidemc "Ggg... Ouch!"
scene dojomichiko02 with dissolve
mi "Oh, I think I hurt you. See? Despite your huge muscles, you were no match against a skilled fighter like me..."
mi "I'm sorry you had to learn the hard way... Does it hurt a lot? Where does it hurt?"
mc "Everywhere!"
scene dojomichiko03 with dissolve
mi "Even there? There does seem to be a great big lump right THERE..."
mc "Yeah, you kicked me right in the nuts!"
mi "I'll take to you the medbay then if you are really hurt...."
mi "But it proves that you clearly need to train A LOT. If you follow three sessions, you will definitely improve under my expert guidance!"
jump MichikoGallery

label MichikoGallery02:
play music "Sounds/michiko.mp3"
scene michikoroom01
show michikoroom01b
mi "I'm so glad you came... for our date."
hide michikoroom01b
show michikoroom01a
with fastdissolve
mi "I have prepared some traditional herbal tea. I hope you like it!"
mc "(I hope there is more to it than just driniking tea...)"
scene michikoroom02
show michikoroom02a
show michikoroomtable
with dissolve
mi "I'm so sorry I beat the crap out of you the other day. It was to train you to become a better fighter for our cause!"
mc "It hurt like hell. You should go easy on me, I'm a noob at fighting."
hide michikoroom02a
hide michikoroomtable
show michikoroom02b
show michikoroomtableb 
mi sidemi "Ooh, I'm so sorry, my poor boy... Here, have some tea, it will give you inner strength. The outer strength, you already have (wink)."
hide michikoroom02b
hide michikoroomtable
show michikoroom02a
show michikoroomtable        
mi sidemi "Do you like my outfit? I wear it only on special occasions..."
mc "I like it a lot. Especially the deep cleavage..."
hide michikoroom02a
hide michikoroomtable
show michikoroom02d
show michikoroomtableb                
mi "Yes, I noticed you OGLING them... That's why I wore it..."
mi "And since you're interested in them, I would like you to help me choose an outfit for my stripping gig."
mc "Alright!"
mi "Don't move, I'll come back wearing something even SEXIER..."
stop music
scene michikoroombed
show michikoroom10
with dissolve
mi "So, what do you think of this outfit?"
mc "Very nice, hugs your curves tightly..."
hide michikoroom10
show michikoroom11
with fastdissolve
mi "Check out the back and tell me what you think..."
mi "You can come closer... this once. To admire my ass."
scene michikoroombed blurred
show michikoroom14
with dissolve
mc "I think I'm getting DIZZY! But it's so TIGHT, it seems hard to take off."
scene michikoroombed
show michikoroom12
with dissolve
mi "Oh, it's not, all I have to do is slowly let the straps fall off..."
hide michikoroom12
show michikoroom13
with fastdissolve
mi "And my huge tits are out in no time!"
mc "I can get my COCK out in no time if you want!"
mi "Not now, let's not ruin this date with sex."
mc "(Damn it.)"
mi "If you want to see MORE, come and visit me in the strip corner next to the bar! *wink*"
hide michikoroom13
show michikoroom10
with fastdissolve
mi "Thank you for accepting my date offer [name], I enjoyed TALKING to you. And being just slightly NAUGHTY."
mc "(I guess I should go back to my bedroom then. And wank myself silly.)"
jump MichikoGallery

label MichikoGallery03:
stop music
play music "Sounds/stripmusic.mp3"
scene michikostriplarge:
        ypos -3.0
        linear 10.0 ypos 0.0
$ renpy.pause(10.0, hard=True)
mi "Ready?"
mc "Hard and ready!"
scene michikostrip01 with dissolve
pause        
scene michikostrip02 with dissolve
pause
scene michikostrip03 with dissolve
pause
scene michikostrip04 with dissolve
pause
scene michikostrip05 with dissolve
pause
scene michikostrip06 with dissolve
pause
scene michikostrip07 with dissolve
pause
scene michikostrip08 with dissolve
pause
scene michikostrip09 with dissolve
pause
scene michikostrip10 with dissolve
pause
stop music
scene strip01
show stripmichiko05 with fastdissolve
mi "Mmh, my backdoor is really dilated now... And it's delicious!"
mc "Please let me have a taste!"
mi "I don't think so. You have to CONTROL yourself to be a good fighter."
jump MichikoGallery

label MichikoGallery04:
scene strip02 blurred
show stripmichiko05
mi "Now that I'm all NAKED... Time for YOU to get naked too and show me that piece of boymeat that's distending your pants to bursting point!"
scene michikoprefootjob with dissolve
mi "Mmmh, I'm gonna have to be VERY flexible to take care of such a monster rod. Get out of the chair and lie down on the floor [name]..."
scene michikofootjobbackground with dissolve
show michikofootjob00
mi "There, my feet are at the base of your giant shaft, ready to travel all the way to the tip... Ready [name]?"
mc "Yeah, I'm ready as can be Michiko!"
play music "Sounds/wank.mp3"
scene michikofootjobbackground
label MichikoFootjobSlowx:
show michikofootjobslow
hide michikofootjobfast
call screen michikofootjobslow01x
screen michikofootjobslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoFootjobEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MichikoFootjobFastx") 

label MichikoFootjobFastx:
mi "Oh, you want me to go faster do you?"
window hide
hide michikofootjobslow
show michikofootjobfast
call screen michikofootjobfast01x
screen michikofootjobfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoFootjobEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MichikoFootjobSlowx") 

label MichikoFootjobEndx:
stop music
scene michikofootjobcumbackground blurred
show michikofootjobcum01
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mi "Oooh, my feet are THAT good [name]? You're cumming like a STALLION all over the place!"
hide michikofootjobcum01
show michikofootjobcum02
mi "Those jets of spunk are flying sssooo HIGH!"
hide michikofootjobcum02
show michikofootjobcum03
mi "And look at you now, your still rock-hard behemoth is still spewing some afterdreads all over your chest and we're both covered in your thick spunk... What a naughty boy you are [name]!"
mc "Why don't you take care of my cock some more then Michiko?"
mi "Tempting but you paid for ONE footjob, not several in a row..."
scene strip01 with dissolve
show stripmichiko05
mi "I hope you enjoyed the show [name]... and the footjob."
mc "I sure did. Even if I have to take a shower now since I'm covered in my own cream..."
jump MichikoGallery

label MichikoGallery05:
play music "v07/datemusic.mp3"
scene bedroom01
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
jump MichikoGallery

label MichikoGallery06:
scene bedroom01 with fade
show michikonaked at center with moveinright
mi "I'm ready to service you [name]. And get pounded as BRUTALLY as I deserve."
label MichikoFuckChoicex:
stop music
menu:
    "Get on your kness and worship my enormous fuckstick Michiko!":
        mi "Yes Master, your giant boymeat is ssooo addictive..."
        jump MichikoPraisex
    "Get on all fours, I'm gonna pound your pussy into oblivion!":
        mi "Oh, FUCK!"
        jump MichikoPoundx  
    "I'm gonna pummel through your cleavage with my giant teenage meat!":
        mi "And cover them with an ENORMOUS load of boycream I hope!"
        jump MichikoTitsx
    "Give me a footjob and make me explode Michiko.":
        mi "My feet are so flexible you'll come in no time [name]..."
        jump MichikoFeetx
    "You're ready to be impregnated. And I'm ready to impregnate you." if renpy.seen_image("michikoprepreg01"):
        mi "I bet that's going to be a BRUTAL breeding. How will you proceed?"
        mc "Breeding by IMPALEMENT!"
        jump MichikoImpregnationx
    "I'm done with this gallery.":
        mi "Thanks for giving me the brutal fucking I deserved [name]..."
        jump MichikoGallery

label MichikoPraisex:
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
label MichikoPraiseSlowx:
hide michikopraisefast
show michikopraiseslow
call screen michikopraiseslow01x
screen michikopraiseslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoPraiseEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MichikoPraiseFastx") 

label MichikoPraiseFastx:
mc "Go faster Michiko, shove my fat cock all the way down your throat!"
hide michikopraiseslow
show michikopraisefast
call screen michikopraisefast01x
screen michikopraisefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoPraiseEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MichikoPraiseSlowx") 

label MichikoPraiseEndx:
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
jump MichikoFuckChoicex
    
label MichikoPoundx:
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
label MichikoPoundSlowx:
hide michikopoundfast
show michikopoundslow
call screen michikopoundslow01x
screen michikopoundslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoPoundEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MichikoPoundFastx") 

label MichikoPoundFastx:
mi "I'm getting POUNDED by your MONSTER ROD! But I want it EVEN HARDER!"
hide michikopoundslow
show michikopoundfast
call screen michikopoundfast01x
screen michikopoundfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoPoundEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MichikoPoundSlowx") 

label MichikoPoundEndx:
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
label MichikoPoundSlow02x:
hide michikorefuckfast
show michikorefuckslow
call screen michikopoundslow02x
screen michikopoundslow02x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoPoundEnd02x")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MichikoPoundFast02x") 

label MichikoPoundFast02x:
mi "FUCK! Your cock is so MASSIVE! Give it to me [name], really POUND IT!"
hide michikorefuckslow
show michikorefuckfast
call screen michikopoundfast02x
screen michikopoundfast02x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoPoundEnd02x")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MichikoPoundSlow02x") 

label MichikoPoundEnd02x:
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
jump MichikoFuckChoicex
    
label MichikoTitsx:
scene bedroom17 with dissolve
show michikopretit01
mi "Damn [name], that cock of yours is a LETHAL weapon... Fuck my tits without mercy with it!"
mc "Will do Michiko, will do..."
scene bedroom18 blurred with dissolve
play music "Sounds/fucksound.mp3"
label MichikoTitSlowx:
hide michikotitfast
show michikotitslow
call screen michikotitslow01x
screen michikotitslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoTitEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MichikoTitFastx") 

label MichikoTitFastx:
mi "Go on, slide it even FASTER between my firm mammaries!"
hide michikotitslow
show michikotitfast
call screen michikotitfast01x
screen michikotitfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoTitEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MichikoTitSlowx") 

label MichikoTitEndx:
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
jump MichikoFuckChoicex

label MichikoFeetx:
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
label MichikoFeetSlowx:
hide michikofeetfast
hide michikofeetpovslow
hide michikofeetpovfast
scene bedroom19 blurred
show michikofeetslow
call screen michikofeetslow01x
screen michikofeetslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoFeetEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MichikoFeetFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("MichikoFeetPOVSlowx") 
        
label MichikoFeetPOVSlowx:
hide michikofeetfast
hide michikofeetslow
hide michikofeetpovfast
scene bedroom14 blurred
show michikofeetpovslow
call screen michikofeetpovslow01x
screen michikofeetpovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoFeetEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MichikoFeetPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MichikoFeetSlowx") 

label MichikoFeetPOVFastx:
hide michikofeetfast
hide michikofeetslow
hide michikofeetpovslow
scene bedroom14 blurred
show michikofeetpovfast
call screen michikofeetpovfast01x
screen michikofeetpovfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoFeetEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MichikoFeetPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MichikoFeetFastx") 

label MichikoFeetFastx:
hide michikofeetslow
hide michikofeetpovslow
hide michikofeetpovfast
scene bedroom19 blurred
show michikofeetfast
call screen michikofeetfast01x
screen michikofeetfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoFeetEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MichikoFeetSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("MichikoFeetPOVFastx") 

label MichikoFeetEndx:
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
jump MichikoFuckChoicex

label MichikoImpregnationx:
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
label MichikoPregnantSlowx:
hide michikopregnantfast
hide michikopregnantsceneslow
hide michikopregnantscenefast
scene bedroom13 blurred
show michikopregnantslow
call screen michikopregnantslow01x
screen michikopregnantslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoPregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MichikoPregnantFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("MichikoImpregnateSlowx") 

label MichikoImpregnateSlowx:
hide michikopregnantslow
hide michikopregnantfast
hide michikopregnantscenefast
scene bedroom41 blurred
show michikopregnantsceneslow
call screen michikopregnantsceneslow01x
screen michikopregnantsceneslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoPregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MichikoImpregnateFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MichikoPregnantSlowx") 

label MichikoPregnantFastx:
hide michikopregnantslow
hide michikopregnantsceneslow
hide michikopregnantscenefast
scene bedroom13 blurred
show michikopregnantfast
call screen michikopregnantfast01x
screen michikopregnantfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoPregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MichikoPregnantSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("MichikoImpregnateFastx") 

label MichikoImpregnateFastx:
hide michikopregnantslow
hide michikopregnantfast
hide michikopregnantsceneslow
scene bedroom41 blurred
show michikopregnantscenefast
call screen michikopregnantscenefast01x
screen michikopregnantscenefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MichikoPregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("MichikoImpregnateSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MichikoPregnantFastx") 
            
label MichikoPregnantEndx:
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
jump MichikoGallery