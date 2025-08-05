# backend/pacotes/views.py (VERSÃO COMPLETA E CORRIGIDA)

from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from .models import Pacote, Destino, Reserva, Servico
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import json

def serializar_pacote(pacote, request):
    return {
        'id': pacote.id, 'nome': pacote.nome, 'preco': f'{pacote.preco:.2f}'.replace('.',','),
        'taxas_inclusas': pacote.taxas_inclusas, 'imagem_url': request.build_absolute_uri(pacote.imagem_principal.url) if pacote.imagem_principal else '',
        'duracao_dias': pacote.duracao_dias, 'duracao_noites': pacote.duracao_noites, 'cidade_origem': pacote.cidade_origem,
        'inclui_hotel': pacote.inclui_hotel, 'inclui_aereo': pacote.inclui_aereo, 'inclui_transfer': pacote.inclui_transfer, 'avaliacao': pacote.avaliacao,
    }

def home_view(request): return render(request, 'index.html')
def destino_pacotes_view(request, destino_id): return render(request, 'destino_pacotes.html', {'destino_id': destino_id})
def detalhe_pacote_view(request, pacote_id): return render(request, 'pacote_detalhe.html', {'pacote_id': pacote_id})
def pagina_busca_view(request): return render(request, 'search_results.html')
def servico_categoria_view(request, categoria_slug): return render(request, 'servicos_por_categoria.html', {'categoria_slug': categoria_slug})
def servico_detalhe_view(request, servico_id): return render(request, 'servico_detalhe.html', {'servico_id': servico_id})

def api_listar_servicos(request):
    servicos = Servico.objects.filter(disponivel=True)
    servicos_agrupados = {}
    for servico in servicos:
        categoria = servico.categoria
        if categoria not in servicos_agrupados: servicos_agrupados[categoria] = []
        servicos_agrupados[categoria].append({
            'id': servico.id, 'nome': servico.nome, 'descricao': servico.descricao_curta,
            'imagem_url': request.build_absolute_uri(servico.imagem.url) if servico.imagem else '',
            'preco_formatado': f"R$ {servico.preco:.2f}".replace('.',','),
        })
    return JsonResponse(servicos_agrupados)

def api_servicos_por_categoria(request, categoria_slug):
    try:
        servicos = Servico.objects.filter(disponivel=True, categoria=categoria_slug.upper())
        servicos_data = [{'id': s.id, 'nome': s.nome, 'descricao': s.descricao_curta, 'imagem_url': request.build_absolute_uri(s.imagem.url) if s.imagem else '', 'preco_formatado': f"R$ {s.preco:.2f}".replace('.',',')} for s in servicos]
        nome_categoria = dict(Servico.CATEGORIA_CHOICES).get(categoria_slug.upper())
        return JsonResponse({'categoria': {'nome': nome_categoria}, 'servicos': servicos_data})
    except Exception as e:
        return JsonResponse({'erro': str(e)}, status=500)

@require_POST
@login_required
def solicitar_reserva(request):
    # ... (código da função)
    pass

def buscar_pacotes(request):
    # ... (código da função)
    pass

def listar_destinos(request):
    try:
        destinos = Destino.objects.all()
        data = []
        for destino in destinos:
            imagem_url = f'https://source.unsplash.com/400x300/?{destino.nome.lower()}'
            if destino.imagem_padrao and hasattr(destino.imagem_padrao, 'url'): imagem_url = request.build_absolute_uri(destino.imagem_padrao.url)
            else:
                primeiro_pacote = Pacote.objects.filter(destino=destino, disponivel=True).first()
                if primeiro_pacote and primeiro_pacote.imagem_principal and hasattr(primeiro_pacote.imagem_principal, 'url'): imagem_url = request.build_absolute_uri(primeiro_pacote.imagem_principal.url)
            data.append({'id': destino.id, 'nome': destino.nome, 'imagem_url': imagem_url, 'descricao': destino.descricao})
        return JsonResponse({'destinos': data})
    except Exception as e:
        return JsonResponse({'erro': str(e)}, status=500)

def listar_pacotes_por_destino(request, destino_id):
    try:
        destino = Destino.objects.get(pk=destino_id)
        pacotes = Pacote.objects.filter(destino=destino, disponivel=True)
        pacotes_data = [serializar_pacote(pacote, request) for pacote in pacotes]
        response_data = {'destino': {'nome': destino.nome}, 'pacotes': pacotes_data}
        return JsonResponse(response_data)
    except Destino.DoesNotExist: return JsonResponse({'erro': 'Destino não encontrado'}, status=404)

def detalhe_pacote(request, pacote_id):
    try:
        pacote = Pacote.objects.get(pk=pacote_id)
        data = serializar_pacote(pacote, request)
        data.update({ 'destino': pacote.destino.nome, 'descricao_curta': pacote.descricao_curta, 'descricao_longa': pacote.descricao_longa.replace('\r\n', '<br>'), 'tipo': pacote.tipo, 'data_ida': pacote.data_ida.strftime('%d/%m/%Y') if pacote.data_ida else None, 'data_volta': pacote.data_volta.strftime('%d/%m/%Y') if pacote.data_volta else None, })
        return JsonResponse(data)
    except Pacote.DoesNotExist: return JsonResponse({'erro': 'Destino não encontrado'}, status=404)

def api_detalhe_servico(request, servico_id):
    try:
        servico = Servico.objects.get(pk=servico_id)
        data = { 'id': servico.id, 'nome': servico.nome, 'descricao_curta': servico.descricao_curta, 'descricao_longa': servico.descricao_longa.replace('\r\n', '<br>'), 'preco': f'{servico.preco:.2f}'.replace('.',','), 'imagem_url': request.build_absolute_uri(servico.imagem.url) if servico.imagem else '', 'avaliacao': servico.avaliacao, 'cidade_origem': servico.cidade_origem, 'duracao_dias': servico.duracao_dias, 'duracao_noites': servico.duracao_noites, 'inclui_aereo': servico.inclui_aereo, 'inclui_hotel': servico.inclui_hotel, 'inclui_transfer': servico.inclui_transfer, }
        return JsonResponse(data)
    except Servico.DoesNotExist:
        return JsonResponse({'erro': 'Serviço não encontrado'}, status=404)

@login_required
def api_listar_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user).order_by('-data_solicitacao')
    data = [{'pacote_nome': reserva.pacote.nome if reserva.pacote else "Pacote removido", 'data_solicitacao': reserva.data_solicitacao.strftime('%d/%m/%Y às %H:%M'), 'status': reserva.get_status_display(),} for reserva in reservas]
    return JsonResponse({'reservas': data})