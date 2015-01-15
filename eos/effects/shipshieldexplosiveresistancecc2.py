# shipShieldExplosiveResistanceCC2
#
# Used by:
# Variations of ship: Moa (3 of 4)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Cruiser").level
    fit.ship.boostItemAttr("shieldExplosiveDamageResonance", ship.getModifiedItemAttr("shipBonusCC2") * level)
