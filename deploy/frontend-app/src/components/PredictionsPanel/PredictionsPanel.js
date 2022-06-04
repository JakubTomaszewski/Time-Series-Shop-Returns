import React from "react";
import Grid from "@mui/material/Grid";

const PredictionsPanel = ({
  firstModelTitle,
  firstPredictions,
  secondModelTitle,
  secondPredictions,
}) => {
  return (
    <Grid container>
      <Grid item xs={6}>
        <h1>{firstModelTitle}</h1>
        {Object.keys(firstPredictions).map((date) => (
          <Grid container spacing={2}>
            <Grid item xs={6}>
              Data: {date}
            </Grid>
            <Grid item xs={6}>
              Liczba zwrotów: {firstPredictions[date]}
            </Grid>
          </Grid>
        ))}
      </Grid>
      <Grid item xs={6}>
        <h1>{secondModelTitle}</h1>
        {Object.keys(secondPredictions).map((date) => (
          <Grid container spacing={2}>
            <Grid item xs={6}>
              Data: {date}
            </Grid>
            <Grid item xs={6}>
              Liczba zwrotów: {secondPredictions[date]}
            </Grid>
          </Grid>
        ))}
      </Grid>
    </Grid>
  );
};

export default PredictionsPanel;
