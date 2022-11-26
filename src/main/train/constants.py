import os

#url to read titanic info
URL = "https://www.openml.org/data/get_csv/16826755/phpMYEkMl"
BASE_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
ROOT_DIR = os.path.realpath(os.path.join(BASE_DIR, ".."))
PATH_MODEL = os.path.realpath(os.path.join(ROOT_DIR, "main/resources/models", "model.sav"))

#numeric variables
NUMERIC_VARS = ["pclass", "age", "sibsp", "parch", "fare"]
#Categorical variables
#CATEGORICAL_VARS = ["female", "cabin", "embarked", "title"]
CATEGORICAL_VARS = ["pclass", "embarked","title"]
#columns to delete
DROP_COLUMNS = ["ticket", "body", "name","boat","sex","sibsp","parch","cabin"]

TEST_SIZE = 0.2
SEED_SPLIT = 404

TARGET = "survived"

#FEATURES = ["age","travel_alone","pclass_1","pclass_2","embarked_C","embarked_S","female"]

FEATURES = ["age","travel_alone","pclass_1","embarked_S","female"]
