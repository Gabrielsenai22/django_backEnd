from django.shortcuts import render, HttpResponse
from .models import Produto, Preco_Produto

def raiz(requests):
    a = 120732103720937109
    return render(requests, "raiz.html", {"ok": a})

def produtos(request):
    cod_produto = request.POST.get("cod_produto")
    descricao = request.POST.get("descricao")
    produtos = Produto(
      cod_produto=cod_produto,
      descricao=descricao
    )
    produtos.save()

    preco: object = request.POST.get('preco')
    preco_produto = Preco_Produto(
        preco_produto=preco,
        cod_produto=Produto.objects.last()
    )
    preco_produto.save()
    #return render(request, "ler produto.html")



    return render(request, 'produtos_cadastrar.html')

def consultar_ultimo(request):
    ultimo = Produto.objects.all()
    preco = Preco_Produto.objects.all()
    return render(request, 'ler produto.html', {'ultimo': ultimo, "preco": preco})
