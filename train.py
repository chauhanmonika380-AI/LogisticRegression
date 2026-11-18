from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

iris=load_iris()
x= iris.data
y=iris.target

X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=LogisticRegression()
model.fit(X_train,Y_train)
acc=model.score(X_test,Y_test)
print("Accuracy:",acc)
joblib.dump(model,"model.pkl")

print("model saved successfully")