 
import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import CardTitle from '../CardTitle';
import moment from 'moment'


const useStyles = makeStyles({
  depositContext: {
    flex: 1,
  },
});

const TotalCard = (props) => {
  const classes = useStyles();
  const {title, total} = props
  return (
    <React.Fragment>
      <CardTitle>Total {title}</CardTitle>
      <Typography component="p" variant="h2">
        {total}
      </Typography>
      <Typography color="textSecondary" className={classes.depositContext}>
        {moment().format('LL')}
      </Typography>
    </React.Fragment>
  );
}

export default TotalCard;