
//Ejemplo scanf#include <stdio.h>
#include<stdio.h>

int main()
{
int n;  
int A = 0;
int B = 1;
int i = 0;
int C = 0;
int d = 0;

printf("=================================================\n");
printf("            Serie de Fibonacci                  \n");
printf("=================================================\n\n");


printf("Cuantos numeros de Fibonacci deseas: \n");
scanf("%i",&n);

if (n==1) 
    printf("El números de la serie Fibonacci es: \n %i",A);
if (n==2)
    printf("Los números de la serie Fibonacci son: \n %i %i",A, B);     
if (n >= 3)
    {
    d = n-2;
    printf("Los números de la serie Fibonacci son: \n %i %i ",A, B);  
    for(i=1; i <= d ; i++)
        {
        C = A + B;
        printf("%i ", C);
        A = B;
        B = C;    
        }
    }
printf("\n\nEl numero que escribistes es %i",n);


printf("\n\n\n=================================================\n");
printf("           Hasta pronto                         \n");
printf("=================================================\n\n");


return 0;
}
