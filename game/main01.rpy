label NewDay:
hide screen calendar
hide screen mcstats
stop sound
stop music
if loc == "medbay":
    scene medbay02
    show tara02
    show medbay02b
    with fade
    "You wake up the next day feeling much better."
    ta "Looks like you've recovered [name]. You are free to go. Actually, just go, you're costing us a fortune!"
    hide tara02 with dissolve 
    mc "I'd better get back to my bedroom and get some new clothes for the day..."
    $ loc = "bedroom"
$ day += 1    
$ period = 1
if day >= 8:
    $ week +=1
    $ day = 1
    if alienfuck == False and week >=3 and wave01explored and planetlifted == False:
        scene earth with dissolve
        pause
        play sound "Sounds/radiation01.mp3"
        $ renpy.pause(2, hard=True)
        scene earthdestroyed with dissolve
        stop sound
        play sound "Sounds/explosion.mp3"
        $ renpy.pause(2, hard=True)
        "You failed to provide the Glorglans with an adequate supply of porn vids and they destroyed the Earth. EPIC FAIL. THE END."
        menu:
            "Fine, I'll play by the game rules and I'll start over again until I don't screw up.":
                $ MainMenu(confirm=False)()
            "Let's pretend the Glorglans gave me an extra week...":
                stop sound
                pass
    scene bedroom01 with dissolve
    if exploredhex01 and exploredhex02 and exploredhex03 and week >= 2:
        $ wave01explored = True
    if exploredhex11 and exploredhex12 and exploredhex13 and exploredhex14 and exploredhex15 and exploredhex16 and exploredhex17 and week >= 4:
        $ wave02explored = True
    if exploredhex21 and exploredhex22 and exploredhex23 and exploredhex24 and exploredhex25 and exploredhex26 and exploredhex27 and week >= 6:
        $ wave03explored = True
    if exploredhex31 and exploredhex32 and exploredhex33 and exploredhex34 and exploredhex35 and exploredhex36 and week >= 8:
        $ wave04explored = True
    if exploredhex41 and exploredhex42 and exploredhex44 and exploredhex45 and exploredhex46 and week >= 11:
        $ wave05explored = True
    if exploredhex51 and renpy.seen_image("bunkerfar") and exploredhex53 and exploredhex54 and exploredhex55 and exploredhex56 and week >= 15:
        $ wave06explored = True
    if wave01explored == False and week >= 2:
        mc "It's the start of a new week! But it looks like I haven't explored all available areas in the vicinity of the compound."
        mc "I really should visit all of them  before moving out further. That should be my mission this week..."
    
    if week >= 26 and qanonwonfight == False and seenwarning == False:
        "You've been playing this game for 25 weeks now, which is past the official deadline at this stage."
        "If you want the game to continue and have more days, with more areas to explore and more sex and shit, please support the dev on Patreon!"
        $ seenwarning = True
        menu:
            "Ok, I'm done anyway, let's save my progress then.":
                call screen save()
            "Ok, I'm done anyway, I will immediately click on the dev's patreon page button (on the main menu) and give him shitloads of cash.":
                $ MainMenu(confirm=False)()
            "Ok, I'm done, but I enjoyed the game so far so I'll make the effort of pressing the \"Like\" button and maybe even write a review on the game's dedicated thread over at f95zone.com.":
                $ renpy.run(OpenURL('https://f95zone.to/threads/apocalypse-v0-4-epiclust.33875/'))
                $ MainMenu(confirm=False)()
            "Give me another week, I love grinding and I don't think I saw everything.":
                pass
    if week >= 31 and qanonwonfight and seenwarning02 == False:
        "You've been playing this game for 30 weeks now, which is past the official deadline at this stage."
        "If you want the game to continue and have more days, with more areas to explore and more sex and shit, please support the dev on Patreon!"
        $ seenwarning02 = True
        menu:
            "Ok, I'm done anyway, let's save my progress then.":
                call screen save()
            "Ok, I'm done anyway, I will immediately click on the dev's patreon page button (on the main menu) and give him shitloads of cash.":
                $ MainMenu(confirm=False)()
            "Ok, I'm done, but I enjoyed the game so far so I'll make the effort of pressing the \"Like\" button and maybe even write a review on the game's dedicated thread over at f95zone.com.":
                $ renpy.run(OpenURL('https://f95zone.to/threads/apocalypse-v0-4-epiclust.33875/'))
                $ MainMenu(confirm=False)()
            "Give me another week, I love grinding and I don't think I saw everything.":
                pass
    if bouquet >= 1:
        mc "Ah shit, that bouquet of wild flowers I picked the other day has now withered. It's useless a a gift..."
        $ bouquet = 0
    if churchattended == False and tyroneexplained:
        $ churchnotattended += 1
    if churchnotattended == 3:
        call MinusChurch
        mc "Ah, shit, I haven't been to Sunday service for a while and my standing in the Church has dropped..."
        $ churchnotattended = 0
    if mcstrength >= 16 and superstrength == False:
        $ mcstrength = 15
    if mcstrength >= 17 and superstrength:
        $ mcstrength = 16
    if mcfrench >= 11:
        $ mcfrench = 10
    if mccombat >= 11:
        $ mccombat = 10
    if mcfirearms >= 11:
        $ mcfirearms = 10
    if mcmechanics >= 11:
        $ mcmechanics = 10
    $ marnielustslave = False
    $ churchattended = False    
    $ zaradismissed = False
    $ angiedismissed = False
    $ momdismissed = False
    $ michikodismissed = False
    $ cyrldismissed = False
    $ rubydismissed = False
    $ amydismissed = False
    $ ayladismissed = False
    $ sukidismissed = False
    $ gwendismissed = False
    $ pennydismissed = False
    $ marniedismissed = False
    $ claradismissed = False
    $ lauriedismissed = False
    $ lenadismissed = False
    $ barbaradismissed = False
    $ debradismissed = False
    $ belladismissed = False
    $ impregnatedsomeone = False
    $ nancypoolbanged = False
    call HaremInterface
    if sawbirth:
        "You spent some time in the medbay this morning. Time has moved on..."
        $ period += 1
        $ sawbirth = False
    $ weekmomslept = False
    $ maintenanceza = False
    $ maintenancean = False
    $ maintenancemo = False
    $ maintenancemi = False
    $ maintenancecy = False
    $ maintenanceru = False
    $ maintenanceam = False
    $ maintenanceay = False
    $ maintenancesu = False
    $ maintenancegw = False
    $ maintenancepe = False
    $ maintenancema = False
    $ maintenancecl = False
    $ maintenancela = False
    $ maintenancele = False
    $ maintenanceba = False
    $ maintenancebe = False
    $ maintenancede = False
    $ askedbellajoin = False
    $ haremzararejoined = False
    $ seenweekwhitehousecall = False
    $ canuckdefeated = False
    $ weekschool = 0
    $ nightduties = 0
    $ worklab = 0
    $ alienfuck = False
    $ amybet = 0
    $ aylabet = 0
    $ lenabet = 0
    $ rubybet = 0
    $ michikobet = 0
    $ sukibet = 0
    $ d2rollfight = 0
    $ d2girlharem = 0
    $ sinsconfessed = False
    $ weekfuckedmichiko = False
    $ weekfuckedmom = False
    $ weekfuckedangie = False
    $ weekfuckedcyrl = False
    $ weekfuckedruby = False
    $ weekfuckedamy = False
    $ weekfuckedayla = False
    $ weekfuckedsuki = False
    $ weekfuckedgwen = False
    $ weekfuckedpenny = False
    $ weekfuckedmarnie = False
    $ weekfuckedclara = False
    $ weekfuckedlaurie = False
    $ weekfuckedlena = False
    $ weekfuckedbarbara = False
    $ weekfuckedbella = False
    $ weekfuckeddebra = False
    $ spokeruby02 = False
    $ seenmarago01 = False
    $ sukicheated = False
    $ boughtcocktailjake = False
    $ gottip = False
    $ spliffused = False
    $ cleanedaltar = False
    $ nancypoolbanged = False
    if pregto:
        $ pregtostart += 1
    $ nightwatchduty = 0
    $ gaveqautograph = False
    $ barbaranolust = False
$ ivankafirst = False
$ melaniafirst = False
$ askedbellajoin = False
$ fuckwithdiamond = False
$ marketseen = False
$ camelshot = False
$ camelcaptured = False
$ seenwhitehousecall = False
$ mcinjured = False
$ mcinjuredalien = False
$ mcinjuredmichiko = False
$ mcinjuredgun = False
$ mcinjuredsalad = False
$ mcinjuredopala = False
$ mcinjuredprisoner = False
$ mcinjuredsand = False
$ mcinjuredgwen = False
$ mcinjuredfight = False
$ mcinjuredtaser = False
$ mcinjuredfaint = False
$ mcinjuredjaguar = False
$ mcinjuredvirus = False
$ mcinjuredcurse = False
$ mcinjureddoor = False
$ mcinjuredstomach = False
$ mcinjuredmushroom = False
$ mcinjuredgator = False
$ mcinjuredfbi = False
$ mcinjuredcock = False
$ schoolmust = False
$ angiecosplayafternoon = False
$ angiecosplayevening = False
$ angieplayed = False
$ hippyfled = False
$ churchclgone = False
$ showedpendulum = False
$ mcwatch = False
$ claratitssaid = False
$ hex = 0
$ collectedstones = (8 - stonepieces)
$ totalgems = gem + hulkgem + aliendiamonds
$ beatqanon = False

$ nightduty = False

$ churchbegone = False
$ churchtygone = False

$ d6rollgym = renpy.random.randint(1, 6)
$ d3rollgymworkout = renpy.random.randint(1, 3)
$ jakelocker = False
$ d2rollwith = renpy.random.randint(1, 2)
$ d4rollbounty = renpy.random.randint(1, 4)

