####################################################
##   Análise de Cadeias impostas e não impostas   ##
##   Código desenvolvido por José Maria Bezerra   ##
##   Uso exclusivo alunos Mecanismos UFPE/DEMEC   ##
####################################################

#!/usr/bin/env python
# coding: utf-8

from io import FileIO
from sympy import *
from sympy import diff as D
from IPython.display import display, Math, Markdown, Latex
init_printing(use_latex='mathjax')

ReturnMatrices = true
π = pi

# Defining Constants
a,b,c,d,e,f,g,h,m,n,p,q,r,s,u,v,w,t,l,ℓ = symbols('a b c d e f g h m n p q r s u v w t \\ell \\ell')

# Defining Variables
α,β,γ,δ,φ,θ,α1,α2,α3,β1,β2,β3,θ1,θ2,θ3,φ1,φ2,φ3 = symbols('alpha beta gamma delta varphi theta alpha_1 alpha_2 alpha_3 beta_1 beta_2 beta_3 theta_1 theta_2 theta_3 varphi_1 varphi_2 varphi_3')
x,y,z,x1,x2,x3,y1,y2,y3,z1,z2,z3 = symbols('x y z x_1 x_2 x_3 y_1 y_2 y_3 z_1 z_2 z_3')

# Definig Velocity Coeficients
kα,kβ,kγ,kδ,kφ,kθ = symbols('k_{\\alpha} k_{\\beta} k_{\\gamma} k_{\\delta} k_{\\varphi} k_{\\theta}')
kα1,kα2,kα3,kβ1,kβ2,kβ3,kθ1,kθ2,kθ3,kφ1,kφ2,kφ3 = symbols('k_{\\alpha_1} k_{\\alpha_2} k_{\\alpha_3} k_{\\beta_1} k_{\\beta_2} k_{\\beta_3} k_{\\theta_1} k_{\\theta_2} k_{\\theta_3} k_{\\varphi_1} k_{\\varphi_2} k_{\\varphi_3}')
kx,ky,kz,kx1,kx2,kx3,ky1,ky2,ky3,kz1,kz2,kz3 = symbols('k_x k_y k_z k_{\\x_1} k_{\\x_2} k_{\\x_3} k_{\\y_1} k_{\\y_2} k_{\\y_3} k_{\\z_1} k_{\\z_2} k_{\\z_3}')
ku,kv,kw = symbols('k_u k_v k_w')

# Associating Velocity Coeficients
Ck = {α:kα,β:kβ,γ:kγ,δ:kδ,θ:kθ,φ:kφ,x:kx,y:ky,z:kz,φ1:kφ1,φ2:kφ2,φ3:kφ3,θ1:kθ1,θ2:kθ2,θ3:kθ3,u:ku,v:kv,w:kw,x1:kx1,x2:kx2,x3:kx3,y1:ky1,y2:ky2,y3:ky3,z1:kz1,z2:kz2,z3:kz3}

# Definig Aceleration Coeficients
ℓα,ℓβ,ℓγ,ℓδ,ℓθ,ℓφ = symbols('\\ell_{\\alpha} \\ell_{\\beta} \\ell_{\\gamma} \\ell_{\\delta} \\ell_{\\theta} \\ell_{\\varphi}')
ℓx,ℓy,ℓz,ℓu,ℓv,ℓw = symbols('\\ell_x \\ell_y \\ell_z \\ell_u \\ell_v \\ell_w')
ℓx1,ℓx2,ℓx3,ℓy1,ℓy2,ℓy3,ℓz1,ℓz2,ℓz3 = symbols('\\ell_{\\x_1} \\ell_{\\x_2} \\ell_{\\x_3} \\ell_{\\y_1} \\ell_{\\y_2} \\ell_{\\y_3} \\ell_{\\z_1} \\ell_{\\z_2} \\ell_{\\z_3}')
ℓθ1,ℓθ2,ℓθ3,ℓφ1,ℓφ2,ℓφ3 = symbols('\\ell_{\\theta_1} \\ell_{\\theta_2} \\ell_{\\theta_3} \\ell_{\\varphi_1} \\ell_{\\varphi_2} \\ell_{\\varphi_3}')
ℓα1,ℓα2,ℓα3,ℓβ1,ℓβ2,ℓβ3 = symbols('\\ell_{\\alpha_1} \\ell_{\\alpha_2} \\ell_{\\alpha_3} \\ell_{\\beta_1} \\ell_{\\beta_2} \\ell_{\\beta_3}')

# Associating Aceleration Coeficients
Ls = {α:ℓα,β:ℓβ,γ:ℓγ,δ:ℓδ,θ:ℓθ,φ:ℓφ,x:ℓx,y:ℓy,z:ℓz,u:ℓu,v:ℓv,w:ℓw,x1:ℓx1,x2:ℓx2,x3:ℓx3,y1:ℓy1,y2:ℓy2,y3:ℓy3,z1:ℓz1,z2:ℓz2,z3:ℓz3,φ1:ℓφ1,φ2:ℓφ2,φ3:ℓφ3,θ1:ℓθ1,θ2:ℓθ2,θ3:ℓθ3,α1:ℓα1,α2:ℓα2,α3:ℓα3,β1:ℓβ1,β2:ℓβ2,β3:ℓβ3}

αt,βt,γt,δt,θt,φt = symbols('\\dot{\\alpha} \\dot{\\beta} \\dot{\\gamma} \\dot{\\delta} \\dot{\\theta} \\dot{\\varphi}')
θ1t,θ2t,θ3t = symbols('\\dot{\\theta_1} \\dot{\\theta_2} \\dot{\\theta_3}')
x1t,x2t,y1t,y2t,z1t,z2t = symbols('\\dot{x_1} \\dot{x_2} \\dot{y_1} \\dot{y_2} \\dot{z_1} \\dot{z_2}')
xt,yt,zt = symbols('\\dot{x} \\dot{y} \\dot{z}')
Ve = {α:αt,β:βt,γ:γt,δ:δt,θ:θt,θ1:θ1t,θ2:θ2t,θ3:θ3t,φ:φt,x:xt,y:yt,z:zt,x1:x1t,x2:x2t,y1:y1t,y2:y2t,z1:z1t,z2:z2t}

