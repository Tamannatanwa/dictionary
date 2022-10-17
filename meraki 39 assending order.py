dt={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
sorted_dt = {key: value for key, value in sorted(dt.items(), key=lambda item: item[1])}
print(sorted_dt)
sorted_dt = {key: value for key, value in reversed(sorted(dt.items(), key=lambda item: item[1]))}
print(sorted_dt)












