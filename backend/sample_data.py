"""Generate sample banking documents for testing"""

LOAN_FAQ = """
PERSONAL LOAN FAQ

Q: What is a personal loan?
A: A personal loan is an unsecured loan that can be used for various purposes like medical expenses, home renovation, education, or debt consolidation.

Q: What is the interest rate for personal loans?
A: Interest rates range from 10.5% to 24% per annum depending on your credit score, income, and loan amount.

Q: What is the maximum loan amount?
A: You can borrow up to $50,000 based on your eligibility.

Q: What is the repayment tenure?
A: Repayment tenure ranges from 12 months to 60 months.

Q: What documents are required?
A: You need ID proof, address proof, income proof (salary slips/bank statements), and employment proof.

Q: How long does approval take?
A: Loan approval typically takes 24-48 hours after document verification.
"""

CREDIT_CARD_INFO = """
CREDIT CARD INFORMATION

PLATINUM CREDIT CARD
- Annual Fee: $99 (waived first year)
- Interest Rate: 18% APR
- Credit Limit: Up to $10,000
- Rewards: 2% cashback on all purchases
- Benefits: Travel insurance, airport lounge access

GOLD CREDIT CARD
- Annual Fee: $49
- Interest Rate: 21% APR
- Credit Limit: Up to $5,000
- Rewards: 1.5% cashback on dining and groceries
- Benefits: Purchase protection, extended warranty

ELIGIBILITY CRITERIA
- Minimum age: 21 years
- Minimum income: $25,000 per year
- Good credit score (650+)

PAYMENT TERMS
- Grace period: 45 days interest-free
- Minimum payment: 5% of outstanding balance
- Late payment fee: $35
"""

BANKING_FAQ = """
GENERAL BANKING FAQ

Q: How do I open a savings account?
A: Visit any branch with ID proof, address proof, and initial deposit of $100. You can also apply online.

Q: What is the interest rate on savings accounts?
A: Current rate is 3.5% per annum, calculated daily and credited quarterly.

Q: Are there any account maintenance charges?
A: No charges if minimum balance of $1,000 is maintained. Otherwise $10/month fee applies.

Q: How do I activate internet banking?
A: Visit our website, click "Register", enter your account number and registered mobile number to receive OTP.

Q: What is the daily ATM withdrawal limit?
A: $500 per day from ATMs. You can request temporary limit increase through internet banking.

Q: How do I report a lost debit card?
A: Call our 24/7 helpline immediately or use the mobile app to block your card instantly.
"""

def create_sample_files():
    os.makedirs("sample_docs", exist_ok=True)
    
    with open("sample_docs/loan_faq.txt", "w") as f:
        f.write(LOAN_FAQ)
    
    with open("sample_docs/credit_card_info.txt", "w") as f:
        f.write(CREDIT_CARD_INFO)
    
    with open("sample_docs/banking_faq.txt", "w") as f:
        f.write(BANKING_FAQ)
    
    print("Sample documents created in sample_docs/")

if __name__ == "__main__":
    import os
    create_sample_files()
