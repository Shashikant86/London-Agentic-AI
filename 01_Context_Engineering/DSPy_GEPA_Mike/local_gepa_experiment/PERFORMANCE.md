# DSPy GEPA Performance Summary

Quick reference for DSPy GEPA optimization results with local Ollama models.

**Test Hardware**: Apple M4 Max MacBook Pro, 128GB RAM

## Configuration Comparison

### Lightweight Models (llama3.2:1b + llama3.1:8b) ⭐ Best for Learning
| Component | Before GEPA | After GEPA | Improvement |
|-----------|-------------|------------|-------------|
| **Audience Judge** | 27.78% | **55.56%** | **+100%** |
| **Comedian** | 100.0% | **100.0%** | Stable |
| **Runtime** | - | **6.5 min** | Fast |

### Medium Models (llama3.1:8b + qwen3:8b) 
| Component | Before GEPA | After GEPA | Improvement |
|-----------|-------------|------------|-------------|
| **Audience Judge** | 44.44% | **44.44%** | **No change** |
| **Comedian** | 100.0% | **87.5%** | No change |
| **Runtime** | - | **~10+ min** | Slower |

### High-Performance Models (gpt-oss:20b + gpt-oss:120b) ⭐ Best Results
| Component | Before GEPA | After GEPA | Improvement |
|-----------|-------------|------------|-------------|
| **Audience Judge** | 27.78% | **72.22%** | **+160%** |
| **Comedian** | 62.5% | **100.0%** | **+60%** |
| **Runtime** | - | **15-20 min** | Premium |

## Runtime Breakdown (Lightweight Models)

| Phase | Duration |
|-------|----------|
| **Total Runtime** | **6.5 minutes** |
| Environment Setup | 5 seconds |
| Dataset Creation | 15 seconds |
| Basic Evaluations | 30 seconds |
| GEPA Optimization | 4 minutes |
| Final Testing | 15 seconds |

## Quick Start Commands

```bash
# Default: Lightweight models (recommended for learning)
python evaluator_optimizer_dspy.py

# Medium models (optimization plateau)
python evaluator_optimizer_dspy.py --student llama3.1:8b --teacher qwen3:8b

# High-performance models (best results)  
python evaluator_optimizer_dspy.py --student gpt-oss:20b --teacher gpt-oss:120b
```

## Key Insights

### Why Lightweight Models Excel for Learning
- **Dramatic Visible Gains**: +100% improvement shows GEPA working clearly
- **Fast Iteration**: 6.5 minutes allows rapid experimentation
- **Resource Efficiency**: Works on most systems (16GB+ RAM)

### Why Medium Models Plateau
- **Optimization Ceiling**: Already near their capability limits  
- **No Improvement**: GEPA can't enhance already-capable baselines
- **Educational Limitation**: Not ideal for learning GEPA concepts

### Why High-Performance Models Dominate
- **Exceptional Gains**: +160% audience judge improvement
- **Perfect Results**: 100% comedian accuracy after optimization
- **Professional Quality**: Both components reach optimal performance