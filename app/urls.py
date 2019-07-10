from django.urls import path
from .views import *

urlpatterns = [

    # path('', Qurilish_view.as_view(), name='home'),
    # path('send', sendjson, name='sendjson')
    path('hi/', hi, name='hi'),
    path('delete/<int:id>', destroy, name='delete'),
    path('delete/', delete, name='delete1'),
    # path('delete/(?P<id>[0-9]+)$', delete, name='delete')
]
