label BountyHunter:
play music "Sounds/desertwind01.mp3"
scene bountybackground01 with fade
if alone == False or withnone == False:
    mc "There's someone blocking our way... I'll go and see what she's up to."
if withbe and seenbounty == False:
    be "Be careful, she might be a bounty huntress."
    mc "Pfff, she's just a chick, I ain't scared of her!"
if withpe and seenbounty == False:
    pe "Be careful, she might be a bounty huntress."
    mc "Pfff, she's just a chick, I ain't scared of her!"
if withbe and seenbounty:
    be "It's that bounty huntress again..."
    mc "I'll show her this time who's the HERO here!"
if withpe and seenbounty:
    pe "It's that bounty huntress again..."
    mc "I'll show her this time who's the HERO here!"
if alone and seenbounty:
    mc "Damn, it's that nasty bounty huntress again..."

scene 
show bountybackground02
show bounty01
with dissolve
if persistent.tipson:
    show bountytip at tips with dissolve
    pause
    hide bountytip
if seenbounty == False:
    bh "Finally, we meet..."
    mc "Who are you?"
    hide bounty01
    show bounty02
    with fastdissolve
    bh "I'm the bounty huntress who's going to get the reward that's on YOUR head."
    menu:
        "This is a case of mistaken identity. I am...err... someone else.":
            bh "You look remarkably like the boy I'm hunting. Which is good enough for me!"
            if withbe:
                be "Leave him alone, we are no threat to you!"
                hide bounty02
                show bounty03
                with fastdissolve
                bh "Stay out of this girl, nothing says I have to keep YOU alive!"
                mc "Damn, she's quick...For a left-hander."
                be "May the Phallus Lord strike you down like a billy-club!"
            if withpe:
                pe "Leave him alone, we are no threat to you!"
                hide bounty02
                show bounty03
                with fastdissolve
                bh "Stay out of this girl, nothing says I have to keep YOU alive!"
                mc "Damn, she's quick... For a left-hander."
                pe "You'll pay for this, the Road Warriors never forget!"
                bh "I won't pay jack, I'll be getting a REWARD, remember?"
            hide bounty03
            show bounty02
            with dissolve
            bh "Now, back to you... It's too easy, so I'll give you a chance. Here's a gun loaded with non-lethal bullets, just like my gun."
            bh "I challenge you to a... NON-LETHAL DUEL!"
            mc "Challenge accepted, lady!"
            jump Duel
        "We are heavily armed. Step aside, lady!":
            hide bounty02
            show bounty04
            with fastdissolve
            bh "I don't think so. You don't even have a holster with a gun on you. I could shoot you RIGHT NOW!"
            mc "Err... Let's negotiate. First of all, you can't kill me, because the bounty says \"injured or alive\" and..."
            hide bounty04
            show bounty02
            with fastdissolve
            bh "I KNOW what it says! Which is why, I challenge you to a... DUEL!"
            mc "Ah, ok. but as you said, ain't got no gun so no can't do. We'll just be on our merry w..."
            hide bounty02
            show bounty04
            with fastdissolve
            bh "I've got a spare one, I'll give it to you, loaded with non-lethal bullets, just like my gun. You accept NOW or I'll shoot both your legs off!"
            mc "Ah, what a difficult choice...err... I accept then."
            jump Duel
            
if seenbounty:
    bh "[name]... We meet again."
    mc "Do you ever give up?"
    hide bounty01
    show bounty02
    with fastdissolve
    bh "Nope. You know the drill. I challenge you to a non-lethal DUEL! Here's your tiny gun."
    mc "I only get a small gun cos I have a huge co..."
    bh "Shut up! Get into position!"
    jump Duel
            
label Duel:

$ seenbounty = True
scene duel01
with dissolve
bh "When the ravens start croaking, this is the cue...."
window hide
play music "Sounds/duel.mp3"
show duelmczoom at duelmc:
pause 4
mc "I'm ready."    
window hide
show duelbhzoom at duelbounty:
pause 4
bh "You'd better be..."    
scene duel01 with dissolve
play sound "Sounds/raven.mp3"
$ renpy.pause(1.5, hard=True)
call DiceRoll
window hide
scene duel02 with dissolve
play sound "Sounds/gun.mp3"
$ renpy.pause(1.0, hard=True)
stop sound
if mcfirearms >= 7:
    $ dshootroll=6+diceroll    
if mcfirearms <= 6:
    $ dshootroll=mcfirearms+diceroll
stop music
if ((dshootroll >= 9 and not diceroll == 1) and bounty and knowbounty) or ((dshootroll >= 11 and not diceroll == 1) and melaniabounty and knowmelaniabounty) or diceroll == 6:
    show duel03a
    show duel03b
    with dissolve
    mc "Shit, she got me, right in my stomach. Thanks God she didn't aim lower."
    call MCInjury
    $ mcinjuredgun = True
    bh "Aargh, I can't believe I let myself get shot by this noob!"
    scene duel04 with dissolve
    bh "Well, it's a tie then... I'll let you go. THIS TIME."
    if withbe:
        be "I'm cancelling this scouting mission, we need to get back to the compound to treat your wound!"
    if withpe:
        pe "I'm cancelling this scouting mission, we need to get back to the compound to treat your wound!"
    if alone and withan:
        an "That was exciting to watch! I didn't know who was going to win and now no one did! YIPEEE!"
        mc "I need to get back to the compound Angie, I'm actually INJURED."
        an "Oh..."
    if alone and withay:
        ay "Finally, this BORING duel is over and we can go back home."
    if alone and withru:
        ru "If I didn't have any Road Warrior code, I swear... I'd shoot her right between the eyes!"
        mc "Don't try Ruby and help me back on my bike, I need to go to the medbay..."
    if alone and withcy:
        cy "I'm ve seen the same thing happen in Robot Wars once. The whole server crashed because a tie was not programmed to happen."
        mc "Help me back on my bike please Cyrl, I need to go to the medbay..."
        cy "Humans are such frail creatures."
    if alone and witham:
        am "Well, for once, I'ma actually glad I'm NOT a scout."
        mc "Help me back on my bike please Amy, I need to go to the medbay..."
    if alone and withmo:
        mo "Are you alright, sweetie?"
        mc "Not really, help me back on my bike please, I need to go to the medbay..."
        mo "Of course sweetie, anything for you."
    if alone and withmi:
        mi "Should I finish her off with a ninja high-kick?"
        mc "No, it won't be necessary. Just help me back on my bike, I need to go to the medbay..."        
    if alone and withza:
        za "The West is so wild! We don't shoot each other where I come from, we just chop them up."
        mc "Help me back on my bike please Zara, I need to go to the medbay..."
    if alone and withsu:
        su "The real world is much more dangerous than I thought it would be."
        mc "Help me back on my bike please Suki, I need to go to the medbay..."
    jump ScoutMissionOut01
