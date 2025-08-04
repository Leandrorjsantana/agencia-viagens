// frontend/js/destino.js (VERSÃO COMPLETA E CORRIGIDA)

document.addEventListener('DOMContentLoaded', () => {

    const packagesGrid = document.getElementById('packages-grid');
    const destinoNome = document.getElementById('destino-nome');

    // A variável 'destinoId' agora é fornecida pelo template HTML.
    if (!destinoId) {
        destinoNome.textContent = 'Destino não encontrado.';
        return;
    }

    async function fetchPackagesByDestino() {
        try {
            const response = await fetch(`http://127.0.0.1:8000/api/destinos/${destinoId}/pacotes/`);
            if (!response.ok) {
                throw new Error('Não foi possível carregar os pacotes para este destino.');
            }
            const data = await response.json();
            displayPackages(data);
        } catch (error) {
            packagesGrid.innerHTML = `<p class="text-danger text-center col-12">${error.message}</p>`;
        }
    }

    function displayPackages(data) {
        destinoNome.textContent = `Pacotes para ${data.destino.nome}`;
        document.title = `Pacotes para ${data.destino.nome}`;
        packagesGrid.innerHTML = '';

        if (data.pacotes.length === 0) {
            packagesGrid.innerHTML = '<p class="text-center col-12">Nenhum pacote disponível para este destino no momento.</p>';
            return;
        }

        data.pacotes.forEach(pkg => {
            // Gera a tag de Hotel + Aéreo
            let inclusoText = '';
            if (pkg.inclui_hotel && pkg.inclui_aereo) {
                inclusoText = 'Hotel + Aéreo';
            } else if (pkg.inclui_hotel) {
                inclusoText = 'Hotel';
            } else if (pkg.inclui_aereo) {
                inclusoText = 'Aéreo';
            }

            const card = document.createElement('div');
            card.className = 'col';
            
            // --- CÓDIGO DO NOVO CARD IDÊNTICO AO PRINT ---
            card.innerHTML = `
            <div class="package-card h-100">
                <div class="package-card-img-wrapper">
                    <img src="${pkg.imagem_url}" class="card-img-top" alt="${pkg.nome}" style="height: 200px; object-fit: cover;">
                    ${pkg.duracao_dias ? `<div class="package-card-overlay">${pkg.duracao_dias} DIAS / ${pkg.duracao_noites} NOITES</div>` : ''}
                </div>
                <div class="package-card-content d-flex flex-column">
                    <div class="package-card-label">PACOTE</div>
                    <h3 class="package-card-title">${pkg.nome}</h3>
                    
                    ${pkg.avaliacao ? `
                    <div class="package-card-rating">
                        <span class="badge">${pkg.avaliacao}</span>
                        <span class="stars">
                            <i class="bi bi-star-fill"></i>
                            <i class="bi bi-star-fill"></i>
                            <i class="bi bi-star-fill"></i>
                            <i class="bi bi-star-fill"></i>
                            <i class="bi bi-star-half"></i>
                        </span>
                    </div>
                    ` : ''}

                    <div class="package-card-details">
                        ${pkg.cidade_origem ? `Saindo de ${pkg.cidade_origem}<br>` : ''}
                        ${inclusoText ? `${inclusoText}<br>` : ''}
                    </div>
                    
                    <div class="package-card-price-info mt-auto">
                        <div class="price-label">Preço por pessoa</div>
                        <div class="price-value">R$ ${pkg.preco}</div>
                        <div class="price-notes">${pkg.taxas_inclusas ? 'Taxas e impostos inclusos' : 'Taxas e impostos não inclusos'}</div>
                    </div>
                </div>
            </div>
            `;
            
            // O link <a> agora envolve o card inteiro
            const link = document.createElement('a');
            link.href = `/pacotes/${pkg.id}/`;
            link.className = 'text-decoration-none';
            link.appendChild(card);
            packagesGrid.appendChild(link);
        });
    }

    fetchPackagesByDestino();
});