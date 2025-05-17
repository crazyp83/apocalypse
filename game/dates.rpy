label AmyDate:
play music "v07/datemusic.mp3"
scene canyon01
show amydate01
with fade
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
call LustPlusAmy
scene amycanyon08 with dissolve
am "Let's keep this date... romantic. And not indulge your growing boyhood... Even if it is HUGE and demanding...."
mc "OK, I don't want to rush you in any way. I mean, there's the stairway to heavens to climb, right?"
am "That's right, and I AM your heaven! So let's go back to the compound, I need to finish fitting some exhaust pipe on a rig. See you later [name]!"
mc "(That went fast from romantic to not-romantic-at-all...)"
$ period += 1
$ amydateon = False
$ amydatedone = True
stop music
jump Bedroom

label AngieDate:
play music "v07/datemusic.mp3"
scene canyon01
show angiedate01
with fade
an "Wow, this place is absolutely BEAUTIFUL! Thank you so much for taking me here [name]!"
mc "My pleasure, I knew you would like to get outdoors and...err... get in your bikini."
hide angiedate01
show angiedate02
with fastdissolve
an "It's the only one I've got... It's a bit too small since I grew a bit..."
mc "Don't worry about it, it fits you perfectly."
hide angiedate02
show angiedate04
with fastdissolve
an "Really, you mean it? You're such an ACE friend to have!"
an "Come and play with me in the water..."
mc "Sure, I'll get my swimming trunks..."
scene canyon02
show angiedate05
an "The water is so great! I hope it's not radioactive though..."
mc "Not much. 3.6 Roentgen to be precise."
hide angiedate05
show angiedate06
with fastdissolve
an "I don't know what that means... Why don't you carry me on your SUPER-STRONG back and we can fight imaginary foes!"
mc "Sure, why not..."
hide angiedate06
show angiedate05
with fastdissolve
an "Let's FIGHT against the bad people who are the ENEMY of the people!"
mc "Right, right. So we'll fight imaginary newspapers then. Like the New New York Tribune."
hide angiedate05
show angiedate06
with fastdissolve
an "Uuh?"
mc "Never mind."
hide angiedate06
show angiedate07
with dissolve
an "YIPPEE! We have VANQUISHED our enemies! They all lie dead in the water!"
mc "RIP Free press."
scene canyon01 
show angiedate01
with fade
an "Thank you so much for this FUN day out [name]!"
call LustPlusAngie
mc "We should probably head back to the compound, it's getting late..."
$ angiedatedone = True
$ angiedateon = False
$ period += 1
stop music
jump Bedroom

label MichikoDate:
play music "Sounds/michiko.mp3"
scene michikoroom01
show michikoroom01b
with fade
mi "I'm so glad you came... for our date."
hide michikoroom01b
show michikoroom01a
with fastdissolve
mi "I have prepared some traditional herbal tea. I hope you like it!"
mc "(I hope there is more to it than just driniking tea...)"
scene michikoroom02
show michikoroom02a
show michikoroomtable
with dissolve
mi "I'm so sorry I beat the crap out of you the other day. It was to train you to become a better fighter for our cause!"
menu:
    "I understand, don't worry.":
        hide michikoroom02a
        hide michikoroomtable
        show michikoroom02b
        show michikoroomtableb        
        mi "I'm glad you didn't take it too badly. Here, have some tea, it will give you inner strength."
        hide michikoroom02b
        hide michikoroomtableb        
        show michikoroom02a
        show michikoroomtable        
        jump MichikoDate02
    "It was just some minor scratches. Nothing really.":
        hide michikoroom02a
        hide michikoroomtable
        show michikoroom02c
        show michikoroomtable        
        mi "Just some scratches? I left you bloodied and with a black eye..."
        $ michikodate -= 1
        hide michikoroom02c
        hide michikoroomtable
        show michikoroom02b
        show michikoroomtableb        
        mi sidemi "Here, have some tea, it will give you inner strength."
        hide michikoroom02b
        hide michikoroomtable
        show michikoroom02a
        show michikoroomtable        
        jump MichikoDate02
    "It hurt like hell. You should go easy on me, I'm a noob at fighting.":
        hide michikoroom02a
        hide michikoroomtable
        show michikoroom02b
        show michikoroomtableb 
        $ michikodate += 1
        mi sidemi "Ooh, I'm so sorry, my poor boy... Here, have some tea, it will give you inner strength. The outer strength, you already have (wink)."
        hide michikoroom02b
        hide michikoroomtable
        show michikoroom02a
        show michikoroomtable        
        jump MichikoDate02

label MichikoDate02:

