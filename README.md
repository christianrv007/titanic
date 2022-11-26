**Crear ambiente virtual**
> python -m venv my_env

**Activar ambiente virtual**
> my_env\Scripts\activate.bat

**Instalar requirements**
> pip install -r requirements.txt

**En el directorio donde se ecnuentra el archivo titanic_api.py, inicuar uvicorn para deployar la api**
> uvicorn inference:app --reload

**Ingresar al localhost para ver la documentacion en OpenAPI**
> http://127.0.0.1:8000/docs

**En try out, ingresar los siguientes parametros**
```
{
    "pclass": 1,
    "name": "Allen, Miss. Elisabeth Walton",
    "sex": "female",
    "age": "29",
    "sibsp": 0,
    "parch": 0,
    "ticket": "24160",
    "fare": "211.3375",
    "cabin": "B5",
    "embarked": "S",
    "boat": "2",
    "body": "?"
}
```