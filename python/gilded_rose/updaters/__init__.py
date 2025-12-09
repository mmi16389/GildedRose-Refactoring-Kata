# updaters/__init__.py
from .base import ItemUpdater, is_conjured
from .standard import StandardItemUpdater
from .aged_brie import AgedBrieUpdater
from .sulfuras import SulfurasUpdater
from .backstage import BackstagePassUpdater
from .conjured import ConjuredItemUpdater


SPECIAL_UPDATERS: dict[str, ItemUpdater] = {
    "Aged Brie": AgedBrieUpdater(),
    "Sulfuras, Hand of Ragnaros": SulfurasUpdater(),
    "Backstage passes to a TAFKAL80ETC concert": BackstagePassUpdater(),
}


def get_updater_for(item) -> ItemUpdater:
    if item.name in SPECIAL_UPDATERS:
        return SPECIAL_UPDATERS[item.name]

    if is_conjured(item):
        return ConjuredItemUpdater()

    return StandardItemUpdater()


__all__ = [ "get_updater_for", 
           "ItemUpdater", 
           "StandardItemUpdater", 
           "AgedBrieUpdater", 
           "SulfurasUpdater", 
           "BackstagePassUpdater", 
           "ConjuredItemUpdater" 
           ]