from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import random

app = Flask(__name__)


current_id = 10
data = {
 "1": {
 "id": "1",
 "title": "Spider-Man",
 "image": "https://m.media-amazon.com/images/M/MV5BZDEyN2NhMjgtMjdhNi00MmNlLWE5YTgtZGE4MzNjMTRlMGEwXkEyXkFqcGdeQXVyNDUyOTg3Njg@._V1_FMjpg_UX1000_.jpg",
 "year": "2002",
 "summary": "Peter Parker is a shy teenager who visits a genetics laboratory at Columbia University with his friend Harry Osborn. When Peter is bitten by a genetically engineered spider created by Harry’s father Norman Osborn, he gains spider-like superpower. He uses his newly gained superpower to fight crime and injustice. During the process, he comes across Green Goblin, a super-villain, and loses many of his loves ones.",
 "directors": ["Sam Raimi"],
 "stars": ["Tobey Maguire", "Willem Dafoe", "Kirsten Dunst", "James Franco", "Cliff Robertson", "Rosemary Harris"],
 "budget": "139,000,000",
 "running_time_min": "121",
 "countries": ["United States"],
 "locations": ["Times Square", "Columbia University", "Queensboro Bridge","Brooklyn Bridge", "Flatiron Building", "Empire State Building", "Tudor City Place", "New York Public Library"]
},
 "2": {
 "id": "2",
 "title": "King Kong",
 "image": "https://m.media-amazon.com/images/M/MV5BMjYxYmRlZWYtMzAwNC00MDA1LWJjNTItOTBjMzlhNGMzYzk3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_FMjpg_UX1000_.jpg",
 "year": "2005",
 "summary": "Filmmaker Carl Denham casts performer Ann Darrow to be in a movie written by Jack Driscoll with actor Bruce Baxter. The filming takes place on the SS Venture which is supposed to head to Singapore under Captain Englehorn. During the voyage, Ann and Jack fall in love, while the ship ends up on a mysterious island called Skulled Island. On the island, while the film crew explores the island, they are attacked by natives who offer Ann as a sacrifice to a 25-foot-tall ape named Kong. The story unfolds as Ann and Kong build an amicable relationship while the rest of the crew tries to rescue Ann from Kong.",
 "directors": ["Peter Jackson"],
 "stars": ["Naomi Watts", "Jack Black", "Adrien Brody", "Thomas Kretschmann", "Colin Hanks", "Jamie Bell", "Andy Serkis"],
 "budget": "207,000,000",
 "running_time_min": "188",
 "countries": ["United States", "New Zealand"],
 "locations": ["Times Square","Empire State Building", "Gapstow Bridge", "Washington Street and Water Street (Brooklyn)"]
},
 "3": {
 "id": "3",
 "title": "Spider-Man: Homecoming",
 "image": "https://m.media-amazon.com/images/M/MV5BODY2MTAzOTQ4M15BMl5BanBnXkFtZTgwNzg5MTE0MjI@._V1_FMjpg_UX1000_.jpg",
 "year": "2017",
 "summary": "The story takes place after the Battle of New York in 2012. Tony Stark, Iron Man, recruits Spider-Man, Peter Parker, to join the Avengers to mitigate an internal drama in Germany, but Peter returns to school when Tony tells him that he is not ready to become a full-time Avenger. To prove Tony wrong, Peter neglects his studies and spends more time fighting injustice as Spider-Man, which leads to his best friend Ned discovering his identity. This angers Tony who confiscates Peter’s Spider-Man suit. Despite this, Peter continues to fight injustice, and the story unfolds as Tony returns the Spider-Man suit to Peter.",
 "directors": ["Jon Watts"],
 "stars": ["Tom Holland", "Michael Keaton", "Jon Favreau", "Gwyneth Paltrow", "Zendaya", "Donald Glover", "Jacob Batalon", "Laura Harrier", "Tony Revolori", "Bokeem Woodbine", "Tyne Daly", "Marisa Tomei", "Robert Downey Jr."],
 "budget": "175,000,000",
 "running_time_min": "133",
 "countries": ["United States"],
 "locations": ["The Franklin K. Lane High School", "31st Street and 23rd Avenue in Astoria", "St George Terminal", "Luna Park"]
},
 "4": {
 "id": "4",
 "title": "Home Alone 2: Lost in New York",
 "image": "https://m.media-amazon.com/images/M/MV5BNDI1MzM0Y2YtYmIyMS00ODE3LTlhZjEtZTUyNmEzMTNhZWU5XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
 "year": "1992",
 "summary": "The McCallister family plans to spend Christmas in Miami, Florida. Kevin McCallister, the youngest brother, does not like this plan. On the day of the trip, the McCallister family oversleeps and rushes to the airport, where Kevin becomes separated and ends up on a flight to New York City while carrying his dad Peter's bag. In New York City, Kevin uses Peter's credit card to check in at the Plaza Hotel, where the Wet Bandits eventually kidnap him. In Miami, the McCallister family discovers that Kevin is missing and files a police report.  The story unfolds as Kevin attempts to escape the Wet Bandits.",
 "directors": ["Chris Columbus"],
 "stars": ["Macaulay Culkin", "Joe Pesci", "Daniel Stern", "John Heard", "Tim Curry", "Brenda Fricker" , "Catherine O'Hara"],
 "budget": "28,000,000",
 "running_time_min": "120",
 "countries": ["United States"],
 "locations": ["LaGuardia Airport", "Queensboro Bridge", "Radio City Music Hall", "Battery Park", "World Trade Center", "Subway (6th Avenue)", "Central Park South and Center Drive", "The Plaza", "Wollman Rink", "Bethesda Terrace", "Carnegie Hall", "Times Square", "Rockefeller Center"]
},
 "5": {
 "id": "5",
 "title": "West Side Story",
 "image": "https://m.media-amazon.com/images/M/MV5BMTM0NDAxOTI5MF5BMl5BanBnXkFtZTcwNjI4Mjg3NA@@._V1_.jpg",
 "year": "1961",
 "summary": "The story takes place in 1957 in New York City, where two teenage gangs named the Jets, a group of whites, and the Sharks, a group of Puerto Ricans, compete over the Upper West Side. Riff leads the Jets, and Bernardo leads the Sharks. While law enforcement comes and breaks them up, the Jets call the Sharks to a rumble after an upcoming dance. At the dance, Riff’s co-founder Tony falls in love with Bernardo's already-engaged younger sister Maria. Bernardo disapproves of the relationship between Bernardo and Maria. After the dance, Maria tells Tony to break up the rumble, but Tony ends up killing Bernardo. The story unfolds as Bernardo’s death causes a series of cascading events to occur between the two gangs.",
 "directors": ["Robert Wise", "Jerome Robbins"],
 "stars": ["Natalie Wood", "Richard Beymer", "Russ Tamblyn", "Rita Moreno", "George Chakiris"],
 "budget": "6,750,000",
 "running_time_min": "152",
 "countries": ["United States"],
 "locations": ["Playground (110th Street)", "110th Street (Between 2nd and 3rd Avenues)"]
},
 "6": {
 "id": "6",
 "title": "American Psycho",
 "image": "https://m.media-amazon.com/images/M/MV5BZTM2ZGJmNjQtN2UyOS00NjcxLWFjMDktMDE2NzMyNTZlZTBiXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_FMjpg_UX1000_.jpg",
 "year": "2000",
 "summary": "Patrick Bateman is a young, successful, wealthy investment banker who has a hard time keeping up with the socialites in New York City. One day, after being enraged by his colleague Paul Allen’s superiority, Bateman kills a homeless man and his dog at night in an alley. After having had one experience, he later kills Allen with an axe and leaves a message on his answering machine that he has gone to London. With no remorse, he continues to kill more people. The story unfolds as Bateman experiences a decline in morality.",
 "directors": ["Mary Harron"],
 "stars": ["Christian Bale", "Willem Dafoe", "Jared Leto", "Josh Lucas", "Samantha Mathis", "Matt Ross", "Bill Sage", "Chloë Sevigny", "Cara Seymour", "Justin Theroux", "Guinevere Turner", "Reese Witherspoon"],
 "budget": "7,000,000",
 "running_time_min": "101",
 "countries": ["United States", "Canada"],
 "locations": ["New York Yacht Club"]
},
 "7": {
 "id": "7",
 "title": "Begin Again",
 "image": "https://m.media-amazon.com/images/M/MV5BNjAxMTI4MTgzMV5BMl5BanBnXkFtZTgwOTAwODEwMjE@._V1_.jpg",
 "year": "2013",
 "summary": "Dan Mulligan is a formally successful record label executive who lives in New York City. His lifestyle has declined as he now struggles to keep up with the changing music industry. One day, after being fired, he goes to a bar on the Lower East Side, where he meets Gretta James, a young independent songwriter from England. Dan offers to sign Gretta to his former record label. The story unfolds by telling the story of a new musical partnership between Gretta and Dan.",
 "directors": ["John Carney"],
 "stars": ["Keira Knightley", "Mark Ruffalo", "Hailee Steinfeld", "Adam Levine", "James Corden", "Yasiin Bey", "CeeLo Green", "Catherine Keener"],
 "budget": "8,000,000",
 "running_time_min": "104",
 "countries": ["United States"],
 "locations": ["Vazac's Horseshoe Bar", "Subway (Delaney Street and Norfolk Street)", "Gitane Café", "Times Square", "Washington Square Park", "Boating Lake", "Bethesda Terrace", "Suffolk Street"]
},
 "8": {
 "id": "8",
 "title": "The Devil Wears Prada",
 "image": "https://m.media-amazon.com/images/M/MV5BZjQ3ZTIzOTItMGNjNC00MWRmLWJlMGEtMjJmMDM5ZDIzZGM3XkEyXkFqcGdeQXVyMTkzODUwNzk@._V1_.jpg",
 "year": "2006",
 "summary": "Andrea Sachs is a new-graduate from Northwestern University who is hired as a junior personal assistant to Miranda Priestly, the editor-in-chief of Runway magazine. With no experience working in the fashion industry, Andy puts up with the demands from Miranda in hopes of using her experience working at Runway to start a career in journalism. Initially, Andrea is belittled by her coworkers, but Andrea makes attempts to improve, making Miranda notice Andrea’s effort. The story follows Andrea’s journey as Miranda’s assistant in the fashion industry.",
 "directors": ["David Frankel"],
 "stars": ["Meryl Streep", "Anne Hathaway", "Stanley Tucci", "Simon Baker", "Emily Blunt", "Adrian Grenier"],
 "budget": "35,000,000",
 "running_time_min": "109",
 "countries": ["United States"],
 "locations": ["Subway (Spring Street)", "Subway (Lexington Avenue and East 51st Street)","1221 Avenue of the Americas", "Bubby's", "Times Square", "Craf", "56 Crosby Street", "Smith and Wollensky", "The St. Regis New York", "American Museum of Natural History", "Lenox Hill Hospital"]
},
 "9": {
 "id": "9",
 "title": "Enchanted",
 "image": "https://m.media-amazon.com/images/M/MV5BMjE4NDQ2Mjc0OF5BMl5BanBnXkFtZTcwNzQ2NDE1MQ@@._V1_FMjpg_UX1000_.jpg",
 "year": "2007",
 "summary": "Enchanted is a fantasy-musical film that follows Giselle, an archetypal Disney princess, as she is thrown into New York City. Giselle lives happily in Andalasia, waiting for her designated true love, Prince Edward. Prince Edward's evil stepmother, Queen Narissa, fears that she will lose her position on the throne once Prince Edward marries the love of his life. So, Queen Narissa disguises herself as an old hag and sends Giselle to 'where there are no happily ever afters:' New York City. Edwards follows Giselle to New York City. The story unfolds as Giselle navigates through her independence outside of a fairytale life.",
 "directors": ["Kevin Lima"],
 "stars": ["Amy Adams", "Patrick Dempsey", "James Marsden", "Timothy Spall", "Idina Menzel", "Susan Sarandon"],
 "budget": "85,000,000",
 "running_time_min": "107",
 "countries": ["United States"],
 "locations": ["Brooklyn Bridge", "Bethesda Fountain", "Columbus Circle Subway", "Times Square", "Time Warner Center", "Elie Tahari Store", "Merchant's Gate Fountain", "Gapstow Bridge", "Boating Lake", "Reservoir Bridge", "Sheep Meadow", "Bow Bridge"]
},
 "10": {
 "id": "10",
 "title": "When Harry Met Sally",
 "image": "https://m.media-amazon.com/images/M/MV5BMjE0ODEwNjM2NF5BMl5BanBnXkFtZTcwMjU2Mzg3NA@@._V1_.jpg",
 "year": "1989",
 "summary": "In 1977, Harry Burns and Sally Albrights both graduated from the University of Chicago. At the time, Harry dates Sally’s friend Amanda Reese, which makes Sally and Harry ride-share to New York City, where Sally will attend journalism school and Harry will start a new job. On their journey to New York, Harry tells Sally that she is very attractive, which makes Sally mad as she thinks he is making a pass. They arrive in New York and never see each other until five years later, when they find each other on the same flight. The story unfolds as Harry and Sally meet each other again throughout time and develop feelings for each other.",
 "directors": ["Rob Reiner"],
 "stars": ["Billy Crystal", "Meg Ryan", "Carrie Fisher", "Bruno Kirby"],
 "budget": "16,000,000",
 "running_time_min": "96",
 "countries": ["United States"],
 "locations": ["Washington Square Park Arch", "Loeb Boathouse", "Café Luxembourg","Metropolitan Museum of Art", "Katz's Delicatessen", "Bethesda Terrace & Fountain", "PlantShed"]
},
}

