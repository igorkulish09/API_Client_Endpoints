"""Email verification."""

from typing import Dict, List, Optional


class EmailVerificationService:
    """
    Service for verifying email addresses.

    Attributes:
        result_list (List[Dict[str, Optional[bool]]]): A list to store verification results.
    """

    def __init__(self) -> None:
        """
        Initialize the EmailVerificationService.

        This method sets up the initial state of the EmailVerificationService.
        It creates an empty list to store verification results.
        """
        self.result_list: List[Dict[str, Optional[bool]]] = []

    def verify_email(self, email: str) -> Dict[str, Optional[bool]]:
        """
        Verify the validity of an email address.

        Args:
            email (str): Email address to be verified.

        Returns:
            Dict[str, Optional[bool]]: A dictionary with the verification result (valid/invalid).
        """
        is_valid: Optional[bool] = '@' in email
        result: Dict[str, Optional[bool]] = {'email': email, 'is_valid': bool(is_valid)}
        self.result_list.append(result)
        return result

    def get_verification_results(self) -> List[Dict[str, Optional[bool]]]:
        """
        Retrieve the results of email verification.

        Returns:
            List[Dict[str, Optional[bool]]]: List of dictionaries with verification results.
        """
        return self.result_list

    def clear_results(self) -> None:
        """Clear the results of email verification."""
        self.result_list = []
