// // Event listener for auto close message function using DOM Content Loaded
document.addEventListener('DOMContentLoaded', alertTimeout);

// // Javascript function for auto close messages
function alertTimeout() {
    setTimeout(function () {
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 2500);
}