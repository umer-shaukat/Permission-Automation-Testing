# Permission Platform Automation Testing
This project contains automated test scripts for the Permission platform, specifically targeting login functionality, form validation, and UI checks. The tests use Selenium WebDriver with Python and follow the Page Object Model (POM) design pattern for easy maintenance.

## Project Setup


PermissionTests/
│
├── page_objects/
│   ├── login_page.py             # Page object for login page interactions
│   ├── home_page.py              # Page object for homepage interactions after login
│
├── tests/
│   ├── test_login.py             # Test cases for login scenarios
│
├── utils/                        # Utility functions (e.g., reCAPTCHA handling)
│   └── recaptcha_handler.py
│
├── reports/                      # Directory for test reports
│   └── test_report.html          # HTML test report (generated after each run)
│
├── constants.py                  # Centralized constants for selectors, messages, and test data
├── README.md                     # Project setup and instructions
└── requirements.txt              # Dependencies for the project


### Prerequisites

- Python 3.x
- ChromeDriver (matching the version of Chrome installed)

### Installation

1. Clone the repository.
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   
### Run All Tests

To execute all tests in the suite and generate an HTML report:
   
   pytest --html=reports/test_report.htm

### Run a Specific Test
To run a specific test case, use the following syntax (e.g., test_valid_login):
   
   pytest tests/test_login.py::test_valid_login --html=reports/test_report.html

### Generating Reports

   pytest --html=reports/test_report.html

