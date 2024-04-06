import React, { useState } from 'react';
import ReactDOM from 'react-dom';

const App = () => {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <h1>Calculator</h1>
      <button onClick={handleClick}>+</button>
      <span>{count}</span>
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));