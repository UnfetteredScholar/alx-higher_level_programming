#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: the head of the linked list to be checked
 *
 * Return: 1 for palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i = 0, j = 0;
	int *arr = NULL;
	listint_t *curr = *head;

	if (*head == NULL)
		return (1);
	/* find length of linked list */
	while (curr != NULL)
	{
		len++;
		curr = curr->next;
	}
	arr = malloc(sizeof(int) * len);
	if (arr == NULL)
		exit(1);
	curr = *head;
	while (curr != NULL)
	{
		arr[i++] = curr->n;
		curr = curr->next;
	}
	for (i = 0, j = len - 1; i < j; i++, j--)
	{
		if (arr[i] != arr[j])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
