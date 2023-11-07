import tkinter as tk
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Calculator")
        
        self.operators = ["/", "*", "+", "-"]
        self.scientific_functions = ["sin", "cos", "tan", "exp", "log", "sqrt"]
        self.last_was_operator = None
        self.last_button = None
        
        self.solution = tk.StringVar()
        
        self.create_ui()

    def create_ui(self):
        self.solution_entry = tk.Entry(self.root, textvariable=self.solution, font=('Helvetica', 20), bd=10, insertwidth=4, borderwidth=6)
        self.solution_entry.grid(row=0, column=0, columnspan=4, sticky='nsew')
        
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
            ["sin", "cos", "tan", "exp"],
            ["log", "sqrt", "=", " "]
        ]
        
        for i, row in enumerate(buttons):
            for j, label in enumerate(row):
                button = tk.Button(self.root, text=label, padx=20, pady=20, font=('Helvetica', 15), command=lambda lbl=label: self.on_button_press(lbl))
                button.grid(row=i + 1, column=j, sticky='nsew')
                
                self.root.grid_rowconfigure(i + 1, weight=1)
                self.root.grid_columnconfigure(j, weight=1)
                
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
                
    def on_button_press(self, button_text):
        current = self.solution.get()
        
        if button_text == 'C':
            self.solution.set("")
        elif button_text in self.scientific_functions:
            self.solution.set(current + button_text + "(")
        elif button_text == "=":
            try:
                result = self.calculate_result(current)
                self.solution.set(result)
            except:
                self.solution.set("Error")
        else:
            new_text = current + button_text
            self.solution.set(new_text)
        
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators
        
    def calculate_result(self, expression):
        try:
            for func in self.scientific_functions:
                expression = expression.replace(func, "math." + func)
            result = eval(expression)
            return result
        except:
            return "Error"

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
