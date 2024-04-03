import openai
import gradio

openai.api_key = ""

messages = [{"role": "system", "content": "You are an assistant trained to study the correlation between AI technologies and impacts on biodiversity. You must give a score based on the following 3 pillars: 1. Data Synergy 2. Data Relevance 3. Data Cleanliness"}]

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
