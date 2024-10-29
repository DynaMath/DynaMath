import base64
import os
import json

import numpy as np
import time
import openai
from openai import OpenAI
import anthropic
import re
from anthropic import Anthropic


from PIL import Image
from io import BytesIO

def convert_and_encode_image(jpeg_path):
    # Open JPEG and convert to PNG
    with Image.open(jpeg_path) as img:
        # Create a BytesIO object to hold the PNG data
        png_buffer = BytesIO()
        # Save as PNG to the buffer
        img.save(png_buffer, format='PNG')
        # Get the PNG data and encode to base64
        png_data = png_buffer.getvalue()
        return base64.b64encode(png_data).decode('utf-8')

# def image_encoding(filepath):
#     with open(filepath, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#         return encoded_string.decode('utf-8')

def preprocess(str1):
    while str1[0] != "{":
        str1 = str1[1:]
    while str1[-1] != "}":
        str1 = str1[:-1]
    str2 = str1.replace("\\", "")
    str2 = str2.replace("\\n", "\n")
    return str2



def extract_json(response):
    # Find the start and end of the JSON object
    json_start = response.find("{")
    json_end = response.rfind("}")
    
    if json_start == -1 or json_end == -1:
        raise ValueError("No valid JSON object found in the response")
    
    # Extract the JSON substring
    json_str = response[json_start:json_end + 1]
    
    # Remove any invalid control characters
    json_str = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', json_str)
    
    # Parse the cleaned JSON string
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {str(e)}")
        print(f"Problematic JSON string: {json_str}")
        raise


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
client = Anthropic(api_key="your_api_key")
image_media_type = "image/png"
start = time.time()

for trial in range(1, 11):
    data = {}
    count = 0
    # folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")

    folder = f'.\\DynaMath\\samples and result\\10trials\\trial{trial}\\'


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
        image_data = convert_and_encode_image(image_path)

        # message = f"{text}\n\n[Image](data:image/jpeg;base64,{image_encoding(image_path)})"

        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=8192,
            temperature = 0.0,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": image_media_type,
                                "data": image_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": text
                        }
                    ],
                }
            ],
        ).content[0].text
        try:
            dj = extract_json(message)
            print("Successfully extracted JSON")
        except Exception as e:
            dj = {
                "solution": message,
                "short answer": "wait for check"
            }
            print(f"Error extracting JSON: {str(e)}")

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

        data[f"{i}"] = temp_data


        data[f"{temp}"] = temp_data


        with open(f'{folder}report_claude.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

end = time.time()

print(f"The running time is {end-start}")
