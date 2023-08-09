#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks for cycles in a linked list
 * @list: head node of the list to be searched
 *
 * Return: 0 no cycle, 1 cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = NULL;

	if (list == NULL || list->next == NULL)
		return (0);
	fast = list->next;

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
