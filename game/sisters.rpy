label ExploreHex42:
$ exploredhex42 = True
scene cloister01 with fade
mc "Looks like some kind of old religious building. Probably as old as the twentieth century."
if withcl and claratoldsisters == False:
    $ claratoldsisters = True
    cl "I recognize this cloister. I saw a picture of it during my seminary. It belongs to the Sisters of the Phallus Dei."
    mc "And what is that order?"
    cl "Well... Err, they are... VERY devout."
    mc "Why don't you come with me then, you can introduce me to them and we can clear this hex."
    if sistersseen01 == False:
        cl "I don't know... I am not from the same Order. They might... not be happy to see me. Maybe another time."
        mc "Alright, I'll go alone then. I am a BIG sinner so I really need some... sisterly comforting."
        jump SistersDeiFirst
    if sistersseen01:
        cl "Well.. I suppose... If this can help you in your divine quest."
        jump SistersDeiSecond
if withcl and claratoldsisters:
    if sistersseen01:
        mc "Will you come with me this time Clara?"
        cl "Well.. I suppose... If this can help you in your divine quest."
        jump SistersDeiSecond        
    pass        
if withbe and not withcl:
    be "I hope it's inhabited and that we shall find pennance for our sins beneath its walls!"
    mc "Yeah, maybe... Let me go alone though, I am a BIG sinner so I really need some...whatever you call it."
    be "Alright, I'll pray here for your safe return. But don't take too long."
if withpe and not withcl:
    pe "Looks like it's been abandoned. Road Warriors probably pillaged it long ago."
    mc "Yeah, maybe... I'll go and investigate, you keep marauders away."
    pe "Sure, why not, I mean, I'm just a scout, right? Why should I go and investigate and have all the fun?"
    mc "Well, someone needs to stay behind to keep your rig. Since it's YOUR rig, that would be YOU."
    pe "Pfff."
if alone and not withcl:
    mc "Let's have a look... To clear this hex. Hopefully."
    call AloneStance

if sistersseen01 == False:
    jump SistersDeiFirst
    
if sistersseen01:
    jump SistersDeiSecond

label SistersDeiFirst:
scene cloister02 with dissolve
mc "This place is kind of spooky... But I'm brave, so let's enter..."
play sound "Sounds/doorsqueak.mp3"
scene cloister03
show sistermary01 at left
show sisteranna01 at right
show mothertheresa01
with dissolve
stop sound
mt "Welcome to our cloister young man. We are sisters of the Order of the Phallus Dei. We atone for YOUR sins through our prayers and pain from self-flagellation."
menu:
    "I see. You're totally nuts.":
        hide mothertheresa01
        show mothertheresa02
        with fastdissolve
        mt "How can you not see the divine necessity of our vows?"
        hide sistermary01
        hide sisteranna01
        show sisteranna03 at right
        show sistermary04 at left
        with dissolve
        sa "A non-believer in our cloister! I feel like I'm going to faint and hurt myself even more for HIS sins!"
        mc "Well, don't bother, I'm leaving this place and you can forget about me!"
        call MinusChurch
        hide mothertheresa01
        show mothertheresa02
        with fastdissolve
        mt "One day you shall see the Light my son! Jizz be with you..."
        jump BackHex42
    "So is this some kind of BDSM cult?":
        hide mothertheresa01
        show mothertheresa02
        with fastdissolve
        mt "OUR pain is YOUR salvation my son!"
        hide sistermary01
        show sistermary03 at left
        with dissolve
        sm "Let us demonstrate to you the power of PAIN."
        mc "Err... YOUR pain, right? Not mine?"
        hide sisteranna01
        show sisteranna02 at farright
        with dissolve
        sa "Of course, we are women, we deserve to feel AGONY for our TERRIBLE SINS! You deserve worship and praise as a STUD, so sayeth the Phallus Lord!"
        mc "Well, he certainly sayeth damn right! You go girls!"
        hide mothertheresa02
        show mothertheresa04
        with fastdissolve        
        mt "Follow us to our chapel where our PUNISHMENT will lift you closer to the Holy Spurt!"
        mc "Alright!"
    "And so should you, you sinning whores!" if mcchurch == 5:
        hide sistermary01
        show sistermary03 at left
        with dissolve
        sm "Oh, praise the Phallus Lord, he is a member of the Church! He will help us reach DIVINE PAIN for our terrible sins!"
        mc "You're damn right I will. Let's get this show started then."
        hide mothertheresa01
        show mothertheresa04
        with fastdissolve        
        mt "Follow us to our chapel where our PUNISHMENT will lift you closer to the Holy Spurt!"
        mc "Alright! I've already got something lifting itself closer to the Holy Spurt actually..."

