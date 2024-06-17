$(document).ready(function() {
    $('.form-inline').submit(function(event) {
        let query = $('#search-input').val().trim(); // Get the query value and remove leading/trailing whitespace
        if (query === '') {
            // Clear whitespace from the search bar
            $('#search-input').val("");
            // Keep focus on the search bar
            $('#search-input').focus();
            event.preventDefault(); // Prevent form submission if query is whitespace
        }
    });
});
