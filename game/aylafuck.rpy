label AylaFuck01:
hide screen calendar
hide screen mcstats
if pregay and pregaystart >= 3:
    scene bedroom01
    show aylapregnant02a
    with fade
    ay "What do you want? Can't you see I'm bloody PREGNANT?"
    mc "Ah, so you mean you're TOO pregnant for sex?"
    hide aylapregnant02a
    show aylapregnant02b
    with fastdissolve
    ay "Well, this baby is BORING and SEX is much LESS boring, but..."
    mc "Yeah, keep going, think it through."
    hide aylapregnant02b
    show aylapregnant02c
    with fastdissolve
    ay "You're just a PERVERT! You'd fuck anything including a heavily pregnant girl!"
    mc "Only to make your life less boring, nothing more, I swear!"
    hide aylapregnant02c
    show aylapregnant02a
    with fastdissolve
    ay "Just don't BOTHER calling me again until AFTER I give birth to this baby, FREAK!"
    window hide
    hide aylapregnant02a with dissolve
    $ weekfuckedayla = True    
    jump Bedroom
scene bedroom01 with fade
show ayla01
$ alienfuck = True
$ weekfuckedayla = True
menu:
    "Run scene":
        pass
    "Skip scene":
        jump AylaEnd
ay "Why did you call me in the middle of the night? I was SLEEPING!"
mc "Well, I've got a better activity for you than this snore-fest."
hide ayla01
show ayla02
with fastdissolve
ay "And what would that be?"
mc "SEX. You owe me sexual allegiance and respect as a girl in my harem, remember."
ay "Pff. I don't even know why I bothered joining your stupid harem. Alright, let's get it over with then. What should I wear?"
menu:
    "A kinky BDSM outfit. I feel like being dominated by a short angry girl tonight.":
        hide ayla02
        show ayla06
        with fastdissolve
        ay "I can do that. I LOVE dominating men. Especially wannabe studs like you!"
        jump AylaLingerie01
    "The sexiest outfit you have for the sexiest girl in my harem.":
        hide ayla02
        show ayla03
        with fastdissolve
        ay "I only wear this outfit for my REAL boyfriend. Unless, of course, I am covered in Holy Baby Oil."
        if holyoil:
            mc "And I so happen to have a bottle of the stuff."
            hide ayla03
            show ayla06
            with fastdissolve
            ay "Really, you do? Alright, I'll go and fetch my special lingerie then!"
            jump AylaLingerie02
        if holyoil == False:
            mc "And you don't have any? I mean, you're a member of the Church, you should have some Holy Baby Oil with you at all times."
            if aylaoil:
                hide ayla03
                show ayla02
                with fastdissolve  
                ay "I suppose... Just this ONCE. I'll use my own stock of Holy Baby Oil; But you'll have to find some yourself in the future."
                $ aylaoil = False
                jump AylaLingerie02
            hide ayla03
            show ayla05
            with fastdissolve            
            ay "So what, I used it! What you gonna do about it? It's the kinky BDSM session for you tonight then, you have no choice!"
            mc "Alright, alright, gee."
            if persistent.tipson:
                show babyoiltip at tips with dissolve
                pause
                hide babyoiltip            
            jump AylaLingerie01
        
label AylaLingerie01:
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
jump AylaFuckChoiceB

label AylaLingerie02:
play music "v07/datemusic.mp3"
scene bedroom01 with fade
show aylalingerie01 at center with moveinright
ay "I am ready to atone for my sins!... by letting you fuck me senseless with your punishing ramrod."
if churchnickname:
    mc "Very appropriate since I am well known within the clergy as \"[name] the Punisher\"."
    hide aylalingerie01
    show aylalingerie05
    with fastdissolve    
    ay "Indeed you are! Let me thank the invisible sky to have unleashed you on such a dreadful sinner as myself!"
if churchnickname == False:
    hide aylalingerie01
    show aylalingerie05
    with fastdissolve
    ay "And since you are going to punish me, I pray to the Phallus Lord to grant you a new nickname. \"[name] the Punisher\"!"
    window hide
    show mcchurchnickname at posmission
    $ renpy.pause(2.0, hard=True)
    $ churchnickname = True
    mc "Alright! I have a nickname now! Woo-ooh! Prepare to be PUNISHED by \"[name] the Punisher\", Ayla!"
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

label AylaFuckChoiceA:
stop music
$ alienfuck = True
$ weekfuckedayla = True
scene bedroom03b blurred
show aylaready01
with dissolve
ay "What could we do to please the Phallus Lord, while at the same time, HAVING FUN?"
mc "And the aliens. Err... I mean, the angels in the sky."
label AylaFuckChoiceAb:
menu:
    "Wrap those massive titties around my giant pole.":
        ay "Ooh, a titfuck? Then I'll rub Holy Baby Oil all over YOU too! To make everything nice and slippery..."
        mc "Yeah, coat my muscled body in oil, and don't forget my knob."
        jump AylaTits
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
        jump AylaMissionary
    "I've been a sinner too and I'm not allowed to jerk off anymore. May your feet do the jerking as a replacement then.":
        ay "My feet as as substitute for your unholy hands? I like the idea..."
        jump AylaFootJob
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
        jump AylaAnal
    "I'll put a smile on your face by giving you the gift of LIFE. Prepare to get IMPREGNATED, Ayla!" if pregayready >= 3 and impregnatedsomeone == False and babyayla == False:
        ay "What? A baby? I... This is actually quite exciting for once. DO IT! PUMP YOUR SEED IN ME AND MAKE ME PREGNANT!"
        $ impregnatedsomeone = True
        jump AylaImpregnation
    "I'm done, let's go to sleep.":
        jump AylaEnd

