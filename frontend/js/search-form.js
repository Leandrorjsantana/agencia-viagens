// frontend/js/search-form.js

document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('search-form');

    searchForm.addEventListener('submit', (event) => {
        // Impede o envio padrão do formulário, que recarregaria a página
        event.preventDefault();

        // Pega o valor do campo de destino
        const destination = document.getElementById('search-destination').value;

        // Constrói a URL da página de resultados com o parâmetro de busca
        const searchURL = `search_results.html?destino=${encodeURIComponent(destination)}`;

        // Redireciona o usuário para a página de resultados
        window.location.href = searchURL;
    });
});