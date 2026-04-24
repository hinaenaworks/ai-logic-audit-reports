# Audit Checklist: Hinaena-Audit-Protocol (HAP-v1)

本ドキュメントは、AI生成コードおよびAPI実装における論理的脆弱性を排除するための標準監査チェックリストである。各フェーズにおいて「期待される仕様」と「実装」の論理的不整合を検証する。

## Phase 1: Input/Output Integrity (スキーマ整合性)
AI生成コードがAPI仕様書（OpenAPI/Swagger）の制約を遵守しているかを確認する。
- [ ] **Data Type Validation:** 仕様書で定義された型制約がコードレベルでバリデーションされているか。
- [ ] **Required Fields:** 必須パラメータの欠落チェックが実装されているか。
- [ ] **Enum Constraint:** 定義外の不正な値が許容されていないか。

## Phase 2: State Consistency (状態遷移の整合性)
ビジネスロジックの根幹である「状態遷移」の論理破綻を検証する。
- [ ] **Transition Rule:** 未定義の状態遷移（例: キャンセル→処理中）がコードレベルでブロックされているか。
- [ ] **State Lockdown:** 最終ステータス（完了・無効化）到達後の更新が適切に制御されているか。
- [ ] **Context Switching:** コンテキストに応じた正しい状態遷移が保証されているか。

## Phase 3: Data Integrity & Concurrency (データ整合性と並行性)
リクエストの重複や競合に対する耐性を検証する。
- [ ] **Idempotency Verification:** 同一リクエストの多重処理に対する保護ロジック（冪等性）が実装されているか。
- [ ] **Race Condition Check:** 並行リクエストに対してトランザクションが整合性を保っているか。
- [ ] **Atomic Operation:** 処理が中断された際、データが不整合な状態で放置されないか（ロールバックの論理）。

## Phase 4: Security & Error Handling (セキュリティと例外処理)
エラー発生時のシステム挙動を検証する。
- [ ] **Error Exposure:** エラーメッセージに機密情報や詳細なスタックトレースが含まれていないか。
- [ ] **Fallback Mechanism:** 例外発生時に、システムが安全な状態（Fail-safe）へ遷移するか。

---
**Audited by:** Designer_Hinaena_V12.30
