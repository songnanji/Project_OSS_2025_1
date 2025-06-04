import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.monthly_income = {}  # 월별 수입 저장: {("2024", "06"): 2000000}

    def add_expense(self, category, description, amount):
        today = datetime.date.today()
        expense = Expense(today.isoformat(), category, description, amount)
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

    # ✅ 수입 입력 기능
    def set_monthly_income(self, amount):
        today = datetime.date.today()
        key = (str(today.year), f"{today.month:02}")
        self.monthly_income[key] = amount
        print(f"{today.year}년 {today.month}월 수입이 {amount}원으로 설정되었습니다.\n")

    # ✅ 월말 정산 기능
    def summarize_month(self):
        today = datetime.date.today()
        year, month = str(today.year), f"{today.month:02}"
        key = (year, month)

        # 월 수입
        income = self.monthly_income.get(key)
        if income is None:
            print("먼저 수입을 설정해 주세요. (메뉴에서 '수입 설정')\n")
            return

        # 월별 지출 합계
        month_expenses = [
            e.amount for e in self.expenses
            if e.date.startswith(f"{year}-{month}")
        ]
        total_spent = sum(month_expenses)
        remaining = income - total_spent
        saving_rate = round((remaining / income) * 100, 2)

        print(f"\n[{year}년 {month}월 정산 결과]")
        print(f"- 수입: {income}원")
        print(f"- 지출: {total_spent}원")
        print(f"- 잔액: {remaining}원")
        print(f"- 절약률: {saving_rate}%\n")
