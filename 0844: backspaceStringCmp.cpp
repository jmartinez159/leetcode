class Solution {
public:
    bool backspaceCompare(string s, string t) {
        
        stack<char> s1;
        stack<char> s2;
        for(int i = 0; i<s.size(); i++){
            if(s[i] == '#' && !s1.empty()){
                s1.pop();
            }
            else{
                s1.push(s[i]);
            }
        }
        for(int i = 0; i<t.size(); i++){
            if(t[i] == '#' && !s2.empty()){
                s2.pop();
            }
            else{
                s2.push(t[i]);
            }
        }

        string a = "";
        string b = "";
        while(!s1.empty()){
            if(s1.top() == '#'){
                s1.pop();
                continue;
            }
            a += s1.top();
            s1.pop();
        }
        cout << a <<endl;
        while(!s2.empty()){
            if(s2.top() == '#'){
                s2.pop();
                continue;
            }
            b += s2.top();
            s2.pop();
        }
        cout<<b<<endl;

        return a==b;
    }
};