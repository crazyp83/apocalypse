label Church:
show screen mcstats
$ loc = "church"
$ seenchurch = True
if period == 1 and day == 7:
    jump SundayService
if period == 1:
    jump ChurchMorning01
if period == 2 or period == 3:
    jump Church01
if period == 4:
    jump ChurchNight01

label SundayService:
scene church01 with fade
show aylachurch
play music "Sounds/church.mp3"
mc "I think Sunday Service is about to start. It might be a good idea to stay if I want to improve my standing in the Church."
menu:
    "Stay for the duration of the service (+1 Church of the Redeeming Phallus)":
        jump SundayService02
    "Leave before anyone notices me":
        jump Main01

label SundayService02:
stop music
ty "...And my sermon on the Capitol Hill shall remind the Lost World of its glorious past."
ty "And women shall repent their sins, for THEY are the True Sinners in the one-eye of the Phallus Lord. Santorum 6:9."
"(Congregation) Se-men"
" Some time later..."
$ period +=1
scene church02 with dissolve
show tyne
ty "I am glad you attended our service my son. That is a sign that you are a True Believer of the New Gospel according to Saint-Orum."
if tyroneexplained == False:
    ty "I hope to see you here REGULARLY. If you don't, your standing in the Church will drop (after three weeks without attendance, -1 faction point)."
    $ tyroneexplained = True
$ churchattended = True
$ churchnotattended = 0
window hide
call PlusChurch
jump LeaveChurch

call screen church01c
screen church01c:
    modal True        
    imagebutton:
        focus_mask True
        idle "Icons/exitidle.png"
        hover "Icons/exithover.png"
        action Jump ("LeaveChurch")
    if churchclgone == False:
        imagebutton:
            focus_mask True
            idle "Church/church01claraidle.png"
            hover "Church/church01clarahover.png"
            action [Jump ("ChurchClara01")]
    if churchtygone == False:
        imagebutton:
            focus_mask True
            idle "Church/church01priestidle.png"
            hover "Church/church01priesthover.png"
            action [Jump ("ChurchTyrone01")]
    if churchbegone == False:
        imagebutton:
            focus_mask True
            idle "Church/church01bellaidle.png"
            hover "Church/church01bellahover.png"
            action [Jump ("ChurchBella01")]
    imagebutton:
        focus_mask True
        idle "Church/church01confidle.png"
        hover "Church/church01confhover.png"
        action [Jump ("ChurchConfess01")]
    if knowcrypt == True:
        imagebutton:
            focus_mask True
            idle "Church/church01cryptidle.png"
            hover "Church/church01crypthover.png"
            action [Jump ("ChurchCrypt01")]
    imagebutton:
        focus_mask True
        idle "Church/church01crossidle.png"
        hover "Church/church01crosshover.png"
        action [Jump ("ChurchCross01")]

label ChurchMorning01:
scene church01c with dissolve
show church01crossidle
mc "Looks very quiet this morning..."
label ChurchMorningb:
call screen churchmorning01
screen churchmorning01:
    add "Church/church01c.jpg"
    modal True    
    imagebutton:
        focus_mask True
        idle "Icons/exitidle.png"
        hover "Icons/exithover.png"
        action Jump ("LeaveChurch")
    imagebutton:
        focus_mask True
        idle "Church/church01confidle.png"
        hover "Church/church01confhover.png"
        action Jump ("ConfessionalMorning")
    if knowcrypt == True:
        imagebutton:
            focus_mask True
            idle "Church/church01cryptidle.png"
            hover "Church/church01crypthover.png"
            action Jump ("CryptMorning")
    imagebutton:
        focus_mask True
        idle "Church/altaridle.png"
        hover "Church/altarhover.png"
        action Jump ("AltarMorning")
    imagebutton:
        focus_mask True
        idle "Church/church01crossidle.png"
        hover "Church/church01crosshover.png"
        action [Jump ("ChurchCrossMorning")]
        
label ChurchCrossMorning:
mc "The cross appears to bear a giant penis instead of Jesus. The pope ain't gonna be happy about that."
jump ChurchMorningb

label AltarMorning:
mc "I can't go there at the moment, this section has not yet been implemented..."
jump ChurchMorningb

label CryptMorning:
mc "I can't go there, the door is locked..."
jump ChurchMorningb

label Church01:
scene church01 with dissolve
play music "Sounds/church.mp3"
mc "Looks like I came in during a church service. I'll stay at the back and wait for it to finish."
ty "...And My Penis shall be the savior of Humanity, and women shall repent their sins and worship it. \n Se-men."
"(Congregation) Se-men"
stop music

label Church01b:
scene church01b
call screen church01b
screen church01b:
    modal True        
    imagebutton:
        focus_mask True
        idle "Icons/exitidle.png"
        hover "Icons/exithover.png"
        action Jump ("LeaveChurch")
    if churchclgone == False:
        imagebutton:
            focus_mask True
            idle "Church/church01claraidle.png"
            hover "Church/church01clarahover.png"
            action [Jump ("ChurchClara01")]
    if churchtygone == False:
        imagebutton:
            focus_mask True
            idle "Church/church01priestidle.png"
            hover "Church/church01priesthover.png"
            action [Jump ("ChurchTyrone01")]
    if churchbegone == False:
        imagebutton:
            focus_mask True
            idle "Church/church01bellaidle.png"
            hover "Church/church01bellahover.png"
            action [Jump ("ChurchBella01")]
    imagebutton:
        focus_mask True
        idle "Church/church01confidle.png"
        hover "Church/church01confhover.png"
        action [Jump ("ChurchConfess01")]
    if knowcrypt == True:
        imagebutton:
            focus_mask True
            idle "Church/church01cryptidle.png"
            hover "Church/church01crypthover.png"
            action [Jump ("ChurchCrypt01")]
    imagebutton:
        focus_mask True
        idle "Church/church01crossidle.png"
        hover "Church/church01crosshover.png"
        action [Jump ("ChurchCross01")]


label ChurchCross01:
if churchbegone == False:
    show church01bellaidle
mc "The cross appears to bear a giant penis instead of Jesus. The pope ain't gonna be happy about that."
jump Church01b

label ChurchConfess01:
if churchbegone == False:
    show church01bellaidle
mc "The confessional is currently empty. I can't go there."
jump Church01b

label ChurchCrypt01:
if churchbegone == False:
    show church01bellaidle
mc "That's the door to the Moist Crypt. I doubt that I can just barge into it in front of everyone like that."
jump Church01b

