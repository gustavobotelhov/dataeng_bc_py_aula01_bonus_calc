CONSTANTE_BONUS = 1000
# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario_usuario = float(input("Digite o seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite o bônus recebido: "))

# 4) Calcule o valor do bônus final

valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario  

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# usar o f no print permite colocar texto e variáveis juntos
print(f"O usuário {nome_usuario} possui o bonus de {valor_do_bonus}")


# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

# 1° Ausência de Validação de Entrada: O código assume que o usuário sempre insere valores numéricos válidos para o salário e o bônus, 
# o que pode resultar em erros caso o usuário digite algo incorreto (como letras ou símbolos). Isso pode ser mitigado com um bloco try/except para tratar exceções como ValueError.
# 2° Falta de Validação para Bônus ou Salário Negativo.
# 3° Possível ZeroDivisionError ao usar o valor do bônus como multiplicador.
# 4° Formatação de Números no Print:
