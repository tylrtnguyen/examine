import React from 'react';
import RegisterForm from '../../components/RegisterForm';
import NavBar from '../../components/NavBar'

const RegisterPage = () => {
    return (
        <React.Fragment>
            <NavBar />
            <RegisterForm />
        </React.Fragment>
    )
}

export default RegisterPage;