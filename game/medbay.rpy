label Medbay:
show screen calendar
show screen mcstats
$ loc = "medbay"
$ period = 3
image medbay03 blurred = im.Blur("medbay/medbay03.jpg", 1.5)
image medbay04 blurred = im.Blur("medbay/medbay04.jpg", 1.5)
image medbay05 blurred = im.Blur("medbay/medbay05.jpg", 1.5)

if mcinjuredvirus:
    scene medbay03
    show rachelvirus01
    with fade
    ra "According to your health card, you caught Covid-19. This thing hasn't been around since like...last year or something."
    ra "As per the rules of social distancing, no hanky-panky for you tonight! You rest, and tomorrow, you'll feel better."
    ra "Either that or you'll die from pneumonia, since we don't have any ventilators here. They all belong to Jared Cuckner."
    jump MedBayNight
if mcinjuredcock:
    scene medbay03
    show rachel02
    with fade
    ra  "I had a look at your health card already. And then at your cock... Yuck, it's really GROSS!"
    mc "Hey, that's not a very nice thing to say!"
    hide rachel02
    show rachel01
    with fastdissolve
    ra "Sorry but even a bimbo nurse like me has standards! You rest and hopefully that horsedick of yours will recover from whatever it is that happened to it..."
    jump MedBayNight

scene medbay03
show rachel02
with fade
ra "Ooh, my poor boy, you got injured today? Nurse Rachel will make sure you recover in no time!"
if mcinjuredfbi:
    ra  "Let me check your health card... What, you almost committed virtual suicide?"
    menu:
        "Err, yeah, it sounds bad the way you say it, but I was conned!":
            hide rachel02
            show rachel04
            with fastdissolve
            if money >= 5:
                ra "Mmmh, so you're easily conned then... Maybe I can interest you in some SEX for like, 5$?"
                mc "Alright, that sounds like a great deal!"
                $ money -= 5
                hide rachel04
                show rachel06
                with fastdissolve
                ra "You're so silly, I normally give you sex for FREE!"
                hide rachel06
                jump MedBaySex
            if money >= 1 and money <= 4:
                ra "Mmmh, so you're easily conned then... Maybe I can interest you in some SEX for like, [money]$?"
                mc "Alright, that sounds like a great deal!"
                $ money = 0
                hide rachel04
                show rachel06
                with fastdissolve
                ra "You're so silly, I normally give you sex for FREE!"
                hide rachel06
                jump MedBaySex
            if money == 0:
                ra "I'd make you pay for sex, but you're just too damn POOR! So we'll have sex for FREE!"
                hide rachel04
                jump MedBaySex
        "It was part of some crazy test. I survived so I'm not THAT mentally weak.":
            hide rachel02
            show rachel01
            with fastdissolve
            ra "Maybe... But you're PHYSICALLY WEAK now. You rest, and tomorrow you'll feel better."
            hide rachel01
            with dissolve
            jump MedBaySex
if mcinjuredmushroom:
    ra  "Let me check your health card... What, you ate some poisonous mushrooms?"
    menu:
        "They looked so cute, how could I tell?":
            hide rachel02
            show rachel04
            with fastdissolve
            ra "Mmmh, I thought I was the dumb bimbo here but I see you're an even dumber himbo. So we're a good match. Let's have sex!"
            hide rachel04
            jump MedBaySex
        "I was forced to eat them by...err... a very convincing lady.":
            hide rachel02
            show rachel05
            with fastdissolve
            ra "So you're totally gullible then... The only cure to your affliction is SEX. You believe me, right?"
            mc "Err...Sure, it makes total sense."
            hide rachel05
            with dissolve
            jump MedBaySex
if mcinjuredstomach:
    ra  "Let me check your health card... What, you drank some Lysol?"
    menu:
        "Yeah, so? President-for-life Trumpf says it's good, and that's good enough for me cos I'm gullible.":
            hide rachel02
            show rachel04
            with fastdissolve
            ra "Mmmh, I thought I was the dumb bimbo here but I see you're an even dumber himbo. So we're a good match. Let's have sex!"
            hide rachel04
            jump MedBaySex
        "I was forced to drink it after being kidnapped by a bounty huntress.":
            hide rachel02
            show rachel01
            with fastdissolve
            ra "Your adventures are really exciting! But you must have clearly failed in your mission in that instance. So you rest, and tomorrow you'll feel much better!"
            hide rachel01
            with dissolve
            jump MedBayNight
