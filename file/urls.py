from django.urls import path
from . import views

urlpatterns = [
    path('upload',views.contract_upload,name='contract_upload')


]