label ChurchBella01:
show bene with dissolve
be "Yes?"
if churchlore01:
    label BellaChurchDialogue:
    menu:
        "Offer her a Holy Pubic Hair" if pubichair >=1:
            mc "I have something for you. Related to the Church... A Holy Pubic Hair!"
            be "Oh, thank you [name]! I was really hoping you'd offer me one of these, since Pythia never wants to grant ME an audience..."
            call LustPlusBella
            mc "Not her fault, you're a chick, you know, the sinful inferior gender and all that."
            hide bene
            show bella08
            with fastdissolve
            be "I supposed that IS true... I should leave to confess my sins now that you've reminded me..."
            $ pubichair -= 1
            hide bella08 with dissolve
            $ period += 1
            jump LeaveChurch
        "What better place than a church to ask a devout woman like you on adate, don't you think?" if lustbe >= 2 and belladatedone == False and knowredcanyon:
            hide bene
            show bella07
            with fastdissolve            
            be "You mean under the One-Eye of our Phallus Lord?"
            mc "Err, yeah, it would be ike a holy date, right?"
            hide bella07
            show bella06
            with fastdissolve            
            be "It certainly would and therefore I agree!"
            $ belladateon = True  
            mc "I'll pick you up in the morning and take you to the Red Caznyon then!"
            $ period += 1
            jump LeaveChurch                
        "It's time for you to join my harem... So sayeth the Phallus Lord." if lustbe >= 4 and harembe == False and askedbellajoin == False and bellaharem == False and girlsinharem <= 6 and belladatedone and mcchurch >= 4:
            be "Does he now? Did he also warn you about this..."
            $ bellachurch = True
            call BellaHarem
            $ bellachurch = False
            $ period += 1
            jump LeaveChurch                
        "It's time for you to re-join my harem... And be in communion with the wishes of the One-Eye." if lustbe >= 4 and harembe == False and askedbellajoin == False and bellaharem and belladismissed == False and girlsinharem <= 6:
            be "You know what I'm about to say, right?"
            mc "Not really, a girl will need to be kicked out, but who? The suspense is killing me."
            $ bellachurch = True
            call BellaHarem
            $ bellachurch = False
            $ period += 1
            jump LeaveChurch                
        "How do I get to volunteer to clean the Church?":
            hide bene
            show bella07
            with fastdissolve            
            be "You need to acquire sufficient church lore for that. Novices can't hold a holy broom. Talk to Father Tyrone and ask him for Enlightement. TWICE."
            mc "I see. Thanks for the tip, Bella."
            hide bella08
            show bene
            with fastdissolve            
            jump BellaChurchDialogue        
        "That was a nice church service wans't it?":
            be "Beautiful as always. I especially liked the sermon. What was your take on it?"
            mc "Err... I think I might have been praying at that time."
            hide bene
            show bella06
            with fastdissolve            
            be "I see... You weren't listening."
            mc "Nope."
            be "You should think about confessing THAT sin one day... Bye [name]."
            hide bella06 with dissolve
            $ period += 1
            jump LeaveChurch

if churchlore01 == False:
    mc "That priest is a bit weird don't you think? He keeps talking about his penis all the time."
    be "He is only quoting the God of the Brand New Gospel who clearly states that His Phallus is the Road to Salvation!"
    mc "Ah, right, I see. Can my phallus count as a road to salvation?"
    be "Only if it is canonized through the Scepter of God."
    $ churchlore01 = True
    mc "It's a pretty mighty cannon as it is."
    hide bene
    show bean
    be "I meant the priest has to officially elevate your cock to Saint-Manhood. God you're thick."
    mc "Hey, give me a break! I just woke up from this nuclear nightmare, I'm still learning!"
    $ churchbegone = True
    jump Church01b

label ChurchTyrone01:
scene church02 with dissolve
show tyne
if spokety == 0:
    ty "Welcome my son. I am glad to see you came to join us in our daily religious service. Even if I noticed you were late..."
if spokety >= 1 and claraharem and toldtyroneclaraharem == False:
    ty "So I heard that Sister Clara joined your harem..."
    mc "Yeah, she basically left one abusive relationship for another."
    hide tyne
    show tyan
    with fastdissolve
    ty "I can't say that I approve of this turn of events, young man. She is meant to be married to the CHURCH!"
    hide tyan
    show tyrone07b
    with fastdissolve
    ty "But it seems you have relations in high places and Chief Lena has tied my hands, so there's nothing much I can do about it..."
    hide tyrone07b
    show tyrone05b
    with fastdissolve
    ty "Except this!"
    call MinusChurch
    mc "Whatever, I'll grind my way back up the Church's ladder when I see fit, so there!"
    hide tyrone05b with dissolve
    $ period += 1
    $ toldtyroneclaraharem = True
    jump LeaveChurch
if spokety >= 1:
    ty "Welcome my son. I am glad to see you came to join us in our daily religious service. Even if I noticed you were late... Again."
