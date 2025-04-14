import sqlite3

class DBManager:
    def __init__(self, db_name='database.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()
        self.insert_sample_data_if_needed()

    def create_tables(self):
        courses = ['accounting', 'marketing', 'finance', 'management', 'economics']
        for course in courses:
            self.conn.execute(f'''
                CREATE TABLE IF NOT EXISTS {course} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    question TEXT NOT NULL,
                    option_a TEXT NOT NULL,
                    option_b TEXT NOT NULL,
                    option_c TEXT NOT NULL,
                    option_d TEXT NOT NULL,
                    correct_option TEXT NOT NULL
                )
            ''')
        self.conn.commit()

    def is_table_empty(self, course):
        cursor = self.conn.execute(f'SELECT COUNT(*) FROM {course}')
        count = cursor.fetchone()[0]
        return count == 0

    def insert_sample_data_if_needed(self):
        sample_questions = {
            'accounting': [
                ("What is the main financial statement that shows a company's financial position?", "Income Statement", "Balance Sheet", "Cash Flow", "Retained Earnings", "B"),
                ("What is depreciation?", "Paying off debt", "Value loss of assets", "Tax on income", "A cost increase", "B"),
                ("Which method records income when earned, not when cash is received?", "Cash Basis", "Accrual Basis", "Modified Cash", "Hybrid", "B"),
                ("What is an example of a liability?", "Office Supplies", "Accounts Payable", "Sales Revenue", "Prepaid Rent", "B"),
                ("The matching principle matches expenses with what?", "Assets", "Revenue", "Inventory", "Cash", "B"),
                ("Which account is an asset?", "Accounts Receivable", "Accounts Payable", "Revenue", "Common Stock", "A"),
                ("What is the purpose of closing entries?", "To calculate profit", "To reset temporary accounts", "To balance the trial balance", "To avoid tax", "B"),
                ("What is retained earnings?", "Owner investment", "Total revenue", "Undistributed profits", "Gross profit", "C"),
                ("What does GAAP stand for?", "General Accepted Accounting Plans", "Generally Accepted Accounting Principles", "Government Approved Accounting Practices", "Gross Annual Accounting Principles", "B"),
                ("Which document shows cash inflows and outflows?", "Balance Sheet", "Income Statement", "Cash Flow Statement", "Equity Statement", "C"),
            ],
            'marketing': [
                ("What is the 4th P in marketing?", "Product", "Price", "Place", "Promotion", "D"),
                ("Market segmentation divides a market into?", "Profits", "Groups", "Goals", "Processes", "B"),
                ("What does brand loyalty mean?", "Customer regularly buys same brand", "Customer dislikes new products", "Switches often", "Avoids shopping", "A"),
                ("What is the goal of promotion?", "Lower cost", "Attract talent", "Raise awareness", "Set prices", "C"),
                ("What is a target market?", "Any customer", "A competitor", "A specific group of potential customers", "The mass market", "C"),
                ("Which is a pricing strategy?", "Public Relations", "Skimming", "Budgeting", "Advertising", "B"),
                ("The main goal of advertising is to?", "Cut costs", "Influence behavior", "Control quality", "Reduce staff", "B"),
                ("Which medium is traditional advertising?", "Instagram", "Email", "TV Commercial", "SEO", "C"),
                ("A product's perceived value is influenced by?", "Features only", "Price only", "Promotion", "All of the above", "D"),
                ("Which is NOT a distribution channel?", "Retailer", "Wholesaler", "Consumer", "Advertiser", "D"),
            ],
            'finance': [
                ("What does ROI stand for?", "Return on Investment", "Rate of Interest", "Ratio of Income", "Revenue of Investment", "A"),
                ("Time value of money means?", "Money gains interest", "Money is better now than later", "Money depreciates", "Time is money", "B"),
                ("What is an example of a liability?", "Savings", "Loan", "Stock", "Dividend", "B"),
                ("What is diversification?", "Putting all money in one asset", "Spreading investments", "Saving money", "Paying debt", "B"),
                ("What is a bond?", "Equity investment", "Debt instrument", "Loan request", "Stock option", "B"),
                ("Which is a type of financial statement?", "Cash flow", "Price list", "Balance check", "Invoice", "A"),
                ("Compound interest means?", "Interest only on principal", "No interest", "Interest on interest", "Simple savings", "C"),
                ("What is net income?", "Revenue - Expenses", "Gross Sales", "Taxes only", "Equity", "A"),
                ("What does a credit score indicate?", "Income level", "Spending habits", "Debt ratio", "Creditworthiness", "D"),
                ("The role of a financial manager includes?", "Hiring", "Branding", "Risk management", "Auditing", "C"),
            ],
            'management': [
                ("Who is known as the Father of Modern Management?", "Peter Drucker", "Elton Mayo", "Henry Ford", "Steve Jobs", "A"),
                ("What is the first function of management?", "Controlling", "Planning", "Leading", "Staffing", "B"),
                ("Organizing involves?", "Budgeting", "Structuring roles", "Scheduling ads", "Developing products", "B"),
                ("Controlling in management refers to?", "Micromanaging", "Measuring performance", "Delegating", "Rewarding", "B"),
                ("Which is a leadership style?", "Democratic", "Competitive", "Academic", "Profit-based", "A"),
                ("What does SWOT stand for?", "Sales, Worth, Output, Trade", "Strengths, Weaknesses, Opportunities, Threats", "Systems, Work, Objectives, Team", "Strategy, Workforce, Organization, Tactics", "B"),
                ("Which is NOT a function of management?", "Planning", "Directing", "Accounting", "Controlling", "C"),
                ("What is strategic planning?", "Short-term goals", "Marketing budget", "Long-term objectives", "Hiring plan", "C"),
                ("Delegation means?", "Avoiding work", "Assigning tasks", "Planning events", "Taking control", "B"),
                ("A manager who motivates is using which function?", "Planning", "Organizing", "Leading", "Controlling", "C"),
            ],
            'economics': [
                ("Scarcity refers to?", "Too much demand", "Limited resources", "Abundant supply", "Overproduction", "B"),
                ("Opportunity cost is?", "The price of the next-best choice", "Loss of income", "Cost of debt", "Tax paid", "A"),
                ("Supply and demand determine?", "Advertising", "Stock prices", "Market equilibrium", "Tax rate", "C"),
                ("What is inflation?", "Decrease in prices", "Increase in prices", "Steady economy", "Trade surplus", "B"),
                ("Which is a type of economic system?", "Democratic", "Mixed economy", "Capital reserve", "Profit-based", "B"),
                ("A market economy is controlled by?", "Government", "Military", "Private citizens", "Nonprofits", "C"),
                ("GDP stands for?", "Gross Domestic Product", "Government Development Plan", "Global Data Points", "Gross Debt Payments", "A"),
                ("Which is a microeconomic concept?", "GDP", "National debt", "Consumer choice", "Inflation", "C"),
                ("What is fiscal policy?", "Control of money supply", "Government taxing/spending", "Interest rate policy", "Stock trading", "B"),
                ("What is a recession?", "Economic boom", "Temporary economic decline", "Global crash", "Stock increase", "B"),
            ]
        }

        for course, questions in sample_questions.items():
            if self.is_table_empty(course):
                for question_data in questions:
                    self.add_question(course, question_data)

    def add_question(self, course, question_data):
        self.conn.execute(f'''
            INSERT INTO {course} (question, option_a, option_b, option_c, option_d, correct_option)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', question_data)
        self.conn.commit()

    def get_questions(self, course):
        cursor = self.conn.execute(f'SELECT * FROM {course}')
        return cursor.fetchall()

    def delete_question(self, course, question_id):
        self.conn.execute(f'DELETE FROM {course} WHERE id = ?', (question_id,))
        self.conn.commit()

    def update_question(self, course, question_id, question_data):
        self.conn.execute(f'''
            UPDATE {course}
            SET question = ?, option_a = ?, option_b = ?, option_c = ?, option_d = ?, correct_option = ?
            WHERE id = ?
        ''', (*question_data, question_id))
        self.conn.commit()
