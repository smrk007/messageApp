import { useState } from 'react';

const HeaderButton = ({
  IoniconsComponent,
  onClick,
  type
}) => {

  return (
    <IoniconsComponent
      height="40px"
      width="40px"
      color="skyblue"
      onClick={onClick}
      style={{
        padding: 5,
        cursor: 'pointer',
        borderRightColor: type === 'left' ? 'black' : undefined,
        borderRightStyle: type === 'left' ? 'solid' : undefined,
        borderRightWidth: type === 'left' ? 1 : undefined,
        borderLeftColor: type === 'right' ? 'black' : undefined,
        borderLeftStyle: type === 'right' ? 'solid' : undefined,
        borderLeftWidth: type === 'right' ? 1 : undefined,
      }}
    />
  )
}

export default HeaderButton;