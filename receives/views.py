from django.shortcuts import render
from receives.forms import UserForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from core.views import home

# Create your views here.
def home(request):
    return render(request, 'index.html')

def register_users(request):
    if request.method == "POST":
        form_data = UserForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('painel')
        else:
            form_data = UserForm(request.POST)
            return render(request, 'forms/users/forms.html', {'form':form_data})
        return render(request, 'forms/users/forms.html', {'form':form_data})
    else:
        form_data = UserForm()
        context = {
            "form":form_data,
            "title":"Cadastro"
        }
        return render(request, 'forms/users/forms.html', context)

@login_required
def edit_users(request):
    user = User.object.get(id=request.user.id)
    if request.method == "POST":
        form_data = UserForm(request.POST or user)
        if form_data.is_valid():
            form_data.save()
        else:
            form_data = UserForm(user)
            context = {
                "form":form_data,
                "title":"Edição"
            }
            return render(request, 'forms/users/forms.html', context)
        context = {
            "form":form_data,
            "title":"Edição"
        }
        return render(request, 'forms/users/forms.html', context)
    else:
        form_data = UserForm()
        context = {
            "form":form_data,
            "title":"Edição"
        }
        return render(request, 'forms/users/forms.html', context)

@login_required
def delete_user(request):
    email = request.user.email
    #send_mail


    context = {
    }
    return render(request, 'forms/users/confirm.html', context)