scene cloister04
show mothertheresa02
show sistermary01 at left
show sisteranna01 at right
with fade
$ sistersseen01 = True
mt "Let us pray to the Phallus Lord!"
hide sistermary01
show sistermary03 at left
with fastdissolve
sm "Will you be joining us young man?"
mc "Err... Yeah, sure."
hide mothertheresa02
show mothertheresa01
with fastdissolve        
sa "Then you should get undressed down to your skivvies, as men must be free of the burden of vanity."
mc "Right. Why not."
hide mothertheresa01
show mothertheresa03
with fastdissolve        
mt "Get undressed too, sisters. We must prepare for our flogging ceremony and pain is best served on RAW skin."
window hide
hide sistermary03 with moveoutleft
hide sisteranna01 with moveoutright
hide mothertheresa03 with moveoutright


scene cloister09
show mothertheresanude01 with moveinright
mt "First, let me flog myself for the SINS of mankind! I've been such a bad, naughty girl, I must pay the penalty!"
hide mothertheresanude01
show theresaflogged01
with dissolve
pause 1.0
hide theresaflogged01
show theresaflogged02
with fastdissolve
play sound "Sounds/whip.wav"
mt "YES, this is ssooo GOOD!"
hide theresaflogged02
show theresaflogged01
with fastdissolve
pause 1.0
hide theresaflogged01
show theresaflogged02
with fastdissolve
play sound "Sounds/whip.wav"
mt "I can feel your sins lashing onto my skin, young man! AAAH! MORE, MORE!"
hide theresaflogged02
show theresaflogged03
with fastdissolve
pause 1.0
hide theresaflogged03
show theresaflogged04
with fastdissolve
play sound "Sounds/whip.wav"
mt "Oh, the bruising on my big fat filthy tits is going to be divine!"
hide theresaflogged04
show theresaflogged03
with fastdissolve
pause 1.0
hide theresaflogged03
show theresaflogged04
with fastdissolve
play sound "Sounds/whip.wav"
mt "Aaah, yes!"
mc "Jeeezus, you girls are total whackadoodles."
hide theresaflogged04
show theresaflogged05b
with fastdissolve
mt "You sinful miscreant! You cannot fathom the beatitude we experience during self-flagellation!"
show sistermarynude01 at left with moveinleft
show sisterannanude01 at right with moveinright
with fastdissolve
hide theresaflogged05b
show mothertheresanude01
with dissolve
mt "But this is enough. For me. The sisters have arrived and they are ready to move on to the Superior Punishment. You may join and deliver lashes onto them." 
hide sistermarynude01
show sistermarynude02 at left with fastdissolve
sm "Please let me go first, Mother Theresa! My ass is ready for a good beating!"
hide sisterannanude01
show sisterannanude03 at right with fastdissolve
sa "No, I want to go first, I sinned so much this week, I need a good spanking! I've been such a bad, naughty girl!"
hide mothertheresanude01
show mothertheresanude02
with fastdissolve
mt "Maybe our guest here could administer your well-deserved punishment Sister Mary. While I deal with Sister Anna and her twisted soul."
hide sistermarynude02
show sistermarynude01 at left
with fastdissolve
hide mothertheresanude02
show mothertheresanude02
sm "Oh, joy and beatitude befalls ME!"
hide sisterannanude02
show sisterannanude03 at right
with fastdissolve
sa "Oh, but I wanted to get flogged by HIM! He seems... so strong, I'm sure his lashes are POWERFUL and would inflict TREMENDOUS pain on my butt!"
mt "He will flog you once he is done with Sister Anna. I am dealing with you FIRST."
hide mothertheresanude02
show mothertheresanude03
with fastdissolve
mt "I noticed that a cucumber was missing from the pantry... YOU took it, didn't you, you wretched whore!"
hide sisterannanude03
show sisterannanude04 at right
with fastdissolve
sa "Yes, I did. I am so sinful! I... could not resist the temptation... I need to be PUNISHED!"
mt "Very well, turn round and bend over. In the meantime, go and fetch the flogger Sister Mary..."
sm "Of course, Mother!"
hide sistermarynude01 with moveoutleft
scene cloister10
show sisterannaflogged01
with dissolve
mt "Get ready, I will wash away your sins and, a tiny bit, those of Mankind."
hide sisterannaflogged01
show sisterannaflogged02
with fastdissolve
play sound "Sounds/whip.wav"
sa "AAAH! I am in HEAVENS right now, with the Angels of Pain!"
hide sisterannaflogged02
show sisterannaflogged01
with fastdissolve
pause 1.0
hide sisterannaflogged01
show sisterannaflogged02
with fastdissolve
play sound "Sounds/whip.wav"
mt "Let them take away your sins through your penitence!"
hide sisterannaflogged02
show sisterannaflogged01
with fastdissolve
pause 1.0
hide sisterannaflogged01
show sisterannaflogged02
with fastdissolve
play sound "Sounds/whip.wav"
mc "You're not doing this lightly are you! The poor girl's ass is all bruised!"
scene cloister05
show sisterannaflogged03
with dissolve
sa "Oh, but I fully... *sniff*.... deserve it. I've been so naughty!"
mt "I see that Sister Mary has returned with the flogger... Let's turn our attention to her."
scene cloister09
show sistermaryflog01
show mothertheresanude01 at farright
with dissolve
mt "Now it is your duty to slap her harshly until her sins are washed away."
mc "Alright, give me the paddle then..."
scene cloister06
show sistermaryflog04
with dissolve
sm "Do not hold back, I want to feel PAIN, LOTS OF IT!"
scene cloister08
show sistermaryflog02
with dissolve
mc "Err..."
mt "Go on, slap her dirty sinful ass, young man!"
hide sistermaryflog02
show sistermaryflog03
with fastdissolve
play sound "Sounds/slap.mp3"
sm "Ouch! Please do it HARDER, I KNOW you can!"
hide sistermaryflog03
show sistermaryflog02
with fastdissolve
pause 1.0
hide sistermaryflog02
show sistermaryflog03
with fastdissolve
play sound "Sounds/slap.mp3"
mc "There, is that better?"
sm "Oooh, YES! I like it! I LIKE IT A LOT! AGAIN!"
hide sistermaryflog03
show sistermaryflog02
with fastdissolve
pause 1.0
hide sistermaryflog02
show sistermaryflog03
with fastdissolve
play sound "Sounds/slap.mp3"
mt "Can you see IT?"
hide sistermaryflog03
show sistermaryflog02
with fastdissolve
mc "See what?"
mt "Your sins floating away. Directly out of her butt."
mc "Err... No, I don't see anything coming out of her backside. *nutcase*"
mt "Then use your mighty phallus, you will definitely see IT then!"
mt "What??? You want me to flog her with my cock?"
mt "Yes I do. I REALLY DO."
scene cloister06
show sistermaryflog04
with dissolve
sm "His cock is probably so HUGE, it's going to HURT me sssooo much!"
mc "Alright. It sure is a fine ass to cock-slap... So I'll do it."
scene cloister07
show sistermaryflog07
with dissolve
sm "Is it a BIG, PAINFUL cock, Mother Theresa?"
mt "I'd say so. One that has clearly received the blessing of the Phallus Lord."
sm "Ooh, goody then!"
mc "Shut up already and feel THAT!"
hide sistermaryflog07
show sistermaryflog06
with ultrafastdissolve
hide sistermaryflog06
show sistermaryflog05
with ultrafastdissolve
play sound "Sounds/slap.mp3"
sm "AAAH, his divine MONSTER is battering my asscheeks!"
hide sistermaryflog05
show sistermaryflog06
with ultrafastdissolve
hide sistermaryflog06
show sistermaryflog07
with fastdissolve
hide sistermaryflog07
show sistermaryflog06
with ultrafastdissolve
hide sistermaryflog06
show sistermaryflog05
with ultrafastdissolve
play sound "Sounds/slap.mp3"
hide sistermaryflog05
show sistermaryflog06
with ultrafastdissolve
hide sistermaryflog06
show sistermaryflog07
with fastdissolve
hide sistermaryflog07
show sistermaryflog06
with ultrafastdissolve
hide sistermaryflog06
show sistermaryflog05
with ultrafastdissolve
play sound "Sounds/slap.mp3"
mt "Now, can you see IT?"
hide sistermaryflog05
show sistermaryflog06
with fastdissolve
mc "Nope. Nada."
mt "Then do it again. And again. Until you see our Vision and BELIEVE!"
hide sistermaryflog06
show sistermaryflog07
with fastdissolve
hide sistermaryflog07
show sistermaryflog06
with ultrafastdissolve
hide sistermaryflog06
show sistermaryflog05
with ultrafastdissolve
play sound "Sounds/slap.mp3"
mt "Now, can you see?"
hide sistermaryflog05
show sistermaryflog06
with ultrafastdissolve
hide sistermaryflog06
show sistermaryflog07
with fastdissolve
hide sistermaryflog07
show sistermaryflog06
with ultrafastdissolve
hide sistermaryflog06
show sistermaryflog05
with ultrafastdissolve
play sound "Sounds/slap.mp3"
hide sistermaryflog05
show sistermaryflog06
with ultrafastdissolve
hide sistermaryflog06
show sistermaryflog07
with fastdissolve
hide sistermaryflog07
show sistermaryflog06
with ultrafastdissolve
hide sistermaryflog06
show sistermaryflog05
with ultrafastdissolve
play sound "Sounds/slap.mp3"
sm "More, please, MORE!"
hide sistermaryflog05
show sistermaryflog06
with ultrafastdissolve
hide sistermaryflog06
show sistermaryflog07
with fastdissolve
hide sistermaryflog07
show sistermaryflog06
with ultrafastdissolve
hide sistermaryflog06
show sistermaryflog05
with ultrafastdissolve
play sound "Sounds/slap.mp3"
hide sistermaryflog05
show sistermaryflog06
with ultrafastdissolve
hide sistermaryflog06
show sistermaryflog07
with fastdissolve
hide sistermaryflog07
show sistermaryflog06
with ultrafastdissolve
hide sistermaryflog06
show sistermaryflog05
with ultrafastdissolve
play sound "Sounds/slap.mp3"
hide sistermaryflog05
show sistermaryflog06
with ultrafastdissolve
show gemsparkling at sinaway
play sound "Sounds/desertwind01.mp3"
mc "I think... I see something now..."
stop sound
sa "Then it is MY turn to get cock-slapped! I must pay the penalty!"
mt "Assume the penitant position on the flogger Sister Anna... You will get the only punishment we have in this cloister. A good SPANKING!"
sm "Oooh, a spanking, yes, SPANKING, SPANKING! And after that, oral sex."
mc "Whh... What?"
mt "Don't listen to Sister Mary, she's just a bad, naughty, girl. Just take the flogger in your hand..."
scene cloister08
show sisterannaflog02
with dissolve
mc "And what should I do with that dirty girl?"
mt "She talks to much. Always yapping about. I believe the Phallus Lord wants her to taste a mouthful of your punishing manhood!"
sm "Yes, ORAL SEX after a good SPANKING!"
sa "Err... Isn't that... How is that supposed to be painful exactly?"
mt "It will be when he CHOKES your throat with it!"
scene cloister06
show sisterannaflog03
with dissolve
mc "You heard your superior. Now open your mouth wide and say... Nothing."
hide sisterannaflog03
scene cloister11 blurred
play music "Sounds/hardsucking.mp3"
label AnnaMouthSlow:
hide annamouthfast
show annamouthslow
call screen annamouthslow01
screen annamouthslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AnnaMouthEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AnnaMouthFast") 


