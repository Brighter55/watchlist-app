import React, {useState, useEffect} from "react"

function Watched() {
    // fetch movies in api_watched
    const [movies, setMovies] = useState([]);

    useEffect(() => {
        async function getMovies() {
            if (sessionStorage.getItem("access_token")) {
                try {
                    const response = await fetch("http://127.0.0.1:8000/api/watched/", {
                        method: "POST",
                        headers: {"Authorization": `Bearer ${sessionStorage.getItem("access_token")}`},
                    });
                    const data = await response.json();
                    setMovies(data.movies);
                } catch (error) {
                    console.error("Error:", error)
                }
            } else {
                try {
                    const response = await fetch("http://127.0.0.1:8000/api/watched/", {
                        method: "POST",
                        headers: {"Content-Type": "application/json"},
                        body: JSON.stringify({owner: sessionStorage.getItem("owner")}),
                    });
                    const data = await response.json();
                    setMovies(data.movies);
                } catch (error) {
                    console.error("Error:", error)
                }
            }
        }

        getMovies();
    }, []);

    function handleDrop(movie) {
        async function deleteAddMovie() {
            try {
                const response = await fetch("http://127.0.0.1:8000/api/delete-add-movie/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${sessionStorage.getItem("access_token")}`,
                    },
                    body: JSON.stringify(movie),
                });
                const data = await response.json();
                console.log(data.success);
                window.location.reload();
            } catch (error) {
                console.error("Error:", error);
            }
        }

        deleteAddMovie();
    }

    return (
       <div className="boxes"
            onDragOver={(event) => {event.preventDefault();}}
            onDrop={(event) => {
                const movie = JSON.parse(event.dataTransfer.getData("text/plain"));
                handleDrop({...movie, to: "Watched"});
            }}
       >
            <h1>Watched:</h1>
            {movies.map((movie) => <h3 key={movie.id}
                                       draggable
                                       onDragStart={(event) => {
                                                                    const payload = {...movie, from: "Watched"};
                                                                    event.dataTransfer.setData("text/plain", JSON.stringify(payload));
                                                                }}>{movie.title}</h3>)}
        </div>
    )
}

export default Watched
