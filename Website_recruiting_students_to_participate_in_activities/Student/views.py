from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required, user_passes_test
from Person_responsible_for_the_project.models import db_create_activity, db_activity_adduser
from Student.forms import UserStudentrUpdateForm
from Accounts.models import UserStudent
from Accounts.forms import UserStudentrRegistrationForm
# from Person_responsible_for_the_project.forms import forms_activity_adduser

# Create your views here.
def is_student(user):
    return user.is_authenticated and hasattr(user, 'is_student') and user.is_student

@login_required
@user_passes_test(is_student, login_url='login')
def home(request):
    db = db_activity_adduser.objects.all()
    user_student = UserStudent.objects.get(user=request.user)
    activity_all = db_create_activity.objects.all()
    return render(request, 'Student/home.html', {
        'db' : activity_all,
        # 'i' : user_student,
        'std' : db,
        })

@login_required
@user_passes_test(is_student, login_url='login')
def activity(request, id):
    activity_get_id = db_create_activity.objects.get(pk=id)
    activity_get_all = db_activity_adduser.objects.all()
    # db1 = db_activity_adduser.objects.filter(activity_id=id)
    # db = db_activity_adduser.objects.filter(activity_id=id)

    # existing_registration1 = db_activity_adduser.objects.filter(activity=activity_get_id, student=request.user).exists()
    # existing_registration = db_activity_adduser.objects.all().filter(activity=activity_get_id, student=request.user)

    # form = forms_activity_adduser()
    # activity_get_id = db_create_activity.objects.get(pk=id)
    # activity_id = db_activity_adduser.objects.get(pk=id)
    db = db_activity_adduser.objects.filter(status=True)
    # form = forms_activity_adduser()

    if request.method == 'POST':
        # form = forms_activity_adduser(request.POST, instance=existing_registration)
            # ตรวจสอบว่านักเรียนลงทะเบียนกิจกรรมนี้แล้วหรือไม่
        existing_registration1 = db_activity_adduser.objects.filter(activity=activity_get_id, student=request.user).exists()
        # existing_registration = db_activity_adduser.objects.get(activity=activity_get_id, student=request.user).exists()
        # form = forms_activity_adduser(request.POST)

        if existing_registration1:
            # กรณีลงทะเบียนกิจกรรมซ้ำ
            messages.error(request, 'คุณได้ลงทะเบียนกิจกรรมนี้ไปแล้ว')

 # หรือ redirect ไปที่หน้าอื่นที่คุณต้องการ

        # # if request.user.is_recruitment_announcer:
        # elif form.is_valid():
        #         # form.save()
        #     # if activity.student_id == 
        #     activity = form.save(commit=False)
        #     activity.student_id = request.user.id # กำหนดผู้ประกาศข่าวเป็นผู้ใช้ปัจจุบัน
        #     activity.activity_id = activity_get_id.id # กำหนดผู้ประกาศข่าวเป็นผู้ใช้ปัจจุบัน
        #     form.save()
        #     activity.save()

        # elif form.is_valid():
        #         # form.save()
        #     # if activity.student_id == 
        #     activity = form.save(commit=True)
        #     activity.student_id == request.user.id # กำหนดผู้ประกาศข่าวเป็นผู้ใช้ปัจจุบัน
        #     activity.activity_id == activity_get_id.id # กำหนดผู้ประกาศข่าวเป็นผู้ใช้ปัจจุบัน
        #     form.save()
        #     activity.save()
# @login_required
# @user_passes_test(is_student, login_url='login')
# def activity(request, id):
#     db = db_activity_adduser.objects.filter(id=id)

#     # ดึงกิจกรรมที่ต้องการลงทะเบียนด้วย id
#     activity_get_id = db_create_activity.objects.get(pk=id)

#     # ตรวจสอบว่านักเรียนลงทะเบียนกิจกรรมนี้แล้วหรือไม่
#     existing_registration = db_activity_adduser.objects.filter(activity=activity_get_id, student=request.user).exists()

#     if existing_registration:
#         # กรณีลงทะเบียนกิจกรรมซ้ำ
#         messages.error(request, 'คุณได้ลงทะเบียนกิจกรรมนี้ไปแล้ว')
#         return redirect('/Student')  # หรือ redirect ไปที่หน้าอื่นที่คุณต้องการ

#     # สร้างฟอร์มลงทะเบียนกิจกรรม
#     form = forms_activity_adduser(request.POST or None)

#     if form.is_valid():
#         # บันทึกข้อมูลเมื่อฟอร์มถูกต้อง
#         activity = form.save(commit=False)
#         activity.student = request.user  # กำหนดผู้ใช้ปัจจุบันเป็นนักเรียน
#         activity.activity = activity_get_id  # กำหนดกิจกรรมที่ต้องการลงทะเบียน
#         activity.save()
#         messages.success(request, 'ลงทะเบียนกิจกรรมเรียบร้อยแล้ว')
#         return redirect('/Student')  # หรือ redirect ไปที่หน้าอื่นที่คุณต้องการ


    return render(request, 'Student/activity.html', {
        'i' : activity_get_id,
        # 'form' : form,
        'db' : db,
        # 'existing_registration' : existing_registration,
        'activity_get_all' : activity_get_all
        })

@user_passes_test(is_student, login_url='login')
def profileStudent(request):
    user_student = UserStudent.objects.get(user=request.user)   #get id from user not request id
    db = UserStudent.objects.get(pk=user_student.id)  #get id from user not request id

    return render(request, 'Student/profile.html', {
        'i' : db,
        })

@user_passes_test(is_student, login_url='login')
def updateprofileStudent(request, id):
    db = UserStudent.objects.get(pk=id)
    form = UserStudentrUpdateForm(instance=request.user)
    if request.method == 'POST':
        form = UserStudentrUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            form.save()
            return redirect('profileStudent')
    return render(request, 'Student/updateprofile.html', {
        'form' : form,
        'i' : db,
        })