if mcinjuredcurse:
    ra  "Let me check your health card... What, you were cursed by the Phallus Lord?"
    menu:
        "Fortunately, he didn't curse my cock.":
            hide rachel02
            show rachel01
            with fastdissolve
            ra "Ooh, that's good to know! And there's only one way to lift the curse. SEX!"
            hide rachel01
            jump MedBaySex
        "I didn't do nothing wrong, I swear!":
            hide rachel02
            show rachel04
            with fastdissolve
            ra "You say that, but you must have. And I don't want to catch your curse. So you rest, and tomorrow you'll feel much better!"
            hide rachel04
            with dissolve
            jump MedBayNight
if mcinjureddoor:
    ra  "Let me check your health card... What, you've got nasty hematomas?"
    menu:
        "Nasty, but acquired in the course of my duty as the savior of humanity.":
            hide rachel02
            show rachel01
            with fastdissolve
            ra "Ooh, you truly are so brave! Such a brave young boy deserves a SEXUAL reward!"
            hide rachel01
            jump MedBaySex
        "Knock knock.":
            hide rachel02
            show rachel04
            with fastdissolve
            ra "Err... Who's there?"
            mc "Nobody. I was telling you how I got injured. Trying to knock a door open."
            hide rachel04
            show rachel06
            with fastdissolve
            ra "You're such a silly boy. A silly boy who needs to go to sleep now. You rest, and tomorrow you'll feel much better!"            
            hide rachel06
            with dissolve
            jump MedBayNight
if mcinjuredjaguar:
    ra  "Let me check your health card... What, you've got scratches all over your body?"
    menu:
        "Hysterical admiring fans can be pretty crazy with their nails.":
            hide rachel02
            show rachel01
            with fastdissolve
            ra "Ooh, my poor boy. It must be hard having to fight off all these girls who want a taste of your MONSTER COCK!"
            hide rachel01
            show rachel02
            with fastdissolve
            ra "Fortunately, I don't have to fight any of THEM off, I've got you all TO MYSELF tonight!"
            hide rachel02
            with dissolve
            jump MedBaySex
        "I was viciously attacked by a jaguar. I let him win out of respect for Mother Nature. (+1 Club Sierra)":
            call PlusSierra 
            hide rachel02
            show rachel04
            with fastdissolve
            ra "Your respectful behavior is laudable... In bizarro-world. You rest, and tomorrow you'll feel much better!"
            hide rachel04
            with dissolve
            jump MedBayNight
if mcinjuredgator:
    ra  "Let me check your health card... What, you've got bite marks all over your body?"
    menu:
        "Hickies. Not bite marks.":
            hide rachel02
            show rachel01
            with fastdissolve
            ra "Ooh, my poor boy. It must be hard having to fight off all these girls who want a taste of your MONSTER COCK!"
            hide rachel01
            show rachel02
            with fastdissolve
            ra "Fortunately, I don't have to fight any of THEM off, I've got you all TO MYSELF tonight!"
            hide rachel02
            with dissolve
            jump MedBaySex
        "I was viciously attacked by some gators. I let them win out of respect for Mother Nature. (+1 Club Sierra)":
            call PlusSierra   
            hide rachel02
            show rachel04
            with fastdissolve
            ra "Your respectful behavior is laudable... In bizarro-world. You rest, and tomorrow you'll feel much better!"
            hide rachel04
            with dissolve
            jump MedBayNight
if mcinjuredfaint:
    ra  "Let me check your health card... What, you fainted?"
    menu:
        "I pushed myself too hard during an intense MUSCLE TRAINING session.":
            hide rachel02
            show rachel01
            with fastdissolve
            ra "Ooh, my poor boy. I hope your MAIN muscle is still functional, cos I need some CUM TRAINING on my body tonight!"
            hide rachel01
            with dissolve
            jump MedBaySex
        "I got conned by a genie. Wasted my wish on her.":
            hide rachel02
            show rachel04
            with fastdissolve
            ra "Maybe you should have asked for a bigger BRAIN. You rest, and tomorrow you'll feel much better!"
            hide rachel04
            with dissolve
            jump MedBayNight
