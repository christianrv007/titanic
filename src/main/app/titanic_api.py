from fastapi import FastAPI, Depends
import uvicorn
import api_utils
from titanic_delegate import TitanicDelegate

app = FastAPI(title = 'Titanic FastAPI',
              description = 'Entregable modulo 3',
              version = '1.0.0')

titanic_delegate = TitanicDelegate()

@app.get('/')
def home():
    return {'text': 'Titanic Survival Prediction'}

@app.post('/predict')
def predict(response : api_utils.response = Depends(titanic_delegate.predict) ):
    return response

if __name__ == '__main__':
    uvicorn.run(app)