label ExploreHex53:
if kristaentered:
    scene containerfar01
    show containerfar01b
    with fade
    play music "Sounds/desertwind01.mp3"
    mc "Derek and Krista and Angie are gone... I guess the only thing to do here is to try and enter Trumpf City through the West Gate."
    jump TrumpfWall01

if kristaentered == False:
    scene containerfar01 with fade
    play music "Sounds/desertwind01.mp3"
    if exploredhex53 and derekplantried:
        mc "Back at the refugee container park... I guess it's time to try Derek's plan again. Or try and enter Trumpf City without him by clicking on the wall in the distance for example..."
        jump ContainerBase
    if exploredhex53 and seedquest and seedbag:
        mc "Back at the refugee container park... I guess it's time to implement Derek's plan. Or try and enter Trumpf City without him by clicking on the wall in the distance for example..."
        jump ContainerBase
    if exploredhex53:
        mc "Back at the refugee container park... I guess I can either talk to these two hillbillies or try and enter Trumpf City without them by clicking on the wall in the distance for example..."
        jump ContainerBase
    if knowcity:
        mc "Well, that's a desolate place. I think I can see the walls of Trumpf City in the distance though, so I'm getting close to my goal."
        mc "And there are a bunch of people over there..."
    if knowcity == False:
        mc "Well, that's a desolate place. But there are a bunch of people over there." 
    
label ContainerBase:
hide screen mcstats
hide screen calendar
call screen container
screen container:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/exitidle.png"
        hover "Icons/exithover.png"
        action Jump ("LeaveContainer")
    imagebutton:
        focus_mask True
        idle "v08/wallidle.png"
        hover "v08/wallhover.png"
        action Jump ("TrumpWall")
    imagebutton:
        focus_mask True
        idle "v08/peopleidle.png"
        hover "v08/peoplehover.png"
        action Jump ("WhiteTrash")
    
label LeaveContainer:
mc "I don't know why, but I feel the urge. The urge to leave this God-forsaken place. Let's go back to the compound."
jump BackHex53

label TrumpWall:
"What appears to be a large portion of fortified wall. Paid for by the Mexicans. Or not."
menu:
    "Go to the Western Gate with Bella" if withbe and knowcity:
        mc "It's time to try and enter Trumpf City and I'll need your help Bella."
        be "My duty as a scout is to explore, not partake in your crazy objectives!"
        mc "Well, there's one hex we haven't explored yet. TRUMPF CITY. So you're coming with me, whether you like it or not!"
        jump TrumpfWall01
    "Go to the Western Gate with Penny" if withpe and knowcity:
        mc "It's time to try and enter Trumpf City and I'll need your help Penny."
        pe "Road Warriors don't meddle in political stuff."
        mc "You want Roads on which to be a Warrior? I promise to have an Infrastructure Week once I'm president."
        pe "I suppose.... It does sound like a great campaign promise..."
        mc "Then it is agreed. You help me kick Trumpf out of office and I'll build you the best, most beautiful roads you've ever seen, believe me!"
        jump TrumpfWall01
    "Go to the Western Gate alone" if knowcity:
        $ withbe = False
        $ withpe = False
        mc "It's time to try and enter Trumpf City and I'm the HERO to DO IT."
        jump TrumpfWall01
jump ContainerBase

label WhiteTrash:
show screen mcstats
show screen calendar
if persistent.tipson and angiereunited == False:
    show hex53tip at tips with dissolve
    pause
    hide hex53tip 
if withan:
    an "I'll stay behind if you don't mind. This place scares me..."
    if withpe or withbe:
        mc "Fine Angie, we'll keep an eye on you."
    if alone:
        mc "Fine Angie, I'll keep an eye on you."
scene container01
show krista01 at left
show derek01 at midright
with dissolve
if derekplanfail:
    dr "You again? We told ya to leave us alone! We're going inside Trumpf City on our own."
    hide derek01
    show derekspit at midright
    with fastdissolve
    play sound "v08/spitting.mp3"
    $ renpy.pause(0.5, hard=True)
    hide derekspit
    show derek01 at midright
    kr "He don't get it hun."
    mc "Fine, you do that, after all the money I spent on this bag of seeds! I'll find a way ot get inside. ON MY OWN."
    hide derek01
    show derek02 at midright
    with fastdissolve
    dr "He thinks we ain't good enough for 'im. I told ya!"
    hide krista01
    show krista02 at farleft
    with fastdissolve
    kr "Let's go back inside. I need another pack of cigarettes." 
    jump ExploreHex53
if derekplantried:
    mc "So, are we all ready to try the \"Plan\" again?"
    hide derek01
    show derek02 at midright
    with fastdissolve
    dr "He screwed up last time and now he wants to screw up again!"
    hide krista01
    show krista02 at farleft
    with fastdissolve
    kr "Let's try once more time hun. Give him a chance."
    hide derek02
    show derek01 at midright
    with fastdissolve
    dr "Good thing the cart is ready and Angie isn't at Turdshacks. I'll go and get her."
    window hide
    hide derek01 with moveoutright
    show angietrash04 with moveinright
    show cart with moveinright
    show derek01 at right with moveinright
    an "Are we going inside Trumpf City this time? Yipee!"
    hide krista02
    show krista01 at farleft
    with fastdissolve
    kr "I hope so. I'll get the babies and we can leave."
    jump TrumpfWallDerek
    
if seedquest and derekplanfail == False and seedbag:
    mc "So, I'm here, you're here, I presume the babies are here too if you haven't lost them. Time to make a move Derek!"
    hide derek01
    show derek02 at midright
    with fastdissolve
    dr "He's pressuring me again!"
    hide krista01
    show krista02 at farleft
    with fastdissolve
    kr "He's right hun, we need to get inside Trumpf City..."
    window hide
    hide derek02
    show derek03 at midright
    play sound "v08/gulp.mp3"
    dr "Fine, I'll get the cart and Angie, you get the little ones. And I'll grab me another can too."
    hide derek03
    hide krista02
    show krista01 at left
    show derek01 at midright
    with fastdissolve
    kr "You do that hun."
    hide derek01 with moveoutright
    jump KristaFuck
if exploredhex53:
    dr "You again? I told ya to leave us alone!"
    hide derek01
    show derekspit at midright
    with fastdissolve
    play sound "v08/spitting.mp3"
    $ renpy.pause(0.5, hard=True)
    hide derekspit
    show derek01 at midright
    kr "He don't get it hun."
    if withza:
        dr "Hang on..."
        hide derek01
        show derekangry at midright
        with fastdissolve
        dr "Is that an Islamo-Nucleorist with ya? She can fuck off back to Gitmo!"
        za "I REALLY don't like these people. Let's go back to the compound please, [name]."
        mc "Yeah, OK, just a min..."
        hide derekangry
        show derekspit at midright
        with fastdissolve
        play sound "v08/spitting.mp3"
        $ renpy.pause(0.5, hard=True)
        hide derekspit
        show derek03 at midright
        play sound "v08/gulp.mp3"
        za "I mean NOW!"
        mc "Alright, alright. I guess I shouldn't have brought you to this container park..."
        mc "I'll be back. Without her."
        hide krista01
        show krista02 at left
        with fastdissolve
        kr "Sure. Whatever."
        window hide
        hide derek03
        show derek01 at midright
        with fastdissolve    
        dr "Yeah, see ya dude."
        $ beenhex53 = True
        jump BackHex53b    
    jump WhiteTrashDialogue    
dr "Are you looking for trouble, dude?"
$ exploredhex53 = True
if alone and withnone:
    kr "Maybe he's a new refugee. Whatever."
if alone == False or withnone == False:
    kr "Maybe they're new refugees. Whatever."
dr "And we don't have no more room for no stinkin' refugees."
window hide
hide derek01
show derekspit at midright
with fastdissolve
play sound "v08/spitting.mp3"
$ renpy.pause(0.5, hard=True)
hide derekspit
show derek01 at midright
with fastdissolve
if withza:
    dr "Hang on..."
    hide derek01
    show derekangry at midright
    with fastdissolve
    dr "Is that an Islamo-Nucleorist with ya? She can fuck off back to Gitmo!"
    za "I REALLY don't like these people. Let's go back to the compound please, [name]."
    mc "Yeah, OK, just a min..."
    hide derekangry
    show derekspit at midright
    with fastdissolve
    play sound "v08/spitting.mp3"
    $ renpy.pause(0.5, hard=True)
    hide derekspit
    show derek03 at midright
    play sound "v08/gulp.mp3"
    za "I mean NOW!"
    mc "Alright, alright. I guess I shouldn't have brought you to this container park..."
    mc "I'll be back. Without her."
    hide krista01
    show krista02 at left
    with fastdissolve
    kr "Sure. Whatever."
    window hide
    hide derek03
    show derek01 at midright
    with fastdissolve    
    dr "Yeah, see ya dude."
    jump BackHex53
