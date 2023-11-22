/**
 * @Author - @DeanLogan
 * @Description - Displays a message in the Journal interface with a specified sender.
 * Scrolls to the bottom of the journal content for viewing the new message.
 * @param {string} message - The message text to be displayed.
 */
function displayJournalEntry(entry, date) {
    if (entry.trim().length > 0) {
        // Append the message to the Journal interface with the specified sender
        $(".journals-container").append(`
        <div class="journal-table">
            <div class="top-of-table">
                <p><b class="heading">Date: </b><span> ${date}</span></p>
            </div>
            <div>
                <p><b class="heading">Entry: </b><span> ${entry}</span></p>
            </div>
        </div>
    `);
        
        const element = $('.content'); // Get the journal content element
        // Scroll to the bottom of the content for viewing the new message
        element.animate({
            scrollTop: element.prop("scrollHeight")
        }, 30); // Wait 30ms for response from the Journal
    }
}

/**
 * @Author - @DeanLogan
 * @Description - Executes when the journal page loads to initialize and display introductory messages.
 * Displays example instructions to the user.
 */
function journalPageLoad() {
    // Resize the Journal page to ensure proper UI layout
    resizeJournalPage();
}

/**
 * @Author - @DeanLogan
 * @Description - Sets up event listeners for the Journal page to handle user input and window resizing.
 */
function listenersForJournalPage() {
    // Listen for the Enter key press event on the user input field
    var input = document.getElementById("userInput");
    input.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            usersInput = input.value;
            var date = new Date().toLocaleDateString();
            displayJournalEntry(usersInput, date);
            input.value = "";
            event.preventDefault();
        }
    });

    // Listen for window resize event to adjust UI elements
    window.addEventListener('resize', function() {
        resizeJournalPage(); // Resize UI elements when the window is resized
    });
}

/**
 * @Author - @DeanLogan
 * @Description - Resizes UI elements of the Journal page based on window width and navigation status.
 * Adjusts widths and positions of the bottom bar, textarea, and content area.
 */
function resizeJournalPage() {
    const bottomBarDiv = document.querySelector('.bottom-bar'); // Get the bottom bar element
    const textarea = document.getElementById("userInput"); // Get the user input textarea element
    const windowWidth = window.innerWidth; // Get the current window width
    const navOpen = sessionStorage.getItem("navOpen") === "true"; // Check if navigation sidebar is open

    // Adjust content area height to fit the remaining space
    document.querySelector('.content').style.height = (window.innerHeight - 185) + "px";

    // Initialize variables for new dimensions
    let newBottomBarWidth, newBottomBarLeft, newTextareaWidth;

    // Check window width for responsive adjustments
    if (windowWidth < 1117.1) {
        newBottomBarWidth = windowWidth - (navOpen ? 145 : 32);
        newBottomBarLeft = navOpen ? 145 : 32;
        newTextareaWidth = windowWidth - (windowWidth * 0.0625) - newBottomBarLeft;
    } else {
        newBottomBarWidth = windowWidth - (windowWidth * (navOpen ? 0.13 : 0.0286));
        newBottomBarLeft = windowWidth * (navOpen ? 0.13 : 0.0286);
        newTextareaWidth = windowWidth - (windowWidth * (navOpen ? 0.1925 : 0.0911));
    }

    // Apply the new dimensions to UI elements
    bottomBarDiv.style.width = newBottomBarWidth + 'px';
    bottomBarDiv.style.left = newBottomBarLeft + 'px';
    textarea.style.width = newTextareaWidth + "px";
}

/**
 * @Author - @DeanLogan
 * @Description - Toggles the navigation sidebar and resizes UI elements on the Journal page.
 */
function navToggleOnJournalPage(){
    navToggle();
    resizeJournalPage();
}


// Execute journalPageLoad function when the window finishes loading
window.onload = journalPageLoad();

// Set up event listeners for the Journal page
listenersForJournalPage();