label AnnaMouthFast:
hide annamouthslow
show annamouthfast
call screen annamouthfast01
screen annamouthfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AnnaMouthEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AnnaMouthSlow") 

label AnnaMouthEnd:
mc "I'm gonna cum, I'm gonna..."
hide annamouthslow
hide annamouthfast
show sisterannacum01
with dissolve
stop music
mc "...CUM.....AAAHHH!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
hide sisterannacum01
show sisterannacum02
with dissolve
mc "Are you feeling relieved of your sins now, Sister Anna?"
sa "Err... * glurb* I'll definitely NEVER steal a cucumber from the pantry again!"
mt "Your duty is done here, young man. You may leave while I finish admonishing them."
mc "Err... Alright. My pleasure."
jump BackHex42

label SistersDeiSecond:
$ exploredhex42 = True
$ sistersrevisited = True
if withcl:
    scene cloister03
    show mothertheresa02
    show sisteranna01 at farright
    show sistermary01 at left
    with dissolve
    mt "Who is this... SLUT with you?"
    mc "Err, what do you mean, she's a Sister, just like you! That is kinda rude if you ask me."
    mt "She is a Sister of Penitence clearly. Meaning she was a SLUT before in her previous life!"
    cl "It is true. Mother Superior is right... That is my Order... I... I should leave..."
    hide mothertheresa02
    show mothertheresa01
    with fastdissolve
    mt "We will however pray for you Sister. By flogging ourselves silly, as per usual. But only the boy may enter..."
    mc "(whispering) Well, thanks Clara, you were still were helpful in gettting me inside. I'll see you outside again!"
    cl "I am glad I could help... Despite my numerous previous sins..."
    call LustPlusClara
    hide sisteranna01
    show sisteranna02 at farright
    with fastdissolve    
    sa "The Phallus Lord gave us a sign! Hallelu-Jizz!"
    hide sistermary01
    show sistermary03 at left
    with fastdissolve
    sm "Yes, He told us to canonize your mighty phallus and raise it to Saint-Manhood!"
    mc "Alright! Now we're talking!"
    hide mothertheresa01
    show mothertheresa04
    with fastdissolve            
    mt "Follow us to the chapel where we will perform the ritual." 
    jump SisterRitual
