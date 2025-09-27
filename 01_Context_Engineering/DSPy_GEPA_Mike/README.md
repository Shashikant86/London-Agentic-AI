# DSPy GEPA Demo - Evaluator and Optimizer in DSPy

**Speaker**: Mike Taylor, Leonardo Ubbiali
**Meetup**: London Agentic AI #1 Context Engineering: Building Reliable AI Agents: From Context to Evals
**Topic**: Evaluator-Optimizer Pattern in DSPy, Semantic Layer

## Overview

This demo teaches the **evaluator-optimizer pattern** in DSPy by building a joke-telling AI system that demonstrates how to create, evaluate, and optimize AI programs systematically. The example shows how to build a comedian AI that generates jokes in specific comedian styles and uses an AI judge to evaluate and improve joke quality through evolutionary optimization.


## Whats inside 

This directory has the original notebook from the Mike as well as re-writen version for the developers who want to try the Python script directly. 

- `evaluator-optimizer-in-dspy.ipynb` - Original Jupyter notebook with full demonstration (From Mike Taylor)
- `evaluator_optimizer_dspy.py` - Converted Python script by Shashi  (runnable version for developers locally)
- `requirement.txt` - Project dependencies can be installed via pip or uv 


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


### Environment Setup

#### Option 1: OpenAI (Original Notebook by Mike)

Create a `.env` file in this directory with: KEEP `.env` file safe and do not commit this file

```env
OPENAI_API_KEY=your_openai_api_key_here
```

#### Option 2: Ollama (Local, No API Key Required)

**🏠 Local Version Available**: The Python script uses **Ollama** for completely local inference - no API keys or internet required!

2. **Install Ollama & Pull required models**:

Install [Ollama](https://ollama.com) and get some models locally. This is an example but you need advanced model for optimization
   ```bash
   ollama pull llama3.2:1b        # Lightweight model
   # or
   ollama pull llama3.1:8b        # Standard model (needs more RAM)
   ```

Create virtualenv and install dependencies. 

```bash
pip install -r requirements.txt
```


#### For OpenAI (Original & Recommended)
- Python 3.8+
- OpenAI API access
- Internet connection for API calls


#### For Ollama (Local for developers)
- Python 3.8+
- **RAM Requirements**:
  - **Minimum**: 16GB RAM (basic functionality only)
  - **Optimal**: 16GB+ RAM (for smooth GEPA optimization)
- Local compute (no internet required for inference)

## Running the Demo

```bash
# Run complete demo with full optimization
python evaluator_optimizer_dspy.py  # Full GEPA optimization experience

```
### ⚠️ **Performance Warnings**
- **RAM Requirements**: Minimum 16GB RAM recommended
- **Optimization Warning**: GEPA optimization is computationally intensive and may take significant time on slower machines
- **Low RAM Warning**: Do not run full optimization on machines with less than 8GB RAM - it may cause system slowdown or crashes



# DEMO Option 1: Jupyter Notebook (Recommended)

**Original OpenAI Version:**
```bash
jupyter notebook evaluator-optimizer-in-dspy.ipynb
```

**Advantage**: You can stop at any point if your system becomes slow. Run cells sequentially to see the step-by-step demonstration.

# DEMO Option 2: Python Script (Ollama Local Version)

```bash
python evaluator_optimizer_dspy.py
```

**Warning**: This runs the full optimization pipeline which can be resource-intensive on low RAM systems. it allows users to run optimization locally. 

## Demo Workflow

1. **Environment Setup**: Configure DSPy with OpenAI models
2. **Program Creation**: Build the comedian joke generator
3. **Dataset Preparation**: Create examples of funny vs unfunny jokes
4. **Judge Development**: Implement AI-based joke evaluation
5. **Optimization**: Use GEPA to improve both comedian and judge
6. **Evaluation**: Measure and compare performance improvements
7. **Analysis**: Examine optimized prompts and learned behaviors


## Contact

**Speaker**: Mike Taylor, Shashi Jagtap
For questions about this demo or DSPy implementation details, please create an issue in this repository.

## License

This demo is shared for educational purposes within the London Agentic AI community.