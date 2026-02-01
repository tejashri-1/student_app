function validateForm() {
    // Get input values
    let name = document.forms["studentForm"]["name"].value.trim();
    let email = document.forms["studentForm"]["email"].value.trim();

    // Name validation
    if (name === "") {
        alert("Name must be filled out!");
        return false; // stops form submission
    }

    // Email validation using regex
    let emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (!emailPattern.test(email)) {
        alert("Please enter a valid email address!");
        return false; // stops form submission
    }

    return true; // everything is fine, allow form submission
}
