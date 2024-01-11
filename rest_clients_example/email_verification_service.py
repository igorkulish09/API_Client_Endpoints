"""Email verification."""

from typing import Dict, List, Optional

VerificationResult = Dict[str, Optional[bool]]


class EmailVerificationService(object):
    """
    Service for verifying email addresses.

    Attributes:
        result_list (List[Dict[str, Optional[bool]]]): A list to store verification results.
    """

    def __init__(self):
        """
        Initialize the EmailVerificationService.

        This method sets up the initial state of the EmailVerificationService.
        It creates an empty list to store verification results.
        """
        self.result_list = []

    async def async_verify_email(self, email: str) -> Dict[str, bool]:
        """
        Asynchronously verify the validity of an email address.

        Args:
            email (str): Email address to be verified.

        Returns:
            Dict[str, bool]: A dictionary with the verification result (valid/invalid).
        """
        is_valid = '@' in email
        res_ult = {'email': email, 'is_valid': is_valid}
        self.result_list.append(res_ult)
        return res_ult

    async def async_get_verification_results(self) -> List[VerificationResult]:
        """
        Asynchronously retrieve the results of email verification.

        Returns:
            List[Dict[str, Optional[bool]]]: List of dictionaries with verification results.
        """
        return self.result_list

    def clear_results(self):
        """Clear the results of email verification."""
        self.result_list = []
