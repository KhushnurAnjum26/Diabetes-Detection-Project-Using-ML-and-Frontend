from django.shortcuts import render, redirect
import joblib
import os
import numpy as np


# Load model once globally (at the top level)
model = joblib.load(os.path.join(os.path.dirname(__file__), 'diabetes_model.pkl'))

def home(request):
    return render(request, 'home.html')
import joblib
import os
import numpy as np

BASE_DIR = os.path.dirname(__file__)

model = joblib.load(os.path.join(BASE_DIR, 'diabetes_model.pkl'))
scaler = joblib.load(os.path.join(BASE_DIR, 'scaler.pkl'))

def predict(request):
    if request.method == "POST":
        pregnancies = int(request.POST.get('pregnancies', 0))
        glucose = int(request.POST.get('glucose', 0))
        bloodpressure = int(request.POST.get('bloodpressure', 0))
        skinthickness = int(request.POST.get('skinthickness', 0))
        insulin = int(request.POST.get('insulin', 0))
        bmi = float(request.POST.get('bmi', 0))
        dpf = float(request.POST.get('dpf', 0))
        age = int(request.POST.get('age', 0))

        raw_data = np.array([[pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, dpf, age]])
        scaled_data = scaler.transform(raw_data)  # Important: scale input same way!

        prediction = model.predict(scaled_data)

        result = "Prediction: Positive for Diabetes." if prediction[0] == 1 else "Prediction: Negative for Diabetes."

        return render(request, "predict.html", {"result": result})

    return redirect('home')
