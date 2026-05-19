from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
import os

def create_banking_pdf():
    # Create sample_docs directory if it doesn't exist
    os.makedirs("sample_docs", exist_ok=True)
    
    # Create PDF
    pdf_file = "sample_docs/banking_guide.pdf"
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor='darkblue',
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor='darkblue',
        spaceAfter=12,
        spaceBefore=12
    )
    
    # Title
    title = Paragraph("Complete Banking Services Guide", title_style)
    elements.append(title)
    elements.append(Spacer(1, 0.3*inch))
    
    # Personal Loans Section
    elements.append(Paragraph("Personal Loans", heading_style))
    
    loan_content = """
    <b>What is a Personal Loan?</b><br/>
    A personal loan is an unsecured loan that can be used for various purposes including medical expenses, 
    home renovation, education, wedding expenses, or debt consolidation. No collateral is required.
    <br/><br/>
    <b>Interest Rates:</b><br/>
    Our personal loan interest rates range from 10.5% to 24% per annum, depending on your credit score, 
    income level, and loan amount. Customers with excellent credit scores (750+) qualify for the lowest rates.
    <br/><br/>
    <b>Loan Amount:</b><br/>
    You can borrow anywhere from $1,000 to $50,000 based on your eligibility and repayment capacity.
    <br/><br/>
    <b>Repayment Tenure:</b><br/>
    Flexible repayment options from 12 months to 60 months. Choose a tenure that suits your budget.
    <br/><br/>
    <b>Required Documents:</b><br/>
    • Valid government-issued ID proof (Driver's License, Passport)<br/>
    • Address proof (Utility bill, Lease agreement)<br/>
    • Income proof (Last 3 months salary slips or bank statements)<br/>
    • Employment verification letter<br/>
    • Recent passport-size photographs
    <br/><br/>
    <b>Processing Time:</b><br/>
    Loan approval typically takes 24-48 hours after document verification. Funds are disbursed within 
    2-3 business days of approval.
    <br/><br/>
    <b>Eligibility Criteria:</b><br/>
    • Age: 21 to 65 years<br/>
    • Minimum monthly income: $2,500<br/>
    • Employment: Salaried or self-employed with stable income<br/>
    • Credit score: Minimum 650 (higher scores get better rates)
    """
    
    elements.append(Paragraph(loan_content, styles['BodyText']))
    elements.append(PageBreak())
    
    # Credit Cards Section
    elements.append(Paragraph("Credit Card Options", heading_style))
    
    cc_content = """
    <b>Platinum Credit Card</b><br/>
    Our premium offering for high-value customers.
    <br/><br/>
    • Annual Fee: $99 (waived for first year)<br/>
    • Interest Rate: 18% APR<br/>
    • Credit Limit: Up to $10,000<br/>
    • Rewards: 2% cashback on all purchases, 5% on travel and dining<br/>
    • Benefits: Complimentary airport lounge access (4 visits/year), travel insurance up to $100,000, 
    purchase protection, extended warranty on electronics, concierge service
    <br/><br/>
    <b>Gold Credit Card</b><br/>
    Perfect for everyday spending and building credit.
    <br/><br/>
    • Annual Fee: $49<br/>
    • Interest Rate: 21% APR<br/>
    • Credit Limit: Up to $5,000<br/>
    • Rewards: 1.5% cashback on dining and groceries, 1% on other purchases<br/>
    • Benefits: Purchase protection, extended warranty, fraud protection, mobile app management
    <br/><br/>
    <b>Student Credit Card</b><br/>
    Designed for students building their first credit history.
    <br/><br/>
    • Annual Fee: $0<br/>
    • Interest Rate: 24% APR<br/>
    • Credit Limit: Up to $1,500<br/>
    • Rewards: 1% cashback on all purchases<br/>
    • Benefits: Credit education resources, no foreign transaction fees, fraud protection
    <br/><br/>
    <b>Eligibility Criteria:</b><br/>
    • Minimum age: 21 years (18 for student card with co-signer)<br/>
    • Minimum annual income: $25,000 (Platinum), $18,000 (Gold), $0 (Student)<br/>
    • Good credit score: 650+ (Platinum), 600+ (Gold), No credit history OK (Student)
    <br/><br/>
    <b>Payment Terms:</b><br/>
    • Grace period: 45 days interest-free on purchases<br/>
    • Minimum payment: 5% of outstanding balance or $25, whichever is higher<br/>
    • Late payment fee: $35<br/>
    • Over-limit fee: $25<br/>
    • Foreign transaction fee: 3% (waived on Platinum)
    """
    
    elements.append(Paragraph(cc_content, styles['BodyText']))
    elements.append(PageBreak())
    
    # Savings Account Section
    elements.append(Paragraph("Savings Accounts", heading_style))
    
    savings_content = """
    <b>How to Open a Savings Account:</b><br/>
    Visit any branch with required documents or apply online through our website. The process takes 
    about 15 minutes in-branch or 24 hours for online applications.
    <br/><br/>
    <b>Required Documents:</b><br/>
    • Government-issued photo ID<br/>
    • Social Security Number or Tax ID<br/>
    • Proof of address (utility bill, lease agreement)<br/>
    • Initial deposit: $100 minimum
    <br/><br/>
    <b>Interest Rate:</b><br/>
    Current rate is 3.5% per annum (APY), calculated daily and credited quarterly. Rates are subject 
    to change based on market conditions.
    <br/><br/>
    <b>Account Maintenance:</b><br/>
    No monthly maintenance charges if you maintain a minimum balance of $1,000. Otherwise, a $10/month 
    service fee applies. Fee is waived for students and seniors (65+).
    <br/><br/>
    <b>Online Banking Activation:</b><br/>
    1. Visit our website and click "Register"<br/>
    2. Enter your account number and registered mobile number<br/>
    3. Receive OTP (One-Time Password) via SMS<br/>
    4. Create your username and password<br/>
    5. Set up security questions<br/>
    6. Start banking online 24/7
    <br/><br/>
    <b>Features:</b><br/>
    • Free debit card with contactless payment<br/>
    • Unlimited ATM withdrawals at our network<br/>
    • Mobile banking app for iOS and Android<br/>
    • Bill payment and fund transfer services<br/>
    • Email and SMS alerts for transactions<br/>
    • Overdraft protection available
    """
    
    elements.append(Paragraph(savings_content, styles['BodyText']))
    elements.append(PageBreak())
    
    # ATM and Debit Card Section
    elements.append(Paragraph("ATM & Debit Card Services", heading_style))
    
    atm_content = """
    <b>Daily ATM Withdrawal Limit:</b><br/>
    Standard limit is $500 per day from ATMs. You can request a temporary limit increase up to $2,000 
    through internet banking or mobile app for special circumstances (travel, large purchases).
    <br/><br/>
    <b>ATM Network:</b><br/>
    • 5,000+ ATMs nationwide in our network (free withdrawals)<br/>
    • 50,000+ partner ATMs (small fee may apply)<br/>
    • International ATM access in 150+ countries<br/>
    • 24/7 availability
    <br/><br/>
    <b>Debit Card Features:</b><br/>
    • Contactless payment up to $100<br/>
    • EMV chip security<br/>
    • Zero liability fraud protection<br/>
    • International usage enabled<br/>
    • Daily purchase limit: $5,000
    <br/><br/>
    <b>Lost or Stolen Card:</b><br/>
    Report immediately by:<br/>
    • Calling our 24/7 helpline: 1-800-BANK-HELP<br/>
    • Using mobile app "Block Card" feature (instant)<br/>
    • Visiting any branch<br/>
    <br/>
    Your card will be blocked immediately and a replacement card will be issued within 5-7 business days 
    at no charge.
    <br/><br/>
    <b>Card Replacement:</b><br/>
    • Lost/Stolen: Free replacement<br/>
    • Damaged: Free replacement<br/>
    • Upgrade: $10 fee<br/>
    • Express delivery: $25 (2-3 days)
    """
    
    elements.append(Paragraph(atm_content, styles['BodyText']))
    elements.append(PageBreak())
    
    # Customer Support Section
    elements.append(Paragraph("Customer Support", heading_style))
    
    support_content = """
    <b>Contact Us:</b><br/>
    • 24/7 Helpline: 1-800-BANK-HELP (1-800-226-5435)<br/>
    • Email: support@bankingsupport.com<br/>
    • Live Chat: Available on website and mobile app<br/>
    • Branch Locator: www.bankingsupport.com/branches<br/>
    • Social Media: @BankingSupport on Twitter, Facebook, Instagram
    <br/><br/>
    <b>Branch Hours:</b><br/>
    • Monday - Friday: 9:00 AM - 5:00 PM<br/>
    • Saturday: 9:00 AM - 1:00 PM<br/>
    • Sunday: Closed<br/>
    • Extended hours at select locations
    <br/><br/>
    <b>Common Issues Resolution Time:</b><br/>
    • Account balance inquiry: Instant<br/>
    • Card blocking: Instant<br/>
    • Transaction disputes: 5-7 business days<br/>
    • Loan application: 24-48 hours<br/>
    • Account opening: Same day (in-branch), 24 hours (online)
    <br/><br/>
    <b>Complaint Resolution:</b><br/>
    If you're not satisfied with our service:<br/>
    1. Contact customer service first<br/>
    2. Escalate to branch manager if unresolved<br/>
    3. File formal complaint online<br/>
    4. We respond within 48 hours<br/>
    5. Resolution within 7 business days
    <br/><br/>
    <b>Security Tips:</b><br/>
    • Never share your PIN or password<br/>
    • Enable two-factor authentication<br/>
    • Monitor your account regularly<br/>
    • Report suspicious activity immediately<br/>
    • Use secure internet connections for online banking<br/>
    • Keep your contact information updated
    """
    
    elements.append(Paragraph(support_content, styles['BodyText']))
    
    # Build PDF
    doc.build(elements)
    print(f"✅ PDF created successfully: {pdf_file}")
    return pdf_file

if __name__ == "__main__":
    create_banking_pdf()
