

from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder='templates')

# Load the model
model = pickle.load(open("C:\\Users\\Ganesh\\Desktop\\Major Project\\flask\\liver1.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/pred")
def index():
    return render_template("index.html")

@app.route("/out", methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        try:
            
           
            # Convert numeric form inputs to float
            Age = float(request.form["Age"])
            Bilirubin = float(request.form["Bilirubin"])
            Cholesterol = float(request.form["Cholesterol"])
            Albumin = float(request.form["Albumin"])
            # Convert other attributes to appropriate types
            Drug = request.form['Drug']
            Sex = float(request.form['Sex'])
            Ascites = request.form["Ascites"]
            Hepatomegaly = request.form["Hepatomegaly"]
            Spiders = request.form["Spiders"]
            Edema = request.form["Edema"]
            Copper = float(request.form["Copper"])
            Alk_Phos = float(request.form["Alk_Phos"])
            SGOT = float(request.form["SGOT"])
            Tryglicerides = float(request.form["Tryglicerides"])
            Platelets = float(request.form["Platelets"])
            Prothrombin = float(request.form["Prothrombin"])
            Stage = float(request.form["Stage"])

            # Use the form data to make predictions
            prediction = model.predict([[Age, Sex, Ascites, Hepatomegaly, Spiders, Edema,
                                          Bilirubin, Cholesterol, Albumin, Copper, Alk_Phos,
                                          SGOT, Tryglicerides, Platelets, Prothrombin, Stage]])
            result_text = "The person is suffering from liver cirrhosis." if prediction[0] == 1 else "The person is not suffering from liver cirrhosis."
            return render_template("result.html", prediction=result_text)
        except ValueError as e:
            # Handle the error when converting non-numeric values to float
            error_message = "Error: " + str(e)
            return render_template("error.html", error_message=error_message)

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
