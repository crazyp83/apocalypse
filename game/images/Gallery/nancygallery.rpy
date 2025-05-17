label NancyGallery:
call screen gallerynancy
screen gallerynancy:
    add "Gallery/nancygallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("gallerynancy"), Jump ("MainGallery")]

    if renpy.seen_image("nancy11"):
        imagebutton:
            focus_mask True
            idle "Gallery/towngallery05.png" xpos 621 ypos 100
            hover "Gallery/towngallery05.png"
            action Jump ("NancyGallery01")

    if renpy.seen_image("nancy11") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("NancyGallery")

    if renpy.seen_image("nancytrain01"):
        imagebutton:
            focus_mask True
            idle "Gallery/nancygallery02.png" xpos 1050 ypos 100
            hover "Gallery/nancygallery02.png"
            action Jump ("NancyGallery02")

    if renpy.seen_image("nancytrain01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("NancyGallery")

    if renpy.seen_image("nancyshower01"):
        imagebutton:
            focus_mask True
            idle "Gallery/nancygallery03.png" xpos 1478 ypos 100
            hover "Gallery/nancygallery03.png"
            action Jump ("NancyGallery03")

    if renpy.seen_image("nancyshower01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("NancyGallery")

    if renpy.seen_image("nancysleeping"):
        imagebutton:
            focus_mask True
            idle "Gallery/nancygallery04.png" xpos 621 ypos 400
            hover "Gallery/nancygallery04.png"
            action Jump ("NancyGallery04")

    if renpy.seen_image("nancysleeping") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("NancyGallery")

    if renpy.seen_image("nancylingerie04"):
        imagebutton:
            focus_mask True
            idle "Gallery/nancygallery05.png" xpos 1050 ypos 400
            hover "Gallery/nancygallery05.png"
            action Jump ("NancyGallery05")

    if renpy.seen_image("nancylingerie04") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("NancyGallery")

    if renpy.seen_image("nancymcsleep"):
        imagebutton:
            focus_mask True
            idle "Gallery/nancygallery06.png" xpos 1478 ypos 400
            hover "Gallery/nancygallery06.png"
            action Jump ("NancyGallery06")

    if renpy.seen_image("nancymcsleep") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("NancyGallery")
            
    if renpy.seen_image("nancymarvel01"):
        imagebutton:
            focus_mask True
            idle "Gallery/nancygallery07.png" xpos 621 ypos 700
            hover "Gallery/nancygallery07.png"
            action Jump ("NancyGallery07")

    if renpy.seen_image("nancymarvel01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("NancyGallery")

    if renpy.seen_image("scarlettnancy01"):
        imagebutton:
            focus_mask True
            idle "Gallery/widowgallery03.png" xpos 1050 ypos 700
            hover "Gallery/widowgallery03.png"
            action Jump ("NancyGallery08")

    if renpy.seen_image("scarlettnancy01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("NancyGallery")

    if renpy.seen_image("mcmompool10"):
        imagebutton:
            focus_mask True
            idle "Gallery/nancygallery09.png" xpos 1478 ypos 700
            hover "Gallery/nancygallery09.png"
            action Jump ("NancyGallery09")

    if renpy.seen_image("mcmompool10") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("NancyGallery")

    add "Gallery/gallerygrid02.png"
    add "Gallery/textnancy.png"

label NancyGallery01:
scene nancycage01
mc "Damn, these people put women in cages, they really are barbarians. Or maybe just Republicans."
mc "Hang on a minute, I... recognize her... It's Nancy!"
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
mo "MMh, your landlady is VERY proud of you..."
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
jump NancyGallery

label NancyGallery02: 
scene gym06
show nancytrain01
mc "There's Nancy doing some crunches..."
hide nancytrain01
show nancygym
call screen nancygymx
screen nancygymx:
    add "Icons/nextidle.png"
    modal True
    button:
        xpos .91
        ypos .44
        xysize(140, 80)        
        action Jump ("NancyGymWorkoutEndx")

label NancyGymWorkoutEndx:
scene gym02
show nancygym01
mo "Oh, hi [name]! I wasn't expecting you here."
mc "I come here often to train Nancy, I need to get EVEN STRONGER!"
mo "And how are you going to do that?"
mc "By PUMPING over 2000lbs of iron!"
hide nancygym01
show nancygym02
with fastdissolve
mo "What? THAT MUCH? I want to see that..."
hide nancygym02
play music "Sounds/mcworkout.mp3"
call screen mcgym01m
screen mcgym01m:
    add mcgym01 at center
    modal True
    button:
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("GymWorkoutEnd01m")    

label GymWorkoutEnd01m:
stop music
scene machine01 with dissolve
mc "Damn, that was a good workout! I need to POSE and FLEX those muscles!"
scene gymposing02 with dissolve
mc "Fuck yeah! Monster teen muscle stud right here!"
scene gym03
show nancygym03
with dissolve
mo "I'm so proud of you [name]! You must be the STRONGEST boy on the planet!"
mc "Damn right Nancy! And I'll protect you from anyone who tries to kidnap you and sell you as a sex slave, I swear!"
hide nancygym03
show nancygym02
with fastdissolve
mo "I feel so SAFE with you around, you really have become the MAN of the house!"
mo "I'm off to take a shower now. And recover from all these EMOTIONS..."
jump NancyGallery

label NancyGallery03:           
play sound "Sounds/dream.mp3"
scene locker03dream
show nancyshower01
play music "Sounds/showerstrip.mp3"
mo "Oh [name], please help me! Free me from these horrible chains... And your landlady will do ANYTHING for you. \nAnd I mean ANYTHING."
mc "Of course mom, I'll break them apart with my SUPERMAN STRENGTH!"
hide nancyshower01    
show nancyshower02
mo "Wow, you did it with such ease, you are ssooo STRONG my sweet young tenant..."
mc "About that promise of yours..."
mo "Of course [name], I haven't forgotten..."
hide nancyshower02    
show nancyshower03                                            
mo "I bet your muscles are huge ALL OVER for your landlady?"
mc "Damn right, I'm hard as a rock for your smoking hot bod Nancy!"
hide nancyshower03
scene locker03 blurred
show nancyshower04
mo "Maybe you'd like to suckle on my big tits for starters?"
mc "Gimme, gimme your milk!"
scene lockernancytit01 with dissolve    
mo "I still have plenty of milk for my sweet man!"
mc "*slurp* Mmh, it tastes so good..."
scene lockernancytit02 with fastdissolve    
mo "I'm so happy to be FEEDING you! Get as much of my milk as you can, it will make you stronger!"
mc "Now it's time for ME to feed YOU! With some MEAT!"
scene lockernancy01 with dissolve
mo "I can barely fit the head in my mouth, you're so HUNG [name]!"
mc "Just let it slip down your throat, I'm sure you can do it!"
scene lockernancy02 with dissolve
mc "Fuck Nancy, you're DEVOURING my cock almost to the balls!"
mo "Glllurgg..."
mc "God, I'm so hard I need to FUCK you NOW!"
scene lockernancyfuck01 with dissolve
mo "And I'm so HORNY I want to ride that sweet massive manmeat till it explodes inside of my womb!" 
mc "Fuck, that's so dirty! And I'm a DIRTY BOY!"
scene lockernancyfuck02 with dissolve 
mo "Oh my God, your dick is like a tree trunk inside of my tender pussy, [name]! Fuck me HARD! FUCK YOUR LANDLADY!"
call screen nancygymdreamx
screen nancygymdreamx:
    add dreamnancygym at center
    modal True
    button:
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("DreamNancyGymEndx")    
label DreamNancyGymEndx:
scene lockernancycum01 with dissolve
mc "I'm EXPLODING inside you and dumping my load in your womb!"
mo "I can feel it [name], you're FLOODING it with your sweet sweet BOYCUM!"
scene lockernancycum02 with dissolve
mc "I can tell, it's dripping like crazy down my shaft and balls, you must be BLOATED with the stuff!"
mo "I am son and it feels ssoo good! Keep pumping your seed inside of me please!"
stop music
play music "Sounds/shower.mp3"
scene lockermccum01 with dissolve
mc "Yeah, take that Nancy! AAAH!"  
scene lockermccum02 with dissolve
mc "Damn, I made a right dreamy mess. I'd better clean all of it before I leave or people will think I'm a total pervert. Which I definitely AM NOT."
jump NancyGallery

label NancyGallery04:
scene bedroom01
show nancycountry01 with moveinleft
mo "I really need to sleep tight tonight, I have a lot of work tomorrow and my bunk roomies make too much noise..."
mc "No worries Nancy, the bed is all yours..."
mo "Thanks, I'll change into my night clothes then, turn around... You don't want to see your landlady all naked now do you?"
mc "Err, no, that would be totally inappropriate indeed..."
scene bedroom01 with fade
mo "You can turn round now [name]!"
show nancybedroom02
mo "That's all I have... I hope you don't mind."
mc "Not at all Nancy, you look...err... real nice in that... outfit."
hide nancybedroom02
show nancybedroom03
with fastdissolve
mo "Oh thanks [name], I was afraid it might be too revealing for you!"
mc "(actually, it IS revealing but she's smoking HOT in that outfit!)"
hide nancybedroom03
show nancybedroom04
with fastdissolve
mo "I hope I won't be too much of a bother. And that you don't snore..."
scene nancysleeping with fade
mc "She's sound asleep... Maybe I could have a peak at her ass..."
show nancyarse01
mc "Fuck yeah, Nancy has a nice tight muscular ass... Let's see her tits now."
show nancytits01
play sound "Sounds/womanmoan.mp3"
mc "Fuck yeah, she also has a huge rack..."
mc "I'd better go to sleep now, I have a long day ahead of me tomorrow..."
scene mcsleep02
play sound "Sounds/snoring.mp3"
pause 3
scene bedroom03 with fade
show nancywaking01
mo "AAh, I had a LOVELY night's sleep!"
hide nancywaking01
show nancywaking02
with fastdissolve
mo "Thank you so much for letting me stay here my sweet darling tenant! I'd better get dressed and go to work. Have a wonderful day, and don't do anything TOO dangerous!"
jump NancyGallery

label NancyGallery05:
scene bedroom01
show nancycountry01
mo "Oh, hello sweetie pie! You want to have some HOT loving with your landlady tonight?"
mc "Yeah, you're the hottest girl around Nancy!"
hide nancycountry01
show nancycountry04 with fastdissolve
mo "Oooh, that is such a SWEET thing to say to your landlady!"
mc "I have a lingerie set for you to try on!"
hide nancycountry04
show nancycountry05 with fastdissolve
mo "Really! Let me see!"
mc "Promise you'll wear it for me."
hide nancycountry05
show nancycountry01 with fastdissolve
mo "Of course my son! Anything for my sweet young boy!"
scene bedroom01 with fade
show nancylingerie04 at center with moveinright
mo "So, how do I look?"
mc "You look like a total MILF, Nancy!"
hide nancylingerie04
show nancylingerie01 with fastdissolve
mo "You mean you'd like to fuck your landlady [name]?"
mc "Damn right I'd like to!"
hide nancylingerie01
show nancylingerie02 with fastdissolve
mo "And would you like to fuck my nice tight ass?"
mc "Mmmh, let me have a closer look to think about that..."
scene bedroom01 blurred with fastdissolve
show nancylingerie03
mc "I made up my mind and it's a resounding \"YES\"!"
scene bedroom01 with fastdissolve
show nancylingerie05
mo "What about my big landlady titties?"
mc "Let's have a look at that too then..."
scene bedroom01 blurred with fastdissolve
show nancylingerie06
mo "They are so big and firm they could really PUMP that GIANT boymeat of yours [name]!"
mc "I see... That is definitely a plus in my books! I say let's do it Nancy!"
mo "Then get undressed son, I'll get out of this set too so you can REALLY fuck me!"
mo "I'll get out of this lingerie straight away so you can really fuck me!"
hide nancylingerie06
show nancynaked04
with dissolve
mo "There, much better. So what do you want us to do sweetie pie?"
jump NancyGallery

label NancyGallery06:
scene bedroom01
show nancynaked04
mo "So what do you want us to do sweetie pie?"
label NancyFuckChoicex:
stop music
menu:
    "Let's see how much of my giant fuckstick you can take in your pussy.":
        mo "I hope I can take a LOT of inches for you, [name]!"
        jump NancyFuckx
    "Let's fuck standing up.":
        mo "Ooh, you're gonna show me how STRONG you are [name]? I can't wait... Lift me up in your MUSCULAR arms and give me all you've got!"
        jump NancyLiftx   
    "I think my cock demands some serious tit-pumping.":
        mo "And my tits will be happy to oblige, [name]!"
        jump NancyTitsx
    "Let's dilate that sumptuous ass of yours Nancy.":
        mo "My ass? Oh, I thought you'd never ask sweetie pie! I LOVE a good anal pounding!"
        jump NancyArsex
    "The world needs to be re-populated. So I need to impregnate you." if renpy.seen_image("nancypreimpregnate00"):
        mo "Really? You want to have a baby with your landlady?"
        mc "Yeah, I'm into pregnancy and now that the dev has implemented it by popular demand, I want in!"
        jump NancyPregnantx
    "I'm done with this gallery":
        return

label NancyFuckx:
scene bedroom12 with dissolve
show mcnancyprefuck01
mo "Ooh, you look ssoo STUDLY my sweet boy!"
hide mcnancyprefuck01
show mcnancyprefuck02
mo "YES! Your fingers on my pussy are making me so wet..."
mc "Time to stick my stallion-sized cock up there then Nancy..."
scene bedroom12 with dissolve
play music "Sounds/fucksound.mp3"
label NancyFuckSlowx:
hide nancyfuckfast
show nancyfuckslow
call screen nancyfuckslow01x
screen nancyfuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("NancyFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("NancyFuckFastx") 

label NancyFuckFastx:
mo "Yes, you're fucking me so good [name]! But fuck her HARDER!"
mc "I will, while I play with those massive titties of yours!"
hide nancyfuckslow
show nancyfuckfast
call screen nancyfuckfast01x
screen nancyfuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("NancyFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("NancyFuckSlowx") 

label NancyFuckEndx:
hide nancyfuckslow
hide nancyfuckfast
stop music
show nancyfuckcum01 with fastdissolve
mc "Damn, I'm BLASTING my seed inside your pussy Nancy!"
hide nancyfuckcum01
show nancyfuckcum02
play sound "Sounds/cumming.mp3"
mo "Keep pumping that sweet young spunk till I'm bloated!"
mc "AAAH, I can't stop cumming, your pussy muscles are milking the cum out of my balls! RHAAA!"
mo "I'm full son, cover my tummy with the rest of your giant load!"
hide nancyfuckcum02
show nancyfuckcum03
play sound "Sounds/mccum.mp3"
mc "There you go, a full belly bukkake for you mom! OOOH!"
mo "Sweet Jesus, how much sweet young cream did you have stored up for your cum-hungry landlady?"
mc "Always a LOT for you Nancy! Let's have some more fun..."
jump NancyFuckChoicex

label NancyLiftx:
scene bedroom13 with dissolve
show nancyprelift01
mo "OOh, honey, you're ssoo MUSCULAR, and your solid fuckrod feels ssoo HUGE between my thighs..."
mc "And they are so tight, I can feel a LOT of friction on my shaft! Time to ease my fuckstick into something more comfy... Your DEEP PUSSY!"
hide nancyprelift01
show nancyprelift02
mo "Son! Your cock is absolutely MASSIVE! It's sticking way past my bumcheeks! How is it ever going to fit?"
mc "Don't worry mom, once you're up in the air, I'll have more space to stick it right up your fuckhole!"
mo "You're such a considerate tenant when you fuck your landlady [name]. I'm ready to get impaled, [name]!"
scene bedroom13 blurred with dissolve
play music "Sounds/fucksound.mp3"
label NancyLiftSlowx:
hide nancyliftfast
show nancyliftslow
call screen nancyliftslow01x
screen nancyliftslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("NancyLiftEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("NancyLiftFastx") 

label NancyLiftFastx:
hide nancyliftslow
show nancyliftfast
mo "Ooh, you lift me up so easily! You're so STRONG [name]... And you have such a MASSIVE cock for your landlady!"
call screen nancyliftfast01x
screen nancyliftfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("NancyLiftEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("NancyLiftSlowx") 

label NancyLiftEndx:
hide nancyliftslow
hide nancyliftfast
stop music
show nancyliftcum01
mc "Fuck yeah! I'm blowing my load inside your tight pussy! AAAH!"
mo "Ooh, you're really filling me up aren't you? Sssoo much sweet sweet cream from my studly tenant!"
hide nancyliftcum01
show nancyliftcum02
play sound "Sounds/cumming.mp3"
mc "You bet Nancy! Here, take some more ounces of my cream!"
mo "Ounces? Wow, you must be the BIGGEST CUMLOADER on the planet [name]! Give mommy all you've got please, [name]!"
hide nancyliftcum02
show nancyliftcum03
mc "Anything to please you Nancy! RHAAA!"
mo "Mmmh, sssoo much young virile spunk for your landlady..."
mc "Let's move on, I'm still rockhard and raring to go!"
jump NancyFuckChoicex

label NancyTitsx:
scene bedroom10 with dissolve
show nancypretits01
mo "Is that what you wanted [name]? My big alpha-radiated tits wrapped around your ALPHA-STUDCOCK?"
mc "Damn mom, they feel ssoo nice around my shaft..."
mo "Then let me do the pumping and enjoy the feeling..."
scene bedroom03b blurred with dissolve
play music "Sounds/wank.mp3"
label NancyTitSlowx:
hide nancytitfast
show nancytitslow
call screen nancytitslow01x
screen nancytitslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("NancyTitEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("NancyTitFastx") 

label NancyTitFastx:
mo "Mmh, look at that MONSTER shaft pummeling my cleavage! I'm gonna pump it HARD and FAST!"
hide nancytitslow
show nancytitfast
call screen nancytitfast01x
screen nancytitfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("NancyTitEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("NancyTitSlowx") 

label NancyTitEndx:
mo "Now BLAST your load all over my tits [name]!"
hide nancytitslow
hide nancytitfast
stop music
play sound "Sounds/mccum.mp3"
show nancytitcum01
mc "RHAAA! I can't hold it, your tits feel so good around my dong Nancy!"
mo "Wow, I can see that [name], you're cumming all over the place! MORE, MORE FOR YOUR LANDLADY!"
play sound "Sounds/cumming.mp3"
hide nancytitcum01
show nancytitcum02
mc "Ask and I shall deliver Nancy! Take that! AAAH!"
mo "Mmh, yes, PLASTER your virile seed all over my face and tits [name]!"
hide nancytitcum02
show nancytitcum03
play sound "Sounds/mccum.mp3"
mc "I'm cumming some more for you Nancy!"
mo "Your beast is EXPLODING and giving me a full cummy face mask!"
hide nancytitcum03
show nancytitcum04
mc "Phew, I don't think I ever came that much before in my life..."
mo "I'm so proud I'm the ONE who made you dump such a MASSIVE load then...  Let me slurp up all that warm offering... Are you still hard for me?"
mc "Of course Nancy! Let's do some more HOT loving!"
jump NancyFuckChoicex

label NancyArsex:
scene bedroom10 with dissolve
play music "Sounds/fucksound.mp3"
label NancyArseSlowx:
hide nancyarsefast
show nancyarseslow
call screen nancyarseslow01x
screen nancyarseslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("NancyArseEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("NancyArseFastx") 

label NancyArseFastx:
mo "Yes, fuck your landlady's ass HARDER, [name]!"
hide nancyarseslow
show nancyarsefast
call screen nancyarsefast01x
screen nancyarsefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("NancyArseEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("NancyArseSlowx") 

label NancyArseEndx:
mo "Please flood my ass with your cream [name]!"
stop music
scene bedroom10 blurred with dissolve
show nancyarsecum01 with fastdissolve
play sound "Sounds/mccum.mp3"
mc "CUMMING! RHAAA!"
mo "Oooh, I can feel every single MONSTER shot of your seed!"
hide nancyarsecum01
show nancyarsecum02
mc "There's more where that came from Nancy!"
mo "I don't doubt it, your nuts are so FULL and HEAVY with nice young boycum for your landlady, aren't they?"
hide nancyarsecum02
show nancyarsecum03
play sound "Sounds/cumming.mp3"
mc "Fuck YEAH! AAAH!"
mo "OOoh, you're filling up my ass with your HOT SPUNK!"
hide nancyarsecum03
show nancyarsecum04
mc "And I've got enough to cover your back too Nancy! SSOO GOOD! CUMMING SO FUCKING HARD!"
mo "Oh my God, you truly are a SUPER-STUD SON!"
mc "Phew, I'm still hard for some more HOT FUCKING..."
mo "I can't wait for what you have in store for me [name], I'm ssoo HORNY for my tenant's MASSIVE HORSEDICK!"
jump NancyFuckChoicex

label NancyPregnantx:
scene nancypreimpregnate00 with dissolve
mo "Come and suck on your my juicy tits, my sweet hung tenant..."
play sound "Sounds/slurp.mp3"
mc "*suck*"
mo "That's it, get some strength from my protein-filled boobie-milk... And now get on the floor, I'm gonna prep your cock up for the impregnation."
scene nancypreimpregnate01 with dissolve
mo "Ooh, look at you! Your great big monstercock demands attention from my tiny little feet..."
mc "Ooh, Nancy, I..."
mo "Just relax and enjoy sweetie pie. But don't come just yet!"
play channel1 "Sounds/wank.mp3"
play channel2 "Sounds/boymoan02.mp3"
label NancyPrePregSlowx:
hide nancyprepregfast
show nancyprepregslow
call screen nancyprepregslow01x
screen nancyprepregslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nextidle.png"
        action Jump ("NancyPrePregEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("NancyPrePregFastx") 

label NancyPrePregFastx:
mo "Your cock is getting sssooo stiff, sweetie! But I'll make it even STIFFER!"
hide nancyprepregslow
show nancyprepregfast
call screen nancyprepregfast01x
screen nancyprepregfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nextidle.png"
        action Jump ("NancyPrePregEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("NancyPrePregSlowx") 
        
label NancyPrePregEndx:
scene preimpregnate10b with fastdissolve
stop channel1
stop channel2
mo "Mmmh, I think it's as ROCK-HARD as it will get! You're positively LEAKING pre-cum all over my feet, honeypot!"
play sound "Sounds/boymoan.mp3"
mc "AAAh... AAAHH..."
scene preimpregnate11 with dissolve
mo "Now let your landlady slide down your GIANT BREEDING STALLION-COCK!"
play music "Sounds/massive.mp3"
show nancypregslow
label NancyPregSlowx:
hide nancypregfast
show nancypregslow
call screen nancypregslow01x
screen nancypregslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("NancyPregEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("NancyPregFastx") 

label NancyPregFastx:
mo "Go on [name], fuck me and BLAST your virile sperm inside me!"
hide nancypregslow
show nancypregfast
call screen nancypregfast01x
screen nancypregfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("NancyPregEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("NancyPregSlowx") 

label NancyPregEndx:
mc "I'm about to blow, mom!"
mo "Don't pull out and FILL ME UP then!"
stop music
scene nancyimpregnatecum01 with fastdissolve
play music "Sounds/splooge02.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAAH! I'm NUTTING INSIDE YOU LANDLADY!"
scene nancyimpregnatecum01 with flash
mo "Yes, I can feel it! I can feel your MASSIVE pellets of cum PLASTERING my womb! Sssoo goood, my studly tenant!"
$ pregmo = True
scene nancyimpregnatecum02 with dissolve
play sound "Sounds/cumming.mp3"
mc "RHAAAA!"
mo "Keep PUMPING that seed, sweetie pie!"
mc "I am, I'm PUMPING ALL OF IT! AAAH!"
scene nancyimpregnatecum02 with fastflash
mo "Ssso, sssoo much of it, my belly is SWELLING UP with your virile cum!"
stop music
scene nancyimpregnatecum03 with dissolve
stop sound
mo "You did REALLY well, my sweet boy. I'm sure you'll knock me up with such a MASSIVE LOAD!"
mc "*puff* I... gave you all of my cream..."
mo "I KNOW. You came like ONE THOUSAND MEN at least! Let's go to sleep so I can gently massage my womb and help your sperms swim towards their target..."
mc "That's a good idea."
jump NancyFuckChoicex

label NancyGallery07:
scene bedroom03b with fade
show nancynaked03b    
mc "Oh, by the way Nancy, I'd like to you to join the Avengers and become a SUPER-HERO like me!"
scene bedroom03 blurred with fastdissolve
show nancynaked01b
mo "What? But, sweetie, I'm no super-hero! I'm just a... normal woman with a SUPER-HERO tenant..."
mc "Well, it's probably genetic, which means that you have IT IN YOU mom! Especially if I give you the costume to go with it."
mo "What costume?"
mc "A Captain Marvel costume. I'm the new Captain America and you'll become the new Captain Marvel. Together with the Black Widow, we shall fight for FREEDOM and JUSTICE!"
hide nancynaked01b
show nancynaked02b
with fastdissolve
mo "Oh, honey, I think you saw too many Hollywood movies. The Avengers don't actually exist."
mc "Yes they DO! I saw the Black Widow, I mean, Scarlett Johannson on my...erm... adventures and she is gathering an army of super-fighters to topple President-for-Life Trumpf and restore democracy."
hide nancynaked02b
show nancynaked01b
with fastdissolve
mo "But i'm not really into politics. And I voted without thinking for Mr Trumpf anyway, like all the white soccer moms in our suburb, remember?"
mc "Well neither am I but it's the aim of the game, so you've got to help me Nancymom..."
hide nancynaked01b
show nancynaked04b
with fastdissolve
mo "Alright, mommy will do ANYTHING for her young sweet SUPER-HERO tenant! Show me that costume and we'll see if I fit into it..."
scene bedroom13 with fade
show nancymarvel01
mo "The material seems to be VERY stretchy, I managed to put it on."
mc "Yeah, it can expand too. I think it suits you great Nancy! Why don't you do a super-hero pose?"
mo "A super-hero pose? I'm not sure I know how to... I'll try."   
hide nancymarvel01
show nancymarvel02
with fastdissolve
mo "Like that? Does mommy look like a super-hero now?"
mc "Yeah mum, you do! A super-FIT super-HERO!"
hide nancymarvel02
show nancymarvel03
with fastdissolve
mo "I'm starting to like this costume, I feel like a different woman in it!"
mc "Turn round so I can see your bu... I mean back."
hide nancymarvel03
show nancymarvel04
with fastdissolve
mo "There, does it hug my curvy ass enough for you [name]?"
mc "It sure does Nancy!"
hide nancymarvel04
show nancymarvel05
with fastdissolve
mo "Oh my God, I can feel my breasts... they are growing! What's happening [name]?"
mc "Ah yes, I forgot to mention it's laced with highly-radioactive alpha-rays."
mo "Please do something about it [name], I just... keep growing... My muscles too! It's terrifying!"
scene bedroom13 blurred
show nancymarvel06
with fastdissolve
mo "The costume is going to burst if you don't find a way to stop it [name]! Please help me!"
mc "Maybe turn round so I can see if there is a way of removing the radiation..."
mo "Oh please, make it so!"
hide nancymarvel06
show nancymarvel07
with fastdissolve
"So, did you find anything [name]? Hurry up, my tits, they are still growing... even BIGGER than before!"
mc "Nope, can't say there's anything to see here... *Damn, her ass is also bigger and tighter!*"
mo "Maybe if I removed the costume, it will go away?"
mc "That's a good idea, get completely naked and we'll see if you remain a super-fit muscl... I mean, if those pesky alpha-radiations are gone or not."
scene bedroom13 with dissolve
show nancynaked05 with moveinright
mo "Oh no, I'm still HUGE and MUSCULAR!"
mc "Oh well, I guess you'll just have to get used to this new super-hero bo..."
mo "Hang on, I feel like I'm shrinking..."
hide nancynaked05
show nancynaked06
with fastdissolve
mc "* Damn you to hell dev!* "    
mo "Oh, thanks God I'm back to normal! I'm so relieved..."
mc "Yeah, that's...err... great news."
mo "We can finally go to sleep, safe in the knowledge that my body did NOT change and my muscles did NOT grow, and my tits did NOT..."
mc "Yeah yeah okay, we got the picture."
scene bedroom03 blurred with fade
show nancynaked03b
mo "It's probably best that mommy take a shower, she's covered in your virile cream..."
mc "Sure Nancy, I'll get in with you, I'm caked too. I come so much, it just flew everywhere..."    
hide nancynaked03b    
show nancynaked02b
with fastdissolve
mo "Alright son, but don't get any funny ideas. I really need to go to sleep after that shower..."
scene mcnancyshower                                                                                                                               
play music "Sounds/shower.mp3"
mo "What's that I feel on my back? You're STILL HARD after all this hot fucking we did [name]?"
mc "I'm ALWAYS hard for you Nancy!"
mo "Oh [name], mommy really needs to go to sleep, she has a lot of work to do tomorrow to feed everyone in the compound..."
mc "It's okay mom, I came enough times tonight to have a good night's sleep and SAVE THE WORLD tomorrow!"
mo "That's good my SUPER-HERO tenant!"
jump NancyGallery

label NancyGallery08:
$ momcum = 0
$ widowcum = 0
scene widowlair01
show widow02 at right with move
hide widow02
show widow07 at right
show nancymarvel08 at left with moveinleft
wi "Oh wow, your landlady looks AMAZING in that outfit! We definitely have a new Captain Marvel fighting alongside the AVENGERS!"
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
mc "It's part of the team bonding procedure that the Black Widow put in place Nancy. Just go with the flow."
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
mo "And what do you plan to achieve with that GIANT erect cock, [name]? This is no time for hanky-panky sweetie! I need HELP!"
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
label WidownancyHJSlowy:
hide widownancyhjfast
show widownancyhjslow
call screen widownancyhjslow01y
screen widownancyhjslow01y:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WidownancyHJEndy")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WidownancyHJFasty") 

label WidownancyHJFasty:
hide widownancyhjslow
show widownancyhjfast
mc "Yes, FASTER!"
call screen widownancyhjfast01y
screen widownancyhjfast01y:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WidownancyHJEndy")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WidownancyHJSlowy") 

label WidownancyHJEndy:
mc "Yes, you're making me cum! Get ready Nancy!"
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
mc "Keep still Nancy, I've got more ropes of cum to deliver flying right at you! AAAH!"
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
wi "Oh my God [name]! Your landlady... She's twirling her tongue on my pussy... Ooooh!"
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
label WidownancyFuckaSlowy:
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
call screen widownancyfuckaslow01y
screen widownancyfuckaslow01y:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckaEndy")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WidownancyFuckaFasty") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckbSlowy") 

label WidownancyFuckaFasty:
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
call screen widownancyfuckafast01y
screen widownancyfuckafast01y:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckaEndy")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WidownancyFuckaSlowy") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckbSlowy") 


label WidownancyFuckcSlowy:
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
call screen widownancyfuckcslow01y
screen widownancyfuckcslow01y:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckcEndy")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WidownancyFuckcFasty") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckdSlowy") 

label WidownancyFuckcFasty:
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
call screen widownancyfuckcfast01y
screen widownancyfuckcfast01y:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckcEndy")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WidownancyFuckcSlowy") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckdFasty") 

    
label WidownancyFuckbSlowy:
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
call screen widownancyfuckbslow01y
screen widownancyfuckbslow01y:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckbEndy")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WidownancyFuckbFasty") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckaSlowy") 

label WidownancyFuckbFasty:
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
call screen widownancyfuckbfast01y
screen widownancyfuckbfast01y:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckbEndy")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WidownancyFuckbSlowy") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckaFasty") 

label WidownancyFuckdSlowy:
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
call screen widownancyfuckdslow01y
screen widownancyfuckdslow01y:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckdEndy")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WidownancyFuckdFasty") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckcSlowy") 

label WidownancyFuckdFasty:
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
call screen widownancyfuckdfast01y
screen widownancyfuckdfast01y:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("WidownancyFuckdEndy")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WidownancyFuckdSlowy") 
    imagebutton:
        focus_mask True
        idle "Icons/switch.png"
        hover "Icons/switch.png"
        action Jump ("WidownancyFuckcFasty") 


label WidownancyFuckaEndy:
mo "You're pounding me so good sweetie pie, it's time for you to COME INSIDE ME!"
stop music
hide widownancyfuckaslow
hide widownancyfuckafast
show widownancyacum01
stop music
play sound "Sounds/cumming.mp3"
mc "I'm filling you up Nancy, AAAH!"
mo "AAAH, I can feel it PULSING inside me, I'm cumming with you!!!"
hide widownancyacum01
show widownancyacum02
mc "Take some more shots on your back, RHAAAA!"
mo "Oh my God sweetie pie, your loads... They are so BIG for me!"
mc "Phew... I'm still hard so I'm going to fuck you some more!"
mo "What? You're such a SUPER-STUD for me [name]. Fuck me again HARD!"
hide widownancyacum02
$ momcum += 1
jump WidownancyFuckcSlowy

label WidownancyFuckcEndy:
mo "You're pounding me so good sweetie pie, it's time for you to COME INSIDE ME!"
stop music
hide widownancyfuckcslow
hide widownancyfuckcfast
show widownancyccum01
stop music
play sound "Sounds/cumming.mp3"
mc "I'm filling you up mom, AAAH!"
mo "AAAH, I can feel it son, I'm cumming with you!!!"
hide widownancyccum01
show widownancyccum02
mc "Take some more shots on your back, RHAAAA!"
mo "Oh my God sweetie pie, AGAIN? You're just a CUM-MACHINE aren't you?"
$ momcum += 1
if momcum >= 2 and widowcum >= 2:
    jump WidownancyFuckAllEndy
mc "Phew... I'm still hard so I'm going to fuck you some more Nancy! Get ready for the pounding of your life!"
mo "Oh, I AM ready. Ready to take on my tenant's MONSTERCOCK once more!"
hide widownancyccum02
jump WidownancyFuckcSlowy

label WidownancyFuckbEndy:
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
    jump WidownancyFuckAllEndy
mc "Phew... I'm still hard so I'm going to fuck you some more Black Widow! Get ready to receive Captain's America's SUPERHERO cock!"
hide widownancywidowcumb03
if momcum == 1:
    jump WidownancyFuckdSlowy
if momcum == 0:
    jump WidownancyFuckbSlowy

label WidownancyFuckdEndy:
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
    jump WidownancyFuckAllEndy
mc "Phew... I'm still hard so I'm going to fuck you some more Black Widow! Captain America's superhero BULLBALLS are not done with you!"
wi "Oh my God, with such stamina, you could FUCK our enemies to DEATH Captain America!"
hide widownancywidowcumd03
if momcum == 1:
    jump WidownancyFuckdSlowy
if momcum == 0:
    jump WidownancyFuckbSlowy

label WidownancyFuckAllEndy:
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
jump NancyGallery

label NancyGallery09:
stop music
scene pool03
show mompool06
with dissolve
mo "Hi sweetie!"
mc "Hi Nancy! Nice to see you here again... In that hot NEW bikini."
hide mompool06
show mompool09
with fastdissolve
mo "I REALLY like it a LOT. It feels so comfortable and SEXY at the same time."
mc "SEXY is definitely the word I would use to describe it. ON YOU."
mo "And I like feeling SEXY for my harem Master! *wink*"
mc "Damn right! Turn round and show me that ass again, I'm getting a HARDON just looking at you..."
hide mompool09
show mompool08
with fastdissolve
mo "Like that my sweet tenant?"
mc "Fuck yeah! I'm going to bang that ass later this week like it's never been banged! Phew, I need to go for a swim to cool off now..."
mo "Don't cool off TOO much! *wink*"
mc "You know what? I 'm so fucking horny I'm gonna bang you right NOW!"
show mompool08
play music "v07/datemusic.mp3"
hide mompool08
show mompool09
with fastdissolve
mo "Right here? With the risk of people walking in on us?"
window hide
show mompool09 at right with move
show mcmompool10 at farleft with moveinleft
mc "The girl who was here with us just left... We have time for a quickie."
hide mompool09
show mompool10 at right
with fastdissolve
mo "Oh, my sweet tenant, you're such a naughty boy!"
hide mompool10
hide mcmompool10
show mcmompool11 
with dissolve
mc "So what do you say?"
mo "I... I don't know... I am kind of horny too... seeing you like this!"
scene pool03 blurred
show mcmompool12 
with dissolve
mc "Then get out of that tight bikini bottom and I'll give you a good pounding right away!"
mo "Ooooh, you're... so MANLY! I just want to kiss my studly landboy first..."
play sound "Sounds/kiss.mp3"
hide mcmompool12
show mcmompool13 
with dissolve
mc "I can't wait any longer, I NEED to fuck that tight ass of yours, Nancy!"
mo "My ass? Oh God, this is so dirty, anyone could just walk in on us and see me with your giant teenage cock stretching my poor little ass..."
mc "I guess you'll just have to try and keep the moaning down..."
hide mcmompool13
show mcmompool14a 
with dissolve
mc "Can you feel my dong slapping against your thighs, Nancy?"
window hide
hide mcmompool14a
show mcmompool14b
with fastdissolve
play sound "Sounds/slap.mp3"
hide mcmompool14b
show mcmompool14a
with fastdissolve
mo "Oh, honey, it's so HEAVY and BRUTAL! You're going to HAMMER it into me, aren't you?"
window hide
hide mcmompool14a
show mcmompool14b
with fastdissolve
play sound "Sounds/slap.mp3"
mc "Fuck yeah, so let's do it standing up, I just can't wait any longer..."
hide mcmompool14b
play music "Sounds/womansex01.mp3"
label NancyPoolSlowx:
hide nancypoolfast
show nancypoolslow
call screen nancypoolslow01x
screen nancypoolslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("NancyPoolEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("NancyPoolFastx") 

label NancyPoolFastx:
mc "I'm gonna make you moan louder now... By POUNDING IT FASTER!"
mo "Oh, sweetie pie, someone might hear us if you do th..."
play music "Sounds/womansex02.mp3"
hide nancypoolslow
show nancypoolfast
call screen nancypoolfast01x
screen nancypoolfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("NancyPoolEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("NancyPoolSlowx") 

label NancyPoolEndx:
mc "That's it, I'm close, Nancy..."
mo "Come inside me [name], I want to feel your warm sperm ERUPTING in my little pussy!"
stop music
hide nancypoolfast
hide nancypoolslow
show mcmompoolfuckcum01
with dissolve
play music "Sounds/splooge02.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH, GODDAMIT? this is sssooo GOOOD!"
window hide
with fastflash
mc "My cock is EXPLODING, that pussy is just the BEST!"
scene pool05 blurred
show mcmompoolfuckcum02
with dissolve
mo "YES! Keep pumping that seed, sweetie pie!"
window hide
with fastflash
mc "I'm gonna FILL YOU UP, AAHHH!"
scene pool03 blurred
show mcmompoolfuckcum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mo "My belly... It's SWELLING with your MONSTERLOAD!"
window hide
with fastflash
mc "That's cos you're making me cum BIG TIME, RHAAA!"
stop music
scene pool06 blurred
show mcmompoolfuckcum04
with dissolve
play sound "Sounds/splooge01.mp3"
mo "You came ssooo MUCH, honey pot... I hope nobody walks in on us with your seed POURING out of my stretched ass like that..."
mc "It does look rather lewd I agree. I think I'd better go for a swim to exonerate myself."
mo "And I'll just... wait for it to stop pumping out and then clean up the mess..."    
jump NancyGallery
