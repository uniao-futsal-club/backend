from django.urls import path, include
from .views import api, public

urlpatterns = [
    path('', public, name='public'),
    path('api/', api, name='api'),
    # path('api/accounts/', include('accounts.urls')),
    # path('api/address/', include('address.urls')),
    # path('api/authentication/', include('authentication.urls')),
    # path('api/order/', include('order.urls')),
    # path('api/validation/', include('validation.urls')),
    # path('api/vehicle/', include('vehicle.urls')),
]
