const express = require('express');
const fetch = require('node-fetch');
const app = express();
const port = 3000;

const API_KEY = 'your_openai_api_key';

app.set('view engine', 'ejs');
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.render('index');
});

app.post('/generate', async (req, res) => {
  const { audience, product, tone } = req.body;
  const prompt = `Write a ${tone} advertisement for a ${product} targeted at ${audience}.`;

  try {
    const generatedText = await generateText(prompt);
    res.render('result', { generatedText });
  } catch (error) {
    console.error(`Error: ${error.message}`);
    res.status(500).send('Error generating text');
  }
});

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

app.listen(port, () => {
  console.log(`AI Copywriter app listening at http://localhost:${port}`);
});