if (dshootroll <= 8 and not diceroll == 6 and bounty and knowbounty) or (dshootroll <= 10 and not diceroll == 6 and melaniabounty and knowmelaniabounty) or diceroll == 1:
    show duel03a
    with dissolve
    mc "Shit, she got me, right in my stomach. Thanks God she didn't aim lower."
    call MCInjury
    bh "And you missed. So you are MINE."
    if withbe:
        be "I'm sorry [name], there's nothing I can do for you, she's just too quick with that gun and I ain't going to the medbay."
    if withpe:
        pe "I'm sorry [name], there's nothing I can do for you, she's just too quick with that gun and I ain't going to the medbay."
    scene duel04 with dissolve
    if melaniabounty:
        bh "Now I'll tie you up like a hog and take you to the First Lady for my REWARD!"
        jump Maragogo    
    bh "Now I'll tie you up like a hog and take you to General Ivanka for my REWARD!"
    jump IvankaBDSM

label IvankaBDSM:
stop music
$ period += 1
scene bossroom01 blurred
show ivankabdsm01
with fade
iv "Look who's waking up? The TRAITOR who foiled my attack plans!"
mc "Hey, untie me, Ivanka!"
iv "I don't think so. I think you need a good WHIPPING!"
hide ivankabdsm01
show ivankabdsm02
with fastdissolve
iv "With my trusted braided whip!"
play sound "Sounds/whip.wav"
hide ivankabdsm02
show ivankabdsm03
with fastdissolve
mc "Stop it please, it hurts!"
iv "Mmh, it seems useless, because you're already injured and I can't KILL you like I'd love to, since the dev is a SNOWFLAKE!"
hide ivankabdsm03
show ivankabdsm04
with fastdissolve
iv "But maybe this dog leash will change your TRAITOROUS mindset. I borrowed it from the Supreme White House... Now put on the dog collar that daddy makes Mike Ponce wear around the Oval Office!"
scene bossroom02
show ivankabdsm05
with fastdissolve
iv "Now that's better. So, are you a good doggy or a bad doggy?"
menu:
    "A good doggy! Warf, warf!":
        jump GoodDoggy
    "A BAD doggy. GRRRLLL!":
        jump BadDoggy
        
label GoodDoggy:
iv "That's good. But you need to PROVE it to me. So get on your back and lap at my butthole like a GOOD DOGGY then!"
scene bossroom02 blurred
show ivankabdsm20
with fastdissolve
iv "Yeah, stick your tongue right up there, I want it SQUEAKY CLEAN, you hear me?"
play sound "Sounds/sucking.mp3"
iv "Good doggy, you're a natural. I'll allow you to pull your hard monster out and WANK IT FOR ME now..."
hide ivankabdsm20
show ivankabdsm21
with fastdissolve
iv "...While you lick the other side. Mmmh, my little anus is all tingly now... And wet from your saliva."
scene bossroom07
show ivankabdsm22
with dissolve
iv "Oh yeah, you're a nasty little doggy aren't you? Sniffing and slurping up my ass juices... Filthy, FILTHY DOGGY! You deserve a reward.... My FRONT PRIZE."
scene bossroom07
show ivankabdsm23
with dissolve
iv "Let me give you access to my juicy cunt..."
scene bossroom08 blurred
show ivankabdsm24
with dissolve
iv "There you go, twirl that dirty doggy tongue around my engorged pussylips. And wank that cock for me. But NO CUMMING, you hear me doggy?"
mc "But I want to cum so bad, Ivanka!"
iv "Don't call me that! I'm your MISTRESS and you're my LAPDOG, got it?"
mc "But..."
scene bossroom07 blurred
show ivankabdsm25
with dissolve
iv "It seems you don't quite understand what it means to be a REALLY GOOD DOGGY. I'll teach you a new trick then. See that rock-hard MONSTER COCK that's dripping filthy pre-cum?"
hide ivankabdsm25
show ivankabdsm26
with fastdissolve
play sound "Sounds/slap.mp3"
iv "Bad, BAD COCK! No cumming for you, BAD DOGGY!"
mc "Hey, I said I was a \"good doggy\"!"
hide ivankabdsm26
show ivankabdsm27
with fastdissolve
iv "YOU don't get to decide, I GET TO DECIDE, I'm your MISTRESS, remember?"
iv "And I've decided that you are a..."
hide ivankabdsm27
show ivankabdsm28
with fastdissolve
play sound "Sounds/slap.mp3"
iv "...BAD DOGGY!"
mc "Please tell me what can I do to be treated like a good doggy MISTRESS! I'll do anything to be allowed to cum!"
hide ivankabdsm28
show ivankabdsm27
with fastdissolve
iv "Well, for starters, you should embrace the dar... I mean the Trumpf side!"
if mctrumpster == 5:
    mc "But I'm already a Trumpster, Ivanka!!!"
    iv "Are you? Oh, I didn't realize. Then, you can come, GOOD DOGGY!"
    jump GoodDoggyCum
menu:
    "Agree with her (+1 Trumpsters, abandon previous faction)" if mctrumpster == 4:
        call PlusTrumpsterReal
        iv "Now that's better... Your mistress will allow you to CUM then!"
        jump GoodDoggyCum
    "Agree with her (+1 Trumpsters)" if mctrumpster <= 3:
        call PlusTrumpster
        iv "Now that's better... Your mistress will allow you to CUM then!"
        jump GoodDoggyCum
    "Never!":
        hide ivankabdsm27
        show ivankabdsm26
        with fastdissolve
        iv "You're such a stubborn nuisance, [name]! No cumming for you tonight, then!"
        jump IvankaBDSMend
        
