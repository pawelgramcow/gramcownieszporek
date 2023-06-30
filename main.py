import model
import pandas as pd
from fastapi import FastAPI

app = FastAPI()
model = model.make_model()

@app.post("/predict")
def predict_price(age: int, sex: str, race: str, educationnum: int, workclass: str, occupation: str, maritalstatus: str, hoursperweek: int):
    teraz = [age, sex, race, educationnum, workclass, occupation, maritalstatus, hoursperweek]
    df = pd.read_csv("csv.csv", sep=",", engine="python")
    df.loc[(len(df) - 1), "age"] = teraz[0]
    df.loc[(len(df) - 1), "sex"] = teraz[1]
    df.loc[(len(df) - 1), "race"] = teraz[2]
    df.loc[(len(df) - 1), "education-num"] = teraz[3]
    df.loc[(len(df) - 1), "workclass"] = teraz[4]
    df.loc[(len(df) - 1), "occupation"] = teraz[5]
    df.loc[(len(df) - 1), "marital-status"] = teraz[6]
    df.loc[(len(df) - 1), "hours-per-week"] = teraz[7]
    X_new = df[['age', 'sex', 'race', 'education-num', 'workclass', 'occupation', 'marital-status', 'hours-per-week']]
    X_new_dummies = pd.get_dummies(data=X_new)
    nowy = X_new_dummies.tail(1)
    value = model.predict(nowy)

    for col in value:
        wynik = value

    if (wynik == [0]):
        return 'biedny'
    else:
        return 'bogaty'