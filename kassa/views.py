from django.shortcuts import render

def index(request):
    return render(request, 'kassa/index.html')

def bus(request):
    return render(request, 'kassa/bus.html')

def footer(request):
    return render(request, 'kassa/footer.html')

def privacy(request):
    return render(request, 'kassa/privacy.html')

def refund(request):
    return render(request, 'kassa/refund.html')

def help(request):
    return render(request, 'kassa/help.html')

def hotel(request):
    return render(request, 'kassa/hotel.html')