label GoodDoggyCum:
hide ivankabdsm27
show ivankabdsm29
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
iv "Empty your cum-laden balls, doggy boy!"
mc "AAAH!"
hide ivankabdsm29
show ivankabdsm30
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
iv "Yeah, shoot some MORE! Your mistress DEMANDS a MASSIVE LOAD OF CUM!"
mc "AAAH!"
scene bossroom04:
    zoom 1.5
    xalign 1.0 yalign 1.0
show ivankabdsm31
with fastdissolve
iv "Mmmh, you did well, you ARE a good doggy after all... And you gave me all that sweet cum... Just for your mistress... Yummy!"
if gooddoggy == False:
    call LustPlusIvanka
$ gooddoggy = True
jump IvankaBDSMend

label BadDoggy:
iv "I KNEW you were a BAD DOGGY! Pull your jockstrap down and bend over that chair with your fat balls hanging between your legs..."
scene bossroom04 blurred
show ivankabdsm06
with fastdissolve
iv "Now prepare to be FLOGGED until you get RED BALLS, bad doggy!"
scene bossroom05
show ivankabdsm07a
with fastdissolve
iv "I'm going to enjoy doing THIS!"
hide ivankabdsm07a
show ivankabdsm07b
with fastdissolve
play sound "Sounds/slap.mp3"
mc "AAAH! My balls!"
hide ivankabdsm07b
show ivankabdsm07a
with fastdissolve
iv "They'll be USELESS once I'm done with them!"
hide ivankabdsm07a
show ivankabdsm07b
with fastdissolve
play sound "Sounds/slap.mp3"
mc "Stop it, I beg you!"
hide ivankabdsm07b
show ivankabdsm07a
with fastdissolve
iv "A bad doggy needs a SEVERE punishment!"
hide ivankabdsm07a
show ivankabdsm07b
with fastdissolve
play sound "Sounds/slap.mp3"
iv "Mmh, now they're all BLOATED and ready for MILKING TIME!"
mc "Wh...what?"
scene bossroom06 blurred
show ivankabdsm08
with dissolve
iv "Just let yourself go, you're nothing but my MILK SLAVE now! Don't resist!"
mc "Oooh, my balls ache so much, I need to empty them!"
iv "That's exactly right! They are sssooo MASSIVE. I'm gonna pump a REALLY HUGE load out of them!"
hide ivankabdsm08
show ivankabdsm09
with dissolve
play sound "Sounds/lick.mp3"
iv "Mmh, I love the musky scent of FAT BALLS ready to UNLOAD!"
scene bossroom04
show ivankabdsm10
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
iv "Let it all go, I want you to FILL UP that jar, you hear me?"
mc "Oh my God, I'm being milked like a cow!"
scene bossroom04 blurred:
    zoom 1.5
    xalign .5 yalign .5
show ivankabdsm11 at centerright
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
iv "Good boy, you've filled it up and you're STILL spewing some more thick shots of young virile semen."
if baddoggy == False:
    call LustPlusIvanka
$ baddoggy = True
mc "I can't.... Keep going... Empty..."
scene bossroom07 blurred:
    zoom 2.0
    xalign .5 yalign .8
show ivankabdsm12
with dissolve
play sound "Sounds/sucking.mp3"
iv "I'll suck the afterdregs out of your cumslit.... *suck*"
jump IvankaBDSMend

label IvankaBDSMend:
$ mcinjured = False
scene bossroom01 blurred
show ivankabdsm01
with dissolve
iv "Now, I'm going to put you to sleep for the night. By injecting you with Lysol and hydroxychloroquine."
mc "What? That sounds dangerous!"
iv "No it's not, Daddy thinks it's safe. And he wants me to check something for him. You're my guinea pig-dog, that's your punishment for being a TRAITOR!"
scene black with dissolve
$ day += 1
$ period = 1
scene bossroom01
show ivankaops01
with fade
iv "So, how are you feeling this morning [name]?"
call MCInjury
$ mcinjuredstomach = True
mc "Terrible! My stomach aches so bad from drinking this godamn Lysol you gave me!"
hide ivankaops01
show ivankaops07
with fastdissolve
iv "Umpf, that's disappointing. But I'm sure you'll recover. Now if you'll excuse me, I want you OUT of MY base. The bounty huntress will take you to the middle of the desert. Good luck finding your way home!"
if lustiv >= 2 or mctrumpster == 5:
    hide ivankaops07
    show ivankaops08
    with fastdissolve
    iv "But since you've been a good boy, I'll... remove the bounty I put on your head. For now. Do come back and visit for some more nasty BDSM sessions, [name]!"
    $ bounty = False
    
$ period += 1
scene bountydump with fade
play music "Sounds/desertwind01.mp3"
bh "I'm just going to dump you like a bag of potatoes right here. Hope you make it back to your secret base, I wouldn't want to miss yet ANOTHER reward on your head!"
if bounty == False:
    mc "I DON'T have a bounty on my head anymore. So there!"
    bh "I'm sure you'll make another mistake some day..."
if bounty:
    mc "Why are all my enemies so mean to me? I don't get it."
scene mesa02 with dissolve
play sound "Sounds/explorepenny02.mp3"
mc "Now I'm on my own. But I think I know where to go, I recognize this place..."
$ period += 1
scene intro07
with fade
mc "Finally, I managed to find the base, just as dusk approaches."
scene intro08
with dissolve
mc "And here comes Bella. I'm saved. Again."
stop music
scene command01
show lena06
show pennyfriendly01 at right
show bella08 at left
with fade
le "Ah, there you are! Thanks goodness you're safe! Even though you seem to be in a pretty bad shape..."
if withbe:
    hide bella08
    show bella01 at left
    with fastdissolve
    be "I searched for you after you were taken away by that horrible bounty huntress, but to no avail..."
    hide bella01
    show bella08 at left
    with fastdissolve  
if withpe:
    hide pennyfriendly01
    show penny03 at right
    with fastdissolve    
    pe "I searched for you after you were taken away by that horrible bounty huntress, but to no avail..."
    hide penny03
    show pennyfriendly01 at right
    with fastdissolve  
