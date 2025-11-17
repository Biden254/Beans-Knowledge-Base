import ./Model

-- Infestation Facts
axiom aphids_common : Infests Pest.Aphid Bean.CommonBean
axiom aphids_french : Infests Pest.Aphid Bean.FrenchBean
axiom whitefly_french : Infests Pest.Whitefly Bean.FrenchBean
axiom weevil_kidney : Infests Pest.BeanWeevil Bean.KidneyBean
axiom mite_common : Infests Pest.SpiderMite Bean.CommonBean
axiom thrip_lima : Infests Pest.Thrip Bean.LimaBean

-- Control Facts
axiom neem_aphid : Controls Pesticide.NeemOil Pest.Aphid
axiom pyrethrin_whitefly : Controls Pesticide.Pyrethrin Pest.Whitefly
axiom bt_cutworm : Controls Pesticide.BT Pest.Cutworm
axiom soap_mite : Controls Pesticide.InsecticidalSoap Pest.SpiderMite
axiom de_weevil : Controls Pesticide.DiatomaceousEarth Pest.BeanWeevil

-- Safety Facts
axiom neem_safe_common : Safe Pesticide.NeemOil Bean.CommonBean
axiom neem_safe_french : Safe Pesticide.NeemOil Bean.FrenchBean
axiom neem_safe_kidney : Safe Pesticide.NeemOil Bean.KidneyBean
axiom neem_safe_lima : Safe Pesticide.NeemOil Bean.LimaBean
axiom neem_safe_black : Safe Pesticide.NeemOil Bean.BlackBean

axiom permethrin_not_safe : NotSafe Pesticide.Permethrin Bean.LimaBean
