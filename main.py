from flask import Flask, escape, request, render_template,url_for
import pickle

model = pickle.load(open("model_pickle.pkl", 'rb'))

app = Flask(__name__,template_folder='template')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        Age = int(request.form['Age'])
        Height = int(request.form['Height'])
        Weight = int(request.form['Weight'])
        Diabetes = request.form['Diabetes']
        BloodPressureProblems = request.form['BloodPressureProblems']
        AnyTransplants = request.form['AnyTransplants']
        AnyChronicDiseases = request.form['AnyChronicDiseases']
        NumberOfMajorSurgeries = int(request.form['NumberOfMajorSurgeries'])
        KnownAllergies = request.form['KnownAllergies']
        HistoryOfCancerInFamily = request.form['HistoryOfCancerInFamily']

        # diabetes
        if (Diabetes == "Yes"):
            Diabetes = 1
        else:
            Diabetes = 0

        # BloodPressureProblems
        if (BloodPressureProblems == "Yes"):
            BloodPressureProblems = 1
        else:
            BloodPressureProblems = 0

        # AnyTransplants
        if (AnyTransplants == "Yes"):
            AnyTransplants = 1
        else:
            AnyTransplants = 0

        # AnyChronicDiseases
        if (AnyChronicDiseases == "Yes"):
            AnyChronicDiseases = 1
        else:
            AnyChronicDiseases = 0

        # AnyTransplants
        if (AnyTransplants == "Yes"):
            AnyTransplants = 1
        else:
            AnyTransplants = 0

        # AnyTransplants
        if (KnownAllergies == "Yes"):
                KnownAllergies = 1
        else:
            KnownAllergies = 0

        # AnyTransplants
        if (HistoryOfCancerInFamily == "Yes"):
            HistoryOfCancerInFamily = 1
        else:
            HistoryOfCancerInFamily = 0


        feature = [[Age,Height,Weight,Diabetes,BloodPressureProblems,AnyTransplants,AnyChronicDiseases,KnownAllergies,HistoryOfCancerInFamily,NumberOfMajorSurgeries]]

        prediction = model.predict(feature)[0]
        # print(prediction)

        return render_template("index.html", prediction_text="Predicted cost is --> {}".format(prediction))


    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)