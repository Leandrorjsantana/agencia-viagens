// frontend/js/detalhe.js (VERSÃO COMPLETA E CORRIGIDA)

document.addEventListener('DOMContentLoaded', () => {
    const packageDetailContent = document.getElementById('package-detail-content');
    const urlParams = new URLSearchParams(window.location.search);
    const packageId = urlParams.get('id');

    // Variável para guardar os dados do pacote
    let pacoteAtual = null;

    if (!packageId) {
        packageDetailContent.innerHTML = '<p class="text-center text-danger">Erro: Pacote não especificado.</p>';
        return;
    }

    async function fetchPackageDetails() {
        try {
            const response = await fetch(`http://127.0.0.1:8000/api/pacotes/${packageId}/`);
            if (!response.ok) throw new Error('Pacote não encontrado.');
            
            pacoteAtual = await response.json(); // Salva os dados do pacote
            displayPackageDetails(pacoteAtual);
        } catch (error) {
            packageDetailContent.innerHTML = `<p class="text-center text-danger">${error.message}</p>`;
        }
    }

    function displayPackageDetails(pkg) {
        document.title = pkg.nome;
        packageDetailContent.innerHTML = `
            <nav aria-label="breadcrumb"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Início</a></li><li class="breadcrumb-item"><a href="#">Destinos</a></li><li class="breadcrumb-item active" aria-current="page">${pkg.destino}</li></ol></nav>
            <div class="row g-4">
                <div class="col-lg-8">
                    <h1 class="mb-3">${pkg.nome}</h1>
                    <img src="${pkg.imagem_url}" class="img-fluid rounded shadow-sm mb-4 w-100" alt="${pkg.nome}" style="max-height: 450px; object-fit: cover;">
                    <div class="card"><div class="card-header"><h5>Descrição Completa</h5></div><div class="card-body"><p class="lead">${pkg.descricao_curta}</p><hr><p>${pkg.descricao_longa.replace(/\\r\\n/g, '<br>')}</p></div></div>
                </div>
                <div class="col-lg-4">
                    <div class="card shadow-sm sticky-top" style="top: 20px;">
                        <div class="card-body">
                            <h3 class="text-primary my-3">R$ ${pkg.preco}</h3>
                            <p class="text-muted">por pessoa</p>
                            <hr>
                            <div class="d-flex align-items-center mb-2"><i class="bi bi-calendar-check fs-4 me-2"></i><span><strong>Ida:</strong> ${pkg.data_ida}</span></div>
                            <div class="d-flex align-items-center mb-3"><i class="bi bi-calendar-x fs-4 me-2"></i><span><strong>Volta:</strong> ${pkg.data_volta}</span></div>
                            <div class="d-grid">
                                <button class="btn btn-primary btn-lg" data-bs-toggle="modal" data-bs-target="#reservaModal">Reservar Agora</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>`;
    }

    // --- NOVA LÓGICA PARA O FORMULÁRIO DE RESERVA ---
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

        // 1. Enviar e-mail via API
        try {
            const response = await fetch('http://127.0.0.1:8000/api/solicitar-reserva/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    pacoteId: packageId,
                    nome: nome,
                    email: email,
                    telefone: telefone
                })
            });
            const result = await response.json();
            if (!response.ok) throw new Error(result.erro || 'Falha ao enviar e-mail.');
            
            feedbackDiv.innerHTML = `<div class="alert alert-success">Sua solicitação foi enviada por e-mail!</div>`;

        } catch (error) {
            feedbackDiv.innerHTML = `<div class="alert alert-danger">${error.message}</div>`;
        }

        // 2. Abrir conversa no WhatsApp
        const numeroAgencia = '5511999999999'; // <-- COLOQUE AQUI O WHATSAPP DA SUA AGÊNCIA (formato 55 + DDD + NUMERO)
        const mensagemWhats = `Olá! Tenho interesse em reservar o pacote "${pacoteAtual.nome}".\n\nMeus dados:\nNome: ${nome}\nE-mail: ${email}\nTelefone: ${telefone}`;
        const whatsappURL = `https://wa.me/${numeroAgencia}?text=${encodeURIComponent(mensagemWhats)}`;
        
        // Abre o WhatsApp em uma nova aba
        window.open(whatsappURL, '_blank');
    });

    fetchPackageDetails();
});