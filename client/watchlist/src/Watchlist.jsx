import add from "./assets/add.png"
import React, {useState} from "react"
import { useNavigate } from "react-router-dom"


function Watchlist() {
    const navigate = useNavigate()
    const [name, setName] = useState("")

    function handleAddClicked(event) {
        navigate("/Add");
    }

    return (
        <div className="boxes">
            <div className="watchlist-header">
                <h1>Watchlist:</h1>
                <img onClick={handleAddClicked} src={add} style={{width: "20px", height: "20px"}}/>
            </div>
            <h3 style={{marginTop: 0}}>Movie 1</h3>
            <h3>Movie 2</h3>
            <h3>Movie 3</h3>
        </div>
    )
}

export default Watchlist
