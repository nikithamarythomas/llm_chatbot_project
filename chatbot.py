import os
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage

# Load local model
llm = ChatOllama(model="llama3")

print("Local AI Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = llm.invoke([HumanMessage(content=user_input)])

    print("AI:", response.content)