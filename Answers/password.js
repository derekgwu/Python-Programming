function validatePassword() {
    var enteredPassword = document.getElementById('password').value;

    // Example: Check if the password meets certain criteria (e.g., minimum length)
    if (enteredPassword.length >= 8) {
      alert('Password is valid!');
    } else {
      alert('Password must be at least 8 characters long.');
    }
}

function unmask(str){

}
