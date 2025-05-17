label LenaGallery:
call screen gallerylena
screen gallerylena:
    add "Gallery/lenagallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("gallerylena"), Jump ("MainGallery")]

    if renpy.seen_image("lenagym03"):
        imagebutton:
            focus_mask True
            idle "Gallery/lenagallery01.png" xpos 621 ypos 100
            hover "Gallery/lenagallery01.png"
            action Jump ("LenaGallery01")

    if renpy.seen_image("lenagym03") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("LenaGallery")

    if renpy.seen_image("lenashower01"):
        imagebutton:
            focus_mask True
            idle "Gallery/lenagallery02.png" xpos 1050 ypos 100
            hover "Gallery/lenagallery02.png"
            action Jump ("LenaGallery02")

    if renpy.seen_image("lenashower01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("LenaGallery")

    if renpy.seen_image("fightlenawin"):
        imagebutton:
            focus_mask True
            idle "Gallery/lenagallery03.png" xpos 1478 ypos 100
            hover "Gallery/lenagallery03.png"
            action Jump ("LenaGallery03")

    if renpy.seen_image("fightlenawin") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("LenaGallery")

    if renpy.seen_image("lenagymlingerie02"):
        imagebutton:
            focus_mask True
            idle "Gallery/lenagallery04.png" xpos 621 ypos 400
            hover "Gallery/lenagallery04.png"
            action Jump ("LenaGallery04")

    if renpy.seen_image("lenagymlingerie02") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("LenaGallery")

    if renpy.seen_image("lenadate01"):
        imagebutton:
            focus_mask True
            idle "Gallery/lenagallery05.png" xpos 1050 ypos 400
            hover "Gallery/lenagallery05.png"
            action Jump ("LenaGallery05")

    if renpy.seen_image("lenadate01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("LenaGallery")

    if renpy.seen_image("lenamclingerie03"):
        imagebutton:
            focus_mask True
            idle "Gallery/lenagallery06.png" xpos 1478 ypos 400
            hover "Gallery/lenagallery06.png"
            action Jump ("LenaGallery06")

    if renpy.seen_image("lenamclingerie03") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("LenaGallery")
    
    if renpy.seen_image("lenajakelingerie01"):
        imagebutton:
            focus_mask True
            idle "Gallery/lenagallery07.png" xpos 621 ypos 700
            hover "Gallery/lenagallery07.png"
            action Jump ("LenaGallery07")

    if renpy.seen_image("lenajakelingerie01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("LenaGallery")


    add "Gallery/galleryfuture.png" xpos 1050 ypos 700

    add "Gallery/galleryfuture.png" xpos 1478 ypos 700

    add "Gallery/gallerygrid02.png"
    add "Gallery/textlena.png"

label LenaGallery01:
scene gym02
show lenagym01
le "Hi [name], I was about to do some pull-ups... Wanna watch?"
mc "Sure chief..."
scene gym02
call screen lenagymx
screen lenagymx:
    add "lenagym"
    add "Icons/nextidle.png"
    modal True
    button:
        xpos .91
        ypos .44
        xysize(140, 80)        
        action Jump ("LenaGymWorkoutEndx")

label LenaGymWorkoutEndx:
scene gym02 with dissolve
show lenagym02
le "I'm glad to see that you use our gym. We want you to become as strong as possible to defeat our enemies!"
mc "I was just passing by really, like visiting to see what's on offer."
hide lenagym02
show lenagym03
le "Oh. Well, as you can see, there is some very good equipment for a man like you to pump iron."
le "Notably, a titanium-barbell that can support over 2000lbs of steel plates. You should train with these... You look like you could be capable of lifting such heavy weights..."
mc "Sure, I'll try one day. But right now, I have others things to do."
hide lenagym03
show lenagym01
le "Fine. But don't forget to train HARD before you PLAY hard! (wink)"
jump LenaGallery

label LenaGallery02:
play sound "Sounds/dream.mp3"
scene locker03dream
show lenashower01
play music "Sounds/showerstrip.mp3"
le "Well, hello [name]. I was just about to take a shower myself..."
mc "Then why don't you join me Chief Lena!"
hide lenashower01    
show lenashower02
le "Of course I will, but first I have to get totally undressed..."
mc "What a fine body you have Chief!"
le "That's why I'm the Chief..."
hide lenashower02    
show lenashower03                                            
le "Oh my, [name]. Your cock is sssooo much bigger than Jake's. He's a toddler next to you."
mc "Fuck yeah, I'm da REAL man here!"
hide lenashower03
scene locker03 blurred
show lenashower04
le "Show me what you can do with your mighty love sword STUD!"
mc "I'll impale you on it Chief! Then you'll feel the power of a REAL man, not a wimp like your pindick hubby!"
le "Ooooh, you're ssoo manly! But first, I want to lick your shaft EVERYWHERE!" 
scene lockerlena01    
mc "There you go Chief, can you feel how hard I am for you?"
le "You're so BIG! I've never been with a man as virile as you! I want to suck it NOW!"
scene lockerlenasuck01 with dissolve
le "You're doing good Lena... But let me feed you a few more inches to see how GREAT a cocksucker you can be!"
scene lockerlenasuck02 with dissolve
mc "That's it, all the way down your throat!"
le "Glllurgg..."
scene lockerlena02 with dissolve
mc "And now for the main course... Your tight pussy!"
le "It's so thick [name]! You're such a MEGA-stud!"  
scene lockerlena02a with dissolve 
le "AAAH! Your giant love muscle is pulsating inside me and making me cum like crazy!"
mc "Take it Chief Lena, take ALL of it! RHHAAA!"
call screen lenagymdreamx
screen lenagymdreamx:
    add dreamlenagym at center
    modal True
    button:
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("DreamLenaGymEndx")    
label DreamLenaGymEndx:
le "I'm squirting! Oh my God, I never squirt with Jake! Your cock is ssooo good!"
mc "I'm about to blow my load too Chief Lena, get ready for a mighty cum shower!"
scene lockerlena03 with dissolve
mc "RHAAA? I'm still cumming after filling you up!"
le "YES, YES, keep pumping your sauce [name], I want to be covered in it!"
scene lockerlena04 with dissolve
mc "Ask and you shall receive! Here's more thick jets of spunk for you Chief Lena!"
le "So good, and so warm, you're a real cum-machine [name], I can't believe how much cum you can spew, keep going I beg you!"
stop music
play music "Sounds/shower.mp3"
scene lockermccum01 with dissolve
mc "Yeah, take that Chief Lena! AAAH!"
scene lockermccum02 with dissolve
mc "Damn, I made a right dreamy mess. I'd better clean all of it before I leave or people will think I'm a total pervert. Which I definitely AM NOT."
jump LenaGallery

label LenaGallery03:
scene fridayparty02
show virtuallena at left
show virtualruby at midright
$ ruby_health = 5.0
$ lena_health = 5.0
show screen screenfightlenaruby
play sound "Sounds/barfight.mp3"
ma "Our two contenders tonight are..."
scene lenafight01 with dissolve
ma "LENA!"
window hide
play sound "Sounds/applause.mp3"
show lenasign at streetfight01
$ renpy.pause(1, hard=True)
show lenasign:
    xalign 0.4
    yalign 0.4
ma "And..."
window hide
show versussign at streetfight02
stop sound
play sound "Sounds/versus.mp3"
$ renpy.pause(1, hard=True)
show versussign:
    xalign 0.5
    yalign 0.5
scene rubyfight01 with dissolve
show lenasign:
    xalign 0.4
    yalign 0.4
show versussign:
    xalign 0.5
    yalign 0.5
ma "RUBY!"
window hide
play sound "Sounds/applause.mp3"
show rubysign at streetfight03
$ renpy.pause(1, hard=True)
show rubysign:
    xalign 0.6
    yalign 0.6
pause 1.0
stop sound
scene fightsetup with dissolve
show rubysetup at midright
show lenasetup at midleft
play sound "Sounds/fight.mp3"
show fightsign at streetfight02
$ renpy.pause(1, hard=True)
hide fightsign
show rubysetup at center with move
ma "Ruby makes a move..."
scene lenarubyfight01    
ma "She lounges forward with the mindset of a berserk Road Warrior..."
scene lenarubyfight02
ma "..But Chief Lena saw it coming and fiercely knees her pussy!"
play sound "Sounds/punch.mp3"
$ renpy.pause(.5, hard=True)
show groinkick:
    xalign 0.5
    yalign 0.8    
$ counting = 0
while counting < 20:
    $ ruby_health -= 0.05
    $ counting += 1
    pause 0.01
scene lenarubyfight03
ma "Followed by a hick kick to the boobs! Ruby is sent flying into the corner! What a move by our Chief!"
play sound "Sounds/punch.mp3"
$ renpy.pause(.5, hard=True)
show boobkick:
    xalign 0.7
    yalign 0.4    
$ counting = 0
while counting < 20:
    $ ruby_health -= 0.05
    $ counting += 1
    pause 0.01
scene fightsetup with dissolve
show rubysetup at midright
show lenasetup at midleft
$ renpy.pause(1, hard=True)
ma "Back to the drawing board with Chief Lena in the lead!"
show lenasetup at center with move
ma "Lena is the one on the attack this time..."
scene lenarubyfight08
ma ".. But Ruby grabs her on the move and holds her tight in a spine-crushing fashion!"        
$ renpy.pause(.5, hard=True)
show spinecrush:
    xalign 0.6
    yalign 0.6       
$ counting = 0
while counting < 20:
    $ lena_health -= 0.1
    $ counting += 1
    pause 0.01
ma "That will cause a huge health loss to Lena for sure..."
scene lenarubyfight12 with fastdissolve
ma "But hang on, Lena manages to free herself from Ruby's hold and throws her pointy heel right in Ruby's neck!"
$ renpy.pause(.5, hard=True)
show heelkick:
    xalign 0.2
    yalign 0.4       
$ counting = 0
while counting < 20:
    $ ruby_health -= 0.1
    $ counting += 1
    pause 0.01
ma "Virtual blood is pouring out, Ruby took a serious hit there!"
scene fightsetup with dissolve
show lenasetup at midleft
show rubysetup at midright
$ renpy.pause(1, hard=True)
show rubysetup at center with move
ma "Ruby makes a move..."
scene lenarubyfight01 with fastdissolve
ma "She's gone into berserk mode again!"
scene lenarubyfight04
ma "But Lena counteracts with a swift catgirl back throw!"
scene lenarubyfight05
ma "Followed by a neck twirl that will surely spell doom for virtual Ruby..."
$ renpy.pause(.5, hard=True)
play sound "Sounds/bonecrack.mp3"
show necktwirl:
    xalign 0.5
    yalign 0.6       
$ counting = 0
while counting < 20:
    $ ruby_health -= 0.1
    $ counting += 1
    pause 0.01
ma "Yes, I can confirm her neck is broken and she's a goner..."
play sound "Sounds/winner.mp3"
window hide
scene fightlenawin with dissolve
show winnersign at streetfight02
$ renpy.pause(1, hard=True)
ma "Which means Lena is tonight's winner of this deadly fight!" 
play music "Sounds/applause.mp3"
$ renpy.pause(1, hard=True)
hide screen screenfightlenaruby
stop music
jump LenaGallery

label LenaGallery04:
scene mcliftend02
show lena07
le "Let's see what you've got, young man. Get into that sexy pouch I got you, I have a surprise for you..."
mc "Okay... I was going to do that anyway."
scene mcliftnew00
mc "I'm ready to PUMP IRON with the heaviest set in human history! Just watch and BEHOLD my POWER, Chief!"
scene gym03
show lenagymlingerie02
with dissolve
le "Oh, I'll watch, don't you worry about it. But you'll have to watch ME too while you're doing your reps..."
mc "You're in lingerie Chief!"
hide lenagymlingerie02
show lenagymlingerie01
with dissolve
le "That's right. To see if you can FOCUS."
mc "Alright, just watch this..."

play music "Sounds/mcworkout.mp3"
show mcgym01b
call screen mcgymlenasexyx
screen mcgymlenasexyx:
    modal True
    button:
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("GymLenaSexyEndx")        
        
label GymLenaSexyEndx:
stop music
scene mcliftnew18 with dissolve
mc "See that, Chief? That's RAW TEENAGE POWER!"
le "I'm impressed so far. But..."
scene lenagymhot01 with dissolve
le "...Being able to focus on the task at hand is ESSENTIAL in your line of work... So let's see if you can still lift those heavy weights if I PRESS DOWN on them while DISTRACTING you even more..."
mc "Fuck... OK, I'll show you, Chief!"
play music "Sounds/mcworkout.mp3" 
scene lenagymhot02 with dissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with dissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with dissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with dissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with dissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with dissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with dissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
stop music
le "You're doing good, [name]! Keep going, show me how STRONG and FOCUSED you are!"             
play music "Sounds/mcworkout.mp3"
scene lenagymhot02 with fastdissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with fastdissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with fastdissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with fastdissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with fastdissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with fastdissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
scene lenagymhot02 with fastdissolve
pause 0.2
scene lenagymhot01 with fastdissolve
pause 0.2
stop music
mc "See, I did it, Chief!"
le "You can put the weight down now, [name]..."
scene lenagymhot03 with dissolve
le "I'm impressed. VERY impressed, young man! Can you feel how hard my nipples have become because of YOU?"
mc "Aaah... Something else is getting HARD, Chief!"
le "Yeah, I can feel your COCK growing bigger, naughty boy... Mmmh, yes, feel those big breasts... You deserve them as a small reward..."
scene lenagymhot04 with dissolve
play sound "Sounds/womanmoan.mp3"
mc "Oh damn, Chief, they feel so FULL and RIPE!"
le "These are a REAL WOMAN's breasts!"
play sound "Sounds/ripping.mp3"
le "What was that? You RIPPED through your jockstrap with your hardening MEGADONG?"
mc "You're making me so horny, Chief!"
scene lenagymhot05 with dissolve
le "Let me this this thing..."
mc "Not before you let me see THESE things!"
scene lenagymhot06 with dissolve
mc "Now you can look at it, Chief!"
le "Mmmh, you're so MANLY! Just the way I wanted you to become!"
scene lenagymhot07 with dissolve
le "Damn, it reaches all the way to my CHEST! Let me tease it..."
scene lenagymhot07b with fastdissolve
pause 0.3
play sound "Sounds/boymoan.mp3"
mc "AAAH..."
scene lenagymhot07 with fastdissolve
pause 0.3
scene lenagymhot07b with fastdissolve
pause 0.3
scene lenagymhot07 with fastdissolve
pause 0.3
scene lenagymhot07b with fastdissolve
pause 0.3
scene lenagymhot07 with fastdissolve
pause 0.3
scene lenagymhot07b with fastdissolve
pause 0.3
scene lenagymhot07 with fastdissolve
pause 0.3
scene lenagymhot07b with fastdissolve
pause 0.3
scene lenagymhot07 with fastdissolve
pause 0.3
scene lenagymhot07b with fastdissolve
pause 0.3
scene lenagymhot07 with fastdissolve
pause 0.3
scene lenagymhot07b with fastdissolve
pause 0.3
scene lenagymhot07 with fastdissolve
pause 0.3
scene lenagymhot07b with fastdissolve
pause 0.3
scene lenagymhot07 with fastdissolve
pause 0.3
le "And now, I want you to lift those weights with just ONE arm [name]! Do it for me and then CUM FOR ME!"
scene lenagymhotcum01 with dissolve
play sound "Sounds/mcworkout.mp3"
mc "RHAAAA!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
le "YES! What a POWERFUL blast!"
scene lenagymhotcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH, I did it, I'm so fucking pumped up!!!"
le "Damn it [name], your cum jets are GIGANTIC! You're already covering me in your hot ball-batter and it's STILL spewing with full force while lifting those weights with ONE ARM!"
scene lenagymhotcum03 with dissolve
play sound "Sounds/womanmoan.mp3"
le "That was... HOT, [name]. I... never felt this way with another man... Or boy..."
mc "You realize now how POWERFUL I am, Chief Lena?"
le "Yes I do, I do. But let's get cleaned up, I don't want to be caught by anyone in this... position."
jump LenaGallery

label LenaGallery05:
play channel1 "v07/datemusic.mp3"
scene canyon01
show lenadate01
le "I had to tell Jake I was going on an exploratory mission. This had better be worth me lying to my husband."
mc "Oh, it will be Lena, it will be..."
hide lenadate01
show lenadate02
with fastdissolve
le "What is this place anyway? And how come no one ever told me about it? It's quite beautiful..."
mc "It's a well-known dating place around the compound. So remember I'm the one who told you about it then. All the others are liars. And maybe Jake too for all we know..."
hide lenadate02
show lenadate03
with fastdissolve
le "Jake? You think he might... But who would want to date this dufus?"
mc "Some women are desperate. But not you... You're the boss, you can choose whoever you want..." 
hide lenadate03
show lenadate04
with fastdissolve
le "Well, today, I choose YOU [name]. Jake never invited me HERE on a romantic date."
mc "I know how to treat my women... Err, I mean, ladies such as yourself."
le "Is that so? Prove it by kissing me then..."
hide lenadate04
show lenadate05
with fastdissolve
play sound "Sounds/kiss.mp3"
le "Mmmmh, you're a better kisser than Jake I must admit..." 
scene canyon02 blurred
show lenadate06
with fastdissolve
le "And what is this thing that's growing in your swimtrunks and getting absolutely MASSIVE?"
mc "Well, err... sorry, it has a mind of its own."
le "Well, you can't go swimming with this monster log down there, so why don't you take your trunks off. In exchange, I'll take MY top off..."
mc "It's a deal!"
scene lenadate07
with dissolve
mc "Will you join me in the water, Chief?"
le "Let me put some water on my skin first... You go ahead."
scene lenadate08
with dissolve
le "Mmh, the water has the perfect temperature... To make my nipples all hard..."
mc "And my cock ROCK-HARD."
scene lenadate09
with dissolve
le "What? Are you jerking off??? On our date?"
mc "No, I was just... err... Moving it aside to hide it. I mean, it's not appropriate to have a big boner on a date, is it?"
scene lenadate10
with dissolve
le "I think you're lying... You WERE jerking off weren't you? To my body... Right?"
mc "Well, err... Yes, maybe... No... I mean, I wouldn't do that on a date!"
le "I don't believe you. So go on, wank that fat shaft. Jerk it for me. I want to see you EXPLODE. Thinking about me..."
mc "Err. Okay. Chief."
play channel2 "Sounds/wank.mp3"
show lenadateslow
call screen lenadatewankslowx
screen lenadatewankslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaDateWankFastx") 

label LenaDateWankFastx:
le "Do it faster now, stroke that monsterdick for your chief!"
hide lenadateslow
show lenadatefast
call screen lenadatewankfastx
screen lenadatewankfastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaDateWankEndx") 

label LenaDateWankEndx:
mc "Chief...I'm so eager to please you, tell me when to cum for you please!"    
scene lenadate13 with fastdissolve
le "That's right, I 'm still your boss. So I'm giving you an ORDER to flog your monster dong with BOTH HANDS NOW, until you EXPLODE everywhere, you hear me?"
mc "Oh God, you're making me so horny speaking to me like that, I'll do it, I'll obey your orders Chief!"
hide lenadateslow
hide lenadatefast
show lenadatebothslow
call screen lenadatewankbothslowx
screen lenadatewankbothslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaDateWankbothFastx") 

label LenaDateWankbothFastx:
le "Keep going [name], but FASTER now! I LOVE watching you pleasure your YOUNG GIANT pussy-wrecker! It's so much BIGGER and POWERFUL than Jake's!"
hide lenadatebothslow
show lenadatebothfast
call screen lenadatewankbothfastx
screen lenadatewankbothfastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaDateWankbothEndx") 

label LenaDateWankbothEndx:
le "And now, I ORDER you to COME for me!"
scene lenadate16 with fastdissolve
pause 0.2
stop channel2
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH! Here it comes!"
scene lenadate17 with dissolve
stop sound
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
le "Yes, keep pumping that fat load while you admire my toned buttcheeks name!"
mc "I am Chief Lena, I'm cumming for you! RHHAAAA!"
scene lenadate18 with dissolve
stop sound
mc "God, I came so much... And all over myself too."
le "That's cos you're a very DIRTY boy! You came like, a year's worth of supply of sperm from Jake, it was incredible..."
scene canyon01
show lenadate01
with dissolve
le "Well, that date went pretty well I'd say. For YOU especially... And now I know about this place. So I learnt something too."
mc "Glad you enjoyed Lena..."
le "CHIEF Lena to you. I'm not your harem girl... Yet. *wink*" 
le "Let's go back to the compound, it's getting late."
stop channel1
jump LenaGallery

label LenaGallery06:
play channel1 "v07/datemusic.mp3"
scene bedroom02
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

label LenaFuckChoiceBx:
scene bedroom09 blurred
show lenabed01
with fade
le "What are you going to do to me, Daddy?"
stop music
menu:
    "I've just got to play with those sumptuous tits!":
        le "They're all yours to play with, Daddy!"
        jump LenaTitsx
    "Get ready for some serious pussy-pounding!":
        le "I can't wait for you to STRETCH my hole!"
        jump LenaSexx
    "You've always wanted me to become stronger and stronger. I'll show you how strong I am now!":
        le "Ooh, yes please, let me worship your HUGE muscles, Daddy!"
        jump LenaUpx
    "I'm done with this gallery.":
        jump LenaGallery

label LenaTitsx:
scene lenaprefondle01 with dissolve
mc "Fuck yeah, I've always wanted to fondle those nice titties of yours..."
play music "Sounds/moaning02.mp3"
label LenaFondleSlowx:
hide lenafondlefast
show lenafondleslow
call screen lenafondleslow01x
screen lenafondleslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaFondleEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaFondleFastx") 

label LenaFondleFastx:
le "You know your stuff [name]... Your strong hands can be real delicate..."
mc "I always take good care of my girls' most precious assets..."
hide lenafondleslow
show lenafondlefast
call screen lenafondlefast01x
screen lenafondlefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaFondleEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LenaFondleSlowx") 

label LenaFondleEndx:
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
label LenaTitsSlowx:
hide lenatitscloseslow
hide lenatitsfast
show lenatitsslow
call screen lenatitsslow01x
screen lenatitsslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaTitsEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaTitsFastx") 
    imagebutton:
        focus_mask True
        idle "v08/bottomview.png"
        hover "v08/bottomview.png"
        action Jump ("LenaTitsPOVSlowx") 

label LenaTitsPOVSlowx:
hide lenatitsslow
hide lenatitsclosefast
show lenatitscloseslow
call screen lenatitscloseslow01x
screen lenatitscloseslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaTitsEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaTitsPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("LenaTitsSlowx") 

label LenaTitsFastx:
hide lenatitsslow
hide lenatitsclosefast
show lenatitsfast
call screen lenatitsfast01x
screen lenatitsfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaTitsEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LenaTitsSlowx") 
    imagebutton:
        focus_mask True
        idle "v08/bottomview.png"
        hover "v08/bottomview.png"
        action Jump ("LenaTitsPOVFastx") 

label LenaTitsPOVFastx:
hide lenatitscloseslow
hide lenatitsfast
show lenatitsclosefast
call screen lenatitsclosefast01x
screen lenatitsclosefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaTitsEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("LenaTitsPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("LenaTitsFastx") 
            
label LenaTitsEndx:
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
jump LenaFuckChoiceBx

label LenaSexx:
scene lenapresex01 with dissolve
mc "Ready for it, Chief?"
scene lenapresex02 with dissolve
le "Ready for what, Daddy? Your MONSTER COCK that's drooling pre-cum all over the place?"
mc "Yeah, that thing..."
scene lenapresex03 with dissolve
le "I'm ready... My pussy is all wet for you, Daddy!"
mc "Then it's time to stretch it!"
play music "Sounds/barbarasex.mp3"
label LenaSexSlowx:
hide lenasexfast
hide lenasexpovslow
show lenasexslow
call screen lenasexslow01x
screen lenasexslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaSexEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaSexFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("LenaSexPOVSlowx") 

label LenaSexPOVSlowx:
hide lenasexpovfast
hide lenasexslow
show lenasexpovslow
call screen lenasexcloseslow01x
screen lenasexcloseslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaSexEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaSexPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("LenaSexSlowx") 

label LenaSexFastx:
mc "Gonna pummel that tight pussy of yours even faster, Lena!!"
le "Yes, do that daddy! Drill my fuckhole as deep and fast as you please!"
hide lenasexslow
hide lenasexpovfast
show lenasexfast
call screen lenasexfast01x
screen lenasexfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaSexEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LenaSexSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("LenaSexPOVFastx") 

label LenaSexPOVFastx:
mc "Gonna pummel that tight pussy of yours even faster, Lena!!"
le "Yes, do that daddy! Drill my fuckhole as deep and fast as you please!"
hide lenasexfast
hide lenasexpovslow
show lenasexpovfast
call screen lenasexclosefast01x
screen lenasexclosefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaSexEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("LenaSexPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("LenaSexFastx") 
            
label LenaSexEndx:
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
jump LenaFuckChoiceBx

label LenaUpx:
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
label LenaUpSlowx:
hide lenaupfast
show lenaupslow
call screen lenaupslow01x
screen lenaupslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaUpEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaUpFastx") 

label LenaUpFastx:
le "Your donkey-dick is splitting me in half, Daddy!"
mc "I'm going balls deep on each stroke, Lena!"
hide lenaupslow
show lenaupfast
call screen lenaupfast01x
screen lenaupfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaUpEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LenaUpSlowx") 

label LenaUpEndx:
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
jump LenaFuckChoiceBx

label LenaGallery07:
play music "v07/datemusic.mp3"
scene bedroom02
show lenalingerie01 at right with moveinright
le "I'm back [name]! In sexy lingerie. For YOU."
window hide
show jakecuck01 at farleft with moveinleft
hide lenalingerie01
show lenajakelingerie01 at right
with fastdissolve
le "And look who I brought. My darling hubby!"
ja "Are you going to fuck him in front of me again?"
le "That's right, and there's nothing you can do about it."
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
label JakeBlowSlowx:
hide jakeblowfast
show jakeblowslow
call screen jakeblowslow01x
screen jakeblowslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("JakeBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("JakeBlowFastx") 

label JakeBlowFastx:
mc "Damn that mouth was made to suck huge cocks. Just like in my dreams..."
hide jakeblowslow
show jakeblowfast
call screen jakeblowfast01x
screen jakeblowfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("JakeBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("JakeBlowSlowx") 

label JakeBlowEndx:    
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
le "Come on hubby, you wanted this, remember? Now get on the bed and start licking my pussy for the night's events."

label LenaFuckChoiceAx:
$ lenaasssaidx = False
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
        jump LenaFuckx
    "I want to drill that tight ass of yours, Chief!":
        le "Did you hear that, hubby? I don't remember the last time I let you ass-fuck me..."
        ja "So why are you letting HIM do it then?"
        le "Because he's got a monstercock, that's why."        
        jump LenaAssx
    "How about we DP you. Small-dick here obviously takes your ass.":
        le "That's very kinky. Too bad it won't be with TWO big cocks but yours is so big, it will be sufficient."
        ja "So... I get to fuck your ass, Lena?"
        le "As a reward for being a good cuckboy. Obviously, I won't feel a thing with [name]'s monstercock stuffed in my pussy."
        jump LenaDPx
    "I'm done with this gallery.":
        jump LenaGallery

label LenaFuckx:
scene jakeprecuck01 with dissolve
mc "See that dong, Jake? That's why your wife is in my harem..."
ja "It's not fair, how can I compete with THAT thing?"
le "You simply can't, hubby. You'll just have to watch this stallion STRETCH my hole and pray I can even feel your puny dick afer such a massive pounding!"
scene jakeprecuck02 with dissolve
mc "Let's see if it fits first. It does. Your wife was made to take HUGE COCKS up there."
le "YES! Only YOUR cock, Harem Master! Now fuck me please, FUCK ME HARD IN FRONT OF MY CUCKOLD HUSBAND!"
play music "Sounds/womansex02.mp3"
label LenaJakeSlowx:
hide jakecuckfast
hide jakecuckpovslow
hide jakecuckpovfast
show jakecuckslow
call screen jakecuckslow01x
screen jakecuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaJakeEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaJakeFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("LenaJakePOVSlowx") 

label LenaJakePOVSlowx:
hide jakecuckslow
hide jakecuckfast
hide jakecuckpovfast
show jakecuckpovslow
call screen jakecuckpovslow01x
screen jakecuckpovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaJakeEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaJakePOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("LenaJakeSlowx") 

label LenaJakeFastx:
hide jakecuckslow
hide jakecuckpovslow
hide jakecuckpovfast
show jakecuckfast
call screen jakecuckfast01x
screen jakecuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaJakeEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LenaJakeSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("LenaJakePOVFastx") 

label LenaJakePOVFastx:
hide jakecuckslow
hide jakecuckfast
hide jakecuckpovslow
show jakecuckpovfast
call screen jakecuckpovfast01x
screen jakecuckpovfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaJakeEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("LenaJakePOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("LenaJakeFastx") 
            
label LenaJakeEndx:
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
jump LenaFuckChoiceAx

label LenaAssx:
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
label LenaAssSlowx:
hide lenaassfast
show lenaassslow
call screen lenaassslow01x
screen lenaassslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaAssEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaAssFastx") 

label LenaAssFastx:
mc "Who's your ass-daddy, hey? Who's your ass-daddy?"
le "Oh God, you are, YOU ARE! Fuck me FASTER!"
hide lenaassslow
show lenaassfast
call screen lenaassfast01x
screen lenaassfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaAssEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LenaAssSlowx") 

label LenaAssEndx:
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
label LenaAssAgainSlowx:
show lenaassagainslow
call screen lenaassagainslow01x
screen lenaassagainslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaAssAgainEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaAssAgainFastx") 
    imagebutton:
        focus_mask True
        idle "v08/bottomview.png"
        hover "v08/bottomview.png"
        action Jump ("LenaAssBottomSlowx") 

label LenaAssAgainFastx:
if lenaasssaidx == False:
    le "This is incredible! Getting ass-fucked by the biggest dick ever while my hubby watches us and wanks his tiny cock... PLEASE POUND THAT MONSTERCOCK INTO ME FASTER NOW!"
    $ lenaasssaidx = True
show lenaassagainfast
call screen lenaassagainfast01x
screen lenaassagainfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaAssAgainEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LenaAssAgainSlowx") 
    imagebutton:
        focus_mask True
        idle "v08/bottomview.png"
        hover "v08/bottomview.png"
        action Jump ("LenaAssBottomFastx") 

label LenaAssBottomSlowx:
scene bedroom49 blurred
show lenaassbottomslow
call screen lenaassassslow01x
screen lenaassassslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaAssAgainEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaAssBottomFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("LenaAssAgainSlowx") 

label LenaAssBottomFastx:
if lenaasssaidx == False:
    le "This is incredible! Getting ass-fucked by the biggest dick ever while my hubby watches us and wanks his tiny cock... PLEASE POUND THAT MONSTERCOCK INTO ME FASTER NOW!"
    $ lenaasssaidx = True
scene bedroom49 blurred
show lenaassbottomfast
call screen lenaassassfast01x
screen lenaassassfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaAssAgainEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LenaAssBottomSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("LenaAssAgainFastx") 
        
label LenaAssAgainEndx:
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
$ lenaasssaidx = False
jump LenaFuckChoiceAx

label LenaDPx:
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
label LenaDPSlowx:
hide lenadpfast
show lenadpslow
call screen lenaDPslow01x
screen lenaDPslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaDPEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaDPFastx") 

label LenaDPFastx:
mc "This pussy is so good, cuckboy. But once I'm done with your wife, she won't be able to feel your pindick in there!"
le "I ain't letting him anywhere near my pussy anyway! Except to lick my Harem Master's cum out of it!"
mc "Let's move  faster now Jake, shall we?"
ja "O... Okay."
hide lenadpslow
show lenadpfast
call screen lenaDPfast01x
screen lenaDPfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaDPEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("LenaDPSlowx") 

label LenaDPEndx:
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
jump LenaFuckChoiceAx
