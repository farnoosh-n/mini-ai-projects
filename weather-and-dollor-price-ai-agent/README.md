# Weather & Dollar Price AI Agent

A simple AI Agent built with **LangChain** and **Ollama**.

## Features

* Get current weather for a city
* Get the current US dollar price in toman
* Uses LangChain Tools
* Uses Qwen 2.5 3B with Ollama

## Technologies

* Python
* LangChain
* Ollama
* Qwen 2.5 3B
* Open-Meteo API
* Tindex API

## Example

User:

```text
What's the weather in Berlin and what is the current US dollar price in toman?
```

Agent:

```text
The current weather in Berlin is 18.8°C with partly cloudy skies.
The current US dollar price in toman is 214950 tomans.
```

## Setup

Create a `.env` file:

```env
TINDEX_TOKEN=your_tindex_token
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python agent-weather-and-dollor3.py
```

> Do not upload your `.env` file or API token to GitHub.