label PriestDialogue01:
menu:
    "I apologize father." if spokety == 0:
        hide tyne
        show typr
        with fastdissolve
        ty "The road to Salvation comes through a long and hard redemption for both women AND men."
        hide typr
        show tyne
        with fastdissolve
        jump PriestDialogue01
    "I would like to know more about the Church." if churchlore02 == False:
        ty "The Church was founded upon the ruins of New America as the guiding beacon to Salvation."
        hide tyne
        show typr
        with fastdissolve
        ty "Women were spared by God so they could repent their sins, and admit that they failed to obey his Manly Orders."
        hide typr
        show tyne 
        with fastdissolve
        mc "I can totally get behind those misogynistic scriptures."
        ty "The Brand New Gospel was written by Prophet Rick Santorum before his demise from an overdose of beta-radiations."
        mc "Santorum? I thought that word meant some kind of anal gay slime. Must be hard to carry such a name."
        hide tyne
        show tyan
        with fastdissolve
        ty "Do not mock our Prophet. He foresaw what would happen if women were left to take over the world. The Church is here to maintain male domination in these troubled times."
        mc "How so?"
        hide tyan
        show typr
        with fastdissolve
        ty "Women are the post-original sinners. It is because of their sins that the end of Great American Days came about. The Church reminds them not to forget that..."
        mc "I see. Thank you Father for taking the time to explain the finer points of the Church's teachings."
        hide typr
        show tyne
        with fastdissolve
        ty "Jizz be with you, my son."        
        $ spokety += 1
        hide tyne
        $ churchlore02 = True
        $ churchtygone = True 
        $ period += 1
        jump LeaveChurch
    "I would like to offer my humble services to the Church." if churchlore04 == True:
        if churchbaptized == False:
            ty "While I admire your devotion, we do not accept novices who aren't baptized."
            mc "And how could I get baptized?"
            hide tyne
            show typr
            with fastdissolve
            ty "It's simple. You pay 10$ and I baptized you. Your donation will serve the Church's funds well, I assure you."
            menu:
                "Pay 10$ and get baptized (+1 Church)" if money >= 10:
                    $ money -= 10
                    ty "Great, follow me to the Moist Crypt."
                    jump Baptism01                    
                "Not now, I'll think about it Father.":
                    ty "Fine. Jizz be with you my son."
                    $ churchtygone = True
                    jump Church01b
        if churchbaptized == True:            
            hide tyne
            show typr
            with fastdissolve
            ty "What devotion! We always are in need of young novices willing to do menial tasks for the glory of the Church of the Redeeming Phallus!"
            label ChurchCleaning:
            $ d2rollchurch=renpy.random.randint(1,2)
            if missionchurch and successchurch == False and failchurch == False and pencescroll == False:
                $ d2rollchurch = 1 
            if claraquest and claraquestdone == False and cleanedaltar == False and marnietipclara:
                mc "May I suggest that I take care of the crypt? It was quite filthy when I last went there for my baptism."
                hide typr
                show tyan
                with fastdissolve
                ty "ABSOLUTELY NOT! You haven't even cleaned the altar this week, why would I let you clean a place that I have clearly designated as OFF-LIMITS to novices such as yourself?"
                mc "I see, but if I clean the altar, maybe you'll let me clean the crypt another day then?"
                hide tyan
                show tyrone07b
                with fastdissolve
                ty "I have no time to even consider this request at this stage. Just do the menial task you VOLUNTEERED to do and clean the altar, it's too dirty right now!"
                $ cleanedaltar = True
                jump CleanAltarChurch                
            if claraquest and claraquestdone == False and cleanedaltar and marnietipclara:
                ty "Why don't you clean the altar? It needs to be as clean as a virgin's bottom."
                mc "I already cleaned the altar this week Father. Why don't I clean the crypt this time? I mean, I saw it when I got baptized, this place needs a thorough scrubbing..."
                hide typr
                show tyrone07b
                with fastdissolve
                ty "This place is normally off-limits... But I suppose I could trust you after all, you have proven your devotion to the Church through the accomplishment of menial tasks."
                mc "You won't regret it, Father, it'll be so clean, you won't even recognize the place!"
                hide tyrone07b
                show tyne
                with fastdissolve
                ty "Fine, I'll open the door for you. But I will come and CHECK on your progress, I'm warning you."
                scene crypt03 with fade
                mc "Ah, finally, I'm alone inside the crypt... Let's look for that redemption box then, can't be that hard to find..."
                mc "I probably don't have that much time until Father Tyrone comes back, so I guess I'll have to snoop around. Just like in that silly game Battle of the Bulges."
                call screen cryptsnoop
                screen cryptsnoop:
                    add "church/crypt03.jpg"
                    modal True
                    default time_leftc = 6.0
                    default topleftnothing = False
                    default toprightnothing = False
                    default rightnothing = False
                    default bottomrightnothing = False
                        
                    if time_leftc <= 0:
                        timer .001 action Return
                    else:
                        timer .1 repeat True action SetScreenVariable("time_leftc", time_leftc-.1)
                    
                    imagebutton:
                        focus_mask True
                        idle "v071/topleftidle.png"
                        hover "v071/toplefthover.png"
                        action [SetScreenVariable('time_leftc', time_leftc-2), SetScreenVariable('topleftnothing', True)]
                    if topleftnothing:
                        add "v071/topleftnothing.png"
                    
                    imagebutton:
                        focus_mask True
                        idle "v071/toprightidle.png"
                        hover "v071/toprighthover.png"
                        action [SetScreenVariable('time_leftc', time_leftc-2), SetScreenVariable('toprightnothing', True)]
                    if toprightnothing:
                        add "v071/toprightnothing.png"
                        
                    imagebutton:
                        focus_mask True
                        idle "v071/bottomleftidle.png"
                        hover "v071/bottomlefthover.png"
                        action [SetScreenVariable('time_leftc', time_leftc-2), Jump ("FoundBox")]

                    imagebutton:
                        focus_mask True
                        idle "v071/bottomrightidle.png"
                        hover "v071/bottomrighthover.png"
                        action [SetScreenVariable('time_leftc', time_leftc-2), SetScreenVariable('bottomrightnothing', True)]
                    if bottomrightnothing:
                        add "v071/bottomrightnothing.png"

                    imagebutton:
                        focus_mask True
                        idle "v071/rightidle.png"
                        hover "v071/righthover.png"
                        action [SetScreenVariable('time_leftc', time_leftc-2), SetScreenVariable('rightnothing', True)]
                    if rightnothing:
                        add "v071/rightnothing.png"

                    bar value StaticValue(time_leftc, 6.0):
                        xalign 0.45 yalign 0.05
                        xmaximum 800 
                        ymaximum 10
                        
                play sound "Sounds/footsteps.mp3"
                mc "Damn it, I was too slow to find anything and now I hear Father Tyrone approaching..."
                window hide
                jump TyroneCrypt
                label FoundBox:
                mc "Victory, I found it!"
                window hide
                show missionclarasuccess at posmission
                $ renpy.pause(2.0, hard=True)
                pause
                hide missionclarasuccess
                $ claraquestdone = True
                mc "Let's hide this box. In my...err...rucksack, which never appears on-screen but that I carry at all times."
                play sound "Sounds/footsteps.mp3"
                mc "UH-OH, I hear Father Tyrone approaching..."                
                window hide
                label TyroneCrypt:
                show tyrone04 with moveinright
                ty "I came to check on your prog.."
                hide tyrone04
                show tyan
                with fastdissolve
                ty "By the Phallus Lord, this place is just as FILTHY as it's always been! What have you been doing all this time???"                
                mc "Well hang on, I've only just started! I put the broom on the broomstick, I rinsed the cleaning cloth in the water, I..."
                ty "GET OUT OF HERE! You are soiling this holiest of places by your very presence!"
                call MinusChurch
                mc "Fine, fine, I see my ability at doing menial tasks isn't appreciated around it. This task was too grindy anyway."
                $ period += 1
                hide tyan with dissolve
                jump LeaveChurch
            if d2rollchurch == 1:
                ty "The floor between the pews happens to need sweeping. Here is a broom. Remember, cleanliness is next to godliness my son!"
                scene churchcleanfloor with dissolve
                ty "I'll watch for a while and make sure you do your JOB properly."
                mc "Hey! I do this for FREE!"
                ty "You do it for the glory of the Phallus Lord! Alright, I have some more important things to do than watch some guy sweeping a floor. I'll see you at the end of the period, my son."
                if missionchurch and successchurch == False and failchurch == False and pencescroll == False:
                    scene churchscroll with dissolve
                    mc "What's that? Looks like some ancient scroll or something..."
                    window hide
                    show poncescroll at posmission
                    pause
                    hide poncescroll
                    $ pencescroll = True
                    mc "Interesting... It says that \"A Priest shall not remain alone in the same room with a woman or he will face Mother's Wrath.\""
                    mc "Not sure what it means but it might be useful for my mission...."
                    window hide
                    show achievementchurch at posmission
                    pause
                    hide achievementchurch
                    $ churchevidence += 1
                jump ChurchCleanEnd
            if d2rollchurch == 2:
                $ cleanedaltar = True
                ty "The altar happens to need a good rubbing. Here are some cloths. Remember, cleanliness is next to godliness my son!"
                label CleanAltarChurch:
                scene churchcleanaltar with dissolve
                ty "I'll watch for a while and make sure you do your JOB properly."
                mc "Hey! I do this for FREE!"
                ty "You do it for the glory of the Phallus Lord! Alright, I have some more important things to do than watch some guy cleaning an altar. I'll see you at the end of the period, my son."
                if holyoil == False:
                    scene churchoil with dissolve
                    mc "What's that? Looks like a small flask of something..."
                    window hide
                    show holybabyoil at posmission
                    pause
                    hide holybabyoil
                    $ holyoil = True                
                jump ChurchCleanEnd  
            label ChurchCleanEnd:
            scene church02
            show typr with fade
            mc "I'm done cleaning this place. It's spotless now. I hope I get something in return from... err... God. Like some money."
            ty "You will my son but not right now. In the After-Life... Thank you for your services and Jizz be with you."
            $ workchurch += 1
            if workchurch == 3:
                window hide
                call PlusChurch
                $ workchurch = 0
            $ period += 1
            hide typr with dissolve
            jump LeaveChurch       
    "I would like to get my cock canonized." if churchlore01 == True and churchbaptized == False:
        ty "I don't canonize any cock that barges in here willy-nilly. You must prove that your cock is worthy of Saint-Manhood."
        mc "And apart from stating its clearly godly size, what should I do?"
        ty "You can start by having your cock baptized so you can join the Church. That's just 10 dollars. Would you like to get baptized?"
        menu:
            "Pay 10$ and get baptized (+1 Church)" if money >= 10:
                $ money -= 10
                ty "Great, follow me to the Moist Crypt."
                jump Baptism01
            "Not now, I'll think about it Father.":
                ty "Fine. Jizz be with you my son."
                $ churchtygone = True
                jump Church01b
    "Nice church you have there Father. Shame if something were to happen to it.":
        hide tyne
        show tyan
        with fastdissolve
        ty "What are you insinuating?"
        mc "Hey, calm down Father. I'm just saying it's made of bricks and wood and wood burns, that's all."
        ty "Get out of here immediately you scoundrel! I shall not have my church defamed before the Great Phallus!"
        if mcchurch >= 1:
            call MinusChurch
        $ churchtygone = True
        jump LeaveChurch
    "I am thirsty for Church lore. Enlighten me Father." if churchlore02:
        hide tyne
        show tyha
        with fastdissolve
        ty "Hallelu-jizz! I am always happy to show the path to redemption that the Church offers to its flock!"
        hide tyha
        show typr
        with fastdissolve
        ty "The Church offers various services to redeem women AND men of their sins. For money most of the time."
        mc "I see. So it's really a commercial business..."
        hide typr
        show tyan 
        with fastdissolve
        ty "Certainly NOT! I am but a humble servant of the Phallus Lord!"
        mc "Alright, alright."        
        if churchbaptized == True:
            hide tyan
            show tyne
            with fastdissolve
            ty "Since you are baptized, it is time for you to repent your sins."
            mc "And how do I do that?"
            ty "A simple weekly visit to the confessional in the morning will be sufficient. I gather you are not a great sinner, being a boy after all."
            hide tyne
            show typr
            with fastdissolve
            ty "The sinful women of our World take much longer to repent THEIR deviations!"
            mc "Dirty, dirty sluts."
            hide typr
            show tyan
            with fastdissolve
            ty "Indeed. And they need to be severely punished for their misdeeds!"
            mc "Thank you for your enlightenment Father. I will leave you to your Holy Scriptures."
            hide tyan
            show tyne
            with fastdissolve
            ty "Jizz be with you my son."
            $ churchtygone = True
            $ churchlore04 = True
            $ period += 1
            jump LeaveChurch
        if churchbaptized == False:
            hide tyan
            show tyne
            with fastdissolve
            ty "Dare I say that's it probably time for you to get baptized and join the flock my son..."
            mc "Yeah, sure, I'll do that once I feel ready, I promise."
            ty "Jizz be with you my son."            
            $ churchtygone = True
            jump Church01b

