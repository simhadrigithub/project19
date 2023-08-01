from django.shortcuts import render

# Create your views here.
d={'goals':['father:reach good position','mother:care her childrens','simhadri:owner of mns companies','lavanye:coock food very tasty']}
def goals(request):
    return render(request,'goals.html',context=d)