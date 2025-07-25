from django.urls import path
from .views import *

urlpatterns = [
    path('', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', HomeView.as_view(), name='home'),
    path('addemployee/', AddEmployeeView.as_view(), name='addemployee'),
    path('viewemployee/', ViewEmployeeList.as_view(), name='viewemployee'),
    path('editemployee/<int:empid>/', EditEmployeeView.as_view(), name='editemployee'),
    path('deleteemployee/<int:empid>/', DeleteEmployeeView.as_view(), name='deleteemployee'),
]