mi sidemi "Do you like my outfit? I wear it only on special occasions..."
menu:
    "You look beautiful in it Michiko.":
        hide michikoroom02a
        hide michikoroomtable
        show michikoroom02d
        show michikoroomtableb                
        mi "My mother made it for me. Before she died... It's one of the few family belongings I have left..."
        mc "Then you should treasure it. Remembering our fallen families is important."
        hide michikoroom02d
        hide michikoroomtable
        show michikoroom02b
        show michikoroomtableb                
        mi "Yes it is. Here have some more tea."
        if michikodate >= 1:
            mi "I would like you to help me choose an outfit for my stripping gig, since you have been such a gentleman..." 
            mc "Alright!"
            mi "Don't move, I'll come back wearing something even SEXIER..."
            jump MichikoDateLast
        if michikodate == 0:
            hide michikoroom02b
            hide michikoroomtable
            show michikoroom02a
            show michikoroomtableb                
            mi "Well, thank you for coming over. I appreciated your comapny... Somewhat. Now I must get ready for tomorrow. And you are not invited in my bed tonight." 
            mc "(Damn it. I think I screwed up this date...)"
            mi "Goodnight [name]..."
            $ period += 1
            $ michikodatedone = True
            $ michikodateon = False
            $ michikodateontomorrow  = False
            jump Bedroom        
    "I like it a lot. Especially the deep cleavage...":
        hide michikoroom02a
        hide michikoroomtable
        show michikoroom02d
        show michikoroomtableb                
        mi "Yes, I noticed you OGLING them... That's why I wore it..."
        $ michikodate += 1
        mi "And since you're interested in them, I would like you to help me choose an outfit for my stripping gig."
        mc "Alright!"
        mi "Don't move, I'll come back wearing something even SEXIER..."
        jump MichikoDateLast       
    "What's the special occasion then?":
        hide michikoroom02a
        hide michikoroomtable
        show michikoroom02c
        show michikoroomtable        
        mi "But... How could you ask THAT? We are on a DATE!"
        mc "Ah yeah, I forgot, sorry. Drinking tea and dating are a weird concept to me."
        mi "Humpf.... It is traditional when dating Asian girls. You have still much to learn. You are too young."        
        hide michikoroom02c
        hide michikoroomtable
        show michikoroom02a
        show michikoroomtable        
        $ michikodate -= 1
        if michikodate >= 1:
            mi "However, I would still like you to help me choose an outfit for my stripping gig, since you have good taste in women..." 
            mc "Alright!"
            mi "Don't move, I'll come back wearing something even SEXIER..."
            jump MichikoDateLast
        if michikodate == 0:
            mi "Well, thank you for coming over. I appreciated your comapny... Somewhat. Now I must get ready for tomorrow. And you are not invited in my bed tonight." 
            mc "(Damn it. I think I screwed up this date...)"
            mi "Goodnight [name]..."
            $ period += 1
            $ michikodatedone = True
            $ michikodateon = False
            $ michikodateontomorrow  = False
            jump Bedroom        
                
label MichikoDateLast:
stop music
scene michikoroombed
show michikoroom10
with dissolve
mi "So, what do you think of this outfit?"
mc "Very nice, hugs your curves tightly..."
hide michikoroom10
show michikoroom11
with fastdissolve
mi "Check out the back and tell me what you think..."
mi "You can come closer... this once. To admire my ass."
scene michikoroombed blurred
show michikoroom14
with dissolve
mc "I think I'm getting DIZZY! But it's so TIGHT, it seems hard to take off."
scene michikoroombed
show michikoroom12
with dissolve
mi "Oh, it's not, all I have to do is slowly let the straps fall off..."
hide michikoroom12
show michikoroom13
with fastdissolve
mi "And my huge tits are out in no time!"
mc "I can get my COCK out in no time if you want!"
mi "Not now, let's not ruin this date with sex."
mc "(Damn it.)"
mi "If you want to see MORE, come and visit me in the strip corner next to the bar! *wink*"
hide michikoroom13
show michikoroom10
with fastdissolve
mi "Thank you for accepting my date offer [name], I enjoyed TALKING to you. And being just slightly NAUGHTY."
call LustPlusMichiko
$ period += 1
mc "(I guess I should go back to my bedroom then. And wank myself silly.)"
$ michikodatedone = True
$ michikodateon = False
$ michikodateontomorrow  = False
jump Bedroom

label RubyDate:
play music "v07/datemusic.mp3"
scene canyon01
show rubydate00
with fade
ru "What's this place. I see... trees. What the fuck???"
mc "So, err... Isn't it beautiful, right? And so peaceful."
hide rubydate00
show rubydate01
ru "Are you taking the piss? I don't want PEACE, I'm a Road Warrior! Let's chop those trees down."
mc "Well, hang on, I mean... We could find something else to do."
ru "Like what? This place is totally BORING."
mc "How about we compare muscles? I bet mine are bigger."
hide rubydate01
show rubydate02
ru "Oh yeah? I'd like to see you beat THESE!"
hide rubydate02
show rubydate03
with fastdissolve
ru "See that muscular body? No one can compare to me..."
mc "Well, girls maybe. ALPHA-STUDS like me on the other hand..."
hide rubydate03
show rubydate04
with fastdissolve
ru "You're sure about that? Watch those biceps... How fucking huge they are..."
show rubydate04 at right with move
show mcdate01 at left with moveinleft
mc "Not bad. For a girl."
ru "Shut up and come and worship them [name]! Or this date is OVER!"
mc "Alright, alright... Gee."
scene canyon01 blurred
show rubyworship01
with fastdissolve
ru "Yeah, that's it, lick those guns...Feel how HARD they feel, like solid granite..."
mc "Indeed. And something else is getting hard around here..."
ru "FILTHY BOY! We're comparing muscles, not cocks, so show me what you've got , big boy..."
scene canyon01
show rubydate05
with dissolve
ru "Impressive... But not the boulders I was expecting."
mc "That's cos I haven't flexed them yet... Now watch me flex my MASSIVE GUNS until they almost reach the sky!"
hide rubydate05
show rubydate06
with fastdissolve
ru "FUCK ME! I've never seen chunks of muscle that BIG! Even on Road Warriors..."
call LustPlusRuby
mc "Over 25 inches around of pure teenage muscle power right there Ruby!"
ru "You should train at the gym as often as possible then, to get EVEN BIGGER!"
mc "I AM going there, and getting STRONGER every week I assure you!"
hide rubydate06
show rubydate07
with fastdissolve
ru "I'll only agree to join your harem when you're TOTALLY RIPPED TO SHREDS [name]..."
play sound "Sounds/kiss.mp3"
$ renpy.pause(2.0, hard='True')
mc "(I guess I need to reach a certain level of strength before I can invite her into my harem then...)"
scene canyon01
show rubydate02
with dissolve
ru "Thanks for that MANLY date [name]. But I need to go back to the workshop and do even MANLIER stuff."
mc "See you around Ruby..."
$ period += 1
$ rubydatedone = True
$ rubydateon = False
stop music
jump Bedroom

