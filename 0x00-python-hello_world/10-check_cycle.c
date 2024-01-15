#include "lists.h"
/**
 * check_cycle - A function to track cycle in a linked list
 * @list: the linked list to track
 * Return: 1 cycle found 0 cycle not found
 */
int check_cycle(listint_t *list)
{
	listint_t *black = list;
	listint_t *white = list;

	if (list == NULL)
		return (0);

	while (black && white && white->next)
	{
		black = black->next;
		white = white->next->next;
		if (black == white)
			return (1);
	}
	return (0);
}
