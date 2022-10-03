import React, { useState, useEffect } from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
    const [totalReactPackages, setTotalReactPackages] = useState(String);

    setInterval(
        () => {
            fetch("http://127.0.0.1:5000/")
                .then((response) => response.text())
                .then((data) => setTotalReactPackages(data));
        },
        // Delay in milliseconds or null to stop it
        5000
    );
    return (
        <div className="card text-center m-3">
            <h5 className="card-header">Current updated value</h5>
            <div className="card-body">{totalReactPackages}</div>
        </div>
    );
    return <div className="App">tmp</div>;
}

export default App;
