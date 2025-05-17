# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    def show_gallery_menu():
        renpy.call_in_new_context("MainGallery")
    config.keymap["open_gallery_menu"] = ["c"]
    
    # When key is pressed at anytime, open custom screen.
    config.underlay.append(renpy.Keymap(open_gallery_menu=show_gallery_menu))
init python:
    def show_inventory_menu():
        renpy.call_in_new_context("InventoryGallery")
    config.keymap["open_inventory_menu"] = ["i"]

    def show_mccumsound_menu():
        renpy.call_in_new_context("Mccumsound")
    config.keymap["open_mccumsound_menu"] = ["b"]

    def show_tipsmenu_menu():
        renpy.call_in_new_context("TipsMenu")
    config.keymap["open_tipsmenu_menu"] = ["t"]

    # When key is pressed at anytime, open custom screen.
    config.underlay.append(renpy.Keymap(open_inventory_menu=show_inventory_menu))
    config.underlay.append(renpy.Keymap(open_mccumsound_menu=show_mccumsound_menu))
    config.underlay.append(renpy.Keymap(open_tipsmenu_menu=show_tipsmenu_menu))
    define.move_transitions("movefast", 0.1)
init python:
    renpy.music.register_channel("channel1", loop=True)
    renpy.music.register_channel("channel2", loop=True)

init:

    define flash  = Fade(.25, 0.0, .5, color="#fff")
    define fastflash  = Fade(.2, 0.0, .3, color="#fff")
    style say_dialogue2:
        size 40
        font "gui/Boogaloo-Regular.ttf"
        xpos 300
        ypos 40
        xmaximum 1500
        bold False
        color "#e2edff"
        justify True
        line_spacing 2

    style say_dialogue1:
        size 40
        font "gui/Boogaloo-Regular.ttf"
        xpos 300
        ypos 40
        xmaximum 1500
        bold False
        color "#feedff"
        justify True
        line_spacing 2

    style statsCommon is default:
        outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)]
        font "Gui/goodtimes.ttf"

    style statsMain is statsCommon:
        size 25
        color "#1c73ff"

    style statsPhysical is statsCommon:
        size 35
        color "#ff0000"

    image gwendebrasexslow:
        "Science/gwendebrafuck00.png"
        pause 0.06
        "Science/gwendebrafuck01.png"
        pause 0.06
        "Science/gwendebrafuck02.png"
        pause 0.06
        "Science/gwendebrafuck03.png"
        pause 0.06
        "Science/gwendebrafuck04.png"
        pause 0.06
        "Science/gwendebrafuck05.png"
        pause 0.06
        "Science/gwendebrafuck06.png"
        pause 0.06
        "Science/gwendebrafuck07.png"
        pause 0.06
        "Science/gwendebrafuck08.png"
        pause 0.06
        "Science/gwendebrafuck07.png"
        pause 0.06
        "Science/gwendebrafuck06.png"
        pause 0.06
        "Science/gwendebrafuck05.png"
        pause 0.06
        "Science/gwendebrafuck04.png"
        pause 0.06
        "Science/gwendebrafuck03.png"
        pause 0.06
        "Science/gwendebrafuck02.png"
        pause 0.06
        "Science/gwendebrafuck01.png"
        pause 0.06
        repeat

    image gwendebrasexfast:
        "Science/gwendebrafuck00.png"
        pause 0.04
        "Science/gwendebrafuck01.png"
        pause 0.04
        "Science/gwendebrafuck02.png"
        pause 0.04
        "Science/gwendebrafuck03.png"
        pause 0.04
        "Science/gwendebrafuck04.png"
        pause 0.04
        "Science/gwendebrafuck05.png"
        pause 0.04
        "Science/gwendebrafuck06.png"
        pause 0.04
        "Science/gwendebrafuck07.png"
        pause 0.04
        "Science/gwendebrafuck08.png"
        pause 0.04
        "Science/gwendebrafuck07.png"
        pause 0.04
        "Science/gwendebrafuck06.png"
        pause 0.04
        "Science/gwendebrafuck05.png"
        pause 0.04
        "Science/gwendebrafuck04.png"
        pause 0.04
        "Science/gwendebrafuck03.png"
        pause 0.04
        "Science/gwendebrafuck02.png"
        pause 0.04
        "Science/gwendebrafuck01.png"
        pause 0.04
        repeat
            
    image francinesex01:
        "School/francine101.png"
        pause 0.04
        "School/francine102.png"
        pause 0.04
        "School/francine103.png"
        pause 0.04
        "School/francine104.png"
        pause 0.04
        "School/francine105.png"
        pause 0.04
        "School/francine106.png"
        pause 0.04
        "School/francine107.png"
        pause 0.04
        "School/francine108.png"
        pause 0.04
        "School/francine109.png"
        pause 0.04
        "School/francine110.png"
        pause 0.08
        "School/francine109.png"
        pause 0.06
        "School/francine108.png"
        pause 0.06
        "School/francine107.png"
        pause 0.06
        "School/francine106.png"
        pause 0.06
        "School/francine105.png"
        pause 0.06
        "School/francine104.png"
        pause 0.06
        "School/francine103.png"
        pause 0.06
        "School/francine102.png"
        pause 0.06
        repeat

    image francinesex02:
        "School/francine101.png"
        pause 0.03
        "School/francine102.png"
        pause 0.03
        "School/francine103.png"
        pause 0.03
        "School/francine104.png"
        pause 0.03
        "School/francine105.png"
        pause 0.03
        "School/francine106.png"
        pause 0.03
        "School/francine107.png"
        pause 0.03
        "School/francine108.png"
        pause 0.03
        "School/francine109.png"
        pause 0.03
        "School/francine110.png"
        pause 0.06
        "School/francine109.png"
        pause 0.04
        "School/francine108.png"
        pause 0.04
        "School/francine107.png"
        pause 0.04
        "School/francine106.png"
        pause 0.04
        "School/francine105.png"
        pause 0.04
        "School/francine104.png"
        pause 0.04
        "School/francine103.png"
        pause 0.04
        "School/francine102.png"
        pause 0.04
        repeat

    image francinesex02b:
        "School/francine101.png"
        pause 0.04
        "School/francine102.png"
        pause 0.04
        "School/francine103.png"
        pause 0.04
        "School/francine104.png"
        pause 0.04
        "School/francine105.png"
        pause 0.04
        "School/francine106.png"
        pause 0.04
        "School/francine107.png"
        pause 0.04
        "School/francine108.png"
        pause 0.08
        "School/francine107.png"
        pause 0.06
        "School/francine106.png"
        pause 0.06
        "School/francine105.png"
        pause 0.06
        "School/francine104.png"
        pause 0.06
        "School/francine103.png"
        pause 0.06
        "School/francine102.png"
        pause 0.06
        repeat

    image francinesex01b:
        "School/francine101.png"
        pause 0.08
        "School/francine102.png"
        pause 0.08
        "School/francine103.png"
        pause 0.08
        "School/francine104.png"
        pause 0.08
        "School/francine105.png"
        pause 0.08
        "School/francine106.png"
        pause 0.08
        "School/francine107.png"
        pause 0.08
        "School/francine108.png"
        pause 0.16
        "School/francine107.png"
        pause 0.12
        "School/francine106.png"
        pause 0.12
        "School/francine105.png"
        pause 0.12
        "School/francine104.png"
        pause 0.12
        "School/francine103.png"
        pause 0.12
        "School/francine102.png"
        pause 0.12
        repeat

    image dancingangie01:
        "angiedancing01c" with fastdissolve
        pause 0.7
        "angiedancing01bc"
        pause 1.0
        "angiedancing02c" with fastdissolve
        pause 1.1
        "angiedancing02bc"
        pause 0.9
        "angiedancing03c" with fastdissolve
        pause 1.0
        "angiedancing03bc"
        pause 1.0
        "angiedancing04c" with fastdissolve
        pause 1.0
        "angiedancing04bc"
        pause 0.5
        repeat

    image dancingangie02:        
        "angiedancing01c" with fastdissolve
        pause 0.6
        "angiedancing01bc"
        pause .4
        "angiedancing02c" with fastdissolve
        pause .8
        "angiedancing02bc"
        pause 0.8
        "angiedancing03c" with fastdissolve
        pause .8
        "angiedancing03bc"
        pause .8
        "angiedancing04c" with fastdissolve
        pause .8
        "angiedancing04bc"
        pause .4
        "angiedancing02c" with fastdissolve
        pause .4
        "angiedancing02bc"
        pause 0.4
        repeat

    image dancingcyrl01:
        "Dancing/cyrldancing01.png" with fastdissolve
        pause 0.7
        "Dancing/cyrldancing01b.png"
        pause 1.0
        "Dancing/cyrldancing02.png" with fastdissolve
        pause 1.1
        "Dancing/cyrldancing02b.png"
        pause 0.9
        "Dancing/cyrldancing03.png" with fastdissolve
        pause 1.0
        "Dancing/cyrldancing03b.png"
        pause 1.0
        "Dancing/cyrldancing04.png" with fastdissolve
        pause 1.0
        "Dancing/cyrldancing04b.png"
        pause .5
        repeat
        
    image dancingcyrl02:
        "Dancing/cyrldancing01.png" with fastdissolve
        pause 0.6
        "Dancing/cyrldancing01b.png"
        pause .4
        "Dancing/cyrldancing02.png" with fastdissolve
        pause .8
        "Dancing/cyrldancing02b.png"
        pause 0.8
        "Dancing/cyrldancing03.png" with fastdissolve
        pause .8
        "Dancing/cyrldancing03b.png"
        pause .8
        "Dancing/cyrldancing04.png" with fastdissolve
        pause .8
        "Dancing/cyrldancing04b.png"
        pause .4
        "Dancing/cyrldancing02.png" with fastdissolve
        pause .4
        "Dancing/cyrldancing02b.png"
        pause .4
        repeat
        
    image dancingayla01:
        "ayladancing01c" with fastdissolve
        pause .7
        "ayladancing01bc"
        pause 1.0
        "ayladancing02c" with fastdissolve
        pause 1.1
        "ayladancing02bc"
        pause .9
        "ayladancing03c" with fastdissolve
        pause 1.0
        "ayladancing03bc"
        pause 1.0
        "ayladancing04c" with fastdissolve
        pause 1.0
        "ayladancing04bc"
        pause .5
        repeat

    image dancingayla02:
        "ayladancing01c" with fastdissolve
        pause 0.6
        "ayladancing01bc"
        pause .4
        "ayladancing02c" with fastdissolve
        pause .8
        "ayladancing02bc"
        pause 0.8
        "ayladancing03c" with fastdissolve
        pause .8
        "ayladancing03bc"
        pause .8
        "ayladancing04c" with fastdissolve
        pause .8
        "ayladancing04bc"
        pause .4
        "ayladancing02c" with fastdissolve
        pause .4
        "ayladancing02bc"
        pause .4
        repeat

    image dancingmichiko01:
        "Dancing/michikodancing01.png" with fastdissolve
        pause .7
        "Dancing/michikodancing01b.png"
        pause 1.0
        "Dancing/michikodancing02.png" with fastdissolve
        pause 1.1
        "Dancing/michikodancing02b.png"
        pause .9
        "Dancing/michikodancing03.png" with fastdissolve
        pause 1.0
        "Dancing/michikodancing03b.png"
        pause 1.0
        "Dancing/michikodancing04.png" with fastdissolve
        pause 1.0
        "Dancing/michikodancing04b.png"
        pause .5
        repeat

    image dancingmichiko02:
        "Dancing/michikodancing01.png" with fastdissolve
        pause 0.6
        "Dancing/michikodancing01b.png"
        pause .4
        "Dancing/michikodancing02.png" with fastdissolve
        pause .8
        "Dancing/michikodancing02b.png"
        pause .8
        "Dancing/michikodancing03.png" with fastdissolve
        pause .8
        "Dancing/michikodancing03b.png"
        pause .8
        "Dancing/michikodancing04.png" with fastdissolve
        pause .8
        "Dancing/michikodancing04b.png"
        pause .4
        "Dancing/michikodancing02.png" with fastdissolve
        pause .4
        "Dancing/michikodancing02b.png"
        pause .4
        repeat

    image dancingbella01:
        "Dancing/belladancing01.png" with fastdissolve
        pause .7
        "Dancing/belladancing01b.png"
        pause 1.0
        "Dancing/belladancing02.png" with fastdissolve
        pause 1.1
        "Dancing/belladancing02b.png"
        pause .9
        "Dancing/belladancing03.png" with fastdissolve
        pause 1.0
        "Dancing/belladancing03b.png"
        pause 1.0
        "Dancing/belladancing04.png" with fastdissolve
        pause 1.0
        "Dancing/belladancing04b.png"
        pause .5
        repeat

    image dancingbella02:
        "Dancing/belladancing01.png" with fastdissolve
        pause 0.6
        "Dancing/belladancing01b.png"
        pause .4
        "Dancing/belladancing02.png" with fastdissolve
        pause .8
        "Dancing/belladancing02b.png"
        pause 0.8
        "Dancing/belladancing03.png" with fastdissolve
        pause .8
        "Dancing/belladancing03b.png"
        pause .8
        "Dancing/belladancing04.png" with fastdissolve
        pause .8
        "Dancing/belladancing04b.png"
        pause .4
        "Dancing/belladancing02.png" with fastdissolve
        pause .4
        "Dancing/belladancing02b.png"
        pause .4
        repeat

    image dancingsuki01:
        "v072/sukidancing01.png" with fastdissolve
        pause .7
        "v072/sukidancing01b.png"
        pause 1.0
        "v072/sukidancing02.png" with fastdissolve
        pause 1.1
        "v072/sukidancing02b.png"
        pause .9
        "v072/sukidancing03.png" with fastdissolve
        pause 1.0
        "v072/sukidancing03b.png"
        pause 1.0
        "v072/sukidancing04.png" with fastdissolve
        pause 1.0
        "v072/sukidancing04b.png"
        pause .5
        repeat

    image dancingsuki02:
        "v072/sukidancing01.png" with fastdissolve
        pause 0.6
        "v072/sukidancing01b.png"
        pause .4
        "v072/sukidancing02.png" with fastdissolve
        pause .8
        "v072/sukidancing02b.png"
        pause 0.8
        "v072/sukidancing03.png" with fastdissolve
        pause .8
        "v072/sukidancing03b.png"
        pause .8
        "v072/sukidancing04.png" with fastdissolve
        pause .8
        "v072/sukidancing04b.png"
        pause .4
        "v072/sukidancing02.png" with fastdissolve
        pause .4
        "v072/sukidancing02b.png"
        pause .4
        repeat
            
    image dancingmc02:
        "Dancing/mcdancing01.png" with fastdissolve
        pause 0.6
        "Dancing/mcdancing01b.png"
        pause .4
        "Dancing/mcdancing02.png" with fastdissolve
        pause .8
        "Dancing/mcdancing02b.png"
        pause 0.8
        "Dancing/mcdancing03.png" with fastdissolve
        pause .8
        "Dancing/mcdancing03b.png"
        pause .8
        "Dancing/mcdancing04.png" with fastdissolve
        pause .8
        "Dancing/mcdancing04b.png"
        pause .4
        "Dancing/mcdancing02.png" with fastdissolve
        pause .4
        "Dancing/mcdancing02b.png"
        pause .4
        repeat

    screen dancing:
        modal True
        if dpartyroll == 1:
            imagebutton:
                focus_mask True
                idle "Icons/approachleft.png"
                hover "Icons/approachleft.png"
                action Jump ("CyrlDancing")
            imagebutton:
                focus_mask True
                idle "Icons/approachright.png"
                hover "Icons/approachright.png"
                action Jump ("AngieDancing") 
        if dpartyroll == 2:
            imagebutton:
                focus_mask True
                idle "Icons/approachleft.png"
                hover "Icons/approachleft.png"
                action Jump ("AngieDancing")
            imagebutton:
                focus_mask True
                idle "Icons/approachright.png"
                hover "Icons/approachright.png"
                action Jump ("BellaDancing") 
        if dpartyroll == 3:
            imagebutton:
                focus_mask True
                idle "Icons/approachleft.png"
                hover "Icons/approachleft.png"
                action Jump ("BellaDancing")
            imagebutton:
                focus_mask True
                idle "Icons/approachright.png"
                hover "Icons/approachright.png"
                action Jump ("MichikoDancing") 
        if dpartyroll == 4:
            imagebutton:
                focus_mask True
                idle "Icons/approachleft.png"
                hover "Icons/approachleft.png"
                action Jump ("MichikoDancing")
            imagebutton:
                focus_mask True
                idle "Icons/approachright.png"
                hover "Icons/approachright.png"
                action Jump ("AylaDancing") 
        if dpartyroll == 5:
            imagebutton:
                focus_mask True
                idle "Icons/approachleft.png"
                hover "Icons/approachleft.png"
                action Jump ("AylaDancing")
            imagebutton:
                focus_mask True
                idle "Icons/approachright.png"
                hover "Icons/approachright.png"
                action Jump ("SukiDancing") 
        if dpartyroll == 6:
            imagebutton:
                focus_mask True
                idle "Icons/approachleft.png"
                hover "Icons/approachleft.png"
                action Jump ("SukiDancing")
            imagebutton:
                focus_mask True
                idle "Icons/approachright.png"
                hover "Icons/approachright.png"
                action Jump ("CyrlDancing") 
        
    screen dancing02:
        modal True
        if dpartyroll == 1:
            imagebutton:
                focus_mask True
                idle "Icons/approachleft.png"
                hover "Icons/approachleft.png"
                action Jump ("CyrlDancing")
            imagebutton:
                focus_mask True
                idle "Icons/approachright.png"
                hover "Icons/approachright.png"
                action Jump ("BellaDancing") 
        if dpartyroll == 2:
            imagebutton:
                focus_mask True
                idle "Icons/approachleft.png"
                hover "Icons/approachleft.png"
                action Jump ("BellaDancing")
            imagebutton:
                focus_mask True
                idle "Icons/approachright.png"
                hover "Icons/approachright.png"
                action Jump ("MichikoDancing") 
        if dpartyroll == 3:
            imagebutton:
                focus_mask True
                idle "Icons/approachleft.png"
                hover "Icons/approachleft.png"
                action Jump ("MichikoDancing")
            imagebutton:
                focus_mask True
                idle "Icons/approachright.png"
                hover "Icons/approachright.png"
                action Jump ("AylaDancing") 
        if dpartyroll == 4:
            imagebutton:
                focus_mask True
                idle "Icons/approachleft.png"
                hover "Icons/approachleft.png"
                action Jump ("AylaDancing")
            imagebutton:
                focus_mask True
                idle "Icons/approachright.png"
                hover "Icons/approachright.png"
                action Jump ("SukiDancing") 
        if dpartyroll == 5:
            imagebutton:
                focus_mask True
                idle "Icons/approachleft.png"
                hover "Icons/approachleft.png"
                action Jump ("SukiDancing")
            imagebutton:
                focus_mask True
                idle "Icons/approachright.png"
                hover "Icons/approachright.png"
                action Jump ("CyrlDancing") 
        
    image zarabutt:
        "Zara/zarabutt015.png"
        pause .05
        "Zara/zarabutt016.png"
        pause .05
        "Zara/zarabutt017.png"
        pause .05
        "Zara/zarabutt018.png"
        pause .05
        "Zara/zarabutt019.png"
        pause .05
        "Zara/zarabutt020.png"
        pause .05
        "Zara/zarabutt021.png"
        pause .05
        "Zara/zarabutt022.png"
        pause .05
        "Zara/zarabutt023.png"
        pause .05
        "Zara/zarabutt024.png"
        pause .05
        "Zara/zarabutt025.png"
        pause .05
        "Zara/zarabutt026.png"
        pause .05
        "Zara/zarabutt027.png"
        pause .05
        "Zara/zarabutt028.png"
        pause .05
        "Zara/zarabutt029.png"
        pause .05
        "Zara/zarabutt030.png"
        pause .05
        "Zara/zarabutt031.png"
        pause .05
        "Zara/zarabutt032.png"
        pause .05
        "Zara/zarabutt033.png"
        pause .05
        "Zara/zarabutt034.png"
        pause .05
        "Zara/zarabutt035.png"
        pause .05
        "Zara/zarabutt036.png"
        pause .05
        "Zara/zarabutt037.png"
        pause .05
        "Zara/zarabutt038.png"
        pause .05
        "Zara/zarabutt039.png"
        pause .05
        "Zara/zarabutt040.png"
        pause .05
        "Zara/zarabutt041.png"
        pause .05
        "Zara/zarabutt042.png"
        pause .05
        "Zara/zarabutt043.png"
        pause .05
        "Zara/zarabutt044.png"
        pause .05
        "Zara/zarabutt045.png"
        pause .05
        "Zara/zarabutt046.png"
        pause .05
        "Zara/zarabutt047.png"
        pause .05
        "Zara/zarabutt048.png"
        pause .05
        "Zara/zarabutt049.png"
        pause .05
        "Zara/zarabutt050.png"
        pause .05
        "Zara/zarabutt051.png"
        pause .05

        repeat

    image zaradance01:
        "Zara/zaradance015.png"
        pause .05
        "Zara/zaradance016.png"
        pause .05
        "Zara/zaradance017.png"
        pause .05
        "Zara/zaradance018.png"
        pause .05
        "Zara/zaradance019.png"
        pause .05
        "Zara/zaradance020.png"
        pause .05
        "Zara/zaradance021.png"
        pause .05
        "Zara/zaradance022.png"
        pause .05
        "Zara/zaradance023.png"
        pause .05
        "Zara/zaradance024.png"
        pause .05
        "Zara/zaradance025.png"
        pause .05
        "Zara/zaradance026.png"
        pause .05
        "Zara/zaradance027.png"
        pause .05
        "Zara/zaradance028.png"
        pause .05
        "Zara/zaradance029.png"
        pause .05
        "Zara/zaradance030.png"
        pause .05
        "Zara/zaradance031.png"
        pause .05
        "Zara/zaradance032.png"
        pause .05
        "Zara/zaradance033.png"
        pause .05
        "Zara/zaradance034.png"
        pause .05
        "Zara/zaradance035.png"
        pause .05
        "Zara/zaradance036.png"
        pause .05
        "Zara/zaradance037.png"
        pause .05
        "Zara/zaradance038.png"
        pause .05
        "Zara/zaradance039.png"
        pause .05
        "Zara/zaradance040.png"
        pause .05
        "Zara/zaradance041.png"
        pause .05
        "Zara/zaradance042.png"
        pause .05
        "Zara/zaradance043.png"
        pause .05
        "Zara/zaradance044.png"
        pause .05
        "Zara/zaradance045.png"
        pause .05
        "Zara/zaradance046.png"
        pause .05
        "Zara/zaradance047.png"
        pause .05
        "Zara/zaradance048.png"
        pause .05
        "Zara/zaradance049.png"
        pause .05
        "Zara/zaradance050.png"
        pause .05
        "Zara/zaradance051.png"
        pause .05
        "Zara/zaradance052.png"
        pause .05
        "Zara/zaradance053.png"
        pause .05
        "Zara/zaradance054.png"
        pause .05
        "Zara/zaradance055.png"
        pause .05
        "Zara/zaradance056.png"
        pause .05
        "Zara/zaradance057.png"
        pause .05
        "Zara/zaradance058.png"
        pause .05
        "Zara/zaradance059.png"
        pause .05
        "Zara/zaradance060.png"
        pause .05
        "Zara/zaradance061.png"
        pause .05
        "Zara/zaradance062.png"
        pause .05
        "Zara/zaradance063.png"
        pause .05
        "Zara/zaradance064.png"
        pause .05
        "Zara/zaradance065.png"
        pause .05
        "Zara/zaradance066.png"
        pause .05
        "Zara/zaradance067.png"
        pause .05
        "Zara/zaradance068.png"
        pause .05
        "Zara/zaradance069.png"
        pause .05
        "Zara/zaradance070.png"
        pause .05
        "Zara/zaradance071.png"
        pause .05
        "Zara/zaradance072.png"
        pause .05
        "Zara/zaradance073.png"
        pause .05
        "Zara/zaradance074.png"
        pause .05
        "Zara/zaradance075.png"
        pause .05
        "Zara/zaradance076.png"
        pause .05
        "Zara/zaradance077.png"
        pause .05
        "Zara/zaradance078.png"
        pause .05
        "Zara/zaradance079.png"
        pause .05
        "Zara/zaradance080.png"
        pause .05
        "Zara/zaradance081.png"
        pause .05
        "Zara/zaradance082.png"
        pause .05
        "Zara/zaradance083.png"
        pause .05
        "Zara/zaradance084.png"
        pause .05
        "Zara/zaradance085.png"
        pause .05
        "Zara/zaradance086.png"
        pause .05
        "Zara/zaradance087.png"
        pause .05
        "Zara/zaradance088.png"
        pause .05
        "Zara/zaradance089.png"
        pause .05
        repeat

    image zaradance02:
        "Zara/zaradancec015.png"
        pause .05
        "Zara/zaradancec016.png"
        pause .05
        "Zara/zaradancec017.png"
        pause .05
        "Zara/zaradancec018.png"
        pause .05
        "Zara/zaradancec019.png"
        pause .05
        "Zara/zaradancec020.png"
        pause .05
        "Zara/zaradancec021.png"
        pause .05
        "Zara/zaradancec022.png"
        pause .05
        "Zara/zaradancec023.png"
        pause .05
        "Zara/zaradancec024.png"
        pause .05
        "Zara/zaradancec025.png"
        pause .05
        "Zara/zaradancec026.png"
        pause .05
        "Zara/zaradancec027.png"
        pause .05
        "Zara/zaradancec028.png"
        pause .05
        "Zara/zaradancec029.png"
        pause .05
        "Zara/zaradancec030.png"
        pause .05
        "Zara/zaradancec031.png"
        pause .05
        "Zara/zaradancec032.png"
        pause .05
        "Zara/zaradancec033.png"
        pause .05
        "Zara/zaradancec034.png"
        pause .05
        "Zara/zaradancec035.png"
        pause .05
        "Zara/zaradancec036.png"
        pause .05
        "Zara/zaradancec037.png"
        pause .05
        "Zara/zaradancec038.png"
        pause .05
        "Zara/zaradancec039.png"
        pause .05
        "Zara/zaradancec040.png"
        pause .05
        "Zara/zaradancec041.png"
        pause .05
        "Zara/zaradancec042.png"
        pause .05
        "Zara/zaradancec043.png"
        pause .05
        "Zara/zaradancec044.png"
        pause .05
        "Zara/zaradancec045.png"
        pause .05
        "Zara/zaradancec046.png"
        pause .05
        "Zara/zaradancec047.png"
        pause .05
        "Zara/zaradancec048.png"
        pause .05
        "Zara/zaradancec049.png"
        pause .05
        "Zara/zaradancec050.png"
        pause .05
        "Zara/zaradancec051.png"
        pause .05
        "Zara/zaradancec052.png"
        pause .05
        "Zara/zaradancec053.png"
        pause .05
        "Zara/zaradancec054.png"
        pause .05
        "Zara/zaradancec055.png"
        pause .05
        "Zara/zaradancec056.png"
        pause .05
        "Zara/zaradancec057.png"
        pause .05
        "Zara/zaradancec058.png"
        pause .05
        "Zara/zaradancec059.png"
        pause .05
        "Zara/zaradancec060.png"
        pause .05
        "Zara/zaradancec061.png"
        pause .05
        "Zara/zaradancec062.png"
        pause .05
        "Zara/zaradancec063.png"
        pause .05
        "Zara/zaradancec064.png"
        pause .05
        "Zara/zaradancec065.png"
        pause .05
        "Zara/zaradancec066.png"
        pause .05
        "Zara/zaradancec067.png"
        pause .05
        "Zara/zaradancec068.png"
        pause .05
        "Zara/zaradancec069.png"
        pause .05
        "Zara/zaradancec070.png"
        pause .05
        "Zara/zaradancec071.png"
        pause .05
        "Zara/zaradancec072.png"
        pause .05
        "Zara/zaradancec073.png"
        pause .05
        "Zara/zaradancec074.png"
        pause .05
        "Zara/zaradancec075.png"
        pause .05
        "Zara/zaradancec076.png"
        pause .05
        "Zara/zaradancec077.png"
        pause .05
        "Zara/zaradancec078.png"
        pause .05
        "Zara/zaradancec079.png"
        pause .05
        "Zara/zaradancec080.png"
        pause .05
        "Zara/zaradancec081.png"
        pause .05
        "Zara/zaradancec082.png"
        pause .05
        "Zara/zaradancec083.png"
        pause .05
        "Zara/zaradancec084.png"
        pause .05
        "Zara/zaradancec085.png"
        pause .05
        "Zara/zaradancec086.png"
        pause .05
        "Zara/zaradancec087.png"
        pause .05
        "Zara/zaradancec088.png"
        pause .05
        "Zara/zaradancec089.png"
        pause .05
        repeat    
    
    transform alienfuck:
        "Explore/alienfuck00.png"
        pause .05
        "Explore/alienfuck01.png"
        pause .05
        "Explore/alienfuck02.png"
        pause .05
        "Explore/alienfuck03.png"
        pause .05
        "Explore/alienfuck04.png"
        pause .05
        "Explore/alienfuck05.png"
        pause .05
        "Explore/alienfuck06.png"
        pause .05
        "Explore/alienfuck07.png"
        pause .05
        "Explore/alienfuck08.png"
        pause .05
        "Explore/alienfuck09.png"
        pause .05
        "Explore/alienfuck11.png"
        pause .05
        "Explore/alienfuck12.png"
        pause .05
        "Explore/alienfuck13.png"
        pause .05
        "Explore/alienfuck14.png"
        pause .05
        "Explore/alienfuck15.png"
        pause .05
        "Explore/alienfuck16.png"
        pause .05
        "Explore/alienfuck17.png"
        pause .05
        "Explore/alienfuck18.png"
        pause .05
        "Explore/alienfuck19.png"
        pause .05
        "Explore/alienfuck20.png"
        pause .05
        repeat

    transform alienpennyfuck:
        "Explore/pennyfuck00.png"
        pause .05
        "Explore/pennyfuck01.png"
        pause .05
        "Explore/pennyfuck02.png"
        pause .05
        "Explore/pennyfuck03.png"
        pause .05
        "Explore/pennyfuck04.png"
        pause .05
        "Explore/pennyfuck05.png"
        pause .05
        "Explore/pennyfuck06.png"
        pause .05
        "Explore/pennyfuck07.png"
        pause .05
        "Explore/pennyfuck08.png"
        pause .05
        "Explore/pennyfuck09.png"
        pause .05
        "Explore/pennyfuck10.png"
        pause .05
        "Explore/pennyfuck11.png"
        pause .05
        "Explore/pennyfuck12.png"
        pause .05
        "Explore/pennyfuck13.png"
        pause .05
        "Explore/pennyfuck14.png"
        pause .05
        "Explore/pennyfuck15.png"
        pause .05
        "Explore/pennyfuck16.png"
        pause .05
        "Explore/pennyfuck17.png"
        pause .05
        "Explore/pennyfuck18.png"
        pause .05
        "Explore/pennyfuck19.png"
        pause .05
        "Explore/pennyfuck20.png"
        pause .05
        repeat
        
    transform alienbellafuck:
        "Explore/bellafuck00.png"
        pause .05
        "Explore/bellafuck01.png"
        pause .05
        "Explore/bellafuck02.png"
        pause .05
        "Explore/bellafuck03.png"
        pause .05
        "Explore/bellafuck04.png"
        pause .05
        "Explore/bellafuck05.png"
        pause .05
        "Explore/bellafuck06.png"
        pause .05
        "Explore/bellafuck07.png"
        pause .05
        "Explore/bellafuck08.png"
        pause .05
        "Explore/bellafuck09.png"
        pause .05
        "Explore/bellafuck10.png"
        pause .05
        "Explore/bellafuck11.png"
        pause .05
        "Explore/bellafuck12.png"
        pause .05
        "Explore/bellafuck13.png"
        pause .05
        "Explore/bellafuck14.png"
        pause .05
        "Explore/bellafuck15.png"
        pause .05
        "Explore/bellafuck16.png"
        pause .05
        "Explore/bellafuck17.png"
        pause .05
        "Explore/bellafuck18.png"
        pause .05
        "Explore/bellafuck19.png"
        pause .05
        "Explore/bellafuck20.png"
        pause .05
        repeat

    image nancygym:
        "Gym/nancytrain01.png" with fastdissolve
        pause .5
        "Gym/nancytrain02.png" with fastdissolve
        pause .4
        "Gym/nancytrain03.png" with fastdissolve
        pause .4
        "Gym/nancytrain04.png" with fastdissolve
        pause .3
        "Gym/nancytrain05.png" with fastdissolve
        pause .3
        "Gym/nancytrain04.png" with fastdissolve
        pause .3
        "Gym/nancytrain06.png" with fastdissolve
        pause .3
        "Gym/nancytrain04.png" with fastdissolve
        pause .3
        "Gym/nancytrain03.png" with fastdissolve
        pause .3
        "Gym/nancytrain02.png" with fastdissolve
        pause .3
        repeat

    image marniegym:
        "Gym/marnietrain00.png" with fastdissolve
        pause .15
        "Gym/marnietrain01.png" with fastdissolve
        pause .08
        "Gym/marnietrain02.png" with fastdissolve
        pause .15
        "Gym/marnietrain03.png" with fastdissolve
        pause .08
        "Gym/marnietrain04.png" with fastdissolve
        pause .08
        "Gym/marnietrain05.png" with fastdissolve
        pause .08
        "Gym/marnietrain06.png" with fastdissolve
        pause .15
        "Gym/marnietrain05.png" with fastdissolve
        pause .08
        "Gym/marnietrain04.png" with fastdissolve
        pause .08
        "Gym/marnietrain03.png" with fastdissolve
        pause .08
        "Gym/marnietrain02.png" with fastdissolve
        pause .15
        "Gym/marnietrain01.png" with fastdissolve
        pause .08
        repeat

    image lenagym:
        "Gym/lenagymworkout00.jpg"
        pause .05
        "Gym/lenagymworkout01.jpg"
        pause .05
        "Gym/lenagymworkout02.jpg"
        pause .05
        "Gym/lenagymworkout03.jpg"
        pause .05
        "Gym/lenagymworkout04.jpg"
        pause .05
        "Gym/lenagymworkout05.jpg"
        pause .05
        "Gym/lenagymworkout06.jpg"
        pause .05
        "Gym/lenagymworkout07.jpg"
        pause .05
        "Gym/lenagymworkout08.jpg"
        pause .05
        "Gym/lenagymworkout09.jpg"
        pause .05
        "Gym/lenagymworkout10.jpg"
        pause .05
        "Gym/lenagymworkout11.jpg"
        pause .05
        "Gym/lenagymworkout12.jpg"
        pause .05
        "Gym/lenagymworkout13.jpg"
        pause .05
        "Gym/lenagymworkout14.jpg"
        pause .05
        "Gym/lenagymworkout15.jpg"
        pause .05
        "Gym/lenagymworkout16.jpg"
        pause .05
        "Gym/lenagymworkout17.jpg"
        pause .05
        "Gym/lenagymworkout18.jpg"
        pause .2
        "Gym/lenagymworkout17.jpg"
        pause .04
        "Gym/lenagymworkout16.jpg"
        pause .04
        "Gym/lenagymworkout15.jpg"
        pause .04
        "Gym/lenagymworkout14.jpg"
        pause .04
        "Gym/lenagymworkout13.jpg"
        pause .04
        "Gym/lenagymworkout12.jpg"
        pause .04
        "Gym/lenagymworkout11.jpg"
        pause .04
        "Gym/lenagymworkout10.jpg"
        pause .04
        "Gym/lenagymworkout09.jpg"
        pause .04
        "Gym/lenagymworkout08.jpg"
        pause .04
        "Gym/lenagymworkout07.jpg"
        pause .04
        "Gym/lenagymworkout06.jpg"
        pause .04
        "Gym/lenagymworkout05.jpg"
        pause .04
        "Gym/lenagymworkout04.jpg"
        pause .04
        "Gym/lenagymworkout03.jpg"
        pause .04
        "Gym/lenagymworkout02.jpg"
        pause .04
        "Gym/lenagymworkout01.jpg"
        pause .04
        repeat

    image widowpoundslow:
        "Explore/widowpound00.png"
        pause .04
        "Explore/widowpound01.png"
        pause .04
        "Explore/widowpound02.png"
        pause .04
        "Explore/widowpound03.png"
        pause .04
        "Explore/widowpound04.png"
        pause .04
        "Explore/widowpound05.png"
        pause .04
        "Explore/widowpound06.png"
        pause .04
        "Explore/widowpound07.png"
        pause .04
        "Explore/widowpound08.png"
        pause .04
        "Explore/widowpound09.png"
        pause .04
        "Explore/widowpound10.png"
        pause .04
        "Explore/widowpound11.png"
        pause .04
        "Explore/widowpound12.png"
        pause .04
        "Explore/widowpound13.png"
        pause .04
        "Explore/widowpound14.png"
        pause .04
        "Explore/widowpound15.png"
        pause .04
        "Explore/widowpound16.png"
        pause .04
        "Explore/widowpound17.png"
        pause .04
        "Explore/widowpound18.png"
        pause .04
        "Explore/widowpound19.png"
        pause .04
        "Explore/widowpound20.png"
        pause .04
        "Explore/widowpound21.png"
        pause .04
        "Explore/widowpound22.png"
        pause .04
        "Explore/widowpound23.png"
        pause .04
        "Explore/widowpound24.png"
        pause .04
        repeat
 
    image widowpoundfast:
        "Explore/widowpound00.png"
        pause .03
        "Explore/widowpound01.png"
        pause .03
        "Explore/widowpound02.png"
        pause .03
        "Explore/widowpound03.png"
        pause .03
        "Explore/widowpound04.png"
        pause .03
        "Explore/widowpound05.png"
        pause .03
        "Explore/widowpound06.png"
        pause .03
        "Explore/widowpound07.png"
        pause .03
        "Explore/widowpound08.png"
        pause .03
        "Explore/widowpound09.png"
        pause .03
        "Explore/widowpound10.png"
        pause .03
        "Explore/widowpound11.png"
        pause .03
        "Explore/widowpound12.png"
        pause .03
        "Explore/widowpound13.png"
        pause .03
        "Explore/widowpound14.png"
        pause .03
        "Explore/widowpound15.png"
        pause .03
        "Explore/widowpound16.png"
        pause .03
        "Explore/widowpound17.png"
        pause .03
        "Explore/widowpound18.png"
        pause .03
        "Explore/widowpound19.png"
        pause .03
        "Explore/widowpound20.png"
        pause .03
        "Explore/widowpound21.png"
        pause .03
        "Explore/widowpound22.png"
        pause .04
        "Explore/widowpound23.png"
        pause .04
        "Explore/widowpound24.png"
        pause .04
        repeat
      
    image widowfuckslow:
        "Explore/widowfuck03.png"
        pause .05
        "Explore/widowfuck04.png"
        pause .05
        "Explore/widowfuck05.png"
        pause .05
        "Explore/widowfuck06.png"
        pause .05
        "Explore/widowfuck07.png"
        pause .05
        "Explore/widowfuck08.png"
        pause .05
        "Explore/widowfuck09.png"
        pause .05
        "Explore/widowfuck10.png"
        pause .05
        "Explore/widowfuck11.png"
        pause .05
        "Explore/widowfuck12.png"
        pause .05
        "Explore/widowfuck13.png"
        pause .05
        "Explore/widowfuck14.png"
        pause .05
        "Explore/widowfuck13b.png"
        pause .04
        "Explore/widowfuck12b.png"
        pause .04
        "Explore/widowfuck11b.png"
        pause .04
        "Explore/widowfuck10b.png"
        pause .04
        "Explore/widowfuck09b.png"
        pause .04
        "Explore/widowfuck08b.png"
        pause .04
        "Explore/widowfuck07b.png"
        pause .04
        "Explore/widowfuck06b.png"
        pause .04
        "Explore/widowfuck05b.png"
        pause .04
        "Explore/widowfuck04b.png"
        pause .04       
        repeat

    image widowfuckfast:
        "Explore/widowfuck03.png"
        pause .04
        "Explore/widowfuck04.png"
        pause .04
        "Explore/widowfuck05.png"
        pause .04
        "Explore/widowfuck06.png"
        pause .04
        "Explore/widowfuck07.png"
        pause .04
        "Explore/widowfuck08.png"
        pause .04
        "Explore/widowfuck09.png"
        pause .04
        "Explore/widowfuck10.png"
        pause .04
        "Explore/widowfuck11.png"
        pause .04
        "Explore/widowfuck12.png"
        pause .04
        "Explore/widowfuck13.png"
        pause .04
        "Explore/widowfuck14.png"
        pause .04
        "Explore/widowfuck13b.png"
        pause .03
        "Explore/widowfuck12b.png"
        pause .03
        "Explore/widowfuck11b.png"
        pause .03
        "Explore/widowfuck10b.png"
        pause .03
        "Explore/widowfuck09b.png"
        pause .03
        "Explore/widowfuck08b.png"
        pause .03
        "Explore/widowfuck07b.png"
        pause .03
        "Explore/widowfuck06b.png"
        pause .03
        "Explore/widowfuck05b.png"
        pause .03
        "Explore/widowfuck04b.png"
        pause .03       
        repeat
    
    image siri01aa:
        "Bedroom/siri01a.png"
        pause 3.0
        "Bedroom/siri01ab.png"
        pause 0.2
        "Bedroom/siri01a.png"
        pause 0.1
        "Bedroom/siri01ab.png"
        pause 0.2
        repeat
        
    image siri01ba:
        "Bedroom/siri01b.png"
        pause 3.0
        "Bedroom/siri01bb.png"
        pause 0.2
        "Bedroom/siri01b.png"
        pause 0.1
        "Bedroom/siri01bb.png"
        pause 0.2
        repeat

    image siri01ca:
        "Bedroom/siri01c.png"
        pause 3.0
        "Bedroom/siri01cb.png"
        pause 0.2
        "Bedroom/siri01c.png"
        pause 0.1
        "Bedroom/siri01cb.png"
        pause 0.2
        repeat

    image siri02aa:
        "Bedroom/siri02a.png"
        pause 3.0
        "Bedroom/siri02ab.png"
        pause 0.2
        "Bedroom/siri02a.png"
        pause 0.1
        "Bedroom/siri02ab.png"
        pause 0.2
        repeat
        
    image siri02ba:
        "Bedroom/siri02b.png"
        pause 3.0
        "Bedroom/siri02bb.png"
        pause 0.2
        "Bedroom/siri02b.png"
        pause 0.1
        "Bedroom/siri02bb.png"
        pause 0.2
        repeat

    image siri02ca:
        "Bedroom/siri02c.png"
        pause 3.0
        "Bedroom/siri02cb.png"
        pause 0.2
        "Bedroom/siri02c.png"
        pause 0.1
        "Bedroom/siri02cb.png"
        pause 0.2
        repeat

    image siri03aa:
        "Bedroom/siri03a.png"
        pause 3.0
        "Bedroom/siri03ab.png"
        pause 0.2
        "Bedroom/siri03a.png"
        pause 0.1
        "Bedroom/siri03ab.png"
        pause 0.2
        repeat
        
    image siri03ba:
        "Bedroom/siri03b.png"
        pause 3.0
        "Bedroom/siri03bb.png"
        pause 0.2
        "Bedroom/siri03b.png"
        pause 0.1
        "Bedroom/siri03bb.png"
        pause 0.2
        repeat

    image siri03ca:
        "Bedroom/siri03c.png"
        pause 3.0
        "Bedroom/siri03cb.png"
        pause 0.2
        "Bedroom/siri03c.png"
        pause 0.1
        "Bedroom/siri03cb.png"
        pause 0.2
        repeat

    image siri04aa:
        "Bedroom/siri04a.png"
        pause 3.0
        "Bedroom/siri04ab.png"
        pause 0.2
        "Bedroom/siri04a.png"
        pause 0.1
        "Bedroom/siri04ab.png"
        pause 0.2
        repeat
        
    image siri04ba:
        "Bedroom/siri04b.png"
        pause 3.0
        "Bedroom/siri04bb.png"
        pause 0.2
        "Bedroom/siri04b.png"
        pause 0.1
        "Bedroom/siri04bb.png"
        pause 0.2
        repeat

    image siri04ca:
        "Bedroom/siri04c.png"
        pause 3.0
        "Bedroom/siri04cb.png"
        pause 0.2
        "Bedroom/siri04c.png"
        pause 0.1
        "Bedroom/siri04cb.png"
        pause 0.2
        repeat

    image siri05aa:
        "Bedroom/siri05a.png"
        pause 3.0
        "Bedroom/siri05ab.png"
        pause 0.2
        "Bedroom/siri05a.png"
        pause 0.1
        "Bedroom/siri05ab.png"
        pause 0.2
        repeat
        
    image siri05ba:
        "Bedroom/siri05b.png"
        pause 3.0
        "Bedroom/siri05bb.png"
        pause 0.2
        "Bedroom/siri05b.png"
        pause 0.1
        "Bedroom/siri05bb.png"
        pause 0.2
        repeat

    image siri05ca:
        "Bedroom/siri05c.png"
        pause 3.0
        "Bedroom/siri05cb.png"
        pause 0.2
        "Bedroom/siri05c.png"
        pause 0.1
        "Bedroom/siri05cb.png"
        pause 0.2
        repeat

    image siri06aa:
        "Bedroom/siri06a.png"
        pause 3.0
        "Bedroom/siri06ab.png"
        pause 0.2
        "Bedroom/siri06a.png"
        pause 0.1
        "Bedroom/siri06ab.png"
        pause 0.2
        repeat
        
    image siri06ba:
        "Bedroom/siri06b.png"
        pause 3.0
        "Bedroom/siri06bb.png"
        pause 0.2
        "Bedroom/siri06b.png"
        pause 0.1
        "Bedroom/siri06bb.png"
        pause 0.2
        repeat

    image siri06ca:
        "Bedroom/siri06c.png"
        pause 3.0
        "Bedroom/siri06cb.png"
        pause 0.2
        "Bedroom/siri06c.png"
        pause 0.1
        "Bedroom/siri06cb.png"
        pause 0.2
        repeat

    transform rubygymbell:
        "Gym/rubyworkout00.png"
        pause .05
        "Gym/rubyworkout01.png"
        pause .05
        "Gym/rubyworkout02.png"
        pause .05
        "Gym/rubyworkout03.png"
        pause .05
        "Gym/rubyworkout04.png"
        pause .05
        "Gym/rubyworkout05.png"
        pause .05
        "Gym/rubyworkout06.png"
        pause .05
        "Gym/rubyworkout07.png"
        pause .05
        "Gym/rubyworkout08.png"
        pause .05
        "Gym/rubyworkout09.png"
        pause .05
        "Gym/rubyworkout10.png"
        pause .05
        "Gym/rubyworkout11.png"
        pause .05
        "Gym/rubyworkout12.png"
        pause .05
        "Gym/rubyworkout13.png"
        pause .05
        "Gym/rubyworkout14.png"
        pause .05
        "Gym/rubyworkout15.png"
        pause .05
        "Gym/rubyworkout16.png"
        pause .05
        "Gym/rubyworkout17.png"
        pause .05
        "Gym/rubyworkout18.png"
        pause .2
        "Gym/rubyworkout17.png"
        pause .04
        "Gym/rubyworkout16.png"
        pause .04
        "Gym/rubyworkout15.png"
        pause .04
        "Gym/rubyworkout14.png"
        pause .04
        "Gym/rubyworkout13.png"
        pause .04
        "Gym/rubyworkout12.png"
        pause .04
        "Gym/rubyworkout11.png"
        pause .04
        "Gym/rubyworkout10.png"
        pause .04
        "Gym/rubyworkout09.png"
        pause .04
        "Gym/rubyworkout08.png"
        pause .04
        "Gym/rubyworkout07.png"
        pause .04
        "Gym/rubyworkout06.png"
        pause .04
        "Gym/rubyworkout05.png"
        pause .04
        "Gym/rubyworkout04.png"
        pause .04
        "Gym/rubyworkout03.png"
        pause .04
        "Gym/rubyworkout02.png"
        pause .04
        "Gym/rubyworkout01.png"
        pause .04
        repeat

    transform lauriegym:
        "Gym/lauriegym00.png"
        pause .05
        "Gym/lauriegym01.png"
        pause .05
        "Gym/lauriegym02.png"
        pause .05
        "Gym/lauriegym03.png"
        pause .05
        "Gym/lauriegym04.png"
        pause .05
        "Gym/lauriegym05.png"
        pause .05
        "Gym/lauriegym06.png"
        pause .05
        "Gym/lauriegym07.png"
        pause .05
        "Gym/lauriegym08.png"
        pause .05
        "Gym/lauriegym09.png"
        pause .05
        "Gym/lauriegym10.png"
        pause .05
        "Gym/lauriegym11.png"
        pause .05
        "Gym/lauriegym12.png"
        pause .05
        "Gym/lauriegym13.png"
        pause .05
        "Gym/lauriegym14.png"
        pause .05
        "Gym/lauriegym15.png"
        pause .05
        "Gym/lauriegym16.png"
        pause .05
        "Gym/lauriegym17.png"
        pause .05
        "Gym/lauriegym18.png"
        pause .05
        "Gym/lauriegym19.png"
        pause .05
        "Gym/lauriegym20.png"
        pause .05
        repeat

    image mcgym01:
        "Gym/mcgym01.jpg"
        pause .15
        "Gym/mcgym02.jpg"
        pause .05
        "Gym/mcgym03.jpg"
        pause .05
        "Gym/mcgym04.jpg"
        pause .05
        "Gym/mcgym05.jpg"
        pause .05
        "Gym/mcgym06.jpg"
        pause .05
        "Gym/mcgym07.jpg"
        pause .05
        "Gym/mcgym08.jpg"
        pause .05
        "Gym/mcgym09.jpg"
        pause .05
        "Gym/mcgym10.jpg"
        pause .05
        "Gym/mcgym11.jpg"
        pause .05
        "Gym/mcgym12.jpg"
        pause .05
        "Gym/mcgym13.jpg"
        pause .05
        "Gym/mcgym14.jpg"
        pause .05
        "Gym/mcgym15.jpg"
        pause .05
        "Gym/mcgym16.jpg"
        pause .05
        "Gym/mcgym17.jpg"
        pause .05
        "Gym/mcgym18.jpg"
        pause .2
        "Gym/mcgym17.jpg"
        pause .04
        "Gym/mcgym16.jpg"
        pause .04
        "Gym/mcgym15.jpg"
        pause .04
        "Gym/mcgym14.jpg"
        pause .04
        "Gym/mcgym13.jpg"
        pause .04
        "Gym/mcgym12.jpg"
        pause .04
        "Gym/mcgym11.jpg"
        pause .04
        "Gym/mcgym10.jpg"
        pause .04
        "Gym/mcgym09.jpg"
        pause .04
        "Gym/mcgym08.jpg"
        pause .04
        "Gym/mcgym07.jpg"
        pause .04
        "Gym/mcgym06.jpg"
        pause .04
        "Gym/mcgym05.jpg"
        pause .04
        "Gym/mcgym04.jpg"
        pause .04
        "Gym/mcgym03.jpg"
        pause .04
        "Gym/mcgym02.jpg"
        pause .04        
        repeat

    image mcgym01b:
        "Gym/mcliftNEW01.jpg"
        pause .15
        "Gym/mcliftNEW02.jpg"
        pause .05
        "Gym/mcliftNEW03.jpg"
        pause .05
        "Gym/mcliftNEW04.jpg"
        pause .05
        "Gym/mcliftNEW05.jpg"
        pause .05
        "Gym/mcliftNEW06.jpg"
        pause .05
        "Gym/mcliftNEW07.jpg"
        pause .05
        "Gym/mcliftNEW08.jpg"
        pause .05
        "Gym/mcliftNEW09.jpg"
        pause .05
        "Gym/mcliftNEW10.jpg"
        pause .05
        "Gym/mcliftNEW11.jpg"
        pause .05
        "Gym/mcliftNEW12.jpg"
        pause .05
        "Gym/mcliftNEW13.jpg"
        pause .05
        "Gym/mcliftNEW14.jpg"
        pause .05
        "Gym/mcliftNEW15.jpg"
        pause .05
        "Gym/mcliftNEW16.jpg"
        pause .05
        "Gym/mcliftNEW17.jpg"
        pause .05
        "Gym/mcliftNEW18.jpg"
        pause .2
        "Gym/mcliftNEW17.jpg"
        pause .04
        "Gym/mcliftNEW16.jpg"
        pause .04
        "Gym/mcliftNEW15.jpg"
        pause .04
        "Gym/mcliftNEW14.jpg"
        pause .04
        "Gym/mcliftNEW13.jpg"
        pause .04
        "Gym/mcliftNEW12.jpg"
        pause .04
        "Gym/mcliftNEW11.jpg"
        pause .04
        "Gym/mcliftNEW10.jpg"
        pause .04
        "Gym/mcliftNEW09.jpg"
        pause .04
        "Gym/mcliftNEW08.jpg"
        pause .04
        "Gym/mcliftNEW07.jpg"
        pause .04
        "Gym/mcliftNEW06.jpg"
        pause .04
        "Gym/mcliftNEW05.jpg"
        pause .04
        "Gym/mcliftNEW04.jpg"
        pause .04
        "Gym/mcliftNEW03.jpg"
        pause .04
        "Gym/mcliftNEW02.jpg"
        pause .04        
        repeat

    image rachelblow:
        "medbay/rachelblow00.png"
        pause .1
        "medbay/rachelblow01.png"
        pause .04
        "medbay/rachelblow02.png"
        pause .04
        "medbay/rachelblow03.png"
        pause .04
        "medbay/rachelblow04.png"
        pause .04
        "medbay/rachelblow05.png"
        pause .04
        "medbay/rachelblow06.png"
        pause .04
        "medbay/rachelblow07.png"
        pause .04
        "medbay/rachelblow08.png"
        pause .04
        "medbay/rachelblow09.png"
        pause .04
        "medbay/rachelblow10.png"
        pause .04
        "medbay/rachelblow11.png"
        pause .04
        "medbay/rachelblow12.png"
        pause .04
        "medbay/rachelblow13.png"
        pause .04
        "medbay/rachelblow14.png"
        pause .04
        "medbay/rachelblow15.png"
        pause .04
        "medbay/rachelblow14.png"
        pause .04
        "medbay/rachelblow13.png"
        pause .04
        "medbay/rachelblow11.png"
        pause .04
        "medbay/rachelblow11.png"
        pause .04
        "medbay/rachelblow10.png"
        pause .04
        "medbay/rachelblow09.png"
        pause .04
        "medbay/rachelblow08.png"
        pause .04
        "medbay/rachelblow07.png"
        pause .04
        "medbay/rachelblow06.png"
        pause .04
        "medbay/rachelblow05.png"
        pause .04
        "medbay/rachelblow04.png"
        pause .04
        "medbay/rachelblow03.png"
        pause .04
        "medbay/rachelblow02.png"
        pause .04
        "medbay/rachelblow01.png"
        pause .04
        repeat

    image rachelbutt:
        "medbay/rachelbutt00.png"
        pause .08
        "medbay/rachelbutt01.png"
        pause .05
        "medbay/rachelbutt02.png"
        pause .05
        "medbay/rachelbutt03.png"
        pause .05
        "medbay/rachelbutt04.png"
        pause .05
        "medbay/rachelbutt05.png"
        pause .05
        "medbay/rachelbutt06.png"
        pause .05
        "medbay/rachelbutt07.png"
        pause .08
        "medbay/rachelbutt06.png"
        pause .05
        "medbay/rachelbutt05.png"
        pause .05
        "medbay/rachelbutt04.png"
        pause .05
        "medbay/rachelbutt03.png"
        pause .05
        "medbay/rachelbutt02.png"
        pause .05
        "medbay/rachelbutt01.png"
        pause .05
        repeat

    image rachelwank:
        "medbay/rachelwank00.png"
        pause .1
        "medbay/rachelwank01.png"
        pause .05
        "medbay/rachelwank02.png"
        pause .05
        "medbay/rachelwank03.png"
        pause .05
        "medbay/rachelwank04.png"
        pause .05
        "medbay/rachelwank05.png"
        pause .05
        "medbay/rachelwank06.png"
        pause .05
        "medbay/rachelwank07.png"
        pause .05
        "medbay/rachelwank08.png"
        pause .1
        "medbay/rachelwank07.png"
        pause .05
        "medbay/rachelwank06.png"
        pause .05
        "medbay/rachelwank05.png"
        pause .05
        "medbay/rachelwank04.png"
        pause .05
        "medbay/rachelwank03.png"
        pause .05
        "medbay/rachelwank02.png"
        pause .05
        "medbay/rachelwank01.png"
        pause .05
        repeat

    image racheltits:
        "medbay/racheltits00.png"
        pause .08
        "medbay/racheltits01.png"
        pause .04
        "medbay/racheltits02.png"
        pause .04
        "medbay/racheltits03.png"
        pause .04
        "medbay/racheltits04.png"
        pause .04
        "medbay/racheltits05.png"
        pause .04
        "medbay/racheltits06.png"
        pause .04
        "medbay/racheltits07.png"
        pause .04
        "medbay/racheltits08.png"
        pause .04
        "medbay/racheltits09.png"
        pause .04
        "medbay/racheltits08.png"
        pause .04
        "medbay/racheltits07.png"
        pause .04
        "medbay/racheltits06.png"
        pause .04
        "medbay/racheltits05.png"
        pause .04
        "medbay/racheltits04.png"
        pause .04
        "medbay/racheltits03.png"
        pause .04
        "medbay/racheltits02.png"
        pause .04
        "medbay/racheltits01.png"
        pause .04
        repeat
        
    transform rachelslap:
        "medbay/tarapanties03.png" with dissolve
        pause .75
        "medbay/tarapanties03b.png"
        pause .19
        "medbay/tarapanties03.png" with dissolve
        pause .75
        "medbay/tarapanties03c.png"
        pause .19
        repeat

    transform rachelblow:
        "medbay/rachelblowb02.png"
        pause .08
        "medbay/rachelblowb03.png"
        pause .04
        "medbay/rachelblowb04.png"
        pause .04
        "medbay/rachelblowb05.png"
        pause .04
        "medbay/rachelblowb06.png"
        pause .04
        "medbay/rachelblowb07.png"
        pause .04
        "medbay/rachelblowb08.png"
        pause .04
        "medbay/rachelblowb09.png"
        pause .04
        "medbay/rachelblowb10.png"
        pause .04
        "medbay/rachelblowb11.png"
        pause .04
        "medbay/rachelblowb12.png"
        pause .04
        "medbay/rachelblowb13.png"
        pause .04
        "medbay/rachelblowb14.png"
        pause .04
        "medbay/rachelblowb15.png"
        pause .04
        "medbay/rachelblowb16.png"
        pause .04
        "medbay/rachelblowb17.png"
        pause .04
        "medbay/rachelblowb18.png"
        pause .04
        "medbay/rachelblowb19.png"
        pause .04
        "medbay/rachelblowb20.png"
        pause .04
        "medbay/rachelblowb21.png"
        pause .04
        "medbay/rachelblowb22.png"
        pause .04
        "medbay/rachelblowb21.png"
        pause .04
        "medbay/rachelblowb20.png"
        pause .04
        "medbay/rachelblowb19.png"
        pause .04
        "medbay/rachelblowb18.png"
        pause .04
        "medbay/rachelblowb17.png"
        pause .04
        "medbay/rachelblowb16.png"
        pause .04
        "medbay/rachelblowb15.png"
        pause .04
        "medbay/rachelblowb14.png"
        pause .04
        "medbay/rachelblowb13.png"
        pause .04
        "medbay/rachelblowb12.png"
        pause .04
        "medbay/rachelblowb11.png"
        pause .04
        "medbay/rachelblowb10.png"
        pause .04
        "medbay/rachelblowb09.png"
        pause .04
        "medbay/rachelblowb08.png"
        pause .04
        "medbay/rachelblowb07.png"
        pause .04
        "medbay/rachelblowb06.png"
        pause .04
        "medbay/rachelblowb05.png"
        pause .04
        "medbay/rachelblowb04.png"
        pause .04
        "medbay/rachelblowb03.png"
        pause .04
        repeat
    
    transform angiewalk:
        "Bedroom/angiewalk00.png"
        pause 0.04
        "Bedroom/angiewalk01.png"
        pause 0.04
        "Bedroom/angiewalk02.png"
        pause 0.04
        "Bedroom/angiewalk03.png"
        pause 0.04
        "Bedroom/angiewalk04.png"
        pause 0.04
        "Bedroom/angiewalk05.png"
        pause 0.04
        "Bedroom/angiewalk06.png"
        pause 0.04
        "Bedroom/angiewalk07.png"
        pause 0.04
        "Bedroom/angiewalk08.png"
        pause 0.04
        "Bedroom/angiewalk09.png"
        pause 0.04
        "Bedroom/angiewalk10.png"
        pause 0.04
        "Bedroom/angiewalk11.png"
        pause 0.04
        "Bedroom/angiewalk12.png"
        pause 0.04
        "Bedroom/angiewalk13.png"
        pause 0.04
        "Bedroom/angiewalk14.png"
        pause 0.04
        "Bedroom/angiewalk15.png"
        pause 0.04
        "Bedroom/angiewalk16.png"
        pause 0.04
        "Bedroom/angiewalk17.png"
        pause 0.04
        "Bedroom/angiewalk18.png"
        pause 0.04
        "Bedroom/angiewalk19.png"
        pause 0.04
        "Bedroom/angiewalk20.png"
        pause 0.04
        "Bedroom/angiewalk21.png"
        pause 0.04
        "Bedroom/angiewalk22.png"
        pause 0.04
        "Bedroom/angiewalk23.png"
        pause 0.04
        "Bedroom/angiewalk24.png"
        pause 0.04
        "Bedroom/angiewalk25.png"
        pause 0.04
        "Bedroom/angiewalk26.png"
        pause 0.04
        "Bedroom/angiewalk27.png"
        pause 0.04
        "Bedroom/angiewalk28.png"
        pause 0.04
        "Bedroom/angiewalk29.png"
        pause 0.04
        "Bedroom/angiewalk30.png"
        pause 0.04
        repeat

    transform debrawalk:
        "Bedroom/debrawalk00.png"
        pause 0.04
        "Bedroom/debrawalk01.png"
        pause 0.04
        "Bedroom/debrawalk02.png"
        pause 0.04
        "Bedroom/debrawalk03.png"
        pause 0.04
        "Bedroom/debrawalk04.png"
        pause 0.04
        "Bedroom/debrawalk05.png"
        pause 0.04
        "Bedroom/debrawalk06.png"
        pause 0.04
        "Bedroom/debrawalk07.png"
        pause 0.04
        "Bedroom/debrawalk08.png"
        pause 0.04
        "Bedroom/debrawalk09.png"
        pause 0.04
        "Bedroom/debrawalk10.png"
        pause 0.04
        "Bedroom/debrawalk11.png"
        pause 0.04
        "Bedroom/debrawalk12.png"
        pause 0.04
        "Bedroom/debrawalk13.png"
        pause 0.04
        "Bedroom/debrawalk14.png"
        pause 0.04
        "Bedroom/debrawalk15.png"
        pause 0.04
        "Bedroom/debrawalk16.png"
        pause 0.04
        "Bedroom/debrawalk17.png"
        pause 0.04
        "Bedroom/debrawalk18.png"
        pause 0.04
        "Bedroom/debrawalk19.png"
        pause 0.04
        "Bedroom/debrawalk20.png"
        pause 0.04
        "Bedroom/debrawalk21.png"
        pause 0.04
        "Bedroom/debrawalk22.png"
        pause 0.04
        "Bedroom/debrawalk23.png"
        pause 0.04
        "Bedroom/debrawalk24.png"
        pause 0.04
        "Bedroom/debrawalk25.png"
        pause 0.04
        "Bedroom/debrawalk26.png"
        pause 0.04
        "Bedroom/debrawalk27.png"
        pause 0.04
        "Bedroom/debrawalk28.png"
        pause 0.04
        "Bedroom/debrawalk29.png"
        pause 0.04
        "Bedroom/debrawalk30.png"
        pause 0.04
        repeat

    transform lenawalk:
        "Bedroom/lenawalk00.png"
        pause 0.04
        "Bedroom/lenawalk01.png"
        pause 0.04
        "Bedroom/lenawalk02.png"
        pause 0.04
        "Bedroom/lenawalk03.png"
        pause 0.04
        "Bedroom/lenawalk04.png"
        pause 0.04
        "Bedroom/lenawalk05.png"
        pause 0.04
        "Bedroom/lenawalk06.png"
        pause 0.04
        "Bedroom/lenawalk07.png"
        pause 0.04
        "Bedroom/lenawalk08.png"
        pause 0.04
        "Bedroom/lenawalk09.png"
        pause 0.04
        "Bedroom/lenawalk10.png"
        pause 0.04
        "Bedroom/lenawalk11.png"
        pause 0.04
        "Bedroom/lenawalk12.png"
        pause 0.04
        "Bedroom/lenawalk13.png"
        pause 0.04
        "Bedroom/lenawalk14.png"
        pause 0.04
        "Bedroom/lenawalk15.png"
        pause 0.04
        "Bedroom/lenawalk16.png"
        pause 0.04
        "Bedroom/lenawalk17.png"
        pause 0.04
        "Bedroom/lenawalk18.png"
        pause 0.04
        "Bedroom/lenawalk19.png"
        pause 0.04
        "Bedroom/lenawalk20.png"
        pause 0.04
        "Bedroom/lenawalk21.png"
        pause 0.04
        "Bedroom/lenawalk22.png"
        pause 0.04
        "Bedroom/lenawalk23.png"
        pause 0.04
        "Bedroom/lenawalk24.png"
        pause 0.04
        "Bedroom/lenawalk25.png"
        pause 0.04
        "Bedroom/lenawalk26.png"
        pause 0.04
        "Bedroom/lenawalk27.png"
        pause 0.04
        "Bedroom/lenawalk28.png"
        pause 0.04
        "Bedroom/lenawalk29.png"
        pause 0.04
        "Bedroom/lenawalk30.png"
        pause 0.04
        repeat

    transform lauriewalk:
        "Bedroom/lauriewalk00.png"
        pause 0.04
        "Bedroom/lauriewalk01.png"
        pause 0.04
        "Bedroom/lauriewalk02.png"
        pause 0.04
        "Bedroom/lauriewalk03.png"
        pause 0.04
        "Bedroom/lauriewalk04.png"
        pause 0.04
        "Bedroom/lauriewalk05.png"
        pause 0.04
        "Bedroom/lauriewalk06.png"
        pause 0.04
        "Bedroom/lauriewalk07.png"
        pause 0.04
        "Bedroom/lauriewalk08.png"
        pause 0.04
        "Bedroom/lauriewalk09.png"
        pause 0.04
        "Bedroom/lauriewalk10.png"
        pause 0.04
        "Bedroom/lauriewalk11.png"
        pause 0.04
        "Bedroom/lauriewalk12.png"
        pause 0.04
        "Bedroom/lauriewalk13.png"
        pause 0.04
        "Bedroom/lauriewalk14.png"
        pause 0.04
        "Bedroom/lauriewalk15.png"
        pause 0.04
        "Bedroom/lauriewalk16.png"
        pause 0.04
        "Bedroom/lauriewalk17.png"
        pause 0.04
        "Bedroom/lauriewalk18.png"
        pause 0.04
        "Bedroom/lauriewalk19.png"
        pause 0.04
        "Bedroom/lauriewalk20.png"
        pause 0.04
        "Bedroom/lauriewalk21.png"
        pause 0.04
        "Bedroom/lauriewalk22.png"
        pause 0.04
        "Bedroom/lauriewalk23.png"
        pause 0.04
        "Bedroom/lauriewalk24.png"
        pause 0.04
        "Bedroom/lauriewalk25.png"
        pause 0.04
        "Bedroom/lauriewalk26.png"
        pause 0.04
        "Bedroom/lauriewalk27.png"
        pause 0.04
        "Bedroom/lauriewalk28.png"
        pause 0.04
        "Bedroom/lauriewalk29.png"
        pause 0.04
        "Bedroom/lauriewalk30.png"
        pause 0.04
        repeat

    transform michikowalk:
        "Bedroom/michikowalk00.png"
        pause 0.04
        "Bedroom/michikowalk01.png"
        pause 0.04
        "Bedroom/michikowalk02.png"
        pause 0.04
        "Bedroom/michikowalk03.png"
        pause 0.04
        "Bedroom/michikowalk04.png"
        pause 0.04
        "Bedroom/michikowalk05.png"
        pause 0.04
        "Bedroom/michikowalk06.png"
        pause 0.04
        "Bedroom/michikowalk07.png"
        pause 0.04
        "Bedroom/michikowalk08.png"
        pause 0.04
        "Bedroom/michikowalk09.png"
        pause 0.04
        "Bedroom/michikowalk10.png"
        pause 0.04
        "Bedroom/michikowalk11.png"
        pause 0.04
        "Bedroom/michikowalk12.png"
        pause 0.04
        "Bedroom/michikowalk13.png"
        pause 0.04
        "Bedroom/michikowalk14.png"
        pause 0.04
        "Bedroom/michikowalk15.png"
        pause 0.04
        "Bedroom/michikowalk16.png"
        pause 0.04
        "Bedroom/michikowalk17.png"
        pause 0.04
        "Bedroom/michikowalk18.png"
        pause 0.04
        "Bedroom/michikowalk19.png"
        pause 0.04
        "Bedroom/michikowalk20.png"
        pause 0.04
        "Bedroom/michikowalk21.png"
        pause 0.04
        "Bedroom/michikowalk22.png"
        pause 0.04
        "Bedroom/michikowalk23.png"
        pause 0.04
        "Bedroom/michikowalk24.png"
        pause 0.04
        "Bedroom/michikowalk25.png"
        pause 0.04
        "Bedroom/michikowalk26.png"
        pause 0.04
        "Bedroom/michikowalk27.png"
        pause 0.04
        "Bedroom/michikowalk28.png"
        pause 0.04
        "Bedroom/michikowalk29.png"
        pause 0.04
        "Bedroom/michikowalk30.png"
        pause 0.04
        repeat

    transform rubywalk:
        "Bedroom/rubywalk00.png"
        pause 0.04
        "Bedroom/rubywalk01.png"
        pause 0.04
        "Bedroom/rubywalk02.png"
        pause 0.04
        "Bedroom/rubywalk03.png"
        pause 0.04
        "Bedroom/rubywalk04.png"
        pause 0.04
        "Bedroom/rubywalk05.png"
        pause 0.04
        "Bedroom/rubywalk06.png"
        pause 0.04
        "Bedroom/rubywalk07.png"
        pause 0.04
        "Bedroom/rubywalk08.png"
        pause 0.04
        "Bedroom/rubywalk09.png"
        pause 0.04
        "Bedroom/rubywalk10.png"
        pause 0.04
        "Bedroom/rubywalk11.png"
        pause 0.04
        "Bedroom/rubywalk12.png"
        pause 0.04
        "Bedroom/rubywalk13.png"
        pause 0.04
        "Bedroom/rubywalk14.png"
        pause 0.04
        "Bedroom/rubywalk15.png"
        pause 0.04
        "Bedroom/rubywalk16.png"
        pause 0.04
        "Bedroom/rubywalk17.png"
        pause 0.04
        "Bedroom/rubywalk18.png"
        pause 0.04
        "Bedroom/rubywalk19.png"
        pause 0.04
        "Bedroom/rubywalk20.png"
        pause 0.04
        "Bedroom/rubywalk21.png"
        pause 0.04
        "Bedroom/rubywalk22.png"
        pause 0.04
        "Bedroom/rubywalk23.png"
        pause 0.04
        "Bedroom/rubywalk24.png"
        pause 0.04
        "Bedroom/rubywalk25.png"
        pause 0.04
        "Bedroom/rubywalk26.png"
        pause 0.04
        "Bedroom/rubywalk27.png"
        pause 0.04
        "Bedroom/rubywalk28.png"
        pause 0.04
        "Bedroom/rubywalk29.png"
        pause 0.04
        "Bedroom/rubywalk30.png"
        pause 0.04
        repeat

    transform gwenwalk:
        "Bedroom/gwenwalk00.png"
        pause 0.04
        "Bedroom/gwenwalk01.png"
        pause 0.04
        "Bedroom/gwenwalk02.png"
        pause 0.04
        "Bedroom/gwenwalk03.png"
        pause 0.04
        "Bedroom/gwenwalk04.png"
        pause 0.04
        "Bedroom/gwenwalk05.png"
        pause 0.04
        "Bedroom/gwenwalk06.png"
        pause 0.04
        "Bedroom/gwenwalk07.png"
        pause 0.04
        "Bedroom/gwenwalk08.png"
        pause 0.04
        "Bedroom/gwenwalk09.png"
        pause 0.04
        "Bedroom/gwenwalk10.png"
        pause 0.04
        "Bedroom/gwenwalk11.png"
        pause 0.04
        "Bedroom/gwenwalk12.png"
        pause 0.04
        "Bedroom/gwenwalk13.png"
        pause 0.04
        "Bedroom/gwenwalk14.png"
        pause 0.04
        "Bedroom/gwenwalk15.png"
        pause 0.04
        "Bedroom/gwenwalk16.png"
        pause 0.04
        "Bedroom/gwenwalk17.png"
        pause 0.04
        "Bedroom/gwenwalk18.png"
        pause 0.04
        "Bedroom/gwenwalk19.png"
        pause 0.04
        "Bedroom/gwenwalk20.png"
        pause 0.04
        "Bedroom/gwenwalk21.png"
        pause 0.04
        "Bedroom/gwenwalk22.png"
        pause 0.04
        "Bedroom/gwenwalk23.png"
        pause 0.04
        "Bedroom/gwenwalk24.png"
        pause 0.04
        "Bedroom/gwenwalk25.png"
        pause 0.04
        "Bedroom/gwenwalk26.png"
        pause 0.04
        "Bedroom/gwenwalk27.png"
        pause 0.04
        "Bedroom/gwenwalk28.png"
        pause 0.04
        "Bedroom/gwenwalk29.png"
        pause 0.04
        "Bedroom/gwenwalk30.png"
        pause 0.04
        repeat

    transform clarawalk:
        "Bedroom/clarawalk00.png"
        pause 0.04
        "Bedroom/clarawalk01.png"
        pause 0.04
        "Bedroom/clarawalk02.png"
        pause 0.04
        "Bedroom/clarawalk03.png"
        pause 0.04
        "Bedroom/clarawalk04.png"
        pause 0.04
        "Bedroom/clarawalk05.png"
        pause 0.04
        "Bedroom/clarawalk06.png"
        pause 0.04
        "Bedroom/clarawalk07.png"
        pause 0.04
        "Bedroom/clarawalk08.png"
        pause 0.04
        "Bedroom/clarawalk09.png"
        pause 0.04
        "Bedroom/clarawalk10.png"
        pause 0.04
        "Bedroom/clarawalk11.png"
        pause 0.04
        "Bedroom/clarawalk12.png"
        pause 0.04
        "Bedroom/clarawalk13.png"
        pause 0.04
        "Bedroom/clarawalk14.png"
        pause 0.04
        "Bedroom/clarawalk15.png"
        pause 0.04
        "Bedroom/clarawalk16.png"
        pause 0.04
        "Bedroom/clarawalk17.png"
        pause 0.04
        "Bedroom/clarawalk18.png"
        pause 0.04
        "Bedroom/clarawalk19.png"
        pause 0.04
        "Bedroom/clarawalk20.png"
        pause 0.04
        "Bedroom/clarawalk21.png"
        pause 0.04
        "Bedroom/clarawalk22.png"
        pause 0.04
        "Bedroom/clarawalk23.png"
        pause 0.04
        "Bedroom/clarawalk24.png"
        pause 0.04
        "Bedroom/clarawalk25.png"
        pause 0.04
        "Bedroom/clarawalk26.png"
        pause 0.04
        "Bedroom/clarawalk27.png"
        pause 0.04
        "Bedroom/clarawalk28.png"
        pause 0.04
        "Bedroom/clarawalk29.png"
        pause 0.04
        "Bedroom/clarawalk30.png"
        pause 0.04
        repeat
        
    transform marniewalk:
        "Bedroom/marniewalk00.png"
        pause 0.04
        "Bedroom/marniewalk01.png"
        pause 0.04
        "Bedroom/marniewalk02.png"
        pause 0.04
        "Bedroom/marniewalk03.png"
        pause 0.04
        "Bedroom/marniewalk04.png"
        pause 0.04
        "Bedroom/marniewalk05.png"
        pause 0.04
        "Bedroom/marniewalk06.png"
        pause 0.04
        "Bedroom/marniewalk07.png"
        pause 0.04
        "Bedroom/marniewalk08.png"
        pause 0.04
        "Bedroom/marniewalk09.png"
        pause 0.04
        "Bedroom/marniewalk10.png"
        pause 0.04
        "Bedroom/marniewalk11.png"
        pause 0.04
        "Bedroom/marniewalk12.png"
        pause 0.04
        "Bedroom/marniewalk13.png"
        pause 0.04
        "Bedroom/marniewalk14.png"
        pause 0.04
        "Bedroom/marniewalk15.png"
        pause 0.04
        "Bedroom/marniewalk16.png"
        pause 0.04
        "Bedroom/marniewalk17.png"
        pause 0.04
        "Bedroom/marniewalk18.png"
        pause 0.04
        "Bedroom/marniewalk19.png"
        pause 0.04
        "Bedroom/marniewalk20.png"
        pause 0.04
        "Bedroom/marniewalk21.png"
        pause 0.04
        "Bedroom/marniewalk22.png"
        pause 0.04
        "Bedroom/marniewalk23.png"
        pause 0.04
        "Bedroom/marniewalk24.png"
        pause 0.04
        "Bedroom/marniewalk25.png"
        pause 0.04
        "Bedroom/marniewalk26.png"
        pause 0.04
        "Bedroom/marniewalk27.png"
        pause 0.04
        "Bedroom/marniewalk28.png"
        pause 0.04
        "Bedroom/marniewalk29.png"
        pause 0.04
        "Bedroom/marniewalk30.png"
        pause 0.04
        repeat
    
    transform melaniawalk:
        "Bedroom/melaniawalk00.png"
        pause 0.04
        "Bedroom/melaniawalk01.png"
        pause 0.04
        "Bedroom/melaniawalk02.png"
        pause 0.04
        "Bedroom/melaniawalk03.png"
        pause 0.04
        "Bedroom/melaniawalk04.png"
        pause 0.04
        "Bedroom/melaniawalk05.png"
        pause 0.04
        "Bedroom/melaniawalk06.png"
        pause 0.04
        "Bedroom/melaniawalk07.png"
        pause 0.04
        "Bedroom/melaniawalk08.png"
        pause 0.04
        "Bedroom/melaniawalk09.png"
        pause 0.04
        "Bedroom/melaniawalk10.png"
        pause 0.04
        "Bedroom/melaniawalk11.png"
        pause 0.04
        "Bedroom/melaniawalk12.png"
        pause 0.04
        "Bedroom/melaniawalk13.png"
        pause 0.04
        "Bedroom/melaniawalk14.png"
        pause 0.04
        "Bedroom/melaniawalk15.png"
        pause 0.04
        "Bedroom/melaniawalk16.png"
        pause 0.04
        "Bedroom/melaniawalk17.png"
        pause 0.04
        "Bedroom/melaniawalk18.png"
        pause 0.04
        "Bedroom/melaniawalk19.png"
        pause 0.04
        "Bedroom/melaniawalk20.png"
        pause 0.04
        "Bedroom/melaniawalk21.png"
        pause 0.04
        "Bedroom/melaniawalk22.png"
        pause 0.04
        "Bedroom/melaniawalk23.png"
        pause 0.04
        "Bedroom/melaniawalk24.png"
        pause 0.04
        "Bedroom/melaniawalk25.png"
        pause 0.04
        "Bedroom/melaniawalk26.png"
        pause 0.04
        "Bedroom/melaniawalk27.png"
        pause 0.04
        "Bedroom/melaniawalk28.png"
        pause 0.04
        "Bedroom/melaniawalk29.png"
        pause 0.04
        "Bedroom/melaniawalk30.png"
        pause 0.04
        repeat    

    transform amywalk:
        "Bedroom/amywalk00.png"
        pause 0.04
        "Bedroom/amywalk01.png"
        pause 0.04
        "Bedroom/amywalk02.png"
        pause 0.04
        "Bedroom/amywalk03.png"
        pause 0.04
        "Bedroom/amywalk04.png"
        pause 0.04
        "Bedroom/amywalk05.png"
        pause 0.04
        "Bedroom/amywalk06.png"
        pause 0.04
        "Bedroom/amywalk07.png"
        pause 0.04
        "Bedroom/amywalk08.png"
        pause 0.04
        "Bedroom/amywalk09.png"
        pause 0.04
        "Bedroom/amywalk10.png"
        pause 0.04
        "Bedroom/amywalk11.png"
        pause 0.04
        "Bedroom/amywalk12.png"
        pause 0.04
        "Bedroom/amywalk13.png"
        pause 0.04
        "Bedroom/amywalk14.png"
        pause 0.04
        "Bedroom/amywalk15.png"
        pause 0.04
        "Bedroom/amywalk16.png"
        pause 0.04
        "Bedroom/amywalk17.png"
        pause 0.04
        "Bedroom/amywalk18.png"
        pause 0.04
        "Bedroom/amywalk19.png"
        pause 0.04
        "Bedroom/amywalk20.png"
        pause 0.04
        "Bedroom/amywalk21.png"
        pause 0.04
        "Bedroom/amywalk22.png"
        pause 0.04
        "Bedroom/amywalk23.png"
        pause 0.04
        "Bedroom/amywalk24.png"
        pause 0.04
        "Bedroom/amywalk25.png"
        pause 0.04
        "Bedroom/amywalk26.png"
        pause 0.04
        "Bedroom/amywalk27.png"
        pause 0.04
        "Bedroom/amywalk28.png"
        pause 0.04
        "Bedroom/amywalk29.png"
        pause 0.04
        "Bedroom/amywalk30.png"
        pause 0.04
        repeat    
    
    transform pennywalk:
        "Bedroom/pennywalk00.png"
        pause 0.04
        "Bedroom/pennywalk01.png"
        pause 0.04
        "Bedroom/pennywalk02.png"
        pause 0.04
        "Bedroom/pennywalk03.png"
        pause 0.04
        "Bedroom/pennywalk04.png"
        pause 0.04
        "Bedroom/pennywalk05.png"
        pause 0.04
        "Bedroom/pennywalk06.png"
        pause 0.04
        "Bedroom/pennywalk07.png"
        pause 0.04
        "Bedroom/pennywalk08.png"
        pause 0.04
        "Bedroom/pennywalk09.png"
        pause 0.04
        "Bedroom/pennywalk10.png"
        pause 0.04
        "Bedroom/pennywalk11.png"
        pause 0.04
        "Bedroom/pennywalk12.png"
        pause 0.04
        "Bedroom/pennywalk13.png"
        pause 0.04
        "Bedroom/pennywalk14.png"
        pause 0.04
        "Bedroom/pennywalk15.png"
        pause 0.04
        "Bedroom/pennywalk16.png"
        pause 0.04
        "Bedroom/pennywalk17.png"
        pause 0.04
        "Bedroom/pennywalk18.png"
        pause 0.04
        "Bedroom/pennywalk19.png"
        pause 0.04
        "Bedroom/pennywalk20.png"
        pause 0.04
        "Bedroom/pennywalk21.png"
        pause 0.04
        "Bedroom/pennywalk22.png"
        pause 0.04
        "Bedroom/pennywalk23.png"
        pause 0.04
        "Bedroom/pennywalk24.png"
        pause 0.04
        "Bedroom/pennywalk25.png"
        pause 0.04
        "Bedroom/pennywalk26.png"
        pause 0.04
        "Bedroom/pennywalk27.png"
        pause 0.04
        "Bedroom/pennywalk28.png"
        pause 0.04
        "Bedroom/pennywalk29.png"
        pause 0.04
        "Bedroom/pennywalk30.png"
        pause 0.04
        repeat

    transform aylawalk:
        "Bedroom/aylawalk00.png"
        pause 0.04
        "Bedroom/aylawalk01.png"
        pause 0.04
        "Bedroom/aylawalk02.png"
        pause 0.04
        "Bedroom/aylawalk03.png"
        pause 0.04
        "Bedroom/aylawalk04.png"
        pause 0.04
        "Bedroom/aylawalk05.png"
        pause 0.04
        "Bedroom/aylawalk06.png"
        pause 0.04
        "Bedroom/aylawalk07.png"
        pause 0.04
        "Bedroom/aylawalk08.png"
        pause 0.04
        "Bedroom/aylawalk09.png"
        pause 0.04
        "Bedroom/aylawalk10.png"
        pause 0.04
        "Bedroom/aylawalk11.png"
        pause 0.04
        "Bedroom/aylawalk12.png"
        pause 0.04
        "Bedroom/aylawalk13.png"
        pause 0.04
        "Bedroom/aylawalk14.png"
        pause 0.04
        "Bedroom/aylawalk15.png"
        pause 0.04
        "Bedroom/aylawalk16.png"
        pause 0.04
        "Bedroom/aylawalk17.png"
        pause 0.04
        "Bedroom/aylawalk18.png"
        pause 0.04
        "Bedroom/aylawalk19.png"
        pause 0.04
        "Bedroom/aylawalk20.png"
        pause 0.04
        "Bedroom/aylawalk21.png"
        pause 0.04
        "Bedroom/aylawalk22.png"
        pause 0.04
        "Bedroom/aylawalk23.png"
        pause 0.04
        "Bedroom/aylawalk24.png"
        pause 0.04
        "Bedroom/aylawalk25.png"
        pause 0.04
        "Bedroom/aylawalk26.png"
        pause 0.04
        "Bedroom/aylawalk27.png"
        pause 0.04
        "Bedroom/aylawalk28.png"
        pause 0.04
        "Bedroom/aylawalk29.png"
        pause 0.04
        "Bedroom/aylawalk30.png"
        pause 0.04
        repeat

    transform tarawalk:
        "Bedroom/tarawalk00.png"
        pause 0.04
        "Bedroom/tarawalk01.png"
        pause 0.04
        "Bedroom/tarawalk02.png"
        pause 0.04
        "Bedroom/tarawalk03.png"
        pause 0.04
        "Bedroom/tarawalk04.png"
        pause 0.04
        "Bedroom/tarawalk05.png"
        pause 0.04
        "Bedroom/tarawalk06.png"
        pause 0.04
        "Bedroom/tarawalk07.png"
        pause 0.04
        "Bedroom/tarawalk08.png"
        pause 0.04
        "Bedroom/tarawalk09.png"
        pause 0.04
        "Bedroom/tarawalk10.png"
        pause 0.04
        "Bedroom/tarawalk11.png"
        pause 0.04
        "Bedroom/tarawalk12.png"
        pause 0.04
        "Bedroom/tarawalk13.png"
        pause 0.04
        "Bedroom/tarawalk14.png"
        pause 0.04
        "Bedroom/tarawalk15.png"
        pause 0.04
        "Bedroom/tarawalk16.png"
        pause 0.04
        "Bedroom/tarawalk17.png"
        pause 0.04
        "Bedroom/tarawalk18.png"
        pause 0.04
        "Bedroom/tarawalk19.png"
        pause 0.04
        "Bedroom/tarawalk20.png"
        pause 0.04
        "Bedroom/tarawalk21.png"
        pause 0.04
        "Bedroom/tarawalk22.png"
        pause 0.04
        "Bedroom/tarawalk23.png"
        pause 0.04
        "Bedroom/tarawalk24.png"
        pause 0.04
        "Bedroom/tarawalk25.png"
        pause 0.04
        "Bedroom/tarawalk26.png"
        pause 0.04
        "Bedroom/tarawalk27.png"
        pause 0.04
        "Bedroom/tarawalk28.png"
        pause 0.04
        "Bedroom/tarawalk29.png"
        pause 0.04
        "Bedroom/tarawalk30.png"
        pause 0.04
        repeat

    transform rachelwalk:
        "Bedroom/rachelwalk00.png"
        pause 0.04
        "Bedroom/rachelwalk01.png"
        pause 0.04
        "Bedroom/rachelwalk02.png"
        pause 0.04
        "Bedroom/rachelwalk03.png"
        pause 0.04
        "Bedroom/rachelwalk04.png"
        pause 0.04
        "Bedroom/rachelwalk05.png"
        pause 0.04
        "Bedroom/rachelwalk06.png"
        pause 0.04
        "Bedroom/rachelwalk07.png"
        pause 0.04
        "Bedroom/rachelwalk08.png"
        pause 0.04
        "Bedroom/rachelwalk09.png"
        pause 0.04
        "Bedroom/rachelwalk10.png"
        pause 0.04
        "Bedroom/rachelwalk11.png"
        pause 0.04
        "Bedroom/rachelwalk12.png"
        pause 0.04
        "Bedroom/rachelwalk13.png"
        pause 0.04
        "Bedroom/rachelwalk14.png"
        pause 0.04
        "Bedroom/rachelwalk15.png"
        pause 0.04
        "Bedroom/rachelwalk16.png"
        pause 0.04
        "Bedroom/rachelwalk17.png"
        pause 0.04
        "Bedroom/rachelwalk18.png"
        pause 0.04
        "Bedroom/rachelwalk19.png"
        pause 0.04
        "Bedroom/rachelwalk20.png"
        pause 0.04
        "Bedroom/rachelwalk21.png"
        pause 0.04
        "Bedroom/rachelwalk22.png"
        pause 0.04
        "Bedroom/rachelwalk23.png"
        pause 0.04
        "Bedroom/rachelwalk24.png"
        pause 0.04
        "Bedroom/rachelwalk25.png"
        pause 0.04
        "Bedroom/rachelwalk26.png"
        pause 0.04
        "Bedroom/rachelwalk27.png"
        pause 0.04
        "Bedroom/rachelwalk28.png"
        pause 0.04
        "Bedroom/rachelwalk29.png"
        pause 0.04
        "Bedroom/rachelwalk30.png"
        pause 0.04
        repeat

    transform barbarawalk:
        "Bedroom/barbarawalk00.png"
        pause 0.04
        "Bedroom/barbarawalk01.png"
        pause 0.04
        "Bedroom/barbarawalk02.png"
        pause 0.04
        "Bedroom/barbarawalk03.png"
        pause 0.04
        "Bedroom/barbarawalk04.png"
        pause 0.04
        "Bedroom/barbarawalk05.png"
        pause 0.04
        "Bedroom/barbarawalk06.png"
        pause 0.04
        "Bedroom/barbarawalk07.png"
        pause 0.04
        "Bedroom/barbarawalk08.png"
        pause 0.04
        "Bedroom/barbarawalk09.png"
        pause 0.04
        "Bedroom/barbarawalk10.png"
        pause 0.04
        "Bedroom/barbarawalk11.png"
        pause 0.04
        "Bedroom/barbarawalk12.png"
        pause 0.04
        "Bedroom/barbarawalk13.png"
        pause 0.04
        "Bedroom/barbarawalk14.png"
        pause 0.04
        "Bedroom/barbarawalk15.png"
        pause 0.04
        "Bedroom/barbarawalk16.png"
        pause 0.04
        "Bedroom/barbarawalk17.png"
        pause 0.04
        "Bedroom/barbarawalk18.png"
        pause 0.04
        "Bedroom/barbarawalk19.png"
        pause 0.04
        "Bedroom/barbarawalk20.png"
        pause 0.04
        "Bedroom/barbarawalk21.png"
        pause 0.04
        "Bedroom/barbarawalk22.png"
        pause 0.04
        "Bedroom/barbarawalk23.png"
        pause 0.04
        "Bedroom/barbarawalk24.png"
        pause 0.04
        "Bedroom/barbarawalk25.png"
        pause 0.04
        "Bedroom/barbarawalk26.png"
        pause 0.04
        "Bedroom/barbarawalk27.png"
        pause 0.04
        "Bedroom/barbarawalk28.png"
        pause 0.04
        "Bedroom/barbarawalk29.png"
        pause 0.04
        "Bedroom/barbarawalk30.png"
        pause 0.04
        repeat

    transform zarawalk:
        "Bedroom/zarawalk00.png"
        pause 0.04
        "Bedroom/zarawalk01.png"
        pause 0.04
        "Bedroom/zarawalk02.png"
        pause 0.04
        "Bedroom/zarawalk03.png"
        pause 0.04
        "Bedroom/zarawalk04.png"
        pause 0.04
        "Bedroom/zarawalk05.png"
        pause 0.04
        "Bedroom/zarawalk06.png"
        pause 0.04
        "Bedroom/zarawalk07.png"
        pause 0.04
        "Bedroom/zarawalk08.png"
        pause 0.04
        "Bedroom/zarawalk09.png"
        pause 0.04
        "Bedroom/zarawalk10.png"
        pause 0.04
        "Bedroom/zarawalk11.png"
        pause 0.04
        "Bedroom/zarawalk12.png"
        pause 0.04
        "Bedroom/zarawalk13.png"
        pause 0.04
        "Bedroom/zarawalk14.png"
        pause 0.04
        "Bedroom/zarawalk15.png"
        pause 0.04
        "Bedroom/zarawalk16.png"
        pause 0.04
        "Bedroom/zarawalk17.png"
        pause 0.04
        "Bedroom/zarawalk18.png"
        pause 0.04
        "Bedroom/zarawalk19.png"
        pause 0.04
        "Bedroom/zarawalk20.png"
        pause 0.04
        "Bedroom/zarawalk21.png"
        pause 0.04
        "Bedroom/zarawalk22.png"
        pause 0.04
        "Bedroom/zarawalk23.png"
        pause 0.04
        "Bedroom/zarawalk24.png"
        pause 0.04
        "Bedroom/zarawalk25.png"
        pause 0.04
        "Bedroom/zarawalk26.png"
        pause 0.04
        "Bedroom/zarawalk27.png"
        pause 0.04
        "Bedroom/zarawalk28.png"
        pause 0.04
        "Bedroom/zarawalk29.png"
        pause 0.04
        "Bedroom/zarawalk30.png"
        pause 0.04
        repeat

    transform cyrlwalk:
        "Bedroom/cyrlwalk00.png"
        pause 0.04
        "Bedroom/cyrlwalk01.png"
        pause 0.04
        "Bedroom/cyrlwalk02.png"
        pause 0.04
        "Bedroom/cyrlwalk03.png"
        pause 0.04
        "Bedroom/cyrlwalk04.png"
        pause 0.04
        "Bedroom/cyrlwalk05.png"
        pause 0.04
        "Bedroom/cyrlwalk06.png"
        pause 0.04
        "Bedroom/cyrlwalk07.png"
        pause 0.04
        "Bedroom/cyrlwalk08.png"
        pause 0.04
        "Bedroom/cyrlwalk09.png"
        pause 0.04
        "Bedroom/cyrlwalk10.png"
        pause 0.04
        "Bedroom/cyrlwalk11.png"
        pause 0.04
        "Bedroom/cyrlwalk12.png"
        pause 0.04
        "Bedroom/cyrlwalk13.png"
        pause 0.04
        "Bedroom/cyrlwalk14.png"
        pause 0.04
        "Bedroom/cyrlwalk15.png"
        pause 0.04
        "Bedroom/cyrlwalk16.png"
        pause 0.04
        "Bedroom/cyrlwalk17.png"
        pause 0.04
        "Bedroom/cyrlwalk18.png"
        pause 0.04
        "Bedroom/cyrlwalk19.png"
        pause 0.04
        "Bedroom/cyrlwalk20.png"
        pause 0.04
        "Bedroom/cyrlwalk21.png"
        pause 0.04
        "Bedroom/cyrlwalk22.png"
        pause 0.04
        "Bedroom/cyrlwalk23.png"
        pause 0.04
        "Bedroom/cyrlwalk24.png"
        pause 0.04
        "Bedroom/cyrlwalk25.png"
        pause 0.04
        "Bedroom/cyrlwalk26.png"
        pause 0.04
        "Bedroom/cyrlwalk27.png"
        pause 0.04
        "Bedroom/cyrlwalk28.png"
        pause 0.04
        "Bedroom/cyrlwalk29.png"
        pause 0.04
        "Bedroom/cyrlwalk30.png"
        pause 0.04
        repeat

    transform bellawalk:
        "Bedroom/bellawalk00.png"
        pause 0.04
        "Bedroom/bellawalk01.png"
        pause 0.04
        "Bedroom/bellawalk02.png"
        pause 0.04
        "Bedroom/bellawalk03.png"
        pause 0.04
        "Bedroom/bellawalk04.png"
        pause 0.04
        "Bedroom/bellawalk05.png"
        pause 0.04
        "Bedroom/bellawalk06.png"
        pause 0.04
        "Bedroom/bellawalk07.png"
        pause 0.04
        "Bedroom/bellawalk08.png"
        pause 0.04
        "Bedroom/bellawalk09.png"
        pause 0.04
        "Bedroom/bellawalk10.png"
        pause 0.04
        "Bedroom/bellawalk11.png"
        pause 0.04
        "Bedroom/bellawalk12.png"
        pause 0.04
        "Bedroom/bellawalk13.png"
        pause 0.04
        "Bedroom/bellawalk14.png"
        pause 0.04
        "Bedroom/bellawalk15.png"
        pause 0.04
        "Bedroom/bellawalk16.png"
        pause 0.04
        "Bedroom/bellawalk17.png"
        pause 0.04
        "Bedroom/bellawalk18.png"
        pause 0.04
        "Bedroom/bellawalk19.png"
        pause 0.04
        "Bedroom/bellawalk20.png"
        pause 0.04
        "Bedroom/bellawalk21.png"
        pause 0.04
        "Bedroom/bellawalk22.png"
        pause 0.04
        "Bedroom/bellawalk23.png"
        pause 0.04
        "Bedroom/bellawalk24.png"
        pause 0.04
        "Bedroom/bellawalk25.png"
        pause 0.04
        "Bedroom/bellawalk26.png"
        pause 0.04
        "Bedroom/bellawalk27.png"
        pause 0.04
        "Bedroom/bellawalk28.png"
        pause 0.04
        "Bedroom/bellawalk29.png"
        pause 0.04
        "Bedroom/bellawalk30.png"
        pause 0.04
        repeat

    transform sukiwalk:
        "Bedroom/sukiwalk00.png"
        pause 0.04
        "Bedroom/sukiwalk01.png"
        pause 0.04
        "Bedroom/sukiwalk02.png"
        pause 0.04
        "Bedroom/sukiwalk03.png"
        pause 0.04
        "Bedroom/sukiwalk04.png"
        pause 0.04
        "Bedroom/sukiwalk05.png"
        pause 0.04
        "Bedroom/sukiwalk06.png"
        pause 0.04
        "Bedroom/sukiwalk07.png"
        pause 0.04
        "Bedroom/sukiwalk08.png"
        pause 0.04
        "Bedroom/sukiwalk09.png"
        pause 0.04
        "Bedroom/sukiwalk10.png"
        pause 0.04
        "Bedroom/sukiwalk11.png"
        pause 0.04
        "Bedroom/sukiwalk12.png"
        pause 0.04
        "Bedroom/sukiwalk13.png"
        pause 0.04
        "Bedroom/sukiwalk14.png"
        pause 0.04
        "Bedroom/sukiwalk15.png"
        pause 0.04
        "Bedroom/sukiwalk16.png"
        pause 0.04
        "Bedroom/sukiwalk17.png"
        pause 0.04
        "Bedroom/sukiwalk18.png"
        pause 0.04
        "Bedroom/sukiwalk19.png"
        pause 0.04
        "Bedroom/sukiwalk20.png"
        pause 0.04
        "Bedroom/sukiwalk21.png"
        pause 0.04
        "Bedroom/sukiwalk22.png"
        pause 0.04
        "Bedroom/sukiwalk23.png"
        pause 0.04
        "Bedroom/sukiwalk24.png"
        pause 0.04
        "Bedroom/sukiwalk25.png"
        pause 0.04
        "Bedroom/sukiwalk26.png"
        pause 0.04
        "Bedroom/sukiwalk27.png"
        pause 0.04
        "Bedroom/sukiwalk28.png"
        pause 0.04
        "Bedroom/sukiwalk29.png"
        pause 0.04
        "Bedroom/sukiwalk30.png"
        pause 0.04
        repeat

    transform widowwalk:
        "Bedroom/widowwalk00.png"
        pause 0.04
        "Bedroom/widowwalk01.png"
        pause 0.04
        "Bedroom/widowwalk02.png"
        pause 0.04
        "Bedroom/widowwalk03.png"
        pause 0.04
        "Bedroom/widowwalk04.png"
        pause 0.04
        "Bedroom/widowwalk05.png"
        pause 0.04
        "Bedroom/widowwalk06.png"
        pause 0.04
        "Bedroom/widowwalk07.png"
        pause 0.04
        "Bedroom/widowwalk08.png"
        pause 0.04
        "Bedroom/widowwalk09.png"
        pause 0.04
        "Bedroom/widowwalk10.png"
        pause 0.04
        "Bedroom/widowwalk11.png"
        pause 0.04
        "Bedroom/widowwalk12.png"
        pause 0.04
        "Bedroom/widowwalk13.png"
        pause 0.04
        "Bedroom/widowwalk14.png"
        pause 0.04
        "Bedroom/widowwalk15.png"
        pause 0.04
        "Bedroom/widowwalk16.png"
        pause 0.04
        "Bedroom/widowwalk17.png"
        pause 0.04
        "Bedroom/widowwalk18.png"
        pause 0.04
        "Bedroom/widowwalk19.png"
        pause 0.04
        "Bedroom/widowwalk20.png"
        pause 0.04
        "Bedroom/widowwalk21.png"
        pause 0.04
        "Bedroom/widowwalk22.png"
        pause 0.04
        "Bedroom/widowwalk23.png"
        pause 0.04
        "Bedroom/widowwalk24.png"
        pause 0.04
        "Bedroom/widowwalk25.png"
        pause 0.04
        "Bedroom/widowwalk26.png"
        pause 0.04
        "Bedroom/widowwalk27.png"
        pause 0.04
        "Bedroom/widowwalk28.png"
        pause 0.04
        "Bedroom/widowwalk29.png"
        pause 0.04
        "Bedroom/widowwalk30.png"
        pause 0.04
        repeat

    transform nancywalk:
        "Bedroom/nancywalk00.png"
        pause 0.04
        "Bedroom/nancywalk01.png"
        pause 0.04
        "Bedroom/nancywalk02.png"
        pause 0.04
        "Bedroom/nancywalk03.png"
        pause 0.04
        "Bedroom/nancywalk04.png"
        pause 0.04
        "Bedroom/nancywalk05.png"
        pause 0.04
        "Bedroom/nancywalk06.png"
        pause 0.04
        "Bedroom/nancywalk07.png"
        pause 0.04
        "Bedroom/nancywalk08.png"
        pause 0.04
        "Bedroom/nancywalk09.png"
        pause 0.04
        "Bedroom/nancywalk10.png"
        pause 0.04
        "Bedroom/nancywalk11.png"
        pause 0.04
        "Bedroom/nancywalk12.png"
        pause 0.04
        "Bedroom/nancywalk13.png"
        pause 0.04
        "Bedroom/nancywalk14.png"
        pause 0.04
        "Bedroom/nancywalk15.png"
        pause 0.04
        "Bedroom/nancywalk16.png"
        pause 0.04
        "Bedroom/nancywalk17.png"
        pause 0.04
        "Bedroom/nancywalk18.png"
        pause 0.04
        "Bedroom/nancywalk19.png"
        pause 0.04
        "Bedroom/nancywalk20.png"
        pause 0.04
        "Bedroom/nancywalk21.png"
        pause 0.04
        "Bedroom/nancywalk22.png"
        pause 0.04
        "Bedroom/nancywalk23.png"
        pause 0.04
        "Bedroom/nancywalk24.png"
        pause 0.04
        "Bedroom/nancywalk25.png"
        pause 0.04
        "Bedroom/nancywalk26.png"
        pause 0.04
        "Bedroom/nancywalk27.png"
        pause 0.04
        "Bedroom/nancywalk28.png"
        pause 0.04
        "Bedroom/nancywalk29.png"
        pause 0.04
        "Bedroom/nancywalk30.png"
        pause 0.04
        repeat

    transform ivankawalk:
        "Bedroom/ivankawalk00.png"
        pause 0.04
        "Bedroom/ivankawalk01.png"
        pause 0.04
        "Bedroom/ivankawalk02.png"
        pause 0.04
        "Bedroom/ivankawalk03.png"
        pause 0.04
        "Bedroom/ivankawalk04.png"
        pause 0.04
        "Bedroom/ivankawalk05.png"
        pause 0.04
        "Bedroom/ivankawalk06.png"
        pause 0.04
        "Bedroom/ivankawalk07.png"
        pause 0.04
        "Bedroom/ivankawalk08.png"
        pause 0.04
        "Bedroom/ivankawalk09.png"
        pause 0.04
        "Bedroom/ivankawalk10.png"
        pause 0.04
        "Bedroom/ivankawalk11.png"
        pause 0.04
        "Bedroom/ivankawalk12.png"
        pause 0.04
        "Bedroom/ivankawalk13.png"
        pause 0.04
        "Bedroom/ivankawalk14.png"
        pause 0.04
        "Bedroom/ivankawalk15.png"
        pause 0.04
        "Bedroom/ivankawalk16.png"
        pause 0.04
        "Bedroom/ivankawalk17.png"
        pause 0.04
        "Bedroom/ivankawalk18.png"
        pause 0.04
        "Bedroom/ivankawalk19.png"
        pause 0.04
        "Bedroom/ivankawalk20.png"
        pause 0.04
        "Bedroom/ivankawalk21.png"
        pause 0.04
        "Bedroom/ivankawalk22.png"
        pause 0.04
        "Bedroom/ivankawalk23.png"
        pause 0.04
        "Bedroom/ivankawalk24.png"
        pause 0.04
        "Bedroom/ivankawalk25.png"
        pause 0.04
        "Bedroom/ivankawalk26.png"
        pause 0.04
        "Bedroom/ivankawalk27.png"
        pause 0.04
        "Bedroom/ivankawalk28.png"
        pause 0.04
        "Bedroom/ivankawalk29.png"
        pause 0.04
        "Bedroom/ivankawalk30.png"
        pause 0.04
        repeat

    transform taylorwalk:
        "Bedroom/taylorwalk00.png"
        pause 0.04
        "Bedroom/taylorwalk01.png"
        pause 0.04
        "Bedroom/taylorwalk02.png"
        pause 0.04
        "Bedroom/taylorwalk03.png"
        pause 0.04
        "Bedroom/taylorwalk04.png"
        pause 0.04
        "Bedroom/taylorwalk05.png"
        pause 0.04
        "Bedroom/taylorwalk06.png"
        pause 0.04
        "Bedroom/taylorwalk07.png"
        pause 0.04
        "Bedroom/taylorwalk08.png"
        pause 0.04
        "Bedroom/taylorwalk09.png"
        pause 0.04
        "Bedroom/taylorwalk10.png"
        pause 0.04
        "Bedroom/taylorwalk11.png"
        pause 0.04
        "Bedroom/taylorwalk12.png"
        pause 0.04
        "Bedroom/taylorwalk13.png"
        pause 0.04
        "Bedroom/taylorwalk14.png"
        pause 0.04
        "Bedroom/taylorwalk15.png"
        pause 0.04
        "Bedroom/taylorwalk16.png"
        pause 0.04
        "Bedroom/taylorwalk17.png"
        pause 0.04
        "Bedroom/taylorwalk18.png"
        pause 0.04
        "Bedroom/taylorwalk19.png"
        pause 0.04
        "Bedroom/taylorwalk20.png"
        pause 0.04
        "Bedroom/taylorwalk21.png"
        pause 0.04
        "Bedroom/taylorwalk22.png"
        pause 0.04
        "Bedroom/taylorwalk23.png"
        pause 0.04
        "Bedroom/taylorwalk24.png"
        pause 0.04
        "Bedroom/taylorwalk25.png"
        pause 0.04
        "Bedroom/taylorwalk26.png"
        pause 0.04
        "Bedroom/taylorwalk27.png"
        pause 0.04
        "Bedroom/taylorwalk28.png"
        pause 0.04
        "Bedroom/taylorwalk29.png"
        pause 0.04
        "Bedroom/taylorwalk30.png"
        pause 0.04
        repeat
            
    transform wendywalk:
        "v06/wendywalk00.png"
        pause 0.04
        "v06/wendywalk01.png"
        pause 0.04
        "v06/wendywalk02.png"
        pause 0.04
        "v06/wendywalk03.png"
        pause 0.04
        "v06/wendywalk04.png"
        pause 0.04
        "v06/wendywalk05.png"
        pause 0.04
        "v06/wendywalk06.png"
        pause 0.04
        "v06/wendywalk07.png"
        pause 0.04
        "v06/wendywalk08.png"
        pause 0.04
        "v06/wendywalk09.png"
        pause 0.04
        "v06/wendywalk10.png"
        pause 0.04
        "v06/wendywalk11.png"
        pause 0.04
        "v06/wendywalk12.png"
        pause 0.04
        "v06/wendywalk13.png"
        pause 0.04
        "v06/wendywalk14.png"
        pause 0.04
        "v06/wendywalk15.png"
        pause 0.04
        "v06/wendywalk16.png"
        pause 0.04
        "v06/wendywalk17.png"
        pause 0.04
        "v06/wendywalk18.png"
        pause 0.04
        "v06/wendywalk19.png"
        pause 0.04
        "v06/wendywalk20.png"
        pause 0.04
        "v06/wendywalk21.png"
        pause 0.04
        "v06/wendywalk22.png"
        pause 0.04
        "v06/wendywalk23.png"
        pause 0.04
        "v06/wendywalk24.png"
        pause 0.04
        "v06/wendywalk25.png"
        pause 0.04
        "v06/wendywalk26.png"
        pause 0.04
        "v06/wendywalk27.png"
        pause 0.04
        "v06/wendywalk28.png"
        pause 0.04
        "v06/wendywalk29.png"
        pause 0.04
        "v06/wendywalk30.png"
        pause 0.04
        repeat
            
    transform kimberlywalk:
        "v07/guilfoolwalk00.png"
        pause 0.04
        "v07/guilfoolwalk01.png"
        pause 0.04
        "v07/guilfoolwalk02.png"
        pause 0.04
        "v07/guilfoolwalk03.png"
        pause 0.04
        "v07/guilfoolwalk04.png"
        pause 0.04
        "v07/guilfoolwalk05.png"
        pause 0.04
        "v07/guilfoolwalk06.png"
        pause 0.04
        "v07/guilfoolwalk07.png"
        pause 0.04
        "v07/guilfoolwalk08.png"
        pause 0.04
        "v07/guilfoolwalk09.png"
        pause 0.04
        "v07/guilfoolwalk10.png"
        pause 0.04
        "v07/guilfoolwalk11.png"
        pause 0.04
        "v07/guilfoolwalk12.png"
        pause 0.04
        "v07/guilfoolwalk13.png"
        pause 0.04
        "v07/guilfoolwalk14.png"
        pause 0.04
        "v07/guilfoolwalk15.png"
        pause 0.04
        "v07/guilfoolwalk16.png"
        pause 0.04
        "v07/guilfoolwalk17.png"
        pause 0.04
        "v07/guilfoolwalk18.png"
        pause 0.04
        "v07/guilfoolwalk19.png"
        pause 0.04
        "v07/guilfoolwalk20.png"
        pause 0.04
        "v07/guilfoolwalk21.png"
        pause 0.04
        "v07/guilfoolwalk22.png"
        pause 0.04
        "v07/guilfoolwalk23.png"
        pause 0.04
        "v07/guilfoolwalk24.png"
        pause 0.04
        "v07/guilfoolwalk25.png"
        pause 0.04
        "v07/guilfoolwalk26.png"
        pause 0.04
        "v07/guilfoolwalk27.png"
        pause 0.04
        "v07/guilfoolwalk28.png"
        pause 0.04
        "v07/guilfoolwalk29.png"
        pause 0.04
        "v07/guilfoolwalk30.png"
        pause 0.04
        repeat
            
    transform hulkwalk:
        "v07/hulkwalk00.png"
        pause 0.04
        "v07/hulkwalk01.png"
        pause 0.04
        "v07/hulkwalk02.png"
        pause 0.04
        "v07/hulkwalk03.png"
        pause 0.04
        "v07/hulkwalk04.png"
        pause 0.04
        "v07/hulkwalk05.png"
        pause 0.04
        "v07/hulkwalk06.png"
        pause 0.04
        "v07/hulkwalk07.png"
        pause 0.04
        "v07/hulkwalk08.png"
        pause 0.04
        "v07/hulkwalk09.png"
        pause 0.04
        "v07/hulkwalk10.png"
        pause 0.04
        "v07/hulkwalk11.png"
        pause 0.04
        "v07/hulkwalk12.png"
        pause 0.04
        "v07/hulkwalk13.png"
        pause 0.04
        "v07/hulkwalk14.png"
        pause 0.04
        "v07/hulkwalk15.png"
        pause 0.04
        "v07/hulkwalk16.png"
        pause 0.04
        "v07/hulkwalk17.png"
        pause 0.04
        "v07/hulkwalk18.png"
        pause 0.04
        "v07/hulkwalk19.png"
        pause 0.04
        "v07/hulkwalk20.png"
        pause 0.04
        "v07/hulkwalk21.png"
        pause 0.04
        "v07/hulkwalk22.png"
        pause 0.04
        "v07/hulkwalk23.png"
        pause 0.04
        "v07/hulkwalk24.png"
        pause 0.04
        "v07/hulkwalk25.png"
        pause 0.04
        "v07/hulkwalk26.png"
        pause 0.04
        "v07/hulkwalk27.png"
        pause 0.04
        "v07/hulkwalk28.png"
        pause 0.04
        "v07/hulkwalk29.png"
        pause 0.04
        "v07/hulkwalk30.png"
        pause 0.04
        repeat
            
    transform sukyuwalk:
        "v07/sukyuwalk00.png"
        pause 0.04
        "v07/sukyuwalk01.png"
        pause 0.04
        "v07/sukyuwalk02.png"
        pause 0.04
        "v07/sukyuwalk03.png"
        pause 0.04
        "v07/sukyuwalk04.png"
        pause 0.04
        "v07/sukyuwalk05.png"
        pause 0.04
        "v07/sukyuwalk06.png"
        pause 0.04
        "v07/sukyuwalk07.png"
        pause 0.04
        "v07/sukyuwalk08.png"
        pause 0.04
        "v07/sukyuwalk09.png"
        pause 0.04
        "v07/sukyuwalk10.png"
        pause 0.04
        "v07/sukyuwalk11.png"
        pause 0.04
        "v07/sukyuwalk12.png"
        pause 0.04
        "v07/sukyuwalk13.png"
        pause 0.04
        "v07/sukyuwalk14.png"
        pause 0.04
        "v07/sukyuwalk15.png"
        pause 0.04
        "v07/sukyuwalk16.png"
        pause 0.04
        "v07/sukyuwalk17.png"
        pause 0.04
        "v07/sukyuwalk18.png"
        pause 0.04
        "v07/sukyuwalk19.png"
        pause 0.04
        "v07/sukyuwalk20.png"
        pause 0.04
        "v07/sukyuwalk21.png"
        pause 0.04
        "v07/sukyuwalk22.png"
        pause 0.04
        "v07/sukyuwalk23.png"
        pause 0.04
        "v07/sukyuwalk24.png"
        pause 0.04
        "v07/sukyuwalk25.png"
        pause 0.04
        "v07/sukyuwalk26.png"
        pause 0.04
        "v07/sukyuwalk27.png"
        pause 0.04
        "v07/sukyuwalk28.png"
        pause 0.04
        "v07/sukyuwalk29.png"
        pause 0.04
        "v07/sukyuwalk30.png"
        pause 0.04
        repeat
            
    transform heatherwalk:
        "v07/heatherwalk00.png"
        pause 0.04
        "v07/heatherwalk01.png"
        pause 0.04
        "v07/heatherwalk02.png"
        pause 0.04
        "v07/heatherwalk03.png"
        pause 0.04
        "v07/heatherwalk04.png"
        pause 0.04
        "v07/heatherwalk05.png"
        pause 0.04
        "v07/heatherwalk06.png"
        pause 0.04
        "v07/heatherwalk07.png"
        pause 0.04
        "v07/heatherwalk08.png"
        pause 0.04
        "v07/heatherwalk09.png"
        pause 0.04
        "v07/heatherwalk10.png"
        pause 0.04
        "v07/heatherwalk11.png"
        pause 0.04
        "v07/heatherwalk12.png"
        pause 0.04
        "v07/heatherwalk13.png"
        pause 0.04
        "v07/heatherwalk14.png"
        pause 0.04
        "v07/heatherwalk15.png"
        pause 0.04
        "v07/heatherwalk16.png"
        pause 0.04
        "v07/heatherwalk17.png"
        pause 0.04
        "v07/heatherwalk18.png"
        pause 0.04
        "v07/heatherwalk19.png"
        pause 0.04
        "v07/heatherwalk20.png"
        pause 0.04
        "v07/heatherwalk21.png"
        pause 0.04
        "v07/heatherwalk22.png"
        pause 0.04
        "v07/heatherwalk23.png"
        pause 0.04
        "v07/heatherwalk24.png"
        pause 0.04
        "v07/heatherwalk25.png"
        pause 0.04
        "v07/heatherwalk26.png"
        pause 0.04
        "v07/heatherwalk27.png"
        pause 0.04
        "v07/heatherwalk28.png"
        pause 0.04
        "v07/heatherwalk29.png"
        pause 0.04
        "v07/heatherwalk30.png"
        pause 0.04
        repeat
            
    transform kristawalk:
        "v08/kristawalk00.png"
        pause 0.04
        "v08/kristawalk01.png"
        pause 0.04
        "v08/kristawalk02.png"
        pause 0.04
        "v08/kristawalk03.png"
        pause 0.04
        "v08/kristawalk04.png"
        pause 0.04
        "v08/kristawalk05.png"
        pause 0.04
        "v08/kristawalk06.png"
        pause 0.04
        "v08/kristawalk07.png"
        pause 0.04
        "v08/kristawalk08.png"
        pause 0.04
        "v08/kristawalk09.png"
        pause 0.04
        "v08/kristawalk10.png"
        pause 0.04
        "v08/kristawalk11.png"
        pause 0.04
        "v08/kristawalk12.png"
        pause 0.04
        "v08/kristawalk13.png"
        pause 0.04
        "v08/kristawalk14.png"
        pause 0.04
        "v08/kristawalk15.png"
        pause 0.04
        "v08/kristawalk16.png"
        pause 0.04
        "v08/kristawalk17.png"
        pause 0.04
        "v08/kristawalk18.png"
        pause 0.04
        "v08/kristawalk19.png"
        pause 0.04
        "v08/kristawalk20.png"
        pause 0.04
        "v08/kristawalk21.png"
        pause 0.04
        "v08/kristawalk22.png"
        pause 0.04
        "v08/kristawalk23.png"
        pause 0.04
        "v08/kristawalk24.png"
        pause 0.04
        "v08/kristawalk25.png"
        pause 0.04
        "v08/kristawalk26.png"
        pause 0.04
        "v08/kristawalk27.png"
        pause 0.04
        "v08/kristawalk28.png"
        pause 0.04
        "v08/kristawalk29.png"
        pause 0.04
        "v08/kristawalk30.png"
        pause 0.04
        repeat
            
    transform paulettewalk:
        "v081/paulettewalk00.png"
        pause 0.04
        "v081/paulettewalk01.png"
        pause 0.04
        "v081/paulettewalk02.png"
        pause 0.04
        "v081/paulettewalk03.png"
        pause 0.04
        "v081/paulettewalk04.png"
        pause 0.04
        "v081/paulettewalk05.png"
        pause 0.04
        "v081/paulettewalk06.png"
        pause 0.04
        "v081/paulettewalk07.png"
        pause 0.04
        "v081/paulettewalk08.png"
        pause 0.04
        "v081/paulettewalk09.png"
        pause 0.04
        "v081/paulettewalk10.png"
        pause 0.04
        "v081/paulettewalk11.png"
        pause 0.04
        "v081/paulettewalk12.png"
        pause 0.04
        "v081/paulettewalk13.png"
        pause 0.04
        "v081/paulettewalk14.png"
        pause 0.04
        "v081/paulettewalk15.png"
        pause 0.04
        "v081/paulettewalk16.png"
        pause 0.04
        "v081/paulettewalk17.png"
        pause 0.04
        "v081/paulettewalk18.png"
        pause 0.04
        "v081/paulettewalk19.png"
        pause 0.04
        "v081/paulettewalk20.png"
        pause 0.04
        "v081/paulettewalk21.png"
        pause 0.04
        "v081/paulettewalk22.png"
        pause 0.04
        "v081/paulettewalk23.png"
        pause 0.04
        "v081/paulettewalk24.png"
        pause 0.04
        "v081/paulettewalk25.png"
        pause 0.04
        "v081/paulettewalk26.png"
        pause 0.04
        "v081/paulettewalk27.png"
        pause 0.04
        "v081/paulettewalk28.png"
        pause 0.04
        "v081/paulettewalk29.png"
        pause 0.04
        "v081/paulettewalk30.png"
        pause 0.04
        repeat
            
    transform sciencefuck01:
        "Science/science10.jpg" with fastdissolve
        pause 0.4
        "Science/science11.jpg" with fastdissolve
        pause 0.6
        repeat
    
    transform aylagymjog01:
        "Gym/aylagym00.png"
        pause 0.05
        "Gym/aylagym01.png"
        pause 0.05
        "Gym/aylagym02.png"
        pause 0.05
        "Gym/aylagym03.png"
        pause 0.05
        "Gym/aylagym04.png"
        pause 0.05
        "Gym/aylagym05.png"
        pause 0.05
        "Gym/aylagym06.png"
        pause 0.05
        "Gym/aylagym07.png"
        pause 0.05
        "Gym/aylagym08.png"
        pause 0.05
        "Gym/aylagym09.png"
        pause 0.05
        "Gym/aylagym10.png"
        pause 0.05
        "Gym/aylagym11.png"
        pause 0.05
        "Gym/aylagym12.png"
        pause 0.05
        "Gym/aylagym13.png"
        pause 0.05
        "Gym/aylagym14.png"
        pause 0.05
        "Gym/aylagym15.png"
        pause 0.05
        "Gym/aylagym16.png"
        pause 0.05
        repeat

    image intromc02:
        "Intro/intromc02e.jpg"
        pause 0.5
        "Intro/intromc02c.jpg"
        pause 0.3
        "Intro/intromc02e.jpg"
        pause 0.8
        "Intro/intromc02e.jpg"
        pause 0.1
        "Intro/intromc02e.jpg"
        pause 0.5
        repeat

    image intromc02g:
        "Intro/intromc02d.jpg"
        pause 0.5
        "Intro/intromc02f.jpg"
        pause 0.3
        "Intro/intromc02d.jpg"
        pause 0.8
        "Intro/intromc02f.jpg"
        pause 0.1
        "Intro/intromc02d.jpg"
        pause 0.5
        repeat
    
    image prisonfuckmovie01slow:
        "Command/prisonfuckmovie00.png"
        pause 0.16
        "Command/prisonfuckmovie01.png"
        pause 0.08
        "Command/prisonfuckmovie02.png"
        pause 0.08
        "Command/prisonfuckmovie03.png"
        pause 0.08
        "Command/prisonfuckmovie04.png"
        pause 0.08
        "Command/prisonfuckmovie05.png"
        pause 0.08
        "Command/prisonfuckmovie06.png"
        pause 0.08
        "Command/prisonfuckmovie07.png"
        pause 0.08
        "Command/prisonfuckmovie06.png"
        pause 0.06
        "Command/prisonfuckmovie05.png"
        pause 0.06
        "Command/prisonfuckmovie04.png"
        pause 0.06
        "Command/prisonfuckmovie03.png"
        pause 0.06
        "Command/prisonfuckmovie02.png"
        pause 0.06
        "Command/prisonfuckmovie01.png"
        pause 0.06
        repeat    

    image prisonfuckmovie01fast:
        "Command/prisonfuckmovie00.png"
        pause 0.12
        "Command/prisonfuckmovie01.png"
        pause 0.06
        "Command/prisonfuckmovie02.png"
        pause 0.06
        "Command/prisonfuckmovie03.png"
        pause 0.06
        "Command/prisonfuckmovie04.png"
        pause 0.06
        "Command/prisonfuckmovie05.png"
        pause 0.06
        "Command/prisonfuckmovie06.png"
        pause 0.06
        "Command/prisonfuckmovie07.png"
        pause 0.06
        "Command/prisonfuckmovie06.png"
        pause 0.04
        "Command/prisonfuckmovie05.png"
        pause 0.04
        "Command/prisonfuckmovie04.png"
        pause 0.04
        "Command/prisonfuckmovie03.png"
        pause 0.04
        "Command/prisonfuckmovie02.png"
        pause 0.04
        "Command/prisonfuckmovie01.png"
        pause 0.04
        repeat    
    
    image prisonanalfast:
        "Command/prisonanal00.png"
        pause 0.10
        "Command/prisonanal01.png"
        pause 0.06
        "Command/prisonanal02.png"
        pause 0.06
        "Command/prisonanal03.png"
        pause 0.06
        "Command/prisonanal04.png"
        pause 0.06
        "Command/prisonanal05.png"
        pause 0.06
        "Command/prisonanal06.png"
        pause 0.06
        "Command/prisonanal07.png"
        pause 0.06
        "Command/prisonanal08.png"
        pause 0.06
        "Command/prisonanal07.png"
        pause 0.04
        "Command/prisonanal06.png"
        pause 0.04
        "Command/prisonanal05.png"
        pause 0.04
        "Command/prisonanal04.png"
        pause 0.04
        "Command/prisonanal03.png"
        pause 0.04
        "Command/prisonanal02.png"
        pause 0.04
        "Command/prisonanal01.png"
        pause 0.04
        repeat

    image prisonanalslow:
        "Command/prisonanal00.png"
        pause 0.15
        "Command/prisonanal01.png"
        pause 0.08
        "Command/prisonanal02.png"
        pause 0.08
        "Command/prisonanal03.png"
        pause 0.08
        "Command/prisonanal04.png"
        pause 0.08
        "Command/prisonanal05.png"
        pause 0.08
        "Command/prisonanal06.png"
        pause 0.08
        "Command/prisonanal07.png"
        pause 0.08
        "Command/prisonanal08.png"
        pause 0.08
        "Command/prisonanal07.png"
        pause 0.06
        "Command/prisonanal06.png"
        pause 0.06
        "Command/prisonanal05.png"
        pause 0.06
        "Command/prisonanal04.png"
        pause 0.06
        "Command/prisonanal03.png"
        pause 0.06
        "Command/prisonanal02.png"
        pause 0.06
        "Command/prisonanal01.png"
        pause 0.06
        repeat
    
    image scarlettfuckfast:
        "Explore/scarlettfuck00.png"
        pause 0.04
        "Explore/scarlettfuck01.png"
        pause 0.04
        "Explore/scarlettfuck02.png"
        pause 0.04
        "Explore/scarlettfuck03.png"
        pause 0.04
        "Explore/scarlettfuck04.png"
        pause 0.04
        "Explore/scarlettfuck05.png"
        pause 0.04
        "Explore/scarlettfuck06.png"
        pause 0.04
        "Explore/scarlettfuck07.png"
        pause 0.04
        "Explore/scarlettfuck08.png"
        pause 0.04
        "Explore/scarlettfuck09.png"
        pause 0.04
        "Explore/scarlettfuck10.png"
        pause 0.04
        "Explore/scarlettfuck11.png"
        pause 0.04
        "Explore/scarlettfuck12.png"
        pause 0.04
        "Explore/scarlettfuck13.png"
        pause 0.04
        "Explore/scarlettfuck14.png"
        pause 0.04
        "Explore/scarlettfuck15.png"
        pause 0.04
        "Explore/scarlettfuck16.png"
        pause 0.04
        "Explore/scarlettfuck17.png"
        pause 0.04
        "Explore/scarlettfuck18.png"
        pause 0.04
        repeat


    image scarlettfuckslow:
        "Explore/scarlettfuck00.png"
        pause 0.06
        "Explore/scarlettfuck01.png"
        pause 0.06
        "Explore/scarlettfuck02.png"
        pause 0.06
        "Explore/scarlettfuck03.png"
        pause 0.06
        "Explore/scarlettfuck04.png"
        pause 0.06
        "Explore/scarlettfuck05.png"
        pause 0.06
        "Explore/scarlettfuck06.png"
        pause 0.06
        "Explore/scarlettfuck07.png"
        pause 0.06
        "Explore/scarlettfuck08.png"
        pause 0.06
        "Explore/scarlettfuck09.png"
        pause 0.06
        "Explore/scarlettfuck10.png"
        pause 0.06
        "Explore/scarlettfuck11.png"
        pause 0.06
        "Explore/scarlettfuck12.png"
        pause 0.06
        "Explore/scarlettfuck13.png"
        pause 0.06
        "Explore/scarlettfuck14.png"
        pause 0.06
        "Explore/scarlettfuck15.png"
        pause 0.06
        "Explore/scarlettfuck16.png"
        pause 0.06
        "Explore/scarlettfuck17.png"
        pause 0.06
        "Explore/scarlettfuck18.png"
        pause 0.06
        repeat
    
    image scarlettblowfast:
        "Explore/scarlettblow00.png"
        pause 0.06
        "Explore/scarlettblow01.png"
        pause 0.06
        "Explore/scarlettblow02.png"
        pause 0.06
        "Explore/scarlettblow03.png"
        pause 0.06
        "Explore/scarlettblow04.png"
        pause 0.06
        "Explore/scarlettblow05.png"
        pause 0.06
        "Explore/scarlettblow06.png"
        pause 0.06
        "Explore/scarlettblow07.png"
        pause 0.06
        "Explore/scarlettblow06.png"
        pause 0.06
        "Explore/scarlettblow05.png"
        pause 0.06
        "Explore/scarlettblow04.png"
        pause 0.06
        "Explore/scarlettblow03.png"
        pause 0.06
        "Explore/scarlettblow02.png"
        pause 0.06
        "Explore/scarlettblow01.png"
        pause 0.06
        repeat
    
    image scarlettblowslow:
        "Explore/scarlettblow00.png"
        pause 0.09
        "Explore/scarlettblow01.png"
        pause 0.09
        "Explore/scarlettblow02.png"
        pause 0.09
        "Explore/scarlettblow03.png"
        pause 0.09
        "Explore/scarlettblow04.png"
        pause 0.09
        "Explore/scarlettblow05.png"
        pause 0.09
        "Explore/scarlettblow06.png"
        pause 0.09
        "Explore/scarlettblow07.png"
        pause 0.09
        "Explore/scarlettblow06.png"
        pause 0.09
        "Explore/scarlettblow05.png"
        pause 0.09
        "Explore/scarlettblow04.png"
        pause 0.09
        "Explore/scarlettblow03.png"
        pause 0.09
        "Explore/scarlettblow02.png"
        pause 0.09
        "Explore/scarlettblow01.png"
        pause 0.09
        repeat
    
    image widowbjslow:
        "Explore/widowbj02.png"
        pause 0.04
        "Explore/widowbj03.png"
        pause 0.04
        "Explore/widowbj04.png"
        pause 0.04
        "Explore/widowbj05.png"
        pause 0.04
        "Explore/widowbj06.png"
        pause 0.04
        "Explore/widowbj07.png"
        pause 0.04
        "Explore/widowbj08.png"
        pause 0.04
        "Explore/widowbj09.png"
        pause 0.04
        "Explore/widowbj10.png"
        pause 0.04
        "Explore/widowbj11.png"
        pause 0.04
        "Explore/widowbj12.png"
        pause 0.04
        "Explore/widowbj13.png"
        pause 0.04
        "Explore/widowbj14.png"
        pause 0.08
        "Explore/widowbj13.png"
        pause 0.05
        "Explore/widowbj12.png"
        pause 0.05
        "Explore/widowbj11.png"
        pause 0.05
        "Explore/widowbj10.png"
        pause 0.05
        "Explore/widowbj09.png"
        pause 0.05
        "Explore/widowbj08.png"
        pause 0.05
        "Explore/widowbj07.png"
        pause 0.05
        "Explore/widowbj06.png"
        pause 0.05
        "Explore/widowbj05.png"
        pause 0.05
        "Explore/widowbj04.png"
        pause 0.05
        "Explore/widowbj03.png"
        pause 0.05
        repeat

    image widowbjfast:
        "Explore/widowbj02.png"
        pause 0.03
        "Explore/widowbj03.png"
        pause 0.03
        "Explore/widowbj04.png"
        pause 0.03
        "Explore/widowbj05.png"
        pause 0.03
        "Explore/widowbj06.png"
        pause 0.03
        "Explore/widowbj07.png"
        pause 0.03
        "Explore/widowbj08.png"
        pause 0.03
        "Explore/widowbj09.png"
        pause 0.03
        "Explore/widowbj10.png"
        pause 0.03
        "Explore/widowbj11.png"
        pause 0.03
        "Explore/widowbj12.png"
        pause 0.03
        "Explore/widowbj13.png"
        pause 0.03
        "Explore/widowbj14.png"
        pause 0.06
        "Explore/widowbj13.png"
        pause 0.04
        "Explore/widowbj12.png"
        pause 0.04
        "Explore/widowbj11.png"
        pause 0.04
        "Explore/widowbj10.png"
        pause 0.04
        "Explore/widowbj09.png"
        pause 0.04
        "Explore/widowbj08.png"
        pause 0.04
        "Explore/widowbj07.png"
        pause 0.04
        "Explore/widowbj06.png"
        pause 0.04
        "Explore/widowbj05.png"
        pause 0.04
        "Explore/widowbj04.png"
        pause 0.04
        "Explore/widowbj03.png"
        pause 0.04
        repeat

    transform barbarasex:
        "School/barbarasex03.png"
        pause 0.04
#        "School/barbarasex04.png"
#        pause 0.04
        "School/barbarasex05.png"
        pause 0.04
#        "School/barbarasex06.png"
#        pause 0.04
        "School/barbarasex07.png"
        pause 0.04
#        "School/barbarasex08.png"
#        pause 0.04
        "School/barbarasex09.png"
        pause 0.04
#        "School/barbarasex10.png"
#        pause 0.04
        "School/barbarasex11.png"
        pause 0.04
#        "School/barbarasex12.png"
#        pause 0.04
        "School/barbarasex13.png"
        pause 0.04
        "School/barbarasex14.png"
        pause 0.04
#        "School/barbarasex15.png"
#        pause 0.04
        "School/barbarasex16.png"
        pause 0.04
        "School/barbarasex17.png"
        pause 0.04
        "School/barbarasex18.png"
        pause 0.04
#        "School/barbarasex19.png"
#        pause 0.04
        "School/barbarasex20.png"
        pause 0.04
#        "School/barbarasex21.png"
#        pause 0.04
        "School/barbarasex22.png"
        pause 0.04
#        "School/barbarasex21.png"
#        pause 0.04
        "School/barbarasex20.png"
        pause 0.04
        "School/barbarasex19.png"
        pause 0.04
        "School/barbarasex18.png"
        pause 0.04
        "School/barbarasex17.png"
        pause 0.04
        "School/barbarasex16.png"
        pause 0.04
        "School/barbarasex15.png"
        pause 0.04
        "School/barbarasex14.png"
        pause 0.04
        "School/barbarasex13.png"
        pause 0.04
        "School/barbarasex12.png"
        pause 0.04
        "School/barbarasex11.png"
        pause 0.04
        "School/barbarasex10.png"
        pause 0.04
        "School/barbarasex09.png"
        pause 0.04
        "School/barbarasex08.png"
        pause 0.04
        "School/barbarasex07.png"
        pause 0.04
        "School/barbarasex06.png"
        pause 0.04
        "School/barbarasex05.png"
        pause 0.04
        "School/barbarasex04.png"
        pause 0.04
        repeat

    transform aliensex:
        "Explore/aliensex00.png"
        pause 0.04
        "Explore/aliensex01.png"
        pause 0.04
        "Explore/aliensex02.png"
        pause 0.04
        "Explore/aliensex03.png"
        pause 0.04
        "Explore/aliensex04.png"
        pause 0.04
        "Explore/aliensex05.png"
        pause 0.04
        "Explore/aliensex06.png"
        pause 0.04
        "Explore/aliensex07.png"
        pause 0.04
        "Explore/aliensex08.png"
        pause 0.04
        "Explore/aliensex09.png"
        pause 0.04
        "Explore/aliensex10.png"
        pause 0.04
        "Explore/aliensex11.png"
        pause 0.04
        "Explore/aliensex12.png"
        pause 0.04
        "Explore/aliensex13.png"
        pause 0.04
        "Explore/aliensex14.png"
        pause 0.04
        "Explore/aliensex15.png"
        pause 0.04
        "Explore/aliensex16.png"
        pause 0.04
        "Explore/aliensex17.png"
        pause 0.04
        "Explore/aliensex18.png"
        pause 0.04
        "Explore/aliensex19.png"
        pause 0.04
        "Explore/aliensex20.png"
        pause 0.04
        "Explore/aliensex21.png"
        pause 0.04
        "Explore/aliensex22.png"
        pause 0.04
        "Explore/aliensex23.png"
        pause 0.04
        "Explore/aliensex24.png"
        pause 0.04
        "Explore/aliensex25.png"
        pause 0.04
        "Explore/aliensex26.png"
        pause 0.04
        "Explore/aliensex27.png"
        pause 0.04
        repeat  
            
    transform zarahandjob:
        "Zara/zarahandjob01.png" with fastdissolve
        pause 0.4
        "Zara/zarahandjob02.png" with fastdissolve
        pause 0.2
        "Zara/zarahandjob03.png" with fastdissolve
        pause 0.2
        "Zara/zarahandjob04.png" with fastdissolve
        pause 0.2
        "Zara/zarahandjob05.png" with fastdissolve
        pause 0.2
        "Zara/zarahandjob06.png" with fastdissolve
        pause 0.4
        "Zara/zarahandjob05.png" with fastdissolve
        pause 0.2
        "Zara/zarahandjob04.png" with fastdissolve
        pause 0.2
        "Zara/zarahandjob03.png" with fastdissolve
        pause 0.2
        "Zara/zarahandjob02.png" with fastdissolve
        pause 0.2
        repeat

    image zararideslow:
        "Zara/zararide00.png"
        pause 0.09
        "Zara/zararide01.png"
        pause 0.07
        "Zara/zararide02.png"
        pause 0.07
        "Zara/zararide03.png"
        pause 0.07
        "Zara/zararide04.png"
        pause 0.07
        "Zara/zararide05.png"
        pause 0.07
        "Zara/zararide06.png"
        pause 0.07
        "Zara/zararide07.png"
        pause 0.07
        "Zara/zararide08.png"
        pause 0.07
        "Zara/zararide09.png"
        pause 0.09
        "Zara/zararide08.png"
        pause 0.06
        "Zara/zararide07.png"
        pause 0.06
        "Zara/zararide06.png"
        pause 0.06
        "Zara/zararide05.png"
        pause 0.06
        "Zara/zararide04.png"
        pause 0.06
        "Zara/zararide03.png"
        pause 0.06
        "Zara/zararide02.png"
        pause 0.06
        "Zara/zararide01.png"
        pause 0.04
        repeat

    image zararidefast:
        "Zara/zararide00.png"
        pause 0.07
        "Zara/zararide01.png"
        pause 0.05
        "Zara/zararide02.png"
        pause 0.05
        "Zara/zararide03.png"
        pause 0.05
        "Zara/zararide04.png"
        pause 0.05
        "Zara/zararide05.png"
        pause 0.05
        "Zara/zararide06.png"
        pause 0.05
        "Zara/zararide07.png"
        pause 0.05
        "Zara/zararide08.png"
        pause 0.05
        "Zara/zararide09.png"
        pause 0.07
        "Zara/zararide08.png"
        pause 0.04
        "Zara/zararide07.png"
        pause 0.04
        "Zara/zararide06.png"
        pause 0.04
        "Zara/zararide05.png"
        pause 0.04
        "Zara/zararide04.png"
        pause 0.04
        "Zara/zararide03.png"
        pause 0.04
        "Zara/zararide02.png"
        pause 0.04
        "Zara/zararide01.png"
        pause 0.04
        repeat

    image zarafistslow:
        "Zara/zarafist00.png"
        pause 0.06
        "Zara/zarafist01.png"
        pause 0.06
        "Zara/zarafist02.png"
        pause 0.06
        "Zara/zarafist03.png"
        pause 0.06
        "Zara/zarafist04.png"
        pause 0.06
        "Zara/zarafist05.png"
        pause 0.06
        "Zara/zarafist06.png"
        pause 0.06
        "Zara/zarafist07.png"
        pause 0.06
        "Zara/zarafist08.png"
        pause 0.06
        "Zara/zarafist09.png"
        pause 0.09
        "Zara/zarafist08.png"
        pause 0.06
        "Zara/zarafist07.png"
        pause 0.06
        "Zara/zarafist06.png"
        pause 0.06
        "Zara/zarafist05.png"
        pause 0.06
        "Zara/zarafist04.png"
        pause 0.06
        "Zara/zarafist03.png"
        pause 0.06
        "Zara/zarafist02.png"
        pause 0.06
        "Zara/zarafist01.png"
        pause 0.06
        repeat

    image zarafistfast:
        "Zara/zarafist00.png"
        pause 0.04
        "Zara/zarafist01.png"
        pause 0.04
        "Zara/zarafist02.png"
        pause 0.04
        "Zara/zarafist03.png"
        pause 0.04
        "Zara/zarafist04.png"
        pause 0.04
        "Zara/zarafist05.png"
        pause 0.04
        "Zara/zarafist06.png"
        pause 0.04
        "Zara/zarafist07.png"
        pause 0.04
        "Zara/zarafist08.png"
        pause 0.04
        "Zara/zarafist09.png"
        pause 0.06
        "Zara/zarafist08.png"
        pause 0.04
        "Zara/zarafist07.png"
        pause 0.04
        "Zara/zarafist06.png"
        pause 0.04
        "Zara/zarafist05.png"
        pause 0.04
        "Zara/zarafist04.png"
        pause 0.04
        "Zara/zarafist03.png"
        pause 0.04
        "Zara/zarafist02.png"
        pause 0.04
        "Zara/zarafist01.png"
        pause 0.04
        repeat

    image zarabounceslow:
        "Zara/zarabounce00.png"
        pause 0.05
        "Zara/zarabounce01.png"
        pause 0.05
        "Zara/zarabounce02.png"
        pause 0.05
        "Zara/zarabounce03.png"
        pause 0.05
        "Zara/zarabounce04.png"
        pause 0.05
        "Zara/zarabounce05.png"
        pause 0.05
        "Zara/zarabounce06.png"
        pause 0.05
        "Zara/zarabounce07.png"
        pause 0.05
        "Zara/zarabounce08.png"
        pause 0.05
        "Zara/zarabounce09.png"
        pause 0.05
        "Zara/zarabounce10.png"
        pause 0.05
        "Zara/zarabounce11.png"
        pause 0.05
        "Zara/zarabounce12.png"
        pause 0.05
        "Zara/zarabounce13.png"
        pause 0.05
        "Zara/zarabounce14.png"
        pause 0.05
        "Zara/zarabounce15.png"
        pause 0.05
        "Zara/zarabounce16.png"
        pause 0.05
        "Zara/zarabounce17.png"
        pause 0.05
        "Zara/zarabounce18.png"
        pause 0.05
        "Zara/zarabounce19.png"
        pause 0.05
        repeat

    image zarabouncefast:
        "Zara/zarabounce00.png"
        pause 0.03
        "Zara/zarabounce01.png"
        pause 0.03
        "Zara/zarabounce02.png"
        pause 0.03
        "Zara/zarabounce03.png"
        pause 0.03
        "Zara/zarabounce04.png"
        pause 0.03
        "Zara/zarabounce05.png"
        pause 0.03
        "Zara/zarabounce06.png"
        pause 0.03
        "Zara/zarabounce07.png"
        pause 0.03
        "Zara/zarabounce08.png"
        pause 0.03
        "Zara/zarabounce09.png"
        pause 0.03
        "Zara/zarabounce10.png"
        pause 0.03
        "Zara/zarabounce11.png"
        pause 0.03
        "Zara/zarabounce12.png"
        pause 0.03
        "Zara/zarabounce13.png"
        pause 0.03
        "Zara/zarabounce14.png"
        pause 0.03
        "Zara/zarabounce15.png"
        pause 0.03
        "Zara/zarabounce16.png"
        pause 0.03
        "Zara/zarabounce17.png"
        pause 0.03
        "Zara/zarabounce18.png"
        pause 0.03
        "Zara/zarabounce19.png"
        pause 0.03
        repeat

    image angiespread:
        "Angie/angiespread00.png"
        pause 0.04
        "Angie/angiespread01.png"
        pause 0.04
        "Angie/angiespread02.png"
        pause 0.04
        "Angie/angiespread03.png"
        pause 0.04
        "Angie/angiespread04.png"
        pause 0.04
        "Angie/angiespread05.png"
        pause 0.04
        "Angie/angiespread06.png"
        pause 0.04
        "Angie/angiespread05.png"
        pause 0.04
        "Angie/angiespread04.png"
        pause 0.04
        "Angie/angiespread03.png"
        pause 0.04
        "Angie/angiespread02.png"
        pause 0.04
        "Angie/angiespread01.png"
        pause 0.04
        repeat
    
    image angietugslow:
        "Angie/angietug00.png"
        pause 0.05
        "Angie/angietug01.png"
        pause 0.05
        "Angie/angietug02.png"
        pause 0.05
        "Angie/angietug03.png"
        pause 0.05
        "Angie/angietug04.png"
        pause 0.05
        "Angie/angietug05.png"
        pause 0.05
        "Angie/angietug06.png"
        pause 0.05
        "Angie/angietug07.png"
        pause 0.05
        "Angie/angietug08.png"
        pause 0.05
        "Angie/angietug07.png"
        pause 0.05
        "Angie/angietug06.png"
        pause 0.05
        "Angie/angietug05.png"
        pause 0.05
        "Angie/angietug04.png"
        pause 0.05
        "Angie/angietug03.png"
        pause 0.05
        "Angie/angietug02.png"
        pause 0.05
        "Angie/angietug01.png"
        pause 0.05
        repeat

    image angietugfast:
        "Angie/angietug00.png"
        pause 0.03
        "Angie/angietug01.png"
        pause 0.03
        "Angie/angietug02.png"
        pause 0.03
        "Angie/angietug03.png"
        pause 0.03
        "Angie/angietug04.png"
        pause 0.03
        "Angie/angietug05.png"
        pause 0.03
        "Angie/angietug06.png"
        pause 0.03
        "Angie/angietug07.png"
        pause 0.03
        "Angie/angietug08.png"
        pause 0.03
        "Angie/angietug07.png"
        pause 0.03
        "Angie/angietug06.png"
        pause 0.03
        "Angie/angietug05.png"
        pause 0.03
        "Angie/angietug04.png"
        pause 0.03
        "Angie/angietug03.png"
        pause 0.03
        "Angie/angietug02.png"
        pause 0.03
        "Angie/angietug01.png"
        pause 0.03
        repeat
    
    image angieanalslow:
        "Angie/angieanal00.png"
        pause 0.05
        "Angie/angieanal01.png"
        pause 0.05
        "Angie/angieanal02.png"
        pause 0.05
        "Angie/angieanal03.png"
        pause 0.05
        "Angie/angieanal04.png"
        pause 0.05
        "Angie/angieanal05.png"
        pause 0.05
        "Angie/angieanal06.png"
        pause 0.05
        "Angie/angieanal07.png"
        pause 0.05
        "Angie/angieanal08.png"
        pause 0.05
        "Angie/angieanal07b.png"
        pause 0.05
        "Angie/angieanal06b.png"
        pause 0.05
        "Angie/angieanal05b.png"
        pause 0.05
        "Angie/angieanal04b.png"
        pause 0.05
        "Angie/angieanal03b.png"
        pause 0.05
        "Angie/angieanal02b.png"
        pause 0.05
        "Angie/angieanal01b.png"
        pause 0.05
        repeat
        
    image angieanalfast:
        "Angie/angieanal00.png"
        pause 0.03
        "Angie/angieanal01.png"
        pause 0.03
        "Angie/angieanal02.png"
        pause 0.03
        "Angie/angieanal03.png"
        pause 0.03
        "Angie/angieanal04.png"
        pause 0.03
        "Angie/angieanal05.png"
        pause 0.03
        "Angie/angieanal06.png"
        pause 0.03
        "Angie/angieanal07.png"
        pause 0.03
        "Angie/angieanal08.png"
        pause 0.03
        "Angie/angieanal07b.png"
        pause 0.03
        "Angie/angieanal06b.png"
        pause 0.03
        "Angie/angieanal05b.png"
        pause 0.03
        "Angie/angieanal04b.png"
        pause 0.03
        "Angie/angieanal03b.png"
        pause 0.03
        "Angie/angieanal02b.png"
        pause 0.03
        "Angie/angieanal01b.png"
        pause 0.03
        repeat

    image angiefuckslow:
        "Angie/mcangiefuck00.png"
        pause 0.05
        "Angie/mcangiefuck02.png"
        pause 0.05
        "Angie/mcangiefuck03.png"
        pause 0.05
        "Angie/mcangiefuck04.png"
        pause 0.05
        "Angie/mcangiefuck05.png"
        pause 0.05
        "Angie/mcangiefuck06.png"
        pause 0.05
        "Angie/mcangiefuck07.png"
        pause 0.05
        "Angie/mcangiefuck08.png"
        pause 0.05
        "Angie/mcangiefuck09.png"
        pause 0.05
        "Angie/mcangiefuck10.png"
        pause 0.05
        "Angie/mcangiefuck11.png"
        pause 0.05
        "Angie/mcangiefuck12.png"
        pause 0.05
        "Angie/mcangiefuck14.png"
        pause 0.05
        "Angie/mcangiefuck11.png"
        pause 0.04
        "Angie/mcangiefuck10.png"
        pause 0.04
        "Angie/mcangiefuck09.png"
        pause 0.04
        "Angie/mcangiefuck08.png"
        pause 0.04
        "Angie/mcangiefuck07.png"
        pause 0.04
        "Angie/mcangiefuck06.png"
        pause 0.04
        "Angie/mcangiefuck05.png"
        pause 0.04
        "Angie/mcangiefuck04.png"
        pause 0.04
        "Angie/mcangiefuck03.png"
        pause 0.04
        "Angie/mcangiefuck02.png"
        pause 0.04
        repeat

    image angiefuckfast:
        "Angie/mcangiefuck00.png"
        pause 0.04
        "Angie/mcangiefuck02.png"
        pause 0.04
        "Angie/mcangiefuck03.png"
        pause 0.04
        "Angie/mcangiefuck04.png"
        pause 0.04
        "Angie/mcangiefuck05.png"
        pause 0.04
        "Angie/mcangiefuck06.png"
        pause 0.04
        "Angie/mcangiefuck07.png"
        pause 0.04
        "Angie/mcangiefuck08.png"
        pause 0.04
        "Angie/mcangiefuck09.png"
        pause 0.04
        "Angie/mcangiefuck10.png"
        pause 0.04
        "Angie/mcangiefuck11.png"
        pause 0.04
        "Angie/mcangiefuck12.png"
        pause 0.04
        "Angie/mcangiefuck14.png"
        pause 0.04
        "Angie/mcangiefuck11.png"
        pause 0.03
        "Angie/mcangiefuck10.png"
        pause 0.03
        "Angie/mcangiefuck09.png"
        pause 0.03
        "Angie/mcangiefuck08.png"
        pause 0.03
        "Angie/mcangiefuck07.png"
        pause 0.03
        "Angie/mcangiefuck06.png"
        pause 0.03
        "Angie/mcangiefuck05.png"
        pause 0.03
        "Angie/mcangiefuck04.png"
        pause 0.03
        "Angie/mcangiefuck03.png"
        pause 0.03
        "Angie/mcangiefuck02.png"
        pause 0.03
        repeat

    image hammamhandjobslow:
        "deserttown/hammamhandjob01.jpg"
        pause 0.06
        "deserttown/hammamhandjob02.jpg"
        pause 0.06
        "deserttown/hammamhandjob03.jpg"
        pause 0.06
        "deserttown/hammamhandjob04.jpg"
        pause 0.06
        "deserttown/hammamhandjob05.jpg"
        pause 0.06
        "deserttown/hammamhandjob06.jpg"
        pause 0.06
        "deserttown/hammamhandjob07.jpg"
        pause 0.06
        "deserttown/hammamhandjob06.jpg"
        pause 0.06
        "deserttown/hammamhandjob05.jpg"
        pause 0.06
        "deserttown/hammamhandjob04.jpg"
        pause 0.06
        "deserttown/hammamhandjob03.jpg"
        pause 0.06
        "deserttown/hammamhandjob02.jpg"
        pause 0.06
        repeat

    image hammamhandjobfast:
        "deserttown/hammamhandjob01.jpg"
        pause 0.04
        "deserttown/hammamhandjob02.jpg"
        pause 0.04
        "deserttown/hammamhandjob03.jpg"
        pause 0.04
        "deserttown/hammamhandjob04.jpg"
        pause 0.04
        "deserttown/hammamhandjob05.jpg"
        pause 0.04
        "deserttown/hammamhandjob06.jpg"
        pause 0.04
        "deserttown/hammamhandjob07.jpg"
        pause 0.04
        "deserttown/hammamhandjob06.jpg"
        pause 0.04
        "deserttown/hammamhandjob05.jpg"
        pause 0.04
        "deserttown/hammamhandjob04.jpg"
        pause 0.04
        "deserttown/hammamhandjob03.jpg"
        pause 0.04
        "deserttown/hammamhandjob02.jpg"
        pause 0.04
        repeat

    image hammamfuckslow:
        "deserttown/hammamfuck00.png"
        pause 0.04
        "deserttown/hammamfuck01.png"
        pause 0.04
        "deserttown/hammamfuck02.png"
        pause 0.04
        "deserttown/hammamfuck03.png"
        pause 0.04
        "deserttown/hammamfuck04.png"
        pause 0.04
        "deserttown/hammamfuck05.png"
        pause 0.04
        "deserttown/hammamfuck06.png"
        pause 0.04
        "deserttown/hammamfuck07.png"
        pause 0.04
        "deserttown/hammamfuck08.png"
        pause 0.04
        "deserttown/hammamfuck09.png"
        pause 0.04
        "deserttown/hammamfuck10.png"
        pause 0.05
        "deserttown/hammamfuck11.png"
        pause 0.05
        "deserttown/hammamfuck12.png"
        pause 0.05
        "deserttown/hammamfuck13.png"
        pause 0.05
        "deserttown/hammamfuck14.png"
        pause 0.05
        "deserttown/hammamfuck15.png"
        pause 0.05
        "deserttown/hammamfuck16.png"
        pause 0.05
        "deserttown/hammamfuck17.png"
        pause 0.05
        "deserttown/hammamfuck18.png"
        pause 0.06
        repeat

    image hammamfuckfast:
        "deserttown/hammamfuck00.png"
        pause 0.03
        "deserttown/hammamfuck01.png"
        pause 0.03
        "deserttown/hammamfuck02.png"
        pause 0.03
        "deserttown/hammamfuck03.png"
        pause 0.03
        "deserttown/hammamfuck04.png"
        pause 0.03
        "deserttown/hammamfuck05.png"
        pause 0.03
        "deserttown/hammamfuck06.png"
        pause 0.03
        "deserttown/hammamfuck07.png"
        pause 0.03
        "deserttown/hammamfuck08.png"
        pause 0.03
        "deserttown/hammamfuck09.png"
        pause 0.03
        "deserttown/hammamfuck10.png"
        pause 0.04
        "deserttown/hammamfuck11.png"
        pause 0.04
        "deserttown/hammamfuck12.png"
        pause 0.04
        "deserttown/hammamfuck13.png"
        pause 0.04
        "deserttown/hammamfuck14.png"
        pause 0.04
        "deserttown/hammamfuck15.png"
        pause 0.04
        "deserttown/hammamfuck16.png"
        pause 0.04
        "deserttown/hammamfuck17.png"
        pause 0.04
        "deserttown/hammamfuck18.png"
        pause 0.05
        repeat

    image tattoohandjobslow:
        "deserttown/tattoohandjob01.jpg"
        pause 0.06
        "deserttown/tattoohandjob02.jpg"
        pause 0.06
        "deserttown/tattoohandjob03.jpg"
        pause 0.06
        "deserttown/tattoohandjob04.jpg"
        pause 0.06
        "deserttown/tattoohandjob05.jpg"
        pause 0.06
        "deserttown/tattoohandjob06.jpg"
        pause 0.06
        "deserttown/tattoohandjob07.jpg"
        pause 0.06
        "deserttown/tattoohandjob08.jpg"
        pause 0.06
        "deserttown/tattoohandjob07.jpg"
        pause 0.06
        "deserttown/tattoohandjob06.jpg"
        pause 0.06
        "deserttown/tattoohandjob05.jpg"
        pause 0.06
        "deserttown/tattoohandjob04.jpg"
        pause 0.06
        "deserttown/tattoohandjob03.jpg"
        pause 0.06
        "deserttown/tattoohandjob02.jpg"
        pause 0.06
        repeat
    
    image tattoohandjobfast:
        "deserttown/tattoohandjob01.jpg"
        pause 0.04
        "deserttown/tattoohandjob02.jpg"
        pause 0.04
        "deserttown/tattoohandjob03.jpg"
        pause 0.04
        "deserttown/tattoohandjob04.jpg"
        pause 0.04
        "deserttown/tattoohandjob05.jpg"
        pause 0.04
        "deserttown/tattoohandjob06.jpg"
        pause 0.04
        "deserttown/tattoohandjob07.jpg"
        pause 0.04
        "deserttown/tattoohandjob08.jpg"
        pause 0.04
        "deserttown/tattoohandjob07.jpg"
        pause 0.04
        "deserttown/tattoohandjob06.jpg"
        pause 0.04
        "deserttown/tattoohandjob05.jpg"
        pause 0.04
        "deserttown/tattoohandjob04.jpg"
        pause 0.04
        "deserttown/tattoohandjob03.jpg"
        pause 0.04
        "deserttown/tattoohandjob02.jpg"
        pause 0.04
        repeat

    image mcbarbarawank01slow:
        "Bar/barbarawank00.png"
        pause 0.05
        "Bar/barbarawank01.png"
        pause 0.05
        "Bar/barbarawank02.png"
        pause 0.05
        "Bar/barbarawank03.png"
        pause 0.05
        "Bar/barbarawank04.png"
        pause 0.05
        "Bar/barbarawank05.png"
        pause 0.05
        "Bar/barbarawank06.png"
        pause 0.05
        "Bar/barbarawank07.png"
        pause 0.05
        "Bar/barbarawank08.png"
        pause 0.05
        "Bar/barbarawank09.png"
        pause 0.05
        "Bar/barbarawank08.png"
        pause 0.05
        "Bar/barbarawank07.png"
        pause 0.05
        "Bar/barbarawank06.png"
        pause 0.05
        "Bar/barbarawank05.png"
        pause 0.05
        "Bar/barbarawank04.png"
        pause 0.05
        "Bar/barbarawank03.png"
        pause 0.05
        "Bar/barbarawank02.png"
        pause 0.05
        "Bar/barbarawank01.png"
        pause 0.05
        repeat
    
    image mcbarbarawank01fast:
        "Bar/barbarawank00.png"
        pause 0.03
        "Bar/barbarawank01.png"
        pause 0.03
        "Bar/barbarawank02.png"
        pause 0.03
        "Bar/barbarawank03.png"
        pause 0.03
        "Bar/barbarawank04.png"
        pause 0.03
        "Bar/barbarawank05.png"
        pause 0.03
        "Bar/barbarawank06.png"
        pause 0.03
        "Bar/barbarawank07.png"
        pause 0.03
        "Bar/barbarawank08.png"
        pause 0.03
        "Bar/barbarawank09.png"
        pause 0.03
        "Bar/barbarawank08.png"
        pause 0.03
        "Bar/barbarawank07.png"
        pause 0.03
        "Bar/barbarawank06.png"
        pause 0.03
        "Bar/barbarawank05.png"
        pause 0.03
        "Bar/barbarawank04.png"
        pause 0.03
        "Bar/barbarawank03.png"
        pause 0.03
        "Bar/barbarawank02.png"
        pause 0.03
        "Bar/barbarawank01.png"
        pause 0.03
        repeat

    image mcharder:
        "School/mchard01.png"
        pause 0.1
        "School/mchard02.png"
        pause 0.1
        "School/mchard03.png"
        pause 0.1
        "School/mchard04.png"
        pause 0.1
        "School/mchard05.png"
        pause 0.1
        "School/mchard06.png"
        pause 0.1
        "School/mchard07.png"
        pause 0.1
        "School/mchard08.png"
        pause 0.1

    image cyrltitsgrow:
        "Cyrl/cyrltitsgrow00.png"
        pause 0.08
        "Cyrl/cyrltitsgrow01.png"
        pause 0.08
        "Cyrl/cyrltitsgrow02.png"
        pause 0.08
        "Cyrl/cyrltitsgrow03.png"
        pause 0.08
        "Cyrl/cyrltitsgrow04.png"
        pause 0.08
        "Cyrl/cyrltitsgrow05.png"
        pause 0.08
        "Cyrl/cyrltitsgrow06.png"
        pause 0.08
        "Cyrl/cyrltitsgrow07.png"
        pause 0.08
        "Cyrl/cyrltitsgrow08.png"
        pause 0.08
        "Cyrl/cyrltitsgrow09.png"
        pause 0.1

    image mcfrancinesex01:
        "School/mcfrancine01.png"
        pause 0.1
        "School/mcfrancine02.png"
        pause 0.1
        "School/mcfrancine03.png"
        pause 0.1
        "School/mcfrancine04.png"
        pause 0.1
        "School/mcfrancine05.png"
        pause 0.1
        "School/mcfrancine06.png"
        pause 0.1
        "School/mcfrancine05.png"
        pause 0.1
        "School/mcfrancine04.png"
        pause 0.1
        "School/mcfrancine03.png"
        pause 0.1
        "School/mcfrancine02.png"
        pause 0.1
        repeat

    image mcfrancinesex02:
        "School/mcfrancine07.png"
        pause 0.1
        "School/mcfrancine08.png"
        pause 0.1
        "School/mcfrancine09.png"
        pause 0.1
        "School/mcfrancine10.png"
        pause 0.1
        "School/mcfrancine11.png"
        pause 0.1
        "School/mcfrancine12.png"
        pause 0.1
        "School/mcfrancine11.png"
        pause 0.1
        "School/mcfrancine10.png"
        pause 0.1
        "School/mcfrancine09.png"
        pause 0.1
        "School/mcfrancine08.png"
        pause 0.1
        repeat
    
    image clarahandjobslow:
        "Stripping/clarahandjob01.png"
        pause 0.06
        "Stripping/clarahandjob02.png"
        pause 0.06
        "Stripping/clarahandjob03.png"
        pause 0.06
        "Stripping/clarahandjob04.png"
        pause 0.06
        "Stripping/clarahandjob05.png"
        pause 0.06
        "Stripping/clarahandjob06.png"
        pause 0.06
        "Stripping/clarahandjob07.png"
        pause 0.06
        "Stripping/clarahandjob08.png"
        pause 0.06
        "Stripping/clarahandjob09.png"
        pause 0.06
        "Stripping/clarahandjob08.png"
        pause 0.06
        "Stripping/clarahandjob07.png"
        pause 0.06
        "Stripping/clarahandjob06.png"
        pause 0.06
        "Stripping/clarahandjob05.png"
        pause 0.06
        "Stripping/clarahandjob04.png"
        pause 0.06
        "Stripping/clarahandjob03.png"
        pause 0.06
        "Stripping/clarahandjob02.png"
        pause 0.06
        repeat

    image clarahandjobfast:
        "Stripping/clarahandjob01.png"
        pause 0.04
        "Stripping/clarahandjob02.png"
        pause 0.04
        "Stripping/clarahandjob03.png"
        pause 0.04
        "Stripping/clarahandjob04.png"
        pause 0.04
        "Stripping/clarahandjob05.png"
        pause 0.04
        "Stripping/clarahandjob06.png"
        pause 0.04
        "Stripping/clarahandjob07.png"
        pause 0.04
        "Stripping/clarahandjob08.png"
        pause 0.04
        "Stripping/clarahandjob09.png"
        pause 0.04
        "Stripping/clarahandjob08.png"
        pause 0.04
        "Stripping/clarahandjob07.png"
        pause 0.04
        "Stripping/clarahandjob06.png"
        pause 0.04
        "Stripping/clarahandjob05.png"
        pause 0.04
        "Stripping/clarahandjob04.png"
        pause 0.04
        "Stripping/clarahandjob03.png"
        pause 0.04
        "Stripping/clarahandjob02.png"
        pause 0.04
        repeat
    
    image pennytitjobslow:
        "Stripping/pennytitjob00.png"
        pause 0.06
        "Stripping/pennytitjob01.png"
        pause 0.06
        "Stripping/pennytitjob02.png"
        pause 0.06
        "Stripping/pennytitjob03.png"
        pause 0.06
        "Stripping/pennytitjob04.png"
        pause 0.06
        "Stripping/pennytitjob05.png"
        pause 0.06
        "Stripping/pennytitjob06.png"
        pause 0.06
        "Stripping/pennytitjob07.png"
        pause 0.06
        "Stripping/pennytitjob08.png"
        pause 0.06
        "Stripping/pennytitjob09.png"
        pause 0.06
        "Stripping/pennytitjob08.png"
        pause 0.06
        "Stripping/pennytitjob07.png"
        pause 0.06
        "Stripping/pennytitjob06.png"
        pause 0.06
        "Stripping/pennytitjob05.png"
        pause 0.06
        "Stripping/pennytitjob04.png"
        pause 0.06
        "Stripping/pennytitjob03.png"
        pause 0.06
        "Stripping/pennytitjob02.png"
        pause 0.06
        "Stripping/pennytitjob01.png"
        pause 0.06
        repeat

    image pennytitjobfast:
        "Stripping/pennytitjob00.png"
        pause 0.04
        "Stripping/pennytitjob01.png"
        pause 0.04
        "Stripping/pennytitjob02.png"
        pause 0.04
        "Stripping/pennytitjob03.png"
        pause 0.04
        "Stripping/pennytitjob04.png"
        pause 0.04
        "Stripping/pennytitjob05.png"
        pause 0.04
        "Stripping/pennytitjob06.png"
        pause 0.04
        "Stripping/pennytitjob07.png"
        pause 0.04
        "Stripping/pennytitjob08.png"
        pause 0.04
        "Stripping/pennytitjob09.png"
        pause 0.06
        "Stripping/pennytitjob08.png"
        pause 0.06
        "Stripping/pennytitjob07.png"
        pause 0.04
        "Stripping/pennytitjob06.png"
        pause 0.04
        "Stripping/pennytitjob05.png"
        pause 0.04
        "Stripping/pennytitjob04.png"
        pause 0.04
        "Stripping/pennytitjob03.png"
        pause 0.04
        "Stripping/pennytitjob02.png"
        pause 0.04
        "Stripping/pennytitjob01.png"
        pause 0.04
        repeat

    image michikofootjobslow:
        "Stripping/michikofootjob00.png"
        pause 0.06
        "Stripping/michikofootjob01.png"
        pause 0.06
        "Stripping/michikofootjob02.png"
        pause 0.06
        "Stripping/michikofootjob03.png"
        pause 0.06
        "Stripping/michikofootjob04.png"
        pause 0.06
        "Stripping/michikofootjob05.png"
        pause 0.06
        "Stripping/michikofootjob06.png"
        pause 0.06
        "Stripping/michikofootjob07.png"
        pause 0.06
        "Stripping/michikofootjob08.png"
        pause 0.06
        "Stripping/michikofootjob07.png"
        pause 0.06
        "Stripping/michikofootjob06.png"
        pause 0.06
        "Stripping/michikofootjob05.png"
        pause 0.06
        "Stripping/michikofootjob04.png"
        pause 0.06
        "Stripping/michikofootjob03.png"
        pause 0.06
        "Stripping/michikofootjob02.png"
        pause 0.06
        "Stripping/michikofootjob01.png"
        pause 0.06
        repeat

    image michikofootjobfast:
        "Stripping/michikofootjob00.png"
        pause 0.04
        "Stripping/michikofootjob01.png"
        pause 0.04
        "Stripping/michikofootjob02.png"
        pause 0.04
        "Stripping/michikofootjob03.png"
        pause 0.04
        "Stripping/michikofootjob04.png"
        pause 0.04
        "Stripping/michikofootjob05.png"
        pause 0.04
        "Stripping/michikofootjob06.png"
        pause 0.04
        "Stripping/michikofootjob07.png"
        pause 0.04
        "Stripping/michikofootjob08.png"
        pause 0.04
        "Stripping/michikofootjob07.png"
        pause 0.04
        "Stripping/michikofootjob06.png"
        pause 0.04
        "Stripping/michikofootjob05.png"
        pause 0.04
        "Stripping/michikofootjob04.png"
        pause 0.04
        "Stripping/michikofootjob03.png"
        pause 0.04
        "Stripping/michikofootjob02.png"
        pause 0.04
        "Stripping/michikofootjob01.png"
        pause 0.04
        repeat    
    
    image nancyfuckslow:
        "Nancy/mcnancy00.png"
        pause 0.06
        "Nancy/mcnancy01.png"
        pause 0.06
        "Nancy/mcnancy02.png"
        pause 0.06
        "Nancy/mcnancy03.png"
        pause 0.06
        "Nancy/mcnancy04.png"
        pause 0.06
        "Nancy/mcnancy05.png"
        pause 0.06
        "Nancy/mcnancy06.png"
        pause 0.06
        "Nancy/mcnancy07.png"
        pause 0.06
        "Nancy/mcnancy08.png"
        pause 0.06
        "Nancy/mcnancy09.png"
        pause 0.10
        "Nancy/mcnancy08.png"
        pause 0.06
        "Nancy/mcnancy07.png"
        pause 0.06
        "Nancy/mcnancy06.png"
        pause 0.06
        "Nancy/mcnancy05.png"
        pause 0.06
        "Nancy/mcnancy04.png"
        pause 0.06
        "Nancy/mcnancy03.png"
        pause 0.06
        "Nancy/mcnancy02.png"
        pause 0.06
        "Nancy/mcnancy01.png"
        pause 0.06
        repeat
            
    image nancyfuckfast:
        "Nancy/mcnancy00.png"
        pause 0.04
        "Nancy/mcnancy01.png"
        pause 0.04
        "Nancy/mcnancy02.png"
        pause 0.04
        "Nancy/mcnancy03.png"
        pause 0.04
        "Nancy/mcnancy04.png"
        pause 0.04
        "Nancy/mcnancy05.png"
        pause 0.04
        "Nancy/mcnancy06.png"
        pause 0.04
        "Nancy/mcnancy07.png"
        pause 0.04
        "Nancy/mcnancy08.png"
        pause 0.04
        "Nancy/mcnancy09.png"
        pause 0.07
        "Nancy/mcnancy08.png"
        pause 0.04
        "Nancy/mcnancy07.png"
        pause 0.04
        "Nancy/mcnancy06.png"
        pause 0.04
        "Nancy/mcnancy05.png"
        pause 0.04
        "Nancy/mcnancy04.png"
        pause 0.04
        "Nancy/mcnancy03.png"
        pause 0.04
        "Nancy/mcnancy02.png"
        pause 0.04
        "Nancy/mcnancy01.png"
        pause 0.04
        repeat

    image nancyliftslow:
        "Nancy/nancylift00.png"
        pause 0.06
        "Nancy/nancylift01.png"
        pause 0.06
        "Nancy/nancylift02.png"
        pause 0.06
        "Nancy/nancylift03.png"
        pause 0.06
        "Nancy/nancylift04.png"
        pause 0.06
        "Nancy/nancylift05.png"
        pause 0.06
        "Nancy/nancylift06.png"
        pause 0.06
        "Nancy/nancylift07.png"
        pause 0.06
        "Nancy/nancylift08.png"
        pause 0.06
        "Nancy/nancylift09.png"
        pause 0.06
        "Nancy/nancylift08.png"
        pause 0.06
        "Nancy/nancylift07.png"
        pause 0.06
        "Nancy/nancylift06.png"
        pause 0.06
        "Nancy/nancylift05.png"
        pause 0.06
        "Nancy/nancylift04.png"
        pause 0.06
        "Nancy/nancylift03.png"
        pause 0.06
        "Nancy/nancylift02.png"
        pause 0.06
        "Nancy/nancylift01.png"
        pause 0.06
        repeat

    image nancyliftfast:
        "Nancy/nancylift00.png"
        pause 0.04
        "Nancy/nancylift01.png"
        pause 0.04
        "Nancy/nancylift02.png"
        pause 0.04
        "Nancy/nancylift03.png"
        pause 0.04
        "Nancy/nancylift04.png"
        pause 0.04
        "Nancy/nancylift05.png"
        pause 0.04
        "Nancy/nancylift06.png"
        pause 0.04
        "Nancy/nancylift07.png"
        pause 0.04
        "Nancy/nancylift08.png"
        pause 0.04
        "Nancy/nancylift09.png"
        pause 0.04
        "Nancy/nancylift08.png"
        pause 0.04
        "Nancy/nancylift07.png"
        pause 0.04
        "Nancy/nancylift06.png"
        pause 0.04
        "Nancy/nancylift05.png"
        pause 0.04
        "Nancy/nancylift04.png"
        pause 0.04
        "Nancy/nancylift03.png"
        pause 0.04
        "Nancy/nancylift02.png"
        pause 0.04
        "Nancy/nancylift01.png"
        pause 0.04
        repeat
    
    image widownancyhjslow:
        "Nancy/widownancyhandjob00.png"
        pause 0.05
        "Nancy/widownancyhandjob01.png"
        pause 0.05
        "Nancy/widownancyhandjob02.png"
        pause 0.05
        "Nancy/widownancyhandjob03.png"
        pause 0.05
        "Nancy/widownancyhandjob04.png"
        pause 0.05
        "Nancy/widownancyhandjob05.png"
        pause 0.05
        "Nancy/widownancyhandjob06.png"
        pause 0.05
        "Nancy/widownancyhandjob07.png"
        pause 0.05
        "Nancy/widownancyhandjob08.png"
        pause 0.05
        "Nancy/widownancyhandjob09.png"
        pause 0.05
        "Nancy/widownancyhandjob10.png"
        pause 0.05
        "Nancy/widownancyhandjob09.png"
        pause 0.05
        "Nancy/widownancyhandjob08.png"
        pause 0.05
        "Nancy/widownancyhandjob07.png"
        pause 0.05
        "Nancy/widownancyhandjob06.png"
        pause 0.05
        "Nancy/widownancyhandjob05.png"
        pause 0.05
        "Nancy/widownancyhandjob04.png"
        pause 0.05
        "Nancy/widownancyhandjob03.png"
        pause 0.05
        "Nancy/widownancyhandjob02.png"
        pause 0.05
        "Nancy/widownancyhandjob01.png"
        pause 0.05
        repeat
     
    image widownancyhjfast:
        "Nancy/widownancyhandjob00.png"
        pause 0.03
        "Nancy/widownancyhandjob01.png"
        pause 0.03
        "Nancy/widownancyhandjob02.png"
        pause 0.03
        "Nancy/widownancyhandjob03.png"
        pause 0.03
        "Nancy/widownancyhandjob04.png"
        pause 0.03
        "Nancy/widownancyhandjob05.png"
        pause 0.03
        "Nancy/widownancyhandjob06.png"
        pause 0.03
        "Nancy/widownancyhandjob07.png"
        pause 0.03
        "Nancy/widownancyhandjob08.png"
        pause 0.03
        "Nancy/widownancyhandjob09.png"
        pause 0.03
        "Nancy/widownancyhandjob10.png"
        pause 0.03
        "Nancy/widownancyhandjob09.png"
        pause 0.03
        "Nancy/widownancyhandjob08.png"
        pause 0.03
        "Nancy/widownancyhandjob07.png"
        pause 0.03
        "Nancy/widownancyhandjob06.png"
        pause 0.03
        "Nancy/widownancyhandjob05.png"
        pause 0.03
        "Nancy/widownancyhandjob04.png"
        pause 0.03
        "Nancy/widownancyhandjob03.png"
        pause 0.03
        "Nancy/widownancyhandjob02.png"
        pause 0.03
        "Nancy/widownancyhandjob01.png"
        pause 0.03
        repeat

    image widownancyfuckaslow:
        "Nancy/widownancyfucka00.png"
        pause 0.05
        "Nancy/widownancyfucka01.png"
        pause 0.05
        "Nancy/widownancyfucka02.png"
        pause 0.05
        "Nancy/widownancyfucka03.png"
        pause 0.05
        "Nancy/widownancyfucka04.png"
        pause 0.05
        "Nancy/widownancyfucka05.png"
        pause 0.05
        "Nancy/widownancyfucka06.png"
        pause 0.05
        "Nancy/widownancyfucka07.png"
        pause 0.05
        "Nancy/widownancyfucka08.png"
        pause 0.05
        "Nancy/widownancyfucka07.png"
        pause 0.05
        "Nancy/widownancyfucka06.png"
        pause 0.05
        "Nancy/widownancyfucka05.png"
        pause 0.05
        "Nancy/widownancyfucka04.png"
        pause 0.05
        "Nancy/widownancyfucka03.png"
        pause 0.05
        "Nancy/widownancyfucka02.png"
        pause 0.05
        "Nancy/widownancyfucka01.png"
        pause 0.05
        repeat    

    image widownancyfuckafast:
        "Nancy/widownancyfucka00.png"
        pause 0.033
        "Nancy/widownancyfucka01.png"
        pause 0.033
        "Nancy/widownancyfucka02.png"
        pause 0.033
        "Nancy/widownancyfucka03.png"
        pause 0.033
        "Nancy/widownancyfucka04.png"
        pause 0.033
        "Nancy/widownancyfucka05.png"
        pause 0.033
        "Nancy/widownancyfucka06.png"
        pause 0.033
        "Nancy/widownancyfucka07.png"
        pause 0.033
        "Nancy/widownancyfucka08.png"
        pause 0.033
        "Nancy/widownancyfucka07.png"
        pause 0.033
        "Nancy/widownancyfucka06.png"
        pause 0.033
        "Nancy/widownancyfucka05.png"
        pause 0.033
        "Nancy/widownancyfucka04.png"
        pause 0.033
        "Nancy/widownancyfucka03.png"
        pause 0.033
        "Nancy/widownancyfucka02.png"
        pause 0.033
        "Nancy/widownancyfucka01.png"
        pause 0.033
        repeat    
        
    image widownancyfuckbslow:
        "Nancy/widownancyfuckb00.png"
        pause 0.05
        "Nancy/widownancyfuckb01.png"
        pause 0.05
        "Nancy/widownancyfuckb02.png"
        pause 0.05
        "Nancy/widownancyfuckb03.png"
        pause 0.05
        "Nancy/widownancyfuckb04.png"
        pause 0.05
        "Nancy/widownancyfuckb05.png"
        pause 0.05
        "Nancy/widownancyfuckb06.png"
        pause 0.05
        "Nancy/widownancyfuckb07.png"
        pause 0.05
        "Nancy/widownancyfuckb08.png"
        pause 0.05
        "Nancy/widownancyfuckb07.png"
        pause 0.05
        "Nancy/widownancyfuckb06.png"
        pause 0.05
        "Nancy/widownancyfuckb05.png"
        pause 0.05
        "Nancy/widownancyfuckb04.png"
        pause 0.05
        "Nancy/widownancyfuckb03.png"
        pause 0.05
        "Nancy/widownancyfuckb02.png"
        pause 0.05
        "Nancy/widownancyfuckb01.png"
        pause 0.05
        repeat    

    image widownancyfuckbfast:
        "Nancy/widownancyfuckb00.png"
        pause 0.033
        "Nancy/widownancyfuckb01.png"
        pause 0.033
        "Nancy/widownancyfuckb02.png"
        pause 0.033
        "Nancy/widownancyfuckb03.png"
        pause 0.033
        "Nancy/widownancyfuckb04.png"
        pause 0.033
        "Nancy/widownancyfuckb05.png"
        pause 0.033
        "Nancy/widownancyfuckb06.png"
        pause 0.033
        "Nancy/widownancyfuckb07.png"
        pause 0.033
        "Nancy/widownancyfuckb08.png"
        pause 0.033
        "Nancy/widownancyfuckb07.png"
        pause 0.033
        "Nancy/widownancyfuckb06.png"
        pause 0.033
        "Nancy/widownancyfuckb05.png"
        pause 0.033
        "Nancy/widownancyfuckb04.png"
        pause 0.033
        "Nancy/widownancyfuckb03.png"
        pause 0.033
        "Nancy/widownancyfuckb02.png"
        pause 0.033
        "Nancy/widownancyfuckb01.png"
        pause 0.033
        repeat    
    
    image widownancyfuckcslow:
        "Nancy/widownancyfuckc00.png"
        pause 0.05
        "Nancy/widownancyfuckc01.png"
        pause 0.05
        "Nancy/widownancyfuckc02.png"
        pause 0.05
        "Nancy/widownancyfuckc03.png"
        pause 0.05
        "Nancy/widownancyfuckc04.png"
        pause 0.05
        "Nancy/widownancyfuckc05.png"
        pause 0.05
        "Nancy/widownancyfuckc06.png"
        pause 0.05
        "Nancy/widownancyfuckc07.png"
        pause 0.05
        "Nancy/widownancyfuckc08.png"
        pause 0.05
        "Nancy/widownancyfuckc07.png"
        pause 0.05
        "Nancy/widownancyfuckc06.png"
        pause 0.05
        "Nancy/widownancyfuckc05.png"
        pause 0.05
        "Nancy/widownancyfuckc04.png"
        pause 0.05
        "Nancy/widownancyfuckc03.png"
        pause 0.05
        "Nancy/widownancyfuckc02.png"
        pause 0.05
        "Nancy/widownancyfuckc01.png"
        pause 0.05
        repeat    

    image widownancyfuckcfast:
        "Nancy/widownancyfuckc00.png"
        pause 0.033
        "Nancy/widownancyfuckc01.png"
        pause 0.033
        "Nancy/widownancyfuckc02.png"
        pause 0.033
        "Nancy/widownancyfuckc03.png"
        pause 0.033
        "Nancy/widownancyfuckc04.png"
        pause 0.033
        "Nancy/widownancyfuckc05.png"
        pause 0.033
        "Nancy/widownancyfuckc06.png"
        pause 0.033
        "Nancy/widownancyfuckc07.png"
        pause 0.033
        "Nancy/widownancyfuckc08.png"
        pause 0.033
        "Nancy/widownancyfuckc07.png"
        pause 0.033
        "Nancy/widownancyfuckc06.png"
        pause 0.033
        "Nancy/widownancyfuckc05.png"
        pause 0.033
        "Nancy/widownancyfuckc04.png"
        pause 0.033
        "Nancy/widownancyfuckc03.png"
        pause 0.033
        "Nancy/widownancyfuckc02.png"
        pause 0.033
        "Nancy/widownancyfuckc01.png"
        pause 0.033
        repeat    

    image widownancyfuckdslow:
        "Nancy/widownancyfuckd00.png"
        pause 0.05
        "Nancy/widownancyfuckd01.png"
        pause 0.05
        "Nancy/widownancyfuckd02.png"
        pause 0.05
        "Nancy/widownancyfuckd03.png"
        pause 0.05
        "Nancy/widownancyfuckd04.png"
        pause 0.05
        "Nancy/widownancyfuckd05.png"
        pause 0.05
        "Nancy/widownancyfuckd06.png"
        pause 0.05
        "Nancy/widownancyfuckd07.png"
        pause 0.05
        "Nancy/widownancyfuckd08.png"
        pause 0.05
        "Nancy/widownancyfuckd07.png"
        pause 0.05
        "Nancy/widownancyfuckd06.png"
        pause 0.05
        "Nancy/widownancyfuckd05.png"
        pause 0.05
        "Nancy/widownancyfuckd04.png"
        pause 0.05
        "Nancy/widownancyfuckd03.png"
        pause 0.05
        "Nancy/widownancyfuckd02.png"
        pause 0.05
        "Nancy/widownancyfuckd01.png"
        pause 0.05
        repeat    

    image widownancyfuckdfast:
        "Nancy/widownancyfuckd00.png"
        pause 0.033
        "Nancy/widownancyfuckd01.png"
        pause 0.033
        "Nancy/widownancyfuckd02.png"
        pause 0.033
        "Nancy/widownancyfuckd03.png"
        pause 0.033
        "Nancy/widownancyfuckd04.png"
        pause 0.033
        "Nancy/widownancyfuckd05.png"
        pause 0.033
        "Nancy/widownancyfuckd06.png"
        pause 0.033
        "Nancy/widownancyfuckd07.png"
        pause 0.033
        "Nancy/widownancyfuckd08.png"
        pause 0.033
        "Nancy/widownancyfuckd07.png"
        pause 0.033
        "Nancy/widownancyfuckd06.png"
        pause 0.033
        "Nancy/widownancyfuckd05.png"
        pause 0.033
        "Nancy/widownancyfuckd04.png"
        pause 0.033
        "Nancy/widownancyfuckd03.png"
        pause 0.033
        "Nancy/widownancyfuckd02.png"
        pause 0.033
        "Nancy/widownancyfuckd01.png"
        pause 0.033
        repeat    

    image nancyarseslow:
        "Nancy/nancyarse00.png"
        pause 0.06
        "Nancy/nancyarse01.png"
        pause 0.06
        "Nancy/nancyarse02.png"
        pause 0.06
        "Nancy/nancyarse03.png"
        pause 0.06
        "Nancy/nancyarse04.png"
        pause 0.06
        "Nancy/nancyarse05.png"
        pause 0.06
        "Nancy/nancyarse06.png"
        pause 0.06
        "Nancy/nancyarse07.png"
        pause 0.06
        "Nancy/nancyarse08.png"
        pause 0.06
        "Nancy/nancyarse09.png"
        pause 0.10
        "Nancy/nancyarse08.png"
        pause 0.06
        "Nancy/nancyarse07.png"
        pause 0.06
        "Nancy/nancyarse06.png"
        pause 0.06
        "Nancy/nancyarse05.png"
        pause 0.06
        "Nancy/nancyarse04.png"
        pause 0.06
        "Nancy/nancyarse03.png"
        pause 0.06
        "Nancy/nancyarse02.png"
        pause 0.06
        "Nancy/nancyarse01.png"
        pause 0.06
        repeat

    image nancyarsefast:
        "Nancy/nancyarse00.png"
        pause 0.04
        "Nancy/nancyarse01.png"
        pause 0.04
        "Nancy/nancyarse02.png"
        pause 0.04
        "Nancy/nancyarse03.png"
        pause 0.04
        "Nancy/nancyarse04.png"
        pause 0.04
        "Nancy/nancyarse05.png"
        pause 0.04
        "Nancy/nancyarse06.png"
        pause 0.04
        "Nancy/nancyarse07.png"
        pause 0.04
        "Nancy/nancyarse08.png"
        pause 0.04
        "Nancy/nancyarse09.png"
        pause 0.07
        "Nancy/nancyarse08.png"
        pause 0.04
        "Nancy/nancyarse07.png"
        pause 0.04
        "Nancy/nancyarse06.png"
        pause 0.04
        "Nancy/nancyarse05.png"
        pause 0.04
        "Nancy/nancyarse04.png"
        pause 0.04
        "Nancy/nancyarse03.png"
        pause 0.04
        "Nancy/nancyarse02.png"
        pause 0.04
        "Nancy/nancyarse01.png"
        pause 0.04
        repeat
    
    image nancytitslow:
        "Nancy/nancytits00.png"
        pause 0.06
        "Nancy/nancytits01.png"
        pause 0.06
        "Nancy/nancytits02.png"
        pause 0.06
        "Nancy/nancytits03.png"
        pause 0.06
        "Nancy/nancytits04.png"
        pause 0.06
        "Nancy/nancytits05.png"
        pause 0.06
        "Nancy/nancytits06.png"
        pause 0.06
        "Nancy/nancytits07.png"
        pause 0.06
        "Nancy/nancytits08.png"
        pause 0.06
        "Nancy/nancytits09.png"
        pause 0.06
        "Nancy/nancytits08.png"
        pause 0.06
        "Nancy/nancytits07.png"
        pause 0.06
        "Nancy/nancytits06.png"
        pause 0.06
        "Nancy/nancytits05.png"
        pause 0.06
        "Nancy/nancytits04.png"
        pause 0.06
        "Nancy/nancytits03.png"
        pause 0.06
        "Nancy/nancytits02.png"
        pause 0.06
        "Nancy/nancytits01.png"
        pause 0.06
        repeat

    image nancytitfast:
        "Nancy/nancytits00.png"
        pause 0.04
        "Nancy/nancytits01.png"
        pause 0.04
        "Nancy/nancytits02.png"
        pause 0.04
        "Nancy/nancytits03.png"
        pause 0.04
        "Nancy/nancytits04.png"
        pause 0.04
        "Nancy/nancytits05.png"
        pause 0.04
        "Nancy/nancytits06.png"
        pause 0.04
        "Nancy/nancytits07.png"
        pause 0.04
        "Nancy/nancytits08.png"
        pause 0.04
        "Nancy/nancytits09.png"
        pause 0.04
        "Nancy/nancytits08.png"
        pause 0.04
        "Nancy/nancytits07.png"
        pause 0.04
        "Nancy/nancytits06.png"
        pause 0.04
        "Nancy/nancytits05.png"
        pause 0.04
        "Nancy/nancytits04.png"
        pause 0.04
        "Nancy/nancytits03.png"
        pause 0.04
        "Nancy/nancytits02.png"
        pause 0.04
        "Nancy/nancytits01.png"
        pause 0.04
        repeat

    image michikotitslow:
        "Michiko/michikotit01.png"
        pause 0.08
        "Michiko/michikotit02.png"
        pause 0.06
        "Michiko/michikotit03.png"
        pause 0.06
        "Michiko/michikotit04.png"
        pause 0.06
        "Michiko/michikotit05.png"
        pause 0.06
        "Michiko/michikotit06.png"
        pause 0.06
        "Michiko/michikotit07.png"
        pause 0.06
        "Michiko/michikotit08.png"
        pause 0.06
        "Michiko/michikotit09.png"
        pause 0.08
        "Michiko/michikotit08.png"
        pause 0.06
        "Michiko/michikotit07.png"
        pause 0.06
        "Michiko/michikotit06.png"
        pause 0.06
        "Michiko/michikotit05.png"
        pause 0.06
        "Michiko/michikotit04.png"
        pause 0.06
        "Michiko/michikotit03.png"
        pause 0.06
        "Michiko/michikotit02.png"
        pause 0.06
        repeat

    image michikotitfast:
        "Michiko/michikotit01.png"
        pause 0.06
        "Michiko/michikotit02.png"
        pause 0.04
        "Michiko/michikotit03.png"
        pause 0.04
        "Michiko/michikotit04.png"
        pause 0.04
        "Michiko/michikotit05.png"
        pause 0.04
        "Michiko/michikotit06.png"
        pause 0.04
        "Michiko/michikotit07.png"
        pause 0.04
        "Michiko/michikotit08.png"
        pause 0.04
        "Michiko/michikotit09.png"
        pause 0.06
        "Michiko/michikotit08.png"
        pause 0.04
        "Michiko/michikotit07.png"
        pause 0.04
        "Michiko/michikotit06.png"
        pause 0.04
        "Michiko/michikotit05.png"
        pause 0.04
        "Michiko/michikotit04.png"
        pause 0.04
        "Michiko/michikotit03.png"
        pause 0.04
        "Michiko/michikotit02.png"
        pause 0.04
        repeat

    image michikofeetslow:
        "Michiko/michikofeet00.png"
        pause 0.05
        "Michiko/michikofeet01.png"
        pause 0.05
        "Michiko/michikofeet02.png"
        pause 0.05
        "Michiko/michikofeet03.png"
        pause 0.05
        "Michiko/michikofeet04.png"
        pause 0.05
        "Michiko/michikofeet05.png"
        pause 0.05
        "Michiko/michikofeet06.png"
        pause 0.05
        "Michiko/michikofeet07.png"
        pause 0.05
        "Michiko/michikofeet08.png"
        pause 0.05
        "Michiko/michikofeet09.png"
        pause 0.05
        "Michiko/michikofeet08.png"
        pause 0.05
        "Michiko/michikofeet07.png"
        pause 0.05
        "Michiko/michikofeet06.png"
        pause 0.05
        "Michiko/michikofeet05.png"
        pause 0.05
        "Michiko/michikofeet04.png"
        pause 0.05
        "Michiko/michikofeet03.png"
        pause 0.05
        "Michiko/michikofeet02.png"
        pause 0.05
        "Michiko/michikofeet01.png"
        pause 0.05
        repeat

    image michikofeetfast:
        "Michiko/michikofeet00.png"
        pause 0.03
        "Michiko/michikofeet01.png"
        pause 0.03
        "Michiko/michikofeet02.png"
        pause 0.03
        "Michiko/michikofeet03.png"
        pause 0.03
        "Michiko/michikofeet04.png"
        pause 0.03
        "Michiko/michikofeet05.png"
        pause 0.03
        "Michiko/michikofeet06.png"
        pause 0.03
        "Michiko/michikofeet07.png"
        pause 0.03
        "Michiko/michikofeet08.png"
        pause 0.03
        "Michiko/michikofeet09.png"
        pause 0.03
        "Michiko/michikofeet08.png"
        pause 0.03
        "Michiko/michikofeet07.png"
        pause 0.03
        "Michiko/michikofeet06.png"
        pause 0.03
        "Michiko/michikofeet05.png"
        pause 0.03
        "Michiko/michikofeet04.png"
        pause 0.03
        "Michiko/michikofeet03.png"
        pause 0.03
        "Michiko/michikofeet02.png"
        pause 0.03
        "Michiko/michikofeet01.png"
        pause 0.03
        repeat

    image michikofeetpovslow:
        "Michiko/michikofeetpov00.png"
        pause 0.05
        "Michiko/michikofeetpov01.png"
        pause 0.05
        "Michiko/michikofeetpov02.png"
        pause 0.05
        "Michiko/michikofeetpov03.png"
        pause 0.05
        "Michiko/michikofeetpov04.png"
        pause 0.05
        "Michiko/michikofeetpov05.png"
        pause 0.05
        "Michiko/michikofeetpov06.png"
        pause 0.05
        "Michiko/michikofeetpov07.png"
        pause 0.05
        "Michiko/michikofeetpov08.png"
        pause 0.05
        "Michiko/michikofeetpov09.png"
        pause 0.05
        "Michiko/michikofeetpov08.png"
        pause 0.05
        "Michiko/michikofeetpov07.png"
        pause 0.05
        "Michiko/michikofeetpov06.png"
        pause 0.05
        "Michiko/michikofeetpov05.png"
        pause 0.05
        "Michiko/michikofeetpov04.png"
        pause 0.05
        "Michiko/michikofeetpov03.png"
        pause 0.05
        "Michiko/michikofeetpov02.png"
        pause 0.05
        "Michiko/michikofeetpov01.png"
        pause 0.05
        repeat

    image michikofeetpovfast:
        "Michiko/michikofeetpov00.png"
        pause 0.03
        "Michiko/michikofeetpov01.png"
        pause 0.03
        "Michiko/michikofeetpov02.png"
        pause 0.03
        "Michiko/michikofeetpov03.png"
        pause 0.03
        "Michiko/michikofeetpov04.png"
        pause 0.03
        "Michiko/michikofeetpov05.png"
        pause 0.03
        "Michiko/michikofeetpov06.png"
        pause 0.03
        "Michiko/michikofeetpov07.png"
        pause 0.03
        "Michiko/michikofeetpov08.png"
        pause 0.03
        "Michiko/michikofeetpov09.png"
        pause 0.03
        "Michiko/michikofeetpov08.png"
        pause 0.03
        "Michiko/michikofeetpov07.png"
        pause 0.03
        "Michiko/michikofeetpov06.png"
        pause 0.03
        "Michiko/michikofeetpov05.png"
        pause 0.03
        "Michiko/michikofeetpov04.png"
        pause 0.03
        "Michiko/michikofeetpov03.png"
        pause 0.03
        "Michiko/michikofeetpov02.png"
        pause 0.03
        "Michiko/michikofeetpov01.png"
        pause 0.03
        repeat

    image michikorefuckslow:
        "Michiko/michikorefuck00.png"
        pause 0.05
        "Michiko/michikorefuck01.png"
        pause 0.05
        "Michiko/michikorefuck02.png"
        pause 0.05
        "Michiko/michikorefuck03.png"
        pause 0.05
        "Michiko/michikorefuck04.png"
        pause 0.05
        "Michiko/michikorefuck05.png"
        pause 0.05
        "Michiko/michikorefuck06.png"
        pause 0.05
        "Michiko/michikorefuck07.png"
        pause 0.05
        "Michiko/michikorefuck08.png"
        pause 0.05
        "Michiko/michikorefuck09.png"
        pause 0.05
        "Michiko/michikorefuck08.png"
        pause 0.05
        "Michiko/michikorefuck07.png"
        pause 0.05
        "Michiko/michikorefuck06.png"
        pause 0.05
        "Michiko/michikorefuck05.png"
        pause 0.05
        "Michiko/michikorefuck04.png"
        pause 0.05
        "Michiko/michikorefuck03.png"
        pause 0.05
        "Michiko/michikorefuck02.png"
        pause 0.05
        "Michiko/michikorefuck01.png"
        pause 0.05
        repeat

    image michikorefuckfast:
        "Michiko/michikorefuck00.png"
        pause 0.03
        "Michiko/michikorefuck01.png"
        pause 0.03
        "Michiko/michikorefuck02.png"
        pause 0.03
        "Michiko/michikorefuck03.png"
        pause 0.03
        "Michiko/michikorefuck04.png"
        pause 0.03
        "Michiko/michikorefuck05.png"
        pause 0.03
        "Michiko/michikorefuck06.png"
        pause 0.03
        "Michiko/michikorefuck07.png"
        pause 0.03
        "Michiko/michikorefuck08.png"
        pause 0.03
        "Michiko/michikorefuck09.png"
        pause 0.03
        "Michiko/michikorefuck08.png"
        pause 0.03
        "Michiko/michikorefuck07.png"
        pause 0.03
        "Michiko/michikorefuck06.png"
        pause 0.03
        "Michiko/michikorefuck05.png"
        pause 0.03
        "Michiko/michikorefuck04.png"
        pause 0.03
        "Michiko/michikorefuck03.png"
        pause 0.03
        "Michiko/michikorefuck02.png"
        pause 0.03
        "Michiko/michikorefuck01.png"
        pause 0.03
        repeat

    image michikopoundslow:
        "Michiko/michikofuck00.png"
        pause 0.05
        "Michiko/michikofuck01.png"
        pause 0.05
        "Michiko/michikofuck02.png"
        pause 0.05
        "Michiko/michikofuck03.png"
        pause 0.05
        "Michiko/michikofuck04.png"
        pause 0.05
        "Michiko/michikofuck05.png"
        pause 0.05
        "Michiko/michikofuck06.png"
        pause 0.05
        "Michiko/michikofuck07.png"
        pause 0.05
        "Michiko/michikofuck08.png"
        pause 0.05
        "Michiko/michikofuck09.png"
        pause 0.05
        "Michiko/michikofuck10.png"
        pause 0.05
        "Michiko/michikofuck11.png"
        pause 0.05
        "Michiko/michikofuck12.png"
        pause 0.05
        "Michiko/michikofuck13.png"
        pause 0.05
        "Michiko/michikofuck14.png"
        pause 0.05
        "Michiko/michikofuck15.png"
        pause 0.05
        "Michiko/michikofuck16.png"
        pause 0.05
        "Michiko/michikofuck17.png"
        pause 0.05
        "Michiko/michikofuck18.png"
        pause 0.05
        repeat

    image michikopoundfast:
        "Michiko/michikofuck00.png"
        pause 0.03
        "Michiko/michikofuck01.png"
        pause 0.03
        "Michiko/michikofuck02.png"
        pause 0.03
        "Michiko/michikofuck03.png"
        pause 0.03
        "Michiko/michikofuck04.png"
        pause 0.03
        "Michiko/michikofuck05.png"
        pause 0.03
        "Michiko/michikofuck06.png"
        pause 0.03
        "Michiko/michikofuck07.png"
        pause 0.03
        "Michiko/michikofuck08.png"
        pause 0.03
        "Michiko/michikofuck09.png"
        pause 0.03
        "Michiko/michikofuck10.png"
        pause 0.03
        "Michiko/michikofuck11.png"
        pause 0.03
        "Michiko/michikofuck12.png"
        pause 0.03
        "Michiko/michikofuck13.png"
        pause 0.03
        "Michiko/michikofuck14.png"
        pause 0.03
        "Michiko/michikofuck15.png"
        pause 0.03
        "Michiko/michikofuck16.png"
        pause 0.03
        "Michiko/michikofuck17.png"
        pause 0.03
        "Michiko/michikofuck18.png"
        pause 0.03
        repeat
    
    image michikopraiseslow:
        "Michiko/michikopraise01.png"
        pause 0.05
        "Michiko/michikopraise02.png"
        pause 0.05
        "Michiko/michikopraise03.png"
        pause 0.05
        "Michiko/michikopraise04.png"
        pause 0.05
        "Michiko/michikopraise05.png"
        pause 0.05
        "Michiko/michikopraise06.png"
        pause 0.05
        "Michiko/michikopraise07.png"
        pause 0.05
        "Michiko/michikopraise08.png"
        pause 0.05
        "Michiko/michikopraise09.png"
        pause 0.05
        "Michiko/michikopraise08.png"
        pause 0.05
        "Michiko/michikopraise07.png"
        pause 0.05
        "Michiko/michikopraise06.png"
        pause 0.05
        "Michiko/michikopraise05.png"
        pause 0.05
        "Michiko/michikopraise04.png"
        pause 0.05
        "Michiko/michikopraise03.png"
        pause 0.05
        "Michiko/michikopraise02.png"
        pause 0.05
        repeat

    image michikopraisefast:
        "Michiko/michikopraise01.png"
        pause 0.03
        "Michiko/michikopraise02.png"
        pause 0.03
        "Michiko/michikopraise03.png"
        pause 0.03
        "Michiko/michikopraise04.png"
        pause 0.03
        "Michiko/michikopraise05.png"
        pause 0.03
        "Michiko/michikopraise06.png"
        pause 0.03
        "Michiko/michikopraise07.png"
        pause 0.03
        "Michiko/michikopraise08.png"
        pause 0.03
        "Michiko/michikopraise09.png"
        pause 0.03
        "Michiko/michikopraise08.png"
        pause 0.03
        "Michiko/michikopraise07.png"
        pause 0.03
        "Michiko/michikopraise06.png"
        pause 0.03
        "Michiko/michikopraise05.png"
        pause 0.03
        "Michiko/michikopraise04.png"
        pause 0.03
        "Michiko/michikopraise03.png"
        pause 0.03
        "Michiko/michikopraise02.png"
        pause 0.03
        repeat

    image cyrlrideslowbig:
        "Cyrl/cyrlrideb00.png"
        pause 0.05
        "Cyrl/cyrlrideb01b.png"
        pause 0.05
        "Cyrl/cyrlrideb02b.png"
        pause 0.05
        "Cyrl/cyrlrideb03b.png"
        pause 0.05
        "Cyrl/cyrlrideb04b.png"
        pause 0.05
        "Cyrl/cyrlrideb05b.png"
        pause 0.05
        "Cyrl/cyrlrideb06b.png"
        pause 0.05
        "Cyrl/cyrlrideb07b.png"
        pause 0.05
        "Cyrl/cyrlrideb08.png"
        pause 0.05
        "Cyrl/cyrlrideb07.png"
        pause 0.05
        "Cyrl/cyrlrideb06.png"
        pause 0.05
        "Cyrl/cyrlrideb05.png"
        pause 0.05
        "Cyrl/cyrlrideb04.png"
        pause 0.05
        "Cyrl/cyrlrideb03.png"
        pause 0.05
        "Cyrl/cyrlrideb02.png"
        pause 0.05
        "Cyrl/cyrlrideb01.png"
        pause 0.05
        repeat

    image cyrlridefastbig:
        "Cyrl/cyrlrideb00.png"
        pause 0.03
        "Cyrl/cyrlrideb01b.png"
        pause 0.03
        "Cyrl/cyrlrideb02b.png"
        pause 0.03
        "Cyrl/cyrlrideb03b.png"
        pause 0.03
        "Cyrl/cyrlrideb04b.png"
        pause 0.03
        "Cyrl/cyrlrideb05b.png"
        pause 0.03
        "Cyrl/cyrlrideb06b.png"
        pause 0.03
        "Cyrl/cyrlrideb07b.png"
        pause 0.03
        "Cyrl/cyrlrideb08.png"
        pause 0.03
        "Cyrl/cyrlrideb07.png"
        pause 0.03
        "Cyrl/cyrlrideb06.png"
        pause 0.03
        "Cyrl/cyrlrideb05.png"
        pause 0.03
        "Cyrl/cyrlrideb04.png"
        pause 0.03
        "Cyrl/cyrlrideb03.png"
        pause 0.03
        "Cyrl/cyrlrideb02.png"
        pause 0.03
        "Cyrl/cyrlrideb01.png"
        pause 0.03
        repeat

    image cyrlfootslow:
        "Cyrl/cyrlfoot00.png"
        pause 0.09
        "Cyrl/cyrlfoot01.png"
        pause 0.06
        "Cyrl/cyrlfoot02.png"
        pause 0.06
        "Cyrl/cyrlfoot03.png"
        pause 0.06
        "Cyrl/cyrlfoot04.png"
        pause 0.06
        "Cyrl/cyrlfoot05.png"
        pause 0.06
        "Cyrl/cyrlfoot06.png"
        pause 0.06
        "Cyrl/cyrlfoot07.png"
        pause 0.06
        "Cyrl/cyrlfoot08.png"
        pause 0.06
        "Cyrl/cyrlfoot09.png"
        pause 0.06
        "Cyrl/cyrlfoot08.png"
        pause 0.06
        "Cyrl/cyrlfoot07.png"
        pause 0.06
        "Cyrl/cyrlfoot06.png"
        pause 0.06
        "Cyrl/cyrlfoot05.png"
        pause 0.06
        "Cyrl/cyrlfoot04.png"
        pause 0.06
        "Cyrl/cyrlfoot03.png"
        pause 0.06
        "Cyrl/cyrlfoot02.png"
        pause 0.06
        "Cyrl/cyrlfoot01.png"
        pause 0.06
        repeat

    image cyrlfootfast:
        "Cyrl/cyrlfoot00.png"
        pause 0.06
        "Cyrl/cyrlfoot01.png"
        pause 0.04
        "Cyrl/cyrlfoot02.png"
        pause 0.04
        "Cyrl/cyrlfoot03.png"
        pause 0.04
        "Cyrl/cyrlfoot04.png"
        pause 0.04
        "Cyrl/cyrlfoot05.png"
        pause 0.04
        "Cyrl/cyrlfoot06.png"
        pause 0.04
        "Cyrl/cyrlfoot07.png"
        pause 0.04
        "Cyrl/cyrlfoot08.png"
        pause 0.04
        "Cyrl/cyrlfoot09.png"
        pause 0.04
        "Cyrl/cyrlfoot08.png"
        pause 0.04
        "Cyrl/cyrlfoot07.png"
        pause 0.04
        "Cyrl/cyrlfoot06.png"
        pause 0.04
        "Cyrl/cyrlfoot05.png"
        pause 0.04
        "Cyrl/cyrlfoot04.png"
        pause 0.04
        "Cyrl/cyrlfoot03.png"
        pause 0.04
        "Cyrl/cyrlfoot02.png"
        pause 0.04
        "Cyrl/cyrlfoot01.png"
        pause 0.04
        repeat

    image cyrlrideslow:
        "Cyrl/cyrlride00.png"
        pause 0.05
        "Cyrl/cyrlride01.png"
        pause 0.05
        "Cyrl/cyrlride02.png"
        pause 0.05
        "Cyrl/cyrlride03.png"
        pause 0.05
        "Cyrl/cyrlride04.png"
        pause 0.05
        "Cyrl/cyrlride05.png"
        pause 0.05
        "Cyrl/cyrlride06.png"
        pause 0.05
        "Cyrl/cyrlride07.png"
        pause 0.05
        "Cyrl/cyrlride08.png"
        pause 0.05
        "Cyrl/cyrlride07.png"
        pause 0.05
        "Cyrl/cyrlride06.png"
        pause 0.05
        "Cyrl/cyrlride05.png"
        pause 0.05
        "Cyrl/cyrlride04.png"
        pause 0.05
        "Cyrl/cyrlride03.png"
        pause 0.05
        "Cyrl/cyrlride02.png"
        pause 0.05
        "Cyrl/cyrlride01.png"
        pause 0.05
        repeat

    image cyrlridefast:
        "Cyrl/cyrlride00.png"
        pause 0.03
        "Cyrl/cyrlride01.png"
        pause 0.03
        "Cyrl/cyrlride02.png"
        pause 0.03
        "Cyrl/cyrlride03.png"
        pause 0.03
        "Cyrl/cyrlride04.png"
        pause 0.03
        "Cyrl/cyrlride05.png"
        pause 0.03
        "Cyrl/cyrlride06.png"
        pause 0.03
        "Cyrl/cyrlride07.png"
        pause 0.03
        "Cyrl/cyrlride08.png"
        pause 0.03
        "Cyrl/cyrlride07.png"
        pause 0.03
        "Cyrl/cyrlride06.png"
        pause 0.03
        "Cyrl/cyrlride05.png"
        pause 0.03
        "Cyrl/cyrlride04.png"
        pause 0.03
        "Cyrl/cyrlride03.png"
        pause 0.03
        "Cyrl/cyrlride02.png"
        pause 0.03
        "Cyrl/cyrlride01.png"
        pause 0.03
        repeat
        
    image cyrltitslow:
        "Cyrl/cyrltit00.png"
        pause 0.06
        "Cyrl/cyrltit01.png"
        pause 0.06
        "Cyrl/cyrltit02.png"
        pause 0.06
        "Cyrl/cyrltit03.png"
        pause 0.06
        "Cyrl/cyrltit04.png"
        pause 0.06
        "Cyrl/cyrltit05.png"
        pause 0.06
        "Cyrl/cyrltit06.png"
        pause 0.06
        "Cyrl/cyrltit07.png"
        pause 0.06
        "Cyrl/cyrltit08.png"
        pause 0.06
        "Cyrl/cyrltit09.png"
        pause 0.06
        "Cyrl/cyrltit08.png"
        pause 0.06
        "Cyrl/cyrltit07.png"
        pause 0.06
        "Cyrl/cyrltit06.png"
        pause 0.06
        "Cyrl/cyrltit05.png"
        pause 0.06
        "Cyrl/cyrltit04.png"
        pause 0.06
        "Cyrl/cyrltit03.png"
        pause 0.06
        "Cyrl/cyrltit02.png"
        pause 0.06
        "Cyrl/cyrltit01.png"
        pause 0.06
        repeat

    image cyrltitslowbig:
        "Cyrl/cyrltitbig00.png"
        pause 0.06
        "Cyrl/cyrltitbig01.png"
        pause 0.06
        "Cyrl/cyrltitbig02.png"
        pause 0.06
        "Cyrl/cyrltitbig03.png"
        pause 0.06
        "Cyrl/cyrltitbig04.png"
        pause 0.06
        "Cyrl/cyrltitbig05.png"
        pause 0.06
        "Cyrl/cyrltitbig06.png"
        pause 0.06
        "Cyrl/cyrltitbig07.png"
        pause 0.06
        "Cyrl/cyrltitbig08.png"
        pause 0.06
        "Cyrl/cyrltitbig09.png"
        pause 0.06
        "Cyrl/cyrltitbig08.png"
        pause 0.06
        "Cyrl/cyrltitbig07.png"
        pause 0.06
        "Cyrl/cyrltitbig06.png"
        pause 0.06
        "Cyrl/cyrltitbig05.png"
        pause 0.06
        "Cyrl/cyrltitbig04.png"
        pause 0.06
        "Cyrl/cyrltitbig03.png"
        pause 0.06
        "Cyrl/cyrltitbig02.png"
        pause 0.06
        "Cyrl/cyrltitbig01.png"
        pause 0.06
        repeat

    image cyrltitfast:
        "Cyrl/cyrltit00.png"
        pause 0.04
        "Cyrl/cyrltit01.png"
        pause 0.04
        "Cyrl/cyrltit02.png"
        pause 0.04
        "Cyrl/cyrltit03.png"
        pause 0.04
        "Cyrl/cyrltit04.png"
        pause 0.04
        "Cyrl/cyrltit05.png"
        pause 0.04
        "Cyrl/cyrltit06.png"
        pause 0.04
        "Cyrl/cyrltit07.png"
        pause 0.04
        "Cyrl/cyrltit08.png"
        pause 0.04
        "Cyrl/cyrltit09.png"
        pause 0.04
        "Cyrl/cyrltit08.png"
        pause 0.04
        "Cyrl/cyrltit07.png"
        pause 0.04
        "Cyrl/cyrltit06.png"
        pause 0.04
        "Cyrl/cyrltit05.png"
        pause 0.04
        "Cyrl/cyrltit04.png"
        pause 0.04
        "Cyrl/cyrltit03.png"
        pause 0.04
        "Cyrl/cyrltit02.png"
        pause 0.04
        "Cyrl/cyrltit01.png"
        pause 0.04
        repeat

    image cyrltitfastbig:
        "Cyrl/cyrltitbig00.png"
        pause 0.04
        "Cyrl/cyrltitbig01.png"
        pause 0.04
        "Cyrl/cyrltitbig02.png"
        pause 0.04
        "Cyrl/cyrltitbig03.png"
        pause 0.04
        "Cyrl/cyrltitbig04.png"
        pause 0.04
        "Cyrl/cyrltitbig05.png"
        pause 0.04
        "Cyrl/cyrltitbig06.png"
        pause 0.04
        "Cyrl/cyrltitbig07.png"
        pause 0.04
        "Cyrl/cyrltitbig08.png"
        pause 0.04
        "Cyrl/cyrltitbig09.png"
        pause 0.04
        "Cyrl/cyrltitbig08.png"
        pause 0.04
        "Cyrl/cyrltitbig07.png"
        pause 0.04
        "Cyrl/cyrltitbig06.png"
        pause 0.04
        "Cyrl/cyrltitbig05.png"
        pause 0.04
        "Cyrl/cyrltitbig04.png"
        pause 0.04
        "Cyrl/cyrltitbig03.png"
        pause 0.04
        "Cyrl/cyrltitbig02.png"
        pause 0.04
        "Cyrl/cyrltitbig01.png"
        pause 0.04
        repeat

    image rubyblowslow:
        "Ruby/rubyblowanim00.png"
        pause 0.04
        "Ruby/rubyblowanim01.png"
        pause 0.04
        "Ruby/rubyblowanim02.png"
        pause 0.04
        "Ruby/rubyblowanim03.png"
        pause 0.04
        "Ruby/rubyblowanim04.png"
        pause 0.04
        "Ruby/rubyblowanim05.png"
        pause 0.04
        "Ruby/rubyblowanim06.png"
        pause 0.04
        "Ruby/rubyblowanim07.png"
        pause 0.04
        "Ruby/rubyblowanim08.png"
        pause 0.04
        "Ruby/rubyblowanim09.png"
        pause 0.04
        "Ruby/rubyblowanim10.png"
        pause 0.04
        "Ruby/rubyblowanim11.png"
        pause 0.04
        "Ruby/rubyblowanim12.png"
        pause 0.04
        "Ruby/rubyblowanim13.png"
        pause 0.04
        "Ruby/rubyblowanim14.png"
        pause 0.04
        "Ruby/rubyblowanim15.png"
        pause 0.04
        "Ruby/rubyblowanim14.png"
        pause 0.04
        "Ruby/rubyblowanim13.png"
        pause 0.04
        "Ruby/rubyblowanim12.png"
        pause 0.04
        "Ruby/rubyblowanim11.png"
        pause 0.04
        "Ruby/rubyblowanim10.png"
        pause 0.04
        "Ruby/rubyblowanim09.png"
        pause 0.04
        "Ruby/rubyblowanim08.png"
        pause 0.04
        "Ruby/rubyblowanim07.png"
        pause 0.04
        "Ruby/rubyblowanim06.png"
        pause 0.04
        "Ruby/rubyblowanim05.png"
        pause 0.04
        "Ruby/rubyblowanim04.png"
        pause 0.04
        "Ruby/rubyblowanim03.png"
        pause 0.04
        "Ruby/rubyblowanim02.png"
        pause 0.04
        "Ruby/rubyblowanim01.png"
        pause 0.04
        repeat

    image rubyblowfast:
        "Ruby/rubyblowanim00.png"
        pause 0.03
        "Ruby/rubyblowanim01.png"
        pause 0.03
        "Ruby/rubyblowanim02.png"
        pause 0.03
        "Ruby/rubyblowanim03.png"
        pause 0.03
        "Ruby/rubyblowanim04.png"
        pause 0.03
        "Ruby/rubyblowanim05.png"
        pause 0.03
        "Ruby/rubyblowanim06.png"
        pause 0.03
        "Ruby/rubyblowanim07.png"
        pause 0.03
        "Ruby/rubyblowanim08.png"
        pause 0.03
        "Ruby/rubyblowanim09.png"
        pause 0.03
        "Ruby/rubyblowanim10.png"
        pause 0.03
        "Ruby/rubyblowanim11.png"
        pause 0.03
        "Ruby/rubyblowanim12.png"
        pause 0.03
        "Ruby/rubyblowanim13.png"
        pause 0.03
        "Ruby/rubyblowanim14.png"
        pause 0.03
        "Ruby/rubyblowanim15.png"
        pause 0.03
        "Ruby/rubyblowanim14.png"
        pause 0.03
        "Ruby/rubyblowanim13.png"
        pause 0.03
        "Ruby/rubyblowanim12.png"
        pause 0.03
        "Ruby/rubyblowanim11.png"
        pause 0.03
        "Ruby/rubyblowanim10.png"
        pause 0.03
        "Ruby/rubyblowanim09.png"
        pause 0.03
        "Ruby/rubyblowanim08.png"
        pause 0.03
        "Ruby/rubyblowanim07.png"
        pause 0.03
        "Ruby/rubyblowanim06.png"
        pause 0.03
        "Ruby/rubyblowanim05.png"
        pause 0.03
        "Ruby/rubyblowanim04.png"
        pause 0.03
        "Ruby/rubyblowanim03.png"
        pause 0.03
        "Ruby/rubyblowanim02.png"
        pause 0.03
        "Ruby/rubyblowanim01.png"
        pause 0.03
        repeat

    image rubypinslow:
        "Ruby/rubypinanim00.png"
        pause 0.04
        "Ruby/rubypinanim01.png"
        pause 0.04
        "Ruby/rubypinanim02.png"
        pause 0.04
        "Ruby/rubypinanim03.png"
        pause 0.04
        "Ruby/rubypinanim04.png"
        pause 0.04
        "Ruby/rubypinanim05.png"
        pause 0.04
        "Ruby/rubypinanim06.png"
        pause 0.04
        "Ruby/rubypinanim07.png"
        pause 0.04
        "Ruby/rubypinanim08.png"
        pause 0.04
        "Ruby/rubypinanim09.png"
        pause 0.04
        "Ruby/rubypinanim10.png"
        pause 0.04
        "Ruby/rubypinanim11.png"
        pause 0.04
        "Ruby/rubypinanim12.png"
        pause 0.04
        "Ruby/rubypinanim13.png"
        pause 0.04
        "Ruby/rubypinanim14.png"
        pause 0.04
        "Ruby/rubypinanim15.png"
        pause 0.04
        "Ruby/rubypinanim16.png"
        pause 0.04
        "Ruby/rubypinanim17.png"
        pause 0.04
        "Ruby/rubypinanim18.png"
        pause 0.04
        "Ruby/rubypinanim19.png"
        pause 0.04
        "Ruby/rubypinanim20.png"
        pause 0.04
        repeat

    image rubypinfast:
        "Ruby/rubypinanim00.png"
        pause 0.03
        "Ruby/rubypinanim01.png"
        pause 0.03
        "Ruby/rubypinanim02.png"
        pause 0.03
        "Ruby/rubypinanim03.png"
        pause 0.03
        "Ruby/rubypinanim04.png"
        pause 0.03
        "Ruby/rubypinanim05.png"
        pause 0.03
        "Ruby/rubypinanim06.png"
        pause 0.03
        "Ruby/rubypinanim07.png"
        pause 0.03
        "Ruby/rubypinanim08.png"
        pause 0.03
        "Ruby/rubypinanim09.png"
        pause 0.03
        "Ruby/rubypinanim10.png"
        pause 0.03
        "Ruby/rubypinanim11.png"
        pause 0.03
        "Ruby/rubypinanim12.png"
        pause 0.03
        "Ruby/rubypinanim13.png"
        pause 0.03
        "Ruby/rubypinanim14.png"
        pause 0.03
        "Ruby/rubypinanim15.png"
        pause 0.03
        "Ruby/rubypinanim16.png"
        pause 0.03
        "Ruby/rubypinanim17.png"
        pause 0.03
        "Ruby/rubypinanim18.png"
        pause 0.03
        "Ruby/rubypinanim19.png"
        pause 0.04
        "Ruby/rubypinanim20.png"
        pause 0.04
        repeat

    image rubyarseslow:
        "Ruby/rubyarse00.png"
        pause 0.05
        "Ruby/rubyarse01.png"
        pause 0.05
        "Ruby/rubyarse02.png"
        pause 0.05
        "Ruby/rubyarse03.png"
        pause 0.05
        "Ruby/rubyarse04.png"
        pause 0.05
        "Ruby/rubyarse05.png"
        pause 0.05
        "Ruby/rubyarse06.png"
        pause 0.05
        "Ruby/rubyarse07.png"
        pause 0.05
        "Ruby/rubyarse08.png"
        pause 0.05
        "Ruby/rubyarse09.png"
        pause 0.05
        "Ruby/rubyarse10.png"
        pause 0.05
        "Ruby/rubyarse09.png"
        pause 0.05
        "Ruby/rubyarse08.png"
        pause 0.05
        "Ruby/rubyarse07.png"
        pause 0.05
        "Ruby/rubyarse06.png"
        pause 0.05
        "Ruby/rubyarse05.png"
        pause 0.05
        "Ruby/rubyarse04.png"
        pause 0.05
        "Ruby/rubyarse03.png"
        pause 0.05
        "Ruby/rubyarse02.png"
        pause 0.05
        "Ruby/rubyarse01.png"
        pause 0.05
        repeat

    image rubyarsefast:
        "Ruby/rubyarse00.png"
        pause 0.03
        "Ruby/rubyarse01.png"
        pause 0.03
        "Ruby/rubyarse02.png"
        pause 0.03
        "Ruby/rubyarse03.png"
        pause 0.03
        "Ruby/rubyarse04.png"
        pause 0.03
        "Ruby/rubyarse05.png"
        pause 0.03
        "Ruby/rubyarse06.png"
        pause 0.03
        "Ruby/rubyarse07.png"
        pause 0.03
        "Ruby/rubyarse08.png"
        pause 0.03
        "Ruby/rubyarse09.png"
        pause 0.03
        "Ruby/rubyarse10.png"
        pause 0.05
        "Ruby/rubyarse09.png"
        pause 0.05
        "Ruby/rubyarse08.png"
        pause 0.03
        "Ruby/rubyarse07.png"
        pause 0.03
        "Ruby/rubyarse06.png"
        pause 0.03
        "Ruby/rubyarse05.png"
        pause 0.03
        "Ruby/rubyarse04.png"
        pause 0.03
        "Ruby/rubyarse03.png"
        pause 0.03
        "Ruby/rubyarse02.png"
        pause 0.03
        "Ruby/rubyarse01.png"
        pause 0.03
        repeat
        
    image rubyarsepovslow:
        "Ruby/rubyarseb00.png"
        pause 0.05
        "Ruby/rubyarseb01.png"
        pause 0.05
        "Ruby/rubyarseb02.png"
        pause 0.05
        "Ruby/rubyarseb03.png"
        pause 0.05
        "Ruby/rubyarseb04.png"
        pause 0.05
        "Ruby/rubyarseb05.png"
        pause 0.05
        "Ruby/rubyarseb06.png"
        pause 0.05
        "Ruby/rubyarseb07.png"
        pause 0.05
        "Ruby/rubyarseb08.png"
        pause 0.05
        "Ruby/rubyarseb09.png"
        pause 0.05
        "Ruby/rubyarseb10.png"
        pause 0.05
        "Ruby/rubyarseb09.png"
        pause 0.05
        "Ruby/rubyarseb08.png"
        pause 0.05
        "Ruby/rubyarseb07.png"
        pause 0.05
        "Ruby/rubyarseb06.png"
        pause 0.05
        "Ruby/rubyarseb05.png"
        pause 0.05
        "Ruby/rubyarseb04.png"
        pause 0.05
        "Ruby/rubyarseb03.png"
        pause 0.05
        "Ruby/rubyarseb02.png"
        pause 0.05
        "Ruby/rubyarseb01.png"
        pause 0.05
        repeat

    image rubyarsepovfast:
        "Ruby/rubyarseb00.png"
        pause 0.03
        "Ruby/rubyarseb01.png"
        pause 0.03
        "Ruby/rubyarseb02.png"
        pause 0.03
        "Ruby/rubyarseb03.png"
        pause 0.03
        "Ruby/rubyarseb04.png"
        pause 0.03
        "Ruby/rubyarseb05.png"
        pause 0.03
        "Ruby/rubyarseb06.png"
        pause 0.03
        "Ruby/rubyarseb07.png"
        pause 0.03
        "Ruby/rubyarseb08.png"
        pause 0.03
        "Ruby/rubyarseb09.png"
        pause 0.03
        "Ruby/rubyarseb10.png"
        pause 0.05
        "Ruby/rubyarseb09.png"
        pause 0.05
        "Ruby/rubyarseb08.png"
        pause 0.03
        "Ruby/rubyarseb07.png"
        pause 0.03
        "Ruby/rubyarseb06.png"
        pause 0.03
        "Ruby/rubyarseb05.png"
        pause 0.03
        "Ruby/rubyarseb04.png"
        pause 0.03
        "Ruby/rubyarseb03.png"
        pause 0.03
        "Ruby/rubyarseb02.png"
        pause 0.03
        "Ruby/rubyarseb01.png"
        pause 0.03
        repeat
 
    image rubyimpaleslow:
        "Ruby/rubyimpale00.png"
        pause 0.05
        "Ruby/rubyimpale01.png"
        pause 0.05
        "Ruby/rubyimpale02.png"
        pause 0.05
        "Ruby/rubyimpale03.png"
        pause 0.05
        "Ruby/rubyimpale04.png"
        pause 0.05
        "Ruby/rubyimpale05.png"
        pause 0.05
        "Ruby/rubyimpale06.png"
        pause 0.05
        "Ruby/rubyimpale07.png"
        pause 0.05
        "Ruby/rubyimpale08.png"
        pause 0.05
        "Ruby/rubyimpale09.png"
        pause 0.05
        "Ruby/rubyimpale10.png"
        pause 0.05
        "Ruby/rubyimpale11.png"
        pause 0.05
        "Ruby/rubyimpale12.png"
        pause 0.05
        "Ruby/rubyimpale13.png"
        pause 0.05
        "Ruby/rubyimpale14.png"
        pause 0.05
        "Ruby/rubyimpale15.png"
        pause 0.05
        "Ruby/rubyimpale16.png"
        pause 0.05
        "Ruby/rubyimpale17.png"
        pause 0.05
        "Ruby/rubyimpale18.png"
        pause 0.05
        "Ruby/rubyimpale19.png"
        pause 0.05
        repeat

    image rubyimpalefast:
        "Ruby/rubyimpale00.png"
        pause 0.03
        "Ruby/rubyimpale01.png"
        pause 0.03
        "Ruby/rubyimpale02.png"
        pause 0.03
        "Ruby/rubyimpale03.png"
        pause 0.03
        "Ruby/rubyimpale04.png"
        pause 0.03
        "Ruby/rubyimpale05.png"
        pause 0.03
        "Ruby/rubyimpale06.png"
        pause 0.03
        "Ruby/rubyimpale07.png"
        pause 0.03
        "Ruby/rubyimpale08.png"
        pause 0.03
        "Ruby/rubyimpale09.png"
        pause 0.03
        "Ruby/rubyimpale10.png"
        pause 0.03
        "Ruby/rubyimpale11.png"
        pause 0.03
        "Ruby/rubyimpale12.png"
        pause 0.03
        "Ruby/rubyimpale13.png"
        pause 0.03
        "Ruby/rubyimpale14.png"
        pause 0.03
        "Ruby/rubyimpale15.png"
        pause 0.03
        "Ruby/rubyimpale16.png"
        pause 0.03
        "Ruby/rubyimpale17.png"
        pause 0.03
        "Ruby/rubyimpale18.png"
        pause 0.03
        "Ruby/rubyimpale19.png"
        pause 0.03
        repeat

    image rubypussyslow:
        "Ruby/rubypussy00.png"
        pause 0.05
        "Ruby/rubypussy01.png"
        pause 0.05
        "Ruby/rubypussy02.png"
        pause 0.05
        "Ruby/rubypussy03.png"
        pause 0.05
        "Ruby/rubypussy04.png"
        pause 0.05
        "Ruby/rubypussy05.png"
        pause 0.05
        "Ruby/rubypussy06.png"
        pause 0.05
        "Ruby/rubypussy07.png"
        pause 0.05
        "Ruby/rubypussy08.png"
        pause 0.05
        "Ruby/rubypussy09.png"
        pause 0.05
        "Ruby/rubypussy08.png"
        pause 0.05
        "Ruby/rubypussy07.png"
        pause 0.05
        "Ruby/rubypussy06.png"
        pause 0.05
        "Ruby/rubypussy05.png"
        pause 0.05
        "Ruby/rubypussy04.png"
        pause 0.05
        "Ruby/rubypussy03.png"
        pause 0.05
        "Ruby/rubypussy02.png"
        pause 0.05
        "Ruby/rubypussy01.png"
        pause 0.05
        repeat

    image rubypussyfast:
        "Ruby/rubypussy00.png"
        pause 0.03
        "Ruby/rubypussy01.png"
        pause 0.03
        "Ruby/rubypussy02.png"
        pause 0.03
        "Ruby/rubypussy03.png"
        pause 0.03
        "Ruby/rubypussy04.png"
        pause 0.03
        "Ruby/rubypussy05.png"
        pause 0.03
        "Ruby/rubypussy06.png"
        pause 0.03
        "Ruby/rubypussy07.png"
        pause 0.03
        "Ruby/rubypussy08.png"
        pause 0.03
        "Ruby/rubypussy09.png"
        pause 0.03
        "Ruby/rubypussy08.png"
        pause 0.03
        "Ruby/rubypussy07.png"
        pause 0.03
        "Ruby/rubypussy06.png"
        pause 0.03
        "Ruby/rubypussy05.png"
        pause 0.03
        "Ruby/rubypussy04.png"
        pause 0.03
        "Ruby/rubypussy03.png"
        pause 0.03
        "Ruby/rubypussy02.png"
        pause 0.03
        "Ruby/rubypussy01.png"
        pause 0.03
        repeat

    image stripperfuckslow:
        "deserttown/stripperfuck00.jpg"
        pause 0.03
        "deserttown/stripperfuck01.jpg"
        pause 0.03
        "deserttown/stripperfuck02.jpg"
        pause 0.03
        "deserttown/stripperfuck03.jpg"
        pause 0.03
        "deserttown/stripperfuck04.jpg"
        pause 0.03
        "deserttown/stripperfuck05.jpg"
        pause 0.03
        "deserttown/stripperfuck06.jpg"
        pause 0.03
        "deserttown/stripperfuck07.jpg"
        pause 0.03
        "deserttown/stripperfuck08.jpg"
        pause 0.03
        "deserttown/stripperfuck09.jpg"
        pause 0.03
        "deserttown/stripperfuck10.jpg"
        pause 0.03
        "deserttown/stripperfuck11.jpg"
        pause 0.03
        "deserttown/stripperfuck12.jpg"
        pause 0.03
        "deserttown/stripperfuck13.jpg"
        pause 0.03
        "deserttown/stripperfuck14.jpg"
        pause 0.03
        "deserttown/stripperfuck15.jpg"
        pause 0.03
        "deserttown/stripperfuck16.jpg"
        pause 0.03
        "deserttown/stripperfuck17.jpg"
        pause 0.03
        "deserttown/stripperfuck18.jpg"
        pause 0.04
        "deserttown/stripperfuck17.jpg"
        pause 0.03
        "deserttown/stripperfuck16.jpg"
        pause 0.03
        "deserttown/stripperfuck15.jpg"
        pause 0.03
        "deserttown/stripperfuck14.jpg"
        pause 0.03
        "deserttown/stripperfuck13.jpg"
        pause 0.03
        "deserttown/stripperfuck12.jpg"
        pause 0.03
        "deserttown/stripperfuck11.jpg"
        pause 0.03
        "deserttown/stripperfuck10.jpg"
        pause 0.03
        "deserttown/stripperfuck09.jpg"
        pause 0.03
        "deserttown/stripperfuck08.jpg"
        pause 0.03
        "deserttown/stripperfuck07.jpg"
        pause 0.03
        "deserttown/stripperfuck06.jpg"
        pause 0.03
        "deserttown/stripperfuck05.jpg"
        pause 0.03
        "deserttown/stripperfuck04.jpg"
        pause 0.03
        "deserttown/stripperfuck03.jpg"
        pause 0.03
        "deserttown/stripperfuck02.jpg"
        pause 0.03
        "deserttown/stripperfuck01.jpg"
        pause 0.03
        repeat
    
    image stripperfuckfast:
        "deserttown/stripperfuck00.jpg"
        pause 0.02
        "deserttown/stripperfuck01.jpg"
        pause 0.02
        "deserttown/stripperfuck02.jpg"
        pause 0.02
        "deserttown/stripperfuck03.jpg"
        pause 0.02
        "deserttown/stripperfuck04.jpg"
        pause 0.02
        "deserttown/stripperfuck05.jpg"
        pause 0.02
        "deserttown/stripperfuck06.jpg"
        pause 0.02
        "deserttown/stripperfuck07.jpg"
        pause 0.02
        "deserttown/stripperfuck08.jpg"
        pause 0.02
        "deserttown/stripperfuck09.jpg"
        pause 0.02
        "deserttown/stripperfuck10.jpg"
        pause 0.02
        "deserttown/stripperfuck11.jpg"
        pause 0.02
        "deserttown/stripperfuck12.jpg"
        pause 0.02
        "deserttown/stripperfuck13.jpg"
        pause 0.02
        "deserttown/stripperfuck14.jpg"
        pause 0.02
        "deserttown/stripperfuck15.jpg"
        pause 0.02
        "deserttown/stripperfuck16.jpg"
        pause 0.02
        "deserttown/stripperfuck17.jpg"
        pause 0.02
        "deserttown/stripperfuck18.jpg"
        pause 0.03
        "deserttown/stripperfuck17.jpg"
        pause 0.02
        "deserttown/stripperfuck16.jpg"
        pause 0.02
        "deserttown/stripperfuck15.jpg"
        pause 0.02
        "deserttown/stripperfuck14.jpg"
        pause 0.02
        "deserttown/stripperfuck13.jpg"
        pause 0.02
        "deserttown/stripperfuck12.jpg"
        pause 0.02
        "deserttown/stripperfuck11.jpg"
        pause 0.02
        "deserttown/stripperfuck10.jpg"
        pause 0.02
        "deserttown/stripperfuck09.jpg"
        pause 0.02
        "deserttown/stripperfuck08.jpg"
        pause 0.02
        "deserttown/stripperfuck07.jpg"
        pause 0.02
        "deserttown/stripperfuck06.jpg"
        pause 0.02
        "deserttown/stripperfuck05.jpg"
        pause 0.02
        "deserttown/stripperfuck04.jpg"
        pause 0.02
        "deserttown/stripperfuck03.jpg"
        pause 0.02
        "deserttown/stripperfuck02.jpg"
        pause 0.02
        "deserttown/stripperfuck01.jpg"
        pause 0.02
        repeat

    image opalablowslow:
        "Explore/opalablow00.png"
        pause 0.04
        "Explore/opalablow01.png"
        pause 0.04
        "Explore/opalablow02.png"
        pause 0.04
        "Explore/opalablow03.png"
        pause 0.04
        "Explore/opalablow04.png"
        pause 0.04
        "Explore/opalablow05.png"
        pause 0.04
        "Explore/opalablow06.png"
        pause 0.04
        "Explore/opalablow07.png"
        pause 0.04
        "Explore/opalablow08.png"
        pause 0.04
        "Explore/opalablow09.png"
        pause 0.04
        "Explore/opalablow10.png"
        pause 0.04
        "Explore/opalablow09.png"
        pause 0.04
        "Explore/opalablow08.png"
        pause 0.04
        "Explore/opalablow07.png"
        pause 0.04
        "Explore/opalablow06.png"
        pause 0.04
        "Explore/opalablow05.png"
        pause 0.04
        "Explore/opalablow04.png"
        pause 0.04
        "Explore/opalablow03.png"
        pause 0.04
        "Explore/opalablow02.png"
        pause 0.04
        "Explore/opalablow01.png"
        pause 0.04
        repeat

    image opalablowfast:
        "Explore/opalablow00.png"
        pause 0.03
        "Explore/opalablow01.png"
        pause 0.03
        "Explore/opalablow02.png"
        pause 0.03
        "Explore/opalablow03.png"
        pause 0.03
        "Explore/opalablow04.png"
        pause 0.03
        "Explore/opalablow05.png"
        pause 0.03
        "Explore/opalablow06.png"
        pause 0.03
        "Explore/opalablow07.png"
        pause 0.03
        "Explore/opalablow08.png"
        pause 0.03
        "Explore/opalablow09.png"
        pause 0.03
        "Explore/opalablow10.png"
        pause 0.03
        "Explore/opalablow09.png"
        pause 0.03
        "Explore/opalablow08.png"
        pause 0.03
        "Explore/opalablow07.png"
        pause 0.03
        "Explore/opalablow06.png"
        pause 0.03
        "Explore/opalablow05.png"
        pause 0.03
        "Explore/opalablow04.png"
        pause 0.03
        "Explore/opalablow03.png"
        pause 0.03
        "Explore/opalablow02.png"
        pause 0.03
        "Explore/opalablow01.png"
        pause 0.03
        repeat
        
    image ivankadeskslow:
        "Explore/idesk00.png"
        pause 0.03
        "Explore/idesk01.png"
        pause 0.03
        "Explore/idesk02.png"
        pause 0.03
        "Explore/idesk03.png"
        pause 0.03
        "Explore/idesk04.png"
        pause 0.03
        "Explore/idesk05.png"
        pause 0.03
        "Explore/idesk06.png"
        pause 0.03
        "Explore/idesk07.png"
        pause 0.03
        "Explore/idesk08.png"
        pause 0.03
        "Explore/idesk09.png"
        pause 0.03
        "Explore/idesk10.png"
        pause 0.03
        "Explore/idesk11.png"
        pause 0.03
        "Explore/idesk12.png"
        pause 0.03
        "Explore/idesk13.png"
        pause 0.03
        "Explore/idesk14.png"
        pause 0.03
        "Explore/idesk15.png"
        pause 0.03
        "Explore/idesk16.png"
        pause 0.03
        "Explore/idesk17.png"
        pause 0.03
        "Explore/idesk18.png"
        pause 0.03
        "Explore/idesk19.png"
        pause 0.03
        "Explore/idesk20.png"
        pause 0.03
        "Explore/idesk21.png"
        pause 0.03
        "Explore/idesk22.png"
        pause 0.03
        "Explore/idesk23.png"
        pause 0.03
        "Explore/idesk24.png"
        pause 0.03
        repeat
    
    image ivankadeskfast:
        "Explore/idesk00.png"
        pause 0.02
        "Explore/idesk01.png"
        pause 0.02
        "Explore/idesk02.png"
        pause 0.02
        "Explore/idesk03.png"
        pause 0.02
        "Explore/idesk04.png"
        pause 0.02
        "Explore/idesk05.png"
        pause 0.02
        "Explore/idesk06.png"
        pause 0.02
        "Explore/idesk07.png"
        pause 0.02
        "Explore/idesk08.png"
        pause 0.02
        "Explore/idesk09.png"
        pause 0.02
        "Explore/idesk10.png"
        pause 0.02
        "Explore/idesk11.png"
        pause 0.02
        "Explore/idesk12.png"
        pause 0.02
        "Explore/idesk13.png"
        pause 0.02
        "Explore/idesk14.png"
        pause 0.02
        "Explore/idesk15.png"
        pause 0.02
        "Explore/idesk16.png"
        pause 0.02
        "Explore/idesk17.png"
        pause 0.02
        "Explore/idesk18.png"
        pause 0.02
        "Explore/idesk19.png"
        pause 0.02
        "Explore/idesk20.png"
        pause 0.02
        "Explore/idesk21.png"
        pause 0.02
        "Explore/idesk22.png"
        pause 0.02
        "Explore/idesk23.png"
        pause 0.02
        "Explore/idesk24.png"
        pause 0.02
        repeat
    
    image ivankaanalslow:
        "Explore/ivankanal10.png"
        pause 0.04
        "Explore/ivankanal09.png"
        pause 0.04
        "Explore/ivankanal08.png"
        pause 0.04
        "Explore/ivankanal07.png"
        pause 0.04
        "Explore/ivankanal06.png"
        pause 0.04
        "Explore/ivankanal05.png"
        pause 0.04
        "Explore/ivankanal04.png"
        pause 0.04
        "Explore/ivankanal03.png"
        pause 0.04
        "Explore/ivankanal02.png"
        pause 0.04
        "Explore/ivankanal01.png"
        pause 0.04
        "Explore/ivankanal00.png"
        pause 0.06
        "Explore/ivankanal01.png"
        pause 0.04
        "Explore/ivankanal02.png"
        pause 0.04
        "Explore/ivankanal03.png"
        pause 0.04
        "Explore/ivankanal04.png"
        pause 0.04
        "Explore/ivankanal05.png"
        pause 0.04
        "Explore/ivankanal06.png"
        pause 0.04
        "Explore/ivankanal07.png"
        pause 0.04
        "Explore/ivankanal08.png"
        pause 0.04
        "Explore/ivankanal09.png"
        pause 0.04
        repeat

    image ivankaanalfast:
        "Explore/ivankanal10.png"
        pause 0.03
        "Explore/ivankanal09.png"
        pause 0.03
        "Explore/ivankanal08.png"
        pause 0.03
        "Explore/ivankanal07.png"
        pause 0.03
        "Explore/ivankanal06.png"
        pause 0.03
        "Explore/ivankanal05.png"
        pause 0.03
        "Explore/ivankanal04.png"
        pause 0.03
        "Explore/ivankanal03.png"
        pause 0.03
        "Explore/ivankanal02.png"
        pause 0.03
        "Explore/ivankanal01.png"
        pause 0.03
        "Explore/ivankanal00.png"
        pause 0.04
        "Explore/ivankanal01.png"
        pause 0.03
        "Explore/ivankanal02.png"
        pause 0.03
        "Explore/ivankanal03.png"
        pause 0.03
        "Explore/ivankanal04.png"
        pause 0.03
        "Explore/ivankanal05.png"
        pause 0.03
        "Explore/ivankanal06.png"
        pause 0.03
        "Explore/ivankanal07.png"
        pause 0.03
        "Explore/ivankanal08.png"
        pause 0.03
        "Explore/ivankanal09.png"
        pause 0.03
        repeat

    
    image opalafuckslow:
        "Explore/opalafuck00.png"
        pause 0.04
        "Explore/opalafuck01.png"
        pause 0.04
        "Explore/opalafuck02.png"
        pause 0.04
        "Explore/opalafuck03.png"
        pause 0.04
        "Explore/opalafuck04.png"
        pause 0.04
        "Explore/opalafuck05.png"
        pause 0.04
        "Explore/opalafuck06.png"
        pause 0.04
        "Explore/opalafuck07.png"
        pause 0.04
        "Explore/opalafuck08.png"
        pause 0.04
        "Explore/opalafuck09.png"
        pause 0.04
        "Explore/opalafuck10.png"
        pause 0.04
        "Explore/opalafuck11.png"
        pause 0.04
        "Explore/opalafuck12.png"
        pause 0.04
        "Explore/opalafuck13.png"
        pause 0.04
        "Explore/opalafuck14.png"
        pause 0.04
        "Explore/opalafuck15.png"
        pause 0.04
        "Explore/opalafuck16.png"
        pause 0.04
        "Explore/opalafuck17.png"
        pause 0.04
        "Explore/opalafuck18.png"
        pause 0.04
        "Explore/opalafuck19.png"
        pause 0.04
        repeat

    image opalafuckfast:
        "Explore/opalafuck00.png"
        pause 0.03
        "Explore/opalafuck01.png"
        pause 0.03
        "Explore/opalafuck02.png"
        pause 0.03
        "Explore/opalafuck03.png"
        pause 0.03
        "Explore/opalafuck04.png"
        pause 0.03
        "Explore/opalafuck05.png"
        pause 0.03
        "Explore/opalafuck06.png"
        pause 0.03
        "Explore/opalafuck07.png"
        pause 0.03
        "Explore/opalafuck08.png"
        pause 0.03
        "Explore/opalafuck09.png"
        pause 0.03
        "Explore/opalafuck10.png"
        pause 0.03
        "Explore/opalafuck11.png"
        pause 0.03
        "Explore/opalafuck12.png"
        pause 0.03
        "Explore/opalafuck13.png"
        pause 0.03
        "Explore/opalafuck14.png"
        pause 0.03
        "Explore/opalafuck15.png"
        pause 0.03
        "Explore/opalafuck16.png"
        pause 0.03
        "Explore/opalafuck17.png"
        pause 0.03
        "Explore/opalafuck18.png"
        pause 0.03
        "Explore/opalafuck19.png"
        pause 0.03
        repeat

    image oraclefuckslow:
        "Explore/oraclefuck00.jpg"
        pause 0.04
        "Explore/oraclefuck01.jpg"
        pause 0.04
        "Explore/oraclefuck02.jpg"
        pause 0.04
        "Explore/oraclefuck03.jpg"
        pause 0.04
        "Explore/oraclefuck04.jpg"
        pause 0.04
        "Explore/oraclefuck05.jpg"
        pause 0.04
        "Explore/oraclefuck06.jpg"
        pause 0.04
        "Explore/oraclefuck07.jpg"
        pause 0.04
        "Explore/oraclefuck08.jpg"
        pause 0.04
        "Explore/oraclefuck09.jpg"
        pause 0.04
        "Explore/oraclefuck10.jpg"
        pause 0.04
        "Explore/oraclefuck11.jpg"
        pause 0.04
        "Explore/oraclefuck12.jpg"
        pause 0.04
        "Explore/oraclefuck13.jpg"
        pause 0.04
        "Explore/oraclefuck14.jpg"
        pause 0.04
        "Explore/oraclefuck15.jpg"
        pause 0.04
        "Explore/oraclefuck16.jpg"
        pause 0.04
        "Explore/oraclefuck17.jpg"
        pause 0.04
        "Explore/oraclefuck18.jpg"
        pause 0.04
        "Explore/oraclefuck19.jpg"
        pause 0.04
        "Explore/oraclefuck20.jpg"
        pause 0.04
        "Explore/oraclefuck21.jpg"
        pause 0.04
        repeat

    image oraclefuckfast:
        "Explore/oraclefuck00.jpg"
        pause 0.03
        "Explore/oraclefuck01.jpg"
        pause 0.03
        "Explore/oraclefuck02.jpg"
        pause 0.03
        "Explore/oraclefuck03.jpg"
        pause 0.03
        "Explore/oraclefuck04.jpg"
        pause 0.03
        "Explore/oraclefuck05.jpg"
        pause 0.03
        "Explore/oraclefuck06.jpg"
        pause 0.03
        "Explore/oraclefuck07.jpg"
        pause 0.03
        "Explore/oraclefuck08.jpg"
        pause 0.03
        "Explore/oraclefuck09.jpg"
        pause 0.03
        "Explore/oraclefuck10.jpg"
        pause 0.03
        "Explore/oraclefuck11.jpg"
        pause 0.03
        "Explore/oraclefuck12.jpg"
        pause 0.03
        "Explore/oraclefuck13.jpg"
        pause 0.03
        "Explore/oraclefuck14.jpg"
        pause 0.03
        "Explore/oraclefuck15.jpg"
        pause 0.03
        "Explore/oraclefuck16.jpg"
        pause 0.03
        "Explore/oraclefuck17.jpg"
        pause 0.03
        "Explore/oraclefuck18.jpg"
        pause 0.03
        "Explore/oraclefuck19.jpg"
        pause 0.03
        "Explore/oraclefuck20.jpg"
        pause 0.03
        "Explore/oraclefuck21.jpg"
        pause 0.03
        repeat

    image shehulkslow:
        "Explore/shehulkdoggy00.png"
        pause 0.04
        "Explore/shehulkdoggy01.png"
        pause 0.04
        "Explore/shehulkdoggy02.png"
        pause 0.04
        "Explore/shehulkdoggy03.png"
        pause 0.04
        "Explore/shehulkdoggy04.png"
        pause 0.04
        "Explore/shehulkdoggy05.png"
        pause 0.04
        "Explore/shehulkdoggy06.png"
        pause 0.04
        "Explore/shehulkdoggy07.png"
        pause 0.04
        "Explore/shehulkdoggy08.png"
        pause 0.04
        "Explore/shehulkdoggy09.png"
        pause 0.04
        "Explore/shehulkdoggy08.png"
        pause 0.04
        "Explore/shehulkdoggy07.png"
        pause 0.04
        "Explore/shehulkdoggy06.png"
        pause 0.04
        "Explore/shehulkdoggy05.png"
        pause 0.04
        "Explore/shehulkdoggy04.png"
        pause 0.04
        "Explore/shehulkdoggy03.png"
        pause 0.04
        "Explore/shehulkdoggy02.png"
        pause 0.04
        "Explore/shehulkdoggy01.png"
        pause 0.04
        repeat

    image shehulkfast:
        "Explore/shehulkdoggy00.png"
        pause 0.03
        "Explore/shehulkdoggy01.png"
        pause 0.03
        "Explore/shehulkdoggy02.png"
        pause 0.03
        "Explore/shehulkdoggy03.png"
        pause 0.03
        "Explore/shehulkdoggy04.png"
        pause 0.03
        "Explore/shehulkdoggy05.png"
        pause 0.03
        "Explore/shehulkdoggy06.png"
        pause 0.03
        "Explore/shehulkdoggy07.png"
        pause 0.03
        "Explore/shehulkdoggy08.png"
        pause 0.03
        "Explore/shehulkdoggy09.png"
        pause 0.03
        "Explore/shehulkdoggy08.png"
        pause 0.03
        "Explore/shehulkdoggy07.png"
        pause 0.03
        "Explore/shehulkdoggy06.png"
        pause 0.03
        "Explore/shehulkdoggy05.png"
        pause 0.03
        "Explore/shehulkdoggy04.png"
        pause 0.03
        "Explore/shehulkdoggy03.png"
        pause 0.03
        "Explore/shehulkdoggy02.png"
        pause 0.03
        "Explore/shehulkdoggy01.png"
        pause 0.03
        repeat
    
    image amyliftslow:
        "Amy/amylift00.png"
        pause 0.04
        "Amy/amylift01.png"
        pause 0.04
        "Amy/amylift02.png"
        pause 0.04
        "Amy/amylift03.png"
        pause 0.04
        "Amy/amylift04.png"
        pause 0.04
        "Amy/amylift05.png"
        pause 0.04
        "Amy/amylift06.png"
        pause 0.04
        "Amy/amylift07.png"
        pause 0.04
        "Amy/amylift08.png"
        pause 0.04
        "Amy/amylift09.png"
        pause 0.04
        "Amy/amylift08.png"
        pause 0.04
        "Amy/amylift07.png"
        pause 0.04
        "Amy/amylift06.png"
        pause 0.04
        "Amy/amylift05.png"
        pause 0.04
        "Amy/amylift04.png"
        pause 0.04
        "Amy/amylift03.png"
        pause 0.04
        "Amy/amylift02.png"
        pause 0.04
        "Amy/amylift01.png"
        pause 0.04
        repeat

    image amyliftfast:
        "Amy/amylift00.png"
        pause 0.03
        "Amy/amylift01.png"
        pause 0.03
        "Amy/amylift02.png"
        pause 0.03
        "Amy/amylift03.png"
        pause 0.03
        "Amy/amylift04.png"
        pause 0.03
        "Amy/amylift05.png"
        pause 0.03
        "Amy/amylift06.png"
        pause 0.03
        "Amy/amylift07.png"
        pause 0.03
        "Amy/amylift08.png"
        pause 0.03
        "Amy/amylift09.png"
        pause 0.03
        "Amy/amylift08.png"
        pause 0.03
        "Amy/amylift07.png"
        pause 0.03
        "Amy/amylift06.png"
        pause 0.03
        "Amy/amylift05.png"
        pause 0.03
        "Amy/amylift04.png"
        pause 0.03
        "Amy/amylift03.png"
        pause 0.03
        "Amy/amylift02.png"
        pause 0.03
        "Amy/amylift01.png"
        pause 0.03
        repeat

    image amymissionaryslow:
        "Amy/amymissionary00.png"
        pause 0.04
        "Amy/amymissionary01.png"
        pause 0.04
        "Amy/amymissionary02.png"
        pause 0.04
        "Amy/amymissionary03.png"
        pause 0.04
        "Amy/amymissionary04.png"
        pause 0.04
        "Amy/amymissionary05.png"
        pause 0.04
        "Amy/amymissionary06.png"
        pause 0.04
        "Amy/amymissionary07.png"
        pause 0.04
        "Amy/amymissionary08.png"
        pause 0.04
        "Amy/amymissionary09.png"
        pause 0.04
        "Amy/amymissionary10.png"
        pause 0.04
        "Amy/amymissionary11.png"
        pause 0.04
        "Amy/amymissionary12.png"
        pause 0.04
        "Amy/amymissionary13.png"
        pause 0.04
        "Amy/amymissionary14.png"
        pause 0.04
        "Amy/amymissionary15.png"
        pause 0.04
        "Amy/amymissionary16.png"
        pause 0.04
        "Amy/amymissionary17.png"
        pause 0.04
        "Amy/amymissionary18.png"
        pause 0.04
        "Amy/amymissionary19.png"
        pause 0.04
        "Amy/amymissionary20.png"
        pause 0.04
        repeat

    image amymissionaryfast:
        "Amy/amymissionary00.png"
        pause 0.03
        "Amy/amymissionary01.png"
        pause 0.03
        "Amy/amymissionary02.png"
        pause 0.03
        "Amy/amymissionary03.png"
        pause 0.03
        "Amy/amymissionary04.png"
        pause 0.03
        "Amy/amymissionary05.png"
        pause 0.03
        "Amy/amymissionary06.png"
        pause 0.03
        "Amy/amymissionary07.png"
        pause 0.03
        "Amy/amymissionary08.png"
        pause 0.03
        "Amy/amymissionary09.png"
        pause 0.03
        "Amy/amymissionary10.png"
        pause 0.03
        "Amy/amymissionary11.png"
        pause 0.03
        "Amy/amymissionary12.png"
        pause 0.03
        "Amy/amymissionary13.png"
        pause 0.03
        "Amy/amymissionary14.png"
        pause 0.03
        "Amy/amymissionary15.png"
        pause 0.03
        "Amy/amymissionary16.png"
        pause 0.03
        "Amy/amymissionary17.png"
        pause 0.03
        "Amy/amymissionary18.png"
        pause 0.03
        "Amy/amymissionary19.png"
        pause 0.03
        "Amy/amymissionary20.png"
        pause 0.03
        repeat

    image amycockslow:
        "Amy/amycock00.png"
        pause 0.04
        "Amy/amycock01.png"
        pause 0.04
        "Amy/amycock02.png"
        pause 0.04
        "Amy/amycock03.png"
        pause 0.04
        "Amy/amycock04.png"
        pause 0.04
        "Amy/amycock05.png"
        pause 0.04
        "Amy/amycock06.png"
        pause 0.04
        "Amy/amycock07.png"
        pause 0.04
        "Amy/amycock08.png"
        pause 0.04
        "Amy/amycock09.png"
        pause 0.04
        "Amy/amycock10.png"
        pause 0.04
        "Amy/amycock11.png"
        pause 0.04
        "Amy/amycock12.png"
        pause 0.04
        "Amy/amycock13.png"
        pause 0.04
        "Amy/amycock14.png"
        pause 0.04
        "Amy/amycock15.png"
        pause 0.04
        "Amy/amycock16.png"
        pause 0.04
        "Amy/amycock17.png"
        pause 0.04
        "Amy/amycock18.png"
        pause 0.04
        "Amy/amycock19.png"
        pause 0.04
        "Amy/amycock20.png"
        pause 0.04
        repeat

    image amycockfast:
        "Amy/amycock00.png"
        pause 0.03
        "Amy/amycock01.png"
        pause 0.03
        "Amy/amycock02.png"
        pause 0.03
        "Amy/amycock03.png"
        pause 0.03
        "Amy/amycock04.png"
        pause 0.03
        "Amy/amycock05.png"
        pause 0.03
        "Amy/amycock06.png"
        pause 0.03
        "Amy/amycock07.png"
        pause 0.03
        "Amy/amycock08.png"
        pause 0.03
        "Amy/amycock09.png"
        pause 0.03
        "Amy/amycock10.png"
        pause 0.03
        "Amy/amycock11.png"
        pause 0.03
        "Amy/amycock12.png"
        pause 0.03
        "Amy/amycock13.png"
        pause 0.03
        "Amy/amycock14.png"
        pause 0.03
        "Amy/amycock15.png"
        pause 0.03
        "Amy/amycock16.png"
        pause 0.03
        "Amy/amycock17.png"
        pause 0.03
        "Amy/amycock18.png"
        pause 0.03
        "Amy/amycock19.png"
        pause 0.03
        "Amy/amycock20.png"
        pause 0.03
        repeat

    image amysidefast:
        "Amy/amybehind00.png"
        pause 0.02
        "Amy/amybehind01.png"
        pause 0.02
        "Amy/amybehind02.png"
        pause 0.02
        "Amy/amybehind03.png"
        pause 0.02
        "Amy/amybehind04.png"
        pause 0.02
        "Amy/amybehind05.png"
        pause 0.02
        "Amy/amybehind06.png"
        pause 0.02
        "Amy/amybehind07.png"
        pause 0.02
        "Amy/amybehind08.png"
        pause 0.02
        "Amy/amybehind09.png"
        pause 0.02
        "Amy/amybehind10.png"
        pause 0.02
        "Amy/amybehind11.png"
        pause 0.02
        "Amy/amybehind12.png"
        pause 0.02
        "Amy/amybehind13.png"
        pause 0.02
        "Amy/amybehind14.png"
        pause 0.02
        "Amy/amybehind15.png"
        pause 0.02
        "Amy/amybehind16.png"
        pause 0.02
        "Amy/amybehind17.png"
        pause 0.02
        "Amy/amybehind18.png"
        pause 0.02
        "Amy/amybehind19.png"
        pause 0.02
        "Amy/amybehind20.png"
        pause 0.02
        repeat

    image amysideslow:
        "Amy/amybehind00.png"
        pause 0.03
        "Amy/amybehind01.png"
        pause 0.03
        "Amy/amybehind02.png"
        pause 0.03
        "Amy/amybehind03.png"
        pause 0.03
        "Amy/amybehind04.png"
        pause 0.03
        "Amy/amybehind05.png"
        pause 0.03
        "Amy/amybehind06.png"
        pause 0.03
        "Amy/amybehind07.png"
        pause 0.03
        "Amy/amybehind08.png"
        pause 0.03
        "Amy/amybehind09.png"
        pause 0.03
        "Amy/amybehind10.png"
        pause 0.03
        "Amy/amybehind11.png"
        pause 0.03
        "Amy/amybehind12.png"
        pause 0.03
        "Amy/amybehind13.png"
        pause 0.03
        "Amy/amybehind14.png"
        pause 0.03
        "Amy/amybehind15.png"
        pause 0.03
        "Amy/amybehind16.png"
        pause 0.03
        "Amy/amybehind17.png"
        pause 0.03
        "Amy/amybehind18.png"
        pause 0.03
        "Amy/amybehind19.png"
        pause 0.03
        "Amy/amybehind20.png"
        pause 0.03
        repeat
    
    image amyhandslow:
        "Amy/amyhandjob00.png"
        pause 0.04
        "Amy/amyhandjob01.png"
        pause 0.04
        "Amy/amyhandjob02.png"
        pause 0.04
        "Amy/amyhandjob03.png"
        pause 0.04
        "Amy/amyhandjob04.png"
        pause 0.04
        "Amy/amyhandjob05.png"
        pause 0.04
        "Amy/amyhandjob06.png"
        pause 0.04
        "Amy/amyhandjob07.png"
        pause 0.04
        "Amy/amyhandjob08.png"
        pause 0.04
        "Amy/amyhandjob09.png"
        pause 0.04
        "Amy/amyhandjob10.png"
        pause 0.04
        "Amy/amyhandjob09.png"
        pause 0.04
        "Amy/amyhandjob08.png"
        pause 0.04
        "Amy/amyhandjob07.png"
        pause 0.04
        "Amy/amyhandjob06.png"
        pause 0.04
        "Amy/amyhandjob05.png"
        pause 0.04
        "Amy/amyhandjob04.png"
        pause 0.04
        "Amy/amyhandjob03.png"
        pause 0.04
        "Amy/amyhandjob02.png"
        pause 0.04
        "Amy/amyhandjob01.png"
        pause 0.04
        repeat

    image amyhandfast:
        "Amy/amyhandjob00.png"
        pause 0.03
        "Amy/amyhandjob01.png"
        pause 0.03
        "Amy/amyhandjob02.png"
        pause 0.03
        "Amy/amyhandjob03.png"
        pause 0.03
        "Amy/amyhandjob04.png"
        pause 0.03
        "Amy/amyhandjob05.png"
        pause 0.03
        "Amy/amyhandjob06.png"
        pause 0.03
        "Amy/amyhandjob07.png"
        pause 0.03
        "Amy/amyhandjob08.png"
        pause 0.03
        "Amy/amyhandjob09.png"
        pause 0.03
        "Amy/amyhandjob10.png"
        pause 0.03
        "Amy/amyhandjob09.png"
        pause 0.03
        "Amy/amyhandjob08.png"
        pause 0.03
        "Amy/amyhandjob07.png"
        pause 0.03
        "Amy/amyhandjob06.png"
        pause 0.03
        "Amy/amyhandjob05.png"
        pause 0.03
        "Amy/amyhandjob04.png"
        pause 0.03
        "Amy/amyhandjob03.png"
        pause 0.03
        "Amy/amyhandjob02.png"
        pause 0.03
        "Amy/amyhandjob01.png"
        pause 0.03
        repeat        

    image amyanalslow:
        "Amy/amyanal00.png"
        pause 0.04
        "Amy/amyanal01.png"
        pause 0.04
        "Amy/amyanal02.png"
        pause 0.04
        "Amy/amyanal03.png"
        pause 0.04
        "Amy/amyanal04.png"
        pause 0.04
        "Amy/amyanal05.png"
        pause 0.04
        "Amy/amyanal06.png"
        pause 0.04
        "Amy/amyanal07.png"
        pause 0.04
        "Amy/amyanal08.png"
        pause 0.04
        "Amy/amyanal09.png"
        pause 0.04
        "Amy/amyanal08.png"
        pause 0.04
        "Amy/amyanal07.png"
        pause 0.04
        "Amy/amyanal06.png"
        pause 0.04
        "Amy/amyanal05.png"
        pause 0.04
        "Amy/amyanal04.png"
        pause 0.04
        "Amy/amyanal03.png"
        pause 0.04
        "Amy/amyanal02.png"
        pause 0.04
        "Amy/amyanal01.png"
        pause 0.04
        repeat

    image amyanalfast:
        "Amy/amyanal00.png"
        pause 0.03
        "Amy/amyanal01.png"
        pause 0.03
        "Amy/amyanal02.png"
        pause 0.03
        "Amy/amyanal03.png"
        pause 0.03
        "Amy/amyanal04.png"
        pause 0.03
        "Amy/amyanal05.png"
        pause 0.03
        "Amy/amyanal06.png"
        pause 0.03
        "Amy/amyanal07.png"
        pause 0.03
        "Amy/amyanal08.png"
        pause 0.03
        "Amy/amyanal09.png"
        pause 0.03
        "Amy/amyanal08.png"
        pause 0.03
        "Amy/amyanal07.png"
        pause 0.03
        "Amy/amyanal06.png"
        pause 0.03
        "Amy/amyanal05.png"
        pause 0.03
        "Amy/amyanal04.png"
        pause 0.03
        "Amy/amyanal03.png"
        pause 0.03
        "Amy/amyanal02.png"
        pause 0.03
        "Amy/amyanal01.png"
        pause 0.03
        repeat
    
    image aylamissionaryslow:
        "Ayla/aylaarnieanim00.png"
        pause 0.03
        "Ayla/aylaarnieanim01.png"
        pause 0.03
        "Ayla/aylaarnieanim02.png"
        pause 0.03
        "Ayla/aylaarnieanim03.png"
        pause 0.03
        "Ayla/aylaarnieanim04.png"
        pause 0.03
        "Ayla/aylaarnieanim05.png"
        pause 0.03
        "Ayla/aylaarnieanim06.png"
        pause 0.03
        "Ayla/aylaarnieanim07.png"
        pause 0.03
        "Ayla/aylaarnieanim08.png"
        pause 0.03
        "Ayla/aylaarnieanim09.png"
        pause 0.03
        "Ayla/aylaarnieanim10.png"
        pause 0.03
        "Ayla/aylaarnieanim11.png"
        pause 0.03
        "Ayla/aylaarnieanim12.png"
        pause 0.03
        "Ayla/aylaarnieanim13.png"
        pause 0.03
        "Ayla/aylaarnieanim14.png"
        pause 0.03
        "Ayla/aylaarnieanim15.png"
        pause 0.03
        "Ayla/aylaarnieanim16.png"
        pause 0.03
        "Ayla/aylaarnieanim17.png"
        pause 0.03
        "Ayla/aylaarnieanim18.png"
        pause 0.03
        "Ayla/aylaarnieanim19.png"
        pause 0.03
        repeat
    
    image aylamissionaryfast:
        "Ayla/aylaarnieanim00.png"
        pause 0.02
        "Ayla/aylaarnieanim01.png"
        pause 0.02
        "Ayla/aylaarnieanim02.png"
        pause 0.02
        "Ayla/aylaarnieanim03.png"
        pause 0.02
        "Ayla/aylaarnieanim04.png"
        pause 0.02
        "Ayla/aylaarnieanim05.png"
        pause 0.02
        "Ayla/aylaarnieanim06.png"
        pause 0.02
        "Ayla/aylaarnieanim07.png"
        pause 0.02
        "Ayla/aylaarnieanim08.png"
        pause 0.02
        "Ayla/aylaarnieanim09.png"
        pause 0.02
        "Ayla/aylaarnieanim10.png"
        pause 0.02
        "Ayla/aylaarnieanim11.png"
        pause 0.02
        "Ayla/aylaarnieanim12.png"
        pause 0.02
        "Ayla/aylaarnieanim13.png"
        pause 0.02
        "Ayla/aylaarnieanim14.png"
        pause 0.02
        "Ayla/aylaarnieanim15.png"
        pause 0.02
        "Ayla/aylaarnieanim16.png"
        pause 0.02
        "Ayla/aylaarnieanim17.png"
        pause 0.02
        "Ayla/aylaarnieanim18.png"
        pause 0.02
        "Ayla/aylaarnieanim19.png"
        pause 0.02
        repeat
    
    image aylaanalslow:
        "Ayla/aylaanal00.png"
        pause 0.05
        "Ayla/aylaanal01.png"
        pause 0.03
        "Ayla/aylaanal02.png"
        pause 0.03
        "Ayla/aylaanal03.png"
        pause 0.03
        "Ayla/aylaanal04.png"
        pause 0.03
        "Ayla/aylaanal05.png"
        pause 0.03
        "Ayla/aylaanal06.png"
        pause 0.03
        "Ayla/aylaanal07.png"
        pause 0.03
        "Ayla/aylaanal08.png"
        pause 0.03
        "Ayla/aylaanal09.png"
        pause 0.05
        "Ayla/aylaanal10.png"
        pause 0.04
        "Ayla/aylaanal11.png"
        pause 0.04
        "Ayla/aylaanal12.png"
        pause 0.04
        "Ayla/aylaanal13.png"
        pause 0.04
        "Ayla/aylaanal14.png"
        pause 0.04
        "Ayla/aylaanal15.png"
        pause 0.04
        "Ayla/aylaanal16.png"
        pause 0.04
        "Ayla/aylaanal17.png"
        pause 0.04
        repeat

    image aylaanalfast:
        "Ayla/aylaanal00.png"
        pause 0.04
        "Ayla/aylaanal01.png"
        pause 0.02
        "Ayla/aylaanal02.png"
        pause 0.02
        "Ayla/aylaanal03.png"
        pause 0.02
        "Ayla/aylaanal04.png"
        pause 0.02
        "Ayla/aylaanal05.png"
        pause 0.02
        "Ayla/aylaanal06.png"
        pause 0.02
        "Ayla/aylaanal07.png"
        pause 0.02
        "Ayla/aylaanal08.png"
        pause 0.02
        "Ayla/aylaanal09.png"
        pause 0.04
        "Ayla/aylaanal10.png"
        pause 0.03
        "Ayla/aylaanal11.png"
        pause 0.03
        "Ayla/aylaanal12.png"
        pause 0.03
        "Ayla/aylaanal13.png"
        pause 0.03
        "Ayla/aylaanal14.png"
        pause 0.03
        "Ayla/aylaanal15.png"
        pause 0.03
        "Ayla/aylaanal16.png"
        pause 0.03
        "Ayla/aylaanal17.png"
        pause 0.03
        repeat

    image aylarideslow:
        "Ayla/aylaride00.png"
        pause 0.06
        "Ayla/aylaride01.png"
        pause 0.06
        "Ayla/aylaride02.png"
        pause 0.06
        "Ayla/aylaride03.png"
        pause 0.06
        "Ayla/aylaride04.png"
        pause 0.06
        "Ayla/aylaride05.png"
        pause 0.06
        "Ayla/aylaride06.png"
        pause 0.06
        "Ayla/aylaride07.png"
        pause 0.06
        "Ayla/aylaride08.png"
        pause 0.06
        "Ayla/aylaride09.png"
        pause 0.08
        "Ayla/aylaride08.png"
        pause 0.06
        "Ayla/aylaride07.png"
        pause 0.06
        "Ayla/aylaride06.png"
        pause 0.06
        "Ayla/aylaride05.png"
        pause 0.06
        "Ayla/aylaride04.png"
        pause 0.06
        "Ayla/aylaride03.png"
        pause 0.06
        "Ayla/aylaride02.png"
        pause 0.06
        "Ayla/aylaride01.png"
        pause 0.06
        repeat

    image aylaridefast:
        "Ayla/aylaride00.png"
        pause 0.04
        "Ayla/aylaride01.png"
        pause 0.04
        "Ayla/aylaride02.png"
        pause 0.04
        "Ayla/aylaride03.png"
        pause 0.04
        "Ayla/aylaride04.png"
        pause 0.04
        "Ayla/aylaride05.png"
        pause 0.04
        "Ayla/aylaride06.png"
        pause 0.04
        "Ayla/aylaride07.png"
        pause 0.04
        "Ayla/aylaride08.png"
        pause 0.04
        "Ayla/aylaride09.png"
        pause 0.05
        "Ayla/aylaride08.png"
        pause 0.04
        "Ayla/aylaride07.png"
        pause 0.04
        "Ayla/aylaride06.png"
        pause 0.04
        "Ayla/aylaride05.png"
        pause 0.04
        "Ayla/aylaride04.png"
        pause 0.04
        "Ayla/aylaride03.png"
        pause 0.04
        "Ayla/aylaride02.png"
        pause 0.04
        "Ayla/aylaride01.png"
        pause 0.04
        repeat

    image aylahandslow:
        "Ayla/aylahandjob00.png"
        pause 0.04
        "Ayla/aylahandjob01.png"
        pause 0.04
        "Ayla/aylahandjob02.png"
        pause 0.04
        "Ayla/aylahandjob03.png"
        pause 0.04
        "Ayla/aylahandjob04.png"
        pause 0.04
        "Ayla/aylahandjob05.png"
        pause 0.04
        "Ayla/aylahandjob06.png"
        pause 0.04
        "Ayla/aylahandjob07.png"
        pause 0.04
        "Ayla/aylahandjob08.png"
        pause 0.04
        "Ayla/aylahandjob09.png"
        pause 0.04
        "Ayla/aylahandjob08.png"
        pause 0.04
        "Ayla/aylahandjob07.png"
        pause 0.04
        "Ayla/aylahandjob06.png"
        pause 0.04
        "Ayla/aylahandjob05.png"
        pause 0.04
        "Ayla/aylahandjob04.png"
        pause 0.04
        "Ayla/aylahandjob03.png"
        pause 0.04
        "Ayla/aylahandjob02.png"
        pause 0.04
        "Ayla/aylahandjob01.png"
        pause 0.04
        repeat

    image aylahandfast:
        "Ayla/aylahandjob00.png"
        pause 0.03
        "Ayla/aylahandjob01.png"
        pause 0.03
        "Ayla/aylahandjob02.png"
        pause 0.03
        "Ayla/aylahandjob03.png"
        pause 0.03
        "Ayla/aylahandjob04.png"
        pause 0.03
        "Ayla/aylahandjob05.png"
        pause 0.03
        "Ayla/aylahandjob06.png"
        pause 0.03
        "Ayla/aylahandjob07.png"
        pause 0.03
        "Ayla/aylahandjob08.png"
        pause 0.03
        "Ayla/aylahandjob09.png"
        pause 0.03
        "Ayla/aylahandjob08.png"
        pause 0.03
        "Ayla/aylahandjob07.png"
        pause 0.03
        "Ayla/aylahandjob06.png"
        pause 0.03
        "Ayla/aylahandjob05.png"
        pause 0.03
        "Ayla/aylahandjob04.png"
        pause 0.03
        "Ayla/aylahandjob03.png"
        pause 0.03
        "Ayla/aylahandjob02.png"
        pause 0.03
        "Ayla/aylahandjob01.png"
        pause 0.03
        repeat
        
    image aylahandpovslow:
        "Ayla/aylahandjobpov00.png"
        pause 0.04
        "Ayla/aylahandjobpov01.png"
        pause 0.04
        "Ayla/aylahandjobpov02.png"
        pause 0.04
        "Ayla/aylahandjobpov03.png"
        pause 0.04
        "Ayla/aylahandjobpov04.png"
        pause 0.04
        "Ayla/aylahandjobpov05.png"
        pause 0.04
        "Ayla/aylahandjobpov06.png"
        pause 0.04
        "Ayla/aylahandjobpov07.png"
        pause 0.04
        "Ayla/aylahandjobpov08.png"
        pause 0.04
        "Ayla/aylahandjobpov09.png"
        pause 0.04
        "Ayla/aylahandjobpov08.png"
        pause 0.04
        "Ayla/aylahandjobpov07.png"
        pause 0.04
        "Ayla/aylahandjobpov06.png"
        pause 0.04
        "Ayla/aylahandjobpov05.png"
        pause 0.04
        "Ayla/aylahandjobpov04.png"
        pause 0.04
        "Ayla/aylahandjobpov03.png"
        pause 0.04
        "Ayla/aylahandjobpov02.png"
        pause 0.04
        "Ayla/aylahandjobpov01.png"
        pause 0.04
        repeat

    image aylahandpovfast:
        "Ayla/aylahandjobpov00.png"
        pause 0.03
        "Ayla/aylahandjobpov01.png"
        pause 0.03
        "Ayla/aylahandjobpov02.png"
        pause 0.03
        "Ayla/aylahandjobpov03.png"
        pause 0.03
        "Ayla/aylahandjobpov04.png"
        pause 0.03
        "Ayla/aylahandjobpov05.png"
        pause 0.03
        "Ayla/aylahandjobpov06.png"
        pause 0.03
        "Ayla/aylahandjobpov07.png"
        pause 0.03
        "Ayla/aylahandjobpov08.png"
        pause 0.03
        "Ayla/aylahandjobpov09.png"
        pause 0.03
        "Ayla/aylahandjobpov08.png"
        pause 0.03
        "Ayla/aylahandjobpov07.png"
        pause 0.03
        "Ayla/aylahandjobpov06.png"
        pause 0.03
        "Ayla/aylahandjobpov05.png"
        pause 0.03
        "Ayla/aylahandjobpov04.png"
        pause 0.03
        "Ayla/aylahandjobpov03.png"
        pause 0.03
        "Ayla/aylahandjobpov02.png"
        pause 0.03
        "Ayla/aylahandjobpov01.png"
        pause 0.03
        repeat
            
    image aylalickslow:
        "Ayla/aylalick00.png"
        pause 0.04
        "Ayla/aylalick01.png"
        pause 0.04
        "Ayla/aylalick02.png"
        pause 0.04
        "Ayla/aylalick03.png"
        pause 0.04
        "Ayla/aylalick04.png"
        pause 0.04
        "Ayla/aylalick05.png"
        pause 0.04
        "Ayla/aylalick06.png"
        pause 0.04
        "Ayla/aylalick07.png"
        pause 0.04
        "Ayla/aylalick08.png"
        pause 0.04
        "Ayla/aylalick09.png"
        pause 0.04
        "Ayla/aylalick08.png"
        pause 0.04
        "Ayla/aylalick07.png"
        pause 0.04
        "Ayla/aylalick06.png"
        pause 0.04
        "Ayla/aylalick05.png"
        pause 0.04
        "Ayla/aylalick04.png"
        pause 0.04
        "Ayla/aylalick03.png"
        pause 0.04
        "Ayla/aylalick02.png"
        pause 0.04
        "Ayla/aylalick01.png"
        pause 0.04
        repeat

    image aylatitsslow:
        "Ayla/aylatits00.png"
        pause 0.06
        "Ayla/aylatits01.png"
        pause 0.06
        "Ayla/aylatits02.png"
        pause 0.06
        "Ayla/aylatits03.png"
        pause 0.06
        "Ayla/aylatits04.png"
        pause 0.06
        "Ayla/aylatits05.png"
        pause 0.06
        "Ayla/aylatits06.png"
        pause 0.06
        "Ayla/aylatits07.png"
        pause 0.06
        "Ayla/aylatits08.png"
        pause 0.06
        "Ayla/aylatits09.png"
        pause 0.1
        "Ayla/aylatits08.png"
        pause 0.04
        "Ayla/aylatits07.png"
        pause 0.04
        "Ayla/aylatits06.png"
        pause 0.04
        "Ayla/aylatits05.png"
        pause 0.04
        "Ayla/aylatits04.png"
        pause 0.04
        "Ayla/aylatits03.png"
        pause 0.04
        "Ayla/aylatits02.png"
        pause 0.04
        "Ayla/aylatits01.png"
        pause 0.04
        repeat

    image aylatitsslowb:
        "Ayla/aylatitsb00.png"
        pause 0.06
        "Ayla/aylatitsb01.png"
        pause 0.06
        "Ayla/aylatitsb02.png"
        pause 0.06
        "Ayla/aylatitsb03.png"
        pause 0.06
        "Ayla/aylatitsb04.png"
        pause 0.06
        "Ayla/aylatitsb05.png"
        pause 0.06
        "Ayla/aylatitsb06.png"
        pause 0.06
        "Ayla/aylatitsb07.png"
        pause 0.06
        "Ayla/aylatitsb08.png"
        pause 0.06
        "Ayla/aylatitsb09.png"
        pause 0.1
        "Ayla/aylatitsb08.png"
        pause 0.04
        "Ayla/aylatitsb07.png"
        pause 0.04
        "Ayla/aylatitsb06.png"
        pause 0.04
        "Ayla/aylatitsb05.png"
        pause 0.04
        "Ayla/aylatitsb04.png"
        pause 0.04
        "Ayla/aylatitsb03.png"
        pause 0.04
        "Ayla/aylatitsb02.png"
        pause 0.04
        "Ayla/aylatitsb01.png"
        pause 0.04
        repeat

    image aylatitsfast:
        "Ayla/aylatits00.png"
        pause 0.05
        "Ayla/aylatits01.png"
        pause 0.05
        "Ayla/aylatits02.png"
        pause 0.05
        "Ayla/aylatits03.png"
        pause 0.05
        "Ayla/aylatits04.png"
        pause 0.05
        "Ayla/aylatits05.png"
        pause 0.05
        "Ayla/aylatits06.png"
        pause 0.05
        "Ayla/aylatits07.png"
        pause 0.05
        "Ayla/aylatits08.png"
        pause 0.05
        "Ayla/aylatits09.png"
        pause 0.08
        "Ayla/aylatits08.png"
        pause 0.03
        "Ayla/aylatits07.png"
        pause 0.03
        "Ayla/aylatits06.png"
        pause 0.03
        "Ayla/aylatits05.png"
        pause 0.03
        "Ayla/aylatits04.png"
        pause 0.03
        "Ayla/aylatits03.png"
        pause 0.03
        "Ayla/aylatits02.png"
        pause 0.03
        "Ayla/aylatits01.png"
        pause 0.03
        repeat

    image aylatitsfastb:
        "Ayla/aylatitsb00.png"
        pause 0.05
        "Ayla/aylatitsb01.png"
        pause 0.05
        "Ayla/aylatitsb02.png"
        pause 0.05
        "Ayla/aylatitsb03.png"
        pause 0.05
        "Ayla/aylatitsb04.png"
        pause 0.05
        "Ayla/aylatitsb05.png"
        pause 0.05
        "Ayla/aylatitsb06.png"
        pause 0.05
        "Ayla/aylatitsb07.png"
        pause 0.05
        "Ayla/aylatitsb08.png"
        pause 0.05
        "Ayla/aylatitsb09.png"
        pause 0.08
        "Ayla/aylatitsb08.png"
        pause 0.03
        "Ayla/aylatitsb07.png"
        pause 0.03
        "Ayla/aylatitsb06.png"
        pause 0.03
        "Ayla/aylatitsb05.png"
        pause 0.03
        "Ayla/aylatitsb04.png"
        pause 0.03
        "Ayla/aylatitsb03.png"
        pause 0.03
        "Ayla/aylatitsb02.png"
        pause 0.03
        "Ayla/aylatitsb01.png"
        pause 0.03
        repeat

    image aylalickfast:
        "Ayla/aylalick00.png"
        pause 0.04
        "Ayla/aylalick01.png"
        pause 0.04
        "Ayla/aylalick02.png"
        pause 0.04
        "Ayla/aylalick03.png"
        pause 0.04
        "Ayla/aylalick04.png"
        pause 0.04
        "Ayla/aylalick05.png"
        pause 0.04
        "Ayla/aylalick06.png"
        pause 0.04
        "Ayla/aylalick07.png"
        pause 0.04
        "Ayla/aylalick08.png"
        pause 0.04
        "Ayla/aylalick09.png"
        pause 0.04
        "Ayla/aylalick08.png"
        pause 0.04
        "Ayla/aylalick07.png"
        pause 0.04
        "Ayla/aylalick06.png"
        pause 0.04
        "Ayla/aylalick05.png"
        pause 0.04
        "Ayla/aylalick04.png"
        pause 0.04
        "Ayla/aylalick03.png"
        pause 0.04
        "Ayla/aylalick02.png"
        pause 0.04
        "Ayla/aylalick01.png"
        pause 0.04
        repeat

    image aylafootslow:
        "Ayla/aylafoot00.png"
        pause 0.04
        "Ayla/aylafoot01.png"
        pause 0.04
        "Ayla/aylafoot02.png"
        pause 0.04
        "Ayla/aylafoot03.png"
        pause 0.04
        "Ayla/aylafoot04.png"
        pause 0.04
        "Ayla/aylafoot05.png"
        pause 0.04
        "Ayla/aylafoot06.png"
        pause 0.04
        "Ayla/aylafoot07.png"
        pause 0.04
        "Ayla/aylafoot08.png"
        pause 0.04
        "Ayla/aylafoot09.png"
        pause 0.04
        "Ayla/aylafoot08.png"
        pause 0.04
        "Ayla/aylafoot07.png"
        pause 0.04
        "Ayla/aylafoot06.png"
        pause 0.04
        "Ayla/aylafoot05.png"
        pause 0.04
        "Ayla/aylafoot04.png"
        pause 0.04
        "Ayla/aylafoot03.png"
        pause 0.04
        "Ayla/aylafoot02.png"
        pause 0.04
        "Ayla/aylafoot01.png"
        pause 0.04
        repeat

    image aylafootfast:
        "Ayla/aylafoot00.png"
        pause 0.03
        "Ayla/aylafoot01.png"
        pause 0.03
        "Ayla/aylafoot02.png"
        pause 0.03
        "Ayla/aylafoot03.png"
        pause 0.03
        "Ayla/aylafoot04.png"
        pause 0.03
        "Ayla/aylafoot05.png"
        pause 0.03
        "Ayla/aylafoot06.png"
        pause 0.03
        "Ayla/aylafoot07.png"
        pause 0.03
        "Ayla/aylafoot08.png"
        pause 0.03
        "Ayla/aylafoot09.png"
        pause 0.03
        "Ayla/aylafoot08.png"
        pause 0.03
        "Ayla/aylafoot07.png"
        pause 0.03
        "Ayla/aylafoot06.png"
        pause 0.03
        "Ayla/aylafoot05.png"
        pause 0.03
        "Ayla/aylafoot04.png"
        pause 0.03
        "Ayla/aylafoot03.png"
        pause 0.03
        "Ayla/aylafoot02.png"
        pause 0.03
        "Ayla/aylafoot01.png"
        pause 0.03
        repeat

    image aylacryptslow:
        "church/ayladreadanim00.png"
        pause 0.04
        "church/ayladreadanim01.png"
        pause 0.04
        "church/ayladreadanim02.png"
        pause 0.04
        "church/ayladreadanim03.png"
        pause 0.04
        "church/ayladreadanim04.png"
        pause 0.04
        "church/ayladreadanim05.png"
        pause 0.04
        "church/ayladreadanim06.png"
        pause 0.04
        "church/ayladreadanim07.png"
        pause 0.04
        "church/ayladreadanim08.png"
        pause 0.04
        "church/ayladreadanim07.png"
        pause 0.04
        "church/ayladreadanim06.png"
        pause 0.04
        "church/ayladreadanim05.png"
        pause 0.04
        "church/ayladreadanim04.png"
        pause 0.04
        "church/ayladreadanim03.png"
        pause 0.04
        "church/ayladreadanim02.png"
        pause 0.04
        "church/ayladreadanim01.png"
        pause 0.04
        repeat

    image aylacryptfast:
        "church/ayladreadanim00.png"
        pause 0.03
        "church/ayladreadanim01.png"
        pause 0.03
        "church/ayladreadanim02.png"
        pause 0.03
        "church/ayladreadanim03.png"
        pause 0.03
        "church/ayladreadanim04.png"
        pause 0.03
        "church/ayladreadanim05.png"
        pause 0.03
        "church/ayladreadanim06.png"
        pause 0.03
        "church/ayladreadanim07.png"
        pause 0.03
        "church/ayladreadanim08.png"
        pause 0.03
        "church/ayladreadanim07.png"
        pause 0.03
        "church/ayladreadanim06.png"
        pause 0.03
        "church/ayladreadanim05.png"
        pause 0.03
        "church/ayladreadanim04.png"
        pause 0.03
        "church/ayladreadanim03.png"
        pause 0.03
        "church/ayladreadanim02.png"
        pause 0.03
        "church/ayladreadanim01.png"
        pause 0.03
        repeat

    image sofiaslow:
        "Explore/sofiafuck00.jpg"
        pause 0.04
        "Explore/sofiafuck01.jpg"
        pause 0.04
        "Explore/sofiafuck02.jpg"
        pause 0.04
        "Explore/sofiafuck03.jpg"
        pause 0.04
        "Explore/sofiafuck04.jpg"
        pause 0.04
        "Explore/sofiafuck05.jpg"
        pause 0.04
        "Explore/sofiafuck06.jpg"
        pause 0.04
        "Explore/sofiafuck07.jpg"
        pause 0.04
        "Explore/sofiafuck08.jpg"
        pause 0.04
        "Explore/sofiafuck09.jpg"
        pause 0.04
        "Explore/sofiafuck10.jpg"
        pause 0.04
        "Explore/sofiafuck11.jpg"
        pause 0.04
        "Explore/sofiafuck12.jpg"
        pause 0.04
        "Explore/sofiafuck13.jpg"
        pause 0.04
        "Explore/sofiafuck14.jpg"
        pause 0.04
        "Explore/sofiafuck15.jpg"
        pause 0.04
        "Explore/sofiafuck16.jpg"
        pause 0.04
        "Explore/sofiafuck17.jpg"
        pause 0.04
        "Explore/sofiafuck18.jpg"
        pause 0.04
        repeat

    image sofiafast:
        "Explore/sofiafuck00.jpg"
        pause 0.03
        "Explore/sofiafuck01.jpg"
        pause 0.03
        "Explore/sofiafuck02.jpg"
        pause 0.03
        "Explore/sofiafuck03.jpg"
        pause 0.03
        "Explore/sofiafuck04.jpg"
        pause 0.03
        "Explore/sofiafuck05.jpg"
        pause 0.03
        "Explore/sofiafuck06.jpg"
        pause 0.03
        "Explore/sofiafuck07.jpg"
        pause 0.03
        "Explore/sofiafuck08.jpg"
        pause 0.03
        "Explore/sofiafuck09.jpg"
        pause 0.03
        "Explore/sofiafuck10.jpg"
        pause 0.03
        "Explore/sofiafuck11.jpg"
        pause 0.03
        "Explore/sofiafuck12.jpg"
        pause 0.03
        "Explore/sofiafuck13.jpg"
        pause 0.03
        "Explore/sofiafuck14.jpg"
        pause 0.03
        "Explore/sofiafuck15.jpg"
        pause 0.03
        "Explore/sofiafuck16.jpg"
        pause 0.03
        "Explore/sofiafuck17.jpg"
        pause 0.03
        "Explore/sofiafuck18.jpg"
        pause 0.03
        repeat

    image hulkmagnusslow:
        "Explore02/hulkmagnussex00.png"
        pause 0.04
        "Explore02/hulkmagnussex01.png"
        pause 0.04
        "Explore02/hulkmagnussex02.png"
        pause 0.04
        "Explore02/hulkmagnussex03.png"
        pause 0.04
        "Explore02/hulkmagnussex04.png"
        pause 0.04
        "Explore02/hulkmagnussex05.png"
        pause 0.04
        "Explore02/hulkmagnussex06.png"
        pause 0.04
        "Explore02/hulkmagnussex07.png"
        pause 0.04
        "Explore02/hulkmagnussex08.png"
        pause 0.04
        "Explore02/hulkmagnussex09.png"
        pause 0.06
        "Explore02/hulkmagnussex08.png"
        pause 0.05
        "Explore02/hulkmagnussex07.png"
        pause 0.05
        "Explore02/hulkmagnussex06.png"
        pause 0.05
        "Explore02/hulkmagnussex05.png"
        pause 0.05
        "Explore02/hulkmagnussex04.png"
        pause 0.05
        "Explore02/hulkmagnussex03.png"
        pause 0.05
        "Explore02/hulkmagnussex02.png"
        pause 0.05
        "Explore02/hulkmagnussex01.png"
        pause 0.05
        repeat

    image hulkmagnusfast:
        "Explore02/hulkmagnussex00.png"
        pause 0.02
        "Explore02/hulkmagnussex01.png"
        pause 0.03
        "Explore02/hulkmagnussex02.png"
        pause 0.03
        "Explore02/hulkmagnussex03.png"
        pause 0.03
        "Explore02/hulkmagnussex04.png"
        pause 0.03
        "Explore02/hulkmagnussex05.png"
        pause 0.03
        "Explore02/hulkmagnussex06.png"
        pause 0.03
        "Explore02/hulkmagnussex07.png"
        pause 0.03
        "Explore02/hulkmagnussex08.png"
        pause 0.03
        "Explore02/hulkmagnussex09.png"
        pause 0.05
        "Explore02/hulkmagnussex08.png"
        pause 0.04
        "Explore02/hulkmagnussex07.png"
        pause 0.04
        "Explore02/hulkmagnussex06.png"
        pause 0.04
        "Explore02/hulkmagnussex05.png"
        pause 0.04
        "Explore02/hulkmagnussex04.png"
        pause 0.04
        "Explore02/hulkmagnussex03.png"
        pause 0.04
        "Explore02/hulkmagnussex02.png"
        pause 0.04
        "Explore02/hulkmagnussex01.png"
        pause 0.04
        repeat

    image POVhulkmagnusslow:
        "Explore02/hulksexPOV00.png"
        pause 0.04
        "Explore02/hulksexPOV01.png"
        pause 0.04
        "Explore02/hulksexPOV02.png"
        pause 0.04
        "Explore02/hulksexPOV03.png"
        pause 0.04
        "Explore02/hulksexPOV04.png"
        pause 0.04
        "Explore02/hulksexPOV05.png"
        pause 0.04
        "Explore02/hulksexPOV06.png"
        pause 0.04
        "Explore02/hulksexPOV07.png"
        pause 0.04
        "Explore02/hulksexPOV08.png"
        pause 0.04
        "Explore02/hulksexPOV09.png"
        pause 0.06
        "Explore02/hulksexPOV08.png"
        pause 0.05
        "Explore02/hulksexPOV07.png"
        pause 0.05
        "Explore02/hulksexPOV06.png"
        pause 0.05
        "Explore02/hulksexPOV05.png"
        pause 0.05
        "Explore02/hulksexPOV04.png"
        pause 0.05
        "Explore02/hulksexPOV03.png"
        pause 0.05
        "Explore02/hulksexPOV02.png"
        pause 0.05
        "Explore02/hulksexPOV01.png"
        pause 0.05
        repeat

    image POVhulkmagnusfast:
        "Explore02/hulksexPOV00.png"
        pause 0.03
        "Explore02/hulksexPOV01.png"
        pause 0.03
        "Explore02/hulksexPOV02.png"
        pause 0.03
        "Explore02/hulksexPOV03.png"
        pause 0.03
        "Explore02/hulksexPOV04.png"
        pause 0.03
        "Explore02/hulksexPOV05.png"
        pause 0.03
        "Explore02/hulksexPOV06.png"
        pause 0.03
        "Explore02/hulksexPOV07.png"
        pause 0.03
        "Explore02/hulksexPOV08.png"
        pause 0.03
        "Explore02/hulksexPOV09.png"
        pause 0.05
        "Explore02/hulksexPOV08.png"
        pause 0.04
        "Explore02/hulksexPOV07.png"
        pause 0.04
        "Explore02/hulksexPOV06.png"
        pause 0.04
        "Explore02/hulksexPOV05.png"
        pause 0.04
        "Explore02/hulksexPOV04.png"
        pause 0.04
        "Explore02/hulksexPOV03.png"
        pause 0.04
        "Explore02/hulksexPOV02.png"
        pause 0.04
        "Explore02/hulksexPOV01.png"
        pause 0.04
        repeat
            
    image hulkupfast:
        "Explore02/hulkup00.png"
        pause 0.05
        "Explore02/hulkup01.png"
        pause 0.03
        "Explore02/hulkup02.png"
        pause 0.03
        "Explore02/hulkup03.png"
        pause 0.03
        "Explore02/hulkup04.png"
        pause 0.03
        "Explore02/hulkup05.png"
        pause 0.03
        "Explore02/hulkup06.png"
        pause 0.03
        "Explore02/hulkup07.png"
        pause 0.03
        "Explore02/hulkup08.png"
        pause 0.03
        "Explore02/hulkup09.png"
        pause 0.05
        "Explore02/hulkup08.png"
        pause 0.02
        "Explore02/hulkup07.png"
        pause 0.02
        "Explore02/hulkup06.png"
        pause 0.02
        "Explore02/hulkup05.png"
        pause 0.02
        "Explore02/hulkup04.png"
        pause 0.02
        "Explore02/hulkup03.png"
        pause 0.02
        "Explore02/hulkup02.png"
        pause 0.02
        "Explore02/hulkup01.png"
        pause 0.02
        repeat

    image hulkupslow:
        "Explore02/hulkup00.png"
        pause 0.06
        "Explore02/hulkup01.png"
        pause 0.04
        "Explore02/hulkup02.png"
        pause 0.04
        "Explore02/hulkup03.png"
        pause 0.04
        "Explore02/hulkup04.png"
        pause 0.04
        "Explore02/hulkup05.png"
        pause 0.04
        "Explore02/hulkup06.png"
        pause 0.04
        "Explore02/hulkup07.png"
        pause 0.04
        "Explore02/hulkup08.png"
        pause 0.04
        "Explore02/hulkup09.png"
        pause 0.06
        "Explore02/hulkup08.png"
        pause 0.03
        "Explore02/hulkup07.png"
        pause 0.03
        "Explore02/hulkup06.png"
        pause 0.03
        "Explore02/hulkup05.png"
        pause 0.03
        "Explore02/hulkup04.png"
        pause 0.03
        "Explore02/hulkup03.png"
        pause 0.03
        "Explore02/hulkup02.png"
        pause 0.03
        "Explore02/hulkup01.png"
        pause 0.03
        repeat

    image bikeblowslow:
        "Explore02/bikeblow00.png"
        pause 0.04
        "Explore02/bikeblow01.png"
        pause 0.04
        "Explore02/bikeblow02.png"
        pause 0.04
        "Explore02/bikeblow03.png"
        pause 0.04
        "Explore02/bikeblow04.png"
        pause 0.04
        "Explore02/bikeblow05.png"
        pause 0.04
        "Explore02/bikeblow06.png"
        pause 0.04
        "Explore02/bikeblow07.png"
        pause 0.04
        "Explore02/bikeblow08.png"
        pause 0.04
        "Explore02/bikeblow09.png"
        pause 0.06
        "Explore02/bikeblow08.png"
        pause 0.03
        "Explore02/bikeblow07.png"
        pause 0.03
        "Explore02/bikeblow06.png"
        pause 0.03
        "Explore02/bikeblow05.png"
        pause 0.03
        "Explore02/bikeblow04.png"
        pause 0.03
        "Explore02/bikeblow03.png"
        pause 0.03
        "Explore02/bikeblow02.png"
        pause 0.03
        "Explore02/bikeblow01.png"
        pause 0.03
        repeat

    image bikeblowfast:
        "Explore02/bikeblow00.png"
        pause 0.03
        "Explore02/bikeblow01.png"
        pause 0.03
        "Explore02/bikeblow02.png"
        pause 0.03
        "Explore02/bikeblow03.png"
        pause 0.03
        "Explore02/bikeblow04.png"
        pause 0.03
        "Explore02/bikeblow05.png"
        pause 0.03
        "Explore02/bikeblow06.png"
        pause 0.03
        "Explore02/bikeblow07.png"
        pause 0.03
        "Explore02/bikeblow08.png"
        pause 0.03
        "Explore02/bikeblow09.png"
        pause 0.04
        "Explore02/bikeblow08.png"
        pause 0.02
        "Explore02/bikeblow07.png"
        pause 0.02
        "Explore02/bikeblow06.png"
        pause 0.02
        "Explore02/bikeblow05.png"
        pause 0.02
        "Explore02/bikeblow04.png"
        pause 0.02
        "Explore02/bikeblow03.png"
        pause 0.02
        "Explore02/bikeblow02.png"
        pause 0.02
        "Explore02/bikeblow01.png"
        pause 0.02
        repeat

    image bikeblowslow02:
        "Explore02/taylorblow00.png"
        pause 0.04
        "Explore02/taylorblow01.png"
        pause 0.04
        "Explore02/taylorblow02.png"
        pause 0.04
        "Explore02/taylorblow03.png"
        pause 0.04
        "Explore02/taylorblow04.png"
        pause 0.04
        "Explore02/taylorblow05.png"
        pause 0.04
        "Explore02/taylorblow06.png"
        pause 0.04
        "Explore02/taylorblow07.png"
        pause 0.05
        "Explore02/taylorblow08.png"
        pause 0.06
        "Explore02/taylorblow09.png"
        pause 0.2
        "Explore02/taylorblow08.png"
        pause 0.03
        "Explore02/taylorblow07.png"
        pause 0.03
        "Explore02/taylorblow06.png"
        pause 0.03
        "Explore02/taylorblow05.png"
        pause 0.03
        "Explore02/taylorblow04.png"
        pause 0.03
        "Explore02/taylorblow03.png"
        pause 0.03
        "Explore02/taylorblow02.png"
        pause 0.03
        "Explore02/taylorblow01.png"
        pause 0.03
        repeat

    image bikeblowfast02:
        "Explore02/taylorblow00.png"
        pause 0.03
        "Explore02/taylorblow01.png"
        pause 0.03
        "Explore02/taylorblow02.png"
        pause 0.03
        "Explore02/taylorblow03.png"
        pause 0.03
        "Explore02/taylorblow04.png"
        pause 0.03
        "Explore02/taylorblow05.png"
        pause 0.03
        "Explore02/taylorblow06.png"
        pause 0.03
        "Explore02/taylorblow07.png"
        pause 0.04
        "Explore02/taylorblow08.png"
        pause 0.05
        "Explore02/taylorblow09.png"
        pause 0.15
        "Explore02/taylorblow08.png"
        pause 0.02
        "Explore02/taylorblow07.png"
        pause 0.02
        "Explore02/taylorblow06.png"
        pause 0.02
        "Explore02/taylorblow05.png"
        pause 0.02
        "Explore02/taylorblow04.png"
        pause 0.02
        "Explore02/taylorblow03.png"
        pause 0.02
        "Explore02/taylorblow02.png"
        pause 0.02
        "Explore02/taylorblow01.png"
        pause 0.02
        repeat

    image cindyfuckslow:
        "Explore02/cindyfuck09.png"
        pause 0.1
        "Explore02/cindyfuck08.png"
        pause 0.03
        "Explore02/cindyfuck07.png"
        pause 0.03
        "Explore02/cindyfuck06.png"
        pause 0.03
        "Explore02/cindyfuck05.png"
        pause 0.03
        "Explore02/cindyfuck04.png"
        pause 0.03
        "Explore02/cindyfuck03.png"
        pause 0.03
        "Explore02/cindyfuck02.png"
        pause 0.03
        "Explore02/cindyfuck01.png"
        pause 0.03
        "Explore02/cindyfuck00.png"
        pause 0.06
        "Explore02/cindyfuck01.png"
        pause 0.04
        "Explore02/cindyfuck02.png"
        pause 0.04
        "Explore02/cindyfuck03.png"
        pause 0.04
        "Explore02/cindyfuck04.png"
        pause 0.04
        "Explore02/cindyfuck05.png"
        pause 0.04
        "Explore02/cindyfuck06.png"
        pause 0.04
        "Explore02/cindyfuck07.png"
        pause 0.04
        "Explore02/cindyfuck08.png"
        pause 0.04
        repeat

    image cindyfuckfast:
        "Explore02/cindyfuck09.png"
        pause 0.08
        "Explore02/cindyfuck08.png"
        pause 0.02
        "Explore02/cindyfuck07.png"
        pause 0.02
        "Explore02/cindyfuck06.png"
        pause 0.02
        "Explore02/cindyfuck05.png"
        pause 0.02
        "Explore02/cindyfuck04.png"
        pause 0.02
        "Explore02/cindyfuck03.png"
        pause 0.02
        "Explore02/cindyfuck02.png"
        pause 0.02
        "Explore02/cindyfuck01.png"
        pause 0.02
        "Explore02/cindyfuck00.png"
        pause 0.05
        "Explore02/cindyfuck01.png"
        pause 0.03
        "Explore02/cindyfuck02.png"
        pause 0.03
        "Explore02/cindyfuck03.png"
        pause 0.03
        "Explore02/cindyfuck04.png"
        pause 0.03
        "Explore02/cindyfuck05.png"
        pause 0.03
        "Explore02/cindyfuck06.png"
        pause 0.03
        "Explore02/cindyfuck07.png"
        pause 0.03
        "Explore02/cindyfuck08.png"
        pause 0.03
        repeat

    image melaniahandslow:
        "Explore02/melaniahand00.png"
        pause 0.04
        "Explore02/melaniahand01.png"
        pause 0.04
        "Explore02/melaniahand02.png"
        pause 0.04
        "Explore02/melaniahand03.png"
        pause 0.04
        "Explore02/melaniahand04.png"
        pause 0.04
        "Explore02/melaniahand05.png"
        pause 0.04
        "Explore02/melaniahand06.png"
        pause 0.04
        "Explore02/melaniahand07.png"
        pause 0.05
        "Explore02/melaniahand08.png"
        pause 0.06
        "Explore02/melaniahand09.png"
        pause 0.2
        "Explore02/melaniahand08.png"
        pause 0.03
        "Explore02/melaniahand07.png"
        pause 0.03
        "Explore02/melaniahand06.png"
        pause 0.03
        "Explore02/melaniahand05.png"
        pause 0.03
        "Explore02/melaniahand04.png"
        pause 0.03
        "Explore02/melaniahand03.png"
        pause 0.03
        "Explore02/melaniahand02.png"
        pause 0.03
        "Explore02/melaniahand01.png"
        pause 0.03
        repeat

    image melaniahandfast:
        "Explore02/melaniahand00.png"
        pause 0.03
        "Explore02/melaniahand01.png"
        pause 0.03
        "Explore02/melaniahand02.png"
        pause 0.03
        "Explore02/melaniahand03.png"
        pause 0.03
        "Explore02/melaniahand04.png"
        pause 0.03
        "Explore02/melaniahand05.png"
        pause 0.03
        "Explore02/melaniahand06.png"
        pause 0.03
        "Explore02/melaniahand07.png"
        pause 0.04
        "Explore02/melaniahand08.png"
        pause 0.05
        "Explore02/melaniahand09.png"
        pause 0.15
        "Explore02/melaniahand08.png"
        pause 0.02
        "Explore02/melaniahand07.png"
        pause 0.02
        "Explore02/melaniahand06.png"
        pause 0.02
        "Explore02/melaniahand05.png"
        pause 0.02
        "Explore02/melaniahand04.png"
        pause 0.02
        "Explore02/melaniahand03.png"
        pause 0.02
        "Explore02/melaniahand02.png"
        pause 0.02
        "Explore02/melaniahand01.png"
        pause 0.02
        repeat

    image melaniabounceslow:
        "Explore02/melaniabounce00.png"
        pause 0.04
        "Explore02/melaniabounce01.png"
        pause 0.04
        "Explore02/melaniabounce02.png"
        pause 0.04
        "Explore02/melaniabounce03.png"
        pause 0.04
        "Explore02/melaniabounce04.png"
        pause 0.04
        "Explore02/melaniabounce05.png"
        pause 0.04
        "Explore02/melaniabounce06.png"
        pause 0.04
        "Explore02/melaniabounce07.png"
        pause 0.04
        "Explore02/melaniabounce08.png"
        pause 0.04
        "Explore02/melaniabounce09.png"
        pause 0.04
        "Explore02/melaniabounce10.png"
        pause 0.04
        "Explore02/melaniabounce11.png"
        pause 0.04
        "Explore02/melaniabounce12.png"
        pause 0.04
        "Explore02/melaniabounce13.png"
        pause 0.04
        "Explore02/melaniabounce14.png"
        pause 0.04
        "Explore02/melaniabounce15.png"
        pause 0.04
        "Explore02/melaniabounce16.png"
        pause 0.04
        "Explore02/melaniabounce17.png"
        pause 0.04
        "Explore02/melaniabounce18.png"
        pause 0.04
        repeat

    image melaniabouncefast:
        "Explore02/melaniabounce00.png"
        pause 0.03
        "Explore02/melaniabounce01.png"
        pause 0.03
        "Explore02/melaniabounce02.png"
        pause 0.03
        "Explore02/melaniabounce03.png"
        pause 0.03
        "Explore02/melaniabounce04.png"
        pause 0.03
        "Explore02/melaniabounce05.png"
        pause 0.03
        "Explore02/melaniabounce06.png"
        pause 0.03
        "Explore02/melaniabounce07.png"
        pause 0.03
        "Explore02/melaniabounce08.png"
        pause 0.03
        "Explore02/melaniabounce09.png"
        pause 0.03
        "Explore02/melaniabounce10.png"
        pause 0.03
        "Explore02/melaniabounce11.png"
        pause 0.03
        "Explore02/melaniabounce12.png"
        pause 0.03
        "Explore02/melaniabounce13.png"
        pause 0.03
        "Explore02/melaniabounce14.png"
        pause 0.03
        "Explore02/melaniabounce15.png"
        pause 0.03
        "Explore02/melaniabounce16.png"
        pause 0.03
        "Explore02/melaniabounce17.png"
        pause 0.03
        "Explore02/melaniabounce18.png"
        pause 0.03
        repeat
            
    image hippyfuck02slow:
        "Explore02/hippie02sex00.png"
        pause 0.05
        "Explore02/hippie02sex01.png"
        pause 0.05
        "Explore02/hippie02sex02.png"
        pause 0.05
        "Explore02/hippie02sex03.png"
        pause 0.05
        "Explore02/hippie02sex04.png"
        pause 0.05
        "Explore02/hippie02sex05.png"
        pause 0.05
        "Explore02/hippie02sex06.png"
        pause 0.05
        "Explore02/hippie02sex07.png"
        pause 0.05
        "Explore02/hippie02sex08.png"
        pause 0.10
        "Explore02/hippie02sex09.png"
        pause 0.10
        "Explore02/hippie02sex08.png"
        pause 0.04
        "Explore02/hippie02sex07.png"
        pause 0.04
        "Explore02/hippie02sex06.png"
        pause 0.04
        "Explore02/hippie02sex05.png"
        pause 0.04
        "Explore02/hippie02sex04.png"
        pause 0.04
        "Explore02/hippie02sex03.png"
        pause 0.04
        "Explore02/hippie02sex02.png"
        pause 0.04
        "Explore02/hippie02sex01.png"
        pause 0.04
        repeat

    image bountythreesomeslow:
        "Explore02/bountythreesome00.png"
        pause 0.04
        "Explore02/bountythreesome01.png"
        pause 0.04
        "Explore02/bountythreesome02.png"
        pause 0.04
        "Explore02/bountythreesome03.png"
        pause 0.04
        "Explore02/bountythreesome04.png"
        pause 0.04
        "Explore02/bountythreesome05.png"
        pause 0.04
        "Explore02/bountythreesome06.png"
        pause 0.04
        "Explore02/bountythreesome07.png"
        pause 0.04
        "Explore02/bountythreesome08.png"
        pause 0.04
        "Explore02/bountythreesome09.png"
        pause 0.04
        "Explore02/bountythreesome10.png"
        pause 0.04
        "Explore02/bountythreesome11.png"
        pause 0.04
        "Explore02/bountythreesome12.png"
        pause 0.04
        "Explore02/bountythreesome13.png"
        pause 0.04
        "Explore02/bountythreesome14.png"
        pause 0.04
        "Explore02/bountythreesome15.png"
        pause 0.04
        "Explore02/bountythreesome16.png"
        pause 0.04
        "Explore02/bountythreesome17.png"
        pause 0.04
        "Explore02/bountythreesome18.png"
        pause 0.04
        repeat

    image bountythreesomefast:
        "Explore02/bountythreesome00.png"
        pause 0.03
        "Explore02/bountythreesome01.png"
        pause 0.03
        "Explore02/bountythreesome02.png"
        pause 0.03
        "Explore02/bountythreesome03.png"
        pause 0.03
        "Explore02/bountythreesome04.png"
        pause 0.03
        "Explore02/bountythreesome05.png"
        pause 0.03
        "Explore02/bountythreesome06.png"
        pause 0.03
        "Explore02/bountythreesome07.png"
        pause 0.03
        "Explore02/bountythreesome08.png"
        pause 0.03
        "Explore02/bountythreesome09.png"
        pause 0.03
        "Explore02/bountythreesome10.png"
        pause 0.03
        "Explore02/bountythreesome11.png"
        pause 0.03
        "Explore02/bountythreesome12.png"
        pause 0.03
        "Explore02/bountythreesome13.png"
        pause 0.03
        "Explore02/bountythreesome14.png"
        pause 0.03
        "Explore02/bountythreesome15.png"
        pause 0.03
        "Explore02/bountythreesome16.png"
        pause 0.03
        "Explore02/bountythreesome17.png"
        pause 0.03
        "Explore02/bountythreesome18.png"
        pause 0.03
        repeat
            
    image hippyfuck02slow:
        "Explore02/hippie02sex00.png"
        pause 0.05
        "Explore02/hippie02sex01.png"
        pause 0.05
        "Explore02/hippie02sex02.png"
        pause 0.05
        "Explore02/hippie02sex03.png"
        pause 0.05
        "Explore02/hippie02sex04.png"
        pause 0.05
        "Explore02/hippie02sex05.png"
        pause 0.05
        "Explore02/hippie02sex06.png"
        pause 0.05
        "Explore02/hippie02sex07.png"
        pause 0.05
        "Explore02/hippie02sex08.png"
        pause 0.10
        "Explore02/hippie02sex09.png"
        pause 0.10
        "Explore02/hippie02sex08.png"
        pause 0.04
        "Explore02/hippie02sex07.png"
        pause 0.04
        "Explore02/hippie02sex06.png"
        pause 0.04
        "Explore02/hippie02sex05.png"
        pause 0.04
        "Explore02/hippie02sex04.png"
        pause 0.04
        "Explore02/hippie02sex03.png"
        pause 0.04
        "Explore02/hippie02sex02.png"
        pause 0.04
        "Explore02/hippie02sex01.png"
        pause 0.04
        repeat
            
    image hippyfuck02fast:
        "Explore02/hippie02sex00.png"
        pause 0.03
        "Explore02/hippie02sex01.png"
        pause 0.03
        "Explore02/hippie02sex02.png"
        pause 0.03
        "Explore02/hippie02sex03.png"
        pause 0.03
        "Explore02/hippie02sex04.png"
        pause 0.03
        "Explore02/hippie02sex05.png"
        pause 0.03
        "Explore02/hippie02sex06.png"
        pause 0.03
        "Explore02/hippie02sex07.png"
        pause 0.04
        "Explore02/hippie02sex08.png"
        pause 0.05
        "Explore02/hippie02sex09.png"
        pause 0.05
        "Explore02/hippie02sex08.png"
        pause 0.02
        "Explore02/hippie02sex07.png"
        pause 0.02
        "Explore02/hippie02sex06.png"
        pause 0.02
        "Explore02/hippie02sex05.png"
        pause 0.02
        "Explore02/hippie02sex04.png"
        pause 0.02
        "Explore02/hippie02sex03.png"
        pause 0.02
        "Explore02/hippie02sex02.png"
        pause 0.02
        "Explore02/hippie02sex01.png"
        pause 0.02
        repeat

    image hippyfuck01slow:
        "Explore02/hippiesex00.png"
        pause 0.05
        "Explore02/hippiesex01.png"
        pause 0.05
        "Explore02/hippiesex02.png"
        pause 0.05
        "Explore02/hippiesex03.png"
        pause 0.05
        "Explore02/hippiesex04.png"
        pause 0.05
        "Explore02/hippiesex05.png"
        pause 0.05
        "Explore02/hippiesex06.png"
        pause 0.05
        "Explore02/hippiesex07.png"
        pause 0.05
        "Explore02/hippiesex08.png"
        pause 0.05
        "Explore02/hippiesex09.png"
        pause 0.05
        "Explore02/hippiesex10.png"
        pause 0.05
        "Explore02/hippiesex11.png"
        pause 0.1
        "Explore02/hippiesex10.png"
        pause 0.05
        "Explore02/hippiesex09.png"
        pause 0.04
        "Explore02/hippiesex08.png"
        pause 0.04
        "Explore02/hippiesex07.png"
        pause 0.04
        "Explore02/hippiesex06.png"
        pause 0.04
        "Explore02/hippiesex05.png"
        pause 0.04
        "Explore02/hippiesex04.png"
        pause 0.04
        "Explore02/hippiesex03.png"
        pause 0.04
        "Explore02/hippiesex02.png"
        pause 0.04
        "Explore02/hippiesex01.png"
        pause 0.04
        repeat

    image hippyfuck01fast:
        "Explore02/hippiesex00.png"
        pause 0.03
        "Explore02/hippiesex01.png"
        pause 0.03
        "Explore02/hippiesex02.png"
        pause 0.03
        "Explore02/hippiesex03.png"
        pause 0.03
        "Explore02/hippiesex04.png"
        pause 0.03
        "Explore02/hippiesex05.png"
        pause 0.03
        "Explore02/hippiesex06.png"
        pause 0.03
        "Explore02/hippiesex07.png"
        pause 0.04
        "Explore02/hippiesex08.png"
        pause 0.04
        "Explore02/hippiesex09.png"
        pause 0.04
        "Explore02/hippiesex10.png"
        pause 0.04
        "Explore02/hippiesex11.png"
        pause 0.1
        "Explore02/hippiesex10.png"
        pause 0.03
        "Explore02/hippiesex09.png"
        pause 0.02
        "Explore02/hippiesex08.png"
        pause 0.02
        "Explore02/hippiesex07.png"
        pause 0.02
        "Explore02/hippiesex06.png"
        pause 0.02
        "Explore02/hippiesex05.png"
        pause 0.02
        "Explore02/hippiesex04.png"
        pause 0.02
        "Explore02/hippiesex03.png"
        pause 0.02
        "Explore02/hippiesex02.png"
        pause 0.02
        "Explore02/hippiesex01.png"
        pause 0.02
        repeat
    
    image titahontasslow:
        "Explore02/titahontasbounce00.jpg"
        pause 0.04
        "Explore02/titahontasbounce01.jpg"
        pause 0.04
        "Explore02/titahontasbounce02.jpg"
        pause 0.04
        "Explore02/titahontasbounce03.jpg"
        pause 0.04
        "Explore02/titahontasbounce04.jpg"
        pause 0.04
        "Explore02/titahontasbounce05.jpg"
        pause 0.04
        "Explore02/titahontasbounce06.jpg"
        pause 0.04
        "Explore02/titahontasbounce07.jpg"
        pause 0.04
        "Explore02/titahontasbounce08.jpg"
        pause 0.04
        "Explore02/titahontasbounce09.jpg"
        pause 0.04
        "Explore02/titahontasbounce10.jpg"
        pause 0.04
        "Explore02/titahontasbounce11.jpg"
        pause 0.04
        "Explore02/titahontasbounce12.jpg"
        pause 0.04
        "Explore02/titahontasbounce11.jpg"
        pause 0.03
        "Explore02/titahontasbounce10.jpg"
        pause 0.03
        "Explore02/titahontasbounce09.jpg"
        pause 0.03
        "Explore02/titahontasbounce08.jpg"
        pause 0.03
        "Explore02/titahontasbounce07.jpg"
        pause 0.03
        "Explore02/titahontasbounce06.jpg"
        pause 0.03
        "Explore02/titahontasbounce05.jpg"
        pause 0.03
        "Explore02/titahontasbounce04.jpg"
        pause 0.03
        "Explore02/titahontasbounce03.jpg"
        pause 0.03
        "Explore02/titahontasbounce02.jpg"
        pause 0.03
        "Explore02/titahontasbounce01.jpg"
        pause 0.03
        repeat

    image titahontasfast:
        "Explore02/titahontasbounce00.jpg"
        pause 0.03
        "Explore02/titahontasbounce01.jpg"
        pause 0.03
        "Explore02/titahontasbounce02.jpg"
        pause 0.03
        "Explore02/titahontasbounce03.jpg"
        pause 0.03
        "Explore02/titahontasbounce04.jpg"
        pause 0.03
        "Explore02/titahontasbounce05.jpg"
        pause 0.03
        "Explore02/titahontasbounce06.jpg"
        pause 0.03
        "Explore02/titahontasbounce07.jpg"
        pause 0.03
        "Explore02/titahontasbounce08.jpg"
        pause 0.03
        "Explore02/titahontasbounce09.jpg"
        pause 0.03
        "Explore02/titahontasbounce10.jpg"
        pause 0.03
        "Explore02/titahontasbounce11.jpg"
        pause 0.03
        "Explore02/titahontasbounce12.jpg"
        pause 0.03
        "Explore02/titahontasbounce11.jpg"
        pause 0.02
        "Explore02/titahontasbounce10.jpg"
        pause 0.02
        "Explore02/titahontasbounce09.jpg"
        pause 0.02
        "Explore02/titahontasbounce08.jpg"
        pause 0.02
        "Explore02/titahontasbounce07.jpg"
        pause 0.02
        "Explore02/titahontasbounce06.jpg"
        pause 0.02
        "Explore02/titahontasbounce05.jpg"
        pause 0.02
        "Explore02/titahontasbounce04.jpg"
        pause 0.02
        "Explore02/titahontasbounce03.jpg"
        pause 0.02
        "Explore02/titahontasbounce02.jpg"
        pause 0.02
        "Explore02/titahontasbounce01.jpg"
        pause 0.02
        repeat
    
    image titahontasslowb:
        "Explore02/titahontasbounceb00.jpg"
        pause 0.04
        "Explore02/titahontasbounceb01.jpg"
        pause 0.04
        "Explore02/titahontasbounceb02.jpg"
        pause 0.04
        "Explore02/titahontasbounceb03.jpg"
        pause 0.04
        "Explore02/titahontasbounceb04.jpg"
        pause 0.04
        "Explore02/titahontasbounceb05.jpg"
        pause 0.04
        "Explore02/titahontasbounceb06.jpg"
        pause 0.04
        "Explore02/titahontasbounceb07.jpg"
        pause 0.04
        "Explore02/titahontasbounceb08.jpg"
        pause 0.04
        "Explore02/titahontasbounceb09.jpg"
        pause 0.04
        "Explore02/titahontasbounceb10.jpg"
        pause 0.04
        "Explore02/titahontasbounceb11.jpg"
        pause 0.04
        "Explore02/titahontasbounceb12.jpg"
        pause 0.04
        "Explore02/titahontasbounceb11.jpg"
        pause 0.03
        "Explore02/titahontasbounceb10.jpg"
        pause 0.03
        "Explore02/titahontasbounceb09.jpg"
        pause 0.03
        "Explore02/titahontasbounceb08.jpg"
        pause 0.03
        "Explore02/titahontasbounceb07.jpg"
        pause 0.03
        "Explore02/titahontasbounceb06.jpg"
        pause 0.03
        "Explore02/titahontasbounceb05.jpg"
        pause 0.03
        "Explore02/titahontasbounceb04.jpg"
        pause 0.03
        "Explore02/titahontasbounceb03.jpg"
        pause 0.03
        "Explore02/titahontasbounceb02.jpg"
        pause 0.03
        "Explore02/titahontasbounceb01.jpg"
        pause 0.03
        repeat

    image titahontasfastb:
        "Explore02/titahontasbounceb00.jpg"
        pause 0.03
        "Explore02/titahontasbounceb01.jpg"
        pause 0.03
        "Explore02/titahontasbounceb02.jpg"
        pause 0.03
        "Explore02/titahontasbounceb03.jpg"
        pause 0.03
        "Explore02/titahontasbounceb04.jpg"
        pause 0.03
        "Explore02/titahontasbounceb05.jpg"
        pause 0.03
        "Explore02/titahontasbounceb06.jpg"
        pause 0.03
        "Explore02/titahontasbounceb07.jpg"
        pause 0.03
        "Explore02/titahontasbounceb08.jpg"
        pause 0.03
        "Explore02/titahontasbounceb09.jpg"
        pause 0.03
        "Explore02/titahontasbounceb10.jpg"
        pause 0.03
        "Explore02/titahontasbounceb11.jpg"
        pause 0.03
        "Explore02/titahontasbounceb12.jpg"
        pause 0.03
        "Explore02/titahontasbounceb11.jpg"
        pause 0.02
        "Explore02/titahontasbounceb10.jpg"
        pause 0.02
        "Explore02/titahontasbounceb09.jpg"
        pause 0.02
        "Explore02/titahontasbounceb08.jpg"
        pause 0.02
        "Explore02/titahontasbounceb07.jpg"
        pause 0.02
        "Explore02/titahontasbounceb06.jpg"
        pause 0.02
        "Explore02/titahontasbounceb05.jpg"
        pause 0.02
        "Explore02/titahontasbounceb04.jpg"
        pause 0.02
        "Explore02/titahontasbounceb03.jpg"
        pause 0.02
        "Explore02/titahontasbounceb02.jpg"
        pause 0.02
        "Explore02/titahontasbounceb01.jpg"
        pause 0.02
        repeat
    
    image titaanalslow:
        "Explore02/titaanal00.jpg"
        pause 0.04
        "Explore02/titaanal01.jpg"
        pause 0.04
        "Explore02/titaanal02.jpg"
        pause 0.04
        "Explore02/titaanal03.jpg"
        pause 0.04
        "Explore02/titaanal04.jpg"
        pause 0.04
        "Explore02/titaanal05.jpg"
        pause 0.04
        "Explore02/titaanal06.jpg"
        pause 0.04
        "Explore02/titaanal07.jpg"
        pause 0.04
        "Explore02/titaanal08.jpg"
        pause 0.04
        "Explore02/titaanal09.jpg"
        pause 0.06
        "Explore02/titaanal08.jpg"
        pause 0.03
        "Explore02/titaanal07.jpg"
        pause 0.03
        "Explore02/titaanal06.jpg"
        pause 0.03
        "Explore02/titaanal05.jpg"
        pause 0.03
        "Explore02/titaanal04.jpg"
        pause 0.03
        "Explore02/titaanal03.jpg"
        pause 0.03
        "Explore02/titaanal02.jpg"
        pause 0.03
        "Explore02/titaanal01.jpg"
        pause 0.03
        repeat

    image titaanalfast:
        "Explore02/titaanal00.jpg"
        pause 0.03
        "Explore02/titaanal01.jpg"
        pause 0.03
        "Explore02/titaanal02.jpg"
        pause 0.03
        "Explore02/titaanal03.jpg"
        pause 0.03
        "Explore02/titaanal04.jpg"
        pause 0.03
        "Explore02/titaanal05.jpg"
        pause 0.03
        "Explore02/titaanal06.jpg"
        pause 0.03
        "Explore02/titaanal07.jpg"
        pause 0.03
        "Explore02/titaanal08.jpg"
        pause 0.03
        "Explore02/titaanal09.jpg"
        pause 0.05
        "Explore02/titaanal08.jpg"
        pause 0.02
        "Explore02/titaanal07.jpg"
        pause 0.02
        "Explore02/titaanal06.jpg"
        pause 0.02
        "Explore02/titaanal05.jpg"
        pause 0.02
        "Explore02/titaanal04.jpg"
        pause 0.02
        "Explore02/titaanal03.jpg"
        pause 0.02
        "Explore02/titaanal02.jpg"
        pause 0.02
        "Explore02/titaanal01.jpg"
        pause 0.02
        repeat

    image bountyslow:
        "Explore02/bountyanal00.png"
        pause 0.03
        "Explore02/bountyanal01.png"
        pause 0.03
        "Explore02/bountyanal02.png"
        pause 0.03
        "Explore02/bountyanal03.png"
        pause 0.03
        "Explore02/bountyanal04.png"
        pause 0.03
        "Explore02/bountyanal05.png"
        pause 0.03
        "Explore02/bountyanal06.png"
        pause 0.03
        "Explore02/bountyanal07.png"
        pause 0.03
        "Explore02/bountyanal08.png"
        pause 0.03
        "Explore02/bountyanal09.png"
        pause 0.03
        "Explore02/bountyanal10.png"
        pause 0.03
        "Explore02/bountyanal09.png"
        pause 0.04
        "Explore02/bountyanal08.png"
        pause 0.04
        "Explore02/bountyanal07.png"
        pause 0.04
        "Explore02/bountyanal06.png"
        pause 0.04
        "Explore02/bountyanal05.png"
        pause 0.04
        "Explore02/bountyanal04.png"
        pause 0.04
        "Explore02/bountyanal03.png"
        pause 0.04
        "Explore02/bountyanal02.png"
        pause 0.04
        "Explore02/bountyanal01.png"
        pause 0.04
        repeat

    image bountyfast:
        "Explore02/bountyanal00.png"
        pause 0.02
        "Explore02/bountyanal01.png"
        pause 0.02
        "Explore02/bountyanal02.png"
        pause 0.02
        "Explore02/bountyanal03.png"
        pause 0.02
        "Explore02/bountyanal04.png"
        pause 0.02
        "Explore02/bountyanal05.png"
        pause 0.02
        "Explore02/bountyanal06.png"
        pause 0.02
        "Explore02/bountyanal07.png"
        pause 0.02
        "Explore02/bountyanal08.png"
        pause 0.02
        "Explore02/bountyanal09.png"
        pause 0.02
        "Explore02/bountyanal10.png"
        pause 0.02
        "Explore02/bountyanal09.png"
        pause 0.03
        "Explore02/bountyanal08.png"
        pause 0.03
        "Explore02/bountyanal07.png"
        pause 0.03
        "Explore02/bountyanal06.png"
        pause 0.03
        "Explore02/bountyanal05.png"
        pause 0.03
        "Explore02/bountyanal04.png"
        pause 0.03
        "Explore02/bountyanal03.png"
        pause 0.03
        "Explore02/bountyanal02.png"
        pause 0.03
        "Explore02/bountyanal01.png"
        pause 0.03
        repeat

    image bountybjslow:
        "Explore02/bountybj00.png"
        pause 0.03
        "Explore02/bountybj01.png"
        pause 0.03
        "Explore02/bountybj02.png"
        pause 0.03
        "Explore02/bountybj03.png"
        pause 0.03
        "Explore02/bountybj04.png"
        pause 0.03
        "Explore02/bountybj05.png"
        pause 0.03
        "Explore02/bountybj06.png"
        pause 0.03
        "Explore02/bountybj07.png"
        pause 0.03
        "Explore02/bountybj08.png"
        pause 0.03
        "Explore02/bountybj09.png"
        pause 0.03
        "Explore02/bountybj10.png"
        pause 0.03
        "Explore02/bountybj09.png"
        pause 0.04
        "Explore02/bountybj08.png"
        pause 0.04
        "Explore02/bountybj07.png"
        pause 0.04
        "Explore02/bountybj06.png"
        pause 0.04
        "Explore02/bountybj05.png"
        pause 0.04
        "Explore02/bountybj04.png"
        pause 0.04
        "Explore02/bountybj03.png"
        pause 0.04
        "Explore02/bountybj02.png"
        pause 0.04
        "Explore02/bountybj01.png"
        pause 0.04
        repeat

    image bountybjfast:
        "Explore02/bountybj00.png"
        pause 0.02
        "Explore02/bountybj01.png"
        pause 0.02
        "Explore02/bountybj02.png"
        pause 0.02
        "Explore02/bountybj03.png"
        pause 0.02
        "Explore02/bountybj04.png"
        pause 0.02
        "Explore02/bountybj05.png"
        pause 0.02
        "Explore02/bountybj06.png"
        pause 0.02
        "Explore02/bountybj07.png"
        pause 0.02
        "Explore02/bountybj08.png"
        pause 0.02
        "Explore02/bountybj09.png"
        pause 0.02
        "Explore02/bountybj10.png"
        pause 0.02
        "Explore02/bountybj09.png"
        pause 0.03
        "Explore02/bountybj08.png"
        pause 0.03
        "Explore02/bountybj07.png"
        pause 0.03
        "Explore02/bountybj06.png"
        pause 0.03
        "Explore02/bountybj05.png"
        pause 0.03
        "Explore02/bountybj04.png"
        pause 0.03
        "Explore02/bountybj03.png"
        pause 0.03
        "Explore02/bountybj02.png"
        pause 0.03
        "Explore02/bountybj01.png"
        pause 0.03
        repeat

    image stripgwenhandjobslow:
        "Stripping/gwenhandjob00.jpg"
        pause 0.06
        "Stripping/gwenhandjob01.jpg"
        pause 0.06
        "Stripping/gwenhandjob02.jpg"
        pause 0.06
        "Stripping/gwenhandjob03.jpg"
        pause 0.06
        "Stripping/gwenhandjob04.jpg"
        pause 0.06
        "Stripping/gwenhandjob05.jpg"
        pause 0.06
        "Stripping/gwenhandjob06.jpg"
        pause 0.06
        "Stripping/gwenhandjob07.jpg"
        pause 0.06
        "Stripping/gwenhandjob08.jpg"
        pause 0.06
        "Stripping/gwenhandjob09.jpg"
        pause 0.06
        "Stripping/gwenhandjob10.jpg"
        pause 0.06
        "Stripping/gwenhandjob11.jpg"
        pause 0.06
        "Stripping/gwenhandjob12.jpg"
        pause 0.06
        "Stripping/gwenhandjob13.jpg"
        pause 0.06
        "Stripping/gwenhandjob14.jpg"
        pause 0.06
        "Stripping/gwenhandjob15.jpg"
        pause 0.06
        "Stripping/gwenhandjob16.jpg"
        pause 0.06
        "Stripping/gwenhandjob17.jpg"
        pause 0.06
        "Stripping/gwenhandjob18.jpg"
        pause 0.06
        "Stripping/gwenhandjob19.jpg"
        pause 0.06
        "Stripping/gwenhandjob20.jpg"
        pause 0.06
        "Stripping/gwenhandjob21.jpg"
        pause 0.06
        "Stripping/gwenhandjob22.jpg"
        pause 0.06
        "Stripping/gwenhandjob23.jpg"
        pause 0.06
        "Stripping/gwenhandjob24.jpg"
        pause 0.06
        repeat

    image stripgwenhandjobfast:
        "Stripping/gwenhandjob00.jpg"
        pause 0.04
        "Stripping/gwenhandjob01.jpg"
        pause 0.04
        "Stripping/gwenhandjob02.jpg"
        pause 0.04
        "Stripping/gwenhandjob03.jpg"
        pause 0.04
        "Stripping/gwenhandjob04.jpg"
        pause 0.04
        "Stripping/gwenhandjob05.jpg"
        pause 0.04
        "Stripping/gwenhandjob06.jpg"
        pause 0.04
        "Stripping/gwenhandjob07.jpg"
        pause 0.04
        "Stripping/gwenhandjob08.jpg"
        pause 0.04
        "Stripping/gwenhandjob09.jpg"
        pause 0.04
        "Stripping/gwenhandjob10.jpg"
        pause 0.04
        "Stripping/gwenhandjob11.jpg"
        pause 0.04
        "Stripping/gwenhandjob12.jpg"
        pause 0.04
        "Stripping/gwenhandjob13.jpg"
        pause 0.04
        "Stripping/gwenhandjob14.jpg"
        pause 0.04
        "Stripping/gwenhandjob15.jpg"
        pause 0.04
        "Stripping/gwenhandjob16.jpg"
        pause 0.04
        "Stripping/gwenhandjob17.jpg"
        pause 0.04
        "Stripping/gwenhandjob18.jpg"
        pause 0.04
        "Stripping/gwenhandjob19.jpg"
        pause 0.04
        "Stripping/gwenhandjob20.jpg"
        pause 0.04
        "Stripping/gwenhandjob21.jpg"
        pause 0.04
        "Stripping/gwenhandjob22.jpg"
        pause 0.04
        "Stripping/gwenhandjob23.jpg"
        pause 0.04
        "Stripping/gwenhandjob24.jpg"
        pause 0.04
        repeat
            
    image nancywiggle:
        "Nancy/nancywig000.png"
        pause 0.03
        "Nancy/nancywig001.png"
        pause 0.03
        "Nancy/nancywig002.png"
        pause 0.03
        "Nancy/nancywig003.png"
        pause 0.03
        "Nancy/nancywig004.png"
        pause 0.03
        "Nancy/nancywig005.png"
        pause 0.03
        "Nancy/nancywig006.png"
        pause 0.03
        "Nancy/nancywig007.png"
        pause 0.03
        "Nancy/nancywig008.png"
        pause 0.03
        "Nancy/nancywig009.png"
        pause 0.03
        "Nancy/nancywig010.png"
        pause 0.03
        "Nancy/nancywig011.png"
        pause 0.03
        "Nancy/nancywig012.png"
        pause 0.03
        "Nancy/nancywig013.png"
        pause 0.03
        "Nancy/nancywig014.png"
        pause 0.03
        "Nancy/nancywig015.png"
        pause 0.03
        "Nancy/nancywig016.png"
        pause 0.03
        "Nancy/nancywig017.png"
        pause 0.03
        "Nancy/nancywig018.png"
        pause 0.03
        "Nancy/nancywig019.png"
        pause 0.03
        "Nancy/nancywig020.png"
        pause 0.03
        "Nancy/nancywig021.png"
        pause 0.03
        "Nancy/nancywig022.png"
        pause 0.03
        "Nancy/nancywig023.png"
        pause 0.03
        "Nancy/nancywig024.png"
        pause 0.03
        "Nancy/nancywig025.png"
        pause 0.03
        "Nancy/nancywig026.png"
        pause 0.03
        "Nancy/nancywig027.png"
        pause 0.03
        "Nancy/nancywig028.png"
        pause 0.03
        "Nancy/nancywig029.png"
        pause 0.03
        "Nancy/nancywig030.png"
        pause 0.03
        repeat
            
    image sukiwiggle:
        "Suki/sukiwiggle000.png"
        pause 0.03
        "Suki/sukiwiggle001.png"
        pause 0.03
        "Suki/sukiwiggle002.png"
        pause 0.03
        "Suki/sukiwiggle003.png"
        pause 0.03
        "Suki/sukiwiggle004.png"
        pause 0.03
        "Suki/sukiwiggle005.png"
        pause 0.03
        "Suki/sukiwiggle006.png"
        pause 0.03
        "Suki/sukiwiggle007.png"
        pause 0.03
        "Suki/sukiwiggle008.png"
        pause 0.03
        "Suki/sukiwiggle009.png"
        pause 0.03
        "Suki/sukiwiggle010.png"
        pause 0.03
        "Suki/sukiwiggle011.png"
        pause 0.03
        "Suki/sukiwiggle012.png"
        pause 0.03
        "Suki/sukiwiggle013.png"
        pause 0.03
        "Suki/sukiwiggle014.png"
        pause 0.03
        "Suki/sukiwiggle015.png"
        pause 0.03
        "Suki/sukiwiggle016.png"
        pause 0.03
        "Suki/sukiwiggle017.png"
        pause 0.03
        "Suki/sukiwiggle018.png"
        pause 0.03
        "Suki/sukiwiggle019.png"
        pause 0.03
        "Suki/sukiwiggle020.png"
        pause 0.03
        "Suki/sukiwiggle021.png"
        pause 0.03
        "Suki/sukiwiggle022.png"
        pause 0.03
        "Suki/sukiwiggle023.png"
        pause 0.03
        "Suki/sukiwiggle024.png"
        pause 0.03
        "Suki/sukiwiggle025.png"
        pause 0.03
        "Suki/sukiwiggle026.png"
        pause 0.03
        "Suki/sukiwiggle027.png"
        pause 0.03
        "Suki/sukiwiggle028.png"
        pause 0.03
        "Suki/sukiwiggle029.png"
        pause 0.03
        "Suki/sukiwiggle030.png"
        pause 0.03
        "Suki/sukiwiggle031.png"
        pause 0.03
        repeat

    image sukiimpaleslow:
        "Suki/mcbedsukijump00.jpg"
        pause 0.08
        "Suki/mcbedsukijump01.jpg"
        pause 0.05
        "Suki/mcbedsukijump02.jpg"
        pause 0.05
        "Suki/mcbedsukijump03.jpg"
        pause 0.05
        "Suki/mcbedsukijump04.jpg"
        pause 0.05
        "Suki/mcbedsukijump05.jpg"
        pause 0.05
        "Suki/mcbedsukijump06.jpg"
        pause 0.05
        "Suki/mcbedsukijump07.jpg"
        pause 0.05
        "Suki/mcbedsukijump08.jpg"
        pause 0.05
        "Suki/mcbedsukijump09.jpg"
        pause 0.05
        "Suki/mcbedsukijump10.jpg"
        pause 0.05
        "Suki/mcbedsukijump11.jpg"
        repeat

    image sukiimpalefast:
        "Suki/mcbedsukijump00.jpg"
        pause 0.05
        "Suki/mcbedsukijump01.jpg"
        pause 0.03
        "Suki/mcbedsukijump02.jpg"
        pause 0.03
        "Suki/mcbedsukijump03.jpg"
        pause 0.03
        "Suki/mcbedsukijump04.jpg"
        pause 0.03
        "Suki/mcbedsukijump05.jpg"
        pause 0.03
        "Suki/mcbedsukijump06.jpg"
        pause 0.03
        "Suki/mcbedsukijump07.jpg"
        pause 0.03
        "Suki/mcbedsukijump08.jpg"
        pause 0.03
        "Suki/mcbedsukijump09.jpg"
        pause 0.03
        "Suki/mcbedsukijump10.jpg"
        pause 0.03
        "Suki/mcbedsukijump11.jpg"
        pause 0.03
        repeat

    image mcbedroomsukislow:
        "Suki/mcbedroomsukianim00.jpg"
        pause 0.06
        "Suki/mcbedroomsukianim01.jpg"
        pause 0.06
        "Suki/mcbedroomsukianim02.jpg"
        pause 0.06
        "Suki/mcbedroomsukianim03.jpg"
        pause 0.06
        "Suki/mcbedroomsukianim04.jpg"
        pause 0.06
        "Suki/mcbedroomsukianim05.jpg"
        pause 0.06
        "Suki/mcbedroomsukianim06.jpg"
        pause 0.06
        "Suki/mcbedroomsukianim07.jpg"
        pause 0.06
        "Suki/mcbedroomsukianim08.jpg"
        pause 0.06
        "Suki/mcbedroomsukianim09.jpg"
        pause 0.06
        "Suki/mcbedroomsukianim08.jpg"
        pause 0.06
        "Suki/mcbedroomsukianim07.jpg"
        pause 0.06
        "Suki/mcbedroomsukianim06.jpg"
        pause 0.06
        "Suki/mcbedroomsukianim05.jpg"
        pause 0.06
        "Suki/mcbedroomsukianim04.jpg"
        pause 0.06
        "Suki/mcbedroomsukianim03.jpg"
        pause 0.06
        "Suki/mcbedroomsukianim02.jpg"
        pause 0.06
        "Suki/mcbedroomsukianim01.jpg"
        pause 0.06
        repeat

    image mcbedroomsukifast:
        "Suki/mcbedroomsukianim00.jpg"
        pause 0.04
        "Suki/mcbedroomsukianim01.jpg"
        pause 0.04
        "Suki/mcbedroomsukianim02.jpg"
        pause 0.04
        "Suki/mcbedroomsukianim03.jpg"
        pause 0.04
        "Suki/mcbedroomsukianim04.jpg"
        pause 0.04
        "Suki/mcbedroomsukianim05.jpg"
        pause 0.04
        "Suki/mcbedroomsukianim06.jpg"
        pause 0.04
        "Suki/mcbedroomsukianim07.jpg"
        pause 0.04
        "Suki/mcbedroomsukianim08.jpg"
        pause 0.04
        "Suki/mcbedroomsukianim09.jpg"
        pause 0.04
        "Suki/mcbedroomsukianim08.jpg"
        pause 0.04
        "Suki/mcbedroomsukianim07.jpg"
        pause 0.04
        "Suki/mcbedroomsukianim06.jpg"
        pause 0.04
        "Suki/mcbedroomsukianim05.jpg"
        pause 0.04
        "Suki/mcbedroomsukianim04.jpg"
        pause 0.04
        "Suki/mcbedroomsukianim03.jpg"
        pause 0.04
        "Suki/mcbedroomsukianim02.jpg"
        pause 0.04
        "Suki/mcbedroomsukianim01.jpg"
        pause 0.04
        repeat

    image sukiblowslow:
        "Suki/mcbedsukisuck00.jpg"
        pause 0.08
        "Suki/mcbedsukisuck01.jpg"
        pause 0.05
        "Suki/mcbedsukisuck02.jpg"
        pause 0.05
        "Suki/mcbedsukisuck03.jpg"
        pause 0.05
        "Suki/mcbedsukisuck04.jpg"
        pause 0.05
        "Suki/mcbedsukisuck05.jpg"
        pause 0.05
        "Suki/mcbedsukisuck06.jpg"
        pause 0.05
        "Suki/mcbedsukisuck07.jpg"
        pause 0.05
        "Suki/mcbedsukisuck08.jpg"
        pause 0.08
        "Suki/mcbedsukisuck07.jpg"
        pause 0.04
        "Suki/mcbedsukisuck06.jpg"
        pause 0.04
        "Suki/mcbedsukisuck05.jpg"
        pause 0.04
        "Suki/mcbedsukisuck04.jpg"
        pause 0.04
        "Suki/mcbedsukisuck03.jpg"
        pause 0.04
        "Suki/mcbedsukisuck02.jpg"
        pause 0.04
        "Suki/mcbedsukisuck01.jpg"
        pause 0.04
        repeat

    image sukiblowfast:
        "Suki/mcbedsukisuck00.jpg"
        pause 0.06
        "Suki/mcbedsukisuck01.jpg"
        pause 0.04
        "Suki/mcbedsukisuck02.jpg"
        pause 0.04
        "Suki/mcbedsukisuck03.jpg"
        pause 0.04
        "Suki/mcbedsukisuck04.jpg"
        pause 0.04
        "Suki/mcbedsukisuck05.jpg"
        pause 0.04
        "Suki/mcbedsukisuck06.jpg"
        pause 0.04
        "Suki/mcbedsukisuck07.jpg"
        pause 0.04
        "Suki/mcbedsukisuck08.jpg"
        pause 0.06
        "Suki/mcbedsukisuck07.jpg"
        pause 0.03
        "Suki/mcbedsukisuck06.jpg"
        pause 0.03
        "Suki/mcbedsukisuck05.jpg"
        pause 0.03
        "Suki/mcbedsukisuck04.jpg"
        pause 0.03
        "Suki/mcbedsukisuck03.jpg"
        pause 0.03
        "Suki/mcbedsukisuck02.jpg"
        pause 0.03
        "Suki/mcbedsukisuck01.jpg"
        pause 0.03
        repeat

    image mcsukiprejump:
        "Suki/sukiprejump00.jpg"
        pause 0.1
        "Suki/sukiprejump01.jpg"
        pause 0.06
        "Suki/sukiprejump02.jpg"
        pause 0.06
        "Suki/sukiprejump03.jpg"
        pause 0.06
        "Suki/sukiprejump04.jpg"
        pause 0.06
        "Suki/sukiprejump05.jpg"
        pause 0.06
        "Suki/sukiprejump06.jpg"
        pause 0.06
        "Suki/sukiprejump07.jpg"
        pause 0.06
        "Suki/sukiprejump08.jpg"
        pause 0.06
        "Suki/sukiprejump09.jpg"
        pause 0.1
        "Suki/sukiprejump08.jpg"
        pause 0.06
        "Suki/sukiprejump07.jpg"
        pause 0.06
        "Suki/sukiprejump06.jpg"
        pause 0.06
        "Suki/sukiprejump05.jpg"
        pause 0.06
        "Suki/sukiprejump04.jpg"
        pause 0.06
        "Suki/sukiprejump03.jpg"
        pause 0.06
        "Suki/sukiprejump02.jpg"
        pause 0.06
        "Suki/sukiprejump01.jpg"
        pause 0.06
        repeat

    image mcsukifuckslow:
        "Suki/sukibedfuck00.png"
        pause 0.04
        "Suki/sukibedfuck01.png"
        pause 0.04
        "Suki/sukibedfuck02.png"
        pause 0.04
        "Suki/sukibedfuck03.png"
        pause 0.04
        "Suki/sukibedfuck04.png"
        pause 0.04
        "Suki/sukibedfuck05.png"
        pause 0.04
        "Suki/sukibedfuck06.png"
        pause 0.04
        "Suki/sukibedfuck07.png"
        pause 0.04
        "Suki/sukibedfuck08.png"
        pause 0.04
        "Suki/sukibedfuck09.png"
        pause 0.04
        "Suki/sukibedfuck08.png"
        pause 0.04
        "Suki/sukibedfuck07.png"
        pause 0.04
        "Suki/sukibedfuck06.png"
        pause 0.04
        "Suki/sukibedfuck05.png"
        pause 0.04
        "Suki/sukibedfuck04.png"
        pause 0.04
        "Suki/sukibedfuck03.png"
        pause 0.04
        "Suki/sukibedfuck02.png"
        pause 0.04
        "Suki/sukibedfuck01.png"
        pause 0.04
        repeat

    image mcsukifuckfast:
        "Suki/sukibedfuck00.png"
        pause 0.03
        "Suki/sukibedfuck01.png"
        pause 0.03
        "Suki/sukibedfuck02.png"
        pause 0.03
        "Suki/sukibedfuck03.png"
        pause 0.03
        "Suki/sukibedfuck04.png"
        pause 0.03
        "Suki/sukibedfuck05.png"
        pause 0.03
        "Suki/sukibedfuck06.png"
        pause 0.03
        "Suki/sukibedfuck07.png"
        pause 0.03
        "Suki/sukibedfuck08.png"
        pause 0.03
        "Suki/sukibedfuck09.png"
        pause 0.03
        "Suki/sukibedfuck08.png"
        pause 0.03
        "Suki/sukibedfuck07.png"
        pause 0.03
        "Suki/sukibedfuck06.png"
        pause 0.03
        "Suki/sukibedfuck05.png"
        pause 0.03
        "Suki/sukibedfuck04.png"
        pause 0.03
        "Suki/sukibedfuck03.png"
        pause 0.03
        "Suki/sukibedfuck02.png"
        pause 0.03
        "Suki/sukibedfuck01.png"
        pause 0.03
        repeat

    image sukianalslow:
        "Suki/sukianal00.png"
        pause 0.04
        "Suki/sukianal01.png"
        pause 0.04
        "Suki/sukianal02.png"
        pause 0.04
        "Suki/sukianal03.png"
        pause 0.04
        "Suki/sukianal04.png"
        pause 0.04
        "Suki/sukianal05.png"
        pause 0.04
        "Suki/sukianal06.png"
        pause 0.04
        "Suki/sukianal07.png"
        pause 0.04
        "Suki/sukianal08.png"
        pause 0.04
        "Suki/sukianal09.png"
        pause 0.04
        "Suki/sukianal08.png"
        pause 0.04
        "Suki/sukianal07.png"
        pause 0.04
        "Suki/sukianal06.png"
        pause 0.04
        "Suki/sukianal05.png"
        pause 0.04
        "Suki/sukianal04.png"
        pause 0.04
        "Suki/sukianal03.png"
        pause 0.04
        "Suki/sukianal02.png"
        pause 0.04
        "Suki/sukianal01.png"
        pause 0.04
        repeat

    image sukianalfast:
        "Suki/sukianal00.png"
        pause 0.03
        "Suki/sukianal01.png"
        pause 0.03
        "Suki/sukianal02.png"
        pause 0.03
        "Suki/sukianal03.png"
        pause 0.03
        "Suki/sukianal04.png"
        pause 0.03
        "Suki/sukianal05.png"
        pause 0.03
        "Suki/sukianal06.png"
        pause 0.03
        "Suki/sukianal07.png"
        pause 0.03
        "Suki/sukianal08.png"
        pause 0.03
        "Suki/sukianal09.png"
        pause 0.03
        "Suki/sukianal08.png"
        pause 0.03
        "Suki/sukianal07.png"
        pause 0.03
        "Suki/sukianal06.png"
        pause 0.03
        "Suki/sukianal05.png"
        pause 0.03
        "Suki/sukianal04.png"
        pause 0.03
        "Suki/sukianal03.png"
        pause 0.03
        "Suki/sukianal02.png"
        pause 0.03
        "Suki/sukianal01.png"
        pause 0.03
        repeat

    image povsukianalslow:
        "Suki/sukianalpov00.png"
        pause 0.04
        "Suki/sukianalpov01.png"
        pause 0.04
        "Suki/sukianalpov02.png"
        pause 0.04
        "Suki/sukianalpov03.png"
        pause 0.04
        "Suki/sukianalpov04.png"
        pause 0.04
        "Suki/sukianalpov05.png"
        pause 0.04
        "Suki/sukianalpov06.png"
        pause 0.04
        "Suki/sukianalpov07.png"
        pause 0.04
        "Suki/sukianalpov08.png"
        pause 0.04
        "Suki/sukianalpov09.png"
        pause 0.04
        "Suki/sukianalpov08.png"
        pause 0.04
        "Suki/sukianalpov07.png"
        pause 0.04
        "Suki/sukianalpov06.png"
        pause 0.04
        "Suki/sukianalpov05.png"
        pause 0.04
        "Suki/sukianalpov04.png"
        pause 0.04
        "Suki/sukianalpov03.png"
        pause 0.04
        "Suki/sukianalpov02.png"
        pause 0.04
        "Suki/sukianalpov01.png"
        pause 0.04
        repeat

    image povsukianalfast:
        "Suki/sukianalpov00.png"
        pause 0.03
        "Suki/sukianalpov01.png"
        pause 0.03
        "Suki/sukianalpov02.png"
        pause 0.03
        "Suki/sukianalpov03.png"
        pause 0.03
        "Suki/sukianalpov04.png"
        pause 0.03
        "Suki/sukianalpov05.png"
        pause 0.03
        "Suki/sukianalpov06.png"
        pause 0.03
        "Suki/sukianalpov07.png"
        pause 0.03
        "Suki/sukianalpov08.png"
        pause 0.03
        "Suki/sukianalpov09.png"
        pause 0.03
        "Suki/sukianalpov08.png"
        pause 0.03
        "Suki/sukianalpov07.png"
        pause 0.03
        "Suki/sukianalpov06.png"
        pause 0.03
        "Suki/sukianalpov05.png"
        pause 0.03
        "Suki/sukianalpov04.png"
        pause 0.03
        "Suki/sukianalpov03.png"
        pause 0.03
        "Suki/sukianalpov02.png"
        pause 0.03
        "Suki/sukianalpov01.png"
        pause 0.03
        repeat

    image gwenwiggle:
        "Gwen/gwenwiggle00.png"
        pause 0.03
        "Gwen/gwenwiggle01.png"
        pause 0.03
        "Gwen/gwenwiggle02.png"
        pause 0.03
        "Gwen/gwenwiggle03.png"
        pause 0.03
        "Gwen/gwenwiggle04.png"
        pause 0.03
        "Gwen/gwenwiggle05.png"
        pause 0.03
        "Gwen/gwenwiggle06.png"
        pause 0.03
        "Gwen/gwenwiggle07.png"
        pause 0.03
        "Gwen/gwenwiggle08.png"
        pause 0.03
        "Gwen/gwenwiggle09.png"
        pause 0.03
        "Gwen/gwenwiggle10.png"
        pause 0.03
        "Gwen/gwenwiggle11.png"
        pause 0.03
        "Gwen/gwenwiggle12.png"
        pause 0.03
        "Gwen/gwenwiggle13.png"
        pause 0.03
        "Gwen/gwenwiggle14.png"
        pause 0.03
        "Gwen/gwenwiggle15.png"
        pause 0.03
        "Gwen/gwenwiggle16.png"
        pause 0.03
        "Gwen/gwenwiggle17.png"
        pause 0.03
        "Gwen/gwenwiggle18.png"
        pause 0.03
        "Gwen/gwenwiggle19.png"
        pause 0.03
        "Gwen/gwenwiggle20.png"
        pause 0.03
        "Gwen/gwenwiggle21.png"
        pause 0.03
        "Gwen/gwenwiggle22.png"
        pause 0.03
        "Gwen/gwenwiggle23.png"
        pause 0.03
        "Gwen/gwenwiggle24.png"
        pause 0.03
        "Gwen/gwenwiggle25.png"
        pause 0.03
        "Gwen/gwenwiggle26.png"
        pause 0.03
        "Gwen/gwenwiggle27.png"
        pause 0.03
        "Gwen/gwenwiggle28.png"
        pause 0.03
        "Gwen/gwenwiggle29.png"
        pause 0.03
        "Gwen/gwenwiggle30.png"
        pause 0.03
        "Gwen/gwenwiggle31.png"
        pause 0.03
        "Gwen/gwenwiggle32.png"
        pause 0.03
        repeat

    image gwenblowslow:
        "Gwen/gwenblownew00.png"
        pause 0.05
        "Gwen/gwenblownew01.png"
        pause 0.05
        "Gwen/gwenblownew02.png"
        pause 0.05
        "Gwen/gwenblownew03.png"
        pause 0.05
        "Gwen/gwenblownew04.png"
        pause 0.05
        "Gwen/gwenblownew05.png"
        pause 0.05
        "Gwen/gwenblownew06.png"
        pause 0.05
        "Gwen/gwenblownew07.png"
        pause 0.05
        "Gwen/gwenblownew08.png"
        pause 0.05
        "Gwen/gwenblownew09.png"
        pause 0.05
        "Gwen/gwenblownew10.png"
        pause 0.05
        "Gwen/gwenblownew11.png"
        pause 0.05
        "Gwen/gwenblownew12.png"
        pause 0.05
        "Gwen/gwenblownew13.png"
        pause 0.05
        "Gwen/gwenblownew14.png"
        pause 0.05
        "Gwen/gwenblownew15.png"
        pause 0.05
        "Gwen/gwenblownew16.png"
        pause 0.05
        "Gwen/gwenblownew17.png"
        pause 0.05
        repeat

    image gwenblowfast:
        "Gwen/gwenblownew00.png"
        pause 0.03
        "Gwen/gwenblownew01.png"
        pause 0.03
        "Gwen/gwenblownew02.png"
        pause 0.03
        "Gwen/gwenblownew03.png"
        pause 0.03
        "Gwen/gwenblownew04.png"
        pause 0.03
        "Gwen/gwenblownew05.png"
        pause 0.03
        "Gwen/gwenblownew06.png"
        pause 0.03
        "Gwen/gwenblownew07.png"
        pause 0.03
        "Gwen/gwenblownew08.png"
        pause 0.03
        "Gwen/gwenblownew09.png"
        pause 0.03
        "Gwen/gwenblownew10.png"
        pause 0.03
        "Gwen/gwenblownew11.png"
        pause 0.03
        "Gwen/gwenblownew12.png"
        pause 0.03
        "Gwen/gwenblownew13.png"
        pause 0.03
        "Gwen/gwenblownew14.png"
        pause 0.03
        "Gwen/gwenblownew15.png"
        pause 0.03
        "Gwen/gwenblownew16.png"
        pause 0.03
        "Gwen/gwenblownew17.png"
        pause 0.03
        repeat

    image gwenwallanalslow:
        "Gwen/gwenwallanal00.png"
        pause 0.08
        "Gwen/gwenwallanal01.png"
        pause 0.04
        "Gwen/gwenwallanal02.png"
        pause 0.04
        "Gwen/gwenwallanal03.png"
        pause 0.04
        "Gwen/gwenwallanal04.png"
        pause 0.04
        "Gwen/gwenwallanal05.png"
        pause 0.04
        "Gwen/gwenwallanal06.png"
        pause 0.04
        "Gwen/gwenwallanal07.png"
        pause 0.04
        "Gwen/gwenwallanal08.png"
        pause 0.04
        "Gwen/gwenwallanal09.png"
        pause 0.04
        "Gwen/gwenwallanal10.png"
        pause 0.06
        "Gwen/gwenwallanal09.png"
        pause 0.04
        "Gwen/gwenwallanal09.png"
        pause 0.04
        "Gwen/gwenwallanal08.png"
        pause 0.04
        "Gwen/gwenwallanal07.png"
        pause 0.04
        "Gwen/gwenwallanal06.png"
        pause 0.04
        "Gwen/gwenwallanal05.png"
        pause 0.04
        "Gwen/gwenwallanal04.png"
        pause 0.04
        "Gwen/gwenwallanal03.png"
        pause 0.04
        "Gwen/gwenwallanal02.png"
        pause 0.04
        "Gwen/gwenwallanal01.png"
        pause 0.04
        repeat
    
    image gwenwallanalfast:
        "Gwen/gwenwallanal00.png"
        pause 0.06
        "Gwen/gwenwallanal01.png"
        pause 0.03
        "Gwen/gwenwallanal02.png"
        pause 0.03
        "Gwen/gwenwallanal03.png"
        pause 0.03
        "Gwen/gwenwallanal04.png"
        pause 0.03
        "Gwen/gwenwallanal05.png"
        pause 0.03
        "Gwen/gwenwallanal06.png"
        pause 0.03
        "Gwen/gwenwallanal07.png"
        pause 0.03
        "Gwen/gwenwallanal08.png"
        pause 0.03
        "Gwen/gwenwallanal09.png"
        pause 0.03
        "Gwen/gwenwallanal10.png"
        pause 0.045
        "Gwen/gwenwallanal09.png"
        pause 0.03
        "Gwen/gwenwallanal09.png"
        pause 0.03
        "Gwen/gwenwallanal08.png"
        pause 0.03
        "Gwen/gwenwallanal07.png"
        pause 0.03
        "Gwen/gwenwallanal06.png"
        pause 0.03
        "Gwen/gwenwallanal05.png"
        pause 0.03
        "Gwen/gwenwallanal04.png"
        pause 0.03
        "Gwen/gwenwallanal03.png"
        pause 0.03
        "Gwen/gwenwallanal02.png"
        pause 0.03
        "Gwen/gwenwallanal01.png"
        pause 0.03
        repeat

    image gwenwallanalcumslow:
        "Gwen/gwenwallanalcum00.png"
        pause 0.08
        "Gwen/gwenwallanalcum01.png"
        pause 0.04
        "Gwen/gwenwallanalcum02.png"
        pause 0.04
        "Gwen/gwenwallanalcum03.png"
        pause 0.04
        "Gwen/gwenwallanalcum04.png"
        pause 0.04
        "Gwen/gwenwallanalcum05.png"
        pause 0.04
        "Gwen/gwenwallanalcum06.png"
        pause 0.04
        "Gwen/gwenwallanalcum07.png"
        pause 0.04
        "Gwen/gwenwallanalcum08.png"
        pause 0.04
        "Gwen/gwenwallanalcum09.png"
        pause 0.04
        "Gwen/gwenwallanalcum10.png"
        pause 0.06
        "Gwen/gwenwallanalcum09.png"
        pause 0.04
        "Gwen/gwenwallanalcum09.png"
        pause 0.04
        "Gwen/gwenwallanalcum08.png"
        pause 0.04
        "Gwen/gwenwallanalcum07.png"
        pause 0.04
        "Gwen/gwenwallanalcum06.png"
        pause 0.04
        "Gwen/gwenwallanalcum05.png"
        pause 0.04
        "Gwen/gwenwallanalcum04.png"
        pause 0.04
        "Gwen/gwenwallanalcum03.png"
        pause 0.04
        "Gwen/gwenwallanalcum02.png"
        pause 0.04
        "Gwen/gwenwallanalcum01.png"
        pause 0.04
        repeat
    
    image gwenwallanalcumfast:
        "Gwen/gwenwallanalcum00.png"
        pause 0.06
        "Gwen/gwenwallanalcum01.png"
        pause 0.03
        "Gwen/gwenwallanalcum02.png"
        pause 0.03
        "Gwen/gwenwallanalcum03.png"
        pause 0.03
        "Gwen/gwenwallanalcum04.png"
        pause 0.03
        "Gwen/gwenwallanalcum05.png"
        pause 0.03
        "Gwen/gwenwallanalcum06.png"
        pause 0.03
        "Gwen/gwenwallanalcum07.png"
        pause 0.03
        "Gwen/gwenwallanalcum08.png"
        pause 0.03
        "Gwen/gwenwallanalcum09.png"
        pause 0.03
        "Gwen/gwenwallanalcum10.png"
        pause 0.045
        "Gwen/gwenwallanalcum09.png"
        pause 0.03
        "Gwen/gwenwallanalcum09.png"
        pause 0.03
        "Gwen/gwenwallanalcum08.png"
        pause 0.03
        "Gwen/gwenwallanalcum07.png"
        pause 0.03
        "Gwen/gwenwallanalcum06.png"
        pause 0.03
        "Gwen/gwenwallanalcum05.png"
        pause 0.03
        "Gwen/gwenwallanalcum04.png"
        pause 0.03
        "Gwen/gwenwallanalcum03.png"
        pause 0.03
        "Gwen/gwenwallanalcum02.png"
        pause 0.03
        "Gwen/gwenwallanalcum01.png"
        pause 0.03
        repeat

    image gwenwallpussyslow:
        "Gwen/gwenwallpussy00.png"
        pause 0.08
        "Gwen/gwenwallpussy01.png"
        pause 0.04
        "Gwen/gwenwallpussy02.png"
        pause 0.04
        "Gwen/gwenwallpussy03.png"
        pause 0.04
        "Gwen/gwenwallpussy04.png"
        pause 0.04
        "Gwen/gwenwallpussy05.png"
        pause 0.04
        "Gwen/gwenwallpussy06.png"
        pause 0.04
        "Gwen/gwenwallpussy07.png"
        pause 0.04
        "Gwen/gwenwallpussy08.png"
        pause 0.04
        "Gwen/gwenwallpussy09.png"
        pause 0.04
        "Gwen/gwenwallpussy10.png"
        pause 0.06
        "Gwen/gwenwallpussy09.png"
        pause 0.04
        "Gwen/gwenwallpussy09.png"
        pause 0.04
        "Gwen/gwenwallpussy08.png"
        pause 0.04
        "Gwen/gwenwallpussy07.png"
        pause 0.04
        "Gwen/gwenwallpussy06.png"
        pause 0.04
        "Gwen/gwenwallpussy05.png"
        pause 0.04
        "Gwen/gwenwallpussy04.png"
        pause 0.04
        "Gwen/gwenwallpussy03.png"
        pause 0.04
        "Gwen/gwenwallpussy02.png"
        pause 0.04
        "Gwen/gwenwallpussy01.png"
        pause 0.04
        repeat
    
    image gwenwallpussyfast:
        "Gwen/gwenwallpussy00.png"
        pause 0.06
        "Gwen/gwenwallpussy01.png"
        pause 0.03
        "Gwen/gwenwallpussy02.png"
        pause 0.03
        "Gwen/gwenwallpussy03.png"
        pause 0.03
        "Gwen/gwenwallpussy04.png"
        pause 0.03
        "Gwen/gwenwallpussy05.png"
        pause 0.03
        "Gwen/gwenwallpussy06.png"
        pause 0.03
        "Gwen/gwenwallpussy07.png"
        pause 0.03
        "Gwen/gwenwallpussy08.png"
        pause 0.03
        "Gwen/gwenwallpussy09.png"
        pause 0.03
        "Gwen/gwenwallpussy10.png"
        pause 0.045
        "Gwen/gwenwallpussy09.png"
        pause 0.03
        "Gwen/gwenwallpussy09.png"
        pause 0.03
        "Gwen/gwenwallpussy08.png"
        pause 0.03
        "Gwen/gwenwallpussy07.png"
        pause 0.03
        "Gwen/gwenwallpussy06.png"
        pause 0.03
        "Gwen/gwenwallpussy05.png"
        pause 0.03
        "Gwen/gwenwallpussy04.png"
        pause 0.03
        "Gwen/gwenwallpussy03.png"
        pause 0.03
        "Gwen/gwenwallpussy02.png"
        pause 0.03
        "Gwen/gwenwallpussy01.png"
        pause 0.03
        repeat

    image gwenwallpussycumslow:
        "Gwen/gwenwallpussycum00.png"
        pause 0.08
        "Gwen/gwenwallpussycum01.png"
        pause 0.04
        "Gwen/gwenwallpussycum02.png"
        pause 0.04
        "Gwen/gwenwallpussycum03.png"
        pause 0.04
        "Gwen/gwenwallpussycum04.png"
        pause 0.04
        "Gwen/gwenwallpussycum05.png"
        pause 0.04
        "Gwen/gwenwallpussycum06.png"
        pause 0.04
        "Gwen/gwenwallpussycum07.png"
        pause 0.04
        "Gwen/gwenwallpussycum08.png"
        pause 0.04
        "Gwen/gwenwallpussycum09.png"
        pause 0.04
        "Gwen/gwenwallpussycum10.png"
        pause 0.06
        "Gwen/gwenwallpussycum09.png"
        pause 0.04
        "Gwen/gwenwallpussycum09.png"
        pause 0.04
        "Gwen/gwenwallpussycum08.png"
        pause 0.04
        "Gwen/gwenwallpussycum07.png"
        pause 0.04
        "Gwen/gwenwallpussycum06.png"
        pause 0.04
        "Gwen/gwenwallpussycum05.png"
        pause 0.04
        "Gwen/gwenwallpussycum04.png"
        pause 0.04
        "Gwen/gwenwallpussycum03.png"
        pause 0.04
        "Gwen/gwenwallpussycum02.png"
        pause 0.04
        "Gwen/gwenwallpussycum01.png"
        pause 0.04
        repeat
    
    image gwenwallpussycumfast:
        "Gwen/gwenwallpussycum00.png"
        pause 0.06
        "Gwen/gwenwallpussycum01.png"
        pause 0.03
        "Gwen/gwenwallpussycum02.png"
        pause 0.03
        "Gwen/gwenwallpussycum03.png"
        pause 0.03
        "Gwen/gwenwallpussycum04.png"
        pause 0.03
        "Gwen/gwenwallpussycum05.png"
        pause 0.03
        "Gwen/gwenwallpussycum06.png"
        pause 0.03
        "Gwen/gwenwallpussycum07.png"
        pause 0.03
        "Gwen/gwenwallpussycum08.png"
        pause 0.03
        "Gwen/gwenwallpussycum09.png"
        pause 0.03
        "Gwen/gwenwallpussycum10.png"
        pause 0.045
        "Gwen/gwenwallpussycum09.png"
        pause 0.03
        "Gwen/gwenwallpussycum09.png"
        pause 0.03
        "Gwen/gwenwallpussycum08.png"
        pause 0.03
        "Gwen/gwenwallpussycum07.png"
        pause 0.03
        "Gwen/gwenwallpussycum06.png"
        pause 0.03
        "Gwen/gwenwallpussycum05.png"
        pause 0.03
        "Gwen/gwenwallpussycum04.png"
        pause 0.03
        "Gwen/gwenwallpussycum03.png"
        pause 0.03
        "Gwen/gwenwallpussycum02.png"
        pause 0.03
        "Gwen/gwenwallpussycum01.png"
        pause 0.03
        repeat

    image amygwenrideslow:
        "Gwen/gwenthreesome00.png"
        pause 0.05
        "Gwen/gwenthreesome01.png"
        pause 0.05
        "Gwen/gwenthreesome02.png"
        pause 0.05
        "Gwen/gwenthreesome03.png"
        pause 0.05
        "Gwen/gwenthreesome04.png"
        pause 0.05
        "Gwen/gwenthreesome05.png"
        pause 0.05
        "Gwen/gwenthreesome06.png"
        pause 0.05
        "Gwen/gwenthreesome07.png"
        pause 0.05
        "Gwen/gwenthreesome08.png"
        pause 0.05
        "Gwen/gwenthreesome09.png"
        pause 0.05
        "Gwen/gwenthreesome10.png"
        pause 0.05
        "Gwen/gwenthreesome11.png"
        pause 0.05
        "Gwen/gwenthreesome12.png"
        pause 0.05
        "Gwen/gwenthreesome13.png"
        pause 0.05
        "Gwen/gwenthreesome14.png"
        pause 0.05
        "Gwen/gwenthreesome15.png"
        pause 0.05
        "Gwen/gwenthreesome16.png"
        pause 0.05
        "Gwen/gwenthreesome17.png"
        pause 0.05
        "Gwen/gwenthreesome18.png"
        pause 0.05
        repeat

    image amygwenridefast:
        "Gwen/gwenthreesome00.png"
        pause 0.03
        "Gwen/gwenthreesome01.png"
        pause 0.03
        "Gwen/gwenthreesome02.png"
        pause 0.03
        "Gwen/gwenthreesome03.png"
        pause 0.03
        "Gwen/gwenthreesome04.png"
        pause 0.03
        "Gwen/gwenthreesome05.png"
        pause 0.03
        "Gwen/gwenthreesome06.png"
        pause 0.03
        "Gwen/gwenthreesome07.png"
        pause 0.03
        "Gwen/gwenthreesome08.png"
        pause 0.03
        "Gwen/gwenthreesome09.png"
        pause 0.03
        "Gwen/gwenthreesome10.png"
        pause 0.03
        "Gwen/gwenthreesome11.png"
        pause 0.03
        "Gwen/gwenthreesome12.png"
        pause 0.03
        "Gwen/gwenthreesome13.png"
        pause 0.03
        "Gwen/gwenthreesome14.png"
        pause 0.03
        "Gwen/gwenthreesome15.png"
        pause 0.03
        "Gwen/gwenthreesome16.png"
        pause 0.03
        "Gwen/gwenthreesome17.png"
        pause 0.03
        "Gwen/gwenthreesome18.png"
        pause 0.03
        repeat

    image amygwenanalslow:
        "Gwen/gwenthreesomeanal00.png"
        pause 0.05
        "Gwen/gwenthreesomeanal01.png"
        pause 0.05
        "Gwen/gwenthreesomeanal02.png"
        pause 0.05
        "Gwen/gwenthreesomeanal03.png"
        pause 0.05
        "Gwen/gwenthreesomeanal04.png"
        pause 0.05
        "Gwen/gwenthreesomeanal05.png"
        pause 0.05
        "Gwen/gwenthreesomeanal06.png"
        pause 0.05
        "Gwen/gwenthreesomeanal07.png"
        pause 0.05
        "Gwen/gwenthreesomeanal08.png"
        pause 0.05
        "Gwen/gwenthreesomeanal09.png"
        pause 0.05
        "Gwen/gwenthreesomeanal10.png"
        pause 0.05
        "Gwen/gwenthreesomeanal09.png"
        pause 0.05
        "Gwen/gwenthreesomeanal08.png"
        pause 0.05
        "Gwen/gwenthreesomeanal07.png"
        pause 0.05
        "Gwen/gwenthreesomeanal06.png"
        pause 0.05
        "Gwen/gwenthreesomeanal05.png"
        pause 0.05
        "Gwen/gwenthreesomeanal04.png"
        pause 0.05
        "Gwen/gwenthreesomeanal03.png"
        pause 0.05
        "Gwen/gwenthreesomeanal02.png"
        pause 0.05
        "Gwen/gwenthreesomeanal01.png"
        pause 0.05
        repeat

    image amygwenanalfast:
        "Gwen/gwenthreesomeanal00.png"
        pause 0.03
        "Gwen/gwenthreesomeanal01.png"
        pause 0.03
        "Gwen/gwenthreesomeanal02.png"
        pause 0.03
        "Gwen/gwenthreesomeanal03.png"
        pause 0.03
        "Gwen/gwenthreesomeanal04.png"
        pause 0.03
        "Gwen/gwenthreesomeanal05.png"
        pause 0.03
        "Gwen/gwenthreesomeanal06.png"
        pause 0.03
        "Gwen/gwenthreesomeanal07.png"
        pause 0.03
        "Gwen/gwenthreesomeanal08.png"
        pause 0.03
        "Gwen/gwenthreesomeanal09.png"
        pause 0.03
        "Gwen/gwenthreesomeanal10.png"
        pause 0.03
        "Gwen/gwenthreesomeanal09.png"
        pause 0.03
        "Gwen/gwenthreesomeanal08.png"
        pause 0.03
        "Gwen/gwenthreesomeanal07.png"
        pause 0.03
        "Gwen/gwenthreesomeanal06.png"
        pause 0.03
        "Gwen/gwenthreesomeanal05.png"
        pause 0.03
        "Gwen/gwenthreesomeanal04.png"
        pause 0.03
        "Gwen/gwenthreesomeanal03.png"
        pause 0.03
        "Gwen/gwenthreesomeanal02.png"
        pause 0.03
        "Gwen/gwenthreesomeanal01.png"
        pause 0.03
        repeat

    image amygwenanalbslow:
        "Gwen/gwenthreesomeanalb00.png"
        pause 0.05
        "Gwen/gwenthreesomeanalb01.png"
        pause 0.05
        "Gwen/gwenthreesomeanalb02.png"
        pause 0.05
        "Gwen/gwenthreesomeanalb03.png"
        pause 0.05
        "Gwen/gwenthreesomeanalb04.png"
        pause 0.05
        "Gwen/gwenthreesomeanalb05.png"
        pause 0.05
        "Gwen/gwenthreesomeanalb06.png"
        pause 0.05
        "Gwen/gwenthreesomeanalb07.png"
        pause 0.05
        "Gwen/gwenthreesomeanalb08.png"
        pause 0.05
        "Gwen/gwenthreesomeanalb09.png"
        pause 0.05
        "Gwen/gwenthreesomeanalb10.png"
        pause 0.05
        "Gwen/gwenthreesomeanalb09.png"
        pause 0.05
        "Gwen/gwenthreesomeanalb08.png"
        pause 0.05
        "Gwen/gwenthreesomeanalb07.png"
        pause 0.05
        "Gwen/gwenthreesomeanalb06.png"
        pause 0.05
        "Gwen/gwenthreesomeanalb05.png"
        pause 0.05
        "Gwen/gwenthreesomeanalb04.png"
        pause 0.05
        "Gwen/gwenthreesomeanalb03.png"
        pause 0.05
        "Gwen/gwenthreesomeanalb02.png"
        pause 0.05
        "Gwen/gwenthreesomeanalb01.png"
        pause 0.05
        repeat

    image amygwenanalbfast:
        "Gwen/gwenthreesomeanalb00.png"
        pause 0.03
        "Gwen/gwenthreesomeanalb01.png"
        pause 0.03
        "Gwen/gwenthreesomeanalb02.png"
        pause 0.03
        "Gwen/gwenthreesomeanalb03.png"
        pause 0.03
        "Gwen/gwenthreesomeanalb04.png"
        pause 0.03
        "Gwen/gwenthreesomeanalb05.png"
        pause 0.03
        "Gwen/gwenthreesomeanalb06.png"
        pause 0.03
        "Gwen/gwenthreesomeanalb07.png"
        pause 0.03
        "Gwen/gwenthreesomeanalb08.png"
        pause 0.03
        "Gwen/gwenthreesomeanalb09.png"
        pause 0.03
        "Gwen/gwenthreesomeanalb10.png"
        pause 0.03
        "Gwen/gwenthreesomeanalb09.png"
        pause 0.03
        "Gwen/gwenthreesomeanalb08.png"
        pause 0.03
        "Gwen/gwenthreesomeanalb07.png"
        pause 0.03
        "Gwen/gwenthreesomeanalb06.png"
        pause 0.03
        "Gwen/gwenthreesomeanalb05.png"
        pause 0.03
        "Gwen/gwenthreesomeanalb04.png"
        pause 0.03
        "Gwen/gwenthreesomeanalb03.png"
        pause 0.03
        "Gwen/gwenthreesomeanalb02.png"
        pause 0.03
        "Gwen/gwenthreesomeanalb01.png"
        pause 0.03
        repeat
            
    image amygwenfuckslow:
        "Gwen/gwenthreesomefuck00.png"
        pause 0.04
        "Gwen/gwenthreesomefuck01.png"
        pause 0.04
        "Gwen/gwenthreesomefuck02.png"
        pause 0.04
        "Gwen/gwenthreesomefuck03.png"
        pause 0.04
        "Gwen/gwenthreesomefuck04.png"
        pause 0.04
        "Gwen/gwenthreesomefuck05.png"
        pause 0.04
        "Gwen/gwenthreesomefuck06.png"
        pause 0.04
        "Gwen/gwenthreesomefuck07.png"
        pause 0.04
        "Gwen/gwenthreesomefuck08.png"
        pause 0.04
        "Gwen/gwenthreesomefuck09.png"
        pause 0.04
        "Gwen/gwenthreesomefuck10.png"
        pause 0.04
        "Gwen/gwenthreesomefuck11.png"
        pause 0.04
        "Gwen/gwenthreesomefuck12.png"
        pause 0.04
        "Gwen/gwenthreesomefuck11.png"
        pause 0.04
        "Gwen/gwenthreesomefuck10.png"
        pause 0.04
        "Gwen/gwenthreesomefuck09.png"
        pause 0.04
        "Gwen/gwenthreesomefuck08.png"
        pause 0.04
        "Gwen/gwenthreesomefuck07.png"
        pause 0.04
        "Gwen/gwenthreesomefuck06.png"
        pause 0.04
        "Gwen/gwenthreesomefuck05.png"
        pause 0.04
        "Gwen/gwenthreesomefuck04.png"
        pause 0.04
        "Gwen/gwenthreesomefuck03.png"
        pause 0.04
        "Gwen/gwenthreesomefuck02.png"
        pause 0.04
        "Gwen/gwenthreesomefuck01.png"
        pause 0.04
        repeat

    image amygwenfuckfast:
        "Gwen/gwenthreesomefuck00.png"
        pause 0.03
        "Gwen/gwenthreesomefuck01.png"
        pause 0.03
        "Gwen/gwenthreesomefuck02.png"
        pause 0.03
        "Gwen/gwenthreesomefuck03.png"
        pause 0.03
        "Gwen/gwenthreesomefuck04.png"
        pause 0.03
        "Gwen/gwenthreesomefuck05.png"
        pause 0.03
        "Gwen/gwenthreesomefuck06.png"
        pause 0.03
        "Gwen/gwenthreesomefuck07.png"
        pause 0.03
        "Gwen/gwenthreesomefuck08.png"
        pause 0.03
        "Gwen/gwenthreesomefuck09.png"
        pause 0.03
        "Gwen/gwenthreesomefuck10.png"
        pause 0.03
        "Gwen/gwenthreesomefuck11.png"
        pause 0.03
        "Gwen/gwenthreesomefuck12.png"
        pause 0.03
        "Gwen/gwenthreesomefuck11.png"
        pause 0.03
        "Gwen/gwenthreesomefuck10.png"
        pause 0.03
        "Gwen/gwenthreesomefuck09.png"
        pause 0.03
        "Gwen/gwenthreesomefuck08.png"
        pause 0.03
        "Gwen/gwenthreesomefuck07.png"
        pause 0.03
        "Gwen/gwenthreesomefuck06.png"
        pause 0.03
        "Gwen/gwenthreesomefuck05.png"
        pause 0.03
        "Gwen/gwenthreesomefuck04.png"
        pause 0.03
        "Gwen/gwenthreesomefuck03.png"
        pause 0.03
        "Gwen/gwenthreesomefuck02.png"
        pause 0.03
        "Gwen/gwenthreesomefuck01.png"
        pause 0.03
        repeat

    image gwensideslow:
        "Gwen/gwenside00.png"
        pause 0.05
        "Gwen/gwenside01.png"
        pause 0.05
        "Gwen/gwenside02.png"
        pause 0.05
        "Gwen/gwenside03.png"
        pause 0.05
        "Gwen/gwenside04.png"
        pause 0.05
        "Gwen/gwenside05.png"
        pause 0.05
        "Gwen/gwenside06.png"
        pause 0.05
        "Gwen/gwenside07.png"
        pause 0.05
        "Gwen/gwenside08.png"
        pause 0.05
        "Gwen/gwenside09.png"
        pause 0.05
        "Gwen/gwenside10.png"
        pause 0.05
        "Gwen/gwenside11.png"
        pause 0.05
        "Gwen/gwenside12.png"
        pause 0.05
        "Gwen/gwenside11.png"
        pause 0.05
        "Gwen/gwenside10.png"
        pause 0.05
        "Gwen/gwenside09.png"
        pause 0.05
        "Gwen/gwenside08.png"
        pause 0.05
        "Gwen/gwenside07.png"
        pause 0.05
        "Gwen/gwenside06.png"
        pause 0.05
        "Gwen/gwenside05.png"
        pause 0.05
        "Gwen/gwenside04.png"
        pause 0.05
        "Gwen/gwenside03.png"
        pause 0.05
        "Gwen/gwenside02.png"
        pause 0.05
        "Gwen/gwenside01.png"
        pause 0.05
        repeat
            
    image gwensidefast:
        "Gwen/gwenside00.png"
        pause 0.03
        "Gwen/gwenside01.png"
        pause 0.03
        "Gwen/gwenside02.png"
        pause 0.03
        "Gwen/gwenside03.png"
        pause 0.03
        "Gwen/gwenside04.png"
        pause 0.03
        "Gwen/gwenside05.png"
        pause 0.03
        "Gwen/gwenside06.png"
        pause 0.03
        "Gwen/gwenside07.png"
        pause 0.03
        "Gwen/gwenside08.png"
        pause 0.03
        "Gwen/gwenside09.png"
        pause 0.03
        "Gwen/gwenside10.png"
        pause 0.03
        "Gwen/gwenside11.png"
        pause 0.03
        "Gwen/gwenside12.png"
        pause 0.03
        "Gwen/gwenside11.png"
        pause 0.03
        "Gwen/gwenside10.png"
        pause 0.03
        "Gwen/gwenside09.png"
        pause 0.03
        "Gwen/gwenside08.png"
        pause 0.03
        "Gwen/gwenside07.png"
        pause 0.03
        "Gwen/gwenside06.png"
        pause 0.03
        "Gwen/gwenside05.png"
        pause 0.03
        "Gwen/gwenside04.png"
        pause 0.03
        "Gwen/gwenside03.png"
        pause 0.03
        "Gwen/gwenside02.png"
        pause 0.03
        "Gwen/gwenside01.png"
        pause 0.03
        repeat
                        
    image gwenupslow:
        "Gwen/gwenup00.png"
        pause 0.1
        "Gwen/gwenup01.png"
        pause 0.04
        "Gwen/gwenup02.png"
        pause 0.04
        "Gwen/gwenup03.png"
        pause 0.04
        "Gwen/gwenup04.png"
        pause 0.04
        "Gwen/gwenup05.png"
        pause 0.04
        "Gwen/gwenup06.png"
        pause 0.04
        "Gwen/gwenup07.png"
        pause 0.04
        "Gwen/gwenup08.png"
        pause 0.04
        "Gwen/gwenup09.png"
        pause 0.04
        "Gwen/gwenup10.png"
        pause 0.04
        "Gwen/gwenup09.png"
        pause 0.04
        "Gwen/gwenup08.png"
        pause 0.04
        "Gwen/gwenup07.png"
        pause 0.04
        "Gwen/gwenup06.png"
        pause 0.04
        "Gwen/gwenup05.png"
        pause 0.04
        "Gwen/gwenup04.png"
        pause 0.04
        "Gwen/gwenup03.png"
        pause 0.04
        "Gwen/gwenup02.png"
        pause 0.04
        "Gwen/gwenup01.png"
        pause 0.04
        repeat
            
    image gwenupfast:
        "Gwen/gwenup00.png"
        pause 0.08
        "Gwen/gwenup01.png"
        pause 0.03
        "Gwen/gwenup02.png"
        pause 0.03
        "Gwen/gwenup03.png"
        pause 0.03
        "Gwen/gwenup04.png"
        pause 0.03
        "Gwen/gwenup05.png"
        pause 0.03
        "Gwen/gwenup06.png"
        pause 0.03
        "Gwen/gwenup07.png"
        pause 0.03
        "Gwen/gwenup08.png"
        pause 0.03
        "Gwen/gwenup09.png"
        pause 0.03
        "Gwen/gwenup10.png"
        pause 0.03
        "Gwen/gwenup09.png"
        pause 0.03
        "Gwen/gwenup08.png"
        pause 0.03
        "Gwen/gwenup07.png"
        pause 0.03
        "Gwen/gwenup06.png"
        pause 0.03
        "Gwen/gwenup05.png"
        pause 0.03
        "Gwen/gwenup04.png"
        pause 0.03
        "Gwen/gwenup03.png"
        pause 0.03
        "Gwen/gwenup02.png"
        pause 0.03
        "Gwen/gwenup01.png"
        pause 0.03
        repeat

    image gwenuppovslow:
        "Gwen/gwenuppov00.png"
        pause 0.1
        "Gwen/gwenuppov01.png"
        pause 0.04
        "Gwen/gwenuppov02.png"
        pause 0.04
        "Gwen/gwenuppov03.png"
        pause 0.04
        "Gwen/gwenuppov04.png"
        pause 0.04
        "Gwen/gwenuppov05.png"
        pause 0.04
        "Gwen/gwenuppov06.png"
        pause 0.04
        "Gwen/gwenuppov07.png"
        pause 0.04
        "Gwen/gwenuppov08.png"
        pause 0.04
        "Gwen/gwenuppov09.png"
        pause 0.04
        "Gwen/gwenuppov10.png"
        pause 0.04
        "Gwen/gwenuppov09.png"
        pause 0.04
        "Gwen/gwenuppov08.png"
        pause 0.04
        "Gwen/gwenuppov07.png"
        pause 0.04
        "Gwen/gwenuppov06.png"
        pause 0.04
        "Gwen/gwenuppov05.png"
        pause 0.04
        "Gwen/gwenuppov04.png"
        pause 0.04
        "Gwen/gwenuppov03.png"
        pause 0.04
        "Gwen/gwenuppov02.png"
        pause 0.04
        "Gwen/gwenuppov01.png"
        pause 0.04
        repeat
            
    image gwenuppovfast:
        "Gwen/gwenuppov00.png"
        pause 0.08
        "Gwen/gwenuppov01.png"
        pause 0.03
        "Gwen/gwenuppov02.png"
        pause 0.03
        "Gwen/gwenuppov03.png"
        pause 0.03
        "Gwen/gwenuppov04.png"
        pause 0.03
        "Gwen/gwenuppov05.png"
        pause 0.03
        "Gwen/gwenuppov06.png"
        pause 0.03
        "Gwen/gwenuppov07.png"
        pause 0.03
        "Gwen/gwenuppov08.png"
        pause 0.03
        "Gwen/gwenuppov09.png"
        pause 0.03
        "Gwen/gwenuppov10.png"
        pause 0.03
        "Gwen/gwenuppov09.png"
        pause 0.03
        "Gwen/gwenuppov08.png"
        pause 0.03
        "Gwen/gwenuppov07.png"
        pause 0.03
        "Gwen/gwenuppov06.png"
        pause 0.03
        "Gwen/gwenuppov05.png"
        pause 0.03
        "Gwen/gwenuppov04.png"
        pause 0.03
        "Gwen/gwenuppov03.png"
        pause 0.03
        "Gwen/gwenuppov02.png"
        pause 0.03
        "Gwen/gwenuppov01.png"
        pause 0.03
        repeat

    image debrawank:
        "Science/debrawank00.png"
        pause 0.04
        "Science/debrawank01.png"
        pause 0.04
        "Science/debrawank02.png"
        pause 0.04
        "Science/debrawank03.png"
        pause 0.04
        "Science/debrawank04.png"
        pause 0.04
        "Science/debrawank05.png"
        pause 0.04
        "Science/debrawank06.png"
        pause 0.04
        "Science/debrawank07.png"
        pause 0.04
        "Science/debrawank08.png"
        pause 0.04
        "Science/debrawank09.png"
        pause 0.04
        "Science/debrawank10.png"
        pause 0.04
        "Science/debrawank09.png"
        pause 0.03
        "Science/debrawank08.png"
        pause 0.03
        "Science/debrawank07.png"
        pause 0.03
        "Science/debrawank06.png"
        pause 0.03
        "Science/debrawank05.png"
        pause 0.03
        "Science/debrawank04.png"
        pause 0.03
        "Science/debrawank03.png"
        pause 0.03
        "Science/debrawank02.png"
        pause 0.03
        "Science/debrawank01.png"
        pause 0.03
        repeat

    image annamouthslow:
        "Explore02/annamouth00.png"
        pause 0.1
        "Explore02/annamouth01.png"
        pause 0.04
        "Explore02/annamouth02.png"
        pause 0.04
        "Explore02/annamouth03.png"
        pause 0.04
        "Explore02/annamouth04.png"
        pause 0.04
        "Explore02/annamouth05.png"
        pause 0.04
        "Explore02/annamouth06.png"
        pause 0.04
        "Explore02/annamouth07.png"
        pause 0.04
        "Explore02/annamouth08.png"
        pause 0.04
        "Explore02/annamouth09.png"
        pause 0.04
        "Explore02/annamouth08.png"
        pause 0.04
        "Explore02/annamouth07.png"
        pause 0.04
        "Explore02/annamouth06.png"
        pause 0.04
        "Explore02/annamouth05.png"
        pause 0.04
        "Explore02/annamouth04.png"
        pause 0.04
        "Explore02/annamouth03.png"
        pause 0.04
        "Explore02/annamouth02.png"
        pause 0.04
        "Explore02/annamouth01.png"
        pause 0.04
        repeat
  
    image annamouthfast:
        "Explore02/annamouth00.png"
        pause 0.08
        "Explore02/annamouth01.png"
        pause 0.03
        "Explore02/annamouth02.png"
        pause 0.03
        "Explore02/annamouth03.png"
        pause 0.03
        "Explore02/annamouth04.png"
        pause 0.03
        "Explore02/annamouth05.png"
        pause 0.03
        "Explore02/annamouth06.png"
        pause 0.03
        "Explore02/annamouth07.png"
        pause 0.03
        "Explore02/annamouth08.png"
        pause 0.03
        "Explore02/annamouth09.png"
        pause 0.03
        "Explore02/annamouth08.png"
        pause 0.03
        "Explore02/annamouth07.png"
        pause 0.03
        "Explore02/annamouth06.png"
        pause 0.03
        "Explore02/annamouth05.png"
        pause 0.03
        "Explore02/annamouth04.png"
        pause 0.03
        "Explore02/annamouth03.png"
        pause 0.03
        "Explore02/annamouth02.png"
        pause 0.03
        "Explore02/annamouth01.png"
        pause 0.03
        repeat

    image amygwenfistslow:
        "Gwen/gwenfist00.png"
        pause 0.08
        "Gwen/gwenfist01.png"
        pause 0.04
        "Gwen/gwenfist02.png"
        pause 0.04
        "Gwen/gwenfist03.png"
        pause 0.04
        "Gwen/gwenfist04.png"
        pause 0.04
        "Gwen/gwenfist05.png"
        pause 0.04
        "Gwen/gwenfist06.png"
        pause 0.04
        "Gwen/gwenfist07.png"
        pause 0.04
        "Gwen/gwenfist08.png"
        pause 0.04
        "Gwen/gwenfist09.png"
        pause 0.04
        "Gwen/gwenfist08.png"
        pause 0.04
        "Gwen/gwenfist07.png"
        pause 0.04
        "Gwen/gwenfist06.png"
        pause 0.04
        "Gwen/gwenfist05.png"
        pause 0.04
        "Gwen/gwenfist04.png"
        pause 0.04
        "Gwen/gwenfist03.png"
        pause 0.04
        "Gwen/gwenfist02.png"
        pause 0.04
        "Gwen/gwenfist01.png"
        pause 0.04
        repeat

    image amygwenfistfast:
        "Gwen/gwenfist00.png"
        pause 0.06
        "Gwen/gwenfist01.png"
        pause 0.03
        "Gwen/gwenfist02.png"
        pause 0.03
        "Gwen/gwenfist03.png"
        pause 0.03
        "Gwen/gwenfist04.png"
        pause 0.03
        "Gwen/gwenfist05.png"
        pause 0.03
        "Gwen/gwenfist06.png"
        pause 0.03
        "Gwen/gwenfist07.png"
        pause 0.03
        "Gwen/gwenfist08.png"
        pause 0.03
        "Gwen/gwenfist09.png"
        pause 0.03
        "Gwen/gwenfist08.png"
        pause 0.03
        "Gwen/gwenfist07.png"
        pause 0.03
        "Gwen/gwenfist06.png"
        pause 0.03
        "Gwen/gwenfist05.png"
        pause 0.03
        "Gwen/gwenfist04.png"
        pause 0.03
        "Gwen/gwenfist03.png"
        pause 0.03
        "Gwen/gwenfist02.png"
        pause 0.03
        "Gwen/gwenfist01.png"
        pause 0.03
        repeat

    image nancypregslow:
        "v06/nancyimpregnate00.jpg"
        pause 0.08
        "v06/nancyimpregnate01.jpg"
        pause 0.04
        "v06/nancyimpregnate02.jpg"
        pause 0.04
        "v06/nancyimpregnate03.jpg"
        pause 0.04
        "v06/nancyimpregnate04.jpg"
        pause 0.04
        "v06/nancyimpregnate05.jpg"
        pause 0.04
        "v06/nancyimpregnate06.jpg"
        pause 0.04
        "v06/nancyimpregnate07.jpg"
        pause 0.04
        "v06/nancyimpregnate08.jpg"
        pause 0.04
        "v06/nancyimpregnate09.jpg"
        pause 0.04
        "v06/nancyimpregnate08.jpg"
        pause 0.04
        "v06/nancyimpregnate07.jpg"
        pause 0.04
        "v06/nancyimpregnate06.jpg"
        pause 0.04
        "v06/nancyimpregnate05.jpg"
        pause 0.04
        "v06/nancyimpregnate04.jpg"
        pause 0.04
        "v06/nancyimpregnate03.jpg"
        pause 0.04
        "v06/nancyimpregnate02.jpg"
        pause 0.04
        "v06/nancyimpregnate01.jpg"
        pause 0.04
        repeat

    image nancypregfast:
        "v06/nancyimpregnate00.jpg"
        pause 0.06
        "v06/nancyimpregnate01.jpg"
        pause 0.03
        "v06/nancyimpregnate02.jpg"
        pause 0.03
        "v06/nancyimpregnate03.jpg"
        pause 0.03
        "v06/nancyimpregnate04.jpg"
        pause 0.03
        "v06/nancyimpregnate05.jpg"
        pause 0.03
        "v06/nancyimpregnate06.jpg"
        pause 0.03
        "v06/nancyimpregnate07.jpg"
        pause 0.03
        "v06/nancyimpregnate08.jpg"
        pause 0.03
        "v06/nancyimpregnate09.jpg"
        pause 0.03
        "v06/nancyimpregnate08.jpg"
        pause 0.03
        "v06/nancyimpregnate07.jpg"
        pause 0.03
        "v06/nancyimpregnate06.jpg"
        pause 0.03
        "v06/nancyimpregnate05.jpg"
        pause 0.03
        "v06/nancyimpregnate04.jpg"
        pause 0.03
        "v06/nancyimpregnate03.jpg"
        pause 0.03
        "v06/nancyimpregnate02.jpg"
        pause 0.03
        "v06/nancyimpregnate01.jpg"
        pause 0.03
        repeat

    image nancyprepregslow:
        "v06/preimpregnate00.jpg"
        pause 0.06
        "v06/preimpregnate01.jpg"
        pause 0.04
        "v06/preimpregnate02.jpg"
        pause 0.04
        "v06/preimpregnate03.jpg"
        pause 0.04
        "v06/preimpregnate04.jpg"
        pause 0.04
        "v06/preimpregnate05.jpg"
        pause 0.04
        "v06/preimpregnate06.jpg"
        pause 0.04
        "v06/preimpregnate07.jpg"
        pause 0.04
        "v06/preimpregnate08.jpg"
        pause 0.04
        "v06/preimpregnate09.jpg"
        pause 0.04
        "v06/preimpregnate10.jpg"
        pause 0.06
        "v06/preimpregnate09.jpg"
        pause 0.04
        "v06/preimpregnate08.jpg"
        pause 0.04
        "v06/preimpregnate07.jpg"
        pause 0.04
        "v06/preimpregnate06.jpg"
        pause 0.04
        "v06/preimpregnate05.jpg"
        pause 0.04
        "v06/preimpregnate04.jpg"
        pause 0.04
        "v06/preimpregnate03.jpg"
        pause 0.04
        "v06/preimpregnate02.jpg"
        pause 0.04
        "v06/preimpregnate01.jpg"
        pause 0.04
        repeat
    
    image nancyprepregfast:
        "v06/preimpregnate00.jpg"
        pause 0.05
        "v06/preimpregnate01.jpg"
        pause 0.04
        "v06/preimpregnate02.jpg"
        pause 0.03
        "v06/preimpregnate03.jpg"
        pause 0.03
        "v06/preimpregnate04.jpg"
        pause 0.03
        "v06/preimpregnate05.jpg"
        pause 0.03
        "v06/preimpregnate06.jpg"
        pause 0.03
        "v06/preimpregnate07.jpg"
        pause 0.03
        "v06/preimpregnate08.jpg"
        pause 0.03
        "v06/preimpregnate09.jpg"
        pause 0.03
        "v06/preimpregnate10.jpg"
        pause 0.05
        "v06/preimpregnate09.jpg"
        pause 0.03
        "v06/preimpregnate08.jpg"
        pause 0.03
        "v06/preimpregnate07.jpg"
        pause 0.03
        "v06/preimpregnate06.jpg"
        pause 0.03
        "v06/preimpregnate05.jpg"
        pause 0.03
        "v06/preimpregnate04.jpg"
        pause 0.03
        "v06/preimpregnate03.jpg"
        pause 0.03
        "v06/preimpregnate02.jpg"
        pause 0.03
        "v06/preimpregnate01.jpg"
        pause 0.03
        repeat

    image taylorfuckslow:
        "v06/taylorfuck00.jpg"
        pause 0.06
        "v06/taylorfuck01.jpg"
        pause 0.04
        "v06/taylorfuck02.jpg"
        pause 0.04
        "v06/taylorfuck03.jpg"
        pause 0.04
        "v06/taylorfuck04.jpg"
        pause 0.04
        "v06/taylorfuck05.jpg"
        pause 0.04
        "v06/taylorfuck06.jpg"
        pause 0.04
        "v06/taylorfuck07.jpg"
        pause 0.04
        "v06/taylorfuck08.jpg"
        pause 0.04
        "v06/taylorfuck09.jpg"
        pause 0.04
        "v06/taylorfuck10.jpg"
        pause 0.04
        "v06/taylorfuck11.jpg"
        pause 0.04
        "v06/taylorfuck12.jpg"
        pause 0.06
        "v06/taylorfuck11.jpg"
        pause 0.03
        "v06/taylorfuck10.jpg"
        pause 0.03
        "v06/taylorfuck09.jpg"
        pause 0.03
        "v06/taylorfuck08.jpg"
        pause 0.03
        "v06/taylorfuck07.jpg"
        pause 0.03
        "v06/taylorfuck06.jpg"
        pause 0.03
        "v06/taylorfuck05.jpg"
        pause 0.03
        "v06/taylorfuck04.jpg"
        pause 0.03
        "v06/taylorfuck03.jpg"
        pause 0.03
        "v06/taylorfuck02.jpg"
        pause 0.03
        "v06/taylorfuck01.jpg"
        pause 0.03
        repeat
 
    image taylorfuckfast:
        "v06/taylorfuck00.jpg"
        pause 0.05
        "v06/taylorfuck01.jpg"
        pause 0.03
        "v06/taylorfuck02.jpg"
        pause 0.03
        "v06/taylorfuck03.jpg"
        pause 0.03
        "v06/taylorfuck04.jpg"
        pause 0.03
        "v06/taylorfuck05.jpg"
        pause 0.03
        "v06/taylorfuck06.jpg"
        pause 0.03
        "v06/taylorfuck07.jpg"
        pause 0.03
        "v06/taylorfuck08.jpg"
        pause 0.03
        "v06/taylorfuck09.jpg"
        pause 0.03
        "v06/taylorfuck10.jpg"
        pause 0.03
        "v06/taylorfuck11.jpg"
        pause 0.03
        "v06/taylorfuck12.jpg"
        pause 0.06
        "v06/taylorfuck11.jpg"
        pause 0.025
        "v06/taylorfuck10.jpg"
        pause 0.025
        "v06/taylorfuck09.jpg"
        pause 0.025
        "v06/taylorfuck08.jpg"
        pause 0.025
        "v06/taylorfuck07.jpg"
        pause 0.025
        "v06/taylorfuck06.jpg"
        pause 0.025
        "v06/taylorfuck05.jpg"
        pause 0.025
        "v06/taylorfuck04.jpg"
        pause 0.025
        "v06/taylorfuck03.jpg"
        pause 0.025
        "v06/taylorfuck02.jpg"
        pause 0.025
        "v06/taylorfuck01.jpg"
        pause 0.025
        repeat
            
    image taylorfuckpovslow:
        "v06/taylorfuckpov00.jpg"
        pause 0.06
        "v06/taylorfuckpov01.jpg"
        pause 0.04
        "v06/taylorfuckpov02.jpg"
        pause 0.04
        "v06/taylorfuckpov03.jpg"
        pause 0.04
        "v06/taylorfuckpov04.jpg"
        pause 0.04
        "v06/taylorfuckpov05.jpg"
        pause 0.04
        "v06/taylorfuckpov06.jpg"
        pause 0.04
        "v06/taylorfuckpov07.jpg"
        pause 0.04
        "v06/taylorfuckpov08.jpg"
        pause 0.04
        "v06/taylorfuckpov09.jpg"
        pause 0.04
        "v06/taylorfuckpov10.jpg"
        pause 0.04
        "v06/taylorfuckpov11.jpg"
        pause 0.04
        "v06/taylorfuckpov12.jpg"
        pause 0.06
        "v06/taylorfuckpov11.jpg"
        pause 0.03
        "v06/taylorfuckpov10.jpg"
        pause 0.03
        "v06/taylorfuckpov09.jpg"
        pause 0.03
        "v06/taylorfuckpov08.jpg"
        pause 0.03
        "v06/taylorfuckpov07.jpg"
        pause 0.03
        "v06/taylorfuckpov06.jpg"
        pause 0.03
        "v06/taylorfuckpov05.jpg"
        pause 0.03
        "v06/taylorfuckpov04.jpg"
        pause 0.03
        "v06/taylorfuckpov03.jpg"
        pause 0.03
        "v06/taylorfuckpov02.jpg"
        pause 0.03
        "v06/taylorfuckpov01.jpg"
        pause 0.03
        repeat
 
    image taylorfuckpovfast:
        "v06/taylorfuckpov00.jpg"
        pause 0.05
        "v06/taylorfuckpov01.jpg"
        pause 0.03
        "v06/taylorfuckpov02.jpg"
        pause 0.03
        "v06/taylorfuckpov03.jpg"
        pause 0.03
        "v06/taylorfuckpov04.jpg"
        pause 0.03
        "v06/taylorfuckpov05.jpg"
        pause 0.03
        "v06/taylorfuckpov06.jpg"
        pause 0.03
        "v06/taylorfuckpov07.jpg"
        pause 0.03
        "v06/taylorfuckpov08.jpg"
        pause 0.03
        "v06/taylorfuckpov09.jpg"
        pause 0.03
        "v06/taylorfuckpov10.jpg"
        pause 0.03
        "v06/taylorfuckpov11.jpg"
        pause 0.03
        "v06/taylorfuckpov12.jpg"
        pause 0.06
        "v06/taylorfuckpov11.jpg"
        pause 0.025
        "v06/taylorfuckpov10.jpg"
        pause 0.025
        "v06/taylorfuckpov09.jpg"
        pause 0.025
        "v06/taylorfuckpov08.jpg"
        pause 0.025
        "v06/taylorfuckpov07.jpg"
        pause 0.025
        "v06/taylorfuckpov06.jpg"
        pause 0.025
        "v06/taylorfuckpov05.jpg"
        pause 0.025
        "v06/taylorfuckpov04.jpg"
        pause 0.025
        "v06/taylorfuckpov03.jpg"
        pause 0.025
        "v06/taylorfuckpov02.jpg"
        pause 0.025
        "v06/taylorfuckpov01.jpg"
        pause 0.025
        repeat
            
    image amypregnantslow:
        "v06/amyimpregnate00.png"
        pause 0.06
        "v06/amyimpregnate01.png"
        pause 0.04
        "v06/amyimpregnate02.png"
        pause 0.04
        "v06/amyimpregnate03.png"
        pause 0.04
        "v06/amyimpregnate04.png"
        pause 0.04
        "v06/amyimpregnate05.png"
        pause 0.04
        "v06/amyimpregnate06.png"
        pause 0.04
        "v06/amyimpregnate07.png"
        pause 0.04
        "v06/amyimpregnate08.png"
        pause 0.04
        "v06/amyimpregnate09.png"
        pause 0.04
        "v06/amyimpregnate10.png"
        pause 0.06
        "v06/amyimpregnate09.png"
        pause 0.03
        "v06/amyimpregnate08.png"
        pause 0.03
        "v06/amyimpregnate07.png"
        pause 0.03
        "v06/amyimpregnate06.png"
        pause 0.03
        "v06/amyimpregnate05.png"
        pause 0.03
        "v06/amyimpregnate04.png"
        pause 0.03
        "v06/amyimpregnate03.png"
        pause 0.03
        "v06/amyimpregnate02.png"
        pause 0.03
        "v06/amyimpregnate01.png"
        pause 0.03
        repeat
            
    image amypregnantfast:
        "v06/amyimpregnate00.png"
        pause 0.05
        "v06/amyimpregnate01.png"
        pause 0.03
        "v06/amyimpregnate02.png"
        pause 0.03
        "v06/amyimpregnate03.png"
        pause 0.03
        "v06/amyimpregnate04.png"
        pause 0.03
        "v06/amyimpregnate05.png"
        pause 0.03
        "v06/amyimpregnate06.png"
        pause 0.03
        "v06/amyimpregnate07.png"
        pause 0.03
        "v06/amyimpregnate08.png"
        pause 0.03
        "v06/amyimpregnate09.png"
        pause 0.03
        "v06/amyimpregnate10.png"
        pause 0.06
        "v06/amyimpregnate09.png"
        pause 0.025
        "v06/amyimpregnate08.png"
        pause 0.025
        "v06/amyimpregnate07.png"
        pause 0.025
        "v06/amyimpregnate06.png"
        pause 0.025
        "v06/amyimpregnate05.png"
        pause 0.025
        "v06/amyimpregnate04.png"
        pause 0.025
        "v06/amyimpregnate03.png"
        pause 0.025
        "v06/amyimpregnate02.png"
        pause 0.025
        "v06/amyimpregnate01.png"
        pause 0.025
        repeat
            
    image amypregnantsceneslow:
        "v06/amypregnantscene00.png"
        pause 0.06
        "v06/amypregnantscene01.png"
        pause 0.04
        "v06/amypregnantscene02.png"
        pause 0.04
        "v06/amypregnantscene03.png"
        pause 0.04
        "v06/amypregnantscene04.png"
        pause 0.04
        "v06/amypregnantscene05.png"
        pause 0.04
        "v06/amypregnantscene06.png"
        pause 0.04
        "v06/amypregnantscene07.png"
        pause 0.04
        "v06/amypregnantscene08.png"
        pause 0.04
        "v06/amypregnantscene09.png"
        pause 0.04
        "v06/amypregnantscene10.png"
        pause 0.06
        "v06/amypregnantscene09.png"
        pause 0.03
        "v06/amypregnantscene08.png"
        pause 0.03
        "v06/amypregnantscene07.png"
        pause 0.03
        "v06/amypregnantscene06.png"
        pause 0.03
        "v06/amypregnantscene05.png"
        pause 0.03
        "v06/amypregnantscene04.png"
        pause 0.03
        "v06/amypregnantscene03.png"
        pause 0.03
        "v06/amypregnantscene02.png"
        pause 0.03
        "v06/amypregnantscene01.png"
        pause 0.03
        repeat
            
    image amypregnantscenefast:
        "v06/amypregnantscene00.png"
        pause 0.05
        "v06/amypregnantscene01.png"
        pause 0.03
        "v06/amypregnantscene02.png"
        pause 0.03
        "v06/amypregnantscene03.png"
        pause 0.03
        "v06/amypregnantscene04.png"
        pause 0.03
        "v06/amypregnantscene05.png"
        pause 0.03
        "v06/amypregnantscene06.png"
        pause 0.03
        "v06/amypregnantscene07.png"
        pause 0.03
        "v06/amypregnantscene08.png"
        pause 0.03
        "v06/amypregnantscene09.png"
        pause 0.03
        "v06/amypregnantscene10.png"
        pause 0.06
        "v06/amypregnantscene09.png"
        pause 0.025
        "v06/amypregnantscene08.png"
        pause 0.025
        "v06/amypregnantscene07.png"
        pause 0.025
        "v06/amypregnantscene06.png"
        pause 0.025
        "v06/amypregnantscene05.png"
        pause 0.025
        "v06/amypregnantscene04.png"
        pause 0.025
        "v06/amypregnantscene03.png"
        pause 0.025
        "v06/amypregnantscene02.png"
        pause 0.025
        "v06/amypregnantscene01.png"
        pause 0.025
        repeat
            
    image theresafuckslow:
        "v06/theresafuck00.png"
        pause 0.06
        "v06/theresafuck01.png"
        pause 0.04
        "v06/theresafuck02.png"
        pause 0.04
        "v06/theresafuck03.png"
        pause 0.04
        "v06/theresafuck04.png"
        pause 0.04
        "v06/theresafuck05.png"
        pause 0.04
        "v06/theresafuck06.png"
        pause 0.04
        "v06/theresafuck07.png"
        pause 0.04
        "v06/theresafuck08.png"
        pause 0.04
        "v06/theresafuck09.png"
        pause 0.04
        "v06/theresafuck10.png"
        pause 0.06
        "v06/theresafuck09.png"
        pause 0.03
        "v06/theresafuck08.png"
        pause 0.03
        "v06/theresafuck07.png"
        pause 0.03
        "v06/theresafuck06.png"
        pause 0.03
        "v06/theresafuck05.png"
        pause 0.03
        "v06/theresafuck04.png"
        pause 0.03
        "v06/theresafuck03.png"
        pause 0.03
        "v06/theresafuck02.png"
        pause 0.03
        "v06/theresafuck01.png"
        pause 0.03
        repeat
            
    image theresafuckfast:
        "v06/theresafuck00.png"
        pause 0.05
        "v06/theresafuck01.png"
        pause 0.03
        "v06/theresafuck02.png"
        pause 0.03
        "v06/theresafuck03.png"
        pause 0.03
        "v06/theresafuck04.png"
        pause 0.03
        "v06/theresafuck05.png"
        pause 0.03
        "v06/theresafuck06.png"
        pause 0.03
        "v06/theresafuck07.png"
        pause 0.03
        "v06/theresafuck08.png"
        pause 0.03
        "v06/theresafuck09.png"
        pause 0.03
        "v06/theresafuck10.png"
        pause 0.06
        "v06/theresafuck09.png"
        pause 0.025
        "v06/theresafuck08.png"
        pause 0.025
        "v06/theresafuck07.png"
        pause 0.025
        "v06/theresafuck06.png"
        pause 0.025
        "v06/theresafuck05.png"
        pause 0.025
        "v06/theresafuck04.png"
        pause 0.025
        "v06/theresafuck03.png"
        pause 0.025
        "v06/theresafuck02.png"
        pause 0.025
        "v06/theresafuck01.png"
        pause 0.025
        repeat
            
    image theresafuckpovslow:
        "v06/theresafuckpov00.png"
        pause 0.06
        "v06/theresafuckpov01.png"
        pause 0.04
        "v06/theresafuckpov02.png"
        pause 0.04
        "v06/theresafuckpov03.png"
        pause 0.04
        "v06/theresafuckpov04.png"
        pause 0.04
        "v06/theresafuckpov05.png"
        pause 0.04
        "v06/theresafuckpov06.png"
        pause 0.04
        "v06/theresafuckpov07.png"
        pause 0.04
        "v06/theresafuckpov08.png"
        pause 0.04
        "v06/theresafuckpov09.png"
        pause 0.04
        "v06/theresafuckpov10.png"
        pause 0.06
        "v06/theresafuckpov09.png"
        pause 0.03
        "v06/theresafuckpov08.png"
        pause 0.03
        "v06/theresafuckpov07.png"
        pause 0.03
        "v06/theresafuckpov06.png"
        pause 0.03
        "v06/theresafuckpov05.png"
        pause 0.03
        "v06/theresafuckpov04.png"
        pause 0.03
        "v06/theresafuckpov03.png"
        pause 0.03
        "v06/theresafuckpov02.png"
        pause 0.03
        "v06/theresafuckpov01.png"
        pause 0.03
        repeat
            
    image theresafuckpovfast:
        "v06/theresafuckpov00.png"
        pause 0.05
        "v06/theresafuckpov01.png"
        pause 0.03
        "v06/theresafuckpov02.png"
        pause 0.03
        "v06/theresafuckpov03.png"
        pause 0.03
        "v06/theresafuckpov04.png"
        pause 0.03
        "v06/theresafuckpov05.png"
        pause 0.03
        "v06/theresafuckpov06.png"
        pause 0.03
        "v06/theresafuckpov07.png"
        pause 0.03
        "v06/theresafuckpov08.png"
        pause 0.03
        "v06/theresafuckpov09.png"
        pause 0.03
        "v06/theresafuckpov10.png"
        pause 0.06
        "v06/theresafuckpov09.png"
        pause 0.025
        "v06/theresafuckpov08.png"
        pause 0.025
        "v06/theresafuckpov07.png"
        pause 0.025
        "v06/theresafuckpov06.png"
        pause 0.025
        "v06/theresafuckpov05.png"
        pause 0.025
        "v06/theresafuckpov04.png"
        pause 0.025
        "v06/theresafuckpov03.png"
        pause 0.025
        "v06/theresafuckpov02.png"
        pause 0.025
        "v06/theresafuckpov01.png"
        pause 0.025
        repeat
            
    image maryfuckslow:
        "v06/maryfuck00.png"
        pause 0.06
        "v06/maryfuck01.png"
        pause 0.04
        "v06/maryfuck02.png"
        pause 0.04
        "v06/maryfuck03.png"
        pause 0.04
        "v06/maryfuck04.png"
        pause 0.04
        "v06/maryfuck05.png"
        pause 0.04
        "v06/maryfuck06.png"
        pause 0.04
        "v06/maryfuck07.png"
        pause 0.04
        "v06/maryfuck08.png"
        pause 0.04
        "v06/maryfuck09.png"
        pause 0.04
        "v06/maryfuck10.png"
        pause 0.06
        "v06/maryfuck09.png"
        pause 0.03
        "v06/maryfuck08.png"
        pause 0.03
        "v06/maryfuck07.png"
        pause 0.03
        "v06/maryfuck06.png"
        pause 0.03
        "v06/maryfuck05.png"
        pause 0.03
        "v06/maryfuck04.png"
        pause 0.03
        "v06/maryfuck03.png"
        pause 0.03
        "v06/maryfuck02.png"
        pause 0.03
        "v06/maryfuck01.png"
        pause 0.03
        repeat
            
    image maryfuckfast:
        "v06/maryfuck00.png"
        pause 0.05
        "v06/maryfuck01.png"
        pause 0.03
        "v06/maryfuck02.png"
        pause 0.03
        "v06/maryfuck03.png"
        pause 0.03
        "v06/maryfuck04.png"
        pause 0.03
        "v06/maryfuck05.png"
        pause 0.03
        "v06/maryfuck06.png"
        pause 0.03
        "v06/maryfuck07.png"
        pause 0.03
        "v06/maryfuck08.png"
        pause 0.03
        "v06/maryfuck09.png"
        pause 0.03
        "v06/maryfuck10.png"
        pause 0.06
        "v06/maryfuck09.png"
        pause 0.025
        "v06/maryfuck08.png"
        pause 0.025
        "v06/maryfuck07.png"
        pause 0.025
        "v06/maryfuck06.png"
        pause 0.025
        "v06/maryfuck05.png"
        pause 0.025
        "v06/maryfuck04.png"
        pause 0.025
        "v06/maryfuck03.png"
        pause 0.025
        "v06/maryfuck02.png"
        pause 0.025
        "v06/maryfuck01.png"
        pause 0.025
        repeat
    
    image maryfuckpovslow:
        "v06/maryfuckpov01.png"
        pause 0.04
        "v06/maryfuckpov02.png"
        pause 0.04
        "v06/maryfuckpov03.png"
        pause 0.04
        "v06/maryfuckpov04.png"
        pause 0.04
        "v06/maryfuckpov05.png"
        pause 0.04
        "v06/maryfuckpov06.png"
        pause 0.04
        "v06/maryfuckpov07.png"
        pause 0.04
        "v06/maryfuckpov08.png"
        pause 0.04
        "v06/maryfuckpov09.png"
        pause 0.04
        "v06/maryfuckpov10.png"
        pause 0.06
        "v06/maryfuckpov09.png"
        pause 0.03
        "v06/maryfuckpov08.png"
        pause 0.03
        "v06/maryfuckpov07.png"
        pause 0.03
        "v06/maryfuckpov06.png"
        pause 0.03
        "v06/maryfuckpov05.png"
        pause 0.03
        "v06/maryfuckpov04.png"
        pause 0.03
        "v06/maryfuckpov03.png"
        pause 0.03
        "v06/maryfuckpov02.png"
        pause 0.03
        repeat
            
    image maryfuckpovfast:
        "v06/maryfuckpov01.png"
        pause 0.03
        "v06/maryfuckpov02.png"
        pause 0.03
        "v06/maryfuckpov03.png"
        pause 0.03
        "v06/maryfuckpov04.png"
        pause 0.03
        "v06/maryfuckpov05.png"
        pause 0.03
        "v06/maryfuckpov06.png"
        pause 0.03
        "v06/maryfuckpov07.png"
        pause 0.03
        "v06/maryfuckpov08.png"
        pause 0.03
        "v06/maryfuckpov09.png"
        pause 0.03
        "v06/maryfuckpov10.png"
        pause 0.06
        "v06/maryfuckpov09.png"
        pause 0.025
        "v06/maryfuckpov08.png"
        pause 0.025
        "v06/maryfuckpov07.png"
        pause 0.025
        "v06/maryfuckpov06.png"
        pause 0.025
        "v06/maryfuckpov05.png"
        pause 0.025
        "v06/maryfuckpov04.png"
        pause 0.025
        "v06/maryfuckpov03.png"
        pause 0.025
        "v06/maryfuckpov02.png"
        pause 0.025
        repeat
            
    image annafuckslow:
        "v06/annafuck00.png"
        pause 0.06
        "v06/annafuck01.png"
        pause 0.04
        "v06/annafuck02.png"
        pause 0.04
        "v06/annafuck03.png"
        pause 0.04
        "v06/annafuck04.png"
        pause 0.04
        "v06/annafuck05.png"
        pause 0.04
        "v06/annafuck06.png"
        pause 0.04
        "v06/annafuck07.png"
        pause 0.04
        "v06/annafuck08.png"
        pause 0.04
        "v06/annafuck09.png"
        pause 0.04
        "v06/annafuck10.png"
        pause 0.03
        "v06/annafuck11.png"
        pause 0.06
        "v06/annafuck10.png"
        pause 0.03
        "v06/annafuck09.png"
        pause 0.03
        "v06/annafuck08.png"
        pause 0.03
        "v06/annafuck07.png"
        pause 0.03
        "v06/annafuck06.png"
        pause 0.03
        "v06/annafuck05.png"
        pause 0.03
        "v06/annafuck04.png"
        pause 0.03
        "v06/annafuck03.png"
        pause 0.03
        "v06/annafuck02.png"
        pause 0.03
        "v06/annafuck01.png"
        pause 0.03
        repeat
            
    image annafuckfast:
        "v06/annafuck00.png"
        pause 0.05
        "v06/annafuck01.png"
        pause 0.03
        "v06/annafuck02.png"
        pause 0.03
        "v06/annafuck03.png"
        pause 0.03
        "v06/annafuck04.png"
        pause 0.03
        "v06/annafuck05.png"
        pause 0.03
        "v06/annafuck06.png"
        pause 0.03
        "v06/annafuck07.png"
        pause 0.03
        "v06/annafuck08.png"
        pause 0.03
        "v06/annafuck09.png"
        pause 0.03
        "v06/annafuck10.png"
        pause 0.03
        "v06/annafuck11.png"
        pause 0.06
        "v06/annafuck10.png"
        pause 0.025
        "v06/annafuck09.png"
        pause 0.025
        "v06/annafuck08.png"
        pause 0.025
        "v06/annafuck07.png"
        pause 0.025
        "v06/annafuck06.png"
        pause 0.025
        "v06/annafuck05.png"
        pause 0.025
        "v06/annafuck04.png"
        pause 0.025
        "v06/annafuck03.png"
        pause 0.025
        "v06/annafuck02.png"
        pause 0.025
        "v06/annafuck01.png"
        pause 0.025
        repeat
            
    image annafuckpussyslow:
        "v06/annafuckpussy11.png"
        pause 0.06
        "v06/annafuckpussy10.png"
        pause 0.03
        "v06/annafuckpussy09.png"
        pause 0.03
        "v06/annafuckpussy08.png"
        pause 0.03
        "v06/annafuckpussy07.png"
        pause 0.03
        "v06/annafuckpussy06.png"
        pause 0.03
        "v06/annafuckpussy05.png"
        pause 0.03
        "v06/annafuckpussy04.png"
        pause 0.03
        "v06/annafuckpussy03.png"
        pause 0.03
        "v06/annafuckpussy02.png"
        pause 0.03
        "v06/annafuckpussy01.png"
        pause 0.03
        "v06/annafuckpussy00.png"
        pause 0.06
        "v06/annafuckpussy01.png"
        pause 0.04
        "v06/annafuckpussy02.png"
        pause 0.04
        "v06/annafuckpussy03.png"
        pause 0.04
        "v06/annafuckpussy04.png"
        pause 0.04
        "v06/annafuckpussy05.png"
        pause 0.04
        "v06/annafuckpussy06.png"
        pause 0.04
        "v06/annafuckpussy07.png"
        pause 0.04
        "v06/annafuckpussy08.png"
        pause 0.04
        "v06/annafuckpussy09.png"
        pause 0.04
        "v06/annafuckpussy10.png"
        pause 0.03
        repeat
            
    image annafuckpussyfast:
        "v06/annafuckpussy11.png"
        pause 0.06
        "v06/annafuckpussy10.png"
        pause 0.025
        "v06/annafuckpussy09.png"
        pause 0.025
        "v06/annafuckpussy08.png"
        pause 0.025
        "v06/annafuckpussy07.png"
        pause 0.025
        "v06/annafuckpussy06.png"
        pause 0.025
        "v06/annafuckpussy05.png"
        pause 0.025
        "v06/annafuckpussy04.png"
        pause 0.025
        "v06/annafuckpussy03.png"
        pause 0.025
        "v06/annafuckpussy02.png"
        pause 0.025
        "v06/annafuckpussy01.png"
        pause 0.025
        "v06/annafuckpussy00.png"
        pause 0.05
        "v06/annafuckpussy01.png"
        pause 0.03
        "v06/annafuckpussy02.png"
        pause 0.03
        "v06/annafuckpussy03.png"
        pause 0.03
        "v06/annafuckpussy04.png"
        pause 0.03
        "v06/annafuckpussy05.png"
        pause 0.03
        "v06/annafuckpussy06.png"
        pause 0.03
        "v06/annafuckpussy07.png"
        pause 0.03
        "v06/annafuckpussy08.png"
        pause 0.03
        "v06/annafuckpussy09.png"
        pause 0.03
        "v06/annafuckpussy10.png"
        pause 0.03
        repeat
            
    image annafucktopslow:
        "v06/annafucktop00.png"
        pause 0.06
        "v06/annafucktop01.png"
        pause 0.04
        "v06/annafucktop02.png"
        pause 0.04
        "v06/annafucktop03.png"
        pause 0.04
        "v06/annafucktop04.png"
        pause 0.04
        "v06/annafucktop05.png"
        pause 0.04
        "v06/annafucktop06.png"
        pause 0.04
        "v06/annafucktop07.png"
        pause 0.04
        "v06/annafucktop08.png"
        pause 0.04
        "v06/annafucktop09.png"
        pause 0.04
        "v06/annafucktop10.png"
        pause 0.03
        "v06/annafucktop11.png"
        pause 0.06
        "v06/annafucktop10.png"
        pause 0.03
        "v06/annafucktop09.png"
        pause 0.03
        "v06/annafucktop08.png"
        pause 0.03
        "v06/annafucktop07.png"
        pause 0.03
        "v06/annafucktop06.png"
        pause 0.03
        "v06/annafucktop05.png"
        pause 0.03
        "v06/annafucktop04.png"
        pause 0.03
        "v06/annafucktop03.png"
        pause 0.03
        "v06/annafucktop02.png"
        pause 0.03
        "v06/annafucktop01.png"
        pause 0.03
        repeat
            
    image annafucktopfast:
        "v06/annafucktop00.png"
        pause 0.05
        "v06/annafucktop01.png"
        pause 0.03
        "v06/annafucktop02.png"
        pause 0.03
        "v06/annafucktop03.png"
        pause 0.03
        "v06/annafucktop04.png"
        pause 0.03
        "v06/annafucktop05.png"
        pause 0.03
        "v06/annafucktop06.png"
        pause 0.03
        "v06/annafucktop07.png"
        pause 0.03
        "v06/annafucktop08.png"
        pause 0.03
        "v06/annafucktop09.png"
        pause 0.03
        "v06/annafucktop10.png"
        pause 0.03
        "v06/annafucktop11.png"
        pause 0.06
        "v06/annafucktop10.png"
        pause 0.025
        "v06/annafucktop09.png"
        pause 0.025
        "v06/annafucktop08.png"
        pause 0.025
        "v06/annafucktop07.png"
        pause 0.025
        "v06/annafucktop06.png"
        pause 0.025
        "v06/annafucktop05.png"
        pause 0.025
        "v06/annafucktop04.png"
        pause 0.025
        "v06/annafucktop03.png"
        pause 0.025
        "v06/annafucktop02.png"
        pause 0.025
        "v06/annafucktop01.png"
        pause 0.025
        repeat
            
    image zaratitsslow:
        "v06/zaratits00.png"
        pause 0.06
        "v06/zaratits01.png"
        pause 0.03
        "v06/zaratits02.png"
        pause 0.03
        "v06/zaratits03.png"
        pause 0.03
        "v06/zaratits04.png"
        pause 0.03
        "v06/zaratits05.png"
        pause 0.03
        "v06/zaratits06.png"
        pause 0.03
        "v06/zaratits07.png"
        pause 0.03
        "v06/zaratits08.png"
        pause 0.03
        "v06/zaratits09.png"
        pause 0.03
        "v06/zaratits10.png"
        pause 0.06
        "v06/zaratits09.png"
        pause 0.04
        "v06/zaratits08.png"
        pause 0.04
        "v06/zaratits07.png"
        pause 0.04
        "v06/zaratits06.png"
        pause 0.04
        "v06/zaratits05.png"
        pause 0.04
        "v06/zaratits04.png"
        pause 0.04
        "v06/zaratits03.png"
        pause 0.04
        "v06/zaratits02.png"
        pause 0.04
        "v06/zaratits01.png"
        pause 0.04
        repeat
            
    image zaratitsfast:
        "v06/zaratits00.png"
        pause 0.05
        "v06/zaratits01.png"
        pause 0.025
        "v06/zaratits02.png"
        pause 0.025
        "v06/zaratits03.png"
        pause 0.025
        "v06/zaratits04.png"
        pause 0.025
        "v06/zaratits05.png"
        pause 0.025
        "v06/zaratits06.png"
        pause 0.025
        "v06/zaratits07.png"
        pause 0.025
        "v06/zaratits08.png"
        pause 0.025
        "v06/zaratits09.png"
        pause 0.025
        "v06/zaratits10.png"
        pause 0.06
        "v06/zaratits09.png"
        pause 0.03
        "v06/zaratits08.png"
        pause 0.03
        "v06/zaratits07.png"
        pause 0.03
        "v06/zaratits06.png"
        pause 0.03
        "v06/zaratits05.png"
        pause 0.03
        "v06/zaratits04.png"
        pause 0.03
        "v06/zaratits03.png"
        pause 0.03
        "v06/zaratits02.png"
        pause 0.03
        "v06/zaratits01.png"
        pause 0.03
        repeat
            
    image zarapregslow:
        "v06/zarapreg00.png"
        pause 0.06
        "v06/zarapreg01.png"
        pause 0.03
        "v06/zarapreg02.png"
        pause 0.03
        "v06/zarapreg03.png"
        pause 0.03
        "v06/zarapreg04.png"
        pause 0.03
        "v06/zarapreg05.png"
        pause 0.03
        "v06/zarapreg06.png"
        pause 0.03
        "v06/zarapreg07.png"
        pause 0.03
        "v06/zarapreg08.png"
        pause 0.03
        "v06/zarapreg09.png"
        pause 0.03
        "v06/zarapreg10.png"
        pause 0.06
        "v06/zarapreg09.png"
        pause 0.04
        "v06/zarapreg08.png"
        pause 0.04
        "v06/zarapreg07.png"
        pause 0.04
        "v06/zarapreg06.png"
        pause 0.04
        "v06/zarapreg05.png"
        pause 0.04
        "v06/zarapreg04.png"
        pause 0.04
        "v06/zarapreg03.png"
        pause 0.04
        "v06/zarapreg02.png"
        pause 0.04
        "v06/zarapreg01.png"
        pause 0.04
        repeat
            
    image zarapregfast:
        "v06/zarapreg00.png"
        pause 0.05
        "v06/zarapreg01.png"
        pause 0.025
        "v06/zarapreg02.png"
        pause 0.025
        "v06/zarapreg03.png"
        pause 0.025
        "v06/zarapreg04.png"
        pause 0.025
        "v06/zarapreg05.png"
        pause 0.025
        "v06/zarapreg06.png"
        pause 0.025
        "v06/zarapreg07.png"
        pause 0.025
        "v06/zarapreg08.png"
        pause 0.025
        "v06/zarapreg09.png"
        pause 0.025
        "v06/zarapreg10.png"
        pause 0.06
        "v06/zarapreg09.png"
        pause 0.03
        "v06/zarapreg08.png"
        pause 0.03
        "v06/zarapreg07.png"
        pause 0.03
        "v06/zarapreg06.png"
        pause 0.03
        "v06/zarapreg05.png"
        pause 0.03
        "v06/zarapreg04.png"
        pause 0.03
        "v06/zarapreg03.png"
        pause 0.03
        "v06/zarapreg02.png"
        pause 0.03
        "v06/zarapreg01.png"
        pause 0.03
        repeat
            
    image michikopregnantsceneslow:
        "v06/michikoimpreg00.png"
        pause 0.04
        "v06/michikoimpreg01.png"
        pause 0.04
        "v06/michikoimpreg02.png"
        pause 0.04
        "v06/michikoimpreg03.png"
        pause 0.04
        "v06/michikoimpreg04.png"
        pause 0.04
        "v06/michikoimpreg05.png"
        pause 0.04
        "v06/michikoimpreg06.png"
        pause 0.04
        "v06/michikoimpreg07.png"
        pause 0.04
        "v06/michikoimpreg08.png"
        pause 0.04
        "v06/michikoimpreg09.png"
        pause 0.04
        "v06/michikoimpreg10.png"
        pause 0.04
        "v06/michikoimpreg11.png"
        pause 0.04
        "v06/michikoimpreg12.png"
        pause 0.04
        "v06/michikoimpreg13.png"
        pause 0.04
        "v06/michikoimpreg14.png"
        pause 0.04
        "v06/michikoimpreg15.png"
        pause 0.04
        "v06/michikoimpreg16.png"
        pause 0.04
        "v06/michikoimpreg17.png"
        pause 0.04
        "v06/michikoimpreg18.png"
        pause 0.04
        "v06/michikoimpreg19.png"
        pause 0.04
        repeat

    image michikopregnantscenefast:
        "v06/michikoimpreg00.png"
        pause 0.03
        "v06/michikoimpreg01.png"
        pause 0.03
        "v06/michikoimpreg02.png"
        pause 0.03
        "v06/michikoimpreg03.png"
        pause 0.03
        "v06/michikoimpreg04.png"
        pause 0.03
        "v06/michikoimpreg05.png"
        pause 0.03
        "v06/michikoimpreg06.png"
        pause 0.03
        "v06/michikoimpreg07.png"
        pause 0.03
        "v06/michikoimpreg08.png"
        pause 0.03
        "v06/michikoimpreg09.png"
        pause 0.03
        "v06/michikoimpreg10.png"
        pause 0.03
        "v06/michikoimpreg11.png"
        pause 0.03
        "v06/michikoimpreg12.png"
        pause 0.03
        "v06/michikoimpreg13.png"
        pause 0.03
        "v06/michikoimpreg14.png"
        pause 0.03
        "v06/michikoimpreg15.png"
        pause 0.03
        "v06/michikoimpreg16.png"
        pause 0.03
        "v06/michikoimpreg17.png"
        pause 0.03
        "v06/michikoimpreg18.png"
        pause 0.03
        "v06/michikoimpreg19.png"
        pause 0.03
        repeat

    image michikopregnantslow:
        "v06/michikobalance00.png"
        pause 0.04
        "v06/michikobalance01.png"
        pause 0.04
        "v06/michikobalance02.png"
        pause 0.04
        "v06/michikobalance03.png"
        pause 0.04
        "v06/michikobalance04.png"
        pause 0.04
        "v06/michikobalance05.png"
        pause 0.04
        "v06/michikobalance06.png"
        pause 0.04
        "v06/michikobalance07.png"
        pause 0.04
        "v06/michikobalance08.png"
        pause 0.04
        "v06/michikobalance09.png"
        pause 0.04
        "v06/michikobalance10.png"
        pause 0.04
        "v06/michikobalance11.png"
        pause 0.04
        "v06/michikobalance12.png"
        pause 0.04
        "v06/michikobalance13.png"
        pause 0.04
        "v06/michikobalance14.png"
        pause 0.04
        "v06/michikobalance15.png"
        pause 0.04
        "v06/michikobalance16.png"
        pause 0.04
        "v06/michikobalance17.png"
        pause 0.04
        "v06/michikobalance18.png"
        pause 0.04
        "v06/michikobalance19.png"
        pause 0.04
        repeat

    image michikopregnantfast:
        "v06/michikobalance00.png"
        pause 0.03
        "v06/michikobalance01.png"
        pause 0.03
        "v06/michikobalance02.png"
        pause 0.03
        "v06/michikobalance03.png"
        pause 0.03
        "v06/michikobalance04.png"
        pause 0.03
        "v06/michikobalance05.png"
        pause 0.03
        "v06/michikobalance06.png"
        pause 0.03
        "v06/michikobalance07.png"
        pause 0.03
        "v06/michikobalance08.png"
        pause 0.03
        "v06/michikobalance09.png"
        pause 0.03
        "v06/michikobalance10.png"
        pause 0.03
        "v06/michikobalance11.png"
        pause 0.03
        "v06/michikobalance12.png"
        pause 0.03
        "v06/michikobalance13.png"
        pause 0.03
        "v06/michikobalance14.png"
        pause 0.03
        "v06/michikobalance15.png"
        pause 0.03
        "v06/michikobalance16.png"
        pause 0.03
        "v06/michikobalance17.png"
        pause 0.03
        "v06/michikobalance18.png"
        pause 0.03
        "v06/michikobalance19.png"
        pause 0.03
        repeat
        
    image wendyfuckslow:
        "v06/wendyfuck00.jpg"
        pause 0.04
        "v06/wendyfuck01.jpg"
        pause 0.04
        "v06/wendyfuck02.jpg"
        pause 0.04
        "v06/wendyfuck03.jpg"
        pause 0.04
        "v06/wendyfuck04.jpg"
        pause 0.04
        "v06/wendyfuck05.jpg"
        pause 0.04
        "v06/wendyfuck06.jpg"
        pause 0.04
        "v06/wendyfuck07.jpg"
        pause 0.04
        "v06/wendyfuck08.jpg"
        pause 0.04
        "v06/wendyfuck09.jpg"
        pause 0.04
        "v06/wendyfuck10.jpg"
        pause 0.04
        "v06/wendyfuck11.jpg"
        pause 0.04
        "v06/wendyfuck12.jpg"
        pause 0.04
        "v06/wendyfuck13.jpg"
        pause 0.04
        "v06/wendyfuck14.jpg"
        pause 0.04
        "v06/wendyfuck15.jpg"
        pause 0.04
        "v06/wendyfuck16.jpg"
        pause 0.04
        "v06/wendyfuck17.jpg"
        pause 0.04
        "v06/wendyfuck18.jpg"
        pause 0.04
        "v06/wendyfuck19.jpg"
        pause 0.04
        repeat

    image wendyfuckfast:
        "v06/wendyfuck00.jpg"
        pause 0.03
        "v06/wendyfuck01.jpg"
        pause 0.03
        "v06/wendyfuck02.jpg"
        pause 0.03
        "v06/wendyfuck03.jpg"
        pause 0.03
        "v06/wendyfuck04.jpg"
        pause 0.03
        "v06/wendyfuck05.jpg"
        pause 0.03
        "v06/wendyfuck06.jpg"
        pause 0.03
        "v06/wendyfuck07.jpg"
        pause 0.03
        "v06/wendyfuck08.jpg"
        pause 0.03
        "v06/wendyfuck09.jpg"
        pause 0.03
        "v06/wendyfuck10.jpg"
        pause 0.03
        "v06/wendyfuck11.jpg"
        pause 0.03
        "v06/wendyfuck12.jpg"
        pause 0.03
        "v06/wendyfuck13.jpg"
        pause 0.03
        "v06/wendyfuck14.jpg"
        pause 0.03
        "v06/wendyfuck15.jpg"
        pause 0.03
        "v06/wendyfuck16.jpg"
        pause 0.03
        "v06/wendyfuck17.jpg"
        pause 0.03
        "v06/wendyfuck18.jpg"
        pause 0.03
        "v06/wendyfuck19.jpg"
        pause 0.03
        repeat

    image wendyanalslow:
        "v06/wendyanal00.jpg"
        pause 0.04
        "v06/wendyanal01.jpg"
        pause 0.04
        "v06/wendyanal02.jpg"
        pause 0.04
        "v06/wendyanal03.jpg"
        pause 0.04
        "v06/wendyanal04.jpg"
        pause 0.04
        "v06/wendyanal05.jpg"
        pause 0.04
        "v06/wendyanal06.jpg"
        pause 0.04
        "v06/wendyanal07.jpg"
        pause 0.04
        "v06/wendyanal08.jpg"
        pause 0.04
        "v06/wendyanal09.jpg"
        pause 0.04
        "v06/wendyanal10.jpg"
        pause 0.04
        "v06/wendyanal11.jpg"
        pause 0.04
        "v06/wendyanal12.jpg"
        pause 0.04
        "v06/wendyanal13.jpg"
        pause 0.04
        "v06/wendyanal14.jpg"
        pause 0.04
        "v06/wendyanal15.jpg"
        pause 0.04
        "v06/wendyanal16.jpg"
        pause 0.04
        "v06/wendyanal17.jpg"
        pause 0.04
        "v06/wendyanal18.jpg"
        pause 0.04
        "v06/wendyanal19.jpg"
        pause 0.04
        repeat

    image wendyanalfast:
        "v06/wendyanal00.jpg"
        pause 0.03
        "v06/wendyanal01.jpg"
        pause 0.03
        "v06/wendyanal02.jpg"
        pause 0.03
        "v06/wendyanal03.jpg"
        pause 0.03
        "v06/wendyanal04.jpg"
        pause 0.03
        "v06/wendyanal05.jpg"
        pause 0.03
        "v06/wendyanal06.jpg"
        pause 0.03
        "v06/wendyanal07.jpg"
        pause 0.03
        "v06/wendyanal08.jpg"
        pause 0.03
        "v06/wendyanal09.jpg"
        pause 0.03
        "v06/wendyanal10.jpg"
        pause 0.03
        "v06/wendyanal11.jpg"
        pause 0.03
        "v06/wendyanal12.jpg"
        pause 0.03
        "v06/wendyanal13.jpg"
        pause 0.03
        "v06/wendyanal14.jpg"
        pause 0.03
        "v06/wendyanal15.jpg"
        pause 0.03
        "v06/wendyanal16.jpg"
        pause 0.03
        "v06/wendyanal17.jpg"
        pause 0.03
        "v06/wendyanal18.jpg"
        pause 0.03
        "v06/wendyanal19.jpg"
        pause 0.03
        repeat
            
    transform pitfallvine:
        "v06/vine05.png"
        pause .2
        "v06/vine06.png"
        pause .2
        "v06/vine07.png"
        pause .2
        "v06/vine08.png"
        pause .2
        "v06/vine09.png"
        pause .2
        "v06/vine08.png"
        pause .2
        "v06/vine07.png"
        pause .2
        "v06/vine06.png"
        pause .2
        "v06/vine05.png"
        pause .2
        "v06/vine04.png"
        pause .2
        "v06/vine03.png"
        pause .2
        "v06/vine02.png"
        pause .2
        "v06/vine01.png"
        pause .2
        "v06/vine02.png"
        pause .2
        "v06/vine03.png"
        pause .2
        "v06/vine04.png"
        pause .2
        repeat
            
    image pitfallvine02:
        "v06/vine05.png"
        pause .2
        "v06/vine06.png"
        pause .2
        "v06/vine07.png"
        pause .2
        "v06/vine08.png"
        pause .2
        "v06/vine09.png"
        pause .2
        "v06/vine08.png"
        pause .2
        "v06/vine07.png"
        pause .2
        "v06/vine06.png"
        pause .2
        "v06/vine05.png"
        pause .2
        "v06/vine04.png"
        pause .2
        "v06/vine03.png"
        pause .2
        "v06/vine02.png"
        pause .2
        "v06/vine01.png"
        pause .2
        "v06/vine02.png"
        pause .2
        "v06/vine03.png"
        pause .2
        "v06/vine04.png"
        pause .2
        repeat

    image pitfallvine03:
        "v06/vine08.png"
        pause .2
        "v06/vine07.png"
        pause .2
        "v06/vine06.png"
        pause .2
        "v06/vine05.png"
        pause .2
        "v06/vine04.png"
        pause .2
        "v06/vine03.png"
        pause .2
        "v06/vine02.png"
        pause .2
        "v06/vine01.png"
        pause .2
        "v06/vine02.png"
        pause .2
        "v06/vine03.png"
        pause .2
        "v06/vine04.png"
        pause .2
        "v06/vine05.png"
        pause .2
        "v06/vine06.png"
        pause .2
        "v06/vine07.png"
        pause .2
        "v06/vine08.png"
        pause .2
        "v06/vine09.png"
        pause .2
        repeat

    image pitfallvinemc:
        "v06/vine01b.png"
        pause .2
        "v06/vine02b.png"
        pause .2
        "v06/vine03b.png"
        pause .2
        "v06/vine04b.png"
        pause .2
        "v06/vine05b.png"
        pause .2
        "v06/vine06b.png"
        pause .2
        "v06/vine07b.png"
        pause .2
        "v06/vine08b.png"
        pause .2
        "v06/vine09b.png"
        pause .2

    image wendyhandslow:
        "v06/wendyhand00.jpg"
        pause 0.06
        "v06/wendyhand01.jpg"
        pause 0.03
        "v06/wendyhand02.jpg"
        pause 0.03
        "v06/wendyhand03.jpg"
        pause 0.03
        "v06/wendyhand04.jpg"
        pause 0.03
        "v06/wendyhand05.jpg"
        pause 0.03
        "v06/wendyhand06.jpg"
        pause 0.03
        "v06/wendyhand07.jpg"
        pause 0.03
        "v06/wendyhand08.jpg"
        pause 0.03
        "v06/wendyhand09.jpg"
        pause 0.03
        "v06/wendyhand10.jpg"
        pause 0.03
        "v06/wendyhand11.jpg"
        pause 0.06
        "v06/wendyhand10.jpg"
        pause 0.04
        "v06/wendyhand09.jpg"
        pause 0.04
        "v06/wendyhand08.jpg"
        pause 0.04
        "v06/wendyhand07.jpg"
        pause 0.04
        "v06/wendyhand06.jpg"
        pause 0.04
        "v06/wendyhand05.jpg"
        pause 0.04
        "v06/wendyhand04.jpg"
        pause 0.04
        "v06/wendyhand03.jpg"
        pause 0.04
        "v06/wendyhand02.jpg"
        pause 0.04
        "v06/wendyhand01.jpg"
        pause 0.04
        repeat
            
    image wendyhandfast:
        "v06/wendyhand00.jpg"
        pause 0.05
        "v06/wendyhand01.jpg"
        pause 0.025
        "v06/wendyhand02.jpg"
        pause 0.025
        "v06/wendyhand03.jpg"
        pause 0.025
        "v06/wendyhand04.jpg"
        pause 0.025
        "v06/wendyhand05.jpg"
        pause 0.025
        "v06/wendyhand06.jpg"
        pause 0.025
        "v06/wendyhand07.jpg"
        pause 0.025
        "v06/wendyhand08.jpg"
        pause 0.025
        "v06/wendyhand09.jpg"
        pause 0.025
        "v06/wendyhand10.jpg"
        pause 0.025
        "v06/wendyhand11.jpg"
        pause 0.06
        "v06/wendyhand10.jpg"
        pause 0.03
        "v06/wendyhand09.jpg"
        pause 0.03
        "v06/wendyhand08.jpg"
        pause 0.03
        "v06/wendyhand07.jpg"
        pause 0.03
        "v06/wendyhand06.jpg"
        pause 0.03
        "v06/wendyhand05.jpg"
        pause 0.03
        "v06/wendyhand04.jpg"
        pause 0.03
        "v06/wendyhand03.jpg"
        pause 0.03
        "v06/wendyhand02.jpg"
        pause 0.03
        "v06/wendyhand01.jpg"
        pause 0.03
        repeat
            
    image wendyblowslow:
        "v06/wendyblow00.jpg"
        pause 0.06
        "v06/wendyblow01.jpg"
        pause 0.03
        "v06/wendyblow02.jpg"
        pause 0.03
        "v06/wendyblow03.jpg"
        pause 0.03
        "v06/wendyblow04.jpg"
        pause 0.03
        "v06/wendyblow05.jpg"
        pause 0.03
        "v06/wendyblow06.jpg"
        pause 0.03
        "v06/wendyblow07.jpg"
        pause 0.03
        "v06/wendyblow08.jpg"
        pause 0.03
        "v06/wendyblow09.jpg"
        pause 0.03
        "v06/wendyblow10.jpg"
        pause 0.03
        "v06/wendyblow11.jpg"
        pause 0.06
        "v06/wendyblow10.jpg"
        pause 0.04
        "v06/wendyblow09.jpg"
        pause 0.04
        "v06/wendyblow08.jpg"
        pause 0.04
        "v06/wendyblow07.jpg"
        pause 0.04
        "v06/wendyblow06.jpg"
        pause 0.04
        "v06/wendyblow05.jpg"
        pause 0.04
        "v06/wendyblow04.jpg"
        pause 0.04
        "v06/wendyblow03.jpg"
        pause 0.04
        "v06/wendyblow02.jpg"
        pause 0.04
        "v06/wendyblow01.jpg"
        pause 0.04
        repeat
            
    image wendyblowfast:
        "v06/wendyblow00.jpg"
        pause 0.05
        "v06/wendyblow01.jpg"
        pause 0.025
        "v06/wendyblow02.jpg"
        pause 0.025
        "v06/wendyblow03.jpg"
        pause 0.025
        "v06/wendyblow04.jpg"
        pause 0.025
        "v06/wendyblow05.jpg"
        pause 0.025
        "v06/wendyblow06.jpg"
        pause 0.025
        "v06/wendyblow07.jpg"
        pause 0.025
        "v06/wendyblow08.jpg"
        pause 0.025
        "v06/wendyblow09.jpg"
        pause 0.025
        "v06/wendyblow10.jpg"
        pause 0.3
        "v06/wendyblow11.jpg"
        pause 0.06
        "v06/wendyblow10.jpg"
        pause 0.03
        "v06/wendyblow09.jpg"
        pause 0.03
        "v06/wendyblow08.jpg"
        pause 0.03
        "v06/wendyblow07.jpg"
        pause 0.03
        "v06/wendyblow06.jpg"
        pause 0.03
        "v06/wendyblow05.jpg"
        pause 0.03
        "v06/wendyblow04.jpg"
        pause 0.03
        "v06/wendyblow03.jpg"
        pause 0.03
        "v06/wendyblow02.jpg"
        pause 0.03
        "v06/wendyblow01.jpg"
        pause 0.03
        repeat
            
    image pennystandslow:
        "v061/pennystand00.png"
        pause 0.06
        "v061/pennystand01.png"
        pause 0.03
        "v061/pennystand02.png"
        pause 0.03
        "v061/pennystand03.png"
        pause 0.03
        "v061/pennystand04.png"
        pause 0.03
        "v061/pennystand05.png"
        pause 0.03
        "v061/pennystand06.png"
        pause 0.03
        "v061/pennystand07.png"
        pause 0.03
        "v061/pennystand08.png"
        pause 0.03
        "v061/pennystand09.png"
        pause 0.03
        "v061/pennystand10.png"
        pause 0.06
        "v061/pennystand09.png"
        pause 0.04
        "v061/pennystand08.png"
        pause 0.04
        "v061/pennystand07.png"
        pause 0.04
        "v061/pennystand06.png"
        pause 0.04
        "v061/pennystand05.png"
        pause 0.04
        "v061/pennystand04.png"
        pause 0.04
        "v061/pennystand03.png"
        pause 0.04
        "v061/pennystand02.png"
        pause 0.04
        "v061/pennystand01.png"
        pause 0.04
        repeat
            
    image pennystandfast:
        "v061/pennystand00.png"
        pause 0.05
        "v061/pennystand01.png"
        pause 0.025
        "v061/pennystand02.png"
        pause 0.025
        "v061/pennystand03.png"
        pause 0.025
        "v061/pennystand04.png"
        pause 0.025
        "v061/pennystand05.png"
        pause 0.025
        "v061/pennystand06.png"
        pause 0.025
        "v061/pennystand07.png"
        pause 0.025
        "v061/pennystand08.png"
        pause 0.025
        "v061/pennystand09.png"
        pause 0.025
        "v061/pennystand10.png"
        pause 0.06
        "v061/pennystand09.png"
        pause 0.03
        "v061/pennystand08.png"
        pause 0.03
        "v061/pennystand07.png"
        pause 0.03
        "v061/pennystand06.png"
        pause 0.03
        "v061/pennystand05.png"
        pause 0.03
        "v061/pennystand04.png"
        pause 0.03
        "v061/pennystand03.png"
        pause 0.03
        "v061/pennystand02.png"
        pause 0.03
        "v061/pennystand01.png"
        pause 0.03
        repeat

    image pennystandbslow:
        "v061/pennystandb00.png"
        pause 0.06
        "v061/pennystandb01.png"
        pause 0.03
        "v061/pennystandb02.png"
        pause 0.03
        "v061/pennystandb03.png"
        pause 0.03
        "v061/pennystandb04.png"
        pause 0.03
        "v061/pennystandb05.png"
        pause 0.03
        "v061/pennystandb06.png"
        pause 0.03
        "v061/pennystandb07.png"
        pause 0.03
        "v061/pennystandb08.png"
        pause 0.03
        "v061/pennystandb09.png"
        pause 0.03
        "v061/pennystandb10.png"
        pause 0.06
        "v061/pennystandb09.png"
        pause 0.04
        "v061/pennystandb08.png"
        pause 0.04
        "v061/pennystandb07.png"
        pause 0.04
        "v061/pennystandb06.png"
        pause 0.04
        "v061/pennystandb05.png"
        pause 0.04
        "v061/pennystandb04.png"
        pause 0.04
        "v061/pennystandb03.png"
        pause 0.04
        "v061/pennystandb02.png"
        pause 0.04
        "v061/pennystandb01.png"
        pause 0.04
        repeat
            
    image pennystandbfast:
        "v061/pennystandb00.png"
        pause 0.05
        "v061/pennystandb01.png"
        pause 0.025
        "v061/pennystandb02.png"
        pause 0.025
        "v061/pennystandb03.png"
        pause 0.025
        "v061/pennystandb04.png"
        pause 0.025
        "v061/pennystandb05.png"
        pause 0.025
        "v061/pennystandb06.png"
        pause 0.025
        "v061/pennystandb07.png"
        pause 0.025
        "v061/pennystandb08.png"
        pause 0.025
        "v061/pennystandb09.png"
        pause 0.025
        "v061/pennystandb10.png"
        pause 0.06
        "v061/pennystandb09.png"
        pause 0.03
        "v061/pennystandb08.png"
        pause 0.03
        "v061/pennystandb07.png"
        pause 0.03
        "v061/pennystandb06.png"
        pause 0.03
        "v061/pennystandb05.png"
        pause 0.03
        "v061/pennystandb04.png"
        pause 0.03
        "v061/pennystandb03.png"
        pause 0.03
        "v061/pennystandb02.png"
        pause 0.03
        "v061/pennystandb01.png"
        pause 0.03
        repeat

    image pennyanalslow:
        "v061/pennyanal00.png"
        pause 0.06
        "v061/pennyanal01.png"
        pause 0.03
        "v061/pennyanal02.png"
        pause 0.03
        "v061/pennyanal03.png"
        pause 0.03
        "v061/pennyanal04.png"
        pause 0.03
        "v061/pennyanal05.png"
        pause 0.03
        "v061/pennyanal06.png"
        pause 0.03
        "v061/pennyanal07.png"
        pause 0.03
        "v061/pennyanal08.png"
        pause 0.03
        "v061/pennyanal09.png"
        pause 0.03
        "v061/pennyanal10.png"
        pause 0.03
        "v061/pennyanal11.png"
        pause 0.06
        "v061/pennyanal10.png"
        pause 0.04
        "v061/pennyanal09.png"
        pause 0.04
        "v061/pennyanal08.png"
        pause 0.04
        "v061/pennyanal07.png"
        pause 0.04
        "v061/pennyanal06.png"
        pause 0.04
        "v061/pennyanal05.png"
        pause 0.04
        "v061/pennyanal04.png"
        pause 0.04
        "v061/pennyanal03.png"
        pause 0.04
        "v061/pennyanal02.png"
        pause 0.04
        "v061/pennyanal01.png"
        pause 0.04
        repeat
    
    image pennyanalfast:
        "v061/pennyanal00.png"
        pause 0.05
        "v061/pennyanal01.png"
        pause 0.025
        "v061/pennyanal02.png"
        pause 0.025
        "v061/pennyanal03.png"
        pause 0.025
        "v061/pennyanal04.png"
        pause 0.025
        "v061/pennyanal05.png"
        pause 0.025
        "v061/pennyanal06.png"
        pause 0.025
        "v061/pennyanal07.png"
        pause 0.025
        "v061/pennyanal08.png"
        pause 0.025
        "v061/pennyanal09.png"
        pause 0.025
        "v061/pennyanal10.png"
        pause 0.03
        "v061/pennyanal11.png"
        pause 0.06
        "v061/pennyanal10.png"
        pause 0.03
        "v061/pennyanal09.png"
        pause 0.03
        "v061/pennyanal08.png"
        pause 0.03
        "v061/pennyanal07.png"
        pause 0.03
        "v061/pennyanal06.png"
        pause 0.03
        "v061/pennyanal05.png"
        pause 0.03
        "v061/pennyanal04.png"
        pause 0.03
        "v061/pennyanal03.png"
        pause 0.03
        "v061/pennyanal02.png"
        pause 0.03
        "v061/pennyanal01.png"
        pause 0.03
        repeat

    image pennyanalpovslow:
        "v061/pennyanalb00.png"
        pause 0.06
        "v061/pennyanalb01.png"
        pause 0.03
        "v061/pennyanalb02.png"
        pause 0.03
        "v061/pennyanalb03.png"
        pause 0.03
        "v061/pennyanalb04.png"
        pause 0.03
        "v061/pennyanalb05.png"
        pause 0.03
        "v061/pennyanalb06.png"
        pause 0.03
        "v061/pennyanalb07.png"
        pause 0.03
        "v061/pennyanalb08.png"
        pause 0.03
        "v061/pennyanalb09.png"
        pause 0.03
        "v061/pennyanalb10.png"
        pause 0.03
        "v061/pennyanalb11.png"
        pause 0.06
        "v061/pennyanalb10.png"
        pause 0.04
        "v061/pennyanalb09.png"
        pause 0.04
        "v061/pennyanalb08.png"
        pause 0.04
        "v061/pennyanalb07.png"
        pause 0.04
        "v061/pennyanalb06.png"
        pause 0.04
        "v061/pennyanalb05.png"
        pause 0.04
        "v061/pennyanalb04.png"
        pause 0.04
        "v061/pennyanalb03.png"
        pause 0.04
        "v061/pennyanalb02.png"
        pause 0.04
        "v061/pennyanalb01.png"
        pause 0.04
        repeat

    image pennyanalpovfast:
        "v061/pennyanalb00.png"
        pause 0.05
        "v061/pennyanalb01.png"
        pause 0.025
        "v061/pennyanalb02.png"
        pause 0.025
        "v061/pennyanalb03.png"
        pause 0.025
        "v061/pennyanalb04.png"
        pause 0.025
        "v061/pennyanalb05.png"
        pause 0.025
        "v061/pennyanalb06.png"
        pause 0.025
        "v061/pennyanalb07.png"
        pause 0.025
        "v061/pennyanalb08.png"
        pause 0.025
        "v061/pennyanalb09.png"
        pause 0.025
        "v061/pennyanalb10.png"
        pause 0.03
        "v061/pennyanalb11.png"
        pause 0.06
        "v061/pennyanalb10.png"
        pause 0.03
        "v061/pennyanalb09.png"
        pause 0.03
        "v061/pennyanalb08.png"
        pause 0.03
        "v061/pennyanalb07.png"
        pause 0.03
        "v061/pennyanalb06.png"
        pause 0.03
        "v061/pennyanalb05.png"
        pause 0.03
        "v061/pennyanalb04.png"
        pause 0.03
        "v061/pennyanalb03.png"
        pause 0.03
        "v061/pennyanalb02.png"
        pause 0.03
        "v061/pennyanalb01.png"
        pause 0.03
        repeat
    
    image pennybedroomslow:
        "v061/pennybedroomfuck00.jpg"
        pause 0.06
        "v061/pennybedroomfuck01.jpg"
        pause 0.03
        "v061/pennybedroomfuck02.jpg"
        pause 0.03
        "v061/pennybedroomfuck03.jpg"
        pause 0.03
        "v061/pennybedroomfuck04.jpg"
        pause 0.03
        "v061/pennybedroomfuck05.jpg"
        pause 0.03
        "v061/pennybedroomfuck06.jpg"
        pause 0.03
        "v061/pennybedroomfuck07.jpg"
        pause 0.03
        "v061/pennybedroomfuck08.jpg"
        pause 0.03
        "v061/pennybedroomfuck09.jpg"
        pause 0.03
        "v061/pennybedroomfuck10.jpg"
        pause 0.06
        "v061/pennybedroomfuck09.jpg"
        pause 0.04
        "v061/pennybedroomfuck08.jpg"
        pause 0.04
        "v061/pennybedroomfuck07.jpg"
        pause 0.04
        "v061/pennybedroomfuck06.jpg"
        pause 0.04
        "v061/pennybedroomfuck05.jpg"
        pause 0.04
        "v061/pennybedroomfuck04.jpg"
        pause 0.04
        "v061/pennybedroomfuck03.jpg"
        pause 0.04
        "v061/pennybedroomfuck02.jpg"
        pause 0.04
        "v061/pennybedroomfuck01.jpg"
        pause 0.04
        repeat
            
    image pennybedroomfast:
        "v061/pennybedroomfuck00.jpg"
        pause 0.05
        "v061/pennybedroomfuck01.jpg"
        pause 0.025
        "v061/pennybedroomfuck02.jpg"
        pause 0.025
        "v061/pennybedroomfuck03.jpg"
        pause 0.025
        "v061/pennybedroomfuck04.jpg"
        pause 0.025
        "v061/pennybedroomfuck05.jpg"
        pause 0.025
        "v061/pennybedroomfuck06.jpg"
        pause 0.025
        "v061/pennybedroomfuck07.jpg"
        pause 0.025
        "v061/pennybedroomfuck08.jpg"
        pause 0.025
        "v061/pennybedroomfuck09.jpg"
        pause 0.025
        "v061/pennybedroomfuck10.jpg"
        pause 0.06
        "v061/pennybedroomfuck09.jpg"
        pause 0.03
        "v061/pennybedroomfuck08.jpg"
        pause 0.03
        "v061/pennybedroomfuck07.jpg"
        pause 0.03
        "v061/pennybedroomfuck06.jpg"
        pause 0.03
        "v061/pennybedroomfuck05.jpg"
        pause 0.03
        "v061/pennybedroomfuck04.jpg"
        pause 0.03
        "v061/pennybedroomfuck03.jpg"
        pause 0.03
        "v061/pennybedroomfuck02.jpg"
        pause 0.03
        "v061/pennybedroomfuck01.jpg"
        pause 0.03
        repeat
            
    image pennyacrobaticslow:
        "v061/pennyacro00.png"
        pause 0.06
        "v061/pennyacro01.png"
        pause 0.03
        "v061/pennyacro02.png"
        pause 0.03
        "v061/pennyacro03.png"
        pause 0.03
        "v061/pennyacro04.png"
        pause 0.03
        "v061/pennyacro05.png"
        pause 0.03
        "v061/pennyacro06.png"
        pause 0.03
        "v061/pennyacro07.png"
        pause 0.03
        "v061/pennyacro08.png"
        pause 0.03
        "v061/pennyacro09.png"
        pause 0.03
        "v061/pennyacro10.png"
        pause 0.03
        "v061/pennyacro11.png"
        pause 0.06
        "v061/pennyacro10.png"
        pause 0.04
        "v061/pennyacro09.png"
        pause 0.04
        "v061/pennyacro08.png"
        pause 0.04
        "v061/pennyacro07.png"
        pause 0.04
        "v061/pennyacro06.png"
        pause 0.04
        "v061/pennyacro05.png"
        pause 0.04
        "v061/pennyacro04.png"
        pause 0.04
        "v061/pennyacro03.png"
        pause 0.04
        "v061/pennyacro02.png"
        pause 0.04
        "v061/pennyacro01.png"
        pause 0.04
        repeat
            
    image pennyacrobaticfast:
        "v061/pennyacro00.png"
        pause 0.05
        "v061/pennyacro01.png"
        pause 0.025
        "v061/pennyacro02.png"
        pause 0.025
        "v061/pennyacro03.png"
        pause 0.025
        "v061/pennyacro04.png"
        pause 0.025
        "v061/pennyacro05.png"
        pause 0.025
        "v061/pennyacro06.png"
        pause 0.025
        "v061/pennyacro07.png"
        pause 0.025
        "v061/pennyacro08.png"
        pause 0.025
        "v061/pennyacro09.png"
        pause 0.025
        "v061/pennyacro10.png"
        pause 0.025
        "v061/pennyacro11.png"
        pause 0.05
        "v061/pennyacro10.png"
        pause 0.03
        "v061/pennyacro09.png"
        pause 0.03
        "v061/pennyacro08.png"
        pause 0.03
        "v061/pennyacro07.png"
        pause 0.03
        "v061/pennyacro06.png"
        pause 0.03
        "v061/pennyacro05.png"
        pause 0.03
        "v061/pennyacro04.png"
        pause 0.03
        "v061/pennyacro03.png"
        pause 0.03
        "v061/pennyacro02.png"
        pause 0.03
        "v061/pennyacro01.png"
        pause 0.03
        repeat

    image pennyacrobaticpovslow:
        "v061/pennyacropov00.png"
        pause 0.06
        "v061/pennyacropov01.png"
        pause 0.03
        "v061/pennyacropov02.png"
        pause 0.03
        "v061/pennyacropov03.png"
        pause 0.03
        "v061/pennyacropov04.png"
        pause 0.03
        "v061/pennyacropov05.png"
        pause 0.03
        "v061/pennyacropov06.png"
        pause 0.03
        "v061/pennyacropov07.png"
        pause 0.03
        "v061/pennyacropov08.png"
        pause 0.03
        "v061/pennyacropov09.png"
        pause 0.03
        "v061/pennyacropov10.png"
        pause 0.03
        "v061/pennyacropov11.png"
        pause 0.06
        "v061/pennyacropov10.png"
        pause 0.04
        "v061/pennyacropov09.png"
        pause 0.04
        "v061/pennyacropov08.png"
        pause 0.04
        "v061/pennyacropov07.png"
        pause 0.04
        "v061/pennyacropov06.png"
        pause 0.04
        "v061/pennyacropov05.png"
        pause 0.04
        "v061/pennyacropov04.png"
        pause 0.04
        "v061/pennyacropov03.png"
        pause 0.04
        "v061/pennyacropov02.png"
        pause 0.04
        "v061/pennyacropov01.png"
        pause 0.04
        repeat
            
    image pennyacrobaticpovfast:
        "v061/pennyacropov00.png"
        pause 0.05
        "v061/pennyacropov01.png"
        pause 0.025
        "v061/pennyacropov02.png"
        pause 0.025
        "v061/pennyacropov03.png"
        pause 0.025
        "v061/pennyacropov04.png"
        pause 0.025
        "v061/pennyacropov05.png"
        pause 0.025
        "v061/pennyacropov06.png"
        pause 0.025
        "v061/pennyacropov07.png"
        pause 0.025
        "v061/pennyacropov08.png"
        pause 0.025
        "v061/pennyacropov09.png"
        pause 0.025
        "v061/pennyacropov10.png"
        pause 0.025
        "v061/pennyacropov11.png"
        pause 0.05
        "v061/pennyacropov10.png"
        pause 0.03
        "v061/pennyacropov09.png"
        pause 0.03
        "v061/pennyacropov08.png"
        pause 0.03
        "v061/pennyacropov07.png"
        pause 0.03
        "v061/pennyacropov06.png"
        pause 0.03
        "v061/pennyacropov05.png"
        pause 0.03
        "v061/pennyacropov04.png"
        pause 0.03
        "v061/pennyacropov03.png"
        pause 0.03
        "v061/pennyacropov02.png"
        pause 0.03
        "v061/pennyacropov01.png"
        pause 0.03
        repeat

    image pennydoggyslow:
        "v061/pennydoggy00.png"
        pause 0.06
        "v061/pennydoggy01.png"
        pause 0.03
        "v061/pennydoggy02.png"
        pause 0.03
        "v061/pennydoggy03.png"
        pause 0.03
        "v061/pennydoggy04.png"
        pause 0.03
        "v061/pennydoggy05.png"
        pause 0.03
        "v061/pennydoggy06.png"
        pause 0.03
        "v061/pennydoggy07.png"
        pause 0.03
        "v061/pennydoggy08.png"
        pause 0.03
        "v061/pennydoggy09.png"
        pause 0.03
        "v061/pennydoggy10.png"
        pause 0.06
        "v061/pennydoggy09.png"
        pause 0.04
        "v061/pennydoggy08.png"
        pause 0.04
        "v061/pennydoggy07.png"
        pause 0.04
        "v061/pennydoggy06.png"
        pause 0.04
        "v061/pennydoggy05.png"
        pause 0.04
        "v061/pennydoggy04.png"
        pause 0.04
        "v061/pennydoggy03.png"
        pause 0.04
        "v061/pennydoggy02.png"
        pause 0.04
        "v061/pennydoggy01.png"
        pause 0.04
        repeat
            
    image pennydoggyfast:
        "v061/pennydoggy00.png"
        pause 0.05
        "v061/pennydoggy01.png"
        pause 0.025
        "v061/pennydoggy02.png"
        pause 0.025
        "v061/pennydoggy03.png"
        pause 0.025
        "v061/pennydoggy04.png"
        pause 0.025
        "v061/pennydoggy05.png"
        pause 0.025
        "v061/pennydoggy06.png"
        pause 0.025
        "v061/pennydoggy07.png"
        pause 0.025
        "v061/pennydoggy08.png"
        pause 0.025
        "v061/pennydoggy09.png"
        pause 0.025
        "v061/pennydoggy10.png"
        pause 0.05
        "v061/pennydoggy09.png"
        pause 0.03
        "v061/pennydoggy08.png"
        pause 0.03
        "v061/pennydoggy07.png"
        pause 0.03
        "v061/pennydoggy06.png"
        pause 0.03
        "v061/pennydoggy05.png"
        pause 0.03
        "v061/pennydoggy04.png"
        pause 0.03
        "v061/pennydoggy03.png"
        pause 0.03
        "v061/pennydoggy02.png"
        pause 0.03
        "v061/pennydoggy01.png"
        pause 0.03
        repeat

    image pennydoggypovslow:
        "v061/pennydoggypov00.png"
        pause 0.06
        "v061/pennydoggypov01.png"
        pause 0.03
        "v061/pennydoggypov02.png"
        pause 0.03
        "v061/pennydoggypov03.png"
        pause 0.03
        "v061/pennydoggypov04.png"
        pause 0.03
        "v061/pennydoggypov05.png"
        pause 0.03
        "v061/pennydoggypov06.png"
        pause 0.03
        "v061/pennydoggypov07.png"
        pause 0.03
        "v061/pennydoggypov08.png"
        pause 0.03
        "v061/pennydoggypov09.png"
        pause 0.03
        "v061/pennydoggypov10.png"
        pause 0.06
        "v061/pennydoggypov09.png"
        pause 0.04
        "v061/pennydoggypov08.png"
        pause 0.04
        "v061/pennydoggypov07.png"
        pause 0.04
        "v061/pennydoggypov06.png"
        pause 0.04
        "v061/pennydoggypov05.png"
        pause 0.04
        "v061/pennydoggypov04.png"
        pause 0.04
        "v061/pennydoggypov03.png"
        pause 0.04
        "v061/pennydoggypov02.png"
        pause 0.04
        "v061/pennydoggypov01.png"
        pause 0.04
        repeat
            
    image pennydoggypovfast:
        "v061/pennydoggypov00.png"
        pause 0.05
        "v061/pennydoggypov01.png"
        pause 0.025
        "v061/pennydoggypov02.png"
        pause 0.025
        "v061/pennydoggypov03.png"
        pause 0.025
        "v061/pennydoggypov04.png"
        pause 0.025
        "v061/pennydoggypov05.png"
        pause 0.025
        "v061/pennydoggypov06.png"
        pause 0.025
        "v061/pennydoggypov07.png"
        pause 0.025
        "v061/pennydoggypov08.png"
        pause 0.025
        "v061/pennydoggypov09.png"
        pause 0.025
        "v061/pennydoggypov10.png"
        pause 0.05
        "v061/pennydoggypov09.png"
        pause 0.03
        "v061/pennydoggypov08.png"
        pause 0.03
        "v061/pennydoggypov07.png"
        pause 0.03
        "v061/pennydoggypov06.png"
        pause 0.03
        "v061/pennydoggypov05.png"
        pause 0.03
        "v061/pennydoggypov04.png"
        pause 0.03
        "v061/pennydoggypov03.png"
        pause 0.03
        "v061/pennydoggypov02.png"
        pause 0.03
        "v061/pennydoggypov01.png"
        pause 0.03
        repeat
    
    image pennywiggle:
        "v061/pennywiggle00.png"
        pause 0.03
        "v061/pennywiggle01.png"
        pause 0.03
        "v061/pennywiggle02.png"
        pause 0.03
        "v061/pennywiggle03.png"
        pause 0.03
        "v061/pennywiggle04.png"
        pause 0.03
        "v061/pennywiggle05.png"
        pause 0.03
        "v061/pennywiggle06.png"
        pause 0.03
        "v061/pennywiggle07.png"
        pause 0.03
        "v061/pennywiggle08.png"
        pause 0.03
        "v061/pennywiggle09.png"
        pause 0.03
        "v061/pennywiggle10.png"
        pause 0.03
        "v061/pennywiggle11.png"
        pause 0.03
        "v061/pennywiggle12.png"
        pause 0.03
        "v061/pennywiggle13.png"
        pause 0.03
        "v061/pennywiggle14.png"
        pause 0.03
        "v061/pennywiggle15.png"
        pause 0.03
        "v061/pennywiggle16.png"
        pause 0.03
        "v061/pennywiggle17.png"
        pause 0.03
        "v061/pennywiggle18.png"
        pause 0.03
        "v061/pennywiggle19.png"
        pause 0.03
        "v061/pennywiggle20.png"
        pause 0.03
        "v061/pennywiggle21.png"
        pause 0.03
        "v061/pennywiggle22.png"
        pause 0.03
        "v061/pennywiggle23.png"
        pause 0.03
        "v061/pennywiggle24.png"
        pause 0.03
        "v061/pennywiggle25.png"
        pause 0.03
        "v061/pennywiggle26.png"
        pause 0.03
        "v061/pennywiggle27.png"
        pause 0.03
        "v061/pennywiggle28.png"
        pause 0.03
        "v061/pennywiggle29.png"
        pause 0.03
        "v061/pennywiggle30.png"
        pause 0.03
        repeat
            
    image jennaslow:
        "v061/jennafuck00.jpg"
        pause 0.035
        "v061/jennafuck01.jpg"
        pause 0.035
        "v061/jennafuck02.jpg"
        pause 0.035
        "v061/jennafuck03.jpg"
        pause 0.035
        "v061/jennafuck04.jpg"
        pause 0.035
        "v061/jennafuck05.jpg"
        pause 0.035
        "v061/jennafuck06.jpg"
        pause 0.035
        "v061/jennafuck07.jpg"
        pause 0.035
        "v061/jennafuck08.jpg"
        pause 0.035
        "v061/jennafuck09.jpg"
        pause 0.035
        "v061/jennafuck10.jpg"
        pause 0.035
        "v061/jennafuck11.jpg"
        pause 0.035
        "v061/jennafuck12.jpg"
        pause 0.035
        "v061/jennafuck13.jpg"
        pause 0.035
        "v061/jennafuck14.jpg"
        pause 0.035
        "v061/jennafuck15.jpg"
        pause 0.035
        "v061/jennafuck16.jpg"
        pause 0.035
        "v061/jennafuck17.jpg"
        pause 0.035
        "v061/jennafuck18.jpg"
        pause 0.035
        "v061/jennafuck19.jpg"
        pause 0.035
        repeat
            
    image jennafast:
        "v061/jennafuck00.jpg"
        pause 0.025
        "v061/jennafuck01.jpg"
        pause 0.025
        "v061/jennafuck02.jpg"
        pause 0.025
        "v061/jennafuck03.jpg"
        pause 0.025
        "v061/jennafuck04.jpg"
        pause 0.025
        "v061/jennafuck05.jpg"
        pause 0.025
        "v061/jennafuck06.jpg"
        pause 0.025
        "v061/jennafuck07.jpg"
        pause 0.025
        "v061/jennafuck08.jpg"
        pause 0.025
        "v061/jennafuck09.jpg"
        pause 0.025
        "v061/jennafuck10.jpg"
        pause 0.025
        "v061/jennafuck11.jpg"
        pause 0.025
        "v061/jennafuck12.jpg"
        pause 0.025
        "v061/jennafuck13.jpg"
        pause 0.025
        "v061/jennafuck14.jpg"
        pause 0.025
        "v061/jennafuck15.jpg"
        pause 0.025
        "v061/jennafuck16.jpg"
        pause 0.025
        "v061/jennafuck17.jpg"
        pause 0.025
        "v061/jennafuck18.jpg"
        pause 0.025
        "v061/jennafuck19.jpg"
        pause 0.025
        repeat
            
    image jennapovslow:
        "v061/jennapov00.jpg"
        pause 0.035
        "v061/jennapov01.jpg"
        pause 0.035
        "v061/jennapov02.jpg"
        pause 0.035
        "v061/jennapov03.jpg"
        pause 0.035
        "v061/jennapov04.jpg"
        pause 0.035
        "v061/jennapov05.jpg"
        pause 0.035
        "v061/jennapov06.jpg"
        pause 0.035
        "v061/jennapov07.jpg"
        pause 0.035
        "v061/jennapov08.jpg"
        pause 0.035
        "v061/jennapov09.jpg"
        pause 0.035
        "v061/jennapov10.jpg"
        pause 0.035
        "v061/jennapov11.jpg"
        pause 0.035
        "v061/jennapov12.jpg"
        pause 0.035
        "v061/jennapov13.jpg"
        pause 0.035
        "v061/jennapov14.jpg"
        pause 0.035
        "v061/jennapov15.jpg"
        pause 0.035
        "v061/jennapov16.jpg"
        pause 0.035
        "v061/jennapov17.jpg"
        pause 0.035
        "v061/jennapov18.jpg"
        pause 0.035
        "v061/jennapov19.jpg"
        pause 0.035
        repeat
            
    image jennapovfast:
        "v061/jennapov00.jpg"
        pause 0.025
        "v061/jennapov01.jpg"
        pause 0.025
        "v061/jennapov02.jpg"
        pause 0.025
        "v061/jennapov03.jpg"
        pause 0.025
        "v061/jennapov04.jpg"
        pause 0.025
        "v061/jennapov05.jpg"
        pause 0.025
        "v061/jennapov06.jpg"
        pause 0.025
        "v061/jennapov07.jpg"
        pause 0.025
        "v061/jennapov08.jpg"
        pause 0.025
        "v061/jennapov09.jpg"
        pause 0.025
        "v061/jennapov10.jpg"
        pause 0.025
        "v061/jennapov11.jpg"
        pause 0.025
        "v061/jennapov12.jpg"
        pause 0.025
        "v061/jennapov13.jpg"
        pause 0.025
        "v061/jennapov14.jpg"
        pause 0.025
        "v061/jennapov15.jpg"
        pause 0.025
        "v061/jennapov16.jpg"
        pause 0.025
        "v061/jennapov17.jpg"
        pause 0.025
        "v061/jennapov18.jpg"
        pause 0.025
        "v061/jennapov19.jpg"
        pause 0.025
        repeat

    image gwenimpregnateslow:
        "v061/gwenimpregnate00.png"
        pause 0.06
        "v061/gwenimpregnate01.png"
        pause 0.03
        "v061/gwenimpregnate02.png"
        pause 0.03
        "v061/gwenimpregnate03.png"
        pause 0.03
        "v061/gwenimpregnate04.png"
        pause 0.03
        "v061/gwenimpregnate05.png"
        pause 0.03
        "v061/gwenimpregnate06.png"
        pause 0.03
        "v061/gwenimpregnate07.png"
        pause 0.03
        "v061/gwenimpregnate08.png"
        pause 0.03
        "v061/gwenimpregnate09.png"
        pause 0.03
        "v061/gwenimpregnate10.png"
        pause 0.06
        "v061/gwenimpregnate09.png"
        pause 0.04
        "v061/gwenimpregnate08.png"
        pause 0.04
        "v061/gwenimpregnate07.png"
        pause 0.04
        "v061/gwenimpregnate06.png"
        pause 0.04
        "v061/gwenimpregnate05.png"
        pause 0.04
        "v061/gwenimpregnate04.png"
        pause 0.04
        "v061/gwenimpregnate03.png"
        pause 0.04
        "v061/gwenimpregnate02.png"
        pause 0.04
        "v061/gwenimpregnate01.png"
        pause 0.04
        repeat
            
    image gwenimpregnatefast:
        "v061/gwenimpregnate00.png"
        pause 0.05
        "v061/gwenimpregnate01.png"
        pause 0.025
        "v061/gwenimpregnate02.png"
        pause 0.025
        "v061/gwenimpregnate03.png"
        pause 0.025
        "v061/gwenimpregnate04.png"
        pause 0.025
        "v061/gwenimpregnate05.png"
        pause 0.025
        "v061/gwenimpregnate06.png"
        pause 0.025
        "v061/gwenimpregnate07.png"
        pause 0.025
        "v061/gwenimpregnate08.png"
        pause 0.025
        "v061/gwenimpregnate09.png"
        pause 0.025
        "v061/gwenimpregnate10.png"
        pause 0.05
        "v061/gwenimpregnate09.png"
        pause 0.03
        "v061/gwenimpregnate08.png"
        pause 0.03
        "v061/gwenimpregnate07.png"
        pause 0.03
        "v061/gwenimpregnate06.png"
        pause 0.03
        "v061/gwenimpregnate05.png"
        pause 0.03
        "v061/gwenimpregnate04.png"
        pause 0.03
        "v061/gwenimpregnate03.png"
        pause 0.03
        "v061/gwenimpregnate02.png"
        pause 0.03
        "v061/gwenimpregnate01.png"
        pause 0.03
        repeat
    
    image gwenimpregnatepovslow:
        "v061/gwenimpregnatepov00.png"
        pause 0.06
        "v061/gwenimpregnatepov01.png"
        pause 0.03
        "v061/gwenimpregnatepov02.png"
        pause 0.03
        "v061/gwenimpregnatepov03.png"
        pause 0.03
        "v061/gwenimpregnatepov04.png"
        pause 0.03
        "v061/gwenimpregnatepov05.png"
        pause 0.03
        "v061/gwenimpregnatepov06.png"
        pause 0.03
        "v061/gwenimpregnatepov07.png"
        pause 0.03
        "v061/gwenimpregnatepov08.png"
        pause 0.03
        "v061/gwenimpregnatepov09.png"
        pause 0.03
        "v061/gwenimpregnatepov10.png"
        pause 0.06
        "v061/gwenimpregnatepov09.png"
        pause 0.04
        "v061/gwenimpregnatepov08.png"
        pause 0.04
        "v061/gwenimpregnatepov07.png"
        pause 0.04
        "v061/gwenimpregnatepov06.png"
        pause 0.04
        "v061/gwenimpregnatepov05.png"
        pause 0.04
        "v061/gwenimpregnatepov04.png"
        pause 0.04
        "v061/gwenimpregnatepov03.png"
        pause 0.04
        "v061/gwenimpregnatepov02.png"
        pause 0.04
        "v061/gwenimpregnatepov01.png"
        pause 0.04
        repeat
            
    image gwenimpregnatepovfast:
        "v061/gwenimpregnatepov00.png"
        pause 0.05
        "v061/gwenimpregnatepov01.png"
        pause 0.025
        "v061/gwenimpregnatepov02.png"
        pause 0.025
        "v061/gwenimpregnatepov03.png"
        pause 0.025
        "v061/gwenimpregnatepov04.png"
        pause 0.025
        "v061/gwenimpregnatepov05.png"
        pause 0.025
        "v061/gwenimpregnatepov06.png"
        pause 0.025
        "v061/gwenimpregnatepov07.png"
        pause 0.025
        "v061/gwenimpregnatepov08.png"
        pause 0.025
        "v061/gwenimpregnatepov09.png"
        pause 0.025
        "v061/gwenimpregnatepov10.png"
        pause 0.05
        "v061/gwenimpregnatepov09.png"
        pause 0.03
        "v061/gwenimpregnatepov08.png"
        pause 0.03
        "v061/gwenimpregnatepov07.png"
        pause 0.03
        "v061/gwenimpregnatepov06.png"
        pause 0.03
        "v061/gwenimpregnatepov05.png"
        pause 0.03
        "v061/gwenimpregnatepov04.png"
        pause 0.03
        "v061/gwenimpregnatepov03.png"
        pause 0.03
        "v061/gwenimpregnatepov02.png"
        pause 0.03
        "v061/gwenimpregnatepov01.png"
        pause 0.03
        repeat
        
    image marniefemdomslow:
        "v07/marniefemfuck00.png"
        pause 0.04
        "v07/marniefemfuck01.png"
        pause 0.04
        "v07/marniefemfuck02.png"
        pause 0.04
        "v07/marniefemfuck03.png"
        pause 0.04
        "v07/marniefemfuck04.png"
        pause 0.04
        "v07/marniefemfuck05.png"
        pause 0.04
        "v07/marniefemfuck06.png"
        pause 0.04
        "v07/marniefemfuck07.png"
        pause 0.04
        "v07/marniefemfuck08.png"
        pause 0.04
        "v07/marniefemfuck09.png"
        pause 0.04
        "v07/marniefemfuck10.png"
        pause 0.04
        "v07/marniefemfuck11.png"
        pause 0.04
        "v07/marniefemfuck12.png"
        pause 0.04
        "v07/marniefemfuck13.png"
        pause 0.04
        "v07/marniefemfuck14.png"
        pause 0.04
        "v07/marniefemfuck15.png"
        pause 0.04
        "v07/marniefemfuck16.png"
        pause 0.04
        "v07/marniefemfuck17.png"
        pause 0.04
        "v07/marniefemfuck18.png"
        pause 0.04
        repeat
            
    image marniefemdomfast:
        "v07/marniefemfuck00.png"
        pause 0.03
        "v07/marniefemfuck01.png"
        pause 0.03
        "v07/marniefemfuck02.png"
        pause 0.03
        "v07/marniefemfuck03.png"
        pause 0.03
        "v07/marniefemfuck04.png"
        pause 0.03
        "v07/marniefemfuck05.png"
        pause 0.03
        "v07/marniefemfuck06.png"
        pause 0.03
        "v07/marniefemfuck07.png"
        pause 0.03
        "v07/marniefemfuck08.png"
        pause 0.03
        "v07/marniefemfuck09.png"
        pause 0.03
        "v07/marniefemfuck10.png"
        pause 0.03
        "v07/marniefemfuck11.png"
        pause 0.03
        "v07/marniefemfuck12.png"
        pause 0.03
        "v07/marniefemfuck13.png"
        pause 0.03
        "v07/marniefemfuck14.png"
        pause 0.03
        "v07/marniefemfuck15.png"
        pause 0.03
        "v07/marniefemfuck16.png"
        pause 0.03
        "v07/marniefemfuck17.png"
        pause 0.03
        "v07/marniefemfuck18.png"
        pause 0.03
        repeat

    image marniefemdompovslow:
        "v07/marniefemfuckb00.png"
        pause 0.04
        "v07/marniefemfuckb01.png"
        pause 0.04
        "v07/marniefemfuckb02.png"
        pause 0.04
        "v07/marniefemfuckb03.png"
        pause 0.04
        "v07/marniefemfuckb04.png"
        pause 0.04
        "v07/marniefemfuckb05.png"
        pause 0.04
        "v07/marniefemfuckb06.png"
        pause 0.04
        "v07/marniefemfuckb07.png"
        pause 0.04
        "v07/marniefemfuckb08.png"
        pause 0.04
        "v07/marniefemfuckb09.png"
        pause 0.04
        "v07/marniefemfuckb10.png"
        pause 0.04
        "v07/marniefemfuckb11.png"
        pause 0.04
        "v07/marniefemfuckb12.png"
        pause 0.04
        "v07/marniefemfuckb13.png"
        pause 0.04
        "v07/marniefemfuckb14.png"
        pause 0.04
        "v07/marniefemfuckb15.png"
        pause 0.04
        "v07/marniefemfuckb16.png"
        pause 0.04
        "v07/marniefemfuckb17.png"
        pause 0.04
        "v07/marniefemfuckb18.png"
        pause 0.04
        repeat
            
    image marniefemdompovfast:
        "v07/marniefemfuckb00.png"
        pause 0.03
        "v07/marniefemfuckb01.png"
        pause 0.03
        "v07/marniefemfuckb02.png"
        pause 0.03
        "v07/marniefemfuckb03.png"
        pause 0.03
        "v07/marniefemfuckb04.png"
        pause 0.03
        "v07/marniefemfuckb05.png"
        pause 0.03
        "v07/marniefemfuckb06.png"
        pause 0.03
        "v07/marniefemfuckb07.png"
        pause 0.03
        "v07/marniefemfuckb08.png"
        pause 0.03
        "v07/marniefemfuckb09.png"
        pause 0.03
        "v07/marniefemfuckb10.png"
        pause 0.03
        "v07/marniefemfuckb11.png"
        pause 0.03
        "v07/marniefemfuckb12.png"
        pause 0.03
        "v07/marniefemfuckb13.png"
        pause 0.03
        "v07/marniefemfuckb14.png"
        pause 0.03
        "v07/marniefemfuckb15.png"
        pause 0.03
        "v07/marniefemfuckb16.png"
        pause 0.03
        "v07/marniefemfuckb17.png"
        pause 0.03
        "v07/marniefemfuckb18.png"
        pause 0.03
        repeat

    image marniemaledomslow:
        "v07/maledom00.jpg"
        pause 0.035
        "v07/maledom01.jpg"
        pause 0.035
        "v07/maledom02.jpg"
        pause 0.035
        "v07/maledom03.jpg"
        pause 0.035
        "v07/maledom04.jpg"
        pause 0.035
        "v07/maledom05.jpg"
        pause 0.035
        "v07/maledom06.jpg"
        pause 0.035
        "v07/maledom07.jpg"
        pause 0.035
        "v07/maledom08.jpg"
        pause 0.035
        "v07/maledom09.jpg"
        pause 0.035
        "v07/maledom10.jpg"
        pause 0.035
        "v07/maledom09.jpg"
        pause 0.035
        "v07/maledom08.jpg"
        pause 0.035
        "v07/maledom07.jpg"
        pause 0.035
        "v07/maledom06.jpg"
        pause 0.035
        "v07/maledom05.jpg"
        pause 0.035
        "v07/maledom04.jpg"
        pause 0.035
        "v07/maledom03.jpg"
        pause 0.035
        "v07/maledom02.jpg"
        pause 0.035
        "v07/maledom01.jpg"
        pause 0.035
        repeat
    
    image marniemaledomfast:
        "v07/maledom00.jpg"
        pause 0.025
        "v07/maledom01.jpg"
        pause 0.025
        "v07/maledom02.jpg"
        pause 0.025
        "v07/maledom03.jpg"
        pause 0.025
        "v07/maledom04.jpg"
        pause 0.025
        "v07/maledom05.jpg"
        pause 0.025
        "v07/maledom06.jpg"
        pause 0.025
        "v07/maledom07.jpg"
        pause 0.025
        "v07/maledom08.jpg"
        pause 0.025
        "v07/maledom09.jpg"
        pause 0.025
        "v07/maledom10.jpg"
        pause 0.025
        "v07/maledom09.jpg"
        pause 0.025
        "v07/maledom08.jpg"
        pause 0.025
        "v07/maledom07.jpg"
        pause 0.025
        "v07/maledom06.jpg"
        pause 0.025
        "v07/maledom05.jpg"
        pause 0.025
        "v07/maledom04.jpg"
        pause 0.025
        "v07/maledom03.jpg"
        pause 0.025
        "v07/maledom02.jpg"
        pause 0.025
        "v07/maledom01.jpg"
        pause 0.025
        repeat

    image marniemaledompovslow:
        "v07/maledompov00.jpg"
        pause 0.025
        "v07/maledompov01.jpg"
        pause 0.025
        "v07/maledompov02.jpg"
        pause 0.025
        "v07/maledompov03.jpg"
        pause 0.025
        "v07/maledompov04.jpg"
        pause 0.025
        "v07/maledompov05.jpg"
        pause 0.025
        "v07/maledompov06.jpg"
        pause 0.025
        "v07/maledompov07.jpg"
        pause 0.025
        "v07/maledompov08.jpg"
        pause 0.025
        "v07/maledompov09.jpg"
        pause 0.025
        "v07/maledompov08.jpg"
        pause 0.035
        "v07/maledompov07.jpg"
        pause 0.035
        "v07/maledompov06.jpg"
        pause 0.035
        "v07/maledompov05.jpg"
        pause 0.035
        "v07/maledompov04.jpg"
        pause 0.035
        "v07/maledompov03.jpg"
        pause 0.035
        "v07/maledompov02.jpg"
        pause 0.035
        "v07/maledompov01.jpg"
        pause 0.035
        repeat
    
    image marniemaledompovfast:
        "v07/maledompov00.jpg"
        pause 0.025
        "v07/maledompov01.jpg"
        pause 0.025
        "v07/maledompov02.jpg"
        pause 0.025
        "v07/maledompov03.jpg"
        pause 0.025
        "v07/maledompov04.jpg"
        pause 0.025
        "v07/maledompov05.jpg"
        pause 0.025
        "v07/maledompov06.jpg"
        pause 0.025
        "v07/maledompov07.jpg"
        pause 0.025
        "v07/maledompov08.jpg"
        pause 0.025
        "v07/maledompov09.jpg"
        pause 0.025
        "v07/maledompov08.jpg"
        pause 0.025
        "v07/maledompov07.jpg"
        pause 0.025
        "v07/maledompov06.jpg"
        pause 0.025
        "v07/maledompov05.jpg"
        pause 0.025
        "v07/maledompov04.jpg"
        pause 0.025
        "v07/maledompov03.jpg"
        pause 0.025
        "v07/maledompov02.jpg"
        pause 0.025
        "v07/maledompov01.jpg"
        pause 0.025
        repeat

    image marniemaledompostslow:
        "v07/maledompost00.jpg"
        pause 0.035
        "v07/maledompost01.jpg"
        pause 0.035
        "v07/maledompost02.jpg"
        pause 0.035
        "v07/maledompost03.jpg"
        pause 0.035
        "v07/maledompost04.jpg"
        pause 0.035
        "v07/maledompost05.jpg"
        pause 0.035
        "v07/maledompost06.jpg"
        pause 0.035
        "v07/maledompost07.jpg"
        pause 0.035
        "v07/maledompost08.jpg"
        pause 0.035
        "v07/maledompost09.jpg"
        pause 0.035
        "v07/maledompost10.jpg"
        pause 0.035
        "v07/maledompost09.jpg"
        pause 0.035
        "v07/maledompost08.jpg"
        pause 0.035
        "v07/maledompost07.jpg"
        pause 0.035
        "v07/maledompost06.jpg"
        pause 0.035
        "v07/maledompost05.jpg"
        pause 0.035
        "v07/maledompost04.jpg"
        pause 0.035
        "v07/maledompost03.jpg"
        pause 0.035
        "v07/maledompost02.jpg"
        pause 0.035
        "v07/maledompost01.jpg"
        pause 0.035
        repeat
    
    image marniemaledompostfast:
        "v07/maledompost00.jpg"
        pause 0.025
        "v07/maledompost01.jpg"
        pause 0.025
        "v07/maledompost02.jpg"
        pause 0.025
        "v07/maledompost03.jpg"
        pause 0.025
        "v07/maledompost04.jpg"
        pause 0.025
        "v07/maledompost05.jpg"
        pause 0.025
        "v07/maledompost06.jpg"
        pause 0.025
        "v07/maledompost07.jpg"
        pause 0.025
        "v07/maledompost08.jpg"
        pause 0.025
        "v07/maledompost09.jpg"
        pause 0.025
        "v07/maledompost10.jpg"
        pause 0.025
        "v07/maledompost09.jpg"
        pause 0.025
        "v07/maledompost08.jpg"
        pause 0.025
        "v07/maledompost07.jpg"
        pause 0.025
        "v07/maledompost06.jpg"
        pause 0.025
        "v07/maledompost05.jpg"
        pause 0.025
        "v07/maledompost04.jpg"
        pause 0.025
        "v07/maledompost03.jpg"
        pause 0.025
        "v07/maledompost02.jpg"
        pause 0.025
        "v07/maledompost01.jpg"
        pause 0.025
        repeat

    image marnietitfuckslow:
        "v07/marnietitfuck00.png"
        pause 0.035
        "v07/marnietitfuck01.png"
        pause 0.035
        "v07/marnietitfuck02.png"
        pause 0.035
        "v07/marnietitfuck03.png"
        pause 0.035
        "v07/marnietitfuck04.png"
        pause 0.035
        "v07/marnietitfuck05.png"
        pause 0.035
        "v07/marnietitfuck06.png"
        pause 0.035
        "v07/marnietitfuck07.png"
        pause 0.035
        "v07/marnietitfuck08.png"
        pause 0.035
        "v07/marnietitfuck09.png"
        pause 0.035
        "v07/marnietitfuck10.png"
        pause 0.035
        "v07/marnietitfuck11.png"
        pause 0.035
        "v07/marnietitfuck10.png"
        pause 0.035
        "v07/marnietitfuck09.png"
        pause 0.035
        "v07/marnietitfuck08.png"
        pause 0.035
        "v07/marnietitfuck07.png"
        pause 0.035
        "v07/marnietitfuck06.png"
        pause 0.035
        "v07/marnietitfuck05.png"
        pause 0.035
        "v07/marnietitfuck04.png"
        pause 0.035
        "v07/marnietitfuck03.png"
        pause 0.035
        "v07/marnietitfuck02.png"
        pause 0.035
        "v07/marnietitfuck01.png"
        pause 0.035
        repeat
        
    image marnietitfuckfast:
        "v07/marnietitfuck00.png"
        pause 0.025
        "v07/marnietitfuck01.png"
        pause 0.025
        "v07/marnietitfuck02.png"
        pause 0.025
        "v07/marnietitfuck03.png"
        pause 0.025
        "v07/marnietitfuck04.png"
        pause 0.025
        "v07/marnietitfuck05.png"
        pause 0.025
        "v07/marnietitfuck06.png"
        pause 0.025
        "v07/marnietitfuck07.png"
        pause 0.025
        "v07/marnietitfuck08.png"
        pause 0.025
        "v07/marnietitfuck09.png"
        pause 0.025
        "v07/marnietitfuck10.png"
        pause 0.025
        "v07/marnietitfuck11.png"
        pause 0.025
        "v07/marnietitfuck10.png"
        pause 0.025
        "v07/marnietitfuck09.png"
        pause 0.025
        "v07/marnietitfuck08.png"
        pause 0.025
        "v07/marnietitfuck07.png"
        pause 0.025
        "v07/marnietitfuck06.png"
        pause 0.025
        "v07/marnietitfuck05.png"
        pause 0.025
        "v07/marnietitfuck04.png"
        pause 0.025
        "v07/marnietitfuck03.png"
        pause 0.025
        "v07/marnietitfuck02.png"
        pause 0.025
        "v07/marnietitfuck01.png"
        pause 0.025
        repeat
            
    image marniehandjobslow:
        "v07/marniehandjob00.png"
        pause 0.035
        "v07/marniehandjob01.png"
        pause 0.035
        "v07/marniehandjob02.png"
        pause 0.035
        "v07/marniehandjob03.png"
        pause 0.035
        "v07/marniehandjob04.png"
        pause 0.035
        "v07/marniehandjob05.png"
        pause 0.035
        "v07/marniehandjob06.png"
        pause 0.035
        "v07/marniehandjob07.png"
        pause 0.035
        "v07/marniehandjob08.png"
        pause 0.035
        "v07/marniehandjob09.png"
        pause 0.035
        "v07/marniehandjob10.png"
        pause 0.035
        "v07/marniehandjob11.png"
        pause 0.035
        "v07/marniehandjob12.png"
        pause 0.035
        "v07/marniehandjob11.png"
        pause 0.035
        "v07/marniehandjob10.png"
        pause 0.035
        "v07/marniehandjob09.png"
        pause 0.035
        "v07/marniehandjob08.png"
        pause 0.035
        "v07/marniehandjob07.png"
        pause 0.035
        "v07/marniehandjob06.png"
        pause 0.035
        "v07/marniehandjob05.png"
        pause 0.035
        "v07/marniehandjob04.png"
        pause 0.035
        "v07/marniehandjob03.png"
        pause 0.035
        "v07/marniehandjob02.png"
        pause 0.035
        "v07/marniehandjob01.png"
        pause 0.035
        repeat
        
    image marniehandjobfast:
        "v07/marniehandjob00.png"
        pause 0.025
        "v07/marniehandjob01.png"
        pause 0.025
        "v07/marniehandjob02.png"
        pause 0.025
        "v07/marniehandjob03.png"
        pause 0.025
        "v07/marniehandjob04.png"
        pause 0.025
        "v07/marniehandjob05.png"
        pause 0.025
        "v07/marniehandjob06.png"
        pause 0.025
        "v07/marniehandjob07.png"
        pause 0.025
        "v07/marniehandjob08.png"
        pause 0.025
        "v07/marniehandjob09.png"
        pause 0.025
        "v07/marniehandjob10.png"
        pause 0.025
        "v07/marniehandjob11.png"
        pause 0.025
        "v07/marniehandjob12.png"
        pause 0.025
        "v07/marniehandjob11.png"
        pause 0.025
        "v07/marniehandjob10.png"
        pause 0.025
        "v07/marniehandjob09.png"
        pause 0.025
        "v07/marniehandjob08.png"
        pause 0.025
        "v07/marniehandjob07.png"
        pause 0.025
        "v07/marniehandjob06.png"
        pause 0.025
        "v07/marniehandjob05.png"
        pause 0.025
        "v07/marniehandjob04.png"
        pause 0.025
        "v07/marniehandjob03.png"
        pause 0.025
        "v07/marniehandjob02.png"
        pause 0.025
        "v07/marniehandjob01.png"
        pause 0.025
        repeat
            
    image marnieanalslow:
        "v07/marnieanal00.png"
        pause 0.035
        "v07/marnieanal01.png"
        pause 0.035
        "v07/marnieanal02.png"
        pause 0.035
        "v07/marnieanal03.png"
        pause 0.035
        "v07/marnieanal04.png"
        pause 0.035
        "v07/marnieanal05.png"
        pause 0.035
        "v07/marnieanal06.png"
        pause 0.035
        "v07/marnieanal07.png"
        pause 0.035
        "v07/marnieanal08.png"
        pause 0.035
        "v07/marnieanal09.png"
        pause 0.035
        "v07/marnieanal10.png"
        pause 0.05
        "v07/marnieanal09.png"
        pause 0.04
        "v07/marnieanal08.png"
        pause 0.04
        "v07/marnieanal07.png"
        pause 0.04
        "v07/marnieanal06.png"
        pause 0.04
        "v07/marnieanal05.png"
        pause 0.04
        "v07/marnieanal04.png"
        pause 0.04
        "v07/marnieanal03.png"
        pause 0.04
        "v07/marnieanal02.png"
        pause 0.04
        "v07/marnieanal01.png"
        pause 0.04
        repeat
        
    image marnieanalfast:
        "v07/marnieanal00.png"
        pause 0.025
        "v07/marnieanal01.png"
        pause 0.025
        "v07/marnieanal02.png"
        pause 0.025
        "v07/marnieanal03.png"
        pause 0.025
        "v07/marnieanal04.png"
        pause 0.025
        "v07/marnieanal05.png"
        pause 0.025
        "v07/marnieanal06.png"
        pause 0.025
        "v07/marnieanal07.png"
        pause 0.025
        "v07/marnieanal08.png"
        pause 0.025
        "v07/marnieanal09.png"
        pause 0.025
        "v07/marnieanal10.png"
        pause 0.04
        "v07/marnieanal09.png"
        pause 0.03
        "v07/marnieanal08.png"
        pause 0.03
        "v07/marnieanal07.png"
        pause 0.03
        "v07/marnieanal06.png"
        pause 0.03
        "v07/marnieanal05.png"
        pause 0.03
        "v07/marnieanal04.png"
        pause 0.03
        "v07/marnieanal03.png"
        pause 0.03
        "v07/marnieanal02.png"
        pause 0.03
        "v07/marnieanal01.png"
        pause 0.03
        repeat
            
    image marnieanalpovslow:
        "v07/marnieanalb00.png"
        pause 0.035
        "v07/marnieanalb01.png"
        pause 0.035
        "v07/marnieanalb02.png"
        pause 0.035
        "v07/marnieanalb03.png"
        pause 0.035
        "v07/marnieanalb04.png"
        pause 0.035
        "v07/marnieanalb05.png"
        pause 0.035
        "v07/marnieanalb06.png"
        pause 0.035
        "v07/marnieanalb07.png"
        pause 0.035
        "v07/marnieanalb08.png"
        pause 0.035
        "v07/marnieanalb09.png"
        pause 0.035
        "v07/marnieanalb10.png"
        pause 0.05
        "v07/marnieanalb09.png"
        pause 0.04
        "v07/marnieanalb08.png"
        pause 0.04
        "v07/marnieanalb07.png"
        pause 0.04
        "v07/marnieanalb06.png"
        pause 0.04
        "v07/marnieanalb05.png"
        pause 0.04
        "v07/marnieanalb04.png"
        pause 0.04
        "v07/marnieanalb03.png"
        pause 0.04
        "v07/marnieanalb02.png"
        pause 0.04
        "v07/marnieanalb01.png"
        pause 0.04
        repeat
        
    image marnieanalpovfast:
        "v07/marnieanalb00.png"
        pause 0.025
        "v07/marnieanalb01.png"
        pause 0.025
        "v07/marnieanalb02.png"
        pause 0.025
        "v07/marnieanalb03.png"
        pause 0.025
        "v07/marnieanalb04.png"
        pause 0.025
        "v07/marnieanalb05.png"
        pause 0.025
        "v07/marnieanalb06.png"
        pause 0.025
        "v07/marnieanalb07.png"
        pause 0.025
        "v07/marnieanalb08.png"
        pause 0.025
        "v07/marnieanalb09.png"
        pause 0.025
        "v07/marnieanalb10.png"
        pause 0.04
        "v07/marnieanalb09.png"
        pause 0.03
        "v07/marnieanalb08.png"
        pause 0.03
        "v07/marnieanalb07.png"
        pause 0.03
        "v07/marnieanalb06.png"
        pause 0.03
        "v07/marnieanalb05.png"
        pause 0.03
        "v07/marnieanalb04.png"
        pause 0.03
        "v07/marnieanalb03.png"
        pause 0.03
        "v07/marnieanalb02.png"
        pause 0.03
        "v07/marnieanalb01.png"
        pause 0.03
        repeat
            
    image angiepregnantslow:
        "v07/angieimpregnate00.png"
        pause 0.035
        "v07/angieimpregnate01.png"
        pause 0.035
        "v07/angieimpregnate02.png"
        pause 0.035
        "v07/angieimpregnate03.png"
        pause 0.035
        "v07/angieimpregnate04.png"
        pause 0.035
        "v07/angieimpregnate05.png"
        pause 0.035
        "v07/angieimpregnate06.png"
        pause 0.035
        "v07/angieimpregnate07.png"
        pause 0.035
        "v07/angieimpregnate08.png"
        pause 0.035
        "v07/angieimpregnate09.png"
        pause 0.035
        "v07/angieimpregnate10.png"
        pause 0.035
        "v07/angieimpregnate11.png"
        pause 0.035
        "v07/angieimpregnate12.png"
        pause 0.035
        "v07/angieimpregnate11.png"
        pause 0.035
        "v07/angieimpregnate10.png"
        pause 0.035
        "v07/angieimpregnate09.png"
        pause 0.035
        "v07/angieimpregnate08.png"
        pause 0.035
        "v07/angieimpregnate07.png"
        pause 0.035
        "v07/angieimpregnate06.png"
        pause 0.035
        "v07/angieimpregnate05.png"
        pause 0.035
        "v07/angieimpregnate04.png"
        pause 0.035
        "v07/angieimpregnate03.png"
        pause 0.035
        "v07/angieimpregnate02.png"
        pause 0.035
        "v07/angieimpregnate01.png"
        pause 0.035
        repeat
 
    image angiepregnantfast:
        "v07/angieimpregnate00.png"
        pause 0.025
        "v07/angieimpregnate01.png"
        pause 0.025
        "v07/angieimpregnate02.png"
        pause 0.025
        "v07/angieimpregnate03.png"
        pause 0.025
        "v07/angieimpregnate04.png"
        pause 0.025
        "v07/angieimpregnate05.png"
        pause 0.025
        "v07/angieimpregnate06.png"
        pause 0.025
        "v07/angieimpregnate07.png"
        pause 0.025
        "v07/angieimpregnate08.png"
        pause 0.025
        "v07/angieimpregnate09.png"
        pause 0.025
        "v07/angieimpregnate10.png"
        pause 0.025
        "v07/angieimpregnate11.png"
        pause 0.025
        "v07/angieimpregnate12.png"
        pause 0.025
        "v07/angieimpregnate11.png"
        pause 0.025
        "v07/angieimpregnate10.png"
        pause 0.025
        "v07/angieimpregnate09.png"
        pause 0.025
        "v07/angieimpregnate08.png"
        pause 0.025
        "v07/angieimpregnate07.png"
        pause 0.025
        "v07/angieimpregnate06.png"
        pause 0.025
        "v07/angieimpregnate05.png"
        pause 0.025
        "v07/angieimpregnate04.png"
        pause 0.025
        "v07/angieimpregnate03.png"
        pause 0.025
        "v07/angieimpregnate02.png"
        pause 0.025
        "v07/angieimpregnate01.png"
        pause 0.025
        repeat
            
    image angiepregnantpussyslow:
        "v07/angieimpregnatepussy00.png"
        pause 0.035
        "v07/angieimpregnatepussy01.png"
        pause 0.035
        "v07/angieimpregnatepussy02.png"
        pause 0.035
        "v07/angieimpregnatepussy03.png"
        pause 0.035
        "v07/angieimpregnatepussy04.png"
        pause 0.035
        "v07/angieimpregnatepussy05.png"
        pause 0.035
        "v07/angieimpregnatepussy06.png"
        pause 0.035
        "v07/angieimpregnatepussy07.png"
        pause 0.035
        "v07/angieimpregnatepussy08.png"
        pause 0.035
        "v07/angieimpregnatepussy09.png"
        pause 0.035
        "v07/angieimpregnatepussy10.png"
        pause 0.035
        "v07/angieimpregnatepussy11.png"
        pause 0.035
        "v07/angieimpregnatepussy12.png"
        pause 0.035
        "v07/angieimpregnatepussy11.png"
        pause 0.035
        "v07/angieimpregnatepussy10.png"
        pause 0.035
        "v07/angieimpregnatepussy09.png"
        pause 0.035
        "v07/angieimpregnatepussy08.png"
        pause 0.035
        "v07/angieimpregnatepussy07.png"
        pause 0.035
        "v07/angieimpregnatepussy06.png"
        pause 0.035
        "v07/angieimpregnatepussy05.png"
        pause 0.035
        "v07/angieimpregnatepussy04.png"
        pause 0.035
        "v07/angieimpregnatepussy03.png"
        pause 0.035
        "v07/angieimpregnatepussy02.png"
        pause 0.035
        "v07/angieimpregnatepussy01.png"
        pause 0.035
        repeat
 
    image angiepregnantpussyfast:
        "v07/angieimpregnatepussy00.png"
        pause 0.025
        "v07/angieimpregnatepussy01.png"
        pause 0.025
        "v07/angieimpregnatepussy02.png"
        pause 0.025
        "v07/angieimpregnatepussy03.png"
        pause 0.025
        "v07/angieimpregnatepussy04.png"
        pause 0.025
        "v07/angieimpregnatepussy05.png"
        pause 0.025
        "v07/angieimpregnatepussy06.png"
        pause 0.025
        "v07/angieimpregnatepussy07.png"
        pause 0.025
        "v07/angieimpregnatepussy08.png"
        pause 0.025
        "v07/angieimpregnatepussy09.png"
        pause 0.025
        "v07/angieimpregnatepussy10.png"
        pause 0.025
        "v07/angieimpregnatepussy11.png"
        pause 0.025
        "v07/angieimpregnatepussy12.png"
        pause 0.025
        "v07/angieimpregnatepussy11.png"
        pause 0.025
        "v07/angieimpregnatepussy10.png"
        pause 0.025
        "v07/angieimpregnatepussy09.png"
        pause 0.025
        "v07/angieimpregnatepussy08.png"
        pause 0.025
        "v07/angieimpregnatepussy07.png"
        pause 0.025
        "v07/angieimpregnatepussy06.png"
        pause 0.025
        "v07/angieimpregnatepussy05.png"
        pause 0.025
        "v07/angieimpregnatepussy04.png"
        pause 0.025
        "v07/angieimpregnatepussy03.png"
        pause 0.025
        "v07/angieimpregnatepussy02.png"
        pause 0.025
        "v07/angieimpregnatepussy01.png"
        pause 0.025
        repeat

    image aylaimpregslow:
        "v071/aylaimpreg00.jpg"
        pause 0.035
        "v071/aylaimpreg01.jpg"
        pause 0.035
        "v071/aylaimpreg02.jpg"
        pause 0.035
        "v071/aylaimpreg03.jpg"
        pause 0.035
        "v071/aylaimpreg04.jpg"
        pause 0.035
        "v071/aylaimpreg05.jpg"
        pause 0.035
        "v071/aylaimpreg06.jpg"
        pause 0.035
        "v071/aylaimpreg07.jpg"
        pause 0.035
        "v071/aylaimpreg08.jpg"
        pause 0.035
        "v071/aylaimpreg09.jpg"
        pause 0.035
        "v071/aylaimpreg10.jpg"
        pause 0.035
        "v071/aylaimpreg09.jpg"
        pause 0.035
        "v071/aylaimpreg08.jpg"
        pause 0.035
        "v071/aylaimpreg07.jpg"
        pause 0.035
        "v071/aylaimpreg06.jpg"
        pause 0.035
        "v071/aylaimpreg05.jpg"
        pause 0.035
        "v071/aylaimpreg04.jpg"
        pause 0.035
        "v071/aylaimpreg03.jpg"
        pause 0.035
        "v071/aylaimpreg02.jpg"
        pause 0.035
        "v071/aylaimpreg01.jpg"
        pause 0.035
        repeat
            
    image aylaimpregfast:
        "v071/aylaimpreg00.jpg"
        pause 0.025
        "v071/aylaimpreg01.jpg"
        pause 0.025
        "v071/aylaimpreg02.jpg"
        pause 0.025
        "v071/aylaimpreg03.jpg"
        pause 0.025
        "v071/aylaimpreg04.jpg"
        pause 0.025
        "v071/aylaimpreg05.jpg"
        pause 0.025
        "v071/aylaimpreg06.jpg"
        pause 0.025
        "v071/aylaimpreg07.jpg"
        pause 0.025
        "v071/aylaimpreg08.jpg"
        pause 0.025
        "v071/aylaimpreg09.jpg"
        pause 0.025
        "v071/aylaimpreg10.jpg"
        pause 0.025
        "v071/aylaimpreg09.jpg"
        pause 0.025
        "v071/aylaimpreg08.jpg"
        pause 0.025
        "v071/aylaimpreg07.jpg"
        pause 0.025
        "v071/aylaimpreg06.jpg"
        pause 0.025
        "v071/aylaimpreg05.jpg"
        pause 0.025
        "v071/aylaimpreg04.jpg"
        pause 0.025
        "v071/aylaimpreg03.jpg"
        pause 0.025
        "v071/aylaimpreg02.jpg"
        pause 0.025
        "v071/aylaimpreg01.jpg"
        pause 0.025
        repeat

    image aylaimpregtopslow:
        "v071/aylaimpregtop00.jpg"
        pause 0.035
        "v071/aylaimpregtop01.jpg"
        pause 0.035
        "v071/aylaimpregtop02.jpg"
        pause 0.035
        "v071/aylaimpregtop03.jpg"
        pause 0.035
        "v071/aylaimpregtop04.jpg"
        pause 0.035
        "v071/aylaimpregtop05.jpg"
        pause 0.035
        "v071/aylaimpregtop06.jpg"
        pause 0.035
        "v071/aylaimpregtop07.jpg"
        pause 0.035
        "v071/aylaimpregtop08.jpg"
        pause 0.035
        "v071/aylaimpregtop09.jpg"
        pause 0.035
        "v071/aylaimpregtop10.jpg"
        pause 0.035
        "v071/aylaimpregtop09.jpg"
        pause 0.035
        "v071/aylaimpregtop08.jpg"
        pause 0.035
        "v071/aylaimpregtop07.jpg"
        pause 0.035
        "v071/aylaimpregtop06.jpg"
        pause 0.035
        "v071/aylaimpregtop05.jpg"
        pause 0.035
        "v071/aylaimpregtop04.jpg"
        pause 0.035
        "v071/aylaimpregtop03.jpg"
        pause 0.035
        "v071/aylaimpregtop02.jpg"
        pause 0.035
        "v071/aylaimpregtop01.jpg"
        pause 0.035
        repeat
            
    image aylaimpregtopfast:
        "v071/aylaimpregtop00.jpg"
        pause 0.025
        "v071/aylaimpregtop01.jpg"
        pause 0.025
        "v071/aylaimpregtop02.jpg"
        pause 0.025
        "v071/aylaimpregtop03.jpg"
        pause 0.025
        "v071/aylaimpregtop04.jpg"
        pause 0.025
        "v071/aylaimpregtop05.jpg"
        pause 0.025
        "v071/aylaimpregtop06.jpg"
        pause 0.025
        "v071/aylaimpregtop07.jpg"
        pause 0.025
        "v071/aylaimpregtop08.jpg"
        pause 0.025
        "v071/aylaimpregtop09.jpg"
        pause 0.025
        "v071/aylaimpregtop10.jpg"
        pause 0.025
        "v071/aylaimpregtop09.jpg"
        pause 0.025
        "v071/aylaimpregtop08.jpg"
        pause 0.025
        "v071/aylaimpregtop07.jpg"
        pause 0.025
        "v071/aylaimpregtop06.jpg"
        pause 0.025
        "v071/aylaimpregtop05.jpg"
        pause 0.025
        "v071/aylaimpregtop04.jpg"
        pause 0.025
        "v071/aylaimpregtop03.jpg"
        pause 0.025
        "v071/aylaimpregtop02.jpg"
        pause 0.025
        "v071/aylaimpregtop01.jpg"
        pause 0.025
        repeat
    
    image clarablowslow:
        "v071/clarablow00.png"
        pause 0.035
        "v071/clarablow01.png"
        pause 0.035
        "v071/clarablow02.png"
        pause 0.035
        "v071/clarablow03.png"
        pause 0.035
        "v071/clarablow04.png"
        pause 0.035
        "v071/clarablow05.png"
        pause 0.035
        "v071/clarablow06.png"
        pause 0.035
        "v071/clarablow07.png"
        pause 0.035
        "v071/clarablow08.png"
        pause 0.035
        "v071/clarablow09.png"
        pause 0.035
        "v071/clarablow10.png"
        pause 0.035
        "v071/clarablow11.png"
        pause 0.035
        "v071/clarablow12.png"
        pause 0.05
        "v071/clarablow11.png"
        pause 0.04
        "v071/clarablow10.png"
        pause 0.04
        "v071/clarablow09.png"
        pause 0.04
        "v071/clarablow08.png"
        pause 0.04
        "v071/clarablow07.png"
        pause 0.04
        "v071/clarablow06.png"
        pause 0.04
        "v071/clarablow05.png"
        pause 0.04
        "v071/clarablow04.png"
        pause 0.04
        "v071/clarablow03.png"
        pause 0.04
        "v071/clarablow02.png"
        pause 0.04
        "v071/clarablow01.png"
        pause 0.04
        repeat
            
    image clarablowfast:
        "v071/clarablow00.png"
        pause 0.025
        "v071/clarablow01.png"
        pause 0.025
        "v071/clarablow02.png"
        pause 0.025
        "v071/clarablow03.png"
        pause 0.025
        "v071/clarablow04.png"
        pause 0.025
        "v071/clarablow05.png"
        pause 0.025
        "v071/clarablow06.png"
        pause 0.025
        "v071/clarablow07.png"
        pause 0.025
        "v071/clarablow08.png"
        pause 0.025
        "v071/clarablow09.png"
        pause 0.025
        "v071/clarablow10.png"
        pause 0.025
        "v071/clarablow11.png"
        pause 0.025
        "v071/clarablow12.png"
        pause 0.04
        "v071/clarablow11.png"
        pause 0.035
        "v071/clarablow10.png"
        pause 0.035
        "v071/clarablow09.png"
        pause 0.035
        "v071/clarablow08.png"
        pause 0.035
        "v071/clarablow07.png"
        pause 0.035
        "v071/clarablow06.png"
        pause 0.035
        "v071/clarablow05.png"
        pause 0.035
        "v071/clarablow04.png"
        pause 0.035
        "v071/clarablow03.png"
        pause 0.035
        "v071/clarablow02.png"
        pause 0.035
        "v071/clarablow01.png"
        pause 0.035
        repeat
            
    image claratitfuckslow:
        "v071/claratitfuck00.jpg"
        pause 0.035
        "v071/claratitfuck01.jpg"
        pause 0.035
        "v071/claratitfuck02.jpg"
        pause 0.035
        "v071/claratitfuck03.jpg"
        pause 0.035
        "v071/claratitfuck04.jpg"
        pause 0.035
        "v071/claratitfuck05.jpg"
        pause 0.035
        "v071/claratitfuck06.jpg"
        pause 0.035
        "v071/claratitfuck07.jpg"
        pause 0.035
        "v071/claratitfuck08.jpg"
        pause 0.035
        "v071/claratitfuck09.jpg"
        pause 0.035
        "v071/claratitfuck10.jpg"
        pause 0.035
        "v071/claratitfuck11.jpg"
        pause 0.035
        "v071/claratitfuck10.jpg"
        pause 0.035
        "v071/claratitfuck09.jpg"
        pause 0.035
        "v071/claratitfuck08.jpg"
        pause 0.035
        "v071/claratitfuck07.jpg"
        pause 0.035
        "v071/claratitfuck06.jpg"
        pause 0.035
        "v071/claratitfuck05.jpg"
        pause 0.035
        "v071/claratitfuck04.jpg"
        pause 0.035
        "v071/claratitfuck03.jpg"
        pause 0.035
        "v071/claratitfuck02.jpg"
        pause 0.035
        "v071/claratitfuck01.jpg"
        pause 0.035
        repeat
            
    image claratitfuckfast:
        "v071/claratitfuck00.jpg"
        pause 0.025
        "v071/claratitfuck01.jpg"
        pause 0.025
        "v071/claratitfuck02.jpg"
        pause 0.025
        "v071/claratitfuck03.jpg"
        pause 0.025
        "v071/claratitfuck04.jpg"
        pause 0.025
        "v071/claratitfuck05.jpg"
        pause 0.025
        "v071/claratitfuck06.jpg"
        pause 0.025
        "v071/claratitfuck07.jpg"
        pause 0.025
        "v071/claratitfuck08.jpg"
        pause 0.025
        "v071/claratitfuck09.jpg"
        pause 0.025
        "v071/claratitfuck10.jpg"
        pause 0.025
        "v071/claratitfuck11.jpg"
        pause 0.025
        "v071/claratitfuck10.jpg"
        pause 0.025
        "v071/claratitfuck09.jpg"
        pause 0.025
        "v071/claratitfuck08.jpg"
        pause 0.025
        "v071/claratitfuck07.jpg"
        pause 0.025
        "v071/claratitfuck06.jpg"
        pause 0.025
        "v071/claratitfuck05.jpg"
        pause 0.025
        "v071/claratitfuck04.jpg"
        pause 0.025
        "v071/claratitfuck03.jpg"
        pause 0.025
        "v071/claratitfuck02.jpg"
        pause 0.025
        "v071/claratitfuck01.jpg"
        pause 0.025
        repeat
            
    image claratitfuckpovslow:
        "v071/claratitfuckpov00.jpg"
        pause 0.035
        "v071/claratitfuckpov01.jpg"
        pause 0.035
        "v071/claratitfuckpov02.jpg"
        pause 0.035
        "v071/claratitfuckpov03.jpg"
        pause 0.035
        "v071/claratitfuckpov04.jpg"
        pause 0.035
        "v071/claratitfuckpov05.jpg"
        pause 0.035
        "v071/claratitfuckpov06.jpg"
        pause 0.035
        "v071/claratitfuckpov07.jpg"
        pause 0.035
        "v071/claratitfuckpov08.jpg"
        pause 0.035
        "v071/claratitfuckpov09.jpg"
        pause 0.035
        "v071/claratitfuckpov10.jpg"
        pause 0.035
        "v071/claratitfuckpov11.jpg"
        pause 0.035
        "v071/claratitfuckpov10.jpg"
        pause 0.035
        "v071/claratitfuckpov09.jpg"
        pause 0.035
        "v071/claratitfuckpov08.jpg"
        pause 0.035
        "v071/claratitfuckpov07.jpg"
        pause 0.035
        "v071/claratitfuckpov06.jpg"
        pause 0.035
        "v071/claratitfuckpov05.jpg"
        pause 0.035
        "v071/claratitfuckpov04.jpg"
        pause 0.035
        "v071/claratitfuckpov03.jpg"
        pause 0.035
        "v071/claratitfuckpov02.jpg"
        pause 0.035
        "v071/claratitfuckpov01.jpg"
        pause 0.035
        repeat
            
    image claratitfuckpovfast:
        "v071/claratitfuckpov00.jpg"
        pause 0.025
        "v071/claratitfuckpov01.jpg"
        pause 0.025
        "v071/claratitfuckpov02.jpg"
        pause 0.025
        "v071/claratitfuckpov03.jpg"
        pause 0.025
        "v071/claratitfuckpov04.jpg"
        pause 0.025
        "v071/claratitfuckpov05.jpg"
        pause 0.025
        "v071/claratitfuckpov06.jpg"
        pause 0.025
        "v071/claratitfuckpov07.jpg"
        pause 0.025
        "v071/claratitfuckpov08.jpg"
        pause 0.025
        "v071/claratitfuckpov09.jpg"
        pause 0.025
        "v071/claratitfuckpov10.jpg"
        pause 0.025
        "v071/claratitfuckpov11.jpg"
        pause 0.025
        "v071/claratitfuckpov10.jpg"
        pause 0.025
        "v071/claratitfuckpov09.jpg"
        pause 0.025
        "v071/claratitfuckpov08.jpg"
        pause 0.025
        "v071/claratitfuckpov07.jpg"
        pause 0.025
        "v071/claratitfuckpov06.jpg"
        pause 0.025
        "v071/claratitfuckpov05.jpg"
        pause 0.025
        "v071/claratitfuckpov04.jpg"
        pause 0.025
        "v071/claratitfuckpov03.jpg"
        pause 0.025
        "v071/claratitfuckpov02.jpg"
        pause 0.025
        "v071/claratitfuckpov01.jpg"
        pause 0.025
        repeat
            
    image claramissionaryslow:
        "v071/claramissionary00.jpg"
        pause 0.035
        "v071/claramissionary01.jpg"
        pause 0.035
        "v071/claramissionary02.jpg"
        pause 0.035
        "v071/claramissionary03.jpg"
        pause 0.035
        "v071/claramissionary04.jpg"
        pause 0.035
        "v071/claramissionary05.jpg"
        pause 0.035
        "v071/claramissionary06.jpg"
        pause 0.035
        "v071/claramissionary07.jpg"
        pause 0.035
        "v071/claramissionary08.jpg"
        pause 0.035
        "v071/claramissionary09.jpg"
        pause 0.035
        "v071/claramissionary10.jpg"
        pause 0.035
        "v071/claramissionary11.jpg"
        pause 0.035
        "v071/claramissionary10.jpg"
        pause 0.035
        "v071/claramissionary09.jpg"
        pause 0.035
        "v071/claramissionary08.jpg"
        pause 0.035
        "v071/claramissionary07.jpg"
        pause 0.035
        "v071/claramissionary06.jpg"
        pause 0.035
        "v071/claramissionary05.jpg"
        pause 0.035
        "v071/claramissionary04.jpg"
        pause 0.035
        "v071/claramissionary03.jpg"
        pause 0.035
        "v071/claramissionary02.jpg"
        pause 0.035
        "v071/claramissionary01.jpg"
        pause 0.035
        repeat
            
    image claramissionaryfast:
        "v071/claramissionary00.jpg"
        pause 0.025
        "v071/claramissionary01.jpg"
        pause 0.025
        "v071/claramissionary02.jpg"
        pause 0.025
        "v071/claramissionary03.jpg"
        pause 0.025
        "v071/claramissionary04.jpg"
        pause 0.025
        "v071/claramissionary05.jpg"
        pause 0.025
        "v071/claramissionary06.jpg"
        pause 0.025
        "v071/claramissionary07.jpg"
        pause 0.025
        "v071/claramissionary08.jpg"
        pause 0.025
        "v071/claramissionary09.jpg"
        pause 0.025
        "v071/claramissionary10.jpg"
        pause 0.025
        "v071/claramissionary11.jpg"
        pause 0.025
        "v071/claramissionary10.jpg"
        pause 0.025
        "v071/claramissionary09.jpg"
        pause 0.025
        "v071/claramissionary08.jpg"
        pause 0.025
        "v071/claramissionary07.jpg"
        pause 0.025
        "v071/claramissionary06.jpg"
        pause 0.025
        "v071/claramissionary05.jpg"
        pause 0.025
        "v071/claramissionary04.jpg"
        pause 0.025
        "v071/claramissionary03.jpg"
        pause 0.025
        "v071/claramissionary02.jpg"
        pause 0.025
        "v071/claramissionary01.jpg"
        pause 0.025
        repeat
            
    image claraanalslow:
        "v071/claraanal00.jpg"
        pause 0.035
        "v071/claraanal01.jpg"
        pause 0.035
        "v071/claraanal02.jpg"
        pause 0.035
        "v071/claraanal03.jpg"
        pause 0.035
        "v071/claraanal04.jpg"
        pause 0.035
        "v071/claraanal05.jpg"
        pause 0.035
        "v071/claraanal06.jpg"
        pause 0.035
        "v071/claraanal07.jpg"
        pause 0.035
        "v071/claraanal08.jpg"
        pause 0.035
        "v071/claraanal09.jpg"
        pause 0.035
        "v071/claraanal10.jpg"
        pause 0.035
        "v071/claraanal11.jpg"
        pause 0.035
        "v071/claraanal12.jpg"
        pause 0.035
        "v071/claraanal11.jpg"
        pause 0.035
        "v071/claraanal10.jpg"
        pause 0.035
        "v071/claraanal09.jpg"
        pause 0.035
        "v071/claraanal08.jpg"
        pause 0.035
        "v071/claraanal07.jpg"
        pause 0.035
        "v071/claraanal06.jpg"
        pause 0.035
        "v071/claraanal05.jpg"
        pause 0.035
        "v071/claraanal04.jpg"
        pause 0.035
        "v071/claraanal03.jpg"
        pause 0.035
        "v071/claraanal02.jpg"
        pause 0.035
        "v071/claraanal01.jpg"
        pause 0.035
        repeat
            
    image claraanalfast:
        "v071/claraanal00.jpg"
        pause 0.025
        "v071/claraanal01.jpg"
        pause 0.025
        "v071/claraanal02.jpg"
        pause 0.025
        "v071/claraanal03.jpg"
        pause 0.025
        "v071/claraanal04.jpg"
        pause 0.025
        "v071/claraanal05.jpg"
        pause 0.025
        "v071/claraanal06.jpg"
        pause 0.025
        "v071/claraanal07.jpg"
        pause 0.025
        "v071/claraanal08.jpg"
        pause 0.025
        "v071/claraanal09.jpg"
        pause 0.025
        "v071/claraanal10.jpg"
        pause 0.025
        "v071/claraanal11.jpg"
        pause 0.025
        "v071/claraanal12.jpg"
        pause 0.025
        "v071/claraanal11.jpg"
        pause 0.025
        "v071/claraanal10.jpg"
        pause 0.025
        "v071/claraanal09.jpg"
        pause 0.025
        "v071/claraanal08.jpg"
        pause 0.025
        "v071/claraanal07.jpg"
        pause 0.025
        "v071/claraanal06.jpg"
        pause 0.025
        "v071/claraanal05.jpg"
        pause 0.025
        "v071/claraanal04.jpg"
        pause 0.025
        "v071/claraanal03.jpg"
        pause 0.025
        "v071/claraanal02.jpg"
        pause 0.025
        "v071/claraanal01.jpg"
        pause 0.025
        repeat
            
    image clarafuckslow:
        "v071/clarafuck00.png"
        pause 0.035
        "v071/clarafuck01.png"
        pause 0.035
        "v071/clarafuck02.png"
        pause 0.035
        "v071/clarafuck03.png"
        pause 0.035
        "v071/clarafuck04.png"
        pause 0.035
        "v071/clarafuck05.png"
        pause 0.035
        "v071/clarafuck06.png"
        pause 0.035
        "v071/clarafuck07.png"
        pause 0.035
        "v071/clarafuck08.png"
        pause 0.035
        "v071/clarafuck09.png"
        pause 0.035
        "v071/clarafuck10.png"
        pause 0.035
        "v071/clarafuck11.png"
        pause 0.035
        "v071/clarafuck12.png"
        pause 0.035
        "v071/clarafuck11.png"
        pause 0.035
        "v071/clarafuck10.png"
        pause 0.035
        "v071/clarafuck09.png"
        pause 0.035
        "v071/clarafuck08.png"
        pause 0.035
        "v071/clarafuck07.png"
        pause 0.035
        "v071/clarafuck06.png"
        pause 0.035
        "v071/clarafuck05.png"
        pause 0.035
        "v071/clarafuck04.png"
        pause 0.035
        "v071/clarafuck03.png"
        pause 0.035
        "v071/clarafuck02.png"
        pause 0.035
        "v071/clarafuck01.png"
        pause 0.035
        repeat
            
    image clarafuckfast:
        "v071/clarafuck00.png"
        pause 0.025
        "v071/clarafuck01.png"
        pause 0.025
        "v071/clarafuck02.png"
        pause 0.025
        "v071/clarafuck03.png"
        pause 0.025
        "v071/clarafuck04.png"
        pause 0.025
        "v071/clarafuck05.png"
        pause 0.025
        "v071/clarafuck06.png"
        pause 0.025
        "v071/clarafuck07.png"
        pause 0.025
        "v071/clarafuck08.png"
        pause 0.025
        "v071/clarafuck09.png"
        pause 0.025
        "v071/clarafuck10.png"
        pause 0.025
        "v071/clarafuck11.png"
        pause 0.025
        "v071/clarafuck12.png"
        pause 0.025
        "v071/clarafuck11.png"
        pause 0.025
        "v071/clarafuck10.png"
        pause 0.025
        "v071/clarafuck09.png"
        pause 0.025
        "v071/clarafuck08.png"
        pause 0.025
        "v071/clarafuck07.png"
        pause 0.025
        "v071/clarafuck06.png"
        pause 0.025
        "v071/clarafuck05.png"
        pause 0.025
        "v071/clarafuck04.png"
        pause 0.025
        "v071/clarafuck03.png"
        pause 0.025
        "v071/clarafuck02.png"
        pause 0.025
        "v071/clarafuck01.png"
        pause 0.025
        repeat
            
    image clarafucktopslow:
        "v071/clarafucktop00.jpg"
        pause 0.035
        "v071/clarafucktop01.jpg"
        pause 0.035
        "v071/clarafucktop02.jpg"
        pause 0.035
        "v071/clarafucktop03.jpg"
        pause 0.035
        "v071/clarafucktop04.jpg"
        pause 0.035
        "v071/clarafucktop05.jpg"
        pause 0.035
        "v071/clarafucktop06.jpg"
        pause 0.035
        "v071/clarafucktop07.jpg"
        pause 0.035
        "v071/clarafucktop08.jpg"
        pause 0.035
        "v071/clarafucktop09.jpg"
        pause 0.035
        "v071/clarafucktop10.jpg"
        pause 0.035
        "v071/clarafucktop11.jpg"
        pause 0.035
        "v071/clarafucktop12.jpg"
        pause 0.035
        "v071/clarafucktop11.jpg"
        pause 0.035
        "v071/clarafucktop10.jpg"
        pause 0.035
        "v071/clarafucktop09.jpg"
        pause 0.035
        "v071/clarafucktop08.jpg"
        pause 0.035
        "v071/clarafucktop07.jpg"
        pause 0.035
        "v071/clarafucktop06.jpg"
        pause 0.035
        "v071/clarafucktop05.jpg"
        pause 0.035
        "v071/clarafucktop04.jpg"
        pause 0.035
        "v071/clarafucktop03.jpg"
        pause 0.035
        "v071/clarafucktop02.jpg"
        pause 0.035
        "v071/clarafucktop01.jpg"
        pause 0.035
        repeat
            
    image clarafucktopfast:
        "v071/clarafucktop00.jpg"
        pause 0.025
        "v071/clarafucktop01.jpg"
        pause 0.025
        "v071/clarafucktop02.jpg"
        pause 0.025
        "v071/clarafucktop03.jpg"
        pause 0.025
        "v071/clarafucktop04.jpg"
        pause 0.025
        "v071/clarafucktop05.jpg"
        pause 0.025
        "v071/clarafucktop06.jpg"
        pause 0.025
        "v071/clarafucktop07.jpg"
        pause 0.025
        "v071/clarafucktop08.jpg"
        pause 0.025
        "v071/clarafucktop09.jpg"
        pause 0.025
        "v071/clarafucktop10.jpg"
        pause 0.025
        "v071/clarafucktop11.jpg"
        pause 0.025
        "v071/clarafucktop12.jpg"
        pause 0.025
        "v071/clarafucktop11.jpg"
        pause 0.025
        "v071/clarafucktop10.jpg"
        pause 0.025
        "v071/clarafucktop09.jpg"
        pause 0.025
        "v071/clarafucktop08.jpg"
        pause 0.025
        "v071/clarafucktop07.jpg"
        pause 0.025
        "v071/clarafucktop06.jpg"
        pause 0.025
        "v071/clarafucktop05.jpg"
        pause 0.025
        "v071/clarafucktop04.jpg"
        pause 0.025
        "v071/clarafucktop03.jpg"
        pause 0.025
        "v071/clarafucktop02.jpg"
        pause 0.025
        "v071/clarafucktop01.jpg"
        pause 0.025
        repeat
            
    image clarahugeslow:
        "v071/clarahuge00.png"
        pause 0.035
        "v071/clarahuge01.png"
        pause 0.035
        "v071/clarahuge02.png"
        pause 0.035
        "v071/clarahuge03.png"
        pause 0.035
        "v071/clarahuge04.png"
        pause 0.035
        "v071/clarahuge05.png"
        pause 0.035
        "v071/clarahuge06.png"
        pause 0.035
        "v071/clarahuge07.png"
        pause 0.035
        "v071/clarahuge08.png"
        pause 0.035
        "v071/clarahuge09.png"
        pause 0.035
        "v071/clarahuge10.png"
        pause 0.035
        "v071/clarahuge11.png"
        pause 0.035
        "v071/clarahuge12.png"
        pause 0.035
        "v071/clarahuge11.png"
        pause 0.035
        "v071/clarahuge10.png"
        pause 0.035
        "v071/clarahuge09.png"
        pause 0.035
        "v071/clarahuge08.png"
        pause 0.035
        "v071/clarahuge07.png"
        pause 0.035
        "v071/clarahuge06.png"
        pause 0.035
        "v071/clarahuge05.png"
        pause 0.035
        "v071/clarahuge04.png"
        pause 0.035
        "v071/clarahuge03.png"
        pause 0.035
        "v071/clarahuge02.png"
        pause 0.035
        "v071/clarahuge01.png"
        pause 0.035
        repeat
            
    image clarahugefast:
        "v071/clarahuge00.png"
        pause 0.025
        "v071/clarahuge01.png"
        pause 0.025
        "v071/clarahuge02.png"
        pause 0.025
        "v071/clarahuge03.png"
        pause 0.025
        "v071/clarahuge04.png"
        pause 0.025
        "v071/clarahuge05.png"
        pause 0.025
        "v071/clarahuge06.png"
        pause 0.025
        "v071/clarahuge07.png"
        pause 0.025
        "v071/clarahuge08.png"
        pause 0.025
        "v071/clarahuge09.png"
        pause 0.025
        "v071/clarahuge10.png"
        pause 0.025
        "v071/clarahuge11.png"
        pause 0.025
        "v071/clarahuge12.png"
        pause 0.025
        "v071/clarahuge11.png"
        pause 0.025
        "v071/clarahuge10.png"
        pause 0.025
        "v071/clarahuge09.png"
        pause 0.025
        "v071/clarahuge08.png"
        pause 0.025
        "v071/clarahuge07.png"
        pause 0.025
        "v071/clarahuge06.png"
        pause 0.025
        "v071/clarahuge05.png"
        pause 0.025
        "v071/clarahuge04.png"
        pause 0.025
        "v071/clarahuge03.png"
        pause 0.025
        "v071/clarahuge02.png"
        pause 0.025
        "v071/clarahuge01.png"
        pause 0.025
        repeat
            
    image aliens01fuckslow:
        "v071/aliensfuckanimb00.jpg"
        pause 0.035
        "v071/aliensfuckanimb01.jpg"
        pause 0.035
        "v071/aliensfuckanimb02.jpg"
        pause 0.035
        "v071/aliensfuckanimb03.jpg"
        pause 0.035
        "v071/aliensfuckanimb04.jpg"
        pause 0.035
        "v071/aliensfuckanimb05.jpg"
        pause 0.035
        "v071/aliensfuckanimb06.jpg"
        pause 0.035
        "v071/aliensfuckanimb07.jpg"
        pause 0.035
        "v071/aliensfuckanimb08.jpg"
        pause 0.035
        "v071/aliensfuckanimb09.jpg"
        pause 0.035
        "v071/aliensfuckanimb10.jpg"
        pause 0.035
        "v071/aliensfuckanimb11.jpg"
        pause 0.035
        "v071/aliensfuckanimb12.jpg"
        pause 0.035
        "v071/aliensfuckanimb11.jpg"
        pause 0.035
        "v071/aliensfuckanimb10.jpg"
        pause 0.035
        "v071/aliensfuckanimb09.jpg"
        pause 0.035
        "v071/aliensfuckanimb08.jpg"
        pause 0.035
        "v071/aliensfuckanimb07.jpg"
        pause 0.035
        "v071/aliensfuckanimb06.jpg"
        pause 0.035
        "v071/aliensfuckanimb05.jpg"
        pause 0.035
        "v071/aliensfuckanimb04.jpg"
        pause 0.035
        "v071/aliensfuckanimb03.jpg"
        pause 0.035
        "v071/aliensfuckanimb02.jpg"
        pause 0.035
        "v071/aliensfuckanimb01.jpg"
        pause 0.035
        repeat
            
    image aliens01fuckfast:
        "v071/aliensfuckanimb00.jpg"
        pause 0.025
        "v071/aliensfuckanimb01.jpg"
        pause 0.025
        "v071/aliensfuckanimb02.jpg"
        pause 0.025
        "v071/aliensfuckanimb03.jpg"
        pause 0.025
        "v071/aliensfuckanimb04.jpg"
        pause 0.025
        "v071/aliensfuckanimb05.jpg"
        pause 0.025
        "v071/aliensfuckanimb06.jpg"
        pause 0.025
        "v071/aliensfuckanimb07.jpg"
        pause 0.025
        "v071/aliensfuckanimb08.jpg"
        pause 0.025
        "v071/aliensfuckanimb09.jpg"
        pause 0.025
        "v071/aliensfuckanimb10.jpg"
        pause 0.025
        "v071/aliensfuckanimb11.jpg"
        pause 0.025
        "v071/aliensfuckanimb12.jpg"
        pause 0.025
        "v071/aliensfuckanimb11.jpg"
        pause 0.025
        "v071/aliensfuckanimb10.jpg"
        pause 0.025
        "v071/aliensfuckanimb09.jpg"
        pause 0.025
        "v071/aliensfuckanimb08.jpg"
        pause 0.025
        "v071/aliensfuckanimb07.jpg"
        pause 0.025
        "v071/aliensfuckanimb06.jpg"
        pause 0.025
        "v071/aliensfuckanimb05.jpg"
        pause 0.025
        "v071/aliensfuckanimb04.jpg"
        pause 0.025
        "v071/aliensfuckanimb03.jpg"
        pause 0.025
        "v071/aliensfuckanimb02.jpg"
        pause 0.025
        "v071/aliensfuckanimb01.jpg"
        pause 0.025
        repeat
            
    image aliens02fuckslow:
        "v071/aliens02fuckanim00.jpg"
        pause 0.035
        "v071/aliens02fuckanim01.jpg"
        pause 0.035
        "v071/aliens02fuckanim02.jpg"
        pause 0.035
        "v071/aliens02fuckanim03.jpg"
        pause 0.035
        "v071/aliens02fuckanim04.jpg"
        pause 0.035
        "v071/aliens02fuckanim05.jpg"
        pause 0.035
        "v071/aliens02fuckanim06.jpg"
        pause 0.035
        "v071/aliens02fuckanim07.jpg"
        pause 0.035
        "v071/aliens02fuckanim08.jpg"
        pause 0.035
        "v071/aliens02fuckanim09.jpg"
        pause 0.035
        "v071/aliens02fuckanim10.jpg"
        pause 0.035
        "v071/aliens02fuckanim11.jpg"
        pause 0.035
        "v071/aliens02fuckanim12.jpg"
        pause 0.035
        "v071/aliens02fuckanim11.jpg"
        pause 0.035
        "v071/aliens02fuckanim10.jpg"
        pause 0.035
        "v071/aliens02fuckanim09.jpg"
        pause 0.035
        "v071/aliens02fuckanim08.jpg"
        pause 0.035
        "v071/aliens02fuckanim07.jpg"
        pause 0.035
        "v071/aliens02fuckanim06.jpg"
        pause 0.035
        "v071/aliens02fuckanim05.jpg"
        pause 0.035
        "v071/aliens02fuckanim04.jpg"
        pause 0.035
        "v071/aliens02fuckanim03.jpg"
        pause 0.035
        "v071/aliens02fuckanim02.jpg"
        pause 0.035
        "v071/aliens02fuckanim01.jpg"
        pause 0.035
        repeat
            
    image aliens02fuckfast:
        "v071/aliens02fuckanim00.jpg"
        pause 0.025
        "v071/aliens02fuckanim01.jpg"
        pause 0.025
        "v071/aliens02fuckanim02.jpg"
        pause 0.025
        "v071/aliens02fuckanim03.jpg"
        pause 0.025
        "v071/aliens02fuckanim04.jpg"
        pause 0.025
        "v071/aliens02fuckanim05.jpg"
        pause 0.025
        "v071/aliens02fuckanim06.jpg"
        pause 0.025
        "v071/aliens02fuckanim07.jpg"
        pause 0.025
        "v071/aliens02fuckanim08.jpg"
        pause 0.025
        "v071/aliens02fuckanim09.jpg"
        pause 0.025
        "v071/aliens02fuckanim10.jpg"
        pause 0.025
        "v071/aliens02fuckanim11.jpg"
        pause 0.025
        "v071/aliens02fuckanim12.jpg"
        pause 0.025
        "v071/aliens02fuckanim11.jpg"
        pause 0.025
        "v071/aliens02fuckanim10.jpg"
        pause 0.025
        "v071/aliens02fuckanim09.jpg"
        pause 0.025
        "v071/aliens02fuckanim08.jpg"
        pause 0.025
        "v071/aliens02fuckanim07.jpg"
        pause 0.025
        "v071/aliens02fuckanim06.jpg"
        pause 0.025
        "v071/aliens02fuckanim05.jpg"
        pause 0.025
        "v071/aliens02fuckanim04.jpg"
        pause 0.025
        "v071/aliens02fuckanim03.jpg"
        pause 0.025
        "v071/aliens02fuckanim02.jpg"
        pause 0.025
        "v071/aliens02fuckanim01.jpg"
        pause 0.025
        repeat
            
    image diamondlickslow:
        "v07/diamondlick00.png"
        pause 0.06
        "v07/diamondlick01.png"
        pause .05
        "v07/diamondlick02.png"
        pause .05
        "v07/diamondlick03.png"
        pause .05
        "v07/diamondlick04.png"
        pause .05
        "v07/diamondlick05.png"
        pause .05
        "v07/diamondlick06.png"
        pause .05
        "v07/diamondlick07.png"
        pause .05
        "v07/diamondlick08.png"
        pause .05
        "v07/diamondlick09.png"
        pause .05
        "v07/diamondlick10.png"
        pause .05
        "v07/diamondlick11.png"
        pause .05
        "v07/diamondlick12.png"
        pause .05
        "v07/diamondlick11.png"
        pause .05
        "v07/diamondlick10.png"
        pause .05
        "v07/diamondlick09.png"
        pause .05
        "v07/diamondlick08.png"
        pause .05
        "v07/diamondlick07.png"
        pause .05
        "v07/diamondlick06.png"
        pause .05
        "v07/diamondlick05.png"
        pause .05
        "v07/diamondlick04.png"
        pause .05
        "v07/diamondlick03.png"
        pause .05
        "v07/diamondlick02.png"
        pause .05
        "v07/diamondlick01.png"
        pause .05
        repeat
            
    image diamondlickfast:
        "v07/diamondlick00.png"
        pause 0.04
        "v07/diamondlick01.png"
        pause 0.03
        "v07/diamondlick02.png"
        pause 0.03
        "v07/diamondlick03.png"
        pause 0.03
        "v07/diamondlick04.png"
        pause 0.03
        "v07/diamondlick05.png"
        pause 0.03
        "v07/diamondlick06.png"
        pause 0.03
        "v07/diamondlick07.png"
        pause 0.03
        "v07/diamondlick08.png"
        pause 0.03
        "v07/diamondlick09.png"
        pause 0.03
        "v07/diamondlick10.png"
        pause 0.03
        "v07/diamondlick11.png"
        pause 0.03
        "v07/diamondlick12.png"
        pause 0.03
        "v07/diamondlick11.png"
        pause 0.03
        "v07/diamondlick10.png"
        pause 0.03
        "v07/diamondlick09.png"
        pause 0.03
        "v07/diamondlick08.png"
        pause 0.03
        "v07/diamondlick07.png"
        pause 0.03
        "v07/diamondlick06.png"
        pause 0.03
        "v07/diamondlick05.png"
        pause 0.03
        "v07/diamondlick04.png"
        pause 0.03
        "v07/diamondlick03.png"
        pause 0.03
        "v07/diamondlick02.png"
        pause 0.03
        "v07/diamondlick01.png"
        pause 0.03
        repeat
            
    image diamondtitslow:
        "v07/diamondtit00.png"
        pause .06
        "v07/diamondtit01.png"
        pause .05
        "v07/diamondtit02.png"
        pause .05
        "v07/diamondtit03.png"
        pause .05
        "v07/diamondtit04.png"
        pause .05
        "v07/diamondtit05.png"
        pause .05
        "v07/diamondtit06.png"
        pause .05
        "v07/diamondtit07.png"
        pause .05
        "v07/diamondtit08.png"
        pause .05
        "v07/diamondtit09.png"
        pause .05
        "v07/diamondtit10.png"
        pause .05
        "v07/diamondtit11.png"
        pause 0.05
        "v07/diamondtit12.png"
        pause 0.06
        "v07/diamondtit11.png"
        pause 0.05
        "v07/diamondtit10.png"
        pause .05
        "v07/diamondtit09.png"
        pause .05
        "v07/diamondtit08.png"
        pause .05
        "v07/diamondtit07.png"
        pause .05
        "v07/diamondtit06.png"
        pause .05
        "v07/diamondtit05.png"
        pause .05
        "v07/diamondtit04.png"
        pause .05
        "v07/diamondtit03.png"
        pause .05
        "v07/diamondtit02.png"
        pause .05
        "v07/diamondtit01.png"
        pause 0.05
        repeat
            
    image diamondtitfast:
        "v07/diamondtit00.png"
        pause 0.04
        "v07/diamondtit01.png"
        pause 0.03
        "v07/diamondtit02.png"
        pause 0.03
        "v07/diamondtit03.png"
        pause 0.03
        "v07/diamondtit04.png"
        pause 0.03
        "v07/diamondtit05.png"
        pause 0.03
        "v07/diamondtit06.png"
        pause 0.03
        "v07/diamondtit07.png"
        pause 0.03
        "v07/diamondtit08.png"
        pause 0.03
        "v07/diamondtit09.png"
        pause 0.03
        "v07/diamondtit10.png"
        pause 0.03
        "v07/diamondtit11.png"
        pause 0.03
        "v07/diamondtit12.png"
        pause 0.04
        "v07/diamondtit11.png"
        pause 0.03
        "v07/diamondtit10.png"
        pause 0.03
        "v07/diamondtit09.png"
        pause 0.03
        "v07/diamondtit08.png"
        pause 0.03
        "v07/diamondtit07.png"
        pause 0.03
        "v07/diamondtit06.png"
        pause 0.03
        "v07/diamondtit05.png"
        pause 0.03
        "v07/diamondtit04.png"
        pause 0.03
        "v07/diamondtit03.png"
        pause 0.03
        "v07/diamondtit02.png"
        pause 0.03
        "v07/diamondtit01.png"
        pause 0.03
        repeat
            
    image heatherfuckslow:
        "v07/heatherfuck00.png"
        pause 0.035
        "v07/heatherfuck01.png"
        pause 0.035
        "v07/heatherfuck02.png"
        pause 0.035
        "v07/heatherfuck03.png"
        pause 0.035
        "v07/heatherfuck04.png"
        pause 0.035
        "v07/heatherfuck05.png"
        pause 0.035
        "v07/heatherfuck06.png"
        pause 0.035
        "v07/heatherfuck07.png"
        pause 0.035
        "v07/heatherfuck08.png"
        pause 0.035
        "v07/heatherfuck09.png"
        pause 0.035
        "v07/heatherfuck10.png"
        pause 0.035
        "v07/heatherfuck11.png"
        pause 0.035
        "v07/heatherfuck12.png"
        pause 0.035
        "v07/heatherfuck13.png"
        pause 0.035
        "v07/heatherfuck14.png"
        pause 0.035
        "v07/heatherfuck15.png"
        pause 0.035
        "v07/heatherfuck16.png"
        pause 0.035
        "v07/heatherfuck17.png"
        pause 0.035
        "v07/heatherfuck18.png"
        pause 0.035
        repeat
            
    image heatherfuckfast:
        "v07/heatherfuck00.png"
        pause 0.025
        "v07/heatherfuck01.png"
        pause 0.025
        "v07/heatherfuck02.png"
        pause 0.025
        "v07/heatherfuck03.png"
        pause 0.025
        "v07/heatherfuck04.png"
        pause 0.025
        "v07/heatherfuck05.png"
        pause 0.025
        "v07/heatherfuck06.png"
        pause 0.025
        "v07/heatherfuck07.png"
        pause 0.025
        "v07/heatherfuck08.png"
        pause 0.025
        "v07/heatherfuck09.png"
        pause 0.025
        "v07/heatherfuck10.png"
        pause 0.025
        "v07/heatherfuck11.png"
        pause 0.025
        "v07/heatherfuck12.png"
        pause 0.025
        "v07/heatherfuck13.png"
        pause 0.025
        "v07/heatherfuck14.png"
        pause 0.025
        "v07/heatherfuck15.png"
        pause 0.025
        "v07/heatherfuck16.png"
        pause 0.025
        "v07/heatherfuck17.png"
        pause 0.025
        "v07/heatherfuck18.png"
        pause 0.025
        repeat
            
    image sukyufuckslow:
        "v07/sukyufuck00.png"
        pause 0.035
        "v07/sukyufuck01.png"
        pause 0.035
        "v07/sukyufuck02.png"
        pause 0.035
        "v07/sukyufuck03.png"
        pause 0.035
        "v07/sukyufuck04.png"
        pause 0.035
        "v07/sukyufuck05.png"
        pause 0.035
        "v07/sukyufuck06.png"
        pause 0.035
        "v07/sukyufuck07.png"
        pause 0.035
        "v07/sukyufuck08.png"
        pause 0.035
        "v07/sukyufuck09.png"
        pause 0.035
        "v07/sukyufuck10.png"
        pause 0.035
        "v07/sukyufuck11.png"
        pause 0.035
        "v07/sukyufuck12.png"
        pause 0.035
        "v07/sukyufuck11.png"
        pause 0.035
        "v07/sukyufuck10.png"
        pause 0.035
        "v07/sukyufuck09.png"
        pause 0.035
        "v07/sukyufuck08.png"
        pause 0.035
        "v07/sukyufuck07.png"
        pause 0.035
        "v07/sukyufuck06.png"
        pause 0.035
        "v07/sukyufuck05.png"
        pause 0.035
        "v07/sukyufuck04.png"
        pause 0.035
        "v07/sukyufuck03.png"
        pause 0.035
        "v07/sukyufuck02.png"
        pause 0.035
        "v07/sukyufuck01.png"
        pause 0.035
        repeat
            
    image sukyufuckfast:
        "v07/sukyufuck00.png"
        pause 0.025
        "v07/sukyufuck01.png"
        pause 0.025
        "v07/sukyufuck02.png"
        pause 0.025
        "v07/sukyufuck03.png"
        pause 0.025
        "v07/sukyufuck04.png"
        pause 0.025
        "v07/sukyufuck05.png"
        pause 0.025
        "v07/sukyufuck06.png"
        pause 0.025
        "v07/sukyufuck07.png"
        pause 0.025
        "v07/sukyufuck08.png"
        pause 0.025
        "v07/sukyufuck09.png"
        pause 0.025
        "v07/sukyufuck10.png"
        pause 0.025
        "v07/sukyufuck11.png"
        pause 0.025
        "v07/sukyufuck12.png"
        pause 0.025
        "v07/sukyufuck11.png"
        pause 0.025
        "v07/sukyufuck10.png"
        pause 0.025
        "v07/sukyufuck09.png"
        pause 0.025
        "v07/sukyufuck08.png"
        pause 0.025
        "v07/sukyufuck07.png"
        pause 0.025
        "v07/sukyufuck06.png"
        pause 0.025
        "v07/sukyufuck05.png"
        pause 0.025
        "v07/sukyufuck04.png"
        pause 0.025
        "v07/sukyufuck03.png"
        pause 0.025
        "v07/sukyufuck02.png"
        pause 0.025
        "v07/sukyufuck01.png"
        pause 0.025
        repeat
            
    image diamondsukyuslow:
        "v07/diamondsukyu00.png"
        pause 0.06
        "v07/diamondsukyu01.png"
        pause 0.05
        "v07/diamondsukyu02.png"
        pause 0.05
        "v07/diamondsukyu03.png"
        pause 0.05
        "v07/diamondsukyu04.png"
        pause 0.05
        "v07/diamondsukyu05.png"
        pause 0.05
        "v07/diamondsukyu06.png"
        pause 0.05
        "v07/diamondsukyu07.png"
        pause 0.05
        "v07/diamondsukyu08.png"
        pause 0.05
        "v07/diamondsukyu09.png"
        pause 0.06
        "v07/diamondsukyu08.png"
        pause 0.05
        "v07/diamondsukyu07.png"
        pause 0.05
        "v07/diamondsukyu06.png"
        pause 0.05
        "v07/diamondsukyu05.png"
        pause 0.05
        "v07/diamondsukyu04.png"
        pause 0.05
        "v07/diamondsukyu03.png"
        pause 0.05
        "v07/diamondsukyu02.png"
        pause 0.05
        "v07/diamondsukyu01.png"
        pause 0.05
        repeat
            
    image diamondsukyufast:
        "v07/diamondsukyu00.png"
        pause 0.04
        "v07/diamondsukyu01.png"
        pause 0.03
        "v07/diamondsukyu02.png"
        pause 0.03
        "v07/diamondsukyu03.png"
        pause 0.03
        "v07/diamondsukyu04.png"
        pause 0.03
        "v07/diamondsukyu05.png"
        pause 0.03
        "v07/diamondsukyu06.png"
        pause 0.03
        "v07/diamondsukyu07.png"
        pause 0.03
        "v07/diamondsukyu08.png"
        pause 0.03
        "v07/diamondsukyu09.png"
        pause 0.04
        "v07/diamondsukyu08.png"
        pause 0.03
        "v07/diamondsukyu07.png"
        pause 0.03
        "v07/diamondsukyu06.png"
        pause 0.03
        "v07/diamondsukyu05.png"
        pause 0.03
        "v07/diamondsukyu04.png"
        pause 0.03
        "v07/diamondsukyu03.png"
        pause 0.03
        "v07/diamondsukyu02.png"
        pause 0.03
        "v07/diamondsukyu01.png"
        pause 0.03
        repeat
            
    image diamondheatherslow:
        "v07/diamondheather00.png"
        pause 0.06
        "v07/diamondheather01.png"
        pause 0.05
        "v07/diamondheather02.png"
        pause 0.05
        "v07/diamondheather03.png"
        pause 0.05
        "v07/diamondheather04.png"
        pause 0.05
        "v07/diamondheather05.png"
        pause 0.05
        "v07/diamondheather06.png"
        pause 0.05
        "v07/diamondheather07.png"
        pause 0.05
        "v07/diamondheather08.png"
        pause 0.05
        "v07/diamondheather09.png"
        pause 0.06
        "v07/diamondheather08.png"
        pause 0.05
        "v07/diamondheather07.png"
        pause 0.05
        "v07/diamondheather06.png"
        pause 0.05
        "v07/diamondheather05.png"
        pause 0.05
        "v07/diamondheather04.png"
        pause 0.05
        "v07/diamondheather03.png"
        pause 0.05
        "v07/diamondheather02.png"
        pause 0.05
        "v07/diamondheather01.png"
        pause 0.05
        repeat
            
    image diamondheatherfast:
        "v07/diamondheather00.png"
        pause 0.04
        "v07/diamondheather01.png"
        pause 0.03
        "v07/diamondheather02.png"
        pause 0.03
        "v07/diamondheather03.png"
        pause 0.03
        "v07/diamondheather04.png"
        pause 0.03
        "v07/diamondheather05.png"
        pause 0.03
        "v07/diamondheather06.png"
        pause 0.03
        "v07/diamondheather07.png"
        pause 0.03
        "v07/diamondheather08.png"
        pause 0.03
        "v07/diamondheather09.png"
        pause 0.04
        "v07/diamondheather08.png"
        pause 0.03
        "v07/diamondheather07.png"
        pause 0.03
        "v07/diamondheather06.png"
        pause 0.03
        "v07/diamondheather05.png"
        pause 0.03
        "v07/diamondheather04.png"
        pause 0.03
        "v07/diamondheather03.png"
        pause 0.03
        "v07/diamondheather02.png"
        pause 0.03
        "v07/diamondheather01.png"
        pause 0.03
        repeat
            
    image michikodojotraining:
        "v071/michikodojob01.png"
        pause 0.07
        "v071/michikodojob02.png"
        pause 0.07
        "v071/michikodojob03.png"
        pause 0.07
        "v071/michikodojob04.png"
        pause 0.07
        "v071/michikodojob05.png"
        pause 0.07
        "v071/michikodojob06.png"
        pause 0.07
        "v071/michikodojob07.png"
        pause 0.07
        "v071/michikodojob08.png"
        pause 0.07
        "v071/michikodojob09.png"
        pause 0.07
        "v071/michikodojob11.png"
        pause 0.07
        "v071/michikodojob12.png"
        pause 0.07
        "v071/michikodojob13.png"
        pause 0.07
        "v071/michikodojob14.png"
        pause 0.07
        "v071/michikodojob15.png"
        pause 0.07
        "v071/michikodojob16.png"
        pause 0.07
        "v071/michikodojob17.png"
        pause 0.07
        "v071/michikodojob18.png"
        pause 0.07
        "v071/michikodojob19.png"
        pause 0.07
        "v071/michikodojob20.png"
        pause 0.07
        "v071/michikodojob21.png"
        pause 0.07
        "v071/michikodojob22.png"
        pause 0.07
        "v071/michikodojob23.png"
        pause 0.07
        "v071/michikodojob24.png"
        pause 0.07
        "v071/michikodojob25.png"
        pause 0.07
        "v071/michikodojob26.png"
        pause 0.07
            
    image michikodojoattack:
        "v071/michikoattack04.png"
        pause 0.05
        "v071/michikoattack05.png"
        pause 0.05
        "v071/michikoattack06.png"
        pause 0.05
        "v071/michikoattack07.png"
        pause 0.05
        "v071/michikoattack08.png"
        pause 0.05
        "v071/michikoattack09.png"
        pause 0.05
        "v071/michikoattack11.png"
        pause 0.05
        "v071/michikoattack11.png"
        pause 0.05
        "v071/michikoattack12.png"
        pause 0.05
        "v071/michikoattack13.png"
        pause 0.05
        "v071/michikoattack14.png"
        pause 0.05
        "v071/michikoattack15.png"
        pause 0.05
        "v071/michikoattack16.png"
        pause 0.05
        "v071/michikoattack17.png"
        pause 0.05
        "v071/michikoattack18.png"
        pause 0.05
        "v071/michikoattack19.png"
        pause 0.05
        "v071/michikoattack20.png"
        pause 0.05
        "v071/michikoattack21.png"
        pause 0.05
        "v071/michikoattack22.png"
        pause 0.05
        "v071/michikoattack23.png"
        pause 0.05
        "v071/michikoattack24.png"
        pause 0.05
            
    image leatherfuckslow:
        "v071/heatherleatherfuck01.jpg"
        pause 0.035
        "v071/heatherleatherfuck02.jpg"
        pause 0.035
        "v071/heatherleatherfuck03.jpg"
        pause 0.035
        "v071/heatherleatherfuck04.jpg"
        pause 0.035
        "v071/heatherleatherfuck05.jpg"
        pause 0.035
        "v071/heatherleatherfuck06.jpg"
        pause 0.035
        "v071/heatherleatherfuck07.jpg"
        pause 0.035
        "v071/heatherleatherfuck08.jpg"
        pause 0.035
        "v071/heatherleatherfuck09.jpg"
        pause 0.035
        "v071/heatherleatherfuck10.jpg"
        pause 0.035
        "v071/heatherleatherfuck11.jpg"
        pause 0.035
        "v071/heatherleatherfuck12.jpg"
        pause 0.035
        "v071/heatherleatherfuck13.jpg"
        pause 0.06
        "v071/heatherleatherfuck12.jpg"
        pause 0.04
        "v071/heatherleatherfuck11.jpg"
        pause 0.04
        "v071/heatherleatherfuck10.jpg"
        pause 0.04
        "v071/heatherleatherfuck09.jpg"
        pause 0.04
        "v071/heatherleatherfuck08.jpg"
        pause 0.04
        "v071/heatherleatherfuck07.jpg"
        pause 0.04
        "v071/heatherleatherfuck06.jpg"
        pause 0.04
        "v071/heatherleatherfuck05.jpg"
        pause 0.04
        "v071/heatherleatherfuck04.jpg"
        pause 0.04
        "v071/heatherleatherfuck03.jpg"
        pause 0.04
        "v071/heatherleatherfuck02.jpg"
        pause 0.04
        repeat
            
    image leatherfuckfast:
        "v071/heatherleatherfuck01.jpg"
        pause 0.025
        "v071/heatherleatherfuck02.jpg"
        pause 0.025
        "v071/heatherleatherfuck03.jpg"
        pause 0.025
        "v071/heatherleatherfuck04.jpg"
        pause 0.025
        "v071/heatherleatherfuck05.jpg"
        pause 0.025
        "v071/heatherleatherfuck06.jpg"
        pause 0.025
        "v071/heatherleatherfuck07.jpg"
        pause 0.025
        "v071/heatherleatherfuck08.jpg"
        pause 0.025
        "v071/heatherleatherfuck09.jpg"
        pause 0.025
        "v071/heatherleatherfuck10.jpg"
        pause 0.025
        "v071/heatherleatherfuck11.jpg"
        pause 0.025
        "v071/heatherleatherfuck12.jpg"
        pause 0.025
        "v071/heatherleatherfuck13.jpg"
        pause 0.05
        "v071/heatherleatherfuck12.jpg"
        pause 0.03
        "v071/heatherleatherfuck11.jpg"
        pause 0.03
        "v071/heatherleatherfuck10.jpg"
        pause 0.03
        "v071/heatherleatherfuck09.jpg"
        pause 0.03
        "v071/heatherleatherfuck08.jpg"
        pause 0.03
        "v071/heatherleatherfuck07.jpg"
        pause 0.03
        "v071/heatherleatherfuck06.jpg"
        pause 0.03
        "v071/heatherleatherfuck05.jpg"
        pause 0.03
        "v071/heatherleatherfuck04.jpg"
        pause 0.03
        "v071/heatherleatherfuck03.jpg"
        pause 0.03
        "v071/heatherleatherfuck02.jpg"
        pause 0.03
        repeat
            
    image lauriemishugeslow:
        "v072/lauriemishuge01.jpg"
        pause 0.035
        "v072/lauriemishuge02.jpg"
        pause 0.035
        "v072/lauriemishuge03.jpg"
        pause 0.035
        "v072/lauriemishuge04.jpg"
        pause 0.035
        "v072/lauriemishuge05.jpg"
        pause 0.035
        "v072/lauriemishuge06.jpg"
        pause 0.035
        "v072/lauriemishuge07.jpg"
        pause 0.035
        "v072/lauriemishuge08.jpg"
        pause 0.035
        "v072/lauriemishuge09.jpg"
        pause 0.035
        "v072/lauriemishuge10.jpg"
        pause 0.035
        "v072/lauriemishuge11.jpg"
        pause 0.035
        "v072/lauriemishuge12.jpg"
        pause 0.035
        "v072/lauriemishuge13.jpg"
        pause 0.04
        "v072/lauriemishuge14.jpg"
        pause 0.04
        "v072/lauriemishuge15.jpg"
        pause 0.04
        "v072/lauriemishuge16.jpg"
        pause 0.04
        "v072/lauriemishuge17.jpg"
        pause 0.04
        "v072/lauriemishuge18.jpg"
        pause 0.04
        "v072/lauriemishuge19.jpg"
        pause 0.04
        repeat
            
    image lauriemishugefast:
        "v072/lauriemishuge01.jpg"
        pause 0.025
        "v072/lauriemishuge02.jpg"
        pause 0.025
        "v072/lauriemishuge03.jpg"
        pause 0.025
        "v072/lauriemishuge04.jpg"
        pause 0.025
        "v072/lauriemishuge05.jpg"
        pause 0.025
        "v072/lauriemishuge06.jpg"
        pause 0.025
        "v072/lauriemishuge07.jpg"
        pause 0.025
        "v072/lauriemishuge08.jpg"
        pause 0.025
        "v072/lauriemishuge09.jpg"
        pause 0.025
        "v072/lauriemishuge10.jpg"
        pause 0.025
        "v072/lauriemishuge11.jpg"
        pause 0.025
        "v072/lauriemishuge12.jpg"
        pause 0.025
        "v072/lauriemishuge13.jpg"
        pause 0.03
        "v072/lauriemishuge14.jpg"
        pause 0.03
        "v072/lauriemishuge15.jpg"
        pause 0.03
        "v072/lauriemishuge16.jpg"
        pause 0.03
        "v072/lauriemishuge17.jpg"
        pause 0.03
        "v072/lauriemishuge18.jpg"
        pause 0.03
        "v072/lauriemishuge19.jpg"
        pause 0.03
        repeat
            
    image heatherdpslow:
        "v072/heatherdp00.png"
        pause 0.04
        "v072/heatherdp01.png"
        pause 0.04
        "v072/heatherdp02.png"
        pause 0.04
        "v072/heatherdp03.png"
        pause 0.04
        "v072/heatherdp04.png"
        pause 0.04
        "v072/heatherdp05.png"
        pause 0.04
        "v072/heatherdp06.png"
        pause 0.04
        "v072/heatherdp07.png"
        pause 0.04
        "v072/heatherdp08.png"
        pause 0.04
        "v072/heatherdp09.png"
        pause 0.04
        "v072/heatherdp10.png"
        pause 0.04
        "v072/heatherdp11.png"
        pause 0.05
        "v072/heatherdp10.png"
        pause 0.04
        "v072/heatherdp09.png"
        pause 0.04
        "v072/heatherdp08.png"
        pause 0.04
        "v072/heatherdp07.png"
        pause 0.04
        "v072/heatherdp06.png"
        pause 0.04
        "v072/heatherdp05.png"
        pause 0.04
        "v072/heatherdp04.png"
        pause 0.04
        "v072/heatherdp03.png"
        pause 0.04
        "v072/heatherdp02.png"
        pause 0.04
        "v072/heatherdp01.png"
        pause 0.04
        repeat
            
    image heatherdpfast:
        "v072/heatherdp00.png"
        pause 0.03
        "v072/heatherdp01.png"
        pause 0.03
        "v072/heatherdp02.png"
        pause 0.03
        "v072/heatherdp03.png"
        pause 0.03
        "v072/heatherdp04.png"
        pause 0.03
        "v072/heatherdp05.png"
        pause 0.03
        "v072/heatherdp06.png"
        pause 0.03
        "v072/heatherdp07.png"
        pause 0.03
        "v072/heatherdp08.png"
        pause 0.03
        "v072/heatherdp09.png"
        pause 0.03
        "v072/heatherdp10.png"
        pause 0.03
        "v072/heatherdp11.png"
        pause 0.04
        "v072/heatherdp10.png"
        pause 0.03
        "v072/heatherdp09.png"
        pause 0.03
        "v072/heatherdp08.png"
        pause 0.03
        "v072/heatherdp07.png"
        pause 0.03
        "v072/heatherdp06.png"
        pause 0.03
        "v072/heatherdp05.png"
        pause 0.03
        "v072/heatherdp04.png"
        pause 0.03
        "v072/heatherdp03.png"
        pause 0.03
        "v072/heatherdp02.png"
        pause 0.03
        "v072/heatherdp01.png"
        pause 0.03
        repeat
            
    image sukyudpslow:
        "v072/sukyudp00.png"
        pause 0.04
        "v072/sukyudp01.png"
        pause 0.04
        "v072/sukyudp02.png"
        pause 0.04
        "v072/sukyudp03.png"
        pause 0.04
        "v072/sukyudp04.png"
        pause 0.04
        "v072/sukyudp05.png"
        pause 0.04
        "v072/sukyudp06.png"
        pause 0.04
        "v072/sukyudp07.png"
        pause 0.04
        "v072/sukyudp08.png"
        pause 0.04
        "v072/sukyudp09.png"
        pause 0.04
        "v072/sukyudp10.png"
        pause 0.04
        "v072/sukyudp11.png"
        pause 0.05
        "v072/sukyudp10.png"
        pause 0.04
        "v072/sukyudp09.png"
        pause 0.04
        "v072/sukyudp08.png"
        pause 0.04
        "v072/sukyudp07.png"
        pause 0.04
        "v072/sukyudp06.png"
        pause 0.04
        "v072/sukyudp05.png"
        pause 0.04
        "v072/sukyudp04.png"
        pause 0.04
        "v072/sukyudp03.png"
        pause 0.04
        "v072/sukyudp02.png"
        pause 0.04
        "v072/sukyudp01.png"
        pause 0.04
        repeat
            
    image sukyudpfast:
        "v072/sukyudp00.png"
        pause 0.03
        "v072/sukyudp01.png"
        pause 0.03
        "v072/sukyudp02.png"
        pause 0.03
        "v072/sukyudp03.png"
        pause 0.03
        "v072/sukyudp04.png"
        pause 0.03
        "v072/sukyudp05.png"
        pause 0.03
        "v072/sukyudp06.png"
        pause 0.03
        "v072/sukyudp07.png"
        pause 0.03
        "v072/sukyudp08.png"
        pause 0.03
        "v072/sukyudp09.png"
        pause 0.03
        "v072/sukyudp10.png"
        pause 0.03
        "v072/sukyudp11.png"
        pause 0.04
        "v072/sukyudp10.png"
        pause 0.03
        "v072/sukyudp09.png"
        pause 0.03
        "v072/sukyudp08.png"
        pause 0.03
        "v072/sukyudp07.png"
        pause 0.03
        "v072/sukyudp06.png"
        pause 0.03
        "v072/sukyudp05.png"
        pause 0.03
        "v072/sukyudp04.png"
        pause 0.03
        "v072/sukyudp03.png"
        pause 0.03
        "v072/sukyudp02.png"
        pause 0.03
        "v072/sukyudp01.png"
        pause 0.03
        repeat
            
    image laurieballsslow:
        "v072/laurieballs00.png"
        pause 0.04
        "v072/laurieballs01.png"
        pause 0.04
        "v072/laurieballs02.png"
        pause 0.04
        "v072/laurieballs03.png"
        pause 0.04
        "v072/laurieballs04.png"
        pause 0.04
        "v072/laurieballs05.png"
        pause 0.04
        "v072/laurieballs06.png"
        pause 0.04
        "v072/laurieballs07.png"
        pause 0.04
        "v072/laurieballs08.png"
        pause 0.04
        "v072/laurieballs09.png"
        pause 0.04
        "v072/laurieballs10.png"
        pause 0.04
        "v072/laurieballs09.png"
        pause 0.04
        "v072/laurieballs08.png"
        pause 0.04
        "v072/laurieballs07.png"
        pause 0.04
        "v072/laurieballs06.png"
        pause 0.04
        "v072/laurieballs05.png"
        pause 0.04
        "v072/laurieballs04.png"
        pause 0.04
        "v072/laurieballs03.png"
        pause 0.04
        "v072/laurieballs02.png"
        pause 0.04
        "v072/laurieballs01.png"
        pause 0.04
        repeat
            
    image laurieballsfast:
        "v072/laurieballs00.png"
        pause 0.03
        "v072/laurieballs01.png"
        pause 0.03
        "v072/laurieballs02.png"
        pause 0.03
        "v072/laurieballs03.png"
        pause 0.03
        "v072/laurieballs04.png"
        pause 0.03
        "v072/laurieballs05.png"
        pause 0.03
        "v072/laurieballs06.png"
        pause 0.03
        "v072/laurieballs07.png"
        pause 0.03
        "v072/laurieballs08.png"
        pause 0.03
        "v072/laurieballs09.png"
        pause 0.03
        "v072/laurieballs10.png"
        pause 0.03
        "v072/laurieballs09.png"
        pause 0.03
        "v072/laurieballs08.png"
        pause 0.03
        "v072/laurieballs07.png"
        pause 0.03
        "v072/laurieballs06.png"
        pause 0.03
        "v072/laurieballs05.png"
        pause 0.03
        "v072/laurieballs04.png"
        pause 0.03
        "v072/laurieballs03.png"
        pause 0.03
        "v072/laurieballs02.png"
        pause 0.03
        "v072/laurieballs01.png"
        pause 0.03
        repeat

    image lauriehugeupslow:
        "v072/lauriehugeup00.png"
        pause 0.05
        "v072/lauriehugeup01.png"
        pause 0.04
        "v072/lauriehugeup02.png"
        pause 0.04
        "v072/lauriehugeup03.png"
        pause 0.04
        "v072/lauriehugeup04.png"
        pause 0.04
        "v072/lauriehugeup05.png"
        pause 0.04
        "v072/lauriehugeup06.png"
        pause 0.04
        "v072/lauriehugeup07.png"
        pause 0.04
        "v072/lauriehugeup08.png"
        pause 0.04
        "v072/lauriehugeup09.png"
        pause 0.04
        "v072/lauriehugeup10.png"
        pause 0.04
        "v072/lauriehugeup11.png"
        pause 0.05
        "v072/lauriehugeup10.png"
        pause 0.04
        "v072/lauriehugeup09.png"
        pause 0.04
        "v072/lauriehugeup08.png"
        pause 0.04
        "v072/lauriehugeup07.png"
        pause 0.04
        "v072/lauriehugeup06.png"
        pause 0.04
        "v072/lauriehugeup05.png"
        pause 0.04
        "v072/lauriehugeup04.png"
        pause 0.04
        "v072/lauriehugeup03.png"
        pause 0.04
        "v072/lauriehugeup02.png"
        pause 0.04
        "v072/lauriehugeup01.png"
        pause 0.04
        repeat
            
    image lauriehugeupfast:
        "v072/lauriehugeup00.png"
        pause 0.04
        "v072/lauriehugeup01.png"
        pause 0.03
        "v072/lauriehugeup02.png"
        pause 0.03
        "v072/lauriehugeup03.png"
        pause 0.03
        "v072/lauriehugeup04.png"
        pause 0.03
        "v072/lauriehugeup05.png"
        pause 0.03
        "v072/lauriehugeup06.png"
        pause 0.03
        "v072/lauriehugeup07.png"
        pause 0.03
        "v072/lauriehugeup08.png"
        pause 0.03
        "v072/lauriehugeup09.png"
        pause 0.03
        "v072/lauriehugeup10.png"
        pause 0.03
        "v072/lauriehugeup11.png"
        pause 0.04
        "v072/lauriehugeup10.png"
        pause 0.03
        "v072/lauriehugeup09.png"
        pause 0.03
        "v072/lauriehugeup08.png"
        pause 0.03
        "v072/lauriehugeup07.png"
        pause 0.03
        "v072/lauriehugeup06.png"
        pause 0.03
        "v072/lauriehugeup05.png"
        pause 0.03
        "v072/lauriehugeup04.png"
        pause 0.03
        "v072/lauriehugeup03.png"
        pause 0.03
        "v072/lauriehugeup02.png"
        pause 0.03
        "v072/lauriehugeup01.png"
        pause 0.03
        repeat
            
    image lauriefuckslow:
        "v072/lauriehugefuck00.jpg"
        pause 0.05
        "v072/lauriehugefuck01.jpg"
        pause 0.04
        "v072/lauriehugefuck02.jpg"
        pause 0.04
        "v072/lauriehugefuck03.jpg"
        pause 0.04
        "v072/lauriehugefuck04.jpg"
        pause 0.04
        "v072/lauriehugefuck05.jpg"
        pause 0.04
        "v072/lauriehugefuck06.jpg"
        pause 0.04
        "v072/lauriehugefuck07.jpg"
        pause 0.04
        "v072/lauriehugefuck08.jpg"
        pause 0.04
        "v072/lauriehugefuck09.jpg"
        pause 0.05
        "v072/lauriehugefuck08.jpg"
        pause 0.04
        "v072/lauriehugefuck07.jpg"
        pause 0.04
        "v072/lauriehugefuck06.jpg"
        pause 0.04
        "v072/lauriehugefuck05.jpg"
        pause 0.04
        "v072/lauriehugefuck04.jpg"
        pause 0.04
        "v072/lauriehugefuck03.jpg"
        pause 0.04
        "v072/lauriehugefuck02.jpg"
        pause 0.04
        "v072/lauriehugefuck01.jpg"
        pause 0.04
        repeat
            
    image lauriefuckfast:
        "v072/lauriehugefuck00.jpg"
        pause 0.04
        "v072/lauriehugefuck01.jpg"
        pause 0.03
        "v072/lauriehugefuck02.jpg"
        pause 0.03
        "v072/lauriehugefuck03.jpg"
        pause 0.03
        "v072/lauriehugefuck04.jpg"
        pause 0.03
        "v072/lauriehugefuck05.jpg"
        pause 0.03
        "v072/lauriehugefuck06.jpg"
        pause 0.03
        "v072/lauriehugefuck07.jpg"
        pause 0.03
        "v072/lauriehugefuck08.jpg"
        pause 0.03
        "v072/lauriehugefuck09.jpg"
        pause 0.04
        "v072/lauriehugefuck08.jpg"
        pause 0.03
        "v072/lauriehugefuck07.jpg"
        pause 0.03
        "v072/lauriehugefuck06.jpg"
        pause 0.03
        "v072/lauriehugefuck05.jpg"
        pause 0.03
        "v072/lauriehugefuck04.jpg"
        pause 0.03
        "v072/lauriehugefuck03.jpg"
        pause 0.03
        "v072/lauriehugefuck02.jpg"
        pause 0.03
        "v072/lauriehugefuck01.jpg"
        pause 0.03
        repeat

    image lauriemegaslow:
        "v072/lauriemega00.jpg"
        pause 0.05
        "v072/lauriemega01.jpg"
        pause 0.04
        "v072/lauriemega02.jpg"
        pause 0.04
        "v072/lauriemega03.jpg"
        pause 0.04
        "v072/lauriemega04.jpg"
        pause 0.04
        "v072/lauriemega05.jpg"
        pause 0.04
        "v072/lauriemega06.jpg"
        pause 0.04
        "v072/lauriemega07.jpg"
        pause 0.04
        "v072/lauriemega08.jpg"
        pause 0.04
        "v072/lauriemega09.jpg"
        pause 0.04
        "v072/lauriemega10.jpg"
        pause 0.05
        "v072/lauriemega09.jpg"
        pause 0.04
        "v072/lauriemega08.jpg"
        pause 0.04
        "v072/lauriemega07.jpg"
        pause 0.04
        "v072/lauriemega06.jpg"
        pause 0.04
        "v072/lauriemega05.jpg"
        pause 0.04
        "v072/lauriemega04.jpg"
        pause 0.04
        "v072/lauriemega03.jpg"
        pause 0.04
        "v072/lauriemega02.jpg"
        pause 0.04
        "v072/lauriemega01.jpg"
        pause 0.04
        repeat

    image lauriemegafast:
        "v072/lauriemega00.jpg"
        pause 0.04
        "v072/lauriemega01.jpg"
        pause 0.03
        "v072/lauriemega02.jpg"
        pause 0.03
        "v072/lauriemega03.jpg"
        pause 0.03
        "v072/lauriemega04.jpg"
        pause 0.03
        "v072/lauriemega05.jpg"
        pause 0.03
        "v072/lauriemega06.jpg"
        pause 0.03
        "v072/lauriemega07.jpg"
        pause 0.03
        "v072/lauriemega08.jpg"
        pause 0.03
        "v072/lauriemega09.jpg"
        pause 0.03
        "v072/lauriemega10.jpg"
        pause 0.04
        "v072/lauriemega09.jpg"
        pause 0.03
        "v072/lauriemega08.jpg"
        pause 0.03
        "v072/lauriemega07.jpg"
        pause 0.03
        "v072/lauriemega06.jpg"
        pause 0.03
        "v072/lauriemega05.jpg"
        pause 0.03
        "v072/lauriemega04.jpg"
        pause 0.03
        "v072/lauriemega03.jpg"
        pause 0.03
        "v072/lauriemega02.jpg"
        pause 0.03
        "v072/lauriemega01.jpg"
        pause 0.03
        repeat

    image lauriesexhugeslow:
        "v072/lauriesexhuge00.jpg"
        pause 0.04
        "v072/lauriesexhuge01.jpg"
        pause 0.04
        "v072/lauriesexhuge02.jpg"
        pause 0.04
        "v072/lauriesexhuge03.jpg"
        pause 0.04
        "v072/lauriesexhuge04.jpg"
        pause 0.04
        "v072/lauriesexhuge05.jpg"
        pause 0.04
        "v072/lauriesexhuge06.jpg"
        pause 0.04
        "v072/lauriesexhuge07.jpg"
        pause 0.04
        "v072/lauriesexhuge08.jpg"
        pause 0.04
        "v072/lauriesexhuge09.jpg"
        pause 0.04
        "v072/lauriesexhuge10.jpg"
        pause 0.04
        "v072/lauriesexhuge11.jpg"
        pause 0.05
        "v072/lauriesexhuge12.jpg"
        pause 0.04
        "v072/lauriesexhuge13.jpg"
        pause 0.04
        "v072/lauriesexhuge14.jpg"
        pause 0.04
        "v072/lauriesexhuge15.jpg"
        pause 0.04
        "v072/lauriesexhuge16.jpg"
        pause 0.04
        "v072/lauriesexhuge17.jpg"
        pause 0.04
        "v072/lauriesexhuge18.jpg"
        pause 0.04
        "v072/lauriesexhuge19.jpg"
        pause 0.04
        repeat

    image lauriesexhugefast:
        "v072/lauriesexhuge00.jpg"
        pause 0.03
        "v072/lauriesexhuge01.jpg"
        pause 0.03
        "v072/lauriesexhuge02.jpg"
        pause 0.03
        "v072/lauriesexhuge03.jpg"
        pause 0.03
        "v072/lauriesexhuge04.jpg"
        pause 0.03
        "v072/lauriesexhuge05.jpg"
        pause 0.03
        "v072/lauriesexhuge06.jpg"
        pause 0.03
        "v072/lauriesexhuge07.jpg"
        pause 0.03
        "v072/lauriesexhuge08.jpg"
        pause 0.03
        "v072/lauriesexhuge09.jpg"
        pause 0.03
        "v072/lauriesexhuge10.jpg"
        pause 0.03
        "v072/lauriesexhuge11.jpg"
        pause 0.05
        "v072/lauriesexhuge12.jpg"
        pause 0.03
        "v072/lauriesexhuge13.jpg"
        pause 0.03
        "v072/lauriesexhuge14.jpg"
        pause 0.03
        "v072/lauriesexhuge15.jpg"
        pause 0.03
        "v072/lauriesexhuge16.jpg"
        pause 0.03
        "v072/lauriesexhuge17.jpg"
        pause 0.03
        "v072/lauriesexhuge18.jpg"
        pause 0.03
        "v072/lauriesexhuge19.jpg"
        pause 0.03
        repeat
            
    image laurierideslow:
        "v072/laurieride00.jpg"
        pause 0.04
        "v072/laurieride01.jpg"
        pause 0.04
        "v072/laurieride02.jpg"
        pause 0.04
        "v072/laurieride03.jpg"
        pause 0.04
        "v072/laurieride04.jpg"
        pause 0.04
        "v072/laurieride05.jpg"
        pause 0.04
        "v072/laurieride06.jpg"
        pause 0.04
        "v072/laurieride07.jpg"
        pause 0.04
        "v072/laurieride08.jpg"
        pause 0.04
        "v072/laurieride09.jpg"
        pause 0.04
        "v072/laurieride10.jpg"
        pause 0.04
        "v072/laurieride11.jpg"
        pause 0.05
        "v072/laurieride12.jpg"
        pause 0.04
        "v072/laurieride13.jpg"
        pause 0.04
        "v072/laurieride14.jpg"
        pause 0.04
        "v072/laurieride15.jpg"
        pause 0.04
        "v072/laurieride16.jpg"
        pause 0.04
        "v072/laurieride17.jpg"
        pause 0.04
        repeat
            
    image laurieridefast:
        "v072/laurieride00.jpg"
        pause 0.04
        "v072/laurieride01.jpg"
        pause 0.03
        "v072/laurieride02.jpg"
        pause 0.03
        "v072/laurieride03.jpg"
        pause 0.03
        "v072/laurieride04.jpg"
        pause 0.03
        "v072/laurieride05.jpg"
        pause 0.03
        "v072/laurieride06.jpg"
        pause 0.03
        "v072/laurieride07.jpg"
        pause 0.03
        "v072/laurieride08.jpg"
        pause 0.03
        "v072/laurieride09.jpg"
        pause 0.03
        "v072/laurieride10.jpg"
        pause 0.03
        "v072/laurieride11.jpg"
        pause 0.05
        "v072/laurieride12.jpg"
        pause 0.03
        "v072/laurieride13.jpg"
        pause 0.03
        "v072/laurieride14.jpg"
        pause 0.03
        "v072/laurieride15.jpg"
        pause 0.03
        "v072/laurieride16.jpg"
        pause 0.03
        "v072/laurieride17.jpg"
        pause 0.03
        repeat
            
    image laurietitfuckslow:
        "v072/laurietitfuck00.jpg"
        pause 0.05
        "v072/laurietitfuck01.jpg"
        pause 0.04
        "v072/laurietitfuck02.jpg"
        pause 0.04
        "v072/laurietitfuck03.jpg"
        pause 0.04
        "v072/laurietitfuck04.jpg"
        pause 0.04
        "v072/laurietitfuck05.jpg"
        pause 0.04
        "v072/laurietitfuck06.jpg"
        pause 0.04
        "v072/laurietitfuck07.jpg"
        pause 0.04
        "v072/laurietitfuck08.jpg"
        pause 0.04
        "v072/laurietitfuck09.jpg"
        pause 0.04
        "v072/laurietitfuck10.jpg"
        pause 0.04
        "v072/laurietitfuck11.jpg"
        pause 0.05
        "v072/laurietitfuck10.jpg"
        pause 0.04
        "v072/laurietitfuck09.jpg"
        pause 0.04
        "v072/laurietitfuck08.jpg"
        pause 0.04
        "v072/laurietitfuck07.jpg"
        pause 0.04
        "v072/laurietitfuck06.jpg"
        pause 0.04
        "v072/laurietitfuck05.jpg"
        pause 0.04
        "v072/laurietitfuck04.jpg"
        pause 0.04
        "v072/laurietitfuck03.jpg"
        pause 0.04
        "v072/laurietitfuck02.jpg"
        pause 0.04
        "v072/laurietitfuck01.jpg"
        pause 0.04
        repeat
            
    image laurietitfuckfast:
        "v072/laurietitfuck00.jpg"
        pause 0.04
        "v072/laurietitfuck01.jpg"
        pause 0.03
        "v072/laurietitfuck02.jpg"
        pause 0.03
        "v072/laurietitfuck03.jpg"
        pause 0.03
        "v072/laurietitfuck04.jpg"
        pause 0.03
        "v072/laurietitfuck05.jpg"
        pause 0.03
        "v072/laurietitfuck06.jpg"
        pause 0.03
        "v072/laurietitfuck07.jpg"
        pause 0.03
        "v072/laurietitfuck08.jpg"
        pause 0.03
        "v072/laurietitfuck09.jpg"
        pause 0.03
        "v072/laurietitfuck10.jpg"
        pause 0.03
        "v072/laurietitfuck11.jpg"
        pause 0.04
        "v072/laurietitfuck10.jpg"
        pause 0.03
        "v072/laurietitfuck09.jpg"
        pause 0.03
        "v072/laurietitfuck08.jpg"
        pause 0.03
        "v072/laurietitfuck07.jpg"
        pause 0.03
        "v072/laurietitfuck06.jpg"
        pause 0.03
        "v072/laurietitfuck05.jpg"
        pause 0.03
        "v072/laurietitfuck04.jpg"
        pause 0.03
        "v072/laurietitfuck03.jpg"
        pause 0.03
        "v072/laurietitfuck02.jpg"
        pause 0.03
        "v072/laurietitfuck01.jpg"
        pause 0.03
        repeat
            
    image lauriepregnantslow:
        "v072/lauriepreg00.png"
        pause 0.05
        "v072/lauriepreg01.png"
        pause 0.04
        "v072/lauriepreg02.png"
        pause 0.04
        "v072/lauriepreg03.png"
        pause 0.04
        "v072/lauriepreg04.png"
        pause 0.04
        "v072/lauriepreg05.png"
        pause 0.04
        "v072/lauriepreg06.png"
        pause 0.04
        "v072/lauriepreg07.png"
        pause 0.04
        "v072/lauriepreg08.png"
        pause 0.04
        "v072/lauriepreg09.png"
        pause 0.04
        "v072/lauriepreg10.png"
        pause 0.04
        "v072/lauriepreg11.png"
        pause 0.04
        "v072/lauriepreg12.png"
        pause 0.05
        "v072/lauriepreg11.png"
        pause 0.04
        "v072/lauriepreg10.png"
        pause 0.04
        "v072/lauriepreg09.png"
        pause 0.04
        "v072/lauriepreg08.png"
        pause 0.04
        "v072/lauriepreg07.png"
        pause 0.04
        "v072/lauriepreg06.png"
        pause 0.04
        "v072/lauriepreg05.png"
        pause 0.04
        "v072/lauriepreg04.png"
        pause 0.04
        "v072/lauriepreg03.png"
        pause 0.04
        "v072/lauriepreg02.png"
        pause 0.04
        "v072/lauriepreg01.png"
        pause 0.04
        repeat
            
    image lauriepregnantfast:
        "v072/lauriepreg00.png"
        pause 0.04
        "v072/lauriepreg01.png"
        pause 0.03
        "v072/lauriepreg02.png"
        pause 0.03
        "v072/lauriepreg03.png"
        pause 0.03
        "v072/lauriepreg04.png"
        pause 0.03
        "v072/lauriepreg05.png"
        pause 0.03
        "v072/lauriepreg06.png"
        pause 0.03
        "v072/lauriepreg07.png"
        pause 0.03
        "v072/lauriepreg08.png"
        pause 0.03
        "v072/lauriepreg09.png"
        pause 0.03
        "v072/lauriepreg10.png"
        pause 0.03
        "v072/lauriepreg11.png"
        pause 0.03
        "v072/lauriepreg12.png"
        pause 0.04
        "v072/lauriepreg11.png"
        pause 0.03
        "v072/lauriepreg10.png"
        pause 0.03
        "v072/lauriepreg09.png"
        pause 0.03
        "v072/lauriepreg08.png"
        pause 0.03
        "v072/lauriepreg07.png"
        pause 0.03
        "v072/lauriepreg06.png"
        pause 0.03
        "v072/lauriepreg05.png"
        pause 0.03
        "v072/lauriepreg04.png"
        pause 0.03
        "v072/lauriepreg03.png"
        pause 0.03
        "v072/lauriepreg02.png"
        pause 0.03
        "v072/lauriepreg01.png"
        pause 0.03
        repeat
            
    image lauriepregslow:
        "v072/lauriepussypreg00.png"
        pause 0.05
        "v072/lauriepussypreg01.png"
        pause 0.04
        "v072/lauriepussypreg02.png"
        pause 0.04
        "v072/lauriepussypreg03.png"
        pause 0.04
        "v072/lauriepussypreg04.png"
        pause 0.04
        "v072/lauriepussypreg05.png"
        pause 0.04
        "v072/lauriepussypreg06.png"
        pause 0.04
        "v072/lauriepussypreg07.png"
        pause 0.04
        "v072/lauriepussypreg08.png"
        pause 0.04
        "v072/lauriepussypreg09.png"
        pause 0.04
        "v072/lauriepussypreg10.png"
        pause 0.04
        "v072/lauriepussypreg11.png"
        pause 0.04
        "v072/lauriepussypreg12.png"
        pause 0.05
        "v072/lauriepussypreg11.png"
        pause 0.04
        "v072/lauriepussypreg10.png"
        pause 0.04
        "v072/lauriepussypreg09.png"
        pause 0.04
        "v072/lauriepussypreg08.png"
        pause 0.04
        "v072/lauriepussypreg07.png"
        pause 0.04
        "v072/lauriepussypreg06.png"
        pause 0.04
        "v072/lauriepussypreg05.png"
        pause 0.04
        "v072/lauriepussypreg04.png"
        pause 0.04
        "v072/lauriepussypreg03.png"
        pause 0.04
        "v072/lauriepussypreg02.png"
        pause 0.04
        "v072/lauriepussypreg01.png"
        pause 0.04
        repeat
            
    image lauriepregfast:
        "v072/lauriepussypreg00.png"
        pause 0.04
        "v072/lauriepussypreg01.png"
        pause 0.03
        "v072/lauriepussypreg02.png"
        pause 0.03
        "v072/lauriepussypreg03.png"
        pause 0.03
        "v072/lauriepussypreg04.png"
        pause 0.03
        "v072/lauriepussypreg05.png"
        pause 0.03
        "v072/lauriepussypreg06.png"
        pause 0.03
        "v072/lauriepussypreg07.png"
        pause 0.03
        "v072/lauriepussypreg08.png"
        pause 0.03
        "v072/lauriepussypreg09.png"
        pause 0.03
        "v072/lauriepussypreg10.png"
        pause 0.03
        "v072/lauriepussypreg11.png"
        pause 0.03
        "v072/lauriepussypreg12.png"
        pause 0.04
        "v072/lauriepussypreg11.png"
        pause 0.03
        "v072/lauriepussypreg10.png"
        pause 0.03
        "v072/lauriepussypreg09.png"
        pause 0.03
        "v072/lauriepussypreg08.png"
        pause 0.03
        "v072/lauriepussypreg07.png"
        pause 0.03
        "v072/lauriepussypreg06.png"
        pause 0.03
        "v072/lauriepussypreg05.png"
        pause 0.03
        "v072/lauriepussypreg04.png"
        pause 0.03
        "v072/lauriepussypreg03.png"
        pause 0.03
        "v072/lauriepussypreg02.png"
        pause 0.03
        "v072/lauriepussypreg01.png"
        pause 0.03
        repeat
            
    image lauriehugeanalslow:
        "v072/lauriehugeanal00.jpg"
        pause 0.05
        "v072/lauriehugeanal01.jpg"
        pause 0.04
        "v072/lauriehugeanal02.jpg"
        pause 0.04
        "v072/lauriehugeanal03.jpg"
        pause 0.04
        "v072/lauriehugeanal04.jpg"
        pause 0.04
        "v072/lauriehugeanal05.jpg"
        pause 0.04
        "v072/lauriehugeanal06.jpg"
        pause 0.04
        "v072/lauriehugeanal07.jpg"
        pause 0.04
        "v072/lauriehugeanal08.jpg"
        pause 0.04
        "v072/lauriehugeanal09.jpg"
        pause 0.04
        "v072/lauriehugeanal10.jpg"
        pause 0.04
        "v072/lauriehugeanal11.jpg"
        pause 0.05
        "v072/lauriehugeanal10.jpg"
        pause 0.04
        "v072/lauriehugeanal09.jpg"
        pause 0.04
        "v072/lauriehugeanal08.jpg"
        pause 0.04
        "v072/lauriehugeanal07.jpg"
        pause 0.04
        "v072/lauriehugeanal06.jpg"
        pause 0.04
        "v072/lauriehugeanal05.jpg"
        pause 0.04
        "v072/lauriehugeanal04.jpg"
        pause 0.04
        "v072/lauriehugeanal03.jpg"
        pause 0.04
        "v072/lauriehugeanal02.jpg"
        pause 0.04
        "v072/lauriehugeanal01.jpg"
        pause 0.04
        repeat
            
    image lauriehugeanalfast:
        "v072/lauriehugeanal00.jpg"
        pause 0.04
        "v072/lauriehugeanal01.jpg"
        pause 0.03
        "v072/lauriehugeanal02.jpg"
        pause 0.03
        "v072/lauriehugeanal03.jpg"
        pause 0.03
        "v072/lauriehugeanal04.jpg"
        pause 0.03
        "v072/lauriehugeanal05.jpg"
        pause 0.03
        "v072/lauriehugeanal06.jpg"
        pause 0.03
        "v072/lauriehugeanal07.jpg"
        pause 0.03
        "v072/lauriehugeanal08.jpg"
        pause 0.03
        "v072/lauriehugeanal09.jpg"
        pause 0.03
        "v072/lauriehugeanal10.jpg"
        pause 0.03
        "v072/lauriehugeanal11.jpg"
        pause 0.04
        "v072/lauriehugeanal10.jpg"
        pause 0.03
        "v072/lauriehugeanal09.jpg"
        pause 0.03
        "v072/lauriehugeanal08.jpg"
        pause 0.03
        "v072/lauriehugeanal07.jpg"
        pause 0.03
        "v072/lauriehugeanal06.jpg"
        pause 0.03
        "v072/lauriehugeanal05.jpg"
        pause 0.03
        "v072/lauriehugeanal04.jpg"
        pause 0.03
        "v072/lauriehugeanal03.jpg"
        pause 0.03
        "v072/lauriehugeanal02.jpg"
        pause 0.03
        "v072/lauriehugeanal01.jpg"
        pause 0.03
        repeat
            
    image laurieanalslow:
        "v072/laurieanalhugeb00.png"
        pause 0.05
        "v072/laurieanalhugeb01.png"
        pause 0.04
        "v072/laurieanalhugeb02.png"
        pause 0.04
        "v072/laurieanalhugeb03.png"
        pause 0.04
        "v072/laurieanalhugeb04.png"
        pause 0.04
        "v072/laurieanalhugeb05.png"
        pause 0.04
        "v072/laurieanalhugeb06.png"
        pause 0.04
        "v072/laurieanalhugeb07.png"
        pause 0.04
        "v072/laurieanalhugeb08.png"
        pause 0.04
        "v072/laurieanalhugeb09.png"
        pause 0.04
        "v072/laurieanalhugeb10.png"
        pause 0.04
        "v072/laurieanalhugeb11.png"
        pause 0.04
        "v072/laurieanalhugeb12.png"
        pause 0.05
        "v072/laurieanalhugeb11.png"
        pause 0.04
        "v072/laurieanalhugeb10.png"
        pause 0.04
        "v072/laurieanalhugeb09.png"
        pause 0.04
        "v072/laurieanalhugeb08.png"
        pause 0.04
        "v072/laurieanalhugeb07.png"
        pause 0.04
        "v072/laurieanalhugeb06.png"
        pause 0.04
        "v072/laurieanalhugeb05.png"
        pause 0.04
        "v072/laurieanalhugeb04.png"
        pause 0.04
        "v072/laurieanalhugeb03.png"
        pause 0.04
        "v072/laurieanalhugeb02.png"
        pause 0.04
        "v072/laurieanalhugeb01.png"
        pause 0.04
        repeat
            
    image laurieanalfast:
        "v072/laurieanalhugeb00.png"
        pause 0.04
        "v072/laurieanalhugeb01.png"
        pause 0.03
        "v072/laurieanalhugeb02.png"
        pause 0.03
        "v072/laurieanalhugeb03.png"
        pause 0.03
        "v072/laurieanalhugeb04.png"
        pause 0.03
        "v072/laurieanalhugeb05.png"
        pause 0.03
        "v072/laurieanalhugeb06.png"
        pause 0.03
        "v072/laurieanalhugeb07.png"
        pause 0.03
        "v072/laurieanalhugeb08.png"
        pause 0.03
        "v072/laurieanalhugeb09.png"
        pause 0.03
        "v072/laurieanalhugeb10.png"
        pause 0.03
        "v072/laurieanalhugeb11.png"
        pause 0.03
        "v072/laurieanalhugeb12.png"
        pause 0.04
        "v072/laurieanalhugeb11.png"
        pause 0.03
        "v072/laurieanalhugeb10.png"
        pause 0.03
        "v072/laurieanalhugeb09.png"
        pause 0.03
        "v072/laurieanalhugeb08.png"
        pause 0.03
        "v072/laurieanalhugeb07.png"
        pause 0.03
        "v072/laurieanalhugeb06.png"
        pause 0.03
        "v072/laurieanalhugeb05.png"
        pause 0.03
        "v072/laurieanalhugeb04.png"
        pause 0.03
        "v072/laurieanalhugeb03.png"
        pause 0.03
        "v072/laurieanalhugeb02.png"
        pause 0.03
        "v072/laurieanalhugeb01.png"
        pause 0.03
        repeat
            
    image heatherstandslow:
        "v072/heatherstand00.jpg"
        pause 0.05
        "v072/heatherstand01.jpg"
        pause 0.04
        "v072/heatherstand02.jpg"
        pause 0.04
        "v072/heatherstand03.jpg"
        pause 0.04
        "v072/heatherstand04.jpg"
        pause 0.04
        "v072/heatherstand05.jpg"
        pause 0.04
        "v072/heatherstand06.jpg"
        pause 0.04
        "v072/heatherstand07.jpg"
        pause 0.04
        "v072/heatherstand08.jpg"
        pause 0.04
        "v072/heatherstand09.jpg"
        pause 0.04
        "v072/heatherstand10.jpg"
        pause 0.04
        "v072/heatherstand11.jpg"
        pause 0.04
        "v072/heatherstand12.jpg"
        pause 0.05
        "v072/heatherstand11.jpg"
        pause 0.04
        "v072/heatherstand10.jpg"
        pause 0.04
        "v072/heatherstand09.jpg"
        pause 0.04
        "v072/heatherstand08.jpg"
        pause 0.04
        "v072/heatherstand07.jpg"
        pause 0.04
        "v072/heatherstand06.jpg"
        pause 0.04
        "v072/heatherstand05.jpg"
        pause 0.04
        "v072/heatherstand04.jpg"
        pause 0.04
        "v072/heatherstand03.jpg"
        pause 0.04
        "v072/heatherstand02.jpg"
        pause 0.04
        "v072/heatherstand01.jpg"
        pause 0.04
        repeat
            
    image heatherstandfast:
        "v072/heatherstand00.jpg"
        pause 0.04
        "v072/heatherstand01.jpg"
        pause 0.03
        "v072/heatherstand02.jpg"
        pause 0.03
        "v072/heatherstand03.jpg"
        pause 0.03
        "v072/heatherstand04.jpg"
        pause 0.03
        "v072/heatherstand05.jpg"
        pause 0.03
        "v072/heatherstand06.jpg"
        pause 0.03
        "v072/heatherstand07.jpg"
        pause 0.03
        "v072/heatherstand08.jpg"
        pause 0.03
        "v072/heatherstand09.jpg"
        pause 0.03
        "v072/heatherstand10.jpg"
        pause 0.03
        "v072/heatherstand11.jpg"
        pause 0.03
        "v072/heatherstand12.jpg"
        pause 0.04
        "v072/heatherstand11.jpg"
        pause 0.03
        "v072/heatherstand10.jpg"
        pause 0.03
        "v072/heatherstand09.jpg"
        pause 0.03
        "v072/heatherstand08.jpg"
        pause 0.03
        "v072/heatherstand07.jpg"
        pause 0.03
        "v072/heatherstand06.jpg"
        pause 0.03
        "v072/heatherstand05.jpg"
        pause 0.03
        "v072/heatherstand04.jpg"
        pause 0.03
        "v072/heatherstand03.jpg"
        pause 0.03
        "v072/heatherstand02.jpg"
        pause 0.03
        "v072/heatherstand01.jpg"
        pause 0.03
        repeat
            
    image heatherblowslow:
        "v072/heatherblow00.jpg"
        pause 0.05
        "v072/heatherblow01.jpg"
        pause 0.04
        "v072/heatherblow02.jpg"
        pause 0.04
        "v072/heatherblow03.jpg"
        pause 0.04
        "v072/heatherblow04.jpg"
        pause 0.04
        "v072/heatherblow05.jpg"
        pause 0.04
        "v072/heatherblow06.jpg"
        pause 0.04
        "v072/heatherblow07.jpg"
        pause 0.04
        "v072/heatherblow08.jpg"
        pause 0.04
        "v072/heatherblow09.jpg"
        pause 0.04
        "v072/heatherblow10.jpg"
        pause 0.04
        "v072/heatherblow11.jpg"
        pause 0.05
        "v072/heatherblow10.jpg"
        pause 0.04
        "v072/heatherblow09.jpg"
        pause 0.04
        "v072/heatherblow08.jpg"
        pause 0.04
        "v072/heatherblow07.jpg"
        pause 0.04
        "v072/heatherblow06.jpg"
        pause 0.04
        "v072/heatherblow05.jpg"
        pause 0.04
        "v072/heatherblow04.jpg"
        pause 0.04
        "v072/heatherblow03.jpg"
        pause 0.04
        "v072/heatherblow02.jpg"
        pause 0.04
        "v072/heatherblow01.jpg"
        pause 0.04
        repeat
            
    image heatherblowfast:
        "v072/heatherblow00.jpg"
        pause 0.04
        "v072/heatherblow01.jpg"
        pause 0.03
        "v072/heatherblow02.jpg"
        pause 0.03
        "v072/heatherblow03.jpg"
        pause 0.03
        "v072/heatherblow04.jpg"
        pause 0.03
        "v072/heatherblow05.jpg"
        pause 0.03
        "v072/heatherblow06.jpg"
        pause 0.03
        "v072/heatherblow07.jpg"
        pause 0.03
        "v072/heatherblow08.jpg"
        pause 0.03
        "v072/heatherblow09.jpg"
        pause 0.03
        "v072/heatherblow10.jpg"
        pause 0.03
        "v072/heatherblow11.jpg"
        pause 0.05
        "v072/heatherblow10.jpg"
        pause 0.03
        "v072/heatherblow09.jpg"
        pause 0.03
        "v072/heatherblow08.jpg"
        pause 0.03
        "v072/heatherblow07.jpg"
        pause 0.03
        "v072/heatherblow06.jpg"
        pause 0.03
        "v072/heatherblow05.jpg"
        pause 0.03
        "v072/heatherblow04.jpg"
        pause 0.03
        "v072/heatherblow03.jpg"
        pause 0.03
        "v072/heatherblow02.jpg"
        pause 0.03
        "v072/heatherblow01.jpg"
        pause 0.03
        repeat
            
    image sukyublowslow:
        "v072/sukyublow00.jpg"
        pause 0.05
        "v072/sukyublow01.jpg"
        pause 0.04
        "v072/sukyublow02.jpg"
        pause 0.04
        "v072/sukyublow03.jpg"
        pause 0.04
        "v072/sukyublow04.jpg"
        pause 0.04
        "v072/sukyublow05.jpg"
        pause 0.04
        "v072/sukyublow06.jpg"
        pause 0.04
        "v072/sukyublow07.jpg"
        pause 0.04
        "v072/sukyublow08.jpg"
        pause 0.04
        "v072/sukyublow09.jpg"
        pause 0.04
        "v072/sukyublow10.jpg"
        pause 0.04
        "v072/sukyublow11.jpg"
        pause 0.05
        "v072/sukyublow10.jpg"
        pause 0.04
        "v072/sukyublow09.jpg"
        pause 0.04
        "v072/sukyublow08.jpg"
        pause 0.04
        "v072/sukyublow07.jpg"
        pause 0.04
        "v072/sukyublow06.jpg"
        pause 0.04
        "v072/sukyublow05.jpg"
        pause 0.04
        "v072/sukyublow04.jpg"
        pause 0.04
        "v072/sukyublow03.jpg"
        pause 0.04
        "v072/sukyublow02.jpg"
        pause 0.04
        "v072/sukyublow01.jpg"
        pause 0.04
        repeat
            
    image sukyublowfast:
        "v072/sukyublow00.jpg"
        pause 0.04
        "v072/sukyublow01.jpg"
        pause 0.03
        "v072/sukyublow02.jpg"
        pause 0.03
        "v072/sukyublow03.jpg"
        pause 0.03
        "v072/sukyublow04.jpg"
        pause 0.03
        "v072/sukyublow05.jpg"
        pause 0.03
        "v072/sukyublow06.jpg"
        pause 0.03
        "v072/sukyublow07.jpg"
        pause 0.03
        "v072/sukyublow08.jpg"
        pause 0.03
        "v072/sukyublow09.jpg"
        pause 0.03
        "v072/sukyublow10.jpg"
        pause 0.03
        "v072/sukyublow11.jpg"
        pause 0.04
        "v072/sukyublow10.jpg"
        pause 0.03
        "v072/sukyublow09.jpg"
        pause 0.03
        "v072/sukyublow08.jpg"
        pause 0.03
        "v072/sukyublow07.jpg"
        pause 0.03
        "v072/sukyublow06.jpg"
        pause 0.03
        "v072/sukyublow05.jpg"
        pause 0.03
        "v072/sukyublow04.jpg"
        pause 0.03
        "v072/sukyublow03.jpg"
        pause 0.03
        "v072/sukyublow02.jpg"
        pause 0.03
        "v072/sukyublow01.jpg"
        pause 0.03
        repeat
            
    image sukstandslow:
        "v072/sukstand00.jpg"
        pause 0.05
        "v072/sukstand01.jpg"
        pause 0.04
        "v072/sukstand02.jpg"
        pause 0.04
        "v072/sukstand03.jpg"
        pause 0.04
        "v072/sukstand04.jpg"
        pause 0.04
        "v072/sukstand05.jpg"
        pause 0.04
        "v072/sukstand06.jpg"
        pause 0.04
        "v072/sukstand07.jpg"
        pause 0.04
        "v072/sukstand08.jpg"
        pause 0.04
        "v072/sukstand09.jpg"
        pause 0.04
        "v072/sukstand10.jpg"
        pause 0.04
        "v072/sukstand11.jpg"
        pause 0.05
        "v072/sukstand10.jpg"
        pause 0.04
        "v072/sukstand09.jpg"
        pause 0.04
        "v072/sukstand08.jpg"
        pause 0.04
        "v072/sukstand07.jpg"
        pause 0.04
        "v072/sukstand06.jpg"
        pause 0.04
        "v072/sukstand05.jpg"
        pause 0.04
        "v072/sukstand04.jpg"
        pause 0.04
        "v072/sukstand03.jpg"
        pause 0.04
        "v072/sukstand02.jpg"
        pause 0.04
        "v072/sukstand01.jpg"
        pause 0.04
        repeat
            
    image sukstandfast:
        "v072/sukstand00.jpg"
        pause 0.04
        "v072/sukstand01.jpg"
        pause 0.03
        "v072/sukstand02.jpg"
        pause 0.03
        "v072/sukstand03.jpg"
        pause 0.03
        "v072/sukstand04.jpg"
        pause 0.03
        "v072/sukstand05.jpg"
        pause 0.03
        "v072/sukstand06.jpg"
        pause 0.03
        "v072/sukstand07.jpg"
        pause 0.03
        "v072/sukstand08.jpg"
        pause 0.03
        "v072/sukstand09.jpg"
        pause 0.03
        "v072/sukstand10.jpg"
        pause 0.03
        "v072/sukstand11.jpg"
        pause 0.05
        "v072/sukstand10.jpg"
        pause 0.03
        "v072/sukstand09.jpg"
        pause 0.03
        "v072/sukstand08.jpg"
        pause 0.03
        "v072/sukstand07.jpg"
        pause 0.03
        "v072/sukstand06.jpg"
        pause 0.03
        "v072/sukstand05.jpg"
        pause 0.03
        "v072/sukstand04.jpg"
        pause 0.03
        "v072/sukstand03.jpg"
        pause 0.03
        "v072/sukstand02.jpg"
        pause 0.03
        "v072/sukstand01.jpg"
        pause 0.03
        repeat
            
    image jakecuckslow:
        "v08/jakecuckscene00.jpg"
        pause 0.05
        "v08/jakecuckscene01.jpg"
        pause 0.045
        "v08/jakecuckscene02.jpg"
        pause 0.045
        "v08/jakecuckscene03.jpg"
        pause 0.045
        "v08/jakecuckscene04.jpg"
        pause 0.045
        "v08/jakecuckscene05.jpg"
        pause 0.045
        "v08/jakecuckscene06.jpg"
        pause 0.045
        "v08/jakecuckscene07.jpg"
        pause 0.045
        "v08/jakecuckscene08.jpg"
        pause 0.045
        "v08/jakecuckscene09.jpg"
        pause 0.045
        "v08/jakecuckscene10.jpg"
        pause 0.045
        "v08/jakecuckscene11.jpg"
        pause 0.045
        "v08/jakecuckscene12.jpg"
        pause 0.06
        "v08/jakecuckscene11.jpg"
        pause 0.03
        "v08/jakecuckscene10.jpg"
        pause 0.03
        "v08/jakecuckscene09.jpg"
        pause 0.03
        "v08/jakecuckscene08.jpg"
        pause 0.03
        "v08/jakecuckscene07.jpg"
        pause 0.03
        "v08/jakecuckscene06.jpg"
        pause 0.03
        "v08/jakecuckscene05.jpg"
        pause 0.03
        "v08/jakecuckscene04.jpg"
        pause 0.03
        "v08/jakecuckscene03.jpg"
        pause 0.03
        "v08/jakecuckscene02.jpg"
        pause 0.03
        "v08/jakecuckscene01.jpg"
        pause 0.03
        repeat
            
    image jakecuckfast:
        "v08/jakecuckscene00.jpg"
        pause 0.04
        "v08/jakecuckscene01.jpg"
        pause 0.03
        "v08/jakecuckscene02.jpg"
        pause 0.03
        "v08/jakecuckscene03.jpg"
        pause 0.03
        "v08/jakecuckscene04.jpg"
        pause 0.03
        "v08/jakecuckscene05.jpg"
        pause 0.03
        "v08/jakecuckscene06.jpg"
        pause 0.03
        "v08/jakecuckscene07.jpg"
        pause 0.03
        "v08/jakecuckscene08.jpg"
        pause 0.03
        "v08/jakecuckscene09.jpg"
        pause 0.03
        "v08/jakecuckscene10.jpg"
        pause 0.03
        "v08/jakecuckscene11.jpg"
        pause 0.03
        "v08/jakecuckscene12.jpg"
        pause 0.04
        "v08/jakecuckscene11.jpg"
        pause 0.02
        "v08/jakecuckscene10.jpg"
        pause 0.02
        "v08/jakecuckscene09.jpg"
        pause 0.02
        "v08/jakecuckscene08.jpg"
        pause 0.02
        "v08/jakecuckscene07.jpg"
        pause 0.02
        "v08/jakecuckscene06.jpg"
        pause 0.02
        "v08/jakecuckscene05.jpg"
        pause 0.02
        "v08/jakecuckscene04.jpg"
        pause 0.02
        "v08/jakecuckscene03.jpg"
        pause 0.02
        "v08/jakecuckscene02.jpg"
        pause 0.02
        "v08/jakecuckscene01.jpg"
        pause 0.02
        repeat
            
    image jakecuckpovslow:
        "v08/jakecuckpov00.jpg"
        pause 0.05
        "v08/jakecuckpov01.jpg"
        pause 0.045
        "v08/jakecuckpov02.jpg"
        pause 0.045
        "v08/jakecuckpov03.jpg"
        pause 0.045
        "v08/jakecuckpov04.jpg"
        pause 0.045
        "v08/jakecuckpov05.jpg"
        pause 0.045
        "v08/jakecuckpov06.jpg"
        pause 0.045
        "v08/jakecuckpov07.jpg"
        pause 0.045
        "v08/jakecuckpov08.jpg"
        pause 0.045
        "v08/jakecuckpov09.jpg"
        pause 0.045
        "v08/jakecuckpov10.jpg"
        pause 0.045
        "v08/jakecuckpov11.jpg"
        pause 0.045
        "v08/jakecuckpov12.jpg"
        pause 0.06
        "v08/jakecuckpov11.jpg"
        pause 0.03
        "v08/jakecuckpov10.jpg"
        pause 0.03
        "v08/jakecuckpov09.jpg"
        pause 0.03
        "v08/jakecuckpov08.jpg"
        pause 0.03
        "v08/jakecuckpov07.jpg"
        pause 0.03
        "v08/jakecuckpov06.jpg"
        pause 0.03
        "v08/jakecuckpov05.jpg"
        pause 0.03
        "v08/jakecuckpov04.jpg"
        pause 0.03
        "v08/jakecuckpov03.jpg"
        pause 0.03
        "v08/jakecuckpov02.jpg"
        pause 0.03
        "v08/jakecuckpov01.jpg"
        pause 0.03
        repeat
            
    image jakecuckpovfast:
        "v08/jakecuckpov00.jpg"
        pause 0.04
        "v08/jakecuckpov01.jpg"
        pause 0.035
        "v08/jakecuckpov02.jpg"
        pause 0.035
        "v08/jakecuckpov03.jpg"
        pause 0.035
        "v08/jakecuckpov04.jpg"
        pause 0.035
        "v08/jakecuckpov05.jpg"
        pause 0.035
        "v08/jakecuckpov06.jpg"
        pause 0.035
        "v08/jakecuckpov07.jpg"
        pause 0.035
        "v08/jakecuckpov08.jpg"
        pause 0.035
        "v08/jakecuckpov09.jpg"
        pause 0.035
        "v08/jakecuckpov10.jpg"
        pause 0.035
        "v08/jakecuckpov11.jpg"
        pause 0.035
        "v08/jakecuckpov12.jpg"
        pause 0.05
        "v08/jakecuckpov11.jpg"
        pause 0.02
        "v08/jakecuckpov10.jpg"
        pause 0.02
        "v08/jakecuckpov09.jpg"
        pause 0.02
        "v08/jakecuckpov08.jpg"
        pause 0.02
        "v08/jakecuckpov07.jpg"
        pause 0.02
        "v08/jakecuckpov06.jpg"
        pause 0.02
        "v08/jakecuckpov05.jpg"
        pause 0.02
        "v08/jakecuckpov04.jpg"
        pause 0.02
        "v08/jakecuckpov03.jpg"
        pause 0.02
        "v08/jakecuckpov02.jpg"
        pause 0.02
        "v08/jakecuckpov01.jpg"
        pause 0.02
        repeat
            
    image lenaassslow:
        "v08/lenaass00.png"
        pause 0.05
        "v08/lenaass01.png"
        pause 0.05
        "v08/lenaass02.png"
        pause 0.05
        "v08/lenaass03.png"
        pause 0.05
        "v08/lenaass04.png"
        pause 0.05
        "v08/lenaass05.png"
        pause 0.05
        "v08/lenaass06.png"
        pause 0.05
        "v08/lenaass07.png"
        pause 0.05
        "v08/lenaass08.png"
        pause 0.05
        "v08/lenaass09.png"
        pause 0.05
        "v08/lenaass10.png"
        pause 0.05
        "v08/lenaass11.png"
        pause 0.06
        "v08/lenaass10.png"
        pause 0.04
        "v08/lenaass09.png"
        pause 0.04
        "v08/lenaass08.png"
        pause 0.04
        "v08/lenaass07.png"
        pause 0.04
        "v08/lenaass06.png"
        pause 0.04
        "v08/lenaass05.png"
        pause 0.04
        "v08/lenaass04.png"
        pause 0.04
        "v08/lenaass03.png"
        pause 0.04
        "v08/lenaass02.png"
        pause 0.04
        "v08/lenaass01.png"
        pause 0.04
        repeat
                            
    image lenaassfast:
        "v08/lenaass00.png"
        pause 0.035
        "v08/lenaass01.png"
        pause 0.035
        "v08/lenaass02.png"
        pause 0.035
        "v08/lenaass03.png"
        pause 0.035
        "v08/lenaass04.png"
        pause 0.035
        "v08/lenaass05.png"
        pause 0.035
        "v08/lenaass06.png"
        pause 0.035
        "v08/lenaass07.png"
        pause 0.035
        "v08/lenaass08.png"
        pause 0.035
        "v08/lenaass09.png"
        pause 0.035
        "v08/lenaass10.png"
        pause 0.035
        "v08/lenaass11.png"
        pause 0.04
        "v08/lenaass10.png"
        pause 0.02
        "v08/lenaass09.png"
        pause 0.02
        "v08/lenaass08.png"
        pause 0.02
        "v08/lenaass07.png"
        pause 0.02
        "v08/lenaass06.png"
        pause 0.02
        "v08/lenaass05.png"
        pause 0.02
        "v08/lenaass04.png"
        pause 0.02
        "v08/lenaass03.png"
        pause 0.02
        "v08/lenaass02.png"
        pause 0.02
        "v08/lenaass01.png"
        pause 0.02
        repeat
            
    image lenaassagainslow:
        "v08/lenaassagain00.jpg"
        pause 0.05
        "v08/lenaassagain01.jpg"
        pause 0.05
        "v08/lenaassagain02.jpg"
        pause 0.05
        "v08/lenaassagain03.jpg"
        pause 0.05
        "v08/lenaassagain04.jpg"
        pause 0.05
        "v08/lenaassagain05.jpg"
        pause 0.05
        "v08/lenaassagain06.jpg"
        pause 0.05
        "v08/lenaassagain07.jpg"
        pause 0.05
        "v08/lenaassagain08.jpg"
        pause 0.05
        "v08/lenaassagain09.jpg"
        pause 0.05
        "v08/lenaassagain10.jpg"
        pause 0.05
        "v08/lenaassagain09.jpg"
        pause 0.04
        "v08/lenaassagain08.jpg"
        pause 0.04
        "v08/lenaassagain07.jpg"
        pause 0.04
        "v08/lenaassagain06.jpg"
        pause 0.04
        "v08/lenaassagain05.jpg"
        pause 0.04
        "v08/lenaassagain04.jpg"
        pause 0.04
        "v08/lenaassagain03.jpg"
        pause 0.04
        "v08/lenaassagain02.jpg"
        pause 0.04
        "v08/lenaassagain01.jpg"
        pause 0.04
        repeat
                            
    image lenaassagainfast:
        "v08/lenaassagain00.jpg"
        pause 0.035
        "v08/lenaassagain01.jpg"
        pause 0.035
        "v08/lenaassagain02.jpg"
        pause 0.035
        "v08/lenaassagain03.jpg"
        pause 0.035
        "v08/lenaassagain04.jpg"
        pause 0.035
        "v08/lenaassagain05.jpg"
        pause 0.035
        "v08/lenaassagain06.jpg"
        pause 0.035
        "v08/lenaassagain07.jpg"
        pause 0.035
        "v08/lenaassagain08.jpg"
        pause 0.035
        "v08/lenaassagain09.jpg"
        pause 0.035
        "v08/lenaassagain10.jpg"
        pause 0.035
        "v08/lenaassagain09.jpg"
        pause 0.02
        "v08/lenaassagain08.jpg"
        pause 0.02
        "v08/lenaassagain07.jpg"
        pause 0.02
        "v08/lenaassagain06.jpg"
        pause 0.02
        "v08/lenaassagain05.jpg"
        pause 0.02
        "v08/lenaassagain04.jpg"
        pause 0.02
        "v08/lenaassagain03.jpg"
        pause 0.02
        "v08/lenaassagain02.jpg"
        pause 0.02
        "v08/lenaassagain01.jpg"
        pause 0.02
        repeat
            
    image lenaassbottomslow:
        "v08/lenaassass00.png"
        pause 0.05
        "v08/lenaassass01.png"
        pause 0.05
        "v08/lenaassass02.png"
        pause 0.05
        "v08/lenaassass03.png"
        pause 0.05
        "v08/lenaassass04.png"
        pause 0.05
        "v08/lenaassass05.png"
        pause 0.05
        "v08/lenaassass06.png"
        pause 0.05
        "v08/lenaassass07.png"
        pause 0.05
        "v08/lenaassass08.png"
        pause 0.05
        "v08/lenaassass09.png"
        pause 0.05
        "v08/lenaassass10.png"
        pause 0.05
        "v08/lenaassass09.png"
        pause 0.04
        "v08/lenaassass08.png"
        pause 0.04
        "v08/lenaassass07.png"
        pause 0.04
        "v08/lenaassass06.png"
        pause 0.04
        "v08/lenaassass05.png"
        pause 0.04
        "v08/lenaassass04.png"
        pause 0.04
        "v08/lenaassass03.png"
        pause 0.04
        "v08/lenaassass02.png"
        pause 0.04
        "v08/lenaassass01.png"
        pause 0.04
        repeat
                            
    image lenaassbottomfast:
        "v08/lenaassass00.png"
        pause 0.035
        "v08/lenaassass01.png"
        pause 0.035
        "v08/lenaassass02.png"
        pause 0.035
        "v08/lenaassass03.png"
        pause 0.035
        "v08/lenaassass04.png"
        pause 0.035
        "v08/lenaassass05.png"
        pause 0.035
        "v08/lenaassass06.png"
        pause 0.035
        "v08/lenaassass07.png"
        pause 0.035
        "v08/lenaassass08.png"
        pause 0.035
        "v08/lenaassass09.png"
        pause 0.035
        "v08/lenaassass10.png"
        pause 0.035
        "v08/lenaassass09.png"
        pause 0.02
        "v08/lenaassass08.png"
        pause 0.02
        "v08/lenaassass07.png"
        pause 0.02
        "v08/lenaassass06.png"
        pause 0.02
        "v08/lenaassass05.png"
        pause 0.02
        "v08/lenaassass04.png"
        pause 0.02
        "v08/lenaassass03.png"
        pause 0.02
        "v08/lenaassass02.png"
        pause 0.02
        "v08/lenaassass01.png"
        pause 0.02
        repeat
            
    image lenaupslow:
        "v08/lenaup00.png"
        pause 0.045
        "v08/lenaup01.png"
        pause 0.045
        "v08/lenaup02.png"
        pause 0.045
        "v08/lenaup03.png"
        pause 0.045
        "v08/lenaup04.png"
        pause 0.045
        "v08/lenaup05.png"
        pause 0.045
        "v08/lenaup06.png"
        pause 0.045
        "v08/lenaup07.png"
        pause 0.045
        "v08/lenaup08.png"
        pause 0.045
        "v08/lenaup09.png"
        pause 0.045
        "v08/lenaup10.png"
        pause 0.045
        "v08/lenaup11.png"
        pause 0.06
        "v08/lenaup10.png"
        pause 0.03
        "v08/lenaup09.png"
        pause 0.03
        "v08/lenaup08.png"
        pause 0.03
        "v08/lenaup07.png"
        pause 0.03
        "v08/lenaup06.png"
        pause 0.03
        "v08/lenaup05.png"
        pause 0.03
        "v08/lenaup04.png"
        pause 0.03
        "v08/lenaup03.png"
        pause 0.03
        "v08/lenaup02.png"
        pause 0.03
        "v08/lenaup01.png"
        pause 0.03
        repeat

    image lenaupfast:
        "v08/lenaup00.png"
        pause 0.03
        "v08/lenaup01.png"
        pause 0.03
        "v08/lenaup02.png"
        pause 0.03
        "v08/lenaup03.png"
        pause 0.03
        "v08/lenaup04.png"
        pause 0.03
        "v08/lenaup05.png"
        pause 0.03
        "v08/lenaup06.png"
        pause 0.03
        "v08/lenaup07.png"
        pause 0.03
        "v08/lenaup08.png"
        pause 0.03
        "v08/lenaup09.png"
        pause 0.03
        "v08/lenaup10.png"
        pause 0.03
        "v08/lenaup11.png"
        pause 0.04
        "v08/lenaup10.png"
        pause 0.02
        "v08/lenaup09.png"
        pause 0.02
        "v08/lenaup08.png"
        pause 0.02
        "v08/lenaup07.png"
        pause 0.02
        "v08/lenaup06.png"
        pause 0.02
        "v08/lenaup05.png"
        pause 0.02
        "v08/lenaup04.png"
        pause 0.02
        "v08/lenaup03.png"
        pause 0.02
        "v08/lenaup02.png"
        pause 0.02
        "v08/lenaup01.png"
        pause 0.02
        repeat
    
    image jakeblowslow:
        "v08/jakecuckblow00.png"
        pause 0.05
        "v08/jakecuckblow01.png"
        pause 0.05
        "v08/jakecuckblow02.png"
        pause 0.05
        "v08/jakecuckblow03.png"
        pause 0.05
        "v08/jakecuckblow04.png"
        pause 0.05
        "v08/jakecuckblow05.png"
        pause 0.05
        "v08/jakecuckblow06.png"
        pause 0.05
        "v08/jakecuckblow07.png"
        pause 0.05
        "v08/jakecuckblow08.png"
        pause 0.05
        "v08/jakecuckblow09.png"
        pause 0.05
        "v08/jakecuckblow10.png"
        pause 0.05
        "v08/jakecuckblow11.png"
        pause 0.06
        "v08/jakecuckblow10.png"
        pause 0.04
        "v08/jakecuckblow09.png"
        pause 0.04
        "v08/jakecuckblow08.png"
        pause 0.04
        "v08/jakecuckblow07.png"
        pause 0.04
        "v08/jakecuckblow06.png"
        pause 0.04
        "v08/jakecuckblow05.png"
        pause 0.04
        "v08/jakecuckblow04.png"
        pause 0.04
        "v08/jakecuckblow03.png"
        pause 0.04
        "v08/jakecuckblow02.png"
        pause 0.04
        "v08/jakecuckblow01.png"
        pause 0.04
        repeat
            
    image jakeblowfast:
        "v08/jakecuckblow00.png"
        pause 0.03
        "v08/jakecuckblow01.png"
        pause 0.03
        "v08/jakecuckblow02.png"
        pause 0.03
        "v08/jakecuckblow03.png"
        pause 0.03
        "v08/jakecuckblow04.png"
        pause 0.03
        "v08/jakecuckblow05.png"
        pause 0.03
        "v08/jakecuckblow06.png"
        pause 0.03
        "v08/jakecuckblow07.png"
        pause 0.03
        "v08/jakecuckblow08.png"
        pause 0.03
        "v08/jakecuckblow09.png"
        pause 0.03
        "v08/jakecuckblow10.png"
        pause 0.03
        "v08/jakecuckblow11.png"
        pause 0.04
        "v08/jakecuckblow10.png"
        pause 0.02
        "v08/jakecuckblow09.png"
        pause 0.02
        "v08/jakecuckblow08.png"
        pause 0.02
        "v08/jakecuckblow07.png"
        pause 0.02
        "v08/jakecuckblow06.png"
        pause 0.02
        "v08/jakecuckblow05.png"
        pause 0.02
        "v08/jakecuckblow04.png"
        pause 0.02
        "v08/jakecuckblow03.png"
        pause 0.02
        "v08/jakecuckblow02.png"
        pause 0.02
        "v08/jakecuckblow01.png"
        pause 0.02
        repeat
            
    image lenaassagainslow:
        "v08/lenaassagain00.jpg"
        pause 0.035
        "v08/lenaassagain01.jpg"
        pause 0.035
        "v08/lenaassagain02.jpg"
        pause 0.035
        "v08/lenaassagain03.jpg"
        pause 0.035
        "v08/lenaassagain04.jpg"
        pause 0.035
        "v08/lenaassagain05.jpg"
        pause 0.035
        "v08/lenaassagain06.jpg"
        pause 0.035
        "v08/lenaassagain07.jpg"
        pause 0.035
        "v08/lenaassagain08.jpg"
        pause 0.035
        "v08/lenaassagain09.jpg"
        pause 0.035
        "v08/lenaassagain10.jpg"
        pause 0.035
        "v08/lenaassagain09.jpg"
        pause 0.03
        "v08/lenaassagain08.jpg"
        pause 0.03
        "v08/lenaassagain07.jpg"
        pause 0.03
        "v08/lenaassagain06.jpg"
        pause 0.03
        "v08/lenaassagain05.jpg"
        pause 0.03
        "v08/lenaassagain04.jpg"
        pause 0.03
        "v08/lenaassagain03.jpg"
        pause 0.03
        "v08/lenaassagain02.jpg"
        pause 0.03
        "v08/lenaassagain01.jpg"
        pause 0.03
        repeat
            
    image lenaassagainfast:
        "v08/lenaassagain00.jpg"
        pause 0.025
        "v08/lenaassagain01.jpg"
        pause 0.025
        "v08/lenaassagain02.jpg"
        pause 0.025
        "v08/lenaassagain03.jpg"
        pause 0.025
        "v08/lenaassagain04.jpg"
        pause 0.025
        "v08/lenaassagain05.jpg"
        pause 0.025
        "v08/lenaassagain06.jpg"
        pause 0.025
        "v08/lenaassagain07.jpg"
        pause 0.025
        "v08/lenaassagain08.jpg"
        pause 0.025
        "v08/lenaassagain09.jpg"
        pause 0.025
        "v08/lenaassagain10.jpg"
        pause 0.025
        "v08/lenaassagain09.jpg"
        pause 0.02
        "v08/lenaassagain08.jpg"
        pause 0.02
        "v08/lenaassagain07.jpg"
        pause 0.02
        "v08/lenaassagain06.jpg"
        pause 0.02
        "v08/lenaassagain05.jpg"
        pause 0.02
        "v08/lenaassagain04.jpg"
        pause 0.02
        "v08/lenaassagain03.jpg"
        pause 0.02
        "v08/lenaassagain02.jpg"
        pause 0.02
        "v08/lenaassagain01.jpg"
        pause 0.02
        repeat
            
    image lenafondleslow:
        "v08/lenafondle00.jpg"
        pause 0.035
        "v08/lenafondle01.jpg"
        pause 0.035
        "v08/lenafondle02.jpg"
        pause 0.035
        "v08/lenafondle03.jpg"
        pause 0.035
        "v08/lenafondle04.jpg"
        pause 0.035
        "v08/lenafondle05.jpg"
        pause 0.035
        "v08/lenafondle06.jpg"
        pause 0.035
        "v08/lenafondle07.jpg"
        pause 0.035
        "v08/lenafondle08.jpg"
        pause 0.035
        "v08/lenafondle09.jpg"
        pause 0.035
        "v08/lenafondle10.jpg"
        pause 0.035
        "v08/lenafondle11.jpg"
        pause 0.035
        "v08/lenafondle12.jpg"
        pause 0.035
        "v08/lenafondle13.jpg"
        pause 0.035
        "v08/lenafondle14.jpg"
        pause 0.035
        "v08/lenafondle15.jpg"
        pause 0.035
        "v08/lenafondle16.jpg"
        pause 0.035
        "v08/lenafondle17.jpg"
        pause 0.035
        "v08/lenafondle18.jpg"
        pause 0.035
        "v08/lenafondle19.jpg"
        pause 0.035
        "v08/lenafondle20.jpg"
        pause 0.035
        "v08/lenafondle21.jpg"
        pause 0.035
        "v08/lenafondle22.jpg"
        pause 0.035
        "v08/lenafondle23.jpg"
        pause 0.035
        repeat
            
    image lenafondlefast:
        "v08/lenafondle00.jpg"
        pause 0.025
        "v08/lenafondle01.jpg"
        pause 0.025
        "v08/lenafondle02.jpg"
        pause 0.025
        "v08/lenafondle03.jpg"
        pause 0.025
        "v08/lenafondle04.jpg"
        pause 0.025
        "v08/lenafondle05.jpg"
        pause 0.025
        "v08/lenafondle06.jpg"
        pause 0.025
        "v08/lenafondle07.jpg"
        pause 0.025
        "v08/lenafondle08.jpg"
        pause 0.025
        "v08/lenafondle09.jpg"
        pause 0.025
        "v08/lenafondle10.jpg"
        pause 0.025
        "v08/lenafondle11.jpg"
        pause 0.025
        "v08/lenafondle12.jpg"
        pause 0.025
        "v08/lenafondle13.jpg"
        pause 0.025
        "v08/lenafondle14.jpg"
        pause 0.025
        "v08/lenafondle15.jpg"
        pause 0.025
        "v08/lenafondle16.jpg"
        pause 0.025
        "v08/lenafondle17.jpg"
        pause 0.025
        "v08/lenafondle18.jpg"
        pause 0.025
        "v08/lenafondle19.jpg"
        pause 0.025
        "v08/lenafondle20.jpg"
        pause 0.025
        "v08/lenafondle21.jpg"
        pause 0.025
        "v08/lenafondle22.jpg"
        pause 0.025
        "v08/lenafondle23.jpg"
        pause 0.025
        repeat
        
    image lenatitsslow:
        "v08/lenatits00.jpg"
        pause 0.045
        "v08/lenatits01.jpg"
        pause 0.045
        "v08/lenatits02.jpg"
        pause 0.045
        "v08/lenatits03.jpg"
        pause 0.045
        "v08/lenatits04.jpg"
        pause 0.045
        "v08/lenatits05.jpg"
        pause 0.045
        "v08/lenatits06.jpg"
        pause 0.045
        "v08/lenatits07.jpg"
        pause 0.045
        "v08/lenatits08.jpg"
        pause 0.045
        "v08/lenatits09.jpg"
        pause 0.045
        "v08/lenatits10.jpg"
        pause 0.045
        "v08/lenatits11.jpg"
        pause 0.045
        "v08/lenatits10.jpg"
        pause 0.04
        "v08/lenatits09.jpg"
        pause 0.04
        "v08/lenatits08.jpg"
        pause 0.04
        "v08/lenatits07.jpg"
        pause 0.04
        "v08/lenatits06.jpg"
        pause 0.04
        "v08/lenatits05.jpg"
        pause 0.04
        "v08/lenatits04.jpg"
        pause 0.04
        "v08/lenatits03.jpg"
        pause 0.04
        "v08/lenatits02.jpg"
        pause 0.04
        "v08/lenatits01.jpg"
        pause 0.04
        repeat
            
    image lenatitsfast:
        "v08/lenatits00.jpg"
        pause 0.035
        "v08/lenatits01.jpg"
        pause 0.035
        "v08/lenatits02.jpg"
        pause 0.035
        "v08/lenatits03.jpg"
        pause 0.035
        "v08/lenatits04.jpg"
        pause 0.035
        "v08/lenatits05.jpg"
        pause 0.035
        "v08/lenatits06.jpg"
        pause 0.035
        "v08/lenatits07.jpg"
        pause 0.035
        "v08/lenatits08.jpg"
        pause 0.035
        "v08/lenatits09.jpg"
        pause 0.035
        "v08/lenatits10.jpg"
        pause 0.035
        "v08/lenatits11.jpg"
        pause 0.035
        "v08/lenatits10.jpg"
        pause 0.03
        "v08/lenatits09.jpg"
        pause 0.03
        "v08/lenatits08.jpg"
        pause 0.03
        "v08/lenatits07.jpg"
        pause 0.03
        "v08/lenatits06.jpg"
        pause 0.03
        "v08/lenatits05.jpg"
        pause 0.03
        "v08/lenatits04.jpg"
        pause 0.03
        "v08/lenatits03.jpg"
        pause 0.03
        "v08/lenatits02.jpg"
        pause 0.03
        "v08/lenatits01.jpg"
        pause 0.03
        repeat
            
    image lenatitscloseslow:
        "v08/lenatitsclose00.jpg"
        pause 0.045
        "v08/lenatitsclose01.jpg"
        pause 0.045
        "v08/lenatitsclose02.jpg"
        pause 0.045
        "v08/lenatitsclose03.jpg"
        pause 0.045
        "v08/lenatitsclose04.jpg"
        pause 0.045
        "v08/lenatitsclose05.jpg"
        pause 0.045
        "v08/lenatitsclose06.jpg"
        pause 0.045
        "v08/lenatitsclose07.jpg"
        pause 0.045
        "v08/lenatitsclose08.jpg"
        pause 0.045
        "v08/lenatitsclose09.jpg"
        pause 0.045
        "v08/lenatitsclose10.jpg"
        pause 0.045
        "v08/lenatitsclose11.jpg"
        pause 0.045
        "v08/lenatitsclose10.jpg"
        pause 0.04
        "v08/lenatitsclose09.jpg"
        pause 0.04
        "v08/lenatitsclose08.jpg"
        pause 0.04
        "v08/lenatitsclose07.jpg"
        pause 0.04
        "v08/lenatitsclose06.jpg"
        pause 0.04
        "v08/lenatitsclose05.jpg"
        pause 0.04
        "v08/lenatitsclose04.jpg"
        pause 0.04
        "v08/lenatitsclose03.jpg"
        pause 0.04
        "v08/lenatitsclose02.jpg"
        pause 0.04
        "v08/lenatitsclose01.jpg"
        pause 0.04
        repeat
            
    image lenatitsclosefast:
        "v08/lenatitsclose00.jpg"
        pause 0.035
        "v08/lenatitsclose01.jpg"
        pause 0.035
        "v08/lenatitsclose02.jpg"
        pause 0.035
        "v08/lenatitsclose03.jpg"
        pause 0.035
        "v08/lenatitsclose04.jpg"
        pause 0.035
        "v08/lenatitsclose05.jpg"
        pause 0.035
        "v08/lenatitsclose06.jpg"
        pause 0.035
        "v08/lenatitsclose07.jpg"
        pause 0.035
        "v08/lenatitsclose08.jpg"
        pause 0.035
        "v08/lenatitsclose09.jpg"
        pause 0.035
        "v08/lenatitsclose10.jpg"
        pause 0.035
        "v08/lenatitsclose11.jpg"
        pause 0.035
        "v08/lenatitsclose10.jpg"
        pause 0.03
        "v08/lenatitsclose09.jpg"
        pause 0.03
        "v08/lenatitsclose08.jpg"
        pause 0.03
        "v08/lenatitsclose07.jpg"
        pause 0.03
        "v08/lenatitsclose06.jpg"
        pause 0.03
        "v08/lenatitsclose05.jpg"
        pause 0.03
        "v08/lenatitsclose04.jpg"
        pause 0.03
        "v08/lenatitsclose03.jpg"
        pause 0.03
        "v08/lenatitsclose02.jpg"
        pause 0.03
        "v08/lenatitsclose01.jpg"
        pause 0.03
        repeat
            
    image lenadpslow:
        "v08/lenadp00.jpg"
        pause 0.035
        "v08/lenadp01.jpg"
        pause 0.035
        "v08/lenadp02.jpg"
        pause 0.035
        "v08/lenadp03.jpg"
        pause 0.035
        "v08/lenadp04.jpg"
        pause 0.035
        "v08/lenadp05.jpg"
        pause 0.035
        "v08/lenadp06.jpg"
        pause 0.035
        "v08/lenadp07.jpg"
        pause 0.035
        "v08/lenadp08.jpg"
        pause 0.035
        "v08/lenadp09.jpg"
        pause 0.035
        "v08/lenadp10.jpg"
        pause 0.035
        "v08/lenadp11.jpg"
        pause 0.035
        "v08/lenadp10.jpg"
        pause 0.03
        "v08/lenadp09.jpg"
        pause 0.03
        "v08/lenadp08.jpg"
        pause 0.03
        "v08/lenadp07.jpg"
        pause 0.03
        "v08/lenadp06.jpg"
        pause 0.03
        "v08/lenadp05.jpg"
        pause 0.03
        "v08/lenadp04.jpg"
        pause 0.03
        "v08/lenadp03.jpg"
        pause 0.03
        "v08/lenadp02.jpg"
        pause 0.03
        "v08/lenadp01.jpg"
        pause 0.03
        repeat
            
    image lenadpfast:
        "v08/lenadp00.jpg"
        pause 0.025
        "v08/lenadp01.jpg"
        pause 0.025
        "v08/lenadp02.jpg"
        pause 0.025
        "v08/lenadp03.jpg"
        pause 0.025
        "v08/lenadp04.jpg"
        pause 0.025
        "v08/lenadp05.jpg"
        pause 0.025
        "v08/lenadp06.jpg"
        pause 0.025
        "v08/lenadp07.jpg"
        pause 0.025
        "v08/lenadp08.jpg"
        pause 0.025
        "v08/lenadp09.jpg"
        pause 0.025
        "v08/lenadp10.jpg"
        pause 0.025
        "v08/lenadp11.jpg"
        pause 0.025
        "v08/lenadp10.jpg"
        pause 0.02
        "v08/lenadp09.jpg"
        pause 0.02
        "v08/lenadp08.jpg"
        pause 0.02
        "v08/lenadp07.jpg"
        pause 0.02
        "v08/lenadp06.jpg"
        pause 0.02
        "v08/lenadp05.jpg"
        pause 0.02
        "v08/lenadp04.jpg"
        pause 0.02
        "v08/lenadp03.jpg"
        pause 0.02
        "v08/lenadp02.jpg"
        pause 0.02
        "v08/lenadp01.jpg"
        pause 0.02
        repeat
            
    image lenasexslow:
        "v08/lenasex00.jpg"
        pause 0.04
        "v08/lenasex01.jpg"
        pause 0.035
        "v08/lenasex02.jpg"
        pause 0.035
        "v08/lenasex03.jpg"
        pause 0.035
        "v08/lenasex04.jpg"
        pause 0.035
        "v08/lenasex05.jpg"
        pause 0.035
        "v08/lenasex06.jpg"
        pause 0.035
        "v08/lenasex07.jpg"
        pause 0.035
        "v08/lenasex08.jpg"
        pause 0.035
        "v08/lenasex09.jpg"
        pause 0.035
        "v08/lenasex10.jpg"
        pause 0.035
        "v08/lenasex11.jpg"
        pause 0.035
        "v08/lenasex12.jpg"
        pause 0.04
        "v08/lenasex11.jpg"
        pause 0.03
        "v08/lenasex10.jpg"
        pause 0.03
        "v08/lenasex09.jpg"
        pause 0.03
        "v08/lenasex08.jpg"
        pause 0.03
        "v08/lenasex07.jpg"
        pause 0.03
        "v08/lenasex06.jpg"
        pause 0.03
        "v08/lenasex05.jpg"
        pause 0.03
        "v08/lenasex04.jpg"
        pause 0.03
        "v08/lenasex03.jpg"
        pause 0.03
        "v08/lenasex02.jpg"
        pause 0.03
        "v08/lenasex01.jpg"
        pause 0.03
        repeat
            
    image lenasexfast:
        "v08/lenasex00.jpg"
        pause 0.03
        "v08/lenasex01.jpg"
        pause 0.025
        "v08/lenasex02.jpg"
        pause 0.025
        "v08/lenasex03.jpg"
        pause 0.025
        "v08/lenasex04.jpg"
        pause 0.025
        "v08/lenasex05.jpg"
        pause 0.025
        "v08/lenasex06.jpg"
        pause 0.025
        "v08/lenasex07.jpg"
        pause 0.025
        "v08/lenasex08.jpg"
        pause 0.025
        "v08/lenasex09.jpg"
        pause 0.025
        "v08/lenasex10.jpg"
        pause 0.025
        "v08/lenasex11.jpg"
        pause 0.025
        "v08/lenasex12.jpg"
        pause 0.03
        "v08/lenasex11.jpg"
        pause 0.02
        "v08/lenasex10.jpg"
        pause 0.02
        "v08/lenasex09.jpg"
        pause 0.02
        "v08/lenasex08.jpg"
        pause 0.02
        "v08/lenasex07.jpg"
        pause 0.02
        "v08/lenasex06.jpg"
        pause 0.02
        "v08/lenasex05.jpg"
        pause 0.02
        "v08/lenasex04.jpg"
        pause 0.02
        "v08/lenasex03.jpg"
        pause 0.02
        "v08/lenasex02.jpg"
        pause 0.02
        "v08/lenasex01.jpg"
        pause 0.02
        repeat
            
    image lenasexpovslow:
        "v08/lenasexpov00.jpg"
        pause 0.04
        "v08/lenasexpov01.jpg"
        pause 0.035
        "v08/lenasexpov02.jpg"
        pause 0.035
        "v08/lenasexpov03.jpg"
        pause 0.035
        "v08/lenasexpov04.jpg"
        pause 0.035
        "v08/lenasexpov05.jpg"
        pause 0.035
        "v08/lenasexpov06.jpg"
        pause 0.035
        "v08/lenasexpov07.jpg"
        pause 0.035
        "v08/lenasexpov08.jpg"
        pause 0.035
        "v08/lenasexpov09.jpg"
        pause 0.035
        "v08/lenasexpov10.jpg"
        pause 0.035
        "v08/lenasexpov11.jpg"
        pause 0.04
        "v08/lenasexpov10.jpg"
        pause 0.03
        "v08/lenasexpov09.jpg"
        pause 0.03
        "v08/lenasexpov08.jpg"
        pause 0.03
        "v08/lenasexpov07.jpg"
        pause 0.03
        "v08/lenasexpov06.jpg"
        pause 0.03
        "v08/lenasexpov05.jpg"
        pause 0.03
        "v08/lenasexpov04.jpg"
        pause 0.03
        "v08/lenasexpov03.jpg"
        pause 0.03
        "v08/lenasexpov02.jpg"
        pause 0.03
        "v08/lenasexpov01.jpg"
        pause 0.03
        repeat
            
    image lenasexpovfast:
        "v08/lenasexpov00.jpg"
        pause 0.03
        "v08/lenasexpov01.jpg"
        pause 0.025
        "v08/lenasexpov02.jpg"
        pause 0.025
        "v08/lenasexpov03.jpg"
        pause 0.025
        "v08/lenasexpov04.jpg"
        pause 0.025
        "v08/lenasexpov05.jpg"
        pause 0.025
        "v08/lenasexpov06.jpg"
        pause 0.025
        "v08/lenasexpov07.jpg"
        pause 0.025
        "v08/lenasexpov08.jpg"
        pause 0.025
        "v08/lenasexpov09.jpg"
        pause 0.025
        "v08/lenasexpov10.jpg"
        pause 0.025
        "v08/lenasexpov11.jpg"
        pause 0.03
        "v08/lenasexpov10.jpg"
        pause 0.02
        "v08/lenasexpov09.jpg"
        pause 0.02
        "v08/lenasexpov08.jpg"
        pause 0.02
        "v08/lenasexpov07.jpg"
        pause 0.02
        "v08/lenasexpov06.jpg"
        pause 0.02
        "v08/lenasexpov05.jpg"
        pause 0.02
        "v08/lenasexpov04.jpg"
        pause 0.02
        "v08/lenasexpov03.jpg"
        pause 0.02
        "v08/lenasexpov02.jpg"
        pause 0.02
        "v08/lenasexpov01.jpg"
        pause 0.02
        repeat
            
    image danablowfast:
        "v08/danasuck00.png"
        pause 0.03
        "v08/danasuck01.png"
        pause 0.03
        "v08/danasuck02.png"
        pause 0.03
        "v08/danasuck03.png"
        pause 0.03
        "v08/danasuck04.png"
        pause 0.03
        "v08/danasuck05.png"
        pause 0.03
        "v08/danasuck06.png"
        pause 0.03
        "v08/danasuck07.png"
        pause 0.03
        "v08/danasuck08.png"
        pause 0.03
        "v08/danasuck09.png"
        pause 0.03
        "v08/danasuck10.png"
        pause 0.03
        "v08/danasuck11.png"
        pause 0.04
        "v08/danasuck12.png"
        pause 0.04
        "v08/danasuck13.png"
        pause 0.04
        "v08/danasuck14.png"
        pause 0.04
        "v08/danasuck15.png"
        pause 0.04
        repeat

    image danablowslow:
        "v08/danasuck00.png"
        pause 0.05
        "v08/danasuck01.png"
        pause 0.05
        "v08/danasuck02.png"
        pause 0.05
        "v08/danasuck03.png"
        pause 0.05
        "v08/danasuck04.png"
        pause 0.05
        "v08/danasuck05.png"
        pause 0.05
        "v08/danasuck06.png"
        pause 0.05
        "v08/danasuck07.png"
        pause 0.05
        "v08/danasuck08.png"
        pause 0.05
        "v08/danasuck09.png"
        pause 0.05
        "v08/danasuck10.png"
        pause 0.05
        "v08/danasuck11.png"
        pause 0.06
        "v08/danasuck12.png"
        pause 0.06
        "v08/danasuck13.png"
        pause 0.06
        "v08/danasuck14.png"
        pause 0.06
        "v08/danasuck15.png"
        pause 0.06
        repeat
            
    image barbarahjslow:
        "v081/barbarahj00.png"
        pause 0.03
        "v081/barbarahj01.png"
        pause 0.03
        "v081/barbarahj02.png"
        pause 0.03
        "v081/barbarahj03.png"
        pause 0.03
        "v081/barbarahj04.png"
        pause 0.03
        "v081/barbarahj05.png"
        pause 0.03
        "v081/barbarahj06.png"
        pause 0.03
        "v081/barbarahj07.png"
        pause 0.03
        "v081/barbarahj08.png"
        pause 0.03
        "v081/barbarahj09.png"
        pause 0.03
        "v081/barbarahj10.png"
        pause 0.03
        "v081/barbarahj11.png"
        pause 0.03
        "v081/barbarahj12.png"
        pause 0.03
        "v081/barbarahj13.png"
        pause 0.03
        "v081/barbarahj14.png"
        pause 0.03
        "v081/barbarahj15.png"
        pause 0.04
        "v081/barbarahj14.png"
        pause 0.04
        "v081/barbarahj13.png"
        pause 0.04
        "v081/barbarahj12.png"
        pause 0.04
        "v081/barbarahj11.png"
        pause 0.04
        "v081/barbarahj10.png"
        pause 0.04
        "v081/barbarahj09.png"
        pause 0.04
        "v081/barbarahj08.png"
        pause 0.04
        "v081/barbarahj07.png"
        pause 0.04
        "v081/barbarahj06.png"
        pause 0.04
        "v081/barbarahj05.png"
        pause 0.04
        "v081/barbarahj04.png"
        pause 0.04
        "v081/barbarahj03.png"
        pause 0.04
        "v081/barbarahj02.png"
        pause 0.04
        "v081/barbarahj01.png"
        pause 0.04
        repeat
            
    image barbarahjfast:
        "v081/barbarahj00.png"
        pause 0.02
        "v081/barbarahj01.png"
        pause 0.02
        "v081/barbarahj02.png"
        pause 0.02
        "v081/barbarahj03.png"
        pause 0.02
        "v081/barbarahj04.png"
        pause 0.02
        "v081/barbarahj05.png"
        pause 0.02
        "v081/barbarahj06.png"
        pause 0.02
        "v081/barbarahj07.png"
        pause 0.02
        "v081/barbarahj08.png"
        pause 0.02
        "v081/barbarahj09.png"
        pause 0.02
        "v081/barbarahj10.png"
        pause 0.02
        "v081/barbarahj11.png"
        pause 0.02
        "v081/barbarahj12.png"
        pause 0.02
        "v081/barbarahj13.png"
        pause 0.02
        "v081/barbarahj14.png"
        pause 0.02
        "v081/barbarahj15.png"
        pause 0.03
        "v081/barbarahj14.png"
        pause 0.03
        "v081/barbarahj13.png"
        pause 0.03
        "v081/barbarahj12.png"
        pause 0.03
        "v081/barbarahj11.png"
        pause 0.03
        "v081/barbarahj10.png"
        pause 0.03
        "v081/barbarahj09.png"
        pause 0.03
        "v081/barbarahj08.png"
        pause 0.03
        "v081/barbarahj07.png"
        pause 0.03
        "v081/barbarahj06.png"
        pause 0.03
        "v081/barbarahj05.png"
        pause 0.03
        "v081/barbarahj04.png"
        pause 0.03
        "v081/barbarahj03.png"
        pause 0.03
        "v081/barbarahj02.png"
        pause 0.03
        "v081/barbarahj01.png"
        pause 0.03
        repeat
            
    image barbara02hjslow:
        "v081/barbara02hj00.png"
        pause 0.03
        "v081/barbara02hj01.png"
        pause 0.03
        "v081/barbara02hj02.png"
        pause 0.03
        "v081/barbara02hj03.png"
        pause 0.03
        "v081/barbara02hj04.png"
        pause 0.03
        "v081/barbara02hj05.png"
        pause 0.03
        "v081/barbara02hj06.png"
        pause 0.03
        "v081/barbara02hj07.png"
        pause 0.03
        "v081/barbara02hj08.png"
        pause 0.03
        "v081/barbara02hj09.png"
        pause 0.03
        "v081/barbara02hj10.png"
        pause 0.03
        "v081/barbara02hj11.png"
        pause 0.03
        "v081/barbara02hj12.png"
        pause 0.03
        "v081/barbara02hj11.png"
        pause 0.04
        "v081/barbara02hj10.png"
        pause 0.04
        "v081/barbara02hj09.png"
        pause 0.04
        "v081/barbara02hj08.png"
        pause 0.04
        "v081/barbara02hj07.png"
        pause 0.04
        "v081/barbara02hj06.png"
        pause 0.04
        "v081/barbara02hj05.png"
        pause 0.04
        "v081/barbara02hj04.png"
        pause 0.04
        "v081/barbara02hj03.png"
        pause 0.04
        "v081/barbara02hj02.png"
        pause 0.04
        "v081/barbara02hj01.png"
        pause 0.04
        repeat
            
    image barbara02hjfast:
        "v081/barbara02hj00.png"
        pause 0.02
        "v081/barbara02hj01.png"
        pause 0.02
        "v081/barbara02hj02.png"
        pause 0.02
        "v081/barbara02hj03.png"
        pause 0.02
        "v081/barbara02hj04.png"
        pause 0.02
        "v081/barbara02hj05.png"
        pause 0.02
        "v081/barbara02hj06.png"
        pause 0.02
        "v081/barbara02hj07.png"
        pause 0.02
        "v081/barbara02hj08.png"
        pause 0.02
        "v081/barbara02hj09.png"
        pause 0.02
        "v081/barbara02hj10.png"
        pause 0.02
        "v081/barbara02hj11.png"
        pause 0.02
        "v081/barbara02hj12.png"
        pause 0.02
        "v081/barbara02hj11.png"
        pause 0.03
        "v081/barbara02hj10.png"
        pause 0.03
        "v081/barbara02hj09.png"
        pause 0.03
        "v081/barbara02hj08.png"
        pause 0.03
        "v081/barbara02hj07.png"
        pause 0.03
        "v081/barbara02hj06.png"
        pause 0.03
        "v081/barbara02hj05.png"
        pause 0.03
        "v081/barbara02hj04.png"
        pause 0.03
        "v081/barbara02hj03.png"
        pause 0.03
        "v081/barbara02hj02.png"
        pause 0.03
        "v081/barbara02hj01.png"
        pause 0.03
        repeat
            
    image barbaramissionarypovslow:
        "v081/barbaramissionarypov00.png"
        pause 0.03
        "v081/barbaramissionarypov01.png"
        pause 0.03
        "v081/barbaramissionarypov02.png"
        pause 0.03
        "v081/barbaramissionarypov03.png"
        pause 0.03
        "v081/barbaramissionarypov04.png"
        pause 0.03
        "v081/barbaramissionarypov05.png"
        pause 0.03
        "v081/barbaramissionarypov06.png"
        pause 0.03
        "v081/barbaramissionarypov07.png"
        pause 0.03
        "v081/barbaramissionarypov08.png"
        pause 0.03
        "v081/barbaramissionarypov09.png"
        pause 0.03
        "v081/barbaramissionarypov10.png"
        pause 0.03
        "v081/barbaramissionarypov11.png"
        pause 0.03
        "v081/barbaramissionarypov12.png"
        pause 0.03
        "v081/barbaramissionarypov11.png"
        pause 0.04
        "v081/barbaramissionarypov10.png"
        pause 0.04
        "v081/barbaramissionarypov09.png"
        pause 0.04
        "v081/barbaramissionarypov08.png"
        pause 0.04
        "v081/barbaramissionarypov07.png"
        pause 0.04
        "v081/barbaramissionarypov06.png"
        pause 0.04
        "v081/barbaramissionarypov05.png"
        pause 0.04
        "v081/barbaramissionarypov04.png"
        pause 0.04
        "v081/barbaramissionarypov03.png"
        pause 0.04
        "v081/barbaramissionarypov02.png"
        pause 0.04
        "v081/barbaramissionarypov01.png"
        pause 0.04
        repeat
            
    image barbaramissionarypovfast:
        "v081/barbaramissionarypov00.png"
        pause 0.02
        "v081/barbaramissionarypov01.png"
        pause 0.02
        "v081/barbaramissionarypov02.png"
        pause 0.02
        "v081/barbaramissionarypov03.png"
        pause 0.02
        "v081/barbaramissionarypov04.png"
        pause 0.02
        "v081/barbaramissionarypov05.png"
        pause 0.02
        "v081/barbaramissionarypov06.png"
        pause 0.02
        "v081/barbaramissionarypov07.png"
        pause 0.02
        "v081/barbaramissionarypov08.png"
        pause 0.02
        "v081/barbaramissionarypov09.png"
        pause 0.02
        "v081/barbaramissionarypov10.png"
        pause 0.02
        "v081/barbaramissionarypov11.png"
        pause 0.02
        "v081/barbaramissionarypov12.png"
        pause 0.02
        "v081/barbaramissionarypov11.png"
        pause 0.03
        "v081/barbaramissionarypov10.png"
        pause 0.03
        "v081/barbaramissionarypov09.png"
        pause 0.03
        "v081/barbaramissionarypov08.png"
        pause 0.03
        "v081/barbaramissionarypov07.png"
        pause 0.03
        "v081/barbaramissionarypov06.png"
        pause 0.03
        "v081/barbaramissionarypov05.png"
        pause 0.03
        "v081/barbaramissionarypov04.png"
        pause 0.03
        "v081/barbaramissionarypov03.png"
        pause 0.03
        "v081/barbaramissionarypov02.png"
        pause 0.03
        "v081/barbaramissionarypov01.png"
        pause 0.03
        repeat
            
    image barbaramissionaryslow:
        "v081/barbaramissionary00.png"
        pause 0.03
        "v081/barbaramissionary01.png"
        pause 0.03
        "v081/barbaramissionary02.png"
        pause 0.03
        "v081/barbaramissionary03.png"
        pause 0.03
        "v081/barbaramissionary04.png"
        pause 0.03
        "v081/barbaramissionary05.png"
        pause 0.03
        "v081/barbaramissionary06.png"
        pause 0.03
        "v081/barbaramissionary07.png"
        pause 0.03
        "v081/barbaramissionary08.png"
        pause 0.03
        "v081/barbaramissionary09.png"
        pause 0.03
        "v081/barbaramissionary10.png"
        pause 0.03
        "v081/barbaramissionary11.png"
        pause 0.03
        "v081/barbaramissionary12.png"
        pause 0.03
        "v081/barbaramissionary11.png"
        pause 0.04
        "v081/barbaramissionary10.png"
        pause 0.04
        "v081/barbaramissionary09.png"
        pause 0.04
        "v081/barbaramissionary08.png"
        pause 0.04
        "v081/barbaramissionary07.png"
        pause 0.04
        "v081/barbaramissionary06.png"
        pause 0.04
        "v081/barbaramissionary05.png"
        pause 0.04
        "v081/barbaramissionary04.png"
        pause 0.04
        "v081/barbaramissionary03.png"
        pause 0.04
        "v081/barbaramissionary02.png"
        pause 0.04
        "v081/barbaramissionary01.png"
        pause 0.04
        repeat
            
    image barbaramissionaryfast:
        "v081/barbaramissionary00.png"
        pause 0.02
        "v081/barbaramissionary01.png"
        pause 0.02
        "v081/barbaramissionary02.png"
        pause 0.02
        "v081/barbaramissionary03.png"
        pause 0.02
        "v081/barbaramissionary04.png"
        pause 0.02
        "v081/barbaramissionary05.png"
        pause 0.02
        "v081/barbaramissionary06.png"
        pause 0.02
        "v081/barbaramissionary07.png"
        pause 0.02
        "v081/barbaramissionary08.png"
        pause 0.02
        "v081/barbaramissionary09.png"
        pause 0.02
        "v081/barbaramissionary10.png"
        pause 0.02
        "v081/barbaramissionary11.png"
        pause 0.02
        "v081/barbaramissionary12.png"
        pause 0.02
        "v081/barbaramissionary11.png"
        pause 0.03
        "v081/barbaramissionary10.png"
        pause 0.03
        "v081/barbaramissionary09.png"
        pause 0.03
        "v081/barbaramissionary08.png"
        pause 0.03
        "v081/barbaramissionary07.png"
        pause 0.03
        "v081/barbaramissionary06.png"
        pause 0.03
        "v081/barbaramissionary05.png"
        pause 0.03
        "v081/barbaramissionary04.png"
        pause 0.03
        "v081/barbaramissionary03.png"
        pause 0.03
        "v081/barbaramissionary02.png"
        pause 0.03
        "v081/barbaramissionary01.png"
        pause 0.03
        repeat
            
    image barbarafuckslow:
        "v081/barbarafuck00.png"
        pause 0.03
        "v081/barbarafuck01.png"
        pause 0.03
        "v081/barbarafuck02.png"
        pause 0.03
        "v081/barbarafuck03.png"
        pause 0.03
        "v081/barbarafuck04.png"
        pause 0.03
        "v081/barbarafuck05.png"
        pause 0.03
        "v081/barbarafuck06.png"
        pause 0.03
        "v081/barbarafuck07.png"
        pause 0.03
        "v081/barbarafuck08.png"
        pause 0.03
        "v081/barbarafuck09.png"
        pause 0.03
        "v081/barbarafuck10.png"
        pause 0.03
        "v081/barbarafuck11.png"
        pause 0.03
        "v081/barbarafuck12.png"
        pause 0.03
        "v081/barbarafuck11.png"
        pause 0.04
        "v081/barbarafuck10.png"
        pause 0.04
        "v081/barbarafuck09.png"
        pause 0.04
        "v081/barbarafuck08.png"
        pause 0.04
        "v081/barbarafuck07.png"
        pause 0.04
        "v081/barbarafuck06.png"
        pause 0.04
        "v081/barbarafuck05.png"
        pause 0.04
        "v081/barbarafuck04.png"
        pause 0.04
        "v081/barbarafuck03.png"
        pause 0.04
        "v081/barbarafuck02.png"
        pause 0.04
        "v081/barbarafuck01.png"
        pause 0.04
        repeat
            
    image barbarafuckfast:
        "v081/barbarafuck00.png"
        pause 0.02
        "v081/barbarafuck01.png"
        pause 0.02
        "v081/barbarafuck02.png"
        pause 0.02
        "v081/barbarafuck03.png"
        pause 0.02
        "v081/barbarafuck04.png"
        pause 0.02
        "v081/barbarafuck05.png"
        pause 0.02
        "v081/barbarafuck06.png"
        pause 0.02
        "v081/barbarafuck07.png"
        pause 0.02
        "v081/barbarafuck08.png"
        pause 0.02
        "v081/barbarafuck09.png"
        pause 0.02
        "v081/barbarafuck10.png"
        pause 0.02
        "v081/barbarafuck11.png"
        pause 0.02
        "v081/barbarafuck12.png"
        pause 0.02
        "v081/barbarafuck11.png"
        pause 0.03
        "v081/barbarafuck10.png"
        pause 0.03
        "v081/barbarafuck09.png"
        pause 0.03
        "v081/barbarafuck08.png"
        pause 0.03
        "v081/barbarafuck07.png"
        pause 0.03
        "v081/barbarafuck06.png"
        pause 0.03
        "v081/barbarafuck05.png"
        pause 0.03
        "v081/barbarafuck04.png"
        pause 0.03
        "v081/barbarafuck03.png"
        pause 0.03
        "v081/barbarafuck02.png"
        pause 0.03
        "v081/barbarafuck01.png"
        pause 0.03
        repeat
            
    image barbaraanalslow:
        "v081/barbaraanal00.png"
        pause 0.03
        "v081/barbaraanal01.png"
        pause 0.03
        "v081/barbaraanal02.png"
        pause 0.03
        "v081/barbaraanal03.png"
        pause 0.03
        "v081/barbaraanal04.png"
        pause 0.03
        "v081/barbaraanal05.png"
        pause 0.03
        "v081/barbaraanal06.png"
        pause 0.03
        "v081/barbaraanal07.png"
        pause 0.03
        "v081/barbaraanal08.png"
        pause 0.03
        "v081/barbaraanal09.png"
        pause 0.03
        "v081/barbaraanal10.png"
        pause 0.03
        "v081/barbaraanal11.png"
        pause 0.03
        "v081/barbaraanal12.png"
        pause 0.03
        "v081/barbaraanal11.png"
        pause 0.04
        "v081/barbaraanal10.png"
        pause 0.04
        "v081/barbaraanal09.png"
        pause 0.04
        "v081/barbaraanal08.png"
        pause 0.04
        "v081/barbaraanal07.png"
        pause 0.04
        "v081/barbaraanal06.png"
        pause 0.04
        "v081/barbaraanal05.png"
        pause 0.04
        "v081/barbaraanal04.png"
        pause 0.04
        "v081/barbaraanal03.png"
        pause 0.04
        "v081/barbaraanal02.png"
        pause 0.04
        "v081/barbaraanal01.png"
        pause 0.04
        repeat
            
    image barbaraanalfast:
        "v081/barbaraanal00.png"
        pause 0.02
        "v081/barbaraanal01.png"
        pause 0.02
        "v081/barbaraanal02.png"
        pause 0.02
        "v081/barbaraanal03.png"
        pause 0.02
        "v081/barbaraanal04.png"
        pause 0.02
        "v081/barbaraanal05.png"
        pause 0.02
        "v081/barbaraanal06.png"
        pause 0.02
        "v081/barbaraanal07.png"
        pause 0.02
        "v081/barbaraanal08.png"
        pause 0.02
        "v081/barbaraanal09.png"
        pause 0.02
        "v081/barbaraanal10.png"
        pause 0.02
        "v081/barbaraanal11.png"
        pause 0.02
        "v081/barbaraanal12.png"
        pause 0.02
        "v081/barbaraanal11.png"
        pause 0.03
        "v081/barbaraanal10.png"
        pause 0.03
        "v081/barbaraanal09.png"
        pause 0.03
        "v081/barbaraanal08.png"
        pause 0.03
        "v081/barbaraanal07.png"
        pause 0.03
        "v081/barbaraanal06.png"
        pause 0.03
        "v081/barbaraanal05.png"
        pause 0.03
        "v081/barbaraanal04.png"
        pause 0.03
        "v081/barbaraanal03.png"
        pause 0.03
        "v081/barbaraanal02.png"
        pause 0.03
        "v081/barbaraanal01.png"
        pause 0.03
        repeat
            
    image barbaraassslow:
        "v081/barbaraass00.png"
        pause 0.03
        "v081/barbaraass01.png"
        pause 0.03
        "v081/barbaraass02.png"
        pause 0.03
        "v081/barbaraass03.png"
        pause 0.03
        "v081/barbaraass04.png"
        pause 0.03
        "v081/barbaraass05.png"
        pause 0.03
        "v081/barbaraass06.png"
        pause 0.03
        "v081/barbaraass07.png"
        pause 0.03
        "v081/barbaraass08.png"
        pause 0.03
        "v081/barbaraass09.png"
        pause 0.03
        "v081/barbaraass10.png"
        pause 0.03
        "v081/barbaraass11.png"
        pause 0.03
        "v081/barbaraass12.png"
        pause 0.03
        "v081/barbaraass11.png"
        pause 0.04
        "v081/barbaraass10.png"
        pause 0.04
        "v081/barbaraass09.png"
        pause 0.04
        "v081/barbaraass08.png"
        pause 0.04
        "v081/barbaraass07.png"
        pause 0.04
        "v081/barbaraass06.png"
        pause 0.04
        "v081/barbaraass05.png"
        pause 0.04
        "v081/barbaraass04.png"
        pause 0.04
        "v081/barbaraass03.png"
        pause 0.04
        "v081/barbaraass02.png"
        pause 0.04
        "v081/barbaraass01.png"
        pause 0.04
        repeat
            
    image barbaraassfast:
        "v081/barbaraass00.png"
        pause 0.02
        "v081/barbaraass01.png"
        pause 0.02
        "v081/barbaraass02.png"
        pause 0.02
        "v081/barbaraass03.png"
        pause 0.02
        "v081/barbaraass04.png"
        pause 0.02
        "v081/barbaraass05.png"
        pause 0.02
        "v081/barbaraass06.png"
        pause 0.02
        "v081/barbaraass07.png"
        pause 0.02
        "v081/barbaraass08.png"
        pause 0.02
        "v081/barbaraass09.png"
        pause 0.02
        "v081/barbaraass10.png"
        pause 0.02
        "v081/barbaraass11.png"
        pause 0.02
        "v081/barbaraass12.png"
        pause 0.02
        "v081/barbaraass11.png"
        pause 0.03
        "v081/barbaraass10.png"
        pause 0.03
        "v081/barbaraass09.png"
        pause 0.03
        "v081/barbaraass08.png"
        pause 0.03
        "v081/barbaraass07.png"
        pause 0.03
        "v081/barbaraass06.png"
        pause 0.03
        "v081/barbaraass05.png"
        pause 0.03
        "v081/barbaraass04.png"
        pause 0.03
        "v081/barbaraass03.png"
        pause 0.03
        "v081/barbaraass02.png"
        pause 0.03
        "v081/barbaraass01.png"
        pause 0.03
        repeat
            
    image barbarasuckslow:
        "v081/barbarasuck00.jpg"
        pause 0.03
        "v081/barbarasuck01.jpg"
        pause 0.03
        "v081/barbarasuck02.jpg"
        pause 0.03
        "v081/barbarasuck03.jpg"
        pause 0.03
        "v081/barbarasuck04.jpg"
        pause 0.03
        "v081/barbarasuck05.jpg"
        pause 0.03
        "v081/barbarasuck06.jpg"
        pause 0.03
        "v081/barbarasuck07.jpg"
        pause 0.03
        "v081/barbarasuck08.jpg"
        pause 0.03
        "v081/barbarasuck09.jpg"
        pause 0.03
        "v081/barbarasuck10.jpg"
        pause 0.03
        "v081/barbarasuck11.jpg"
        pause 0.03
        "v081/barbarasuck12.jpg"
        pause 0.03
        "v081/barbarasuck11.jpg"
        pause 0.04
        "v081/barbarasuck10.jpg"
        pause 0.04
        "v081/barbarasuck09.jpg"
        pause 0.04
        "v081/barbarasuck08.jpg"
        pause 0.04
        "v081/barbarasuck07.jpg"
        pause 0.04
        "v081/barbarasuck06.jpg"
        pause 0.04
        "v081/barbarasuck05.jpg"
        pause 0.04
        "v081/barbarasuck04.jpg"
        pause 0.04
        "v081/barbarasuck03.jpg"
        pause 0.04
        "v081/barbarasuck02.jpg"
        pause 0.04
        "v081/barbarasuck01.jpg"
        pause 0.04
        repeat
            
    image barbarasuckfast:
        "v081/barbarasuck00.jpg"
        pause 0.02
        "v081/barbarasuck01.jpg"
        pause 0.02
        "v081/barbarasuck02.jpg"
        pause 0.02
        "v081/barbarasuck03.jpg"
        pause 0.02
        "v081/barbarasuck04.jpg"
        pause 0.02
        "v081/barbarasuck05.jpg"
        pause 0.02
        "v081/barbarasuck06.jpg"
        pause 0.02
        "v081/barbarasuck07.jpg"
        pause 0.02
        "v081/barbarasuck08.jpg"
        pause 0.02
        "v081/barbarasuck09.jpg"
        pause 0.02
        "v081/barbarasuck10.jpg"
        pause 0.02
        "v081/barbarasuck11.jpg"
        pause 0.02
        "v081/barbarasuck12.jpg"
        pause 0.02
        "v081/barbarasuck11.jpg"
        pause 0.03
        "v081/barbarasuck10.jpg"
        pause 0.03
        "v081/barbarasuck09.jpg"
        pause 0.03
        "v081/barbarasuck08.jpg"
        pause 0.03
        "v081/barbarasuck07.jpg"
        pause 0.03
        "v081/barbarasuck06.jpg"
        pause 0.03
        "v081/barbarasuck05.jpg"
        pause 0.03
        "v081/barbarasuck04.jpg"
        pause 0.03
        "v081/barbarasuck03.jpg"
        pause 0.03
        "v081/barbarasuck02.jpg"
        pause 0.03
        "v081/barbarasuck01.jpg"
        pause 0.03
        repeat
            
    image barbaradildoslow:
        "v081/barbaradildo00.jpg"
        pause 0.03
        "v081/barbaradildo01.jpg"
        pause 0.03
        "v081/barbaradildo02.jpg"
        pause 0.03
        "v081/barbaradildo03.jpg"
        pause 0.03
        "v081/barbaradildo04.jpg"
        pause 0.03
        "v081/barbaradildo05.jpg"
        pause 0.03
        "v081/barbaradildo06.jpg"
        pause 0.03
        "v081/barbaradildo07.jpg"
        pause 0.03
        "v081/barbaradildo08.jpg"
        pause 0.03
        "v081/barbaradildo09.jpg"
        pause 0.03
        "v081/barbaradildo10.jpg"
        pause 0.03
        "v081/barbaradildo09.jpg"
        pause 0.04
        "v081/barbaradildo08.jpg"
        pause 0.04
        "v081/barbaradildo07.jpg"
        pause 0.04
        "v081/barbaradildo06.jpg"
        pause 0.04
        "v081/barbaradildo05.jpg"
        pause 0.04
        "v081/barbaradildo04.jpg"
        pause 0.04
        "v081/barbaradildo03.jpg"
        pause 0.04
        "v081/barbaradildo02.jpg"
        pause 0.04
        "v081/barbaradildo01.jpg"
        pause 0.04
        repeat
            
    image barbaradildofast:
        "v081/barbaradildo00.jpg"
        pause 0.02
        "v081/barbaradildo01.jpg"
        pause 0.02
        "v081/barbaradildo02.jpg"
        pause 0.02
        "v081/barbaradildo03.jpg"
        pause 0.02
        "v081/barbaradildo04.jpg"
        pause 0.02
        "v081/barbaradildo05.jpg"
        pause 0.02
        "v081/barbaradildo06.jpg"
        pause 0.02
        "v081/barbaradildo07.jpg"
        pause 0.02
        "v081/barbaradildo08.jpg"
        pause 0.02
        "v081/barbaradildo09.jpg"
        pause 0.02
        "v081/barbaradildo10.jpg"
        pause 0.02
        "v081/barbaradildo09.jpg"
        pause 0.03
        "v081/barbaradildo08.jpg"
        pause 0.03
        "v081/barbaradildo07.jpg"
        pause 0.03
        "v081/barbaradildo06.jpg"
        pause 0.03
        "v081/barbaradildo05.jpg"
        pause 0.03
        "v081/barbaradildo04.jpg"
        pause 0.03
        "v081/barbaradildo03.jpg"
        pause 0.03
        "v081/barbaradildo02.jpg"
        pause 0.03
        "v081/barbaradildo01.jpg"
        pause 0.03
        repeat
    
    image barbaraimpregslow:
        "v081/barbaraimpreg00.jpg"
        pause 0.03
        "v081/barbaraimpreg01.jpg"
        pause 0.03
        "v081/barbaraimpreg02.jpg"
        pause 0.03
        "v081/barbaraimpreg03.jpg"
        pause 0.03
        "v081/barbaraimpreg04.jpg"
        pause 0.03
        "v081/barbaraimpreg05.jpg"
        pause 0.03
        "v081/barbaraimpreg06.jpg"
        pause 0.03
        "v081/barbaraimpreg07.jpg"
        pause 0.03
        "v081/barbaraimpreg08.jpg"
        pause 0.03
        "v081/barbaraimpreg09.jpg"
        pause 0.03
        "v081/barbaraimpreg10.jpg"
        pause 0.03
        "v081/barbaraimpreg11.jpg"
        pause 0.03
        "v081/barbaraimpreg12.jpg"
        pause 0.03
        "v081/barbaraimpreg11.jpg"
        pause 0.04
        "v081/barbaraimpreg10.jpg"
        pause 0.04
        "v081/barbaraimpreg09.jpg"
        pause 0.04
        "v081/barbaraimpreg08.jpg"
        pause 0.04
        "v081/barbaraimpreg07.jpg"
        pause 0.04
        "v081/barbaraimpreg06.jpg"
        pause 0.04
        "v081/barbaraimpreg05.jpg"
        pause 0.04
        "v081/barbaraimpreg04.jpg"
        pause 0.04
        "v081/barbaraimpreg03.jpg"
        pause 0.04
        "v081/barbaraimpreg02.jpg"
        pause 0.04
        "v081/barbaraimpreg01.jpg"
        pause 0.04
        repeat
            
    image barbaraimpregfast:
        "v081/barbaraimpreg00.jpg"
        pause 0.02
        "v081/barbaraimpreg01.jpg"
        pause 0.02
        "v081/barbaraimpreg02.jpg"
        pause 0.02
        "v081/barbaraimpreg03.jpg"
        pause 0.02
        "v081/barbaraimpreg04.jpg"
        pause 0.02
        "v081/barbaraimpreg05.jpg"
        pause 0.02
        "v081/barbaraimpreg06.jpg"
        pause 0.02
        "v081/barbaraimpreg07.jpg"
        pause 0.02
        "v081/barbaraimpreg08.jpg"
        pause 0.02
        "v081/barbaraimpreg09.jpg"
        pause 0.02
        "v081/barbaraimpreg10.jpg"
        pause 0.02
        "v081/barbaraimpreg11.jpg"
        pause 0.02
        "v081/barbaraimpreg12.jpg"
        pause 0.02
        "v081/barbaraimpreg11.jpg"
        pause 0.03
        "v081/barbaraimpreg10.jpg"
        pause 0.03
        "v081/barbaraimpreg09.jpg"
        pause 0.03
        "v081/barbaraimpreg08.jpg"
        pause 0.03
        "v081/barbaraimpreg07.jpg"
        pause 0.03
        "v081/barbaraimpreg06.jpg"
        pause 0.03
        "v081/barbaraimpreg05.jpg"
        pause 0.03
        "v081/barbaraimpreg04.jpg"
        pause 0.03
        "v081/barbaraimpreg03.jpg"
        pause 0.03
        "v081/barbaraimpreg02.jpg"
        pause 0.03
        "v081/barbaraimpreg01.jpg"
        pause 0.03
        repeat
            
    image barbaraimpregpovslow:
        "v081/barbaraimpregpov00.png"
        pause 0.03
        "v081/barbaraimpregpov01.png"
        pause 0.03
        "v081/barbaraimpregpov02.png"
        pause 0.03
        "v081/barbaraimpregpov03.png"
        pause 0.03
        "v081/barbaraimpregpov04.png"
        pause 0.03
        "v081/barbaraimpregpov05.png"
        pause 0.03
        "v081/barbaraimpregpov06.png"
        pause 0.03
        "v081/barbaraimpregpov07.png"
        pause 0.03
        "v081/barbaraimpregpov08.png"
        pause 0.03
        "v081/barbaraimpregpov09.png"
        pause 0.03
        "v081/barbaraimpregpov10.png"
        pause 0.03
        "v081/barbaraimpregpov11.png"
        pause 0.03
        "v081/barbaraimpregpov12.png"
        pause 0.03
        "v081/barbaraimpregpov11.png"
        pause 0.04
        "v081/barbaraimpregpov10.png"
        pause 0.04
        "v081/barbaraimpregpov09.png"
        pause 0.04
        "v081/barbaraimpregpov08.png"
        pause 0.04
        "v081/barbaraimpregpov07.png"
        pause 0.04
        "v081/barbaraimpregpov06.png"
        pause 0.04
        "v081/barbaraimpregpov05.png"
        pause 0.04
        "v081/barbaraimpregpov04.png"
        pause 0.04
        "v081/barbaraimpregpov03.png"
        pause 0.04
        "v081/barbaraimpregpov02.png"
        pause 0.04
        "v081/barbaraimpregpov01.png"
        pause 0.04
        repeat
            
    image barbaraimpregpovfast:
        "v081/barbaraimpregpov00.png"
        pause 0.02
        "v081/barbaraimpregpov01.png"
        pause 0.02
        "v081/barbaraimpregpov02.png"
        pause 0.02
        "v081/barbaraimpregpov03.png"
        pause 0.02
        "v081/barbaraimpregpov04.png"
        pause 0.02
        "v081/barbaraimpregpov05.png"
        pause 0.02
        "v081/barbaraimpregpov06.png"
        pause 0.02
        "v081/barbaraimpregpov07.png"
        pause 0.02
        "v081/barbaraimpregpov08.png"
        pause 0.02
        "v081/barbaraimpregpov09.png"
        pause 0.02
        "v081/barbaraimpregpov10.png"
        pause 0.02
        "v081/barbaraimpregpov11.png"
        pause 0.02
        "v081/barbaraimpregpov12.png"
        pause 0.02
        "v081/barbaraimpregpov11.png"
        pause 0.03
        "v081/barbaraimpregpov10.png"
        pause 0.03
        "v081/barbaraimpregpov09.png"
        pause 0.03
        "v081/barbaraimpregpov08.png"
        pause 0.03
        "v081/barbaraimpregpov07.png"
        pause 0.03
        "v081/barbaraimpregpov06.png"
        pause 0.03
        "v081/barbaraimpregpov05.png"
        pause 0.03
        "v081/barbaraimpregpov04.png"
        pause 0.03
        "v081/barbaraimpregpov03.png"
        pause 0.03
        "v081/barbaraimpregpov02.png"
        pause 0.03
        "v081/barbaraimpregpov01.png"
        pause 0.03
        repeat
    
    image barbarawiggle:
        "v081/barbarawiggle00.png"
        pause 0.03
        "v081/barbarawiggle01.png"
        pause 0.03
        "v081/barbarawiggle02.png"
        pause 0.03
        "v081/barbarawiggle03.png"
        pause 0.03
        "v081/barbarawiggle04.png"
        pause 0.03
        "v081/barbarawiggle05.png"
        pause 0.03
        "v081/barbarawiggle06.png"
        pause 0.03
        "v081/barbarawiggle07.png"
        pause 0.03
        "v081/barbarawiggle08.png"
        pause 0.03
        "v081/barbarawiggle09.png"
        pause 0.03
        "v081/barbarawiggle10.png"
        pause 0.03
        "v081/barbarawiggle11.png"
        pause 0.03
        "v081/barbarawiggle12.png"
        pause 0.03
        "v081/barbarawiggle13.png"
        pause 0.03
        "v081/barbarawiggle14.png"
        pause 0.03
        "v081/barbarawiggle15.png"
        pause 0.03
        "v081/barbarawiggle16.png"
        pause 0.03
        "v081/barbarawiggle17.png"
        pause 0.03
        "v081/barbarawiggle18.png"
        pause 0.03
        "v081/barbarawiggle19.png"
        pause 0.03
        "v081/barbarawiggle20.png"
        pause 0.03
        "v081/barbarawiggle21.png"
        pause 0.03
        "v081/barbarawiggle22.png"
        pause 0.03
        "v081/barbarawiggle23.png"
        pause 0.03
        "v081/barbarawiggle24.png"
        pause 0.03
        "v081/barbarawiggle25.png"
        pause 0.03
        repeat
            
    image kristatitsslow:
        "v081/kristatits00.png"
        pause 0.03
        "v081/kristatits01.png"
        pause 0.03
        "v081/kristatits02.png"
        pause 0.03
        "v081/kristatits03.png"
        pause 0.03
        "v081/kristatits04.png"
        pause 0.03
        "v081/kristatits05.png"
        pause 0.03
        "v081/kristatits06.png"
        pause 0.03
        "v081/kristatits07.png"
        pause 0.03
        "v081/kristatits08.png"
        pause 0.03
        "v081/kristatits09.png"
        pause 0.03
        "v081/kristatits10.png"
        pause 0.03
        "v081/kristatits11.png"
        pause 0.03
        "v081/kristatits10.png"
        pause 0.04
        "v081/kristatits09.png"
        pause 0.04
        "v081/kristatits08.png"
        pause 0.04
        "v081/kristatits07.png"
        pause 0.04
        "v081/kristatits06.png"
        pause 0.04
        "v081/kristatits05.png"
        pause 0.04
        "v081/kristatits04.png"
        pause 0.04
        "v081/kristatits03.png"
        pause 0.04
        "v081/kristatits02.png"
        pause 0.04
        "v081/kristatits01.png"
        pause 0.04
        repeat
            
    image kristatitsfast:
        "v081/kristatits00.png"
        pause 0.02
        "v081/kristatits01.png"
        pause 0.02
        "v081/kristatits02.png"
        pause 0.02
        "v081/kristatits03.png"
        pause 0.02
        "v081/kristatits04.png"
        pause 0.02
        "v081/kristatits05.png"
        pause 0.02
        "v081/kristatits06.png"
        pause 0.02
        "v081/kristatits07.png"
        pause 0.02
        "v081/kristatits08.png"
        pause 0.02
        "v081/kristatits09.png"
        pause 0.02
        "v081/kristatits10.png"
        pause 0.02
        "v081/kristatits11.png"
        pause 0.02
        "v081/kristatits10.png"
        pause 0.03
        "v081/kristatits09.png"
        pause 0.03
        "v081/kristatits08.png"
        pause 0.03
        "v081/kristatits07.png"
        pause 0.03
        "v081/kristatits06.png"
        pause 0.03
        "v081/kristatits05.png"
        pause 0.03
        "v081/kristatits04.png"
        pause 0.03
        "v081/kristatits03.png"
        pause 0.03
        "v081/kristatits02.png"
        pause 0.03
        "v081/kristatits01.png"
        pause 0.03
        repeat
            
    image kristatitspovslow:
        "v081/kristatitspov00.png"
        pause 0.03
        "v081/kristatitspov01.png"
        pause 0.03
        "v081/kristatitspov02.png"
        pause 0.03
        "v081/kristatitspov03.png"
        pause 0.03
        "v081/kristatitspov04.png"
        pause 0.03
        "v081/kristatitspov05.png"
        pause 0.03
        "v081/kristatitspov06.png"
        pause 0.03
        "v081/kristatitspov07.png"
        pause 0.03
        "v081/kristatitspov08.png"
        pause 0.03
        "v081/kristatitspov09.png"
        pause 0.03
        "v081/kristatitspov10.png"
        pause 0.03
        "v081/kristatitspov11.png"
        pause 0.03
        "v081/kristatitspov10.png"
        pause 0.04
        "v081/kristatitspov09.png"
        pause 0.04
        "v081/kristatitspov08.png"
        pause 0.04
        "v081/kristatitspov07.png"
        pause 0.04
        "v081/kristatitspov06.png"
        pause 0.04
        "v081/kristatitspov05.png"
        pause 0.04
        "v081/kristatitspov04.png"
        pause 0.04
        "v081/kristatitspov03.png"
        pause 0.04
        "v081/kristatitspov02.png"
        pause 0.04
        "v081/kristatitspov01.png"
        pause 0.04
        repeat
            
    image kristatitspovfast:
        "v081/kristatitspov00.png"
        pause 0.02
        "v081/kristatitspov01.png"
        pause 0.02
        "v081/kristatitspov02.png"
        pause 0.02
        "v081/kristatitspov03.png"
        pause 0.02
        "v081/kristatitspov04.png"
        pause 0.02
        "v081/kristatitspov05.png"
        pause 0.02
        "v081/kristatitspov06.png"
        pause 0.02
        "v081/kristatitspov07.png"
        pause 0.02
        "v081/kristatitspov08.png"
        pause 0.02
        "v081/kristatitspov09.png"
        pause 0.02
        "v081/kristatitspov10.png"
        pause 0.02
        "v081/kristatitspov11.png"
        pause 0.02
        "v081/kristatitspov10.png"
        pause 0.03
        "v081/kristatitspov09.png"
        pause 0.03
        "v081/kristatitspov08.png"
        pause 0.03
        "v081/kristatitspov07.png"
        pause 0.03
        "v081/kristatitspov06.png"
        pause 0.03
        "v081/kristatitspov05.png"
        pause 0.03
        "v081/kristatitspov04.png"
        pause 0.03
        "v081/kristatitspov03.png"
        pause 0.03
        "v081/kristatitspov02.png"
        pause 0.03
        "v081/kristatitspov01.png"
        pause 0.03
        repeat
            
    image paulettewankslow:
        "v081/paulettewank00.jpg"
        pause 0.03
        "v081/paulettewank01.jpg"
        pause 0.03
        "v081/paulettewank02.jpg"
        pause 0.03
        "v081/paulettewank03.jpg"
        pause 0.03
        "v081/paulettewank04.jpg"
        pause 0.03
        "v081/paulettewank05.jpg"
        pause 0.03
        "v081/paulettewank06.jpg"
        pause 0.03
        "v081/paulettewank07.jpg"
        pause 0.03
        "v081/paulettewank08.jpg"
        pause 0.03
        "v081/paulettewank09.jpg"
        pause 0.03
        "v081/paulettewank10.jpg"
        pause 0.03
        "v081/paulettewank11.jpg"
        pause 0.03
        "v081/paulettewank12.jpg"
        pause 0.03
        "v081/paulettewank11.jpg"
        pause 0.035
        "v081/paulettewank10.jpg"
        pause 0.035
        "v081/paulettewank09.jpg"
        pause 0.035
        "v081/paulettewank08.jpg"
        pause 0.035
        "v081/paulettewank07.jpg"
        pause 0.035
        "v081/paulettewank06.jpg"
        pause 0.035
        "v081/paulettewank05.jpg"
        pause 0.035
        "v081/paulettewank04.jpg"
        pause 0.035
        "v081/paulettewank03.jpg"
        pause 0.035
        "v081/paulettewank02.jpg"
        pause 0.035
        "v081/paulettewank01.jpg"
        pause 0.035
        repeat
            
    image paulettewankfast:
        "v081/paulettewank00.jpg"
        pause 0.02
        "v081/paulettewank01.jpg"
        pause 0.02
        "v081/paulettewank02.jpg"
        pause 0.02
        "v081/paulettewank03.jpg"
        pause 0.02
        "v081/paulettewank04.jpg"
        pause 0.02
        "v081/paulettewank05.jpg"
        pause 0.02
        "v081/paulettewank06.jpg"
        pause 0.02
        "v081/paulettewank07.jpg"
        pause 0.02
        "v081/paulettewank08.jpg"
        pause 0.02
        "v081/paulettewank09.jpg"
        pause 0.02
        "v081/paulettewank10.jpg"
        pause 0.02
        "v081/paulettewank11.jpg"
        pause 0.02
        "v081/paulettewank12.jpg"
        pause 0.02
        "v081/paulettewank11.jpg"
        pause 0.025
        "v081/paulettewank10.jpg"
        pause 0.025
        "v081/paulettewank09.jpg"
        pause 0.025
        "v081/paulettewank08.jpg"
        pause 0.025
        "v081/paulettewank07.jpg"
        pause 0.025
        "v081/paulettewank06.jpg"
        pause 0.025
        "v081/paulettewank05.jpg"
        pause 0.025
        "v081/paulettewank04.jpg"
        pause 0.025
        "v081/paulettewank03.jpg"
        pause 0.025
        "v081/paulettewank02.jpg"
        pause 0.025
        "v081/paulettewank01.jpg"
        pause 0.025
        repeat
            
    image paulettesexfast:
        "v081/paulettesex12.png"
        pause 0.05
        "v081/paulettesex13.png"
        pause 0.03
        "v081/paulettesex14.png"
        pause 0.03
        "v081/paulettesex15.png"
        pause 0.03
        "v081/paulettesex16.png"
        pause 0.03
        "v081/paulettesex17.png"
        pause 0.03
        "v081/paulettesex18.png"
        pause 0.03
        "v081/paulettesex19.png"
        pause 0.03
        "v081/paulettesex20.png"
        pause 0.03
        "v081/paulettesex21.png"
        pause 0.03
        "v081/paulettesex22.png"
        pause 0.03
        "v081/paulettesex23.png"
        pause 0.03
        "v081/paulettesex00.png"
        pause 0.04
        "v081/paulettesex01.png"
        pause 0.04
        "v081/paulettesex02.png"
        pause 0.04
        "v081/paulettesex03.png"
        pause 0.04
        "v081/paulettesex04.png"
        pause 0.04
        "v081/paulettesex05.png"
        pause 0.04
        "v081/paulettesex06.png"
        pause 0.04
        "v081/paulettesex07.png"
        pause 0.04
        "v081/paulettesex08.png"
        pause 0.04
        "v081/paulettesex09.png"
        pause 0.04
        "v081/paulettesex10.png"
        pause 0.04
        "v081/paulettesex11.png"
        pause 0.04
        repeat
            
    image paulettesexslow:
        "v081/paulettesex12.png"
        pause 0.06
        "v081/paulettesex13.png"
        pause 0.04
        "v081/paulettesex14.png"
        pause 0.04
        "v081/paulettesex15.png"
        pause 0.04
        "v081/paulettesex16.png"
        pause 0.04
        "v081/paulettesex17.png"
        pause 0.04
        "v081/paulettesex18.png"
        pause 0.04
        "v081/paulettesex19.png"
        pause 0.04
        "v081/paulettesex20.png"
        pause 0.04
        "v081/paulettesex21.png"
        pause 0.04
        "v081/paulettesex22.png"
        pause 0.04
        "v081/paulettesex23.png"
        pause 0.04
        "v081/paulettesex00.png"
        pause 0.05
        "v081/paulettesex01.png"
        pause 0.05
        "v081/paulettesex02.png"
        pause 0.05
        "v081/paulettesex03.png"
        pause 0.05
        "v081/paulettesex04.png"
        pause 0.05
        "v081/paulettesex05.png"
        pause 0.05
        "v081/paulettesex06.png"
        pause 0.05
        "v081/paulettesex07.png"
        pause 0.05
        "v081/paulettesex08.png"
        pause 0.05
        "v081/paulettesex09.png"
        pause 0.05
        "v081/paulettesex10.png"
        pause 0.05
        "v081/paulettesex11.png"
        pause 0.05
        repeat
            
    image paulettefuckslow:
        "v081/paulettefuck12.png"
        pause 0.04
        "v081/paulettefuck11.png"
        pause 0.04
        "v081/paulettefuck10.png"
        pause 0.04
        "v081/paulettefuck09.png"
        pause 0.04
        "v081/paulettefuck08.png"
        pause 0.04
        "v081/paulettefuck07.png"
        pause 0.04
        "v081/paulettefuck06.png"
        pause 0.04
        "v081/paulettefuck05.png"
        pause 0.04
        "v081/paulettefuck04.png"
        pause 0.04
        "v081/paulettefuck03.png"
        pause 0.05
        "v081/paulettefuck04.png"
        pause 0.05
        "v081/paulettefuck05.png"
        pause 0.05
        "v081/paulettefuck06.png"
        pause 0.05
        "v081/paulettefuck07.png"
        pause 0.05
        "v081/paulettefuck08.png"
        pause 0.05
        "v081/paulettefuck09.png"
        pause 0.05
        "v081/paulettefuck10.png"
        pause 0.05
        "v081/paulettefuck11.png"
        pause 0.05
        repeat
            
    image paulettefuckfast:
        "v081/paulettefuck12.png"
        pause 0.025
        "v081/paulettefuck11.png"
        pause 0.02
        "v081/paulettefuck10.png"
        pause 0.02
        "v081/paulettefuck09.png"
        pause 0.02
        "v081/paulettefuck08.png"
        pause 0.02
        "v081/paulettefuck07.png"
        pause 0.02
        "v081/paulettefuck06.png"
        pause 0.02
        "v081/paulettefuck05.png"
        pause 0.02
        "v081/paulettefuck04.png"
        pause 0.02
        "v081/paulettefuck03.png"
        pause 0.02
        "v081/paulettefuck02.png"
        pause 0.02
        "v081/paulettefuck01.png"
        pause 0.025
        "v081/paulettefuck02.png"
        pause 0.025
        "v081/paulettefuck03.png"
        pause 0.025
        "v081/paulettefuck04.png"
        pause 0.025
        "v081/paulettefuck05.png"
        pause 0.025
        "v081/paulettefuck06.png"
        pause 0.025
        "v081/paulettefuck07.png"
        pause 0.025
        "v081/paulettefuck08.png"
        pause 0.025
        "v081/paulettefuck09.png"
        pause 0.025
        "v081/paulettefuck10.png"
        pause 0.025
        "v081/paulettefuck11.png"
        pause 0.025
        repeat

    image paulettefuckcum:
        "v081/paulettefuck12.png"
        pause 0.025
        "v081/paulettefuck11.png"
        pause 0.02
        "v081/paulettefuck10.png"
        pause 0.02
        "v081/paulettefuck09.png"
        pause 0.02
        "v081/paulettefuck08cum.png"
        pause 0.02
        "v081/paulettefuck07cum.png"
        pause 0.02
        "v081/paulettefuck06cum.png"
        pause 0.02
        "v081/paulettefuck05cum.png"
        pause 0.02
        "v081/paulettefuck04cum.png"
        pause 0.02
        "v081/paulettefuck03cum.png"
        pause 0.02
        "v081/paulettefuck02cum.png"
        pause 0.02
        "v081/paulettefuck01cum.png"
        pause 0.025
        "v081/paulettefuck02cumb.png"
        pause 0.025
        "v081/paulettefuck03cumb.png"
        pause 0.025
        "v081/paulettefuck04cumb.png"
        pause 0.025
        "v081/paulettefuck05cumb.png"
        pause 0.025
        "v081/paulettefuck06cumb.png"
        pause 0.025
        "v081/paulettefuck07.png"
        pause 0.025
        "v081/paulettefuck08.png"
        pause 0.025
        "v081/paulettefuck09.png"
        pause 0.025
        "v081/paulettefuck10.png"
        pause 0.025
        "v081/paulettefuck11.png"
        pause 0.025
        repeat
             
    image bellalegslow:
        "v082/bellaleg00.png"
        pause 0.06
        "v082/bellaleg01.png"
        pause 0.06
        "v082/bellaleg02.png"
        pause 0.06
        "v082/bellaleg03.png"
        pause 0.06
        "v082/bellaleg04.png"
        pause 0.06
        "v082/bellaleg05.png"
        pause 0.06
        "v082/bellaleg06.png"
        pause 0.06
        "v082/bellaleg07.png"
        pause 0.06
        "v082/bellaleg08.png"
        pause 0.06
        "v082/bellaleg09.png"
        pause 0.06
        "v082/bellaleg10.png"
        pause 0.06
        "v082/bellaleg11.png"
        pause 0.06
        "v082/bellaleg12.png"
        pause 0.06
        "v082/bellaleg13.png"
        pause 0.06
        repeat
            
    image bellalegfast:
        "v082/bellaleg00.png"
        pause 0.04
        "v082/bellaleg01.png"
        pause 0.04
        "v082/bellaleg02.png"
        pause 0.04
        "v082/bellaleg03.png"
        pause 0.04
        "v082/bellaleg04.png"
        pause 0.04
        "v082/bellaleg05.png"
        pause 0.04
        "v082/bellaleg06.png"
        pause 0.04
        "v082/bellaleg07.png"
        pause 0.04
        "v082/bellaleg08.png"
        pause 0.04
        "v082/bellaleg09.png"
        pause 0.04
        "v082/bellaleg10.png"
        pause 0.04
        "v082/bellaleg11.png"
        pause 0.04
        "v082/bellaleg12.png"
        pause 0.04
        "v082/bellaleg13.png"
        pause 0.04
        repeat

    image bellalegcum:
        "v082/bellalegcum00.png"
        pause 0.04
        "v082/bellalegcum01.png"
        pause 0.04
        "v082/bellalegcum02.png"
        pause 0.04
        "v082/bellalegcum03.png"
        pause 0.04
        "v082/bellalegcum04.png"
        pause 0.04
        "v082/bellalegcum05.png"
        pause 0.04
        "v082/bellalegcum06.png"
        pause 0.04
        "v082/bellalegcum07.png"
        pause 0.04
        "v082/bellalegcum08.png"
        pause 0.04
        "v082/bellalegcum09.png"
        pause 0.04
        "v082/bellaleg10.png"
        pause 0.04
        "v082/bellaleg11.png"
        pause 0.04
        "v082/bellaleg12.png"
        pause 0.04
        "v082/bellaleg13.png"
        pause 0.04
        repeat

    image bellarideslow:
        "v082/bellaride00.png"
        pause 0.03
        "v082/bellaride01.png"
        pause 0.03
        "v082/bellaride02.png"
        pause 0.03
        "v082/bellaride03.png"
        pause 0.03
        "v082/bellaride04.png"
        pause 0.03
        "v082/bellaride05.png"
        pause 0.03
        "v082/bellaride06.png"
        pause 0.03
        "v082/bellaride07.png"
        pause 0.03
        "v082/bellaride08.png"
        pause 0.03
        "v082/bellaride09.png"
        pause 0.03
        "v082/bellaride10.png"
        pause 0.03
        "v082/bellaride11.png"
        pause 0.03
        "v082/bellaride12.png"
        pause 0.03
        "v082/bellaride13.png"
        pause 0.035
        "v082/bellaride14.png"
        pause 0.035
        "v082/bellaride15.png"
        pause 0.035
        "v082/bellaride16.png"
        pause 0.035
        "v082/bellaride17.png"
        pause 0.035
        "v082/bellaride18.png"
        pause 0.035
        "v082/bellaride19.png"
        pause 0.035
        "v082/bellaride20.png"
        pause 0.035
        "v082/bellaride21.png"
        pause 0.035
        "v082/bellaride22.png"
        pause 0.035
        "v082/bellaride23.png"
        pause 0.035
        repeat
            
    image bellaridefast:
        "v082/bellaride00.png"
        pause 0.02
        "v082/bellaride01.png"
        pause 0.02
        "v082/bellaride02.png"
        pause 0.02
        "v082/bellaride03.png"
        pause 0.02
        "v082/bellaride04.png"
        pause 0.02
        "v082/bellaride05.png"
        pause 0.02
        "v082/bellaride06.png"
        pause 0.02
        "v082/bellaride07.png"
        pause 0.02
        "v082/bellaride08.png"
        pause 0.02
        "v082/bellaride09.png"
        pause 0.02
        "v082/bellaride10.png"
        pause 0.02
        "v082/bellaride11.png"
        pause 0.02
        "v082/bellaride12.png"
        pause 0.02
        "v082/bellaride13.png"
        pause 0.025
        "v082/bellaride14.png"
        pause 0.025
        "v082/bellaride15.png"
        pause 0.025
        "v082/bellaride16.png"
        pause 0.025
        "v082/bellaride17.png"
        pause 0.025
        "v082/bellaride18.png"
        pause 0.025
        "v082/bellaride19.png"
        pause 0.025
        "v082/bellaride20.png"
        pause 0.025
        "v082/bellaride21.png"
        pause 0.025
        "v082/bellaride22.png"
        pause 0.025
        "v082/bellaride23.png"
        pause 0.025
        repeat
            
    image bellaridepovslow:
        "v082/bellaridepov00.png"
        pause 0.03
        "v082/bellaridepov01.png"
        pause 0.03
        "v082/bellaridepov02.png"
        pause 0.03
        "v082/bellaridepov03.png"
        pause 0.03
        "v082/bellaridepov04.png"
        pause 0.03
        "v082/bellaridepov05.png"
        pause 0.03
        "v082/bellaridepov06.png"
        pause 0.03
        "v082/bellaridepov07.png"
        pause 0.03
        "v082/bellaridepov08.png"
        pause 0.03
        "v082/bellaridepov09.png"
        pause 0.03
        "v082/bellaridepov10.png"
        pause 0.03
        "v082/bellaridepov11.png"
        pause 0.03
        "v082/bellaridepov12.png"
        pause 0.03
        "v082/bellaridepov13.png"
        pause 0.035
        "v082/bellaridepov14.png"
        pause 0.035
        "v082/bellaridepov15.png"
        pause 0.035
        "v082/bellaridepov16.png"
        pause 0.035
        "v082/bellaridepov17.png"
        pause 0.035
        "v082/bellaridepov18.png"
        pause 0.035
        "v082/bellaridepov19.png"
        pause 0.035
        "v082/bellaridepov20.png"
        pause 0.035
        "v082/bellaridepov21.png"
        pause 0.035
        "v082/bellaridepov22.png"
        pause 0.035
        "v082/bellaridepov23.png"
        pause 0.035
        repeat
            
    image bellaridepovfast:
        "v082/bellaridepov00.png"
        pause 0.02
        "v082/bellaridepov01.png"
        pause 0.02
        "v082/bellaridepov02.png"
        pause 0.02
        "v082/bellaridepov03.png"
        pause 0.02
        "v082/bellaridepov04.png"
        pause 0.02
        "v082/bellaridepov05.png"
        pause 0.02
        "v082/bellaridepov06.png"
        pause 0.02
        "v082/bellaridepov07.png"
        pause 0.02
        "v082/bellaridepov08.png"
        pause 0.02
        "v082/bellaridepov09.png"
        pause 0.02
        "v082/bellaridepov10.png"
        pause 0.02
        "v082/bellaridepov11.png"
        pause 0.02
        "v082/bellaridepov12.png"
        pause 0.02
        "v082/bellaridepov13.png"
        pause 0.025
        "v082/bellaridepov14.png"
        pause 0.025
        "v082/bellaridepov15.png"
        pause 0.025
        "v082/bellaridepov16.png"
        pause 0.025
        "v082/bellaridepov17.png"
        pause 0.025
        "v082/bellaridepov18.png"
        pause 0.025
        "v082/bellaridepov19.png"
        pause 0.025
        "v082/bellaridepov20.png"
        pause 0.025
        "v082/bellaridepov21.png"
        pause 0.025
        "v082/bellaridepov22.png"
        pause 0.025
        "v082/bellaridepov23.png"
        pause 0.025
        repeat

    image bellasexslow:
        "v082/bellasex00.jpg"
        pause 0.03
        "v082/bellasex01.jpg"
        pause 0.03
        "v082/bellasex02.jpg"
        pause 0.03
        "v082/bellasex03.jpg"
        pause 0.03
        "v082/bellasex04.jpg"
        pause 0.03
        "v082/bellasex05.jpg"
        pause 0.03
        "v082/bellasex06.jpg"
        pause 0.03
        "v082/bellasex07.jpg"
        pause 0.03
        "v082/bellasex08.jpg"
        pause 0.03
        "v082/bellasex09.jpg"
        pause 0.03
        "v082/bellasex10.jpg"
        pause 0.03
        "v082/bellasex11.jpg"
        pause 0.03
        "v082/bellasex12.jpg"
        pause 0.03
        "v082/bellasex13.jpg"
        pause 0.035
        "v082/bellasex14.jpg"
        pause 0.035
        "v082/bellasex15.jpg"
        pause 0.035
        "v082/bellasex16.jpg"
        pause 0.035
        "v082/bellasex17.jpg"
        pause 0.035
        "v082/bellasex18.jpg"
        pause 0.035
        "v082/bellasex19.jpg"
        pause 0.035
        "v082/bellasex20.jpg"
        pause 0.035
        "v082/bellasex21.jpg"
        pause 0.035
        "v082/bellasex22.jpg"
        pause 0.035
        "v082/bellasex23.jpg"
        pause 0.035
        repeat
            
    image bellasexfast:
        "v082/bellasex00.jpg"
        pause 0.02
        "v082/bellasex01.jpg"
        pause 0.02
        "v082/bellasex02.jpg"
        pause 0.02
        "v082/bellasex03.jpg"
        pause 0.02
        "v082/bellasex04.jpg"
        pause 0.02
        "v082/bellasex05.jpg"
        pause 0.02
        "v082/bellasex06.jpg"
        pause 0.02
        "v082/bellasex07.jpg"
        pause 0.02
        "v082/bellasex08.jpg"
        pause 0.02
        "v082/bellasex09.jpg"
        pause 0.02
        "v082/bellasex10.jpg"
        pause 0.02
        "v082/bellasex11.jpg"
        pause 0.02
        "v082/bellasex12.jpg"
        pause 0.02
        "v082/bellasex13.jpg"
        pause 0.025
        "v082/bellasex14.jpg"
        pause 0.025
        "v082/bellasex15.jpg"
        pause 0.025
        "v082/bellasex16.jpg"
        pause 0.025
        "v082/bellasex17.jpg"
        pause 0.025
        "v082/bellasex18.jpg"
        pause 0.025
        "v082/bellasex19.jpg"
        pause 0.025
        "v082/bellasex20.jpg"
        pause 0.025
        "v082/bellasex21.jpg"
        pause 0.025
        "v082/bellasex22.jpg"
        pause 0.025
        "v082/bellasex23.jpg"
        pause 0.025
        repeat
            
    image devcavefuckslow:
        "v082/devcavefuck00.jpg"
        pause 0.04
        "v082/devcavefuck01.jpg"
        pause 0.04
        "v082/devcavefuck02.jpg"
        pause 0.04
        "v082/devcavefuck03.jpg"
        pause 0.04
        "v082/devcavefuck04.jpg"
        pause 0.04
        "v082/devcavefuck05.jpg"
        pause 0.04
        "v082/devcavefuck06.jpg"
        pause 0.04
        "v082/devcavefuck07.jpg"
        pause 0.04
        "v082/devcavefuck08.jpg"
        pause 0.04
        "v082/devcavefuck09.jpg"
        pause 0.04
        "v082/devcavefuck10.jpg"
        pause 0.04
        "v082/devcavefuck09.jpg"
        pause 0.04
        "v082/devcavefuck08.jpg"
        pause 0.04
        "v082/devcavefuck07.jpg"
        pause 0.045
        "v082/devcavefuck06.jpg"
        pause 0.045
        "v082/devcavefuck05.jpg"
        pause 0.045
        "v082/devcavefuck04.jpg"
        pause 0.045
        "v082/devcavefuck03.jpg"
        pause 0.045
        "v082/devcavefuck02.jpg"
        pause 0.045
        "v082/devcavefuck01.jpg"
        pause 0.045
        repeat
            
    image devcavefuckfast:
        "v082/devcavefuck00.jpg"
        pause 0.025
        "v082/devcavefuck01.jpg"
        pause 0.025
        "v082/devcavefuck02.jpg"
        pause 0.025
        "v082/devcavefuck03.jpg"
        pause 0.025
        "v082/devcavefuck04.jpg"
        pause 0.025
        "v082/devcavefuck05.jpg"
        pause 0.025
        "v082/devcavefuck06.jpg"
        pause 0.025
        "v082/devcavefuck07.jpg"
        pause 0.025
        "v082/devcavefuck08.jpg"
        pause 0.025
        "v082/devcavefuck09.jpg"
        pause 0.025
        "v082/devcavefuck10.jpg"
        pause 0.025
        "v082/devcavefuck09.jpg"
        pause 0.03
        "v082/devcavefuck08.jpg"
        pause 0.03
        "v082/devcavefuck07.jpg"
        pause 0.03
        "v082/devcavefuck06.jpg"
        pause 0.03
        "v082/devcavefuck05.jpg"
        pause 0.03
        "v082/devcavefuck04.jpg"
        pause 0.03
        "v082/devcavefuck03.jpg"
        pause 0.03
        "v082/devcavefuck02.jpg"
        pause 0.03
        "v082/devcavefuck01.jpg"
        pause 0.03
        repeat
            
    image devcaveanimslow:
        "v082/devcaveanim00.jpg"
        pause 0.04
        "v082/devcaveanim01.jpg"
        pause 0.04
        "v082/devcaveanim02.jpg"
        pause 0.04
        "v082/devcaveanim03.jpg"
        pause 0.04
        "v082/devcaveanim04.jpg"
        pause 0.04
        "v082/devcaveanim05.jpg"
        pause 0.04
        "v082/devcaveanim06.jpg"
        pause 0.04
        "v082/devcaveanim07.jpg"
        pause 0.04
        "v082/devcaveanim08.jpg"
        pause 0.04
        "v082/devcaveanim09.jpg"
        pause 0.04
        "v082/devcaveanim10.jpg"
        pause 0.04
        "v082/devcaveanim11.jpg"
        pause 0.04
        "v082/devcaveanim12.jpg"
        pause 0.04
        "v082/devcaveanim11.jpg"
        pause 0.045
        "v082/devcaveanim10.jpg"
        pause 0.045
        "v082/devcaveanim09.jpg"
        pause 0.045
        "v082/devcaveanim08.jpg"
        pause 0.045
        "v082/devcaveanim07.jpg"
        pause 0.045
        "v082/devcaveanim06.jpg"
        pause 0.045
        "v082/devcaveanim05.jpg"
        pause 0.045
        "v082/devcaveanim04.jpg"
        pause 0.045
        "v082/devcaveanim03.jpg"
        pause 0.045
        "v082/devcaveanim02.jpg"
        pause 0.045
        "v082/devcaveanim01.jpg"
        pause 0.045
        repeat
            
    image devcaveanimfast:
        "v082/devcaveanim00.jpg"
        pause 0.025
        "v082/devcaveanim01.jpg"
        pause 0.025
        "v082/devcaveanim02.jpg"
        pause 0.025
        "v082/devcaveanim03.jpg"
        pause 0.025
        "v082/devcaveanim04.jpg"
        pause 0.025
        "v082/devcaveanim05.jpg"
        pause 0.025
        "v082/devcaveanim06.jpg"
        pause 0.025
        "v082/devcaveanim07.jpg"
        pause 0.025
        "v082/devcaveanim08.jpg"
        pause 0.025
        "v082/devcaveanim09.jpg"
        pause 0.025
        "v082/devcaveanim10.jpg"
        pause 0.025
        "v082/devcaveanim11.jpg"
        pause 0.025
        "v082/devcaveanim12.jpg"
        pause 0.025
        "v082/devcaveanim11.jpg"
        pause 0.03
        "v082/devcaveanim10.jpg"
        pause 0.03
        "v082/devcaveanim09.jpg"
        pause 0.03
        "v082/devcaveanim08.jpg"
        pause 0.03
        "v082/devcaveanim07.jpg"
        pause 0.03
        "v082/devcaveanim06.jpg"
        pause 0.03
        "v082/devcaveanim05.jpg"
        pause 0.03
        "v082/devcaveanim04.jpg"
        pause 0.03
        "v082/devcaveanim03.jpg"
        pause 0.03
        "v082/devcaveanim02.jpg"
        pause 0.03
        "v082/devcaveanim01.jpg"
        pause 0.03
        repeat
            
    image devcavemouthslow:
        "v082/devmouthanim00.jpg"
        pause 0.04
        "v082/devmouthanim01.jpg"
        pause 0.04
        "v082/devmouthanim02.jpg"
        pause 0.04
        "v082/devmouthanim03.jpg"
        pause 0.04
        "v082/devmouthanim04.jpg"
        pause 0.04
        "v082/devmouthanim05.jpg"
        pause 0.04
        "v082/devmouthanim06.jpg"
        pause 0.04
        "v082/devmouthanim07.jpg"
        pause 0.04
        "v082/devmouthanim08.jpg"
        pause 0.04
        "v082/devmouthanim09.jpg"
        pause 0.04
        "v082/devmouthanim10.jpg"
        pause 0.04
        "v082/devmouthanim09.jpg"
        pause 0.045
        "v082/devmouthanim08.jpg"
        pause 0.045
        "v082/devmouthanim07.jpg"
        pause 0.045
        "v082/devmouthanim06.jpg"
        pause 0.045
        "v082/devmouthanim05.jpg"
        pause 0.045
        "v082/devmouthanim04.jpg"
        pause 0.045
        "v082/devmouthanim03.jpg"
        pause 0.045
        "v082/devmouthanim02.jpg"
        pause 0.045
        "v082/devmouthanim01.jpg"
        pause 0.045
        repeat
            
    image devcavemouthfast:
        "v082/devmouthanim00.jpg"
        pause 0.025
        "v082/devmouthanim01.jpg"
        pause 0.025
        "v082/devmouthanim02.jpg"
        pause 0.025
        "v082/devmouthanim03.jpg"
        pause 0.025
        "v082/devmouthanim04.jpg"
        pause 0.025
        "v082/devmouthanim05.jpg"
        pause 0.025
        "v082/devmouthanim06.jpg"
        pause 0.025
        "v082/devmouthanim07.jpg"
        pause 0.025
        "v082/devmouthanim08.jpg"
        pause 0.025
        "v082/devmouthanim09.jpg"
        pause 0.025
        "v082/devmouthanim10.jpg"
        pause 0.025
        "v082/devmouthanim09.jpg"
        pause 0.03
        "v082/devmouthanim08.jpg"
        pause 0.03
        "v082/devmouthanim07.jpg"
        pause 0.03
        "v082/devmouthanim06.jpg"
        pause 0.03
        "v082/devmouthanim05.jpg"
        pause 0.03
        "v082/devmouthanim04.jpg"
        pause 0.03
        "v082/devmouthanim03.jpg"
        pause 0.03
        "v082/devmouthanim02.jpg"
        pause 0.03
        "v082/devmouthanim01.jpg"
        pause 0.03
        repeat
            

    image devcavesophiafuckslow:
        "v082/devsophiafuck00.jpg"
        pause 0.04
        "v082/devsophiafuck01.jpg"
        pause 0.04
        "v082/devsophiafuck02.jpg"
        pause 0.04
        "v082/devsophiafuck03.jpg"
        pause 0.04
        "v082/devsophiafuck04.jpg"
        pause 0.04
        "v082/devsophiafuck05.jpg"
        pause 0.04
        "v082/devsophiafuck06.jpg"
        pause 0.04
        "v082/devsophiafuck07.jpg"
        pause 0.04
        "v082/devsophiafuck08.jpg"
        pause 0.04
        "v082/devsophiafuck09.jpg"
        pause 0.04
        "v082/devsophiafuck10.jpg"
        pause 0.04
        "v082/devsophiafuck11.jpg"
        pause 0.04
        "v082/devsophiafuck12.jpg"
        pause 0.04
        "v082/devsophiafuck11.jpg"
        pause 0.045
        "v082/devsophiafuck10.jpg"
        pause 0.045
        "v082/devsophiafuck09.jpg"
        pause 0.045
        "v082/devsophiafuck08.jpg"
        pause 0.045
        "v082/devsophiafuck07.jpg"
        pause 0.045
        "v082/devsophiafuck06.jpg"
        pause 0.045
        "v082/devsophiafuck05.jpg"
        pause 0.045
        "v082/devsophiafuck04.jpg"
        pause 0.045
        "v082/devsophiafuck03.jpg"
        pause 0.045
        "v082/devsophiafuck02.jpg"
        pause 0.045
        "v082/devsophiafuck01.jpg"
        pause 0.045
        repeat
            
    image devcavesophiafuckfast:
        "v082/devsophiafuck00.jpg"
        pause 0.025
        "v082/devsophiafuck01.jpg"
        pause 0.025
        "v082/devsophiafuck02.jpg"
        pause 0.025
        "v082/devsophiafuck03.jpg"
        pause 0.025
        "v082/devsophiafuck04.jpg"
        pause 0.025
        "v082/devsophiafuck05.jpg"
        pause 0.025
        "v082/devsophiafuck06.jpg"
        pause 0.025
        "v082/devsophiafuck07.jpg"
        pause 0.025
        "v082/devsophiafuck08.jpg"
        pause 0.025
        "v082/devsophiafuck09.jpg"
        pause 0.025
        "v082/devsophiafuck10.jpg"
        pause 0.025
        "v082/devsophiafuck11.jpg"
        pause 0.025
        "v082/devsophiafuck12.jpg"
        pause 0.025
        "v082/devsophiafuck11.jpg"
        pause 0.03
        "v082/devsophiafuck10.jpg"
        pause 0.03
        "v082/devsophiafuck09.jpg"
        pause 0.03
        "v082/devsophiafuck08.jpg"
        pause 0.03
        "v082/devsophiafuck07.jpg"
        pause 0.03
        "v082/devsophiafuck06.jpg"
        pause 0.03
        "v082/devsophiafuck05.jpg"
        pause 0.03
        "v082/devsophiafuck04.jpg"
        pause 0.03
        "v082/devsophiafuck03.jpg"
        pause 0.03
        "v082/devsophiafuck02.jpg"
        pause 0.03
        "v082/devsophiafuck01.jpg"
        pause 0.03
        repeat
            
    image bellarubslow:
        "v082/bellarub00.jpg"
        pause 0.04
        "v082/bellarub01.jpg"
        pause 0.04
        "v082/bellarub02.jpg"
        pause 0.04
        "v082/bellarub03.jpg"
        pause 0.04
        "v082/bellarub04.jpg"
        pause 0.04
        "v082/bellarub05.jpg"
        pause 0.04
        "v082/bellarub06.jpg"
        pause 0.04
        "v082/bellarub07.jpg"
        pause 0.04
        "v082/bellarub08.jpg"
        pause 0.04
        "v082/bellarub09.jpg"
        pause 0.04
        "v082/bellarub10.jpg"
        pause 0.04
        "v082/bellarub11.jpg"
        pause 0.045
        "v082/bellarub10.jpg"
        pause 0.045
        "v082/bellarub09.jpg"
        pause 0.045
        "v082/bellarub08.jpg"
        pause 0.045
        "v082/bellarub07.jpg"
        pause 0.045
        "v082/bellarub06.jpg"
        pause 0.045
        "v082/bellarub05.jpg"
        pause 0.045
        "v082/bellarub04.jpg"
        pause 0.045
        "v082/bellarub03.jpg"
        pause 0.045
        "v082/bellarub02.jpg"
        pause 0.045
        "v082/bellarub01.jpg"
        pause 0.045
        repeat
            
    image bellarubfast:
        "v082/bellarub00.jpg"
        pause 0.025
        "v082/bellarub01.jpg"
        pause 0.025
        "v082/bellarub02.jpg"
        pause 0.025
        "v082/bellarub03.jpg"
        pause 0.025
        "v082/bellarub04.jpg"
        pause 0.025
        "v082/bellarub05.jpg"
        pause 0.025
        "v082/bellarub06.jpg"
        pause 0.025
        "v082/bellarub07.jpg"
        pause 0.025
        "v082/bellarub08.jpg"
        pause 0.025
        "v082/bellarub09.jpg"
        pause 0.025
        "v082/bellarub10.jpg"
        pause 0.025
        "v082/bellarub11.jpg"
        pause 0.03
        "v082/bellarub10.jpg"
        pause 0.03
        "v082/bellarub09.jpg"
        pause 0.03
        "v082/bellarub08.jpg"
        pause 0.03
        "v082/bellarub07.jpg"
        pause 0.03
        "v082/bellarub06.jpg"
        pause 0.03
        "v082/bellarub05.jpg"
        pause 0.03
        "v082/bellarub04.jpg"
        pause 0.03
        "v082/bellarub03.jpg"
        pause 0.03
        "v082/bellarub02.jpg"
        pause 0.03
        "v082/bellarub01.jpg"
        pause 0.03
        repeat
            
    image bellaanalslow:
        "v082/bellaanal00.jpg"
        pause 0.035
        "v082/bellaanal01.jpg"
        pause 0.035
        "v082/bellaanal02.jpg"
        pause 0.035
        "v082/bellaanal03.jpg"
        pause 0.035
        "v082/bellaanal04.jpg"
        pause 0.035
        "v082/bellaanal05.jpg"
        pause 0.035
        "v082/bellaanal06.jpg"
        pause 0.035
        "v082/bellaanal07.jpg"
        pause 0.035
        "v082/bellaanal08.jpg"
        pause 0.035
        "v082/bellaanal09.jpg"
        pause 0.035
        "v082/bellaanal10.jpg"
        pause 0.035
        "v082/bellaanal11.jpg"
        pause 0.035
        "v082/bellaanal12.jpg"
        pause 0.035
        "v082/bellaanal13.jpg"
        pause 0.035
        "v082/bellaanal14.jpg"
        pause 0.035
        "v082/bellaanal15.jpg"
        pause 0.035
        "v082/bellaanal16.jpg"
        pause 0.035
        "v082/bellaanal17.jpg"
        pause 0.035
        "v082/bellaanal18.jpg"
        pause 0.035
        "v082/bellaanal19.jpg"
        pause 0.035
        "v082/bellaanal20.jpg"
        pause 0.035
        "v082/bellaanal21.jpg"
        pause 0.035
        "v082/bellaanal22.jpg"
        pause 0.035
        "v082/bellaanal23.jpg"
        pause 0.035
        repeat
            
    image bellaanalfast:
        "v082/bellaanal00.jpg"
        pause 0.025
        "v082/bellaanal01.jpg"
        pause 0.025
        "v082/bellaanal02.jpg"
        pause 0.025
        "v082/bellaanal03.jpg"
        pause 0.025
        "v082/bellaanal04.jpg"
        pause 0.025
        "v082/bellaanal05.jpg"
        pause 0.025
        "v082/bellaanal06.jpg"
        pause 0.025
        "v082/bellaanal07.jpg"
        pause 0.025
        "v082/bellaanal08.jpg"
        pause 0.025
        "v082/bellaanal09.jpg"
        pause 0.025
        "v082/bellaanal10.jpg"
        pause 0.025
        "v082/bellaanal11.jpg"
        pause 0.025
        "v082/bellaanal12.jpg"
        pause 0.025
        "v082/bellaanal13.jpg"
        pause 0.025
        "v082/bellaanal14.jpg"
        pause 0.025
        "v082/bellaanal15.jpg"
        pause 0.025
        "v082/bellaanal16.jpg"
        pause 0.025
        "v082/bellaanal17.jpg"
        pause 0.025
        "v082/bellaanal18.jpg"
        pause 0.025
        "v082/bellaanal19.jpg"
        pause 0.025
        "v082/bellaanal20.jpg"
        pause 0.025
        "v082/bellaanal21.jpg"
        pause 0.025
        "v082/bellaanal22.jpg"
        pause 0.025
        "v082/bellaanal23.jpg"
        pause 0.025
        repeat            
            
    image bellaanalsideslow:
        "v082/bellaanalside00.jpg"
        pause 0.035
        "v082/bellaanalside01.jpg"
        pause 0.035
        "v082/bellaanalside02.jpg"
        pause 0.035
        "v082/bellaanalside03.jpg"
        pause 0.035
        "v082/bellaanalside04.jpg"
        pause 0.035
        "v082/bellaanalside05.jpg"
        pause 0.035
        "v082/bellaanalside06.jpg"
        pause 0.035
        "v082/bellaanalside07.jpg"
        pause 0.035
        "v082/bellaanalside08.jpg"
        pause 0.035
        "v082/bellaanalside09.jpg"
        pause 0.035
        "v082/bellaanalside10.jpg"
        pause 0.035
        "v082/bellaanalside11.jpg"
        pause 0.035
        "v082/bellaanalside12.jpg"
        pause 0.035
        "v082/bellaanalside13.jpg"
        pause 0.035
        "v082/bellaanalside14.jpg"
        pause 0.035
        "v082/bellaanalside15.jpg"
        pause 0.035
        "v082/bellaanalside16.jpg"
        pause 0.035
        "v082/bellaanalside17.jpg"
        pause 0.035
        "v082/bellaanalside18.jpg"
        pause 0.035
        "v082/bellaanalside19.jpg"
        pause 0.035
        "v082/bellaanalside20.jpg"
        pause 0.035
        "v082/bellaanalside21.jpg"
        pause 0.035
        "v082/bellaanalside22.jpg"
        pause 0.035
        "v082/bellaanalside23.jpg"
        pause 0.035
        repeat
            
    image bellaanalsidefast:
        "v082/bellaanalside00.jpg"
        pause 0.025
        "v082/bellaanalside01.jpg"
        pause 0.025
        "v082/bellaanalside02.jpg"
        pause 0.025
        "v082/bellaanalside03.jpg"
        pause 0.025
        "v082/bellaanalside04.jpg"
        pause 0.025
        "v082/bellaanalside05.jpg"
        pause 0.025
        "v082/bellaanalside06.jpg"
        pause 0.025
        "v082/bellaanalside07.jpg"
        pause 0.025
        "v082/bellaanalside08.jpg"
        pause 0.025
        "v082/bellaanalside09.jpg"
        pause 0.025
        "v082/bellaanalside10.jpg"
        pause 0.025
        "v082/bellaanalside11.jpg"
        pause 0.025
        "v082/bellaanalside12.jpg"
        pause 0.025
        "v082/bellaanalside13.jpg"
        pause 0.025
        "v082/bellaanalside14.jpg"
        pause 0.025
        "v082/bellaanalside15.jpg"
        pause 0.025
        "v082/bellaanalside16.jpg"
        pause 0.025
        "v082/bellaanalside17.jpg"
        pause 0.025
        "v082/bellaanalside18.jpg"
        pause 0.025
        "v082/bellaanalside19.jpg"
        pause 0.025
        "v082/bellaanalside20.jpg"
        pause 0.025
        "v082/bellaanalside21.jpg"
        pause 0.025
        "v082/bellaanalside22.jpg"
        pause 0.025
        "v082/bellaanalside23.jpg"
        pause 0.025
        repeat            
            
            
    image bellafootslow:
        "v082/bellafoot00.jpg"
        pause 0.04
        "v082/bellafoot01.jpg"
        pause 0.04
        "v082/bellafoot02.jpg"
        pause 0.04
        "v082/bellafoot03.jpg"
        pause 0.04
        "v082/bellafoot04.jpg"
        pause 0.04
        "v082/bellafoot05.jpg"
        pause 0.04
        "v082/bellafoot06.jpg"
        pause 0.04
        "v082/bellafoot07.jpg"
        pause 0.04
        "v082/bellafoot08.jpg"
        pause 0.04
        "v082/bellafoot09.jpg"
        pause 0.04
        "v082/bellafoot10.jpg"
        pause 0.05
        "v082/bellafoot09.jpg"
        pause 0.045
        "v082/bellafoot08.jpg"
        pause 0.045
        "v082/bellafoot07.jpg"
        pause 0.045
        "v082/bellafoot06.jpg"
        pause 0.045
        "v082/bellafoot05.jpg"
        pause 0.045
        "v082/bellafoot04.jpg"
        pause 0.045
        "v082/bellafoot03.jpg"
        pause 0.045
        "v082/bellafoot02.jpg"
        pause 0.045
        "v082/bellafoot01.jpg"
        pause 0.045
        repeat
            
    image bellafootfast:
        "v082/bellafoot00.jpg"
        pause 0.025
        "v082/bellafoot01.jpg"
        pause 0.025
        "v082/bellafoot02.jpg"
        pause 0.025
        "v082/bellafoot03.jpg"
        pause 0.025
        "v082/bellafoot04.jpg"
        pause 0.025
        "v082/bellafoot05.jpg"
        pause 0.025
        "v082/bellafoot06.jpg"
        pause 0.025
        "v082/bellafoot07.jpg"
        pause 0.025
        "v082/bellafoot08.jpg"
        pause 0.025
        "v082/bellafoot09.jpg"
        pause 0.025
        "v082/bellafoot10.jpg"
        pause 0.04
        "v082/bellafoot09.jpg"
        pause 0.03
        "v082/bellafoot08.jpg"
        pause 0.03
        "v082/bellafoot07.jpg"
        pause 0.03
        "v082/bellafoot06.jpg"
        pause 0.03
        "v082/bellafoot05.jpg"
        pause 0.03
        "v082/bellafoot04.jpg"
        pause 0.03
        "v082/bellafoot03.jpg"
        pause 0.03
        "v082/bellafoot02.jpg"
        pause 0.03
        "v082/bellafoot01.jpg"
        pause 0.03
        repeat
                  
    image bellablowslow:
        "v082/bellablow00.jpg"
        pause 0.04
        "v082/bellablow01.jpg"
        pause 0.04
        "v082/bellablow02.jpg"
        pause 0.04
        "v082/bellablow03.jpg"
        pause 0.04
        "v082/bellablow04.jpg"
        pause 0.04
        "v082/bellablow05.jpg"
        pause 0.04
        "v082/bellablow06.jpg"
        pause 0.04
        "v082/bellablow07.jpg"
        pause 0.04
        "v082/bellablow08.jpg"
        pause 0.04
        "v082/bellablow09.jpg"
        pause 0.04
        "v082/bellablow10.jpg"
        pause 0.05
        "v082/bellablow09.jpg"
        pause 0.045
        "v082/bellablow08.jpg"
        pause 0.045
        "v082/bellablow07.jpg"
        pause 0.045
        "v082/bellablow06.jpg"
        pause 0.045
        "v082/bellablow05.jpg"
        pause 0.045
        "v082/bellablow04.jpg"
        pause 0.045
        "v082/bellablow03.jpg"
        pause 0.045
        "v082/bellablow02.jpg"
        pause 0.045
        "v082/bellablow01.jpg"
        pause 0.045
        repeat
            
    image bellablowfast:
        "v082/bellablow00.jpg"
        pause 0.025
        "v082/bellablow01.jpg"
        pause 0.025
        "v082/bellablow02.jpg"
        pause 0.025
        "v082/bellablow03.jpg"
        pause 0.025
        "v082/bellablow04.jpg"
        pause 0.025
        "v082/bellablow05.jpg"
        pause 0.025
        "v082/bellablow06.jpg"
        pause 0.025
        "v082/bellablow07.jpg"
        pause 0.025
        "v082/bellablow08.jpg"
        pause 0.025
        "v082/bellablow09.jpg"
        pause 0.025
        "v082/bellablow10.jpg"
        pause 0.04
        "v082/bellablow09.jpg"
        pause 0.03
        "v082/bellablow08.jpg"
        pause 0.03
        "v082/bellablow07.jpg"
        pause 0.03
        "v082/bellablow06.jpg"
        pause 0.03
        "v082/bellablow05.jpg"
        pause 0.03
        "v082/bellablow04.jpg"
        pause 0.03
        "v082/bellablow03.jpg"
        pause 0.03
        "v082/bellablow02.jpg"
        pause 0.03
        "v082/bellablow01.jpg"
        pause 0.03
        repeat
            
    image kimfbianim:
        "v082/kimfbianim00.png"
        pause 0.05
        "v082/kimfbianim01.png"
        pause 0.03
        "v082/kimfbianim02.png"
        pause 0.03
        "v082/kimfbianim03.png"
        pause 0.03
        "v082/kimfbianim04.png"
        pause 0.03
        "v082/kimfbianim05.png"
        pause 0.03
        "v082/kimfbianim06.png"
        pause 0.03
        "v082/kimfbianim07.png"
        pause 0.03
        "v082/kimfbianim08.png"
        pause 0.03
        "v082/kimfbianim09.png"
        pause 0.03
        "v082/kimfbianim10.png"
        pause 0.05
        "v082/kimfbianim09.png"
        pause 0.035
        "v082/kimfbianim08.png"
        pause 0.035
        "v082/kimfbianim07.png"
        pause 0.035
        "v082/kimfbianim06.png"
        pause 0.035
        "v082/kimfbianim05.png"
        pause 0.035
        "v082/kimfbianim04.png"
        pause 0.035
        "v082/kimfbianim03.png"
        pause 0.035
        "v082/kimfbianim02.png"
        pause 0.035
        "v082/kimfbianim01.png"
        pause 0.035
        repeat
            
    image titianafuckslow:
        "v082/titianafuck00.png"
        pause 0.03
        "v082/titianafuck01.png"
        pause 0.03
        "v082/titianafuck02.png"
        pause 0.03
        "v082/titianafuck03.png"
        pause 0.03
        "v082/titianafuck04.png"
        pause 0.03
        "v082/titianafuck05.png"
        pause 0.03
        "v082/titianafuck06.png"
        pause 0.03
        "v082/titianafuck07.png"
        pause 0.03
        "v082/titianafuck08.png"
        pause 0.03
        "v082/titianafuck09.png"
        pause 0.03
        "v082/titianafuck10.png"
        pause 0.03
        "v082/titianafuck11.png"
        pause 0.03
        "v082/titianafuck12.png"
        pause 0.03
        "v082/titianafuck13.png"
        pause 0.035
        "v082/titianafuck14.png"
        pause 0.035
        "v082/titianafuck15.png"
        pause 0.035
        "v082/titianafuck16.png"
        pause 0.035
        "v082/titianafuck17.png"
        pause 0.035
        "v082/titianafuck18.png"
        pause 0.035
        "v082/titianafuck19.png"
        pause 0.035
        "v082/titianafuck20.png"
        pause 0.035
        "v082/titianafuck21.png"
        pause 0.035
        "v082/titianafuck22.png"
        pause 0.035
        "v082/titianafuck23.png"
        pause 0.035
        repeat
            
    image titianafuckfast:
        "v082/titianafuck00.png"
        pause 0.02
        "v082/titianafuck01.png"
        pause 0.02
        "v082/titianafuck02.png"
        pause 0.02
        "v082/titianafuck03.png"
        pause 0.02
        "v082/titianafuck04.png"
        pause 0.02
        "v082/titianafuck05.png"
        pause 0.02
        "v082/titianafuck06.png"
        pause 0.02
        "v082/titianafuck07.png"
        pause 0.02
        "v082/titianafuck08.png"
        pause 0.02
        "v082/titianafuck09.png"
        pause 0.02
        "v082/titianafuck10.png"
        pause 0.02
        "v082/titianafuck11.png"
        pause 0.02
        "v082/titianafuck12.png"
        pause 0.02
        "v082/titianafuck13.png"
        pause 0.025
        "v082/titianafuck14.png"
        pause 0.025
        "v082/titianafuck15.png"
        pause 0.025
        "v082/titianafuck16.png"
        pause 0.025
        "v082/titianafuck17.png"
        pause 0.025
        "v082/titianafuck18.png"
        pause 0.025
        "v082/titianafuck19.png"
        pause 0.025
        "v082/titianafuck20.png"
        pause 0.025
        "v082/titianafuck21.png"
        pause 0.025
        "v082/titianafuck22.png"
        pause 0.025
        "v082/titianafuck23.png"
        pause 0.025
        repeat
            
    image titianatitsslow:
        "v082/titianatits00.jpg"
        pause 0.04
        "v082/titianatits01.jpg"
        pause 0.04
        "v082/titianatits02.jpg"
        pause 0.04
        "v082/titianatits03.jpg"
        pause 0.04
        "v082/titianatits04.jpg"
        pause 0.04
        "v082/titianatits05.jpg"
        pause 0.04
        "v082/titianatits06.jpg"
        pause 0.04
        "v082/titianatits07.jpg"
        pause 0.04
        "v082/titianatits08.jpg"
        pause 0.04
        "v082/titianatits09.jpg"
        pause 0.04
        "v082/titianatits10.jpg"
        pause 0.04
        "v082/titianatits11.jpg"
        pause 0.04
        "v082/titianatits12.jpg"
        pause 0.05
        "v082/titianatits11.jpg"
        pause 0.03
        "v082/titianatits10.jpg"
        pause 0.03
        "v082/titianatits09.jpg"
        pause 0.03
        "v082/titianatits08.jpg"
        pause 0.03
        "v082/titianatits07.jpg"
        pause 0.03
        "v082/titianatits06.jpg"
        pause 0.03
        "v082/titianatits05.jpg"
        pause 0.03
        "v082/titianatits04.jpg"
        pause 0.03
        "v082/titianatits03.jpg"
        pause 0.03
        "v082/titianatits02.jpg"
        pause 0.03
        "v082/titianatits01.jpg"
        pause 0.03
        repeat
            
    image titianatitsfast:
        "v082/titianatits00.jpg"
        pause 0.03
        "v082/titianatits01.jpg"
        pause 0.03
        "v082/titianatits02.jpg"
        pause 0.03
        "v082/titianatits03.jpg"
        pause 0.03
        "v082/titianatits04.jpg"
        pause 0.03
        "v082/titianatits05.jpg"
        pause 0.03
        "v082/titianatits06.jpg"
        pause 0.03
        "v082/titianatits07.jpg"
        pause 0.03
        "v082/titianatits08.jpg"
        pause 0.03
        "v082/titianatits09.jpg"
        pause 0.03
        "v082/titianatits10.jpg"
        pause 0.03
        "v082/titianatits11.jpg"
        pause 0.03
        "v082/titianatits12.jpg"
        pause 0.04
        "v082/titianatits11.jpg"
        pause 0.02
        "v082/titianatits10.jpg"
        pause 0.02
        "v082/titianatits09.jpg"
        pause 0.02
        "v082/titianatits08.jpg"
        pause 0.02
        "v082/titianatits07.jpg"
        pause 0.02
        "v082/titianatits06.jpg"
        pause 0.02
        "v082/titianatits05.jpg"
        pause 0.02
        "v082/titianatits04.jpg"
        pause 0.02
        "v082/titianatits03.jpg"
        pause 0.02
        "v082/titianatits02.jpg"
        pause 0.02
        "v082/titianatits01.jpg"
        pause 0.02
        repeat
            
    image debrahandslow:
        "v09/debramcsofawank00.jpg"
        pause 0.06
        "v09/debramcsofawank01.jpg"
        pause 0.04
        "v09/debramcsofawank02.jpg"
        pause 0.04
        "v09/debramcsofawank03.jpg"
        pause 0.04
        "v09/debramcsofawank04.jpg"
        pause 0.04
        "v09/debramcsofawank05.jpg"
        pause 0.04
        "v09/debramcsofawank06.jpg"
        pause 0.04
        "v09/debramcsofawank07.jpg"
        pause 0.04
        "v09/debramcsofawank08.jpg"
        pause 0.04
        "v09/debramcsofawank09.jpg"
        pause 0.04
        "v09/debramcsofawank10.jpg"
        pause 0.06
        "v09/debramcsofawank09.jpg"
        pause 0.045
        "v09/debramcsofawank08.jpg"
        pause 0.045
        "v09/debramcsofawank07.jpg"
        pause 0.045
        "v09/debramcsofawank06.jpg"
        pause 0.045
        "v09/debramcsofawank05.jpg"
        pause 0.045
        "v09/debramcsofawank04.jpg"
        pause 0.045
        "v09/debramcsofawank03.jpg"
        pause 0.045
        "v09/debramcsofawank02.jpg"
        pause 0.045
        "v09/debramcsofawank01.jpg"
        pause 0.045
        repeat
            
    image debrahandfast:
        "v09/debramcsofawank00.jpg"
        pause 0.05
        "v09/debramcsofawank01.jpg"
        pause 0.03
        "v09/debramcsofawank02.jpg"
        pause 0.03
        "v09/debramcsofawank03.jpg"
        pause 0.03
        "v09/debramcsofawank04.jpg"
        pause 0.03
        "v09/debramcsofawank05.jpg"
        pause 0.03
        "v09/debramcsofawank06.jpg"
        pause 0.03
        "v09/debramcsofawank07.jpg"
        pause 0.03
        "v09/debramcsofawank08.jpg"
        pause 0.03
        "v09/debramcsofawank09.jpg"
        pause 0.03
        "v09/debramcsofawank10.jpg"
        pause 0.05
        "v09/debramcsofawank09.jpg"
        pause 0.035
        "v09/debramcsofawank08.jpg"
        pause 0.035
        "v09/debramcsofawank07.jpg"
        pause 0.035
        "v09/debramcsofawank06.jpg"
        pause 0.035
        "v09/debramcsofawank05.jpg"
        pause 0.035
        "v09/debramcsofawank04.jpg"
        pause 0.035
        "v09/debramcsofawank03.jpg"
        pause 0.035
        "v09/debramcsofawank02.jpg"
        pause 0.035
        "v09/debramcsofawank01.jpg"
        pause 0.035
        repeat
            
    image debrarideslow:
        "v09/debraride00.jpg"
        pause 0.06
        "v09/debraride01.jpg"
        pause 0.04
        "v09/debraride02.jpg"
        pause 0.04
        "v09/debraride03.jpg"
        pause 0.04
        "v09/debraride04.jpg"
        pause 0.04
        "v09/debraride05.jpg"
        pause 0.04
        "v09/debraride06.jpg"
        pause 0.04
        "v09/debraride07.jpg"
        pause 0.04
        "v09/debraride08.jpg"
        pause 0.04
        "v09/debraride09.jpg"
        pause 0.04
        "v09/debraride10.jpg"
        pause 0.06
        "v09/debraride09.jpg"
        pause 0.045
        "v09/debraride08.jpg"
        pause 0.045
        "v09/debraride07.jpg"
        pause 0.045
        "v09/debraride06.jpg"
        pause 0.045
        "v09/debraride05.jpg"
        pause 0.045
        "v09/debraride04.jpg"
        pause 0.045
        "v09/debraride03.jpg"
        pause 0.045
        "v09/debraride02.jpg"
        pause 0.045
        "v09/debraride01.jpg"
        pause 0.045
        repeat
            
    image debraridefast:
        "v09/debraride00.jpg"
        pause 0.05
        "v09/debraride01.jpg"
        pause 0.03
        "v09/debraride02.jpg"
        pause 0.03
        "v09/debraride03.jpg"
        pause 0.03
        "v09/debraride04.jpg"
        pause 0.03
        "v09/debraride05.jpg"
        pause 0.03
        "v09/debraride06.jpg"
        pause 0.03
        "v09/debraride07.jpg"
        pause 0.03
        "v09/debraride08.jpg"
        pause 0.03
        "v09/debraride09.jpg"
        pause 0.03
        "v09/debraride10.jpg"
        pause 0.05
        "v09/debraride09.jpg"
        pause 0.035
        "v09/debraride08.jpg"
        pause 0.035
        "v09/debraride07.jpg"
        pause 0.035
        "v09/debraride06.jpg"
        pause 0.035
        "v09/debraride05.jpg"
        pause 0.035
        "v09/debraride04.jpg"
        pause 0.035
        "v09/debraride03.jpg"
        pause 0.035
        "v09/debraride02.jpg"
        pause 0.035
        "v09/debraride01.jpg"
        pause 0.035
        repeat
            
    image debradoggyslow:
        "v09/debradoggy01.jpg"
        pause 0.06
        "v09/debradoggy02.jpg"
        pause 0.04
        "v09/debradoggy03.jpg"
        pause 0.04
        "v09/debradoggy04.jpg"
        pause 0.04
        "v09/debradoggy05.jpg"
        pause 0.04
        "v09/debradoggy06.jpg"
        pause 0.04
        "v09/debradoggy07.jpg"
        pause 0.04
        "v09/debradoggy08.jpg"
        pause 0.04
        "v09/debradoggy09.jpg"
        pause 0.04
        "v09/debradoggy10.jpg"
        pause 0.04
        "v09/debradoggy11.jpg"
        pause 0.04
        "v09/debradoggy12.jpg"
        pause 0.06
        "v09/debradoggy11.jpg"
        pause 0.045
        "v09/debradoggy10.jpg"
        pause 0.045
        "v09/debradoggy09.jpg"
        pause 0.045
        "v09/debradoggy08.jpg"
        pause 0.045
        "v09/debradoggy07.jpg"
        pause 0.045
        "v09/debradoggy06.jpg"
        pause 0.045
        "v09/debradoggy05.jpg"
        pause 0.045
        "v09/debradoggy04.jpg"
        pause 0.045
        "v09/debradoggy03.jpg"
        pause 0.045
        "v09/debradoggy02.jpg"
        pause 0.045
        repeat
            
    image debradoggyfast:
        "v09/debradoggy01.jpg"
        pause 0.05
        "v09/debradoggy02.jpg"
        pause 0.03
        "v09/debradoggy03.jpg"
        pause 0.03
        "v09/debradoggy04.jpg"
        pause 0.03
        "v09/debradoggy05.jpg"
        pause 0.03
        "v09/debradoggy06.jpg"
        pause 0.03
        "v09/debradoggy07.jpg"
        pause 0.03
        "v09/debradoggy08.jpg"
        pause 0.03
        "v09/debradoggy09.jpg"
        pause 0.03
        "v09/debradoggy10.jpg"
        pause 0.03
        "v09/debradoggy11.jpg"
        pause 0.03
        "v09/debradoggy12.jpg"
        pause 0.05
        "v09/debradoggy11.jpg"
        pause 0.035
        "v09/debradoggy10.jpg"
        pause 0.035
        "v09/debradoggy09.jpg"
        pause 0.035
        "v09/debradoggy08.jpg"
        pause 0.035
        "v09/debradoggy07.jpg"
        pause 0.035
        "v09/debradoggy06.jpg"
        pause 0.035
        "v09/debradoggy05.jpg"
        pause 0.035
        "v09/debradoggy04.jpg"
        pause 0.035
        "v09/debradoggy03.jpg"
        pause 0.035
        "v09/debradoggy02.jpg"
        pause 0.035
        repeat
            
    image debrasuckslow:
        "v09/debrasuck00.jpg"
        pause 0.06
        "v09/debrasuck01.jpg"
        pause 0.04
        "v09/debrasuck02.jpg"
        pause 0.04
        "v09/debrasuck03.jpg"
        pause 0.04
        "v09/debrasuck04.jpg"
        pause 0.04
        "v09/debrasuck05.jpg"
        pause 0.04
        "v09/debrasuck06.jpg"
        pause 0.04
        "v09/debrasuck07.jpg"
        pause 0.04
        "v09/debrasuck08.jpg"
        pause 0.04
        "v09/debrasuck09.jpg"
        pause 0.04
        "v09/debrasuck10.jpg"
        pause 0.04
        "v09/debrasuck11.jpg"
        pause 0.04
        "v09/debrasuck12.jpg"
        pause 0.06
        "v09/debrasuck11.jpg"
        pause 0.045
        "v09/debrasuck10.jpg"
        pause 0.045
        "v09/debrasuck09.jpg"
        pause 0.045
        "v09/debrasuck08.jpg"
        pause 0.045
        "v09/debrasuck07.jpg"
        pause 0.045
        "v09/debrasuck06.jpg"
        pause 0.045
        "v09/debrasuck05.jpg"
        pause 0.045
        "v09/debrasuck04.jpg"
        pause 0.045
        "v09/debrasuck03.jpg"
        pause 0.045
        "v09/debrasuck02.jpg"
        pause 0.045
        "v09/debrasuck01.jpg"
        pause 0.045
        repeat
            
    image debrasuckfast:
        "v09/debrasuck00.jpg"
        pause 0.05
        "v09/debrasuck01.jpg"
        pause 0.03
        "v09/debrasuck02.jpg"
        pause 0.03
        "v09/debrasuck03.jpg"
        pause 0.03
        "v09/debrasuck04.jpg"
        pause 0.03
        "v09/debrasuck05.jpg"
        pause 0.03
        "v09/debrasuck06.jpg"
        pause 0.03
        "v09/debrasuck07.jpg"
        pause 0.03
        "v09/debrasuck08.jpg"
        pause 0.03
        "v09/debrasuck09.jpg"
        pause 0.03
        "v09/debrasuck10.jpg"
        pause 0.03
        "v09/debrasuck11.jpg"
        pause 0.03
        "v09/debrasuck12.jpg"
        pause 0.05
        "v09/debrasuck11.jpg"
        pause 0.035
        "v09/debrasuck10.jpg"
        pause 0.035
        "v09/debrasuck09.jpg"
        pause 0.035
        "v09/debrasuck08.jpg"
        pause 0.035
        "v09/debrasuck07.jpg"
        pause 0.035
        "v09/debrasuck06.jpg"
        pause 0.035
        "v09/debrasuck05.jpg"
        pause 0.035
        "v09/debrasuck04.jpg"
        pause 0.035
        "v09/debrasuck03.jpg"
        pause 0.035
        "v09/debrasuck02.jpg"
        pause 0.035
        "v09/debrasuck01.jpg"
        pause 0.035
        repeat
            
    image debrasuck02slow:
        "v09/debrasuck00.jpg"
        pause 0.06
        "v09/debrasuck01.jpg"
        pause 0.04
        "v09/debrasuck02.jpg"
        pause 0.04
        "v09/debrasuck03.jpg"
        pause 0.04
        "v09/debrasuck04.jpg"
        pause 0.04
        "v09/debrasuck05.jpg"
        pause 0.04
        "v09/debrasuck06.jpg"
        pause 0.04
        "v09/debrasuck07.jpg"
        pause 0.04
        "v09/debrasuck08.jpg"
        pause 0.04
        "v09/debrasuck09.jpg"
        pause 0.04
        "v09/debrasuck10.jpg"
        pause 0.04
        "v09/debrasuck11.jpg"
        pause 0.04
        "v09/debrasuck12.jpg"
        pause 0.06
        "v09/debrasuck13.jpg"
        pause 0.04
        "v09/debrasuck14.jpg"
        pause 0.04
        "v09/debrasuck15.jpg"
        pause 0.04
        "v09/debrasuck16.jpg"
        pause 0.04
        "v09/debrasuck17.jpg"
        pause 0.04
        "v09/debrasuck18.jpg"
        pause 0.06
        "v09/debrasuck17.jpg"
        pause 0.045
        "v09/debrasuck16.jpg"
        pause 0.045
        "v09/debrasuck15.jpg"
        pause 0.045
        "v09/debrasuck14.jpg"
        pause 0.045
        "v09/debrasuck13.jpg"
        pause 0.045
        "v09/debrasuck11.jpg"
        pause 0.045
        "v09/debrasuck10.jpg"
        pause 0.045
        "v09/debrasuck09.jpg"
        pause 0.045
        "v09/debrasuck08.jpg"
        pause 0.045
        "v09/debrasuck07.jpg"
        pause 0.045
        "v09/debrasuck06.jpg"
        pause 0.045
        "v09/debrasuck05.jpg"
        pause 0.045
        "v09/debrasuck04.jpg"
        pause 0.045
        "v09/debrasuck03.jpg"
        pause 0.045
        "v09/debrasuck02.jpg"
        pause 0.045
        "v09/debrasuck01.jpg"
        pause 0.045
        repeat
            
    image debrasuck02fast:
        "v09/debrasuck00.jpg"
        pause 0.06
        "v09/debrasuck01.jpg"
        pause 0.03
        "v09/debrasuck02.jpg"
        pause 0.03
        "v09/debrasuck03.jpg"
        pause 0.03
        "v09/debrasuck04.jpg"
        pause 0.03
        "v09/debrasuck05.jpg"
        pause 0.03
        "v09/debrasuck06.jpg"
        pause 0.03
        "v09/debrasuck07.jpg"
        pause 0.03
        "v09/debrasuck08.jpg"
        pause 0.03
        "v09/debrasuck09.jpg"
        pause 0.03
        "v09/debrasuck10.jpg"
        pause 0.03
        "v09/debrasuck11.jpg"
        pause 0.03
        "v09/debrasuck12.jpg"
        pause 0.05
        "v09/debrasuck13.jpg"
        pause 0.03
        "v09/debrasuck14.jpg"
        pause 0.03
        "v09/debrasuck15.jpg"
        pause 0.03
        "v09/debrasuck16.jpg"
        pause 0.03
        "v09/debrasuck17.jpg"
        pause 0.03
        "v09/debrasuck18.jpg"
        pause 0.05
        "v09/debrasuck17.jpg"
        pause 0.035
        "v09/debrasuck16.jpg"
        pause 0.035
        "v09/debrasuck15.jpg"
        pause 0.035
        "v09/debrasuck14.jpg"
        pause 0.035
        "v09/debrasuck13.jpg"
        pause 0.035
        "v09/debrasuck11.jpg"
        pause 0.035
        "v09/debrasuck10.jpg"
        pause 0.035
        "v09/debrasuck09.jpg"
        pause 0.035
        "v09/debrasuck08.jpg"
        pause 0.035
        "v09/debrasuck07.jpg"
        pause 0.035
        "v09/debrasuck06.jpg"
        pause 0.035
        "v09/debrasuck05.jpg"
        pause 0.035
        "v09/debrasuck04.jpg"
        pause 0.035
        "v09/debrasuck03.jpg"
        pause 0.035
        "v09/debrasuck02.jpg"
        pause 0.035
        "v09/debrasuck01.jpg"
        pause 0.035
        repeat
            
    image debrarideassslow:
        "v09/debrarideass00.jpg"
        pause 0.06
        "v09/debrarideass01.jpg"
        pause 0.04
        "v09/debrarideass02.jpg"
        pause 0.04
        "v09/debrarideass03.jpg"
        pause 0.04
        "v09/debrarideass04.jpg"
        pause 0.04
        "v09/debrarideass05.jpg"
        pause 0.04
        "v09/debrarideass06.jpg"
        pause 0.04
        "v09/debrarideass07.jpg"
        pause 0.04
        "v09/debrarideass08.jpg"
        pause 0.04
        "v09/debrarideass09.jpg"
        pause 0.04
        "v09/debrarideass10.jpg"
        pause 0.06
        "v09/debrarideass09.jpg"
        pause 0.045
        "v09/debrarideass08.jpg"
        pause 0.045
        "v09/debrarideass07.jpg"
        pause 0.045
        "v09/debrarideass06.jpg"
        pause 0.045
        "v09/debrarideass05.jpg"
        pause 0.045
        "v09/debrarideass04.jpg"
        pause 0.045
        "v09/debrarideass03.jpg"
        pause 0.045
        "v09/debrarideass02.jpg"
        pause 0.045
        "v09/debrarideass01.jpg"
        pause 0.045
        repeat
            
    image debrarideassfast:
        "v09/debrarideass00.jpg"
        pause 0.05
        "v09/debrarideass01.jpg"
        pause 0.03
        "v09/debrarideass02.jpg"
        pause 0.03
        "v09/debrarideass03.jpg"
        pause 0.03
        "v09/debrarideass04.jpg"
        pause 0.03
        "v09/debrarideass05.jpg"
        pause 0.03
        "v09/debrarideass06.jpg"
        pause 0.03
        "v09/debrarideass07.jpg"
        pause 0.03
        "v09/debrarideass08.jpg"
        pause 0.03
        "v09/debrarideass09.jpg"
        pause 0.03
        "v09/debrarideass10.jpg"
        pause 0.05
        "v09/debrarideass09.jpg"
        pause 0.035
        "v09/debrarideass08.jpg"
        pause 0.035
        "v09/debrarideass07.jpg"
        pause 0.035
        "v09/debrarideass06.jpg"
        pause 0.035
        "v09/debrarideass05.jpg"
        pause 0.035
        "v09/debrarideass04.jpg"
        pause 0.035
        "v09/debrarideass03.jpg"
        pause 0.035
        "v09/debrarideass02.jpg"
        pause 0.035
        "v09/debrarideass01.jpg"
        pause 0.035
        repeat
            
    image debrahugeanimslow:
        "v09/debramuscleanim00.jpg"
        pause 0.03
        "v09/debramuscleanim01.jpg"
        pause 0.03
        "v09/debramuscleanim02.jpg"
        pause 0.03
        "v09/debramuscleanim03.jpg"
        pause 0.03
        "v09/debramuscleanim04.jpg"
        pause 0.03
        "v09/debramuscleanim05.jpg"
        pause 0.03
        "v09/debramuscleanim06.jpg"
        pause 0.03
        "v09/debramuscleanim07.jpg"
        pause 0.03
        "v09/debramuscleanim08.jpg"
        pause 0.03
        "v09/debramuscleanim09.jpg"
        pause 0.03
        "v09/debramuscleanim10.jpg"
        pause 0.03
        "v09/debramuscleanim11.jpg"
        pause 0.03
        "v09/debramuscleanim12.jpg"
        pause 0.03
        "v09/debramuscleanim13.jpg"
        pause 0.035
        "v09/debramuscleanim14.jpg"
        pause 0.035
        "v09/debramuscleanim15.jpg"
        pause 0.035
        "v09/debramuscleanim16.jpg"
        pause 0.035
        "v09/debramuscleanim17.jpg"
        pause 0.035
        "v09/debramuscleanim18.jpg"
        pause 0.035
        "v09/debramuscleanim19.jpg"
        pause 0.035
        "v09/debramuscleanim20.jpg"
        pause 0.035
        "v09/debramuscleanim21.jpg"
        pause 0.035
        repeat
            
    image debrahugeanimfast:
        "v09/debramuscleanim00.jpg"
        pause 0.02
        "v09/debramuscleanim01.jpg"
        pause 0.02
        "v09/debramuscleanim02.jpg"
        pause 0.02
        "v09/debramuscleanim03.jpg"
        pause 0.02
        "v09/debramuscleanim04.jpg"
        pause 0.02
        "v09/debramuscleanim05.jpg"
        pause 0.02
        "v09/debramuscleanim06.jpg"
        pause 0.02
        "v09/debramuscleanim07.jpg"
        pause 0.02
        "v09/debramuscleanim08.jpg"
        pause 0.02
        "v09/debramuscleanim09.jpg"
        pause 0.02
        "v09/debramuscleanim10.jpg"
        pause 0.02
        "v09/debramuscleanim11.jpg"
        pause 0.02
        "v09/debramuscleanim12.jpg"
        pause 0.02
        "v09/debramuscleanim13.jpg"
        pause 0.025
        "v09/debramuscleanim14.jpg"
        pause 0.025
        "v09/debramuscleanim15.jpg"
        pause 0.025
        "v09/debramuscleanim16.jpg"
        pause 0.025
        "v09/debramuscleanim17.jpg"
        pause 0.025
        "v09/debramuscleanim18.jpg"
        pause 0.025
        "v09/debramuscleanim19.jpg"
        pause 0.025
        "v09/debramuscleanim20.jpg"
        pause 0.025
        "v09/debramuscleanim21.jpg"
        pause 0.025
        repeat
            
    image debrahugepovanimslow:
        "v09/debramusclepovanim00.jpg"
        pause 0.03
        "v09/debramusclepovanim01.jpg"
        pause 0.03
        "v09/debramusclepovanim02.jpg"
        pause 0.03
        "v09/debramusclepovanim03.jpg"
        pause 0.03
        "v09/debramusclepovanim04.jpg"
        pause 0.03
        "v09/debramusclepovanim05.jpg"
        pause 0.03
        "v09/debramusclepovanim06.jpg"
        pause 0.03
        "v09/debramusclepovanim07.jpg"
        pause 0.03
        "v09/debramusclepovanim08.jpg"
        pause 0.03
        "v09/debramusclepovanim09.jpg"
        pause 0.03
        "v09/debramusclepovanim10.jpg"
        pause 0.03
        "v09/debramusclepovanim11.jpg"
        pause 0.03
        "v09/debramusclepovanim12.jpg"
        pause 0.03
        "v09/debramusclepovanim13.jpg"
        pause 0.035
        "v09/debramusclepovanim14.jpg"
        pause 0.035
        "v09/debramusclepovanim15.jpg"
        pause 0.035
        "v09/debramusclepovanim16.jpg"
        pause 0.035
        "v09/debramusclepovanim17.jpg"
        pause 0.035
        "v09/debramusclepovanim18.jpg"
        pause 0.035
        "v09/debramusclepovanim19.jpg"
        pause 0.035
        "v09/debramusclepovanim20.jpg"
        pause 0.035
        "v09/debramusclepovanim21.jpg"
        pause 0.035
        repeat
            
    image debrahugepovanimfast:
        "v09/debramusclepovanim00.jpg"
        pause 0.02
        "v09/debramusclepovanim01.jpg"
        pause 0.02
        "v09/debramusclepovanim02.jpg"
        pause 0.02
        "v09/debramusclepovanim03.jpg"
        pause 0.02
        "v09/debramusclepovanim04.jpg"
        pause 0.02
        "v09/debramusclepovanim05.jpg"
        pause 0.02
        "v09/debramusclepovanim06.jpg"
        pause 0.02
        "v09/debramusclepovanim07.jpg"
        pause 0.02
        "v09/debramusclepovanim08.jpg"
        pause 0.02
        "v09/debramusclepovanim09.jpg"
        pause 0.02
        "v09/debramusclepovanim10.jpg"
        pause 0.02
        "v09/debramusclepovanim11.jpg"
        pause 0.02
        "v09/debramusclepovanim12.jpg"
        pause 0.02
        "v09/debramusclepovanim13.jpg"
        pause 0.025
        "v09/debramusclepovanim14.jpg"
        pause 0.025
        "v09/debramusclepovanim15.jpg"
        pause 0.025
        "v09/debramusclepovanim16.jpg"
        pause 0.025
        "v09/debramusclepovanim17.jpg"
        pause 0.025
        "v09/debramusclepovanim18.jpg"
        pause 0.025
        "v09/debramusclepovanim19.jpg"
        pause 0.025
        "v09/debramusclepovanim20.jpg"
        pause 0.025
        "v09/debramusclepovanim21.jpg"
        pause 0.025
        repeat
            
    image nancypoolslow:
        "v09/mompoolfuck00.png"
        pause 0.05
        "v09/mompoolfuck01.png"
        pause 0.03
        "v09/mompoolfuck02.png"
        pause 0.03
        "v09/mompoolfuck03.png"
        pause 0.03
        "v09/mompoolfuck04.png"
        pause 0.03
        "v09/mompoolfuck05.png"
        pause 0.03
        "v09/mompoolfuck06.png"
        pause 0.03
        "v09/mompoolfuck07.png"
        pause 0.03
        "v09/mompoolfuck08.png"
        pause 0.03
        "v09/mompoolfuck09.png"
        pause 0.03
        "v09/mompoolfuck10.png"
        pause 0.03
        "v09/mompoolfuck11.png"
        pause 0.05
        "v09/mompoolfuck10.png"
        pause 0.035
        "v09/mompoolfuck09.png"
        pause 0.035
        "v09/mompoolfuck08.png"
        pause 0.035
        "v09/mompoolfuck07.png"
        pause 0.035
        "v09/mompoolfuck06.png"
        pause 0.035
        "v09/mompoolfuck05.png"
        pause 0.035
        "v09/mompoolfuck04.png"
        pause 0.035
        "v09/mompoolfuck03.png"
        pause 0.035
        "v09/mompoolfuck02.png"
        pause 0.035
        "v09/mompoolfuck01.png"
        pause 0.035
        repeat

    image nancypoolfast:
        "v09/mompoolfuck00.png"
        pause 0.04
        "v09/mompoolfuck01.png"
        pause 0.02
        "v09/mompoolfuck02.png"
        pause 0.02
        "v09/mompoolfuck03.png"
        pause 0.02
        "v09/mompoolfuck04.png"
        pause 0.02
        "v09/mompoolfuck05.png"
        pause 0.02
        "v09/mompoolfuck06.png"
        pause 0.02
        "v09/mompoolfuck07.png"
        pause 0.02
        "v09/mompoolfuck08.png"
        pause 0.02
        "v09/mompoolfuck09.png"
        pause 0.02
        "v09/mompoolfuck10.png"
        pause 0.02
        "v09/mompoolfuck11.png"
        pause 0.04
        "v09/mompoolfuck10.png"
        pause 0.025
        "v09/mompoolfuck09.png"
        pause 0.025
        "v09/mompoolfuck08.png"
        pause 0.025
        "v09/mompoolfuck07.png"
        pause 0.025
        "v09/mompoolfuck06.png"
        pause 0.025
        "v09/mompoolfuck05.png"
        pause 0.025
        "v09/mompoolfuck04.png"
        pause 0.025
        "v09/mompoolfuck03.png"
        pause 0.025
        "v09/mompoolfuck02.png"
        pause 0.025
        "v09/mompoolfuck01.png"
        pause 0.025
        repeat

    image kristasexslow:
        "v09/kristasex00.png"
        pause 0.05
        "v09/kristasex01.png"
        pause 0.03
        "v09/kristasex02.png"
        pause 0.03
        "v09/kristasex03.png"
        pause 0.03
        "v09/kristasex04.png"
        pause 0.03
        "v09/kristasex05.png"
        pause 0.03
        "v09/kristasex06.png"
        pause 0.03
        "v09/kristasex07.png"
        pause 0.03
        "v09/kristasex08.png"
        pause 0.03
        "v09/kristasex09.png"
        pause 0.03
        "v09/kristasex10.png"
        pause 0.03
        "v09/kristasex11.png"
        pause 0.03
        "v09/kristasex12.png"
        pause 0.03
        "v09/kristasex13.png"
        pause 0.05
        "v09/kristasex14.png"
        pause 0.035
        "v09/kristasex15.png"
        pause 0.035
        "v09/kristasex16.png"
        pause 0.035
        "v09/kristasex17.png"
        pause 0.035
        "v09/kristasex18.png"
        pause 0.035
        "v09/kristasex19.png"
        pause 0.035
        "v09/kristasex20.png"
        pause 0.035
        "v09/kristasex21.png"
        pause 0.035
        "v09/kristasex22.png"
        pause 0.035
        "v09/kristasex23.png"
        pause 0.035
        "v09/kristasex24.png"
        pause 0.035
        "v09/kristasex25.png"
        pause 0.035
        repeat
            
    image kristasexfast:
        "v09/kristasex00.png"
        pause 0.04
        "v09/kristasex01.png"
        pause 0.02
        "v09/kristasex02.png"
        pause 0.02
        "v09/kristasex03.png"
        pause 0.02
        "v09/kristasex04.png"
        pause 0.02
        "v09/kristasex05.png"
        pause 0.02
        "v09/kristasex06.png"
        pause 0.02
        "v09/kristasex07.png"
        pause 0.02
        "v09/kristasex08.png"
        pause 0.02
        "v09/kristasex09.png"
        pause 0.02
        "v09/kristasex10.png"
        pause 0.02
        "v09/kristasex11.png"
        pause 0.02
        "v09/kristasex12.png"
        pause 0.02
        "v09/kristasex13.png"
        pause 0.04
        "v09/kristasex14.png"
        pause 0.025
        "v09/kristasex15.png"
        pause 0.025
        "v09/kristasex16.png"
        pause 0.025
        "v09/kristasex17.png"
        pause 0.025
        "v09/kristasex18.png"
        pause 0.025
        "v09/kristasex19.png"
        pause 0.025
        "v09/kristasex20.png"
        pause 0.025
        "v09/kristasex21.png"
        pause 0.025
        "v09/kristasex22.png"
        pause 0.025
        "v09/kristasex23.png"
        pause 0.025
        "v09/kristasex24.png"
        pause 0.025
        "v09/kristasex25.png"
        pause 0.025
        repeat
            
    image kristafrontslow:
        "v09/kristafront00.png"
        pause 0.05
        "v09/kristafront01.png"
        pause 0.03
        "v09/kristafront02.png"
        pause 0.03
        "v09/kristafront03.png"
        pause 0.03
        "v09/kristafront04.png"
        pause 0.03
        "v09/kristafront05.png"
        pause 0.03
        "v09/kristafront06.png"
        pause 0.03
        "v09/kristafront07.png"
        pause 0.03
        "v09/kristafront08.png"
        pause 0.03
        "v09/kristafront09.png"
        pause 0.03
        "v09/kristafront10.png"
        pause 0.03
        "v09/kristafront11.png"
        pause 0.03
        "v09/kristafront12.png"
        pause 0.03
        "v09/kristafront13.png"
        pause 0.05
        "v09/kristafront14.png"
        pause 0.035
        "v09/kristafront15.png"
        pause 0.035
        "v09/kristafront16.png"
        pause 0.035
        "v09/kristafront17.png"
        pause 0.035
        "v09/kristafront18.png"
        pause 0.035
        "v09/kristafront19.png"
        pause 0.035
        "v09/kristafront20.png"
        pause 0.035
        "v09/kristafront21.png"
        pause 0.035
        "v09/kristafront22.png"
        pause 0.035
        "v09/kristafront23.png"
        pause 0.035
        "v09/kristafront24.png"
        pause 0.035
        "v09/kristafront25.png"
        pause 0.035
        repeat
            
    image kristafrontfast:
        "v09/kristafront00.png"
        pause 0.04
        "v09/kristafront01.png"
        pause 0.02
        "v09/kristafront02.png"
        pause 0.02
        "v09/kristafront03.png"
        pause 0.02
        "v09/kristafront04.png"
        pause 0.02
        "v09/kristafront05.png"
        pause 0.02
        "v09/kristafront06.png"
        pause 0.02
        "v09/kristafront07.png"
        pause 0.02
        "v09/kristafront08.png"
        pause 0.02
        "v09/kristafront09.png"
        pause 0.02
        "v09/kristafront10.png"
        pause 0.02
        "v09/kristafront11.png"
        pause 0.02
        "v09/kristafront12.png"
        pause 0.02
        "v09/kristafront13.png"
        pause 0.04
        "v09/kristafront14.png"
        pause 0.025
        "v09/kristafront15.png"
        pause 0.025
        "v09/kristafront16.png"
        pause 0.025
        "v09/kristafront17.png"
        pause 0.025
        "v09/kristafront18.png"
        pause 0.025
        "v09/kristafront19.png"
        pause 0.025
        "v09/kristafront20.png"
        pause 0.025
        "v09/kristafront21.png"
        pause 0.025
        "v09/kristafront22.png"
        pause 0.025
        "v09/kristafront23.png"
        pause 0.025
        "v09/kristafront24.png"
        pause 0.025
        "v09/kristafront25.png"
        pause 0.025
        repeat
            
    image melaniaivankablowslow:
        "v10/melaniaivankablow00.png"
        pause 0.06
        "v10/melaniaivankablow01.png"
        pause 0.05
        "v10/melaniaivankablow02.png"
        pause 0.05
        "v10/melaniaivankablow03.png"
        pause 0.05
        "v10/melaniaivankablow04.png"
        pause 0.05
        "v10/melaniaivankablow05.png"
        pause 0.05
        "v10/melaniaivankablow06.png"
        pause 0.05
        "v10/melaniaivankablow07.png"
        pause 0.05
        "v10/melaniaivankablow08.png"
        pause 0.05
        "v10/melaniaivankablow09.png"
        pause 0.05
        "v10/melaniaivankablow10.png"
        pause 0.05
        "v10/melaniaivankablow11.png"
        pause 0.05
        "v10/melaniaivankablow12.png"
        pause 0.06
        "v10/melaniaivankablow11.png"
        pause 0.055
        "v10/melaniaivankablow10.png"
        pause 0.055
        "v10/melaniaivankablow09.png"
        pause 0.055
        "v10/melaniaivankablow08.png"
        pause 0.055
        "v10/melaniaivankablow07.png"
        pause 0.055
        "v10/melaniaivankablow06.png"
        pause 0.055
        "v10/melaniaivankablow05.png"
        pause 0.055
        "v10/melaniaivankablow04.png"
        pause 0.055
        "v10/melaniaivankablow03.png"
        pause 0.055
        "v10/melaniaivankablow02.png"
        pause 0.055
        "v10/melaniaivankablow01.png"
        pause 0.055
        repeat
            
    image melaniaivankablowfast:
        "v10/melaniaivankablow00.png"
        pause 0.05
        "v10/melaniaivankablow01.png"
        pause 0.03
        "v10/melaniaivankablow02.png"
        pause 0.03
        "v10/melaniaivankablow03.png"
        pause 0.03
        "v10/melaniaivankablow04.png"
        pause 0.03
        "v10/melaniaivankablow05.png"
        pause 0.03
        "v10/melaniaivankablow06.png"
        pause 0.03
        "v10/melaniaivankablow07.png"
        pause 0.03
        "v10/melaniaivankablow08.png"
        pause 0.03
        "v10/melaniaivankablow09.png"
        pause 0.03
        "v10/melaniaivankablow10.png"
        pause 0.03
        "v10/melaniaivankablow11.png"
        pause 0.03
        "v10/melaniaivankablow12.png"
        pause 0.05
        "v10/melaniaivankablow11.png"
        pause 0.035
        "v10/melaniaivankablow10.png"
        pause 0.035
        "v10/melaniaivankablow09.png"
        pause 0.035
        "v10/melaniaivankablow08.png"
        pause 0.035
        "v10/melaniaivankablow07.png"
        pause 0.035
        "v10/melaniaivankablow06.png"
        pause 0.035
        "v10/melaniaivankablow05.png"
        pause 0.035
        "v10/melaniaivankablow04.png"
        pause 0.035
        "v10/melaniaivankablow03.png"
        pause 0.035
        "v10/melaniaivankablow02.png"
        pause 0.035
        "v10/melaniaivankablow01.png"
        pause 0.035
        repeat

    image winmelaniaivanka01-6:
        "v10/melaniaivankaanima00.png"
        pause 0.04
        "v10/melaniaivankaanima01.png"
        pause 0.035
        "v10/melaniaivankaanima02.png"
        pause 0.035
        "v10/melaniaivankaanima03.png"
        pause 0.035
        "v10/melaniaivankaanima04.png"
        pause 0.035
        "v10/melaniaivankaanima05.png"
        pause 0.035
        "v10/melaniaivankaanima06.png"
        pause 0.035
        "v10/melaniaivankaanima07.png"
        pause 0.035
        "v10/melaniaivankaanima08.png"
        pause 0.035
        "v10/melaniaivankaanima09.png"
        pause 0.04
        "v10/melaniaivankaanima10.png"
        pause 0.03
        "v10/melaniaivankaanima11.png"
        pause 0.03
        "v10/melaniaivankaanima12.png"
        pause 0.03
        "v10/melaniaivankaanima13.png"
        pause 0.03
        "v10/melaniaivankaanima14.png"
        pause 0.03
        "v10/melaniaivankaanima15.png"
        pause 0.03
        "v10/melaniaivankaanima16.png"
        pause 0.03
        "v10/melaniaivankaanima17.png"
        pause 0.03

    image winmelaniaivanka01-705:
        "v10/melaniaivankaanima00.png"
        pause 0.04
        "v10/melaniaivankaanima01.png"
        pause 0.04
        "v10/melaniaivankaanima02.png"
        pause 0.04
        "v10/melaniaivankaanima03.png"
        pause 0.04
        "v10/melaniaivankaanima04.png"
        pause 0.04
        "v10/melaniaivankaanima05.png"
        pause 0.04
        "v10/melaniaivankaanima06.png"
        pause 0.04
        "v10/melaniaivankaanima07.png"
        pause 0.04
        "v10/melaniaivankaanima08.png"
        pause 0.04
        "v10/melaniaivankaanima09.png"
        pause 0.05
        "v10/melaniaivankaanima10.png"
        pause 0.04
        "v10/melaniaivankaanima11.png"
        pause 0.04
        "v10/melaniaivankaanima12.png"
        pause 0.04
        "v10/melaniaivankaanima13.png"
        pause 0.04
        "v10/melaniaivankaanima14.png"
        pause 0.035
        "v10/melaniaivankaanima15.png"
        pause 0.035
        "v10/melaniaivankaanima16.png"
        pause 0.035
        "v10/melaniaivankaanima17.png"
        pause 0.03
            
    image winmelaniaivanka01-74:
        "v10/melaniaivankaanima00.png"
        pause 0.05
        "v10/melaniaivankaanima01.png"
        pause 0.04
        "v10/melaniaivankaanima02.png"
        pause 0.04
        "v10/melaniaivankaanima03.png"
        pause 0.04
        "v10/melaniaivankaanima04.png"
        pause 0.04
        "v10/melaniaivankaanima05.png"
        pause 0.04
        "v10/melaniaivankaanima06.png"
        pause 0.04
        "v10/melaniaivankaanima07.png"
        pause 0.04
        "v10/melaniaivankaanima08.png"
        pause 0.04
        "v10/melaniaivankaanima09.png"
        pause 0.05
        "v10/melaniaivankaanima10.png"
        pause 0.04
        "v10/melaniaivankaanima11.png"
        pause 0.04
        "v10/melaniaivankaanima12.png"
        pause 0.04
        "v10/melaniaivankaanima13.png"
        pause 0.04
        "v10/melaniaivankaanima14.png"
        pause 0.04
        "v10/melaniaivankaanima15.png"
        pause 0.04
        "v10/melaniaivankaanima16.png"
        pause 0.04
        "v10/melaniaivankaanima17.png"
        pause 0.04
            
    image winmelaniaivanka01-79:
        "v10/melaniaivankaanima00.png"
        pause 0.055
        "v10/melaniaivankaanima01.png"
        pause 0.045
        "v10/melaniaivankaanima02.png"
        pause 0.045
        "v10/melaniaivankaanima03.png"
        pause 0.045
        "v10/melaniaivankaanima04.png"
        pause 0.045
        "v10/melaniaivankaanima05.png"
        pause 0.045
        "v10/melaniaivankaanima06.png"
        pause 0.045
        "v10/melaniaivankaanima07.png"
        pause 0.045
        "v10/melaniaivankaanima08.png"
        pause 0.045
        "v10/melaniaivankaanima09.png"
        pause 0.05
        "v10/melaniaivankaanima10.png"
        pause 0.045
        "v10/melaniaivankaanima11.png"
        pause 0.04
        "v10/melaniaivankaanima12.png"
        pause 0.04
        "v10/melaniaivankaanima13.png"
        pause 0.04
        "v10/melaniaivankaanima14.png"
        pause 0.04
        "v10/melaniaivankaanima15.png"
        pause 0.04
        "v10/melaniaivankaanima16.png"
        pause 0.04
        "v10/melaniaivankaanima17.png"
        pause 0.04

    image winmelaniaivanka01-95:
        "v10/melaniaivankaanima00.png"
        pause 0.06
        "v10/melaniaivankaanima01.png"
        pause 0.055
        "v10/melaniaivankaanima02.png"
        pause 0.055
        "v10/melaniaivankaanima03.png"
        pause 0.05
        "v10/melaniaivankaanima04.png"
        pause 0.05
        "v10/melaniaivankaanima05.png"
        pause 0.05
        "v10/melaniaivankaanima06.png"
        pause 0.05
        "v10/melaniaivankaanima07.png"
        pause 0.05
        "v10/melaniaivankaanima08.png"
        pause 0.06
        "v10/melaniaivankaanima09.png"
        pause 0.07
        "v10/melaniaivankaanima10.png"
        pause 0.06
        "v10/melaniaivankaanima11.png"
        pause 0.05
        "v10/melaniaivankaanima12.png"
        pause 0.05
        "v10/melaniaivankaanima13.png"
        pause 0.05
        "v10/melaniaivankaanima14.png"
        pause 0.05
        "v10/melaniaivankaanima15.png"
        pause 0.05
        "v10/melaniaivankaanima16.png"
        pause 0.05
        "v10/melaniaivankaanima17.png"
        pause 0.05
        
    image winmelaniaivanka02-6:
        "v10/melaniaivanka02anim00.png"
        pause 0.04
        "v10/melaniaivanka02anim01.png"
        pause 0.035
        "v10/melaniaivanka02anim02.png"
        pause 0.035
        "v10/melaniaivanka02anim03.png"
        pause 0.035
        "v10/melaniaivanka02anim04.png"
        pause 0.035
        "v10/melaniaivanka02anim05.png"
        pause 0.035
        "v10/melaniaivanka02anim06.png"
        pause 0.035
        "v10/melaniaivanka02anim07.png"
        pause 0.035
        "v10/melaniaivanka02anim08.png"
        pause 0.035
        "v10/melaniaivanka02anim09.png"
        pause 0.04
        "v10/melaniaivanka02anim10.png"
        pause 0.03
        "v10/melaniaivanka02anim11.png"
        pause 0.03
        "v10/melaniaivanka02anim12.png"
        pause 0.03
        "v10/melaniaivanka02anim13.png"
        pause 0.03
        "v10/melaniaivanka02anim14.png"
        pause 0.03
        "v10/melaniaivanka02anim15.png"
        pause 0.03
        "v10/melaniaivanka02anim16.png"
        pause 0.03
        "v10/melaniaivanka02anim17.png"
        pause 0.03
            
    image winmelaniaivanka02-705:
        "v10/melaniaivanka02anim00.png"
        pause 0.04
        "v10/melaniaivanka02anim01.png"
        pause 0.04
        "v10/melaniaivanka02anim02.png"
        pause 0.04
        "v10/melaniaivanka02anim03.png"
        pause 0.04
        "v10/melaniaivanka02anim04.png"
        pause 0.04
        "v10/melaniaivanka02anim05.png"
        pause 0.04
        "v10/melaniaivanka02anim06.png"
        pause 0.04
        "v10/melaniaivanka02anim07.png"
        pause 0.04
        "v10/melaniaivanka02anim08.png"
        pause 0.04
        "v10/melaniaivanka02anim09.png"
        pause 0.05
        "v10/melaniaivanka02anim10.png"
        pause 0.04
        "v10/melaniaivanka02anim11.png"
        pause 0.04
        "v10/melaniaivanka02anim12.png"
        pause 0.04
        "v10/melaniaivanka02anim13.png"
        pause 0.04
        "v10/melaniaivanka02anim14.png"
        pause 0.035
        "v10/melaniaivanka02anim15.png"
        pause 0.035
        "v10/melaniaivanka02anim16.png"
        pause 0.035
        "v10/melaniaivanka02anim17.png"
        pause 0.03
            
    image winmelaniaivanka02-74:
        "v10/melaniaivanka02anim00.png"
        pause 0.05
        "v10/melaniaivanka02anim01.png"
        pause 0.04
        "v10/melaniaivanka02anim02.png"
        pause 0.04
        "v10/melaniaivanka02anim03.png"
        pause 0.04
        "v10/melaniaivanka02anim04.png"
        pause 0.04
        "v10/melaniaivanka02anim05.png"
        pause 0.04
        "v10/melaniaivanka02anim06.png"
        pause 0.04
        "v10/melaniaivanka02anim07.png"
        pause 0.04
        "v10/melaniaivanka02anim08.png"
        pause 0.04
        "v10/melaniaivanka02anim09.png"
        pause 0.05
        "v10/melaniaivanka02anim10.png"
        pause 0.04
        "v10/melaniaivanka02anim11.png"
        pause 0.04
        "v10/melaniaivanka02anim12.png"
        pause 0.04
        "v10/melaniaivanka02anim13.png"
        pause 0.04
        "v10/melaniaivanka02anim14.png"
        pause 0.04
        "v10/melaniaivanka02anim15.png"
        pause 0.04
        "v10/melaniaivanka02anim16.png"
        pause 0.04
        "v10/melaniaivanka02anim17.png"
        pause 0.04
            
    image winmelaniaivanka02-79:
        "v10/melaniaivanka02anim00.png"
        pause 0.055
        "v10/melaniaivanka02anim01.png"
        pause 0.045
        "v10/melaniaivanka02anim02.png"
        pause 0.045
        "v10/melaniaivanka02anim03.png"
        pause 0.045
        "v10/melaniaivanka02anim04.png"
        pause 0.045
        "v10/melaniaivanka02anim05.png"
        pause 0.045
        "v10/melaniaivanka02anim06.png"
        pause 0.045
        "v10/melaniaivanka02anim07.png"
        pause 0.045
        "v10/melaniaivanka02anim08.png"
        pause 0.045
        "v10/melaniaivanka02anim09.png"
        pause 0.05
        "v10/melaniaivanka02anim10.png"
        pause 0.045
        "v10/melaniaivanka02anim11.png"
        pause 0.04
        "v10/melaniaivanka02anim12.png"
        pause 0.04
        "v10/melaniaivanka02anim13.png"
        pause 0.04
        "v10/melaniaivanka02anim14.png"
        pause 0.04
        "v10/melaniaivanka02anim15.png"
        pause 0.04
        "v10/melaniaivanka02anim16.png"
        pause 0.04
        "v10/melaniaivanka02anim17.png"
        pause 0.04

    image winmelaniaivanka02-95:
        "v10/melaniaivanka02anim00.png"
        pause 0.06
        "v10/melaniaivanka02anim01.png"
        pause 0.055
        "v10/melaniaivanka02anim02.png"
        pause 0.055
        "v10/melaniaivanka02anim03.png"
        pause 0.05
        "v10/melaniaivanka02anim04.png"
        pause 0.05
        "v10/melaniaivanka02anim05.png"
        pause 0.05
        "v10/melaniaivanka02anim06.png"
        pause 0.05
        "v10/melaniaivanka02anim07.png"
        pause 0.05
        "v10/melaniaivanka02anim08.png"
        pause 0.06
        "v10/melaniaivanka02anim09.png"
        pause 0.07
        "v10/melaniaivanka02anim10.png"
        pause 0.06
        "v10/melaniaivanka02anim11.png"
        pause 0.05
        "v10/melaniaivanka02anim12.png"
        pause 0.05
        "v10/melaniaivanka02anim13.png"
        pause 0.05
        "v10/melaniaivanka02anim14.png"
        pause 0.05
        "v10/melaniaivanka02anim15.png"
        pause 0.05
        "v10/melaniaivanka02anim16.png"
        pause 0.05
        "v10/melaniaivanka02anim17.png"
        pause 0.05
            
    image winmelaniaivanka03-95:
        "v10/melaniaivankaanimc00.png"
        pause 0.045
        "v10/melaniaivankaanimc01.png"
        pause 0.045
        "v10/melaniaivankaanimc02.png"
        pause 0.045
        "v10/melaniaivankaanimc03.png"
        pause 0.045
        "v10/melaniaivankaanimc04.png"
        pause 0.045
        "v10/melaniaivankaanimc05.png"
        pause 0.045
        "v10/melaniaivankaanimc06.png"
        pause 0.045
        "v10/melaniaivankaanimc07.png"
        pause 0.045
        "v10/melaniaivankaanimc08.png"
        pause 0.045
        "v10/melaniaivankaanimc09.png"
        pause 0.045
        "v10/melaniaivankaanimc10.png"
        pause 0.045
        "v10/melaniaivankaanimc11.png"
        pause 0.045
        "v10/melaniaivankaanimc12.png"
        pause 0.05
        "v10/melaniaivankaanimc13.png"
        pause 0.03
        "v10/melaniaivankaanimc14.png"
        pause 0.03
        "v10/melaniaivankaanimc15.png"
        pause 0.03
        "v10/melaniaivankaanimc16.png"
        pause 0.03
        "v10/melaniaivankaanimc17.png"
        pause 0.03
        "v10/melaniaivankaanimc18.png"
        pause 0.03
        "v10/melaniaivankaanimc19.png"
        pause 0.03
        "v10/melaniaivankaanimc20.png"
        pause 0.03
        "v10/melaniaivankaanimc21.png"
        pause 0.03
        "v10/melaniaivankaanimc22.png"
        pause 0.03
        "v10/melaniaivankaanimc23.png"
        pause 0.03
            
    image winmelaniaivanka03-79:
        "v10/melaniaivankaanimc00.png"
        pause 0.035
        "v10/melaniaivankaanimc01.png"
        pause 0.035
        "v10/melaniaivankaanimc02.png"
        pause 0.035
        "v10/melaniaivankaanimc03.png"
        pause 0.035
        "v10/melaniaivankaanimc04.png"
        pause 0.035
        "v10/melaniaivankaanimc05.png"
        pause 0.035
        "v10/melaniaivankaanimc06.png"
        pause 0.035
        "v10/melaniaivankaanimc07.png"
        pause 0.035
        "v10/melaniaivankaanimc08.png"
        pause 0.035
        "v10/melaniaivankaanimc09.png"
        pause 0.035
        "v10/melaniaivankaanimc10.png"
        pause 0.035
        "v10/melaniaivankaanimc11.png"
        pause 0.035
        "v10/melaniaivankaanimc12.png"
        pause 0.04
        "v10/melaniaivankaanimc13.png"
        pause 0.025
        "v10/melaniaivankaanimc14.png"
        pause 0.025
        "v10/melaniaivankaanimc15.png"
        pause 0.025
        "v10/melaniaivankaanimc16.png"
        pause 0.025
        "v10/melaniaivankaanimc17.png"
        pause 0.025
        "v10/melaniaivankaanimc18.png"
        pause 0.025
        "v10/melaniaivankaanimc19.png"
        pause 0.03
        "v10/melaniaivankaanimc20.png"
        pause 0.03
        "v10/melaniaivankaanimc21.png"
        pause 0.03
        "v10/melaniaivankaanimc22.png"
        pause 0.03
        "v10/melaniaivankaanimc23.png"
        pause 0.03

    image winmelaniaivanka03-74:
        "v10/melaniaivankaanimc00.png"
        pause 0.03
        "v10/melaniaivankaanimc01.png"
        pause 0.03
        "v10/melaniaivankaanimc02.png"
        pause 0.03
        "v10/melaniaivankaanimc03.png"
        pause 0.03
        "v10/melaniaivankaanimc04.png"
        pause 0.03
        "v10/melaniaivankaanimc05.png"
        pause 0.03
        "v10/melaniaivankaanimc06.png"
        pause 0.03
        "v10/melaniaivankaanimc07.png"
        pause 0.03
        "v10/melaniaivankaanimc08.png"
        pause 0.03
        "v10/melaniaivankaanimc09.png"
        pause 0.03
        "v10/melaniaivankaanimc10.png"
        pause 0.035
        "v10/melaniaivankaanimc11.png"
        pause 0.035
        "v10/melaniaivankaanimc12.png"
        pause 0.04
        "v10/melaniaivankaanimc13.png"
        pause 0.025
        "v10/melaniaivankaanimc14.png"
        pause 0.025
        "v10/melaniaivankaanimc15.png"
        pause 0.025
        "v10/melaniaivankaanimc16.png"
        pause 0.025
        "v10/melaniaivankaanimc17.png"
        pause 0.025
        "v10/melaniaivankaanimc18.png"
        pause 0.025
        "v10/melaniaivankaanimc19.png"
        pause 0.03
        "v10/melaniaivankaanimc20.png"
        pause 0.03
        "v10/melaniaivankaanimc21.png"
        pause 0.03
        "v10/melaniaivankaanimc22.png"
        pause 0.03
        "v10/melaniaivankaanimc23.png"
        pause 0.03

    image winmelaniaivanka03-705:
        "v10/melaniaivankaanimc00.png"
        pause 0.03
        "v10/melaniaivankaanimc01.png"
        pause 0.03
        "v10/melaniaivankaanimc02.png"
        pause 0.03
        "v10/melaniaivankaanimc03.png"
        pause 0.03
        "v10/melaniaivankaanimc04.png"
        pause 0.03
        "v10/melaniaivankaanimc05.png"
        pause 0.03
        "v10/melaniaivankaanimc06.png"
        pause 0.03
        "v10/melaniaivankaanimc07.png"
        pause 0.03
        "v10/melaniaivankaanimc08.png"
        pause 0.03
        "v10/melaniaivankaanimc09.png"
        pause 0.03
        "v10/melaniaivankaanimc10.png"
        pause 0.03
        "v10/melaniaivankaanimc11.png"
        pause 0.03
        "v10/melaniaivankaanimc12.png"
        pause 0.04
        "v10/melaniaivankaanimc13.png"
        pause 0.025
        "v10/melaniaivankaanimc14.png"
        pause 0.025
        "v10/melaniaivankaanimc15.png"
        pause 0.025
        "v10/melaniaivankaanimc16.png"
        pause 0.025
        "v10/melaniaivankaanimc17.png"
        pause 0.025
        "v10/melaniaivankaanimc18.png"
        pause 0.025
        "v10/melaniaivankaanimc19.png"
        pause 0.025
        "v10/melaniaivankaanimc20.png"
        pause 0.025
        "v10/melaniaivankaanimc21.png"
        pause 0.025
        "v10/melaniaivankaanimc22.png"
        pause 0.025
        "v10/melaniaivankaanimc23.png"
        pause 0.025
            
    image winmelaniaivanka03-6:
        "v10/melaniaivankaanimc00.png"
        pause 0.025
        "v10/melaniaivankaanimc01.png"
        pause 0.025
        "v10/melaniaivankaanimc02.png"
        pause 0.025
        "v10/melaniaivankaanimc03.png"
        pause 0.025
        "v10/melaniaivankaanimc04.png"
        pause 0.025
        "v10/melaniaivankaanimc05.png"
        pause 0.025
        "v10/melaniaivankaanimc06.png"
        pause 0.025
        "v10/melaniaivankaanimc07.png"
        pause 0.025
        "v10/melaniaivankaanimc08.png"
        pause 0.025
        "v10/melaniaivankaanimc09.png"
        pause 0.025
        "v10/melaniaivankaanimc10.png"
        pause 0.025
        "v10/melaniaivankaanimc11.png"
        pause 0.025
        "v10/melaniaivankaanimc12.png"
        pause 0.04
        "v10/melaniaivankaanimc13.png"
        pause 0.020
        "v10/melaniaivankaanimc14.png"
        pause 0.020
        "v10/melaniaivankaanimc15.png"
        pause 0.020
        "v10/melaniaivankaanimc16.png"
        pause 0.020
        "v10/melaniaivankaanimc17.png"
        pause 0.020
        "v10/melaniaivankaanimc18.png"
        pause 0.020
        "v10/melaniaivankaanimc19.png"
        pause 0.020
        "v10/melaniaivankaanimc20.png"
        pause 0.020
        "v10/melaniaivankaanimc21.png"
        pause 0.02
        "v10/melaniaivankaanimc22.png"
        pause 0.025
        "v10/melaniaivankaanimc23.png"
        pause 0.025
            
    image windebrafuck:
        "v10/debraorgy00.png"
        pause 0.04
        "v10/debraorgy01.png"
        pause 0.035
        "v10/debraorgy02.png"
        pause 0.035
        "v10/debraorgy03.png"
        pause 0.035
        "v10/debraorgy04.png"
        pause 0.035
        "v10/debraorgy05.png"
        pause 0.035
        "v10/debraorgy06.png"
        pause 0.035
        "v10/debraorgy07.png"
        pause 0.035
        "v10/debraorgy08.png"
        pause 0.035
        "v10/debraorgy09.png"
        pause 0.04
        "v10/debraorgy10.png"
        pause 0.03
        "v10/debraorgy11.png"
        pause 0.03
        "v10/debraorgy12.png"
        pause 0.03
        "v10/debraorgy13.png"
        pause 0.03
        "v10/debraorgy14.png"
        pause 0.03
        "v10/debraorgy15.png"
        pause 0.03
        "v10/debraorgy16.png"
        pause 0.03
        "v10/debraorgy17.png"
        pause 0.03
        
    image winbellafuck:
        "v10/orgybella00.png"
        pause 0.04
        "v10/orgybella01.png"
        pause 0.035
        "v10/orgybella02.png"
        pause 0.035
        "v10/orgybella03.png"
        pause 0.035
        "v10/orgybella04.png"
        pause 0.035
        "v10/orgybella05.png"
        pause 0.035
        "v10/orgybella06.png"
        pause 0.035
        "v10/orgybella07.png"
        pause 0.035
        "v10/orgybella08.png"
        pause 0.035
        "v10/orgybella09.png"
        pause 0.04
        "v10/orgybella10.png"
        pause 0.03
        "v10/orgybella11.png"
        pause 0.03
        "v10/orgybella12.png"
        pause 0.03
        "v10/orgybella13.png"
        pause 0.03
        "v10/orgybella14.png"
        pause 0.03
        "v10/orgybella15.png"
        pause 0.03
        "v10/orgybella16.png"
        pause 0.03
        "v10/orgybella17.png"
        pause 0.03
            
    image winmarniefuck:
        "v10/orgymarnie00.png"
        pause 0.04
        "v10/orgymarnie01.png"
        pause 0.035
        "v10/orgymarnie02.png"
        pause 0.035
        "v10/orgymarnie03.png"
        pause 0.035
        "v10/orgymarnie04.png"
        pause 0.035
        "v10/orgymarnie05.png"
        pause 0.035
        "v10/orgymarnie06.png"
        pause 0.035
        "v10/orgymarnie07.png"
        pause 0.035
        "v10/orgymarnie08.png"
        pause 0.035
        "v10/orgymarnie09.png"
        pause 0.04
        "v10/orgymarnie10.png"
        pause 0.03
        "v10/orgymarnie11.png"
        pause 0.03
        "v10/orgymarnie12.png"
        pause 0.03
        "v10/orgymarnie13.png"
        pause 0.03
        "v10/orgymarnie14.png"
        pause 0.03
        "v10/orgymarnie15.png"
        pause 0.03
        "v10/orgymarnie16.png"
        pause 0.03
        "v10/orgymarnie17.png"
        pause 0.03

    image winangiefuck:
        "v10/orgyangie00.png"
        pause 0.04
        "v10/orgyangie01.png"
        pause 0.035
        "v10/orgyangie02.png"
        pause 0.035
        "v10/orgyangie03.png"
        pause 0.035
        "v10/orgyangie04.png"
        pause 0.035
        "v10/orgyangie05.png"
        pause 0.035
        "v10/orgyangie06.png"
        pause 0.035
        "v10/orgyangie07.png"
        pause 0.035
        "v10/orgyangie08.png"
        pause 0.035
        "v10/orgyangie09.png"
        pause 0.04
        "v10/orgyangie10.png"
        pause 0.03
        "v10/orgyangie11.png"
        pause 0.03
        "v10/orgyangie12.png"
        pause 0.03
        "v10/orgyangie13.png"
        pause 0.03
        "v10/orgyangie14.png"
        pause 0.03
        "v10/orgyangie15.png"
        pause 0.03
        "v10/orgyangie16.png"
        pause 0.03
        "v10/orgyangie17.png"
        pause 0.03
        "v10/orgyangie18.png"
        pause 0.03
        "v10/orgyangie19.png"
        pause 0.03
        "v10/orgyangie20.png"
        pause 0.03
        "v10/orgyangie21.png"
        pause 0.03
        "v10/orgyangie22.png"
        pause 0.03
        "v10/orgyangie23.png"
        pause 0.03
        "v10/orgyangie24.png"
        pause 0.03
        "v10/orgyangie25.png"
        pause 0.03
        "v10/orgyangie26.png"
        pause 0.03
        "v10/orgyangie27.png"
        pause 0.03
        "v10/orgyangie28.png"
        pause 0.03
        "v10/orgyangie29.png"
        pause 0.03
        "v10/orgyangie30.png"
        pause 0.03

    image winaylafuck:
        "v10/orgyayla00.png"
        pause 0.04
        "v10/orgyayla01.png"
        pause 0.035
        "v10/orgyayla02.png"
        pause 0.035
        "v10/orgyayla03.png"
        pause 0.035
        "v10/orgyayla04.png"
        pause 0.035
        "v10/orgyayla05.png"
        pause 0.035
        "v10/orgyayla06.png"
        pause 0.035
        "v10/orgyayla07.png"
        pause 0.035
        "v10/orgyayla08.png"
        pause 0.035
        "v10/orgyayla09.png"
        pause 0.04
        "v10/orgyayla10.png"
        pause 0.03
        "v10/orgyayla11.png"
        pause 0.03
        "v10/orgyayla12.png"
        pause 0.03
        "v10/orgyayla13.png"
        pause 0.03
        "v10/orgyayla14.png"
        pause 0.03
        "v10/orgyayla15.png"
        pause 0.03
        "v10/orgyayla16.png"
        pause 0.03
        "v10/orgyayla17.png"
        pause 0.03
        "v10/orgyayla18.png"
        pause 0.03
        "v10/orgyayla19.png"
        pause 0.03
        "v10/orgyayla20.png"
        pause 0.03
        "v10/orgyayla21.png"
        pause 0.03
        "v10/orgyayla22.png"
        pause 0.03
        "v10/orgyayla23.png"
        pause 0.03
        "v10/orgyayla24.png"
        pause 0.03
        "v10/orgyayla25.png"
        pause 0.03
        "v10/orgyayla26.png"
        pause 0.03
        "v10/orgyayla27.png"
        pause 0.03
        "v10/orgyayla28.png"
        pause 0.03
        "v10/orgyayla29.png"
        pause 0.03
            
    image winbarbarafuck:
        "v10/orgybarbara00.png"
        pause 0.04
        "v10/orgybarbara01.png"
        pause 0.035
        "v10/orgybarbara02.png"
        pause 0.035
        "v10/orgybarbara03.png"
        pause 0.035
        "v10/orgybarbara04.png"
        pause 0.035
        "v10/orgybarbara05.png"
        pause 0.035
        "v10/orgybarbara06.png"
        pause 0.035
        "v10/orgybarbara07.png"
        pause 0.035
        "v10/orgybarbara08.png"
        pause 0.035
        "v10/orgybarbara09.png"
        pause 0.04
        "v10/orgybarbara10.png"
        pause 0.03
        "v10/orgybarbara11.png"
        pause 0.03
        "v10/orgybarbara12.png"
        pause 0.03
        "v10/orgybarbara13.png"
        pause 0.03
        "v10/orgybarbara14.png"
        pause 0.03
        "v10/orgybarbara15.png"
        pause 0.03
        "v10/orgybarbara16.png"
        pause 0.03
        "v10/orgybarbara17.png"
        pause 0.03
        "v10/orgybarbara18.png"
        pause 0.03
        "v10/orgybarbara19.png"
        pause 0.03
        "v10/orgybarbara20.png"
        pause 0.03
        "v10/orgybarbara21.png"
        pause 0.03
        "v10/orgybarbara22.png"
        pause 0.03
        "v10/orgybarbara23.png"
        pause 0.03
        "v10/orgybarbara24.png"
        pause 0.03
        "v10/orgybarbara25.png"
        pause 0.03
        "v10/orgybarbara26.png"
        pause 0.03
        "v10/orgybarbara27.png"
        pause 0.03
        "v10/orgybarbara28.png"
        pause 0.03
        "v10/orgybarbara29.png"
        pause 0.03
        "v10/orgybarbara30.png"
        pause 0.03
            
    image wingwenfuck:
        "v10/orgygwen00.png"
        pause 0.04
        "v10/orgygwen01.png"
        pause 0.035
        "v10/orgygwen02.png"
        pause 0.035
        "v10/orgygwen03.png"
        pause 0.035
        "v10/orgygwen04.png"
        pause 0.035
        "v10/orgygwen05.png"
        pause 0.035
        "v10/orgygwen06.png"
        pause 0.035
        "v10/orgygwen07.png"
        pause 0.035
        "v10/orgygwen08.png"
        pause 0.035
        "v10/orgygwen09.png"
        pause 0.035
        "v10/orgygwen10.png"
        pause 0.035
        "v10/orgygwen11.png"
        pause 0.035
        "v10/orgygwen12.png"
        pause 0.035
        "v10/orgygwen13.png"
        pause 0.03
        "v10/orgygwen14.png"
        pause 0.03
        "v10/orgygwen15.png"
        pause 0.03
        "v10/orgygwen16.png"
        pause 0.03
        "v10/orgygwen17.png"
        pause 0.03
        "v10/orgygwen18.png"
        pause 0.03
        "v10/orgygwen19.png"
        pause 0.03
        "v10/orgygwen20.png"
        pause 0.03
        "v10/orgygwen21.png"
        pause 0.03
        "v10/orgygwen22.png"
        pause 0.03
        "v10/orgygwen23.png"
        pause 0.03
            
    image winlenafuck:
        "v10/orgylena00.png"
        pause 0.04
        "v10/orgylena01.png"
        pause 0.035
        "v10/orgylena02.png"
        pause 0.035
        "v10/orgylena03.png"
        pause 0.035
        "v10/orgylena04.png"
        pause 0.035
        "v10/orgylena05.png"
        pause 0.035
        "v10/orgylena06.png"
        pause 0.035
        "v10/orgylena07.png"
        pause 0.035
        "v10/orgylena08.png"
        pause 0.035
        "v10/orgylena09.png"
        pause 0.035
        "v10/orgylena10.png"
        pause 0.035
        "v10/orgylena11.png"
        pause 0.035
        "v10/orgylena12.png"
        pause 0.035
        "v10/orgylena13.png"
        pause 0.03
        "v10/orgylena14.png"
        pause 0.03
        "v10/orgylena15.png"
        pause 0.03
        "v10/orgylena16.png"
        pause 0.03
        "v10/orgylena17.png"
        pause 0.03
        "v10/orgylena18.png"
        pause 0.03
        "v10/orgylena19.png"
        pause 0.03
        "v10/orgylena20.png"
        pause 0.03
        "v10/orgylena21.png"
        pause 0.03
        "v10/orgylena22.png"
        pause 0.03
        "v10/orgylena23.png"
        pause 0.03
            
    image winsukifuck:
        "v10/orgysuki00.png"
        pause 0.04
        "v10/orgysuki01.png"
        pause 0.035
        "v10/orgysuki02.png"
        pause 0.035
        "v10/orgysuki03.png"
        pause 0.035
        "v10/orgysuki04.png"
        pause 0.035
        "v10/orgysuki05.png"
        pause 0.035
        "v10/orgysuki06.png"
        pause 0.035
        "v10/orgysuki07.png"
        pause 0.035
        "v10/orgysuki08.png"
        pause 0.035
        "v10/orgysuki09.png"
        pause 0.035
        "v10/orgysuki10.png"
        pause 0.035
        "v10/orgysuki11.png"
        pause 0.035
        "v10/orgysuki12.png"
        pause 0.035
        "v10/orgysuki13.png"
        pause 0.03
        "v10/orgysuki14.png"
        pause 0.03
        "v10/orgysuki15.png"
        pause 0.03
        "v10/orgysuki16.png"
        pause 0.03
        "v10/orgysuki17.png"
        pause 0.03
        "v10/orgysuki18.png"
        pause 0.03
        "v10/orgysuki19.png"
        pause 0.03
        "v10/orgysuki20.png"
        pause 0.03
        "v10/orgysuki21.png"
        pause 0.03
        "v10/orgysuki22.png"
        pause 0.03
        "v10/orgysuki23.png"
        pause 0.03
 
    image winnancyfuck:
        "v10/orgynancy00.png"
        pause 0.04
        "v10/orgynancy01.png"
        pause 0.03
        "v10/orgynancy02.png"
        pause 0.03
        "v10/orgynancy03.png"
        pause 0.03
        "v10/orgynancy04.png"
        pause 0.03
        "v10/orgynancy05.png"
        pause 0.03
        "v10/orgynancy06.png"
        pause 0.03
        "v10/orgynancy07.png"
        pause 0.03
        "v10/orgynancy08.png"
        pause 0.03
        "v10/orgynancy09.png"
        pause 0.03
        "v10/orgynancy10.png"
        pause 0.04
        "v10/orgynancy09.png"
        pause 0.035
        "v10/orgynancy08.png"
        pause 0.035
        "v10/orgynancy07.png"
        pause 0.035
        "v10/orgynancy06.png"
        pause 0.035
        "v10/orgynancy05.png"
        pause 0.035
        "v10/orgynancy04.png"
        pause 0.035
        "v10/orgynancy03.png"
        pause 0.035
        "v10/orgynancy02.png"
        pause 0.035
        "v10/orgynancy01.png"
        pause 0.035
            
    image winamyfuck:
        "v10/orgyamy00.png"
        pause 0.04
        "v10/orgyamy01.png"
        pause 0.03
        "v10/orgyamy02.png"
        pause 0.03
        "v10/orgyamy03.png"
        pause 0.03
        "v10/orgyamy04.png"
        pause 0.03
        "v10/orgyamy05.png"
        pause 0.03
        "v10/orgyamy06.png"
        pause 0.03
        "v10/orgyamy07.png"
        pause 0.03
        "v10/orgyamy08.png"
        pause 0.03
        "v10/orgyamy09.png"
        pause 0.03
        "v10/orgyamy10.png"
        pause 0.04
        "v10/orgyamy09.png"
        pause 0.035
        "v10/orgyamy08.png"
        pause 0.035
        "v10/orgyamy07.png"
        pause 0.035
        "v10/orgyamy06.png"
        pause 0.035
        "v10/orgyamy05.png"
        pause 0.035
        "v10/orgyamy04.png"
        pause 0.035
        "v10/orgyamy03.png"
        pause 0.035
        "v10/orgyamy02.png"
        pause 0.035
        "v10/orgyamy01.png"
        pause 0.035

    image winmichikofuck:
        "v10/orgymichiko00.png"
        pause 0.04
        "v10/orgymichiko01.png"
        pause 0.03
        "v10/orgymichiko02.png"
        pause 0.03
        "v10/orgymichiko03.png"
        pause 0.03
        "v10/orgymichiko04.png"
        pause 0.03
        "v10/orgymichiko05.png"
        pause 0.03
        "v10/orgymichiko06.png"
        pause 0.03
        "v10/orgymichiko07.png"
        pause 0.03
        "v10/orgymichiko08.png"
        pause 0.03
        "v10/orgymichiko09.png"
        pause 0.03
        "v10/orgymichiko10.png"
        pause 0.04
        "v10/orgymichiko09.png"
        pause 0.035
        "v10/orgymichiko08.png"
        pause 0.035
        "v10/orgymichiko07.png"
        pause 0.035
        "v10/orgymichiko06.png"
        pause 0.035
        "v10/orgymichiko05.png"
        pause 0.035
        "v10/orgymichiko04.png"
        pause 0.035
        "v10/orgymichiko03.png"
        pause 0.035
        "v10/orgymichiko02.png"
        pause 0.035
        "v10/orgymichiko01.png"
        pause 0.035
            
    image wintaylorfuck:
        "v10/orgytaylor00.png"
        pause 0.04
        "v10/orgytaylor01.png"
        pause 0.03
        "v10/orgytaylor02.png"
        pause 0.03
        "v10/orgytaylor03.png"
        pause 0.03
        "v10/orgytaylor04.png"
        pause 0.03
        "v10/orgytaylor05.png"
        pause 0.03
        "v10/orgytaylor06.png"
        pause 0.03
        "v10/orgytaylor07.png"
        pause 0.03
        "v10/orgytaylor08.png"
        pause 0.03
        "v10/orgytaylor09.png"
        pause 0.03
        "v10/orgytaylor10.png"
        pause 0.03
        "v10/orgytaylor11.png"
        pause 0.03
        "v10/orgytaylor12.png"
        pause 0.04
        "v10/orgytaylor13.png"
        pause 0.030
        "v10/orgytaylor14.png"
        pause 0.030
        "v10/orgytaylor15.png"
        pause 0.030
        "v10/orgytaylor16.png"
        pause 0.030
        "v10/orgytaylor17.png"
        pause 0.030
        "v10/orgytaylor18.png"
        pause 0.030
        "v10/orgytaylor19.png"
        pause 0.030
        "v10/orgytaylor20.png"
        pause 0.030
        "v10/orgytaylor21.png"
        pause 0.030
        "v10/orgytaylor22.png"
        pause 0.030
        "v10/orgytaylor23.png"
        pause 0.030

    image winzarafuck:
        "v10/orgyzara00.png"
        pause 0.04
        "v10/orgyzara01.png"
        pause 0.03
        "v10/orgyzara02.png"
        pause 0.03
        "v10/orgyzara03.png"
        pause 0.03
        "v10/orgyzara04.png"
        pause 0.03
        "v10/orgyzara05.png"
        pause 0.03
        "v10/orgyzara06.png"
        pause 0.03
        "v10/orgyzara07.png"
        pause 0.03
        "v10/orgyzara08.png"
        pause 0.03
        "v10/orgyzara09.png"
        pause 0.03
        "v10/orgyzara10.png"
        pause 0.03
        "v10/orgyzara11.png"
        pause 0.03
        "v10/orgyzara12.png"
        pause 0.04
        "v10/orgyzara13.png"
        pause 0.030
        "v10/orgyzara14.png"
        pause 0.030
        "v10/orgyzara15.png"
        pause 0.030
        "v10/orgyzara16.png"
        pause 0.030
        "v10/orgyzara17.png"
        pause 0.030
        "v10/orgyzara18.png"
        pause 0.030
        "v10/orgyzara19.png"
        pause 0.030
        "v10/orgyzara20.png"
        pause 0.030
        "v10/orgyzara21.png"
        pause 0.030
        "v10/orgyzara22.png"
        pause 0.030
        "v10/orgyzara23.png"
        pause 0.030

    image wintarafuck:
        "v10/orgytara00.png"
        pause 0.04
        "v10/orgytara01.png"
        pause 0.03
        "v10/orgytara02.png"
        pause 0.03
        "v10/orgytara03.png"
        pause 0.03
        "v10/orgytara04.png"
        pause 0.03
        "v10/orgytara05.png"
        pause 0.03
        "v10/orgytara06.png"
        pause 0.03
        "v10/orgytara07.png"
        pause 0.03
        "v10/orgytara08.png"
        pause 0.03
        "v10/orgytara09.png"
        pause 0.03
        "v10/orgytara10.png"
        pause 0.03
        "v10/orgytara11.png"
        pause 0.03
        "v10/orgytara12.png"
        pause 0.04
        "v10/orgytara13.png"
        pause 0.030
        "v10/orgytara14.png"
        pause 0.030
        "v10/orgytara15.png"
        pause 0.030
        "v10/orgytara16.png"
        pause 0.030
        "v10/orgytara17.png"
        pause 0.030
        "v10/orgytara18.png"
        pause 0.030
        "v10/orgytara19.png"
        pause 0.030
        "v10/orgytara20.png"
        pause 0.030
        "v10/orgytara21.png"
        pause 0.030
        "v10/orgytara22.png"
        pause 0.030
        "v10/orgytara23.png"
        pause 0.030
            
    image winpennyfuck:
        "v10/orgypenny00.png"
        pause 0.04
        "v10/orgypenny01.png"
        pause 0.03
        "v10/orgypenny02.png"
        pause 0.03
        "v10/orgypenny03.png"
        pause 0.03
        "v10/orgypenny04.png"
        pause 0.03
        "v10/orgypenny05.png"
        pause 0.03
        "v10/orgypenny06.png"
        pause 0.03
        "v10/orgypenny07.png"
        pause 0.03
        "v10/orgypenny08.png"
        pause 0.03
        "v10/orgypenny09.png"
        pause 0.03
        "v10/orgypenny10.png"
        pause 0.03
        "v10/orgypenny11.png"
        pause 0.03
        "v10/orgypenny12.png"
        pause 0.04
        "v10/orgypenny11.png"
        pause 0.030
        "v10/orgypenny10.png"
        pause 0.030
        "v10/orgypenny09.png"
        pause 0.030
        "v10/orgypenny08.png"
        pause 0.030
        "v10/orgypenny07.png"
        pause 0.030
        "v10/orgypenny06.png"
        pause 0.030
        "v10/orgypenny05.png"
        pause 0.030
        "v10/orgypenny04.png"
        pause 0.030
        "v10/orgypenny03.png"
        pause 0.030
        "v10/orgypenny02.png"
        pause 0.030
        "v10/orgypenny01.png"
        pause 0.030

    image winrubyfuck:
        "v10/orgyruby00.png"
        pause 0.04
        "v10/orgyruby01.png"
        pause 0.03
        "v10/orgyruby02.png"
        pause 0.03
        "v10/orgyruby03.png"
        pause 0.03
        "v10/orgyruby04.png"
        pause 0.03
        "v10/orgyruby05.png"
        pause 0.03
        "v10/orgyruby06.png"
        pause 0.03
        "v10/orgyruby07.png"
        pause 0.03
        "v10/orgyruby08.png"
        pause 0.03
        "v10/orgyruby09.png"
        pause 0.03
        "v10/orgyruby10.png"
        pause 0.03
        "v10/orgyruby11.png"
        pause 0.03
        "v10/orgyruby12.png"
        pause 0.04
        "v10/orgyruby11.png"
        pause 0.030
        "v10/orgyruby10.png"
        pause 0.030
        "v10/orgyruby09.png"
        pause 0.030
        "v10/orgyruby08.png"
        pause 0.030
        "v10/orgyruby07.png"
        pause 0.030
        "v10/orgyruby06.png"
        pause 0.030
        "v10/orgyruby05.png"
        pause 0.030
        "v10/orgyruby04.png"
        pause 0.030
        "v10/orgyruby03.png"
        pause 0.030
        "v10/orgyruby02.png"
        pause 0.030
        "v10/orgyruby01.png"
        pause 0.030
            
    image winlauriefuck:
        "v10/orgylaurie00.png"
        pause 0.04
        "v10/orgylaurie01.png"
        pause 0.03
        "v10/orgylaurie02.png"
        pause 0.03
        "v10/orgylaurie03.png"
        pause 0.03
        "v10/orgylaurie04.png"
        pause 0.03
        "v10/orgylaurie05.png"
        pause 0.03
        "v10/orgylaurie06.png"
        pause 0.03
        "v10/orgylaurie07.png"
        pause 0.03
        "v10/orgylaurie08.png"
        pause 0.03
        "v10/orgylaurie09.png"
        pause 0.03
        "v10/orgylaurie10.png"
        pause 0.03
        "v10/orgylaurie11.png"
        pause 0.03
        "v10/orgylaurie12.png"
        pause 0.04
        "v10/orgylaurie11.png"
        pause 0.030
        "v10/orgylaurie10.png"
        pause 0.030
        "v10/orgylaurie09.png"
        pause 0.030
        "v10/orgylaurie08.png"
        pause 0.030
        "v10/orgylaurie07.png"
        pause 0.030
        "v10/orgylaurie06.png"
        pause 0.030
        "v10/orgylaurie05.png"
        pause 0.030
        "v10/orgylaurie04.png"
        pause 0.030
        "v10/orgylaurie03.png"
        pause 0.030
        "v10/orgylaurie02.png"
        pause 0.030
        "v10/orgylaurie01.png"
        pause 0.030
            
    image wincyrlfuck:
        "v10/orgycyrl00.png"
        pause 0.04
        "v10/orgycyrl01.png"
        pause 0.03
        "v10/orgycyrl02.png"
        pause 0.03
        "v10/orgycyrl03.png"
        pause 0.03
        "v10/orgycyrl04.png"
        pause 0.03
        "v10/orgycyrl05.png"
        pause 0.03
        "v10/orgycyrl06.png"
        pause 0.03
        "v10/orgycyrl07.png"
        pause 0.03
        "v10/orgycyrl08.png"
        pause 0.03
        "v10/orgycyrl09.png"
        pause 0.03
        "v10/orgycyrl10.png"
        pause 0.03
        "v10/orgycyrl11.png"
        pause 0.03
        "v10/orgycyrl12.png"
        pause 0.04
        "v10/orgycyrl11.png"
        pause 0.030
        "v10/orgycyrl10.png"
        pause 0.030
        "v10/orgycyrl09.png"
        pause 0.030
        "v10/orgycyrl08.png"
        pause 0.030
        "v10/orgycyrl07.png"
        pause 0.030
        "v10/orgycyrl06.png"
        pause 0.030
        "v10/orgycyrl05.png"
        pause 0.030
        "v10/orgycyrl04.png"
        pause 0.030
        "v10/orgycyrl03.png"
        pause 0.030
        "v10/orgycyrl02.png"
        pause 0.030
        "v10/orgycyrl01.png"
        pause 0.030
            
    image winclarafuck:
        "v10/orgyclara00.png"
        pause 0.04
        "v10/orgyclara01.png"
        pause 0.03
        "v10/orgyclara02.png"
        pause 0.03
        "v10/orgyclara03.png"
        pause 0.03
        "v10/orgyclara04.png"
        pause 0.03
        "v10/orgyclara05.png"
        pause 0.03
        "v10/orgyclara06.png"
        pause 0.03
        "v10/orgyclara07.png"
        pause 0.03
        "v10/orgyclara08.png"
        pause 0.03
        "v10/orgyclara09.png"
        pause 0.03
        "v10/orgyclara10.png"
        pause 0.03
        "v10/orgyclara11.png"
        pause 0.03
        "v10/orgyclara12.png"
        pause 0.04
        "v10/orgyclara11.png"
        pause 0.030
        "v10/orgyclara10.png"
        pause 0.030
        "v10/orgyclara09.png"
        pause 0.030
        "v10/orgyclara08.png"
        pause 0.030
        "v10/orgyclara07.png"
        pause 0.030
        "v10/orgyclara06.png"
        pause 0.030
        "v10/orgyclara05.png"
        pause 0.030
        "v10/orgyclara04.png"
        pause 0.030
        "v10/orgyclara03.png"
        pause 0.030
        "v10/orgyclara02.png"
        pause 0.030
        "v10/orgyclara01.png"
        pause 0.030
            
    image winrachelfuck:
        "v10/orgyrachel00.png"
        pause 0.04
        "v10/orgyrachel01.png"
        pause 0.035
        "v10/orgyrachel02.png"
        pause 0.035
        "v10/orgyrachel03.png"
        pause 0.035
        "v10/orgyrachel04.png"
        pause 0.035
        "v10/orgyrachel05.png"
        pause 0.035
        "v10/orgyrachel06.png"
        pause 0.035
        "v10/orgyrachel07.png"
        pause 0.035
        "v10/orgyrachel08.png"
        pause 0.035
        "v10/orgyrachel09.png"
        pause 0.035
        "v10/orgyrachel10.png"
        pause 0.035
        "v10/orgyrachel11.png"
        pause 0.035
        "v10/orgyrachel12.png"
        pause 0.035
        "v10/orgyrachel13.png"
        pause 0.03
        "v10/orgyrachel14.png"
        pause 0.03
        "v10/orgyrachel15.png"
        pause 0.03
        "v10/orgyrachel16.png"
        pause 0.03
        "v10/orgyrachel17.png"
        pause 0.03
        "v10/orgyrachel18.png"
        pause 0.03
        "v10/orgyrachel19.png"
        pause 0.03
        "v10/orgyrachel20.png"
        pause 0.03
        "v10/orgyrachel21.png"
        pause 0.03
        "v10/orgyrachel22.png"
        pause 0.03
        "v10/orgyrachel23.png"
        pause 0.03

    image winwendyfuck:
        "v10/orgywendy00.png"
        pause 0.04
        "v10/orgywendy01.png"
        pause 0.035
        "v10/orgywendy02.png"
        pause 0.035
        "v10/orgywendy03.png"
        pause 0.035
        "v10/orgywendy04.png"
        pause 0.035
        "v10/orgywendy05.png"
        pause 0.035
        "v10/orgywendy06.png"
        pause 0.035
        "v10/orgywendy07.png"
        pause 0.035
        "v10/orgywendy08.png"
        pause 0.035
        "v10/orgywendy09.png"
        pause 0.035
        "v10/orgywendy10.png"
        pause 0.035
        "v10/orgywendy11.png"
        pause 0.035
        "v10/orgywendy12.png"
        pause 0.035
        "v10/orgywendy13.png"
        pause 0.03
        "v10/orgywendy14.png"
        pause 0.03
        "v10/orgywendy15.png"
        pause 0.03
        "v10/orgywendy16.png"
        pause 0.03
        "v10/orgywendy17.png"
        pause 0.03
        "v10/orgywendy18.png"
        pause 0.03
        "v10/orgywendy19.png"
        pause 0.03
        "v10/orgywendy20.png"
        pause 0.03
        "v10/orgywendy21.png"
        pause 0.03
        "v10/orgywendy22.png"
        pause 0.03
        "v10/orgywendy23.png"
        pause 0.03
            
    image winwidowfuck:
        "v10/orgywidow00.png"
        pause 0.04
        "v10/orgywidow01.png"
        pause 0.035
        "v10/orgywidow02.png"
        pause 0.035
        "v10/orgywidow03.png"
        pause 0.035
        "v10/orgywidow04.png"
        pause 0.035
        "v10/orgywidow05.png"
        pause 0.035
        "v10/orgywidow06.png"
        pause 0.035
        "v10/orgywidow07.png"
        pause 0.035
        "v10/orgywidow08.png"
        pause 0.035
        "v10/orgywidow09.png"
        pause 0.035
        "v10/orgywidow10.png"
        pause 0.035
        "v10/orgywidow11.png"
        pause 0.035
        "v10/orgywidow12.png"
        pause 0.035
        "v10/orgywidow13.png"
        pause 0.03
        "v10/orgywidow14.png"
        pause 0.03
        "v10/orgywidow15.png"
        pause 0.03
        "v10/orgywidow16.png"
        pause 0.03
        "v10/orgywidow17.png"
        pause 0.03
        "v10/orgywidow18.png"
        pause 0.03
        "v10/orgywidow19.png"
        pause 0.03
        "v10/orgywidow20.png"
        pause 0.03
        "v10/orgywidow21.png"
        pause 0.03
        "v10/orgywidow22.png"
        pause 0.03
        "v10/orgywidow23.png"
        pause 0.03
            
    image winpaulettefuck:
        "v10/orgypaulete00.png"
        pause 0.04
        "v10/orgypaulete01.png"
        pause 0.03
        "v10/orgypaulete02.png"
        pause 0.03
        "v10/orgypaulete03.png"
        pause 0.03
        "v10/orgypaulete04.png"
        pause 0.03
        "v10/orgypaulete05.png"
        pause 0.03
        "v10/orgypaulete06.png"
        pause 0.03
        "v10/orgypaulete07.png"
        pause 0.03
        "v10/orgypaulete08.png"
        pause 0.03
        "v10/orgypaulete09.png"
        pause 0.03
        "v10/orgypaulete10.png"
        pause 0.03
        "v10/orgypaulete11.png"
        pause 0.03
        "v10/orgypaulete12.png"
        pause 0.04
        "v10/orgypaulete11.png"
        pause 0.030
        "v10/orgypaulete10.png"
        pause 0.030
        "v10/orgypaulete09.png"
        pause 0.030
        "v10/orgypaulete08.png"
        pause 0.030
        "v10/orgypaulete07.png"
        pause 0.030
        "v10/orgypaulete06.png"
        pause 0.030
        "v10/orgypaulete05.png"
        pause 0.030
        "v10/orgypaulete04.png"
        pause 0.030
        "v10/orgypaulete03.png"
        pause 0.030
        "v10/orgypaulete02.png"
        pause 0.030
        "v10/orgypaulete01.png"
        pause 0.030
            
    image ivankawhfuckslow:
        "v10/whdoggyivanka00.png"
        pause 0.05
        "v10/whdoggyivanka01.png"
        pause 0.04
        "v10/whdoggyivanka02.png"
        pause 0.04
        "v10/whdoggyivanka03.png"
        pause 0.04
        "v10/whdoggyivanka04.png"
        pause 0.04
        "v10/whdoggyivanka05.png"
        pause 0.04
        "v10/whdoggyivanka06.png"
        pause 0.04
        "v10/whdoggyivanka07.png"
        pause 0.04
        "v10/whdoggyivanka08.png"
        pause 0.04
        "v10/whdoggyivanka09.png"
        pause 0.04
        "v10/whdoggyivanka10.png"
        pause 0.04
        "v10/whdoggyivanka11.png"
        pause 0.04
        "v10/whdoggyivanka12.png"
        pause 0.05
        "v10/whdoggyivanka13.png"
        pause 0.045
        "v10/whdoggyivanka14.png"
        pause 0.045
        "v10/whdoggyivanka15.png"
        pause 0.045
        "v10/whdoggyivanka16.png"
        pause 0.045
        "v10/whdoggyivanka17.png"
        pause 0.045
        "v10/whdoggyivanka18.png"
        pause 0.045
        "v10/whdoggyivanka19.png"
        pause 0.045
        "v10/whdoggyivanka20.png"
        pause 0.045
        "v10/whdoggyivanka21.png"
        pause 0.045
        "v10/whdoggyivanka22.png"
        pause 0.045
        "v10/whdoggyivanka23.png"
        pause 0.045
        repeat
            
    image ivankawhfuckfast:
        "v10/whdoggyivanka00.png"
        pause 0.04
        "v10/whdoggyivanka01.png"
        pause 0.03
        "v10/whdoggyivanka02.png"
        pause 0.03
        "v10/whdoggyivanka03.png"
        pause 0.03
        "v10/whdoggyivanka04.png"
        pause 0.03
        "v10/whdoggyivanka05.png"
        pause 0.03
        "v10/whdoggyivanka06.png"
        pause 0.03
        "v10/whdoggyivanka07.png"
        pause 0.03
        "v10/whdoggyivanka08.png"
        pause 0.03
        "v10/whdoggyivanka09.png"
        pause 0.03
        "v10/whdoggyivanka10.png"
        pause 0.03
        "v10/whdoggyivanka11.png"
        pause 0.03
        "v10/whdoggyivanka12.png"
        pause 0.04
        "v10/whdoggyivanka13.png"
        pause 0.035
        "v10/whdoggyivanka14.png"
        pause 0.035
        "v10/whdoggyivanka15.png"
        pause 0.035
        "v10/whdoggyivanka16.png"
        pause 0.035
        "v10/whdoggyivanka17.png"
        pause 0.035
        "v10/whdoggyivanka18.png"
        pause 0.035
        "v10/whdoggyivanka19.png"
        pause 0.035
        "v10/whdoggyivanka20.png"
        pause 0.035
        "v10/whdoggyivanka21.png"
        pause 0.035
        "v10/whdoggyivanka22.png"
        pause 0.035
        "v10/whdoggyivanka23.png"
        pause 0.035
        repeat
            
    image ivankatopwhfuckslow:
        "v10/whdoggyivankatop00.png"
        pause 0.05
        "v10/whdoggyivankatop01.png"
        pause 0.04
        "v10/whdoggyivankatop02.png"
        pause 0.04
        "v10/whdoggyivankatop03.png"
        pause 0.04
        "v10/whdoggyivankatop04.png"
        pause 0.04
        "v10/whdoggyivankatop05.png"
        pause 0.04
        "v10/whdoggyivankatop06.png"
        pause 0.04
        "v10/whdoggyivankatop07.png"
        pause 0.04
        "v10/whdoggyivankatop08.png"
        pause 0.04
        "v10/whdoggyivankatop09.png"
        pause 0.04
        "v10/whdoggyivankatop10.png"
        pause 0.04
        "v10/whdoggyivankatop11.png"
        pause 0.04
        "v10/whdoggyivankatop12.png"
        pause 0.05
        "v10/whdoggyivankatop13.png"
        pause 0.045
        "v10/whdoggyivankatop14.png"
        pause 0.045
        "v10/whdoggyivankatop15.png"
        pause 0.045
        "v10/whdoggyivankatop16.png"
        pause 0.045
        "v10/whdoggyivankatop17.png"
        pause 0.045
        "v10/whdoggyivankatop18.png"
        pause 0.045
        "v10/whdoggyivankatop19.png"
        pause 0.045
        "v10/whdoggyivankatop20.png"
        pause 0.045
        "v10/whdoggyivankatop21.png"
        pause 0.045
        "v10/whdoggyivankatop22.png"
        pause 0.045
        "v10/whdoggyivankatop23.png"
        pause 0.045
        repeat
            
    image ivankatopwhfuckfast:
        "v10/whdoggyivankatop00.png"
        pause 0.04
        "v10/whdoggyivankatop01.png"
        pause 0.03
        "v10/whdoggyivankatop02.png"
        pause 0.03
        "v10/whdoggyivankatop03.png"
        pause 0.03
        "v10/whdoggyivankatop04.png"
        pause 0.03
        "v10/whdoggyivankatop05.png"
        pause 0.03
        "v10/whdoggyivankatop06.png"
        pause 0.03
        "v10/whdoggyivankatop07.png"
        pause 0.03
        "v10/whdoggyivankatop08.png"
        pause 0.03
        "v10/whdoggyivankatop09.png"
        pause 0.03
        "v10/whdoggyivankatop10.png"
        pause 0.03
        "v10/whdoggyivankatop11.png"
        pause 0.03
        "v10/whdoggyivankatop12.png"
        pause 0.04
        "v10/whdoggyivankatop13.png"
        pause 0.035
        "v10/whdoggyivankatop14.png"
        pause 0.035
        "v10/whdoggyivankatop15.png"
        pause 0.035
        "v10/whdoggyivankatop16.png"
        pause 0.035
        "v10/whdoggyivankatop17.png"
        pause 0.035
        "v10/whdoggyivankatop18.png"
        pause 0.035
        "v10/whdoggyivankatop19.png"
        pause 0.035
        "v10/whdoggyivankatop20.png"
        pause 0.035
        "v10/whdoggyivankatop21.png"
        pause 0.035
        "v10/whdoggyivankatop22.png"
        pause 0.035
        "v10/whdoggyivankatop23.png"
        pause 0.035
        repeat
            
    image melaniawhdoggyslow:
        "v10/melaniawhdoggy00.png"
        pause 0.04
        "v10/melaniawhdoggy01.png"
        pause 0.035
        "v10/melaniawhdoggy02.png"
        pause 0.035
        "v10/melaniawhdoggy03.png"
        pause 0.035
        "v10/melaniawhdoggy04.png"
        pause 0.035
        "v10/melaniawhdoggy05.png"
        pause 0.035
        "v10/melaniawhdoggy06.png"
        pause 0.035
        "v10/melaniawhdoggy07.png"
        pause 0.035
        "v10/melaniawhdoggy08.png"
        pause 0.035
        "v10/melaniawhdoggy09.png"
        pause 0.035
        "v10/melaniawhdoggy10.png"
        pause 0.035
        "v10/melaniawhdoggy11.png"
        pause 0.035
        "v10/melaniawhdoggy12.png"
        pause 0.04
        "v10/melaniawhdoggy11.png"
        pause 0.035
        "v10/melaniawhdoggy10.png"
        pause 0.035
        "v10/melaniawhdoggy09.png"
        pause 0.035
        "v10/melaniawhdoggy08.png"
        pause 0.035
        "v10/melaniawhdoggy07.png"
        pause 0.035
        "v10/melaniawhdoggy06.png"
        pause 0.035
        "v10/melaniawhdoggy05.png"
        pause 0.035
        "v10/melaniawhdoggy04.png"
        pause 0.035
        "v10/melaniawhdoggy03.png"
        pause 0.035
        "v10/melaniawhdoggy02.png"
        pause 0.035
        "v10/melaniawhdoggy01.png"
        pause 0.035
        repeat
    
    image melaniawhdoggyfast:
        "v10/melaniawhdoggy00.png"
        pause 0.03
        "v10/melaniawhdoggy01.png"
        pause 0.025
        "v10/melaniawhdoggy02.png"
        pause 0.025
        "v10/melaniawhdoggy03.png"
        pause 0.025
        "v10/melaniawhdoggy04.png"
        pause 0.025
        "v10/melaniawhdoggy05.png"
        pause 0.025
        "v10/melaniawhdoggy06.png"
        pause 0.025
        "v10/melaniawhdoggy07.png"
        pause 0.025
        "v10/melaniawhdoggy08.png"
        pause 0.025
        "v10/melaniawhdoggy09.png"
        pause 0.025
        "v10/melaniawhdoggy10.png"
        pause 0.025
        "v10/melaniawhdoggy11.png"
        pause 0.025
        "v10/melaniawhdoggy12.png"
        pause 0.03
        "v10/melaniawhdoggy11.png"
        pause 0.025
        "v10/melaniawhdoggy10.png"
        pause 0.025
        "v10/melaniawhdoggy09.png"
        pause 0.025
        "v10/melaniawhdoggy08.png"
        pause 0.025
        "v10/melaniawhdoggy07.png"
        pause 0.025
        "v10/melaniawhdoggy06.png"
        pause 0.025
        "v10/melaniawhdoggy05.png"
        pause 0.025
        "v10/melaniawhdoggy04.png"
        pause 0.025
        "v10/melaniawhdoggy03.png"
        pause 0.025
        "v10/melaniawhdoggy02.png"
        pause 0.025
        "v10/melaniawhdoggy01.png"
        pause 0.025
        repeat
            
    image whpredoggyanimslow:
        "v10/whitehousepredoggyanim00.png"
        pause 0.04
        "v10/whitehousepredoggyanim01.png"
        pause 0.035
        "v10/whitehousepredoggyanim02.png"
        pause 0.035
        "v10/whitehousepredoggyanim03.png"
        pause 0.035
        "v10/whitehousepredoggyanim04.png"
        pause 0.035
        "v10/whitehousepredoggyanim05.png"
        pause 0.035
        "v10/whitehousepredoggyanim06.png"
        pause 0.035
        "v10/whitehousepredoggyanim07.png"
        pause 0.035
        "v10/whitehousepredoggyanim08.png"
        pause 0.035
        "v10/whitehousepredoggyanim09.png"
        pause 0.035
        "v10/whitehousepredoggyanim10.png"
        pause 0.035
        "v10/whitehousepredoggyanim11.png"
        pause 0.035
        "v10/whitehousepredoggyanim12.png"
        pause 0.04
        "v10/whitehousepredoggyanim11.png"
        pause 0.035
        "v10/whitehousepredoggyanim10.png"
        pause 0.035
        "v10/whitehousepredoggyanim09.png"
        pause 0.035
        "v10/whitehousepredoggyanim08.png"
        pause 0.035
        "v10/whitehousepredoggyanim07.png"
        pause 0.035
        "v10/whitehousepredoggyanim06.png"
        pause 0.035
        "v10/whitehousepredoggyanim05.png"
        pause 0.035
        "v10/whitehousepredoggyanim04.png"
        pause 0.035
        "v10/whitehousepredoggyanim03.png"
        pause 0.035
        "v10/whitehousepredoggyanim02.png"
        pause 0.035
        "v10/whitehousepredoggyanim01.png"
        pause 0.035
        repeat
    
    image kimwankslow:
        "v10/kimwank00.png"
        pause 0.04
        "v10/kimwank01.png"
        pause 0.035
        "v10/kimwank02.png"
        pause 0.035
        "v10/kimwank03.png"
        pause 0.035
        "v10/kimwank04.png"
        pause 0.035
        "v10/kimwank05.png"
        pause 0.035
        "v10/kimwank06.png"
        pause 0.035
        "v10/kimwank07.png"
        pause 0.035
        "v10/kimwank08.png"
        pause 0.035
        "v10/kimwank09.png"
        pause 0.035
        "v10/kimwank10.png"
        pause 0.035
        "v10/kimwank11.png"
        pause 0.035
        "v10/kimwank12.png"
        pause 0.035
        "v10/kimwank13.png"
        pause 0.04
        "v10/kimwank12.png"
        pause 0.035
        "v10/kimwank11.png"
        pause 0.035
        "v10/kimwank10.png"
        pause 0.035
        "v10/kimwank09.png"
        pause 0.035
        "v10/kimwank08.png"
        pause 0.035
        "v10/kimwank07.png"
        pause 0.035
        "v10/kimwank06.png"
        pause 0.035
        "v10/kimwank05.png"
        pause 0.035
        "v10/kimwank04.png"
        pause 0.035
        "v10/kimwank03.png"
        pause 0.035
        "v10/kimwank02.png"
        pause 0.035
        "v10/kimwank01.png"
        pause 0.035
        repeat
    
    image kimwankfast:
        "v10/kimwank00.png"
        pause 0.03
        "v10/kimwank01.png"
        pause 0.025
        "v10/kimwank02.png"
        pause 0.025
        "v10/kimwank03.png"
        pause 0.025
        "v10/kimwank04.png"
        pause 0.025
        "v10/kimwank05.png"
        pause 0.025
        "v10/kimwank06.png"
        pause 0.025
        "v10/kimwank07.png"
        pause 0.025
        "v10/kimwank08.png"
        pause 0.025
        "v10/kimwank09.png"
        pause 0.025
        "v10/kimwank10.png"
        pause 0.025
        "v10/kimwank11.png"
        pause 0.025
        "v10/kimwank12.png"
        pause 0.025
        "v10/kimwank13.png"
        pause 0.03
        "v10/kimwank12.png"
        pause 0.025
        "v10/kimwank11.png"
        pause 0.025
        "v10/kimwank10.png"
        pause 0.025
        "v10/kimwank09.png"
        pause 0.025
        "v10/kimwank08.png"
        pause 0.025
        "v10/kimwank07.png"
        pause 0.025
        "v10/kimwank06.png"
        pause 0.025
        "v10/kimwank05.png"
        pause 0.025
        "v10/kimwank04.png"
        pause 0.025
        "v10/kimwank03.png"
        pause 0.025
        "v10/kimwank02.png"
        pause 0.025
        "v10/kimwank01.png"
        pause 0.025
        repeat
            
    image kimfuckslow:
        "v10/kimwhfuck00.jpg"
        pause 0.05
        "v10/kimwhfuck01.jpg"
        pause 0.045
        "v10/kimwhfuck02.jpg"
        pause 0.045
        "v10/kimwhfuck03.jpg"
        pause 0.045
        "v10/kimwhfuck04.jpg"
        pause 0.045
        "v10/kimwhfuck05.jpg"
        pause 0.045
        "v10/kimwhfuck06.jpg"
        pause 0.045
        "v10/kimwhfuck07.jpg"
        pause 0.045
        "v10/kimwhfuck08.jpg"
        pause 0.045
        "v10/kimwhfuck09.jpg"
        pause 0.045
        "v10/kimwhfuck10.jpg"
        pause 0.045
        "v10/kimwhfuck11.jpg"
        pause 0.045
        "v10/kimwhfuck12.jpg"
        pause 0.05
        "v10/kimwhfuck13.jpg"
        pause 0.04
        "v10/kimwhfuck14.jpg"
        pause 0.04
        "v10/kimwhfuck15.jpg"
        pause 0.04
        "v10/kimwhfuck16.jpg"
        pause 0.04
        "v10/kimwhfuck17.jpg"
        pause 0.04
        "v10/kimwhfuck18.jpg"
        pause 0.04
        "v10/kimwhfuck19.jpg"
        pause 0.04
        "v10/kimwhfuck20.jpg"
        pause 0.04
        "v10/kimwhfuck21.jpg"
        pause 0.04
        "v10/kimwhfuck22.jpg"
        pause 0.04
        "v10/kimwhfuck23.jpg"
        pause 0.04
        repeat
            
    image kimfuckfast:
        "v10/kimwhfuck00.jpg"
        pause 0.04
        "v10/kimwhfuck01.jpg"
        pause 0.035
        "v10/kimwhfuck02.jpg"
        pause 0.035
        "v10/kimwhfuck03.jpg"
        pause 0.035
        "v10/kimwhfuck04.jpg"
        pause 0.035
        "v10/kimwhfuck05.jpg"
        pause 0.035
        "v10/kimwhfuck06.jpg"
        pause 0.035
        "v10/kimwhfuck07.jpg"
        pause 0.035
        "v10/kimwhfuck08.jpg"
        pause 0.035
        "v10/kimwhfuck09.jpg"
        pause 0.035
        "v10/kimwhfuck10.jpg"
        pause 0.035
        "v10/kimwhfuck11.jpg"
        pause 0.035
        "v10/kimwhfuck12.jpg"
        pause 0.04
        "v10/kimwhfuck13.jpg"
        pause 0.03
        "v10/kimwhfuck14.jpg"
        pause 0.03
        "v10/kimwhfuck15.jpg"
        pause 0.03
        "v10/kimwhfuck16.jpg"
        pause 0.03
        "v10/kimwhfuck17.jpg"
        pause 0.03
        "v10/kimwhfuck18.jpg"
        pause 0.03
        "v10/kimwhfuck19.jpg"
        pause 0.03
        "v10/kimwhfuck20.jpg"
        pause 0.03
        "v10/kimwhfuck21.jpg"
        pause 0.03
        "v10/kimwhfuck22.jpg"
        pause 0.03
        "v10/kimwhfuck23.jpg"
        pause 0.03
        repeat
            
    image kristaballs:
        "v081/kristaballs01.png" with fastdissolve
        pause 0.3
        "v081/kristaballs02.png" with fastdissolve
        pause 0.3
        repeat

    image alien02suck:
        "v071/aliensprefuck03a.jpg" with fastdissolve
        pause 0.4
        "v071/aliensprefuck03b.jpg" with fastdissolve
        pause 0.4
        repeat

    image clarahugewank:
        "v071/claraprehuge01a.png" with fastdissolve
        pause 0.4
        "v071/claraprehuge01b.png" with fastdissolve
        pause 0.4
        repeat

    image alienslickanim:
        "v071/alienslick02.jpg" with fastdissolve
        pause 0.4
        "v071/alienslick03.jpg" with fastdissolve
        pause 0.4
        repeat

    image marniefemdomstick:
        "v07/marniefemdom06a.jpg" with fastdissolve
        pause 0.5
        "v07/marniefemdom06b.jpg" with fastdissolve
        pause 0.4
        "v07/marniefemdom06c.jpg" with fastdissolve
        pause 0.5
        "v07/marniefemdom06b.jpg" with fastdissolve
        pause 0.4
        repeat

    image marniemaledomblowslow:
        "v07/marniemaledom07a.jpg" with fastdissolve
        pause 0.4
        "v07/marniemaledom07b.jpg" with fastdissolve
        pause 0.4
        repeat

    image marniemaledomblowfast:
        "v07/marniemaledom07a.jpg" with fastdissolve
        pause 0.3
        "v07/marniemaledom07b.jpg" with fastdissolve
        pause 0.3
        repeat

    image melaniasofiafuck:
        "v07/melania26.png" with fastdissolve
        pause 0.4
        "v07/melania27.png" with fastdissolve
        pause 0.4
        repeat

    image lenadateslow:
        "v061/lenadate11.jpg"
        pause 0.35
        "v061/lenadate12.jpg"
        pause 0.35
        repeat

    image lenadatefast:
        "v061/lenadate11.jpg"
        pause 0.25
        "v061/lenadate12.jpg"
        pause 0.25
        repeat

    image lenadatebothslow:
        "v061/lenadate14.jpg"
        pause 0.35
        "v061/lenadate15.jpg"
        pause 0.35
        repeat

    image lenadatebothfast:
        "v061/lenadate14.jpg"
        pause 0.25
        "v061/lenadate15.jpg"
        pause 0.25
        repeat
    
    transform pitfall:
        "v06/pitfall01.jpg"
        pause 1.0
        "v06/pitfall02.jpg"
        pause 1.0
        repeat

    image pitfallclip02:
        "v06/pitfall01.jpg"
        pause 1.0
        "v06/pitfall02.jpg"
        pause 1.0
        repeat

    transform pitfallpos01:
        xpos 40
        ypos 535
    
    transform pitfallpos02:
        xpos 350
        ypos 535
            
    transform pitfallpos03:
        xpos 1320
        ypos 535

    transform pitfallpos04:
        xpos 450
        ypos 500

    transform pitfallpos05:
        xpos 1320
        ypos 525

    transform pitfallpos06:
        xpos 1820
        ypos 535

    transform pitfallpos07:
        xpos 550
        ypos 450

    transform pitfallpos08:
        xpos 600
        ypos 525
    
    image mckinky01slow:
        "v08/mckinky11.png" with fastdissolve
        pause 0.4
        "v08/mckinky12.png" with fastdissolve
        pause 0.4
        repeat
 
    image mckinky01fast:
        "v08/mckinky11.png" with fastdissolve
        pause 0.3
        "v08/mckinky12.png" with fastdissolve
        pause 0.3
        repeat

    image mcwank01slow:
        "Bar/mcpouch08.png" with fastdissolve
        pause 0.4
        "Bar/mcpouch09.png" with fastdissolve
        pause 0.4
        repeat
        
    image mcwank01fast:
        "Bar/mcpouch08.png" with fastdissolve
        pause 0.3
        "Bar/mcpouch09.png" with fastdissolve
        pause 0.3
        repeat

    transform flexayla:
        "Gym/mcflexmaxayla05.png" with fastdissolve
        pause 0.3
        "Gym/mcflexmaxayla06.png" with fastdissolve
        pause 0.5
        repeat

    transform flexlena:
        "Gym/mcflexmaxlena05.png" with fastdissolve
        pause 0.3
        "Gym/mcflexmaxlena06.png" with fastdissolve
        pause 0.5
        repeat
    transform flexruby:
        "Gym/mcflexmaxruby05.png" with fastdissolve
        pause 0.3
        "Gym/mcflexmaxruby06.png" with fastdissolve
        pause 0.5
        repeat

    transform flexnancy:
        "Gym/mcflexmaxnancy05.png" with fastdissolve
        pause 0.3
        "Gym/mcflexmaxnancy06.png" with fastdissolve
        pause 0.5
        repeat
    transform flexmarnie:
        "Gym/mcflexmaxmarnie05.png" with fastdissolve
        pause 0.3
        "Gym/mcflexmaxmarnie06.png" with fastdissolve
        pause 0.5
        repeat
    
    transform dreammarniegym01:
        "Gym/lockermarnietit02.jpg" with fastdissolve
        pause 0.3
        "Gym/lockermarnietit03.jpg" with fastdissolve
        pause 0.5
        repeat
        
    transform dreammarniegym02:
        "Gym/lockermarniefuck01.jpg" with fastdissolve
        pause 0.3
        "Gym/lockermarniefuck02.jpg" with fastdissolve
        pause 0.5
        repeat

    transform dreamnancygym:
        "Gym/lockernancyfuck01.jpg" with fastdissolve
        pause 0.3
        "Gym/lockernancyfuck02.jpg" with fastdissolve
        pause 0.5
        repeat
        
    transform dreamlenagym:
        "Gym/lockerlena02b.jpg" with fastdissolve
        pause 0.3
        "Gym/lockerlena02a.jpg" with fastdissolve
        pause 0.5
        repeat

    transform dreamaylagym:
        "Gym/lockeraylafuck02.jpg" with fastdissolve
        pause 0.3
        "Gym/lockeraylafuck03.jpg" with fastdissolve
        pause 0.5
        repeat

    transform dreamrubygym:
        "Gym/lockerrubyfuck01a.jpg" with fastdissolve
        pause 0.3
        "Gym/lockerrubyfuck01b.jpg" with fastdissolve
        pause 0.5
        repeat

    transform dreamrubygym02:
        "Gym/lockerrubyfuck01a.jpg" with fastdissolve
        pause 0.4
        "Gym/lockerrubyfuck01b.jpg" with fastdissolve
        pause 0.6
        repeat

    image kohn01:
        "Explore02/cohen01.png" with fastdissolve
        pause 0.3
        "Explore02/cohen02.png" with fastdissolve
        pause 0.3
        "Explore02/cohen03.png" with fastdissolve
        pause 0.3
        "Explore02/cohen04.png" with fastdissolve
        pause 0.3
        "Explore02/cohen01.png" with fastdissolve
        pause 1

    image kohn02:
        "Explore02/cohen05.png" with fastdissolve
        pause 0.3
        "Explore02/cohen06.png" with fastdissolve
        pause 0.3
        "Explore02/cohen07.png" with fastdissolve
        pause 0.3
        "Explore02/cohen08.png" with fastdissolve
        pause 0.3
        "Explore02/cohen06.png" with fastdissolve
        pause 0.3
        "Explore02/cohen05.png" with fastdissolve
        pause 1

    image kohn03:
        "Explore02/cohen09.png" with fastdissolve
        pause 0.3
        "Explore02/cohen10.png" with fastdissolve
        pause 0.3
        "Explore02/cohen11.png" with fastdissolve
        pause 0.3
        "Explore02/cohen12.png" with fastdissolve
        pause 0.3
        "Explore02/cohen10.png" with fastdissolve
        pause 0.3
        "Explore02/cohen11.png" with fastdissolve
        pause 0.3
        "Explore02/cohen12.png" with fastdissolve
        pause 0.3
        "Explore02/cohen10.png" with fastdissolve
        pause 0.3
        "Explore02/cohen09.png" with fastdissolve
        pause 1

    screen injury():
        zorder 97
        if mcinjured == True:
            add "Icons/mcinjuredicon.png"

    screen nightwatch():
        zorder 96
        if mcwatch == True:
            add "Icons/mcwatch.png"

    screen mcstats():
        add "Icons/mcsidestats.png"
        button:
            xpos .00
            ypos .04
            xysize(35, 140)        
            action ui.callsinnewcontext("PlayerInterface")

    transform Line01:
        xpos 1280
        ypos 500
    transform Line02:
        xpos 1280
        ypos 540
    transform Line03:
        xpos 1280
        ypos 580
    transform Line04:
        xpos 1280
        ypos 620
    transform Line05:
        xpos 1280
        ypos 660
    transform Line06:
        xpos 1280
        ypos 700
    transform Line07:
        xpos 1280
        ypos 740
    transform Line08:
        xpos 1280
        ypos 780
    transform Line09:
        xpos 1280
        ypos 820
    transform Line10:
        xpos 1280
        ypos 920

    transform duelmc:
        xpos -910
        ypos -600
        linear 3.0 zoom 2.0 xoffset -1920 yoffset -600
    transform duelbounty:
        xpos -910
        ypos -600
        linear 3.0 zoom 2.0 xoffset -1920 yoffset -600

    transform posstrength:
        xpos 1500
        ypos 187
    transform posfirearms:
        xpos 1500
        ypos 231
    transform poscombat:
        xpos 1500
        ypos 275
    transform poslust:
        xpos 1500
        ypos 368
    transform poscharacterfaction:
        xpos 1420
        ypos 60
    transform posnickname:
        xpos 1000
        ypos 60

    transform posfaction:
        xpos 1750
        ypos 100
    transform posfaction02:
        xpos 1820
        ypos 100

    transform postotal:
        xpos 1400
        ypos 100
    transform postrumpf01:
        xpos 1650
        ypos 454
    transform postrumpf02:
        xpos 1650
        ypos 404
    transform postrumpf03:
        xpos 1650
        ypos 354
    transform posmc01:
        xpos 1500
        ypos 454
    transform posmc02:
        xpos 1500
        ypos 404
    transform posmc03:
        xpos 1500
        ypos 354
    transform posmc04:
        xpos 1500
        ypos 304

    transform tips:
        xpos 400
        ypos 100

    transform sinaway:
        xpos 400 ypos -300
        linear 4 ypos -1000

    transform creepygem:
        xpos 800 ypos 800

    transform aliensshoot01:
        xpos 1000 ypos -180

    transform alienshipmove:
        xpos 0 ypos -800
        linear 2 ypos -300

    transform alienshipmoveout:
        xpos 0 ypos -300
        linear 2 ypos -1000

    transform posnewfaction:
        xpos 1920 ypos 300
        linear .5 xpos 1295

    transform poshareminterface:
        xpos 1920 ypos 20
        linear .5 xpos 1295

    transform poshareminterface02:
        xpos 1295
        ypos 20

    transform pospubichairs:
        xpos 1400
        ypos 730
    
    transform posdarts:
        xpos 200
        ypos 490

    transform poscamels:
        xpos 200
        ypos 250

    transform posinventorystones:
        xpos 200
        ypos 970

    transform posinventorygems:
        xpos 400
        ypos 970

    transform posbouquets:
        xpos 200
        ypos 730
    
    transform pospendulums:
        xpos 1000
        ypos 250
    
    transform posharem01:
        xpos 1320
        ypos 80

    transform posharem02:
        xpos 1320
        ypos 240

    transform posharem03:
        xpos 1320
        ypos 400

    transform posharem04:
        xpos 1320
        ypos 560

    transform posharem05:
        xpos 1320
        ypos 720

    transform posharem06:
        xpos 1320
        ypos 880

    transform posframe:
        xpos 1000
        ypos 100

    transform posname:
        xpos 1350
        ypos 100

    transform mcposname:
        xpos 150
        ypos 90

    transform mcposstrength:
        xpos 150
        ypos 182
    transform mcposfirearms:
        xpos 150
        ypos 226
    transform mcposcombat:
        xpos 150
        ypos 270
    transform mcposmechanics:
        xpos 150
        ypos 314
    transform mcposfrench:
        xpos 150
        ypos 358
    transform mcposbabies:
        xpos 120
        ypos 850
    transform mcposbabies02:
        xpos 100
        ypos 800
    transform posbabies:
        xpos 1700
        ypos 360
    transform posbabies02:
        xpos 1680
        ypos 310

    transform posmcstats:
        xpos 80
        ypos 600

    transform mcposdeep:
        xpos 110
        ypos 480
    transform mcpostrumpster:
        xpos 230
        ypos 480
    transform mcpossierra:
        xpos 350
        ypos 480
    transform mcposwarrior:
        xpos 470
        ypos 480
    transform mcposchurch:
        xpos 590
        ypos 480

    transform poslustam:
        xpos 100
        ypos 200
    transform posbabyam:
        xpos 150
        ypos 100
    transform poslustan:
        xpos 270
        ypos 200
    transform posbabyan:
        xpos 320
        ypos 100
    transform poslustay:
        xpos 424
        ypos 200
    transform posbabyay:
        xpos 474
        ypos 100
    transform poslustba:
        xpos 570
        ypos 200
    transform posbabyba:
        xpos 620
        ypos 100
    transform poslustbe:
        xpos 100
        ypos 368
    transform poslustcl:
        xpos 270
        ypos 368
    transform poslustcy:
        xpos 424
        ypos 368
    transform poslustde:
        xpos 570
        ypos 368
    transform poslustgw:
        xpos 100
        ypos 537
    transform posbabygw:
        xpos 150
        ypos 437
    transform poslustla:
        xpos 270
        ypos 537
    transform posbabyla:
        xpos 320
        ypos 437
    transform poslustle:
        xpos 424
        ypos 537
    transform poslustma:
        xpos 570
        ypos 537
    transform poslustmi:
        xpos 100
        ypos 704
    transform posbabymi:
        xpos 170
        ypos 604
    transform poslustpe:
        xpos 270
        ypos 704
    transform poslustra:
        xpos 424
        ypos 704
    transform poslustru:
        xpos 570
        ypos 704
    transform poslustsu:
        xpos 100
        ypos 880
    transform poslustta:
        xpos 270
        ypos 880
    transform poslustza:
        xpos 100
        ypos 200
    transform posbabyza:
        xpos 150
        ypos 100
    transform poslustwi:
        xpos 270
        ypos 200
    transform poslustmo:
        xpos 424
        ypos 200
    transform posbabymo:
        xpos 474
        ypos 100
    transform poslustiv:
        xpos 570
        ypos 200
    transform poslustme:
        xpos 100
        ypos 368
    transform poslustto:
        xpos 270
        ypos 368
    transform posbabyto:
        xpos 320
        ypos 268
    transform posbabytocount:
        xpos 350
        ypos 268
    transform poslustwe:
        xpos 424
        ypos 368
    transform poslustkg:
        xpos 570
        ypos 368
    transform poslustsy:
        xpos 100
        ypos 537
    transform poslusthe:
        xpos 270
        ypos 537
    transform poslustkr:
        xpos 424
        ypos 537
    transform poslustqu:
        xpos 570
        ypos 537

    transform pospatreon:
        xpos 1500
        ypos 300

    transform posupkeep:
        xpos 1920 ypos 160
        linear .5 xpos 1550
    transform posmission:
        xpos 1920 ypos 300
        linear .5 xpos 1515
    transform posmission2:
        xpos 1515 ypos 300
    transform poswave:
        xpos 1200 ypos 200
        linear 2.0 xpos 500

    transform posdiceroll:
        xpos 1560 ypos 330

    transform danceright:
        xpos 1920 ypos 80
        linear .5 xpos 1000
    transform dancerighta:
        xpos 1920 ypos 130
        linear .5 xpos 1000
    transform danceleft:
        xpos -900 ypos 0
        linear .5 xpos 100
    transform dancerightb:
        xpos 1000 ypos 80
    transform dancerightba:
        xpos 1000 ypos 130
    transform dancerightc:
        xpos 1920 ypos 0
        linear .5 xpos 1000
    transform dancerightca:
        xpos 1000 ypos 0
    transform dancerightda:
        xpos 800 ypos 0

    transform plus:
        xpos 1920 ypos 300
        linear .5 xpos 1600
        pause 2

    transform minus:
        xpos 1920 ypos 600
        linear .5 xpos 1600
        pause 2

    transform posskill:
        xpos 1920 ypos 300
        linear .5 xpos 1515
        pause 2

    transform injured:
        xpos 1920 ypos 300
        linear .5 xpos 1700
        pause 2

    transform camelleft:
        xpos 750
        ypos 400

    transform camelright:
        xpos 1600
        ypos 450

    transform cameldeadleft:
        xpos 700
        ypos 550

    transform cameldeadright:
        xpos 1600
        ypos 590

    transform approachleft:
        xpos 50
        ypos 800

    transform approachright:
        xpos 1600
        ypos 800

    transform PrisonerPosition:
        xpos 1880
        ypos 440

    transform ChurchPosition:
        xpos 1820
        ypos 635

    transform JakePlusPosition:
        xpos 1880
        ypos 405

    transform JakeMinusPosition:
        xpos 1880
        ypos 700

    transform BabyPosition:
        xpos 1780
        ypos 420

    transform StonePosition:
        xpos 1805
        ypos 697
    transform MoneyPosition:
        xpos 90
        ypos 8
    transform MoneyPositionb:
        xpos 40
        ypos 0

    transform StrengthPosition:
        xpos 60
        ypos 65

    transform stat:
        xalign 0.5 yalign 0.1
        zoom 0.5
        linear 2.0 zoom 1.0
        pause 4
        
    transform barleft:
        xpos 100
        ypos 15

    transform barleft02:
        xpos 100
        ypos 100

    transform barright:
        xpos 1738
        ypos 15

    transform barright02:
        xpos 1738
        ypos 100
    
    define midright = Position(xpos=0.7)
    define midleft = Position(xpos=0.3)
    define farright = Position(xpos=0.8)
    define farleft = Position(xpos=0.2)
    define farleft02 = Position(xpos=0.1)
    define farleft03 = Position(xpos=0.05)
    define centerleft = Position(xpos=0.4)
    define centerright = Position(xpos=0.6)
    define farright02 = Position(xpos=0.7)
    define farright03 = Position(xpos=0.9)

    screen screenfightwhbase:
        add "Explore/mcbar.png" at barleft
        add "v10/iconguardshoot01.png" at barright
        add "v10/iconguardshoot02.png" at barright02
        bar value StaticValue(whmc_health, 2.0):
            xalign 0.15 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/rightbar.png", 0, 0)
            right_bar Frame("Bar/rightbarb.png", 0, 0)
        bar value StaticValue(whguard02_health, 2.0):
            xalign 0.85 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/leftbar.png", 0, 0)
            right_bar Frame("Bar/leftbarb.png", 0, 0)    
        bar value StaticValue(whguard01_health, 2.0):
            xalign 0.85 yalign 0.12
            xmaximum 400 
            left_bar Frame("Bar/leftbar.png", 0, 0)
            right_bar Frame("Bar/leftbarb.png", 0, 0)    

    screen screenfightwhpenny:
        add "v10/iconpennyshoot.png" at barleft02
        bar value StaticValue(whpenny_health, 2.0):
            xalign 0.15 yalign 0.12
            xmaximum 400 
            left_bar Frame("Bar/rightbar.png", 0, 0)
            right_bar Frame("Bar/rightbarb.png", 0, 0)
    screen screenfightwhbella:
        add "v10/iconbellashoot.png" at barleft02
        bar value StaticValue(whbella_health, 2.0):
            xalign 0.15 yalign 0.12
            xmaximum 400 
            left_bar Frame("Bar/rightbar.png", 0, 0)
            right_bar Frame("Bar/rightbarb.png", 0, 0)
    screen screenfightwhwidow:
        add "v10/iconwidowshoot.png" at barleft02
        bar value StaticValue(whwidow_health, 2.0):
            xalign 0.15 yalign 0.12
            xmaximum 400 
            left_bar Frame("Bar/rightbar.png", 0, 0)
            right_bar Frame("Bar/rightbarb.png", 0, 0)

    screen screenfightmcivanka:
        add "Explore/mcbar.png" at barleft
        add "v10/ivankafightsprite.png" at barright
        
        bar value StaticValue(mc_health, 2.0):
            xalign 0.15 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/rightbar.png", 0, 0)
            right_bar Frame("Bar/rightbarb.png", 0, 0)
            
        bar value StaticValue(ivanka_health, 2.0):
            xalign 0.85 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/leftbar.png", 0, 0)
            right_bar Frame("Bar/leftbarb.png", 0, 0)    

    screen screenfightmcmelania:
        add "Explore/mcbar.png" at barleft
        add "v10/melaniafightsprite.png" at barright
        
        bar value StaticValue(mc_health, 2.0):
            xalign 0.15 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/rightbar.png", 0, 0)
            right_bar Frame("Bar/rightbarb.png", 0, 0)
            
        bar value StaticValue(melania_health, 2.0):
            xalign 0.85 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/leftbar.png", 0, 0)
            right_bar Frame("Bar/leftbarb.png", 0, 0)    

    screen screenfightmcopala:
        add "Explore/mcbar.png" at barleft
        add "Explore/opalabar.png" at barright
        
        bar value StaticValue(mc_health, 2.0):
            xalign 0.15 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/rightbar.png", 0, 0)
            right_bar Frame("Bar/rightbarb.png", 0, 0)
            
        bar value StaticValue(opala_health, 2.0):
            xalign 0.85 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/leftbar.png", 0, 0)
            right_bar Frame("Bar/leftbarb.png", 0, 0)    

    screen screenfightmcinquis:
        add "Explore/mcbar.png" at barleft
        add "Explore/inquisitorbar.png" at barright
        
        bar value StaticValue(mc_health, 2.0):
            xalign 0.15 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/rightbar.png", 0, 0)
            right_bar Frame("Bar/rightbarb.png", 0, 0)
            
        bar value StaticValue(inquis_health, 2.0):
            xalign 0.85 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/leftbar.png", 0, 0)
            right_bar Frame("Bar/leftbarb.png", 0, 0)    

    screen screenfightmcgator:
        add "Explore/mcbar.png" at barleft
        add "v06/gatorbar.png" at barright
        
        bar value StaticValue(mc_health, 2.0):
            xalign 0.15 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/rightbar.png", 0, 0)
            right_bar Frame("Bar/rightbarb.png", 0, 0)
            

        bar value StaticValue(gator_health, 2.0):
            xalign 0.85 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/leftbar.png", 0, 0)
            right_bar Frame("Bar/leftbarb.png", 0, 0)    

    screen screenfightmcqanon:
        add "Explore/mcbar.png" at barleft
        add "v072/qbar.png" at barright
        
        bar value StaticValue(mc_health, 3.0):
            xalign 0.15 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/rightbar.png", 0, 0)
            right_bar Frame("Bar/rightbarb.png", 0, 0)
            

        bar value StaticValue(qanon_health, 3.0):
            xalign 0.85 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/leftbar.png", 0, 0)
            right_bar Frame("Bar/leftbarb.png", 0, 0)    

    screen screenfightmcevil:
        add "Explore/mcbar.png" at barleft
        add "Explore/evilbar.png" at barright
        
        bar value StaticValue(mc_health, 2.0):
            xalign 0.15 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/rightbar.png", 0, 0)
            right_bar Frame("Bar/rightbarb.png", 0, 0)
            

        bar value StaticValue(evil_health, 2.0):
            xalign 0.85 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/leftbar.png", 0, 0)
            right_bar Frame("Bar/leftbarb.png", 0, 0)    

    screen screenfightavengers:
        add "v09/avengersbar.png" at barleft
        add "v09/hannitybar.png" at barright
        
        bar value StaticValue(avengers_health, 3.0):
            xalign 0.15 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/rightbar.png", 0, 0)
            right_bar Frame("Bar/rightbarb.png", 0, 0)
            

        bar value StaticValue(hannity_health, 3.0):
            xalign 0.85 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/leftbar.png", 0, 0)
            right_bar Frame("Bar/leftbarb.png", 0, 0)    

    screen screenfightamyayla:
        add "Bar/amybar.png" at barleft
        add "Bar/aylabar.png" at barright
        
        bar value StaticValue(amy_health, 5.0):
            xalign 0.15 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/rightbar.png", 0, 0)
            right_bar Frame("Bar/rightbarb.png", 0, 0)
            

        bar value StaticValue(ayla_health, 5.0):
            xalign 0.85 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/leftbar.png", 0, 0)
            right_bar Frame("Bar/leftbarb.png", 0, 0)    
            
    screen screenfightlenaruby:
        add "Bar/lenabar.png" at barleft
        add "Bar/rubybar.png" at barright
        
        bar value StaticValue(lena_health, 5.0):
            xalign 0.15 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/rightbar.png", 0, 0)
            right_bar Frame("Bar/rightbarb.png", 0, 0)
            

        bar value StaticValue(ruby_health, 5.0):
            xalign 0.85 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/leftbar.png", 0, 0)
            right_bar Frame("Bar/leftbarb.png", 0, 0)    

    screen screenfightmichikosuki:
        add "Bar/michikobar.png" at barleft
        add "Bar/sukibar.png" at barright
        
        bar value StaticValue(michiko_health, 5.0):
            xalign 0.15 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/rightbar.png", 0, 0)
            right_bar Frame("Bar/rightbarb.png", 0, 0)
            

        bar value StaticValue(suki_health, 5.0):
            xalign 0.85 yalign 0.03
            xmaximum 400 
            left_bar Frame("Bar/leftbar.png", 0, 0)
            right_bar Frame("Bar/leftbarb.png", 0, 0)    

    screen allicons():
        zorder 98
        add "Icons/allicons.png"

    style periodWeek is statsCommon:
        size 20
        color "#1c73ff"

    screen calendar():
        zorder 99        
        add "Icons/dollar.png" at MoneyPositionb
        text "{font=Gui/goodtimes.ttf}[money]{/font}" color "#2f4f8a" size 20 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at MoneyPosition
        add ("Icons/{}day.png".format( [ "sun", "mon", "tues", "wednes", "thurs", "fri", "satur"][day%7] )) at DayPosition
        text ( "{}".format( [ None, "Morning", "Afternoon", "Evening", "Night"][period] ) ) style "periodWeek" xpos 1532 yalign 0.01
        text ( "Week {:02}".format( week ) ) style "periodWeek" xalign 0.75 yalign 0.01

    transform PeriodPosition:
        xpos 1532
        yalign 0.01
    transform WeekPosition:
        xalign .75
        yalign 0.01
    transform DayPosition:
        xalign .79
        yalign 0.00
    transform streetfight01:
        xalign 0.4 yalign 0.4
        zoom 0.5
        linear 0.5 zoom 1.0
        pause 1
    transform streetfight02:
        xalign 0.5 yalign 0.5
        zoom 0.5
        linear 0.5 zoom 1.0
        pause 1
    transform streetfight03:
        xalign 0.6 yalign 0.6
        zoom 0.5
        linear 0.5 zoom 1.0
        pause 1

    transform haremsheetpos:
        xalign 0.05
        yalign 0.05


    image bar04 blurred = im.Blur("Bar/bar04.jpg", 1.5)
    image medbay02 blurred = im.Blur("medbay/medbay02.jpg", 1.5)
    image medbay03 blurred = im.Blur("medbay/medbay03.jpg", 1.5)
    image medbay04 blurred = im.Blur("medbay/medbay04.jpg", 1.5)
    image medbay05 blurred = im.Blur("medbay/medbay05.jpg", 1.5)
    image medbay06 blurred = im.Blur("medbay/medbay06.jpg", 1.5)
    image medbay07 blurred = im.Blur("medbay/medbay07.jpg", 1.5)
    image widowlair02 blurred = im.Blur("Explore/widowlair02.jpg", 1.5)
    image widowlair03 blurred = im.Blur("Explore/widowlair03.jpg", 1.5)
    image widowlair04 blurred = im.Blur("Explore/widowlair04.jpg", 1.5)
    image widowlair05 blurred = im.Blur("Explore/widowlair05.jpg", 1.5)
    image widowlair07 blurred = im.Blur("Explore/widowlair07.jpg", 1.5)
    image oasis01 blurred = im.Blur("oasis/oasis01.jpg", 1.5)
    image oasiscamelidle blurred = im.Blur("oasis/oasiscamelidle.png", 1.5)
    image dojo01 blurred = im.Blur("Gym/dojo01.jpg", 1.5)
    image foodunit01 blurred = im.Blur("Science/foodunit01.jpg", 1.5)
    image lab02 blurred = im.Blur("Science/lab02.jpg", 1.5)
    image pool04 blurred = im.Blur("Pool/pool04.jpg", 1.5)
    image pool05 blurred = im.Blur("Pool/pool05.jpg", 1.5)
    image strip02 blurred = im.Blur("Stripping/strip02.jpg", 1.5)
    image church03 blurred = im.Blur("Church/church03.jpg", 1.5)

    image locker03 blurred = im.Blur("Gym/locker03.jpg", 1.5)
    image gym04squirt blurred = im.Blur("Gym/gym04squirt.jpg", 1.5)

    image prisonfuck01 blurred = im.Blur("Command/prisonfuck01.jpg", 1.2)

    image market02 blurred = im.Blur("deserttown/market02.jpg", 1.2)
    image widowroom02 blurred = im.Blur("Explore/widowroom02.jpg", 1.2)
    image widowroom03 blurred = im.Blur("Explore/widowroom03.jpg", 1.2)
    image widowroom08 blurred = im.Blur("Explore/widowroom08.jpg", 1.2)
    image widowroom09 blurred = im.Blur("Explore/widowroom09.jpg", 1.2)

    image bedroom02 blurred = im.Blur("Bedroom/bedroom02.jpg", 1.2)
    image fridayparty02 blurred = im.Blur("Dancing/fridayparty02.jpg", 1.2)
    image workshop03 blurred = im.Blur("Workshop/workshop03.jpg", 1.2)
    image gwendebrabackground blurred = im.Blur("Science/gwendebrabackground.jpg", 1.2)
    image bedroom01 blurred = im.Blur("Bedroom/bedroom01.jpg", 1.2)
    image bedroom06 blurred = im.Blur("Bedroom/bedroom06.jpg", 1.2)
    image bedroom05 blurred = im.Blur("Bedroom/bedroom05.jpg", 1.2)
    image bedroom03 blurred = im.Blur("Bedroom/bedroom03.jpg", 1.2)
    image bedroom03b blurred = im.Blur("Bedroom/bedroom03b.jpg", 1.2)
    image bedroom07 blurred = im.Blur("Bedroom/bedroom07.jpg", 1.2)
    image bedroom08 blurred = im.Blur("Bedroom/bedroom08.jpg", 1.2)
    image bedroom09 blurred = im.Blur("Bedroom/bedroom09.jpg", 1.2)
    image bedroom10 blurred = im.Blur("Bedroom/bedroom10.jpg", 1.2)
    image bedroom11 blurred = im.Blur("Bedroom/bedroom11.jpg", 1.2)
    image bedroom12 blurred = im.Blur("Bedroom/bedroom12.jpg", 1.2)
    image bedroom13 blurred = im.Blur("Bedroom/bedroom13.jpg", 1.2)
    image bedroom14 blurred = im.Blur("Bedroom/bedroom14.jpg", 1.2)
    image bedroom15 blurred = im.Blur("Bedroom/bedroom15.jpg", 1.2)
    image bedroom16 blurred = im.Blur("Bedroom/bedroom16.jpg", 1.2)
    image bedroom17 blurred = im.Blur("Bedroom/bedroom17.jpg", 1.2)
    image bedroom18 blurred = im.Blur("Bedroom/bedroom18.jpg", 1.2)
    image bedroom19 blurred = im.Blur("Bedroom/bedroom19.jpg", 1.2)
    image bedroom20 blurred = im.Blur("Bedroom/bedroom20.jpg", 1.2)
    image bedroom21 blurred = im.Blur("Bedroom/bedroom21.jpg", 1.2)
    image bedroom22 blurred = im.Blur("Bedroom/bedroom22.jpg", 1.2)
    image bedroom23 blurred = im.Blur("Bedroom/bedroom23.jpg", 1.2)
    image bedroom24 blurred = im.Blur("Bedroom/bedroom24.jpg", 1.2)
    image bedroom25 blurred = im.Blur("Bedroom/bedroom25.jpg", 1.2)
    image bedroom26 blurred = im.Blur("Bedroom/bedroom26.jpg", 1.2)
    image bedroom27 blurred = im.Blur("Bedroom/bedroom27.jpg", 1.2)
    image bedroom28 blurred = im.Blur("Bedroom/bedroom28.jpg", 1.2)
    image bedroom29 blurred = im.Blur("Bedroom/bedroom29.jpg", 1.2)
    image bedroom30 blurred = im.Blur("Bedroom/bedroom30.jpg", 1.2)
    image bedroom31 blurred = im.Blur("Bedroom/bedroom31.jpg", 1.2)
    image bedroom32 blurred = im.Blur("Bedroom/bedroom32.jpg", 1.2)
    image bedroom33 blurred = im.Blur("Bedroom/bedroom33.jpg", 1.2)
    image bedroom34 blurred = im.Blur("Bedroom/bedroom34.jpg", 1.2)
    image bedroom35 blurred = im.Blur("Bedroom/bedroom35.jpg", 1.2)
    image bedroom36 blurred = im.Blur("Bedroom/bedroom36.jpg", 1.2)
    image bedroom37 blurred = im.Blur("Bedroom/bedroom37.jpg", 1.2)
    image bedroom38 blurred = im.Blur("Bedroom/bedroom38.jpg", 1.2)
    image bedroom39 blurred = im.Blur("Bedroom/bedroom39.jpg", 1.2)
    image bedroom40 blurred = im.Blur("Bedroom/bedroom40.jpg", 1.2)
    image bedroom41 blurred = im.Blur("Bedroom/bedroom41.jpg", 1.2)
    image bedroom42 blurred = im.Blur("Bedroom/bedroom42.jpg", 1.2)
    image bedroom43 blurred = im.Blur("Bedroom/bedroom43.jpg", 1.2)
    image bedroom44 blurred = im.Blur("Bedroom/bedroom44.jpg", 1.2)
    image bedroom45 blurred = im.Blur("Bedroom/bedroom45.jpg", 1.2)
    image bedroom46 blurred = im.Blur("Bedroom/bedroom46.jpg", 1.2)
    image bedroom47 blurred = im.Blur("Bedroom/bedroom47.jpg", 1.2)
    image bedroom48 blurred = im.Blur("Bedroom/bedroom48.jpg", 1.2)
    image bedroom49 blurred = im.Blur("Bedroom/bedroom49.jpg", 1.2)
    image bedroom50 blurred = im.Blur("v061/bedroom50.jpg", 1.2)
    image bedroom51 blurred = im.Blur("v061/bedroom51.jpg", 1.2)
    image bedroom52 blurred = im.Blur("v061/bedroom52.jpg", 1.2)
    image michikofootjobcumbackground blurred = im.Blur("Stripping/michikofootjobcumbackground.jpg", 1.2)
    image studio03b blurred = im.Blur("Bar/studio03b.jpg", 1.5)
    image studio04b blurred = im.Blur("Bar/studio04b.jpg", 1.5)
    image canyon01 blurred = im.Blur("Dates/canyon01.jpg", 1.5)
    image canyon02 blurred = im.Blur("Dates/canyon02.jpg", 1.5)
    image canyon03 blurred = im.Blur("Dates/canyon03.jpg", 1.5)
    image widowroom01 blurred = im.Blur("Explore/widowroom01.jpg", 1.5)
    image widowroom03 blurred = im.Blur("Explore/widowroom03.jpg", 1.5)
    image widowroom04 blurred = im.Blur("Explore/widowroom04.jpg", 1.5)
    image widowroom05 blurred = im.Blur("Explore/widowroom05.jpg", 1.5)
    image widowroom07 blurred = im.Blur("Explore/widowroom07.jpg", 1.5)
    image widowroom11 blurred = im.Blur("Explore/widowroom11.jpg", 1.5)
    image widowroom13 blurred = im.Blur("Explore/widowroom13.jpg", 1.5)
    image bossroom01 blurred = im.Blur("Explore/bossroom01.jpg", 1.5)
    image bossroom02 blurred = im.Blur("Explore/bossroom02.jpg", 1.5)
    image bossroom03 blurred = im.Blur("Explore/bossroom03.jpg", 1.5)
    image bossroom04 blurred = im.Blur("Explore/bossroom04.jpg", 1.5)
    image bossroom05 blurred = im.Blur("Explore/bossroom05.jpg", 1.5)
    image bossroom06 blurred = im.Blur("Explore/bossroom06.jpg", 1.5)
    image bossroom07 blurred = im.Blur("Explore/bossroom07.jpg", 1.5)
    image bossroom08 blurred = im.Blur("Explore/bossroom08.jpg", 1.5)
    image ivankanalscene blurred = im.Blur("Explore/ivankanalscene.jpg", 1.5)
    image templesex01 blurred = im.Blur("Explore/templesex01.jpg", 1.5)
    image templesex02 blurred = im.Blur("Explore/templesex02.jpg", 1.5)
    image templesex03 blurred = im.Blur("Explore/templesex03.jpg", 1.5)
    image classdream02 blurred = im.Blur("School/classdream02.jpg", 1.5)
    image evillairbottom01 blurred = im.Blur("Explore/evillairbottom01.jpg", 1.5)
    image ivankadeskscene blurred = im.Blur("Explore/ivankadeskscene.jpg", 1.5)
    image oracle01 blurred = im.Blur("Explore/oracle01.jpg", 1.5)
    image oracle02 blurred = im.Blur("Explore/oracle02.jpg", 1.5)
    image oracle03 blurred = im.Blur("Explore/oracle03.jpg", 1.5)
    image oracle04 blurred = im.Blur("Explore/oracle04.jpg", 1.5)
    image pool03 blurred = im.Blur("Pool/pool03.jpg", 1.5)
    image pool06 blurred = im.Blur("Pool/pool06.jpg", 1.5)
    image cloister20 blurred = im.Blur("v06/cloister20.jpg", 1.5)
    image cloister22 blurred = im.Blur("v06/cloister22.jpg", 1.5)
    image cloister21 blurred = im.Blur("v06/cloister21.jpg", 1.5)
    image cloister23 blurred = im.Blur("v06/cloister23.jpg", 1.5)
    image cloister24 blurred = im.Blur("v06/cloister24.jpg", 1.5)
    image cloister25 blurred = im.Blur("v06/cloister25.jpg", 1.5)
    image cloister26 blurred = im.Blur("v06/cloister26.jpg", 1.5)
    image cloister27 blurred = im.Blur("v06/cloister27.jpg", 1.5)
    image cloister28 blurred = im.Blur("v06/cloister28.jpg", 1.5)
    image cloister29 blurred = im.Blur("v06/cloister29.jpg", 1.5)
    image fbibackground02 blurred = im.Blur("v082/fbibackground02.jpg", 1.5)

    image crater03 blurred = im.Blur("Explore/crater03.jpg", 1.5)
    image crater04 blurred = im.Blur("Explore/crater04.jpg", 1.5)
    image michikoroombed blurred = im.Blur("Dates/michikoroombed.jpg", 1.5)
    image pennytitjobbackground blurred = im.Blur("Stripping/pennytitjobbackground.jpg", 1.5)
    image basementsofiabackground blurred = im.Blur("Explore/basementsofiabackground.jpg", 1.5)
    image junktown01 blurred = im.Blur("Explore02/junktown01.jpg", 1.5)
    image junktown02 blurred = im.Blur("Explore02/junktown02.jpg", 1.5)
    image junktown05 blurred = im.Blur("Explore02/junktown05.jpg", 1.5)
    image junktown06 blurred = im.Blur("Explore02/junktown06.jpg", 1.5)
    image maragogo02 blurred = im.Blur("Explore02/maragogo02.jpg", 1.5)
    image maragogo03 blurred = im.Blur("Explore02/maragogo03.jpg", 1.5)
    image maragogo04 blurred = im.Blur("Explore02/maragogo04.jpg", 1.5)
    image maragogo06 blurred = im.Blur("Explore02/maragogo06.jpg", 1.5)
    image maragogo05 blurred = im.Blur("Explore02/maragogo05.jpg", 1.5)
    image maragogo07 blurred = im.Blur("Explore02/maragogo07.jpg", 1.5)
    image cloister11 blurred = im.Blur("Explore02/cloister11.jpg", 1.5)
    image cloister05 blurred = im.Blur("Explore02/cloister05.jpg", 1.5)
    image cloister06 blurred = im.Blur("Explore02/cloister06.jpg", 1.5)
    image cloister07 blurred = im.Blur("Explore02/cloister07.jpg", 1.5)
    image cloister08 blurred = im.Blur("Explore02/cloister08.jpg", 1.5)
    image mcliftend02 blurred = im.Blur("Gym/mcliftend02.jpg", 1.5)
    image swamphouse01 blurred = im.Blur("v06/swamphouse01.jpg", 1.5)
    image ivankawhitehouse blurred = im.Blur("v07/ivankawhitehouse.jpg", 1.5)
    image kimberlywhitehouse blurred = im.Blur("v07/kimberlywhitehouse.jpg", 1.5)
    image melaniawhitehouse blurred = im.Blur("v07/melaniawhitehouse.jpg", 1.5)
    image diamondlickbackground blurred = im.Blur("v07/diamondlickbackground.jpg", 1.5)
    image diamondsukyubackground01 blurred = im.Blur("v07/diamondsukyubackground01.jpg", 1.5)
    image heathercumbackground01 blurred = im.Blur("v07/heathercumbackground01.jpg", 1.5)
    image heathercumbackground02 blurred = im.Blur("v07/heathercumbackground02.jpg", 1.5)
    image heathercumbackground03 blurred = im.Blur("v07/heathercumbackground03.jpg", 1.5)
    image diamondheatherbackground01 blurred = im.Blur("v07/diamondheatherbackground01.jpg", 1.5)
    image sukyucumbackground blurred = im.Blur("v07/sukyucumbackground.jpg", 1.5)
    image diamondhighbackground blurred = im.Blur("v07/diamondhighbackground.jpg", 1.5)
    image diamondtitcumbackground blurred = im.Blur("v07/diamondtitcumbackground.jpg", 1.5)
    image newaliens01 blurred = im.Blur("v071/newaliens01.jpg", 1.5)
    image clarablowjobbackground blurred = im.Blur("v071/clarablowjobbackground.jpg", 1.5)
    image caravan03 blurred = im.Blur("v071/caravan03.jpg", 1.5)
    image diamondheatherbackground01 blurred = im.Blur("v07/diamondheatherbackground01.jpg", 1.5)
    image studio02b blurred = im.Blur("Bar/studio02b.jpg", 1.5)
    image container01 blurred = im.Blur("v08/container01.jpg", 1.5)
    image container02 blurred = im.Blur("v08/container02.jpg", 1.5)
    image container03 blurred = im.Blur("v09/container03.jpg", 1.5)
    image containerkristafront blurred = im.Blur("v09/containerkristafront.jpg", 1.5)
    image fbibackground02 blurred = im.Blur("v08/fbibackground02.jpg", 1.5)
    image fbibackground03 blurred = im.Blur("v08/fbibackground03.jpg", 1.5)
    image fbibackground04 blurred = im.Blur("v08/fbibackground04.jpg", 1.5)
    image barbarahandjobbackground blurred = im.Blur("v081/barbarahandjobbackground.jpg", 1.5)
    image containerkristatits blurred = im.Blur("v081/containerkristatits.jpg", 1.5)
    image containerkristatitspov blurred = im.Blur("v081/containerkristatitspov.jpg", 1.5)
    image quebec02 blurred = im.Blur("v081/quebec02.jpg", 1.5)
    image quebec08 blurred = im.Blur("v081/quebec08.jpg", 1.5)
    image paulettesexbackground blurred = im.Blur("v081/paulettesexbackground.jpg", 1.5)
    image paulettefuckbackground blurred = im.Blur("v081/paulettefuckbackground.jpg", 1.5)
    image maragogo08 blurred = im.Blur("v082/maragogo08.jpg", 1.5)
    image maragogo09 blurred = im.Blur("v082/maragogo09.jpg", 1.5)
    image maragogo10 blurred = im.Blur("v082/maragogo10.jpg", 1.5)
    image maragogo04b blurred = im.Blur("maragogo04b", 1.5)
    image trumpfwall02 blurred = im.Blur("v09/trumpfwall02.jpg", 1.5)
    image trumpfwall02b blurred = im.Blur("v09/trumpfwall02b.jpg", 1.5)
    image melaniaivankablowbackground blurred = im.Blur("v10/melaniaivankablowbackground.jpg", 1.5)
    image whitehouseentrance blurred = im.Blur("v10/whitehouseentrance.jpg", 1.5)
    image whdoggymelaniabackground blurred = im.Blur("v10/whdoggymelaniabackground.jpg", 1.5)

    image frame = "Bedroom/frame01.png"
        
    image jake01b = im.FactorScale("Characters/jake01.png",0.9)
    image jake02b = im.FactorScale("Characters/jake02.png",0.9)
    image jakeshower03b = im.FactorScale("Gym/jakeshower03.png",0.9)
    image jakeshower01b = im.FactorScale("Gym/jakeshower01.png",0.9)
    image jakeshower02b = im.FactorScale("Gym/jakeshower02.png",0.9)
    image jakeshower04b = im.FactorScale("Gym/jakeshower04.png",0.9)
    image jakeshower05b = im.FactorScale("Gym/jakeshower05.png",0.9)
    image jakeshower06b = im.FactorScale("Gym/jakeshower06.png",0.9)
    image jake03b = im.FactorScale("Characters/jake03.png",0.9)
    image tara01b = im.FactorScale("Medbay/tara01.png",0.95)
    image rachel02b = im.FactorScale("Medbay/rachel02.png",0.95)
    image rachel05b = im.FactorScale("Medbay/rachel05.png",0.95)
    image amy01b = im.FactorScale("Characters/amy01.png",0.95)
    image amy02b = im.FactorScale("Characters/amy02.png",0.95)
    image amy03b = im.FactorScale("Characters/amy03.png",0.95)
    image amy04b = im.FactorScale("Characters/amy04.png",0.95)
    image amy05b = im.FactorScale("Characters/amy05.png",0.95)
    image michiko01b = im.FactorScale("Characters/michiko01.png",0.95)
    image michiko02b = im.FactorScale("Characters/michiko02.png",0.95)
    image bella01b = im.FactorScale("Characters/bella01.png",0.95)
    image bella02b = im.FactorScale("Characters/bella02.png",0.95)
    image beneb = im.FactorScale("Characters/bene.png",0.95)
    image beanb = im.FactorScale("Characters/bean.png",0.95)
    image gwen05b = im.FactorScale("Characters/gwen05.png",0.90)
    image gwen06b = im.FactorScale("Characters/gwen06.png",0.90)
    image bellaout02b = im.FactorScale("Characters/bellaout02.png",0.9)
    image bellaout01b = im.FactorScale("Characters/bellaout01.png",0.9)
    image gwen08b = im.FactorScale("Characters/gwen08.png",0.92)
    image taylor01b = im.FactorScale("Explore02/taylor01.png",0.92)
    image taylor02b = im.FactorScale("Explore02/taylor02.png",0.92)
    image taylor03b = im.FactorScale("Explore02/taylor03.png",0.92)
    image taylor04b = im.FactorScale("Explore02/taylor04.png",0.92)
    image stellaevening01b = im.FactorScale("Explore02/stellaevening01.png",0.92)
    image stellaevening02b = im.FactorScale("Explore02/stellaevening02.png",0.92)

    image francois01b = im.FactorScale("School/francois01.png", 0.95)
    image francois02b = im.FactorScale("School/francois02.png", 0.95)

    image slaver01b = im.FactorScale("deserttown/slaver01.png", 0.95)
    image slaver02b = im.FactorScale("deserttown/slaver02.png", 0.95)
    image slaver03b = im.FactorScale("deserttown/slaver03.png", 0.95)
    image slaver04b = im.FactorScale("deserttown/slaver04.png", 0.95)
    image slavershootb = im.FactorScale("deserttown/slavershoot.png", 0.95)

    image angiedancing01c = im.FactorScale("Dancing/angiedancing01.png", 0.95)
    image angiedancing01bc = im.FactorScale("Dancing/angiedancing01b.png", 0.95)
    image angiedancing02c = im.FactorScale("Dancing/angiedancing02.png", 0.95)
    image angiedancing02bc = im.FactorScale("Dancing/angiedancing02b.png", 0.95)
    image angiedancing03c = im.FactorScale("Dancing/angiedancing03.png", 0.95)
    image angiedancing03bc = im.FactorScale("Dancing/angiedancing03b.png", 0.95)
    image angiedancing04c = im.FactorScale("Dancing/angiedancing04.png", 0.95)
    image angiedancing04bc = im.FactorScale("Dancing/angiedancing04b.png", 0.95)
    image ayladancing01c = im.FactorScale("Dancing/ayladancing01.png", 0.95)
    image ayladancing01bc = im.FactorScale("Dancing/ayladancing01b.png", 0.95)
    image ayladancing02c = im.FactorScale("Dancing/ayladancing02.png", 0.95)
    image ayladancing02bc = im.FactorScale("Dancing/ayladancing02b.png", 0.95)
    image ayladancing03c = im.FactorScale("Dancing/ayladancing03.png", 0.95)
    image ayladancing03bc = im.FactorScale("Dancing/ayladancing03b.png", 0.95)
    image ayladancing04c = im.FactorScale("Dancing/ayladancing04.png", 0.95)
    image ayladancing04bc = im.FactorScale("Dancing/ayladancing04b.png", 0.95)

    image angieschool01b = im.FactorScale("School/angieschool01.png", 0.95)
    image angieschool02b = im.FactorScale("School/angieschool02.png", 0.95)
    image angieschool03b = im.FactorScale("School/angieschool03.png", 0.95)
    image amyschool01b = im.FactorScale("School/amyschool01.png", 0.95)
    image amyschool02b = im.FactorScale("School/amyschool02.png", 0.95)
    image amyschool03b = im.FactorScale("School/amyschool03.png", 0.95)
    image widonancyaftercumb = im.FactorScale("Nancy/widonancyaftercum.png", 0.92)
    image junktown03c = im.FactorScale("Explore02/junktown03.jpg",1.5)
    image maragogo04b = im.FactorScale("Explore02/maragogo04.jpg",1.5)
    image maragogo07b = im.FactorScale("Explore02/maragogo07.jpg",1.5)
    image theresaflogged05b = im.FactorScale("Explore02/theresaflogged05.png",.95)
    image taylorpregnant01b = im.FactorScale("v06/taylorpregnant01.png",0.95)
    image taylorpregnant02b = im.FactorScale("v06/taylorpregnant02.png",0.98)
    image taylorpregnant03b = im.FactorScale("v06/taylorpregnant03.png",0.95)
    image taylorpregnant04b = im.FactorScale("v06/taylorpregnant04.png",0.98)
    image taylorpregnant05b = im.FactorScale("v06/taylorpregnant05.png",0.95)
    image taylorpregnant06b = im.FactorScale("v06/taylorpregnant06.png",0.98)
    image taylorpregnant07b = im.FactorScale("v06/taylorpregnant07.png",0.95)
    image clarablowjobbackgroundzoom = im.FactorScale("v071/clarablowjobbackground.jpg",2)
    image stripclara01b = im.FactorScale("Stripping/stripclara01.png", 0.95)
    image stripclara02b = im.FactorScale("Stripping/stripclara02.png", 0.95)
    image tyrone04b = im.FactorScale("Church/tyrone04.png", 0.95)
    image tyrone05b = im.FactorScale("Church/tyrone05.png", 0.95)
    image tyrone06b = im.FactorScale("Church/tyrone06.png", 0.95)
    image tyrone07b = im.FactorScale("Church/tyrone07.png", 0.95)
    image containerkristatitszoom = im.FactorScale("v081/containerkristatits.jpg", 1.5)
    image barbarawiggle00b = im.FactorScale("v081/barbarawiggle00.png", .9)
    image titiana01b = im.FactorScale("v082/titiana01.png", .95)
    image titiana02b = im.FactorScale("v082/titiana02.png", .95)
    image titiana03b = im.FactorScale("v082/titiana03.png", .95)
    image maragogo04b blurred = im.FactorScale("Explore02/maragogo04.jpg",1.5)
    image trumpfoval01b = im.FactorScale("v10/trumpfoval01.png", 0.95)
    image trumpfoval02b = im.FactorScale("v10/trumpfoval02.png", 0.95)
    image trumpfoval03b = im.FactorScale("v10/trumpfoval03.png", 0.95)
    image trumpfoval04b = im.FactorScale("v10/trumpfoval04.png", 0.95)
    image trumpfoval05b = im.FactorScale("v10/trumpfoval05.png", 0.95)
    image trumpfoval06b = im.FactorScale("v10/trumpfoval06.png", 0.95)
    image trumpfoval07b = im.FactorScale("v10/trumpfoval07.png", 0.95)
    image trumpfoval08b = im.FactorScale("v10/trumpfoval08.png", 0.95)
    image trumpfoval09b = im.FactorScale("v10/trumpfoval09.png", 0.95)
    image trumpfoval10b = im.FactorScale("v10/trumpfoval10.png", 0.95)
    image paulette01b = im.FactorScale("v081/paulette01.png", 0.95)
    image paulette02b = im.FactorScale("v081/paulette02.png", 0.95)
    image paulette03b = im.FactorScale("v081/paulette03.png", 0.95)
    image paulette05b = im.FactorScale("v081/paulette05.png", 0.95)
    image pauletteprecanuck01b = im.FactorScale("v09/pauletteprecanuck01.png", 0.95)
    image paulettecanuck01bb = im.FactorScale("v09/paulettecanuck01b.png", 0.95)
    image paulettecanuck01d = im.FactorScale("v09/paulettecanuck01.png", 0.95)
    image paulettecanuck01cb = im.FactorScale("v09/paulettecanuck01c.png", 0.95)
    image paulettecanuck02b = im.FactorScale("v09/paulettecanuck02.png", 0.95)
    image mcend01b = im.FactorScale("v10/mcend01.png", 0.95)
    image mcend02b = im.FactorScale("v10/mcend02.png", 0.95)
    image mcend03b = im.FactorScale("v10/mcend03.png", 0.95)
    image mcend04b = im.FactorScale("v10/mcend04.png", 0.95)
    image ovaloffice02zoom = im.FactorScale("v10/ovaloffice02.jpg",2)
    image ovaloffice02zoom blurred = im.Blur("v10/ovaloffice02.jpg", 2.0)
    image ovalofficeaftermath blurred = im.Blur("v10/ovalofficeaftermath.jpg", 1.5)
    image whdoggyivankabackground blurred = im.Blur("v10/whdoggyivankabackground.jpg", 1.5)
    image whbothbackground blurred = im.Blur("v10/whbothbackground.jpg", 1.5)
    image whivankacumbackgroundzoom = im.FactorScale("v10/whivankacumbackground.jpg",1.5)
    image whivankacumbackground blurred = im.Blur("v10/whivankacumbackground.jpg", 1.5)
    define fastdissolve = Dissolve(0.2)
    define ultrafastdissolve = Dissolve(0.1)

# The game starts here.

label start:
jump Intro
    
return
