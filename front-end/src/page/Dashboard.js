import React from 'react';

import CurrencyBar from "../components/CurrencyBar"
import Wallets from "../components/Wallets"

import ExchangeRate from "../data/exchangeRate.json"
import Wallets_data from "../data/wallet.json"
import Wallets_cur from "../data/currency.json"

import "../css/dashboard.css";

export default function Secondpage() {
    
    return (
        <div>
            <h1 className = "dashboard-title">Exchange Rates</h1>
            <CurrencyBar er_data = {{...ExchangeRate}} ></CurrencyBar>

            <h1 className = "dashboard-title" style = {{color:'rgb(139, 156, 232)'}}>Wallets</h1>
            <Wallets wallet_data = {{...Wallets_data}} currency = {{... Wallets_cur}}></Wallets>

        </div>
    );
}