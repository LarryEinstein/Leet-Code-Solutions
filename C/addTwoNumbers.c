#include <stdio.h>
#include <stdlib.h>

int main() {

    int universe_answer = 42;

    printf("The answer to the universe is: %i \n", universe_answer);
    printf("It's location in memory is: %p \n", &universe_answer);

    char hello[] = "Hi Beeblebrox";

    char *str = malloc(4); //malloc = allocate memory

    str[0] = 'h';
    str[1] = 'e';
    str[2] = 'y';
    str[3] = '\0';

    // all done now

    free(str);

    return 0;
}