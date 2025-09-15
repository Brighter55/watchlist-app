import Watchlist from "./Watchlist.jsx"
import Watching from "./Watching.jsx"
import Watched from "./Watched.jsx"

function WatchlistManager() {
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


export default WatchlistManager

