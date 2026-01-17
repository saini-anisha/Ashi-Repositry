import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen_var.set(result)
        except:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen.get() + text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold", bd=10, relief=tk.SUNKEN)
screen.pack(fill=tk.X, padx=10, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for btn in row:
        b = tk.Button(frame, text=btn, font="lucida 15 bold", width=5, height=2)
        b.pack(side=tk.LEFT, padx=5, pady=5)
        b.bind("<Button-1>", click)

root.mainloop()