label SukiDate:
play music "v07/datemusic.mp3"
scene canyon01
show sukidate01
with fade
su "Wow, this place is absolutely BEAUTIFUL! Thank you so much for taking me here [name]!"
mc "My pleasure, I knew you would like to get outdoors and...err... get in your bikini."
hide sukidate01
show sukidate02
with fastdissolve
su "I can finally stretch my legs a bit and enjoy the sunshine, instead of being stuck in the compound basement..."
mc "You're welcome to suntan, we have several hours ahead of us here..."
hide sukidate02
show sukidate03
with fastdissolve
su "Mmh, yes, I might just do that."
menu:
    "Topless?":
        su "Why, you want to ogle my big Asian breasts [name]?"
    "Watch out for sunburns though.":
        su "Thank you for reminding me, I almost forgot how it feels to be outdoors..."
mc "It's just that tanlines might ruin your otherwise flawless complexion."
hide sukidate03
show sukidate01
su "Ah yeah, that's true. I hadn't thought about that, you seem to know a lot more than me about outdoors stuff."
mc "Sure, I'm an adventurer and a HERO, so I need to know about that kind of stuff."
su "Sure you are, sure you are... And hopefully a valuable asset for the Deep State... Let's go and lie down on that rock over there."
        
scene sukidatenaked01 with fade
mc "Cool, she even decided to go full naked..."
scene sukidatenaked02
su "Did you say something [name]?"
mc "Err..."
su "Why don't you join me on this rock, you need to catch some sun too. I read on the dark web that sun rays cleanse the skin of radioactivity..."
mc "Really? Then I'll definitely join you. COMMANDO-style!"
su "I thought so..."
scene sukidatenaked03
su "Especially since there is a LOT of skin that needs cleansing on that giant dong of yours... *wink*"
scene canyon01 with dissolve
show sukidate01
$ period += 1
su "Well, thank you for this great date with me... I... should go now."
mc "A goodbye kiss perhaps?"
su "Of course, I thought you'd never ask!"
hide sukidate01
scene canyon01 blurred with fastdissolve
show sukidate04
play sound "Sounds/kiss.mp3"
$ renpy.pause(2.0, hard='True')
call LustPlusSuki
scene canyon01 with dissolve
show sukidate01
mc "See you around the compound Suki..."
su "Yes, I sure WILL..."
$ sukidatedone = True
$ sukidateon = False
stop music
jump Bedroom

label MarnieDate:
play music "v07/datemusic.mp3"
scene canyon01
show marniedate02
with fade
ma "I know this place, but I haven't been here in a while... There are too many alcoholics in the compound and I have very little free time."
mc "Who's manning the bar this morning then?"
hide marniedate02
show marniedate01
with fastdissolve
ma "Cyrl is. But I'll make sure to count how many Tar Cocktails she drinks and CHARGE them to her account!"
mc "So, what shall we do?"
hide marniedate01
show marniedate04
with fastdissolve
ma "I know what you're thinking... You're wondering where my Road Warriors tattoo is, aren't you?"
mc "Purely out of professional interest. I need to better understand Road Warriors lore and customs for my missions."
hide marniedate04
show marniedate05
with fastdissolve
ma "Well, it's right there on my left ankle... Do you want to get a closer look since you're such a \"professional\"?"
scene canyon03 blurred
show marniedate06
mc "I see... A skull. Surrounded by roses."
ma "That's right, it represents the fight between love and death. Sometimes you have to sacrifice your loved ones to avoid death."
mc "(She's a troubled girl it seems...) Well, I'm also in a fight between love and death. The love for my dead family and the fact that I'm going to kill that motherfucker Trumpf!"
scene canyon02
show marniedate03
with fastdissolve
ma "That's good [name], you have RESOLVE. And you NEED that to survive in this merciless world."
call LustPlusMarnie
hide marniedate03
show marniedate07
ma "Now let's swim, it's good for the muscles. And you NEED to get even BIGGER muscles."
scene marniecanyon01 with dissolve
play sound "Sounds/dive.mp3"
mc "Wow, she's pretty fit and a very good swimmer. I really have to strain myself to keep up with her."
$ period += 1
scene marniecanyon02 with fade
ma "Mmmh, isn't it a marvellous place? I wish I could be here all day... Did you have a good swim?"
mc "*Puff*... Yeah, I think... I can feel it in my muscles."
ma "I told you it was a good exercise. Now let's see how BIG they've become..."
scene marniecanyon03
ma "Mmmh, VERY nice... And VERY BIG..."
$ mcstrengthlevel += 1
scene marniecanyon03 with dissolve
if mcstrengthlevel == 1:
    mc "A couple more workouts like this one and I'll get STRONGER for sure!"   
if mcstrengthlevel == 2:
    mc "I need another workout like this one and I'll get STRONGER for sure!"   
if mcstrengthlevel == 3:
    mc "Damn, my muscles are definitely getting BIGGER and STRONGER!"
    call PlusStrength
    $ mcstrengthlevel = 0
ma "I told you this was a very good exercise for your muscles [name]. That's how I get MY six-pack."
ma "But enough admiring our muscles, it's getting late and I have to get back to the bar. Hopefully, Cyrl won't be on the floor, totally tar-drunk, like last time."
scene canyon01 blurred
show marniedate01
with dissolve
ma "Thanks a lot for this wonderful date [name]!"
$ marniedatedone = True
$ marniedateon = False
stop music
jump Bedroom

