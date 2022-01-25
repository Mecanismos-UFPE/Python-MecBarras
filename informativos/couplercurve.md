# [elevdiagram py](https://github.com/Mecanismos-UFPE/Python-Cames/blob/d0a6fe4e0e1c62cb841fde6c5e7e90c90020dd01/elevdiagram.py)

### Funções Disponíveis
* **GetElev**
* **GetRet**
* **PlotCurv**
* **PlotDiagrams**

 ### Chamada das Funções

~~~python
curv = GetElev('Curva', h, β)
curv = GetRet('Curva', h, β)
PlotCurv(curv)
PlorCurv(curv, AcelTrue)
~~~

>
> **Argumentos**
>
> *Funçao GetElev e GetRet:*
> 
> * 'harmonica'
> * 'cicloide'
> * 'duplaharmonica'
> * 'duplacicloide'
> * '3-4' ou '4-5'
> * '3-4-5' ou '4-5-6'
> * '3-4-5-6' ou '4-5-6-7'
>
> - h - Valor que representa a altura de elevação
> - β - Ângulo de elevação, sempre em radianos
> 
>
> *Funçao PlotCurv:*
>
> - curv     - Valor retornado pela função GetElev ou pela função GetRet
> - AcelTrue - Argumento, não obrigatório, se presente, com valor
>            diferente de zero, não plota o gráfico da aceleração segunda.
>
> *Funçao PlotDiagrams:*
>
> - f  - Valor retornado pela função GetElev.
> - βs - Ângulo de repouso superior (se não houver, deixe zero)
> - g  - Valor retornado pela função GetRet.
> - βi - Ângulo de repouso inferior (se não houver, deixe zero)

### Forma de uso do Código
~~~python
from elevdiagram import *

f = GetElev('duplacicloide', 2, pi/2)
g = GetElev('duplahamonica', 2, 2*pi/3)
PlotCurv(f,1)
PlotCurv(g)
PlotDiagrams(f, pi/2, g, pi/3)
~~~
