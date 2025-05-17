label InventoryGallery:
call screen inventoryinterface
screen inventoryinterface:
    modal True
    add "Inventory/inventoryinterface01.png"
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryexit.png"
        hover "Inventory/inventoryexit.png"
        action [Hide ("inventoryinterface"), Return]

# PERSONAL ITEMS

    if camels >= 1:
        imagebutton:
            focus_mask True
            idle "Inventory/camelidle.png"
            hover "Inventory/camelhover.png"
            action [renpy.music.stop, Jump ("InventoryCamels")]   
        text "{font=Gui/goodtimes.ttf} [camels]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at poscamels

    if posingpouch:
        imagebutton:
            focus_mask True
            idle "Inventory/pouchidle.png"
            hover "Inventory/pouchhover.png"
            action [renpy.music.stop, Jump ("InventoryPouch")]   

    if mnagahat:
        imagebutton:
            focus_mask True
            idle "Inventory/hatidle.png"
            hover "Inventory/hathover.png"
            action [renpy.music.stop, Jump ("InventoryHat")]   

    if americacostume:
        imagebutton:
            focus_mask True
            idle "Inventory/americaidle.png"
            hover "Inventory/americahover.png"
            action [renpy.music.stop, Jump ("InventoryAmerica")]   

    if pendulum:
        $ pendulumusedleft = (3 - pendulumused)
        imagebutton:
            focus_mask True
            idle "Inventory/pendulumidle.png"
            hover "Inventory/pendulumhover.png"
            action [renpy.music.stop, Jump ("InventoryPendulum")]   
        text "{font=Gui/goodtimes.ttf} [pendulumusedleft]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at pospendulums
        if pendulumusedleft == 0:
            add "Inventory/used.png" xpos 904 ypos 117

    if mcbike:
        imagebutton:
            focus_mask True
            idle "Inventory/bikeidle.png"
            hover "Inventory/bikehover.png"
            action [renpy.music.stop, Jump ("InventoryBike")]   
            
    if talisman:
       imagebutton:
            focus_mask True
            idle "Inventory/talismanidle.png"
            hover "Inventory/talismanhover.png"
            action [renpy.music.stop, Jump ("InventoryTalisman")]
    if usedtalisman:
        add "Inventory/used.png" xpos 1304 ypos 117
            
    if diplomaticpass:
       imagebutton:
            focus_mask True
            idle "Inventory/passportidle.png"
            hover "Inventory/passporthover.png"
            action [renpy.music.stop, Jump ("InventoryPass")]

    if moustache:
       imagebutton:
            focus_mask True
            idle "Inventory/moustacheidle.png"
            hover "Inventory/moustachehover.png"
            action [renpy.music.stop, Jump ("InventoryMoustache")]
       # WEAPONS AND TOOLS    
    
    if darts >= 1:
        imagebutton:
            focus_mask True
            idle "Inventory/dartsidle.png"
            hover "Inventory/dartshover.png"
            action [renpy.music.stop, Jump ("InventoryDarts")]   
        text "{font=Gui/goodtimes.ttf} [darts]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posdarts
    
    if dagger:
        imagebutton:
            focus_mask True
            idle "Inventory/knifeidle.png"
            hover "Inventory/knifehover.png"
            action [renpy.music.stop, Jump ("InventoryDagger")]   

    if rifle:
        imagebutton:
            focus_mask True
            idle "Inventory/rifleidle.png"
            hover "Inventory/riflehover.png"
            action [renpy.music.stop, Jump ("InventoryRifle")]   

    if explosives:
        imagebutton:
            focus_mask True
            idle "Inventory/explosivesidle.png"
            hover "Inventory/explosiveshover.png"
            action [renpy.music.stop, Jump ("InventoryExplosives")]   
    
    if sniper:
        imagebutton:
            focus_mask True
            idle "Inventory/sniperidle.png"
            hover "Inventory/sniperhover.png"
            action [renpy.music.stop, Jump ("InventorySniper")]   

    if gasmask:
        imagebutton:
            focus_mask True
            idle "Inventory/maskidle.png"
            hover "Inventory/maskhover.png"
            action [renpy.music.stop, Jump ("InventoryMask")]   

    if repairkit:
        imagebutton:
            focus_mask True
            idle "Inventory/repairidle.png"
            hover "Inventory/repairhover.png"
            action [renpy.music.stop, Jump ("InventoryRepair")]   

    if lilbra:
        imagebutton:
            focus_mask True
            idle "Inventory/ballbraidle.png"
            hover "Inventory/ballbrahover.png"
            action [renpy.music.stop, Jump ("InventoryBallbra")]   

