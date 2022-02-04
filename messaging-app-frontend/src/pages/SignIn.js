import { useState, useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

const SignIn = (props) => {

  let navigate = useNavigate();

  useEffect(() => {

    // Ensure that the user is unauthenticated
    let token = localStorage.getItem('token')
    if (typeof token !== 'undefined' && token !== '') {
      navigate('/inbox')
    }

  }, []);

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const submitForm = () => {
    fetch(`http://localhost:8000/auth/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username,
        password
      })
    }).then(response => {
      response.json().then(async (json) => {
        localStorage.setItem('token', json.token);
        navigate('/inbox');
      });
    })
  }

  return (
    <div style={{
      display: 'flex',
      flexDirection: 'row',
      justifyContent: 'center',
    }}>
      <div style={{
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        height: '100vh'
      }}>
        <Form
          onSubmit={e => {
            e.preventDefault()
            submitForm()
          }}
        >
          <Form.Group>
            <Form.Label>Username</Form.Label>
            <Form.Control value={username} onChange={(e) => setUsername(e.target.value)} type="text" placeholder="Enter your username." />
          </Form.Group>
          <Form.Group>
            <Form.Label>Password</Form.Label>
            <Form.Control value={password} onChange={(e) => setPassword(e.target.value)} type="password" placeholder="Enter your password." />
          </Form.Group>
          <Button onClick={submitForm} type="submit">
            Sign In
          </Button>
        </Form>
        <div>Don't have an account? <Link to="/signup">Sign Up</Link></div>
      </div>
    </div>
  )
}

export default SignIn;