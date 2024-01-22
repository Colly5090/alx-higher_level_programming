#include "list.h"
/**
 * is_palindrome -  A function to check palindrome
 * @head: the head pointer in the list
 * Return: 0 failed 1 sucess
 */
int is_palindrome(listint_t **head);
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, slow = *head;
	int is_palindrome = 1;
	listint_t *stack = NULL, *temp;

	if (!*head || !(*head)->next)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;

		temp = malloc(sizeof(listint_t));
		if (!temp)
		{
			while (stack)
			{
				temp = stack->next;
				free(temp);
				stack = temp;
			}
			return (-1);
		}
		temp->n = slow->n;
		temp->next = stack;
		stack = temp;

		slow = slow->next;
	}

	if (fast)
	{
		slow = slow->next;
	}

	while (slow)
	{
		temp = stack;
		stack = stack->next;

		if (temp->n != slow->n)
		{
			is_palindrome = 0;
			free(temp);
			break;
		}
		slow = slow->next;
		free(temp);
	}

	while (stack)
	{
		temp = stack->next;
		free(stack);
		stack = temp;
	}

	return (is_palindrome);
}
