from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect, reverse


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(reverse('credentials:new_page'))
        else:
            messages.info(request, "Invalid username or password.")
            return redirect(reverse('credentials:login'))

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        # Check if the passwords match
        if password == cpassword:
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is taken.")
                return redirect(reverse('credentials:register'))
            else:
                # Create a new user
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, "Registration successful. Please log in.")
                return redirect(reverse('credentials:login'))
        else:
            messages.error(request, "Passwords do not match.")
            return redirect(reverse('credentials:register'))

    return render(request, "reg.html")

# def new_page(request):
#     # Your view logic here
#     return render(request, 'new_page.html')


# def logout(request):
#     auth.logout(request)
#     return redirect('/')


def new_page_view(request):
    return render(request, 'new_page.html')


#
# def your_view(request):
#     # Your form processing logic here
#
#     # Assuming the form is valid and the order is confirmed
#     messages.success(request, 'Order Confirmed!')
#
#     return render(request, 'new_page.html')


def show_form(request):
    if request.method == 'POST':
        # Your form handling logic goes here
        # ...

        # Add a success message
        messages.success(request, 'Order Confirmed!')

        return redirect(reverse('credentials:show_form'))  # Redirect to the same page to display the message

    return render(request, 'form.html')

