import React, { useState, useEffect } from 'react';

import './App.css';

function App() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `Count: ${count}`;
  });

  return (
    <div className="App">
      <header className="App-header">
        <h1>Count: {count}</h1>
        <button onClick={() => setCount(count + 1)}>+</button>
        <button onClick={() => setCount(count - 1)}>-</button>
      </header>
    </div>
  );
}

export default App;