label ConfessionalMorning:
scene church05 with dissolve
if churchlore04 == True and sinsconfessed == False and mcchurch >= 1:
    show tyne
    ty "Hello my son. Are you here to confess your sins to the All-Manly?"
    menu:
        "Yes I am Father. (-2 dollars)" if churchbaptized == True and money >=2:
            hide tyne
            show typr
            with fastdissolve
            ty "Good. Enter the right side of the confessional then. And pay the measly confessional fee of two New Dollars."
            $ money -= 2
            jump Confession
        "No, I'm good.":
            hide tyne
            show tyan
            with fastdissolve
            ty "You may THINK you're good, but you are a sinner! We all are sinners!"
            mc "Speak for yourself. I ain't done nothing bad."
            ty "Umpf. Clearly, you are not ready to be a true servant of the Church."
            if workchurch >= 1:
                ty "I am relieving you of your Church duties then. Until you accept that you ARE a sinner in the eyes of the Holy Spurt!"
                call MinusChurch
                $ workchurch = 0
            jump LeaveChurch
        "No, but I'll offer my humble services to clean and mop this filthy place." if missionchurch and successchurch == False and failchurch == False:
            hide tyne
            show tyrone05
            with fastdissolve
            ty "It is true that my church is dirty. Dirty from the SINS of this compound!"
            jump ChurchCleaning            
            
if churchlore04 == True and sinsconfessed:
    show tyne
    ty "I appreciate your enthusiasm in confessing your sins, but you already have done so this week. And a boy doesn't need to confess more often that that."
    hide tyne
    show tyan
    with fastdissolve
    ty "Women on the other hand... I need to see them EVERY DAY!"
    mc "Dirty, dirty sluts."
    ty "Indeed. And they need to be severely punished for their misdeeds!"
    mc "I wholecockedly agree!"
    hide tyan
    show tyne
    with fastdissolve
    ty "Jizz be with you my son."
    jump ChurchMorning01
show tyan
if mcchurch == 0:
    ty "This confessional is sacred ground and shall not be desecrated by a novice such as yourself!"
if mcchurch >= 1:
    ty "You do not know enough about Church Lore to be able to confess your sins. YET."
jump ChurchMorning01
        
label Confession:
scene church06a with dissolve
ty "I am listening my son."
mc "I have naughty thoughts."
scene church06b with fastdissolve
ty "We all do my son. You are a healthy young man, it is natural. Do you masturbate a lot?"
mc "Err... Yeah, maybe..."
scene church06a with fastdissolve
$ sinsconfessed = True
ty "With your right hand or your left hand?"
menu:
    "My left hand.":
        scene church06a with fastdissolve
        ty "That is good. It is the hand of the Jizz-Devil. The one that shall spill the Seed of God."
        window hide
        call PlusChurch
        mc "So we're all good then?"
        scene church06b with fastdissolve
        ty "Yes my son. But still, spend the rest of your time here praying. Jizz be with you."
        $ period += 1
        jump LeaveChurch        
    "My right hand.":
        scene church06c with fastdissolve
        ty "How dare you use the hand of God for such a vile act?"
        call MinusChurch
        mc "Well, I'm right-handed, it's much easier is all."
        scene church06a with fastdissolve
        ty "(sigh). I command you to read Santorum 6:9, the Sermon on the Capitol Hill. You will need to pray a LOT to repent your terrible sins my son!"
        mc "Gee, I didn't realize a quick wank was so taboo in the Church... Fine, I'll read your \"Holy passage\". Holy back passage, Santorum, got it?"
        scene church06c with fastdissolve
        ty "Do not take the teachings of the Church lightly! Go, I command thee!"
        scene church04 with dissolve
        "You spend the next few hours catching up on Santorum's back log. Back log, got it?"
        $ period += 1
        jump LeaveChurch
    "Both hands, I'm THAT big.":
        scene church06c
        ty "That still means you are using the hand of God for such a vile act! On top of being a bragger instead of showing humility."
        call MinusChurch
        mc "It's not my fault I'm hung like a horse Father!"
        scene church06a with fastdissolve
        ty "(sigh). I command you to read Santorum 6:9, the Sermon on the Capitol Hill. You will need to pray a LOT to repent your terrible sins my son!"
        mc "Gee, I didn't realize a quick wank was so taboo in the Church... Fine, I'll read your \"Holy passage\". Holy back passage, Santorum, got it?"
        scene church06c with fastdissolve
        ty "Do not take the teachings of the Church lightly! Go, I command thee!"
        scene church04 with dissolve
        "You spend the next few hours catching up on Santorum's back log. Back log, got it?" 
        $ period += 1
        if stonepiece06 == False and missionge:
            call screen churchstone
            screen churchstone:
                imagebutton:
                    focus_mask True
                    idle "Icons/exitidle.png"
                    hover "Icons/exithover.png"
                    action Jump ("LeaveChurch")
                if stonepiece06 == False and missionge:
                    imagebutton:
                        focus_mask True
                        idle "Icons/stone06idle.png"
                        hover "Icons/stone06hover.png"
                        action Jump ("StonePiece06")            
        jump LeaveChurch

label StonePiece06:
"You found one of the missing pieces of the Stone Artefact."
$ stonepieces -= 1
window hide
show achievementgenie at posmission
$ renpy.pause(0.5, hard=True)
show text "{font=Gui/Boogaloo-Regular.ttf}{color=#ff0000}{size=30}[stonepieces]{/font}" at StonePosition
$ renpy.pause(2.0, hard=True)
hide achievementgenie
$ stonepiece06 = True
jump LeaveChurch        

