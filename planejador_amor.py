import datetime

def contador_especial(data_inicio):
    hoje = datetime.date.today()
    diferenca = hoje - data_inicio
    
    anos = diferenca.days // 365
    meses = (diferenca.days % 365) // 30
    dias = (diferenca.days % 365) % 30
    
    return anos, meses, dias

def exibir_planejador():
    # --- AJUSTE AQUI A DATA DO SEU NAMORO (Ano, Mês, Dia) ---
    data_namoro = datetime.date(2025, 12, 28) 
    
    anos, meses, dias = contador_especial(data_namoro)

    print("\n" + "💖 " * 10)
    print("      NOSSO MOMENTO      ")
    print("💖 " * 10)
    
    print(f"\n💌 Estamos juntos há:")
    print(f"👉 {anos} Anos, {meses} Meses e {dias} Dias.")
    
    print("\n" + "─" * 30)
    print("🌟 IDEIAS PARA SURPREENDER:")
    print("• Noite de Fondue ou Pizza em casa")
    print("• Enviar um lanche/doce surpresa no trabalho/casa")
    print("• Bilhete escrito à mão (clássico nunca falha)")
    
    print("\n🎁 LISTA DE DESEJOS (Dela):")
    # Você pode editar essa lista sempre que ela comentar que gostou de algo
    print("- Perfume que ela mencionou")
    print("- Aquela joia/acessório do Instagram")
    print("- Viagem para o lugar X")
    print("\n" + "─" * 30)
    
    input("\nPressione Enter para fechar...")

if __name__ == "__main__":
    exibir_planejador()
