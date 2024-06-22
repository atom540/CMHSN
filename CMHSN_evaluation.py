import streamlit as st
import openai
from openai import AzureOpenAI

# Set up OpenAI API credentials
openai.api_key = st.secrets["OPENAI_API_KEY"]
ENDPOINT = "https://polite-ground-030dc3103.4.azurestaticapps.net/api/v1"
MODEL_NAME = "gpt-35-turbo"
API_VERSION = "2024-02-01"

client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    api_key=openai.api_key,
    api_version=API_VERSION,
)

def generate_ai_recommendation(user_data):
    # Define the prompts tailored for mental health support
    messages = [
        {
            "role": "system",
            "content": "You are a mental health advisor."
        },
        {
            "role": "user",
            "content": (
                f"I am currently facing the following mental health issue:\n"
                f"Issue: {user_data['issue_facing']}\n"
                f"\nDuration of the issue: {user_data['duration_issue']}\n"
                f"\nHave I sought professional help before? {user_data['sought_help']}\n"
                f"\nSpecific concerns or symptoms I would like to share:\n{user_data['specific_concerns']}"
            )
        },
        {
            "role": "assistant",
            "content": (
                "Based on the information provided, here are some recommendations and advice to support your mental well-being:\n"
                "\n1. **Self-care Practices**: Consider incorporating daily self-care routines such as meditation, yoga, or spending time in nature to reduce stress levels.\n"
                "\n2. **Professional Support**: It is important to consider consulting with a qualified mental health professional for a proper assessment and personalized support. They can provide guidance tailored to your specific needs.\n"
                "\n3. **Community and Social Support**: Connecting with supportive friends, family members, or joining peer support groups can provide emotional support and reduce feelings of isolation.\n"
                "\n4. **Healthy Lifestyle**: Maintaining a balanced diet, regular physical activity, and ensuring adequate sleep can positively impact your overall mental health.\n"
                "\n5. **Stress Management Techniques**: Practice relaxation techniques such as deep breathing exercises, progressive muscle relaxation, or mindfulness meditation to manage anxiety and stress effectively.\n"
                "\n6. **Further Assessment and Treatment**: If your symptoms persist or worsen, consider seeking a comprehensive evaluation from a mental health professional. They can discuss treatment options such as therapy or medication if necessary.\n"
                "\nPlease remember, while these recommendations aim to provide support, they are not a substitute for professional advice. It's essential to consult with a qualified mental health professional for personalized guidance and treatment.\n"
            )
        }
    ]


    # Generate AI response based on the provided prompts
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        max_tokens=1500,
        temperature=0.7,
        seed=42,
    )

    return response.choices[0].message.content


def generate_gpt_response(question):
    # Define prompts for additional questions to GPT-3.5-turbo
    messages = [
        {
            "role": "system",
            "content": "You are a knowledgeable mental health adviser."
        },
        {
            "role": "user",
            "content": (
                f"I would like to know more about {question}. "
                "Could you provide detailed insights or practical advice on this topic?"
            )
        }
    ]

    # Generate AI response based on the user's question
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        max_tokens=1500,  # Adjust max_tokens based on desired response length
        temperature=0.7,
        seed=42,
    )

    return response.choices[0].message.content
