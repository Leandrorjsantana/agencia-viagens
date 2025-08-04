// frontend/js/search-form.js

document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('search-form');

    searchForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const destination = document.getElementById('search-destination').value;

        // --- LINHA CORRIGIDA AQUI ---
        // Antes: search_results.html?destino=...
        // Agora: /busca/?destino=...
        const searchURL = `/busca/?destino=${encodeURIComponent(destination)}`;
        // ----------------------------

        window.location.href = searchURL;
    });
});