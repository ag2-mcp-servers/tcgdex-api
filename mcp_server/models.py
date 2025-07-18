# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T10:16:37+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field, RootModel


class Ability(BaseModel):
    effect: Optional[str] = Field(None, examples=['As often as you like...'])
    name: Optional[str] = Field(None, examples=['Damage Swap'])
    type: Optional[str] = Field(None, examples=['Poke-POWER'])


class Attack(BaseModel):
    cost: Optional[List[str]] = None
    damage: Optional[float] = Field(None, examples=[30])
    effect: Optional[str] = Field(None, examples=['Flip a coin. If heads, ...'])
    name: str = Field(..., examples=['Confuse Ray'])


class Item(BaseModel):
    effect: str
    name: str


class Legal(BaseModel):
    expanded: Optional[bool] = Field(None, examples=[False])
    standard: Optional[bool] = Field(None, examples=[False])


class Variants(BaseModel):
    firstEdition: bool
    holo: bool
    normal: bool
    reverse: bool
    wPromo: bool


class CardResume(BaseModel):
    id: str = Field(..., examples=['base1-1'])
    image: Optional[str] = Field(
        None, examples=['https://assets.tcgdex.net/en/base/base1/1']
    )
    localId: str = Field(..., examples=['1'])
    name: str = Field(..., examples=['Alakazam'])


class SerieResume(BaseModel):
    id: str
    logo: Optional[str] = None
    name: str


class CardCount(BaseModel):
    firstEd: Optional[float] = None
    holo: Optional[float] = None
    normal: Optional[float] = None
    official: float = Field(..., examples=[100])
    reverse: Optional[float] = None
    total: float = Field(..., examples=[101])


class Set(BaseModel):
    cardCount: CardCount
    cards: List[CardResume]
    id: str = Field(..., examples=['base1'])
    logo: Optional[str] = Field(
        None, examples=['https://assets.tcgdex.net/en/base/base1/logo']
    )
    name: str = Field(..., examples=['Base Set'])
    symbol: Optional[str] = Field(
        None, examples=['https://assets.tcgdex.net/univ/base/base1/symbol']
    )


class CardCount1(BaseModel):
    official: float = Field(..., examples=[100])
    total: float = Field(..., examples=[101])


class SetResume(BaseModel):
    cardCount: CardCount1
    id: str = Field(..., examples=['base1'])
    logo: Optional[str] = Field(
        None, examples=['https://assets.tcgdex.net/en/base/base1/logo']
    )
    name: str = Field(..., examples=['Base Set'])
    symbol: Optional[str] = Field(
        None, examples=['https://assets.tcgdex.net/univ/base/base1/symbol']
    )


class StringEndpoint(BaseModel):
    cards: List[CardResume]
    name: str


class WeakRe(BaseModel):
    type: str = Field(..., examples=['Psychic'])
    value: Optional[str] = Field(None, examples=['x2'])


class WeakRes(RootModel[List[WeakRe]]):
    root: List[WeakRe]


class CardsGetResponse(RootModel[List[CardResume]]):
    root: List[CardResume]


class CategoriesGetResponse(RootModel[List[str]]):
    root: List[str]


class DexIdsGetResponse(RootModel[List[str]]):
    root: List[str]


class DexIdsDexIdGetResponse(RootModel[List[CardResume]]):
    root: List[CardResume]


class EnergyTypesGetResponse(RootModel[List[str]]):
    root: List[str]


class EnergyTypesEnergyTypeGetResponse(RootModel[List[CardResume]]):
    root: List[CardResume]


class HpGetResponse(RootModel[List[str]]):
    root: List[str]


class IllustratorsGetResponse(RootModel[List[str]]):
    root: List[str]


class RaritiesGetResponse(RootModel[List[str]]):
    root: List[str]


class RegulationMarksGetResponse(RootModel[List[str]]):
    root: List[str]


class RegulationMarksRegulationMarkGetResponse(RootModel[List[CardResume]]):
    root: List[CardResume]


class RetreatsGetResponse(RootModel[List[str]]):
    root: List[str]


class SeriesGetResponse(RootModel[List[SerieResume]]):
    root: List[SerieResume]


class SetsGetResponse(RootModel[List[SetResume]]):
    root: List[SetResume]


class StagesGetResponse(RootModel[List[str]]):
    root: List[str]


class StagesStageGetResponse(RootModel[List[CardResume]]):
    root: List[CardResume]


class SuffixesGetResponse(RootModel[List[str]]):
    root: List[str]


class SuffixesSuffixGetResponse(RootModel[List[CardResume]]):
    root: List[CardResume]


class TrainerTypesGetResponse(RootModel[List[str]]):
    root: List[str]


class TrainerTypesTrainerTypeGetResponse(RootModel[List[CardResume]]):
    root: List[CardResume]


class TypesGetResponse(RootModel[List[str]]):
    root: List[str]


class TypesTypeGetResponse(RootModel[List[CardResume]]):
    root: List[CardResume]


class VariantsGetResponse(RootModel[List[str]]):
    root: List[str]


class VariantsVariantGetResponse(RootModel[List[CardResume]]):
    root: List[CardResume]


class Card(BaseModel):
    abilities: Optional[List[Ability]] = None
    attacks: Optional[List[Attack]] = None
    category: str = Field(..., examples=['Pokemon'])
    description: Optional[str] = None
    dexId: Optional[List[float]] = None
    energyType: Optional[str] = None
    evolveFrom: Optional[str] = Field(None, examples=['Kadabra'])
    hp: Optional[float] = Field(None, examples=[80])
    id: str = Field(..., examples=['base1-1'])
    illustrator: Optional[str] = Field(None, examples=['Ken Sugimori'])
    image: Optional[str] = Field(
        None, examples=['https://assets.tcgdex.net/en/base/base1/1']
    )
    item: Optional[Item] = None
    legal: Legal
    level: Optional[float] = Field(None, examples=[30])
    localId: str = Field(..., examples=['1'])
    name: str = Field(..., examples=['Alakazam'])
    rarity: str = Field(..., examples=['Rare'])
    regulationMark: Optional[str] = Field(None, examples=['D'])
    resistances: Optional[List[WeakRes]] = None
    retreat: Optional[float] = Field(None, examples=[3])
    set: SetResume
    stage: Optional[str] = Field(None, examples=['Stage2'])
    suffix: Optional[str] = None
    trainerType: Optional[str] = None
    types: Optional[List[str]] = None
    variants: Optional[Variants] = None
    weaknesses: Optional[List[WeakRes]] = None


class Serie(BaseModel):
    id: str
    logo: Optional[str] = None
    name: str
    sets: List[SetResume]
