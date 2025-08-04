// frontend/js/config.js (VERSÃO CORRIGIDA E COMPLETA)

document.addEventListener('DOMContentLoaded', () => {
    async function loadSiteConfig() {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/configuracao/');
            if (!response.ok) return;

            const config = await response.json();

            // Atualiza o logotipo
            const logoElement = document.getElementById('site-logo');
            if (logoElement && config.logotipo_url) {
                logoElement.src = config.logotipo_url;
            }

            // Atualiza o televendas (agora feito pelo template do Django)
            
            // --- LÓGICA DO BOTÃO WHATSAPP ADICIONADA ---
            const whatsappButton = document.getElementById('whatsapp-float-button');
            if (whatsappButton && config.whatsapp_numero) {
                const whatsappLink = `https://wa.me/${config.whatsapp_numero}`;
                whatsappButton.href = whatsappLink;
                whatsappButton.style.visibility = 'visible'; // Torna o botão visível
            }
            // ---------------------------------------------

        } catch (error) {
            console.error('Erro ao carregar as configurações do site:', error);
        }
    }

    loadSiteConfig();

    if (typeof updateSummary === 'function') {
        updateSummary();
    }
});