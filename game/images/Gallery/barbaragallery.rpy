label BarbaraGallery:
call screen gallerybarbara
screen gallerybarbara:
    add "Gallery/barbaragallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("gallerybarbara"), Jump ("MainGallery")]

    if renpy.seen_image("barbarapool04"):
        imagebutton:
            focus_mask True
            idle "Gallery/barbaragallery01.png" xpos 621 ypos 100
            hover "Gallery/barbaragallery01.png"
            action Jump ("BarbaraGallery01")

    if renpy.seen_image("barbarapool04") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("BarbaraGallery")

    if renpy.seen_image("dreambarbara09"):
        imagebutton:
            focus_mask True
            idle "Gallery/barbaragallery02.png" xpos 1050 ypos 100
            hover "Gallery/barbaragallery02.png"
            action Jump ("BarbaraGallery02")

    if renpy.seen_image("dreambarbara09") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("BarbaraGallery")

    if renpy.seen_image("barbarapose01"):
        imagebutton:
            focus_mask True
            idle "Gallery/compoundgallery02.png" xpos 1478 ypos 100
            hover "Gallery/compoundgallery02.png"
            action Jump ("BarbaraGallery03")

    if renpy.seen_image("barbarapose01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("BarbaraGallery")
    
    if renpy.seen_image("barbara09"):
        imagebutton:
            focus_mask True
            idle "Gallery/barbaragallery04.png" xpos 621 ypos 400
            hover "Gallery/barbaragallery04.png"
            action Jump ("BarbaraGallery04")

    if renpy.seen_image("barbara09") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("BarbaraGallery")

    if renpy.seen_image("barbaradate01"):
        imagebutton:
            focus_mask True
            idle "Gallery/barbaragallery05.png" xpos 1050 ypos 400
            hover "Gallery/barbaragallery05.png"
            action Jump ("BarbaraGallery05")

    if renpy.seen_image("barbaradate01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("BarbaraGallery")

    if renpy.seen_image("barbaralingerie01"):
        imagebutton:
            focus_mask True
            idle "Gallery/barbaragallery06.png" xpos 1478 ypos 400
            hover "Gallery/barbaragallery06.png"
            action Jump ("BarbaraGallery06")

    if renpy.seen_image("barbaralingerie01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("BarbaraGallery")

    add "Gallery/galleryfuture.png" xpos 620 ypos 700

    add "Gallery/galleryfuture.png" xpos 1048 ypos 700

    add "Gallery/galleryfuture.png" xpos 1478 ypos 700

    add "Gallery/gallerygrid02.png"
    add "Gallery/textbarbara.png"

label BarbaraGallery01:
scene pool03
show barbarapool01
mc "Barbara sure has a fine ass..."
hide barbarapool01
show barbarapool02
with fastdissolve
mc "I got myself a patriotic MNAGAt hat teach!"
hide barbarapool02
show barbarapool05
with fastdissolve
ba "Oh really, let's see it then!"
show mcpoolhat01 at midleft with moveinleft
show barbarapool05 at midright with move
hide barbarapool05
show barbarapool07 at midright       
ba "Oh, you look so CLASSY in that baseball cap [name]! You could definitely join one of our Glorious Leader's great rallies with it."
mc "Yeah, I can tell by my reflection in the pool. Totally not deplorable at all."
mc "Would you like to pose for a PATRIOTIC calendar with me Barbara?"
hide barbarapool07
show barbarapool03 at midright   
with fastdissolve
ba "What? I'm not sure, I've never done that before... Why would you need me for such a calendar?"
mc "Well, you already have a patriotic swimming suit for starters... And you're smoking hot too."
hide barbarapool03
show barbarapool04 at midright   
with fastdissolve
ba "I'm not planning on posing in a swimsuit with you [name]! This would be highly inappropriate..."
mc "The calendar competition was launched by President-for-life Trumpf himself teach! How could you refuse?"
hide barbarapool04
show barbarapool08 at midright   
with fastdissolve
ba "Err... Ok, if it is for the sake of our Great Nation, then I'll do it I guess..."
hide barbarapool08
show barbarapool02 at midright   
with fastdissolve
mc "I'll call you when Joe is ready for it then. Bye Barbara!"
jump BarbaraGallery

label BarbaraGallery02:
play sound "Sounds/dream.mp3"
scene classdream
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
stop music
jump BarbaraGallery

label BarbaraGallery03:
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
label MCBarbaraWankSlowz:
hide mcbarbarawank01fast
show mcbarbarawank01slow
call screen mcbarbarawankslowz
screen mcbarbarawankslowz:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MCBarbaraWankEndz")    
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MCBarbaraWankFastz") 

label MCBarbaraWankFastz:
jo "Jerk it faster Barbara, I think it's on the verge of EXPLODING!"
hide mcbarbarawank01slow
show mcbarbarawank01fast
call screen mcbarbarawankfastz
screen mcbarbarawankfastz:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MCBarbaraWankEndz")    
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MCBarbaraWankSlowz") 

label MCBarbaraWankEndz:
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
jump BarbaraGallery

label BarbaraGallery04:
scene class02
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
call screen barbarasexx
screen barbarasexx:
    add barbarasex at center
    modal True
    button:
        xpos .91
        ypos .44
        xysize(140, 80)        
        action Jump ("BarbaraSexEndx")    

label BarbaraSexEndx:
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
jump BarbaraGallery


label BarbaraGallery05:
play channel1 "v07/datemusic.mp3"
scene canyon01
show barbaradate01
ba "Is this the place? I never knew it even existed. Chief Lena doesn't allow me out of the compound much...."
mc "Don't worry, she doesn't know you're here."
hide barbaradate01
show barbaradate02
with fastdissolve
ba "Well, it IS beautiful. Is the water radioactive?"
mc "Err, I never checked to be honest. But I'm been swimming here for a while and I'm totally normal."
hide barbaradate02
show barbaradate03
with fastdissolve
ba "Well, let's go for a swim then, it's scorching hot out here."
mc "Sure, Barbara!"
scene barbaradate04 with dissolve
ba "The water is really refreshing. I can't believe how hot it is today!"
mc "Yeah, I agree, it's hotter than normal. Maybe we're in summer?"
scene barbaradate05 with dissolve
ba "Yes, it's August. Don't you keep track of time? I'm getting out, I want to work on my tan while I'm here..."
scene barbaradate06 with dissolve
mc "I think you should put some protection on you. You wouldn't want to get sunburnt now would you?"
ba "Well, thank you for thinking about my health [name]... Unfortunately, I don't have any sunscreen. Do you?"
mc "No, but... err... I can provide some special cream."
scene barbaradate06b with dissolve
ba "Let me guess. You want me to rub your spunk over my body to protect me from the sun? Did I get that right?"
mc "Err, not exactly. I'd be rubbing it myself, you wouldn't have to do anything, teach!"
scene barbaradate06 with dissolve
ba "*sigh* Well, I have nothing to lose I guess. So go on, take your cock out and jack it over my body until you nut, you filthy boy."
mc "Alright! One serving of [name]'s special sun cream coming right your way, Barbara!"
play channel2 "Sounds/wank.mp3"
scene barbaradate07 with fastdissolve
pause 0.2
scene barbaradate08 with fastdissolve
pause 0.2
scene barbaradate07 with fastdissolve
pause 0.2
scene barbaradate08 with fastdissolve
pause 0.2
scene barbaradate07 with fastdissolve
pause 0.2
scene barbaradate08 with fastdissolve
pause 0.2
scene barbaradate07 with fastdissolve
pause 0.2
scene barbaradate08 with fastdissolve
pause 0.2
scene barbaradate07 with fastdissolve
pause 0.2
scene barbaradate08 with fastdissolve
pause 0.2
scene barbaradate07 with fastdissolve
pause 0.2
scene barbaradate08 with fastdissolve
pause 0.2
scene barbaradate07 with fastdissolve
pause 0.2
scene barbaradate08 with fastdissolve
pause 0.2
scene barbaradate07 with fastdissolve
pause 0.2
scene barbaradate08 with fastdissolve
pause 0.2
scene barbaradate08b with fastdissolve
stop channel2
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "That's it, [name]'s superior sunscreen for maximal protection is CO-O-MING!"
window hide
with fastflash
show barbaradate08c with dissolve
stop channel2
ba "Oh My God [name], that's a LOT of cream!"
window hide
with fastflash
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "My balls are FU-UUU-LLL!"
scene barbaradate09 with fastdissolve
mc "Turn around, teach, you also need cream on your front!"
window hide
with fastflash
mc "RHAAA!"
scene barbaradate10 with fastdissolve
ba "What the?... You're PLASTERING me in your filthy boyspunk!"
window hide
with fastflash
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "You wanted protection, I give you protection Barbara, RHAAA!"
scene barbaradate11 with fastdissolve
play sound "Sounds/moaning02.mp3"
ba "Well, this date didn't go at all the way I expected it... I just let one of my students shower me with his cum..."
mc "I must admit I didn't see that coming either..."
ba "Still, you gave me the protection I needed. So now I'm going to enjoy the sun, and your sperm, on my skin..."
stop channel1
stop sound
scene canyon01
show barbaradate01
with dissolve
ba "I'm done, I have a great tan now, thanks for taking me on this... date [name]."
mc "Glad I could have been of service to you... And your skin."
hide barbaradate01
show barbaradate03
with fastdissolve
ba "...Yes... But it's our little secret, you hear me?... Now let's get back to the compound before anyone sees us."
mc "Sure teach... The period just advanced anyway so I'm supposed to do something else now. Like go back to the gallery menu."
jump BarbaraGallery

label BarbaraGallery06:
scene bedroom01
show barbara01
ba "Good evening [name], do you need help with your school homework?"
mc "No, that's done. But I have some nightwork to do still. WITH YOUR BODY!"
window hide
hide barbara01
show barbara08
with fastdissolve
ba "I thought you might, you naughty boy... Let me get my nightwork outfit for you then...Be right back!"
hide barbara08 with moveoutright
play music "v07/datemusic.mp3"
scene bedroom02 with fade
show barbaralingerie01 at center with moveinright
ba "So what do you think? Is it NAUGHTY enough for my favorite student?"
mc "Hell yeah teach!"
hide barbaralingerie01
show barbaralingerie02
with fastdissolve
ba "And just how NAUGHTY do you plan to be with me tonight [name]?"
mc "Very VERY naughty Barbara..."
scene bedroom02 blurred
show barbaralingerie02b
with dissolve
mc "You have such a fine body teach... I'm getting hard for you right now..."
scene bedroom02
show barbarawiggle00
with dissolve
ba "Let me help you get it ROCKHARD then..."
hide barbarawiggle00
show barbarawiggle
with dissolve
stop music
play music "Sounds/stripmusic.mp3"
call screen barbarawigx
screen barbarawigx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraWiggleEndx")

label BarbaraWiggleEndx:
mc "That did it, Barbara, my cock is as hard as a BAR OF TITANIUM!"
ba "Well come and show me, I want to see it. Because I feel VERY naughty too!"
stop music
hide barbarawiggle
show barbarawiggle00b
show barbarawiggle00b at farleft with move
show barbaralingeriemc01 at right with moveinright
mc "Here I am, Barbara!"
ba "My, what a hugely ERECT cock you're sporting for your teacher..."
scene bedroom02 blurred
show barbaralingeriemc02
with fastdissolve
play sound "Sounds/moaning.mp3"
ba "Mmmh, you like grabbing my big milky funbags, don't you?"
if trumpsternickname:    
    mc "They don't call me \"[name] the Grabber\" for nothing!"
    ba "Go right ahead, grab as much as you want, you can do whatever you like..."
if mctrumpster == 5 and trumpsternickname == False:
    ba "I think it's time for you to get a nickname... \"[name] the Grabber\" seems appropriate!"
    ba "And now go right ahead, grab as much as you want, you can do whatever you like..."
if mctrumpster <= 4 and trumpsternickname == False:
    ba "You're a VERY naughty boy [name]!"
hide barbaralingeriemc02
show barbaralingeriemc03
with fastdissolve
ba "Oooh, you just grabbed me BY THE PUSSY, you naughty boy!"
mc "Just checking that it's nice and wet for my horsedick, teach!"
ba "I can assure you that IT IS! Now go and sit on the sofa and I'll join you right away.. to admire that rockhard HORSEDICK!" 
scene barbarasofa01 with dissolve
mc "God those tits, they're just so... amazing..."
ba "I take good care of my body... For students like YOU."
scene barbarasofa02 with dissolve
ba "So that they pop hardons in my class... That way, I can spot the really HUNG ONES and give them after-class PRIVATE lessons...."
mc "You're so NAUGHTY Barbara! I'm gonna wank my pole and get it ROCKHARD for you!"
scene barbarasofa03 with dissolve
play sound "Sounds/lick.mp3"
play channel1 "Sounds/moaning03.ogg"
ba "Let me take care of those big FAT balls while you do that..."
scene barbarasofa04 with dissolve
ba "What a MONSTERCOCK! I've never seen such a HUGE ROD on a such a young MUSCLED STUD before!"
mc "Then let's see how your mouth handles it, teach!"
ba "Ooh, you want me to blow your GIANT teenage love muscle all the way down my throat [name]?"
mc "Y... Yes please, Barbara!"
play channel2 "Sounds/hardsucking.mp3"
label BarbaraSuckSlowx:
hide barbarasuckfast
show barbarasuckslow
call screen barbarasuckslow01x
screen barbarasuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraSuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BarbaraSuckFastx") 

label BarbaraSuckFastx:
mc "Come on teach, do it faster and make me BLOW MY NUT!"
hide barbarasuckslow
show barbarasuckfast
call screen barbarasuckfast01x
screen barbarasuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraSuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BarbaraSuckSlowx") 

label BarbaraSuckEndx:
mc "I'm about to unload down your throat!"
stop channel1
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
scene barbarasuckcum01 with dissolve
mc "There I go, AAAH!"
window hide
with fastflash
mc "You suck me sssooo GOOD!"
scene barbarasuckcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "FUCK YEAH! MORE FOR YOU TEACH!"
window hide
with fastflash
mc "Damn it, I'm cumming NON-STOP, RHAAA!"
stop channel2
scene barbarasuckcum03 with dissolve
ba "That was a real CUM MEAL you gave me [name]!"
mc "And you didn't EAT IT ALL..."
scene barbarasuckcum04 with dissolve
play sound "Sounds/sucking.mp3"
ba "I will, don't worry... Your young musky cum is so tasty..."
mc "You're a real cum-addict aren't you Barbara?"
play sound "Sounds/sucking.mp3"
ba "For a STALLION such as yourself, YES! Now stay hard and take me to the bed for some MORE SEX!"
scene barbarasuckcum05 with dissolve
mc "Sure, I'm still HARD and we can begin the night's entertainment STRAIGHT AWAY!"
ba "Mmmh, such a POWERFUL bull-stud!"

label BarbaraFuckChoicex:
stop music
scene barbarabed with dissolve
ba "I'm ready [name]. Ready for YOU and your MONSTERCOCK!"
label BarbaraFuckChoiceDialoguex:
menu:
    "As my teacher, your job is to give me a hand. job.":
        ba "Oh, my poor student needs some relief? Just sit on the edge of the bed and I'll take care of that giant teenage boner!"
        jump BarbaraHandjobx
    "What's your position on sexual harassment, teach?":
        ba "Well, I... err..."
        mc "On your back, that's what it is! Prepare your pussy for some deep harassment, Barbara!"
        ba "Oh my, that is definitely NOT in De Vos's education guide, but why not..."
        jump BarbaraMissionaryx
    "One good teaching method is to pummel something over and over until it sticks.":
        ba "Yes, where are you going with that?"
        mc "Your ass needs a lesson, that's where I'm going!"
        ba "So are you going to pummel it over and over again???"
        mc "You learn fast, teach!"
        jump BarbaraAnalx
    "How about some tender illicit-yet-totally-authorized-by-Patreon teacher-student love?":
        ba "Of course [name], give me a nice sensual massage then, I like those!"
        mc "Ah okay, I was thinking more along the lin..."
        ba "...of giving your teacher a nice massage if you want to get an A on your next test, right?"
        mc "Err, yeah, right."
        jump BarbaraMassagex
    "You taught us how to make babies during class. Now let's practice what I learnt!" if renpy.seen_image("barbarapreimpreg01a"):
        ba "Make sure you dump a big load in me then [name], I want this to be a success on the first go!"
        mc "And let's go to the sofa for a change for that scene."
        jump BarbaraImpregnationx
    "I'm done, let's go back to the gallery.":
        jump BarbaraGallery

label BarbaraHandjobx:
scene barbarahandjobbackground blurred
show barbaraprehandjob01
with dissolve
ba "It's ssoo BIG! But I know how to handle such a BEAST!"
mc "I can't wait to see that, I need some relief FAST, Barbara!"
hide barbaraprehandjob01
show barbaraprehandjob02
with dissolve
ba "Let me kiss it first... For good luck. *wink*"
window hide
play sound "Sounds/kiss.mp3"
$ renpy.pause(1.0, hard=True)
mc "Good luck for me or for you?"
ba "For you..."
hide barbaraprehandjob02
show barbaraprehandjob03
with dissolve
ba "So are you ready for my expert hand to jack your titanic dong off and relieve you?"
mc "I am, Barbara, I'm ain't sc..."
hide barbaraprehandjob03
play channel1 "Sounds/wank.mp3"
play channel2 "Sounds/moaning03.ogg"
hide barbaraprehandjob01
label BarbaraHandSlowx:
hide barbarahjfast
show barbarahjslow
call screen barbarahandslow01x
screen barbarahandslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraHandEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BarbaraHandFastx") 

label BarbaraHandFastx:
ba "This is really a nice workout for my right arm... Because this cock is so MASSIVE!"
mc "Oh God, that GRIP on my cock!"
hide barbarahjslow
show barbarahjfast
call screen barbarahandfast01x
screen barbarahandfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraHandEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BarbaraHandSlowx") 

label BarbaraHandEndx:
mc "Oh, I'm gonna cum if you keep that up!"
ba "DO IT! I want my favorite student to be able to focus in class and this is the only way! You MUST relieve yourself of all that pent-up semen!"
stop channel1
stop channel2
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
hide barbarahjslow
hide barbarahjfast
show barbara01handjobcum01
with fastdissolve
ba "That's it, shoot it out, keep going!"
window hide
with fastflash
mc "Barbara, oooh..."
hide barbara01handjobcum01
show barbara01handjobcum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Fuck, RHAAA!"
window hide
with fastflash
ba "It's so HOT and STICKY, I love it, give your teacher a MONSTERLOAD, [name]!"
hide barbara01handjobcum02
show barbara01handjobcum03
with fastdissolve
ba "Oh my dear President-for-Life, that what a magnificent display of CUM-BLASTING!"
mc "Phew, Barbara, I feel better now, like I can foc..."
hide barbara01handjobcum03
show barbara02hj00
with fastdissolve
ba "Who said we were done young man? I need you to TOTALLY EMPTY THOSE FAT NUTS!"
mc "Oh God, oh God..."
ba "Good luck..."
play channel1 "Sounds/wank.mp3"
play channel2 "Sounds/moaning03.ogg"
hide barbara02hj00
label BarbaraHand02Slowx:
hide barbara02hjfast
show barbara02hjslow
call screen barbara02handslow01x
screen barbara02handslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraHand02Endx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BarbaraHand02Fastx") 

label BarbaraHand02Fastx:
ba "Does it feel good [name]? Having your teacher wank your fat shaft like that with both hands, mmmh?"
mc "Damn, you're a real PRO Barbara! I can tell you've wanked many young cocks before..."
ba "Mmmh, that's because I'm such a NAUGHTY teacher!"
hide barbara02hjslow
show barbara02hjfast
call screen barbara02handfast01x
screen barbara02handfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraHand02Endx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BarbaraHand02Slowx") 

label BarbaraHand02Endx:
ba "I can feel your spermtube expanding, you're close to dumping ANOTHER great big fat load for your teacher, [name]?"
mc "Y... yeah, I'm CLOSE for sure!"
stop channel1
stop channel2
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
hide barbara02hjslow
hide barbara02hjfast
show barbara02handjobcum01
with fastdissolve
mc "That's it, I'm cumming AGAIN, RHAAA!"
window hide
with fastflash
ba "I can see that, at least an OUNCE of teenage virile seed is POURING out of your cumhole this time!"
hide barbara02handjobcum01
show barbara02handjobcum02
with fastdissolve
if persistent.cumsoundon:
    play channel1 "Sounds/cumming.mp3"
play sound "v08/wow.mp3"
ba "Wow, you had ssso much cum left in your great big cum-factories, didn't you?"
window hide
with fastflash
mc "Your hands are THAT good, AAAH!"
window hide
with fastflash
ba "I can see that, you're SPUNKING all over the place!"
stop channel1
hide barbara02handjobcum02
show barbara02handjobcum03
with fastdissolve
ba "I am totally drenched in your red-hot spunk [name]!"
play sound "Sounds/panting.mp3"
mc "Yeah, you made me cum BIG TIME, Barbara..."
ba "ooh, my poor boy, how are you going to get it up again after I've DRAINED you like that?"
mc "Don't you worry about that, teach! I can feel another hardon coming down my groin, so hop on the bed and get ready for some MORE!"
ba "Oooh my, what a STUD HAREM MASTER I have here!"
jump BarbaraFuckChoicex
    
label BarbaraMissionaryx:
$ barbaratoldfuckx = False
scene bedroom20
show barbarapremissionary01
with dissolve
ba "I'm in position... Of being fucked by your GIANT fuckpole!"
scene bedroom18 blurred
show barbarapremissionary02a
with dissolve
ba "Oh my God, it looks ssoo HEAVY!"
mc "Yeah, you think so?"
window hide
hide barbarapremissionary02a
show barbarapremissionary02b
with fastdissolve
play sound "Sounds/thud.mp3"
$ renpy.pause(.3, hard=True)
hide barbarapremissionary02b
show barbarapremissionary02a
with fastdissolve
$ renpy.pause(.3, hard=True)
hide barbarapremissionary02a
show barbarapremissionary02b
with fastdissolve
play sound "Sounds/thud.mp3"
$ renpy.pause(.3, hard=True)
hide barbarapremissionary02b
show barbarapremissionary02a
with fastdissolve
$ renpy.pause(.3, hard=True)
hide barbarapremissionary02a
show barbarapremissionary02b
with fastdissolve
play sound "Sounds/thud.mp3"
$ renpy.pause(.3, hard=True)
hide barbarapremissionary02b
show barbarapremissionary02a
with fastdissolve
$ renpy.pause(.3, hard=True)
hide barbarapremissionary02a
show barbarapremissionary02b
with fastdissolve
play sound "Sounds/thud.mp3"
$ renpy.pause(.3, hard=True)
hide barbarapremissionary02b
show barbarapremissionary02a
with fastdissolve
$ renpy.pause(.3, hard=True)
hide barbarapremissionary02a
show barbarapremissionary02b
with fastdissolve
play sound "Sounds/thud.mp3"
$ renpy.pause(.3, hard=True)
hide barbarapremissionary02b
show barbarapremissionary02a
with fastdissolve
$ renpy.pause(.3, hard=True)
mc "Now open your legs a bit wider..."
scene bedroom14
show barbarapremissionary03
with dissolve
play sound "Sounds/gasp.mp3"
mc "There you go, the head is in. Just need to ram the next 15 inches..."
ba "What? No, pl..."
scene bedroom17 blurred
play music "Sounds/fucksound.mp3"
label BarbaraMissionarySlowx:
scene bedroom18 blurred
show barbaramissionaryslow
call screen barbarapoundslow01x
screen barbarapoundslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraMissionaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BarbaraMissionaryFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("BarbaraCockSlowx") 

label BarbaraCockSlowx:
scene bedroom14 blurred
show barbaramissionarypovslow
call screen barbaracockslow01x
screen barbaracockslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraMissionaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BarbaraCockFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("BarbaraMissionarySlowx") 

label BarbaraMissionaryFastx:
if barbaratoldfuckx == False:
    ba "You're fucking your teacher so good [name].... AAAH, UUUH!"
    $ barbaratoldfuckx = True
scene bedroom18 blurred
show barbaramissionaryfast
call screen barbarapoundfast01x
screen barbarapoundfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraMissionaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BarbaraMissionarySlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("BarbaraCockFastx") 

label BarbaraCockFastx:
if barbaratoldfuckx == False:
    ba "You're fucking your teacher so good [name].... AAAH, UUUH!"
    $ barbaratoldfuckx = True
scene bedroom14 blurred
show barbaramissionarypovfast
call screen barbaracockfast01x
screen barbaracockfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraMissionaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("BarbaraCockSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("BarbaraMissionaryFastx") 
            
label BarbaraMissionaryEndx:
ba "Please give me your seed [name]! I NEED it! I want to feel it SPLASHING INSIDE ME!"
stop music
play music "v07/creampie.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene bedroom14 blurred
show barbaramissionarycum01
with fastdissolve
mc "Here it CO-O-MES!"
window hide
with fastflash
ba "I LOVE IT! Keep going, give your teacher a HEAVY NUTLOAD! COME ALL OVER ME NOW!"
scene bedroom17 blurred
show barbaramissionarycum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "RHAA, you asked for it teach!"
window hide
with fastflash
ba "You cumshots are so MASSIVE!"
hide barbaramissionarycum02
show barbaramissionarycum03
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Her's another one for you, AAAH!"
window hide
with fastflash
ba "My tits are covered are you're STILL shooting!"
scene bedroom14 blurred
show barbaramissionarycum04
with fastdissolve
play sound "Sounds/lick.mp3"
ba "Your plentiful cream tastes delicious... I hope you have a LOT more in store for me..."
mc "You want more?"
ba "YES I DO!"
mc "Then I'll fuck you some MORE and give you MORE cum!"
scene bedroom20 blurred
show barbarafuck00
with dissolve
ba "You...You've rammed your cum-covered dong BACK inside me!"
mc "That's right, teach, so I can FUCK YOU SOME MORE!"
hide barbarafuck00
play music "Sounds/womansex01.mp3"
label BarbaraFuckSlowx:
hide barbarafuckfast
show barbarafuckslow
call screen barbarafuckslow01x
screen barbarafuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BarbaraFuckFastx") 

label BarbaraFuckFastx:
ba "AAAh, you're a BEAST, [name]! I want you to FUCK ME FASTER AND DOUSE ME WITH ANOTHER MIGHTY LOAD!"
hide barbarafuckslow
show barbarafuckfast
call screen barbarafuckfast01x
screen barbarafuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BarbaraFuckSlowx") 

label BarbaraFuckEndx:
mc "I'm about to blow my load again, Barbara!"
ba "Oh my God, you're such a SEX GOD, with bullballs ALWAYS FULL TO THE BRIM!"
hide barbarafuckslow
hide barbarafuckfast
show barbarafuckcum01
with dissolve
stop music
play channel1 "v07/creampie.mp3"
play channel2 "Sounds/splooge02.mp3"
mc "Here it CO-O-MES!!!!"
window hide
with fastflash
ba "This feels amazing, I can feel every thick jet of your nasty scum shooting inside me! AAAH!"
window hide
with fastflash
mc "Wait for MORE MONSTER SHOTS THEN, RHAAA!"
hide barbarafuckcum01
show barbarafuckcum02
with fastdissolve
mc "LIKE THESE!!! OOOH!"
window hide
with fastflash
ba "I'm seeing stars! A+, A+!"
window hide
with fastflash
mc "I'm not done by a LONG SHOT, teach!"
stop channel1
stop channel2
scene bedroom34 blurred
show barbarafuckcum03
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "FU-UUU-CK!"
window hide
with fastflash
ba "That is indeed a LONG SHOT!"
window hide
with fastflash
mc "I want to pass with flying colors! AAAH!"
ba "You do, you do, you're my BEST STUDENT!"
scene bedroom14
show barbarafuckcum04
with fastdissolve
play sound "Sounds/panting.mp3"
ba "I am totally covered in your cum. There must be several ounces of it splashed everywhere..."
mc "Yeah... You almost drained me, Barbara. ALMOST."
ba "So does that mean I'm going to have MORE HOT SEX from my SUPER-HUNG stud student?"
mc "You bet, teach! Get cleaned up and I'll be right with you."
jump BarbaraFuckChoicex
    
label BarbaraAnalx:
scene bedroom37 blurred
show barbarapreanal01
with dissolve
ba "Please be gentle..."
mc "I'll be gentle, don't worry. As gentle as I can, forcing a soda can-thick cock into a tight rosebud."
scene bedroom17
show barbarapreanal02
with dissolve
ba "I can feel your monsterdick lodged between my asscheeks.... What did I let myself into?"
scene bedroom14
show barbarapreanal03
with dissolve
mc "This! One big fat ass-destroying truncheon!"
play music "Sounds/debrasex.mp3"
label BarbaraAnalSlowx:
scene bedroom18 blurred
show barbaraanalslow
call screen barbaraanalslow01x
screen barbaraanalslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BarbaraAnalFastx") 
    imagebutton:
        focus_mask True
        idle "v08/bottomview.png"
        hover "v08/bottomview.png"
        action Jump ("BarbaraAssSlowx") 

label BarbaraAssSlowx:
scene bedroom48 blurred
show barbaraassslow
call screen barbaraassslow01x
screen barbaraassslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BarbaraAssFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("BarbaraAnalSlowx") 

label BarbaraAnalFastx:
scene bedroom18 blurred
show barbaraanalfast
call screen barbaraanalfast01x
screen barbaraanalfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BarbaraAnalSlowx") 
    imagebutton:
        focus_mask True
        idle "v08/bottomview.png"
        hover "v08/bottomview.png"
        action Jump ("BarbaraAssFastx") 

label BarbaraAssFastx:
scene bedroom48 blurred
show barbaraassfast
call screen barbaraassfast01x
screen barbaraassfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("BarbaraAssSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("BarbaraAnalFastx") 
            
label BarbaraAnalEndx:
ba "Please give me your seed, I want it all INSIDE MY ASS!"
mc "Your wish is about to be..."
scene bedroom48 blurred
show barbaraanalcum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...FULFILLED, AAAH!"
window hide
with fastflash
ba "OOOh, my bowels are EXPLODING with cum! AAAH! Please pull out, I feel like I'm past breaking point [name]!!!"
scene bedroom12
show barbaraanalcum02
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Your ass is gripping so TIGHT on my shaft, it's MILKING my dong, AAAH!"
window hide
with fastflash
ba "I can't do anything about that, your pole is just so MASSIVE!"
scene bedroom32 blurred
show barbaraanalcum03
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH, that's better, I can let loose, RHAAA!"
window hide 
with fastflash
ba "My poor ass..."
scene barbarabed with dissolve
ba "After DESTROYING my ass, what could you possibly do to TOP THAT?"
jump BarbaraFuckChoiceDialogue
    
label BarbaraMassagex:
play channel1 "Sounds/michiko.mp3"
scene barbaramassage01 with dissolve
ba "I hope your hands are more delicate than your horsecock..."
mc "Just relax, teach. I'll remove all that Trumpster anger you've got built up inside you."
ba "You'd better not turn me into some woke socialist! If you do, I'll CANCEL you!"
scene barbaramassage02 with dissolve
mc "Just relax... And shut up."
window hide
$ renpy.pause(1.0, hard=True)
scene barbaramassage03 with dissolve
ba "Mmh, this is nice... But..."
window hide
play sound "Sounds/moaning.mp3"
$ renpy.pause(1.0, hard=True)
scene barbaramassage04a with dissolve
ba "Oooh, what are you doing?"
mc "This muscle also needs to be massaged..."
window hide
play channel2 "Sounds/moaning02.mp3"
scene barbaramassage04b with dissolve
scene barbaramassage04a with dissolve
scene barbaramassage04b with dissolve
scene barbaramassage04a with dissolve
scene barbaramassage04b with dissolve
scene barbaramassage04a with dissolve
scene barbaramassage04b with dissolve
scene barbaramassage04a with dissolve
scene barbaramassage04b with dissolve
scene barbaramassage04a with dissolve
scene barbaramassage04b with dissolve
scene barbaramassage04a with dissolve
scene barbaramassage04b with dissolve
scene barbaramassage05 with dissolve
stop channel2
play sound "Sounds/gasp.mp3"
ba "Oooh, I'm... getting so wet."
mc "That's your pelvic muscles relaxing... Turn round Barbara, I'll be able to reach even deeper inside yur pussy and REALLY help you relax..."
ba "Uh... Alright."
scene barbaramassage06 with dissolve
play sound "Sounds/moaning03.ogg"
ba "[name]! You're..."
mc "...Fingering your womb? Yeah, it's a technique I learnt from...err... The internet. Like before the war."
scene barbaramassage07 with dissolve
mc "And now you can taste your juices... It's the cycle of juice life."
play sound "Sounds/lick.mp3"
ba "Mmh... It's delicious actually. Thank you for this nice relaxing massage [name]!"
stop channel1
scene barbarabed with dissolve
ba "I'm so relaxed now, I could even take your cock up my ass."
mc "Err. That's good to know."
jump BarbaraFuckChoiceDialoguex

label BarbaraImpregnationx:
scene barbarapreimpreg01a with dissolve
ba "First, I need to really open up my womb... So that your cream can really FLOOD it to overfilling..."
mc "Go ahead... I'll watch and make sure I'm ROCKHARD for the impregnation process..."
scene barbarapreimpreg01b with dissolve
play music "Sounds/moaning02.mp3"
$ renpy.pause(0.3, hard=True)
scene barbarapreimpreg01a with fastdissolve
$ renpy.pause(0.3, hard=True)
scene barbarapreimpreg01b with fastdissolve
$ renpy.pause(0.3, hard=True)
scene barbarapreimpreg01a with fastdissolve
$ renpy.pause(0.3, hard=True)
scene barbarapreimpreg01b with fastdissolve
$ renpy.pause(0.3, hard=True)
scene barbarapreimpreg01a with fastdissolve
$ renpy.pause(0.3, hard=True)
scene barbarapreimpreg01b with fastdissolve
$ renpy.pause(0.3, hard=True)
scene barbarapreimpreg01a with fastdissolve
$ renpy.pause(0.3, hard=True)
scene barbarapreimpreg01b with fastdissolve
pause
stop music
ba "But I brought something better than my hand... My GREAT BIG WHITE DILDO!"
stop music
scene barbarapreimpreg02 with dissolve
ba "It's a full 14 inches long and super-THICK! It will stretch me out enough to be ready to take on YOUR great big white MONSTERCOCK!"
mc "Which, by the way, is even bigger. But carry on."
play channel1 "Sounds/moaning02.mp3"
play channel2 "Sounds/wank.mp3"
show barbaradildoslow
with dissolve
call screen barbaradildo01x
screen barbaradildo01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraDildoNextx")

label BarbaraDildoNextx:
hide barbaradildoslow
show barbaradildofast
with fastdissolve
stop music
play music "Sounds/stripmusic.mp3"
call screen barbaradildo02x
screen barbaradildo02x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraDildoEndx")

label BarbaraDildoEndx:
ba "AAAH,, I think I'm..."
stop channel1
stop channel2
scene barbarapreimpreg03 with dissolve
play sound "Sounds/moaning.mp3"
ba "..gonna SQUIRT!!!!"
play sound "Sounds/waterspray.mp3"
window hide
with fastflash
mc "Yeah, I think you're ready indeed... Let's DO IT!"
scene barbarapreimpreg04 with dissolve
ba "Mmh, that was good... Now I hope you can do even BETTER than my great big white dildo..."
mc "Of course! I'm BIGGER and I can spew hot sauce non-stop unlike this useless non-impregnating plastic toy...."
ba "Well then, come and show me... Come and IMPREGNATE your teacher [name]!"
play music "Sounds/womansex02.mp3"
label BarbaraPregnantSlowx:
hide barbaraimpregpovfast
hide barbaraimpregpovslow
show barbaraimpregslow
call screen barbarapregnantslow01x
screen barbarapregnantslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraPregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BarbaraPregnantFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("BarbaraImpregnateSlowx") 

label BarbaraImpregnateSlowx:
scene bedroom08 blurred
show barbaraimpregpovslow
call screen barbarapregnantsceneslow01x
screen barbarapregnantsceneslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraPregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BarbaraImpregnateFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("BarbaraPregnantSlowx") 

label BarbaraPregnantFastx:
hide barbaraimpregpovfast
hide barbaraimpregpovslow
show barbaraimpregfast
call screen barbarapregnantfast01x
screen barbarapregnantfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraPregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BarbaraPregnantSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("BarbaraImpregnateFastx") 

label BarbaraImpregnateFastx:
scene bedroom08 blurred
show barbaraimpregpovfast
call screen barbarapregnantscenefast01x
screen barbarapregnantscenefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraPregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("BarbaraImpregnateSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("BarbaraPregnantFastx") 
            
label BarbaraPregnantEndx:
ba "Are you ready to make a baby [name]? Are you ready to dump a great big WHITE load deep inside my tender teacher snatch?"
mc "I am teach, I'm ready!"
ba "Then DO IT!"
hide barbaraimpregpovslow
hide barbaraimpregpovfast
stop music
scene bedroom08 blurred
show barbaraimpregcum01
with dissolve
play music "Sounds/splooge02.mp3"
ba "Go on STUD! Pump my womb FULL OF VIRILE CREAM!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
window hide
with fastflash
hide barbaraimpregcum01
show barbaraimpregcum02
with fastdissolve
stop music
play sound "Sounds/splooge01.mp3"
ba "This is so good, I can even HEAR it splashing inside me [name]!"
window hide
with fastflash
ba "My stomach is SWELLING with your cum!"
stop music
hide barbaraimpregcum02
show barbaraimpregcum03
with dissolve
play sound "Sounds/panting.mp3"
ba "I'll make sure to keep as much seed inside me and not waste a single drop..."
mc "You really want to get pregnant, don't you teach?"
ba "Yes, and with a SUPERIOR baby. I'll get pregnant for sure now with the amount of cum you've dumped inside me..."
mc "My pleasure. I'm drained though, so it's time to go back to the gallery."
jump BarbaraGallery

