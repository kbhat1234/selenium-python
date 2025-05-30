cities = ["delhi", "mumbai", "bangalore", "kolkata", "chennai"]
heroes = ["aunty no.1", "biwi no.1", "saali no.1", "baap no.1"]
print(len(cities))
print(len(heroes))

def print_len(list):
    print(f'cities list is {len(list)}')

def prt_len(list):
    return len(list)

def func_list(list):
    for item in list:
        print(item, end=" ")
        

print_len(cities)
her = prt_len(heroes)
print(f'Film list is {her}')
func_list(cities)