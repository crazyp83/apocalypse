label GwenGallery:
call screen gallerygwen
screen gallerygwen:
    add "Gallery/gwengallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("gallerygwen"), Jump ("MainGallery")]

    if renpy.seen_image("gwenpool01"):
        imagebutton:
            focus_mask True
            idle "Gallery/gwengallery01.png" xpos 621 ypos 100
            hover "Gallery/gwengallery01.png"
            action Jump ("GwenGallery01")

    if renpy.seen_image("gwenpool01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("GwenGallery")

    if renpy.seen_image("science02"):
        imagebutton:
            focus_mask True
            idle "Gallery/lab01gallery.png" xpos 1050 ypos 100
            hover "Gallery/lab01gallery.png"
            action Jump ("GwenGallery02")

    if renpy.seen_image("science02") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("GwenGallery")

    if renpy.seen_image("science21"):
        imagebutton:
            focus_mask True
            idle "Gallery/lab02gallery.png" xpos 1478 ypos 100
            hover "Gallery/lab02gallery.png"
            action Jump ("GwenGallery03")

    if renpy.seen_image("science21") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("GwenGallery")

    if renpy.seen_image("gwenstrip01"):
        imagebutton:
            focus_mask True
            idle "Gallery/gwengallery04.png" xpos 621 ypos 400
            hover "Gallery/gwengallery04.png"
            action Jump ("GwenGallery04")

    if renpy.seen_image("gwenstrip01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("GwenGallery")

    if renpy.seen_image("amygwenstrip01"):
        imagebutton:
            focus_mask True
            idle "Gallery/amygallery05.png" xpos 1050 ypos 400
            hover "Gallery/amygallery05.png"
            action Jump ("GwenGallery05")

    if renpy.seen_image("amygwenstrip01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("GwenGallery")

    if renpy.seen_image("gwenhandjobcum01 "):
        imagebutton:
            focus_mask True
            idle "Gallery/gwengallery06.png" xpos 1478 ypos 400
            hover "Gallery/gwengallery06.png"
            action Jump ("GwenGallery06")

    if renpy.seen_image("gwenhandjobcum01 ") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("GwenGallery")

    if renpy.seen_image("gwendate05"):
        imagebutton:
            focus_mask True
            idle "Gallery/gwengallery07.png" xpos 621 ypos 700
            hover "Gallery/gwengallery07.png"
            action Jump ("GwenGallery07")

    if renpy.seen_image("gwendate05") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("GwenGallery")

    if renpy.seen_image("gwenmcsleep"):
        imagebutton:
            focus_mask True
            idle "Gallery/gwengallery08.png" xpos 1050 ypos 700
            hover "Gallery/gwengallery08.png"
            action Jump ("GwenGallery08")

    if renpy.seen_image("gwenmcsleep") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("GwenGallery")

    if renpy.seen_image("amygwenlingerie01"):
        imagebutton:
            focus_mask True
            idle "Gallery/gwengallery09.png" xpos 1478 ypos 700
            hover "Gallery/gwengallery09.png"
            action Jump ("GwenGallery09")

    if renpy.seen_image("amygwenlingerie01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("GwenGallery")

    add "Gallery/gallerygrid02.png"
    add "Gallery/textgwen.png"

label GwenGallery01:
scene pool05
show gwenpool01
gw "And what brings you here? You need to relax?"
mc "Yeah. What about you? Aren't you supposed to be working in the lab with Debra?"
gw "Not right now. Thanks God I'm allowed every now and then to escape the daily routine of getting fired at or burnt or maimed in the most excrutiating way Debra can find..."
mc "You look beautiful in that bikini Gwen."
gw "Thanks [name]. That means... not a lot to me. For your information, the only thing I care about is finishing my PhD..."
mc "Ah, right.. Anything I could do to help you with that?"
gw "Well, except if you have the brains of Albert Einstein, which, no offense, you clearly DON'T, the only thing I could think of..."
gw "...You could always help me in the lab. I work on the side on top of what Debra tells me to do to finish my PhD."
hide gwenpool01
show gwenpool04
with fastdissolve
gw "If you did the same, I could finish my experiments faster and finally write up my thesis!"
mc "Alright, I'll think about it. Are you hurt right now? Maybe I can give you a back rub."
gw "Oh, wow, that would be wonderful! I've just been beaten with a stick by this lunatic who wanted to test its rigidity so I am all sore back there..."
scene gwenrub01 with dissolve
mc "I'll start with a thigh rub."
gw "Fine by me, let's see how good you are with your hands, when you're not breaking stuff in the lab..."
scene gwenrub02 with dissolve
play sound "Sounds/womanmoan.mp3"
mc "(She's enjoying it...)"
scene gwenrub03 with dissolve
gw "That's a bit naughty of you to be rubbing my crotch like that [name]... But I liked your massage, I feel so much more relaxed..."
gw "I can go back to the lab now and work on my thesis, thanks to that relaxing \"massage\"."
mc "You're welcome!"
jump GwenGallery

label GwenGallery02:
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
call screen sciencefuck01y
screen sciencefuck01y:
    add sciencefuck01
    modal True
    button:
        xpos .91
        ypos .44
        xysize(140, 80)        
        action Jump ("ScienceFuck02y")        
label ScienceFuck02y:
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
jump GwenGallery

label GwenGallery03:
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
label GwenDebraSexSlowy:
play music "Sounds/debrasex.mp3"
scene gwendebrabackground blurred
show gwendebrasexslow
call screen gwendebrasexslowy
screen gwendebrasexslowy:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenDebraSexEndy")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenDebraSexFasty") 

label GwenDebraSexFasty:
scene gwendebrabackground
show gwendebrasexfast
de "Get the fucking antidote [name], I can't take much more of that pounding!"
mc "I'm looking for it Professor..."
call screen gwendebrasexfasty
screen gwendebrasexfasty:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenDebraSexEndy")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("GwenDebraSexSlowy")

label GwenDebraSexEndy:
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
jump GwenGallery

label GwenGallery04:
stop music
scene strip01
show stripgwen01
gw "Oh, hello [name]... I am a bit embarrassed... I mean, we  are colleagues..."
mc "Don't worry, I won't tell Debra."
hide stripgwen01
show stripgwen02 with fastdissolve
gw "Thanks! In that case, I am willing to provide my services to you... In exchange for a fee of course..."
mc "I'll take a striptease session please."
hide stripgwen02
show stripgwen01
with fastdissolve
gw "Relax in the comfy chair and watch... My body being displayed to you for hard cash."
play music "Sounds/stripmusic.mp3"
scene gwenstriplarge with dissolve:
        ypos -3.0
        linear 10.0 ypos 0.0
$ renpy.pause(10.0, hard=True)
gw "Ready?"
mc "Fuck yeah!"
scene gwenstrip01 with dissolve
pause
scene gwenstrip02 with dissolve
gw "Oh,I forgot my make-up! Let me get it... I'll look naughtier with it."
pause
scene gwenstrip03 with dissolve
pause
scene gwenstrip04 with dissolve
pause
scene gwenstrip05 with dissolve
pause
scene gwenstrip06 with dissolve
pause
scene gwenstrip07 with dissolve
pause
scene gwenstrip08 with dissolve
pause
scene gwenstrip09 with dissolve
pause
scene gwenstrip10 with dissolve
pause
stop music
scene strip01
show stripgwen04
with dissolve
gw "That's it, I see you liked the show didn't you [name]?..."
mc "Yes, thank you. I shall now go and have a.. wank."
gw "Eew, too much information..."    
jump GwenGallery

label GwenGallery05:
scene strip01
show stripamy01
am "Oh, hello [name]... You finally decided to come and see me \"in the flesh\"..."
mc "In the flesh, I can see the soul better."
am "How deep of you."
mc "Yeah, I can go pretty deep..."
am "So what would you like me to do so you can relax that tension tonight?"
mc "I'm in for a dual-babes session with Gwen please!"
am "I'll call her then... Sit back and enjoy the show."
play music "Sounds/stripmusic.mp3"
scene amygwenstrip01 with dissolve
pause        
scene amygwenstrip02 with dissolve
pause
scene amygwenstrip03 with dissolve
pause
scene amygwenstrip04 with dissolve
pause        
scene amygwenstrip05 with dissolve
pause      
scene amygwenstrip07 with dissolve
pause
scene amygwenstrip08 with dissolve
pause        
scene amygwenstrip09 with dissolve
pause
scene amygwenstrip10 with dissolve
pause        
stop music
scene strip01
show stripamy04 at midleft with fastdissolve
show stripgwen04 at midright with fastdissolve
am "That's it, time to cough up the money [name]..."
mc "Sure, sure, let me fondle inside my pockets... Ahem, oh, what's that I feel?"
gw "Give it up, we ain't playing with your dong, just pay up!"
mc "Right, right..."    
jump GwenGallery

label GwenGallery06:
scene strip02 blurred
show stripgwen04
gw "So... Are you ready for your $20 handjob?"
mc "Fuck yeah! I'm as hard as granite right now!"
scene gwenprehandjob01 with dissolve
gw "I can see that... It's so fucking LONG and FAT. And you're already drooling precum all over the place. Am I making you THAT horny?"
mc "Y...YES... OH shit, I think I'm gonna..."
scene gwenprehandjob02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...CUM already! AAAH!"
gw "Oh, wow! You really ARE horny tonight, aren't you?"
scene gwenprehandjob03 with dissolve
mc "Phew... Yeah, that was just a tiny horny spurt... I... think you can go ahead with the handjob now... I seem to have calmed down a bit."
gw "I will... I'll tease you slowly with my nails at first..."
play channel1 "Sounds/nailtease.mp3"
play channel2 "Sounds/boymoan02.mp3"
label GwenHandjobSlowx:
show stripgwenhandjobslow
hide stripgwenhandjobfast
call screen gwenhandjobslowx
screen gwenhandjobslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenHandjobEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenHandjobFastx") 

label GwenHandjobFastx:
gw "Maybe I should tease your trembling cock a little faster, hum? I think that'll make you CUM, right?"
mc "Aaaah..."
window hide
hide stripgwenhandjobslow
show stripgwenhandjobfast
call screen gwenhandjobfastx
screen gwenhandjobfastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenHandjobEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("GwenHandjobSlowx") 

label GwenHandjobEndx:
scene gwenhandjobcum01 with dissolve
stop channel1
stop channel2
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
gw "That's it [name], let it ALL out!"
scene gwenhandjobcum02 with dissolve
gw "You're pumping spunk out of your fat shaft like a FIREHOSE! My long nails really bloated your balls with a HEAVY DOSE!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene gwenhandjobcum03 with dissolve
mc "AAAAH! Y... YES... AAAH, Can't stop CUUUUMMMIING!"
gw "How can you cum THAT much? You truly are a SPERM MACHINE!"
scene gwenhandjobcum04 with dissolve
stop sound
gw "Oh my God... I'm plastered in your load... I'm gonna have to clean myself up by... slurping it in my mouth."
mc "You go ahead Gwen. And you can lick the drops that landed on me too while you're at it..."
gw "MMmh, you're such a NAUGHTY boy."
scene strip01
show stripgwen04b
with dissolve
gw "That's it, I hope you enjoyed my... teasing handjob. Now I've got to take a shower, I still feel all sticky..."
mc "And I think I'll have a good night's sleep. Phew!"
jump GwenGallery

label GwenGallery07:
play channel1 "v07/datemusic.mp3"
scene canyon01
show gwendate01
gw "I haven't been on a date for so long. Like, ever since I started my PhD thesis and I stopped having a life."
mc "Well, this date will be so great you'll remember it for the rest of your life!"
hide gwendate01
show gwendate02
with fastdissolve
gw "I like your enthusiasm. But I have to warn you that I prefer older guys personally..."
mc "Older MUSCULAR guys?"
gw "I don't care for that. As long as they have lots of money."
mc "Well, I might not be loaded with money, but I'm loaded in some other ways, if you catch my drift..." 
hide gwendate02
show gwendate01
with fastdissolve
gw "I guess sperm is a valued asset these days. Especially alpha-radiated cum."
mc "Think of the monetary value of all the sperm I ejaculated inside you during that science experiment gone wrong, and you'll see the whole episode in a brand new light."
hide gwendate01
show gwendate03
with fastdissolve
gw "You nearly KILLED ME with it. And the gallons of cum you pumped into me were discarded by Doctor Tara anyway. So I got NOTHING out of it."
mc "Maybe she kept it somewhere. In a fridge. I like to think I'm actually a millionnaire. Depending on my mood at the time of the IRS audit." 
hide gwendate03
show gwendate02
with fastdissolve
gw "Is this date going anywhere?"
mc "Err, right... Let's go for a swim in this pristine water, shall we?"
hide gwendate02
show gwendate03
with fastdissolve
gw "About bloody time!"
mc "Naked?"
hide gwendate03
show gwendate02
with fastdissolve
gw "Don't push your luck... Yet."
scene gwendate04 with dissolve
mc "So, how are you enjoying your date with me, Gwen?"
gw "I'll grant you it's a... change from working in the lab."
scene gwendate05 with dissolve
gw "And you can't turn into a Hulk-raping monster here at least."
mc "I wasn't myself then."
scene gwendate06 with dissolve
gw "Yes I know. But can you be a gentle, caring lover?"
mc "Err... Sure I can, anything for you Gwen!"
gw "Why don't you come closer and show me..."
scene gwendate07 with dissolve
play sound "Sounds/kiss.mp3"
gw "You're a decent kisser... Kiss me some more and play with my breasts..."
scene gwendate08 with dissolve
play sound "Sounds/kiss.mp3"
play sound "Sounds/womanmoan.mp3"
gw "Mmmh... Just like that... Here, let me help you..."
scene gwendate09 with dissolve
gw "AAAH! You're making my sensitive nipples so hard! Now let me return the favor..."
scene gwendate10 with dissolve
gw "Your cock seems to like my ass grinding against it... I can feel it HARDEN and GROW!"
mc "Uh..Oh.. I'm sorry, you're just so hot, I can't help but get a boner!"
gw "Well, make good use of it then, stick it between my legs... I want to PLAY with it."
scene gwendate11 with dissolve
gw "Wow, it's so MASSIVE and LONG, it looks like I have a HUGE FUTA COCK!"
play sound "Sounds/boymoan.mp3"
mc "AAAh.... You're gonna make me CUM Gwen!"
scene gwendate12 with dissolve
gw "No, I'm going to make ME CUM! This is MY COCK NOW!"
play channel2 "Sounds/wank.mp3"
scene gwendate13 with fastdissolve
pause 0.2
scene gwendate12 with fastdissolve
pause 0.2
scene gwendate13 with fastdissolve
pause 0.2
scene gwendate12 with fastdissolve
pause 0.2
scene gwendate13 with fastdissolve
pause 0.2
scene gwendate12 with fastdissolve
pause 0.2
scene gwendate13 with fastdissolve
pause 0.2
scene gwendate12 with fastdissolve
pause 0.2
scene gwendate13 with fastdissolve
pause 0.2
scene gwendate12 with fastdissolve
pause 0.2
scene gwendate13 with fastdissolve
pause 0.2
scene gwendate12 with fastdissolve
pause 0.2
scene gwendate13
show gwendate13cum
with fastdissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
gw "Yes, I'm CUMMING OUT OF MY HUGE FUTA COCK!"
mc "AAAH!"
scene gwendate14 with dissolve
stop channel2
stop sound
gw "Thanks for letting me act out of this little fantasy of mine [name]..."
mc "You're welcome... Wow, you really pumped me dry. I mean, pumped yourself dry..."
gw "I can see that, cum puddles are floating everywhere around us. I hope no one else plans on coming here today..."
scene canyon01
show gwendate01
with dissolve
gw "I think that date went pretty well at the end... But I'm exhausted, so let's go back to the compound."
mc "Sure... I'm exhausted too for some reason."
$ gwendatedone = True
$ gwendateon = False
stop channel1
jump GwenGallery

label GwenGallery08:
scene bedroom01
show gwenlingerie01 with moveinright
gw "I'm guessing you called me late at night to satisfy my sexual needs. So I came in lingerie."
mc "You walked through the corridors half-naked to get here?"
hide gwenlingerie01
show gwenlingerie02
with fastdissolve
gw "I was ALREADY half-naked because Debra tried to KILL me once again with one of her crazy experiments."
hide gwenlingerie02
show gwenlingerie03
with fastdissolve
gw "But that dastardly experience is over now, so we can move on to something much more PLEASURABLE..."
menu:
    "Dance for me Gwen, I want to see those big tits wiggle and jiggle in that hot lingerie!":
        jump GwenLingerie01x
    "Alright! Let's not waste time then, and let's move to the bed.":
        gw "Oh, so you don't want to see me slowly peel off my lingerie?"
        mc "Nope. Let's go straight to sex. Get naked and hop on the bed."
        jump GwenFuckChoiceax
        
label GwenLingerie01x:
hide gwenlingerie03
show gwenlingerie04
with fastdissolve
gw "I'll show why I'm the best stripper in the compound! Go and sit in the sofa and WATCH."
scene bedroom02 blurred
show gwenwiggle
with dissolve
play music "Sounds/stripmusic.mp3"
call screen gwenwigx
screen gwenwigx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenWiggleEndx")

label GwenWiggleEndx:
stop music
hide gwenwiggle
show gwenlingerie02
with dissolve
mc "I think you don't need a hypnosis pendulum to lure guys into your lair!"
gw "What are you babbling about?"
mc "Err... Nothing. Why don't you take ALL your clothes off for me, pretty please?"
hide gwenlingerie02
show gwenlingerie03
with fastdissolve
gw "But YOU need to take yours off too! *wink*"
hide gwenlingerie03
show gwenlingerie04
with fastdissolve
gw "I'll turn round first..."
scene bedroom02 blurred
show gwenlingerie05
mc "Oh yeah! Now peel your top off and turn back round..."
hide gwenlingerie05
show gwenlingerie06
with fastdissolve
mc "Such a nice pair of titties... Could you... Peel your panties off for me now? Slowly and sensuously..."
hide gwenlingerie06
show gwenlingerie07
with fastdissolve
gw "Alright, since you ask so nicely..."
hide gwenlingerie07
show gwenlingerie08
with fastdissolve
gw "Tada! All naked and ready for that young MONSTER SCHLONG!"
mc "And I'm ready too! Come over to the sofa, it's more comfortable...."
scene gwensofa01 with dissolve
mc "Now let's see what we're working on... Yeah, fucking nice tits..."
gw "What about my pussy?"
scene gwensofa02 with dissolve
mc "Yeah, I approve, nice and tender..."
play sound "Sounds/womanmoan.mp3"
gw "Oooh..."
scene gwensofa03 with dissolve
play sound "Sounds/kiss.mp3"
gw "*kiss* Thank you for taking care of me like that..."
mc "Now it's your turn... *kiss* ...to return the favor..."
gw "Oh yeah? How? *kiss*"
scene gwensofa04 with dissolve
mc "By sucking on my throbbing manhood!"
gw "I see... It sure looks yummy..."
play music "Sounds/hardsucking.mp3"
scene gwensofa06 with fastdissolve
pause 0.2
scene gwensofa05 with fastdissolve
pause 0.2
scene gwensofa06 with fastdissolve
pause 0.2
scene gwensofa05 with fastdissolve
pause 0.2
scene gwensofa06 with fastdissolve
pause 0.2
scene gwensofa05 with fastdissolve
pause 0.2
scene gwensofa06 with fastdissolve
pause 0.2
scene gwensofa05 with fastdissolve
pause 0.2
scene gwensofa06 with fastdissolve
pause 0.2
scene gwensofa05 with fastdissolve
pause 0.2
scene gwensofa06 with fastdissolve
pause 0.2
scene gwensofa05 with fastdissolve
pause 0.2
scene gwensofa06 with fastdissolve
pause 0.2
scene gwensofa05 with fastdissolve
pause 0.2
stop music
scene gwensofa07 with dissolve
gw "*pufff* Mmh, that was a good mouth exercise. Oooh, looks like you're right on the edge already! You're drooling more spunk than a month's worth of supply from a normal man..."
mc "Oh fuck, you blew me so good... I..."
show gwensofa07b with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
gw "GO ON, CUM! Yes, that's it, empty your nuts!"
mc "AAAH!"
gw "Look at how HUGE that cumshot is, I really made you BLAST your load BIG TIME, didn't I?"
show gwensofa07b  with flash
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Oh God, Gwen... RHAAA! There's more!"
gw "Keep delivering that sweet boygoo, [name]!"
scene gwensofa08 with dissolve
stop sound
play sound "Sounds/lick.mp3"
gw "*slurp* Ssso much CUM, you must be totally empty by now..."
scene gwensofa09 with dissolve
mc "No I'm not! I'm still raring to go! Just like a 74yo on dexamethasone! I'll show you what I'm capable of!"
gw "THROW me on the bed, [name]!"

label GwenFuckChoiceax:
scene bedroom03b
show gwenbed01
with dissolve
gw "And now bring that GIANT piece of boymeat over here..."

label GwenFuckChoicex:
stop music
menu:
    "Let's party like it's nineteen-69!":
        gw "This party will BLOW your mind..."
        jump GwenBlowjobx
    "I've got a PhD too. A Pretty huge Dick!":
        gw "Your puns are pathetic, but I'm willing to allow you to defend that so-called thesis of yours by FUCKING ME HARD!"
        jump GwenUpx
    "Stand up, I'll fuck your holes into the wall!":
        gw "BOTH holes? Pound them NICE and HARD, [name]!"
        jump GwenWallx
    "Well, fuck me sideways. No, I meant fuck YOU sideways!":
        gw "*sigh* Stop messing around and make good use of that HUGE WEAPON of yours!"
        jump GwenSidex
    "It is my duty to repopulate the Earth. And yours to get pregnant over and over again." if renpy.seen_image("gwenpreimpregnate01"):
        gw "Well, I finally submitted my thesis, so I can abandon all my career aspirations and become a conservative woman cum receptacle I guess."
        jump GwenImpregnationx
    "I'm done with this gallery.":
        jump GwenGallery

label GwenBlowjobx:
scene bedroom48
show gwenprefuck02
with dissolve
gw "That MONSTERDONG looks so... tasty and enticing... And ready to BURST already, precum is leaking down your shaft..."
mc "Go for it, I can take your HOT mouth."
scene bedroom18
show gwenprefuck03
with dissolve
mc "...While I lick your HOT pussy."
play sound "Sounds/moaning.mp3"
gw "Ooh, just like that, yes, mmmh! Shit, I NEED to SUCK on that cock so BAD!"
scene bedroom48 blurred with dissolve
play music "Sounds/hardsucking.mp3"
label GwenBlowSlowx:
hide gwenblowfast
show gwenblowslow
call screen gwenblowslow01x
screen gwenblowslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenBlowFastx") 

label GwenBlowFastx:
mc "Oh God, take me right to the edge now, Gwen!"
hide gwenblowslow
show gwenblowfast
call screen gwenblowfast01x
screen gwenblowfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("GwenBlowSlowx") 

label GwenBlowEndx:
stop music
hide gwenblowslow
hide gwenblowfast
show gwenblowcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "FUCK, AAAH!"
gw "*gobble*"
hide gwenblowcum01
show gwenblowcum02
with dissolve
gw "STILL spewing???"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Yeah, You made me so...AAAHHH... HORNY!"
scene bedroom49 blurred
show gwenblowcum03
with dissolve
stop sound
gw "I thought you'd never... *slurp* ... stop cumming. You gave me a... *lick* ... MASSIVE load!"
mc "Yeah, it was pretty big even by my standards. But enough chit-chat, I'm still HARD and I want MORE!"
play sound "Sounds/lick.mp3"
gw "Let me get... *slurp* ... myself cleaned up and I'll be with you in a sec."
scene bedroom03b
show gwenbed01
with dissolve
gw "There, now come and give me some MORE of that hot fuckstick..."
jump GwenFuckChoicex

label GwenUpx:
scene bedroom13
show gwenpreup01
with dissolve
mc "First, I'll show you what my Pretty huge Dick can do..."
gw "Wh... What do you have in mind?"
hide gwenpreup01
show gwenpreup02
with dissolve
mc "THIS!"
gw "Mmmmh, that's a POWERFUL opening statement, [name]!"
gw "Now dwell deeper into that theory of yours, inspect every nook and cranny with your \"PhD\"!"
play music "Sounds/womansex02.mp3"
label GwenLiftSlowx:
scene bedroom46
hide gwenupfast
show gwenupslow
call screen gwenupslow01x
screen gwenupslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenLiftEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenLiftFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("GwenLiftPOVSlowx") 

label GwenLiftFastx:
gw "You're pummeling me so HARD! But do it FASTER now!"
scene bedroom46
hide gwenupslow
show gwenupfast
call screen gwenupfast01x
screen gwenupfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenLiftEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("GwenLiftSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("GwenLiftPOVFastx") 

label GwenLiftPOVSlowx:
scene bedroom47
hide gwenuppovfast
show gwenuppovslow
call screen gwenuppovslow01x
screen gwenuppovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenLiftEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenLiftPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("GwenLiftSlowx") 

label GwenLiftPOVFastx:
gw "You're pummeling me so HARD! But do it FASTER now!"
scene bedroom47
hide gwenuppovslow
show gwenuppovfast
call screen gwenuppovfast01x
screen gwenuppovfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenLiftEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("GwenLiftPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("GwenLiftFastx")
            
label GwenLiftEndx:
gw "Time for your closing argument [name]!"
mc "I'm about to deliver it. BIG TIME!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene bedroom47 with fastdissolve
show gwenupcum01
mc "Here's my final statement! RHAAAA!"
gw "Oh God, you're ejaculating sssooo much spunk into my womb, I award you a degree CUM LOADED!"
hide gwenupcum01
show gwenupcum02
with fastdissolve
stop sound
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "AAAH! I still need to spermmark my thesis, here you go!"
scene bedroom46
show gwenupcum03
with fastdissolve
gw "Damn [name], did you get your degree in Fuckology or what?"
mc "Phew, you brought out the best in me, it was team work."
scene bedroom03b
show gwenbed01
with dissolve
gw "Come on, let's discover something new and exciting together then!"
jump GwenFuckChoicex
    
label GwenWallx:
scene bedroom42 with dissolve
show gwenprewall01
mc "Mmh, which hole should I choose first I wonder?..."
gw "I don't care what you choose, just FUCK ME!"
mc "Alright, I'll go with..."
menu:
    "Your backdoor!":
        hide gwenprewall01
        jump GwenWallAnalSlowx
    "Your front entrance!":
        hide gwenprewall01
        jump GwenWallPussySlowx

label GwenWallPussySlowx:
scene bedroom42
stop music
play music "Sounds/fucksound.mp3"
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
show gwenwallpussyslow
call screen gwenwallpussyslow01x
screen gwenwallpussyslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("GwenWallPussyEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenWallPussyFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("GwenWallAnalSlowx") 

label GwenWallAnalSlowx:
scene bedroom42
stop music
play music "Sounds/womansex01.mp3"
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallpussyslow
show gwenwallanalslow
call screen gwenwallanalslow01x
screen gwenwallanalslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("GwenWallAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenWallAnalFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("GwenWallPussySlowx") 

label GwenWallPussyFastx:
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
show gwenwallpussyfast
call screen gwenwallpussyfast01x
screen gwenwallpussyfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("GwenWallPussyEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("GwenWallPussySlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("GwenWallAnalSlowx") 

label GwenWallAnalFastx:
hide gwenwallpussyfast
hide gwenwallanalslow
hide gwenwallpussyslow
show gwenwallanalfast
call screen gwenwallanalfast01x
screen gwenwallanalfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("GwenWallAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("GwenWallAnalSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("GwenWallPussySlowx") 
            
label GwenWallPussyCumSlowx:
stop music
play music "Sounds/fucksound.mp3"
hide gwenwallpussycumfast
hide gwenwallanalcumfast
hide gwenwallanalcumslow
show gwenwallpussycumslow
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
call screen gwenwallpussycumslow01x
screen gwenwallpussycumslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("GwenWallPussyEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenWallPussyCumFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("GwenWallAnalCumSlowx") 

label GwenWallAnalCumSlowx:
stop music
play music "Sounds/womansex01.mp3"
hide gwenwallpussycumfast
hide gwenwallanalcumfast
hide gwenwallpussycumslow
show gwenwallanalcumslow
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
call screen gwenwallanalcumslow01x
screen gwenwallanalcumslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("GwenWallAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenWallAnalCumFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("GwenWallPussyCumSlowx") 

label GwenWallPussyCumFastx:
hide gwenwallanalcumfast
hide gwenwallanalcumslow
hide gwenwallpussycumslow
show gwenwallpussycumfast
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
call screen gwenwallpussycumfast01x
screen gwenwallpussycumfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("GwenWallPussyEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("GwenWallPussyCumSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("GwenWallAnalCumSlowx") 

label GwenWallAnalCumFastx:
hide gwenwallpussycumfast
hide gwenwallanalcumslow
hide gwenwallpussycumslow
show gwenwallanalcumfast
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
call screen gwenwallanalcumfast01x
screen gwenwallanalcumfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("GwenWallAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("GwenWallAnalCumSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("GwenWallPussyCumSlowx") 
            
label GwenWallPussyEndx:
mc "I'm about to flood your pussy, Gwen!"
gw "Go on, dump your nut inside me and then PLASTER my back with the rest, I need some skin lotion!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
hide gwenwallpussycumfast
hide gwenwallanalcumslow
hide gwenwallpussycumslow
hide gwenwallanalcumfast
if gwenwallanalcumx == False and gwenwallpussycumx == False:
    show gwenwallpussy05
    show gwenwallcumpussy01nocum
    with fastdissolve
    mc "You asked for it! RHAAA!!!"
    gw "Oooh, your cock gets even MORE MASSIVE with every POWERFUL jet of boygoo!"
    mc "Hang on Gwen, I've got some more cum lotion for your skin!"
    if persistent.cumsoundon:
        play sound "Sounds/cumming.mp3"
    hide gwenwallcumpussy01nocum
    hide gwenwallpussy05
    show gwenwallcumpussy02
    with fastdissolve
if gwenwallanalcumx or gwenwallpussycumx:
    show gwenwallpussycum05
    show gwenwallcumpussy01
    with fastdissolve
    mc "You asked for it! RHAAA!!!"
    gw "Oooh, your cock gets even MORE MASSIVE with every POWERFUL jet of boygoo!"
    mc "Hang on Gwen, I've got some more cum lotion for your skin!"
    if persistent.cumsoundon:
        play sound "Sounds/cumming.mp3"
    hide gwenwallcumpussy01
    hide gwenwallpussycum05
    show gwenwallcumpussy02
    with fastdissolve
gw "Oh my God, you've totally COVERED my back in your never-ending pellets."
$ gwenwallpussycumx = True
if gwenwallanalcumx:
    hide gwenwallcumpussy02
    show gwenwallcumanal03
    with fastdissolve    
    mc "Your holes have actually DRAINED me. temporarily of course. Get cleaned up and hop on the bed!"
    stop sound
    scene bedroom03b blurred
    show gwenbed01
    with dissolve
    gw "I don't even how you can still be hard after this MARATHON romp, but I'll gladly continue servicing your SEX PILLAR!"
    $ gwenwallpussycumx = False
    $ gwenwallanalcumx = False
    jump GwenFuckChoice
if gwenwallanalcumx == False:
    hide gwenwallcumpussy02
    show gwenwallcumanal03
    with fastdissolve    
    mc "I ain't done with you, still need to cum inside that enticing rosebud of yours..."
    hide gwenwallcumanal03
    play music "Sounds/womansex01.mp3"
    jump GwenWallAnalCumSlowx

label GwenWallAnalEndx:
mc "I'm about to flood your backdoor, Gwen!"
gw "YES! Give me a cum enema and then PLASTER the rest of my back!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
hide gwenwallpussycumfast
hide gwenwallanalcumslow
hide gwenwallpussycumslow
hide gwenwallanalcumfast
if gwenwallpussycumx == False and gwenwallanalcumx == False:
    show gwenwallanal05
    show gwenwallcumanal01nocum
    with fastdissolve
    mc "You asked for it! RHAAA!!!"
    gw "Oooh, your cock get even MORE MASSIVE with every POWERFUL jet of boygoo!"
    mc "Hang on Gwen, I've got some more cum lotion for your skin!"
    if persistent.cumsoundon:
        play sound "Sounds/cumming.mp3"
    hide gwenwallcumanal01nocum
    hide gwenwallanal05
    show gwenwallcumanal02
    with fastdissolve
if gwenwallpussycumx or gwenwallanalcumx:
    show gwenwallanalcum05
    show gwenwallcumanal01
    with fastdissolve
    mc "You asked for it! RHAAA!!!"
    gw "Oooh, your cock get even MORE MASSIVE with every POWERFUL jet of boygoo!"
    mc "Hang on Gwen, I've got some more cum lotion for your skin!"
    if persistent.cumsoundon:
        play sound "Sounds/cumming.mp3"
    hide gwenwallcumanal01
    hide gwenwallanalcum05
    show gwenwallcumanal02
    with fastdissolve
gw "Oh my God, you've totally COVERED my back in your never-ending pellets."
$ gwenwallanalcumx = True
if gwenwallpussycumx:
    hide gwenwallcumanal02
    show gwenwallcumanal03
    with fastdissolve    
    mc "Your holes have actually DRAINED me. temporarily of course. Get cleaned up and hop on the bed!"
    stop sound
    scene bedroom03b blurred
    show gwenbed01
    with dissolve
    gw "I don't even how you can still be hard after this MARATHON romp, but I'll gladly continue servicing your SEX PILLAR!"
    $ gwenwallpussycumx = False
    $ gwenwallanalcumx = False
    jump GwenFuckChoice
if gwenwallpussycumx == False:
    hide gwenwallcumanal02
    show gwenwallcumanal03
    with fastdissolve    
    mc "I ain't done with you, still need to cum inside that enticing fuckhole of yours..."
    hide gwenwallcumanal03
    play music "Sounds/fucksound.mp3"
    jump GwenWallPussyCumSlowx
    
label GwenSidex:
scene bedroom17
show gwenprefuck04
with dissolve
gw "Ooh, you're so grabby [name]!"
mc "That's cos they are so many good things to grab on YOU!"
scene bedroom16 blurred
show gwenprefuck05
with dissolve
mc "Your pussylips are just so moist... You really want this, don't you?"
gw "Yes I DO! Please, just stick it inside me, I NEED IT!"
scene bedroom16 blurred with dissolve
play music "Sounds/wank.mp3"
label GwenSideSlowx:
hide gwensidefast
show gwensideslow
call screen gwensideslow01x
screen gwensideslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenSideEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenSideFastx") 

label GwenSideFastx:
gw "GRAB me FASTER! I want to be GRABBED so BAD!"
hide gwensideslow
show gwensidefast
call screen gwensidefast01x
screen gwensidefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenSideEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("GwenSideSlowx") 

label GwenSideEndx:
mc "That's it, your pussy muscles are grabbing onto my shaft so hard, they're pulling the cum right out of my nuts..."
hide gwensideslow
hide gwensidefast
show gwensidecum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...And I'm cumming!"
gw "Yes, let me GRAB as much CUM from you as I can! And then, GRAB your cock and spew your load EVERYWHERE!"
hide gwensidecum01
show gwensidecum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
gw "That's it, fire those salvoes of sweet boycum all over me! AAAHH, I LOVE IT!"
mc "RHAAA! Here it comes, Gwen!"
hide gwensidecum02
show gwensidecum03
with fastdissolve
stop sound
gw "Look at the filthy mess you've made [name]. You're such a naughty boy. Grabbing girls like that and cumming all over them..."
mc "Well, I'm a celebrity now, so I guess I'm allowed to do it, right?"
gw "You're DIRTIER than a DIRTY old man. Now FUCK ME SOME MORE!"
scene bedroom03b blurred
show gwenbed01
with dissolve
gw "So, what are you going to GRAB next?"
jump GwenFuckChoicex

label GwenImpregnationx:
scene bedroom17
show gwenpreimpregnate01 with dissolve
gw "How.. Are we going to proceed? I've never done this in order to get pregnant."
mc "Don't worry, just lie down and let my cum-missile do all the work. And let me churn up a MONSTER LOAD for you by some sexy pre-impregnation fun."
scene bedroom16
show gwenpreimpregnate02 
with fastdissolve
play sound "Sounds/moaning02.mp3"
mc "...Like playing with those big funbags."
play sound "Sounds/lick.mp3"
mc "... And licking those tasty nipples... Mmmh..."
play sound "Sounds/moaning.mp3"
gw "Oooh! I like what you're doing... My body, I'm getting all tingly... Come and kiss me."
scene bedroom17 blurred
show gwenpreimpregnate03 
with fastdissolve
play sound "Sounds/kiss.mp3"
gw "Please... [name]... I want a baby! I know this is my duty now, you've convinced me."
scene bedroom12
show gwenpreimpregnate04 
with fastdissolve
mc "And now let the sperm flow and the impregnation begin!"
play music "Sounds/womansex02.mp3"
label GwenPregnantSlowx:
hide gwenimpregnatefast
hide gwenimpregnatepovslow
hide gwenimpregnatepovfast
scene bedroom12
show gwenimpregnateslow
call screen gwenimpregnateslow01x
screen gwenimpregnateslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenPregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenPregnantFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("GwenImpregnateSlowx") 

label GwenImpregnateSlowx:
hide gwenimpregnateslow
hide gwenimpregnatefast
hide gwenimpregnatepovfast
scene bedroom14 blurred
show gwenimpregnatepovslow
call screen gwenimpregnatepovslow01x
screen gwenimpregnatepovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenPregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("GwenImpregnateFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("GwenPregnantSlowx") 

label GwenPregnantFastx:
hide gwenimpregnateslow
hide gwenimpregnatepovslow
hide gwenimpregnatepovfast
scene bedroom12
show gwenimpregnatefast
call screen gwenimpregnatefast01x
screen gwenimpregnatefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenPregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("GwenPregnantSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("GwenImpregnateFastx") 

label GwenImpregnateFastx:
hide gwenimpregnateslow
hide gwenimpregnatefast
hide gwenimpregnatepovslow
scene bedroom14 blurred
show gwenimpregnatepovfast
call screen gwenimpregnatepovfast01x
screen gwenimpregnatepovfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("GwenPregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("GwenImpregnateSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("GwenPregnantFastx") 
            
label GwenPregnantEndx:
stop music
scene bedroom12
show gwenimpregnatecum01
with dissolve
play music "Sounds/splooge02.mp3"
gw "Yes, pump your virile cream inside my womb, AAAH!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
show gwenimpregnatecum01 with flash
mc "I AM, RHAAA!"
scene bedroom12 blurred
show gwenimpregnatecum02 with dissolve
stop music
play sound "Sounds/splooge01.mp3"
gw "You're coming ssoo much, it looks like I'm pregnant with your ball-batter!"
mc "You'll get pregnant for real soon enough! AAHH, STILL COMING!"
show gwenimpregnatecum02 with fastflash
gw "You're coming ssoo much, it looks like I'm pregnant with your ball-batter!"
mc "You'll get pregnant for real soon enough! AAHH, STILL COMING!"
stop music
scene bedroom14
show gwenimpregnatecum03
with fastdissolve
play sound "Sounds/gasp.mp3"
gw "Oh my God, I'm so bloated with your spunk that I'm leaking cum like a faucet..."
mc "When a cum receptacle is full, it's either that or a massive explosion. So count yourself lucky. And pregnant."
scene bedroom12 blurred
show gwenimpregnatecum04
with fastdissolve
gw "Oh my God, I'm so bloated with your spunk that I'm leaking cum like a faucet..."
mc "When a cum receptacle is full, it's either that or a massive explosion. So count yourself lucky. And pregnant."
gw "You're a great sperm provider, but a lousy future father I can already tell."
mc "I told you my job was to impregante you. And that is what I did. Let's go to sleep and think of your bright future ahead as a mother."
jump GwenFuckChoicex

label GwenGallery09:
play music "v07/datemusic.mp3"
scene bedroom01
show amylingerie01 at midleft with moveinleft
show gwenlingerie01 at midright with moveinright
am "Hi [name], you called for BOTH of us?"
mc "That's right. Tonight, I feel especially horny and I've got enough spunk in my balls to satisfy you BOTH."
gw "Mmmh, I like hearing that..."
hide amylingerie01
hide gwenlingerie01
show amygwenlingerie01 with dissolve
am "Alright! Let's get that horny BULLCOCK of yours BIG and HARD then!"
hide amygwenlingerie01
show amygwenlingerie02 with dissolve
gw "What do you have in mind Amy? I see you're looking at my big tits..."
am "I want to FEEL them. And show [name] how full and RIPE they are..."
hide amygwenlingerie02
show amygwenlingerie03 with dissolve
gw "Do you hear that [name]? But you can't touch, you can just watch. For the moment..."
hide amygwenlingerie03
show amygwenlingerie04 with dissolve
am "Mmh, they are so BIG and soft, I love your tits Gwen..."
gw "And I like how you fondle them. Your hands are so delicate. Not like the burly hands of some horny boy who doesn't know what he's doing."
mc "Hey! I'm a Master Tit-Fondler I'll have you know!"
hide amygwenlingerie04
show amygwenlingerie05 with dissolve
gw "Is that so? We'll see about that."
am "I'll take my top off too [name]. Do you think you can handle TWO pairs of sumptuous breasts?"
mc "Sure I can! I have TWO hands I'll have you know."
scene bedroom35 blurred
show amygwenlingerie06 with dissolve
gw "Silly boy. Watch and learn how women like to be pleased..."
play sound "Sounds/lick.mp3"
am "Mmmh, Gwen!"
mc "That's it, I'm coming over to take control of this sordid situation!"
scene bedroom13 blurred
show amygwenlingerie07 with dissolve
mc "See, I can fondle tits just as well as the next girl."
gw "Ooh yeah... Now let me fondle that hardening SLAB of meat..."
am "Get him HARD Gwen, I want to have fun with his giant fuckstick!"
mc "Alright girls! Let's move to the sofa and I'll let you admire it in all its ROCK-HARD GLORY!"
stop music
scene gwenamybedroom01 with dissolve
am "Ooh, look at that STIFF cock, Gwen, it's like a bar of iron! [name] must be sssoo excited!"
gw "And it looks so DELICIOUS..."
am "Why don't you have a go on it first then? I'll hold the base for you."
scene gwenamybedroom02 with dissolve
mc "Aaaah..."
am "There you go... Try and stretch your mouth even further..."
scene gwenamybedroom03 with dissolve
gw "GGGllbrrr..."
am "Mmmh, she's really gobbling your cock isn't she [name]?"
scene gwenamybedroom02 with fastdissolve
pause 0.2
scene gwenamybedroom03 with fastdissolve
pause 0.2
scene gwenamybedroom02 with fastdissolve
pause 0.2
scene gwenamybedroom03 with fastdissolve
pause 0.2
scene gwenamybedroom02 with fastdissolve
pause 0.2
scene gwenamybedroom03 with fastdissolve
pause 0.2
scene gwenamybedroom02 with fastdissolve
pause 0.2
scene gwenamybedroom03 with fastdissolve
pause 0.2
scene gwenamybedroom02 with fastdissolve
pause 0.2
scene gwenamybedroom03 with fastdissolve
pause 0.2
scene gwenamybedroom02 with fastdissolve
pause 0.2
scene gwenamybedroom01 with dissolve
gw "*pufff* Mmh, that was a good mouth exercise..."
am "My turn..."
scene gwenamybedroom04 with dissolve
mc "Oh God!"
gw "Twirl that tongue on his sensitive tip, it'll make him delirious with lust!"
scene gwenamybedroom05 with fastdissolve
pause 0.2
scene gwenamybedroom04 with fastdissolve
pause 0.2
scene gwenamybedroom05 with fastdissolve
pause 0.2
scene gwenamybedroom04 with fastdissolve
pause 0.2
scene gwenamybedroom05 with fastdissolve
pause 0.2
scene gwenamybedroom04 with fastdissolve
pause 0.2
scene gwenamybedroom05 with fastdissolve
pause 0.2
scene gwenamybedroom04 with fastdissolve
pause 0.2
scene gwenamybedroom05 with fastdissolve
pause 0.2
scene gwenamybedroom04 with fastdissolve
pause 0.2
scene gwenamybedroom05 with fastdissolve
pause 0.2
scene gwenamybedroom04 with fastdissolve
pause 0.2
scene gwenamybedroom05 with fastdissolve
pause 0.2
scene gwenamybedroom04 with fastdissolve
pause 0.2
scene gwenamybedroom01
show gwenamybedroom01b
with dissolve
gw "Oooh, looks like he's right on the edge! He's drooling more spunk than a month's worth of supply from a normal man..."
mc "AAAh, please stop pumping my shaft..."
am "Why would I stop, you need to..."
scene gwenamybedroom06 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
am "...CUM! Yes, that's it, empty your nuts!"
gw "Look at how HUGE that cumshot is, we really made him BLAST his load BIG TIME, didn't we?"
scene gwenamybedroom06 with flash
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Oh God, you girls... RHAAA! There's more!"
gw "Keep delivering that sweet boygoo, [name]!"
scene gwenamybedroom07 with dissolve
stop sound
play sound "Sounds/lick.mp3"
gw "*slurp*"
am "Ssso much CUM, you must be totally empty by now..."
mc "I'm still raring to go! Just like a 74yo on dexamethasone! So get on the bed my horny harem girls and I'll show you what I'm capable of!"
scene bedroom03b
show amygwenbed01
with dissolve
am "So. We're waiting, STUD."
stop music
label AmyGwenFuckChoicex:
stop music
menu:
    "I need to fuck Gwen's tight pussy. I just need to.":
        am "What kind of harem girls would we be if we'd deny our harem master what he wants?"
        mc "Some pretty bad ones I reckon."
        gw "We're GOOD harem girls. So yes, come and fuck my pussy. NOW."
        jump AmyGwenFuckx
    "How about Gwen rides me while I lick some sweet Amy pussy.":
        am "My pussy is \"sweet\"? That's such a sweet thing to say."
        gw "Get on your back, bronco, this girl is going to ride you WILD!"
        jump AmyGwenRidex
    "I want to dip my rod into Amy's tight butt while she licks Gwen's pussy.":
        am "Well, are you the romantic type..."
        gw "I'm in! It'll give my holes a bit of respite..."
        am "I see. Then, I will sacrifice my backdoor for you, Gwen!"
        jump AmyGwenAnalx
    "Let me enjoy watching some ANAL fisting action...":
        am "And who should fist who?"
        mc "Gwen is used to huge things being stuck inside her because... err... Just fist her, Amy!"
        gw "I agree only because I know she won't be as MONSTROUS as YOU!"
        jump AmyGwenFistx
    "I'd like some wall-banging special time with Gwen.":
        am "And what am I supposed to do in the meantime?"
        mc "You can watch and frig yourself silly."
        gw "I'll make him cum in no time, don't worry Amy!"
        jump AmyGwenWallx
    "I'd like some missionary special time with Amy.":
        gw "I don't mind, my holes need some... rest."
        am "Alright, so it's just you and me, [name]!"
        jump AmyGwenMissionaryx
    "I'm done with this gallery.":
        jump GwenGallery

label AmyGwenFuckx:
scene bedroom34
show amygwenprefuck01
with dissolve
mc "Are you ready for my rod, Gwen?"
am "Look at it dripping all that filthy precum..."
gw "I don't know... It looks so HUGE."
mc "Well, only one way to find out..."
am "To SHOVE it in DEEP and HARD inside her pussy!"
scene bedroom12 blurred with dissolve
play music "Sounds/fucksound.mp3"
label AmyGwenFuckSlowx:
hide amygwenfuckfast
show amygwenfuckslow
call screen amygwenfuckslow01x
screen amygwenfuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyGwenFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AmyGwenFuckFastx") 

label AmyGwenFuckFastx:
mc "AAHH... You're so tight... I'm going to have to ram my dick inside you FASTER!"
gw "Oh Lord! It's just so THICK!"
hide amygwenfuckslow
show amygwenfuckfast
call screen amygwenfuckfast01x
screen amygwenfuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyGwenFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AmyGwenFuckSlowx") 

label AmyGwenFuckEndx:
am "OOoh, I think [name] is getting there... His MONSTERDICK is PULSING inside your little pussy, Gwen!"
gw "AAH! Y..Yes! OOH! I can... FEEL IT TOO!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
hide amygwenfuckslow
hide amygwenfuckfast
show gwenthreesomefuckcum01
with fastdissolve
mc "RHAAA! Here I come!"
gw "It's squirting inside me! AAAH!"
hide gwenthreesomefuckcum01
show gwenthreesomefuckcum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Damn, I'm nutting directly into your stomach, sssoooo fucking goood! AAAH"
scene bedroom34 blurred
show gwenthreesomefuckcum03
with fastdissolve
am "Look at all that cum on your face and body Gwen... You made [name] spew a MONSTERLOAD!"
mc "And the good news is, I'm STILL HARD for MORE!"
stop sound
am "Are we ever going to be able to go to sleep I wonder?"
gw "This was so good, I don't care if I'm tired in the morning, I just want more of that HOT HORSEDICK!"
scene bedroom03b
show amygwenbed01
with dissolve
am "So, what do you have in store for us, big boy?"
jump AmyGwenFuckChoicex
    
label AmyGwenRidex:
scene bedroom12
show gwenthreesomeprefuck03
with dissolve
gw "Oh my God, look at how ERECT [name]'s cock is! It's like a bar of TITANIUM!"
am "All the better to FUCK you with it! While he licks my pussy..."
mc "Go on, Gwen... *slurp* Ride me!"
scene bedroom12 blurred with dissolve
play music "Sounds/fucksound.mp3"
label AmyGwenRideSlowx:
hide amygwenridefast
show amygwenrideslow
call screen amygwenrideslow01x
screen amygwenrideslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyGwenRideEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AmyGwenRideFastx") 

label AmyGwenRideFastx:
gw "That dong is just so THICK! Need... to... ride it... FASTER!"
am "To make him ERUPT and COVER our bodies in THICK SPUNK!"
hide amygwenrideslow
show amygwenridefast
call screen amygwenridefast01x
screen amygwenridefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyGwenRideEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AmyGwenRideSlowx") 

label AmyGwenRideEndx:
mc "That's it, ride my shaft! Just like that... I...."
gw "Oooh, I think it's about to happen!"
stop music
play sound "Sounds/splooge01.mp3"
hide amygwenrideslow
hide amygwenridefast
show gwenthreesomecum01
with fastdissolve
mc "AAAAH! AAAAAH!"
gw "He's whitewashing my womb with his MONSTER LOAD of young cum!"
scene bedroom41 blurred
show gwenthreesomecum02
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Damn, that pussy is still as tight as ever and milking me BIG TIME! AAAH!"
gw "Let me TASTE THIS! *slurp* Before I remove than ERUPTING cum-cannon so I can get hit directly by those MASSIVE salvoes of sperm!"
scene bedroom18 blurred
show gwenthreesomecum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
am "That's it, pump that seed all over us! I want it to cover my face in an INCH-THICK layer of semen!"
mc "RHAAA! Take that my cum-hungry harem girls!"
scene bedroom41 blurred
show gwenthreesomecum04
with dissolve
play sound "Sounds/kiss.mp3"
am "Let's exchange his yummy nutjuice with our tongues... *kiss*"
gw "*slurp* Mmmh, it's so tasty..."
mc "Oh God, that's it, instant BONER right there!"
am "Good, cos we want MORE of that cum of yours!"
play sound "Sounds/kiss.mp3"
gw "Let us get cleaned up... *kiss* And we'll be right there to take care of your GIANT hardon..."
stop sound
scene bedroom03b
show amygwenbed01
with dissolve
gw "We're waiting... Take your pick. And choose something nice and SEXY."
jump AmyGwenFuckChoicex
    
label AmyGwenAnalx:
scene bedroom20
show gwenthreesomeprefuck02
with dissolve
mc "Let's do this on the floor, the bed isn't big enough for what I have in mind..."
scene bedroom45 blurred
show gwenthreesomeprefuck01
with dissolve
am "See my tender rosebud? It's all yours tonight...So come and claim it, STUD!"
mc "I sure will, get ready for the ass-drilling of your lifetime, Amy!"
play music "Sounds/fucksound.mp3"
label AmyGwenAnalSlowx:
scene bedroom43
hide amygwenanalfast
show amygwenanalslow
call screen amygwenanalslow01x
screen amygwenanalslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyGwenAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AmyGwenAnalFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AmyGwenAnalSlowbx") 

label AmyGwenAnalFastx:
am "Please, just ANALYZE me even FASTER and HARDER!"
scene bedroom43
hide amygwenanalslow
show amygwenanalfast
call screen amygwenanalfast01x
screen amygwenanalfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyGwenAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AmyGwenAnalSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AmyGwenAnalFastbx") 

label AmyGwenAnalSlowbx:
scene bedroom44
hide amygwenanalbfast
show amygwenanalbslow
call screen amygwenanalslow01bx
screen amygwenanalslow01bx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyGwenAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AmyGwenAnalFastbx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("AmyGwenAnalSlowx") 

label AmyGwenAnalFastbx:
scene bedroom44
hide amygwenanalbslow
show amygwenanalbfast
call screen amygwenanalfast01bx
screen amygwenanalfast01bx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyGwenAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AmyGwenAnalSlowbx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("AmyGwenAnalFastx") 

label AmyGwenAnalEndx:
mc "FUCK YEAH! I'm just about...."
scene bedroom45 blurred
show gwenthreesomeanalcum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...to CUUUUMMMMM! RHAAAA!"
am "OOOh, my bowels are EXPLODING with cum! AAAH! Please pull out, I feel like I'm past breaking point [name]!!!"
scene bedroom44
show gwenthreesomeanalcum02
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Take those shots on your back then! AAAH!"
am "Mmmh, yes, it's so hot and so thick!"
scene bedroom43 blurred
show gwenthreesomeanalcum03
am "I can feel OUNCES of your cum on my back.... It feels warm and filthy..."
gw "And his shots were so POWERFUL that I'm also CAKED in his sweet young boycum... Mmmh..."
mc "I aim to please my harem girls and regularly give them nourishing snacks of proteins."
scene bedroom03b
show amygwenbed01
with dissolve
am "And you DID. But we're hungry for ANOTHER snack!"
jump AmyGwenFuckChoicex

label AmyGwenFistx:
scene bedroom20
show gwenlesbians01
with dissolve
am "So, are you ready for this Gwen? Just tell me if you want out..."
gw "No, it's ok, I know you... And how considerate you are..."
am "Let's show him how to treat women well, he doesn't seem to have a clue..."
mc "Hey! I'm here and I can hear you!"
scene bedroom17
show gwenlesbians02
with dissolve
play sound "Sounds/womanmoan.mp3"
am "Oooh, Gwen, your tongue..."
scene bedroom34
show gwenlesbians03
with dissolve
play sound "Sounds/lick.mp3"
am "AAAH, you're making my pussy dripping wet..."
mc "Nice rimming going there, Gwen..."
am "Watch and learn, [name]. Oooh, this is so good..."
play sound "Sounds/womanmoan.mp3"
mc "I am watching, I am watching..."
scene bedroom23
show gwenlesbians04
with dissolve
am "And now, let me return the favor."
gw "Oooh, my ass is so eager... It's totally ready for your fist Amy."
play channel1 "Sounds/moaning02.mp3"
play channel2 "Sounds/wank.mp3"
scene bedroom16
label AmyGwenFistSlowx:
hide amygwenfistfast
show amygwenfistslow
call screen amygwenfistslow01x
screen amygwenfistslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyGwenFistEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AmyGwenFistFastx") 

label AmyGwenFistFastx:
gw "Your fist is almost as THICK as [name]'s MONSTERCOCK!!! Fist me FASTER, please Amy!"
hide amygwenfistslow
show amygwenfistfast
call screen amygwenfistfast01x
screen amygwenfistfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyGwenFistEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AmyGwenFistSlowx") 

label AmyGwenFistEndx:
am "I can feel she's getting there..."
gw "Ooh, ahh..."
hide amygwenfistslow
hide amygwenfistfast
show gwenfistcum01
with dissolve
stop channel1
stop channel2
play sound "Sounds/moaning03.ogg"
gw "AAAH! I'm cumming!"
am "She's squirting BIG TIME!"
scene bedroom34 blurred
show gwenfistcum02
with dissolve
am "Wwo, look at all this cuntjuice [name], it's literally EXPLODING from her pussy."
gw "That's cos your fisting was so good... and tender."
mc "Ok, I get it. I should fist women more nicely. Now let's get on with the show..."
scene bedroom03b
show amygwenbed01
with dissolve
am "We've had our fun. Now it's time for YOU to have some fun!"
jump AmyGwenFuckChoicex

label AmyGwenWallx:
scene bedroom42amy with dissolve
show gwenprewall01
mc "Mmh, which hole should I choose first I wonder?..."
gw "I don't care what you choose, just FUCK ME!"
mc "Alright, I'll go with..."
menu:
    "Your backdoor!":
        hide gwenprewall01
        jump AmyGwenWallAnalSlowx
    "Your front entrance!":
        hide gwenprewall01
        jump AmyGwenWallPussySlowx

label AmyGwenWallPussySlowx:
scene bedroom42amy
stop music
play music "Sounds/fucksound.mp3"
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
show gwenwallpussyslow
call screen amygwenwallpussyslow01x
screen amygwenwallpussyslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("AmyGwenWallPussyEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AmyGwenWallPussyFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("AmyGwenWallAnalSlowx") 

label AmyGwenWallAnalSlowx:
scene bedroom42amy
stop music
play music "Sounds/womansex01.mp3"
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallpussyslow
show gwenwallanalslow
call screen amygwenwallanalslow01x
screen amygwenwallanalslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("AmyGwenWallAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AmyGwenWallAnalFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("AmyGwenWallPussySlowx") 

label AmyGwenWallPussyFastx:
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
show gwenwallpussyfast
call screen amygwenwallpussyfast01x
screen amygwenwallpussyfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("AmyGwenWallPussyEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AmyGwenWallPussySlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("AmyGwenWallAnalSlowx") 

label AmyGwenWallAnalFastx:
hide gwenwallpussyfast
hide gwenwallanalslow
hide gwenwallpussyslow
show gwenwallanalfast
call screen amygwenwallanalfast01x
screen amygwenwallanalfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("AmyGwenWallAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("AmyGwenWallAnalSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("AmyGwenWallPussySlowx") 
            
label AmyGwenWallPussyCumSlowx:
stop music
play music "Sounds/fucksound.mp3"
hide gwenwallpussycumfast
hide gwenwallanalcumfast
hide gwenwallanalcumslow
show gwenwallpussycumslow
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
call screen amygwenwallpussycumslow01x
screen amygwenwallpussycumslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("AmyGwenWallPussyEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AmyGwenWallPussyCumFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("AmyGwenWallAnalCumSlowx") 

label AmyGwenWallAnalCumSlowx:
stop music
play music "Sounds/womansex01.mp3"
hide gwenwallpussycumfast
hide gwenwallanalcumfast
hide gwenwallpussycumslow
show gwenwallanalcumslow
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
call screen amygwenwallanalcumslow01x
screen amygwenwallanalcumslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("AmyGwenWallAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AmyGwenWallAnalCumFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("AmyGwenWallPussyCumSlowx") 

label AmyGwenWallPussyCumFastx:
hide gwenwallanalcumfast
hide gwenwallanalcumslow
hide gwenwallpussycumslow
show gwenwallpussycumfast
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
call screen amygwenwallpussycumfast01x
screen amygwenwallpussycumfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("AmyGwenWallPussyEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AmyGwenWallPussyCumSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("AmyGwenWallAnalCumSlowx") 

label AmyGwenWallAnalCumFastx:
hide gwenwallpussycumfast
hide gwenwallanalcumslow
hide gwenwallpussycumslow
show gwenwallanalcumfast
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
call screen amygwenwallanalcumfast01x
screen amygwenwallanalcumfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("AmyGwenWallAnalEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("AmyGwenWallAnalCumSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("AmyGwenWallPussyCumSlowx") 
            
label AmyGwenWallPussyEndx:
mc "I'm about to flood your pussy, Gwen!"
gw "Go on, dump your nut inside me and then PLASTER my back with the rest, I need some skin lotion!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
hide gwenwallpussycumfast
hide gwenwallanalcumslow
hide gwenwallpussycumslow
hide gwenwallanalcumfast
if gwenwallanalcumx == False and gwenwallpussycumx == False:
    show gwenwallpussy05
    show gwenwallcumpussy01nocum
    with fastdissolve
    mc "You asked for it! RHAAA!!!"
    gw "Oooh, your cock get even MORE MASSIVE with every POWERFUL jet of boygoo!"
    mc "Hang on Gwen, I've got some more cum lotion for your skin!"
    if persistent.cumsoundon:
        play sound "Sounds/cumming.mp3"
    hide gwenwallcumpussy01nocum
    hide gwenwallpussy05
    show gwenwallcumpussy02
    with fastdissolve
if gwenwallanalcumx or gwenwallpussycumx:
    show gwenwallpussycum05
    show gwenwallcumpussy01
    with fastdissolve
    mc "You asked for it! RHAAA!!!"
    gw "Oooh, your cock get even MORE MASSIVE with every POWERFUL jet of boygoo!"
    am "I can see it being propelled out of your pussy, Gwen!"
    mc "Hang on Gwen, I've got some more cum lotion for your skin!"
    if persistent.cumsoundon:
        play sound "Sounds/cumming.mp3"
    hide gwenwallcumpussy01
    hide gwenwallpussycum05
    show gwenwallcumpussy02
    with fastdissolve
gw "Oh my God, you've totally COVERED my back in your never-ending pellets."
$ gwenwallpussycumx = True
if gwenwallanalcumx:
    hide gwenwallcumpussy02
    show gwenwallcumanal03
    with fastdissolve    
    stop sound
    mc "Your holes have actually DRAINED me. temporarily of course. Get cleaned up and hop on the bed!"
    am "I'll help you lick it off!"
    scene bedroom03b blurred
    show amygwenbed01
    with dissolve
    gw "I don't even know how you can still be hard after this MARATHON romp!"
    am "But we'll gladly continue servicing your SEX PILLAR!"
    $ gwenwallpussycumx = False
    $ gwenwallanalcumx = False
    jump AmyGwenFuckChoicex
if gwenwallanalcum == False:
    hide gwenwallcumpussy02
    show gwenwallcumanal03
    with fastdissolve    
    mc "I ain't done with you, still need to cum inside that enticing rosebud of yours..."
    am "Oh my God, he's gonna fuck you SOME MORE!"
    hide gwenwallcumanal03
    play music "Sounds/womansex01.mp3"
    jump AmyGwenWallAnalCumSlowx

label AmyGwenWallAnalEndx:
mc "I'm about to flood your backdoor, Gwen!"
gw "YES! Give me a cum enema and then PLASTER the rest of my back!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
hide gwenwallpussyfast
hide gwenwallanalfast
hide gwenwallanalslow
hide gwenwallpussyslow
hide gwenwallpussycumfast
hide gwenwallanalcumslow
hide gwenwallpussycumslow
hide gwenwallanalcumfast
if gwenwallpussycumx == False and gwenwallanalcumx == False:
    show gwenwallanal05
    show gwenwallcumanal01nocum
    with fastdissolve
    mc "You asked for it! RHAAA!!!"
    gw "Oooh, your cock get even MORE MASSIVE with every POWERFUL jet of boygoo!"
    mc "Hang on Gwen, I've got some more cum lotion for your skin!"
    if persistent.cumsoundon:
        play sound "Sounds/cumming.mp3"
    hide gwenwallcumanal01nocum
    hide gwenwallanal05
    show gwenwallcumanal02
    with fastdissolve
if gwenwallpussycumx or gwenwallanalcumx:
    show gwenwallanalcum05
    show gwenwallcumanal01
    with fastdissolve
    mc "You asked for it! RHAAA!!!"
    gw "Oooh, your cock get even MORE MASSIVE with every POWERFUL jet of boygoo!"
    am "I can see it being propelled out of your ass, Gwen!"
    mc "Hang on Gwen, I've got some more cum lotion for your skin!"
    if persistent.cumsoundon:
        play sound "Sounds/cumming.mp3"
    hide gwenwallcumanal01
    hide gwenwallanalcum05
    show gwenwallcumanal02
    with fastdissolve
gw "Oh my God, you've totally COVERED my back in your never-ending pellets."
$ gwenwallanalcumx = True
if gwenwallpussycumx:
    hide gwenwallcumanal02
    show gwenwallcumanal03
    with fastdissolve    
    stop sound
    mc "Your holes have actually DRAINED me. temporarily of course. Get cleaned up and hop on the bed!"
    am "I'll help you lick it off!"
    scene bedroom03b blurred
    show amygwenbed01
    with dissolve
    gw "I don't even know how you can still be hard after this MARATHON romp!"
    am "But we'll gladly continue servicing your SEX PILLAR!"
    $ gwenwallpussycumx = False
    $ gwenwallanalcumx = False
    jump AmyGwenFuckChoicex
if gwenwallpussycumx == False:
    hide gwenwallcumanal02
    show gwenwallcumanal03
    with fastdissolve    
    mc "I ain't done with you, still need to cum inside that enticing fuckhole of yours..."
    am "Oh my God, he's gonna fuck you SOME MORE!"
    hide gwenwallcumanal03
    play music "Sounds/fucksound.mp3"
    jump AmyGwenWallPussyCumSlowx
    
label AmyGwenMissionaryx:
scene bedroom34 with dissolve
show amyprefuck01
am "You're gonna FUCK ME with your massive rod [name]?"
mc "Yeah, that's what you want isn't it?"
scene bedroom30 with fastdissolve
show amyprefuck02
am "Now you're just teasing me with your apple-sized helmet... Please, just SHOVE IT IN!"
mc "Alright, your pussy is slick enough with my precum, HERE WE GO!"
scene bedroom17 blurred
play music "Sounds/fucksound.mp3"
label AmyGwenMissionarySlowx:
hide amymissionaryfast
hide amycockslow
hide amycockfast
scene bedroom17 blurred
show amymissionaryslow
call screen amygwenpoundslow01x
screen amygwenpoundslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyGwenMissionaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AmyGwenMissionaryFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("AmyGwenCockSlowx") 

label AmyGwenCockSlowx:
hide amymissionaryslow
hide amymissionaryfast
hide amycockfast
scene bedroom03b blurred
show amycockslow
call screen amygwencockslow01x
screen amygwencockslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyGwenMissionaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AmyGwenCockFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AmyGwenMissionarySlowx") 

label AmyGwenMissionaryFastx:
hide amymissionaryslow
hide amycockslow
hide amycockfast
scene bedroom17 blurred
show amymissionaryfast
call screen amygwenpoundfast01x
screen amygwenpoundfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyGwenMissionaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AmyGwenMissionarySlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("AmyGwenCockFastx") 

label AmyGwenCockFastx:
hide amymissionaryslow
hide amymissionaryfast
hide amycockslow
scene bedroom03b blurred
show amycockfast
call screen amygwencockfast01x
screen amygwencockfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyGwenMissionaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("AmyGwenCockSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AmyGwenMissionaryFastx") 
            
label AmyGwenMissionaryEndx:
mc "I'm about to blow my nut Amy!"
am "FLOOD MY PUSSY with your virile spunk, [name]!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene bedroom03b blurred
show amyfuckcum01 with fastdissolve
mc "Gonna fill you up to OVERFLOODING! RHAAA!!!"
am "Keep pumping that load, I'm cumming with you, AAAH! I can feel each of your MASSIVE CUM-RUPTIONS! Oooh, it's ssoo good!"
mc "Hang on Amy, I've got some more sauce for your hot bod!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
scene bedroom12 blurred
show amyfuckcum02
with dissolve
am "Damn, you cumshots are so STRONG!"
mc "I'm repainting your body in white! AAH!"
scene bedroom14 blurred
show amyfuckcum03
with dissolve
mc "That's the last of it... PHEW!"
am "You covered me in TONS of cum... Mmmh, and I just LOVE slurping up those thick globs of semen! I hope you have some MORE for me! *wink*"
mc "Oh, you want MORE? i've got MORE for you, Amy! I'm on a roll and I'm gonna FUCK YOU SIDEWAYS till you're begging for me to stop!"
scene bedroom11
show amyfuckcum04
with dissolve
am "Really? You can fuck me again straight after cumming, STUD?"
mc "You'd better believe it!"
am "Oh, I DO believe it. Come on, stick your still ROCK-HARD MONSTER back in and FUCK ME, [name]!"
scene bedroom09 blurred with dissolve
play music "Sounds/womansex01.mp3"
label AmyGwenSideSlowx:
hide amysidefast
show amysideslow
call screen amygwensideslow01x
screen amygwensideslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyGwenSideEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AmyGwenSideFastx") 

label AmyGwenSideFastx:
mc "Do you feel how DEEP I am inside you? I'm gonna POUND you faster now!"
am "AAAh, you're such a fucking BEAST, [name]! Do it, fuck me harder and faster!"
hide amysideslow
show amysidefast
call screen amygwensidefast01x
screen amygwensidefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyGwenSideEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AmyGwenSideSlowx") 

label AmyGwenSideEndx:
mc "I'm gonna FLOOD your pussy AGAIN!"
scene bedroom28 blurred
show amysidecum01 with fastdissolve
stop music
play sound "v07/creampie.mp3"
am "How can you come So MUCH, you're the BEST harem master ever! AAAH, YES, keep going, MORE, MORE POWERFUL BLASTS OF SEMEN FOR ME!"
mc "Fuck Yeah! I'm can't stop cumming inside your tender snatch, it's gripping my spurting shaft like a VICE! RHAAA!"
am "Please! *puff* Try and pull out, I want to DROWN in your hot white scum!"
hide amysidecum01
show amysidecum02
mc "Alright, here goes! MORE MEGA-SHOTS OF SPUNK FOR YOU AMY! AAAH!"
am "Oh my God, you're cumming like a FOUNTAIN, ther's sssooo much sweet cream.... Mmmmh!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
hide amysidecum02
show amysidecum03
mc "There you go, a few more blasts and we can move on to something else. Get cleaned up while I recover."
am "I LOVE your cum sssooo much, it shouldn't take too long! *wink*"
scene bedroom03b
show amygwenbed01
with dissolve
am "We're READY for some more HOT SEX. So, what do you have in store for us, big boy?"
jump AmyGwenFuckChoicex
    
    

jump GwenGallery
