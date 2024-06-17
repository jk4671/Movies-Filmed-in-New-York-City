function addContent() {
    event.preventDefault();

    // Remove old success messages
    $("#success-message-container").empty();

    let title = $("#title").val();
    let image = $("#image").val();
    let year = $("#year").val();
    let summary = $("#summary").val();
    let budget = $("#budget").val();
    let runningTime = $("#running_time_min").val();

    // Split directors string using a regular expression to handle single director followed by comma
    let directors = $("#directors").val().split(/\s*,\s*(?=\S)/).map(director => director.trim());

    // Split stars string using a regular expression to handle single star followed by comma
    let stars = $("#stars").val().split(/\s*,\s*(?=\S)/).map(star => star.trim());

    // Split countries string using a regular expression to handle single country followed by comma
    let countries = $("#countries").val().split(/\s*,\s*(?=\S)/).map(country => country.trim());

    // Split locations string using a regular expression to handle single location followed by comma
    let locations = $("#locations").val().split(/\s*,\s*(?=\S)/).map(location => location.trim());


    $(".error-message").remove();
    $(".error-indicator").remove();

    let errors = [];

    if (title === "" || /^\s*$/.test(title)) {
        errors.push({ field: "title", message: "Title is required" });
    }

    if (year === "" || /^\s*$/.test(year) || !isValidYear(year)) {
        if (year === "" || /^\s*$/.test(year) ) {
            errors.push({ field: "year", message: "Year is required" });
        } else {
            errors.push({ field: "year", message: "Please enter a valid year" });
        }
    }

    if (image === "" || /^\s*$/.test(image)) {
        errors.push({ field: "image", message: "Image is required" });
    } else {
        if (!isValidUrl(image)) {
            errors.push({ field: "image", message: "Please enter a valid URL for the image" });
        }
    }

    if (locations === "" || /^\s*$/.test(locations)) {
        errors.push({ field: "locations", message: "Locations are required. Please enter locations separated by commas" });
    }



    if (summary === "" || /^\s*$/.test(summary)) {
        errors.push({ field: "summary", message: "Summary is required" });
    }


    if (directors === "" || /^\s*$/.test(directors)) {
        errors.push({ field: "directors", message: "Directors are required. Please enter directors separated by commas" });
    }

    if (stars === "" || /^\s*$/.test(stars)) {
        errors.push({ field: "stars", message: "Stars are required. Please enter stars separated by commas" });
    }

    if (runningTime === "" || /^\s*$/.test(runningTime)) {
        errors.push({ field: "running_time_min", message: "Running Time is required" });
    } else {
        // Check if runningTime is numeric
        if (isNaN(parseFloat(runningTime))) {
            errors.push({ field: "running_time_min", message: "Running Time must be a numerical value" });
        }
    }

    if (countries === "" || /^\s*$/.test(countries)) {
        errors.push({ field: "countries", message: "Countries are required. Please enter countries separated by commas" });
    }


    // Validate budget
    if (budget === "" || /^\s*$/.test(budget)) {
        errors.push({ field: "budget", message: "Budget is required" });
    } else {
        if (!isValidBudget(budget)) {
            errors.push({ field: "budget", message: "Please enter a valid numerical value representing money" });
        }
    }

    if (errors.length > 0) {
        errors.forEach(function(error) {
            let { field, message } = error;
            $("#" + field).after(`<div class='error-message text-danger' id='${field}-error'>${message}</div>`);
            $(`label[for='${field}']`).append("<span class='text-danger error-indicator'> *</span>"); // Add error indicator
        });
        
        // Focus on the first input field with an error
        let firstErrorField = errors[0].field;
        $("#" + firstErrorField).focus();
        
        // Prevent data submission
        return false;
    }

    // Clear error indicators when there are no errors
    $("label .error-indicator").remove();

    let dataToSave = {
        "title": title,
        "image": image,
        "year": year,
        "summary": summary,
        "budget": budget,
        "running_time_min": runningTime,
        "directors": directors,
        "stars": stars,
        "countries": countries,
        "locations": locations
    }

    saveContent(dataToSave);
    return true;
}




function saveContent(dataToSave){

    $.ajax({
        type: "POST",
        url: "add_content",                
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(dataToSave),
        success: function(result) {
            let allData = result["data"];
            data = allData;
        
            // Get the ID of the newly added item
            let newItemId = Object.keys(data).pop();
        
            // Construct the link for viewing the newly added item
            let newItemLink = "/view/" + newItemId;
        
            // Show success message with link to view the item
            let newItemMessage = "<h3 class='fake-black'>New item successfully created.</h3>";
            let newItemLinkHtml = "<div><a href='" + newItemLink + "' class='link-clickable'>See it here</a></div>";
    

            // Append the success message and link to the container
            $("#success-message-container").append("<div class='success-message row'><div class='col-md-12'>" + newItemMessage + newItemLinkHtml + "</div></div>");
        
            // Clear input fields after submission
            $("#title").val("");
            $("#image").val("");
            $("#year").val("");
            $("#summary").val("");
            $("#budget").val("");
            $("#running_time_min").val("");
            $("#directors").val("");
            $("#stars").val("");
            $("#countries").val("");
            $("#locations").val("");
        
            // Focus on the title input box
            $("#title").focus();
        },
        
        
        error: function(request, status, error){
            console.log("Error");
            console.log(request);
            console.log(status);
            console.log(error);
        }
    });
}



// Function to validate URL
function isValidUrl(string) {
    try {
        new URL(string);
        return true;
    } catch (_) {
        return false;  
    }
}

function isValidBudget(budget) {
    return /^\$?\d{1,3}(,\d{3})*(\.\d{2})?$/.test(budget);
}

// Function to validate year
function isValidYear(year) {
    return /^\d{4}$/.test(year) && parseInt(year) >= 1800 && parseInt(year) <= new Date().getFullYear();
}

$(document).ready(function(){
    $("#submit-button").click(addContent);
    $("#budget").keypress(function(event){     
        if(event.which == 13) {
            event.preventDefault();
            addContent();
        }   
    });

})
