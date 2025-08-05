// frontend/js/config.js (VERSÃO CORRIGIDA E COMPLETA)

document.addEventListener('DOMContentLoaded', () => {
    async function loadSiteConfig() {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/configuracao/');
            if (!response.ok) return;

            const config = await response.json();
            // Salva a configuração globalmente para que outros scripts (como detalhe.js) possam acessá-la
            window.siteConfig = config;

            // Atualiza o logotipo
            const logoElement = document.getElementById('site-logo');
            if (logoElement && config.logotipo_url) {
                logoElement.src = config.logotipo_url;
            }
            
            // Lógica do botão WhatsApp
            const whatsappButton = document.getElementById('whatsapp-float-button');
            if (whatsappButton && config.whatsapp_numero) {
                const whatsappLink = `https://wa.me/${config.whatsapp_numero}`;
                whatsappButton.href = whatsappLink;
                whatsappButton.style.visibility = 'visible';
            }

        } catch (error) {
            console.error('Erro ao carregar as configurações do site:', error);
        }
    }

    loadSiteConfig();

    if (typeof updateSummary === 'function') {
        updateSummary();
    }
});