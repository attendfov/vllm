# _*_ coding: utf-8 _*_
from openai import OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://10.10.106.240:8000/v1"

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=openai_api_key,
    base_url=openai_api_base,
)

models = client.models.list()
model = models.data[0].id
stream = True
chat_completion = client.chat.completions.create(
    messages=[{
        "role": "system",
        "content": "You are a helpful assistant."
    }, {
        "role": "user",
        "content": "使用python,写一个贪吃蛇的程序"
    }],
    stop=["<|endoftext|>"],
    model=model,
    stream=stream
)


if not stream:
    print("Chat completion results:")
    print(chat_completion)
    print(chat_completion.choices[0].message.content)
else:
    result_text = ''
    for info in chat_completion:
        content = info.choices[0].delta.content
        if content is None:
            continue

        result_text = result_text + content

    print(result_text)
