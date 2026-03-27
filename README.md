<div align="center">

# 🌐 Federated Learning Core

### FedAvg • Non-IID Partitioning • Compression • Personalization • DP-SGD

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch)](https://pytorch.org/)
[![Flower](https://img.shields.io/badge/Flower-Federated%20Learning-6B46C1?style=flat)](https://flower.ai/)

[Overview](#-overview) • [About](#-about) • [Topics](#-topics) • [Quick Start](#-quick-start) • [Experiments](#-experiments)

---

Core federated learning repository covering **algorithm baselines**, **partitioning strategies**, **communication efficiency**, **personalization**, and **privacy-aware training**.

</div>

---

## 🎯 Overview

`federated-learning-core` provides reusable FL building blocks:

- FedAvg/FedProx/FedAdam orchestration layers
- IID and non-IID client data partitioning
- Compression strategies for communication cost reduction
- Personalization modules for client-specific adaptation
- DP-SGD privacy mechanisms and accounting

## 📌 About

- Engineered for experimentation and modular FL system design
- Supports research workflows and production migration paths
- Includes ready-to-run scenario and experiment scripts

## 🏷️ Topics

`federated-learning` `fedavg` `non-iid` `flower` `differential-privacy` `distributed-ml` `pytorch` `privacy`

## 🧩 Architecture

- `src/algorithms/`: aggregation and strategy modules
- `src/data/partitioning/`: IID and skew partitioners
- `src/training/flower/`: orchestrated FL training
- `src/optimization/`: compression and personalization
- `src/privacy/dp_sgd/`: private training components
- `src/scenarios/`: cross-silo and vertical setups

## ⚡ Quick Start

```bash
pip install -r requirements.txt
pytest -q tests/test_public_surfaces.py
```

## 🧪 Experiments

- `src/experiments/run_fedavg.py`
- `src/experiments/run_flower.py`
- `src/experiments/run_compression.py`
- `src/experiments/run_cross_silo.py`
- `src/experiments/run_vertical.py`
- `src/experiments/run_personalization.py`
- `src/experiments/run_dp.py`

## 🛠️ Tech Stack

**FL/ML:** PyTorch, Flower, NumPy, scikit-learn  
**Optimization:** compression + personalization techniques  
**Privacy:** DP-SGD and accounting utilities
