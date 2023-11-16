from django.shortcuts import render, redirect
from .forms import MessageForm
from BaseConfig.models import FooterData
from .models import ContactUs


def get_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            phone_number = form.cleaned_data.get('phone_number')
            message = form.cleaned_data.get('message')

            new_message = ContactUs(
                name=name,
                phone_number=phone_number,
                message=message,
            )

            new_message.save()
            return redirect('home')
    else:
        form = MessageForm()

    footer_data = FooterData.objects.filter(is_active=True).last()

    context = {
        'form': form,
        'FooterData': footer_data,
    }

    return render(request, 'ContactUs/contactUs.html', context)
