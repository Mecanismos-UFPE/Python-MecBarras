#####################################################
##    Pontos  do  acoplador em cadeias  impostas   ##
##    Código desenvolvido por José Maria Bezerra   ##
##    Uso exclusivo alunos Mecanismos UFPE/DEMEC   ##
#####################################################

#!/usr/bin/env python
# coding: utf-8

from vardefs import *

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
