// make flashed messages disappear after 2 seconds
$(document).ready(function () {
    setTimeout(function () {
        $('.alert').fadeOut('slow');
    }, 3000); // <-- time in milliseconds
});

// clear element from screen
function remove(cls) {
    const elem = document.querySelector(cls);
    elem.parentNode.removeChild(elem);
    console.log('removed', cls);
}