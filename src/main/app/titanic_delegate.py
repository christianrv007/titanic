import joblib
import pandas as pd
import constants
import api_utils
from sklearn.pipeline import Pipeline

class TitanicDelegate:

    prod_model: Pipeline

    def load_model(self):
        self.prod_model = joblib.load(constants.PATH_MODEL)

    def predict(self, input: api_utils.requestParameters) -> api_utils.response:
        """load model"""
        self.load_model()

        """Runs a prediction"""
        df = pd.DataFrame([input.dict()])
        prediction = self.prod_model.predict(df)[0]
        
        return self.response(prediction)
    
    def response(self,prediction: int):
        """process result to send api response"""
        if(prediction == 0):
            message = "This person didn´t survive"
        elif(prediction == 1):
            message = "This person survived"

        return api_utils.response(prediction=prediction, message=message)
