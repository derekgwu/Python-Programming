function checkPassword() {
  var passwordInput = document.getElementById("password").value;
  var messageElement = document.getElementById("message");

  // Example: Check if the password meets certain criteria
  if (passwordInput.localeCompare("dchen36")) {
      messageElement.textContent = "Incorrect Password. Please Try Again";
  } else {
    var button_div = document.getElementById("button_div");
    button_div.style.display = "flex";
    button_div = document.getElementById("entry");
    button_div.style.display = "none";
  }
}

function redirectToPage(url) {
  // Use window.location.href to redirect to the specified URL
  window.location.href = url;
}