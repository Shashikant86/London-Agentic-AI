# DSPy GEPA Demo - Local Ollama Experiment

**Local Version by**: Shashi Jagtap (Based on Mike Taylor's original notebook)


**Meetup**: London Agentic AI #1 Context Engineering: Building Reliable AI Agents: From Context to Evals

## Note

This is an **experimental local version** for advanced users who prefer offline operation. For the **recommended learning experience**, please use the original Jupyter notebook in the parent directory which uses OpenAI API and provides interactive step-by-step learning. This script tested locally with `llama3.1:8b, qwen3:8b, gpt-oss:20b, gpt-oss:120b` models.  

## Overview

This directory contains a **Python script version** of Mike Taylor's DSPy GEPA demonstration, converted to run entirely on local Ollama models. This version demonstrates the evaluator-optimizer pattern using local inference without requiring API keys.

## What's Inside 

### 🔧 **Local Ollama Implementation**
- `evaluator_optimizer_dspy.py` - **Local Python script** (converted by Shashi Jagtap)
  - ✅ No API keys required (uses local Ollama models)
  - ✅ Complete offline operation
  - ✅ Works with various Ollama models
  - ⚠️ Requires significant computational resources
  - ⚠️ More complex setup than the original notebook

### 📚 **Reference Materials**
- `evaluator-optimizer-in-dspy.ipynb` - **Original notebook for reference**
- `requirements.txt` - Python dependencies

## Prerequisites

### 🔧 **System Requirements**
- **Python 3.8+**
- **16GB+ RAM recommended** (for GEPA optimization with larger models)
- **64GB+ RAM recommended** (for optimal performance with 20B+ models)
- Local compute power (no internet required for inference)

### 🦙 **Ollama Setup**

1. **Install Ollama**:
   ```bash
   # On macOS
   brew install ollama
   
   # On Linux  
   curl -fsSL https://ollama.ai/install.sh | sh
   
   # Start Ollama service
   ollama serve
   ```

2. **Pull required models**:
   ```bash
   # Default models (works on most systems with 16GB+ RAM)
   ollama pull llama3.2:1b        # Default student model
   ollama pull llama3.1:8b        # Default teacher model
   
   # Optional: Larger models for better performance
   ollama pull qwen3:8b           # Alternative teacher
   ollama pull gpt-oss:20b        # High-performance student (32GB+ RAM)
   ollama pull gpt-oss:120b       # High-performance teacher (64GB+ RAM)
   ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Model Configuration

The script defaults to `llama3.2:1b` (student) and `llama3.1:8b` (teacher) for broad compatibility. You can easily change models using command-line arguments:

### 🚀 **Quick Start (Default Models)**
```bash
# Uses llama3.2:1b (student) and llama3.1:8b (teacher)
python evaluator_optimizer_dspy.py
```

### 🔧 **Custom Model Selection**
```bash
# Medium performance models
python evaluator_optimizer_dspy.py --student llama3.1:8b --teacher qwen3:8b

# High performance models (requires 64GB+ RAM)
python evaluator_optimizer_dspy.py --student gpt-oss:20b --teacher gpt-oss:120b

# List available models
python evaluator_optimizer_dspy.py --list-models
```

### 📋 **Command Line Options**
```bash
python evaluator_optimizer_dspy.py --help
```

Options:
- `--student MODEL`: Student model name (default: llama3.2:1b)
- `--teacher MODEL`: Teacher model name (default: llama3.1:8b)  
- `--list-models`: Show available Ollama models
- `--help`: Show help message with examples

### 🎯 **Model Recommendations by System**

| System RAM | Student Model | Teacher Model | Performance |
|------------|---------------|---------------|-------------|
| 16GB       | `llama3.2:1b` | `llama3.1:8b` | Basic functionality |
| 32GB       | `llama3.1:8b` | `qwen3:8b`    | Good results |
| 64GB+      | `gpt-oss:20b` | `gpt-oss:120b`| Optimal results |

## Running the Demo

### 🚀 **Local Ollama Execution**

```bash
# Navigate to this directory
cd local_gepa_experiment

# Quick start with default models (recommended for most users)
python evaluator_optimizer_dspy.py

# Or customize models for your system
python evaluator_optimizer_dspy.py --student llama3.1:8b --teacher qwen3:8b
```

### 📊 **What to Expect**

The script will run through these stages:
1. **Environment Setup**: Configure DSPy with local Ollama models
2. **Dataset Creation**: Build training datasets with joke examples
3. **Program Creation**: Create comedian joke generator and audience judge
4. **Baseline Evaluation**: Test initial performance
5. **Few-shot Learning**: Add examples to improve performance  
6. **GEPA Optimization**: Use evolutionary optimization to improve prompts
7. **Final Evaluation**: Compare optimized vs baseline performance

### ⏱️ **Runtime Expectations**

This is approximate and varies based on the machine to machine 

- **With lightweight models (1B-8B)**: Less than 10 minutes
- **With medium models (8B-20B)**: Less than 0 minutes  
- **With large models (20B+)**: More than 30 min 

## ⚠️ Important Warnings

### 🔥 **Resource Intensity**
DSPy optimizers (like GEPA) make **hundreds of LLM calls** during optimization. This can:
- Consume significant system resources
- Cause system slowdown or thermal throttling
- Take much longer than the original OpenAI version
- **Do NOT attempt this on low-end or resource-constrained systems**

### 🛠️ **Troubleshooting**

If you encounter issues:
1. **"Too many open files"**: Reduce thread count in the script (already set to 1)
2. **Out of memory**: Use smaller models or reduce batch sizes
3. **Slow performance**: Use fewer optimization iterations or smaller models
4. **Connection errors**: Ensure Ollama is running (`ollama serve`)

## Technical Differences from Original

This local version includes several optimizations for local execution:
- ✅ Reduced thread count to prevent file descriptor issues
- ✅ Disabled caching to avoid SQLite conflicts  
- ✅ Added error handling with fallbacks
- ✅ Configurable model selection
- ✅ Resource-aware defaults

## When to Use This Version

**Use the local version when:**
- ❌ You cannot use OpenAI API
- ✅ You need completely offline operation
- ✅ You're experienced with local LLM setup  
- ✅ You have sufficient hardware resources (16GB+ RAM)
- ✅ You want to experiment with different models

**Use the original notebook when:**
- ✅ You want to learn DSPy concepts interactively
- ✅ You prefer step-by-step explanations
- ✅ You want faster execution and better results
- ✅ You don't mind using OpenAI API (~$1-5 cost)

## Demo Workflow

1. **Environment Setup**: Configure DSPy with local Ollama models
2. **Program Creation**: Build the comedian joke generator
3. **Dataset Preparation**: Create examples of funny vs unfunny jokes
4. **Judge Development**: Implement AI-based joke evaluation
5. **Optimization**: Use GEPA to improve both comedian and judge with local models
6. **Evaluation**: Measure and compare performance improvements
7. **Analysis**: Examine optimized prompts and learned behaviors



## Contact

Shashi Jagtap (Local conversion) or Mike Taylor (Original notebook design)
For questions about this local implementation or DSPy concepts, please create an issue in the repository.

## License

This demo is shared for educational purposes within the London Agentic AI community.