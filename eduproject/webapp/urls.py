from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'webapp'

urlpatterns = [
    path('employee/', views.employeeList.as_view(), name='list'),
    path('employee/<first_name>',
         views.employeesDetailAPIViews.as_view(), name='detail'),
    path('employee/<first_name>/edit',
         views.employeesUpdateAPIViews.as_view(), name='edit'),
    path('employee/<first_name>/delete',
         views.employeesDeleteAPIViews.as_view(), name='delete'),
    path('employee/create',
         views.employeesCreateAPIViews.as_view(), name='create')
]