if mcinjuredsalad:
    ra  "Let me check your health card... What, you have stomach pain?"
    menu:
        "Yeah, Montezuma's revenge...":
            hide rachel02
            show rachel04
            with fastdissolve
            ra "Hum, in that case, I'm not sure I want to get anywhere near you... I don't like sex with farts."
            hide rachel04
            with dissolve
            jump MedBayNight
        "I had to sacrifice my bowels for the sake of humanity.":
            hide rachel02
            show rachel01
            with fastdissolve
            ra "Your bowels deserve praise... And maybe you deserve a little reward..."
            hide rachel01
            with dissolve
            jump MedBaySex
if mcinjuredalien:
    ra  "Let me check your health card... What, you got shot?"
    menu:
        "Yeah, by some fucking space alien no less!":
            hide rachel02
            show rachel04
            with fastdissolve
            ra "Ah, I see. You also have mental side effects. I will tell the doctor. You rest, and tomorrow you'll feel much better!"
            hide rachel04
            with dissolve
            jump MedBayNight
        "It's a tough job being a hero.":
            hide rachel02
            show rachel01
            with fastdissolve
            ra "We can't thank you enough for your bravery... Maybe you deserve a little reward..."
            hide rachel01
            with dissolve
            jump MedBaySex
if mcinjuredgun:
    ra "Let me check your health card... What, you got shot?"
    menu:
        "Yeah, right in the buttcheek no less!":
            hide rachel02
            show rachel04
            with fastdissolve
            ra "Ah, I see. So you were fleeing then... You rest, and tomorrow you'll feel much better!"
            hide rachel04
            with dissolve
            jump MedBayNight
        "It's a tough job being a hero.":
            hide rachel02
            show rachel01
            with fastdissolve
            ra "We can't thank you enough for your bravery... Maybe you deserve a little reward..."
            hide rachel01
            with dissolve
            jump MedBaySex
if mcinjuredmichiko:
    ra "Let me check your health card... What, you got beaten up?"
    menu:
        "Yeah, by Michiko no less!":
            hide rachel02
            show rachel01
            with fastdissolve
            ra "She was only doing her job helping you train... You rest, and tomorrow you'll feel much better!"
            hide rachel01
            with dissolve
            jump MedBayNight
        "I LET myself get beaten up. Part of my top secret training procedure.":
            hide rachel02
            show rachel04
            with fastdissolve
            ra "mmmh.. Sounds fishy. But I'm horny so I'll give you a reward anyway!"
            hide rachel04
            with dissolve
            jump MedBaySex            
if mcinjuredopala:
    ra  "Let me check your health card... What, you have groin cramps?"
    menu:
        "Yeah, I was fucked to almost death by Queen Opala...":
            hide rachel02
            show rachel04
            with fastdissolve
            ra "Ah, I see. You also have mental side effects. I will tell the doctor. You rest, and tomorrow you'll feel much better!"
            hide rachel04
            with dissolve
            jump MedBayNight
        "I had to use my mighty scepter to subdue a tough enemy.":
            hide rachel02
            show rachel01
            with fastdissolve
            ra "Your scepter deserves praise... If it's still in working order, I'm ready to praise it!"
            hide rachel01
            with dissolve
            jump MedBaySex
if mcinjuredprisoner:
    ra  "Let me check your health card... What, you have choking marks on your neck?"
    menu:
        "Some sexual games that went wrong real fast...":
            hide rachel02
            show rachel04
            with fastdissolve
            with fastdissolve
            ra "I know what you mean, happens to me all the time with Dr Tara... And I think it's time for you to choke ME with your huge cock, what do you say?"
            mc "Alright!"
            hide rachel04
            with dissolve
            jump MedBaySex
        "I had to fight my way through an army of leg-scissoring Amazons.":
            hide rachel02
            show rachel01
            with fastdissolve
            with fastdissolve
            ra "Ah, I see, you are totally delusional. You rest, and tomorrow you'll feel much better!"
            hide rachel01
            with dissolve
            jump MedBayNight
if mcinjuredsand:
    ra  "Let me check your health card... What, your airways are clogged with sand?"
    menu:
        "I like to get REAL close to Mother Nature... And taste her. (+1 Club Sierra)":
            call PlusSierra
            hide rachel02
            show rachel04
            with fastdissolve
            ra "A bit too close I'd say... You rest, and tomorrow you'll feel much better!"
            hide rachel04
            with dissolve
            jump MedBayNight
        "*hiss* Nothing... *breath* to worry... *hiss* about.":
            hide rachel02
            show rachel01
            with fastdissolve
            ra "You can barely talk so I'll assume you can barely fuck. You rest, and tomorrow you'll feel much better!"
            hide rachel01
            with dissolve
            jump MedBayNight
