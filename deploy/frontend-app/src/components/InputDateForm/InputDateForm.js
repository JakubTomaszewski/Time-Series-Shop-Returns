import React from "react";
import isWeekend from "date-fns/isWeekend";
import TextField from "@mui/material/TextField";
import { AdapterDateFns } from "@mui/x-date-pickers/AdapterDateFns";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { StaticDatePicker } from "@mui/x-date-pickers/StaticDatePicker";
import { useState } from "react";

const InputDateForm = ({ getPrediction }) => {
  const [date, setDate] = useState(new Date());

  function handleSubmit() {
    const predictionDate = {
      day: date.getDate(),
      month: date.getMonth() + 1,
      year: date.getFullYear(),
    };

    console.log(predictionDate);

    getPrediction(predictionDate);
  }

  return (
    <div className="date-form">
      <LocalizationProvider dateAdapter={AdapterDateFns}>
        <StaticDatePicker
          orientation="landscape"
          openTo="day"
          value={date}
          onChange={(date) => {
            setDate(date);
          }}
          renderInput={(params) => <TextField {...params} />}
          onAccept={handleSubmit}
        />
      </LocalizationProvider>
    </div>
  );
};

export default InputDateForm;
