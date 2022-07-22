import React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';



export default function CurrencyBar(props) {
    // console.log(props.er_data.data)

    const er_box = props.er_data.data.map((x, index) => ( 
        <Box key = {index} className="currency--box">
            <Card variant="outlined">
                <CardContent>
                    <Typography variant="h5" component="div">
                        {x.base_currency}/{x.exchange_currency}
                    </Typography>
                    <Typography variant="h3">
                        {x.rate}
                    </Typography>
                </CardContent>
            </Card>
        </Box>
    ))

    return (
        <div className="bar">
            {er_box}
        </div>
    );
}

