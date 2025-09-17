import React, {useState} from "react"

function SignIn() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    function handleSubmit(event) {
        event.preventDefault();
        const payload = {"username": username, "password": password};


        async function getTokens() {
            try {
                const response = await fetch("http://127.0.0.1:8000/api/get-tokens/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(payload),
                })
                const data = await response.json();
                sessionStorage.setItem("access_token", data.access);
                console.log("Access key:", sessionStorage.getItem("access_token"));
            } catch (error) {
                console.error("Error:", error);
            }
        }

        getTokens();
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>Username:
                    <input name="username" value={username} onChange={(event) => setUsername(event.target.value)}></input>
                </label>
                <label>Password:
                    <input name="password" value={password} onChange={(event) => setPassword(event.target.value)}></input>
                </label>
                <button type="submit" >Sign in</button>
            </form>
        </div>
    )
}


export default SignIn
