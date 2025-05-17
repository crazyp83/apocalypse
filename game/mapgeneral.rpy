label ExploringMap:
hide screen calendar
hide screen mcstats
scene mapgeneral
call screen mapgeneral
screen mapgeneral:
    modal True    
    imagebutton:
        focus_mask True
        idle "Command/hexA0idle.png"
        hover "Command/hexA0hover.png"  hovered Play("sound", "Sounds/rollover.mp3")
        action Jump ("ExploringMap")

    if exploredhex01:
        imagebutton:
            focus_mask True
            idle "Command/hexA1idle.png"
            hover "Command/hexA1bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(1)
    if exploredhex01 == False:
        imagebutton:
            focus_mask True
            idle "Command/hexA1idle.png"
            hover "Command/hexA1ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(1)

    if exploredhex02:
        imagebutton:
            focus_mask True
            idle "Command/hexA2idle.png"
            hover "Command/hexA2bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")
    if exploredhex02 == False:
        imagebutton:
            focus_mask True
            idle "Command/hexA2idle.png"
            hover "Command/hexA2ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(2)

    if clearedhex03:
        imagebutton:
            focus_mask True
            idle "Command/hexA3idle.png"
            hover "Command/hexA3chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")
    if exploredhex03 and clearedhex03 == False:
        imagebutton:
            focus_mask True
            idle "Command/hexA3idle.png"
            hover "Command/hexA3bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(3)
    if exploredhex03 == False:
        imagebutton:
            focus_mask True
            idle "Command/hexA3idle.png"
            hover "Command/hexA3ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(3)

    if clearedhex11:
        imagebutton:
            focus_mask True
            idle "Command/hexB1idle.png"
            hover "Command/hexB1chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")
    if exploredhex11 and wave01explored and clearedhex11 == False:
        imagebutton:
            focus_mask True
            idle "Command/hexB1idle.png"
            hover "Command/hexB1bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(11)
    if exploredhex11 == False and wave01explored:
        imagebutton:
            focus_mask True
            idle "Command/hexB1idle.png"
            hover "Command/hexB1ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(11)

    if exploredhex12 and wave01explored:
        imagebutton:
            focus_mask True
            idle "Command/hexB2idle.png"
            hover "Command/hexB2bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")
    if exploredhex12 == False and wave01explored:
        imagebutton:
            focus_mask True
            idle "Command/hexB2idle.png"
            hover "Command/hexB2ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(12)

    if exploredhex13 and wave01explored:
        imagebutton:
            focus_mask True
            idle "Command/hexB3idle.png"
            hover "Command/hexB3bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(13)
    if exploredhex13 == False and wave01explored:
        imagebutton:
            focus_mask True
            idle "Command/hexB3idle.png"
            hover "Command/hexB3ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(13)

    if exploredhex14 and wave01explored:
        imagebutton:
            focus_mask True
            idle "Command/hexB4idle.png"
            hover "Command/hexB4bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(14)
    if exploredhex14 == False and wave01explored:
        imagebutton:
            focus_mask True
            idle "Command/hexB4idle.png"
            hover "Command/hexB4ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(14)

    if exploredhex15 and wave01explored:
        imagebutton:
            focus_mask True
            idle "Command/hexB5idle.png"
            hover "Command/hexB5bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(15)
    if exploredhex15 == False and wave01explored:
        imagebutton:
            focus_mask True
            idle "Command/hexB5idle.png"
            hover "Command/hexB5ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(15)

    if exploredhex16 and wave01explored and clearedhex16:
        imagebutton:
            focus_mask True
            idle "Command/hexB6idle.png"
            hover "Command/hexB6chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")
    if exploredhex16 and wave01explored and clearedhex16 == False:
        imagebutton:
            focus_mask True
            idle "Command/hexB6idle.png"
            hover "Command/hexB6bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(16)
    if exploredhex16 == False and wave01explored:
        imagebutton:
            focus_mask True
            idle "Command/hexB6idle.png"
            hover "Command/hexB6ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(16)
            
    if exploredhex17 and scarlettleft and not scarlettjoined and wave01explored:
        imagebutton:
            focus_mask True
            idle "Command/hexB7idle.png"
            hover "Command/hexB7chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(17)
    if exploredhex17 and scarlettjoined and wave01explored:
        imagebutton:
            focus_mask True
            idle "Command/hexB7idle.png"
            hover "Command/hexB7bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(17)
    if exploredhex17 == False and wave01explored:
        imagebutton:
            focus_mask True
            idle "Command/hexB7idle.png"
            hover "Command/hexB7ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(17)

    if exploredhex21 == False and wave02explored and week >= 4 and clearedhex11:
        imagebutton:
            focus_mask True
            idle "Command/hexC1idle.png"
            hover "Command/hexC1bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(21)
    if exploredhex21 == False and wave02explored and week >= 4 and clearedhex11 == False:
        imagebutton:
            focus_mask True
            idle "Command/hexC1idle.png"
            hover "Command/hexC1ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")
    if exploredhex21 and wave02explored and week >= 4 and clearedhex11:
        imagebutton:
            focus_mask True
            idle "Command/hexC1idle.png"
            hover "Command/hexC1chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(21)

    if exploredhex22 == False and wave02explored and week >= 4:
        imagebutton:
            focus_mask True
            idle "Command/hexC2idle.png"
            hover "Command/hexC2ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(22)
    if exploredhex22 and wave02explored and week >= 4:
        imagebutton:
            focus_mask True
            idle "Command/hexC2idle.png"
            hover "Command/hexC2bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(22)

    if clearedhex23:
        imagebutton:
            focus_mask True
            idle "Command/hexC3bidle.png"
            hover "Command/hexC3chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")
    if wave02explored and knowforwardops == False and successprisoner == False and week >= 4:
        imagebutton:
            focus_mask True
            idle "Command/hexC3idle.png"
            hover "Command/hexC3ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(23)
    if wave01explored and (successprisoner or knowforwardops) and clearedhex23 == False:
        imagebutton:
            focus_mask True
            idle "Command/hexC3bidle.png"
            hover "Command/hexC3bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(23)

    if exploredhex24 == False and wave02explored and week >= 4:
        imagebutton:
            focus_mask True
            idle "Command/hexC4idle.png"
            hover "Command/hexC4ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(24)
    if exploredhex24 and wave02explored and clearedhex24 == False and week >= 4:
        imagebutton:
            focus_mask True
            idle "Command/hexC4idle.png"
            hover "Command/hexC4bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(24)
    if clearedhex24 and week >= 4:
        imagebutton:
            focus_mask True
            idle "Command/hexC4idle.png"
            hover "Command/hexC4chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")
        
    if wave01explored and knowdeserttown:
        imagebutton:
            focus_mask True
            idle "Command/hexC5bidle.png"
            hover "Command/hexC5bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(25)
    if exploredhex25 == False and wave02explored and knowdeserttown == False and week >= 4:
        imagebutton:
            focus_mask True
            idle "Command/hexC5idle.png"
            hover "Command/hexC5ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(25)

    if exploredhex26 == False and wave02explored and week >= 4:
        imagebutton:
            focus_mask True
            idle "Command/hexC6idle.png"
            hover "Command/hexC6ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(26)
    if exploredhex26 and wave02explored and clearedhex26 == False and week >= 4:
        imagebutton:
            focus_mask True
            idle "Command/hexC6idle.png"
            hover "Command/hexC6chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(26)
    if clearedhex26 and week >=4:
        imagebutton:
            focus_mask True
            idle "Command/hexC6idle.png"
            hover "Command/hexC6bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")
    
    if wave02explored and missionop == False and donemissionop == False and week >= 4:
        imagebutton:
            focus_mask True
            idle "Command/hexC7idle.png"
            hover "Command/hexC7ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(27)
    if wave02explored and missionop and donemissionop == False and week >= 4:
        imagebutton:
            focus_mask True
            idle "Command/hexC7idle.png"
            hover "Command/hexC7bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(27)
    if donemissionop and week >= 4:
        imagebutton:
            focus_mask True
            idle "Command/hexC7idle.png"
            hover "Command/hexC7chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")

    if wave03explored and exploredhex31 == False and week >= 6:
        imagebutton:
            focus_mask True
            idle "Command/hexD1idle.png"
            hover "Command/hexD1ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(31)
    if wave03explored and exploredhex31 and week >= 6:
        imagebutton:
            focus_mask True
            idle "Command/hexD1idle.png"
            hover "Command/hexD1bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(31)
    if wave03explored and exploredhex31 and seenmilking and week >= 6:
        imagebutton:
            focus_mask True
            idle "Command/hexD1idle.png"
            hover "Command/hexD1chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(31)
    if wave03explored and clearedhex31 and week >= 6:
        imagebutton:
            focus_mask True
            idle "Command/hexD1idle.png"
            hover "Command/hexD1dhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")

    if wave03explored and missionhulk == False and seenhulk == False and exploredhex32 == False and week >= 6:
        imagebutton:
            focus_mask True
            idle "Command/hexD2idle.png"
            hover "Command/hexD2ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(32)
    if wave03explored and seenhulk == False and exploredhex32 and week >= 6:
        imagebutton:
            focus_mask True
            idle "Command/hexD2idle.png"
            hover "Command/hexD2bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(32)
    if wave03explored and seenhulk and exploredhex32 and week >= 6:
        imagebutton:
            focus_mask True
            idle "Command/hexD2idle.png"
            hover "Command/hexD2chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(32)
    if wave03explored and clearedhex32 and week >= 6:
        imagebutton:
            focus_mask True
            idle "Command/hexD2idle.png"
            hover "Command/hexD2dhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")

    if wave03explored and exploredhex33 == False and week >= 6:
        imagebutton:
            focus_mask True
            idle "Command/hexD3idle.png"
            hover "Command/hexD3ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(33)
    if wave03explored and exploredhex33 and week >= 6:
        imagebutton:
            focus_mask True
            idle "Command/hexD3idle.png"
            hover "Command/hexD3chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(33)
    if wave03explored and clearedhex33 and week >= 6:
        imagebutton:
            focus_mask True
            idle "Command/hexD3idle.png"
            hover "Command/hexD3dhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")

    if wave03explored and exploredhex34 == False and week >= 6:
        imagebutton:
            focus_mask True
            idle "Command/hexD4idle.png"
            hover "Command/hexD4ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(34)
    if wave03explored and exploredhex34 and missionticompleted == False and week >= 6:
        imagebutton:
            focus_mask True
            idle "Command/hexD4idle.png"
            hover "Command/hexD4bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(34)
    if wave03explored and exploredhex34 and clearedhex34 and week >= 6:
        imagebutton:
            focus_mask True
            idle "Command/hexD4idle.png"
            hover "Command/hexD4chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")

    if wave03explored and exploredhex35 == False and week >= 6:
        imagebutton:
            focus_mask True
            idle "Command/hexD5idle.png"
            hover "Command/hexD5ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(35)
    if wave03explored and exploredhex35 and week >= 6:
        imagebutton:
            focus_mask True
            idle "Command/hexD5idle.png"
            hover "Command/hexD5bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(35)

    if wave03explored and exploredhex36 == False and week >= 6:
        imagebutton:
            focus_mask True
            idle "Command/hexD6idle.png"
            hover "Command/hexD6ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(36)
    if wave03explored and exploredhex36 and clearedhex36 == False and week >= 6:
        imagebutton:
            focus_mask True
            idle "Command/hexD6idle.png"
            hover "Command/hexD6bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(36)
    if wave03explored and exploredhex36 and clearedhex36 and week >= 6:
        imagebutton:
            focus_mask True
            idle "Command/hexD6idle.png"
            hover "Command/hexD6chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")

    if wave04explored and exploredhex41 == False and week >= 8:
        imagebutton:
            focus_mask True
            idle "v07/hexE1idle.png"
            hover "v07/hexE1ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(41)
    if wave04explored and exploredhex41 and week >= 8:
        imagebutton:
            focus_mask True
            idle "v07/hexE1idle.png"
            hover "v07/hexE1bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")

    if wave04explored and exploredhex42 == False and week >= 8:
        imagebutton:
            focus_mask True
            idle "Command/hexE2idle.png"
            hover "Command/hexE2ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(42)
    if wave04explored and exploredhex42 and canonized == False and week >= 8:
        imagebutton:
            focus_mask True
            idle "Command/hexE2idle.png"
            hover "Command/hexE2bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(42)
    if wave04explored and exploredhex42 and canonized and week >= 8:
        imagebutton:
            focus_mask True
            idle "Command/hexE2idle.png"
            hover "v06/hexE2chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")

    if wave04explored and warriorcapture == False and exploredhex43 == False and week >= 8:
        imagebutton:
            focus_mask True
            idle "v07/hexE3idle.png"
            hover "v07/hexE3ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(43)
    if wave04explored and warriorcapture == False and exploredhex43 and week >= 8:
        imagebutton:
            focus_mask True
            idle "v07/hexE3idle.png"
            hover "v07/hexE3bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(43)
    if wave04explored and warriorcapture and week >= 8:
        imagebutton:
            focus_mask True
            idle "v07/hexE3bidle.png"
            hover "v07/hexE3chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(43)
    if wave04explored and clearedhex43 and week >= 8:
        imagebutton:
            focus_mask True
            idle "v07/hexE3bidle.png"
            hover "v07/hexE3chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")
    
    if wave04explored and exploredhex44 == False and week >= 8:
        imagebutton:
            focus_mask True
            idle "Command/hexE4idle.png"
            hover "Command/hexE4ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(44)
    if wave04explored and exploredhex44 and clearedhex44 == False and week >= 8:
        imagebutton:
            focus_mask True
            idle "Command/hexE4idle.png"
            hover "Command/hexE4bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(44)
    if wave04explored and exploredhex44 and clearedhex44 and week >= 8:
        imagebutton:
            focus_mask True
            idle "Command/hexE4idle.png"
            hover "Command/hexE4chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")

    if wave04explored and exploredhex45 == False and week >= 8:
        imagebutton:
            focus_mask True
            idle "v06/hexE5idle.png"
            hover "v06/hexE5ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(45)
    if wave04explored and exploredhex45 and clearedhex45 == False and week >= 8:
        imagebutton:
            focus_mask True
            idle "v06/hexE5idle.png"
            hover "v06/hexE5bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(45)
    if wave04explored and exploredhex45 and clearedhex45 and week >= 8:
        imagebutton:
            focus_mask True
            idle "v06/hexE5idle.png"
            hover "v06/hexE5chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")

    if wave04explored and exploredhex46 == False and week >= 8:
        imagebutton:
            focus_mask True
            idle "v06/hexE6idle.png"
            hover "v06/hexE6ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(46)
    if wave04explored and exploredhex46 and seenwendy == False and week >= 8:
        imagebutton:
            focus_mask True
            idle "v06/hexE6idle.png"
            hover "v06/hexE6bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(46)
    if wave04explored and exploredhex46 and seenwendy and week >= 8:
        imagebutton:
            focus_mask True
            idle "v06/hexE6idle.png"
            hover "v06/hexE6chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(46)

    if wave05explored and exploredhex51 == False and week >= 11:
        imagebutton:
            focus_mask True
            idle "v071/hexF1idle.png"
            hover "v071/hexF1ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(51)
    if wave05explored and exploredhex51 and seencaravan == False and week >= 11:
        imagebutton:
            focus_mask True
            idle "v071/hexF1idle.png"
            hover "v071/hexF1bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(51)
    if wave05explored and exploredhex51 and seencaravan and choseheather == False and week >= 11:
        imagebutton:
            focus_mask True
            idle "v071/hexF1idle.png"
            hover "v071/hexF1ehover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(51)
    if wave05explored and exploredhex51 and seencaravan and choseheather and week >= 11:
        imagebutton:
            focus_mask True
            idle "v071/hexF1idle.png"
            hover "v071/hexF1chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(51)
    if wave05explored and clearedhex51 and choseheather and week >= 11:
        imagebutton:
            focus_mask True
            idle "v071/hexF1idle.png"
            hover "v071/hexF1dhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")
    if wave05explored and clearedhex51 and choseheather == False and week >= 11:
        imagebutton:
            focus_mask True
            idle "v071/hexF1idle.png"
            hover "v071/hexF1fhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")
    
    if wave05explored and exploredhex52 == False and week >= 11:
        imagebutton:
            focus_mask True
            idle "v072/hexF2idle.png"
            hover "v072/hexF2ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(52)
    if wave05explored and seencaravan == False and week >= 11:
        imagebutton:
            focus_mask True
            idle "v072/hexF2idle.png"
            hover "v072/hexF2bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(52)
    if wave05explored and seencaravan and week >= 11:
        imagebutton:
            focus_mask True
            idle "v072/hexF2idle.png"
            hover "v072/hexF2chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(52)
    if wave05explored and clearedhex52 and week >= 11:
        imagebutton:
            focus_mask True
            idle "v072/hexF2idle.png"
            hover "v072/hexF2dhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")
            
    if wave05explored and exploredhex53 == False and week >= 11:
        imagebutton:
            focus_mask True
            idle "v08/hexF3idle.png"
            hover "v08/hexF3ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(53)
    if wave05explored and exploredhex53 and week >= 11:
        imagebutton:
            focus_mask True
            idle "v08/hexF3idle.png"
            hover "v08/hexF3bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(53)

    if wave05explored and exploredhex54 == False and week >= 11:
        imagebutton:
            focus_mask True
            idle "v081/hexF4idle.png"
            hover "v081/hexF4ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(54)
    if wave05explored and exploredhex54 and week >= 11:
        imagebutton:
            focus_mask True
            idle "v081/hexF4idle.png"
            hover "v081/hexF4bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(54)

    if wave05explored and exploredhex55 == False and week >= 11:
        imagebutton:
            focus_mask True
            idle "v071/hexF5idle.png"
            hover "v071/hexF5ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(55)
    if wave05explored and exploredhex55 and week >= 11:
        imagebutton:
            focus_mask True
            idle "v071/hexF5idle.png"
            hover "v071/hexF5bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")

    if wave05explored and exploredhex56 == False and week >= 11:
        imagebutton:
            focus_mask True
            idle "v08/hexF6idle.png"
            hover "v08/hexF6ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(56)
    if wave05explored and exploredhex56 and week >= 11:
        imagebutton:
            focus_mask True
            idle "v08/hexF6idle.png"
            hover "v08/hexF6bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(56)

    if wave06explored and exploredhex61 == False and week >= 15:
        imagebutton:
            focus_mask True
            idle "v081/hexG1idle.png"
            hover "v081/hexG1ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(61)
    if wave06explored and exploredhex61 and week >= 15:
        imagebutton:
            focus_mask True
            idle "v081/hexG1idle.png"
            hover "v081/hexG1bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(61)

    if wave06explored and exploredhex62 == False and week >= 15:
        imagebutton:
            focus_mask True
            idle "v082/hexG2idle.png"
            hover "v082/hexG2ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(62)
    if wave06explored and exploredhex62 and week >= 15:
        imagebutton:
            focus_mask True
            idle "v082/hexG2idle.png"
            hover "v082/hexG2bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(62)

    if wave06explored and exploredhex64 == False and week >= 15:
        imagebutton:
            focus_mask True
            idle "v081/hexG4idle.png"
            hover "v081/hexG4ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(64)
    if wave06explored and exploredhex64 and week >= 15:
        imagebutton:
            focus_mask True
            idle "v081/hexG4idle.png"
            hover "v081/hexG4bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(64)
    
    if wave06explored and exploredhex65 == False and week >= 15:
        imagebutton:
            focus_mask True
            idle "v082/hexG5idle.png"
            hover "v082/hexG5ahover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(65)
    if wave06explored and exploredhex65 and seenmaragogo01 == False and clearedhex65 == False and week >= 15:
        imagebutton:
            focus_mask True
            idle "v082/hexG5idle.png"
            hover "v082/hexG5bhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(65)
    if wave06explored and exploredhex65 and seenmaragogo01 and clearedhex65 == False and week >= 15:
        imagebutton:
            focus_mask True
            idle "v082/hexG5idle.png"
            hover "v082/hexG5chover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Return(65)
    if wave06explored and clearedhex65 and week >= 15:
        imagebutton:
            focus_mask True
            idle "v082/hexG5idle.png"
            hover "v082/hexG5dhover.png" hovered Play("sound", "Sounds/rollover.mp3")
            action Jump ("ExploringMap")

    if knowcity and toldlenawall == False:
        imagebutton:
            focus_mask True
            idle "v06/hexG3idle.png"
            hover "v06/hexG3ahover.png"
            action Jump ("ExploringMap")
    if knowcity and toldlenawall:
        imagebutton:
            focus_mask True
            idle "v06/hexG3idle.png"
            hover "v08/hexG3bhover.png"
            action Jump ("ExploringMap")

