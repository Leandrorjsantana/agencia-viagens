// frontend/js/search_results.js

document.addEventListener('DOMContentLoaded', () => {
    const packagesGrid = document.getElementById('packages-grid');
    const searchTitle = document.getElementById('search-title');

    // Pega TODOS os parâmetros da URL
    const urlParams = new URLSearchParams(window.location.search);
    const destinoQuery = urlParams.get('destino');

    // Monta um título dinâmico
    if (destinoQuery) {
        searchTitle.textContent = `Exibindo resultados para "${destinoQuery}"`;
        document.title = `Busca por "${destinoQuery}"`;
    } else {
        searchTitle.textContent = 'Exibindo todos os pacotes';
    }

    async function fetchSearchResults() {
        try {
            // Constrói a URL da API de busca repassando TODOS os parâmetros
            const apiUrl = `http://127.0.0.1:8000/api/search/?${urlParams.toString()}`;
            
            const response = await fetch(apiUrl);
            if (!response.ok) {
                throw new Error('Não foi possível realizar a busca.');
            }
            const data = await response.json();
            displayPackages(data.pacotes);
        } catch (error) {
            packagesGrid.innerHTML = `<p class="text-danger text-center col-12">${error.message}</p>`;
        }
    }

    function displayPackages(packages) {
        packagesGrid.innerHTML = '';
        if (packages.length === 0) {
            let message = 'Nenhum pacote encontrado para esta busca.';
            if(destinoQuery) message = `Nenhum pacote encontrado para "${destinoQuery}".`
            packagesGrid.innerHTML = `<p class="text-center col-12">${message}</p>`;
            return;
        }
        packages.forEach(pkg => {
            let inclusoText = '';
            if (pkg.inclui_hotel && pkg.inclui_aereo) inclusoText = 'Hotel + Aéreo';
            else if (pkg.inclui_hotel) inclusoText = 'Hotel';
            else if (pkg.inclui_aereo) inclusoText = 'Aéreo';

            const card = document.createElement('div');
            card.className = 'col';
            card.innerHTML = `
            <div class="package-card h-100">
                <div class="package-card-img-wrapper">
                    <img src="${pkg.imagem_url}" class="card-img-top" alt="${pkg.nome}" style="height: 200px; object-fit: cover;">
                    ${pkg.duracao_dias ? `<div class="package-card-overlay">${pkg.duracao_dias} DIAS / ${pkg.duracao_noites} NOITES</div>` : ''}
                </div>
                <div class="package-card-content d-flex flex-column">
                    <div class="package-card-label">PACOTE</div>
                    <h3 class="package-card-title">${pkg.nome}</h3>
                    ${pkg.avaliacao ? `<div class="package-card-rating"><span class="badge">${pkg.avaliacao}</span><span class="stars"><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-half"></i></span></div>` : ''}
                    <div class="package-card-details">${pkg.cidade_origem ? `Saindo de ${pkg.cidade_origem}<br>` : ''}${inclusoText ? `${inclusoText}<br>` : ''}</div>
                    <div class="package-card-price-info mt-auto">
                        <div class="price-label">Preço por pessoa</div>
                        <div class="price-value">R$ ${pkg.preco}</div>
                        <div class="price-notes">${pkg.taxas_inclusas ? 'Taxas e impostos inclusos' : 'Taxas e impostos não inclusos'}</div>
                    </div>
                </div>
            </div>
            `;
            const link = document.createElement('a');
            link.href = `/pacotes/${pkg.id}/`;
            link.className = 'text-decoration-none';
            link.appendChild(card);
            packagesGrid.appendChild(link);
        });
    }

    fetchSearchResults();
});