#/usr/bin python3
import re, time

file = 'output_1981.10.21.txt'
pattern = r'\d{4}.\d{2}.\d{2}'
time_str = re.search(pattern, file).group()
print(time_str)

new_time = time.strptime(time_str, "%Y.%m.%d")
#print(new_time)

new_file = '%s-%s-%s-%s' %(new_time.tm_year,new_time.tm_mon, new_time.tm_mday, new_time.tm_wday + 1)

print(new_file)

