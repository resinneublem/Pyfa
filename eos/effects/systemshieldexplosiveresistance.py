# Used by:
# Celestials named like: Wolf Rayet Beacon (6 of 6)
runTime = "early"
type = ("projected", "offline")
def handler(fit, beacon, context):
    fit.ship.boostItemAttr("shieldExplosiveDamageResonance", beacon.getModifiedItemAttr("shieldExplosiveDamageResistanceBonus"),
                           stackingPenalties = True)