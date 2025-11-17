# First-Order Logic Rules

## Rule 1: Effectiveness Rule
∀ p ∀ x ∀ b:
(Controls(p, x) ∧ Infests(x, b)) → Effective(p, b)

## Rule 2: Safety Rule
∀ p ∀ b:
NotSafe(p, b) → ¬Effective(p, b)

## Rule 3: Broad-Spectrum Rule
∀ p:
(∃x ∃y (Controls(p, x) ∧ Controls(p, y) ∧ x ≠ y)) → BroadSpectrum(p)

## Rule 4: Hard-to-Manage Pests
∀x:
(¬∃p Controls(p, x)) → HardToManage(x)
