from time import perf_counter

def replace( filename, substr, new_substr):
    print(f'process {filename}')
    with open(filename, 'r') as f:
        content = f.read()
    content = content.replace(substr, new_substr)
    
    with open(filename, 'w') as f:
        f.write(content)


def main():
    filenames = []
    for i in range(1, 11):
        filenames.append(f'test{str(i)}.json')
        
    for filename in filenames:
        replace(filename, "Отопление", "Жара")


start_time = perf_counter()
main()
end_time = perf_counter()

print(f'Time taken: {end_time-start_time: 0.6f} seconds')
