"""
DMJ LLM Configuration
=====================

Global project configuration for DMJ LLM.
This file contains project paths and general settings.
Model-specific hyperparameters are stored in model_config.py.
"""

from pathlib import Path

# ============================================================
# Project Information
# ============================================================

PROJECT_NAME = "DMJ LLM"
VERSION = "0.2.0-alpha"

# ============================================================
# Project Paths
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_DIR = PROJECT_ROOT / "datasets"
DATASET_PATH = DATASET_DIR / "dmj_dataset_v1.0.0.jsonl"

MODEL_DIR = PROJECT_ROOT / "models"

CHECKPOINT_DIR = PROJECT_ROOT / "training" / "checkpoints"

LOG_DIR = PROJECT_ROOT / "training" / "logs"

CACHE_DIR = PROJECT_ROOT / "training" / "cache"

OUTPUT_DIR = MODEL_DIR / "dmj-llm-v0.2.0-alpha"

# ============================================================
# Runtime Settings
# ============================================================

SEED = 42

NUM_WORKERS = 2

USE_FP16 = True

USE_BF16 = False

PIN_MEMORY = True

# ============================================================
# Logging
# ============================================================

LOG_LEVEL = "INFO"

LOG_EVERY_N_STEPS = 10

SAVE_EVERY_N_STEPS = 500

# ============================================================
# Create Required Directories
# ============================================================

MODEL_DIR.mkdir(parents=True, exist_ok=True)

CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)

LOG_DIR.mkdir(parents=True, exist_ok=True)

CACHE_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)