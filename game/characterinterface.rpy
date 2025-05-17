label CharacterInterface:        
scene interface01
if siriclothes == 1:            
    show siri06aa at left
if siriclothes == 2:
    show siri06ba at left
if siriclothes == 3:
    show siri06ca at left
label PreviousPage:
show characterinterface01
call screen characterinterface03
screen characterinterface03:
    
    imagebutton:
        focus_mask True
        idle "Icons/exitleftidle.png"
        hover "Icons/exitlefthover.png"
        action Jump ("Interface02")

    imagebutton:
        focus_mask True
        idle "Bedroom/charam.png"
        hover "Bedroom/charam.png"
        action Jump ("AmyInterface")
    
    imagebutton:
        focus_mask True
        idle "Bedroom/charan.png"
        hover "Bedroom/charan.png"
        action Jump ("AngieInterface")
    
    imagebutton:
        focus_mask True
        idle "Bedroom/charay.png"
        hover "Bedroom/charay.png"
        action Jump ("AylaInterface")
    
    imagebutton:
        focus_mask True
        idle "Bedroom/charba.png"
        hover "Bedroom/charba.png"
        action Jump ("BarbaraInterface")
    
    imagebutton:
        focus_mask True
        idle "Bedroom/charbe.png"
        hover "Bedroom/charbe.png"
        action Jump ("BellaInterface")
    
    imagebutton:
        focus_mask True
        idle "Bedroom/charcl.png"
        hover "Bedroom/charcl.png"
        action Jump ("ClaraInterface")
    
    imagebutton:
        focus_mask True
        idle "Bedroom/charcy.png"
        hover "Bedroom/charcy.png"
        action Jump ("CyrlInterface")
    
    imagebutton:
        focus_mask True
        idle "Bedroom/charde.png"
        hover "Bedroom/charde.png"
        action Jump ("DebraInterface")
    
    imagebutton:
        focus_mask True
        idle "Bedroom/charta.png"
        hover "Bedroom/charta.png"
        action Jump ("TaraInterface")
    
    imagebutton:
        focus_mask True
        idle "Bedroom/charma.png"
        hover "Bedroom/charma.png"
        action Jump ("MarnieInterface")
    
    imagebutton:
        focus_mask True
        idle "Bedroom/charpe.png"
        hover "Bedroom/charpe.png"
        action Jump ("PennyInterface")
    
    imagebutton:
        focus_mask True
        idle "Bedroom/charla.png"
        hover "Bedroom/charla.png"
        action Jump ("LaurieInterface")
    
    imagebutton:
        focus_mask True
        idle "Bedroom/charra.png"
        hover "Bedroom/charra.png"
        action Jump ("RachelInterface")
            
    imagebutton:
        focus_mask True
        idle "Bedroom/charle.png"
        hover "Bedroom/charle.png"
        action Jump ("LenaInterface")

    imagebutton:
        focus_mask True
        idle "Bedroom/chargw.png"
        hover "Bedroom/chargw.png"
        action Jump ("GwenInterface")

    imagebutton:
        focus_mask True
        idle "Bedroom/charmi.png"
        hover "Bedroom/charmi.png"
        action Jump ("MichikoInterface")

    imagebutton:
        focus_mask True
        idle "Bedroom/charsu.png"
        hover "Bedroom/charsu.png"
        action Jump ("SukiInterface")

    imagebutton:
        focus_mask True
        idle "Bedroom/charru.png"
        hover "Bedroom/charru.png"
        action Jump ("RubyInterface")

    imagebutton:
        focus_mask True
        idle "Bedroom/nextpage.png"
        hover "Bedroom/nextpage.png"
        action Jump ("NextPage")

