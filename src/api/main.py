import functions_framework  # Google Cloud Functions framework
from flask import abort      # Used to send error responses

from weather import get_weather  # Importing the weather fetching function

# Define a Cloud Function that handles HTTP requests
@functions_framework.http
def handle_request(request):
    # Only handle GET requests
    if request.method == "GET":
        # Extract 'city' query parameter from the URL
        city = request.args.get("city")
        
        # If city is not provided, return a 404 error
        if not city:
            return abort(404, "Please provide a city.")

        # Call the weather function for the given city
        success, response = get_weather(city)

        # If successful, return the weather info
        if success:
            return response
        else:
            # Return a 500 error if weather retrieval fails
            return abort(500, response)
    else:
        # Reject non-GET requests with a 403 error
        return abort(403)