$ hex = _return
show hexA0idle
show hexA1idle
show hexA2idle
show hexA3idle
if wave01explored:
    show hexB1idle
    show hexB2idle
    show hexB3idle
    show hexB4idle
    show hexB5idle
    show hexB6idle
    show hexB7idle
if wave02explored and week >= 4:
    show hexC1idle
    show hexC2idle
    show hexC3idle
    show hexC4idle
    show hexC5idle
    show hexC6idle
    show hexC7idle
if knowdeserttown and wave01explored:
    if wave02explored:
        hide hexc5idle
    show hexC5bidle
if (knowforwardops and wave02explored) or (successprisoner and wave01explored):   
    if wave02explored:
        hide hexc3idle
    show hexC3bidle
if wave03explored and week >= 6:
    show hexD1idle
    show hexD2idle
    show hexD3idle
    show hexD5idle
    show hexD4idle
    show hexD6idle
if wave04explored and week >= 8:
    show hexE1idle
    show hexE2idle
    if warriorcapture:
        show hexE3bidle
    if warriorcapture == False:
        show hexE3idle        
    show hexE4idle
    show hexE5idle
    show hexE6idle
if wave05explored and week >= 11:
    show hexF1idle    
    show hexF2idle
    show hexF3idle
    show hexF4idle
    show hexF5idle
    show hexF6idle
