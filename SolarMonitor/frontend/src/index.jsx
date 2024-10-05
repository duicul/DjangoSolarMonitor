
import { createRoot } from 'react-dom/client';
import React from 'react'
import ReactDOM from 'react-dom'
import Gauge from 'react-gauge-chart'


// Define the React app
const App = () => {
  const [count, setCount] = React.useState(0)
  const onClick = () => setCount(c => c + 1)
  return React.createElement('div', null,
    React.createElement('h1', null, 'The count is ' + count),
    React.createElement('button', { onClick: onClick }, 'Count'),
     React.createElement('GaugeChart', { id: "gauge-chart1" }, 'Gauge'),
  )
}
class GaugeShow extends React.Component {
    render() {
    return (<Gauge animate={false} 
  nrOfLevels={15} 
  percent={0.56} 
  needleColor="#345243"  />)}
    
}
// Mount the app to the mount point.
const domNode = document.getElementById('app')
const root1 = createRoot(domNode);
root1.render(React.createElement(App, null, null));

/*const domNode1 = document.getElementById('app1')
const root2 = createRoot(domNode);
root2.render(React.createElement(GaugeShow, null, null));*/

ReactDOM.render(<GaugeShow />, document.getElementById("app1"));
