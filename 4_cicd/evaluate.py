
import subprocess
import sys

# 1. Install xgboost into the sklearn container dynamically
subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "xgboost"])

# 2. Now perform our imports
import json
import os
import tarfile
import pandas as pd
from sklearn.metrics import roc_auc_score
import xgboost as xgb

def main():
    model_dir = "/opt/ml/processing/model"
    test_path = "/opt/ml/processing/test/test.csv"
    out_path  = "/opt/ml/processing/evaluation/evaluation.json"

    # Extract any tar.gz present
    for fname in os.listdir(model_dir):
        if fname.endswith(".tar.gz"):
            tar_path = os.path.join(model_dir, fname)
            with tarfile.open(tar_path, "r:gz") as tar:
                tar.extractall(path=model_dir)

    # Prefer standard filenames
    candidates = ["xgboost-model", "model.xgb", "model"]
    model_path = None
    for c in candidates:
        p = os.path.join(model_dir, c)
        if os.path.exists(p) and os.path.isfile(p):
            model_path = p
            break

    # Last resort: pick first file that isn't tar.gz
    if model_path is None:
        for fname in os.listdir(model_dir):
            p = os.path.join(model_dir, fname)
            if os.path.isfile(p) and not fname.endswith(".tar.gz"):
                model_path = p
                break

    if model_path is None:
        raise FileNotFoundError(f"No model file found. Contents: {os.listdir(model_dir)}")

    df = pd.read_csv(test_path, header=None)
    y = df.iloc[:, 0].values
    X = df.iloc[:, 1:].values

    booster = xgb.Booster()
    booster.load_model(model_path)

    preds = booster.predict(xgb.DMatrix(X))
    auc = float(roc_auc_score(y, preds))

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump({"binary_classification_metrics": {"auc": {"value": auc}}}, f)

if __name__ == "__main__":
    main()
