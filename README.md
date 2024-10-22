# **Cálculo de Bônus de Usuário**

Este é um script simples em Python que solicita ao usuário informações sobre o nome, salário e bônus, e calcula o valor total do bônus que ele receberá.

## **Funcionamento**

O script faz as seguintes operações:
1. Solicita o nome do usuário.
2. Solicita o valor do salário do usuário.
3. Solicita o valor do bônus do usuário.
4. Calcula o valor final do bônus com base na fórmula:
   ```python
   valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario
   ```
5. Exibe uma mensagem personalizada com o nome do usuário e o valor do bônus calculado.

## **Constantes**
- `CONSTANTE_BONUS`: Um valor fixo de **1000** adicionado ao valor do bônus final.

## **Exemplo de Saída**

```
Digite o seu nome: João
Digite o seu salário: 2500
Digite o bônus recebido: 0.1
O usuário João possui um bônus de 1250.00 reais
```

## **Requisitos**

- Python 3.x instalado.

## **Como Executar**

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/repositorio.git
   ```
2. Execute o script:
   ```bash
   python calcular_bonus.py
   ```

## **Melhorias Futuras**

- Validação de entrada para garantir que os valores digitados sejam números válidos e não negativos.
- Formatação do valor do bônus para exibir apenas duas casas decimais.
