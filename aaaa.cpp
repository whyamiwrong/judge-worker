#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // 배열의 크기를 입력받음
    int n;
    cin >> n;

    // 주어진 배열을 저장할 벡터
    vector<int> R(n);

    // 배열의 요소들을 입력받음
    for (int i = 0; i < n; ++i) {
        cin >> R[i];
    }

    // 각 요소까지의 가장 긴 부분 수열의 길이를 저장할 배열
    vector<int> lis(n, 1);

    // 가장 긴 부분 수열의 길이를 찾음
    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (R[i] > R[j] && lis[i] < lis[j] + 1) {
                lis[i] = lis[j] + 1;
            }
        }
    }

    // lis 배열에서 가장 큰 값이 가장 긴 부분 수열의 길이
    int maxLength = *max_element(lis.begin(), lis.end());

    // 결과 출력
    cout << maxLength << endl;

    return 0;
}