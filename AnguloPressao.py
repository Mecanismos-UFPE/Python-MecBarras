#####################################################
##    Mecanismos de Came  -   Ângulo de Pressaão   ##
##    Código desenvolvido por José Maria Bezerra   ##
##    Uso exclusivo alunos Mecanismos UFPE/DEMEC   ##
#####################################################

from sympy import *
from IPython.display import HTML
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

def Newton(f,x):     # Raiz de f por Newton Raphson
    df = diff(f, θ)
    f, df = Lambda( θ, f ), Lambda( θ, df )
    while ( abs( f(x) ) > 0.001 ):
        x = x - f(x)/(df(x))
    return x

def bissect(f, L):
    f = Lambda( θ, f )

    a = L[0]; b = L[1]
    fa, fb = f(a), f(b)
    if ( fa*fb > 0 ):
        b += 0.1
    while abs(b-a) > 0.001:
        xm = (a+b)/2.0
        fm = f(xm)
        if fm*fa > 0.0:
            a,fa = xm,fm
        else:
            b,fb = xm,fm
    return a,b

θ = symbols('theta',real=True)

def GetElev(curva, h, β):
    if (curva == 'harmonica'):
        u = 0.5*h*( 1 - cos(pi*θ/β) )
    elif (curva == 'cicloide'):
        u = h*( θ/β - (1/(2*pi))*sin(2*pi*θ/β) )
    elif (curva == 'duplaharmonica'):
        u = 0.5*h*( 1 - cos(pi*θ/β) - 0.25*(1 - cos(2*pi*θ/β)) )
    elif (curva[0] in ['2','3','4']):
        curva = curva.replace('-',"")
        k = [int(i) for i in curva]
        if (len(k) == 2):
            a,b = k[0],k[1]
            u = h*(b*(θ/β)**a - a*(θ/β)**b)
        elif (len(k) == 3):
            a,b,c = k[0],k[1],k[2]
            u = 0.5*h*(b*c*(θ/β)**a - 2*a*c*(θ/β)**b + a*b*(θ/β)**c)
        elif (len(k) == 4):
            a,b,c,d = k[0],k[1],k[2],k[3]
            u = 0.5*h*( (1/3)*b*c*d*(θ/β)**a - a*c*d*(θ/β)**b + a*b*d*(θ/β)**c - (1/3)*a*b*c*(θ/β)**d )
    else:
        print('ERRO --> função '+curva+' inexistente')
        return 0
    return u

def OffSetMaxPressAngle(curva, h, β, φ̂, ε):
    u = GetElev(curva, h, β)
    v = diff(u,θ); a = diff(u,θ,2)

    uₜ = Lambda( θ, u )
    vₜ = Lambda( θ, v )

    Rₚ = 0.5*h;  ΔRₚ = 0.05
    Tφ = 1;  T = tan(φ̂)
    L = [0.2,β]
    while ( Tφ - T > 0.0001 ):
        Rₚ += ΔRₚ; R = sqrt( Rₚ*Rₚ - ε*ε )
        L = bissect( a*(u + R)-v*(v-ε), L); θₒ = L[0]
        Tφ = ( vₜ(θₒ)-ε )/( uₜ(θₒ)+R )

    φₘₐₓ = atan( (vₜ(θₒ)-ε)/( uₜ(θₒ)+sqrt(Rₚ*Rₚ-ε*ε) ) )
    Rᵢ = uₜ(θₒ)+sqrt( Rₚ*Rₚ - ε*ε )

    p = plot( atan((v-ε)/( u+sqrt(Rₚ*Rₚ-ε*ε) )), (θ,0,β), show=False, title='Ângulo de Pressão no intervalo [0,β]', xlabel='θ', ylabel='φ' )
    return N(Rₚ,5), N(Rᵢ,5), N(θₒ,5), N(φₘₐₓ,5), p

def GetMaxPressureAng(curva, h, β, φ̂):
    u = GetElev(curva, h, β)
    v = diff(u,θ); a = diff(u,θ,2)

    uₜ = Lambda( θ, u ); vₜ = Lambda( θ, v )

    Rₚ = 0.5*h;  ΔRₚ = 0.05
    Tφ = 1;  T = tan(φ̂)
    L = [0.2,β]
    while ( Tφ - T > 0.0001 ):
        Rₚ += ΔRₚ
        L = bissect( a*(u + Rₚ)-v*v, L); θₒ = L[0]
        Tφ = vₜ(θₒ)/( uₜ(θₒ)+Rₚ )

    φₘₐₓ = atan( vₜ(θₒ)/( uₜ(θₒ)+Rₚ ) )
    Rᵢ = uₜ(θₒ)+Rₚ

    p = plot( atan(v/(u+Rₚ)), (θ,0,β), show=False, title='Ângulo de Pressão no intervalo [0,β]', xlabel='θ', ylabel='φ' )
    return N(Rₚ,5), N(Rᵢ,5), N(θₒ,5), N(φₘₐₓ,5), p

def PhiAngleInformation(curva, h, β, φ̂, ε = 0):
    if (ε == 0):
        L = GetMaxPressureAng(curva, h, β, φ̂)
    else:
        L = OffSetMaxPressAngle(curva, h, β, φ̂, ε)

    print('Rₚ = '+str(L[0])+'\nRᵢ = '+str(L[1])+'\nθₒ = '+str(L[2])+' rad\nφₘₐₓ = '+str(L[3])+' rad')
    L[4].show()
    return 180*L[2]/pi, 180*L[3]/pi
    HTML('''<script> $('div .input').hide()''')