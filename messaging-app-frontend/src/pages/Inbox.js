import { Component } from 'react';
import { useNavigate } from 'react-router-dom';

import Container from 'react-bootstrap/Container';

import HeaderButton from './components/HeaderButton';
import {
  Mail,
  Send,
  Create,
  Exit
} from 'react-ionicons';
import { Navigate } from 'react-ionicons';

const Inbox = (props) => {

  let navigate = useNavigate();

  return (
    <>
      {/* Header */}
      <div style={{
        display: 'flex',
        flexDirection: 'row',
        borderBottomColor: 'black',
        borderBottomStyle: 'solid',
        borderBottomWidth: 1,
      }}>
        <HeaderButton
          IoniconsComponent={Mail}
          type="left"
          onClick={()=>navigate('/inbox')}
        />
        <HeaderButton
          IoniconsComponent={Send}
          type="left"
          onClick={()=>navigate('/sent')}
        />
        <HeaderButton
          IoniconsComponent={Create}
          type="left"
          onClick={()=>navigate('/compose')}
        />
        <h3>Inbox</h3>
        <span style={{ flex: 1 }} />
        <HeaderButton
          IoniconsComponent={Exit}
          type="right"
          onClick={()=>navigate('/signin')}
        />
      </div>
    </>
  )
}

export default Inbox;