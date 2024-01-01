import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are an assistant trained to study the correlation between AI technologies and impacts on biodiversity"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "BioBot")

demo.launch(share=True)