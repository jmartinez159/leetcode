class MyQueue {
public:

    stack<int> main;
    stack<int> getter;
    MyQueue() {

    }
    
    void push(int x) {
        
        main.push(x);
    }
    
    int pop() {

        /*
        main = 4 5 6
        getter = 3   
        */    
        int ans = peek(); 
        getter.pop();
        
        return ans;
    }
    
    int peek() {
        

        if(getter.empty()){

            while(!main.empty()){

                getter.push(main.top());
                main.pop();
            }
        }

        return getter.top();
    }
    
    bool empty() {
        
        return main.empty() && getter.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
