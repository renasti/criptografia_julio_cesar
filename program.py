`def decodificaTexto(textoParaDecifrar,qtdCasasDecifrar):
    
    #Parametros de uso
    alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    tamanhoTextoCifrado = len(textoParaDecifrar); 
    tamanhoAlfabeto = len(alfabeto)
    textoDecifrado = ''
    letraEncontrada = ''
    resumoCriptografico = ''
    
    #Decifra texto
    for x in range(tamanhoTextoCifrado):

        for y in range(tamanhoAlfabeto):

            if textoParaDecifrar[x] == alfabeto[y]:
                posAtual = y; 
                posFinal = posAtual - qtdCasasDecifrar
                
                if(posFinal < 0):
                    posFinal = len(alfabeto) - abs(posFinal)
                    letraEncontrada = alfabeto[posFinal]
                else:
                    letraEncontrada = alfabeto[posFinal]

            elif ( textoParaDecifrar[x] == " " ):
                letraEncontrada = " "
                        
            elif( textoParaDecifrar[x] == "."):
                letraEncontrada = "."
            
        #Incrementa o texto decifrado em cada interação
        textoDecifrado = textoDecifrado + letraEncontrada
    
    #Criptografa o texto decifrado em sha1
    resumoCriptografico = hashlib.sha1(textoDecifrado.encode())
    
    #Criar json resultado
    dados = {
        "texto_decifrado" : textoDecifrado,
        "resumo_criptografico" : resumoCriptografico.hexdigest()
    }

    python2json = json.dumps(dados)
    return (python2json)
