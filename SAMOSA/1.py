
import pandas as pd

# load dataset
data = pd.read_csv("creditcard.csv")

data = data.dropna()

# see first rows
print(data.head())

# see dataset info
print(data.shape)

print(data['Class'].value_counts())
X = data.drop('Class', axis=1)
y = data['Class']
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)

print("Model accuracy:", accuracy)
prediction = model.predict(X_test.iloc[0:1])

print("Prediction:", prediction)