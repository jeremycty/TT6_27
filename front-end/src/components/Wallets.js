import React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';

import Table from './WalletTable';

export default function Wallets(props) {
    console.log(props.currency.data[0])
    console.log(props.wallet_data.data[0])


    const wallet_array = props.wallet_data.data.map((x, index) => (

        <Grid item xs={4} key = {index}>
            <Card >
                <CardMedia
                component="img"
                alt={x.name}
                height="140"
                image="/static/images/cards/contemplative-reptile.jpg"
                />
                    <CardContent>
                    <Typography gutterBottom variant="h5" component="div">
                        {x.name}
                    </Typography>
                    {/* <Typography variant="body2" color="text.secondary"> */}
                    <Table data = {props.currency.data} id = {x.id}/>
                    {/* </Typography> */}
                    </CardContent>
                    <CardActions>

                    <div style={{textalign: 'center'}} className = 'button--div'>
                        <Button size="small" >Access Wallet</Button>
                    </div>
                    
                </CardActions>
            </Card>
        </Grid>
    ))

    return (

    <Grid container rowSpacing={1} columnSpacing={{ xs: 1, sm: 2, md: 3 }}>
        {wallet_array}
    </Grid>
    );
}
