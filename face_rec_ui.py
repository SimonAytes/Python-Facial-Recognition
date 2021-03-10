import tkinter as tk #User-interface package

#GLOBAL VARIABLES
COLOR_BG = "#212121"
COLOR_FG = "#272727"

#Create an application window
window = tk.Tk()
window.title("Facial Recognition (v0.1.0)")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

"""#Create a text element inside the 
greeting = tk.Label(text = "hello world!")
#Resize the window to fit your elements
greeting.pack()"""

###BUTTON FRAME###
#Create the button frame
frm_button_content = tk.Frame(master=window, width=100, height=100, bg=COLOR_BG)
frm_button_content.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#Create the button frame title
lbl_button_header = tk.Label(master=frm_button_content, text = "Main Menu", bg=COLOR_BG)
lbl_button_header.config(font = ("Helvetica", 30, "bold"), foreground="#FFFFFF")
lbl_button_header.pack()

#Create Face Profile Button
btn_new_profile = tk.Button(frm_button_content, text="Create Face Profile", highlightbackground=COLOR_BG)
btn_new_profile.config(width=20, bg = COLOR_BG)
#Process Image Button
btn_process_img = tk.Button(frm_button_content, text="Process Image", highlightbackground=COLOR_BG)
btn_process_img.config(width=20)
#Remove Profile Button
btn_rm_profile = tk.Button(frm_button_content, text="Remove Profile", highlightbackground=COLOR_BG)
btn_rm_profile.config(width=20)
#List All Profiles Button
btn_list_profiles = tk.Button(frm_button_content, text="List All Profiles", highlightbackground=COLOR_BG)
btn_list_profiles.config(width=20)
#Quit Program Button
btn_quit_prog = tk.Button(frm_button_content, text="Quit", highlightbackground=COLOR_BG)
btn_quit_prog.config(width=10)

#Pack Buttons
btn_new_profile.pack()
btn_process_img.pack()
btn_rm_profile.pack()
btn_list_profiles.pack()
btn_quit_prog.pack()

###CONTENT FRAME###
#Create the content frame
frm_main_content = tk.Frame(master=window, width=200, bg=COLOR_FG)
frm_main_content.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

btn_main_img = tk.Button(master=frm_main_content, text="This Is An Image!", highlightbackground = COLOR_FG)
btn_main_img.config(width=20, height=10)

#Add Title
lbl_content_title = tk.Label(master=frm_main_content, text = "Facial Recognition", bg = COLOR_FG)
lbl_content_title.config(font=("Helvetica", 50, "bold"))
#Add Subtitle
lbl_content_subtitle = tk.Label(master=frm_main_content, text = "(v0.1.0)", bg = COLOR_FG)
lbl_content_subtitle.config(font=("Helvetica", 30, "italic"))

#Pack labels
btn_main_img.pack()
lbl_content_title.pack()
lbl_content_subtitle.pack()

#Add Subtitle
lbl1 = tk.Label(master=frm_main_content, text = "(v0.1.0)", bg = COLOR_FG)
lbl1.config(font=("Helvetica", 30, "italic"))

#Run tkinter's event loop and keep window open/active
window.mainloop()