label ChurchClara01:
scene church03 with dissolve
label ChurchClara01b:
show stripclara01b
if spokecl == 0:
    cl "I am sister Clara, how may I help you?"
    menu:
        "Sister, I would like your opinion on my cock. Its worthiness for canonization if you will." if churchlore03 == False:
            cl "I am but a humble servant of the Church. Only the priest may grant such holy Saint-Manhood."
            mc "I get that, but I'd rather show YOU my cock than him. I mean, it's kind of gay."
            hide stripclara01b
            show stripclara02b
            with fastdissolve
            cl "Fear not, Priest Tyrone is a good man and... err... a good servant of the Church too. I should leave now..."
            hide stripclara02b with dissolve
            $ churchlore03 = True
            mc "(Mmh, she seemed embarrassed about something. But what could it be?)"            
            $ spokecl += 1
            $ churchclgone = True
            jump Church01b
        "What is your role in the Church?":
            cl "I assist Father Tyrone in his daily duties. And I pray. A LOT."
            menu:
                "That sounds kind of boring.":
                    hide stripclara01b
                    show clara06
                    with fastdissolve
                    cl "It may sound boring to YOU, but it is the Road to Salvation!"
                    mc "Alright, alright. I didn't mean to offend you."
                    cl "Now if you'll excuse me, I have some praying to do..."
                    window hide
                    $ spokecl += 1
                    $ churchclgone = True
                    hide clara06 with dissolve
                    jump Church01b                    
                "So you're a sister... Does that mean you're a virgin?":
                    hide stripclara01b
                    show clara04
                    with fastdissolve
                    cl "A virg.. Well, err... This is a rather PERSONAL question. Please go away."
                    mc "I was asking cos I need to build a har..."
                    hide clara04
                    show clara05
                    with fastdissolve
                    cl "I'm not interested. Just go away please!"
                    mc "Alright, Alright."
                    $ spokecl += 1
                    $ churchclgone = True
                    jump Church01b
                "Maybe we can pray together one day.":
                    hide stripclara01b
                    show clara03
                    with fastdissolve
                    cl "I would like that. But you first need to raise your standing in the Church."
                    mc "And how do I do that?"
                    cl "You should come to our Sunday services. And eventually, you could volunteer to help in some duties. Like cleaning..."
                    mc "Mmmh, well that doesn't sound too exciting."                    
                    hide clara03
                    show stripclara01b
                    with fastdissolve
                    cl "The Road to Salvation is long and hard."
                    mc "Long and hard. Long and hard. Where have I heard this phrase before?..."
                    hide stripclara01b
                    show clara03
                    with fastdissolve
                    cl "I will leave you to your thoughts. Bye [name]."
                    window hide
                    $ spokecl += 1
                    $ churchclgone = True
                    hide clara03 with dissolve
                    jump Church01b
        "Leave":
            jump Church01b
            
