import os
try:
    import kivy
except:
    os.system('easy_install kivy')
    import kivy
    pass
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.spacing=1
        self.Label = Label(text="Use / to denote an unknown")
        self.add_widget(self.Label)
        self.BlankLabel = Label(text="Use ` to denote a value to work out")
        self.add_widget(self.BlankLabel)
        self.sLabel = Label(text="Displacement/m")
        self.add_widget(self.sLabel)
        self.sTextInput = TextInput(font_size=35, size_hint_y=None, height=50)
        self.add_widget(self.sTextInput)
        self.uLabel = Label(text="Initial Velocity/ms^-1")
        self.add_widget(self.uLabel)
        self.uTextInput = TextInput(font_size=35, size_hint_y=None, height=50)
        self.add_widget(self.uTextInput)
        self.vLabel = Label(text="Final Velocity/ms^-1")
        self.add_widget(self.vLabel)
        self.vTextInput = TextInput(font_size=35, size_hint_y=None, height=50)
        self.add_widget(self.vTextInput)
        self.aLabel = Label(text="Acceleration/ms^-2")
        self.add_widget(self.aLabel)
        self.aTextInput = TextInput(font_size=35, size_hint_y=None, height=50)
        self.add_widget(self.aTextInput)
        self.tLabel = Label(text="Time/s")
        self.add_widget(self.tLabel)
        self.tTextInput = TextInput(font_size=35, size_hint_y=None, height=50)
        self.add_widget(self.tTextInput)
        self.submitButton = Button(text="Submit`")
        self.submitButton.bind(on_press=self.submitPressed)
        self.add_widget(self.submitButton)
        s = NumericProperty()
        u = NumericProperty()
        v = NumericProperty()
        a = NumericProperty()
        t = NumericProperty()
    def submitPressed(self, instance):
        def show_popup(message):
            layout = GridLayout(cols = 1, padding = 10) 
            popupLabel = Label(text =message) 
            closeButton = Button(text ="Close") 
            layout.add_widget(popupLabel) 
            layout.add_widget(closeButton)        
            popup = Popup(title ='Answer', content = layout) 
            closeButton.bind(on_press=popup.dismiss)
            popup.open()    
        def verify_numbers(s,u,v,a,t):
            verifyList=[s,u,v,a,t]
            print(verifyList)
            for index in verifyList:
                if "/" in verifyList:
                    verifyList.remove('/')
                if "`" in verifyList:
                   verifyList.remove('`')
            print(verifyList)
            for elem in verifyList:
                elem.replace("","0")
                if type(elem)!=int or type(elem)!=float:
                    message="Invalid input"
                    self.sTextInput.text=""
                    self.uTextInput.text=""
                    self.vTextInput.text=""
                    self.aTextInput.text=""
                    self.tTextInput.text=""
                    show_popup(message)
        def excludeS(u,v,a,t):
            if u=="`":
                v=float(v)
                a=float(a)
                t=float(t)
                answer=v-a*t
                message="Initial velocity = {0}-({1}*{2}) = {3}ms^-1".format(v,a,t,answer)
                show_popup(message)
            if v=="`":
                u=float(u)
                a=float(a)
                t=float(t)
                answer=u+a*t
                message="Final velocity = {0}+({1}*{2}) = {3}ms^-1".format(u,a,t,answer)
                show_popup(message)
            if a=="`":
                v=float(v)
                u=float(u)
                t=float(t)
                try:
                    answer=(v-u)/t
                    message="Acceleration = ({0}-{1})/{2} = {3}ms^-2".format(v,u,t,answer)
                    show_popup(message)
                except:
                    message="Can't divide by 0"
                    show_popup(message)
            if t=="`":
                v=float(v)
                u=float(u)
                a=float(a)
                try:
                    answer=(v-u)/a
                    message="Time = ({0}-{1})/{2}={3}s".format(v,u,a,answer)
                    show_popup(message)
                except:
                    message="Can't divide by 0"
                    show_popup(message)
        def excludeU(s,v,a,t):
            print("test")
                    
        s = self.sTextInput.text
        u = self.uTextInput.text
        v = self.vTextInput.text
        a = self.aTextInput.text
        t = self.tTextInput.text
        verify_numbers(s,u,v,a,t)
        print(s, u, v, a, t)
        if s == "/":
            if u == "":
                u = 0
            elif v == "":
                v = 0
            elif a == "":
                a = 0
            elif t == "":
                t = 0
            excludeS(u,v,a,t)
        if u == "/":
            if s == "":
                s = 0
            elif v == "":
                v = 0
            elif a == "":
                a = 0
            elif t == "":
                t = 0
        if v == "/":
            if s == "":
                s = 0
            elif u == "":
                u = 0
            elif a == "":
                a = 0
            elif t == "":
                t = 0
        if a == "/":
            if s == "":
                s = 0
            elif u == "":
                u = 0
            elif v == "":
                v = 0
            elif t == "":
                t = 0
        if t == "/":
            if s == "":
                s = 0
            elif u == "":
                u = 0
            elif v == "":
                v = 0
            elif a == "":
                a = 0


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()