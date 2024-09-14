from itertools import count
from random import randint
from kivy.app import App
from kivy.graphics import Line, Color, Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class Main_Menu(Screen):
    pass


class ImagesExample(Screen):
    pass


class Page(Screen):
    pass


class CanvasExample(Screen):
    pass


class CanvasExample2(Screen):
    pass


class CanvasExample3(Screen):
    pass


class CanvasExample4(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=2)
            Color(0, 1, 0)
            Line(circle=(400, 200, 81), width=2)
            Line(rectangle=(700, 500, 150, 100), width=2)
            self.rect = Rectangle(pos=(700, 200), size=(150, 100))

    def on_move_square_press(self):
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)
        diff = self.width - (x + w)
        if x < inc:
            inc = x

        x -= inc
        self.rect.pos = (x, y)

    def on_move_square_right(self):
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)
        diff = self.width - (x + w)
        if diff < inc:
            inc = diff

        x += inc
        self.rect.pos = (x, y)


class CanvasExample5(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(3)
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
            Clock.schedule_interval(self.update, 0.01)

    def on_size(self, *args):
        #print("on size :" + str(self.width) + ", " + str(self.height))
        self.ball.pos = (self.center_x - self.ball_size / 2, self.center_y - self.ball_size / 2)

    def update(self, dt):
        #print("update")
        x, y = self.ball.pos

        x += self.vx
        y += self.vy

        #print("x", x)
        #print("w", self.width)

        if x > (self.width - self.ball_size):
            self.vx = -self.vx

        if y > (self.height - self.ball_size):
            self.vy = - self.vy
        if y < 0:
            self.vy = - self.vy

        if x < 0:
            self.vx = - self.vx

        self.ball.pos = (x, y)


class CanvasExample6(Screen):
    pass


class CanvasExample7(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class Wid2(Screen):
    count = 1
    my_text = StringProperty("0")
    Active_Button = BooleanProperty(False)
    #slider_value = StringProperty("50")
    #Active_Slider = BooleanProperty(False)
    Text_String_str = StringProperty("")

    def on_button_click(self):
        if self.Active_Button:
            self.my_text = str(self.count)
            self.count += 1
        if self.count > 10:
            self.count = 0
        else:
            pass

    def on_toggle_button_state(self, widget):
        #print(widget.state)
        if widget.state == "normal":
            widget.text = "Off"
            self.Active_Button = False
        else:
            widget.text = "On"
            self.Active_Button = True

    def on_text_validate(self, widget):
        self.Text_String_str = widget.text


"""
    def on_switch_active(self, widget):
        print(widget.active)
        if widget.active:
            self.Active_Slider = True
        else:
            self.Active_Slider = False

    def on_value(self, widget):
        pass
        self.slider_value = str(int(widget.value))
        print(int(widget.value))
"""


class Stack(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, 100):
            five = Button(text=str(i + 1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(five)


class Grid(GridLayout):
    pass


class Anchor(AnchorLayout):
    pass


class Box(BoxLayout):
    pass
    """def __init__(self, **kwargs):
        pass
        super(Box, self).__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="test")
        b2 = Button(text="working")
        b3 = Button(text="clever")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)"""


class Wid(Widget):
    pass


kv = Builder.load_file("lab.kv")


class LabApp(App):
    def build(self):
        return kv


LabApp().run()
