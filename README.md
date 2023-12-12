# FastAPI ChatGPT Server

This repository contains a FastAPI server that utilizes the OpenAI GPT-3.5 language model for chat-based applications.

## Prerequisites

Before running the FastAPI server, make sure you have the following prerequisites installed:

- Python 3.7 or later
- Pip (Python package installer)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Belgrak/chatgpt-server.git
    ```

2. Change to the project directory:

   ```bash
   cd chatgpt-server
    ```
   
3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
    ```
   
## Configuration
1. Obtain your OpenAI GPT-3.5 API key from OpenAI.

2. Create a file named .env in the project root and add your API key:

   ```env
   OPENAI_API_KEY=your-api-key-goes-here
    ```
   
## Usage
Run the FastAPI server using the following command:

   ```bash
   uvicorn main:app --reload
   ```

The `--reload` flag enables auto-reloading of the server when code changes are detected, which is useful during development.

Visit http://127.0.0.1:8000/docs in your browser to access the FastAPI interactive documentation. You can test the chat endpoint and interact with the OpenAI GPT-3.5 model.

## API Endpoints
1. `/messages_history`: POST endpoint for interacting with the GPT-3.5 model. Send a JSON request with the user and system messages.
Example JSON request:

   ```json
      {
     "messages": [
       {"role": "user", "content": "Hello, GPT!"},
       {"role": "assistant", "content": "Hi there! How can I assist you today?"}
     ]
     }
   ```

2. `/user_messages`: POST endpoint for interacting with the GPT-3.5 model. Send a JSON request with the user messages only.
Example JSON request:

```json
   {
    "messages": ["Hello", "How are you?"]
   }
```