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
    if "leave" in topic:
        return HR_POLICIES["leave"]
    elif "wfh" in topic or "work from home" in topic or "remote" in topic:
        return HR_POLICIES["wfh"]
    elif "salary" in topic or "pay" in topic or "benefit" in topic:
        return HR_POLICIES["salary"]
    elif "onboard" in topic or "join" in topic or "new" in topic:
        return HR_POLICIES["onboarding"]
    else:
        return "I'm not sure about that policy. Please contact HR at hr@company.com for details."