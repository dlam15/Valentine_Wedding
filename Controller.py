import StartScreen
import Intro
import Game
import Conclusion
from characterSelectScreen import characterSelectScreenBegin

class Controller:
    #first we open start screen
    start = StartScreen.StartScreen()
    if start.startScreenBegin() == True:
        print("starting game")

    #returns path to images
    #[0] is non flipped (facing right)
    #[1] is flipped (facing left)
    pathToImages = characterSelectScreenBegin()
    Intro.Intro(pathToImages[0],pathToImages[1])
    Game.Game(pathToImages[0],pathToImages[1])
    end = Conclusion.Conclusion()
    end.conclusionScreenBegin()



#next we'll open character select
#we'll return vals to pass to game (which characters)

#then we'll play intro sequence

#then start game


#Call controller to start game
Controller()