mc "She took me back to the Forward Ops base and sold me to General Ivanka. Who proceeded to physically and sexually assault me, as it happens quite often in this game I've noticed."
hide lena06
show lena03
with fastdissolve
le "What a bitch! Now you have a VERY GOOD reason to find Trumpf City and get rid of her father!"
if mctrumpster == 5:
    mc "Well, actually, she made me see the light. I'm a Trumpster now."
    hide lena03
    show lena10
    with fastdissolve
    le "What??? Are you a fucking moron or something???"
    call LustMinusLena
    mc "Err... Does the Lysol she made me drink count for being one?"
    hide lena10
    show lena05
    with fastdissolve
    le "*sigh* Just go to the medbay and get your stomach pumped. We've wasted enough time as it is."
    mc "I'd rather get something else pum..."
    hide lena05
    show lena10
    with fastdissolve
    le "I DON'T WANT TO KNOW! DISMISSED!"
    jump Medbay
if mctrumpster <= 4:
    mc "I sure have! But I still have a bounty on my head at the same time..."
    hide lena03
    show lena05
    with fastdissolve
    le "Just be careful next time. And train with Ruby to handle a gun like a pro so you're prepared if you ever meet a bounty hunter again. You are dismissed!"
    hide lena05 
    hide pennyfriendly01
    hide bella08
    with dissolve
    mc "I think I'd better head to the medbay. I'm not feeling so well, even if my bowels are now as clean as a whistle, thanks to that disinfectant I was forced to drink."
    jump Medbay

label ScoutMissionOut01:
$ period += 1
scene command01
show lena01
with fade
le "So, what do you have to report about whatever hex it is you were supposed to explore?"
if withbe:
    be "We met a nasty bounty huntress who shot [name], Chief! So I decided to cancel the mission and bring him back here to receive medical attention."
if withpe:
    pe "We met a nasty bounty huntress who shot [name], Chief! So I decided to cancel the mission and bring him back here to receive medical attention."
if alone:
    mc "I was shot, but not lethally, by a nasty bounty huntress who tracked me down, Chief..."
    hide lena01
    show lena06
    with fastdissolve
    le "Then go to the medbay [name], you're bleeding all over the place. DISMISSED!"
    jump Medbay    
hide lena01
show lena03
with fastdissolve
le "You did well, we don't want [name] to die, he might still prove himself useful to us. EVENTUALLY."
hide lena03
show lena06
with fastdissolve
le "Now go to the medbay [name], you're bleeding all over the place. SCOUTS DISMISSED!"
jump Medbay

label Maragogo:
if seenmaragogo01:
    jump MaragogoSecond
if seenmaragogo01 == False:
    pass
$ seenmaragogo01 = True
scene maragogo01 with fade
bh "We've finally arrived at our destination. Mar-a-Gogo. Time to meet your new owner and for me to collect my reward..."
scene maragogo02
show melaniaout01
with dissolve
me "Ah, I see you've brought me the rascal who's been disrupting my sexual activities. Well done, Kelly!"
bh "He's just slightly injured Madam First Lady, you'll find you can still... \"use\" him."
hide melaniaout01
show melaniaout02
with fastdissolve
me "I certainly will. After what he's done, he'll have to pay me back IN NATURE. Your bounty reward is on the living room table."
bh "Thanks ma'am. He's all yours now."
hide melaniaout02
show melaniaout03
with fastdissolve
me "After this long trip, you might want to stay around a bit, Kelly? You can pick a bikini from my wardrobe and join us back here for the \"activities\" I have in mind... *wink*"
bh "Why not? Thanks for the invitation, I'll go and change then into something more \"appropriate\"."
hide melaniaout03
show melaniaout04
with fastdissolve
me "And as for you, [name]... Or should I say \"[name] the Intruder\"?"
mc "Just let me go! I've got a Deep State NICKNAME, so I'm like, super-important!"
hide melaniaout04
show melaniaout02
with fastdissolve
me "Uh. Important you say? You don't seem to realize what class I BELONG TO. The Super-Elites, that's the top 0.001\%."
hide melaniaout02
show melaniaout01
with fastdissolve
me "We scoff at the 1\%ers and we really don't care about the 99\% remaining ones. To which YOU belong." 
mc "Pff! I'm just as important as you, I'm the HERO here!"
hide melaniaout01
show melaniaout04
with fastdissolve
me "It seems you need a reality check, boy! You are in MY hands now. I can DISPOSE of you whichever way I see fit. Now get undressed and prepare to receive your punishment."
window hide
show melaniaout04 at left with move
show bountyout01 at right with moveinright
with fastdissolve
bh "I think this outfit will do."
me "Most certainly. What do you think, [name]?"
mc "I don't care what this nasty bitch wears!"
play sound "Sounds/taser.mp3"
scene maragogobackgroundb with hpunch
$ renpy.pause(2.0, hard=True)
mc "OUCH! What was that?"
scene maragogo02
show melaniaout01 at left
show bountyout01 at right
with fastdissolve
me "Oh, sorry, did I forget to mention you've been equipped with an implant which can send electrical impulses into your spine on MY command?"
mc "That's not fair!"
hide melaniaout01
show melaniaout04 at left
with fastdissolve
me "Oh, spare me. This is the way it has been since the dawn of time. The elites control the people, so it has been, and so it will be. Forever and ev..."
mc "NO! THE REVOLUTION IS COM..."
window hide
play sound "Sounds/taser.mp3"
scene maragogobackgroundb with hpunch
$ renpy.pause(2.0, hard=True)
scene maragogo02
show melaniaout01 at left
show bountyout03 at right
with fastdissolve
me "What were you saying?"
bh "That implant you gave me to put on him while he was unconscious sure does the trick, Melania!"
hide bountyout03
show bountyout01 at right
with fastdissolve
bh "I would do what the First Lady tells you, [name]. I've set the implant so that each new zap increases in intensity... Until DEATH!"
mc "Fine, but will you release me after I've done what you want? I've got some quests and missions to finish and this is a total waste of my time!"
hide melaniaout01
show melaniaout03 at left
with fastdissolve
me "Yes, you will be free to go. After I've decided you've satisfied us ENOUGH. And we've coaxed MANY LOADS out of your great big fat donkey-dick."
hide bountyout01
show bountyout02 at right
with fastdissolve
bh "Well, this is getting interesting, isn't it [name]?"
mc "Whatever. Get on with it you perverted sexual predators."
hide melaniaout03
hide bountyout02
show melaniaout04 at left
show bountyout01 at right
with fastdissolve
me "First, wear this outfit which was designed for a horse-hung muscle stud..."

