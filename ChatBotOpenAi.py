import openai

api_key = "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"
openai.api_key = api_key

def send_message(mensagem):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": mensagem}
        ]
    )

    return response.choices[0].message['content']

print(send_message("Em que ano Einstein publicou a teoria geral da relatividade?"))
0