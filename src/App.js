import React, { useState, useEffect } from 'react';
import Chart from './components/Chart';

const App = () => {
  const [data, setData] = useState([50, 100, 150, 200]);

  useEffect(() => {
    const interval = setInterval(() => {
      setData(data => data.map(d => d + Math.floor(Math.random() * 10)));
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
      <div>
        <h1>Real-Time Game Analytics</h1>
        <Chart data={data} />
      </div>
  );
};

export default App;
