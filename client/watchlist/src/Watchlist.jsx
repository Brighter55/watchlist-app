import add from "./assets/add.png"
import React, {useState, useEffect} from "react"
import { useNavigate } from "react-router-dom"


function Watchlist() {
    const navigate = useNavigate();
    const [movies, setMovies] = useState([]);

    function handleAddClicked(event) {
        navigate("/Add");
    }


    useEffect(() => {
        async function getMovies() { // needs to send access key
            try {
                const response = await fetch("http://127.0.0.1:8000/api/watchlist/", {
                    method: "POST",
                    headers: {"Authorization": `Bearer ${sessionStorage.getItem("access_token")}`},
                });
                const data = await response.json();
                setMovies(data.movies);
            } catch (error) {
                console.error("Error:", error);
            }
        }

        getMovies();
    }, []); // TODO: needs to be refreshed when another movie is added

    function handleDrop(movie) {
        async function deleteAddMovie() {
            try {
                const response = await fetch("http://127.0.0.1:8000/api/delete-add-movie/", {
                    method: "POST",
                    headers: {
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


    // display titles from database
    return (
        <div className="boxes"
            onDragOver={(event) => event.preventDefault()}
            onDrop={(event) => {
                const movie = JSON.parse(event.dataTransfer.getData("text/plain"));
                handleDrop({...movie, to: "Watchlist"});
            }}
        >
            <div className="watchlist-header">
                <h1>Watchlist:</h1>
                <img onClick={handleAddClicked} src={add} style={{width: "20px", height: "20px"}}/>
            </div>
            {movies.map((movie) => <h3 key={movie.id}
                                        draggable
                                        onDragStart={(event) => {
                                                                    const payload = {...movie, from: "Watchlist"};
                                                                    event.dataTransfer.setData("text/plain", JSON.stringify(payload));
                                                                }}>{movie.title}</h3>)}
        </div>
    )
}

export default Watchlist
