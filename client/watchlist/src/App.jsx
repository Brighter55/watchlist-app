import Watchlist from "./Watchlist.jsx"
import Watching from "./Watching.jsx"
import Watched from "./Watched.jsx"
import Index from "./Index.jsx"
import Add from "./Add/Add.jsx"
import { BrowserRouter, Routes, Route } from "react-router-dom"
import React, { useEffect, useState} from "react"


function App() {
  const [JWTToken, setJWTToken] = useState(null);
  // make an async function for this fetch and call it
  // useEffect to fetch the JWT token
  useEffect(() => {
    async function get_JWT_token() {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/", {
          method: "POST",
        });
        const data = await response.json();
        setJWTToken(data.token);
      } catch (error) {
        console.error("Error:", error)
      }
    }
    get_JWT_token();
  }, []);


  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Index></Index>} />
        <Route path="/Watchlist" element={<Watchlist></Watchlist>} />
        <Route path="/Add" element={<Add JWTToken={JWTToken}></Add>} />
        <Route path="/Watching" element={<Watching></Watching>} />
        <Route path="/Watched" element={<Watched></Watched>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App
