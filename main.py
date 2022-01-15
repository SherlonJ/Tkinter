#   a214_login_window.py
import tkinter as tk

def test_my_button():
  root.config(background="sienna2")
  usrnm = ent_username.get()
  pswrd = ent_password.get()
  if usrnm == "admin"  and  pswrd == "qwerty12345":
   ent_username.pack_forget()
   ent_password.pack_forget()
   btn_login.pack_forget()
   lbl_username.pack_forget()
   lbl_password.pack_forget()
   display_special()
# create and show the special (restricted) app
def display_special():
 # authenticted - create the restricted app 
 root.title("Welcome to the Restricted Application")
 lbl_msg = tk.Label(frame_login,text="Welcome to the restricted application.", bg="sienna2")
 
 lbl_msg.config( font=("Arial", 18) ) # Mentioned in 2.1.4 Part 2
 lbl_msg.pack(pady=10)

 lbl_auth = tk.Label(frame_login,text="_The_Secret_Recipe_\nSpread peanut butter on slice of bread. \n Spread jelly on another slice. \n Put the slices together to form a sandwich", bg="sienna2")
 lbl_auth.pack(pady=10)
    
 btn_quit = tk.Button(frame_login, text="Quit", command=quit)
 btn_quit.pack(pady=10)




# main window
root = tk.Tk()
root.wm_geometry("400x400")

#-----more code...-----
root.title('Authorization')

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid()
frame_login.config(bg="sienna2") 

# create username label
lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()
lbl_username.pack(pady=10)
lbl_username.pack(padx=150)

# create username entry
ent_username = tk.Entry(frame_login, bd=3, show='')
ent_username.pack()

# create password label
lbl_password = tk.Label(frame_login, text='password:')
lbl_password.pack()
lbl_password.pack(pady=10)

# create passowrd entry
ent_password = tk.Entry(frame_login, bd=3, show='*')
ent_password.pack()

#create button 
btn_login = tk.Button(frame_login, text="Login", command=test_my_button)
btn_login.pack()
btn_login.pack(pady=10)





root.mainloop()
