label TaraGallery:
call screen gallerytara
screen gallerytara:
    add "Gallery/taragallery.jpg"
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("gallerytara"), Jump ("MainGallery")]

    if renpy.seen_image("tarapanties03"):
        imagebutton:
            focus_mask True
            idle "Gallery/rachelgallery01.png" xpos 621 ypos 100
            hover "Gallery/rachelgallery01.png"
            action Jump ("TaraGallery01")

    if renpy.seen_image("tarapanties03") == False:
        imagebutton:
            focus_mask True
            idle "Gallery/gallerylocked.png" xpos 621 ypos 100
            hover "Gallery/gallerylocked.png"
            action Jump ("TaraGallery")

    add "Gallery/galleryfuture.png" xpos 1050 ypos 100
            
    add "Gallery/galleryfuture.png" xpos 1478 ypos 100

    add "Gallery/galleryfuture.png" xpos 621 ypos 400

    add "Gallery/galleryfuture.png" xpos 1050 ypos 400

    add "Gallery/galleryfuture.png" xpos 1478 ypos 400

    add "Gallery/galleryfuture.png" xpos 621 ypos 700

    add "Gallery/galleryfuture.png" xpos 621 ypos 700

    add "Gallery/galleryfuture.png" xpos 1050 ypos 700

    add "Gallery/galleryfuture.png" xpos 1478 ypos 700

    add "Gallery/gallerygrid02.png"
    add "Gallery/texttara.png"

label TaraGallery01:
scene medbay03
show rachel03
ra "I hope you can get that monster cock hard despite your injury [name]..."
mc "Don't worry about me nurse Rachel, get your kit off and I'll get rock-hard in no time!"
hide rachel03
show rachel07
with fastdissolve
ra "Ta-da! Have you ever seen such HUGE boobies [name]?"
mc "No... They are the biggest around for sure!"
hide rachel07
show rachel08
with fastdissolve
ra "And what about my bubble butt? Do you like it?"
mc "My cock says yes!"
ra "Then, remove that bedsheet and show me!"
scene medbay03 with hpunch
show rachel08
ta "What the hell is going on here? RACHEL, I've been waiting for you for our BDSM session!"
hide rachel08
show rachel09
ra "Uh Uh, I think I'm in BIG trouble!"
show tarapanties01 at midleft with moveinleft
show rachel09 at midright with move
ta "Do you care to explain why you are standing here NAKED in front of this injured patient?"
hide rachel09
show rachel10 at midright
ra "The poor boy needs some stimulation! That way he'll recover more quickly, right?"
hide tarapanties01
show tarapanties02 at midleft
ta "That is the lamest excuse I've heard from you yet. That's it, you need to get punished!"
hide tarapanties02
hide rachel10
show tarapanties03
with dissolve
ra "Prepare to receive your due correction!"
hide tarapanties03
show tarapanties03b
with dissolve
play sound "Sounds/slap.mp3"
ta "Take that, you dirty whore!"
ra "Ouch! She's really giving it to my poor little buttcheek!"
hide tarapanties03b
show tarapanties03
with dissolve
ta "Watch boy, this is the treatment reserved for unfaithful harem girls!"
hide tarapanties03
show tarapanties03c
with dissolve
play sound "Sounds/slap.mp3"
ta "And that, stupid bimbo!"
ra "Ooh, it hurts but I deserve it, I've been so naughty doctor Tara!"
hide tarapanties03c
show nextidle
call screen rachelslapy
screen rachelslapy:
    add rachelslap at center
    modal True
    button:
        xpos .91
        ypos .44
        xysize(140, 80)        
        action Jump ("RachelSlapEndy")    
label RachelSlapEndy:
hide nextidle
show tarapanties04 with dissolve
ra "Did you see? She felt the PAIN of being an untrustworthy bitch! She suffered for it."
mc "I don't think so. She clearly enjoyed it."
ra "My poor buttcheeks, I'm gonna get a right good pounding in my poopy chute now for sure!"
hide tarapanties04
show tarapanties05
with fastdissolve
ta "That's correct, and since you seem to love BIG cocks, it will be my twelve-inch strap-on dildo this time!"
ra "Oh no! It's sssoo big, it's gonna hurt me a LOT!"
mc "Perhaps you could use MY cock instead? It's even bigger so it will hurt more."
ta "No thanks! Men are NOT ALLOWED where we're going! Now go back to sleep and stop being a nuisance patient [name]!"
mc "Right-ee-o Doc."
jump TaraGallery



