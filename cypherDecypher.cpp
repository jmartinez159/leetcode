#include <iostream>
#include <vector>

using namespace std;

int main() {

  string kphrase;
  int n;
  cin >> kphrase;
  cin >> n;
  vector<string> words;
  for (int i = 0; i < n; i++) {
    string temp;
    cin >> temp;
    words.push_back(temp);
  }

  for(int i =0; i < n; i++){

    for(int j = 0; j < kphrase.size(); j++){

      int pos = words[i][j] - 'A';
      int mv = (pos*(kphrase[j] - '0'))%26;
      words[i][j] = mv + 'A';
    }
  }

  for(int i = 0; i < n; i++){

    cout << words[i] <<endl;
  }
  
  return 0;
}