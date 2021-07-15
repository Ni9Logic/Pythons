from kivy.app import App
from kivy.lang import Builder

kv = '''
FloatLayout:
    Button:
        text: 'Look Sunduss What I can do With Python!'
        size_hint: .5, .25
        pos_hint:  {'center_x': 0.5}
        pos_hint: {'center_y': 0.5}
        origin: self.center
'''

class SuperApp(App):
    def build(self):
        return Builder.load_string(kv)

SuperApp().run()