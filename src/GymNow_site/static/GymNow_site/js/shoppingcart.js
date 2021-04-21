var updateBtns = document.getElementsByClassName('update-cart')


for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var bookingId = this.dataset.booking
        var action = this.dataset.action
        console.log('bookingId:', bookingId, 'action:', action)

        console.log('USER:', user)

        if (user == 'AnonymousUser') {
            console.log('User is not logged in')

        } else {
            updateUserBooking(bookingId, action)
        }
    })
}


function updateUserBooking(bookingId, action) {
    console.log('User is logged in, sending data...')

    var url = '/UpdateBooking/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'bookingId': bookingId, 'action': action })
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log('data:', data)
            location.reload()
        });
}