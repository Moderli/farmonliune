from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, MachineForm  # Assuming you have a MachineForm defined
from .models import MachineModel, UserProfileModel

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to your home page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
from django.shortcuts import render, redirect
from .models import MachineModel
from .forms import MachineForm
def home(request):
    # Fetch all available machines
    available_machines = MachineModel.objects.all()

    # Fetch phone number and insta for each user who uploaded a machine
    user_profiles = UserProfileModel.objects.filter(username__in=available_machines.values('username'))

    if request.method == 'POST':
        form = MachineForm(request.POST, request.FILES)
        if form.is_valid():
            machine = form.save(commit=False)
            machine.username = request.user.username
            machine.save()
            return redirect('home')  # Redirect to home page after successful upload
    else:
        form = MachineForm()

    return render(request, 'home.html', {'form': form, 'available_machines': available_machines, 'user_profiles': user_profiles})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to your home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfileModel

def profile_setup(request):
    user = request.user

    # Check if the user has already filled out the profile form
    if UserProfileModel.objects.filter(username=user.username).exists():
        # User has already filled out the form, redirect to another view or home page
        return redirect('home')  # Change 'home' to the appropriate URL or view name

    # User is accessing the profile setup for the first time
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # Save the user's profile information
            user_profile = form.save(commit=False)
            user_profile.username = user.username
            user_profile.save()

            # Redirect to another view or home page
            return redirect('home')  # Change 'home' to the appropriate URL or view name
    else:
        form = UserProfileForm()

    return render(request, 'profile_setup.html', {'form': form})


from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    # Redirect to the desired URL after logout
    return redirect('login')

