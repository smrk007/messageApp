import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

import Header from './components/Header';
import MailItem from './components/MailItem';

const Inbox = (props) => {

  let navigate = useNavigate();
  const [inbox, setInbox] = useState([]);

  useEffect(() => {

    // Ensure that the user is authenticated
    let token = localStorage.getItem('token')
    if (typeof token === 'undefined' || token === '') {
      navigate('/signin')
    }

    // TODO: Get inbox contents

  }, []);

  return (
    <>
      <Header title="Inbox" />
      {
        inbox.length === 0 ?
        <div>You have no items in your inbox.</div>
        :
        inbox.map(item => (
          <MailItem
          />
        ))
      }
    </>
  )
}

export default Inbox;