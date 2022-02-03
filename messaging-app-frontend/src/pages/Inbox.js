import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

import Header from './components/Header';

const Inbox = (props) => {

  let navigate = useNavigate();

  const [authToken, setAuthToken] = useState('');

  useEffect(() => {

    // Ensure that the user is authenticated
    let token = localStorage.getItem('token')
    if (typeof token === 'undefined' || token === '') {
      navigate('/signin')
    }

    setAuthToken(token);

    // TODO: Get inbox contents

  }, []);

  return (
    <>
      <Header title="Inbox" />
    </>
  )
}

export default Inbox;