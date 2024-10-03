
import { createRoot } from 'react-dom/client';
import React from 'react'
import ReactDOM from 'react-dom'

// Define the React app
const App = () => {
  const [count, setCount] = React.useState(0)
  const onClick = () => setCount(c => c + 1)
  return React.createElement('div', null,
    React.createElement('h1', null, 'The count is ' + count),
    React.createElement('button', { onClick: onClick }, 'Count'),
  )
}
// Mount the app to the mount point.
const domNode = document.getElementById('app')
const root1 = createRoot(domNode);
root1.render(React.createElement(App, null, null));