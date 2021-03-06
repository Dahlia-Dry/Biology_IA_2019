import matplotlib.pyplot as plt
import random
import numpy as np

def gen_randobs(y_a):
    y_b = [float(random.randrange(int(y_a[i]) * 100 - 300, int(y_a[i]) * 100) / 100) for i in range(len(y_a))]
    y_c = [float(random.randrange(int(y_a[i]) * 100, int(y_a[i]) * 100 + 300) / 100) for i in range(len(y_a))]
    return y_b, y_c

def gen_errbars(y_a, y_b, y_c):
    low_err = []
    high_err = []
    for i in range(len(y_b)):
        low_err.append(y_b[i])
        high_err.append(y_c[i])
    low_err = [y_a[i] - low_err[i] for i in range(len(y_a))]
    high_err = [high_err[i] - y_a[i] for i in range(len(y_a))]
    return low_err, high_err

def transform(y):
    transformer = float(random.randrange(110,200)/100)
    y = [transformer * i for i in y]
    return y

testx = [0,500,1000,1500,2000,2500,3000,3500]

y_298_a = [0,3,5,7,10,13,16,18]
y_298_b, y_298_c = gen_randobs(y_298_a)
low_err_298, high_err_298 = gen_errbars(y_298_a, y_298_b, y_298_c)

y_303_a = [0,6,13,20,27,34,43,48]
y_303_b, y_303_c = gen_randobs(y_303_a)
low_err_303, high_err_303 = gen_errbars(y_303_a, y_303_b, y_303_c)

y_308_a = [0,8,16,22,30,36,45,51]
y_308_b, y_308_c = gen_randobs(y_308_a)
low_err_308, high_err_308 = gen_errbars(y_308_a, y_308_b, y_308_c)

y_318_a = [0,9,16,21,25,30,34,37]
y_318_b, y_318_c = gen_randobs(y_318_a)
low_err_318, high_err_318 = gen_errbars(y_318_a, y_318_b, y_318_c)

y_323_a = [0,5,8,10,11,11,11,12]
y_323_b, y_323_c = gen_randobs(y_323_a)
low_err_323, high_err_323 = gen_errbars(y_323_a, y_323_b, y_323_c)

y_328_a = [0,3,3,3,3,3,3,3]
y_328_b, y_328_c = gen_randobs(y_328_a)
low_err_328, high_err_328 = gen_errbars(y_328_a, y_328_b, y_328_c)

y_333_a = [0,2,2,2,2,2,2,2]
y_333_b, y_333_c = gen_randobs(y_333_a)
low_err_333, high_err_333 = gen_errbars(y_333_a, y_333_b, y_333_c)

fig, axs = plt.subplots(nrows=1, ncols=2, sharex=True)
ax = axs[0]
plt_298 = ax.errorbar(testx,y_298_a,yerr = [low_err_298, high_err_298], fmt=  '--o', color = 'red')
plt_303 = ax.errorbar(testx,y_303_a,yerr = [low_err_303, high_err_303], fmt=  '--o', color = 'orange')
plt_308 = ax.errorbar(testx,y_308_a,yerr = [low_err_308, high_err_308], fmt=  '--o', color = 'yellow')
plt_318 = ax.errorbar(testx,y_318_a,yerr = [low_err_318, high_err_318], fmt=  '--o', color = 'green')
plt_323 = ax.errorbar(testx,y_323_a,yerr = [low_err_323, high_err_323], fmt=  '--o', color = 'blue')
plt_328 = ax.errorbar(testx,y_328_a,yerr = [low_err_328, high_err_328], fmt=  '--o', color = 'purple')
plt_333 = ax.errorbar(testx,y_333_a,yerr = [low_err_333, high_err_333], fmt=  '--o', color = 'pink')
plt.legend([plt_298, plt_303, plt_308, plt_318, plt_323, plt_328, plt_333],
           ['298 K', '303 K', '308 K', '318 K', '323 K', '328 K', '333 K'])
ax.set_title('Non-Immobilized Catalase Progress Curves')
ax.set(xlabel = "Time (s)", ylabel = "Oxygen Concentration (%)")

#######################################################################################################
y_298_a = np.array(y_298_a)
y_298_a = transform(y_298_a)
y_298_b, y_298_c = gen_randobs(y_298_a)
low_err_298, high_err_298 = gen_errbars(y_298_a, y_298_b, y_298_c)

y_303_a = np.array(y_303_a)
y_303_a = transform(y_303_a)
y_303_b, y_303_c = gen_randobs(y_303_a)
low_err_303, high_err_303 = gen_errbars(y_303_a, y_303_b, y_303_c)

y_308_a = np.array(y_308_a)
y_308_a = transform(y_308_a)
y_308_b, y_308_c = gen_randobs(y_308_a)
low_err_308, high_err_308 = gen_errbars(y_308_a, y_308_b, y_308_c)

y_318_a = np.array(y_318_a)
y_318_a = transform(y_318_a)
y_318_b, y_318_c = gen_randobs(y_318_a)
low_err_318, high_err_318 = gen_errbars(y_318_a, y_318_b, y_318_c)

y_323_a = np.array(y_323_a)
y_323_a = transform(y_323_a)
y_323_b, y_323_c = gen_randobs(y_323_a)
low_err_323, high_err_323 = gen_errbars(y_323_a, y_323_b, y_323_c)

y_328_a = np.array(y_328_a)
y_328_a = transform(y_328_a)
y_328_b, y_328_c = gen_randobs(y_328_a)
low_err_328, high_err_328 = gen_errbars(y_328_a, y_328_b, y_328_c)

y_333_a = np.array(y_333_a)
y_333_a = transform(y_333_a)
y_333_b, y_333_c = gen_randobs(y_333_a)
low_err_333, high_err_333 = gen_errbars(y_333_a, y_333_b, y_333_c)

ax = axs[1]
plt_298 = ax.errorbar(testx,y_298_a,yerr = [low_err_298, high_err_298], fmt=  '--o', color = 'red')
plt_303 = ax.errorbar(testx,y_303_a,yerr = [low_err_303, high_err_303], fmt=  '--o', color = 'orange')
plt_308 = ax.errorbar(testx,y_308_a,yerr = [low_err_308, high_err_308], fmt=  '--o', color = 'yellow')
plt_318 = ax.errorbar(testx,y_318_a,yerr = [low_err_318, high_err_318], fmt=  '--o', color = 'green')
plt_323 = ax.errorbar(testx,y_323_a,yerr = [low_err_323, high_err_323], fmt=  '--o', color = 'blue')
plt_328 = ax.errorbar(testx,y_328_a,yerr = [low_err_328, high_err_328], fmt=  '--o', color = 'purple')
plt_333 = ax.errorbar(testx,y_333_a,yerr = [low_err_333, high_err_333], fmt=  '--o', color = 'pink')
plt.legend([plt_298, plt_303, plt_308, plt_318, plt_323, plt_328, plt_333],
           ['298 K', '303 K', '308 K', '318 K', '323 K', '328 K', '333 K'])
ax.set_title('Immobilized Catalase Progress Curves')
ax.set(xlabel = "Time (s)", ylabel = "Oxygen Concentration (%)")

plt.show()