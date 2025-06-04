import datetime
from collections import defaultdict

class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"[{self.date}] {self.category} - {self.description}: {self.amount}원"

class Income:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"[{self.date}] {self.category} - {self.description}: {self.amount}원"

class Budget:
    def __init__(self):
        self.expenses = []
        self.incomes = []

    # ✅ 지출 기능
    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category.strip(), description.strip(), amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    # ✅ 수입 기능
    def add_income(self, category, description, amount):
        today = datetime.date.today().isoformat()
        income = Income(today, category.strip(), description.strip(), amount)
        self.incomes.append(income)
        print("수입이 추가되었습니다.\n")

    def list_incomes(self):
        if not self.incomes:
            print("수입 내역이 없습니다.\n")
            return
        print("\n[수입 목록]")
        for idx, i in enumerate(self.incomes, 1):
            print(f"{idx}. {i}")
        print()

    def search_income_by_keyword(self, keyword):
        if not self.incomes:
            print("수입 내역이 없습니다.\n")
            return

        keyword = keyword.strip().lower()
        results = [
            i for i in self.incomes
            if keyword in i.description.lower() or keyword in i.category.lower()
        ]

        if not results:
            print(f"'{keyword}'에 해당하는 수입 항목이 없습니다.\n")
            return

        print(f"\n[검색 결과: '{keyword}']")
        for idx, i in enumerate(results, 1):
            print(f"{idx}. {i}")
        print()