# ROUTES

@app.route('/')
def homepage():
    # Fetch three random movies from the data dictionary
    popular_movie_ids = random.sample(range(1, len(data) + 1), 3)
    popular_movies = {str(movie_id): data[str(movie_id)] for movie_id in popular_movie_ids}

    return render_template('homepage.html', popular_movies=popular_movies)


@app.route('/add')
def add():
    return render_template('add.html', data=data)


@app.route('/view/<id>')
def view(id=None):
    global data
    movie = data.get(id)  # Use .get() method to avoid KeyError if id is not found
    if movie:
        return render_template('movie_page.html', movie=movie)
    else:
        # Handle the case when movie with given id is not found
        return "Movie not found", 404


@app.route('/edit/<id>')
def edit(id=None):
    global data
    movie = data.get(id) 
    if movie:
        print(movie)
        return render_template('edit.html', movie=movie)
    else:
        # Handle the case when movie with given id is not found
        return "Movie not found", 404
    

@app.route('/search')
def search():
    query = request.args.get('query')  # Get search query from URL parameters
    # Search in multiple fields: title, locations, stars, directors, and year
    search_results = [movie for movie in data.values() if
                      query.lower() in movie['title'].lower() or
                      any(query.lower() in location.lower() for location in movie['locations']) or
                      any(query.lower() in star.lower() for star in movie['stars']) or
                      any(query.lower() in director.lower() for director in movie['directors']) or
                      query.lower() in movie['year']]
    
    return render_template('search.html', query=query, search_results=search_results)


