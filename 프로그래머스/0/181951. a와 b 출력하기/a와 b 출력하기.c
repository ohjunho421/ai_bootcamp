#include <stdio.h>

int main(void) {
    int a, b;

    // 사용자 입력
    scanf("%d %d", &a, &b);

    // 조건 확인
    if (a < -100000 || a > 100000 || b < -100000 || b > 100000) {
        return 1;  // 프로그램 종료
    }

    // 결과 출력
    printf("a = %d\n", a);
    printf("b = %d\n", b);

    return 0;
}
