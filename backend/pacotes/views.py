# backend/pacotes/views.py (VERSÃO CORRIGIDA E COMPLETA)

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
import json
from .models import Pacote, Destino

@require_POST
def solicitar_reserva(request):
    try:
        data = json.loads(request.body)
        pacote_id = data.get('pacoteId')
        nome_cliente = data.get('nome')
        email_cliente = data.get('email')
        telefone_cliente = data.get('telefone')
        pacote = Pacote.objects.get(pk=pacote_id)
        assunto = f"Nova Solicitação de Reserva: {pacote.nome}"
        mensagem = f"""
        Você recebeu uma nova solicitação de reserva.
        Cliente: {nome_cliente}
        E-mail: {email_cliente}
        Telefone: {telefone_cliente}
        Pacote: {pacote.nome} (ID: {pacote.id})
        """
        email_remetente = 'nao-responda@suaagencia.com'
        lista_destinatarios = ['email-da-sua-agencia@exemplo.com']
        send_mail(assunto, mensagem, email_remetente, lista_destinatarios)
        return JsonResponse({'sucesso': True, 'mensagem': 'Solicitação enviada com sucesso!'})
    except Exception as e:
        return JsonResponse({'sucesso': False, 'erro': str(e)}, status=400)

def buscar_pacotes(request):
    query_destino = request.GET.get('destino', '')
    pacotes = Pacote.objects.filter(disponivel=True)
    if query_destino:
        pacotes = pacotes.filter(destino__nome__icontains=query_destino)
    data = []
    for pacote in pacotes:
        data.append({'id': pacote.id, 'nome': pacote.nome, 'preco': f'{pacote.preco:.2f}'.replace('.',','), 'imagem_url': request.build_absolute_uri(pacote.imagem_principal.url) if pacote.imagem_principal else ''})
    return JsonResponse({'pacotes': data})

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
            pacotes_data.append({'id': pacote.id, 'nome': pacote.nome, 'preco': f'{pacote.preco:.2f}'.replace('.',','), 'imagem_url': request.build_absolute_uri(pacote.imagem_principal.url) if pacote.imagem_principal else ''})
        response_data = {'destino': {'nome': destino.nome}, 'pacotes': pacotes_data}
        return JsonResponse(response_data)
    except Destino.DoesNotExist:
        return JsonResponse({'erro': 'Destino não encontrado'}, status=404)

# --- FUNÇÃO QUE ESTAVA FALTANDO, ADICIONADA NOVAMENTE ---
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
# --------------------------------------------------------

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
            'imagem_url': request.build_absolute_uri(pacote.imagem_principal.url) if pacote.imagem_principal else '',
            'tipo': pacote.tipo,
            'data_ida': pacote.data_ida.strftime('%d/%m/%Y') if pacote.data_ida else None,
            'data_volta': pacote.data_volta.strftime('%d/%m/%Y') if pacote.data_volta else None,
        }
        return JsonResponse(data)
    except Pacote.DoesNotExist:
        return JsonResponse({'erro': 'Pacote não encontrado'}, status=404)