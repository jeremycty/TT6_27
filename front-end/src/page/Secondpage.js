import React from 'react';

import First from "../components/First"
import Second from "../components/Second"

export default function Secondpage() {
    
  return (
    <div>
      <h1>This is the second page</h1>
      <h1>First component</h1>
      {/* <First/> */}
      <First prop1 = "123" prop3 = "1234"></First>
      <h1>Second component</h1>
      <Second/>
    </div>
  );
}