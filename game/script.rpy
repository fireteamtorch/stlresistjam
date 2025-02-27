# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")

define gui.text_font = "CARERRA-Jones.otf"
define gui.what_font = "CARERRA-Jones.otf"
define gui.interface_text_font = "CARERRA-Jones.otf"
define gui.glyph_font = "CARERRA-Jones.otf"


#define gui.interface_text_font = "The Black Pearl.ttf"
#define gui.glyph_font = "The Black Pearl.ttf"

#define gui.text_size = 40

init:
    $ frank = Character("Frank", image = "frank", color="#009900", what_color="#009900", what_font = "CARERRA-Jones.otf")
    $ claire = Character("Claire",image = "claire", color="#33ccff", what_color="#33ccff", what_font = "CARERRA-Jones.otf")
    $ bartender = Character("Bartender", color = "#dddcc5", what_color = "#dddcc5")

    $ ScaleClaire = 400
    $ ScaleFrank = 450
    $ ScaleCharles = 450

    $ PortraitScale = 1.0

    $ charles = Character("Charles", image = "charles", color="#FFA500", what_color="#FFA500", what_font = "CARERRA-Jones.otf")

    $ disFactor = 0.1

    $ elysia = Character("Elysia", image = "elysia", color="#e5e500", what_color="#e5e500", what_font = "CARERRA-Jones.otf")

    $ braxton = Character("Braxton", image = "braxton", color="#ff4c4c", what_color="#ff4c4c", what_font = "CARERRA-Jones.otf")
# The game starts here.

