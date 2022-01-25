# [CouplerPoint.py](https://github.com/Mecanismos-UFPE/Python-Cames/blob/d0a6fe4e0e1c62cb841fde6c5e7e90c90020dd01/elevdiagram.py)

### Utilização com base na Classe CouplerPoint

* ### Uso da Classe

```python
# Objeto P já pré-definido e deve ser usado

# Os atributos são:
P.u =
P.v =
P.sᵢ =
P.xₒ =
P.yₒ =

# Chamada do Método Base:
P.CouplerSolve()
```

> **Atributos**
> 
> * (P.u, P.v) - Coordenadas locais u e v
> 
> * (P.xₒ, P.yₒ) - Coordenas globais da horigem do sistema local
> 
> * P.sᵢ - Ângulo, em radianos, do eixo das abscissas do sistema local
> 
> **Método**
> 
> - P.CouplerPoint - Chamada do método que efetua os cálculos
> 
> *Objetos da Classe:*
> 
> O objeto "P" já é pré criado e pode ser usado, como acima, porém é
> 
> possível a criação de novos métodos com o comando
> 
> ```python
> VarObj = CouplerPoint()
> ```

### Forma de uso do Código

```python
from CouplerPoint import *

P.u = a
P.v = 0
P.sᵢ = φ
P.xₒ = a*cos(θ)
P.yₒ = a*sin(θ)

P.CouplerSolve()
```

Este código terá, como retorno

![](https://user-images.githubusercontent.com/67014817/151072030-132672e5-b84f-47a3-97de-7cd657511367.jpg)