label PennyDate:
play music "v07/datemusic.mp3"
scene canyon01
show pennydate01
with fade
pe "How come I'm a scout and I don't even know about this place???"
mc "Beats me, it's right next to the compound."
hide pennydate01
show pennydate02
with fastdissolve
pe "How many people know about this? And will someone else turn up while we're on our date?"
mc "Just a few and don't worry, no one will disturb us. We have the the place to ourselves for the whole morning..."
hide pennydate02
show pennydate04
with fastdissolve
pe "Good, now let's get in the water and start this date shall we?"
scene canyon02
show pennydate03
with fastdissolve
pe "The water is nice... But I feel like ALL of my skin is not enjoying it."
mc "What do you mean?"
pe "Modern society's moral constraints are not for ME. I'm a ROAD WARRIOR at heart! So I want to be free and... NAKED!"
mc "I'll all for the old values of old society, Penny!"
scene canyon01 blurred
show pennydate05
pe "That's... not really what I meant. THIS is what I meant."
mc "Yeah, that's what I meant too!"
pe "In that case, you should ALSO get naked, right!"
mc "Err... Right, right."
scene pennydate06
with dissolve
pe "Ah, that's MUCH better."
scene pennydate07
with dissolve
pe "And how are YOU doing, [name]? Enjoying the water on your FULL body?"
scene pennydate08
with dissolve
mc "Err, Yeah sure. I'm just... chilling, you know."
scene pennydate09
with dissolve
pe "With a great big HARDON! That's what you do on all your dates, you dirty boy?"
mc "Err..."
scene pennydate10
with dissolve
pe "Don't answer and let my LIPS do all the talking..."
mc "O..Okay."
pe "Now of course, this is our first date, so you won't get much from me. I'm not such an easy girl..."
scene pennydate11
with dissolve
pe "But a little kiss and a little taste of your abundant pre-cum can't hurt that much, right?"
play sound "Sounds/kiss.mp3"
call LustPlusPenny
pe "There, that's it."
mc "That's it? But... My hardon, it hurts!" 
pe "That'll teach you for rudely displaying your genitals on a first date... But thanks for the date anyway [name], I... enjoyed it."
$ pennydateon = False
$ pennydatedone = True
$ period += 1
stop music
jump Bedroom

label AylaDate:
play music "v07/datemusic.mp3"
scene canyon01
show ayladate01
with fade
ay "Yeah, OK, this place is alright for a date, I guess."
ay "Are you repeating what I'm saying???"
mc "No, there's an echo here, that's all."
hide ayladate01
show ayladate02
with fastdissolve
ay "Boring. BORING!"
"Boring.. Boring..."
mc "That was fun, right? And can you feel the fresh air? It's invigorating, isn't it?"
hide ayladate02
show ayladate03
with fastdissolve
ay "What are you babbling about? It's just... air. Like the air in the compound."
mc "With less radioactivity though, cos there's a breeze flowing through the canyon, can't you feel it?"
ay "Not really."
scene ayladate08 with dissolve
mc "I can totally feel it cos I'm all wet."
ay "I ain't ready to go in the water."
scene ayladate09 with dissolve
mc "Are you scared? There's nothing bad in the water, all life is dead. So it's totally safe."
ay "Al...alright."
scene ayladate10 with dissolve
mc "Yeah, take your top off so you can really feel the breeze."
ay "I knew you would like that..."
scene ayladate11 with dissolve
play sound "Sounds/dive.mp3"
mc "(nice. This date is finally getting somewhere...)"
scene ayladate12 with dissolve
ay "Well, I'm all wet now, but I don't feel a thing. This place is boring. Let's leave."
mc "No, no, no, you need to...err... get out of the water to feel the breeze. Especially on your nipples."
ay "Where did you hear such a pile of nonsense?"
mc "Err... In a book. Trust me. I'm topless and I can feel the breeze. It's coming straight down from Phallus Heaven."
ay "I'll check if it's bullcrap or not then. It better not be BULLSHIT, I'm warning you!"
scene canyon02 blurred
show ayladate04
with dissolve
ay "Mmmh, Ok, I guess I feel something now. And now what?"
mc "Just wait a bit, the breeze will refresh you. And make your nipples harden."
hide ayladate04
show ayladate05
with fastdissolve
ay "Alright, I'll admit it, I can feel the breeze now... But it's not very strong, kind of BORING!"
hide ayladate05
show ayladate06
with fastdissolve
mc "I'll lick you arm and increase the feel of freshness. Can you feel it?"
ay "Hee hee, it's tickling me! But what about my nipples? I'm not letting you lick them on a first date!"
mc "I've got another idea, I'll lift you up and they'll be in contact with my wet skin."
hide ayladate06
show ayladate07
with fastdissolve
ay "OOoh, I see. I can feel your huge musc.. I mean your wet skin on my nipples now... Thanks for showing me your trick."
play sound "Sounds/kiss.mp3"
call LustPlusAyla
ay "Now get me down, you're getting me all wet!"
scene canyon02
show ayladate05
with dissolve
$ period += 1
ay "I think this date is over. I've seen enough... And so have you. It was kind of... nice. Thank you [name]."
$ ayladateon = False
$ ayladatedone = True
stop music
jump Bedroom

