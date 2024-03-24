# Primeiros passos com Scikit-Learn | Machine Learning #04
# Link: https://www.youtube.com/watch?v=39HBlzFV9vk 

# Datasets de treinamento para brincar e aprender a trabalhar com a biblioteca
from sklearn.datasets import load_iris

iris = load_iris()

iris.target[[10,25,50]]