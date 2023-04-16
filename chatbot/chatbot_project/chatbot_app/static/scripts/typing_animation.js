
function showTypingIndicator() {
        // Create the main container div
    const typingContainer = document.createElement('div');
    typingContainer.classList.add('messages__item--typing');

    // Create the three span elements with the 'messages__dot' class
    for (let i = 0; i < 3; i++) {
      const dot = document.createElement('span');
      dot.classList.add('messages__dot');
      typingContainer.appendChild(dot);
    }

    // Append the typingContainer to the desired parent element

    $("#chatbox").append(typingContainer);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);
}

function hideTypingIndicator() {
    const typingContainer = document.querySelector('.messages__item--typing');
    typingContainer.remove();

}