label NextPage:
hide screen characterinterface03
hide characterinterface01
show characterinterface01b
call screen characterinterface04
screen characterinterface04:

    if metza:
        imagebutton:
            focus_mask True
            idle "Bedroom/charza.png"
            hover "Bedroom/charza.png"
            action Jump ("ZaraInterface")

    if metwi:
        imagebutton:
            focus_mask True
            idle "Bedroom/charwi.png"
            hover "Bedroom/charwi.png"
            action Jump ("WidowInterface")

    if metmo:
        imagebutton:
            focus_mask True
            idle "Bedroom/charmo.png"
            hover "Bedroom/charmo.png"
            action Jump ("NancyInterface")

    if metiv:
        imagebutton:
            focus_mask True
            idle "Bedroom/chariv.png"
            hover "Bedroom/chariv.png"
            action Jump ("IvankaInterface")

    if metme:
        imagebutton:
            focus_mask True
            idle "Bedroom/charme.png"
            hover "Bedroom/charme.png"
            action Jump ("MelaniaInterface")

    if metto:
        imagebutton:
            focus_mask True
            idle "Bedroom/charto.png"
            hover "Bedroom/charto.png"
            action Jump ("TaylorInterface")

    if seenwendy:
        imagebutton:
            focus_mask True
            idle "v06/charwe.png"
            hover "v06/charwe.png"
            action Jump ("WendyInterface")

    if metkg:
        imagebutton:
            focus_mask True
            idle "v07/charkg.png"
            hover "v07/charkg.png"
            action Jump ("KimberlyInterface")

    if seenhulk:
        imagebutton:
            focus_mask True
            idle "v07/charsh.png"
            hover "v07/charsh.png"
            action Jump ("HulkInterface")

    if strippercatchwin or methe:
        imagebutton:
            focus_mask True
            idle "v07/charsy.png"
            hover "v07/charsy.png"
            action Jump ("SukYuInterface")

    if methe:
        imagebutton:
            focus_mask True
            idle "v07/charhe.png"
            hover "v07/charhe.png"
            action Jump ("HeatherInterface")

    if metkr:
        imagebutton:
            focus_mask True
            idle "v08/charkr.png"
            hover "v08/charkr.png"
            action Jump ("KristaInterface")

    if metqu:
        imagebutton:
            focus_mask True
            idle "v081/charqu.png"
            hover "v081/charqu.png"
            action Jump ("PauletteInterface")

    imagebutton:
        focus_mask True
        idle "Bedroom/nextpage.png"
        hover "Bedroom/nextpage.png"
        action Jump ("PreviousPage")

label AmyInterface:
scene interface01
show screen amystats
show characterinterface02
call screen amywalk
screen amywalk:
    add amywalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    add "Icons/smallsierra.png" at posfaction
    if haremam:
        add "Icons/haremamy.png" at haremsheetpos
    if babyamy:
        add "v07/mcbabycount.png" at posbabies02
        text "{font=Gui/goodtimes.ttf} 1{/font}" color "#ff0000" size 35 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posbabies
    text "{font=Gui/goodtimes.ttf}   amy{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengtham]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmsam]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatam]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustam]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("amystats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label AngieInterface:
scene interface01
show characterinterface02
show screen angiestats
call screen angiewalk
screen angiewalk:
    add angiewalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    add "Icons/smalltrumpster.png" at posfaction
    if hareman:
        add "Icons/haremangie.png" at haremsheetpos
    if babyangie:
        add "v07/mcbabycount.png" at posbabies02
        text "{font=Gui/goodtimes.ttf} 1{/font}" color "#ff0000" size 35 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posbabies
    text "{font=Gui/goodtimes.ttf} angie{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthan]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmsan]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatan]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustan]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("angiestats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label BellaInterface:
scene interface01
show characterinterface02
show screen bellastats
call screen bellawalk
screen bellawalk:
    add bellawalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    add "Icons/smallchurch.png" at posfaction
    if harembe:
        add "v082/harembella.png" at haremsheetpos
    text "{font=Gui/goodtimes.ttf} bella{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthbe]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmsbe]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatbe]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustbe]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("bellastats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label CyrlInterface:
scene interface01
show characterinterface02
show screen cyrlstats
call screen cyrlwalk
screen cyrlwalk:
    add cyrlwalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    if haremcy:
        add "Icons/haremcyrl.png" at haremsheetpos
    text "{font=Gui/goodtimes.ttf}  cyrl{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthcy]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmscy]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatcy]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustcy]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("cyrlstats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label DebraInterface:
scene interface01
show characterinterface02
show screen debrastats
call screen debrawalk
screen debrawalk:
    add debrawalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    add "Icons/smalldeep.png" at posfaction
    if haremde:
        add "v09/haremdebra.png" at haremsheetpos
    text "{font=Gui/goodtimes.ttf} debra{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthde]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmsde]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatde]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustde]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("debrastats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label GwenInterface:
scene interface01
show characterinterface02
show screen gwenstats
call screen gwenwalk
screen gwenwalk:
    add gwenwalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    add "Icons/smalltrumpster.png" at posfaction
    if haremgw:
        add "Icons/haremgwen.png" at haremsheetpos
    if babygwen:
        add "v07/mcbabycount.png" at posbabies02
        text "{font=Gui/goodtimes.ttf} 1{/font}" color "#ff0000" size 35 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posbabies
    text "{font=Gui/goodtimes.ttf}  gwen{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthgw]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmsgw]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatgw]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustgw]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("gwenstats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label BarbaraInterface:
