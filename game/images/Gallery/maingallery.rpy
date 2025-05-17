label MainGallery:
stop music
hide screen mcstats
hide screen injury
hide screen calendar
call screen gallerymain
screen gallerymain:
    modal True
    add "Gallery/maingallery.jpg"
    if renpy.seen_image("whitehouse01"):
        add "v10/whitehousegrid.png" xpos 1585 ypos 744
    imagebutton:
        focus_mask True
        idle "Gallery/galleryexit.png"
        hover "Gallery/galleryexit.png"
        action [Hide ("gallerymain"), Show ("calendar"), Show ("injury"), Show ("mcstats"), Return]

    button:
        xpos 110
        ypos 140
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("AmyGallery")]

    button:
        xpos 360
        ypos 140
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("AngieGallery")]

    button:
        xpos 610
        ypos 140
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("AylaGallery")]

    button:
        xpos 860
        ypos 140
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("BarbaraGallery")]

    button:
        xpos 1110
        ypos 140
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("BellaGallery")]

    button:
        xpos 1360
        ypos 140
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("ClaraGallery")]

    button:
        xpos 1610
        ypos 140
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("CyrlGallery")]

    button:
        xpos 110
        ypos 340
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("DebraGallery")]

    button:
        xpos 360
        ypos 340
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("GwenGallery")]

    button:
        xpos 610
        ypos 340
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("LaurieGallery")]

    button:
        xpos 860
        ypos 340
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("LenaGallery")]

    button:
        xpos 1110
        ypos 340
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("MarnieGallery")]

    button:
        xpos 1360
        ypos 340
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("MichikoGallery")]

    button:
        xpos 1610
        ypos 340
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("PennyGallery")]

    button:
        xpos 110
        ypos 540
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("RachelGallery")]

    button:
        xpos 360
        ypos 540
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("RubyGallery")]

    button:
        xpos 610
        ypos 540
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("SukiGallery")]

    button:
        xpos 860
        ypos 540
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("TaraGallery")]

    button:
        xpos 1110
        ypos 540
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("ZaraGallery")]

    button:
        xpos 1360
        ypos 540
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("WidowGallery")]

    button:
        xpos 1610
        ypos 540
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("NancyGallery")]

    button:
        xpos 110
        ypos 740
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("IvankaGallery")]

    button:
        xpos 360
        ypos 740
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("MelaniaGallery")]

    button:
        xpos 610
        ypos 740
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("KimberlyGallery")]

    button:
        xpos 860
        ypos 740
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("CompoundGallery")]

    button:
        xpos 1110
        ypos 740
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("ExploreGallery")]

    button:
        xpos 1360
        ypos 740
        xysize(192, 108)      
        action [renpy.music.stop, Jump ("TownGallery")]

    if renpy.seen_image("whitehouse01"):
        button:
            xpos 1610
            ypos 740
            xysize(192, 108)      
            action [renpy.music.stop, Jump ("WhiteHouseGallery")]

return