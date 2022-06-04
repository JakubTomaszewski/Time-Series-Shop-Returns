import "./App.css";
import React from "react";
import InputDateForm from "./components/InputDateForm/InputDateForm";

function App() {
  const predictionURL = "http://localhost:8020/api";

  const getPrediction = async (date) => {
    await fetch(predictionURL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(date),
    })
      .then((response) => response.json())
      .then((predictions) => console.log(predictions));
  };

  return (
    <div className="App">
      <h1 className="App-header">Predykcja liczby zwrotów</h1>
      {/* <h1>System predykcji liczby zwrotów</h1> */}
      <InputDateForm getPrediction={getPrediction} />
    </div>
  );
}

export default App;
