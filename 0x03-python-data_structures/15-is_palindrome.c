#include "lists.h"
/**
 * count - counts the number of nodes
 *
 * @head: a 2d pointer to head of a structure
 *
 * Return: returns the number of noedes in a strucutre
*/
int count(listint_t **head);
int count(listint_t **head)
{
	int count;
	listint_t *temp;

	temp = *head;
	count = 0;
	if (head == NULL)
		return (0);
	while (temp != NULL)
	{
		count++;
		temp = temp->next;
	}
	return (count);
}
/**
 * assigncomp - copies values of n from a stuct to int pointer
 *
 * @head: double pointer to head of a stuct to be copied
 * @compare: int pointer to store values from struct
 *
*/
void assigncomp(listint_t **head, char *compare);
void assigncomp(listint_t **head, char *compare)
{
	int i;
	listint_t *temp;

	i = 0;
	temp = *head;
	while (temp != NULL)
	{
		compare[i] = temp->n;
		temp = temp->next;
		i++;
	}
	free(temp);
}
/**
 * is_palindrome -a function in C that checks if a singly linked
 *                list is a palindrome.
 *
 * @head: a pointer to head of the stuct
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	int i, lenght;
	char *compare;

	lenght = count(head);
	compare = malloc(sizeof(char) * lenght);
	if (compare == NULL)
	{
		free(compare);
		return (0);
	}
	assigncomp(head, compare);
	for (i = 0 ; i <= lenght / 2 ; i++)
	{
		if (compare[i] == compare[lenght - i - 1])
			continue;
		else
			return (0);
	}
	free(compare);
	return (1);
}
