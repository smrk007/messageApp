import { useState, useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

import { serverIp } from "../config";

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
    fetch(`http://${serverIp}:8000/auth/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username,
        password
      })
    }).then(response => {
      console.log(response);
      if (response.ok) {
        response.json().then(async (json) => {
          localStorage.setItem('token', json.token);
          navigate('/inbox');
        });
      } else {
        response.json().then(async (json) => {
          console.log(json)
          alert(json.non_field_errors.join('\n'))
        });
      }
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
            <Form.Control required value={username} onChange={(e) => setUsername(e.target.value)} type="text" placeholder="Enter your username." />
          </Form.Group>
          <Form.Group>
            <Form.Label>Password</Form.Label>
            <Form.Control required value={password} onChange={(e) => setPassword(e.target.value)} type="password" placeholder="Enter your password." />
          </Form.Group>
          <Button type="submit">
            Sign In
          </Button>
        </Form>
        <div>Don't have an account? <Link to="/signup">Sign Up</Link></div>
      </div>
    </div>
  )
}

export default SignIn;