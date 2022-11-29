#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: list head
 * @number: number to store in the new node
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *fast;
	listint_t *new;

	fast = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (fast->next != NULL)
	{
		if ((fast->next)->n >= number)
		{
			new->next = fast->next;
			fast->next = new;
			return (new);
		}
		fast = fast->next;
	}

	new->next = NULL;
	fast->next = new;
	return (new);
}
