label AylaGallery:
call screen galleryayla
screen galleryayla:
    add "Gallery/aylagallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("galleryayla"), Jump ("MainGallery")]

    if renpy.seen_image("aylagymstart"):
        imagebutton:
            focus_mask True
            idle "Gallery/aylagallery01.png" xpos 621 ypos 100
            hover "Gallery/aylagallery01.png"
            action Jump ("AylaGallery01")

    if renpy.seen_image("aylagymstart") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("AylaGallery")

    if renpy.seen_image("aylashower01"):
        imagebutton:
            focus_mask True
            idle "Gallery/aylagallery02.png" xpos 1050 ypos 100
            hover "Gallery/aylagallery02.png"
            action Jump ("AylaGallery02")

    if renpy.seen_image("aylashower01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("AylaGallery")

    if renpy.seen_image("ayladate01"):
        imagebutton:
            focus_mask True
            idle "Gallery/aylagallery03.png" xpos 1478 ypos 100
            hover "Gallery/aylagallery03.png"
            action Jump ("AylaGallery03")

    if renpy.seen_image("ayladate01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("AylaGallery")

    if renpy.seen_image("fightaylawin"):
        imagebutton:
            focus_mask True
            idle "Gallery/aylagallery04.png" xpos 621 ypos 400
            hover "Gallery/aylagallery04.png"
            action Jump ("AylaGallery04")

    if renpy.seen_image("fightaylawin") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("AylaGallery")

    if renpy.seen_image("aylacrypt01"):
        imagebutton:
            focus_mask True
            idle "Gallery/aylagallery05.png" xpos 1050 ypos 400
            hover "Gallery/aylagallery05.png"
            action Jump ("AylaGallery05")

    if renpy.seen_image("aylacrypt01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("AylaGallery")

    if renpy.seen_image("aylalingerie01"):
        imagebutton:
            focus_mask True
            idle "Gallery/aylagallery06.png" xpos 1478 ypos 400
            hover "Gallery/aylagallery06.png"
            action Jump ("AylaGallery06")

    if renpy.seen_image("aylalingerie01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("AylaGallery")

    if renpy.seen_image("aylalingerie20"):
        imagebutton:
            focus_mask True
            idle "Gallery/aylagallery07.png" xpos 621 ypos 700
            hover "Gallery/aylagallery07.png"
            action Jump ("AylaGallery07")

    if renpy.seen_image("aylalingerie20") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("AylaGallery")

    if renpy.seen_image("dreamayla01"):
        imagebutton:
            focus_mask True
            idle "Gallery/aylagallery08.png" xpos 1050 ypos 700
            hover "Gallery/aylagallery08.png"
            action Jump ("AylaGallery08")

    if renpy.seen_image("dreamayla01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("AylaGallery")
            
    add "Gallery/galleryfuture.png" xpos 1478 ypos 700

    add "Gallery/gallerygrid02.png"
    add "Gallery/textayla.png"

label AylaGallery01:
scene aylagymstart
mc sidemc "Ayla is using the treadmill."
scene aylagymbackground
call screen aylagymjog01x
screen aylagymjog01x:
    add aylagymjog01
    add "Icons/nextidle.png"
    modal True
    button:
        xpos .91
        ypos .44
        xysize(140, 80)        
        action Jump ("AylaGymWorkoutEnd")

label AylaGymWorkoutEndx:
scene aylagymstart with dissolve
show aylagymend
ay "I saw you ogling my big tits while I was on the treadmill. That's disgusting!"
mc "What? What have I done?"
ay "Just get out of my face FREAK."
mc "You sound like some chick from that other game... What's her name... Maddy."
jump AylaGallery

label AylaGallery02:
play sound "Sounds/dream.mp3"
scene locker03dream
show aylashower01
play music "Sounds/showerstrip.mp3"
ay "Hello [name]... I feel like a demonic urge to jump that MASSIVE bone of yours, what d'ya say?"
mc "I say it is wise to follow Satan's orders..."
hide aylashower01    
show aylashower02
ay "My body will bring you to the DARK side of LUST and DEPRAVITY!"
mc "I think I'm already almost there but a little help won't hurt..."
hide aylashower02    
show aylashower03                                            
ay "Satan has turned me into a total sizequeen COCK-WHORE... And your MONSTER DONG is just what I NEED!"
mc "Well, come and join me in the shower stall and I'll give you what you need! 18 thick inches of it!"
hide aylashower03
scene locker03 blurred
show aylashower04
ay "My pussy is already dripping wet! I want you to POUND the shit out of me, understood?"
mc "Crystal clear!"
scene lockeraylafuck01a with dissolve
ay "Dear Belzebuth! Your cock is so big that I can suck it standing up... (kiss)"
play sound "Sounds/kiss.mp3"
mc "Well, you're quite tiny too... So tiny that I could easily lift you up on my rock-hard crank..."
scene lockeraylafuck01c with dissolve    
ay "OOOh, YES PLEASE! Show me how POWERFUL it is!"
scene lockeraylalift01 with dissolve
mc "Ready for lift-off?"
ay "YES! Lift me up to the Lord of Jizz, I need to repent my sins!"
scene lockeraylalift02 with dissolve
ay "Fuck! You did that so easily! That love muscle is made of CONCRETE!"
mc "And now, let me impale you on it Ayla!"
scene lockeraylafuck02 with dissolve
ay "Don't hold back! I might be small, but I can take your giant pussy-pleaser, all EIGHTEEN INCHES OF IT!"
mc "You want all of my monster cock Ayla? I'll give it to you then!"
call screen aylagymdreamx
screen aylagymdreamx:
    add dreamaylagym at center
    modal True
    button:
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("DreamAylaGymEndx")    
scene lockeraylafuck03 with fastdissolve
pause 0.15
scene lockeraylafuck02 with fastdissolve
pause 0.1
scene lockeraylafuck03 with fastdissolve
pause 0.15
scene lockeraylafuck02 with fastdissolve
pause 0.1
scene lockeraylafuck03 with fastdissolve
pause 0.15
scene lockeraylafuck02 with fastdissolve
pause 0.1
scene lockeraylafuck03 with fastdissolve
pause 0.15
scene lockeraylafuck02 with fastdissolve
pause 0.1
scene lockeraylafuck03 with fastdissolve
pause 0.15
scene lockeraylafuck02 with fastdissolve
pause 0.1
scene lockeraylafuck03 with fastdissolve
pause 0.15
scene lockeraylafuck02 with fastdissolve
pause 0.1
scene lockeraylafuck03 with fastdissolve
pause 0.15
scene lockeraylafuck02 with fastdissolve
pause 0.1
scene lockeraylafuck03 with fastdissolve
pause 0.15
scene lockeraylafuck02 with fastdissolve
pause 0.1
label DreamAylaGymEndx:
ay "That's it, claim that whore-hole, make it yours with your satanic seed!"
mc "I'm gonna blow any time now, I'll give you a spunk enema Ayla!"
show lockeraylafuck03 with dissolve        
ay "YES? I can feel each and every one of your powerful wads, it's ssoo amazing! "
mc "You want more? I'll give you MORE and take you to sex heaven Ruby!"
stop music
play music "Sounds/shower.mp3"
scene lockermccum01 with dissolve
mc "I've got some more cum showers for you Ayla, RHAAAA!"    
mc "But there isn't one, I'll just wank myself silly anyway..."
scene lockermccum01 with dissolve
mc "Fuck, cumming non-stop, RHAAAA!"    
jump AylaGallery

label AylaGallery03:
play music "v07/datemusic.mp3"
scene canyon01
show ayladate01
ay "Yeah, OK, this place is alright for a date, I guess."
ay "Are you repeating what I'm saying???"
mc "No, there's an echo here, that's all."
hide ayladate01
show ayladate02
with fastdissolve
ay "Boring. BORING!"
"Boring.. Boring..."
mc "That was fun, right? And can you feel the fresh air? It's invigorating, isn't it?"
hide ayladate02
show ayladate03
with fastdissolve
ay "What are you babbling about? It's just... air. Like the air in the compound."
mc "With less radioactivity though, cos there's a breeze flowing through the canyon, can't you feel it?"
ay "Not really."
scene ayladate08 with dissolve
mc "I can totally feel it cos I'm all wet."
ay "I ain't ready to go in the water."
scene ayladate09 with dissolve
mc "Are you scared? There's nothing bad in the water, all life is dead. SO it's totally safe."
ay "Al...alright."
scene ayladate10 with dissolve
mc "Yeah, take your top off so you can really feel the breeze."
ay "I knew you would like that..."
scene ayladate11 with dissolve
play sound "Sounds/dive.mp3"
mc "(nice. This date is finally getting somewhere...)"
scene ayladate12 with dissolve
ay "Well, I'm all wet now, but I don't feel a thing. This place is boring. Let's leave."
mc "No, no, no, you need to...err... get out of the water to feel the breeze. Especially on your nipples."
ay "Where did you hear such a pile of nonsense?"
mc "Err... In a book. Trust me. I'm topless and I can feel the breeze. It's coming straight down from Phallus Heaven."
ay "I'll check if it's bullcrap or not then. It better not be BULLSHIT, I'm warning you!"
scene canyon02 blurred
show ayladate04
with dissolve
ay "Mmmh, Ok, I guess I feel something now. And now what?"
mc "Just wait a bit, the breeze will refresh you. And make your nipples harden."
hide ayladate04
show ayladate05
with fastdissolve
ay "Alright, I'll admit it, I can feel the breeze now... But it's not very strong, kind of BORING!"
hide ayladate05
show ayladate06
with fastdissolve
mc "I'll lick you arm and increase the feel of freshness. Can you feel it?"
ay "Hee hee, it's tickling me! But what about my nipples? I'm not letting you lick them on a first date!"
mc "I've got another idea, I'll lift you up and they'll be in contact with my wet skin."
hide ayladate06
show ayladate07
with fastdissolve
ay "OOoh, I see. I can feel your huge musc.. I mean your wet skin on my nipples now... Thanks for showing me your trick."
play sound "Sounds/kiss.mp3"
ay "Now get me down, you're getting me all wet!"
scene canyon02
show ayladate05
with dissolve
ay "I think this date is over. I've seen enough... And so have you. It was kind of... nice. Thank you [name]."    
stop music
jump AylaGallery
    
label AylaGallery04:
scene fridayparty02
show virtualamy at left
show virtualayla at midright
$ amy_health = 5.0
$ ayla_health = 5.0
show screen screenfightamyayla
play sound "Sounds/barfight.mp3"
ma "Our two contenders tonight are..."
scene fightamy01 with dissolve
ma "AMY!"
window hide
play sound "Sounds/applause.mp3"
show amysign at streetfight01
$ renpy.pause(1, hard=True)
show amysign:
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
scene fightayla01 with dissolve
show amysign:
    xalign 0.4
    yalign 0.4
show versussign:
    xalign 0.5
    yalign 0.5
ma "AYLA!"
window hide
play sound "Sounds/applause.mp3"
show aylasign at streetfight03
$ renpy.pause(1, hard=True)
show aylasign:
    xalign 0.6
    yalign 0.6
pause 1.0
stop sound
scene fightsetup with dissolve
show aylasetup at midright
show amysetup at midleft
play sound "Sounds/fight.mp3"
show fightsign at streetfight02
$ renpy.pause(1, hard=True)
hide fightsign
show amysetup at center with move
ma "Amy makes a move..."
scene aylaup01
ma "..But her attack is dodged by Ayla!"
scene aylaup02
play sound "Sounds/punch.mp3"
$ renpy.pause(.5, hard=True)
show boobpunch:
    xalign 0.4
    yalign 0.6    
$ counting = 0
while counting < 20:
    $ amy_health -= 0.05
    $ counting += 1
    pause 0.01
ma "..who counters with a painful boob punch!"
scene amyup02
$ renpy.pause(.5, hard=True)
show knucklehead:
    xalign 0.6
    yalign 0.3    
$ counting = 0
while counting < 20:
    $ ayla_health -= 0.05
    $ counting += 1
    pause 0.01
play sound "Sounds/punch.mp3"
$ renpy.pause(.5, hard=True)
ma "But Amy isn't letting herself down!"
scene fightayla01 with fastdissolve
ma "That seems to have made Ayla angry as hell!"
scene aylaup03 with fastdissolve
ma "Oh, she's doing the Matrix floating pose! Virtual time has stopped..."
scene aylaup04 with fastdissolve
play sound "Sounds/punch.mp3"
$ renpy.pause(.5, hard=True)
show matrixthrust:
    xalign 0.4
    yalign 0.6       
$ counting = 0
while counting < 20:
    $ amy_health -= 0.1
    $ counting += 1
    pause 0.01
ma "...and Amy didn't have virtual time to see this high kick coming!"
scene fightsetup with dissolve
show aylasetup at midright
show amysetup at midleft
$ renpy.pause(1, hard=True)
show amysetup at center with move
ma "Back to the drawing board with Amy on the attack..."
scene amyup03 with dissolve
ma "She lifts her opponent onto her strong shoulders..."
scene amyup04 with dissolve
ma "..And throws her like a discarded condom!"
scene amyup05 with dissolve
play sound "Sounds/punch.mp3"
$ renpy.pause(.5, hard=True)
show groinstomp:
    xalign 0.4
    yalign 0.6       
$ counting = 0
while counting < 20:
    $ ayla_health -= 0.1
    $ counting += 1
    pause 0.01    
ma "Followed by a painful groin stomp!"
scene aylaup06 with fastdissolve
ma "But Ayla hasn't said her last word... She jumps on Amy's back and flips the situation around!"
scene aylaup05 with fastdissolve
ma "I can hear Amy's virtual spine break in half... That's got to hurt..."
show backbreaker:
    xalign 0.4
    yalign 0.6       
$ counting = 0
while counting < 20:
    $ amy_health -= 0.1
    $ counting += 1
    pause 0.01    
ma "And Amy is out for good!"
play sound "Sounds/winner.mp3"
window hide
scene fightaylawin with dissolve
show winnersign at streetfight02
$ renpy.pause(1, hard=True)
ma "Ayla wins tonight's fight!" 
play music "Sounds/applause.mp3"
$ renpy.pause(1, hard=True)
hide winnersign
hide screen screenfightamyayla
stop music
jump AylaGallery

label AylaGallery05:
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
label AylaCryptSlowx:
hide aylacryptfast
show aylacryptslow
ty "The power of Jizz compels you. The power of Jizz compels you!"
call screen aylacryptslow01x
screen aylacryptslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaCryptEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaCryptFastx") 

label AylaCryptFastx:
hide aylacryptslow
show aylacryptfast
ty "I'll increase the tempo now and raise my voice too. THE POWER OF JIZZ COMPELS YOU. THE POWER OF JIZZ COMPELS YOU!"
call screen aylacryptfast01x
screen aylacryptfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaCryptEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaCryptSlowx") 

label AylaCryptEndx:
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
jump AylaGallery

label AylaGallery06:
play music "v07/datemusic.mp3"
scene bedroom01
show aylalingerie01 at center with moveinright
ay "I am ready to atone for my sins!... by letting you fuck me senseless with your punishing ramrod."
mc "Very appropriate since I am well known within the clergy as \"[name] the Punisher\"."
hide aylalingerie01
show aylalingerie05
with fastdissolve    
ay "Indeed you are! Let me thank the invisible sky to have unleashed you on such a dreadful sinner as myself!"
hide aylalingerie05
show aylalingerie02
with fastdissolve
ay "I will now attempt to entice your massive PUNISHER into rock-hardness..."
mc "That's a good idea, Ayla. And I can already tell you it's responding VERY WELL."
hide aylalingerie02
show aylalingerie03
with fastdissolve
ay "Perhaps seeing my backside will help?"
mc "Perhaps it might indeed..."
scene bedroom07 blurred
show aylalingerie04
with dissolve
mc "Yes... That sumptuous view is certainly stirring my punishing dong into action..."
ay "I'll take my top off and rub that Holy Baby Oil all over my sinning breasts, now..."
scene bedroom01 blurred
show aylalingerie06
with dissolve
ay "So, what do you think, [name] the Punisher?"
mc "I think I 'm READY to PUNISH YOU, Ayla!"
ay "Then come over here and show me how those huge muscles that will handle me like a ragdoll..."
scene bedroom35
show aylaarnie01
with dissolve
ay "[name], you're are such a MUSCLE STUD!"
mc "All the better to PUNISH naughty girls lile you, Ayla!"
hide aylaarnie01
show aylaarnie02
with fastdissolve
ay "Let me rub some baby oil on you too... So our carnal union will be totally approved by the Church!"
mc "Don't forget my dong..."
hide aylaarnie02
show aylaarnie03
with fastdissolve
ay "How could I? It's the strongest punishing ramrod in the whole Church. And it's still growing..."
mc "I'll show you its power, Ayla, just open your legs a little..."
hide aylaarnie03
show aylaarnie04
with fastdissolve
mc "...And there you are. Now we are at eye level finally."
ay "Oooh! I feel... so helpless... ANd horny at the same time!"
hide aylaarnie04
show aylaarnie05
with fastdissolve
ay "...Kiss me. That way, I'll forget about my boyfriend for the night and be entirely YOURS."
play sound "Sounds/kiss.mp3"
ay "And now, let the FUN begin! How shall we proceed?"
stop music
label AylaFuckChoiceAx:
stop music
scene bedroom03b blurred
show aylaready01
ay "What could we do to please the Phallus Lord, while at the same time, HAVING FUN?"
mc "And the aliens. Err... I mean, the angels in the sky."
label AylaFuckChoiceAbx:
menu:
    "Wrap those massive titties around my giant pole.":
        ay "Ooh, a titfuck? Then I'll rub Holy Baby Oil all over YOU too! To make everything nice and slippery..."
        mc "Yeah, coat my muscled body in oil, and don't forget my knob."
        jump AylaTitsx
    "I want to see how far my cock goes into that tiny body of yours...":
        ay "I bet it goes... REALLY FAR! Let me prep my body for it by rubbing Holy Baby-oil all over myself..."
        hide aylaready01
        show aylaready02
        with dissolve
        mc "That's a nice touch, Ayla."
        hide aylaready02
        show aylaready03
        with dissolve 
        ay "Now I'm ready for your pillar of lust to penetrate my body."
        mc "Then, let's penetrate!"
        jump AylaMissionaryx
    "I've been a sinner too and I'm not allowed to jerk off anymore. May your feet do the jerking as a replacement then.":
        ay "My feet as as substitute for your unholy hands? I like the idea..."
        jump AylaFootJobx
    "I've always dreamed of drilling your ass. I dream of it when I masturbate in the gym showers.":
        ay "Eew, too much information! And you're too big anyway."
        mc "Not if you rub Holy Baby-Oil on my cock to make it slippery..."
        ay "That's an interesting thought. I would get a Holy Enema. I'm in!"
        hide aylaready01
        show aylaready02
        with dissolve
        ay "First I'll rub oil all over myself too alleviate the sinfulness of this sodomy."
        scene bedroom10
        show aylaready03
        with dissolve
        ay "Now I'm ready for you to PLUNGE your tool in my ARSE!"        
        jump AylaAnalx
    "I'll put a smile on your face by giving the gift of LIFE. Prepare to get IMPREGNATED, Ayla!" if renpy.seen_image("aaylaimpregcum01"):
        ay "What? A baby? I... This is actually quite exciting for once. DO IT! PUMP YOUR SEED IN ME AND MAKE ME PREGNANT!"
        jump AylaImpregnationx
    "I'm done with this gallery.":
        jump AylaGallery

label AylaTitsx:
scene bedroom23
show aylapretits01
with dissolve
ay "I don't even know where to begin... That horsecock of yours is just so... BIG!"
mc "But so are your tits Ayla, so it's perfect match."
scene bedroom37 blurred
show aylapretits02
with dissolve
ay "You think so? You think my tits are big enough for your GIANT boyhood?"
mc "Yeah, definitely. Let's get this started!"
scene bedroom40 blurred
play music "Sounds/wank.mp3"
label AylaTitsSlowx:
hide aylatitsfast
show aylatitsslow
call screen aylatitsslow01x
screen aylatitsslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaTitsEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaTitsFastx") 

label AylaTitsFastx:
ay "You want me to wrap my jugs around your engorged monsterpole faster [name]? That's what you want isn't it, you BAD BOY! Just watch then..."
hide aylatitsslow
show aylatitsfast
call screen aylatitsfast01x
screen aylatitsfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaTitsEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaTitsSlowx") 

label AylaTitsEndx:
mc "FUUUUUUCK! This is too good, I'm gonna..."
hide aylatitsfast
hide aylatitsslow
show aylatitscum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "...CUUUUMMMM!"
with fastflash
ay "YES! Release that jizz, let it HOSE my tits and face down, GIVE ME ALL THAT SWEET YOUNG CUM!"
scene bedroom40 blurred
show aylatitscum02
with dissolve
ay "Your sperm is landing down on my face from so HIGH ABOVE, it's like a CUM-SHOWER!"
with fastflash
mc "My nuts are exploding for you, Ayla! RHAAA!"
scene bedroom08 blurred
show aylatitscum03
with dissolve
ay "What a MIGHTY load of hot boycream!"
mc "You bring the best out of me. Shall we move on perhaps? My cock is stil hard."
ay "I'll slurp up your plentiful offering and I'm ready to go for ANOTHER ROUND!"
scene bedroom03b blurred
show aylaready01
with dissolve
ay "So, what do you planned for us?"
jump AylaFuckChoiceAbx

label AylaFootJobx:
scene bedroom41 blurred
show aylaprefoot01
with dissolve
ay "Look at that monster cock! It's sssooo BIG!"
mc "All the better to please you."
ay "Now stay back while my feet do all the jerking... No hands!"
mc "Fine by me, though I wonder if your tiny feet will be enough stimul..."
scene bedroom18 blurred with dissolve
play music "Sounds/wank.mp3"
label AylaFootJobSlowx:
hide aylafootfast
show aylafootslow
mc "...ation, AAAH!"
window hide
call screen aylafootslow01x
screen aylafootslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaFootJobEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaFootJobFastx") 

label AylaFootJobFastx:
ay "What if I increased the tempo? Will you give me a nice big FAT load now?"
hide aylafootslow
show aylafootfast
call screen aylafootfast01x
screen aylafootfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaFootJobEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaFootJobSlowx") 

label AylaFootJobEndx:
mc "I'm on the verge of cumming..."
ay "Do it [name]! I want to see it BLASTING from your cumhole!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
hide aylafootslow
hide aylafootfast
show aylafootcum01
with fastdissolve
mc "FUCK YEAH!!! Take those BIG jets!"
ay "BIG? You think you're a BIG SHOT, hey? Then come MASSIVE SHOTS!"
scene bedroom37
show aylafootcum02
with fastdissolve
mc "FUCK, I am, you feet are sssooo good!"
with fastflash
ay "Keep blasting, I want BOTH OF US to be covered in your splooge!"
scene bedroom28
show aylafootcum03
with dissolve
mc "AAAAH! You're making me cum all over myself!"
ay "That came to a very satistfying conclusion for you apparently... But not for me."
scene bedroom18 blurred
show aylaprehand01
with dissolve
mc "What are you doing? I just came, my knob is super-sensitive right now!"
ay "That wasn't enough spunk, I want MORE cum, you hear me? You MUST come again and give me another MONSTER LOAD!"
mc "Of FUCK! OK, OK, I'll do it!"

label AylaHandSlowx:
hide aylahandfast
hide aylahandpovslow
hide aylahandpovfast
scene bedroom37
show aylahandslow
call screen aylahandslow01x
screen aylahandslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaHandEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaHandFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("AylaHandPOVSlowx") 
        
label AylaHandPOVSlowx:
hide aylahandfast
hide aylahandslow
hide aylahandpovfast
scene bedroom08 blurred
show aylahandpovslow
call screen aylahandpovslow01x
screen aylahandpovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaHandEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaHandPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AylaHandSlowx") 

label AylaHandPOVFastx:
hide aylahandfast
hide aylahandslow
hide aylahandpovslow
scene bedroom08 blurred
show aylahandpovfast
call screen aylahandpovfast01x
screen aylahandpovfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaHandEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaHandPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AylaHandFastx") 

label AylaHandFastx:
hide aylahandslow
hide aylahandpovslow
hide aylahandpovfast
scene bedroom37 blurred
show aylahandfast
call screen aylahandfast01x
screen aylahandfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaHandEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaHandSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("AylaHandPOVFastx") 

label AylaHandEndx:
ay "Now COME for me [name]! Give me MORE CUM!"
hide aylahandslow
hide aylahandpovslow
hide aylahandpovfast
hide aylahandfast
scene bedroom08 blurred
show aylahandjobcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
ay "Wow, you had THAT much cum left in your bloated balls?"
mc "AAAAH, wait, I've have MORE for you, Ayla!"
hide aylahandjobcum01
show aylahandjobcum02
with fastdissolve
ay "Oh my God, you're pumping so many shots of boycum! I'm already caked in your seed and you're STILL spewing???"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Almost there, a few more, RHAAA!"
hide aylahandjobcum02
show aylahandjobcum03
with fastdissolve
ay "I think THAT was worth it, don't you think?"
mc "Phew... My cock nods in approval."
ay "Meaning it's still HARD for more fun?"
mc "Of course... Get cleaned up and I'll be right with you."
scene bedroom03b blurred
show aylaready02
with dissolve
ay "I'm squeaky clean now, and ready for more MONSTERCOCK action!"
jump AylaFuckChoiceAbx

label AylaMissionaryx:
scene bedroom16
show aylaarnieprefuck01
with dissolve
ay "You're gonna FUCK ME with your massive rod [name]?"
mc "Yeah, that's what you want, isn't it?"
ay "I don't know, it's just so BIG and I'm so TINY!"
mc "Don't worry, it'll fit. The dev is pretty good at making my ock fit into tiny holes."
scene bedroom20 blurred
play music "Sounds/womansex01.mp3"
label AylaMissionarySlowx:
hide aylamissionaryfast
show aylamissionaryslow
call screen aylapoundslow01x
screen aylapoundslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaMissionaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaMissionaryFastx") 

label AylaMissionaryFastx:
hide aylamissionaryslow
show aylamissionaryfast
call screen aylapoundfast01x
screen aylapoundfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaMissionaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaMissionarySlowx") 

label AylaMissionaryEndx:
mc "I'm about to blow my nut Ayla!"
ay "FLOOD MY PUSSY with your virile spunk, [name]!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
hide aylamissionaryslow
hide aylamissionaryfast
show aylaarnieanimcum01
with fastdissolve
mc "Gonna fill you up to OVERFLOODING! RHAAA!!!"
ay "Keep pumping that load, I'm cumming with you, AAAH! I can feel each of your MASSIVE CUM-RUPTIONS! Oooh, it's ssoo good!"
mc "Hang on Ayla, I've got some more sauce for your hot bod!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
scene bedroom17 blurred
show aylaarnieanimcum02
mc "Fuck YEAH! I'm BLASTING FULL STEAM!"
ay "OOh, my God, you're such a CUM-MACHINE! And my pussy is BLOATED with your spunk too!"
scene bedroom14
show aylaarnieanimcum03
ay "See all that splooge you've given me? You made that mess, [name]."
mc "Isn't every sperm supposed to be sacred? Won't that make the Phallus Lord irrate?"
ay "Maybe, but your sperm was GOOD."
scene bedroom10
show aylaready03
with dissolve
ay "Let's have some more FUN. This is not as boring as I thought."
jump AylaFuckChoiceAbx

label AylaAnalx:
scene bedroom12
show aylapreanal01
with dissolve
mc "Are you ready?"
ay "You're already inside so deep!"
mc "That's just the tip, Ayla. I haven't started. There's 15 more inches to go. Here, I'll show you."
scene bedroom08 blurred with dissolve
play music "Sounds/womansex02.mp3"
label AylaAnalSlowx:
hide aylaanalfast
show aylaanalslow
call screen aylaanalslow01x
screen aylaanalslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaAnalFastx") 

label AylaAnalFastx:
ay "This is..."
ay "...so..."
ay "...GOOD... FASTER, PLEASE!"
hide aylaanalslow
show aylaanalfast
call screen aylaanalfast01x
screen aylaanalfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaAnalSlowx") 

label AylaAnalEndx:
ay "Please, give me a Holy Enema, [name]!"
mc "Just a few more pumps and...."
hide aylaanalslow
hide aylaanalfast
show aylaanalcum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...I'll douse your bowels with my cum, RHAAA!"
ay "It's already leaking out with such FORCE after just a few shots, come over me please!"
scene bedroom34 blurred
show aylaanalcum02
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "I will, take that Ayla, my Holy Sperm! AAAH!"
ay "Mmmh, yes, it's so thick, it's like oatmeal!"
scene bedroom20 blurred
show aylaanalcum03
ay "I'm totally COVERED in sounk.... It's so warm... You just came like a STALLION."
mc "And as a true stallion, I can fuck you some more if you want..."
ay "God, you're such a MEGA-STUD. I DO want more. Let me get cleaned up and I'll be right with you..."
scene bedroom03b blurred
show aylaready01
with dissolve
ay "And what do you have in mind this time for poor little me?"
jump AylaFuckChoiceAbx

label AylaGallery07:
scene bedroom01
show ayla01
ay "Why did you call me in the middle of the night? I was SLEEPING!"
mc "Well, I've got a better activity for you than this snore-fest."
hide ayla01
show ayla02
with fastdissolve
ay "And what would that be?"
mc "SEX. You owe me sexual allegiance and respect as a girl in my harem, remember."
ay "Pff. I don't even know why I bothered joining your stupid harem. Alright, let's get it over with then. What should I wear?"
mc "A kinky BDSM outfit. I feel like being dominated by a short angry girl tonight."
hide ayla02
show ayla06
with fastdissolve
ay "I can do that. I LOVE dominating men. Especially wannabe studs like you!"
play music "v07/datemusic.mp3"
scene bedroom02 with fade
show aylalingerie11 at center with moveinright
ay "MISTRESS AYLA is ready for you!"
mc "Well, I mean, let's not push it Ayla, I'm still the harem Mast..."
hide aylalingerie11
show aylalingerie12
with fastdissolve
ay "What were you saying? I didn't quite hear you call my name PROPERLY."
mc "I see. You want to play? Then, let's play, MISTRESS AYLA!"
ay "Oh, I'm not playing... GET ON YOUR KNEES!"
hide aylalingerie12
show aylalingerie13
with fastdissolve
ay "That's better. And now, lick my boots, SLAVE."
mc "Err... I have a foot fetish but that's kinda gro..."
hide aylalingerie13
show aylalingerie14
with fastdissolve
ay "Do as you're told, SLAVE!"
mc "Yes, Mistress Ayla."
scene bedroom35 blurred
show aylalingerie13b
with fastdissolve
ay "All the way up to my thighs. I want my leather boots to be SHINY with your saliva, slave."
hide aylalingerie13b
show aylalingerie15
with fastdissolve
ay "And now be my poney. I'v always wanted a poney. So I'll ride you like one."
mc "Can I say \"neigh\" and refuse?"
ay "Certainly not! But you can neigh while I ride you, poney-boy!"
hide aylalingerie15
show aylalingerie16
with fastdissolve
ay "Yeah, I have my own poney! Ride me around the room."
scene bedroom02 blurred
show aylalingerie17
with fastdissolve
play sound "Sounds/slap.mp3"
mc "Ouch! I mean \"neigh\"!!!"
ay "Faster, poney, ride your mistress across the room! And then roll on your back!"
hide aylalingerie17
show aylalingerie18
with fastdissolve
ay "Ooh, I see my poney has a great big erection. But I don't see any mare around, how could that be? Are you in rut, my little poney?"
mc "Yeah, err... I'm a poney who's into besti*lity. With humans."
ay "Oh, so I did that, poney-boy? I guess it's time to move onto the bed... For some bestial SEX!"
stop music
jump AylaFuckChoiceBx

label AylaFuckChoiceBx:
stop music
scene bedroom03b blurred
show aylalingerie20
with dissolve
ay "Mmmh, I wonder what I should do with my slave-boy..."
label AylaFuckChoiceBbx:
menu:
    "Do your worse, I deserve to be punished Mistress Ayla!":
        ay "That's what I like to hear, slaveboy! So get on your back, I'm going to ride your giant cock till you explode in my pussy!"
        jump AylaRidex
    "I could lick your delicious pussy for your personal pleasure, mistress Ayla!":
        ay "Ooh, that's a good idea. Like a good lapping-dog."
        jump AylaLickx
    "Torture my cock, any way you see fit Mistress.":
        ay "I know how... With my HUGE tits. You like my huge tits, don't you?"
        mc "Yes I do. They're so MASSIVE on a such a tiny frame..."
        jump AylaTitsbx
    "I'm done with this gallery.":
        jump AylaGallery

label AylaRidex:
scene bedroom18
show aylapreride01
with dissolve
ay "Get that dong absolutely ROCK-HARD cos I'm going to ride you like a poney!"
mc "I'm as hard as a bar of titanium for you, Mistress."
ay "Indeed, I can feel your monster cock running all the way up my back."
hide aylapreride01
show aylapreride02
with fastdissolve
ay "But still. I want to make sure you STAY hard while I ride you, you hear me?"
mc "AAH... Y...Yes Mistress Ayla."
ay "That's good, I think you're ready."
scene bedroom08 blurred with dissolve
play music "Sounds/fucksound.mp3"
label AylaRideSlowx:
hide aylaridefast
show aylarideslow
call screen aylarideslow01x
screen aylarideslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaRideEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaRideFastx") 

label AylaRideFastx:
ay "I'm gonna pump the cumload out of your fat balls even FASTER now!"
hide aylarideslow
show aylaridefast
call screen aylaridefast01x
screen aylaridefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaRideEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaRideSlowx") 

label AylaRideEndx:
mc "Oooh, Mistress, I can't hold it anymore!"
ay "Then RELEASE your spunk directly into my womb, slaveboy! DO IT NOW, I WANT IT NOW!"
stop music
scene bedroom41 blurred
show aylaridecum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "I'm nutting inside of you, Mistress! RHAAA!"
ay "I can FEEL IT!! Now PLASTER my back, I'm sure you still have a HUGE supply left in your FAT BULL-BALLS!"
scene bedroom08 blurred
show aylaridecum02
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
ay "Mmh, I can feel those heavy shots smacking my corset with such FORCE!"
mc "That's the last of my load Mistress..."
ay "Then STAY HARD and let me think of something else to do with you slave..."
jump AylaFuckChoiceBx

label AylaLickx:
scene bedroom18 with dissolve
show aylaprelick01
ay "First, I'll mmake you BEG for IT!"
scene bedroom17 with fastdissolve
show aylaprelick02
play sound "Sounds/sucking.mp3"
ay "While I lick this engorged piece of boymeat standing proudly in front of me..."
mc "I'm ready Mistress, please release my head so I can pleasure you!"
scene bedroom08 with fastdissolve
show aylaprelick03
ay "Alright. You'd better do a REALLY GOOD JOB OF IT, SLAVE!"
scene bedroom20 blurred
play music "Sounds/womansex01.mp3"
label AylaLickSlowx:
play sound "Sounds/lick.mp3"
hide aylalickfast
show aylalickslow
call screen aylalickslow01x
screen aylalickslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaLickEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaLickFastx") 

label AylaLickFastx:
play sound "Sounds/lick.mp3"
ay "Lick my clit faster, swirl that tongue in there, [name]!"
hide aylalickslow
show aylalickfast
call screen aylalickfast01x
screen aylalickfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaLickEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaLickSlowx") 

label AylaLickEndx:
play sound "Sounds/lick.mp3"
ay "This is ssoo good, I'm gonna SQUIRT..."
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene bedroom37 blurred
show aylalickcum01
with dissolve
play sound "Sounds/womanmoan.mp3"
ay "AAH, YES, you're making me cum, my juices are POURING!"
mc "Me too Mistress! RHAAA!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
scene bedroom37 blurred
show aylalickcum02
with fastdissolve
ay "What, how DARE you plaster my back with your vile cum!"
mc "I couldn't help myself, sorry, we came together."
scene bedroom03b 
show aylalingerie20
with dissolve
ay "You've been a VERY NAUGHTY SLAVE! I wonder what I should do next to PUNISH you?..."
jump AylaFuckChoiceBbx

label AylaTitsbx:
scene bedroom16
show aylapretits00b
with dissolve
ay "Mmmh, you're THAT MUCH in a hurry for that titjob, hey?"
mc "That's right, I can't wait for your huge funbags to TORTURE my cock! Let's get into position by the edge of the bed!"
scene bedroom23
show aylapretits01b
with dissolve
ay "Get ready for the titfuck of your lifetime. I'm going to squeeze that rock-hard monster until it EXPLODES!"
mc "Do your worse, Ayla, I'm ready to take it!"
scene bedroom37 blurred
show aylapretits02b
with dissolve
ay "I don't think you realize what I have in store for you..."
scene bedroom40 blurred
play music "Sounds/wank.mp3"
label AylaTitsSlowbx:
hide aylatitsfastb
show aylatitsslowb
call screen aylatitsslow01bx
screen aylatitsslow01bx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaTitsEndbx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaTitsFastbx") 

label AylaTitsFastbx:
ay "Look at you, your face is contorted with the aching pain of imminent release. Let me bring you over the EDGE!"
hide aylatitsslowb
show aylatitsfastb
call screen aylatitsfast01bx
screen aylatitsfast01bx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaTitsEndbx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaTitsSlowbx") 

label AylaTitsEndbx:
mc "FUUUUUUCK! THis is too good, I'm gonna..."
hide aylatitsfastb
hide aylatitsslowb
show aylatitscum01b
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc"....CUUUUMMMM!"
ay "YES! Release that jizz, let it HOSE my tits and face down, I WANT IT!"
scene bedroom40 blurred
show aylatitscum02b
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
ay "It's flying everywhere and PLASTERING my face! Keep going SLAVE!"
with fastflash
mc "AAAH, I'm trying to, I'm giving you as much spunk as I can, Mistress! RHAAA"
scene bedroom08 blurred
show aylatitscum03b
ay "You did well, what a MIGHTY load of hot boycream!"
mc "You bring the best out of me. Shall we move on perhaps?"
ay "I'll slurp up your plentiful offering and I'm ready to go ANOTHER ROUND!"
jump AylaFuckChoiceBx

label AylaImpregnationx:
scene aylapreimpregnate01 with dissolve
ay "What are you doing? This is NOT how babies are made!"
mc "Just making sure you're wide open for the millions of tiny sperms I'm about to dump inside you..."
ay "Well hurry up, this is just boring, yours fingers in my poont...."
scene aylapreimpregnate02 with fastdissolve
play sound "Sounds/moaning.mp3"
ay "...TANG! AAAHH!"
mc "Seems like you like it after all..."
scene aylapreimpregnate03 with dissolve
mc "Get on all fours, this is the best position for me to stick my pud as DEEP as I can inside your tiny body."
ay "It'd better not go too far up my chest, I don't like getting my heart pummelled by a filthy teenage donkey-dick!"
mc "Errr. Right. I'll try and be careful then..."

play music "Sounds/womansex01.mp3"
label AylaPregnantSlowx:
hide aylaimpregfast
hide aylaimpregtopslow
hide aylaimpregtopfast
show aylaimpregslow
call screen aylaimpregslow01x
screen aylaimpregslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaPregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaPregnantFastx") 
    imagebutton:
        focus_mask True
        idle "v071/topview.png"
        hover "v071/topview.png"
        action Jump ("AylaImpregnateSlowx") 

label AylaImpregnateSlowx:
hide aylaimpregslow
hide aylaimpregfast
hide aylaimpregtopfast
show aylaimpregtopslow
call screen aylaimpregtopslow01x
screen aylaimpregtopslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaPregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaImpregnateFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AylaPregnantSlowx") 

label AylaPregnantFastx:
hide aylaimpregslow
hide aylaimpregtopslow
hide aylaimpregtopfast
show aylaimpregfast
call screen aylaimpregfast01x
screen aylaimpregfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaPregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaPregnantSlowx") 
    imagebutton:
        focus_mask True
        idle "v071/topview.png"
        hover "v071/topview.png"
        action Jump ("AylaImpregnateFastx") 

label AylaImpregnateFastx:
hide aylaimpregslow
hide aylaimpregfast
hide aylaimpregtopslow
show aylaimpregtopfast
call screen aylaimpregtopfast01x
screen aylaimpregtopfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaPregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("AylaImpregnateSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AylaPregnantFastx") 
            
label AylaPregnantEndx:
ay "Come on, blow your seed already, you're destroying my uterus with your giant pussy-pounder!"
mc "Alright, you asked for it!"
stop music
window hide
scene aylaimpregcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "TAKE THAT RIGHT IN YOUR WOMB AYLA!"
play music "Sounds/splooge02.mp3"
with fastflash
ay "You're pumping it FULL in just a single shot!"
scene aylaimpregcum02 with dissolve
stop music
play sound "Sounds/splooge01.mp3"
ay "It's POURING out, there's just TOO MUCH young spunk inside me!"
window hide
with fastflash
mc "Damn right, can't stop NUTTING!"
window hide
play channel1 "Sounds/splooge02.mp3"
play channel2 "v07/creampie.mp3"
scene aylaimpregcum01b with fastdissolve
$ renpy.pause(0.5, hard=True)
ay "I'm so FULL, I can now feel it BURSTING out of my vagina with each powerful thrust of your cum-missile! AAAH!"
with fastflash
mc "RHAAA!"
scene aylaimpregcum02b with fastdissolve
$ renpy.pause(0.5, hard=True)
with fastflash
ay "Oooh, ssooo much CUM, AAAHH! I'm squirting!"
window hide
scene aylaimpregcum01b with fastdissolve
$ renpy.pause(0.5, hard=True)
mc "Take that Ayla, more of my heavy dose, RHAAA!"
scene aylaimpregcum02b with fastdissolve
$ renpy.pause(0.5, hard=True)
mc "That's it, the last of my dozen teenage MONSTER CUMSHOTS! RHAAA!"
with fastflash
stop channel1
stop channel2
ay "Oh my God, you HOSED down my insides with your virile cream..."
scene aylaimpregcum03 with dissolve
play sound "Sounds/panting.mp3"
mc "...And I think my balls are actually empty this time... Need to sleep to replenish them..."
scene aylaimpregcum04 with dissolve
ay "My poor pussy got WRECKED. This impregnation had better work, because I don't think I can go through such an ordeal again..."
mc "Well, at least, you didn't find it boring. So let's go to sleep, I need strength for tomorrow..."
play sound "Sounds/moaning03.ogg"
ay "...Alright, just give me a moment..."
jump AylaGallery

label AylaGallery08:
play sound "Sounds/dream.mp3"
scene classdream
show dreamayla01
play music "Sounds/showerstrip.mp3"
ay "God I'm just so BORED."
mc "Maybe we could play a game to keep ourselves entertained?"
ay "What game?"
mc "Err... How about strip poker. But without cards. Goes quicker."
hide dreamayla01
show dreamayla02
with fastdissolve
ay "Alright, but only because I'm so BORED. So how do we play it?"
mc "First, you need to turn round..."
hide dreamayla02
show dreamayla03
with fastdissolve
ay "That doesn't sound like fun AT ALL. But I'll do it anyway. God, SSSOOO BORED!"
mc "It's fun for me at least... Now pull your top off and let your nipples say hi to me."
ay "Why? This game is so STUPID. But I guess I have nothing BETTER to do right now."
hide dreamayla03
show dreamayla04
with fastdissolve
ay "There. Are you happy you sick PERVERT?"
mc "Quite so, quite so."
ay "So, what next, FREAK?"
mc "Pull your panties down too."
hide dreamayla04
show dreamayla05
with fastdissolve
ay "This game had better become more interesting SOON. I'm already getting BORED!"
mc "It will, don't worry, it will."
hide dreamayla05
show dreamayla06
with fastdissolve
ay "I'm waiting... All naked and WAITING for this stupid game to get BETTER."
mc "Alright, let's kick it up a notch then."
hide dreamayla06
show dreamayla07
with fastdissolve
mc "There. Is the game getting more interesting now?"
ay "I guess so. This thing is WAY bigger than my boyfriend's for sure..."
mc "And it can deliver way more cream than him too!"
ay "I don't believe you. I need to check myself."
mc "Be my guest..."
hide dreamayla07
show dreamayla08
with fastdissolve
ay "Alright, let's see... How to make sure you're not lying..."
mc "Maybe tug it hard and fast?"
ay "Yes, I like that new game better than the old one..."
window hide
hide dreamayla08
show dreamayla09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla09
show dreamayla08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla08
show dreamayla09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla09
show dreamayla08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla08
show dreamayla09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla09
show dreamayla08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla08
show dreamayla09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla09
show dreamayla08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla08
show dreamayla09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla09
show dreamayla08
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla08
show dreamayla09
with fastdissolve
$ renpy.pause(0.2, hard=True)
hide dreamayla09
show dreamayla08
with fastdissolve
$ renpy.pause(0.2, hard=True)
mc "I'm about to blow my load Ayla!"
ay "Go ahead, I don't care if you get some on me. I bet it won't be too much trouble cleaning it anyway."
hide dreamayla08
show dreamayla10
with fastdissolve
ay "What the FUCK? You're BLASTING all the way up to the ceiling!?!?"
ay "That is definitely already WAY MORE than my boyfriend."
hide dreamayla10
show dreamayla11
with fastdissolve
ay "You ARSEHOLE! Look at what you've done! I'm covered in your filthy SEED!"
mc "You wanted to know if I came more than your boyfriend. Now you know."
hide dreamayla11
show dreamayla12
with fastdissolve
ay "Alright. I forgive you. THIS ONCE. But only because your cum is DELICIOUS."
mc "I was hoping you'd notice."
stop music
jump AylaGallery