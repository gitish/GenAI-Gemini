import React, { useState } from "react";
import axios from "axios";
import Background from './img/genAI.jpg';

function App() {
    const [message, setMessage] = useState("");
    const [chats, setChats] = useState([]);

    const sendMessage = async () => {
        if (!message.trim()) return;

        const userMessage = { role: "user", content: message };
        setChats([...chats, userMessage]);

        try {
            const botMessage = { role: "assistant", content: "......." };
            setChats([...chats, userMessage, botMessage]);
            const response = await axios.post("http://127.0.0.1:5000/chat", { message });
            botMessage = { role: "assistant", content: response.data.response };
            setChats([...chats, userMessage, botMessage]);
        } catch (error) {
            console.error("Error sending message:", error);
        }

        setMessage("");
    };

    return (
        <div style={{maxWidth: "600px", margin: "auto", padding: "20px" }}>
            <div style={
                { backgroundImage: `url(${Background})`, 
                  backgroundRepeat: 'no-repeat', 
                  backgroundPosition: 'center center', 
                  backgroundSize: 'cover',
                  maxWidth: "600px", 
                  margin: "auto", 
                  padding: "50px" }
                }>
                <h1 style={{color:"white"}}>ChatBOT</h1>
            </div>
            
            <div style={{ height: "400px", overflowY: "auto", border: "1px solid #ccc", padding: "10px" }}>
                {chats.map((chat, index) => (
                    <p key={index} style={{ textAlign: chat.role === "user" ? "right" : "left" }}>
                        <strong>{chat.role === "user" ? "You" : "AI"}:</strong> {chat.content}
                    </p>
                ))}
            </div>
           
            <textarea
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Type your message..."
                style={{ width: "85%", padding: "10px", marginTop: "10px", height: "100px" }}
            />
            <button onClick={sendMessage} style={
                { padding: "5px", 
                  marginLeft: "10px", 
                  height: "100px", 
                  top: "-50px", 
                  position: "relative" 
                }}>Send</button>
        </div>
    );
}

export default App;
