import pandas as pd
from django.shortcuts import render

def pandas_assignment(request):
    """
    Handles the web application logic for the pandas assignment.

    This function responds to both GET and POST requests.
    - On a GET request, it renders the initial form.
    - On a POST request, it processes the form data, converts the numbers
      to a pandas Series with an alphabetical index, and renders the result.
    """
    pandas_series_data = None
    series_exists = False  # New variable to handle the template check

    if request.method == 'POST':
        try:
            numbers = [
                int(request.POST.get('number1')),
                int(request.POST.get('number2')),
                int(request.POST.get('number3')),
                int(request.POST.get('number4')),
                int(request.POST.get('number5')),
            ]
            
            alphabetical_index = ['a', 'b', 'c', 'd', 'e']
            pandas_series_data = pd.Series(numbers, index=alphabetical_index)
            series_exists = True  # Set to True if the series was created
            
        except (ValueError, TypeError):
            # Handle cases where the input is not a valid number
            context = {'error': "Please enter 5 valid numbers."}
            return render(request, 'pandas_app/index.html', context)

    context = {
        'pandas_series': pandas_series_data,
        'series_exists': series_exists, # Pass the new boolean variable to the template
    }

    return render(request, 'alphas/index.html', context)
