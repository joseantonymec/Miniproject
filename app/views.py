from django.shortcuts import render#,render_to_response
from django.shortcuts import redirect
from .forms import UserSignUp 
import json
from django.http import HttpResponse

def start(request):

	form=UserSignUp(request.POST or None)
	vld_value = request.POST.get('name')
        vld_id = request.POST.get('password')
        vld_error = request.POST.get('email')
        array_to_js = [vld_id, vld_error, False]
        if vld_value == "testuser":
            array_to_js[2] = True
            json_data = json.dumps(array_to_js)
            return HttpResponse(json_data)

	context={"form":form,"title":"Reg"}
	if form.is_valid():
		form.save()
		return redirect("http://127.0.0.1:8000/app/signup/thankyou")
	return render(request,'home.html',context)
