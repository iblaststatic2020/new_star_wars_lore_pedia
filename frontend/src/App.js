import React from 'react';
import { BrowserRouter as Router, Route, Switch, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Login from './components/Login';
import Register from './components/Register';
import ArticleList from './components/ArticleList';
import Article from './components/Article';
import CreateArticle from './components/CreateArticle';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/login" component={Login} />
          <Route path="/register" component={Register} />
          <Route path="/article/:id" component={Article} />
          <Route path="/create" component={CreateArticle} />
          <Route path="/" component={ArticleList} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
