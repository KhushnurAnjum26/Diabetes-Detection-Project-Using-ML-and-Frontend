from django.shortcuts import render , redirect
def home(request):
    return render(request,'home.html')

def predict(request):
    if request.method == "POST":
        # Extract form data safely
        pregnancies = int(request.POST.get('pregnancies', 0))
        glucose = int(request.POST.get('glucose', 0))
        bloodpressure = int(request.POST.get('bloodpressure', 0))
        skinthickness = int(request.POST.get('skinthickness', 0))
        insulin = int(request.POST.get('insulin', 0))
        bmi = float(request.POST.get('bmi', 0))
        dpf = float(request.POST.get('dpf', 0))
        age = int(request.POST.get('age', 0))

        # Dummy prediction logic: if glucose > 125 => diabetic
        if glucose > 125:
            result = "Prediction: Positive for Diabetes."
        else:
            result = "Prediction: Negative for Diabetes."

        # Render prediction page with result
        return render(request, 'predict.html', {'result': result})

    # For GET request, redirect to home page (input form)
    return redirect('home')