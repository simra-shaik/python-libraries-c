int add_numbers(int a, int b) {
    return a + b;
}

double calculate_average(int *numbers, int length) {
    double sum = 0;

    for (int i = 0; i < length; i++) {
        sum += numbers[i];
    }

    return sum / length;
}