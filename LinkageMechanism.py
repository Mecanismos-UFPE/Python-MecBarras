#####################################################
##    Análise de Cadeias impostas e não impostas   ##
##    Código desenvolvido por José Maria Bezerra   ##
##    Uso exclusivo alunos Mecanismos UFPE/DEMEC   ##
#####################################################

from vardefs import *

def MD_Matriz(st, mt, row, col):
    V = st + "\\begin{bmatrix}"
    for i in range(row):
        for j in range(col):
            V += latex(mt[i,j])
            if j != col-1:
                V += ' & '
            else:
                V += '\\\ '
    V += "\end{bmatrix}"
    return V

def PrintMD_MultDOF(Cg,f,r,F,J,K,L):
    display( Markdown("### Matrizes F e J") )
    FJ = MD_Matriz("F = ", F, r, f) + MD_Matriz("\qquad J = ", J, r, r)
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
        LN += KS[i]+" = "+MK[i]+" \qquad "
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
        LN += MS[i]+" = "+ML[i]+" \qquad "
    display(Markdown('$ %s $' %LN))
    return

def PrintMD_OneDOF(Cg,r,F,J,K,L):
    display( Markdown("### Matrizes F e J") )

    MF = [latex(i) for i in F]
    VF = "F = \\begin{Bmatrix}"

    for i in range(len(MF)):
        VF += MF[i]
        if i != len(MF)-1:
            VF += '\\\ '
    VF += "\end{Bmatrix}"

    LN = VF + MD_Matriz("\qquad J = ", J, r, r)
    display(Markdown('$ %s $' %LN))

    # Impressão dos Coeficientes de Velocidade
    display( Markdown("### Coeficientes de Velocidade") )
    MK = [latex(i) for i in K]
    KS = [latex(Ck[i]) for i in Cg[1:]]
    LN = ""
    for i in range(len(KS)):
        LN += KS[i]+" = "+MK[i]+" \qquad "
    display(Markdown('$ %s $' %LN))

    # Impressão dos Coeficientes da Aceleração
    display( Markdown("### Coeficientes da Aceleração") )
    Ms = Matrix([ Ls[i] for i in Cg[1:] ])
    ML = [latex(i) for i in L]
    MS = [latex(i) for i in Ms]
    LN = ""
    for i in range(len(KS)):
        LN += MS[i]+" = "+ML[i]+" \qquad "
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
    K1 = simplify( -A**-1 * F1 )
    K2 = simplify( -D**-1 * (F2 + B*K1[0] + C*K1[1]) )

    return A, B, C, D, F1, F2, K1, K2