if wave06explored and week >= 15:
    show hexG1idle
    show hexG2idle
    show hexG4idle
    show hexG5idle

if knowcity:
    show hexG3idle
if hex == 17 and renpy.seen_image("hannityvictory02") and period == 1: 
    mc "I'll enter Trumpf City again. The easy way. Through the dank and dark sewers accompanied by the fearsome Black Widow."
    le "You mean Scarlett Johansson?"
    mc "Yeah, that actress."
    jump AvengersMissionNew    
if hex == 17 and lustwi >= 2:
    le "I really don't understand why you keep wanting to go there, but I guess it's your call..."
    if missionwi01 and donemissionwi01 == False and momcompound:
        mc "And I'll take Nancy with me this time. She has...err... keen sandstorm vision."
        $ withmo = True
if hex == 14 and mcbike:
    mc "And I'll go there on my own... With my OWN BIKE. Like the Lone Ranger."
    le "I won't allow it. This hex is too close to the compound for comfort. You need to be with an experienced scout."
    mc "What? But how am I ever going to bang... I mean discuss important matters with those hippies chicks then?"
    le "Not MY problem."
    if persistent.tipson:
        show hippytip at tips with dissolve
        pause
        hide hippytip    
    jump ExploringMap
if hex == 14 and hippiebella:
    be "Oh, I see, you want to see those sinning hippie chicks again..."
    mc "Purely out of professional curiosity."
    be "Well, NOT with MY rig, I told you!"
    mc "OK, OK. (I'd better get myself my own motorbike if I want to be able to bone those hot chicks...)"
    jump ExploringMap
