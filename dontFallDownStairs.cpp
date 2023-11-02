#include <iostream>
#include <vector>

using namespace std;

int main() {

  vector<int> steps;
  int n;
  int ans = 0;
  cin >> n;
  for(int i = 0; i < n; i++){

    int temp;
    cin >> temp;
    steps.push_back(temp);
  }

  for(int i = 0; i < n-1; i++){

    while(steps[i] -steps[i+1] > 1){
      ans++;
      steps[i]--;
      continue;
    }
  }

  int l = steps.size()-1;
  while(steps[l] > 1){
    steps[l]--;
    ans++;
  }

  cout << ans <<endl;
  return 0;
}