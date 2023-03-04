import sqlalchemy as sqla
from sqlalchemy import create_engine
import requests
import datetime

def write_to_file(text):
    now = datetime.datetime.now()
    with open("weather/weather_{}".format(now).replace(" ", "_").replace(":", "-"), "w") as f:
        f.write(text)

URI = "dbikes.cizsqkc3mbbs.us-east-1.rds.amazonaws.com"
PORT = "3306"
DB = "dbikes"
USER = "admin"
PASSWORD = "niuzhaozhong"
# database driver is mysqlconnector
engine = create_engine("mysql+mysqlconnector://{}:{}@{}:{}/{}".format(USER, PASSWORD, URI, PORT, DB), echo=True)


sql = """
SELECT * FROM dbikes.station;
"""

for row in engine.execute(sql):
    print(row[7], row[8])
    lat = str(row[7])
    lon = str(row[8])
    r = requests.get("https://api.open-meteo.com/v1/forecast?latitude=" + lat + "&longitude=" + lon + "&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m")
    write_to_file(r.text)