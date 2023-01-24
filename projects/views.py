from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from projects.models import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,CreateJobpostForm,CompanyForm,CandidateForm
from .forms import *

# Create your views here.

#post job 
#functions for company 

def createjobpost(request):
    form = CreateJobpostForm()
    if request.method == 'POST':
        form = CreateJobpostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/viewmyuploadedjobs')
    context = {'form':form}
    return render(request, 'createjobs.html', context)




def updatejob(request,job_id):
    tasks = postjob.objects.get(pk = job_id)
    form = CreateJobpostForm(instance=tasks)
    if request.method =='POST':
        form = CreateJobpostForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save(commit = True)
            return redirect('viewmyuploadedjobs')

    context = {'form': form}
    return render(request,'updatejob.html',context)

def deletejob(request, job_id):
    tasks = postjob.objects.get(pk=job_id).delete()

    diction ={'delete_success':'job deleted'}
    return render(request,'deletejob.html',context=diction) 

def appliedcandidate(request):
    user = User.objects.get(id=request.user.id)
    post = postjob.objects.filter(user=request.user).first()
    candidates = applyforjob1.objects.filter(jobno=post)
    context = {'candidates': candidates}
    return render(request,'appliedcandidate.html',context) 


def sendfeedback(request):
	form = CreateFeedback()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = CreateFeedback(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/feedback')


	context = {'form':form}
	return render(request, 'feedback.html', context)

def viewmyuploadedjobs(request):
    if not request.user.is_authenticated:
        return redirect('loginpage')
    user = User.objects.get(id=request.user.id)
    tasks = postjob.objects.filter(user=request.user)
    d = {'tasks':tasks}
    return render(request,'viewmyuploadedjobs.html',d)
def contactcompany(request):
	form = ContactForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/contactcompany')
	context = {'form':form}
	return render(request, 'contactcompany.html', context)
    
#candidate
def applyjob(request):
    user = User.objects.get(id=request.user.id)
    #can = candidate.objects.filter(user=request.user).first()
    jobs = applyforjob1.objects.filter(candidate=request.user)
    context = {'jobs': jobs}
    return render(request,'applyjob.html',context) 
def viewcandidateapplication(request):
    user = User.objects.get(id=request.user.id)
    #can = candidate.objects.filter(user=request.user).first()
    jobs = applyforjob1.objects.filter(candidate=user)
    context = {'candidates': jobs}
    return render(request,'viewcandidateapplication.html',context)
def updatecandidateform(request,candidate_id):
    tasks = applyforjob1.objects.get(pk = candidate_id)
    form = ApplyForm(instance=tasks)
    if request.method =='POST':
        form = ApplyForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save(commit = True)
            return redirect('viewcandidateapplication')
    context = {'form': form}
    return render(request,'updatecandidateform.html',context) 


def getfeedback(request):
    user = User.objects.get(id=request.user.id)
    fe = feedback.objects.filter(user=request.user)
    context = {'feedbacks': fe}
    return render(request,'getfeedback.html',context)
def applyforjobs(request):
	tasks = postjob.objects.all()
	context = {'tasks':tasks}
	return render(request, 'applyforjobs.html', context)

def searchforjob(request):
    query = request.GET['query']
    allpoststitle = postjob.objects.filter(title__icontains=query)
    allpostscontent = postjob.objects.filter(describtion__icontains=query)
    tasks = allpoststitle.union(allpostscontent)
    
    context = {'tasks':tasks}
    return render(request,'searchforjob.html', context)

def apply(request):
    form = ApplyForm()
    if request.method == 'POST':
        form = ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.candidate = request.user
            post.save()
            return redirect('/viewcandidateapplication')
    context = {'form':form}
    return render(request, 'apply.html', context)

def contactcandidate(request):
	form = ContactForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/contactcandidate')   

	context = {'form':form}
	return render(request, 'contactcandidate.html', context)
#others
def index(request):
    return render(request,'index.html')
def search(request):
    query = request.GET['query']
    allpoststitle = Post.objects.filter(title__icontains=query)
    allpostscontent = Post.objects.filter(content__icontains=query)
    allposts = allpoststitle.union(allpostscontent)
    
    context = {'allposts':allposts}
    return render(request,'search.html', context)
def cvtips(request):
    allposts =Post.objects.all()
    context = {'allposts': allposts}
    return render(request,'cvtips.html',context)
def jobs(request):
    return render(request,'jobs.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        if len(name)<2 or len(email)<3 or len(phone)<4 or len(desc)<1:
            messages.error(request,"please fill the form correctly")
        else :
            contact = Contact(name=name,email=email,phone=phone,desc =desc,date=datetime.today())
            contact.save() 
            messages.success(request,"your message has been successfully send")      
    return render(request,'contact.html')


def showjobs(request):
	tasks = postjob.objects.all()


	context = {'tasks':tasks}
	return render(request, 'showjobs.html', context)


def loginpage(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'loginpage.html', locals())
 
            


def loginpage2(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'loginpage2.html', locals())
def logoutuser(request):
    logout(request)
    return redirect('/loginpage')

def signin(request):
    error=""
    if request.method=='POST':
        f = request.POST['firstname']
        c = request.POST['contact']
        e = request.POST['emailid']
        p = request.POST['password']

        try:
            user = User.objects.create_user(username=e,password=p,first_name=f)
            company.objects.create(user=user, contact=c)
            error="no"
        except:
            error="yes"
    return render(request,'signin.html', locals())
   
def signin2(request):
    error=""
    if request.method=='POST':
        f = request.POST['firstname']
        l = request.POST['lastname']
        c = request.POST['contact']
        e = request.POST['emailid']
        p = request.POST['password']

        try:
            user = User.objects.create_user(username=e,password=p,first_name=f,last_name=l)
            candidate.objects.create(user=user, contact=c)
            error="no"
        except:
            error="yes"
    return render(request,'signin2.html', locals())

def profileforcandidate(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    data = candidate.objects.get(user=user)
    d = {'data':data,'user':user}
    return render(request,'profileforcandidate.html',d)

def editforcandidate(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    data = candidate.objects.get(user=user)
    error = False
    if request.method=='POST':
        f = request.POST['firstname']
        l = request.POST['lastname']
        c = request.POST['contact']
        
        user.first_name = f
        user.last_name = l
        data.contact = c
        user.save()
        data.save()
        error=True

    d = {'data':data,'user':user,'error':error}
    return render(request,'editforcandidate.html',d)

def profileforcompany(request):
    if not request.user.is_authenticated:
        return redirect('loginpage')
    user = User.objects.get(id=request.user.id)
    data = company.objects.get(user = user)
    d = {'data':data,'user':user}
    return render(request,'profileforcompany.html',d)
def editforcompany(request):
    if not request.user.is_authenticated:
        return redirect('loginpage2')
    user = User.objects.get(id=request.user.id)
    data = company.objects.get(user=user)
    error = False
    if request.method=='POST':
        f = request.POST['firstname']
        c = request.POST['contact']
        user.first_name = f
        data.contact = c
        
        user.save()
        data.save()
        error=True

    d = {'data':data,'user':user,'error':error}
    return render(request,'editforcompany.html',d)

def changepasswordforcompany(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    if request.method=='POST':
        o = request.POST['old']
        n = request.POST['new']
        c = request.POST['confirm']
        if c==n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error="no"
        else:
            error="yes"

    return render(request,'changepasswordforcompany.html', locals())

def changepasswordforcandidate(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    if request.method=='POST':
        o = request.POST['old']
        n = request.POST['new']
        c = request.POST['confirm']
        if c==n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error="no"
        else:
            error="yes"

    return render(request,'changepasswordforcandidate.html', locals())




#manager
def login_admin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error ="yes"
        except:
            error = "yes"
    return render(request,'login_admin.html', locals())
def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    can = candidate.objects.all().count()
    com = company.objects.all().count()
    postj = postjob.objects.all().count()
    Con = Contact.objects.all().count()
    d = {'can':can,'com':com,'postj':postj,'Con':Con}
    return render(request,'admin_home.html',d)

def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('index')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        c = request.POST['confirmpassword']
        try:
            if user.check_password(o):
                user.set_password(n)

                user.save()

                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'change_passwordadmin.html', locals())

def adminviewjobs(request):
	i = postjob.objects.all()


	context = {'jobs':i}
	return render(request, 'adminviewjobs.html', context)
def adminviewcompany(request):
	i = company.objects.all()


	context = {'jobs':i}
	return render(request, 'adminviewcompany.html', context)
def adminviewcandidate(request):
	i = candidate.objects.all()


	context = {'jobs':i}
	return render(request, 'adminviewcandidate.html', context)
def adminviewcontact(request):
	i = Contact.objects.all()


	context = {'jobs':i}
	return render(request, 'adminviewcontact.html', context)

