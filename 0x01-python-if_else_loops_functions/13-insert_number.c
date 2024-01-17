#include "lists.h"
/**
 * *insert_node - A function to insert node
 * @head: the head pointer to begin
 * @number: the number in the list
 * Return: 0 success
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *previous;

	new_node = (listint_t *)malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		current = *head;
		while (current != NULL && current->n < number)
		{
			previous = current;
			current = current->next;
		}
		previous->next = new_node;
		new_node->next = current;
	}
	return (new_node);
}
