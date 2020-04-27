from DNAToolkit import gc_content

with open('data', 'r') as file:
    data = file.read()

data = data.split('>')[1:]
ros_dict = {d[0:13]: d[13:].replace('\n', '') for d in data}
result = {key: gc_content(val) for (key, val) in ros_dict.items()}

max_key = max(result, key=result.get)
print(f'{max_key}\n{result[max_key]}')
