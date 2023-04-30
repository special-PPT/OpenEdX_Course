document.addEventListener('DOMContentLoaded', function() {
    // Get all the course description elements using the class name
    const descriptionElements = document.getElementsByClassName('course-description');

    // Loop through all the description elements and update each of them
    for (const descriptionElement of descriptionElements) {
        // Get the full description text
        const fullDescription = descriptionElement.textContent;

        // Extract the first sentence
        const firstSentence = fullDescription.match(/(.*?[.!?])(\s|$)/);

        // Update the paragraph element with the first sentence
        if (firstSentence && firstSentence.length > 0) {
            descriptionElement.textContent = firstSentence[0].trim();
        }
    }
});