label GwenDate:
play channel1 "v07/datemusic.mp3"
scene canyon01
show gwendate01
with fade
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
call LustPlusGwen
mc "You're welcome... Wow, you really pumped me dry. I mean, pumped yourself dry..."
gw "I can see that, cum puddles are floating everywhere around us. I hope no one else plans on coming here today..."
scene canyon01
show gwendate01
with dissolve
$ period += 1
gw "I think that date went pretty well at the end... But I'm exhausted, so let's go back to the compound."
mc "Sure... I'm exhausted too for some reason."
$ gwendatedone = True
$ gwendateon = False
stop channel1
jump Bedroom

label LenaDate:
play channel1 "v07/datemusic.mp3"
scene canyon01
show lenadate01
with fade
le "I had to tell Jake I was going on an exploratory mission. This had better be worth me lying to my husband."
mc "Oh, it will be Lena, it will be..."
hide lenadate01
show lenadate02
with fastdissolve
le "What is this place anyway? And how come no one ever told me about it? It's quite beautiful..."
mc "It's a well-known dating place around the compound. So remember I'm the one who told you about it then. All the others are liars. And maybe Jake too for all we know..."
hide lenadate02
show lenadate03
with fastdissolve
le "Jake? You think he might... But who would want to date this dufus?"
mc "Some women are desperate. But not you... You're the boss, you can choose whoever you want..." 
hide lenadate03
show lenadate04
with fastdissolve
le "Well, today, I choose YOU [name]. Jake never invited me HERE on a romantic date."
mc "I know how to treat my women... Err, I mean, ladies such as yourself."
le "Is that so? Prove it by kissing me then..."
hide lenadate04
show lenadate05
with fastdissolve
play sound "Sounds/kiss.mp3"
le "Mmmmh, you're a better kisser than Jake I must admit..." 
scene canyon02 blurred
show lenadate06
with dissolve
le "And what is this thing that's growing in your swimtrunks and getting absolutely MASSIVE?"
mc "Well, err... sorry, it has a mind of its own."
le "Well, you can't go swimming with this monster log down there, so why don't you take your trunks off. In exchange, I'll take MY top off..."
mc "It's a deal!"
scene lenadate07 with dissolve
mc "Will you join me in the water, Chief?"
le "Let me put some water on my skin first... You go ahead."
scene lenadate08 with dissolve
le "Mmh, the water has the perfect temperature... To make my nipples all hard..."
mc "And my cock ROCK-HARD."
scene lenadate09 with dissolve
le "What? Are you jerking off??? On our date?"
mc "No, I was just... err... Moving it aside to hide it. I mean, it's not appropriate to have a big boner on a date, is it?"
scene lenadate10 with dissolve
le "I think you're lying... You WERE jerking off weren't you? To my body... Right?"
mc "Well, err... Yes, maybe... No... I mean, I wouldn't do that on a date!"
le "I don't believe you. So go on, wank that fat shaft. Jerk it for me. I want to see you EXPLODE. Thinking about me..."
mc "Err. Okay. Chief."
play channel2 "Sounds/wank.mp3"
show lenadateslow
call screen lenadatewankslow
screen lenadatewankslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaDateWankFast") 

label LenaDateWankFast:
le "Do it faster now, stroke that monsterdick for your chief!"
hide lenadateslow
show lenadatefast
call screen lenadatewankfast
screen lenadatewankfast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaDateWankEnd") 

label LenaDateWankEnd:
mc "Chief...I'm so eager to please you, tell me when to cum for you please!"    
scene lenadate13 with fastdissolve
le "That's right, I 'm still your boss. So I'm giving you an ORDER to flog your monster dong with BOTH HANDS NOW, until you EXPLODE everywhere, you hear me?"
mc "Oh God, you're making me so horny speaking to me like that, I'll do it, I'll obey your orders Chief!"
hide lenadateslow
hide lenadatefast
show lenadatebothslow
call screen lenadatewankbothslow
screen lenadatewankbothslow:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("LenaDateWankbothFast") 

label LenaDateWankbothFast:
le "Keep going [name], but FASTER now! I LOVE watching you pleasure your YOUNG GIANT pussy-wrecker! It's so much BIGGER and POWERFUL than Jake's!"
hide lenadatebothslow
show lenadatebothfast
call screen lenadatewankbothfast
screen lenadatewankbothfast:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("LenaDateWankbothEnd") 

label LenaDateWankbothEnd:
le "And now, I ORDER you to COME for me!"
scene lenadate16 with fastdissolve
pause 0.2
stop channel2
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "AAAH! Here it comes!"
scene lenadate17 with dissolve
stop sound
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
le "Yes, keep pumping that fat load while you admire my toned buttcheeks name!"
mc "I am Chief Lena, I'm cumming for you! RHHAAAA!"
scene lenadate18 with dissolve
stop sound
mc "God, I came so much... And all over myself too."
le "That's cos you're a very DIRTY boy! You came like, a year's worth of supply of sperm from Jake, it was incredible..."
call LustPlusLena
scene canyon01
show lenadate01
with dissolve
le "Well, that date went pretty well I'd say. For YOU especially... And now I know about this place. So I learnt something too."
mc "Glad you enjoyed Lena..."
le "CHIEF Lena to you. I'm not your harem girl... Yet. *wink*" 
le "Let's go back to the compound, it's getting late."
$ period += 1
$ lenadatedone = True
$ lenadateon = False
stop channel1
jump Bedroom

