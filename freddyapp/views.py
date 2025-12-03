from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.views.generic import UpdateView, DeleteView
from .models import Animatronic
from .forms import AnimatronicForm


# Gestión de temas
def set_dark_theme(request):
    response = redirect(request.META.get('HTTP_REFERER', 'freddyapp:list'))
    response.set_cookie('theme', 'dark')
    return response

def clear_theme_cookie(request):
    response = redirect(request.META.get('HTTP_REFERER', 'freddyapp:list'))
    response.delete_cookie('theme')
    return response

# Vistas de animatrónicos
def animatronic_list(request):
    animatronics = Animatronic.objects.all()
    return render(request, 'freddyapp/list.html', {'animatronics': animatronics})


@login_required
def animatronic_view(request, id):
    animatronic = get_object_or_404(Animatronic, pk=id)
    return render(request, 'freddyapp/detail.html', {'animatronic': animatronic})


@permission_required('freddyapp.add_animatronic', raise_exception=True)
def animatronic_new(request):
    if request.method == 'POST':
        form = AnimatronicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('freddyapp:list')
    else:
        form = AnimatronicForm()
    return render(request, 'freddyapp/form.html', {'form': form})

# Vistas basadas en clases
class AnimatronicUpdate(PermissionRequiredMixin, UpdateView):
    model = Animatronic
    form_class = AnimatronicForm
    template_name = 'freddyapp/form.html'
    success_url = reverse_lazy('freddyapp:list')
    permission_required = 'freddyapp.change_animatronic'
    pk_url_kwarg = 'id'


class AnimatronicDelete(PermissionRequiredMixin, DeleteView):
    model = Animatronic
    template_name = 'freddyapp/confirm_delete.html'
    success_url = reverse_lazy('freddyapp:list')
    permission_required = 'freddyapp.delete_animatronic'
    pk_url_kwarg = 'id'

# Autenticación de usuarios
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Asignar grupo Client al nuevo usuario
            group, created = Group.objects.get_or_create(name='Client')
            user.groups.add(group)
            return redirect('freddyapp:login')
    else:
        form = UserCreationForm()
    return render(request, 'freddyapp/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'freddyapp/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'freddyapp:list'