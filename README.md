# GPT - 4

## Usage - JavaScript/TypeScript

1. Run the python app:

```bash
gunicorn app:app
```

2. Fetch response:

```js
const res = await fetch('https://127.0.0.1:8000/ask', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        messages: [{
            role: 'assistant',
            content: 'Hello! How can I assist you today?'
        }, {
            role: 'user',
            content: 'who built taj mahal and when'
        }]
    })
});

const data = await res.json();

console.log(data.response);

```
