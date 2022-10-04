from django.shortcuts import render 
import datetime 
def wish(request):
    """date_time""" 
    date=datetime.datetime.now() 
    msg="hi gues hellow good"
    h=int(date.strftime('%H')) 
    if h<12:
        msg+="morning"
    elif h<16:
        msg+="ofternoon"
    elif h<21:
        msg+="evening"
    else:
        msg+="very very good night"
    my_dict={"insert_date":date,"insert_msg":msg}  
    return render(request,"test_app/wish.html",context=my_dict)               