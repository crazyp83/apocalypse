label Mccumsound:
call screen mcchoosesound
screen mcchoosesound:
    modal True
    imagebutton:
        focus_mask True
        idle "v07/mcsoundon.png"
        hover "v07/mcsoundon.png"
        action [SetVariable("persistent.cumsoundon", True), renpy.save_persistent(), Hide("mcchoosesound"), Return]
    imagebutton:
        focus_mask True
        idle "v07/mcsoundoff.png"
        hover "v07/mcsoundoff.png"
        action [SetVariable("persistent.cumsoundon", False), renpy.save_persistent(), Hide("mcchoosesound"), Return]
        
