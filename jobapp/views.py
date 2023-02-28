
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import *
from .models import *
from jobportal.settings import EMAIL_HOST_USER


# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def nav(request):
    return render(request,'navbar.html')
def foot(request):
    return render(request,'footer.html')
def prof(request):
    return render(request,'profile.html')
def regview(request):
    if request.method == 'POST':
        a = regform(request.POST)
        if a.is_valid():
            cn = a.cleaned_data['cname']
            ad = a.cleaned_data['address']
            ph = a.cleaned_data['phone']
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            cp=  a.cleaned_data['cpassword']
            if cp==ps:
               b = regmodel(cname=cn, address=ad,phone=ph, email=em,password=ps)
               b.save()
               return redirect(log)
            else:
                return HttpResponse("incorrect password")
        else:
            return HttpResponse("failed")
    else:
        return render(request,'register.html')
def log(request):
    if request.method=='POST':
        a=logform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            ps=a.cleaned_data['password']
            b=regmodel.objects.all()
            for i in b:
                cmp=i.cname
                request.session['cname']=cmp
                id=i.id
                if i.email==em and i.password==ps:
                    return render(request,'profile.html',{'cmp':cmp,'id':id})
            else:
                return HttpResponse("login failed")
    else:
        return render(request,'login.html')
def vacancy(request,id):
    b =regmodel.objects.get(id=id)
    cn = b.cname
    el = b.email
    if request.method=='POST':
        a = upform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['cname']
            em = a.cleaned_data['email']
            jt = a.cleaned_data['jtitle']
            jp = a.cleaned_data['jtype']
            wt = a.cleaned_data['wtype']
            ex = a.cleaned_data['exp']
            ql = a.cleaned_data['qualify']
            b = addmodel(cname=nm, email=em, jtitle=jt, jtype=jp, wtype=wt, exp=ex, qualify=ql)
            b.save()
            return HttpResponse("Upload Success....")
        else:
            return HttpResponse("Upload Failed!")
    else:
        return render(request,'uploadvac.html',{'cn':cn,'el':el})

def viewvac(request):
    a=addmodel.objects.all()
    b=request.session['cname']
    return render(request,'viewvacancy.html',{'x':a,'y':b})

def jobupdate(request, id):
    a = addmodel.objects.get(id=id)
    if request.method == 'POST':
        a.cname = request.POST.get('cname')
        a.email = request.POST.get('email')
        a.jtitle = request.POST.get('jtitle')
        a.jtype = request.POST.get('jtype')
        a.wtype = request.POST.get('wtype')
        a.exp=request.POST.get('exp')
        a.qualify=request.POST.get('qualify')
        a.save()
        return redirect(viewvac)

    return render(request, 'editvacancy.html', {'x': a})
def jobdele(request,id):
    av=addmodel.objects.get(id=id)
    av.delete()
    return render(request, 'viewvacancy.html')
class userreg(generic.CreateView):
    form_class = userregform
    template_name = 'userregister.html'
    success_url = reverse_lazy('userlogin')
class userlog(generic.View):
        form_class = userlogform
        template_name = 'userlogin.html'
        def get(self, request):
            form = self.form_class
            return render(request, self.template_name)
        def post(self, request):
            if request.method == 'POST':
                a = userlogform(request.POST)
                if a.is_valid():
                    em = a.cleaned_data['email']
                    ps = a.cleaned_data['password']
                    b = User.objects.all()
                    for i in b:
                        fname=i.first_name
                        lname=i.last_name
                        usr=i.username
                        if em == i.email and ps == i.password:
                            id=i.id
                            request.session['id']=i.idy
                            return render(request,'userprofile.html',{'fname':fname,'lname':lname,'usr':usr,'id':id})
                    else:
                        return HttpResponse("failed")

def userprof(request):
    return render(request,'userprofile.html')
class adduserprodet(generic.CreateView):
    form_class = userprofform
    template_name = 'userprofdetails.html'
    success_url = reverse_lazy('userprofile')

