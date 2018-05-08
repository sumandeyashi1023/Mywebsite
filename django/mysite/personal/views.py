from django.shortcuts import render


def index(request):
    return render(request,'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html',{'content':['If you would like to contact me, please email me.','bansodeyallaling06@gmail.com / bansode.yallalingram2014@vit.ac.in']})