if mcchurch == 5:
    scene cloister03
    show mothertheresa01
    show sisteranna01 at farright
    show sistermary01 at left
    with dissolve
    mt "Welcome back [name]! We are so happy to see you!"
    hide sisteranna01
    show sisteranna02 at farright
    with fastdissolve    
    sa "The Phallus Lord gave us a sign! Hallelu-Jizz!"
    hide sistermary01
    show sistermary03 at left
    with fastdissolve
    sm "Yes, He told us to canonize your mighty phallus and raise it to Saint-Manhood!"
    mc "Alright! Now we're talking!"
    hide mothertheresa01
    show mothertheresa04
    with fastdissolve            
    mt "Follow us to the chapel where we will perform the ritual."
if mcchurch <= 4:
    scene cloister03
    show mothertheresa02
    show sisteranna01 at farright
    show sistermary01 at left
    with dissolve
    mt "Why are you back here [name]? Our Holy Cloister cannot tolerate your heretical presence anymore!"
    mt "You MUST confess your sins and come back to us, cleansed by the Holy Spurt and as an upstanding pillar of our Church!"
    mc "Gee, last time you didn't mind whether or not I was a member of the Church, now you do! Make up your mind, ladies!"
    hide sistermary01
    show sistermary02 at left
    with fastdissolve
    sm "I feel like his presence is bringing terrible PAIN onto me! I shall faint my dear sisters, do not help me and let me SUFFER in agony!"
    hide sisteranna01
    show sisteranna03 at farright
    with fastdissolve
    sa "See what you did [name]? Please leave or we will ALL faint and enter the eternal pain of the purgatory of the Womb Demon!"
    mc "Alright, alright! I'm leaving, gee! What a way to treat a HERO!"
    $ sistersent = True
    jump BackHex42
    
