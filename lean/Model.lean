
inductive Bean where
  | CommonBean | FrenchBean | KidneyBean | LimaBean | BlackBean
deriving Repr, DecidableEq

inductive Pest where
  | Aphid | BeanWeevil | Whitefly | SpiderMite | Cutworm | LeafMiner | Thrip | BeanLeafBeetle
deriving Repr, DecidableEq

inductive Pesticide where
  | NeemOil | Pyrethrin | BT | DiatomaceousEarth | InsecticidalSoap | Permethrin | Azadirachtin
deriving Repr, DecidableEq

-- Predicates
def Infests : Pest → Bean → Prop := fun _ _ => Prop
def Controls : Pesticide → Pest → Prop := fun _ _ => Prop
def Safe : Pesticide → Bean → Prop := fun _ _ => Prop
def NotSafe : Pesticide → Bean → Prop := fun _ _ => Prop
def Effective : Pesticide → Bean → Prop := fun _ _ => Prop
def BroadSpectrum : Pesticide → Prop := fun _ => Prop
def HardToManage : Pest → Prop := fun _ => Prop
