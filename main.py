from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class VoiceApp(App):
    def build(self):
        # Screen ka layout (Design)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # Oopar likha hua text
        self.label = Label(text="Voice Changer Ready!", font_size='24sp')
        layout.add_widget(self.label)
        
        # Ek bada button
        btn = Button(text="TAP TO START", 
                     size_hint=(1, 0.3), 
                     background_color=(0, 0.7, 0.3, 1))
        
        # Button dabane par kya hoga
        btn.bind(on_press=self.start_rec)
        layout.add_widget(btn)
        
        return layout

    def start_rec(self, instance):
        # Button dabne par text change ho jayega
        self.label.text = "Recording...\n(Machine is Working)"

if __name__ == "__main__":
    VoiceApp().run()
  
