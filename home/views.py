from django.shortcuts import render
from django.views import View 


class index(View):
    def get(self,request,*args,**kwargs):
        return render(request,'home.html')




#templates