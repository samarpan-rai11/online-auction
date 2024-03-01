from django.shortcuts import redirect
from django.urls import reverse
from django.http import JsonResponse


class SetJSONContentTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Check if the response is a JsonResponse
        if isinstance(response, JsonResponse):
            # Set Content-Type header to application/json
            response['Content-Type'] = 'application/json'

        return response



class PreventLoginSignupAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if the user is logged in
        if request.user.is_authenticated:
            # URLs that logged-in users should be redirected from
            restricted_urls = [reverse('userauth:login'), reverse('userauth:signup')]

            if request.path in restricted_urls:
                return redirect('core:index')

        return response
