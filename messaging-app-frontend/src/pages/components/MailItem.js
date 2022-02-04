import { useState } from 'react';

const MailItem = ({
  username,
  title,
  body,
  contentId
}) => {

  const [hovered, setHovered] = useState(false);

  return (
    <div
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      style={{
        borderBottomColor: 'black',
        borderBottomWidth: 1,
        borderBottomStyle: 'solid',
        backgroundColor: hovered ? 'lightgray' : 'white',
        padding: 10,
        cursor: 'pointer'
      }}
    >
      <div><b>{username}</b></div>
      <div><b>{title}</b></div>
      <div>{body}</div>
    </div>
  )
}

export default MailItem;