hide screen calendar
hide screen mcstats
scene maragogo03
show mcgogo01
with dissolve
bh "Nice! I didn't realize he was packing THAT MUCH during our long trip here..."
me "Not as big as the boy he took away from me though... Which is why he needs to be SEVERELY punished."
me "But first, take this camera Kelly, I need a new photo for our upcoming Elite Magazine cover..."
scene maragogo03
show mcgogo02
with dissolve
mc "I'll strike a serious top male model pose..."
play sound "Sounds/flash.mp3"
scene maragogo03
show mcgogo02
with flash
me "There, that will do just perfect, I can already imagine our front cover in my mind..."
play sound "Sounds/dream.mp3"
scene maragogo03
show mcgogo02
with flash
show elitecover:
    xalign 0.5 yalign 0.5
    zoom 0.5
    linear 2.0 zoom 1.0
with dissolve
$ renpy.pause(4.0, hard=True)
mc "Am I on it?"
me "No, only my BEAUTIFUL elite top model face and your HUGE bulge. That's your only redeeming feature for the super-elites!"
mc "Damn, there goes my career in modeling. I've been used like a cheap whore and discarded like a soiled kleenex, just like all aspiring models."
me "Not those who married well. Like me."
hide elitecover
hide mcgogo02
show mcgogo03 
with dissolve
me "And now, let's pull out this trouser snake you're hiding down there..."
scene maragogo04
show mcgogo04 
with dissolve
me "Nice and THICK. And fast getting ROCK-HARD!"
scene maragogo04 blurred
show mcgogo05 
with dissolve
me "Bingo! Now let's see how you cope with an EXPERT First Lady handjob, shall we?"
mc "you won't make me come like that, my willpower is STRONGER than you think!"
bh "I think you haven't met a woman with Melania's skills yet. I have seen her in action and I can assure you she'll make you EXPLODE in no time!"
scene maragogo03 blurred
show mcgogo06 
with dissolve
play sound "Sounds/sucking.mp3"
mc "Oh my God, the way she sucks on my balls! AAAH!"
me "And now for the First Lady Hand of SPUNKCOAXING!"
play music "Sounds/wank.mp3"
scene maragogo04 blurred
label MelaniaHandSlow:
hide melaniahandfast
show melaniahandslow
call screen melaniahandslow01
screen melaniahandslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MelaniaHandEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MelaniaHandFast") 

label MelaniaHandFast:
me "Not there yet? Maybe if I go a little bit faster..."
hide melaniahandslow
show melaniahandfast
call screen melaniahandfast01
screen melaniahandfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MelaniaHandEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MelaniaHandSlow") 

label MelaniaHandEnd:
me "Ready to BURST your nut, [name]? I can sense it, your cumslit is expanding..."
hide melaniahandslow
hide melaniahandfast
show melaniahandcum01
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Fuck, can't hold off! RHAAA!"
bh "I told you!"
scene maragogo03
show melaniahandcum02
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "AAAH! Please...STOP... AAAH!"
me "Just let it ALL out, I'm not stopping wanking that huge monsterdong until you give me ALL YOU'VE GOT!"
scene maragogo04 blurred
show melaniahandcum03
with dissolve
mc "You're... draining me.... AAAH!"
me "You need to make up for stealing Magnus from me, so PUMP THAT FAT LOAD ALL OVER THE PLACE!"
scene maragogo04
show melaniahandcum04
with dissolve
stop sound
me "Mmmh, look at the size of those cum puddles! What a waste... Good thing I got my 20 gallons of Special Pizza Sauce delivered on time."
bh "Does his cum taste good Melania?"
me "Oh yeah. Why don't you join me and get a taste yourself Kelly?"
scene maragogo03 blurred
show melaniabounty01
with dissolve
play sound"Sounds/kiss.mp3"
bh "Mmmh, it does taste wonderful. Salty and fruity at the same time."
me "With that little pinch of radioactivity that makes Special Pizza Sauce so \"special\"..."
hide melaniabounty01
show melaniabounty02
with dissolve
bh "Let me feel those big firm breasts... Mhhh. Alpha-radiated to perfection!"
play sound "Sounds/womanmoan.mp3"
me "Oooh. Let us not forget our guest. I see he has another massive hardon that needs draining once again..."
bh "Of course First Lady. Come over here slaveboy! And don't forget we can fry your brains out if you disobey."
hide melaniabounty02
show melaniabounty03
with dissolve
mc "What... What are you going to do to me?"
me "We are going to get AT LEAST a gallon of spunk out of you my dear boy!"
scene maragogo06
show melaniabounty06
with dissolve
bh "You're in for an exhausting day. In the hands of two sex-crazed succubi..."
mc "A gallon??? I don't think I can..."
bh "You want to be zapped? You'll do EXACTLY what we tell you to do! Get on all fours and lick the First Lady's pussy!"
scene maragogo04 
show melaniabounty04
with dissolve
play sound "Sounds/sucking.mp3"
me "Yes, that's it, stick your tongue in there and twist it around my clit... AAAH!"
play sound "Sounds/womanmoan.mp3"
scene maragogo03 blurred
show melaniabounty03
with dissolve
me "Shall we move on to the SEX part Kelly?"
bh "I definitely think it would BE BEST."
me "You hear that [name]? Lie on your back and let us do all the thrusting..."
scene maragogo04b 
show melaniabounty05
with dissolve
me "You like it when I rub my First Lady moist pussy all over your shaft? Does it make you delirious with lust [name]?"
mc "AAH... Y...Yes, Me...OOH...lania!"
me "Then let me RIDE you while you lick Kelly's moist clit. I'm going to take ALL OF YOU INSIDE of me!"

play music "Sounds/womansex02.mp3"
label MaragogoSlow:
hide melaniabounceslow
hide melaniabouncefast
hide bountythreesomefast
scene maragogo04b
show bountythreesomeslow
call screen bountythreesomeslow01
screen bountythreesomeslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MaragogoEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MaragogoFast") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("MaragogoPOVSlow") 
        
label MaragogoPOVSlow:
hide bountythreesomeslow
hide bountythreesomefast
hide melaniabouncefast
scene maragogo06 blurred
show melaniabounceslow
call screen melaniabounceslow01
screen melaniabounceslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MaragogoEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MaragogoPOVFast") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MaragogoSlow") 

