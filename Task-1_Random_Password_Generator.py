##################################################################################################################################################################
                                                                #CODE-CLAUSE INTERNSHIP 
                                                      #RANDOM PASSWORD GENERATOR BY VATALA PHALGUN

##################################################################################################################################################################

# Importing the Necessary Libraries
import random
import string
from tkinter import *
import pyperclip

# Initializing the Window
root = Tk()
root.geometry("400x350")  # Setting the Window Size
root.maxsize(400, 350)
root.minsize(400, 350)

# Setting the Window Title
root.title("RANDOM PASSWORD GENERATOR")

# Creating Variable to Store the Generated Password
output_pass = StringVar()

# Creating a list of all Possible Characters
all_combi = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]

# Defining a Function to Generate the Password
def randPassGen():
  
  # Creating Empty String
  password = ""

  # Looping Over the Specified Length of the Password
  for y in range(pass_len.get()):

    # Choosing a Random Character from the List of Possible Characters
    char_type = random.choice(all_combi)

    # Appending the Random Character to the Password String
    password += random.choice(char_type)

  # Setting the value of the Output_Pass Variable to the Generated Password
  output_pass.set(password)

# Defining a function to Copy the Generated Password to the Clipboard
def copyPass():

  # Copying the Value of the Output_pass Variable to the Clipboard
  pyperclip.copy(output_pass.get())

# Creating a Label to Display the Password Length
pass_head = Label(root, text="Set Your Password Length: ", font="ComicSansMS 12 ", fg="red", bg="yellow")
pass_head.pack(pady=10)  # Pack the Label in the Window

# Creating an Integer Variable to Store the Input of the Password Length
pass_len = IntVar()

# Creating a Spinbox to Allow the User to Input the Password Length
length = Spinbox(root, from_=4, to_=32, textvariable=pass_len, width=24, font="ComicSansMS 16")
length.pack()  # Pack the Spinbox in the Window

# Creating a Button to Generate the Password
Button(root, command=randPassGen, text="Generate", font="ComicSansMS 10", bg="green", fg="black", activebackground="black", padx=5, pady=5).pack(pady=20) 

# Creating a Label to Display the Generated Password
pass_label = Label(root, text="Here is Your Password:", font="ComicSansMS 12 ", fg="red", bg="yellow")
pass_label.pack(pady="30 10")

# Creating an Entry to Display the Generated Password
Entry(root, textvariable=output_pass, width=24, font="ComicSansMS 16").pack()  # Pack the entry in the window

# Creating a Button to Copy the Password to the Clipboard
Button(root, text="Copy to Clipboard", command=copyPass, font="ComicSansMS 10", bg="green", fg="black", activebackground="black", padx=5, pady=5).pack(pady=20)

# Running the Main Loop
root.mainloop()

##################################################################################################################################################################