if mcinjuredgwen:
    ra  "Let me check your health card... Hum, a nasty bruise in the face? Training with Michiko?"
    menu:
        "No, it was Gwen. she packs a mighty punch":
            hide rachel02
            show rachel04
            with fastdissolve
            ra "Such a tiny girl? You're not as strong as I thought... You rest, and hopefully tomorrow, you won't be a wimp anymore."
            hide rachel04
            with dissolve
            jump MedBayNight
        "I fought... an army of... er...":
            hide rachel02
            show rachel01
            with fastdissolve
            ra "You can barely talk so I'll assume you can barely fuck. You rest, and tomorrow you'll feel much better!"
            hide rachel01
            with dissolve
            jump MedBayNight
if mcinjuredfight:
    ra "Let me check your health card... What, you got beaten up?"
    menu:
        "Yeah, but you should see the other guy's face. I beat him to a pulp.":
            hide rachel02
            show rachel01
            with fastdissolve
            ra "I find that hard to believe. Its' YOUR face that looks like a pineapple right now... You rest, and tomorrow you'll feel better!"
            hide rachel01
            with dissolve
            jump MedBayNight
        "I LET myself get beaten up. Part of my top secret training procedure.":
            hide rachel02
            show rachel04
            with fastdissolve
            ra "mmmh.. Sounds fishy. But I'm horny so I'll give you a reward anyway!"
            hide rachel04
            with dissolve
            jump MedBaySex            
if mcinjuredtaser:
    ra "Let me check your health card... What, you got tasered?"
    menu:
        "And I'm not even black. Go figure.":
            hide rachel02
            show rachel01
            with fastdissolve
            ra "The New United States Police Force only hires color-blind people I heard... You rest and tomorrow, you'll feel better!"
            hide rachel01
            with dissolve
            jump MedBayNight
        "I was testing my resistance to EXTREME torture. I won since I'm still alive.":
            hide rachel02
            show rachel04
            with fastdissolve
            ra "Wow, you're such a brave boy. Good thing you weren't tasered in the GROIN, cos I want to jump on it right now!"
            hide rachel04
            with dissolve
            jump MedBaySex            

label MedBaySex:
show rachel03
ra "I hope you can get that monster cock hard despite your injury [name]..."
mc "Don't worry about me nurse Rachel, get your kit off and I'll get rock-hard in no time!"
hide rachel03
show rachel07
with fastdissolve
ra "Ta-da! Have you ever seen such HUGE boobies [name]?"
mc "No... They are the biggest around for sure!"
hide rachel07
show rachel08
with fastdissolve
ra "And what about my bubble butt? Do you like it?"
mc "My cock says yes!"
ra "Then, remove that bedsheet and show me!"

$ d2rollmedbay = renpy.random.randint(1, 2)
if d2rollmedbay == 1:
    jump MedbayInjured02

label MedbayNew:
stop music
scene medbay04 blurred with dissolve
play sound "Sounds/nurserachel.mp3"
show rachelsex01
with dissolve
ra "Mmmh, such a BIG piece of boymeat for nurse Rachel!"
hide rachelsex01
show rachelsex02
with fastdissolve
ra "I'm gonna have a LOT of fun with that giant cock!"

$ d4rollnursescene = renpy.random.randint(1, 4)
if d4rollnursescene == 1:
    jump MedbayWank
if d4rollnursescene == 2:
    jump MedbayButt
if d4rollnursescene == 3:
    jump MedbayTit
if d4rollnursescene == 4:
    jump MedBayBlow

label MedBayBlow:
ra "Now I'm gonna gobble your fat donkey-shaft!"
play music "Sounds/hardsucking.mp3"
scene medbay07 blurred
show rachelblow
with dissolve
call screen rachelblow01
screen rachelblow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("RachelBlowEnd")

label RachelBlowEnd:
mc "Oh, if you continue sucking me like a vacuum cleaner, I'm gonna cum..."
stop music
scene medbay06 blurred
show rachelblowcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "....anytime soon, RHAAA!"
stop music
hide rachelblowcum01
show rachelblowcum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "YES! Drink my ball-batter, gulp it down like a hungry cum-whore bimbo!"
ra "Ggglulluurb!"
hide rachelblowcum02
show rachelblowcum03
with fastdissolve
ra "Oooh, wow, I think I just drank a GALLON of sweet young teenage spunk! Yummy!"
mc "Phew.... My balls sure feel empty, nurse..."
if nurseblowjob == False:
    call LustPlusRachel
