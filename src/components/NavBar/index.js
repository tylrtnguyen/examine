import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import CssBaseline from '@material-ui/core/CssBaseline';
import Toolbar from '@material-ui/core/Toolbar';
import BorderColorIcon from '@material-ui/icons/BorderColor';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';




const useStyles = makeStyles((theme) => ({
    icon: {
        marginRight: theme.spacing(2)
    }
}))

const NavBar = () => {
    const classes = useStyles();

    return (
        <React.Fragment>
            <CssBaseline />
            <AppBar position="relative">
                <Toolbar>
                <BorderColorIcon className={classes.icon} />
                <Typography variant="h6" color="inherit" noWrap>
                    Examine
                </Typography>
                </Toolbar>
            </AppBar>
        </React.Fragment>
        
    )
}

export default NavBar;