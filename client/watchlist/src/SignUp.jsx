import React, {useState} from "react"


function SignUp() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    function handleSubmit(event) {
        event.preventDefault();
        // send post to api/sign-up/
        async function createAccount() {
            const payload = {username: username, password: password};
            try {
                const response = await fetch("http://127.0.0.1:8000/api/sign-up/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(payload),
                });
                const data = await response.json();
                console.log(data.success)
            } catch (error) {
                console.error("Error:", error);
            }
        }

        createAccount();
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>
                    Username: <input name="username" value={username} onChange={(event) => setUsername(event.target.value)}></input>
                </label>
                <label>
                    Password: <input name="password" value={password} onChange={(event) => setPassword(event.target.value)}></input>
                </label>
                <button type="submit">Create Account</button>
            </form>
        </div>
    )
}

export default SignUp