# GIRL GIFTS           

    if bouquet >= 1:
        imagebutton:
            focus_mask True
            idle "Inventory/bouquetidle.png"
            hover "Inventory/bouquethover.png"
            action [renpy.music.stop, Jump ("InventoryBouquet")]   
        text "{font=Gui/goodtimes.ttf} [bouquet]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posbouquets

    if pubichair >= 1:
        imagebutton:
            focus_mask True
            idle "Inventory/hairidle.png"
            hover "Inventory/hairhover.png"
            action [renpy.music.stop, Jump ("InventoryPubic")]   
        text "{font=Gui/goodtimes.ttf} [pubichair]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at pospubichairs

    if lingerie02:
         imagebutton:
            focus_mask True
            idle "Inventory/lingerieidle.png"
            hover "Inventory/lingeriehover.png"
            action [renpy.music.stop, Jump ("InventoryLingerie")]   

    if spliff:
        imagebutton:
            focus_mask True
            idle "Inventory/spliffidle.png"
            hover "Inventory/spliffhover.png"
            action [renpy.music.stop, Jump ("InventorySpliff")]   

    if necklace:
        imagebutton:
            focus_mask True
            idle "Inventory/necklaceidle.png"
            hover "Inventory/necklacehover.png"
            action [renpy.music.stop, Jump ("InventoryNecklace")]   

    if maidcostume:
        imagebutton:
            focus_mask True
            idle "Inventory/maididle.png"
            hover "Inventory/maidhover.png"
            action [renpy.music.stop, Jump ("InventoryMaid")]   

    if bikini01:
        imagebutton:
            focus_mask True
            idle "Inventory/bikiniidle.png"
            hover "Inventory/bikinihover.png"
            action [renpy.music.stop, Jump ("InventoryBikini")]   
    
    if holyoil:
        imagebutton:
            focus_mask True
            idle "Inventory/oilidle.png"
            hover "Inventory/oilhover.png"
            action [renpy.music.stop, Jump ("InventoryOil")]   

            
# MISSION ITEMS

    $ collectedstones = (8 - stonepieces)

    if missionge and successge == False:
        imagebutton:
            focus_mask True
            idle "Inventory/stoneidle.png"
            hover "Inventory/stonehover.png"
            action [renpy.music.stop, Jump ("InventoryStones")]   
        text "{font=Gui/goodtimes.ttf} [collectedstones]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posinventorystones
        
    $ totalgems = gem + hulkgem + aliendiamonds

    if totalgems >= 1:
        imagebutton:
            focus_mask True
            idle "Inventory/gemsidle.png"
            hover "Inventory/gemshover.png"
            action [renpy.music.stop, Jump ("InventoryGems")]   
        text "{font=Gui/goodtimes.ttf} [totalgems]{/font}" color "#ff0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posinventorygems

    if marvelcostume:
        imagebutton:
            focus_mask True
            idle "Inventory/marvelidle.png"
            hover "Inventory/marvelhover.png"
            action [renpy.music.stop, Jump ("InventoryMarvel")]   

    if nasafood:
        imagebutton:
            focus_mask True
            idle "Inventory/foodidle.png"
            hover "Inventory/foodhover.png"
            action [renpy.music.stop, Jump ("InventoryFood")]   

    if map:
        imagebutton:
            focus_mask True
            idle "Inventory/mapidle.png"
            hover "Inventory/maphover.png"
            action [renpy.music.stop, Jump ("InventoryMap")]   
    
    if donemissionop:
        imagebutton:
            focus_mask True
            idle "Inventory/scepteridle.png"
            hover "Inventory/scepterhover.png"
            action [renpy.music.stop, Jump ("InventoryScepter")]   

    if militiauniform:
        imagebutton:
            focus_mask True
            idle "Inventory/uniformidle.png"
            hover "Inventory/uniformhover.png"
            action [renpy.music.stop, Jump ("InventoryUniform")]   
                            
    if cactusmilk:
        imagebutton:
            focus_mask True
            idle "Inventory/milkidle.png"
            hover "Inventory/milkhover.png"
            action [renpy.music.stop, Jump ("InventoryMilk")]   

    if peetape:
        imagebutton:
            focus_mask True
            idle "Inventory/tapeidle.png"
            hover "Inventory/tapehover.png"
            action [renpy.music.stop, Jump ("InventoryTape")]   

    if mushrooms:
        imagebutton:
            focus_mask True
            idle "Inventory/mushroomidle.png"
            hover "Inventory/mushroomhover.png"
            action [renpy.music.stop, Jump ("InventoryMushroom")]   
            
return

label InventoryCamels:
call screen inventorycamel
screen inventorycamel:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/camels02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorycamel"), Jump ("InventoryGallery")]

label InventoryPouch:
call screen inventorypouch
screen inventorypouch:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/pouch02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorypouch"), Jump ("InventoryGallery")]

label InventoryAmerica:
call screen inventoryamerica
screen inventoryamerica:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/america02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventoryamerica"), Jump ("InventoryGallery")]

label InventoryHat:
call screen inventoryhat
screen inventoryhat:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/hat02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventoryhat"), Jump ("InventoryGallery")]

