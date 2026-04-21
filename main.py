from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class VoiceApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        self.label = Label(text="Voice Changer Ready!", font_size='24sp')
        layout.add_widget(self.label)
        
        btn = Button(text="TAP TO START", size_hint=(1, 0.3), background_color=(0, 1, 0, 1))
        btn.bind(on_press=self.start_rec)
        layout.add_widget(btn)
        return layout

    def start_rec(self, instance):
        self.label.text = "Recording... Machine Working"

if __name__ == "__main__":
    VoiceApp().run()
  
