from kivy.app import App
from kivy.uix.label import Label

class VoiceApp(App):
    def build(self):
        return Label(text='Voice Changer Ready!')

if __name__ == '__main__':
    VoiceApp().run()
  
