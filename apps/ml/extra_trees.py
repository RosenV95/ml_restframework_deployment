import joblib
import pandas as pd
import os


class ExtraTreesClassifier:
    def __init__(self):
        path_to_artifacts = os.path.abspath(os.curdir) + "/research/"
        self.values_fill_missing = joblib.load(path_to_artifacts + "train_mode.joblib")
        self.encoders = joblib.load(path_to_artifacts + "encoders.joblib")
        self.model = joblib.load(path_to_artifacts + "extra_trees.joblib")

    def preprocess(self, input_data):
        # JSON to pd dataframe
        input_data = pd.DataFrame(input_data, index=[0])
        # missing values filled
        input_data.fillna(self.values_fill_missing)
        for column in ['education', 'marital',
                       'job', 'month', 'housing', 'day_of_week',
                       'poutcome', 'loan', 'contact', 'default']:
            categorical_convert = self.encoders[column]
            input_data[column] = categorical_convert.transform(input_data[column])
        return input_data

    def predict(self, input_data):
        return self.model.predict_proba(input_data)

    def postprocessing(self, input_data):
        label = 'no'
        if input_data[1] > 0.5:
            label = 'yes'
        return {"probability": input_data[1], "label": label, "status": "OK"}

    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocess(input_data)
            prediction = self.predict(input_data)[0]  # only one sample
            prediction = self.postprocessing(prediction)
        except Exception as e:
            return {"status": "Error", "message": str(e)}
        return prediction
