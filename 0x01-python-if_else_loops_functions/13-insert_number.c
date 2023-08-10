#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node into a linked list
 * @head: pointer to pointer to head node
 * @number: the number to be inserted
 *
 * Return: the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *curr = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
	}
	else if (curr->n > number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		while (curr->next != NULL && curr->next->n < number)
			curr = curr->next;
		new->next = curr->next;
		curr->next = new;
	}
	return (new);
}
