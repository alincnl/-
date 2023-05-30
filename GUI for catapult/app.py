#DearPyGUI Imports
import dearpygui.dearpygui as dpg

#window object settings
#set_main_window_size(540, 720)
dpg.window(width = 540, height = 720)
#dpg.set_global_font_scale(1.25)
#set_theme("Gold")
#set_style_window_padding(30,30)

with dpg.window(label = "Simple SMS Spam Filter", width=520, height=677):
    print("GUI is running...")
    set_window_pos("Simple SMS Spam Filter", 0, 0)

    #image logo
    dpg.add_drawing("logo", width=520, height=290) #create some space for the image

    dpg.add_separator()
    dpg.add_spacing(count=12)
    #text instructions
    dpg.add_text("Please enter an SMS message of your choice to check if it's spam or not", color=[232,163,33])
    dpg.add_spacing(count=12)
    #collect input
    dpg.add_input_text("Input", width=415, default_value="type message here!")
    dpg.add_spacing(count=12)
    #action button
    dpg.add_button("Check", callback=lambda x,y:check_spam(pred))

#place the image inside the space
dpg.draw_image("logo", "bububu.png", [0, 240])

#IF THE PREVIOUS LINE OF CODE TRIGGERS AN ERRROR TRY
#draw_image("logo", "logo_spamFilter.png", [0,0], [458,192])

dpg.start_dearpygui()
print("Bye Bye, GUI")
