print(' To start a command input the number of the command.')
choose=input('1: Do you want to measure your Calorie(B.M.R.).\n2. Do you want measure your weight standard(B.M.I.)')
if choose=='1':
    gender=input('Please,enter your gender, Male or Female.')
    if gender=='Male':
        weight=float(input('Give your weight in K.G.'))
        height=float(input('Give your height in Centi metre. '))
        age=float(input('Give your age in years'))
        bal=66+(13.7*weight)+(5*height)-(6.8*age)
        print('Your calorie measurement is',bal,'.This power is conserved in your body')
    elif gender=='Female':
        weight=float(input('Give your weight in K.G.'))
        height=float(input('Give your height in Centi metre. '))
        age=float(input('Give your age in years'))
        cal=655+(13.7*weight)+(1.8*height)-(6.8*age)
        print('Your calorie measurement is',cal,'.This power is conserved in your body.')
    else:
        print('Sorry,Invalid text.')
elif choose=='2':
    a=float(input('Input your weight in k.g.'))
    b=float(input('Input your height in Meter'))
    mal=(a/(b*b))
    print('This is your weight standard.',mal,'.In short you can say B.M.I')
    know=input('Do you want some suggestion according to your B.M.I.(Yes or No)')
    if know=='Yes':
        ask=float(input('Input the following B.M.I.'))
        if ask<=18.5:
            print('Your weight is less.\n Suggestion:Eat healthy food regularly.')
        elif 18.5<ask<25:
            print("Your weight standard is right.Don't  be tensed just chill. ")
        elif 25<=ask<30:
            print('Your weight is much.You should be careful.Take exercises and eat less food')
        elif ask>=30:
            print('You are in a serious condition.Be careful, Be careful or else it may take to Allah')
        else:
            ('Invalid')
    if know=='No':
        print('Thank you for checking')
else:
    ("It's invalid.")