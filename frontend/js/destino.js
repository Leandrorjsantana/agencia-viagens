document.addEventListener('DOMContentLoaded', () => {

    const packagesGrid = document.getElementById('packages-grid');
    const destinoNome = document.getElementById('destino-nome');

    const urlParams = new URLSearchParams(window.location.search);
    const destinoId = urlParams.get('id');

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
            packagesGrid.innerHTML = `<p class="text-danger text-center">${error.message}</p>`;
        }
    }

    function displayPackages(data) {
        destinoNome.textContent = `Pacotes para ${data.destino.nome}`;
        document.title = `Pacotes para ${data.destino.nome}`;
        packagesGrid.innerHTML = '';

        if (data.pacotes.length === 0) {
            packagesGrid.innerHTML = '<p class="text-center">Nenhum pacote disponível para este destino no momento.</p>';
            return;
        }

        data.pacotes.forEach(pkg => {
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

    fetchPackagesByDestino();
});