label CompoundGallery:
call screen gallerycompound
screen gallerycompound:
    add "Gallery/compoundgallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("gallerycompound"), Jump ("MainGallery")]

    imagebutton:
        focus_mask True
        idle "Gallery/gallerynextpage.png"
        hover "Gallery/gallerynextpage.png"
        action [Hide ("gallerycompound"), Jump ("CompoundGalleryb")]

    if renpy.seen_image("mcpouch10"):
        imagebutton:
            focus_mask True
            idle "Gallery/compoundgallery01.png" xpos 620 ypos 100
            hover "Gallery/compoundgallery01.png"
            action Jump ("CompoundGallery01")

    if renpy.seen_image("mcpouch10") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 620 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("CompoundGallery")

    if renpy.seen_image("barbarapose01"):
        imagebutton:
            focus_mask True
            idle "Gallery/compoundgallery02.png" xpos 1048 ypos 100
            hover "Gallery/compoundgallery02.png"
            action Jump ("CompoundGallery02")

    if renpy.seen_image("barbarapose01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1048 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("CompoundGallery")

    if renpy.seen_image("prisonerfuck01"):
        imagebutton:
            focus_mask True
            idle "Gallery/compoundgallery03.png" xpos 1478 ypos 100
            hover "Gallery/compoundgallery03.png"
            action Jump ("CompoundGallery03")

    if renpy.seen_image("prisonerfuck01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("CompoundGallery")
            
    if renpy.seen_image("baptism01"):
        imagebutton:
            focus_mask True
            idle "Gallery/compoundgallery04.png" xpos 620 ypos 400
            hover "Gallery/compoundgallery04.png"
            action Jump ("CompoundGallery04")

    if renpy.seen_image("baptism01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 620 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("CompoundGallery")

    if renpy.seen_image("clara11"):
        imagebutton:
            focus_mask True
            idle "Gallery/compoundgallery05.png" xpos 1048 ypos 400
            hover "Gallery/compoundgallery05.png"
            action Jump ("CompoundGallery05")

    if renpy.seen_image("clara11") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1048 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("CompoundGallery")

    if renpy.seen_image("aylacrypt01"):
        imagebutton:
            focus_mask True
            idle "Gallery/aylagallery05.png" xpos 1478 ypos 400
            hover "Gallery/aylagallery05.png"
            action Jump ("CompoundGallery06")

    if renpy.seen_image("aylacrypt01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("CompoundGallery")

    if renpy.seen_image("francine01"):
        imagebutton:
            focus_mask True
            idle "Gallery/compoundgallery07.png" xpos 620 ypos 700
            hover "Gallery/compoundgallery07.png"
            action Jump ("CompoundGallery07")

    if renpy.seen_image("francine01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 620 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("CompoundGallery")

    if renpy.seen_image("mcfrancinesexcum01"):
        imagebutton:
            focus_mask True
            idle "Gallery/compoundgallery08.png" xpos 1048 ypos 700
            hover "Gallery/compoundgallery08.png"
            action Jump ("CompoundGallery08")

    if renpy.seen_image("mcfrancinesexcum01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1048 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("CompoundGallery")

    if renpy.seen_image("amyschool01b"):
        imagebutton:
            focus_mask True
            idle "Gallery/compoundgallery09.png" xpos 1478 ypos 700
            hover "Gallery/compoundgallery09.png"
            action Jump ("CompoundGallery09")

    if renpy.seen_image("amyschool01b") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("CompoundGallery")
            
    add "Gallery/gallerygrid02.png"
    add "Gallery/textcompound.png"

label CompoundGalleryb:
call screen gallerycompoundb
screen gallerycompoundb:
    add "Gallery/compoundgallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("gallerycompoundb"), Jump ("MainGallery")]

    imagebutton:
        focus_mask True
        idle "Gallery/gallerynextpage.png"
        hover "Gallery/gallerynextpage.png"
        action [Hide ("gallerycompoundb"), Jump ("CompoundGallery")]

    if renpy.seen_image("mckinky01"):
        imagebutton:
            focus_mask True
            idle "Gallery/compoundgallery10.png" xpos 620 ypos 100
            hover "Gallery/compoundgallery10.png"
            action Jump ("CompoundGallery10")

    if renpy.seen_image("mckinky01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 620 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("CompoundGallery")

    add "Gallery/galleryfuture.png" xpos 1050 ypos 100

    add "Gallery/galleryfuture.png" xpos 1478 ypos 100

    add "Gallery/galleryfuture.png" xpos 621 ypos 400

    add "Gallery/galleryfuture.png" xpos 1050 ypos 400

    add "Gallery/galleryfuture.png" xpos 1478 ypos 400

    add "Gallery/galleryfuture.png" xpos 620 ypos 700

    add "Gallery/galleryfuture.png" xpos 1048 ypos 700

    add "Gallery/galleryfuture.png" xpos 1478 ypos 700

    add "Gallery/gallerygrid02.png"
    add "Gallery/textcompound02.png"
    
label CompoundGallery01:
stop music
scene studio01
show joe02
jo "So, I'll give you some privacy to let you change into your sexy pouch. I REALLY hope it's SEXY enough for the \"All-New American Stud Hero Calendar\"."
mc "It should be, don't worry."
scene studio02
show mcpouch00
with dissolve
mc "There, I'm ready Joe."
jo "Oh, wow. It definitely IS a sexy pouch... So risqué, I like your way of thinking to win this competition..."
jo "So start flexing those biceps [name], the jury will want to see how RIPPED your body is..."
hide mcpouch00
show mcpouch01
with fastdissolve
jo "Nice, how about you get down on one knee while maintaining that pose now."
mc "Sure..."
scene studio03
show mcpouch02
with fastdissolve
play sound "Sounds/flash.mp3"
jo "Good, flex as MIGHTILY as you can!"
hide mcpouch02
show mcpouch03
with fastdissolve
mc "Oh oh, some blood went to my... thing."
jo "Not a problem, I forgot to mention that this calendar does allow adult content... So keep flexing and pumping blood to your GIANT ROD!"
hide mcpouch03
show mcpouch04
with fastdissolve
mc "Alright, but I'm seriously getting a boner... I don't know if I sh..."
jo "It's really the only way of winning this thing anyway. You want to win, right?"
mc "Yeah, I'm a WINNER!"
jo "Then get HARD for me!"
hide mcpouch04
show mcpouch05
with fastdissolve
play sound "Sounds/thud.mp3"
jo "Yeah! Now grab your cock with one hand..."
mc "What, you want me to jerk off?"
jo "Sure, if you can show them how much cum you have in your young MASSIVE balls, they'll be mightily impressed for sure!"
hide mcpouch05
show mcpouch09
with fastdissolve
jo "It looks like you're big enough to suck yourself off..."
mc "I'm not doing that, that's totally gay!"
jo "Just a lick, that's ten bonus points according to the leaflet I got..."
mc "Alright, but nothing more..."
hide mcpouch09
show mcpouch07
with fastdissolve
mc "There, I've shown you I can lick my own helmet."
jo "Great, let me get a few snaps of that..."
play sound "Sounds/flash.mp3"
jo "Now jerk your cock until you cum..."
hide mcpouch07
label MCWankSlowx:
hide mcwank01fast
show mcwank01slow
call screen mcwank01slowx
screen mcwank01slowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("McWank01Endx")    
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MCWankFastx") 

label MCWankFastx:
hide mcwank01slow
show mcwank01fast
call screen mcwank01fastx
screen mcwank01fastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("McWank01Endx")    
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MCWankSlowx") 

label McWank01Endx:
show mcpouch09
jo "Now CUM [name]!"
hide mcwank01slow
hide mcwank01fast
hide mcpouch09
show mcpouch10
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "FUUCKK!"
jo "Yeah, keep blasting that young cream!"
hide mcpouch10
show mcpouch11
with fastdissolve
jo "Oh, wow, your shots are getting even BIGGER!"
mc "Damn, my balls are in OVERLOAD! RHAAA!"
jo "I want you to blast the MOST POWERFUL CUMSPRAY EVER!"
mc "I'll tr..."
hide mcpouch11
show mcpouch12
with fastdissolve
mc "...try.... AAAHH!"
jo "Damn boy, it's reaching way above your head! We have a WINNER!"
hide mcpouch12
show mcpouch13
with fastdissolve
jo "Yeah, now just hold that pose, I'll take a few snaps of your monster rod DRIPPING ounces of cum as a mere aftermath of that POWERFUL display of VIRILITY!"
play sound "Sounds/flash.mp3"
mc "Yeah, I'm da man, I'm da HERO!"
jo "Here's your money, I'll keep you posted how it went, but I am very EXCITED about our chances of winning this photo competition!"
scene studio01
show joe01
with dissolve
jo "Now I'm gonna have to clean up that studio of all your cum. I've got my own method for that..."
mc "And I don't want to know. Goodbye Joe." 
jump CompoundGallery

label CompoundGallery02:
stop music
scene studio01b
show joe01
jo "Ah, great, you managed to find a partner for the photo shoot."
jo "Barbara is a great choice. As a trumpster, she can sway the jury in our favor. And she definitely fulfills the minimum DD cup measurement."
jo "Now get in your competition gear both of you, I'll set up the equipment. As you can see, I changed the screen color to something more patriotic."
scene studio02b
show barbarapose01 at midright with moveinright
ba "Oh, I'm sssoo excited about this. I can't believe I'm posing for such a PATRIOTIC calendar!"
show mcpose01 at midleft with moveinleft
mc "I hope it won't bring too much attention on the compound from the Trumpf Militia..."
jo "Don't worry, I use a secret server in Ukraine and it's totally safe."
hide barbarapose01
show barbarapose02 at midright
ba "Oh, [name], your... thong... It's busting with POWER!"
hide mcpose01
show mcpose02 at midleft
mc "That's because it's trying to hide something VERY BIG underneath it!"
jo "There are set poses for this calendar. So, first, [name] needs to flex his biceps while Barbara feels them up..."
scene studio03b
show mcbarbarapose01
ba "Like that Joe? Oooh, that bicep... It's ssoo hard!"
play sound "Sounds/flash.mp3"
jo "Yeah, perfect. Now point at his crotch, like you're very impressed."
hide mcbarbarapose01
show mcbarbarapose02
ba "I AM mightily impressed for real!"
play sound "Sounds/flash.mp3"
jo "Now [name], you hold her in one arm, looking at her lovingly, while Barbara feels up your crotch a little bit..."
hide mcbarbarapose02
show mcbarbarapose03
jo "Nice, let me take a few snaps... Barbara, you're a lucky woman!"
play sound "Sounds/flash.mp3"
mc "I'd say I'm a lucky man too!"
ba "How, that is such a nice thing to say [name]..."
jo "Now, Barbara, this calendar is meant to be a little bit saucy. According to the leaflet, you need to take your top off."
ba "What? But..."
jo "Do you want to be an All-New American Hero for President-for-Life Trumpf or not?"
ba "Oh... Alright then. I will do ANYTHING for our Great President!"
hide mcbarbarapose03
show mcbarbarapose04
jo "Just like that, hold her tenderly [name]... Now, maybe move your right arm a little higher..."
hide mcbarbarapose04
show mcbarbarapose05
ba "[name]! You're fondling my breast! Stop it!"
play sound "Sounds/flash.mp3"
mc "Joe told me to do that. It's for the calendar. The PATRIOTIC \"All-New American Alpha-Couple\" calendar."
hide mcbarbarapose05
show mcbarbarapose06
ba "Oh, but... Is this really in the instructions Joe?"
jo "Yes, definitely, page 69. \"The male shall fondle the female's breast prior to removing her bikini bottom.\""
ba "What? You mean, I have to be naked after that?"
jo "Don't worry, you won't be alone. [name] also has to get butt-naked. And has to display a massive rock-hard ERECTION."
mc "Come on Barbara, we've been there before, what's the big deal?"
ba "Umpf... I find those instruction rather fishy. I can't believe our Great President-for-Life would want such a salacious calendar. He normally has such outstanding moral values..."
jo "Maybe some covfefe boy he never met wrote these instructions. In any case, it's the deal if you want you continue. Or would you rather give up?"
ba "No! A trumpster NEVER gives up!"
hide mcbarbarapose06
show mcbarbarapose07
jo "This set \"pussy-grabbing\" pose is perfect. Hold it..."
play sound "Sounds/flash.mp3"
jo "Now it's time to unveil your dong [name], soft to begin with please..."
hide mcbarbarapose07
show mcbarbarapose08
ba "At last, I'm not the only one naked around here anymore..."
jo "Now do a bodybuilder pose while Barbara stands beside you..."
hide mcbarbarapose08
show mcbarbarapose09
mc "Like that?"
play sound "Sounds/flash.mp3"
jo "Yes, perfect. Get that giant piece of boymeat ROCKHARD for me...I mean Barbara, please."
hide mcbarbarapose09
show mcbarbarapose10
mc "There you go, erect and reporting for duty!"
ba "I don't like where this is headed... What does your instruction booklet say Joe?"
jo "The final first-stage pose requires the female to sit on the male's erect penis and do a victory pose."
ba "What, do you think your cock will support my WHOLE body [name]? I've... gained a bit of weight lately..."
mc "No problem for my MEGA-COCK. It's so powerful I'll lift you clear off the ground!"
hide mcbarbarapose10
show mcbarbarapose11
mc "See Barbara? I can hold that pose for Joe for as long as I want."
ba "Wow [name], that thing really is POWERFUL!"
play sound "Sounds/flash.mp3"
jo "And now from a different angle, stand still, hold the pose..."
scene studio03b blurred
show mcbarbarapose12
play sound "Sounds/flash.mp3"
jo "There, now, for the final stage..."
jo "The \"Make New America Cum Again\" pics."
ba "Come again?"
jo "No, I said \"CUM AGAIN\". You need to wank [name]'s massive All-New American COCK with both hands and make him ERUPT for Trumpf."
ba "WHHAAAT???"
jo "It's for our Great President-for-Life, Barbara, remember... To show the remaining New Americans that we are still a nation of HEROES and STUDS."
ba "Alright, just this once. For President TRUMPF!"
scene studio03b
label MCBarbaraWankSlowx:
hide mcbarbarawank01fast
show mcbarbarawank01slow
call screen mcbarbarawankslowx
screen mcbarbarawankslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MCBarbaraWankEndx")    
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MCBarbaraWankFastx") 

label MCBarbaraWankFastx:
jo "Jerk it faster Barbara, I think it's on the verge of EXPLODING!"
hide mcbarbarawank01slow
show mcbarbarawank01fast
call screen mcbarbarawankfastx
screen mcbarbarawankfastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MCBarbaraWankEndx")    
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MCBarbaraWankSlowx") 

label MCBarbaraWankEndx:
mc "Get ready Joe, because I'm about to BU-URST!"
hide mcbarbarawank01slow
hide mcbarbarawank01fast
show mcbarbaracum01
mc "FUCK YEAH! ALL-NEW AMERICAN STUD CREAM COMING YOUR WAY BARBARA! RHAAA!"
jo "Cover her tits, that would make for a great photo to send!"
hide mcbarbaracum01
show mcbarbaracum02
with fastdissolve
ba "Oh my God, how will I get rid of ALL THAT VIRILE SPUNK!!!"
jo "Err... I've got a method for th..."
mc "We DON'T want to know, keep snapping, there's TONS MORE cum to come! AAAAH!"
scene studio04b blurred
show mcbarbaracum03
ba "I'm getting plastered with the stuff! How much cum do those giant seedmakers hold???"
mc "A LOT MORE teach!"
hide mcbarbaracum03
show mcbarbaracum04
with fastdissolve
mc "AAAH! I think I'm done now. No, hang on a minute..."
hide mcbarbaracum04
show mcbarbaracum05
with fastdissolve
mc "I had another shot in me..."
ba "How can you KEEP coming after pumping over a dozen MONSTER CUMSHOTS?"
jo "That will definitely impress the jury. Biggest load I've ever seen from a boy and I've...err... seen many. By pure coincidence of course."
scene studio01b
show joe02
with dissolve
jo "Thanks to both of you, this photoshoot was a success! I'll send the pics via my secret server in Ukraine as soon as I've developed them and err... analyzed them for a while."
hide joe02
show joe01
with fastdissolve
jo "You're sure you don't want any help cleaning up Barbara?"
mc "NO, she DOESN'T. Goodbye Joe."    
jump CompoundGallery

label CompoundGallery03:
scene prison02 
show prisoner01
mc "So, I hear you won't talk, Number 6? I'll make you talk."
hide prisoner01
show prisoner02
with fastdissolve
pr "PLEA-EASE. You're just a little boy with abnormally large muscles, you don't scare me."
hide prisoner02
show prisoner01
with fastdissolve
mc "Perhaps my BIG FAT truncheon will change your mind about that!"
hide prisoner01
show prisoner02
with fastdissolve
pr "Oh, I get it, you have a big dildo attached to your groin. Ooh, I'm sssoo scared!"
mc "No, it's my REAL abnormally large PUSSY WRECKER lady! You're gonna feel its wrath!"
hide prisoner02
show prisoner04
with fastdissolve
pr "Go on, rape me with your dildo, you fucking pervert. Shall I take off my panties for you and give you instructions?"
mc "Err... No, that won't be necessary, I know what I'm doing. But yeah, take your panties off, BITCH!"
hide prisoner04
show prisoner03
with fastdissolve
pr "Oooh, I'm ssoo scared, the little boy is going to rape me with his pee-pee! Help! *snickers*"
stop music
scene prisonfuck01 blurred with dissolve
show prisonerfuck01
pr "So, are you in yet? I can't feel a thing. It must be real SMALL, boy! Ho ho..."
hide prisonerfuck01
show prisonerfuck02
with fastdissolve
pr "....AAAAAAAH! What the fuck is that?"
mc "Sorry, you were saying?"
pr "Get that fucking thing out of me, I beg you!"
mc "Oh, am I hurting you? But my dong is only halway-..."
hide prisonerfuck02
show prisonerfuck03
with fastdissolve
mc "...in!"
play sound "Sounds/womanscream.ogg"
pr "AAAH, It's so fucking DEEP! Please, have MERCY!"
mc "No way, you deserve what you're getting! Until you talk!"
label Prison01Slowerx:
play music "Sounds/womansex01.mp3"
show prisonfuckmovie01slow
call screen prison01slowx
screen prison01slowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PrisonerFuck01Endx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("Prison01Fasterx") 

label Prison01Fasterx:
hide prisonfuckmovie01slow
show prisonfuckmovie01fast
call screen prison01fastx
screen prison01fastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PrisonerFuck01Endx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("Prison01Slowerx") 

label PrisonerFuck01Endx:
pr "Come in me, I want your seed!"
mc "Will you talk if I give you my seed?"
pr "YES, I promise! Just come in ME, PLEASE!"
mc "You don't deserve my seed!"        
stop music
scene prisonercum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Fuck, I'm blowing my load! AAH!"
pr "No, you're spilling it, please! What a waste!"
scene prisonercum02 with dissolve
mc "There you go, I've plastered your back with my cum. I OWE you now BITCH!"
stop sound
pr "Why are so you so cruel to me? *sob*"
mc "I might be less cruel if you were to talk..."
pr "Too late, you've spilt your seed, you're no use to me now..."
mc "You think I'm done?"
scene prisonfuck02 with dissolve
show prisonfuck02cumlayout
mc "This time, I'll fuck you up THE ARSE!"
pr "What? Your dong is too big for that!"
mc "I'll be the judge of that..."
scene prisonarse01 with dissolve
mc "It seems perfectly capable of fitting, what do you think?"
pr "Oh my God, oh my God, please, I beg you!"
scene prisonarse02 with dissolve
play sound "Sounds/womanscream.ogg"
mc "As I said, no problem sticking it all the way up your backdoor!"
pr "AAAH, take it out, it's impaling my guts!"
mc "I don't think so... I like it there."
scene prisonanalbackground with dissolve
label PrisonAnal01Slowerx:
play music "Sounds/womansex01.mp3"
hide prisonanalfast
show prisonanalslow
call screen prisonanal01slowx
screen prisonanal01slowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("Prisoner02AnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PrisonAnal01Fasterx") 

label PrisonAnal01Fasterx:
hide prisonanalslow
show prisonanalfast
call screen prisonanal01fastx
screen prisonanal01fastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("Prisoner02AnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PrisonAnal01Slowerx") 

label Prisoner02AnalEndx:
stop music
scene prisonanalcumbackground
show prisonanalcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Fuck Yeah! Cumming so much! Giving you a sperm edema!"
pr "This is so humiliating, you are so cruel!"
scene prisonerend01 with dissolve
mc "See you again for more CRUELTY until you SPEAK number 6!"
jump CompoundGallery

label CompoundGallery04:
scene crypt01
show tyrone05 at midright
show clara03 at midleft
ty "What's your name young man?"
mc "[name]."
cl "That is such a lovely and holy name..."
ty "Alright, pull your penis out [name]."
mc "What? Why?"
ty "You want to get baptized? That's how the ceremony works..."
mc "Alright? I'll pull it out..."
play sound "Sounds/zipper.mp3"
hide tyrone05
show tyrone07 at midright
hide clara03
show clara05 at midleft
with fastdissolve
ty "What the fuck? Are you a mutant or something?"
mc "I received a healthy dose of alpha-radiations you could say. So, can I get baptized now?"
ty "Err... Sure. I'll start the ceremony. Sister Clara, hold his penis if you will while I perform the ritual."
hide clara05
show clara04 at midleft
with fastdissolve
cl "What? But this is so embarrassing Father..."
hide tyrone07
show tyrone04 at midright
with fastdissolve
ty "It's not like it's the first time you've held a cock, you sinning bitch. Get on with it!"
cl "At your pleasure... Father."
scene baptism01 with dissolve
mc "Don't be scared Sister Clara, It won't bite..."
cl "How do you even hold that thing?"
ty "Put your hand underneath it and lift it Sister. It needs to be facing the Heavens while I baptize [name]."
scene baptism02 with dissolve
mc "Uh Oh,... OK, I'm holding it Father."
ty "Do you reject Satan, and all his anal buggery?"
mc "Err.. Yes."
ty "Do you believe in the Holy Sperm, the Holy Phallic Church, the reserection of the Cock, and life everlasting?"
mc "Absolutely."
scene crypt03
show tyrone06
with dissolve
ty "In the name of the Father, the Son and the Holy Sperm, I baptized thy penis..."
cl "Se-men."
mc "That's it?"
hide tyrone06
show tyrone05
with fastdissolve
ty "That's it. What, you were expecting Sister Clara to give you a blowjob or something?"
mc "Well, it would have been nice for sure..."
ty "You can pull your pants back up young man. You are now officially a congregant of the Church of the Redeeming Phallus."
scene baptism03 with dissolve
cl "Uh-ooh... It's so big..."
mc "Thank you Father, I think I'd better get going then..."    
jump CompoundGallery

label CompoundGallery05:
stop music
play sound "Sounds/footsteps.mp3"
scene cryptenter
mc "Oh, oh, Father Tyrone and Sister Clara are entering the Moist Crypt. Let's follow them and hide in the shadows."
stop sound
scene cryptdooropen with dissolve
play sound "Sounds/doorsqueak.mp3"
mc "This door's hinges clearly need some WD-69."
stop sound
scene crypt01 with fade
mc "I found a good hiding place with a clear view of the crypt. What a stroke of luck. Thank you dev."
window hide
show clara10 with moveinleft
mc "Oh, Oh, Clara is wearing some rather naughty nun outfit..."
ty "Sister Clara, do you confess to your utter depravity?"
cl "Y.. Yes, Father."
ty "And do you know what is the punishment for sinning whores like you?"
hide clara10
show clara10b
with fastdissolve
cl "Y..Yes Father. But, I..."
ty "Silence! May the Phallus Lord have mercy on you, cos I sure won't. Assume your position for your Holy Flogging."
scene crypt05
show clara11
with dissolve
ty "I will administer your flogging in my Punisher outfit. As per the rules."
cl "But the rules say th..."
ty "Silence! I KNOW the rules, don't try and teach them to me! Now lift that fine ass higher to the Phallus Lord..."
hide clara11
show clara12
with dissolve
ty "That's better... What a shame it is to flog such a nice piece of booty..."
cl "Wh...What are you saying Father?"
ty "Tell you what, I will commute your punishment to Holy Spanking."
cl "I... never heard of this, Fath..."
hide clara12
show clara13
with dissolve
ty "Silence! The rules are clear, it's not my fault if you are an ignorant slut!"
hide clara13
show clara14
with fastdissolve
play sound "Sounds/slap.mp3"
ty "Take that, you depraved hussy!"
hide clara14
show clara13
with fastdissolve
cl "AAAH, you're hurting me Father!"
hide clara13
show clara14
with fastdissolve
play sound "Sounds/slap.mp3"
ty "And some more, devilishly tempting creature!"
hide clara14
show clara13
with fastdissolve
cl "AAAH, I repent, please stop!"
ty "Not good enough, get on my knees for a REAL spanking."
hide clara13
show clara15
with fastdissolve
ty "Yeah, that's nice..."
cl "But Father, I can feel your... thingie rubbing ag..."
hide clara15
show clara16
with fastdissolve
play sound "Sounds/slap.mp3"
ty "Silence while I spank you!"
hide clara16
show clara15
with fastdissolve
mc "It feels wrong. And kinda right at the same time knowing that crazy Church. I don't know what to make of it..."
hide clara15
show clara16
with fastdissolve
play sound "Sounds/slap.mp3"
ty "And don't you dare complain to the Cardinal, you hear me, nasty bitch?"
mc "Oh, oh, he's hiding something..."
cl "AAAH! I... I promise, Father."
window hide
play sound "Sounds/drop.mp3"
$ renpy.pause(1.0, hard=True)
mc "Ah shit, I dropped a candelaber... Let's get the hell out of here quickly!"
stop sound    
jump CompoundGallery

label CompoundGallery06:
play sound "Sounds/footsteps.mp3"
scene aylacryptenter
mc "Oh, oh, Father Tyrone and Ayla are entering the Moist Crypt. Let's follow them and hide in the shadows."
stop sound
scene cryptdooropen with dissolve
play sound "Sounds/doorsqueak.mp3"
$ renpy.pause(1.0, hard=True)
scene crypt01 with fade
stop sound
mc "I'm in position, let's wait for the sinners to sin..."
window hide
show aylacrypt01 at left with moveinleft
show tyronecrypt01 at right with moveinright
ay "Why did you call me here, Father? And why are dressed like a fucking PERVERT?"
ty "I'll tell you, I've noticed that you don't take part in communion and that you're always angry when I insist that you eat the Meat of the Phallus."
hide aylacrypt01
show aylacrypt02 at left
with fastdissolve
ay "Yeah, so , what's it to you? I'm a vegetarian!"
ty "No, my sweet little thing, you show all the signs that you are POSSESSED by a PUSSY-DEMONESS."
ay "WHAT???"
ty "And I need to perform an exorcism on your pussy as soon as possible before your soul is corrupted by this succubus from Hell."
hide aylacrypt02
show aylacrypt03 at left
with fastdissolve
ay "I'm possessed...  That's why I have been so unlucky in finding my boyfriend. I'm CURSED! What did I do to deserve this, Father?"
hide tyronecrypt01
show tyronecrypt02 at right
with fastdissolve
ty "We are all sinners, but you're a particular kind. You must follow my every order if you want to rid yourself of this devilish fiend inside your pussy!"
hide aylacrypt03
show aylacrypt01 at left
with fastdissolve
ay "And what do I have to do?"
ty "Take your lingerie off, the exorcism machine needs access to your intimate, but demon-possessed parts..."
ay "That sounds... disgusting!"
ty "It is the Devil that speaks through! OBEY, creature from HELL!"
hide aylacrypt01
show aylacrypt04 at left
with dissolve
ay "There, are you happy you fucking PERVERT FREAK?"
hide tyronecrypt02
show tyronecrypt01 at right
with fastdissolve
ty "Quite so, quite so Ayla... Now get in the machine."
ay "This had better not hurt. Or I'll head-punch you in the groin!"
scene crypt05
show ayladread03
with dissolve
ty "There... The machine will introduce a dildo blessed with Holy Baby Oil into your orifices now..."
ay "That's DISGUSTING!"
ty "Standard exorcism procedures, Ayla, I don't make the rules..."
ay "Go ahead with your filthy PERVERT machine then!"
scene crypt07
show ayladread04
with dissolve
play music "Sounds/vibrator.ogg"
ay "Ah, It's going too deep!"
scene crypt08
show ayladread02
with dissolve
ty "The demoness is lodged DEEP inside you, that's why! Just relax your muscles and let the Holy Spurt do the trick."
scene crypt07
label AylaCryptSlowz:
hide aylacryptfast
show aylacryptslow
ty "The power of Jizz compels you. The power of Jizz compels you!"
call screen aylafootslow01z
screen aylafootslow01z:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaCryptEndz")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaCryptFastz") 

label AylaCryptFastz:
hide aylacryptslow
show aylacryptfast
ty "I'll increase the tempo now and raise my voice too. THE POWER OF JIZZ COMPELS YOU. THE POWER OF JIZZ COMPELS YOU!"
call screen aylafootfast01z
screen aylafootfast01z:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaCryptEndz")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaCryptSlowz") 

label AylaCryptEndz:
stop music
hide aylacryptslow
hide aylacryptfast
show ayladreadend
play sound "Sounds/womanmoan.mp3"
ay "AAAH!"
ty "Good, you're expulsing the demoness, keep squirting Ayla!"
scene crypt05
show ayladread01
with dissolve
ty "Now let me check that it's not there anymore... With my fingers of course..."
mc "Cheeky bugger! I'm sure this whole ploy was just to stick his fingers up her cooch."
play sound "Sounds/drop.mp3"
$ renpy.pause(1.0, hard=True)
mc "Ah shit, I dropped a candelaber... Again. Let's get the hell out of here quickly!"
stop sound    
jump CompoundGallery

label CompoundGallery07:
scene interface02
play sound "Sounds/interfacestart.mp3"
pause 1.0
scene interface01 with dissolve
show francine01
fr "Bonjour! Je m'appelle Francine!"
fr "Comment t'appelles-tu?"
mc "What's it to you froggy?"
hide francine01
show francine03
with fastdissolve
fr "Ooh la la! Tu es un naughty garçon!"
hide francine03
show francine04
with fastdissolve
fr "Voulez-vous admirer mes big melons?"
mc "Oui!"
fr "Ooh la la! Tu es un très naughty garçon!"
mc "Yep, that's me!"
hide francine04
show francine01
with fastdissolve
fr "Et maintenant..."
hide francine01
show francinelingerie01
with fastdissolve
fr "La lingerie. Ooh la la!"
mc "What the fuck is this online course?"
hide francinelingerie01
show francinelingerie02
with fastdissolve
fr "Et maintenant..."
hide francinelingerie02
show francinecorset01
with fastdissolve
fr "Le corset. Très sexy, n'est-ce pas?"
hide francinecorset01
show francinecorset02
with fastdissolve
fr "Et maintenant..."
hide francinecorset02
show francinestring01
with fastdissolve
fr "Où est le string?"
hide francinestring01
show francinestring02
with fastdissolve
fr "Le string est sur ma pussy chatte. Ooh la la!"
mc "I wonder what the hell the girls are seeing in their online course..."
hide francinestring02
show francinestring03
with fastdissolve
fr "Voulez-vous un bébé?"
fr "Moi, je veux un bébé..."
hide francinestring03
show francineend01
with fastdissolve
fr "Look! J'ai un bébé maintenant! Bravo [name]!"
mc "I think it's meant to encourage me to fuck girls and make babies but I'm not sure..."
hide francineend01
show francineend02
with fastdissolve
fr "Au revoir [name]. A bientôt!"
mc "Err... yeah, bye Francine..."
scene interface01 with fade
show francine01
fr "Bonjour [name]!"
mc "Yeah, hi Francine. Again."
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
jump FrancineSex01x
label FrancineSex01prex:
fr "Moins vite!"
label FrancineSex01x:
hide francinesex02
show francinesex01
call screen francinesex01x
screen francinesex01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("FrancineSexEndx")    
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("FrancineSex02x")    

label FrancineSex02x:
fr "Plus vite!"
hide francinesex01
show francinesex02
call screen francinesex02x
screen francinesex02x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("FrancineSexEndx")    
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("FrancineSex01prex")    

label FrancineSexEndx:
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
jump CompoundGallery

label CompoundGallery08:
scene class02
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
hide mcharder
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
hide mcbigger01
hide francineblue04
show mcfrancinesex01
call screen mcfrancinesex01x
screen mcfrancinesex01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("McFrancine01Endx")

label McFrancine01Endx:
fr "Oui, c'est bon! Ooh la la! J'aime ton super-grand cock [name]!"
fr "Je veux ton ENORME cock dans ma pussy chatte!"
hide mcfrancinesex01
show mcfrancinesex02
call screen mcfrancinesex02x
screen mcfrancinesex02x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("McFrancine02Endx")
label McFrancine02Endx:        
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
jump CompoundGallery

label CompoundGallery09:
scene class02
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
scene class02 with fade
show barbara01
ba "Next up for our French conversational class is Amy!"
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
jump CompoundGallery

label CompoundGallery10:
stop music
scene studio01b
show joe02
jo "So, I'll give you some privacy to let you change into THIS. That's what I want you to wear."
mc "Fine, just give me THIS and I'll be back wearing it..."
scene studio02b
show mckinky01
with dissolve
mc "This posing pouch is kinda leathery gay, isn't it?"
jo "It is leathery, yes."
jo "Now take a menacing pose, like you're angry and flex those muscles for me [name]..."
hide mckinky01
show mckinky02
with fastdissolve
jo "you look like a MEAN BAD BOY! Now get hard a bit for me, I want to see that thong EXPAND!"
play sound "Sounds/flash.mp3"
with fastflash
mc "Sure..."
hide mckinky02
show mckinky03
with fastdissolve
play sound "Sounds/flash.mp3"
with fastflash
jo "Wow, you're really stretching it, but you need to STRETCH IT SOME MORE!"
scene studio03b
show mckinky04
with fastdissolve
mc "I'm getting totally ROCK-HARD Joe! Need to get out of it soon!"
jo "Hang on a minute, just a couple more snaps..."
play sound "Sounds/flash.mp3"
with fastflash
jo "Now pull it down and show me that horsecock!"
scene studio02b
show mckinky05
with fastdissolve
mc "There, feast your eyes..."
jo "I am, I am..."
play sound "Sounds/flash.mp3"
with fastflash
jo "Now I want you to use this penis pump. I had it specially designed for a SUPERHUGE appendage. Like yours."
mc "Alright, hand it over."
hide mckinky05
show mckinky06
with fastdissolve
jo "That's good, place it over your throbbing shaft for me..."
play sound "Sounds/flash.mp3"
with fastflash
mc "It's not as big as I thought, I hope it will fit..."
hide mckinky06
show mckinky07
with dissolve
mc "Just about. It's a pretty tight fit at the base though..."
jo "Go on, activate the pump and make your cock TOTALLY FILL THE TUBE UP!"
play sound "v08/pumping.mp3"
hide mckinky07
show mckinky08
with fastdissolve
jo "Perfect, it's working!"
mc "Yeah, but... the pump is getting too tight!"
hide mckinky08
show mckinky09
with fastdissolve
jo "Oh damn, it's about to burst, the glass is cracking, your cock is just too POWERFUL!"
mc "AAAH!..."
play sound "v08/glass.mp3"
scene studio04b blurred
show mckinky10
with fastdissolve
jo "You just DESTROYED my pump!"
mc "Sorry about that Joe...."
jo "Don't be, I'm really enjoying the show... Now put both hands around that MONSTER cock for me [name]..."
hide mckinky10
show mckinky11
with dissolve
jo "Look at that thing, you must have grown several inches, let me snap a few shots of that."
window hide
play sound "Sounds/flash.mp3"
with fastflash
jo "Now jerk that fat dong with BOTH hands..."
play music "Sounds/wank.mp3"
label MCKinkySlowx:
hide mckinky01fast
show mckinky01slow
call screen mckinkyslowx
screen mckinkyslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("McKinky01Endx")    
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MCKinkyFastx") 

label MCKinkyFastx:
jo "Go on, jerk it faster for me!"
hide mckinky01slow
show mckinky01fast
call screen mckinkyfastx
screen mckinkyfastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("McKinky01Endx")    
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MCKinkySlowx") 

label McKinky01Endx:
jo "Now BLAST THE CUM OUT OF YOUR MONSTERCOCK!"
stop music
scene studio02b blurred
show mckinky13
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "RHAAAA, FUUCKK!"
window hide
with fastflash
jo "you're erupting MONSTERSHOTS, as I expected after that heavy pumping!"
hide mckinky13
show mckinky14
with fastdissolve
jo "STILL MORE!!! I need to take some pics of that!!!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
window hide
play sound "Sounds/flash.mp3"
with fastflash
mc "Can't stop cumming, GODAMMMIT, AHHHH!"
window hide
with fastflash
hide mckinky14
show mckinky15
with dissolve
mc "Shoo, I'm covered in my own spunk..."
jo "I can help you clean it u..."
mc "NO THANK YOU. Just give me a towel or something. And also that garment you promised me."
jo "I suppose. I did make a promise.... *sigh*"
jo "But let me take a final shot of your dripping monstercock please."
mc "Sure..."
window hide
play sound "Sounds/flash.mp3"
with fastflash
jo "Fuck yeah..."
jump CompoundGalleryb
