# Coffee Knowledge Base: A KR&R System for Coffee Pest Management

A comprehensive Knowledge Representation and Reasoning (KR&R) system for coffee pest management, implemented in Jupyter Notebook. This system demonstrates formal knowledge representation techniques applied to the practical domain of agricultural pest control.

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Knowledge Representation](#-knowledge-representation)
- [System Architecture](#-system-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Key Components](#-key-components)
- [Examples](#-examples)
- [Extension Possibilities](#-extension-possibilities)
- [Contributing](#-contributing)
- [License](#-license)
- [Academic Context](#-academic-context)

## 🌟 Overview

This project implements a formal knowledge base system for coffee pest management using modern KR&R techniques. The system combines:

- **Formal Ontologies** with class hierarchies and relationships
- **First-Order Logic (FOL)** rules for automated reasoning
- **Semantic Networks** for relationship visualization
- **Rule-based Reasoning** for intelligent recommendations
- **Interactive Diagnosis** for practical application

The system helps farmers and agronomists identify coffee pests, understand their characteristics, and receive intelligent recommendations for sustainable management using Integrated Pest Management (IPM) principles.

## ✨ Features

- 🔍 **Intelligent Pest Diagnosis** - Identify pests from observed symptoms
- 🧠 **First-Order Logic Reasoning** - Formal logical inference for recommendations
- 🌐 **Semantic Network Visualization** - Graph-based knowledge representation
- 🛡️ **Safe-First Recommendations** - Prioritizes biological and cultural controls
- 📊 **Interactive Jupyter Interface** - User-friendly exploration and queries
- 🎯 **Real-World Application** - Practical agricultural knowledge domain
- 📈 **Extensible Architecture** - Easy to add new pests, pesticides, and rules

## 🧩 Knowledge Representation

### Formal Ontology

The system implements a comprehensive ontology with the following core classes:

- **Pest** (Insect, Fungus, Mites, Bacteria)
- **Pesticide** (Biological, Chemical, Cultural)
- **ControlMethod** (Cultural, Biological, Chemical, Mechanical)
- **Symptom** - Observable pest indicators
- **SafetyLevel** - Toxicity classifications

### First-Order Logic Rules

1. **Safe-First Principle:** ∀pest ∀control (Pest(pest) ∧ Controls(control, pest) ∧ Safe(control) → RecommendedFirst(control))

2. **Last-Resort Principle:** ∀pesticide ∀pest (Pesticide(pesticide) ∧ Controls(pesticide, pest) ∧ Dangerous(pesticide) → LastResort(pesticide))

3. **Symptom-Based Diagnosis:** ∀symptoms ∃pest (Exhibits(pest, symptoms) → Identified(pest))

## 🏗️ System Architecture

```
graph TD
    A[User Input] --> B[Knowledge Base]
    B --> C[Pest Ontology]
    B --> D[Pesticide Database]
    B --> E[Control Methods]
    C --> F[Reasoning Engine]
    D --> F
    E --> F
    F --> G[FOL Rules]
    F --> H[Semantic Network]
    G --> I[Recommendations]
    H --> I
    I --> J[Output & Visualization]
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Jupyter Notebook/JupyterLab

### Required Libraries

All dependencies are listed in `requirements.txt`. Install them using:

```bash
pip install -r requirements.txt
```

### Quick Start

1. Clone or download this repository

2. Install the required dependencies (see above)

3. Open the Jupyter notebook:
```bash
jupyter notebook coffee_knowledge_base.ipynb
```

## 💻 Usage

### Basic Demonstration

Run the complete system demonstration:

```python
advisor = demonstrate_system()
```

### Interactive Session

Launch the interactive advisor:

```python
run_interactive_session()
```

## 📁 Project Structure

```
coffee-pest-knowledge-base/
│
├── coffee_knowledge_base.ipynb     # Main Jupyter notebook
├── README.md                       # This file
└── requirements.txt                # Python dependencies
```

The notebook is organized into the following sections:

- **Introduction** - Project overview and KR&R concepts
- **Formal Ontology** - Class definitions and hierarchies
- **Knowledge Base** - Data instantiation
- **FOL Rules** - First-Order Logic implementations
- **Interactive System** - User interface components
- **Demonstration** - Comprehensive system showcase
- **Queries** - Knowledge base exploration examples
- **Summary** - Assignment documentation

## 🔧 Key Components

### Core Classes

- **CoffeePestKnowledgeBase** - Main knowledge container
- **PestManagementLogic** - Reasoning engine with FOL rules
- **InteractivePestAdvisor** - User interface controller

### Data Models

- **Pest** - Pest characteristics, symptoms, life cycle
- **Pesticide** - Chemical properties, safety, usage guidelines
- **ControlMethod** - Non-chemical management strategies

### Reasoning Capabilities

- Symptom-based pest diagnosis
- Safety-prioritized recommendation engine
- Semantic relationship queries
- Integrated Pest Management (IPM) strategy formulation

## 🎯 Examples

### Pest Diagnosis

**Input Symptoms:** "orange powder on leaves, leaf yellowing"

**Output:**
- Diagnosed: Coffee Leaf Rust (Confidence: 100%)
- Recommendations: Copper-based fungicides, shade management

### Safe-First Reasoning

For Coffee Berry Borer:

- 🟢 **PRIORITY:** Beauveria bassiana (biological), Harvest Hygiene (cultural)
- 🔴 **LAST RESORT:** Cypermethrin (chemical)

## 🔬 Extension Possibilities

This system can be extended in several ways:

- **Add More Pests:** Extend the knowledge base with additional coffee pests
- **Regional Adaptation:** Add location-specific pest and control information
- **Weather Integration:** Incorporate climate-based risk assessment
- **Mobile Interface:** Create a web or mobile application frontend
- **Machine Learning:** Add predictive analytics for pest outbreaks
- **Multi-language Support:** Translate for use in different regions

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- Additional pest and pesticide data
- Enhanced reasoning rules
- Improved visualization techniques
- Performance optimizations
- Documentation improvements

Please feel free to submit issues and pull requests.

## 📄 License

This project is created for educational purposes as part of a Knowledge Representation and Reasoning assignment. Feel free to use and modify for academic and research purposes.

## 📚 Academic Context

This implementation demonstrates key KR&R concepts suitable for university courses in:

- Artificial Intelligence
- Knowledge Representation
- Expert Systems
- Computational Agriculture
- Decision Support Systems

