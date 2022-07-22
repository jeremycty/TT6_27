import React from 'react';

import Button from '@mui/material/Button';
import First from "../components/First"
import Second from "../components/Second"

export default function Secondpage() {
    
  return (
    <div>
      <input type = "number"></input>
      <Button variant="contained">Contained</Button>
      {/* <h1>This is the second page</h1>
      <h1>First component</h1>
      <First prop1 = "123" prop3 = "1234"></First>
      <h1>Second component</h1>
      <Second/> */}
    </div>
  );
}