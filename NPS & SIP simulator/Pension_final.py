from cProfile import label
from code import interact
from tkinter.filedialog import SaveFileDialog
import matplotlib.pyplot as plt
import random
import numpy as np

# fixed amount the individuals are willing to save throughout the year in SIP
saving = 0

salary = [int(input('What is your monthly salary: '))]
age = [int(input('What is your age: '))]
year = 60 - age[-1]
# Ensuring the saving amount is not less than 500
while True:
    saving = int(input('How much do you want to save: '))
    if saving <500:
        print('The saving amount is less than 500. Please re-enter')
    else:
        break

save = [] 
bankrate = []
i = year*12
amount = [0]
for x in range(i):
    s =  round(saving,2)
    # taking into account the compounding of interest rate on the previous contribution
    savings = round(saving,2) + amount[-1]
    save.append(s)
    #Interest rate between 8-15%
    nps_rate = random.uniform(0.0067,0.0125)
    bankrate.append(nps_rate)
    interest = savings + savings * nps_rate
    interests = round(interest, 2)
    amount.append(interests)

np_bankrate = np.array(bankrate)*1200 

print()
# Principal Amount Invested
print('Amount Invested: ' + str(round(sum(save))))
# maturity amount 
print('Maturity Amount: ' + str(round(amount[-1])))
#Monthly contribution 
print('Monthly Contribution: ' + str(saving))
# Interest Earned on Investment
print('Interest Earned: ' + str(round(amount[-1]-sum(save))))
# Lump Sum
# Proportion of salary invested
print('Percentage of Salary Invested: ' + str(int((saving/salary[-1])*100)) + '%')

plt.plot(np_bankrate)
plt.show()






