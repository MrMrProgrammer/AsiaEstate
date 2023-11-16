from django.shortcuts import render, redirect
from .forms import MessageForm
from BaseConfig.models import FooterData
from .models import Message


def get_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MessageForm()

    footer_data = FooterData.objects.filter(is_active=True).last()

    context = {
        'form': form,
        'FooterData': footer_data,

    }

    return render(request, 'ContactUs/contactUs.html', context)
