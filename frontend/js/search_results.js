// frontend/js/search_results.js

document.addEventListener('DOMContentLoaded', () => {
    const packagesGrid = document.getElementById('packages-grid');
    const searchTitle = document.getElementById('search-title');

    const urlParams = new URLSearchParams(window.location.search);
    const destinoQuery = urlParams.get('destino');

    if (!destinoQuery) {
        searchTitle.textContent = 'Nenhum termo de busca fornecido.';
        return;
    }

    searchTitle.textContent = `Exibindo resultados para "${destinoQuery}"`;

    async function fetchSearchResults() {
        try {
            // Constrói a URL da API de busca com o parâmetro
            const response = await fetch(`http://127.0.0.1:8000/api/search/?destino=${encodeURIComponent(destinoQuery)}`);
            if (!response.ok) {
                throw new Error('Não foi possível realizar a busca.');
            }
            const data = await response.json();
            displayPackages(data.pacotes);
        } catch (error) {
            packagesGrid.innerHTML = `<p class="text-danger text-center">${error.message}</p>`;
        }
    }

    function displayPackages(packages) {
        packagesGrid.innerHTML = '';
        if (packages.length === 0) {
            packagesGrid.innerHTML = `<p class="text-center col-12">Nenhum pacote encontrado para "${destinoQuery}".</p>`;
            return;
        }
        packages.forEach(pkg => {
            const card = document.createElement('div');
            card.className = 'col';
            card.innerHTML = `
                <div class="card h-100 shadow-sm">
                    <img src="${pkg.imagem_url}" class="card-img-top" alt="${pkg.nome}" style="height: 200px; object-fit: cover;">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">${pkg.nome}</h5>
                        <div class="mt-auto">
                            <p class="card-price">R$ ${pkg.preco}</p>
                            <a href="pacote_detalhe.html?id=${pkg.id}" class="btn btn-primary w-100">Ver Detalhes</a>
                        </div>
                    </div>
                </div>
            `;
            packagesGrid.appendChild(card);
        });
    }

    fetchSearchResults();
});