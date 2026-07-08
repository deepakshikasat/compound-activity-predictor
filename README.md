# Compound Activity Predictor

    Regression workflow for predicting compound potency from interpretable molecular descriptors.

    ## Dataset

    Synthetic public-safe compound table inspired by ChEMBL/TDC bioactivity schemas.

    ## Methods

    - Descriptor engineering
- Ridge-style regression baseline
- Predicted-vs-actual and residual outputs
- RDKit-ready descriptor module

    ## Reproduce

    ```bash
    python scripts/run_pipeline.py
    ```

    ## Outputs

    - `data/compound_activity.csv`
- `outputs/regression_metrics.csv`
- `outputs/predictions.csv`
- `figures/predicted_vs_actual.svg`

    ## Analysis Report

    Open `reports/analysis_report.html` for the full hypothesis, data provenance,
    process, outputs, and interpretation narrative.

    ## Portfolio Note

    This repository uses public or synthetic demonstration data only. It is
    intended to show reproducible computational biology and AI/ML workflow
    design without relying on confidential or employer-owned material.