$ d6rollpool = renpy.random.randint(1, 6)

$ d6rollnightduty = renpy.random.randint(1, 6)
$ d2rollmedbay = renpy.random.randint(1, 2)

$ d4rollpennyexplore = renpy.random.randint(1, 4)

$ d2rollnancypool = renpy.random.randint(1, 2)

$ seenworkshop = False
$ seenpool = False
$ seenchurch = False
$ seengym = False
$ seenlab = False
$ seenbar = False
$ seencommand = False
$ seenfood = False
$ seendojo = False
$ seenshooting = False
$ seenschool = False
$ seenprisoner = False

$ aylagym = False
$ rubygym = False
$ lenagym = False
$ lauriegym = False
$ momgym = False
$ marniegym = False
$ seenlenagym = False
$ seenlauriegym = False
$ seenrubygym = False
$ seenaylagym = False
$ seenmomgym = False
$ seenmarniegym = False

$ aylagymout = False

$ bellapool = False
$ marniepool = False

$ seeninterface = False

$ spokeamy = False
$ spokeruby = False
$ explored = False
$ drunkcocktail = False

$ withbe = False
$ withpe = False
$ withmo = False
$ withcy = False
$ withan = False
$ withmi = False
$ withza = False
$ withru = False
$ witham = False
$ withay = False
$ withsu = False
$ withgw = False
$ withma = False
$ withcl = False
$ withla = False
$ withba = False
$ withde = False
$ mcwatch = False
$ withnone = False
$ alone = False
$ withmarvel = False

$ seennoticechurch = False
$ seennoticeprisoner = False

$ mcbikebought = False

if period == 1 and missionprisoner == True and successprisoner == False and failprisoner == False and daysprisoner <=3 and seennoticeprisoner == False:
    $ daysprisoner -= 1
    window hide
    show missionprisoner at posmission
    $ renpy.pause(1.0, hard=True)
    show text "{font=Gui/Boogaloo-Regular.ttf}{color=#ff0000}{size=35}[daysprisoner]{/font}" at ChurchPosition
    pause
    hide missionprisoner
    hide text
    $ seennoticeprisoner = True
if period == 1 and missionchurch == True and successchurch == False and failchurch == False and dayschurch <= 3 and seennoticechurch == False:
    $ dayschurch -= 1
    window hide
    if dayschurch >= 1:
        show missionchurch at posmission
        $ renpy.pause(1.0, hard=True)
        show text "{font=Gui/Boogaloo-Regular.ttf}{color=#ff0000}{size=35}[dayschurch]{/font}" at ChurchPosition
        pause
        hide missionchurch
        hide text
    $ seennoticechurch = True

show screen calendar
show screen mcstats
return

label Main01:
stop music

if period == 2 and angiecosplayafternoon:
    jump AngieCosplay
if period == 3 and angiecosplayevening:
    jump AngieCosplay
    
if mcinjured and michikodateon:
    mc "Shit, I have a date with Michiko tonight normally, I should cancel since I have to go to the medbay..."
    $ michikodatecancelled = True
    jump Medbay

if mcinjured:
    jump Medbay

if period == 1 and sukidateon and sukidatedone == False and (angiedateon or amydateon or lenadateon or marniedateon or pennydateon or claradateon or ayladateon or gwendateon or lenadateon or barbaradateon):
    mc "Shit, it appears I have several dates at the same time, I'll have to cancel one of them. I'll go with Suki as a first choice cos it was promise I made. First I'll take a shower."
    if angiedateon:
        $ angiedateon = False
    if amydateon:
        $ amydateon = False
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to see that nerdy-yet-hot Suki..." 
    jump SukiDate

if period == 1 and sukidateon and sukidatedone == False :
    mc "I should get ready for my date with Suki... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to see that nerdy-yet-hot Suki..." 
    jump SukiDate

if period == 1 and angiedateon and angiedatedone == False:
    mc "I should get ready for my date with Angie... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to see that naive Angie..." 
    jump AngieDate

if period == 1 and amydateon and amydatedone == False:
    mc "Ah, I have a date with Amy on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Amy to take her to the Red Canyon then..." 
    jump AmyDate

if period == 1 and ayladateon and ayladatedone == False:
    mc "Ah, I have a date with Ayla on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Ayla to take her to the Red Canyon then..." 
    jump AylaDate

if period == 1 and rubydateon and rubydatedone == False:
    mc "Ah, I have a date with Ruby on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Ruby to take her to the Red Canyon then..." 
    jump RubyDate

if period == 1 and gwendateon and gwendatedone == False:
    mc "Ah, I have a date with Gwen on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Gwen to take her to the Red Canyon then..." 
    jump GwenDate

if period == 1 and pennydateon and pennydatedone == False:
    mc "Ah, I have a date with Penny on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Penny to take her to the Red Canyon then..." 
    jump PennyDate

if period == 1 and lenadateon and lenadatedone == False:
    mc "Ah, I have a date with Chief Lena on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Lena to take her to the Red Canyon then..." 
    jump LenaDate

if period == 1 and claradateon and claradatedone == False:
    mc "Ah, I have a date with Sister Clara on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Clara to take her to the Red Canyon then..." 
    jump ClaraDate

if period == 1 and lauriedateon and lenadatedone == False:
    mc "Ah, I have a date with Laurie on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Laurie to take her to the Red Canyon then..." 
    jump LaurieDate

if period == 1 and barbaradateon and barbaradatedone == False:
    mc "Ah, I have a date with Barbara on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Barabra to take her to the Red Canyon then..." 
    jump BarbaraDate

if period == 1 and belladateon and belladatedone == False:
    mc "Ah, I have a date with Bellaa on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Bellaa to take her to the Red Canyon then..." 
    jump BellaDate

if period == 1 and debradateon and debradatedone == False:
    mc "Ah, I have a date with Debra on this beautiful morning.... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to meet Debra to take her to the Red Canyon then..." 
    jump DebraDate

if period == 4:
    mc "Ah, it's late, I'd better go back to my bedroom..."
    jump Bedroom
if period == 5:
    $ period = 4
    mc "Ah, it's late, I'd better go back to my bedroom..."
    jump Bedroom

if period == 2 and explored == False and (not (day == 6 or day == 7)):
    call screen mustexplore
    screen mustexplore:
        modal True
        imagebutton:
            focus_mask True
            idle "Icons/commandmust.png"
            hover "Icons/commandmust.png"
            action Jump ("CommandExplore")

if period == 1 and day == 4 and weekschool == 0:
    mc "Oh, oh, looks like I've been skipping school this week, I need to go there pronto..."
    $ schoolmust = True
    call screen mustclassa
    screen mustclassa:
        modal True
        imagebutton:
            focus_mask True
            idle "Icons/schoolmust.png"
            hover "Icons/schoolmust.png"
            action Jump ("School")
if period == 1 and day == 5 and weekschool <= 1:
    mc "Oh, oh, looks like I've been skipping school this week, I need to go there pronto..."
    $ schoolmust = True
    call screen mustclassb
    screen mustclassb:
        modal True
        imagebutton:
            focus_mask True
            idle "Icons/schoolmust.png"
            hover "Icons/schoolmust.png"
            action Jump ("School")

if period == 3 and (michikodateon or michikodateontomorrow):
    mc "I should get ready for my date with Michiko... First I'll take a shower."
    scene mcshowering with dissolve
    play music "Sounds/shower.mp3"
    mc "Yeah, that's nice... And now off to see busty Michiko..." 
    jump MichikoDate

call screen mainchoice
screen mainchoice:
    modal True    
    if period <= 3:
        imagebutton:
            focus_mask True
            idle "v061/passtime.png"
            hover "v061/passtime.png"
            action [SetVariable("period", period+1), Jump ("Main01")]
    if not loc == "bedroom":
        imagebutton:
            focus_mask True
            idle "Icons/bedroomidle.png"
            hover "Icons/bedroomhover.png"
            action Jump ("Bedroom")
    imagebutton:
        focus_mask True
        idle "Icons/baridle.png"
        hover "Icons/barhover.png"
        action Jump ("Bar")
    if seenpool == False:
        imagebutton:
            focus_mask True
            idle "Icons/poolidle.png"
            hover "Icons/poolhover.png"
            action Jump ("Pool")
    imagebutton:
        focus_mask True
        idle "Icons/commandidle.png"
        hover "Icons/commandhover.png"
        action Jump ("Command")
    if seengym == False:
        imagebutton:
            focus_mask True
            idle "Icons/gymidle.png"
            hover "Icons/gymhover.png"
            action Jump ("Gym")
    if seenchurch == False:
        imagebutton:
            focus_mask True
            idle "Icons/churchidle.png"
            hover "Icons/churchhover.png"
            action Jump ("Church")
    if seenlab == False:
        imagebutton:
            focus_mask True
            idle "Icons/labidle.png"
            hover "Icons/labhover.png"
            action Jump ("Lab")
    if seenschool == False and period <= 2 and not (day == 6 or day == 7):
        imagebutton:
            focus_mask True
            idle "Icons/schoolidle.png"
            hover "Icons/schoolhover.png"
            action Jump ("School")
    if seendojo == False:
        imagebutton:
            focus_mask True
            idle "Icons/dojoidle.png"
            hover "Icons/dojohover.png"
            action Jump ("Dojo")
    if seenworkshop == False and period <= 3:
        imagebutton:
            focus_mask True
            idle "Icons/workshopidle.png"
            hover "Icons/workshophover.png"
            action Jump ("Workshop")
    if seenfood == False and period <= 2:
        imagebutton:
            focus_mask True
            idle "Icons/foodidle.png"
            hover "Icons/foodhover.png"
            action Jump ("FoodUnit")
    if seenworkshop == True:
        add "Icons/workshopnone.png"
    if seengym == True:
        add "Icons/gymnone.png"
    if seenfood == True:
        add "Icons/foodnone.png"
    if seenpool == True:
        add "Icons/poolnone.png"
    if seenlab == True:
        add "Icons/labnone.png"
    if seenchurch == True:
        add "Icons/churchnone.png"
    if seendojo == True:
        add "Icons/dojonone.png"
    if seenschool == True:
        add "Icons/schoolnone.png"
    if seenfood == True:
        add "Icons/foodnone.png"
    if period >= 3 or day == 6 or day == 7:
        add "Icons/schoolnone.png"
    if period >= 3:
        add "Icons/foodnone.png"    