if hex == 14 and hippiepenny:
    pe "Oh, I see, you want to see those stoned hippie chicks again..."
    mc "Purely out of professional curiosity."
    pe "Well, NOT with MY rig, I told you!"
    mc "OK, OK. (I'd better get myself my own motorbike if I want to be able to bone those hot chicks...)"
    jump ExploringMap
if hex == 46 and seenwendy and mcbike and period == 1:
    mc "And I'll go alone this time..."
    $ alone = True
    $ withnone = True
    jump Explore
if hex == 46 and seenwendy and mcbike == False and period == 1:
    mc "I should really try and get my own rig before going there so I can work for Wendy for a full day."
    jump ExploringMap
if hex == 46 and seenwendy and mcbike and period == 2:
    "It's too late in the day to start working for Wendy... Choose this hex in the mornings only."
    jump ExploringMap

if mcbike and bikepaid and not hex==01 and not hex==02 and not hex==03 and not hex==11 and not hex==12 and not hex==13 and not hex==14 and not hex==15 and not hex==16 and not hex==17:
    menu:
        "Go with your own rig":            
            le "Alright, Bella and Penny can take a day off then."
            $ alone = True
            jump MapGirlChoice
        "Accompany a scout":
            pass

$ d2rollwith = renpy.random.randint(1, 2)
if d2rollwith == 1:
    le "You'll go with Bella this time."
    $ withbe = True
