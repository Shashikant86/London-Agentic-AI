# DSPy GEPA Demo - Evaluator and Optimizer in DSPy

**Speaker**: Mike Taylor

**Meetup**: London Agentic AI #1 Context Engineering: Building Reliable AI Agents: From Context to Evals

**Topic**: Evaluator-Optimizer Pattern in DSPy with GEPA Optimization, Semantic Layer

## Overview

This demo teaches the **evaluator-optimizer pattern** in DSPy by building a joke-telling AI system that demonstrates how to create, evaluate, and optimize AI programs systematically. The example shows how to build a comedian AI that generates jokes in specific comedian styles and uses an AI judge to evaluate and improve joke quality through evolutionary optimization.

## What's Inside 

This directory contains Mike's **original Jupyter notebook demonstration**, which is the **primary and recommended** way to experience this demo.

### 🎯 **Jupyter Notebook **
- `evaluator-optimizer-in-dspy.ipynb` - **⭐ Original Jupyter notebook with full demonstration** (From Mike Taylor)
  - ✅ Interactive step-by-step learning experience
  - ✅ Clear explanations and markdown documentation  
  - ✅ Easy to pause, restart, and explore at your own pace
  - ✅ **Best way to understand DSPy concepts**
  - ✅ Works with OpenAI API (as intended by the speaker)
  - ✅ **Cost effective**: Uses OpenAI API efficiently



## What You'll Learn

### Core DSPy Concepts Demonstrated

1. **Signatures and Predictors**: Creating custom input/output specifications for AI programs
2. **GEPA Optimizer**: Using evolutionary algorithms for prompt optimization
3. **LLM-as-a-Judge**: Implementing AI-based evaluation metrics
4. **Evaluation Framework**: Building systematic performance measurement systems

### Key Technical Components

- **Comedian Program**: Generates jokes in specific comedian styles (Ricky Gervais, Billy Connolly, etc.)
- **AI Judge**: Evaluates joke quality using LLM as Judge
- **GEPA Evolutionary Optimizer**: Automatically improves both comedian and judge performance
- **Dataset Creation**: Building training datasets with funny vs unfunny jokes
- **Performance Evaluation**: Measuring and comparing system improvements

## Prerequisites

### 🎯 **For Jupyter Notebook**

1. **Jupyter Notebook**: Supported packages or IDE to run the notebook.

2. **Get OpenAI API Key**:
   - Sign up at [OpenAI](https://platform.openai.com/)
   - Create API key from your dashboard
   - Create a `.env` file in this directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   **IMPORTANT**: Keep the `.env` file safe and do not commit this file to version control.

3. **System Requirements**:
   - Python 3.8+
   - OpenAI API access
   - Internet connection

## Running the Demo

### 🎯 **Jupyter Notebook (START HERE!)**

**This is the recommended way to learn DSPy concepts:**

```bash
pip install -r requirements.txt
jupyter notebook evaluator-optimizer-in-dspy.ipynb
```

**Notebook Features:**
- ✅ **Interactive learning**: Step-by-step with explanations
- ✅ **Easy to pause/resume**: Stop at any cell, restart later  
- ✅ **Visual outputs**: See results and plots inline
- ✅ **Original experience**: Exactly as Mike presented it
- ✅ **Cost effective**: Uses OpenAI API efficiently (~$1-5 total)
- ✅ **No local setup required**: Just need OpenAI API key

**Getting started:**
1. Get Jupyter notebook friedly packages or Colab
2. Set up your OpenAI API key in `.env` file
3. Open the notebook in Jupyter
4. Run cells sequentially from top to bottom
5. Read the markdown explanations between code cells
6. Experiment with parameters if you want

## Demo Workflow

1. **Environment Setup**: Configure DSPy with OpenAI models
2. **Program Creation**: Build the comedian joke generator
3. **Dataset Preparation**: Create examples of funny vs unfunny jokes
4. **Judge Development**: Implement AI-based joke evaluation
5. **Optimization**: Use GEPA to improve both comedian and judge
6. **Evaluation**: Measure and compare performance improvements
7. **Analysis**: Examine optimized prompts and learned behaviors

## Alternative: Local Ollama Version

If you prefer to run everything locally without API calls, check out the `local_gepa_experiment/` directory which contains:
- A Python script version of this demo
- Instructions for running with local Ollama models
- **Note**: Requires significant computational resources and setup

## Contact

Mike Taylor
For questions about this demo or DSPy implementation details, please create an issue in this repository.

## License

This demo is shared for educational purposes within the London Agentic AI community.