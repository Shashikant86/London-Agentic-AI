# DSPy GEPA Local Benchmarks

Benchmarking results for DSPy GEPA optimizer with local Ollama models.

## Test Environment

- **Date**: September 27, 2025
- **Hardware**: Apple M4 Max MacBook Pro, 128GB RAM
- **System**: macOS Darwin 24.2.0
- **Ollama**: Latest stable version
- **DSPy**: Latest stable version

## Model Configurations

| Configuration | Student Model | Teacher Model | Command |
|---------------|---------------|---------------|---------|
| **Lightweight** | llama3.2:1b (1.3B) | llama3.1:8b (8B) | `python evaluator_optimizer_dspy.py` |
| **Medium** | llama3.1:8b (8B) | qwen3:8b (8B) | `python evaluator_optimizer_dspy.py --student llama3.1:8b --teacher qwen3:8b` |
| **High-Performance** | gpt-oss:20b (20B) | gpt-oss:120b (120B) | `python evaluator_optimizer_dspy.py --student gpt-oss:20b --teacher gpt-oss:120b` |

## Performance Results

### Audience Judge Optimization

| Configuration | Baseline | GEPA Optimized | Improvement |
|---------------|----------|----------------|-------------|
| **Lightweight** | 27.78% | **55.56%** | **+100%** |
| **Medium** | 44.44% | **44.44%** | **No change** |
| **High-Performance** | 27.78% | **72.22%** | **+160%** |

### Comedian Performance

| Configuration | Baseline | GEPA Optimized | Improvement |
|---------------|----------|----------------|-------------|
| **Lightweight** | 100.0% | **100.0%** | Stable |
| **Medium** | 100.0% | **87.5%** | No change |
| **High-Performance** | 62.5% | **100.0%** | **+60%** |

## Runtime Performance

| Configuration | Total Runtime | GEPA Phase | Use Case |
|---------------|---------------|------------|----------|
| **Lightweight** | ~6.5 minutes | ~4 minutes | Learning/Development |
| **Medium** | ~10+ minutes | ~8 minutes | Baseline Testing |
| **High-Performance** | ~15-20 minutes | ~12-15 minutes | Production Quality |

## Key Findings

### Lightweight Models (Recommended for Learning)
- **Audience Judge**: 100% improvement (27.78% → 55.56%)
- **Comedian**: Stable 100% accuracy
- **Runtime**: Fast 6.5 minutes
- **Best for**: Understanding GEPA optimization

### Medium Models (Optimization Plateau)
- **Audience Judge**: No improvement (44.44% baseline)
- **Comedian**: No optimization gain
- **Runtime**: ~10+ minutes
- **Insight**: Better baselines limit optimization potential

### High-Performance Models (Best Results)
- **Audience Judge**: 160% improvement (27.78% → 72.22%)
- **Comedian**: 60% improvement (62.5% → 100%)
- **Runtime**: 15-20 minutes
- **Best for**: Production-quality results

## Hardware Requirements

| RAM | Recommended Configuration | Expected Performance |
|-----|---------------------------|----------------------|
| 16GB | llama3.2:1b + llama3.1:8b | Good for learning |
| 32GB | llama3.1:8b + qwen3:8b | Baseline testing |
| 64GB+ | gpt-oss:20b + gpt-oss:120b | Production quality |

## Reproducibility

To reproduce these results:
```bash
cd local_gepa_experiment
python evaluator_optimizer_dspy.py  # Default: llama3.2:1b + llama3.1:8b
python evaluator_optimizer_dspy.py --student llama3.1:8b --teacher qwen3:8b
python evaluator_optimizer_dspy.py --student gpt-oss:20b --teacher gpt-oss:120b
```

**Note**: Results may vary slightly due to model randomness and system performance differences.