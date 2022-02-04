import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter, Routes, Route } from "react-router-dom";

import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';

import App from './App';
import Inbox from './pages/Inbox';
import Sent from './pages/Sent.js';
import SignIn from './pages/SignIn.js';
import SignUp from './pages/SignUp';
import Compose from './pages/Compose';

ReactDOM.render(
  <div style={{
    backgroundColor: 'skyblue',
    minHeight: '100vh',
    width: '100%',
  }}>
    <Container style={{
      backgroundColor: 'skyblue',
      minHeight: '100vh',
      padding: 0,
    }}>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<App />} />
          <Route path="inbox" element={<Inbox />} />
          <Route path="sent" element={<Sent />} />
          <Route path="signin" element={<SignIn />} />
          <Route path="signup" element={<SignUp />} />
          <Route path="compose" element={<Compose />} />
        </Routes>
      </BrowserRouter>
    </Container>
  </div>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
