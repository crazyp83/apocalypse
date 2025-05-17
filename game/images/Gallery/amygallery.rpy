label AmyGallery:
call screen galleryamy
screen galleryamy:
    add "Gallery/amygallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("galleryamy"), Jump ("MainGallery")]

    imagebutton:
        focus_mask True
        idle "Gallery/gallerynextpage.png"
        hover "Gallery/gallerynextpage.png"
        action [Hide ("galleryamy"), Jump ("AmyGalleryb")]

    if renpy.seen_image("amypool01"):
        imagebutton:
            focus_mask True
            idle "Gallery/amygallery01.png" xpos 621 ypos 100
            hover "Gallery/amygallery01.png"
            action Jump ("Amygallery01")

    if renpy.seen_image("amypool01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("AmyGallery")

    if renpy.seen_image("dreamamy01"):
        imagebutton:
            focus_mask True
            idle "Gallery/amygallery02.png" xpos 1050 ypos 100
            hover "Gallery/amygallery02.png"
            action Jump ("Amygallery02")

    if renpy.seen_image("dreamamy01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("AmyGallery")

    if renpy.seen_image("amycanyon01"):
        imagebutton:
            focus_mask True
            idle "Gallery/amygallery03.png" xpos 1478 ypos 100
            hover "Gallery/amygallery03.png"
            action Jump ("Amygallery03")

    if renpy.seen_image("amycanyon01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("AmyGallery")

    if renpy.seen_image("amystrip01"):
        imagebutton:
            focus_mask True
            idle "Gallery/amygallery04.png" xpos 621 ypos 400
            hover "Gallery/amygallery04.png"
            action Jump ("Amygallery04")

    if renpy.seen_image("amystrip01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("AmyGallery")

    if renpy.seen_image("amygwenstrip01"):
        imagebutton:
            focus_mask True
            idle "Gallery/amygallery05.png" xpos 1050 ypos 400
            hover "Gallery/amygallery05.png"
            action Jump ("Amygallery05")

    if renpy.seen_image("amygwenstrip01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("AmyGallery")

    if renpy.seen_image("fightamywin"):
        imagebutton:
            focus_mask True
            idle "Gallery/amygallery06.png" xpos 1478 ypos 400
            hover "Gallery/amygallery06.png"
            action Jump ("Amygallery06")

    if renpy.seen_image("fightamywin") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("AmyGallery")

    if renpy.seen_image("mcamybedroom01"):
        imagebutton:
            focus_mask True
            idle "Gallery/amygallery07.png" xpos 621 ypos 700
            hover "Gallery/amygallery07.png"
            action Jump ("Amygallery07")

    if renpy.seen_image("mcamybedroom01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("AmyGallery")

    if renpy.seen_image("amyqueen01"):
        imagebutton:
            focus_mask True
            idle "Gallery/amygallery08.png" xpos 1050 ypos 700
            hover "Gallery/amygallery08.png"
            action Jump ("Amygallery08")

    if renpy.seen_image("amyqueen01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("AmyGallery")
            
    if renpy.seen_image("amybedroombed"):
        imagebutton:
            focus_mask True
            idle "Gallery/amygallery09.png" xpos 1478 ypos 700
            hover "Gallery/amygallery09.png"
            action Jump ("Amygallery09")

    if renpy.seen_image("amybedroombed") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("AmyGallery")

    add "Gallery/gallerygrid02.png"
    add "Gallery/textamy.png"
   
label AmyGalleryb:
call screen galleryamyb
screen galleryamyb:
    add "Gallery/amygallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("galleryamyb"), Jump ("MainGallery")]

    imagebutton:
        focus_mask True
        idle "Gallery/gallerynextpage.png"
        hover "Gallery/gallerynextpage.png"
        action [Hide ("galleryamyb"), Jump ("AmyGallery")]

    if renpy.seen_image("mcamypool01"):
        imagebutton:
            focus_mask True
            idle "Gallery/amygallery10.png" xpos 621 ypos 100
            hover "Gallery/amygallery10.png"
            action Jump ("Amygallery10")

    if renpy.seen_image("mcamypool01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("AmyGalleryb")

    add "Gallery/galleryfuture.png" xpos 1050 ypos 100

    add "Gallery/galleryfuture.png" xpos 1478 ypos 100

    add "Gallery/galleryfuture.png" xpos 621 ypos 400

    add "Gallery/galleryfuture.png" xpos 1050 ypos 400

    add "Gallery/galleryfuture.png" xpos 1478 ypos 400

    add "Gallery/galleryfuture.png" xpos 620 ypos 700

    add "Gallery/galleryfuture.png" xpos 1048 ypos 700

    add "Gallery/galleryfuture.png" xpos 1478 ypos 700

    add "Gallery/gallerygrid02.png"
    add "Gallery/textamy02.png"

label Amygallery01:
scene pool04
show amypool01
mc "Amy sure has a fine ass..."
play sound "Sounds/wolfwhistle.mp3"
hide amypool01
show amypool02
with dissolve
am "Is it for my ass or my muscles?"
mc "Your muscles."
am "I'm glad you're an admirer of female muscles, most guys are taken aback by them..."
am "Now watch this..."
hide amypool02
show amypool05
with fastdissolve
am "Aaaar."
mc "NICE."
hide amypool05
show amypool02
with fastdissolve
am "That's enough for now [name], I need to get back to the workshop. See you later!"
jump AmyGallery

label Amygallery02:
play sound "Sounds/dream.mp3"
scene classdream
show dreamamy01
play music "Sounds/showerstrip.mp3"
am "Do you like what I'm wearing [name]?"
hide dreamamy01
show dreamamy02
with fastdissolve
am "It's so comfortable. I LOVE natural cotton and how it hugs my ass curves, right?"
mc "Oooh yeah!"
hide dreamamy02
show dreamamy03
with fastdissolve
am "Of course, it's even better when I'm half naked... Letting the warm breeze flow over my hardening nipples..."
mc "The breeze is good. The breeze is good."
hide dreamamy03
show dreamamy04
with fastdissolve
am "And when it flows between my thighs and tickles my clit... I get so HORNY!"
mc "Praise the Breeze!"
hide dreamamy04
show dreamamy05
with fastdissolve
am "And I bet you're horny and hard already, right? I've got just the thing to make you even harder and BIGGER!"
am "So pull those pants down and show me your fuckpole, I'm going to PUMP IT UP!"
mc "Praise the Pump!"
hide dreamamy05
show dreamamy06
with fastdissolve
am "There, I think it fits perfectly over your megadong. It's the XXXXL version of course..."
am "Now let's PUMP!"
hide dreamamy06
show dreamamy07
with fastdissolve
am "Look at it! It's already getting FATTER! I'm going to pump it until you FILL IT UP!"
hide dreamamy07
show dreamamy08
with fastdissolve
am "Almost there... It's becoming monstrously HUGE! I want your fat shaft to reach the TIP!"
mc "Damn, it feels GOOOOOD!"
hide dreamamy08
show dreamamy09
with fastdissolve
am "I think you're ALL PUMPED UP now! Look at that BEHEMOTH of a cock! It makes my mouth salivate."
mc "Maybe it's time to pull the pump off Amy? Cos I feel like I'm about to cum..."
am "You're right, let's see that DONKEY-DICK up close so it can unload a MONSTER LOAD all over me!"
hide dreamamy09
show dreamamy10
with fastdissolve
am "My God, it's sooo HUGE!... And leaking TONS of precum! Come for me [name], let it all OUT!"
mc "Yes, Amy, I'm about to..."
hide dreamamy10
show dreamamy11
with fastdissolve
mc "...UNLEASH! RHAAA!"
am "YES! BLAST THAT VIRILE CREAM! COVER ME FROM HEAD TO TOE IN YOUR WARM SPUNK!"
hide dreamamy11
show dreamamy12
with fastdissolve
mc "Phew... I'm done. Plastering your body."
am "And plaster it you did! I cannot thank you enough for providing me with this vital natural energy, [name]!"
mc "You're welcome."
stop music
jump AmyGallery    

label Amygallery03:
play music "v07/datemusic.mp3"
scene canyon01
show amydate01
am "Thanks for bringing me here on our... date. It's a very romantic place [name]."
mc "Yes, I knew you would love it since you are like... in tune with Mother Nature and all that."    
am "That's right... And all that as you say..."
hide amydate01
show amydate02
with fastdissolve
am "So is this where you take all the girls [name]? *wink*"
mc "Only the most beautiful ones like you Amy..."
hide amydate02
show amydate03
with fastdissolve
am "*blush* Well, thank you... Let's move on into the water and see how pure it is."
scene canyon02
show amydate04
with dissolve
am "I feel like swimming a bit in that crystal clear water... \"Au naturel\"."
mc "Err.. meaning?"
am "I see all those lessons still haven't made you any better at French... It means NAKED. Care to join me?"
mc "Oui! Ooh la la!"
am "lol, you're such a funny dorky... stud."
scene amycanyon01 with dissolve
play music "Sounds/pool.mp3"
am "Mmh, the water is so refreshing... You should take a plunge [name], you'll see what I mean!"
scene amycanyon02 with dissolve
stop music
mc "Indeed, the view is much more interesting from down below..."
scene amycanyon03 with dissolve
am "But I'm getting almost too cold, I'll go and stand in the sun for a bit..."
scene amycanyon04 with dissolve
am "Here, in the sun, it's much warmer..."
mc "I can help you warm up Amy..."
scene amycanyon05 with dissolve
am "Oh yeah? And how do you plan to do that exactly [name]?"
mc "Body heat. And I'll protect you from the scorching sunshine too..."
am "Well come over here my valiant knight in... naked armor."
scene amycanyon06 with dissolve
am "And now kiss me..."
scene amycanyon07 with dissolve
scene amycanyon08 with dissolve
am "Let's keep this date... romantic. And not indulge your growing boyhood... Even if it is HUGE and demanding...."
mc "OK, I don't want to rush you in any way. I mean, there's the stairway to heavens to climb, right?"
am "That's right, and I AM your heaven! So let's go back to the compound, I need to finish fitting some exhaust pipe on a rig. See you later [name]!"
mc "(That went fast from romantic to not-romantic-at-all...)"
stop music
jump AmyGallery    

label Amygallery04:
scene strip01
show stripamy01
am "Oh, hello [name]... You finally decided to come and see me \"in the flesh\"..."
mc "In the flesh, I can see the soul better."
am "How deep of you."
mc "Yeah, I can go pretty deep..."
am "So what would you like me to do so you can relax that tension tonight?"
mc "I'll take the striptease session with just you please."
am "Sit back and enjoy the show..."
play music "Sounds/stripmusic.mp3"
scene amystriplarge with dissolve:
        ypos -3.0
        linear 10.0 ypos 0.0
$ renpy.pause(10.0, hard=True)
am "Ready?"
mc "Fuck yeah!"
scene amystrip01 with dissolve
pause        
scene amystrip02 with dissolve
pause
scene amystrip03 with dissolve
pause        
scene amystrip04 with dissolve
pause
scene amystrip05 with dissolve
pause        
scene amystrip06 with dissolve
pause
scene amystrip07 with dissolve
pause        
scene amystrip08 with dissolve
pause
scene amystrip09 with dissolve
pause        
scene amystrip10 with dissolve
pause
stop music
scene strip01
show stripamy04 with fastdissolve
am "That's it, time to cough up the money [name]..."
mc "Sure, sure, let me fondle inside my pockets... Ahem, oh, what's that I feel?"
am "Give it up, I ain't playing with your dong, just pay up!"
mc "Right, right..."
jump AmyGallery

label Amygallery05:
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
jump AmyGallery

label Amygallery06:
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
scene amyup07
play sound "Sounds/punch.mp3"
$ renpy.pause(.5, hard=True)
ma "She's fighting back with a nasty face punch!"
$ counting = 0
while counting < 20:
    $ ayla_health -= 0.1
    $ counting += 1
    pause 0.01
ma "That will cause a huge health loss to Ayla for sure..."
scene fightsetup with dissolve
show aylasetup at midright
show amysetup at midleft
$ renpy.pause(1, hard=True)
show aylasetup at center with move
ma "Ayla makes a move..."
scene fightayla01 with fastdissolve
ma "She looks mighty angry!"
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
scene amyup06 with dissolve
show pussygrab:
    xalign 0.4
    yalign 0.6       
$ counting = 0
while counting < 20:
    $ ayla_health -= 0.05
    $ counting += 1
    pause 0.01    
ma "And Amy crushes Ayla's tiny head with her strong pelvic muscles. Ayla cannot recover from such a lethal move..."
window hide
play sound "Sounds/winner.mp3"
scene fightamywin with dissolve
show winnersign at streetfight02
$ renpy.pause(1, hard=True)
ma "Amy wins tonight's fight!"    
play music "Sounds/applause.mp3"
$ renpy.pause(1, hard=True)
hide screen screenfightamyayla
stop music
jump AmyGallery

label Amygallery07:
scene bedroom01
show amy01
am "Hi [name]? You called for me? I hope it's for a HOT night of SEX and PASSION!"
mc "And cum all over the place, don't forget the cum all over the place."
am "And what should I wear tonight for YOU, [name]?"
mc "What you wear when going to bed will do just fine..."
hide amy01
show amy02
with fastdissolve
am "Alright, I'll get into my bedtime clothes then... Wait for me, I'll be back in a second. *wink*"
mc "Oh, I'll wait don't worry, I'll wait."
play music "v07/datemusic.mp3"
scene bedroom01 with fade
show amylingerie01 at center with moveinright
am "It might look like a pyjama, but it's still sexy enough for some HOT action."
mc "Especially when it's going to be off you!"
hide amylingerie01
show amylingerie02
with fastdissolve
am "But don't you want to see how it hugs my ass cheeks first?"
mc "Sure, sure, Amy. I'm getting a boner right now thinking about it."
hide amylingerie02
show amylingerie03
with fastdissolve
am "You're the ROMANTIC type I see... So, do you like what you see, Mr Boner?"
mc "Mr Boner is nodding in approval!"
scene bedroom01 blurred
hide amylingerie03
show amylingerie04
with fastdissolve
am "Then let me slowly peel off my top for him..."
hide amylingerie04
show amylingerie05
with fastdissolve
am "And now the bottom..."
mc "You're a tease Amy!"
hide amylingerie05
show amylingerie06
with fastdissolve
am "And now I'm naked. But you're not yet. So come over and show me YOUR muscular bod [name]..."
scene mcamybedroom01 with fastdissolve
am "God, your bulge is so MASSIVE!"
mc "I'm not even hard yet Amy..."
am "Really, so it can get even BIGGER? Let me see if I can entice your cock to GROW then!"
scene mcamybedroom02 with fastdissolve
mc "Fuck, that did it, Amy, you made me horny as hell! Get on the bed and I'm going to fuck you all night long!"
am "Then come and pound it NOW!"
stop music
jump AmyGallery

label Amygallery08:
scene bedroom01
show amy01
am "Hi [name]? You called for me? I hope it's for a HOT night of SEX and PASSION!"
mc "And cum all over the place, don't forget the cum all over the place."
am "And what should I wear tonight for YOU, [name]?"
hide amy01
show amy02
with fastdissolve
am "You're in luck, cos I've got the NON-VIRTUAL version! Wait for me, I'll be back in a second. *wink*"
mc "Oh, I'll wait don't worry, I'll wait. On my personal sofa."
play music "v07/datemusic.mp3"
scene bedroom02 blurred with fade
show amyqueen01 at center with moveinright
am "I only wear this on SPECIAL occasions you know..."
mc "And what's the special occasion then?"
hide amyqueen01
show amyqueen02
with fastdissolve
am "Tonight's special occasion is that it's the night I'm going to get FUCKED and POUNDED by a giant fuckstick!"
mc "You got that right, Amy! And you've got the bod made for HEAVY SEX."
hide amyqueen02
show amyqueen03
with fastdissolve
am "Oh yeah, you think so? Look at my biceps, pretty neat hey?"
mc "Very neat. It means you have enough wrist power to handle a thick truncheon like mine for HOURS."
am "I'll give you the best handjob you ever had. If..."
scene bedroom02 blurred
show amyqueen04
with fastdissolve
am "...you don't leave my fine ass dry before the night is over..."
mc "I would never do that, that would be rude indeed. I'll sodomize you good and proper, just like any gentleman would do."
scene bedroom02
show amyqueen05
with fastdissolve
am "I'm glad to hear that, because I'm a sizequeen-asswhore. I just LOOOVE anal."
mc "I shall gladly partake in your sexual fetish."
hide amyqueen05
show amyqueen06
with fastdissolve
am "Another fetish of mine is MUSCLES. You've seen mine. Now let me see YOURS!"
mc "Alright! Let's switch, you get on the sofa and I get my posing pouch for you..."
scene mcamybedroom01 with fastdissolve
am "I see Mr Boner is getting VERY BIG indeed! But not quite ROCK-HARD enough yet... maybe I should do something about it."
scene mcamybedroom02 with fastdissolve
mc "Of fuck, that ARSE! Mr Boner can't wait to pound that sweet ass of yours..."
am "Then come and pound it NOW!"
scene mcamybedroom03 with fastdissolve
am "Oh, FUCK! You've just RAMMED your log into my tight asshole! But it feels GOOD. Now you can just PUMP MY ARSE PLEASE!"
mc "You really are a sizequeen-asswhore. Alright, I'll give you what you want."
scene mcamybedroom04 with fastdissolve
am "AAAH, It's in ALL THE WAY now! So deep! I'm cumming on your fucking ass-destroying MONSTERCOCK!"
mc "Yeah, cream all over it, it'll make it even easier for me..."
scene mcamybedroom03 with fastdissolve
pause 0.2
scene mcamybedroom04 with fastdissolve
pause 0.2
scene mcamybedroom03 with fastdissolve
pause 0.2
scene mcamybedroom04 with fastdissolve
pause 0.2
scene mcamybedroom03 with fastdissolve
pause 0.2
scene mcamybedroom04 with fastdissolve
pause 0.2
scene mcamybedroom03 with fastdissolve
pause 0.2
scene mcamybedroom04 with fastdissolve
pause 0.2
scene mcamybedroom03 with fastdissolve
pause 0.2
scene mcamybedroom04 with fastdissolve
pause 0.2
scene mcamybedroom03 with fastdissolve
pause 0.2
scene mcamybedroom04 with fastdissolve
pause 0.2
scene mcamybedroom03 with fastdissolve
pause 0.2
scene mcamybedroom04 with fastdissolve
pause 0.2
mc "Damn, your ass is ssoo good, I'm gonna pump a load already!"
scene mcamybedroom05 with fastdissolve
play sound "v07/creampie.mp3"
am "Yeah, just FLOOD my ass with your cum!"
scene mcamybedroom06 with fastdissolve
mc "FUCK YEAH!"
am "Shit, you're cumming like a stallion. Don't empty your balls, [name], we're just getting STARTED!"
mc "Don't worry Amy, I've got plenty more cum in store for you. Let's move to the bed and I'll show you..."
stop sound
stop music
jump AmyGallery

label Amygallery09:
scene bedroom03b blurred
show amybedroombed
am "Alright, so what do you have planned for us for our all-night fuck session then?"
label AmyFuckChoicex:
stop music
menu:
    "I'm on a mission to make your pussy mine!":
        am "So, \"missionary\", I take it?"
        mc "That's right. You got the joke, you're good, Amy."
        jump AmyMissionaryx
    "Prepare for lift-off and open your mouth wide, Amy!":
        am "Ooh, you're going to lift me up in your strong arms and skull-fuck me? I can't wait for THAT!"
        jump AmyLiftx
    "I wouldn't mind letting YOU do all the work. By jerking me off.":
        am "With BOTH hands, I'll make you cum FASTER!"
        jump AmyHandjobx
    "Your puckered butthole looks enticing. Let's go there. Where no man has gone before.":
        am "You're a Star Trek nerd too? Probe my black hole, then!"
        jump AmyAnalx
    "Mother Nature demands more children. So I need to impregnate you." if renpy.seen_image("amykegel02"):
        am "I'm still young but... YES, I want to have your baby!"
        jump AmyImpregnationx
    "I'm done with this gallery.":
        jump AmyGallery

label AmyLiftx:
scene bedroom13
show amyprelift00
with dissolve
mc "Mmmh, that pussy is nice and wet..."
am "It's wet cos I can't wait to feel that MONSTER DONG down my throat!"
mc "First, I'm going to show you how powerful it is. Open your thighs and let me slide it through..."
scene bedroom35
show amyprelift01
with dissolve
am "What??? Oh my God, you're LIFTING me up with it? It's ssooo POWERFUL!"
play sound "Sounds/kiss.mp3"
mc "A true alpha-stud cock for you, Amy..."
scene bedroom13 blurred
show amyprelift02
with dissolve
am "Being handled like a rag doll by a male specimen such as yourself makes me so... horny."
scene bedroom33 blurred
show amyprelift03
play sound "Sounds/kiss.mp3"
$ renpy.pause(1.0, hard=True)
am "Do you like the taste of my lips [name]?"
mc "I sure do. And I feel my cock would also like the taste of your lips..."
am "Then turn me upside down, romantic boy, and I'll show you what they can do to that fat rod of yours..."
scene bedroom13 blurred with dissolve
play music "Sounds/hardsucking.mp3"
label AmyLiftSlowx:
hide amyliftfast
show amyliftslow
call screen amyliftslow01x
screen amyliftslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyLiftEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AmyLiftFastx") 

label AmyLiftFastx:
mc "Prepare to have my fat cock shoved down your throat even FASTER, Amy!"
hide amyliftslow
show amyliftfast
call screen amyliftfast01x
screen amyliftfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyLiftEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AmyLiftSlowx") 

label AmyLiftEndx:
mc "Get ready for a mouthful and a half, Amy!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
hide amyliftslow
hide amyliftfast
show amyliftcum01
with fastdissolve
mc "Open your throat wider, there's a lot more powerblasting to come! RHAAA!"
with fastflash
am "Gllrruuurrrbbb!"
hide amyliftcum01
show amyliftcum02
with fastdissolve
mc "Damn, I'm nutting directly into your stomach, I hope you're still getting a good taste of my chunky cum!"
scene bedroom36
show amyliftcum03
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Oh wow, that was an INTENSE blowjob, Amy."
am "I didn't even know my mouth could open WIDE enough for that arm-thick anaconda of yours.... The dev must have really boosted my mouth morphs to achieve that."
mc "Clean your face up and let's move to some more sexy fun."
am "Oooh, more?"
jump AmyFuckChoicex
    
label AmyMissionaryx:
scene bedroom34 with dissolve
show amyprefuck01
am "You're gonna FUCK ME with your massive rod [name]?"
mc "Yeah, that's what you want isn't it?"
scene bedroom30 with fastdissolve
show amyprefuck02
am "Now you're just teasing me with your apple-sized helmet... Please, just SHOVE IT ON!"
mc "Alright, your pussy is slick enough with my precum, HERE WE GO!"
scene bedroom17 blurred
play music "Sounds/fucksound.mp3"
label AmyMissionarySlowx:
scene bedroom17 blurred
show amymissionaryslow
call screen amypoundslow01x
screen amypoundslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyMissionaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AmyMissionaryFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("AmyCockSlowx") 

label AmyCockSlowx:
scene bedroom03b blurred
show amycockslow
call screen amycockslow01x
screen amycockslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyMissionaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AmyCockFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AmyMissionarySlowx") 

label AmyMissionaryFastx:
scene bedroom17 blurred
show amymissionaryfast
call screen amypoundfast01x
screen amypoundfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyMissionaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AmyMissionarySlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("AmyCockFastx") 

label AmyCockFastx:
scene bedroom03b blurred
show amycockfast
call screen amycockfast01x
screen amycockfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyMissionaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("AmyCockSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AmyMissionaryFastx") 
            
label AmyMissionaryEndx:
mc "I'm about to blow my nut Amy!"
am "FLOOD MY PUSSY with your virile spunk, [name]!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene bedroom03b blurred
show amyfuckcum01 with fastdissolve
mc "Gonna fill you up to OVERFLOODING! RHAAA!!!"
am "Keep pumping that load, I'm cumming with you, AAAH! I can feel each of your MASSIVE CUM-RUPTIONS! Oooh, it's ssoo good!"
with fastflash
mc "Hang on Amy, I've got some more sauce for your hot bod!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
scene bedroom12 blurred
show amyfuckcum02
am "Damn, you cumshots are so STRONG!"
mc "I'm repainting your body in white! AAH!"
scene bedroom14 blurred
show amyfuckcum03
mc "That's the last of it... PHEW!"
am "You covered me in TONS of cum... Mmmh, and I just LOVE slurping up those thick globs of semen! I hope you have some MORE for me! *wink*"
mc "Oh, you want MORE? i've got MORE for you, Amy! I'm on a roll and I'm gonna FUCK YOU SIDEWAYS till you're begging for me to stop!"
hide amyfuckcum03
show amyfuckcum04
am "Really? You can fuck me again straight after cumming, STUD?"
mc "You'd better believe it!"
am "Oh, I DO believe it. Come on, stick your still ROCK-HARD MONSTER back in and FUCK ME, [name]!"
scene bedroom09 blurred with dissolve
play music "Sounds/womansex01.mp3"
label AmySideSlowx:
hide amysidefast
show amysideslow
call screen amysideslow01x
screen amysideslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmySideEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AmySideFastx") 

label AmySideFastx:
mc "Do you feel how DEEP I am inside you? I'm gonna POUND you faster now!"
am "AAAh, you're such a fucking BEAST, [name]! Do it, fuck me harder and faster!"
hide amysideslow
show amysidefast
call screen amysidefast01x
screen amysidefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmySideEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AmySideSlowx") 

label AmySideEndx:
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
jump AmyFuckChoicex
    
label AmyHandjobx:
scene bedroom16 blurred
show amyprehandjob01
with dissolve
am "I've never seen a dong as MASSIVE as yours. Either you were hung like a horse to start with, or your crotch was exposed to a LOT of alpha-radiations."
mc "Let's just say I had a head-start when it happened..."
scene bedroom03b blurred
show amyprehandjob02
with fastdissolve
am "Oh yeah? That's why you're so experienced then... You were already banging MILF pussies as a pre-teen stud I bet. And all the HOT girls at school, right?"
mc "Oh God, you're such a dirty talker... Just wank me already, just like all those size-queens I had back then!"
scene bedroom16 blurred with dissolve
play music "Sounds/wank.mp3"
label AmyHanddSlowx:
hide amyhandfast
show amyhandslow
call screen amyhandslow01x
screen amyhandslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyHandEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AmyHandFastx") 

label AmyHandFastx:
am "It takes a while to make a BEAST like that cum, I'm going to have to increase the tempo to bring you over the EDGE!"
mc "AAAH, sssooo goood...."
hide amyhandslow
show amyhandfast
call screen amyhandfast01x
screen amyhandfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyHandEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AmyHanddSlowx") 

label AmyHandEndx:
am "That's it, I can feel your beast RUMBLE. The spermtube is expanding and..."
scene bedroom17
show amyhandjobcum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...Thar she blows!"
am "Damn it, you're such a tease! RHAAA!"
hide amyhandjobcum01
show amyhandjobcum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
am "I think you deserve some sperm ON YOU! I'll aim your cum-cannon a little bit LOWER..."
scene bedroom34 blurred
show amyhandjobcum03
am "That's it, you've COVERED your bedsheet and your musculed pecs with your warm cream.... Does it feel good [name]? I bet it does... I wanna taste it too, you know..."
mc "Of fuck, I'm spent... Hang on, NO, I can KEEP ON GOING ALL NIGHT LONG!"
am "Oh my, and how shall we continue making that BEAST explode over and over again?"
jump AmyFuckChoicex
    
label AmyAnalx:
scene bedroom09 with dissolve
show amypreanal01
am "Don't go warp speed on me to begin with, I need to adjust to your cum-pole..."
mc "I'll be gentle, don't worry."
scene bedroom12 blurred with dissolve
play music "Sounds/fucksound.mp3"
label AmyAnalSlowx:
hide amyanalfast
show amyanalslow
call screen amyanalslow01x
screen amyanalslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AmyAnalFastx") 

label AmyAnalFastx:
am "Go on, get on the OTHER side of that black hole! Backstab FASTER!"
hide amyanalslow
show amyanalfast
call screen amyanalfast01x
screen amyanalfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AmyAnalSlowx") 

label AmyAnalEndx:
am "Now turn it into a white hole with your cream, [name]!"
mc "FUCK YEAH! I will, just about...."
scene bedroom14 blurred
show amyanalcum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...NOW! RHAAAA!"
am "OOOh, my bowels are EXPLODING with cum! AAAH! Please pull out, I feel like I'm past breaking point [name]!!!"
hide amyanalcum01
show amyanalcum02
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "As you wish, Captain! Take those shots on your back then! AAAH!"
am "Mmmh, yes, it's so hot and so thick!"
scene bedroom32 blurred
show amyanalcum03
am "I can feel OUNCES of your cum on my back.... It's so warm and filthy... Just like me."
mc "Yes, you're a naughty girl for sure, Amy. But I'm an even naughtier BOY, so let's move on to something else!"
am "And what do you have in mind this time, NAUGHTY BOY?"
jump AmyFuckChoicex

label AmyImpregnationx:
scene bedroom20
show amykegel02 with dissolve
am "Let me prep myself then. I'll do some kegel exercises to make sure my ovaries are ready to receive your most virile sperms as they swim towards them."
mc "Err... Yeah, that's a bit too much anantomical detail... But I'll watch."
hide amykegel02
show amykegel01 
with fastdissolve
play sound "Sounds/moaning02.mp3"
am "Yeah, that's good, I can feel my pelvic muscles relaxing..."
window hide
hide amykegel01
show amykegel02 
with fastdissolve
play sound "Sounds/panting.mp3"
pause 1.0
stop sound
hide amykegel02
show amykegel01 
with fastdissolve
play sound "Sounds/moaning02.mp3"
pause 1.0
hide amykegel01
show amykegel02 
with fastdissolve
play sound "Sounds/panting.mp3"
pause 1.0
stop sound
hide amykegel02
show amykegel01 
with fastdissolve
play sound "Sounds/moaning02.mp3"
pause 1.0
hide amykegel01
show amykegel02 
with fastdissolve
play sound "Sounds/panting.mp3"
pause 1.0
stop sound
hide amykegel02
show amykegel03 
with fastdissolve
am "I think I'm nicely relaxed now... You can shove your cumstick in me."
mc "Let me check..."
scene bedroom14 blurred
show amykegel04
with dissolve
play sound "Sounds/moaning.mp3"
mc "Yeah, I think you're ready indeed... Let's DO IT!"

play music "Sounds/womansex02.mp3"
label AmyPregnantSlowx:
hide amypregnantfast
hide amypregnantsceneslow
hide amypregnantscenefast
scene bedroom17 blurred
show amypregnantslow
call screen amypregnantslow01x
screen amypregnantslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyPregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AmyPregnantFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AmyImpregnateSlowx") 

label AmyImpregnateSlowx:
hide amypregnantslow
hide amypregnantfast
hide amypregnantscenefast
scene bedroom06 blurred
show amypregnantsceneslow
call screen amypregnantsceneslow01x
screen amypregnantsceneslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyPregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AmyImpregnateFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("AmyPregnantSlowx") 

label AmyPregnantFastx:
hide amypregnantslow
hide amypregnantsceneslow
hide amypregnantscenefast
scene bedroom17 blurred
show amypregnantfast
call screen amypregnantfast01x
screen amypregnantfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyPregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AmyPregnantSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AmyImpregnateFastx") 

label AmyImpregnateFastx:
hide amypregnantslow
hide amypregnantfast
hide amypregnantsceneslow
scene bedroom06 blurred
show amypregnantscenefast
call screen amypregnantscenefast01x
screen amypregnantscenefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AmyPregnantEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("AmyImpregnateSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("AmyPregnantFastx") 
            
label AmyPregnantEndx:
stop music
scene bedroom20 blurred
show amypregnantcum01
with dissolve
play music "Sounds/splooge02.mp3"
am "Yes, pump your virile cream inside my womb, AAAH!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
with fastflash
mc "I AM, RHAAA!"
scene bedroom29 blurred
show amypregnantcum02
with dissolve
stop music
play sound "Sounds/splooge01.mp3"
am "My belly is SWELLING, PULL OUT OR I'LL BURST!"
with fastflash
mc "What? Oh yeah, sorry, I'm cumming ssooo much!"
stop music
hide amypregnantcum02
show amypregnantcum03
with dissolve
play sound "Sounds/gasp.mp3"
am "Goddamit, how can you hold that much cum? There's like a GALLON of SPUNK swimming inside me!"
play sound "Sounds/panting.mp3"
mc "Just making sure you'll get pregnant, that's all... But I'm totally drained now."
am "Let's go to bed then and let Mother Nature take its course..."
jump AmyGallery

label Amygallery10:
scene pool04
show amypool01
mc "Amy sure has a fine ass..."
hide amypool01
show amypool03
am "Yes?"    
mc "Let's compare muscles. Just for the heck of it."
hide amypool03
show amypool02
with fastdissolve
am "Alright! Let's see what you've got..."
window hide
show amypool02 at right with move
show mcmompool10 at left with moveinleft
mc "Fuck yeah, my muscles are all pumped up in anticipation..."
hide mcmompool10
hide amypool02
show mcamypool01
with dissolve
am "I'll start..."
play sound "Sounds/womangroan.mp3"
mc "Nice biceps flexing there, Amy, I can really see the definition..."
scene pool04 blurred
show mcamypool02
with dissolve
mc "My turn..."
play sound "Sounds/mcworkout.mp3"
mc "What do you think of THOSE biceps?"
am "Wow! They're so... fucking HUGE!"
am "Now flex them with me with your hands above your head!"
scene pool04
show mcamypool03
with dissolve
play sound "Sounds/womangroan.mp3"
mc "ALRIGHT!"
am "We're like two muscle FREAKS! Well, especially YOU! Can I touch them?"
mc "Of course, I'll flex my right bicep as BIG as possible for you Amy..."        
hide mcamypool03
show mcamypool04
with dissolve
mc "Like that..."
play sound "Sounds/mcworkout.mp3"
am "Damn [name]! Your bicep must be AT LEAST 25 inches around in that state!"
mc "Even more Amy..."
am "You're making me... all dizzy..."
scene pool05 blurred
show mcamypool05
with dissolve
mc "Then feel those triceps too!"
am "Everything in you is like HARDENED STEEL!"
mc "Yeah, pretty much. ROCKHARD STEEL you might even say!"
scene pool04 blurred
show mcamypool06
with dissolve
am "You're really a naughty boy... But a naughty MUSCLE STUD BOY, so you can get away with it..."
am "And also, please take your hand off my tit, I need to go back to the workshop."
mc "Ah.. Yeah, alright. I'll go for a swim then... See you around, Amy!"
am "See you, ROCKHARD STUD!"
jump AmyGalleryb