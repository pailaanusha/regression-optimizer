# Regression Optimization Workflow Simulation

## Overview

This project is a simulation-based Proof of Concept (POC) created to understand how regression test optimization can be designed using code-change impact, historical test data, test coverage, risk-based prioritization, and LLM-assisted analysis.

The POC uses static datasets and configuration files to simulate inputs that would normally be obtained dynamically from source-control systems, test management systems, coverage tools, and CI/CD environments.

The project is intended for learning and demonstrating regression optimization concepts and workflow design. It is not intended to represent a production-ready regression test optimization engine.

---

## Objective

The objective of this POC is to understand how a regression testing workflow can identify and prioritize relevant tests instead of executing an entire regression suite for every change.

The workflow demonstrates:

- Change impact analysis
- Test-to-module coverage mapping
- Historical test execution data
- Rule-based risk scoring
- Test prioritization
- LLM-assisted test analysis
- Pytest-based test execution
- GitHub Actions CI/CD workflow

Static files are used to simulate the data that would normally be collected dynamically in a real-world implementation.

---

## Workflow

```text
             STATIC / SIMULATED INPUTS
                       |
        +--------------+--------------+
        |              |              |
        v              v              v
 changed_files    coverage_map    test_history
        |              |              |
        +--------------+--------------+
                       |
                       v
              Regression Optimizer
                       |
              +--------+--------+
              |                 |
              v                 v
       Change Impact       Risk Scoring
          Analysis
              |                 |
              +--------+--------+
                       |
                       v
              Test Prioritization
                       |
                       v
               LLM Assistance
                       |
                       v
              Optimized Test Suite
                       |
                       v
                    Pytest
                       |
                       v
               GitHub Actions
```

---

## Key Concepts Demonstrated

### 1. Change Impact Analysis

The `changed_files.txt` file is used to simulate application files or modules affected by a code change.

The optimizer compares the changed files with the test-to-module relationships defined in `coverage_map.json` to identify tests associated with impacted application components.

In a real-world implementation, changed files could be obtained dynamically from source-control information such as Git changes, pull requests, or commands such as `git diff`.

### 2. Test Coverage Mapping

The `coverage_map.json` file contains a simulated mapping between tests and the application files or modules they cover.

The optimizer uses this mapping to determine which tests are related to the changed application components.

This demonstrates the basic idea of using coverage relationships for change-impact-based regression test selection.

### 3. Historical Test Analysis

The `test_history.csv` file contains simulated historical test execution information.

The dataset represents the type of historical information that could be used to understand previous test results and execution behavior.

In a production environment, this information could be obtained dynamically from CI/CD systems or test management platforms instead of a static CSV file.

### 4. Rule-Based Risk Scoring

The POC uses a simplified rule-based scoring approach to assign risk or priority to tests based on historical test results.

The scoring logic is intentionally static and simplified for learning purposes.

The purpose is to demonstrate how historical test information can contribute to risk-based test prioritization.

This scoring model is not intended to represent an enterprise or production-grade risk calculation model.

### 5. Test Prioritization

The optimizer combines the identified impacted tests with the risk-based prioritization of tests.

Higher-priority tests can be selected earlier for regression execution.

The POC demonstrates the basic workflow of narrowing a regression suite based on change impact and test risk.

### 6. LLM-Assisted Workflow Exploration

The project also explores the potential use of an LLM in regression optimization.

The simulated historical test data can be provided to an LLM-assisted workflow to explore tasks such as:

- Identifying potentially redundant tests
- Analyzing historical test patterns
- Supporting test prioritization
- Explaining risk factors
- Suggesting regression test scenarios

The current implementation focuses on understanding the workflow and architecture rather than building a production-grade LLM-based regression optimizer.

### 7. CI/CD Integration

The project includes a GitHub Actions workflow to demonstrate automated test execution through a CI/CD pipeline.

The workflow demonstrates how Pytest-based test execution can be incorporated into an automated CI/CD process.

The CI/CD workflow is primarily included as a learning exercise to understand how automated regression test execution can be integrated into a software delivery workflow.

---

## POC Inputs and Possible Real-World Sources