# AJAX FUNCTIONS

# ajax for add.js
@app.route('/add_content', methods=['POST'])
def add_content():
    global data
    global current_id

    json_data = request.get_json()   
    title = json_data["title"]
    image = json_data["image"]
    year = json_data["year"]
    summary = json_data["summary"]
    directors = json_data["directors"]
    stars = json_data["stars"]
    budget = json_data["budget"]
    running_time_min = json_data["running_time_min"]
    countries = json_data["countries"]
    locations = json_data["locations"]

    # Assign a unique id to the new content
    current_id += 1
    content_id = str(current_id)
    new_content_entry = {
        "id": current_id,
        "title": title,
        "image": image,
        "year": year,
        "summary": summary,
        "directors": directors,
        "stars": stars,
        "budget": budget,
        "running_time_min": running_time_min,
        "countries": countries,
        "locations": locations
    }

    data[content_id] = new_content_entry
    
    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(data = data)
 
# ajax for edit.js
@app.route('/edit_content/<int:id>', methods=['PUT'])
def edit_content(id=None):
    global data

    json_data = request.get_json() 
    title = json_data["title"]
    image = json_data["image"]
    year = json_data["year"]
    summary = json_data["summary"]
    directors = json_data["directors"]
    stars = json_data["stars"]
    budget = json_data["budget"]
    running_time_min = json_data["running_time_min"]
    countries = json_data["countries"]
    locations = json_data["locations"]

    new_content_entry = {
        "id": id,
        "title": title,
        "image": image,
        "year": year,
        "summary": summary,
        "directors": directors,
        "stars": stars,
        "budget": budget,
        "running_time_min": running_time_min,
        "countries": countries,
        "locations": locations
    }

    id = str(id)
    data[id].update(new_content_entry)
    movie = data.get(id) 
    # Respond with the updated resource
    return jsonify(movie)


if __name__ == '__main__':
   app.run(debug = True)




