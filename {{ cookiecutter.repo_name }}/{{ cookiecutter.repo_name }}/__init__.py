import yaml
from pathlib import Path


# Define project base directory
project_dir = Path(__file__).resolve().parents[1]

# Model config file
with open(project_dir / "model_config.yaml", "rt") as f:
    model_config = yaml.safe_load(f.read())