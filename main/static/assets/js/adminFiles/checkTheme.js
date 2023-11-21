window.onload = checkTheme(); // Run the checkTheme function when the page loads

/**
 * @Author - @DeanLogan
 * @Description - Checks the user's selected theme and applies it to the page's body element.
 * Removes non-default themes to ensure only one theme is applied at a time.
 */
function checkTheme() {
    var theme = localStorage.getItem('theme'); // Get the user's selected theme from local storage
    let element = document.body; // Get the body element of the page

    // Remove non-default themes to ensure only one theme is applied at a time
    element.classList.remove('light-mode');
    element.classList.remove('high-contrast-mode');

    // Check the selected theme and apply it to the page's body element
    if (theme == 'light-mode') {
        element.classList.add('light-mode'); // Apply the light mode theme
    } else if (theme == 'high-contrast-mode') {
        element.classList.add('high-contrast-mode'); // Apply the high contrast mode theme
    }
}