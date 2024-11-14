from django.shortcuts import render

def index(request):
    return render(request, 'communication/index.html')

# View to display custom 404 page
def custom_404(request, exception):
    return render(request, '404.html', status=404)