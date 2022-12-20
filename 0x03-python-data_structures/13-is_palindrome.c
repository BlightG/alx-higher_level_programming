#include "lists.h"
listint_t *reversed(listint_t **head);
listint_t *reversed(listint_t **head)
{
	listint_t *prev, *curr, *next;

	curr = *head;
	prev = NULL;
	/*printf("print");*/
	while (curr->next != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;

	}
	curr->next = prev;
	return (curr);
}
int is_palindrome(listint_t **head)
{
	listint_t *reverse;

	reverse = reversed(head);
	print_listint(reverse);
	return (0);
}