scene interface01
show characterinterface02
show screen barbarastats
call screen barbarawalk
screen barbarawalk:
    add barbarawalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    add "Icons/smalltrumpster.png" at posfaction
    if haremba:
        add "v081/harembarbara.png" at haremsheetpos
    if babybarbara:
        add "v07/mcbabycount.png" at posbabies02
        text "{font=Gui/goodtimes.ttf} 1{/font}" color "#ff0000" size 35 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posbabies
    text "{font=Gui/goodtimes.ttf}barbara{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthba]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmsba]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatba]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustba]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("barbarastats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label PennyInterface:
scene interface01
show characterinterface02
show screen pennystats
call screen pennywalk
screen pennywalk:
    add pennywalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    add "Icons/smallwarrior.png" at posfaction
    if harempe:
        add "v061/harempenny.png" at haremsheetpos
    text "{font=Gui/goodtimes.ttf} penny{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthpe]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmspe]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatpe]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustpe]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("pennystats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label LenaInterface:
scene interface01
show characterinterface02
show screen lenastats
call screen lenawalk
screen lenawalk:
    add lenawalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    add "Icons/smalldeep.png" at posfaction
    if haremle:
        add "v08/haremlena.png" at haremsheetpos
    text "{font=Gui/goodtimes.ttf}  lena{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthle]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmsle]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatle]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustle]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("lenastats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label LaurieInterface:
scene interface01
show characterinterface02
show screen lauriestats
call screen lauriewalk
screen lauriewalk:
    add lauriewalk xalign 0.35 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    add "Icons/smallsierra.png" at posfaction
    if haremla:
        add "v072/haremlaurie.png" at haremsheetpos
    if babylaurie:
        add "v07/mcbabycount.png" at posbabies02
        text "{font=Gui/goodtimes.ttf} 1{/font}" color "#ff0000" size 35 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posbabies
    text "{font=Gui/goodtimes.ttf}laurie{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthla]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmsla]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatla]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustla]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("lauriestats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label MarnieInterface:
scene interface01
show characterinterface02
show screen marniestats
call screen marniewalk
screen marniewalk:
    add marniewalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    add "Icons/smallwarrior.png" at posfaction
    if haremma:
        add "v07/haremmarnie.png" at haremsheetpos
    text "{font=Gui/goodtimes.ttf}marnie{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthma]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmsma]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatma]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustma]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("marniestats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label TaraInterface:
scene interface01
show characterinterface02
show screen tarastats
call screen tarawalk
screen tarawalk:
    add tarawalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    add "Icons/smalldeep.png" at posfaction
    text "{font=Gui/goodtimes.ttf}  tara{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthta]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmsta]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatta]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustta]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("tarastats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label SukiInterface:
scene interface01
show characterinterface02
show screen sukistats
call screen sukiwalk
screen sukiwalk:
    add sukiwalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    if haremsu:
        add "Icons/haremsuki.png" at haremsheetpos
    add "Icons/smalldeep.png" at posfaction
    text "{font=Gui/goodtimes.ttf}  suki{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthsu]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmssu]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatsu]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustsu]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("sukistats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label AylaInterface:
scene interface01
show characterinterface02
show screen aylastats
call screen aylawalk
screen aylawalk:
    add aylawalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    if haremay:
        add "Icons/haremayla.png" at haremsheetpos
    if babyayla >= 1:
        add "v07/mcbabycount.png" at posbabies02
        text "{font=Gui/goodtimes.ttf} 1{/font}" color "#ff0000" size 35 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posbabies
    add "Icons/smallchurch.png" at posfaction
    text "{font=Gui/goodtimes.ttf}  ayla{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthay]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmsay]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatay]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustay]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("aylastats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label RachelInterface:
scene interface01
show characterinterface02
show screen rachelstats
call screen rachelwalk
screen rachelwalk:
    add rachelwalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    text "{font=Gui/goodtimes.ttf}rachel{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthra]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmsra]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatra]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustra]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("rachelstats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label ZaraInterface:
scene interface01
show characterinterface02
show screen zarastats
call screen zarawalk
screen zarawalk:
    add zarawalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    if haremza:
        add "Icons/haremzara.png" at haremsheetpos
    if babyzara:
        add "v07/mcbabycount.png" at posbabies02
        text "{font=Gui/goodtimes.ttf} 1{/font}" color "#ff0000" size 35 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posbabies
    text "{font=Gui/goodtimes.ttf}  zara{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthza]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmsza]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatza]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustza]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("zarastats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label ClaraInterface:
