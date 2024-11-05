#include <stdio.h>
#include <string.h>
int main()
{
    float faturamento_mensal;
    char estado[2];
    float faturamento_total;
    float percentual;
    printf("Qual estado?");
    scanf("%s", estado);
    if (estado == "SP")
    faturamento_mensal = 67.836,43;
    else if (estado == "RJ")
    faturamento_mensal = 36.678,66;
    else if (estado == "MG")
    faturamento_mensal = 29.229,88;
    else if (estado == "ES")
    faturamento_mensal = 27.165,48;
    else
    faturamento_mensal = 19.849,53;
    faturamento_total=180.759,98;
    percentual=(faturamento_mensal/faturamento_total)*100;
    printf("%f", percentual);
    return 0; 
}
