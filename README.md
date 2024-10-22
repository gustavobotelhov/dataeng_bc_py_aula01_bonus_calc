Cálculo de Bônus de Usuário
Este é um script simples em Python que solicita ao usuário informações sobre o nome, salário e bônus, e calcula o valor total do bônus que ele receberá.

Funcionamento
O script faz as seguintes operações:

Solicita o nome do usuário.
Solicita o valor do salário do usuário.
Solicita o valor do bônus do usuário.
Calcula o valor final do bônus com base na fórmula:
python
Copy code
valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario
Exibe uma mensagem personalizada com o nome do usuário e o valor do bônus calculado.
Constantes
CONSTANTE_BONUS: Um valor fixo de 1000 adicionado ao valor do bônus final.
Exemplo de Saída
yaml
Copy code
Digite o seu nome: João
Digite o seu salário: 2500
Digite o bônus recebido: 0.1
O usuário João possui um bônus de 1250.00 reais
Requisitos
Python 3.x instalado.
Como Executar
Clone o repositório:
bash
Copy code
git clone https://github.com/seuusuario/repositorio.git
Execute o script:
bash
Copy code
python calcular_bonus.py
Melhorias Futuras
Validação de entrada para garantir que os valores digitados sejam números válidos e não negativos.
Formatação do valor do bônus para exibir apenas duas casas decimais.