scene interface01
show characterinterface02
show screen clarastats
call screen clarawalk
screen clarawalk:
    add clarawalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    add "Icons/smallchurch.png" at posfaction
    if haremcl:
        add "v071/haremclara.png" at haremsheetpos
    text "{font=Gui/goodtimes.ttf} clara{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthcl]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmscl]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatcl]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustcl]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("clarastats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label RubyInterface:
scene interface01
show characterinterface02
show screen rubystats
call screen rubywalk
screen rubywalk:
    add rubywalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    add "Icons/smallwarrior.png" at posfaction
    if haremru:
        add "Icons/haremruby.png" at haremsheetpos
    text "{font=Gui/goodtimes.ttf}  ruby{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthru]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmsru]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatru]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustru]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("rubystats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label MichikoInterface:
scene interface01
show characterinterface02
show screen michikostats
call screen michikowalk
screen michikowalk:
    add michikowalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    add "Icons/smallsierra.png" at posfaction
    if haremmi:
        add "Icons/haremmichiko.png" at haremsheetpos
    if babymichiko:
        add "v07/mcbabycount.png" at posbabies02
        text "{font=Gui/goodtimes.ttf} 1{/font}" color "#ff0000" size 35 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posbabies
    text "{font=Gui/goodtimes.ttf}michiko{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthmi]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmsmi]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatmi]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustmi]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("michikostats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label WidowInterface:
scene interface01
show characterinterface02
show screen widowstats
call screen widowwalk
screen widowwalk:
    add widowwalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    text "{font=Gui/goodtimes.ttf}Black Widow{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthwi]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmswi]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatwi]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustwi]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("widowstats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label NancyInterface:
scene interface01
show characterinterface02
show screen nancystats
call screen nancywalk
screen nancywalk:
    add nancywalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    if haremmo:
        add "Icons/haremnancy.png" at haremsheetpos
    if babynancy:
        add "v07/mcbabycount.png" at posbabies02
        text "{font=Gui/goodtimes.ttf} 1{/font}" color "#ff0000" size 35 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posbabies
    text "{font=Gui/goodtimes.ttf}mom{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthmo]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmsmo]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatmo]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustmo]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("nancystats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label IvankaInterface:
scene interface01
show characterinterface02
show screen ivankastats
call screen ivankawalk
screen ivankawalk:
    add ivankawalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    add "Icons/smalltrumpster.png" at posfaction
    text "{font=Gui/goodtimes.ttf}Ivanka{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthiv]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmsiv]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combativ]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustiv]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("ivankastats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label MelaniaInterface:
scene interface01
show characterinterface02
show screen melaniastats
call screen melaniawalk01
screen melaniawalk01:
    add melaniawalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    add "Icons/smalltrumpster.png" at posfaction
    add "Icons/smalldeep.png" at posfaction02
    text "{font=Gui/goodtimes.ttf}Melania{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthme]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmsme]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatme]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustme]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("melaniastats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label TaylorInterface:
scene interface01
show characterinterface02
show screen taylorstats
call screen taylorwalk01
screen taylorwalk01:
    add taylorwalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    if babytaylor >= 1:
        add "v07/mcbabycount.png" at posbabies02
        text "{font=Gui/goodtimes.ttf}[babytaylorcount]{/font}" color "#ff0000" size 35 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posbabies
    text "{font=Gui/goodtimes.ttf}Taylor{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthto]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmsto]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatto]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustto]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("taylorstats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label WendyInterface:
scene interface01
show characterinterface02
show screen wendystats
call screen wendywalk01
screen wendywalk01:
    add wendywalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    text "{font=Gui/goodtimes.ttf}Wendy{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}[strengthwe]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}[firearmswe]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}[combatwe]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustwe]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("wendystats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label KimberlyInterface:
scene interface01
show characterinterface02
show screen kimberlystats
call screen kimberlywalk01
screen kimberlywalk01:
    add kimberlywalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    add "Icons/smalltrumpster.png" at posfaction
    text "{font=Gui/goodtimes.ttf}Kimberly{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}9-18{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}5{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}6-12{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustkg]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("kimberlystats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label HulkInterface:
