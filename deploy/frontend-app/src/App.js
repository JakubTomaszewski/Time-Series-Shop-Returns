import "./App.css";
import React from "react";
import { useState } from "react";

import InputDateForm from "./components/InputDateForm/InputDateForm";
import PredictionsPanel from "./components/PredictionsPanel/PredictionsPanel";

function App() {
  const linRegPredictionURL = "http://localhost:8020/api/regression";
  const randomForestPredictionURL = "http://localhost:8020/api/forest";

  const [linRegPredictions, setLinRegPredictions] = useState();
  const [randomForestpredictions, setRandomForestpredictions] = useState([]);

  const fetchPredictions = async (url, date, handleResponse) => {
    await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(date),
    })
      .then((response) => response.json())
      .then((predictionsResponse) => handleResponse(predictionsResponse));
  };

  const getPredictions = (date) => {
    fetchPredictions(
      randomForestPredictionURL,
      date,
      setRandomForestpredictions
    );
    fetchPredictions(linRegPredictionURL, date, setLinRegPredictions);
  };

  return (
    <div className="App">
      <h1 className="App-header">Predykcja liczby zwrotów</h1>
      <InputDateForm getPredictions={getPredictions} />
      {randomForestpredictions && linRegPredictions && (
        <PredictionsPanel
          firstModelTitle={"Predykcje dla LR"}
          firstPredictions={linRegPredictions}
          secondModelTitle={"Predykcje dla RF"}
          secondPredictions={randomForestpredictions}
        />
      )}
    </div>
  );
}

export default App;
