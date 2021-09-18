import os
import time

# clear screen after each progress
# os.system('cls' if os.name == 'nt' else 'clear')


class ProgressBar():
    def __init__(self, processes, bar_length=50, prefix='Progress', sufix='Complete') -> None:
        """
    terminal progress bar
    @params:
        processes   - Required  : number of iterations (Int)
        bar_length  - Required  : character length of bar (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
    """
        self.fill = '█'
        self.empty_bar = ''
        self.full_bar_length = bar_length
        self.prefix = prefix
        self.sufix = sufix
        self.completion = 0
        self.processes = processes
        self.fill_per_process = self.full_bar_length // self.processes
        self.percentage_per_process = 100 / self.processes
        self.scale()

    def scale(self):
        """determine fill increment"""
        fill_increment = ''
        for i in range(self.fill_per_process):
            fill_increment += self.fill
        return fill_increment

    def update(self):
        """update bar"""
        self.empty_bar += self.scale()
        self.completion += self.percentage_per_process
        print(
            f'|{self.prefix}: |{self.empty_bar}| {round(self.completion)}% {self.sufix}')
        time.sleep(1)


#####--------------------------------------- Sample usage---------------------------------------#####

fruit_list = ['apple', 'banana', 'orange',
              'papaya', 'pineapple', 'strawberry', 'coconut']

# Instanciate progress bar
progress_bar = ProgressBar(processes=len(fruit_list), bar_length=50)
os.system('cls' if os.name == 'nt' else 'clear')

# 0% complete
print("Strating process...")
print(
    f'|Progress: |{progress_bar.empty_bar}| {progress_bar.completion}% Complete')
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

# print each fruit while monitoring progress
for item in fruit_list:
    print(item)
    progress_bar.update()
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
print(
    f'|Progress: |{progress_bar.empty_bar}| {round(progress_bar.completion)}% Complete')
