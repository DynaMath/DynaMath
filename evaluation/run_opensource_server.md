# Opensource Server
### Step0: Preparation

Install lmdeploy.
When running models, please install corresponding dependencies if needed.

```
conda create -n lmdeploy python=3.8 -y
conda activate lmdeploy
pip install lmdeploy
```

```



### Step 1: Run the following example to start the server

```
bash start_opensource_server.sh --model_name liuhaotian/llava-v1.5-7b
```

### Step 2: Run evaluation code 

```
python opensource_json_eval.py
```


## Supported Models

```
liuhaotian/llava-v1.5-7b 
liuhaotian/Llava-v1.6-vicuna-7b 
liuhaotian/llava-v1.6-vicuna-13b 
liuhaotian/llava-v1.6-34b 
llava-hf/llama3-llava-next-8b-hf 

deepseek-ai/deepseek-vl-7b-chat 

Qwen/Qwen-VL-Chat 

internlm/internlm-xcomposer2d5-7b 
InternVL1.5-Chat 
OpenGVLab/InternVL2-8B 
OpenGVLab/InternVL2-26B 
OpenGVLab/InternVL2-40B 
OpenGVLab/InternVL2-Llama3-76B 
```