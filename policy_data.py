# policy_data.py - HR Policy Knowledge Base

HR_POLICIES = {
    "leave": """
    📅 Leave Policy:
    • Casual Leave: 12 days per year
    • Sick Leave: 6 days per year
    • Earned Leave: 15 days per year
    • Leave must be applied 24 hours in advance
    • Max 3 consecutive casual leaves without manager approval
    """,
    
    "wfh": """
    🏠 Work From Home Policy:
    • WFH requests must be submitted via HR portal
    • Minimum 24 hours notice required
    • Max 2 WFH days per week
    • Manager approval mandatory
    • Core hours (10 AM - 4 PM) must be online
    """,
    
    "salary": """
    💰 Salary & Benefits:
    • Salary credited on 1st of every month
    • PF deduction: 12% of basic salary
    • Health insurance for employee + family
    • Annual bonus based on performance
    • Reimbursement for internet (WFH): ₹500/month
    """,
    
    "onboarding": """
    🎉 New Joiner Onboarding:
    • Day 1: ID card, laptop, access setup
    • Week 1: Team introductions + training
    • Month 1: Probation review
    • Buddy assigned for first 30 days
    • HR orientation session on Day 2
    """
}

def get_policy(topic: str) -> str:
    """Retrieve policy based on topic keyword"""
    topic = topic.lower()
    
    # Leave keywords
    if any(word in topic for word in ["leave", "vacation", "time off", "casual", "sick", "earned"]):
        return HR_POLICIES["leave"]
    
    # WFH keywords
    if any(word in topic for word in ["wfh", "work from home", "remote", "home office", "work remotely"]):
        return HR_POLICIES["wfh"]
    
    # Salary keywords
    if any(word in topic for word in ["salary", "pay", "payment", "benefit", "allowance", "pf", "bonus", "insurance"]):
        return HR_POLICIES["salary"]
    
    # Onboarding keywords
    if any(word in topic for word in ["onboard", "join", "new", "first day", "probation", "buddy", "orientation"]):
        return HR_POLICIES["onboarding"]
    
    # Fallback for unknown topics
    return "I'm not sure about that policy. Please contact HR at hr@company.com for details."