def MD_Matriz(st, mt, row, col):
    V = st + "\\begin{bmatrix}"
    for i in range(row):
        for j in range(col):
            V += latex(mt[i,j])
            if j != col-1:
                V += ' & '
            else:
                V += "\\\\ "
    V += "\\end{bmatrix}"
    return V

def PrintMD_MultDOF(Cg,f,r,F,J,K,L):
    display( Markdown("### Matrizes F e J") )
    FJ = MD_Matriz("F = ", F, r, f) + MD_Matriz("\\qquad J = ", J, r, r)
    display(Markdown('$ %s $' %FJ))

    # Impressão dos Coeficientes de Velocidade
    display( Markdown("### Coeficientes de Velocidade") )
    MK = [latex(i) for i in K]
    KS = []
    for i in range(r):
        for j in range(f):
            KS.append( latex(Ck[ Cg[j] ])  + latex( Cg[f+i] ) )
    KS = [i.replace('}',' ')+'}' for i in KS]
    KS = [i.replace('}',' ')+'}' for i in KS]
    LN = ""
    for i in range(len(KS)):
        LN += KS[i]+" = "+MK[i]+" \\qquad "
    display(Markdown('$ %s $' %LN))

    # Impressão dos Coeficientes da Aceleração
    display( Markdown("### Coeficientes da Aceleração") )
    ML = [latex(i) for i in L]
    MS = []
    for i in range(r):
        for j in range(f):
            MS.append( latex(Ls[ Cg[j] ])  + latex( Cg[f+i] ) )
    MS = [i.replace('}',' ')+'}' for i in MS]
    LN = ""
    for i in range(len(KS)):
        LN += MS[i]+" = "+ML[i]+" \\qquad "
    display(Markdown('$ %s $' %LN))
    return

def PrintMD_OneDOF(Cg,r,F,J,K,L):
    display( Markdown("### Matrizes F e J") )

    MF = [latex(i) for i in F]

    VF = "F = \\begin{Bmatrix}"
    for i in range(len(MF)):
        VF += MF[i]
        if i != len(MF)-1:
            VF += '\\\\ '
    VF += "\\end{Bmatrix}"

    LN = VF + MD_Matriz("\\qquad J = ", J, r, r)
    display(Markdown('$ %s $' %LN))

    # Impressão dos Coeficientes de Velocidade
    display( Markdown("### Coeficientes de Velocidade") )
    MK = [latex(i) for i in K]
    KS = [latex(Ck[i]) for i in Cg[1:]]
    LN = ""
    for i in range(len(KS)):
        LN += KS[i]+" = "+MK[i]+" \\qquad "
    display(Markdown('$ %s $' %LN))

    # Impressão dos Coeficientes da Aceleração
    display( Markdown("### Coeficientes da Aceleração") )
    Ms = Matrix([ Ls[i] for i in Cg[1:] ])
    ML = [latex(i) for i in L]
    MS = [latex(i) for i in Ms]
    LN = ""
    for i in range(len(KS)):
        LN += MS[i]+" = "+ML[i]+" \\qquad "
    display(Markdown('$ %s $' %LN))
    return

def All_Matrix(Cg,Eq,f):
    Eq = Matrix(Eq)
    J = Eq.jacobian(Cg[f:])     # Jacobiano do sistema
    F = Eq.jacobian([Cg[:f]])   # Obtenção da matriz F
    K = simplify(-(J**-1)*F)    # Obtenção da matriz K
    if f == 1:
        Ks = Matrix([ Ck[i] for i in Cg[1:] ])
        L = simplify( K.jacobian([Cg[0]]) + K.jacobian([Cg[f:]])*Ks )
    else:
        L = Matrix([])
        Vv = [ Ve[i] for i in Cg ]
        for i in range(f):          # Obtenção da matriz L
            Lprov = K.col(i).jacobian(Cg[:f])*((1/Vv[i])*Matrix(Vv[:f])) + K.col(i).jacobian(Cg[f:])*((1/Vv[i])*Matrix(Vv[f:]))
            L = L.row_join(Lprov)
    return F, K, J, L

def MecSolve(Cg,Eq,flag=0):     # Cg,Vg Coords e Veloc Generalizadas
    f = len(Cg)-len(Eq)         # Graus de liberdade
    r = len(Eq)                 # Qtd. de Equações de restrição

    F,K,J,L = All_Matrix(Cg,Eq,f)

    if flag == true:
        return F, J, K, L

    if f == 1:
        PrintMD_OneDOF(Cg,r,F,J,K,L)
    else:
        PrintMD_MultDOF(Cg,f,r,F,J,K,L)

def BlockSolve(Cg,Eq):
    F,J,K,L = MecSolve(Cg,Eq,true)

    A = Matrix([J[0,:2],J[1,:2]])
    D = Matrix([J[2,2:],J[3,2:]])
    B = Matrix([J[2,0],J[3,0]])
    C = Matrix([J[2,1],J[3,1]])
    F1 = Matrix([F[0],F[1]])
    F2 = Matrix([F[2],F[3]])
    #K1 = simplify( -A**-1 * F1 )
    #K2 = simplify( -D**-1 * (F2 + B*K1[0] + C*K1[1]) )

    #return A, B, C, D, F1, F2, K1, K2
    return A, B, C, D, F1, F2
