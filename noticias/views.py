from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Comentario

# 1. Página inicial: Lista todos os artigos
def lista_artigos(request):
    artigos = Artigo.objects.all()
    return render(request, 'lista_artigos.html', {'artigos': artigos})

# 2. Página do artigo: Mostra os detalhes de um artigo específico
def detalhe_artigo(request, id_artigo):
    # Procura o artigo pelo ID, se não existir dá erro 404
    artigo = get_object_or_404(Artigo, id=id_artigo)
    return render(request, 'detalhe_artigo.html', {'artigo': artigo})

# 3. Página de comentários: Mostra e guarda novos comentários
def comentarios_artigo(request, id_artigo):
    artigo = get_object_or_404(Artigo, id=id_artigo)
    
    # Se o utilizador submeter um comentário (método POST)
    if request.method == 'POST':
        texto_comentario = request.POST.get('texto_comentario')
        if texto_comentario: # Se o campo não estiver vazio
            Comentario.objects.create(artigo=artigo, texto=texto_comentario)
            # Recarrega a página para mostrar o novo comentário
            return redirect('comentarios_artigo', id_artigo=artigo.id)
            
    return render(request, 'comentarios_artigo.html', {'artigo': artigo})