#weather app
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt, QTimer, QTime
import requests

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Weather App')
        self.setGeometry(100, 100, 400, 200)

        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.weather_label = QLabel(self)
        vbox.addWidget(self.weather_label)  # Add the weather label to the layout
        self.weather_label.setAlignment(Qt.AlignCenter)
        self.weather_label.setStyleSheet("font-size: 20px;"
                                         "color: black;"
                                         "background-color: white;"
                                         "border: 2px solid black;"
                                         "border-radius: 10px;"
                                         "padding: 10px;"
                                         "font-family: 'Arial';")

        self.update_weather()   
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_weather)
        self.timer.start(60000)
    def update_weather(self):
        api
_key =
    "your_api_key_here"
    city = "your_city_here"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city  }&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        self.weather_label.setText(f"Temperature: {temperature}°C\nDescription: {description}")     
    except requests.RequestException as e:
        self.weather_label.setText("Error fetching weather data")   
if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())