scene interface01
show characterinterface02
show screen hulkstats
call screen hulkwalk01
screen hulkwalk01:
    add hulkwalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    text "{font=Gui/goodtimes.ttf}She-Hulk{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}15{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}0{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}15{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustsh]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("hulkstats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label SukYuInterface:
scene interface01
show characterinterface02
show screen sukyustats
call screen sukyuwalk01
screen sukyuwalk01:
    add sukyuwalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    add "Icons/smallwarrior.png" at posfaction
    text "{font=Gui/goodtimes.ttf}Suk-Yu{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}2{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}1{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}3{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustsy]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("sukyustats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label HeatherInterface:
scene interface01
show characterinterface02
show screen heatherstats
call screen heatherwalk01
screen heatherwalk01:
    add heatherwalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    add "Icons/smallwarrior.png" at posfaction
    text "{font=Gui/goodtimes.ttf}Heather{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}2{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}2{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}2{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lusthe]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("heatherstats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label KristaInterface:
scene interface01
show characterinterface02
show screen kristastats
call screen kristawalk01
screen kristawalk01:
    add kristawalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    add "Icons/smalltrumpster.png" at posfaction
    text "{font=Gui/goodtimes.ttf}Krista{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}2{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}3{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}1{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustkr]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("kristastats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label PauletteInterface:
scene interface01
show characterinterface02
show screen paulettestats
call screen paulettewalk01
screen paulettewalk01:
    add paulettewalk xalign 0.37 yalign 0.8
    add "Bedroom/frame01.png" xalign 0.38 yalign 0.0
    add "Icons/exitleftidle.png"
    text "{font=Gui/goodtimes.ttf}Paulette{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posname
    text "{font=Gui/goodtimes.ttf}18{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstrength
    text "{font=Gui/goodtimes.ttf}1{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posfirearms
    text "{font=Gui/goodtimes.ttf}5{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscombat
    text "{font=Gui/goodtimes.ttf}[lustqu]{/font}" color "#ff0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslust
    modal True
    button:
        xpos .02
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("paulettestats"), renpy.hide_screen("characters"), Jump ("CharacterInterface")]

label PlayerInterface:
$ totalfrench = frenchovermax + mcfrench
hide lustinterface
hide lustinterface02
hide nextpagelust
show mcbackground at centerright
if mcwarrior == 5:
    show mcwarrior01 at centerright
if mcdeep == 5:
    show mcdeep01 at centerright
if mcsierra == 5:
    show mcsierra01 at centerright
if mctrumpster == 5:
    show mctrumpster01 at centerright
if mcchurch == 5:
    show mcchurch01 at centerright
if mcwarrior <= 4 and mcdeep <= 4 and mcchurch <= 4 and mcsierra <= 4 and mctrumpster <= 4:
    show mcnofaction at centerright
