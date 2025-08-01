// frontend/js/config.js (VERSÃO CORRIGIDA)

document.addEventListener('DOMContentLoaded', () => {
    async function loadSiteConfig() {
        try {
            // O ERRO ESTAVA AQUI: Eu digitei 127.001 em vez de 127.0.0.1
            const response = await fetch('http://127.0.0.1:8000/api/configuracao/');
            
            if (!response.ok) return; // Se falhar, não faz nada

            const config = await response.json();

            // Atualiza o logotipo
            const logoElement = document.getElementById('site-logo');
            if (logoElement && config.logotipo_url) {
                logoElement.src = config.logotipo_url;
            }

            // Atualiza o televendas
            const televendasElement = document.getElementById('televendas-link');
            if (televendasElement && config.telefone_televendas) {
                televendasElement.innerHTML = `<i class="bi bi-telephone-fill me-2"></i>Televendas ${config.telefone_televendas}`;
            }

        } catch (error) {
            console.error('Erro ao carregar as configurações do site:', error);
        }
    }

    loadSiteConfig();

    // Se a função updateSummary existir na página (como no index.html), chame-a
    if (typeof updateSummary === 'function') {
        updateSummary();
    }
});