$ exploredhex53 = True
label WhiteTrashDialogue:
menu:
    "Hello to you too my dear friends! What a warm welcome!" if spoketrash01 == False:
        $ spoketrash01 = True
        hide derek01
        show derek02 at midright
        with fastdissolve
        dr "Is he fuckin' with us?"
        hide krista01
        show krista02 at left
        with fastdissolve
        kr "I don't know hun. He looks darn stoopid to me."
        hide derek02
        show derek01 at midright
        with fastdissolve 
        dr "Probably just another goddam refugee. There's no more room for you 'ere I told ya."
        window hide
        hide derek01
        show derekspit at midright
        with fastdissolve
        play sound "v08/spitting.mp3"
        $ renpy.pause(0.5, hard=True)
        hide derekspit
        show derek01 at midright
        with fastdissolve
        hide krista02
        show krista01 at left
        with fastdissolve
        kr "He could try Turdshacks. I hear they got some empty containers over there."
        jump WhiteTrashDialogue
    "I'm NOT a refugee." if spoketrash02 == False:
        $ spoketrash02 = True
        hide derek01
        show derekangry at midright
        with fastdissolve        
        dr "Then what are ya doin' 'ere? Either you barter or you fuck off and leave us alone!"
        window hide
        hide derekangry
        show derekspit at midright
        with fastdissolve
        play sound "v08/spitting.mp3"
        $ renpy.pause(0.5, hard=True)
        hide derekspit
        show derek01 at midright
        hide krista01
        show krista02 at left
        with fastdissolve        
        kr "He could try Turdshacks. I hear they don't mind non-refugees over there."
        hide krista02
        show krista01 at left
        with fastdissolve
        jump WhiteTrashDialogue        
    "I'm here to trade. If you have anything interesting to barter..." if spoketrash01 or spoketrash02:
        hide derek01
        show derek04 at midright
        with fastdissolve
        dr "Oh yeah? We trade too, don't we babe?"
        hide krista01
        show krista02 at left
        with fastdissolve
        kr "For sure hun. Anything than can get us into Trumpf City..."
        hide derek04
        show derek01 at midright
        with fastdissolve
        if boughtbaby == False:
            dr "Do you want a baby?"
            mc "A baby??? What?"
            hide derek01
            show derek03 at midright
            with fastdissolve
            play sound "v08/gulp.mp3"
            dr "Yeah, we got plenty of the darn kids. We can sell you the young' un, the missus popped it out just a couple of weeks ago."
            hide krista02
            show krista01 at left
            with fastdissolve
            kr "Came out of nowhere that one. Didn't feel a thing."
            hide derek03
            show derek05 at midright
            with fastdissolve
            dr "Also, don't know how it happened, but he's a bit dark. No good to us."
            kr "Too much sun. Fell on his head. Whatever."
            hide derek05
            show derek01 at midright
            with fastdissolve
            menu:
                "Buy the baby (-10$)" if money >= 10 and boughtbaby == False:
                    mc "Ok, I might need it for some strange reasons, I'll buy it."
                    $ money -= 10
                    call MCbabies
                    $ boughtbaby = True
                    hide derek01
                    show derek04 at midright
                    with fastdissolve
                    dr "One baby to go! Do you want it wrapped up?"
                    hide krista02
                    show krista01 at left
                    with fastdissolve                
                    kr "Give him a blanket hun. So he don't get cold on the way."
                    hide derek04
                    show derek01 at midright
                    with fastdissolve
                    dr "Well, I'm gonna grab me another can."
                    kr "You do that hun."
                    hide derek01 with moveoutright
                    jump KristaTalk                
                "Don't buy the baby":
                    mc "Thanks, but I'll pass."
                    hide derek01
                    show derek03 at midright
                    with fastdissolve
                    play sound "v08/gulp.mp3"
                    dr "The offer still holds, man. If you come back here."                      
                    hide derek03
                    show derek01 at midright
                    with fastdissolve
                    label DerekSkunk:
                    dr "What about a skunk? I got a dead one. Freshly skinned."
                    mc "And what the hell am I supposed to do with a skinned skunk?"
                    hide derek01
                    show derek04 at midright
                    with fastdissolve
                    dr "Well eat it, doh!"
                    mc "Yuck, no thanks, I prefer camel burgers. And salad."
                    hide derek04
                    show derek02 at midright
                    with fastdissolve
                    dr "Is he fuckin' with us?"
                    hide krista01
                    show krista02 at left
                    with fastdissolve
                    kr "I don't know hun. I guess he don't like skunk. How are we gonna get inside Trumpf City?"
                    hide derek02
                    show derek01 at midright
                    with fastdissolve
                    dr "Don't you worry, I got a plan."
                    window hide
                    hide derek01
                    show derek03 at midright
                    play sound "v08/gulp.mp3"
                    kr "I hope it's a good plan hun."
                    hide derek03
                    show derek01 at midright
                    with fastdissolve
                    dr "I'm gonna grab me another can."
                    hide krista02
                    show krista01 at left
                    with fastdissolve
                    kr "You do that hun."
                    hide derek01 with moveoutright
                    jump KristaTalk
        if boughtbaby:
            jump DerekSkunk
    "I'm trying to get inside Trumpf City. And you guys are in my way." if spoketrash04 == False and knowcity:
        $ spoketrash04 = True
        hide derek01
        show derek02 at midright
        with fastdissolve
        dr "Is he fuckin' with us?"
        hide krista01
        show krista02 at left
        with fastdissolve
        kr "I don't know hun, he looks like he means it."
        hide derek02
        show derekangry at midright
        with fastdissolve
        dr "You can't get in there without a PLAN. I got a plan. And you're not part of it."
        window hide
        hide derekangry
        show derek03 at midright
        play sound "v08/gulp.mp3"
        kr "I hope it's a good plan hun."
        hide derek03
        show derek01 at midright
        with fastdissolve
        dr "I'm gonna grab me another can."
        hide krista02
        show krista01 at left
        with fastdissolve
        kr "You do that hun."
        hide derek01 with moveoutright
        jump KristaTalk
    "Where's Angie? Is she okay?" if angiereunited:
        dr "She's over at Turdshacks gettin' some water from the well."
        hide krista01
        show krista02 at left
        with fastdissolve
        kr "That's how we lost her last time." 
        hide derek01
        show derek02 at midright
        with fastdissolve
        if babyangie:
            dr "Don't tell 'im that, he'll try and kidnap her to knock her up again!"
        if babyangie == False:
            dr "Don't tell 'im that, he'll try and kidnap her again!"
        hide krista02
        show krista01 at left
        with fastdissolve 
        kr "Well, you told him where she was hun."
        hide derek02
        show derek01 at midright
        with fastdissolve 
        dr "That was stoopid of me."
        jump WhiteTrashDialogue
    "So what's the plan, hey Derek?" if (spoketrash01 or spoketrash02) and angiereunited and seedquest == False:
        $ derekplan01 = True
        hide derek01
        show derek04 at midright
        with fastdissolve
        dr "What, you think I don't have a plan, man? I HAVE a plan!"
        hide krista01
        show krista02 at left
        with fastdissolve
        kr "Well let's hear it hun." 
        hide derek04
        show derek02 at midright
        with fastdissolve
        dr "You also think I don't have a plan! I'll tell you what my plan is!"
        mc "I'm all ears."
        hide krista02
        show krista01 at left
        with fastdissolve
        kr "So am I hun."
        hide derek02
        show derek01 at midright
        with fastdissolve
        dr "I wrote it down on a piece of paper. I'll go and fetch it. And grab a can."
        kr "Sure, you do that hun."
        hide derek01 with moveoutright
        jump KristaTalk
    "I've got a bag of salad seeds!" if seedquest and seedbag:
        hide derek01
        show derek04 at midright
        with fastdissolve
        dr "Well done, man! I didn't think you'd do it."
        hide krista01
        show krista02 at left
        with fastdissolve
        kr "So can we get into Trumpf City now hun?" 
        hide derek04
        show derek02 at midright
        with fastdissolve
        dr "Don't pressure me! I've got to think. About my next move."
        mc "I'm all ears."
        hide krista02
        show krista01 at left
        with fastdissolve
        kr "So am I hun."
        hide derek02
        show derek01 at midright
        with fastdissolve
        dr "I don't know yet. I guess we'll just have to wait until that goddamm vee-oh-point-nine..."
        hide krista01
        show krista02 at left
        with fastdissolve
        kr "* sigh* I knew it."
        mc "Well I guess I'll come back another time to talk about it then...."
        hide krista02
        hide derek01
        with dissolve
        jump BackHex53        
    "I'll be leaving. Considering the welcome here..." if spoketrash01 or spoketrash02:
        hide derek01
        show derek02 at midright
        with fastdissolve
        dr "He thinks we ain't good enough for 'im. I told ya."
        hide krista01
        show krista02 at left
        with fastdissolve
        kr "Let's go back inside. I need another pack of cigarettes." 
        hide krista02
        hide derek02
        with dissolve
        if beenhex53:
            jump BackHex53b            
        jump BackHex53

