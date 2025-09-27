# DSPy GEPA Demo - Evaluator and Optimizer in DSPy

**Speaker**: Mike Taylor, Leonardo Ubbiali

**Meetup**: London Agentic AI #1 Context Engineering: Building Reliable AI Agents: From Context to Evals

**Topic**: Evaluator-Optimizer Pattern in DSPy with GEPA Optimization, Semantic Layer

## Overview

This demo teaches the **evaluator-optimizer pattern** in DSPy by building a joke-telling AI system that demonstrates how to create, evaluate, and optimize AI programs systematically. The example shows how to build a comedian AI that generates jokes in specific comedian styles and uses an AI judge to evaluate and improve joke quality through evolutionary optimization.


## What's Inside 

This directory contains Mike's original notebook demonstration, which is the **🎯 RECOMMENDED** way to experience this demo. We also provide an optional local version for developers who prefer command-line execution.

### 🎯 **RECOMMENDED: Jupyter Notebook (Primary)**
- `evaluator-optimizer-in-dspy.ipynb` - **⭐ Original Jupyter notebook with full demonstration** (From Mike Taylor)
  - ✅ Interactive step-by-step learning experience
  - ✅ Clear explanations and markdown documentation  
  - ✅ Easy to pause, restart, and explore at your own pace
  - ✅ **Best way to understand DSPy concepts**
  - ✅ Works with OpenAI API (as intended by the speaker)

### 🔧 **OPTIONAL: Python Script (Secondary)**  
- `evaluator_optimizer_dspy.py` - Local Ollama version (converted by Shashi Jagtap)
  - Command-line execution for experienced developers
  - No API keys required (uses local Ollama models)
  - **Alternative for users who prefer local inference**
  - Requires more setup (Ollama installation + models)

### 📦 **Dependencies**
- `requirements.txt` - Project dependencies that can be installed via pip or uv 


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

### 🎯 **For Jupyter Notebook (RECOMMENDED)**

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
   - OpenAI API access (~$1-5 for full demo)
   - Internet connection

### 🔧 **For Python Script (OPTIONAL - Advanced Users)**

Only follow this section if you want to run the local Ollama version instead of the recommended notebook.

1. **Install Ollama**:
   ```bash
   # On macOS
   brew install ollama
   
   # On Linux  
   curl -fsSL https://ollama.ai/install.sh | sh
   ```

2. **Pull required models**:
   ```bash
   ollama pull llama3.1:8b        # Recommended for optimization
   # OR for lower RAM systems:
   ollama pull llama3.2:1b        # Lightweight but less capable
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **System Requirements**:
   - Python 3.8+
   - **16GB+ RAM recommended** (for GEPA optimization)
   - Local compute (no internet required for inference)

## Running the Demo

### 🎯 **RECOMMENDED: Jupyter Notebook (START HERE!)**

**This is the best way to learn DSPy concepts:**

```bash
jupyter notebook evaluator-optimizer-in-dspy.ipynb
```

**Why the notebook is recommended:**
- ✅ **Interactive learning**: Step-by-step with explanations
- ✅ **Easy to pause/resume**: Stop at any cell, restart later  
- ✅ **Visual outputs**: See results and plots inline
- ✅ **Original experience**: Exactly as Mike presented it
- ✅ **Cost effective**: Uses OpenAI API efficiently (~$1-5 total)

**Getting started:**
1. Open the notebook in Jupyter
2. Run cells sequentially from top to bottom
3. Read the markdown explanations between code cells
4. Experiment with parameters if you want

---

### 🔧 **OPTIONAL: Python Script (Local Ollama)**

**Only use this if you specifically need local inference and has resource to run optimization:**

```bash
python evaluator_optimizer_dspy.py
```

**⚠️ Important considerations for the Python script:**
- Requires significant RAM (16GB+ recommended)
- Takes longer to run than OpenAI version  
- More complex setup (Ollama + models)
- **Intended for advanced users only**
- May cause system slowdown on lower-end machines

**When to use the Python script:**
- You cannot use OpenAI API
- You need completely offline operation  
- You're experienced with local LLM setup
- You have sufficient hardware resources

**🔧 Customizing Models for Better Results:**

The script uses `llama3.2:1b` as student and `llama3.1:8b` as teacher by default, but you can modify it to use larger models for better optimization results:

1. **Edit the Python script** (`evaluator_optimizer_dspy.py`) and change the model names in the `setup_environment()` function:

```python
# For better results, replace with larger models for teacher and/or student LM:
student_lm = dspy.LM(
    model="ollama_chat/qwen3:8b",     
    # model="ollama_chat/llama3.1:8b",  # or llama3.1:70b
    # model="ollama_chat/gpt-oss:20b",  # or gpt-oss:120b (if your machine supports)
    api_key="",
    max_tokens=4000,
    temperature=1.0
)
```

⚠️ **IMPORTANT WARNING: DSPy Optimization Intensity**

DSPy optimizers (like GEPA) make **hundreds of LLM calls** during optimization. This is computationally intensive and can:
- Consume significant system resources
- Cause system slowdown or crashes on low-end machines
- **Do NOT attempt this on low-end or resource-constrained systems**

**Model Recommendations by System for Optimization:**
- **16GB RAM**: less than 7b models 
- **32GB RAM**: Over 8b
- **64GB+ RAM**: over 20b 


## Demo Workflow

1. **Environment Setup**: Configure DSPy with OpenAI models
2. **Program Creation**: Build the comedian joke generator
3. **Dataset Preparation**: Create examples of funny vs unfunny jokes
4. **Judge Development**: Implement AI-based joke evaluation
5. **Optimization**: Use GEPA to improve both comedian and judge
6. **Evaluation**: Measure and compare performance improvements
7. **Analysis**: Examine optimized prompts and learned behaviors


## Contact

Mike Taylor or Shashi Jagtap 
For questions about this demo or DSPy implementation details, please create an issue in this repository.

## License

This demo is shared for educational purposes within the London Agentic AI community.