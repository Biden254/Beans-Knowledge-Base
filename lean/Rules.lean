import ./Model

-- Rule 1: Effectiveness rule
axiom rule_effective :
  ∀ p x b, Controls p x → Infests x b → Effective p b

-- Rule 2: Safety rule
axiom rule_not_safe :
  ∀ p b, NotSafe p b → ¬ Effective p b

-- Rule 3: Broad-spectrum rule
axiom rule_broad :
  ∀ p, (∃x y, Controls p x ∧ Controls p y ∧ x ≠ y) → BroadSpectrum p

-- Rule 4: Hard-to-manage pests
axiom rule_hard :
  ∀ x, (¬ ∃p, Controls p x) → HardToManage x
