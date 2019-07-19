from uagame import Window 
from time import sleep

window = Window("Terminal", 1000,500)
window.set_font_color("white")
window.set_font_name("Potra")
window.set_bg_color("black")
window.set_font_size(25)

line_y = 0
string_height = window.get_font_height()



window.draw_string("WELCOME AGENT", 0, line_y)
window.update()
sleep(1)
line_y = line_y + string_height

window.draw_string("YOU HAVE BEEN SELECTED FOR A TOP SECRET MISSION", 0, line_y)
window.update()
sleep(1)
line_y = line_y + string_height

window.draw_string("YOUR MISSION, SHOULD YOU CHOOSE TO ACCEPT IT,", 0, line_y)
window.update()
sleep(1)
line_y = line_y + string_height

window.draw_string("IS TO HACK INTO THE MAINFRAME BEFORE YOU, ", 0, line_y)
window.update()
sleep(1)
line_y = line_y + string_height

window.draw_string("AND DESTROY THE FILE LABELED 'LAUNCH CODES.'", 0, line_y)
window.update()
sleep(1)
line_y = line_y + string_height


awnser = window.input_string("DO YOU ACCEPT YOUR MISSION? >", 0, line_y)


if awnser == ("YES"):
    window.clear()
    
    
    window.draw_string("WE KNOW VERY LITTLE ABOUT THE SYSTEM YOU CURRENTLY FACE.", 0, line_y)
    window.update()
    sleep(1)
    line_y = line_y + string_height 
    
    window.draw_string("ONE OF THE FEW THINGS WE DO KNOW IS THAT YOU CAN TYPE 'COMMANDS' ", 0, line_y)
    window.update()
    sleep(1)
    line_y = line_y + string_height
    
    window.draw_string("AND YOU WILL GET A LIST OF COMMANDS THAT YOU CAN USE TO GET TO THE FILE AND DELETE IT.", 0, line_y)
    window.update()
    sleep(1)
    line_y = line_y + string_height    
    
    window.draw_string("GOOD LUCK AGENT. THIS MESSAGE WILL SELF-DESTRUCT IN 5 SECONDS.", 0, line_y)
    window.update()
    sleep(1)
    line_y = line_y + string_height 
    
    sleep(5)
    window.clear()
    
    game = True
    while game == True:
        CommmandInput = window.input_string(">", 0, line_y)
    
        if CommmandInput == ("COMMANDS"):
            
            window.draw_string("COMMAND LIST:", 0, line_y)
            window.update()
            sleep(1)
            line_y = line_y + string_height
            
            window.draw_string("      FIND", 0, line_y)
            window.update()
            sleep(1)
            line_y = line_y + string_height
            
            window.draw_string("     DEBUG", 0, line_y)
            window.update()
            sleep(1)
            line_y = line_y + string_height
            
            window.draw_string("      BACK", 0, line_y)
            window.update()
            sleep(1)
            line_y = line_y + string_height
            
            window.draw_string("    DELETE", 0, line_y)
            window.update()
            sleep(1)
            line_y = line_y + string_height
            
            window.draw_string("     GO-TO", 0, line_y)
            window.update()
            sleep(1)
            line_y = line_y + string_height
            
            
        elif CommmandInput == ("GO-TO"):
            
            destination = window.input_string("DESTINATION >", 0, line_y)
                
            if destination == ("LAUNCH CODES"):
                window.clear()
                code = window.input_string("ENTERY CODE >", 0, line_y)
                if code == ("1543"):
                    window.clear
                    window.set_font_color("green")
                    window.draw_string("ACCESS GRANTED", 0, line_y)
                    window.set_font_color("white")
                    window.update()
                    sleep(1)
                    line_y = line_y + string_height
                    
                    window.draw_string("LAUNCH CODE 1- 5478", 0, line_y)
                    window.update()
                    sleep(1)
                    line_y = line_y + string_height 
                   
                    window.draw_string("LAUNCH CODE 2- 4365", 0, line_y)
                    window.update()
                    sleep(1)
                    line_y = line_y + string_height
                   
                    window.draw_string("LUNCH CODE 3- 1369", 0, line_y)
                    window.update()
                    sleep(1)
                    line_y = line_y + string_height
                   
                    window.draw_string("LAUNCH CODE 4- 6342", 0, line_y)
                    window.update()
                    sleep(1)
                    line_y = line_y + string_height
                   
                    CommmandInput = window.input_string(">", 0, line_y)   
                    if CommmandInput == ("DELETE"):
                    
                        verify = window.input_string("VERIFY DELETE >", 0, line_y)
                        if verify == ("YES"):
                            window.draw_string("DELETING  FILE 'LAUNCH CODES' IN 3 SECONDS", 0, line_y)
                            sleep(3)
                            window.clear
                            
                            window.set_font_color("green")
                            window.draw_string("MISSION ACCOMPLISHED", 0, line_y)
                            sleep(6)
                            game = exit
                        
                    
                else:
                    window.clear
                    window.set_font_color("red")
                    window.draw_string("ACCESS DENIED", 0, line_y)
                    window.set_font_color("white")
                    window.update()
                    sleep(1)
                    line_y = line_y + string_height
            
            elif destination == ("CODE BLOCK"):
                
                window.draw_string("XLWV ULI WZMP NVNVH: 1234", 0, line_y)
                window.update()
                sleep(1)
                line_y = line_y + string_height
                
                window.draw_string("XLWV ULI HBHGVN: 1979", 0, line_y)
                window.update()
                sleep(1)
                line_y = line_y + string_height
                
                window.draw_string("XLWV ULI XFNKFGVL: 5643 ", 0, line_y)
                window.update()
                sleep(1)
                line_y = line_y + string_height
                
                window.draw_string("XLWV ULI IVW SVIIRMT: 0357", 0, line_y)
                window.update()
                sleep(1)
                line_y = line_y + string_height                
                
                window.draw_string("XLWV ULI SRGNVM I FH: 3267", 0, line_y)
                window.update()
                sleep(1)
                line_y = line_y + string_height 
                
                window.draw_string("XLWV ULI UZGSVL VTTH: 4827", 0, line_y)
                window.update()
                sleep(1)
                line_y = line_y + string_height  
                
                window.draw_string("XLWV ULI PIZKKB KZGB HVXIVG ULINFOZ: 1130", 0, line_y)
                window.update()
                sleep(1)
                line_y = line_y + string_height 
                
                window.draw_string("XLWV ULI TIZERGB UZOOH H3: 0615", 0, line_y)
                window.update()
                sleep(1)
                line_y = line_y + string_height  
                
                window.draw_string("XLWV ULI OZFMXS XLWVH: 1543", 0, line_y)
                window.update()
                sleep(1)
                line_y = line_y + string_height 
                
                window.draw_string("XLWV ULI HMZPV TZNV: 4236", 0, line_y)
                window.update()
                sleep(1)
                line_y = line_y + string_height 
                
                window.draw_string("XLWV ULI HRXP GFNVH: 8147", 0, line_y)
                window.update()
                sleep(1)
                line_y = line_y + string_height                
                
                
            else:
                window.draw_string("ERROR: LOCATION INVALID", 0, line_y)
                window.update()
                sleep(0.3)
                line_y = line_y + string_height
                
        elif CommmandInput == ("FIND"):
            shearch = window.input_string("LOCATE >", 0, line_y)
            if shearch == ("ENTERY CODE"):
                window.draw_string("'ENTERY CODE' FOUND: CODE BLOCK", 0, line_y)
                window.update()
                sleep(1)
                line_y = line_y + string_height
                
        elif CommmandInput == ("BACK"):
            window.clear()
                
            
                
                    
                    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    
     
    
    