let rating = $('#rating').html();

let veryLowRatingMax = 3;
let lowRatingsMax = 4.5;
let mediumRatingsMax = 6;
let mediumHighRatingsMax = 8;

if (rating < veryLowRatingMax) {
    $('#rating').css('color', '#ff4545');
} else if (rating < lowRatingsMax) {
    $('#rating').css('color', '#ffa534');
} else if (rating < mediumRatingsMax) {
    $('#rating').css('color', '#ffe234');
} else if (rating < mediumHighRatingsMax) {
    $('#rating').css('color', '#b7dd29');
} else if (rating <= 10 ) {
    $('#rating').css('color', '#57e32c');
}
