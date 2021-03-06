import React from 'react';
import RegisterForm from '../../components/RegisterForm';
import NavBar from '../../components/NavBar';
import Footer from '../../components/Footer';

const RegisterPage = () => {
    return (
        <React.Fragment>
            <NavBar title="Examine" link="/" />
            <RegisterForm />
            <Footer />
        </React.Fragment>
    )
}

export default RegisterPage;