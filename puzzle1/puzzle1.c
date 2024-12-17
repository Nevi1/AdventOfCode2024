/*
** EPITECH PROJECT, 2024
** AdventOfCode2024 [WSL: Ubuntu]
** File description:
** puzzle1
*/

#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>
#include <stdlib.h>

char **str_to_word_array(char *str, char *sep);

int arr_len(char **array)
{
    int i = 0;

    for (; array[i]; i++);
    return i;
}

void free_array(char **array)
{
    for (int i = 0; array[i]; i++)
        free(array[i]);
    free(array);
}

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int swap_list(int *tab, int start, int end)
{
    int i = start;
    int j = end;
    int pivot = tab[start];

    while (i < j) {
        while (tab[i] <= pivot && i <= end - 1)
            i++;
        while (tab[j] > pivot && j >= start + 1)
            j--;
        if (i < j)
            swap(&tab[i], &tab[j]);
    }
    swap(&tab[start], &tab[j]);
    return j;
}

void quick_sort(int *tab, int start, int end)
{
    int pivot = 0;

    if (start < end) {
        pivot = swap_list(tab, start, end);
        quick_sort(tab, start, pivot - 1);
        quick_sort(tab, pivot + 1, end);
    }
}

int parse_input(char *content)
{
    char **array = str_to_word_array(content, "\n");
    char **line = NULL;
    int *tab1 = malloc(sizeof(int) * (arr_len(array) + 1));
    int *tab2 = malloc(sizeof(int) * (arr_len(array) + 1));
    int i = 0;
    int total = 0;

    for (; array[i]; i++) {
        line = str_to_word_array(array[i], " ");
        tab1[i] = atoi(line[0]);
        tab2[i] = atoi(line[1]);
        free_array(line);
    }
    quick_sort(tab1, 0, arr_len(array) - 1);
    quick_sort(tab2, 0, arr_len(array) - 1);
    for (i = 0; i < arr_len(array); i++) {
        total += abs(tab1[i] - tab2[i]);
    }
    free_array(array);
    free(tab1);
    free(tab2);
    return total;
}

int main(void)
{
    int file = open("input.txt", O_RDONLY);
    struct stat sb;
    char *content;

    if (file == -1)
        return 1;
    if (fstat(file, &sb) == -1)
        return 1;
    content = malloc(sb.st_size);
    if (read(file, content, sb.st_size) != sb.st_size)
        return 1;
    printf("%d\n", parse_input(content));
    free(content);
    close(file);
    return 0;
}