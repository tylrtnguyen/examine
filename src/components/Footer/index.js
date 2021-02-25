import React from 'react';
import Copyright from '../Copyright';
import Typography from '@material-ui/core/Typography';
import Link from '@material-ui/core/Link';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = () => makeStyles((theme) => ({
    footer: {
        backgroundColor: theme.palette.background.paper,
        padding: theme.spacing(10)
    }
}))

const Footer = () => {
    const classes = useStyles();

    return (
        <footer className={classes.footer}>
            <Typography variant="h6" align="center" gutterBottom>
                Examine
            </Typography>
            <Typography variant="subtitle1" align="center" color="textSecondary" component="p">
                Made with ❤ by <Link color="inherit" href="https://thongba.io">Thong Nguyen</Link>
            </Typography>
            <Copyright />
        </footer>
    )

};

export default Footer;