label SisterRitual:
$ sistersseen02 = True
scene cloister04
show mothertheresanude04
with dissolve
mt "The girls are getting ready..."
window hide
show sistermarynude01 at left with moveinleft
show sisterannanude01 at right with moveinright
hide mothertheresanude04
show mothertheresanude05
with fastdissolve
mt "Let us pray to the Phallus Lord!"
hide sistermarynude01
show sistermarynude03 at left
with fastdissolve
sm "Get your cock ready for canonization [name]. Lie on the Altar of Saint-Manhood!"
hide sisterannanude01
show sisterannanude05 at right
with fastdissolve
sa "Naked of course."
mc "That went without saying knowing you girls."

scene cloister21
show mchuge01
with dissolve
mt "I will begin the ritual. Oh, Phallus Lord, grant this boy's ENORMOUS breeding bullcock Saint-Manhood!"
sm "In the name of the Father, the Son and the Holy Spurt. Se-men."
play music "Sounds/church.mp3"
hide mchuge01
show mchuge02
with dissolve
play sound "Sounds/thunder.mp3"
show mchuge02 with flash
mc "What the hell, my cock is growing?!?! What's going on?"
hide mchuge02
show mchuge03
with dissolve
mc "Even MORE???"
play sound "Sounds/thunder.mp3"
show mchuge03 with flash
mt "It is normal, young man! We summoned the Mother of Growth for you, to raise your cock to Saint-Manhood!"
sm "And it looks like our prayers have been answered! Praise the Phallus Lord, praise the Mother of Growth!"
sa "For He shall bring the Studs back on Earth to re-fertilize the land of womankind! Hallelu-Jizz!"
stop music
scene cloister25
show mothertheresanude04
show sistermarynude01 at left
show sisterannanude01 at right
show cloister25b
with dissolve
mt "And now, you must fornicate with each and every one of us. To cleanse our sinful wombs."
mc "Err... What do you mean?"
hide cloister25b
hide mothertheresanude04
show mothertheresanude05
show cloister25b
with fastdissolve
mt "I mean, you must IMPREGNATE US with your DIVINE essence! The Holy Spurt is within you, you must RELEASE it!"
hide cloister25b
hide sistermarynude01
show sistermarynude03 at left
show cloister25b
with fastdissolve
sm "Yes, release it into our sinful wombs so we may be cleansed with the Holy Spurts of your MEGA Saint-Manhood!"
hide cloister25b
hide sisterannanude01
show sisterannanude05 at right
show cloister25b
with fastdissolve
sa "It is so MASSIVE that you will surely HURT US in the most excruciatingly way when you IMPALE us on it!"
sm "Oh, I can already see the image of the glorious One-Eye of the Phallus Lord in my mind, as he looks down upon us and rewards us for our painful sacrifice!"
mc "Okay, whatever, but make it go DOWN please, I can't go around carrying this MONSTERLOG between my legs!"
hide cloister25b
hide mothertheresanude05
show mothertheresanude04
with fastdissolve
show cloister25b
mt "Let me be the first to test-drive your Godly Phallus, young man... Lie down on the floor."

