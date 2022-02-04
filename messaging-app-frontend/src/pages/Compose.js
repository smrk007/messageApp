import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

import Header from './components/Header';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Spinner from 'react-bootstrap/Spinner';

import { serverIp } from '../config';

const Compose = (props) => {

  let navigate = useNavigate();

  const [recipient, setRecipient] = useState('');
  const [title, setTitle] = useState('');
  const [body, setBody] = useState('');
  const [sending, setSending] = useState(false);

  const [authToken, setAuthToken] = useState('');

  useEffect(() => {

    // Ensure that the user is authenticated
    const token = localStorage.getItem('token')
    if (typeof token === 'undefined' || token === '') {
      navigate('/signin')
    }

    setAuthToken(token);

  }, []);


  return (
    <>
      <Header title="Compose" />
      <Container>
        <Form
          onSubmit={e => {
            e.preventDefault()

            if (title.length === 0) {
              alert("Please enter a title")
              return;
            }
            if (body.length === 0) {
              alert("Please enter text into the body")
              return;
            }

            setSending(true);
            fetch(`http://${serverIp}:8000/api/message/`,{
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${authToken}`,
              },
              body: JSON.stringify({
                recipient,
                body,
                title,
              })
            }).then(response => {
              setSending(false);
              if (response.ok) {
                navigate('/sent');
              } else {
                response.json().then(json => {
                  alert(Object.values(json).join('\n'));
                })
              }
            }).catch((err) => {
              console.error(err);
              setSending(false);
            });
          }}
        >
          <Form.Group>
            <Form.Label>Recipient</Form.Label>
            <Form.Control required value={recipient} onChange={(e) => setRecipient(e.target.value)} type="text" placeholder="Enter your message recipient." />
          </Form.Group>
          <Form.Group>
            <Form.Label>Title</Form.Label>
            <Form.Control value={title} onChange={(e) => setTitle(e.target.value)} type="text" placeholder="Enter your message title." />
          </Form.Group>
          <Form.Group>
            <Form.Label>Body</Form.Label>
            <Form.Control as="textarea" value={body} onChange={(e) => setBody(e.target.value)} type="text" placeholder="Enter your message body." />
          </Form.Group>
          <div style={{
            display: 'flex',
            flexDirection: 'row',
            justifyContent: 'flex-end',
          }}>
            <Button variant="info" type="submit">
              {sending ? <Spinner animation="border" variant="dark" /> : "Send"}
            </Button>
          </div>
        </Form>
      </Container>
    </>
  )
}

export default Compose;