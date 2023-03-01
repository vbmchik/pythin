from matplotlib import animation
import matplotlib.pyplot as plt
import random
import seaborn as sns
import sys
# frequencies [ a,b,c,d,e,f]
# [0,0,0,0,0,0]
def getframe( frame_number, rolls, faces, frequencies):
    # roll die and update data
    for i in range(rolls):
        frequencies[random.randrange(1,7)-1] += 1
    plt.cla()
    axes = sns.barplot(x=faces, y=frequencies, palette="bright")
    axes.set_title(f'Die frequencies {sum(frequencies):,} Rolls')
    axes.set(xlabel="Dice value", ylabel="Frequency")
    axes.set_ylim(top=max(frequencies)*1.10)
    # 0,23234234234  -> 23.234%
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x()+bar.get_width()/2.0
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency/sum(frequencies):.3%}'
        axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')
        
number_of_frames = int(sys.argv[1])
rolls_per_frame = int(sys.argv[2])

sns.set_style('whitegrid')

figure = plt.figure('Rolling 6-seded die')
values = list(range(1,7))   # labels for X-axis
frequencies = [0]*6  # -> [0,0,0,0,0,0]

die_animation = animation.FuncAnimation(
    figure, getframe, repeat=False, frames=number_of_frames, interval=8, 
    fargs=(rolls_per_frame,values,frequencies)
)

plt.show()