if spokecl >= 1:
    cl "Hello [name]. Would you like to pray with me today and repent your sins?"
    menu:
        "Of course, lead the way and lead me to the Holy Spurt." if mcchurch >= 4:
            $ prayinginarow += 1
            hide stripclara01b
            show clara03
            with fastdissolve
            cl "That's easy, the Holy Spurt is spurting everywhere. We can just pray here in the pews."
            mc "Why not in the crypt?"
            hide clara03
            show stripclara02b
            with fastdissolve
            cl "Err, no... That's off-limits... Maybe another time... Just kneel next to me and let's pray..."
            scene claramcpraying01 with fade
            cl "May the Holy Spurt bless us Oh Lord Phallus, and may It show us the the errors of our ways. Se-men."
            mc "Se-men."
            cl "Let's pray some more. Like for a full period basically."
            mc "Fine, Sister Clara."
            scene claramcpraying02 with fade
            ty "Fancy seeing you two in deep prayers here in the pews. Especially [name]. This young man is becoming one of our most devout students!"
            cl "Oh, thank you Father, I taught him some of our Lord's prayers and he has been a very ke..."
            scene claramcpraying03 with fastdissolve
            ty "Trying to redeem your terribles sins, Sister Clara? I fear THIS won't be enough."
            cl "... Yes, sorry Father, I am trying my best you know."
            ty "A sinful woman such as yourself can NEVER do what's best. Hallelu-Jizz!"
            cl "Ha...Hallelu-jizz."
            mc "Same here."
            $ tyroneseengmcpraying = True
            $ period += 1
            scene church03
            show stripclara01b
            with fade
            cl "Well thank you for being by my side while I prayed... I mean, WE prayed for the Phallus Lord's Forgiveness."
            if prayinginarow == 3:
                hide stripclara01b
                show clara03
                with dissolve
                cl "And for doing that THREE times already."
                call LustPlusClara
                mc "And thank you for teaching me some valuable prayers, Clara."
                cl "You're such a nice young man. *blush* Goodbye [name], I hope to see you again soon."
                window hide
                hide clara03 with dissolve
                $ prayinginarow = 0
                jump LeaveChurch            
            mc "And thank you for teaching me some valuable prayers, Clara."
            hide stripclara01b
            show clara03
            with fastdissolve
            cl "You're such a nice young man. *blush* Goodbye [name], I hope to see you again soon."
            window hide
            hide clara03 with dissolve
            jump LeaveChurch            
        "What is your role in the Church?":
            cl "I assist Father Tyrone in his daily duties. And I pray. A LOT."
            menu:
                "That sounds kind of boring.":
                    hide stripclara01b
                    show clara06
                    with fastdissolve
                    cl "It may sound boring to YOU, but it is the Road to Salvation!"
                    mc "Alright, alright. I didn't mean to offend you."
                    cl "Now if you'll excuse me, I have some praying to do..."
                    window hide
                    $ spokecl += 1
                    $ churchclgone = True
                    hide clara06 with dissolve
                    jump Church01b                    
                "So you're a sister... Does that mean you're a virgin?":
                    hide stripclara01b
                    show clara04
                    with fastdissolve
                    cl "A virg.. Well, err... This is a rather PERSONAL question. Please go away."
                    mc "I was asking cos I need to build a har..."
                    hide clara04
                    show clara05
                    with fastdissolve
                    cl "I'm not interested. Just go away please!"
                    mc "Alright, Alright."
                    window hide
                    $ spokecl += 1
                    $ churchclgone = True
                    hide clara05 with dissolve
                    jump Church01b
                "Maybe we can pray together one day.":
                    hide stripclara01b
                    show clara03
                    with fastdissolve
                    cl "I would like that. But you first need to raise your standing in the Church."
                    mc "And how do I do that?"
                    cl "You should come to our Sunday services. And eventually, you could volunteer to help in some duties. Like cleaning..."
                    mc "Mmmh, well that doesn't sound too exciting."                    
                    hide clara03
                    show stripclara01b
                    with fastdissolve
                    cl "The Road to Salvation is long and hard."
                    mc "Long and hard. Long and hard. Where have I heard this phrase before?..."
                    hide stripclara01b
                    show clara03
                    with fastdissolve
                    cl "I will leave you to your thoughts. Bye [name]."
                    window hide
                    $ spokecl += 1
                    $ churchclgone = True
                    hide clara03 with dissolve
                    jump Church01b
        "I have acquired a valuable relic. Which I would like to offer you as a sign of my religious devotion." if pubichair >= 1:
            hide stripclara01b
            show clara05
            with fastdissolve
            cl "Oh, it is so beautiful! A Holy Pubic Hair from the Phallus Lord Himself! Thank you so much [name], I will cherish it like...err... one cherishes a holy pubic hair."
            call LustPlusClara
            mc "You're welcome."
            $ pubichair -= 1
            hide clara05
            show clara03
            with fastdissolve
            cl "I will leave to pray with a Holy Pubic Hair in tow, I hope to see you again soon, \"[name] the Punisher\"!"
            $ period += 1
            jump LeaveChurch
        "I'd like to show you something (hypnotize her, +1 lust)" if pendulum and showedpendulum == False:
            call UsePendulum
            scene church03 blurred
            show stripclara01b
            with dissolve
            cl "Wh...what happened... The Phallus Lord is making me... wet myself."
            call LustPlusClara
            hide stripclara01b
            show clara04
            with fastdissolve
            cl "This is embarrassing. Sorry, I have to go [name]."
            $ showedpendulum = True
            $ spokecl += 1
            $ churchclgone = True
            $ period += 1
            jump LeaveChurch
        "I don't need to anymore. I have reached SAINT-MANHOOD!" if canonized and toldclaracanonized == False:
            hide stripclara01b
            show clara03
            with fastdissolve
            $ toldclaracanonized = True
            cl "Really? Wow, this is a sign that you are truly the Chosen One to accomplish your divine mission, whatever it is."
            call LustPlusClara
            mc "Indeed it is, indeed it is..."
            cl "You still need to pray though. I'll pray extra-hard for both you and me today as an exception!"
            hide clara03 with dissolve
            $ spokecl += 1
            $ churchclgone = True
            $ period += 1
            jump LeaveChurch
        "I would like to invite you on a date. At a holy and beautiful place actually." if lustcl >= 2 and claradatedone == False and knowredcanyon and claraquest == False:
            hide stripclara01b
            show clara03
            with fastdissolve
            cl "Oh? Where is that beautiful and Holy place [name]? Is it nearby? I cannot leave the church for too long, Father Tyrone would notice..."
            mc "It's real close don't worry. It has flowing water and... err... rocks. You should bring a swimsuit."
            hide clara03
            show stripclara02b
            with fastdissolve 
            cl "Erm, I don't have any... I'm a Sister, remember?"
            mc "Ah yes, sisters don't wear swimsuits. Damn."
            cl "I used to own one of course, but all my belongings from my previous life are locked in my \"Redemption Box\". And I don't know where Father Tyrone keeps it..."
            mc "I will find that box, I swear to the Phallus Lord!"
            window hide
            show missionclara at posmission
            $ renpy.pause(2.0, hard=True)
            pause
            hide missionclara            
            $ claraquest = True
            hide stripclara02b
            show clara04
            with fastdissolve 
            cl "Be careful with Father Tyrone. He must not know about this, he would get VERY angry."
            mc "Don't worry, I'll investigate discreetly."
            hide clara04
            show clara03
            with fastdissolve 
            cl "I put my trust in you then. And I'll go and pray for the success of your quest!"
            window hide
            hide clara03 with dissolve
            $ spokecl += 1
            $ churchclgone = True
            jump Church01b
        "I found your redemption box Clara!" if lustcl >= 2 and claradatedone == False and knowredcanyon and claraquestdone:
            hide stripclara01b
            show clara05
            with fastdissolve
            cl "Really? That is wonderful! Please tell me Father Tyrone doesn't know anything about this!"
            mc "Oh, he doesn't. Totally oblivious. You can get all your belongings back now. Including that swimsuit."
            $ claradateon = True
            hide clara05
            show clara03
            with fastdissolve
            cl "Which means you can now take me on that date to that beautiful place you talked about..."
            mc "You can read my mind... I'll pick you up in the morning, and we'll be back for lunchtime prayers without Father Tyrone being any the wiser!"
            cl "I can't wait for this! Thank you so much, [name]... *blush*"
            window hide
            hide clara03 with dissolve
            $ spokecl += 1
            $ churchclgone = True
            jump Church01b
        "I think it's time for you to join my harem, Clara." if lustcl >= 4 and haremcl == False and claraharem == False and girlsinharem <= 5 and claradatedone:
            hide stripclara01b
            show clara04
            with fastdissolve
            cl "I don't know, I am officially married to the Church. Wouldn't that be cheating?"
            mc "Are you having sex with the Church?"
            hide clara04
            show stripclara02b
            with fastdissolve
            cl "Well, no of course."
            mc "Then it's not cheating."
            hide stripclara02b
            show clara03
            with fastdissolve
            cl "You're so smart. I guess you're right. I accept then."            
            $ haremcl = True
            $ girlsinharem += 1
            $ claraharem = True
            window hide
            show haremclara at plus
            $ renpy.pause(2.0, hard=True)
            hide haremclara
            mc "I'll call you at nights and show you how the Phallus Lord has nothing on me when it comes to SIZE and POWER!"
            cl "Alright [name]."            
            window hide
            hide clara03 with dissolve
            jump LeaveChurch
        "Maybe it's time for you to re-join my harem... What do you say?" if lustcl >= 4 and haremcl == False and claraharem and claradismissed == False and girlsinharem <= 5:
            if mcchurch <= 4:
                hide stripclara01b
                show stripclara02b
                with fastdissolve            
                cl "Father Tyrone has instructed me to severe all social ties with lapsed members. Such as yourself."
                mc "What? I ain't lapsed! Or maybe I am, but it's a temporary lapse!"
                hide stripclara02b
                show clara04
                with fastdissolve            
                cl "Well, you can ask me again once you're back in favor with our Church... Sorry, [name]. I will pray for your redemption, since you clearly need it..."
                window hide
                hide clara04 with dissolve
                jump LeaveChurch
            hide stripclara01b
            show clara03
            with fastdissolve                    
            cl "Fine. Since you are still a decent and devout man, I know you will treat me well. Right?"
            $ haremcl = True
            $ girlsinharem += 1
            window hide
            show haremclara at plus
            $ renpy.pause(2.0, hard=True)
            hide haremclara
            mc "Of course. As well as...err... Father Tyrone himself treats you."
            cl "Alright [name]."            
            window hide
            hide clara03 with dissolve
            jump LeaveChurch            
        "Leave":
            jump LeaveChurch

label Baptism01:
scene crypt01 with dissolve
$ knowcrypt = True
show tyrone05 at midright
show clara03 at midleft
ty "What's your name young man?"
mc "[name]."
cl "That is such a lovely and holy name..."
ty "Alright, pull your penis out [name]."
mc "What? Why?"
ty "You want to get baptized? That's how the ceremony works..."
mc "Alright? I'll pull it out..."
play sound "Sounds/zipper.mp3"
hide tyrone05
show tyrone07 at midright
hide clara03
show clara05 at midleft
with fastdissolve
ty "What the fuck? Are you a mutant or something?"
mc "I received a healthy dose of alpha-radiations you could say. So, can I get baptized now?"
ty "Err... Sure. I'll start the ceremony. Sister Clara, hold his penis if you will while I perform the ritual."
hide clara05
show clara04 at midleft
with fastdissolve
cl "What? But this is so embarrassing Father..."
hide tyrone07
show tyrone04 at midright
with fastdissolve
ty "It's not like it's the first time you've held a cock, you sinning bitch. Get on with it!"
cl "At your pleasure... Father."
scene baptism01 with dissolve
mc "Don't be scared Sister Clara, It won't bite..."
cl "How do you even hold that thing?"
ty "Put your hand underneath it and lift it Sister. It needs to be facing the Heavens while I baptize [name]."
scene baptism02 with dissolve
mc "Uh Oh,... OK, I'm holding it Father."
ty "Do you reject Satan, and all his anal buggery?"
mc "Err.. Yes."
ty "Do you believe in the Holy Spurt, the Holy Phallic Church, the reserection of the Cock, and life everlasting?"
mc "Absolutely."
scene crypt03
show tyrone06
with dissolve
ty "In the name of the Father, the Son and the Holy Spurt, I baptized thy penis..."
cl "Se-men."
window hide
call PlusChurch
mc "That's it?"
hide tyrone06
show tyrone05
with fastdissolve
ty "That's it. What, you were expecting Sister Clara to give you a blowjob or something?"
mc "Well, it would have been nice for sure..."
ty "You can pull your pants back up young man. You are now officially a congregant of the Church of the Redeeming Phallus."
scene baptism03 with dissolve
cl "Uh-ooh... It's so big..."
$ churchbaptized = True
call LustPlusClara
mc "Thank you Father, I think I'd better get going then..."
$ period += 1
jump LeaveChurch

