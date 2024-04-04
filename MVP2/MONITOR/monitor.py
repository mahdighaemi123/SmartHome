class Monitor():

    def __init__(self, getway):
        self.getway = getway

    def get_status(self):
        status = {}

        status["light_intensity"] = self.getway.service_call(
            service_name="LightIntensityKeeper",
            endpoint="/light_intensity/retrive/last",
            data={}
        )["light_intensity"]

        status["temp"] = self.getway.service_call(
            service_name="TempKeeper",
            endpoint="/temp/retrive/last",
            data={}
        )["temp"]

        status["humidity"] = self.getway.service_call(
            service_name="HumidityKeeper",
            endpoint="/humidity/retrive/last",
            data={}
        )["humidity"]

        status["rain_status"] = self.getway.service_call(
            service_name="RainStatusKeeper",
            endpoint="/rain_status/retrive/last",
            data={}
        )["rain_status"]

        status["tomorrow_rain_status_prediction"] = self.getway.service_call(
            service_name="RainPredictionServer",
            endpoint="/rain_status/predict",
            data={
                "humidity_9am": status["humidity"],
                "temp_9am": status["temp"],
                "rain_today": status["rain_status"],
            }
        )["rain_status_prediction"]

        status["date_time"] = self.getway.service_call(
            service_name="DateTimeServer",
            endpoint="/date_time/retrive",
            data={}
        )["date_time"]

        return status
