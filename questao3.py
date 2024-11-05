def main():
    faturamento_diario = 0
    menor_faturamento = min(faturamento_diario) 
    maior_faturamento = max(faturamento_diario) 
    dias_com_faturamento = len([f for f in faturamento_diario if f > 0]) 
    media_faturamento = sum(faturamento_diario)/(dias_com_faturamento) 
    print("Faturamento diário %d")
    if dias_com_faturamento > 0:
        print("Faturamento")
    else: 0 
    dias_acima_media = len([f for f in faturamento_diario if f > media_faturamento])

    print(f"Menor valor de faturamento: R${menor_faturamento}", menor_faturamento) 
    print(f"Maior valor de faturamento: R${maior_faturamento}") 
    print(f"Número de dias com faturamento superior à média mensal: {dias_acima_media}" )
    
    if __name__ == "__main__": main() 
