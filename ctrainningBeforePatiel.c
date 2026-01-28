/*int match_from(const char pattern[], const char string[], int p_idx, int s_idx) {
    while (pattern[p_idx] != '\0') {
        if (pattern[p_idx] == '\\') { 
            p_idx++;
            if (pattern[p_idx] == '\0') return 1;
            if (pattern[p_idx] != string[s_idx]) return 1;
            p_idx++;
            s_idx++;
        } else if (pattern[p_idx] == '?') {
            if (string[s_idx] == '\0') return 1; 
            p_idx++;
            s_idx++;
        } else if (pattern[p_idx] == '*') {
            p_idx++;
            if (pattern[p_idx] == '\0') return 0;
            for (int i = s_idx; string[i] != '\0'; i++) {
                if (match_from(pattern, string, p_idx, i) == 0) return 0;
            }
            return 1; 
        } else {
            if (pattern[p_idx] != string[s_idx]) return 1;
            p_idx++;
            s_idx++;
        }
    }
    return string[s_idx] != '\0';
}
*/

#include <stdio.h>
int simple_fnmatch(const char pattern[], const char string[]) {
    int p_idx = 0;
    int s_idx = 0;
    while (pattern[p_idx] != '\0')
    {
        if (pattern[p_idx] == '*'){
            p_idx++;
            if (pattern[p_idx] == '\0') return 1;
            for(int i = s_idx; string[i] !='\0'; i++){
                if(simple_fnmatch(pattern+p_idx,string+i) == 1) {
                    return 1;
                }
            }
            return 0;
        }else if (pattern[p_idx] == '\\'){
            p_idx++;
            if (pattern[p_idx] != string[s_idx])
            {
                return 0;
            }
            p_idx++;
            s_idx++;
        }else if (pattern[p_idx] == '?'){
            if (string[s_idx] == '\0') return 0;

            p_idx++;
            s_idx++;
        }
        else{
            if (pattern[p_idx] != string[s_idx])
            {
                return 0;
            }
            p_idx++;
            s_idx++;
        }
    }

    return 1;
}


int main(){
    printf("%d\n", simple_fnmatch("*12", "I12"));
    printf("%d\n", simple_fnmatch("I have to fai?l", "I have to faiql"));

}