show frame01 at centerright
show mcinterface at left with moveinleft
call screen mcinterface
screen mcinterface:
    add "Icons/exitidle.png"
    add "Icons/luststats.png"
    if mcchildren >= 1:
        add "v07/mcbabycount.png" at mcposbabies02
        text "{font=Gui/goodtimes.ttf} [mcchildren]{/font}" color "#ff0000" size 35 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at mcposbabies
    text "{font=Gui/goodtimes.ttf} [name]{/font}" color "#1c73ff" size 45 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at mcposname
    if mcstrength <= 15 and mcmaxstrength == False:
        text "{font=Gui/goodtimes.ttf} strength      [mcstrength]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at mcposstrength
    if mcmaxstrength:
        text "{font=Gui/goodtimes.ttf} strength      16{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at mcposstrength
    text "{font=Gui/goodtimes.ttf} firearms       [mcfirearms]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at mcposfirearms
    text "{font=Gui/goodtimes.ttf} combat           [mccombat]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at mcposcombat
    text "{font=Gui/goodtimes.ttf} mechanics    [mcmechanics]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at mcposmechanics
    text "{font=Gui/goodtimes.ttf} french            [totalfrench]{/font}" color "#1c73ff" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at mcposfrench
    text "{font=Gui/goodtimes.ttf}[mcdeep]{/font}" color "#ff0000" size 35 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at mcposdeep
    text "{font=Gui/goodtimes.ttf}[mctrumpster]{/font}" color "#ff0000" size 35 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at mcpostrumpster
    text "{font=Gui/goodtimes.ttf}[mcsierra]{/font}" color "#ff0000" size 35 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at mcpossierra
    text "{font=Gui/goodtimes.ttf}[mcwarrior]{/font}" color "#ff0000" size 35 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at mcposwarrior
    text "{font=Gui/goodtimes.ttf}[mcchurch]{/font}" color "#ff0000" size 35 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at mcposchurch
    text "{font=Gui/goodtimes.ttf}height: 6ft0         age: 18 \n \nbiceps: 24\"          chest: 62\" \nwaist: 28\"            quads: 30\"{/font}" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posmcstats
    if mcwarrior == 5:
        add "Icons/smallwarrior.png" at poscharacterfaction
        if warriornickname:
            text "{font=gui/Boogaloo-Regular.ttf} \"The Impaler\"{/font}" color "#3f2c7f" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posnickname
    if mcdeep == 5:
        add "Icons/smalldeep.png" at poscharacterfaction
    if mctrumpster == 5:
        add "Icons/smalltrumpster.png" at poscharacterfaction
        if trumpsternickname:
            text "{font=gui/Boogaloo-Regular.ttf} \"The Grabber\"{/font}" color "#3f2c7f" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posnickname
    if mcsierra == 5:
        add "Icons/smallsierra.png" at poscharacterfaction
        if sierranickname:
            text "{font=gui/Boogaloo-Regular.ttf} \"The Seeder\"{/font}" color "#3f2c7f" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posnickname
    if mcchurch == 5:
        add "Icons/smallchurch.png" at poscharacterfaction
        if churchnickname:
            text "{font=gui/Boogaloo-Regular.ttf} \"The Punisher\"{/font}" color "#3f2c7f" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posnickname

    button:
        xpos .92
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("mcinterface"), renpy.show_screen("mcstats"), renpy.hide("frame01"), renpy.hide("mcbackground"), renpy.hide("Icons/smallwarrior.png"), renpy.hide("Icons/smalldeep.png"), renpy.hide("Icons/smalltrumpster.png"), renpy.hide("Icons/smallsierra.png"), renpy.hide("Icons/smallchurch.png"),
            renpy.hide("mcnofaction"), renpy.hide("mctrumpster01"), renpy.hide("mcdeep01"), renpy.hide("mcsierra01"), renpy.hide("mcchurch01"), renpy.hide("mcinterface"), renpy.hide("mcwarrior01"), Return()]
    imagebutton:
        focus_mask True
        idle "Icons/luststats.png"
        hover "Icons/luststats.png"
        action [renpy.hide_screen("mcinterface"), Jump ("LustInterface")]
return

label LustInterface:
hide mcinterface
hide lustinterface02
hide mcbackground
hide nextpagelust
show mcbackground at centerright
if mcwarrior == 5:
    show mcwarrior01 at centerright
if mcdeep == 5:
    show mcdeep01 at centerright
if mcsierra == 5:
    show mcsierra01 at centerright
if mctrumpster == 5:
    show mctrumpster01 at centerright
if mcchurch == 5:
    show mcchurch01 at centerright
if mcwarrior <= 4 and mcdeep <= 4 and mcchurch <= 4 and mcsierra <= 4 and mctrumpster <= 4:
    show mcnofaction at centerright
