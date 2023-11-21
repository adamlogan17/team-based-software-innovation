/**
 * @Author - @DeanLogan
 * @Description - Executes when the chatbot page loads to initialize and display introductory messages.
 * Displays instructions and capabilities of the chatbot to help EEECS students.
 */
function chatbotPageLoad() {
    // Display introductory messages to the user
    displayText("This is sample text of what a social workers text would look like","botText");
    // Resize the chatbot page to ensure proper UI layout
    resizeChatbotPage();
}

/**
 * @Author - @DeanLogan
 * @Description - Sets up event listeners for the chatbot page to handle user input and window resizing.
 */
function listenersForChatbotPage() {
    // Listen for the Enter key press event on the user input field
    var input = document.getElementById("userInput");
    input.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            usersInput = input.value;
            processUserInput(usersInput); // Process the user's input
            input.value = "";
            event.preventDefault();
            displayText(usersInput, "userText"); // Display the user's input as a message
        }
    });

    // Listen for window resize event to adjust UI elements
    window.addEventListener('resize', function() {
        resizeChatbotPage(); // Resize UI elements when the window is resized
    });
}

/**
 * @Author - @DeanLogan
 * @Description - Resizes UI elements of the chatbot page based on window width and navigation status.
 * Adjusts widths and positions of the bottom bar, textarea, and content area.
 */
function resizeChatbotPage() {
    const bottomBarDiv = document.querySelector('.bottom-bar'); // Get the bottom bar element
    const textarea = document.getElementById("userInput"); // Get the user input textarea element
    const windowWidth = window.innerWidth; // Get the current window width
    const navOpen = sessionStorage.getItem("navOpen") === "true"; // Check if navigation sidebar is open

    // Adjust content area height to fit the remaining space
    document.querySelector('.content').style.height = (window.innerHeight - 85) + "px";

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
 * @Description - Toggles the navigation sidebar and resizes UI elements on the chatbot page.
 */
function navToggleOnChatbotPage(){
    navToggle();
    resizeChatbotPage();
}

/* START OF CHATBOT CODE */

/**
 * @Author - @DeanLogan
 * @Description - Displays a message in the chatbot interface with a specified sender.
 * Scrolls to the bottom of the chat content for viewing the new message.
 * @param {string} message - The message text to be displayed.
 * @param {string} sender - The sender of the message (either 'botText' or 'userText').
 */
function displayText(message, sender) {
    if (message.trim().length > 0) {
        // Append the message to the chatbot interface with the specified sender
        $(".chatbot").append('<div class=' + sender + '><p>' + message + '</p></div>');
        
        const element = $('.content'); // Get the chat content element
        // Scroll to the bottom of the chat content for viewing the new message
        element.animate({
            scrollTop: element.prop("scrollHeight")
        }, 30); // Wait 30ms for response from the chatbot
    }
}

/**
 * @Author - @KyleMcComb
 * @Description - Sends message to the chatbot, then passes the result of this message to the displatText functio
 * @param {string} inputMessage - a message in form of a string that will be sent to the chatbot
 */
function processUserInput(inputMessage) {
    // Make an AJAX request to your server to get the bot response
    $.get("/receive_message/", { message: inputMessage }, function (data) {
        displayText(data.message, "botText"); //display bot response 
    });
}


/* END OF CHATBOT CODE */

// Execute chatbotPageLoad function when the window finishes loading
window.onload = chatbotPageLoad();

// Set up event listeners for the chatbot page
listenersForChatbotPage();