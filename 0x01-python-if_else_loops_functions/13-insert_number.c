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
		*head->next = NULL;
		free(curr);
		return (*head);
	}
	prev = *head;
	nxt = prev->next;
	while(nxt != NULL)
	{
		if (nxt->n >= number) 	
		{
			prev->next = curr;
			curr->next = nxt;
			break;
		}
		else
		{
			prev = prev->next;
			nxt = nxt->next;
		}
	}
	return(curr);
}
