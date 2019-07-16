from uagame import Window
from time import sleep

# create window

window = Window("Hakin'", 600, 500)
window.set_font_color('white')
window.set_font_name("Comic sans")
window.set_bg_color("black")
window.set_font_size(35)

line_y = 0
string_height = window.get_font_height()

#display attemps left
window.draw_string("1 ATTEMPT REMAINING", 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

#Password list
window.draw_string("DOGE", 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string("PEPE", 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string("MEME", 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string("DUCK", 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string("WACK", 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height


#prompt user for password
guess = window.input_string('ENTER PASSWORD >', 0, line_y)

#clear window
window.clear()

# outcome
if guess == ("PEPE"):
    window.set_font_color('green')
    window.draw_string('ACCESS GRANTED', 0, 0)
    sleep(2)

elif guess == ("N/A"):
    window.set_font_color('blue')
    window.draw_string("WELCOME BACK, SIR.", 0, 0)
    sleep(2)

else:
    window.set_font_color('red') 
    window.draw_string('ACCESS DENIED', 0, 0)
    sleep(2)
    

    
#prompt end
window.set_font_color('white')
window.input_string('PRESS [ENTER] TO QUIT', 0, line_y)
sleep(3)


# close window
window.close()