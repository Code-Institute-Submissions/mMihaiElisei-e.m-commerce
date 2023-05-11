from django.shortcuts import render

# Create your views here.


def checkout(request):
    """ A view to handle checkout funtionality """

    
    template = 'checkout/checkout.html'
    context = {
        
    }
    return render(request, template, context)