import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

import Header from './components/Header';

const Sent = (props) => {

  let navigate = useNavigate();

  const [authToken, setAuthToken] = useState('');

  useEffect(() => {

    // Ensure that the user is authenticated
    let token = localStorage.getItem('token')
    if (typeof token === 'undefined' || token === '') {
      navigate('/signin')
    }

    setAuthToken(token);

    // TODO: Get sent contents

  }, []);

  return (
    <>
      <Header title="Sent" />
    </>
  )
}

export default Sent;