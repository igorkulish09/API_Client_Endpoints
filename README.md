# API_Client_Endpoints

This package provides Python clients for interacting with The Cat API.

## Installation

pip install rest_client_example

# Endpoints

**The Cat API Client**

- get_random_cats(limit: int = 5) -> List[Dict]:
Returns a list of random cat details from The Cat API.

- get_cat_by_id(cat_id: str) -> Dict:
Retrieves information about a specific cat based on its ID from The Cat API.

# **Email Verification Service**

EmailVerificationService:
An email verification service that checks the validity of email addresses. It stores the verification results, allowing retrieval and clearing of the results.

- verify_email(email: str) -> Dict[str, bool]:
Verifies the validity of the provided email address.

- get_verification_results() -> List[Dict[str, Optional[bool]]]:
Retrieves a list of all email verification results.

- clear_results():
Clears the stored email verification results.

# Type Annotations and Linter

This package utilizes type annotations to enhance code clarity and adheres to the wemake-python-styleguide linting standards.

# Contributing

Contributions to this project are welcome! If you have any suggestions, feedback, or would like to contribute code, please feel free to open an issue or submit a pull request.

# Local Installation

To install the package locally for development purposes, follow these steps:

1. Navigate to the root directory of your project in the command line.
2. Run the following command:

python -m pip install .
