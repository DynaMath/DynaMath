import base64
import os
import json
from dataclasses import dataclass, field

import numpy as np
import openai
from openai import OpenAI

OPENAI_API_KEY = 'xx'

client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="http://0.0.0.0:23333/v1"
)
model_name = client.models.list().data[0].id
print(model_name)


def image_encoding(path):
    with open(path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')
    return f"data:image/jpeg;base64,{base64_image}"


def preprocess(str1):
    str0 = str1
    if str0 == "":
        return str1
    while str0[0] != "{":
        str0 = str0[1:]
        if len(str0) == 1:
            return str1
    while str0[-1] != "}":
        str0 = str0[:-1]
        if len(str0) == 1:
            return str1
    str2 = str0.replace("\\", "")
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
## Answer Instruction Please provide an answer to the question outlined above. Your response should adhere 
to the following JSON format, which includes two keys: 'solution' and 'short answer'. The 'solution' key can contain 
detailed steps needed to solve the question, and the 'short answer' key should provide a concise response. If the problem is a multiple choice problem, just provide the corresponing choice option, 
such as 'A', 'B', 'C', or 'D'. If the answer is a numerical value, format it as a three-digit floating-point number.

Example of expected JSON response format:

"""

example = {
    "solution": "[Detailed step-by-step explanation]",
    "short answer": "[Concise Answer]"
}
text_example = json.dumps(example, indent=4)

prefix = model_name.split('models--')[1].split('/')[0]
# result path for continue test
# with open('xxxxx') as dat_file:
# data = json.load(dat_file)
path = os.path.join(os.path.dirname(os.getcwd()), "dataset")
data = {}
count = 0

with open(f'{path}/dataset.json') as file:  # dataset path
    json_dict = json.load(file)

for i in range(1, 502):
    temp = i
    text = "## Question\n" + json_dict.get(f"{temp}").get('question')
    if json_dict.get(f"{temp}").get("answer_type") == "float":
        text = text + "Please answer in a floating-point number."
    text = "<IMAGE_TOKEN>" + text + guide + text_example
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": [
                {"type": "text", "text": text},
                {"type": "image_url", "image_url": {"url": image_encoding(f"{path}/image/image{temp}.png")}}]  # image path
             }
        ]
    )
    import pdb;

    try:
        description = preprocess(response.choices[0].message.content)
    except:
        description = response.choices[0].message.content
    try:
        dj = json.loads(description, strict=False)
    except:
        dj = {
            "solution": description,
            "short answer": description.split('\n')[-1][:-1]
        }
    temp_data = {"question": json_dict.get(f"{temp}").get('question'),
                 "subject": json_dict.get(f"{temp}").get('subject'),
                 "knowledge level": json_dict.get(f"{temp}").get('level'),
                 "Ground truth": json_dict.get(f"{temp}").get('answer'),
                 "image": f"image/image{i}.png",
                 "response": dj}
    try:
        answer = str(dj.get("short answer"))
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

    data[f"{i}"] = temp_data
    json_data = json.dumps(data, indent=4)
    prefix = model_name.split('models--')[1].split('/')[0]
    with open(f"{path}"prefix + "report", 'w') as json_file:  # result path
        json_file.write(json_data)
