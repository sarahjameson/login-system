from tkinter import *
import mysql.connector as mysql
import hashlib, uuid

db = mysql.connect(
    host = "127.0.0.1",
    user = "root",
    password = "Sugarboom1",
    database = "login_project"
)

mycur = db.cursor()

print(db)



######################################

def error_destroy():
    err.destroy()

######################################

def succ_destroy():
    succ.destroy()
    root1.destroy()

######################################

# shows when details are not entered as required
def error():
    global err
    err = Toplevel(root1)
    err.title("Error")
    err.geometry("200x100")
    Label(err, text = "All fields are required", fg = "red", font = "bold").pack()
    Label(err, text = "").pack()
    Button(err, text = "OK", bg= "grey", width = 8, height = 1, command = error_destroy).pack()

######################################

# shows when registration is successful
def success():
    global succ
    succ = Toplevel(root1)
    succ.title("Success")
    succ.geometry("200x100")
    Label(succ, text = "Registration successful", fg = "green", font = "bold").pack()
    Label(succ, text = "").pack()
    Button(succ, text = "OK", bg = "grey", width = 8, height = 1, command = succ_destroy).pack()

######################################

# register user
def register_user():
    global password_info
    username_info = username.get()
    password_info = password.get()
    email_info = email.get()
    if username_info == "":
        error()
    elif password_info == "":
        error()
    elif email_info == "":
        error()
    else:
        sql = "INSERT INTO users VALUES (%s, %s, %s)"
        values = (username_info, password_info, email_info)
        mycur.execute(sql, values)
        db.commit()
        Label(root1, text = "").pack()
        success()

######################################

# registration window
def registration():
    global root1
    root1 = Toplevel(root)
    root1.title("Registration")
    root1.geometry("300x300")
    global username
    global password
    global email
    Label(root1, text = "Register your account", bg = "pink", fg = "black", font = "bold", width = 300).pack()
    username = StringVar()
    password = StringVar()
    email = StringVar()
    Label(root1, text = "").pack()
    Label(root1, text = "Username :", font = "bold").pack()
    Entry(root1, textvariable = username).pack()
    Label(root1, text = "").pack()
    Label(root1, text = "Password :").pack()
    Entry(root1, textvariable = password, show = "*").pack()
    Label(root1, text = "").pack()
    Label(root1, text = "Email :").pack()
    Entry(root1, textvariable = email, font = "bold").pack()
    Label(root1, text = "").pack()
    Button(root1,text = "Register", bg="red", command = register_user).pack()
    Label(root1, text = "").pack()
 

######################################

# login window
def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Login")
    root2.geometry("300x300")
    global username_verify
    global password_verify
    Label(root2, text = "Login", bg = "pink", fg = "black", font = "bold", width = 300).pack()
    username_verify = StringVar()
    password_verify = StringVar()
    Label(root2, text = "").pack()
    Label(root2, text = "Username :", font="bold").pack()
    Entry(root2, textvariable = username_verify).pack()
    Label(root2, text = "").pack()
    Label(root2, text = "Password :").pack()
    Entry(root2, textvariable = password_verify, show = "*").pack()
    Label(root2, text = "").pack()
    Button(root2, text = "Login", bg = "red", command = login_verify).pack()
    Label(root2, text = "")

######################################

# destorys window
def logg_destroy():
    logg.destroy()
    root2.destroy()


######################################

# destroys window
def fail_destroy():
    fail.destroy()

######################################

# successful login window
def logged():
    global logg
    logg = Toplevel(root2)
    logg.title("Welcome")
    logg.geometry("200x100")
    Label(logg, text = f"Welcome {username_verify.get()}", fg = "green", font = "bold").pack()
    Label(logg, text = "").pack()
    Button(logg, text = "Log out", bg = "grey", width = 8, height = 1, command = logg_destroy).pack()

######################################

# failed window for invalid credentials
def failed():
    global fail
    fail = Toplevel(root2)
    fail.title("Invalid")
    fail.geometry("200x100")
    Label(fail, text = "Invalid credentials", fg = "red", font = "bold").pack()
    Label(fail, text = "").pack()
    Button(fail, text = "Ok", bg = "grey", width = 8, height = 1, command = fail_destroy).pack()

######################################

# login verify, check if person is in system
def login_verify():
    user_verify = username_verify.get()
    pas_verify = password_verify.get()
    sql = "SELECT * FROM users WHERE username = %s and password = %s"
    mycur.execute(sql,[(user_verify),(pas_verify)])
    results = mycur.fetchall()
    if results:
        for result in results:
            logged()
            break
    else:
        failed()



######################################

# first screen welcome
def main_screen():
    global root
    root = Tk()
    root.title("Sarah J's Login project")
    root.geometry("300x300")
    Label(root, text = "Welcome user. Press one!", font = "bold", bg = "pink", fg = "black", width = 300).pack()
    Label(root, text = "").pack()
    # login button
    Button(root, text = "Login", width = "15", height = "1", bg = "red", font = "bold", command = login).pack()
    Label(root, text = "").pack()
    # register button
    Button(root, text = "Registration", height = "1", width = "15", bg = "red", font = "bold", command = registration).pack()
    Label(root, text = "").pack()
    # exit button
    Button(root, text = "Exit", heigh = "1", width = "15", bg = "red", font = "bold", command = root.destroy).pack()
    Label(root, text = "").pack()

######################################


main_screen()
root.mainloop()