label start:
    image choicepic = im.Scale("Frankchoice.png", 768, 432)
    image grouppic = im.Scale("Grouppic.png", 768, 432)
    image bgBar = "bgSectionsEdit1080.png"
    image bgBarDay = "Bar-BG-Daytime.png"
    #image bgBarDay = im.Scale("Bar-BG-Daytime.png", 1280 , 720)
    image bgBarNight = "Bar-BG-Nighttime.png"
    
    #image bgCounterTop = "bgBarTop1080.png"
    image bgCounterTop = "tempBarCounter.png"
    
    image bgTeamTBA = "TeamTBA-Screen.png"
    image bgPaintedBlade = "PaintedBlade-Screen.png"
    image bgResistJam = "ResistJamScreen.png"
    image bgMadeInSTL = "MadeInSTL-Screen.png"

    #image claire sit = 'ClaireLook1.png'
    image claire sit = im.Scale("ClaireLook1.png", ScaleClaire, ScaleClaire)
    image side claire = im.Scale("tempClairePortrait.png", ScaleClaire * PortraitScale, ScaleClaire* PortraitScale)

    image claire angry = im.Scale("ClaireAngry1.png", ScaleClaire, ScaleClaire)
    image claire angry up = im.Scale("ClaireAngry2.png", ScaleClaire, ScaleClaire)
    #image claire angry up = 'ClaireAngry1.png'

    image claire look left = im.Scale("ClaireLook2.png", ScaleClaire, ScaleClaire)
    image claire sit lookLeft = im.Scale("ClaireLook2.png", ScaleClaire, ScaleClaire)
    #image claire look left = 'ClaireLook2.png'

    image claire look player = im.Scale("ClaireLook-Player.png", ScaleClaire, ScaleClaire)
    image claire sit lookPlayer = im.Scale("ClaireLook-Player.png", ScaleClaire, ScaleClaire)

    image claire happy = im.Scale("ClaireHappy.png", ScaleClaire, ScaleClaire)

    image claire happy player= im.Scale("ClaireHappy2.png", ScaleClaire, ScaleClaire)

    #image frank sit = "TruckerSmall.png"
    image frank sit = im.Scale("RegularFrank.png", ScaleFrank, ScaleFrank)

    image side frank = im.Scale("tempFrankPortrait.png", ScaleFrank * PortraitScale * 0.85, ScaleFrank * PortraitScale * 0.85)

    image frank sit beer lookPlayer= im.Scale("Frank-Beer-PLayer-Look.png", ScaleFrank, ScaleFrank)

    image frank sit beer lookRight = im.Scale("Frank-BeerLook1.png", ScaleFrank, ScaleFrank)
    image frank sit beer lookLeft = im.Scale("Frank-BeerLook2.png", ScaleFrank, ScaleFrank)

    image frank angry lookLeft = im.Scale("Frank-Angry2.png", ScaleFrank, ScaleFrank)
    image frank angry lookRight = im.Scale("Frank-Angry1.png", ScaleFrank, ScaleFrank)

    image frank smile = im.Scale("Frank-Smile1.png", ScaleFrank, ScaleFrank)
    image frank smile beer = im.Scale("Frank-Smile2.png", ScaleFrank, ScaleFrank)

    image frank sad = im.Scale("Frank-Sad1.png", ScaleFrank, ScaleFrank)
    #image frank smile = im.Scale("Frank-Smile1.png", ScaleFrank, ScaleFrank)
    
    image frank sad = im.Scale("Frank-Sad1.png", ScaleFrank, ScaleFrank)
    image frank sad no hat = im.Scale("Frank-Sad2.png", ScaleFrank, ScaleFrank)

    image frank drunk = im.Scale("Frank-BeerDrunk1.png", ScaleFrank, ScaleFrank)

    image frank drunk angry lookLeft = im.Scale("Frank-AngryDrunk2.png", ScaleFrank, ScaleFrank)
    image frank drunk angry lookRight = im.Scale("Frank-AngryDrunk1.png", ScaleFrank, ScaleFrank)

    image frank looking anim:
        #"Frank-BeerLook1.png"
        im.Scale("Frank-BeerLook1.png", ScaleFrank, ScaleFrank)
        pause 1.0
        #"Frank-BeerLook2.png"
        im.Scale("Frank-BeerLook2.png", ScaleFrank, ScaleFrank)
        pause 1.0
        repeat

    image frank drink anim:
        "TruckerSmallDrink.png"
        pause 1.0
        "TruckerSmall.png"
        pause 1.0
        repeat

    image charles sit = im.Scale("Charles-Player-Look.png", ScaleCharles, ScaleCharles)
    image charles sit lookLeft = im.Scale("Charles-Look-Left.png", ScaleCharles, ScaleCharles)
    image charles sit lookRight = im.Scale("Charles-Player-Look.png", ScaleCharles, ScaleCharles)
    image charles smile = im.Scale("Charles-Player-Look-Smile.png", ScaleCharles, ScaleCharles)

    image charles teased = im.Scale("Charles-Look-Teased.png", ScaleCharles, ScaleCharles)

    image charles explain = im.Scale("Charles-Explain.png", ScaleCharles, ScaleCharles)

    image charles sad = im.Scale("Charles-Sad.png", ScaleCharles, ScaleCharles)

    image side charles = im.Scale("tempCharlesPortrait.png", ScaleCharles * PortraitScale * 0.8, ScaleCharles* PortraitScale * 0.8)


    image braxton sit lookPlayer = im.Scale("Brock-PlayerLook.png", ScaleCharles, ScaleCharles)
    image braxton sit lookLeft = im.Scale("Brock-LookLeft.png", ScaleCharles, ScaleCharles)
    image braxton sit lookRight = im.Scale("Brock-LookRight.png", ScaleCharles, ScaleCharles)

    image braxton closed = im.Scale("Brock-Neutral-Eyes-Closed.png", ScaleCharles, ScaleCharles)
    image braxton sipping = im.Scale("Brock-Sipping-Beer.png", ScaleCharles, ScaleCharles)

    image braxton angry = im.Scale("Brock-Angry.png", ScaleCharles, ScaleCharles)

    image braxton smile = im.Scale("Brock-PlayerLook-Smile.png", ScaleCharles, ScaleCharles)
    image braxton smile lookRight = im.Scale("Brock-LookRight-Smile.png", ScaleCharles, ScaleCharles)

    image side braxton = im.Scale("tempBrockPortrait.png", ScaleCharles * PortraitScale * 0.8, ScaleCharles* PortraitScale * 0.8)

    image elysia sit lookLeft = im.Scale("Elysia-Look-Left.png", ScaleCharles, ScaleCharles)
    image elysia sit lookRight = im.Scale("Elysia-Look-Right.png", ScaleCharles, ScaleCharles)

    image elysia smile lookLeft = im.Scale("Elysia-Smile-Left.png", ScaleCharles, ScaleCharles)
    image elysia smile lookRight = im.Scale("Elysia-Smile-Right.png", ScaleCharles, ScaleCharles)
    image elysia smile lookPlayer = im.Scale("Elysia-Smile-Player.png", ScaleCharles, ScaleCharles)

    image elysia closed = im.Scale("Elysia-Eyes-Closed.png", ScaleCharles, ScaleCharles)

    image side elysia = im.Scale("tempElysiaPortrait.png", ScaleCharles * 0.8, ScaleCharles * 0.8)


    $ factorSeat = (0.1) * 0.85
    $ factorSeatOffset = 0.1
    $ factorSeatHeightOffset = -0.08

    transform Seat1:
        xcenter ((1 * factorSeat) + factorSeatOffset)
        yalign 0.25 + factorSeatHeightOffset

    transform Seat2:
        xcenter ((3 * factorSeat) + factorSeatOffset)
        yalign 0.25 + factorSeatHeightOffset

    transform Seat3:
        xcenter ((5 * factorSeat) + factorSeatOffset)
        yalign 0.25 + factorSeatHeightOffset
        
    transform Seat4:
        xcenter ((7 * factorSeat) + factorSeatOffset)
        yalign 0.25 + factorSeatHeightOffset
        
    transform Seat5:
        xcenter ((9 *factorSeat) + factorSeatOffset)
        yalign 0.25 + factorSeatHeightOffset



    transform Seat3half:
        xcenter ((6 *factorSeat) + factorSeatOffset)
        yalign 0.25 + factorSeatHeightOffset

    transform Seat4half:
        xcenter ((8 *factorSeat) + factorSeatOffset)
        yalign 0.25 + factorSeatHeightOffset




    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene black
    with dissolve
    
    stop music fadeout 1.0
    
    scene bgTeamTBA
    with fade
    pause 1.5
    scene bgPaintedBlade
    with fade
    pause 1.5
    scene bgResistJam
    with fade
    pause 1.5
    scene bgMadeInSTL
    with fade
    pause 1.5

    jump Day1Block
    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    #"Hello, world."

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
