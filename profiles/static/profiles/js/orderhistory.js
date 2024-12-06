$(document).ready(function() {
    $('#order-history-table').css('display', 'none');
    });

$('#order-history-button').on('click', function() {
    $(this).html($(this).text() == 'Hide Order History' ? 'View Order History': 'Hide Order History');
    $('#order-history-table').toggle();
});
   