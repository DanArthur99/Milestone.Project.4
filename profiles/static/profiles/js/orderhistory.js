$(document).ready(function() {
    $('#order-history-table').css('display', 'none');
    })

table = $('#order-history-table')

$('#order-history-button').on('click', function() {
    if (table.css)
    $(this).html($(this).text() == 'Hide Order History' ? 'View Order History': 'Hide Order History');
    $('#order-history-table').toggle()
})
   