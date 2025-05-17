label TipsMenu:
call screen tipsmenu
screen tipsmenu:
    modal True
    imagebutton:
        focus_mask True
        idle "v08/tipson.png"
        hover "v08/tipson.png"
        action [SetVariable("persistent.tipson", True), renpy.save_persistent(), Hide("tipsmenu"), Return]
    imagebutton:
        focus_mask True
        idle "v08/tipsoff.png"
        hover "v08/tipsoff.png"
        action [SetVariable("persistent.tipson", False), renpy.save_persistent(), Hide("tipsmenu"), Return]
        
