import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder as oneHot
from sklearn.preprocessing import MinMaxScaler as MMScaler
import utils 

class CleanData(BaseEstimator, TransformerMixin):
    """Prepares the data for the training phase"""

    def __init__(self):
        self.feature_names_out = []

    def fit(self, df, y=None):
        self.feature_names_out = df.columns
        return self

    def transform(self, df, y=None):
        """This method transform data
                missing values
                tranform sex value to int
                replaced rare characters
                set datatypes
        """
        df.replace("?", np.nan, inplace=True)

        #set the most common value to missing values
        df["embarked"].fillna(df['embarked'].value_counts().idxmax(), inplace=True)
        #set median to missing values
        df["age"].fillna(df["age"].median(skipna=True), inplace=True)
        df["fare"].fillna(df["fare"].median(skipna=True), inplace=True)
        #set datatypes
        df["age"] = df["age"].astype("float")
        df["fare"] = df["fare"].astype("float")

        return df

class CreateCategoricalVariables(BaseEstimator, TransformerMixin):
    """Prepares the data for the training phase"""

    def __init__(self):
        self.feature_names_out = []

    def fit(self, df, y=None):
        self.feature_names_out = df.columns
        return self

    def transform(self, df, y=None):
        #set only first cabin
        df["cabin"] = df["cabin"].apply(utils.get_first_cabin)
        #set the title inside the name
        df["title"] = df["name"].apply(utils.get_title)
        #set if is female
        df["female"] = df.sex.apply(lambda x: 1 if x=='female' else 0)
        #set if travel alone
        df['travel_alone']=np.where((df["sibsp"]+df["parch"])>0, 0, 1)

        return df

class CreateDummies(BaseEstimator, TransformerMixin):
    """Prepares the data for the training phase"""

    def __init__(self,columns):
        self.feature_names_out = []
        self.columns = columns

    def fit(self, df, y=None):
        self.feature_names_out = df.columns
        return self

    def transform(self, df, y=None):
        return pd.get_dummies(df, columns=self.columns)



class DropColumns(BaseEstimator, TransformerMixin):
    """
    Drop columns that are not will be used in the model
    """

    def __init__(self, drop_columns):
        self.drop_columns = drop_columns
        self.feature_columns = []
        self.feature_names_out = []

    def fit(self, df, y=None):
        self.feature_columns = df.drop(columns=self.drop_columns).columns
        return self

    def transform(self, df, y=None):
        return df.drop(columns=self.drop_columns)

class SelectFeatures(BaseEstimator, TransformerMixin):
    """
    Selected the most important columns
    """

    def __init__(self, columns):
        self.columns = columns
        self.feature_columns = []
        self.feature_names_out = []

    def fit(self, df, y=None):
        self.feature_columns = self.columns
        return self

    def transform(self, df, y=None):
        return df[self.columns]

class MinMaxScaler(BaseEstimator, TransformerMixin):
    """Scales the values of numerical columns between 0 and 1"""

    def __init__(self):
        self.scaler = MMScaler()
        self.feature_names_out = []

    def fit(self, df, y=None):
        self.scaler.fit(df)
        self.feature_names_out = df.columns
        return self

    def transform(self, df, y=None):
        return self.scaler.transform(df)