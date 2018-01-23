import pyautogui as pg
import time
import webbrowser

points = 0

# Question
answer = pg.prompt(
"""
What trait do you value the most?
a) Loyalty
b) Kindness
c) Adventurousness
d) Cunning
"""
    )
pg.alert("You chose " + answer)

#answer points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4

# Question    

answer = pg.prompt(
"""
What infuriates you the most?
a) Stealing
b) Prejudice
c) Gossiping
d) Rewarding the undeserving
"""
    )
pg.alert("You chose " + answer)

#answer points
if answer == "a":
    points += 3
elif answer == "b":
    points += 1
elif answer == "c":
    points += 4
elif answer == "d":
    points += 2

# Question    

answer = pg.prompt(
"""
To reach your difficult goals you are most likely to . . .
a) Ask someone for help
b) Despair that you will never achieve them
c) Give up on your dreams
d) Buckle down and get to work
"""
    )
pg.alert("You chose " + answer)

#answer points
if answer == "a":
    points += 2
elif answer == "b":
    points += 3
elif answer == "c":
    points += 4
elif answer == "d":
    points += 1

#End of Survey

pg.alert("You are . . ." )
#Most Hufflepuff
if points <= 3:
    pg.alert ("Completely Hufflepuff! You can be my friend.")
    webbrowser.open("https://img00.deviantart.net/1df0/i/2014/252/9/9/hd_hufflepuff_traits_wallpaper_by_emily_corene-d7ylice.jpg")
#Second to most Hufflepuff
elif points > 3 and points <= 6:
    pg.alert ("Pretty darn Hufflepuff! Congrats!")
    webbrowser.open("https://vignette.wikia.nocookie.net/harrypotter/images/5/50/0.51_Hufflepuff_Crest_Transparent.png/revision/latest/scale-to-width-down/350?cb=20161020182518")
#Second to least Hufflepuff
elif points > 6 and points <= 9:
    pg.alert ("Probably not a hufflepuff. Perhaps a different House?")
    webbrowser.open("https://i1.wp.com/www.tor.com/wp-content/uploads/2014/12/hogwarts-houses3.jpg?fit=475%2C+9999&crop=0%2C0%2C100%2C356px&ssl=1")
#Not Hufflepuff
elif points > 9 and points <= 16:
    pg. alert ("Oh you're not a Huffepuff. Get out.")
    webbrowser.open("https://i.pinimg.com/originals/c8/ec/a0/c8eca0c24ac59100a45f7952069197bb.jpg")
