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

    #next we'll open character select
    #returns path to images
    #[0] is character1
    #[1] is character2
    pathToImages = characterSelectScreenBegin()

    #then we'll play intro sequence
    Intro.Intro(pathToImages[0],pathToImages[1])

    #then start game
    Game.Game(pathToImages[0],pathToImages[1])

    
    Conclusion.Conclusion(pathToImages[0],pathToImages[1])

    pygame.quit()










#Call controller to start game
Controller()
