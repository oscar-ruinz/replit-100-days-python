import tkinter as tk

window = tk.Tk()
window.title("Calculator") 
window.geometry("300x300") 

label = 0

def buttonChoice(number):
  hello["text"] = number


def operatorChoice(opChoice):
  global operator, lastnumber
  operator = opChoice
  lastnumber = int(hello["text"])
  hello["text"] = 0

def calc():
  global operator, lastnumber, answer
  if operator == "+":
    answer = lastnumber + hello["text"]
  elif operator == "-":
    answer = lastnumber - hello["text"]
  elif operator == "/":
    answer = lastnumber / hello["text"]
  elif operator == "*":
    answer = lastnumber * hello["text"]
  lastnumber = answer
  hello["text"] = lastnumber
  

hello = tk.Label(text = label)
hello.grid(row=0, column=1) # New line here

#First Row
button = tk.Button(text = "1", command = lambda: buttonChoice(1)).grid(row=1, column=0)
button = tk.Button(text = "2", command = lambda: buttonChoice(2)).grid(row=1, column=1)
button = tk.Button(text = "3", command = lambda: buttonChoice(3)).grid(row=1, column=2)
button = tk.Button(text = "+", command = lambda: operatorChoice("+")).grid(row=1, column=3)
button = tk.Button(text = "-", command = lambda: operatorChoice("-")).grid(row=1, column=4)

#Second row
button = tk.Button(text = "4", command = lambda: buttonChoice(4)).grid(row=2, column=0)
button = tk.Button(text = "5", command = lambda: buttonChoice(5)).grid(row=2, column=1)
button = tk.Button(text = "6", command = lambda: buttonChoice(6)).grid(row=2, column=2)
button = tk.Button(text = "*", command = lambda: operatorChoice("*")).grid(row=2, column=3)
button = tk.Button(text = "/", command = lambda: operatorChoice("/")).grid(row=2, column=4)

#Third row
button = tk.Button(text = "7", command = lambda: buttonChoice(7)).grid(row=3, column=0)
button = tk.Button(text = "8", command = lambda: buttonChoice(8)).grid(row=3, column=1)
button = tk.Button(text = "9", command = lambda: buttonChoice(9)).grid(row=3, column=2)

#Fourth row
button = tk.Button(text = "0", command = lambda: buttonChoice(0)).grid(row=4, column=1)
button = tk.Button(text = "=", command = lambda: calc()).grid(row=4, column=3)
tk.mainloop()