const fetch = require('node-fetch');

const API_KEY = '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';

async function generateText(prompt) {
  const headers = {
    'Authorization': `Bearer ${API_KEY}`,
    'Content-Type': 'application/json',
  };

  const data = {
    'model': 'text-davinci-002',
    'prompt': prompt,
    'temperature': 0.8,
    'max_tokens': 100,
  };

  const response = await fetch('https://api.openai.com/v1/engines/davinci-codex/completions', {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error(`API request failed with status ${response.status}`);
  }

  const jsonResponse = await response.json();
  return jsonResponse.choices[0].text.trim();
}

(async () => {
  try {
    const prompt = 'Write a short advertisement for a new smartphone.';
    const generatedText = await generateText(prompt);
    console.log(generatedText);
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
})();


/*
Replace your_openai_api_key with your actual API key from OpenAI.
The example code defines an async function generateText that takes a prompt as input and returns the generated text from the ChatGPT API.
The main part of the script is an immediately-invoked async function that provides a prompt and prints the generated text.

Please note that this example is intended for running in a Node.js environment.
If you plan to use the API in a browser environment,
consider using a back-end proxy to avoid exposing your API key on the client-side,
as client-side JavaScript code can be viewed and manipulated by users.
*/