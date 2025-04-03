from django.shortcuts import render

def resultadoCotacao(request):
    return render(request, 'resultadoCotacao/index.html')