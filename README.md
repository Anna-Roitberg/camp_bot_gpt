# Summer Camp GPT bot
**Summer Camp GPT bot** is a conversational AI assistant for parents interested in the fictional GenAI Summer Camp

## Short Approach Description
0) I generated the camp description using LLM (Language Model): `capm_text.txt`      

1) Upon receiving a user's query, I consult the LLM to determine if the user intends to enroll a child in the camp.

    a) If the response is "YES," I transition to collecting essential details (parent's full name, phone number, email, and         child's age).

    b) If the response is "NO," I forward both the user's question and the camp description to the LLM, requesting an answer         based on the provided description.

2) During the final stage of the information collection process, I engage the LLM to structure the information into a JSON format with specific organization.

Note: I maintain a complete record of the conversation history, which I append to the current request made to the LLM.


## Usage
1. Install requirements `pip install requirements.txt`
2. Run the bot `python camp_bot.py`

## Example usage:
```
Welcome to our Summer Camp near Kinneret lake! We are thrilled to offer a fun and enriching experience for children of various age groups. Here is all the information you need:

Offerings:
- Our Summer Camp provides a wide range of activities including outdoor adventures, water sports, arts and crafts, team-building games, nature exploration, sports competitions, talent shows, themed events, and more.
- Our goal is to create an inclusive and stimulating environment where campers can develop new skills, make lasting friendships, and create wonderful memories.

Values:
- Safety, personal growth, respect, teamwork, and environmental awareness are our core values.
- Our experienced staff members ensure that every camper feels supported, valued, and encouraged to reach their full potential.

Policies:
- We have implemented certain policies to maintain a safe and enjoyable environment.
- These include adhering to a code of conduct promoting kindness, inclusivity, and respect.
- Strict safety protocols are in place during all activities for the well-being of every participant.

Location:
- Our Summer Camp is located near the beautiful Kinneret lake (Sea of Galilee) in Israel.
- The stunning natural surroundings provide the perfect backdrop for exciting adventures and unforgettable experiences.

Dates:
- The Summer Camp runs from June 1st to August 31st.
- You can choose the specific week(s) or month(s) that best suit your schedule and preferences.

Prices:
- The cost of the Summer Camp varies depending on the duration of enrollment.
- For one week, the price is $200.
- If you enroll your child for a longer period, we offer discounted rates: $700 per month (four consecutive weeks).
- Please note that these prices include all activities, meals, and accommodations during the camp.

Age Range:
- Our Summer Camp welcomes children between the ages of 7 and 14.
- We have age-appropriate programs and activities designed to cater to each group's specific needs and interests.

We hope this information helps you in planning a fantastic summer experience for your child at our Summer Camp near Kinneret lake. If you have any further questions or need additional details, please feel free to reach out to us.
```

`How can I help you?` <ins>*Where the camp is loacted?*  </ins>     
`Our Summer Camp is located near the picturesque Kinneret lake, also known as the Sea of Galilee, in Israel. The stunning natural surroundings provide the perfect backdrop for exciting adventures and unforgettable experiences.`   

`How can I help you?` <ins>*What price for two weeks?* </ins>     
`The price for two weeks at our Summer Camp is $400. This includes all activities, meals, and accommodations during the camp.`   

`How can I help you?` <ins>*I want to enroll my child*</ins>     

```
To enroll your child in our Summer Camp near Kinneret lake, we kindly ask for the following information:

1. Full Name of Parent/Guardian:
2. Phone Number (please provide a valid phone number):
3. Email Address (please provide a valid email address):
4. Child's Age (please ensure that the age falls within the range of 7-14):

Please provide the requested information so we can proceed with the enrollment process.
```
`Please provide information (type STOP to end conversation):`  <ins>*Anna Roytberg, +333222777888, anna@home.org, 7*</ins>   
     

```
Thank you for providing the information. I have noted down your details as follows:

- Full Name of Parent/Guardian: Anna Roytberg
- Phone Number: +333222777888
- Email Address: anna@home.org
- Child's Age: 7

Please note that we will validate the provided phone number and email address to ensure accurate communication. We will be in touch with you shortly regarding the enrollment process for your child.
```

`Please provide information (type STOP to end conversation):` <ins>*STOP*</ins>   

```
{'parentName': 'Anna Roytberg', 'phoneNumber': '+333222777', 'emailAddress': 'anna@home.org', 'childAge': 7}
```


