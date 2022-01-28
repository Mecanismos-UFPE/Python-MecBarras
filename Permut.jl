function Compute_Var_Livres(n)
    global k; global n₂; global n₃
    n₂, n₃ = 4, 2*k - 4
    for i in 1:k-3
        n₂ += (i)*n[i]
        n₃ -= (i+1)*n[i]
    end
    n₃ < 0 ? false : true
end

function Verify(N)
    if N % 2 ≠ 0 || N < 4
        println("n tem que ser par e maior ou igual a 4")
        return false
    elseif N == 4
        println("Permutação Única - ",[4, 0])
        return false
    elseif N == 6
        println("Permutação Única - ",[4, 2])
        return false
    end
    true
end

function Show_Combines(N)
    Verify(N) ? p=1 : return     # Inicia Contador de permutações

    global k; global n₂; global n₃
    k = N >> 1                   # k = n/2 da teoria
    orig = collect(0:k-2)        # Vetor [n4,...,nk]
    aux = [1 for i in 1:k-2]     # Auxilia na troca dos elementos
    aux[end] = 0                 # e encerra o while
    v_livre = [0 for i in 1:k-3] # Variáveis livres em cada set.
    
    print("  PERMUTAÇÃO   |n₂-n₃|n4")
    println(join(["-n$(i)" for i in 5:k]),"|")
    println(join(["---" for i in 1:k+4]))
    
    while aux[end] == 0
        for i in [1:k]
            for j in 1:k-3                    # preenche o vetor das
                v_livre[k-2-j] = orig[aux[j]] # variáveis livres
            end
            if Compute_Var_Livres(v_livre)
                println("Permutação ",p," - ",append!([n₂,n₃],v_livre))
                p += 1
            end
            aux[1] += 1
        end
        for i in 1:k-3                    # efetua as permutações
            if aux[i] == k                # no vetor aux.
                aux[i] = 1
                aux[i+1] += 1
            end
        end
    end
end