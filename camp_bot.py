import openai
import json
openai.api_key = "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"

DET_PROMPT = "Can we assume from the Text that parent whants to sign his/her kid up in the camp, answer only YES or NO?" \
             " Text:"

ENROLL_PREFX = "Ask about full name, phone number, email, and kid's age (validate kid's age). " \
               "Validate phone number and email address. Avoid text like [Your Name], [Insert Camp Phone Number] etc. "


def send_request(context, request):
    messages = [{"role": "system", "content": "You are a helpful and accurate assistant."}]

    for n, msg in enumerate(context):
        if n % 2 == 0:
            role = "user"
        else:
            role = "assistant"
        messages.append({"role": role, "content": msg})
    messages.append({"role": "user", "content": request})

    r = openai.ChatCompletion.create(
        temperature=0.5,
        model="gpt-3.5-turbo", presence_penalty=2.0,
        messages=messages
    )
    return r['choices'][0]['message']['content']


def main_loop(context):
    u_prompt = "How can I help you?"
    enroll_stage = False

    while True:
        request2 = input(u_prompt)
        if request2.strip() == "STOP":
            break

        im_replay = "NO"
        if not enroll_stage:
            im_replay = send_request([], DET_PROMPT + request2)

        if im_replay.upper().replace(".", "").strip() == "YES":
            request2 = ENROLL_PREFX + request2
            u_prompt = "Please provide information (type STOP to end conversation):"
            enroll_stage = True

        gpt_replay = send_request(context=context, request=request2)

        print(gpt_replay)
        context.append(request2)
        context.append(gpt_replay)


if __name__ == '__main__':
    with open("../../workspace/camp_bot/camp_text.txt") as f:
        camp_text = "\n".join(f.readlines())
    request1 = "Using provided text assist parents with the camp. \n" + camp_text

    welcome_text = send_request([], request1)

    print(welcome_text)
    cur_context = [request1, welcome_text]

    main_loop(cur_context)

    summary_request = "Please print parent's full name, phone number, email, and kid's age in json form. " \
                      "Print only json."
    replay = send_request(context=cur_context, request=summary_request)
    #print(replay)
    try:
        data = json.loads(replay)
        print(data)
    except Exception as e:
        print("ERROR: Cant parce response from GPT", e)
