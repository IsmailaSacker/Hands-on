import tkinter as tk
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Calculator App")
        
        # Change the background color of the layout
        root.configure(bg='grey')
        
        # List of basic arithmetic operators
        self.operators = ["/", "*", "+", "-"]
        
        # List of scientific function names
        self.scientific_functions = ["sin", "cos", "tan", "exp", "log", "sqrt", "ln"]
        
        # Variables to track the last action
        self.last_was_operator = None
        self.last_button = None
        
        # StringVar to store and display the calculation
        self.solution = tk.StringVar()
        
        # Create the user interface
        self.create_ui()

    def create_ui(self):
        # Entry widget to display the calculation with a black background
        self.solution_entry = tk.Entry(self.root, textvariable=self.solution, font=('Helvetica', 20), bd=10, insertwidth=4, borderwidth=6, bg='grey', fg='white')
        self.solution_entry.grid(row=0, column=0, columnspan=4, sticky='nsew')
        
        # List of buttons layout
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
            ["sin", "cos", "tan", "exp"],
            ["log", "sqrt", "AC", " "],
            ["ln", "(", ")", "="]
        ]
        
        # Create buttons and adjust the layout with grey background and the button text to white
        for i, row in enumerate(buttons):
            for j, label in enumerate(row):
                button = tk.Button(self.root, text=label, padx=20, pady=20, font=('Helvetica', 15),fg='white', bg='grey', command=lambda lbl=label: self.on_button_press(lbl))
                button.grid(row=i + 1, column=j, sticky='nsew')
                
                # Adjust layout weights
                self.root.grid_rowconfigure(i + 1, weight=1)
                self.root.grid_columnconfigure(j, weight=1)
                
        # Configure layout weights for the display textbox
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
                
        # Set focus to the display textbox upon startup
        self.solution_entry.focus_set()
                
    def on_button_press(self, button_text):
        current = self.solution.get()
        
        if button_text == 'C' or button_text == 'AC':
            # Clear the display
            self.solution.set("")
        elif button_text in self.scientific_functions:
            # Append the scientific function to the expression
            self.solution.set(current + button_text + "(")
        elif button_text == "=":
            try:
                # Evaluate the expression and display the result
                result = self.calculate_result(current)
                self.solution.set(result)
            except:
                self.solution.set("Error")
        else:
            # Append the pressed button to the expression
            new_text = current + button_text
            self.solution.set(new_text)
        
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators
        
    def calculate_result(self, expression):
        try:
            # Replace scientific function names with "math." prefix for evaluation
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
