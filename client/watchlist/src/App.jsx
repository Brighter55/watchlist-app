import Index from "./Index/Index.jsx"
import Watchlist from "./Watchlist.jsx"
import Watching from "./Watching.jsx"
import Watched from "./Watched.jsx"
import WatchlistManager from "./WatchlistManager.jsx"
import Add from "./Add/Add.jsx"
import SignUp from "./SignUp.jsx"
import SignIn from "./SignIn.jsx"
import { BrowserRouter, Routes, Route } from "react-router-dom"


function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Index></Index>} />
        <Route path="/sign-up" element={<SignUp></SignUp>} />
        <Route path="/sign-in" element={<SignIn></SignIn>} />
        <Route path="/WatchlistManager" element={<WatchlistManager></WatchlistManager>} />
        <Route path="/Watchlist" element={<Watchlist></Watchlist>} />
        <Route path="/Add" element={<Add></Add>} />
        <Route path="/Watching" element={<Watching></Watching>} />
        <Route path="/Watched" element={<Watched></Watched>} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
