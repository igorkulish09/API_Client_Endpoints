from typing import Dict, List, Optional


class EmailVerificationService:
    def __init__(self):
        self.email_results: List[Dict[str, str]] = []

    def verify_email(self, email: str) -> Dict[str, str]:
        # Simulate email verification logic
        result = {"email": email, "status": "verified"}
        self.email_results.append(result)
        return result

    def get_all_results(self) -> List[Dict[str, str]]:
        return self.email_results

    def get_result_by_email(self, email: str) -> Optional[Dict[str, str]]:
        for result in self.email_results:
            if result["email"] == email:
                return result
        return None

    def delete_result_by_email(self, email: str) -> None:
        self.email_results = [result for result in self.email_results if result["email"] != email]
