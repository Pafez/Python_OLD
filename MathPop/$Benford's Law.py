from time import sleep
from os import system

def clear():
    return system("clear")


def nletise(entry):
    
    letters = "abcdefghijklmnopqrstuvwxyz "
    l = list(entry)
    nlet = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    for char in l:
        for num in range(27):
            if char.lower() == letters[num]:
                nlet[num] += 1
                
    return nlet
    
def nletper(entry):
    nlets = nletise(entry)
    
    t = sum(nlets)
    nlp = []
    for i in nlets:
        nlp.append(i/t)
        
    return nlp
def init():
    return nletper("""Once upon a time in Venice, Italy, there was a very rich merchant named Antonio. He had many ships that sailed in the sea. His ships carried different types of merchandise to other countries. He sold those goods there. He bought spices and other valuables from foreign countries and sold them in  Venice. Antonio was a very good and kind man. He always helped then poor. The people of Venice loved him very much for his honesty and kindness. 

Antonio had a close friend named Bassanio. He was a handsome young man and was born in a noble family. Bassanio liked to live a very luxurious life. He loved grandeur and style. He spent more money than he earned. As a result, he was very often short of money. In such situations, Bassanio would go to his best friend Antonio for help. Antonio would help him with cash. 

It so happened that Bassanio fell in love with a wealthy lady named Portia. Portia was known not only for her beauty but also for her wisdom. She was soft towards Bassanio too. He wanted to visit Portia in a grand manner but he did not have any money. So he went to Antonio. 

Bassanio : Dear friend Antonio, I am in great need of some money. I would like to visit Portia at Belmont, grandly dressed and with many servants. But I don't have any money right now. Please help me to fulfill my intention. 

Antonio : This is not a problem, my friend. How much do you need? 

Bassanio : Three thousand ducats will do. 

Antonio : I don't have that much money with me now as all my ships have gone out in the sea with merchandise. But don't worry, my friend, I'll arrange three thousand ducats for you. 

So he decided to borrow the sum from a moneylender named Shylock. Shylock was a very crooked man. Antonio and Shylock hated each other. Shylock used to lend money with high interest. He would ever send the debtor to prison if the latter failed to pay his debt. On the contrary, Antonio used to lend money to help those who needed it and wouldn't charge any interest. 

Shylock agreed to lend him money but on one condition. If he failed to repay the money in three months' time, he would pay a penalty. Shylock would cut a pound of flesh from any part of Antonio's body. Antonio willingly agreed, thinking that his ships would soon return with all the rich merchandise and he could easily return the money to Shylock by selling them. Shylock made Antonio sign a bond before giving him the money. Antonio took the money and gave it to Bassanio. 

Bassanio went to Belmont to visit Portia grandly dressed, with many servants. Portia's father had died lately. Before his death he had thought of an unusual plan to find a good husband for his daughter. He wanted a to marry Portia for herself and not for her wealth. He had three caskets made, one of gold, one of silver and one of lead. One of the caskets had Portia's Portrait in it. The suitor who would first choose the casket with the portrait would marry her. The first one to try was prince of Morocco. He thought that silver and lead are poor metals. It is the casket made of precious metal that can hold the precious picture. So he chose the gold casket. But all he found was a picture of a skull with a message that said, 
"All that glitters is not gold." The prince was very sad and went back home.  Then came the prince of Spain. He looked at the silver casket for a long time. On it was written, "He who chooses me will get what he deserves." The prince had a very high opinion about himself. He thought that he deserved the best. He therefore chose the silver casket and opened it. Inside the casket he found the picture of a blinking fool. He was very disappointed and offended. He immediately rode away. 

 Then it was Bassanio's turn. """)