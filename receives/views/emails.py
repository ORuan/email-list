from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from receives.forms import CampaignForm


@login_required
def create_campaigne(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        form_data = CampaignForm(request.POST)
        if form_data.is_valid():
            save_data = form_data.save()
            save_data.user_id = user
            save_data.save()
            return redirect('painel')
        else:
            form_data = CampaignForm(request.POST)
            return render(request, 'form/campaigne/form.html', {'form':form_data})
        return render(request, 'form/campaigne/form.html', {'form':form_data})
    else:
        form_data = CampaignForm()
        context = {
            "form":form_data,
            "title":"Cadastro"
        }
        return render(request, 'form/campaigne/form.html')