label ChurchNight:
if seenclaraflog == False:
    jump ChurchNight01
if seenclaraflog and seenaylacrypt == False:
    jump ChurchNight02
if seenclaraflog and seenaylacrypt:
    jump ChurchNight03
label ChurchNight01:
scene churchnight01 with dissolve
mc "It's spookily quiet."
if persistent.tipson:
    show church01tip at tips with dissolve
    pause
    hide church01tip
call screen churchnight
screen churchnight:
    imagebutton:
        focus_mask True
        idle "Icons/exitidle.png"
        hover "Icons/exithover.png"
        action Jump ("LeaveChurchNight")
    imagebutton:
        focus_mask True
        idle "Church/altarnightidle.png"
        hover "Church/altarnighthover.png"
        action Jump ("AltarNight")
    if knowcrypt == True:
        imagebutton:
            focus_mask True
            idle "Church/cryptnightidle.png"
            hover "Church/cryptnighthover.png"
            action Jump ("CryptNight")
    imagebutton:
        focus_mask True
        idle "Church/pewnightidle.png"
        hover "Church/pewnighthover.png"
        action Jump ("PewNight")

label LeaveChurchNight:
mc "Mission abort, I repeat, mission abort!"
scene bedroom01 with fade
mc "Let's go to sleep, it's super-late now, even too late to invite a girl."
jump MCsleep   

label AltarNight:
scene churchoil with dissolve
mc "Ah, some Holy Baby Oil. I might as well take it..."
if holyoil == False:
    window hide
    show holybabyoil at posmission
    pause
    hide holybabyoil
    $ holyoil = True  
window hide
play sound "Sounds/footsteps.mp3"
$ renpy.pause(2.0, hard=True)
scene altarnight with dissolve
mc "Oh shit, Father Tyrone is coming this way. Mission abort, mission abort!"
scene bedroom01 with fade
mc "Phew, that was close... Let's go to sleep, it's super-late now, even too late to invite a girl."
jump MCsleep

label CryptNight:
scene cryptdoorlocked with dissolve
mc "Ah, the door is locked and I don't have a key...."
jump ChurchNight01

label PewNight:
play sound "Sounds/footsteps.mp3"
scene cryptenter with fade
mc "Oh, oh, Father Tyrone and Sister Clara are entering the Moist Crypt. Let's follow them and hide in the shadows."
stop sound
scene cryptdooropen with dissolve
play sound "Sounds/doorsqueak.mp3"
mc "This door's hinges clearly need some WD-69."
stop sound
scene crypt01 with fade
mc "I found a good hiding place with a clear view of the crypt. What a stroke of luck. Thank you dev."
window hide
show clara10 with moveinleft
mc "Oh, Oh, Clara is wearing some rather naughty nun outfit..."
ty "Sister Clara, do you confess to your utter depravity?"
cl "Y.. Yes, Father."
ty "And do you know what is the punishment for sinning whores like you?"
hide clara10
show clara10b
with fastdissolve
cl "Y..Yes Father. But, I..."
ty "Silence! May the Phallus Lord have mercy on you, cos I sure won't. Assume your position for your Holy Flogging."
scene crypt05
show clara11
with dissolve
ty "I will administer your flogging in my Punisher outfit. As per the rules."
cl "But the rules say th..."
ty "Silence! I KNOW the rules, don't try and teach them to me! Now lift that fine ass higher to the Phallus Lord..."
hide clara11
show clara12
with dissolve
ty "That's better... What a shame it is to flog such a nice piece of booty..."
cl "Wh...What are you saying Father?"
ty "Tell you what, I will commute your punishment to Holy Spanking."
cl "I... never heard of this, Fath..."
hide clara12
show clara13
with dissolve
ty "Silence! The rules are clear, it's not my fault if you are an ignorant slut!"
hide clara13
show clara14
with fastdissolve
play sound "Sounds/slap.mp3"
ty "Take that, you depraved hussy!"
hide clara14
show clara13
with fastdissolve
cl "AAAH, you're hurting me Father!"
hide clara13
show clara14
with fastdissolve
play sound "Sounds/slap.mp3"
ty "And some more, devilishly tempting creature!"
hide clara14
show clara13
with fastdissolve
cl "AAAH, I repent, please stop!"
ty "Not good enough, get on my knees for a REAL spanking."
hide clara13
show clara15
with fastdissolve
ty "Yeah, that's nice..."
cl "But Father, I can feel your... thingie rubbing ag..."
hide clara15
show clara16
with fastdissolve
play sound "Sounds/slap.mp3"
ty "Silence while I spank you!"
hide clara16
show clara15
with fastdissolve
mc "It feels wrong. And kinda right at the same time knowing that crazy Church. I don't know what to make of it..."
hide clara15
show clara16
with fastdissolve
play sound "Sounds/slap.mp3"
ty "And don't you dare complain to the Cardinal, you hear me, nasty bitch?"
mc "Oh, oh, he's hiding something..."
window hide
show achievementchurch at posmission
pause
hide achievementchurch
$ churchevidence += 1
$ seenclaraflog = True
cl "AAAH! I... I promise, Father."
window hide
play sound "Sounds/drop.mp3"
$ renpy.pause(1.0, hard=True)
mc "Ah shit, I dropped a candelaber... Let's get the hell out of here quickly!"
stop sound
scene bedroom01 with fade
mc "Phew, that was close... Let's go to sleep, it's super-late now, even too late to invite a girl."
jump MCsleep                                                                        

label ChurchNight02:
scene churchnight01 with dissolve
mc "It's spookily quiet. Again."
if persistent.tipson:
    show church01tip at tips with dissolve
    pause
    hide church01tip
call screen churchnight02
screen churchnight02:
    imagebutton:
        focus_mask True
        idle "Icons/exitidle.png"
        hover "Icons/exithover.png"
        action Jump ("LeaveChurchNight")
    imagebutton:
        focus_mask True
        idle "Church/altarnightidle.png"
        hover "Church/altarnighthover.png"
        action Jump ("AltarNight02")
    if knowcrypt == True:
        imagebutton:
            focus_mask True
            idle "Church/cryptnightidle.png"
            hover "Church/cryptnighthover.png"
            action Jump ("CryptNight02")
    imagebutton:
        focus_mask True
        idle "Church/pewnightidle.png"
        hover "Church/pewnighthover.png"
        action Jump ("PewNight02")

