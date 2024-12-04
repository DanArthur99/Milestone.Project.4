$(document).ready(function() {
    $('#order-history-table').css('display', 'none');
    })

table = $('#order-history-table')

$('#order-history-button').on('click', function() {
    if (table.css)
    $(this).html($(this).text() == 'Hide Order History' ? 'Show Order History': 'Hide Order Historu')
    $('#order-history-table').toggle()
})
   