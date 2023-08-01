from django.shortcuts import render

# Create your views here.
d={'occupations':['father:contractor','mother:house wife','simhadri:studying mca','chinna:studying 10th class','lavanye:learning coocking']}
def occupations(request):
    return render(request,'occupations.html',context=d)