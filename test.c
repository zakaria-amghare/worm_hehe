#include <stdio.h>
#include <stdlib.h>
int main()
{
    FILE *f;
    
    f=fopen("the_hehe_file.c","w");
    fprintf(f,"#include <stdio.h>\n");
    fprintf(f,"int main(){\n");
    fprintf(f,"printf(\"hehe\");}\n");

    fclose(f);
    int c = system("gcc the_hehe_file.c -o the_hehe_file.exe");
    if (c != 0)
    {
     printf("sorry ....");
     return 0;   /* code */
    }
    
    system("the_hehe_file.exe");
    printf("miwmiw");

}