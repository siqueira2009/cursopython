# A partir da lista apresentada, utilizar List Comprehension para criar outra lista apenas com 
# animais que comecem com 'C' e que o tamanho de seu nome seja menor ou igual a 7. Por fim, imprima a nova lista

animais = ["Cavalo", "Vaca", "Cachorro", "Gato", "Caracol", "Macaco"]
animaisEspecificos = [animal for animal in animais if animal[0].lower() == "c" and len(animal) <= 7]

print("--------- ANIMAIS COM LETRA C E MENOR QUE 7 ---------")
print(animaisEspecificos)