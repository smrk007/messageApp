import logo from './logo.svg';
import './App.css';
import { Navigate } from "react-router-dom";

function App() {
  // Send users to inbox if authenticated
  // Send users to signin if not
  let token = localStorage.getItem('token')
  if (token == null || token === '') {
    return (
      <Navigate to="signin" />
    );
  } else {
    return (
      <Navigate to="inbox" />
    )
  }
}

export default App;
