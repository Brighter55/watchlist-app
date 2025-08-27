import React, {useState} from "react"
import styles from "./Add.module.css"

function Add() {
    const [name, setName] = useState("");


    async function handleSubmit(event) {
        event.preventDefault();
        const payload = {
            name: name
        };

        // send data to Django endpoint
        try {
            const response = await fetch("http://127.0.0.1:8000/api/watchlist-add/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(payload),
            });
            const result = await response.json();
            console.log(result);
        }
        catch (error) {
            console.error("Something is wrong sending Django api", error)
        }
    }


    return (
        <div className={styles.addBody}>
            <div className={styles.formContent}>
            <form onSubmit={handleSubmit} className={styles.form}>


                <div className={styles.group}>
                    <input className={styles.input} name="name" value={name} onChange={(event) => setName(event.target.value)} placeholder="Enter your movie name" />
                    <span className={styles.highlight}></span>
                    <span className={styles.bar}></span>
                </div>

                <button className={styles.submitInput} type="submit" value="submit">
                    <svg height={24} width={24} fill="#FFFFFF" viewBox="0 0 24 24" data-name="Layer 1" id="Layer_1" className={styles.sparkle}>
                    <path d="M10,21.236,6.755,14.745.264,11.5,6.755,8.255,10,1.764l3.245,6.491L19.736,11.5l-6.491,3.245ZM18,21l1.5,3L21,21l3-1.5L21,18l-1.5-3L18,18l-3,1.5ZM19.333,4.667,20.5,7l1.167-2.333L24,3.5,21.667,2.333,20.5,0,19.333,2.333,17,3.5Z" />
                    </svg>
                    <span className={styles.textButton}>Generate</span>
                </button>
            </form>
            </div>
        </div>

    )
}

export default Add
