#1. For centralized model configuration
#2. Easy Model Swapping Later
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm():
    return ChatGoogleGenerativeAI(
        # model="gemini-1.5-pro",
        model = "gemini-2.5-flash",
        temperature=0.3
    )

