import re
import tldextract

def analyze_url(url):
    """
    วิเคราะห์ URL และประเมินความเสี่ยง
    """
    risk_score = 0

    # ตรวจสอบว่ามี HTTPS หรือไม่
    if not url.startswith("https://"):
        risk_score += 1

    # ตรวจสอบความยาวของ URL
    if len(url) > 75:
        risk_score += 1

    # วิเคราะห์โดเมนย่อย
    domain_info = tldextract.extract(url)
    if domain_info.subdomain:
        risk_score += 1

    # ตรวจสอบคำต้องสงสัยใน URL
    suspicious_keywords = ["login", "secure", "verify", "account", "update"]
    for keyword in suspicious_keywords:
        if keyword in url.lower():
            risk_score += 2

    # ประเมินความเสี่ยง
    if risk_score >= 5:
        return {"level": "สูง", "color": "red", "description": "เว็บไซต์นี้มีความเสี่ยงสูง กรุณาหลีกเลี่ยงการใช้งาน"}
    elif 3 <= risk_score < 5:
        return {"level": "ปานกลาง", "color": "orange", "description": "เว็บไซต์นี้มีความเสี่ยงปานกลาง กรุณาระมัดระวัง"}
    else:
        return {"level": "ต่ำ", "color": "green", "description": "เว็บไซต์นี้มีความเสี่ยงต่ำ สามารถเข้าใช้งานได้ปกติ"}
