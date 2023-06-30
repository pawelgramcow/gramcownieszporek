import pandas as pd
from sklearn.linear_model import LogisticRegression

def make_model():
    df = pd.read_csv("csv.csv", sep=",", engine="python")
    df['income'] = (df['income'] == '>50K').astype(int)
    y = df['income']
    X = df[['age', 'sex', 'race', 'education-num', 'workclass', 'occupation', 'marital-status', 'hours-per-week']]
    X = pd.get_dummies(X, columns=['sex', 'race', 'workclass', 'occupation', 'marital-status'])
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, stratify=y, random_state=1)

    model = LogisticRegression(solver='lbfgs', max_iter=2000)
    model.fit(X_train, y_train)

    return model