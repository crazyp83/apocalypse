label ExploreGallery:
call screen galleryexplore
screen galleryexplore:
    add "Gallery/exploregallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("galleryexplore"), Jump ("MainGallery")]

    imagebutton:
        focus_mask True
        idle "Gallery/gallerynextpage.png"
        hover "Gallery/gallerynextpage.png"
        action [Hide ("galleryexplore"), Jump ("ExploreGalleryb")]

    if renpy.seen_image("aliencum"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery01.png" xpos 621 ypos 100
            hover "Gallery/exploregallery01.png"
            action Jump ("ExploreGallery01")

    if renpy.seen_image("aliencum") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGallery")

    if renpy.seen_image("opalasex01"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery02.png" xpos 1050 ypos 100
            hover "Gallery/exploregallery02.png"
            action Jump ("ExploreGallery02")

    if renpy.seen_image("opalasex01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGallery")

    if renpy.seen_image("oracleprefuck01"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery03.png" xpos 1478 ypos 100
            hover "Gallery/exploregallery03.png"
            action Jump ("ExploreGallery03")

    if renpy.seen_image("oracleprefuck01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGallery")

    if renpy.seen_image("shehulkcum01"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery04.png" xpos 621 ypos 400
            hover "Gallery/exploregallery04.png"
            action Jump ("ExploreGallery04")

    if renpy.seen_image("shehulkcum01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGallery")

    if renpy.seen_image("sofiaprefuck01"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery05.png" xpos 1050 ypos 400
            hover "Gallery/exploregallery05.png"
            action Jump ("ExploreGallery05")

    if renpy.seen_image("sofiaprefuck01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGallery")

    if renpy.seen_image("titahontasprefuck01"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery06.png" xpos 1478 ypos 400
            hover "Gallery/exploregallery06.png"
            action Jump ("ExploreGallery06")

    if renpy.seen_image("titahontasprefuck01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGallery")

    if renpy.seen_image("bikewash01"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery07.png" xpos 621 ypos 700
            hover "Gallery/exploregallery07.png"
            action Jump ("ExploreGallery07")

    if renpy.seen_image("bikewash01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGallery")

    if renpy.seen_image("hulkmagnusprelick01"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery08.png" xpos 1050 ypos 700
            hover "Gallery/exploregallery08.png"
            action Jump ("ExploreGallery08")

    if renpy.seen_image("hulkmagnusprelick01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGallery")

    if renpy.seen_image("hippyfire03"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery09.png" xpos 1478 ypos 700
            hover "Gallery/exploregallery09.png"
            action Jump ("ExploreGallery09")

    if renpy.seen_image("hippyfire03") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGallery")

    add "Gallery/gallerygrid02.png"
    add "Gallery/textexplore.png"

label ExploreGalleryb:
call screen galleryexploreb
screen galleryexploreb:
    add "Gallery/exploregallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("galleryexploreb"), Jump ("MainGallery")]

    imagebutton:
        focus_mask True
        idle "Gallery/gallerynextpage.png"
        hover "Gallery/gallerynextpage.png"
        action [Hide ("galleryexploreb"), Jump ("ExploreGalleryc")]

    if renpy.seen_image("sisterannacum01"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery10.png" xpos 621 ypos 100
            hover "Gallery/exploregallery10.png"
            action Jump ("ExploreGallery10")

    if renpy.seen_image("sisterannacum01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGalleryb")

    if renpy.seen_image("annafuckcum01"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery11.png" xpos 1050 ypos 100
            hover "Gallery/exploregallery11.png"
            action Jump ("ExploreGallery11")

    if renpy.seen_image("annafuckcum01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGalleryb")

    if renpy.seen_image("wendyhandcum01"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery12.png" xpos 1478 ypos 100
            hover "Gallery/exploregallery12.png"
            action Jump ("ExploreGallery12")

    if renpy.seen_image("wendyhandcum01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGalleryb")

    if renpy.seen_image("wendyfuckcum01"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery13.png" xpos 621 ypos 400
            hover "Gallery/exploregallery13.png"
            action Jump ("ExploreGallery13")

    if renpy.seen_image("wendyfuckcum01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGallery")

    if renpy.seen_image("taylorfucksetup"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery14.png" xpos 1050 ypos 400
            hover "Gallery/exploregallery14.png"
            action Jump ("ExploreGallery14")

    if renpy.seen_image("taylorfucksetup") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGallery")

    if renpy.seen_image("diamondharem01b"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery15.png" xpos 1478 ypos 400
            hover "Gallery/exploregallery15.png"
            action Jump ("ExploreGallery15")

    if renpy.seen_image("diamondharem01b") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGallery")

    if renpy.seen_image("alien01fuckcum01"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery16.png" xpos 620 ypos 700
            hover "Gallery/exploregallery16.png"
            action Jump ("ExploreGallery16")

    if renpy.seen_image("alien01fuckcum01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 620 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGallery")

    if renpy.seen_image("sukyupreharem01"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery17.png" xpos 1050 ypos 700
            hover "Gallery/exploregallery17.png"
            action Jump ("ExploreGallery17")

    if renpy.seen_image("sukyupreharem01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGallery")

    if renpy.seen_image("heatherpreharem01"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery18.png" xpos 1478 ypos 700
            hover "Gallery/exploregallery18.png"
            action Jump ("ExploreGallery18")

    if renpy.seen_image("heatherpreharem01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGallery")

    add "Gallery/gallerygrid02.png"
    add "Gallery/textexplore02.png"

label ExploreGalleryc:
call screen galleryexplorec
screen galleryexplorec:
    add "Gallery/exploregallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("galleryexplorec"), Jump ("MainGallery")]

    imagebutton:
        focus_mask True
        idle "Gallery/gallerynextpage.png"
        hover "Gallery/gallerynextpage.png"
        action [Hide ("galleryexplorec"), Jump ("ExploreGallery")]

    if renpy.seen_image("krista12"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery19.png" xpos 621 ypos 100
            hover "Gallery/exploregallery19.png"
            action Jump ("ExploreGallery19")

    if renpy.seen_image("krista12") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGalleryc")

    if renpy.seen_image("danaguard04"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery20.png" xpos 1050 ypos 100
            hover "Gallery/exploregallery20.png"
            action Jump ("ExploreGallery20")

    if renpy.seen_image("danaguard04") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGalleryc")
    
    if renpy.seen_image("krista06cum"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery21.png" xpos 1478 ypos 100
            hover "Gallery/exploregallery21.png"
            action Jump ("ExploreGallery21")

    if renpy.seen_image("krista06cum") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGalleryc")

    if renpy.seen_image("quebecriver07"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery22.png" xpos 621 ypos 400
            hover "Gallery/exploregallery22.png"
            action Jump ("ExploreGallery22")

    if renpy.seen_image("quebecriver07") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGalleryc")

    if renpy.seen_image("paulettepresex01"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery23.png" xpos 1050 ypos 400
            hover "Gallery/exploregallery23.png"
            action Jump ("ExploreGallery23")

    if renpy.seen_image("paulettepresex01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGalleryc")

    if renpy.seen_image("devcave01"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery24.png" xpos 1478 ypos 400
            hover "Gallery/exploregallery24.png"
            action Jump ("ExploreGallery24")

    if renpy.seen_image("devcave01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGalleryc")

    if renpy.seen_image("titiana04"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery25.png" xpos 621 ypos 700
            hover "Gallery/exploregallery25.png"
            action Jump ("ExploreGallery25")

    if renpy.seen_image("titiana04") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGalleryc")

    if renpy.seen_image("kimfbi08"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery26.png" xpos 1050 ypos 700
            hover "Gallery/exploregallery26.png"
            action Jump ("ExploreGallery26")

    if renpy.seen_image("kimfbi08") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGalleryc")

    if renpy.seen_image("kristapresex01"):
        imagebutton:
            focus_mask True
            idle "Gallery/exploregallery27.png" xpos 1478 ypos 700
            hover "Gallery/exploregallery27.png"
            action Jump ("ExploreGallery27")

    if renpy.seen_image("kristapresex01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("ExploreGalleryc")

    add "Gallery/gallerygrid02.png"
    add "Gallery/textexplore03.png"
    
label ExploreGallery01:
stop music
scene aliens02
show alienfemale04 at right
show alienmale01 at left
mc "I beg to differ! You'll find that since the nuclear war, some of us guys have grown mammoth dongs!"
hide alienmale01        
show alienmale02 at left
with fastdissolve        
alm "Oh yeah? Prove it subspecies! Or we'll destroy your planet!"
mc "Alright, you asked for it."
scene aliens03
show mcout01
with dissolve
alf "Wow, it is indeed the most MASSIVE sex organ I have ever seen in the whole galaxy."
alm "Yeah, OK, but he's still a pitiful human, right Glurglub?"
alf "Of course my fierce Glorglob! I resent this inferior species. But still..."
scene aliens02
show alienmale01 at left
show alienfemale01 at right
with dissolve
alm "Now, my beauty Glurglub, I have an idea. How about you join this sub-alien for some interspecies porn?"
hide alienfemale01
show alienfemale02 at right
with fastdissolve
alf "What a great idea my fierce Glorglob! This will be a first and make us very rich indeed!"
mc "Of course, oh Lord Master of our Galaxy."
hide alienfemale02
show alienfemale03 at right
with fastdissolve
alf "I like this human specimen, my glorglaries are all tingly."
hide alienmale01
show alienmale02 at left
with fastdissolve
alm "Good, this will work even better then."
alm "Glurglub will assume the insemination position and you will stick your semen pole all the way up her baby hole."
mc "I don't think it will work, if you have in mind what I think you have in mind, but whatever, I'll do it."
scene aliens04 with dissolve
show mcalien01
mc "Err, it that the insemination position?"
alf "No, that's the gloggy position silly. I'm just priming my glorglaries..."
alm "Stick it as far up up her stomach as you can, I want to see a baby bump in there, understood inferior species?"
mc "Sure..."
alm "My VHS camera is ready. You can fuck her now, pitiful human!"
scene aliens04 with dissolve
play music "Sounds/aliensex.mp3"
call screen mcalienx
screen mcalienx:
    add aliensex at center
    modal True
    button:
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("McAlienEndx")    
        
label McAlienEndx:
stop music
scene aliens05
show aliencum
with dissolve
alf "YES, fill me up! Give me an intergalactic baby!!!"
alm "Don't stop shooting inside her, she needs billions and billions of tiny babies to grow inside her so we can repopulate the universe!"
mc "Shit, you guys are CRAY-AY-ZYYYY..."
scene aliens04
show aliencumend
with dissolve
mc "Fuck... I've nutted as much seed as I could... I'm empty."
alf "I can feel my multi-billion eggs getting inseminated by this inferior specimen my fierce Glorglob!"
alm "Great, it worked! I knew it, that's why we are the most intelligent species in the galaxy!"
mc "The CRAY-AY-ZIEST species you mean..."
alm "Shut up insolent human! Now stand up and cover your mammoth appendage, it's vulgar."
scene aliens02
show alienmale02 at left
show alienfemale01 at right
with dissolve
alm "We'll go right back to Glorglon now, the foul pure air on this planet is unbearable! Come, my beauty Glurglub."
jump ExploreGallery

label ExploreGallery02:
scene templesex01
show opalasex01
op "Unzip those pants and show your Queen YOUR mighty scepter!"
window hide
play sound "Sounds/zipper.mp3"
$ renpy.pause(1.0, hard=True)
op "Oh my... Let me handle that thing first, to make sure it is nice and SLIPPERY before it enters my fertile Amazon womb!"
mc "It's all yours, your Majesty..."
scene templesex02
show opalasex02
with dissolve
op "Mmmh... So tasty... *lick*"
window hide
play sound "Sounds/lick.mp3"
$ renpy.pause(1.0, hard=True)
op "Please... FUCK MY ROYAL MOUTH WITH IT!"
scene templesex01 with dissolve
play music "Sounds/hardsucking.mp3"
label OpalaBlowSlowx:
hide opalablowfast
show opalablowslow
call screen opalablowslow02x
screen opalablowslow02x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("OpalaBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("OpalaBlowFastx") 

label OpalaBlowFastx:
mc "Open your mouth even WIDER my Queen, cos I'm going to fuck it even FASTER!"
hide opalablowslow
show opalablowfast
call screen opalablowfast02x
screen opalablowfast02x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("OpalaBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("OpalaBlowSlowx") 

label OpalaBlowEndx:
stop music
scene templesex02 blurred
show opalablowcum01
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Swallow it ALL! RHAAAA!"
op "Gllurb.... Cccbuum... on... mbeeee..."
mc "I think I got that."
hide opalablowcum01
show opalablowcum02
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "And there you go, what you asked for, FUCK YEAH!"
op "And I'll... glurb... lick those FAT balls to make you cum... glub... even MORE!"
scene templesex04
show opalablowcum03
with dissolve
op "I'm covered in your filthy scum.... But it's not in the right place. I want it sloshing in my WOMB!"
mc "Well, I have another MEGA-LOAD for you stored up in my balls, your Majesty, so hop on the creamy...I mean gravy train!"
scene templesex03 blurred
show opalaprefuck01
with dissolve
op "I don't know how I'm ever going to fit something THAT big in my poor pussy..."
mc "Come on, you're an Amazon Queen, surely your fuckhole is a true warrior too."
op "Of course it is, every fiber of my body is made for fighting! And I WILL FIGHT your cock right now!"
hide opalaprefuck01
play music "Sounds/fucksound.mp3"
label OpalaFuckSlowx:
hide opalafuckfast
show opalafuckslow
call screen opalafuck02x
screen opalafuck02x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("OpalaFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("OpalaFuckFastx") 

label OpalaFuckFastx:
op "I'm going to ride you FASTER to COAX the BIGGEST load of cum possible from your MONSTER NUTS!"
hide opalafuckslow
show opalafuckfast
call screen opalafuckfast02x
screen opalafuckfast02x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("OpalaFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("OpalaFuckSlowx") 

label OpalaFuckEndx:
op "Cum in me, GIVE ME YOUR SEED TO START MY NEW TRIBE!"
mc "*Gee, what's with all those crazy nymphos wanting babies from me?*"
hide opalafuckslow
hide opalafuckfast
stop music
show opalafuckcum01
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "CUMMING FOR YOU MY QUEEN!"
scene templesex04
show opalafuckcum02
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
op "Keep blasting that virile ball-batter, IMPREGNATE ME!"
mc "I can't stop cumming for you! AAAAAHHH!"
scene templesex01 blurred
show opalafuckcum03
with dissolve
op "That's not enough! I want EVERY LAST DROP!"
mc "*cough* You're... choking me... And hitting my groin too hard!"
op "My babies need to be conceived in agony. YOUR agony!"
scene templesex02
show opalafuckcum04
with dissolve
op "You did good, your sperm is sloshing in my womb and will give me a healthy tribe to rule anew over my KINDGOM!"
mc "*cough* Glad... I could help... (Fuck, my groin hurts!)"
op "As a low-life impregnating stud to the Amazon Queen, you are of course forever banned from this temple."
mc "Well, that's not very nice..."
op "But I will gladly reward you with treasures beyond your wildest imagination!"
mc "I have a pretty wild imagination, I'm warning you."
op "Have this jewelled necklace and a gift of gold and begone, Absent Father of the Amazons!"
mc "I'm only absent cos you banned me..."
op "Stop moaning, take your money and get the fuck out of here."
mc "Roger that."
jump ExploreGallery

label ExploreGallery03:
scene oracle02
show pythia01
py "Jizz be with you, traveller. I am High Priestess Pythia, the Oracle of the Church of the Redeeming Phallus."
mc "And what are you doing in the middle of nowhere?"
hide pythia01
show pythia03
with dissolve
py "Members of the Church come from far and wide to learn about their futures. \nFor I alone can see through the One-Eye of the Phallus Lord!"
py "Follow me up the steps to the Temple, young man."
hide pythia03
show pythia04
with dissolve
py "And leave all your anger and fears behind."
scene oracle03
show pythia05
show pythia06
with dissolve
py "For the ceremony to proceed, you must first make a jizz offering to the Phallus Lord!"
mc "What???"
py "Yes, the Phallus Lord demands it. Also, I want to see what's hiding underneath that HUGE bulge of yours."
mc "Fine, fine..."
play sound "Sounds/zipper.mp3"
hide pythia06
show pythia07
with fastdissolve
py "Oh my..."
hide pythia05
hide pythia07
show pythia02
with fastdissolve
py "And now the Phallus Lord demands that the offering be made IN MY PUSSY!"
mc "Oh, here we go again. Bunch of nymphos."
scene oracleprefuck01 with fade
py "What are you waiting for? Get that godly phallus HARD and come and seed me!"
mc "I'm coming, getting my clothes off as fast as I can, High Priestess!"
scene oracleprefuck02 with dissolve
py "I've been a VERY NAUGHTY High Priestess, you need to PUNISH me [name]!"
mc "Oh I will, and I've got the tool to flagellate your insides too!"
py "The Phallus Lord will therefore grant you a new nickname... \"[name] the Punisher\"!"
mc "Alright! I have a nickname now! Woo-ooh! Prepare to be PUNISHED by \"[name] the Punisher\"!"
play music "Sounds/fucksound.mp3"
label OracleFuckSlowx:
hide oraclefuckfast
show oraclefuckslow
call screen oraclefuck02x
screen oraclefuck02x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("OracleFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("OracleFuckFastx") 

label OracleFuckFastx:
py "Fuck me FASTER! I need your offering in my pussy blasting at FULL SPEED!"
hide oraclefuckslow
show oraclefuckfast
call screen oraclefuckfast02x
screen oraclefuckfast02x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("OracleFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("OracleFuckSlowx") 

label OracleFuckEndx:
py "This is so good! You truly are an upstanding MEMBER of the Church!"
mc "I'm about to blow my load, High Priestess!"
stop music
scene oraclefuckcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "FUCK! RHAAA!"
py "Your Holy Seed is in ME! AAAH, I'm cumming a CELESTIAL orgasm!"
scene oraclefuckcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "I've got some more splooge for you, High Priestess! AAARGH!"
py "I can FEEL it! Every MASSIVE cumshot! And it's making me cum too!"
scene oraclefuckcum03 with dissolve
mc "Phew, I hope the Phallus Lord is happy with that offering."
py "I don't know about Him, but I sure am! Mmmh, so yummy... Let me get dressed so I can bid you farewell in an appropriate attire..."
scene oracle03
show pythia02
with dissolve
py "Farewell, \"[name] the Punisher\"!"
jump ExploreGallery

label ExploreGallery04:
scene crater02
mc "That green fog is getting worse. oh, well. Down we go..."
scene crater03
stop music
play music "Sounds/mask.mp3"
show greenmist
with dissolve
mc "I can barely see a thing in this green fog..."
play sound "Sounds/hulkgrowl01.mp3"
"GRRR!"
mc "What was that?"
window hide
hide greenmist
show shehulk01
with dissolve
play sound "Sounds/hulkgrowl01.mp3"
$ renpy.pause(1, hard=True)
mc "An 8ft tall She-Hulk! Fortunately, she seems to be shackled at the ankles..."
sh "AAAAR! MASK....BAD MAN... GRRR!"
play sound "Sounds/hulkgrowl02.mp3"
mc "Maybe she think I'm her captor because of my mask. So I'll remove it."
stop music
show shehulk01b with dissolve
mc "*cough* I'm getting... radioactive sand... *cough*  in my lungs."
scene crater04
show shehulk03
with dissolve
sh "AAAR... COME... BOY... DRINK... MILK... GOOD... SAFE..."
mc "Mmmh, Green Giant milk. Can't be that bad, right?"
hide shehulk03
show shehulk04
with dissolve
play sound "Sounds/sucking.mp3"
mc "Oh wow, it seems to have cured me of my injuries..."
scene crater03 blurred
show shehulk05
with dissolve
sh "MILK... GOOD..."
mc "Yes, very good. Thank you."
sh "Boy... Me... BREED... BABIES!"
mc "Ah. I should have seen this one coming."
mc "Alright, lady. I'll get undressed and show you my mighty HERO COCK."
play sound "Sounds/zipper.mp3"
hide shehulk05
show shehulk06
with dissolve
sh "BOY... BIG COCK... GOOD..."
mc "That's right, she-hulk! And there's plenty of cream sloshing around in my cum factories to satisfy your needs for breeding!"
hide shehulk06
show shehulk07
with dissolve
play sound "Sounds/lick.mp3"
sh "BIG BALLS... SPERM... LOT OF SPERM... *lick*"
mc "Yeah, make them warm and shiny with your tongue... And I'll give you LOTS OF SPERM. AAAH!"
hide shehulk07
show shehulk08
with dissolve
play sound "Sounds/hulkgrowl01.mp3"
sh "GRR! BOY... FUCK... NOW!"
mc "Yeah, OK, I'll fuck you, don't worry! But please don't crush my cock with your ass muscles."
scene crater04 blurred
show shehulkpredoggy01
with dissolve
play sound "Sounds/hulkgrowl02.mp3"
sh "AAAR! NOW!"
mc "Yeah, hang on, I'm trying to get it in... You might be a giant she-hulk, but my cock is still XXXL-sized!"
hide shehulkpredoggy01
show shehulkdoggy00
with fastdissolve
mc "Damn, she's quite tight despite being 8ft tall... Her pussy muscles are gripping my knob... Here we go!"
hide shehulkdoggy00
play music "Sounds/fucksound.mp3"
label SheHulkFuckSlowx:
hide shehulkfast
show shehulkslow
call screen shehulkslow01x
screen shehulkslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SheHulkFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("SheHulkFuckFastx") 

label SheHulkFuckFastx:
mc "I think she wants me to fuck her FASTER."
hide shehulkslow
show shehulkfast
call screen shehulkfast01x
screen shehulkfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SheHulkFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("SheHulkFuckSlowx") 

label SheHulkFuckEndx:
mc "Time to unload in that green pussy..."
stop music
hide shehulkslow
hide shehulkfast
show shehulkcum01
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Yeah, take my seed, She-Hulk! AAAH!"
hide shehulkcum01
show shehulkcum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "RHAA! Gonna paint your skin white again!"
play sound "Sounds/hulkgrowl01.mp3"
mc "Ok, I'll stop and flood your insides... Calm down..."
hide shehulkcum02
show shehulkcum03
with dissolve
mc "There. Is that better?"
play sound "Sounds/womanmoan.mp3"
mc "See, you can have a tender voice. When you're receiving ounces of cum in your womb!"
mc "Now, if you don't mind, I've done my duty and I'll be on my merry way..."
jump ExploreGallery


label ExploreGallery05:
scene basement03
so "There he is, our bigga boy, ready for his milking session. Would-a you like to watch, Special Deep State Agent?"
so "Wait for me and watch over the boy, I will change into my pizza parlor ped*phile gang mafiosa boss outfit."
scene basement04 with dissolve
mc "So, how is it hanging...err...so to speak?"
mg "I've been captured! Please help me mister! *sniff*"
mc "I don't know what to do, sorry buddy. I'd need a quest or something, but you're not on any of my current ones."
window hide
play sound "Sounds/footsteps.mp3"
$ renpy.pause(2.0, hard=True)
mc "Sssh, she's coming back."
stop sound
scene basement05 with dissolve   
mg "NOOOOO! Not again, please Mamma Sofia! You already milked me five times today! *sob*"
so "I need MORE cream from you, my sweet bambino. Your cream is VERY valuable cos you are such a BIGGA STRONG boy!"
mc "Please proceed with the cum extraction Mamma Sofia... I will watch and... err... take notes."
if deepnickname == False:
    so "Of course Special Deep State Agent [name]."
if deepnickname:
    so "Of course, Special Deep State Agent \"[name] the Intruder\"."
label PizzaBasement02x:
so "First, I will fit the merchandise with an XXXXXL-MEGA condom to capture his ENORMOUS boyloads."

scene basement06 with dissolve
play music "Sounds/vibrator.ogg"
so "And I will tease him with my edging stick to get him ROCK-HARD...."
scene basement07 with dissolve
so "See? He got rock-hard and ready for extraction in no time. Mamma Sofia's edging skills are that-a good, ha, my bigga boy?"
play sound "Sounds/boymoan.mp3"
mg "*sob* I... didn't want to get hard but..."
so "Don't-a worry, bambino, just let your juices flow and give Mamma Sofia a LOT of \special pizza sauce\"!"
stop music
scene basement08a with dissolve
so "There you go my bigga boy! Your stallion cock is a perfect fit for my 30-inch-around studcock gripper!"
play music "Sounds/wank.mp3"
scene basement08b with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08a with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08b with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08a with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08b with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08a with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08b with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08a with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08b with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08a with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08b with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08a with fastdissolve
$ renpy.pause(.2, hard=True)
scene basement08b with fastdissolve
$ renpy.pause(.2, hard=True)
stop music
scene basement09 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mg "AAAHHHH!"
so "That's a good-a strong boy! Give Mamma Sofia what-a she wants, a BIG load of young warm-a spunk!"
scene basement10 with dissolve
mg "OOOOH! AAAHHHH!"
so "You see this Special Deep State Agent? Another gallon of cum for-a the client. Now, I just need to empty the condom into the cum storage unit. Easy-peasy."
mc "Damn, how many gallons do you have already????"
so "Oh, A LOT. This boy is the biggest cum supplier I've ever had, that's-a for sure!"
scene basementsofiabackground blurred
show mammasofia01
with dissolve
so "Before you go... I'll show you the automatic cum extraction procedure with the milking-a machine..."
hide mammasofia01
show mammasofia02
with fastdissolve
so "So we can have some fun time together, what do you say? *wink*"
mc "Well, it's not against Deep State regulations so..."
hide mammasofia02
show mammasofia03
with fastdissolve
so "I've seen that bulge in your pants. You are a BIGGA boy too. Big enough for Mamma Sofia to give her a LOTTA OF PLEASURE! Show it to me!"
play sound "Sounds/zipper.mp3"
hide mammasofia03
show mammasofia04
with fastdissolve
so "Mmmmh, Mamma Sofia is VERY impressed, young agent! Your cock is the PERFECT size. This boy is just too big, I don't-a know what the client wants to do with him..."
so "But let's show him how it's done so he's prepared for when he's delivered..."
mg "What? But... Mamma Sofia, please, I don't want to do that, let me go back to my mommy!"
so "Now now, bambino, just watch-a and learn, This STUD will show you the ropes."
scene sofiaprefuck01 with dissolve
mc "First, you moisten her pussy with your fingers to prep her fuckhole for your cock..."
so "Mmh, Mamma Sofia is sssoo wetta already! Please SHOVE IT IN!"
play music "Sounds/womansex02.mp3"
label SofiaFuckSlowx:
hide sofiafast
show sofiaslow
call screen sofiafuckslow01x
screen sofiafuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SofiaFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("SofiaFuckFastx") 

label SofiaFuckFastx:
mc "And now, I'll increase the pace to make her cum big time!"
so "Oooh, yes, Mamma Sofia is COMING!!! AAAH!"
hide sofiaslow
show sofiafast
call screen sofiafuckfast01x
screen sofiafuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SofiaFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("SofiaFuckSlowx") 

label SofiaFuckEndx:
mc "DUMPING MY LOAD INSIDE YOU! AAH!"
stop music
scene sofiafuckcum01 with dissolve
play sound "Sounds/boycum.mp3"
mg "AAAH!"
so "Yes bambini, come together, make Mamma Sofia proud!"
scene sofiafuckcum02 with dissolve
mc "Repainting your body with my cream! RHAAA!"
so "See that, my stronga boy? THIS is how you do it! He's coming EVERYWHERE, women LOVE that!"
mg "But I can't do that, my cum is getting sucked up by the pump! AAAH!"
so "That's because I need another gallon of spunk from you, bambino, so EXPLODE in the tube for Mamma Sofia!"
stop sound
scene sofiafuckcum03 with dissolve
so "I see you're both done... Mmh, and YOUR cum is DELICIOUS!"
scene basementsofiabackground blurred
show mammasofia01
with dissolve    
so "I hope you learnt well, bambino! Just a few more gallons from you and you'll be good-a to go!"
scene basementsofiabackground blurred
show mammasofia01
with dissolve
so "Grazie for your help, Special Agent. I hope you learnt something too..."
mc "I sure did, Mamma Sofia, I sure did... See you another time. I hope."
so "Arrivederci!"
jump ExploreGallery

label ExploreGallery06:
scene native02
show titahontas08
ti "I want to know why you are called \"Humongous White Cock\"... Come back with me behind the teepee."
mc "Alright, now we're talking! I'll show you my HUMONGOUS WHITE COCK and what I can do with it, Titahontas!"
ti "That's what I expect from you! Hurry up, my daughter is sleeping right now."
scene titahontasprefuck01 with fade
ti "Now I see why you are called \"Humongous White Cock\", whiteskin! Let me ride that tremendous pole and show you the pleasure of native pussy!"
play sound "Sounds/lick.mp3"
mc "Oh yeah, never tasted such lovely nipples before too!"
stop sound
scene titahontasprefuck02 with dissolve
ti "You like it when I grind my pussy against your groin?"
mc "Yeah, but I'll LOVE it even more when my dong gets inside it!"
ti "Then let me ride you like a wild mustang!"
play music "Sounds/fucksound.mp3"
label TitahontasSlowx:
hide titahontasfast
hide titahontasfastb
hide titahontasshowb
show titahontasslow
call screen titahontasslow01x
screen titahontasslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TitahontasEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TitahontasFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("TitahontasPOVSlowx") 

label TitahontasPOVSlowx:
hide titahontasfast
hide titahontasfastb
hide titahontasshow
show titahontasslowb   
call screen titahontasslow01bx
screen titahontasslow01bx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TitahontasEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TitahontasPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("TitahontasSlowx") 

label TitahontasFastx:
mc "Yeah, twerk that tight Indian pussy on my cock, Titahontas!"
ti "I can sense you like that, don't you whiteskin?"
hide titahontasslow
hide titahontasfastb
hide titahontasshowb
show titahontasfast
call screen titahontasfast01x
screen titahontasfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TitahontasEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("TitahontasSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("TitahontasPOVFastx") 

label TitahontasPOVFastx:
hide titahontasfast
hide titahontasslowb
hide titahontasshow
show titahontasfastb 
call screen titahontasfast01bx
screen titahontasfast01bx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TitahontasEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("TitahontasPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("TitahontasFastx") 

label TitahontasEndx:
mc "Oh Fuck, you're gonna make me EXPLODE!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene titahontasbouncecum01 with dissolve
ti "Yes, fill me up with your whiteskin sperm!"
scene titahontasbouncecum02 with dissolve
ti "Oh, this is so good, you're cumming inside me so MUCH! You are such a HUMONGOUS WHITE STUD!"
scene titahontasbouncecum03 with dissolve
mc "Phew... That was something else. Nothing like some primeval wild native pussy I must say."
play sound "Sounds/moaning.mp3"
ti "This was sssoo good.... My pussy is pounding to the heartbeat of the wild buffalo. I cannot take anymore of that humongous cock of yours there..."
scene titapreanal01 with dissolve
mc "Well, I'm not done with you, Titahontas! I'm gonna pound that tight ass of yours into submission! Turn round and prepare for my deep anal penetration!"
ti "Where have I heard that before... Fine, do your worse, \"Humongous White Cock\"!"
hide titapreanal01
play channel1 "Sounds/barbarasex.mp3"
play channel2 "Sounds/wank.mp3"
label TitaAnalSlowx:
hide titaanalfast
show titaanalslow
call screen rockslow01x
screen rockslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TitaAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TitaAnalFastx") 

label TitaAnalFastx:
ti "Your cock is... just too HUMONGOUS!"
mc "Then I'll go faster so it will be over FASTER!"
hide titaanalslow
show titaanalfast
call screen rockfast01x
screen rockfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TitaAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("TitaAnalSlowx") 

label TitaAnalEndx:
mc "That's it, I'm on the verge of WHITEWASHING your ass with my spunk!"
stop channel1
stop channel2
play music "Sounds/splooge02.mp3"
scene titaanalcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
ti "Oh my God, i can HEAR it spurt inside my ass!"
scene titaanalcum02 with dissolve
stop music
stop sound
play sound "Sounds/splooge01.mp3"
ti "I'm releasing the overflow! I'M POURING CUM OUT OF MY BACKSIDE!"
stop sound
scene titaanalcum03 with dissolve
mc "Yeah, I did come a lot actually. My balls are drained... Time for me to leave you and your daughter, Titahontas..."
ti "Really? So soon... But you're right, I should go and check on Lolihontas anyway... Let's get dressed."
jump ExploreGallery

label ExploreGallery07:
scene junktown02
show cindybikini02 at right with moveinright
ci "Get the bucket and the soap Taylor, we're ready to show this city boy how we's wash things proper down 'ere."
window hide
show taylorwet01 with moveinleft
to "Heehee..."
play sound "Sounds/waterspray.mp3"
scene junktown02
show junktownwet01 
with dissolve
ci "What are you doing TAYLOR? You're nuttier than a squirrel's turd, you're getting your mamma all wet!"
hide junktownwet01
show taylorbikini01 at left
show cindybikini03 at right
with dissolve
ci "Now look at the mess you've made Taylor! I'm all wet and mah bikini is almost see-thru now."
scene junktown02 blurred
show cindybikini04
with fastdissolve
ci "Well, it’s hotter than blue blazes out here, so I might as well take it off..."
hide cindybikini04
show cindybikini05
with fastdissolve
to "Oh Ma, you're showing your big jugs to this city boy, that's real sugar of you! Mahbe I should do the same then..."
scene junktown02
show cindybikini06 at right
show taylortopless01 at left
with dissolve
ci "Oh look at mah daughter sweet-talking to ya'all. Now let's wash his motorbike like we said we'd do. Go and get the soap and bucket this time Taylor."
hide taylortopless01 with moveoutleft
ci "What's your name boy?"
mc "[name]. The HERO."
show bikewash01 at left with moveinleft
with dissolve
to "Heehee, I've made a mess of the soap, it's all over mah tits now."
ci "TAYLOR! You're a naughty girl, and now I'm gonna have to look just like you so no one's jealous."
scene junktown02 blurred
show bikewash02
with dissolve
ci "Come over and run that sponge over your Ma's skin. I'll use mah tits to wash [name]'s rig, they have more surface than that sponge."
scene junktown03
show bikewash03
with dissolve
ci "Your motorbike is so dirty it don't belong to a hero. We'll make it real clean in no time I reckon."
hide bikewash03
show bikewash04
with dissolve
to "Heehee, you're rubbing your big jugs all over that bike, you're gonna get'em all dirty Ma!"
ci "That way we do the job faster and we get our five bucks faster honey!"
hide bikewash04
show bikewash05
with dissolve
to "Ma, you're cleaning ME instead of the bike, silly!"
ci "I'm just getting the grit out of your skin so you look nice for that city boy. I think we're done 'ere."
mc "Time for me to inspect your handiwork ladies. In my jockstrap cos I like to ride my bike almost commando-style."
scene junktown04
show bikewash06 
with dissolve
play sound "Sounds/gasp.mp3"
to "*gasp* Look, Ma, he's packing more than an inbred country mule!"
stop sound
ci "I sure wish your pa had been hung like that when he knocked me up in high school. And he was mah cousin." 
hide bikewash06
show bikewash07 
with dissolve
mc "Yeah, I like what you did ladies. It's squeaky clean and the brakes now work better than before!"
to "Well, I think we deserve a reward [name] for the work we done, dontcha think?"
scene junktown03
show bikewash08 
with dissolve
ci "He already paid us honey, what else you want from him?"
to "I want to see his great big pecker!"
ci "Well that ain't no manners Taylor! I home trained you better than to ask a city boy to show you his big old fat pud!"
ci "I reckon you should ask sweeter than that."
mc "It's alright, I don't mind one bit. Get on your knees then Taylor and behold..."
scene junktown04
show bikewash09 
with dissolve
mc "...my HERO cock!"
to "Oh, wow, it's even bigger than I hoped it would be! It's a whopper!"
mc "And why don't say hello to him with your mouth Taylor?"
ci "That would be the proper thing to do."
to "I don't know, it's sssoo big I don't think even an Alabama anaconda could swallow that monster!"
ci "Now, now, I brought you up better than to refuse a challenge Taylor. Let me demonstrate, like a good mother would."
scene junktown05
show bikewash10
with dissolve
to "How are you going to do it Ma, [name]'s pud is just so... GIGANTIC!"
ci "You just have to let your lips stretch real wide and it'll fit. Watch and learn Taylor."
scene junktown05 blurred
label BikeBlowSlowx:
play music "Sounds/hardsucking.mp3"
hide bikeblowfast
show bikeblowslow
call screen bikeblowslow01x
screen bikeblowslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BikeBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BikeBlowFastx") 

label BikeBlowFastx:
to "Oh wow, look at how your giant dong is stretching my Ma's lips... Try and gobble his pole faster Ma!"
hide bikeblowslow
show bikeblowfast
call screen bikeblowfast01x
screen bikeblowfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BikeBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BikeBlowSlowx") 

label BikeBlowEndx:
stop music
scene junktown05
show bikewash10
with dissolve
ci "Now it's your turn Taylor. You make me proud, girl, and you get [name] to spew his sauce right down your throat."
to "Oh, wow, Ma, thanks for letting me be the one to swallow his monstercock spunk, that's real sugar of you!"
ci "I'll suck on his juicenuts and make sure he delivers when we wants him to."
scene junktown05 blurred
label BikeBlowSlow02x:
play music "Sounds/hardsucking.mp3"
hide bikeblowfast02
show bikeblowslow02
call screen bikeblowslow02x
screen bikeblowslow02x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BikeBlowEnd02x")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("BikeBlowFast02x") 

label BikeBlowFast02x:
ci "That's mah girl! Now get that log down your throat even faster honey!!"
hide bikeblowslow02
show bikeblowfast02
call screen bikeblowfast02x
screen bikeblowfast02x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("BikeBlowEnd02x")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("BikeBlowSlow02x") 

label BikeBlowEnd02x:
ci "I think he's about to spew his Texas sauce! Open your throat real wide and swallow as much you can Taylor. You don't want to be making a mess of it now do ya?"
stop music
hide bikeblowfast02
hide bikeblowslow02
show taylorblow09
show taylorblowcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "FU-U-UCK!"
hide taylorblowcum01
hide taylorblow09
show taylorblow03
show taylorblowcum02
with fastdissolve
mc "Damn it! She's sucking my load right out of my cumslit! AAAH!"
ci "Now I don't know where you learnt that Taylor but you seem to be givin' that boy some real sugar there!"
hide taylorblowcum02
hide taylorblow03
show taylorblowcum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "I've got more Texas sauce for you ladies, RHAAA!"
ci "PLASTER us in it then [name], I want mah tits to be COVERED in red-hot spunk!"
hide taylorblowcum03
show bikeblowcum05
with dissolve
stop sound
play sound "Sounds/kiss.mp3"
ci "Mmmh, I LOVE slurping that city boy's splooge directly out of your mouth, Taylor!"

mc "FUCK! You country bumpkins really are filthy incels!"
scene junktown02
show cindybikini07
with dissolve
ci "What did you say??? Now that ain't no way to show respect to us ladies, young man!"
ci "You come right 'ere behind me and you fuck me real good to make things right, you hear me, city boy?"
mc "Err... Ok, missus."
to "Oh Ma, you're gonna let this boy fuck your old pussy with his monstercock, that's real sugar of you!"
scene junktown06
show cindyprefuck
with dissolve
ci "No need for any lubing, I'm already dripping with mah own slime, so just SHOVE IT IN!"
scene junktown04
label CindyFuckSlowx:
play music "Sounds/fucksound.mp3"
hide cindyfuckfast
show cindyfuckslow
call screen cindyfuckslow01x
screen cindyfuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("CindyFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("CindyFuckFastx") 

label CindyFuckFastx:
ci "That's it! Pound that fuckhole faster [name]!"
hide cindyfuckslow
show cindyfuckfast
call screen cindyfuckfast01x
screen cindyfuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("CindyFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("CindyFuckSlowx") 

label CindyFuckEndx:
ci "You'd better give me a nice fat creamy load to make up for yar rudeness, boy!"
scene junktown06 blurred
show cindyfuckcum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
to "Oh Ma, he's filling you up like a gas tank!"
ci "That's how you get babies, so watch and learn Taylor!"
mc "FU-UU-UCK! I'll pull out, I'm still cumming full-blast!"
scene junktown04
show cindyfuckcum02
with dissolve
ci "That's a good boy, I'm full anyway, pump that spunk outside of mah overfilled stretched-out pussy."
to "[name]! You're spewing over your own motorbike, silly! You're gonna make it all dirty again!"
scene junktown03c
show bikewash12
with dissolve
to "Now I'm gonna have to clean your mess with mah tongue! *slurp*"
play sound "Sounds/lick.mp3"
$ renpy.pause(2.0, hard=True)
scene junktown05 blurred
show bikewash13
with dissolve
ci "I'll join you Taylor, so we's do it faster and the boy can go with a clean motorbike."
to "That's the last of it... *slurp* All clean mister!"
play sound "Sounds/lick.mp3"
mc "Well, thank you very much ladies. Now I shall bid you farewell, it's getting late..."
stop sound
jump ExploreGallery

label ExploreGallery08:
scene crater03
show hulksexbackground
show magnusmeethulk01 at left with moveinleft
show magnusmeethulk02 at right with moveinright
sh "MAGNUS...MOMMY!"
mg "Mom! Yippee, I found you... (cough)... again!"
mc "That scene's gonna make for fascinating conversation I fear..."
sh "Drink... MOMMY... MILK..."
mc "Yeah, you go ahead buddy, it's good, I can vouch for it. Ahem."
scene crater03 blurred
show hulkmagnusmilk01
with dissolve
play sound "Sounds/sucking.mp3"
mg "Mmmh, just like I remember it."
sh "BABY...GOOD....MOMMY... CHECK ON YOU..."
hide hulkmagnusmilk01
show hulkmagnusmilk02
with dissolve
play sound "Sounds/ripping.mp3"
mc "Oh, oh, she found out about his MONSTER cock. Was bound to happen, right?"
sh "MAGNUS... COCK... SO BIG! MOMMY... LOVE!"
mc "Of course, she's not really human anymore, so it's no longer inc*st at all. Which makes it perfectly suitable for Patreon audiences around the world."
hide hulkmagnusmilk02
show hulkmagnusprelick01
with dissolve
play sound "Sounds/lick.mp3"
mg "But mommy.... What are you doing? AAAH, your tongue... it feel so good!"
mc "You wait till she dislocates her jaws and engulfs your entire helmet, buddy...."
hide hulkmagnusprelick01
show hulkmagnusprelick02
with dissolve
mg "AAAH! MOMMMYYY!"
mc "I think it's about to happen..."
play sound "Sounds/crunch.mp3"
hide hulkmagnusprelick02
show hulksexbackground
show hulkmagnusblow01
with fastdissolve
mg "Mommy... You're swallowing my...."
stop sound
mc "Cock. Yeah, she's blowing you basically. Enjoy."
window hide
play music "Sounds/hardsucking.mp3"
hide hulkmagnusblow01
show hulkmagnusblow02
with fastdissolve
pause 0.2
hide hulkmagnusblow02
show hulkmagnusblow01
with fastdissolve
pause 0.3
hide hulkmagnusblow01
show hulkmagnusblow02
with fastdissolve
pause 0.2
hide hulkmagnusblow02
show hulkmagnusblow01
with fastdissolve
pause 0.3
hide hulkmagnusblow01
show hulkmagnusblow02
with fastdissolve
pause 0.2
hide hulkmagnusblow02
show hulkmagnusblow01
with fastdissolve
pause 0.3
hide hulkmagnusblow01
show hulkmagnusblow02
with fastdissolve
pause 0.2
hide hulkmagnusblow02
show hulkmagnusblow01
with fastdissolve
pause 0.3
hide hulkmagnusblow01
show hulkmagnusblow02
with fastdissolve
pause 0.2
hide hulkmagnusblow02
show hulkmagnusblow01
with fastdissolve
pause 0.3
hide hulkmagnusblow01
show hulkmagnusblow02
with fastdissolve
pause 0.2
hide hulkmagnusblow02
show hulkmagnusblow01
with fastdissolve
pause 0.3
hide hulkmagnusblow01
show hulkmagnusblow02
with fastdissolve
pause 0.2
hide hulkmagnusblow02
show hulkmagnusblow01
with fastdissolve
pause 0.3
play sound "Sounds/boymoan.mp3"
mg "AAAAH!"
mc "Looks like he's about to blow..."
stop music
hide hulkmagnusblow01
show hulkmagnusblowcum01
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mg "OOOOH, I'm pumping my seed in your mouth MOMMMMMYYY!"
mc "Yeah, make her GAG on it, Magnus, I can tell she wants to!"
hide hulkmagnusblowcum01
show hulkmagnusblowcum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
sh "Mmmgggbbb, CUM... SON..."
hide hulkmagnusblowcum02
show hulkmagnusblowcum03
with fastdissolve
sh "MOMMY... PROUD... LOTS OF CUM... NOW FUCK MOMMY..."
mc "Can I join the fuckfest this time She-Hulk pretty please?"
sh "YOU... GIVE ME COCK... IN MOUTH... FUCK MY FACE...."
mc "Alright! Let's do it Magnus, you fuck her giant gaping green pussy with your monstercock and I'll fuck her mouth with mine, okay?"
mg "Err... Okay, mister..."
scene crater04
show hulksexbackground
show hulkmagnusprefuck01
with dissolve
mc "I'm ready, already half my cock is buried in your mom's mouth. Now shove yours into her moist cunt, Magnus!"
mg "I...don't know how it could fit...."
mc "Let the dev worry about that. Her pussy will distend enough for it to fit, trust me."
sh "MAGNUS... FUCK.... MOMMY..."
mg "O...Okay."
scene crater03 blurred
play music "Sounds/fucksound.mp3"
label MagnusFuckSlowx:
hide hulkmagnusfast
hide POVhulkmagnusslow
hide POVhulkmagnusfast
show hulksexbackground
show hulkmagnusslow
call screen hulkmagnusslow01x
screen hulkmagnusslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MagnusFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MagnusFuckFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("MagnusFuckPOVSlowx") 
        
label MagnusFuckPOVSlowx:
hide POVhulkmagnusfast
hide hulkmagnusfast
hide hulkmagnusslow
show POVhulkmagnusslow
call screen hulkmagnuspovslow01x
screen hulkmagnuspovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MagnusFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MagnusFuckPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MagnusFuckSlowx") 

label MagnusFuckPOVFastx:
hide POVhulkmagnusslow
hide hulkmagnusfast
hide hulkmagnusslow
show POVhulkmagnusfast
call screen hulkmagnuspovfast01x
screen hulkmagnuspovfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MagnusFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MagnusFuckPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MagnusFuckFastx") 

label MagnusFuckFastx:
hide hulkmagnusslow
hide POVhulkmagnusslow
hide POVhulkmagnusfast
show hulksexbackground
show hulkmagnusfast
call screen hulkmagnusfast01x
screen hulkmagnusfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MagnusFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MagnusFuckSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("MagnusFuckPOVFastx") 

label MagnusFuckEndx:
mc "God, I'm close..."
mg "Me too, I can't hold it anymore, AAAH!"
hide hulkmagnusslow
hide hulkmagnusfast
hide POVhulkmagnusslow
hide POVhulkmagnusfast
stop music
play channel1 "Sounds/splooge02.mp3"
if persistent.cumsoundon:
    play channel2 "Sounds/mccum.mp3"
scene crater04 blurred
show hulksexbackground
show hulksexcum01
with dissolve
mg "AAAH, MOMMY, I'm cumming inside you!"
mc "Fuck, I'm about to blow too!"
scene crater03 blurred
show hulksexpovcum01
stop channel2
play sound "Sounds/boycum.mp3"
mc "Nutting right down She-Hulk's throat, RHAAAA!"
hide hulksexpovcum01
show hulksexpovcum02
with dissolve
mc "Here, take that on your face She-Hulk!"
sh "SPERM.... GOOOD.... MMMH...."
stop channel1
play sound "Sounds/splooge01.mp3"
mc "Yeah, you like that, hey? Your son is filling you up with his boygoo too what I can hear back there... Why don't you pull out and cover your mom's tits with it Magnus?"
scene crater04 blurred
show hulksexcum02
with dissolve
stop channel1
stop channel2
play sound "Sounds/splooge01.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Hey, watch out where you're aiming those massive jets of spunk buddy!"
sh "MAGNUS SPERM... LOTS OF IT... MOMMMY... SSSOOO PROUD..."
mc "I'm still hard and I have a bit of time. What about youy Magnus, ready for another round?"
mg "Y...Yes, I think so."
sh "YOU TWO... FUCK ME... STANDING UP..."
mc "Alright! I'll take her ass cos I don't think you'll manage to squeeze that THING back there, even in your mom. Maybe in the future, with some practice..."
scene crater05
show hulksexbackground
with dissolve
play channel1 "Sounds/wank.mp3"
play channel2 "Sounds/barbarasex.mp3"
label HulkUpSlowx:
hide hulkupfast
show hulkupslow
call screen hulkupslow01x
screen hulkupslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HulkUpEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("HulkUpFastx") 

label HulkUpFastx:
sh "FUCK ME... FASTER!"
hide hulkupslow
show hulkupfast
call screen hulkupfast01x
screen hulkupfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HulkUpEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("HulkUpSlowx") 

label HulkUpEndx:
mc "That ass is ssso tight... I think I'm gonna cum soon!"
mg "Me...Me too!"
sh "COME... TOGETHER... IN MY HOLES..."
stop channel1
stop channel2
play sound "Sounds/boycum.mp3"
scene crater06
show hulksexbackground
show hulkupcum01
with dissolve
mc "Fuck, blowing right in your poopchute, She-Hulk!"
mg "AAAH, MOMMY, I'm CUMMING AGAIN INSIDE YOU!"
sh "GOOD BOY... CUM...IN MOMMY..."
stop sound
hide hulkupcum01
show hulkupcum02
with dissolve
sh "MMMMH... STILL HARD... FUCK MOMMY MORE..."
scene crater03 blurred
show hulkdiamonds 
with dissolve
mc "Okay, I'm done guys and it's getting late, I'll leave you getting to know each other better..."
jump ExploreGallery

label ExploreGallery09:
scene hippyfire02
$ renpy.pause(1.0, hard=True)
mc "Psychedelic dude, I'm seeing things.... That ganja is strong."
stop music
scene hippykiss01 with psych01
$ renpy.pause(1.0, hard=True)
mc "Oh wow, when did that just happen?"
play sound "Sounds/kiss.mp3"
st "Mmmh..."
play sound "Sounds/womanmoan.mp3"
li "Are you out of your trip, [name]? Why don't you come and join us..."
mc "Oh yeah. What, I'm already naked too? Cool, dude, I don't have to take my clothes off then."
scene hippykiss02 with dissolve
play sound "Sounds/kiss.mp3"
st "Your cock is sssooo BIG! I want it..."
mc "Then come and get it..."
scene hippykiss03 with dissolve
play sound "Sounds/lick.mp3"
st "Like that?"
li "Oooh, I can sense you TREMBLING with anticipation, [name]..."
st "I want to FUCK! Sex is way better when you're totally stoned..."
mc "AAAh, yeah, sure... I'll fuck you... Where am I?"
scene hippiefuckbackground03
show hippyprefuck01
with dissolve
mc "Are you ready girl?"
st "Oh, you aren't in yet? I thought you were. Man, I'm so stoned..."
scene hippiefuckbackground01
show hippiesex00
with fastdissolve
play sound "Sounds/moaning.mp3"
st "AAAH! Now I'm really SURE you're in!"
hide hippiesex00
play music "Sounds/womansex01.mp3"
label HippyFuckaSlowx:
show hippyfuck01slow
hide hippyfuck01fast
call screen hippyfuckaslowx
screen hippyfuckaslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HippyFuckaEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("HippyFuckaFastx")     

label HippyFuckaFastx:
st "Oooh, fuck me faster, cos right now, everything feels ssooo slow..."
show hippyfuck01fast
hide hippyfuck01slow
call screen hippyfuckafastx
screen hippyfuckafastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HippyFuckaEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("HippyFuckaSlowx")     

label HippyFuckaEndx:
mc "Oh, I feel like... I'm going to..."
stop music
hide hippyfuck01fast
hide hippyfuck01slow
show hippiefuckcum01
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "...CU-UM!!!! AAAH!"
st "AAAH, I'm cumming too with your horsecock lodged sssooo DEEP inside me!"
hide hippiefuckcum01
show hippiefuckcum02
with dissolve
mc "RHAAA! Let me plaster your back with my teenage scum! SSSOOO GOOOD!"
scene hippiefuckbackground02
show hippiefuckcum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
st "Please put it back inside me, I want the rest sloshing aroung in my WOMB!"
scene hippiefuckbackground03
show hippiefuckcum04
with dissolve
mc "Alright, here it comes, the last of my cum-salvoes! AAAH"
li "OOoh, I missed out on sssooo much cum..."
mc "Don't worry Livie, I'm still ROCK-HARD and RARING TO GO!"
scene hippiefuckbackground02
show hippyprefuck02
with dissolve
mc "Just let yourself slide down that shaft, Livie..."
st "Looks like there's a LOT of inches to slide down onto!"
li "I'm so stoned I actually think I can do it..."
mc "Time to PROVE IT!"
hide hippyprefuck02
play music "Sounds/womansex02.mp3"
label HippyFuckbSlowx:
show hippyfuck02slow
hide hippyfuck02fast
call screen hippyfuckbslowx
screen hippyfuckbslowx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HippyFuckbEnd")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("HippyFuckbFastx")     

label HippyFuckbFastx:
li "I LOVE bouncing up and down your fat boymeat!"
show hippyfuck02fast
hide hippyfuck02slow
call screen hippyfuckbfastx
screen hippyfuckbfastx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HippyFuckbEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("HippyFuckbSlowx")     

label HippyFuckbEndx:
li "Come inside me please! I want it, I want your LOAD!"
mc "AAAH, here it comes BLASTING, Livie!"
stop music
hide hippyfuck02slow
hide hippyfuck02fast
show hippiesex02cum01
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
li "Ooh, it's pumping inside my womb like a firehose! SSSOOO MUCH SWEET YOUNG CUM! MORE!"
mc "There's more where that came from!"
li "Show me, GIVE ME MORE!"
hide hippiesex02cum01
show hippiesex02cum02
with dissolve
mc "There, FUCKING CU-UU-MMING!"
st "Look at how POWERFUL he blasts his spunk all over your back! Just like he did with me... What a STALLION!"
li "I'm cumming too! AAAH! And cum is still pouring out of my overfilled snatch!"
scene hippiefuckbackground03
show hippiesex02cum03
with dissolve
mc "Phew! Ladies, I think I should go... I don't know how I'll ride back home cos I don't even know where is home but it ain't here and they'll be looking for me if I don't go back..."
jump ExploreGalleryb

label ExploreGallery10:
scene cloister04
show mothertheresa02
show sistermary01 at left
show sisteranna01 at right
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
label AnnaMouthSlowx:
hide annamouthfast
show annamouthslow
call screen annamouthslow01x
screen annamouthslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AnnaMouthEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AnnaMouthFastx") 

label AnnaMouthFastx:
hide annamouthslow
show annamouthfast
call screen annamouthfast01x
screen annamouthfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AnnaMouthEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AnnaMouthSlowx") 

label AnnaMouthEndx:
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
jump ExploreGalleryb
    
label ExploreGallery11:
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
play music "Sounds/womansex02.mp3"
label TheresaSlowx:
hide theresafuckfast
hide theresafuckpovslow
hide theresafuckpovfast
scene cloister23
show theresafuckslow
call screen theresafuckslow01x
screen theresafuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TheresaEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TheresaFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("TheresaPOVSlowx") 

label TheresaPOVSlowx:
hide theresafuckslow
hide theresafuckfast
hide theresafuckpovfast
scene cloister22 blurred
show theresafuckpovslow
call screen theresafuckpovslow01x
screen theresafuckpovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TheresaEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TheresaPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("TheresaSlowx") 

label TheresaFastx:
mt "I need to... *puff* ... ride him FASTER and make him NUT!"
hide theresafuckslow
hide theresafuckpovslow
hide theresafuckpovfast
scene cloister23
show theresafuckfast
call screen theresafuckfast01x
screen theresafuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TheresaEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("TheresaSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("TheresaPOVFastx") 

label TheresaPOVFastx:
hide theresafuckslow
hide theresafuckfast
hide theresafuckpovslow
scene cloister22 blurred
show theresafuckpovfast
call screen theresafuckpovfast01x
screen theresafuckpovfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TheresaEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("TheresaPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("TheresaFastx") 
            
label TheresaEndx:
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
mt "You'll know soon enough, sister Mary. It's YOUR TURN NOW!"
scene cloister27
show maryprefuck01
with dissolve
mc "That's it, lick my balls and get them to churn another MONSTER LOAD for you!"
mt "Not monstrous, simply GODLY AND HOLY!"
sa "I am so ENVIOUS! Getting impregnated by such a SUPERIOR bullcock!"
play music "Sounds/womansex02.mp3"
label MarySlowx:
hide maryfuckfast
hide maryfuckpovslow
hide maryfuckpovfast
scene cloister20
show maryfuckslow
call screen maryfuckslow01x
screen maryfuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MaryFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("MaryPOVSlowx") 

label MaryPOVSlowx:
hide maryfuckslow
hide maryfuckfast
hide maryfuckpovfast
scene cloister08 blurred
show maryfuckpovslow
call screen maryfuckpovslow01x
screen maryfuckpovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("MaryPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MarySlowx") 

label MaryFastx:
mt "Fuck her HARDER and FASTER! SHe's been a vile sinful creature!"
sm "Oh yes, I HAVE!"
hide maryfuckslow
hide maryfuckpovslow
hide maryfuckpovfast
scene cloister20
show maryfuckfast
call screen maryfuckfast01x
screen maryfuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("MarySlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("MaryPOVFastx") 

label MaryPOVFastx:
hide maryfuckslow
hide maryfuckfast
hide maryfuckpovslow
scene cloister08 blurred
show maryfuckpovfast
call screen maryfuckpovfast01x
screen maryfuckpovfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("MaryEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("MaryPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("MaryFastx") 
            
label MaryEndx:
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
label AnnaSlowx:
hide annafuckfast
show annafuckslow
call screen annafuckslow01x
screen annafuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AnnaFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("AnnaPussySlowx") 

label AnnaFastx:
mt "Fuck her ass HARDER and FASTER! She deserves an ANAL punishment!"
sa "Oh yes, my ass has been so NAUGHTY!"
hide annafuckslow
show annafuckfast
call screen annafuckfast01x
screen annafuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AnnaSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/pussyview.png"
        hover "Icons/pussyview.png"
        action Jump ("AnnaPussyFastx") 
            
label AnnaPussySlowx:
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
        action Jump ("AnnaEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AnnaPussyFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/POVview.png"
        hover "Icons/POVview.png"
        action Jump ("AnnaPOVSlowx") 

label AnnaPussyFastx:
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
call screen annafuckpussyfast01x
screen annafuckpussyfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AnnaEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("AnnaPussySlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/POVview.png"
        hover "Icons/POVview.png"
        action Jump ("AnnaPOVFastx") 
            
label AnnaPOVSlowx:
hide annafuckpussyslow
hide annafuckpussyfast
hide annafucktopfast
scene cloister08 blurred
show annafucktopslow
call screen annafuckpovslow01x
screen annafuckpovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AnnaEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("AnnaPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AnnaPussySlowx") 

label AnnaPOVFastx:
hide annafuckpussyslow
hide annafuckpussyfast
hide annafucktopslow
scene cloister08 blurred
show annafucktopfast
call screen annafuckpovfast01x
screen annafuckpovfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AnnaEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("AnnaPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("AnnaPussyFastx") 
            
label AnnaEndx:
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
jump ExploreGalleryb

label ExploreGallery12:
stop music
play music "Sounds/shower.mp3"
scene wendyshower01
we "What are you waiting for [name]?"
scene wendyshower02 with dissolve
mc "I'm right here behind you..."
scene wendyshower03 with dissolve
we "Ooh, and what's that HUGE thing I feel nudging between my ass cheeks?"
mc "That would be my HUGE cock. Still soft but getting hard fast... Cos your body is smoking hot!"
scene wendyshower04 with fastdissolve
we "Oh my, what are we going to do about it? I know. I'll make it go down with my expert hands!"
stop music
scene wendyshower05 with fastdissolve
we "What a MASSIVE fuckstick. I'm gonna have to use BOTH hands on such a MONSTER."

label WendyHandSlowx:
play music "Sounds/wank.mp3"
hide wendyhandfast
show wendyhandslow
call screen wendyhandslow01x
screen wendyhandslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyHandEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WendyHandFastx") 

label WendyHandFastx:
we "You like that, don't you? A two-handed jacking of your monster cock... I'll go faster for you..."
hide wendyhandslow
show wendyhandfast
call screen wendyhandfast01x
screen wendyhandfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyHandEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WendyHandSlowx") 

label WendyHandEndx:
mc "Aah, gonna cum Wendy!"
we "Give me a CUM SHOWER, please!"
stop music
scene wendyhandcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "There you goooo! RHAAA!"
scene wendyhandcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
we "Yes, aim it at my tits, COVER THEM WITH YOUR CREAM!"
scene wendyhandcum02 with fastflash
mc "AAAH, can't stop CUMMMMMIINNNGGG!"
scene wendyhandcum03 with dissolve
stop sound
we "Oh my God, look at HOW MUCH you came! There's TONS of it. I'm gonna have to take ANOTHER shower..."
mc "Phew! And I need to go back to my compound, they'll be asking too many questions otherwise..."
we "Don't forget to COME BACK and get a even BETTER reward, [name]!"
mc "Sure will do, Wendy."
jump ExploreGalleryb

label ExploreGallery13:
stop music
play music "Sounds/shower.mp3"
scene wendyshower01
we "Come over here [name]. You and your HUGE COCK!"
scene wendyshower02 with dissolve
mc "I'm right here behind you..."
we "Now that I've seen how GIGANTIC and POWERFUL that fuckpole of yours is, I want to FEEL it INSIDE ME!"
mc "And I'm ROCK-HARD and READY for that!"
scene wendyshower04 with dissolve
we "Indeed you are... Let me turn the shower off and suck on that FAT DONG!"
stop music
scene wendyshower05 with dissolve
we "Are you ready, big boy?"
mc "Fuck yeah!"

label WendyBlowSlowx:
play channel1 "Sounds/hardsucking.mp3"
play channel2 "Sounds/boymoan02.mp3"
hide wendyblowfast
show wendyblowslow
call screen wendyblowslow01x
screen wendyblowslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WendyBlowFastx") 

label WendyBlowFastx:
mc "Get ready, I'm going to fuck your mouth faster!"
hide wendyblowslow
show wendyblowfast
call screen wendyblowfast01x
screen wendyblowfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WendyBlowSlowx") 

label WendyBlowEndx:
mc "AAh, gonna blow down your throat, Wendy!"
stop channel1
stop channel2
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene wendyblowcum01 with dissolve
mc "Oh God, that's it, right down your THROAT! AAAH!"
scene wendyblowcum02 with dissolve
play music "Sounds/splooge02.mp3"
mc "Here, let me help you!"
scene wendyblowcum02 with fastflash
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "Ssssooo, so GOOD! RHAAA!"
stop music
scene wendyblowcum03 with dissolve
we "You FILLED my stomach UP! I can feel your dirty spunk sloshing inside me... There's... too much of it!"
mc "Come on now, just swallow like a good girl, this is unbecoming..."
scene wendyblowcum04 with dissolve
we "Alrigh,t I'm feeling better now..."
mc "Good, cos we haven't fucked yet and I'm still ROCK-HARD!"
we "Pound me from behind with that giant log!"
    
label WendyFuckSlowx:
play music "Sounds/fucksound.mp3"
hide wendyfuckfast
show wendyfuckslow
call screen wendyfuckslow01x
screen wendyfuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WendyFuckFastx") 

label WendyFuckFastx:
mc "Fuck, that pussy is sssoo nice, I'm just gonna have to pound it faster!"
we "Yes, do it, STUD!"
hide wendyfuckslow
show wendyfuckfast
call screen wendyfuckfast01x
screen wendyfuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WendyFuckSlowx") 

label WendyFuckEndx:    
we "Oh God, I'm cumming again, you're fucking me so goooood!"
mc "And I'm about to..."
scene wendyfuckcum01 with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "...blow too! RHAAA!"
we "My pussy is being filled to the brim with your cream! AAAH!"
scene wendyfuckcum01 with fastflash
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "God, can't stop cumming!"
scene wendyfuckcum02 with dissolve
stop sound
we "I see you've made a big mess all over my back, you naughty boy... I'm going to have to take yet ANOTHER shower!"
scene wendyfuckcum03 with dissolve
mc "No time for that. I'm still hard and I want to fuck that lovely ARSE of yours!"
we "What? You're gonna fuck me some more after you just dumped TWO HUGE LOADS all over me???"
mc "Your hot bod is making me THAT horny!"

label WendyAnalSlowx:
play music "Sounds/fucksound.mp3"
hide wendyanalfast
show wendyanalslow
call screen wendyanalslow01x
screen wendyanalslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("WendyAnalFastx") 

label WendyAnalFastx:
we "I love feeling your giant log in my ass while I'm dripping with your load, it's so hot, but please FUCK ME FASTER!"
hide wendyanalslow
show wendyanalfast
call screen wendyanalfast01x
screen wendyanalfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("WendyAnalEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("WendyAnalSlowx") 

label WendyAnalEndx:
we "Oh God, I'm cumming again, you're fucking me so goooood!"
mc "And I'm about to..."
scene wendyanalcum01 with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "...blow too! RHAAA!"
we "My ass is being filled to the brim with your cream! AAAH!"
scene wendyanalcum01 with fastflash
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "God, can't stop cumming!"
scene wendyanalcum02 with dissolve
play sound "Sounds/splooge01.mp3"
we "AAAH, you're so DEEP in my ass!"
scene wendyanalcum02 with fastflash
mc "A few... more... shots, AAAAh!"
we "I can't take it anymore, my legs are failing me..."
scene wendyanalcum03 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
we "You're STILL hosing me down? My ass... It's leaking your cream like a faucet... I've never been... fucked so HARD in my life!"
scene wendyanalcum04 with dissolve
stop sound
mc "Phew, I think you've drained me for good this time."
we "Let me recover... And meet me at the wooden dock."
scene swamphouse01 blurred
show wendy11
with fade
we "I'm gonna have to take ANOTHER shower now, you've COVERED me in your yummy cum!"
mc "About that promise of yours..."
we "OK, show me your map and I'll tell you where Trumpf City is, I THINK..."
hide wendy11
show wendy12
with dissolve
we "Mmmh, I would say... Hex G3. Yep, definitely, that one."
mc "Thanks for the IMPORTANT tip, Wendy!"
hide wendy12
show wendy11
with dissolve
we "You're welcome, come back ANYTIME you want, STUD..."
jump ExploreGalleryb

label ExploreGallery14:
scene junktown01 
show cindy01 at right
show taylorbride01 at left with moveinleft
to "Oh, hi [name]! Is it true? you're gonna make me happier than a puppy with two peckers?"
mc "Err... Yeah, That's correct."
hide cindy01
show cindy03 at right
with fastdissolve
ci "Now we just need to find someone else, cos we need at least two witnesses in the One-Eye of our Lord down 'ere in Texas..."
mc "As it happens, I came with someone, I'll go and get her!"
hide cindy03
show cindy01 at right
with fastdissolve
ci "And I'll get my New Bible."
to "Yippee, I'm going to get knocked up by a super-huge whopper!"
scene junktownfar
show bellaout09
with fade
be "So, are you ready to go back to the compound [name]?"
mc "Err.. Not quite. I need you to do something for me. Be a witness to a totally religious ceremony."
be "What's that?"
mc "I'm getting married. You'll be a witness."
hide bellaout09
show bellaout08
with fastdissolve
be "I see... Are you serious about this or is it just you being stupidly young and horny?"
mc "I'm dead serious! I need to re-populate the Earth for our Phallus Lord, remember?"
be "Alright then, I'll do it..."
scene junktown03 with fade
play sound "v06/wedding.mp3"
show taylorwedding01 at left with moveinleft
show weddingbella01 at right with moveinright
ci "In the name of our Phallus Lord, we are here to witness the breeding... sorry wedding, between Taylor and [name]. May they be fertile and re-populate the Earth. Se-men."
be "Se-men."
ci "You may kiss the bride. And then fuck her."
hide taylorwedding01
show taylorwedding02 at left
hide weddingbella01
show weddingbella02 at right
with fastdissolve
to "Oooh, [name], you're sssoo romantic. This breeding is going to be PERFECT!"
mc "And err... Where are we supposed to do it by the way?"
ci "Well, in the back of the van, where else are you gonna make a baby in Texas?"
be "Dare I ask you to hurry up? We need to get back to the compound soon..."
ci "Let's just go sunbathin' while they do their stuff. I bet he knocks up mah daughter real good and fast."
stop sound
scene taylorfucksetup
show taylorprefuck01
with dissolve
to "So, I'm READY! Are you ready to fuck me and BREED ME, [name]?"
mc "Why don't you take off your wedding dress for me, Tayl... I mean, my darling wife."
hide taylorprefuck01
show taylorprefuck02
with fastdissolve
to "Of course, hubby! See your wife's panties? They're darn wet for your whopper!"
mc "I see... Why don't you turn round while I get... hard."
hide taylorprefuck02
show taylorprefuck03
with fastdissolve
to "I hope I'm SEXY enough to get you ROCK-HARD so you can really give it to me HARD!"
show mctaylorprefuck03 at farright with moveinright
"Oh, I'll give it to you HARD, don't worry Taylor!"
to "Look at that HUGE whopper! Come and kiss me, darling husband..."
hide taylorprefuck03
hide mctaylorprefuck03
show mctaylorprefuck04
with fastdissolve
play sound "Sounds/kiss.mp3"
to "*kiss* Please, BREED ME!"
mc "Lie back on the van mattress then, I'll show you how it's done."
scene pretaylorfuck01 with dissolve
play sound "Sounds/gasp.mp3"
to "Oh my Golly, your cock is just so big! How is it going to enter into my tight little virgin pussy [name]?"
mc "With all the pre-goo I'm producing right now, quite easily as a matter of fact. Let me demonstrate..."
play music "v06/taylorfuck.mp3"
label TaylorSlowx:
hide taylorfuckfast
hide taylorfuckpovslow
hide taylorfuckpovfast
show taylorfuckslow
call screen taylorfuckslow01x
screen taylorfuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TaylorEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TaylorFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("TaylorPOVSlowx") 
        
label TaylorPOVSlowx:
hide taylorfuckfast
hide taylorfuckslow
hide taylorfuckpovfast
show taylorfuckpovslow
call screen taylorfuckpovslow01x
screen taylorfuckpovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TaylorEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TaylorPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("TaylorSlowx") 

label TaylorPOVFastx:
hide taylorfuckfast
hide taylorfuckslow
hide taylorfuckpovslow
show taylorfuckpovfast
call screen taylorfuckpovfast01x
screen taylorfuckpovfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TaylorEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("TaylorPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("TaylorFastx") 

label TaylorFastx:
hide taylorfuckslow
hide taylorfuckpovslow
hide taylorfuckpovfast
show taylorfuckfast
call screen taylorfuckfast01x
screen taylorfuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TaylorEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("TaylorSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("TaylorPOVFastx") 

label TaylorEndx:
mc "I'm gonna BREEEEDDD YOU!"
to "Please hubby, fill me up like a spermtank!"
scene taylorfuckcum01 with dissolve
stop music
play music "Sounds/splooge02.mp3"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
scene taylorfuckcum01 with fastflash
mc "RHAAA! Take my seed Taylor!"
stop music
scene taylorfuckcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "I'm coming right up your womb! AAAH!"
play sound "Sounds/splooge01.mp3"
to "I can sure darn feel it, hubby! My belly is SWELLING with your cum!"
scene taylorfuckcum03 with dissolve
mc "Phew, that tight virgin pussy of yours DRAINED me."
to "So, am I a good wife?"
mc "Oooh yeah, you're a perfect cum-draining wife Taylor!"
to "Quick, get dressed, I hear Ma coming back!"
scene taylorfucksetup
show taylorpostfuck01 at left
with fade
show cindy06 at farright with moveinright
ci "So, did you knock up mah daughter real good [name]?"
mc "I'm pretty sure I did my duty."
to "Oh, yes Ma, I'm BURSTING with my hubby's bull-sized load! He came sssooo much in me, I'm dang leaking cum everywhere!"
ci "Well, lemme check... Like a good mother would do."
scene taylorpostfuck02 with dissolve
play sound "Sounds/slurp.mp3"
ci "That's darn good, boy, this is a high-grade quality sperm."
be "Sorry to interfere with your family reunion, but [name] and I need to go now, it's getting late and we are expected back at the compound."
scene taylorpostfuck03 with dissolve
to "Can I come with you hubby?"
ci "Certainly not Taylor! Your place is down 'ere in Texas with your Ma. Your husband will do his conjugal duty and come and visit you once a week to breed you until you get a baby."
mc "And if I don't come cos I'm too busy saving the world and all that?"
ci "Most likely, mah daughter's lust for you will go down I reckon..."
mc "I see. At least, there aren't any maintenance fees, right?"
ci "We girls can take care of ourselves. Huntin' varmint and such with our guns."
mc "Well, I'll be on my way then. See you my darling wife... err, Taylor, right?"
to "Yes, my name is Taylor, mah darling hubby!"
be "Let's go, \"Darling Hubby\"."
jump ExploreGalleryb

label ExploreGallery15:
$ heathercumbx = False
$ heathercumax = False
scene diamondharem01b
show warriorchief01
play music "v07/diamondmusic.mp3"
di "Ah, there you are. It took a while for my Warriors to find you."
mc "What is this place?"
hide warriorchief01
show warriorchief03
with fastdissolve
di "This is in MY harem, hex E3, where you are at MY mercy."
if renpy.seen_image("strippershow01"):
    mc "What do you want from me? By the way, is that Suk-Yu over there? And who's the other big-titted chick? She looks hot."
if renpy.seen_image("strippershow01") == False:
    mc "What do you want from me? And who are these two big-bosomed beauties behind you?"
hide warriorchief03
show warriorchief02
with fastdissolve
di "They're MY harem girls, and they will NEVER be yours, you hear me?"
hide warriorchief02
show warriorchief03
with fastdissolve
if renpy.seen_image("strippershow01"):
    di "However, as it turns out, I did bring you here because of them. And because I saw your \"performance\" with Suk-Yu at the stripclub in Desert Town... "
if renpy.seen_image("strippershow01") == False:
    di "However, as it turns out, I did bring you here because I heard about you... And your ALPHA-cock."
hide warriorchief03
show warriorchief04
with fastdissolve
if renpy.seen_image("strippershow01"):
    di "You seem to be the ideal person to help me decide whether to keep her as my feature stripper or... replace her with Heather over there."
if renpy.seen_image("strippershow01") == False:
    di "You seem to be the ideal person to help me decide whether to keep Suk-Yu as my feature stripper or... replace her with Heather over there."
hide warriorchief04
show warriorchief02
with fastdissolve
di "So go and meet them both, they know why you're here..."
scene haremsukyu01 with dissolve
if renpy.seen_image("strippershow01"):
    mc "*Oh yeah, I remember that big-titted Asian stripper...*"
if renpy.seen_image("strippershow01") == False:
    mc "*Fuck yeah, damn those titties are HUGE!...*"
scene haremsukyu02 with dissolve
if renpy.seen_image("strippershow01"):
    sy "Well, hello [name], fancy meeting YOU here..."
    mc "I'm always where the HOT action is!"
if renpy.seen_image("strippershow01") == False:
    sy "Well, hello there, we haven't had the PLEASURE to meet yet..."
    mc "The pleasure is all mine at the moment..."
scene haremsukyu03 with dissolve
if renpy.seen_image("strippershow15"):
    sy "My pussy is still tingly from the feeling of your MASSIVE teenage fucktool plowing through it..."
    mc "And I'm getting hard remembering how great your DEEP Asian pussy felt impaled on my giant shaft!"
if renpy.seen_image("strippershow15") == False:
    sy "By the looks of that BULGE on you, you could easily fill up my very DEEP Asian pussy... What do you think?"
    mc "Oh yeah, I'm sure I could. I'd hit the back of your womb with my GIANT teenage cock for sure!"
scene haremsukyu04 with dissolve
if renpy.seen_image("strippershow15"):
    sy "Oh, you're watching my tits, aren't you? I never got to WRAP them around your rockhard shaft... I think you would enjoy that A LOT, wouldn't you?"
if renpy.seen_image("strippershow15") == False:
    sy "Oh, you're watching my tits, aren't you? Can you imagine how good they'd feel WRAPPED around your MONSTER shaft... I think you would enjoy that A LOT, wouldn't you?"
mc "Damn, you're getting me ROCKHARD Suk-Yu!"
di "Now move on and check out Heather, my new recruit..."
scene haremheather01 with dissolve
mc "*Well, what do we have here?... That's a DDD-cup AT LEAST!"
scene haremheather02 with dissolve
he "Chief Diamond told me about you.. How you like girls with HUGE bazongas... Because you have such a HUMONGOUS lovepole. Is that true?"
mc "She's damn right, BIGGEST ROD in the country!"
scene haremheather03 with dissolve
he "And I have the biggest JUGGS you'll ever encounter... Imagine how BLISSFUL your shaft would feel lodged between these two puppies?"
mc "Fuck yeah!"
scene haremheather04 with dissolve
he "That much titflesh rubbing against your sensitive veins as your cock gets harder than a bar of steel, ready to EXPLODE all over them!"
mc "Oh damn, my cock is trying to pierce a hole through my pants right now, if you'll excuse me young lady..."
scene diamondharem01b
show diamond01
with dissolve
mc "Errr, you're naked too? Wow, this harem is PARADISE!"
di "You won't be fucking me if that's what you were thinking!"
hide diamond01
show diamond02
with fastdissolve
di "But I'll be having FUN with my two harem girls on the other hand!"
hide diamond02
show diamond03
with fastdissolve
mc "What the fuck? You're a FUTA???"
di "You don't get to rise to my position as Chief of the Road Warriors without some MANLY equipment!"
mc "You're... You're going to fuck me with this, is that what this is all about you sick PERVERT?"
di "Don't FLATTER yourself, you're just a piece of meat to me! And I ain't attracted to MEN."
hide diamond03
show diamond04
with fastdissolve
di "What I want you to do for me is to be a test suject. A customer waiting to be so entirely and completely satisfied that he will fork out heavy tips and come back for more."
mc "Alright! I like that! Way more than gettng fucked up the arse by your futa dick!"
di "The future of these girls depends on the wisdom of your judgment."
mc "I am wise beyond my age, trust me, everybody says so!"
di "We'll start with a cock-licking session. Get naked and get hard [name], and girls, get on either side of his pillar!"
stop music
scene diamondlickbackground
show diamondprelick01 with dissolve
he "It's so big mister! I've never seen such a MOUTHFUL!"
sy "He's actually bigger than my King Dong dildo, which I use for one of MY main attractions as the FEATURE STRIPPER OF THE BLUE OYSTER!"
di "Stop talking and start LICKING!"
hide diamondprelick01
show diamondlick00
with dissolve
mc "Oh God, this is going to be GOOD!"
hide diamondlick00
play channel1 "Sounds/lick.mp3"
play channel2 "v07/lick02.ogg"
label DiamondLickSlowx:
hide diamondlickfast
show diamondlickslow
call screen diamondlickslow01x
screen diamondlickslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DiamondLickEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DiamondLickFastx") 

label DiamondLickFastx:
di "Go on girls, show him what you're capable of doing... I want the customer to cum UNDER 2 minutes max!"
hide diamondlickslow
show diamondlickfast
call screen diamondlickfast01x
screen diamondlickfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DiamondLickEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DiamondLickSlowx") 

label DiamondLickEndx:
di "That's it, he's ready to BURST. I can see his veins throbbing and his cumslit expanding!"
hide diamondlickslow
hide diamondlickfast
show diamondlickcum01
with dissolve
stop channel1
stop channel2
mc "Fuck, AAAAH!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
he "Oh my God, I've never seen such a MASSIVE jet of boyspunk!"
with fastflash
sy "He's cumming like a STALLION!"
hide diamondlickcum01
show diamondlickcum02
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
he "It's flying so HIGH up in the air, you're going to get plastered with the stuff, boss!"
with fastflash
di "Don't worry about me, keep holding his shaft and let it FLY!"
hide diamondlickcum02
show diamondlickcum03
with fastdissolve
di "Nice one girls, that was WELL UNDER two minutes..."
mc "I... I fell drained. And I need to go back to the compound, it(s getting late already. So I will bid you g..."
di "Where do you think you're going?"
hide diamondlickcum03
show diamondpretit01
with dissolve
di "Your cock is still in functioning order.  And we're FAR from over!"
mc "Oh, dear Lord, I'm going to be la..."
hide diamondpretit01
show diamondtit00
with dissolve
he "We're ready whenever you say so, Chief Diamond..."
di "Good, and I'll massage his balls with my feet while you girls rub those huge shaft-pleasing tits all over his throbbing manhood."
sy "Ready to cover our boobs in a GIANT boyload [name]?"
he "I want AT LEAST an inch-thick layer of your splooge all over my ENORMOUS bosom!"
scene diamondlickbackground blurred
play channel1 "v07/twogirls.mp3"
play channel2 "Sounds/wank.mp3"
hide diamondtit00
label DiamondTitSlowx:
hide diamondtitfast
show diamondtitslow
call screen diamondtitslow01x
screen diamondtitslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DiamondTitEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DiamondTitFastx") 

label DiamondTitFastx:
di "Keep going girls, rub that titflesh against his shaft even FASTER and make him ERUPT!"
hide diamondtitslow
show diamondtitfast
call screen diamondtitfast01x
screen diamondtitfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DiamondTitEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DiamondTitSlowx") 

label DiamondTitEndx:
hide diamondtitslow
hide diamondtitfast
show diamondtitcum01
with dissolve
stop channel2
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH, those monster tits are making me CUM!"
with fastflash
di "Keep rubbing his shaft and DRAIN HIM, girls!"
scene diamondtitcumbackground blurred
show diamondtitcum02
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
with dissolve
he "Mmmh, look at how HIGH his cumshots are going!"
with fastflash
sy "He's PLASTERING us with his young boycream, it's ALL OVER THE PLACE!"
hide diamondtitcum02
show diamondtitcum03
with dissolve
stop sound
stop channel1
di "That was a nice BIG load you gave us there... But some of our customers want MORE than a titfuck. So let's move on to the MAIN COURSES!"
he "Please, can I go first, boss? I've been stretching my pussy and I'm sure I can take it and bring him over the edge in less than two minutes!"
if renpy.seen_image("strippershow15"):
    sy "I did that when he visited me in Desert Town in a minute flat!"
if renpy.seen_image("strippershow15") == False:
    sy "My more experienced pussy is what this boy needs to make him cum HARDER THAN EVER BEFORE!"
di "Don't worry girls, you'll both have your turn. But Heather will go first and you will show me your handjob skills..."
sy "Sure thing Chief Diamond!"
scene heathercumbackground03
show heatherprefuck01
with dissolve
he "See that nice, tight, young pussy [name]? It's all yours. RAM your dick in there and feel my warmth engulf your shaft until you can't stop cumming!"
scene heathercumbackground03
show heatherprefuck02
with dissolve
mc "Oh God... Yes, I will do it!"
he "It will make you spew your sauce in no time!"
play music "v07/heatherfuck.mp3"
label HeatherFuckSlowx:
scene heatherfuckbackground
show heatherfuckslow
call screen heatherfuckslow01x
screen heatherfuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HeatherFuckEndAx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("HeatherFuckFastx") 
    imagebutton:
        focus_mask True
        idle "v07/sukyuview.png"
        hover "v07/sukyuview.png"
        action Jump ("DiamondSukYuSlowx") 

label DiamondSukYuSlowx:
play sound "Sounds/zarahandjob.mp3"
scene diamondsukyubackground01 blurred
show diamondsukyuslow
call screen diamondsukyuslow01x
screen diamondsukyuslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HeatherFuckEndBx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DiamondSukYuFastx") 
    imagebutton:
        focus_mask True
        idle "v07/heatherview.png"
        hover "v07/heatherview.png"
        action Jump ("HeatherFuckSlowx") 

label HeatherFuckFastx:
scene heatherfuckbackground
show heatherfuckfast
call screen heatherfuckfast01x
screen heatherfuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HeatherFuckEndAx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("HeatherFuckSlowx") 
    imagebutton:
        focus_mask True
        idle "v07/sukyuview.png"
        hover "v07/sukyuview.png"
        action Jump ("DiamondSukYuFastx") 

label DiamondSukYuFastx:
play sound "Sounds/zarahandjob.mp3"
scene diamondsukyubackground01 blurred
show diamondsukyufast
call screen diamondsukyufast01x
screen diamondsukyufast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HeatherFuckEndBx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("DiamondSukYuSlowx") 
    imagebutton:
        focus_mask True
        idle "v07/heatherview.png"
        hover "v07/heatherview.png"
        action Jump ("HeatherFuckFastx") 
            
label HeatherFuckEndAx:
$ heathercumax = True
he "Come on STUD, I want to feel your POWERFUL shots BLASTING away inside my womb! Do it!"
mc "Hang on, I'm getting close..."
scene heathercumbackground01 blurred
show heatherfuckcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
stop music
play music "v07/heathercumming.mp3"
mc "RHAAA, that's IT! Your pussy is making me ERUPT!"
scene heathercumbackground02 blurred
show heatherfuckcum02
with dissolve
he "I'm cumming too, this is soo good!"
with fastflash
he "Douse my HUGE TITS with the rest of your GIGANTIC load please!"
scene heathercumbackground03 blurred
show heatherfuckcum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "You asked for it, RHAAA!"
with fastflash
he "Oh, I LOVE IT! MORE, MORE!"
stop music
if heathercumbx:
    jump DiamondSessionNextx
play sound "Sounds/zarahandjob.mp3"
scene diamondsukyubackground01 blurred
show diamondsukyuslow
with dissolve
label HeatherFuckEndBx:
$ heathercumbx = True
sy "Boss, I can feel your cock TREMBLING, are you ready to COVER ME in your futa-cum?"
di "Just keep pumping away Suk-Yu...and I'll..."
scene diamondsukyubackground01
show diamondsukyucum01
with dissolve
stop music
play sound "Sounds/moaning02.mp3"
di "....CUM!"
with fastflash
sy "Oh boss, you had sssoo much futa-sperm left for me in your balls... Let me massage them for you..."
hide diamondsukyucum01
show diamondsukyucum02
with fastdissolve
di "Wh.. What are you doing? OOOOH, I'm cumming even MORE!"
sy "It's my special new technique to DRAIN customers, boss! You like it?"
with fastflash
di "Y...Yeah, AAAHHH!"
scene diamondlickbackground blurred
show diamondsukyucum03
with dissolve
play sound "Sounds/lick.mp3"
sy "Mmmmh, it's... delicious, boss!"
if heathercumax:
    jump DiamondSessionNextx
if heathercumax == False:
    play music "v07/heatherfuck.mp3"
    scene heatherfuckbackground
    show heatherfuckslow
    with dissolve
    jump HeatherFuckEndAx

label DiamondSessionNextx:
stop music
stop sound
scene diamondhighbackground blurred
show diamondhigh01
with dissolve
di "OK, time to switch partners. You take Suk-Yu and I'm gonna bang Heather's sweet pussy..."
he "Oooh, I can't wait boss!"
sy "And I can't wait to get STRETCHED by [name]'s MONSTERCOCK!"
scene heathercumbackground01
show sukyuprefuck01
with fade
sy "You're going to fuck me HARD [name]? I LOVE it DEEP and POWERFUL!"
play sound "Sounds/moaning.mp3"
mc "Damn, not only are your tits amazing but so is that tight arse... I'm going to POWERFUCK you doggy-style then!"
scene diamondheatherbackground01
show diamondheatherprefuck01
with dissolve
he "Are you ready for me to impale myself on your ALPHA-FUTA cock, boss?"
di "Oh yeah, you're making me so ROCKHARD Heather, GET DOWN ON IT!"

play music "v07/heatherfuck.mp3"
label SukYuFuckSlowx:
scene heathercumbackground01
show sukyufuckslow
call screen sukyufuckslow01x
screen sukyufuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukYuFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("SukYuFuckFastx") 
    imagebutton:
        focus_mask True
        idle "v07/heatherview.png"
        hover "v07/heatherview.png"
        action Jump ("DiamondHeatherSlowx") 

label DiamondHeatherSlowx:
scene diamondheatherbackground01
show diamondheatherslow
call screen diamondheatherslow01x
screen diamondheatherslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukYuFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DiamondHeatherFastx") 
    imagebutton:
        focus_mask True
        idle "v07/sukyuview.png"
        hover "v07/sukyuview.png"
        action Jump ("SukYuFuckSlowx") 

label SukYuFuckFastx:
sy "Please PILE-DRIVE your mammoth dong into me FASTER!"
scene heathercumbackground01
show sukyufuckfast
call screen sukyufuckfast01x
screen sukyufuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukYuFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("SukYuFuckSlowx") 
    imagebutton:
        focus_mask True
        idle "v07/heatherview.png"
        hover "v07/heatherview.png"
        action Jump ("DiamondHeatherFastx") 

label DiamondHeatherFastx:
di "Go on Heather, fuck my futa cock FASTER!"
scene diamondheatherbackground01
show diamondheatherfast
call screen diamondheatherfast01x
screen diamondheatherfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukYuFuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("DiamondHeatherSlowx") 
    imagebutton:
        focus_mask True
        idle "v07/sukyuview.png"
        hover "v07/sukyuview.png"
        action Jump ("SukYuFuckFastx") 
            
label SukYuFuckEndx:
sy "Are you about to PUMP YOUR SEED inside me [name]? I can't wait to feel your GIANT jets of jizz!"
mc "Oh God, you're spurring me on... I..."
scene heathercumbackground01 blurred
show sukyufuckcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
stop music
play music "Sounds/splooge02.mp3"
sy "Oh YES, I LOVE being filled up by a young stud-shota's sweet cum!"
with fastflash
mc "I'm giving it ALL, ALL OF MY NUTJUICE! AAAH!"
scene sukyucumbackground blurred
show sukyufuckcum02
with dissolve
sy "Oooh, you're already DRIPPING out of my tight Asian fuckhole, there's SSOOO MUCH of your sweet nectar!"
with fastflash
mc "I have some MORE for you Suk-Yu!"
stop music
hide sukyufuckcum02
show sukyufuckcum03
with dissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "More pumped-up shota cum for you Suk-Yu! AAAH!"
with fastflash
sy "Mmmh, it feels so SCALDING on my back [name], you're my BEST customer!"
mc "Phew, that's cos you bring out the BEST in me Suk-Yu!"

play music "Sounds/womansex01.mp3"
scene diamondheatherbackground01 blurred
show diamondheatherfast
with dissolve
di "I'm ready to unleash a torrent of my futa-cum inside you Heather!"
he "Go on boss, do it, I'm ready!"
hide diamondheatherfast
show diamondheathercum01
with dissolve
stop music
play sound "Sounds/moaning02.mp3"
di "I'm cumming!"
with fastflash
he "So am I boss, your cock feel sssooo good pumping its jizz inside my tender pussy!"
hide diamondheathercum01
show diamondheathercum02
with dissolve
he "Oooh? You're still BLASTING your BIG load all over my back!"
with fastflash
di "Damn girl, I never cam so much, AAAHH!"
scene diamondheatherbackground01 blurred
show diamondheathercum03
with dissolve
play sound "Sounds/kiss.mp3"
he "Mmmh, boss... You're the best... And I hope I was the BEST for YOU!"
di "Get cleaned up girls, I need to talk with my test subject..."    
jump ExploreGalleryb

label ExploreGallery16:
scene newaliens02
mc "That's it, it's the END. I'm about to die. In a game where no one dies, what a pathetic death that will b..."
window hide
play sound "v071/spaceshipdoor.mp3"
show aliengirl01 at left with dissolve
show alien02girl01 at right with dissolve
alg01 "Oh my Glod, it's HIM!"
alg02 "Oh my Glod, oh my Glod, I'm wetting my panties right now, I'm so excited!"
hide aliengirl01
show aliengirl04 at left
with fastdissolve
alg01 "All the girls at Glorglimbo High are going to be sssooo jealous!"
hide alien02girl01
show alien02girl03 at right
with fastdissolve
alg02 "When we show them the pictures of us getting fucked by the biggest sex appendage in the galaxy!"
hide aliengirl04
show aliengirl01 at left
with fastdissolve
alg01 "Please give us an autograph, \"Earthling Stallion\"!"
mc "So my intergalactic nickname is \"Earthling Stallion\"? Interesting..."
hide aliengirl01
show aliengirl04 at left
with fastdissolve
alg01 "Yes, you're the biggest Kunt-Popping Star on our planet!"
alg02 "Your sex romps are watched by over 200 trillion delirious preteen Glorglan girls each week!"
hide alien02girl03
show alien02girl03 at right
with fastdissolve
alg02 "And we're the FIRST ones to find you and meet you in the flesh!"
mc "What's in it for me though?"
hide aliengirl04
hide alien02girl03        
show aliengirl03 at left
show alien02girl02 at right
with fastdissolve
alg01 "What? You ask for something in return? When you have the opportunity to bang the two hottest girls of Glorglimbo High?"
mc "Wee, err.... I mean, I'm the star here, ain't I?"
hide alien02girl02
show alien02girl01 at right
with fastdissolve
alg02 "Fine, what do you want?"
mc "I want to be paid. In dollars, not Glorgonubs."
alg01 "Alright, we'll give you 30 of your pitiful and useless dollars that we stole from some guy wandering the desert."
mc "That's better, I'll definitely whore myself out to some intergalactic invasion force for that amount of money, no problemo."
hide alien02girl01
show alien02girl03 at right
with fastdissolve
alg02 "And now that you got what you wanted, let's get NAKED and have some FUN!"
hide aliengirl07
hide aliengirl03
show aliengirl06 at left
with fastdissolve
alg01 "So drop those trousers and show us your \"Earthling Stallion\" Megadong!"
hide alien02girl03
show alien02girl01 at right
with fastdissolve
alg02 "And we'll show you OUR MEGATONGUES!"
hide aliengirl06
hide alien02girl01
show aliengirl08 at left
show alien02girl05 at right
with fastdissolve
alg01 "Oh wow, it's just as BIG as I imagined it from those VHS videos!"
hide alien02girl05
show alien02girl06 at right
with fastdissolve
alg02 "I bet he can really fuck my tight purple pussy REAL DEEP!"
stop music
scene alienslick01 with dissolve
play music "Sounds/lick.mp3"
mc "Ooooh, how... How are you doing this?"
alg01 "Ggglll, our glllongues are... extendaglgggllle and ....pregglllhensile...."
scene alienslick02 with dissolve
alg02 "Glllyou like gglllthat , don't ya?"
mc "Oh damn, your tongues are... rubbing all over my shaft, it's sssooo goood!"
scene alienslick03 with dissolve
alg01 "We're the best cocklickers on Glorglon, that's why!"
stop music
play music "v071/alienslick.mp3"
show alienslickanim
call screen alienslickanimx
screen alienslickanimx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("AliensLickEndx")

label AliensLickEndx:
mc "God damn, I can't hold it any longer!"
scene alienslick04 with dissolve
stop music
mc "FUCK, AAAHH!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
alg02 "Glllast away!"
scene alienslick04 with fastflash
alg01 "Wglwe want gllbbmore! GLMUCH MORE!"
scene alienslick05 with dissolve
mc "You're PUMPING THE CUM OUT OF ME, OOOOH!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene alienslick05 with fastflash
mc "There's more, you're coaxing sso much spunk out of my sperm factories, RHAAA!"
scene alienslick06 with dissolve
stop sound
mc "Phew, you alien girls certainly know your way around a soda-thick shaft... With those tongues of yours. So, can I go now?"
alg01 "We're only JUST GETTING STARTED!"
scene aliens02prefuck01 with dissolve
play sound "Sounds/panting.mp3"
alg02 "You'd better have some MORE hot loads in those monster nuts of yours, earthling! Cos we ain't satisfied till we can show our friends your dong stuffed INSIDE our juicy pussies!"
mc "Stop it, you're choking me!"
alg01 "Will you FUCK ME GOOD? I NEED to know."
mc "Y...Yes, yes I WILL!"
alg02 "Let's check if this cock is truly ROCKHARD then..."
scene aliens02prefuck02 with dissolve
play sound "Sounds/slap.mp3"
alg01 "Oooh, I LIKED the sound of that massive slab of fuckmeat THUMPING your chest!"
mc "Then let me go and I'll show you what I can do with it! I'll fuck you girls so HARD I'll send your pussies back to whatever fucking galaxy you cray-ay-zy guys come from!"
alg02 "Oooh, is that so? Let him go Glaty, I want to see if he REALLY can deliver on this promise..."
alg01 "Bring that fat pussy-splitter over to my fuckhole! I'm gonna lie down on your filthy Earth, that'll make the sex even more DIRTY!"
scene alien01prefuck01 with dissolve
alg01 "I'm ready to receive your \"Earthling Stallion\" mega-dick inside my baby-hole!"
scene alien01prefuck02 with fastdissolve
play sound "v071/cockslap.mp3"
mc "Oh yeah? And how bad do you want it, hey?"
scene alien01prefuck01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene alien01prefuck02 with fastdissolve
play sound "v071/cockslap.mp3"
$ renpy.pause(0.4, hard=True)
scene alien01prefuck01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene alien01prefuck02 with fastdissolve
play sound "v071/cockslap.mp3"
$ renpy.pause(0.4, hard=True)
alg01 "Stop teasing me and SHOVE it in, please!"
scene alien01prefuck01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene alien01prefuck02 with fastdissolve
play sound "v071/cockslap.mp3"
$ renpy.pause(0.4, hard=True)
mc "And where should I come after I'm done with you, you dirty preteen Glorglan girl?"
scene alien01prefuck01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene alien01prefuck02 with fastdissolve
play sound "v071/cockslap.mp3"
$ renpy.pause(0.4, hard=True)
alg01 "Pump it all inside my baby-hole!"
mc "I thought you didn't want to get pregnant with zillions of spawns?"
alg02 "She's on the pill, silly! Every preteen is on the pill on Glorglon, until they reach 13 glorglyears. That's about 90 of your inferior years."
mc "You guys are CRAY-AY..."
alg01 "Stop talking and start FUCKING!"
scene aliensfuckanimb00
play music "Sounds/aliensex.mp3"
label Aliens01FuckSlowx:
hide aliens01fuckfast
show aliens01fuckslow
call screen aliens01fuckslow01x
screen aliens01fuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("Aliens01FuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("Aliens01FuckFastx") 

label Aliens01FuckFastx:
alg02 "Come on, show us why you're the biggest Kunt-Popping star on Glorglon, FUCK HER FASTER!"
hide aliens01fuckslow
show aliens01fuckfast
call screen aliens01fuckfast01x
screen aliens01fuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("Aliens01FuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("Aliens01FuckSlowx") 

label Aliens01FuckEndx:
alg01 "Oh, he's fucking me so good, AAAH, I'm coming AGAIN!"
alg02 "It's time for you to DELIVER, \"Earthling Stallion\"! Pump your sub-species seed inside her fuckhole, so I can have a go on that monster prong!"
mc "Just a sec... AAAH, yes, it's coming! I can feel it in my balls!"
scene alien01fuckcum01 with fastdissolve
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
alg01 "I can feel it! He's pumping his Earthling seed inside me! AAAH!"
scene alien01fuckcum02 with dissolve
play sound "Sounds/splooge02.mp3"
mc "FUCK AAAAH! Damn it, you dirty preteen Glorglan sex-addict!"
window hide
with fastflash
show alien01fuckcum02b with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
alg02 "Your belly is SWELLING with his unending streams!"
window hide
with fastflash
alg01 "Yes, he's really DUMPING an INTERGALACTIC LOAD IN ME, I LOVE IT, AAAHH!"
scene alien01fuckcum03 with dissolve
play sound "Sounds/panting.mp3"
mc "Phew, I hope you don't get pregnant, I don't want to have to maintain ten zillions babies, I don't have enough money for that..."
alg02 "Enough of your nonsensical sub-species talk, I NEED that cock and I need it NOW!"
scene aliensprefuck01 with dissolve
alg02 "But first, let me make SURE this cock is EXTRA-HARD for me..."
mc "Oh God, what are you doing?"
play sound "Sounds/lick.mp3"
scene aliensprefuck02 with dissolve
alg02 "Hold him still while I suck his vital life essence out of him, Glaty!"
alg01 "He ain't going nowhere Glaren! Do it, SUCK HIM DRY!"
show alien02suck
play music "Sounds/hardsucking.mp3"
call screen alien02suck01x
screen alien02suck01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("Alien02SuckEndx")    
label Alien02SuckEndx:
hide alien02suck
stop music
scene aliensprefuck04 with dissolve
alg02 "Yeah, that was a nice APPETIZER. Now let's move on to the REAL FUCK SESSION!"
alg01 "You heard her, \"Earthling Stallion\", get into the Gloglinary position!"
stop music

scene alien02prefuck01 with fastdissolve
$ renpy.pause(0.4, hard=True)
mc "That's it, I've had enough, now I'm in charge and I'm gonna POUND my dong into you!"
scene alien02prefuck02 with fastdissolve
play sound "v071/cockslap.mp3"
$ renpy.pause(0.4, hard=True)
mc "Hear that? That's the sound of my POWERFUL pussy-tamer! It can tame ANY pussy, even a Glorglan one!"
play sound "Sounds/moaning02.mp3"
alg02 "Oooh, you're such an intergalactic STUD!"
scene alien02prefuck01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene alien02prefuck02 with fastdissolve
play sound "v071/cockslap.mp3"
$ renpy.pause(0.4, hard=True)
scene alien02prefuck01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene alien02prefuck02 with fastdissolve
play sound "v071/cockslap.mp3"
$ renpy.pause(0.4, hard=True)
scene alien02prefuck01 with fastdissolve
$ renpy.pause(0.4, hard=True)
scene alien02prefuck02 with fastdissolve
play sound "v071/cockslap.mp3"
$ renpy.pause(0.4, hard=True)
mc "Damn right I am! Now get ready, I'm going to IMPALE you on this thing!"
alg01 "Fuck her HARD, I'll film everything with my mini-VHS camera for the girls back home!"

play music "Sounds/womansex01.mp3"
label Aliens02FuckSlowx:
hide aliens02fuckfast
show aliens02fuckslow
call screen aliens02fuckslow01x
screen aliens02fuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("Aliens02FuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("Aliens02FuckFastx") 

label Aliens02FuckFastx:
mc "So you like my stallion cock, hey, alien girl?"
alg02 "YES! I love it... It's sssooo massive!"
mc "Then let me shove it in even FASTER!"
hide aliens02fuckslow
show aliens02fuckfast
call screen aliens02fuckfast01x
screen aliens02fuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("Aliens02FuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("Aliens02FuckSlowx") 

label Aliens02FuckEndx:
mc "Oh, I'm getting close!"
alg01 "Give her all you've got left of your babyjuice \"Earthling Stallion\", we want to show our friends how we coaxed THREE HUGE NUTLOADS OUT OF YOU!"
stop music
scene alien02fuckcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "That's it, take it you little alien sex-fiend!"
window hide
with fastflash
alg02 "PLASTER me with it, I want to have a photo of me taken with your earthling juices ALL OVER ME!"
scene alien02fuckcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "That's for you then, RHAAA!"
window hide
with fastflash

scene alien02fuckcum03 with dissolve
play sound "Sounds/moaning.mp3"
alg02 "I'm CAKED in his HOT baby-cream...Aaaah..."
alg01 "You did good, just as we expected, \"Earthling Stallion\"... Now let's get dressed, we don't want to be seen like this on this filthy planet."
scene newaliens02
show aliengirl05 at left
show alien02girl01 at right
with fastdissolve
mc "So, what channel will this hot romp be aired on?"
hide aliengirl05
show aliengirl04 at left
with fastdissolve
alg01 "Channel? Oh boy, you're such an old-timer! Even if you're only 2 Glorglyear-old..."
hide alien02girl01
show alien02girl02 at right
with fastdissolve
alg02 "Doh! We'll be streaming it on our galactic FikFok account OBVIOUSLY!"
hide aliengirl04
show aliengirl03 at left
with fastdissolve
alg01 "Glaren, let's leave this planet, it's full of total losers."
$ money += 20
mc "Hey! We're not losers, we're WINNING! Even getting tired of it actually."
hide alien02girl02
show alien02girl04 at right
with fastdissolve
alg02 "Wha-tever! See you old-timer. In your GRAVE!"
window hide
hide alien02girl04
hide aliengirl03
with dissolve
play sound "v071/spaceship.mp3"
scene newaliens01 blurred
show alienship at alienshipmoveout
$ renpy.pause(2.0, hard='True')
mc "Thanks God they're gone. FOR GOOD!"
stop sound
jump ExploreGalleryb

label ExploreGallery17:
play music "v07/datemusic.mp3"
scene sukyupreharem01
sy "Hello [name], you can't get enough of my big tits, can you?"
mc "I certainly can't. Best tits in the land, Suk-Yu!"
sy "Then let me show them better to you..."
scene sukyupreharem02 with dissolve
play sound "Sounds/moaning.mp3"
sy "Ooh, I can feel something getting really BIG between my legs..."
mc "That would be my cock. Hard for YOU!"
sy "Let me suck it for you [name]. I want to hold it in my hands and feel it down my throat."
scene sukyupreblow01 with dissolve
sy "You really have the BIGGEST fuckstick in the land. Anf those balls... I just have to play with them, they are so MASSIVE.."
mc "Please Suk-Yu, just blow me, I can't stand it!"
sy "Alright big boy... I'll play with your balls and your asshole to enhance your pleasure while I give you the best blowjob of your life!"
stop music
play music "Sounds/hardsucking.mp3"
label SukyuBlowSlowx:
hide sukyublowfast
show sukyublowslow
call screen sukyublowhugeslow01x
screen sukyublowhugeslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukyuBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("SukyuBlowFastx") 

label SukyuBlowFastx:
mc "Your lips are so warm... And that finger in my ass, you're a real PRO, OOOH!"
hide sukyublowslow
show sukyublowfast
call screen sukyublowhugefast01x
screen sukyublowhugefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukyuBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("SukyuBlowSlowx") 

label SukyuBlowEndx:
mc "I... I think I'm about to blow my load Suk-Yu!"
stop music
scene sukyublowcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Damn it, oh my GOoooooOOOODDDD!"
with fastflash
scene sukyublowcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
sy "Yeah, keep BLASTING that white boy cream all over my Asian MILF boobs [name]!"
with fastflash
mc "I can't STOP, AAAH!"
scene sukyublowcum03 with dissolve
sy "You've COVERED me in your nasty spunk.. *slurp*"
mc "Now it's my turn to return the favor Suk-Yu. I wanna taste that sweet pussy of yours... And prep it for by rod."
scene sukyupostblow01 with dissolve
play music "Sounds/lick.mp3"
sy "OOOh, you're such a naughty boy... Licking my Asian MILF pussy like that..."
scene sukyupostblow02 with dissolve
play sound "Sounds/moaning03.ogg"
mc "Ah yes, I recognize the cliched and stereotypical ahegao face made by Asian women during sex the world over."
stop music
scene sukyupostblow03 with dissolve
mc "I think you're nice and slippery down there and therefore... READY to take on my teenage monsterdong!"
scene sukyuprestand01 with dissolve
sy "Oh I AM READY, believe it! Please FUCK ME SENSELESS!"
mc "You asked for it..."
hide sukyuprestand01
play music "Sounds/womansex02.mp3"
label SukStandSlowx:
hide sukstandfast
show sukstandslow
call screen sukstandhugeslow01x
screen sukstandhugeslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukStandEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("SukStandFastx") 

label SukStandFastx:
sy "Pound me HARDER and FASTER, I know you can do it, just pound the shit out of me!!"
hide sukstandslow
show sukstandfast
call screen sukstandhugefast01x
screen sukstandhugefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukStandEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("SukStandSlowx") 

label SukStandEndx:
sy "COme on, STUD! Pump a STALLION dose of cum inside me!"
stop music
scene sukstandcum01 with dissolve
play music "v07/creampie.mp3"
mc "Ohhhh, Here it comes!"
with fastflash
sy "You're delivering so much sweet young cream inside me, even after having cum so much earlier!"
scene sukstandcum02 with dissolve
mc "That's cos your hot bod is making me so HORNY, RHAAA!"
with fastflash
sy "Please, pull out and shower me with your hot spunk!"
stop music
scene sukstandcum03 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
sy "Look at the SIZE of these cumshots!"
with fastflash
mc "HUGE cumshots for a huge-titted babe, Suk-Yu, AAAH!"
with fastflash
sy "Oh fuck, this is so good! And you're such a FILTHY boy to be licking YOUR cum off my Asian MILF tits like that!"
if renpy.seen_image("sukyupredp") == False:
    scene sukstandcumend with dissolve
    he "That was an amazing POWERFUCK, [name]! Thanks for coming by. *wink*"
    jump ExploreGalleryb
if renpy.seen_image("sukyupredp"):
    scene sukstandcum04 with dissolve
    di "That was a HOT display... And watching you two got me HARD and HORNY!"
    mc "Ho-Ho... I think she means to DP you, Suk-Yu."
    sy "What, both of your big cocks at once in my poor holes?"
    di "I've got a better idea, both of our cocks at once in ONE hole. Your tight pussy!"
    menu:
        "FUCK YEAH!":            
            jump SukYuDPx
        "No, but my innocent futaphobic eyes cannot take in such a lewd display so let's skip to the end.":
            jump ExploreGalleryb

label SukYuDPx:
scene diamondheatherbackground01
show sukyupredp 
with dissolve
sy "Oh my God, how will your BIG cocks ever fit? They will STRETCH me out ssoo much!"
mc "Just give it a try. It will prep you for money-making gangbangs I reckon..."
scene diamondheatherbackground01 blurred
play music "Sounds/scarlettpound.mp3"
label SukyuDPSlowx:
hide sukyudpfast
show sukyudpslow
call screen sukyudphugeslow01x
screen sukyudphugeslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukyuDPEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("SukyuDPFastx") 

label SukyuDPFastx:
mc "Let's kick it up a notch, shall we?"
hide sukyudpslow
show sukyudpfast
call screen sukyudphugefast01x
screen sukyudphugefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("SukyuDPEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("SukyuDPSlowx") 

label SukyuDPEndx:
play sound "Sounds/moaning.mp3"    
sy "I've never been stretched so much before in my life! AAAH, I'm cumming!"
mc "I'm close..."
di "Same here, anytime..."
scene diamondheatherbackground01 blurred
show sukyudpcum01
with dissolve
play music "Sounds/splooge02.mp3"
play sound "Sounds/bothcum.mp3"
mc "...NOW, RHAAA!"
with fastflash
di "My futa cock is unloading too, OOOOH!"
with fastflash
sy "I can feel both of your cocks blasting inside me, AAAHH!"
hide sukyudpcum01
show sukyudpcum02
with dissolve
sy "You're BOTH still going so STRONG, this is the BEST FUCK EVER!"
with fastflash
sy "But I need to see those BIG cocks erupting one last time..."
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
hide sukyudpcum02
show sukyudpcum03
with dissolve
sy "Look at those thick plumes of viscous cream! Mmmh, my tits are getting covered!"
scene heathercumbackground02
show sukyudpcum04
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
sy "You're still going [name]? You're a TRUE STALLION!"
with fastflash
mc "FUCK, YEAH, AH, FUCK!!!!!"
with fastflash
mc "That's the last of it, I'm gonna faint!"    
jump ExploreGalleryb

label ExploreGallery18:
play music "v07/datemusic.mp3"
scene heatherpreharem01
he "Hello [name], you can't get enough of my big tits, can you?"
mc "I certainly can't. Best tits in the land, Heather!"
he "Then come and fondle them..."
scene heatherpreharem02 with dissolve
play sound "Sounds/moaning.mp3"
he "Mmmh, your strong hands on my breasts feel real nice... And I can feel something getting really BIG between my legs..."
mc "That would be my cock. Hard for YOU!"
he "Let me suck it for you [name]. I want to hold it in my hands and feel it down my throat."
scene heatherpreblow01 with dissolve
he "You really have the BIGGEST fuckstick in the land. It looks so TASTY too."
mc "Please Heather, just blow me, I can't stand it!"
he "Alright big boy... I'll play with your balls and your asshole to enhance your pleasure while I give you the best blowjob of your life!"
stop music
play music "Sounds/hardsucking.mp3"
label HeatherBlowSlowx:
hide heatherblowfast
show heatherblowslow
call screen heatherblowhugeslow01x
screen heatherblowhugeslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HeatherBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("HeatherBlowFastx") 

label HeatherBlowFastx:
mc "Your lips are so warm... And that finger in my ass, you're a real PRO, OOOH!"
hide heatherblowslow
show heatherblowfast
call screen heatherblowhugefast01x
screen heatherblowhugefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HeatherBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("HeatherBlowSlowx") 

label HeatherBlowEndx:
mc "I... I think I'm about to blow my load Heather!"
stop music
scene heatherblowcum01 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Damn it, oh my GOoooooOOOODDDD!"
with fastflash
scene heatherblowcum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
he "Yeah, keep BLASTING that teenage boy cream all over my monster boobs [name]!"
with fastflash
mc "I can't STOP, AAAH!"
scene heatherblowcum03 with dissolve
he "You've COVERED me in your nasty spunk.. *slurp*"
mc "Now it's my turn to return the favor, Heather. I wanna taste that sweet pussy of yours... And prep it for by rod."
scene heatherpostblow01 with dissolve
play music "Sounds/lick.mp3"
he "OOOh, you're such a naughty boy... Licking my horny wet pussy like that..."
scene heatherpostblow02 with dissolve
play sound "Sounds/moaning03.ogg"
he "AAAAH! You're making me CCUUUUMMMM!"
stop music
scene heatherpostblow03 with dissolve
mc "I think you're nice and slippery now down there and therefore... READY to take on my teenage monsterdong!"
scene heatherprestand01 with dissolve
he "Oh I AM READY, believe it! Please FUCK ME SENSELESS!"
mc "You asked for it..."
hide heatherprestand01
play music "Sounds/womansex02.mp3"
label HeatherStandSlowx:
hide heatherstandfast
show heatherstandslow
call screen heatherstandhugeslow01x
screen heatherstandhugeslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HeatherStandEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("HeatherStandFastx") 

label HeatherStandFastx:
he "Pound me HARDER and FASTER, I know you can do it, just pound the shit out of me!"
hide heatherstandslow
show heatherstandfast
call screen heatherstandhugefast01x
screen heatherstandhugefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HeatherStandEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("HeatherStandSlowx") 

label HeatherStandEndx:
he "COme on, STUD! Pump a STALLION dose of cum inside me!"
stop music
scene heatherstandcum01 with dissolve
play music "v07/creampie.mp3"
mc "Ohhhh, Here it comes!"
with fastflash
he "You're delivering so much sweet young cream inside me, even after having cum so much earlier!"
scene heatherstandcum02 with dissolve
mc "That's cos your hot bod is making me so HORNY, RHAAA!"
with fastflash
he "Please, pull out and shower me with your hot spunk!"
stop music
scene heatherstandcum03 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
he "Look at the SIZE of these cumshots!"
with fastflash
mc "HUGE cumshots for a huge-titted babe, Heather, AAAH!"
with fastflash
he "Oh fuck, this is so good! And you're such a FILTHY boy to be licking YOUR cum off my tits like that!"
if renpy.seen_image("heatherpredp") == False:
    scene heatherstandcumend with dissolve
    he "That was an amazing POWERFUCK, [name]! Thanks for coming by. *wink*"
    jump ExploreGalleryb
if renpy.seen_image("heatherpredp"):
    scene heatherstandcum04 with dissolve
    di "That was a HOT display... And watching you two got me HARD and HORNY!"
    mc "Ho-Ho... I think she means to DP you, Suk-Yu."
    he "What, both of your big cocks at once in my poor holes?"
    di "I've got a better idea, both of our cocks at once in ONE hole. Your tight pussy!"
    menu:
        "FUCK YEAH!":            
            jump HeatherDPx
        "No, but my innocent futaphobic eyes cannot take in such a lewd display so let's skip to the end.":
            jump ExploreGalleryb

label HeatherDPx:
scene diamondheatherbackground01
show heatherpredp 
with dissolve
he "Oh my God, how will your BIG cocks ever fit? They will STRETCH me out ssoo much!"
mc "Just give it a try. It will prep you for motherhood I reckon..."
scene diamondheatherbackground01 blurred
play music "Sounds/scarlettpound.mp3"
label HeatherDPSlowx:
hide heatherdpfast
show heatherdpslow
call screen heatherdphugeslow01x
screen heatherdphugeslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HeatherDPEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("HeatherDPFastx") 

label HeatherDPFastx:
mc "Let's kick it up a notch, shall we?"
hide heatherdpslow
show heatherdpfast
call screen heatherdphugefast01x
screen heatherdphugefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("HeatherDPEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("HeatherDPSlowx") 

label HeatherDPEndx:
play sound "Sounds/moaning.mp3"    
he "I've never been stretched so much before in my life! AAAH, I'm cumming!"
mc "I'm close..."
di "Same here, anytime..."
scene diamondheatherbackground01 blurred
show heatherdpcum01
with dissolve
play music "Sounds/splooge02.mp3"
play sound "Sounds/bothcum.mp3"
mc "...NOW, RHAAA!"
with fastflash
di "My futa cock is unloading too, OOOOH!"
with fastflash
he "I can feel both of your cocks blasting inside me, AAAHH!"
hide heatherdpcum01
show heatherdpcum02
with dissolve
he "You're BOTH still going so STRONG, this is the BEST FUCK EVER!"
with fastflash
he "But I need to see those BIG cocks erupting one last time..."
stop music
hide heatherdpcum02
show heatherdpcum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
he "Look at those thick plumes of viscous cream! Mmmh, my tits are getting covered!"
scene heathercumbackground02
show heatherdpcum04
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
he "You're still going [name]? You're a TRUE STALLION!"
with fastflash
mc "FUCK, YEAH, AH, FUCK!!!!!"
with fastflash
mc "That's the last of it, I'm gonna faint!"
jump ExploreGalleryb

label ExploreGallery19:
show container01
show krista01
play music "v07/datemusic.mp3"
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
de "What you're doing, babe?"
kr "Nuffin. I lost an earring but it dropped between my mounds."
hide derek05 
show derek04 at midright
with fastdissolve
de "Now fuck off back to your gallery instead of oglin' my wife's tits!"
jump ExploreGalleryc

label ExploreGallery20:
scene fbi01
fo "Subject 42. SUBJECT 42! WAKE UP!"
scene fbi02 with dissolve
mc "Uh? AAAH, I can't see anything, I'm BLIND!"
da "No you're not. Activate Google mental goggles, Siri."
play sound "Sounds/interfacestart.mp3"
scene fbibackground02
show dana07a at right
show fox04 at left
with dissolve
if mcdeep <= 4:
    da "There, now, can you see, [name]?"
if mcdeep == 5:
    da "There, now, can you see, Special Field Agent [name]?"
mc "Yeah. Phew. Err... Why are you half-naked, Agent Dana?"
hide dana07a
show dana10 at right
with fastdissolve
da "I'm NOT half-naked. What you are seeing is your own mental projection of me. Which means you're a pervert. We'll have to do something about that later."
hide fox04
show fox03 at left
with fastdissolve
fo "At least he's not gay, I'm not naked."
mc "That's a relief!"
hide dana10
show dana07b at right
with fastdissolve
da "Now concentrate [name]. This is not a test, this is a Real-Life Mental Event."
mc "Oh, you took your bra off. Nice tits, Agent Dana."
hide dana07b
show dana08 at right
with fastdissolve
da "No, YOU took my bra off! In your mind."
mc "Ah yes, sorry, my bad."
hide fox03
show fox02 at left
fo "He's right though, you do have a nice pair. Like, for real."
hide dana08
show dana09 at right
da "Shut up, Agent Fox! Can we get on with the test or what?"
mc "I thought it wasn't a test, I'm confused now."
da "*sigh*. Get out of the mental projection, Agent Fox, I think it's best if I stay alone with [name]. To help him CONCENTRATE."
hide fox02
show fox04 at left
fo "Subject 42 is all yours, Agent Dana. Over."
window hide
hide fox04 with moveoutleft
show dana09 at center with move
hide dana09
show dana08
with fastdissolve
da "Listen carefully [name]. You're in front of the Supreme White House and..."
mc "Am I? I can't see the entrance..."
hide dana08
show danayell
with fastdissolve
da "LISTEN! You have to IMAGINE what I'm telling you, GOT IT?"
mc "Ok, but it's really hard, especially with those tits hanging in my face."
da "Well, put some clothes back on me then!"
mc "Alright, alright, please stop yelling at me!"
hide danayell
show dana07a
with dissolve
da "Now, that's slightly better. I won't ask for more, because you are clearly mentally TOO WEAK."
hide dana07a
show dana12
with dissolve
da "So, imagine I am a Trumpf Militia Supreme White House guard, can you do that, or is it above your mental paygrade?"
mc "Gee lady, I'm not THAT stupid."
play sound "Sounds/dreaming.mp3"
hide dana12 with dissolve
show danaguard01 with dissolve
mc "There, you're a guard now. In a bikini of course."
da "*sigh* Why not actually, it might make the Real-Life Mental Test easier actually."
hide danaguard01
show danaguard02
with dissolve
da "Oooh, \"[name] the Grabber\"! Can I get an autograph please?"
mc "Err, sure baby."
hide danaguard02
show danaguard03
with dissolve
da "Thank you sssoo much, \"[name] the Grabber\"... Now I need to return the FAVOR."
play sound "Sounds/zipper.mp3"
mc "Errr, what... What are you doing?"
da "Returning the favor, \"[name] the Grabber\"! By sucking on your great big whopper! You don't mind, do you?"
scene fbi03 with dissolve
mc "N..No, of course not, I'm getting ROCKHARD for you, baby!"
scene fbibackground03
show danaguard04 
with dissolve
play sound "v08/wow.mp3"
da "Wow, \"[name] the Grabber\", your cock is HUGE! I just want to SUCK on it until you BLOW YOUR LOAD FOR ME!"
scene fbi04 with dissolve
mc "Oh fuck, this is amazing, I can mentally feel her lips on my dong, Agent Dana!"
scene fbibackground04 blurred
show danaguard05 
with dissolve
da "What about my tongue piercings? Does they feel good twirling all over your fist-sized helmet?"
hide danaguard05 
show danaguard06 
with fastdissolve
play sound "Sounds/lick.mp3"
mc "Oh God, oh God, this is incredible!"
hide danaguard06 
show danaguard05 
with fastdissolve
da "I should really let them SLIDE all over your sensitive glans..."
hide danaguard05 
show danaguard06 
with fastdissolve
play sound "Sounds/lick.mp3"
mc "Oh please, just... If you keep th.."
scene fbibackground03
show danaguard07
with dissolve
mc "I can't feel her mouth on my knobhead! Sssooo good!"
label DanaSuckSlowx:
scene fbibackground03 blurred
play channel1 "Sounds/hardsucking.mp3"
play channel2 "Sounds/boymoan02.mp3"
hide danablowfast
show danablowslow
call screen danablowslow01x
screen danablowslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DanaSuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DanaSuckFastx") 

label DanaSuckFastx:
mc "Aaah, those sucking lips, and that tongue piercing, OOOOH!"
hide danablowslow
show danablowfast
call screen danablowfast01x
screen danablowfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DanaSuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DanaSuckSlowx") 

label DanaSuckEndx:
mc "Oh fuck yeah, I'm gonna cum!"
stop channel1
stop channel2
hide danablowslow
hide danablowfast
show danapostblow01
with dissolve
da "No you're not, you're DEAD now!"
mc "Wh...What???"
da "Supreme White House guards have poisoned tongue piercings, so you just FAILED your infiltration!"
scene fbi05 with dissolve
mc "AAAH, I'm still GONNA CUM, GODAMMIT! Not gonna waste a hardon, RHAAA!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene fbibackground02
show danapostblow02 at centerright
with dissolve
da "Oh my God, you are sssooo totally not ready yet! Stop spewing your filthy virtual spunk all over me, Subject 42, you sexual pervert!"
window hide
show fox03 at farleft with moveinleft
fo "Should I virtually eliminate him, Agent Dana? By commiting suicide on him?"
da "Yes, Agent Fox, send him back up the Deep State rabbit-hole... This test was a TOTAL FAILURE... *sigh*"
hide fox03
show fox05 at left
with fastdissolve
play sound "Sounds/gun.mp3"
fo "You are TERMINATED!"
stop sound
scene fbi06 with dissolve
mc "You just shot me! I'm gonna d... Or just go back to the gallery."    
jump ExploreGalleryc

label ExploreGallery21:
$ kristatitssaidx = False
show container01
show krista01
play channel1 "v07/datemusic.mp3"
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
hide krista07
show kristapreballs01
with fastdissolve
kr "Look at that thing! So much bigger than Derek's..."
mc "You like it I can tell, hey?"
kr "Sure hun. Let me taste those fat bull-balls for starters..."
play channel2 "Sounds/lick.mp3"
scene containerkristatits
show kristaballs    
call screen kristaballsscreen01x
screen kristaballsscreen01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KristaBallsEndx")    
label KristaBallsEndx:    
mc "That's... enough, I need to fuck those big tits, Krista!"
hide kristaballs
stop channel2
play channel2 "Sounds/wank.mp3"
label KristaTitfuckSlowx:
hide kristatitsfast
hide kristatitspovslow
hide kristatitspovfast
scene containerkristatits blurred
show kristatitsslow
call screen kristatitsslow01x
screen kristatitsslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KristaTitfuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("KristaTitfuckFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("KristaTitfuckPOVSlowx") 

label KristaTitfuckPOVSlowx:
hide kristatitsslow
hide kristatitsfast
hide kristatitspovfast
scene containerkristatitspov blurred
show kristatitspovslow
call screen kristatitspovslow01x
screen kristatitspovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KristaTitfuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("KristaTitfuckPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("KristaTitfuckSlowx") 

label KristaTitfuckFastx:
if kristatitssaidx == False:
    kr "Hurry up hun, Derek will come back soon..."
    $ kristatitssaidx = True
hide kristatitsslow
hide kristatitspovslow
hide kristatitspovfast
scene containerkristatits blurred
show kristatitsfast
call screen kristatitsfast01x
screen kristatitsfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KristaTitfuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("KristaTitfuckSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("KristaTitfuckPOVFastx") 

label KristaTitfuckPOVFastx:
if kristatitssaidx == False:
    kr "Hurry up hun, Derek will come back soon..."
    $ kristatitssaidx = True
hide kristatitsslow
hide kristatitsfast
hide kristatitspovslow
scene containerkristatitspov blurred
show kristatitspovfast
call screen kristatitspovfast01x
screen kristatitspovfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KristaTitfuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("KristaTitfuckPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("KristaTitfuckFastx") 
            
label KristaTitfuckEndx:
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
mc "Fascinating. I'm going back to the gallery."
jump ExploreGalleryc

label ExploreGallery22:
scene quebec05
show paulettelumberjack00 
qu "I think we've worked enough for today, we've cleared a bit more of that forest."
mc "I notice indeed that a couple MORE trees are gone from the previous background pic."
qu "We were faster than last time. You have time to get cleaned up in the river with me before heading back to your country [name]? *wink*"
mc "Sure! I'm all dirty, I need a THOROUGH cleaning."
hide paulettelumberjack00 
show paulettelumberjack01 
with fastdissolve
qu "Then follow me to the river. And get your clothes off once we get there."
scene quebecriver02 with dissolve
play music "v081/river.mp3"
qu "You know, I saw you the other day."
scene quebecriver03 with dissolve
qu "...Spying on me while I was naked..."
mc "Err, I just stumbled upon you on my way back, it was not intentional and I didn't stay more than four pics, I swear!"
scene quebecriver04 with dissolve
qu "Well, maybe this time, you'll get a few more pics. I mean more \"peeks\"."
mc "(* Alright! *)"
scene quebecriver05 with dissolve
qu "Do you always get a blood rush down to your cock when you bathe with a MUSCLED lass?"
mc "Oh, shit, I didn't realize..."
scene quebecriver06 with dissolve
qu "...That you were sporting a great big hardon next to me?"
mc "Err..."
qu "Let'ts see if you other muscles are as BIG as this one... Let's compare biceps."
mc "Right... Okay..."
scene quebecriver07 with dissolve
mc "(* need... to... flex... MIGHTILY! *)"
play sound "Sounds/mcworkout.mp3"
scene quebecriver08 with dissolve
qu "You can try as hard as you want, BOY, I'm BIGGER than you..."
mc "I... realize that."
qu "For being such a puny American boy, KISS MY BICEPS."
mc "Wh... What?"
qu "I said KISS IT!"
scene quebecriver09 with dissolve
play sound "Sounds/kiss.mp3"
qu "That's right, kiss those superior muscular BOULDERS and worship them!"
play sound "Sounds/kiss.mp3"
qu "Your cock is getting even harder, isn't it [name]?"
scene quebecriver10 with dissolve
qu "I think you need to UNLOAD then, don't you? I'll make sure you spill your seed on sacred Canadian soil!"
mc "Oh fuck! Your grip is so TIGHT on my shaft!"
qu "I'll show you what a REAL handjob feels like!"
play channel1 "Sounds/wank.mp3"
play channel2 "Sounds/panting.mp3"
label PauletteWankSlowx:
hide paulettewankfast
show paulettewankslow
call screen paulettewankslow01x
screen paulettewankslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PauletteWankEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PauletteWankFastx") 

label PauletteWankFastx:
qu "You like that, dirty boy, don't you? I'll make you EXPLODE in no time, you'll see..."
hide paulettewankslow
show paulettewankfast
call screen paulettewankfast01x
screen paulettewankfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PauletteWankEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PauletteWankSlowx") 

label PauletteWankEndx:
stop channel1
stop channel2
hide paulettewankslow
hide paulettewankfast
show paulettewankcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH!"
with fastflash
qu "That's it, get it all out [name]!"
scene paulettewankcum02 with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
qu "Nice! You really needed to unload those balls, didn't you, DIRTY BOY?"
with fastflash
mc "You... AAAHH? made me COME like that!"
scene paulettewankcum03 with fastdissolve
qu "Still MORE? That's a load for the record..."
with fastflash
mc "I'm... done, you've drained me..."
play sound "Sounds/panting.mp3"
qu "You made a right mess and you're all dirty again. What aboot I lick some cum off your chest and help you clean up?"
scene paulettewankcum04 with fastdissolve
play sound "Sounds/lick.mp3"
mc "Oh Paulette, this is so fucking hot..."
qu "Mmh... *slurp*.... Do you know what a French-Canadian kiss is?"
mc "Err... A French kiss that tastes of maple syrup?"
qu "No silly boy..."
scene paulettewankcum05 with fastdissolve
qu "THIS is a French-Canadian kiss!"
play sound "Sounds/kiss.mp3"
mc "Ah, so a French kiss that tastes of cum then."
scene quebecriver11 with fastdissolve
qu "Now go back to your country [name] or you'll be late. For whatever it is you Americans do in the evenings."
mc "And what will YOU do Paulette? *wink*"
qu "I've got some Netflix DVDs."
jump ExploreGalleryc

label ExploreGallery23:
scene quebec06
show paulettelumberjack00 
qu "Since you're super-strong now, we can have super-dirty sex. No need to clean ourselves, I want it RAW!"
mc "Alright, I'm in Paulette!"
hide paulettelumberjack00 
show paulettelumberjack01 
with fastdissolve
qu "Let's do it over there. Get your kit off and your cock HARD! I need some SEXERCISE!"
scene quebec08
show paulettepresex01
with dissolve
qu "Here is good. Under the arch."
scene quebec08 blurred
show paulettepresex02
with dissolve
qu "Are you naked yet? Get down on your knees. I'm going to do front squats ON YOUR COCK."
mc "Err, that sounds dangerous. A bit?"
scene paulettesexbackground
show paulettepresex03
with dissolve
qu "Stop being such a puss. Just hold your cock steady and make sure it goes in the RIGHT hole when I squat down. Ready?"
mc "I... I guess so."
hide paulettepresex03
play channel1 "Sounds/womangroan.mp3"
play channel2 "Sounds/wank.mp3"
label PauletteSexSlowx:
hide paulettesexfast
show paulettesexslow
call screen paulettesexslow01x
screen paulettesexslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PauletteSexEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("PauletteSexFastx") 

label PauletteSexFastx:
qu "That's a good SEXERCISE! Let's do it FASTER now, I hope your big cock is ready for it!"
hide paulettesexslow
show paulettesexfast
call screen paulettesexfast01x
screen paulettesexfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PauletteSexEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("PauletteSexSlowx") 

label PauletteSexEndx:
qu "Yeah, I can feel my quads really straining... As well as my pussy."
mc "Can we... take a break... PLEASE!"
qu "Alright, puny boy."
stop channel1
stop channel2
hide paulettesexslow
hide paulettesexfast
show paulettepresex03
with dissolve
play sound "Sounds/panting.mp3"
qu "Is your cock still intact?"
mc "AAAH... barely..."
qu "But it still is, right? What aboot we do some more POWERFUCKING then?"
mc "You want some powerfucking? I'll POWERFUCK YOU alright, Paulette! Get on your back and you'll see!"
qu "Oooh, I like boys with CONFIDENCE! I usually scare them away, but you seem up for the task!"
scene paulettefuckbackground
show pauletteprefuck
with dissolve
mc "I've got the tip in... Feels so tight already!"
qu "I'm totally WET I am for your magnificent MONSTERCOCK so just SHOVE IT IN!"                                                                  
scene paulettefuckbackground blurred
play channel1 "Sounds/debrasex.mp3"
play channel2 "Sounds/wank.mp3"
label PauletteFuckSlowx:
hide paulettefuckfast
show paulettefuckslow
mc "Nice and slow at first, so you can get used to my size..."
qu "Mon Dieu! Even Canadian lumberjacks don't have LOGS THAT SIZE!"
call screen paulettefuckslow01x
screen paulettefuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PauletteFuckFastx")

label PauletteFuckFastx:
mc "And now, FASTER, so I can really plunge my tool DEEP inside you!"
hide paulettefuckslow
show paulettefuckfast
qu "AAAh, you're really STRETCHING me, STUD!"
call screen paulettefuckfast01x
screen paulettefuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PauletteFuckEndx")

label PauletteFuckEndx:
mc "I'm gonna shoot my load inside you NOW!"
stop channel1
stop channel2
hide paulettefuckslow
hide paulettefuckfast
show paulettefuckcum
play channel1 "Sounds/splooge02.mp3"
play channel2 "v07/creampie.mp3"
call screen paulettefuckcum01x
screen paulettefuckcum01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("PauletteFuckEndCumx")

label PauletteFuckEndCumx:
qu "Dump the rest on me please!"
stop channel1
stop channel2
hide paulettefuckcum
show paulettefuckcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "ALRIGHT, HERE IT COMES, AAAH!"
window hide
with fastflash
qu "Becoming super-strong really made you HORNY, didn't it, [name]?"
window hide
with fastflash
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "FUCK YEAH!"
window hide
with fastflash
qu "It never ends, you're STILL ERUPTING!"
scene paulettefuckbackground
show paulettefuckcum02
with dissolve
play sound "Sounds/panting.mp3"
qu "I'm TOTALLY covered in your dirty American boycum... What a MESS you made..."
scene quebec08 blurred
show paulettepostsex
with dissolve
qu "I'm finally gonna need to go and clean myself in the river... You covered me with TOO MUCH HOT SPUNK!"
mc "Ah, well, I can't join you Paulette, it's getting late and I need to get back to my compound."
qu "That's too bad for you... Being forced to leave sacred Canadian soil."    
jump ExploreGalleryc

label ExploreGallery24:
stop music
scene devcave01
mc "I'm BACK ladies!"
scene devcave02 with dissolve
ln "About bloody time! Get us out of here and FUCK US REAL GOOD!"
scene devcave04 with dissolve
mc "Sure, where's the latch?"
scene devcave08 with dissolve
aw "We don't know... Our devs never tell us anything about who we are and why we're here..."
scene devcave05 with dissolve
ln "The why is easy Sophia! They are MILKING us. And their patrons! Just look around for some switch, [name]... And hurry up, I need a good FUCK!!!"
scene devcave11 with dissolve
play sound "v08/doorwoosh.mp3"
aw "That did the trick! I can finally breathe fresh air."
ln "Well done, REAL HERO!"
scene devcave12 with dissolve
ln "Look Sophia, this place is even stranger than I anticipated... What twisted devs we have."
aw "It feels so weird being in 1920*1080 resolution... I'm normally only rendered at 1280*720 pixels..."
ln "At least there's a nice big cushion right in the middle of the cave."
scene devcave13 with dissolve
aw "What are you thinking about Linda?"
ln "That it's the perfect spot for a HOT ROMP with our hero STUD! So let's show him what we've got in store for his massive dong!"
play music "v07/datemusic.mp3"
scene devcave14 with dissolve
ln "That's it Sophia, show him that fine ass... That should get him HARD and READY for us in no time!"
aw "I'm used to exposing myself like that to boys for some strange reason..."
ln "I want to rub my pussy against yours Sophia... Let's get on the love pillow..."
scene devcave15 with dissolve
play sound "Sounds/moaning03.ogg"
aw "OOOH, I haven't felt this naughty in such a long time!"
scene devcave16 with dissolve
ln "You like our boots I see?"
mc "Yes... And your tits too."
ln "Then lie on the ground by the pillow, we'll use them to jack your crank into a mighty orgasm!"
scene devcaveprefoot01 with dissolve
ln "There, are you feeling comfortable?"
aw "This is so dirty, our boots rubbing against his fat shaft... Mmmh..."
mc "Y...Yes, I think I'm ready..."
ln "I can see that, you're already LEAKING... Let's get to work Sophia, shall we?"
play music "Sounds/wank.mp3"
label DevCaveAnimSexSlowx:
scene devcaveanimslow with fastdissolve
call screen devcaveanimsexslow01x
screen devcaveanimsexslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DevCaveAnimSexEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DevCaveAnimSexFastx") 

label DevCaveAnimSexFastx:
ln "I think we need to increase the tempo. To get him to SPEW HIS SAUCE!"
scene devcaveanimfast with fastdissolve
call screen devcaveanimsexfast01x
screen devcaveanimsexfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DevCaveAnimSexEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DevCaveAnimSexSlowx") 

label DevCaveAnimSexEndx:
stop music
scene devcavecum01 with dissolve                                         
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH!"
ln "That's it, we made you cum with our boots!"
window hide
with fastflash
aw "There's sooo much of it, I've never seen a load THAT big!"
scene devcavecum02 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
ln "I told you, [name] is the biggest STUD on f95zone..."
window hide
with fastflash
aw "If only he was a love interest in \"A Wife And Mother\"... Instead of the beta-boys I have to contend with..."
scene devcavecum03 with dissolve
play sound "Sounds/panting.mp3"
ln "Was that good [name]? Did it relieve your big fat straining balls?"
mc "Phew, yeah, it did the trick, they feel lighter now..."
ln "And I'm feeling SUPER-HORNY. And I want that hard cock UP MY ASS! I expect a STUD like you to keep it UP and ROCKHARD!"
scene devcavecum04 with dissolve
aw "Are you sure Linda? It looks awfully HUGE for that hole!"
ln "Don't worry about me, I've been practising this for so long, I could stick a telephone pole up there!"
scene devcave17 with dissolve
play music "v07/datemusic.mp3"
ln "Let me first get you into the mood [name]..."
scene devcave18 with dissolve
ln "Mmh, there you go, I can see you are already back to FULL HARDNESS for me... You really can't wait to pound that ass, hey?"
scene devcave19 with dissolve
mc "Shit, it looks so fucking amazing, I want IN, right NOW! Come over here and bend over!"
aw "Sssoo manly... Not like my pindick husband..."
scene devcavepreass03 with dissolve
aw "I can't believe you're going to stick this monster pud inside that tiny hole... You're going to DESTROY it with that massive weapon of yours!"
scene devcavepreass02 with dissolve
ln "It is indeed a weapon of ASS DESTRUCTION! Spread my asscheeks for him will you Sophia?"
mc "And watch carefully Sophia.... Cos this is what will happen to your pussy NEXT!"
scene devcavepreass04 with dissolve
mc "Are you ready to have your ass DESTROYED?"
ln "YES! Pound it HARD, and show me what I've been missing for over two years!"
label DevCaveFuckSexSlowx:
$ devcaveoralx = False
play music "Sounds/fucksound.mp3"
scene devcavefuckslow with fastdissolve
call screen devcavefucksexslow01x
screen devcavefucksexslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DevCaveFuckSexFastx") 
    imagebutton:
        focus_mask True
        idle "v082/mouth.png"
        hover "v082/mouth.png"
        action Jump ("DevCaveMouthSlowx") 

label DevCaveFuckSexFastx:
if devcaveoralx == False:
    ln "Go on, POUND ME HARDER!"
$ devcaveoralx = False
play music "Sounds/fucksound.mp3"
scene devcavefuckfast with fastdissolve
call screen devcavefucksexfast01x
screen devcavefucksexfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DevCaveFuckSexEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DevCaveFuckSexSlowx") 
    imagebutton:
        focus_mask True
        idle "v082/mouth.png"
        hover "v082/mouth.png"
        action Jump ("DevCaveMouthFastx") 

label DevCaveMouthSlowx:
if devcaveoralx == False:
    mc "Let's switch holes... Sophia's MOUTH!"
$ devcaveoralx = True
play music "Sounds/hardsucking.mp3"
scene devcavemouthslow with fastdissolve
call screen devcavemouthslow01x
screen devcavemouthslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DevCaveMouthFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("DevCaveFuckSexSlowx") 

label DevCaveMouthFastx:
if devcaveoralx == False:
    mc "Let's switch holes... Sophia's MOUTH!"
$ devcaveoralx = True
play music "Sounds/hardsucking.mp3"
scene devcavemouthfast with fastdissolve
call screen devcavemouthfast01x
screen devcavemouthfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DevCaveMouthSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/analidle.png"
        hover "Icons/analidle.png"
        action Jump ("DevCaveFuckSexFastx") 

label DevCaveFuckSexEndx:
stop music
scene devcavefuckcum01 with dissolve                                         
play music "v07/creampie.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "Dumping my load, AAAHH!"
window hide
with fastflash
mc "Open your mouth real WIDE Sophia!"
aw "What? W...Why???"
scene devcavefuckcum02 with dissolve   
stop music
play music "Sounds/hardsucking.mp3"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "That's why!"
window hide
with fastflash
aw "* Glllurb...* "
scene devcavefuckcum03 with dissolve   
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "And now directly down your gullet! AAAH!"
window hide
with fastflash
ln "Yes, fill up her stomach with your sauce [name]!"
scene devcavefuckcum04 with dissolve   
stop music
stop sound
play sound "Sounds/slurp.mp3"
mc "Yeah, swap mouthfulls of my cum ladies.... That's so nasty..."
ln "Mmmh, it's so tasty, give me more Sophia..."
scene devcavefuckcum05 with dissolve   
mc "There, here are a few more afterdregs for you..."
aw "Wow, there MORE cum left in your spermtube than my poor hubby can produce in a MONTH!"
scene devcavefuckcum06 with dissolve  
play sound "Sounds/thud.mp3"
mc "And guess what? I'm still ROCKHARD!"
ln "I think it's your turn to get your pussy DESTROYED, Sophia..."
scene devsophiaprefuck01 with dissolve
ln "And you can lick my cummy butthole while [name] rams his cunt-destroyer inside your tender snatch!"
scene devsophiaprefuck02 with dissolve
play sound "Sounds/lick.mp3"
ln "Mmmh, that's nice, Sophia, keep going... And you stud, FUCK HER!"
play music "Sounds/womansex02.mp3"
label DevCaveSophiaSexSlowx:
scene devcavesophiafuckslow with fastdissolve
call screen devcavesophiafucksexslow01x
screen devcavesophiafucksexslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DevCaveSophiaSexEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("DevCaveSophiaSexFastx") 

label DevCaveSophiaSexFastx:
aw "AAAH, UUUH, Genesis 8 boys are so much better than Genesis 3 ones!"
mc "That's correct, we're BIGGER and STRONGER. Let me demonstrate by pummeling your fuckhole even FASTER!"
scene devcavesophiafuckfast with fastdissolve
call screen devcavesophiafucksexfast01x
screen devcavesophiafucksexfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("DevCaveSophiaSexEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("DevCaveSophiaSexSlowx") 

label DevCaveSophiaSexEndx:
mc "That pussy is gonna MILK the cum out of me VERY SOON!"
aw "I have a lot of experience with MILKING. Milking patrons essentially."
stop music
play music "Sounds/splooge02.mp3"
scene devsophiacum01 with dissolve                                         
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "That's it, I'm blowing ANOTHER LOAD!"
window hide
with fastflash
aw "It's so DEEP and WARM inside me! My hubby never FILLED ME UP LIKE THAT!"
scene devsophiacum02 with dissolve                                         
stop music
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "And there's more for you pretty ladies, RHAAA!"
window hide
with fastflash
ln "God, even though this is your THIRD load in a row, it's still more CREAM than my so.. landboy can muster in a FULL GAME. Whenever that will be complete."
scene devsophiacum03 with dissolve                                         
play sound "Sounds/panting.mp3"
mc "Phew, well that was worth waiting two months for, wasn't it ladies?"
scene devcaveend01 with dissolve
ln "Yes, you fucked us real good. But now I somehow feel compelled to go back into my cage."
aw "I have the same strange feeling... Like I am drawn to it."
scene devcaveend02 with dissolve
mc "Come on ladies, you're being mind-controlled by your devs! You're FREE to go now!"
scene devcaveend03 with dissolve
ln "No, I think it's best if we go back... What would we do in the REAL world outside?"
aw "I don't have a home in this world. I NEED to go back to my virtual mansion, my pindick hubby and take care of my children. By regularly exposing myself to them."
scene devcaveend02 with dissolve
mc "So I did all this for NOTHING?"
scene devcaveend04 with dissolve
ln "I found some money in my panty. 10 bucks. With someone's goofy face on it that I don't recognize."
mc "Let me see. Ah, it's President-for-Life Donald Trumpf. It's REAL money then."
scene devcaveend05 with dissolve
aw "What? That doofus is president in the REAL world? Oh my God, please take the banknote I ALSO found in my panty and let's go back to our virtual slavery."
scene devcaveend06 with dissolve
ln "For sure, I would rather wait idly for another 2 years to maybe resurface than live in a world where Donald Trumpf is president!"
mc "That's actually a decent argument I guess. Alright, I'll put you back into your cages then..."
scene devcaveend07 with dissolve
aw "Thank you so much for your kindness. HORSE-HUNG HERO."
ln "Like they should be in every game really."
scene devcave01 with dissolve
ln "ICSTOR, I'm back! When are you going to use me instead of that little freckled redhead trollop?"
aw "It's me L\&P! I'm ready for some REAL virtual sex now! Pretty please..."
mc "I guess I should leave, they're hopeless cases..."
jump ExploreGalleryc

label ExploreGallery25:
scene maragogofar02 with dissolve
mc "Up the ledge and  behind the bushes by the pool where I shall first observe what she's up to..."
scene maragogofar03 with dissolve
mc "Who's that? She's talking to some big-titted chick in a uniform and a strange hat."
mc "Let's squint my eyes so I can zoom in and listen onto what they say..."
scene maragogo02 blurred
show melaniatitiana01
with dissolve
me "There you are Agent Titiana, everything is on the microfilm."
mc "What's all this about? I should go and confront them."
scene maragogo02
show melaniaout03 at left
show titiana01b at centerright
with dissolve
me "What are YOU doing here?"
tn "Who is this boy, comrade?"
hide melaniaout03
show melaniaout02 at left
with fastdissolve
me "A pain in the ass, that's who..."
mc "What the hell? She's a Russian spy! You're not a double-agent Melania, you're a TRIPLE-agent!"
hide titiana01b
show titiana02b at centerright
with fastdissolve
tn "Fear not Comrade Melania, I shall protect you with my bosom! For the glory of Mother Russia!"
me "I'm not scared of him, he probably just came over to try and fuck me."
mc "Hey, how did you guess?"
hide titiana02b
show titiana03b at centerright
with fastdissolve
tn "Then let me deal with this Western spy. The Russian way."
play music "v082/russia.mp3"
scene maragogo08 blurred
show titiana04
with dissolve
tn "So, you want SEX, American boy?"
mc "Err... Yeah, but with Melania cos I can blackmail her now, so step aside lady and let m..."
window hide
hide titiana04
show titiana05
with fastdissolve
tn "Not before I show you this!"
hide titiana05
show titiana06
with dissolve
$ renpy.pause(0.5, hard='True')
hide titiana06
show titiana05
with dissolve
hide titiana05
show titiana07
with dissolve
$ renpy.pause(0.5, hard='True')
hide titiana07
show titiana05
with dissolve
hide titiana05
show titiana06
with dissolve
$ renpy.pause(0.5, hard='True')
hide titiana06
show titiana05
with dissolve
hide titiana05
show titiana07
with dissolve
$ renpy.pause(0.5, hard='True')
hide titiana07
show titiana05
with dissolve
hide titiana05
show titiana06
with dissolve
$ renpy.pause(0.5, hard='True')
hide titiana06
show titiana05
with dissolve
hide titiana05
show titiana07
with dissolve
$ renpy.pause(0.5, hard='True')
hide titiana07
show titiana05
with dissolve
hide titiana05
show titiana06
with dissolve
$ renpy.pause(0.5, hard='True')
hide titiana06
show titiana05
with dissolve
hide titiana05
show titiana07
with dissolve
$ renpy.pause(0.5, hard='True')
hide titiana07
show titiana05
with dissolve
hide titiana05
show titiana06
with dissolve
mc "What... What is she doing flicking her hair like that in front of me? This is somewhat... mesmerizing...."
hide titiana06
show titiana05
with dissolve
tn "And now, let me get undressed for you, American Boy..."
scene maragogo02
show titiana10
with dissolve
mc "Fuck me, those melons are worthy of Mother Russia AND Mother America!"
hide titiana10
show titiana11
with fastdissolve
tn "Now it's your turn to get naked... and ROCKHARD for me!"
stop music
scene titianapretitfuck01 with dissolve
tn "I see you have wasted no time, American Boy."
mc "The sooner I'm done fucking you till you submit, the sooner I can move on to Melania..."
scene titianapretitfuck02 with dissolve
tn "Oh, but we have TIME, don't we? Your MONSTER American boycock needs some tender tit-loving first..."
mc "I suppose I could indulge in some titfucking first... To get me in the mood..."
tn "Oh, it'll get you in the mood, don't worry about THAT!"
play channel1 "Sounds/wank.mp3"
play channel2 "Sounds/moaning03.ogg"
label TitianaTitsSlowx:
show titianatitsslow
call screen titianatitfuckslow01x
screen titianatitfuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TitianaTitsEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TitianaTitsFastx") 

label TitianaTitsFastx:
tn "You seem to enjoy my warm Russian bosom, don't you?"
mc "Oh... Fuck... I... can... resist. You're not going to get to me!... Aaaah..."
tn "You think so? I think it's time to make you EXPLODE your filthy capitalist cum all over the place!"
show titianatitsfast
call screen titianatitfuckfast01x
screen titianatitfuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TitianaTitsEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("TitianaTitsSlowx") 

label TitianaTitsEndx:
tn "Come on American boy, show me how much SPUNK you hold, RELEASE IT ALL!"    
stop channel1
stop channel2
scene titianatitscum01 with dissolve    
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "FUCK, I'm blowing my load, AAAH!"
window hide
with fastflash
tn "YES! EMPTY THOSE BALLS FOR ME!"
scene titianatitscum02 with dissolve    
mc "Those tits... I can't hold back, RHAAA!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
window hide
with fastflash
tn "That's right, Russian breasts can milk any American boycock DRY!"
scene titianatitscum03 with dissolve  
play sound "Sounds/gasp.mp3"
tn "Well, what a mess you made. Now you're empty and I have you at MY MERCY! *slurp*"
mc "Is that what you think?"
scene titianatitscum04 with dissolve  
mc "I'll show you that my American cock is not about to be overcome by enemy trickery!"
tn "What??? You're not empty yet?"
mc "That's right, and I'm gonna to turn you from a commie spy into a cummy mess!"
scene maragogo05 blurred
show titianaprefuck01
with dissolve
mc "You think you can manage this super-sized American boycock, hey, Titiana?"
tn "I can take it, I have been trained in extreme sexual resistance at the school of famous sexologist Professor Jakkov, just shove it in already!"
scene maragogo04b blurred
show titianaprefuck02
with dissolve
mc "I don't know... Your pussy looks awfully tiny compared to it. Can you feel its massive girth rubbing on your clit?"
play sound "Sounds/moaning.mp3"
tn "I... I can feel it, yes... My pussy will withstand your pound..."
hide titianaprefuck02
show titianaprefuck03
with dissolve
play sound "Sounds/womanscream.ogg"
tn "AAAH! I... must... endure it... For the glory of Mother Russia, I will take it for Team Red!"
mc "We'll see about that!"
play music "Sounds/fucksound.mp3"
scene maragogo04 blurred
label TitianaSexSlowx:
hide titianafuckfast
show titianafuckslow
call screen titianafuckslow01x
screen titianafuckslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TitianaSexEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("TitianaSexFastx") 

label TitianaSexFastx:
tn "Come on American boy, show me what you got! Pound that Russian pussy HARDER!"
mc "You asked for it!"
hide titianafuckslow
show titianafuckfast
call screen titianafuckfast01x
screen titianafuckfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("TitianaSexEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("TitianaSexSlowx") 

label TitianaSexEndx:
tn "Please stop pummelling my pussy, I relent! Your Western Capitalist cock is far superior to the Russian Communist ones!"
mc "Beg for my cum then, Titiana!"
tn "Please American boy, fill me up with your superior seed, I BEG YOU!"
scene maragogo04b blurred
show titianafuckcum01
with dissolve
play music "v07/creampie.mp3"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH, there you go, directly into your Russian spy snatch!"
window hide
with fastflash
tn "Pull out, your plumes are just TOO POWERFUL!"
play music "sounds/splooge02.mp3"
scene maragogo10 blurred
show titianafuckcum02
with dissolve
mc "No fucking way, you thought I was empty, I'll prove you wrong, RHAAA, take that!"
window hide
with fastflash
tn "T...Too MUCH, AAAH!"
scene maragogo04b blurred
show titianafuckcum03
with dissolve
mc "Fuck ME, it's POURING out of your pussy! RHAAA!"
window hide
with fastflash
tn "That's because you pumped a GALLON of spunk inside it!"
hide titianafuckcum03
show titianafuckcum04
with dissolve
mc "Now that I have disposed of you, I will fuck Melania into submission! Where is she actually? I thought she was watching us."
tn "HA HA, American boy, I have succeeded! My Russian charms have given Comrade Melania enough time to escape out of your clutches and into the safety of the Supreme White House!"
mc "Damn it, I've been had! Now get dressed before I decide to fuck you to death, you wicked Russian agent!"
stop music
jump ExploreGalleryc

label ExploreGallery26:
stop music
scene fbi01
fo "Subject 42. SUBJECT 42! WAKE UP! Activate Google mental goggles, Siri."
scene fbi02 with dissolve
mc "Uh? My cock, is it still intact?"
play sound "Sounds/interfacestart.mp3"
scene fbibackground02
show dana07a
with dissolve
da "Your cock is doing just fine [name]. For the time being..."
mc "Phew, that's a relief. Now get me out of here, or I'll..."
hide dana07a
show dana20
with fastdissolve
da "NOT until you PASS the test."
hide dana20
show dana22
with fastdissolve
da "You know the drill, but this time, CONCENTRATE and FOCUS YOUR STRENGTH DOWN TO YOUR DICK!"
window hide
hide dana22 with moveoutright
show kimfbi01 with moveinleft
mc "Hey, please don't leave me alone with h..."
play sound "Sounds/hulkgrowl01.mp3"
kg "YOU ARE AN ENEMY OF THE PEOPLE, PREPARE TO DIE BY PUSSY SMOTHERING!"
mc "AAAAH, HELP!"
window hide
hide kimfbi01
show kimfbi04 
with fastdissolve
kg "I'm getting ANGRY!"
play sound "Sounds/ripping.mp3"
hide kimfbi04
show kimfbi05 
with dissolve
kg "AND ANGRIER!"
hide kimfbi05
show kimfbi07
with dissolve
kg "AND ANGRIEST!"
mc "* Oh shit, oh shit, concentrate [name], concentrate! The life of your prized horsecock depends on it! *"
scene fbibackground02 blurred
show kimfbi08
with dissolve
play sound "Sounds/hulkgrowl01.mp3"
kg "NOW FUCK ME!"
play channel1 "Sounds/debrasex.mp3"
hide kimfbi08
show kimfbianim
with fastdissolve
call screen kimfbianim03x
screen kimfbianim03x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KimberlyFBIEnd03x")

label KimberlyFBIEnd03x:
play channel2 "v08/humming.mp3"
scene fbi10 with dissolve
mc "AAAH! My cock! Must... FIGHT... the... PAIN!"
stop channel2
scene fbibackground02 blurred
show kimfbianim
with dissolve
call screen kimfbianim04x
screen kimfbianim04x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KimberlyFBIEnd04x")

label KimberlyFBIEnd04x:
play channel2 "v08/humming.mp3"
scene fbi11 with dissolve
mc "NEED... TO... CUM..."
da "FOCUS! BELIEVE your cock is STRONGER than her PUSSY!"
scene fbi12 with dissolve
mc "YES! AAAAH!"
window hide
with fastflash
da "Well done [name]! Keep going!"
scene fbi13 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "FUCK YEAH, MASSIVE CUMLOAD, RHAAA!"
scene fbibackground02 blurred
stop channel2
show kimfbi09
with dissolve
play channel2 "Sounds/splooge02.mp3"
kg "WHAT IS HAPPENING? MY PUSSY IS THE STRONGEST PUSSY IN THE WORLD!!!"
window hide
with fastflash
mc "My cock is STRONGER, RHAAA!"
stop channel2
stop channel1
play channel2 "v08/humming.mp3"
scene fbi14 with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"    
mc "NOW I AM BECOME SEX, THE DESTROYER OF CUNTS!!!"
window hide
with fastflash
da "Amazing, you succeeded! Project Man-at-Twat accomplished!"
stop channel2
scene fbi15 with fade
play sound "Sounds/panting.mp3"
mc "Eeeh... Uuuuh..." 
da "Agent Fox, go and get the mop..."
jump ExploreGalleryc

label ExploreGallery27:
$ kristafucksaidx = False
show container01
show krista01
play channel1 "v07/datemusic.mp3"
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
kr "Mmmh, I love your fat donkey dong. Let me taste those fat bull-balls for starters..."
play channel2 "Sounds/lick.mp3"
scene containerkristatits
show kristaballs    
call screen kristaballsscreen01bx
screen kristaballsscreen01bx:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KristaBallsEndbx")    
label KristaBallsEndbx:    
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
play channel2 "Sounds/barbarasex.mp3"
label KristafuckSlowx:
scene container02 blurred
show kristasexslow
call screen kristaslow01x
screen kristaslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KristafuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("KristafuckFastx") 
    imagebutton:
        focus_mask True
        idle "v07/frontidle.png"
        hover "v07/frontidle.png"
        action Jump ("KristafuckPOVSlowx") 

label KristafuckPOVSlowx:
scene containerkristafront blurred
show kristafrontslow
call screen kristafrontslow01x
screen kristafrontslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KristafuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("KristafuckPOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("KristafuckSlowx") 

label KristafuckFastx:
if kristafucksaidx == False:
    kr "Hurry up hun, Derek will come back soon..."
    $ kristafucksaidx = True
scene container02 blurred
show kristasexfast
call screen kristafast01x
screen kristafast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KristafuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("KristafuckSlowx") 
    imagebutton:
        focus_mask True
        idle "v07/frontidle.png"
        hover "v07/frontidle.png"
        action Jump ("KristafuckPOVFastx") 

label KristafuckPOVFastx:
if kristafucksaidx == False:
    kr "Hurry up hun, Derek will come back soon..."
    $ kristafucksaidx = True
scene containerkristafront blurred
show kristafrontfast
call screen kristafrontfast01x
screen kristafrontfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("KristafuckEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/sloweridle.png"
        action Jump ("KristafuckPOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("KristafuckFastx") 
                
label KristafuckEndx:
kr "Now you dump a nice big fat load inside my pussy hun. Let's see what you got."
mc "Fuck yeah, I'm getting there, I will, I'm gonna..."
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
jump ExploreGalleryc