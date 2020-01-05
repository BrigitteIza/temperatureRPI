from flask import Flask, render_template
import Adafruit_DHT
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/temperature")
def temperature():
    sensor= 11;
    pin= 4;
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        return('Temperature={0:0.1f} #Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        return('Temperature=ERROR #Humidity=ERROR')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1092, debug=True)
