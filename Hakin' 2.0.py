from uagame import Window
from time import sleep

# create window

window = Window("Haking Terminal", 800, 500)
window.set_font_color('white')
window.set_font_name("potra")
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

#NOT the code
window.draw_string("20-8-5 3-15-4-5 12-15-12-19 9-19 16-15-19-19-9-2-12-5", 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height
#The code
window.draw_string("20-8-5 3-15-4-5 13-5-13-5 9-19 9-14-3-15-18-18-3-20", 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height
#MAY be the code
window.draw_string("20-8-5 3-15-4-5 1-9-7-9 9-19 14-15-20 16-15-19-19-9-2-12-5", 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height
#COULD be the code
window.draw_string("20-8-5 3-15-4-5 7-9-20-1 9-19 3-15-18-18-3-20", 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

#prompt user for password
guess = window.input_string('ENTER PASSWORD >', 0, line_y)

#clear window
window.clear()

# outcome
if guess == ("GITA"):
    window.set_font_color('green')
    window.draw_string('ACCESS GRANTED', 0, 0)

else:
    window.set_font_color('red') 
    window.draw_string('ACCESS DENIED', 0, 0)

#prompt end
window.set_font_color('white')
window.input_string('PRESS [ENTER] TO QUIT', 0, line_y)
sleep(3)


# close window
window.close()