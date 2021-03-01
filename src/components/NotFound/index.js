import React from 'react';
import Button from '@material-ui/core/Button';
import { Link } from 'react-router-dom';
import { ReactComponent as NotFoundIcon } from '../../assets/404.svg'
import './styles.css'


const NotFound = () => {
    return (

            <div className="container">
                <NotFoundIcon />
                <h1>Page Not Found</h1>
                <Link to="/"><Button variant="contained" color="primary">Return to home page</Button></Link>
            </div>
        
        
    )
}

export default NotFound;