show frame01 at centerright
show lustinterface at left with moveinleft
show nextpagelust
call screen lustinterface
screen lustinterface:
    add "Icons/exitidle.png"
    add "Icons/mcstats01.png"
    if babyamy:
        add "v09/minibabya.png" at posbabyam
    if babyamy == False:
        add "v09/minibabyb.png" at posbabyam
    if babyangie:
        add "v09/minibabya.png" at posbabyan
    if babyangie == False:
        add "v09/minibabyb.png" at posbabyan
    if babyayla:
        add "v09/minibabya.png" at posbabyay
    if babyayla == False:
        add "v09/minibabyb.png" at posbabyay
    if babybarbara:
        add "v09/minibabya.png" at posbabyba
    if babybarbara == False:
        add "v09/minibabyb.png" at posbabyba
    if babylaurie:
        add "v09/minibabya.png" at posbabyla
    if babylaurie == False:
        add "v09/minibabyb.png" at posbabyla
    if babymichiko:
        add "v09/minibabya.png" at posbabymi
    if babymichiko == False:
        add "v09/minibabyb.png" at posbabymi
    if babynancy:
        add "v09/minibabya.png" at posbabymo
    if babynancy == False:
        add "v09/minibabyb.png" at posbabymo
    if babyzara:
        add "v09/minibabya.png" at posbabyza
    if babyzara == False:
        add "v09/minibabyb.png" at posbabyza
    if babygwen:
        add "v09/minibabya.png" at posbabygw
    if babygwen == False:
        add "v09/minibabyb.png" at posbabygw
    text "{font=Gui/goodtimes.ttf} [lustam]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustam
    text "{font=Gui/goodtimes.ttf} [lustan]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustan
    text "{font=Gui/goodtimes.ttf} [lustay]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustay
    text "{font=Gui/goodtimes.ttf} [lustba]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustba
    text "{font=Gui/goodtimes.ttf} [lustbe]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustbe
    text "{font=Gui/goodtimes.ttf} [lustcl]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustcl
    text "{font=Gui/goodtimes.ttf} [lustcy]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustcy
    text "{font=Gui/goodtimes.ttf} [lustde]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustde
    text "{font=Gui/goodtimes.ttf} [lustgw]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustgw
    text "{font=Gui/goodtimes.ttf} [lustla]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustla
    text "{font=Gui/goodtimes.ttf} [lustle]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustle
    text "{font=Gui/goodtimes.ttf} [lustma]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustma
    text "{font=Gui/goodtimes.ttf} [lustmi]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustmi
    text "{font=Gui/goodtimes.ttf} [lustpe]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustpe
    text "{font=Gui/goodtimes.ttf} [lustra]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustra
    text "{font=Gui/goodtimes.ttf} [lustru]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustru
    text "{font=Gui/goodtimes.ttf} [lustsu]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustsu
    text "{font=Gui/goodtimes.ttf} [lustta]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustta
    if mcwarrior == 5:
        add "Icons/smallwarrior.png" at poscharacterfaction
        if warriornickname:
            text "{font=gui/Boogaloo-Regular.ttf} \"The Impaler\"{/font}" color "#3f2c7f" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posnickname
    if mcdeep == 5:
        add "Icons/smalldeep.png" at poscharacterfaction
    if mctrumpster == 5:
        add "Icons/smalltrumpster.png" at poscharacterfaction
        if trumpsternickname:
            text "{font=gui/Boogaloo-Regular.ttf} \"The Grabber\"{/font}" color "#3f2c7f" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posnickname
    if mcsierra == 5:
        add "Icons/smallsierra.png" at poscharacterfaction
        if sierranickname:
            text "{font=gui/Boogaloo-Regular.ttf} \"The Tree-Trunk\"{/font}" color "#3f2c7f" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posnickname
    if mcchurch == 5:
        add "Icons/smallchurch.png" at poscharacterfaction
        if churchnickname:
            text "{font=gui/Boogaloo-Regular.ttf} \"The Punisher\"{/font}" color "#3f2c7f" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posnickname
    modal True
    button:
        xpos .92
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("mcinterface"), renpy.show_screen("mcstats"), renpy.hide("frame01"), renpy.hide("nextpagelust"), renpy.hide("mcbackground"), renpy.hide("Icons/smallwarrior.png"), renpy.hide("Icons/smalldeep.png"), renpy.hide("Icons/smalltrumpster.png"), renpy.hide("Icons/smallsierra.png"), renpy.hide("Icons/smallchurch.png"),
            renpy.hide("mcnofaction"), renpy.hide("mctrumpster01"), renpy.hide("mcdeep01"), renpy.hide("mcsierra01"), renpy.hide("mcchurch01"), renpy.hide("lustinterface"), renpy.hide("mcwarrior01"), Return()]
    imagebutton:
        focus_mask True
        idle "Icons/mcstats01.png"
        hover "Icons/mcstats01.png"
        action [renpy.hide_screen("lustinterface"), Jump ("PlayerInterface")]
    if metza or metwi or metmo or metiv or metme or metto or seenwendy or metkg or strippercatchwin or methe or metkr or metqu:
        imagebutton:
            focus_mask True
            idle "Icons/nextpagelust.png"
            hover "Icons/nextpagelust.png"
            action [renpy.hide_screen("lustinterface"), Jump ("LustInterface02")]
return

label LustInterface02:
hide mcinterface
hide lustinterface
hide mcbackground
hide nextpagelust
show mcbackground at centerright
if mcwarrior == 5:
    show mcwarrior01 at centerright
if mcdeep == 5:
    show mcdeep01 at centerright
if mcsierra == 5:
    show mcsierra01 at centerright
if mctrumpster == 5:
    show mctrumpster01 at centerright
if mcchurch == 5:
    show mcchurch01 at centerright
if mcwarrior <= 4 and mcdeep <= 4 and mcchurch <= 4 and mcsierra <= 4 and mctrumpster <= 4:
    show mcnofaction at centerright
