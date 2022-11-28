#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a
 * singly-linked list
 * @list: pointer to the list struct
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (!list)
		return (0);

	fast = list->next;
	slow = list;
	while (fast && slow && fast->next)
	{
		if (slow == fast)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
