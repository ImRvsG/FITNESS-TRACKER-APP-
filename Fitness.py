from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from plyer import accelerometer

class FitnessTracker(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.steps = 0

        self.label = Label(text="Steps Count: 0", font_size=24)
        self.add_widget(self.label)

        self.start_button = Button(text="Start Tracking", on_press=self.start_tracking)
        self.add_widget(self.start_button)

    def start_tracking(self, instance):
        accelerometer.enable()
        self.bind(on_touch_down=self.step_detected)

    def step_detected(self, instance, touch):
        self.steps += 1
        self.label.text = f"Steps Count: {self.steps}"

class TrackerApp(App):
    def build(self):
        return FitnessTracker()

if __name__ == "__main__":
    TrackerApp().run()
