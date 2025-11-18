import ./Model
import ./Facts
import ./Rules

-- Example Proof: Neem Oil is effective for Common Bean
theorem neem_effective_common :
  Effective Pesticide.NeemOil Bean.CommonBean :=
  rule_effective Pesticide.NeemOil Pest.Aphid Bean.CommonBean
    neem_aphid
    aphids_common

-- Example Proof: Permethrin is not effective for Lima Bean
theorem permethrin_not_effective :
  ¬ Effective Pesticide.Permethrin Bean.LimaBean :=
  rule_not_safe Pesticide.Permethrin Bean.LimaBean
    permethrin_not_safe