label KristaTalk:
if derekplan01 and lustkr >= 2:
    play channel1 "v07/datemusic.mp3"
    show krista01 at center with move
    kr "Stoopid's gone again. And I think he'll be quite a while..."
    mc "Ah, so you mean..."
    hide krista01
    show krista05
    with fastdissolve
    kr "You want to stick your pud between them mounds or not?"
    mc "Err, sure Krista!"
    hide krista05
    show krista06
    with fastdissolve
    kr "Well get naked hun, let's see what you got. I bet it's a big one, ain't it? I saw your bulge."
    play sound "Sounds/zipper.mp3"
    hide krista06
    show krista07
    with fastdissolve
    kr "Wow, it's a whopper! Never seen one that big on a white boy before."
    call LustPlusKrista
    hide krista07
    show kristapreballs01
    with fastdissolve
    kr "Look at that thing! So much bigger than Derek's..."
    mc "You like it I can tell, hey?"
    kr "Sure hun. Let me taste those fat bull-balls for starters..."
    play channel2 "Sounds/lick.mp3"
    scene containerkristatits
    show kristaballs    
    call screen kristaballsscreen01
    screen kristaballsscreen01:
        modal True
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("KristaBallsEnd")    
    label KristaBallsEnd:    
    mc "That's... enough, I need to fuck those big tits, Krista!"
    hide kristaballs
    stop channel2
    
    play channel2 "Sounds/wank.mp3"
    label KristaTitfuckSlow:
    hide kristatitsfast
    hide kristatitspovslow
    hide kristatitspovfast
    scene containerkristatits blurred
    show kristatitsslow
    call screen kristatitsslow01
    screen kristatitsslow01:
        modal True
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("KristaTitfuckEnd")
        imagebutton:
            focus_mask True
            idle "Icons/fasteridle.png"
            hover "Icons/fasterhover.png"
            action Jump ("KristaTitfuckFast") 
        imagebutton:
            focus_mask True
            idle "Icons/povview.png"
            hover "Icons/povview.png"
            action Jump ("KristaTitfuckPOVSlow") 

    label KristaTitfuckPOVSlow:
    hide kristatitsslow
    hide kristatitsfast
    hide kristatitspovfast
    scene containerkristatitspov blurred
    show kristatitspovslow
    call screen kristatitspovslow01
    screen kristatitspovslow01:
        modal True
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("KristaTitfuckEnd")
        imagebutton:
            focus_mask True
            idle "Icons/fasteridle.png"
            hover "Icons/fasterhover.png"
            action Jump ("KristaTitfuckPOVFast") 
        imagebutton:
            focus_mask True
            idle "Icons/sceneview.png"
            hover "Icons/sceneview.png"
            action Jump ("KristaTitfuckSlow") 

    label KristaTitfuckFast:
    if kristatitssaid == False:
        kr "Hurry up hun, Derek will come back soon..."
        $ kristatitssaid = True
    hide kristatitsslow
    hide kristatitspovslow
    hide kristatitspovfast
    scene containerkristatits blurred
    show kristatitsfast
    call screen kristatitsfast01
    screen kristatitsfast01:
        modal True
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("KristaTitfuckEnd")
        imagebutton:
            focus_mask True
            idle "Icons/sloweridle.png"
            hover "Icons/slowerhover.png"
            action Jump ("KristaTitfuckSlow") 
        imagebutton:
            focus_mask True
            idle "Icons/povview.png"
            hover "Icons/povview.png"
            action Jump ("KristaTitfuckPOVFast") 

    label KristaTitfuckPOVFast:
    if kristatitssaid == False:
        kr "Hurry up hun, Derek will come back soon..."
        $ kristatitssaid = True
    hide kristatitsslow
    hide kristatitsfast
    hide kristatitspovslow
    scene containerkristatitspov blurred
    show kristatitspovfast
    call screen kristatitspovfast01
    screen kristatitspovfast01:
        modal True
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("KristaTitfuckEnd")
        imagebutton:
            focus_mask True
            idle "Icons/sloweridle.png"
            hover "Icons/sloweridle.png"
            action Jump ("KristaTitfuckPOVSlow") 
        imagebutton:
            focus_mask True
            idle "Icons/sceneview.png"
            hover "Icons/sceneview.png"
            action Jump ("KristaTitfuckFast") 
                
    label KristaTitfuckEnd:
    kr "Now you dump a nice big fat load hun. Let's see what you got."
    mc "Your tits rubbing against my shaft... That's so good, I..."
    hide kristatitsslow
    hide kristatitspovslow
    hide kristatitspovfast
    hide kristatitsfast
    stop channel2
    scene containerkristatitspov blurred
    show kristatitscum01
    with dissolve
    mc "AAAAH!"
    if persistent.cumsoundon:
        play sound "Sounds/mccum.mp3"
    with fastflash
    kr "Keep going hun, I know you got more cream for me."
    scene containerkristatits blurred
    show kristatitscum02
    with dissolve
    if persistent.cumsoundon:
        play sound "Sounds/cumming.mp3"
    mc "Fuck yeah, HERE IT COMES!"
    window hide
    with fastflash
    kr "That's a LOT hun."
    hide kristatitscum02
    show kristatitscum03
    with dissolve
    if persistent.cumsoundon:
        play sound "Sounds/mccum.mp3"
    mc "Damn it, there's even MORE!"
    with fastflash
    kr "I ain't never seen no boy come that much hun."
    with fastflash
    scene containerkristatitszoom
    show kristatitscum04
    with dissolve
    stop sound
    mc "Phew... Shit, I think Derek is coming back..."
    kr "Don't you worry about that hun. Get dressed and I'll deal with him."
    stop channel1
    scene container01
    show krista06cum at left
    show derek05 at midright with moveinright
    with dissolve
    dr "What you're doing, babe?"
    kr "Nuffin. I was feeding the small one and he choked on my milk and spit it all out on me."
    hide derek05 
    show derek04 at midright
    with fastdissolve
    dr "You hear that? She's got too much milk in those big funbags of hers. Kids can't even keep up."
    hide derek04 
    show derek01 at midright
    with fastdissolve    
    dr "That way we don't have to buy no milk from Walmart. And I can spend my money on beer."
    hide krista06cum
    show krista01 at left
    with dissolve
    kr "I know hun."
    mc "So what's the plan, Derek?"
    hide derek01
    show derekcan at midright
    with dissolve
    play sound "v08/canopening.mp3"
    dr "I got some contact at the gate. They let through farmers with seeds. I got some fake papers."
    kr "We ain't got no seed hun."
    hide derekcan
    show derek02 at midright
    with dissolve
    dr "I know, but you wanted Mr smart-ass here to be part of the plan, so that's the plan!"
    hide derek02
    show derek01 at midright
    with dissolve
    dr "You gotta bring back some seeds dude. Preferably salad seeds. They need those at the moment."
    hide derek01
    show derek04 at midright
    with dissolve
    dr "Until vee-oh-point-nine they said!"
    window hide
    show missionseed at posmission
    $ renpy.pause(2.0, hard=True)
    hide missionseed
    $ seedquest = True
    mc "No worries, we have plenty of mutated salads back at the compound, I know the chick who takes care of them, won't be a problem!"
    if persistent.tipson:
        show derekplantip at tips with dissolve
        pause
        hide derekplantip
        mc "Or maybe it will..."
    hide krista01
    show krista02 at left
    with dissolve
    kr "Well, that's good to hear. Been waiting for so long to get into Trumpf City."
    hide derek04
    show derek03 at midright
    play sound "v08/gulp.mp3"    
    mc "I'll bid you farewell. And I'll come back with some seeds. For the PLAN."
    hide derek03
    show derek01 at midright
    dr "Yeah, see ya, man."  
    jump BackHex53c

if metkr:
    play music "v07/datemusic.mp3"
    show krista01 at center with move
    kr "Stoopid's gone again. You wanna fondle my tits?"
    mc "Err, yeah, sure, why not."
    hide krista01
    show krista06
    with fastdissolve
    kr "Well come and get 'em..."
    mc "Damn, you're really gonna do it? Again?"
    hide krista06
    show krista07
    with fastdissolve
    kr "I'm horny. And I'm leaking. Why don't ya come and suck some milk out of my funbags?"
    mc "Alright!"
    if withbe:
        be "Don't mind me, I still literally don't exist. *sigh*"
    if withpe:
        pe "Don't mind me, I still literally don't exist. *sigh*" 
    jump KristaAgain
$ metkr = True
play music "v07/datemusic.mp3"
show krista01 at center with move
kr "Name's Krista. What's yours, sweetie?"
mc "[name]. Nice, err... to meet you Krista."
hide krista01
show krista04
with fastdissolve
kr "You've got some big muscles on ya, hun."
mc "Yeah, thanks for noticing."
hide krista04
show krista05
with fastdissolve
kr "You wanna see my knockers? They're pretty darn big. And soft..."
mc "Err, aren't you... like, worried about your..."
hide krista05
show krista06
with fastdissolve
kr "Derek? He's as stoopid as stoopid goes. Don't ya worry about him, hun...."
mc "Damn, you're really gonna do it?"
hide krista06
show krista07
with fastdissolve
kr "I'm horny. And I'm leaking. Why don't ya come and suck some milk out of my funbags?"
mc "Alright!"
if withbe:
    be "Don't mind me, I literally don't exist. Apparently."
if withpe:
    pe "Don't mind me, I literally don't exist. Apparently."
