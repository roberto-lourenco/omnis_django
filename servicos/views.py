from django.shortcuts import render

def servicos(request):
    return render(request, 'servicos/index.html')
