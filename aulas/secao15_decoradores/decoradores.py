"""
Decoradores (No sentido de decoração mesmo) - Decorators

O que são Decorators?
- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de HOF (Higher Order Functions);
- Decorators tem uma sintaxe própria, usando '@' (Syntact Sugar / Açúcar Sintático);


# Não confunda Decorator com Decorator Function


/------------------------------------------/
/            Function Decorator            /
/------------------------------------------/

/------------------------------------------/
/              Function Comum              /
/------------------------------------------/


# Decorators como funções (Syntax não recomendada, sem Açúcar)


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem vindo(a) à Geek University!')


# Testando 1

# saudacao()

teste = seja_educado(saudacao)
teste()

# Testando 2


def raiva():
    print('EU TE ODEIO!')


raiva_educada = seja_educado(raiva)
raiva_educada()




# Decorators com Syntax Sugar, com Açúcar


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')


# Testando

apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir...')


dormir()

"""
