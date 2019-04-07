from django.shortcuts import render,redirect
from manager_app.models import Managerinfo,Department
from manager_app.forms import  ManagerForm,DepartmentForm
import authorised as au

def index(request):
    if request.method == "POST":
        try:

            email=request.POST['email']
            data=Managerinfo.objects.get(email=email)
            password1=data.password
            password2=request.POST['password']
        except:
            return render(request,"index.html",{'wrnguname':True})

        if(password1==password2):
            request.session['email']=data.email
            request.session['authenticated']=True
            request.session['roleid']=data.role_id_id
            if(request.session['roleid']==3):
                return redirect("/manager/")


    return render(request, "index.html")


def manager_info(request):
    if (request.method=="POST"):
        form=ManagerForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.name=request.POST['name']
            f.email = request.POST['email']
            f.Password = request.POST['c_password']
            f.role_id_id = 4
            f.save()
            return render(request,"index1.html",{'inserted':True})
        else:
            return render(request,"index2.html")
    return render(request, "index.html")
    #try:
     #   auth=au.authoriseuser(request.session["authenticated"],request.session["roleid"],1)
    #except:

     #   return redirect("/not login")
    #if(auth):
     #
    #else:
     #   aut,message=auth
      #  if(message=="Wrong User"):
       #     return redirect("/wrong user/")
        #elif(message=="Not Login"):
         #   return redirect("/not login/")


#def logout(request):
 #   request.session['authenticated']=False
  #  return render(request, "/")


def signin(request):
    if request.method=="POST":
        uemail=request.POST["email"]
        upassword=request.POST["password"]
        userdata=Managerinfo.objects.get(user_email=uemail)
        dp=userdata.user_passsword
        if dp==upassword:
            request.session['authenticated']=True
            request.session['roleid']=userdata.role_id_id
            request.session['useremail']=userdata.user_email
        return redirect("/admin/")

    return render(request, "index.html")
def manager(request):
    return render(request,'managerindex.html')
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