label ClaraDate:
play music "v07/datemusic.mp3"
scene canyon01
show claradate01
with fade
cl "I hope this bathing suit is to your liking, it is unfortunately the only one the Church will allow me to wear..."
mc "My imagination is seeing right through it, so don't worry."
cl "Oh... Well, I sure hope that you have a... nice imagination."
hide claradate01
show claradate02
with fastdissolve
cl "It is amazing how the sun shining from the Phallus Lord's One Eye turns this canyon into such a wonderful and peaceful place..."
cl "I really don't know how to thank you for showing me this place..."
mc "An extra lust point perhaps?"
hide claradate02
show claradate03
with fastdissolve
cl "That would be...too soon. This date hasn't even started properly yet."
cl "And I... I am embarrassed to admit... that I can't swim. I... never learnt."
hide claradate03
show claradate04
with fastdissolve
mc "Well don't worry, I'm a good swimmer and I'll teach you."
cl "Oh really? That is... so sweet of you... I actually brought along an inflatable banana float. Which is all I could find in the Church's inventory."
mc "That should do the trick to start with. I'll blow it up and you just get in the water where it's shallow."
scene claradate05 with dissolve
cl "I... I think I'm in too deep, I can't feel the bottom of the lake!" 
mc "Hang on, I'll come and help you Clara!" 
scene claradate06 with dissolve
mc "There, you have nothing to worry about anymore. Why don't you try without the float?"
cl "O...Okay, But you stay behind me to catch me if I start drowning, right?"
mc "Of course, I'll be right behind you."
scene claradate07 with dissolve
mc "See, it wasn't so hard. And I can easily catch you if you slip and carry you to safety."
cl "Thanks [name]. I feel... safer with you around... And I know you could easily lift me in your... muscular arms."
mc "You want me to show you?"
cl "Err, alright, but please hold me tight [name]!"
scene claradate08 with dissolve
mc "I don't need to hold you tight when I can just hold you with one arm up in the air!"
cl "Dear Phallus Lord! You are sso STRONG! But please let me down, I am scared of height on top of being scared of water!"
scene claradate09 with dissolve
cl "This date went... very well. I haven't felt that way since I... embraced the Phallus Lord and made my vows..."
mc "Why don't you embrace ME this time then?"
scene claradate10 with dissolve
play sound "Sounds/kiss.mp3"
cl "Mmmh...."
call LustPlusClara
mc "*Bingo*"
scene claradate09 with dissolve
cl "Let's go back to the compound, it's getting late and I have Church duty."
mc "Of course Clara, I'll help you back onto the shore."
$ period += 1
$ claradatedone = True
$ claradateon = False
stop music
jump Bedroom

label LaurieDate:
play music "v07/datemusic.mp3"
scene canyon01
show lauriedate01
with fade
mc "This is it. The Red Canyon. Even has trees. Not edible though, I warn you."
hide lauriedate01
show lauriedate02
with fastdissolve
la "Ah yes, I remember this place when I visited it years ago to install a water pump for my salads..."
mc "But you haven't been here since, right?"
hide lauriedate02
show lauriedate03
with fastdissolve
la "No I haven't. I haven't been invited on a date actually. Come, let's go for a swim, I'm dying to get into the water!"
scene lauriedate04 with dissolve
la "The water is so nice. And pure. That's why my salads taste so great!"
mc "Don't go too far though, it can get pretty deep around here."
scene lauriedate05 with dissolve
la "Don't worry about me, I know how to swim, I want to cross onto the other side and see if I can find some interesting new plants."
mc "Okay, I'll swim along with you then, just to be on the safe side."
la "You wouldn't want to lose your date, now would you? *wink*"
scene lauriedate06 with dissolve
la "Oh, I think I found the entrance to a cave... Let's go inside, this is exciting!"
mc "Err... You're sure this is a good idea. I was thinking more of...like swimming and you admiring my muscles and then me kissing you. The sort of stuff that usually happens on my dates."
la "Yes, I AM sure. If you don't come with me, I'll go ALONE."
mc "Fine, I'll follow you then..."
stop music
play music "v072/cave.mp3"
scene lauriedate07 with dissolve
la "Wow, look at this cave, it's beautiful!"
mc "Remember that I invited you on this date. Without my input, we would never have stumbled upon this place..."
scene lauriedate08 with dissolve
la "And look, there are some mushrooms here too! Do you know that mushrooms are VERY nutritious?"
mc "And some of them are poisonous..."
scene cavebackground
show lauriedate09 at right
show lauriedate10 at left
with dissolve
la "These look alright to me. Why don't you try one? For me? Please."
menu:
    "Accept":
        jump MushroomAte
    "Refuse":
        jump MushroomNotAte

label MushroomAte:
hide lauriedate09
hide lauriedate10
show lauriedate11 at right
show lauriedate11b at left
with fastdissolve
la "So? Did it taste good?"
mc "It's okay I guess..."
stop music
hide lauriedate11b
show lauriedate12b at left
with fastdissolve
mc "AAARGH, what's happening? It hurts all over!"
la "[name]! Your bulge.... It's getting BIGGER! You're gonna rip the fabr..."
play sound "Sounds/ripping.mp3"
hide lauriedate12b
hide lauriedate11
show lauriedate12 at right
show lauriedate13b at left
with fastdissolve
mc "This is too much! My cock! It can't stop GROWING!"
la "I can see that... It's getting bigger than a tree trunk!"
hide lauriedate13b
hide lauriedate12
show lauriedate13 at right
show lauriedate14b at left
with fastdissolve
mc "Help me please Laurie, I can't feel my heart pumping anymore, all the blood is in my rod, AAAAH!"
la "Okay, maybe... Try and EJACULATE! Your cock will go soft and smaller and you'll have enough blood flowing into the rest of your body that way!"
hide lauriedate14b
show lauriedate15b at left
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "AAAAAHHHHH!"
with fastflash
la "Oh my God, this is the biggest monster cumshot I've eveer seen in my life! And I owned a poney when I was a child!"
hide lauriedate15b
hide lauriedate13
show lauriedate17 at right
show lauriedate16b at left
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "GOD DAMN, THIS IS TOO MUCH, RHAAAA!"
with fastflash
la "Keep going [name], let it ALL OUT, it's the ONLY way!"
hide lauriedate16b
show lauriedate17b at left
with fastdissolve
mc "Oooh, finally, I'm done, I... can feel the blood coming back..."
hide lauriedate17
show lauriedate16 at centerright
mc "But I feel nauseous. I think those mushrooms were poisonous..."
call MCInjury
$ mcinjuredmushroom = True
la "I'm sorry I told you to eat that thing... But you were very brave for sacrificing your health for the future of humanity!"
call LustPlusLaurie
mc "*Well at least I got a lust point out of this...*"
mc "I think I really need to get to the medbay, Laurie!"
la "Sure, I'll take you there, just hang in there and continue to be brave..."
jump LaurieDateEnd