label MaragogoPOVFast:
hide bountythreesomeslow
hide bountythreesomefast
hide melaniabounceslow
scene maragogo06 blurred
show melaniabouncefast
me "You didn't think I could take ALL of your donkey-dick inside me did you? Now watch me ride you EVEN FASTER!"
call screen melaniabouncefast01
screen melaniabouncefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MaragogoEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MaragogoPOVSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MaragogoFast") 

label MaragogoFast:
hide bountythreesomeslow
hide melaniabounceslow
hide melaniabouncefast
scene maragogo04b
show bountythreesomefast
me "Oh, this dick is so LONG and FAT, my tits are bouncing all over the place while I'm riding this STUD!"
call screen bountythreesomefast01
screen bountythreesomefast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MaragogoEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MaragogoSlow") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("MaragogoPOVFast") 

label MaragogoEnd:
stop music
scene maragogo06 blurred
show melaniabouncecum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
me "Yes, come in ME!"
bh "Fill the First Lady up with your cream, [name]! And they'd better be A LOT!"
hide melaniabouncecum01
show melaniabouncecum02
play sound "Sounds/splooge01.mp3"
me "Mmmh, that's so FILTHY! You're pumping your seed in my snatch and it's OVERFILLING!"
mc "God, AAAH! I can't STOP CUMMING!"
me "Then PLASTER the rest all over me slave-boy!"
hide melaniabouncecum02
show melaniabouncecum03
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
me "Oh My Bestness, you DO cum A LOT!"
bh "Wow, Melania, he's totally COATED your tits in his spunk and he's STILL GOING STRONG! We've got ourselves a true STALLION CUM-MACHINE here!"
me "I know how to pick my boys Kelly!"
call LustPlusMelania
hide melaniabouncecum03
show melaniabouncecum04
mc "AAAH, You've.... drained me..."
bh "I don't think so. You still have one more hole to fill up with tons of cum. MY ARSE!"
me "I'll just watch. In the corner. Like Jerry Falwell."
bh "In the meantime, come and prep my rosebud and get hard again FAST!"
scene maragogo04b
show bountyfinger01
with dissolve
bh "Mmmh, yeah, that's it, get my pussy wet and let the slime flow into my tiny backdoor... And then ass-fuck me HARD AND DEEP!"

scene maragogo07
show bountypreanal01
with dissolve
bh "I'm ready to take on your MASSIVE ARSE-SPLITTER!"
mc "I'm gonna shove it in so deep, I'll rearrange your colon!"
play music "Sounds/womansex01.mp3"
hide bountypreanal01
label BountyAnaSlow:
hide bountyfast
show bountyslow
call screen bountyanalslow01
screen bountyanalslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BountyAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BountyAnalFast") 

label BountyAnalFast:
bh "Holy FUCK! It's so HUGE and DEEP inside me!"
mc "I'll fuck you faster to really SHOW you!"
hide bountyslow
show bountyfast
call screen bountyanalfast01
screen bountyanalfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BountyAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BountyAnaSlow") 

label BountyAnalEnd:
mc "That's it, I'm gonna CUM!"
hide bountyfast
hide bountyslow
show bountyanalcum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
bh "Oh my God, he's BLASTING right inside my ass! It feels so good!"
me "Just hold on tight, Kelly, I think there's MORE to come!"
hide bountyanalcum01
show bountyanalcum02
with dissolve
mc "Fuck yeah, still spewing my sauce! RHAAAA!"
me "Look at those great big globs of boycum, he really had a GALLON of cum in those fat bull-balls of his!"
scene maragogo07b
show bountyanalcum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
bh "So much... So mcuh come..."
me "Keep launching those cum missiles all over us and I'll REWARD you a the end, [name]!"
scene maragogo04 blurred
show bountyanalcum04
mc "That's it, I've done my repainting job... PHEW!"
bh "There's warm cum spilling out of my backside, I feel so dirty... I LOVE IT!"
scene maragogo07
show bountyanalend
with dissolve
mc "So, can I go now?"
me "Y...Yeah... You did well.... Gave us a GALLON of cum. You may go. But I'm NOT removing that bounty. Just yet..."
bh "Damn, my poor ass... Let me recover a bit and I'll take you back to your compound on my rig..."
mc "Well, hurry up, I don't have all day!"

$ mcinjuredtaser = True
stop music
$ period = 4
scene command01
show lena06
show pennyfriendly01 at right
show bella08 at left
with fade
le "Ah, there you are! Thanks goodness you're safe! What happened?"
mc "I was taken to Mar-a-Gogo where I forced to engage, against my will, in a wild threesome sexual orgy with the First Lady and that bitchy bounty huntress. She's called Kelly by the way."
hide lena06
show lena03
with fastdissolve
le "Never mind her damn name! How did you escape?"
mc "Put it that way. They underestimated me. I performed above their expectations and they released me."
if withbe:
    be "What, you mean your sexual prowess got you out of this predicament?"
    mc "Yep. Precisely."
    call LustPlusBella
    be "I see..."
if withpe:
    pe "What, you mean your sexual prowess got you out of this predicament?"
    mc "Yep. Precisely."
    call LustPlusPenny
    pe "I see..."
le "If you had done what you were supposed to do in the first place, you wouldn't have had a bounty on your head! You've been wasting valuable time with your shenanigans!"
mc "Ah yeah, about that. I still have a bounty on my head apparently. I guess they want some MORE of me, if you catch my drift..."
le "*sigh* Now it's getting very late, so ALL SCOUTS DISMISSED!"
mc "(And since I'm injured, I'll spend the night in the medbay...)"
jump Medbay

