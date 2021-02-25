import React from 'react';
import Footer from '../../components/Footer';
import MainLayout from '../../components/MainLayout';
import NavBar from '../../components/NavBar';

const IndexPage = () => {
    return (
        <React.Fragment>
            <NavBar />
            <MainLayout />
            <Footer />
        </React.Fragment>
    )
}

export default IndexPage;