label MushroomNotAte:
hide lauriedate10
show lauriedate10b at left
with fastdissolve
mc "Not really, I don't feel good about this..."
play sound "Sounds/slap.mp3"
hide lauriedate10b
hide lauriedate09
show lauriedateno
with fastdissolve
la "How dare you refuse my on-date demand! This date is OVER. Let's go back to the compound, I have to take care of my salads."
mc "Wow, that escalated quickly."
label LaurieDateEnd:
$ period += 1
$ lauriedatedone = True
$ lauriedateon = False
stop music
if mcinjured:
    jump Medbay
jump Bedroom

label BarbaraDate:
play channel1 "v07/datemusic.mp3"
scene canyon01
show barbaradate01
with fade
ba "Is this the place? I never knew it even existed. Chief Lena doesn't allow me out of the compound much...."
mc "Don't worry, she doesn't know you're here."
hide barbaradate01
show barbaradate02
with fastdissolve
ba "Well, it IS beautiful. Is the water radioactive?"
mc "Err, I never checked to be honest. But I'm been swimming here for a while and I'm totally normal."
hide barbaradate02
show barbaradate03
with fastdissolve
ba "Well, let's go for a swim then, it's scorching hot out here."
mc "Sure, Barbara!"
scene barbaradate04 with dissolve
ba "The water is really refreshing. I can't believe how hot it is today!"
mc "Yeah, I agree, it's hotter than normal. Maybe we're in summer?"
scene barbaradate05 with dissolve
ba "Yes, it's August. Don't you keep track of time? I'm getting out, I want to work on my tan while I'm here..."
scene barbaradate06 with dissolve
mc "I think you should put some protection on you. You wouldn't want to get sunburnt now would you?"
ba "Well, thank you for thinking about my health [name]... Unfortunately, I don't have any sunscreen. Do you?"
mc "No, but... err... I can provide some special cream."
scene barbaradate06b with dissolve
ba "Let me guess. You want me to rub your spunk over my body to protect me from the sun? Did I get that right?"
mc "Err, not exactly. I'd be rubbing it myself, you wouldn't have to do anything, teach!"
scene barbaradate06 with dissolve
ba "*sigh* Well, I have nothing to lose I guess. So go on, take your cock out and jack it over my body until you nut, you filthy boy."
mc "Alright! One serving of [name]'s special sun cream coming right your way, Barbara!"
play channel2 "Sounds/wank.mp3"
scene barbaradate07 with fastdissolve
pause 0.2
scene barbaradate08 with fastdissolve
pause 0.2
scene barbaradate07 with fastdissolve
pause 0.2
scene barbaradate08 with fastdissolve
pause 0.2
scene barbaradate07 with fastdissolve
pause 0.2
scene barbaradate08 with fastdissolve
pause 0.2
scene barbaradate07 with fastdissolve
pause 0.2
scene barbaradate08 with fastdissolve
pause 0.2
scene barbaradate07 with fastdissolve
pause 0.2
scene barbaradate08 with fastdissolve
pause 0.2
scene barbaradate07 with fastdissolve
pause 0.2
scene barbaradate08 with fastdissolve
pause 0.2
scene barbaradate07 with fastdissolve
pause 0.2
scene barbaradate08 with fastdissolve
pause 0.2
scene barbaradate07 with fastdissolve
pause 0.2
scene barbaradate08 with fastdissolve
pause 0.2
scene barbaradate08b with fastdissolve
stop channel2
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "That's it, [name]'s superior sunscreen for maximal protection is CO-O-MING!"
window hide
with fastflash
show barbaradate08c with dissolve
stop channel2
ba "Oh My God [name], that's a LOT of cream!"
window hide
with fastflash
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "My balls are FU-UUU-LLL!"
scene barbaradate09 with fastdissolve
mc "Turn around, teach, you also need cream on your front!"
window hide
with fastflash
mc "RHAAA!"
scene barbaradate10 with fastdissolve
ba "What the?... You're PLASTERING me in your filthy boyspunk!"
window hide
with fastflash
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
mc "You wanted protection, I give you protection Barbara, RHAAA!"
scene barbaradate11 with fastdissolve
play sound "Sounds/moaning02.mp3"
ba "Well, this date didn't go at all the way I expected it... I just let one of my students shower me with his cum..."
mc "I must admit I didn't see that coming either..."
ba "Still, you gave me the protection I needed. So now I'm going to enjoy the sun, and your sperm, on my skin..."
call LustPlusBarbara
stop channel1
stop sound
scene canyon01
show barbaradate01
with dissolve
ba "I'm done, I have a great tan now, thanks for taking me on this... date [name]."
mc "Glad I could have been of service to you... And your skin."
hide barbaradate01
show barbaradate03
with fastdissolve
ba "...Yes... But it's our little secret, you hear me?... Now let's get back to the compound before anyone sees us."
$ period += 1
mc "Sure teach... The period just advanced anyway so I'm supposed to do something else now."
$ barbaradatedone = True
$ barbaradateon = False
jump Bedroom

