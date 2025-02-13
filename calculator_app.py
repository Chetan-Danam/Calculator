import tkinter as tk

# Function to update the input field with the button clicked
def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)  # Clear current input
    entry.insert(tk.END, current_text + str(value))

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())  # Use eval to calculate the result of the entered expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Initialize the main application window
app = tk.Tk()
app.title("Calculator")
app.geometry("400x600")

# Create the input field (display screen)
entry = tk.Entry(app, width=16, font=('Arial', 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(app, text=text, width=10, height=3, font=('Arial', 18), command=calculate)
    else:
        button = tk.Button(app, text=text, width=10, height=3, font=('Arial', 18), command=lambda value=text: button_click(value))
    button.grid(row=row, column=col, padx=5, pady=5)

# Add the clear button
clear_button = tk.Button(app, text="C", width=10, height=3, font=('Arial', 18), command=clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Start the Tkinter event loop
app.mainloop()