scene cloister23
show theresaprefuck00
mt "Gather round sisters and make sure he doesn't pull out until he's blown his load INSIDE MY WOMB!"
sa "Of course, Mother Superior! Oh, this is going to be so wonderfully PAINFUL for you!"
play music "Sounds/barbarasex.mp3"
label TheresaSlow:
hide theresafuckfast
hide theresafuckpovslow
hide theresafuckpovfast
scene cloister23
show theresafuckslow
call screen theresafuckslow01
screen theresafuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TheresaEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TheresaFast") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("TheresaPOVSlow") 

label TheresaPOVSlow:
hide theresafuckslow
hide theresafuckfast
hide theresafuckpovfast
scene cloister22 blurred
show theresafuckpovslow
call screen theresafuckpovslow01
screen theresafuckpovslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TheresaEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TheresaPOVFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("TheresaSlow") 

label TheresaFast:
mt "I need to... *puff* ... ride him FASTER and make him NUT!"
hide theresafuckslow
hide theresafuckpovslow
hide theresafuckpovfast
scene cloister23
show theresafuckfast
call screen theresafuckfast01
screen theresafuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TheresaEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("TheresaSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("TheresaPOVFast") 

label TheresaPOVFast:
hide theresafuckslow
hide theresafuckfast
hide theresafuckpovslow
scene cloister22 blurred
show theresafuckpovfast
call screen theresafuckpovfast01
screen theresafuckpovfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TheresaEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("TheresaPOVSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("TheresaFast") 
            
label TheresaEnd:
mt "IMPREGNATE ME WITH YOUR HOLY SPURT!"
scene cloister22 blurred
show theresafuckcum01
with dissolve
stop music
play music "Sounds/splooge01.mp3"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "CUMMMINGGGG! RHAAA!"
hide theresafuckcum01
show theresafuckcum02
with dissolve
sm "Oh my sweet Phallus Lord, we can HEAR the cum FLOWING inside you"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "There's more!"
stop music
mt "I'm getting BLOATED with his Holy Spurt!"
scene cloister26
show theresafuckcum03
with dissolve
mt "*puff* I.. Can barely move..."
sa "Oh wow, he must have pumped a GALLON of spunk inside your womb, Mother Superior!"
sm "How does it feel, please tell us, we're dying to know!"
mt "You'll know soon enough, Sister Mary. It's YOUR TURN NOW!"

scene cloister27
show maryprefuck01
with dissolve
mc "That's it, lick my balls and get them to churn another MONSTER LOAD for you!"
mt "Not monstrous, simply GODLY AND HOLY!"
sa "I am so ENVIOUS! Getting impregnated by such a SUPERIOR bullcock!"
play music "Sounds/womansex02.mp3"

label MarySlow:
hide maryfuckfast
hide maryfuckpovslow
hide maryfuckpovfast
scene cloister20
show maryfuckslow
call screen maryfuckslow01
screen maryfuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MaryEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MaryFast") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("MaryPOVSlow") 

label MaryPOVSlow:
hide maryfuckslow
hide maryfuckfast
hide maryfuckpovfast
scene cloister08 blurred
show maryfuckpovslow
call screen maryfuckpovslow01
screen maryfuckpovslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MaryEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MaryPOVFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MarySlow") 

label MaryFast:
mt "Fuck her HARDER and FASTER! SHe's been a vile sinful creature!"
sm "Oh yes, I HAVE!"
hide maryfuckslow
hide maryfuckpovslow
hide maryfuckpovfast
scene cloister20
show maryfuckfast
call screen maryfuckfast01
screen maryfuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MaryEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MarySlow") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("MaryPOVFast") 

label MaryPOVFast:
hide maryfuckslow
hide maryfuckfast
hide maryfuckpovslow
scene cloister08 blurred
show maryfuckpovfast
call screen maryfuckpovfast01
screen maryfuckpovfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MaryEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("MaryPOVSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MaryFast") 
            
label MaryEnd:
mt "Let her receive your Holy Load of Jizz!"
mc "Will do, I'm just about to dump it, AAAH, like right NOW!"
scene cloister08 blurred
show maryfuckcum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
play music "Sounds/moaning03.ogg"
mc "CUMMMINGGGG! RHAAA!"
play sound "Sounds/splooge01.mp3"
show maryfuckcum01 with fastflash
sm "AAAH, so much of it! I'm being IMPREGNATED by the Holy Spurt!"
scene cloister20 blurred
show maryfuckcum02
with dissolve
stop music
play sound "Sounds/splooge02.mp3"
sm "The Holy Spurt is... ssoo.... voluminous!"
mc "There's more!"
stop music
show maryfuckcum02 with fastflash
sa "Your womb is swelling with his thick cum Sister Mary! Oh, I so wish it was my uterus at the end of his cum-cannon!"
mt "Your time will come, Sister Anna, be patient. Let this young studboy finish impregnating Sister Mary."
hide maryfuckcum02
show maryfuckcum03
with dissolve
mc "Well, I'm done with this womb, let's move on to the next since my Saint-Manhood DEMANDS more pussy!"
mt "Ooh, so eager! Did you hear that Sister Anna? His Saint-Manhood is now totally ready to impregnate YOU!"
sa "I am so happy that I will be painfully ravished by his monster dong!"
stop music
stop sound
scene cloister28 blurred
show annaprefuck01
with dissolve
mc "Mmmh, I'm wondering which hole to choose..."
mt "As long as you come inside her womb, you are welcome to fuck her in EVERY OF HER SINFUL FUCKHOLES!"
sa "What? He can't possibly fit such a MASSIVE Saint-Manhood inside my poor little rosebud!"
mc "Then I'll fuck your ass first to prove you wrong!"
hide annaprefuck01
show annafuck11
with dissolve
play sound "Sounds/gasp.mp3"
mc "There. You see, it fits."

play music "Sounds/womansex01.mp3"
scene cloister28 blurred
label AnnaSlow:
hide annafuckfast
show annafuckslow
call screen annafuckslow01
screen annafuckslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AnnaFast") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("AnnaPussySlow") 

label AnnaFast:
mt "Fuck her ass HARDER and FASTER! She deserves an ANAL punishment!"
sa "Oh yes, my ass has been so NAUGHTY!"
hide annafuckslow
show annafuckfast
call screen annafuckfast01
screen annafuckfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AnnaSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("AnnaPussyFast") 
            
label AnnaPussySlow:
if pussysaid == False:
    mc "Let's move on to the IMPREGNATION hole!"
    sa "Yes please, let your Saint-Manhood ravish my sinful womb!"
    $ pussysaid = True
hide annafucktopslow
hide annafuckpussyfast
hide annafucktopfast
scene cloister28 blurred
show annafuckpussyslow
call screen annafuckpussyslow01
screen annafuckpussyslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AnnaEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AnnaPussyFast") 
    imagebutton:
        focus_mask True
        idle "Icons/POVview.png"
        hover "Icons/POVview.png"
        action Jump ("AnnaPOVSlow") 

label AnnaPussyFast:
if pussyslowsaid == False and pussysaid:
    mt "That's it, faster now, and build up a HUGE LOAD for her!"
    sm "Sister Anna, be ready for your womb to be FLOODED with cum!"
    $ pussyslowsaid = True
if pussysaid == False:
    mc "Let's move on to the IMPREGNATION hole!"
    sa "Yes please, let your Saint-Manhood ravish my sinful womb!"
    $ pussysaid = True
hide annafuckpussyslow
hide annafucktopslow
hide annafucktopfast
scene cloister28 blurred
show annafuckpussyfast
call screen annafuckpussyfast01
screen annafuckpussyfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AnnaEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AnnaPussySlow") 
    imagebutton:
        focus_mask True
        idle "Icons/POVview.png"
        hover "Icons/POVview.png"
        action Jump ("AnnaPOVFast") 
            
label AnnaPOVSlow:
hide annafuckpussyslow
hide annafuckpussyfast
hide annafucktopfast
scene cloister08 blurred
show annafucktopslow
call screen annafuckpovslow01
screen annafuckpovslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AnnaEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AnnaPOVFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AnnaPussySlow") 

label AnnaPOVFast:
hide annafuckpussyslow
hide annafuckpussyfast
hide annafucktopslow
scene cloister08 blurred
show annafucktopfast
call screen annafuckpovfast01
screen annafuckpovfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AnnaEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("AnnaPOVSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AnnaPussyFast") 
            
label AnnaEnd:
mt "DUMP YOUR LOAD INSIDE HER NOW YOUNG MAN!"
scene cloister28 blurred
show annafuckcum01
with dissolve
stop music
play music "Sounds/splooge02.mp3"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Fuck yeah, I'm cumming! The phallus Lord is making me CCOOOOOMMMMMEEE!"
show annafuckcum01 with fastflash
sa "AAAAAH, and me TOO!"
scene cloister08 blurred
show annafuckcum02
with dissolve
mc "Still PUMPING, RHAAA!"
show annafuckcum02 with fastflash
sm "Pull out, she's going to burst!"
stop music
hide annafuckcum02
show annafuckcum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "My cock won't stop!"
mt "We can see that, you're PLASTERING her face with Holy Jizz!"
sa "Glurb... *swallow*"
hide annafuckcum03
show annafuckcum04
with dissolve
stop sound
mc "Finally... And my cock is getting back to \"normal\" size... Phew!"
mt "This marks the end of your cock canonization. But you have reached \"Saint-Manhood\" for eternity."
window hide
show canonization at posmission
$ renpy.pause(2.0, hard=True)
pause
hide canonization
$ canonized = True
sa "Se-men."
sm "Se-men. Lots of it!"

scene cloister04
show mothertheresanude04
show sistermarynude01 at left
show sisterannanude01 at right
with dissolve
mt "Your cock has now been canonized. Through our pain and suffering."
hide sistermarynude01
show sistermarynude03 at left
with fastdissolve
sm "You have reached Saint-Manhood!"
hide sisterannanude01
show sisterannanude05 at right
with fastdissolve
play sound "Sounds/church.mp3"
sa "Praise the Phallus Lord for this Holy Gift bestowed upon you!"
mc "I sure will, I'll praise him everyday. I need to leave now and spread the Word. About my Saint-Manhood."
hide mothertheresanude04
show mothertheresanude05
with fastdissolve
mt "And we will continue praying for the salvation of your Soul by flagellating ourselves silly."
sa" Oh yes! VERY SILLY!"
sm "VERY VERY silly!"
mc "Yeah... err... Okay."
stop sound

label BackHex42:
scene cloister01 with fade
play music "Sounds/desertwind01.mp3"   
if withbe:
    show bellaout03 with dissolve
    be "So, what happened? Are you now closer to God and the Phallus Lord?"
    if canonized:
        mc "Oh yeah. Definitely. I have reached SAINT-MANHOOD."
        hide bellaout03
        show bellaout09
        with dissolve
        be "What? That's... amazing. So few men reach such an ALPHA-GOD status..."
        call LustPlusBella
        mc "Indeed. I am SPECIAL. Now let's go back to the compound and spread the Word."
        jump BackHex42b
    mc "Oh yeah. Definitely."
    call PlusChurch
    hide bellaout03
    show bellaout01
    with fastdissolve
    be "Good, let's go back to the compound then, it's getting late."
if withpe:
    show pennyout03 with dissolve
    pe "So, was there something inside that pile of ruins?"
    if canonized:
        mc "Oh yeah. Definitely. Enough for me to reach SAINT-MANHOOD."
        pe "Yeah, whatever... Let's go back to the compound."
        jump BackHex42b
    mc "Oh yeah. Definitely. Worth visiting. And RE-visiting I'd say."
    call PlusChurch
    pe "Umpf... Let's go back to the compound then, it's getting late."

label BackHex42b:
stop music
$ period += 1
scene command01
show lena01
with fade
if alone == False:
    le "So, what do you have to report about area E2, scouts?"
if alone:
    le "So, what do you have to report about area E2, [name]?"
if canonized:
    mc "I have now reached Saint-Manhood, Chief!"
    hide lena01
    show lena06
    with fastdissolve
    le "What are you babbling about? More religious gobbledygook?"
    mc "It's TRUE! You should have seen it! It GREW to MAMMOTH proportions. Through the Holy Spurt."
    hide lena06
    show lena10
    with fastdissolve
    le "Did you just fall asleep and had a dream ON THE JOB? You are DISMISSED!"
    hide lena10 with dissolve
    mc "Ah, it looks like spreading the Word is going to be more difficult than I thought... Maybe I should talk to the Priest or Sister Clara about that."
    jump LeaveCommand
if sistersrevisited:
    mc "A waste of time. I blame the dev rather than my inability to properly read a hints guide."
    hide lena01
    show lena05
    with fastdissolve
    le "And I think I blame YOU. DISMISSED!"
    hide lena05 with dissolve
    $ sistersrevisited = False
    jump LeaveCommand
else:
    mc "I came upon a cloister. Full of crazy nuns."
    hide lena01
    show lena06
    with fastdissolve
    le "We have our own problems with the Church inside the compound, so stay away from this place in the future..."
    mc "Sure thing, Chief!"
    le "You are dismissed, [name]."
    hide lena06 with dissolve
    jump LeaveCommand
    

