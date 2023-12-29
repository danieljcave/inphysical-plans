/*jshint esversion: 6 */
// Event listener for auto close message function using DOM Content Loaded
// Javascript function for auto close messages
document.addEventListener("DOMContentLoaded", (alertTimeoutalertTimeout) => {
    setTimeout(function () {
      $("#msg").alert("close");
    }, 2500);
  });