label InventoryPendulum:
call screen inventorypendulum
screen inventorypendulum:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/pendulum02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorypendulum"), Jump ("InventoryGallery")]

label InventoryBike:
call screen inventorybike
screen inventorybike:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/bike02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorybike"), Jump ("InventoryGallery")]

label InventoryTalisman:
call screen inventorytalisman
screen inventorytalisman:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/talisman02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorytalisman"), Jump ("InventoryGallery")]

label InventoryPass:
call screen inventorypass
screen inventorypass:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/pass02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorypass"), Jump ("InventoryGallery")]

label InventoryDarts:
call screen inventorydarts
screen inventorydarts:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/darts02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorydarts"), Jump ("InventoryGallery")]

label InventoryDagger:
call screen inventorydagger
screen inventorydagger:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/knife02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorydagger"), Jump ("InventoryGallery")]

label InventoryRifle:
call screen inventoryrifle
screen inventoryrifle:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/rifle02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventoryrifle"), Jump ("InventoryGallery")]

label InventoryExplosives:
call screen inventoryexplosives
screen inventoryexplosives:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/explosives02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventoryexplosives"), Jump ("InventoryGallery")]

label InventorySniper:
call screen inventorysniper
screen inventorysniper:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/sniper02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorysniper"), Jump ("InventoryGallery")]

label InventoryMask:
call screen inventorymask
screen inventorymask:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/mask02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorymask"), Jump ("InventoryGallery")]

label InventoryRepair:
call screen inventoryrepair
screen inventoryrepair:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/repair02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventoryrepair"), Jump ("InventoryGallery")]

label InventoryBallbra:
call screen inventorylilbra
screen inventorylilbra:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/ballbra02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorylilbra"), Jump ("InventoryGallery")]

label InventoryBouquet:
call screen inventorybouquet
screen inventorybouquet:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/bouquet02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorybouquet"), Jump ("InventoryGallery")]

label InventoryMarvel:
call screen inventorymarvel
screen inventorymarvel:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/marvel02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorymarvel"), Jump ("InventoryGallery")]

label InventoryLingerie:
call screen inventorylingerie
screen inventorylingerie:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/lingerie02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorylingerie"), Jump ("InventoryGallery")]

label InventoryOil:
call screen inventoryoil
screen inventoryoil:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/oil02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventoryoil"), Jump ("InventoryGallery")]

label InventoryMaid:
call screen inventorymaid
screen inventorymaid:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/maid02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorymaid"), Jump ("InventoryGallery")]

label InventoryNecklace:
call screen inventorynecklace
screen inventorynecklace:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/necklace02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorynecklace"), Jump ("InventoryGallery")]

label InventoryPubic:
call screen inventorypubic
screen inventorypubic:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/hair02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorypubic"), Jump ("InventoryGallery")]

label InventoryBikini:
call screen inventorybikini
screen inventorybikini:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/bikini02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorybikini"), Jump ("InventoryGallery")]

label InventorySpliff:
call screen inventoryspliff
screen inventoryspliff:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/spliff02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventoryspliff"), Jump ("InventoryGallery")]

label InventoryStones:
call screen inventorystones
screen inventorystones:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/stone02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorystones"), Jump ("InventoryGallery")]

label InventoryGems:
call screen inventorygems
screen inventorygems:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/gems02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorygems"), Jump ("InventoryGallery")]

label InventoryScepter:
call screen inventoryscepter
screen inventoryscepter:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/scepter02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventoryscepter"), Jump ("InventoryGallery")]

label InventoryMap:
call screen inventorymap
screen inventorymap:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/map02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorymap"), Jump ("InventoryGallery")]

label InventoryFood:
call screen inventoryfood
screen inventoryfood:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/food02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventoryfood"), Jump ("InventoryGallery")]

label InventoryMilk:
call screen inventorymilk
screen inventorymilk:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/milk02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorymilk"), Jump ("InventoryGallery")]

label InventoryUniform:
call screen inventoryuniform
screen inventoryuniform:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/uniform02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventoryuniform"), Jump ("InventoryGallery")]

label InventoryTape:
call screen inventorytape
screen inventorytape:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/tape02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorytape"), Jump ("InventoryGallery")]
        
label InventoryMushroom:
call screen inventorymushroom
screen inventorymushroom:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "Inventory/mushroom02.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorymushroom"), Jump ("InventoryGallery")]

label InventoryMoustache:
call screen inventorymoustache
screen inventorymoustache:
    modal True
    add "Inventory/inventoryinterface01.png"
    add "v082/frenchmoustache.png" xpos 800 ypos 350
    imagebutton:
        focus_mask True
        idle "Inventory/inventoryback.png"
        hover "Inventory/inventoryback.png"
        action [Hide ("inventorymoustache"), Jump ("InventoryGallery")]

