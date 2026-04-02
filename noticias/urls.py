from django.urls import path
from . import views

urlpatterns = [
    # O caminho vazio '' será a página principal
    path('', views.lista_artigos, name='lista_artigos'),
    
    # Exemplo de URL: /artigo/1/
    path('artigo/<int:id_artigo>/', views.detalhe_artigo, name='detalhe_artigo'),
    
    # Exemplo de URL: /artigo/1/comentarios/
    path('artigo/<int:id_artigo>/comentarios/', views.comentarios_artigo, name='comentarios_artigo'),
]