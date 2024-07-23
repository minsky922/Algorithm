#include <vector>

using namespace std;

void mapping(vector<int> &hash, const vector<int> &arr, int target) {
  for (int i = 0; i < arr.size(); i++) {
    if (arr[i] > target) continue;
    hash[arr[i]] =
        1;  // 현재 원소값을 hash 인덱스로 활용, 해당 위치의 값을 1로 설정
  }
}
bool solution(vector<int> arr, int target) {
  vector<int> hash(target + 1, 0);  // target+1 공간이 있는 hashvector 선언
  mapping(hash, arr, target);  // arr 원소값에 대하여 해시테이블 생성
  for (int i = 0; i < arr.size(); i++) {
    int num = target - arr[i];
    if (arr[i] == num) continue;
    if (num < 0) continue;
    if (hash[num]) return true;
  }
  return false;
}