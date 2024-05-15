import random
from busca_palavra import buscar_palavra

def jogar():
    data = buscar_palavra()
    if not data:
        return
 
    while True:
        valor_secreto = random.choice(data)
        palavra_secreta = valor_secreto.get('palavra')
        dica = valor_secreto.get('dica')
        
        print(f'A palavra secreta tem {len(palavra_secreta)} letras')
        print(f'A dica é -> {dica}')
        chute = input('O que você acha que é: ')
        print()  # Adiciona uma quebra de linha após o chute do usuário

        if chute.lower() == palavra_secreta.lower():
            print('Parabéns, você acertou!\n')
        else:
            print(f'Errou.. a palavra secreta era "{palavra_secreta}"\n')

        jogar_novamente = input('Quer jogar novamente? (s/n): ')
        print()  # Adiciona uma quebra de linha após a pergunta
        
        if jogar_novamente.lower() != 's':
            break
            