# Test Case - Valid Login Automation

---

# Test Case ID
TC-AUTO-LOGIN-001

---

# Test Scenario
Verify that a valid user can successfully login into the application.

---

# Automation Type
UI Automation Testing

---

# Tool Used
- Playwright
- Pytest
- Python

---

# Preconditions
- Internet connection available
- Website accessible
- Valid credentials available

---

# Test Data

| Field | Value |
|---|---|
| Username | standard_user |
| Password | secret_sauce |

---

# Test Steps

1. Launch Chromium browser
2. Open SauceDemo website
3. Enter username
4. Enter password
5. Click login button
6. Wait for navigation
7. Verify inventory page loads successfully

---

# Expected Result

User should successfully login and navigate to inventory page.

---

# Actual Result

User successfully logged in and inventory page loaded correctly.

---

# Status

PASS

---

# Assertion Used

```python
assert "inventory" in page.url
```

---

# Failure Handling

If test execution fails:
- Screenshot automatically captured
- Exception raised for debugging

---

# Screenshot Path

```text
screenshots/login_failure.png
```

---

# CI/CD Validation

This test is configured to run automatically using GitHub Actions pipeline.

Pipeline Result:
- PASS (Green Build)

---

# Concepts Demonstrated

- Browser automation
- Form interaction
- Assertions
- Exception handling
- Screenshot capture
- Automated CI execution
- QA automation workflow
