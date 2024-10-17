from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse,JsonResponse
from myapp.models import Ouruser, Product, RegisteredUsers #if you ever need to import something from template, do: from template.form.html ....
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from ProjectModels.models import CustomUser, Profile, ProfileImage
from django.contrib import messages
# Create your views here.
class BooksView(View):
    def get(self,request):
        return HttpResponse("Hi, return string")
class Homeview(View):
    def get(self,request):
        try:
            return render(request,"Homepage.html")
        except Exception as exeptionerror:
            print("There is an exeption error!", exeptionerror)
            return  render(request,"Error.html")
class UserFormview(View):
    def get(self,request):
        try:
            return render(request,"Form.html")
        except Exception as exeptionerror:
            print("There is an exeption error!", exeptionerror)
            return  render(request,"Error.html")
    def post(self,request):
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            print(name,email,message)
            obj = Ouruser(name = name, email = email, message = message)
            obj.save()
            print(obj.name, obj.email, obj.message, "dddddd") # apperas in terminal
            context = {'name':obj.name, 'email':obj.email, 'message':obj.message}
            return render(request,"Successful.html",{'obj':obj}) #HttpResponse(context)            
        except Exception as exeptionerror:
            print("There is an exeption error!", exeptionerror)
            return  render(request,"Error.html")
        
class ProductView(View):
    def get(self,request):
        try:
            return render(request,"Form2.html")
        except Exception as exeptionerror:
            print("There is an exeption error!", exeptionerror)
            return  render(request,"Error.html")


    def post(self,request):
        print("Hello")
        try:
            product_name = request.POST.get('product_name')
            #print('product_name',product_name)
            product_model = request.POST.get('product_model')
            product_price = request.POST.get('product_price')
            product_desc = request.POST.get('product_desc')
            #print(product_name,product_model,product_price,product_desc)
            obj = Product(product_name = product_name,  product_model = product_model,  product_price = product_price, product_desc = product_desc)
            print(obj)
            obj.save()
            
            # apperas in terminal
            context = {'product_name':obj.product_name, 'product_model':obj.product_model, 'product_desc':obj.product_desc}
            return render(request,"Successful.html",{'obj':obj}) #HttpResponse(context)            
        except Exception as exeptionerror:
            print("There is an exeption error!", exeptionerror)
            return  render(request,"Error.html")

class AllOurUsersView(View):
    def get(self,request):
        Data = {}
        count = 1
        obj = Ouruser.objects.all()
        for users in obj:
            name = users.name
            email = users.email
            message = users.message
            Created_Date = users.createdDate
            Created_Time = users.createdTime
            
            context = {"name": users.name, "email": users.email, "message": users.message, "Created Date": users.createdDate, "Created Time": users.createdTime}
            var1 = f"context_{count}"
            print(var1)
            #Data[var1] = context
            Data.setdefault(var1,context)
            count+= 1
        #print(context)
        print(Data)
        return JsonResponse(context)

class DashboardView(View):
    def get(self,request):
        try:
            return render(request,"Dashboard.html")
        except Exception as exeptionerror:
            print("There is an exeption error!", exeptionerror)
            return render(request,"Error.html")
        
class SignUpView(View):
    def get(self,request):
        try:
            messages.success(request,"I am In signup form!")
            return render(request,"SignUp.html")
        except Exception as exeptionerror:
            print("There is an exeption error!", exeptionerror)
            messages.error(request, "Something went wrong")
            return render(request,"Error.html")
    def post(self,request):
        try:
            # user_name = request.POST.get('username')
            user_email = request.POST.get('email')
            user_password = request.POST.get('password')
            #password = request.POST.get('password')
            #user_password = make_password('user_password')
            obj = CustomUser(email = user_email)
            obj.set_password(user_password)
            #print(obj.user_name, obj.user_email, obj.user_password, "dddddd") # apperas in terminal
            obj.save()
            
            context = {'email':obj.email, 'password':obj.password}
            messages.success(request,"Sign up successful")
            # return render(request,"login.html",{'obj':obj}) #HttpResponse(context)
            return redirect('login')
        except Exception as exeptionerror:
            messages.error(request,"Something went wrong")
            print("There is an exeption error!", exeptionerror)
            return render(request,"Error.html")



class LoginView(View):
    def get(self,request):
        try:
            messages.warning(request, "successful, login page open")
            return render(request,"login.html")
        except Exception as exeptionerror:
            print("There is an exeption error!", exeptionerror)
            return render(request,"Error.html")
    def post(self,request):
        try:
            print("Trying")
            user_email = request.POST.get('email')
            user_password = request.POST.get('password')
            if not user_email and not user_password:
                return (request,"Error.html")
            if CustomUser.objects.filter(email = user_email).exists():
                print("username is ",user_email)
                user = authenticate(request,email = user_email, password = user_password)
                print(user.id)
                print("user is ",user)
                login(request,user)
                if user is not None:
                    
                    if Profile.objects.filter(user = user).first():
                        return redirect("userdisplay")
                    #return render(request,"userinfo.html")
                    return redirect("userinfo",user.id)
                else:
                    print("Error! password not authenticated!")
                    return render(request,"login.html")

            else:
                print("You are not registered, try signing up!")
                return render(request,"SignUp.html")

            # return render(request,"Dashboard.html")
            print("except") 
        except Exception as exeptionerror:
            print("There is an exeption error!", exeptionerror)
            return render(request,"Error.html")
        
        
# class UserInfoView(View):
#     def get(self,request):
#         try:
#             return render(request,"userinfo.html")
#         except Exception as exeptionerror:
#             print("There is an exeption error", exeptionerror)
#             return render(request,"index.html")
#     def post(self,request):
#         try:
#             DOB = request.POST.get('DOB')
#             gender = request.POST.get('gender')
#             image1 = request.POST.get('image1')
#             image2 = request.POST.get('image2')
#             image3 = request.POST.get('image3')
#             image4 = request.POST.get('image4')
#             image5 = request.POST.get('image5')
#             image6 = request.POST.get('image6')
#         except Exception as exeptionerror:
#             print("There is an exeption error!", exeptionerror)
#             return render(request,"index.html")
        
class UserProfileView(View):
    def get(self,request,id):
        try:
            user = CustomUser.objects.get(id = id)
            return render(request,"userinfo.html")
        except Exception as exeptionerror:
            print("There is an exeption error!", exeptionerror)
            return render(request,"Error.html")
        
    def post(self,request,id):
        try:
            dob1 = request.POST.get('dob')
            print(dob1, " This is DOB ")
            gender = request.POST.get('gender',"")
            image = request.FILES.getlist('image')
            print("This is the print after image",image)
            
            obj = CustomUser.objects.get(id = id)
            pro = Profile.objects.create(user = obj, dob = dob1, gender = gender)
            pro.save()
            for img in image:
                picpro = ProfileImage.objects.create(user = pro, profimage = img)
            messages.success(request,"User profile created successfully!")
            #return render(request,"userdisplay.html")
            return redirect("userdisplay")
        except Exception as exeptionerror:
            print("There is an exeption error!", exeptionerror)
            return render(request,"Error.html")
        
class UserDisplayView(View):
    def get(self,request):
        try:
            user = request.user
            print(user)
            profileinfoobj = Profile.objects.get(user = user)
            imageinfoobj = ProfileImage.objects.filter(user = profileinfoobj)
            contents = {'dob':profileinfoobj.dob, 'gender': profileinfoobj.gender, 'profileImage': imageinfoobj}

            return render(request, "userdisplay.html",contents)
        except Exception as exeptionerror:
            print("There is an exeption error!", exeptionerror)
            return render(request,"Error.html")
            