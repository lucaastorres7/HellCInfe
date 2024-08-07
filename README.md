# HellCInfe

## Equipe

| <img src="https://avatars.githubusercontent.com/u/151575079?s=400&u=96fac0907f9100c143dc9f46242cacdf17af240f&v=4" alt="Lucas Torres" width="70" height="70"> | <img src="https://avatars.githubusercontent.com/u/92034541?v=4" alt="Guilherme da Matta" width="70" height="70"> | <img src="https://avatars.githubusercontent.com/u/141738614?v=4" alt="Carlos Alexandre" width="70" height="70"> | <img src="https://avatars.githubusercontent.com/u/82117231?v=4" alt="Pedro Vinícius" width="70" height="70"> | <img src="https://avatars.githubusercontent.com/u/165108906?v=4" alt="Thiago Fernandes" width="70" height="70"> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| [Lucas Torres](mailto:lrts@cin.ufpe.br)                                                                                                                      | [Guilherme da Matta](mailto:gpms@cin.ufpe.br)                                                                    | [Carlos Alexandre](mailto:cassj@cin.ufpe.br)                                                                    | [Pedro Vinicius](mailto:pvcb2@cin.ufpe.br)                                                                   | [Thiago Fernandes](mailto:tfls@cin.ufpe.br)                                                                     |

## Como rodar o jogo?

1. Instalar a biblioteca pygame no computador. Para isso, vá no terminal e digite

```
pip3 install pygame
```

2. Copie o link do repositório "https://github.com/lucaastorres7/HellCInfe"
3. Após isso vá no terminal e use o seguinte comando para copiar o repositório em seu computador:

```
git clone https://github.com/lucaastorres7/HellCInfe
```

4. Para executar o programa, use esse comando no VSCode:

```
python src/main.py
```

## Arquitetura e Organização do Código

O código foi estruturado principalmente Orientado à Objetos.

### Pastas e arquivos

Organizamos nosso projeto em pastas. A pasta assets que contém os arquivos de imagem e de som utilizado no jogo e a pasta src que contém o código inteiro. Dentro dessas pastas, há outras pastas para deixar o código um pouco mais organizado. Além disso, o código está dividido em diversos arquivos, sendo os principais a main.py e settings.py

### Codigo

#### Classes

- Player():
  > É a classe responsável por criar o personagem principal e realizar as principais funções do jogo. Como a movimentação, a colisão, a derrota e a vitória, a barra de vida, o ataque, o dano recebido e os sprites.
- Enemy():
  > É a classe responsável por criar o inimigo e as funções relacionadas a ele. Como a sua movimentação, seu dano recebido e o ataque.
- StaticObject():
  > É a classe responsável por criar os objetos que não se movem na tela.
- Drop():
  > É a classe responsável por criar um item no chão ao matar um inimigo.
- Button():
  > É a classe responsável por criar o botão no menu e na tela de derrota e detectar o clique do mouse.

#### Funções

- def show_menu():
  > É a função que cria o menu na tela.
- def show_defeat():
  > É a função que cria a tela de derrota na tela.
- def show_win():
  > É a função que cria a tela de vitória na tela.

## Controles:

| Jogador          | Teclas                                |
| ---------------- | ------------------------------------- |
| **Movimentação** | &#8592; , &#8593; , &#8594; , &#8595; |
| **Ataque**       | Barra de espaço                       |

## Itens

| Objetos      | Ação                                                                                     |
| ------------ | ---------------------------------------------------------------------------------------- |
| **Poção**    | Aumenta a vida do jogador.                                                               |
| **Escudo**   | Deixa o jogador invulnerável.                                                            |
| **Moeda**    | Aumenta a pontuação do jogador.                                                          |
| **Inimigos** | Ao colidir com o personagem principal tira uma vida dele e ao ser atacado por ele morre. |

## Capturas de Tela

<img src="assets\screenshots\death.jpg"/>
<img src="assets\screenshots\game.jpg"/>
<img src="assets\screenshots\menu.jpg"/>
<img src="assets\screenshots\victory.jpg"/>

## Ferramentas, Bibliotecas e Frameworks

| Biblioteca, Ferramentas e Frameworks | Aplicação                                                                                                                                                                                    |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PyGame                               | A biblioteca "pygame" é a principal desse projeto, já que ela é essencial para o funcionamento de um jogo em python. Utilizamos para renderizar objetos na tela e receber inputs do teclado. |
| Random                               | A biblioteca "Random" foi utilizada por meio da função "Randint", para aleatorizar a posição de spawn dos inimigos e dos itens.                                                              |
| Sys                                  | A biblioteca "Sys" foi utilizada para encerrar o funcionamento do programa.                                                                                                                  |
| Time                                 | A biblioteca "Time" foi utilizada para definir um tempo para o spawn dos itens e dos inimigos no cenário.                                                                                    |
| Piskel                               | O site "Piskel" foi utilizado para melhorar o spritesheet do personagem principal.                                                                                                           |

## Divisão de Tarefas

| Integrante             | Atribuições                                                                                                                     |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Lucas Torres**       | Implementação dos sprites do personagem principal, temporizador do spawn de itens, mudança do status do personagem com os itens |
| **Pedro Vinícius**     | Implementação do menu, do som e da tela de derrota.                                                                             |
| **Carlos Alexandre**   | Criou os itens, a colisão com eles, um contador de coleta na tela e ajeitou o design                                            |
| **Guilherme da Matta** | Inicializou o esqueleto do código, implementou os inimigos, movimentação, colisão                                               |
| **Thiago Fernandes**   | Implementou o boss e auxiliou no design                                                                                         |

## Conceitos e Aplicação

Ao decorrer do código, usamos diversos conceitos que aprendemos durante as aulas. Sendo os principais utilizados os Laços de Repetições, as Estruturas Condicionais, Funções, Listas e também a Programação Orientada a Objetos.

O uso dos laços de repetições é evidente no arquivo "main.py", já que nele o jogo roda dentro de um "While" e dentro desse while tem vários "for" loops utilizados para diversas finalidades. Como por exemplo, para verificar eventos que estão acontecendo com o jogador, para spawnar e verificar os inimigos. O for também é utilizado em conjunto com as listas para iterar nela para desenhar os sprites do personagem na tela de acordo com a ação que ele faz.

As estruturas condicionais foram uma parte essencial do código, já que em quase todo o código elas foram utilizadas. Ela foi usada para o spawn de itens, para a movimentação do personagem, para detectar as colisões, para verificar o estado do personagem e escolher o sprite, para mudar o status do personagem, para fazer a verificação de vitória e derrota, entre outros usos.

A utilização da Programação Orientada a Objetos tornou o código mais organizado e também foi essencial para o funcionamento do código, já que com o uso de seus métodos e atributos, o código acaba ficando mais organizado e conectado. As classes foram fundamentais para que pudessem ser criados os inimigos, os objetos estáticos e do jogador.

## Desafios/Erros/Experiência

- O maior desafio do grupo foi a utilização do github, já que nunca haviamos utilizado ele antes. A nossa solução para esse problema foi assistir a vídeos no youtube sobre git e compartilhando o conhecimento entre nós.
- O maior erro que cometemos foi de não se comunicar e dividir as tarefas bem no começo, o que causou um atraso no desenvolvimento do jogo. A solução que encontramos para esse problema, foi entrarmos em call mais frequentemente para discutir mais sobre as ideias e dificuldades um do outro.
- As principais lições que aprendemos foram que nós deveriamos nos organizar mais para trabalhar em grupo e que trabalhar em um projeto mais complexo do que apenas exercícios é mais complicado do que pensávamos.
