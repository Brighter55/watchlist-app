import React, {useEffect, useState} from "react"


function Watching(props) {
    const [movies, setMovies] = useState([]);


    useEffect(() => {
        async function getMovies() {
            try {
                const response = await fetch("http://127.0.0.1:8000/api/watching/", {
                    method: "POST",
                    headers: {
                        "Authorization": `Bearer ${props.JWTToken}`,
                    },
                });
                const data = await response.json();
                setMovies(data.movies);
            } catch (error) {
                console.error("Error:", error)
            }
        }

        getMovies();
    }, []);

    function handleDrop(movie) { // movie is {title: ..., id: ..., from: "Watchlist" or "Watched", to: "Watching"}
        // remove from watchlist/watched database by sending a POST to Django
        // add to watching database
        async function deleteAddMovie() {
            try {
                const response = await fetch("http://127.0.0.1:8000/api/delete-add-movie/", {
                    method: "POST",
                    headers: {
                        "Authorization": `Bearer ${props.JWTToken}`,
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(movie),
                });
                const data = await response.json();
                console.log(data.success);
            } catch (error) {
                console.error("Error:", error);
            }
        }


        deleteAddMovie();
    }

    return (
        <div className="boxes"
            onDragOver={(event) => event.preventDefault()}
            onDrop={(event) => {
                const movie = JSON.parse(event.dataTransfer.getData("text/plain"));
                handleDrop({...movie, to: "Watching"});
            }}
        >
            <h1>Watching:</h1>
            {movies.map((movie) => <h3 key={movie.id}
                                       draggable
                                       onDragStart={(event) => {
                                                                    const payload = {...movie, from: "Watching"};
                                                                    event.dataTransfer.setData("text/plain", JSON.stringify(payload));
                                                               }}>{movie.title}</h3>)}
        </div>
    )
}

export default Watching
