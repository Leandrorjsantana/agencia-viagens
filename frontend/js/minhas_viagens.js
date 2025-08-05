document.addEventListener('DOMContentLoaded', () => {
    const listaReservasDiv = document.getElementById('lista-reservas');

    async function fetchReservas() {
        try {
            const response = await fetch('/api/minhas-reservas/');
            if (!response.ok) throw new Error('Não foi possível carregar suas reservas.');
            const data = await response.json();
            displayReservas(data.reservas);
        } catch (error) {
            listaReservasDiv.innerHTML = `<p class="text-danger text-center">${error.message}</p>`;
        }
    }

    function displayReservas(reservas) {
        if (reservas.length === 0) {
            listaReservasDiv.innerHTML = '<p class="text-center">Você ainda não fez nenhuma solicitação de reserva.</p>';
            return;
        }
        let html = '<ul class="list-group">';
        reservas.forEach(reserva => {
            let statusClass = 'bg-secondary';
            if (reserva.status === 'Confirmada') statusClass = 'bg-success';
            if (reserva.status === 'Cancelada') statusClass = 'bg-danger';

            html += `
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    <div>
                        <strong>${reserva.pacote_nome}</strong><br>
                        <small class="text-muted">Solicitada em: ${reserva.data_solicitacao}</small>
                    </div>
                    <span class="badge ${statusClass} rounded-pill">${reserva.status}</span>
                </li>
            `;
        });
        html += '</ul>';
        listaReservasDiv.innerHTML = html;
    }

    fetchReservas();
});