from django.views.generic import TemplateView, CreateView, ListView, UpdateView, FormView, DeleteView
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Employee
from .forms import NewUserForm, AddEmployeeForm

class SignupView(FormView):
    template_name = 'signup.html'
    form_class = NewUserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginView(AuthLoginView):
    template_name = 'login.html'

class LogoutView(AuthLogoutView):
    next_page = reverse_lazy('login')

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

class AddEmployeeView(LoginRequiredMixin, CreateView):
    model = Employee
    form_class = AddEmployeeForm
    template_name = 'addemployee.html'
    success_url = reverse_lazy('viewemployee')

class ViewEmployeeList(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'viewemployee.html'
    context_object_name = 'employees'

class EditEmployeeView(LoginRequiredMixin, UpdateView):
    model = Employee
    form_class = AddEmployeeForm
    template_name = 'editemployee.html'
    pk_url_kwarg = 'empid'
    success_url = reverse_lazy('viewemployee')

class DeleteEmployeeView(LoginRequiredMixin, DeleteView):
    model = Employee
    template_name = 'confirm_delete.html'
    pk_url_kwarg = 'empid'
    success_url = reverse_lazy('viewemployee')
