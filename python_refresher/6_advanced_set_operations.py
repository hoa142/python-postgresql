friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad) #Rolf
local_freinds = abroad.difference(friends) #set()

local = {"Rolf"}
abroad = {"Bob", "Anne"}
friends = local.union(abroad) #{'Anne', 'Bob', 'Rolf'}


art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science) #{'Bob', 'Jen'}
