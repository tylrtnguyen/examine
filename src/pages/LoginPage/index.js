import React from 'react';
import NavBar from '../../components/NavBar';
import Footer from '../../components/Footer';
import LoginForm from '../../components/LoginForm';

const LoginPage = () => {
    return (
        <React.Fragment>
            <NavBar />
            <LoginForm />
            <Footer />
        </React.Fragment>
    )
}

export default LoginPage;