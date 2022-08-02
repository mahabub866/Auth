
from django.urls import path

from users.api.views import ClientOnlyView, ClientSignupView, CustomeAuthToken, FreelanceOnlyView, FreelanceSignupView, http_response


urlpatterns = [
    path('signup/freelance/',FreelanceSignupView.as_view(), ),
    path('signup/client/',ClientSignupView.as_view(), ),
    path('login/',CustomeAuthToken.as_view(), name='auth-token'),
    path('freelance/dashboard/',FreelanceOnlyView.as_view(),name='freelancer-dashboard'),
    path('client/dashboard/',ClientOnlyView.as_view(),name='client-dashboard'),
    path('httpresponse/', http_response.as_view(), name='http_response'),
]
