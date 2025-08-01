# backend/pacotes/views.py (VERSÃO CORRIGIDA E COMPLETA)

from django.http import JsonResponse
from .models import Pacote, Destino

# --- NOVA FUNÇÃO DE BUSCA ADICIONADA ---
def buscar_pacotes(request):
    # Pega o parâmetro 'destino' da URL (ex: ?destino=Rio)
    query_destino = request.GET.get('destino', '')
    
    # Inicia a busca com todos os pacotes disponíveis
    pacotes = Pacote.objects.filter(disponivel=True)

    # Se um termo de busca para 'destino' foi fornecido, filtra os resultados
    if query_destino:
        # __icontains faz uma busca "case-insensitive" (não diferencia maiúsculas/minúsculas)
        # que contém o texto pesquisado.
        pacotes = pacotes.filter(destino__nome__icontains=query_destino)

    data = []
    for pacote in pacotes:
        data.append({
            'id': pacote.id,
            'nome': pacote.nome,
            'preco': f'{pacote.preco:.2f}'.replace('.',','),
            'imagem_url': request.build_absolute_uri(pacote.imagem_principal.url) if pacote.imagem_principal else ''
        })
    
    return JsonResponse({'pacotes': data})
# ----------------------------------------

def listar_destinos(request):
    destinos = Destino.objects.all()
    data = []
    for destino in destinos:
        imagem_url = f'https://source.unsplash.com/400x300/?{destino.nome.lower()}'
        if destino.imagem_padrao:
            imagem_url = request.build_absolute_uri(destino.imagem_padrao.url)
        else:
            primeiro_pacote = Pacote.objects.filter(destino=destino, disponivel=True).first()
            if primeiro_pacote and primeiro_pacote.imagem_principal:
                imagem_url = request.build_absolute_uri(primeiro_pacote.imagem_principal.url)
        data.append({'id': destino.id, 'nome': destino.nome, 'imagem_url': imagem_url})
    return JsonResponse({'destinos': data})

def listar_pacotes_por_destino(request, destino_id):
    try:
        destino = Destino.objects.get(pk=destino_id)
        pacotes = Pacote.objects.filter(destino=destino, disponivel=True)
        pacotes_data = []
        for pacote in pacotes:
            pacotes_data.append({
                'id': pacote.id,
                'nome': pacote.nome,
                'preco': f'{pacote.preco:.2f}'.replace('.',','),
                'imagem_url': request.build_absolute_uri(pacote.imagem_principal.url) if pacote.imagem_principal else ''
            })
        response_data = {'destino': {'nome': destino.nome}, 'pacotes': pacotes_data}
        return JsonResponse(response_data)
    except Destino.DoesNotExist:
        return JsonResponse({'erro': 'Destino não encontrado'}, status=404)

def listar_pacotes(request):
    pacotes = Pacote.objects.filter(disponivel=True)
    data = []
    for pacote in pacotes:
        data.append({
            'id': pacote.id,
            'nome': pacote.nome,
            'destino': pacote.destino.nome,
            'preco': f'{pacote.preco:.2f}'.replace('.',','),
            'imagem_url': request.build_absolute_uri(pacote.imagem_principal.url) if pacote.imagem_principal else ''
        })
    return JsonResponse({'pacotes': data})

def detalhe_pacote(request, pacote_id):
    try:
        pacote = Pacote.objects.get(pk=pacote_id)
        data = {
            'id': pacote.id,
            'nome': pacote.nome,
            'destino': pacote.destino.nome,
            'descricao_curta': pacote.descricao_curta,
            'descricao_longa': pacote.descricao_longa.replace('\r\n', '<br>'),
            'preco': f'{pacote.preco:.2f}'.replace('.',','),
            'data_ida': pacote.data_ida.strftime('%d/%m/%Y'),
            'data_volta': pacote.data_volta.strftime('%d/%m/%Y'),
            'imagem_url': request.build_absolute_uri(pacote.imagem_principal.url) if pacote.imagem_principal else ''
        }
        return JsonResponse(data)
    except Pacote.DoesNotExist:
        return JsonResponse({'erro': 'Pacote não encontrado'}, status=404)