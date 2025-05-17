label GwenDialogueRape:
if loc == "lab":
    show gwen06 with dissolve
if loc == "pool":
    show gwenpool03 with dissolve
label GwenDialogueRapeMenu01:
menu:
    "I want to apologize to you Gwen, it was all because the experiment went terribly wrong!" if missiongw01 == False:
        if loc == "lab":
            hide gwen06
            show gwen02
            with fastdissolve
        if loc == "pool":
            hide gwenpool03
            show gwenpool02 
            with fastdissolve
        gw "Yeah I know, Debra and her stupid dangerous crazy ideas, I'm sick of them!"
        mc "Next time, we should try and get back at her."
        if loc == "lab":
            hide gwen02
            show gwen03
            with fastdissolve
        if loc == "pool":
            hide gwenpool02
            show gwenpool01 
            with fastdissolve
        gw "How?"
        mc "I don't know yet, but I'll think of something I promise."
        window hide
        show missiongw01 at posmission
        $ renpy.pause(4.0, hard=True)
        hide missiongw01
        $ missiongw01 = True
        $ gwenapologized = True
        if loc == "lab":
            hide gwen03
            show gwen04
            with fastdissolve
        if loc == "pool":
            hide gwenpool01
            show gwenpool04 
            with fastdissolve
        gw "I can't wait to hear what you have in mind!"
        $ period += 1
        jump Bedroom            
    "It wasn't really me, I would never touch you like that!":
        if loc == "lab":
            hide gwen06
            show gwen05b
            with fastdissolve
        if loc == "pool":
            pass        
        gw "Oh, so now you're saying I'm too ugly to touch?"
        mc "Err... No, that's not what I meant! Your butt doesn't look big in that outfit, I mean it's big enough, fuck it, there's no way to win this one."
        if loc == "lab":
            hide gwen05b
            show gwen02
            with fastdissolve
        if loc == "pool":
            hide gwenpool04
            show gwenpool01
            with fastdissolve
        gw sidegw "That's right loser. Now if you'll excuse me, I need to talk to people who didn't rape me."
        if lustgw >=1:
            call LustMinusGwen
        if loc == "pool":
            hide gwenpool01 with dissolve
            mc "I might as well go for a swim now..."
            jump PoolOut
        if loc == "lab":
            hide gwen02 with dissolve
            jump Lab
            
           
label GwenDialogueJoe:
if loclab:
    show gwen01
if locpool:
    show gwenpool01
gw "What's this about?... It better not hurt!"
mc "It's about President Trumpf looking for the ultimate \"All American Alpha Couple\" to promote the... err... purity of the American Race."
if loc == "lab":
    hide gwen01
    show gwen04
    with fastdissolve
    gw "Oh, really? That sounds interesting..."
    hide gwen04
if loc == "pool":
    hide gwenpool01
    show gwenpool04
    with fastdissolve
    gw "Oh, really? That sounds interesting..."
    hide gwenpool04
if lustgw <=1:
    if loc == "pool":
        show gwenpool03
    if loc == "lab":        
        show gwen02
    gw "But I don't have time right now. I need to concentrate on my PhD."
    hide gwen02
    
if loc == "lab":
    hide gwen02
    $ spokegwen = True
    jump Lab
if loc == "pool":
    hide gwenpool03
    mc "I might as well go for a swim now..."
    jump PoolOut
    
