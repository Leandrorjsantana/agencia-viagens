// backend/static/js/admin_reserva.js

window.addEventListener("load", function() {
    (function($) {
        $(document).ready(function() {
            // Monitora a mudança no campo de seleção de usuário
            $('#id_usuario').on('change', function() {
                var userId = $(this).val();
                if (userId) {
                    // Faz uma chamada para nossa API para buscar os dados
                    $.ajax({
                        url: '/api/get-user-details/',
                        data: { 'user_id': userId },
                        success: function(data) {
                            // Preenche os campos com os dados recebidos
                            $('#id_nome_cliente').val(data.nome);
                            $('#id_email_cliente').val(data.email);
                            $('#id_telefone_cliente').val(data.telefone);
                        }
                    });
                } else {
                    // Limpa os campos se nenhum usuário for selecionado
                    $('#id_nome_cliente').val('');
                    $('#id_email_cliente').val('');
                    $('#id_telefone_cliente').val('');
                }
            });
        });
    })(django.jQuery);
});