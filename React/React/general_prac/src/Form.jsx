import {useState} from 'react'
export default function Form()
{
    const [username,setUsername] = useState("");
    const [password,setPassword] = useState("");
    const [msg,setMsg] = useState("");
    const handleClick=(e)=>{
        e.preventDefault();
        if(username === "admin" && password === "123")
            setMsg("Login Successful");
        else
            setMsg("Invalid Username or Password");
    }

    return(
        <div>
            <form onSubmit={handleClick}>
                <h1>Login App</h1>
                <label>Username:</label>
                <input type="text" placeholder="Enter Username" value={username} onChange={(e)=>setUsername(e.target.value)}/><br></br>
                 <label>Password:</label>
                <input type="password" placeholder="Enter Password" value={password} onChange={(e)=>setPassword(e.target.value)}/><br></br>
                <button type="submit">Login</button>
            </form>
            <h2>{msg}</h2>
        </div>
    );
}