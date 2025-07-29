def advise_user(goal):
    goal = goal.lower()
    if 'save' in goal:
        return '✅ Try Money Market Funds or Treasury Bills.'
    elif 'long' in goal or 'retire' in goal:
        return '📈 Consider a mix of stocks and bonds for long-term growth.'
    elif 'loan' in goal:
        return '💡 Compare interest rates from banks and MMFs before borrowing.'
    else:
        return '🤔 Consider diversifying: low-risk savings + stocks for higher returns.'
