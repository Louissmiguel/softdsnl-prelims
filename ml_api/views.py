import os
import joblib
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'weather_model.pkl')
model_path = os.path.normpath(model_path)

model = joblib.load(model_path)

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            temperature = data.get('temperature')
            humidity = data.get('humidity')
            wind_speed = data.get('wind_speed')

            if None in (temperature, humidity, wind_speed):
                return JsonResponse({'error': 'Missing one or more inputs'}, status=400)

            prediction = model.predict([[temperature, humidity, wind_speed]])
            return JsonResponse({'prediction': prediction.tolist()[0]})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