if d2rollwith == 2:
    le "You'll go with Penny this time."
    $ withpe = True
if hex == 32 and rescuedmagnus and (mcbike == False or bikepaid == False) and girlsinharem >= 1 and withmo == False:
    mc "And I won't take any harem girl with me this time. This is a solo job. Mano-a-hulko."
    le "Fine, but you'd better come back and tell me that hex is CLEARED, you hear me?"
    $ withnone = True
    jump Explore

label MapGirlChoice:
if girlsinharem == 0:
    $ withnone = True

if (girlsinharem >= 2 or (girlsinharem == 1 and haremle == False)) and withmo == False:
    menu:
        "Zara is too far into her pregnancy." if haremza and pregzastart >= 4:
            jump MapGirlChoice
        "Take Zara with you" if haremza and pregzastart <= 3:
            $ withza = True
        "Angie is too far into her pregnancy." if hareman and preganstart >= 4:
            jump MapGirlChoice
        "Take Angie with you" if hareman and preganstart <= 3:
            $ withan = True
        "Take Cyrl with you" if haremcy:
            $ withcy = True
        "Nancy is too far into her pregnancy." if haremmo and pregmostart >= 4:
            jump MapGirlChoice
        "Take Nancy with you" if haremmo and pregmostart <= 3:
            $ withmo = True
        "Michiko is too far into her pregnancy." if haremmi and pregmistart >= 4:
            jump MapGirlChoice
        "Take Michiko with you" if haremmi and pregmistart <= 3:
            $ withmi = True
        "Take Ruby with you" if haremru:
            $ withru = True
        "Amy is too far into her pregnancy." if haremam and pregamstart >= 4:
            jump MapGirlChoice
        "Take Amy with you" if haremam and pregamstart <= 3:
            $ witham = True
        "Ayla is too far into her pregnancy." if haremay and pregaystart >= 4:
            jump MapGirlChoice
        "Take Ayla with you" if haremay and pregaystart <= 3:
            $ withay = True
        "Take Suki with you" if haremsu:
            $ withsu = True
        "Gwen is too far into her pregnancy." if haremgw and preggwstart >= 4:
            jump MapGirlChoice
        "Take Gwen with you" if haremgw and preggwstart <= 3:
            $ withgw = True
        "Take Marnie with you" if haremma:
            $ withma = True
        "Take Clara with you" if haremcl:
            $ withcl = True
        "Laurie is too far into her pregnancy." if haremla and preglastart >= 4:
            jump MapGirlChoice
        "Take Laurie with you" if haremla and preglastart <= 3:
            $ withla = True
        "Barbara is too far into her pregnancy." if haremba and pregbastart >= 4:
            jump MapGirlChoice
        "Take Barbara with you" if haremba and pregbastart <= 3:
            $ withba = True
        "Take Debra with you" if haremde:
            $ withde = True
        "Take Lena with you" if haremle and choselena == False:
            le "I can't leave the compound! I'm too important, I'm the Chief here, remember?"
            mc "Ah yeah, was just trying my luck, the button was available and..."
            le "Pick another option!"
            $ choselena = True
            jump MapGirlChoice
        "Don't take anyone":
            $ withnone = True
            pass
jump Explore