label MaragogoSecond:
$ seenmaragogo02 = True
scene maragogo01 with fade
bh "We've finally arrived at Mar-a-Gogo again. And I've equipped you once more with that zapping implant, so be warned..."
scene maragogo02
show melaniaout04
with dissolve
me "Ah, welcome back [name]! My pussy for craving for some MASSIVE cock. And another GALLON of spunk."
mc "I don't know if I've replenished them enough since my la..."
play sound "Sounds/taser.mp3"
scene maragogobackgroundc with hpunch
$ renpy.pause(2.0, hard=True)
mc "OUCH! FUCK, it hurts GODAMMIT!"
scene maragogo02
show melaniaout01
me "It does, doesn't it? So you KNOW that you'd better DELIVER and DELIVER BIG TIME!"
bh "I'll go and get my bikini for the \"activities\" Melania!"
hide melaniaout01
show melaniaout03
with fastdissolve
me "Of course. And I'll get my hands on his MONSTERCOCK while you change yourself. Get into YOUR slave-boy gigolo outfit, [name]!"
hide screen calendar
hide screen mcstats
scene maragogo03
show mcgogo03 
with dissolve
me "Get hard fast for me boy, I'm dying to see that GIANT fuckpole again..."
scene maragogo04
show mcgogo04 
with dissolve
me "Nice and THICK. Just like last time... Mmhhh."
scene maragogo04 blurred
show mcgogo05 
with dissolve
me "I bet II can make you cum EVEN FASTER than last time!"
mc "I'll... resist your expert hands Melania, I swear to God, you won't drain me this time!"
me "We'll see about that..."
scene maragogo03 blurred
show mcgogo06 
with dissolve
play sound "Sounds/sucking.mp3"
mc "Oh my God, the way she sucks on my balls! AAAH!"
me "And now for the First Lady Hand of SPUNKCOAXING!"
play music "Sounds/wank.mp3"
scene maragogo04 blurred
label MelaniaHandSlowb:
hide melaniahandfast
show melaniahandslow
call screen melaniahandslow01b
screen melaniahandslow01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MelaniaHandEndb")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MelaniaHandFastb") 

label MelaniaHandFastb:
me "Not there yet? Maybe if I go a little bit faster..."
hide melaniahandslow
show melaniahandfast
call screen melaniahandfast01b
screen melaniahandfast01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MelaniaHandEndb")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MelaniaHandSlowb") 

label MelaniaHandEndb:
me "Ready to BURST your nut, [name]? I can sense it, your cumslit is expanding..."
hide melaniahandslow
hide melaniahandfast
show melaniahandcum01
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Fuck, can't hold off! RHAAA!"
me "As I suspected, my expert hands are just too much for an amateur like you!"
scene maragogo03
show melaniahandcum02
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "AAAH! Please...STOP... AAAH!"
me "Just let it ALL out, I'm not stopping wanking that huge monsterdong until you give me ALL YOU'VE GOT!"
scene maragogo04 blurred
show melaniahandcum03
with dissolve
mc "You're... draining me.... AAAH!"
me "You need to make up for stealing Magnus from me, so PUMP THAT FAT LOAD ALL OVER THE PLACE!"
scene maragogo04
show melaniahandcum04
with dissolve
stop sound
me "Mmmh, your cum puddles look even BIGGER than last time. Seems like you were actually looking forward to this session, weren't you, you NAUGHTY boy?"
bh "I'm back! I see I missed the first CUM ERUPTION..."
me "You're not too late to get a taste. It's still warm..."
scene maragogo03 blurred
show melaniabounty01
with dissolve
play sound"Sounds/kiss.mp3"
bh "Mmmh, it does taste wonderful. Salty and fruity at the same time."
me "With that little pinch of radioactivity that makes Special Pizza Sauce so \"special\"..."
hide melaniabounty01
show melaniabounty02
with dissolve
bh "Let me feel those big firm breasts... Mhhh. Alpha-radiated to perfection!"
play sound "Sounds/womanmoan.mp3"
me "Oooh. Let us not forget our guest. I see he has another massive hardon that needs draining once again..."
bh "Of course First Lady. Come over here slaveboy! And don't forget we can fry your brains out if you disobey."
hide melaniabounty02
show melaniabounty03
with dissolve
mc "What... What are you going to do to me this time?"
me "Same as last time, pump AT LEAST a gallon of spunk out of you my dear boy!"
scene maragogo06
show melaniabounty06
with dissolve
bh "You're in for an exhausting day. In the hands of two sex-crazed succubi..."
mc "A gallon??? I don't think I can..."
bh "You want to be zapped? You'll do EXACTLY what we tell you to do! Get on all fours and lick the First Lady's pussy!"
scene maragogo04 
show melaniabounty04
with dissolve
play sound "Sounds/sucking.mp3"
me "Yes, that's it, stick your tongue in there and twist it around my clit... AAAH!"
play sound "Sounds/womanmoan.mp3"
scene maragogo03 blurred
show melaniabounty03
with dissolve
me "Shall we move on to the SEX part Kelly?"
bh "I definitely think it would BE BEST."
me "You hear that [name]? Lie on your back and let us do all the thrusting..."
scene maragogo04b
show melaniabounty05
with dissolve
me "You like it when I rub my First Lady moist pussy all over your shaft? Does it make you delirious with lust [name]?"
mc "AAH... Y...Yes, Me...OOH...lania!"
me "Then let me RIDE you while you lick Kelly's moist clit. I'm going to take ALL OF YOU INSIDE of me!"

play music "Sounds/womansex02.mp3"
label MaragogoSlowb:
hide melaniabounceslow
hide melaniabouncefast
hide bountythreesomefast
scene maragogo04b
show bountythreesomeslow
call screen bountythreesomeslow01b
screen bountythreesomeslow01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MaragogoEndb")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MaragogoFastb") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("MaragogoPOVSlowb") 
        
label MaragogoPOVSlowb:
hide bountythreesomeslow
hide bountythreesomefast
hide melaniabouncefast
scene maragogo06 blurred
show melaniabounceslow
call screen melaniabounceslow01b
screen melaniabounceslow01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MaragogoEndb")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MaragogoPOVFastb") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MaragogoSlowb") 

label MaragogoPOVFastb:
hide bountythreesomeslow
hide bountythreesomefast
hide melaniabounceslow
scene maragogo06 blurred
show melaniabouncefast
me "You didn't think I could take ALL of your donkey-dick inside me did you? Now watch me ride you EVEN FASTER!"
call screen melaniabouncefast01b
screen melaniabouncefast01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MaragogoEndb")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MaragogoPOVSlowb") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MaragogoFastb") 

label MaragogoFastb:
hide bountythreesomeslow
hide melaniabounceslow
hide melaniabouncefast
scene maragogo04b
show bountythreesomefast
me "Oh, this dick is so LONG and FAT, my tits are bouncing all over the place while I'm riding this STUD!"
call screen bountythreesomefast01b
screen bountythreesomefast01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MaragogoEndb")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MaragogoSlowb") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("MaragogoPOVFastb") 

