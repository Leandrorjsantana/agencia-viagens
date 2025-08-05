// frontend/js/servicos_categoria.js

document.addEventListener('DOMContentLoaded', () => {
    const servicosGrid = document.getElementById('servicos-grid');
    const categoriaNome = document.getElementById('categoria-nome');

    if (!categoriaSlug) {
        categoriaNome.textContent = 'Categoria não encontrada.';
        return;
    }

    async function fetchServicosPorCategoria() {
        try {
            const response = await fetch(`/api/servicos/${categoriaSlug}/`);
            if (!response.ok) throw new Error('Não foi possível carregar os serviços.');
            const data = await response.json();
            displayServicos(data);
        } catch (error) {
            servicosGrid.innerHTML = `<p class="text-danger text-center">${error.message}</p>`;
        }
    }

    function displayServicos(data) {
        categoriaNome.textContent = data.categoria.nome;
        document.title = data.categoria.nome;
        servicosGrid.innerHTML = '';

        if (data.servicos.length === 0) {
            servicosGrid.innerHTML = `<p class="text-center col-12">Nenhum item disponível para "${data.categoria.nome}" no momento.</p>`;
            return;
        }

        data.servicos.forEach(servico => {
            const card = document.createElement('div');
            card.className = 'col';
            
            // --- LINK ATUALIZADO AQUI ---
            card.innerHTML = `
                <a href="/servicos/item/${servico.id}/" class="text-decoration-none">
                    <div class="card h-100 shadow-sm">
                        <img src="${servico.imagem_url}" class="card-img-top" alt="${servico.nome}" style="height: 180px; object-fit: cover;">
                        <div class="card-body">
                            <h5 class="card-title">${servico.nome}</h5>
                            <p class="card-text small text-muted">${servico.descricao}</p>
                            <p class="fw-bold">A partir de R$ ${servico.preco_formatado}</p>
                        </div>
                    </div>
                </a>
            `;
            servicosGrid.appendChild(card);
        });
    }

    fetchServicosPorCategoria();
});