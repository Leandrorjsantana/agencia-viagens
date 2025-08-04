// frontend/js/main.js

document.addEventListener('DOMContentLoaded', () => {
    const destinosGrid = document.getElementById('destinos-grid');

    async function fetchDestinos() {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/destinos/');
            if (!response.ok) {
                throw new Error('Não foi possível carregar os destinos.');
            }
            const data = await response.json();
            displayDestinos(data.destinos);
        } catch (error) {
            destinosGrid.innerHTML = `<p class="text-danger text-center">${error.message}</p>`;
        }
    }

    function displayDestinos(destinos) {
        destinosGrid.innerHTML = '';
        if (destinos.length === 0) {
            destinosGrid.innerHTML = '<p class="text-center">Nenhum destino disponível no momento.</p>';
            return;
        }
        destinos.forEach(destino => {
            const card = document.createElement('div');
            card.className = 'col';
            card.innerHTML = `
                <a href="/destinos/${destino.id}/" class="card-link">
                    <div class="card h-100 shadow-sm text-white">
                        <img src="${destino.imagem_url}" class="card-img" alt="${destino.nome}" style="height: 250px; object-fit: cover;">
                        <div class="card-img-overlay d-flex flex-column justify-content-end p-4" style="background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);">
                            <h3 class="card-title">${destino.nome}</h3>
                            <p class="card-text small">${destino.descricao ? destino.descricao.substring(0, 100) + '...' : ''}</p>
                        </div>
                    </div>
                </a>
            `;
            destinosGrid.appendChild(card);
        });
    }

    fetchDestinos();
});