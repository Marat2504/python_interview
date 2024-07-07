from django.urls import path

from interview.views import all_offers, offer_data, add_offer

urlpatterns = [
    path('', all_offers, name='all_offers'),
    path('<uuid:pk>/', offer_data, name='offer_data'),
    path('add/', add_offer, name='add_offer')
]
