class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance
    
import unittest

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        """This runs before each test"""
        self.account = BankAccount(1000)

    def test_initial_balance(self):
        """Test if account is initialized with correct balance"""
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit(self):
        """Test deposit functionality"""
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_negative_deposit(self):
        """Test if depositing negative amount raises error"""
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_withdraw(self):
        """Test withdrawal functionality"""
        self.account.withdraw(300)
        self.assertEqual(self.account.get_balance(), 700)

    def test_insufficient_funds(self):
        """Test if withdrawing more than balance raises error"""
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)

    def test_negative_withdraw(self):
        """Test if withdrawing negative amount raises error"""
        with self.assertRaises(ValueError):
            self.account.withdraw(-100)

if __name__ == '__main__':
    unittest.main()