label MelaniaGallery:
call screen gallerymelania
screen gallerymelania:
    add "Gallery/melaniagallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("gallerymelania"), Jump ("MainGallery")]

    if renpy.seen_image("melania01"):
        imagebutton:
            focus_mask True
            idle "Gallery/melaniagallery01.png" xpos 621 ypos 100
            hover "Gallery/melaniagallery01.png"
            action Jump ("MelaniaGallery01")

    if renpy.seen_image("melania01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("MelaniaGallery")

    if renpy.seen_image("melania04"):
        imagebutton:
            focus_mask True
            idle "Gallery/melaniagallery02.png" xpos 1050 ypos 100
            hover "Gallery/melaniagallery02.png"
            action Jump ("MelaniaGallery02")

    if renpy.seen_image("melania04") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("MelaniaGallery")

    if renpy.seen_image("melania08"):
        imagebutton:
            focus_mask True
            idle "Gallery/melaniagallery03.png" xpos 1478 ypos 100
            hover "Gallery/melaniagallery03.png"
            action Jump ("MelaniaGallery03")

    if renpy.seen_image("melania08") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("MelaniaGallery")

    if renpy.seen_image("ivankamelania01"):
        imagebutton:
            focus_mask True
            idle "Gallery/ivankagallery04.png" xpos 621 ypos 400
            hover "Gallery/ivankagallery04.png"
            action Jump ("MelaniaGallery04")

    if renpy.seen_image("ivankamelania01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("MelaniaGallery")

    if renpy.seen_image("melaniaivanka01"):
        imagebutton:
            focus_mask True
            idle "Gallery/melaniagallery04.png" xpos 1050 ypos 400
            hover "Gallery/melaniagallery04.png"
            action Jump ("MelaniaGallery05")

    if renpy.seen_image("melaniaivanka01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("MelaniaGallery")

    if renpy.seen_image("maragogo01"):
        imagebutton:
            focus_mask True
            idle "Gallery/melaniagallery06.png" xpos 1478 ypos 400
            hover "Gallery/melaniagallery06.png"
            action Jump ("MelaniaGallery06")

    if renpy.seen_image("maragogo01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("MelaniaGallery")

    if renpy.seen_image("melaniawhitehouse"):
        imagebutton:
            focus_mask True
            idle "Gallery/melaniagallery07.png" xpos 621 ypos 700
            hover "Gallery/melaniagallery07.png"
            action Jump ("MelaniaGallery07")

    if renpy.seen_image("melaniawhitehouse") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("MelaniaGallery")

    if renpy.seen_image("whbothend01"):
        imagebutton:
            focus_mask True
            idle "Gallery/whitehousegallery02.png" xpos 1050 ypos 700
            hover "Gallery/whitehousegallery02.png"
            action Jump ("MelaniaGallery08")

    if renpy.seen_image("whbothend01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("MelaniaGallery")

    if renpy.seen_image("newovaloffice01"):
        imagebutton:
            focus_mask True
            idle "Gallery/whitehousegallery03.png" xpos 1478 ypos 700
            hover "Gallery/whitehousegallery03.png"
            action Jump ("MelaniaGallery09")

    if renpy.seen_image("newovaloffice01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("MelaniaGallery")

    add "Gallery/gallerygrid02.png"
    add "Gallery/textmelania.png"
        

label MelaniaGallery01:
scene melania01
show whitehouseframe
me "Hello [name]. Don't be alarmed, this is just a friendly call..."
me "From me, the First Lady, The Mother of Patriots..."
scene melania02 with dissolve
show whitehouseframe
me "I was told that you... are not happy with my husband? Don't listen to the fake media, the president only wants to make us all Great!"
play sound "Sounds/melania01.mp3"
window hide
pause 2
me "I have... a new therapy for you. To make you feel better. To make you feel GREAT!"
scene melania03 with dissolve
show whitehouseframe
me "So don't try and be a hero. And see what you could get if you decide to stop your desire for vengeance..."
me "The First Pussy of the First Lady awaits you... Don't be a hero, be best, and come and grab this GREAT pussy..."
stop sound
hide whitehouseframe
jump MelaniaGallery

label MelaniaGallery02:
scene melania04
show whitehouseframe
me "So, have you thought about my offer?"
me "Maybe, I can show you some more to help you make up your mind..."
scene melania05 with dissolve
show whitehouseframe
me "What would you look like to see... My great big new fake boobies? Or my tight First Pussy?"
scene melania06 with dissolve
show whitehouseframe
me "I'll show you both to prove to you that I mean BUSINESS... And if YOU also mean business, you know it's time to stop hating my husband. Time to join him to become GREAT!"
scene melania07 with dissolve
show whitehouseframe
me "I'm waiting for you... In the Supreme White House. Come and find me STUD, and this pussy will be ALL YOURS!"
hide whitehouseframe
jump MelaniaGallery

label MelaniaGallery03:
scene melania08
show whitehouseframe
if mctrumpster <= 3:
    me "I think you might need some more enticing to BE BEST."
    me "So I took my top off...  I hope that will bring you to the dar... I mean, the TRUMPF side."
if mctrumpster == 5:
    me "I think you need a reward for being such a loyal subject to the Trumpf Imperial Nepotic Family."
    me "So I took my top off...  And I will show you MUCH MORE, dear uneducated MNAGAt!"
scene melania09 with dissolve
show whitehouseframe
me "See my big new tits? Custom alpha-radiated to be perfectly round, youthful and soft to the touch..."
me "A perfect target for your superior seed!"
scene melania10 with dissolve
show whitehouseframe
me "What about my SUPREME WHITE PUSSY? It's GREAT because it can take in GREAT things! And many people say that YOU have a HUGE thing."
scene melania11 with dissolve
show whitehouseframe
me "I'll show you exactly what I mean... Watch how that monster black dildo, which by the way definitely proves that I am NOT racist, can plunge into my FIRST PUSSY!"
me "So come and replace that nigg.. sorry, black cock with your SUPREME white cock and come and FUCK me in the SUPREME WHITE HOUSE! I'm waiting for you!"
hide whitehouseframe
jump MelaniaGallery

label MelaniaGallery04:
scene melaniaivanka01
show whitehouseframe
me "Mmh, I'm feeling so HORNY today... But our President-for-Life is too busy making New America GREAT AGAIN."
me "Fortunately, his daughter isn't so busy, since she's just a senior adviser with no clear duties... Maybe I should call her, what do you think [name]?"
scene melaniaivanka02 with dissolve
show whitehouseframe
iv "Here I am! Ready for some SPECIAL FAMILY TIME!"
me "I bet you already have your HUGE cock out and ready to fap [name], right? My pussy is sssoo wet too..."
iv "We're not letting you into our private sex life for no reason [name]..."
me "We need you to PROMISE us that you'll be a good boy and abandon your vendetta against my hubby."
iv "And we'll show you what you can get in return..."
scene melaniaivanka03 with dissolve
show whitehouseframe
play sound "Sounds/kiss.mp3"
iv "I LOVE your tongue on mine Melania... Mmmmh..."
me "My daughter-in-law is such a NAUGHTY girl! For YOU!"
scene melaniaivanka04 with dissolve
show whitehouseframe
iv "And I love even more GRINDING my pussy against yours!"
me "Ooh, I'm sure [name] LOVES watching us being BEST!"
iv "I want you to PUMP MY PUSSY UP! It needs to be GIGANTIC to fit his ENORMOUS BOYCOCK!"
me "Ooh, that's a good idea Ivanka! And I have just the tool for that..."
scene melaniaivanka05 with dissolve
show whitehouseframe
play sound "Sounds/moaning.mp3"
me "See that [name]? Her pussy is SWELLING UP, ready to take on your GIANT PUSSY-PLEASER!"
iv "Oh yes, my clit is so fucking HUGE now, keep PUMPING IT Melania!"    
scene melaniaivanka06 with dissolve
show whitehouseframe
me "I just have to taste this MEGA-PUSSY now..."
iv "Yeah, rub your tongue all over my swollen pussy lips... And slurp up all my copious sex juices, God, I'm just so fucking HORNY!"
me "*lick* Mmmh, sssooo tasty, I wish you were here to savour my daughter-in-law's DELICIOUS cunt with me [name]!"
iv "Now it's my turn to return the favor Melania..."
scene melaniaivanka07 with dissolve
show whitehouseframe
me "Oh my God, I'm squirting, your tongue is so good Ivanka!"
iv "I hope you're CUMMING a MONSTERLOAD too, [name]!"
me "I imagine that his BEAST must be EXPLODING!"
scene melaniaivanka08 with dissolve
show whitehouseframe
me "I hope you enjoyed our little display of family bonding..."
if mctrumpster <= 4:
    iv "You could be part of it too, you know that, right? All you have to do is join the Trumpf syndic... I meant FAMILY!"
if mctrumpster == 5 and bounty == False:
    iv "And since you're already a Trumpster, we'll make sure to treat you like FAMILY when you come and bang us with your SUPERIOR FUCKSTICK!"
    me "We'll be waiting... Our pussies all swollen and READY to take you on, STUD!"
hide whitehouseframe
jump MelaniaGallery

label MelaniaGallery05:
scene ivankamelania01
show whitehouseframe
iv "Oh, hello [name]. You've caught us in an intimate position. My SLAVE is busy licking my pussy."
scene ivankamelania02 with dissolve
show whitehouseframe
iv "That's right, I can DOMINATE any woman I want, even the First Lady, and make them worship my SUPERIOR body!"
me "Yes, Ivanka, you are ssoo POWERFUL! So much more powerful than [name]..."
iv "What do you have to say about that? Melania seems to think you're nothing but a WIMP after all! Cos you STILL haven't FUCKED HER!"
scene ivankamelania03 with dissolve
show whitehouseframe
iv "And now it's time to give my mother-in-law what she's craving for. A BIG THICK DILDO!"
me "Ooh, Ivanka, give me what [name] REFUSES to give me! I want it DEEP in my creamy FIRST CUNT!"
scene ivankamelania04 with dissolve
show whitehouseframe
iv "There you go Melania, take it hard! See how I'm pounding her into oblivion [name]! Would you like to be in MY PLACE?"
play sound "Sounds/moaning.mp3"
me "I'm sure he would, but he still hasn't UNDERSTOOD what it means to be a part of the FAMILY... AAAh, I'm cumming AGAIN!"
scene ivankamelania05 with dissolve
show whitehouseframe
iv "So be reasonable and stop being DEPLORABLE! Or you might end up on the WRONG end of THIS stick!"
if bounty:
    iv "And maybe when a bounty hunter brings you back to me, I will treat you the same way. So be warned!"    
hide whitehouseframe
jump MelaniaGallery

label MelaniaGallery06:
scene maragogo03
show mcgogo01
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
label MelaniaHandSlowx:
hide melaniahandfast
show melaniahandslow
call screen melaniahandslow01x
screen melaniahandslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MelaniaHandEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MelaniaHandFastx") 

label MelaniaHandFastx:
me "Not there yet? Maybe if I go a little bit faster..."
hide melaniahandslow
show melaniahandfast
call screen melaniahandfast01x
screen melaniahandfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MelaniaHandEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MelaniaHandSlowx") 

label MelaniaHandEndx:
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
bh "You're in for an exhausting night. In the hands of two sex-crazed succubi..."
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
label MaragogoSlowx:
hide melaniabounceslow
hide melaniabouncefast
hide bountythreesomefast
scene maragogo04b
show bountythreesomeslow
call screen bountythreesomeslow01x
screen bountythreesomeslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MaragogoEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MaragogoFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("MaragogoPOVSlowx") 
        
label MaragogoPOVSlowx:
hide bountythreesomeslow
hide bountythreesomefast
hide melaniabouncefast
scene maragogo06 blurred
show melaniabounceslow
call screen melaniabounceslow01x
screen melaniabounceslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MaragogoEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MaragogoPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MaragogoSlowx") 

label MaragogoPOVFastx:
me "You didn't think I could take ALL of your donkey-dick inside me did you? Now watch me ride you EVEN FASTER!"
hide bountythreesomeslow
hide bountythreesomefast
hide melaniabounceslow
scene maragogo06 blurred
show melaniabouncefast
call screen melaniabouncefast01x
screen melaniabouncefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MaragogoEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MaragogoPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MaragogoFastx") 

label MaragogoFastx:
me "Oh, this dick is so LONG and FAT, my tits are bouncing all over the place while I'm riding this STUD!"
hide bountythreesomeslow
hide melaniabounceslow
hide melaniabouncefast
scene maragogo04b
show bountythreesomefast
call screen bountythreesomefast01x
screen bountythreesomefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MaragogoEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MaragogoSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("MaragogoPOVFastx") 

label MaragogoEndx:
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
play sound "Sounds/cumming.mp3"
me "Oh My Bestness, you DO cum A LOT!"
bh "Wow, Melania, he's totally COATED your tits in his spunk and he's STILL GOING STRONG! We've got ourselves a true STALLION CUM-MACHINE here!"
me "I know how to pick my boys Kelly!"
hide melaniabouncecum03
show melaniabouncecum04
mc "AAAH, You've.... drained me..."
bh "I don't think so. You still have one more pussy to fill up. MINE!"
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
label BountyBlowSlowx:
hide bountybjfast
show bountybjslow
call screen bountyblowslow01x
screen bountyblowslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BountyBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BountyBlowFastx") 

label BountyBlowFastx:
mc "Oh FUCK! She's DEVOURING my knob!"
me "Go on, deepthroat him even FASTER so he blow his load, Kelly!"
hide bountybjslow
show bountybjfast
call screen bountyblowfast01xb
screen bountyblowfast01xb:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BountyBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BountyBlowSlowx") 

label BountyBlowEndx:
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
label BountyAnaSlowbxb:
hide bountyfast
show bountyslow
call screen bountyanalslow01bxb
screen bountyanalslow01bxb:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BountyAnalEndbxb")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BountyAnalFastbxb") 

label BountyAnalFastbxb:
bh "Holy FUCK! It's so HUGE and DEEP inside me!"
mc "I'll fuck you faster to really SHOW you!"
hide bountyslow
show bountyfast
call screen bountyanalfast01bxb
screen bountyanalfast01bxb:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BountyAnalEndbxb")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BountyAnaSlowbxb") 

label BountyAnalEndbxb:
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
jump MelaniaGallery

label MelaniaGallery07:
scene melaniawhitehouse
show melania20
show whitehouseframe
me "Hello again [name]... How was your special time with me in Mar-a-Gogo?"
window hide
scene melaniawhitehouse blurred
show melania21
show whitehouseframe
with dissolve
me "I hope your harem girls aren't complaining that your balls are COMPLETELY DRAINED!"
me "You were quite defiant too, if I remember well... As a member of the Super-Elite, it is my duty to show you what happens to those who defy us... LOWER THE SLAVE!"
window hide
hide melania21
show melania22
with dissolve
play sound "v07/clunk.mp3"
me "Now, where did I put that strapon?"
window hide
hide melania22
show melania23
with dissolve        
me "Oh, do you recognize her now? She won't be serving free pizza anymore. But she'll be serving FREE ANUS to my Elite Super-Dong!"
so "MMmgglll. Mmmuuummpppffff."
me "Ah, there it is..."
window hide
hide melania23
show melania24
with dissolve
play sound "v07/chain.mp3"
me "She can't even talk, that's how we deal with LOUDMOUTHS! But soon, she'll BE BEST and she'll take my huge cock up her ass!"
so "NNNuuuu. Pgglleeeefff."
window hide
hide melania24
show melania25
with dissolve
me "There you go, milk ME this time, with your ass muscles!"
so "AAAAff... Nnnnurffff...."
hide melania25
show melaniasofiafuck
play music "Sounds/barbarasex.mp3"
call screen melaniasofiafuck01x
screen melaniasofiafuck01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MelaniaSofiaFuckEndx")
label MelaniaSofiaFuckEndx:
stop music
hide melaniasofiafuck
show melania28
show whitehouseframe
with dissolve
me "And now her ass is like a brand new freeway. That's how the Super-Elite deal with Infrastructure Week!"
me "So I hope you learnt your lesson [name] and that you won't cross me EVER AGAIN..."
jump MelaniaGallery

label MelaniaGallery08:
$ ivankaloadx = False
$ melaniadeepx = False
$ ivankadeepx = False
$  melanialoadx = False


scene ovaloffice02
show mcprewhfuck01
mc "See this? That's a schlong worthy of a REAL President!"
play sound "v08/wow.mp3"
me "Indeed... But how much Special Pizza Sauce can it deliver?"
iv "And how DEEP can it get into our pussies?"
hide mcprewhfuck01
show mcprewhfuck02
with dissolve
play sound "Sounds/lick.mp3"
mc "I'll show you soon enough. But first, I want a taste of those succulent nipples..."
scene ovaloffice02zoom blurred
show mcprewhfuck03
with dissolve
play sound "Sounds/slurp.mp3"
mc "Let me get a taste of your mommy-milk..."
iv "Oooh, but... That's normally reserved for my children..."
mc "Not anymore... I take what's MINE!"
iv "You're so forceful and... MANLY. Kiss me please..."
hide mcprewhfuck03
show mcprewhfuck04
with dissolve
play sound "Sounds/kiss.mp3"
me "Now that you're here, UNINVITED, with your massive cock all ROCKHARD and READY, why don't you show us some good times, [name]?"
mc "Of course First Lady... Get on all fours on the Oval Office carpet and I'll show you some GREAT times!"
scene whpredoggybackground
show whpredoggyanimslow
with dissolve
play music "Sounds/moaning02.mp3"
mc "Now that's better ladies. So, who will go first I wonder?"
menu:
    "Melania":
        mc "First Lady first..."
        jump MelaniaHouseFuckxb
    "Ivanka":
        mc "Muscles galore for my BIG MUSCLE first!"
        jump IvankaHouseFuckxb

label MelaniaHouseFuckxb:
stop music
scene whivankacumbackgroundzoom
show whmelaniaprefuck
with dissolve
mc "Ready First Lady?"
play sound "Sounds/moaning.mp3"
me "Mmmh, YES I AM!"
label MelaniaHouseFuckbxb:
stop music
play music "Sounds/womansex01.mp3"
scene whdoggymelaniabackground blurred
label MelaniaHouseSlowxb:
hide melaniawhdoggyfast
show melaniawhdoggyslow
call screen melaniawhfuckslow01xb
screen melaniawhfuckslow01xb:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("MelaniaHouseEndxb")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MelaniaHouseFastxb") 
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("IvankaHouseSwitchxb") 

label MelaniaHouseFastxb:
if melaniadeepx:
    mc "I'm the FIRST man that DEEP inside the First Lady! Fuck Yeah!"
if melaniadeepx == False:
    mc "You love that cock, don't you Melania?"
    me "YES, I LOVE IT, I admit it, just shut up and FUCK MY DIRTY HOLE HARDER!"
    $ melaniadeepx = True
hide melaniawhdoggyslow
show melaniawhdoggyfast
call screen melaniawhfuckfast01xb
screen melaniawhfuckfast01xb:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("MelaniaHouseEndxb")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MelaniaHouseSlowxb")
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("IvankaHouseSwitchxb") 
        
label MelaniaHouseEndxb:
me "DUMP your load inside my First Lady pussy [name]!"
stop music
play music "Sounds/splooge02.mp3"
scene whdoggymelaniabackground blurred
show whmelaniacum01
with dissolve
mc "You don't need to ask me twice, AAAAH"
window hide
with fastflash
me "Oh God, he's really FIRING his shots up my super-elite fuckhole!"
hide whmelaniacum01
show whmelaniacum02
with dissolve
play sound "Sounds/womanscream.ogg"
me "AAAH, sssoo sssoo DEEP, directly into my womb!"
window hide
with fastflash
mc "Damn right, RHAAAA!"
window hide
with fastflash
me "Pull out and DOUSE my back with your warm spunk!"
stop music
scene whmelaniacumbackground
show whmelaniacum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "There you go, massive ball-busting nutload coming your way, RHAAA!"
$ melanialoadx = True
window hide
with fastflash
iv "Oh fuck, I want some of that too... It looks so yummy..."
hide whmelaniacum03
show whmelaniacum04
with dissolve
play sound "Sounds/panting.mp3"
if ivankaloadx:
    mc "Then come and slurp it up Ivanka..."
    jump WhbothfuckEndxb
if ivankaloadx == False:
    mc "Don't you worry, I've got enough cum left for YOUR PUSSY!"
    iv "Please, fuck me, I'm dying to feel that GIANT shaft STRETCHING my hole..."
    jump IvankaHouseFuckxb

label IvankaHouseSwitchxb:
mc "Gonna switch before I cum inside that tight hole, aaah... Get ready Ivanka!"
jump IvankaHouseFuckbxb

label IvankaHouseFuckxb:
stop music
scene whivankacumbackgroundzoom
show whivankaprefuck
with dissolve
mc "Ready Ivanka?"
play sound "Sounds/moaning.mp3"
iv "Always ready for a big fat teenage MONSTERCOCK!"
label IvankaHouseFuckbxb:
stop music
play music "Sounds/womansex02.mp3"
label IvankaHouseSlowxb:
scene whdoggyivankabackground blurred
show ivankawhfuckslow
call screen ivankawhfuckslow01xb
screen ivankawhfuckslow01xb:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("IvankaHouseEndxb")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("IvankaHouseFastxb") 
    imagebutton:
        focus_mask True
        idle "v071/topview.png"
        hover "v071/topview.png"
        action Jump ("IvankaHouseTopSlowxb") 
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("MelaniaHouseSwitchxb") 
 
label IvankaHouseFastxb:
if ivankadeepx:
    mc "Gonna POUND that presidential-family fuckhole HARDER and FASTER!"
if ivankadeepx == False:
    mc "Am I DEEP enough inside your pussy Ivanka?"
    iv "Oooh, YES! But go faster please, fuck me HARD, make me CUM!"
    $ ivankadeepx = True
scene whdoggyivankabackground
show ivankawhfuckfast
call screen ivankawhfuckfast01xb
screen ivankawhfuckfast01xb:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("IvankaHouseEndxb")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("IvankaHouseSlowxb")
    imagebutton:
        focus_mask True
        idle "v071/topview.png"
        hover "v071/topview.png"
        action Jump ("IvankaHouseTopFastxb") 
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("MelaniaHouseSwitchxb") 

label IvankaHouseTopSlowxb:
scene whdoggyivankatopbackground
show ivankatopwhfuckslow
call screen ivankawhfucktopslow01xb
screen ivankawhfucktopslow01xb:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("IvankaHouseEndxb")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("IvankaHouseTopFastxb") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("IvankaHouseSlowxb") 
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("MelaniaHouseSwitchxb") 

label IvankaHouseTopFastxb:
if ivankadeepx:
    mc "Gonna POUND that presidential-family fuckhole HARDER and FASTER!"
if ivankadeepx == False:
    mc "Am I DEEP enough inside your pussy Ivanka?"
    iv "Oooh, YES! But go faster please, fuck me HARD, make me CUM!"
    $ ivankadeepx = True
scene whdoggyivankatopbackground
show ivankatopwhfuckfast
call screen ivankawhfucktopfast01xb
screen ivankawhfucktopfast01xb:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/cum.png"
        hover "Icons/cum.png"
        action Jump ("IvankaHouseEndxb")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("IvankaHouseTopSlowxb")
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("IvankaHouseFastxb") 
    imagebutton:
        focus_mask True
        idle "v10/switchgirl.png"
        hover "v10/switchgirl.png"
        action Jump ("MelaniaHouseSwitchxb") 

label IvankaHouseEndxb:
iv "Are you going to give me your fat load [name]?"
mc "* puff *  You want it? BEG FOR IT!"
iv "Ooohh, please, PLEASE, FLOOD MY FILTHY HOLE, IT'S YOURS!"
stop music
play music "Sounds/splooge02.mp3"
scene whdoggyivankabackground
show whivankacum01
with dissolve
mc "NUTTING INSIDE IVANKA TRUMPF, RHAAAA!"
window hide
with fastflash
iv "Uuuh, AAAAH, I'm coming too!"
stop music
scene whdoggyivankatopbackground
show whivankacum02
mc "There's MORE for you Ivanka, AAAAH!"
window hide
with fastflash
iv "Give it ALL to me, STALLION!"
stop music
scene whivankacumbackground blurred
show whivankacum03
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Take those shots on your amazon body, AAAH"
window hide
with fastflash
iv "CLAIM ME WITH YOUR SPERM, LIKE A TRUE ALPHA-MALE!"
play sound "Sounds/panting.mp3"
me "What about me? I'm the FIRST LADY and I should get priority for your SPECIAL PIZZA SAUCE!"
$ ivankaloadx = True
if melanialoadx:
    mc "Then come and have a taste yourself Melania..."
    iv "And I'll lick the cream off YOUR body too!"
    jump WhbothfuckEndxb
if melanialoadx == False:
    mc "Don't you worry, I've got enough cum left for YOUR PUSSY!"
    iv "Please, fuck me, I'm dying to feel that GIANT shaft STRETCHING my hole..."
    jump IvankaHouseFuckxb

label MelaniaHouseSwitchxb:
mc "Time to switch girls, this cock needs more than one pussy to make it come. Spread your legs wide open Melania!"
jump MelaniaHouseFuckbxb

label WhbothfuckEndxb:
scene whbothbackground blurred
show whbothend01
with dissolve
play sound "Sounds/lick.mp3"
mc "Oh fuck, watching you ladies going at each other is getting me HARD AGAIN!"
scene whbothbackgroundzoom
show whbothend02
with dissolve
play music "Sounds/footsteps.mp3"
me "Oh shit, I hear Donnie's footsteps. Quick, let's get dressed!"
stop music
jump MelaniaGallery

label MelaniaGallery09:
play channel1 "v10/ohyeah.mp3"
scene newovaloffice01
show mcwin01
mc "Fuck yeah!"
scene newovaloffice02
show mcwin02
with dissolve
mc "Before the FUCKING begins, my dev has instructed me to direct you to his Patreon page."
mc "If you're not yet a patron but enjoyed this now COMPLETED game, now is the time to join and leave a tip to show your appreciation."
hide mcwin02
show mcwin03
with fastdissolve
mc "So just click right THERE!..."
call screen endcredits
screen endcredits:
    modal True
    imagebutton idle "v10/epiclustpatreon.png" hover "v10/epiclustpatreon.png" xpos 1500 ypos 300 focus_mask True action OpenURL("https://www.patreon.com/epiclust")
    imagebutton idle "v10/epiclustpatreonnext.png" hover "v10/epiclustpatreonnext.png" xpos 1500 ypos 900 focus_mask True action Return
    
hide mcwin03
show mcwin04
with fastdissolve
mc "Now ladies, you're my Special SEX Advisors, so it's time to make the prez CUM!"
hide mcwin04
show mcwin05
with fastdissolve
play sound "Sounds/lick.mp3"
iv "Of course President [name]!"
me "We will make you cum as often as you like EVERY DAY from now on!"
stop music
play channel2 "Sounds/sucking.mp3"
scene melaniaivankablowbackground blurred
label MelaniaIvankaBlowSlowxb:
hide melaniaivankablowfast
show melaniaivankablowslow
call screen melaniaivankablowslow01xb
screen melaniaivankablowslow01xb:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MelaniaIvankaBlowEndxb")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MelaniaIvankaBlowFastxb") 

label MelaniaIvankaBlowFastxb:
hide melaniaivankablowslow
show melaniaivankablowfast
mc "You're getting my juices going, girls..."
me "We'll make them go FASTER then!"
call screen melaniaivankablowfast01xb
screen melaniaivankablowfast01xb:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MelaniaIvankaBlowEndxb")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MelaniaIvankaBlowSlowxb")

label MelaniaIvankaBlowEndxb:
iv "He's tensing up! The Prez is about to BLOW!"
mc "He sure is..."
hide melaniaivankablowslow
hide melaniaivankablowfast
show melaniaivankablowcum01
with dissolve
me "It's bubbling at the tip..."
window hide
with fastflash
mc "AAAH! I'm about to blow a big..."
stop channel2
hide melaniaivankablowcum01
show melaniaivankablowcum02
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "...ONE! RHAAA!"
window hide
with fastflash
mc "Fuck yeah, blowing my nut in the Oval Office!!!!"
play sound "Sounds/moaning02.mp3"
hide melaniaivankablowcum02
show melaniaivankablowcum03
with dissolve
me "Look at him DOUSE us with his warm teenage spunk!"
window hide
with fastflash
iv "I've never seen such THICK, CREAMY cumshots EVER! We're getting CAKED in it!"
window hide
with fastflash
mc "There's plenty more where that came from, ladies! But I need some reserves for the next scene..."
scene newovaloffice01
show melaniaivankablowcum04
with dissolve
play sound "Sounds/kiss.mp3"
mc "And now, BRING ON THE GIRLS FOR THE FINAL ORGY!"
stop channel1
jump MelaniaGallery


