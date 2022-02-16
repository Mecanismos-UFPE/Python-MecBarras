# [LinkageMechanism.py](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/Mecanismos-UFPE/Python-MecBarras/blob/dfe02a91259ff396605f323bce8f6888c320b73e/LinkageMechanism.py)
A utilização do módulo "LinkageMechanism" exige que o módulo ["vardefs.py"](https://github.com/Mecanismos-UFPE/Python-MecBarras/blob/2c7919d6e725b8af7a2f2a9502b8fa78812ef233/vardefs.py) esteja na mesma pasta onde se encontra o "LinkageMechanism" 
### Funções Disponíveis

* **MecSolve**

* **BlockSolve**

* ### Chamada das Funções

```python
MecSolve(Cg, Eq)
F,K,J,M = MecSolve(Cg, Eq, 1)
A, B, C, D, F1, F2, K1, K2 = BlockSolve(Cg, Eq)
```

> **Argumentos**
> 
> *Funçao MecSolve e BlockSolve:*
> 
> * Cg - Lista contendo as coordenadas generalizadas
> 
> * Eq - Lista contendo as equações de restrição
>   
>   > A função MecSolve quando chamada com o terceiro argumento,
>   > 
>   > este não é obrigatório, não nulo, tetorna as matrizes F, K, J e M.
> 
> *Funçao BlockSolve:*
> 
> A função BlockSolve deve ser utilizada em cadeias de 4 barras, quando se
> 
> deseja obter as matrizes bloco. Normalmente para conferência.

### Forma de uso do Código

```python
from LinkageMechanism import *

f1 = a*cos(θ) + b*cos(φ) - x
f2 = a*sin(θ) - b*sin(φ)

MecSolve([θ,φ,x],[f1,f2])
```

Este código terá, como retorno

![](https://user-images.githubusercontent.com/67014817/151065611-5fcb981e-fa6a-4af6-89f6-372d840580d8.jpg)
