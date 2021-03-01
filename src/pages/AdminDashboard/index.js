import React, {useState, useEffect } from 'react';
import clsx from 'clsx';
import Unauthorized from '../../components/Unauthorized';
import { Container, Grid, Paper } from '@material-ui/core';
import TotalCard from '../../components/TotalCard';
import { UseStyles } from './UseStyles';
import { getToken, checkAuthorization } from '../../utils';
import StaticToolbar from '../../components/StaticToolbar';





const AdminDashboard = () => {
    // Custom Styles
    const classes = UseStyles();
    // Local State
    const [hasToken, setHasToken] = useState(false)
    const [isAuthorized, setIsAuthorized] = useState(false)

    
    

    const fixedHeightPaper = clsx(classes.paper, classes.fixedHeight);

    // Pass [] as the second parameter to avoid activating it on component
    // updates but only for the mounting of the component.
    useEffect(() => {
      const token = getToken()
      const hasToken = token === null ? false : true
      setHasToken(hasToken)
      const authStatus = checkAuthorization()
      setIsAuthorized(authStatus)
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [])

    

    if(hasToken && isAuthorized){
        return (
            <div className={classes.root}>
            <StaticToolbar title="Dashboard" />
            <main className={classes.content}>
              <div className={classes.appBarSpacer} />
              <Container maxWidth="lg" className={classes.container}>
                <Grid container spacing={3}>
                   {/* Total Users */}
                    <Grid item xs={12} md={6} lg={6}>
                    <Paper className={fixedHeightPaper}>
                        <TotalCard title="Users" total="17"/>
                    </Paper>
                    </Grid>
                    {/* Total Events */}
                    <Grid item xs={12} md={6} lg={6}>
                        <Paper className={fixedHeightPaper}>
                            <TotalCard title="Events" total="17"/>
                        </Paper>
                    </Grid>
                    {/* Total rooms */}
                    <Grid item xs={12} md={6} lg={6}>
                        <Paper className={fixedHeightPaper}>
                            <TotalCard title="Rooms" total="17"/>
                        </Paper>
                    </Grid>
                    <Grid item xs={12} md={6} lg={6}>
                        <Paper className={fixedHeightPaper}>
                            <TotalCard title="Messages" total="17"/>
                        </Paper>
                    </Grid>
                </Grid>
              </Container>
            </main>
          </div>
        )
    }
    else{
        return (
        <Unauthorized />
        )
    }
}

export default AdminDashboard;