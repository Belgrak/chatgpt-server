from typing import List
from fastapi import FastAPI
from openai import OpenAI
from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam, \
    ChatCompletionAssistantMessageParam, ChatCompletionToolMessageParam, ChatCompletionFunctionMessageParam
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()


class UserMessages(BaseModel):
    messages: List[str]


class MessagesHistory(BaseModel):
    messages: List[ChatCompletionSystemMessageParam | ChatCompletionUserMessageParam |
                   ChatCompletionAssistantMessageParam | ChatCompletionToolMessageParam |
                   ChatCompletionFunctionMessageParam]


OPENAI_KEY = os.getenv("OPENAI_API_KEY")
app = FastAPI()


@app.post("/messages_history")
async def root(msgs: MessagesHistory):
    client = OpenAI(api_key=OPENAI_KEY)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=msgs.messages
    )
    return response.choices[0].message


@app.post("/user_messages")
async def root(msgs: UserMessages):
    client = OpenAI(api_key=OPENAI_KEY)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": i} for i in msgs.messages]
    )
    return response.choices[0].message
