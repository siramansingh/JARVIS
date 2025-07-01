from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role":"system", "content": "You are virtual assistant named jarvis skilled in general task like alexa and Google Cloud",
            "role":"user", "content": "what is coding"
        }
    ]
    
)

print(chat_completion.choices[0].message.content)





# {"role":"system", "content": "You are virtual assistant named jarvis skilled in general task like alexa and Google Cloud"},
#         {"role":"user", "content": "what is coding"}