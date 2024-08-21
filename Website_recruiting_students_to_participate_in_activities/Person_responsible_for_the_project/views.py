from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from Person_responsible_for_the_project.models import db_create_activity
from Accounts.models import UserPerson_responsible_for_the_project
from Person_responsible_for_the_project.forms import UserPerson_responsible_for_the_projectUpdateForm, forms_create_activity

# Create your views here.
def home(request):
    aa = UserPerson_responsible_for_the_project.objects.get(user=request.user)
    activity_all = db_create_activity.objects.all()
    
    return render(request, 'Person_responsible_for_the_project/home.html', {
        'i':aa,
        'db' : activity_all
    })

def profilePerson_responsible_for_the_project(request):
    user = UserPerson_responsible_for_the_project.objects.get(user=request.user)
    db = UserPerson_responsible_for_the_project.objects.get(pk=user.id)

    return render(request, 'Person_responsible_for_the_project/profile.html', {
        'i' : db,
        })

# @user_passes_test(is_student, login_url='login')
def updateprofilePerson_responsible_for_the_project(request, id):
    db = UserPerson_responsible_for_the_project.objects.get(pk=id)
    form = UserPerson_responsible_for_the_projectUpdateForm(instance=request.user)
    if request.method == 'POST':
        form = UserPerson_responsible_for_the_projectUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_person_responsible_for_the_project = True
            user.save()
            form.save()
            return redirect('profilePerson_responsible_for_the_project')
    return render(request, 'Person_responsible_for_the_project/updateprofile.html', {
        'form' : form,
        'i' : db,
        })

@login_required
# @user_passes_test(is_recruitment_announcer or is_staff, login_url='login')
# @receiver(post_save, sender=db_create_activity)
def create_activity2(request):
    # user = UserRecruitment_announcer.objects.get(user=request.user)
    form = forms_create_activity()
    if request.method == 'POST':
        form = forms_create_activity(request.POST, request.FILES)
        # if request.user.is_recruitment_announcer == is_recruitment_announcer.user:
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user # กำหนดผู้ประกาศข่าวเป็นผู้ใช้ปัจจุบัน
            activity.save()
            # if created:  # ตรวจสอบว่ากิจกรรมถูกสร้างใหม่หรือไม่
            # user = request.user.id  # กำหนดผู้ใช้งานปัจจุบันเป็นผู้สร้างกิจกรรม
            # user.save()
            # user = form.save(commit=False)
            # user.is_recruitment_announcer = True
            # user.save()
            # form.save()
            # user = form.save(commit=False)
            # user = request.user.id # กำหนดผู้ประกาศข่าวเป็นผู้ใช้ปัจจุบัน
            # user.save()
            # activity = form.save(commit=False)
            # activity.user = request.user  # กำหนดผู้ประกาศข่าวเป็นผู้ใช้ปัจจุบัน
            # activity.save()
            return redirect('/Person_responsible_for_the_project')
        # else:

    return render(request, 'Person_responsible_for_the_project/create_activity.html', {
        'form' : form,
        })


@login_required
# @user_passes_test(is_recruitment_announcer or is_staff, login_url='login')
def update_activity2(request, id):
    activity_get_id = db_create_activity.objects.get(pk=id)
    form = forms_create_activity(instance=activity_get_id)
    if request.method == 'POST':
        form = forms_create_activity(request.POST, request.FILES, instance=activity_get_id)
        # if request.user.is_recruitment_announcer:
        if form.is_valid():
                # form.save()
                activity = form.save(commit=False)
                activity.user.id = request.user.id # กำหนดผู้ประกาศข่าวเป็นผู้ใช้ปัจจุบัน
                activity.save()
                return redirect('activity_crateby_user2')
        else:
            form = forms_create_activity(instance=activity_get_id)

    return render(request, 'Person_responsible_for_the_project/update_activity.html', {
        'form':form,
        'i': activity_get_id,
        })

def activity_crateby_user2(request):
    # user = User.objects.get(user=request.user)
    s = db_create_activity.objects.filter(user_id=request.user.id)  
    return render(request, 'Person_responsible_for_the_project/activitys_crateby_user.html', {
        'db':s,
        # 'aa':user,
        })