// frontend/js/detalhe.js (VERSÃO COMPLETA COM AS DUAS CORREÇÕES)

// Função helper para pegar o token CSRF dos cookies do navegador
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener('DOMContentLoaded', () => {
    const packageDetailContent = document.getElementById('package-detail-content');
    let pacoteAtual = null;

    if (!pacoteId) {
        packageDetailContent.innerHTML = '<p class="text-center text-danger">Erro: Pacote não especificado.</p>';
        return;
    }

    async function fetchPackageDetails() {
        try {
            const response = await fetch(`http://127.0.0.1:8000/api/pacotes/${pacoteId}/`);
            if (!response.ok) throw new Error('Pacote não encontrado.');
            pacoteAtual = await response.json();
            displayPackageDetails(pacoteAtual);
        } catch (error) {
            packageDetailContent.innerHTML = `<p class="text-center text-danger">${error.message}</p>`;
        }
    }

    function displayPackageDetails(pkg) {
        document.title = pkg.nome;
        let secaoDatas = '';
        if (pkg.tipo === 'DATA_FIXA' && pkg.data_ida && pkg.data_volta) {
            secaoDatas = `<div class="d-flex align-items-center mb-2"><i class="bi bi-calendar-check fs-4 me-2"></i><span><strong>Ida:</strong> ${pkg.data_ida}</span></div><div class="d-flex align-items-center mb-3"><i class="bi bi-calendar-x fs-4 me-2"></i><span><strong>Volta:</strong> ${pkg.data_volta}</span></div>`;
        } else {
            secaoDatas = `<div class="d-flex align-items-center mb-3"><i class="bi bi-calendar-event fs-4 me-2"></i><span><strong>Datas flexíveis</strong><br><small>Disponível o ano todo.</small></span></div>`;
        }
        packageDetailContent.innerHTML = `
            <nav aria-label="breadcrumb"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="/">Início</a></li><li class="breadcrumb-item"><a href="/">Destinos</a></li><li class="breadcrumb-item active" aria-current="page">${pkg.destino}</li></ol></nav>
            <div class="row g-4">
                <div class="col-lg-8"><h1 class="mb-3">${pkg.nome}</h1><img src="${pkg.imagem_url}" class="img-fluid rounded shadow-sm mb-4 w-100" alt="${pkg.nome}" style="max-height: 450px; object-fit: cover;"><div class="card"><div class="card-header"><h5>Descrição Completa</h5></div><div class="card-body"><p class="lead">${pkg.descricao_curta}</p><hr><p>${pkg.descricao_longa.replace(/\\r\\n/g, '<br>')}</p></div></div></div>
                <div class="col-lg-4"><div class="card shadow-sm sticky-top" style="top: 20px;"><div class="card-body"><h3 class="text-primary my-3">R$ ${pkg.preco}</h3><p class="text-muted">a partir de</p><hr>${secaoDatas}<div class="d-grid"><button class="btn btn-primary btn-lg" data-bs-toggle="modal" data-bs-target="#reservaModal">Reservar Agora</button></div></div></div></div>
            </div>`;
    }

    const enviarReservaBtn = document.getElementById('enviarReservaBtn');
    const reservaForm = document.getElementById('reservaForm');
    const feedbackDiv = document.getElementById('form-feedback');

    enviarReservaBtn.addEventListener('click', async () => {
        if (!reservaForm.checkValidity()) {
            reservaForm.reportValidity();
            return;
        }

        const nome = document.getElementById('nomeCliente').value;
        const email = document.getElementById('emailCliente').value;
        const telefone = document.getElementById('telefoneCliente').value;
        const csrftoken = getCookie('csrftoken'); // Pega o token de segurança

        // 1. Enviar e-mail e salvar reserva via API
        try {
            const response = await fetch('/api/solicitar-reserva/', {
                method: 'POST',
                // Adiciona o token CSRF nos headers da requisição
                headers: { 
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken 
                },
                body: JSON.stringify({
                    pacoteId: pacoteId,
                    nome: nome,
                    email: email,
                    telefone: telefone
                })
            });
            const result = await response.json();
            if (!response.ok) throw new Error(result.erro || 'Falha ao enviar sua solicitação.');
            
            feedbackDiv.innerHTML = `<div class="alert alert-success">Sua solicitação foi enviada com sucesso! Em breve um consultor entrará em contato.</div>`;

        } catch (error) {
            feedbackDiv.innerHTML = `<div class="alert alert-danger">${error.message}</div>`;
        }

        // 2. Abrir conversa no WhatsApp (usando o número dinâmico)
        const numeroAgencia = window.siteConfig ? window.siteConfig.whatsapp_numero : '';
        if (numeroAgencia) {
            const mensagemWhats = `Olá! Tenho interesse em reservar o pacote "${pacoteAtual.nome}".\n\nMeus dados:\nNome: ${nome}\nE-mail: ${email}\nTelefone: ${telefone}`;
            const whatsappURL = `https://wa.me/${numeroAgencia}?text=${encodeURIComponent(mensagemWhats)}`;
            window.open(whatsappURL, '_blank');
        }
    });

    fetchPackageDetails();
});