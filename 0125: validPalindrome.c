bool isPalindrome(char* s) {
    
    int n = 0;
    for(int i = 0; s[i] != '\0'; i++){

        if( (s[i] >= 'A' && s[i] <= 'Z') || (s[i] >= 'a' && s[i] <= 'z') || (s[i] >= '0' && s[i] <= '9') ){

            n++;
        }
    }

    char* str = (char*)malloc(sizeof(char)*n);
    int cur = 0;
    for(int i = 0; s[i] != '\0'; i++){

        if(s[i] >= 'A' && s[i] <= 'Z'){

            str[cur] = s[i]-'A'+'a';
            cur++;
        }

        if((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= '0' && s[i] <= '9')){

            str[cur] = s[i];
            cur++;
        }
    }

    int i = 0;
    int j = n-1;
    while(i < j){

        if(str[i] != str[j]){

            return false;
        }
        i++;
        j--;
    }

    return true;
}