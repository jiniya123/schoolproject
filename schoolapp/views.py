from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import User


from .forms import RegistrationForm,UserProfileForm
from .models import Department
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages,auth
# Create your views here.
def home(request):
    departments = Department.objects.all()
    return render(request, 'home.html', {'departments': departments})
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
def redirect_to_wikipedia(request, department_id):
    department = Department.objects.get(pk=department_id)
    return redirect(department.wikipedia_link)

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('school:login')  # Redirect to the login page after successful registration

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        profile_form = UserProfileForm()

    return render(request, 'profile.html', {'profile_form': profile_form})














from django.shortcuts import render, redirect
from django.contrib import auth, messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('school:another_page')  # Redirect to the new page upon successful login
        else:
            messages.error(request, 'Invalid login credentials')

    return render(request, 'login.html')



# from django.shortcuts import render
#
def another_page_view(request):
    return render(request, 'another_page.html')
# def some_other_view(request):
#     # Your view logic here
#     return render(request, 'some_other_view.html')



def handle_form_submission(request):
    if request.method == 'POST':
        return redirect('success_page')

from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Department, Course, Material,Purpose

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Department, Course, Material, UserProfile, Purpose
from .forms import RegistrationForm, UserProfileForm


from django.contrib import messages

def form_page(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # Form is valid, process the data as before
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            selected_purpose_id = request.POST.get('purpose')
            selected_purpose = Purpose.objects.get(id=selected_purpose_id)

            if selected_purpose.name == 'Place order':
                message = 'Order Confirmed'
            elif selected_purpose.name == 'For Enquiry':
                message = 'Our team will contact you soon.'
            elif selected_purpose.name == 'Return':
                message = 'Our return person will contact you soon.'

            messages.success(request, message)
            return redirect('school:confirmation', username=request.user.username, purpose=selected_purpose.name)
        else:
            # Form is not valid, display error messages
            messages.error(request, 'Form submission failed. Please check the form data.')

    else:
        form = UserProfileForm()

    departments = Department.objects.all()
    courses = Course.objects.all()
    materials = Material.objects.all()
    purposes = Purpose.objects.all()

    return render(request, 'form_page.html', {
        'form': form,
        'departments': departments,
        'courses': courses,
        'materials': materials,
        'purposes': purposes,
    })



def logout_view(request):
    logout(request)
    return redirect('school:home')

# views.py



from django.shortcuts import render

def confirmation_view(request, username, purpose):
    # Render the confirmation page with different messages based on 'purpose'
    if purpose == 'Place order':
        message = 'Order Confirmed'
    elif purpose == 'For Enquiry':
        message = 'Our team will contact you soon.'
    elif purpose == 'Return':
        message = 'Our return person will contact you soon.'

    return render(request, 'confirmation_page.html', {'username': username, 'message': message})

