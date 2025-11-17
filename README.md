
# Bean Pest Management Knowledge Base

A focused Knowledge Representation & Reasoning (KR&R) system for bean pest management. This repository contains a well-documented Jupyter Notebook that implements a formal knowledge base, first-order logic rules, and an interactive advisor to diagnose pests and recommend safe, practical control measures.

## Quick links

- Notebook: `beans_pest_knowledge.ipynb`
- Dependencies: `requirements.txt`

## Overview

This project implements a compact, production-minded KR&R pipeline for bean pest management. It includes:

- A formal ontology for pests and control methods
- A knowledge base instantiated with common bean pests and control products
- First-Order Logic (FOL) rules that encode safety-first and IPM principles
- An interactive advisor for symptom-based diagnosis and recommendations
- Visualization of semantic relationships between pests and control options

The implementation is intended for educational and research use, and to serve as a foundation for decision-support tools in smallholder and research contexts.

## Features

- Symptom-driven pest diagnosis with confidence scoring
- Safety-prioritized recommendations (low-risk options first)
- Environmental and user-safety warnings for high-risk products
- Resistance-management suggestions (rotation options)
- Interactive command-line/Jupyter interface and visualizations

## Installation

Prerequisites

- Python 3.8+
- Jupyter Notebook or JupyterLab

Install dependencies:

```powershell
pip install -r "requirements.txt"
```

Note: run the command from the repository root. The path above works from Windows PowerShell when your current directory is the workspace root.

## Usage

Open the notebook and run the cells in order, or run the interactive advisor from a Python session.

In Jupyter:

1. Launch Jupyter and open `beans_pest_knowledge.ipynb`.
2. Run the demonstration cells (`run_demonstration()`) to see system capabilities.
3. Use `interactive_session()` to start the interactive advisor loop.

From a Python script or REPL you can import and run the main functions provided in the notebook (the notebook defines `BeanPestAdvisor`, `run_demonstration`, and `interactive_session`).

## Project structure

```
<workspace root>/
│  ├─ beans_pest_knowledge.ipynb          # Primary notebook (this project)
│  ├─ README.md                           # This file
│  └─ requirements.txt                    # Python dependencies
```

## Key components (notebook summary)

- BeanPestKnowledgeBase: data models for pests, pesticides and symptom mappings
- BeanPestLogic: FOL-based diagnosis, safety-first recommendation engine, rotation logic
- BeanPestAdvisor: simple interactive CLI and demonstration harness
- Visualization utilities: severity/risk charts and semantic network graphs

## Examples

Typical notebook examples include:

- Symptom diagnosis (e.g. `['leaf_curling','yellowing']`) → returns likely pests with confidence
- Recommendations grouped by risk level (low → moderate → high)
- Visual semantic network of pest–control relationships

## Extensibility

The knowledge base is intentionally modular. Suggested extensions:

- Add regional pest variants and local control products
- Add weather or phenology-based risk predictors
- Export the knowledge base to a lightweight API for web/mobile clients

## Contributing

Contributions are welcome. Please open issues for suggestions or submit pull requests with small, well-tested changes. Keep changes focused on data additions, rule improvements, or documentation.

## License and academic note

This repository was developed for educational and research purposes. If you reuse code or data, please credit the author and follow standard academic citation practices.

---


