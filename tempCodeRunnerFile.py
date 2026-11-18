@app.get("/Bio")
def home():
    return{"Name":"Monika",
           "age":20,
           "Education":"BBA"}
