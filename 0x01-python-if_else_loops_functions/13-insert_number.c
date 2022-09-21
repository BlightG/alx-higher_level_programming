#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *nxt, *prev;

	curr = malloc(sizeof(listint_t));
	if (curr == NULL && head == NULL)
	{
		free(curr);
		return(NULL);
	}
	curr->n = number;
	if (*head == NULL)
	{
		*head = curr;
		curr->next = NULL;
		return (*head);
	}
	prev = *head;
	nxt = prev->next;
	if (prev->n >= number)
	{
		*head = curr;
		curr->next = prev;
		return(curr);
	}
	while(prev != NULL)
	{
		if (nxt == NULL)
		{
			prev->next = curr;
			curr->next = nxt;
			break;
		}
		else if (nxt->n >= number) 	
		{
			prev->next = curr;
			curr->next = nxt;
			break;
		}
		else if (nxt->n < number) 	
		{
			prev = prev->next;
			nxt = nxt->next;
		}
	}
	return(curr);
}
