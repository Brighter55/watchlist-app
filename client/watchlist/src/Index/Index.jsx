import styles from "./Index.module.css"

function Index() {
    const users = ["User 0", "User 1", "User 2", "User 3", "User 4", "User 5"];

    return (
        <div>
            <h1 style={{textAlign: "center"}}>All users</h1>
            <div className={styles.body}>
                {users.map(user => <div className={styles.card}><h1>{user}</h1></div>)}
            </div>
        </div>
    )
}

export default Index
