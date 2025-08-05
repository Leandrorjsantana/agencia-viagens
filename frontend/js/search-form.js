// frontend/js/search-form.js

document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('search-form');

    if (searchForm) {
        searchForm.addEventListener('submit', (event) => {
            event.preventDefault();
            const destination = document.getElementById('search-destination').value;
            const dataIda = document.getElementById('search-ida').value;
            const dataVolta = document.getElementById('search-volta').value;

            const params = new URLSearchParams();
            if (destination) {
                params.append('destino', destination);
            }
            if (dataIda) {
                params.append('data_ida', dataIda);
            }
            if (dataVolta) {
                params.append('data_volta', dataVolta);
            }
            
            const searchURL = `/busca/?${params.toString()}`;
            window.location.href = searchURL;
        });
    }

    // --- LÓGICA DO MENU ÂNCORA COM ROLAGEM SUAVE ---
    const navTabs = document.querySelectorAll('#myTab .nav-link');

    navTabs.forEach(tab => {
        tab.addEventListener('click', function(event) {
            // Pega o ID da seção do atributo data-scroll-to
            const targetId = this.getAttribute('data-scroll-to');
            if (!targetId) return; // Se não houver o atributo, não faz nada

            const targetSection = document.querySelector(targetId);

            if (targetSection) {
                // Calcula a posição da seção e desconta a altura do cabeçalho para não ficar escondido atrás dele
                const headerOffset = 100; // Altura aproximada do seu header em pixels. Ajuste se necessário.
                const elementPosition = targetSection.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                // Rola a página suavemente até a posição calculada
                window.scrollTo({
                    top: offsetPosition,
                    behavior: "smooth"
                });
            }
        });
    });
    // ----------------------------------------------------
});