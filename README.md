# Playwright QA Automation Portfolio Project

## Project Overview

This repository demonstrates a beginner-to-intermediate level QA automation framework built using Python and Playwright.

The project focuses on:
- UI automation testing
- Professional test structure
- CI/CD integration
- Screenshot capture on failures
- GitHub Actions automation pipeline
- QA engineering workflow practices

This repository was created as part of a QA Automation learning and portfolio project.

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Automation scripting |
| Playwright | Browser automation |
| Pytest | Test execution framework |
| GitHub Actions | CI/CD pipeline |
| GitHub | Version control and portfolio hosting |

---

# Project Structure

```text
playwright-qa-automation/
│
├── 
│   test_file.py
│
├── screenshots/
│
├── .github/
│   └── workflows/
│       └── playwright.yml
│
├── requirements.txt
│
└── README.md
```

---

# Automated Test Scenario

The current automation suite validates:

- Successful login functionality
- Page navigation after login
- Basic assertion handling
- Screenshot capture on failure

---

# Test Environment

- Python 3
- Chromium Browser
- Playwright
- GitHub Codespaces
- GitHub Actions CI Environment

---

# Implemented Features

## UI Automation
- Browser launch automation
- Login form interaction
- Assertion validation
- URL verification

## Error Handling
- Automatic screenshot capture on failure
- Exception handling structure

## CI/CD Integration
- Automated test execution using GitHub Actions
- Continuous Integration pipeline validation
- Automated workflow execution on push

---

# Test Workflow

```text
Launch Browser
    ↓
Open Website
    ↓
Enter Credentials
    ↓
Submit Login
    ↓
Verify Successful Navigation
    ↓
Capture Screenshot on Failure
    ↓
Close Browser
```

---

# Implemented Automation Concepts

This project demonstrates understanding of:
- Playwright automation
- Pytest framework basics
- Browser automation lifecycle
- Assertions
- Error handling
- CI/CD workflows
- GitHub Actions
- Automated testing pipelines
- QA automation workflow

---

# CI/CD Pipeline

The repository includes a GitHub Actions pipeline that:
- Installs dependencies
- Installs Playwright browsers
- Executes automated tests
- Reports test execution status

Pipeline Status:
- Successfully configured
- Green build passing

---

# Challenges Faced During Setup

## 1. Browser Launch Failure
### Error
```text
TargetClosedError: BrowserType.launch
```

### Cause
Missing Playwright browser dependencies in container environment.

### Solution
Installed Playwright dependencies using:

```bash
playwright install --with-deps
```

---

## 2. Git Push Rejection
### Error
```text
Updates were rejected because the remote contains work that you do not have locally
```

### Cause
Remote repository had changes not available locally.

### Solution
Performed:
```bash
git pull origin main
```

Then pushed successfully.

---

# Future Improvements

Planned future upgrades:
- Multiple test scenarios
- Pytest fixtures
- Page Object Model (POM)
- API testing integration
- Allure reporting
- Parallel execution
- Appium mobile automation
- Load testing integration

---

# Portfolio Purpose

This repository was created to demonstrate:
- QA automation learning progress
- Practical browser automation
- CI/CD pipeline integration
- Automation debugging experience
- Professional QA workflow understanding

---

# Author

QA Automation portfolio project created using Python, Playwright, Pytest, and GitHub Actions.
