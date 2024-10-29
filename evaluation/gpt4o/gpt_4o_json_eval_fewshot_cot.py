import openai
from openai import OpenAI
import base64
import os
import random
import json
import numpy as np

OPENAI_API_KEY = 'your_api_key'
openai.api_key = OPENAI_API_KEY

# client = OpenAI()
def image_encoding(path):
    with open(path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')
    return f"data:image/jpeg;base64,{base64_image}"

def load_prompt(file):
    prompt = ''
    with open(file, encoding="utf8") as f:
        for line in f:
            prompt = prompt + line.strip() + '\n'
    return prompt


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

for trial in range(1, 11):
    data = {}

    folder = f'.\\DynaMath\\samples and result\\10trials2.0\\trial{trial}\\'


    with open(f'{folder}dataset.json') as file:
        json_dict = json.load(file)

    for i in range(1, 502):
        print(f"working on trial {trial} problem {i}")
        temp = i
        text = "## Question\n" + json_dict.get(f"{temp}").get('question')
        if json_dict.get(f"{temp}").get("answer_type") == "float":
            text = text + "Please answer in a floating-point number."

        new_problem = "Now please answer the following question based on the last image:" + text
        subject = json_dict.get(f"{temp}").get('subject')

        txt_files = [file for file in os.listdir(f".\\DynaMath\\demonstrations\\{subject}\\text") if file.endswith('.txt')]
        file_index = random.sample(range(1, 6), 3)
        demonstrations = "" 
        img_index = 1
        for i in file_index:
            demo = f"example{i}.txt"
            demo_content = load_prompt(os.path.join(f".\\DynaMath\\demonstrations\\{subject}\\text", demo))
            demonstrations += f"For image {img_index}: " + demo_content + "\n\n"
            img_index += 1
        problem_statement = "Please answer the question based on the last image. To clearly explain the task, we provide the following example:\n\n" + demonstrations + new_problem + guide + text_example

        image_path1 = f".\\DynaMath\\demonstrations\\{subject}\\images\\example{file_index[0]}.png"
        image_path2 = f".\\DynaMath\\demonstrations\\{subject}\\images\\example{file_index[1]}.png"
        image_path3 = f".\\DynaMath\\demonstrations\\{subject}\\images\\example{file_index[2]}.png"
        image_path4 = f"{folder}image\\image{temp}.png"

        response = openai.chat.completions.create(
          model="gpt-4o-2024-08-06",
          messages=[
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": problem_statement,
                },
                {
                  "type": "image_url",
                  "image_url": {
                    "url": image_encoding(image_path1),
                  },
                },
                {
                  "type": "image_url",
                  "image_url": {
                    "url": image_encoding(image_path2),
                  },
                },
                {
                  "type": "image_url",
                  "image_url": {
                    "url": image_encoding(image_path3),
                  },
                },
                {
                  "type": "image_url",
                  "image_url": {
                    "url": image_encoding(image_path4),
                  },
                },
              ],
            }
          ],
          response_format={"type": "json_object"},
          temperature=0
        )
        description = response.choices[0].message.content
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
                if abs(diff) <= 0.05:
                    temp_data["result"] = "correct"
                else:
                    temp_data["result"] = "fail"
            elif json_dict.get(f"{temp}").get('answer_type') == "multiple choice":
                if len(answer) == 1:
                    if answer == temp_data.get("Ground truth"):
                        temp_data["result"] = "correct"
                    else:
                        temp_data["result"] = "fail"
                else:
                    if temp_data.get("Ground truth") in answer[0:3]:
                        temp_data["result"] = "correct"
                    else:
                        temp_data["result"] = "fail"
            else:
                if temp_data.get("Ground truth") in answer:
                    temp_data["result"] = "correct"
                else:
                    temp_data["result"] = "fail"
        except:
            temp_data["result"] = "fail"

        # data[f"{i}"] = temp_data

        data[f"{temp}"] = temp_data


        with open(f'{folder}report_4o_fewshot_cot.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
