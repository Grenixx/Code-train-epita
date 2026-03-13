#include <stdio.h>
#include <time.h>
#include <unistd.h>

void progress_bar(long long current, long long total)
{
    // depart de la clock a 0 pour init toujour demarer progressbar a 0
    static time_t start;
    if (current == 0) {
        start = time(NULL);
    }
    time_t currtime = time(NULL);
    unsigned long secondPastsinceStart = (unsigned long) difftime(current, start);
    
    static int last_percent = -1;
    int percent = (int)((current * 100) / total);
    if (current >= total)
        percent = 100;
    if (percent == last_percent)
        return;
    last_percent = percent;

    int width = 30;
    int filled = (int)((current * width) / total);

    printf("\r[");
    for (int i = 0; i < width; i++)
        printf(i < filled ? "O" : "-");
    printf("] %3d%% %lu", percent, secondPastsinceStart);
    fflush(stdout);
}

int main(){
    for (int i = 0; i<100000; i++){
        progress_bar(i,100000);
    }
}

/*void progress(int current, int total)
{
    int percent = (current * 100) / total;
    printf("\rProgress: %3d%%", percent);
    //fflush(stdout);
}*/
/*
void progress_bar(int current, int total)
{
    int width = 30;
    int filled = (current * width) / total;

    printf("\r[");
    for (int i = 0; i < width; i++)
        printf(i < filled ? "O" : "-");
    printf("] %3d%%", (current * 100) / total);
    fflush(stdout);
}
*/

/*void progress_bar(long long current, long long total)
{
    static int last_percent = -1;
    int percent = (int)((current * 100) / total);
    if (percent == last_percent)
        return;
    last_percent = percent;

    int width = 30;
    int filled = (int)((current * width) / total);

    printf("\r[");
    for (int i = 0; i < width; i++)
        printf(i < filled ? "O" : "-");
    printf("] %3d%%", percent);
    fflush(stdout);
}*/