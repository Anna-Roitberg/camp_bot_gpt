# Summer Camp GPT bot
**Summer Camp GPT bot** is a conversational AI assistant for parents interested in the fictional GenAI Summer Camp

## Short Approach Description
0) I generated the camp description using LLM (Language Model): `capm_text.txt`      

1) Upon receiving a user's query, I consult the LLM to determine if the user intends to enroll a child in the camp.

    a) If the response is "YES," I transition to collecting essential details (parent's full name, phone number, email, and child's age).

    b) If the response is "NO," I forward both the user's question and the camp description to the LLM, requesting an answer based on the provided description.

2) During the final stage of the information collection process, I engage the LLM to structure the information into a JSON format with specific organization.

Note: I maintain a complete record of the conversation history, which I append to the current request made to the LLM.


## Usage
1. Install requirements `pip install requirements.txt`
2. Run the bot `python camp_bot.py`

Example usage:
....


