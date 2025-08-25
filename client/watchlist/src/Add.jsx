import React, {useState} from "react"


function Add() {
    const [name, setName] = useState("");


    function handleSubmit(event) {
        event.preventDefault();

        const payload = {
            "name": name
        }
    }


    return (
        <form onSubmit={handleSubmit}>
            <input name="name" value={name} onChange={(event) => setName(event.target.value)} />
            <input type="submit" value="submit"/>
        </form>
    )
}

export default Add
