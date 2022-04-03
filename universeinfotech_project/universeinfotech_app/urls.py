from django.urls import path
from .views import *

urlpatterns = [
    path('', index , name='home'),
    path('developer_team/', developer_team , name='developer_team'),
    path('blog/', blog , name='blog'),
    path('about/', about , name='about'),
    path('service/', service , name='service'),
    path('portfolio/', portfolio , name='portfolio'),
    path('history/', history , name='history'),
    path('client/', client , name='client'),

    #delails page path
    path('feature/<slug>', FeatureDetails, name='feature-detail'),
    path('service/<slug>', ServiceDetails, name='service-detail'),
    path('blog/<slug>', BlogDetails, name='blog-detail'),
]