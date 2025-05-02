import kivy
from kivy.app import App
from kivy.uix.label import Label
from plyer import notification
import winsound

def show_notification(message):
    notification.notify(
        title="Flood Warning!",
        message=message,
        timeout=10
    )

def trigger_buzzer():
    winsound.Beep(1000, 500)

class WeatherApp(App):
    def build(self):
        self.label = Label(text="Waiting for alert...", font_size=32)
        self.check_threshold()
        return self.label

    def check_threshold(self):
        threshold_exceeded = True

        if threshold_exceeded:
            alert_message = "Flood warning in XXX area. Water levels are rising!"
            self.label.text = alert_message
            show_notification(alert_message)
            trigger_buzzer()

if __name__ == '__main__':
    WeatherApp().run()