label CommandExplore:
scene command02 with dissolve
show lena06
show commandtable
le "Ah, there you are! Just in time for a scouting mission. Have a look at the map and choose an area to explore."
jump ExploringMap

label MCInjury:
window hide
show mcinjured at injured
play sound "Sounds/panting.mp3"
$ renpy.pause(2.0, hard=True)
hide mcinjured
$ mcinjured = True
return

label PlusTrumpster:
if mctrumpster <= 4:
    window hide
    show plustrumpster at posmission
    $ renpy.pause(2.0, hard=True)
    hide plustrumpster
    $ mctrumpster += 1
    if mctrumpster == 5:
        if mcdeep == 5 or mcsierra == 5 or mcchurch == 5 or mcwarrior == 5:
            menu:
                "Adopt Trumpsters Faction (leave previous faction)":
                    if mcdeep == 5:
                        call MinusDeep        
                    if mcsierra == 5:
                        call MinusSierra
                    if mcwarrior == 5:
                        call MinusWarrior
                    if mcchurch == 5:
                        call MinusChurch
                    call FactionTrumpster
                    return
                "Stay with your current faction (-1 Trumpsters)":
                    call MinusTrumpster
                    return
        call FactionTrumpster
return

label PlusSierra:
if mcsierra <= 4:
    window hide
    show plussierra at posmission
    $ renpy.pause(2.0, hard=True)
    hide plussierra
    $ mcsierra += 1
    if mcsierra == 5:
        if mcdeep == 5 or mctrumpster == 5 or mcchurch == 5 or mcwarrior == 5:
            menu:
                "Adopt Sierra Club Faction (leave previous faction)":
                    if mcdeep == 5:
                        call MinusDeep
                    if mctrumpster == 5:
                        call MinusTrumpster
                    if mcwarrior == 5:
                        call MinusWarrior 
                    if mcchurch == 5:
                        call MinusChurch 
                    call FactionSierra
                    return
                "Stay with your current faction (-1 Sierra Club)":
                    call MinusSierra
                    return
        call FactionSierra
return

label PlusWarrior:
if mcwarrior <= 4:
    window hide
    show pluswarrior at posmission
    $ renpy.pause(2.0, hard=True)
    hide pluswarrior
    $ mcwarrior += 1
    if mcwarrior == 5:
        if mcdeep == 5 or mctrumpster == 5 or mcchurch == 5 or mcsierra == 5:
            menu:
                "Adopt Road Warriors Faction (leave previous faction)":
                    if mcdeep == 5:
                        call MinusDeep 
                    if mctrumpster == 5:
                        call MinusTrumpster
                    if mcsierra == 5:
                        call MinusSierra
                    if mcchurch == 5:
                        call MinusChurch
                    call FactionWarrior
                    return
                "Stay with your current faction (-1 Road Warriors)":
                    call MinusWarrior
                    return
        call FactionWarrior
return

label PlusChurch:
if mcchurch <= 4:
    window hide
    show pluschurch at posmission
    $ renpy.pause(2.0, hard=True)
    hide pluschurch
    $ mcchurch += 1
    if mcchurch == 5:
        if mcdeep == 5 or mctrumpster == 5 or mcsierra == 5 or mcwarrior == 5:
            menu:
                "Adopt Church of the Redeeming Phallus Faction (leave previous faction)":
                    if mcdeep == 5:
                        call MinusDeep
                    if mctrumpster == 5:
                        call MinusTrumpster
                    if mcwarrior == 5:
                        call MinusWarrior
                    if mcsierra == 5:
                        call MinusSierra
                    call FactionChurch
                    return
                "Stay with your current faction (-1 Church of the Reeeming Phallus)":
                    call MinusChurch
                    return
        call FactionChurch
return

label PlusDeep:
if mcdeep <= 4:
    window hide
    show plusdeep at posmission
    $ renpy.pause(2.0, hard=True)
    hide plusdeep
    $ mcdeep += 1
    if mcdeep == 5:
        if mcsierra == 5 or mctrumpster == 5 or mcchurch == 5 or mcwarrior == 5:
            menu:
                "Adopt Deep State Faction (leave previous faction)":
                    if mctrumpster == 5:
                        call MinusTrumpster    
                    if mcsierra == 5:
                        call MinusSierra
                    if mcwarrior == 5:
                        call MinusWarrior
                    if mcchurch == 5:
                        call MinusChurch
                    call FactionDeep
                    return
                "Stay with your current faction (-1 Deep State)":
                    call MinusDeep
                    return
        call FactionDeep
return

label PlusDeepReal:
window hide
show plusdeep at posmission
$ renpy.pause(2.0, hard=True)
hide plusdeep
$ mcdeep += 1
if mcdeep == 5:
    call FactionDeep
    if mcchurch == 5:
        call MinusChurch
    if mctrumpster == 5:
        call MinusTrumpster
    if mcwarrior == 5:
        call MinusWarrior
    if mcsierra == 5:
        call MinusSierra
return

label PlusChurchReal:
window hide
show pluschurch at posmission
$ renpy.pause(2.0, hard=True)
hide pluschurch
$ mcchurch += 1
if mcchurch == 5:
    call FactionChurch
    if mcdeep == 5:
        call MinusDeep
    if mctrumpster == 5:
        call MinusTrumpster
    if mcwarrior == 5:
        call MinusWarrior
    if mcsierra == 5:
        call MinusSierra
return

label PlusTrumpsterReal:
window hide
show plustrumpster at posmission
$ renpy.pause(2.0, hard=True)
hide plustrumpster
$ mctrumpster += 1
if mctrumpster == 5:
    call FactionTrumpster
    if mcdeep == 5:
        call MinusDeep
    if mcchurch == 5:
        call MinusChurch
    if mcwarrior == 5:
        call MinusWarrior
    if mcsierra == 5:
        call MinusSierra
return

label PlusWarriorReal:
window hide
show pluswarrior at posmission
$ renpy.pause(2.0, hard=True)
hide pluswarrior
$ mcwarrior += 1
if mcwarrior == 5:
    call FactionWarrior
    if mcdeep == 5:
        call MinusDeep
    if mcchurch == 5:
        call MinusChurch
    if mctrumpster == 5:
        call MinusTrumpster
    if mcsierra == 5:
        call MinusSierra
return

label MinusTrumpster:
if mctrumpster >= 1:
    window hide
    show minustrumpster at posmission
    $ renpy.pause(2.0, hard=True)
    hide minustrumpster
    $ mctrumpster -= 1
return

label MinusSierra:
if mcsierra >= 1:
    window hide
    show minussierra at posmission
    $ renpy.pause(2.0, hard=True)
    hide minussierra
    $ mcsierra -= 1
return

label MinusWarrior:
if mcwarrior >= 1:
    window hide
    show minuswarrior at posmission
    $ renpy.pause(2.0, hard=True)
    hide minuswarrior
    $ mcwarrior -= 1
return

label MinusChurch:
if mcchurch >= 1:
    window hide
    show minuschurch at posmission
    $ renpy.pause(2.0, hard=True)
    hide minuschurch
    $ mcchurch -= 1
return

label MinusDeep:
if mcdeep >= 1:
    window hide
    show minusdeep at posmission
    $ renpy.pause(2.0, hard=True)
    hide minusdeep
    $ mcdeep -= 1
return

label FactionTrumpster:
window hide
play sound "Sounds/faction.mp3"
show factiontrumpster at posnewfaction
$ renpy.pause(3.0, hard=True)
mc "Hail to the Commander-in-Chief! TRUTH IS NOT TRUTH!"
hide factiontrumpster
return
    
label FactionChurch:
window hide
play sound "Sounds/faction.mp3"
show factionchurch at posnewfaction
$ renpy.pause(3.0, hard=True)
mc "Hallelu-Jizz! I have seen the Light of the Saviour Phallus!"
hide factionchurch
return
    
label FactionSierra:
window hide
play sound "Sounds/faction.mp3"
show factionsierra at posnewfaction
$ renpy.pause(3.0, hard=True)
mc "I am ONE with MOTHER NATURE! I shall worship her giant bosom!"
hide factionsierra
return
    
label FactionWarrior:
window hide
play sound "Sounds/faction.mp3"
show factionwarrior at posnewfaction
$ renpy.pause(3.0, hard=True)
mc "The Road is my Soul! Its soul is my Road! BURN AND PILLAGE!"
hide factionwarrior
return
    
label FactionDeep:
window hide
play sound "Sounds/faction.mp3"
show factiondeep at posnewfaction
$ renpy.pause(3.0, hard=True)
mc "The Shadow is my Weapon to CONTROL THE WORLD!"
hide factiondeep
return

label LustPlusAmy:
if lustam<=4:
    $ lustam += 1
    window hide
    show lustplusam at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplusam
return

label LustMinusAmy:
if lustam>=1:
    $ lustam -= 1
    window hide
    show lustminusam at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminusam
return

label LustPlusAngie:
if lustan<=4:
    $ lustan += 1
    window hide
    show lustplusan at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplusan
