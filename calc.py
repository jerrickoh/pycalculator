import tkinter as tk

def button_click(value):
    if value == "Clear":
        entry.delete(0, tk.END)
    elif value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except ZeroDivisionError:
            entry.delete(0, tk.END)
            entry.insert(0, "Error: Division by Zero")
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    else:
        entry.insert(tk.END, value)

# Create a window
window = tk.Tk()
window.title("PyCalculator")

# Create an entry field
entry = tk.Entry(window, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "Clear", "=", "+",
]

# Add buttons to the window
for row in range(1, 5):
    for col in range(4):
        text = buttons[(row - 1) * 4 + col]
        button = tk.Button(window, text=text, padx=20, pady=10, command=lambda v=text: button_click(v), bg="#E6E6E6", fg="black")
        button.grid(row=row, column=col, padx=5, pady=5)

window.mainloop()