def companydis(request):
    a=regmodel.objects.all()
    return render(request,'displaycompanies.html',{'x':a})

def userviewvac(request):
    a=addmodel.objects.all()
    return render(request,"userviewvac.html",{'x':a})

def applyclass(request,id):
    b=addmodel.objects.get(id=id)
    cn=b.cname
    jb=b.jtitle
    if request.method=='POST':
        a=applyform(request.POST,request.FILES)
        if a.is_valid():
            cn=a.cleaned_data['cname']
            jt=a.cleaned_data['jobtitle']
            fn=a.cleaned_data['fname']
            em=a.cleaned_data['email']
            re=a.cleaned_data['resume']
            c=applymodel(cname=cn,jobtitle=jt,fname=fn,email=em,resume=re)
            c.save()
            subject=f"new job applied to {cn}"
            message=f"hi {fn}\n your application is successfully applied for the r+ole of {jt}"
            send_mail(subject,message,EMAIL_HOST_USER,[em])
            return HttpResponse("mail uploaded successfully")
        else:
            return HttpResponse("apply failed")
    else:
        return render(request, 'userapply.html', {'cn': cn, 'jb': jb})

def wishlist(request,id):
    a=addmodel.objects.get(id=id)
    b=wishmodel(cname=a.cname,email=a.email,jtitle=a.jtitle,jtype=a.jtype,wtype=a.wtype,exp=a.exp,qualify=a.qualify)
    b.save()
    return HttpResponse("job added to wishlist")
def wishdis(request):
    a=wishmodel.objects.all()
    return render(request,'wishlist.html',{'x':a})
def wishdele(request,id):
    a=wishmodel.objects.get(id=id)
    a.delete()
    return HttpResponse("Removed Successfully")
def viewappusers(request):
    a=applymodel.objects.all()
    cn=[]
    jt=[]
    fn=[]
    em=[]
    res = []
    id=[]
    b = request.session['cname']
    for i in a:
        re=i.resume
        res.append(str(re).split('/')[-1])
        cm=i.cname
        cn.append(cm)
        jb=i.jobtitle
        jt.append(jb)
        fl=i.fname
        fn.append(fl)
        el=i.email
        em.append(el)
        id1=i.id
        id.append(id1)

    mylist=zip(fn,cn,jt,em,res,id)
    return render(request,'viewappusers.html',{'x':mylist,'y':b})
def remuser(request,id):
    a=applymodel.objects.get(id=id)
    a.delete()
    return HttpResponse('removed successfully')
def select(request,id):
    a=applymodel.objects.get(id=id)
    em=a.email
    if request.method=='POST':
        b=selectform(request.POST)
        if b.is_valid():
            em=b.cleaned_data['email']
            ms=b.cleaned_data['msg']
            message=ms
            subject = f'appointment letter'
            send_mail(subject, message, EMAIL_HOST_USER,[em])
            return HttpResponse("success")
    return render(request,"select.html",{'em':em})
def udetailview(request,id):
    b=User.objects.get(id=id)
    fn=b.first_name
    ln=b.last_name
    el=b.email
    if request.method=='POST':
        a=userprofform(request.POST,request.FILES)
        if a.is_valid():
            im=a.cleaned_data['image']
            nm=a.cleaned_data['fname']
            em=a.cleaned_data['email']
            re=a.cleaned_data['resume']
            ql=a.cleaned_data['eduquali']
            ex=a.cleaned_data['experience']
            ad=a.cleaned_data['address']
            ph=a.cleaned_data['phone']
            id=request.session['id']
            b=userprofmodel(uid=id,image=im,fname=nm,email=em,resume=re,eduquali=ql,experience=ex,address=ad,phone=ph)
            b.save()
            return render(request,'userprofdis.html',{'b':b})
        else:
            return HttpResponse('Details Upload Failed')
    return render(request,'userprofdetails.html',{'fn':fn,'ln':ln,'el':el})



