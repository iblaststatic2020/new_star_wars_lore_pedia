import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Login from './components/Login';
import Register from './components/Register';
import ArticleList from './components/ArticleList';
import Article from './components/Article';
import CreateArticle from './components/CreateArticle';
import LoginModal from './components/LoginModal';
import Footer from './components/footer'; // Import your Footer component



function App() {
  const [showModal, setShowModal] = useState(false);
  const toggleModal = () => {
    setShowModal(!showModal);
  };

  return (
    <Router>
      <div className="App">
        <Navbar toggleModal={toggleModal} />
        <LoginModal showModal={showModal} handleClose={toggleModal} />
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/article/:id" element={<Article />} />
          <Route path="/create" element={<CreateArticle />} />
          <Route path="/" element={<ArticleList />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
