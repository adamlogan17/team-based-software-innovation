/**
 * @Author Adam Logan
 * @Description - Executes when the page loads to ensure set up of event listeners.
 */
function loginPageLoad() {
    loginListeners(); // Add event listeners to the page
}

/**
 * @Author Adam Logan
 * @Description - Holds event listeners that are applied to the login page.
 */
function loginListeners() {
    document.addEventListener("keypress", function(event) {
        if (event.key == "Enter" && (event.target.id == "username" || event.target.id == "password")) {
            login();
        }
    });

    document.getElementById("authForm").addEventListener("submit", function(event) {
        document.getElementById('code').disabled=true;
        event.preventDefault();
        login();
    });
}

/**
 * @Author Adam Logan
 * @Description - Gathers the entered login information and sends a POST request to verify the credentials.
 * If successful, the user is logged in; if not, an alert is displayed.
 */
function login() {
    // Send a POST request to verify login credentials
    $.post('/verify/', {
        username: document.getElementById('username').value,
        password: document.getElementById('password').value,
        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
    }, function (data) {
        if (data.loggedIn == 'true') {
            // If login is successful, display a success alert and reload the page
            alert('Login success');
            window.location.href = '/';
        } else {
            // If login fails, display an alert
            alert(data.errors);
            location.reload();
        }
    });
}

// Run the pageLoad function when the window is fully loaded
window.onload = loginPageLoad();