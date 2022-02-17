#include<stdio.h>
#include<stdlib.h>
struct student{
char name[20];
char city[20];
char dept[10];
};
void write(struct student s);
void write(struct student s){


FILE *fptr1;
fptr1=fopen("test1.txt","w");
if(fptr1==NULL)
{
printf("error in opening file\n");
exit(0);
}
struct student s1 ={"pranee","banglore","ece"};
fwrite(&s1,sizeof(struct student),1,fptr1);
if(fwrite!=NULL)
printf("successfully content is written\n");
else
printf("error in opening file\n");
fclose(fptr1);
}
void read(struct student s);
void read(struct student s){
    FILE *fptr2;
    fptr2=fopen("test1.txt","r");
    if(fptr2==NULL)
    {
        printf("error in opening file\n");
        exit(1);
    }
     fread(&s,sizeof(struct student),1,fptr2);
     printf("\n name=%s\n city=%s\n dept=%s\n",s.name,s.city,s.dept);
     fclose(fptr2);
}
int main()
{
struct student s;
write(s);
read(s);
}

