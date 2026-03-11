# chatbot.py - AI Chatbot Logic

import os
from groq import Groq
from policy_data import get_policy

# Initialize Groq client (API key from environment variable)
# Streamlit Cloud injects secrets as env vars automatically
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_bot(user_question: str) -> str:
    """
    Takes user question, retrieves relevant policy, 
    and generates AI-powered answer
    """
    # Step 1: Get relevant policy from our knowledge base
    policy_context = get_policy(user_question)
    
    # Step 2: Create prompt for AI
    prompt = f"""
    You are a helpful HR assistant. Answer the employee's question using the policy information below.
    
    Policy Information:
    {policy_context}
    
    Employee Question: {user_question}
    
    Answer clearly and professionally. If the policy doesn't cover this, politely direct to HR.
    Keep responses concise but helpful.
    """
    
    # Step 3: Get AI response
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # Updated free model
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.3  # Keep answers consistent
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"