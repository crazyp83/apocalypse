label BarbaraFuck01:
hide screen calendar
hide screen mcstats
if pregba and pregbastart >= 3:
    scene bedroom01
    show barbarapregnant02a
    with fade
    ba "Hi [name]! I am so proud of you and how you so perfectly knocked me up with a genetically superior ALL-AMERICAN baby!"
    mc "Yeah, cool. How about some ALL-AMERICAN hot sex tonight to celebrate teach?"
    hide barbarapregnant02a
    show barbarapregnant02b
    with fastdissolve
    ba "What? No! We can't endanger future generations of American Patriots by hurting them with your massive slab of meat!"
    hide barbarapregnant02a
    show barbarapregnant01b
    with fastdissolve
    ba "They might end up becoming degenerates or mentally retarded like liberals, I cannot allow it!"
    mc "Right, right. I see."
    hide barbarapregnant01b
    show barbarapregnant02a
    with fastdissolve
    ba "So wait for me to give birth to this wonderful future Trumpster baby before even THINKING of sticking your giant pud inside me again..."
    hide barbarapreggo02 with dissolve
    $ weekfuckedbarbara = True    
    jump Bedroom    
scene bedroom01
show barbara01
with fade
menu:
    "Run scene":
        pass
    "Skip scene":
        $ alienfuck = True
        $ weekfuckedbarbara = True
        jump BarbaraEnd
ba "Good evening [name], do you need help with your school homework?"
mc "No, that's done. But I have some nightwork to do still. WITH YOUR BODY!"
window hide
hide barbara01
show barbara08
with fastdissolve
ba "I thought you might, you naughty boy... Let me get my nightwork outfit for you then...Be right back!"
hide barbara08 with moveoutright
        
label BarbaraLingerie:
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
call screen barbarawig
screen barbarawig:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraWiggleEnd")

label BarbaraWiggleEnd:
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
    window hide
    show mctrumpsternickname at posmission
    play sound "Sounds/skill.mp3"
    $ renpy.pause(2.0, hard=True)
    $ trumpsternickname = True
    mc "Alright! I have a nickname now! Woo-ooh!"
    hide mctrumpsternickname
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
label BarbaraSuckSlow:
hide barbarasuckfast
show barbarasuckslow
call screen barbarasuckslow01
screen barbarasuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraSuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BarbaraSuckFast") 

label BarbaraSuckFast:
mc "Come on teach, do it faster and make me BLOW MY NUT!"
hide barbarasuckslow
show barbarasuckfast
call screen barbarasuckfast01
screen barbarasuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraSuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BarbaraSuckSlow") 

label BarbaraSuckEnd:
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

label BarbaraFuckChoice:
$ alienfuck = True
$ weekfuckedbarbara = True
stop music
scene barbarabed with dissolve
ba "I'm ready [name]. Ready for YOU and your MONSTERCOCK!"
label BarbaraFuckChoiceDialogue:
menu:
    "As my teacher, your job is to give me a hand. job.":
        ba "Oh, my poor student needs some relief? Just sit on the edge of the bed and I'll take care of that giant teenage boner!"
        jump BarbaraHandjob
    "What's your position on sexual harassment, teach?":
        ba "Well, I... err..."
        mc "On your back, that's what it is! Prepare your pussy for some deep harassment, Barbara!"
        ba "Oh my, that is definitely NOT in De Vos's education guide, but why not..."
        jump BarbaraMissionary
    "One good teaching method is to pummel something over and over until it sticks.":
        ba "Yes, where are you going with that?"
        mc "Your ass needs a lesson, that's where I'm going!"
        ba "So are you going to pummel it over and over again???"
        mc "You learn fast, teach!"
        jump BarbaraAnal
    "How about some tender illicit-yet-totally-authorized-by-Patreon teacher-student love?":
        ba "Of course [name], give me a nice sensual massage then, I like those!"
        mc "Ah okay, I was thinking more along the lin..."
        ba "...of giving your teacher a nice massage if you want to get an A on your next test, right?"
        mc "Err, yeah, right."
        jump BarbaraMassage
    "You taught us how to make babies during class. Now let's practice what I learnt!" if pregbaready >= 3 and impregnatedsomeone == False and babybarbara == False:
        $ impregnatedsomeone = True
        ba "Make sure you dump a big load in me then [name], I want this to be a success on the first go!"
        mc "And let's go to the sofa for a change for that scene."
        jump BarbaraImpregnation
    "I'm done, let's go to sleep.":
        jump BarbaraEnd

label BarbaraHandjob:
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
label BarbaraHandSlow:
hide barbarahjfast
show barbarahjslow
call screen barbarahandslow01
screen barbarahandslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraHandEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BarbaraHandFast") 

label BarbaraHandFast:
ba "This is really a nice workout for my right arm... Because this cock is so MASSIVE!"
mc "Oh God, that GRIP on my cock!"
hide barbarahjslow
show barbarahjfast
call screen barbarahandfast01
screen barbarahandfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraHandEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BarbaraHandSlow") 

label BarbaraHandEnd:
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
label BarbaraHand02Slow:
hide barbara02hjfast
show barbara02hjslow
call screen barbara02handslow01
screen barbara02handslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraHand02End")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BarbaraHand02Fast") 

