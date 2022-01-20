from django.shortcuts import render
from django.http import HttpResponse
from .models import Transacao
from .forms import TransacaoForm
from django.shortcuts import redirect

def transacao(request):
    data = {}
    data['transacao'] = Transacao.objects.all()
    return render(request, 'transacao.html', data)

def novatransacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('transacao')
        
    data['form'] = form
    return render(request,'form.html',data )

def atualizar(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)
    if form.is_valid():
        form.save()
        return redirect('transacao')
    data['obj'] = transacao     
    data['form'] = form
    return render(request,'form.html',data ) 

def deletar(request,pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    
    return redirect('transacao')
