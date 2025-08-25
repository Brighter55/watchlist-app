import Watchlist from "./Watchlist.jsx"
import Watching from "./Watching.jsx"
import Watched from "./Watched.jsx"
import Index from "./Index.jsx"
import Add from "./Add.jsx"
import { BrowserRouter, Routes, Route } from "react-router-dom"



// give a page dedicated to a form
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Index></Index>} />
        <Route path="/Watchlist" element={<Watchlist></Watchlist>} />
        <Route path="/Add" element={<Add></Add>} />
        <Route path="/Watching" element={<Watching></Watching>} />
        <Route path="/Watched" element= {<Watched></Watched>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App
