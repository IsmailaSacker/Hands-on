import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# print("happy for you")

class MainApp(App):
    def build(self):
        self.icon = "cal1_icon.png"
        self.operators = ["/", "*","+", "-"]
        self.last_was_operator = None
        self.last_button = None
        
        #creating layout of the screen
        main_layout = BoxLayout(orientation = "vertical")
        
        #creating a screen for the calculations
        self.solution = TextInput(background_color = "black", foreground_color = "white", multiline = False, halign = "right", font_size = 56, readonly = True)
        
        #creating a nested array to hold the number buttons and the operators
        main_layout.add_widget(self.solution)
        button = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
            
        ]
        
        #putting label on each buttons and adjust it to put the screen
        for row in button:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text = label, font_size = 30, background_color = "grey",
                    pos_hint = {"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press = self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        #making the equal button fit the screen returning the main layout
        equal_button = Button(
            text = "=", font_size = 30, background_color = "grey",
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
        )
        equal_button.bind(on_press = self.on_solution)
        main_layout.add_widget(equal_button)
        
        return main_layout
    
    #let the number that is pressed to show on the textbox
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        
        #this will clear the screen when the C button is pressed
        if button_text == 'C':
            self.solution.text = ""
            
        else:
            #when two or more operator nothing should show on the screen
            if current and(
                self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                #this should hold any button that is pressed and perform any operations that is pressed to the button
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators
    #this will pass the result to the textbox
    def on_solution(self, instance):
        text = self.solution.text
        if text:
            #convert the final result to the  string and display
            solution = str(eval(self.solution.text))
            self.solution.text = solution
        
if __name__ == "__main__":
    app = MainApp()
    app.run()