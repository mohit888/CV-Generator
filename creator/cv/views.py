from django.shortcuts import render,redirect
from cv.forms import resume_dataForm, UserLoginForm, UserRegisterForm,EducationForm,experienceForm,skillsForm
from .models import resume_data,skills,experience,Education
from django.views.generic.edit import UpdateView
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model
)
from django.contrib.auth.decorators import login_required


class resume_dataUpdateView(UpdateView):
    model = resume_data


    fields = ['address', 'univ', 'email', 'phone', 'profession',]

    success_url = "/data"

def home(request):
    return render(request,'webpages/index.html')

"""def contact(request):
    if request.method == 'POST':
        form1 = reg_infoForm(request.POST)
        if form1.is_valid():
            print('form is valid')
            form1.save()
    else:
        print('form is not valid')
        form1 = reg_infoForm()
    return render(request,'form.html',{'form':form1})"""

@login_required
def data(request):
    if request.method == 'POST':
        form1 = resume_dataForm(request.POST)
        if form1.is_valid():
            print('form is valid')
            da = form1.save(commit = False)
            da.user = request.user
            da.save()
            return redirect('/data')
    else:
        print('form is not valid')
        form1 = resume_dataForm()
    return render(request, 'webpages/fillform.html', {'form': form1})

@login_required
def skill_added(request):
    if request.method == 'POST':
        form2 = skillsForm(request.POST)
        if form2.is_valid():
            print('form is valid')
       
            sk = form2.save(commit = False)
            sk.user = request.user
            sk.save()
            return redirect('/skills')
    else:
        print('form is not valid')
        form2 = skillsForm
    return render(request, 'webpages/skills.html', {'form': form2})


@login_required
def experience_add(request):
    if request.method == 'POST':
        form3 = experienceForm(request.POST)
        if form3.is_valid():
            print('form is valid')
        
            ex = form3.save(commit = False)
            ex.user = request.user
            ex.save()
            return redirect('/exp')
    else:
        print('form is not valid')
        form3 = experienceForm()
    return render(request, 'webpages/experience.html', {'form': form3})


@login_required
def schooling_add(request):
    if request.method == 'POST':
        form4 = EducationForm(request.POST)
        if form4.is_valid():
            print('form is valid')
            sc = form4.save(commit = False)
            sc.user = request.user
            sc.save()
            return redirect('/sch')
    else:
        print('form is not valid')
        form4 = EducationForm()
    return render(request, 'webpages/school.html', {'form': form4})


@login_required
def resume(request):
    dat = resume_data.objects.filter(user = request.user.id)
    skill = skills.objects.filter(user = request.user.id)
    exper = experience.objects.filter(user = request.user.id)
    schoo = Education.objects.filter(user = request.user.id)
    if len(dat) >= 1:
        data = dat[0]
        data_dict = { 'name' : data.FullName,
                       'address' : data.Address,
                        'univ'    : data.University,
                        'email'   : data.Email,
                        'phone'   : data.Phone,
                        'profile' : data.Profile,
                        'skills'  : skill,
                        'exper'   : exper,
                        'schoo'   : schoo,
        }
    else:
        data_dict = { }
    return render(request,'webpages/resume.html',context = data_dict)

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/data')

    context = {
        'form': form,
    }
    return render(request, "webpages/signin.html", context)



def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/sdata')

    context = {
        'form': form,
    }
    return render(request, "webpages/signup.html", context)

def signupdata(request):
    mail = request.user.email
    return render(request,"webpages/signupdata.html",{'email':mail})

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')



