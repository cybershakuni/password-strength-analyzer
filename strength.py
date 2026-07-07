import re
import math

def calculate_entropy(password):
    """Calculate password entropy in bits"""
    charset_size = 0
    if re.search(r'[a-z]', password): charset_size += 26
    if re.search(r'[A-Z]', password): charset_size += 26
    if re.search(r'[0-9]', password): charset_size += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): charset_size += 32
    
    if charset_size == 0:
        return 0
    return round(len(password) * math.log2(charset_size), 2)

def check_strength(password):
    """Analyze password strength"""
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 8: score += 1
    if len(password) >= 12: score += 1
    if len(password) >= 16: score += 1
    else: feedback.append("❌ Use at least 12 characters")
    
    # Character diversity
    if re.search(r'[a-z]', password): score += 1
    else: feedback.append("❌ Add lowercase letters")
    if re.search(r'[A-Z]', password): score += 1
    else: feedback.append("❌ Add uppercase letters")
    if re.search(r'[0-9]', password): score += 1
    else: feedback.append("❌ Add numbers")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): score += 1
    else: feedback.append("❌ Add special characters")
    
    # Common patterns
    common = ['password', '12345', 'qwerty', 'admin', 'welcome']
    if any(p in password.lower() for p in common):
        feedback.append("❌ Avoid common words like 'password', '12345'")
        score -= 2
    else:
        score += 1
    
    # Final rating
    if score <= 3: rating = "🔴 WEAK"
    elif score <= 5: rating = "🟡 MODERATE"
    elif score <= 7: rating = "🟢 STRONG"
    else: rating = "💪 VERY STRONG"
    
    entropy = calculate_entropy(password)
    return {
        "rating": rating,
        "score": score,
        "entropy": entropy,
        "feedback": feedback
    }
