Movies = [
    {
        "Action":{
            "Dunkirk" : {
                "Actors": ["Tom Hardy", "Mark Rylance"],
                "Director": ["Christoper Nolan"]
            },
            "Mission Impossible: Fallout": {
                "Actors": ["Tom Cruise", "Rebecca Ferguson"],
                "Director": ["Christopher McQuarrie"]
            }            
        }
    },
    { 
        "Drama": {
             "First Man" : {
                "Actors": ["Ryan Gosling", "Claire Foy"],
                "Director":["Damien Chazelle"]
            }
    }
    },
    {
        "Thriller": {
            "A Quiet Place" : {
                "Actors" : ["John Krazinski", "Emily Blunt"],
                "Director": ["John Krazinksi"]
            }
        }
    }
]

print(Movies[1].get("Drama", "Genre Not Found").get("First Man", "Movie Not Found",).get("Actors", "Actor Not Found")[0])