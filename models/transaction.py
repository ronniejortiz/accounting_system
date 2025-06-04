# Create transaction class

from datetime import datetime

class Transaction:
    def __init__(self, date, description, debit_account, credit_account, amount, user):
        """
        :param date: datetime or str - When the transaction occurred
        :param description: str - Description of the transaction
        :param debit_account: str - Name of the account to debit
        :param credit_account: str - Name of the account to credit
        :param amount: float - Amount of the transaction
        :param user: str - Who entered the transaction
        """
        self.date = self._parse_date(date)
        self.description = description
        self.debit_account = debit_account
        self.credit_account = credit_account
        self.amount = amount
        self.user = user
        self.timestamp = datetime.now()  # time the transaction was recorded

    def _parse_date(self, date):
        if isinstance(date, datetime):
            return date
        return datetime.strptime(date, "%Y-%m-%d")
        
    def __str__(self):
        return (
            f"{self.date.date()} | {self.description} | "
            f"DR: {self.debit_account} | CR: {self.credit_account} | "
            f"${self.amount:.2f} by {self.user}"
        )