label BarbaraHand02Fast:
ba "Does it feel good [name]? Having your teacher wank your fat shaft like that with both hands, mmmh?"
mc "Damn, you're a real PRO Barbara! I can tell you've wanked many young cocks before..."
ba "Mmmh, that's because I'm such a NAUGHTY teacher!"
hide barbara02hjslow
show barbara02hjfast
call screen barbara02handfast01
screen barbara02handfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraHand02End")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BarbaraHand02Slow") 

label BarbaraHand02End:
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
jump BarbaraFuckChoice
    
label BarbaraMissionary:
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
label BarbaraMissionarySlow:
scene bedroom18 blurred
show barbaramissionaryslow
call screen barbarapoundslow01
screen barbarapoundslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraMissionaryEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BarbaraMissionaryFast") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("BarbaraCockSlow") 

label BarbaraCockSlow:
scene bedroom14 blurred
show barbaramissionarypovslow
call screen barbaracockslow01
screen barbaracockslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraMissionaryEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BarbaraCockFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("BarbaraMissionarySlow") 

label BarbaraMissionaryFast:
if barbaratoldfuck == False:
    ba "You're fucking your teacher so good [name].... AAAH, UUUH!"
    $ barbaratoldfuck = True
scene bedroom18 blurred
show barbaramissionaryfast
call screen barbarapoundfast01
screen barbarapoundfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraMissionaryEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BarbaraMissionarySlow") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("BarbaraCockFast") 

label BarbaraCockFast:
if barbaratoldfuck == False:
    ba "You're fucking your teacher so good [name].... AAAH, UUUH!"
    $ barbaratoldfuck = True
scene bedroom14 blurred
show barbaramissionarypovfast
call screen barbaracockfast01
screen barbaracockfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraMissionaryEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("BarbaraCockSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("BarbaraMissionaryFast") 
            
label BarbaraMissionaryEnd:
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
label BarbaraFuckSlow:
hide barbarafuckfast
show barbarafuckslow
call screen barbarafuckslow01
screen barbarafuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BarbaraFuckFast") 

label BarbaraFuckFast:
ba "AAAh, you're a BEAST, [name]! I want you to FUCK ME FASTER AND DOUSE ME WITH ANOTHER MIGHTY LOAD!"
hide barbarafuckslow
show barbarafuckfast
call screen barbarafuckfast01
screen barbarafuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraFuckEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BarbaraFuckSlow") 

label BarbaraFuckEnd:
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
jump BarbaraFuckChoice
    
label BarbaraAnal:
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
label BarbaraAnalSlow:
scene bedroom18 blurred
show barbaraanalslow
call screen barbaraanalslow01
screen barbaraanalslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BarbaraAnalFast") 
    imagebutton:
        focus_mask True
        idle "v08/bottomview.png"
        hover "v08/bottomview.png"
        action Jump ("BarbaraAssSlow") 

label BarbaraAssSlow:
scene bedroom48 blurred
show barbaraassslow
call screen barbaraassslow01
screen barbaraassslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BarbaraAssFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("BarbaraAnalSlow") 

label BarbaraAnalFast:
scene bedroom18 blurred
show barbaraanalfast
call screen barbaraanalfast01
screen barbaraanalfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BarbaraAnalSlow") 
    imagebutton:
        focus_mask True
        idle "v08/bottomview.png"
        hover "v08/bottomview.png"
        action Jump ("BarbaraAssFast") 

label BarbaraAssFast:
scene bedroom48 blurred
show barbaraassfast
call screen barbaraassfast01
screen barbaraassfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("BarbaraAssSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("BarbaraAnalFast") 
            
label BarbaraAnalEnd:
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
    
label BarbaraMassage:
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
jump BarbaraFuckChoiceDialogue

label BarbaraImpregnation:
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
call screen barbaradildo01
screen barbaradildo01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraDildoNext")

label BarbaraDildoNext:
hide barbaradildoslow
show barbaradildofast
with fastdissolve
stop music
play music "Sounds/stripmusic.mp3"
call screen barbaradildo02
screen barbaradildo02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraDildoEnd")

label BarbaraDildoEnd:
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
label BarbaraPregnantSlow:
hide barbaraimpregpovfast
hide barbaraimpregpovslow
show barbaraimpregslow
call screen barbarapregnantslow01
screen barbarapregnantslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraPregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BarbaraPregnantFast") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("BarbaraImpregnateSlow") 

label BarbaraImpregnateSlow:
scene bedroom08 blurred
show barbaraimpregpovslow
call screen barbarapregnantsceneslow01
screen barbarapregnantsceneslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraPregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BarbaraImpregnateFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("BarbaraPregnantSlow") 

label BarbaraPregnantFast:
hide barbaraimpregpovfast
hide barbaraimpregpovslow
show barbaraimpregfast
call screen barbarapregnantfast01
screen barbarapregnantfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraPregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BarbaraPregnantSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("BarbaraImpregnateFast") 

label BarbaraImpregnateFast:
scene bedroom08 blurred
show barbaraimpregpovfast
call screen barbarapregnantscenefast01
screen barbarapregnantscenefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BarbaraPregnantEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("BarbaraImpregnateSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("BarbaraPregnantFast") 
            
label BarbaraPregnantEnd:
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
$ pregba = True
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
call LustPlusBarbara
mc "My pleasure. I'm drained though, so it's time to go to bed."

label BarbaraEnd:
show screen calendar
show screen mcstats
scene barbarasleep with fade
$ loc = "bedroom"
play sound "Sounds/snoring.mp3"
pause 3
call NewDay
jump Bedroom