label AylaTits:
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
label AylaTitsSlow:
hide aylatitsfast
show aylatitsslow
call screen aylatitsslow01
screen aylatitsslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaTitsEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaTitsFast") 

label AylaTitsFast:
ay "You want me to wrap my jugs around your engorged monsterpole faster [name]? That's what you want isn't it, you BAD BOY! Just watch then..."
hide aylatitsslow
show aylatitsfast
call screen aylatitsfast01
screen aylatitsfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaTitsEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaTitsSlow") 

label AylaTitsEnd:
mc "FUUUUUUCK! This is too good, I'm gonna..."
hide aylatitsfast
hide aylatitsslow
show aylatitscum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc"....CUUUUMMMM!"
ay "YES! Release that jizz, let it HOSE my tits and face down, GIVE ME ALL THAT SWEET YOUNG CUM!"
scene bedroom40 blurred
show aylatitscum02
with dissolve
ay "Your sperm is landing down on my face from so HIGH ABOVE, it's like a CUM-SHOWER!"
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
jump AylaFuckChoiceAb

label AylaFootJob:
scene bedroom41 blurred
show aylaprefoot01
with dissolve
ay "Look at that monster cock! It's sssooo BIG!"
mc "All the better to please you."
ay "Now stay back while my feet do all the jerking... No hands!"
mc "Fine by me, though I wonder if your tiny feet will be enough stimul..."
scene bedroom18 blurred with dissolve
play music "Sounds/wank.mp3"
label AylaFootJobSlow:
hide aylafootfast
show aylafootslow
mc "...ation, AAAH!"
window hide
call screen aylafootslow01
screen aylafootslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaFootJobEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaFootJobFast") 

label AylaFootJobFast:
ay "What if I increased the tempo? Will you give me a nice big FAT load now?"
hide aylafootslow
show aylafootfast
call screen aylafootfast01
screen aylafootfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaFootJobEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaFootJobSlow") 

label AylaFootJobEnd:
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

label AylaHandSlow:
hide aylahandfast
hide aylahandpovslow
hide aylahandpovfast
scene bedroom37
show aylahandslow
call screen aylahandslow01
screen aylahandslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaHandEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaHandFast") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("AylaHandPOVSlow") 
        
label AylaHandPOVSlow:
hide aylahandfast
hide aylahandslow
hide aylahandpovfast
scene bedroom08 blurred
show aylahandpovslow
call screen aylahandpovslow01
screen aylahandpovslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaHandEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaHandPOVFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AylaHandSlow") 

label AylaHandPOVFast:
hide aylahandfast
hide aylahandslow
hide aylahandpovslow
scene bedroom08 blurred
show aylahandpovfast
call screen aylahandpovfast01
screen aylahandpovfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaHandEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaHandPOVSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AylaHandFast") 

label AylaHandFast:
hide aylahandslow
hide aylahandpovslow
hide aylahandpovfast
scene bedroom37 blurred
show aylahandfast
call screen aylahandfast01
screen aylahandfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaHandEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaHandSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("AylaHandPOVFast") 

label AylaHandEnd:
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
jump AylaFuckChoiceAb
    
label AylaMissionary:
scene bedroom16
show aylaarnieprefuck01
with dissolve
ay "You're gonna FUCK ME with your massive rod [name]?"
mc "Yeah, that's what you want, isn't it?"
ay "I don't know, it's just so BIG and I'm so TINY!"
mc "Don't worry, it'll fit. The dev is pretty good at making my cock fit into tiny holes."
scene bedroom20 blurred
play music "Sounds/womansex01.mp3"
label AylaMissionarySlow:
hide aylamissionaryfast
show aylamissionaryslow
call screen aylapoundslow01
screen aylapoundslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaMissionaryEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaMissionaryFast") 

label AylaMissionaryFast:
hide aylamissionaryslow
show aylamissionaryfast
call screen aylapoundfast01
screen aylapoundfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaMissionaryEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaMissionarySlow") 

label AylaMissionaryEnd:
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
jump AylaFuckChoiceAb
    
label AylaAnal:
scene bedroom12
show aylapreanal01
with dissolve
mc "Are you ready?"
ay "You're already inside so deep!"
mc "That's just the tip, Ayla. I haven't started. There's 15 more inches to go. Here, I'll show you."
scene bedroom08 blurred with dissolve
play music "Sounds/womansex02.mp3"
label AylaAnalSlow:
hide aylaanalfast
show aylaanalslow
ay "AAAAH!"
call screen aylaanalslow01
screen aylaanalslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaAnalFast") 

