from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('results/<poll_id>', views.results, name='results'),
    path('vote/<poll_id>', views.vote, name='vote'),
    path('delete/<int:id>/',views.delete_data , name="DeletePoll"),

]