import { Component, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

import Container from 'react-bootstrap/Container';

import HeaderButton from './HeaderButton';
import {
  Mail,
  Send,
  Create,
  Exit
} from 'react-ionicons';

const Header = ({
  title
}) => {

  let navigate = useNavigate();

  return (
    <div style={{
      display: 'flex',
      flexDirection: 'row',
      borderBottomColor: 'black',
      borderBottomStyle: 'solid',
      borderBottomWidth: 1,
      backgroundColor: 'white',
    }}>
      <HeaderButton
        IoniconsComponent={Mail}
        type="left"
        onClick={() => navigate('/inbox')}
      />
      <HeaderButton
        IoniconsComponent={Send}
        type="left"
        onClick={() => navigate('/sent')}
      />
      <HeaderButton
        IoniconsComponent={Create}
        type="left"
        onClick={() => navigate('/compose')}
      />
      <h3>{title}</h3>
      <span style={{ flex: 1 }} />
      <HeaderButton
        IoniconsComponent={Exit}
        type="right"
        onClick={() => {
          localStorage.setItem('token', '');
          navigate('/signin')
        }}
      />
    </div>
  )
}

export default Header;