label AylaAnalFast:
ay "This is..."
ay "...so..."
ay "...GOOD... FASTER, PLEASE!"
hide aylaanalslow
show aylaanalfast
call screen aylaanalfast01
screen aylaanalfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaAnalSlow") 

label AylaAnalEnd:
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
stop sound
scene bedroom03b blurred
show aylaready01
with dissolve
ay "And what do you have in mind this time for poor little me?"
jump AylaFuckChoiceAb
    
label AylaFuckChoiceB:
$ alienfuck = True
$ weekfuckedayla = True
stop music
scene bedroom03b blurred
show aylalingerie20
with dissolve
ay "Mmmh, I wonder what I should do with my slave-boy..."
label AylaFuckChoiceBb:
menu:
    "Do your worse, I deserve to be punished Mistress Ayla!":
        ay "That's what I like to hear, slaveboy! So get on your back, I'm going to ride your giant cock till you explode in my pussy!"
        jump AylaRide
    "I could lick your delicious pussy for your personal pleasure, mistress Ayla!":
        ay "Ooh, that's a good idea. Like a good lapping-dog."
        jump AylaLick
    "Torture my cock, any way you see fit Mistress.":
        ay "I know how... With my HUGE tits. You like my huge tits, don't you?"
        mc "Yes I do. They're so MASSIVE on a such a tiny frame..."
        jump AylaTitsb
    "I'm done, let's go to sleep.":
        jump AylaEnd

label AylaRide:
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
label AylaRideSlow:
hide aylaridefast
show aylarideslow
call screen aylarideslow01
screen aylarideslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaRideEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaRideFast") 

label AylaRideFast:
ay "I'm gonna pump the cumload out of your fat balls even FASTER now!"
hide aylarideslow
show aylaridefast
call screen aylaridefast01
screen aylaridefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaRideEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaRideSlow") 

label AylaRideEnd:
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
jump AylaFuckChoiceB

label AylaLick:
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
label AylaLickSlow:
play sound "Sounds/lick.mp3"
hide aylalickfast
show aylalickslow
call screen aylalickslow01
screen aylalickslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaLickEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaLickFast") 

label AylaLickFast:
play sound "Sounds/lick.mp3"
ay "Lick my clit faster, swirl that tongue in there, [name]!"
hide aylalickslow
show aylalickfast
call screen aylalickfast01
screen aylalickfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaLickEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaLickSlow") 

label AylaLickEnd:
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
jump AylaFuckChoiceBb

label AylaTitsb:
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
label AylaTitsSlowb:
hide aylatitsfastb
show aylatitsslowb
call screen aylatitsslow01b
screen aylatitsslow01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaTitsEndb")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaTitsFastb") 

label AylaTitsFastb:
ay "Look at you, your face is contorted with the aching pain of imminent release. Let me bring you over the EDGE!"
hide aylatitsslowb
show aylatitsfastb
call screen aylatitsfast01b
screen aylatitsfast01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaTitsEndb")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaTitsSlowb") 

label AylaTitsEndb:
mc "FUUUUUUCK! This is too good, I'm gonna..."
hide aylatitsfastb
hide aylatitsslowb
show aylatitscum01b
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "...CUUUUMMMM!"
with fastflash
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
jump AylaFuckChoiceB

label AylaImpregnation:
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
label AylaPregnantSlow:
hide aylaimpregfast
hide aylaimpregtopslow
hide aylaimpregtopfast
show aylaimpregslow
call screen aylaimpregslow01
screen aylaimpregslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaPregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaPregnantFast") 
    imagebutton:
        focus_mask True
        idle "v071/topview.png"
        hover "v071/topview.png"
        action Jump ("AylaImpregnateSlow") 

label AylaImpregnateSlow:
hide aylaimpregslow
hide aylaimpregfast
hide aylaimpregtopfast
show aylaimpregtopslow
call screen aylaimpregtopslow01
screen aylaimpregtopslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaPregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaImpregnateFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AylaPregnantSlow") 

label AylaPregnantFast:
hide aylaimpregslow
hide aylaimpregtopslow
hide aylaimpregtopfast
show aylaimpregfast
call screen aylaimpregfast01
screen aylaimpregfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaPregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaPregnantSlow") 
    imagebutton:
        focus_mask True
        idle "v071/topview.png"
        hover "v071/topview.png"
        action Jump ("AylaImpregnateFast") 

label AylaImpregnateFast:
hide aylaimpregslow
hide aylaimpregfast
hide aylaimpregtopslow
show aylaimpregtopfast
call screen aylaimpregtopfast01
screen aylaimpregtopfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaPregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("AylaImpregnateSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AylaPregnantFast") 
            
label AylaPregnantEnd:
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
$ pregay = True
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
    
label AylaEnd:
show screen calendar
show screen mcstats
scene aylamcsleep with fade
$ loc = "bedroom"
play sound "Sounds/snoring.mp3"
pause 3
call NewDay
jump Bedroom