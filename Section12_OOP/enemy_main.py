#!/usr/bin/env python3

from enemy import Enemy, Troll, Vampyre, VampyreKing

# random_monster = Enemy("Basic enemy", 12, 1)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)
#
# random_monster.take_damage(8)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)

# ugly_troll = Troll("Pug")
# print("Ugly troll - {}".format(ugly_troll))
#
# another_troll = Troll("Ug")
# print(another_troll)
#
# brother_troll = Troll("Urg")
# print(brother_troll)
#
# ugly_troll.grunt()
# another_troll.grunt()
# brother_troll.grunt()

# ugly_troll.take_damage(22)
# print(ugly_troll)
#
# ugly_troll.take_damage(5)
# print(ugly_troll)

# blood_vampyre = Vampyre("Vlad")
# print(blood_vampyre)
#
# while blood_vampyre._alive:
#     blood_vampyre.take_damage(4)
#     print(blood_vampyre)

king = VampyreKing("Dracul")
print(king)

king.take_damage(40)
print(king)
