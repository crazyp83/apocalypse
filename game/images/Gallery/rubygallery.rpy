label RubyGallery:
stop music
call screen galleryruby
screen galleryruby:
    add "Gallery/rubygallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("galleryruby"), Jump ("MainGallery")]

    if renpy.seen_image("rubytits01"):
        imagebutton:
            focus_mask True
            idle "Gallery/rubygallery01.png" xpos 621 ypos 100
            hover "Gallery/rubygallery01.png"
            action Jump ("RubyGallery01")

    if renpy.seen_image("rubytits01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("RubyGallery")

    if renpy.seen_image("rubydate01"):
        imagebutton:
            focus_mask True
            idle "Gallery/rubygallery02.png" xpos 1050 ypos 100
            hover "Gallery/rubygallery02.png"
            action Jump ("RubyGallery02")

    if renpy.seen_image("rubydate01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("RubyGallery")

    if renpy.seen_image("fightrubywin"):
        imagebutton:
            focus_mask True
            idle "Gallery/rubygallery03.png" xpos 1478 ypos 100
            hover "Gallery/rubygallery03.png"
            action Jump ("RubyGallery03")

    if renpy.seen_image("fightrubywin") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("RubyGallery")

    if renpy.seen_image("rubygym02"):
        imagebutton:
            focus_mask True
            idle "Gallery/rubygallery04.png" xpos 621 ypos 400
            hover "Gallery/rubygallery04.png"
            action Jump ("RubyGallery04")

    if renpy.seen_image("rubygym02") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("RubyGallery")

    if renpy.seen_image("lockerrubyfuck01a"):
        imagebutton:
            focus_mask True
            idle "Gallery/rubygallery05.png" xpos 1050 ypos 400
            hover "Gallery/rubygallery05.png"
            action Jump ("RubyGallery05")

    if renpy.seen_image("lockerrubyfuck01a") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1050 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("RubyGallery")

    if renpy.seen_image("rubylingerie01"):
        imagebutton:
            focus_mask True
            idle "Gallery/rubygallery06.png" xpos 1478 ypos 400
            hover "Gallery/rubygallery06.png"
            action Jump ("RubyGallery06")

    if renpy.seen_image("rubylingerie01") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 1478 ypos 400
            hover "Gallery/gallerylocked.png"
            action Jump ("RubyGallery")

    if renpy.seen_image("rubylingerie05"):
        imagebutton:
            focus_mask True
            idle "Gallery/rubygallery07.png" xpos 621 ypos 700
            hover "Gallery/rubygallery07.png"
            action Jump ("RubyGallery07")

    if renpy.seen_image("rubylingerie05") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 700
            hover "Gallery/gallerylocked.png"
            action Jump ("RubyGallery")

    add "Gallery/galleryfuture.png" xpos 1050 ypos 700

    add "Gallery/galleryfuture.png" xpos 1478 ypos 700

    add "Gallery/gallerygrid02.png"
    add "Gallery/textruby.png"


label RubyGallery01:
scene workshop03
show ruby01
ru "Hey there big boy. What's up?"
scene workshop03
show ruby01
mc "You said you were a Road Warrior. But I can't see any tattoo on you."
hide ruby01
show rubyflex
ru "Oh, you wanna see my tattoo, hey? You're wondering where it is aren't you? Have a guess."
mc "On your huge clitoris?"
hide rubyflex
show ruby07
with fastdissolve
ru "What the fuck? No, you moron!"
hide ruby07
scene workshop03 blurred
show rubytits01
with fastdissolve
ru "It's on my right breast...Just below my nipple stud... You wanna suck on it big boy?"
mc "Of course! And fondle those massive tits too!"
ru "You can't, no touching, just your tongue on my nipple..."
hide rubytits01
show rubytits02
with fastdissolve
ru "There you go, just suck on it, play with your tongue..."
hide rubytits02
show rubytits03
with fastdissolve
ru "Oooh, I feel... so turned on..."
hide rubytits03
show rubytits04
with fastdissolve
ru "Enough now... You got my nipples all hard... Naughty boy..."
ru "I'd better get my top back on before someone sees us..."
hide rubytits04 with dissolve
jump RubyGallery

label RubyGallery02:
play music "v07/datemusic.mp3"
scene canyon01
show rubydate00
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
mc "Over 25 inches around of pure teenage muscle power right there Ruby!"
ru "You should train at the gym as often as possible then, to get EVEN BIGGER!"
mc "I AM going there, and getting STRONGER every week I assure you!"
hide rubydate06
show rubydate07
with fastdissolve
ru "I'll only agree to join your harem when you're TOTALLY RIPPED TO SHREDS [name]..."
play sound "Sounds/kiss.mp3"
window hide
$ renpy.pause(1.0, hard='True')
mc "(I guess I need to reach a certain level of strength before I can invite her into my harem then...)"
scene canyon01
show rubydate02
with dissolve
ru "Thanks for that MANLY date [name]. But I need to go back to the workshop and do even MANLIER stuff."
mc "See you around Ruby..."  
stop music
jump RubyGallery

label RubyGallery03:
scene fridayparty02
show virtuallena at left
show virtualruby at midright
$ ruby_health = 5.0
$ lena_health = 5.0
show screen screenfightlenaruby
play sound "Sounds/barfight.mp3"
ma "Our two contenders tonight are..."
scene lenafight01 with dissolve
ma "LENA!"
window hide
play sound "Sounds/applause.mp3"
show lenasign at streetfight01
$ renpy.pause(1, hard=True)
show lenasign:
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
scene rubyfight01 with dissolve
show lenasign:
    xalign 0.4
    yalign 0.4
show versussign:
    xalign 0.5
    yalign 0.5
ma "RUBY!"
window hide
play sound "Sounds/applause.mp3"
show rubysign at streetfight03
$ renpy.pause(1, hard=True)
show rubysign:
    xalign 0.6
    yalign 0.6
pause 1.0
stop sound
scene fightsetup with dissolve
show rubysetup at midright
show lenasetup at midleft
play sound "Sounds/fight.mp3"
show fightsign at streetfight02
$ renpy.pause(1, hard=True)
hide fightsign
show rubysetup at center with move
ma "Ruby makes a move..."
scene lenarubyfight01    
ma "She lounges forward with the mindset of a berserk Road Warrior..."
scene lenarubyfight02
ma "..But Chief Lena saw it coming and fiercely knees her pussy!"
play sound "Sounds/punch.mp3"
$ renpy.pause(.5, hard=True)
show groinkick:
    xalign 0.5
    yalign 0.8    
$ counting = 0
while counting < 20:
    $ ruby_health -= 0.05
    $ counting += 1
    pause 0.01
scene lenarubyfight03
ma "Followed by a hick kick to the boobs! Ruby is sent flying into the corner! What a move by our Chief!"
play sound "Sounds/punch.mp3"
$ renpy.pause(.5, hard=True)
show boobkick:
    xalign 0.7
    yalign 0.4    
$ counting = 0
while counting < 20:
    $ ruby_health -= 0.05
    $ counting += 1
    pause 0.01
scene fightsetup with dissolve
show rubysetup at midright
show lenasetup at midleft
$ renpy.pause(1, hard=True)
ma "Back to the drawing board with Chief Lena in the lead!"
show lenasetup at center with move
ma "Lena is the one on the attack this time..."
scene lenarubyfight08
ma ".. But Ruby grabs her on the move and holds her tight in a spine-crushing fashion!"        
$ renpy.pause(.5, hard=True)
show spinecrush:
    xalign 0.6
    yalign 0.6       
$ counting = 0
while counting < 20:
    $ lena_health -= 0.05
    $ counting += 1
    pause 0.01
ma "That will cause a huge health loss to Lena for sure..."
scene fightsetup with dissolve
show lenasetup at midleft
show rubysetup at midright
$ renpy.pause(1, hard=True)
show rubysetup at center with move
ma "Ruby makes a move..."
scene lenarubyfight01 with fastdissolve
ma "She's gone into berserk mode again!"
scene lenarubyfight06 with fastdissolve
ma "This time, Lena can't stop her from scissoring her with her strong legs..."
$ renpy.pause(.5, hard=True)
show scissorlegs:
    xalign 0.7
    yalign 0.6       
$ counting = 0
while counting < 20:
    $ lena_health -= 0.05
    $ counting += 1
    pause 0.01
ma "Oops, Lena is showing some virtual nipple there, children please look away."
scene lenarubyfight07 with fastdissolve
ma "... And Ruby ends her move by delivering a mighty punch to Lena's face!"
play sound "Sounds/punch.mp3"
$ renpy.pause(.5, hard=True)
show headpunch:
    xalign 0.3
    yalign 0.6       
$ counting = 0
while counting < 20:
    $ lena_health -= 0.1
    $ counting += 1
    pause 0.01
ma "Lena is badly bruised but not yet defeated..."
scene fightsetup with dissolve
show rubysetup at midright
show lenasetup at midleft
$ renpy.pause(1, hard=True)
show lenasetup at center with move
ma "And now Lena is on the prowl..."
scene lenarubyfight04 with dissolve
ma "She moves like a cat in heat and appears out of nowhere from underneath Ruby..."
$ renpy.pause(.5, hard=True)
$ counting = 0
while counting < 20:
    $ ruby_health -= 0.05
    $ counting += 1
    pause 0.01    
scene rubyfight01
ma "Ruby fell hard on this one but quickly gets up!"
scene lenarubyfight10 with dissolve
ma "While Lena is still on the floor, Ruby grabs her by the legs..."
scene lenarubyfight11 with dissolve
ma "She's pushing hard with all her might to break Lena's spine! My God, this is so hard to watch!"
play sound "Sounds/bonecrack.mp3"
$ renpy.pause(.5, hard=True)
show spinecrush:
    xalign 0.5
    yalign 0.7       
$ counting = 0
while counting < 20:
    $ lena_health -= 0.05
    $ counting += 1
    pause 0.01    
ma "And it's over for poor Chief Lena who'll never fall back on her legs again after that mighty blow..."
play sound "Sounds/winner.mp3"
window hide
scene fightrubywin with dissolve
show winnersign at streetfight02
$ renpy.pause(1, hard=True)
ma "And so Ruby wins tonight's fight!" 
play music "Sounds/applause.mp3"
$ renpy.pause(1, hard=True)
hide winnersign 
hide screen screenfightlenaruby
stop music
jump RubyGallery

label RubyGallery04:
scene gym03
show rubygym01
ru "Hi there big man. Wanna see me lift this super-heavy barbell?"
mc "Fine. Go ahead."
hide rubygym01
scene gym03
show nextidle
play music "Sounds/womangroan.mp3"
call screen rubygymbellx
screen rubygymbellx:
    add rubygymbell at center
    modal True
    button:
        xpos .91
        ypos .44
        xysize(140, 80)        
        action Jump ("RubyGymWorkoutEndx")        
label RubyGymWorkoutEndx:
stop music
scene gym03
show rubygym02
ru "Enjoyed watching the show big man? Do you think you can power-lift as much as me?"
mc "Of course, I'm more muscular and stronger than you!"
hide rubygym02
show rubygym03
ru "Oh yeah, you think so?"
hide rubygym03
show rubygym04
ru "You really think you can compare to this body?"
mc "Well, obviously, my tits are smaller..."
hide rubygym04
show rubygym05
ru "I'm talking about my chorded musculature...."
mc "Yeah I'm sure and I'll prove it! I'll pick the heaviest set of weights to show you what I'm made of..."
hide rubygym05
show rubygym01
ru "Let's see you in action then big man. See if you've got enough spunk in you to be a true Road Warrior."
hide rubygym01    
jump RubyGallery

label RubyGallery05:
play sound "Sounds/dream.mp3"
scene locker03dream
show rubyshower01
play music "Sounds/showerstrip.mp3"
ru "Well, what do we have here? A teen muscle stud with a giant hard cock!"
mc "That's right Ruby, ALL my muscles are HUGE and HARD!"
hide rubyshower01    
show rubyshower02
ru "I can see that [name]. Never seen someone as buff as you. My pussy is all tingly."
mc "Then we should remedy this tingling sensation and replace it with a HARD POUNDING one."
hide rubyshower02    
show rubyshower03                                            
ru "I like your way of thinking. Fuck me HARD then, as HARD as you can! Just like it says right here on my butt..."
mc "I don't need to be asked twice!"
hide rubyshower03
scene locker03 blurred
show rubyshower04
ru "I'm sure a young virile monstercock like yours can handle my fit muscled body and HUGE tits!"
mc "Of course Ruby! I'll lift you up in my strong arms and impale you on my GIANT manmeat!"
scene lockerrubyfuck00 with dissolve
ru "Damn, this is the biggest and hardest fuckstick I've ever had the pleasure of handling..."
mc "It's ROCK-HARD to better SMASH your pussy Ruby!"    
ru "Show me how STRONG and POWERFUL you are [name]!"
scene lockerrubyfuck01 with dissolve
ru "Your monster cock is pounding the shit out of my poor pussy, I LOVE IT! Fuck me HARDER!"
scene lockerrubyfuck01a with dissolve
mc "I like women who can take it like you, I'll fucking DESTROY your pussy and make it mine forever!"
call screen rubygymdream02x
screen rubygymdream02x:
    add dreamrubygym02 at center
    modal True
    button:
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("DreamRubyGymEnd02x")    
label DreamRubyGymEnd02x:
ru "AAAH, ooh! YES, YES! Give it to me [name], I want ALL of it!"
mc "You want more huh? You want more of that monster teen cock hey?"
ru "YES, SMASH my pussy! FASTER!"
call screen rubygymdreamx
screen rubygymdreamx:
    add dreamrubygym at center
    modal True
    button:
        imagebutton:
            focus_mask True
            idle "Icons/nextidle.png"
            hover "Icons/nexthover.png"
            action Jump ("DreamRubyGymEndx")    
label DreamRubyGymEndx:
mc "Let's switch position, lean against the shower wall..." 
scene lockerrubyfuck02 with dissolve
ru "That dick is just so good, ssooo fucking good. Kiss me while you take me [name]..."
scene lockerrubyfuck03 with dissolve
play sound "Sounds/kiss.mp3"
ru "And you're a great kisser too. What a TOTAL STUD! Fuck me some more please! HARDER, make me COME!"
scene lockerrubyfuck02 with dissolve    
ru "I'm cumming, shit, I'm cumming so hard with your cock ssoo DEEP inside me, AAAAH!"
mc "I'm gonna cum too! Your belly will swell with my mighty cumload! RHHHHAAAA!"
scene lockerrubyfuck04 with dissolve
ru "Fuck, you're filling me up like a spermtank with your MASSIVE loads!"
mc "Fuck yeah! I've got tons more creamy sauce to feed your hungry hole Ruby!"
ru "AAAH, what a TORRENT of young virile spunk!"
stop music
play music "Sounds/shower.mp3"
scene lockermccum01 with dissolve
mc "Yeah, feel my jets of spunk inside you Ruby! AAAH!"    
scene lockermccum02 with dissolve
mc "Damn, I made a right dreamy mess. I'd better clean all of it before I leave or people will think I'm a total pervert. Which I definitely AM NOT."
jump RubyGallery

label RubyGallery06:
play music "v07/datemusic.mp3"
scene bedroom01
show ruby01
ru "So, you're ready to fuck a MUSCLE BABE I gather?"
mc "Indeed. Pumped up and raring to go!"
hide ruby01
show ruby04
ru "And I suppose you want me to change into something more suitable?"
mc "That would be appropriate, although I'd fuck you right here right now the way you are."
ru "My pants are made of reinforced kevlar so that would be hard, muscle boy... Wait for me, I'll be back in a sec..."
mc "Alright, I can't wait to see you in some sexy lingerie."
scene bedroom01 with fade
show rubylingerie01 at center with moveinright
ru "Now that's better, don't you think [name]?"
mc "I like how your huge boobs stretch against that corset Ruby."
hide rubylingerie01
show rubylingerie02
with fastdissolve
ru "You're a filthy boy. I bet you get a huge hardon every time you see a REAL woman with BIG FIRM TITS, hey?"
mc "I can't deny this. But I'm also an ass-man, so why don't you turn round for me Ruby?"
hide rubylingerie02
show rubylingerie03
with fastdissolve
ru "You're lucky I'm in your harem. I would have punched your fucking face in for being so rude if not..."
mc "Being a harem master does have its rewards..."
scene bedroom01 blurred with fastdissolve
show rubylingeriearse
ru "Don't get too cocky, big boy. I could CRUSH your manhood with my firm buttcheeks."
mc "I see... They sure look muscular enough to do just that..."
scene bedroom01
show rubylingerie04
with fastdissolve
ru "And my ALPHA-RACK could do some SERIOUS damage to any boy who doesn't show me the respect I deserve! Wanna see?"
mc "I do! That is, if you allow me to, of course..."
hide rubylingerie04
show rubylingerie05
with fastdissolve
ru "What a gentleman. There you are then, big boy. Just for YOU!"
mc "You are a true ALPHA-GODDESS Ruby!"
ru "I like it when a MAN speaks to me like that..."
ru "My pussy is so wet... I can't wait to get fucked by a muscled STUD like YOU!"
mc "I'll get into something more comfortable then... A XXXL-sized bodybuilder pouch."
ru "Mmmh, that sounds... DELICIOUS!"
scene mcbedroomruby01 with dissolve
ru "Oh my... That's a VERY BIG package for me [name]."
mc "And I ain't even hard yet Ruby..."
ru "Really? Then I want you to slowly FILL UP that shaft with blood until it DISTENDS that poor posing pouch to its limits!"
scene mcbedroomruby02 with dissolve
mc "Watch it grow Ruby... Feast your eyes on my MASSIVE bulge as it grows BIGGER AND BIGGER!"
ru "Nice... GO on, I want that cock FULLY ENGORGED!"
scene mcbedroomruby03 with dissolve
mc "I'll get there in no time for your hot bod, don't worry."
ru "Mmh, you sure know how to speak to real women... cos real women LOVE HUGE HARD DONGS!"
scene mcbedroomruby04 with dissolve
ru "I can't wait any longer, I NEED to feel that MONSTER BULGE!"
mc "Tha's it, rub your hands against it and feel it GROW Ruby!"
ru "It's the BIGGEST fucking cock I've ever felt up... I want to see it now, let me pull this pouch down before you TEAR IT APART!"
scene mcbedroomruby05 with dissolve
ru "I can feel every engorged vein on that shaft with my feet..."
mc "And I can feel your feet rubbing against my obymeat! Wow, it's so good!"
ru "You ain't seen nothing yet big boy..."
scene mcbedroomruby06 with dissolve
scene mcbedroomruby05 with dissolve
scene mcbedroomruby06 with dissolve
scene mcbedroomruby05 with dissolve
scene mcbedroomruby06 with dissolve
scene mcbedroomruby05 with dissolve
scene mcbedroomruby06 with dissolve
scene mcbedroomruby05 with dissolve
scene mcbedroomruby06 with dissolve
scene mcbedroomruby05 with dissolve
scene mcbedroomruby06 with dissolve
scene mcbedroomruby05 with dissolve
scene mcbedroomruby06 with dissolve
scene mcbedroomruby05 with dissolve
scene mcbedroomruby06 with dissolve
scene mcbedroomruby05 with dissolve
ru "Now I can feel those veins almost POPPING!"
mc "That's cos I'm ready to EXPLODE!"
ru "Then do it, cover me in your sticky spunk [name]!"
scene mcbedroomruby07 with dissolve
mc "FUUUUCK!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
ru "What a MONSTER SHOT OF CUM! YES! COVER MY BODY WITH IT!"
scene mcbedroomruby08 with dissolve
mc "FUUUUCK!"
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
ru "Damn big boy, you made a REAL CUM MESS of me, didn't you?"
mc "Not messy enough to my taste. I say let's move on to the main course. On my bed..."
ru "I LOVE how that MASSIVE LOAD didn't even put a dent in your ROCK-HARDNESS!"
stop music
jump RubyGallery

label RubyGallery07:
 scene bedroom01 with fade
show rubylingerie05
ru "I'm fucking ready big boy. My pussy is soaking wet and tingling."
mc "And I'm now ROCKHARD and ready too!"
ru "Show me that you deserve this HOT BOD. Let's see what you have in store for me..."   
label RubyFuckChoicex:
stop music
menu:
    "Your lips were made for my huge cock. Get to work Ruby.":
        ru "And it does look very tasty indeed..."
        jump RubyBlowx
    "I want to see your face while I pound that muscled pussy...":
        jump RubyPinx    
    "I'l show how strong I am by impaling you on my mighty shaft!":
        ru "Oooh, that sounds... ATHLETIC! Just like I like it..."
        jump RubyImpalex
    "Your ass needs some nice pounding.":
        ru "You'd better make it a VERY GOOD POUNDING then!"
        jump RubyArsex
    "I'm done with this gallery.":
        jump RubyGallery
        
label RubyBlowx:
scene bedroom27 with dissolve
show rubypreblow01
ru "Let me lick those balls... I want a MONSTER load to churn in them."
mc "I always deliver MASSIVE loads of virile spunk to my harem girls..."
ru "But I want and DESERVE the BIGGEST one!"
mc "Sure baby..."
hide rubypreblow01
show rubypreblow02
ru "Agreed? You're going to give me the BIGGEST LOAD OF CUM EVER, stud?"
play sound "Sounds/kiss.mp3"
mc "You ask so politely, how could I refuse..."
ru "Let me get to work on that lovepole then... I'm going to SWALLOW IT WHOLE!"
scene bedroom19 blurred
play music "Sounds/hardsucking.mp3"
label RubyBlowSlowx:
hide rubyblowfast
show rubyblowslow
call screen rubyblowslow01x
screen rubyblowslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("RubyBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("RubyBlowFastx") 

label RubyBlowFastx:
mc "Damn! You're a real pro Ruby! But work those throat muscles FASTER!"
hide rubyblowslow
show rubyblowfast
call screen rubyblowfast01x
screen rubyblowfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("RubyBlowEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("RubyBlowSlowx") 

label RubyBlowEndx:
mc "That's it, I'm gonna fill your stomach with a meal and half of RICH, CREAMY, BALL-BATTER!"
stop music
hide rubyblowslow
hide rubyblowfast
show rubyblowanim00
show rubyblowcum01
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "I'm coming, RHAAAA!"
ru "Gllrrbbb!"
hide rubyblowcum01
hide rubyblowanim00
show rubyblowcum02
with dissolve
mc "Good girl, all the way down your throat while I dump my virile seed! FUCK YEAH!"
hide rubyblowcum02
show rubyblowcum03
with dissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
ru "I need to see this GEYSER of spunk!"
mc "Take those jets, you muscled cum-warrior!"
ru "YES! RUIN my face with your goo!"
scene bedroom08 blurred
show rubyblowcum04
with dissolve
play sound "Sounds/biggest.mp3"
ru "Thank you for giving me the biggest load of cum EVER!"
mc "You'd better get cleaned up because I have MORE LOADS in my cum factories for you!"
stop sound
ru "Really? So what's next, big boy?"
jump RubyFuckChoicex
    
label RubyPinx:
scene bedroom10 blurred
show rubyprepin00
with dissolve
ru "You think you can handle this pussy?"
mc "Let me have a closer look..."
scene bedroom25 blurred
show rubyprepin01
with fastdissolve
mc "Fuck, your clit is HUGE!"
ru "All the better to rub against your shaft and make it explode that sweet young cum deep inside me!"
play sound "Sounds/sucking.mp3"
hide rubyprepin01
show rubyprepin02
ru "Ooh, my clit is sssoo sensitive, I'm dying for a good pounding!"
mc "Alright, you asked for it. I'm going to pound you so hard, your clit will swell until it's scalding with lust!"
ru "Oooh, let's see what you've got then, big boy!"
scene bedroom09 blurred
play music "Sounds/fucksound.mp3"
scene bedroom19 blurred
label RubyPinSlowx:
hide rubypinfast
show rubypinslow
call screen rubypinslow01x
screen rubypinslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("RubyPinEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("RubyPinFastx") 

label RubyPinFastx:
ru "Fuck, FUCK FUCK FUCK! I'm cumming HARD on that MONSTERCOCK! Fuck me even HARDER please [name]!"
hide rubypinslow
show rubypinfast
call screen rubypinfast01x
screen rubypinfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("RubyPinEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("RubyPinSlowx") 

label RubyPinEndx:
mc "My balls are ready for launching!"
ru "Fire those cum-missiles and fill me up, big boy!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene bedroom19 blurred
show rubypincum01
with fastdissolve  
mc "AAAH! CUMMMINNGGGG!"
ru "Blast that spunk all over me now!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
scene bedroom28 blurred
show rubypincum02
with fastdissolve  
mc "Here, take that nut-juice in your face Ruby!"
ru "You're such a filthy boy, but I LOVE IT!"
scene bedroom29 blurred
show rubypincum03
with fastdissolve 
ru "Oh my God, your cock is STILL hard???"    
mc "I'm not done yet with that cum-filled pussy of yours! Turn around and get on the edge of the bed!"
ru "And my pussy isn't done yet with that young meatpole of yours! SMASH IT, POUND IT, FUCKING DESTROY IT!"
scene bedroom23 blurred
show rubyprepussy01
with fastdissolve  
mc "There, the tip is in... The rest will follow in due course."
ru "Oh my God, my pussy is ssoo tiny compared to your MASSIVE cock!"
play music "Sounds/fucksound.mp3"
hide rubyprepussy01
label RubyPoundSlowx:
hide rubypussyfast
show rubypussyslow
call screen rubypoundslow01x
screen rubypoundslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("RubyPoundEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("RubyPoundFastx") 

label RubyPoundFastx:
ru "Give me MORE big boy!"
hide rubypussyslow
show rubypussyfast
call screen rubypoundfast01x
screen rubypoundfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("RubyPoundEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("RubyPoundSlowx") 

label RubyPoundEndx:
mc "Another MEGA-LOAD of cum churning up in my balls RIGHT NOW!"
ru "Then dump it in my overstuffed fuckhole [name]! Use it as your cum-dump!"
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene bedroom23 blurred
show rubypussycum01 with fastdissolve
mc "Here it comes, get ready for a second filling, RHAAAA!"
ru "Fuck, I LOVE how you can just SPEW your sauce NON-STOP!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
hide rubypussycum01
show rubypussycum02
mc "More nut-juice for you Ruby! AAAH!"
ru "Re-cover me in your HOT SPUNK [name]!"
scene bedroom20 blurred
show rubypussycum03
with fastdissolve
mc "That's the last of it. For now."
ru "I'm.... like, TOTALLY DRENCHED IN CUM! And it's ssoo tasty..."
mc "And there's more in store for you. Clean yourself up and let's move on."
ru "What do you have in mind, big boy?"
jump RubyFuckChoicex
    
label RubyArsex:
scene bedroom08 with dissolve
show rubyprearse01
ru "Let me adjust my sphincter muscles for that great big invader..."
ru "You ain't hurting me, big boy. Ruby can take it and I'll prove it to you!"
scene bedroom26 blurred with dissolve
play music "Sounds/fucksound.mp3"
label RubyArseSlowx:
scene bedroom26 blurred
show rubyarseslow
call screen rubyarseslow01x
screen rubyarseslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("RubyArseEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("RubyArseFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("RubyArsePOVSlowx") 

label RubyArseFastx:
ru "Come on, that's all you've got? Fuck my ass FASTER!"
label RubyArseFastbx:
scene bedroom26 blurred
show rubyarsefast
call screen rubyarsefast01x
screen rubyarsefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("RubyArseEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("RubyArseSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/povview.png"
        hover "Icons/povview.png"
        action Jump ("RubyArsePOVFastbx") 

label RubyArsePOVSlowx:
scene bedroom08 blurred
show rubyarsepovslow
call screen rubyarsepovslow01x
screen rubyarsepovslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("RubyArseEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("RubyArsePOVFastx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("RubyArseSlowx") 

label RubyArsePOVFastx:
ru "Come on, that's all you've got? Fuck my ass FASTER!"
label RubyArsePOVFastbx:
scene bedroom08 blurred
show rubyarsepovfast
call screen rubyarsepovfast01x
screen rubyarsepovfast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("RubyArseEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("RubyArsePOVSlowx") 
    imagebutton:
        focus_mask True
        idle "Icons/sceneview.png"
        hover "Icons/sceneview.png"
        action Jump ("RubyArseFastbx") 

label RubyArseEndx:
ru "Now fill me up with cum! Make my ass slippery with ounces of your viscous ball-batter!"
stop music
scene bedroom08 blurred
show rubyarsecum01
with fastdissolve
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
mc "You asked for it, here it comes, AAAAH!"
ru "Yes, yes, YES! I can feel my guts bloating up with your MONSTER LOAD!"
hide rubyarsecum01
show rubyarsecum02
ru "I'm taking charge now, blow your load DEEEEP inside me! Aaah, I'm cumming too!!!"
ru "Damn girl, you're clenching your glutes so tight, FUCK!"
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
scene bedroom27 blurred
show rubyarsecum03
with dissolve
mc "Take some more shots on your back, feel the power of my jets Ruby!"
ru "I feel it, you're a true ALPHA-STUD [name]!"
hide rubyarsecum03
show rubyarsecum04
with dissolve
mc "That was INTENSE... Phew..."
ru "Your balls must be empty now, you nutted so much cum... Both inside my ass and all over my body."
mc "Nope. I've got unlimited supplies in there, go get ready for some more hot musclestud-fucking!"
ru "Really? So what's next then, big boy?"
jump RubyFuckChoicex

label RubyImpalex:
scene bedroom13 with dissolve
show rubypreimpale01
ru "You want to impale me with this thing, hey?"
mc "That's right. I'll lift you up with my strong arms and make you bounce up and down my fat truncheon!"
hide rubypreimpale01
show rubypreimpale02
with fastdissolve
ru "Let's see first it this boymeat is strong enough to handle MY body, shall we?"
mc "What do you have in mind?"
ru "I want you to lift me up with it! Show me how STRONG and POWERFUL your teenage fuckstick truly is!"
hide rubypreimpale02
show rubypreimpale03
with fastdissolve
ru "I can feel my feet leaving the floor... Carry me on your GIANT DICK [name]!"
mc "*groan* I'll show you Ruby, watch THIS!"
hide rubypreimpale03
show rubypreimpale04
with fastdissolve
ru "Mmmh, yes, my whole muscle weight resting on a MONSTER shaft, just like I like it..."
mc "Turn round, the Glorglans will want to see that!"
ru "The what???"
mc "Err... Forget I said it. But turn round, still."
hide rubypreimpale04
show rubyimpale00
with fastdissolve
mc "Ready? There's an awful lot more inches to go..."
ru "I don't care, I can take it, just fucking do it, IMPALE ME ON THAT DONG!"
play music "Sounds/fucksound.mp3"
scene bedroom13 blurred
label RubyImpaleSlowx:
hide rubyimpalefast
show rubyimpaleslow
call screen rubyimpaleslow01x
screen rubyimpaleslow01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("RubyImpaleEndx")
    imagebutton:
        focus_mask True
        idle "Icons/fasteridle.png"
        hover "Icons/fasterhover.png"
        action Jump ("RubyImpaleFastx") 

label RubyImpaleFastx:
ru "SMASH that pussy! Really give it all you've got, STUD!"
hide rubyimpaleslow
show rubyimpalefast
call screen rubyimpalefast01x
screen rubyimpalefast01x:
    modal True
    imagebutton:
        focus_mask True
        idle "Icons/nextidle.png"
        hover "Icons/nexthover.png"
        action Jump ("RubyImpaleEndx")
    imagebutton:
        focus_mask True
        idle "Icons/sloweridle.png"
        hover "Icons/slowerhover.png"
        action Jump ("RubyImpaleSlowx") 

label RubyImpaleEndx:
mc "DUMPING MY LOAD ANYTIME NOW!"
hide rubyimpaleslow
hide rubyimpalefast
stop music
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
scene bedroom10 blurred
show rubyimpalecum01
ru "I can feel it! MASSIVE PELLETS of cum thundering through my fuckhole!"
mc "Goddamn right, I'm EXPLODING like a volcano! RHAAA!"
stop sound
if persistent.cumsoundon:
    play sound "Sounds/cumming.mp3"
hide rubyimpalecum01
show rubyimpalecum02
ru "Pull out your CUM-CANNON and fire those shots ON me! I want some more hot boycream!"
mc "Sure, I've got plenty left for your cum-hungry muscled bod! AAAH!"
hide rubyimpalecum01
show rubyimpalecum02
if persistent.cumsoundon:
    play sound "Sounds/mccum.mp3"
ru "What a GIANT load again! Aim it higher, I want to be PLASTERED in it!"
hide rubyimpalecum02
show rubyimpalecum03
mc "There you go! RHAAA!"
ru "Mmmh, so,so much young sweet cum!"
scene bedroom24 blurred
show rubyimpalecum04
with dissolve
mc "Phew... I think I'm done. For now."
ru "Am I going to finally have a respite from your BEHEMOTH?"
mc "Nope. My cock is still hard and ready."
ru "You're a fucking SEX-MACHINE [name]! So, what next, big boy?"
jump RubyFuckChoicex