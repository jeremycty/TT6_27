import * as React from 'react';
import Checkbox from '@mui/material/Checkbox';

const label = { inputProps: { 'aria-label': 'Checkbox demo' } };

export default function SizeCheckboxes(example) {
    console.log(example)
    return (
        <div>
        <h3>{example.prop3}</h3>
        <Checkbox {...label} defaultChecked size="small" />
        <Checkbox {...label} defaultChecked />
        <Checkbox
            {...label}
            defaultChecked
            sx={{ '& .MuiSvgIcon-root': { fontSize: 28 } }}
        />
        </div>
    );
}
