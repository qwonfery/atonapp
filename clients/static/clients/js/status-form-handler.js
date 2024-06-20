$(document).ready(function(){
    $('.status-form').on('change', function(event){
        event.preventDefault();
        const form = $(this);
        const url = form[0].dataset.clientId + '/status/';
        $.ajax({
            type: 'POST',
            url: url,
            data: form.serialize(),
            success: function(response){
                if (response.status === 'success') {
                    alert('Статус успешно обновлен');
                } else {
                    alert('Ошибка при обновлении статуса');
                }
            },
            error: function(){
                alert('Ошибка при отправке запроса');
            }
        });
    });
});