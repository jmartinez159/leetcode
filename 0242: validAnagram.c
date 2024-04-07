bool isAnagram(char* s, char* t) {
    int sSize = 0;
    int tSize = 0;
    int chars[26];
    for(int i = 0; i < 26; i++){

        chars[i] = 0;
        char cur = 'a' + i;
    }

    for(int i = 0; s[i] != '\0'; i++){

        int index = s[i] - 'a';
        chars[index]++;
    }

    for(int i = 0; t[i] != '\0'; i++){

        int index = t[i] - 'a';
        chars[index]--;
    }

    for(int i = 0; i < 26; i++){

        if(chars[i] != 0){

            return false;
        }
    }

    return true;
}