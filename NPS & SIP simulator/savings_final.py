from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import random

# fixed amount the individuals are willing to save throughout the year in SIP
saving = 0
salary = [int(input('What is your monthly salary: '))]
# Ensuring not accepting arguments below Rs.100
while True:    
    saving = int(input('How much do you want to save: '))
    if saving <100:
        print('The saving amount is less than 100. Please re-enter')
    else:
        break
save = []
sip = []

bank = [0]
amount = [0]
for x in range(12):
    s =  round(saving,2)
    # taking into account the compounding of interest rate on the previous contribution
    savings = round(saving,2) + amount[-1] 
    save.append(s)
    # taking into account the compounding on interest rate on previous contribution 
    b = s + bank[-1] 
    # bank interest rate varying between 5-7% annually 
    bacc = b + ( b * random.uniform(0.005,0.00625))  
    baccs = round(bacc,2) 
    # SIP rate of Interest Varying Between 20-40%
    sip_in = random.uniform(0.0167,0.0375) 
    sip.append(sip_in)
    interest = savings + savings * sip_in
    interests = round(interest,2)
    amount.append(interests)
    bank.append(baccs)
# Monthly fluctuations in the SIP interest rate
np_sip = np.array(sip)*1200
f = round(sum(save))
print()
print('Contribution: ' + str(round(sum(save))))
print('Percentage of salary invested: ' + str(round((save[-1]/salary[-1])*100)) + '%')
print()
print('SIP')
print('End of the year amount is: ' + str(round(amount[-1])))

print ('Interest Earned: ' + str(round(amount[-1] - f )))

print('Rate of Interest: ' + str(round((100*(amount[-1] - f )/sum(save)),2)) +'%')
print()
print('Bank')
print('Bank rate of interest earning: ' + str(round(bank[-1])))
print ('Bank Interest Earned: ' +  str(round(bank[-1] - f )))
print('Bank rate of interest: ' + str(round((100*(bank[-1] - f )/sum(save)),2)) + '%')

# graphical plotting of SIP interest Rates
plt.plot(np_sip,  label= 'SIP Interest Rate')
plt.xlabel('Months')
plt.ylabel('Interest Rate')
plt.legend()
plt.show()