label AltarNight02:
scene altarnight with dissolve
mc "Oh, oh, the Holy Baby Oil that's normally there is gone... Father Tyrone must be doing something with it, dirty old man."
mc "Oh shit, Father Tyrone is coming this way. Mission abort, mission abort!"
scene bedroom01 with fade
mc "Phew, that was close... Let's go to sleep, it's super-late now, even too late to invite a girl."
jump MCsleep

label CryptNight02:
scene cryptdoorlocked with dissolve
mc "Ah, the door is locked and I don't have a key...."
jump ChurchNight02

label PewNight02:
play sound "Sounds/footsteps.mp3"
scene aylacryptenter with fade
mc "Oh, oh, Father Tyrone and Ayla are entering the Moist Crypt. Let's follow them and hide in the shadows."
stop sound
scene cryptdooropen with dissolve
play sound "Sounds/doorsqueak.mp3"
$ renpy.pause(1.0, hard=True)
scene crypt01 with fade
stop sound
mc "I'm in position, let's wait for the sinners to sin..."
window hide
show aylacrypt01 at left with moveinleft
show tyronecrypt01 at right with moveinright
ay "Why did you call me here, Father? And why are dressed like a fucking PERVERT?"
ty "I'll tell you, I've noticed that you don't take part in communion and that you're always angry when I insist that you eat the Meat of the Phallus."
hide aylacrypt01
show aylacrypt02 at left
with fastdissolve
ay "Yeah, so , what's it to you? I'm a vegetarian!"
ty "No, my sweet little thing, you show all the signs that you are POSSESSED by a PUSSY-DEMONESS."
ay "WHAT???"
ty "And I need to perform an exorcism on your pussy as soon as possible before your soul is corrupted by this succubus from Hell."
hide aylacrypt02
show aylacrypt03 at left
with fastdissolve
ay "I'm possessed...  That's why I have been so unlucky in finding my boyfriend. I'm CURSED! What did I do to deserve this, Father?"
hide tyronecrypt01
show tyronecrypt02 at right
with fastdissolve
ty "We are all sinners, but you're a particular kind. You must follow my every order if you want to rid yourself of this devilish fiend inside your pussy!"
hide aylacrypt03
show aylacrypt01 at left
with fastdissolve
ay "And what do I have to do?"
ty "Take your lingerie off, the exorcism machine needs access to your intimate, but demon-possessed parts..."
ay "That sounds... disgusting!"
ty "It is the Devil that speaks through! OBEY, creature from HELL!"
hide aylacrypt01
show aylacrypt04 at left
with dissolve
ay "There, are you happy you fucking PERVERT FREAK?"
hide tyronecrypt02
show tyronecrypt01 at right
with fastdissolve
ty "Quite so, quite so Ayla... Now get in the machine."
ay "This had better not hurt. Or I'll head-punch you in the groin!"
scene crypt05
show ayladread03
with dissolve
ty "There... The machine will introduce a dildo blessed with Holy Baby Oil into your orifices now..."
ay "That's DISGUSTING!"
ty "Standard exorcism procedures, Ayla, I don't make the rules..."
ay "Go ahead with your filthy PERVERT machine then!"
scene crypt07
show ayladread04
with dissolve
play music "Sounds/vibrator.ogg"
ay "Ah, It's going too deep!"
scene crypt08
show ayladread02
with dissolve
ty "The demoness is lodged DEEP inside you, that's why! Just relax your muscles and let the Holy Spurt do the trick."
scene crypt07
label AylaCryptSlow:
hide aylacryptfast
show aylacryptslow
ty "The power of Jizz compels you. The power of Jizz compels you!"
call screen aylacryptslow01
screen aylacryptslow01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaCryptEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AylaCryptFast") 

label AylaCryptFast:
hide aylacryptslow
show aylacryptfast
ty "I'll increase the tempo now and raise my voice too. THE POWER OF JIZZ COMPELS YOU. THE POWER OF JIZZ COMPELS YOU!"
call screen aylacryptfast01
screen aylacryptfast01:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AylaCryptEnd")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AylaCryptSlow") 

label AylaCryptEnd:
stop music
hide aylacryptslow
hide aylacryptfast
show ayladreadend
play sound "Sounds/womanmoan.mp3"
ay "AAAH!"
ty "Good, you're expulsing the demoness, keep squirting Ayla!"
scene crypt05
show ayladread01
with dissolve
ty "Now let me check that it's not there anymore... With my fingers of course..."
mc "Cheeky bugger! I'm sure this whole ploy was just to stick his fingers up her cooch."
window hide
show achievementchurch at posmission
pause
hide achievementchurch
$ churchevidence += 1
$ seenaylacrypt = True
window hide
play sound "Sounds/drop.mp3"
$ renpy.pause(1.0, hard=True)
mc "Ah shit, I dropped a candelaber... Again. Let's get the hell out of here quickly!"
stop sound
scene bedroom01 with fade
if pencescroll == False:
    mc "I think I really need some hard material evidence to wrap this mission up. But where could I find that?"
if pencescroll:
    mc "What I've seen plus the hard evidence from those scrolls should be sufficient for Chief Lena I believe..."
mc "Let's go to sleep, it's super-late now, even too late to invite a girl."
jump MCsleep

label ChurchNight03:
scene churchnight01 with dissolve
mc "It's spookily quiet. Again."
call screen churchnight03
screen churchnight03:
    imagebutton:
        focus_mask True
        idle "Icons/exitidle.png"
        hover "Icons/exithover.png"
        action Jump ("LeaveChurchNight")
    imagebutton:
        focus_mask True
        idle "Church/altarnightidle.png"
        hover "Church/altarnighthover.png"
        action Jump ("AltarNight03")
    if knowcrypt == True:
        imagebutton:
            focus_mask True
            idle "Church/cryptnightidle.png"
            hover "Church/cryptnighthover.png"
            action Jump ("CryptNight03")
    imagebutton:
        focus_mask True
        idle "Church/pewnightidle.png"
        hover "Church/pewnighthover.png"
        action Jump ("PewNight03")

label AltarNight03:
scene churchoil with dissolve
mc "Ah, some Holy Baby Oil. I might as well take it..."
if holyoil:
    mc "Except I already have some, so I'll leave it there cos I have no use for two flasks, that's just TOO much holiness in one go."
    jump AltarNight03b
if holyoil == False:
    window hide
    show holybabyoil at posmission
    pause
    hide holybabyoil
    $ holyoil = True  
label AltarNight03b:
window hide
play sound "Sounds/footsteps.mp3"
$ renpy.pause(2.0, hard=True)
scene altarnight with dissolve
mc "Oh shit, Father Tyrone is coming this way. Mission abort, mission abort!"
scene bedroom01 with fade
mc "Phew, that was close... Let's go to sleep, it's super-late now, even too late to invite a girl."
jump MCsleep

label CryptNight03:
scene cryptdoorlocked with fade
mc "Ah, the door is locked and I don't have a key...."
jump ChurchNight03

label PewNight03:
scene cryptdoorlocked with fade
mc "Mmmh, it's getting really late and no one seems to be coming. What a waste of time this thing has been."
if pencescroll == False:
    mc "I think I really need some hard material evidence to wrap this mission up. But where could I find that?"
if pencescroll:
    mc "What I've seen plus the hard evidence from those scrolls should be sufficient for Chief Lena anyway I believe..."
scene bedroom01 with fade
mc "And now it's super-late, even too late to call a harem girl. So I'll go to sleep. Alone like a loser who just wasted his time hiding in pews for no reason."
jump MCsleep
    
label LeaveChurch:
scene church01c with dissolve
show church01crossidle
jump Main01





