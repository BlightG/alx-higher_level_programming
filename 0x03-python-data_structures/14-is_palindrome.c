#include "lists.h"
/**
 *
 *
*/
int count(listint_t **head);
int count(listint_t **head)
{
	int count;
	listint_t *temp;

	temp = *head;
	count = 1;
/*	if (head == NULL)
		return (0);*/
	while (temp != NULL)
	{
		count++;
		temp = temp->next;
	}
	return (count);
}
/**
 *
 *
*/
void assigncomp(listint_t **head, int* compare);
void assigncomp(listint_t **head, int* compare)
{
	int i;
	listint_t *temp;

	i = 0;
	temp = *head;
/*	if (head == NULL)
		exit(0);*/
	while (temp != NULL)
	{
		compare[i] = temp->n;
		*head = temp->next;
		i++;
	}
}
/**
 *
 *
*/
int is_palindrome(listint_t **head)
{
	int i, lenght;
	int *compare;

/*	if (*head == NULL)
		return (0);*/

	printf("got to is_palindrome");
	lenght = count(head);
	compare = malloc(sizeof(char) * lenght);
	if (compare == NULL)
	{
		free(compare);
		return (0);
	}
	assigncomp(head, compare);
	for (i = 0 ; i <= lenght/2 ; i++)
		if (compare[i] == compare[lenght - i])
			continue;
		else
			return (0);
	free(compare);
	return (1);
}
