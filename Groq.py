import os
from groq import Groq

# Initialize client using environment variable
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
#Query Function
def chat(user_message):
    """Send message to Groq API and get response"""
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant. Answer clearly in simple words."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            max_tokens=1000,
            temperature=0.7
        )

        print("\nResponse:")
        print(response.choices[0].message.content)

    except Exception as e:
        print("Error:", e)


# Main program
if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    chat(user_input)