return

label LustMinusAngie:
if lustan>=1:
    $ lustan -= 1
    window hide
    show lustminusan at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminusan
return

label LustPlusAyla:
if lustay<=4:
    $ lustay += 1
    window hide
    show lustplusay at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplusay
return

label LustMinusAyla:
if lustay>=1:
    $ lustay -= 1
    window hide
    show lustminusay at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminusay
return

label LustPlusBarbara:
if lustba<=4:
    $ lustba += 1
    window hide
    show lustplusba at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplusba
return

label LustMinusBarbara:
if lustba>=1:
    $ lustba -= 1
    window hide
    show lustminusba at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminusba
return

label LustPlusBella:
if lustbe<=4:
    $ lustbe += 1
    window hide
    show lustplusbe at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplusbe
return

label LustMinusBella:
if lustbe>=1:
    $ lustbe -= 1
    window hide
    show lustminusbe at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminusbe
return

label LustPlusClara:
if lustcl<=4:
    $ lustcl += 1
    window hide
    show lustpluscl at plus
    $ renpy.pause(2.0, hard=True)
    hide lustpluscl
return

label LustMinusClara:
if lustcl>=1:
    $ lustcl -= 1
    window hide
    show lustminuscl at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminuscl
return
    
label LustPlusCyrl:
if lustcy<=4:
    $ lustcy += 1
    window hide
    show lustpluscy at plus
    $ renpy.pause(2.0, hard=True)
    hide lustpluscy
return

label LustMinusCyrl:
if lustcy>=1:
    $ lustcy -= 1
    window hide
    show lustminuscy at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminuscy
return

label LustPlusDebra:
if lustde<=4:
    $ lustde += 1
    window hide
    show lustplusde at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplusde
return

label LustPlusDebra02:
if lustde==4:
    $ lustde += 1
    window hide
    show lustplusde at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplusde
if lustde<=3:
    $ lustde += 2
    window hide
    show lustplustwode at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplustwode
return

label LustMinusDebra:
if lustde>=1:
    $ lustde -= 1
    window hide
    show lustminusde at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminusde
return

label LustPlusGwen:
if lustgw<=4:
    $ lustgw += 1
    window hide
    show lustplusgw at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplusgw
return

label LustMinusGwen:
if lustgw>=1:
    $ lustgw -= 1
    window hide
    show lustminusgw at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminusgw
return

label LustPlusIvanka:
if lustiv<=4:
    $ lustiv += 1
    window hide
    show lustplusiv at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplusiv
return

label LustMinusIvanka:
if lustiv>=1:
    $ lustiv -= 1
    window hide
    show lustminusiv at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminusiv
return

label LustPlusLaurie:
if lustla<=4:
    $ lustla += 1
    window hide
    show lustplusla at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplusla
return

label LustMinusLaurie:
if lustla>=1:
    $ lustla -= 1
    window hide
    show lustminusla at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminusla
return

label LustPlusLena:
if lustle<=4:
    $ lustle += 1
    window hide
    show lustplusle at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplusle
return

label LustMinusLena:
if lustle>=1:
    $ lustle -= 1
    window hide
    show lustminusle at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminusle
return

label LustPlusMarnie:
if lustma<=4:
    $ lustma += 1
    window hide
    show lustplusma at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplusma
return

label LustMinusMarnie:
if lustma>=1:
    $ lustma -= 1
    window hide
    show lustminusma at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminusma
return

label LustPlusMichiko:
if lustmi<=4:
    $ lustmi += 1
    window hide
    show lustplusmi at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplusmi
return

label LustMinusMichiko:
if lustmi>=1:
    $ lustmi -= 1
    window hide
    show lustminusmi at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminusmi
return

label LustPlusPenny:
if lustpe<=4:
    $ lustpe += 1
    window hide
    show lustpluspe at plus
    $ renpy.pause(2.0, hard=True)
    hide lustpluspe
return

label LustMinusPenny:
if lustpe>=1:
    $ lustpe -= 1
    window hide
    show lustminuspe at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminuspe
return


label LustPlusRachel:
if lustra<=4:
    $ lustra += 1
    window hide
    show lustplusra at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplusra
return

label LustMinusRachel:
if lustra>=1:
    $ lustra -= 1
    window hide
    show lustminusra at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminusra
return

label LustPlusRuby:
if lustru<=4:
    $ lustru += 1
    window hide
    show lustplusru at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplusru
return

label LustMinusRuby:
if lustru>=1:
    $ lustru -= 1
    window hide
    show lustminusru at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminusru
return

label LustPlusSuki:
if lustsu<=4:
    $ lustsu += 1
    window hide
    show lustplussu at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplussu
return

label LustMinusSuki:
if lustsu>=1:
    $ lustsu -= 1
    window hide
    show lustminussu at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminussu
return

label LustPlusTara:
if lustta<=4:
    $ lustta += 1
    window hide
    show lustplusta at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplusta
return

label LustMinusTara:
if lustta>=1:
    $ lustta -= 1
    window hide
    show lustminusta at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminusta
return

label LustPlusWidow:
if lustwi<=4:
    $ lustwi += 1
    window hide
    show lustpluswi at plus
    $ renpy.pause(2.0, hard=True)
    hide lustpluswi
return

label LustMinusWidow:
if lustwi>=1:
    $ lustwi -= 1
    window hide
    show lustminuswi at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminuswi
return

label LustPlusZara:
if lustza<=4:
    $ lustza += 1
    window hide
    show lustplusza at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplusza
return

label LustMinusZara:
if lustza>=1:
    $ lustza -= 1
    window hide
    show lustminusza at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminusza
return

label LustPlusMelania:
if lustme<=4:
    $ lustme += 1
    window hide
    show lustplusme at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplusme
return

label LustMinusMelania:
if lustme>=1:
    $ lustme -= 1
    window hide
    show lustminusme at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminusme
return

label LustPlusTaylor:
if lustto<=4:
    $ lustto += 1
    window hide
    show lustplusto at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplusto
return

label LustMinusTaylor:
if lustto>=1:
    $ lustto -= 1
    window hide
    show lustminusto at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminusto
return

label LustPlusWendy:
if lustwe<=4:
    $ lustwe += 1
    window hide
    show lustpluswe at plus
    $ renpy.pause(2.0, hard=True)
    hide lustpluswe
return

label LustMinusWendy:
if lustwe>=1:
    $ lustwe -= 1
    window hide
    show lustminuswe at minus
    $ renpy.pause(2.0, hard=True)
    hide lustminuswe
return
    
label LustPlusKimberly:
if lustkg<=4:
    $ lustkg += 1
    window hide
    show lustpluskg at plus
    $ renpy.pause(2.0, hard=True)
    hide lustpluskg
return

label LustPlusSukYu:
if lustsy<=4:
    $ lustsy += 1
    window hide
    show lustplussy at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplussy
return

label LustPlusHeather:
if lusthe<=4:
    $ lusthe += 1
    window hide
    show lustplushe at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplushe
return

label LustPlusKrista:
if lustkr<=4:
    $ lustkr += 1
    window hide
    show lustpluskr at plus
    $ renpy.pause(2.0, hard=True)
    hide lustpluskr
return

label LustPlusPaulette:
if lustqu<=4:
    $ lustqu += 1
    window hide
    show lustplusqu at plus
    $ renpy.pause(2.0, hard=True)
    hide lustplusqu
return

label FriendPlusJake:
if jakefriend<=5:
    $ jakefriend += 1
    window hide
    show jakefriendplus at plus
    $ renpy.pause(.5, hard=True)
    show text "{font=Gui/Boogaloo-Regular.ttf}{color=#ff0000}{size=35}[jakefriend]{/font}" at JakePlusPosition    
    pause
    hide text
    hide jakefriendplus
return

label FriendMinusJake:
if jakefriend>=1:
    $ jakefriend -= 1
    window hide
    show jakefriendminus at minus
    $ renpy.pause(.5, hard=True)
    show text "{font=Gui/Boogaloo-Regular.ttf}{color=#ff0000}{size=35}[jakefriend]{/font}" at JakeMinusPosition    
    pause
    hide text
    hide jakefriendminus    
return

label LenaDateConvince:
$ lenaconvincedate += 1
window hide
show lenadateconvincing at posskill
$ renpy.pause(1.0, hard=True)
pause
hide lenadateconvincing
return

label PlusStrength:
if mcstrength <= 14:
    $ mcstrength += 1
    window hide
    play sound "Sounds/skill.mp3"
    show plusstrength at posskill
    $ renpy.pause(2.0, hard=True)
    hide plusstrength
return

label PlusMechanics:
if mcmechanics <= 9:
    $ mcmechanics += 1
    window hide
    play sound "Sounds/skill.mp3"
    show plusmechanics at posskill
    $ renpy.pause(2.0, hard=True)
    hide plusmechanics
return

label PlusCombat:
if mccombat <= 9:
    $ mccombat += 1
    window hide
    play sound "Sounds/skill.mp3"
    show pluscombat at posskill
    $ renpy.pause(2.0, hard=True)
    hide pluscombat
return

label PlusFirearms:
if mcfirearms <= 9:
    $ mcfirearms += 1
    window hide
    play sound "Sounds/skill.mp3"
    show plusfirearms at posskill
    $ renpy.pause(2.0, hard=True)
    hide plusfirearms
return

label PlusFrench:
if mcfrench <= 9:
    $ mcfrench += 1
    window hide
    play sound "Sounds/skill.mp3"
    show plusfrench at posskill
    $ renpy.pause(2.0, hard=True)
    hide plusfrench
return

label PlusMaxFrench:
    $ frenchovermax += 1
    window hide
    play sound "Sounds/skill.mp3"
    show plusfrench at posskill
    $ renpy.pause(2.0, hard=True)
    hide plusfrench
    $ totalfrench = 10 + frenchovermax
