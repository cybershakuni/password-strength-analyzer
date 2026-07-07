import hashlib
import requests

def check_breach(password):
    """Check if password has been leaked using HIBP API (k-Anonymity)"""
    
    # Step 1: Hash the password with SHA-1
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
    # Step 2: Split hash into prefix (first 5 chars) and suffix
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]
    
    # Step 3: Send prefix to HIBP API
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return {"error": "Could not reach breach database"}
        
        # Step 4: Search suffix in response
        for line in response.text.splitlines():
            hash_suffix, count = line.split(":")
            if hash_suffix == suffix:
                return {
                    "breached": True,
                    "count": int(count),
                    "message": f"⚠️  Found in {int(count):,} data breaches!"
                }
        
        return {
            "breached": False,
            "count": 0,
            "message": "✅ Not found in any known breach"
        }
    
    except Exception as e:
        return {"error": str(e)}
