$(document).ready(function () {
    // Function to render search results
    function renderSearchResults() {
        // Empty the container before populating it with new data
        $("#searchItems").empty();
        // Wrap the query in a span element with a class
        let highlightedQuery = '<span class="query-bold">' + query + '</span>';

        // Generate the search heading with the highlighted query
        let searchHeading = $('<h1 class="query-results">').html(search_results.length + ' Movie(s) Related to "' + highlightedQuery + '"');

        // Append the search heading and item count to the searchItems container
        $('#searchItems').append(searchHeading);

        // Check if search_results exist and is not empty
        if (search_results && search_results.length > 0) {
            // Create a new row for each 3 movie cards
            for (let i = 0; i < search_results.length; i += 3) {
                let row = $('<div class="row">');
                // Loop through each movie in search_results
                for (let j = i; j < i + 3 && j < search_results.length; j++) {
                    let movie = search_results[j];
                    // Create HTML elements for displaying movie details
                    let movieCard = $('<div class="col-md-4">');
                    let cardBody = $('<div class="card-body">');

                    // Create a new row for the title
                    let titleRow = $('<div class="row search-title-cstm">');
                    // Create a column for the title
                    let titleCol = $('<div class="col-md-12">');
                    // Create view link with class and hover effect
                    let viewLink = $('<a>').attr('href', '/view/' + movie.id).addClass('link-clickable').html(boldifyTerms(movie.title, query) + ' (' + boldifyTerms(movie.year, query) + ')');
                    // Add hover effect
                    viewLink.hover(
                        function () {
                            $(this).addClass('link-hovered');
                        },
                        function () {
                            $(this).removeClass('link-hovered');
                        }
                    );
                    // Append view link to title column
                    titleCol.append(viewLink);
                    // Append title column to title row
                    titleRow.append(titleCol);

                    // Create a new row for the image
                    let imageRow = $('<div class="row search-img-row">');
                    // Create a column for the image
                    let imageCol = $('<div class="col-md-12">');
                    // Create an anchor element to wrap the image and link to the movie details
                    let imageLink = $('<a>').attr('href', '/view/' + movie.id);
                    // Append the image to the anchor element
                    imageLink.append($('<img class="card-img-top">').attr({
                        'src': movie.image,
                        'alt': movie.title + ' movie poster' // Add alt attribute with the movie title concatenated with ' poster'
                    }));                    
                    // Append image link to image column
                    imageCol.append(imageLink);
                    // Append image column to image row
                    imageRow.append(imageCol);

                    // Create a new row for directors, stars, and locations
                    let infoRow = $('<div class="row">');
                    // Create a column for directors, stars, and locations
                    let infoCol = $('<div class="col-md-12">');
                    // Boldify and join the directors, stars, and locations
                    let directors = $('<span>').addClass('light-gray').html(boldifyAndJoinTerms(movie.directors, query));
                    let directorsParagraph = $('<p>').html('<span class="dark-gray bold">Directors:</span> ').append(directors);
                    let stars = $('<span>').addClass('light-gray').html(boldifyAndJoinTerms(movie.stars, query));
                    let starsParagraph = $('<p>').html('<span class="dark-gray bold">Actors:</span> ').append(stars);
                    let locations = $('<span>').addClass('light-gray').html(boldifyAndJoinTerms(movie.locations, query));
                    let locationsParagraph = $('<p>').html('<span class="dark-gray bold">Locations:</span> ').append(locations);
                    // Append directors, stars, and locations paragraphs to info column
                    infoCol.append(directorsParagraph, starsParagraph, locationsParagraph);
                    // Append info column to info row
                    infoRow.append(infoCol);

                    // Append title row, image row, and info row to card body
                    cardBody.append(titleRow, imageRow, infoRow);
                    // Append card body to movie card
                    movieCard.append(cardBody);
                    // Append movie card to the current row
                    row.append(movieCard);
                }
                // Append the row to the searchItems container
                $('#searchItems').append(row);
            }
        } else {
            // If no results found, display a message
            $('#searchItems').append('<p>No results found.</p>');
        }
    }

    function boldifyTerms(text, query) {
        // Escape special characters in the query string
        const escapedQuery = query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&').replace(/&amp;/g, "&").replace(/&#39;/g, "'").replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&#34;/g, '"');
        // Create a regular expression to match the query string globally and case-insensitively
        const regex = new RegExp(escapedQuery, 'gi');
        // Replace all occurrences of the query string with a bold version
        return text.replace(regex, '<span class="highlight">$&</span>');
    }

    // Function to boldify and join terms
    function boldifyAndJoinTerms(terms, query) {
        // Boldify each term individually
        let boldifiedTerms = terms.map(term => boldifyTerms(term, query));
        // Join the boldified terms with ' | ' delimiter
        return boldifiedTerms.join(' | ');
    }

    // Render search results initially
    renderSearchResults();
});
