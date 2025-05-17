label TownGallery:
call screen gallerytown
screen gallerytown:
    add "Gallery/towngallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("gallerytown"), Jump ("MainGallery")]

    if renpy.seen_image("hammamcumend01"):
        imagebutton:
            focus_mask True
            idle "Gallery/towngallery01.png" xpos 621 ypos 100
            hover "Gallery/towngallery01.png"
            action Jump ("TownGallery01")

    if renpy.seen_image("hammamcumend01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("TownGallery")

    if renpy.seen_image("tattooparlor02"):
        imagebutton:
            focus_mask True
            idle "Gallery/towngallery02.png" xpos 1050 ypos 100
            hover "Gallery/towngallery02.png"
            action Jump ("TownGallery02")

    if renpy.seen_image("tattooparlor02") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("TownGallery")

    if renpy.seen_image("strippershow01"):
        imagebutton:
            focus_mask True
            idle "Gallery/towngallery03.png" xpos 1478 ypos 100
            hover "Gallery/towngallery03.png"
            action Jump ("TownGallery03")

    if renpy.seen_image("strippershow01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("TownGallery")

    if renpy.seen_image("strippercum01"):
        imagebutton:
            focus_mask True
            idle "Gallery/towngallery04.png" xpos 621 ypos 400
            hover "Gallery/towngallery04.png"
            action Jump ("TownGallery04")

    if renpy.seen_image("strippercum01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("TownGallery")

    if renpy.seen_image("nancy11"):
        imagebutton:
            focus_mask True
            idle "Gallery/towngallery05.png" xpos 1050 ypos 400
            hover "Gallery/towngallery05.png"
            action Jump ("TownGallery05")

    if renpy.seen_image("nancy11") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("TownGallery")

    if renpy.seen_image("heatherstrip07"):
        imagebutton:
            focus_mask True
            idle "Gallery/towngallery06.png" xpos 1478 ypos 400
            hover "Gallery/towngallery06.png"
            action Jump ("TownGallery06")

    if renpy.seen_image("heatherstrip07") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("TownGallery")

    if renpy.seen_image("heatherleathercum01"):
        imagebutton:
            focus_mask True
            idle "Gallery/towngallery07.png" xpos 621 ypos 700
            hover "Gallery/towngallery07.png"
            action Jump ("TownGallery07")

    if renpy.seen_image("heatherleathercum01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("TownGallery")

    add "Gallery/galleryfuture.png" xpos 1050 ypos 700

    add "Gallery/galleryfuture.png" xpos 1478 ypos 700

    add "Gallery/gallerygrid02.png"
    add "Gallery/texttown.png"

label TownGallery01:
scene hammam01
show hammamgirl01
hg "Welcome to Sulfurous Hammam!"
mc "That name doesn't sound very enticing..."
hide hammamgirl01
show hammamgirl02
hg "On the contrary, sulfur helps in the regeneration of radioactivity-ladden skin. I'll be taking a dip myself in a moment. Come and join me..."
scene hammam04 with dissolve
mc "So, what's a nice girl like you doing in a sulfurous place like this?"
hg "What a charmer..., And a naughty one at that, you're sporting a MASSIVE hardon! What if your friend sees us?"
mc "I'd say she's lost in the fog and we have enough time to get better acquainted..."
scene hammam05 with dissolve
hg "You mean better acquainted like that? With my tiny hand wrapped around your monster pole?"
mc "AAAH, yeah, just like that..."
play music "Sounds/wank.mp3"
hide hammamhandjobfast
show hammamhandjobslow
call screen hammamhandjobslowx
screen hammamhandjobslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HammamHandJobEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("HammamHandJobFastx") 

label HammamHandJobFastx:
hide hammamhandjobslow
show hammamhandjobfast
mc "Yes, faster! AAAHH!"
call screen hammamhandjobfastx
screen hammamhandjobfastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HammamHandJobEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("HammamHandJobSlowx") 

label HammamHandJobEndx:
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
scene hammamhandjob07
show hacum01
$ renpy.pause(0.06, hard=True)
scene hammamhandjob06
show hacum02
$ renpy.pause(0.06, hard=True)
scene hammamhandjob05
show hacum03
$ renpy.pause(0.06, hard=True)
scene hammamhandjob04
show hacum04
$ renpy.pause(0.06, hard=True)
scene hammamhandjob03
show hacum05
$ renpy.pause(0.06, hard=True)
scene hammamhandjob02
show hacum06
$ renpy.pause(0.06, hard=True)
scene hammamhandjob01
show hacum07
$ renpy.pause(0.06, hard=True)
scene hammamhandjob02
show hacum08
$ renpy.pause(0.06, hard=True)
scene hammamhandjob03
show hacum09
$ renpy.pause(0.06, hard=True)
scene hammamhandjob04
show hacum10
$ renpy.pause(0.06, hard=True)
scene hammamhandjob05
show hacum11
$ renpy.pause(0.12, hard=True)
scene hammamhandjob07
show hacum12
$ renpy.pause(0.06, hard=True)
scene hammamhandjob06
show hacum13
$ renpy.pause(0.06, hard=True)
scene hammamhandjob05
show hacum14
$ renpy.pause(0.06, hard=True)
scene hammamhandjob04
show hacum15
$ renpy.pause(0.06, hard=True)
scene hammamhandjob03
show hacum16
$ renpy.pause(0.06, hard=True)
scene hammamhandjob02
show hacum17
$ renpy.pause(0.06, hard=True)
scene hammamhandjob01
show hamcum01
$ renpy.pause(0.06, hard=True)
scene hammamhandjob02
show hamcum02
$ renpy.pause(0.06, hard=True)
scene hammamhandjob03
show hamcum03
$ renpy.pause(0.06, hard=True)
scene hammamhandjob04
show hamcum04
$ renpy.pause(0.06, hard=True)
scene hammamhandjob05
show hamcum05
$ renpy.pause(0.06, hard=True)
scene hammamhandjob06
show hamcum06
$ renpy.pause(0.06, hard=True)
scene hammamhandjob07
show hamcum07
$ renpy.pause(0.06, hard=True)
scene hammamhandjob06
show hamcum08
$ renpy.pause(0.06, hard=True)
scene hammamhandjob05
show hamcum09
$ renpy.pause(0.06, hard=True)
scene hammamhandjob04
show hamcum10
$ renpy.pause(0.06, hard=True)
scene hammamhandjob03
show hamcum11
$ renpy.pause(0.06, hard=True)
scene hammamhandjob02
show hamcum12
$ renpy.pause(0.06, hard=True)
show hamcum13
$ renpy.pause(0.06, hard=True)
stop music
scene hammamcumend01
hg "Oh my God, you cum like a STALLION!"
scene hammamcumend02
hg "But So soon?"
mc "Yeah, we don't have much time, and I want to FUCK YOU. Now my shaft is nice and slick, it will plough through your hole like BUTTER!"
hg "Oh, wow, you can just stay hard like that???"
mc "That's right, I'm the HERO of this game and I have UNLIMITED cum supplies in my balls!"
mc "Not like that wimp in Battle of the Bulges who can only nut like 5 times a day."
hg "O-kay. No idea what you're talking about, but please let me do the riding, I don't want you to destroy my poor pussy by being too rough."
mc "No worries, you go for a ride girl!"
scene hammamfuck with dissolve
label HammamFuckSlowx:
play music "Sounds/fucksound.mp3"
hide hammamfuckfast
show hammamfuckslow
call screen hammamfuckslowx
screen hammamfuckslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HammamFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("HammamFuckFastx") 

label HammamFuckFastx:
hide hammamfuckslow
show hammamfuckfast
call screen hammamfuckfastx
screen hammamfuckfastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HammamFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("HammamFuckSlowx") 

label HammamFuckEndx:
stop music
scene hammamfuckcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Damn, you're making me cum AGAIN! RHAAA!"
hg "What, it's OVERFLOWING my pussy, you had THAT MUCH left in you???"
mc "Yep, I have unlimited supplies in my alpha-radiated nuts!"
mc "But I'd better get back to my compound, it's getting late. We'll meet again hopefully, hammam girl!"
jump TownGallery

label TownGallery02:
scene tattooparlor02
tt "Now, where would you like your tattoo?"
mc "On my cock. It seems appropriate since it has a HUGE skin surface area to work on."
show tattooparlor02b
tt "Err, okay, that's a rather unusual request... But I'll do it, I'm curious..."
hide tattooparlor02b
tt "So get undressed then. And get hard cos I need to do it on distended skin! *wink*"
mc "Sure thing!"
scene tattoocock01 with dissolve
tt "Wow, that's a HUGE Road Warrior dong you have there!"
tt "I didn't know they could come THAT big! I never worked on such a MASSIVE fuckstick before..."
mc "Well go ahead, it's all yours."
scene tattoocock02 with dissolve
play music "Sounds/tattoodrill.mp3"
tt "Does it hurt?"
mc "Not a bit..."
scene tattoocock03 with fastdissolve
tt "It would be good if you stopped pumping all that pre-cum that's dripping down your shaft..."
mc "Oops, sorry, it has a mind of its own..."
tt "You can unload it AFTERWARDS."
scene tattoocock02 with fastdissolve
$ renpy.pause(2.0, hard=True)
stop music
tt "There, done!"
tt "And now..."
scene tattoocock04 with dissolve
tt "Pump your seed, give me as much as you can muster STUD!"
hide screen mcstats
hide screen calendar
label TattooHandJobSlowx:
hide tattoohandjobfast
show tattoohandjobslow
call screen tattoohandjobslowx
screen tattoohandjobslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TattooHandJobEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TattooHandJobFastx") 

label TattooHandJobFastx:
hide tattoohandjobslow
show tattoohandjobfast
call screen tattoohandjobfastx
screen tattoohandjobfastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TattooHandJobEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("TattooHandJobSlowx") 

label TattooHandJobEndx:
scene tattoohandjob01
show tattoocum01
mc "RHAAAA!"
tt "Yes, gimme, gimme, cover my apron in your thick load!"
scene tattoohandjob04 with fastdissolve
show tattoocum02
tt "Keep going! But ON my apron, not my FACE!"
mc "I AM! It's sssoo goood!"
scene tattoocum03 with fastdissolve
tt "That's better, I can lick it  up later that way...."
show tattoocum04
tt "Thanks for all that delicious cream Mr ROAD WARRIOR. Come back anytime, some Road Warriors have more than one tattoo!"
jump TownGallery

label TownGallery03:
stop music
scene stripclub01
play music "Sounds/strippermusic.mp3"
"And now, ladies and gentlemen, for your viewing pleasure, the \"Queen of the Blue Oyster\",\nthe \"Mother of Melons\", the distinguished... SUK-YU DONG!"
scene strippershow01 with dissolve
pause
scene strippershow02 with dissolve
pause
scene strippershow03 with dissolve
pause
scene strippershow04 with dissolve
pause
scene strippershow05 with dissolve
pause
scene strippershow06 with dissolve
mc "I can't stop myself from giving her five bucks... Those tits in my face..."
sy "Ooh, a fan I see..."
mc "SHUT UP AND TAKE MY MONEY!"
scene strippershow07 with dissolve
pause
scene strippershow08 with dissolve
pause
scene strippershow09 with dissolve
"And now, ladies and gentlemen, the \"Suk-Yu Dong Ping-Pong Show!\""
scene strippershow10 with dissolve
play sound "Sounds/plop.mp3"
pause
scene strippershow09 with dissolve
sy "Who wants to play? Catch the ball with your mouth if you can!"
mc "Me, me, me!"
sy "Get ready to catch it then!"
scene strippershow09 with dissolve
window hide
show angiecatch

play sound "Sounds/plop.mp3"
call screen strippercatch02b
screen strippercatch02b:
    modal True
    default time_left = 0.6
    
    add "deserttown/ballempty.png"
    if time_left <= 0.6:
        add "deserttown/ballcenter01.png"
    if time_left <= 0.4:
        add "deserttown/strippershow09.jpg"
        add "deserttown/ballempty.png"
        add "deserttown/ballcenter02.png"
    if time_left <= 0.2:
        add "deserttown/strippershow09.jpg"
        add "deserttown/ballempty.png"
        add "deserttown/ballcenter03.png"

    if time_left <= 0:
        timer .01 action Return
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)

scene strippercatchball with dissolve
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)
mc "Yeah, I caught it! I win!"
sy "Congratulations. But please give me my ping pong ball back. You can stick it back inside my pussy if you want... *wink*"
scene stripperballend with dissolve
sy "Ooh, yeah, put it back DEEP inside me. AAAH!"
mc "Damn, you're deep."
scene stripperkiss with dissolve
sy "For the winner... a kiss."
jump TownGallery

label TownGallery04:
stop music
scene stripclub01
play music "Sounds/strippermusic.mp3"
"And now, ladies and gentlemen, for your viewing pleasure, the \"Queen of the Blue Oyster\",\nthe \"Mother of Melons\", the distinguished... SUK-YU DONG!"
scene strippershow01 with dissolve
pause
scene strippershow02 with dissolve
pause
scene strippershow03 with dissolve
pause
scene strippershow04 with dissolve
pause
scene strippershow05 with dissolve
pause
scene strippershow06 with dissolve
mc "I can't stop myself from giving her five bucks... Those tits in my face..."
sy "Ooh, a fan I see..."
mc "SHUT UP AND TAKE MY MONEY!"
scene strippershow07 with dissolve
pause
scene strippershow08 with dissolve
pause
scene strippershow15 with dissolve
"And now, ladies and gentlemen, the \"Suk-Yu Dong King-Kong Dong Show!\""
scene strippershow16 with dissolve
pause
scene strippershow17 with dissolve
pause
scene strippershow18 with dissolve
pause
sy "Is there anyone in the assistance who thinks he's big enough to replace this King-sized dildo?"
mc "Me, me, me!"
sy "Oooh, you again [name]. Alright, let's see what you have... Hop onto the stage."
window hide
play sound "Sounds/applause.mp3"
$ renpy.pause(1.0, hard=True)
scene stripperprefuck01 with dissolve
sy "Your young manhood certainly looks like it could be as BIG as my King-Kong dildo..."
mc "And it can get yet HARDER and BIGGER."
sy "Then GET hard so I can compare the two and see if you can replace it..."
scene stripperprefuck02 with dissolve
sy "Wow, look at that MASSIVE fuckstick. Even LARGER than my 16-inch MONSTER pussy-plugger!"
mc "Yep, that's me."
sy "Lie down on your back and I'll IMPALE MYSELF on your GIANT lovesword!"
mc "That's why they call me \"[name] the Impaler\"..."
scene stripperprefuck03 with dissolve
sy "Let me just spread my pussylips wider... And here we go!"
label StripperFuckSlowx:
hide stripperfuckfast
show stripperfuckslow
call screen stripperfuckslow01x
screen stripperfuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("StripperFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("StripperFuckFastx") 

label StripperFuckFastx:
mc "Oh god, impale yourself on my shaft even FASTER Suk-Yu!"
sy "Ooh, YES! I can see where you got your nickname from!"
hide stripperfuckslow
show stripperfuckfast
call screen stripperfuckfast01x
screen stripperfuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("StripperFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("StripperFuckSlowx") 

label StripperFuckEndx:
sy "Fill me up with cum [name]!"
scene strippercum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
sy "Ooh, that's good, I've been missing that..."
play music "Sounds/splooge01.mp3"
scene strippercum01 with fastflash
mc "AAAH! My nuts are EXPLODING!"
scene strippercum02 with dissolve
sy "You're making such a MESS..."
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
scene strippercum02 with fastflash
mc "That's cos I can't stop CUMMING! RHAAA!"
stop music
stop sound
play sound "Sounds/panting.mp3"
scene strippercum03 with dissolve
sy "I'll just have to clean your cock now... Mmmh, your seed is DELICIOUS!"
mc "Alpha-radiated cum tastes like chicken, I've been told."
scene strippercum04 with dissolve
sy "Now that we're abone, I'b got to tell you... *lick*"
mc "Try and speak slowly Suk-Yu... You've got a mouth full of cum..."
sy "Biamonb's weak point is... BIAMONBS."
mc "You mean \"diamonds\"?"
sy "Bes..."
mc "Interesting... Thanks for the tip, Suk-Yu."
sy "You're belcome."
jump TownGallery

label TownGallery05:
scene nancycage01
mc "Damn, these people put women in cages, they really are barbarians. Or maybe just Republicans."
mc "Hang on a minute, I... recognize her... It's NANCY!"
scene nancycage02 with dissolve
mo "[name]! Is that you? Oh my God, I thought you were dead! My sweet, sweet tenant!"
mc "Nancy! I thought you were dead too! What happened to you?"
mo "I... ended up here, I was kidnapped by a gang of horrible people who sold me as a slave! Please get me out of here, I beg you!"
mc "Of course Nancy, you can count on me!"
scene market02
show slaver01b
with dissolve
mc "I'd like to inspect the merchandise please."
sl "Of course. I'll get her out of her cage so you can inspect her better."
hide slaver01b
show nancy01 at midleft with dissolve
show slaver02b at midright with dissolve
sl "See? She is in perfect condition... 32DDD-24-36. A bit of mileage of course, she's an '87 MILF model. But ain't she a beauty, sir?"
mc "Ahem... Sure, sure... What about the back?"
sl "Oh, you won't be disappointed my friend, she's got one fine booty. Turn around slave!"
hide nancy01
show nancy02 at midleft
hide slaver02b
show slaver01b at midright
sl "Not a scratch, nothing. And only 200 new Dollars for this top notch quality product. What do you say, sir?"
mc "Not bad, but I'd like to check out the nipples. I'm a nipple man you see..."
sl "Whatever rocks your boat Sir. Get your top off for the nice customer slave!"
hide nancy02
show nancy03 at midleft
sl "Don't hesitate to step closer sir, so you can better inpect those funbags... Best in town, 100\% customer satisfaction guaranteed!"
hide slaver01b
scene market02 blurred
hide nancy03
show nancy04 with fastdissolve 
mc "Yes, yes, I see better the quality of the product now..."                
scene market02
show slaver01b at midright
show nancy03 at midleft                                
mc "Okay, you convinced me, I'll buy her!"
hide slaver01b
show slaver03b at midright
sl "Excellent purchase my friend! I'll wrap her up for you. Is it a present?"
mc "Err... No, it's to go."
hide slaver03b
show slaver02b at midright
sl "Fine sir, then she's all yours, here are the keys. To the collar."
scene market01
show cageempty
show nancy06 with dissolve
mo "[name], thank you SSOO much for saving me from this horrible place!"
hide nancy06
show nancy07 with fastdissolve
mo "My, you have grown so... MANLY..."
mc "Err, yeah, I received a ton of alpha-radiations, I'm a total alpha-STUD now!"
mo "MMh, Nancy is VERY proud of you..."
mc "Well, you're super-BUFF too Nancy! Wow!"
hide nancy07
show nancy08 with fastdissolve
mo "Ye, I was caught in the same alpha-radiation pocket as you I think. Oh honey, I looked for you for days, I left you for dead, I'm so sorry!"
mc "It's okay Nancy, I survived as you can see."
mc "What about your husband? Did you find him?"
hide nancy08
show nancy09 with fastdissolve
mo "Oh, he was downtown when the nuke fell on Springfield, there's no way he could have survived..."
mo "You're the MAN of the house now [name]..."
hide nancy09
show nancy10 with fastdissolve
mo "Now please [name], take this collar off me, I feel so cheap wearing it!"
mc "Sure Nancy, I've got the keys since I...err... own you."
mo "Don't talk like that please [name]..."
hide nancy10
show nancy11 with fastdissolve
mo "Oh, I feel so much lighter! Now let's leave this God-forsaken place!"
mc "Sure Nancy, I'll take you back to the compound where I live straight away!"   

scene command01 with fade
show lena01
le "So, what do you have to report about area C5 scouts?"
mc "I found my landlady, she survived!"
hide lena01
show lena03
with fastdissolve
le "What? So she wasn't killed by President-for-Life Trumpf then?"
mc "Nope. And I brought her back here, cos she was a slave and she has nowhere to live."
window hide
show lena03 at midright with move
show nancyinside01 at midleft with moveinleft
hide lena03
show lena02 at midright
le "Ah. Err, that's fantastic! For YOU."
mc "I'm sure you can find her a job so she can be useful to the compound. I know she's a great cook!"
le "Sure... She can be a cook if you insist then. We should also find her some clothes... Cos she can't walk around the compound like that."
hide nancyinside01
show nancyinside02 at midleft
mo "Oh thank you so much! I won't disappoint you I promise! [name] told me so many nice things about this place and...you!"
hide lena02
show lenapensive at midright
le "Well, we do have some spare clothes lying around... Suki will show you."
hide nancyinside02 with moveoutleft
hide lenapensive
show lena01 at midright
le "She'll have to sleep in bunks though, we cannot spare a luxury room for a woman, even if she is your landlady..."
show nancycountry01 at midleft with moveinleft
mc "These clothes look great on you mom!"
le "Well, I'll let you show her around, I have to go back to WORK, managing a compound with yet ANOTHER person in it."
mc "Come with me, I'll show you my room, it's top ace!"
scene bedroom01 with fade
show nancycountry02 with moveinright
mo "Oh [name], I'm so proud of you, you're becoming a HERO in this compound to have such a BIG bedroom!"
mc "Yeah, I AM the HERO actually Nancy!"
scene bedroom03b
show nancycountry03 with fastdissolve
mo "I sure would LOVE to have such a comfy bed... Especially after having slept in a cage for MONTHS..."
mc "Well, you're always welcome to come and sleep here, and I'll sleep... on the floor."
mo "Oh, I recognize my SWEET SWEET tenant!"
mc "Come, I'll show you the gym where I train to get even STRONGER!"
mo "I can't wait!"
scene machine01 with fade
show nancycountry02 at midright with dissolve
mc "I use these weights. They're over 2000lbs and I can do hundreds of reps with them."
mo "Oh my God, you are sssooo STRONG!"
mc "I wonder how much YOU can benchpress..."
hide nancycountry02
show nancycountry01 at midright with fastdissolve
mo "I don't know either, I never had the CHANCE to try... Maybe I'll come and use this gym in my spare time!"
mc "(Fuck yeah... So I can have a SEX dream sequence in the locker room with her...)"
mc "I think I need to go back to the command center now, I'll let you discover your new job in the kitchen...yourself. Cos there's no useless eating sequences in this game."
mo "Of course son, I think I can handle myself. Thanks a bunch for being such a SWEET boy to your landlady!"
jump TownGallery

label TownGallery06:
scene stripclub01h
play music "Sounds/strippermusic.mp3"
"And now, ladies and gentlemen, for your viewing pleasure, the \"New Queen of the Blue Oyster\",\nthe \"Mother of Balloons\", the young kinky... HEATHER!"
scene heatherstrip01 with dissolve
pause
scene heatherstrip02 with dissolve
pause
scene heatherstrip03 with dissolve
pause
scene heatherstrip04 with dissolve
pause
scene heatherstrip05 with dissolve
pause
scene heatherstrip06 with dissolve
mc "I can't stop myself from giving her five bucks... Those tits in my face..."
he "Ooh, my BIGGEST fan here... *wink*"
mc "SHUT UP AND TAKE MY MONEY!"
"And now, ladies and gentlemen, Heather will demonstrate her acrobatic skills. With a chair!"
play sound "Sounds/applause.mp3"
pause
scene heatherstrip07 with dissolve
pause
scene heatherstrip08 with dissolve
pause
scene heatherstrip09 with dissolve
pause
scene heatherstrip10 with dissolve
pause
scene heatherstrip11 with dissolve
pause
scene heatherstrip12 with dissolve
"Thank you for watching the show and a round of applause for our new sensation... HEATHER!"
window hide
play sound "Sounds/applause.mp3"
stop music
scene heatherstripkiss with dissolve
play sound "Sounds/kiss.mp3"
he "And a special thank you to YOU. *kiss*"
play sound "Sounds/kiss.mp3"
jump TownGallery

label TownGallery07:
play music "Sounds/strippermusic.mp3"
scene heatherleather01 with dissolve
pause
scene heatherleather02 with dissolve
pause
scene heatherleather03 with dissolve
pause
scene heatherleather03b with dissolve
he "You might be wondering why I've been wearing this crotchless leather outfit... Here's the reason!"
window hide
play sound "Sounds/applause.mp3"
$ renpy.pause(2.0, hard=True)
scene heatherleather05 with dissolve
play sound "Sounds/moaning02.mp3"
pause
scene heatherleather04 with dissolve
pause
scene heatherleather06 with dissolve
play sound "Sounds/moaning03.ogg"
he "It's nice... But not BIG enough..."
pause
stop sound
scene heatherleather07 with dissolve
he "Is there anyone in the audience with a BIG cock who's ready to come and FUCK this pussy real good in front of EVERYONE?"
scene heatherleather08 with dissolve
he "What about you [name]? I KNOW you have a really HUGE cock for me... *wink*"
mc "Damn right and I'll show you what it can do to a tight pussy!"
stop music
scene heatherleatherprefuck01 with dissolve
stop music
play sound "Sounds/audiencegasp.mp3"
he "Hear them gasp [name]? That's cos they are MIGHTY impressed by that hard horsecock of yours... Bring it over..."
scene heatherleatherprefuck02 with dissolve
play sound "Sounds/applause.mp3"
he "I'm going to have a LOT of fun coaxing a GIANT load out of those boulders... You have a lot of cum for me [name]?"
mc "Fuck yeah, plenty to satisfy you, Heather!"
he "Just imagine the people's faces in this room when they see your cum-missile unloading its mighty load all over poor little me..."
mc "You're... such a TEASE, Heather!"
scene heatherleatherprefuck03 with dissolve
he "You want me to stop teasing you? Then come and fuck this pussy real HARD, donkey-dicked boy!"

play music "Sounds/barbarasex.mp3"
label LeatherFuckSlowx:
hide leatherfuckfast
show leatherfuckslow
call screen leatherfuckslow01x
screen leatherfuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LeatherFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LeatherFuckFastx") 

label LeatherFuckFastx:
he "Aaah, this is so HOT, I LOVE getting fucked by a horse-hung guy in front of everyone like that!"
mc "You like that dick you dirty little stripper, hey?"
he "Ooh, yeah, it's so good DEEP in my pussy like that. Fuck me FASTER, show these people what you're made of, STUD!"
hide leatherfuckslow
show leatherfuckfast
call screen leatherfuckfast01x
screen leatherfuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LeatherFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LeatherFuckSlowx") 

label LeatherFuckEndx:
he "Are you going to blow your load [name]? I want you to pump it inside my pussy... To OVERFILLING!"
mc "Aah, jut a sec...."
stop music
scene heatherleathercum01 with dissolve
play music "Sounds/splooge02.mp3"
play sound "v07/creampie.mp3"
mc "Oh, FUCK!"
with fastflash
he "BLAST THAT NASTY TEENAGE SPUNK! AAAAH!"
scene heatherleathercum02 with dissolve
mc "RHAAA, CAN'T STOP CUMMING!"
with fastflash
he "I'm getting pumped full of cum in public, OOH-UUUHHH!"
stop music
stop sound
scene heatherleathercum03 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Let them see these cumshots too then, FU-UUU-CCCKKK!"
with fastflash
he "You're STILL spewing? This is so NASTY!"
scene heatherleathercum04 with dissolve
play sound "Sounds/applause.mp3"
he "Oooh, [name], you made such a nasty mess... In front of all these people watching us FUCK... It's sssoo kinky..."
mc "I had to show them what I'm made of, just like you said..."
he "You've proven to them than you are a true Road Warrior STALLION!"
scene heatherleathercum05 with dissolve
play sound "Sounds/sucking.mp3"
he "And you've reminded me how TASTY your spunk is... *slurp*"
he "Now off you go, I have to get myself ready for my NEXT show! *wink*"
jump TownGallery
