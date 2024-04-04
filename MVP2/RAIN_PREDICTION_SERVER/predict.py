import pickle
import os
import pandas as pd


class PredictRainStatus:

    def __init__(self, models_path="models") -> None:
        self.models_path = models_path
        self.load_models()

    def load_models(self):
        self.models = {}

        for model_file_name in os.listdir(self.models_path):

            model_name = model_file_name.split(".")[0]

            model_path = os.path.join(self.models_path, model_file_name)

            with open(model_path, "rb") as model_file:
                model = pickle.load(model_file)
                self.models[model_name] = model

    def predict(self, data):
        results = []
        df = pd.DataFrame(data)

        for index in range(len(df)):
            predicts = []
            data = df.iloc[index].to_frame().T
            for model_name, model in self.models.items():
                predict = model.predict(data)[0]
                predicts.append(predict)

            final_result = round(sum(predicts)/len(predicts) * 100, 2)
            results.append(final_result)

        return results


if __name__ == "__main__":
    predictRainStatus = PredictRainStatus()

    humidity_9am = 99.0
    temp_9am = 0.0
    rain_today = 0

    data = {"Humidity9am": [humidity_9am],
            "Temp9am": [temp_9am],
            "RainToday": [rain_today]}

    print(predictRainStatus.predict(data))
