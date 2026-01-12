import webbrowser
import os
import platform

# --- CONFIGURAÇÃO DO SEU WORKSPACE ---
# Aqui você pode adicionar os caminhos dos programas do seu Nitro V15 depois
opcoes = {
    "1": ("ArchDaily (Inspiração)", "https://www.archdaily.com.br"),
    "2": ("Pinterest (Plantas e Cortes)", "https://www.pinterest.com"),
    "3": ("BIMobject (Objetos 3D)", "https://www.bimobject.com"),
    "4": ("AutoCAD / Revit", "C:/Caminho/Para/Seu/Programa.exe"), 
    "5": ("Pasta de Projetos (Local)", "C:/Users/Documentos/Arquitetura"),
    "6": ("YouTube (Tutoriais de Render)", "https://www.youtube.com")
}

def exibir_menu():
    print("\n" + "="*30)
    print("📐 LANÇADOR DE ARQUITETURA 📐")
    print("="*30)
    for tecla, (nome, _) in opcoes.items():
        print(f"[{tecla}] - {nome}")
    print("[0] - Sair")
    print("="*30)

def iniciar():
    while True:
        exibir_menu()
        escolhas = input("\nEscolha os números (ex: 1 2 6) e aperte ENTER: ").split()
        
        if '0' in escolhas:
            print("Encerrando lançador... Bom trabalho!")
            break
            
        for num in escolhas:
            if num in opcoes:
                nome, destino = opcoes[num]
                print(f"🚀 Abrindo: {nome}...")
                
                # Se for link (http), abre no navegador. Se não, tenta abrir como arquivo/app.
                if destino.startswith("http"):
                    webbrowser.open(destino)
                else:
                    # Verifica se o caminho do arquivo existe antes de tentar abrir
                    if os.path.exists(destino):
                        os.startfile(destino)
                    else:
                        print(f"⚠️ Configure o caminho do {nome} no seu novo PC!")
        
        input("\n✅ Comandos enviados! Pressione Enter para voltar ao menu...")

if __name__ == "__main__":
    iniciar()
