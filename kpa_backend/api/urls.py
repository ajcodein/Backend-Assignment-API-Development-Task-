from django.urls import path
from .views import KPAFormCreateView, KPAFormDetailView

urlpatterns = [
    path('form/', KPAFormCreateView.as_view(), name='form-create'),
    path('form/<int:pk>/', KPAFormDetailView.as_view(), name='form-detail'),
]
