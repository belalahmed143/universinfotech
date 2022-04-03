from django.urls import path
from .views import *

urlpatterns = [
    path('', index , name='home'),
    path('developer_team/', developer_team , name='developer_team'),
    path('blog/', blog , name='blog'),
    path('about/', about , name='about'),
    path('portfolio/', portfolio , name='portfolio'),

    #delails page path
    path('feature/<slug>', FeatureDetails, name='feature-detail'),
    path('service/<slug>', ServiceDetails, name='service-detail'),
    path('blog/<slug>', BlogDetails, name='blog-detail'),
]