# HellCInfe
## Equipe
| <img src="https://avatars.githubusercontent.com/u/151575079?s=400&u=96fac0907f9100c143dc9f46242cacdf17af240f&v=4" alt="Lucas Torres" width="70" height="70"> | <img src="https://avatars.githubusercontent.com/u/92034541?v=4" alt="Guilherme da Matta" width="70" height="70"> | <img src="https://avatars.githubusercontent.com/u/141738614?v=4" alt="Carlos Alexandre" width="70" height="70"> | <img src="https://avatars.githubusercontent.com/u/82117231?v=4" alt="Pedro Vinícius" width="70" height="70"> | <img src="https://avatars.githubusercontent.com/u/165108906?v=4" alt="Thiago Fernandes" width="70" height="70"> |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| [Lucas Torres](mailto:lrts@cin.ufpe.br)                                                                         | [Guilherme da Matta](mailto:gpms@cin.ufpe.br)                                                                          | [Carlos Alexandre](mailto:cassj@cin.ufpe.br)                                                                          | [Pedro Vinicius](mailto:pvcb2@cin.ufpe.br)                                                                             | [Thiago Fernandes](mailto:tfls@cin.ufpe.br)

## Como rodar o jogo?
```
python src/main.py
```

## Arquitetura e Organização do Código

## Controles:
|    Jogador      |     Teclas    |
| ------------------- | ------------------- |
|  **Movimentação**|  &#8592; , &#8593; , &#8594; , &#8595; |
|  **Ataque** | Barra de espaço |

## Itens
|    Objetos     |     Ação    |
| ------------------- | ------------------- |
|  **Poção**|  Aumenta a vida do jogador. |
|  **Escudo** | Deixa o jogador invulnerável. |
|  **Moeda** | Aumenta a pontuação do jogador. |
|  **Inimigos** | Ao colidir com o personagem principal tira uma vida dele e ao ser atacado por ele morre. |

## Capturas de Tela

## Ferramentas, Bibliotecas e Frameworks
|      Biblioteca, Ferramentas e Frameworks      |     Aplicação     |
| ------------------- | ------------------- |
|  PyGame  |  A biblioteca "pygame" é a principal desse projeto, já que ela é essencial para o funcionamento de um jogo em python. Utilizamos para renderizar objetos na tela e receber inputs do teclado. |
|  Random  | A biblioteca "Random" foi utilizada por meio da função "Randint", para aleatorizar a posição de spawn dos inimigos e dos itens. |
|  Sys |  A biblioteca "Sys" foi utilizada para encerrar o funcionamento do programa. |
| Time | A biblioteca "Time" foi utilizada para definir um tempo para o spawn dos itens e dos inimigos no cenário. |
|  Piskel |  O site "Piskel" foi utilizado para melhorar o spritesheet do personagem principal. | 

## Divisão de Tarefas
|      Integrante      |     Atribuições     |
| ------------------- | ------------------- |
|  **Lucas Torres**| Implementação dos sprites do personagem principal, temporizador do spawn de itens, mudança do status do personagem com os itens |
|  **Pedro Vinícius** | Implementação do menu, do som e da tela de derrota.  |
|  **Carlos Alexandre** |  Criou os itens, a colisão com eles, um contador de coleta na tela e ajeitou o design  |
|  **Guilherme da Matta** |  Inicializou o esqueleto do código, implementou os inimigos, movimentação, colisão  |
|  **Thiago Fernandes** | Implementou o boss e auxiliou no design |

## Conceitos e Aplicação

## Desafios/Erros/Experiência
- O maior desafio do grupo foi a utilização do github, já que nunca haviamos utilizado ele antes. A nossa solução para esse problema foi assistir a vídeos no youtube sobre git e compartilhando o conhecimento entre nós.
- O maior erro que cometemos foi de não se comunicar e dividir as tarefas bem no começo, o que causou um atraso no desenvolvimento do jogo. A solução que encontramos para esse problema, foi entrarmos em call mais frequentemente para discutir mais sobre as ideias e dificuldades um do outro.
- As principais lições que aprendemos foram que nós deveriamos nos organizar mais para trabalhar em grupo e que trabalhar em um projeto mais complexo do que apenas exercícios é mais complicado do que pensávamos.