label KristaAgain:
hide krista07
show krista08
with fastdissolve
play sound "Sounds/slurp.mp3"    
kr "Mmh, you like that don't you, dirty boy?"
scene container02 blurred
show krista09
with fastdissolve
play sound "v08/mclick.mp3"
kr "Oooh, you wan't to feel the warmth of my big tits, hey?"
hide krista09
show krista10
with fastdissolve
play sound "Sounds/moaning.mp3"
kr "Well, go on, stick your head DEEP in there, I'll SMOTHER you with 'em!"
mc "Mmmmhhhhh..."
scene container01
show krista11
with fastdissolve
play sound "v08/squish.mp3"
mc "I want some more milk..."
window hide
with fastflash
play sound "v08/squish.mp3"
kr "You help yourself sweetie, there's plenty of the stuff. Darn kids are always at 'em."
if lustkrista == False:
    call LustPlusKrista
    $ lustkrista = True
window hide
play sound "v08/spitting.mp3"
hide krista11
show krista12
with fastdissolve
mc "Uh oh, I think your husband is coming back our way..."
kr "Don't you worry about him, hun. Just go back over there, I'll deal with it."
stop music
play music "Sounds/desertwind01.mp3"
scene container01
show krista06 at left
show derek05 at midright with moveinright
with dissolve
dr "What you're doing, babe?"
kr "Nuffin. I lost an earring but it dropped between my mounds."
hide derek05 
show derek04 at midright
with fastdissolve
dr "You hear that? She's losing those earrings all the time in those big funbags of hers."
dr "Good thing they're so big, they catch 'em every time, I paid good money for 'em earrings at Walmart."
hide krista06
show krista01 at left
with dissolve
kr "I know hun."
hide derek04 
show derek01 at midright
with fastdissolve
dr "Where were we? Fuck, I can't remember. Gonna open that can."
hide derek01
show derekcan at midright
with dissolve
play sound "v08/canopening.mp3"
if knowcity:
    mc "You were going to tell me about your plan to get inside Trumpf City."
    hide derekcan
    show derek01 at midright
    with fastdissolve
    dr "Was I?"
    jump DerekWall
if knowcity == False:
    mc "You were going to tell me about Trumpf City. Is it nearby?"
    hide derekcan
    show derek04 at midright
    with fastdissolve
    dr "Well doh! Can't you see the wall in the distance behind us? That's Trumpf City."
    mc "Good to know."
    hide derek04
    show derek01 at midright
    with fastdissolve
label DerekWall:
dr "Nobody gets in or out lately anyways. They say there's maintenance work on the West Gate. Sumfin about an upgrade."
hide derek01
show derek03 at midright
hide krista01
show krista02 at left
with fastdissolve
play sound "v08/gulp.mp3"
kr "Yeah, something like, they're waiting for v0.9 at least. Whatever."
mc "v0.9? Oh, I get it."
hide derek03
show derek04 at midright
with fastdissolve
dr "Well tell us man, what's a vee-oh-point-nine?"
mc "They're basically breaking the fourth wall. Get it?"
hide derek04
show derek01 at midright
with fastdissolve
dr "Na, you're making no sense, dude."
hide krista02
show krista01 at left
with fastdissolve
kr "That's just stoopid."    
if withan:
    hide krista01
    show krista02 at left
    with fastdissolve
    kr "What's that girl's name over there?"
    mc "What, Angie? She's travelling with m..."
    hide derek01
    show derek04 at midright
    with fastdissolve
    dr "Angie? You found our Angie?"
    mc "What???"
    hide krista02
    show kristahail at left
    with fastdissolve
    kr "Angie, come over 'ere luv. It's mom and pa!"
    mc "Jee-zus, how old were you when she was born???"
    hide derek04
    hide kristahail
    show krista02 at left
    show derekangie01 at midright
    with fastdissolve            
    kr "I don't know, 12 or sumfin. I don't remember. Whatever."
    dr "Come 'ere to yar old man, my little piece of mud pie!"
    hide krista02
    show krista03 at farleft
    with fastdissolve
    an "Oh pa, I KNEW I would get re-united with you all!"    
    kr "There she is, I knew it was her!"
    $ angiereunited = True
    scene container02 blurred
    show kristaangie01
    with dissolve
    an "Ma, I'm so happy to see you again!"
    kr "Well look at how you've grown!"
    if boughtbaby == False:
        dr "All your brothers are sisters are back inside our container waiting for ya. There's 16 of 'em now."
        kr "Seventeen with the last one that popped out two weeks ago hun."
    if boughtbaby:
        dr "All your brothers are sisters are back inside our container waiting for ya. There's 17 of 'em now."
        kr "We just sold the last one hun. That makes sixteen now..."
    if babyangie:
        an "I have a baby too! She's called Dolly."
        dr "Alright, chuck her in with the rest."
        kr "Who's the father?"
        scene container02
        show krista02 at farleft
        show derek03 at farright
        show angietrash01
        with dissolve
        an "[name] here. He's been protecting me all along!"
        hide derek03        
        show derek01 at farright
        with fastdissolve        
        dr "What, that dork? I'm a grandfather to his kid?"
        hide krista02
        show krista01 at farleft
        with fastdissolve
        kr "Be nice hun, he's our stepson now. And he'll be living with us."
        call LustPlusKrista
        mc "Err, we're not married actually. I have a harem and Angie is in it, that's all. So I won't stay here with you. Sadly."                
        dr "A ha-what? Sounds foreign to me. If you're an Islamo-Nucleorist, you can fuck off back to Gitmo!"
        hide derek01
        show derekspit at farright
        with fastdissolve
        play sound "v08/spitting.mp3"
        $ renpy.pause(0.5, hard=True)
        hide derekspit
        hide angietrash01
        show derekangie02 at right
        with dissolve
        an "He's NOT Pa! He's a HERO! And he's fighting all the bad guys and protecting our Great New Country!"
        dr "Well, can he get us into Trumpf City?"
        hide krista01
        show krista02 at farleft
        with fastdissolve
        kr "Why d'you need him hun? I thought you had a plan."
        dr "I HAVE a plan! Don't need him, but he's welcome to join seeing he's family now."
        $ derekplan = True
        mc "OK, so what's your plan?"
        hide derekangie02
        hide krista02
        show krista01 at farleft
        show derek01 at farright
        show angietrash02
        with dissolve
        dr "I'm still working on it."
    if babyangie == False:
        kr "You didn't get knocked up, did ya sweetie?"
        an "No ma. I've been a GOOD girl!"
        kr "You mean you don't even have a boyfriend luv?"
        scene container02
        show krista02 at farleft
        show derek03 at farright
        show angietrash01
        with dissolve
        an "Well, I... cosplay with [name] here. He's been protecting me all along!"
        hide derek03        
        show derek01 at farright
        with fastdissolve        
        dr "What, that dork?"
        hide krista02
        show krista01 at farleft
        with fastdissolve
        kr "Be nice hun, he brought us our Angie back."
        call LustPlusKrista
        dr "Yeah he did. Sorry man, it was stoopid of me. It's just that you ain't one our kind."
        hide derek01
        hide angietrash01
        show derekangie02 at right
        with dissolve
        an "But he's a HERO! And he's fighting all the bad guys and protecting our Great New Country!"
        dr "Well, can he get us into Trumpf City?"
        hide krista01
        show krista02 at farleft
        with fastdissolve
        kr "Why d'you need him hun? I thought you had a plan."
        dr "I HAVE a plan! Don't need him, but he's welcome to join seeing he brought us our Angie back."
        $ derekplan = True
        mc "OK, so what's your plan?"
        hide derekangie02
        hide krista02
        show krista01 at farleft
        show derek01 at farright
        show angietrash02
        with dissolve
        dr "I'm still working on it."
    an "I hope you don't mind if I stay with my mom and pa?"
    mc "Err... So you're leaving my harem?"
    hide derek01
    hide angietrash02
    show derek03 at farright
    show angietrash02
    with fastdissolve
    play sound "v08/gulp.mp3"
    an "Y...Yes. I've got to take care of all my little brothers and sisters!"
    hide angietrash02
    show angietrash03
    with fastdissolve
    mc "It's fine Angie. I'll come and visit every now and then. Until v0.9 at least."
    hide derek03
    hide angietrash03
    show derek04 at farright
    show angietrash02
    with fastdissolve
    dr "There he goes again about that vee-oh-point-nine!"
    $ hareman = False
    $ girlsinharem -= 1
    hide krista01
    hide derek04
    show krista01 at farleft
    show derek01 at farright
    with fastdissolve
    kr "Let it go hun. Whatever."
    mc "Well, I'll leave your happy family get-together. It's late and I need to get back to the compound and my nice comfy bed."
    hide angietrash02
    show angietrash03
    with dissolve
    an "Bye [name]! Thanks for re-uniting me with my mom and pa!"
    hide derek01
    hide angietrash03
    show derek02 at farright
    show angietrash03
    with fastdissolve
    dr "He thinks we ain't good enough for 'im. I told ya."
    hide krista01
    show krista02 at farleft
    with fastdissolve
    kr "Let's go back inside. I need another pack of cigarettes." 
    hide krista02
    hide derek02
    hide angietrash03
    with dissolve
    jump BackHex53
