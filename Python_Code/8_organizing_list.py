#Organizing List

#permanent sort

must_visit = ['st augustine','st-diego','miami','new york', 'home']

print(must_visit)
#using sorted --> temporary sorting, original list is unchanged.
print(sorted(must_visit))
#original list
print(must_visit)
#using reverse method to change order
must_visit.reverse() # makes original list as reversed.
print(must_visit)
must_visit.reverse()
print(must_visit)
must_visit.sort()
print(must_visit)
must_visit.sort(reverse=True)
print(must_visit)
print(len(must_visit))
