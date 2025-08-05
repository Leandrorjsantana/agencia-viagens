// frontend/js/servicos.js

document.addEventListener('DOMContentLoaded', () => {
    const gridMapping = {
        'HOSPEDAGEM': 'hospedagem-grid', 'PASSAGEM': 'passagem-grid', 'CRUZEIRO': 'cruzeiro-grid',
        'SEGURO': 'seguro-grid', 'DISNEY': 'disney-grid', 'OFERTA': 'oferta-grid',
    };

    async function fetchServicos() {
        try {
            const response = await fetch('/api/servicos/');
            if (!response.ok) return;
            const servicosAgrupados = await response.json();
            displayServicos(servicosAgrupados);
        } catch (error) {
            console.error('Erro ao carregar serviços:', error);
        }
    }

    function displayServicos(servicosAgrupados) {
        for (const categoria in servicosAgrupados) {
            const gridId = gridMapping[categoria];
            const gridElement = document.getElementById(gridId);
            
            if (gridElement) {
                const servicos = servicosAgrupados[categoria];
                gridElement.innerHTML = '';

                servicos.forEach(servico => {
                    const cardWrapper = document.createElement('div');
                    cardWrapper.className = 'col';
                    
                    // --- LINK DO CARD ATUALIZADO ---
                    cardWrapper.innerHTML = `
                        <a href="/servicos/${categoria.toLowerCase()}/" class="card-link">
                            <div class="card h-100 shadow-sm text-white">
                                <img src="${servico.imagem_url}" class="card-img" alt="${servico.nome}" style="height: 250px; object-fit: cover;">
                                <div class="card-img-overlay d-flex flex-column justify-content-end p-4" style="background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);">
                                    <h5 class="card-title">${servico.nome}</h5>
                                    <p class="card-text small">${servico.descricao ? servico.descricao.substring(0, 100) : ''}</p>
                                </div>
                            </div>
                        </a>
                    `;
                    gridElement.appendChild(cardWrapper);
                });
            }
        }
    }

    fetchServicos();
});