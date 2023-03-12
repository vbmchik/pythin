from threading import Thread
from time import perf_counter


def replace(filename, substr, new_substr):
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
    threads = [Thread(target=replace, args=(filename, "Отопление", "Жара")) for filename in filenames]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    

start_time = perf_counter()
main()
end_time = perf_counter()

print(f'Time taken: {end_time-start_time: 0.6f} seconds')
