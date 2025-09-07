import Watchlist from "./Watchlist.jsx"
import Watching from "./Watching.jsx"
import Watched from "./Watched.jsx"

function Index(props) {
    return (
        <div className="content">
            <div className="boxes-container">
                <Watchlist JWTToken={props.JWTToken}></Watchlist>
                <Watching JWTToken={props.JWTToken}></Watching>
                <Watched></Watched>
            </div>
        </div>
  )
}


export default Index

