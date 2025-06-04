#Create account class
class Account:
    def __init__(self, name, account_type):
        """
        :param name: str - Account name (e.g., 'Cash', 'Revenue')
        :param account_type: str - One of: 'Asset', 'Liability', 'Equity', 'Revenue', 'Expense'
        """
        self.name = name
        self.account_type = account_type
        self.balance = 0.0
        self.transactions = []

    def post(self, amount, is_debit):
        """
        Posts a transaction to the account.

        :param amount: float - Amount to post
        :param is_debit: bool - True if debit, False if credit
        """
        if self.account_type in ['Asset', 'Expense']:
            self.balance += amount if is_debit else -amount
        elif self.account_type in ['Liability', 'Equity', 'Revenue']:
            self.balance += -amount if is_debit else amount
        else:
            raise ValueError(f"Unsupported account type: {self.account_type}")
        
        self.transactions.append({
            'amount': amount,
            'type': 'debit' if is_debit else 'credit'
        })

    def __str__(self):
        return f"{self.name} ({self.account_type}): {self.balance:.2f}"
