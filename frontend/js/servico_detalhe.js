// frontend/js/servico_detalhe.js

document.addEventListener('DOMContentLoaded', () => {
    const servicoDetailContent = document.getElementById('servico-detail-content');

    // A variável 'servicoId' é fornecida pelo template HTML
    if (!servicoId) {
        servicoDetailContent.innerHTML = '<p class="text-center text-danger">Erro: Serviço não especificado.</p>';
        return;
    }

    async function fetchServicoDetails() {
        try {
            const response = await fetch(`/api/servicos/item/${servicoId}/`);
            if (!response.ok) throw new Error('Serviço não encontrado.');
            const servico = await response.json();
            displayServicoDetails(servico);
        } catch (error) {
            servicoDetailContent.innerHTML = `<p class="text-center text-danger">${error.message}</p>`;
        }
    }

    function displayServicoDetails(servico) {
        document.title = servico.nome;
        servicoDetailContent.innerHTML = `
            <div class="row g-4">
                <div class="col-lg-8">
                    <h1 class="mb-3">${servico.nome}</h1>
                    <img src="${servico.imagem_url}" class="img-fluid rounded shadow-sm mb-4 w-100" alt="${servico.nome}" style="max-height: 450px; object-fit: cover;">
                    <div class="card"><div class="card-header"><h5>Descrição Completa</h5></div><div class="card-body"><p class="lead">${servico.descricao_curta}</p><hr><p>${servico.descricao_longa}</p></div></div>
                </div>
                <div class="col-lg-4">
                    <div class="card shadow-sm sticky-top" style="top: 20px;">
                        <div class="card-body">
                            <h3 class="text-primary my-3">R$ ${servico.preco}</h3>
                            <p class="text-muted">a partir de</p>
                            <hr>
                            <div class="d-grid">
                                <a href="#" class="btn btn-primary btn-lg">Solicitar Cotação</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>`;
    }

    fetchServicoDetails();
});