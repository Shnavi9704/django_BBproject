
from django.contrib import admin
from django.urls import path
from fruits import views as fruit_views 
from vegetables import views as vegies_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('fruits/',fruit_views.fruits,name='fruits'),
    path('fruits/count/',fruit_views.fruit_count,name="fruit_count"),
    path('vegies/',vegies_views.vegies,name='vegies'),
    path('vegies/count/',vegies_views.vegies_count,name="vegies_count"),


]