ra "Well, now you rest, after all, that's what you were supposed to be doing before I decided to have a cum dinner with your monster dong."
hide rachelblowcum03
with fastdissolve
$ nurseblowjob = True
$ period += 1
jump MedBayNight

label MedbayButt:
hide rachelsex02
show rachelbutta01
with fastdissolve
ra "Ooh, what do I feel snuck between my buttcheeks?"
hide rachelbutta01
show rachelbutta02
with fastdissolve
ra "Looks like a very LONG, THICK and HARD pole... That belongs in my little backhole!"
mc "0oh yeah! Go for it, nurse Rachel!"
scene medbay07 blurred
show rachelbutt
with dissolve
play sound "Sounds/fucksound.mp3"
call screen rachelbutt01
screen rachelbutt01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("RachelButtEnd")

label RachelButtEnd:
ra "Ooh, I can feel it... Your mega-cock is getting ready to burst, isn't it [name]?"
mc "Y..Yeah!"
hide rachelbutt
show rachelbuttfuckcum01
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
ra "That's it, naughty boy, empty your balls into nurse Rachel's backdoor! That will DEFINITELY make you feel BETTER!"
hide rachelbuttfuckcum01
show rachelbuttfuckcum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
ra "Oh my God, you're STILL spewing! How much sweet boycream did you have pent-up in those massive balls, poor boy? Good thing nurse Rachel is here to RELIEVE you!"
hide rachelbuttfuckcum02
show rachelbuttfuckcum03
with fastdissolve
ra "My butthole is just FULL OF CUM... How am I ever going to clean this mess before Tara finds out I've been butt-fucked by a patient? I'm in BIG TROUBLE!"
if nursebuttfuck == False:
    call LustPlusRachel
mc "I was passive, I take no responsibility at all. Just like Trumpf."
ra "Ooh, don't worry, just sleep tight until the morning... I'll just have to take what's coming to me for being such a SLUTTY NURSE!"
hide rachelbuttfuckcum03
with fastdissolve
$ nursebuttfuck = True
$ period += 1
jump MedBayNight

label MedbayWank:
hide rachelsex02
show rachelwank00
with fastdissolve
ra "Look at all those veins.... The biggest one is as thick as my middle finger! I'm gonna pump your shaft!"
hide rachelwank00
play sound "Sounds/wank.mp3"
show rachelwank
call screen rachelwank01
screen rachelwank01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("RachelWankEnd")

label RachelWankEnd:
ra "So, you're not coming yet? Then maybe I should turn round to let you lick my pussy... That should get your juices going, right?"
mc "It might help indeed..."
stop sound
hide rachelwank
show rachellick01
with fastdissolve
play sound "Sounds/womanmoan.mp3"
ra "Mmmh, your tongue on my naughty clit... Soo nice..."
mc "I think I need to expand that aperture a bit more..."
ra "Oooh, what do you have in mind naughty boy?"
show rachellick01b
mc "Just a bit of probing so see how deep the rabbit-hole goes..."
hide rachellick01b
hide rachellick01
show rachellick02
with fastdissolve
ra "Oooh, is it deep enough for you mister? You do know that I can't take your cock in there, I belong to Dr Tara's harem, silly boy!"
hide rachellick02
show rachelbutta01
with fastdissolve
ra "Ooh, what do I feel snuck between my buttcheeks?"
hide rachelbutta01
show rachelbutta02
with fastdissolve
ra "Looks like a very LONG, THICK and HARD pole..."
mc "Fuck, you're gonna make me nut nurse..."
scene medbay05 blurred
show rachelbuttcum01
with dissolve
ra "Yes, keep spurting [name], I need you to empty your balls of their virile seed so you can sleep tight tonight..."
mc "RHAAA, I'm coming non-stop!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
hide rachelbuttcum01
show rachelbuttcum02
with fastdissolve
ra "Ooh, I can feel TONS of warm spunk oozing down my back..."
hide rachelbuttcum02
show rachelbuttcum03
with fastdissolve
if nursewank == False:
    call LustPlusRachel
