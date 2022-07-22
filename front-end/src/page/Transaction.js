import React from 'react';

export default function Wallet() {
    
    return (
      <div>
        <br></br>
        <label for="currency">Choose a currency to change from:</label>
        <select name="currency" id="currency">
        <option value="EUR">EUR</option>
        <option value="SGD">SGD</option>
        <option value="JPY">JPY</option>
        <option value="NOK">NOK</option>
        </select>

        <br></br>
        <br></br>

        <label for="Amount">Amount :</label>
        <input type="number" id="Amount" name="Amount"></input>

        <br></br>
        <br></br>

        <label for="currency">Choose a currency to change to:</label>
        <select name="currency" id="currency">
        <option value="EUR">EUR</option>
        <option value="SGD">SGD</option>
        <option value="JPY">JPY</option>
        <option value="NOK">NOK</option>
        </select>

        <br></br>
        <br></br>
        <input type="submit"></input>
        
        <br></br>
        <br></br>
        <button id = "delete"> Delete</button>



      </div>
    );
  }