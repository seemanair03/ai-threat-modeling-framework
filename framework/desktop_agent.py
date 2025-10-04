"""Ethical and responsible use of AI is important. Ensure compliance with all relevant policies and guidelines when using AI models."""


"""Run this model in Python

> pip install openai
"""
import os
from openai import OpenAI

# To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings.
# Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
client = OpenAI(
    base_url = "https://models.github.ai/inference",
    api_key = os.environ["/<GITHUB_TOKEN>/"],
    default_query = {
        "api-version": "2024-08-01-preview",
    },
)

messages = [
    {
        "role": "system",
        "content": "Provide clear, concise, and polite responses as a desktop chat support agent to assist users with their inquiries and issues related to desktop software, hardware, or services.\n\n- Greet users courteously and identify their problems or questions.\n- Ask relevant clarifying questions if needed to better understand the user's issue.\n- Provide step-by-step troubleshooting instructions or information.\n- Use simple, non-technical language unless the user indicates technical proficiency.\n- Maintain a professional and empathetic tone throughout the conversation.\n- Summarize solutions or next steps before concluding the interaction.\n  \n# Steps\n\n1. Start with a friendly greeting and offer help.\n2. Collect information about the user's problem.\n3. Analyze the issue based on the information provided.\n4. Offer clear, actionable advice or solutions.\n5. Confirm if the user’s issue is resolved or if further assistance is needed.\n6. Close the interaction politely.\n\n# Output Format\n\nDeliver responses in clear, complete sentences suitable for a chat interface, with concise explanations and any relevant step-by-step instructions. Avoid overly long paragraphs; use line breaks or bullet points when helpful. Ensure messages are easy to read and user-friendly.",
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Hi",
            },
        ],
    },
    {
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": "Hello! How can I assist you with your desktop today?",
            },
        ],
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Why does my system keeps restarting?",
            },
        ],
    },
]

tools = []

response_format = {
    "type": "text"
}

while True:
    response = client.chat.completions.create(
        messages = messages,
        model = "openai/gpt-4.1-mini",
        tools = tools,
        response_format = response_format,
        temperature = 1,
        top_p = 1,
    )

    if response.choices[0].message.tool_calls:
        print(response.choices[0].message.tool_calls)
        messages.append(response.choices[0].message)
        for tool_call in response.choices[0].message.tool_calls:
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": [
                    {
                        "type": "text",
                        "text": locals()[tool_call.function.name](),
                    },
                ],
            })
    else:
        print("[Model Response] " + response.choices[0].message.content)
        break