if withan == False:
    mc "Well, I guess I won't hold you up any longer. It's late and I need to get back to the compound and my nice comfy bed."
    hide derek01
    show derek02 at midright
    with fastdissolve
    dr "He thinks we ain't good enough for 'im. I told ya."
    hide krista01
    show krista02 at left
    with fastdissolve
    kr "Let's go back inside. I need another pack of cigarettes."
    hide krista02
    hide derek02
    with dissolve
    if beenhex53:
        jump BackHex53b            
    jump BackHex53

label BackHex53:
if withbe and angiereunited and bellalustangie ==False:
    $ bellalustangie = True
    scene container02
    show bellaout01
    with dissolve
    be "That's the first time I see you giving away something you own for the greater good..."
    call LustPlusBella
    hide bellaout01
    show bellaout03
    with fastdissolve
    be "You are following the teachings of the Church in doing so."
    mc "Really? I hadn't even realized the Church taught that actually...."
stop music
$ period += 1
scene command01
show lena01
with fade
le "So, what do you have to report about area F3?"
if withza:
    mc "Err, we met some hillbillies. They didn't take too kindly to Zara. So I'll have to go back there without her."
    hide lena01
    show lenapensive
    with fastdissolve
    le "Hillbillies? I guess nobody thought of nuking Kentucky or West Virginia..."
    hide lenapensive
    show lena03
    with fastdissolve
    le "You're dismissed. But do go back there. Without Zara."
    hide lena03 with dissolve
    jump LeaveCommand
if angiereunited and toldlenaangie == False:
    $ toldlenaangie = True
    mc "Thanks to me, Angie is re-united with her...err... lovely family. That's one less mouth to feed here, Chief!"
    hide lena01
    show lena06 
    with fastdissolve
    le "I suppose that is good news, she never had the fighting spirit we need. Plus, she was a Trumpster anyway."
    mc "That's right, one less Trumpster too, Chief! Only 74 millions to go."
    hide lena06
    show lena01
    with fastdissolve
    le "Anything else?"
if boughtbaby and toldlenababy == False:
    $ toldlenababy = True
    mc "I bought... A baby."
    hide lena01
    show lena03
    with fastdissolve
    le "And why the hell would you do that?"
    mc "Err, because it might be useful in the future. Or so I'm told."
    hide lena03
    show lena06
    with fastdissolve
    le "*sigh*. What's the baby's name?"
    mc "Ah. That is a good question. I forgot to ask."
    hide lena06
    show lena05
    with fastdissolve
    le "You're really a pathetic father you know?"
    mc "Doesn't matter, I'll put it in the crib and nurse Rachel will take care of him for me."
    hide lena05
    show lena01
    with fastdissolve
    le "Anything else?"
    if knowcity and toldlenawall:
        mc "Not that I can think of, Chief."
        le "You are dismissed."
        jump LeaveCommand        
if knowcity and toldlenawall == False:
    $ toldlenawall = True
    mc "Good news Chief, I can now CONFIRM that Trumpf City is indeed in hex G3."
    hide lena01
    show lena07
    with fastdissolve
    le "Very well, I will update the map accordingly. Now is the time to start thinking of a plan to ENTER the city..." 
    mc "Err... Not until v0.9 at least from what I heard. Maintenance work at the gate..."
    hide lena07
    show lena03
    with fastdissolve
    le "What? Oh, I get it."
    mc "I knew you would. That's why you're the boss, Chief!"
    le "You are dismissed."
    hide lena03 with dissolve
    jump LeaveCommand
if knowcity == False:
    $ knowcity = True
    mc "Good news Chief, I think we're getting close. I believe Trumpf City might be in hex G3."
    hide lena01
    show lena07
    with fastdissolve
    le "FINALLY! I will update the map accordingly. Good work, [name], you are dismissed." 
    window hide
    show knowledgecity at posmission
    $ renpy.pause(1.0, hard=True)
    pause
    hide knowledgecity
    hide lena07 with dissolve
    jump LeaveCommand
mc "Not that I can think of, Chief."
le "You are dismissed."
jump LeaveCommand

label BackHex53b:
stop music
$ period += 1
scene command01
show lena01
with fade
le "So, what do you have to report about area F3?"
mc "Nothing new since my last visit, Chief!"
hide lena01
show lena06 
with fastdissolve
le "Then stop wasting your time going there!"
mc "Just waiting for that maintenance work at the gate to be finished..."
hide lena06
show lenapensive 
with fastdissolve
le "I know. It's taking ages. We really need a Game Infrastructure Week in this country..."
mc "Not gonna happen with those Trumpster senators, that's for sure!"
hide lenapensive
show lena03 
with fastdissolve
le "You are dismissed."
hide lena03 with dissolve
jump LeaveCommand
    
label BackHex53c:
stop music
$ period += 1
scene command01
show lena01
with fade
le "So, what do you have to report about area F3?"
mc "I've got a new quest, Chief!"
hide lena01
show lena06 
with fastdissolve
le "Consisting in what?"
mc "Just need to bring some salad seeds back and I'll get into Trumpf City. I'll ask Laurie for them."
hide lena06
show lenapensive 
with fastdissolve
le "Not sure that will work. If I remember correctly, she doesn't keep seeds but uses radiations to grow her damn salads."
mc "Ah. Well, I'll ask her anyway, what do I have to lose?"
hide lenapensive
show lena03 
with fastdissolve
le "Fine. You are dismissed."
hide lena03 with dissolve
jump LeaveCommand
    
