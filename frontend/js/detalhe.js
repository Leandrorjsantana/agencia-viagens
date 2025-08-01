// frontend/js/detalhe.js (VERSÃO CORRIGIDA E COMPLETA)

document.addEventListener('DOMContentLoaded', () => {
    const packageDetailContent = document.getElementById('package-detail-content');

    const urlParams = new URLSearchParams(window.location.search);
    const packageId = urlParams.get('id');

    if (!packageId) {
        packageDetailContent.innerHTML = '<p class="text-center text-danger">Erro: Pacote não especificado.</p>';
        return;
    }

    async function fetchPackageDetails() {
        try {
            const response = await fetch(`http://127.0.0.1:8000/api/pacotes/${packageId}/`);
            if (!response.ok) {
                throw new Error('Pacote não encontrado ou erro no servidor.');
            }
            const pkg = await response.json();
            displayPackageDetails(pkg);
        } catch (error) {
            packageDetailContent.innerHTML = `<p class="text-center text-danger">${error.message}</p>`;
        }
    }

    function displayPackageDetails(pkg) {
        document.title = pkg.nome;

        packageDetailContent.innerHTML = `
            <nav aria-label="breadcrumb">
                <ol class="breadcrumb">
                    <li class="breadcrumb-item"><a href="index.html">Início</a></li>
                    <li class="breadcrumb-item"><a href="#">Destinos</a></li>
                    <li class="breadcrumb-item active" aria-current="page">${pkg.destino}</li>
                </ol>
            </nav>

            <div class="row g-4">
                <div class="col-lg-8">
                    <h1 class="mb-3">${pkg.nome}</h1>
                    <img src="${pkg.imagem_url}" class="img-fluid rounded shadow-sm mb-4 w-100" alt="${pkg.nome}" style="max-height: 450px; object-fit: cover;">
                    
                    <div class="card">
                        <div class="card-header">
                            <h5>Descrição Completa</h5>
                        </div>
                        <div class="card-body">
                            <p class="lead">${pkg.descricao_curta}</p>
                            <hr>
                            <p>${pkg.descricao_longa.replace(/\\n/g, '<br>')}</p> </div>
                    </div>
                </div>

                <div class="col-lg-4">
                    <div class="card shadow-sm sticky-top" style="top: 20px;">
                        <div class="card-body">
                            <h3 class="text-primary my-3">R$ ${pkg.preco}</h3>
                            <p class="text-muted">por pessoa</p>
                            <hr>
                            <div class="d-flex align-items-center mb-2">
                                <i class="bi bi-calendar-check fs-4 me-2"></i>
                                <span><strong>Ida:</strong> ${pkg.data_ida}</span>
                            </div>
                            <div class="d-flex align-items-center mb-3">
                                <i class="bi bi-calendar-x fs-4 me-2"></i>
                                <span><strong>Volta:</strong> ${pkg.data_volta}</span>
                            </div>
                            <div class="d-grid">
                                <a href="#" class="btn btn-primary btn-lg">Reservar Agora</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }

    fetchPackageDetails();
});