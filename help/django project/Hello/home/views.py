from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request  ,  "index.html" ) 
    # return HttpResponse("WELCOME GYYMZZ")

def about(request):
    return render(request  ,  "about.html" )

def contact(request):
    return render(request  ,  "contact.html" )

    if request.method == "POST":
        message_name = request.POST["message-name"]
        message_email = request.POST["message-email"]
        message = request.POST["message"]
        
        # sending email by send_mail function
        send_mail(
            
            message_name, #sub
            message,      #message
            message_email,  #from
            ["madhukeshsingh87205@gmail.com"],  #to
            
        )
        
        return render(request, "contact.html",{'message_name': message_name})
        
    else :
        return render(request, "contact.html", {})
    