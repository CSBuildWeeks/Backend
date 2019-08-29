from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

r_outside = Room(title="Outside Cave Entrance",
               description="North of you, the cave mount beckons")

r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
passages run north and east.""")

r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_bedroom = Room(title="Bedroom", description="""You've found the bedroom, feel free to take a nap or take the 
exits to the East or North.""")

r_study= Room(title="Study", description="""You've found the study, no treasure here but there are plenty of books and
exits to the South and East.""")

r_office = Room(title="Office", description="""You've walked into the office. Take a look around and see what you can find,
 there is no treasure so continue East or take your chances and see whats up North""")

r_attic = Room(title="Attic", description="""You've choosen North and reached the Attic, something is shining in the back corner.
You walk over to see what it could be...... Congrats, You've found the long lost treasure! The only exit is South""")

r_closet = Room(title="closet", description="""You've walked right into a closet! It's dark and cold. 
There is nothing in here, go back West in search of the treasure""")

r_outside.save()
r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()
r_bedroom.save()
r_study.save()
r_office.save()
r_attic.save()
r_closet.save()

# Link rooms together
r_outside.connectRooms(r_foyer, "n")
r_foyer.connectRooms(r_outside, "s")

r_foyer.connectRooms(r_overlook, "n")
r_overlook.connectRooms(r_foyer, "s")

r_foyer.connectRooms(r_narrow, "e")
r_narrow.connectRooms(r_foyer, "w")

r_narrow.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_narrow, "s")

r_overlook.connectRooms(r_bedroom, "w")
r_bedroom.connectRooms(r_overlook,"e")

r_bedroom.connectRooms(r_study, "n")
r_study.connectRooms(r_bedroom, "s")

r_study.connectRooms(r_office, "w")
r_office.connectRooms(r_study, "e")

r_office.connectRooms(r_attic, "n")
r_attic.connectRooms(r_office, "s")

r_office.connectRooms(r_closet, "e")
r_closet.connectRooms(r_office, "w")




players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

