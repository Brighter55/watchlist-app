import styles from "./Index.module.css"
import {useEffect, useState} from "react"
import { useNavigate } from "react-router-dom"

function Index() {
    const navigate = useNavigate();
    const [users, setUsers] = useState([]);

    useEffect(() => {
        async function getUsers() {
            try {
                const response = await fetch("http://127.0.0.1:8000/api/get-users/", {method: "POST"});
                const data = await response.json();
                setUsers(data.users);
            } catch (error) {
                console.error("Error:", error);
            }
        }

        getUsers();
    }, []);

    function handleClicked(user_id) {
        event.preventDefault();
        sessionStorage.setItem("owner", user_id);
        navigate("/WatchlistManager");
    }

    return (
        <div>
            <h1 style={{textAlign: "center"}}>All users</h1>
            <div className={styles.body}>
                {users.map(user => <div key={user.id} onClick={() => handleClicked(user.id)} className={styles.card}><h1>{user.username}</h1></div>)}
            </div>
        </div>
    )
}

export default Index
