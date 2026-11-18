from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app=FastAPI()
# model=joblib.load("model.pkl")
# class Flowerdata(BaseModel):
#     sepal_length:float
#     sepal_width:float
#     petal_length:float
#     petal_width:float

# @app.get("/")
# def home():
#     return{"message":"model is running"}

# @app.post("/predict")
# def predict(data:Flowerdata):
#     input_data=[[data.sepal_length,
#                  data.sepal_width,data.petal_length,data.petal_width]]

#     prediction=model.predict(input_data)
#     flower_names=["setosa","versicolor","virginica"]

#     result=flower_names[int(prediction[0])]
#     return{"prediction":result}




@app.get("/Bio")
def home():
    return{"Name":"Monika",
           "age":20,
           "Education":"BBA"}

class Biodata(BaseModel):
    name:str
    age:int
    education:str

@app.post("/Biodata")
def data(data:Biodata):
    return{"Name":data.name,"age":data.age,"Education":data.education}