return

label MCbabies:
$ mcchildren += 1
window hide
show mcbabies at posskill
$ renpy.pause(.5, hard=True)
show text "{font=Gui/Boogaloo-Regular.ttf}{color=#ff0000}{size=50}[mcchildren]{/font}" at BabyPosition    
pause
hide text
hide mcbabies
return
    
label DiceRoll:
window hide
show dicerollnone at posmission
play sound "Sounds/diceroll.mp3"
$ renpy.pause(0.5, hard=True)
$ diceroll = renpy.random.randint(1, 6)
if diceroll == 1:
    show dieone at posdiceroll
if diceroll == 2:
    show dietwo at posdiceroll
if diceroll == 3:
    show diethree at posdiceroll
if diceroll == 4:
    show diefour at posdiceroll
if diceroll == 5:
    show diefive at posdiceroll
if diceroll == 6:
    show diesix at posdiceroll
pause
hide dicerollnone
if diceroll == 1:
    hide dieone
if diceroll == 2:
    hide dietwo
if diceroll == 3:
    hide diethree
if diceroll == 4:
    hide diefour
if diceroll == 5:
    hide diefive
if diceroll == 6:
    hide diesix
return    

label UsePendulum:
window hide
show mchypno02
$ renpy.pause(1.0, hard=True)
mc "Just watch this pendulum as I wiggle it in front of your eyes..."
window hide
hide mchypno02
show mchypno03
$ renpy.pause(0.25, hard=True)
hide mchypno03
show mchypno02
$ renpy.pause(0.2, hard=True)
hide mchypno02
show mchypno01
$ renpy.pause(0.25, hard=True)
hide mchypno01
show mchypno02
$ renpy.pause(0.2, hard=True)
hide mchypno02
show mchypno03
$ renpy.pause(0.25, hard=True)
hide mchypno03
show mchypno02
$ renpy.pause(0.2, hard=True)
hide mchypno02
show mchypno01
$ renpy.pause(0.25, hard=True)
hide mchypno01
show mchypno02
$ renpy.pause(0.2, hard=True)
mc "You feel very sleepy... And you start dreaming... about fucking my HERO cock..."
window hide
hide mchypno02
show mchypno03
$ renpy.pause(0.25, hard=True)
hide mchypno03
show mchypno02
$ renpy.pause(0.2, hard=True)
hide mchypno02
show mchypno01
$ renpy.pause(0.25, hard=True)
hide mchypno01
show mchypno02
$ renpy.pause(0.2, hard=True)
hide mchypno02
show mchypno03
$ renpy.pause(0.25, hard=True)
hide mchypno03
show mchypno02
$ renpy.pause(0.2, hard=True)
hide mchypno02
show mchypno01
$ renpy.pause(0.25, hard=True)
if pendulumused >= 3:
    play sound "Sounds/snap.mp3"
    hide mchypno01
    show mchypnobreak
    mc "Shit, the pendulum snapped! I guess I won't be able to use it again... Just like in that other game."
    hide mchypnobreak
    $ pendulum = False
    return
$ usedpendulum = True
$ pendulumused += 1
mc "I think that should do the trick..."
hide mchypno01
return

label AloneStance:
if witham:
    mc "I'll go and investigate this place. Stay behind Amy, it might be dangerous."
    am "Oh? That sounds adventurous, I so wish I could come..."
if withan:
    mc "I'll go and investigate this place. Stay behind Angie, it might be dangerous."
    an "I hope it's not bad guys that you are going to have to FIGHT with all your MIGHT!"
if withcy:
    mc "I'll go and investigate this place. Stay behind Cyrl, and be on the lookout."
    cy "As usual, the menial tasks for the cyborg..."
if withmo:
    mc "I'll go and investigate this place. Stay behind Nancy, it might be dangerous."
    mo "Be careful sweetie pie!"
if withru:
    mc "I'll go and investigate this place, Ruby. You need to stay behind and shoot anything and anyone suspect that comes along."
    ru "And then get away Scot-free thanks to my NRANRA card!"
if withay:
    mc "I'll go and investigate this place. Stay behind Ayla, it might be dangerous."
    ay "Fine, whatever is up there is probably BORING anyway."
if withmi:
    mc "I'll go and investigate this place. Stay behind Michiko, and fight off any enemy that might come along."
    mi "They'll get the beating of their life if they do!"
if withza:
    mc "I'll go and investigate this place. Stay behind Zara, it might be dangerous."
    za "I am so lucky to have such a brave and courageous harem Master."
if withsu:
    mc "I'll go and investigate this place. Stay behind Suki, it might be dangerous."
    su "I'll be ready to contact the compound via satellite if we need help. If I can get a connection."
if withgw:
    mc "I'll go and investigate this place. Stay behind Gwen, it might be dangerous."
    gw "Thanks. I do enough dangerous stuff in the lab, I don't want to get injured here on top of that."
if withma:
    mc "I'll go and investigate this place. Stay behind Marnie and look out for Road Warriors."
    ma "I wish some would come, at least I could have an interesting conversation with someone."
    mc "I'll pretend I didn't hear that."
if withcl:
    mc "I'll go and investigate this place. Stay behind Clara, it might be dangerous."
    cl "I'll pray for your safety, [name]."
if withla:
    mc "I'll go and investigate this place. Stay behind Laurie, it might be dangerous."
    la "While you're gone, I'll look if I can find some interesting seeds buried in the ground around here."
if withba:
    mc "I'll go and investigate this place. Stay behind Barbara, it might be dangerous."
    ba "Fine, I don't know why I left my classroom to come along anyway..."
if withde:
    mc "I'll go and investigate this place. Stay behind Barbara, it might be dangerous."
    de "Fine, I don't know why I left my lab to come along anyway..."
if withnone:
    mc "I should go and investigate..."
return

label CindyInventory:
show inventoryinterface at left with moveinleft
jump CindyInventory02

label CindyInventory02a:
$ money -= 6
hide cindy02
show cindy01 at right
with fastdissolve
ci "Gosh, you'll be able to lick some varmints with this blade I reckon."
hide cindy01
show cindy02 at right
with fastdissolve
jump CindyInventory02

label CindyInventory02b:
$ money -= 8
$ darts += 5
$ dart = True
hide cindy02
show cindy01 at right
with fastdissolve
ci "These are darn' tootin' for starting a camel ranch."
hide cindy01
show cindy02 at right
with fastdissolve
jump CindyInventory02

label CindyInventory02c:
$ money -= 12
hide cindy02
show cindy01 at right
with fastdissolve
ci "That mask will look as snug as a bug on you!"
hide cindy01
show cindy02 at right
with fastdissolve
jump CindyInventory02

label CindyInventory02d:
$ money -= 10
hide cindy02
show cindy01 at right
with fastdissolve
ci "Thanks for your purchase, I'm as happy as a dead pig in the sunshine now."
hide cindy01
show cindy02 at right
with fastdissolve
jump CindyInventory02

label CindyInventory02e:
$ money -= 30
hide inventoryinterface
hide cindy02
show cindy04 at right
with fastdissolve
ci "You ain’t got no home trainin’, but ya know your guns mister!"
hide cindy04
show cindy05 at right
with fastdissolve
ci "I'll wrap it up for you."
hide cindy05
show cindy02 at right
with fastdissolve
show inventoryinterface at left with moveinleft
jump CindyInventory02

label CindyInventory02f:
$ money -= 15
hide cindy02
show cindy01 at right
with fastdissolve
ci "That'll fix anything that got all caddywhompus."
hide cindy01
show cindy02 at right
with fastdissolve
jump CindyInventory02

label CindyInventory02g:
$ money -= 10
hide cindy02
show cindy01 at right
with fastdissolve
hide inventoryinterface
ci "I can try it on for ya to see how pretty it looks first."
mc "Alright!"
ci "I'll be right back, dontcha go nowhere."
hide cindy01 with moveoutright
$ renpy.pause(1.0, hard='True')
show cindylingerie01 with moveinright
ci "See, it hugs a lass' curves real snugly."
scene junktown01
show cindylingerie02
with dissolve
ci "And it don't leave much to the imagination..."
mc "Indeed, although I am still capable of imagining some things..."
scene junktown01
show cindylingerie04
with dissolve
ci "It's real snug at the back. Fits right between the arsecheeks."
mc "I see..."
scene junktown01 blurred
show cindylingerie03
with dissolve
mc "Even better now... I'll take it for sure!"
scene junktown01
show cindylingerie01
with dissolve
ci "Well I'm glad you liked it. I'll wrap it up for ya. Be right back, dontcha go nowhere."
hide cindylingerie01 with moveoutright
$ renpy.pause(1.0, hard='True')
show cindy02 at right with moveinright
ci "Here's the rest of mah stuff I've got selling."
show inventoryinterface at left with moveinleft
jump CindyInventory02

label CindyInventory02h:
$ money -= 50
hide inventoryinterface
hide cindy02
show cindy04 at right
with fastdissolve
ci "That's mah most expensive gun, I’m happier than a tornado in a trailer park to be selling it to ya!"
hide cindy04
show cindy05 at right
with fastdissolve
ci "I'll wrap it up for you. Be right back, dontcha go nowhere."
hide cindy05
show cindy02 at right
with fastdissolve
show inventoryinterface at left with moveinleft
jump CindyInventory02

