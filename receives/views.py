from django.shortcuts import render
from receives.forms import UserForm


# Create your views here.
def home(request):
    return render(request, 'index.html')

def register_users(request):
    if request.method == "POST":
        form_data = UserForm(request.POST)
        if form_data.is_valid():
            form_data.save()
        else:
            form_data = UserForm(request.POST)
            return render(request, 'forms/users/forms.html', {'form':form_data})
        return render(request, 'forms/users/forms.html', {'form':form_data})
    else:
        form_data = UserForm()
        return render(request, 'forms/users/forms.html', {'form':form_data})