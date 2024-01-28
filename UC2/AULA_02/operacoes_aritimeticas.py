import pandas as pd

Serie1 = pd.Series([1,2,3,4,5])
Serie2 = pd.Series([10,20,30,40,50])

# somando duas series
s1_mais_s2 = Serie1 + Serie2
print(s1_mais_s2)

# subtraindo duas series
s1_menos_s2 = Serie1 - Serie2
print(s1_menos_s2)

# multiplicando duas series
s1_vezes_s2 = Serie1 * Serie2
print(s1_vezes_s2)

# dividindo duas series
s1_por_s2 = Serie1 / Serie2
print(s1_por_s2)

