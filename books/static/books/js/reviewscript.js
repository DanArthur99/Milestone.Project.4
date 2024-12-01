rating = $('#rating').text()

ratings = document.getElementsByClassName('rating')

rating_texts = []

for (let rating of ratings) {
    rating_texts.push(rating.innerHTML)
}

veryLowRatingMax = 3
lowRatingsMax = 4.5
mediumRatingsMax = 6
mediumHighRatingsMax = 8

if (rating < veryLowRatingMax) {
    $('#rating').css('color', '#ff4545')
} else if (rating < lowRatingsMax) {
    $('#rating').css('color', '#ffa534')
} else if (rating < mediumRatingsMax) {
    $('#rating').css('color', '#ffe234')
} else if (rating < mediumHighRatingsMax) {
    $('#rating').css('color', '#b7dd29')
} else if (rating <= 10 ) {
    $('#rating').css('color', '#57e32c')
}

for (let rating of ratings) {
    if (rating < veryLowRatingMax) {
        $(rating).css('color', '#ff4545')
    } else if (rating < lowRatingsMax) {
        $(rating).css('color', '#ffa534')
    } else if (rating < mediumRatingsMax) {
        $(rating).css('color', '#ffe234')
    } else if (rating < mediumHighRatingsMax) {
        $(rating).css('color', '#b7dd29')
    } else if (rating <= 10 ) {
        $(rating).css('color', '#57e32c')
    }
}