label MaragogoEndb:
stop music
scene maragogo06 blurred
show melaniabouncecum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
me "Yes, come in ME!"
bh "Fill the First Lady up with your cream, [name]! And they'd better be A LOT!"
hide melaniabouncecum01
show melaniabouncecum02
play sound "Sounds/splooge01.mp3"
me "Mmmh, that's so FILTHY! You're pumping your seed in my snatch and it's OVERFILLING!"
mc "God, AAAH! I can't STOP CUMMING!"
me "Then PLASTER the rest all over me slave-boy!"
hide melaniabouncecum02
show melaniabouncecum03
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
me "Oh My Bestness, you DO cum A LOT!"
bh "Wow, Melania, he's totally COATED your tits in his spunk and he's STILL GOING STRONG! We've got ourselves a true STALLION CUM-MACHINE here!"
me "I know how to pick my boys Kelly!"
call LustPlusMelania
hide melaniabouncecum03
show melaniabouncecum04
mc "AAAH, You've.... drained me..."
bh "I don't think so. You still have one more hole to fill up with tons of cum. MY ARSE!"
me "I'll just watch. In the corner. Like Jerry Falwell."
bh "In the meantime, come and prep my rosebud and get hard again FAST!"
scene maragogo04b
show bountyfinger01
with dissolve
bh "Mmmh, yeah, that's it, get my pussy wet and let the slime flow into my tiny backdoor... You deserve a reward, bring that cock over to my MOUTH, I'll give you a blowjob first!"
scene maragogo05
show bountyprebj01
with dissolve
play sound "Sounds/sucking.mp3"
bh "Mmmh, so tasty, and those afterdregs still pumping out of your cumslit... DELICIOUS!"
mc "I'm gonna skull-fuck you till you're begging me to stop!"
me "Do your worse, she can handle your giant tool!"
play channel1 "Sounds/boymoan.mp3"
play channel2 "Sounds/hardsucking.mp3"
scene maragogo05 blurred
label BountyBlowSlow:
hide bountybjfast
show bountybjslow
call screen bountyblowslow01
screen bountyblowslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BountyBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BountyBlowFast") 

label BountyBlowFast:
mc "Oh FUCK! She's DEVOURING my knob!"
me "Go on, deepthroat him even FASTER so he blow his load, Kelly!"
hide bountybjslow
show bountybjfast
call screen bountyblowfast01
screen bountyblowfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BountyBlowEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BountyBlowSlow") 

label BountyBlowEnd:
mc "That's it, I'm gonna CUM!"
hide bountybjfast
hide bountybjslow
show bountybjcum01 with fastdissolve
stop channel1
stop channel2
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "FUCK! AAAAH!"
me "Yeah, pump that fat load down her gullet [name], I want to see it dripping down her chin in thick rivulets!"
bh "GGGrlllb!"
mc "I've got some more for you... And your FACE!"
hide bountybjcum01
show bountybjcum02
with dissolve
mc "RHAAAAAAA! Take those shots!"
bh "YES! Cover my face in your THICK LOAD!"
me "Damn boy, you're really pumping a FAT load there!"
hide bountybjcum02
show bountybjcum03
with dissolve
bh "Still ROCKHARD? Then I'm ready for your anal ONSLAUGHT!"
mc "Then lie down on your back and I'll fuck that ass of yours since that's what you want!"
scene maragogo07
show bountypreanal01 
with dissolve
bh "Oh my God, I think I might have spoken too fast..."
mc "I'm gonna shove it in so deep, I'll rearrange your colon!"
play music "Sounds/womansex01.mp3"
hide bountypreanal01
label BountyAnaSlowb:
hide bountyfast
show bountyslow
call screen bountyanalslow01b
screen bountyanalslow01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BountyAnalEndb")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BountyAnalFastb") 

label BountyAnalFastb:
bh "Holy FUCK! It's so HUGE and DEEP inside me!"
mc "I'll fuck you faster to really SHOW you!"
hide bountyslow
show bountyfast
call screen bountyanalfast01b
screen bountyanalfast01b:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BountyAnalEndb")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BountyAnaSlowb") 

label BountyAnalEndb:
mc "That's it, I'm gonna CUM!"
hide bountyfast
hide bountyslow
show bountyanalcum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
bh "Oh my God, he's BLASTING right inside my ass! It feels so good!"
me "Just hold on tight, Kelly, I think there's MORE to come!"
hide bountyanalcum01
show bountyanalcum02
with dissolve
mc "Fuck yeah, still spewing my sauce! RHAAAA!"
me "Look at those great big globs of boycum, he really had a GALLON of cum in those fat bull-balls of his!"
scene maragogo07b
show bountyanalcum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
bh "So much... So mcuh come..."
me "Keep launching those cum missiles all over us and I'll REWARD you a the end, [name]!"
scene maragogo04 blurred
show bountyanalcum04
mc "That's it, I've done my repainting job... PHEW!"
bh "There's warm cum spilling out of my backside, I feel so dirty... I LOVE IT!"
scene maragogo07
show bountyanalend
with dissolve
mc "So, can I go now?"
me "Y...Yeah... You did well.... Gave us another GALLON of cum. You may go. And this time, I'm removing the bounty that's on your head..."
bh "Damn, my poor ass... Let me recover a bit and I'll take you back to your compound on my rig..."
mc "Well, hurry up, I don't have all day!"
show screen calendar
show screen mcstats
$ mcinjuredtaser = True
stop music
$ period = 4
scene command01
show lena06
show pennyfriendly01 at right
show bella08 at left
with fade
le "Ah, there you are! Thanks goodness you're safe! What happened? Let me guess, another sexual orgy that you didn't want to take part in? *sarcasm*"
mc "That's right, Chief Lena. Although THIS time, I gave it to them so good, the First Lady removed the bounty that was on my head."
hide lena06
show lena03
with fastdissolve
le "Oh, finally, you are free to do what you ARE SUPPOSED TO DO, instead of wasting valuable time on nonsense that doesn't advance the storyline."
mc "What storyline?"
le "*sigh* Now it's getting very late, so ALL SCOUTS DISMISSED!"
$ seenmaragogo02 = True
$ melaniabounty = False
mc "(And since I'm injured, I'll spend the night in the medbay...)"
jump Medbay