import React, { useState, useEffect } from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
    const [totalReactPackages, setTotalReactPackages] = useState(String);

    useEffect(() => {
        // GET request using fetch inside useEffect React hook
        fetch("http://127.0.0.1:5000/")
            .then((response) => response.text())
            .then((data) => setTotalReactPackages(data));

        // empty dependency array means this effect will only run once (like componentDidMount in classes)
    }, []);

    setInterval(
        () => {
            fetch("http://127.0.0.1:5000/")
                .then((response) => response.text())
                .then((data) => setTotalReactPackages(data));
        },
        // Delay in milliseconds or null to stop it
        2000
    );
    return (
        <div className="card text-center m-3">
            <h5 className="card-header">GET Request with React Hooks</h5>
            <div className="card-body">
                Total react packages: {totalReactPackages}
            </div>
        </div>
    );
    return <div className="App">tmp</div>;
}

export default App;
