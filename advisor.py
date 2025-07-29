def advise_user(goal):
    goal = goal.lower()
    if "save" in goal:
        return "✅ Consider Money Market Funds or Treasury Bills for short-term savings."
    elif "long term" in goal:
        return "📈 Consider a mix of NSE stocks and government bonds."
    elif "loan" in goal:
        return "💡 Compare bank rates before taking a loan. Try secured options first."
    else:
        return "🤔 Try diversifying between low-risk and high-return assets."
