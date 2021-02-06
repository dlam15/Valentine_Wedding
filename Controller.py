import StartScreen


class Controller:
    #first we open start screen
    start = StartScreen.StartScreen()
    if start.startScreenBegin() == True:
        print("starting game")

#next we'll open character select
#we'll return vals to pass to game (which characters)

#then we'll play intro sequence

#then start game


#Call controller to start game
Controller()