| POC Input | Possible Real-World Source |
|------------|----------------------------|
| `changed_files.txt` | Git/GitHub change information or `git diff` |
| `coverage_map.json` | Code coverage or test coverage systems |
| `test_history.csv` | CI/CD or test management systems |
| Rule-based risk score | Enterprise risk/prioritization logic |
| LLM-assisted analysis | LLM/GenAI service |

The POC intentionally uses static files instead of implementing these external integrations.

---

## Project Structure

```text
regression-optimizer/
│
├── .github/
│   └── workflows/
│       └── <GitHub Actions workflow>
│
├── tests/
│   ├── test_app.py
│   └── test_optimizer.py
│
├── app.py
├── optimizer.py
├── run_tests.py
├── changed_files.txt
├── coverage_map.json
├── test_history.csv
├── pytest.ini
└── README.md
```

### File Description

| File | Purpose |
|------|---------|
| `optimizer.py` | Contains regression optimization, change-impact analysis, risk scoring, and test prioritization logic |
| `app.py` | Sample application/workflow used by the tests |
| `run_tests.py` | Test execution helper |
| `tests/test_app.py` | Tests for the sample application |
| `tests/test_optimizer.py` | Tests for the optimization logic |
| `changed_files.txt` | Simulated changed application files/modules |
| `coverage_map.json` | Simulated mapping between tests and application modules/files |
| `test_history.csv` | Simulated historical test execution data |
| `.github/workflows/` | GitHub Actions CI/CD workflow configuration |
| `pytest.ini` | Pytest configuration |

---

## Test Execution

The project uses Pytest for test execution.

The sample test suite contains tests for both:

- The sample application
- The regression optimization logic

The test cases include examples such as:

- Login validation
- Product-related validation
- Discount calculation
- Payment validation
- Regression optimizer validation

The project also demonstrates parameterized testing using Pytest.

---

## Running the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Tests

```bash
pytest
```

### Run the Regression Optimizer

```bash
python optimizer.py
```

If `run_tests.py` is used as the execution helper:

```bash
python run_tests.py
```

---

## CI/CD Execution

The project contains a GitHub Actions workflow that automatically executes the test suite.

The workflow demonstrates:

```text
Code / Repository Change
          |
          v
GitHub Actions Trigger
          |
          v
Environment Setup
          |
          v
Install Dependencies
          |
          v
Execute Pytest
          |
          v
Display Test Results
```

The GitHub Actions execution provides a practical demonstration of integrating automated testing into a CI/CD workflow.

---

## Limitations

This project is intentionally implemented as a simulation-based POC.

The following limitations apply:

- Changed files are provided through a static file rather than dynamically retrieved from Git.
- Test coverage relationships are represented using a static JSON mapping.
- Historical test execution data is represented using a sample CSV dataset.
- Risk scoring uses simplified rule-based logic.
- The LLM-assisted workflow is exploratory rather than a production-grade AI optimization engine.
- The project does not currently integrate with an enterprise test management system.
- The project does not implement dynamic production test selection.

These limitations are intentional because the primary purpose of the project is to understand the concepts and workflow involved in regression test optimization.

---

## Learning Outcome

This POC provided hands-on understanding of how multiple testing and development concepts can work together in a regression optimization workflow:

- Python-based automation
- Pytest test execution
- Change impact analysis
- Test coverage mapping
- Historical test analysis
- Risk-based test prioritization
- LLM-assisted testing concepts
- CI/CD workflow integration
- GitHub Actions
- Regression test optimization concepts

---

## Future Enhancements

The simulation can be extended into a more dynamic regression optimization solution by integrating:

- Git-based change detection
- Dynamic code-change analysis
- Real test coverage information
- CI/CD test history
- Test management systems
- More advanced LLM-based test analysis
- MCP-based tool integration
- Automated test prioritization
- More sophisticated risk-based regression selection
- Test-result feedback loops

These enhancements are outside the scope of the current POC.

---

## Disclaimer

This project is a learning-oriented Proof of Concept created to understand the architecture and workflow of regression test optimization.

The static datasets, simplified risk scoring, and simulated integrations are intentionally designed to demonstrate the underlying concepts without representing a production enterprise implementation.
