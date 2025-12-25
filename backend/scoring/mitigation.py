def calculate_mitigation(protections: list) -> float:
    """
    Calculates mitigation factor (0.0 - 0.999).
    Never 1.0 (Zero Trust).
    
    Weights:
    - Hardware Key (YubiKey): 0.95
    - App TOTP (Authy/Google): 0.85
    - SMS 2FA: 0.60
    - Complex Password (Unique): +0.3 (Additive wrapper)
    """
    base_mitigation = 0.0
    
    # Strongest 2FA overrides weaker ones usually, but let's take max
    if "hardware_key" in protections:
        base_mitigation = max(base_mitigation, 0.95)
    elif "2fa_app" in protections:
        base_mitigation = max(base_mitigation, 0.85)
    elif "2fa_sms" in protections:
        base_mitigation = max(base_mitigation, 0.60)
        
    # Additional layers (Defense in Depth)
    if "unique_password" in protections:
        # If no 2FA, password is main defense. If 2FA, it adds residual cover.
        # We apply remaining risk reduction: current + (1-current)*0.5
        residual = 1.0 - base_mitigation
        base_mitigation += (residual * 0.5) 
        
    return min(base_mitigation, 0.99)