label CindyInventory02:
show inventoryinterface at left
call screen cindyinventory02
screen cindyinventory02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/exitidle.png"
        hover "Icons/exithover.png"
        action Jump ("CindyReturn")
    if dagger == False:
        imagebutton:
            focus_mask True
            idle "Explore02/cindyknifeidle.png"
            hover "Explore02/cindyknifehover.png"
            action Jump ("CindyInventory02")
        if money >= 6:
            imagebutton:
                focus_mask True
                idle "Icons/buy01.png"
                hover "Icons/buy01.png"
                action [SetVariable('dagger', True), Jump ("CindyInventory02a")]
    imagebutton:
        focus_mask True
        idle "Icons/dartsidle.png"
        hover "Explore02/cindydartshover.png"
        action Jump ("CindyInventory02")
    if money >= 8:
        imagebutton:
            focus_mask True
            idle "Icons/buy02.png"
            hover "Icons/buy02.png"
            action [SetVariable('dart', True), Jump ("CindyInventory02b")]
    if explosives == False:
        imagebutton:
            focus_mask True
            idle "Explore02/cindyexplosivesidle.png"
            hover "Explore02/cindyexplosiveshover.png"
            action Jump ("CindyInventory02")
        if money >= 10:
            imagebutton:
                focus_mask True
                idle "Icons/buy03.png"
                hover "Icons/buy03.png"
                action [SetVariable('explosives', True), Jump ("CindyInventory02d")]
    if bikini01 == False:
        imagebutton:
            focus_mask True
            idle "Explore02/cindybikiniidle.png"
            hover "Explore02/cindybikinihover.png"
            action Jump ("CindyInventory02")
        if money >= 10:
            imagebutton:
                focus_mask True
                idle "Icons/buy04.png"
                hover "Icons/buy04.png"
                action [SetVariable('bikini01', True), Jump ("CindyInventory02g")]
    if gasmask == False:
        imagebutton:
            focus_mask True
            idle "Icons/gasmaskidle.png"
            hover "Explore02/cindygasmaskhover.png"
            action Jump ("CindyInventory02")
        if money >= 12:
            imagebutton:
                focus_mask True
                idle "Icons/buy05.png"
                hover "Icons/buy05.png"
                action [SetVariable('gasmask', True), Jump ("CindyInventory02c")]
    if rifle == False:
        imagebutton:
            focus_mask True
            idle "Icons/rifleidle.png"
            hover "Explore02/cindyriflehover.png"
            action Jump ("CindyInventory02")
        if money >= 30:
            imagebutton:
                focus_mask True
                idle "Icons/buy06.png"
                hover "Icons/buy06.png"
                action [SetVariable('rifle', True), Jump ("CindyInventory02e")]
    if sniper == False:
        imagebutton:
            focus_mask True
            idle "Explore02/cindysniperidle.png"
            hover "Explore02/cindysniperhover.png"
            action Jump ("CindyInventory02")
        if money >= 50:
            imagebutton:
                focus_mask True
                idle "Icons/buy07.png"
                hover "Icons/buy07.png"
                action [SetVariable('sniper', True), Jump ("CindyInventory02h")]
    if repairkit == False:
        imagebutton:
            focus_mask True
            idle "Icons/repairidle.png"
            hover "Explore02/cindyrepairhover.png"
            action Jump ("CindyInventory02")
        if money >= 15:
            imagebutton:
                focus_mask True
                idle "Icons/buy08.png"
                hover "Icons/buy08.png"
                action [SetVariable('repairkit', True), Jump ("CindyInventory02f")]

label CindyReturn:
if cindyinventory01:
    jump CindyInventoryReturn01
if cindyinventory02:
    jump CindyInventoryReturn02
if cindyinventory03:
    jump CindyInventoryReturn03

label JoeInventory:
show inventoryinterface at left with moveinleft
jump JoeInventory02

label JoeInventory02z:
jo "This stone has weird markings on it, that's why it's more expensive than you would expect..."
"You found one of the missing pieces of the Stone Artefact."
$ money -= 5
$ stonepieces -= 1
window hide
show achievementgenie at posmission
$ renpy.pause(0.5, hard=True)
show text "{font=Gui/Boogaloo-Regular.ttf}{color=#ff0000}{size=30}[stonepieces]{/font}" at StonePosition
$ renpy.pause(2.0, hard=True)
hide achievementgenie
hide text
$ stonepiece05 = True
jump JoeInventory02

label JoeInventory02a:
$ money -= 10
$ darts += 5
$ dart = True
jo "Excellent choice! I use them myself... to capture reluctant male models."
jump JoeInventory02

label JoeInventory02b:
$ money -= 15
jo "A perfect fit for you, it's the EXTRA-muscular version. With a XXL pouch..."
jump JoeInventory02

label JoeInventory02x:
$ money -= 15
jo "This gas mask will get you through a minefield of noxious odors."
jump JoeInventory02

label JoeInventory02c:
$ money -= 10
jo "You need a maid? You'll turn any girl into your slave with that costume..."
jump JoeInventory02

label JoeInventory02d:
$ money -= 20
jo "Wise purchase! You'll be able to repair your rig in the middle of the desert with that."
jump JoeInventory02

label JoeInventory02e:
$ money -= 40
jo "Better safe than sorry with this self-defense attack weapon!"
jump JoeInventory02

label JoeInventory02f:
$ money -= 10
jo "A fine piece of lingerie. Unfortunately, for a woman."
jump JoeInventory02

label JoeInventory02:
show inventoryinterface at left
call screen joeinventory02
screen joeinventory02:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/exitidle.png"
        hover "Icons/exithover.png"
        action Jump ("BarJoeMenu")
    if stonepiece05 == False and missionge:
        imagebutton:
            focus_mask True
            idle "Icons/stone05idle.png"
            hover "Icons/stone05hover.png"
            action Jump ("JoeInventory02")
        if money >= 5:
            imagebutton:
                focus_mask True
                idle "Icons/buy01.png"
                hover "Icons/buy01.png"
                action [SetVariable('stonepiece05', True), Jump ("JoeInventory02z")]
    imagebutton:
        focus_mask True
        idle "Icons/dartsidle.png"
        hover "Icons/dartshover.png"
        action Jump ("JoeInventory02")
    if money >= 10:
        imagebutton:
            focus_mask True
            idle "Icons/buy02.png"
            hover "Icons/buy02.png"
            action [SetVariable('dart', True), Jump ("JoeInventory02a")]
    if americacostume == False:
        imagebutton:
            focus_mask True
            idle "Icons/americaidle.png"
            hover "Icons/americahover.png"
            action Jump ("JoeInventory02")
        if money >= 15:
            imagebutton:
                focus_mask True
                idle "Icons/buy03.png"
                hover "Icons/buy03.png"
                action [SetVariable('americacostume', True), Jump ("JoeInventory02b")]
    if gasmask == False:
        imagebutton:
            focus_mask True
            idle "Icons/gasmaskidle.png"
            hover "Icons/gasmaskhover.png"
            action Jump ("JoeInventory02")
        if money >= 15:
            imagebutton:
                focus_mask True
                idle "Icons/buy05.png"
                hover "Icons/buy05.png"
                action [SetVariable('gasmask', True), Jump ("JoeInventory02x")]
    if maidcostume == False:
        imagebutton:
            focus_mask True
            idle "Icons/maididle.png"
            hover "Icons/maidhover.png"
            action Jump ("JoeInventory02")
        if money >= 10:
            imagebutton:
                focus_mask True
                idle "Icons/buy04.png"
                hover "Icons/buy04.png"
                action [SetVariable('maidcostume', True), Jump ("JoeInventory02c")]
    if lingerie02 == False:
        imagebutton:
            focus_mask True
            idle "Icons/lingerie02idle.png"
            hover "Icons/lingerie02hover.png"
            action Jump ("JoeInventory02")
        if money >= 10:
            imagebutton:
                focus_mask True
                idle "Icons/buy07.png"
                hover "Icons/buy07.png"
                action [SetVariable('lingerie02', True), Jump ("JoeInventory02f")]
    if repairkit == False:
        imagebutton:
            focus_mask True
            idle "Icons/repairidle.png"
            hover "Icons/repairhover.png"
            action Jump ("JoeInventory02")
        if money >= 20:
            imagebutton:
                focus_mask True
                idle "Icons/buy08.png"
                hover "Icons/buy08.png"
                action [SetVariable('repairkit', True), Jump ("JoeInventory02d")]
    if rifle == False:
        imagebutton:
            focus_mask True
            idle "Icons/rifleidle.png"
            hover "Icons/riflehover.png"
            action Jump ("JoeInventory02")
        if money >= 40:
            imagebutton:
                focus_mask True
                idle "Icons/buy06.png"
                hover "Icons/buy06.png"
                action [SetVariable('rifle', True), Jump ("JoeInventory02e")]

return

label BellaHarem:
$ askedbellajoin = True
if girlsinharem == 0:
    if bellabar:
        hide belladancing05
        show belladancing06
        with fastdissolve
    if bellachurch:
        hide bene
        show bella06
        with fastdissolve
    if bellapool:
        hide poolbella03
        show poolbella04
        with fastdissolve
    be "Poor lonely boy, you don't seem to have anyone in your harem... I'll be there to comfort you and show the path to Redemption then. Count me in!"
    $ girlsinharem += 1
    $ harembe = True
    $ bellaharem = True
    mc "Thanks Bella, you won't regret being my sexual...err...slave. I'll call you at nights!"
    return

if bellabar:
    hide belladancing05
    show belladancing06
    with fastdissolve
if bellachurch:
    hide bene
    show bella06
    with fastdissolve
if bellapool:
    hide poolbella03
    show poolbella04
    with fastdissolve
