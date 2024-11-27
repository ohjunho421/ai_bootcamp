#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num, int n) {
    // num이 n의 배수인지 확인
    if (num % n == 0) {
        return 1;  // n의 배수라면 1 반환
    } else {
        return 0;  // n의 배수가 아니라면 0 반환
    }
}

int main(void) {
    int num, n;

    // 사용자 입력
    printf("num과 n을 입력하세요 (2 ≤ num ≤ 100, 2 ≤ n ≤ 9): ");
    scanf("%d %d", &num, &n);

    // 조건 확인
    if (num < 2 || num > 100 || n < 2 || n > 9) {
        printf("입력값이 조건을 만족하지 않습니다.\n");
        return 1;  // 비정상 종료
    }

    // solution 함수 호출 및 결과 출력
    int result = solution(num, n);
    printf("결과: %d\n", result);

    return 0;
}
