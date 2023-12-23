document.addEventListener('DOMContentLoaded', alertTimeout);

function alertTimeout() {
    setTimeout(function () {
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 3000);
}