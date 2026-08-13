from kivy.app import App
from kivy.uix.widget import Widget


class Calculator(Widget):

    def calculation(self, input_value):
        all_operator = ["+", "-", "*", "/", "%"]

        textbox = self.ids.text_box.text

        if input_value == "C":
            textbox = ""

        elif input_value == "<<":
            textbox = textbox[:-1]

        elif input_value == "=":
            try:
                textbox = str(eval(textbox))
            except:
                textbox = "Error"

        elif input_value == "." and "." in textbox:
            pass

        elif textbox == "0" and input_value != "." and input_value not in all_operator:
            textbox = input_value

        elif input_value in all_operator:
            if textbox and textbox[-1] not in all_operator and textbox[-1] != ".":
                textbox += input_value

        elif input_value == "+/-":
            try:
                textbox = str(-float(textbox))
                if textbox.endswith(".0"):
                    textbox = textbox[:-2]
            except:
                pass

        else:
            textbox += input_value

        if textbox == "":
            self.ids.text_box.text = "0"
        else:
            self.ids.text_box.text = textbox


class CalculatorApp(App):
    def build(self):
        return Calculator()


if __name__ == "__main__":
    CalculatorApp().run()
