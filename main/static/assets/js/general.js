var pathwayData = ''; // global variable that will hold information on each of the pathways which is taken from the database

/**
 * @Author - @DeanLogan
 * @Description - Executes when the page loads to ensure proper initialization and sizing of UI elements.
 * Handles navigation, theme, font size, sign-up data, and sets up event listeners.
 */
function pageLoad() {
    // Ensure the navigation sidebar is closed whenever the page loads and adjust UI elements
    sessionStorage.setItem('navOpen', 'true');
    navToggle();
    resizeContentDiv();

    // Set up event listeners
    listeners();
}


/**
 * @Author - @DeanLogan
 * @Description - Toggles the side bar (nav) open or closed, and updates its state in session storage.
 * Adjusts UI elements by calling resizeNav and resizeContentDiv functions.
 */
function navToggle() {
    var navOpen = sessionStorage.getItem('navOpen'); // Get the current state of the navigation sidebar from session storage

    // Close the navigation sidebar if it's currently open
    if (navOpen == 'true') {
        sessionStorage.setItem('navOpen', 'false'); // Update the navigation state to closed
    }
    // Open the navigation sidebar if it's currently closed
    else if (navOpen == 'false') {
        sessionStorage.setItem('navOpen', 'true'); // Update the navigation state to open
    }

    // Resize the navigation and content elements based on the updated navigation state
    resizeNav(sessionStorage.getItem('navOpen')); // Resize the navigation sidebar
    resizeContentDiv(); // Resize the content div
}


/**
 * @Author - @DeanLogan
 * @Description - Resizes the navigation sidebar based on its state (open or closed) and window width.
 * Adjusts the width and height of the sidebar and resizes the close button accordingly.
 * @param {string} navOpen - The state of the navigation sidebar ('true' for open, 'false' for closed).
 */
function resizeNav(navOpen) {
    var windowWidth = window.innerWidth; // Get the current window width

    // Close the navigation sidebar
    if (navOpen == 'false') {
        // Check if the window width is smaller than 1117.1px
        if (windowWidth < 1117.1) {
            document.getElementsByClassName('sidebar')[0].style.width = '32px'; // Set small width for closed sidebar
        } else {
            document.getElementsByClassName('sidebar')[0].style.width = '2.864vw'; // Set responsive width for closed sidebar
        }
    }
    // Open the navigation sidebar
    else if (navOpen == "true") {
        // Check if the window width is smaller than 1117.1px
        if (windowWidth < 1117.1) {
            document.getElementsByClassName('sidebar')[0].style.width = '145.22px'; // Set width for open sidebar
        } else {
            document.getElementsByClassName('sidebar')[0].style.width = '13vw'; // Set responsive width for open sidebar
        }
    }
    
    resiveClosebtn(); // Resize the close button (burger icon)
    document.getElementsByClassName('sidebar')[0].style.height = '100vh'; // Set sidebar height to cover the entire viewport
}


/**
 * @Author - @DeanLogan
 * @Description - Resizes the close button (often called "burger" icon) based on window width.
 * Adjusts the font size of the close button for responsive design.
 */
function resiveClosebtn() {
    var windowWidth = window.innerWidth; // Get the current window width
    var closebtn = document.getElementsByClassName('closebtn')[0]; // Get the close button element

    // Check the window width and adjust the font size of the close button
    if (windowWidth < 1117.1) {
        closebtn.style.fontSize = '20.1076px'; // Set font size for small screens
    } else {
        closebtn.style.fontSize = '1.8vw'; // Set responsive font size for larger screens
    }
}

/**
 * @Author - @DeanLogan
 * @Description - Resizes the content div based on the state of the navigation sidebar (open or closed) and window width.
 * Adjusts the width and position of the content div to fit the layout.
 */
function resizeContentDiv() {
    var contentDiv = document.getElementsByClassName('content')[0]; // Get the content div element
    var windowWidth = window.innerWidth; // Get the current window width

    var navOpen = sessionStorage.getItem('navOpen'); // Get the state of the navigation sidebar

    // NAV IS OPEN
    if (navOpen == 'true') {
        // Check if the window width is smaller than 1117.1px
        if (windowWidth < 1117.1) {
            contentDiv.style.width = (windowWidth - 145) + 'px'; // Set the width for open sidebar on small screens
            contentDiv.style.left = '145px'; // Set the left position
        } else {
            contentDiv.style.width = windowWidth - (windowWidth * 0.13) + 'px'; // Set responsive width for open sidebar
            contentDiv.style.left = windowWidth * 0.13 + 'px'; // Set responsive left position
        }
    }
    // NAV IS NOT OPEN
    else if (navOpen == 'false') {
        // Check if the window width is smaller than 1117.1px
        if (windowWidth < 1117.1) {
            contentDiv.style.width = (windowWidth - 32) + 'px'; // Set the width for closed sidebar on small screens
            contentDiv.style.left = '32px'; // Set the left position
        } else {
            contentDiv.style.width = windowWidth - (windowWidth * 0.0286) + 'px'; // Set responsive width for closed sidebar
            contentDiv.style.left = windowWidth * 0.0286 + 'px'; // Set responsive left position
        }
    }
}


/**
 * @Author - @DeanLogan
 * @Description - Holds event listeners that are applied to every web page.
 */
function listeners() {
    // When the window is resized, adjust UI elements
    window.addEventListener('resize', function() { resizeContentDiv(); }); // Resize content div
    window.addEventListener('resize', function() { resizeNav(sessionStorage.getItem('navOpen')); }); // Resize navigation sidebar
    
    // Menu animation code
    const menu = document.getElementById('menu');
    Array.from(document.getElementsByClassName('menu-item')).forEach((item, index) => {
        // When hovering over a menu item, set the active index for CSS animation
        item.onmouseover = () => {
            menu.dataset.activeIndex = index;
        }
    });
}

// Run the pageLoad function when the window is fully loaded
window.onload = pageLoad();