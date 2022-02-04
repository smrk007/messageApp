import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

import Header from './components/Header';
import MailItem from './components/MailItem';

const Sent = (props) => {

  let navigate = useNavigate();

  const [outbox, setOutbox] = useState([]);

  useEffect(() => {

    // Ensure that the user is authenticated
    let token = localStorage.getItem('token')
    if (typeof token === 'undefined' || token === '') {
      navigate('/signin')
    }

    fetch(`http://localhost:8000/api/outbox/`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}`,
      },
    }).then(response => {
      response.json().then(json => {
        setOutbox(json);
      })
    }).catch((err) => {
      console.error(err);
    });

  }, []);

  return (
    <>
      <Header title="Sent" />
      {
        outbox.map((item, idx) => (
          <MailItem
            key={idx}
            username={item.recipient}
            title={item.title}
            body={item.body}
          />
        ))
      }
    </>
  )
}

export default Sent;