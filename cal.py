import tkinter as tk

def is_valid_expression(expr):
    allowed_chars = "0123456789+-*/.() "
    for ch in expr:
        if ch not in allowed_chars:
            return False
    return True

def contains_division_by_zero(expr):
    expr_no_spaces = expr.replace(" ", "")
    if "/0" in expr_no_spaces:
        return True
    return False

def safe_eval(expr):
    if not is_valid_expression(expr):
        return "Error: Invalid characters"
    if contains_division_by_zero(expr):
        return "Error: Division by zero"
    return str(eval(expr))

def click(event):
    current = entry.get()
    text = event.widget.cget("text")
    
    if text == "=":
        if current.strip() == "":
            entry.delete(0, tk.END)
            entry.insert(0, "Error: Empty input")
        else:
            result = safe_eval(current)
            entry.delete(0, tk.END)
            entry.insert(0, result)
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Basic Calculator")

entry = tk.Entry(root, font="Arial 20", bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        b = tk.Button(frame, text=btn, font="Arial 18", relief=tk.GROOVE)
        b.pack(side="left", expand=True, fill="both")
        b.bind("<Button-1>", click)

root.mainloop()
