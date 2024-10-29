import inspect
import json
import importlib.util
import os
import random
from pathlib import Path
import sys
import numpy as np
import shutil


def import_all_py_files_from_directory(directory_path):
    directory = Path(directory_path).resolve()
    all_classes = {}
    if not directory.is_dir():
        raise NotADirectoryError(f"{directory} is not a valid directory")

    for file in directory.glob("*.py"):
        module_name = file.stem
        spec = importlib.util.spec_from_file_location(module_name, file)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)

        for class_name in dir(module):
            attr = getattr(module, class_name)
            if isinstance(attr, type):
                all_classes[class_name] = attr
    return all_classes


def generate(start, num, rdseed=0, npseed=0):
    destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
    destination_path = os.path.join(destination_folder, "dataset.json")
    with open(destination_path) as file:
        data1 = json.load(file)
    data = data1

    if start <= 0:
        return "Error: the index cannot be negative"
    elif num <= 0:
        return "Error: the number of questions generated cannot be negative"
    elif start + num > 502:
        return "Error: out of index"
    if rdseed != 0:
        random.seed(rdseed)
    if npseed != 0:
        np.random.seed(npseed)
    for i in range(start, start + num):
        if i < 10:
            question_name = f"Q0{i}"
        else:
            question_name = f"Q{i}"
        print(f"now generate Q{i}")
        question_temp = classes[question_name]()
        question_temp.draw(i)
        if question_temp.answer_type == "float":
            answer = round(question_temp.answer, 4)
        else:
            answer = question_temp.answer
        temp_data = {
            "question": question_temp.query,
            "answer": str(answer),
            "image": f"image/image{i}.png",
            "answer_type": question_temp.answer_type,
            "subject": question_temp.subject,
            "level": question_temp.level
        }
        data[f"{i}"] = temp_data
        

    json_data = json.dumps(data, indent=4)
    with open(destination_path, 'w') as json_file:
        json_file.write(json_data)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        classes = import_all_py_files_from_directory("")
        generate(int(sys.argv[1]), int(sys.argv[2]))
    elif len(sys.argv) == 4:
        classes = import_all_py_files_from_directory("")
        generate(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    elif len(sys.argv) == 5:
        classes = import_all_py_files_from_directory("")
        generate(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))