label KristaFuck:
    play channel1 "v07/datemusic.mp3"
    show krista01 at center with move
    mc "Stoopid's gone again. I mean your husband. According to the stairwell to heavens adult game rule, this would mean..."
    hide krista01
    show krista05
    with fastdissolve
    kr "...That I'm going to let you fuck me with your horsecock? Sure hun."
    mc "Bingo! You just got to love the stairwell."
    hide krista05
    show krista06
    with fastdissolve
    kr "Well get naked hun, we don't have much time."
    play sound "Sounds/zipper.mp3"
    hide krista06
    show krista07
    with fastdissolve
    kr "Still as big as an Alabama Anaconda. Come over 'ere hun."
    hide krista07
    show kristapreballs01
    with fastdissolve
    call LustPlusKrista
    kr "Mmmh, I love your fat donkey dong. Let me taste those fat bull-balls for starters..."
    play channel2 "Sounds/lick.mp3"
    scene containerkristatits
    show kristaballs    
    call screen kristaballsscreen01b
    screen kristaballsscreen01b:
        modal True
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("KristaBallsEndb")    
    label KristaBallsEndb:    
    mc "That's... enough, I need to fuck that pussy of yours, Krista!"
    kr "Let me get out of these shorts for you hun."
    hide kristaballs
    stop channel2
    scene container01 blurred
    show kristapresex00
    with dissolve
    kr "Your cock is so hard for me hun..."
    hide kristapresex00
    show kristapresex01
    with fastdissolve
    kr "And you're leaking all over my ass. You like it, hun?"
    scene container02 blurred
    show kristapresex02
    with fastdissolve
    mc "Fuck yeah, it's a nice bubble ass, ideal for a good pussy-POUNDING from behind!"
    play music "Sounds/barbarasex.mp3"
    label KristafuckSlow:
    scene container02 blurred
    show kristasexslow
    call screen kristaslow01
    screen kristaslow01:
        modal True
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("KristafuckEnd")
        imagebutton:
            focus_mask True
            idle "Icons/fasteridle.png"
            hover "Icons/fasterhover.png"
            action Jump ("KristafuckFast") 
        imagebutton:
            focus_mask True
            idle "v07/frontidle.png"
            hover "v07/frontidle.png"
            action Jump ("KristafuckPOVSlow") 

    label KristafuckPOVSlow:
    scene containerkristafront blurred
    show kristafrontslow
    call screen kristafrontslow01
    screen kristafrontslow01:
        modal True
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("KristafuckEnd")
        imagebutton:
            focus_mask True
            idle "Icons/fasteridle.png"
            hover "Icons/fasterhover.png"
            action Jump ("KristafuckPOVFast") 
        imagebutton:
            focus_mask True
            idle "Icons/sceneview.png"
            hover "Icons/sceneview.png"
            action Jump ("KristafuckSlow") 

    label KristafuckFast:
    if kristafucksaid == False:
        kr "Hurry up hun, Derek will come back soon..."
        $ kristafucksaid = True
    scene container02 blurred
    show kristasexfast
    call screen kristafast01
    screen kristafast01:
        modal True
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("KristafuckEnd")
        imagebutton:
            focus_mask True
            idle "Icons/sloweridle.png"
            hover "Icons/slowerhover.png"
            action Jump ("KristafuckSlow") 
        imagebutton:
            focus_mask True
            idle "v07/frontidle.png"
            hover "v07/frontidle.png"
            action Jump ("KristafuckPOVFast") 

    label KristafuckPOVFast:
    if kristafucksaid == False:
        kr "Hurry up hun, Derek will come back soon..."
        $ kristafucksaid = True
    scene containerkristafront blurred
    show kristafrontfast
    call screen kristafrontfast01
    screen kristafrontfast01:
        modal True
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("KristafuckEnd")
        imagebutton:
            focus_mask True
            idle "Icons/sloweridle.png"
            hover "Icons/sloweridle.png"
            action Jump ("KristafuckPOVSlow") 
        imagebutton:
            focus_mask True
            idle "Icons/sceneview.png"
            hover "Icons/sceneview.png"
            action Jump ("KristafuckFast") 
                
    label KristafuckEnd:
    $ kristafucksaid = False
    kr "Now you dump a nice big fat load inside my pussy hun. Let's see what you got."
    mc "Yeah, I'm getting there, I will, I'm gonna..."
    stop music
    scene container02 blurred
    show kristasexcum01
    with dissolve
    stop channel2
    play channel2 "Sounds/splooge01.mp3"
    mc "CUM, AAAH!"
    if persistent.cumsoundon:
        play sound "Sounds/mccum.mp3"
    window hide
    with fastflash
    kr "Keep going hun, I know you got more cream for me. Stick it real deep inside my womb."
    hide kristasexcum01
    show kristasexcum02
    with dissolve
    if persistent.cumsoundon:
        play sound "Sounds/cumming.mp3"
    mc "HERE IT COMES!"
    window hide
    with fastflash
    kr "Blow that nut right there, I want your BABY hun!!!"
    stop channel2
    scene containerkristafront blurred
    show kristasexcum03
    with dissolve
    if persistent.cumsoundon:
        play sound "Sounds/mccum.mp3"
    mc "You've got enough in you, I don't want triplets, RHAAA!"
    window hide
    with fastflash
    kr "I ain't never seen no boy come that much hun."
    hide kristasexcum03
    show kristasexcum04
    with dissolve
    if persistent.cumsoundon:
        play sound "Sounds/cumming.mp3"
    kr "Still going? You want to cover my big funbags, don't you hun?"
    window hide
    with fastflash
    mc "AAAH, YEAH, HERE ARE THE LAST FEW SHOTS!"
    window hide
    with fastflash
    kr "Derek ain't never come that much hun. In a whole year."
    stop sound
    stop channel1
    hide kristasexcum04
    show kristasexcum05
    with dissolve
    mc "Shit... You've got cum all over your knockers and Derek is coming back..."
    kr "Don't you worry about that hun. Get dressed and I'll deal with him."    
    stop channel1
    scene container01
    show krista06cum at left
    show angietrash04 with moveinright
    show cart with moveinright
    show derek05 at midright with moveinright
    dr "What you're doing, babe?"
    kr "Nuffin. I was feeding the small one and he choked on my milk and spit it all out on me."
    hide derek05 
    show derek01 at midright
    with fastdissolve
    dr "That's a good idea to feed 'im before we go to the wall. Don't want him crying inside those bags."
    hide krista06cum
    show krista02 at left
    with dissolve
    kr "What bags hun?"
    hide derek01
    show derekcan at midright
    with dissolve
    play sound "v08/canopening.mp3"    
    dr "We'll have to hide the babies in the bags. We put the seedbag on top, so they don't find the babies if they check."
    hide krista02
    show krista01 at left
    with dissolve
    mc "THAT'S the plan?"
    hide derekcan
    show derek04 at midright
    with dissolve
    dr "Yeah, you got a better idea Mr Smart Ass? We're supposed to be farmers, and they don't allow babies in there!"
    mc "Alright, fine, if that's the plan, that's the plan. Let me do the talking though."
    $ derekplantried = True
    jump TrumpfWallDerek

label TrumpfWall01:  
show screen mcstats
show screen calendar
scene trumpfwall01 with fade
play music "v06/spooky.mp3"
mc "Jeezus, there's a huge line already... Worse than at the airport. And they're playing spooky music too."
menu:
    "Wait for your turn":
        call AloneStance
        jump TrumpfWall02
    "Get your diplomatic pass ready and wait for your turn" if diplomaticpass and moustache == False:
        call AloneStance
        jump TrumpfWall02
    "Wear your French moustache, get your diplomatic pass ready and wait for your turn" if diplomaticpass and moustache:
        call AloneStance
        jump TrumpfWall02
    "Get the hell outta here":
        mc "Come on, let's go back home, this is going to take too long and this place is spooking me out."
        jump LeaveWall

label TrumpfWall02:
$ period += 1
scene trumpfwall02 blurred
show tsa00
with fade
if period == 3:
    ts "HALT!"
    mc "* Oh my God, this took sssoooo long. And now it's the evening, I hope it's not too late... *"
    hide tsa00
    show tsa01
    with fastdissolve
    ts "City entry is closed for the night. Come back tomorrow."
    mc "What? Hang on, I've been waiting in this godam line for HOURS and I..."
    hide tsa01
    show tsa07
    with fastdissolve
    ts "I said MOVE ALONG! SCHNELL!"
    jump LeaveWall01

ts "HALT! PAPIERE!"
hide tsa00
show tsa01
with fastdissolve
ts "I mean, PAPERS!"
if diplomaticpass == False:
    mc "Papers? Err, I don't have any but I have an appointment with...err..."
    ts "NO PAPERS means NO ENTRY! Move along."
    mc "What? Hey, hang on, let me expl..."
    hide tsa01
    show tsa07
    with fastdissolve
    ts "MOVE ALONG! SCHNELL!"
    jump LeaveWall02

if diplomaticpass:
    mc "I am a French diplomat, here are my credentials..."
    hide tsa01
    show tsa02
    with fastdissolve
    ts "Let me see..."
    window hide
    hide tsa02
    show tsa03
    with dissolve
    $ renpy.pause(2.0, hard=True)
    hide tsa03
    show tsa04
    with fastdissolve
    $ renpy.pause(1.0, hard=True)
    hide tsa04
    show tsa03
    with fastdissolve
    $ renpy.pause(2.0, hard=True)
    if moustache == False:
        hide tsa03
        show tsa06
        with fastdissolve
        ts "You don't look French to me. MOVE ALONG!"        
        play sound "v09/french.wav"
        mc "What? Surely, this is a mistake, you can clearly tell from my out-rrageous accent that I AM French!"
        hide tsa06
        show tsa01
        with fastdissolve
        ts "You're not fooling me! MOVE ALONG!"
        mc "I shall..err... complain to the highest Autorité!"
        hide tsa01
        show tsa07
        with fastdissolve
        ts "Heard that before... MOVE ALONG! SCHNELL!"
        jump LeaveWall03
    if withbe or withpe:
        hide tsa03
        show tsa05
        with fastdissolve
        ts "Who is this woman with you? Is she carrying a weapon?"
        mc "Ah yes, as a French diplomat, I always travel with an entourage. A French word. This is my....military attaché. That's also a French word by the way."
        hide tsa05
        show tsa03
        with fastdissolve
        ts "Get on with it!"
        mc "Yes... err.. So we're together and she's armed of course. For personal protection. That's allowed under the... (cough) Convention if I'm not mistaken."
        hide tsa03
        show tsa04
        with fastdissolve
        ts "Maybe. I'll decide."
        window hide
        hide tsa04
        show tsa03
        with fastdissolve
        $ renpy.pause(2.0, hard=True)
        hide tsa03
        show tsa04
        with fastdissolve
        $ renpy.pause(1.0, hard=True)
        hide tsa04
        show tsa03
        with fastdissolve
        $ renpy.pause(2.0, hard=True)
        if week >= 26:
            hide tsa03
            show tsa06
            with fastdissolve
            ts "This passport is no longer valid."
            play sound "v09/french.wav"
            mc "What? Surely, this is a mistake, you can clearly see from my moustache that I am French! HAN HAN HAN!"
            hide tsa06
            show tsa01
            with fastdissolve
            ts "PAPIERE NOT VALID. Move along."
            mc "I shall..err... complain to the highest Autorité!"
            hide tsa01
            show tsa07
            with fastdissolve
            ts "Heard that before... MOVE ALONG! SCHNELL!"
            jump LeaveWall04
        if week <= 25:
            hide tsa03
            show tsa08
            with fastdissolve
            ts "Everything seems to be in ordnung. You can move to the gate."
            jump TrumpfGate
    if alone:
        hide tsa03
        show tsa05
        with fastdissolve
        ts "You are alone? Do you carry a weapon?"
        mc "Yes, and as a diplomat, I always travel with my service weapon of course. That's allowed under the... (cough) Convention if I'm not mistaken."
        hide tsa05
        show tsa04
        with fastdissolve
        ts "Maybe. I'll decide."
        window hide
        hide tsa04
        show tsa03
        with fastdissolve
        $ renpy.pause(2.0, hard=True)
        hide tsa03
        show tsa04
        with fastdissolve
        $ renpy.pause(1.0, hard=True)
        hide tsa04
        show tsa03
        with fastdissolve
        $ renpy.pause(2.0, hard=True)
        if week >= 26:
            hide tsa03
            show tsa06
            with fastdissolve
            ts "This passport is no longer valid."
            play sound "v09/french.wav"
            mc "What? Surely, this is a mistake, you can clearly see from my moustache that I am French! HAN HAN HAN!"
            hide tsa06
            show tsa01
            with fastdissolve
            ts "PAPIERE NOT VALID. Move along."
            mc "I shall..err... complain to the highest Autorité!"
            hide tsa01
            show tsa07
            with fastdissolve
            ts "Heard that before... MOVE ALONG! SCHNELL!"
            jump LeaveWall04
        if week <= 25:
            hide tsa03
            show tsa08
            with fastdissolve
            ts "Everything seems to be in ordnung. Move towards the gate, Monsieur."
            jump TrumpfGate

