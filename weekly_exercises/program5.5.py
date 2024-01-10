import sys
temperature=[sys.argv[1:]]

maximum_temperature=max(temperature)
minimum_temperature=min(temperature)
avg_temp=sum(data for data in temperature)/len(temperature)
print(f"Maximum Temperature is :{maximum_temperature}\n Minimum Temperature is :{minimum_temperature}\n Average Temperature is :{avg_temp}")

