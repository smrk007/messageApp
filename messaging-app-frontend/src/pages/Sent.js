import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

import Header from './components/Header';
import MailItem from './components/MailItem';
import {
  Trash,
  ArrowBack
} from 'react-ionicons';

import { serverIp } from '../config';

const Sent = (props) => {

  let navigate = useNavigate();

  const [outbox, setOutbox] = useState([]);
  const [mailItem, setMailItem] = useState();

  useEffect(() => {

    // Ensure that the user is authenticated
    let token = localStorage.getItem('token')
    if (token == null || token === '') {
      navigate('/signin')
    }

    // Immediately get the sent items when
    // the page is loaded
    fetch(`http://${serverIp}:8000/api/outbox/`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}`,
      },
    }).then(response => {
      response.json().then(json => {
        json.reverse(); // Reverse chronological order
        setOutbox(json);
      })
    }).catch((err) => {
      console.error(err);
    });

  }, []);

  if (mailItem) {
    // Display a single mail item when one is
    // selected to be displayed
    return (
      <>
        <Header title="Sent" />
        <div style={{
          backgroundColor: 'white',
          borderBottomColor: 'black',
          borderBottomWidth: 1,
          borderBottomStyle: 'solid',
          padding: 10,
        }}>
          <div>
            <ArrowBack
              height="30px"
              width="30px"
              color="skyblue"
              style={{
                cursor: 'pointer'
              }}
              onClick={() => setMailItem()}
            />
            <Trash
              height="30px"
              width="30px"
              color="red"
              style={{
                cursor: 'pointer'
              }}
              onClick={() => {
                if (window.confirm("Are you sure you want to delete this message? This cannot be undone.")) {
                  // Delete from outbox (server side)
                  fetch(`http://${serverIp}:8000/api/outbox/${mailItem.id}`, {
                    method: 'DELETE',
                    headers: {
                      'Content-Type': 'application/json',
                      'Authorization': `Token ${localStorage.getItem('token')}`,
                    },
                  }).then(response => {
                    // Delete from outbox (local side)
                    setOutbox(outbox.filter(filterItem => filterItem.id !== mailItem.id))
                    // Go back to local
                    setMailItem()
                  }).catch((err) => {
                    console.error(err);
                  });
                }
              }}
            />
          </div>
          <div><b>From:</b> You ({mailItem.sender})</div>
          <div><b>To:</b> {mailItem.recipient}</div>
          <div><b>Title:</b> {mailItem.title}</div>
          <div><b>Body: </b> {mailItem.body}</div>
        </div>
      </>
    )
  } else {
    // Display list of items when no one item
    // is selected to be displayed
    return (
      <>
        <Header title="Sent" />
        {
          outbox.length === 0 ?
            <div>You have no sent items.</div>
            :
            outbox.map((item, idx) => (
              <MailItem
                key={idx}
                username={item.recipient}
                title={item.title}
                body={item.body}
                onSelect={() => {
                  setMailItem(item);
                }}
              />
            ))
        }
      </>
    )
  }

}

export default Sent;