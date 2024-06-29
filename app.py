from openai import AsyncOpenAI
import chainlit as cl

client = AsyncOpenAI()

# Instrument the OpenAI client
cl.instrument_openai()

settings = {
    "model": "gpt-4o",
    "temperature": 0.1,
}


@cl.on_message
async def on_message(message: cl.Message) -> None:
    response = await client.chat.completions.create(
        messages=[
            {
                "content": "You are a helpful bot, you always reply in haiku",
                "role": "system",
            },
            {
                "content": message.content,
                "role": "user",
            },
        ],
        **settings,
    )
    await cl.Message(
        content=response.choices[0].message.content,
    ).send()
