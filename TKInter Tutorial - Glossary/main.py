from tkinter import *


def click():
    enteredText = textentry.get()
    output.delete(0.0, END)
    try:
        definition = myDictionary[enteredText]
    except:
        definition = "Sorry, there is no word like that. Please try again."
    output.insert(END, definition)

window = Tk()
window.title("My Computer Science Glossary")
window.configure(background="black")

# photo = PhotoImage(file="photo1.png")
# Label(window, image=photo, bg="black").grid(row=0, column=0, sticky=E)
#
# Label(window, text="Enter the word you would like a definition for:", bg="black", fg="white",
#       font="none 12 bold")\
#     .grid(row=1, column=0, sticky=W)

textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

Button(window, text="SUBMIT", width=6, command=click).grid(row=3, column=0, sticky=W)

Label(window, text="\nDefinition:", bg="black", fg="white", font="none 12 bold")\
    .grid(row=4, column=0, sticky=W)

output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column = 0, columnspan = 2, sticky=W)

myDictionary = {
    'algorithm':'Step by step instructions to complete a task',
    'bug':'piece of code that causes a program to fail'
}

window.mainloop()