label LeaveWall:
stop sound
stop music
$ period += 1
scene command01
show lena01
with fade    
le "I heard you amost tried to enter Trumpf City through the West Gate, and then you chickened out."
mc "That's correct. I just couldn't be bothered."
hide lena01
show lena10
with fastdissolve
le "YOU ARE DISMISSED!"
hide lena10 with dissolve
jump LeaveCommand

label LeaveWall01:
stop sound
stop music
$ period += 1
scene command01
show lena01
with fade    
le "I heard you tried to enter Trumpf City through the West Gate, so why are you back here in the middle of the night?"
mc "Err, well, the line was just... SSSOOO LONG. By the time I arrived at the gate, it had been closed for the night."
hide lena01
show lenapensive
with fastdissolve
le "Clearly, you need to start queuing up there IN THE MORNING. You are dismissed."
hide lenapensive with dissolve
jump LeaveCommand

label LeaveWall02:
stop sound
stop music
$ period += 1
scene command01
show lena01
with fade    
le "I heard you tried to enter Trumpf City through the West Gate, so why are you back here?"
mc "I forgot my papers. Silly mistake really."
hide lena01
show lena10
with fastdissolve
le "And one that just cost us another wasted day! DISMISSED!"
hide lena10 with dissolve
jump LeaveCommand             
    
label LeaveWall03:
stop sound
stop music
$ period += 1
scene command01
show lena01
with fade    
le "I heard you tried to enter Trumpf City through the West Gate, so why are you back here?"
mc "That TSA agent over there wouldn't believe that I was French despite my passport. I shall complain to the highest Autorit..."
hide lena01
show lena10
with fastdissolve
le "I don't believe myself that you're French for an instant, how do you expect a trained TSA agent to be fooled by your amateurish attempts? DISMISSED."
hide lena10 with dissolve
jump LeaveCommand                                                                                            
                                                                                            
label LeaveWall04:
stop sound
stop music
$ period += 1
scene command01
show lena01
with fade    
le "I heard you tried to enter Trumpf City through the West Gate, so why are you back here?"
mc "That diplomatic passport I got from Wendy had expired. I don't get it. Didn't know it even had an expiry date."
hide lena01
show lena10
with fastdissolve
le "I'm pretty sure Wendy explained that to you but you weren't listening as per usual!"
if qanonwonfight == False:
    le "And since we are past week 25 because you've been piss-farting around instead of being FOCUSED on your job, this way to enter Trumpf City is GONE. You NEED to find another way in. DISMISSED!"
if qanonwonfight:
    le "And since we are past week 30 because you've been piss-farting around instead of being FOCUSED on your job, this way to enter Trumpf City is GONE. You NEED to find another way in. DISMISSED!"
hide lena10 with dissolve
jump LeaveCommand              
                                                                                            
label TrumpfGate:
scene trumpfwall03 with dissolve
fg "You can go through now. But something tells me I'll be seeing you again..."
mc "Err, okay..."
scene trumpfwall04 with dissolve
mc "There you have it! I'm about to enter Trumpf City! Woo-Hoo! Supreme White House, here we come!"
if withbe == False and withpe == False and withkr:
    kr "We'll be heading for a container park hun."
    dr "Yeah, I know there's one close by. My contact told me so."   
jump FinalStart

label TrumpfWallDerek:
scene trumpfwall01 with fade
play music "v06/spooky.mp3"
mc "Jeezus, there's a huge line already... Worse than at the airport. And they're playing spooky music too."
dr "Damn refugees. *spit*"
play sound "v08/spitting.mp3"
kr "We're refugees too hun."
menu:
    "Wait for your turn":
        jump WallDerek
    "Get the hell outta here":
        mc "Sorry guys, but I have a thing about waiting in lines for hours. I don't do it."
        dr "He thinks we ain't good enough for 'im. I told ya."
        kr "Lets go back to our container park hun, I ran out of cigarettes."
        scene container01
        show krista01 at left
        show derek01 at midright
        with dissolve        
        kr "We should go there without him, hun. He ain't going with us."
        hide derek01
        show derek02 at midright
        with fastdissolve
        dr "He thinks we ain't good enough for 'im. I told ya."
        hide krista01
        show krista02 at left
        with fastdissolve
        kr "Let's go back inside. I need another pack of cigarettes." 
        hide krista02
        hide derek02
        with dissolve
        stop sound
        stop music
        $ period += 1
        scene command01
        show lena01
        with fade    
        le "I heard you tried to enter Trumpf City through the West Gate, so why are you back here?"
        mc "I don't like queuing up. Heroes don't queue up."
        hide lena01
        show lena10
        with fastdissolve
        le "Heroes do whatever their hero boss tells them to do! And I told you to get INSIDE TRUMPF CITY! DISMISSED!"
        hide lena10 with dissolve
        jump LeaveCommand      

label WallDerek:
$ period += 1
scene trumpfwall02 blurred
show tsa00 at left
with fade
show cart with moveinright

if period == 3:
    ts "HALT!"
    mc "* Oh my God, this took sssoooo long. And now it's the evening, I hope it's not too late... *"
    hide tsa00
    show tsa01 at left
    with fastdissolve
    ts "City entry is closed for the night. Come back tomorrow."
    mc "What? Hang on, we've been waiting in this godam line for HOURS and I..."
    hide tsa01
    show tsa07 at left
    with fastdissolve
    ts "I said MOVE ALONG! SCHNELL!"
    scene container01
    show krista01 at left
    show derek01 at midright
    with dissolve
    kr "We should have gone there in the morning."
    hide derek01
    show derek02 at midright
    with fastdissolve
    dr "Too many godam refugees..."
    hide derek02
    show derekspit at midright
    with fastdissolve
    play sound "v08/spitting.mp3"
    $ renpy.pause(0.5, hard=True)
    hide derekspit
    show derek01 at midright
    mc "Okay, we'll try again tomorrow. MORNING. How's that for a PLAN?"
    hide krista01
    show krista02 at left
    with fastdissolve
    kr "Sure. Whatever."
    window hide
    hide derek01
    show derek04 at midright
    with fastdissolve    
    dr "Yeah, see ya dude."
    stop sound
    stop music
    $ period += 1
    scene command01
    show lena01
    with fade    
    le "I heard you tried to enter Trumpf City through the West Gate, so why are you back here?"
    mc "Err, well, the line was just... SSSOOO LONG. By the time I arrived at the gate, it had been closed for the night."
    hide lena01
    show lenapensive
    with fastdissolve
    le "Clearly, you need to start queuing up there IN THE MORNING. You are dismissed."
    hide lenapensive with dissolve
    jump LeaveCommand      
    
