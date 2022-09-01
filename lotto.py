import random
import collections

lottozahlen = list(range(1, 50))
"""start 1 ziel 50 in +1 schritten, endet bei 49"""

"""nutzereingabe = list(map(int, input("Geben Sie 6 Zahlen an: ").split()))
nutzereingabe.sort()

print("Ihre Zahlen: ", nutzereingabe)"""

lottozahlen_gewinner = random.sample(lottozahlen, 6)
lottozahlen_gewinner.sort()
"""random.sample zieht auslottozahlen 6 verschiedene zahlen und speichert in lottozahlen_gewinner
    alternativ existiert random.choices, welches allerdings zahlen doppelt nimmt deswegen nehmen wir hier sample
"""


print("Gewinnzahlen: ", lottozahlen_gewinner)
