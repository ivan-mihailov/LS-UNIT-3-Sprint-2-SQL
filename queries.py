import sqlite3

conn = sqlite3.connect('rpg_db (1).sqlite3')
cur = conn.cursor()

""" Calculate how many total characters are in the database. """
TOTAL_CHARACTERS = "SELECT count(*) FROM charactercreator_character;"
print(f'TOTAL_CHARACTERS: {cur.execute(TOTAL_CHARACTERS).fetchone()[0]}')

""" 
Calculate how many total characters from each specific subclass are in the 
database. 
"""
TOTAL_CLERIC = "SELECT count(*) FROM charactercreator_cleric;"
TOTAL_FIGHTER = "SELECT count(*) FROM charactercreator_fighter;"
TOTAL_MAGE = "SELECT count(*) FROM charactercreator_mage;"
TOTAL_NECRO = "SELECT count(*) FROM charactercreator_necromancer;"
TOTAL_THIEF = "SELECT count(*) FROM charactercreator_thief;"
TOTAL_SUBCLASS = ((cur.execute(TOTAL_CLERIC).fetchone()[0])\
                  + (cur.execute(TOTAL_FIGHTER).fetchone()[0])\
                  + (cur.execute(TOTAL_MAGE).fetchone()[0])\
                  + (cur.execute(TOTAL_NECRO).fetchone()[0])\
                  + (cur.execute(TOTAL_THIEF).fetchone()[0]))
print(f'Total of All Subclasses (incl. 11 Mages who are\
 also Necromancers): {TOTAL_SUBCLASS}')

""" Calculates how many total items are in the database. """

TOTAL_ITEMS = "SELECT count(*) FROM armory_item"
print(f'TOTAL_ITEMS: {cur.execute(TOTAL_ITEMS).fetchone()[0]}')

""" Calculates how many of the items in the database are weapons. """

TOTAL_WEAPONS = "SELECT count(*) FROM armory_weapon"
print(f'TOTAL_WEAPONS: {cur.execute(TOTAL_WEAPONS).fetchone()[0]}')

""" Calculates how many of the items are not weapons. """

NON_WEAPONS = "SELECT count(item_id) FROM (SELECT ai.* FROM armory_item\
                                        as ai LEFT JOIN armory_weapon\
                                        as aw ON ai.item_id\
                                        = aw.item_ptr_id WHERE\
                                        aw.item_ptr_id IS NULL);"
print(f'NON_WEAPONS: {cur.execute(NON_WEAPONS).fetchone()[0]}')

""" Calculate how many items each character has and return first 20 rows. """

CHARACTER_ITEMS = "SELECT character_id, count(item_id)\
                FROM charactercreator_character_inventory\
                GROUP BY character_id;"
print(f'CHARACTER_ITEMS: {cur.execute(CHARACTER_ITEMS).fetchmany(20)}')

""" Calculate how many Weapons each character has and return first 20 rows."""

CHARACTER_WEAPONS = "SELECT character_id, count(item_id)\
                    FROM charactercreator_character_inventory as chi\
                    JOIN armory_weapon as aw ON chi.item_id\
                    =aw.item_ptr_id GROUP BY character_id;"
print(f'CHARACTER_WEAPONS: \
    {cur.execute(CHARACTER_WEAPONS).fetchmany(20)}')

"""Calculate, on average, how many items each character has. """

AVG_CHARACTER_ITEMS = "SELECT ROUND(avg(ci), 2)\
                      FROM (SELECT count(item_id) as ci\
                            FROM charactercreator_character_inventory\
                            GROUP BY character_id);"
print(f'AVGE_CHARACTER_ITEMS: \
    {cur.execute(AVG_CHARACTER_ITEMS).fetchone()[0]}')

""" Calculate, on average, how many Weapons each character has. """

AVG_CHARACTER_WEAPONS = "SELECT ROUND(avg(cw), 2)\
                        FROM (SELECT count(item_id) as cw\
                            FROM charactercreator_character_inventory\
                            as chi JOIN armory_weapon as aw\
                            ON chi.item_id=aw.item_ptr_id\
                            GROUP BY character_id);"
print(f'AVGE_CHARACTER_WEAPONS: \
    {cur.execute(AVG_CHARACTER_WEAPONS).fetchone()[0]}')

conn.close()