ts "HALT!"
mc "Guys, just let me do the talking, I'm used to dealing with tough women..."
hide tsa00
show tsa01 at left
with fastdissolve
ts "What's this cart? What is your business trying to enter Trumpf City?"
mc "We are farmers selling seeds."
hide tsa01
show tsa07 at left
with fastdissolve
ts "GUARD!"
scene trumpfwall02b blurred
show guardwall01 at farright
show cart
show tsa10 at left
with dissolve
ts "Check the bags. With the bayonet."
hide cart
hide guardwall01
show guardwall02 at farright
show cart
with fastdissolve
fg "All of them?"
mc "* Shit... Let's think quickly here. *"
menu:
    "The seeds need to be kept out of the foul air, they are radiation-organic.":
        hide tsa10
        show tsa01 at left
        with fastdissolve
        ts "Check the top bag only."
        hide cart
        hide guardwall02
        show guardwall03 at farright
        show cart
        with fastdissolve
        play sound "v06/knife.mp3"
        fg "Looks like seeds alright, Sergent Frau Engel."
        scene trumpfwall02 blurred
        show cart
        if withpe:
            show tsa10 at left
            with fastdissolve
            ts "This woman over there. She's a Road Warrior, I can see her tattoo. Road Warriors are BANNED from Trumpf City!"
            pe "Err, me? I'm not with them, I'm in the line BEHIND THEM! And it's moving REAL SLOW!"
            hide tsa10
            show tsa07 at left
            with fastdissolve            
            ts "You shouldn't have bothered queing up then! Get her out of the line!"
            pe "Fine, I never wanted to enter this stinky town in the first place..."
            $ withpe = False
            hide tsa07
            show tsa01 at left
            with fastdissolve
            mc "The gall of some people, hey? Trying to sneak in by pretending to be with honest farmers such as ourselv..."
        if withmo == False and withla == False:
            show tsa01 at left            
            ts "Let me see your hands."
            mc "Err... Okay."
            hide tsa01
            show tsa11 at left
            show mchandswall02 at farleft
            with fastdissolve
            ts "They're clean, as I suspected. You don't look like farmers. Any of you."
            hide mchandswall02
            mc "And what does a farmer look like to you?"
            hide tsa11
            show tsa02 at left
            with fastdissolve            
            ts "A farmer looks like someone with a hand that's holding a nice fat banknote for me..."
            menu:
                "Offer her twenty bucks" if money >= 20:
                    show mchandwall01 at left
                    mc "Okay, that's my dirty farmer's hand for you..."
                    $ money -= 20
                    if mctrumpster <= 4 or trumpsternickname == False:
                        hide mchandwall01
                        hide tsa02
                        show tsa07 at left
                        with fastdissolve
                        ts "Not dirty ENOUGH... Move along."
                        mc "Hey! What about my mon..."
                        ts "Move along, SCHNELL!"
                        jump LeaveWall05
                    if mctrumpster == 5 and trumpsternickname:
                        hide mchandwall01
                        hide tsa02
                        show tsa01 at left
                        with fastdissolve
                        ts "I'll agree to that pitiful amount since you are a famous Trumpster, \"[name] the Grabber\"..."
                        mc "Finally, some use to that faction..."                        
                        hide tsa01
                        show tsa09 at left
                        with fastdissolve
                        ts "Move over to the gate."
                        $ withkr = True
                        jump TrumpfGate                    
                "Offer her fifty bucks" if money >= 50:
                    show mchandwall01 at left
                    with fastdissolve
                    mc "Okay, that's my dirty farmer's hand for you..."
                    $ money -= 50  
                    hide mchandwall01
                    hide tsa02
                    show tsa09 at left
                    with fastdissolve
                    ts "Dirty enough for me to be convinced you are farmers. Move over to the gate..."
                    $ withkr = True                    
                    jump TrumpfGate
                "And what if I reported YOU, Mmmh? How would like THAT?":
                    hide tsa02
                    show tsa11 at left
                    with fastdissolve
                    ts "And who would you report me to exactly?"
                    mc "Err..."
                    hide tsa11
                    show tsa01 at left
                    with fastdissolve
                    ts "That's right. Nobody. I have complete authority here, so says the Super-Duper-Patriot Act."
                    hide tsa01
                    show tsa07 at left
                    with fastdissolve
                    ts "Which means... MOVE ALONG, SCHNELL!"
                    jump LeaveWall05
                    
        if withmo:
            show tsa01 at left
            ts "Let me see your hands."
            mc "Err... Okay."
            hide tsa01
            show tsa11 at left
            show mchandswall02 at farleft
            with fastdissolve
            ts "They're clean, as I suspected."
            hide mchandswall02
            hide tsa11
            show tsa10 at left
            with fastdissolve
            ts "None of you look like farmers. Except this woman over there with you."
            mc "You mean my landl..., Nancy the Farmer?"
            hide tsa10
            show tsa01 at left
            with fastdissolve
            ts "Yes. Why is that?"
            mc "She's our...err... matriarch."
            hide tsa01
            show tsa10 at left
            with fastdissolve
            ts "Then why are YOU talking and not her?"
            mo "Oh dear... Ma'am, I don't speak much, too busy chopping up salads, chop chop, here you go, would you like a burger paddie with that?"
            ts "Uhm..."
            window hide
            $ renpy.pause(1.0, hard=True)
            hide tsa10
            show tsa09 at left
            with fastdissolve
            ts "That's convincing enough, move over to the gate..."
            $ withkr = True
            jump TrumpfGate
        if withla:
            show tsa01 at left
            ts "Let me see your hands."
            mc "Err... Okay."
            hide tsa01
            show tsa11 at left
            show mchandswall02 at farleft
            with fastdissolve
            ts "They're clean, as I suspected."
            hide mchandswall02
            hide tsa11
            show tsa10 at left
            with fastdissolve
            ts "None of you look like farmers. Except this woman over there with you."
            mc "You mean Laurie, our food engineer?"
            hide tsa01
            show tsa10 at left
            with fastdissolve
            ts "Yes. Why is that?"
            mc "She's the one who... puts the seeds in the bag. And we have clean hands because we carry the...clean bags."
            la "Salad needs lots of care. Did you know that one of my mutated salad seeds can feed en entire family for a week?"            
            hide tsa10
            show tsa01 at left
            with fastdissolve
            ts "Uhm..."
            window hide
            $ renpy.pause(1.0, hard=True)
            hide tsa01
            show tsa09 at left
            with fastdissolve
            ts "That's convincing enough, move over to the gate..."
            $ withkr = True
            jump TrumpfGate
        
    "How dare you stop us when we are here to feed YOU and the people inside this city!":
        hide tsa10
        show tsa07 at left
        with fastdissolve
        ts "The Trumpf Militia has plenty of food. And the people inside this camp... I mean, city, are none of my concern!"
        ts "GUARD! Check ALL the bags with the BAYONET!"
        mc "Okay, okay, how about we just leave quietly and there's no need to waste your bayonet tip on our bags, hey?"
        hide tsa07
        show tsa11 at left
        with fastdissolve
        ts "For twenty Deutsche Ma.., I mean New Dollars, I'll look the other way. THIS TIME."
        menu:
            "Give her the money" if money >= 20:
                hide tsa11
                show tsa02 at left
                show mchandwall01 at left
                with fastdissolve
                $ money -= 20
                mc "Alright, here you are, take it and let us go."
                hide mchandwall01
                hide tsa02
                hide cart
                hide guardwall02
                show guardwall01 at farright
                show cart
                show tsa01 at left
                with fastdissolve
                ts "And now, MOVE ALONG! SCHNELL!"
                stop sound
                stop music
                scene container01
                show krista01 at left
                show derek01 at midright
                with dissolve
                kr "Well that was money well spent [name]..."
                mc "I... I picked the wrong option from the menu obviously... But we got out alive, right?"
                hide derek01
                show derek02 at midright
                with fastdissolve
                dr "He thinks it's funny! He ain't serious, I told ya!"
                hide krista01
                show krista02 at left
                with fastdissolve
                kr "We'll try again tomorrow. And [name] will pick the CORRECT option. Let's go back inside hun, I need another pack of cigarettes."
                $ period += 1
                scene command01
                show lena01
                with fade    
                le "I heard you tried to enter Trumpf City through the West Gate, and yet you're back and Trumpf is still President-for-Life. What happened?"
                mc "You just wouldn't believe the corruption inside the TSA. Shocking, just shocking!"
                hide lena01
                show lena06
                with fastdissolve
                le "Actually I would believe it. You are dismissed."
                hide lena06 with dissolve
                mc "Everyone is numb to administrative corruption these days..."
                jump LeaveCommand      
                
            "Refuse to give her the money":
                mc "No way! This is bribery and I will repo..."
                hide tsa11
                hide cart
                hide guardwall02
                show guardwall01 at farright
                show tsa12 at left
                show cart
                with fastdissolve
                ts "ALARM, ALARM!"
                play sound "Sounds/gun.mp3"
                mc "Shit, she's shooting at me! Run, RUN FOR YOUR LIFE!"
                stop sound
                stop music
                scene container01
                show krista01 at left
                show derek01 at midright
                with dissolve
                kr "We almost got shot, all because of YOU!"
                call MCInjury
                $ mcinjuredgun = True
                mc "Hey! I got shot, not you! And I'm injured. I need to go back to my compound since you guys don't even have a medbay."
                hide derek01
                show derek02 at midright
                with fastdissolve
                dr "See? We ain't good enough for 'im. We ain't got no \"medbay\"! I told ya!"
                hide krista01
                show krista02 at left
                with fastdissolve
                kr "Let's just go back inside, hun. We'll try again another day. WITHOUT him."
                $ derekplanfail = True
                $ period += 1
                scene command01
                show lena01
                with fade    
                le "I heard you tried to enter Trumpf City through the West Gate, and here you are, injured. What happened?"
                mc "The TSA agent there SHOT me! Would you believe that?"
                hide lena01
                show lena06
                with fastdissolve
                le "Yes I would. You are DISMISSED. To the medbay."
                hide lena06 with dissolve
                jump Medbay      
                
label LeaveWall05:
stop sound
stop music
$ period += 1
scene command01
show lena01
with fade    
le "I heard you tried to enter Trumpf City through the West Gate, so why are you back here?"
mc "That diplomatic passport I got from Wendy had expired. I don't get it. Didn't know it even had an expiry date."
hide lena01
show lena10
with fastdissolve
le "I'm pretty sure Wendy explained that to you but you weren't listening as per usual!"
if qanonwonfight == False:
    le "And since we are past week 25 because you've been piss-farting around instead of being FOCUSED on your job, this way to enter Trumpf City is GONE. You NEED to find another way in. DISMISSED!"
if qanonwonfight:
    le "And since we are past week 30 because you've been piss-farting around instead of being FOCUSED on your job, this way to enter Trumpf City is GONE. You NEED to find another way in. DISMISSED!"
hide lena10 with dissolve
jump LeaveCommand            
