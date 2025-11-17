# First-Order Logic Facts

## Infestation Facts
Infests(Aphid, CommonBean)
Infests(Aphid, FrenchBean)
Infests(Whitefly, FrenchBean)
Infests(BeanWeevil, KidneyBean)
Infests(SpiderMite, CommonBean)
Infests(Thrip, LimaBean)

## Control Facts
Controls(NeemOil, Aphid)
Controls(Pyrethrin, Whitefly)
Controls(BT, Cutworm)
Controls(InsecticidalSoap, SpiderMite)
Controls(DiatomaceousEarth, BeanWeevil)

## Safety Facts
Safe(NeemOil, CommonBean)
Safe(NeemOil, FrenchBean)
Safe(NeemOil, KidneyBean)
Safe(NeemOil, LimaBean)
Safe(NeemOil, BlackBean)

NotSafe(Permethrin, LimaBean)