if haremde or haremza or hareman or haremmo or haremmi or haremcy or haremru or haremam or haremay or haremsu or harempe or haremma or haremgw or haremcl or haremla or haremle or haremba:

    label BellaHaremRandom:
    $ drollbella=renpy.random.randint(1,17)
    if drollbella == 1 and haremam == False:
        jump BellaHaremRandom
    if drollbella == 2 and hareman == False:
        jump BellaHaremRandom
    if drollbella == 3 and haremba == False:
        jump BellaHaremRandom
    if drollbella == 4 and haremcy == False:
        jump BellaHaremRandom
    if drollbella == 5 and haremde == False:
        jump BellaHaremRandom
    if drollbella == 6 and haremgw == False:
        jump BellaHaremRandom
    if drollbella == 7 and haremmo == False:
        jump BellaHaremRandom
    if drollbella == 8 and haremma == False:
        jump BellaHaremRandom
    if drollbella == 9 and haremay == False:
        jump BellaHaremRandom
    if drollbella == 10 and haremle == False:
        jump BellaHaremRandom    
    if drollbella == 11 and harempe == False:
        jump BellaHaremRandom
    if drollbella == 12 and haremmi == False:
        jump BellaHaremRandom
    if drollbella == 13 and haremza == False:
        jump BellaHaremRandom
    if drollbella == 14 and haremru == False:
        jump BellaHaremRandom
    if drollbella == 15 and haremla == False:
        jump BellaHaremRandom
    if drollbella == 16 and haremcl == False:
        jump BellaHaremRandom
    if drollbella == 17 and haremsu == False:
        jump BellaHaremRandom

    if drollbella == 1 and haremam:
        be "I won't join your harem until you get rid of that sinful bitch Amy!"
        if pregam:
            mc "I can't get rid of her, she's pregnant with my child!"
            if bellabar:
                hide belladancing06
                show belladancing07
                with fastdissolve
            if bellachurch:
                hide bella06
                show bellaangry
                with fastdissolve
            if bellapool:
                hide poolbella04
                show poolbella06
                with fastdissolve
            be "Too bad then. I ain't joining your harem anytime soon."
            return
        menu:
            "Agree and get rid of Amy":
                mc "Alright, I'll let her know next Monday and you can replace her."
                if bellabar:
                    hide belladancing06
                    show belladancing08
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bella08
                    with fastdissolve
                if bellapool:
                    hide poolbella04
                    show poolbella05
                    with fastdissolve
                $ replaceamy = True
                be "You won't regret that rightful decision!"
            "Keep Amy and don't take Bella in":
                if bellabar:
                    hide belladancing06
                    show belladancing07
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bellaangry
                    with fastdissolve                
                if bellapool:
                    hide poolbella04
                    show poolbella06
                    with fastdissolve
                be "You'll regret that..."
                call LustMinusBella 
                be "There. As I foresaw. Bye [name]."
        return                        
                
    if drollbella == 2 and hareman:
        be "I won't join your harem until you get rid of that sinful bitch Angie!"
        if pregan:
            mc "I can't get rid of her, she's pregnant with my child!"
            if bellabar:
                hide belladancing06
                show belladancing07
                with fastdissolve
            if bellachurch:
                hide bella06
                show bellaangry
                with fastdissolve
            if bellapool:
                hide poolbella04
                show poolbella06
                with fastdissolve
            be "Too bad then. I ain't joining your harem anytime soon."
            return
        menu:
            "Agree and get rid of Angie":
                mc "Alright, I'll let her know next Monday and you can replace her."
                if bellabar:
                    hide belladancing06
                    show belladancing08
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bella08
                    with fastdissolve
                if bellapool:
                    hide poolbella04
                    show poolbella05
                    with fastdissolve
                $ replaceangie = True
                be "You won't regret that rightful decision!"
            "Keep Angie and don't take Bella in":
                if bellabar:
                    hide belladancing06
                    show belladancing07
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bellaangry
                    with fastdissolve                
                if bellapool:
                    hide poolbella04
                    show poolbella06
                    with fastdissolve
                be "You'll regret that..."
                call LustMinusBella 
                be "There. As I foresaw. Bye [name]."
        return                
                
    if drollbella == 3 and haremba:
        be "I won't join your harem until you get rid of that sinful bitch Barbara!"
        if pregba:
            mc "I can't get rid of her, she's pregnant with my child!"
            if bellabar:
                hide belladancing06
                show belladancing07
                with fastdissolve
            if bellachurch:
                hide bella06
                show bellaangry
                with fastdissolve
            if bellapool:
                hide poolbella04
                show poolbella06
                with fastdissolve
            be "Too bad then. I ain't joining your harem anytime soon."
            return
        menu:
            "Agree and get rid of Barbara":
                mc "Alright, I'll let her know next Monday and you can replace her."
                if bellabar:
                    hide belladancing06
                    show belladancing08
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bella08
                    with fastdissolve
                if bellapool:
                    hide poolbella04
                    show poolbella05
                    with fastdissolve
                $ replacebarbara = True
                be "You won't regret that rightful decision!"
            "Keep Barbara and don't take Bella in":
                if bellabar:
                    hide belladancing06
                    show belladancing07
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bellaangry
                    with fastdissolve                
                if bellapool:
                    hide poolbella04
                    show poolbella06
                    with fastdissolve
                be "You'll regret that..."
                call LustMinusBella 
                be "There. As I foresaw. Bye [name]."
        return                
                
    if drollbella == 4 and haremcy:
        be "I won't join your harem until you get rid of that sinful android Cyrl!"
        menu:
            "Agree and get rid of Cyrl":
                mc "Alright, I'll let her know next Monday and you can replace her."
                if bellabar:
                    hide belladancing06
                    show belladancing08
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bella08
                    with fastdissolve
                if bellapool:
                    hide poolbella04
                    show poolbella05
                    with fastdissolve
                $ replacecyrl = True
                be "You won't regret that rightful decision!"
            "Keep Cyrl and don't take Bella in":
                if bellabar:
                    hide belladancing06
                    show belladancing07
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bellaangry
                    with fastdissolve                
                if bellapool:
                    hide poolbella04
                    show poolbella06
                    with fastdissolve
                be "You'll regret that..."
                call LustMinusBella 
                be "There. As I foresaw. Bye [name]."
        return                 

    if drollbella == 5 and haremde:
        be "I won't join your harem until you get rid of that sinful bitch Debra!"
        menu:
            "Agree and get rid of Debra":
                mc "Alright, I'll let her know next Monday and you can replace her."
                if bellabar:
                    hide belladancing06
                    show belladancing08
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bella08
                    with fastdissolve
                if bellapool:
                    hide poolbella04
                    show poolbella05
                    with fastdissolve
                $ replacedebra = True
                be "You won't regret that rightful decision!"
            "Keep Debra and don't take Bella in":
                if bellabar:
                    hide belladancing06
                    show belladancing07
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bellaangry
                    with fastdissolve                
                if bellapool:
                    hide poolbella04
                    show poolbella06
                    with fastdissolve
                be "You'll regret that..."
                call LustMinusBella 
                be "There. As I foresaw. Bye [name]."
        return     

    if drollbella == 6 and haremgw:
        be "I won't join your harem until you get rid of that sinful bitch Gwen!"
        if preggw:
            mc "I can't get rid of her, she's pregnant with my child!"
            if bellabar:
                hide belladancing06
                show belladancing07
                with fastdissolve
            if bellachurch:
                hide bella06
                show bellaangry
                with fastdissolve
            if bellapool:
                hide poolbella04
                show poolbella06
                with fastdissolve
            be "Too bad then. I ain't joining your harem anytime soon."
            return
        menu:
            "Agree and get rid of Gwen":
                mc "Alright, I'll let her know next Monday and you can replace her."
                if bellabar:
                    hide belladancing06
                    show belladancing08
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bella08
                    with fastdissolve
                if bellapool:
                    hide poolbella04
                    show poolbella05
                    with fastdissolve
                $ replacegwen = True
                be "You won't regret that rightful decision!"
            "Keep Gwen and don't take Bella in":
                if bellabar:
                    hide belladancing06
                    show belladancing07
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bellaangry
                    with fastdissolve                
                if bellapool:
                    hide poolbella04
                    show poolbella06
                    with fastdissolve
                be "You'll regret that..."
                call LustMinusBella 
                be "There. As I foresaw. Bye [name]."
        return                

    if drollbella == 7 and haremmo:
        be "I won't join your harem until you get rid of that sinful bitch Nancy!"
        if pregmo:
            mc "I can't get rid of her, she's pregnant with my child!"
            if bellabar:
                hide belladancing06
                show belladancing07
                with fastdissolve
            if bellachurch:
                hide bella06
                show bellaangry
                with fastdissolve
            if bellapool:
                hide poolbella04
                show poolbella06
                with fastdissolve
            be "Too bad then. I ain't joining your harem anytime soon."
            return
        menu:
            "Agree and get rid of Nancy":
                mc "Alright, I'll let her know next Monday and you can replace her."
                if bellabar:
                    hide belladancing06
                    show belladancing08
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bella08
                    with fastdissolve
                if bellapool:
                    hide poolbella04
                    show poolbella05
                    with fastdissolve
                $ replacenancy = True
                be "You won't regret that rightful decision!"
            "Keep Nancy and don't take Bella in":
                if bellabar:
                    hide belladancing06
                    show belladancing07
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bellaangry
                    with fastdissolve                
                if bellapool:
                    hide poolbella04
                    show poolbella06
                    with fastdissolve
                be "You'll regret that..."
                call LustMinusBella 
                be "There. As I foresaw. Bye [name]."
        return          

    if drollbella == 8 and haremma:
        be "I won't join your harem until you get rid of that sinful bitch Marnie!"
        menu:
            "Agree and get rid of Marnie":
                mc "Alright, I'll let her know next Monday and you can replace her."
                if bellabar:
                    hide belladancing06
                    show belladancing08
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bella08
                    with fastdissolve
                if bellapool:
                    hide poolbella04
                    show poolbella05
                    with fastdissolve
                $ replacemarnie = True
                be "You won't regret that rightful decision!"
            "Keep Marnie and don't take Bella in":
                if bellabar:
                    hide belladancing06
                    show belladancing07
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bellaangry
                    with fastdissolve                
                if bellapool:
                    hide poolbella04
                    show poolbella06
                    with fastdissolve
                be "You'll regret that..."
                call LustMinusBella 
                be "There. As I foresaw. Bye [name]."
        return     

    if drollbella == 9 and haremay:
        be "I won't join your harem until you get rid of that sinful bitch Ayla!"
        if pregay:
            mc "I can't get rid of her, she's pregnant with my child!"
            if bellabar:
                hide belladancing06
                show belladancing07
                with fastdissolve
            if bellachurch:
                hide bella06
                show bellaangry
                with fastdissolve
            if bellapool:
                hide poolbella04
                show poolbella06
                with fastdissolve
            be "Too bad then. I ain't joining your harem anytime soon."
            return
        menu:
            "Agree and get rid of Ayla":
                mc "Alright, I'll let her know next Monday and you can replace her."
                if bellabar:
                    hide belladancing06
                    show belladancing08
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bella08
                    with fastdissolve
                if bellapool:
                    hide poolbella04
                    show poolbella05
                    with fastdissolve
                $ replaceayla = True
                be "You won't regret that rightful decision!"
            "Keep Ayla and don't take Bella in":
                if bellabar:
                    hide belladancing06
                    show belladancing07
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bellaangry
                    with fastdissolve                
                if bellapool:
                    hide poolbella04
                    show poolbella06
                    with fastdissolve
                be "You'll regret that..."
                call LustMinusBella 
                be "There. As I foresaw. Bye [name]."
        return          

    if drollbella == 10 and haremle:
        be "I won't join your harem until you get rid of Chief Lena!"
        menu:
            "Agree and get rid of Lena":
                mc "Alright, I'll let her know next Monday and you can replace her."
                if bellabar:
                    hide belladancing06
                    show belladancing08
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bella08
                    with fastdissolve
                if bellapool:
                    hide poolbella04
                    show poolbella05
                    with fastdissolve
                $ replacelena = True
                be "You won't regret that rightful decision!"
            "Keep Lena and don't take Bella in":
                if bellabar:
                    hide belladancing06
                    show belladancing07
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bellaangry
                    with fastdissolve                
                if bellapool:
                    hide poolbella04
                    show poolbella06
                    with fastdissolve
                be "You'll regret that..."
                call LustMinusBella 
                be "There. As I foresaw. Bye [name]."
        return     

    if drollbella == 11 and harempe:
        be "I won't join your harem until you get rid of that sinful scout Penny!"
        menu:
            "Agree and get rid of Penny":
                mc "Alright, I'll let her know next Monday and you can replace her."
                if bellabar:
                    hide belladancing06
                    show belladancing08
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bella08
                    with fastdissolve
                if bellapool:
                    hide poolbella04
                    show poolbella05
                    with fastdissolve
                $ replacepenny = True
                be "You won't regret that rightful decision!"
            "Keep Penny and don't take Bella in":
                if bellabar:
                    hide belladancing06
                    show belladancing07
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bellaangry
                    with fastdissolve                
                if bellapool:
                    hide poolbella04
                    show poolbella06
                    with fastdissolve
                be "You'll regret that..."
                call LustMinusBella 
                be "There. As I foresaw. Bye [name]."
        return     

    if drollbella == 12 and haremmi:
        be "I won't join your harem until you get rid of that sinful bitch Michiko!"
        if pregmi:
            mc "I can't get rid of her, she's pregnant with my child!"
            if bellabar:
                hide belladancing06
                show belladancing07
                with fastdissolve
            if bellachurch:
                hide bella06
                show bellaangry
                with fastdissolve
            if bellapool:
                hide poolbella04
                show poolbella06
                with fastdissolve
            be "Too bad then. I ain't joining your harem anytime soon."
            return
        menu:
            "Agree and get rid of Michiko":
                mc "Alright, I'll let her know next Monday and you can replace her."
                if bellabar:
                    hide belladancing06
                    show belladancing08
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bella08
                    with fastdissolve
                if bellapool:
                    hide poolbella04
                    show poolbella05
                    with fastdissolve
                $ replacemichiko = True
                be "You won't regret that rightful decision!"
            "Keep Michiko and don't take Bella in":
                if bellabar:
                    hide belladancing06
                    show belladancing07
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bellaangry
                    with fastdissolve                
                if bellapool:
                    hide poolbella04
                    show poolbella06
                    with fastdissolve
                be "You'll regret that..."
                call LustMinusBella 
                be "There. As I foresaw. Bye [name]."
        return          

    if drollbella == 13 and haremza:
        be "I won't join your harem until you get rid of that sinful heretic Zara!"
        if pregza:
            mc "I can't get rid of her, she's pregnant with my child!"
            if bellabar:
                hide belladancing06
                show belladancing07
                with fastdissolve
            if bellachurch:
                hide bella06
                show bellaangry
                with fastdissolve
            if bellapool:
                hide poolbella04
                show poolbella06
                with fastdissolve
            be "Too bad then. I ain't joining your harem anytime soon."
            return
        menu:
            "Agree and get rid of Zara":
                mc "Alright, I'll let her know next Monday and you can replace her."
                if bellabar:
                    hide belladancing06
                    show belladancing08
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bella08
                    with fastdissolve
                if bellapool:
                    hide poolbella04
                    show poolbella05
                    with fastdissolve
                $ replacezara = True
                be "You won't regret that rightful decision!"
            "Keep Zara and don't take Bella in":
                if bellabar:
                    hide belladancing06
                    show belladancing07
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bellaangry
                    with fastdissolve                
                if bellapool:
                    hide poolbella04
                    show poolbella06
                    with fastdissolve
                be "You'll regret that..."
                call LustMinusBella 
                be "There. As I foresaw. Bye [name]."
        return          

    if drollbella == 14 and haremru:
        be "I won't join your harem until you get rid of that sinful bitch Ruby!"
        menu:
            "Agree and get rid of Ruby":
                mc "Alright, I'll let her know next Monday and you can replace her."
                if bellabar:
                    hide belladancing06
                    show belladancing08
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bella08
                    with fastdissolve
                if bellapool:
                    hide poolbella04
                    show poolbella05
                    with fastdissolve
                $ replaceruby = True
                be "You won't regret that rightful decision!"
            "Keep Ruby and don't take Bella in":
                if bellabar:
                    hide belladancing06
                    show belladancing07
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bellaangry
                    with fastdissolve                
                if bellapool:
                    hide poolbella04
                    show poolbella06
                    with fastdissolve
                be "You'll regret that..."
                call LustMinusBella 
                be "There. As I foresaw. Bye [name]."
        return 

    if drollbella == 15 and haremla:
        be "I won't join your harem until you get rid of that sinful bitch Laurie!"
        if pregla:
            mc "I can't get rid of her, she's pregnant with my child!"
            if bellabar:
                hide belladancing06
                show belladancing07
                with fastdissolve
            if bellachurch:
                hide bella06
                show bellaangry
                with fastdissolve
            if bellapool:
                hide poolbella04
                show poolbella06
                with fastdissolve
            be "Too bad then. I ain't joining your harem anytime soon."
            return
        menu:
            "Agree and get rid of Laurie":
                mc "Alright, I'll let her know next Monday and you can replace her."
                if bellabar:
                    hide belladancing06
                    show belladancing08
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bella08
                    with fastdissolve
                if bellapool:
                    hide poolbella04
                    show poolbella05
                    with fastdissolve
                $ replacelaurie = True
                be "You won't regret that rightful decision!"
            "Keep Laurie and don't take Bella in":
                if bellabar:
                    hide belladancing06
                    show belladancing07
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bellaangry
                    with fastdissolve                
                if bellapool:
                    hide poolbella04
                    show poolbella06
                    with fastdissolve
                be "You'll regret that..."
                call LustMinusBella 
                be "There. As I foresaw. Bye [name]."
        return          

    if drollbella == 16 and haremcl:
        menu:
            "Agree and get rid of Clara":
                mc "Alright, I'll let her know next Monday and you can replace her."
                if bellabar:
                    hide belladancing06
                    show belladancing08
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bella08
                    with fastdissolve
                if bellapool:
                    hide poolbella04
                    show poolbella05
                    with fastdissolve
                $ replaceclara = True
                be "You won't regret that rightful decision!"
            "Keep Clara and don't take Bella in":
                if bellabar:
                    hide belladancing06
                    show belladancing07
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bellaangry
                    with fastdissolve                
                if bellapool:
                    hide poolbella04
                    show poolbella06
                    with fastdissolve
                be "You'll regret that..."
                call LustMinusBella 
                be "There. As I foresaw. Bye [name]."
        return 

    if drollbella == 17 and haremsu:
        be "I won't join your harem until you get rid of that sinful bitch Suki!"
        menu:
            "Agree and get rid of Suki":
                mc "Alright, I'll let her know next Monday and you can replace her."
                if bellabar:
                    hide belladancing06
                    show belladancing08
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bella08
                    with fastdissolve
                if bellapool:
                    hide poolbella04
                    show poolbella05
                    with fastdissolve
                $ replacesuki = True
                be "You won't regret that rightful decision!"
            "Keep Suki and don't take Bella in":
                if bellabar:
                    hide belladancing06
                    show belladancing07
                    with fastdissolve
                if bellachurch:
                    hide bella06
                    show bellaangry
                    with fastdissolve                
                if bellapool:
                    hide poolbella04
                    show poolbella06
                    with fastdissolve
                be "You'll regret that..."
                call LustMinusBella 
                be "There. As I foresaw. Bye [name]."
        return 
