import React, { useEffect, useState } from "react"
import Watchlist from "./Watchlist.jsx"
import Watching from "./Watching.jsx"
import Watched from "./Watched.jsx"

function Index() {
    const [csrftoken, setCSRFtoken] = useState(null);

    useEffect(() => {
        async function get_CSRF_token() {
            try {
                const response = await fetch("http://127.0.0.1:8000/api/");
                const data = await response.json();
                console.log(`${data["success"]} and the csrftoken is ${data["csrftoken"]}`);
                setCSRFtoken(data["csrftoken"]);
            } catch (error) {
                console.error("Error at fetching:", error)
            }
        }
        get_CSRF_token();
    }, []);

    return (
        <div className="content">
            <div className="boxes-container">
                <Watchlist></Watchlist>
                <Watching></Watching>
                <Watched></Watched>
            </div>
        </div>
  )
}


export default Index