show frame01 at centerright
hide lustinterface
show lustinterface02
show nextpagelust
call screen lustinterface02
screen lustinterface02:
    add "Icons/exitidle.png"
    add "Icons/mcstats01.png"
    if metza:
        add "Icons/lustinterfaceza.png"
        text "{font=Gui/goodtimes.ttf} [lustza]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustza
        if babyzara:
            add "v09/minibabya.png" at posbabyza
        if babyzara == False:
            add "v09/minibabyb.png" at posbabyza
    if metwi:
        add "Icons/lustinterfacewi.png"
        text "{font=Gui/goodtimes.ttf} [lustwi]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustwi
    if metmo:
        add "Icons/lustinterfacemo.png"
        text "{font=Gui/goodtimes.ttf} [lustmo]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustmo
        if babynancy:
            add "v09/minibabya.png" at posbabymo
        if babynancy == False:
            add "v09/minibabyb.png" at posbabymo
    if metiv:
        add "Icons/lustinterfaceiv.png"
        text "{font=Gui/goodtimes.ttf} [lustiv]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustiv
    if metme:
        add "Icons/lustinterfaceme.png"
        text "{font=Gui/goodtimes.ttf} [lustme]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustme
    if metto:
        add "Icons/lustinterfaceto.png"
        text "{font=Gui/goodtimes.ttf} [lustto]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustto
        if babytaylor:
            add "v09/minibabya.png" at posbabyto
            text "{font=Gui/goodtimes.ttf} [babytaylorcount]{/font}" color "#ff0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posbabytocount
        if babytaylor == False:
            add "v09/minibabyb.png" at posbabyto
    if seenwendy:
        add "v06/lustinterfacewe.png"
        text "{font=Gui/goodtimes.ttf} [lustwe]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustwe
    if metkg:
        add "v07/lustinterfacekg.png"
        text "{font=Gui/goodtimes.ttf} [lustkg]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustkg
    if strippercatchwin or methe:
        add "v07/lustinterfacesy.png"
        text "{font=Gui/goodtimes.ttf} [lustsy]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustsy
    if methe:
        add "v07/lustinterfacehe.png"
        text "{font=Gui/goodtimes.ttf} [lusthe]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslusthe
    if metkr:
        add "v08/lustinterfacekr.png"
        text "{font=Gui/goodtimes.ttf} [lustkr]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustkr
    if metqu:
        add "v081/lustinterfacequ.png"
        text "{font=Gui/goodtimes.ttf} [lustqu]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poslustqu
    if mcwarrior == 5:
        add "Icons/smallwarrior.png" at poscharacterfaction
        if warriornickname:
            text "{font=gui/Boogaloo-Regular.ttf} \"The Impaler\"{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posnickname
    if mcdeep == 5:
        add "Icons/smalldeep.png" at poscharacterfaction
    if mctrumpster == 5:
        add "Icons/smalltrumpster.png" at poscharacterfaction
        if trumpsternickname:
            text "{font=gui/Boogaloo-Regular.ttf} \"The Grabber\"{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posnickname
    if mcsierra == 5:
        add "Icons/smallsierra.png" at poscharacterfaction
    if mcchurch == 5:
        add "Icons/smallchurch.png" at poscharacterfaction
    modal True
    button:
        xpos .92
        ypos .44
        xysize(140, 80)        
        action [renpy.hide_screen("mcinterface"), renpy.show_screen("mcstats"), renpy.hide("frame01"), renpy.hide("nextpagelust"), renpy.hide("mcbackground"), renpy.hide("Icons/smallwarrior.png"), renpy.hide("Icons/smalldeep.png"), renpy.hide("Icons/smalltrumpster.png"), renpy.hide("Icons/smallsierra.png"), renpy.hide("Icons/smallchurch.png"),
            renpy.hide("mcnofaction"), renpy.hide("mctrumpster01"), renpy.hide("mcdeep01"), renpy.hide("mcsierra01"), renpy.hide("mcchurch01"), renpy.hide("lustinterface02"), renpy.hide("mcwarrior01"), Return()]
    imagebutton:
        focus_mask True
        idle "Icons/mcstats01.png"
        hover "Icons/mcstats01.png"
        action [renpy.hide_screen("lustinterface02"), Jump ("PlayerInterface")]
    imagebutton:
        focus_mask True
        idle "Icons/nextpagelust.png"
        hover "Icons/nextpagelust.png"
        action [renpy.hide_screen("lustinterface02"), Jump ("LustInterface")]
return

