label DebraGallery:
call screen gallerydebra
screen gallerydebra:
    add "Gallery/debragallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("gallerydebra"), Jump ("MainGallery")]

    if renpy.seen_image("debrapool02"):
        imagebutton:
            focus_mask True
            idle "Gallery/debragallery01.png" xpos 621 ypos 100
            hover "Gallery/debragallery01.png"
            action Jump ("DebraGallery01")

    if renpy.seen_image("debrapool02") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("DebraGallery")

    if renpy.seen_image("science02"):
        imagebutton:
            focus_mask True
            idle "Gallery/lab01gallery.png" xpos 1050 ypos 100
            hover "Gallery/lab01gallery.png"
            action Jump ("DebraGallery02")

    if renpy.seen_image("science02") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("DebraGallery")

    if renpy.seen_image("science21"):
        imagebutton:
            focus_mask True
            idle "Gallery/lab02gallery.png" xpos 1478 ypos 100
            hover "Gallery/lab02gallery.png"
            action Jump ("DebraGallery03")

    if renpy.seen_image("science21") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("DebraGallery")
            
    if renpy.seen_image("debrascience01"):
        imagebutton:
            focus_mask True
            idle "Gallery/debragallery04.png" xpos 621 ypos 400
            hover "Gallery/debragallery04.png"
            action Jump ("DebraGallery04")

    if renpy.seen_image("debrascience01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("DebraGallery")

    if renpy.seen_image("debradate01"):
        imagebutton:
            focus_mask True
            idle "Gallery/debragallery05.png" xpos 1050 ypos 400
            hover "Gallery/debragallery05.png"
            action Jump ("DebraGallery05")

    if renpy.seen_image("debradate01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("DebraGallery")

    if renpy.seen_image("debramcsofa01"):
        imagebutton:
            focus_mask True
            idle "Gallery/debragallery06.png" xpos 1478 ypos 400
            hover "Gallery/debragallery06.png"
            action Jump ("DebraGallery06")

    if renpy.seen_image("debramcsofa01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("DebraGallery")

    if renpy.seen_image("debravibro01"):
        imagebutton:
            focus_mask True
            idle "Gallery/debragallery07.png" xpos 621 ypos 700
            hover "Gallery/debragallery07.png"
            action Jump ("DebraGallery07")

    if renpy.seen_image("debravibro01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("DebraGallery")
 
    if renpy.seen_image("debrabed01"):
        imagebutton:
            focus_mask True
            idle "Gallery/debragallery08.png" xpos 1050 ypos 700
            hover "Gallery/debragallery08.png"
            action Jump ("DebraGallery08")

    if renpy.seen_image("debrabed01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("DebraGallery")

    add "Gallery/galleryfuture.png" xpos 1478 ypos 700

    add "Gallery/gallerygrid02.png"
    add "Gallery/textdebra.png"

label DebraGallery01:
scene pool04
show debrapool03
mc "She's got her back turned to me... Ebough time to ogle her ass before she turns round then..."
scene pool04 blurred
show debrapoolarse
with fastdissolve
mc "Yeah, I'm almost getting a boner right here and there..."
scene pool04
show debrapool02
with dissolve
de "You think you can sneak on me like this? I heard you arriving... What do you want?"
mc "Hey boss, any new crazy expriment planned?"
de "My experiments are NOT crazy! They are essential to the survival of the human race."
de "Only those with a superior intellect can fathom the extent of their importance. Ie: NOT YOU!"
hide debrapool02
show debrapool01
with fastdissolve
de "But to answer your question, I DO have experiments planned and I expect your full voluntary cooperation when the time comes."
mc "Sure thing boss, anything to help your \"superior intellect\". *snickers*"
mc "I would also like to offer this beautiful necklace I found on my adventures..."
hide debrapool01
show debrapool04
with fastdissolve
de "For me? I am not used to people giving me gifts, as a scientist, I usually only accept grant money from Soros. But hand it over, I'll try it on."
scene pool04 blurred
show debrapoolnecklace
with fastdissolve
de "Thank you [name], it is indeed a very nice necklace... Now I will go back to the lab to study its mineral composition."
hide debrapoolnecklace
mc "And I'll go for a swim then."
jump DebraGallery

label DebraGallery02:
scene lab03
show debratalking01
mc "I'm ready to give my body for science!"
hide debratalking01
show debrahappy02
with fastdissolve
de "Excellent! I so happen to have finished setting my new device and I need a healthy young subject."
hide debrahappy02
show debrapointing
with fastdissolve
de "Since Gwen is too weak, that subject will be YOU!"
hide debrapointing
show debratalkingright01
with fastdissolve
de "Come over here Gwen, you will also assist me in this new and exciting endeavor! While you come over, I will magically slide towards my left."
show debratalkingright01 at midright with move
show gwen03 at midleft
mc "I'm having second thoughts... What are you going to do to me exactly? Fire nasty stuff at me?"
hide debratalkingright01
show debratalking02 at midright
with fastdissolve
de "Ah, an inquisitive mind! I like it. But next time, do shut up, you only need to listen and obey."
gw "Welcome to my world [name]..." 
hide debratalking02
show debrapointing at midright
with fastdissolve
de "What I have in mind is a completely revolutionary experiment. No firing anything at you that could injure your body, quite the contrary."
hide gwen03
show gwen02 at midleft
with fastdissolve
gw "Oh, so HE gets to do the exciting stuff and I get to be fired at?"
hide debrapointing
show debratalkingright01 at midright
with fastdissolve
de "Wait for the rest Gwen. I need [name] to be completely NAKED."
hide gwen02
show gwen05b at midleft
mc "I don't NECESSARILY have a problem with that but I'd like to know more about that experiment of yours..."
hide debratalkingright01
show debratalking01 at midright
with fastdissolve
de "Do you want to become even MORE muscular? I have converted an X-ray machine into a powerful alpha-radiations dispenser. You will be my beta-tester. Or alpha-tester if you prefer."
de "If I succeed, I could build an army of invicible Amazon warriors ready to take over the world so I can ru... I mean, so WE can rebuild this great nation in peace."
hide gwen05b
show gwen06 at midleft
with fastdissolve
gw "Who says I want to take part in this treasonous endeavor?"
hide debratalking01
show debratalkingright01 at midright
with fastdissolve
de "You want to finish your PhD? Then do as you're told and stop moaning Gwen!"
hide gwen06
show gwen05b at midleft
with fastdissolve
mc "Well, I'm all in for my part!"
hide debratalkingright01
show debraback01 at midright
with fastdissolve
de "You didn't actually have a choice but never mind. Follow me to the radiation room."
scene science02
show debratalking02 at center
with dissolve
de "Now get those trousers off and stand inside the radiation tube. I will start the machine so it's ready as soon as you are."
scene science03 with dissolve
gw "Actually, I'm glad it was YOU that ended up all naked in there..."
de "Stop ogling his great big dangling manhood and step back Gwen, I don't want a radiation leak onto you."
de "Ready? Activation in 3...2...1...."
scene science04 with dissolve
play music "Sounds/radiation01.mp3"
mc "AAAH! What the fuck is happening? My body, it's... in so  much pain... Stop it please!"
de "Muscle contractions are all perfectly normal and expected, don't worry. I will up the dose now..."
scene science05 with dissolve
stop music
play music "Sounds/radiation02.mp3"
mc "AAARGH! GRRRR!"
gw "Is THAT normal professor?"
de "Hang on, let me try and fix this... Oops, I dialed in the wrong number. Oh well, at least it clearly works."
gw "He keeps growing and growing... And his cock too!"
scene science06 with dissolve
stop music
play sound "Sounds/hulkgrowl01.mp3"
mc "NEED... TO... FUCK..."
gw "You've turned him into a SEX MONSTER! Do something about it!"
de "Err... I've lost control, I think you'd better run for your life Gwen, he seems mighty horny right now and you're the nearest pussy to him!"
scene science07 with dissolve
gw "Hey, let me go you oaf!"
mc "SMELL... PUSSY... AAAARRR!"
de "Stop fighting him, you'll get him even madder, just bite your time while I prepare an antidote."
scene science08 with dissolve
gw "His monstrous hands are fondling my tits, this is so humiliating... Help me, I beg you Debra!"
de "Yes, yes, I'm going as fast as I can, just pretend you enjoy it!"
mc "BOOBIES... BIG BOOBIES...."
de "See? He seems to like your breasts. This will buy us some time."
mc "PUSSY... BIG PUSSY...."
de "Ah. That is definitely not good news for you my dear Gwen..."
gw "Is he going to rape me?"
scene science09 with dissolve
de "I'd say it looks increasingly likely."
gw "He's going to KILL me with that thing!"
de "It certainly is going to re-arrange your insides..."
mc "FUCK... PUSSY..."
scene science10 with dissolve
call screen sciencefuck01x
screen sciencefuck01x:
    add sciencefuck01
    modal True
    button:
        xpos .91
        ypos .44
        xysize(140, 80)        
        action Jump ("ScienceFuck02x")        
label ScienceFuck02x:
scene science12 with dissolve
mc "CUM... INSIDE... PUSSY..."
gw "AAAH, he's forcing his filthy load inside me!"
de "Almost done, filling up the syringe, just hang in there Gwen!"
scene science13 with dissolve
gw "I'm about to burst, ther's so much cum filling me up!"
mc "CUM... MORE... CUM..."
de "Keep him occupied, I'll inject the antidote in his buttcheek!"
scene science14 with dissolve
de "There, gotcha! How are you doing up there Gwen?"
gw "Gggg..."
scene science15 with dissolve
de "Finally, he's out and he'll go back to normal soon. Which is a damn shame."
gw "Aahhh, I'm gonna faint..."
de "...And poor Gwen is going to take some time to recover from this ordeal."
de "I guess I'd better call the medical team to take over from here. And the cleaning ladies too."
jump DebraGallery

label DebraGallery03:
scene lab03
show debratalking01
de "Ah, I'm glad you came, I just needed an extra assistant for an experiment..."
mc "What experiment? I'm all ears..."
hide debratalking01
show debrahappy01
with fastdissolve
de "I like your enthusiasm. I'll take that as a yes and we shall therefore proceed with it today."
gw "Nice one [name]... Now we're stuck with doing some crazy shit that might kill us!"
de "Stop moaning and come along. I will again MAGICALLY slide to the right for your sprite to appear in due course..."
show debrahappy01 at midright with move
show gwen06 at midleft with moveinleft
gw "Damn it..."
hide debrahappy01
show debrapointing at midright
with fastdissolve
de "Now listen up. The only reason the previous experiment failed is that Gwen distracted me at a crucial time point."
hide gwen06
show gwen02 at midleft
with fastdissolve
gw "Oh, I get it, it's all MY fault AGAIN, is it?"
hide debrapointing
show debratalkingright01 at midright
with fastdissolve
de "... And therefore, in order to avoid any hiccups this time, YOU will get in the machine."
hide gwen02
show gwen08b at midleft
with fastdissolve
gw "This is nuts! And I have to get naked too?"
de "We all know you're a stripper by night because you spend all the money I pay you as soon as you get your wasteful hands on it, so what's the big deal?"
mc "I sure as hell ain't going back into that radiation tube, I don't want to hurt anyone."
hide gwen08b
show gwen02 at midleft
with fastdissolve
gw "FINE! I'll go into your damn doomsday machine, and hopefully, I'll end up killing both of you!"
hide debratalkingright01
show debratalking01 at midright
with fastdissolve
de "Now, now, calm down Gwen, don't get your knickers in a twist. Actually, take them off, I need you totally naked. The machine doesn't accept any material other than human flesh."
scene science02 with dissolve
show debratalking02 at center
with fastdissolve
de "Just stand on the side and get ready to use your strength to restrain her if she goes berserk, alright [name]?"
mc "Ah, I see you actually have doubts about the success of this experiment after all..."
de "Certainly NOT! I'm just prepared this time, that's all. Now do as you're told and shut up!"
scene science21 with dissolve
de "So, are you ready to get buffed up Gwen?"
gw "I don't feel good about this..."
mc "I hope her tits will get bigger too professor."
gw "Shut up, pervert! And stop looking at me like you want to rape me. You already did that!"
mc "It wasn't my fault, I was somebody else, I would never hurt you Gwen!"
de "Stop arguing, I need to concentrate. Activating sequence."
de "3... 2... 1... Alpha-radiations level 1 activated."
scene science22 with dissolve
play music "Sounds/radiation01.mp3"
gw "It... hurts a bit..."
de "Everything fine on my side, wait for your muscles to contract and grow..."
scene science23 with dissolve
gw "I'm growing, I can feel it!"
mc "And we can see it..."
de "Activating Level 2..."
scene science24 with dissolve
stop music
play music "Sounds/radiation02.mp3"
gw "I'm... still growing...! But it hurts so much!"
de "The pain will subside, hold it!"
mc "Wow... her tits..."
scene science25 with dissolve
play sound "Sounds/hulkgrowl01.mp3"
gw "AAARGH! GRRRR!"
mc "Pretty much exactly what I said at this stage of the procedure..."
de "Stop distracting me [name]. Damn, why is it doing this again?"
stop music
scene science26 with dissolve
mc "I don't want to alarm you Professor, but she'a actually growing a COCK now. A BIG ONE might I add..."
gw "NEED... TO... FUCK..."
gw "...DEBRA!"
de "Restrain her [name], restrain her quickly!"
scene science27b with dissolve
mc "I will use my MIGHTY STRENGTH to restrain her Professor!"
mc "She's.. too strong for me!"
scene science27c with dissolve
play sound "Sounds/punch.mp3"
gw "FUCK...YOU!"
window hide
gw "WILL...RAPE... DEBRA!"
de "Shit!..."
scene science27 with dissolve
de "Let go of me Gwen!"
play sound "Sounds/hulkgrowl02.mp3"
gw "PUSSY...NEED...TO...FUCK...PUSSY...."
label GwenDebraSexSlowx:
play music "Sounds/debrasex.mp3"
scene gwendebrabackground blurred
show gwendebrasexslow
call screen gwendebrasexslowx
screen gwendebrasexslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenDebraSexEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenDebraSexFastx") 

label GwenDebraSexFastx:
scene gwendebrabackground
show gwendebrasexfast
de "Get the fucking antidote [name], I can't take much more of that pounding!"
mc "I'm looking for it Professor..."
call screen gwendebrasexfastx
screen gwendebrasexfastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenDebraSexEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("GwenDebraSexSlowx")

label GwenDebraSexEndx:
scene science29 with dissolve
de "She's pile-driving her mammoth futa-cock into me!"
mc "Ah, there, I found the antidote Professor!"
de "Inject it quickly, my pussy is turning into a mush!"
stop music
scene science30 with dissolve
play sound "Sounds/hulkgrowl01.mp3"
de "Oh my dear Lord, she's nutting her filthy mutated sperm inside my womb!"
scene science31 with dissolve
mc "Not sure how to do this, so I'll do it in her BUTT..."
de "Hurry!"
scene science32 with fade
show debranude01 at centerleft
de "Finally, she's out! What an ordeal... I'll make her pay for that."
hide debranude01
show debranude02 at centerleft
de "And you... You were rather slow... But I'll forgive you THIS TIME."
mc "You're welcome. Do you need help cleaning up that sperm that's still on you?"
de "NO. I DO NOT. Now get out of my lab, I'll take it from here! And no money for you!"
de "And you'd better get to the medbay, your face looks like a giant potato."
mc "Yeah, well, it still looks better than the inside of your pussy."
hide debranude02
show debranude01 at centerleft
de "*sigh*..."
jump DebraGallery

label DebraGallery04:
scene lab03
show debratalking01
de "Ah, I'm glad you came, you will assist me and make sure everything goes right this time."
mc "Hey! I didn't volunteer for anything yet!"
hide debratalking01
show debrapointing
with fastdissolve
de "Irrelevant, I volunteered you and that's all that matters. Gwen, hop along too, you might prove yourself useful for once!"
window hide
show debrapointing at midright with move
show gwen03 at midleft 
with fastdissolve
de "Now listen up, minions. Since I can't trust you NOT to turn into some degenerate monster inside the alpha-radiation machine, I will be the subject of my own experiment."
hide gwen03
show gwen02 at midleft
with fastdissolve
gw "Finally, some good news! So what do you need us for?"
hide debrapointing
show debratalkingright01 at midright
with fastdissolve
de "Just...in case. [name] will have the antidote at the ready while you will follow my instructions to power up the device."
mc "Where should I inject you with the antidote Professor? The butt or the boobs?"
hide debratalkingright01
show debratalking01 at midright
with fastdissolve
de "Shut up! I will not turn into a brainless zombie since my intellect is far superior to yours. Therefore, I shall be able to orally formulate my orders if need be."
mc "Alright, your call..."
de "Now follow me to the alpha-chamber."
scene debrascience01 with fade
de "Do you have the antidote [name]?"
mc "Yes Debra, I have it firmly in my hand!"
de "Good. Now, Gwen, power to level 1!"
gw "Alright, Professor."
scene debrascience02 with dissolve
play music "Sounds/radiation01.mp3"
de "I feel... Very little. My genetically-superior body probably requires a heavy dose. Power to Level 3, Gwen!"
gw "Err, we're skipping level 2 then?"
de "Obey my instructions and don't ask questions!"
scene debrascience03 with dissolve
stop music
play music "Sounds/radiation02.mp3"
de "AAAAH, my muscles are... contracting... This feels sssooo GOOD!"
mc "Is Debra a known masochist, Gwen?"
gw "I only know she's a SADIST."
de "SHUT...UP... LEVEL 4... NOW!"
scene debrascience04 with dissolve
stop music
play music "Sounds/radiation02.mp3"
de "RHHHOOOOAAARRRR!"
mc "Uh oh, she's growing huge and also growing a dick. Just like you did."
gw "Oh fuck, she's gonna RAPE me! Give her the antidote, [name]! I'm turning this machine off! How do I do that, Professor?"
scene debrascience05 with dissolve
de "NO! AAAAH! I LIKE... IT! UUUUH! BIG DICK!"
mc "Sorry Gwen, but she's the boss."
gw "She's barely comprehensible, can't you see she's turning into a degenerate monster like we did?"
mc "I resent that, I was NOT a degenerate monster. Apart from that raping urge, I was perfectly fine."
scene debrascience06 with dissolve
stop music
gw "Oh thanks God, the machine stopped by itself. Look at her, she's FREAKY MASSIVE! Give her the fucking antidote, [name]!"
play sound "Sounds/moaning.mp3"
de "DICK... RHHHAAA!"
mc "She's not doing anything bad, she's just touching herself. I can sympathize with that. I do that all the time."
de "AAAR...NEED...TO....CUM!"
mc "Good girl. Jack off that monster futa cock and cum."
gw "And please don't rape me!"
de "BOY... CATCH... MY SPERM... NEED... FOR... ANALYSIS! RHOOOOAR!"
gw "I'll get the bucket, make sure she doesn't cum just yet, keep her distracted!"
mc "What... How?"
scene debrascience07 with dissolve
play music "Sounds/wank.mp3"
mc "Err... There once was a shy little girl who turned into a massive muscled futa monster and she was...err... very nice to everyone around her and..."
de "BOY...SHUT...THE...FUCK...UP! RHOAAR! BRING BUCKET OR I KILL YOU!"
mc "Alright, gee, I was just telling a nice story. Gwen? Come quick, please!"
gw "I've got it, here you are, you take care of this nonsense now, it's YOUR responsibility."
scene debrascience08 with dissolve
mc "I'm ready to catch your spermblasts in the bucket, Professor!"
de "RRHOOOOAR! DON'T... FUCKING... MISS... AAAH!"
scene debrawankbackground
show debrawank
with dissolve
window hide
show angiecatch

call screen debracatch01x
screen debracatch01x:
    modal True
    default time_left = 0.6

    add "Science/debrawankbackground.jpg"
    add "Angie/angiecatch.png"
    add "Science/debrawank10.png"
    add "Science/debracumleft01.png"
    if time_left <= 0.4:
        add "Science/debracumleft02.png"
    if time_left <= 0.2:
        add "Science/debracumleft03.png"

    if time_left <= 0:
        timer .01 action Return
    else:
        timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)

hide debrawank
stop music
scene debrawankendgood01 with dissolve
$ renpy.pause(1.0, hard=True)
mc "Yeah, I caught most of that gallon of futa sperm!"
de "AAARRR... GOOD.. BOY..."
scene debrawankendgood02 with dissolve
gw "Looks like she's going back to normal after her giant cum release..."
scene debrawankendgood03 with dissolve
de "*Phew* That was... intense. Well done [name], you caught my genetically-superior female sperm. Give me the bucket, I'll do an analysis straight away."
gw "And what about our payment for carrying through with this crazy idea of yours?"
de "You shouldn't be asking for money when you just witnessed the most important scientific discovery this decade! Shame on you, Gwen..."
gw "Umpf... We got ripped off, once again."
mc "I got a lust point out of it so I'm happy."
de "Now get out of here, I need to get dressed!"
jump DebraGallery

label DebraGallery05:
stop music
play channel1 "v07/datemusic.mp3"
scene canyon01
show debradate01
de "So how is this boring place better than working in a lab exactly?"
mc "Well, for starters, we're NOT working." 
hide debradate01
show debradate02
with fastdissolve
de "A REAL scientist NEVER ceases to work. You are just LAZY."
mc "No, no, no! I'm FOCUSED on the objective of my mission I swear!"
de "Remind me what it is?"
mc "Err... Something to do with Trumpf?"
hide debradate02
show debradate03
with fastdissolve
de "* sigh* Yes, indeed. You have to DEFEAT him. And I fail to see how a date with me here is getting you any closer to that."
mc "I NEED the date to get you into my harem and then, usually, the harem girl has some kind of use for the mission."
hide debradate03
show debradate01
with fastdissolve
de "Is that so? I can already tell you what use I'm going to be. My INVENTIONS will save the WORLD!"
mc "Can we... like, just get going with it please Debra?"
hide debradate01
show debradate03
with fastdissolve
de "Fine. I'll get in the water and pretend this has kind of use. To MY objective."
scene debradate04 with dissolve
de "I'll grant you that the water here is... quite nice."
mc "See? It might trigger your brain into inventing something amazing to save the world or something..."
scene debradate05 with dissolve
de "I'm getting out now. To THINK."
scene debradate06 with dissolve
mc "* Nice... I won't think, I'll just watch and... dream... *"
scene debradate07 with dissolve
de "I was thinking..."
scene debradate08 with dissolve
de "Why don't you come and sit next to me... After all, this is supposed to be a DATE, right?"
mc "Of course, Debra."
scene debradate09 with fastdissolve
de "This what meant to be... I can now picture it more clearly. Some designer glasses that can see through clothes to detect... err... weapons for example..."
mc "What made you think of that?"
scene debradate10 with fastdissolve
de "I think you KNOW, dirty boy..."
mc "So this date was USEFUL after all. Thanks to my... WEAPON."
scene debradate11a with fastdissolve
de "I... guess so... I think I need to get back in the lab. And work on these glasses..."
scene debradate11b with fastdissolve
mc "I don't need glasses like that. My vivid imagination is often enough..."
de "I see..."
mc "No, I SEE!"
stop channel1
scene canyon01
show debradate02
with dissolve
de "Thanks for the date after all [name]. It did help me clear my mind."
hide debradate02
show debradate01
with fastdissolve
de "Even a genius like me needs to unclatter it sometimes!"
jump DebraGallery

label DebraGallery06:
stop music
play music "v07/datemusic.mp3"
scene bedroom02
show debrasuccubus01 at center with moveinright
de "I made it myself! I call it the Sucubbus Outfit."
mc "It's... different."
hide debrasuccubus01
show debrasuccubus02
with fastdissolve
de "Oh, it IS different. Scientifically proven to induce a rush of dopamine in horny tenage boys..."
mc "I see... I can feel that dopamine right NOW..."
hide debrasuccubus02
show debrasuccubus03
with fastdissolve
de "It's almost MESMERIZING, don't you think?"
mc "Yes... Let me a have a closer mesmerized look..."
scene bedroom02 blurred
show debrasuccubus04
with dissolve
mc "Yeah, now I'm totally mesmerized... Fuck yeah..."
scene bedroom02
show debrasuccubus05
with dissolve
de "But look. It comes with a special equipment... *wink*"
mc "What's that?"
de "Let me demonstrate... On your HARD cock!"
scene debramcsofa01 with dissolve
de "See? I place it over your apple-sized helmet... Like so..."
mc "Is is going to hurt?"
de " A little bit... Where's the fun if it doesn't?"
mc "But..."
stop music
play channel1 "Sounds/wank.mp3"
play channel2 "Sounds/boymoan02.mp3"
label DebraHandSlowx:
hide debrahandfast
show debrahandslow
call screen debrahandslow01x
screen debrahandslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraHandEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DebraHandFastx") 

label DebraHandFastx:
de "Your cock seems to like that. A LOT. So let's do it FASTER!"
hide debrahandslow
show debrahandfast
call screen debrahandfast01x
screen debrahandfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraHandEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DebraHandSlowx") 

label DebraHandEndx:
mc "Deb...Debra, I'm gonna cum!"
de "That was the whole point of this experiment, so go ahead [name]!"
stop channel1
stop channel2
scene debramcsofawankcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
de "That's it, AAAAH!"
window hide
with fastflash
de "Oooh, the succubus sucked your mojo right out of your cumslit!"
scene debramcsofawankcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
de "Still more splooge for me and my cock-jerker?"
window hide
with fastflash
mc "Gggg! RHAAAA!"
de "YEAH, let it SHOOT OUT!"
scene debramcsofawankcum03 with dissolve
play sound "Sounds/lick.mp3"
mc "Oh GOD! This thing... Just too much."
de "Nonsense. You cock is still sufficiently hard to indulge in more experimental sex. On the bed."
play sound "Sounds/lick.mp3"
de "Let me... *slurp*  lick that yummy cream first, then I'll get naked and wait for you over there. You'd better not make me wait, STUD!"
jump DebraGallery

label DebraGallery07:
stop music
play music "v07/datemusic.mp3"
scene bedroom02
show debravibro01 at center with moveinright
de "Evrything is in place, as you can see..."
mc "Damn. Doesn't that hurt?"
hide debravibro01
show debravibro02
with fastdissolve
de "A little bit, it's GOOD pain. So take a GOOD look."
mc "Ooh yeah, I will.."
scene bedroom02 blurred
show debravibro03
with dissolve
mc "I will. So how does it work?"
hide debravibro03
show debravibro04
with fastdissolve
de "Here is the controller. You can activate each clamp by number. Number 1 for left nipple, number two for right nipple and number three for clit. You think you can remember?"
mc "Sure prof!"
scene debravibrosofa01 with dissolve
de "I'm ready for pleasurable electrical torture... Activate button 2 [name]!"
scene debravibrosofa02 with dissolve
play sound "Sounds/taser.mp3"
scene debravibrosofa02 with hpunch
de "Ooooh.. That's nice... And now the other nipple please..."
scene debravibrosofa03 with dissolve
play sound "Sounds/taser.mp3"
scene debravibrosofa03 with hpunch
de "AAAH! MORE, KEEP GOING!"
play sound "Sounds/taser.mp3"
scene debravibrosofa03 with hpunch
mc "More?"
de "Puff.. The clit NOW..."
scene debravibrosofa04 with dissolve
play sound "Sounds/taser.mp3"
scene debravibrosofa04 with hpunch
de "Gggg..."
mc "I'll take that as a sign I should keep going... I think I'll press ALL the buttons at once actually..."
scene debravibrosofa05 with dissolve
play sound "Sounds/taser.mp3"
scene debravibrosofa05 with hpunch
de "Oooohhh ---- my ---- GODDDD!"
scene debravibrosofa04 with dissolve
play sound "Sounds/taser.mp3"
scene debravibrosofa04 with hpunch
play sound "Sounds/moaning03.ogg"
de "My clit, it's vibbrrr-ATING!"
scene debravibrosofa06 with dissolve
play sound "Sounds/womanscream.ogg"
de "I'm CU-UUU-MMING!"
mc "Damn, that's a squirting WATERFALL!"
scene debravibrosofa07 with dissolve
mc "Let me help you in cleaning this up..."
de "Mmmh, that's a good boy..."
play sound "Sounds/slurp.mp3"
scene debravibrosofa08 with dissolve
play sound "Sounds/moaning02.mp3"
mc "And now, it's time for the REAL fun to begin. Get those things off and hop on the bed, Debra!"
stop sound
jump DebraGallery

label DebraGallery08:
scene debrabed01
label DebraFuckChoicex:
stop music
menu:
    "Since you're a Succubus, ride me to Valhalla!":
        de "I think you got your mythology mixed up but I'm game!"
        jump DebraRidex
    "Let's do something more traditional. Me fucking you senseless doggy.":
        de "I suppose we could try that. For a change of pace."
        jump DebraSexx 
    "Treat me like a slave. A lab assistant basically.":
        de "Lab assistants have to clean up the mess after an experiment. So get on your knees and get cleaning!"
        jump DebraSlavex
    "Some players are heavily into FMG. But we're far away from the alpha-X-ray machine, so I guess they're screwed." if debramuscles == False:
        scene debraprehuge01 with dissolve
        $ debramusclesx = True
        de "Far from it! I have designed a miniature version of my successful machine..."
        mc "That tiny dildo thing? How is that even scientifically plausible?"
        de "Don't ask questions and just go with the flow [name]..."
        jump DebraHugex
    "Why don't you use that female muscle growth dildo or whatever it is?" if debramusclesx:
        scene debraprehuge01 with dissolve
        de "You want some MUSCLE SEX, hey? I'll give you MUSCLE SEX then!"
        jump DebraHugex
    "I'm done, let's go back to the gallery.":
        jump DebraGallery

label DebraRidex:
scene debrapreride01 with dissolve
de "I'm going to take control of that cock now. Are you ready [name]?"
mc "Sure, you go right ahead..."
scene debrapreride02 with dissolve
de "Let me first engulf that monster cockhead of yours... Do NOT move!"
mc "I am as still as a male sex doll. The one with the giant cock."
scene debraride00 with dissolve
play sound "Sounds/womanscream.ogg"
de "* Puff...* Nice and snug inside me and now..."
play music "Sounds/fucksound.mp3"
label DebraRideSlowx:
scene debrarideslow
with fastdissolve
call screen debrarideslow01x
screen debrarideslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraRideEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DebraRideFastx") 

label DebraRideFastx:
scene debraridefast
with fastdissolve
call screen debraridefast01x
screen debraridefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraRideEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DebraRideSlowx") 

label DebraRideEndx:
mc "I don't think I can hold much longer Debra... Where... Where do you want me to cum?"
de "CUM INSIDE MY SNATCH!"
stop music
scene debraridecum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
de "Oh yeah, I will to estimate the volume of cum you can ejaculate with the cum sensors I have placed at strategic points inside my poontang and uterus..."
window hide
with fastflash
mc "Wh.. What? Oh God, AAAH!"
scene debraridecum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
de "That's it, keep blowing, you're up to 500ml of spunk, I want MORE!"
window hide
with fastflash
mc "OOOOH, AAAH!"
scene bedroom41 blurred
show debraridecum03
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
de "You know how much young virile seed you have ejaculated so far [name]?"
window hide
with fastflash
mc "N...no... AAAH! How much?"
window hide
with fastflash
de "A whopping 800ml!"
scene debraridecum04 with dissolve
play sound "Sounds/panting.mp3"
mc "Phew... Is that good?"
de "It is adequate I would say. But NOT SUFFICIENT!"
scene debraridecum05 with dissolve
mc "Hang on, wh.. what are you doing???"
de "I also have sensors in my ASS! So let's try the other hole, shall we?"
scene debrarideass00 with dissolve
play sound "Sounds/womanscream.ogg"
de "UUURH! It's so BIG! But your cock is already nicely lubricated with your copious juices so I can do it!"
play music "Sounds/debrasex.mp3"
label DebraRideAssSlowx:
scene debrarideassslow
with fastdissolve
call screen debrarideassslow01x
screen debrarideassslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraRideAssEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DebraRideAssFastx") 

label DebraRideAssFastx:
scene debrarideassfast
with fastdissolve
call screen debrarideassfast01x
screen debrarideassfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraRideAssEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DebraRideAssSlowx") 

label DebraRideAssEndx:
de "I can feel your monster rumbling... You must be close to delivering your SECOND MONSTERLOAD then!"
mc "I... AAAH!"
stop music
scene debrarideasscum01 with dissolve
play music "Sounds/splooge01.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "... CUMMING NOW! RHAAA!"
window hide
with fastflash
de "Ooh, it's well on its way to being a BIG ONE AGAIN!"
scene debrarideasscum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "FUCK, YOUR TIGHT ASS IS MILKING ME!"
window hide
with fastflash
de "And your giant cock is STRETCHING ME!"
stop music
scene debrarideasscum03 with dissolve
play sound "Sounds/panting.mp3"
de "Seems like you're out. For now."
mc "How much did I come this time?"
scene bedroom41 blurred
show debraridecum03
with dissolve
de "My sensors indicate a whopping 500ml of warm spunk sloshing in my colon... Are you ready for MORE? Cos I am!"
mc "Sure... Just give me a minute or so to recover..."
stop sound
scene debrabed01 with dissolve
de "A minute has passed. And I'm horny."
jump DebraFuckChoicex
    
label DebraSexx:
scene debrapresuck00 with dissolve
de "Before you stick your giant pud in my tight hole, I want to lick it..."
mc "Be my guest, Professor..."
scene debrapresuck01 with dissolve
play sound "Sounds/lick.mp3"
de "First those balls... * lick* That never fail to deliver HUGE amounts of sweet teenage spunk..."
mc "You're damn right!"
scene debrapresuck02 with dissolve
play sound "Sounds/lick.mp3"
de "...Then that veiny THICK shaft..."
mc "Oh yeah!"
play music "Sounds/lick.mp3"
scene debrapresuck03 with dissolve
de "All the way up its amazing length..."
play music "Sounds/slurp.mp3"
scene debrapresuck02 with dissolve
scene debrapresuck03 with dissolve
scene debrapresuck02 with dissolve
scene debrapresuck03 with dissolve
scene debrapresuck02 with dissolve
stop music
de "Ssooo tasty..."
scene debrapresuck04 with dissolve
play sound "Sounds/lick.mp3"
de "Let me suck on that tip. And..."
play channel1 "Sounds/hardsucking.mp3"
play channel2 "Sounds/boymoan02.mp3"
label DebraSuckSlowx:
scene debrasuckslow
with fastdissolve
call screen debrasuckslow01x
screen debrasuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraSuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DebraSuckFastx") 

label DebraSuckFastx:
scene debrasuckfast
with fastdissolve
call screen debrasuckfast01x
screen debrasuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraSuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DebraSuckSlowx") 

label DebraSuckEndx:
mc "Get down that shaft, swallow it deeper into your throat Debra!"
label DebraSuck02Slowx:
scene debrasuck02slow
with fastdissolve
call screen debrasuck02slow01x
screen debrasuck02slow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraSuck02Endx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DebraSuck02Fastx") 

label DebraSuck02Fastx:
scene debrasuck02fast
with fastdissolve
call screen debrasuck02fast01x
screen debrasuck02fast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraSuck02Endx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DebraSuck02Slowx") 

label DebraSuck02Endx:
stop channel1
stop channel2
mc "Oh fuck, that's it, I'm gonna..."
scene debrasuckcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...CUM! AAAH!"
with fastflash
mc "CUMMING DOWN YOUR GULLET, RHAAA!"
scene debrasuckcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
de "Gllurb!!!!"
with fastflash
mc "Yeah, swallow that load, Debra!"
scene debrasuckcum03 with dissolve
mc "Damn, that was a blowjob and a half. I don't even know where my cock went."
de "* slurp * Straight down my stomach, that's where."
scene debrasuckcum04 with dissolve
de "And now... * slurp *... It's going to go straight into my womb! I want YOU to fuck me DEEP and HARD!"
mc "Alright! That was the option I chose at the end of the day."
scene debrapredoggy01 with dissolve
de "Don't go easy on me, pound that pussy [name], show me what a STUD you are!"
play music "Sounds/womansex01.mp3"    
label DebraSexSlowx:
scene debradoggyslow
with fastdissolve
call screen debradoggyslow01x
screen debradoggyslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraSexEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DebraSexFastx") 

label DebraSexFastx:
scene debradoggyfast
with fastdissolve
call screen debradoggyfast01x
screen debradoggyfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraSexEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DebraSexSlowx") 

label DebraSexEndx:
de "You're gonna cum again [name]? I can feel your BEAST GROWING INSIDE ME!"
mc "That's right, I'm getting real close..."
scene debradoggycum01 with dissolve
play music "Sounds/splooge01.mp3"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Here it COMES!"
de "YES, fill my snatch with your ball-batter!"
scene debradoggycum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Still pumping, RHAAA!"
window hide
with fastflash
de "Oh, this is a DELUGE of cum!"
scene debradoggycum03 with dissolve
play sound "Sounds/womanscream.ogg"
mc "And now, take my load even DEEPER! OOOH!"
window hide
with fastflash
de "You're just using my uterus as a cum dump, AAAH!"
scene debradoggycum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Fuck yeah!"
window hide
with fastflash
scene debradoggycum03 with dissolve
play sound "Sounds/womanscream.ogg"
$ renpy.pause(.5, hard=True)
window hide
with fastflash
scene debradoggycum02 with dissolve
$ renpy.pause(.5, hard=True)
window hide
with fastflash
scene debradoggycum03 with dissolve
play sound "Sounds/womanscream.ogg"
$ renpy.pause(.5, hard=True)
window hide
with fastflash
stop music
mc "That's it, I think, I'm done RHAAA!"
scene debradoggycum04 with dissolve
play sound "Sounds/womanmoan.mp3"
de "My poor pussy just got an in-depth lesson in fluid dynamics... Oooh..."
mc "Those fluids are now leaking out from where I'm standing..."
de "I know... Let me... clear my gaping tunnel and recover a bit..."
mc "Hurry up Debra, I'm STILL HARD!"
scene debrabed01 with dissolve
de "So you are indeed... Which means?..."
jump DebraFuckChoicex

label DebraSlavex:
scene debraslave01 with dissolve
de "That's it, I want you to lick my pussy and make it SHINY!"   
mc "Oh, I will, it looks so yummy."
play music "Sounds/lick.mp3"    
scene debraslave02 with dissolve
$ renpy.pause(0.4, hard='True')
scene debraslave03 with dissolve
de "I'll shake my booty while you twirl your tongue in there."
scene debraslave02 with dissolve
$ renpy.pause(0.4, hard='True')
scene debraslave03 with dissolve
$ renpy.pause(0.4, hard='True')
scene debraslave02 with dissolve
$ renpy.pause(0.4, hard='True')
scene debraslave03 with dissolve
$ renpy.pause(0.4, hard='True')
scene debraslave02 with dissolve
$ renpy.pause(0.3, hard='True')
scene debraslave03 with dissolve
$ renpy.pause(0.3, hard='True')
scene debraslave02 with dissolve
$ renpy.pause(0.3, hard='True')
scene debraslave03 with dissolve
$ renpy.pause(0.3, hard='True')
scene debraslave02 with dissolve
$ renpy.pause(0.3, hard='True')
scene debraslave03 with dissolve
$ renpy.pause(0.3, hard='True')
stop music
play sound "Sounds/womanmoan.mp3"
de "That's nice but... You need better access to my snatch. I really want to feel your tongue slide ALL OVER IT."
de "Now you stay on your knees like a good little underling and I'll lie on my back on the bed."
scene debraslave04 with dissolve
play sound "Sounds/slurp.mp3"
play music "Sounds/moaning.mp3"    
de "Mmh, yeah, that's even better..."
scene debraslave05 with dissolve
de "And now, keep licking while I hold your head in place with my strong thighs..."
play music "Sounds/moaning02.mp3"
play sound "Sounds/lick.mp3"
de "That's a good slave. Oooh..."
scene debraslave06 with dissolve
play music "Sounds/moaning03.ogg"
play sound "Sounds/lick.mp3"
de "Yes, YES! You're getting me there, slave, don't stop! AAAH!"
scene debraslave07 with dissolve
de "This was good... But I want to feel your tongue on my rosebud now. I want to SQUIRT all over your dirty boy's face!"
scene debraslave08 with dissolve
play sound "Sounds/slurp.mp3"
de "Yeah, lap it up, [name], ooh, this tickles, sssooo good!"
scene debraslave09 with dissolve
play music "Sounds/splooge01.mp3"
play sound "Sounds/womanscream.ogg"
de "AAAAH! I'm CUMMING!"
window hide
with fastflash
de "Sssooo much squirting, AAAH!"
scene debraslave10 with dissolve
stop music
play sound "Sounds/panting.mp3"
de "Well, look at you. It's YOUR turn to be covered in MY juices. You're a DIRTY BOY!"
mc "I'll...I'll clean up. Like a good underling."
de "And don't you dare go SOFT on me."
scene debrabed01 with dissolve
de "Now that you're nice and clean, I DEMAND some hot sex from your MASSIVELY-SWOLLEN DONKEY-DICK!"
jump DebraFuckChoicex

label DebraHugex:
scene debraprehuge02 with dissolve
de "All I have to do is stick this device up my poontang. Like so."
scene debraprehuge03 with dissolve
play sound "Sounds/moaning.mp3"
de "As DEEP as it will go... Then press the... *puff*... level 4 button right here..."
play music "Sounds/radiation01.mp3"
mc "You're sure you don't want to go through levels 1 to 3 first?"
de "Who's the scientist here?"
scene debraprehuge04 with dissolve
play sound "Sounds/womanscream.ogg"
mc "I hope you don't grow a cock is all..."
scene debraprehuge04 with hpunch
de "Don't be silly now."
scene debraprehuge05 with dissolve
de "I can feel my... MUSCLES GROWING!"
scene debraprehuge05 with hpunch
mc "Shit, it's actually working. Cray-ay-zy."
scene debraprehuge06 with dissolve
play sound "Sounds/plop.mp3"
stop music
mc "Look at you, Professor Debra, you're MASSIVE!"
window hide
with fastflash
de "AAARGH!"
scene debraprehuge07 with dissolve
de "That's right, and my MASSIVE body demands a MASSIVE FUCK!"
de "You'd better be quick about it, the effects will wear off pretty soon..."
mc "Ok, fast fucking, here we go!"
play music "Sounds/fucksound.mp3"
label DebraHugeSlowx:
scene debrahugeanimslow
call screen debrahugeslow01x
screen debrahugeslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraHugeEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DebraHugeFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("POVDebraHugeSlowx") 

label DebraHugeFastx:
mc "You want it even faster, Debra?"
de "Yes, POUND ME HARDER TOO!"
scene debrahugeanimfast
call screen debrahugefast01x
screen debrahugefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraHugeEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("DebraHugeSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("POVDebraHugeFastx") 

label POVDebraHugeSlowx:
scene debrahugepovanimslow
call screen povdebrahugeslow01x
screen povdebrahugeslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraHugeEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasteridle.png"
        action Jump ("POVDebraHugeFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("DebraHugeSlowx") 

label POVDebraHugeFastx:
mc "And now, even FASTER FUCKING!"
scene debrahugepovanimfast
call screen povdebrahugefast01x
screen povdebrahugefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DebraHugeEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("POVDebraHugeSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("DebraHugeFastx") 

label DebraHugeEndx:
de "Cum before the effects wear off [name]!"
mc "Good thing I'm really close because the player pressed the NEXT button in time..."
stop music
scene debrahugecum01 with dissolve
play music "Sounds/splooge02.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Take that, you muscled huge-titted sizequeen! RHAAA!"
window hide
with fastflash
de "Pound that pussy with your young seed! Just fill it to the brim!"
scene debrahugecum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "That's it, I'm cumming non-stop inside you! AAAH!"
window hide
with fastflash
de "YES! FLOOD MY CUNT!"
scene debrahugecum01 with dissolve
de "MORE, MORE!"
scene debrahugecum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "UUUH, AAAH!"
window hide
with fastflash
de "You've got some more left? For my huge VEINY breasts?"
stop music
scene debrahugecum03 with dissolve
play music "Sounds/moaning02.mp3"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Of course, there you go!"
window hide
with fastflash
de "Damn, that's one HUGE CUMSHOT [name]!"
window hide
with fastflash
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "And another one!"
window hide
with fastflash
mc "And..."
stop music
scene debrahugecum04 with dissolve
mc "...I'm spent now. Not for long of course."
de "Obviously. An alpha-irradiated STALLION like you can keep it up for HOURS. It's basic science really."
scene debrahugecum05 with dissolve
play sound "Sounds/womanmoan.mp3"
mc "Uh oh, look like your monster muscles are shrinking, Debra..."
de "Yes, I can see that. As I predicted. I told you the effects are only temporary."
scene debrahugecum06 with dissolve
de "Let me taste that still warm spunk you've covered me with while my body adjusts back to its normal size..."
mc "Of course, be my guest. This protein shake is free of charge."
scene debrabed01 with dissolve
de "I'm back to normal and totally clean again. Therefore, I am ready for some MORE SEX."
jump DebraFuckChoicex
