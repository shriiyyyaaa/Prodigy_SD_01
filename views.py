from django.shortcuts import render
from django.http import JsonResponse

def temperature_converter(request):
    if request.method == 'POST':
        # Get user input from the form
        temperature = float(request.POST.get('temperature'))
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')

        # Convert the temperature
        result = convert_temperature(temperature, from_unit, to_unit)
        
        return JsonResponse({'result': result})

    return render(request, 'index.html')


def convert_temperature(temperature, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return (temperature * 9/5) + 32
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        return temperature + 273.15
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (temperature - 32) * 5/9
    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        return (temperature + 459.67) * 5/9
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        return temperature - 273.15
    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        return (temperature * 9/5) - 459.67
    else:
        return temperature  # No conversion needed