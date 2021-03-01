import React from 'react';
import Copyright from '../Copyright';
import CssBaseline from '@material-ui/core/CssBaseline';
import Container from '@material-ui/core/Container';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
    root: {
      display: 'flex',
      flexDirection: 'column',
      maxHeight: '100vh',
    },
    footer: {
      padding: theme.spacing(3, 2),
      marginTop: 'calc(5% + 60px)',
      bottom: 0,
      backgroundColor:
        theme.palette.type === 'light' ? theme.palette.grey[200] : theme.palette.grey[800],
    },
  }));

const Footer = () => {
    const classes = useStyles();

    return (
        <div className={classes.root}>
      <CssBaseline />
      <footer className={classes.footer}>
        <Container maxWidth="sm">
          <Copyright />
        </Container>
      </footer>
    </div>
    )

};

export default Footer;