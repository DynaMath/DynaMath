# DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models
![Dynamic Benchmark](https://img.shields.io/badge/Task-Dynamic_Benchmark-red) 
![MathQA](https://img.shields.io/badge/Task-MathQA-red) 
![Mathematical Reasoning Robustness](https://img.shields.io/badge/Task-Mathematical_Reasoning_Robustness-red) 
![ScienceQA](https://img.shields.io/badge/Dataset-DynaMath-blue)  
![GPT-4o](https://img.shields.io/badge/Model-GPT--4o-green) 
![Claude-3.5](https://img.shields.io/badge/Model-Claude--3.5-green) 
![Gemini-pro-1.5](https://img.shields.io/badge/Model-Gemini_Pro_1.5-green)
![Qwen2-VL](https://img.shields.io/badge/Model-Qwen2--VL-green)
![InternVL2](https://img.shields.io/badge/Model-InternVL2-green)
![Llama-3.2](https://img.shields.io/badge/Model-Llama--3.2-green)
![Deepseek-VL](https://img.shields.io/badge/Model-Deepseek--VL-green)
![Llava](https://img.shields.io/badge/Model-Llava-green)



<p align="center">
<a href=""><img src="assets/dyna-logo.png" alt="DynaMath logo." width="150px"></a>
</p>

<p align="center">
<a href="README.md"><img src="https://img.shields.io/badge/document-English-blue.svg" alt="EN doc"></a>
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
<a href="https://huggingface.co/DynaMath" target="_blank"><img alt="Hugging Face" src="https://img.shields.io/badge/%F0%9F%A4%97%20-Hugging%20Face-blue?color=blue&logoColor=white" /></a>
</p>


Welcome to the official repository for **DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision-Language Models**. This repository contains the code, resources, and documentation supporting our paper, which introduces DynaMath: a benchmark designed to rigorously evaluate mathematical reasoning across various vision-language models (VLMs).

For further details, including the benchmark leaderboard, please visit our [project website](https://dynamath.github.io) and our [preprint paper](https://arxiv.org/abs/2411.00836).

## 🌟 About DynaMath

The rapid advancements in Vision-Language Models (VLMs) have shown significant potential in tackling mathematical reasoning tasks that involve visual context. However, unlike humans who can reliably apply solution steps to similar problems with minor modifications, state-of-the-art VLMs such as GPT-4o often fail to maintain consistency across such variations, revealing limitations in their mathematical reasoning capabilities.

**DynaMATH** addresses this challenge by providing a **dynamic** visual math benchmark specifically designed to evaluate the **mathematical reasoning robustness** of VLMs. While existing vision-based math benchmarks assess VLMs' problem-solving abilities with static problem sets, they lack the ability to evaluate performance robustness under varying problem conditions.

DynaMATH bridges this gap by introducing a benchmark with 501 high-quality, multi-topic **seed** questions, each represented as a **Python program**. These programs enable automatic generation of a much larger set of **concrete** questions with diverse visual and textual variations, providing a comprehensive testbed for evaluating generalization abilities of VLMs.

<p align="center">
    <img src="assets/DynaMATH_demo.png" width="90%"> <br>
    Figure: Illustration of the dynamic benchmark generation process in DynaMATH.
</p>

We assessed the performance of 14 state-of-the-art VLMs using 5,010 generated concrete questions (10 variations per seed question). The results reveal that the **worst-case model accuracy**, defined as the percentage of correctly answered seed questions across all variations, is significantly lower than the average-case accuracy. Moreover, the analysis shows that model errors on certain variants are not merely due to random chance, but are consistent failures that indicate underlying robustness issues. The findings highlight the need to study the robustness of VLMs' reasoning capabilities. DynaMATH offers valuable insights for developing more reliable models for mathematical reasoning tasks.

## 📊 Benchmark Design

### Dataset Collection

Our benchmark collection consists of two phases: **Seed Question Collection** and **Program-based Question Generation**.

#### Seed Question Collection
- Seed questions were selectively curated from existing visual math datasets and publicly available resources.
- We collected:
  - **107 questions** from [MathVista](https://mathvista.github.io/), covering topics like analytic geometry and statistics.
  - **27 questions** from [MATH-V](https://mathvision-cuhk.github.io/), focused on arithmetic, puzzles, and solid geometry.
  - **45 questions** based on scientific figures.
  - **48 questions** on graph theory from the [MMMU](https://mmmu-benchmark.github.io/) dataset.
  - **236 questions** on advanced reasoning topics such as functions and geometry from publicly accessible resources.
  - **38 newly developed questions** covering linear algebra, set theory, and algorithmic flow.

- After eliminating overly complex questions unsuitable for programmatic generation, the final dataset comprises **501 seed questions**:
  - **45.3%** sourced from established visual math datasets.
  - **54.7%** newly collected or developed from public resources.


#### Program-based Question Generation
- Each seed question is transformed into a carefully designed Python program, enabling the generation of diverse concrete questions under randomly sampled conditions.
- **470 programs** include a plotting function for dynamic visual contexts, while **31 programs** use fixed images with randomized text elements.
-This programmatic approach enables the creation of **infinitely many** concrete benchmark questions, facilitating the evaluation of VLMs' reasoning robustness.

**Variant Types in DynaMath**:
1. **Numerical Value Variants**: Modifying numerical quantities to test arithmetic proficiency.
2. **Geometric Transformations**: Changing shapes, angles, and dimensions to assess spatial understanding.
3. **Function Type Variants**: Varying function types (e.g., linear, quadratic) to evaluate generalization.
4. **Color Variants**: Altering colors to test robustness against superficial visual changes.
5. **Symbolic Substitutions**: Modifying symbols to test adaptability to different mathematical representations.
6. **Graph Structure Variants**: Changing graph layouts to evaluate comprehension of relationships.
7. **Real-life Context Variants**: Modifying real-world scenarios (e.g., calendars, time-related problems) to test contextual understanding.

### Dataset Statistics
- **Mathematical Topics**: Covers nine topics including Solid Geometry (SG, 3.0%), Puzzle Tests (PT, 3.4%), Arithmetic (AR, 5.2%), Scientific Figures (SF, 9.0%), Graph Theory (GT, 9.6%), Algebra (AL, 10.2%), Plane Geometry (PG, 15.4%), Analytic Geometry (AG, 19.4%), and Statistics (ST, 25.0%). 
- **Difficulty Levels**: Questions range from elementary to undergraduate level, with a focus on high school (55.3%) and undergraduate (32.1%) levels.
- **Question Types**: Includes 35.5% multiple-choice questions and 64.7% free-form questions.

This diverse collection of variants and topics makes DynaMath a comprehensive benchmark for evaluating the flexibility, robustness, and accuracy of VLMs in solving mathematical problems.



## 📖 Dataset Usage

**(New!)** DynaMath has been integrated into **[VLMEvalKit](https://github.com/open-compass/VLMEvalKit)**, enabling the one-command evaluation. 

### Generating a Version of DynaMath

Follow these steps to generate a version of the DynaMath dataset:

#### Step 1: Build the Docker Image

First, use the provided `Dockerfile` to create a Docker image for the environment:

```bash
docker build -t dynamath .
```

#### Step 2: Run the Docker Container

Next, run the container interactively based on the created image, ensuring you mount the appropriate directories:

```bash
docker run -it -v /home/user/DynaMath:/app dynamath bash
```

#### Step 3: Generate Variant Questions

Once inside the container, navigate to the `dataset_generator` directory and generate the question variants by running:

```bash
cd dataset_generator
xvfb-run -s "-screen 0 640x480x24" python generate_json.py 1 501
```

This will generate a batch of questions starting from index 1 to 501.

> **Note:** The `generate_json.py` script takes four arguments:
> 1. Starting index
> 2. Number of questions to generate from the starting index
> 3. Default random seed
> 4. Default NumPy seed


# Citation
If you find DynaMath helpful for your research, please cite
```
@misc{zou2024dynamathdynamicvisualbenchmark,
      title={DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models}, 
      author={Chengke Zou and Xingang Guo and Rui Yang and Junyu Zhang and Bin Hu and Huan Zhang},
      year={2024},
      eprint={2411.00836},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2411.00836}, 
}
```
