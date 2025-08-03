from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import userForm
from service.models import Student
from news.models import News

def homePage(request):
    serviceData=Student.objects.all().order_by('-marks')[:3] # sorted in decending order and limit the students by sclicing
    data={
        'serviceData':serviceData
    }
    return render(request,'home.html',data)
 

def aboutPage(request):
    
    output = None
    if request.method == "GET":
        output = request.GET.get('output')
    return render(request, 'about.html', {"output": output})

def contactPage(request):
  return render(request,'contact.html')

def submitForm(request):
  if request.method == "POST":
        try:
            n1 = int(request.POST.get("num1"))
            n2 = int(request.POST.get("num2"))
            finalAns = n1 + n2
            return HttpResponse(finalAns)
          
        except :
          pass

def servicePage(request):
  return render(request,'services.html')

def calculator(request):
    result = ''
    num1 = num2 = ''
    operation = ''
    if request.method == "POST":
        num1 = request.POST.get('num1', '')
        num2 = request.POST.get('num2', '')
        operation = request.POST.get('operation', '')
        try:
            n1 = float(num1)
            n2 = float(num2)
            if operation == 'add':
                result = n1 + n2
            elif operation == 'subtract':
                result = n1 - n2
            elif operation == 'multiply':
                result = n1 * n2
            elif operation == 'divide':
                result = n1 / n2 if n2 != 0 else 'Error'
        except Exception:
            result = 'Invalid input'
    context = {
        'result': result,
        'num1': num1,
        'num2': num2,
        'operation': operation
    }
    return render(request, 'calculator.html', context)
  
def marksheet(request):
    data = {}
    if request.method == "POST":
        try:
            s1 = int(request.POST.get('sub1', 0))
            s2 = int(request.POST.get('sub2', 0))
            s3 = int(request.POST.get('sub3', 0))
            s4 = int(request.POST.get('sub4', 0))
            s5 = int(request.POST.get('sub5', 0))
            t = s1 + s2 + s3 + s4 + s5
            per = t / 5
            if per >= 60:
                division = "1st"
            elif per >= 50:
                division = "2nd"
            elif per >= 33:
                division = "3rd"
            else:
                division = "Fail"
            data = {
                "total": t,
                "percent": f"{per:.2f}%",
                "div": division,
                "sub1": s1,
                "sub2": s2,
                "sub3": s3,
                "sub4": s4,
                "sub5": s5
            }
        except Exception as e:
            data["error"] = "Invalid input"
    return render(request, 'marksheet.html', data)

def userformPage(request):
    finalAns = ''
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            n1 = int(form.cleaned_data['num1'])
            n2 = int(form.cleaned_data['num2'])
            finalAns = n1 + n2
            url = "/about/?output={}".format(finalAns)
            return HttpResponseRedirect(url)
    else:
        form = userForm()
    return render(request, 'userform.html', {'form': form, 'output': finalAns})

def NewsDetails(request, newsId):
    try:
        news = News.objects.get(id=newsId)
    except News.DoesNotExist:
        return HttpResponse("News not found", status=404)
    return render(request, 'news_detail.html', {'news': news})

def NewsList(request):
    newsData = News.objects.all()
    return render(request, 'news.html', {'newsData': newsData})
