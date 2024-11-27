#include <stdio.h>
#define LEN_INPUT 1000001  // 최대 입력 길이 정의 (1,000,000 + 1 for NULL character)

int main(void) {
    char s1[LEN_INPUT];  // 입력 문자열 저장 공간
    
    // 문자열 입력
    scanf("%1000000s", s1);  // 최대 1,000,000자까지 입력받음
    
    // 입력된 문자열 출력
    printf("%s\n", s1);

    return 0;
}
