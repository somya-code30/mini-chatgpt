import React, { useState } from 'react';

function App() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState('');

  const handleAsk = async () => {
    const res = await fetch('http://localhost:5000/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query: input })
    });
    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div className="container">
      <h1>Mini ChatGPT++</h1>
      <input
        type="text"
        value={input}
        onChange={e => setInput(e.target.value)}
        placeholder="Ask your CS question..."
      />
      <button onClick={handleAsk}>Ask</button>
      <p><strong>Response:</strong> {response}</p>
    </div>
  );
}

export default App;
