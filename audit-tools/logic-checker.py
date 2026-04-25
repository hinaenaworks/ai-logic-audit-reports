# logic-checker.py
# 簡易的な状態遷移検証ツール (Proof of Concept)

# 許可された遷移ルール
VALID_TRANSITIONS = {
    'PENDING': ['PROCESSING', 'CANCELLED'],
    'PROCESSING': ['COMPLETED', 'CANCELLED']
}

def check_transition(current_status, next_status):
    if current_status == next_status:
        return True # 変更なしは許容
    
    allowed = VALID_TRANSITIONS.get(current_status, [])
    if next_status in allowed:
        return True
    return False

# テスト実行
if __name__ == "__main__":
    test_cases = [
        ('PENDING', 'PROCESSING'),   # OK
        ('CANCELLED', 'PROCESSING')  # NG (論理欠陥)
    ]
    
    for curr, next_ in test_cases:
        if check_transition(curr, next_):
            print(f"[PASS] {curr} -> {next_}")
        else:
            print(f"[FAIL] {curr} -> {next_} (不正な遷移)")
