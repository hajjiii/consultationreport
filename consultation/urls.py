from django.urls import path
from consultation import views

urlpatterns=[
    path("", views.consultation, name="home"),
    path('create-pdf',views.pdf_report_create,name='create-pdf')
]