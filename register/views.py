from django.shortcuts import render
from django.http import HttpResponse
from . import google_sheets_api
# Create your views here.
def index(request):
    return render(request,'registration/index.html')

def submit(request,event_name):
    name = str(request.POST.get("name"))
    IIITN = str(request.POST.get("IIITN"))
    if IIITN == "IIITN":
        IIITN = "YES"
    else:
        IIITN="NO"
    enr_number_college = str(request.POST.get("college"))
    email = str(request.POST.get("email"))
    phone_number = str(request.POST.get("Phone Number"))
    fees = "No"
    cancelled = "No"
    try:
        if event_name == "craftix":
            type_ = str(request.POST.get("type"))
            google_sheets_api.append_values(event_name,name,type_,IIITN,enr_number_college,email,phone_number,fees,cancelled)

        else:
            if event_name == "prashnaban":
                name1 = str(request.POST.get("name1"))
                name2 = str(request.POST.get("name2"))
                google_sheets_api.append_values(event_name,name,name1,name2,IIITN,enr_number_college,email,phone_number,fees,cancelled)

            else:
                if event_name == "tothebeat":
                    teamname = str(request.POST.get("teamname"))
                    category = str(request.POST.get("Category"))
                    if category == "Solo":
                        name = str(request.POST.get("_name"))
                        teamname = "None"
                    google_sheets_api.append_values(event_name,category,teamname,name,IIITN,enr_number_college,email,phone_number,fees,cancelled)

                else:
                    google_sheets_api.append_values(event_name,name,IIITN,enr_number_college,email,phone_number,fees,cancelled)

    except:

        message = "Registration Failed!"
        title = "Failed to Register"
        return render(request,'registration/success.html',{'message':message,'title':title})
    message = "Successfully Registered"
    title = "Successfully Registered"
    return render(request,'registration/success.html',{'message':message,'title':title})

def feedback(request):
    name = str(request.POST.get("name"))
    email = str(request.POST.get("email"))
    message = str(request.POST.get("message"))
    try:
        google_sheets_api.append_values("feedback",name,email,message)
        message = "Feedback sent to Team Abhivyakti"
        title = "Successfull"
        return render(request,'registration/success.html',{'message':message,'title':title})
    except:
        message = "Feedback Not Send. Try Again Later!"
        title = "Failed"
        return render(request,'registration/success.html',{'message':message,'title':title})



def error404(request):
    message = "Page Not Found"
    title = "Error 404"
    return render(request,'registration/success.html',{'message':message,'title':title})