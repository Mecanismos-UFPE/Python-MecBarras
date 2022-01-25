#####################################################
##    Pontos  do  acoplador em cadeias  impostas   ##
##    Código desenvolvido por José Maria Bezerra   ##
##    Uso exclusivo alunos Mecanismos UFPE/DEMEC   ##
#####################################################

### UTILIZAÇÃO
#
#   Objeto P definido de antemão pelo sistema
#            Atributos do objeto --> u,v,sᵢ,xₒ e yₒ
#
#   P.u = coordenada "u" local
#   P.v = coordenada "v" local
#   P.sᵢ = ângulo do eixo das abscissas (sistema local) com a horizontal
#   P.xₒ = coordenada global, horizontal, da horigem do sietema local
#   P.yₒ = coordenada global, vertical, da horigem do sietema local
#
#   P.CouplerSolve() <-- Chamada da função que vai calcular os
#                        deslocamentos, velocidades e acelerações.
###======================================================================

#!/usr/bin/env python
# coding: utf-8

from sympy import *
from sympy import diff as D
from IPython.display import display, Markdown, Latex

#a,b,c,d,e,t = symbols('a b c d e t')
a,b,c,d,e,f,g,h,x,y,x,z,u,w,k,t,r,l,ℓ = symbols('a b c d e f g h x y x z u w k t r \\ell \\ell')
α,β,γ,δ = Function ('alpha')(t), Function ('beta')(t),Function ('gamma')(t),Function ('delta')(t)
θ,φ,x,y,z = Function ('theta')(t), Function ('varphi')(t),Function ('x')(t),Function ('y')(t),Function ('z')(t)
αt,βt,γt,δt,θt,φt = symbols('\\dot{\\alpha} \\dot{\\beta} \\dot{\\gamma} \\dot{\\delta} \\dot{\\theta} \\dot{\\varphi}')
xt,yt,zt = symbols('\\dot{x} \\dot{y} \\dot{z}')
αtt,βtt,γtt = symbols('\\ddot{\\alpha} \\ddot{\\beta} \\ddot{\\gamma}')
δtt,θtt,φtt = symbols('\\ddot{\\delta} \\ddot{\\theta} \\ddot{\\varphi}')
xtt,ytt,ztt = symbols('\\ddot{x} \\ddot{y} \\ddot{z}')
Vc = {α:αt,β:βt,γ:γt,δ:δt,θ:θt,φ:φt,x:xt,y:yt,z:zt}
Ac = {α:αtt,β:βtt,γ:γtt,δ:δtt,θ:θtt,φ:φtt,x:xtt,y:ytt,z:ztt}

class CouplerPoint:
    """ Definition class for Coupler Points. """
    def __init__(self):
        self.u  = None
        self.v  = None
        self.sᵢ = None
        self.xₒ = None
        self.yₒ = None

    def CouplerSolve(self):
        M  = Matrix([[cos(self.sᵢ), -sin(self.sᵢ)],[sin(self.sᵢ), cos(self.sᵢ)]])
        U  = Matrix([self.u,self.v])
        Xₒ = Matrix([self.xₒ,self.yₒ])
        Ẋₒ = Matrix([D(self.xₒ,t),D(self.yₒ,t)])
        Ẍₒ = Matrix([D(self.xₒ,t,2),D(self.yₒ,t,2)])
        
        P = Xₒ + M*U
        Ω = Matrix([[0, -1],[1,0]])
        Ṗ = Ẋₒ + D(self.sᵢ,t)*M*Ω*U
        Γ = Matrix([[D(self.sᵢ,t)**2, D(self.sᵢ,t,2)],[-D(self.sᵢ,t,2), D(self.sᵢ,t)**2]])
        P̈ = simplify(Ẍₒ) - simplify(M*Γ*U)

        Pt = Ṗ; Ptt = P̈
        for i in Ac:
            Ptt = Ptt.subs( D(i,t,2),Ac[i] )
            Ptt = Ptt.subs( D(i,t),Vc[i] )
        for i in Vc:
            Pt = Pt.subs( D(i,t),Vc[i] )

        desloc = [latex(i) for i in P]
        veloc  = [latex(i) for i in Pt]
        acel   = [latex(i) for i in Ptt]
        d0 = desloc[0]; d1 = desloc[1]
        v0 = veloc[0]; v1 = veloc[1]
        a0 = acel[0]; a1 = acel[1]
        d0 = d0.replace(" ", ""); d1 = d1.replace(" ", "")
        v0 = v0.replace(" ", ""); v1 = v1.replace(" ", "")
        a0 = a0.replace(" ", ""); a1 = a1.replace(" ", "")
        A = B = C = E = G = H = 1
        while (A > 0 or B > 0 or C > 0 or E > 0 or G > 0 or H > 0):
            A = d0.find('{\\left(t'); B = d1.find('{\\left(t')
            C = v0.find('{\\left(t'); E = v1.find('{\\left(t')
            G = a0.find('{\\left(t'); H = a1.find('{\\left(t')
            if A > 0:
                d0 = d0[:A]+d0[(A+16):]
            if B > 0:
                d1 = d1[:B]+d1[(B+16):]
            if C > 0:
                v0 = v0[:C]+v0[(C+16):]
            if E > 0:
                v1 = v1[:E]+v1[(E+16):]
            if G > 0:
                a0 = a0[:G]+a0[(G+16):]
            if H > 0:
                a1 = a1[:H]+a1[(H+16):]

        display(Markdown("### Deslocamentos"))
        display(Markdown("$ \qquad x_p $ = $ %s $" %d0))
        display(Markdown("$ \qquad y_p $ = $ %s $" %d1))
        display(Markdown("### Velocidades"))
        display(Markdown("$ \qquad \dot x_p $ = $ %s $" %v0))
        display(Markdown("$ \qquad \dot y_p $ = $ %s $" %v1))
        display(Markdown("### Acelerações"))
        display(Markdown("$ \qquad \ddot x_p $ = $ %s $" %a0))
        display(Markdown("$ \qquad \ddot y_p $ = $ %s $" %a1))

P = CouplerPoint()