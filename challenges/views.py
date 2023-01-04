from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
# Create your views here.

monthly_challenges = {
    "january":"learn python",
    "february":"learn react",
    "march":"learn nodejs",
    "april":"make projects",
    "may":"learn docker and kubernetes",
    "june":"learn golang",
    "july":"learn docker",
    "august":"learn aws fundamanetals",
    "september":"learn aws more fundamnetals",
    "october":"leanr aws cloud architect",
    "november":"get certified in aws",
    "december":"chill as hell"
}
def index_number(request,month):
    months=list(monthly_challenges.keys())
    if month>len(months):
        return HttpResponseNotFound("Wrong month entered")
    forward_month=months[month-1]
    return HttpResponseRedirect("/challenges/"+ forward_month)

def index(request,month):
    text=None
    try:
        
        text=monthly_challenges[month]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("wrong month entered")
    
