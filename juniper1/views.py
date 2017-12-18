from django.shortcuts import render
from django.template import loader

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.sessions.models import Session
from django.views.decorators.clickjacking import xframe_options_deny
from .scripts import Updatedb,saveFun

@xframe_options_deny
@login_required(login_url='/juniper/login')
def index(request):
    request.session.cycle_key()
    return render(request, 'juniper/home.html')

@xframe_options_deny
@login_required(login_url='/juniper/login')
def release(request):
    return render(request, 'juniper/release.html')

@xframe_options_deny
@login_required(login_url='/juniper/login')
def releasenotes(request):
    return render(request, 'juniper/RELEASE_NOTE.html')


@xframe_options_deny
@login_required(login_url='/juniper/login')
def defect(request):
    return render(request, 'juniper/defect.html')

@xframe_options_deny
@login_required(login_url='/juniper/login')
def defectfinal(request):
    problemarea = request.POST.get('Problem', False)
    defecttitle = request.POST.get('Defect', False)
    defectdescription = request.POST.get('Description', False)
    priority = request.POST.get('Priority', False)
    steps = request.POST.get('Steps', False)
    defecttype = request.POST.get('Type', False)
    print problemarea,defecttitle,defectdescription,priority,steps,defecttype
    #inp=problemarea,defecttitle,defectdescription,priority,steps,defecttype
    Updatedb.defectdbpg(problemarea,defecttitle,defectdescription,priority,steps,defecttype)

    return render(request, 'juniper/defectfinal.html')



@xframe_options_deny
@login_required(login_url='/juniper/login')
def team (request):
    return render(request, 'juniper/team.html')

@xframe_options_deny
@login_required(login_url='/juniper/login')
def help(request):
    return render(request, 'juniper/help.html')

@xframe_options_deny
@login_required(login_url='/juniper/login')
def about(request):
    return render(request, 'juniper/about.html')

@xframe_options_deny
@login_required(login_url='/juniper/login')
def aspire(request):
    return render(request, 'juniper/aspire.html')

def login(request):
    username = request.POST.get('username', '')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username, password=password)
    print(user)
    if user is not None and user.is_active:
        auth.login(request,user)
	request.session.cycle_key()
        return HttpResponseRedirect("/juniper/")
    else:
        return HttpResponseRedirect("login")

def logout_view(request):
    #logout(request)
    auth.logout(request)
    return HttpResponseRedirect("/juniper/login/")


@xframe_options_deny
@login_required(login_url='/juniper/login')
def copyright(request):
    return render(request, 'juniper/copyright.html')

@xframe_options_deny
@login_required(login_url='/juniper/login')
def demo(request):
    return render(request,'juniper/demo.html')

@xframe_options_deny
@login_required(login_url='/juniper/login')	
def aspire_tool_kit(request):
    return render(request, 'juniper/aspire_tool_kit.html')


@xframe_options_deny
@login_required(login_url='/juniper/login')
def intoduction_to_juniper_usecases(request):
    return render(request, 'juniper/intoduction_to_juniper_usecases.html')

@xframe_options_deny
@login_required(login_url='/juniper/login')
def installation_guide(request):
    return render(request, 'juniper/installation_guide.html')

@xframe_options_deny
@login_required(login_url='/juniper/login')
def aspire_user_manual(request):
    return render(request, 'juniper/aspire_user_manual.html')
    
def save(request):
    saveFun.export_users_xlsx(request)
    return render(request, 'juniper/save.html')
