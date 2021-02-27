import React from 'react';
import PropTypes from 'prop-types';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import BorderColorIcon from '@material-ui/icons/BorderColor';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Link from '@material-ui/core/Link';




const useStyles = makeStyles((theme) => ({
    icon: {
        marginRight: theme.spacing(2)
    },
    root: {
        flexGrow: 1,
    },
    title: {
        flexGrow: 1
    }
}))

const NavBar = ({ title, link }) => {
    const classes = useStyles();

    return (
        <div className={classes.root}>
                <AppBar position="static">
                    <Toolbar>
                    <BorderColorIcon className={classes.icon} />
                    <Link href={link} color="inherit">
                    <Typography variant="h6" color="inherit" noWrap>
                        {title}
                    </Typography>
                    </Link>
                    </Toolbar>
                </AppBar>
        </div>
        
    )
}

export default NavBar;

NavBar.propTypes = {
    title: PropTypes.string.isRequired,
    link: PropTypes.string.isRequired
}