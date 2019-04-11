from django.shortcuts import render,redirect
from manager_app.models import Department,Member,UserRole
from manager_app.forms import DepartmentForm,MemberForm
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
import mail as m


def index(request):
    if request.method == "POST":
        try:
            email=request.POST['email']
            data=Member.objects.get(member_email=email)
            password1=data.member_password
            password2=request.POST['password']
        except:
            return render(request,"index.html",{'wrnguname':True,'data':data})

        if(password1==password2):
            request.session['email']=data.member_email
            request.session['authenticated']=True
            request.session['roleid']=data.role_id_id
            if(request.session['roleid']==3):
                return redirect("/manager/")
            elif(request.session['roleid']==1):
                return redirect("/doctor/")
            elif (request.session['roleid'] == 4):
                return redirect("/staff/")
        else:
            return render(request,"index.html",{'wrngpass':True})
    return render(request, "index.html")
def logout(request):
    request.session['authenticated']=False
    return redirect("/")
def manager(request):
    return render(request,'managerindex.html')
def doctor(request):
    return render(request,'doctorindex.html')
def staff(request):
    return render(request,'staffindex.html')
def createdepartment(request):
    if request.method=="POST":
        form=DepartmentForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.department_name=request.POST['department_name']
            f.department_strength=request.POST['department_strength']
            f.department_location=request.POST['department_location']
            f.department_head=request.POST['department_head']
            f.save()
            return render(request,"createdepartment.html",{'success':True})
    return render(request,"createdepartment.html")
def viewdepartment(request):
    data=Department.objects.all()
    return render(request,"viewdepartment.html",{'data':data})
def deletedepartment(request):
    id=request.GET['id']
    data=Department.objects.get(department_id=id)
    data.delete()
    return render(request,"viewdepartment.html")
def updatedepartment(request):
    id=request.GET['id']
    data=Department.objects.get(department_id=id)
    if request.method=="POST":
        dname=request.POST['department_name']
        dstrength=request.POST['department_strength']
        dlocation=request.POST['department_location']
        dhead=request.POST['department_head']
        update=Department(department_id=id,department_name=dname,department_strength=dstrength,department_location=dlocation,department_head=dhead)
        update.save(update_fields=['department_name','department_strength','department_location','department_head'])
        return redirect("/viewdepartment/")
    return render(request,"updatedepartment.html",{'ddata':data})
def addstaff(request):

    department=Department.objects.all()
    if request.method=="POST":
        memberimage=None
        if request.FILES:
            myfile=request.FILES['member_photo']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            memberimage=fs.url
            memberimage=myfile.name
        form=MemberForm(request.POST)
        if form.is_valid:

            f = form.save(commit=False)
            name = request.POST['member_first_name']
            name1 = request.POST['member_last_name']
            address = request.POST['member_address']
            user = UserRole.objects.all()
            department=request.POST['member_department']
            if(department=="Other"):
                a=user.role_id_id=4
            else:
                a=user.role_id_id=1

            length = str(len(name)) + str(len(name1)) + str(len(address))
            password = str(name1) + str(length)
            f.member_image = memberimage
            f.member_first_name = request.POST['member_first_name']
            f.member_last_name = request.POST['member_last_name']
            f.member_address = request.POST['member_address']
            f.member_phone = request.POST['member_phone']
            f.member_email = request.POST['member_email']
            f.member_dob = request.POST['member_dob']
            f.member_gender = request.POST['member_gender']
            f.member_status = True
            f.role_id_id = a
            f.member_password = password
            f.member_department_id=department
            f.save()
            m.mail_sending(f.member_first_name, f.member_last_name, f.member_email, password)

            return render(request,"addstaff.html",{'success': True,'department': department})
        else:
            return render(request,"addstaff.html",{'failed': True,'department': department})

    return render(request,"addstaff.html",{'department':department})

def viewmember(request):
    data=Member.objects.filter(Q(role_id_id=1)| Q(role_id_id=4))
    return render(request,"viewstaff.html",{'mdata':data})
def deletemember(request):
    id=request.GET['id']
    data=Member.objects.get(member_id=id)
    data.delete()
    return redirect("/viewstaff/")
def updatemember(request):
    id=request.GET['id']
    mdata=Member.objects.get(member_id=id)
    if request.method=="POST":
        member_image=mdata.member_image
        if request.FILES:
            newfile=request.FILES['member_image']
            fs=FileSystemStorage()
            filename=fs.save(newfile.name,newfile)
            member_image=fs.url(filename)
            member_image=newfile.name
        mname1=request.POST['member_first_name']
        mname2=request.POST['member_last_name']
        mimage=member_image
        maddress=request.POST['member_address']
        mphone=request.POST['member_phone']
        mdob=request.POST['member_dob']
        mgender=request.POST['member_gender']
        update=Member(member_id=id,member_first_name=mname1,member_last_name=mname2,member_image=mimage,member_address=maddress,member_phone=mphone,member_dob=mdob,member_gender=mgender)
        update.save(update_fields=['member_first_name','member_last_name','member_image','member_address','member_phone','member_dob','member_gender'])
        return redirect("/viewstaff/")
    return render(request,"updatestaff.html",{'mdata':mdata})