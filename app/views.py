from django.shortcuts import render, redirect
from .models import User

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['last']
        password = request.POST['password']
        email = request.POST['email']
        contact = request.POST['contact']

        user = User(name=name, lastname=lastname, password=password, email=email, contact=contact)
        user.save()

        return redirect('login')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        if name and password:
            try:
                user = User.objects.get(name=name, password=password)
                return redirect('home')
            except User.DoesNotExist:
                wrong_password = True
                return render(request, 'login.html', {'wrong_password': wrong_password})
        else:
            error_message = "Username or password is missing."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html', context={})

# def homepage_view(request):
#     raise Exception("This is a test error")
# def custom_404(request, exception):
#     return render(request, 'notfound.html', status=404)