ra "I think I EMPTIED your BIG balls! So go to sleep now. Doctor Tara might barge in at any moment and I don't want her to see me covered in naughty boyscum (giggles)!"
hide rachelbuttcum03
with fastdissolve
$ nursewank = True
$ period += 1
jump MedBayNight

label MedbayTit:
ra "Maybe I should... rub it with my bosom, would you like that [name]?"
mc "I sure would, nurse Rachel!"
hide rachelsex02
show racheltits00
with fastdissolve
ra "I think your young MONSTERCOCK fits nicely between my HUGE melons, they were made for dealing with such a BIG FAT DONKEY-DICK!"
hide racheltits00
show racheltits
play music "Sounds/wank.mp3"
call screen racheltit01
screen racheltit01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("RachelTitEnd")

label RachelTitEnd:
stop music
hide racheltits
show racheltitscum01
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
ra "Ooh, look at all that cum FLYING everywhere! Empty your BULL BALLS so you can sleep nice and tight tonight, [name]!"
hide racheltitscum01
show racheltitscum02
with fastdissolve
ra "Mmmh, I love the feel of your warm cumshots landing heavily on my massive breasts! Keep pumping that fat load [name]!"
mc "Fuck, I'm nutting NON-STOP!"
hide racheltitscum02
show racheltitscum03
with fastdissolve
if nursetitfuck == False:
    call LustPlusRachel
$ nursetitfuck = True
ra "There you go, sleep tight now, I'm going to slurp all that yummy jizz before Doctor Tara arrives... She wouldn't like seeing her harem girl covered in your thick scum!"
hide racheltitscum03
with fastdissolve
$ period += 1
jump MedBayNight

label MedbayInjured02:
scene medbay03 with hpunch
show rachel08
ta "What the hell is going on here? RACHEL, I've been waiting for you for our BDSM session!"
hide rachel08
show rachel09
ra "Uh Uh, I think I'm in BIG trouble!"
show tarapanties01 at midleft with moveinleft
show rachel09 at midright with move
ta "Do you care to explain why you are standing here NAKED in front of this injured patient?"
hide rachel09
show rachel10 at midright
ra "The poor boy needs some stimulation! That way he'll recover more quickly, right?"
hide tarapanties01
show tarapanties02 at midleft
ta "That is the lamest excuse I've heard from you yet. That's it, you need to get punished!"
hide tarapanties02
hide rachel10
show tarapanties03
with dissolve
ra "Prepare to receive your due correction!"
hide tarapanties03
show tarapanties03b
with dissolve
play sound "Sounds/slap.mp3"
ta "Take that, you dirty whore!"
ra "Ouch! She's really giving it to my poor little buttcheek!"
hide tarapanties03b
show tarapanties03
with dissolve
ta "Watch boy, this is the treatment reserved for unfaithful harem girls!"
hide tarapanties03
show tarapanties03c
with dissolve
play sound "Sounds/slap.mp3"
ta "And that, stupid bimbo!"
ra "Ooh, it hurts but I deserve it, I've been so naughty doctor Tara!"
hide tarapanties03c

play music "Sounds/slap.mp3"
pause .25
show nextidle
call screen rachelslap
screen rachelslap:
    add rachelslap at center
    modal True
    button:
        xpos .91
        ypos .44
        xysize(140, 80)  
        action Jump ("RachelSlapEnd")

label RachelSlapEnd:
stop music
hide nextidle
show tarapanties04 with dissolve
ta "Did you see? She felt the PAIN of being an untrustworthy bitch! She suffered for it."
mc "I don't think so. She clearly enjoyed it."
ra "My poor buttcheeks, I'm gonna get a right good pounding in my poopy chute now for sure!"
hide tarapanties04
show tarapanties05
with fastdissolve
ta "That's correct, and since you seem to love BIG cocks, it will be my twelve-inch strap-on dildo this time!"
ra "Oh no! It's sssoo big, it's gonna hurt me a LOT!"
mc "Perhaps you could use MY cock instead? It's even bigger so it will hurt more."
ta "No thanks! Men are NOT ALLOWED where we're going! Now go back to sleep and stop being a nuisance patient [name]!"
mc "Right-ee-o Doc."
jump MedBayNight

label MedBayNight:
$ period = 4
scene medbay02 with dissolve
"You quickly fall asleep after this..."
scene black with dissolve
$ loc == "medbay"
call NewDay
jump Bedroom