import base64
import os
import json

import numpy as np
import time
import openai
from openai import OpenAI

OPENAI_API_KEY = 'your_api_key'
openai.api_key = OPENAI_API_KEY




def image_encoding(path):
    with open(path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')
    return f"data:image/jpeg;base64,{base64_image}"


def preprocess(str1):
    while str1[0] != "{":
        str1 = str1[1:]
    while str1[-1] != "}":
        str1 = str1[:-1]
    str2 = str1.replace("\\", "")
    str2 = str2.replace("\\n", "\n")
    return str2


def transfer(str1):
    if "\u03c0" in str1:
        strs = str1.split('\u03c0')
        str1 = strs[0]
        return float(str1) * np.pi
    else:
        return float(str1)


guide = """
### Response Format
Answer Instruction Please provide an answer to the question outlined above. Your response should adhere to the following JSON format, which includes two keys: 'solution' and 'short answer'. 
# The 'solution' key can contain reasoning steps needed to solve the question.
# The 'short answer' key should only provide a concise response. If the problem is a multiple choice problem, just provide the corresponing choice option, 
such as 'A', 'B', 'C', or 'D'. If the answer is a numerical value, format it as a three-digit floating-point number.  

Example of expected JSON response format:

"""

example = {
    "solution": "[Detailed step-by-step explanation]",
    "short answer": "[Concise Answer]"
}
text_example = json.dumps(example, indent=4)

data = {}
count = 0

start = time.time()

for self_consist in range(1, 2):

    for trial in range(1, 11):
        data = {}
        count = 0
        # folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        folder = f'c:\\Users\\xingang\\Desktop\\DynaMATH_develop\\samples and result\\10trials2.0\\trial{trial}\\'

        with open(f'{folder}dataset.json') as file:
            json_dict = json.load(file)

        for i in range(1, 502):
            print(f"working on trial {trial} problem {i}")
            temp = i
            text = "## Question\n" + json_dict.get(f"{temp}").get('question')
            if json_dict.get(f"{temp}").get("answer_type") == "float":
                text = text + "Please answer in a floating-point number."
            text = text + guide + text_example
            image_path = f"{folder}image/image{temp}.png"
            response = openai.chat.completions.create(
                model="gpt-4o-2024-08-06",
                messages=[
                    {"role": "user", "content": [
                        {"type": "text", "text": text},
                        {"type": "image_url", "image_url": {"url": image_encoding(image_path)}}]
                    }
                ],
                response_format={"type": "json_object"},
                temperature=0
            )
            # description = preprocess(response.choices[0].message.content)
            description = response.choices[0].message.content
            # print(description)
            try:
                # dj = json.loads(description, strict=False)
                dj = json.loads(description)
            except:
                dj = {
                    "solution": description,
                    "short answer": "wait for check"
                }
            temp_data = {"question": json_dict.get(f"{temp}").get('question'),
                        "subject": json_dict.get(f"{temp}").get('subject'),
                        "knowledge level": json_dict.get(f"{temp}").get('level'),
                        "Ground truth": json_dict.get(f"{temp}").get('answer'),
                        "image": f"image/image{i}.png",
                        "response": dj}
            answer = str(dj.get("short answer"))
            try:
                if json_dict.get(f"{temp}").get('answer_type') == "float":
                    if not answer.isdigit():
                        parts = answer.split(' ')
                        answer = parts[0]
                        answer = transfer(answer)
                    diff = float(answer) - float(temp_data.get("Ground truth"))
                    if abs(diff) <= 0.001:
                        temp_data["result"] = "correct"
                        count += 1
                    else:
                        temp_data["result"] = "fail"
                elif json_dict.get(f"{temp}").get('answer_type') == "multiple choice":
                    if len(answer) == 1:
                        if answer == temp_data.get("Ground truth"):
                            temp_data["result"] = "correct"
                            count += 1
                        else:
                            temp_data["result"] = "fail"
                    else:
                        if temp_data.get("Ground truth") in answer[0:3]:
                            temp_data["result"] = "correct"
                            count += 1
                        else:
                            temp_data["result"] = "fail"
                else:
                    if temp_data.get("Ground truth") in answer:
                        temp_data["result"] = "correct"
                        count += 1
                    else:
                        temp_data["result"] = "fail"
            except:
                temp_data["result"] = "fail"

            # data[f"{i}"] = temp_data

        # data["score"] = str(count)
        # json_data = json.dumps(data, indent=4)
        # with open('./10trials/trial1/report.json', 'w') as json_file:
        #     json_file.write(json_data)

            data[f"{temp}"] = temp_data


            with open(f'{folder}report_4o_{self_consist+1}.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
