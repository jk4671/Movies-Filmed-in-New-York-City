// homepage.js

$(document).ready(function() {
    // Function to generate HTML for movie cards
    function generateMovieCard(movie) {
        return `
        <div class="col-md-4 movie-container"> <!-- Add movie-container class -->
            <a href="/view/${movie.id}" class="card-link"> <!-- Add anchor tag -->
                <div class="card">
                    <img src="${movie.image}" class="card-img-top" alt="${movie.title} movie poster">
                    <div class="card-body">
                        <h5 class="card-title dark-gray">${movie.title}</h5>
                        <p class="card-text dark-gray">Year: ${movie.year}</p>
                    </div>
                </div>
            </a>
        </div>
        `;
    }

    // Function to populate popular movies on the homepage
    function populatePopularMovies(popularMovies) {
        // Get the container element where movie cards will be appended
        const container = $('#popularMoviesContainer');

        // Iterate over popularMovies and generate HTML for each movie card
        $.each(popularMovies, function(_, movie) {
            // Generate HTML for movie card
            const movieCardHTML = generateMovieCard(movie);
            // Append movie card HTML to the container
            container.append(movieCardHTML);
        });
    }

    // Call the function to populate popular movies
    populatePopularMovies(popular_movies);
});