label BellaDate:
play channel1 "v07/datemusic.mp3"
scene canyon01
show belladate01
with fade
be "I'm glad we can finally be ALONE. I'm getting tired that you always bring a harem girl with you on my rig."
mc "It's for the good of the missions. Otherwise, I would definitely rather be ALONE with you, Bella..." 
hide belladate01
show belladate02
with fastdissolve
be "I'm flattered. Like, really. But you need MORE to get into MY panties..."
mc "Err, that's why I took you to this beautiful place befitting a... err, beautiful lady such as yourself."
hide belladate02
show belladate03
with fastdissolve
be "Nice try [name]... Is the water here also befitting me?"
mc "Oh, yes! It's crystal clear, pure, refreshing and...err..."
be "So hopefully better than in the compound's underground pool? Let's go for a swim then!"
scene belladate04 with dissolve
be "Mmmh, you were right, the water really IS refreshing here..."
scene belladate05 with dissolve
be "Since I want a nice even tan, I'll remove my top, I expect that you don't mind, do you?"
mc "Of course not, be my guest! I also want an even tan so..."
scene belladate06 with dissolve
mc "* Fuck Yeah... Time to make a move. With my COCK! *"
scene belladate07 with dissolve
if canonized:
    be "The water isn't refreshing enough for that cock of yours apparently. Maybe it's time for me to check what a Saint-Manhood looks like... UP CLOSE!"
    scene belladate10 with fastdissolve
    be "This cock sure is worthy of a Saint-Manhood..."
    mc "And you hot bod sure is worthy of handling it!"
    scene belladate11 with fastdissolve
    be "But can this cock handle THIS?..."
    play channel2 "Sounds/wank.mp3"
    scene belladate11 with fastdissolve
    pause 0.2
    scene belladate12 with fastdissolve
    pause 0.2
    scene belladate11 with fastdissolve
    pause 0.2
    scene belladate12 with fastdissolve
    pause 0.2
    scene belladate11 with fastdissolve
    pause 0.2
    scene belladate12 with fastdissolve
    pause 0.2
    scene belladate11 with fastdissolve
    pause 0.2
    scene belladate12 with fastdissolve
    pause 0.2
    scene belladate11 with fastdissolve
    pause 0.2
    scene belladate12 with fastdissolve
    pause 0.2
    scene belladate11 with fastdissolve
    pause 0.2
    scene belladate12 with fastdissolve
    pause 0.2
    scene belladate11 with fastdissolve
    pause 0.2
    scene belladate12 with fastdissolve
    pause 0.2
    scene belladate11 with fastdissolve
    pause 0.2
    scene belladate12 with fastdissolve
    pause 0.2
    scene belladate11 with fastdissolve
    pause 0.2
    scene belladate12 with fastdissolve
    pause 0.2
    scene belladate11 with fastdissolve
    pause 0.2
    scene belladate12 with fastdissolve
    pause 0.2
    mc "Ah, fuck, you're gonna make me..."
    stop channel2
    scene belladate13 with fastdissolve
    if persistent.cumsoundon:
        play sound "Sounds/mccum.mp3"
    mc "...CU-UUU-UUUM! AAAH!"
    window hide
    with fastflash
    be "Yeah, BLAST that young cream for me!"
    if persistent.cumsoundon:
        play sound "Sounds/cumming.mp3"
    window hide
    with fastflash
    mc "God, still MORE! RHAAA!"
    window hide
    with fastflash
    be "Damn, you keep PUMPING those hot shots everywhere!"
    play sound "Sounds/panting.mp3"
    scene belladate14 with fastdissolve    
    be "That must have been REAL good for you.... You came sssoo much. Very impressive Saint-Manhood!"
    call LustPlusBella
    $ period += 1
    mc "Oooh... The period just advanced, I didn't realize I came for THAT LONG. Maybe we should head back to the compound Bella..."
    be "No respite for HARD working scouts like us!"
    stop channel1
    $ belladatedone = True
    $ belladateon = False
    jump Bedroom
if canonized == False:
    be "The water isn't refreshing enough for that cock of yours apparently. It's a rather disgusting sight while I'm trying to enjoy a relaxing date..."
    mc "Err... Sorry, it has a mind of its own sometimes..."
    stop channel1
    be "Well, cover it at least!"
    scene belladate08 with fastdissolve
    mc "Sure..."
    scene belladate09 with fastdissolve
    be "Now you blew your chances. By being so DISGUSTING in front of a devout woman such as myself. Your cock ain't even canonized! I'm leaving and going back to the compound..."
    scene belladate08 with fastdissolve
    mc "But... The date has even started yet!"
    $ period += 1
    be "Well, the period has advanced, so it's OVER."
    mc "I don't even get a lust point for that???"
    $ belladatedone = True
    $ belladateon = False
    jump Bedroom    


label DebraDate:
play music "v07/datemusic.mp3"
scene canyon01
show debradate01
with fade
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
call LustPlusDebra
scene debradate11a with fastdissolve
de "I... guess so... I think I need to get back in the lab. And work on these glasses..."
scene debradate11b with fastdissolve
mc "I don't need glasses like that. My vivid imagination is often enough..."
de "I see..."
mc "No, I SEE!"
stop music
$ period += 1
scene canyon01
show debradate02
with dissolve
de "Thanks for the date after all [name]. It did help me clear my mind."
hide debradate02
show debradate01
with fastdissolve
de "Even a genius like needs to unclatter it sometimes!"
$ debradatedone = True
$ debradateon = False
jump Bedroom    

