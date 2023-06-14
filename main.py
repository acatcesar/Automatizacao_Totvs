
import subprocess
import time
import pandas as pd
import pyautogui

pyautogui.FAILSAFE = True

def encontrar_imagem(imagem):
    while not pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9):  # reconhecimento de imagem
        time.sleep(1)
    encontrou = pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9)
    return encontrou

def direita(posicoes_imagem):
    return posicoes_imagem[0] + posicoes_imagem[2], posicoes_imagem[1] + posicoes_imagem[3]/2

#Abrir o ERP (Tovs)
subprocess.Popen([r"C:\Teste Totvs\RM.exe"])

encontrou = encontrar_imagem("totvsaberto.png")



#Fazer Login
encontrou= encontrar_imagem(("senha2.png"))
pyautogui.click(pyautogui.center(encontrou))
pyautogui.write("")
encontrou = encontrar_imagem(("Entrar.png"))
pyautogui.click(pyautogui.center(encontrou))


#Entrar no produto e servico
encontrou= encontrar_imagem(("prodser.png"))
pyautogui.click(pyautogui.center(encontrou))

#Escolher filtro
encontrou= encontrar_imagem(("todos.png"))
pyautogui.click(pyautogui.center(encontrou))
encontrou= encontrar_imagem(("executar.png"))
pyautogui.click(pyautogui.center(encontrou))


# preenchendo campos
tabelas_produtos = pd.read_excel("codtotvs.xlsx")
print(tabelas_produtos)

for linha in tabelas_produtos.index:
    # incluir
    encontrou = encontrar_imagem(("incluir.png"))
    pyautogui.click(pyautogui.center(encontrou))

    codprod = tabelas_produtos.loc[linha, "codprod"]
    codauxiliar = tabelas_produtos.loc[linha, "codauxiliar"]
    nomefantasia = tabelas_produtos.loc[linha, "nomefantasia"]
    coddes = tabelas_produtos.loc[linha, "coddes"]
    classi = tabelas_produtos.loc[linha, "classi"]

    pyautogui.write(str(codprod))
    pyautogui.press("tab")
    pyautogui.write(str(codauxiliar))
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("space")
    pyautogui.press("tab")
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.write(str(nomefantasia))

    # detalhes

    encontrou= encontrar_imagem(("detalhes2.png"))
    pyautogui.click(pyautogui.center(encontrou))
    pyautogui.press("tab")
    pyautogui.press("tab")
    encontrou= encontrar_imagem(("descricaoprod.png"))
    pyautogui.click(pyautogui.center(encontrou))


    #coddes = tabelas_produtos.loc[linha, "coddes"]
    pyautogui.write(str(coddes))
    encontrou= encontrar_imagem(("classi.png"))
    pyautogui.click(pyautogui.center(encontrou))
    pyautogui.press("tab")
    #classi = tabelas_produtos.loc[linha, "classi"]
    pyautogui.write(str(classi))
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.press("tab")
    # encontrou= encontrar_imagem(("salvar.png"))
    # pyautogui.click(pyautogui.center(encontrou))

    time.sleep(1)
    # Controle de estoque

    encontrou = encontrar_imagem(("controle.png"))
    pyautogui.click(pyautogui.center(encontrou))

    pyautogui.press("tab")
    pyautogui.write("UN")
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.write("UN")
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.write("UN")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.press("enter")
    pyautogui.press("tab")
    time.sleep(2)


    #Informações filial

    encontrou = encontrar_imagem(("inf.png"))
    pyautogui.click(pyautogui.center(encontrou))
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.press("up")
    time.sleep(2)
    pyautogui.press("enter")
    pyautogui.write("88")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.press("tab")
    time.sleep(2)

    encontrou = encontrar_imagem(("ok.png"))
    time.sleep(2)
    pyautogui.click(pyautogui.center(encontrou))
    time.sleep(2)
    encontrou = encontrar_imagem(("ok.png"))
    time.sleep(2)
    pyautogui.click(pyautogui.center(encontrou))











# pyautogui.press("tab") # 1 tecla só e hotkey multiplas teclas





# encontrou = encontrar_imagem(("login1.png"))


# pyautogui.click(pyautogui.center(encontrou))

# Abrir o ERP (Tovs)
#subprocess.Popen([r"C:\Teste Totvs\RM.exe"])


#while not pyautogui.locateOnScreen("login1.png", grayscale=True, confidence=0.9):
 #   time.sleep(1)
#encontrou = pyautogui.locateOnScreen("login1.png", grayscale=True, confidence=0.9)

#print(encontrou)
# while not pyautogui.locateOnScreen("login1.png", grayscale=True, confidence=0.9)

# Clicar no menu Produtos e Serviços

# Escolher um filtro(todos)


# Clicar no menu incluir
